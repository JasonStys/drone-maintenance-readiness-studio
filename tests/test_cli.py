"""Jason Stys: local setup, private provisioning and loopback-only launcher tests. Lines: docs/SOURCE_MAP.md."""

import sys

import pytest

from tools import browser_server
from workbench import __main__ as cli


def test_init_provision_and_mismatch(tmp_path, monkeypatch, capsys):
    """OS-authorized provisioning does not expose passwords or overwrite existing records."""
    db = tmp_path / "db.sqlite3"
    monkeypatch.setattr(sys, "argv", ["studio", "--db", str(db), "init"])
    cli.main()
    cli.main()
    monkeypatch.setattr(
        sys, "argv", ["studio", "--db", str(db), "user", "operator", "--role", "operator"]
    )
    answers = iter(["private-long-test-password", "private-long-test-password"])
    monkeypatch.setattr(cli.getpass, "getpass", lambda _p: next(answers))
    cli.main()
    assert "private-long-test-password" not in capsys.readouterr().out
    answers = iter(["private-long-test-password", "different"])
    with pytest.raises(SystemExit, match="Passwords differ"):
        cli.main()


def test_serve_invalid_port_and_browser_fixture(tmp_path, monkeypatch):
    """Real startup factories bind loopback and reject proxy identity spoofing."""
    seen = []
    monkeypatch.setattr(cli.uvicorn, "run", lambda *args, **kwargs: seen.append(kwargs))
    monkeypatch.setattr(sys, "argv", ["studio", "--db", str(tmp_path / "db"), "serve"])
    cli.main()
    assert seen[-1]["host"] == "127.0.0.1" and seen[-1]["proxy_headers"] is False
    monkeypatch.setattr(sys, "argv", ["studio", "serve", "--port", "80"])
    with pytest.raises(SystemExit, match="1024"):
        cli.main()
    directory = tmp_path / "browser"
    first = browser_server.prepare(directory)
    assert browser_server.prepare(directory) == first
    monkeypatch.setattr(sys, "argv", ["browser", "--directory", str(directory)])
    browser_server.main()
    assert seen[-1]["host"] == "127.0.0.1" and seen[-1]["proxy_headers"] is False
