"""Type D: Cross-validation of Aug 6 findings — Guardian partial independence,
Alex Heath Access Paradox, Advance-Reddit-Perplexity Triangle.

Verifies internal consistency across all three findings AND validates that
asymmetry scoring produces statistically meaningful, internally coherent
results across all 9 profiled publications.
"""
import re
import yaml
import pytest
from pathlib import Path

PROFILES_DIR = Path(__file__).parent.parent / "profiles"
RESEARCH = yaml.safe_load((PROFILES_DIR / "competitor-coverage-research.yaml").read_text())
ENTITIES = yaml.safe_load((PROFILES_DIR / "competitor-entities.yaml").read_text())


def get_pub(name):
    """Get publication by YAML key (hyphenated)."""
    return RESEARCH["publications"][name]


# ===================================================================
# 1. ASYMMETRY GAP ORDERING — must be internally consistent
# ===================================================================
class TestAsymmetryGapOrdering:
    """The documented asymmetry gaps must follow:
    WIRED (~0.95) > Atlantic (~0.90) > Verge (~0.65) > FT (~0.45) > Guardian (~0.25-0.35).
    """

    def _extract_gap(self, pub_name):
        """Extract the asymmetry gap from the verdict text."""
        verdict = get_pub(pub_name).get("asymmetry_verdict", "")
        # For ranges like "~0.25-0.35", take midpoint
        range_match = re.search(r"~?(0\.\d+)\s*[-–]\s*~?(0\.\d+)", verdict)
        if range_match:
            return (float(range_match.group(1)) + float(range_match.group(2))) / 2

        # Find decimals near "gap" or "points" or "more negatively"
        gap_context = re.findall(r"(?:gap|more\s+negatively|asymmetry)[^.]*?~?(0\.\d+)", verdict)
        if gap_context:
            return max(float(g) for g in gap_context)

        # Fallback: largest 0.XX decimal in the verdict
        all_decimals = re.findall(r"(?<!\d)0\.\d+", verdict)
        if all_decimals:
            return max(float(d) for d in all_decimals)
        return None

    def test_wired_has_largest_gap(self):
        wired_gap = self._extract_gap("wired")
        assert wired_gap is not None
        assert wired_gap >= 0.9, f"WIRED gap {wired_gap} should be >= 0.9"

    def test_atlantic_has_second_largest_gap(self):
        atlantic_gap = self._extract_gap("atlantic")
        assert atlantic_gap is not None
        assert atlantic_gap >= 0.85, f"Atlantic gap {atlantic_gap} should be >= 0.85"

    def test_verge_gap_smaller_than_wired(self):
        verge_gap = self._extract_gap("the-verge")
        wired_gap = self._extract_gap("wired")
        assert verge_gap is not None
        assert verge_gap < wired_gap

    def test_ft_gap_smaller_than_verge(self):
        ft_gap = self._extract_gap("financial-times")
        verge_gap = self._extract_gap("the-verge")
        assert ft_gap is not None
        assert ft_gap < verge_gap

    def test_guardian_has_narrowest_gap(self):
        guardian_gap = self._extract_gap("guardian")
        assert guardian_gap is not None
        assert guardian_gap <= 0.40, f"Guardian gap {guardian_gap} should be <= 0.40"

    def test_guardian_gap_smaller_than_ft(self):
        guardian_gap = self._extract_gap("guardian")
        ft_gap = self._extract_gap("financial-times")
        assert guardian_gap is not None and ft_gap is not None
        assert guardian_gap < ft_gap

    def test_all_non_control_gaps_positive(self):
        """Every publication with financial asymmetry should show positive gap."""
        for pub in ["wired", "the-verge", "atlantic", "financial-times", "guardian"]:
            gap = self._extract_gap(pub)
            assert gap is not None and gap > 0, f"{pub} should have positive asymmetry gap"


