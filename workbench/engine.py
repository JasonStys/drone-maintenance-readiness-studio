"""Jason Stys: deterministic record-based readiness and explicit workload planning.

Functions/variables and exact lines: docs/SOURCE_MAP.md. No flight authorization or empirical failure prediction.
"""

import math

from workbench.models import Assumptions, Policy

RANK = {"within_recorded_limits": 0, "review": 1, "unknown": 2, "blocked": 3}


def worst(statuses):
    """Blocking findings take precedence; absent records can never become an affirmative result."""
    return max(statuses, key=RANK.__getitem__, default="unknown")


def active_policy(state):
    """Select exact immutable active policy version, not the last array position."""
    return Policy.model_validate(
        next(p["content"] for p in state["policies"] if p["version"] == state["policy_version"])
    )


def indexes(state):
    """Index components, latest inspections and open defects once, avoiding repeated fleet scans."""
    inspections, defects = {}, {}
    for entry in state["inspections"]:
        if (
            entry["component"] not in inspections
            or entry["id"] > inspections[entry["component"]]["id"]
        ):
            inspections[entry["component"]] = entry
    for defect in state["defects"]:
        if not defect["closed"]:
            defects.setdefault(defect["component"], []).append(defect)
    return {p["id"]: p for p in state["components"]}, inspections, defects


def component_result(part, limit, inspection, defects, policy, at, assumptions):
    """Evaluate one serialized identity without changing counters or assuming missing evidence passed."""
    findings = []

    def add(code, status, message):
        """Retain every reason even when a higher-precedence finding sets aggregate status."""
        findings.append({"code": code, "status": status, "message": message})

    if part["retired"]:
        add("retired", "blocked", "Part is permanently retired in this workspace")
    if not part["history_complete"]:
        add("history_incomplete", "unknown", "Opening lifetime history is not attested complete")
    remaining_seconds = remaining_cycles = None
    due = None
    if limit is None:
        add("limit_missing", "unknown", "No configured limits for this component kind")
    else:
        remaining_seconds = max(0, limit.seconds - part["seconds"])
        remaining_cycles = max(0, limit.cycles - part["cycles"])
        for key, used, maximum in [
            ("time", part["seconds"], limit.seconds),
            ("cycles", part["cycles"], limit.cycles),
        ]:
            if used >= maximum:
                add(
                    f"{key}_limit",
                    "blocked",
                    f"Recorded {key} reached or exceeded configured limit",
                )
            elif used * 100 >= maximum * (100 - policy.warning_percent):
                add(
                    f"{key}_near_limit", "review", f"Recorded {key} entered configured warning band"
                )
    if inspection is None:
        add("inspection_missing", "unknown", "No inspection evidence is recorded")
    else:
        if inspection["at"] > at:
            add("clock_skew", "unknown", "Inspection is in the future relative to server clock")
        if not inspection["passed"]:
            add("inspection_failed", "blocked", "Latest recorded inspection failed")
        if limit:
            due = inspection["at"] + limit.inspection_days * 86400
            if at >= due:
                add("inspection_overdue", "blocked", "Inspection interval reached or exceeded")
        if part["kind"] == "battery":
            if inspection["capacity"] is None or inspection["resistance"] is None:
                add(
                    "battery_evidence_missing",
                    "unknown",
                    "Capacity/resistance evidence is missing; no battery health inference",
                )
            else:
                if inspection["capacity"] < policy.battery_min_capacity_pct:
                    add(
                        "battery_capacity",
                        "blocked",
                        "Recorded capacity below configured threshold",
                    )
                if inspection["resistance"] > policy.battery_max_resistance_mohm:
                    add(
                        "battery_resistance",
                        "blocked",
                        "Recorded resistance above configured threshold",
                    )
    for defect in defects:
        add(
            f"defect_{defect['id']}",
            "blocked" if defect["severity"] == "blocking" else "review",
            f"Open {defect['severity']} defect: {defect['note']}",
        )
    status = worst(f["status"] for f in findings) if findings else "within_recorded_limits"
    estimates = []
    if limit and part["history_complete"]:
        if assumptions.daily_seconds:
            estimates.append(remaining_seconds / assumptions.daily_seconds)
        if assumptions.daily_cycles:
            estimates.append(remaining_cycles / assumptions.daily_cycles)
    return {
        "id": part["id"],
        "serial": part["serial"],
        "label": part["label"],
        "kind": part["kind"],
        "status": status,
        "seconds": part["seconds"],
        "cycles": part["cycles"],
        "remaining_seconds": remaining_seconds,
        "remaining_cycles": remaining_cycles,
        "inspection_due": due,
        "planning_days_to_usage_limit": round(min(estimates), 3) if estimates else None,
        "findings": findings,
    }


