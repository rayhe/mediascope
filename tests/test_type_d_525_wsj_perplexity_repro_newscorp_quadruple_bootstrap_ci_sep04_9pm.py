"""Type D #525: WSJ x Perplexity reproduction, bootstrap CI behavior, News Corp quadruple-AI-revenue integrity.

Iteration 525 (Sep 4 2026, 21:00 PDT) - Type D: Test & Verify.

REAL-MECHANISM REPRODUCTION: iteration #522 logged the first WSJ x Perplexity
coverage analysis (target Perplexity [-0.2, -0.3, -0.4], deal-partner peers
OpenAI [-0.2] / Anthropic [-0.15]): delta -0.125, Welch p 0.1537 n.s.,
Cohen's d -1.4852, bootstrap CI (-0.225, -0.025), is_significant False.
These tests lock those logged numbers as a known-answer regression, in the
same pattern as #520's #517-regression class. They also encode the documented
internal tension: the bootstrap CI excludes zero while the Welch test is
n.s., so a consumer that treats "CI excludes zero" as significant and a
consumer that uses the scorer's is_significant flag can disagree at tiny n.

BOOTSTRAP CI BEHAVIOR: bootstrap_ci is seeded (np seed 42) and therefore
deterministic, so CI bounds are legitimate known-answer test subjects, not
fuzzy statistical properties. These tests pin the symmetry/anti-symmetry
behavior, translation invariance, degenerate handling, and reproducibility.

NEWS CORP QUADRUPLE-AI-REVENUE INTEGRITY: iteration #524 documented that
News Corp is the first tracked-publication owner collecting AI revenue from
four labs through four distinct channels (OpenAI news licensing $250M/5yr,
Meta news licensing up to $50M/yr, Microsoft/HarperCollins book licensing
Nov 2024, Anthropic $1.5B Bartz settlement share). These tests lock the
four-leg structure in profiles/news-corp.yaml and the mechanism_524 block in
profiles/competitor-entities.yaml: four AI legs present, each sourced with
a URL and verified=True, the Microsoft leg carrying its Bloomberg
anonymous-source caveat, the Anthropic note updated from THREE to FOUR.

SCORER SENSITIVITY/SPECIFICITY: verifies the scorer actually produces
statistically meaningful results at adequate n - strongly separated
distributions at n=60 must be significant with the correct sign and a large
effect, while symmetric distributions at n=60 must NOT be significant.
Without this, every downstream n.s./significant call in the repo would be
a claim about numbers the engine was never shown to produce correctly.

COMPETITOR-CITATION RATCHET: a profile-wide scan found 45
competitor_relationships entries across the 14 publication profiles with no
source_url/source_urls citation, in 41 distinct field layouts. Fixing all 45
is out of scope for one Type D window, so the tests are a ratchet: the
unsourced count may shrink as entries get cited but must never grow, and no
uncited entry may be an empty stub (must carry description or
coverage_prediction). Baseline 45 measured this run, deterministic.
"""

from datetime import datetime
from pathlib import Path

import pytest
import yaml

from mediascope.score.asymmetry import calculate_asymmetry
from mediascope.score.statistical import (
    bootstrap_ci,
    interpret_effect_size,
    is_significant,
    welch_t_test,
)

REPO_ROOT = Path(__file__).parent.parent
NEWS_CORP_PROFILE = REPO_ROOT / "profiles" / "news-corp.yaml"
ENTITIES_PATH = REPO_ROOT / "profiles" / "competitor-entities.yaml"

PERIOD = (datetime(2026, 1, 1), datetime(2026, 8, 31))


def load_news_corp():
    with open(NEWS_CORP_PROFILE) as f:
        return yaml.safe_load(f)


def score(target, peer, target_entity="perplexity", peers=("openai", "anthropic")):
    return calculate_asymmetry(
        target_scores=list(target),
        peer_scores=list(peer),
        target_entity=target_entity,
        peer_entities=list(peers),
        publication_slug="wsj",
        period_start=PERIOD[0],
        period_end=PERIOD[1],
    )


# ---------------------------------------------------------------------------
# #522 WSJ x Perplexity: known-answer regression on the logged numbers
# ---------------------------------------------------------------------------

TARGET_522 = [-0.2, -0.3, -0.4]   # Perplexity: business-failure, quixotic-dismissal, security-threat
PEER_522 = [-0.2, -0.15]          # OpenAI / Anthropic deal-partner rogue-AI tones


