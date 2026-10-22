"""Jason Stys: original unlocated fictional fleet and illustrative limits; lines: docs/SOURCE_MAP.md.

No real manufacturer data, airworthiness criteria, people, locations or operational fleet records.
"""

from workbench.models import Policy


def example_policy():
    """Three-position assembly demo; users may configure individual motors/propellers in profiles."""
    return Policy.model_validate(
        {
            "label": "Fictional training fleet standard",
            "reference": "Synthetic demonstration only; replace with applicable manufacturer-controlled instructions",
            "profiles": [
                {
                    "id": "standard",
                    "label": "Synthetic assembly-level multirotor",
                    "slots": [
                        {"id": "battery", "kind": "battery"},
                        {"id": "propulsion", "kind": "assembly"},
                        {"id": "airframe", "kind": "airframe"},
                    ],
                }
            ],
            "limits": [
                {"kind": kind, "seconds": seconds, "cycles": cycles, "inspection_days": days}
                for kind, seconds, cycles, days in [
                    ("battery", 360000, 200, 14),
                    ("assembly", 1800000, 1000, 30),
                    ("airframe", 7200000, 5000, 90),
                ]
            ],
            "warning_percent": 10,
            "battery_min_capacity_pct": 80.0,
            "battery_max_resistance_mohm": 180.0,
        }
    )


def example_records(now):
    """Return coherent generated identities and evidence for ready/blocked/unknown/watch scenarios."""
    aircraft, components, installations, inspections = [], [], [], []
    for index, (key, label) in enumerate(
        [
            ("flood", "Synthetic flood-response unit"),
            ("inspection", "Synthetic infrastructure unit"),
            ("training", "Synthetic training unit"),
        ]
    ):
        base = {
            "id": key,
            "serial": f"SYNTH-AIR-{index + 1}",
            "label": label,
            "profile": "standard",
            "opening_seconds": 3600,
            "opening_cycles": 4,
            "history_complete": True,
            "source_note": "Original synthetic complete opening-history exercise",
            "seconds": 3600,
            "cycles": 4,
        }
        aircraft.append(base)
        for kind, slot in [
            ("battery", "battery"),
            ("assembly", "propulsion"),
            ("airframe", "airframe"),
        ]:
            identifier = f"{key}-{slot}"
            seconds, cycles = (
                (330000, 185) if key == "inspection" and kind == "battery" else (3600, 4)
            )
            components.append(
                {
                    "id": identifier,
                    "serial": f"SYNTH-{index + 1}-{slot.upper()}",
                    "label": f"{label}: {slot}",
                    "kind": kind,
                    "opening_seconds": seconds,
                    "opening_cycles": cycles,
                    "history_complete": key != "training" or kind != "battery",
                    "source_note": "Synthetic component baseline; no real maintenance measurements",
                    "seconds": seconds,
                    "cycles": cycles,
                    "retired": 0,
                }
            )
            installations.append(
                {
                    "id": len(installations) + 1,
                    "aircraft": key,
                    "slot": slot,
                    "component": identifier,
                    "installed": 1,
                    "removed": None,
                }
            )
            if key != "training" or kind != "battery":
                inspections.append(
                    {
                        "id": len(inspections) + 1,
                        "component": identifier,
                        "passed": 1,
                        "capacity": 95.0 if kind == "battery" else None,
                        "resistance": 75.0 if kind == "battery" else None,
                        "note": "Original synthetic passing inspection evidence",
                        "actor": "synthetic-init",
                        "at": now - 86400,
                        "generation": 1,
                    }
                )
    components.append(
        {
            "id": "spare-battery",
            "serial": "SYNTH-SPARE-BATTERY",
            "label": "Synthetic serviceable spare battery",
            "kind": "battery",
            "opening_seconds": 1200,
            "opening_cycles": 2,
            "history_complete": True,
            "source_note": "Synthetic traceable spare opening history",
            "seconds": 1200,
            "cycles": 2,
            "retired": 0,
        }
    )
    inspections.append(
        {
            "id": len(inspections) + 1,
            "component": "spare-battery",
            "passed": 1,
            "capacity": 96.0,
            "resistance": 70.0,
            "note": "Synthetic spare inspection, not a real measurement",
            "actor": "synthetic-init",
            "at": now - 3600,
            "generation": 1,
        }
    )
    defects = [
        {
            "id": 1,
            "component": "inspection-propulsion",
            "severity": "blocking",
            "note": "Synthetic loose assembly mount finding; controlled-work verification exercise",
            "actor": "synthetic-init",
            "at": now - 3600,
            "closed": 0,
        }
    ]
    return {
        "aircraft": aircraft,
        "components": components,
        "installations": installations,
        "inspections": inspections,
        "defects": defects,
    }
