"""Entity detection and clustering for media coverage analysis.

Identifies mentions of tech companies, executives, and products in article
text using configurable entity clusters with regex-based matching.

Entity clusters can be specified in two formats:

1. **Dict format** (documented API, used in YAML profiles)::

       {"Meta": {"aliases": ["Meta", "Facebook", ...], "regex": r"\\b(Meta|Facebook)\\b"}}

   The ``regex`` key is optional; if omitted, a word-boundary pattern is
   auto-generated from the alias list.

2. **List format** (shorthand)::

       {"Meta": ["Meta", "Facebook", ...]}

   Automatically wrapped into the dict format internally.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from typing import Any, Union

logger = logging.getLogger(__name__)

# Type alias — clusters accept either format; code normalizes to dict format.
ClusterEntry = Union[dict[str, Any], list[str]]
ClusterDict = dict[str, ClusterEntry]

# Default entity clusters: canonical name -> {aliases, regex?}
DEFAULT_ENTITY_CLUSTERS: ClusterDict = {
    "Meta": {
        "aliases": [
            "Meta", "Meta Platforms", "Facebook", "Instagram", "WhatsApp",
            "Threads", "Mark Zuckerberg", "Zuckerberg", "Meta AI",
            "Reality Labs", "Oculus", "Ray-Ban Meta", "Ray-Ban",
            "Oakley smart glasses", "Andrew Bosworth", "Bosworth", "Boz",
            "Meta's smart glasses", "Meta's Ray-Ban",
            "Chris Cox", "Maher Saba", "Meta Superintelligence Labs",
            "Applied AI", "Cambridge Analytica",
        ],
        "regex": r"(?<!\w)(Meta(?!\s+(?:tag|data|description|charset|name|http|content|property|viewport))|Meta Platforms|Facebook|Instagram|WhatsApp|Threads|Mark Zuckerberg|Zuckerberg|Meta AI|Reality Labs|Oculus|Ray-Ban Meta|Ray-Ban|Oakley smart glasses|Andrew Bosworth|Bosworth|Boz|Chris Cox|Maher Saba|Meta Superintelligence Labs|Applied AI|Cambridge Analytica)(?!\w)",
    },
    "Google": {
        "aliases": [
            "Alphabet", "Google", "YouTube", "DeepMind", "Waymo",
            "Sundar Pichai", "Gemini", "Google Cloud", "Android",
        ],
        "regex": r"(?<!\w)(Alphabet|Google(?!\s+(?:Sheet|Doc|Drive|Form|Search))|YouTube|DeepMind|Waymo|Sundar Pichai|Gemini|Google Cloud|Android)(?!\w)",
    },
    "Apple": {
        "aliases": [
            "Apple", "iPhone", "iPad", "Tim Cook", "John Ternus",
            "Apple Intelligence", "Apple Vision Pro", "Siri", "macOS",
            "AirPods", "Apple Watch",
        ],
        "regex": r"(?<!\w)(Apple(?!\s+(?:pie|cider|sauce|tree|juice|cinnamon))|iPhone|iPad|Tim Cook|John Ternus|Apple Intelligence|Apple Vision Pro|Siri|macOS|AirPods|Apple Watch)(?!\w)",
    },
    "Amazon": {
        "aliases": [
            "Amazon", "AWS", "Alexa", "Jeff Bezos", "Andy Jassy",
            "Amazon Web Services", "Kindle", "Ring", "Prime Video",
        ],
        "regex": r"(?<!\w)(Amazon(?!\s+(?:rain|forest|river|basin))|AWS|Alexa|Jeff Bezos|Andy Jassy|Amazon Web Services|Kindle|Ring|Prime Video)(?!\w)",
    },
    "Microsoft": {
        "aliases": [
            "Microsoft", "Satya Nadella", "Azure", "Bing", "LinkedIn",
            "GitHub", "Copilot", "Xbox", "Windows",
        ],
    },
    "OpenAI": {
        "aliases": [
            "OpenAI", "Sam Altman", "ChatGPT", "GPT-4", "GPT-5",
            "DALL-E", "Sora", "GPT-4o",
        ],
    },
    "X/Twitter": {
        "aliases": [
            "Twitter", "X Corp", "Elon Musk", "Musk", "SpaceX", "Tesla",
            "xAI", "Grok", "Starlink", "Neuralink",
        ],
    },
    "Palantir": {
        "aliases": [
            "Palantir", "Alex Karp", "Peter Thiel", "Palantir Technologies",
        ],
    },
    "US Government": {
        "aliases": [
            "Pentagon", "Department of Defense", "FBI", "CIA",
            "NSA", "US Marshals Service", "US Special Operations Command",
            "Naval Criminal Investigative Service", "NCIS",
            "Commerce Department", "FTC",
        ],
    },
    "Surveillance/Biometrics": {
        "aliases": [
            "Rank One Computing", "Rank One", "Clearview AI", "Clearview",
            "NEC", "Cognitec", "Idemia", "Palantir Technologies",
        ],
    },
    "Privacy/Civil Liberties Orgs": {
        "aliases": [
            "Electronic Frontier Foundation", "EFF",
            "ACLU", "American Civil Liberties Union",
            "Access Now", "Fight for the Future",
            "Electronic Privacy Information Center", "EPIC",
        ],
    },
    "Media/Publications": {
        "aliases": [
            "The New York Times", "New York Times", "NYT",
            "The Washington Post", "Washington Post",
            "The Guardian", "Guardian",
            "Reuters", "Associated Press", "AP",
            "Bloomberg", "Financial Times",
            "TechCrunch", "The Verge", "Ars Technica",
            "The Information",
        ],
    },
    "Whistleblowers/Critics": {
        "aliases": [
            "Sarah Wynn-Williams", "Wynn-Williams",
            "Frances Haugen", "Haugen",
            "Sophie Zhang",
            "Christopher Wylie", "Wylie",
            "Carole Cadwalladr", "Cadwalladr",
            "Tim Wu",
        ],
    },
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


def _normalize_cluster(entry: ClusterEntry) -> dict[str, Any]:
    """Normalize a cluster entry to the dict format ``{aliases: [...], regex?: str}``.

    Accepts either a plain list of aliases (shorthand) or the full dict format.
    """
    if isinstance(entry, list):
        return {"aliases": entry}
    if isinstance(entry, dict):
        # Already in dict format — ensure "aliases" key exists
        if "aliases" not in entry:
            logger.warning("Cluster dict missing 'aliases' key: %s", list(entry.keys()))
            return {"aliases": []}
        return entry
    raise TypeError(f"Cluster entry must be a list or dict, got {type(entry).__name__}")


def _build_patterns(
    clusters: ClusterDict,
) -> list[tuple[re.Pattern, str, str]]:
    """Build compiled regex patterns from entity clusters.

    Handles both formats:
    - Dict format: ``{aliases: [...], regex?: "..."}``
    - List format: ``["alias1", "alias2", ...]``

    When a cluster provides a ``regex`` key, that pattern is compiled once for
    the whole cluster.  Otherwise, individual alias patterns are built with
    word-boundary matching (longest-first).

    Returns a list of (compiled_pattern, canonical_name, cluster_name) tuples.
    """
    # Phase 1: clusters that supply their own regex — one pattern per cluster
    cluster_patterns: list[tuple[re.Pattern, str, str]] = []
    # Phase 2: individual alias patterns for clusters without custom regex
    alias_entries: list[tuple[str, str, str]] = []

    for cluster_name, raw_entry in clusters.items():
        entry = _normalize_cluster(raw_entry)
        aliases: list[str] = entry.get("aliases", [])
        custom_regex: str | None = entry.get("regex")

        if custom_regex:
            try:
                compiled = re.compile(custom_regex, re.IGNORECASE)
                # Use the first alias as the canonical name for cluster-level regex
                canonical = aliases[0] if aliases else cluster_name
                cluster_patterns.append((compiled, canonical, cluster_name))
            except re.error as exc:
                logger.warning(
                    "Invalid regex for cluster %s, falling back to alias matching: %s",
                    cluster_name,
                    exc,
                )
                # Fall through to alias-based matching
                for alias in aliases:
                    alias_entries.append((alias, alias, cluster_name))
        else:
            for alias in aliases:
                alias_entries.append((alias, alias, cluster_name))

    # Sort alias entries by length descending so longer/more-specific patterns match first
    alias_entries.sort(key=lambda x: len(x[0]), reverse=True)

    alias_patterns: list[tuple[re.Pattern, str, str]] = []
    for alias, canonical, cluster in alias_entries:
        escaped = re.escape(alias)
        # Replace escaped literal spaces with \s+ to handle line breaks and
        # multiple whitespace in article text (e.g. "The New York\nTimes")
        escaped = re.sub(r"\\ ", r"\\s+", escaped)
        pattern = re.compile(
            rf"(?<!\w){escaped}(?!\w)",
            re.IGNORECASE,
        )
        alias_patterns.append((pattern, canonical, cluster))

    # Cluster-level patterns first (they tend to be more precise), then alias patterns
    return cluster_patterns + alias_patterns


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
    clusters: ClusterDict | None = None,
) -> list[EntityMention]:
    """Detect entity mentions in text using cluster-based matching.

    Args:
        text: The article text to analyze.
        clusters: Entity clusters dict (dict or list format). If None, uses
            DEFAULT_ENTITY_CLUSTERS.

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


