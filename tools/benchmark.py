"""Jason Stys: measured bounded snapshot/assessment benchmark, not a flight-system guarantee. Lines: docs/SOURCE_MAP.md."""

import json
import platform
import statistics
import tempfile
import time
from pathlib import Path

from workbench.engine import evaluate
from workbench.models import Assumptions
from workbench.store import Store


def measure(action, count):
    """Warm once, then report real monotonic median and maximum milliseconds without timing gates."""
    action()
    values = []
    for _ in range(count):
        started = time.perf_counter()
        action()
        values.append((time.perf_counter() - started) * 1000)
    return {
        "iterations": count,
        "median_ms": round(statistics.median(values), 3),
        "max_ms": round(max(values), 3),
    }


def main():
    """Use an isolated real SQLite ledger and original three-aircraft synthetic scenario."""
    with tempfile.TemporaryDirectory() as directory:
        store = Store(Path(directory) / "benchmark.sqlite3")
        store.initialize(examples=True)
        state, _ = store.snapshot()
        assumptions = Assumptions(daily_seconds=1200, daily_cycles=2)
        at = time.time()
        report = {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "scenario": "original synthetic 3 aircraft / 10 components / 1 ledger entry; no concurrent writers",
            "pure_engine": measure(lambda: evaluate(state, at, assumptions), 100),
            "verified_sqlite_dashboard": measure(store.dashboard, 30),
            "limitation": "Microbenchmark only; no p95 SLA, maximum-capacity or operational flight claim",
        }
        print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