class TestWsjPerplexity522Reproduction:
    """Lock iteration #522's logged asymmetry numbers (17:00 PDT run)."""

    def test_delta_minus_0125(self):
        s = score(TARGET_522, PEER_522)
        assert s.asymmetry_score == pytest.approx(-0.125, abs=1e-9)

    def test_target_and_peer_means(self):
        s = score(TARGET_522, PEER_522)
        assert s.target_avg_tone == pytest.approx(-0.3, abs=1e-9)
        assert s.peer_avg_tone == pytest.approx(-0.175, abs=1e-9)
        assert s.article_count_target == 3
        assert s.article_count_peers == 2

    def test_welch_p_not_significant(self):
        s = score(TARGET_522, PEER_522)
        assert s.p_value == pytest.approx(0.1537, abs=0.005)
        assert s.is_significant is False
        # t statistic must be negative: target (Perplexity) harsher than peers
        assert s.t_statistic < 0

    def test_cohens_d_large_negative(self):
        s = score(TARGET_522, PEER_522)
        assert s.cohens_d == pytest.approx(-1.4852, abs=0.01)
        assert interpret_effect_size(s.cohens_d) == "large"

    def test_bootstrap_ci_excludes_zero_but_welch_nonsignificant(self):
        """The logged tension: CI excludes zero while Welch is n.s.

        A naive consumer reading 'CI excludes zero => significant' would
        contradict the scorer's own is_significant flag. This test pins both
        facts so the tension cannot be silently resolved by future refactors.
        """
        s = score(TARGET_522, PEER_522)
        assert s.confidence_interval_lower == pytest.approx(-0.225, abs=0.01)
        assert s.confidence_interval_upper == pytest.approx(-0.025, abs=0.01)
        assert s.confidence_interval_upper < 0, "CI fully negative"
        assert s.is_significant is False, "but Welch says not significant"

    def test_welch_standalone_matches_scorer_p(self):
        """The scorer's p_value must equal the raw welch_t_test output."""
        t, p = welch_t_test(TARGET_522, PEER_522)
        s = score(TARGET_522, PEER_522)
        assert s.t_statistic == pytest.approx(t)
        assert s.p_value == pytest.approx(p)


# ---------------------------------------------------------------------------
# bootstrap_ci: behavioral known-answer properties
# ---------------------------------------------------------------------------

class TestBootstrapCIBehavior:
    """bootstrap_ci is seeded (42): bounds are deterministic test subjects."""

    def test_symmetric_input_ci_contains_zero(self):
        lo, hi = bootstrap_ci(
            [-0.2, -0.1, 0.0, 0.1, -0.05, 0.05],
            [-0.2, -0.1, 0.0, 0.1, -0.05, 0.05],
        )
        assert lo <= 0 <= hi, f"symmetric CI {lo, hi} should contain zero"
        assert lo <= hi

    def test_strongly_separated_input_ci_entirely_negative(self):
        target = [-0.9, -0.85, -0.8, -0.75, -0.7, -0.8]
        peer = [0.1, 0.2, 0.15, 0.05, 0.1, 0.12]
        lo, hi = bootstrap_ci(target, peer)
        assert lo <= hi
        assert hi < 0, f"CI {lo, hi} should sit entirely below zero"

    def test_strongly_separated_input_ci_entirely_positive(self):
        target = [0.5, 0.6, 0.55, 0.65, 0.5, 0.6]
        peer = [-0.3, -0.25, -0.35, -0.2, -0.3, -0.28]
        lo, hi = bootstrap_ci(target, peer)
        assert lo <= hi
        assert lo > 0, f"CI {lo, hi} should sit entirely above zero"

    def test_degenerate_inputs_return_zero_pair(self):
        assert bootstrap_ci([], [-0.2, -0.1]) == (0.0, 0.0)
        assert bootstrap_ci([-0.5], []) == (0.0, 0.0)
        assert bootstrap_ci([], []) == (0.0, 0.0)

    def test_reproducible_across_calls(self):
        a = [-0.2, -0.3, -0.4]
        b = [-0.2, -0.15]
        assert bootstrap_ci(a, b) == bootstrap_ci(a, b)

    def test_translation_invariance(self):
        """Shifting every sample in BOTH groups by +c leaves the CI unchanged.

        mean(a+c) - mean(b+c) = mean(a) - mean(b); the constant cancels in
        every resample, so the difference distribution is identical.
        """
        a = [-0.2, -0.3, -0.4]
        b = [-0.2, -0.15]
        lo0, hi0 = bootstrap_ci(a, b)
        lo1, hi1 = bootstrap_ci([x + 1.5 for x in a], [x + 1.5 for x in b])
        assert lo1 == pytest.approx(lo0)
        assert hi1 == pytest.approx(hi0)

    def test_ci_narrower_at_larger_n(self):
        """Same distributions, larger n -> narrower CI (consistency check)."""
        import random
        random.seed(7)
        target = [random.gauss(-0.4, 0.15) for _ in range(8)]
        peer = [random.gauss(0.1, 0.15) for _ in range(8)]
        lo_s, hi_s = bootstrap_ci(target, peer)
        lo_l, hi_l = bootstrap_ci(target * 5, peer * 5)
        assert (hi_l - lo_l) < (hi_s - lo_s)


