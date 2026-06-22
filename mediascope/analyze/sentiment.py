"""Multi-model sentiment analysis for media coverage asymmetry detection.

Provides VADER and TextBlob baselines plus a composite analyzer that
calculates 8 sentiment dimensions for nuanced coverage analysis.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

logger = logging.getLogger(__name__)

# Singleton VADER analyzer
_vader = SentimentIntensityAnalyzer()

# --- Anonymous source patterns ---
ANONYMOUS_SOURCE_PATTERNS: list[re.Pattern] = [
    re.compile(r"\baccording to (?:people|sources|individuals|persons)\b", re.IGNORECASE),
    re.compile(r"\bpeople familiar with\b", re.IGNORECASE),
    re.compile(r"\bspoke on (?:the )?condition (?:of )?(?:anonymity)?\b", re.IGNORECASE),
    re.compile(r"\basked not to be identified\b", re.IGNORECASE),
    re.compile(r"\bpeople who requested anonymity\b", re.IGNORECASE),
    re.compile(r"\ba person with (?:direct )?knowledge\b", re.IGNORECASE),
    re.compile(r"\bsources (?:said|told|indicated|suggested|confirmed|added)\b", re.IGNORECASE),
    re.compile(r"\bpeople (?:said|told|indicated|suggested|confirmed|added)\b", re.IGNORECASE),
    re.compile(r"\baccording to (?:two|three|four|five|several|multiple) people\b", re.IGNORECASE),
    re.compile(r"\bsomeone (?:close to|briefed on|with knowledge)\b", re.IGNORECASE),
    re.compile(r"\binsiders?\b", re.IGNORECASE),
    re.compile(r"\ba (?:former|current) (?:employee|executive|official) who\b", re.IGNORECASE),
    # Publication-as-source patterns (journalist withholding their own source)
    re.compile(r"\b\w+ has learned\b", re.IGNORECASE),
    re.compile(r"\bobtained by \w+\b", re.IGNORECASE),
    re.compile(r"\breviewed by \w+\b", re.IGNORECASE),
    re.compile(r"\ba source (?:with knowledge|close|familiar|briefed|told|said|confirmed)\b", re.IGNORECASE),
    re.compile(r"\bmultiple sources (?:confirm|said|told)\b", re.IGNORECASE),
]

# Named source patterns — look for "Name said", "said Name", "according to Name"
NAMED_SOURCE_PATTERNS: list[re.Pattern] = [
    # "Name said" / "Name told" — capitalized name followed by attribution verb
    re.compile(
        r"\b([A-Z][a-z]+ (?:[A-Z]\. )?[A-Z][a-z]+)\s+"
        r"(?:said|told|stated|noted|explained|argued|claimed|insisted|warned|added|commented)\b"
    ),
    # "said Name" — attribution verb followed by capitalized name
    re.compile(
        r"\b(?:said|told|stated|noted|explained|argued|claimed|insisted|warned|added|commented)\s+"
        r"([A-Z][a-z]+ (?:[A-Z]\. )?[A-Z][a-z]+)\b"
    ),
    # "according to Name"
    re.compile(
        r"\baccording to ([A-Z][a-z]+ (?:[A-Z]\. )?[A-Z][a-z]+)\b"
    ),
    # "Name, who/the CEO/a spokesperson" — name with title
    re.compile(
        r"\b([A-Z][a-z]+ (?:[A-Z]\. )?[A-Z][a-z]+),\s+"
        r"(?:who|the|a|an|chief|CEO|president|director|spokesperson|head)\b"
    ),
]

# Speculative language indicators
SPECULATIVE_PHRASES: list[str] = [
    "could", "might", "may", "reportedly", "allegedly", "apparently",
    "is expected to", "is said to", "is believed to", "is thought to",
    "is rumored to", "is likely to", "is unlikely to",
    "sources say", "some say", "it is unclear", "remains to be seen",
    "raises questions", "raises concerns", "it appears",
    "seems to", "appeared to", "suggesting that", "suggesting",
    "potentially", "possibly", "perhaps", "probably",
]

# Emotional / loaded language indicators
EMOTIONAL_LANGUAGE: list[str] = [
    "shocking", "outrageous", "alarming", "devastating", "horrifying",
    "explosive", "bombshell", "stunning", "jaw-dropping", "terrifying",
    "unprecedented", "catastrophic", "disastrous", "scandalous",
    "shameful", "disgraceful", "appalling", "egregious", "reckless",
    "sinister", "insidious", "toxic", "predatory", "ruthless",
    "brazen", "defiant", "embattled", "beleaguered", "under fire",
    "under siege", "slammed", "blasted", "hammered", "crushed",
    "destroyed", "eviscerated", "torched", "ripped", "grilled",
    "excoriated", "lambasted",
]

# Passive/victim vs. active/powerful framing indicators
PASSIVE_FRAMING: list[str] = [
    "was forced to", "had to", "was compelled", "was pressured",
    "faces criticism", "faces backlash", "under scrutiny",
    "was hit by", "was plagued by", "was rocked by",
    "struggled", "stumbled", "faltered", "fumbled",
    "failed to", "refused to", "declined to comment",
    "came under fire", "was accused of", "was blamed for",
    "would say almost nothing", "would not say",
    "declined to answer", "declined to respond",
    "quietly built", "quietly removed", "quietly deleted",
    "secretly", "covertly", "surreptitiously",
]

ACTIVE_FRAMING: list[str] = [
    "announced", "launched", "unveiled", "pioneered", "led",
    "spearheaded", "championed", "drove", "transformed",
    "innovated", "invested", "expanded", "committed to",
    "doubled down on", "accelerated", "delivered",
    "outperformed", "exceeded expectations", "set a record",
]

# Comparative framing indicators
NEGATIVE_COMPARISON: list[str] = [
    "lags behind", "falls short", "trails", "unlike",
    "while competitors", "compared unfavorably", "worse than",
    "less than", "behind", "failed where", "losing to",
    "outpaced by", "overshadowed by",
]

POSITIVE_COMPARISON: list[str] = [
    "leads", "ahead of", "outperforms", "surpasses",
    "dominates", "eclipses", "outshines", "beats",
    "better than", "more than", "exceeds", "tops",
]


@dataclass
class SentimentResult:
    """Multi-dimensional sentiment analysis result.

    Eight dimensions capture different aspects of media framing
    beyond simple positive/negative sentiment.
    """

    overall_tone: float = 0.0                  # -1.0 to 1.0
    emotional_language_intensity: float = 0.0  # 0.0 to 1.0
    source_authority_framing: float = 0.0      # -1.0 to 1.0
    agency_attribution: float = 0.0            # -1.0 to 1.0
    headline_body_alignment: float = 0.0       # -1.0 to 1.0
    anonymous_source_ratio: float = 0.0        # 0.0 to 1.0
    speculative_language_ratio: float = 0.0    # 0.0 to 1.0
    comparative_framing: float = 0.0           # -1.0 to 1.0


def analyze_vader(text: str) -> dict:
    """Run VADER sentiment analysis on text.

    Args:
        text: Text to analyze.

    Returns:
        Dict with keys: neg, neu, pos, compound (-1 to 1).
    """
    if not text:
        return {"neg": 0.0, "neu": 1.0, "pos": 0.0, "compound": 0.0}
    return _vader.polarity_scores(text)


def analyze_textblob(text: str) -> dict:
    """Run TextBlob sentiment analysis on text.

    Args:
        text: Text to analyze.

    Returns:
        Dict with keys: polarity (-1 to 1), subjectivity (0 to 1).
    """
    if not text:
        return {"polarity": 0.0, "subjectivity": 0.0}
    blob = TextBlob(text)
    return {
        "polarity": blob.sentiment.polarity,
        "subjectivity": blob.sentiment.subjectivity,
    }


def count_anonymous_sources(text: str) -> tuple[int, int]:
    """Count anonymous and total source attributions in text.

    Args:
        text: Article text to analyze.

    Returns:
        Tuple of (anonymous_source_count, total_source_count).
    """
    anonymous_count = 0
    for pattern in ANONYMOUS_SOURCE_PATTERNS:
        anonymous_count += len(pattern.findall(text))

    named_count = 0
    for pattern in NAMED_SOURCE_PATTERNS:
        named_count += len(pattern.findall(text))

    total = anonymous_count + named_count
    return anonymous_count, total


def measure_speculative_language(text: str) -> float:
    """Measure the ratio of speculative language in text.

    Args:
        text: Article text to analyze.

    Returns:
        Float between 0.0 and 1.0 representing the density of
        speculative phrases relative to text length.
    """
    if not text:
        return 0.0

    text_lower = text.lower()
    word_count = max(len(text.split()), 1)
    spec_count = 0

    for phrase in SPECULATIVE_PHRASES:
        # Count occurrences of each phrase
        escaped = re.escape(phrase)
        matches = re.findall(rf"\b{escaped}\b", text_lower)
        spec_count += len(matches)

    # Normalize: speculative phrases per 100 words, capped at 1.0
    ratio = min(spec_count / (word_count / 50), 1.0)
    return round(ratio, 4)


def _measure_emotional_intensity(text: str) -> float:
    """Measure emotional/loaded language intensity.

    Returns a 0.0–1.0 score based on density of emotional terms.
    """
    if not text:
        return 0.0

    text_lower = text.lower()
    word_count = max(len(text.split()), 1)
    emotional_count = 0

    for term in EMOTIONAL_LANGUAGE:
        escaped = re.escape(term)
        matches = re.findall(rf"\b{escaped}\b", text_lower)
        emotional_count += len(matches)

    # Normalize: emotional terms per 100 words, capped at 1.0
    intensity = min(emotional_count / (word_count / 100), 1.0)
    return round(intensity, 4)


def _measure_agency(text: str) -> float:
    """Measure agency attribution framing.

    Returns -1.0 (passive/victim) to 1.0 (active/powerful).
    """
    if not text:
        return 0.0

    text_lower = text.lower()
    passive_count = 0
    active_count = 0

    for phrase in PASSIVE_FRAMING:
        escaped = re.escape(phrase)
        passive_count += len(re.findall(rf"\b{escaped}\b", text_lower))

    for phrase in ACTIVE_FRAMING:
        escaped = re.escape(phrase)
        active_count += len(re.findall(rf"\b{escaped}\b", text_lower))

    total = passive_count + active_count
    if total == 0:
        return 0.0

    # Scale from -1 (all passive) to +1 (all active)
    score = (active_count - passive_count) / total
    return round(score, 4)


def _measure_source_authority(text: str) -> float:
    """Measure how sources are used to frame the subject.

    Returns -1.0 (sources used to undermine) to 1.0 (sources validate).
    Based on ratio of named vs anonymous sources and attribution verb tone.
    """
    anon_count, total_count = count_anonymous_sources(text)

    if total_count == 0:
        return 0.0

    # More named sources = higher authority framing
    # More anonymous sources = lower authority framing
    named_count = total_count - anon_count
    score = (named_count - anon_count) / total_count
    return round(score, 4)


def _measure_headline_alignment(headline: str, body: str) -> float:
    """Measure how well the headline represents the article body.

    Compares sentiment direction between headline and body.
    Returns -1.0 (contradictory) to 1.0 (aligned).
    """
    if not headline or not body:
        return 0.0

    headline_vader = analyze_vader(headline)
    body_vader = analyze_vader(body)

    h_compound = headline_vader["compound"]
    b_compound = body_vader["compound"]

    # If both have the same sign and similar magnitude, they're aligned
    # If opposite signs, they're misaligned
    if h_compound == 0 and b_compound == 0:
        return 0.0

    # Check if same direction
    if (h_compound >= 0 and b_compound >= 0) or (h_compound < 0 and b_compound < 0):
        # Same direction — alignment is based on magnitude similarity
        if max(abs(h_compound), abs(b_compound)) == 0:
            return 0.0
        magnitude_ratio = min(abs(h_compound), abs(b_compound)) / max(abs(h_compound), abs(b_compound))

        # If headline is much more extreme than body, slight penalty
        if abs(h_compound) > abs(b_compound) * 2:
            return round(magnitude_ratio * 0.5, 4)
        return round(magnitude_ratio, 4)
    else:
        # Opposite directions — misalignment
        diff = abs(h_compound - b_compound)
        return round(-min(diff, 1.0), 4)


def _measure_comparative_framing(text: str) -> float:
    """Measure how the subject is compared to peers.

    Returns -1.0 (unfavorable comparisons) to 1.0 (favorable).
    """
    if not text:
        return 0.0

    text_lower = text.lower()
    neg_count = 0
    pos_count = 0

    for phrase in NEGATIVE_COMPARISON:
        escaped = re.escape(phrase)
        neg_count += len(re.findall(rf"\b{escaped}\b", text_lower))

    for phrase in POSITIVE_COMPARISON:
        escaped = re.escape(phrase)
        pos_count += len(re.findall(rf"\b{escaped}\b", text_lower))

    total = neg_count + pos_count
    if total == 0:
        return 0.0

    score = (pos_count - neg_count) / total
    return round(score, 4)


def analyze_composite(text: str, headline: str = "") -> SentimentResult:
    """Run composite multi-dimensional sentiment analysis.

    Combines VADER, TextBlob, and custom dimension analyzers to produce
    an 8-dimension SentimentResult.

    Args:
        text: Full article text.
        headline: Article headline (optional, used for alignment check).

    Returns:
        SentimentResult with all 8 dimensions calculated.
    """
    if not text:
        return SentimentResult()

    # 1. Overall tone: blend VADER compound and TextBlob polarity
    vader = analyze_vader(text)
    tb = analyze_textblob(text)
    overall_tone = round(0.6 * vader["compound"] + 0.4 * tb["polarity"], 4)
    overall_tone = max(-1.0, min(1.0, overall_tone))

    # 2. Emotional language intensity
    emotional_intensity = _measure_emotional_intensity(text)

    # 3. Source authority framing
    source_authority = _measure_source_authority(text)

    # 4. Agency attribution
    agency = _measure_agency(text)

    # 5. Headline-body alignment
    alignment = _measure_headline_alignment(headline, text)

    # 6. Anonymous source ratio
    anon_count, total_sources = count_anonymous_sources(text)
    anon_ratio = round(anon_count / total_sources, 4) if total_sources > 0 else 0.0

    # 7. Speculative language ratio
    spec_ratio = measure_speculative_language(text)

    # 8. Comparative framing
    comparative = _measure_comparative_framing(text)

    return SentimentResult(
        overall_tone=overall_tone,
        emotional_language_intensity=emotional_intensity,
        source_authority_framing=source_authority,
        agency_attribution=agency,
        headline_body_alignment=alignment,
        anonymous_source_ratio=anon_ratio,
        speculative_language_ratio=spec_ratio,
        comparative_framing=comparative,
    )
