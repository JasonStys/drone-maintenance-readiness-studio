"""Jason Stys: synthetic demonstration/acceptance accounts, never production credentials; lines: docs/SOURCE_MAP.md."""

import argparse
import json
import secrets
from pathlib import Path

import uvicorn

from workbench.api import create_app
from workbench.auth import add_user
from workbench.store import Store


def prepare(directory: Path):
    """Generate random disposable staff accounts in ignored runtime only; no passwords printed."""
    directory.mkdir(parents=True, exist_ok=True)
    db = directory / "workspace.sqlite3"
    store = Store(db)
    store.initialize(examples=True)
    credentials = directory / "credentials.json"
    if not credentials.is_file():
        values = {
            role: {"username": f"demo-{role}", "password": secrets.token_urlsafe(24)}
            for role in ("operator", "technician", "reviewer", "admin")
        }
        for role, record in values.items():
            add_user(store, record["username"], record["password"], role)
        credentials.write_text(json.dumps(values), encoding="utf-8")
    return db


def main():
    """Loopback-only disposable service; each browser suite gets a separate database/login budget."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=Path, default=Path(".runtime/browser"))
    parser.add_argument("--port", type=int, default=8902)
    args = parser.parse_args()
    uvicorn.run(
        create_app(prepare(args.directory), args.port),
        host="127.0.0.1",
        port=args.port,
        access_log=False,
        proxy_headers=False,
        limit_concurrency=24,
    )


if __name__ == "__main__":
    main()
