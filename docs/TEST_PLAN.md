<!-- Jason Stys: risk-based strategy, independent oracles, negative cases and deliberately unclaimed validation. -->
# Test strategy

Highest risk: falsely favourable readiness, lost component lifetime, double-counted use, unauthorized/self repair approval, erased evidence and leaked private data. Tests use original synthetic fixtures with independent expected values and actual temporary SQLite/API/authentication. Pure engine tests mutate isolated snapshots deliberately; they do not mock the engine's own conclusions as an oracle.

| Layer / file | Evidence checked |
| --- | --- |
| `test_engine.py` | Exact limit/warning equality, inspection expiry/future clock, null vs zero battery data, precedence/all findings, missing profile/position/kind limit/history, compatible parts, no-rate planning, inspection ID order |
| `test_lifecycle.py` | Installed-ID attribution, preserved counters across swaps, atomic rollback, exact duplicate/content conflicts, real concurrent writers, stale generation, independent reviewer/fresh inspection, multi-defect repair independence, retirement and overflow |
| `test_evidence.py` | Immutable full input/digest, stale generation/expiry/clock rollback, self/duplicate acknowledgement, corrupted state/chain/truncation/report/review, all record capacities and failed-inspection rollback |
| `test_contracts.py` | Strict units/types/finite values, bool-vs-int, extra attribution/time fields, duplicate profiles/slots/limits, missing configured kind limits |
| `test_security.py` | Anonymous exports/runtime denial, Host/Origin/CSRF, no reflection, JSON size/type/method, hashed bearer, live role, revocation/expiry, login/hash/client/session capacity and provisioning bounds |
| `test_network.py` | Actual TCP service ignores spoofed forwarding headers for direct-client login throttling |
| `test_cli.py` | Idempotent setup, private prompted provisioning, invalid port, loopback/no-proxy launcher and random disposable browser accounts |
| `test_osv_policy.py` | Incomplete inventories, advisory groups/errors/unknown report data cannot turn the live audit green |
| `ui/src/view.test.ts` | All presentation helper lines/branches including safe numeric DOM IDs, missing/zero values and chart bounds |
| `tests/browser/workspace.spec.ts` | Real lost-response usage retry, SQL-backed swaps/repair, JSON download/input snapshot, XSS text, stale reports/CAS, admin policy, role-aware controls, WCAG automated checks, viewport fit and late-response logout privacy |

Browser suites start independent real services per engine. Only the first successful usage response is deliberately dropped in one test; the operation executes on the actual server, then retry and persisted counters are checked. Logout testing delays an actual workspace response, not a fabricated workspace. No app-auth limit bypass or test retries. Mobile is an iPhone-sized WebKit emulation profile, not physical-device validation. Automated Axe WCAG tags are checks, not a complete accessibility certification.

Gates: Python package branch-aware coverage >=90%; `view.ts` helper coverage 100%; strict TS/no unused locals, Ruff, Prettier, source-map/catalog freshness, fixed SHA workflow refs, private-source hygiene and gzip budgets 40 KB JS / 12 KB CSS. Full DOM-controller coverage is represented by acceptance journeys, not included in the helper percentage. CI runs Linux Python 3.12/3.14, Windows/macOS 3.14 and separate Linux browser suites. Live pip-audit checks the fully locked Python dev/runtime graph; official checksum-pinned OSV checks every npm lock identity including platform-optional packages. Zero known findings is time-sensitive, not proof of no vulnerabilities.

Benchmarks use actual monotonic timing, original three-aircraft/ten-component SQLite fixture and stated iteration counts. They are not a maximum-capacity test, concurrency SLA, physical battery degradation validation, penetration audit or real flight test. No real equipment, actual maintenance limits, real people or outside operational records are exercised. See [measured results](VALIDATION.md).
