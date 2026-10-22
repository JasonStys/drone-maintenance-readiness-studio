"""Jason Stys: real API/SQLite swap, attribution, idempotency and maintenance-verification regressions. Lines: docs/SOURCE_MAP.md."""

import concurrent.futures
import secrets
import sqlite3

import pytest
from fastapi import HTTPException

from workbench.models import Usage

NOTE = "Original synthetic maintenance evidence, not real inspection data"


def test_two_repairs_do_not_deadlock_or_close_other_defects(client, login, post):
    """Each repaired defect is verified separately; the unresolved sibling still blocks readiness."""
    login("technician")
    second = post("/api/defects", component="inspection-propulsion", severity="blocking", note=NOTE)
    second_id = second.json()["state"]["defects"][-1]["id"]
    for identifier in [1, second_id]:
        assert post("/api/work", defect=identifier, note=NOTE).status_code == 200
    assert (
        post(
            "/api/inspections", component="inspection-propulsion", passed=True, note=NOTE
        ).status_code
        == 200
    )
    login("reviewer")
    first = post("/api/work/verify", work=1, note=NOTE)
    assert first.status_code == 200
    assert by_id(first.json()["readiness"]["aircraft"], "inspection")["status"] == "blocked"
    second = post("/api/work/verify", work=2, note=NOTE)
    assert second.status_code == 200
    assert by_id(second.json()["readiness"]["aircraft"], "inspection")["status"] == "review"


def by_id(values, identifier):
    """Independent identity selection; never assume SQL ordering matches fixture construction order."""
    return next(value for value in values if value["id"] == identifier)


def test_swap_keeps_component_life_and_usage_attribution(client, login, post):
    """Recorded seconds/cycles accrue to installed IDs only; removed part retains all lifetime use."""
    login("operator")
    key = secrets.token_hex(16)
    response = post(
        "/api/usage", aircraft="flood", seconds=120, cycles=2, request_id=key, note=NOTE
    )
    assert response.status_code == 200
    state = response.json()["state"]
    assert by_id(state["components"], "flood-battery")["seconds"] == 3720
    assert by_id(state["components"], "spare-battery")["seconds"] == 1200
    assert state["usage"][0]["components"] == [
        "flood-airframe",
        "flood-battery",
        "flood-propulsion",
    ]
    login("technician")
    swapped = post(
        "/api/swaps", aircraft="flood", slot="battery", component="spare-battery", note=NOTE
    )
    assert swapped.status_code == 200
    assert by_id(swapped.json()["state"]["components"], "flood-battery")["seconds"] == 3720
    login("operator")
    after = post(
        "/api/usage",
        aircraft="flood",
        seconds=60,
        cycles=1,
        request_id=secrets.token_hex(16),
        note=NOTE,
    ).json()["state"]
    assert by_id(after["components"], "flood-battery")["seconds"] == 3720
    assert by_id(after["components"], "spare-battery")["seconds"] == 1260
    assert by_id(after["aircraft"], "flood")["seconds"] == 3780
    evidence = client.get("/api/evidence/export").json()
    assert NOTE in evidence["ledger"][2]["detail"]
    assert len(evidence["ledger_tip"]) == 64
    assert "users" not in evidence["state"] and "sessions" not in evidence["state"]


def test_idempotency_retries_content_binding_and_concurrent_exactly_once(client, login, store):
    """An ambiguous successful request retry does not depend on its now-old generation."""
    login()
    body = {
        "expected_generation": 1,
        "aircraft": "flood",
        "seconds": 60,
        "cycles": 1,
        "request_id": secrets.token_hex(16),
        "note": NOTE,
    }
    first = client.post("/api/usage", json=body)
    second = client.post("/api/usage", json=body)
    assert first.json()["write"]["duplicate"] is False
    assert second.json()["write"] == {"id": first.json()["write"]["id"], "duplicate": True}
    assert client.post("/api/usage", json={**body, "seconds": 61}).status_code == 409
    assert len(client.get("/api/workspace").json()["state"]["usage"]) == 1
    command = Usage.model_validate(
        {**body, "expected_generation": 2, "request_id": secrets.token_hex(16)}
    )
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        results = list(
            pool.map(
                lambda _: store.usage(command, {"name": "operator", "role": "operator"}), range(2)
            )
        )
    assert sorted(result["duplicate"] for result in results) == [False, True]
    assert by_id(store.snapshot()[0]["aircraft"], "flood")["seconds"] == 3720


def test_stale_concurrent_writes_and_failed_swap_rollback(client, login, post):
    """A rejected double install or mismatched part cannot remove the old part or bump generation."""
    login("technician")
    initial = client.get("/api/workspace").json()["state"]
    for component in ["inspection-battery", "flood-airframe", "missing-part"]:
        response = post(
            "/api/swaps", aircraft="flood", slot="battery", component=component, note=NOTE
        )
        assert response.status_code in {404, 409}
    assert client.get("/api/workspace").json()["state"] == initial
    assert (
        post(
            "/api/swaps", aircraft="flood", slot="missing-slot", component=None, note=NOTE
        ).status_code
        == 422
    )
    assert (
        post("/api/swaps", aircraft="flood", slot="battery", component=None, note=NOTE).status_code
        == 200
    )
    stale = {
        "expected_generation": 1,
        "aircraft": "flood",
        "slot": "battery",
        "component": "spare-battery",
        "note": NOTE,
    }
    assert client.post("/api/swaps", json=stale).status_code == 409
    unknown = by_id(client.get("/api/workspace").json()["readiness"]["aircraft"], "flood")
    assert unknown["status"] == "unknown"


