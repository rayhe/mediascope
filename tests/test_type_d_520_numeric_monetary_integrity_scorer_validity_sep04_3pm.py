"""Type D #520: numeric monetary integrity + asymmetry scorer statistical validity.

Iteration 520 (Sep 4 2026, 15:00 PDT) - Type D: Test & Verify.

REGRESSION: iteration #514 wrote `target_raise_b: 75-86.2` (unquoted) in
profiles/competitor-entities.yaml. Per the 2026-09-04 YAML plain-scalar
silent-mangle rule, `75-86.2` parsed as a STRING, and the aug17 test's
`target_raise >= 50` TypeErrored on every full-suite run since (flagged in
the #517 iteration-log entry as a pre-existing failure for the next Type D
window). Fixed in this run by splitting into numeric
`target_raise_b_low` / `target_raise_b_high` fields. These tests lock the
fix and guard every sibling monetary scalar against the same silent mangle.

SCORER VALIDITY: known-answer tests on mediascope.score.asymmetry's
calculate_asymmetry - symmetric input must yield delta ~ 0 and no
significance claim; strongly asymmetric input must yield correct sign and
direction; the real #517 Guardian numbers (target [-0.65, -0.30], peer
[-0.25, -0.10, -0.15]) must reproduce the logged n.s. result (p ~ 0.315);
degenerate inputs (n=1, empty) must not crash or claim false significance.
"""

from datetime import datetime
from pathlib import Path

import pytest
import yaml

from mediascope.score.asymmetry import calculate_asymmetry
from mediascope.score.statistical import cohens_d, is_significant, welch_t_test

REPO_ROOT = Path(__file__).parent.parent
ENTITIES_PATH = REPO_ROOT / "profiles" / "competitor-entities.yaml"

PERIOD = (datetime(2026, 1, 1), datetime(2026, 8, 31))


def load_entities():
    with open(ENTITIES_PATH) as f:
        return yaml.safe_load(f)


def score(target, peer):
    return calculate_asymmetry(
        target_scores=list(target),
        peer_scores=list(peer),
        target_entity="anthropic",
        peer_entities=["openai", "google"],
        publication_slug="guardian",
        period_start=PERIOD[0],
        period_end=PERIOD[1],
    )


# ---------------------------------------------------------------------------
# Monetary integrity: every numeric-range scalar must actually be numeric
# ---------------------------------------------------------------------------

class TestMonetaryScalarIntegrity:
    """Regression guard for the #514 silent string-mangle (iteration #520)."""

    def test_entities_yaml_parses(self):
        data = load_entities()
        assert "entities" in data

    def test_anthropic_raise_fields_numeric(self):
        ipo = load_entities()["entities"]["anthropic"]["ipo_filing"]
        low = ipo.get("target_raise_b_low")
        high = ipo.get("target_raise_b_high")
        assert isinstance(low, (int, float)) and not isinstance(low, bool)
        assert isinstance(high, (int, float)) and not isinstance(high, bool)
        assert low <= high
        assert low == 75
        assert high == pytest.approx(86.2)

    def test_no_hyphen_range_strings_in_ipo_filing(self):
        """No scalar of the form 'N-N' may sit in a numeric field unquoted."""
        ipo = load_entities()["entities"]["anthropic"]["ipo_filing"]
        import re
        range_pat = re.compile(r"^\d+(\.\d+)?-\d+(\.\d+)?$")
        for key, value in ipo.items():
            if isinstance(value, str) and range_pat.match(value.strip()):
                # Only allowed if the key is an explicit note/source field
                assert "note" in key or "source" in key or "timeline" in key, (
                    f"{key!r} holds range-shaped string {value!r} in a "
                    "numeric position - must be split into numeric low/high fields"
                )

    def test_old_target_raise_b_key_removed(self):
        ipo = load_entities()["entities"]["anthropic"]["ipo_filing"]
        assert "target_raise_b" not in ipo, (
            "legacy string field must not survive alongside the numeric split"
        )

    def test_all_ipo_b_fields_numeric_repo_wide(self):
        """Any key ending in _b under any ipo_filing block must be numeric."""
        data = load_entities()["entities"]
        offenders = []
        for entity, block in data.items():
            if not isinstance(block, dict):
                continue
            ipo = block.get("ipo_filing")
            if not isinstance(ipo, dict):
                continue
            for key, value in ipo.items():
                if key.endswith("_b") and value is not None:
                    if not (isinstance(value, (int, float)) and not isinstance(value, bool)):
                        offenders.append(f"{entity}.{key}={value!r}")
        assert not offenders, f"non-numeric _b fields: {offenders}"


