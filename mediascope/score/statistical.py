"""Statistical utilities for media coverage analysis.

Provides Welch's t-test, Cohen's d effect size, bootstrap confidence intervals,
and significance testing — all with robust edge-case handling.
"""

from __future__ import annotations

import math
import random
from typing import Optional

import numpy as np
from scipy import stats


def welch_t_test(a: list[float], b: list[float]) -> tuple[float, float]:
    """Perform Welch's t-test (unequal variance) on two samples.

    Returns:
        (t_statistic, p_value). Returns (0.0, 1.0) for degenerate inputs.
    """
    if len(a) < 2 or len(b) < 2:
        return (0.0, 1.0)

    a_arr = np.array(a, dtype=float)
    b_arr = np.array(b, dtype=float)

    # If both have zero variance, can't compute t
    if np.std(a_arr, ddof=1) == 0 and np.std(b_arr, ddof=1) == 0:
        if np.mean(a_arr) == np.mean(b_arr):
            return (0.0, 1.0)
        # Identical values in each group but different between groups —
        # technically infinite t, return large t and tiny p
        return (float("inf"), 0.0)

    result = stats.ttest_ind(a_arr, b_arr, equal_var=False)
    t_stat = float(result.statistic)
    p_val = float(result.pvalue)

    # Handle NaN from edge cases
    if math.isnan(t_stat):
        t_stat = 0.0
    if math.isnan(p_val):
        p_val = 1.0

    return (t_stat, p_val)


def cohens_d(a: list[float], b: list[float]) -> float:
    """Calculate Cohen's d effect size for two independent samples.

    Uses the pooled standard deviation. Returns 0.0 for degenerate inputs.
    """
    if len(a) < 1 or len(b) < 1:
        return 0.0

    a_arr = np.array(a, dtype=float)
    b_arr = np.array(b, dtype=float)

    n_a, n_b = len(a_arr), len(b_arr)
    mean_diff = float(np.mean(a_arr) - np.mean(b_arr))

    # Pooled standard deviation
    var_a = float(np.var(a_arr, ddof=1)) if n_a > 1 else 0.0
    var_b = float(np.var(b_arr, ddof=1)) if n_b > 1 else 0.0

    if n_a + n_b <= 2:
        return 0.0

    pooled_var = ((n_a - 1) * var_a + (n_b - 1) * var_b) / (n_a + n_b - 2)
    pooled_sd = math.sqrt(pooled_var)

    if pooled_sd == 0:
        return 0.0

    return mean_diff / pooled_sd


def bootstrap_ci(
    a: list[float],
    b: list[float],
    n_bootstrap: int = 1000,
    ci: float = 0.95,
) -> tuple[float, float]:
    """Bootstrap confidence interval for the difference in means (mean(a) - mean(b)).

    Args:
        a: First sample.
        b: Second sample.
        n_bootstrap: Number of bootstrap resamples.
        ci: Confidence level (default 0.95 for 95% CI).

    Returns:
        (lower_bound, upper_bound). Returns (0.0, 0.0) for degenerate inputs.
    """
    if len(a) < 1 or len(b) < 1:
        return (0.0, 0.0)

    a_arr = np.array(a, dtype=float)
    b_arr = np.array(b, dtype=float)

    rng = np.random.default_rng(seed=42)  # reproducible
    diffs: list[float] = []

    for _ in range(n_bootstrap):
        sample_a = rng.choice(a_arr, size=len(a_arr), replace=True)
        sample_b = rng.choice(b_arr, size=len(b_arr), replace=True)
        diffs.append(float(np.mean(sample_a) - np.mean(sample_b)))

    alpha = 1 - ci
    lower = float(np.percentile(diffs, 100 * alpha / 2))
    upper = float(np.percentile(diffs, 100 * (1 - alpha / 2)))
    return (lower, upper)


def interpret_effect_size(d: float) -> str:
    """Interpret Cohen's d magnitude using conventional thresholds.

    |d| < 0.2  → negligible
    |d| < 0.5  → small
    |d| < 0.8  → medium
    |d| >= 0.8 → large
    """
    abs_d = abs(d)
    if abs_d < 0.2:
        return "negligible"
    elif abs_d < 0.5:
        return "small"
    elif abs_d < 0.8:
        return "medium"
    else:
        return "large"


def is_significant(p_value: float, alpha: float = 0.05) -> bool:
    """Check whether a p-value meets the significance threshold."""
    return p_value < alpha
