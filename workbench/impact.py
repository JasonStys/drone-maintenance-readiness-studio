"""Jason Stys: hypothetical standards impact without changing life records. Map: docs/SOURCE_MAP.md.

Functions and bindings are indexed there. The draft is not ledger-verified or
published; both results use identical records, server time and explicit workload.
"""

import copy

from workbench.engine import evaluate
from workbench.models import Assumptions, Policy


def policy_impact(state: dict, policy: Policy, at: float, assumptions: Assumptions):
    """Compare all aircraft/parts, preserving findings and exact deadlines as well as statuses."""
    hypothetical = copy.deepcopy(state)
    next(
        record
        for record in hypothetical["policies"]
        if record["version"] == state["policy_version"]
    )["content"] = policy.model_dump()
    before, after = evaluate(state, at, assumptions), evaluate(hypothetical, at, assumptions)
    changes = {}
    for kind in ("aircraft", "components"):
        previous = {row["id"]: row for row in before[kind]}
        changes[kind] = [
            {
                "id": row["id"],
                "before": previous[row["id"]],
                "after": row,
                "changed": previous[row["id"]] != row,
            }
            for row in after[kind]
        ]
    return {
        "before": before,
        "after": after,
        "changes": changes,
        "draft_policy": policy.model_dump(),
        "published": False,
        "flight_authorization": False,
        "notice": "UNPUBLISHED POLICY IMPACT. Same recorded fleet, server time and workload assumptions. No policy, life counter, ledger, assessment or review is changed. Draft results are hypothetical, not verified ledger records or service/flight authorization.",
    }
