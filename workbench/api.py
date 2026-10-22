"""Jason Stys: authenticated loopback-only fleet API and self-hosted static review interface.

Exact endpoint/parameter/variable lines: docs/SOURCE_MAP.md. No device control, remote fetches or public signup.
"""

import asyncio
import sqlite3
import threading
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from workbench import auth
from workbench.models import (
    Assess,
    Defect,
    Inspection,
    Login,
    NewAircraft,
    NewComponent,
    Publish,
    Retire,
    Review,
    Swap,
    Usage,
    Verify,
    Work,
)
from workbench.store import Store

ROOT = Path(__file__).resolve().parents[1]
BODY_GATE = threading.BoundedSemaphore(4)
HEADERS = {
    "Content-Security-Policy": "default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'",
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "Referrer-Policy": "no-referrer",
    "Cache-Control": "no-store",
    "Permissions-Policy": "camera=(), microphone=(), geolocation=()",
}


def create_app(database: Path, port=8901):
    """One local trusted staff organization; do not expose this HTTP release as public SaaS."""
    if not 1024 <= port <= 65535:
        raise ValueError("Port outside supported range")
    authority, origin = f"127.0.0.1:{port}", f"http://127.0.0.1:{port}"
    app = FastAPI(
        title="Drone Maintenance Readiness Studio", docs_url=None, redoc_url=None, openapi_url=None
    )
    store = app.state.store = Store(database)

    @app.middleware("http")
    async def boundary(request: Request, call_next):
        """Exact Host/Origin, early auth/CSRF, bounded streamed JSON bodies and strict response headers."""
        acquired = False
        try:
            if request.headers.get("host") != authority:
                raise HTTPException(400, "Untrusted Host")
            if request.method not in {"GET", "HEAD", "POST"}:
                raise HTTPException(405, "Method not allowed")
            if request.url.path.startswith("/api/") and (
                request.headers.get("sec-fetch-site") == "cross-site"
                or request.headers.get("origin", origin) != origin
            ):
                raise HTTPException(403, "Exact same-origin required")
            if request.method == "POST":
                if request.headers.get("origin") != origin:
                    raise HTTPException(403, "Exact same-origin required")
                if request.url.path != "/api/login":
                    auth.authorize(request)
                if request.headers.get("content-type", "").split(";")[0] != "application/json":
                    raise HTTPException(415, "JSON required")
                if not BODY_GATE.acquire(blocking=False):
                    raise HTTPException(429, "Request-body capacity reached")
                acquired = True
                data = bytearray()
                async with asyncio.timeout(5):
                    async for chunk in request.stream():
                        if len(data) + len(chunk) > 65536:
                            raise HTTPException(413, "JSON body exceeds 64 KiB")
                        data.extend(chunk)
                request._body = bytes(data)
            response = await call_next(request)
        except HTTPException as error:
            response = JSONResponse({"detail": error.detail}, status_code=error.status_code)
        except TimeoutError:
            response = JSONResponse({"detail": "Body timeout"}, status_code=408)
        finally:
            if acquired:
                BODY_GATE.release()
        response.headers.update(HEADERS)
        return response

    @app.exception_handler(RequestValidationError)
    async def invalid(_request, error):
        """Field/type diagnostics only; never reflect passwords or private maintenance note values."""
        return JSONResponse(
            {
                "detail": "Invalid fields, bounds, duplicates or contradictory values",
                "fields": [{"location": list(e["loc"]), "type": e["type"]} for e in error.errors()],
            },
            status_code=422,
        )

    @app.exception_handler(sqlite3.IntegrityError)
    async def conflict(_request, _error):
        """Do not leak SQL, private row contents or paths when uniqueness/constraints reject a write."""
        return JSONResponse(
            {"detail": "Conflicting identity, serial or immutable record"}, status_code=409
        )

    @app.get("/healthz")
    def health():
        """Liveness only, never domain/account/database contents."""
        return {"status": "ok", "mode": "local-record-based-maintenance"}

    @app.post("/api/login")
    def login(body: Login, request: Request):
        """Opaque HttpOnly/SameSite Strict one-hour local session, only bearer digest persisted."""
        token, user = auth.sign_in(request, body.username, body.password)
        response = JSONResponse(user)
        response.set_cookie(
            "readiness_session", token, httponly=True, samesite="strict", max_age=3600
        )
        return response

    @app.get("/api/me")
    def me(request: Request):
        """Re-read live role and expiry instead of trusting browser role claims."""
        return auth.identity(request)

    @app.post("/api/logout")
    def logout(request: Request):
        """Immediate session revocation before clearing the browser cookie."""
        auth.sign_out(request)
        response = JSONResponse({"signed_out": True})
        response.delete_cookie("readiness_session")
        return response

    @app.get("/api/workspace")
    def workspace(request: Request):
        """All authorized staff intentionally share this organization's fleet, not other tenants."""
        auth.identity(request)
        return store.dashboard()

    @app.post("/api/aircraft")
    def aircraft(body: NewAircraft, request: Request):
        """Admin creates a unique immutable opening-history identity."""
        store.create(body, auth.authorize(request), "aircraft")
        return store.dashboard()

    @app.post("/api/components")
    def component(body: NewComponent, request: Request):
        """Admin creates a serialized component without a future reset/delete bypass."""
        store.create(body, auth.authorize(request), "components")
        return store.dashboard()

    @app.post("/api/policies")
    def publish(body: Publish, request: Request):
        """Admin publishes immutable configuration; removing required evidence yields visible findings."""
        store.publish(body, auth.authorize(request))
        return store.dashboard()

    @app.post("/api/swaps")
    def swap(body: Swap, request: Request):
        """Technician-only atomic physical identity relocation; cumulative usage follows the part."""
        store.swap(body, auth.authorize(request))
        return store.dashboard()

    @app.post("/api/usage")
    def usage(body: Usage, request: Request):
        """Record self-reported usage even when blocked, preserving rather than concealing bad operations."""
        result = store.usage(body, auth.authorize(request))
        return {**store.dashboard(), "write": result}

    @app.post("/api/inspections")
    def inspect(body: Inspection, request: Request):
        """Technician records current evidence; a pass alone never closes an unresolved defect."""
        store.inspect(body, auth.authorize(request))
        return store.dashboard()

    @app.post("/api/defects")
    def defect(body: Defect, request: Request):
        """Operator/technician can report blocking or watch items with a private note."""
        store.defect(body, auth.authorize(request))
        return store.dashboard()

    @app.post("/api/work")
    def work(body: Work, request: Request):
        """Technician completes a work record; defect remains open pending independent verification."""
        store.complete_work(body, auth.authorize(request))
        return store.dashboard()

    @app.post("/api/work/verify")
    def verify(body: Verify, request: Request):
        """Reviewer cannot override life limits, unknown evidence or missing post-work inspection."""
        store.verify_work(body, auth.authorize(request))
        return store.dashboard()

    @app.post("/api/retire")
    def retire(body: Retire, request: Request):
        """Irreversible retirement only after removal; history/counters remain visible."""
        store.retire(body, auth.authorize(request))
        return store.dashboard()

    @app.post("/api/assessments")
    def assess(body: Assess, request: Request):
        """Persist reproducible input/result evidence with explicit constant-workload assumptions."""
        identifier = store.assess(body, auth.authorize(request))
        return store.report(identifier)

    @app.get("/api/assessments/{identifier}")
    def report(identifier: int, request: Request):
        """Preserve historical findings and display staleness/expiry without making them current."""
        auth.identity(request)
        return store.report(identifier)

    @app.post("/api/assessments/{identifier}/review")
    def review(identifier: int, body: Review, request: Request):
        """Acknowledge evidence for triage; no automatic flight or service authorization."""
        store.review(identifier, body, auth.authorize(request))
        return store.report(identifier)

    @app.get("/api/assessments/{identifier}/export")
    def export(identifier: int, request: Request):
        """Private JSON includes bad/unknown/stale evidence honestly; no CSV formula or HTML execution."""
        auth.identity(request)
        return JSONResponse(
            store.report(identifier),
            headers={"Content-Disposition": 'attachment; filename="maintenance-assessment.json"'},
        )

    @app.get("/api/evidence/export")
    def evidence(request: Request):
        """Authenticated complete domain ledger/state, no password hashes or sessions."""
        auth.identity(request)
        return JSONResponse(
            store.evidence(),
            headers={"Content-Disposition": 'attachment; filename="maintenance-ledger.json"'},
        )

    @app.get("/")
    def index():
        """Serve only fixed built files, never a runtime-directory static mount."""
        if not (ROOT / "dist/index.html").is_file():
            raise HTTPException(503, "Build UI with npm run build")
        return FileResponse(ROOT / "dist/index.html")

    if (ROOT / "dist/assets").is_dir():
        app.mount("/assets", StaticFiles(directory=ROOT / "dist/assets"), name="assets")
    return app
