"""Jason Stys: standards-impact arithmetic, immutable records and real API guards. Map: docs/SOURCE_MAP.md."""

from workbench.engine import active_policy
from workbench.impact import policy_impact
from workbench.models import Policy, Publish
from workbench.store import canonical


def test_exact_hard_limit_and_deadline_deltas_preserve_lifetime_records(state, assumptions):
    """Known flood battery has 3600 seconds / four cycles; thresholds are inclusive."""
    original = canonical(state)
    policy = active_policy(state)
    battery = next(limit for limit in policy.limits if limit.kind == "battery")
    battery.seconds, battery.cycles, battery.inspection_days = 3600, 4, 1
    at = max(row["at"] for row in state["inspections"])
    result = policy_impact(state, policy, at, assumptions)
    row = next(row for row in result["changes"]["components"] if row["id"] == "flood-battery")
    assert row["before"]["remaining_seconds"] == 356400
    assert row["before"]["remaining_cycles"] == 196
    assert row["after"]["remaining_seconds"] == row["after"]["remaining_cycles"] == 0
    assert row["after"]["planning_days_to_usage_limit"] == 0
    assert row["after"]["status"] == "blocked"
    assert {finding["code"] for finding in row["after"]["findings"]} >= {
        "time_limit",
        "cycles_limit",
    }
    recorded = next(row for row in state["inspections"] if row["component"] == "flood-battery")
    assert row["after"]["inspection_due"] == recorded["at"] + 86400
    assert result["published"] is result["flight_authorization"] is False
    assert canonical(state) == original


def test_draft_cannot_erase_history_defects_or_missing_configuration(state, assumptions):
    """Looser thresholds cannot cure failed inspections, open defects or unknown history."""
    policy = active_policy(state)
    for limit in policy.limits:
        limit.seconds, limit.cycles = 10**9, 10**7
    policy.battery_min_capacity_pct, policy.battery_max_resistance_mohm = 1.0, 1000.0
    at = max(row["at"] for row in state["inspections"])
    impact = policy_impact(state, policy, at, assumptions)
    statuses = {row["id"]: row["status"] for row in impact["after"]["aircraft"]}
    assert statuses["inspection"] == "blocked"
    assert statuses["training"] == "unknown"
    changed = policy.model_dump()
    for profile in changed["profiles"]:
        profile["slots"].append({"id": "extra-battery", "kind": "battery"})
    unknown = policy_impact(state, Policy.model_validate(changed), at, assumptions)
    assert (
        next(row for row in unknown["after"]["aircraft"] if row["id"] == "flood")["status"]
        == "unknown"
    )
    assert any(
        finding["code"] == "missing_extra-battery"
        for finding in unknown["after"]["aircraft"][0]["findings"]
    )
    same = policy_impact(state, active_policy(state), at, assumptions)
    assert not any(row["changed"] for rows in same["changes"].values() for row in rows)


def test_actual_preview_api_roles_csrf_generation_immutability_and_race(
    store, state, assumptions, login, client, monkeypatch
):
    """No policy/ledger/assessment mutation occurs; concurrent publication is visible."""
    body = {
        "expected_generation": state["generation"],
        "policy": active_policy(state).model_dump(),
        "assumptions": assumptions.model_dump(),
    }
    endpoint = "/api/policies/preview"
    for role in ("operator", "technician", "reviewer"):
        login(role)
        assert client.post(endpoint, json=body).status_code == 403
    login("admin")
    original = store.evidence()
    token = client.headers.pop("X-CSRF-Token")
    assert client.post(endpoint, json=body).status_code == 403
    client.headers["X-CSRF-Token"] = token
    result = client.post(endpoint, json=body)
    assert result.status_code == 200, result.text
    assert result.json()["source_ledger_tip"] == store.snapshot()[1]
    assert result.json()["published"] is False
    assert store.evidence() == original
    assert client.post(endpoint, json={**body, "expected_generation": 999}).status_code == 409
    assert client.post(endpoint, json={**body, "extra": True}).status_code == 422

    def concurrent(*args):
        """Real publication advances generation during calculation."""
        result = policy_impact(*args)
        store.publish(
            Publish(expected_generation=state["generation"], policy=active_policy(state)),
            {"name": "admin", "role": "admin"},
        )
        return result

    monkeypatch.setattr("workbench.store.policy_impact", concurrent)
    assert client.post(endpoint, json=body).status_code == 409


def test_tampered_source_ledger_cannot_be_previewed(store, state, assumptions, login, client):
    """Draft comparison must not become an integrity-check bypass."""
    login("admin")
    with store.connect(True) as db:
        db.execute("UPDATE components SET seconds=seconds+1 WHERE id='flood-battery'")
    response = client.post(
        "/api/policies/preview",
        json={
            "expected_generation": state["generation"],
            "policy": active_policy(state).model_dump(),
            "assumptions": assumptions.model_dump(),
        },
    )
    assert response.status_code == 503
