"""Editorial leadership change tracking and tone-shift analysis.

Correlates editorial leadership transitions (new EIC, managing editor, etc.)
with coverage tone changes at the publication.  This addresses the question:
*Does the person at the top actually change coverage, or is tone driven by
the broader institutional culture / ownership?*

Uses interrupted time-series analysis: fit a trend line to pre-change coverage
tone, then test whether the post-change period deviates significantly from the
projected trend.
"""

from __future__ import annotations

import math
from collections import defaultdict
from dataclasses import asdict, dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Optional

import numpy as np
from scipy import stats as sp_stats

import yaml

from mediascope.careers.models import EditorialLeadershipChange


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class LeadershipChangeImpact:
    """Result of analyzing the impact of a leadership change on coverage tone.

    Uses interrupted time-series analysis (ITS): a segmented regression that
    fits a trend to pre-change data and tests for a level shift (immediate
    change) and/or slope change (gradual drift) after the leadership change.
    """

    change: EditorialLeadershipChange

    # Pre-change coverage
    pre_mean_tone: float
    pre_trend_slope: float  # monthly trend before the change
    pre_n_articles: int

    # Post-change coverage
    post_mean_tone: float
    post_trend_slope: float  # monthly trend after the change
    post_n_articles: int

    # Impact estimates
    level_shift: float  # immediate tone change (ITS β₂)
    level_shift_p: float
    slope_change: float  # change in trend (ITS β₃)
    slope_change_p: float

    # Overall
    is_significant: bool
    effect_size: float  # Cohen's d on pre vs post tone distributions
    interpretation: str
    methodology_note: str = ""

    def to_dict(self) -> dict:
        d = asdict(self)
        d["change"] = self.change.to_dict()
        return d


# ---------------------------------------------------------------------------
# Analyzer
# ---------------------------------------------------------------------------

