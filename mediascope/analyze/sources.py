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
    "quotes", "cites",  # present-tense third-party attribution
    "thinks", "believes", "considers",  # cognitive/opinion attribution
    "cautions",  # hedged warning attribution
    "quoted", "citing", "cited",  # third-party attribution verbs
    "estimated", "estimates",  # quantitative attribution — "Analysts with SemiAnalysis estimated"
    "projected", "projects",  # forecast attribution — "analysts projected"
    "calculated", "calculates",  # analytical attribution
    "forecast", "forecasts",  # prediction attribution
    "assessed", "assesses",  # evaluation attribution
    "valued", "values",  # valuation attribution
    "rated", "rates",  # rating attribution
    "upgraded", "downgrades", "downgraded", "upgrades",  # analyst rating changes
    "stuck",  # "stuck by" — maintaining a position/rating
    "maintained", "maintains",  # position maintenance — "maintained a hold rating"
    "reiterated", "reiterates",  # reaffirmation — "reiterated a buy rating"
    "initiated", "initiates",  # coverage initiation — "initiated coverage with"
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

# Compound negative attribution phrases — multi-word constructions that
# carry loaded framing through contrastive or failure semantics.
# These are checked before single-word verb lookup because they would
# otherwise match only the neutral verb component (e.g., "attempted"
# alone is neutral, but "attempted yet failed" is loaded).
# Patterns are lowercase and matched case-insensitively.
COMPOUND_LOADED_PHRASES: list[str] = [
    # Contrastive failure: subject tried and failed
    "attempted yet failed",
    "attempted but failed",
    "tried and failed",
    "tried but failed",
    "sought but was denied",
    "sought but was rejected",
    "pushed back but was rejected",
    "pushed back but was overruled",
    "argued but was overruled",
    "argued but the court rejected",
    "appealed but was denied",
    "appealed but lost",
    "fought but lost",
    "fought but was defeated",
    "promised but failed",
    "promised but did not deliver",
    "pledged but failed",
    "vowed but failed",
    # Contrastive concession: grudging/forced compliance
    "was forced to admit",
    "was forced to concede",
    "was compelled to acknowledge",
    "grudgingly acknowledged",
    "grudgingly admitted",
    "reluctantly acknowledged",
    "reluctantly admitted",
    "reluctantly conceded",
    "quietly admitted",
    "quietly conceded",
    "finally admitted",
    "finally acknowledged",
    "finally conceded",
    "belatedly acknowledged",
    "belatedly admitted",
    # Defensive failure: defence collapsed
    "denied but was found",
    "denied but evidence showed",
    "claimed but was contradicted",
    "insisted but was overruled",
    "maintained but the court found",
]


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
    "creative artists agency", "caa",
    "electronic frontier foundation", "eff",
    # Entertainment/labor unions
    "sag-aftra", "wga", "dga", "iatse",
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
    # Political/governmental titles — these are titles, not first names.
    # "Governor Jeff" (from "Governor Jeff Landry") would match the
    # "[A-Z][a-z]+ [A-Z][a-z]+" name pattern.  Discovered in MIT Tech
    # Review Louisiana natural gas article (Jul 2026).
    "Governor", "Senator", "Representative", "Mayor", "Chairman",
    "Chairwoman", "Secretary", "Commissioner", "Councilman",
    "Councilwoman", "Alderman", "Sheriff", "Marshal",
    "Ambassador", "Minister", "Magistrate",
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
    # Common capitalized nouns that start sentences and false-positive when
    # followed by a verb that doubles as an attribution verb (e.g. "charges").
    # Discovered in Reuters Rust Belt data centers article (Jul 2026):
    # "Capacity charges at..." mis-parsed "Capacity" as a named source.
    "Capacity", "Manufacturing", "Production", "Infrastructure",
    "Electricity", "Technology", "Industry",
    # Abstract nouns that open editorial paragraphs — "Balance demands
    # acknowledging..." should not extract "Balance" as a source name.
    # Discovered in TechCentral smart glasses article (Jul 14, 2026).
    "Balance", "Transparency", "Privacy", "Security", "Safety",
    "Progress", "Innovation", "Regulation", "Accountability",
    "Evidence", "History", "Experience", "Research", "Analysis",
    # Number words — "Four states are asking" should not extract "Four" as
    # a source name; quantifiers starting sentences are common in journalism.
    # Discovered in Barron's Meta $1T backlash article (Jul 10, 2026):
    # "Four states—California, Colorado, New Jersey, and Kentucky—are
    # asking the court" mis-parsed "Four" as a named source.
    "One", "Two", "Three", "Four", "Five", "Six", "Seven",
    "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
    "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
    "Nineteen", "Twenty", "Thirty", "Forty", "Fifty",
    "Sixty", "Seventy", "Eighty", "Ninety", "Hundred",
    "Thousand", "Million", "Billion", "Trillion",
    "Dozens", "Hundreds", "Thousands", "Millions", "Billions",
    # "New" prevents "New Jersey" / "New Mexico" / "New Zealand" from
    # having "New" extracted as a source first-word.
    "New",
    # Corporate title words — "Vice President said" should not parse "Vice"
    # as a first name.  Discovered in Washington Examiner Meta Louisiana
    # data center article (Jul 13, 2026): "Meta Vice President of Data
    # Centers Rachel Peterson said" → Pattern 0c mis-parsed "Vice President"
    # as a person name with affiliation "Data Centers Rachel Peterson".
    "Vice", "Deputy", "Associate", "Executive", "Managing",
    "Senior", "Junior", "Chief", "Assistant", "Acting",
    "Interim", "Former", "Emeritus",
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
    # Product/feature names that match "First Last" name pattern
    # Discovered in TechCentral smart glasses article (Jul 14, 2026):
    # "internally called Name Tag" → "Name Tag" false-positived as a source
    # via "called" attribution verb.
    "Name Tag",
    # AI model / product names that look like "First Last"
    "Muse Spark", "Muse Image", "Muse Video",
    "Llama Scout", "Llama Maverick",
    "Google Gemini", "Apple Intelligence",
    # Book/media titles that look like "First Last"
    "Careless People", "Brave New", "Dark Web",
    "Social Dilemma", "Social Network", "Deep State",
    # Government agency / regulatory body partial names
    "Relations Board", "Labor Relations", "National Labor",
    "Trade Commission", "Federal Trade", "Federal Communications",
    "Securities Exchange", "Exchange Commission",
    # Generic descriptive phrases that look like source names
    # but are subject references inside indirect speech
    "the young person", "the young people", "the young user",
    "the young users", "the child user", "the child users",
    "the teen user", "the teen users", "the adult user",
    # Publication names that match "First Last" name pattern
    "Business Insider", "Tech Review", "Technology Review",
    "Daily Beast", "Daily Mail", "Morning Post",
    "Evening Standard",
    # TV / digital media publication names — "told Fox Business" is a
    # publication self-reference, not a human source.  Discovered in
    # Fox Business Meta AI layoff discrimination article (Jul 14, 2026).
    "Fox Business", "Fox News", "Fox Corp",
    "USA Today", "Daily Caller", "Daily Wire",
    "Sky News", "Sky Business",
    # Government / institutional names that match "First Last"
    "White House",
    # Partial organization names that truncate from longer names
    # Discovered in MIT Tech Review Louisiana natural gas article (Jul 2026):
    # "Harvard Law School" → "Law School", "Alliance for Affordable Energy" → "Affordable Energy"
    "Law School", "Affordable Energy", "Concerned Scientists",
    "Environmental Law", "Power Research", "Gas Plants",
    "Public Service", "Service Commission",
    # Discovered in Reuters Rust Belt data centers article (Jul 2026):
    # "Industrial Energy Consumers of America" → "Energy Consumers"
    "Energy Consumers", "Synergy Research", "Smart Electric",
    "Electric Power", "Smart Electric Power",
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
    quote_count: int = 1        # Number of distinct attribution instances


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
        # Pattern -1 (HIGHEST priority): "[Org]'s [Person Name] verb"
        # Handles the journalism pattern "Nvidia's Jensen Huang said",
        # "Anthropic's Dario Amodei said", "OpenAI's Sam Altman said".
        # Returns just the org name, not "Org's Person Name".
        # Must fire before Pattern 1 ("of/at/from [Org]") which can match
        # unrelated phrases from the context window.
        re.compile(
            r"([A-Z][A-Za-z]+)['\u2019]s\s+"
            r"[A-Z][a-z]+\s+[A-Z][a-z]+\s+"
            r"(?:said|told|added|noted|explained|argues|warned|recalled|"
            r"acknowledged|revealed|claimed|contended|suggested|reported|"
            r"confirmed|insisted|reiterated|predicts|believes|stressed|"
            r"emphasized|stated|says|declined|maintains|asserted|countered|"
            r"testified|responded|disclosed|conceded|admitted|objected)",
        ),
        # Pattern 0 (most specific): "[Organization]'s CEO/president/director/etc."
        # Must be tried first — prevents false positives from the broader
        # "of [Organization]" pattern that can match junk from context window.
        # E.g., "Meta's vice president of communications" should extract "Meta",
        # not "NameTag system into the Meta AI app" from "portions of the NameTag..."
        re.compile(
            r"([A-Z][" + _INST_CHARS + r"]+?)"
            r"(?:'s|'s|\u2019s)\s+"
            r"(?:(?:[Cc]hief|[Vv]ice|[Dd]eputy|[Ss]enior|[Ee]xecutive|[Aa]ssociate|[Aa]ssistant|[Mm]anaging)\s+)*"
            r"(?:(?:[Tt]echnology|[Ff]inancial|[Oo]perating|[Pp]roduct|[Mm]arketing|[Ii]nformation|[Ll]egal|[Rr]evenue|[Ss]trategy|"
            r"[Ss]cience|[Dd]ata|[Cc]ommunications?|[Cc]reative|[Ee]ditorial|[Cc]ontent|[Pp]olicy|[Ee]ngineering|[Rr]esearch|[Dd]esign|"
            r"[Ii]ndustrial|[Ee]nvironmental|[Ss]ustainability|[Ff]acilities|[Oo]perations|[Hh]uman\s+[Rr]esources)\s+)*"
            r"(?:CEO|[Pp]resident|[Oo]fficer|[Dd]irector|[Cc]hief|[Hh]ead|[Ss]pokesperson|[Ee]ditor|[Cc]ounsel)",
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
            r"\s+(?:(?:[Cc]hief|[Vv]ice|[Dd]eputy|[Ss]enior|[Ee]xecutive|[Aa]ssociate|[Aa]ssistant|[Mm]anaging|[Ff]ormer|[Aa]cting)\s+)*"
            r"(?:(?:[Tt]echnology|[Ff]inancial|[Oo]perating|[Pp]roduct|[Mm]arketing|[Ii]nformation|[Ll]egal|[Rr]evenue|[Ss]trategy|"
            r"[Ss]cience|[Dd]ata|[Cc]ommunications?|[Cc]reative|[Ee]ditorial|[Cc]ontent|[Pp]olicy|[Ee]ngineering|[Rr]esearch|[Dd]esign|"
            r"[Ii]ndustrial|[Ee]nvironmental|[Ss]ustainability|[Ff]acilities|[Oo]perations|[Hh]uman\s+[Rr]esources)\s+)*"
            r"(?:CEO|CTO|CFO|COO|CMO|CIO|CISO|CSO|"
            r"[Oo]fficer|[Dd]irector|[Pp]resident|[Cc]ounsel|[Ss]pokesperson|[Ss]pokesman|[Ss]pokeswoman|[Ee]ditor|[Ss]ecretary|"
            r"[Mm]anager|[Hh]ead|[Ee]xecutive)\s+[A-Z]",
            re.DOTALL,
        ),
        # Pattern 0e: "[Organization] analyst/researcher/fellow/professor [Name]"
        # Handles "Bernstein Research analyst Madison Rezaei says" where
        # the org precedes a role noun without a preposition.
        re.compile(
            r"([A-Z][" + _INST_CHARS + r"]{1,40}?)"
            r"\s+(?:analyst|researcher|fellow|professor|scholar|economist|"
            r"strategist|correspondent|reporter|columnist|commentator|"
            r"editor|contributor|scientist)\s+"
            r"[A-Z][a-z]",
        ),
        # Pattern 0f: "title of [the] [descriptor words] [Organization]"
        # Handles "president of the trade group Industrial Energy Consumers
        # of America" where lowercase descriptors sit between "of the" and
        # the actual org name.  Captures from the first capital letter after
        # the descriptors through to a sentence boundary.
        # Discovered in Reuters Rust Belt data centers article (Jul 2026).
        re.compile(
            r"(?:[Pp]resident|[Dd]irector|CEO|[Cc]hairman|[Cc]hairwoman|"
            r"[Cc]hairperson|[Hh]ead|[Cc]hief|[Ff]ounder|[Cc]o-founder|"
            r"[Ss]ecretary|[Tt]reasurer|[Mm]anager|[Cc]oordinator|"
            r"[Cc]ounsel|[Aa]ttorney|[Aa]dvocate|[Ee]xecutive|[Oo]fficer|"
            r"[Vv]ice\s+[Pp]resident)"
            r"\s+(?:of|for|at)\s+(?:the\s+)?"
            r"(?:[a-z][\w-]*\s+){0,4}"  # up to 4 lowercase descriptor words
            r"([A-Z][" + _INST_CHARS + r"]{1,80}?)"
            r"(?:[,.\n]|\s+(?:" + "|".join([
                "said", "told", "who", "says", "tells", "noted", "notes",
                "agrees", "adds", "added", "explained", "explains",
                "confirmed", "warned", "argues", "recalled", "reported",
            ]) + r"))",
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
            if m.lastindex and m.lastindex >= 2:
                # Possessive pattern (Pattern 2): combine "Georgetown" + "Center for ..."
                aff = m.group(1).strip() + "'s " + m.group(2).strip()
            else:
                aff = m.group(1).strip()
            # Filter out generic words, overly short matches, and title
            # words that Pattern 0b can false-positive on.  "Chief Executive
            # Mark Zuckerberg" → Pattern 0b captures "Chief" as org, but
            # "Chief" is a title prefix, not an organization.  Discovered in
            # WSJ Meta smartglasses privacy article (Jul 2026).
            _TITLE_FALSE_POS = {
                "Chief", "Vice", "Deputy", "Senior", "Executive",
                "Associate", "Assistant", "Managing", "Former", "Acting",
            }
            if len(aff) > 2 and aff not in {"The", "A", "An", "This", "That"} and aff not in _TITLE_FALSE_POS:
                return aff
    return ""


def _find_attribution_verb(context: str) -> str:
    """Find the attribution verb in a context string.

    Checks compound loaded phrases first (multi-word patterns like
    "attempted yet failed"), then single-word verbs.
    """
    context_lower = context.lower()
    # Check compound loaded phrases first — longer, more specific match
    for phrase in COMPOUND_LOADED_PHRASES:
        if phrase in context_lower:
            return phrase
    # Fall back to single-word verb search
    for verb in sorted(ALL_VERBS, key=len, reverse=True):
        pattern = re.compile(rf"\b{re.escape(verb)}\b", re.IGNORECASE)
        if pattern.search(context_lower):
            return verb
    return ""


def _extract_direct_possessive(text: str, name_start: int) -> str:
    """Check for '[Org]'s' immediately before a source name in the full text.

    Handles the common journalism pattern: "Nvidia's Jensen Huang said".
    Returns just the org name (e.g. "Nvidia") or empty string if no match.

    This is more precise than _extract_affiliation because it uses the
    exact position of the source name in the original text, not a context
    window that may include other possessives from adjacent sentences.
    """
    # Look back up to 40 chars before the name for "[Org]'s "
    lookback_start = max(0, name_start - 40)
    lookback = text[lookback_start:name_start]
    m = re.search(
        r"([A-Z][A-Za-z]+)['\u2019]s\s+$",
        lookback,
    )
    if m:
        return m.group(1).strip()
    return ""


def _is_expert_full_text(text: str, name: str) -> bool:
    """Search all occurrences of *name* in *text* for expert titles.

    When a source is referred to by surname only (e.g. "Bengio says"),
    the narrow context window around that match may not include the
    expert credential from their earlier introduction.  This function
    finds every occurrence of the name in the full text and checks a
    wider window (300 chars each side) for expert titles.
    """
    for m in re.finditer(re.escape(name), text):
        ctx_start = max(0, m.start() - 300)
        ctx_end = min(len(text), m.end() + 300)
        ctx = text[ctx_start:ctx_end]
        if _is_expert_by_title(ctx):
            return True
    return False


def _extract_affiliation_full_text(text: str, name: str) -> str:
    """Search all occurrences of *name* in *text* for affiliations.

    Complement to _is_expert_full_text: finds the affiliation from the
    source's earlier introduction when the immediate context window is
    too narrow.  Uses a forward-biased window (50 chars before, 300
    after) so the matched affiliation is more likely to belong to *name*
    rather than a preceding person's attribution.
    """
    for m in re.finditer(re.escape(name), text):
        # Forward-biased: only 50 chars lookback to avoid cross-source
        # contamination (e.g. preceding "Gabriel, ... at Google DeepMind"
        # bleeding into a Bengio lookup), but 300 chars forward where
        # the appositive "a professor at X" typically appears.
        ctx_start = max(0, m.start() - 50)
        ctx_end = min(len(text), m.end() + 300)
        ctx = text[ctx_start:ctx_end]
        aff = _extract_affiliation(ctx)
        if aff:
            return aff
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

    # Pattern 0: "Title First Last verb" — titled source with attribution verb
    # Catches "Governor Jeff Landry declared", "Senator Sheldon Whitehouse issued",
    # "Chairman Jay Powell said".  Must run before Pattern 1 to capture the
    # full three-word name instead of truncating to "Governor Jeff".
    # Discovered in MIT Tech Review Louisiana natural gas article (Jul 2026).
    _TITLE_PREFIXES = (
        "Governor", "Senator", "Representative", "Mayor", "Chairman",
        "Chairwoman", "Secretary", "Commissioner", "Sheriff",
        "Ambassador", "Minister", "Magistrate", "Justice",
        "Councilman", "Councilwoman", "Alderman", "Marshal",
    )
    _title_alt = "|".join(_TITLE_PREFIXES)
    titled_before_verb = re.compile(
        rf"\b((?:{_title_alt})\s+[A-Z][a-z]+\s+[A-Z][a-z]+(?:-[A-Z][a-z]+)?)\s+({verb_alternation})\b",
    )
    for m in titled_before_verb.finditer(text):
        name = m.group(1).strip()
        verb = m.group(2).strip().lower()
        if name in seen_names:
            continue
        seen_names.add(name)

        ctx_start = max(0, m.start() - 100)
        ctx_end = min(len(text), m.end() + 100)
        context = text[ctx_start:ctx_end]

        sources.append(SourceMention(
            name=name,
            is_anonymous=False,
            is_expert=_is_expert_by_title(context) or _is_expert_full_text(text, name),
            affiliation=_extract_affiliation_full_text(text, name) or _extract_affiliation(context),
            quote=_extract_nearby_quote(text, m.start(), m.end()),
            attribution_verb=verb,
        ))

    # Pattern 0b: "verb Title First Last" — reverse titled source
    # Catches '"A game changer," declared Governor Jeff Landry' where the
    # verb precedes the titled name.
    verb_before_titled = re.compile(
        rf"\b({verb_alternation})\s+((?:{_title_alt})\s+[A-Z][a-z]+\s+[A-Z][a-z]+(?:-[A-Z][a-z]+)?)\b",
    )
    for m in verb_before_titled.finditer(text):
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

    # Pattern 0c: "First Last of Organization VERB" — named source with
    # affiliation separated by "of".  Must run BEFORE Pattern 1 so that the
    # person name is added to ``seen_names`` and the organization name
    # (e.g. "KeyBanc Capital") is not later misidentified as a person.
    # Discovered in WSJ AI spending article (Jul 8, 2026): "Justin
    # Patterson of KeyBanc Capital said" was parsed as person "Capital".
    name_of_org_verb = re.compile(
        rf"\b([A-Z][a-z]+\s+(?:[A-Z]\.\s+)?[A-Z][a-z]+(?:-[A-Z][a-z]+)?)"
        rf"\s+of\s+"
        rf"([A-Z][\w&.]+(?:\s+[A-Z][\w&.]+){{0,4}})"
        rf"\s+({verb_alternation})\b",
    )
    for m in name_of_org_verb.finditer(text):
        name = m.group(1).strip()
        org = m.group(2).strip()
        verb = m.group(3).strip().lower()
        if name in seen_names:
            continue

        first_word = name.split()[0]
        if first_word in _NAME_STOP_FIRST_WORDS:
            continue
        if name in _NAME_STOP_NAMES:
            continue

        seen_names.add(name)
        # Also mark the org name as seen so Pattern 1 won't pick it up
        seen_names.add(org)

        ctx_start = max(0, m.start() - 100)
        ctx_end = min(len(text), m.end() + 100)
        context = text[ctx_start:ctx_end]

        sources.append(SourceMention(
            name=name,
            is_anonymous=False,
            is_expert=_is_expert_by_title(context) or _is_expert_full_text(text, name),
            affiliation=org,
            quote=_extract_nearby_quote(text, m.start(), m.end()),
            attribution_verb=verb,
        ))

    # Pattern 0d: "VERB First Last of Organization" — reverse of 0c.
    # Handles "wrote Brent Thill of Jefferies" and similar constructions.
    verb_name_of_org = re.compile(
        rf"\b({verb_alternation})\s+"
        rf"([A-Z][a-z]+\s+(?:[A-Z]\.\s+)?[A-Z][a-z]+(?:-[A-Z][a-z]+)?)"
        rf"\s+of\s+"
        rf"([A-Z][\w&.]+(?:\s+[A-Z][\w&.]+){{0,4}})\b",
    )
    for m in verb_name_of_org.finditer(text):
        verb = m.group(1).strip().lower()
        name = m.group(2).strip()
        org = m.group(3).strip()
        if name in seen_names:
            continue

        first_word = name.split()[0]
        if first_word in _NAME_STOP_FIRST_WORDS:
            continue
        if name in _NAME_STOP_NAMES:
            continue

        seen_names.add(name)
        seen_names.add(org)

        ctx_start = max(0, m.start() - 100)
        ctx_end = min(len(text), m.end() + 100)
        context = text[ctx_start:ctx_end]

        sources.append(SourceMention(
            name=name,
            is_anonymous=False,
            is_expert=_is_expert_by_title(context) or _is_expert_full_text(text, name),
            affiliation=org,
            quote=_extract_nearby_quote(text, m.start(), m.end()),
            attribution_verb=verb,
        ))

    # Pattern 0e: "[Org] analyst/researcher/fellow [First Last] VERB"
    # Handles "Bernstein Research analyst Madison Rezaei says" where the
    # affiliation precedes a role noun and person name without preposition.
    # Must run before Pattern 1 so the org is captured and the person is
    # added to seen_names (preventing Pattern 1 from re-extracting without
    # the affiliation).
    org_role_name_verb = re.compile(
        rf"\b([A-Z][\w&.]+(?:\s+[A-Z][\w&.]+){{0,3}})"
        rf"\s+(?:analyst|researcher|fellow|professor|scholar|economist|"
        rf"strategist|correspondent|reporter|columnist|commentator|"
        rf"editor|contributor|scientist)\s+"
        rf"([A-Z][a-z]+\s+(?:[A-Z]\.\s+)?[A-Z][a-z]+(?:-[A-Z][a-z]+)?)"
        rf"\s+(?:also\s+|recently\s+|previously\s+|separately\s+|further\s+)?"
        rf"({verb_alternation})\b",
    )
    for m in org_role_name_verb.finditer(text):
        org = m.group(1).strip()
        name = m.group(2).strip()
        verb = m.group(3).strip().lower()
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
            is_expert=True,  # Always expert — role noun is an expert title
            affiliation=org,
            quote=_extract_nearby_quote(text, m.start(), m.end()),
            attribution_verb=verb,
        ))

    # Pattern 1: "Name said/told/etc." — named source with attribution verb
    # Supports hyphenated surnames (e.g. "Hadfield-Menell") — discovered in
    # MIT Tech Review AI agents article (Jul 4, 2026 iteration).
    # Allows optional comma before the verb — handles appositive constructions
    # like "Andrew Bosworth, said" (WSJ Meta smartglasses article, Jul 2026).
    named_before_verb = re.compile(
        rf"\b([A-Z][a-z]+ (?:[A-Z]\. )?[A-Z][a-z]+(?:-[A-Z][a-z]+)?),?\s+({verb_alternation})\b",
    )
    for m in named_before_verb.finditer(text):
        name = m.group(1).strip()
        verb = m.group(2).strip().lower()
        if name in seen_names:
            continue

        # Check if this 2-word match is actually the tail of a 3-word org name.
        # Look back for a preceding capitalized word.  E.g. "Creative Artists
        # Agency wrote" matches "Artists Agency" at Pattern 1, but the full org
        # is "Creative Artists Agency".  If the 3-word name (lowered) is in
        # _KNOWN_ORGS_LOWER, skip — the org patterns below will handle it.
        pre_match = text[max(0, m.start() - 30):m.start()]
        _pre_word_m = re.search(r'([A-Z][a-z]+)\s+$', pre_match)
        if _pre_word_m:
            three_word = f"{_pre_word_m.group(1)} {name}"
            if three_word.lower() in _KNOWN_ORGS_LOWER:
                continue

        # Filter out false-positive names where the first word is a common
        # English word that happened to be capitalised at sentence start
        first_word = name.split()[0]
        if first_word in _NAME_STOP_FIRST_WORDS:
            continue
        # Filter out publication/organization partial names
        if name in _NAME_STOP_NAMES:
            continue
        # Filter out names whose last word is an institutional suffix —
        # these are org-name fragments, not person names.  The comma
        # tolerance in the regex can match "Liberties Union, said" from
        # "American Civil Liberties Union, said".  Discovered in WSJ Meta
        # smartglasses privacy article (Jul 2026).
        _INSTITUTIONAL_SUFFIXES = {
            "Union", "League", "Agency", "Association", "Foundation",
            "Institute", "Committee", "Bureau", "Coalition", "Council",
            "Commission", "Corporation", "Company", "Society", "Board",
            "Authority", "Network", "Organization", "Federation",
            "Consortium", "Alliance", "Forum", "Exchange", "Trust",
        }
        last_word = name.split()[-1]
        if last_word in _INSTITUTIONAL_SUFFIXES:
            continue

        seen_names.add(name)

        # Get surrounding context (100 chars each side)
        ctx_start = max(0, m.start() - 100)
        ctx_end = min(len(text), m.end() + 100)
        context = text[ctx_start:ctx_end]

        sources.append(SourceMention(
            name=name,
            is_anonymous=False,
            is_expert=_is_expert_by_title(context) or _is_expert_full_text(text, name),
            affiliation=_extract_direct_possessive(text, m.start()) or _extract_affiliation(context) or _extract_affiliation_full_text(text, name),
            quote=_extract_nearby_quote(text, m.start(), m.end()),
            attribution_verb=verb,
        ))

    # Pattern 2: "said/told/etc. [Name]" — verb before named source
    verb_before_named = re.compile(
        rf"\b({verb_alternation})\s+([A-Z][a-z]+ (?:[A-Z]\. )?[A-Z][a-z]+(?:-[A-Z][a-z]+)?)\b",
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

        # For "verb Name" pattern, the name starts at m.start() of group 2
        name_pos = m.start(2)
        sources.append(SourceMention(
            name=name,
            is_anonymous=False,
            is_expert=_is_expert_by_title(context) or _is_expert_full_text(text, name),
            affiliation=_extract_direct_possessive(text, name_pos) or _extract_affiliation(context),
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
            # For single-name sources, the immediate context (100 chars)
            # may not contain the expert title from the source's earlier
            # full-name introduction.  Search all mentions of the name
            # in the full text for expert titles and affiliations.
            # Discovered in MIT Tech Review AI agents article (Jul 4,
            # 2026): "Bengio says" was not marked as expert because the
            # "professor of computer science" introduction was paragraphs
            # earlier.
            is_expert=_is_expert_by_title(context) or _is_expert_full_text(text, name),
            affiliation=_extract_affiliation(context) or _extract_affiliation_full_text(text, name),
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

    # Pattern 3a: "according to [title/descriptor] [Name]"
    # Handles modifiers between "according to" and the name, e.g.:
    # "According to veteran cybersecurity reporter Brian Krebs"
    # "according to former Meta employee Jane Manchun Wong"
    according_to_titled = re.compile(
        r"\b[Aa]ccording to "
        r"(?:[a-z][\w-]+ ){1,5}"  # 1-5 lowercase descriptor words
        r"([A-Z][a-z]+ (?:[A-Z][a-z]+ )?[A-Z][a-z]+)\b",
    )
    for m in according_to_titled.finditer(text):
        name = m.group(1).strip()
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
            quote="",
            attribution_verb="according to",
        ))

    # Pattern 3b-pre: "per [Source Name]" — compact indirect attribution
    # Common in legal/financial journalism: "per Reuters", "per Bloomberg",
    # "per the filing". Shorter variant of "according to".
    # Discovered via Gizmodo $1.4T penalty article (Jul 2026):
    # "the penalties were calculated ... per Reuters"
    per_source = re.compile(
        r"\bper\s+(?:[Tt]he\s+)?([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+){0,3})\b",
    )
    for m in per_source.finditer(text):
        name = m.group(1).strip()
        if name in seen_names:
            continue

        # Filter false positives — skip generic nouns that happen to be
        # capitalised at sentence start or after "per"
        _per_stop = {
            "The", "This", "That", "These", "Those", "Each", "Every",
            "Some", "Any", "All", "Most", "Many", "Few", "Several",
            "Her", "His", "Its", "Our", "Their", "Your",
        }
        first_word = name.split()[0]
        if first_word in _per_stop or first_word in _NAME_STOP_FIRST_WORDS:
            continue

        seen_names.add(name)

        ctx_start = max(0, m.start() - 100)
        ctx_end = min(len(text), m.end() + 100)
        context = text[ctx_start:ctx_end]

        sources.append(SourceMention(
            name=name,
            is_anonymous=False,
            is_expert=False,
            affiliation=name,
            quote="",
            attribution_verb="per",
            source_type="news_outlet",
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
            is_expert=_is_expert_by_title(context) or _is_expert_full_text(text, name),
            affiliation=_extract_affiliation_full_text(text, name) or _extract_affiliation(context),
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
        "Fox",    # "told Fox Business" — single-word match from Pattern 5b/5c
        "Media",  # "404 Media" → regex strips numeric prefix, leaving "Media"
        "Insider",  # "Business Insider" — full name blocked by _NAME_STOP_NAMES
                    # but Pattern 5b catches "Insider reported" as single-name
        "Beast",    # "Daily Beast" — same issue
        # Chinese / international tech companies
        "Alibaba", "Baidu", "Tencent", "Huawei", "Xiaomi",
        "ByteDance", "Bytedance",
        # Energy/utility companies — "Entergy acknowledged" is a corporate
        # statement, not a human source.  Discovered in MIT Tech Review
        # Louisiana natural gas article (Jul 2026).
        "Entergy", "Eversource", "Dominion",
        # Common words that start sentences
        "People", "Everyone", "Somebody", "Someone", "Something",
        "Today", "Tomorrow", "Yesterday", "Here", "There",
        "First", "Second", "Third", "Finally", "Overall",
        "Like", "Similar", "Another", "According", "Rather",
        "True", "False", "None", "Yes", "Yeah",
        # Software product names that look like surnames
        "Outlook", "Windows", "Chrome", "Safari", "Firefox",
        "Photoshop", "Figma", "Notion", "Linear", "Canva",
        # AI product names that appear with attribution verbs
        # (e.g. "Operator added a delivery fee") — discovered in
        # MIT Tech Review AI agents article (Jul 4, 2026 iteration).
        "Operator", "Copilot", "Gemini", "Claude", "Cursor",
        "Alexa", "Siri", "Watson", "Cortana",
        # AI model names and publication fragments that match
        # single-word source patterns — discovered in LiveMint Meta/Wang
        # analysis (Jul 6, 2026 iteration).
        "Muse", "Spark", "Llama", "Maverick", "Scout",
        "Journal", "Tribune", "Herald", "Gazette", "Times",
        "Chronicle", "Observer", "Sentinel", "Register",
        "Standard", "Express", "Monitor",
        # Common institutional nouns that appear capitalized at sentence
        # start and false-positive as single-word sources.  Discovered
        # in MIT Tech Review Louisiana natural gas article (Jul 2026).
        "School", "University", "College", "Institute", "Center",
        "Alliance", "Association", "Foundation", "Commission",
        "Council", "Agency", "Bureau", "Department",
        # Economic/infrastructure nouns that start sentences (Jul 2026):
        # "Capacity charges at..." → false-positive "Capacity" as source
        "Capacity", "Manufacturing", "Production", "Electricity",
        # Abstract / common nouns that start sentences or appear in
        # product-naming context (Jul 2026):
        # "internally called Name Tag" → false-positive "Name" as source
        "Name", "Tag", "Balance",
        # Institutional nouns that appear as single words after verbs
        # (e.g. "said the White House" → Pattern 5c extracts "House")
        "House", "Senate", "Parliament", "Cabinet",
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
        # captured.  Also handles hyphenated surnames: skip "Kassaby" if
        # "Dina El-Kassaby" already seen.  Prevents duplicate source
        # entries for the same person.
        if any(seen.endswith(" " + name) or seen.endswith("-" + name) for seen in seen_names):
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
            is_expert=_is_expert_by_title(context) or _is_expert_full_text(text, name),
            # Single-surname sources are typically re-references of a person
            # introduced by full name earlier.  Prefer the full-text search
            # (which finds "D.A. Davidson analyst Gil Luria") over the local
            # context (which may contain unrelated org names like "of Anthropic").
            affiliation=_extract_affiliation_full_text(text, name) or _extract_affiliation(context),
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
        # full name — same dedup logic as Pattern 5b.  Includes hyphen
        # check for names like "El-Kassaby".
        if any(seen.endswith(" " + name) or seen.endswith("-" + name) for seen in seen_names):
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

        # Skip possessive forms — "told Barron's" is a publication or
        # brand reference (Barron's, Forbes's), not a person being quoted.
        # No human source attribution ever appears as "verb Name's that…".
        # Discovered in Barron's "Gigawatt Jolt" article (Jul 2026).
        match_end = m.end()
        if match_end < len(text) and text[match_end] in ("'", "\u2019"):
            continue

        # Skip hyphenated compound words — "blasted Ray-Ban" should NOT
        # extract "Ray" as a source.  When the matched name is immediately
        # followed by a hyphen+letter, it's part of a compound word (brand
        # name, place name, etc.), not a journalist source.
        # Discovered in Gizmodo smart glasses celebrity backlash article
        # (Jul 14, 2026): "Tyler the Creator recently blasted Ray-Ban Meta
        # AI glasses" → false-positive "Ray" extracted as source.
        if match_end < len(text) - 1 and text[match_end] == "-" and text[match_end + 1].isalpha():
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
        re.compile(r"\b((?:one|another|a) (?:worker|employee|engineer|staffer|user)) (?:said|told|called|described|complained)", re.IGNORECASE),
        re.compile(r"\b(an? (?:worker|employee|engineer|staffer|user)) (?:was quoted|was reported)", re.IGNORECASE),
        re.compile(r"\b((?:some|several|multiple|many) (?:workers|employees|engineers|staffers|people|users)) (?:said|told|described|called|complained|say|tell)", re.IGNORECASE),
        # Social media user quote patterns — "Said one X user", "one Twitter user noted"
        # Catches anonymous user quotes from social platforms commonly used in tech reporting.
        # Discovered via TechCrunch Muse Image privacy article (Jul 2026).
        re.compile(r"\b(?:said|wrote|posted|noted|commented)\s+(?:one|an?)\s+(?:X|Twitter|Instagram|Facebook|Threads|Reddit|Mastodon|Bluesky|TikTok)\s+user\b", re.IGNORECASE),
        re.compile(r"\b(?:one|an?)\s+(?:X|Twitter|Instagram|Facebook|Threads|Reddit|Mastodon|Bluesky|TikTok)\s+user\s+(?:" + verb_alternation + r")\b", re.IGNORECASE),
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
        # Match "internal documents obtained/seen/..." only when NOT followed
        # by "by [Outlet]" — those are documentary sources (Pattern 9) and
        # should not be captured here as anonymous.
        re.compile(
            r"\binternal\s+(?:documents?|memos?|emails?|guidelines?|presentations?|reports?|briefings?)\s+"
            r"(?:obtained|reviewed|seen|viewed|shared|circulated|warned|instructed|showed|stated|revealed|indicated)"
            r"(?!\s+by\s+(?:the\s+)?[A-Z])",
            re.IGNORECASE,
        ),
        re.compile(r"\bconfirmed by multiple sources\b", re.IGNORECASE),
        re.compile(
            r"\b(?:reported|confirmed)\s+by\s+(?:The\s+)?[A-Z]\w+\s+and\s+confirmed\s+by\s+multiple\s+sources\b",
            re.IGNORECASE,
        ),
        # "some workers/employees were [adjective]" — anonymous collective
        # sentiment attribution.  Common in wire service reporting where
        # the journalist attributes a group feeling without a direct quote:
        # "some workers were skeptical", "many employees were frustrated".
        # Uses state/sentiment verbs rather than speech attribution verbs.
        #
        # Limited to adjectives that strongly imply a response to specific
        # claims or events (skeptical, doubtful, wary) rather than general
        # emotional states (unhappy, angry, upset) which are more often
        # editorial narration than anonymous attribution.
        re.compile(
            r"\b(?:some|several|multiple|many|numerous|a few|a handful of)"
            r"\s+(?:current\s+(?:and\s+)?(?:former\s+)?)?"
            r"(?:workers|employees|staffers|engineers|people|sources|individuals|executives)"
            r"\s+(?:were|are|remain(?:ed)?|felt|seemed|appeared|grew)"
            r"\s+(?:skeptical|doubtful|unconvinced|wary|critical|"
            r"apprehensive|uneasy|alarmed|dismayed|demoralized)\b",
            re.IGNORECASE,
        ),
    ]

    # No-comment / declined-to-comment patterns — signals the entity chose not
    # to provide its side.  These are NOT anonymous sources; they are editorial
    # signals about the target entity's engagement with the reporter.
    no_comment_patterns: list[re.Pattern] = [
        re.compile(
            r"\b(?:did not|didn't|declined to|chose not to|refused to|would not|wouldn't|couldn't)"
            r" (?:immediately )?"
            r"(?:respond|comment|reply|return|answer|provide)"
            r"(?: to)?"
            r"(?: (?:a|the|our|multiple))?"
            r"(?: (?:request|call|email|query|inquiry|message|questions?))?",
            re.IGNORECASE,
        ),
        # "reached out to [Entity] for comment" — journalist due-diligence
        # disclosure where no response is reported.  Distinct from "declined
        # to comment" (entity explicitly refused) — this signals attempted
        # contact with an implicit non-response.  Gap discovered in Fox
        # Business Meta $1.4T penalty article (Jul 2026): "Fox Business
        # reached out to Meta for further comment" was invisible.
        re.compile(
            r"\breached out to\b.{1,60}\bfor\s+"
            r"(?:further |additional |a )?"
            r"(?:comment|response|clarification|a statement)",
            re.IGNORECASE,
        ),
        # "[Publication] has contacted [Entity] for comment" variant
        re.compile(
            r"\b(?:has |have )?contacted\b.{1,60}\bfor\s+"
            r"(?:further |additional |a )?"
            r"(?:comment|response|clarification|a statement)",
            re.IGNORECASE,
        ),
    ]

    # Regex to detect corporate spokesperson descriptors. If an anonymous
    # match is "a Meta spokesperson" or "the Google representative", it
    # should be reclassified as a corporate_spokesperson — technically
    # unnamed but institutionally identified, distinct from truly anonymous
    # sources ("people familiar with the matter").
    # Added iteration 2026-07-06 from Reuters EU WhatsApp antitrust analysis.
    # Handles hyphenated org names like SAG-AFTRA and all-caps acronyms.
    _CORPORATE_SPOKESPERSON_RE = re.compile(
        r"\b(?:an?|the)\s+([A-Z][A-Za-z-]+(?:\s+[A-Z][A-Za-z-]+)?)\s+"
        r"(?:spokesperson|spokesman|spokeswoman|representative)\b",
        re.IGNORECASE,
    )

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
            # Skip descriptors that match stop-name entries — these are
            # generic subject references inside indirect speech (e.g.
            # "the young person" in "indicates the young person wants"),
            # not journalistic source attributions.
            if descriptor.lower() in {n.lower() for n in _NAME_STOP_NAMES}:
                continue
            # Skip descriptors where "source" refers to a non-journalistic
            # source (energy, data, power, etc.).  "the energy source" in
            # "said the energy source was the only affordable choice" is
            # about natural gas, not a journalistic anonymous source.
            # Discovered in MIT Tech Review Louisiana natural gas article
            # (Jul 2026).
            _desc_lower_check = descriptor.lower()
            if "source" in _desc_lower_check:
                _NON_JOURNALISTIC_SOURCES = [
                    "energy source", "data source", "power source",
                    "fuel source", "light source", "heat source",
                    "food source", "revenue source", "income source",
                    "news source", "information source", "open source",
                    "water source", "resource source", "main source",
                    "primary source", "sole source", "chief source",
                ]
                if any(ns in _desc_lower_check for ns in _NON_JOURNALISTIC_SOURCES):
                    continue
            # Skip bare pronoun-like back-references to previously named
            # spokespeople — e.g. "The spokesperson added" after "A
            # Snapchat spokesperson told CNN".  These are continuations,
            # not new anonymous sources.
            _desc_lower = descriptor.lower()
            if _desc_lower in {
                "the spokesperson", "the spokeswoman", "the spokesman",
                "the representative",
            }:
                # Only skip if a named spokesperson was already captured
                if any(
                    "spokesperson" in n.lower()
                    or "spokesman" in n.lower()
                    or "spokeswoman" in n.lower()
                    for n in seen_names
                ):
                    continue
            seen_names.add(descriptor)

            ctx_start = max(0, m.start() - 100)
            ctx_end = min(len(text), m.end() + 100)
            context = text[ctx_start:ctx_end]

            # Check if this is a corporate spokesperson rather than
            # a truly anonymous source.
            corp_m = _CORPORATE_SPOKESPERSON_RE.search(descriptor)
            if corp_m:
                org_name = corp_m.group(1).strip()
                sources.append(SourceMention(
                    name=descriptor,
                    is_anonymous=False,
                    is_expert=False,
                    affiliation=org_name,
                    quote=_extract_nearby_quote(text, m.start(), m.end()),
                    attribution_verb=_find_attribution_verb(context),
                    source_type="corporate_spokesperson",
                ))
            else:
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
        r"(?:did not|didn't|declined to|chose not to|refused to|would not|wouldn't|couldn't)",
    )
    # Compound no-comment subjects: "X and Y did not respond"
    _NO_COMMENT_COMPOUND_RE = re.compile(
        r"\b([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+)*)"
        r"\s+and\s+"
        r"([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+)*)\s+"
        r"(?:did not|didn't|declined to|chose not to|refused to|would not|wouldn't|couldn't)",
    )
    for pat in no_comment_patterns:
        for m in pat.finditer(text):
            # Try to extract the entity name from the sentence subject
            # by looking at the 80 chars before the match.
            pre_ctx = text[max(0, m.start() - 80):m.end()]
            # First check for compound subjects ("X and Y did not ...")
            compound_m = _NO_COMMENT_COMPOUND_RE.search(pre_ctx)
            if compound_m:
                for grp_idx in (1, 2):
                    ent = compound_m.group(grp_idx).strip()
                    if ent.lower() in {n.lower() for n in seen_names}:
                        continue
                    seen_names.add(ent)
                    sources.append(SourceMention(
                        name=ent,
                        is_anonymous=False,
                        is_expert=False,
                        affiliation="",
                        quote="",
                        attribution_verb="",
                        source_type="no_comment",
                    ))
                continue
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

    # Regex to strip trailing attribution verb phrases from group expert
    # names.  Pattern 7's first regex matches the full "Legal analysts
    # noted that" — the verb + trailing connector must be removed so the
    # source name is just "Legal analysts".
    _STRIP_VERB_TAIL_RE = re.compile(
        rf"\s+(?:have\s+)?(?:{verb_alternation})"
        rf"(?:\s+(?:as much|similarly|likewise|that|in))?$",
        re.IGNORECASE,
    )

    for pat in group_expert_patterns:
        for m in pat.finditer(text):
            descriptor = m.group().strip()

            # Strip trailing attribution verb phrases from the name so
            # "Legal analysts noted that" becomes "Legal analysts".
            descriptor = _STRIP_VERB_TAIL_RE.sub("", descriptor).strip()

            # Deduplicate — also check if this name is a substring of
            # an existing name or vice versa to catch truncated
            # duplicates like "Legal" vs "Legal analysts".
            descriptor_lower = descriptor.lower()
            if descriptor_lower in {n.lower() for n in seen_names}:
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

    # Pattern 9: Documentary sources — recordings, documents, filings,
    # court records, internal materials obtained or reviewed by the
    # publication.  These are not human sources but artifacts cited as
    # evidence.  Common in investigative and financial journalism.
    # Tagged source_type="documentary".
    #
    # Examples:
    #   "a recording heard by Reuters"
    #   "documents obtained by The Guardian"
    #   "internal documents seen by Wired"
    #   "according to a recording of the meeting"
    #   "court records show"
    #   "a filing obtained by Bloomberg"
    #   "an internal memo reviewed by The New York Times"
    #   "the recording, a copy of which was obtained by..."
    documentary_patterns: list[re.Pattern] = [
        # "[a/the/adj] recording/document/filing heard/obtained/seen/reviewed by [Outlet]"
        # Article (a/an/the) is optional so bare adjective+noun phrases like
        # "Internal documents obtained by The Guardian" also match.
        re.compile(
            r"\b(?:an?\s+|the\s+)?"
            r"(?:internal\s+|leaked\s+|confidential\s+|draft\s+)?"
            r"(?:recording|document|documents|filing|filings|memo|"
            r"memorandum|presentation|spreadsheet|email|emails|"
            r"letter|letters|report|tape|audio|video|transcript|"
            r"slide\s+deck|deck|briefing)\s+"
            r"(?:heard|obtained|seen|reviewed|viewed|examined|"
            r"accessed|acquired|provided|shared|furnished|"
            r"made available)\s+"
            r"(?:by|to)\s+"
            r"(?:the\s+)?"
            r"[A-Z][A-Za-z\s]{2,30}",
            re.IGNORECASE,
        ),
        # "according to a/the recording/document/filing"
        re.compile(
            r"\baccording\s+to\s+"
            r"(?:a|an|the|one|two|several|multiple)\s+"
            r"(?:internal\s+|leaked\s+|confidential\s+|draft\s+)?"
            r"(?:recording|document|documents|filing|filings|memo|"
            r"memorandum|presentation|spreadsheet|email|emails|"
            r"letter|report|tape|audio|video|transcript|copy|"
            r"blog\s+post)\b",
            re.IGNORECASE,
        ),
        # "court records/filings show/indicate/reveal"
        re.compile(
            r"\b(?:court|legal|regulatory|SEC|FTC|patent|judicial)\s+"
            r"(?:records?|filings?|documents?|papers?|proceedings?)\s+"
            r"(?:show|shows?|indicate|indicates?|reveal|reveals?|"
            r"suggest|suggests?|confirm|confirms?|state|states?)\b",
            re.IGNORECASE,
        ),
        # "the filing/complaint/lawsuit/suit states/says/argues"
        # The legal document itself used as a source with an attribution verb.
        # Discovered via Gizmodo $1.4T penalty article (Jul 2026):
        # 'the filing states. "The AGs\' demand exceeds..."'
        re.compile(
            r"\b(?:the|a|an)\s+"
            r"(?:filing|complaint|lawsuit|suit|petition|motion|brief|"
            r"indictment|ruling|order|decision|opinion|judgment|"
            r"court\s+(?:filing|submission|document))\s+"
            r"(?:also\s+)?"
            r"(?:state|states|said|says|say|argue|argues|argued|"
            r"allege|alleges|alleged|note|notes|noted|"
            r"claim|claims|claimed|contend|contends|contended|"
            r"assert|asserts|asserted|add|adds|added)\b",
            re.IGNORECASE,
        ),
        # "a copy of which was obtained/provided/shared"
        re.compile(
            r"\b(?:a|the)\s+copy\s+of\s+which\s+was\s+"
            r"(?:obtained|provided|shared|furnished|"
            r"made available|given)\b",
            re.IGNORECASE,
        ),
        # "the blog post / press release / announcement calls/says/states"
        # Non-legal public documents used as sources with attribution verbs.
        # Discovered in Gizmodo Muse Image scrapped article (Jul 11, 2026):
        #   "the blog post announcing it calls it, 'the creative partner...'"
        #   "the blog post now has an update, added Friday"
        re.compile(
            r"\b(?:the|a|an)\s+"
            r"(?:blog\s+post|press\s+release|announcement|statement|"
            r"white\s*paper|policy\s+(?:update|change)|release\s+notes|"
            r"company\s+(?:blog|post)|corporate\s+blog)\s+"
            r"(?:also\s+|now\s+|further\s+)?"
            r"(?:state|states|said|says|say|calls|call|"
            r"note|notes|noted|read|reads|describe|describes|"
            r"explained|explains|mention|mentions|has|had|have)\b",
            re.IGNORECASE,
        ),
        # "documents/emails/recordings [that/which] [Outlet] has seen/reviewed"
        re.compile(
            r"\b(?:internal\s+|leaked\s+|confidential\s+)?"
            r"(?:recordings?|documents?|filings?|memos?|emails?|"
            r"letters?|reports?|tapes?|transcripts?)\s+"
            r"(?:that|which)\s+"
            r"(?:the\s+)?[A-Z][A-Za-z\s]{2,30}\s+"
            r"(?:has|have)\s+"
            r"(?:seen|reviewed|obtained|viewed|examined)\b",
            re.IGNORECASE,
        ),
    ]

    for pat in documentary_patterns:
        for m in pat.finditer(text):
            descriptor = m.group().strip()
            if descriptor.lower() in {n.lower() for n in seen_names}:
                continue
            seen_names.add(descriptor)

            ctx_start = max(0, m.start() - 100)
            ctx_end = min(len(text), m.end() + 200)
            context = text[ctx_start:ctx_end]

            sources.append(SourceMention(
                name=descriptor,
                is_anonymous=False,
                is_expert=False,
                affiliation="",
                quote=_extract_nearby_quote(text, m.start(), m.end()),
                attribution_verb=_find_attribution_verb(context),
                source_type="documentary",
            ))

    # Pattern 6: Organizational sources — "Meta said", "Google confirmed",
    # "the company said in a statement", "a spokesperson told Reuters"
    # These are named non-anonymous sources where the speaker is an entity
    # rather than a person.  They are important for stance analysis because
    # company statements often represent the target entity's official position.
    org_source_patterns: list[re.Pattern] = [
        # "according to [the] [Org]" — organizational attribution via
        # "according to" that won't match person-name Pattern 3 because
        # compound publication names are in _NAME_STOP_NAMES.
        # Example: "According to Business Insider, the project began..."
        # Example: "According to the Daily Beast, sources confirmed..."
        re.compile(
            r"\b[Aa]ccording to (?:the )?"
            r"([A-Z][a-z]+ [A-Z][a-z]+)\b",
        ),
        # "[Company] said/told/confirmed in [a statement/an emailed response]"
        # Supports up to 3-word org names (e.g. "Creative Artists Agency wrote
        # in a statement").  Extended from 2-word in Jul 11 2026 iteration
        # after Washington Examiner Muse Image analysis: "Creative Artists
        # Agency" was truncated to "Artists Agency".
        re.compile(
            rf"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){{0,2}})"
            rf"\s+({verb_alternation})"
            rf"\s+(?:in (?:a|an|the|its)\s+(?:statement|emailed? (?:response|statement|comment)|"
            rf"blog post|press release|filing|report|letter|memo|announcement))\b",
        ),
        # "[Company] said/told/reported" — direct organizational attribution
        # without requiring "in a statement" qualifier.  Validated against
        # _KNOWN_ORGS below to prevent false positives from person surnames.
        # Supports up to 3-word org names.
        re.compile(
            rf"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){{0,2}})"
            rf"\s+({verb_alternation})\b",
        ),
        # "[ACRONYM] ... said/told" — all-caps acronym org with possible
        # appositive clause between name and verb.  Common in Reuters-style
        # wire copy: "DVP, which includes ..., said it was satisfied".
        # Validated against _KNOWN_ORGS below.
        re.compile(
            rf"\b([A-Z]{{2,6}})"
            rf"(?:,\s+[^,]{{1,120}},)?\s+"
            rf"({verb_alternation})\b",
        ),
        # "a [Company] spokesperson/representative said/told"
        # Use [Aa]n? instead of an? to match sentence-initial "A Meta spokesperson said"
        re.compile(
            rf"\b[Aa]n?\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\s+"
            rf"(?:spokesperson|spokeswoman|spokesman|representative|official)\s+"
            rf"({verb_alternation})\b",
        ),
        # "according to a/an [Company] spokesperson/representative" — attribution
        # via "according to" where the spokesperson is org-affiliated.
        # Discovered via Bloomberg Muse Image article (Jul 2026):
        # "according to a Meta spokesperson" was missed because existing
        # patterns required a verb after "spokesperson".
        re.compile(
            rf"\baccording to\s+[Aa]n?\s+"
            rf"([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\s+"
            rf"(?:spokesperson|spokeswoman|spokesman|representative|official)\b",
        ),
        # "[Company] spokesperson [Name] said" — skip if name already captured
        re.compile(
            rf"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\s+"
            rf"(?:spokesperson|spokeswoman|spokesman)\s+"
            rf"[A-Z][a-z]+ [A-Z][a-z]+\b",
        ),
        # "according to [Compound Org Name]" — multi-word org names like
        # "IBD MarketSurge", "Needham & Company", "Barclays Capital"
        # that won't match Pattern 3's two-word capitalized-name pattern.
        re.compile(
            r"\baccording to\s+"
            r"([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+)*)\b",
        ),
    ]

    # Self-validating organizational patterns — these constructions inherently
    # indicate an organizational source (e.g. "Analysts with [Org]") and do
    # NOT require _KNOWN_ORGS membership.  They are processed before the
    # _KNOWN_ORGS-gated patterns below.
    _self_validating_org_patterns: list[re.Pattern] = [
        # "Analysts with/at/from [Org] verb" — organizational attribution via
        # analyst role descriptor.  Handles "Analysts with SemiAnalysis
        # estimated", "analysts at Erste Group upgraded".
        # The org name is extracted as the source, not the generic "Analysts".
        re.compile(
            rf"\b[Aa]nalysts?\s+(?:with|at|from)\s+"
            rf"([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+)*)"
            rf"\s+({verb_alternation})\b",
        ),
        # "[Org] analysts verb" — inverted analyst attribution.
        # Handles "Morgan Stanley analysts said", "Goldman Sachs analysts
        # estimated".  The org name precedes the role descriptor.
        re.compile(
            rf"\b([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+)*)"
            rf"\s+[Aa]nalysts?\s+({verb_alternation})\b",
        ),
    ]

    for pat in _self_validating_org_patterns:
        for m in pat.finditer(text):
            org_name = m.group(1).strip()
            if org_name.lower() in {n.lower() for n in seen_names}:
                continue
            seen_names.add(org_name)

            verb = m.group(2).strip().lower() if m.lastindex >= 2 else ""
            sources.append(SourceMention(
                name=org_name,
                is_anonymous=False,
                is_expert=False,
                affiliation=org_name,
                quote=_extract_nearby_quote(text, m.start(), m.end()),
                attribution_verb=verb,
                source_type="organizational",
            ))

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
        # Research/analyst firms — discovered in IBD Meta cloud
        # article (Jul 2026).
        "semianalysis", "erste group", "ibd marketsurge",
        "needham", "bernstein", "jefferies", "wedbush",
        "morningstar", "cowen", "piper sandler", "baird",
        # Energy/utility companies — discovered in MIT Tech Review
        # Louisiana natural gas article (Jul 2026).
        "entergy", "duke energy", "dominion", "eversource",
        "nextera", "pg&e", "con edison",
        # Compound publication names — these are also in _NAME_STOP_NAMES
        # to prevent person-name false positives, but should still be
        # extractable as organizational/publication sources.
        "business insider", "daily beast", "daily mail",
        "tech review", "technology review",
        "morning post", "evening standard",
        # Broadcast and wire services — often appear as
        # intermediary attribution in multi-source articles
        # (e.g. "CNBC quoted Rob May").
        "cnbc", "bbc", "cnn", "abc", "nbc", "cbs", "fox",
        "associated press", "ap",
        # French media associations — discovered in Reuters French
        # antitrust article (Jul 2026).
        "dvp", "apig",
        # Entertainment/talent agencies — discovered in Washington Examiner
        # Muse Image article (Jul 2026).
        "creative artists agency", "caa",
        # Civil liberties organizations — discovered in Fast Company
        # Meta glasses controversies roundup (Jul 10, 2026).
        "electronic frontier foundation", "eff",
        # Entertainment/labor unions — discovered in Gizmodo Muse Image
        # scrapped article (Jul 11, 2026).
        "sag-aftra", "wga", "dga", "iatse",
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

            # Filter out conditional/speculative constructions like
            # "once Meta acknowledges defeat", "if Google admits", etc.
            # These are not real attribution — the verb is hypothetical.
            # Discovered in IBD article (Jul 8, 2026): "once Meta
            # acknowledges defeat" was a false positive.
            pre_start = max(0, m.start() - 30)
            pre_text = text[pre_start:m.start()].lower().strip()
            if re.search(
                r"\b(?:once|if|when|should|could|would|might|unless|"
                r"until|before|after|whether)\s*$",
                pre_text,
            ):
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

    # Pattern 11: Publication-as-cited-source — when an article
    # attributes a finding to another publication.  "The Verge first
    # pointed out", "as first reported by Reuters", "according to
    # a report by Bloomberg".  These are organizational sources used
    # as attribution authority.
    # Discovered via TechCrunch Muse Image article (Jul 2026):
    # "after The Verge first pointed out how potentially invasive this is"
    _KNOWN_PUBS = {
        "The Verge", "Wired", "The New York Times", "The Guardian",
        "The Atlantic", "MIT Technology Review", "Bloomberg",
        "Reuters", "TechCrunch", "Ars Technica", "The Information",
        "The Wall Street Journal", "Financial Times", "CNBC",
        "The Washington Post", "BBC", "CNN", "NBC News", "ABC News",
        "Axios", "Politico", "Vox", "Gizmodo", "Engadget",
        "9to5Mac", "MacRumors", "The Register", "Futurism",
        "Svenska Dagbladet", "TheWrap", "Digital Trends",
        "Barron's",
    }
    _pub_alt = "|".join(re.escape(p) for p in sorted(_KNOWN_PUBS, key=len, reverse=True))
    pub_cite_patterns: list[re.Pattern] = [
        # "[Publication] first pointed out/reported/revealed/disclosed"
        re.compile(
            rf"\b({_pub_alt})\s+(?:first\s+)?(?:pointed out|reported|revealed|"
            r"disclosed|noted|found|discovered|highlighted|showed|documented)\b",
            re.IGNORECASE,
        ),
        # "as first reported/noted by [Publication]"
        re.compile(
            rf"\bas\s+(?:first\s+)?(?:reported|noted|revealed|disclosed|pointed out)\s+by\s+(?:the\s+)?({_pub_alt})\b",
            re.IGNORECASE,
        ),
        # "according to a report by/in [Publication]"
        re.compile(
            rf"\baccording\s+to\s+(?:a\s+)?(?:report|story|investigation|analysis)\s+(?:by|in|from)\s+(?:the\s+)?({_pub_alt})\b",
            re.IGNORECASE,
        ),
        # "[a/A] report from/by [optional descriptor] [Publication]"
        # Handles: "A report from Swedish newspaper Svenska Dagbladet that..."
        # "a report by Bloomberg detailed..."
        re.compile(
            rf"\b[Aa]n?\s+(?:report|investigation|story|analysis|exposé)\s+"
            rf"(?:from|by)\s+(?:[\w\-]+\s+)?(?:newspaper|publication|outlet|magazine|website)?\s*"
            rf"({_pub_alt})\b",
            re.IGNORECASE,
        ),
        # "according to [Publication]" — direct attribution without
        # intermediate "report/story" noun.  Common with wire services:
        # "According to Reuters, ..." or "according to Bloomberg, ..."
        # Discovered in Gizmodo Muse Image scrapped article (Jul 11, 2026):
        #   "According to Reuters, after the feature was pulled, ..."
        re.compile(
            rf"\baccording\s+to\s+({_pub_alt})\b",
            re.IGNORECASE,
        ),
    ]

    for pat in pub_cite_patterns:
        for m in pat.finditer(text):
            pub_name = m.group(1).strip()
            if pub_name.lower() in {n.lower() for n in seen_names}:
                continue
            seen_names.add(pub_name)

            ctx_start = max(0, m.start() - 100)
            ctx_end = min(len(text), m.end() + 200)
            context = text[ctx_start:ctx_end]

            sources.append(SourceMention(
                name=pub_name,
                is_anonymous=False,
                is_expert=False,
                affiliation=pub_name,
                quote=_extract_nearby_quote(text, m.start(), m.end()),
                attribution_verb="cited",
                source_type="publication_citation",
            ))

    # --- Quote count enrichment ---
    # Count how many distinct attribution instances reference each named
    # source in the full text.  The extraction above deduplicates by name,
    # producing one SourceMention per unique identity.  This post-pass
    # counts all attribution occurrences (verb + name, name + verb,
    # "according to" + name) so consumers can quantify sourcing weight.
    verb_re_str = "|".join(re.escape(v) for v in sorted(ALL_VERBS, key=len, reverse=True))
    for src in sources:
        if src.source_type not in ("named",):
            continue
        name = src.name
        # Build patterns for all name forms (full name + last name)
        name_forms = [re.escape(name)]
        parts = name.split()
        if len(parts) > 1:
            name_forms.append(re.escape(parts[-1]))  # last name
        name_alt = "|".join(name_forms)
        count_pat = re.compile(
            rf"(?:\b(?:{name_alt})\s+(?:{verb_re_str})\b"
            rf"|\b(?:{verb_re_str})\s+(?:{name_alt})\b"
            rf"|\b[Aa]ccording to (?:\w+\s+){{0,3}}(?:{name_alt})\b"
            rf"|\b(?:{name_alt}),\s+[^.\"]*?,\s*(?:\w+ly\s+)?(?:{verb_re_str})\b"
            rf"|\b(?:{name_alt})\s+(?:has|have|had)\s+(?:\w+ly\s+)?(?:{verb_re_str})\b"
            rf"|(?:,\s*(?:{name_alt})\s+(?:{verb_re_str}))"  # ", Zuckerberg said"
            rf"|(?:,\s*he\s+(?:{verb_re_str})))"  # ", he said" — attributed to subject
        )
        hits = list(count_pat.finditer(text))
        if len(hits) > 1:
            src.quote_count = len(hits)

    # Pattern 10: Governmental/legal party sources — collective legal
    # actors like "the states said", "prosecutors argued", "plaintiffs
    # said", "the government said".  These are NOT anonymous: the
    # parties are identified by their role and often individually named
    # elsewhere in the article.  Common in litigation, regulatory, and
    # legislative coverage.  Gap discovered in Reuters $1.4T penalty
    # article (Jul 2026): "the states said" was invisible.
    # Tagged source_type="legal_party".
    legal_party_patterns: list[re.Pattern] = [
        # "the states/plaintiffs/prosecutors/defendants said/argued/claimed"
        re.compile(
            rf"\bthe\s+"
            rf"(?:states?|plaintiffs?|prosecutors?|defendants?|petitioners?"
            rf"|respondents?|appellants?|appellees?|claimants?"
            rf"|government|administration|agency|commission"
            rf"|attorneys?\s+general|AG'?s?)\s+"
            rf"(?:(?:also|further|additionally)\s+)?"
            rf"({verb_alternation})\b",
            re.IGNORECASE,
        ),
        # "prosecutors/plaintiffs have argued/said"
        re.compile(
            rf"\b(?:prosecutors?|plaintiffs?|defendants?|the\s+states?)\s+"
            rf"(?:have|had)\s+({verb_alternation})\b",
            re.IGNORECASE,
        ),
        # "the attorneys/lawyers for [Entity] argued/said/claimed"
        # Discovered via Gizmodo $1.4T penalty article (Jul 2026):
        # "the attorneys for Meta argued that..."
        re.compile(
            rf"\b(?:the\s+)?(?:attorneys?|lawyers?|counsel)\s+"
            rf"(?:for|representing)\s+"
            rf"[A-Z][A-Za-z]+\s+"
            rf"({verb_alternation})\b",
            re.IGNORECASE,
        ),
    ]

    for pat in legal_party_patterns:
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
                affiliation="",
                quote=_extract_nearby_quote(text, m.start(), m.end()),
                attribution_verb=verb,
                source_type="legal_party",
            ))

    # ---- Post-extraction: merge legal_party sources with earlier named/org
    # sources when the legal_party descriptor is a definite-article variant
    # of an established named source.  Example: "the commission said" is a
    # coreference for "European Commission" already extracted.
    # Discovered in CNN EU DSA addictive design article (Jul 10, 2026):
    # "the commission said" was extracted as a separate source from
    # "European Commission".
    _legal_party_indices_to_drop: list[int] = []
    for idx, src in enumerate(sources):
        if src.source_type != "legal_party":
            continue
        # Extract the core noun from "the [noun] said" descriptor.
        # The legal_party name is the full match like "the commission said".
        descriptor_lower = src.name.lower()
        # Strip leading "the " and trailing " <verb>"
        core = re.sub(
            r"^the\s+", "",
            re.sub(rf"\s+(?:{verb_alternation})$", "", descriptor_lower),
        )
        if not core:
            continue
        # Check if any earlier source's canonical name contains the core word
        for earlier_idx, earlier_src in enumerate(sources):
            if earlier_idx == idx:
                continue
            if earlier_src.source_type == "legal_party":
                continue
            # "commission" is contained in "European Commission"
            if core in earlier_src.name.lower():
                _legal_party_indices_to_drop.append(idx)
                # Increment the earlier source's quote count
                earlier_src.quote_count += src.quote_count
                break
    if _legal_party_indices_to_drop:
        sources = [s for i, s in enumerate(sources)
                   if i not in _legal_party_indices_to_drop]

    # ---- Post-extraction: research report sources ----
    # Pattern: "a report from researchers at [Institution] ... found that ..."
    # Academic/institutional research cited as evidence.
    # Discovered in CNN EU DSA article (Jul 10, 2026): NYU/Northeastern
    # research finding was not extracted as a source.
    _research_verbs = (
        r"found|concluded|determined|showed|demonstrated|revealed|"
        r"estimated|suggested|indicated|reported|confirmed|observed"
    )
    _research_report_patterns = [
        # "a report from researchers at [Institution] [and [Institution]] found that"
        re.compile(
            r"\b(?:a|the)\s+(?:report|study|survey|analysis|paper|investigation)"
            r"\s+(?:from|by)\s+(?:researchers?|scientists?|academics?|scholars?)"
            r"\s+at\s+([A-Z][A-Za-z\s]+?(?:\s+and\s+[A-Z][A-Za-z\s]+?)?)"
            rf"\s+(?:[\w\s]{{0,80}})\s+(?:{_research_verbs})\s+that\b",
            re.IGNORECASE,
        ),
        # "researchers at [Institution] found that"
        re.compile(
            r"\b(?:researchers?|scientists?|academics?|scholars?)"
            r"\s+(?:at|from)\s+([A-Z][A-Za-z\s]+?(?:\s+and\s+[A-Z][A-Za-z\s]+?)?)"
            rf"\s+(?:[\w\s]{{0,40}})\s+(?:{_research_verbs})\s+that\b",
            re.IGNORECASE,
        ),
    ]
    for pat in _research_report_patterns:
        for m in pat.finditer(text):
            inst_name = m.group(1).strip()
            # Clean up trailing common words that aren't part of the name
            inst_name = re.sub(r"\s+(?:evaluating|examining|studying|measuring|assessing)\b.*$", "", inst_name)
            inst_lower = inst_name.lower()
            # Containment-aware dedup: skip if this name is a substring of
            # an existing name (existing is more complete) or vice-versa.
            # When the new name is a superset of an existing one, replace
            # the shorter entry so the most complete institution name wins.
            _existing_lower = {n.lower() for n in seen_names}
            if inst_lower in _existing_lower:
                continue
            is_substring_of_existing = any(
                inst_lower in ex for ex in _existing_lower
            )
            if is_substring_of_existing:
                continue
            # If an existing name is a substring of the new (longer) name,
            # replace it in both seen_names and sources list.
            _shorter_existing = [
                n for n in seen_names if n.lower() in inst_lower and n.lower() != inst_lower
            ]
            for shorter in _shorter_existing:
                seen_names.discard(shorter)
                sources[:] = [s for s in sources if s.name != shorter]
            seen_names.add(inst_name)

            ctx_start = max(0, m.start() - 50)
            ctx_end = min(len(text), m.end() + 200)

            sources.append(SourceMention(
                name=inst_name,
                is_anonymous=False,
                is_expert=True,
                affiliation=inst_name,
                quote=_extract_nearby_quote(text, m.start(), m.end()),
                attribution_verb="found",
                source_type="research_report",
            ))

    # ---- Post-extraction: prefix-truncation deduplication ----
    # Remove sources whose name is a strict prefix of another source's
    # name, keeping the longer (more specific) version.  Prevents e.g.
    # "Legal" (Pattern 5b single-name match) from surviving alongside
    # "Legal analysts" (Pattern 7 group expert match).
    #
    # Uses prefix matching (not arbitrary substring) to avoid false
    # positives: "Meta" is a legitimate organizational source even when
    # "the attorneys for Meta argued" exists — "Meta" is embedded in the
    # middle, not a prefix truncation.
    _indices_to_drop: list[int] = []
    for i, src_a in enumerate(sources):
        if i in _indices_to_drop:
            continue
        for j, src_b in enumerate(sources):
            if j <= i or j in _indices_to_drop:
                continue
            a_lower = src_a.name.lower().strip()
            b_lower = src_b.name.lower().strip()
            # Skip if names are identical (already handled by seen_names)
            if a_lower == b_lower:
                _indices_to_drop.append(j)
                continue
            # If shorter name is a prefix of the longer name (word-
            # boundary aligned), drop the shorter one as a truncation.
            if len(a_lower) < len(b_lower):
                if (
                    b_lower.startswith(a_lower + " ")
                    or b_lower.startswith(a_lower + "'")
                ):
                    _indices_to_drop.append(i)
                    break
            elif len(b_lower) < len(a_lower):
                if (
                    a_lower.startswith(b_lower + " ")
                    or a_lower.startswith(b_lower + "'")
                ):
                    _indices_to_drop.append(j)
    if _indices_to_drop:
        sources = [s for i, s in enumerate(sources)
                   if i not in _indices_to_drop]

    return sources