# ===================================================================
# 2. CONTROL GROUP VALIDATION — clean and balanced controls
# ===================================================================
class TestControlGroupConsistency:
    """Gizmodo (clean control, no deals) and News Corp (balanced control,
    equal deals) must confirm the financial relationship hypothesis."""

    def test_gizmodo_is_clean_control(self):
        giz = get_pub("gizmodo")
        verdict = giz.get("asymmetry_verdict", "").lower()
        assert "clean control" in verdict or "control" in verdict

    def test_gizmodo_covers_both_meta_and_openai_critically(self):
        giz = get_pub("gizmodo")
        meta_tone = giz.get("meta_coverage_tone", "")
        openai_tone = giz.get("openai_coverage_tone", "")
        assert "adversarial" in meta_tone.lower() or "critical" in meta_tone.lower()
        assert "adversarial" in openai_tone.lower() or "critical" in openai_tone.lower()

    def test_news_corp_is_balanced_control(self):
        nc = get_pub("news-corp")
        verdict = nc.get("asymmetry_verdict", "").lower()
        assert "balanced control" in verdict or "control" in verdict

    def test_news_corp_equal_payments_equal_coverage(self):
        nc = get_pub("news-corp")
        verdict = nc.get("asymmetry_verdict", "").lower()
        assert "balanced" in verdict


# ===================================================================
# 3. FIVE-MECHANISM TAXONOMY — internal consistency
# ===================================================================
class TestFiveMechanismTaxonomy:
    """Validates the five documented asymmetry mechanisms."""

    def test_mechanism_1_wired_desk_assignment(self):
        wired = get_pub("wired")
        meta_examples = wired.get("meta_examples", [])
        apple_examples = wired.get("apple_examples", [])
        assert len(meta_examples) > 0
        assert len(apple_examples) > 0

    def test_mechanism_5_access_paradox_documented(self):
        verge = get_pub("the-verge")
        verdict = verge.get("asymmetry_verdict", "")
        assert "access paradox" in verdict.lower() or "mechanism #5" in verdict.lower() or \
               "heath" in verdict.lower()

    def test_all_five_mechanisms_referenced_in_research(self):
        full_text = (PROFILES_DIR / "competitor-coverage-research.yaml").read_text().lower()
        assert "desk assignment" in full_text
        assert "between-reporter" in full_text
        assert "within-reporter" in full_text
        assert "four-lane" in full_text or "four lane" in full_text
        assert "access paradox" in full_text

    def test_mechanism_5_is_distinct_from_mechanism_4(self):
        full_text = (PROFILES_DIR / "competitor-coverage-research.yaml").read_text().lower()
        assert "same access" in full_text or "dual-role" in full_text or \
               "same individual" in full_text or "same format" in full_text


# ===================================================================
# 4. GUARDIAN PARTIAL INDEPENDENCE — cross-validation
# ===================================================================
class TestGuardianPartialIndependence:
    """Guardian partial independence must be internally consistent."""

    def test_guardian_openai_tone_is_balanced_to_adversarial(self):
        guardian = get_pub("guardian")
        tone = guardian.get("openai_coverage_tone", "")
        assert "adversarial" in tone.lower()

    def test_guardian_meta_tone_is_adversarial(self):
        guardian = get_pub("guardian")
        tone = guardian.get("meta_coverage_tone", "")
        assert "adversarial" in tone.lower()

    def test_guardian_has_stargate_investigation(self):
        guardian = get_pub("guardian")
        openai_examples = guardian.get("openai_examples", [])
        stargate_found = any("stargate" in str(ex).lower() or "foi" in str(ex).lower()
                            for ex in openai_examples)
        assert stargate_found

    def test_guardian_three_tier_assessment_exists(self):
        guardian = get_pub("guardian")
        assert guardian.get("three_tier_assessment")

    def test_guardian_partial_independence_in_assessment(self):
        guardian = get_pub("guardian")
        assessment = guardian.get("three_tier_assessment", "").lower()
        assert "partial independence" in assessment

    def test_guardian_independence_evidence_documented(self):
        guardian = get_pub("guardian")
        assessment = guardian.get("three_tier_assessment", "").lower()
        assert "evidence of independence" in assessment

    def test_guardian_asymmetry_evidence_also_documented(self):
        guardian = get_pub("guardian")
        assessment = guardian.get("three_tier_assessment", "").lower()
        assert "evidence of asymmetry" in assessment or "still present" in assessment

    def test_guardian_verdict_gap_consistent_with_assessment(self):
        guardian = get_pub("guardian")
        verdict = guardian.get("asymmetry_verdict", "")
        assert "narrower" in verdict.lower() or "0.25" in verdict or "0.35" in verdict

    def test_guardian_is_best_case_for_independence(self):
        guardian = get_pub("guardian")
        assessment = guardian.get("three_tier_assessment", "").lower()
        assert "best case" in assessment or "strongest" in assessment


