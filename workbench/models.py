"""Jason Stys: finite, unit-explicit policy/lifecycle/write/review contracts.

Exact fields, functions and variables: docs/SOURCE_MAP.md. Unknown JSON fields are rejected.
"""

from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

Key = Annotated[str, Field(pattern=r"^[a-z][a-z0-9-]{2,39}$")]
Kind = Literal["battery", "motor", "propeller", "airframe", "payload", "assembly"]
Counter = Annotated[int, Field(ge=0, le=10**12)]
Note = Annotated[str, Field(min_length=10, max_length=500)]


class StrictModel(BaseModel):
    """Reject coercion, nonfinite numbers and extra client claims; server owns clocks/counters/roles."""

    model_config = ConfigDict(extra="forbid", strict=True, allow_inf_nan=False)


class Login(StrictModel):
    """Bound input before expensive password verification."""

    username: str = Field(min_length=3, max_length=40)
    password: str = Field(min_length=1, max_length=128)


class Limit(StrictModel):
    """Operator-entered illustrative limits, not universal manufacturer or regulatory thresholds."""

    kind: Kind
    seconds: int = Field(ge=60, le=10**9)
    cycles: int = Field(ge=1, le=10**7)
    inspection_days: int = Field(ge=1, le=365)


class Slot(StrictModel):
    """A required serialized part position; an assembly is not a record of each individual rotor."""

    id: Key
    kind: Kind


class Profile(StrictModel):
    """Named airframe configuration; supports up to sixteen required component positions."""

    id: Key
    label: str = Field(min_length=3, max_length=80)
    slots: list[Slot] = Field(min_length=1, max_length=16)

    @model_validator(mode="after")
    def unique(self):
        """Reject ambiguous positions instead of overwriting duplicate slot IDs."""
        if len({slot.id for slot in self.slots}) != len(self.slots):
            raise ValueError("Duplicate slot")
        return self


class Policy(StrictModel):
    """Versioned configured standards; evidence references are plain text, never fetched URLs."""

    label: str = Field(min_length=3, max_length=80)
    reference: Note
    profiles: list[Profile] = Field(min_length=1, max_length=8)
    limits: list[Limit] = Field(min_length=1, max_length=6)
    warning_percent: int = Field(ge=1, le=50)
    battery_min_capacity_pct: float = Field(ge=1, le=100)
    battery_max_resistance_mohm: float = Field(gt=0, le=1000)

    @model_validator(mode="after")
    def complete(self):
        """Every configured slot kind must have exactly one limit; profiles are unique."""
        kinds = {limit.kind for limit in self.limits}
        if len(kinds) != len(self.limits) or len({p.id for p in self.profiles}) != len(
            self.profiles
        ):
            raise ValueError("Duplicate profile/limit")
        if any(slot.kind not in kinds for profile in self.profiles for slot in profile.slots):
            raise ValueError("Required slot kind lacks limits")
        return self


class Asset(StrictModel):
    """Immutable identity/opening-history attestation; serial cannot be recreated to reset life."""

    id: Key
    serial: str = Field(pattern=r"^[A-Z0-9][A-Z0-9-]{2,59}$")
    label: str = Field(min_length=3, max_length=80)
    opening_seconds: Counter
    opening_cycles: Counter
    history_complete: bool
    source_note: Note


class Aircraft(Asset):
    """Airframe record whose profile identifies required positions."""

    profile: Key


class Component(Asset):
    """A physical serialized part; counters follow the part across aircraft swaps."""

    kind: Kind


class Change(StrictModel):
    """Global optimistic-concurrency version is required for every state mutation."""

    expected_generation: int = Field(ge=1)


class Publish(Change):
    """Administrator-only immutable policy publication."""

    policy: Policy


class NewAircraft(Change):
    """Administrator-provisioned immutable opening records."""

    aircraft: Aircraft


class NewComponent(Change):
    """Administrator-provisioned serialized part baseline; no counter-reset route."""

    component: Component


class Swap(Change):
    """Remove existing part and optionally install a compatible non-retired spare atomically."""

    aircraft: Key
    slot: Key
    component: Key | None
    note: Note


class Usage(Change):
    """Self-reported usage recorded now; installed part attribution comes only from the database."""

    aircraft: Key
    seconds: int = Field(ge=1, le=7200)
    cycles: int = Field(ge=1, le=100)
    request_id: str = Field(pattern=r"^[a-f0-9]{32}$")
    note: Note


class Inspection(Change):
    """Current-time inspection evidence; battery measurements are optional but missing means unknown."""

    component: Key
    passed: bool
    capacity_pct: float | None = Field(default=None, ge=0, le=100)
    resistance_mohm: float | None = Field(default=None, ge=0, le=1000)
    note: Note


class Defect(Change):
    """A watch item or blocking component defect, never silently closed by a later passed inspection."""

    component: Key
    severity: Literal["watch", "blocking"]
    note: Note


class Work(Change):
    """Technician completes recorded corrective work; it is not independent verification."""

    defect: int = Field(ge=1)
    note: Note


class Verify(Change):
    """Different reviewer verifies a completed work order after fresh passing inspection."""

    work: int = Field(ge=1)
    note: Note


class Retire(Change):
    """Irreversible local retirement after removal; records and life counters remain."""

    component: Key
    note: Note


class Assumptions(StrictModel):
    """Explicit constant workload scenario, not an AI/probabilistic remaining-life prediction."""

    daily_seconds: int = Field(ge=0, le=86400)
    daily_cycles: int = Field(ge=0, le=100)


class Assess(Change):
    """Capture complete fleet inputs, configured policy and planning assumptions at server time."""

    assumptions: Assumptions


class Review(StrictModel):
    """Independent acknowledgement cannot change or override a readiness finding."""

    note: Note
