"""Jason Stys: snapshot staleness, time expiry, evidence tampering and capacity regressions. Lines: docs/SOURCE_MAP.md."""

import json
import time

import pytest
from fastapi import HTTPException

from workbench import store as storage
from workbench.models import Review

NOTE = "Original synthetic evidence review; never a flight clearance"


def test_immutable_assessment_current_stale_export_and_independent_ack(client, login, post):
    """Blocked findings remain blocked after acknowledgement; changed source makes old evidence stale."""
    login()
    captured = post("/api/assessments", assumptions={"daily_seconds": 1200, "daily_cycles": 2})
    assert captured.status_code == 200
    report = captured.json()
    assert report["result"]["status"] == "blocked" and report["stale"] is False
    assert (
        client.post(f"/api/assessments/{report['id']}/review", json={"note": NOTE}).status_code
        == 403
    )
    login("reviewer")
    reviewed = client.post(f"/api/assessments/{report['id']}/review", json={"note": NOTE})
    assert reviewed.status_code == 200
    assert reviewed.json()["result"] == report["result"]
    assert reviewed.json()["flight_authorization"] is False
    assert (
        client.post(f"/api/assessments/{report['id']}/review", json={"note": NOTE}).status_code
        == 409
    )
    login("operator")
    assert (
        post("/api/defects", component="flood-battery", severity="watch", note=NOTE).status_code
        == 200
    )
    stale = client.get(f"/api/assessments/{report['id']}/export")
    assert stale.status_code == 200 and stale.json()["stale"] is True
    assert stale.json()["state"] == report["state"]
    assert stale.json()["digest"] == report["digest"]
    assert "attachment" in stale.headers["content-disposition"]
    assert client.get("/api/assessments/999").status_code == 404


def test_readiness_review_self_and_role_change_no_bypass(client, login, post, store):
    """Changing stored role cannot let the original assessor acknowledge their own evidence."""
    login()
    report = post("/api/assessments", assumptions={"daily_seconds": 0, "daily_cycles": 0}).json()
    with store.connect(True) as db:
        db.execute("UPDATE users SET role='reviewer' WHERE name='operator'")
    assert (
        client.post(f"/api/assessments/{report['id']}/review", json={"note": NOTE}).status_code
        == 409
    )


def test_clock_rollback_inspection_deadline_and_expiry(store, client, login, post, monkeypatch):
    """Clock rollback and exact validity equality invalidate acknowledgement, not rewrite old results."""
    login()
    report = post("/api/assessments", assumptions={"daily_seconds": 1200, "daily_cycles": 2}).json()
    original = time.time
    monkeypatch.setattr(storage.time, "time", lambda: report["created"] - 1)
    assert store.report(report["id"])["stale"] is True
    monkeypatch.setattr(storage.time, "time", lambda: report["result"]["valid_until"])
    assert store.report(report["id"])["stale"] is True
    with pytest.raises(HTTPException):
        store.review(report["id"], Review(note=NOTE), {"name": "reviewer", "role": "reviewer"})
    monkeypatch.setattr(storage.time, "time", original)
    assert store.report(report["id"])["stale"] is False


@pytest.mark.parametrize("tamper", ["state", "chain", "truncate"])
def test_actual_state_or_chain_tampering_fails_closed(store, client, login, tamper):
    """A database owner can bypass triggers, but unexplained state/hash-chain mutations are detected."""
    login()
    with store.connect(True) as db:
        if tamper == "state":
            db.execute("UPDATE components SET cycles=cycles+1 WHERE id='flood-battery'")
        elif tamper == "chain":
            db.execute("DROP TRIGGER immutable_ledger_update")
            db.execute("UPDATE ledger SET actor='tampered'")
        else:
            db.execute("DROP TRIGGER immutable_ledger_delete")
            db.execute("DELETE FROM ledger")
    assert client.get("/api/workspace").status_code == 503
    assert client.get("/api/evidence/export").status_code == 503