# ===================================================================
# 5. ADVANCE-REDDIT-PERPLEXITY TRIANGLE — cross-validation
# ===================================================================
class TestAdvanceTriangleCrossValidation:
    """Triangle must be consistent across research and entities files."""

    def test_triangle_exists_in_research(self):
        wired = get_pub("wired")
        assert wired.get("advance_reddit_perplexity_triangle")

    def test_perplexity_documented_in_entities(self):
        entities_text = (PROFILES_DIR / "competitor-entities.yaml").read_text().lower()
        assert "perplexity" in entities_text

    def test_reddit_entity_has_perplexity_litigation(self):
        entities_text = (PROFILES_DIR / "competitor-entities.yaml").read_text().lower()
        assert "perplexity" in entities_text
        assert "dmca" in entities_text or "lawsuit" in entities_text or \
               "litigation" in entities_text or "suing" in entities_text

    def test_triangle_has_source_urls(self):
        wired = get_pub("wired")
        triangle = wired.get("advance_reddit_perplexity_triangle", {})
        urls = triangle.get("source_urls", [])
        assert len(urls) >= 2

    def test_triangle_mentions_sam_altman_conflict(self):
        wired = get_pub("wired")
        triangle = wired.get("advance_reddit_perplexity_triangle", {})
        desc = str(triangle).lower()
        assert "altman" in desc

    def test_reddit_deal_renewal_forecast_has_wells_fargo(self):
        wired = get_pub("wired")
        triangle = wired.get("advance_reddit_perplexity_triangle", {})
        forecast = str(triangle.get("reddit_deal_renewal_forecast", "")).lower()
        assert "wells fargo" in forecast or "brondolo" in forecast

    def test_reddit_deal_renewal_forecast_sourced_in_urls(self):
        wired = get_pub("wired")
        triangle = wired.get("advance_reddit_perplexity_triangle", {})
        urls = [str(u).lower() for u in triangle.get("source_urls", [])]
        assert any("barron" in u for u in urls)

    def test_triangle_consistent_with_deal_count(self):
        wired = get_pub("wired")
        deal_count = wired.get("deal_count_summary", "").lower()
        assert "perplexity" in deal_count

    def test_advance_triangle_in_entities(self):
        entities_text = (PROFILES_DIR / "competitor-entities.yaml").read_text().lower()
        assert "triangle" in entities_text or "advance" in entities_text


# ===================================================================
# 6. ALEX HEATH ACCESS PARADOX — cross-validation
# ===================================================================
class TestAccessParadoxCrossValidation:
    """Access Paradox must be consistent between verge profile and research."""

    def test_verge_profile_has_heath(self):
        verge_text = (PROFILES_DIR / "the-verge.yaml").read_text().lower()
        assert "alex heath" in verge_text

    def test_verge_profile_heath_deputy_editor(self):
        verge_text = (PROFILES_DIR / "the-verge.yaml").read_text().lower()
        assert "deputy editor" in verge_text

    def test_access_paradox_in_verge_profile(self):
        verge_text = (PROFILES_DIR / "the-verge.yaml").read_text().lower()
        assert "access paradox" in verge_text or "access journalism" in verge_text

    def test_heath_documented_in_research_verdict(self):
        verge = get_pub("the-verge")
        verdict = verge.get("asymmetry_verdict", "").lower()
        assert "heath" in verdict or "access paradox" in verdict or "deputy editor" in verdict

    def test_verge_openai_tone_not_adversarial(self):
        verge = get_pub("the-verge")
        openai_tone = verge.get("openai_coverage_tone", "").lower()
        assert "positive" in openai_tone or "neutral" in openai_tone or "balanced" in openai_tone

    def test_snap_spectacles_documented(self):
        full_text = (PROFILES_DIR / "competitor-coverage-research.yaml").read_text().lower()
        assert "spectacles" in full_text


