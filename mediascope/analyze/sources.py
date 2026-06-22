"""Source authority analysis for media coverage.

Extracts and grades source citations in article text, distinguishing
between named/anonymous sources and neutral/loaded attribution verbs.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)

# Attribution verb classifications
NEUTRAL_VERBS: set[str] = {
    "said", "told", "noted", "explained", "stated",
    "added", "commented", "remarked", "observed", "reported",
    "confirmed", "acknowledged", "responded", "replied",
    "mentioned", "indicated", "described", "recalled",
}

LOADED_VERBS: set[str] = {
    "claimed", "argued", "warned", "insisted", "admitted",
    "conceded", "denied", "blasted", "slammed", "demanded",
    "charged", "accused", "alleged", "suggested", "hinted",
    "boasted", "bragged", "complained", "fumed", "lamented",
    "ranted", "scoffed", "sneered", "vowed", "threatened",
    "confessed", "revealed", "declared", "proclaimed",
}

ALL_VERBS: set[str] = NEUTRAL_VERBS | LOADED_VERBS

# Expert title indicators
EXPERT_TITLES: list[str] = [
    "professor", "prof.", "dr.", "doctor", "researcher",
    "scientist", "analyst", "economist", "attorney", "lawyer",
    "director", "chairman", "chairwoman", "chair",
    "president", "vice president", "vp",
    "chief executive", "ceo", "cto", "cfo", "coo",
    "secretary", "minister", "commissioner",
    "spokesperson", "spokesman", "spokeswoman",
    "expert", "specialist", "consultant", "fellow",
    "scholar", "academic", "strategist", "adviser", "advisor",
]

# Anonymous source indicators
ANONYMOUS_INDICATORS: list[str] = [
    "sources", "people familiar", "a person",
    "insiders", "someone close", "people briefed",
    "officials who", "employees who", "individuals who",
    "people who requested anonymity",
    "spoke on condition of anonymity",
    "asked not to be identified",
    "asked not to be named",
    "who declined to be identified",
    "who spoke anonymously",
    "granted anonymity",
]


@dataclass
class SourceMention:
    """A source citation extracted from article text."""

    name: str                   # Source name or descriptor
    is_anonymous: bool = False  # Whether the source is anonymous
    is_expert: bool = False     # Whether the source has expert credentials
    affiliation: str = ""       # Organization or affiliation if detected
    quote: str = ""             # The quoted text, if any
    attribution_verb: str = ""  # The verb used for attribution


def _is_anonymous_descriptor(text: str) -> bool:
    """Check if a source descriptor indicates an anonymous source."""
    text_lower = text.lower()
    return any(ind in text_lower for ind in ANONYMOUS_INDICATORS)


def _is_expert_by_title(text: str) -> bool:
    """Check if a source description includes expert-level titles."""
    text_lower = text.lower()
    return any(title in text_lower for title in EXPERT_TITLES)


def _extract_affiliation(context: str) -> str:
    """Try to extract an organizational affiliation from surrounding context.

    Looks for patterns like "of [Organization]", "at [Organization]",
    "from [Organization]", "[Organization]'s".
    """
    patterns = [
        re.compile(r"\b(?:of|at|from|with)\s+(?:the\s+)?([A-Z][A-Za-z\s&]+?)(?:[,.]|\s+(?:said|told|who))", re.DOTALL),
        re.compile(r"([A-Z][A-Za-z\s&]+?)(?:'s|'s)\s+(?:CEO|president|director|chief|head|spokesperson)", re.DOTALL),
    ]
    for pat in patterns:
        m = pat.search(context)
        if m:
            aff = m.group(1).strip()
            # Filter out generic words
            if len(aff) > 2 and aff not in {"The", "A", "An", "This", "That"}:
                return aff
    return ""


def _find_attribution_verb(context: str) -> str:
    """Find the attribution verb in a context string."""
    context_lower = context.lower()
    # Search for attribution verbs near quotes or source names
    for verb in sorted(ALL_VERBS, key=len, reverse=True):
        pattern = re.compile(rf"\b{re.escape(verb)}\b", re.IGNORECASE)
        if pattern.search(context_lower):
            return verb
    return ""


def extract_sources(text: str) -> list[SourceMention]:
    """Extract source citations from article text.

    Identifies named sources, anonymous sources, and their attribution
    characteristics using pattern matching.

    Args:
        text: Full article text.

    Returns:
        List of SourceMention objects for each detected source.
    """
    if not text:
        return []

    sources: list[SourceMention] = []
    seen_names: set[str] = set()

    # Build a combined verb pattern
    verb_alternation = "|".join(re.escape(v) for v in sorted(ALL_VERBS, key=len, reverse=True))

    # Pattern 1: "[Name] said/told/etc." — named source with attribution verb
    named_before_verb = re.compile(
        rf"\b([A-Z][a-z]+ (?:[A-Z]\. )?[A-Z][a-z]+)\s+({verb_alternation})\b",
    )
    for m in named_before_verb.finditer(text):
        name = m.group(1).strip()
        verb = m.group(2).strip().lower()
        if name in seen_names:
            continue
        seen_names.add(name)

        # Get surrounding context (100 chars each side)
        ctx_start = max(0, m.start() - 100)
        ctx_end = min(len(text), m.end() + 100)
        context = text[ctx_start:ctx_end]

        sources.append(SourceMention(
            name=name,
            is_anonymous=False,
            is_expert=_is_expert_by_title(context),
            affiliation=_extract_affiliation(context),
            quote=_extract_nearby_quote(text, m.start(), m.end()),
            attribution_verb=verb,
        ))

    # Pattern 2: "said/told/etc. [Name]" — verb before named source
    verb_before_named = re.compile(
        rf"\b({verb_alternation})\s+([A-Z][a-z]+ (?:[A-Z]\. )?[A-Z][a-z]+)\b",
    )
    for m in verb_before_named.finditer(text):
        verb = m.group(1).strip().lower()
        name = m.group(2).strip()
        if name in seen_names:
            continue
        seen_names.add(name)

        ctx_start = max(0, m.start() - 100)
        ctx_end = min(len(text), m.end() + 100)
        context = text[ctx_start:ctx_end]

        sources.append(SourceMention(
            name=name,
            is_anonymous=False,
            is_expert=_is_expert_by_title(context),
            affiliation=_extract_affiliation(context),
            quote=_extract_nearby_quote(text, m.start(), m.end()),
            attribution_verb=verb,
        ))

    # Pattern 3: "according to [Name]"
    according_to = re.compile(
        r"\baccording to ([A-Z][a-z]+ (?:[A-Z]\. )?[A-Z][a-z]+)\b"
    )
    for m in according_to.finditer(text):
        name = m.group(1).strip()
        if name in seen_names:
            continue
        seen_names.add(name)

        ctx_start = max(0, m.start() - 100)
        ctx_end = min(len(text), m.end() + 100)
        context = text[ctx_start:ctx_end]

        sources.append(SourceMention(
            name=name,
            is_anonymous=False,
            is_expert=_is_expert_by_title(context),
            affiliation=_extract_affiliation(context),
            quote="",
            attribution_verb="according to",
        ))

    # Pattern 4: Anonymous sources
    anon_patterns = [
        re.compile(r"\baccording to (?:people|sources|individuals)", re.IGNORECASE),
        re.compile(r"\bpeople familiar with (?:the )?(?:matter|situation|plans|discussions?)", re.IGNORECASE),
        re.compile(r"\bspoke on (?:the )?condition (?:of )?anonymity", re.IGNORECASE),
        re.compile(r"\basked not to be (?:identified|named)", re.IGNORECASE),
        re.compile(r"\bsources (?:said|told|indicated|close to|inside|within|briefed on)", re.IGNORECASE),
        re.compile(r"\ba person with (?:direct )?knowledge", re.IGNORECASE),
        re.compile(r"\bpeople (?:briefed on|with knowledge of)", re.IGNORECASE),
        re.compile(r"\binsiders? (?:said|told|indicated|suggested)", re.IGNORECASE),
        re.compile(r"\ba (?:former|current) (?:employee|executive|official) who", re.IGNORECASE),
        # Unnamed/unidentified source descriptor patterns — common in tech/workplace reporting
        re.compile(r"\ban? unnamed (?:worker|employee|executive|official|source|person|staffer|engineer)", re.IGNORECASE),
        re.compile(r"\ban? (?:second|third|fourth|another) (?:worker|employee|source|person|engineer)", re.IGNORECASE),
        re.compile(r"\b(?:one|another|a) (?:worker|employee|engineer|staffer) (?:said|told|called|described|complained)", re.IGNORECASE),
        re.compile(r"\ban? (?:worker|employee|engineer|staffer) (?:was quoted|was reported)", re.IGNORECASE),
        re.compile(r"\b(?:some|several|multiple|many) (?:workers|employees|engineers|staffers) (?:said|told|described|called|complained)", re.IGNORECASE),
        # Publication-as-investigator patterns
        re.compile(r"\b\w+ (?:found|reported|revealed) (?:widespread|significant|extensive|growing)", re.IGNORECASE),
    ]

    for pat in anon_patterns:
        for m in pat.finditer(text):
            descriptor = m.group().strip()
            # Use the descriptor as a unique key
            if descriptor.lower() in {n.lower() for n in seen_names}:
                continue
            seen_names.add(descriptor)

            ctx_start = max(0, m.start() - 100)
            ctx_end = min(len(text), m.end() + 100)
            context = text[ctx_start:ctx_end]

            sources.append(SourceMention(
                name=descriptor,
                is_anonymous=True,
                is_expert=False,
                affiliation="",
                quote=_extract_nearby_quote(text, m.start(), m.end()),
                attribution_verb=_find_attribution_verb(context),
            ))

    return sources


def _extract_nearby_quote(text: str, ref_start: int, ref_end: int) -> str:
    """Extract a quoted string near a reference position.

    Looks for text enclosed in quotation marks within 200 characters
    of the reference position.
    """
    search_start = max(0, ref_start - 200)
    search_end = min(len(text), ref_end + 300)
    window = text[search_start:search_end]

    # Look for quoted text (double quotes or smart quotes)
    quote_patterns = [
        re.compile(r'"([^"]{10,300})"'),
        re.compile(r'\u201c([^\u201d]{10,300})\u201d'),
        re.compile(r"'([^']{10,300})'"),
    ]
    for qp in quote_patterns:
        m = qp.search(window)
        if m:
            return m.group(1).strip()

    return ""


def grade_source_authority(sources: list[SourceMention]) -> float:
    """Grade the overall source authority of an article.

    Scoring factors:
    - Named sources score higher than anonymous
    - Expert sources get a bonus
    - Neutral attribution verbs score higher than loaded verbs
    - More diverse sources score higher

    Args:
        sources: List of SourceMention objects.

    Returns:
        Float between 0.0 (low authority/quality) and 1.0 (high authority).
    """
    if not sources:
        return 0.0

    total_score = 0.0

    for source in sources:
        score = 0.0

        # Named vs anonymous: named sources worth more
        if not source.is_anonymous:
            score += 0.4
        else:
            score += 0.1

        # Expert bonus
        if source.is_expert:
            score += 0.2

        # Attribution verb quality
        verb = source.attribution_verb.lower() if source.attribution_verb else ""
        if verb in NEUTRAL_VERBS:
            score += 0.2
        elif verb in LOADED_VERBS:
            score += 0.05
        elif verb:
            score += 0.1

        # Has a direct quote
        if source.quote:
            score += 0.1

        # Has affiliation
        if source.affiliation:
            score += 0.1

        total_score += min(score, 1.0)

    # Normalize by number of sources, with a bonus for source diversity
    base_score = total_score / len(sources)

    # Diversity bonus: more sources = higher credibility (up to a point)
    diversity_bonus = min(len(sources) / 10, 0.15)

    # Penalty for heavy reliance on anonymous sources
    anon_count = sum(1 for s in sources if s.is_anonymous)
    anon_ratio = anon_count / len(sources) if sources else 0
    anon_penalty = anon_ratio * 0.2

    final_score = base_score + diversity_bonus - anon_penalty
    return round(max(0.0, min(1.0, final_score)), 4)


def classify_attribution_verb(verb: str) -> str:
    """Classify an attribution verb as neutral or loaded.

    Args:
        verb: The attribution verb to classify.

    Returns:
        "neutral", "loaded", or "unknown".
    """
    v = verb.lower().strip()
    if v in NEUTRAL_VERBS:
        return "neutral"
    elif v in LOADED_VERBS:
        return "loaded"
    return "unknown"


# --- Source stance analysis ---

# Negative stance indicators in quotes/context — signals the source is
# positioned to undermine or criticize the subject entity.
_NEGATIVE_STANCE_TERMS: list[str] = [
    "harmful", "dangerous", "reckless", "irresponsible", "unacceptable",
    "outrageous", "appalling", "unethical", "deceptive", "misleading",
    "violated", "violating", "violation", "abuse", "abusive",
    "exploiting", "exploitation", "surveillance", "invasion",
    "threatening", "threatened", "scary", "alarming", "disturbing",
    "catastrophic", "devastating", "shameful", "disgraceful",
    "failure", "failed", "broken", "corrupt", "toxic",
    "censorship", "silencing", "suppression", "retaliation",
    "monopoly", "anti-competitive", "predatory", "bullying",
    "inadequate", "insufficient", "negligent", "negligence",
    "soul-crushing", "dehumanizing", "atrocious", "brutal",
    "lied", "lying", "dishonest", "hypocrisy", "hypocritical",
    "demand", "demanded", "must stop", "should stop", "must be held",
    "accountability", "hold accountable", "ban", "block", "kill",
]

# Positive stance indicators in quotes/context — signals the source is
# positioned to validate or defend the subject entity.
_POSITIVE_STANCE_TERMS: list[str] = [
    "innovative", "groundbreaking", "revolutionary", "pioneering",
    "impressive", "remarkable", "excellent", "outstanding", "world-class",
    "responsible", "committed", "dedicated", "thoughtful", "careful",
    "improved", "improving", "progress", "achievement", "milestone",
    "beneficial", "positive", "constructive", "helpful", "empowering",
    "proud", "excited", "thrilled", "delighted", "pleased",
    "safe", "safety", "secure", "security", "privacy-focused",
    "transparent", "transparency", "open", "collaborative",
    "leading", "leader", "best-in-class", "state-of-the-art",
]


def analyze_source_stance(
    sources: list[SourceMention],
    target_entity: str = "",
) -> dict:
    """Analyse the collective stance of sources toward a subject entity.

    Unlike ``grade_source_authority`` (which measures source quality),
    this function measures *whose side* the sources are on.  An article
    can have 100% named, high-authority sources — all deployed to
    undermine the subject.  That's high authority but adversarial stance.

    Args:
        sources: Extracted source mentions from the article.
        target_entity: Optional target entity name for context-aware
            stance detection (unused in current version; reserved for
            future entity-coref-based stance detection).

    Returns:
        Dict with:
        - ``adversarial_count``: sources positioned against the subject
        - ``supportive_count``: sources positioned supporting the subject
        - ``neutral_count``: sources with no clear stance
        - ``stance_balance``: -1.0 (all adversarial) to +1.0 (all supportive)
        - ``total_sources``: total source count
        - ``adversarial_sources``: list of adversarial source names/descriptors
        - ``supportive_sources``: list of supportive source names/descriptors
    """
    if not sources:
        return {
            "adversarial_count": 0,
            "supportive_count": 0,
            "neutral_count": 0,
            "stance_balance": 0.0,
            "total_sources": 0,
            "adversarial_sources": [],
            "supportive_sources": [],
        }

    adversarial: list[str] = []
    supportive: list[str] = []
    neutral: list[str] = []

    for source in sources:
        # Combine quote and attribution verb context for stance detection
        context_text = (source.quote + " " + source.attribution_verb).lower()

        neg_count = sum(
            1 for term in _NEGATIVE_STANCE_TERMS
            if re.search(rf"\b{re.escape(term)}\b", context_text)
        )
        pos_count = sum(
            1 for term in _POSITIVE_STANCE_TERMS
            if re.search(rf"\b{re.escape(term)}\b", context_text)
        )

        # Also consider the attribution verb: loaded verbs with negative
        # connotation shift the stance adversarial
        verb = source.attribution_verb.lower().strip() if source.attribution_verb else ""
        if verb in {"warned", "blasted", "slammed", "demanded", "accused",
                     "alleged", "charged", "complained", "fumed", "lamented",
                     "ranted", "scoffed", "sneered", "threatened"}:
            neg_count += 1
        elif verb in {"confirmed", "acknowledged", "noted", "explained"}:
            # These are neutral-to-positive — don't shift
            pass

        if neg_count > pos_count:
            adversarial.append(source.name)
        elif pos_count > neg_count:
            supportive.append(source.name)
        else:
            neutral.append(source.name)

    total = len(sources)
    adversarial_count = len(adversarial)
    supportive_count = len(supportive)
    neutral_count = len(neutral)

    # Stance balance: -1.0 (all adversarial) to +1.0 (all supportive)
    if adversarial_count + supportive_count == 0:
        stance_balance = 0.0
    else:
        stance_balance = (supportive_count - adversarial_count) / (
            adversarial_count + supportive_count
        )
    stance_balance = round(max(-1.0, min(1.0, stance_balance)), 4)

    return {
        "adversarial_count": adversarial_count,
        "supportive_count": supportive_count,
        "neutral_count": neutral_count,
        "stance_balance": stance_balance,
        "total_sources": total,
        "adversarial_sources": adversarial,
        "supportive_sources": supportive,
    }
