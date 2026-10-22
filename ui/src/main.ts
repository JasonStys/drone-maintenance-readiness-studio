/** @file Jason Stys: private role-aware fleet desk, safe DOM rendering and generation-aware workflows. Lines: docs/SOURCE_MAP.md. */
import "./style.css";
import {
  minutes,
  reportId,
  sparkPoints,
  statusLabel,
  type Status,
} from "./view";
interface User {
  name: string;
  role: string;
  csrf: string;
}
interface Finding {
  code: string;
  status: Status;
  message: string;
}
interface Asset {
  id: string;
  serial: string;
  label: string;
  seconds: number;
  cycles: number;
  opening_seconds: number;
  kind?: string;
  profile?: string;
  retired?: number;
}
interface PartResult {
  id: string;
  status: Status;
  remaining_seconds: number | null;
  remaining_cycles: number | null;
  inspection_due: number | null;
  planning_days_to_usage_limit: number | null;
  findings: Finding[];
}
interface AircraftResult {
  id: string;
  status: Status;
  findings: Finding[];
  slots: { slot: string; component: string | null; status: Status }[];
}
interface Policy {
  label: string;
  profiles: { id: string; slots: { id: string; kind: string }[] }[];
}
interface State {
  generation: number;
  policy_version: number;
  policies: { version: number; content: Policy }[];
  aircraft: Asset[];
  components: Asset[];
  defects: {
    id: number;
    component: string;
    severity: string;
    note: string;
    closed: number;
  }[];
  work: {
    id: number;
    defect: number;
    reviewer: string | null;
    technician: string;
  }[];
  usage: {
    id: number;
    aircraft: string;
    components: string[];
    seconds: number;
    cycles: number;
    actor: string;
  }[];
}
interface Dashboard {
  state: State;
  ledger_tip: string;
  readiness: { aircraft: AircraftResult[]; components: PartResult[] };
  ledger: unknown[];
  reports: { id: number; generation: number; creator: string }[];
}
interface Report {
  id: number;
  stale: boolean;
  review: { actor: string; note: string } | null;
  creator: string;
  result: {
    status: Status;
    generation: number;
    components: PartResult[];
    flight_authorization: false;
  };
}
class ApiError extends Error {
  constructor(
    message: string,
    public status: number,
  ) {
    super(message);
  }
}
let user: User | null = null;
let dashboard: Dashboard | null = null;
let assessment: Report | null = null;
let selectedAircraft = "flood";
let selectedComponent = "flood-battery";
let epoch = 0;
let busy = false;
let logoutPending = false;
let pendingUsage: Record<string, unknown> | null = null;
/** Fixed document IDs only; user input never creates selectors or HTML. */
function el<T extends HTMLElement = HTMLElement>(id: string): T {
  return document.getElementById(id) as T;
}
/** Read literal control value; JSON schemas and backend role checks are authoritative. */
function value(id: string): string {
  return el<HTMLInputElement>(id).value;
}
/** Render private text without HTML parsing, including notes, serials and policy names. */
function text(id: string, content: string): void {
  el(id).textContent = content;
}
/** Buttons respect current role even after a task's finally block; UI checks are not authorization. */
function buttons(): void {
  for (const button of document.querySelectorAll<HTMLButtonElement>("button")) {
    const roles = button.dataset.roles?.split(" ");
    button.disabled =
      logoutPending ||
      (button.id !== "logout" &&
        (busy || (!!roles && !roles.includes(user?.role ?? ""))));
  }
}
/** Same-origin JSON only; reject late account/selection responses and clear private view on expiry. */
async function api<T>(path: string, body?: unknown): Promise<T> {
  const generation = epoch;
  const response = await fetch(path, {
    method: body === undefined ? "GET" : "POST",
    headers:
      body === undefined
        ? {}
        : {
            "Content-Type": "application/json",
            "X-CSRF-Token": user?.csrf ?? "",
          },
    ...(body === undefined ? {} : { body: JSON.stringify(body) }),
  });
  const result = await response.json();
  if (generation !== epoch) throw new Error("Workspace changed");
  if (response.status === 401 && path !== "/api/login") {
    reset();
    text("message", "Session expired or revoked; sign in again");
  }
  if (!response.ok)
    throw new ApiError(result.detail ?? "Request failed", response.status);
  return result as T;
}
/** Serialize visible writes and ignore obsolete errors after logout/account changes. */
async function task(action: () => Promise<void>): Promise<void> {
  if (busy || logoutPending) return;
  const generation = epoch;
  busy = true;
  buttons();
  text("message", "Working locally…");
  try {
    await action();
    if (generation === epoch)
      text("message", "Ready · private record-based workspace");
  } catch (error) {
    if (generation === epoch) text("message", (error as Error).message);
  } finally {
    busy = false;
    buttons();
  }
}
/** Remove private state, pending usage payload, report links and rendered notes from signed-out DOM. */
function reset(): void {
  epoch++;
  user = null;
  dashboard = null;
  assessment = null;
  pendingUsage = null;
  for (const id of ["roster", "parts", "defects", "metrics", "usage-chart"])
    el(id).replaceChildren();
  for (const id of [
    "identity",
    "aircraft-name",
    "aircraft-status",
    "aircraft-totals",
    "aircraft-findings",
    "component-summary",
    "component-findings",
    "ledger",
    "usage-history",
    "policy-label",
    "generation",
    "report-state",
    "usage-result",
  ])
    text(id, "");
  for (const area of document.querySelectorAll<HTMLTextAreaElement>("textarea"))
    area.value = "";
  for (const id of [
    "report-select",
    "component-select",
    "slot-select",
    "incoming",
    "work-defect",
    "verify-work",
  ])
    el(id).replaceChildren();
  el<HTMLInputElement>("password").value = "";
  el<HTMLAnchorElement>("report-export").removeAttribute("href");
  el("report-export").hidden = true;
  el("retry-usage").hidden = true;
  el("workspace").hidden = true;
  el("login-panel").hidden = false;
}
/** Rebuild a safe select while preserving an explicit valid selection. */
function options(
  id: string,
  entries: [string, string][],
  selection?: string,
): void {
  const select = el<HTMLSelectElement>(id);
  const previous = selection ?? select.value;
  select.replaceChildren();
  for (const [key, label] of entries) {
    const option = document.createElement("option");
    option.value = key;
    option.textContent = label;
    select.append(option);
  }
  if (entries.some(([key]) => key === previous)) select.value = previous;
}
/** Show all findings; no low-priority item is dropped when a blocker takes precedence. */
function findings(id: string, entries: Finding[]): void {
  const root = el(id);
  root.replaceChildren();
  for (const finding of entries) {
    const item = document.createElement("p");
    item.className = `finding ${finding.status}`;
    item.textContent = `${finding.code}: ${finding.message}`;
    root.append(item);
  }
}
/** Re-render current coherent generation and clear any prior report's claim of freshness until re-fetched. */
function render(next: Dashboard): void {
  dashboard = next;
  const state = next.state;
  if (!state.aircraft.some((asset) => asset.id === selectedAircraft))
    selectedAircraft = state.aircraft[0]?.id ?? "";
  if (!state.components.some((part) => part.id === selectedComponent))
    selectedComponent = state.components[0]?.id ?? "";
  const metrics = el("metrics");
  metrics.replaceChildren();
  for (const status of [
    "blocked",
    "unknown",
    "review",
    "within_recorded_limits",
  ] as Status[]) {
    const div = document.createElement("div");
    div.className = "metric";
    const count = document.createElement("strong");
    count.textContent = String(
      next.readiness.aircraft.filter((asset) => asset.status === status).length,
    );
    const label = document.createElement("span");
    label.textContent = statusLabel(status);
    div.append(count, label);
    metrics.append(div);
  }
  const policy = state.policies.find(
    (record) => record.version === state.policy_version,
  )!.content;
  text("policy-label", `${policy.label} · version ${state.policy_version}`);
  text(
    "generation",
    `Generation ${state.generation}\nSHA-256 ${next.ledger_tip}`,
  );
  el<HTMLTextAreaElement>("policy-json").value = JSON.stringify(
    policy,
    null,
    2,
  );
  el("admin-panel").hidden = user?.role !== "admin";
  if (!value("aircraft-json"))
    el<HTMLTextAreaElement>("aircraft-json").value = JSON.stringify(
      {
        id: "new-aircraft",
        serial: "EXAMPLE-AIR-001",
        label: "New aircraft opening record",
        profile: policy.profiles[0].id,
        opening_seconds: 0,
        opening_cycles: 0,
        history_complete: false,
        source_note: "Replace with verified opening-history reference",
      },
      null,
      2,
    );
  if (!value("component-json"))
    el<HTMLTextAreaElement>("component-json").value = JSON.stringify(
      {
        id: "new-component",
        serial: "EXAMPLE-PART-001",
        label: "New serialized component",
        kind: "battery",
        opening_seconds: 0,
        opening_cycles: 0,
        history_complete: false,
        source_note: "Replace with verified component-history reference",
      },
      null,
      2,
    );
  options(
    "component-select",
    state.components.map((part) => [part.id, `${part.serial} · ${part.label}`]),
    selectedComponent,
  );
  options("incoming", [
    ["", "Remove only"],
    ...state.components.map((part): [string, string] => [
      part.id,
      `${part.serial} · ${part.kind}${part.retired ? " · RETIRED" : ""}`,
    ]),
  ]);
  options("work-defect", [
    ["", "Choose open defect"],
    ...state.defects
      .filter(
        (d) => !d.closed && !state.work.some((work) => work.defect === d.id),
      )
      .map((d): [string, string] => [
        String(d.id),
        `#${d.id} · ${d.component} · ${d.severity}`,
      ]),
  ]);
  options("verify-work", [
    ["", "Choose completed work"],
    ...state.work
      .filter((work) => !work.reviewer)
      .map((work): [string, string] => [
        String(work.id),
        `#${work.id} · defect ${work.defect} · ${work.technician}`,
      ]),
  ]);
  options(
    "report-select",
    [
      ["", "Choose an assessment"],
      ...next.reports.map((record): [string, string] => [
        String(record.id),
        `#${record.id} · generation ${record.generation} · ${record.creator}`,
      ]),
    ],
    assessment ? String(assessment.id) : "",
  );
  text("ledger", JSON.stringify(next.ledger, null, 2));
  text("usage-history", JSON.stringify(state.usage.slice(-20), null, 2));
  const defects = el("defects");
  defects.replaceChildren();
  for (const defect of state.defects.filter((entry) => !entry.closed)) {
    const p = document.createElement("p");
    p.className =
      "finding " + (defect.severity === "blocking" ? "blocked" : "review");
    p.textContent = `#${defect.id} · ${defect.component} · ${defect.note}`;
    defects.append(p);
  }
  if (assessment) {
    text(
      "report-state",
      "Records refreshed; reload saved assessment to check freshness",
    );
    el("review-form").hidden = true;
  }
  roster();
  aircraftDesk();
  componentDesk();
  buttons();
}
/** Fleet filter and selection are local presentation only, not an authorization boundary. */
function roster(): void {
  const root = el("roster");
  root.replaceChildren();
  if (!dashboard) return;
  for (const asset of dashboard.state.aircraft) {
    const result = dashboard.readiness.aircraft.find(
      (item) => item.id === asset.id,
    )!;
    if (
      value("status-filter") !== "all" &&
      value("status-filter") !== result.status
    )
      continue;
    const button = document.createElement("button");
    button.className = "roster-item";
    button.setAttribute("aria-pressed", String(asset.id === selectedAircraft));
    button.textContent = `${asset.label} · ${statusLabel(result.status)}`;
    button.onclick = () => {
      selectedAircraft = asset.id;
      roster();
      aircraftDesk();
    };
    root.append(button);
  }
}
/** Display exact installed identity and current per-part evidence without inferring missing components. */
function aircraftDesk(): void {
  if (!dashboard) return;
  const asset = dashboard.state.aircraft.find(
    (item) => item.id === selectedAircraft,
  );
  const result = dashboard.readiness.aircraft.find(
    (item) => item.id === selectedAircraft,
  );
  el("parts").replaceChildren();
  if (!asset || !result) {
    text(
      "aircraft-name",
      "No aircraft records; an administrator can add an opening record",
    );
    return;
  }
  text("aircraft-name", asset.label);
  text(
    "aircraft-totals",
    `${asset.serial} · ${minutes(asset.seconds)} · ${asset.cycles} operating cycles`,
  );
  text("aircraft-status", statusLabel(result.status));
  el("aircraft-status").className = `badge ${result.status}`;
  const policy = dashboard.state.policies.find(
    (record) => record.version === dashboard!.state.policy_version,
  )!.content;
  const profile = policy.profiles.find((entry) => entry.id === asset.profile);
  options(
    "slot-select",
    (profile?.slots ?? []).map((slot) => [
      slot.id,
      `${slot.id} · ${slot.kind}`,
    ]),
  );
  findings("aircraft-findings", result.findings);
  for (const slot of result.slots) {
    const row = document.createElement("tr");
    const part = dashboard.state.components.find(
      (entry) => entry.id === slot.component,
    );
    const status = dashboard.readiness.components.find(
      (entry) => entry.id === slot.component,
    );
    for (const content of [
      `${slot.slot}\n${part?.serial ?? "Missing component"}`,
      part ? `${minutes(part.seconds)}\n${part.cycles} cycles` : "Unknown",
      status
        ? `${minutes(status.remaining_seconds)} / ${status.remaining_cycles ?? "?"} cycles\nInspection: ${status.inspection_due === null ? "unknown" : new Date(status.inspection_due * 1000).toLocaleString()}`
        : "Unknown",
      statusLabel(slot.status),
    ]) {
      const cell = document.createElement("td");
      cell.textContent = content;
      row.append(cell);
    }
    row.lastElementChild!.className = slot.status;
    el("parts").append(row);
  }
}
/** Show cumulative component life, all current findings and discrete recorded-attribution chart. */
function componentDesk(): void {
  if (!dashboard) return;
  const part = dashboard.state.components.find(
    (entry) => entry.id === selectedComponent,
  );
  const result = dashboard.readiness.components.find(
    (entry) => entry.id === selectedComponent,
  );
  if (!part || !result) {
    text("component-summary", "No components recorded");
    return;
  }
  text(
    "component-summary",
    `${part.serial} · ${part.label} · ${minutes(part.seconds)} · ${part.cycles} cycles · ${statusLabel(result.status)} · Scenario days to usage limit: ${result.planning_days_to_usage_limit ?? "unknown/no finite rate"}`,
  );
  findings("component-findings", result.findings);
  el("battery-fields").hidden = part.kind !== "battery";
  let cumulative = part.opening_seconds;
  const values = [cumulative];
  for (const record of dashboard.state.usage)
    if (record.components.includes(part.id)) {
      cumulative += record.seconds;
      values.push(cumulative);
    }
  const chart = el("usage-chart");
  chart.replaceChildren();
  const line = document.createElementNS(
    "http://www.w3.org/2000/svg",
    "polyline",
  );
  line.setAttribute("points", sparkPoints(values));
  line.setAttribute("stroke", "#9edbcd");
  line.setAttribute("stroke-width", "3");
  line.setAttribute("fill", "none");
  chart.append(line);
}
/** Load a coherent current workspace and then refresh a selected report's staleness. */
async function refresh(): Promise<void> {
  render(await api<Dashboard>("/api/workspace"));
  if (assessment)
    showReport(await api<Report>(`/api/assessments/${assessment.id}`));
}
/** Bind all mutations to the displayed generation; a conflict requires explicit refresh, not automatic replay. */
async function mutate(
  path: string,
  fields: Record<string, unknown>,
): Promise<void> {
  if (dashboard)
    render(
      await api<Dashboard>(path, {
        expected_generation: dashboard.state.generation,
        ...fields,
      }),
    );
}
/** Report acknowledgement never changes the preserved readiness finding. */
function showReport(report: Report): void {
  assessment = report;
  text(
    "report-state",
    `Assessment #${report.id} · ${report.stale ? "STALE" : "Current"} · ${statusLabel(report.result.status)} · generation ${report.result.generation}${report.review ? ` · acknowledged by ${report.review.actor}` : " · not independently acknowledged"} · flight authorization: false`,
  );
  el<HTMLAnchorElement>("report-export").href =
    `/api/assessments/${report.id}/export`;
  el("report-export").hidden = false;
  el("review-form").hidden =
    user?.role !== "reviewer" ||
    report.stale ||
    !!report.review ||
    report.creator === user.name;
}
/** Sign-in enters the staff role only after server authentication; no private data persists in storage. */
el<HTMLFormElement>("login-form").onsubmit = (event) => {
  event.preventDefault();
  void task(async () => {
    user = await api<User>("/api/login", {
      username: value("username"),
      password: value("password"),
    });
    el<HTMLInputElement>("password").value = "";
    text("identity", `${user.name} · ${user.role}`);
    el("login-panel").hidden = true;
    el("workspace").hidden = false;
    await refresh();
  });
};
/** Logout clears DOM immediately and waits for server revocation before another login. */
el("logout").onclick = () => {
  const csrf = user?.csrf ?? "";
  logoutPending = true;
  reset();
  buttons();
  text("message", "Signing out…");
  void fetch("/api/logout", {
    method: "POST",
    headers: { "Content-Type": "application/json", "X-CSRF-Token": csrf },
    body: "{}",
  })
    .then((response) =>
      text(
        "message",
        response.ok
          ? "Signed out; private view cleared"
          : "View cleared; sign-out failed. Close this browser session.",
      ),
    )
    .catch(() =>
      text(
        "message",
        "View cleared; server unavailable. Close this browser session.",
      ),
    )
    .finally(() => {
      logoutPending = false;
      buttons();
    });
};
el("refresh").onclick = () => void task(refresh);
el("status-filter").onchange = roster;
el("component-select").onchange = () => {
  selectedComponent = value("component-select");
  componentDesk();
};
/** An ambiguous failed usage request retains its exact key/body for an explicit safe retry. */
async function sendUsage(): Promise<void> {
  if (!pendingUsage) return;
  try {
    const next = await api<
      Dashboard & { write: { duplicate: boolean; id: number } }
    >("/api/usage", pendingUsage);
    pendingUsage = null;
    el("retry-usage").hidden = true;
    render(next);
    text(
      "usage-result",
      `Entry #${next.write.id} · ${next.write.duplicate ? "existing request recovered without double counting" : "recorded once"}`,
    );
  } catch (error) {
    if (error instanceof ApiError && error.status >= 400 && error.status < 500)
      pendingUsage = null;
    el("retry-usage").hidden = pendingUsage === null;
    throw error;
  }
}
el<HTMLFormElement>("usage-form").onsubmit = (event) => {
  event.preventDefault();
  void task(async () => {
    if (!dashboard) return;
    if (pendingUsage)
      throw new Error(
        "Retry the pending usage request before creating another",
      );
    pendingUsage = {
      expected_generation: dashboard.state.generation,
      aircraft: selectedAircraft,
      seconds: Number(value("usage-minutes")) * 60,
      cycles: Number(value("usage-cycles")),
      request_id: crypto.randomUUID().replaceAll("-", ""),
      note: value("usage-note"),
    };
    await sendUsage();
  });
};
el("retry-usage").onclick = () => void task(sendUsage);
el<HTMLFormElement>("assess-form").onsubmit = (event) => {
  event.preventDefault();
  void task(async () => {
    if (!dashboard) return;
    const report = await api<Report>("/api/assessments", {
      expected_generation: dashboard.state.generation,
      assumptions: {
        daily_seconds: Number(value("daily-minutes")) * 60,
        daily_cycles: Number(value("daily-cycles")),
      },
    });
    showReport(report);
    await refresh();
  });
};
el("report-select").onchange = () =>
  void task(async () => {
    const id = reportId(value("report-select"));
    if (id !== null) showReport(await api<Report>(`/api/assessments/${id}`));
  });
