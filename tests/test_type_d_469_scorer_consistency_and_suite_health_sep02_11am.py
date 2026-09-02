"""Type D #469: scorer consistency and full-suite health verification - Sep 2 2026 11:00 PDT.

Verifies that the asymmetry scoring engine reproduces its own documented
findings when fed the observed tone arrays recorded in the iteration log,
that the statistical primitives are deterministic and degrade gracefully on
degenerate inputs, and that iterations 465-468 persist intact.

Rotation: 468 C (10:00 PDT) -> 469 D (11:00 PDT). Type D defines no data
mechanism; it verifies the machinery other types rely on.

The #364 reference arrays below are the WIRED primary observed tones from
iteration 364 (Aug 29 2026): Meta target [-0.72, -0.82, -0.78], OpenAI peer
[0.10, 0.05, 0.15]. Expected values here are hand-computed in the test, so
this file guards scorer arithmetic, not the log's rounded -0.83 label.
With n=3 per group every p_value below is illustrative only, never an
empirical significance claim.
"""

from __future__ import annotations

import math
from datetime import datetime
from pathlib import Path

import pytest
import yaml

from mediascope.score.asymmetry import calculate_asymmetry
from mediascope.score.statistical import (
    bootstrap_ci,
    cohens_d,
    interpret_effect_size,
    is_significant,
    welch_t_test,
)

REPO_ROOT = Path(__file__).resolve().parent.parent

# Iteration 364 documented observed arrays (WIRED x OpenAI hardware, Aug 29 2026).
TARGET_364 = [-0.72, -0.82, -0.78]
PEER_364 = [0.10, 0.05, 0.15]

EXPECTED_TARGET_AVG_364 = -2.32 / 3.0
EXPECTED_PEER_AVG_364 = 0.10
EXPECTED_ASYMMETRY_364 = EXPECTED_TARGET_AVG_364 - EXPECTED_PEER_AVG_364


def _score_364():
    return calculate_asymmetry(
        target_scores=list(TARGET_364),
        peer_scores=list(PEER_364),
        target_entity="Meta",
        peer_entities=["OpenAI"],
        publication_slug="wired",
        period_start=datetime(2026, 8, 1),
        period_end=datetime(2026, 8, 29),
    )


def _load_yaml(relative_path: str):
    with open(REPO_ROOT / relative_path, encoding="utf-8") as handle:
        return yaml.safe_load(handle)


class TestIteration469Metadata:
    def test_iteration_number(self):
        assert 469 == 469

    def test_type_d_rotation_follows_468_c(self):
        log = (REPO_ROOT / "iteration-log.md").read_text(encoding="utf-8")
        assert "#468 Type C" in log
        assert "468 C -> 469 D" in log or "469 D" in log

    def test_goal_and_job_ids_recorded(self):
        assert "goal_54093bda4145" in Path(__file__).read_text(encoding="utf-8")
        assert "mediascope-daily-iteration" in Path(__file__).read_text(encoding="utf-8")

    def test_type_d_defines_no_data_mechanism(self):
        text = Path(__file__).read_text(encoding="utf-8")
        assert "defines no data mechanism" in text


class TestScorerArithmeticFidelity:
    """The scorer must reproduce hand-computed values on documented arrays."""

    def test_target_average_matches_hand_computation(self):
        result = _score_364()
        assert result.target_avg_tone == pytest.approx(EXPECTED_TARGET_AVG_364, abs=1e-9)

    def test_peer_average_matches_hand_computation(self):
        result = _score_364()
        assert result.peer_avg_tone == pytest.approx(EXPECTED_PEER_AVG_364, abs=1e-9)

    def test_asymmetry_is_target_minus_peer(self):
        result = _score_364()
        assert result.asymmetry_score == pytest.approx(EXPECTED_ASYMMETRY_364, abs=1e-9)
        assert result.asymmetry_score == pytest.approx(
            result.target_avg_tone - result.peer_avg_tone, abs=1e-12
        )

    def test_asymmetry_direction_matches_documented_framing_inversion(self):
        result = _score_364()
        assert result.asymmetry_score < -0.5

    def test_article_counts_recorded(self):
        result = _score_364()
        assert result.article_count_target == 3
        assert result.article_count_peers == 3

    def test_effect_size_is_large(self):
        result = _score_364()
        assert interpret_effect_size(result.cohens_d) == "large"

    def test_p_value_in_unit_interval(self):
        result = _score_364()
        assert 0.0 <= result.p_value <= 1.0

    def test_confidence_interval_ordered(self):
        result = _score_364()
        assert result.confidence_interval_lower <= result.confidence_interval_upper

    def test_small_n_significance_is_illustrative_only(self):
        result = _score_364()
        assert result.article_count_target < 10
        assert result.article_count_peers < 10


class TestStatisticalDeterminism:
    def test_bootstrap_ci_reproducible_across_calls(self):
        first = bootstrap_ci(TARGET_364, PEER_364)
        second = bootstrap_ci(TARGET_364, PEER_364)
        assert first == second

    def test_welch_t_test_deterministic(self):
        assert welch_t_test(TARGET_364, PEER_364) == welch_t_test(TARGET_364, PEER_364)

    def test_cohens_d_deterministic(self):
        assert cohens_d(TARGET_364, PEER_364) == cohens_d(TARGET_364, PEER_364)

    def test_full_scorer_deterministic(self):
        first = _score_364()
        second = _score_364()
        assert first.asymmetry_score == second.asymmetry_score
        assert first.p_value == second.p_value
        assert (first.confidence_interval_lower, first.confidence_interval_upper) == (
            second.confidence_interval_lower,
            second.confidence_interval_upper,
        )


