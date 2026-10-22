<!-- Jason Stys: local trust boundaries, explicit threats, controls and residual privacy/security risks. -->
# Security and privacy model

Assets: private staff identities, password hashes, session bearers, maintenance notes, history, policies, work evidence and reports. Trust boundary: exact loopback browser origin → authenticated typed API → SQLite transactions on a protected local filesystem. All signed-in staff intentionally read the same organization. There is no multi-tenant confidentiality boundary.

| Threat | Implemented control | Residual risk |
| --- | --- | --- |
| Drive-by browser writes / DNS rebinding | Exact 127.0.0.1:port Host/Origin, CSRF, SameSite Strict cookie, no CORS, cross-site reads denied | Not a defense against malicious local processes/browser extensions or an OS owner |
| Credential guessing / resource exhaustion | Argon2id 64 MiB/3 iterations/1 lane; 2 concurrent verifiers; 20 attempts/direct client/minute; 1,000 client rows; bounded bodies/records/connections | Loopback staff share a throttle budget; no Internet-scale DoS claim |
| Cookie/role forgery | Random opaque bearer, only SHA-256 digest stored, 1h absolute expiry, live server-side role, max 10 sessions/user, logout revocation | Local HTTP cookie is not Secure; never expose this build over a network |
| Injection / unsafe content | Parameterized fixed SQL, strict contracts, no execution/fetch/upload interface, textContent-only private rendering, self-only CSP, no inline/third-party scripts | Arbitrary code/extension/OS compromise is outside app isolation |
| Cross-account role bypass | Store role checks and API sessions independent of UI buttons; technician/reviewer identity separation | Separate accounts do not prove separate people or true physical work |
| Lost responses / competing edits | Actor/content-bound usage idempotency and global CAS; serialized atomic swaps and counter updates | No durable browser outbox: inspect ledger after browser crash/reload before manual resubmission |
| Erased or tampered maintenance evidence | No API delete/reset; immutable record triggers, full-state hash chain checked on every domain read/write; report/review hashes | OS/DB owner can replace database, recompute all hashes, read secrets or alter system time; hashes are not signatures |
| Stale favourable reports | Original full inputs preserved, generation/deadline/clock rollback checks, backend rejects stale acknowledgement | Dashboard needs deliberate refresh; no trusted clock or hardware attestation |
| Unauthorized export | Authenticated attachment endpoints; no account/session/password data in domain export | Exports contain private notes/serials; anyone receiving them can read them |

No runtime network calls, model services, ad scripts, remote fonts, tracking, telemetry, embedded advertising or popups are included. Development dependency installation/audits and GitHub CI do contact official registries, advisory services and GitHub. CSP restricts app scripts/connections but is not an OS ad blocker or protection against a compromised browser extension.

`.runtime`, `.venv`, node_modules, DBs, logs and generated results are ignored and checked before publication. SQLite and synthetic credentials are **not encrypted by this app**. Restrict directory/backups to approved OS users, use disk encryption and do not store real sensitive fleet data until an accountable operator reviews requirements. Jason Stys has no remote data collector in this app; a person with OS access still has OS-owner powers. No claim that the machine owner cannot read local data is made.

Account provisioning is CLI-only. Do not distribute demonstration credentials as production defaults. No password-reset/signup bypass exists. Remove compromised sessions using authorized offline operations after stopping the service; never hand-edit domain records to clear a warning. Logs suppress access URLs and response validation does not reflect submitted private values. The ledger stores maintenance notes/actor names intentionally for accountability, not passwords.

Not a penetration-test certification, security compliance certification, flight approval or production SaaS. See the measured [validation](VALIDATION.md) and [operations](OPERATIONS.md), plus root [security reporting](../SECURITY.md).