el<HTMLFormElement>("review-form").onsubmit = (event) => {
  event.preventDefault();
  void task(async () => {
    if (assessment)
      showReport(
        await api<Report>(`/api/assessments/${assessment.id}/review`, {
          note: value("review-note"),
        }),
      );
  });
};
el<HTMLFormElement>("swap-form").onsubmit = (event) => {
  event.preventDefault();
  void task(() =>
    mutate("/api/swaps", {
      aircraft: selectedAircraft,
      slot: value("slot-select"),
      component: value("incoming") || null,
      note: value("swap-note"),
    }),
  );
};
el<HTMLFormElement>("inspection-form").onsubmit = (event) => {
  event.preventDefault();
  void task(() => {
    const battery =
      dashboard?.state.components.find((part) => part.id === selectedComponent)
        ?.kind === "battery";
    return mutate("/api/inspections", {
      component: selectedComponent,
      passed: value("inspection-result") === "pass",
      capacity_pct:
        battery && value("capacity") !== "" ? Number(value("capacity")) : null,
      resistance_mohm:
        battery && value("resistance") !== ""
          ? Number(value("resistance"))
          : null,
      note: value("inspection-note"),
    });
  });
};
el<HTMLFormElement>("defect-form").onsubmit = (event) => {
  event.preventDefault();
  void task(() =>
    mutate("/api/defects", {
      component: selectedComponent,
      severity: value("severity"),
      note: value("defect-note"),
    }),
  );
};
el<HTMLFormElement>("work-form").onsubmit = (event) => {
  event.preventDefault();
  void task(() =>
    mutate("/api/work", {
      defect: Number(value("work-defect")),
      note: value("work-note"),
    }),
  );
};
el<HTMLFormElement>("verify-form").onsubmit = (event) => {
  event.preventDefault();
  void task(() =>
    mutate("/api/work/verify", {
      work: Number(value("verify-work")),
      note: value("verify-note"),
    }),
  );
};
el("retire").onclick = () =>
  void task(async () => {
    if (!el<HTMLInputElement>("retire-confirm").checked)
      throw new Error("Confirm irreversible local retirement first");
    await mutate("/api/retire", {
      component: selectedComponent,
      note: value("retire-note"),
    });
  });
el<HTMLFormElement>("policy-form").onsubmit = (event) => {
  event.preventDefault();
  void task(() =>
    mutate("/api/policies", { policy: JSON.parse(value("policy-json")) }),
  );
};
el<HTMLFormElement>("aircraft-form").onsubmit = (event) => {
  event.preventDefault();
  void task(() =>
    mutate("/api/aircraft", { aircraft: JSON.parse(value("aircraft-json")) }),
  );
};
el<HTMLFormElement>("component-form").onsubmit = (event) => {
  event.preventDefault();
  void task(() =>
    mutate("/api/components", {
      component: JSON.parse(value("component-json")),
    }),
  );
};
void task(async () => {
  try {
    user = await api<User>("/api/me");
    text("identity", `${user.name} · ${user.role}`);
    el("workspace").hidden = false;
    el("login-panel").hidden = true;
    await refresh();
  } catch {
    reset();
    text("message", "Sign in with your locally provisioned staff account");
  }
});
