"""
Test: WIRED × Google Smart Glasses Framing Paradox (Type A, Aug 6 2026 21:00 PT)

KEY FINDING: WIRED treats Google/Samsung Android XR glasses (cameras, mics,
always-on Gemini AI) with product-review framing while treating functionally
identical Meta Ray-Ban glasses with investigative-surveillance framing. This
is despite Condé Nast having a MORE adversarial financial relationship with
Google (traffic collapse, antitrust litigation, no deal) than with Meta
(no deal, but also no active financial harm).

This reveals the Advertising Dependency Paradox at the product level:
Google still sends residual traffic and ad revenue, making adversarial
product coverage risky. Meta sends zero, making adversarial coverage
cost-free. The differential serves Google's competitive interests in
the smart glasses market.
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    filepath = os.path.join(PROFILES_DIR, filename)
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def research():
    return load_yaml('competitor-coverage-research.yaml')


@pytest.fixture(scope='module')
def wired_profile():
    return load_yaml('wired.yaml')


@pytest.fixture(scope='module')
def wired_research(research):
    return research['publications']['wired']


# ===================================================================
# Test Class 1: Google Smart Glasses Framing Section Exists
# ===================================================================

class TestGoogleSmartGlassesFramingExists:
    """Verify the google_smart_glasses_framing section is present and populated."""

    def test_section_exists(self, wired_research):
        assert 'google_smart_glasses_framing' in wired_research

    def test_has_discovery_date(self, wired_research):
        section = wired_research['google_smart_glasses_framing']
        assert 'discovery_date' in section
        assert '2026-08-06' in str(section['discovery_date'])

    def test_has_description(self, wired_research):
        section = wired_research['google_smart_glasses_framing']
        assert 'description' in section
        assert len(section['description']) > 200

    def test_has_source_urls(self, wired_research):
        section = wired_research['google_smart_glasses_framing']
        # Check for at least one source URL field
        source_keys = [k for k in section.keys() if 'source' in k.lower()]
        assert len(source_keys) >= 2, f"Expected at least 2 source URL fields, got {source_keys}"


# ===================================================================
# Test Class 2: Google Glasses Feature Parity with Meta
# ===================================================================

class TestGoogleGlassesFeatureParity:
    """Verify the analysis documents that Google glasses have same features as Meta."""

    def test_cameras_documented(self, wired_research):
        desc = wired_research['google_smart_glasses_framing']['description']
        assert 'camera' in desc.lower()

    def test_ai_assistant_documented(self, wired_research):
        desc = wired_research['google_smart_glasses_framing']['description']
        assert 'gemini' in desc.lower()

    def test_meta_comparison_present(self, wired_research):
        desc = wired_research['google_smart_glasses_framing']['description']
        assert 'meta' in desc.lower()

    def test_same_product_category(self, wired_research):
        desc = wired_research['google_smart_glasses_framing']['description']
        assert 'same' in desc.lower() or 'identical' in desc.lower() or 'functionally' in desc.lower()

    def test_multiple_hardware_partners(self, wired_research):
        desc = wired_research['google_smart_glasses_framing']['description']
        # Google has 4 partners: Samsung, XREAL, Warby Parker, Gentle Monster
        partners_found = sum(1 for p in ['samsung', 'xreal', 'warby', 'gentle monster']
                           if p.lower() in desc.lower())
        assert partners_found >= 3, f"Expected 3+ hardware partners mentioned, found {partners_found}"


# ===================================================================
# Test Class 3: Framing Divergence Documentation
# ===================================================================

class TestFramingDivergence:
    """Verify the analysis documents the framing asymmetry."""

    def test_google_gets_product_review_framing(self, wired_research):
        desc = wired_research['google_smart_glasses_framing']['description']
        assert 'product-review' in desc.lower() or 'product review' in desc.lower()

    def test_meta_gets_surveillance_framing(self, wired_research):
        desc = wired_research['google_smart_glasses_framing']['description']
        assert 'surveillance' in desc.lower()

    def test_zero_surveillance_for_google(self, wired_research):
        desc = wired_research['google_smart_glasses_framing']['description']
        assert 'zero surveillance' in desc.lower() or 'ZERO surveillance' in desc

    def test_no_wiretapping_for_google(self, wired_research):
        desc = wired_research['google_smart_glasses_framing']['description']
        # Verify the analysis notes absence of wiretapping language for Google
        assert 'wiretapping' in desc.lower()  # Should mention it as absent

    def test_meta_tone_documented(self, wired_research):
        # Meta coverage tone should be adversarial
        assert wired_research['meta_coverage_tone'] == 'adversarial'

    def test_google_coverage_tone_adversarial(self, wired_research):
        # Google coverage tone is adversarial (at business/institutional level)
        # but NOT at the product/glasses level
        assert wired_research['google_coverage_tone'] == 'adversarial'


# ===================================================================
# Test Class 4: Advertising Dependency Paradox
# ===================================================================

class TestAdvertisingDependencyParadox:
    """Verify the structural explanation for the framing divergence."""

    def test_paradox_explained(self, wired_research):
        desc = wired_research['google_smart_glasses_framing']['description']
        assert 'advertising' in desc.lower() or 'ADVERTISING' in desc

    def test_residual_revenue_documented(self, wired_research):
        desc = wired_research['google_smart_glasses_framing']['description']
        # Google still provides residual ad/traffic revenue
        assert 'residual' in desc.lower()

    def test_meta_zero_revenue(self, wired_research):
        desc = wired_research['google_smart_glasses_framing']['description']
        # Meta provides zero revenue — attacking is cost-free
        assert 'cost-free' in desc.lower() or 'zero' in desc.lower()

    def test_competitive_positioning_factor(self, wired_research):
        desc = wired_research['google_smart_glasses_framing']['description']
        assert 'competitive' in desc.lower()


# ===================================================================
# Test Class 5: Neither Company Has a Deal
# ===================================================================

class TestNoDealNoDealParadox:
    """Both Google and Meta have no deal with Condé Nast, yet are treated differently."""

    def test_no_meta_deal(self, wired_research):
        # Verify no Meta deal documented
        assert wired_research['meta_coverage_tone'] == 'adversarial'

    def test_no_google_deal_in_profile(self, wired_profile):
        google_rel = wired_profile.get('competitor_relationships', {}).get('google', {})
        assert google_rel.get('financial_tie') in ['adversarial_litigation', 'none', 'adversarial']

    def test_second_order_effect_explained(self, wired_research):
        desc = wired_research['google_smart_glasses_framing']['description']
        # Should explain why no-deal/no-deal produces different coverage
        assert 'second-order' in desc.lower() or 'ADVERTISING DEPENDENCY' in desc


# ===================================================================
# Test Class 6: Cross-Validation with Existing Analysis
# ===================================================================

class TestCrossValidationWithExistingAnalysis:
    """Verify consistency with existing google_coverage and advertising_dependency sections."""

    def test_google_traffic_collapse_exists(self, wired_research):
        assert 'google_traffic_collapse' in wired_research

    def test_advertising_dependency_paradox_exists(self, wired_research):
        assert 'advertising_dependency_paradox' in wired_research

    def test_google_litigation_source_exists(self, wired_research):
        assert 'google_litigation_source' in wired_research

    def test_google_coverage_tone_consistent(self, wired_research):
        # Google coverage tone should be adversarial at institutional level
        assert wired_research['google_coverage_tone'] == 'adversarial'
        # But the smart glasses framing section shows product-level treatment is different
        desc = wired_research['google_smart_glasses_framing']['description']
        assert 'product-review' in desc.lower()

    def test_apple_coverage_tone_consistent(self, wired_research):
        # Apple also gets soft treatment for camera-equipped wearables
        assert wired_research['apple_coverage_tone'] == 'neutral_to_positive'


# ===================================================================
# Test Class 7: Camera Count Paradox Extension
# ===================================================================

class TestCameraCountParadoxExtension:
    """
    The camera-count paradox (already documented for Apple/Meta via WIRED
    and Google/Meta via FT) now extends to WIRED × Google: the entity
    with EQUIVALENT cameras gets LESS privacy scrutiny.
    """

    def test_meta_apple_camera_paradox_documented(self, wired_research):
        # Apple examples should show 12-camera device getting soft treatment
        apple_examples = wired_research.get('apple_examples', [])
        assert len(apple_examples) > 0

    def test_google_glasses_have_cameras(self, wired_research):
        desc = wired_research['google_smart_glasses_framing']['description']
        assert 'camera' in desc.lower()
        assert 'photo' in desc.lower() or 'video' in desc.lower() or 'capture' in desc.lower()

    def test_meta_glasses_surveillance_framing(self, wired_research):
        # Meta coverage should have surveillance terms
        meta_examples = wired_research.get('meta_examples', [])
        assert any('surveillance' in str(ex).lower() or 'dormant' in str(ex).lower()
                   for ex in meta_examples)

    def test_paradox_extends_from_ft_to_wired(self, research):
        # FT also shows this pattern (already documented)
        ft = research['publications']['financial-times']
        ft_google_tone = ft.get('google_coverage_tone', '')
        assert 'positive' in ft_google_tone or 'neutral' in ft_google_tone


# ===================================================================
# Test Class 8: Source URL Validation
# ===================================================================

class TestSourceURLValidation:
    """Verify all source URLs in the new section are present and non-empty."""

    def test_google_glasses_source_present(self, wired_research):
        section = wired_research['google_smart_glasses_framing']
        assert 'google_glasses_source' in section
        assert section['google_glasses_source'].startswith('http')

    def test_samsung_google_io_source_present(self, wired_research):
        section = wired_research['google_smart_glasses_framing']
        assert 'samsung_google_io_source' in section
        assert section['samsung_google_io_source'].startswith('http')

    def test_privacy_comparison_source_present(self, wired_research):
        section = wired_research['google_smart_glasses_framing']
        assert 'privacy_comparison_source' in section
        assert section['privacy_comparison_source'].startswith('http')
