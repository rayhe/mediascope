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
    "wrote", "addressed", "pointed",  # "wrote"/"addressed" for letters, "pointed out"
    "mused", "quipped", "reflected", "pondered",  # reflective/conversational attribution
    "dubbed", "coined",  # naming/labeling attribution
    "pleaded", "implored", "beseeched",  # urgent appeal attribution
    # Present-tense forms — many publications use present tense for
    # attribution ("says Gong", "notes Ji") especially in analytical and
    # explainer articles.  Missing these caused zero-source detection on
    # MIT Technology Review, Nature, and similar outlets.
    "says", "tells", "notes", "explains", "states",
    "adds", "comments", "remarks", "observes", "reports",
    "confirms", "acknowledges", "responds", "replies",
    "mentions", "indicates", "describes", "recalls",
    "agrees", "points",  # "agrees" / "points out" — common neutral verbs
    "writes", "addresses",  # present-tense of added verbs
    "muses", "quips", "reflects", "ponders",  # present-tense reflective
    "dubs", "coins",  # present-tense labeling
    "pleads", "implores",  # present-tense urgent appeal
    "thinks", "believes", "considers",  # cognitive/opinion attribution
    "cautions",  # hedged warning attribution
}

LOADED_VERBS: set[str] = {
    "claimed", "argued", "warned", "insisted", "admitted",
    "conceded", "denied", "blasted", "slammed", "demanded",
    "charged", "accused", "alleged", "suggested", "hinted",
    "boasted", "bragged", "complained", "fumed", "lamented",
    "ranted", "scoffed", "sneered", "vowed", "threatened",
    "confessed", "revealed", "declared", "proclaimed",
    "called", "dismissed", "rejected", "downplayed",
    # Present-tense forms
    "claims", "argues", "warns", "insists", "admits",
    "concedes", "denies", "blasts", "slams", "demands",
    "charges", "accuses", "alleges", "suggests", "hints",
    "boasts", "brags", "complains", "fumes", "laments",
    "rants", "scoffs", "sneers", "vows", "threatens",
    "confesses", "reveals", "declares", "proclaims",
    "calls", "dismisses", "rejects", "downplays",
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
    "judge", "justice", "magistrate", "chief justice",
    "spokesperson", "spokesman", "spokeswoman",
    "expert", "specialist", "consultant", "fellow",
    "scholar", "academic", "strategist", "adviser", "advisor",
]

# Stop-words that look like names in source extraction regex patterns.
# These are common English words that start with a capital letter when
# they begin a sentence and would match the ``[A-Z][a-z]+ [A-Z][a-z]+``
# pattern for "First Last" names, producing false-positive source
# extractions like "After Meta said" → source = "After Meta".

# Known tech company names (lowercase) — used to filter out company
# names from "verb [Name]" patterns that would otherwise match
# "rejected Meta Platforms" as a named human source.
_KNOWN_ORGS_LOWER: set[str] = {
    "meta", "google", "apple", "microsoft", "amazon", "openai",
    "anthropic", "nvidia", "tesla", "spacex", "x", "twitter",
    "alphabet", "ibm", "oracle", "palantir", "samsung",
    "instagram", "snapchat", "snap", "tiktok", "youtube",
    "bytedance", "reddit", "pinterest", "discord", "spotify",
    "netflix", "uber", "lyft", "airbnb", "stripe", "shopify",
    "reuters", "bloomberg",
}
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
    # Short common words that look like names when capitalized
    "Any", "All", "Our", "His", "Her", "Its", "The",
    "They", "We", "You", "She", "He",
    # Day names — "on Thursday argues" should not extract "Thursday" as source
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
    "Saturday", "Sunday",
    # Month names — "In January reported" should not extract "January"
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
    # US state names — "Oakland, California denied" should not extract
    # "California" as a source; state names appear in datelines and venue
    # descriptions, not as journalistic sources.
    "California", "Texas", "Florida", "Georgia", "Virginia",
    "Illinois", "Ohio", "Michigan", "Arizona", "Colorado",
    "Pennsylvania", "Maryland", "Indiana", "Missouri", "Minnesota",
    "Wisconsin", "Oregon", "Connecticut", "Massachusetts",
    "Washington", "Tennessee", "Kentucky", "Louisiana",
    "Carolina", "Alabama", "Oklahoma", "Nebraska", "Delaware",
    "Montana", "Idaho", "Hawaii", "Alaska", "Nevada", "Utah",
    "Arkansas", "Iowa", "Kansas", "Maine", "Wyoming", "Vermont",
    # Common city names that appear in datelines
    "Oakland", "Sacramento", "Austin", "Seattle", "Portland",
    "Chicago", "Boston", "Denver", "Phoenix", "Atlanta",
    "Dallas", "Houston", "Miami", "Orlando", "Detroit",
    "Philadelphia", "Baltimore", "Cleveland", "Cincinnati",
    "Pittsburgh", "Charlotte", "Nashville", "Memphis",
    "Milwaukee", "Minneapolis", "Richmond", "Norfolk",
    "Raleigh", "Tampa", "Jacksonville",
}

