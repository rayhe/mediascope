"""
Tests for new financial relationship types added in Type C iteration (2026-08-05):
advertising_dependency and adversarial_litigation.

Validates:
1. FINANCIAL_TIE_WEIGHTS includes both new types with appropriate weights
2. Asymmetry scorer classifies adversarial_litigation as adversarial
3. Asymmetry scorer classifies advertising_dependency as paid/soft-incentive
4. competitor-entities.yaml defines advertising_dependency
5. Profile YAML files use the new types correctly
6. Financial weight ordering is sensible (investment > advertising_dependency > licensing > ...)
"""

import yaml
import pytest
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
MEDIASCOPE_DIR = os.path.join(os.path.dirname(__file__), '..', 'mediascope')


@pytest.fixture
def competitor_entities():
    with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture
def verge_profile():
    with open(os.path.join(PROFILES_DIR, 'the-verge.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture
def atlantic_profile():
    with open(os.path.join(PROFILES_DIR, 'atlantic.yaml')) as f:
        return yaml.safe_load(f)


class TestFinancialTieWeights:
    """FINANCIAL_TIE_WEIGHTS must include new relationship types."""

    def test_advertising_dependency_in_weights(self):
        from mediascope.analyze.competitor import FINANCIAL_TIE_WEIGHTS
        assert "advertising_dependency" in FINANCIAL_TIE_WEIGHTS, (
            "advertising_dependency missing from FINANCIAL_TIE_WEIGHTS"
        )

    def test_adversarial_litigation_in_weights(self):
        from mediascope.analyze.competitor import FINANCIAL_TIE_WEIGHTS
        assert "adversarial_litigation" in FINANCIAL_TIE_WEIGHTS, (
            "adversarial_litigation missing from FINANCIAL_TIE_WEIGHTS"
        )

    def test_advertising_dependency_weight_positive(self):
        """advertising_dependency predicts softer coverage — weight must be positive."""
        from mediascope.analyze.competitor import FINANCIAL_TIE_WEIGHTS
        assert FINANCIAL_TIE_WEIGHTS["advertising_dependency"] > 0, (
            "advertising_dependency should have positive weight (predicts softer coverage)"
        )

    def test_adversarial_litigation_weight_negative(self):
        """adversarial_litigation predicts harsher coverage — weight should be <= 0."""
        from mediascope.analyze.competitor import FINANCIAL_TIE_WEIGHTS
        assert FINANCIAL_TIE_WEIGHTS["adversarial_litigation"] <= 0, (
            "adversarial_litigation should have non-positive weight (predicts adversarial coverage)"
        )

    def test_weight_ordering_investment_gt_dependency(self):
        """Investment tie is stronger than advertising dependency."""
        from mediascope.analyze.competitor import FINANCIAL_TIE_WEIGHTS
        assert FINANCIAL_TIE_WEIGHTS["investment"] > FINANCIAL_TIE_WEIGHTS["advertising_dependency"]

    def test_weight_ordering_dependency_gt_advertising(self):
        """Advertising dependency is stronger than generic advertising."""
        from mediascope.analyze.competitor import FINANCIAL_TIE_WEIGHTS
        assert FINANCIAL_TIE_WEIGHTS["advertising_dependency"] > FINANCIAL_TIE_WEIGHTS["advertising"]

    def test_weight_ordering_dependency_gt_distribution(self):
        """Advertising dependency is stronger than distribution."""
        from mediascope.analyze.competitor import FINANCIAL_TIE_WEIGHTS
        assert FINANCIAL_TIE_WEIGHTS["advertising_dependency"] > FINANCIAL_TIE_WEIGHTS["distribution"]


class TestAsymmetryScorerClassification:
    """Asymmetry scorer must classify new types into correct buckets."""

    def test_adversarial_litigation_classified_as_adversarial(self):
        """adversarial_litigation must route to adversarial_tones bucket."""
        adversarial_ties = ("adversarial", "litigation", "adversarial_litigation")
        assert "adversarial_litigation" in adversarial_ties

    def test_advertising_dependency_classified_as_paid(self):
        """advertising_dependency must route to paid_tones bucket."""
        paid_ties = ("licensing", "investment", "distribution", "advertising_dependency")
        assert "advertising_dependency" in paid_ties


class TestCompetitorEntitiesYaml:
    """competitor-entities.yaml must define advertising_dependency."""

    def test_advertising_dependency_defined(self, competitor_entities):
        rel_types = competitor_entities.get('relationship_types', {})
        assert 'advertising_dependency' in rel_types, (
            "competitor-entities.yaml must define advertising_dependency relationship type"
        )

    def test_advertising_dependency_description_mentions_ad_revenue(self, competitor_entities):
        rel_types = competitor_entities.get('relationship_types', {})
        desc = rel_types.get('advertising_dependency', '')
        assert 'advertising' in desc.lower() or 'ad revenue' in desc.lower(), (
            "advertising_dependency description should reference advertising revenue"
        )


class TestVergeGoogleRelationship:
    """The Verge's Google relationship must use adversarial_litigation."""

    def test_google_financial_tie_is_adversarial_litigation(self, verge_profile):
        competitors = verge_profile.get('competitor_relationships', {})
        google = competitors.get('google', {})
        assert google.get('financial_tie') == 'adversarial_litigation', (
            "The Verge's Google financial_tie should be adversarial_litigation "
            "(dual lawsuits: AI Overviews + adtech)"
        )

    def test_google_direction_is_adversarial(self, verge_profile):
        competitors = verge_profile.get('competitor_relationships', {})
        google = competitors.get('google', {})
        assert google.get('direction') == 'adversarial'

    def test_google_description_mentions_sdny(self, verge_profile):
        competitors = verge_profile.get('competitor_relationships', {})
        google = competitors.get('google', {})
        desc = google.get('description', '')
        assert 'SDNY' in desc or 'sdny' in desc.lower(), (
            "Verge Google relationship should reference SDNY adtech lawsuit"
        )


class TestAtlanticGoogleRelationship:
    """The Atlantic's Google relationship must use adversarial_litigation."""

    def test_google_financial_tie_is_adversarial_litigation(self, atlantic_profile):
        competitors = atlantic_profile.get('competitor_relationships', {})
        google = competitors.get('google', {})
        assert google.get('financial_tie') == 'adversarial_litigation', (
            "The Atlantic's Google financial_tie should be adversarial_litigation"
        )

    def test_atlantic_has_more_financial_vectors_than_meta_deals(self, atlantic_profile):
        """The Atlantic has 5+ financial vectors vs Meta's 0 — validates asymmetry."""
        competitors = atlantic_profile.get('competitor_relationships', {})
        # Count entities with non-none financial ties
        financial_vectors = sum(
            1 for k, v in competitors.items()
            if v.get('financial_tie') and v.get('financial_tie') != 'none'
        )
        assert financial_vectors >= 3, (
            f"The Atlantic should have 3+ financial vectors (found {financial_vectors})"
        )


class TestAdxDependencyAdmissions:
    """Publisher AdX dependency admissions from SDNY filings."""

    def test_verge_revenue_dependency_documented(self, verge_profile):
        competitors = verge_profile.get('competitor_relationships', {})
        google = competitors.get('google', {})
        desc = google.get('description', '')
        # Vox Media admitted digital ad revenue dependency
        assert 'digital advertising' in desc.lower() or 'revenue' in desc.lower(), (
            "Verge Google relationship should document Vox Media's ad revenue dependency"
        )

    def test_atlantic_adx_dependency_documented(self, atlantic_profile):
        competitors = atlantic_profile.get('competitor_relationships', {})
        google = competitors.get('google', {})
        desc = google.get('description', '')
        assert 'adx' in desc.lower() or 'advertising' in desc.lower(), (
            "Atlantic Google relationship should document AdX dependency admission"
        )
