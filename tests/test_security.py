"""Jason Stys: real authentication, browser-boundary and disclosure regressions. Lines: docs/SOURCE_MAP.md."""

import hashlib
import sqlite3
import time
from types import SimpleNamespace

import pytest

from workbench import api, auth
from workbench.api import create_app


def test_anonymous_boundary_and_private_static_files(client):
    """No public account, maintenance export or runtime-file access."""
    for path in [
        "/api/me",
        "/api/workspace",
        "/api/evidence/export",
        "/api/assessments/1",
        "/api/assessments/1/export",
    ]:
        assert client.get(path).status_code == 401
    for path in [
        "/.runtime/credentials.json",
        "/workbench/schema.sql",
        "/api/signup",
        "/docs",
        "/openapi.json",
    ]:
        assert client.get(path).status_code == 404
    assert client.get("/healthz").json()["status"] == "ok"
    response = client.get("/")
    assert response.status_code == 200
    for name, value in api.HEADERS.items():
        assert response.headers[name] == value
    assert client.get("/api/me", headers={"Host": "evil.example"}).status_code == 400
    assert client.get("/api/me", headers={"Origin": "https://evil.example"}).status_code == 403
    assert client.get("/api/me", headers={"Sec-Fetch-Site": "cross-site"}).status_code == 403
    assert client.put("/api/login", json={}).status_code == 405
    assert client.post("/api/login", json={}, headers={"Origin": "null"}).status_code == 403
    assert (
        client.post(
            "/api/login", content="not json", headers={"Content-Type": "text/plain"}
        ).status_code
        == 415
    )
    assert (
        client.post(
            "/api/login", content=b"x" * 65537, headers={"Content-Type": "application/json"}
        ).status_code
        == 413
    )
    assert client.post("/api/login", json={"password": "PRIVATE-UNREFLECTED"}).status_code == 422
    assert (
        "PRIVATE-UNREFLECTED"
        not in client.post("/api/login", json={"password": "PRIVATE-UNREFLECTED"}).text
    )


def test_csrf_session_hash_expiry_revocation_and_live_roles(client, login, store):
    """Role/cookie claims never grant authority; only opaque bearer digests are stored."""
    login()
    token = client.cookies.get("readiness_session")
    with store.connect() as db:
        row = db.execute("SELECT * FROM sessions").fetchone()
        assert row["digest"] == hashlib.sha256(token.encode()).hexdigest()
        assert token not in str(dict(row))
    assert client.post("/api/logout", json={}, headers={"X-CSRF-Token": "wrong"}).status_code == 403
    assert client.get("/api/assessments/999").status_code == 404
    with store.connect(True) as db:
        db.execute("UPDATE users SET role='reviewer' WHERE name='operator'")
    assert client.get("/api/me").json()["role"] == "reviewer"
    assert client.post("/api/logout", json={}).status_code == 200
    client.cookies.set("readiness_session", token)
    assert client.get("/api/me").status_code == 401
    client.cookies.clear()
    login()
    with store.connect(True) as db:
        db.execute("UPDATE sessions SET expires=?", (time.time() - 1,))
    assert client.get("/api/me").status_code == 401
    client.cookies.clear()
    client.cookies.set("readiness_session", "x" * 101)
    assert client.get("/api/me").status_code == 401


def test_roles_and_body_capacity(client, login, post, monkeypatch):
    """UI visibility is not authorization; reject before mutations on actual service routes."""
    login()
    for path, body in [
        ("/api/work", {"defect": 1, "note": "synthetic test evidence"}),
        ("/api/work/verify", {"work": 1, "note": "synthetic test evidence"}),
        ("/api/retire", {"component": "spare-battery", "note": "synthetic test evidence"}),
        (
            "/api/swaps",
            {
                "aircraft": "flood",
                "slot": "battery",
                "component": None,
                "note": "synthetic test evidence",
            },
        ),
        (
            "/api/inspections",
            {"component": "spare-battery", "passed": True, "note": "synthetic test evidence"},
        ),
    ]:
        assert post(path, **body).status_code == 403
    monkeypatch.setattr(api, "BODY_GATE", SimpleNamespace(acquire=lambda **_kw: False))
    assert client.post("/api/logout", json={}).status_code == 429


def test_login_limits_unknown_password_and_bounded_sessions(client, accounts, store, monkeypatch):
    """Real Argon2 rejection, capacity and busy handling; no external identity service."""
    body = {"username": "operator", "password": "wrong-but-valid-length"}
    assert client.post("/api/login", json=body).status_code == 401
    assert client.post("/api/login", json={**body, "username": "unknown"}).status_code == 401
    monkeypatch.setattr(auth, "VERIFY_GATE", SimpleNamespace(acquire=lambda **_kw: False))
    assert client.post("/api/login", json=body).status_code == 429
    monkeypatch.undo()
    monkeypatch.setattr(auth, "HASHER", SimpleNamespace(verify=lambda *_args: True))
    assert client.post("/api/login", json={**body, "username": "unknown"}).status_code == 401
    for _ in range(11):
        response = client.post(
            "/api/login", json={"username": "operator", "password": accounts["operator"][0]}
        )
        assert response.status_code == 200
        assert "HttpOnly" in response.headers["set-cookie"]
        assert "SameSite=strict" in response.headers["set-cookie"]
    with store.connect() as db:
        assert db.execute("SELECT count(*) FROM sessions").fetchone()[0] == 10
    with store.connect(True) as db:
        db.execute("DELETE FROM attempts")
        db.executemany(
            "INSERT INTO attempts VALUES(?,1,?)", [(str(i), time.time()) for i in range(1000)]
        )
    assert client.post("/api/login", json=body).status_code == 429


def test_provisioning_password_bounds_and_uniqueness(store):
    """Only CLI-authorized provisioning; names cannot reset or overwrite existing staff."""
    for name, password, role in [
        ("X", "x" * 20, "operator"),
        ("staff", "short", "operator"),
        ("staff", "x" * 129, "operator"),
        ("staff", "x" * 20, "root"),
    ]:
        with pytest.raises(ValueError):
            auth.add_user(store, name, password, role)
    auth.add_user(store, "new-staff", "private-long-test-password", "admin")
    with pytest.raises(sqlite3.IntegrityError):
        auth.add_user(store, "new-staff", "another-private-test-password", "reviewer")


def test_invalid_port_and_unbuilt_ui(tmp_path, client, monkeypatch):
    """An unbuilt UI gives setup guidance, not a directory listing."""
    with pytest.raises(ValueError):
        create_app(tmp_path / "db", 80)
    monkeypatch.setattr(api, "ROOT", tmp_path)
    assert client.get("/").status_code == 503
