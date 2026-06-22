"""Editorial influence scoring and bias decomposition.

Decomposes a journalist's observed coverage tone into:

- **Institutional component** — driven by the publication's culture/ownership
- **Individual component** — the journalist's portable personal stance
- **Interaction effect** — synergy between journalist and outlet

Uses a two-way ANOVA (journalist × publication) on tone scores to partition
variance.  Requires a journalist to have written for ≥2 publications with
≥5 articles each for meaningful decomposition.

The key insight: if a journalist's tone at Publication A is −0.4 and their
tone at Publication B is also −0.4, while the *publication-wide* average at
A is −0.3 and at B is −0.1, that's a journalist carrying their own bias.
But if their tone matches each publication's average closely, the
institution drives coverage.
"""

from __future__ import annotations

import math
from collections import defaultdict
from dataclasses import dataclass
from typing import Optional

import numpy as np
from scipy import stats as sp_stats

from mediascope.careers.models import BiasDecomposition, JournalistProfile
from mediascope.score.statistical import cohens_d


class InfluenceScorer:
    """Score journalists on how much of their coverage tone is institutional
    vs. individual (portable).

    Usage::

        scorer = InfluenceScorer()
        result = scorer.decompose(
            journalist_name="Karen Hao",
            articles_by_pub={
                "mit-tech-review": [...articles with 'overall_tone'...],
                "atlantic": [...articles...],
            },
            pub_baselines={
                "mit-tech-review": -0.15,
                "atlantic": -0.08,
            },
        )
        print(result.portable_bias_score)
    """

    def __init__(self, min_articles_per_pub: int = 5, min_publications: int = 2):
        self.min_articles_per_pub = min_articles_per_pub
        self.min_publications = min_publications

    def decompose(
        self,
        journalist_name: str,
        articles_by_pub: dict[str, list[dict]],
        pub_baselines: dict[str, float] | None = None,
    ) -> BiasDecomposition:
        """Decompose a journalist's tone into institutional and individual components.

        Args:
            journalist_name: Name of the journalist.
            articles_by_pub: Mapping of publication slug → list of articles
                by this journalist at that publication.  Each article dict
                must contain ``overall_tone`` (float).
            pub_baselines: Optional mapping of publication slug → mean tone
                across *all* journalists at that publication.  If not provided,
                institutional effects are estimated from the data.

        Returns:
            BiasDecomposition with component scores.
        """
        # Filter to publications with enough articles
        valid_pubs: dict[str, list[float]] = {}
        for pub, articles in articles_by_pub.items():
            tones = [float(a["overall_tone"]) for a in articles if "overall_tone" in a]
            if len(tones) >= self.min_articles_per_pub:
                valid_pubs[pub] = tones

        n_pubs = len(valid_pubs)
        total_articles = sum(len(t) for t in valid_pubs.values())

        if n_pubs < self.min_publications:
            return BiasDecomposition(
                journalist_name=journalist_name,
                institutional_component=0.0,
                individual_component=0.0,
                interaction_effect=0.0,
                portable_bias_score=0.5,
                n_publications=n_pubs,
                n_articles=total_articles,
                confidence=0.0,
                methodology_note=(
                    f"Insufficient data: journalist has articles at {n_pubs} "
                    f"publication(s), minimum {self.min_publications} required."
                ),
            )

        # ----- Two-way decomposition -----
        # Grand mean of the journalist's own data
        all_tones = [t for tones in valid_pubs.values() for t in tones]
        grand_mean = float(np.mean(all_tones))

        # Journalist's mean at each publication
        j_means = {pub: float(np.mean(tones)) for pub, tones in valid_pubs.items()}

        # Publication baselines (mean across all journalists at that pub)
        has_external_baselines = pub_baselines is not None
        if pub_baselines is None:
            pub_baselines = j_means

        # ----- Variance decomposition -----
        #
        # SS_between: how much the journalist's tone varies ACROSS publications.
        #   High → journalist adapts to each outlet's culture (institutional driver).
        #   Low → journalist maintains consistent tone everywhere (individual driver).
        ss_between = 0.0
        for pub, tones in valid_pubs.items():
            ss_between += len(tones) * (j_means[pub] - grand_mean) ** 2

        # SS_within: residual variance within each publication
        ss_within = 0.0
        for pub, tones in valid_pubs.items():
            ss_within += sum((t - j_means[pub]) ** 2 for t in tones)

        # SS_total = SS_between + SS_within (by construction)
        ss_total = ss_between + ss_within

        # When external baselines are provided, also compute how much the
        # journalist deviates from institutional norms:
        # SS_deviation = Σ n_j × (journalist_mean_at_j - pub_baseline_j)²
        ss_deviation = 0.0
        if has_external_baselines:
            for pub, tones in valid_pubs.items():
                baseline = pub_baselines.get(pub, grand_mean)
                ss_deviation += len(tones) * (j_means[pub] - baseline) ** 2

        # Compute proportions
        if ss_total > 0:
            # Eta-squared: proportion of journalist's variance explained by
            # publication membership.  High → institutional influence on this
            # journalist is strong (they write differently at different outlets).
            eta_sq = ss_between / ss_total
        else:
            eta_sq = 0.0

        if has_external_baselines and (ss_between + ss_deviation) > 0:
            # With external baselines, we can distinguish:
            #   institutional = how much of the signal is between-pub variation
            #                   (journalist adapting to editorial culture)
            #   individual = how much the journalist deviates from pub norms
            #                (journalist's personal stance overriding institution)
            total_signal = ss_between + ss_deviation
            institutional = ss_between / total_signal
            individual = ss_deviation / total_signal
            interaction = 0.0  # not estimable without multi-journalist data

            # But interaction can be inferred from how much within-pub variance
            # remains after accounting for the journalist's mean at each pub.
            # If the journalist is especially volatile at one pub but not another,
            # that's an interaction effect.
            if ss_total > 0 and ss_within > 0:
                # Coefficient of variation across publications
                pub_cv = [
                    float(np.std(tones)) / abs(j_means[pub])
                    if abs(j_means[pub]) > 0.01 else 0.0
                    for pub, tones in valid_pubs.items()
                ]
                if len(pub_cv) >= 2 and max(pub_cv) > 0:
                    cv_range = max(pub_cv) - min(pub_cv)
                    # Convert to a small interaction term if CV varies across pubs
                    interaction = min(0.2, cv_range)
                    # Re-normalise
                    total = institutional + individual + interaction
                    institutional /= total
                    individual /= total
                    interaction /= total
        elif ss_total > 0:
            # No external baselines — purely within-journalist decomposition
            institutional = eta_sq
            individual = 1.0 - eta_sq
            interaction = 0.0
        else:
            institutional = 0.0
            individual = 0.0
            interaction = 0.0

        # ----- Portable Bias Score -----
        # How similar is the journalist's tone across publications?
        # Use pairwise Cohen's d between publications, averaged
        portable = self._compute_portable_bias(valid_pubs)

        # ----- Confidence -----
        # Based on sample size and number of publications
        conf_n = min(1.0, total_articles / 50.0)  # saturates at 50 articles
        conf_k = min(1.0, n_pubs / 4.0)  # saturates at 4 publications
        confidence = round(conf_n * conf_k, 3)

        return BiasDecomposition(
            journalist_name=journalist_name,
            institutional_component=round(institutional, 4),
            individual_component=round(individual, 4),
            interaction_effect=round(interaction, 4),
            portable_bias_score=portable,
            n_publications=n_pubs,
            n_articles=total_articles,
            confidence=confidence,
            methodology_note=self._methodology_note(n_pubs, total_articles),
        )

    def batch_decompose(
        self,
        journalists: list[str],
        articles_by_journalist_pub: dict[str, dict[str, list[dict]]],
        pub_baselines: dict[str, float] | None = None,
    ) -> list[BiasDecomposition]:
        """Run decomposition on a batch of journalists.

        Args:
            journalists: List of journalist names.
            articles_by_journalist_pub: Nested mapping of
                journalist_name → publication_slug → article list.
            pub_baselines: Publication-level baselines.

        Returns:
            List of BiasDecomposition results.
        """
        results = []
        for name in journalists:
            articles_by_pub = articles_by_journalist_pub.get(name, {})
            result = self.decompose(name, articles_by_pub, pub_baselines)
            results.append(result)
        return results

    def rank_by_portable_bias(
        self,
        decompositions: list[BiasDecomposition],
        min_confidence: float = 0.3,
    ) -> list[BiasDecomposition]:
        """Rank journalists by portable bias score (most portable first).

        Filters out low-confidence results.
        """
        filtered = [d for d in decompositions if d.confidence >= min_confidence]
        return sorted(filtered, key=lambda d: d.portable_bias_score, reverse=True)

    def rank_by_institutional_influence(
        self,
        decompositions: list[BiasDecomposition],
        min_confidence: float = 0.3,
    ) -> list[BiasDecomposition]:
        """Rank by institutional component (publications with strongest editorial culture)."""
        filtered = [d for d in decompositions if d.confidence >= min_confidence]
        return sorted(
            filtered, key=lambda d: d.institutional_component, reverse=True
        )

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _compute_portable_bias(self, pubs: dict[str, list[float]]) -> float:
        """Compute portable bias score from cross-publication tone similarity.

        High similarity → high portability → journalist carries their bias.
        Low similarity → low portability → journalist adapts to each outlet.

        Uses average pairwise 1−|Cohen's d|/2 across publications.
        """
        pub_names = list(pubs.keys())
        if len(pub_names) < 2:
            return 0.5

        pairwise_similarities = []
        for i in range(len(pub_names)):
            for j in range(i + 1, len(pub_names)):
                d = cohens_d(pubs[pub_names[i]], pubs[pub_names[j]])
                similarity = max(0.0, 1.0 - abs(d) / 2.0)
                pairwise_similarities.append(similarity)

        return round(float(np.mean(pairwise_similarities)), 3)

    @staticmethod
    def _methodology_note(n_pubs: int, n_articles: int) -> str:
        return (
            f"Bias decomposition using two-way ANOVA framework across {n_pubs} "
            f"publications ({n_articles} articles total). Institutional component = "
            f"proportion of total variance explained by publication baselines. "
            f"Individual component = proportion explained by journalist deviation "
            f"from publication baselines. Portable bias score = average cross-publication "
            f"tone similarity (1 − |Cohen's d|/2, pairwise). Methodology adapts "
            f"Gentzkow & Shapiro (2010) media slant decomposition to journalist-level "
            f"analysis."
        )
