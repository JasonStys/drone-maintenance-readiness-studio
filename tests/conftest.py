"""Jason Stys: isolated real SQLite and random staff fixtures, not mocks of domain logic. Lines: docs/SOURCE_MAP.md."""

import secrets

import pytest
from fastapi.testclient import TestClient

from workbench.api import create_app
from workbench.auth import HASHER
from workbench.models import Assumptions

ORIGIN = "http://127.0.0.1:8901"


@pytest.fixture(scope="session")
def accounts():
    """Hash disposable random credentials once; never log or commit their cleartext values."""
    return {
        role: (password := secrets.token_urlsafe(24), HASHER.hash(password))
        for role in ("operator", "technician", "reviewer", "admin")
    }


@pytest.fixture
def app(tmp_path, accounts):
    """Every test owns its private schema, ledger and original synthetic records."""
    instance = create_app(tmp_path / "db.sqlite3")
    instance.state.store.initialize(examples=True)
    with instance.state.store.connect(True) as db:
        for role, (_, hashed) in accounts.items():
            db.execute("INSERT INTO users VALUES(?,?,?)", (role, hashed, role))
    return instance


@pytest.fixture
def store(app):
    """Real store with no data access beyond this test's disposable directory."""
    return app.state.store


@pytest.fixture
def state(store):
    """Original coherent snapshot; pure engine tests may modify their private copy as adversarial input."""
    return store.snapshot()[0]


@pytest.fixture
def assumptions():
    """Explicit two-cycle/twenty-minute constant daily workload scenario."""
    return Assumptions(daily_seconds=1200, daily_cycles=2)


@pytest.fixture
def client(app):
    """Exact Host/Origin and actual Argon2/session/API/SQLite behavior."""
    with TestClient(app, base_url=ORIGIN, headers={"Origin": ORIGIN}) as connection:
        yield connection


@pytest.fixture
def login(client, accounts):
    """Switch current test session by actually authenticating through the login endpoint."""

    def enter(role="operator"):
        response = client.post("/api/login", json={"username": role, "password": accounts[role][0]})
        assert response.status_code == 200, response.text
        client.headers["X-CSRF-Token"] = response.json()["csrf"]
        return response.json()

    return enter


@pytest.fixture
def post(client):
    """Bind each deliberate write to the current displayed generation, not silently retry conflicts."""

    def submit(path, **fields):
        generation = client.get("/api/workspace").json()["state"]["generation"]
        return client.post(path, json={"expected_generation": generation, **fields})

    return submit