def get_primary_entity(mentions: list[EntityMention]) -> str | None:
    """Determine which entity cluster the article is primarily about.

    Based on mention count — the cluster with the most mentions is primary.

    Args:
        mentions: List of EntityMention objects from detect_entities().

    Returns:
        The cluster name with the most mentions, or None if no mentions.
    """
    if not mentions:
        return None

    dist = get_entity_distribution(mentions)
    if not dist:
        return None

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


def load_clusters_from_yaml(path: str) -> ClusterDict:
    """Load custom entity clusters from a YAML file.

    Supports both formats::

        # Dict format (recommended)
        Meta:
          aliases:
            - Meta Platforms
            - Facebook
          regex: "\\\\b(Meta|Facebook)\\\\b"

        # List format (shorthand)
        Google:
          - Alphabet
          - Google

    Args:
        path: Path to the YAML file.

    Returns:
        Dict mapping cluster name to cluster entry.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the YAML structure is invalid.
    """
    import yaml

    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not isinstance(data, dict):
        raise ValueError(f"Entity clusters YAML must be a mapping, got {type(data).__name__}")

    clusters: ClusterDict = {}
    for cluster_name, entry in data.items():
        if isinstance(entry, list):
            clusters[str(cluster_name)] = [str(a) for a in entry]
        elif isinstance(entry, dict):
            clusters[str(cluster_name)] = entry
        else:
            logger.warning(
                "Skipping cluster %s: expected list or dict, got %s",
                cluster_name,
                type(entry).__name__,
            )

    return clusters


def merge_clusters(
    base: ClusterDict,
    override: ClusterDict,
) -> ClusterDict:
    """Merge two cluster dicts, with override adding to/replacing base entries.

    Args:
        base: The base clusters (e.g., DEFAULT_ENTITY_CLUSTERS).
        override: Additional or replacement clusters.

    Returns:
        Merged cluster dict. Override clusters replace base clusters of the
        same name entirely.
    """
    merged = dict(base)
    for cluster_name, entry in override.items():
        merged[cluster_name] = entry
    return merged
