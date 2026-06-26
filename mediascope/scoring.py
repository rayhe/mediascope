"""High-level asymmetry scoring orchestrator.

Wraps ``score.asymmetry`` and ``score.statistical`` into a CLI-friendly
class.
"""

from __future__ import annotations

from mediascope.score.asymmetry import calculate_asymmetry
from mediascope.score.statistical import welch_t_test, cohens_d, bootstrap_ci


class AsymmetryScorer:
    """Calculate and format asymmetry scores for CLI output.

    Usage::

        scorer = AsymmetryScorer(target_entity="Meta")
        result = scorer.score(target_scores=[...], peer_scores=[...])
    """

    def __init__(self, target_entity: str = "Meta"):
        self.target_entity = target_entity

    def score(
        self,
        target_scores: list[float],
        peer_scores: list[float],
        peer_entities: list[str] | None = None,
        publication_slug: str = "",
        period_start: str = "",
        period_end: str = "",
    ) -> dict:
        """Run asymmetry calculation and return a results dict."""
        result = calculate_asymmetry(
            target_scores=target_scores,
            peer_scores=peer_scores,
            target_entity=self.target_entity,
            peer_entities=peer_entities or [],
            publication_slug=publication_slug,
            period_start=period_start,
            period_end=period_end,
        )
        return result
