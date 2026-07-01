"""Career history tracker — loads, indexes, and queries journalist career data.

Reads career events from ``profiles/careers/journalists.yaml`` and builds
indexed ``JournalistProfile`` objects.  Also auto-detects migration events
from consecutive career entries at different publications.
"""

from __future__ import annotations

import os
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path
from typing import Optional

import yaml

from mediascope.careers.models import (
    CareerEvent,
    JournalistProfile,
    MigrationEvent,
)


class CareerTracker:
    """Load and query journalist career histories.

    Usage::

        tracker = CareerTracker(profiles_dir="profiles/careers")
        tracker.load()

        # Get a single journalist
        profile = tracker.get("Zoë Schiffer")

        # Find all journalists who worked at a publication
        wired_writers = tracker.by_publication("wired")

        # Find migrations between two tracked publications
        migrations = tracker.find_migrations(from_pub="mit-tech-review",
                                              to_pub="atlantic")
    """

    def __init__(self, profiles_dir: str | Path | None = None):
        self._profiles_dir = Path(profiles_dir) if profiles_dir else self._default_dir()
        self._journalists: dict[str, JournalistProfile] = {}
        self._by_pub: dict[str, list[str]] = defaultdict(list)
        self._loaded = False

    @staticmethod
    def _default_dir() -> Path:
        """Resolve the default profiles/careers directory."""
        # Walk up from this file → mediascope/ → repo root → profiles/careers
        here = Path(__file__).resolve().parent
        candidates = [
            here.parent.parent / "profiles" / "careers",
            Path.cwd() / "profiles" / "careers",
            Path(os.environ.get("MEDIASCOPE_PROFILES_DIR", "")) / "careers",
        ]
        for c in candidates:
            if c.is_dir():
                return c
        return candidates[0]

    # ------------------------------------------------------------------
    # Loading
    # ------------------------------------------------------------------

    def load(self, journalists_file: str | Path | None = None) -> None:
        """Load career events from YAML.

        Args:
            journalists_file: Explicit path to the journalists YAML file.
                Defaults to ``profiles/careers/journalists.yaml``.
        """
        path = Path(journalists_file) if journalists_file else self._profiles_dir / "journalists.yaml"
        if not path.exists():
            raise FileNotFoundError(f"Career data not found at {path}")

        with open(path, "r", encoding="utf-8") as fh:
            raw = yaml.safe_load(fh) or {}

        journalists_data = raw.get("journalists", [])

        for entry in journalists_data:
            name = entry["name"]
            events: list[CareerEvent] = []

            for ev in entry.get("career", []):
                events.append(
                    CareerEvent(
                        journalist_name=name,
                        event_type=ev.get("event_type", "hired"),
                        publication_slug=ev["publication"],
                        role=ev.get("role", "staff_writer"),
                        date_start=_parse_date(ev["start"]),
                        date_end=_parse_date(ev.get("end")) if ev.get("end") else None,
                        source_url=ev.get("source_url", ""),
                        beat=ev.get("beat"),
                        notes=ev.get("notes"),
                    )
                )

            # Sort events chronologically
            events.sort(key=lambda e: e.date_start)

            profile = JournalistProfile(name=name, events=events)

            # Auto-detect migrations
            migrations = self._detect_migrations(events)
            profile.migrations = migrations

            self._journalists[name.lower()] = profile

            # Index by publication
            for pub in profile.publications_worked_at:
                if name.lower() not in self._by_pub[pub.lower()]:
                    self._by_pub[pub.lower()].append(name.lower())

        self._loaded = True

    def _detect_migrations(self, events: list[CareerEvent]) -> list[MigrationEvent]:
        """Infer migration events from chronological career events.

        A migration is detected when a journalist has a ``departed`` event
        at one publication followed by a ``hired`` event at another, or when
        consecutive tenure events at different publications overlap or are
        within 180 days of each other.
        """
        migrations: list[MigrationEvent] = []

        # Group events by publication, find departure–arrival pairs
        departures: list[CareerEvent] = []
        arrivals: list[CareerEvent] = []

        for ev in events:
            if ev.event_type == "departed" or (ev.date_end is not None):
                departures.append(ev)
            if ev.event_type == "hired":
                arrivals.append(ev)

        # Also detect from sequential tenure events at different publications
        # Include all event types that represent a real position/tenure.
        # Exclude "education" (pre-career), "departed" (already handled above),
        # and "beat_change"/"promoted"/"editorial_role_change" (within same pub).
        _TENURE_EVENT_TYPES = frozenset({
            "hired", "freelance", "founded", "intern", "returned", "rehired",
            "career_change", "fellowship", "foreign_posting", "other",
        })
        tenure_events = [e for e in events if e.event_type in _TENURE_EVENT_TYPES]
        for i in range(len(tenure_events) - 1):
            curr = tenure_events[i]
            nxt = tenure_events[i + 1]

            if curr.publication_slug == nxt.publication_slug:
                continue

            # Determine departure date
            dep_date = curr.date_end or nxt.date_start
            arr_date = nxt.date_start
            gap = (arr_date - dep_date).days if dep_date else 0

            # Only count if within 365 days gap
            if gap > 365:
                continue

            migration = MigrationEvent(
                journalist_name=curr.journalist_name,
                from_publication=curr.publication_slug,
                to_publication=nxt.publication_slug,
                departure_date=dep_date,
                arrival_date=arr_date,
                from_role=curr.role,
                to_role=nxt.role,
                gap_days=max(0, gap),
                notes=f"Auto-detected from career timeline",
            )
            migrations.append(migration)

        return migrations

    # ------------------------------------------------------------------
    # Querying
    # ------------------------------------------------------------------

    def _ensure_loaded(self) -> None:
        if not self._loaded:
            try:
                self.load()
            except FileNotFoundError:
                pass

    def get(self, name: str) -> Optional[JournalistProfile]:
        """Retrieve a journalist profile by name (case-insensitive)."""
        self._ensure_loaded()
        return self._journalists.get(name.lower())

    def all_journalists(self) -> list[JournalistProfile]:
        """Return all loaded journalist profiles."""
        self._ensure_loaded()
        return list(self._journalists.values())

    def by_publication(self, publication_slug: str) -> list[JournalistProfile]:
        """Return all journalists who worked at a given publication."""
        self._ensure_loaded()
        names = self._by_pub.get(publication_slug.lower(), [])
        return [self._journalists[n] for n in names if n in self._journalists]

    def find_migrations(
        self,
        from_pub: Optional[str] = None,
        to_pub: Optional[str] = None,
    ) -> list[MigrationEvent]:
        """Find migration events, optionally filtering by source/destination.

        Args:
            from_pub: Filter to migrations departing this publication.
            to_pub: Filter to migrations arriving at this publication.

        Returns:
            Matching migration events sorted chronologically.
        """
        self._ensure_loaded()
        all_migrations: list[MigrationEvent] = []
        for profile in self._journalists.values():
            for m in profile.migrations:
                if from_pub and m.from_publication.lower() != from_pub.lower():
                    continue
                if to_pub and m.to_publication.lower() != to_pub.lower():
                    continue
                all_migrations.append(m)
        return sorted(all_migrations, key=lambda m: m.departure_date)

    def journalists_at(
        self,
        publication_slug: str,
        on_date: date,
    ) -> list[JournalistProfile]:
        """Return journalists who were at a publication on a specific date."""
        self._ensure_loaded()
        result = []
        for profile in self._journalists.values():
            for event in profile.events:
                if event.publication_slug.lower() != publication_slug.lower():
                    continue
                start = event.date_start
                end = event.date_end or date.today()
                if start <= on_date <= end:
                    result.append(profile)
                    break
        return result


def _parse_date(val) -> date:
    """Parse a date from YAML — handles date objects, strings, year-month, and bare years."""
    if isinstance(val, date):
        return val
    if isinstance(val, (int, float)):
        # Bare year as number (e.g. 2008)
        return date(int(val), 1, 1)
    if isinstance(val, str):
        val = val.strip().strip("'\"")
        # Strip leading approximate marker (~2022 → 2022)
        if val.startswith("~"):
            val = val[1:]
        parts = val.split("-")
        if len(parts) == 1:
            # Bare year string → January 1
            return date(int(parts[0]), 1, 1)
        if len(parts) == 2:
            # Year-month only → first of month
            return date(int(parts[0]), int(parts[1]), 1)
        if len(parts) == 3:
            return date(int(parts[0]), int(parts[1]), int(parts[2]))
    raise ValueError(f"Cannot parse date from {val!r}")
