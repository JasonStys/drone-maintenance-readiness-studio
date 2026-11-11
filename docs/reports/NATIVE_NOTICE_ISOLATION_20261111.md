<!-- Jason Stys: actual Windows main-run notice fixture failure, strict process isolation and unchanged runtime boundaries. -->
# Native notice-fixture isolation — 2026-11-11

The Windows core job 130332216576 in [main Validation 42962539050](https://github.com/JasonStys/drone-maintenance-readiness-studio/actions/runs/42962539050) failed on source 52e75c892ee2d57a01d3f89915515ef8b0235aaf. Its first actual Tcl notice-reader test raised a blank TclError with errorCode NONE; 189 other tests passed. Original browser acceptance, the other core platforms, desktop three-OS and CodeQL passed. The failure is retained, not rerun away or relabelled as a passing main.

The precise interpreter/capture interaction was not established. No production notice reader was changed: unexpected open/read errors still fail closed; only genuine ENOENT permits a narrowly reviewed alternative notice source.

## Correction

All 13 real notice cases now execute together in one fresh owned process with capture=sys and stable native descriptors for the interpreter lifetime. Their original test function/parameter/assertion ASTs are identical to the failed-main source. The ordinary package suite contains one mandatory parent wrapper that requires child exit 0, exactly 13 distinct JUnit cases, zero skips/failures/errors and fresh source-bound receipt data. The native packager invokes this same wrapper before freezing; its build job installs the existing development and packaging hash locks. There are no retries, capture-based skips, fabricated notice bytes or fallback successes.

A real child assertion was deliberately changed in a private sensitivity check. The mandatory parent failed exit 1; exact original source bytes were restored and all 13 cases passed again. The receipt retains every actual case ID plus case/reader source SHA256. No earlier runtime, user store, schema, role, authentication or UI logic is changed.

## Local validation

- 178 parent Python tests passed, including the mandatory child wrapper; all 13 actual isolated notice cases passed. This replaces the earlier 190 flat count transparently rather than adding them twice.
- Branch-aware workbench coverage remains 96.24% against the unchanged 90% floor and denominator.
- Ruff, formatting, current source/file navigation and original public-source/privacy/payload gates passed.
- Existing actual native/role/browser assertions and all workflow deadlines remain active. A fresh exact-head hosted run and new merged-main checks must pass before release. Previous package measurements stay bound to their original source commits.

This is a test/build acceptance lifetime correction, not a new product feature or an installer transaction. Trusted OS-owner administration, unsigned-portable scope, unencrypted local storage and the original synthetic maintenance/non-flight-control limitations are unchanged.