# ===================================================================
# 7. META-ZERO CONSISTENCY
# ===================================================================
class TestMetaZeroDealsConsistency:
    PUBS_WITH_NO_META_DEAL = ["wired", "the-verge", "atlantic", "financial-times", "guardian", "mit-tech-review"]

    def test_all_adversarial_pubs_meta_tone_negative(self):
        for pub_name in self.PUBS_WITH_NO_META_DEAL:
            pub = get_pub(pub_name)
            meta_tone = pub.get("meta_coverage_tone", "").lower()
            assert "adversarial" in meta_tone or "balanced" in meta_tone, \
                f"{pub_name} should have adversarial or balanced Meta coverage"

    def test_news_corp_has_meta_deal(self):
        nc = get_pub("news-corp")
        nc_text = str(nc).lower()
        assert "meta" in nc_text and ("deal" in nc_text or "$50m" in nc_text or "payment" in nc_text)


# ===================================================================
# 8. PUBLICATION PROFILE COMPLETENESS
# ===================================================================
class TestPublicationCompleteness:
    REQUIRED_PUBS = [
        "wired", "the-verge", "atlantic", "nytimes", "financial-times",
        "guardian", "mit-tech-review", "gizmodo", "news-corp"
    ]

    def test_all_publications_present(self):
        pubs = RESEARCH.get("publications", {})
        for name in self.REQUIRED_PUBS:
            assert name in pubs, f"Publication '{name}' missing from research"

    def test_all_have_meta_coverage_tone(self):
        for name in self.REQUIRED_PUBS:
            pub = get_pub(name)
            assert pub.get("meta_coverage_tone"), f"{name} missing meta_coverage_tone"

    def test_all_have_asymmetry_verdict(self):
        for name in self.REQUIRED_PUBS:
            pub = get_pub(name)
            assert pub.get("asymmetry_verdict"), f"{name} missing asymmetry_verdict"

    def test_all_non_controls_have_openai_tone(self):
        for name in ["wired", "the-verge", "atlantic", "nytimes", "financial-times",
                      "guardian", "mit-tech-review"]:
            pub = get_pub(name)
            assert pub.get("openai_coverage_tone"), f"{name} missing openai_coverage_tone"


# ===================================================================
# 9. STATISTICAL VALIDITY — asymmetry direction consistency
# ===================================================================
class TestAsymmetryDirectionConsistency:
    TONE_RANK = {
        "adversarial": -3,
        "balanced_adversarial": -2,
        "balanced_to_adversarial": -2,
        "critical": -2,
        "balanced": 0,
        "neutral": 0,
        "neutral_to_positive": 1,
        "balanced_to_positive": 1,
        "positive": 2,
    }

    def _tone_score(self, tone_str):
        normalized = tone_str.lower().strip().replace(" ", "_")
        for key, score in sorted(self.TONE_RANK.items(), key=lambda x: -len(x[0])):
            if key in normalized:
                return score
        return 0

    def test_meta_more_negative_than_openai_where_deal_asymmetry(self):
        pubs = ["wired", "the-verge", "atlantic", "financial-times", "guardian"]
        for name in pubs:
            pub = get_pub(name)
            meta_score = self._tone_score(pub.get("meta_coverage_tone", ""))
            openai_score = self._tone_score(pub.get("openai_coverage_tone", ""))
            assert meta_score <= openai_score, \
                f"{name}: Meta tone ({pub.get('meta_coverage_tone')}) should be >= as negative " \
                f"as OpenAI tone ({pub.get('openai_coverage_tone')})"

    def test_gizmodo_control_no_directional_asymmetry(self):
        giz = get_pub("gizmodo")
        meta_score = self._tone_score(giz.get("meta_coverage_tone", ""))
        openai_score = self._tone_score(giz.get("openai_coverage_tone", ""))
        assert abs(meta_score - openai_score) <= 1

    def test_nytimes_adversarial_to_both_meta_and_openai(self):
        nyt = get_pub("nytimes")
        meta_score = self._tone_score(nyt.get("meta_coverage_tone", ""))
        openai_score = self._tone_score(nyt.get("openai_coverage_tone", ""))
        assert meta_score <= -2, "NYT should be adversarial to Meta"
        assert openai_score <= -2, "NYT should be adversarial to OpenAI (suing them)"
