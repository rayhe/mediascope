"""Data models for editorial career tracking and bias decomposition.

Every model is a frozen dataclass that serialises cleanly to JSON/YAML so
career data can live in version-controlled profile files alongside the
publication YAML profiles.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import date
from typing import Optional


# ---------------------------------------------------------------------------
# Career events
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class CareerEvent:
    """A single event in a journalist's career timeline.

    Attributes:
        journalist_name: Canonical name (e.g. "Zoë Schiffer").
        event_type: One of ``hired``, ``departed``, ``promoted``,
            ``freelance``, ``editorial_role_change``.
        publication_slug: MediaScope publication slug or free-text outlet name
            for publications not yet profiled.
        role: Role at the publication. One of ``staff_writer``,
            ``senior_writer``, ``editor``, ``section_editor``, ``eic``,
            ``contributor``, ``columnist``, ``correspondent``.
        date_start: When the event began (hire date, promotion date, etc.).
        date_end: When the event ended.  ``None`` if still active.
        source_url: Verification link (LinkedIn, press release, byline archive).
        beat: Optional beat / topic focus (e.g. "AI", "tech labor").
        notes: Free-text context.
    """

    journalist_name: str
    event_type: str
    publication_slug: str
    role: str
    date_start: date
    date_end: Optional[date] = None
    source_url: str = ""
    beat: Optional[str] = None
    notes: Optional[str] = None

    # Valid event types
    VALID_EVENT_TYPES = frozenset({
        "hired",
        "departed",
        "promoted",
        "freelance",
        "editorial_role_change",
        "beat_change",
        "fellowship",
        "career_change",
        "intern",
        "founded",
        "returned",
        "rehired",
        "education",
        "foreign_posting",
        "other",
    })

    # Valid roles (ordered roughly by seniority)
    VALID_ROLES = frozenset({
        "contributor",
        "correspondent",
        "staff_writer",
        "senior_writer",
        "columnist",
        "editor",
        "section_editor",
        "managing_editor",
        "deputy_editor",
        "eic",
    })

    def __post_init__(self):
        if self.event_type not in self.VALID_EVENT_TYPES:
            raise ValueError(
                f"Invalid event_type '{self.event_type}'. "
                f"Must be one of {sorted(self.VALID_EVENT_TYPES)}"
            )

    def to_dict(self) -> dict:
        d = asdict(self)
        d["date_start"] = self.date_start.isoformat()
        if self.date_end:
            d["date_end"] = self.date_end.isoformat()
        return d


# ---------------------------------------------------------------------------
# Migration events
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class MigrationEvent:
    """A journalist moving from one publication to another.

    Automatically derived from consecutive ``CareerEvent`` records or
    hand-coded in career YAML files.
    """

    journalist_name: str
    from_publication: str
    to_publication: str
    departure_date: date
    arrival_date: date
    from_role: str
    to_role: str
    gap_days: int = 0  # time between departure and arrival
    source_url: str = ""
    notes: Optional[str] = None

    @property
    def is_lateral(self) -> bool:
        """True if the journalist moved at roughly the same seniority level."""
        seniority_tiers = {
            "contributor": 0, "correspondent": 1, "staff_writer": 2,
            "senior_writer": 3, "columnist": 3, "editor": 4,
            "section_editor": 5, "managing_editor": 6,
            "deputy_editor": 6, "eic": 7,
        }
        from_tier = seniority_tiers.get(self.from_role, 2)
        to_tier = seniority_tiers.get(self.to_role, 2)
        return abs(from_tier - to_tier) <= 1

    @property
    def is_promotion(self) -> bool:
        """True if the destination role is notably more senior."""
        seniority_tiers = {
            "contributor": 0, "correspondent": 1, "staff_writer": 2,
            "senior_writer": 3, "columnist": 3, "editor": 4,
            "section_editor": 5, "managing_editor": 6,
            "deputy_editor": 6, "eic": 7,
        }
        return (
            seniority_tiers.get(self.to_role, 2)
            - seniority_tiers.get(self.from_role, 2)
        ) >= 2

    def to_dict(self) -> dict:
        d = asdict(self)
        d["departure_date"] = self.departure_date.isoformat()
        d["arrival_date"] = self.arrival_date.isoformat()
        d["is_lateral"] = self.is_lateral
        d["is_promotion"] = self.is_promotion
        return d


# ---------------------------------------------------------------------------
# Editorial leadership changes
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class EditorialLeadershipChange:
    """A change in editorial leadership at a publication.

    These events are tracked separately from journalist careers because
    leadership changes affect institutional tone, independent of the
    individual leader's personal bias.
    """

    publication_slug: str
    position: str  # eic, managing_editor, section_editor, editorial_director
    outgoing_name: Optional[str]
    incoming_name: str
    effective_date: date
    source_url: str = ""
    notes: Optional[str] = None

    VALID_POSITIONS = frozenset({
        "eic",
        "editorial_director",
        "managing_editor",
        "deputy_editor",
        "section_editor",
        "executive_editor",
    })

    def to_dict(self) -> dict:
        d = asdict(self)
        d["effective_date"] = self.effective_date.isoformat()
        return d


# ---------------------------------------------------------------------------
# Journalist profile (aggregate)
# ---------------------------------------------------------------------------

@dataclass
class JournalistProfile:
    """Aggregated career profile for a single journalist.

    Built from a sequence of ``CareerEvent`` records.  Provides convenience
    accessors for current outlet, career span, migration history, etc.
    """

    name: str
    events: list[CareerEvent] = field(default_factory=list)
    migrations: list[MigrationEvent] = field(default_factory=list)

    @property
    def current_publication(self) -> Optional[str]:
        """Publication the journalist is currently at (most recent open event)."""
        open_events = [e for e in self.events if e.date_end is None]
        if not open_events:
            return None
        return max(open_events, key=lambda e: e.date_start or date.min).publication_slug

    @property
    def current_role(self) -> Optional[str]:
        """Current role at the latest publication."""
        open_events = [e for e in self.events if e.date_end is None]
        if not open_events:
            return None
        return max(open_events, key=lambda e: e.date_start or date.min).role

    @property
    def career_span_years(self) -> float:
        """Approximate career span in years from earliest to latest event."""
        if not self.events:
            return 0.0
        earliest = min(e.date_start for e in self.events)
        latest = max(e.date_end or date.today() for e in self.events)
        return (latest - earliest).days / 365.25

    @property
    def publications_worked_at(self) -> list[str]:
        """Ordered list of unique publications (by first appearance)."""
        seen: set[str] = set()
        result: list[str] = []
        for e in sorted(self.events, key=lambda x: x.date_start or date.max):
            if e.publication_slug not in seen:
                seen.add(e.publication_slug)
                result.append(e.publication_slug)
        return result

    @property
    def n_publications(self) -> int:
        return len(self.publications_worked_at)

    def tenure_at(self, publication_slug: str) -> Optional[tuple[date, Optional[date]]]:
        """Return (start, end) dates for the journalist's tenure at a publication."""
        pub_events = [
            e for e in self.events if e.publication_slug == publication_slug
        ]
        if not pub_events:
            return None
        start = min(e.date_start for e in pub_events)
        ends = [e.date_end for e in pub_events]
        end = max((d for d in ends if d is not None), default=None)
        if any(d is None for d in ends):
            end = None  # still active
        return (start, end)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "current_publication": self.current_publication,
            "current_role": self.current_role,
            "career_span_years": round(self.career_span_years, 1),
            "publications_worked_at": self.publications_worked_at,
            "n_publications": self.n_publications,
            "events": [e.to_dict() for e in self.events],
            "migrations": [m.to_dict() for m in self.migrations],
        }


