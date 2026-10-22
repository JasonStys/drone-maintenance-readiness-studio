<!-- Jason Stys: local launch, backup/restore, account handling, failure recovery and release checklist. -->
# Operations and release runbook

## Local operation

Use the README locked setup. Runtime defaults to `.runtime/workspace.sqlite3`; do not move it into source. Launch `python -m workbench serve --port 8901` using the environment interpreter. Bind remains exactly 127.0.0.1; browser must use that address and configured port, not localhost or a LAN address. No reverse proxy is trusted. Health is liveness only, not database-integrity approval. The workspace endpoint verifies integrity after staff authentication.

OS-authorized owner provisions each staff member with `python -m workbench user NAME --role ROLE`. Password entry is interactive, 14–128 characters. There is no public account creation. Use genuinely separate technician/reviewer identities. Keep OS accounts, browser, dependencies and disk encryption maintained. No signed native installer or mobile service is supplied; responsive mobile layout is tested in emulation, not an installed iOS/Android certification.

Disposable demonstration: `python -m tools.browser_server --directory .runtime/demo --port 8901`. It creates original synthetic records and random accounts only in that ignored directory. Read its `credentials.json` privately on this machine; never commit or post it. Repeating preparation preserves records/credentials. The acceptance harness uses this same real service with separate directories per engine and port 8902.

## Backup and recovery

Stop the process before copying the complete private runtime directory to an access-restricted, encrypted backup. Record a SHA-256 checksum of each backup file. Copying the entire stopped SQLite file preserves users, sessions, domain history and reports; a domain JSON export alone is **not** an account/database restore. Exports contain private maintenance evidence and must not be published. Preserve a known-good source revision and locked dependencies alongside a private backup manifest, not passwords in Git.

Restore only a known-good verified copy into a new private directory while stopped. Do not overwrite the only original or a potentially useful corrupt file. Start with `--db` pointing at the restored copy, sign in, compare expected identities/counters, load reports and verify the workspace/ledger. Revoke sessions after an incident through approved offline DB administration; restored sessions may still be valid until original expiry. Test the restore process with synthetic records before relying on it. Whole-database replacement cannot be detected by an unanchored local hash chain; keep the backup manifest/tip separately protected.

For integrity failure: stop further writes, preserve the database/source/logs privately, compare backups and investigate. Never drop triggers or recompute hashes to make a broken record pass. Test corruption cases do so only in disposable fixtures. For capacity/disk exhaustion: stop accepting work and design a reviewed archival/migration strategy; there is no automatic deletion, lifetime reset or data migration implementation. A new empty workspace is not a substitute for old life history.

## Ship checklist

1. Review domain changes for preserved counters, unknown evidence, defect independence, expiry and role checks.
2. Run exact locked lint/format, tests, coverage, build, generated navigation, payload budgets, benchmark and both live dependency audits.
3. Run real-service Chromium/Firefox/WebKit/mobile acceptance including accessibility and private logout races.
4. Verify staged files contain no runtime/vendor/media/private credentials. Review the diff and map generated declarations after formatting.
5. Check Actions artifact storage (separate from caches/billing); never delete runs/artifacts/caches without fresh owner approval. Workflows upload no run artifacts or caches; CI logs/security results still exist on GitHub.
6. Verify all Validation matrix jobs and both CodeQL languages on the exact final main commit, then inspect open code-scanning alerts. Do not treat a green scanner execution alone as zero alerts.
7. Update measured validation notes; final documentation commits must pass their own checks. Keep main equal to origin/main.

Rollback source to a reviewed known-good revision only after protecting private runtime data. This initial release adds no migration framework and cannot assume future schemas are backward compatible. Stop deployment if an integrity failure, counter regression, authorization bypass, unexplained audit difference or failing acceptance test occurs. The safe response is preserve evidence and investigate, not relaxing tests/thresholds or changing fictional limits to obtain a better badge.
