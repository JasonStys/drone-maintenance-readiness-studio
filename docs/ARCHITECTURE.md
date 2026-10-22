<!-- Jason Stys: system model, invariant reasoning, accepted ADR and resource/complexity bounds. -->
# Architecture and ADR 001

Status: accepted. Scope: one trusted local staff organization, small bounded fleet, browser desk backed by a local Python process. No device integration or operational flight authority.

## Decision and alternatives

Use a pure Python assessment engine, strict Pydantic contracts, FastAPI, SQLite transactions and a small TypeScript/HTML/CSS interface. SQLite avoids cloud setup and keeps records local; its one-writer model suits this bounded ledger, not a large multi-tenant SaaS. PostgreSQL would suit a separately designed hosted release but adds deployment/access-control/backup work outside this release. A frontend-only file/localStorage design was rejected because it cannot enforce staff roles or atomic cross-aircraft part attribution. A probabilistic/AI battery-life model was rejected because no validated training or manufacturer fleet data exists.

The pure engine uses identity indexes for components, latest inspection IDs, open defects, required slots and installed positions. Its work is O(R + S + F), where R is the number of domain records, S required positions and F emitted findings; fixed bounded policy profiles/kinds are also read. Memory is O(R + S + F). SQL snapshots/state serialization and chain validation are O(B + L), where B is serialized domain bytes and L ledger bytes. Writes read/verify, mutate and seal within one `BEGIN IMMEDIATE`; this favors auditable correctness over unbounded write throughput. Immutable report snapshots intentionally duplicate input data. These are algorithmic bounds, not measured Big-O conclusions from timing samples. UI joins use bounded scans and are not advertised as a large-fleet optimized virtual grid.

## Invariants and sequence

1. Exact loopback Host/Origin and write CSRF checked before body parsing; typed schemas reject extra fields, coercions and NaN/infinity.
2. Begin a serialized write; verify full ledger chain and latest state digest; enforce live server-side role and displayed global generation.
3. Check domain constraints before mutation. SQL enforces unique active component and position. Failed operations close/roll back the transaction.
4. Update real installed identities/counters, increment generation, append a hash sealing canonical full state, commit atomically.
5. Show coherent state; any old assessment is stale after a domain change. No automatic replay of competing edits.

Usage adds exactly its seconds/cycles to the aircraft and each currently installed component. Missing positions do not prevent honest recording of actual use; they do prevent affirmative readiness. No backdating or client-selected attribution. A request's actor + exact body + generation is bound to a 32-hex key. An exact retry is recognized before generation rejection; changed content/actor conflicts. This protection lasts while the immutable record remains in this workspace. Other commands are not blindly retried.

Opening identity, history attestation and counters are immutable through APIs; usage increments but never resets lifetime. Removal preserves life; retirement is irreversible and requires removal first. Recreating a serial cannot reset it. The app does not import or reconcile unknown external history; a bad baseline needs accountable investigation, not an edit-to-green workaround.

For corrective work: open defect → technician completion → later passing component inspection → different reviewer verification. Inspection generation must exceed work-completion generation. The reviewer cannot bypass incomplete history, retirement, hard life/inspection limits or missing/bad battery observations. Each work order closes only its own defect; unrelated defects remain open and continue to block or warn. This avoids two repairs deadlocking while preserving all unresolved findings. An administrator is not an override reviewer.

## Assessments and time

Precedence is `blocked > unknown > review > within_recorded_limits`; all findings are retained. Limits and inspection expiry block at equality; warning bands use integer multiplication to avoid floating rounding. Battery capacity/resistance equality is allowed; missing either is unknown. A passing inspection never closes a defect. Operating cycles are not inferred full-equivalent battery cycles.

Planning takes explicit daily seconds and operating cycles. Minimum remaining-limit/rate is a constant-workload scenario, not probability, physical degradation, an inspection schedule or empirical remaining useful life. A zero rate has no finite usage estimate. Default dashboard scenario: 1,200 seconds / 2 cycles per day, also shown by the assessment form. Deadlines are UTC epoch seconds; displayed dates use browser locale. Assessments expire at the earliest upcoming inspection deadline or 24 hours and are stale on clock rollback or any domain-generation change. Historical report content is never rewritten to look current. A reviewer may acknowledge even blocked evidence for triage; acknowledgement never changes findings or grants flight permission.

## Bounds and accepted limitations

Maximums: 50 aircraft, 200 components, 20 policies, 1,000 usage entries, 1,500 inspections, 1,000 defects, 100 full-input assessments, 5,000 ledger generations; up to 8 profiles / 16 required positions and 6 component kinds. Lifetime counters at most 10^12. Each note is 10–500 characters; each JSON request at most 64 KiB with a five-second read deadline and four concurrent body readers. Uvicorn bounds concurrent connections at 24. These caps prevent unlimited growth but are not a validated maximum-capacity performance SLA. Report storage can still be significant; monitor disk capacity and private backups. The minimum viable profile has at least one slot; the business owner is responsible for comprehensive controlled profiles/limits, not the software.

Database readers use coherent transactions. Hash chains detect ordinary content mutation/truncation, not deletion/replacement of the entire database or privileged recomputation. No cryptographic signing, trusted clock, external notarization, hardware measurement attestation, encrypted database, multi-tenant isolation or manufacturer validation is claimed. Real deployments need those risks reviewed independently.
