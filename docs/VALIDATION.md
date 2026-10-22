<!-- Jason Stys: measured local checks, known limits and commit-specific hosted verification evidence. -->
# Validation evidence

Local measurements: 2026-10-22 UTC, Windows 11 build 26300, Python 3.14.6, Node 24.18.1. All data is original synthetic data. This file reports observed checks, not manufacturer, legal, flight or security certification.

| Check | Observed result |
| --- | --- |
| Python real engine/SQL/API/contracts/auth/network/CLI and audit-policy tests | 84 passed; branch-aware package coverage 98.45% (engine 100%); gate 90% |
| TypeScript presentation helper tests | 4 passed; 100% lines/statements/functions/branches for `view.ts` |
| Strict TypeScript + Vite build | Passed |
| Ruff lint/format | Passed |
| Actual-service browser acceptance | 16 passed: four journeys each in Chromium, Firefox, WebKit and mobile WebKit; zero retries |
| Automated accessibility and responsive checks | No Axe WCAG 2 A/AA / 2.1 AA findings in tested signed-out/in states; no page horizontal overflow |
| Manual local UI acceptance | Recorded two synthetic minutes, observed 60→62 minute aircraft/component totals, captured current immutable fleet assessment; retained blocking fleet finding and flight_authorization false |
| Live pip-audit, fully locked dev/runtime graph | No known vulnerabilities |
| Google OSV-Scanner v2.7.0 live complete npm lock scan | 81/81 dependency identities, 0 findings, no ignored advisories |

## Hosted evidence

Implementation revision `78c2afadf52be43057aef92bd9e1b2a66a8959e4` passed all five [Validation jobs](https://github.com/JasonStys/drone-maintenance-readiness-studio/actions/runs/39736534532): Linux Python 3.12/3.14, Windows/macOS Python 3.14 and actual-service Chromium/Firefox/WebKit/mobile acceptance. Both [CodeQL languages](https://github.com/JasonStys/drone-maintenance-readiness-studio/actions/runs/39736534491) completed successfully; the API reported zero analysis results and zero open alerts for that revision.

Final follow-up also makes the related private ledger/usage scroll regions keyboard-focusable and opens the evidence/help sections during the unchanged full Axe check. Its exact-commit workflow results are available from [Actions](https://github.com/JasonStys/drone-maintenance-readiness-studio/actions); verify the newest main SHA rather than assuming an earlier green revision certifies a later one. This document links immutable completed evidence, not a circular assertion about its own future workflow result.

Read-only storage check at 2026-10-21 23:53 -07:00: 102 repositories, 62,959,952 artifact bytes, separate caches 8,185,324,614 bytes, quota percentage unavailable. This repository had zero artifacts and zero cache bytes. No cleanup, retention or billing changes were made.

## Performance and review notes

Measured benchmark after installed-position indexing: original 3-aircraft / 10-component / 1-ledger-entry snapshot, no concurrent writers. Warm once. Pure engine 100 measured iterations: median 0.053 ms, maximum 0.123 ms. Real verified SQLite dashboard 30 iterations: median 1.125 ms, maximum 1.517 ms. Numbers are local observations, vary with hardware/load, and are not timing gates or maximum-capacity/operational SLAs. Rerunning `python -m tools.benchmark` reports the current host result rather than assuming these exact numbers. The indexed engine performs a linear traversal, not repeated aircraft-by-installation scans.

Built payload budgets: JavaScript 4,531 gzip bytes / 40,000; CSS 1,904 / 12,000. Source/file navigation and publication hygiene checks passed for 61 files. No private runtime/dependencies/build output were staged.

Review found and corrected multi-defect repair deadlock: work verification now checks independent non-defect life/history/health evidence while closing only the target defect. A regression proves the sibling stays blocking until its own verification. Browser development caught an assertion wording mismatch (actual persisted duplicate recovery was correct) and a real mobile grid/select overflow; the viewport assertion remains enabled. The first hosted run passed all four core platform jobs and both CodeQL languages, but Linux mobile WebKit caught a keyboard-inaccessible scrolling component table. The fix makes that region named and focusable, with a direct focus regression plus the unchanged Axe gate. No test retries, advisory suppression, coverage exclusions or readiness-limit relaxation were used to pass.

Known upstream warning: FastAPI's imported Starlette TestClient emits a deprecation notice about httpx/httpx2. Actual API, TCP and four-engine browser checks remain exercised; the warning is not hidden. Migration can be reviewed when the pinned compatible test transport changes.

Limits: no hardware/drone testing, measured battery aging model, physical inspection proof, actual manufacturer thresholds, native installers, public-hosting certification, independent penetration audit, full manual accessibility audit or maximum-capacity SLA. Dashboard findings require refresh; final authority remains with responsible humans using applicable procedures. Private credentials, databases and generated detailed reports stay outside Git. GitHub logs contain synthetic checks only; workflows do not upload artifacts or caches.
