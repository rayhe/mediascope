"""Quality standards checker for MediaScope content.

Checks articles for banned AI-slop phrases, excessive em dashes,
missing counterarguments/limitations/methodology, and generates
quality reports with scored assessments.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Optional


BANNED_PHRASES: list[str] = [
    "delve",
    "tapestry",
    "landscape",
    "Moreover,",
    "Furthermore,",
    "In conclusion,",
    "It's worth noting",
    "It bears mentioning",
    "game-changer",
    "paradigm shift",
    "synergy",
    "leverage",
    "ecosystem",
    "deep dive",
    "unpack",
    "robust",
    "holistic",
    "at the end of the day",
    "moving forward",
    "circle back",
]

EM_DASH_LIMIT: int = 3


@dataclass
class QualityIssue:
    """A single quality issue found in the text."""

    severity: str  # "error", "warning", "info"
    category: str
    description: str
    line_number: Optional[int] = None


@dataclass
class QualityReport:
    """Aggregate quality report for a piece of text."""

    passed: bool
    score: int  # 0–100
    issues: list[QualityIssue] = field(default_factory=list)
    citations_verified: int = 0
    citations_total: int = 0
    banned_phrases_found: list[str] = field(default_factory=list)
    em_dash_count: int = 0
    has_counterargument: bool = False
    has_limitations: bool = False
    has_methodology: bool = False


def check_quality(text: str, metadata: dict | None = None) -> QualityReport:
    """Run all quality checks on a piece of text.

    Checks performed:
        1. Banned phrase scan (case-insensitive for most, case-sensitive for capitalized phrases)
        2. Em dash count (— U+2014)
        3. Counterargument presence
        4. Limitations section
        5. Methodology reference

    Scoring weights:
        - Banned phrase found: −5 per occurrence (error)
        - Em dash over limit: −3 per extra (warning)
        - Missing counterargument: −10 (warning)
        - Missing limitations: −8 (warning)
        - Missing methodology: −5 (info)

    Args:
        text: The article/report text to check.
        metadata: Optional dict with additional context (e.g. "has_data" flag).

    Returns:
        QualityReport with pass/fail, score, and itemized issues.
    """
    issues: list[QualityIssue] = []
    score = 100  # start perfect, deduct
    lines = text.split("\n")
    text_lower = text.lower()

    # ── 1. Banned phrases ────────────────────────────────────────────
    found_phrases: list[str] = []
    for phrase in BANNED_PHRASES:
        # For phrases starting with uppercase, check case-sensitive first
        # then fall back to case-insensitive
        if phrase[0].isupper():
            pattern = re.compile(re.escape(phrase))
        else:
            pattern = re.compile(re.escape(phrase), re.IGNORECASE)

        for i, line in enumerate(lines, start=1):
            for match in pattern.finditer(line):
                if phrase not in found_phrases:
                    found_phrases.append(phrase)
                issues.append(QualityIssue(
                    severity="error",
                    category="banned_phrase",
                    description=f'Banned phrase found: "{phrase}"',
                    line_number=i,
                ))
                score -= 5

    # ── 2. Em dash count ─────────────────────────────────────────────
    em_dash_count = text.count("—")
    if em_dash_count > EM_DASH_LIMIT:
        excess = em_dash_count - EM_DASH_LIMIT
        issues.append(QualityIssue(
            severity="warning",
            category="em_dash_overuse",
            description=(
                f"Em dash count ({em_dash_count}) exceeds limit of "
                f"{EM_DASH_LIMIT} by {excess}."
            ),
        ))
        score -= 3 * excess

    # ── 3. Counterargument check ─────────────────────────────────────
    counterargument_signals = [
        "however",
        "counterargument",
        "critics argue",
        "on the other hand",
        "opposing view",
        "counter-argument",
        "critics say",
        "skeptics point",
        "detractors argue",
    ]
    has_counterargument = any(signal in text_lower for signal in counterargument_signals)
    if not has_counterargument:
        issues.append(QualityIssue(
            severity="warning",
            category="missing_counterargument",
            description=(
                "No counterargument or opposing viewpoint detected. "
                "Consider adding balance."
            ),
        ))
        score -= 10

    # ── 4. Limitations check ─────────────────────────────────────────
    limitation_signals = [
        "limitation",
        "caveat",
        "this analysis does not",
        "we could not",
        "data was unavailable",
        "important to note that this",
        "scope of this",
    ]
    has_limitations = any(signal in text_lower for signal in limitation_signals)
    if not has_limitations:
        issues.append(QualityIssue(
            severity="warning",
            category="missing_limitations",
            description="No limitations section or acknowledgment detected.",
        ))
        score -= 8

    # ── 5. Methodology check ─────────────────────────────────────────
    methodology_signals = [
        "methodology",
        "method:",
        "our approach",
        "we analyzed",
        "data collection",
        "sampling",
        "statistical",
        "we measured",
    ]
    has_methodology = any(signal in text_lower for signal in methodology_signals)
    if not has_methodology:
        issues.append(QualityIssue(
            severity="info",
            category="missing_methodology",
            description="No methodology reference detected.",
        ))
        score -= 5

    # Clamp score
    score = max(0, min(100, score))

    return QualityReport(
        passed=score >= 60 and not any(i.severity == "error" for i in issues),
        score=score,
        issues=issues,
        banned_phrases_found=found_phrases,
        em_dash_count=em_dash_count,
        has_counterargument=has_counterargument,
        has_limitations=has_limitations,
        has_methodology=has_methodology,
    )
