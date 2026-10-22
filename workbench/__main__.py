"""Jason Stys: trusted local setup, staff provisioning and loopback launcher; lines: docs/SOURCE_MAP.md."""

import argparse
import getpass
from pathlib import Path

import uvicorn

from workbench.api import create_app
from workbench.auth import add_user
from workbench.store import Store


def main():
    """No public setup/reset endpoint; the OS-authorized owner provisions local staff."""
    parser = argparse.ArgumentParser(description="Drone Maintenance Readiness Studio by Jason Stys")
    parser.add_argument("--db", type=Path, default=Path(".runtime/workspace.sqlite3"))
    commands = parser.add_subparsers(dest="command", required=True)
    init = commands.add_parser("init")
    init.add_argument("--examples", action="store_true")
    user = commands.add_parser("user")
    user.add_argument("name")
    user.add_argument(
        "--role", choices=["operator", "technician", "reviewer", "admin"], required=True
    )
    serve = commands.add_parser("serve")
    serve.add_argument("--port", type=int, default=8901)
    args = parser.parse_args()
    store = Store(args.db)
    if args.command == "init":
        store.initialize(examples=args.examples)
        print(
            "Workspace initialized without overwriting existing records. Default limits are synthetic."
        )
    elif args.command == "user":
        password = getpass.getpass("New local password (14-128 characters): ")
        if password != getpass.getpass("Confirm password: "):
            raise SystemExit("Passwords differ")
        add_user(store, args.name, password, args.role)
        print("Local staff account created; password not written to source or command history.")
    else:
        if not 1024 <= args.port <= 65535:
            raise SystemExit("Use a port from 1024 through 65535")
        uvicorn.run(
            create_app(args.db, args.port),
            host="127.0.0.1",
            port=args.port,
            access_log=False,
            proxy_headers=False,
            limit_concurrency=24,
        )


if __name__ == "__main__":
    main()