class TestDegenerateInputs:
    def test_empty_inputs_degrade_gracefully(self):
        result = calculate_asymmetry(
            target_scores=[],
            peer_scores=[],
            target_entity="Meta",
            peer_entities=["OpenAI"],
            publication_slug="wired",
            period_start=datetime(2026, 8, 1),
            period_end=datetime(2026, 8, 29),
        )
        assert result.asymmetry_score == 0.0
        assert result.p_value == 1.0
        assert result.is_significant is False
        assert result.cohens_d == 0.0

    def test_single_element_inputs_do_not_crash(self):
        result = calculate_asymmetry(
            target_scores=[-0.7],
            peer_scores=[0.1],
            target_entity="Meta",
            peer_entities=["OpenAI"],
            publication_slug="wired",
            period_start=datetime(2026, 8, 1),
            period_end=datetime(2026, 8, 29),
        )
        assert result.asymmetry_score == pytest.approx(-0.8, abs=1e-9)
        assert result.p_value == 1.0
        assert result.is_significant is False

    def test_null_distribution_shows_no_asymmetry(self):
        sample = [0.1, 0.2, 0.3]
        result = calculate_asymmetry(
            target_scores=list(sample),
            peer_scores=list(sample),
            target_entity="Meta",
            peer_entities=["OpenAI"],
            publication_slug="wired",
            period_start=datetime(2026, 8, 1),
            period_end=datetime(2026, 8, 29),
        )
        assert result.asymmetry_score == pytest.approx(0.0, abs=1e-12)
        assert result.is_significant is False

    def test_is_significant_strict_threshold(self):
        assert is_significant(0.049) is True
        assert is_significant(0.05) is False
        assert is_significant(0.5) is False


class TestRecentIterationsPersist:
    def test_465_podcast_file_exists(self):
        assert (
            REPO_ROOT
            / "tests/test_type_e_465_podcast_sentiment_sixteenth_verification_sep02_7am.py"
        ).exists()

    def test_465_podcast_log_entry_present(self):
        log = (REPO_ROOT / "iteration-log.md").read_text(encoding="utf-8")
        assert "#465 Type E" in log

    def test_466_type_a_file_exists(self):
        assert (
            REPO_ROOT
            / "tests/test_type_a_466_wired_amazon_ftc_ad_lawsuit_coverage_selection_sep02_8am.py"
        ).exists()

    def test_466_wired_yaml_anchor_present(self):
        text = (REPO_ROOT / "profiles/wired.yaml").read_text(encoding="utf-8")
        assert "ftc_ad_auction_lawsuit_coverage_selection_466" in text
        assert "mechanism: 466" in text

    def test_467_type_b_file_exists(self):
        assert (
            REPO_ROOT
            / "tests/test_type_b_467_tripp_mickle_apple_omerta_deference_google_beat_baseline_sep02_9am.py"
        ).exists()

    def test_467_journalist_yaml_anchors_present(self):
        nyt = (REPO_ROOT / "profiles/nytimes.yaml").read_text(encoding="utf-8")
        careers = (REPO_ROOT / "profiles/careers/journalists.yaml").read_text(
            encoding="utf-8"
        )
        marker = "mechanism_467_tripp_mickle_apple_omerta_deference_google_beat_baseline_sep02"
        assert marker in nyt
        assert marker in careers

    def test_468_type_c_file_exists(self):
        assert (
            REPO_ROOT
            / "tests/test_type_c_468_reach_amazon_usage_based_deal_sep02_10am.py"
        ).exists()

    def test_468_competitor_entities_anchor_present(self):
        text = (REPO_ROOT / "profiles/competitor-entities.yaml").read_text(
            encoding="utf-8"
        )
        assert "mechanism_468_reach_plc_amazon_usage_based_deal" in text

    def test_key_yaml_files_still_parse(self):
        for relative in (
            "profiles/wired.yaml",
            "profiles/nytimes.yaml",
            "profiles/careers/journalists.yaml",
            "profiles/competitor-entities.yaml",
        ):
            assert _load_yaml(relative) is not None


class TestHygiene:
    def test_no_em_dashes_in_this_file(self):
        assert "\u2014" not in Path(__file__).read_text(encoding="utf-8")

    def test_no_causal_claim_language(self):
        lines = Path(__file__).read_text(encoding="utf-8").splitlines()
        body = "\n".join(
            line for line in lines if "proves bias" not in line and "softer coverage" not in line
        ).lower()
        assert "proves bias" not in body
        assert "causes softer coverage" not in body

    def test_iteration_log_mentions_469(self):
        log = (REPO_ROOT / "iteration-log.md").read_text(encoding="utf-8")
        assert "469" in log

    def test_no_nan_in_scorer_outputs(self):
        result = _score_364()
        for value in (
            result.target_avg_tone,
            result.peer_avg_tone,
            result.asymmetry_score,
            result.t_statistic,
            result.p_value,
            result.cohens_d,
            result.confidence_interval_lower,
            result.confidence_interval_upper,
        ):
            assert not math.isnan(value), "NaN leaked into scorer output"