def test_independent_work_fresh_inspection_and_preserved_warning(client, login, post):
    """Work alone does not clear a defect; fresh passing inspection plus another reviewer is required."""
    login("technician")
    assert post("/api/work", defect=1, note=NOTE).status_code == 200
    assert post("/api/work", defect=1, note=NOTE).status_code == 409
    login("reviewer")
    assert post("/api/work/verify", work=1, note=NOTE).status_code == 409
    login("technician")
    assert (
        post(
            "/api/inspections", component="inspection-propulsion", passed=True, note=NOTE
        ).status_code
        == 200
    )
    assert (
        by_id(client.get("/api/workspace").json()["readiness"]["aircraft"], "inspection")["status"]
        == "blocked"
    )
    login("reviewer")
    verified = post("/api/work/verify", work=1, note=NOTE)
    assert verified.status_code == 200
    assert by_id(verified.json()["readiness"]["aircraft"], "inspection")["status"] == "review"
    assert post("/api/work/verify", work=1, note=NOTE).status_code == 409


def test_failed_inspection_cannot_be_erased_by_pass_and_self_review_denied(
    client, login, post, store
):
    """New pass remains separate evidence; role changes do not permit self-verifying completed work."""
    login("technician")
    failed = post("/api/inspections", component="flood-propulsion", passed=False, note=NOTE)
    defect = failed.json()["state"]["defects"][-1]["id"]
    assert post("/api/work", defect=defect, note=NOTE).status_code == 200
    assert (
        post("/api/inspections", component="flood-propulsion", passed=True, note=NOTE).status_code
        == 200
    )
    assert (
        by_id(client.get("/api/workspace").json()["readiness"]["aircraft"], "flood")["status"]
        == "blocked"
    )
    with store.connect(True) as db:
        db.execute("UPDATE users SET role='reviewer' WHERE name='technician'")
    assert post("/api/work/verify", work=1, note=NOTE).status_code == 409


def test_retirement_is_irreversible_and_preserves_serial_and_life(client, login, post):
    """Retire only removed parts; they cannot be installed, inspected back to service or recreated."""
    login("technician")
    assert post("/api/retire", component="flood-battery", note=NOTE).status_code == 409
    assert (
        post(
            "/api/swaps", aircraft="flood", slot="battery", component="spare-battery", note=NOTE
        ).status_code
        == 200
    )
    retired = post("/api/retire", component="flood-battery", note=NOTE)
    assert retired.status_code == 200
    assert by_id(retired.json()["state"]["components"], "flood-battery")["seconds"] == 3600
    assert (
        post(
            "/api/swaps", aircraft="flood", slot="battery", component="flood-battery", note=NOTE
        ).status_code
        == 409
    )
    assert post("/api/retire", component="flood-battery", note=NOTE).status_code == 409
    assert (
        post(
            "/api/inspections",
            component="flood-battery",
            passed=True,
            capacity_pct=95.0,
            resistance_mohm=70.0,
            note=NOTE,
        ).status_code
        == 409
    )
    login("admin")
    part = {
        "id": "reset-attempt",
        "serial": "SYNTH-1-BATTERY",
        "label": "Attempted lifetime reset",
        "kind": "battery",
        "opening_seconds": 0,
        "opening_cycles": 0,
        "history_complete": True,
        "source_note": NOTE,
    }
    assert post("/api/components", component=part).status_code == 409


def test_counter_overflow_and_bad_nonbattery_measurements(client, login, post):
    """Large opening records are preserved honestly; new use cannot overflow bounded counters."""
    login("admin")
    part = {
        "id": "old-battery",
        "serial": "OLD-BATTERY-001",
        "label": "Synthetic end-of-life record",
        "kind": "battery",
        "opening_seconds": 10**12,
        "opening_cycles": 10**12,
        "history_complete": True,
        "source_note": NOTE,
    }
    assert post("/api/components", component=part).status_code == 200
    login("technician")
    assert (
        post(
            "/api/swaps", aircraft="flood", slot="battery", component="old-battery", note=NOTE
        ).status_code
        == 200
    )
    assert (
        post(
            "/api/usage",
            aircraft="flood",
            seconds=1,
            cycles=1,
            request_id=secrets.token_hex(16),
            note=NOTE,
        ).status_code
        == 409
    )
    assert (
        post(
            "/api/inspections",
            component="flood-airframe",
            passed=True,
            capacity_pct=95.0,
            note=NOTE,
        ).status_code
        == 422
    )


def test_records_and_ledger_are_immutable_sql_and_explicit_caps(
    store, client, login, post, monkeypatch
):
    """No safety evidence is removed to make a badge green; capacity rejects before mutation."""
    from workbench.store import CAPACITY

    with pytest.raises(sqlite3.IntegrityError), store.connect(True) as db:
        db.execute("UPDATE ledger SET actor='changed' WHERE generation=1")
    login("operator")
    before = store.snapshot()[0]
    monkeypatch.setitem(CAPACITY, "ledger", 1)
    assert (
        post("/api/defects", component="flood-battery", severity="watch", note=NOTE).status_code
        == 409
    )
    assert (
        post(
            "/api/usage",
            aircraft="flood",
            seconds=1,
            cycles=1,
            request_id=secrets.token_hex(16),
            note=NOTE,
        ).status_code
        == 409
    )
    assert store.snapshot()[0] == before
    with pytest.raises(ValueError):
        store.insert_asset(None, "user-chosen-table", {})
    with pytest.raises(HTTPException):
        store.entity(before, "components", "missing")