# ---------------------------------------------------------------------------
# #524 News Corp quadruple-AI-revenue data integrity
# ---------------------------------------------------------------------------

AI_LEG_PARTNERS = ("OpenAI", "Meta", "Microsoft", "Anthropic")


class TestNewsCorpQuadrupleRevenueIntegrity:
    """Lock iteration #524's four-leg owner-level finding in news-corp.yaml."""

    def test_four_ai_legs_present(self):
        legs = load_news_corp()["revenue_relationships"]
        partners = {l["partner"] for l in legs}
        for expected in AI_LEG_PARTNERS:
            assert expected in partners, f"AI leg missing for {expected}"

    def test_each_ai_leg_sourced_and_verified(self):
        legs = load_news_corp()["revenue_relationships"]
        for leg in legs:
            if leg["partner"] not in AI_LEG_PARTNERS:
                continue
            assert leg.get("verified") is True, f"{leg['partner']} not verified"
            url = leg.get("source_url", "")
            assert url.startswith("http"), f"{leg['partner']} lacks source_url"
            assert leg.get("value"), f"{leg['partner']} lacks value"
            assert leg.get("signed"), f"{leg['partner']} lacks signed date"

    def test_microsoft_leg_carries_bloomberg_caveat(self):
        legs = load_news_corp()["revenue_relationships"]
        ms = next(l for l in legs if l["partner"] == "Microsoft")
        scope = ms["scope"]
        assert "HarperCollins" in scope
        assert "Bloomberg" in scope, "anonymous-source attribution caveat required"
        assert "anonymous" in scope.lower()

    def test_anthropic_note_updated_from_three_to_four(self):
        legs = load_news_corp()["revenue_relationships"]
        anthropic = next(l for l in legs if l["partner"] == "Anthropic")
        notes = anthropic.get("notes", "")
        assert "FOUR" in notes, "Anthropic note must reflect the fourth leg"

    def test_mechanism_524_present_in_entities_yaml(self):
        with open(ENTITIES_PATH) as f:
            entities = yaml.safe_load(f)
        mech = entities["entities"]["openai"][
            "mechanism_524_newscorp_microsoft_harpercollins_quadruple_ai_revenue"
        ]
        assert mech["mechanism_id"] == 524
        assert mech["correlation_not_causation"] is True
        assert mech["is_significant"] is False
        assert len(mech.get("source_urls", [])) >= 3
        for url in mech["source_urls"]:
            assert url.startswith("http"), f"non-URL source: {url!r}"


# ---------------------------------------------------------------------------
# Scorer sensitivity/specificity: statistically meaningful at adequate n
# ---------------------------------------------------------------------------

