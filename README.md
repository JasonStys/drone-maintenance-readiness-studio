<!-- Jason Stys: purpose, executable quickstart, feature/implementation guide and evidence index. -->

# Drone Maintenance Readiness Studio

By [Jason Stys](https://github.com/JasonStys) Â· [Contact / LinkedIn](https://www.linkedin.com/in/jason-stys-31b30b351/)

A local, authenticated maintenance desk for tracing **serialized drone components, lifetime usage, inspections, defects and independently verified corrective work**. A component's recorded life follows its physical identity across aircraft swaps; replacing a battery never erases its earlier use. The interface explains exactly which records block an assessment and which missing records make it unknown.

**Portfolio / educational software, not flight authorization, airworthiness certification, manufacturer instructions, a maintenance approval or a failure-prediction model.** Every bundled aircraft, serial, inspection and threshold is fictional. No drone connection, flight command, tracking, targeting or real fleet data is included. A responsible human must follow applicable instructions, preflight checks and legal requirements; a positive record-based finding is not permission to fly.

## What works

**Preview standards before publication:** an administrator can edit Policy JSON,
choose the explicit daily-workload assumptions and preview how the draft affects
the recorded fleet. Both evaluations use identical records and one server time.
The UI and downloadable comparison show every aircraft/part's status, findings,
remaining configured seconds/cycles and inspection deadlines. Source generation,
verified ledger tip/state digest and draft-policy digest identify the inputs.

This is a read-only hypothetical comparison: no policy version, ledger entry,
usage counter, assessment or review is created. Unknown history, failed inspection,
open defects and missing required slots remain visible. Admin role, CSRF, verified
source ledger and current-generation guards apply. Draft or workload edits clear
old output. See [validation and limits](docs/reports/PRACTICAL_WORKFLOWS_20261109.md).

- **Fleet and lifecycle desk:** filter aircraft by finding, inspect installed serials, cumulative seconds/operating cycles, remaining configured life, inspection deadlines, complete findings and a recorded-use chart. Assembly-level records do not pretend to track every rotor individually.
- **Controlled standards:** administrators publish immutable profiles, required positions, kind-specific time/cycle/inspection limits, warning bands and battery observation thresholds. Missing/changed requirements remain visible; opening-history attestations cannot be rewritten through the application.
- **Atomic swaps and exactly-once usage:** a part cannot be installed twice, mismatched or reinstalled after retirement. The server attributes usage to the actual installed parts. An explicit retry recovers an ambiguously successful request without double-counting; stale competing edits are rejected.
- **Evidence-first repair workflow:** a failed inspection creates an open defect. Completing work or recording a later pass does not close it. A different reviewer must verify completed work after a fresh passing inspection; hard life/health/history problems cannot be overridden. Separate defects remain separate.
- **Reproducible assessments:** immutable full inputs, active policy, ledger tip, explicit workload assumptions, findings and SHA-256 digest. Reports become stale after any domain change, clock rollback, inspection deadline or 24 hours, whichever applies first. JSON downloads retain blocked/unknown/stale findings honestly.
- **Private local staff accounts:** operator, technician, reviewer and administrator roles; Argon2id passwords, opaque expiring sessions, CSRF/origin checks and server-side authorization. All staff intentionally share one organization's records. No public signup, cloud uploads, external scripts, analytics or model APIs.
- **Tamper-evident ledger:** each domain mutation seals the complete normalized state and previous entry. This detects ordinary record/chain alterations, **not** a privileged database owner rewriting all hashes. It is not a signature or proof that a physical inspection occurred.

## Complete desktop application candidate

The 0.2.1 source includes the complete authenticated application, native **profile / first-account / staff / Open / Quit** controls, private persistent profiles and real JSON-file draft import/export. It packages patched Python3.14.10 and actual Tcl/Tk with their notices; no Python/Node installation is required for an extracted release. Prepared examples stay inside the original full application. See [desktop usage, trust boundary and reproducible package validation](docs/DESKTOP.md) and [dated candidate results](docs/reports/DESKTOP_CANDIDATE_20261110.md). This is a source candidate until exact-source hosted acceptance and publication finish; earlier documentation remains tied to its original revision.

The 0.2.1 patch refuses profile paths through symbolic links, Windows junctions/reparse points, linked database/identity files or frozen application directories **before workspace writes**. Existing ordinary external profiles, accounts, roles and records retain their schema and cookie namespace. [Path-admission evidence and limits](docs/reports/PROFILE_PATH_ADMISSION_20261111.md).

## Run locally

Prerequisites: Python 3.12â€“3.14, Node.js 24 and npm. CI tests Python 3.12/3.14 on Linux and 3.14 on Windows/macOS. The source CLI remains available; the portable desktop candidate adds native owner controls around the same browser application. Neither is a signed mobile installer or publicly hosted service.

Windows PowerShell, from the cloned repository:

```powershell
python -m venv .venv
.venv/Scripts/python -m pip install --only-binary=:all: --require-hashes -r requirements.lock
npm ci --ignore-scripts --no-audit
npm run build
.venv/Scripts/python -m workbench init --examples
.venv/Scripts/python -m workbench user owner --role admin
.venv/Scripts/python -m workbench user mechanic --role technician
.venv/Scripts/python -m workbench user inspector --role reviewer
.venv/Scripts/python -m workbench user pilot --role operator
.venv/Scripts/python -m workbench serve
```

Open **http://127.0.0.1:8901/** and use the local accounts you just provisioned. Passwords are prompted privately, not command-line arguments. On Linux/macOS use `.venv/bin/python` in place of `.venv/Scripts/python`. Omit `--examples` for an empty fleet; even its initial policy is illustrative and must be replaced with appropriately controlled standards before any real recordkeeping. Initialization never overwrites an existing workspace. A separate workspace can be selected using `python -m workbench --db PATH init` (global option before the subcommand).

Do not expose this loopback HTTP release on a LAN or the Internet. Protect the runtime directory and backups with OS permissions and disk encryption; the application does not encrypt SQLite against the machine owner. See [operations](docs/OPERATIONS.md) and [security](docs/SECURITY.md).

## Try the original scenarios

1. **Synthetic flood-response unit:** complete recorded opening history and passing inspections, within fictional configured limits. Record two minutes of usage; verify attribution to all three installed identities.
2. **Synthetic infrastructure unit:** blocking propulsion-assembly defect and a near-life battery. Complete corrective work, add a fresh passing inspection, then sign in as a different reviewer to verify. The battery's warning remains; repair does not make the whole aircraft clear.
3. **Synthetic training unit:** missing battery history/inspection. It stays unknown, not optimistically passed. A new inspection cannot manufacture missing lifetime history.
4. **Spare battery:** swap into the flood-response unit. Compare the removed battery's unchanged cumulative life with the spare's own opening life. Failed/double installations roll back atomically.

The [user guide](docs/USER_GUIDE.md) explains each role, form, result and recovery path. The application includes a help section and author/contact links.

## Design and file guide

Python handles typed domain rules, HTTP authentication and atomic ledger operations; SQL supplies constraints/transactions; TypeScript handles role-aware interaction and safe text-only rendering; HTML/CSS provide an accessible responsive desk. No extra language is added merely for a badge.

| Path                                                      | Major responsibility                                                                                 |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `workbench/models.py`                                     | Strict finite unit-explicit policies and write contracts                                             |
| `workbench/engine.py`                                     | Pure readiness findings, exact thresholds, deadline and workload calculations                        |
| `workbench/store.py` / `schema.sql`                       | Serialized lifecycle, transaction/CAS/idempotency, repair verification and hashed evidence           |
| `workbench/auth.py` / `api.py`                            | Local credentials, live roles, browser boundaries, private endpoints and fixed static assets         |
| `workbench/__main__.py` / `examples.py`                   | Trusted setup/launch commands and original fictional scenarios                                       |
| `ui/index.html`, `ui/src/main.ts`, `style.css`, `view.ts` | Responsive forms, roster, chart, reports and pure presentation helpers                               |
| `tests/`                                                  | Domain, real SQLite/API, concurrency, contracts, security, launcher and browser regressions          |
| `tools/`                                                  | Isolated browser service, measured benchmark, full-lock OSV audit and exact source-navigation checks |
| `.github/workflows/`                                      | Cross-platform validation and Python/TypeScript CodeQL; no artifact/cache uploads                    |
| `docs/`                                                   | Architecture/ADR, API, help, threat model, operations, research, test plan and measured evidence     |

Every tracked file is described in the generated [file catalog](docs/FILE_CATALOG.md). Source headers point to the generated [exact declaration/parameter/variable line map](docs/SOURCE_MAP.md), preventing manually maintained line comments from becoming stale. Functions/classes carry their own responsibility documentation. Complexity and bounded-workspace tradeoffs are documented in [architecture](docs/ARCHITECTURE.md).

## Validate

Install `requirements-dev.lock` instead of the runtime lock, then:

```powershell
.venv/Scripts/python -m ruff check workbench tests tools
.venv/Scripts/python -m ruff format --check workbench tests tools
.venv/Scripts/python -m pytest --cov=workbench --cov-report=term-missing
npm run format:check
npm test
npm run build
.venv/Scripts/python tools/docs_index.py --check
.venv/Scripts/python tools/check_repo.py
.venv/Scripts/python -m tools.benchmark
.venv/Scripts/python -m pip_audit --disable-pip --no-deps -r requirements-dev.lock
.venv/Scripts/python tools/audit_osv.py
npx playwright install chromium firefox webkit
npm run test:e2e
```

On Linux browser hosts use `npx playwright install --with-deps chromium firefox webkit`. The e2e launcher starts a fresh real service/database per engine; tests do not bypass authentication throttling or retry failures. CI requires at least 90% branch-aware Python package coverage, 100% tested `view.ts` and bounded-file-reader helper coverage, exact committed source maps, compressed payload budgets and live zero-finding dependency scans. Browser acceptance, rather than helper coverage, exercises the full DOM controller.

[Validation results](docs/VALIDATION.md) distinguish measured checks from limits and unknowns. [GitHub Actions](https://github.com/JasonStys/drone-maintenance-readiness-studio/actions) contains the commit-specific results. MIT-licensed original source; see [contributing](CONTRIBUTING.md) and [security reporting](SECURITY.md).

## Documentation editions

Start with the [organized handbook](docs/handbook.md) for current usage, design, security and test guidance. Reviewed downloadable editions: [project-guide.docx](docs/reports/project-guide.docx).

[Publication identities and source scope](docs/reports/publications.json) Â· [Documentation validation record](docs/reports/documentation-refresh-2026-11-09.md). Historical results retain their own tested revision and date.

## Native validation follow-up

The [dated CodeQL quality follow-up](docs/reports/NATIVE_CODEQL_20261111.md) explains explicit owner-interrupt handling and acyclic shared GUI-runtime validation. Release acceptance remains tied to the exact source tested; historical desktop observations are retained.
