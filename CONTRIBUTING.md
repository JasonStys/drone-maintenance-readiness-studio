<!-- Jason Stys: contributor workflow, invariant requirements and reproducible validation expectations. -->
# Contributing

Use a focused branch and synthetic data only. Preserve serialized lifetime, exact-attribution/idempotency, atomic rollback, unknown evidence, independent work review, immutable reports, expiry and server-side roles. New capabilities need independent expected-value and negative tests, not changes that turn failing fixtures green by lowering maintenance limits or removing guards.

Follow the README validation commands and update the appropriate documentation. Every authored source file needs its responsibility/author header and `docs/SOURCE_MAP.md` reference; functions/classes need local documentation. After formatting, run `python tools/docs_index.py`, commit both generated maps and verify with `--check`. Keep shallow meaningful modules; explain complexity/bounds and tradeoffs. Never commit runtime data/accounts, dependencies, logs or generated binaries.

Dependency upgrades must regenerate hash locks and pass live complete-inventory audits. Actions stay least-privilege, SHA-pinned and without artifact/cache uploads. Do not change storage/retention policies or delete old runs without fresh owner approval. Final main commits must pass the full cross-platform Validation workflow and both CodeQL languages, including inspection of open code-scanning alerts.