# Publication / organization partial names that look like "First Last"
# and would false-positive as a source name.  E.g. "The New York Times
# reported" → the named-source regex might match "York Times" as a name.
_NAME_STOP_NAMES: set[str] = {
    "York Times", "York Post", "Wall Street",
    "Street Journal", "Washington Post",
    "New York", "Los Angeles", "San Francisco",
    "Silicon Valley", "United States", "United Kingdom",
    "South Korea", "North Korea", "South China",
    "North America", "South America", "East Asia",
    "Hong Kong", "Saudi Arabia", "Costa Rica",
    "Puerto Rico", "El Salvador",
    # Product names that look like "First Last"
    "Meta Glasses", "Meta Adventurer", "Meta Fury",
    "Meta Starfire", "Meta Quest", "Meta Horizon",
    "Ray Ban", "Smart Glasses", "Gentle Monster",
    # Book/media titles that look like "First Last"
    "Careless People", "Brave New", "Dark Web",
    "Social Dilemma", "Social Network", "Deep State",
    # Government agency / regulatory body partial names
    "Relations Board", "Labor Relations", "National Labor",
    "Trade Commission", "Federal Trade", "Federal Communications",
    "Securities Exchange", "Exchange Commission",
    # Publication names that match "First Last" name pattern
    "Business Insider", "Tech Review", "Technology Review",
    "Daily Beast", "Daily Mail", "Morning Post",
    "Evening Standard",
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
    # Internal document leaks — the document is named but the leaker is anonymous
    "internal documents", "internal memo", "internal email",
    "internal guidelines", "internal presentation",
    "multiple sources",
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
    source_type: str = "named"  # "named", "anonymous", or "no_comment"


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

    Handles complex institution names with hyphens (Urbana-Champaign),
    em dashes (Wisconsin–Madison), possessives (Georgetown's), and
    lowercase connecting words (Center for Security and Emerging Technology).
    """
    # Character class for institution names: letters, spaces, ampersands,
    # hyphens, en/em dashes, apostrophes/smart quotes, and periods (for
    # abbreviations like "U.S." or "St.").
    _INST_CHARS = r"A-Za-z &\-\u2013\u2014''\."

    patterns = [
        # Pattern 0 (most specific): "[Organization]'s CEO/president/director/etc."
        # Must be tried first — prevents false positives from the broader
        # "of [Organization]" pattern that can match junk from context window.
        # E.g., "Meta's vice president of communications" should extract "Meta",
        # not "NameTag system into the Meta AI app" from "portions of the NameTag..."
        re.compile(
            r"([A-Z][" + _INST_CHARS + r"]+?)"
            r"(?:'s|'s|\u2019s)\s+"
            r"(?:(?:chief|vice|deputy|senior|executive|associate|assistant|managing)\s+)*"
            r"(?:CEO|president|officer|director|chief|head|spokesperson|editor|counsel)",
            re.DOTALL,
        ),
        # Pattern 0b: "[Organization] [title phrase] [Name]" — non-possessive
        # "Meta chief technology officer Andrew Bosworth" → "Meta"
        # Catches the common pattern where an org name directly precedes a
        # title without possessive, followed by a person's name.  Must
        # precede Pattern 2 (possessive "[Org]'s [Noun]") to prevent
        # false matches like "Snap's Specs" beating "Meta" in context.
        re.compile(
            r"\b([A-Z][A-Za-z]+)"
            r"\s+(?:(?:chief|vice|deputy|senior|executive|associate|assistant|managing|former|acting)\s+)*"
            r"(?:(?:technology|financial|operating|product|marketing|information|legal|revenue|strategy|"
            r"science|data|communications?|creative|editorial|content|policy|engineering|research|design|"
            r"industrial|human\s+resources)\s+)*"
            r"(?:officer|director|president|counsel|spokesperson|spokesman|spokeswoman|editor|secretary|"
            r"manager|head|executive)\s+[A-Z]",
            re.DOTALL,
        ),
        # Pattern 1: "at [the] [Institution Name][,. or attribution verb]"
        # Non-greedy match capped at 60 chars to prevent spanning
        # across paragraph boundaries when _INST_CHARS includes spaces.
        re.compile(
            r"\b(?:of|at|from|with)\s+(?:the\s+)?"
            r"([A-Z][" + _INST_CHARS + r"]{1,60}?)"
            r"(?:[,.\n]|\s+(?:" + "|".join([
                "said", "told", "who", "says", "tells", "noted", "notes",
                "agrees", "adds", "added", "explained", "explains",
                "confirmed", "warned", "argues", "recalled", "reported",
            ]) + r"))",
            re.DOTALL,
        ),
        # Pattern 2: Possessive: "Georgetown's Center for ..."
        # Captures the full name after the possessive through to a
        # sentence-ending or attribution cue.
        re.compile(
            r"([A-Z][A-Za-z]+)['\u2019]s\s+"
            r"([A-Z][" + _INST_CHARS + r"]{1,60}?)"
            r"(?:[,.\n]|\s+(?:" + "|".join([
                "said", "told", "who", "says", "tells", "noted", "notes",
                "agrees", "adds", "added", "explained", "explains",
            ]) + r"))",
            re.DOTALL,
        ),
    ]
    for i, pat in enumerate(patterns):
        m = pat.search(context)
        if m:
            if i == 3:
                # Possessive pattern (Pattern 2): combine "Georgetown" + "Center for ..."
                aff = m.group(1).strip() + "'s " + m.group(2).strip()
            else:
                aff = m.group(1).strip()
            # Filter out generic words and overly short matches
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
        # Filter out publication/organization partial names
        if name in _NAME_STOP_NAMES:
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

        # Filter out false-positive names
        first_word = name.split()[0]
        if first_word in _NAME_STOP_FIRST_WORDS:
            continue
        if name in _NAME_STOP_NAMES:
            continue
        # Filter out known company names that look like "First Last" —
        # e.g. "rejected Meta Platforms" should not parse "Meta Platforms"
        # as a named human source.
        if first_word.lower() in _KNOWN_ORGS_LOWER:
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

    # Pattern 2b: "said/told [title/role phrase] [Name]" — verb, then a
    # title like "company spokesperson" or "Meta official", then a proper
    # name.  Wire services (Reuters, AP, AFP) routinely place the role
    # between the verb and the name:  ``said company spokesperson Tracy
    # Clayton``, ``told Reuters correspondent Jane Smith``.  Pattern 2
    # misses these because it requires the name immediately after the verb.
    verb_title_named = re.compile(
        rf"\b({verb_alternation})\s+"
        r"(?:(?:company|corporate|government|senior|chief|lead|former|a|an|the|its)\s+)?"
        r"(?:spokesperson|spokeswoman|spokesman|representative|official|"
        r"executive|director|analyst|correspondent|reporter|attorney|lawyer|"
        r"vice\s+president|president|editor|manager|officer|adviser|advisor|"
        r"chair(?:man|woman|person)?|commissioner|counsel)\s+"
        r"([A-Z][a-z]+ (?:[A-Z]\. )?[A-Z][a-z]+)\b",
    )
    for m in verb_title_named.finditer(text):
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
    # Use [Aa] prefix to handle sentence-initial capitalization without
    # IGNORECASE (which would also make the name capture group case-
    # insensitive, producing false positives like "four people").
    according_to = re.compile(
        r"\b[Aa]ccording to ([A-Z][a-z]+ (?:[A-Z]\. )?[A-Z][a-z]+)\b",
    )
    for m in according_to.finditer(text):
        name = m.group(1).strip()
        if name in seen_names:
            continue

        # Filter out false-positive names
        first_word = name.split()[0]
        if first_word in _NAME_STOP_FIRST_WORDS:
            continue
        if name in _NAME_STOP_NAMES:
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

    # Pattern 3b: "[Name] has/have/had [verb]" — auxiliary + main verb
    # Catches: "Angelos Arnis has dubbed", "Will Manidis had argued",
    # "Joe Weisenthal has noted"
    name_aux_verb = re.compile(
        rf"\b([A-Z][a-z]+ (?:[A-Z]\. )?[A-Z][a-z]+)\s+"
        rf"(?:has|have|had)\s+"
        rf"(?:\w+ly\s+)?"  # optional adverb
        rf"({verb_alternation})\b",
    )
    for m in name_aux_verb.finditer(text):
        name = m.group(1).strip()
        verb = m.group(2).strip().lower()
        if name in seen_names:
            continue

        first_word = name.split()[0]
        if first_word in _NAME_STOP_FIRST_WORDS:
            continue
        if name in _NAME_STOP_NAMES:
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

    # Pattern 5: "[Name], [appositive clause], [verb]"
    # Catches "Jessica Ji, a senior research analyst at Georgetown, agrees."
    # Also catches "Tracy Clayton, a Meta spokesperson, tells WIRED."
    # Also catches adverb+verb: "Will Manidis, a start-up founder, convincingly argued..."
    # The appositive is a comma-delimited descriptor between name and verb.
    name_appositive_verb = re.compile(
        rf"\b([A-Z][a-z]+ (?:[A-Z]\. )?[A-Z][a-z]+)"
        rf",\s+(?:an? |the )?[A-Za-z]{{2,}}"  # start of appositive (may have capitalized org names)
        rf"[^.\"]*?"                         # rest of appositive (no sentence-end or quote)
        rf",\s*(?:\w+ly\s+)?({verb_alternation})\b",  # optional adverb before verb
    )
    for m in name_appositive_verb.finditer(text):
        name = m.group(1).strip()
        verb = m.group(2).strip().lower()
        if name in seen_names:
            continue

        first_word = name.split()[0]
        if first_word in _NAME_STOP_FIRST_WORDS:
            continue
        if name in _NAME_STOP_NAMES:
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

    # Pattern 5b: "[LastName] says/told/etc." — single-name source
    # Common journalism convention: after introducing a source by full
    # name ("Peter Bristol, VP of..."), subsequent references use just
    # the last name.  This catches sources that are ONLY referred to by
    # a single capitalized name + attribution verb in the article.
    # Filtered aggressively to prevent false positives from org names,
    # common English words, and product names.
    _SINGLE_NAME_ORG_STOPS = {
        "Meta", "Google", "Apple", "Amazon", "Microsoft", "Facebook",
        "Instagram", "WhatsApp", "Snapchat", "Tesla", "Samsung",
        "Nvidia", "Oracle", "Palantir", "Intel", "Adobe", "Netflix",
        "Spotify", "Twitter", "TikTok", "Uber", "Lyft", "Airbnb",
        "Pinterest", "Reddit", "Discord", "Slack", "Zoom", "Stripe",
        "Square", "Block", "Shopify", "Congress", "Pentagon",
        "Reuters", "Bloomberg", "WIRED", "Wired",
        "Media",  # "404 Media" → regex strips numeric prefix, leaving "Media"
        # Chinese / international tech companies
        "Alibaba", "Baidu", "Tencent", "Huawei", "Xiaomi",
        "ByteDance", "Bytedance",
        # Common words that start sentences
        "People", "Everyone", "Somebody", "Someone", "Something",
        "Today", "Tomorrow", "Yesterday", "Here", "There",
        "First", "Second", "Third", "Finally", "Overall",
        "Like", "Similar", "Another", "According", "Rather",
        "True", "False", "None", "Yes", "Yeah",
    }
    single_name_verb = re.compile(
        rf"\b([A-Z][a-z]{{2,}})\s+({verb_alternation})\b",
    )
    for m in single_name_verb.finditer(text):
        name = m.group(1).strip()
        verb = m.group(2).strip().lower()
        if name in seen_names:
            continue
        if name in _NAME_STOP_FIRST_WORDS:
            continue
        if name in _SINGLE_NAME_ORG_STOPS:
            continue
        if name in _NAME_STOP_NAMES:
            continue
        # Skip if this single name is the last word of an already-seen
        # full name — e.g., skip "Bosworth" if "Andrew Bosworth" already
        # captured.  Prevents duplicate source entries for the same person.
        if any(seen.endswith(" " + name) for seen in seen_names):
            continue
        # Also skip if this single name is the FIRST word of a full name
        # already seen — e.g., skip "Neil" if "Neil Gong" already captured.
        if any(seen.startswith(name + " ") for seen in seen_names):
            continue

        seen_names.add(name)

        ctx_start = max(0, m.start() - 100)
        ctx_end = min(len(text), m.end() + 200)
        context = text[ctx_start:ctx_end]

        sources.append(SourceMention(
            name=name,
            is_anonymous=False,
            is_expert=_is_expert_by_title(context),
            affiliation=_extract_affiliation(context),
            quote=_extract_nearby_quote(text, m.start(), m.end()),
            attribution_verb=verb,
        ))

    # Pattern 5c: "says/told/etc. [LastName]" — verb before single surname
    # Catches the extremely common journalistic convention where an
    # attribution verb precedes a single surname: "says Shah", "notes Fox".
    # Pattern 2 handles this for full names but not for single-word surnames
    # (bug found via MIT TR DeepMind multi-agent article where ~5 "says Shah"
    # instances were all missed).
    #
    # Naming-context filter for "called": the verb "called" is a valid
    # attribution verb ("she called it a disaster") but also means "named"
    # ("a model called Mythos").  When the preceding context shows a naming
    # construction (noun + "called"), skip the match.  This prevents AI model
    # names, product names, and company names introduced with "called" from
    # being misidentified as journalistic sources.
    # The regex matches the text *before* the "called [Name]" match.
    # Since m.start() is the start of "called", pre_ctx ends right before
    # "called", so we look for the naming noun at the end of the context.
    _CALLED_NAMING_LOOKBEHIND = re.compile(
        r"\b(?:model|version|product|system|company|tool|app|service|platform|"
        r"organization|group|device|feature|program|project|initiative|startup|"
        r"firm|entity|technology|framework|protocol|standard|module|package|"
        r"technique|method|approach|concept|plan|policy|operation|mission|"
        r"variant|iteration|release|update|upgrade|fork|branch|build|suite|"
        r"chip|processor|chatbot|assistant|agent|bot|AI|software|hardware|"
        r"thing|one|it)\s*$",
        re.IGNORECASE,
    )
    verb_before_single = re.compile(
        rf"\b({verb_alternation})\s+([A-Z][a-z]{{2,}})\b",
    )
    for m in verb_before_single.finditer(text):
        verb = m.group(1).strip().lower()
        name = m.group(2).strip()
        if name in seen_names:
            continue
        if name in _NAME_STOP_FIRST_WORDS:
            continue
        if name in _SINGLE_NAME_ORG_STOPS:
            continue
        if name in _NAME_STOP_NAMES:
            continue
        # Skip if this single name is the last word of an already-seen
        # full name — same dedup logic as Pattern 5b.
        if any(seen.endswith(" " + name) for seen in seen_names):
            continue
        # Also skip first-name matches — same as Pattern 5b.
        if any(seen.startswith(name + " ") for seen in seen_names):
            continue
        # Skip "called [Name]" when preceding context shows a naming
        # construction (e.g. "a model called Mythos"), not an attribution.
        if verb == "called":
            pre_ctx = text[max(0, m.start() - 60):m.start()]
            if _CALLED_NAMING_LOOKBEHIND.search(pre_ctx):
                continue

        seen_names.add(name)

        ctx_start = max(0, m.start() - 100)
        ctx_end = min(len(text), m.end() + 200)
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
        re.compile(r"\bspoke (?:with \w+ )?on (?:the )?condition (?:of )?anonymity", re.IGNORECASE),
        re.compile(r"\basked not to be (?:identified|named)", re.IGNORECASE),
        re.compile(r"\bsources (?:said|told|indicated|close to|inside|within|briefed on)", re.IGNORECASE),
        re.compile(r"\ba person with (?:direct )?knowledge", re.IGNORECASE),
        re.compile(r"\bpeople (?:briefed on|with knowledge of)", re.IGNORECASE),
        re.compile(r"\binsiders? (?:said|told|indicated|suggested)", re.IGNORECASE),
        re.compile(r"\ba (?:former|current) (?:employee|executive|official) who", re.IGNORECASE),
        # Unnamed/unidentified source descriptor patterns — common in tech/workplace reporting
        re.compile(r"\ban? unnamed (?:worker|employee|executive|official|source|person|staffer|engineer)", re.IGNORECASE),
        re.compile(r"\ban? (?:second|third|fourth|another) (?:worker|employee|source|person|engineer)", re.IGNORECASE),
        re.compile(r"\b((?:one|another|a) (?:worker|employee|engineer|staffer)) (?:said|told|called|described|complained)", re.IGNORECASE),
        re.compile(r"\b(an? (?:worker|employee|engineer|staffer)) (?:was quoted|was reported)", re.IGNORECASE),
        re.compile(r"\b((?:some|several|multiple|many) (?:workers|employees|engineers|staffers|people)) (?:said|told|described|called|complained|say|tell)", re.IGNORECASE),
        # Role-descriptor + attribution verb patterns — common in tech/workplace
        # reporting where anonymous sources are described by job role:
        # "a policy staffer says", "a legal staffer adds", "the Instagram employee says"
        re.compile(
            r"\b((?:an?|the|one|another)"
            r" (?:[A-Za-z]+[ -])?"  # optional adjective/org name: "policy", "Meta", "longtime"
            r"(?:[A-Za-z]+[ -])?"   # second optional adjective: "senior", "current"
            r"(?:worker|employee|staffer|engineer|executive|official|leader|manager|person|researcher|analyst|source|spokesperson|spokeswoman|spokesman)"
            r"(?:\s+(?:who\s+works?\s+(?:on|at|in|for)\s+\w+|at\s+\w+|inside\s+\w+))?)"  # optional "who works on X" / "at X"
            r"\s+(?:" + verb_alternation + r")\b",
            re.IGNORECASE,
        ),
        # Reverse pattern: verb + role descriptor
        # "says a policy staffer", "says an employee who works on Instagram"
        re.compile(
            r"\b(?:" + verb_alternation + r")"
            r"\s+((?:an?|the|one|another)"
            r" (?:[A-Za-z]+[ -])?"
            r"(?:[A-Za-z]+[ -])?"
            r"(?:worker|employee|staffer|engineer|executive|official|leader|manager|person|researcher|analyst|source|spokesperson|spokeswoman|spokesman)"
            r"(?:\s+(?:who\s+works?\s+(?:on|at|in|for)\s+\w+|at\s+\w+|inside\s+\w+))?)",
            re.IGNORECASE,
        ),
        # "People who requested/declined/asked for anonymity"
        re.compile(
            r"\b(?:people|persons|individuals|sources?) who (?:requested|declined|asked for|demanded|insisted on) anonymity\b",
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
        # "[number] employees/sources with knowledge of" — "two employees with knowledge of the matter"
        # Variant of above that catches "with knowledge of" qualifier
        re.compile(
            r"(?<![,\d])\b(?:\d{1,3}|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|sixteen|twenty|dozen)"
            r"\s+(?:current\s+(?:and\s+)?(?:former\s+)?)?"
            r"(?:workers|employees|staffers|engineers|executives|officials|sources|people|persons?)"
            r"\s+with\s+(?:direct\s+)?knowledge\s+of\b",
            re.IGNORECASE,
        ),
        # "one person/employee familiar with" — singular counted source with "familiar with" qualifier
        # Catches: "one person familiar with the plans", "one employee familiar with the discussions"
        re.compile(
            r"\bone (?:person|employee|source|official|executive|staffer|engineer|worker)"
            r" (?:familiar with|with knowledge of|close to|briefed on)\b",
            re.IGNORECASE,
        ),
        # "several people say" — quantifier + generic people noun + verb
        # Verb is REQUIRED to prevent false positives from editorial
        # narration like "Many people are still concerned" (no attribution).
        re.compile(
            r"\b(?:some|several|multiple|many|numerous|various|a few|a handful of|a number of)"
            r" (?:current\s+(?:and\s+)?(?:former\s+)?)?"
            r"(?:workers|employees|staffers|engineers|people|sources|individuals)"
            r"\s+(?:" + verb_alternation + r")\b",
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
        # Internal document / memo as anonymous source — the leaked document
        # is attributed but whoever provided it is unnamed.  Common in enterprise
        # reporting: "according to internal documents", "an internal memo warned",
        # "confirmed by multiple sources".
        re.compile(
            r"\b(?:according to|viewed by|obtained by|reviewed by|seen by)\s+"
            r"(?:an?\s+)?internal\s+"
            r"(?:documents?|memos?|emails?|guidelines?|presentations?|reports?|briefings?)",
            re.IGNORECASE,
        ),
        re.compile(
            r"\binternal\s+(?:documents?|memos?|emails?|guidelines?|presentations?|reports?|briefings?)\s+"
            r"(?:obtained|reviewed|seen|viewed|shared|circulated|warned|instructed|showed|stated|revealed|indicated)",
            re.IGNORECASE,
        ),
        re.compile(r"\bconfirmed by multiple sources\b", re.IGNORECASE),
        re.compile(
            r"\b(?:reported|confirmed)\s+by\s+(?:The\s+)?[A-Z]\w+\s+and\s+confirmed\s+by\s+multiple\s+sources\b",
            re.IGNORECASE,
        ),
    ]

    # No-comment / declined-to-comment patterns — signals the entity chose not
    # to provide its side.  These are NOT anonymous sources; they are editorial
    # signals about the target entity's engagement with the reporter.
    no_comment_patterns: list[re.Pattern] = [
        re.compile(
            r"\b(?:did not|declined to|chose not to|refused to|would not|couldn't)"
            r" (?:immediately )?"
            r"(?:respond|comment|reply|return|answer|provide)"
            r"(?: to)?"
            r"(?: (?:a|the|our|multiple))?"
            r"(?: (?:request|call|email|query|inquiry|message|questions?))?",
            re.IGNORECASE,
        ),
    ]

    for pat in anon_patterns:
        for m in pat.finditer(text):
            # Use captured group(1) if available (strips trailing verb),
            # otherwise fall back to full match.
            try:
                descriptor = (m.group(1) or m.group()).strip()
            except IndexError:
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
                source_type="anonymous",
            ))

    # Detect no-comment signals separately — tagged as source_type="no_comment"
    # so they can be excluded from source counts and stance analysis.
    # Extract the entity name from the subject preceding the refusal verb,
    # rather than using the refusal phrase itself as the source name.
    _NO_COMMENT_SUBJECT_RE = re.compile(
        r"\b([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+)*)\s+"
        r"(?:did not|declined to|chose not to|refused to|would not|couldn't)",
    )
    for pat in no_comment_patterns:
        for m in pat.finditer(text):
            # Try to extract the entity name from the sentence subject
            # by looking at the 80 chars before the match.
            pre_ctx = text[max(0, m.start() - 80):m.end()]
            subj_m = _NO_COMMENT_SUBJECT_RE.search(pre_ctx)
            if subj_m:
                entity_name = subj_m.group(1).strip()
            else:
                entity_name = m.group().strip()
            if entity_name.lower() in {n.lower() for n in seen_names}:
                continue
            seen_names.add(entity_name)

            sources.append(SourceMention(
                name=entity_name,
                is_anonymous=False,
                is_expert=False,
                affiliation="",
                quote="",
                attribution_verb="",
                source_type="no_comment",
            ))

    # Pattern 7: Group expert sources — named collective groups whose
    # individual members are not named but whose professional identity
    # gives them expert authority.  Examples:
    # - "cybersecurity experts have said as much in an open letter"
    # - "leading AI researchers argued in a joint statement"
    # - "top economists wrote in a letter to Congress"
    # These are NOT anonymous (the group identity is public and carries
    # authority) and NOT individual named sources.  source_type="group_expert".
    _EXPERT_GROUP_NOUNS = (
        r"(?:cybersecurity|security|AI|machine[ -]learning|climate|privacy|"
        r"nuclear|bioethics?|public[ -]health|economics?|legal|policy|"
        r"national[ -]security|computer[ -]science|data[ -]science|"
        r"technology|human[ -]rights|civil[ -](?:rights|liberties))"
        r"\s+"
        r"(?:experts?|researchers?|scientists?|scholars?|analysts?|"
        r"specialists?|professionals?|academics?|authorities|fellows?|"
        r"advisers?|advisors?)"
    )
    group_expert_patterns: list[re.Pattern] = [
        # "[adjective] [domain] experts have said/argued/warned/wrote"
        re.compile(
            rf"\b(?:leading|top|prominent|senior|independent|renowned|noted|respected|"
            rf"former|veteran)?\s*{_EXPERT_GROUP_NOUNS}"
            rf"\s+(?:have\s+)?(?:{verb_alternation})"
            rf"(?:\s+(?:as much|similarly|likewise|that|in))?\b",
            re.IGNORECASE,
        ),
        # "[domain] experts ... in an open letter / joint statement / letter to"
        re.compile(
            rf"\b(?:leading|top|prominent|senior|independent|renowned|noted|respected|"
            rf"former|veteran)?\s*{_EXPERT_GROUP_NOUNS}"
            rf"[^.{{0,80}}]"
            rf"(?:in (?:a|an|the|their)\s+"
            rf"(?:open\s+letter|joint\s+statement|letter\s+to|petition|report|"
            rf"white\s+paper|brief|amicus\s+brief|public\s+letter|"
            rf"signed\s+letter|statement|declaration|communiqu[eé]))\b",
            re.IGNORECASE,
        ),
        # "an open letter signed by [N] [domain] experts/researchers"
        re.compile(
            r"\b(?:an?\s+)?(?:open\s+letter|joint\s+statement|petition|letter)"
            r"\s+(?:signed\s+)?by\s+"
            r"(?:\d+|many|several|dozens?\s+of|hundreds?\s+of|a\s+group\s+of)?\s*"
            rf"(?:leading|top|prominent|senior)?\s*{_EXPERT_GROUP_NOUNS}\b",
            re.IGNORECASE,
        ),
    ]

    for pat in group_expert_patterns:
        for m in pat.finditer(text):
            descriptor = m.group().strip()
            # Deduplicate
            if descriptor.lower() in {n.lower() for n in seen_names}:
                continue
            seen_names.add(descriptor)

            ctx_start = max(0, m.start() - 100)
            ctx_end = min(len(text), m.end() + 200)
            context = text[ctx_start:ctx_end]

            sources.append(SourceMention(
                name=descriptor,
                is_anonymous=False,
                is_expert=True,
                affiliation="",
                quote=_extract_nearby_quote(text, m.start(), m.end()),
                attribution_verb=_find_attribution_verb(context),
                source_type="group_expert",
            ))

    # Pattern 8: Collective research attribution — "the team wrote",
    # "researchers explained", "the authors noted".  Common in science
    # and technology journalism where a research group or paper's authors
    # are cited collectively.  Tagged source_type="collective_research".
    collective_research_patterns: list[re.Pattern] = [
        # "the [research] team/researchers/authors/group verb"
        re.compile(
            rf"\b(?:the\s+)(?:research\s+)?(?:team|researchers|group|authors?)\s+"
            rf"(?:(?:also|further|additionally|later)\s+)?"
            rf"({verb_alternation})\b",
            re.IGNORECASE,
        ),
        # "verb the [research] team/researchers/authors"
        re.compile(
            rf"\b({verb_alternation})\s+"
            rf"(?:the\s+)(?:research\s+)?(?:team|researchers|group|authors?)\b",
            re.IGNORECASE,
        ),
    ]

    for pat in collective_research_patterns:
        for m in pat.finditer(text):
            descriptor = m.group().strip()
            if descriptor.lower() in {n.lower() for n in seen_names}:
                continue
            seen_names.add(descriptor)

            verb = m.group(1).strip().lower()
            ctx_start = max(0, m.start() - 100)
            ctx_end = min(len(text), m.end() + 200)
            context = text[ctx_start:ctx_end]

            sources.append(SourceMention(
                name=descriptor,
                is_anonymous=False,
                is_expert=False,
                affiliation=_extract_affiliation(context),
                quote=_extract_nearby_quote(text, m.start(), m.end()),
                attribution_verb=verb,
                source_type="collective_research",
            ))

    # Pattern 6: Organizational sources — "Meta said", "Google confirmed",
    # "the company said in a statement", "a spokesperson told Reuters"
    # These are named non-anonymous sources where the speaker is an entity
    # rather than a person.  They are important for stance analysis because
    # company statements often represent the target entity's official position.
    org_source_patterns: list[re.Pattern] = [
        # "[Company] said/told/confirmed in [a statement/an emailed response]"
        re.compile(
            rf"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)"
            rf"\s+({verb_alternation})"
            rf"\s+(?:in (?:a|an|the|its)\s+(?:statement|emailed? (?:response|statement|comment)|"
            rf"blog post|press release|filing|report|letter|memo|announcement))\b",
        ),
        # "[Company] said/told/reported" — direct organizational attribution
        # without requiring "in a statement" qualifier.  Validated against
        # _KNOWN_ORGS below to prevent false positives from person surnames.
        re.compile(
            rf"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)"
            rf"\s+({verb_alternation})\b",
        ),
        # "a [Company] spokesperson/representative said/told"
        # Use [Aa]n? instead of an? to match sentence-initial "A Meta spokesperson said"
        re.compile(
            rf"\b[Aa]n?\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\s+"
            rf"(?:spokesperson|spokeswoman|spokesman|representative|official)\s+"
            rf"({verb_alternation})\b",
        ),
        # "[Company] spokesperson [Name] said" — skip if name already captured
        re.compile(
            rf"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\s+"
            rf"(?:spokesperson|spokeswoman|spokesman)\s+"
            rf"[A-Z][a-z]+ [A-Z][a-z]+\b",
        ),
    ]

    # Known tech company names to validate organizational matches
    _KNOWN_ORGS = {
        "meta", "google", "apple", "microsoft", "amazon", "openai",
        "anthropic", "nvidia", "tesla", "spacex", "x", "twitter",
        "alphabet", "ibm", "oracle", "palantir", "samsung",
        "instagram", "snapchat", "snap", "tiktok", "youtube",
        "bytedance", "reddit", "pinterest", "discord", "spotify",
        "netflix", "uber", "lyft", "airbnb", "stripe", "shopify",
        "reuters", "bloomberg",
        "alibaba", "baidu", "tencent", "huawei", "xiaomi",
    }

    for pat in org_source_patterns:
        for m in pat.finditer(text):
            org_name = m.group(1).strip()
            # Only match if it looks like an organization name
            if org_name.lower() not in _KNOWN_ORGS:
                # Also allow if followed by spokesperson-type words
                continue
            if org_name.lower() in {n.lower() for n in seen_names}:
                continue
            seen_names.add(org_name)

            verb = m.group(2).strip().lower() if m.lastindex >= 2 else ""
            ctx_start = max(0, m.start() - 100)
            ctx_end = min(len(text), m.end() + 200)
            context = text[ctx_start:ctx_end]

            sources.append(SourceMention(
                name=org_name,
                is_anonymous=False,
                is_expert=False,
                affiliation=org_name,
                quote=_extract_nearby_quote(text, m.start(), m.end()),
                attribution_verb=verb,
                source_type="organizational",
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

    # Filter out no_comment signals — they are not sources and should
    # not count toward adversarial/supportive/neutral tallies
    sources = [s for s in sources if getattr(s, "source_type", "named") != "no_comment"]

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

        # --- Spokesperson / Executive-by-role detection ---
        # Named spokesperson sources (e.g. "Meta spokesperson Tracy Clayton")
        # are inherently supportive of the entity they represent — that's
        # their job function.  Classify as supportive unless the quote
        # contains strong adversarial language (rare whistleblower edge case).
        # This prevents PR/communications statements ("safeguards in place",
        # "data is not used for any other purpose") from being coded as
        # neutral when they are clearly defensive of the entity.
        #
        # C-suite executives (CTO, CEO, CFO, etc.) quoted defending or
        # explaining their company's position are similarly supportive by
        # role.  Their quotes often contain negative *domain* terms
        # ("risk", "opt-out", "leak") that they are *denying* or
        # *downplaying*, which tricks pure term-counting into adversarial.
        # Treat them like spokespersons: supportive unless overwhelmingly
        # adversarial (3+ negative terms = possible whistleblower/dissident).
        is_spokesperson = False
        if not source.is_anonymous:
            source_context = (source.name + " " + source.affiliation).lower()
            _SPOX_TITLES = (
                "spokesperson", "spokesman", "spokeswoman",
                "communications director", "press secretary",
                "media representative", "pr representative",
                "public relations",
                "vice president of communications",
                "vp of communications",
                "head of communications",
                "chief communications officer",
                "director of communications",
                "communications chief",
            )
            _EXECUTIVE_TITLES = (
                "chief executive officer", "chief technology officer",
                "chief financial officer", "chief operating officer",
                "chief product officer", "chief marketing officer",
                "chief information officer", "chief legal officer",
                "chief revenue officer", "chief strategy officer",
                "chief people officer", "chief human resources officer",
                "chief data officer", "chief science officer",
                "chief ai officer",
                "ceo", "cto", "cfo", "coo", "cpo", "cmo", "cio", "clo",
                "president", "vice president", "senior vice president",
                "executive vice president", "evp", "svp",
                "vp of", "head of", "director of",
                "general counsel", "managing director",
            )
            is_spokesperson = any(
                term in source_context or term in context_text
                for term in _SPOX_TITLES
            )
            # Check executive titles only if not already matched as spox
            if not is_spokesperson:
                is_spokesperson = any(
                    term in source_context or term in context_text
                    for term in _EXECUTIVE_TITLES
                )
            # Also search full article text for "[title] ... [Name]" or
            # "[Name], a/the [title]" patterns — the affiliation field
            # may not capture the spokesperson/executive descriptor.
            if not is_spokesperson and full_text:
                name_parts = source.name.strip().split()
                last_name = name_parts[-1].lower() if name_parts else ""
                full_name_lower = source.name.strip().lower()
                if last_name:
                    ft_lower = full_text.lower()
                    all_role_titles = _SPOX_TITLES + _EXECUTIVE_TITLES
                    for title in all_role_titles:
                        # "[title] [FirstName] [LastName]" or "[title] [LastName]"
                        if (
                            f"{title} {full_name_lower}" in ft_lower
                            or f"{title} {last_name}" in ft_lower
                            or f"{last_name}, a {title}" in ft_lower
                            or f"{last_name}, the {title}" in ft_lower
                            or f"{last_name}, {title}" in ft_lower
                        ):
                            is_spokesperson = True
                            break
                    # Possessive pattern: "[Name], [Org]'s [title]"
                    # e.g. "Andy Stone, Meta's vice president of communications"
                    # e.g. "Andrew Bosworth, Meta's chief technology officer"
                    if not is_spokesperson:
                        for title in all_role_titles:
                            # Match "[name], <any org>'s [title]"
                            poss_pattern = re.compile(
                                rf"{re.escape(last_name)},\s+\w+[''']s\s+{re.escape(title)}",
                                re.IGNORECASE,
                            )
                            if poss_pattern.search(ft_lower):
                                is_spokesperson = True
                                break

        if is_spokesperson and neg_count < 3:
            # Spokesperson classified as supportive unless overwhelmingly
            # adversarial (3+ negative terms = possible whistleblower)
            supportive.append(source.name)
        elif neg_count > pos_count:
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
