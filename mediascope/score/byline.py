"""Per-journalist tracking and asymmetry ranking.

Builds journalist profiles from analyzed articles and ranks them by
how asymmetrically they cover a target entity relative to peers.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from typing import Optional

import numpy as np


@dataclass
class JournalistProfile:
    """Aggregated coverage profile for a single journalist."""

    name: str
    publication: str
    article_count: int = 0
    avg_tone_by_entity: dict[str, float] = field(default_factory=dict)
    primary_topics: list[str] = field(default_factory=list)
    anonymous_source_avg: float = 0.0
    speculative_language_avg: float = 0.0
    framing_devices_freq: dict[str, int] = field(default_factory=dict)


def build_journalist_profiles(articles: list[dict]) -> dict[str, JournalistProfile]:
    """Build journalist profiles from a list of analyzed articles.

    Each article dict is expected to have:
        - "author" (str): journalist name / byline
        - "publication" or "publication_slug" (str)
        - "entities" (list[str]): entities mentioned
        - "sentiment" (dict): at minimum {"overall_tone": float}
        - "anonymous_source_ratio" (float, optional)
        - "speculative_language_ratio" (float, optional)
        - "framing_devices" (list[str], optional)
        - "topics" (list[str], optional)

    Returns:
        Mapping of journalist name → JournalistProfile.
    """
    # Accumulators
    tone_accum: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    anon_accum: dict[str, list[float]] = defaultdict(list)
    spec_accum: dict[str, list[float]] = defaultdict(list)
    frame_accum: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    topic_accum: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    pub_map: dict[str, str] = {}
    count_map: dict[str, int] = defaultdict(int)

    for article in articles:
        author = article.get("author")
        if not author or not isinstance(author, str):
            continue
        author = author.strip()
        if not author:
            continue

        pub = article.get("publication") or article.get("publication_slug", "unknown")
        pub_map[author] = pub
        count_map[author] += 1

        # Sentiment per entity
        tone = article.get("sentiment", {}).get("overall_tone")
        if tone is not None:
            for entity in article.get("entities", []):
                tone_accum[author][entity.lower()].append(float(tone))

        # Anonymous source ratio
        anon = article.get("anonymous_source_ratio")
        if anon is not None:
            anon_accum[author].append(float(anon))

        # Speculative language ratio
        spec = article.get("speculative_language_ratio")
        if spec is not None:
            spec_accum[author].append(float(spec))

        # Framing devices
        for device in article.get("framing_devices", []):
            frame_accum[author][device] += 1

        # Topics
        for topic in article.get("topics", []):
            topic_accum[author][topic] += 1

    # Build profiles
    profiles: dict[str, JournalistProfile] = {}
    all_authors = set(count_map.keys())

    for author in all_authors:
        # Average tone per entity
        avg_tone: dict[str, float] = {}
        for entity, tones in tone_accum[author].items():
            avg_tone[entity] = float(np.mean(tones))

        # Primary topics (top 5 by frequency)
        sorted_topics = sorted(topic_accum[author].items(), key=lambda x: x[1], reverse=True)
        primary_topics = [t for t, _ in sorted_topics[:5]]

        profiles[author] = JournalistProfile(
            name=author,
            publication=pub_map.get(author, "unknown"),
            article_count=count_map[author],
            avg_tone_by_entity=avg_tone,
            primary_topics=primary_topics,
            anonymous_source_avg=(
                float(np.mean(anon_accum[author])) if anon_accum[author] else 0.0
            ),
            speculative_language_avg=(
                float(np.mean(spec_accum[author])) if spec_accum[author] else 0.0
            ),
            framing_devices_freq=dict(frame_accum[author]),
        )

    return profiles


def rank_by_asymmetry(
    profiles: dict[str, JournalistProfile],
    target_entity: str,
) -> list[tuple[str, float]]:
    """Rank journalists by how much more negative they are toward the target entity vs peers.

    For each journalist, computes:
        asymmetry = avg_tone(target) - mean(avg_tone(all other entities))

    A more negative asymmetry means the journalist is disproportionately
    negative toward the target compared to other entities they cover.

    Args:
        profiles: Journalist profiles from build_journalist_profiles().
        target_entity: Entity to measure asymmetry for.

    Returns:
        List of (journalist_name, asymmetry_score), sorted from most negative
        (most asymmetric against target) to most positive.
    """
    target_lower = target_entity.lower()
    results: list[tuple[str, float]] = []

    for name, profile in profiles.items():
        if target_lower not in profile.avg_tone_by_entity:
            continue  # journalist hasn't written about the target

        target_tone = profile.avg_tone_by_entity[target_lower]

        # Compute average tone across all other entities
        peer_tones = [
            tone
            for entity, tone in profile.avg_tone_by_entity.items()
            if entity != target_lower
        ]

        if not peer_tones:
            # No peer coverage — can't compute asymmetry
            continue

        peer_avg = float(np.mean(peer_tones))
        asymmetry = target_tone - peer_avg
        results.append((name, asymmetry))

    # Sort most negative first
    results.sort(key=lambda x: x[1])
    return results