def _extract_nearby_quote(text: str, ref_start: int, ref_end: int) -> str:
    """Extract a quoted string near a reference position.

    Looks for text enclosed in quotation marks near the reference.
    Prefers quotes AFTER the reference (attribution → quote pattern)
    over quotes BEFORE (quote → attribution), to avoid misattributing
    a preceding speaker's quote to the current source.
    """
    # Look for quoted text (double quotes or smart quotes)
    quote_patterns = [
        re.compile(r'"([^"]{10,300})"'),
        re.compile(r'\u201c([^\u201d]{10,300})\u201d'),
        re.compile(r"'([^']{10,300})'"),
    ]

    # Phase 1: Search FORWARD from the reference (preferred — attribution
    # typically precedes the quote: 'says Gong. "..."')
    fwd_end = min(len(text), ref_end + 300)
    fwd_window = text[ref_end:fwd_end]
    for qp in quote_patterns:
        m = qp.search(fwd_window)
        if m:
            return m.group(1).strip()

    # Phase 2: Fall back to searching BACKWARD (quote precedes attribution:
    # '"..." says Gong')
    bwd_start = max(0, ref_start - 200)
    bwd_window = text[bwd_start:ref_start]
    for qp in quote_patterns:
        # Find the LAST match in the backward window (closest to ref)
        last_match = None
        for m in qp.finditer(bwd_window):
            last_match = m
        if last_match:
            return last_match.group(1).strip()

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

    Handles both single-word verbs and compound negative attribution
    phrases (e.g., "attempted yet failed", "reluctantly conceded").

    Args:
        verb: The attribution verb or phrase to classify.

    Returns:
        "neutral", "loaded", or "unknown".
    """
    v = verb.lower().strip()
    # Check compound phrases first — they override single-word classification
    for phrase in COMPOUND_LOADED_PHRASES:
        if phrase in v or v in phrase:
            return "loaded"
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
        else:
            # --- Plaintiff/adversarial-role detection ---
            # Sources described as lawyers/attorneys for the opposing side
            # in litigation, or as plaintiffs, are inherently adversarial
            # to the defendant entities regardless of quote content.
            # "Previn Warren, one of the lead lawyers for the schools"
            # is adversarial to Meta/Snap/TikTok/Google even if his
            # quote is measured.
            is_adversarial_role = False
            if not source.is_anonymous and full_text:
                name_parts = source.name.strip().split()
                last_name = name_parts[-1].lower() if name_parts else ""
                if last_name:
                    ft_lower = full_text.lower()
                    # Look for "[Name], [role] for the [plaintiff group]"
                    # or "lawyer/attorney [Name]" patterns
                    _ADVERSARIAL_ROLE_PATTERNS = [
                        # "Name, one of the lead/lead/chief lawyers for"
                        re.compile(
                            rf"{re.escape(last_name)}.{{0,80}}"
                            r"\b(?:lawyer|lawyers|attorney|attorneys|counsel|"
                            r"plaintiff|plaintiffs|litigant|litigants|"
                            r"lead\s+(?:lawyer|attorney|counsel))\s+"
                            r"(?:for|representing|on\s+behalf\s+of)\b",
                            re.IGNORECASE,
                        ),
                        # "attorney/lawyer for the [schools/districts/families/plaintiffs]"
                        re.compile(
                            rf"{re.escape(last_name)}.{{0,60}}"
                            r"\b(?:lawyer|attorney|counsel)\b"
                            r".{0,40}?"
                            r"\b(?:school|schools|district|districts|"
                            r"families|plaintiffs?|victims?|children|"
                            r"students?|workers?|employees?|consumers?)\b",
                            re.IGNORECASE | re.DOTALL,
                        ),
                    ]
                    for pat in _ADVERSARIAL_ROLE_PATTERNS:
                        if pat.search(ft_lower):
                            is_adversarial_role = True
                            break

            if is_adversarial_role:
                adversarial.append(source.name)
            # --- Documentary complaint/lawsuit stance ---
            # Court complaints, lawsuits, and legal filings cited as
            # documentary sources are inherently adversarial toward the
            # defendant entity.  A "complaint" is filed BY a plaintiff
            # AGAINST a defendant — its allegations are adversarial by
            # nature regardless of the neutral language used in
            # attribution ("the complaint states").
            #
            # Discovered in Analytics Insight Meta AI Layoff article
            # (Jul 15, 2026): the lawsuit/complaint was scored neutral
            # because its attribution verb was "states" (neutral) and
            # quote content discussed discrimination without matching
            # the negative stance terms directly.
            elif (
                getattr(source, "source_type", "") == "documentary"
                and re.search(
                    r"\b(?:complaint|lawsuit|suit|litigation|"
                    r"class[ -]action|legal[ -]action|"
                    r"court[ -]filing|petition|indictment|"
                    r"charge|allegation|claim)\b",
                    (source.name + " " + source.quote + " " + context_text).lower(),
                )
            ):
                adversarial.append(source.name)
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
