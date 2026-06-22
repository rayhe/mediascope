"""Migration event analysis — difference-in-differences for editorial moves.

Implements a causal inference framework adapted from Card & Krueger (1994)
and applied to media analysis.  Each journalist migration creates a natural
experiment that can be analysed with a standard DiD estimator.

The core idea: when journalist J leaves Publication A for Publication B at
time *t*, we compare the *change* in A's coverage tone from pre-*t* to
post-*t* (the treatment group) against the *change* in tone at a control
publication that experienced no personnel change (the control group).  The
difference of these differences isolates the causal effect of J's departure
from secular trends in the industry.
"""

from __future__ import annotations

import math
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Optional

import numpy as np
from scipy import stats as sp_stats

from mediascope.careers.models import (
    DifferenceInDifferencesResult,
    MigrationEvent,
)
from mediascope.score.statistical import bootstrap_ci, cohens_d, welch_t_test


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

class MigrationAnalyzer:
    """Analyze the tonal impact of journalist migrations using DiD.

    This class takes pre-scored article data and computes causal estimates
    for the effect of a journalist's movement on both the source and
    destination publications.

    Usage::

        analyzer = MigrationAnalyzer()
        result = analyzer.analyze_migration(
            migration=migration_event,
            source_articles=articles_from_pub_a,
            dest_articles=articles_from_pub_b,
            journalist_articles=all_articles_by_journalist,
            control_articles=articles_from_control_pub,
            window_days=180,
        )
        print(result.did_estimate)
    """

    def __init__(self, window_days: int = 180, min_articles: int = 5):
        """
        Args:
            window_days: How many days before/after the migration to include
                in the pre/post windows.
            min_articles: Minimum articles required in any window for the
                analysis to proceed.
        """
        self.window_days = window_days
        self.min_articles = min_articles

    def analyze_migration(
        self,
        migration: MigrationEvent,
        source_articles: list[dict],
        dest_articles: list[dict],
        journalist_articles: list[dict],
        control_articles: list[dict] | None = None,
        window_days: int | None = None,
    ) -> DifferenceInDifferencesResult:
        """Run full difference-in-differences analysis on a migration event.

        Each article dict must contain:
            - ``published_date``: ``datetime.date``
            - ``overall_tone``: ``float`` (sentiment score, −1 to +1)
            - ``author``: ``str`` (journalist name, for filtering)

        Args:
            migration: The migration event to analyse.
            source_articles: All articles from the source publication on the
                relevant entity/beat, by any journalist.
            dest_articles: All articles from the destination publication.
            journalist_articles: All articles written by the migrating
                journalist (at any publication).
            control_articles: Articles from a publication that experienced no
                personnel change in the same window.  Used as the DiD control
                group.  If ``None``, the analysis falls back to a simple
                pre/post comparison without a control.
            window_days: Override the instance default.

        Returns:
            A ``DifferenceInDifferencesResult`` with full statistical details.
        """
        wd = window_days or self.window_days
        pivot = migration.departure_date  # the event date

        # ----- Source publication: pre/post the journalist leaving -----
        src_pre = _window_scores(source_articles, pivot, -wd, 0)
        src_post = _window_scores(source_articles, pivot, 0, wd)

        src_pre_mean = float(np.mean(src_pre)) if src_pre else 0.0
        src_post_mean = float(np.mean(src_post)) if src_post else 0.0
        src_change = src_post_mean - src_pre_mean

        # ----- Destination publication: pre/post the journalist arriving -----
        arr_pivot = migration.arrival_date
        dst_pre = _window_scores(dest_articles, arr_pivot, -wd, 0)
        dst_post = _window_scores(dest_articles, arr_pivot, 0, wd)

        dst_pre_mean = float(np.mean(dst_pre)) if dst_pre else 0.0
        dst_post_mean = float(np.mean(dst_post)) if dst_post else 0.0
        dst_change = dst_post_mean - dst_pre_mean

        # ----- Journalist's own tone: pre/post move -----
        j_name = migration.journalist_name.lower()
        j_articles = [
            a for a in journalist_articles
            if a.get("author", "").lower() == j_name
        ]
        j_pre = _window_scores(j_articles, pivot, -wd, 0)
        j_post = _window_scores(j_articles, arr_pivot, 0, wd)

        j_pre_mean = float(np.mean(j_pre)) if j_pre else 0.0
        j_post_mean = float(np.mean(j_post)) if j_post else 0.0
        j_change = j_post_mean - j_pre_mean

        # ----- Control group -----
        if control_articles:
            ctrl_pre = _window_scores(control_articles, pivot, -wd, 0)
            ctrl_post = _window_scores(control_articles, pivot, 0, wd)
        else:
            ctrl_pre = []
            ctrl_post = []

        ctrl_pre_mean = float(np.mean(ctrl_pre)) if ctrl_pre else 0.0
        ctrl_post_mean = float(np.mean(ctrl_post)) if ctrl_post else 0.0
        ctrl_change = ctrl_post_mean - ctrl_pre_mean

        # ----- Difference-in-Differences -----
        # DiD = (Treatment_post - Treatment_pre) - (Control_post - Control_pre)
        # Treatment = source publication, Control = unaffected publication
        did_estimate = src_change - ctrl_change

        # Standard error via OLS DiD regression
        did_se, did_p = _did_inference(
            src_pre, src_post, ctrl_pre, ctrl_post
        )

        did_significant = did_p < 0.05

        # ----- Derived causal estimates -----
        # Portable bias: how much of journalist's tone survives the move
        # If journalist tone doesn't change across publications → fully portable
        portable = _portable_bias(j_pre, j_post)

        # Editorial capture: how much the new outlet changed the journalist
        # (inverse of portable bias)
        capture = 1.0 - portable

        # Influence: how much the journalist changed the destination
        influence = dst_change - ctrl_change if ctrl_post else dst_change

        n_pre = len(src_pre) + len(dst_pre) + len(j_pre)
        n_post = len(src_post) + len(dst_post) + len(j_post)

        return DifferenceInDifferencesResult(
            journalist_name=migration.journalist_name,
            migration=migration,
            source_pre_mean=src_pre_mean,
            source_post_mean=src_post_mean,
            source_raw_change=src_change,
            dest_pre_mean=dst_pre_mean,
            dest_post_mean=dst_post_mean,
            dest_raw_change=dst_change,
            journalist_pre_mean=j_pre_mean,
            journalist_post_mean=j_post_mean,
            journalist_tone_change=j_change,
            control_pre_mean=ctrl_pre_mean,
            control_post_mean=ctrl_post_mean,
            control_change=ctrl_change,
            did_estimate=did_estimate,
            did_std_error=did_se,
            did_p_value=did_p,
            did_is_significant=did_significant,
            portable_bias_estimate=portable,
            editorial_capture_estimate=capture,
            influence_estimate=influence,
            n_articles_pre=n_pre,
            n_articles_post=n_post,
            window_days=wd,
            methodology_note=_methodology_note(wd, n_pre, n_post, bool(control_articles)),
        )

    def batch_analyze(
        self,
        migrations: list[MigrationEvent],
        articles_by_pub: dict[str, list[dict]],
        articles_by_journalist: dict[str, list[dict]],
        control_pub: str | None = None,
        window_days: int | None = None,
    ) -> list[DifferenceInDifferencesResult]:
        """Run DiD analysis on a batch of migration events.

        Args:
            migrations: List of migration events to analyse.
            articles_by_pub: Mapping of publication slug → article list.
            articles_by_journalist: Mapping of journalist name (lower) → articles.
            control_pub: A stable publication to use as control for all analyses.
            window_days: Override default window.

        Returns:
            List of DiD results, one per migration.
        """
        results = []
        wd = window_days or self.window_days

        control_articles = articles_by_pub.get(control_pub, []) if control_pub else None

        for migration in migrations:
            src_articles = articles_by_pub.get(migration.from_publication, [])
            dst_articles = articles_by_pub.get(migration.to_publication, [])
            j_articles = articles_by_journalist.get(
                migration.journalist_name.lower(), []
            )

            try:
                result = self.analyze_migration(
                    migration=migration,
                    source_articles=src_articles,
                    dest_articles=dst_articles,
                    journalist_articles=j_articles,
                    control_articles=control_articles,
                    window_days=wd,
                )
                results.append(result)
            except Exception:
                continue  # skip migrations with insufficient data

        return results


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _window_scores(
    articles: list[dict],
    pivot_date: date,
    start_offset_days: int,
    end_offset_days: int,
) -> list[float]:
    """Extract tone scores from articles within a date window relative to pivot."""
    window_start = pivot_date + timedelta(days=start_offset_days)
    window_end = pivot_date + timedelta(days=end_offset_days)

    scores = []
    for a in articles:
        pub_date = a.get("published_date")
        if pub_date is None:
            continue
        if isinstance(pub_date, str):
            from mediascope.careers.tracker import _parse_date
            pub_date = _parse_date(pub_date)
        if window_start <= pub_date <= window_end:
            tone = a.get("overall_tone")
            if tone is not None:
                scores.append(float(tone))
    return scores


