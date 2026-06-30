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
            "Model Capability Initiative", "MCI",
            "Agent Transformation Accelerator", "ATA",
            "Stephane Kasriel", "Kasriel",
            "Tracy Clayton", "Dave Arnold", "Andy Stone",
            "NameTag",
            "Alex Himel", "Himel",
            "Ankit Brahmbhatt", "Brahmbhatt",
            "Will Cathcart", "Cathcart",
            "Peter Bristol", "Bristol",
            "Muse Spark",
            "Meta Fury", "Fury",
            "Adventurer", "Starfire",
            "Meta Ray-Ban Display",
            "Llama 4",
            "Joel Kaplan", "Kaplan",
            "Sheryl Sandberg", "Sandberg",
            "Nick Clegg", "Clegg",
            "Dina Powell McCormick",
            "Arena", "Francis Brennan", "Alexandr Wang",
            "Scale AI",
            "Virtue AI", "Bo Li", "Dawn Song", "Sanmi Koyejo",
            "FAIR", "Fundamental AI Research",
            "Ime Archibong", "Archibong",
            "the social media giant", "the social media company",
        ],
        "regex": r"(?<!\w)(Meta(?!\s+(?:tag|data|description|charset|name|http|content|property|viewport))|Meta Platforms|Facebook|Instagram|WhatsApp|(?-i:Threads)|Mark Zuckerberg|Zuckerberg|Meta AI|Reality Labs|Oculus|Ray-Ban Meta|Ray-Ban|Oakley smart glasses|Andrew Bosworth|Bosworth|Boz|Chris Cox|Maher Saba|Meta Superintelligence Labs|Applied AI|Cambridge Analytica|Model Capability Initiative|(?-i:MCI)|Agent Transformation Accelerator|(?-i:ATA)|Stephane Kasriel|Kasriel|Tracy Clayton|Dave Arnold|Andy Stone|NameTag|Alex Himel|Himel|Ankit Brahmbhatt|Brahmbhatt|Will Cathcart|Cathcart|Peter Bristol|Bristol|Muse Spark|Meta Fury|(?-i:Fury)(?=\s+(?:glasses|are|is|was|cost|have|included|and|AI|smart))|Adventurer|Starfire|Meta Ray-Ban Display|Llama 4|Joel Kaplan|Kaplan|Sheryl Sandberg|Sandberg|Nick Clegg|Clegg|Dina Powell McCormick|(?-i:Arena)(?=\s+(?:app|prediction|market|is|was|would|will|being|the))|Francis Brennan|Alexandr Wang|Scale AI|Virtue AI|Bo Li|Dawn Song|Sanmi Koyejo|Fundamental AI Research|(?-i:FAIR)(?=\s+(?:Lab|lab|research|team|group))|Ime Archibong|Archibong|the social media (?:giant|company))(?!\w)",
    },
    "Google": {
        "aliases": [
            "Alphabet", "Google", "YouTube", "DeepMind", "Waymo",
            "Sundar Pichai", "Gemini", "Google Cloud", "Android",
            "AlphaFold",
            "the search giant",
        ],
        "regex": r"(?<!\w)(Alphabet|Google(?!\s+(?:Sheet|Doc|Drive|Form|Search))|YouTube|DeepMind|Waymo|Sundar Pichai|Gemini|Google Cloud|Android|AlphaFold|the search giant)(?!\w)",
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
            "DALL-E", "Sora", "GPT-4o", "Stargate", "Sora 2",
        ],
    },
    "X/Twitter": {
        "aliases": [
            "Twitter", "X Corp", "Elon Musk", "Musk",
        ],
        "regex": r"(?<!\w)(Twitter(?!-(?:like|esque|style|inspired))|X Corp|Elon Musk(?!'s xAI)|(?<!Elon\s)Musk(?!\s+(?:Ox|ox|melon|deer)))(?!\w)",
    },
    "xAI": {
        "aliases": [
            "xAI", "Grok", "Colossus", "Colossus II",
        ],
        "regex": r"(?<!\w)(xAI|Grok(?!\s+(?:the|TV|Network))|Colossus(?:\s+II)?)(?!\w)",
    },
    "Tesla/SpaceX": {
        "aliases": [
            "Tesla", "SpaceX", "Starlink", "Neuralink",
        ],
        "regex": r"(?<!\w)(Tesla(?!\s+(?:coil|tower|valve))|SpaceX|Starlink|Neuralink)(?!\w)",
    },
    "Nvidia": {
        "aliases": [
            "Nvidia", "NVIDIA", "Jensen Huang", "CUDA", "H100", "H200",
            "A100", "B200", "GB200", "DGX", "GeForce", "Omniverse",
            "Isaac Sim", "NVLink",
        ],
        "regex": r"(?<!\w)((?-i:NVIDIA)|Nvidia|Jensen Huang|(?-i:CUDA)|(?-i:H100|H200|A100|B200|GB200|DGX)|GeForce|Omniverse|Isaac Sim|NVLink)(?!\w)",
    },
    "CoreWeave": {
        "aliases": [
            "CoreWeave", "Mike Intrator",
        ],
        "regex": r"(?<!\w)(CoreWeave|Mike Intrator)(?!\w)",
    },
    "Palantir": {
        "aliases": [
            "Palantir", "Alex Karp", "Peter Thiel", "Palantir Technologies",
        ],
    },
    "Anthropic": {
        "aliases": [
            "Anthropic", "Dario Amodei", "Daniela Amodei", "Claude",
            "Mythos", "Fable", "Project Glasswing", "Amanda Askell",
        ],
    },
    "IBM": {
        "aliases": [
            "IBM", "Deep Blue", "Watson", "Red Hat",
        ],
        "regex": r"(?<!\w)((?-i:IBM)|Deep Blue|Watson|Red Hat)(?!\w)",
    },
    "Uber": {
        "aliases": [
            "Uber", "Uber Technologies", "Dara Khosrowshahi",
        ],
        "regex": r"(?<!\w)(Uber(?!\s+Eats)|Uber Technologies|Dara Khosrowshahi)(?!\w)",
    },
    "Duolingo": {
        "aliases": [
            "Duolingo", "Luis von Ahn",
        ],
        "regex": r"(?<!\w)(Duolingo|Luis von Ahn)(?!\w)",
    },
    "US Government": {
        "aliases": [
            "Pentagon", "Department of Defense", "FBI", "CIA",
            "NSA", "National Security Agency",
            "US Marshals Service", "US Special Operations Command",
            "Naval Criminal Investigative Service", "NCIS",
            "Commerce Department", "FTC",
            "ICE", "Immigration and Customs Enforcement",
            "Drug Enforcement Administration", "DEA",
            "Department of Government Efficiency", "DOGE",
            "Internal Revenue Service", "IRS",
            "Centers for Medicare & Medicaid Services", "CMS",
            "Edward Snowden", "Snowden",
            "Bureau of Alcohol Tobacco Firearms", "ATF",
            "Securities and Exchange Commission", "SEC",
            "Justice Department", "Department of Justice", "DOJ",
            "Bureau of Industry and Security", "BIS",
            "Center for AI Standards and Innovation", "CAISI",
            "Howard Lutnick",
            "US Army", "the Army", "Army",
            "US Navy", "US Marine Corps", "US Air Force",
            "US Special Operations Command",
            "White House",
        ],
        "regex": r"(?<!\w)(Pentagon|Department of Defense|FBI|CIA"
                 r"|NSA|National Security Agency"
                 r"|US Marshals Service|US Special Operations Command"
                 r"|Naval Criminal Investigative Service|(?-i:NCIS)"
                 r"|Commerce Department|(?-i:FTC)"
                 r"|(?-i:ICE)|Immigration and Customs Enforcement"
                 r"|Drug Enforcement Administration|(?-i:DEA)"
                 r"|Department of Government Efficiency|(?-i:DOGE)"
                 r"|Internal Revenue Service|(?-i:IRS)"
                 r"|Centers for Medicare & Medicaid Services|(?-i:CMS)"
                 r"|Edward Snowden|Snowden"
                 r"|Bureau of Alcohol Tobacco Firearms|(?-i:ATF)"
                 r"|Bureau of Industry and Security|(?-i:BIS)"
                 r"|Center for AI Standards and Innovation|(?-i:CAISI)"
                 r"|Howard Lutnick"
                 r"|Securities and Exchange Commission|(?-i:SEC)"
                 r"|Justice Department|Department of Justice|(?-i:DOJ)"
                 r"|(?:US |U\.S\. |the )Army"
                 r"|(?:US |U\.S\. )(?:Navy|Marine Corps|Air Force)"
                 r"|White House)(?!\w)",
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
            "NOYB", "Irish Council for Civil Liberties", "ICCL",
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
            "Gizmodo",
            "The New Yorker", "New Yorker",
            "Fast Company",
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
            "Quay Barnett", "Barnett",
            "Lattice", "EagleEye",
            "SBMC", "Soldier Born Mission Command",
        ],
    },
    "Policy Research": {
        "aliases": [
            "RAND Corporation", "RAND",
            "Brookings Institution", "Brookings",
            "Center for Strategic and International Studies", "CSIS",
            "Council on Foreign Relations", "CFR",
            "Carnegie Endowment",
            "Pew Research Center", "Pew Research",
            "Graphite",
            "Jonathan Wong",
        ],
    },
    "Political Figures": {
        "aliases": [
            "Donald Trump", "Trump",
            "Joe Biden", "Biden",
            "Kamala Harris",
            "J.D. Vance", "Vance",
        ],
        "regex": r"(?<!\w)(Donald Trump|Trump(?!\s+(?:Tower|Hotel|Organization|National|International))|Joe Biden|Biden|Kamala Harris|J\.?\s*D\.?\s+Vance|Vance)(?!\w)",
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
    "Chinese AI": {
        "aliases": [
            "Zhipu", "Z.ai", "GLM", "DeepSeek", "Baidu", "Alibaba Cloud",
            "Qwen", "Yi", "01.AI", "Moonshot AI", "Kimi",
            "SenseTime", "iFLYTEK",
        ],
    },
    "OpenClaw": {
        "aliases": [
            "OpenClaw", "Hatch",
        ],
        "regex": r"(?<!\w)(OpenClaw|(?-i:Hatch)(?=\s+(?:agent|AI|platform|app|tool|agents)))(?!\w)",
    },
    "Chinese Tech Platforms": {
        "aliases": [
            "Lark", "DingTalk", "Rednote", "Xiaohongshu",
            "WeChat", "Weibo", "Taobao", "Alipay",
            "Tencent", "Alibaba",
        ],
        "regex": r"(?<!\w)((?-i:Lark|DingTalk|Rednote|Xiaohongshu|WeChat|Weibo|Taobao|Alipay)|Tencent|Alibaba(?!\s+Cloud))(?!\w)",
    },
    "Spotify": {
        "aliases": [
            "Spotify", "Daniel Ek",
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
            "Francesco Milleri", "Milleri",
            "LensCrafters",
        ],
    },
    "Garmin": {
        "aliases": [
            "Garmin",
        ],
    },
    "EU Regulatory": {
        "aliases": [
            "GDPR", "General Data Protection Regulation",
            "DPC", "Data Protection Commission",
            "European Commission", "EU Commission",
        ],
    },
    "Data/Intelligence Industry": {
        "aliases": [
            "ShadowDragon", "Babel Street", "LexisNexis",
            "Thomson Reuters CLEAR", "Voyager Labs", "Dataminr",
            "Recorded Future", "Cellebrite", "NSO Group",
            "Pegasus", "S2 Global", "Pen-Link",
        ],
    },
    "VR/Metaverse": {
        "aliases": [
            "Horizon Worlds", "Horizon", "Quest", "Meta Quest",
            "Quest 3S", "Quest 3", "Quest Pro",
            "VRChat", "metaverse",
            "Reality Labs",
        ],
        "regex": r"(?<!\w)(Horizon Worlds|Horizon(?:\s+(?:Spaces|Central|Unity))|"
                 r"(?:Meta\s+)?(?-i:Quest)(?:\s+(?:3S?|Pro))?|VRChat|metaverse|Reality Labs)(?!\w)",
    },
    "Smart Glasses Competitors": {
        "aliases": [
            "Gentle Monster",
            "XREAL", "Even Realities",
            "Halo", "Solos",
            "Brilliant Labs",
        ],
        "regex": r"(?<!\w)(Gentle Monster|(?-i:XREAL)|Even Realities|(?-i:Halo)|Solos|Brilliant Labs)(?!\w)",
    },
    "VC/Tech Investors": {
        "aliases": [
            "Marc Andreessen", "Andreessen",
            "Andreessen Horowitz", "a16z",
            "Sequoia Capital", "Sequoia",
            "Benchmark", "Kleiner Perkins",
            "Y Combinator", "YC",
        ],
        "regex": r"(?<!\w)(Marc Andreessen|Andreessen(?!\s+Horowitz)|Andreessen Horowitz|(?-i:a16z)|Sequoia(?:\s+Capital)?|Benchmark|Kleiner Perkins|Y Combinator|(?-i:YC))(?!\w)",
    },
    "Celebrity/Influencer": {
        "aliases": [
            "Kylie Jenner", "Jenner",
        ],
        "regex": r"(?<!\w)(Kylie Jenner|Jenner(?:'s)?)(?!\w)",
    },
    "Indian Fintech": {
        "aliases": [
            "CRED", "Kunal Shah",
            "PhonePe", "UPI",
        ],
        "regex": r"(?<!\w)((?-i:CRED)|Kunal Shah|PhonePe|(?-i:UPI))(?!\w)",
    },
    "Prediction Markets/Fintech": {
        "aliases": [
            "Polymarket", "Kalshi", "Robinhood", "Interactive Brokers",
            "PredictIt", "Metaculus", "Manifold Markets",
            "CFTC", "Commodity Futures Trading Commission",
            "event contracts", "prediction market",
            "Coatue", "Tarun Chitra",
        ],
        "regex": r"(?<!\w)(Polymarket|Kalshi|Robinhood|Interactive Brokers"
                 r"|PredictIt|Metaculus|Manifold Markets"
                 r"|(?-i:CFTC)|Commodity Futures Trading Commission"
                 r"|event contracts|prediction market"
                 r"|Coatue|Tarun Chitra)(?!\w)",
    },
    "Insurance/Litigation Finance": {
        "aliases": [
            "The Hartford", "Hartford", "Chubb", "ACE American",
            "Flashlight Capital", "Innsworth Capital", "Burford Capital",
            "Marsh", "AIG", "Zurich Insurance", "Lloyd's",
            "Reed Smith", "Calfee Halter",
        ],
        "regex": r"(?<!\w)(The Hartford|Hartford Insurance|Chubb"
                 r"|ACE American|Flashlight Capital|Innsworth Capital"
                 r"|Burford Capital|Reed Smith|Calfee,?\s*Halter"
                 r"|litigation fund(?:ing|er)|third.?party fund(?:ing|er))(?!\w)",
    },
    "Legal/Judicial": {
        "aliases": [
            "Delaware Superior Court", "Delaware Supreme Court",
            "Section 230", "Communications Decency Act",
            "Digital Services Act", "DSA",
        ],
        "regex": r"(?<!\w)(Delaware (?:Superior|Supreme) Court"
                 r"|Section 230|Communications Decency Act"
                 r"|Digital Services Act|(?-i:DSA)"
                 r"|(?-i:MDL)\s*\d+"
                 r"|bellwether (?:trial|verdict|case))(?!\w)",
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
            rf"(?<!\w){escaped}(?![\w]|-(?:like|esque|style|inspired|adjacent)\b)",
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