class LeadershipAnalyzer:
    """Analyze the impact of editorial leadership changes on coverage tone.

    Usage::

        analyzer = LeadershipAnalyzer()
        changes = analyzer.load_changes("profiles/careers/editorial_changes.yaml")
        impact = analyzer.analyze_change(
            change=changes[0],
            articles=publication_articles,
            window_months=12,
        )
    """

    def __init__(self, window_months: int = 12):
        self.window_months = window_months

    def load_changes(
        self, filepath: str | Path | None = None
    ) -> list[EditorialLeadershipChange]:
        """Load editorial leadership changes from YAML."""
        if filepath is None:
            filepath = Path("profiles/careers/editorial_changes.yaml")
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError(f"Leadership changes not found at {path}")

        with open(path, "r", encoding="utf-8") as fh:
            raw = yaml.safe_load(fh) or {}

        changes: list[EditorialLeadershipChange] = []
        for pub_slug, pub_changes in raw.get("editorial_changes", {}).items():
            for ch in pub_changes:
                changes.append(
                    EditorialLeadershipChange(
                        publication_slug=pub_slug,
                        position=ch.get("position", "eic"),
                        outgoing_name=ch.get("outgoing"),
                        incoming_name=ch["incoming"],
                        effective_date=_parse_date(ch["date"]),
                        source_url=ch.get("source_url", ""),
                        notes=ch.get("notes"),
                    )
                )

        return sorted(changes, key=lambda c: c.effective_date)

    def analyze_change(
        self,
        change: EditorialLeadershipChange,
        articles: list[dict],
        target_entity: str | None = None,
        window_months: int | None = None,
    ) -> LeadershipChangeImpact:
        """Analyze the tone impact of a single leadership change.

        Uses interrupted time-series (ITS) analysis:
            Y_t = β₀ + β₁·T + β₂·D_t + β₃·(D_t × T_post) + ε_t

        where:
            T = time index (months from start)
            D_t = 0 before change, 1 after
            T_post = months since the change (0 before)

        β₂ = immediate level shift
        β₃ = change in monthly trend

        Args:
            change: The leadership change event.
            articles: All articles from the publication.  Each must have
                ``published_date`` (date) and ``overall_tone`` (float).
            target_entity: Optional — filter to articles mentioning this entity.
            window_months: Override default analysis window.
        """
        wm = window_months or self.window_months
        pivot = change.effective_date
        window_start = pivot - timedelta(days=wm * 30)
        window_end = pivot + timedelta(days=wm * 30)

        # Filter articles to window
        filtered = []
        for a in articles:
            pub_date = a.get("published_date")
            if pub_date is None:
                continue
            if isinstance(pub_date, str):
                pub_date = _parse_date(pub_date)
            if window_start <= pub_date <= window_end:
                if target_entity:
                    entities = a.get("entities", [])
                    if not any(target_entity.lower() in e.lower() for e in entities):
                        continue
                filtered.append({"date": pub_date, "tone": float(a["overall_tone"])})

        if len(filtered) < 10:
            return _empty_impact(change, "Insufficient articles for analysis")

        # Split into pre/post
        pre = [a for a in filtered if a["date"] < pivot]
        post = [a for a in filtered if a["date"] >= pivot]

        if len(pre) < 5 or len(post) < 5:
            return _empty_impact(change, "Insufficient pre or post data")

        pre_tones = [a["tone"] for a in pre]
        post_tones = [a["tone"] for a in post]

        # ----- Interrupted Time-Series Regression -----
        # Convert dates to month indices relative to window_start
        articles_sorted = sorted(filtered, key=lambda a: a["date"])
        Y = np.array([a["tone"] for a in articles_sorted])
        T = np.array([
            (a["date"] - window_start).days / 30.0 for a in articles_sorted
        ])
        pivot_month = (pivot - window_start).days / 30.0
        D = np.array([1.0 if a["date"] >= pivot else 0.0 for a in articles_sorted])
        T_post = np.array([
            max(0, (a["date"] - pivot).days / 30.0) for a in articles_sorted
        ])

        n = len(Y)

        # Design matrix: [intercept, T, D, D×T_post]
        X = np.column_stack([np.ones(n), T, D, T_post * D])

        try:
            XtX_inv = np.linalg.inv(X.T @ X)
            beta = XtX_inv @ X.T @ Y
            residuals = Y - X @ beta
            df = n - 4
            if df < 1:
                return _empty_impact(change, "Insufficient degrees of freedom")

            sigma_sq = float(np.sum(residuals ** 2) / df)
            var_beta = sigma_sq * XtX_inv

            # Extract coefficients
            # β₁ = pre-change monthly trend
            pre_slope = float(beta[1])
            # β₂ = level shift at the change
            level_shift = float(beta[2])
            se_level = float(np.sqrt(var_beta[2, 2]))
            t_level = level_shift / se_level if se_level > 0 else 0.0
            p_level = float(2 * sp_stats.t.sf(abs(t_level), df))

            # β₃ = change in monthly trend
            slope_change = float(beta[3])
            se_slope = float(np.sqrt(var_beta[3, 3]))
            t_slope = slope_change / se_slope if se_slope > 0 else 0.0
            p_slope = float(2 * sp_stats.t.sf(abs(t_slope), df))

            # Post-change monthly trend = β₁ + β₃
            post_slope = pre_slope + slope_change

        except np.linalg.LinAlgError:
            return _empty_impact(change, "Singular matrix in regression")

        # Effect size
        from mediascope.score.statistical import cohens_d as compute_d
        d = compute_d(post_tones, pre_tones)

        is_sig = p_level < 0.05 or p_slope < 0.05

        # Interpretation
        interp = _interpret_its(
            level_shift, p_level, slope_change, p_slope,
            change.incoming_name, change.position,
        )

        return LeadershipChangeImpact(
            change=change,
            pre_mean_tone=float(np.mean(pre_tones)),
            pre_trend_slope=pre_slope,
            pre_n_articles=len(pre),
            post_mean_tone=float(np.mean(post_tones)),
            post_trend_slope=post_slope,
            post_n_articles=len(post),
            level_shift=level_shift,
            level_shift_p=p_level,
            slope_change=slope_change,
            slope_change_p=p_slope,
            is_significant=is_sig,
            effect_size=d,
            interpretation=interp,
            methodology_note=(
                f"Interrupted time-series analysis with {wm}-month pre/post windows. "
                f"{len(pre)} pre-change and {len(post)} post-change articles. "
                f"OLS segmented regression: Y = β₀ + β₁·T + β₂·D + β₃·D·T_post. "
                f"Significance at α = 0.05."
            ),
        )

    def batch_analyze(
        self,
        changes: list[EditorialLeadershipChange],
        articles_by_pub: dict[str, list[dict]],
        target_entity: str | None = None,
    ) -> list[LeadershipChangeImpact]:
        """Analyze a batch of leadership changes."""
        results = []
        for ch in changes:
            articles = articles_by_pub.get(ch.publication_slug, [])
            try:
                result = self.analyze_change(ch, articles, target_entity)
                results.append(result)
            except Exception:
                continue
        return results


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _empty_impact(
    change: EditorialLeadershipChange,
    reason: str,
) -> LeadershipChangeImpact:
    """Return a zero-valued impact when analysis can't proceed."""
    return LeadershipChangeImpact(
        change=change,
        pre_mean_tone=0.0,
        pre_trend_slope=0.0,
        pre_n_articles=0,
        post_mean_tone=0.0,
        post_trend_slope=0.0,
        post_n_articles=0,
        level_shift=0.0,
        level_shift_p=1.0,
        slope_change=0.0,
        slope_change_p=1.0,
        is_significant=False,
        effect_size=0.0,
        interpretation=reason,
        methodology_note=reason,
    )


def _interpret_its(
    level_shift: float,
    level_p: float,
    slope_change: float,
    slope_p: float,
    incoming_name: str,
    position: str,
) -> str:
    """Generate a human-readable interpretation of the ITS results."""
    parts = []

    if level_p < 0.05:
        direction = "more negative" if level_shift < 0 else "more positive"
        parts.append(
            f"Significant immediate level shift: coverage became {direction} "
            f"after {incoming_name} took over as {position} "
            f"(shift = {level_shift:+.3f}, p = {level_p:.4f})."
        )
    else:
        parts.append(
            f"No significant immediate change in coverage tone when "
            f"{incoming_name} became {position} (p = {level_p:.4f})."
        )

    if slope_p < 0.05:
        direction = "increasingly negative" if slope_change < 0 else "increasingly positive"
        parts.append(
            f"Significant trend change: coverage became {direction} over time "
            f"(monthly slope change = {slope_change:+.4f}, p = {slope_p:.4f})."
        )
    else:
        parts.append(
            f"No significant change in coverage trend after the transition "
            f"(p = {slope_p:.4f})."
        )

    return " ".join(parts)


def _parse_date(val) -> date:
    """Parse a date from YAML."""
    if isinstance(val, date):
        return val
    if isinstance(val, str):
        parts = val.split("-")
        if len(parts) == 2:
            return date(int(parts[0]), int(parts[1]), 1)
        if len(parts) == 3:
            return date(int(parts[0]), int(parts[1]), int(parts[2]))
    raise ValueError(f"Cannot parse date from {val!r}")
