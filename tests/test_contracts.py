"""Jason Stys: strict finite schemas, immutable client claims and duplicate-profile/slot guards. Lines: docs/SOURCE_MAP.md."""

import pytest
from pydantic import ValidationError

from workbench.examples import example_policy
from workbench.models import Inspection, Profile, Usage


@pytest.mark.parametrize(
    "change",
    [
        {"seconds": 0},
        {"seconds": 7201},
        {"cycles": True},
        {"cycles": 0},
        {"seconds": "60"},
        {"request_id": "bad-id"},
        {"components": ["forged-part"]},
        {"at": 0},
        {"note": "short"},
    ],
)
def test_usage_contract_rejects_untrusted_attribution_or_clock(change):
    """Only bounded integer use and an idempotency key are accepted; server chooses attribution/time."""
    with pytest.raises(ValidationError):
        Usage.model_validate(
            {
                "expected_generation": 1,
                "aircraft": "flood",
                "seconds": 60,
                "cycles": 1,
                "request_id": "a" * 32,
                "note": "Original synthetic usage evidence",
                **change,
            }
        )


@pytest.mark.parametrize(
    "change",
    [
        {"capacity_pct": float("nan")},
        {"capacity_pct": float("inf")},
        {"capacity_pct": -1},
        {"capacity_pct": 101},
        {"resistance_mohm": -1},
        {"resistance_mohm": 1001},
        {"passed": "true"},
    ],
)
def test_inspection_measurements_finite_and_strict(change):
    """No NaN/Infinity/implicit boolean conversion can silently make battery evidence positive."""
    with pytest.raises(ValidationError):
        Inspection.model_validate(
            {
                "expected_generation": 1,
                "component": "flood-battery",
                "passed": True,
                "note": "Synthetic inspection evidence",
                **change,
            }
        )


def test_duplicate_and_incomplete_policy_rejected():
    """Configuration never silently overwrites duplicate IDs or leaves required kinds unbounded."""
    policy = example_policy().model_dump()
    with pytest.raises(ValidationError):
        Profile.model_validate(
            {
                "id": "standard",
                "label": "Duplicate positions",
                "slots": [{"id": "battery", "kind": "battery"}] * 2,
            }
        )
    model = type(example_policy())
    for changes in [
        {"profiles": policy["profiles"] * 2},
        {"limits": policy["limits"] * 2},
        {"limits": policy["limits"][1:]},
        {"warning_percent": 0},
        {"battery_min_capacity_pct": float("nan")},
    ]:
        with pytest.raises(ValidationError):
            model.model_validate({**policy, **changes})
