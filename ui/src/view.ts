/** @file Jason Stys: pure readiness labels, unit rendering and discrete-record usage chart. Lines: docs/SOURCE_MAP.md. */
export type Status =
  "blocked" | "unknown" | "review" | "within_recorded_limits";
/** Never use a green 'safe to fly' label for a record-based advisory result. */
export function statusLabel(status: Status): string {
  return {
    blocked: "Blocked",
    unknown: "Unknown evidence",
    review: "Human review",
    within_recorded_limits: "Within recorded limits",
  }[status];
}
/** Explicit missing-value label; zero remaining life is not mistaken for missing data. */
export function minutes(seconds: number | null): string {
  return seconds === null ? "Unknown" : `${(seconds / 60).toFixed(1)} min`;
}
/** Verify DOM-derived IDs before using them as fixed API path segments. */
export function reportId(value: string): number | null {
  const number = Number(value);
  return Number.isSafeInteger(number) && number > 0 ? number : null;
}
/** Discrete recorded-use curve; x is event ordinal, not elapsed time or a continuous telemetry estimate. */
export function sparkPoints(values: number[]): string {
  if (
    values.length === 0 ||
    values.some((value) => !Number.isFinite(value) || value < 0)
  )
    return "";
  const maximum = Math.max(1, ...values);
  return values
    .map(
      (value, index) =>
        `${20 + (index * 560) / Math.max(1, values.length - 1)},${120 - (value / maximum) * 100}`,
    )
    .join(" ");
}
