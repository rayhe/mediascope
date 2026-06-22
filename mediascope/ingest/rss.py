"""RSS feed ingestion for MediaScope.

Fetches and filters RSS/Atom feed entries from publication profiles.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Any

import feedparser

from mediascope.config import PublicationProfile

logger = logging.getLogger(__name__)


@dataclass
class FeedEntry:
    """A single entry from an RSS/Atom feed."""

    title: str
    url: str
    published: datetime | None = None
    author: str = ""
    summary: str = ""
    tags: list[str] = field(default_factory=list)


def _parse_published(entry: Any) -> datetime | None:
    """Try to parse a publication date from a feedparser entry."""
    # feedparser provides published_parsed as a time.struct_time
    if hasattr(entry, "published_parsed") and entry.published_parsed:
        try:
            from calendar import timegm
            ts = timegm(entry.published_parsed)
            return datetime.fromtimestamp(ts, tz=timezone.utc)
        except (TypeError, ValueError, OverflowError):
            pass

    # Fallback: try the raw published string
    raw = getattr(entry, "published", None)
    if raw:
        try:
            return parsedate_to_datetime(raw)
        except (TypeError, ValueError):
            pass

    # Try updated_parsed as last resort
    if hasattr(entry, "updated_parsed") and entry.updated_parsed:
        try:
            from calendar import timegm
            ts = timegm(entry.updated_parsed)
            return datetime.fromtimestamp(ts, tz=timezone.utc)
        except (TypeError, ValueError, OverflowError):
            pass

    return None


def _extract_tags(entry: Any) -> list[str]:
    """Extract tag labels from a feedparser entry."""
    tags = []
    for tag in getattr(entry, "tags", []):
        label = getattr(tag, "term", None) or getattr(tag, "label", None)
        if label:
            tags.append(str(label).strip())
    return tags


def fetch_feed(url: str) -> list[FeedEntry]:
    """Fetch and parse a single RSS/Atom feed.

    Args:
        url: The feed URL.

    Returns:
        List of FeedEntry objects parsed from the feed.
    """
    logger.info("Fetching feed: %s", url)
    try:
        feed = feedparser.parse(url)
    except Exception as e:
        logger.warning("Failed to fetch feed %s: %s", url, e)
        return []

    if feed.bozo and not feed.entries:
        logger.warning(
            "Feed %s returned bozo error: %s",
            url,
            getattr(feed, "bozo_exception", "unknown"),
        )
        return []

    entries: list[FeedEntry] = []
    for entry in feed.entries:
        link = getattr(entry, "link", "") or ""
        title = getattr(entry, "title", "") or ""
        if not link:
            continue

        entries.append(
            FeedEntry(
                title=title.strip(),
                url=link.strip(),
                published=_parse_published(entry),
                author=(getattr(entry, "author", "") or "").strip(),
                summary=(getattr(entry, "summary", "") or "").strip(),
                tags=_extract_tags(entry),
            )
        )

    logger.info("Fetched %d entries from %s", len(entries), url)
    return entries


def fetch_all_feeds(profile: PublicationProfile) -> list[FeedEntry]:
    """Fetch all RSS feeds defined in a publication profile.

    Args:
        profile: A PublicationProfile with rss_feeds populated.

    Returns:
        Combined list of FeedEntry objects from all feeds, deduplicated by URL.
    """
    all_entries: list[FeedEntry] = []
    seen_urls: set[str] = set()

    for feed_url in profile.rss_feeds:
        entries = fetch_feed(feed_url)
        for entry in entries:
            if entry.url not in seen_urls:
                seen_urls.add(entry.url)
                all_entries.append(entry)

    logger.info(
        "Fetched %d unique entries across %d feeds for %s",
        len(all_entries),
        len(profile.rss_feeds),
        profile.name,
    )
    return all_entries


def filter_by_date(
    entries: list[FeedEntry],
    since: datetime,
    until: datetime,
) -> list[FeedEntry]:
    """Filter feed entries to those published within a date range.

    Args:
        entries: List of FeedEntry objects.
        since: Start of date range (inclusive). Timezone-aware.
        until: End of date range (inclusive). Timezone-aware.

    Returns:
        Filtered list of entries. Entries without a published date are excluded.
    """
    # Ensure since and until are timezone-aware for comparison
    if since.tzinfo is None:
        since = since.replace(tzinfo=timezone.utc)
    if until.tzinfo is None:
        until = until.replace(tzinfo=timezone.utc)

    filtered: list[FeedEntry] = []
    for entry in entries:
        if entry.published is None:
            continue
        pub = entry.published
        if pub.tzinfo is None:
            pub = pub.replace(tzinfo=timezone.utc)
        if since <= pub <= until:
            filtered.append(entry)

    return filtered


def filter_by_entities(
    entries: list[FeedEntry],
    entity_names: list[str],
) -> list[FeedEntry]:
    """Filter feed entries to those mentioning any of the given entity names.

    Searches title, summary, and tags (case-insensitive).

    Args:
        entries: List of FeedEntry objects.
        entity_names: Entity names or keywords to match.

    Returns:
        Filtered list of entries mentioning at least one entity.
    """
    if not entity_names:
        return entries

    # Build case-insensitive word-boundary patterns
    patterns = []
    for name in entity_names:
        escaped = re.escape(name)
        patterns.append(re.compile(rf"\b{escaped}\b", re.IGNORECASE))

    filtered: list[FeedEntry] = []
    for entry in entries:
        searchable = f"{entry.title} {entry.summary} {' '.join(entry.tags)}"
        if any(pat.search(searchable) for pat in patterns):
            filtered.append(entry)

    return filtered
