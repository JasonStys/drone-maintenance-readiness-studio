<!-- Jason Stys: operator, technician, reviewer and administrator help with evidence interpretation and recovery. -->
# Using the maintenance desk

All accounts are provisioned by an OS-authorized owner using the CLI. No default production password exists. All signed-in roles share the same fleet and private notes—do not use this release for separate tenants. Author/contact links appear in the page footer.

## Read before acting

Roster findings mean **recorded evidence only**. Within recorded limits is not “safe to fly.” Unknown means missing history/inspection/profile/requirements; it never means a pass. Review means a warning band/watch item needs human attention. Blocked means a hard limit, overdue/failed inspection, retirement, incompatible part or open blocking defect. The highest-severity finding sets the badge but the component desk lists all reasons. A parent aircraft also needs its own complete history and all required positions.

Refresh records to obtain the latest coherent generation and time-based findings. A displayed dashboard is a point-in-time view, not live telemetry; keep refreshing before decisions. The backend rechecks report expiry/inspection deadlines before acknowledgement/verification. Browser/system time is not a trusted instrument. Always perform required physical checks using applicable controlled instructions.

## Operator

Select an aircraft; inspect its serials, use and deadlines. Record actual operating minutes/cycles with a useful private evidence note. The UI takes whole minutes; API accepts individual seconds. Recorded operation is preserved even for a blocked aircraft, because suppressing bad evidence would corrupt maintenance history. No automated event import/backdating is supported. Report a watch or blocking component defect using the selected component.

If the network loses the usage response, click **Retry pending usage safely**. The same request/body/actor is recovered exactly once; do not create a second logical event. The pending body is memory-only: after a reload, logout or browser crash, check the ledger/recorded totals before entering uncertain usage again. A 409 requires explicit refresh/investigation, not repeated clicks or a new key to force acceptance.

Capture a fleet assessment with explicit daily workload assumptions. A rate of zero has no finite usage estimate. Download full JSON to inspect the exact input and result, not only a badge. Reports retain their earlier policy and evidence; any domain change makes them stale globally, even if a different aircraft changed. Report acknowledgement is not flight clearance.

## Technician

Choose the aircraft position and incoming serialized component, or removal only. Compatibility/installation/retirement checks are atomic; failed swaps do not remove the current part. Removed parts retain all their cumulative use. Record a current physical inspection, including observed battery capacity/resistance when applicable; leaving a value blank yields unknown battery evidence. These are entered observations, not computed measurements. A failed inspection creates a separate blocking defect. A later pass does not erase it.

Choose an open defect and record completed work. It stays open. Record a **later** passing inspection of that component, then have a different authorized reviewer verify the work. Each repair closes only its own defect; other defects continue to count. A reviewer cannot override hard limits or incomplete history/battery health evidence. A warning can remain after a repair is verified.

Retirement requires prior removal and explicit confirmation. It is irreversible in this workspace; no restore/delete/reset route exists. It is a recordkeeping action, not physical disposal guidance. Correct mistaken identities/baselines with the accountable record owner; do not invent new serials to reset life.

## Reviewer

Verify completed work only after independently checking evidence and actual process requirements. The app enforces a different account from the technician and a newer passing inspection; it cannot prove that two accounts are two people or that physical work occurred. Acknowledge current fleet reports for triage, including reports with blocked/unknown findings. Acknowledgement does not change those findings; self-acknowledgement and stale/duplicate acknowledgements are denied.

## Administrator

Expand **Administrator · controlled standards and opening records**. Publish strict policy JSON derived from independently approved applicable instructions; every bundled value is fictional. Create immutable aircraft/component opening records. Do not attest complete history without evidence. Duplicate serials, duplicate requirements, extra properties and malformed units are rejected. The JSON editor is intentional explicit configuration, not a free-text AI prompt or code execution feature. Admin cannot bypass technician/reviewer separation.

## Troubleshooting

- Uninitialized/503: use the trusted CLI `init`; preserve and inspect evidence rather than deleting corrupted records.
- Conflict/409: refresh, inspect what changed, then decide whether a new deliberate action is warranted. Never retry a different usage body under the same key.
- Session expired: sign in again; server sessions expire after one hour. Sign out clears private DOM immediately and revokes the server token. If sign-out revocation fails, close the browser session.
- Capacity reached: stop and archive/private-backup the workspace; there is no automatic evidence deletion. Design a reviewed migration before larger-scale use.
- Missing UI: run `npm run build`. Only the built static directory is served, never source/runtime files.
- Sign-in throttled: wait one minute; do not weaken the guard or spoof forwarding headers. Incorrect passwords and successful logins both consume the per-client budget.

Help limitations: no regulatory certification, live drone integration, battery diagnostic hardware, flight scheduling, full-equivalent charge-cycle inference, missing-history reconstruction, cloud multi-tenancy or native installers.
