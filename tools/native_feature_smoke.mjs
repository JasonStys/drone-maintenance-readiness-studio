/** Jason Stys: actual packaged maintenance UI, draft standards, exact usage and independent repair review. Lines: docs/SOURCE_MAP.md. */
import assert from "node:assert/strict";
import crypto from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { chromium, expect } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

const [base, output] = process.argv.slice(2);
assert(base && output && process.env.NATIVE_TEST_PASSWORD);
const origin = new URL(base).origin;
const browser = await chromium.launch();
const context = await browser.newContext({
  viewport: { width: 1440, height: 1000 },
  acceptDownloads: true,
  reducedMotion: "reduce",
});
const page = await context.newPage();
const errors = [];
const external = [];
page.on("pageerror", (error) => errors.push(error.message));
page.on("request", (request) => {
  if (
    /^https?:/.test(request.url()) &&
    new URL(request.url()).origin !== origin
  )
    external.push(request.url());
});

/** Authenticate each actual isolated native-profile role through the ordinary UI. */
async function login(role) {
  await page.goto(base);
  await page.getByLabel("Username", { exact: true }).fill(role);
  await page
    .getByLabel("Password", { exact: true })
    .fill(process.env.NATIVE_TEST_PASSWORD);
  await page.getByRole("button", { name: "Sign in", exact: true }).click();
  await expect(page.locator("#identity")).toContainText(role);
  await ready();
}

/** Wait for actual service acknowledgement, never an arbitrary delay or optimistic DOM change. */
async function ready() {
  await expect(page.locator("#message")).toContainText("Ready");
}

/** Complete real server revocation before navigating roles; a button click alone is not completion. */
async function signOut() {
  const response = page.waitForResponse(
    (response) =>
      new URL(response.url()).pathname === "/api/logout" &&
      response.request().method() === "POST",
  );
  await page.getByRole("button", { name: "Sign out", exact: true }).click();
  assert.equal((await response).status(), 200);
  await expect(
    page.getByRole("button", { name: "Sign in", exact: true }),
  ).toBeEnabled();
}

/** Retain and parse the actual browser download for independent content/digest checks. */
async function download(locator) {
  const pending = page.waitForEvent("download");
  await locator.click();
  const file = await (await pending).path();
  assert(file);
  return JSON.parse(await fs.readFile(file, "utf8"));
}

/** Independent canonical JSON for this ASCII, finite policy fixture; no application hashing helper. */
function canonical(value) {
  if (Array.isArray(value)) return "[" + value.map(canonical).join(",") + "]";
  if (value !== null && typeof value === "object")
    return (
      "{" +
      Object.keys(value)
        .sort()
        .map((key) => JSON.stringify(key) + ":" + canonical(value[key]))
        .join(",") +
      "}"
    );
  return JSON.stringify(value);
}

/** Preserve the two declared Policy float fields' Python normalized JSON kind; JS has no int/float distinction. */
function canonicalPolicy(value) {
  const floatFields = new Set([
    "battery_min_capacity_pct",
    "battery_max_resistance_mohm",
  ]);
  return (
    "{" +
    Object.keys(value)
      .sort()
      .map((key) => {
        const item = value[key];
        const encoded =
          floatFields.has(key) && Number.isInteger(item)
            ? item.toFixed(1)
            : canonical(item);
        return JSON.stringify(key) + ":" + encoded;
      })
      .join(",") +
    "}"
  );
}

