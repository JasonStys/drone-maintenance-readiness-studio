/** @file Jason Stys: independent status/unit/path and discrete-chart presentation oracles. Lines: docs/SOURCE_MAP.md. */
import { expect, it } from "vitest";
import { minutes, reportId, sparkPoints, statusLabel } from "./view";
it("uses advisory labels and never says safe to fly", () => {
  expect(statusLabel("blocked")).toBe("Blocked");
  expect(statusLabel("unknown")).toBe("Unknown evidence");
  expect(statusLabel("review")).toBe("Human review");
  expect(statusLabel("within_recorded_limits")).toBe("Within recorded limits");
});
it("preserves zero remaining life and explicit units", () => {
  expect(minutes(null)).toBe("Unknown");
  expect(minutes(0)).toBe("0.0 min");
  expect(minutes(90)).toBe("1.5 min");
});
it("rejects noninteger/unsafe/hostile DOM report path values", () => {
  expect(reportId("3")).toBe(3);
  for (const value of [
    "",
    "0",
    "-1",
    "0.1",
    "NaN",
    "Infinity",
    "<img src=x>",
    "9007199254740992",
  ])
    expect(reportId(value)).toBeNull();
});
it("scales discrete recorded usage without fictitious time samples", () => {
  expect(sparkPoints([])).toBe("");
  expect(sparkPoints([NaN])).toBe("");
  expect(sparkPoints([-1])).toBe("");
  expect(sparkPoints([0])).toBe("20,120");
  expect(sparkPoints([0, 60, 120])).toBe("20,120 300,70 580,20");
});
