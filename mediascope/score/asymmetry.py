"""Asymmetry scoring engine for media coverage analysis.

Computes sentiment asymmetry between a target entity and peer entities
in a publication's coverage, using Welch's t-test, Cohen's d, and
bootstrap confidence intervals.
"""

from __future__ import annotations

import math
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

import numpy as np
from scipy import stats

from mediascope.score.statistical import (
    bootstrap_ci,
    cohens_d,
    interpret_effect_size,
    is_significant,
    welch_t_test,
)


@dataclass
class AsymmetryScore:
    """Sentiment asymmetry score between a target entity and peer entities."""

    publication_slug: str
    target_entity: str
    peer_entities: list[str]
    period_start: datetime
    period_end: datetime
    target_avg_tone: float
    peer_avg_tone: float
    asymmetry_score: float  # target_avg_tone - peer_avg_tone
    article_count_target: int
    article_count_peers: int
    t_statistic: float
    p_value: float
    cohens_d: float
    confidence_interval_lower: float
    confidence_interval_upper: float
    is_significant: bool  # p < 0.05


@dataclass
class AsymmetryReport:
    """Comprehensive asymmetry report across multiple entities."""

    scores_by_entity: dict[str, AsymmetryScore]
    overall_asymmetry: float
    most_negative_entity: Optional[str]
    most_positive_entity: Optional[str]
    period: tuple[datetime, datetime]
    methodology_note: str


def calculate_asymmetry(
    target_scores: list[float],
    peer_scores: list[float],
    target_entity: str,
    peer_entities: list[str],
    publication_slug: str,
    period_start: datetime,
    period_end: datetime,
) -> AsymmetryScore:
    """Calculate the asymmetry score between target and peer sentiment distributions.

    Args:
        target_scores: Sentiment scores for articles mentioning the target entity.
        peer_scores: Sentiment scores for articles mentioning peer entities.
        target_entity: Name of the entity under analysis.
        peer_entities: Names of comparison entities.
        publication_slug: Identifier for the publication.
        period_start: Start of the analysis window.
        period_end: End of the analysis window.

    Returns:
        AsymmetryScore with full statistical details.
    """
    target_avg = float(np.mean(target_scores)) if target_scores else 0.0
    peer_avg = float(np.mean(peer_scores)) if peer_scores else 0.0
    asymmetry = target_avg - peer_avg

    t_stat, p_val = welch_t_test(target_scores, peer_scores)
    d = cohens_d(target_scores, peer_scores)
    ci_lower, ci_upper = bootstrap_ci(target_scores, peer_scores, n_bootstrap=1000)

    return AsymmetryScore(
        publication_slug=publication_slug,
        target_entity=target_entity,
        peer_entities=peer_entities,
        period_start=period_start,
        period_end=period_end,
        target_avg_tone=target_avg,
        peer_avg_tone=peer_avg,
        asymmetry_score=asymmetry,
        article_count_target=len(target_scores),
        article_count_peers=len(peer_scores),
        t_statistic=t_stat,
        p_value=p_val,
        cohens_d=d,
        confidence_interval_lower=ci_lower,
        confidence_interval_upper=ci_upper,
        is_significant=is_significant(p_val),
    )


def generate_asymmetry_report(
    articles: list[dict],
    publication_slug: str,
    target_entity: str,
    period_start: datetime,
    period_end: datetime,
) -> AsymmetryReport:
    """Generate a comprehensive asymmetry report from analyzed articles.

    Each article dict is expected to have:
        - "entities": list of entity names mentioned
        - "sentiment": dict with "overall_tone" (float, e.g. -1 to 1)
        - "published_date": datetime (optional, for filtering)

    The function groups articles by entity, calculates pairwise asymmetry
    between the target entity and every other entity, and returns a report.

    Args:
        articles: List of analyzed article dicts.
        publication_slug: Identifier for the publication.
        target_entity: The entity whose coverage is being evaluated.
        period_start: Analysis window start.
        period_end: Analysis window end.

    Returns:
        AsymmetryReport with per-entity scores and overall summary.
    """
    # Group sentiment scores by entity
    entity_scores: dict[str, list[float]] = defaultdict(list)
    target_lower = target_entity.lower()

    for article in articles:
        entities = article.get("entities", [])
        tone = article.get("sentiment", {}).get("overall_tone")
        if tone is None:
            continue

        tone = float(tone)
        for entity in entities:
            entity_scores[entity.lower()].append(tone)

    # Extract target scores
    target_scores = entity_scores.pop(target_lower, [])

    if not target_scores:
        return AsymmetryReport(
            scores_by_entity={},
            overall_asymmetry=0.0,
            most_negative_entity=None,
            most_positive_entity=None,
            period=(period_start, period_end),
            methodology_note=_methodology_note(0, 0),
        )

    # Calculate asymmetry for each peer entity
    scores_by_entity: dict[str, AsymmetryScore] = {}
    all_peer_scores: list[float] = []

    for entity_key, scores in entity_scores.items():
        if len(scores) < 2:
            continue  # need at least 2 articles for meaningful stats

        asym = calculate_asymmetry(
            target_scores=target_scores,
            peer_scores=scores,
            target_entity=target_entity,
            peer_entities=[entity_key],
            publication_slug=publication_slug,
            period_start=period_start,
            period_end=period_end,
        )
        scores_by_entity[entity_key] = asym
        all_peer_scores.extend(scores)

    # Overall asymmetry: target vs all peers combined
    overall_asymmetry = 0.0
    if all_peer_scores:
        target_mean = float(np.mean(target_scores))
        peer_mean = float(np.mean(all_peer_scores))
        overall_asymmetry = target_mean - peer_mean

    # Find most negative/positive
    most_negative: Optional[str] = None
    most_positive: Optional[str] = None
    if scores_by_entity:
        most_negative = min(scores_by_entity, key=lambda e: scores_by_entity[e].asymmetry_score)
        most_positive = max(scores_by_entity, key=lambda e: scores_by_entity[e].asymmetry_score)

    return AsymmetryReport(
        scores_by_entity=scores_by_entity,
        overall_asymmetry=overall_asymmetry,
        most_negative_entity=most_negative,
        most_positive_entity=most_positive,
        period=(period_start, period_end),
        methodology_note=_methodology_note(len(target_scores), len(all_peer_scores)),
    )


def _methodology_note(n_target: int, n_peers: int) -> str:
    """Generate the methodology note for a report."""
    return (
        f"Asymmetry scores computed via Welch's t-test (unequal variance) comparing "
        f"sentiment distributions for {n_target} target articles against {n_peers} peer "
        f"articles. Effect sizes reported as Cohen's d. Confidence intervals derived from "
        f"bootstrap resampling (1,000 iterations, 95% CI). Sentiment scores were generated "
        f"by a multi-dimensional LLM-based analyzer; individual scores are not ground truth "
        f"but the comparative distribution is meaningful."
    )
