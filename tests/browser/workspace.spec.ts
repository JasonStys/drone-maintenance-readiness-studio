/** @file Jason Stys: real SQLite service lifecycle, retry, export, role, accessibility and logout-race journeys. Lines: docs/SOURCE_MAP.md. */
import { test, expect, type Page } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";
import fs from "node:fs";
import path from "node:path";
const directory = process.env.MAINT_TEST_DIRECTORY!;
/** Authenticate disposable local staff accounts without printing credentials. */
async function signIn(page: Page, role = "operator"): Promise<void> {
  const account = JSON.parse(
    fs.readFileSync(path.join(directory, "credentials.json"), "utf8"),
  )[role];
  await page.getByLabel("Username", { exact: true }).fill(account.username);
  await page.getByLabel("Password", { exact: true }).fill(account.password);
  await page.getByRole("button", { name: "Sign in", exact: true }).click();
  await expect(page.locator("#identity")).toContainText(account.username);
  await expect(page.locator("#message")).toContainText("Ready");
}
/** Wait for actual mutations, not arbitrary time delays. */
async function ready(page: Page): Promise<void> {
  await expect(page.locator("#message")).toContainText("Ready");
}
test("ambiguous usage retry records once, assessment export and stale detection", async ({
  page,
}) => {
  await page.goto("/");
  await signIn(page);
  await expect(page.locator("#aircraft-status")).toHaveText(
    "Within recorded limits",
  );
  await expect(
    page.getByRole("button", { name: "Record component swap" }),
  ).toBeDisabled();
  await page.route(
    "**/api/usage",
    async (route) => {
      const response = await route.fetch();
      expect(response.status()).toBe(200);
      await route.abort("failed");
    },
    { times: 1 },
  );
  await page.locator("#usage-minutes").fill("2");
  await page
    .locator("#usage-note")
    .fill("Original synthetic exercise usage, two minutes");
  await page.getByRole("button", { name: "Record attributable usage" }).click();
  await expect(
    page.getByRole("button", { name: "Retry pending usage safely" }),
  ).toBeVisible();
  await page
    .getByRole("button", { name: "Retry pending usage safely" })
    .click();
  await ready(page);
  await expect(page.locator("#usage-result")).toContainText(
    "without double counting",
  );
  const workspace = await (await page.request.get("/api/workspace")).json();
  expect(workspace.state.usage).toHaveLength(1);
  expect(
    workspace.state.components.find(
      (p: { id: string }) => p.id === "flood-battery",
    ).seconds,
  ).toBe(3720);
  await page.getByRole("button", { name: "Capture fleet assessment" }).click();
  await expect(page.locator("#report-state")).toContainText("Current");
  const download = page.waitForEvent("download");
  await page.locator("#report-export").click();
  const report = JSON.parse(
    await fs.promises.readFile((await (await download).path())!, "utf8"),
  );
  expect(report.flight_authorization).toBe(false);
  expect(report.state.usage).toHaveLength(1);
  expect(report.digest).toMatch(/^[a-f0-9]{64}$/);
  await page
    .locator("#defect-note")
    .fill("<img src=x onerror=alert(1)> synthetic watch finding");
  await page.locator("#severity").selectOption("watch");
  await page
    .getByRole("button", { name: "Record defect", exact: true })
    .click();
  await ready(page);
  await expect(page.locator("#component-findings")).toContainText("<img src=x");
  await expect(page.locator("#component-findings img")).toHaveCount(0);
  await page.getByRole("button", { name: "Refresh records" }).click();
  await expect(page.locator("#report-state")).toContainText("STALE");
});
test("serialized swap, fresh inspection and independent corrective-work verification", async ({
  page,
}) => {
  await page.goto("/");
  await signIn(page, "technician");
  await page.locator("#slot-select").selectOption("battery");
  await page.locator("#incoming").selectOption("spare-battery");
  await page
    .locator("#swap-note")
    .fill("Synthetic swap preserves original battery lifetime");
  await page.getByRole("button", { name: "Record component swap" }).click();
  await ready(page);
  await expect(page.locator("#parts")).toContainText("SYNTH-SPARE-BATTERY");
  await page.locator("#component-select").selectOption("flood-battery");
  await expect(page.locator("#component-summary")).toContainText("62.0 min");
  await page.locator("#work-defect").selectOption("1");
  await page
    .locator("#work-note")
    .fill("Synthetic corrective-work completion record");
  await page.getByRole("button", { name: "Record completed work" }).click();
  await ready(page);
  await page.locator("#component-select").selectOption("inspection-propulsion");
  await page
    .locator("#inspection-note")
    .fill("Synthetic post-work physical inspection evidence");
  await page
    .getByRole("button", { name: "Record inspection", exact: true })
    .click();
  await ready(page);
  await expect(page.locator("#component-findings")).toContainText("defect_1");
  await page.getByRole("button", { name: "Sign out" }).click();
  await expect(page.locator("#message")).toContainText("Signed out");
  await signIn(page, "reviewer");
  await page.locator("#verify-work").selectOption("1");
  await page
    .locator("#verify-note")
    .fill("Independent synthetic repair evidence verification");
  await page.getByRole("button", { name: "Verify completed work" }).click();
  await ready(page);
  const workspace = await (await page.request.get("/api/workspace")).json();
  expect(
    workspace.state.defects.find((d: { id: number }) => d.id === 1).closed,
  ).toBe(1);
  expect(
    workspace.readiness.aircraft.find(
      (a: { id: string }) => a.id === "inspection",
    ).status,
  ).toBe("review");
});
test("controlled admin policy publication and stale concurrency rejection", async ({
  page,
}) => {
  await page.goto("/");
  await signIn(page, "admin");
  await page.locator("#admin-panel summary").click();
  const policy = JSON.parse(await page.locator("#policy-json").inputValue());
  policy.label = "Synthetic reviewed standard, version two";
  await page.locator("#policy-json").fill(JSON.stringify(policy));
  await page
    .getByRole("button", { name: "Publish new policy version" })
    .click();
  await ready(page);
  await expect(page.locator("#policy-label")).toContainText("version 2");
  const component = JSON.parse(
    await page.locator("#component-json").inputValue(),
  );
  component.id = "additional-battery";
  component.serial = "SYNTH-ADDITIONAL-001";
  await page.locator("#component-json").fill(JSON.stringify(component));
  await page
    .getByRole("button", { name: "Create component", exact: true })
    .click();
  await ready(page);
  await page.locator("#component-select").selectOption("additional-battery");
  await expect(page.locator("#component-findings")).toContainText(
    "history_incomplete",
  );
  // A second real client write invalidates the first UI generation; never silently replay it.
  const identity = await (await page.request.get("/api/me")).json();
  const state = (await (await page.request.get("/api/workspace")).json()).state;
  const changed = await page.request.post("/api/policies", {
    headers: { Origin: "http://127.0.0.1:8902", "X-CSRF-Token": identity.csrf },
    data: { expected_generation: state.generation, policy },
  });
  expect(changed.status()).toBe(200);
  await page
    .getByRole("button", { name: "Publish new policy version" })
    .click();
  await expect(page.locator("#message")).toContainText("changed");
  await page.getByRole("button", { name: "Refresh records" }).click();
  await ready(page);
  await expect(page.locator("#policy-label")).toContainText("version 3");
});
test("WCAG, responsive layout and late-response logout privacy", async ({
  page,
}) => {
  await page.goto("/");
  await expect(page.locator("#message")).toContainText("Sign in");
  expect(
    (
      await new AxeBuilder({ page })
        .withTags(["wcag2a", "wcag2aa", "wcag21aa"])
        .analyze()
    ).violations,
  ).toEqual([]);
  await signIn(page);
  expect(
    (
      await new AxeBuilder({ page })
        .withTags(["wcag2a", "wcag2aa", "wcag21aa"])
        .analyze()
    ).violations,
  ).toEqual([]);
  expect(
    await page.evaluate(
      () => document.documentElement.scrollWidth <= innerWidth + 1,
    ),
  ).toBe(true);
  let release!: () => void;
  let received!: () => void;
  const hold = new Promise<void>((resolve) => {
    release = resolve;
  });
  const responseReady = new Promise<void>((resolve) => {
    received = resolve;
  });
  await page.route(
    "**/api/workspace",
    async (route) => {
      const response = await route.fetch();
      received();
      await hold;
      await route.fulfill({ response });
    },
    { times: 1 },
  );
  await page.getByRole("button", { name: "Refresh records" }).click();
  await responseReady;
  await page.getByRole("button", { name: "Sign out" }).click();
  await expect(page.locator("#login-panel")).toBeVisible();
  release();
  await expect(page.locator("#message")).toContainText("Signed out");
  await expect(page.locator("#workspace")).toBeHidden();
  await expect(page.locator("#parts")).toBeEmpty();
  await expect(page.locator("#ledger")).toHaveText("");
  await expect(page.locator("#report-export")).not.toHaveAttribute("href");
});
