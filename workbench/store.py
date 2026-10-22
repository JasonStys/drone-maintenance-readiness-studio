"""Jason Stys: atomic lifetime attribution, serialized swaps, independent work verification and evidence.

Exact classes/functions/parameters/bindings: docs/SOURCE_MAP.md. No counter reset or delete endpoint.
"""

import hashlib
import json
import sqlite3
import time
from contextlib import contextmanager
from pathlib import Path

from fastapi import HTTPException

from workbench.engine import active_policy, component_result, evaluate, indexes
from workbench.examples import example_policy, example_records
from workbench.models import Assumptions

QUERIES = {
    "policies": "SELECT * FROM policies ORDER BY version",
    "aircraft": "SELECT * FROM aircraft ORDER BY id",
    "components": "SELECT * FROM components ORDER BY id",
    "installations": "SELECT * FROM installations ORDER BY id",
    "inspections": "SELECT * FROM inspections ORDER BY id",
    "defects": "SELECT * FROM defects ORDER BY id",
    "work": "SELECT * FROM work ORDER BY id",
    "usage": "SELECT * FROM usage ORDER BY id",
}
CAPACITY = {
    "ledger": 5000,
    "aircraft": 50,
    "components": 200,
    "policies": 20,
    "usage": 1000,
    "inspections": 1500,
    "defects": 1000,
    "assessments": 100,
}


def canonical(value):
    """Stable finite JSON; hashes are tamper evidence, not signatures against an OS/database owner."""
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(value):
    """SHA-256 of canonical content, never a password hash or proof of real inspection."""
    return hashlib.sha256(canonical(value).encode()).hexdigest()