@pytest.mark.parametrize("target", ["assessment", "review"])
def test_assessment_and_acknowledgement_hashes(store, client, login, post, target):
    """Review notes and snapshots have their own checksums, separate from the domain-state ledger."""
    login()
    report = post("/api/assessments", assumptions={"daily_seconds": 1200, "daily_cycles": 2}).json()
    login("reviewer")
    assert (
        client.post(f"/api/assessments/{report['id']}/review", json={"note": NOTE}).status_code
        == 200
    )
    with store.connect(True) as db:
        if target == "assessment":
            db.execute("DROP TRIGGER immutable_assessment_update")
            content = json.loads(db.execute("SELECT content FROM assessments").fetchone()[0])
            content["result"]["status"] = "within_recorded_limits"
            db.execute("UPDATE assessments SET content=?", (json.dumps(content),))
        else:
            db.execute("DROP TRIGGER immutable_review_update")
            db.execute("UPDATE reviews SET note='Tampered acknowledgement'")
    assert client.get(f"/api/assessments/{report['id']}").status_code == 503


@pytest.mark.parametrize(
    "cap", ["aircraft", "components", "policies", "usage", "inspections", "defects", "assessments"]
)
def test_local_capacities_are_fail_closed(store, client, login, post, monkeypatch, cap):
    """Small local-workspace bounds are exercised without creating thousands of fake production rows."""
    monkeypatch.setitem(storage.CAPACITY, cap, 0)
    before = store.snapshot()[0]
    login("admin")
    if cap in {"aircraft", "components"}:
        asset = {
            "id": "new-object",
            "serial": "UNIQUE-NEW-SERIAL",
            "label": "Synthetic opening record",
            "opening_seconds": 0,
            "opening_cycles": 0,
            "history_complete": False,
            "source_note": NOTE,
        }
        if cap == "aircraft":
            response = post("/api/aircraft", aircraft={**asset, "profile": "standard"})
        else:
            response = post("/api/components", component={**asset, "kind": "battery"})
    elif cap == "policies":
        response = post("/api/policies", policy=before["policies"][0]["content"])
    elif cap == "assessments":
        response = post("/api/assessments", assumptions={"daily_seconds": 0, "daily_cycles": 0})
    else:
        login("technician")
        if cap == "usage":
            response = post(
                "/api/usage", aircraft="flood", seconds=1, cycles=1, request_id="a" * 32, note=NOTE
            )
        elif cap == "inspections":
            response = post("/api/inspections", component="flood-battery", passed=True, note=NOTE)
        else:
            response = post("/api/defects", component="flood-battery", severity="watch", note=NOTE)
            assert (
                post(
                    "/api/inspections", component="flood-battery", passed=False, note=NOTE
                ).status_code
                == 409
            )
    assert response.status_code == 409
    assert store.snapshot()[0] == before


def test_creation_and_policy_publication_preserve_counter_history(client, login, post):
    """Admin provisioning is functional; later policies create explicit unknowns rather than erasing records."""
    login("admin")
    asset = {
        "id": "new-aircraft",
        "serial": "NEW-AIRCRAFT-001",
        "label": "New synthetic aircraft",
        "opening_seconds": 500,
        "opening_cycles": 5,
        "history_complete": False,
        "source_note": NOTE,
        "profile": "standard",
    }
    assert post("/api/aircraft", aircraft={**asset, "profile": "missing"}).status_code == 422
    assert post("/api/aircraft", aircraft=asset).status_code == 200
    policy = client.get("/api/workspace").json()["state"]["policies"][0]["content"]
    policy["profiles"][0]["id"] = "new-standard"
    published = post("/api/policies", policy=policy)
    assert published.status_code == 200 and published.json()["state"]["policy_version"] == 2
    assert published.json()["readiness"]["aircraft"][0]["status"] == "unknown"
    login("technician")
    assert (
        post("/api/swaps", aircraft="flood", slot="battery", component=None, note=NOTE).status_code
        == 422
    )
