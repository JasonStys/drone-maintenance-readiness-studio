# Drone Maintenance Readiness Studio handbook

By Jason Stys.

Compare unpublished maintenance standards against the same ledger, time and workload, exposing component findings and deadline deltas.

Lets authorized reviewers assess standards changes before altering maintenance records or policy.

## Read the documentation

| Edition                                          | Audience and contents                                                                       |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| [project-guide.docx](reports/project-guide.docx) | User and developer guide: purpose, current usage, design, boundaries and source references. |

The editable Markdown remains the maintenance source. The Word files are readable editions, and the workbook is an evidence index rather than a test runner. See [publication identities and review](reports/publications.json) and the [documentation refresh record](reports/documentation-refresh-2026-11-09.md).

## Current usage and help

[README quick start](../README.md) is the entry point. Use the project-specific guides below before changing inputs, operating modes or deployment assumptions.

### Usage and operations

- [OPERATIONS](OPERATIONS.md)
- [USER GUIDE](USER_GUIDE.md)

### Design and contracts

- [API](API.md)
- [ARCHITECTURE](ARCHITECTURE.md)
- [RESEARCH](RESEARCH.md)

### Security and validation

- [SECURITY](SECURITY.md)
- [TEST PLAN](TEST_PLAN.md)
- [VALIDATION](VALIDATION.md)

## Historical results and reproduction

The reviewed source is [`50109b28e90285a63bbb07ad7a0d146bc6b404c9`](https://github.com/JasonStys/drone-maintenance-readiness-studio/tree/50109b28e90285a63bbb07ad7a0d146bc6b404c9). The observed functional workflow baseline is `50109b28e90285a63bbb07ad7a0d146bc6b404c9`; those observations are recorded at `2026-11-10T05:25:40.628667+00:00`. They do not certify an unrun later revision.

- [Detailed recorded validation](reports/PRACTICAL_WORKFLOWS_20261109.md)
- [Current Actions](https://github.com/JasonStys/drone-maintenance-readiness-studio/actions) records later integration checks separately.
- Preserve dated measurements and follow the existing testing guide to reproduce them; a test-source inventory alone does not establish execution.

## Practical boundaries

- Hypothetical configured thresholds and constant workloads, not manufacturer approval or probabilistic component-life predictions.
- Draft comparisons do not publish a maintenance standard, alter the ledger or authorize service/flight.
- No live fleet/hardware integration is supplied; local data is unencrypted and trusts the OS owner.
- Source-first project with current package/service validation; no public native desktop application release is supplied.

## Maintaining these editions

Update the editable usage/design/test documents first. Rebuild and visually review every Word page and workbook tab before replacing an edition; verify the exact binary digests and evidence source in publications.json. Keep account data, logs with secrets, installed-app state and private test stores out of documentation. Source and release assets retain their existing security and licensing boundaries.