def evaluate(state, at: float, assumptions: Assumptions):
    """Evaluate a coherent fleet snapshot: O(records + required slots), not flight or airworthiness approval.

    UTC epoch seconds are server-owned. Planning extrapolates the explicitly supplied constant
    daily workload; zero rate means no finite usage estimate, never infinity/NaN in JSON.
    """
    if not math.isfinite(at) or at < 0:
        raise ValueError("Invalid evaluation clock")
    policy = active_policy(state)
    parts, inspections, defects = indexes(state)
    limits = {limit.kind: limit for limit in policy.limits}
    results = {
        key: component_result(
            part,
            limits.get(part["kind"]),
            inspections.get(key),
            defects.get(key, []),
            policy,
            at,
            assumptions,
        )
        for key, part in parts.items()
    }
    installations = {
        (item["aircraft"], item["slot"]): item["component"]
        for item in state["installations"]
        if item["removed"] is None
    }
    positions = {}
    for aircraft_id, slot_id in installations:
        positions.setdefault(aircraft_id, set()).add(slot_id)
    profiles = {profile.id: profile for profile in policy.profiles}
    aircraft = []
    for asset in state["aircraft"]:
        findings, slots = [], []
        if not asset["history_complete"]:
            findings.append(
                {
                    "code": "aircraft_history",
                    "status": "unknown",
                    "message": "Aircraft opening history is incomplete",
                }
            )
        profile = profiles.get(asset["profile"])
        if profile is None:
            findings.append(
                {
                    "code": "profile_missing",
                    "status": "unknown",
                    "message": "Aircraft profile is absent from active policy",
                }
            )
        else:
            for slot in profile.slots:
                identifier = installations.get((asset["id"], slot.id))
                if identifier not in results:
                    value = {"slot": slot.id, "status": "unknown", "component": None}
                    findings.append(
                        {
                            "code": f"missing_{slot.id}",
                            "status": "unknown",
                            "message": f"Required slot {slot.id} lacks a recorded part",
                        }
                    )
                elif parts[identifier]["kind"] != slot.kind:
                    value = {"slot": slot.id, "status": "blocked", "component": identifier}
                    findings.append(
                        {
                            "code": f"incompatible_{slot.id}",
                            "status": "blocked",
                            "message": "Installed part kind conflicts with current profile",
                        }
                    )
                else:
                    value = {
                        "slot": slot.id,
                        "component": identifier,
                        "status": results[identifier]["status"],
                    }
                slots.append(value)
            known = {slot.id for slot in profile.slots}
            if positions.get(asset["id"], set()) - known:
                findings.append(
                    {
                        "code": "unmodeled_installation",
                        "status": "unknown",
                        "message": "Active installation is not in current profile; reconcile configuration",
                    }
                )
        aircraft.append(
            {
                "id": asset["id"],
                "label": asset["label"],
                "serial": asset["serial"],
                "seconds": asset["seconds"],
                "cycles": asset["cycles"],
                "status": worst([f["status"] for f in findings] + [s["status"] for s in slots]),
                "findings": findings,
                "slots": slots,
            }
        )
    upcoming = [
        result["inspection_due"]
        for result in results.values()
        if result["inspection_due"] is not None and result["inspection_due"] > at
    ]
    return {
        "as_of": at,
        "valid_until": min([at + 86400, *upcoming]),
        "generation": state["generation"],
        "policy_version": state["policy_version"],
        "status": worst(a["status"] for a in aircraft),
        "aircraft": aircraft,
        "components": list(results.values()),
        "assumptions": assumptions.model_dump(),
        "flight_authorization": False,
        "prediction_type": "constant-workload-scenario-not-failure-prediction",
    }
