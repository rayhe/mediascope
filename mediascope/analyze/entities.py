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
        "regex": r"(?<!\w)(Meta(?!\s+(?:tag|data|description|charset|name|http|content|property|viewport))|Meta Platforms|Facebook|Instagram|WhatsApp|(?-i:Threads)|Mark Zuckerberg|Zuckerberg|Meta AI|Reality Labs|Oculus|Ray-Ban Meta|Ray-Ban|Oakley smart glasses|Andrew Bosworth|Bosworth|Boz|Chris Cox|Maher Saba|Meta Superintelligence Labs|Applied AI|Cambridge Analytica)(?!\w)",
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
    "Anthropic": {
        "aliases": [
            "Anthropic", "Dario Amodei", "Daniela Amodei", "Claude",
            "Mythos", "Project Glasswing",
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
            "WIRED", "Wired",
            "The Atlantic", "Atlantic",
            "MIT Technology Review",
            "Reuters", "Associated Press", "AP",
            "Bloomberg", "Financial Times",
            "TechCrunch", "The Verge", "Ars Technica",
            "The Information",
            "Business Insider", "404 Media",
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
    "Defense Tech": {
        "aliases": [
            "Anduril", "Anduril Industries", "Palmer Luckey", "Luckey",
            "Elbit Systems", "Elbit", "Rivet",
            "L3Harris", "Northrop Grumman", "Lockheed Martin",
            "Raytheon", "General Dynamics", "BAE Systems",
            "Shield AI", "Skydio",
        ],
    },
    "Policy Research": {
        "aliases": [
            "RAND Corporation", "RAND",
            "Brookings Institution", "Brookings",
            "Center for Strategic and International Studies", "CSIS",
            "Council on Foreign Relations", "CFR",
            "Carnegie Endowment",
        ],
    },
    "Political Figures": {
        "aliases": [
            "Donald Trump", "Trump",
            "Joe Biden", "Biden",
            "Kamala Harris",
        ],
        "regex": r"(?<!\w)(Donald Trump|Trump(?!\s+(?:Tower|Hotel|Organization|National|International))|Joe Biden|Biden|Kamala Harris)(?!\w)",
    },
    "Labor/Unions": {
        "aliases": [
            "United Tech and Allied Workers", "United Tech & Allied Workers",
            "Communication Workers Union", "CWU",
            "Alphabet Workers Union",
            "SEIU", "AFL-CIO",
            "unionize", "unionization", "labor union",
        ],
    },
    "TikTok": {
        "aliases": [
            "TikTok", "ByteDance", "Shou Zi Chew",
        ],
    },
    "Snap": {
        "aliases": [
            "Snap", "Snapchat", "Spectacles", "Evan Spiegel",
        ],
        "regex": r"(?<!\w)(Snap(?:chat)?|Spectacles|Evan Spiegel)(?!\w)",
    },
    "EssilorLuxottica": {
        "aliases": [
            "EssilorLuxottica", "Essilor", "Luxottica",
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
    the whole cluster.  The canonical name for each match is resolved at match
    time (see ``detect_entities``); the tuple stores the alias list so the
    closest alias can be found.

    Returns a list of (compiled_pattern, canonical_name_or_aliases, cluster_name)
    tuples.  For cluster-level regex patterns, canonical_name_or_aliases is the
    alias list (as a ``|``-joined string prefixed with ``__ALIASES__:``); for
    individual alias patterns, it is the alias string itself.
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
                # Store aliases for later canonical-name resolution
                aliases_tag = "__ALIASES__:" + "|".join(aliases)
                cluster_patterns.append((compiled, aliases_tag, cluster_name))
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


def _resolve_canonical(matched_text: str, aliases_tag: str) -> str:
    """Resolve the canonical name for a cluster-level regex match.

    When a cluster uses a custom regex, the matched text could be any
    entity in the cluster (e.g., "Andrew Bosworth" from the Meta cluster).
    This function finds the closest alias to use as the canonical name,
    preserving individual entity identity instead of collapsing everything
    to the first alias.

    Args:
        matched_text: The actual text matched by the regex.
        aliases_tag: The ``__ALIASES__:...`` string from ``_build_patterns``.

    Returns:
        The best canonical name — either an exact alias match or the
        matched text itself if no alias matches.
    """
    aliases_str = aliases_tag.removeprefix("__ALIASES__:")
    aliases = aliases_str.split("|")

    # Try exact match (case-insensitive) first
    matched_lower = matched_text.lower()
    for alias in aliases:
        if alias.lower() == matched_lower:
            return alias

    # Try substring containment — e.g., matched "Bosworth" is contained in
    # alias "Andrew Bosworth"
    for alias in aliases:
        if matched_lower in alias.lower() or alias.lower() in matched_lower:
            return alias

    # Fallback: return matched text as-is (preserves entity identity)
    return matched_text


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

            # Resolve canonical name for cluster-level regex matches
            resolved_canonical = canonical
            if canonical.startswith("__ALIASES__:"):
                resolved_canonical = _resolve_canonical(match.group(), canonical)

            mentions.append(
                EntityMention(
                    entity=match.group(),
                    canonical_name=resolved_canonical,
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
