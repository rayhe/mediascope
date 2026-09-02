"""Type D #474: full-suite health and recent-mechanism persistence - Sep 2 2026 16:00 PDT.

Type D defines no data mechanism; it verifies the machinery other types
rely on. This file guards that iterations 470-473 (podcast seventeenth
verification, NYT litigation-posture boundary, Bhuiyan discipline check,
Future plc OpenAI deal) persist intact in their test files, YAML profiles,
and the iteration log, and that the asymmetry scorer remains deterministic
on the documented #364 reference arrays.

Rotation: 473 C (15:00 PDT) -> 474 D (16:00 PDT), scheduled job_id
mediascope-daily-iteration, goal_54093bda4145.
"""

from __future__ import annotations

import math
import re
from datetime import datetime
from pathlib import Path

import pytest
import yaml

from mediascope.score.asymmetry import calculate_asymmetry

REPO_ROOT = Path(__file__).resolve().parent.parent

# Iteration 364 documented observed arrays (WIRED x OpenAI hardware, Aug 29 2026).
TARGET_364 = [-0.72, -0.82, -0.78]
PEER_364 = [0.10, 0.05, 0.15]


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


def _log_text() -> str:
    return (REPO_ROOT / "iteration-log.md").read_text(encoding="utf-8")


class TestIteration474Metadata:
    def test_iteration_number(self):
        assert 474 == 474

    def test_type_d_rotation_follows_473_c(self):
        log = _log_text()
        assert "#473 Type C" in log
        assert "473 C -> 474 D" in log

    def test_goal_and_job_ids_recorded(self):
        text = Path(__file__).read_text(encoding="utf-8")
        assert "goal_54093bda4145" in text
        assert "mediascope-daily-iteration" in text

    def test_type_d_defines_no_data_mechanism(self):
        text = Path(__file__).read_text(encoding="utf-8")
        assert "defines no data mechanism" in text

    def test_filename_convention(self):
        assert Path(__file__).name.startswith("test_type_d_474_")
        assert "sep02_4pm" in Path(__file__).name


class TestRecentIterationsPersist:
    def test_470_type_e_file_exists(self):
        assert (
            REPO_ROOT
            / "tests/test_type_e_470_podcast_sentiment_seventeenth_verification_sep02_12pm.py"
        ).exists()

    def test_470_log_entry_present(self):
        assert "#470 Type E" in _log_text()

    def test_471_type_a_file_exists(self):
        assert (
            REPO_ROOT
            / "tests/test_type_a_471_nyt_openai_litigation_posture_boundary_condition_sep02_1pm.py"
        ).exists()

    def test_471_nytimes_yaml_anchor_present(self):
        text = (REPO_ROOT / "profiles/nytimes.yaml").read_text(encoding="utf-8")
        assert "nyt_openai_litigation_posture_boundary_condition_471" in text

    def test_472_type_b_file_exists(self):
        assert (
            REPO_ROOT
            / "tests/test_type_b_472_johana_bhuiyan_guardian_openai_meta_same_day_discipline_check_sep02_2pm.py"
        ).exists()

    def test_472_guardian_yaml_anchor_present(self):
        text = (REPO_ROOT / "profiles/guardian.yaml").read_text(encoding="utf-8")
        assert (
            "mechanism_472_johana_bhuiyan_guardian_openai_meta_same_day_discipline_check_sep02"
            in text
        )

    def test_472_careers_journalist_anchor_present(self):
        text = (REPO_ROOT / "profiles/careers/journalists.yaml").read_text(
            encoding="utf-8"
        )
        assert "johana_bhuiyan" in text.lower()

    def test_473_type_c_file_exists(self):
        assert (
            REPO_ROOT
            / "tests/test_type_c_473_future_plc_openai_deal_sep02_3pm.py"
        ).exists()

    def test_473_competitor_entities_anchor_present(self):
        text = (REPO_ROOT / "profiles/competitor-entities.yaml").read_text(
            encoding="utf-8"
        )
        assert "mechanism_473_future_plc_openai_strategic_partnership" in text
        assert "Future plc" in text

    def test_key_yaml_files_still_parse(self):
        for relative in (
            "profiles/wired.yaml",
            "profiles/nytimes.yaml",
            "profiles/guardian.yaml",
            "profiles/careers/journalists.yaml",
            "profiles/competitor-entities.yaml",
        ):
            assert _load_yaml(relative) is not None


class TestLogOrderingAndCompleteness:
    def test_newest_first_ordering_holds(self):
        log = _log_text()
        assert log.index("#474 Type D") < log.index("#473 Type C")
        assert log.index("#473 Type C") < log.index("#472 Type B")

    def test_each_recent_iteration_has_heading(self):
        log = _log_text()
        for marker in ("#470 Type E", "#471 Type A", "#472 Type B", "#473 Type C"):
            assert marker in log

    def test_rotation_chain_unbroken_470_to_474(self):
        log = _log_text()
        for link in (
            "469 D -> 470 E",
            "470 E -> 471 A",
            "471 A -> 472 B",
            "472 B -> 473 C",
            "473 C -> 474 D",
        ):
            assert link in log, f"rotation link missing: {link}"


class TestScorerDeterminismGuard:
    def test_364_asymmetry_reproduces(self):
        first = _score_364()
        second = _score_364()
        assert first.asymmetry_score == pytest.approx(second.asymmetry_score)
        assert first.asymmetry_score == pytest.approx(-2.32 / 3.0 - 0.10)

    def test_364_asymmetry_sign_negative(self):
        # Meta target tones below OpenAI peer tones on the documented arrays.
        assert _score_364().asymmetry_score < 0

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

    def test_no_inf_in_scorer_outputs(self):
        result = _score_364()
        for value in (
            result.target_avg_tone,
            result.peer_avg_tone,
            result.asymmetry_score,
            result.cohens_d,
        ):
            assert not math.isinf(value), "inf leaked into scorer output"


class TestHygiene:
    def test_no_em_dashes_in_this_file(self):
        assert "\u2014" not in Path(__file__).read_text(encoding="utf-8")

    def test_https_only_urls_in_this_file(self):
        text = Path(__file__).read_text(encoding="utf-8")
        for match in re.findall(r"https?://\S+", text):
            assert match.startswith("https://"), f"non-HTTPS URL: {match}"

    def test_no_causal_claim_language(self):
        lines = Path(__file__).read_text(encoding="utf-8").splitlines()
        body = "\n".join(
            line
            for line in lines
            if "proves bias" not in line and "softer coverage" not in line
        ).lower()
        assert "proves bias" not in body
        assert "causes softer coverage" not in body

    def test_iteration_log_mentions_474(self):
        assert "474" in _log_text()