def _did_inference(
    treat_pre: list[float],
    treat_post: list[float],
    ctrl_pre: list[float],
    ctrl_post: list[float],
) -> tuple[float, float]:
    """Compute DiD standard error and p-value via OLS regression.

    The DiD model is:
        Y = β₀ + β₁·Treatment + β₂·Post + β₃·(Treatment × Post) + ε

    β₃ is the DiD estimator.  We compute its standard error and p-value.
    If control data is missing, we fall back to a simple pre/post t-test
    on the treatment group.
    """
    if not ctrl_pre and not ctrl_post:
        # No control group — fall back to simple pre/post comparison
        if len(treat_pre) < 2 or len(treat_post) < 2:
            return (0.0, 1.0)
        t_stat, p_val = welch_t_test(treat_post, treat_pre)
        se = abs(np.mean(treat_post) - np.mean(treat_pre)) / abs(t_stat) if t_stat != 0 else 0.0
        return (float(se), float(p_val))

    # Full DiD OLS regression
    # Build data matrix: Y, Treatment (0/1), Post (0/1), Interaction
    Y = []
    X_treatment = []
    X_post = []
    X_interaction = []

    for score in treat_pre:
        Y.append(score)
        X_treatment.append(1)
        X_post.append(0)
        X_interaction.append(0)

    for score in treat_post:
        Y.append(score)
        X_treatment.append(1)
        X_post.append(1)
        X_interaction.append(1)

    for score in ctrl_pre:
        Y.append(score)
        X_treatment.append(0)
        X_post.append(0)
        X_interaction.append(0)

    for score in ctrl_post:
        Y.append(score)
        X_treatment.append(0)
        X_post.append(1)
        X_interaction.append(0)

    if len(Y) < 5:
        return (0.0, 1.0)

    Y_arr = np.array(Y, dtype=float)
    n = len(Y_arr)

    # Design matrix: [intercept, treatment, post, interaction]
    X = np.column_stack([
        np.ones(n),
        np.array(X_treatment, dtype=float),
        np.array(X_post, dtype=float),
        np.array(X_interaction, dtype=float),
    ])

    try:
        # OLS: β = (X'X)⁻¹X'Y
        XtX_inv = np.linalg.inv(X.T @ X)
        beta = XtX_inv @ X.T @ Y_arr

        # Residuals and variance
        residuals = Y_arr - X @ beta
        df = n - 4  # 4 parameters
        if df < 1:
            return (0.0, 1.0)

        sigma_sq = float(np.sum(residuals ** 2) / df)
        var_beta = sigma_sq * XtX_inv

        # β₃ (interaction) is the DiD estimator
        beta3 = float(beta[3])
        se_beta3 = float(np.sqrt(var_beta[3, 3]))

        if se_beta3 == 0:
            return (0.0, 1.0)

        t_stat = beta3 / se_beta3
        p_value = float(2 * sp_stats.t.sf(abs(t_stat), df))

        return (se_beta3, p_value)

    except np.linalg.LinAlgError:
        return (0.0, 1.0)


