"""Entity detection and clustering for media coverage analysis.

Identifies mentions of tech companies, executives, and products in article
text using configurable entity clusters with regex-based matching.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from typing import Any

logger = logging.getLogger(__name__)

# Default entity clusters: canonical name -> list of aliases/variants
DEFAULT_ENTITY_CLUSTERS: dict[str, list[str]] = {
    "Meta": [
        "Meta Platforms", "Facebook", "Instagram", "WhatsApp", "Threads",
        "Mark Zuckerberg", "Zuckerberg", "Meta AI", "Reality Labs", "Oculus",
        "Ray-Ban Meta",
    ],
    "Google": [
        "Alphabet", "Google", "YouTube", "DeepMind", "Waymo",
        "Sundar Pichai", "Gemini", "Google Cloud",
    ],
    "Apple": [
        "Apple", "iPhone", "iPad", "Tim Cook", "Apple Intelligence",
        "Apple Vision Pro", "Siri",
    ],
    "Amazon": [
        "Amazon", "AWS", "Alexa", "Jeff Bezos", "Andy Jassy",
        "Amazon Web Services", "Kindle", "Ring",
    ],
    "Microsoft": [
        "Microsoft", "Satya Nadella", "Azure", "Bing", "LinkedIn",
        "GitHub", "Copilot", "Xbox",
    ],
    "OpenAI": [
        "OpenAI", "Sam Altman", "ChatGPT", "GPT-4", "GPT-5",
        "DALL-E", "Sora",
    ],
    "X/Twitter": [
        "Twitter", "X Corp", "Elon Musk", "Musk", "SpaceX", "Tesla",
        "xAI", "Grok", "Starlink", "Neuralink",
    ],
    "Palantir": [
        "Palantir", "Alex Karp", "Peter Thiel", "Palantir Technologies",
    ],
}


@dataclass
class EntityMention:
    """A single entity mention detected in text."""

    entity: str          # The exact text matched
    canonical_name: str  # The canonical alias name (e.g., "Mark Zuckerberg")
    cluster: str         # The cluster this belongs to (e.g., "Meta")
    start: int           # Character offset start
    end: int             # Character offset end
    context: str = ""    # Surrounding sentence for context


def _build_patterns(
    clusters: dict[str, list[str]],
) -> list[tuple[re.Pattern, str, str]]:
    """Build compiled regex patterns from entity clusters.

    Returns a list of (compiled_pattern, canonical_name, cluster_name) tuples,
    sorted longest-first to prefer more specific matches.
    """
    entries: list[tuple[str, str, str]] = []
    for cluster_name, aliases in clusters.items():
        for alias in aliases:
            entries.append((alias, alias, cluster_name))

    # Sort by alias length descending so longer/more-specific patterns match first
    entries.sort(key=lambda x: len(x[0]), reverse=True)

    patterns: list[tuple[re.Pattern, str, str]] = []
    for alias, canonical, cluster in entries:
        escaped = re.escape(alias)
        # Word boundary matching — handle special chars at boundaries
        # Use lookahead/lookbehind for non-word chars at edges
        pattern = re.compile(
            rf"(?<!\w){escaped}(?!\w)",
            re.IGNORECASE,
        )
        patterns.append((pattern, canonical, cluster))

    return patterns


def _extract_sentence(text: str, start: int, end: int) -> str:
    """Extract the sentence containing the character range [start, end).

    Uses simple sentence boundary detection (period, question mark,
    exclamation mark followed by space or end of text).
    """
    # Find sentence start: search backwards for sentence boundary
    sent_start = 0
    for i in range(start - 1, -1, -1):
        if text[i] in ".!?" and (i + 1 >= len(text) or text[i + 1] in " \n\t"):
            sent_start = i + 1
            break

    # Find sentence end: search forwards for sentence boundary
    sent_end = len(text)
    for i in range(end, len(text)):
        if text[i] in ".!?" and (i + 1 >= len(text) or text[i + 1] in " \n\t"):
            sent_end = i + 1
            break

    return text[sent_start:sent_end].strip()


def detect_entities(
    text: str,
    clusters: dict[str, list[str]] | None = None,
) -> list[EntityMention]:
    """Detect entity mentions in text using cluster-based matching.

    Args:
        text: The article text to analyze.
        clusters: Entity clusters dict. If None, uses DEFAULT_ENTITY_CLUSTERS.

    Returns:
        List of EntityMention objects sorted by position in text.
    """
    if not text:
        return []

    if clusters is None:
        clusters = DEFAULT_ENTITY_CLUSTERS

    patterns = _build_patterns(clusters)
    mentions: list[EntityMention] = []
    # Track covered character spans to avoid overlapping matches
    covered: list[tuple[int, int]] = []

    for pattern, canonical, cluster in patterns:
        for match in pattern.finditer(text):
            start, end = match.start(), match.end()

            # Skip if this span overlaps with an already-matched (longer) span
            if any(
                not (end <= cov_start or start >= cov_end)
                for cov_start, cov_end in covered
            ):
                continue

            covered.append((start, end))
            context = _extract_sentence(text, start, end)

            mentions.append(
                EntityMention(
                    entity=match.group(),
                    canonical_name=canonical,
                    cluster=cluster,
                    start=start,
                    end=end,
                    context=context,
                )
            )

    # Sort by position in text
    mentions.sort(key=lambda m: m.start)
    return mentions


def get_primary_entity(mentions: list[EntityMention]) -> str:
    """Determine which entity cluster the article is primarily about.

    Based on mention count — the cluster with the most mentions is primary.

    Args:
        mentions: List of EntityMention objects from detect_entities().

    Returns:
        The cluster name with the most mentions, or empty string if no mentions.
    """
    if not mentions:
        return ""

    dist = get_entity_distribution(mentions)
    if not dist:
        return ""

    return max(dist, key=dist.get)


def get_entity_distribution(mentions: list[EntityMention]) -> dict[str, int]:
    """Count entity mentions per cluster.

    Args:
        mentions: List of EntityMention objects.

    Returns:
        Dict mapping cluster name to mention count, sorted by count descending.
    """
    counts: dict[str, int] = {}
    for mention in mentions:
        counts[mention.cluster] = counts.get(mention.cluster, 0) + 1

    # Sort by count descending
    return dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))


def load_clusters_from_yaml(path: str) -> dict[str, list[str]]:
    """Load custom entity clusters from a YAML file.

    Expected format:
        Meta:
          - Meta Platforms
          - Facebook
          - Instagram
        Google:
          - Alphabet
          - Google

    Args:
        path: Path to the YAML file.

    Returns:
        Dict mapping cluster name to list of aliases.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the YAML structure is invalid.
    """
    import yaml

    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not isinstance(data, dict):
        raise ValueError(f"Entity clusters YAML must be a mapping, got {type(data).__name__}")

    clusters: dict[str, list[str]] = {}
    for cluster_name, aliases in data.items():
        if not isinstance(aliases, list):
            logger.warning(
                "Skipping cluster %s: expected list, got %s",
                cluster_name,
                type(aliases).__name__,
            )
            continue
        clusters[str(cluster_name)] = [str(a) for a in aliases]

    return clusters


def merge_clusters(
    base: dict[str, list[str]],
    override: dict[str, list[str]],
) -> dict[str, list[str]]:
    """Merge two cluster dicts, with override adding to/replacing base entries.

    Args:
        base: The base clusters (e.g., DEFAULT_ENTITY_CLUSTERS).
        override: Additional or replacement clusters.

    Returns:
        Merged cluster dict. Override clusters replace base clusters of the
        same name entirely.
    """
    merged = dict(base)
    for cluster_name, aliases in override.items():
        merged[cluster_name] = aliases
    return merged
