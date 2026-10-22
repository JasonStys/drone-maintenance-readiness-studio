"""Jason Stys: independent readiness boundaries, unknown propagation, clock and planning oracles. Lines: docs/SOURCE_MAP.md."""

import copy
import time

import pytest

from workbench.engine import active_policy, evaluate, indexes, worst
from workbench.models import Assumptions


def result(state, assumptions, at=None):
    """Evaluate deterministic private fixture and select the known flood battery result."""
    report = evaluate(state, time.time() if at is None else at, assumptions)
    return report, next(p for p in report["components"] if p["id"] == "flood-battery")


def test_three_realistic_synthetic_states(state, assumptions):
    """Known fixture expectations are independent of engine-derived statuses."""
    report, part = result(state, assumptions)
    assert {a["id"]: a["status"] for a in report["aircraft"]} == {
        "flood": "within_recorded_limits",
        "inspection": "blocked",
        "training": "unknown",
    }
    assert part["remaining_seconds"] == 356400 and part["remaining_cycles"] == 196
    assert part["planning_days_to_usage_limit"] == 98.0
    assert report["flight_authorization"] is False
    assert report["status"] == "blocked"


@pytest.mark.parametrize(
    "seconds,cycles,status,code",
    [
        (359999, 199, "review", "time_near_limit"),
        (360000, 199, "blocked", "time_limit"),
        (360001, 199, "blocked", "time_limit"),
        (1, 200, "blocked", "cycles_limit"),
        (1, 180, "review", "cycles_near_limit"),
        (323999, 179, "within_recorded_limits", None),
        (324000, 1, "review", "time_near_limit"),
    ],
)
def test_exact_life_and_warning_boundaries(state, assumptions, seconds, cycles, status, code):
    """At a hard limit is blocked; warning fraction uses exact integer comparison, not rounding."""
    part = next(p for p in state["components"] if p["id"] == "flood-battery")
    part.update(seconds=seconds, cycles=cycles)
    _, actual = result(state, assumptions)
    assert actual["status"] == status
    if code:
        assert code in {finding["code"] for finding in actual["findings"]}


def test_inspection_expiry_equality_future_clock_and_evaluation_bounds(state, assumptions):
    """UTC instant equality is expired; future evidence is unknown, never inferred valid."""
    inspection = next(p for p in state["inspections"] if p["component"] == "flood-battery")
    due = inspection["at"] + 14 * 86400
    assert result(state, assumptions, due - 0.001)[1]["status"] == "within_recorded_limits"
    assert "inspection_overdue" in {
        f["code"] for f in result(state, assumptions, due)[1]["findings"]
    }
    assert result(state, assumptions, inspection["at"] - 1)[1]["status"] == "unknown"
    for invalid in [-1, float("nan"), float("inf")]:
        with pytest.raises(ValueError):
            evaluate(state, invalid, assumptions)


@pytest.mark.parametrize(
    "capacity,resistance,status,code",
    [
        (None, 75.0, "unknown", "battery_evidence_missing"),
        (95.0, None, "unknown", "battery_evidence_missing"),
        (79.9, 75.0, "blocked", "battery_capacity"),
        (95.0, 180.1, "blocked", "battery_resistance"),
        (80.0, 180.0, "within_recorded_limits", None),
    ],
)
def test_battery_measurement_boundaries(state, assumptions, capacity, resistance, status, code):
    """Equality follows configured semantics; missing observations are not treated as healthy."""
    inspection = next(p for p in state["inspections"] if p["component"] == "flood-battery")
    inspection.update(capacity=capacity, resistance=resistance)
    actual = result(state, assumptions)[1]
    assert actual["status"] == status
    if code:
        assert code in {f["code"] for f in actual["findings"]}


def test_missing_failed_retired_and_history_findings_accumulate(state, assumptions):
    """Every finding remains visible; a known blocker takes priority over unknown history."""
    part = next(p for p in state["components"] if p["id"] == "flood-battery")
    part.update(history_complete=False, retired=1)
    inspection = next(p for p in state["inspections"] if p["component"] == "flood-battery")
    inspection["passed"] = 0
    actual = result(state, assumptions)[1]
    assert actual["status"] == "blocked"
    assert {f["code"] for f in actual["findings"]} >= {
        "retired",
        "history_incomplete",
        "inspection_failed",
    }
    state["inspections"] = [i for i in state["inspections"] if i["component"] != "flood-battery"]
    assert "inspection_missing" in {f["code"] for f in result(state, assumptions)[1]["findings"]}


def test_configuration_drift_missing_slot_and_unmodeled_part(state, assumptions):
    """A changed profile does not silently reinterpret an installed physical part or omit it."""
    state["aircraft"][0]["history_complete"] = False
    state["installations"][0]["slot"] = "unmodeled"
    report = evaluate(state, time.time(), assumptions)
    assert {f["code"] for f in report["aircraft"][0]["findings"]} >= {
        "aircraft_history",
        "missing_battery",
        "unmodeled_installation",
    }
    state["installations"][0]["slot"] = "battery"
    next(part for part in state["components"] if part["id"] == "flood-battery")["kind"] = "assembly"
    assert "incompatible_battery" in {
        f["code"] for f in evaluate(state, time.time(), assumptions)["aircraft"][0]["findings"]
    }
    state["aircraft"][0]["profile"] = "unknown-profile"
    assert "profile_missing" in {
        f["code"] for f in evaluate(state, time.time(), assumptions)["aircraft"][0]["findings"]
    }


def test_missing_limits_zero_rate_and_latest_inspection_order(state):
    """No rate means no finite forecast; actual latest ID wins regardless of supplied array order."""
    now = time.time()
    part = next(part for part in state["components"] if part["id"] == "flood-battery")
    part["kind"] = "payload"
    actual = result(state, Assumptions(daily_seconds=0, daily_cycles=0))[1]
    assert actual["status"] == "unknown" and actual["remaining_seconds"] is None
    part["kind"] = "battery"
    assert (
        result(state, Assumptions(daily_seconds=0, daily_cycles=0))[1][
            "planning_days_to_usage_limit"
        ]
        is None
    )
    assert (
        result(state, Assumptions(daily_seconds=1200, daily_cycles=0))[1][
            "planning_days_to_usage_limit"
        ]
        == 297.0
    )
    latest = copy.deepcopy(
        next(item for item in state["inspections"] if item["component"] == "flood-battery")
    )
    latest.update(id=999, passed=0, at=now)
    state["inspections"].insert(0, latest)
    assert indexes(state)[1]["flood-battery"]["id"] == 999
    assert result(state, Assumptions(daily_seconds=0, daily_cycles=2))[1]["status"] == "blocked"
    assert worst([]) == "unknown"
    assert active_policy(state).label.startswith("Fictional")


def test_watch_and_empty_fleet_are_not_cleared(state, assumptions):
    """Watch items request review; no aircraft records means unknown, not vacuously ready."""
    state["defects"].append(
        {
            "id": 2,
            "component": "flood-battery",
            "severity": "watch",
            "note": "Synthetic watch finding",
            "closed": 0,
        }
    )
    assert result(state, assumptions)[1]["status"] == "review"
    state["aircraft"] = []
    assert evaluate(state, time.time(), assumptions)["status"] == "unknown"
