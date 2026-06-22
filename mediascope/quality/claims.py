"""Claim-evidence mapping for article analysis.

Extracts factual claims from text and maps each to its supporting
evidence (or lack thereof).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Claim:
    """A factual claim extracted from text."""

    text: str
    evidence_type: str  # "statistic", "quote", "citation", "assertion"
    has_source: bool = False
    source_text: str = ""
    confidence: float = 0.0  # 0.0–1.0, how confident we are this IS a claim


# ── Patterns ─────────────────────────────────────────────────────────

# Statistics: numbers, percentages, dollar amounts, multipliers
_STAT_PATTERN = re.compile(
    r"(?:^|(?<=\s))"
    r"(?:"
    r"\d[\d,]*\.?\d*\s*%"  # percentages
    r"|\$\s*\d[\d,]*\.?\d*\s*(?:billion|million|trillion|B|M|T)?"  # dollar amounts
    r"|\d[\d,]*\.?\d*\s*(?:billion|million|trillion|percent|times|fold)"  # magnitude
    r"|\d[\d,]*\.?\d*x"  # multipliers
    r")",
    re.IGNORECASE,
)

# Quotes: text inside quotation marks (straight or curly)
_QUOTE_PATTERN = re.compile(
    r'["\u201c]([^"\u201d]{10,300})["\u201d]',
)

# Citations: URLs, "according to", formal references
_CITATION_SIGNAL = re.compile(
    r"(?:according to|as reported by|per\s|citing|(?:a\s)?(?:study|report|analysis|survey)\s(?:by|from|published))",
    re.IGNORECASE,
)

# Attribution after a quote
_ATTRIBUTION_AFTER_QUOTE = re.compile(
    r'["\u201d]\s*(?:,\s*)?(?:said|told|wrote|stated|noted|explained|added|argued)\s+([^,\.]{3,60})',
    re.IGNORECASE,
)

# Assertive language (claims without evidence)
_ASSERTION_SIGNALS = re.compile(
    r"\b(?:is\s+(?:the\s+)?(?:largest|smallest|best|worst|most|least|only|first|leading))"
    r"|(?:has\s+(?:never|always|consistently))"
    r"|(?:will\s+(?:definitely|certainly|inevitably|undoubtedly))"
    r"|(?:proves?\s+that)"
    r"|(?:clearly\s+(?:shows|demonstrates|indicates))",
    re.IGNORECASE,
)


def extract_claims(text: str) -> list[Claim]:
    """Identify factual claims in text and classify by evidence type.

    Scans for:
        - Statistics (numbers, percentages, dollar amounts)
        - Quotes (attributed statements)
        - Citations (URLs, "according to" attributions)
        - Assertions (unsupported factual claims)

    Args:
        text: Article or report text.

    Returns:
        List of Claim objects.
    """
    claims: list[Claim] = []
    sentences = _split_sentences(text)

    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) < 15:
            continue

        claim_types_found: list[str] = []

        # Check for statistics
        stat_matches = _STAT_PATTERN.findall(sentence)
        if stat_matches:
            claim_types_found.append("statistic")

        # Check for quotes
        quote_matches = _QUOTE_PATTERN.findall(sentence)
        if quote_matches:
            claim_types_found.append("quote")

        # Check for citation signals
        if _CITATION_SIGNAL.search(sentence):
            claim_types_found.append("citation")

        # Check for bare assertions
        if _ASSERTION_SIGNALS.search(sentence) and not claim_types_found:
            claim_types_found.append("assertion")

        if not claim_types_found:
            continue

        # Determine primary evidence type (preference order)
        for etype in ["statistic", "quote", "citation", "assertion"]:
            if etype in claim_types_found:
                evidence_type = etype
                break
        else:
            evidence_type = "assertion"

        # Determine if the claim has a source
        has_source = _has_source(sentence)
        source_text = _extract_source_text(sentence) if has_source else ""

        # Confidence scoring
        confidence = _score_confidence(sentence, evidence_type, has_source)

        claims.append(Claim(
            text=sentence,
            evidence_type=evidence_type,
            has_source=has_source,
            source_text=source_text,
            confidence=confidence,
        ))

    return claims


def map_claims_to_evidence(claims: list[Claim]) -> dict:
    """Map claims to their evidence status.

    Args:
        claims: List of Claim objects.

    Returns:
        Dict with:
            - "sourced": list of claims with sources
            - "unsourced": list of claims without sources
            - "by_type": {evidence_type: [claims]}
            - "total": total claim count
            - "sourced_ratio": fraction of claims with sources
    """
    sourced = [c for c in claims if c.has_source]
    unsourced = [c for c in claims if not c.has_source]

    by_type: dict[str, list[Claim]] = {}
    for claim in claims:
        by_type.setdefault(claim.evidence_type, []).append(claim)

    total = len(claims)
    return {
        "sourced": sourced,
        "unsourced": unsourced,
        "by_type": by_type,
        "total": total,
        "sourced_ratio": len(sourced) / total if total > 0 else 0.0,
    }


def unsupported_claims_ratio(claims: list[Claim]) -> float:
    """Calculate the ratio of claims without any supporting source.

    Args:
        claims: List of Claim objects.

    Returns:
        Float between 0.0 and 1.0. Returns 0.0 if no claims.
    """
    if not claims:
        return 0.0
    unsourced = sum(1 for c in claims if not c.has_source)
    return unsourced / len(claims)


# ── Internal helpers ─────────────────────────────────────────────────

def _split_sentences(text: str) -> list[str]:
    """Split text into sentences (rough but functional)."""
    # Split on sentence-ending punctuation followed by space + uppercase,
    # or on newlines
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z\u201c"])|(?:\n\s*\n)', text)
    result: list[str] = []
    for part in parts:
        # Further split on newlines for bullet points / lists
        for sub in part.split("\n"):
            sub = sub.strip()
            if sub:
                result.append(sub)
    return result


def _has_source(sentence: str) -> bool:
    """Check whether a sentence contains any source attribution."""
    # URL present
    if re.search(r"https?://", sentence):
        return True
    # Attribution pattern
    if _CITATION_SIGNAL.search(sentence):
        return True
    # Quote with attribution
    if _ATTRIBUTION_AFTER_QUOTE.search(sentence):
        return True
    # Parenthetical reference
    if re.search(r"\(\w+(?:\s+et al\.?)?,?\s*\d{4}\)", sentence):
        return True
    return False


def _extract_source_text(sentence: str) -> str:
    """Extract the source attribution text from a sentence."""
    # Try "according to X"
    match = re.search(
        r"(?:according to|as reported by|per|citing)\s+([^,\.;]{3,80})",
        sentence,
        re.IGNORECASE,
    )
    if match:
        return match.group(1).strip()

    # Try post-quote attribution
    match = _ATTRIBUTION_AFTER_QUOTE.search(sentence)
    if match:
        return match.group(1).strip()

    # Try URL
    url_match = re.search(r"https?://[^\s\)\]>,]+", sentence)
    if url_match:
        return url_match.group(0)

    return ""


def _score_confidence(sentence: str, evidence_type: str, has_source: bool) -> float:
    """Score how confident we are that this sentence IS a factual claim (0–1)."""
    score = 0.5  # base

    # Statistics are almost always claims
    if evidence_type == "statistic":
        score += 0.3

    # Quotes are usually evidence, not claims themselves
    if evidence_type == "quote":
        score += 0.1

    # Having a source boosts confidence it's a real claim
    if has_source:
        score += 0.1

    # Assertions without sources are low confidence as claims
    if evidence_type == "assertion" and not has_source:
        score -= 0.1

    # Longer sentences are more likely to be substantive
    if len(sentence) > 100:
        score += 0.05

    return min(1.0, max(0.0, score))
