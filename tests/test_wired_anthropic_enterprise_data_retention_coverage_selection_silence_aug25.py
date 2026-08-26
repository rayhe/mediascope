"""
Test: WIRED Coverage Selection Silence — Anthropic Mandatory 30-Day Enterprise Data Retention Override

Mechanism #312: WIRED (Condé Nast, OpenAI content deal since Aug 2024) published ZERO
standalone articles covering Anthropic's mandatory 30-day enterprise data retention
policy override (announced Jun 9, 2026), despite 15+ other outlets covering the story.

The policy overrode existing zero-retention agreements, drew backlash from Microsoft CEO
Satya Nadella, White House AI adviser David Sacks, and Palantir CEO Alex Karp. Anthropic
was forced to backtrack (Aug 20). OpenAI countered with "Private Safety Processing" (Aug 19).
WIRED covered none of it, despite extensively covering Meta's data practices adversarially.

Date: 2026-08-25
Type A: Competitor Coverage Deep Dive — WIRED + Anthropic enterprise data retention
"""
import pytest
import yaml
import os
import re
from pathlib import Path


REPO_ROOT = Path(__file__).parent.parent
COMPETITOR_COVERAGE = REPO_ROOT / "profiles" / "competitor-coverage-research.yaml"
WIRED_PROFILE = REPO_ROOT / "profiles" / "wired.yaml"


@pytest.fixture(scope="module")
def competitor_data():
    with open(COMPETITOR_COVERAGE) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def wired_data():
    with open(WIRED_PROFILE) as f:
        return yaml.safe_load(f)


def find_mechanism(data, target_id=312):
    """Recursively find mechanism by ID, handling both mechanism_id and mechanism_number keys."""
    if isinstance(data, dict):
        for key, value in data.items():
            if key in ("mechanism_id", "mechanism_number") and value == target_id:
                return data
            if isinstance(value, (dict, list)):
                result = find_mechanism(value, target_id)
                if result:
                    # Return the parent dict if the result is a nested match
                    if "type" in data or "mechanism_id" in data or "mechanism_number" in data:
                        return data
                    return result
    elif isinstance(data, list):
        for item in data:
            result = find_mechanism(item, target_id)
            if result:
                return result
    return None