try {
  await login("admin");
  await expect(page.locator("#application-version")).toHaveText(
    "Application v0.2.1",
  );
  const original = await (
    await page.request.get(new URL("api/workspace", base).href)
  ).json();
  assert.equal(original.state.aircraft.length, 3);
  assert.equal(original.state.policy_version, 1);
  await page.locator("#admin-panel summary").click();
  const draft = JSON.parse(await page.locator("#policy-json").inputValue());
  draft.label = "Fictional imported coastal training limits";
  const battery = draft.limits.find((limit) => limit.kind === "battery");
  assert(battery);
  battery.seconds = 3600;
  await page.getByLabel("Open policy JSON", { exact: true }).setInputFiles({
    name: "coastal-policy.json",
    mimeType: "application/json",
    buffer: Buffer.from(JSON.stringify(draft)),
  });
  await expect(page.locator("#message")).toContainText("draft only");
  assert.deepEqual(
    JSON.parse(await page.locator("#policy-json").inputValue()),
    draft,
  );
  await page
    .getByRole("button", { name: "Preview policy impact", exact: true })
    .click();
  await expect(
    page.getByLabel("Unpublished maintenance policy impact"),
  ).toContainText("UNPUBLISHED POLICY IMPACT");
  const impact = await download(
    page.getByRole("button", { name: "Download unpublished impact" }),
  );
  assert.equal(impact.published, false);
  assert.equal(impact.flight_authorization, false);
  assert.equal(impact.source_generation, original.state.generation);
  assert.equal(
    impact.draft_policy_digest,
    crypto.createHash("sha256").update(canonicalPolicy(draft)).digest("hex"),
  );
  assert.equal(
    canonicalPolicy({
      battery_min_capacity_pct: 80,
      battery_max_resistance_mohm: 180,
    }),
    '{"battery_max_resistance_mohm":180.0,"battery_min_capacity_pct":80.0}',
  );
  assert.notEqual(
    impact.draft_policy_digest,
    crypto.createHash("sha256").update(canonical(draft)).digest("hex"),
  );
  const change = impact.changes.components.find(
    (row) => row.id === "flood-battery",
  );
  assert(change);
  assert.equal(change.before.remaining_seconds, 356400);
  assert.equal(change.after.remaining_seconds, 0);
  assert.equal(change.after.status, "blocked");
  assert(
    change.after.findings.some((finding) => finding.code === "time_limit"),
  );
  assert.deepEqual(
    await download(page.getByRole("button", { name: "Download policy draft" })),
    draft,
  );
  const after = await (
    await page.request.get(new URL("api/workspace", base).href)
  ).json();
  for (const key of ["state", "ledger_tip", "reports", "ledger"])
    assert.deepEqual(after[key], original[key]);
  assert.deepEqual(
    (
      await new AxeBuilder({ page })
        .withTags(["wcag2a", "wcag2aa", "wcag21aa", "wcag22aa"])
        .analyze()
    ).violations,
    [],
  );
  await page
    .locator("#admin-panel")
    .screenshot({ path: path.join(output, "01-imported-policy-impact.png") });
  const beforeInvalid = await page.locator("#policy-json").inputValue();
  await page.getByLabel("Open policy JSON", { exact: true }).setInputFiles({
    name: "invalid.json",
    mimeType: "application/json",
    buffer: Buffer.from([0xc3, 0x28]),
  });
  await expect(
    page.getByRole("button", { name: "Download unpublished impact" }),
  ).toBeDisabled();
  assert.equal(await page.locator("#policy-json").inputValue(), beforeInvalid);
  await signOut();
  await login("operator");
  await expect(page.locator("#admin-panel")).toBeHidden();
  await expect(
    page.getByRole("button", { name: "Record component swap" }),
  ).toBeDisabled();
  await page.locator("#usage-minutes").fill("2");
  await page
    .locator("#usage-note")
    .fill("Synthetic two-minute recorded use; no aircraft operation occurred.");
  await page.getByRole("button", { name: "Record attributable usage" }).click();
  await ready();
  const used = await (
    await page.request.get(new URL("api/workspace", base).href)
  ).json();
  assert.equal(used.state.usage.length, 1);
  assert.equal(
    used.state.components.find((part) => part.id === "flood-battery").seconds,
    3720,
  );
  await page.getByRole("button", { name: "Capture fleet assessment" }).click();
  await expect(page.locator("#report-state")).toContainText("Current");
  const report = await download(page.locator("#report-export"));
  assert.equal(report.flight_authorization, false);
  assert.equal(report.state.usage.length, 1);
  assert.equal(report.state.policy_version, 1);
  await signOut();
  await login("technician");
  await page.locator("#component-select").selectOption("inspection-propulsion");
  await page.locator("#work-defect").selectOption("1");
  await page
    .locator("#work-note")
    .fill(
      "Synthetic corrective work; independently verify after fresh inspection.",
    );
  await page.getByRole("button", { name: "Record completed work" }).click();
  await ready();
  await page.locator("#inspection-result").selectOption("pass");
  await page
    .locator("#inspection-note")
    .fill(
      "Synthetic post-work inspection evidence, not a physical measurement.",
    );
  await page
    .getByRole("button", { name: "Record inspection", exact: true })
    .click();
  await ready();
  let repaired = await (
    await page.request.get(new URL("api/workspace", base).href)
  ).json();
  assert.equal(
    repaired.state.defects.find((defect) => defect.id === 1).closed,
    0,
  );
  await signOut();
  await login("reviewer");
  await page.locator("#verify-work").selectOption("1");
  await page
    .locator("#verify-note")
    .fill(
      "Independent synthetic verification of work and later passing inspection.",
    );
  await page.getByRole("button", { name: "Verify completed work" }).click();
  await ready();
  repaired = await (
    await page.request.get(new URL("api/workspace", base).href)
  ).json();
  assert.equal(
    repaired.state.defects.find((defect) => defect.id === 1).closed,
    1,
  );
  assert.equal(
    repaired.readiness.aircraft.find((asset) => asset.id === "inspection")
      .status,
    "review",
  );
  assert.equal(
    repaired.state.components.find((part) => part.id === "flood-battery")
      .seconds,
    3720,
  );
  await page.locator("#component-select").selectOption("inspection-propulsion");
  await expect(page.locator("#defects")).toContainText(
    "No open component findings",
  );
  await page
    .getByRole("heading", {
      name: "Corrective work & independent verification",
    })
    .locator("..")
    .screenshot({
      path: path.join(output, "02-independent-repair-evidence.png"),
    });
  await page.setViewportSize({ width: 390, height: 844 });
  assert(
    await page.evaluate(
      () => document.documentElement.scrollWidth <= innerWidth,
    ),
  );
  assert.deepEqual(
    (
      await new AxeBuilder({ page })
        .withTags(["wcag2a", "wcag2aa", "wcag21aa", "wcag22aa"])
        .analyze()
    ).violations,
    [],
  );
  assert.deepEqual(
    await page.evaluate(() => [localStorage.length, sessionStorage.length]),
    [0, 0],
  );
  const cookies = await context.cookies();
  assert.equal(cookies.length, 1);
  assert.equal(cookies[0].name, process.env.NATIVE_TEST_COOKIE_NAME);
  assert.equal(cookies[0].httpOnly, true);
  assert.equal(cookies[0].sameSite, "Strict");
  assert.deepEqual(external, []);
  assert.deepEqual(errors, []);
  await fs.writeFile(
    path.join(output, "feature.json"),
    JSON.stringify(
      {
        passed: true,
        actual_roles: ["admin", "operator", "technician", "reviewer"],
        draft_policy_only: true,
        independent_policy_digest: true,
        hypothetical_battery_seconds_remaining: 0,
        unchanged_ledger_during_preview: true,
        usage_delta_seconds: 120,
        cumulative_battery_seconds: 3720,
        independent_repair_verification_required: true,
        no_flight_authorization: true,
        mobile_width: 390,
        outside_requests: 0,
      },
      null,
      2,
    ) + "\n",
  );
} finally {
  await context.close();
  await browser.close();
}
