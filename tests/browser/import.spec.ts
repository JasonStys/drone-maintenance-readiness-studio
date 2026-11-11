/** Jason Stys: real role-bound policy files, readonly preview/export and deliberately delayed native-file reads. Lines: docs/SOURCE_MAP.md. */
import { test, expect, type Page } from "@playwright/test";
import fs from "node:fs/promises";
import path from "node:path";

declare global {
  interface Window {
    __heldImport?: boolean;
    __releaseImport?: () => void;
  }
}

/** Use only credentials generated in this run's disposable browser database. */
async function login(page: Page, role = "admin") {
  const directory = process.env.MAINT_TEST_DIRECTORY;
  if (!directory)
    throw new Error("Missing disposable browser fixture directory");
  const account = JSON.parse(
    await fs.readFile(path.join(directory, "credentials.json"), "utf8"),
  )[role];
  await page.goto("/");
  await page.getByLabel("Username", { exact: true }).fill(account.username);
  await page.getByLabel("Password", { exact: true }).fill(account.password);
  await page.getByRole("button", { name: "Sign in", exact: true }).click();
  await expect(page.locator("#identity")).toContainText(account.username);
  await expect(page.locator("#message")).toContainText("Ready");
}

test("policy files edit only a draft, preview without writes and download that exact draft", async ({
  page,
}) => {
  await login(page);
  const original = await (await page.request.get("/api/workspace")).json();
  await page.locator("#admin-panel summary").click();
  const draft = JSON.parse(await page.locator("#policy-json").inputValue());
  draft.label = "Fictional imported standards draft";
  await page.getByLabel("Open policy JSON", { exact: true }).setInputFiles({
    name: "policy.json",
    mimeType: "application/json",
    buffer: Buffer.from(JSON.stringify(draft)),
  });
  await expect(page.locator("#message")).toContainText("draft only");
  expect(JSON.parse(await page.locator("#policy-json").inputValue())).toEqual(
    draft,
  );
  await page
    .getByRole("button", { name: "Preview policy impact", exact: true })
    .click();
  await expect(
    page.getByLabel("Unpublished maintenance policy impact"),
  ).toContainText("UNPUBLISHED POLICY IMPACT");
  const after = await (await page.request.get("/api/workspace")).json();
  for (const key of ["state", "ledger_tip", "reports", "ledger"])
    expect(after[key]).toEqual(original[key]);
  const pending = page.waitForEvent("download");
  await page.getByRole("button", { name: "Download policy draft" }).click();
  const file = await (await pending).path();
  if (!file) throw new Error("Actual policy download missing");
  expect(JSON.parse(await fs.readFile(file, "utf8"))).toEqual(draft);
  const retained = await page.locator("#policy-json").inputValue();
  for (const buffer of [
    Buffer.from([0xc3, 0x28]),
    Buffer.alloc(60_001),
    Buffer.from('{"value":1e999}'),
    Buffer.from("[]"),
  ]) {
    await page.getByLabel("Open policy JSON", { exact: true }).setInputFiles({
      name: "invalid.json",
      mimeType: "application/json",
      buffer,
    });
    await expect(page.locator("#message")).not.toContainText("Reading local");
    expect(await page.locator("#policy-json").inputValue()).toBe(retained);
    await expect(
      page.getByRole("button", { name: "Download unpublished impact" }),
    ).toBeDisabled();
  }
});

test("late files cannot overwrite typing, newer choices or a signed-out account", async ({
  page,
}) => {
  await login(page);
  await page.locator("#admin-panel summary").click();
  await page.evaluate(() => {
    const original = File.prototype.arrayBuffer;
    File.prototype.arrayBuffer = function () {
      if (!this.name.startsWith("held-")) return original.call(this);
      window.__heldImport = true;
      return new Promise<ArrayBuffer>((resolve, reject) => {
        window.__releaseImport = () => {
          void original.call(this).then(resolve, reject);
        };
      });
    };
  });
  const before = JSON.parse(await page.locator("#policy-json").inputValue());
  const older = { ...before, label: "Older delayed policy" };
  const newer = { ...before, label: "Newer policy choice" };
  const input = page.getByLabel("Open policy JSON", { exact: true });
  async function hold() {
    await page.evaluate(() => {
      window.__heldImport = false;
    });
    await input.setInputFiles({
      name: "held-policy.json",
      mimeType: "application/json",
      buffer: Buffer.from(JSON.stringify(older)),
    });
    await page.waitForFunction(() => window.__heldImport === true);
  }
  await hold();
  await page.locator("#policy-json").fill(JSON.stringify(newer));
  await page.evaluate(() => window.__releaseImport?.());
  await expect(page.locator("#policy-json")).toHaveValue(JSON.stringify(newer));
  await expect(page.locator("#message")).toContainText(
    "Draft or assumptions changed",
  );
  await hold();
  await input.setInputFiles({
    name: "newer.json",
    mimeType: "application/json",
    buffer: Buffer.from(JSON.stringify(newer)),
  });
  await expect(page.locator("#message")).toContainText("draft only");
  await page.evaluate(() => window.__releaseImport?.());
  expect(JSON.parse(await page.locator("#policy-json").inputValue())).toEqual(
    newer,
  );
  await hold();
  await page.getByRole("button", { name: "Sign out" }).click();
  await expect(page.locator("#message")).toContainText("Signed out");
  await page.evaluate(() => window.__releaseImport?.());
  await expect(page.locator("#policy-json")).toHaveValue("");
  await expect(page.locator("#message")).toContainText("Signed out");
});

test("an operator cannot import standards even by dispatching the hidden file control", async ({
  page,
}) => {
  await login(page, "operator");
  const original = await (await page.request.get("/api/workspace")).json();
  const retained = await page.locator("#policy-json").inputValue();
  await expect(
    page.getByLabel("Open policy JSON", { exact: true }),
  ).toBeHidden();
  await page.getByLabel("Open policy JSON", { exact: true }).setInputFiles({
    name: "attempt.json",
    mimeType: "application/json",
    buffer: Buffer.from('{"label":"unapproved"}'),
  });
  expect(await page.locator("#policy-json").inputValue()).toBe(retained);
  const after = await (await page.request.get("/api/workspace")).json();
  expect(after.state).toEqual(original.state);
  expect(after.ledger_tip).toEqual(original.ledger_tip);
});