class Store:
    """Single trusted local staff organization; all signed-in staff intentionally share fleet records."""

    def __init__(self, path: Path):
        """Initialize schema without seeding/overwriting any existing domain data or account."""
        self.path = path.resolve()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            db.executescript(Path(__file__).with_name("schema.sql").read_text(encoding="utf-8"))

    @contextmanager
    def connect(self, write=False):
        """Serialize writers, roll back failed operations, and always close file handles."""
        db = sqlite3.connect(self.path, timeout=5)
        db.row_factory = sqlite3.Row
        db.execute("PRAGMA foreign_keys=ON")
        try:
            if write:
                db.execute("BEGIN IMMEDIATE")
            yield db
            if write:
                db.commit()
        finally:
            db.close()

    def state(self, db):
        """Read one coherent normalized state using fixed trusted table names, never user SQL identifiers."""
        workspace = db.execute("SELECT generation,policy FROM workspace WHERE id=1").fetchone()
        if workspace is None:
            raise HTTPException(503, "Initialize the private workspace using the CLI")
        result = {"generation": workspace["generation"], "policy_version": workspace["policy"]}
        for table, query in QUERIES.items():
            rows = []
            for record in db.execute(query):
                value = dict(record)
                if "content" in value:
                    content = json.loads(value["content"])
                    if table == "policies":
                        value["content"] = content
                    else:
                        del value["content"]
                        value = {**content, **value}
                if table == "usage":
                    value["components"] = json.loads(value["components"])
                rows.append(value)
            result[table] = rows
        return result

    def verify(self, db, state):
        """Check the complete hash chain and latest state digest; fail closed on accidental row tampering."""
        previous, generation = "0" * 64, 0
        last = None
        for row in db.execute("SELECT * FROM ledger ORDER BY generation"):
            value = dict(row)
            checksum = value.pop("digest")
            if (
                value["generation"] != generation + 1
                or value["previous"] != previous
                or digest(value) != checksum
            ):
                raise HTTPException(503, "Maintenance ledger integrity failure")
            previous, generation, last = checksum, value["generation"], value
        if (
            last is None
            or generation != state["generation"]
            or last["state_digest"] != digest(state)
        ):
            raise HTTPException(503, "Maintenance state integrity failure")
        return previous

    def seal(self, db, actor, event, detail=None):
        """Seal exact new state in the same transaction; global generation invalidates older fleet reports."""
        state = self.state(db)
        row = db.execute("SELECT digest FROM ledger ORDER BY generation DESC LIMIT 1").fetchone()
        value = {
            "generation": state["generation"],
            "actor": actor,
            "event": event,
            "at": time.time(),
            "previous": row["digest"] if row else "0" * 64,
            "state_digest": digest(state),
            "detail": canonical(detail or {}),
        }
        db.execute("INSERT INTO ledger VALUES(?,?,?,?,?,?,?,?)", (*value.values(), digest(value)))

    def initialize(self, examples=False):
        """Idempotent trusted CLI seed; synthetic evidence is generated only on explicit/demo initialization."""
        with self.connect(True) as db:
            if db.execute("SELECT 1 FROM workspace").fetchone():
                return
            db.execute("INSERT INTO policies VALUES(1,?)", (example_policy().model_dump_json(),))
            db.execute("INSERT INTO workspace VALUES(1,1,1)")
            if examples:
                records = example_records(time.time())
                for table in ("aircraft", "components"):
                    for value in records[table]:
                        self.insert_asset(db, table, value)
                for item in records["installations"]:
                    db.execute(
                        "INSERT INTO installations VALUES(?,?,?,?,?,?)", tuple(item.values())
                    )
                for item in records["inspections"]:
                    db.execute(
                        "INSERT INTO inspections VALUES(?,?,?,?,?,?,?,?,?)", tuple(item.values())
                    )
                for item in records["defects"]:
                    db.execute("INSERT INTO defects VALUES(?,?,?,?,?,?,?)", tuple(item.values()))
            self.seal(
                db, "local-init", "synthetic_initialized" if examples else "workspace_initialized"
            )

    def insert_asset(self, db, table, value):
        """Keep immutable opening attestation separate from monotonic recorded totals."""
        if table not in {"aircraft", "components"}:
            raise ValueError("Unknown trusted asset table")
        content = {k: v for k, v in value.items() if k not in {"seconds", "cycles", "retired"}}
        values = (
            value["id"],
            value["serial"],
            canonical(content),
            value.get("seconds", value["opening_seconds"]),
            value.get("cycles", value["opening_cycles"]),
        )
        if table == "aircraft":
            db.execute("INSERT INTO aircraft VALUES(?,?,?,?,?)", values)
        else:
            db.execute(
                "INSERT INTO components VALUES(?,?,?,?,?,?)", (*values, value.get("retired", 0))
            )

    def snapshot(self):
        """Read and verify inside a read transaction so concurrent commits cannot mix generations."""
        with self.connect() as db:
            db.execute("BEGIN")
            state = self.state(db)
            tip = self.verify(db, state)
            return state, tip

    @contextmanager
    def change(self, expected, user, event, roles, detail=None):
        """Authorization + integrity + CAS + limits precede any mutation; no partial writes on failure."""
        if user["role"] not in roles:
            raise HTTPException(403, "Role not permitted for this maintenance action")
        with self.connect(True) as db:
            state = self.state(db)
            self.verify(db, state)
            if expected != state["generation"]:
                raise HTTPException(409, "Workspace changed; refresh before submitting")
            if expected >= CAPACITY["ledger"]:
                raise HTTPException(
                    409, "Local ledger capacity reached; preserve evidence before migration"
                )
            db.execute("UPDATE workspace SET generation=generation+1 WHERE id=1")
            yield db, state, expected + 1
            self.seal(db, user["name"], event, detail)

    def entity(self, state, table, identifier):
        """Resolve a bounded in-memory ID or return a generic missing-record error."""
        result = next((item for item in state[table] if item["id"] == identifier), None)
        if result is None:
            raise HTTPException(404, "Maintenance record not found")
        return result

    def create(self, body, user, table):
        """Administrator records a unique serialized identity; reopening an existing serial is rejected."""
        value = body.aircraft if table == "aircraft" else body.component
        with self.change(body.expected_generation, user, f"{table}_created", {"admin"}) as (
            db,
            state,
            _,
        ):
            if len(state[table]) >= CAPACITY[table]:
                raise HTTPException(409, "Local asset capacity reached")
            if table == "aircraft" and value.profile not in {
                p.id for p in active_policy(state).profiles
            }:
                raise HTTPException(422, "Profile not in current policy")
            self.insert_asset(db, table, value.model_dump())

    def publish(self, body, user):
        """Publish immutable standards; changed slot configuration remains visible as readiness findings."""
        with self.change(body.expected_generation, user, "policy_published", {"admin"}) as (
            db,
            state,
            _,
        ):
            version = state["policy_version"] + 1
            if version > CAPACITY["policies"]:
                raise HTTPException(409, "Policy-version capacity reached")
            db.execute("INSERT INTO policies VALUES(?,?)", (version, body.policy.model_dump_json()))
            db.execute("UPDATE workspace SET policy=? WHERE id=1", (version,))

    def swap(self, body, user):
        """One compatible non-retired part per position/location; remove+install is all-or-nothing."""
        with self.change(
            body.expected_generation, user, "component_swapped", {"technician"}, body.model_dump()
        ) as (db, state, generation):
            aircraft = self.entity(state, "aircraft", body.aircraft)
            profile = next(
                (p for p in active_policy(state).profiles if p.id == aircraft["profile"]), None
            )
            slot = next((s for s in profile.slots if s.id == body.slot), None) if profile else None
            if slot is None:
                raise HTTPException(422, "Slot not in current aircraft profile")
            if body.component:
                part = self.entity(state, "components", body.component)
                if part["retired"] or part["kind"] != slot.kind:
                    raise HTTPException(409, "Retired or incompatible component")
                if any(
                    i["component"] == body.component and i["removed"] is None
                    for i in state["installations"]
                ):
                    raise HTTPException(409, "Component already installed; remove it first")
            db.execute(
                "UPDATE installations SET removed=? WHERE aircraft=? AND slot=? AND removed IS NULL",
                (generation, body.aircraft, body.slot),
            )
            if body.component:
                db.execute(
                    "INSERT INTO installations(aircraft,slot,component,installed) VALUES(?,?,?,?)",
                    (body.aircraft, body.slot, body.component, generation),
                )

    def usage(self, body, user):
        """Exactly-once retry semantics, server-selected installed attribution and no life reset on swap."""
        if user["role"] not in {"operator", "technician"}:
            raise HTTPException(403, "Operator or technician required")
        # Check idempotency before CAS; an identical retried old generation must not double-book usage.
        request_digest = digest({"body": body.model_dump(), "actor": user["name"]})
        with self.connect(True) as db:
            state = self.state(db)
            self.verify(db, state)
            previous = db.execute(
                "SELECT id,request_digest FROM usage WHERE request_id=?", (body.request_id,)
            ).fetchone()
            if previous:
                if previous["request_digest"] != request_digest:
                    raise HTTPException(409, "Idempotency key reused with different content/actor")
                return {"id": previous["id"], "duplicate": True}
            if (
                body.expected_generation != state["generation"]
                or len(state["usage"]) >= CAPACITY["usage"]
                or state["generation"] >= CAPACITY["ledger"]
            ):
                raise HTTPException(409, "Workspace changed or local usage capacity reached")
            aircraft = self.entity(state, "aircraft", body.aircraft)
            parts = sorted(
                i["component"]
                for i in state["installations"]
                if i["aircraft"] == body.aircraft and i["removed"] is None
            )
            for value in [aircraft, *(self.entity(state, "components", key) for key in parts)]:
                if (
                    value["seconds"] + body.seconds > 10**12
                    or value["cycles"] + body.cycles > 10**12
                ):
                    raise HTTPException(409, "Lifetime counter bound exceeded")
            db.execute(
                "UPDATE aircraft SET seconds=seconds+?,cycles=cycles+? WHERE id=?",
                (body.seconds, body.cycles, body.aircraft),
            )
            for identifier in parts:
                db.execute(
                    "UPDATE components SET seconds=seconds+?,cycles=cycles+? WHERE id=?",
                    (body.seconds, body.cycles, identifier),
                )
            generation = state["generation"] + 1
            db.execute("UPDATE workspace SET generation=? WHERE id=1", (generation,))
            cursor = db.execute(
                "INSERT INTO usage(request_id,request_digest,aircraft,seconds,cycles,components,note,actor,at,generation) VALUES(?,?,?,?,?,?,?,?,?,?)",
                (
                    body.request_id,
                    request_digest,
                    body.aircraft,
                    body.seconds,
                    body.cycles,
                    canonical(parts),
                    body.note,
                    user["name"],
                    time.time(),
                    generation,
                ),
            )
            self.seal(db, user["name"], "usage_recorded")
            return {"id": cursor.lastrowid, "duplicate": False}

    def inspect(self, body, user):
        """Append real-time evidence; failed inspections create a separate blocking defect."""
        with self.change(body.expected_generation, user, "inspection_recorded", {"technician"}) as (
            db,
            state,
            generation,
        ):
            part = self.entity(state, "components", body.component)
            if part["retired"] or len(state["inspections"]) >= CAPACITY["inspections"]:
                raise HTTPException(409, "Retired component or inspection capacity reached")
            if part["kind"] != "battery" and (
                body.capacity_pct is not None or body.resistance_mohm is not None
            ):
                raise HTTPException(422, "Battery measurements apply only to batteries")
            now = time.time()
            db.execute(
                "INSERT INTO inspections(component,passed,capacity,resistance,note,actor,at,generation) VALUES(?,?,?,?,?,?,?,?)",
                (
                    body.component,
                    int(body.passed),
                    body.capacity_pct,
                    body.resistance_mohm,
                    body.note,
                    user["name"],
                    now,
                    generation,
                ),
            )
            if not body.passed:
                if len(state["defects"]) >= CAPACITY["defects"]:
                    raise HTTPException(409, "Defect capacity reached")
                db.execute(
                    "INSERT INTO defects(component,severity,note,actor,at,closed) VALUES(?,'blocking',?,?,?,0)",
                    (body.component, "Failed inspection: " + body.note, user["name"], now),
                )

    def defect(self, body, user):
        """Record a finding without pretending new inspection evidence automatically resolves it."""
        with self.change(
            body.expected_generation, user, "defect_reported", {"operator", "technician"}
        ) as (db, state, _):
            self.entity(state, "components", body.component)
            if len(state["defects"]) >= CAPACITY["defects"]:
                raise HTTPException(409, "Defect capacity reached")
            db.execute(
                "INSERT INTO defects(component,severity,note,actor,at,closed) VALUES(?,?,?,?,?,0)",
                (body.component, body.severity, body.note, user["name"], time.time()),
            )

    def complete_work(self, body, user):
        """Record completed corrective work; open defect persists until independent fresh verification."""
        with self.change(body.expected_generation, user, "work_completed", {"technician"}) as (
            db,
            state,
            generation,
        ):
            defect = self.entity(state, "defects", body.defect)
            if defect["closed"] or any(w["defect"] == body.defect for w in state["work"]):
                raise HTTPException(409, "Defect already closed or has a completed work order")
            db.execute(
                "INSERT INTO work(defect,note,technician,at,completed_generation) VALUES(?,?,?,?,?)",
                (body.defect, body.note, user["name"], time.time(), generation),
            )

    def verify_work(self, body, user):
        """Verify one repair independently; other defects remain open, life/health/history cannot be bypassed."""
        with self.change(
            body.expected_generation, user, "work_independently_verified", {"reviewer"}
        ) as (db, state, generation):
            work = self.entity(state, "work", body.work)
            if work["reviewer"] or work["technician"] == user["name"]:
                raise HTTPException(409, "Already verified or independent reviewer required")
            defect = self.entity(state, "defects", work["defect"])
            part = self.entity(state, "components", defect["component"])
            _, inspections, _ = indexes(state)
            inspection = inspections.get(part["id"])
            if (
                inspection is None
                or inspection["generation"] <= work["completed_generation"]
                or not inspection["passed"]
            ):
                raise HTTPException(
                    409, "A fresh passing inspection after work completion is required"
                )
            policy = active_policy(state)
            limit = next((p for p in policy.limits if p.kind == part["kind"]), None)
            # Check non-defect conditions independently. Requiring other defects to close first
            # would deadlock two completed repairs; closing this one never closes the others.
            result = component_result(
                part,
                limit,
                inspection,
                [],
                policy,
                time.time(),
                Assumptions(daily_seconds=0, daily_cycles=0),
            )
            if result["status"] in {"blocked", "unknown"}:
                raise HTTPException(
                    409,
                    "Blocked/unknown component conditions cannot be overridden by work verification",
                )
            db.execute(
                "UPDATE work SET reviewer=?,review_note=?,verified=? WHERE id=?",
                (user["name"], body.note, time.time(), body.work),
            )
            db.execute("UPDATE defects SET closed=1 WHERE id=?", (defect["id"],))

    def retire(self, body, user):
        """Retirement is irreversible, cannot reset a serial and requires removal from all aircraft first."""
        with self.change(
            body.expected_generation, user, "component_retired", {"technician"}, body.model_dump()
        ) as (db, state, _):
            part = self.entity(state, "components", body.component)
            if part["retired"] or any(
                i["component"] == body.component and i["removed"] is None
                for i in state["installations"]
            ):
                raise HTTPException(409, "Remove installed part first, or part is already retired")
            db.execute("UPDATE components SET retired=1 WHERE id=?", (body.component,))

    def assess(self, body, user):
        """Persist an immutable complete input/result/tip snapshot; no source mutation or authority implied."""
        with self.connect(True) as db:
            state = self.state(db)
            tip = self.verify(db, state)
            if (
                state["generation"] != body.expected_generation
                or db.execute("SELECT count(*) FROM assessments").fetchone()[0]
                >= CAPACITY["assessments"]
            ):
                raise HTTPException(409, "Workspace changed or assessment capacity reached")
            now = time.time()
            content = {
                "creator": user["name"],
                "created": now,
                "state": state,
                "ledger_tip": tip,
                "result": evaluate(state, now, body.assumptions),
            }
            cursor = db.execute(
                "INSERT INTO assessments(creator,created,generation,content,digest) VALUES(?,?,?,?,?)",
                (user["name"], now, state["generation"], canonical(content), digest(content)),
            )
            return cursor.lastrowid

    def report(self, identifier, db=None):
        """Verify stored evidence and mark generation/clock/expiry stale without rewriting original results."""
        if db is None:
            with self.connect() as connection:
                connection.execute("BEGIN")
                return self.report(identifier, connection)
        state = self.state(db)
        self.verify(db, state)
        row = db.execute("SELECT * FROM assessments WHERE id=?", (identifier,)).fetchone()
        if row is None:
            raise HTTPException(404, "Assessment not found")
        content = json.loads(row["content"])
        if (
            digest(content) != row["digest"]
            or content["creator"] != row["creator"]
            or content["created"] != row["created"]
            or content["state"]["generation"] != row["generation"]
        ):
            raise HTTPException(503, "Assessment integrity failure")
        review = db.execute(
            "SELECT actor,note,at,digest FROM reviews WHERE assessment=?", (identifier,)
        ).fetchone()
        record = dict(review) if review else None
        if record:
            checksum = record.pop("digest")
            if digest({"assessment": identifier, **record}) != checksum:
                raise HTTPException(503, "Review integrity failure")
        now = time.time()
        return {
            "id": identifier,
            **content,
            "digest": row["digest"],
            "review": record,
            "stale": state["generation"] != row["generation"]
            or now < row["created"]
            or now >= content["result"]["valid_until"],
            "flight_authorization": False,
        }

    def review(self, identifier, body, user):
        """Acknowledge even blocked evidence for triage, never change its findings or authorize a flight."""
        if user["role"] != "reviewer":
            raise HTTPException(403, "Reviewer required")
        with self.connect(True) as db:
            report = self.report(identifier, db)
            if report["stale"] or report["review"] or report["creator"] == user["name"]:
                raise HTTPException(
                    409, "Stale/already reviewed evidence or independent reviewer required"
                )
            record = {
                "assessment": identifier,
                "actor": user["name"],
                "note": body.note,
                "at": time.time(),
            }
            db.execute("INSERT INTO reviews VALUES(?,?,?,?,?)", (*record.values(), digest(record)))

    def dashboard(self):
        """Coherent full small-workspace state, current findings and bounded report/audit navigation."""
        with self.connect() as db:
            db.execute("BEGIN")
            state = self.state(db)
            tip = self.verify(db, state)
            return {
                "state": state,
                "ledger_tip": tip,
                "readiness": evaluate(
                    state, time.time(), Assumptions(daily_seconds=1200, daily_cycles=2)
                ),
                "reports": [
                    dict(r)
                    for r in db.execute(
                        "SELECT id,creator,created,generation FROM assessments ORDER BY id DESC LIMIT 30"
                    )
                ],
                "ledger": [
                    dict(r)
                    for r in db.execute(
                        "SELECT generation,actor,event,at,detail,digest FROM ledger ORDER BY generation DESC LIMIT 50"
                    )
                ],
            }

    def evidence(self):
        """Authorized complete local ledger/state export; includes private maintenance notes, not accounts."""
        with self.connect() as db:
            db.execute("BEGIN")
            state = self.state(db)
            tip = self.verify(db, state)
            return {
                "application": "Drone Maintenance Readiness Studio",
                "author": "Jason Stys",
                "state": state,
                "ledger_tip": tip,
                "ledger": [
                    dict(row) for row in db.execute("SELECT * FROM ledger ORDER BY generation")
                ],
                "flight_authorization": False,
            }