class TestMechanism312Exists:
    """Verify mechanism #312 exists in competitor-coverage-research.yaml with correct metadata."""

    def test_mechanism_exists(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None, "Mechanism #312 must exist in competitor-coverage-research.yaml"

    def test_mechanism_type(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        assert mechanism.get("mechanism_type") == "coverage_selection_silence"

    def test_finding_type(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        assert mechanism.get("finding_type") == "coverage_selection_gap"

    def test_publication(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        assert mechanism.get("publication") == "WIRED"


class TestAnthropicDataRetentionPolicy:
    """Verify the documented facts about Anthropic's 30-day data retention policy."""

    def test_policy_announced_date(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        policy = mechanism.get("anthropic_data_retention_policy", {})
        assert policy.get("announced") == "2026-06-09"

    def test_policy_overrides_zdr(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        policy = mechanism.get("anthropic_data_retention_policy", {})
        policy_text = str(policy.get("policy", "")).lower()
        assert "zero-retention" in policy_text or "zero retention" in policy_text

    def test_backlash_figures_documented(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        policy = mechanism.get("anthropic_data_retention_policy", {})
        figures = policy.get("backlash_figures", [])
        names = " ".join(figures).lower()
        assert "nadella" in names, "Satya Nadella must be listed as backlash figure"
        assert "sacks" in names, "David Sacks must be listed as backlash figure"
        assert "karp" in names, "Alex Karp must be listed as backlash figure"

    def test_microsoft_restricted_access(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        policy = mechanism.get("anthropic_data_retention_policy", {})
        action = str(policy.get("microsoft_action", "")).lower()
        assert "restrict" in action

    def test_anthropic_backtrack_documented(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        policy = mechanism.get("anthropic_data_retention_policy", {})
        backtrack = str(policy.get("anthropic_backtrack", "")).lower()
        assert "2026-08-20" in backtrack

    def test_anthropic_own_admission_documented(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        policy = mechanism.get("anthropic_data_retention_policy", {})
        admission = str(policy.get("anthropic_own_admission", "")).lower()
        assert "unpopular" in admission


class TestOpenAICounterResponse:
    """Verify OpenAI's Private Safety Processing competitive counter is documented."""

    def test_openai_counter_date(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        counter = mechanism.get("openai_counter", {})
        assert counter.get("announcement") == "2026-08-19"

    def test_openai_counter_product(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        counter = mechanism.get("openai_counter", {})
        assert "Private Safety Processing" in str(counter.get("product", ""))

    def test_openai_counter_preserves_zdr(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        counter = mechanism.get("openai_counter", {})
        approach = str(counter.get("approach", "")).lower()
        assert "without retaining" in approach or "without retain" in approach or "not retain" in approach


class TestWIREDCoverageGap:
    """Verify the core asymmetry: WIRED zero coverage vs 15+ outlets covering the story."""

    def test_wired_zero_articles(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        assert mechanism.get("wired_articles_on_topic") == 0

    def test_other_outlets_covered(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        other_coverage = mechanism.get("other_outlet_coverage", [])
        assert len(other_coverage) >= 10, f"At least 10 other outlets must be documented, found {len(other_coverage)}"

    def test_wsj_covered(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        outlets = [item.get("outlet", "") for item in mechanism.get("other_outlet_coverage", [])]
        assert "WSJ" in outlets

    def test_techcrunch_covered(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        outlets = [item.get("outlet", "") for item in mechanism.get("other_outlet_coverage", [])]
        assert "TechCrunch" in outlets

    def test_reuters_covered(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        outlets = [item.get("outlet", "") for item in mechanism.get("other_outlet_coverage", [])]
        assert "Reuters" in outlets

    def test_bloomberg_covered(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        outlets = [item.get("outlet", "") for item in mechanism.get("other_outlet_coverage", [])]
        assert "Bloomberg" in outlets


class TestMetaCoverageContrast:
    """Verify the documented contrast between WIRED's Meta data coverage and Anthropic data silence."""

    def test_wired_meta_adversarial(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        contrast = mechanism.get("wired_meta_data_coverage_contrast", {})
        assert contrast.get("wired_meta_data_articles_adversarial") is True

    def test_wired_meta_nametag_investigation(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        contrast = mechanism.get("wired_meta_data_coverage_contrast", {})
        nametag = str(contrast.get("meta_nametag_investigation", ""))
        assert "3" in nametag, "WIRED published 3+ NameTag investigation articles"

    def test_wired_anthropic_breach_but_not_retention(self, competitor_data):
        """WIRED covered Anthropic breaches (Jul 31) but NOT Anthropic data retention policy."""
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        contrast = mechanism.get("wired_meta_data_coverage_contrast", {})
        assert contrast.get("wired_anthropic_breach_articles") == 2
        assert contrast.get("wired_anthropic_data_retention_articles") == 0


class TestFinancialContextAndPrediction:
    """Verify financial relationship documentation and prediction logic."""

    def test_conde_nast_openai_deal(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        fin = mechanism.get("financial_context", {})
        openai_deal = str(fin.get("conde_nast_openai_deal", "")).lower()
        assert "aug 2024" in openai_deal or "content" in openai_deal

    def test_conde_nast_no_meta_deal(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        fin = mechanism.get("financial_context", {})
        meta_deal = str(fin.get("conde_nast_meta_deal", "")).lower()
        assert "none" in meta_deal

    def test_prediction_dual_incentive(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        fin = mechanism.get("financial_context", {})
        prediction = str(fin.get("prediction", "")).lower()
        assert "dual incentive" in prediction or "silence" in prediction

    def test_asymmetry_score(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        score = mechanism.get("asymmetry_score")
        assert score is not None
        assert 0.7 <= score <= 1.0


class TestCrossReferences:
    """Verify mechanism #312 cross-references related mechanisms."""

    def test_references_mechanism_154(self, competitor_data):
        """Cross-reference to WIRED Anthropic automode coverage silence."""
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        refs = mechanism.get("cross_references", [])
        ref_ids = [r.get("mechanism_id") for r in refs]
        assert 154 in ref_ids

    def test_references_mechanism_48(self, competitor_data):
        """Cross-reference to WIRED OpenAI ad coverage gap."""
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        refs = mechanism.get("cross_references", [])
        ref_ids = [r.get("mechanism_id") for r in refs]
        assert 48 in ref_ids

    def test_references_mechanism_288(self, competitor_data):
        """Cross-reference to WSJ data retention vocabulary bifurcation."""
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        refs = mechanism.get("cross_references", [])
        ref_ids = [r.get("mechanism_id") for r in refs]
        assert 288 in ref_ids

    def test_confounding_factors_present(self, competitor_data):
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        factors = mechanism.get("confounding_factors", [])
        assert len(factors) >= 3, "At least 3 confounding factors must be documented"

    def test_strong_against_confounding_documented(self, competitor_data):
        """The strongest counter-confounding factor (WIRED covered Anthropic breaches same period)."""
        mechanism = find_mechanism(competitor_data, 312)
        assert mechanism is not None
        factors = mechanism.get("confounding_factors", [])
        strong_factors = [f for f in factors if "STRONG" in str(f.get("strength", ""))]
        assert len(strong_factors) >= 1