# ---------------------------------------------------------------------------
# Scorer statistical validity: known-answer tests
# ---------------------------------------------------------------------------

class TestScorerSymmetricInput:
    """Equal tone distributions must produce ~zero delta, no significance."""

    def test_symmetric_input_no_asymmetry(self):
        s = score([-0.2, -0.1, 0.0, 0.1], [-0.2, -0.1, 0.0, 0.1])
        assert abs(s.asymmetry_score) < 1e-9
        assert s.is_significant is False

    def test_symmetric_input_effect_size_zero(self):
        d = cohens_d([-0.2, -0.1, 0.0, 0.1], [-0.2, -0.1, 0.0, 0.1])
        assert abs(d) < 1e-9

    def test_welch_t_equal_means_not_significant(self):
        _, p = welch_t_test([1.0, 2.0, 3.0], [1.0, 2.0, 3.0])
        assert p > 0.05
        assert is_significant(p) is False


class TestScorerStrongAsymmetry:
    """Strongly separated distributions must produce signed, significant deltas."""

    def test_negative_target_detected(self):
        s = score(
            [-0.9, -0.85, -0.8, -0.75, -0.7, -0.8],
            [0.1, 0.2, 0.15, 0.05, 0.1, 0.12],
        )
        assert s.asymmetry_score < 0, "target harsher than peers -> negative delta"
        assert s.is_significant is True
        assert s.p_value < 0.05
        assert s.cohens_d < -1.0, "effect should be large"

    def test_positive_target_detected(self):
        s = score(
            [0.5, 0.6, 0.55, 0.65, 0.5, 0.6],
            [-0.3, -0.25, -0.35, -0.2, -0.3, -0.28],
        )
        assert s.asymmetry_score > 0, "target softer than peers -> positive delta"
        assert s.is_significant is True
        assert s.article_count_target == 6
        assert s.article_count_peers == 6

    def test_confidence_interval_excludes_zero_when_significant(self):
        s = score(
            [-0.9, -0.85, -0.8, -0.75, -0.7, -0.8],
            [0.1, 0.2, 0.15, 0.05, 0.1, 0.12],
        )
        # 95% CI of the mean difference should not straddle zero
        ci = (s.confidence_interval_lower, s.confidence_interval_upper)
        assert (ci[0] > 0) or (ci[1] < 0), f"CI {ci} straddles zero on significant result"


class TestScorerRealMechanismRegression:
    """#517 Guardian x Anthropic numbers must reproduce the logged n.s. result."""

    def test_517_numbers_not_significant(self):
        s = score([-0.65, -0.30], [-0.25, -0.10, -0.15])
        assert s.asymmetry_score == pytest.approx(-0.30833, abs=1e-4)
        assert s.is_significant is False
        assert s.p_value == pytest.approx(0.3154, abs=0.02)
        assert s.cohens_d < -1.0, "large effect despite small n"
        # Direction: Anthropic harsher
        assert s.target_avg_tone < s.peer_avg_tone


class TestScorerDegenerateInput:
    """Degenerate inputs must never crash and never claim false significance."""

    def test_single_article_each_side_no_crash(self):
        s = score([-0.5], [0.2])
        assert s.is_significant is False
        assert s.asymmetry_score == pytest.approx(-0.7)

    def test_empty_target_no_crash(self):
        s = score([], [-0.2, -0.1])
        # Scorer convention: empty target -> target_avg 0.0, so delta = 0 - peer_avg
        assert s.asymmetry_score == pytest.approx(0.0 - (-0.15))
        assert s.is_significant is False
        assert s.article_count_target == 0

    def test_empty_both_no_crash(self):
        s = score([], [])
        assert s.is_significant is False

    def test_is_significant_boundary(self):
        assert is_significant(0.0499) is True
        assert is_significant(0.05) is False
        assert is_significant(0.0501) is False