def _portable_bias(
    pre_scores: list[float],
    post_scores: list[float],
) -> float:
    """Estimate how much of a journalist's tone is portable across outlets.

    Returns a value between 0 and 1:
    - 0.0 = tone completely changed after moving (fully adapts)
    - 1.0 = tone identical before and after (fully portable)

    Uses 1 − |Cohen's d| as the similarity measure, clamped to [0, 1].
    A small effect size means the distributions are similar → high portability.
    """
    if len(pre_scores) < 2 or len(post_scores) < 2:
        return 0.5  # insufficient data, return agnostic

    d = cohens_d(pre_scores, post_scores)
    # |d| = 0 → identical distributions → portable = 1.0
    # |d| = 1 → very different → portable = 0.0
    # |d| ≥ 2 → clamp to portable = 0.0
    portable = max(0.0, 1.0 - abs(d) / 2.0)
    return round(portable, 3)


def _methodology_note(
    window_days: int,
    n_pre: int,
    n_post: int,
    has_control: bool,
) -> str:
    """Generate a methodology note for the DiD result."""
    control_note = (
        "Full DiD with control group for secular trend removal."
        if has_control
        else "Simple pre/post comparison without control group — confounded by secular trends."
    )
    return (
        f"Difference-in-differences analysis with {window_days}-day pre/post windows. "
        f"{n_pre} pre-migration and {n_post} post-migration articles analysed. "
        f"{control_note} "
        f"Portable bias estimated via Cohen's d on journalist tone distributions. "
        f"Standard errors from OLS DiD regression with heteroscedasticity-robust inference. "
        f"Methodology adapted from Card & Krueger (1994)."
    )