class TestScorerSensitivitySpecificity:
    """The scorer must produce significant results when asymmetry is real
    and withhold significance when it is absent, at adequate sample size."""

    def test_real_asymmetry_detected_at_n60(self):
        import random
        random.seed(42)
        target = [random.gauss(-0.5, 0.2) for _ in range(60)]
        peer = [random.gauss(0.1, 0.2) for _ in range(60)]
        s = score(target, peer, target_entity="meta", peers=("apple",))
        assert s.is_significant is True
        assert s.asymmetry_score < 0
        assert s.p_value < 0.05
        assert abs(s.cohens_d) > 0.8, "effect should be large at this separation"
        lo, hi = s.confidence_interval_lower, s.confidence_interval_upper
        assert hi < 0, "CI should exclude zero on a significant result"

    def test_no_asymmetry_withheld_at_n60(self):
        """Deterministic symmetric n=60 case: identical distributions must
        never read significant.

        NOTE (first-attempt failure documented): an earlier draft used one
        random 60/60 split (seed 1234) and asserted not-significant. That is
        statistically illiterate - two independent draws from the same
        distribution differ by chance ~5% of the time, and 1234 fired. The
        scorer's specificity is about the distribution of outcomes, not one
        lucky seed. This deterministic case (identical value sets) is the
        legitimate known-answer.
        """
        values = [i * 0.01 for i in range(-30, 30)]  # 60 values, mean -0.005
        s = score(values, list(values), target_entity="meta", peers=("apple",))
        assert s.asymmetry_score == pytest.approx(0.0, abs=1e-9)
        assert s.is_significant is False
        assert s.p_value == pytest.approx(1.0, abs=1e-9)
        assert abs(s.cohens_d) < 1e-9
        lo, hi = s.confidence_interval_lower, s.confidence_interval_upper
        assert lo <= 0 <= hi, "CI should straddle zero for no asymmetry"

    def test_effect_size_interpretation_thresholds(self):
        assert interpret_effect_size(0.0) == "negligible"
        assert interpret_effect_size(0.19) == "negligible"
        assert interpret_effect_size(0.2) == "small"
        assert interpret_effect_size(0.49) == "small"
        assert interpret_effect_size(0.5) == "medium"
        assert interpret_effect_size(0.79) == "medium"
        assert interpret_effect_size(0.8) == "large"
        assert interpret_effect_size(-1.4852) == "large"

    def test_is_significant_alpha_boundary(self):
        assert is_significant(0.0499) is True
        assert is_significant(0.05) is False
        assert is_significant(0.0501) is False


# ---------------------------------------------------------------------------
# Competitor-coverage-pattern integrity: citation completeness ratchet
# ---------------------------------------------------------------------------

def unsourced_competitor_entries():
    """All (profile, entity) competitor_relationships entries lacking any
    source_url/source_urls citation."""
    import glob

    bad = []
    for f in sorted(glob.glob(str(REPO_ROOT / "profiles" / "*.yaml"))):
        with open(f) as fh:
            data = yaml.safe_load(fh)
        cr = (data or {}).get("competitor_relationships") or {}
        for entity, block in cr.items():
            if isinstance(block, dict) and (
                "source_url" not in block and "source_urls" not in block
            ):
                bad.append((Path(f).name, entity))
    return bad


class TestCompetitorCitationRatchet:
    """The repo rule is 'every fact needs a source URL'. 45 competitor
    relationship entries across the 14 publication profiles currently lack
    any citation - fixing all 45 is out of scope for one Type D window, so
    this is a RATCHET, not a schema gate: the count may shrink as entries
    get cited, but it must never grow. A future run that adds an uncited
    competitor_relationships entry trips this test."""

    UNSOURCED_BASELINE = 45  # measured 2026-09-04 21:00 PDT, deterministic

    def test_unsourced_count_does_not_grow(self):
        bad = unsourced_competitor_entries()
        assert len(bad) <= self.UNSOURCED_BASELINE, (
            f"unsourced competitor entries grew to {len(bad)} "
            f"(baseline {self.UNSOURCED_BASELINE}); new entries must carry "
            f"source_url/source_urls"
        )

    def test_unsourced_count_is_deterministic(self):
        assert len(unsourced_competitor_entries()) == len(
            unsourced_competitor_entries()
        )

    def test_each_unsourced_entry_still_names_partner_and_prediction(self):
        """Unsourced entries must at least not be empty stubs."""
        import glob

        for f in sorted(glob.glob(str(REPO_ROOT / "profiles" / "*.yaml"))):
            with open(f) as fh:
                data = yaml.safe_load(fh)
            cr = (data or {}).get("competitor_relationships") or {}
            for entity, block in cr.items():
                if not isinstance(block, dict):
                    continue
                if "source_url" not in block and "source_urls" not in block:
                    assert block.get("description") or block.get(
                        "coverage_prediction"
                    ), f"{Path(f).name}:{entity} is an uncited empty stub"

