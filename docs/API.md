<!-- Jason Stys: authenticated endpoint contracts, roles, units, conflicts and evidence-export semantics. -->
# API contracts

Base URL `http://127.0.0.1:8901`. Exact Host and same Origin; no CORS. JSON POSTs require `Content-Type: application/json`, matching `Origin` and session `X-CSRF-Token` except login. GETs are also authenticated unless listed public; cross-site API reads are denied. Server binds loopback, disables proxy identity headers and exposes no OpenAPI/schema browser. Paths/fields are fixed; no user SQL, remote URLs, files, executable commands or callbacks.

| Method/path | Authority | Body / behavior |
| --- | --- | --- |
| GET `/`, `/assets/*`, `/healthz` | Public local | Fixed built UI/assets, content-free liveness |
| POST `/api/login` | Local credentials | `username`, `password`; returns name, live role, CSRF and opaque HttpOnly cookie |
| GET `/api/me` | Staff | Current session identity/role/CSRF |
| POST `/api/logout` | Staff + CSRF | `{}`; immediate revocation and cookie clear |
| GET `/api/workspace` | Staff | Coherent state, current readiness, recent 50 ledger entries and 30 report identifiers |
| POST `/api/aircraft` | Admin | `expected_generation`, `aircraft` opening record |
| POST `/api/components` | Admin | `expected_generation`, `component` opening record |
| POST `/api/policies` | Admin | `expected_generation`, strict `policy`; creates new immutable version |
| POST `/api/swaps` | Technician | generation, aircraft ID, slot ID, component ID or null for removal, note |
| POST `/api/usage` | Operator/technician | generation, aircraft ID, seconds 1–7200, operating cycles 1–100, request_id, note |
| POST `/api/inspections` | Technician | generation, component ID, passed boolean, optional capacity_pct / resistance_mohm, note |
| POST `/api/defects` | Operator/technician | generation, component ID, severity `blocking` or `watch`, note |
| POST `/api/work` | Technician | generation, defect positive ID, note |
| POST `/api/work/verify` | Reviewer | generation, work positive ID, note; different identity, fresh passing inspection and non-defect conditions required |
| POST `/api/retire` | Technician | generation, removed component ID, note; irreversible |
| POST `/api/assessments` | Staff | generation, assumptions `{daily_seconds: 0..86400, daily_cycles: 0..100}` |
| GET `/api/assessments/{id}` | Staff | Immutable inputs/findings/digest + computed staleness and optional acknowledgement |
| POST `/api/assessments/{id}/review` | Reviewer | note; cannot be creator; non-stale, not previously acknowledged |
| GET `/api/assessments/{id}/export` | Staff | Private JSON attachment, preserves stale/bad findings |
| GET `/api/evidence/export` | Staff | Full state/hash chain; includes private maintenance notes, excludes users/passwords/sessions |

`generation` above means required integer `expected_generation`. Every string note is 10–500 characters. Strict types/no extra fields. IDs: lowercase letter then 2–39 lowercase alphanumeric/hyphen characters. Serials: 3–60 uppercase alphanumeric/hyphen characters. Units are integer operating seconds/cycles, inspection intervals in days (24h each), capacity percentage and resistance milliohms. Server owns time, current counters, installation attribution, actors, roles and integrity fields. Exact fields/ranges: [`models.py`](../workbench/models.py), mapped in [source navigation](SOURCE_MAP.md).

Opening aircraft: `id, serial, label, profile, opening_seconds, opening_cycles, history_complete, source_note`. Component substitutes `kind` for profile. Kinds: battery, motor, propeller, airframe, payload, assembly. Immutable policy has `label, reference, profiles[{id,label,slots[{id,kind}]}], limits[{kind,seconds,cycles,inspection_days}], warning_percent, battery_min_capacity_pct, battery_max_resistance_mohm`. Required kinds need unique limits. Duplicated profiles/slots/limits are errors. A policy that removes an existing aircraft's profile/position creates an explicit unknown finding, not invented compatibility.

Example usage body (replace generation with one deliberately read from workspace; request ID must be newly random per logical event):

```json
{"expected_generation":1,"aircraft":"flood","seconds":120,"cycles":1,"request_id":"0123456789abcdef0123456789abcdef","note":"Synthetic two-minute exercise, not a real flight"}
```

Usage returns dashboard plus `write:{id,duplicate}`. Retry the **exact** body/key as the same actor only after an ambiguous response. Changing generation or note is not an exact retry. The UI retains pending body in memory only; after reload/logout, inspect the private ledger before manually resubmitting uncertain use. Other state mutations return the dashboard. Assessment creation/review return a report, not a dashboard.

Errors: 400 bad Host, 401 no/expired/revoked session, 403 Origin/CSRF/role denial, 404 unknown record, 405 unsupported method, 408 body read deadline, 409 competing generation/identity/idempotency/domain/capacity conflict, 413 body too large, 415 non-JSON, 422 strict schema/contradictory evidence, 429 login/hash/body-reader capacity, 503 uninitialized/broken evidence integrity. Do not replay 409 automatically. Validation diagnostics return field/type, not submitted password/note values. SQLite uniqueness details and private paths are not returned.
