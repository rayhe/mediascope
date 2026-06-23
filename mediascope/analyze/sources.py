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
    # Present-tense forms — many publications use present tense for
    # attribution ("says Gong", "notes Ji") especially in analytical and
    # explainer articles.  Missing these caused zero-source detection on
    # MIT Technology Review, Nature, and similar outlets.
    "says", "tells", "notes", "explains", "states",
    "adds", "comments", "remarks", "observes", "reports",
    "confirms", "acknowledges", "responds", "replies",
    "mentions", "indicates", "describes", "recalls",
    "agrees", "points",  # "agrees" / "points out" — common neutral verbs
}

LOADED_VERBS: set[str] = {
    "claimed", "argued", "warned", "insisted", "admitted",
    "conceded", "denied", "blasted", "slammed", "demanded",
    "charged", "accused", "alleged", "suggested", "hinted",
    "boasted", "bragged", "complained", "fumed", "lamented",
    "ranted", "scoffed", "sneered", "vowed", "threatened",
    "confessed", "revealed", "declared", "proclaimed",
    # Present-tense forms
    "claims", "argues", "warns", "insists", "admits",
    "concedes", "denies", "blasts", "slams", "demands",
    "charges", "accuses", "alleges", "suggests", "hints",
    "boasts", "brags", "complains", "fumes", "laments",
    "rants", "scoffs", "sneers", "vows", "threatens",
    "confesses", "reveals", "declares", "proclaims",
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

# Stop-words that look like names in source extraction regex patterns.
# These are common English words that start with a capital letter when
# they begin a sentence and would match the ``[A-Z][a-z]+ [A-Z][a-z]+``
# pattern for "First Last" names, producing false-positive source
# extractions like "After Meta said" → source = "After Meta".
_NAME_STOP_FIRST_WORDS: set[str] = {
    "After", "Before", "Because", "Since", "While", "During",
    "Despite", "Although", "Though", "Until", "Unless",
    "Where", "When", "Whether", "Within", "Without",
    "Under", "Behind", "Beyond", "Between", "Among",
    "About", "Above", "Below", "Around", "Outside",
    "Inside", "Against", "Across", "Along", "Among",
    "Through", "Toward", "Towards",
    "Instead", "However", "Meanwhile", "Furthermore",
    "Moreover", "Therefore", "Thus", "Hence",
    "Early", "Later", "Earlier", "Overall",
    "Some", "Many", "Most", "Several", "Other",
    "Both", "Each", "Every", "Either", "Neither",
    "Last", "Next", "That", "This", "These", "Those",
    "But", "And", "Also", "Still", "Yet", "Then", "Now",
    "Such", "Much", "Not", "Just", "Only", "Even",
    "Already", "Perhaps", "Maybe", "Certainly",
}

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

        # Filter out false-positive names where the first word is a common
        # English word that happened to be capitalised at sentence start
        first_word = name.split()[0]
        if first_word in _NAME_STOP_FIRST_WORDS:
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

    # Pattern 5: "[Name], [appositive clause], [verb]"
    # Catches "Jessica Ji, a senior research analyst at Georgetown, agrees."
    # The appositive is a comma-delimited descriptor between name and verb.
    name_appositive_verb = re.compile(
        rf"\b([A-Z][a-z]+ (?:[A-Z]\. )?[A-Z][a-z]+)"
        rf",\s+(?:an? |the )?[a-z]{{2,}}"  # start of appositive
        rf"[^.\"]*?"                         # rest of appositive (no sentence-end or quote)
        rf",\s*({verb_alternation})\b",
    )
    for m in name_appositive_verb.finditer(text):
        name = m.group(1).strip()
        verb = m.group(2).strip().lower()
        if name in seen_names:
            continue

        first_word = name.split()[0]
        if first_word in _NAME_STOP_FIRST_WORDS:
            continue

        seen_names.add(name)

        ctx_start = max(0, m.start() - 100)
        ctx_end = min(len(text), m.end() + 300)
        context = text[ctx_start:ctx_end]

        sources.append(SourceMention(
            name=name,
            is_anonymous=False,
            is_expert=_is_expert_by_title(context),
            affiliation=_extract_affiliation(context),
            quote=_extract_nearby_quote(text, m.start(), m.end()),
            attribution_verb=verb,
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
        re.compile(r"\b(?:some|several|multiple|many) (?:workers|employees|engineers|staffers|people) (?:said|told|described|called|complained|say|tell)", re.IGNORECASE),
        # Role-descriptor + attribution verb patterns — common in tech/workplace
        # reporting where anonymous sources are described by job role:
        # "a policy staffer says", "a legal staffer adds", "the Instagram employee says"
        re.compile(
            r"\b(?:an?|the|one|another)"
            r" (?:[a-z]+[ -])?"  # optional adjective: "policy", "legal", "longtime", "veteran"
            r"(?:[a-z]+[ -])?"   # second optional adjective: "senior", "current"
            r"(?:worker|employee|staffer|engineer|executive|official|leader|manager|person|researcher|analyst|source)"
            r"(?:\s+(?:who\s+works?\s+(?:on|at|in|for)\s+\w+|at\s+\w+|inside\s+\w+))?"  # optional "who works on X" / "at X"
            r"\s+(?:" + verb_alternation + r")\b",
            re.IGNORECASE,
        ),
        # Reverse pattern: verb + role descriptor
        # "says a policy staffer", "says an employee who works on Instagram"
        re.compile(
            r"\b(?:" + verb_alternation + r")"
            r"\s+(?:an?|the|one|another)"
            r" (?:[a-z]+[ -])?"
            r"(?:[a-z]+[ -])?"
            r"(?:worker|employee|staffer|engineer|executive|official|leader|manager|person|researcher|analyst|source)"
            r"(?:\s+(?:who\s+works?\s+(?:on|at|in|for)\s+\w+|at\s+\w+|inside\s+\w+))?",
            re.IGNORECASE,
        ),
        # "[number] employees/sources" — "according to three employees", "16 current and former employees"
        # Use (?<![,\d]) negative lookbehind to avoid matching partial numbers like "000" from "8,000"
        re.compile(
            r"(?<![,\d])\b(?:\d{1,3}|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|sixteen|twenty|dozen)"
            r" (?:current\s+(?:and\s+)?(?:former\s+)?)?"
            r"(?:workers|employees|staffers|engineers|executives|officials|sources|people)"
            r"\s+(?:" + verb_alternation + r"|familiar|briefed|close)\b",
            re.IGNORECASE,
        ),
        # "several people say" — quantifier + generic people noun + verb
        re.compile(
            r"\b(?:some|several|multiple|many|numerous|various|a few|a handful of|a number of)"
            r" (?:current\s+(?:and\s+)?(?:former\s+)?)?"
            r"(?:workers|employees|staffers|engineers|people|sources|individuals)"
            r"(?:\s+(?:" + verb_alternation + r"))?\b",
            re.IGNORECASE,
        ),
        # "organizers inside the company wrote" — collective group sources
        re.compile(
            r"\b(?:organizers?|critics?|activists?|dissidents?|protestors?|complainants?)"
            r" (?:inside|within|at|from) (?:the )?(?:company|firm|organization|group)\b",
            re.IGNORECASE,
        ),
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


def _collect_all_quotes_for_source(text: str, source_name: str) -> str:
    """Aggregate ALL quoted text attributed to a named source.

    The standard ``extract_sources`` deduplicates by name, keeping only
    the first quote from each source.  For stance analysis, we need the
    COMPLETE set of quotes — a source who says "that's surprising" in
    paragraph 3 and "it's a very dangerous thing" in paragraph 12
    should have both quotes contribute to stance scoring.

    Strategy: find every position where the source's LAST name appears,
    then extract any nearby quoted text within 300 chars.
    """
    if not text or not source_name:
        return ""

    # Use the last name (most specific) for matching
    parts = source_name.strip().split()
    last_name = parts[-1] if parts else source_name

    all_quotes: list[str] = []
    # Find all occurrences of the last name
    for m in re.finditer(re.escape(last_name), text):
        quote = _extract_nearby_quote(text, m.start(), m.end())
        if quote and quote not in all_quotes:
            all_quotes.append(quote)

    return " ".join(all_quotes)


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
    # Strong adversarial / harm language
    "harmful", "dangerous", "reckless", "irresponsible", "unacceptable",
    "outrageous", "appalling", "unethical", "deceptive", "misleading",
    "violated", "violating", "violation", "abuse", "abusive",
    "exploiting", "exploitation", "exploited", "surveillance", "invasion",
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
    # Workplace dissatisfaction & complaint — common in employee-sourced
    # tech reporting where anonymous insiders describe morale, conditions,
    # or management behavior.  Without these, articles like Wired's
    # "Dark Mood Inside Meta" register zero adversarial sources despite
    # 16/18 sources being clearly critical of the company.
    "unhappy", "miserable", "anger", "angry", "fear", "fearful",
    "frustrated", "frustrating", "furious", "disgruntled",
    "demoralized", "demoralizing", "depressed", "degrading",
    "belittled", "berated", "disrespected", "mistreated",
    "humiliated", "humiliating", "betrayed", "betrayal",
    "shattered", "cruel", "short-sighted",
    "no choice", "no option", "not possible", "cannot opt out",
    "forced", "mandatory", "not voluntary",
    "replaced", "replace us", "replace them",
    "unnecessary", "pointless", "unfair", "unjust",
    "sucks", "awful", "terrible", "horrible", "horrific",
    "worst", "rock-bottom", "historically low", "historically poor",
    # Privacy/surveillance complaint
    "screen scraped", "scraping", "privacy violation",
    "invasion of privacy", "big brother", "spying",
    "tracked", "tracking", "no opt-out",
    # Negative personal/emotional
    "empathy", "feign empathy", "can't even feign",
    "contempt", "arrogant", "arrogance", "condescending",
    "callous", "indifferent", "dismissive",
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

# Security/safety terms that are positive ONLY when used as features
# (e.g. "our product ensures security"), not when discussing failures
# (e.g. "security vulnerability", "safety concerns").  The positive
# match is suppressed when the quote also contains a vulnerability-
# context signal.
_POSITIVE_TERMS_CONTEXT_DEPENDENT: set[str] = {
    "safe", "safety", "secure", "security",
}
_VULNERABILITY_CONTEXT_SIGNALS: set[str] = {
    # When ANY of these appear alongside "security"/"safe" in a quote,
    # suppress the positive stance credit — the source is discussing
    # problems, not praising the subject.
    "vulnerability", "vulnerabilities", "vulnerable",
    "hack", "hacked", "hacking", "hacker", "hackers",
    "breach", "breached", "breaches",
    "exploit", "exploits", "exploited", "exploiting",
    "attack", "attacks", "attacker", "attackers", "attacked",
    "flaw", "flaws", "weakness", "weaknesses",
    "bug", "bugs", "glitch",
    "compromise", "compromised",
    "risk", "risks", "risky",
    "threat", "threats",
    "incident", "incidents",
    "injection", "prompt injection",
    "hijack", "hijacked", "hijacking",
    "steal", "stolen", "stole", "stealing",
    "mistake", "mistakes", "error", "errors",
    "trade-off", "tradeoff",
    "concern", "concerns", "concerning",
    "guardrail", "guardrails",
    "red-teaming", "red-team",
}

# Indirect criticism patterns — sources that criticize through
# rhetorical questions, expressions of surprise/disbelief, or
# analogies rather than direct negative vocabulary.
_INDIRECT_CRITICISM_PATTERNS: list[re.Pattern] = [
    # Rhetorical questions implying negligence
    re.compile(r"\bwere there even\b", re.IGNORECASE),
    re.compile(r"\bdid anyone (?:think|bother|try)\b", re.IGNORECASE),
    re.compile(r"\bwhy (?:didn't|did they not|wouldn't|did not)\b", re.IGNORECASE),
    re.compile(r"\bhow (?:could|did|can) they not\b", re.IGNORECASE),
    re.compile(r"\bhow is (?:it|that) (?:possible|acceptable)\b", re.IGNORECASE),
    # Expressions of surprise / disbelief as criticism
    re.compile(r"\bi don'?t understand (?:why|how)\b", re.IGNORECASE),
    re.compile(r"\bit'?s (?:really |quite |very |most |particularly )?surprising\b", re.IGNORECASE),
    re.compile(r"\bit'?s (?:really |quite |very |most |particularly )?striking\b", re.IGNORECASE),
    re.compile(r"\b(?:really |quite |very |most |particularly )?surprising (?:that|coming|from)\b", re.IGNORECASE),
    re.compile(r"\bshould have been (?:uncovered|caught|found|detected|prevented|stopped|fixed)\b", re.IGNORECASE),
    re.compile(r"\bshould not have (?:happened|occurred|been (?:deployed|released|launched))\b", re.IGNORECASE),
    re.compile(r"\b(?:simple|basic|elementary|trivial|obvious) (?:problem|issue|flaw|mistake|error|bug|oversight)\b", re.IGNORECASE),
    re.compile(r"\braises (?:serious |real )?questions\b", re.IGNORECASE),
    # Analogies/metaphors deployed as criticism
    re.compile(r"\belementary school\b", re.IGNORECASE),
    re.compile(r"\bjust wants to please\b", re.IGNORECASE),
    re.compile(r"\blike (?:a |an )?(?:child|toddler|student|amateur|intern)\b", re.IGNORECASE),
    # "Embarrassing" / "concerning" as criticism
    re.compile(r"\bembarrassing\b", re.IGNORECASE),
    re.compile(r"\bconcerning\b", re.IGNORECASE),
    re.compile(r"\bworrying\b", re.IGNORECASE),
    re.compile(r"\btroubling\b", re.IGNORECASE),
    # "Dangerous thing" / "very dangerous"
    re.compile(r"\b(?:very |really |extremely |quite )?dangerous\b", re.IGNORECASE),
    # "Without careful scrutiny"
    re.compile(r"\bwithout (?:careful |proper |adequate |sufficient )?(?:scrutiny|testing|review|oversight|vetting)\b", re.IGNORECASE),
    re.compile(r"\bpush(?:ing|ed)? (?:things |it )?out without\b", re.IGNORECASE),
]


def analyze_source_stance(
    sources_or_text: "list[SourceMention] | str",
    target_entity: str = "",
    *,
    full_text: str = "",
) -> dict:
    """Analyse the collective stance of sources toward a subject entity.

    Unlike ``grade_source_authority`` (which measures source quality),
    this function measures *whose side* the sources are on.  An article
    can have 100% named, high-authority sources — all deployed to
    undermine the subject.  That's high authority but adversarial stance.

    Args:
        sources_or_text: Either a list of extracted SourceMention objects,
            or raw article text (which will be run through extract_sources
            first for convenience).
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
    # Accept raw text for convenience
    if isinstance(sources_or_text, str):
        if not full_text:
            full_text = sources_or_text
        sources = extract_sources(sources_or_text)
    else:
        sources = sources_or_text
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

    # Check for vulnerability-context signals in the FULL ARTICLE text.
    # When the article is fundamentally about security failures/hacks,
    # "security" in any source quote is NOT a positive endorsement —
    # it's discussing the problem domain, not praising the subject.
    full_text_lower = full_text.lower() if full_text else ""
    article_has_vulnerability_context = any(
        re.search(rf"\b{re.escape(signal)}\b", full_text_lower)
        for signal in _VULNERABILITY_CONTEXT_SIGNALS
    ) if full_text_lower else False

    adversarial: list[str] = []
    supportive: list[str] = []
    neutral: list[str] = []

    for source in sources:
        # For stance analysis, aggregate ALL quotes attributed to this
        # source across the full article, not just the first one captured
        # by ``extract_sources``.
        if full_text and not source.is_anonymous:
            aggregated_quotes = _collect_all_quotes_for_source(
                full_text, source.name
            )
        else:
            aggregated_quotes = source.quote

        # Combine all quotes + attribution verb for stance detection
        context_text = (aggregated_quotes + " " + source.attribution_verb).lower()

        # Check for vulnerability-context signals at two levels:
        # 1. Quote-level: the individual quote mentions vulnerabilities
        # 2. Article-level: the article is about security failures
        # Either suppresses positive matches on "security"/"safety" etc.
        quote_has_vulnerability_context = any(
            re.search(rf"\b{re.escape(signal)}\b", context_text)
            for signal in _VULNERABILITY_CONTEXT_SIGNALS
        )
        has_vulnerability_context = (
            quote_has_vulnerability_context
            or article_has_vulnerability_context
        )

        neg_count = sum(
            1 for term in _NEGATIVE_STANCE_TERMS
            if re.search(rf"\b{re.escape(term)}\b", context_text)
        )

        # Indirect criticism patterns — rhetorical questions, surprise,
        # analogies — contribute to adversarial stance
        indirect_hits = sum(
            1 for pat in _INDIRECT_CRITICISM_PATTERNS
            if pat.search(context_text)
        )
        neg_count += indirect_hits

        pos_count = sum(
            1 for term in _POSITIVE_STANCE_TERMS
            if re.search(rf"\b{re.escape(term)}\b", context_text)
            # Suppress context-dependent terms when vulnerability context
            # is present — "security" in "security vulnerability" is not
            # a positive endorsement
            and not (
                has_vulnerability_context
                and term in _POSITIVE_TERMS_CONTEXT_DEPENDENT
            )
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