# ---------------------------------------------------------------------------
# Bias decomposition
# ---------------------------------------------------------------------------

@dataclass
class BiasDecomposition:
    """Decomposed bias attribution for a journalist.

    Total observed bias in a journalist's coverage is decomposed into:

    - **institutional_component**: How much the publication's culture drives tone.
      High values mean the publication shapes coverage regardless of who writes it.
    - **individual_component**: How much the journalist carries with them across outlets.
      High values mean the journalist's personal stance persists despite editorial context.
    - **interaction_effect**: Synergy between journalist and publication.
      High values mean this journalist-publication pairing amplifies bias beyond
      what either would produce alone.
    - **portable_bias_score**: 0.0 = fully adapts to each publication's norms,
      1.0 = identical tone everywhere regardless of outlet.

    The decomposition uses a two-way ANOVA framework applied to tone scores
    grouped by (journalist, publication) cells.
    """

    journalist_name: str
    institutional_component: float
    individual_component: float
    interaction_effect: float
    portable_bias_score: float  # 0 = fully adapts, 1 = fully portable
    n_publications: int
    n_articles: int
    confidence: float  # 0–1
    methodology_note: str = ""

    def to_dict(self) -> dict:
        return asdict(self)

    @property
    def dominant_source(self) -> str:
        """Whether bias is predominantly institutional or individual."""
        if self.institutional_component > self.individual_component:
            if self.institutional_component > self.interaction_effect:
                return "institutional"
            return "interaction"
        else:
            if self.individual_component > self.interaction_effect:
                return "individual"
            return "interaction"


# ---------------------------------------------------------------------------
# DiD result
# ---------------------------------------------------------------------------

@dataclass
class DifferenceInDifferencesResult:
    """Result of a difference-in-differences analysis around a migration event.

    The DiD estimator isolates the causal effect of a journalist's move by
    comparing pre/post tone changes at the source publication (treatment) to
    a control group that didn't experience the personnel change.

    ``did_estimate`` is the key number: the causal effect of the migration on
    coverage tone, net of secular trends.
    """

    journalist_name: str
    migration: MigrationEvent

    # Source-side analysis (Publication A after journalist leaves)
    source_pre_mean: float
    source_post_mean: float
    source_raw_change: float

    # Destination-side analysis (Publication B after journalist arrives)
    dest_pre_mean: float
    dest_post_mean: float
    dest_raw_change: float

    # Journalist's own tone change
    journalist_pre_mean: float
    journalist_post_mean: float
    journalist_tone_change: float

    # Control group (journalists who stayed at source publication)
    control_pre_mean: float
    control_post_mean: float
    control_change: float

    # The key causal estimate
    did_estimate: float  # (treatment_post - treatment_pre) - (control_post - control_pre)
    did_std_error: float
    did_p_value: float
    did_is_significant: bool

    # Interpretation
    portable_bias_estimate: float  # How much journalist tone is portable
    editorial_capture_estimate: float  # How much the new outlet changed journalist tone
    influence_estimate: float  # How much the journalist changed the destination outlet

    n_articles_pre: int
    n_articles_post: int
    window_days: int  # Analysis window (days before/after migration)
    methodology_note: str = ""

    def to_dict(self) -> dict:
        d = asdict(self)
        d["migration"] = self.migration.to_dict()
        return d
