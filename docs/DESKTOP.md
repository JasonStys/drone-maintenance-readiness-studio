<!-- Jason Stys: full native application workflow, supported file features and honest local privacy/lifecycle boundaries. -->

# Drone Maintenance Readiness Studio: portable desktop application

The 0.2.0 source candidate packages the project's complete existing authenticated browser application with Python, SQL storage, built TypeScript UI and native Tk owner controls. It is one application, with optional prepared inputs inside it. It is not a signed installer, a cloud service, a native mobile app, or a live aircraft controller. Publication and operating-system acceptance require the exact-source hosted gates; local candidate results do not claim a public release.

## Launch, provision and use

1. Extract the entire verified portable archive into its own directory; keep `_internal`, licenses and RELEASE.json alongside `DroneMaintenanceStudio` (`.exe` on Windows). Never run an executable from an Actions evidence archive.
2. Launch `DroneMaintenanceStudio` normally. The native owner window chooses a new empty folder or an existing identified profile. The default profile is in the signed-in user's local application-data directory, outside the source and executable directories. An unknown nonempty folder is refused; no existing workspace is silently adopted or migrated.
3. Choose **Open private workspace**. Create the first administrator; provision separate technician, reviewer and operator accounts. Set your own 14â€“128-character password and confirmation; there are no default credentials, password command-line arguments, HTTP signup endpoints or plaintext password files. The password widgets clear after each attempt.
4. Choose **Open full application**, sign in with an account you provisioned, and use the genuine role-appropriate project GUI. All staff in this one profile intentionally share the organization's domain records. Other profiles have separate databases and cookies; browser authorization and CSRF checks still apply.
5. Keep the native owner window open while working. Closing a browser tab does not stop the service. Choose **Quit application**, then confirm. Saved accounts and records remain. If active work is still draining, the window and profile lock remain; wait and choose Quit again. A stopped startup failure requires Quit/reopen and exits with a failure status, rather than claiming a successful service.

Choose whether a NEW profile receives the fictional example fleet. With that checkbox clear, the fleet is genuinely empty; its initial policy is still illustrative. An administrator can open Policy JSON, edit a draft, set explicit workload assumptions, compare current versus draft findings without ledger writes, download the exact draft, and explicitly publish when intended. Operators record use, technicians record work and inspections, and a different reviewer verifies corrective work. A later passing inspection alone never closes a defect.

## File and state boundaries

Imported JSON is a draft, not a database/account/history restore. The reader checks actual and advertised byte size (60,000-byte maximum), strict UTF-8, object root, finite numeric data, depth and work budgets. Original server schemas remain authoritative when saving or publishing. Invalid imports retain the previous editor contents. Typing, changing context, a newer import, logout or busy work invalidates older asynchronous results. Downloaded reports preserve the project's source/version/digest and missing/blocked/unknown findings.

Native profile provisioning is trusted **signed-in operating-system session administration**, like the existing local CLI, not an extra authenticated browser role. Anyone controlling that OS session can provision staff and read the local SQLite database. The database is not encrypted against the computer owner. Protect the OS account, files and backups; do not put real passwords, private profiles or exported personal data in GitHub. No outside API, analytics or external script is needed.

The service prebinds only `127.0.0.1` on an ephemeral port. Exact Host/Origin checks, HttpOnly/SameSite Strict sessions, original role checks and CSRF remain enabled. A stable per-profile cookie-name namespace prevents accidental cookie replacement between two same-project localhost profiles; cookies remain host-scoped, **not port-confidential** against another malicious local service or OS owner. Moving a profile requires signing in again. This is not a LAN/Internet deployment or a multi-tenant security boundary.

## Controls and automation

The owner footer remains visible at the 700Ã—600 minimum; the variable-height form/status content scrolls. Cancelled Quit retains the service. A busy Quit does not force termination or release the profile lock.

`--profile PATH` selects a new empty or identified profile. `--no-browser` suppresses automatic browser opening while retaining real native controls. The documented console owner mode `--no-window --no-browser` requires already-provisioned accounts and accepts only `quit` (or Ctrl+C/EOF) to drain the same owned service. `--runtime-info` inspects actual packaged Python/Tcl/Tk identity without touching any profile. No mode creates preset credentials or replaces the project GUI with a canned demonstration.

## Reproduce a package

Use final Python 3.14.10 or a later supported 3.14 security patch, Node.js 24, and the exact locks:

```text
python -m pip install --require-hashes -r requirements-dev.lock -r requirements-package.lock
npm ci --ignore-scripts --no-audit
npm run build
python tools/package_app.py
```

A normal hosted build requires a clean exact checkout. `--allow-dirty` exists only for explicitly labelled local candidates and is refused in Actions. Windows uses ZIP; Linux/macOS use tar.gz with safe path/link/expanded-size checks. Metadata, runtime notices and outer/inner identity must agree. The package is then safely extracted and that executable serves its actual compiled UI; no source-server fallback is allowed. Sidecars are written only after successful acceptance.

The new read-only desktop workflow builds/test-extracts on Windows, macOS and Ubuntu24.04. It preserves original validation/CodeQL/security/coverage/browser jobs, uses pinned Actions and exact dependency locks, and uploads no binary artifacts or caches by default. Linux real Tk tests run under Xvfb. Native Chromium drives the actual extracted executable through the original role workflows, imports, negative cases, exports, responsive accessibility and owned graceful shutdown. Original source browser tests still use all configured browser engines.

## Limits and evidence

All included fleet/scenario/policy values are fictional. The application provides educational evidence review, not dispatch, airworthiness certification, flight permission, prediction of physical safety, or live equipment control. The application is unsigned; archive extraction/launch is not a signed clean-install or uninstall transaction. Automated tests suppress the operating system's default-browser opener; Desktop shortcut and manual OS/browser integration are separate acceptance steps. Existing CLI workspaces are not automatically imported into native profiles.

See [candidate measurements and corrections](reports/DESKTOP_CANDIDATE_20261110.md), [source navigation](SOURCE_MAP.md) and [file catalog](FILE_CATALOG.md). Earlier Office editions and immutable reports retain their own source/date; they are not rebuilt or relabelled by this candidate.

The build acceptance requires the development and packaging hash locks. The same 13 real Tcl/Tk notice assertions run in one mandatory fresh process with stable descriptors and capture=sys, both from ordinary pytest and the native packager. Child errors, missing/duplicate cases or skipped cases fail the parent; there are no retries. [Dated observed fixture failure and correction](reports/NATIVE_NOTICE_ISOLATION_20261111.md).
