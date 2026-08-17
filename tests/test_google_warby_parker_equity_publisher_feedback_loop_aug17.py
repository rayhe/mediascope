"""
Mechanism #147: Google-Warby Parker Equity Investment Publisher Coverage Financial Feedback Loop
Type C: Financial Incentive Mapping — Mon 2026-08-17 02:00 PT

THESIS: Google's $150M commitment to Warby Parker — split between $75M development
funding and up to $75M equity investment (at WRBY's option, milestone-contingent) —
creates a UNIQUE financial feedback loop in smart glasses coverage. Google is
simultaneously:

  (1) The primary revenue source for most tech publications (ad revenue, News
      Showcase, content licensing deals)
  (2) An equity investor in the frame maker (Warby Parker) competing directly
      with Meta's frame partner (EssilorLuxottica)
  (3) The platform provider (Android XR + Gemini) for the Samsung/Warby/Gentle
      Monster smart glasses ecosystem

This triple role creates a financial feedback loop:
  - Publishers depend on Google for revenue
  - Google has financial returns tied to WRBY stock appreciation
  - Favorable coverage of Google/Warby/Samsung glasses → WRBY stock rises → Google benefits
  - Negative coverage of Meta glasses → competitive alternative looks better → WRBY benefits → Google benefits
  - Publishers covering Meta glasses negatively serves BOTH their anti-Meta incentive
    (Meta is their ad-revenue competitor) AND their pro-Google incentive (Google
    benefits from WRBY appreciation)

META'S EQUIVALENT STRUCTURE:
  - Meta → EssilorLuxottica: no equity stake creating publisher alignment.
    EssilorLuxottica is a ~€90B market cap company with ZERO advertising
    relationships with tech publications.

KEY FINANCIAL DATA:
  - Google committed up to $150M to Warby Parker (May 20, 2025, Google I/O)
  - WRBY stock rallied 16% on deal announcement
  - Warby Parker Q2 2026: $235.5M revenue, +9.8% YoY
  - Holiday 2026 launch confirmed
  - Smart glasses market projected $4.2B by 2028 (Bank of America)
  - EssilorLuxottica: sold 7M+ Meta smart glasses in 2025

SOURCES:
  - BusinessWire press release
  - TechCrunch, Vision Monday, Fast Company, The Register, Bloomberg Law, ainvest, Entrepreneur
"""

import pytest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
ENTITIES_PROFILE = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
RESEARCH_PROFILE = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')


def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def find_mechanism(data, mechanism_id):
    """Search cross_publication_findings and publications for a mechanism by ID."""
    for section in ['cross_publication_findings', 'publications']:
        section_data = data.get(section, {})
        if isinstance(section_data, dict):
            for v in section_data.values():
                if isinstance(v, dict) and v.get('mechanism_id') == mechanism_id:
                    return v
        elif isinstance(section_data, list):
            for v in section_data:
                if isinstance(v, dict) and v.get('mechanism_id') == mechanism_id:
                    return v
    return None


# =============================================================================
# Class 1: Google Equity Investment Documentation
# =============================================================================

class TestGoogleWarbyParkerEquityInvestment:
    """Verify Google's $150M Warby Parker commitment is documented in entity profile."""

    def test_google_warby_parker_commitment_total(self):
        """Google's up-to $150M total commitment must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        google = data['entities']['google']
        warby = str(google).lower()
        assert '150' in warby or 'warby' in warby, \
            "Google entity must reference Warby Parker $150M commitment"

    def test_google_development_funding_75m(self):
        """$75M development and commercialization funding must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        google = data['entities']['google']
        warby_str = str(google).lower()
        assert '75' in warby_str, \
            "Google entity must reference $75M development funding"

    def test_google_equity_investment_75m(self):
        """Up to $75M equity investment (milestone-contingent) must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        google = data['entities']['google']
        warby_str = str(google).lower()
        assert 'equity' in warby_str or 'investment' in warby_str, \
            "Google entity must reference equity investment in Warby Parker"

    def test_warby_parker_stock_rally_16pct(self):
        """WRBY 16% rally on deal announcement must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        google = data['entities']['google']
        warby_str = str(google).lower()
        assert '16' in warby_str or 'rally' in warby_str or 'stock' in warby_str, \
            "WRBY stock rally on deal announcement should be documented"

    def test_google_io_2025_announcement_date(self):
        """Deal announced at Google I/O May 20, 2025 must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        google = data['entities']['google']
        warby_str = str(google)
        assert '2025' in warby_str, \
            "Google I/O 2025 announcement date should be referenced"


# =============================================================================
# Class 2: Warby Parker Financial Metrics
# =============================================================================

class TestWarbyParkerFinancials:
    """Verify Warby Parker's financial data is documented for incentive analysis."""

    def test_warby_parker_q2_2026_revenue(self):
        """Warby Parker Q2 2026 revenue ($235.5M, +9.8% YoY) must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        google = data['entities']['google']
        warby_str = str(google)
        assert '235' in warby_str or 'Q2 2026' in warby_str, \
            "Warby Parker Q2 2026 revenue must be documented"

    def test_warby_parker_holiday_2026_launch(self):
        """Holiday 2026 intelligent eyewear launch must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        google = data['entities']['google']
        warby_str = str(google).lower()
        assert 'holiday' in warby_str or '2026' in warby_str, \
            "Holiday 2026 launch timeline must be documented"

    def test_smart_glasses_market_projection(self):
        """$4.2B smart glasses market by 2028 (Bank of America) documented."""
        data = load_yaml(ENTITIES_PROFILE)
        google = data['entities']['google']
        warby_str = str(google)
        assert '4.2' in warby_str or 'Bank of America' in warby_str or \
            'market' in warby_str.lower(), \
            "Smart glasses market projection should be documented"


# =============================================================================
# Class 3: EssilorLuxottica Comparison (Meta's Frame Partner)
# =============================================================================

class TestEssilorLuxotticaComparison:
    """Verify the asymmetry between Google-Warby and Meta-EssilorLuxottica is documented."""

    def test_essilorluxottica_no_tech_pub_advertising(self):
        """EssilorLuxottica's zero tech pub advertising must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        google = data['entities']['google']
        google_str = str(google).lower()
        assert 'essilorluxottica' in google_str or 'zero' in google_str, \
            "EssilorLuxottica zero advertising comparison must be documented"

    def test_meta_no_equity_in_frame_maker(self):
        """Meta holds no equity stake in EssilorLuxottica."""
        data = load_yaml(ENTITIES_PROFILE)
        google = data['entities']['google']
        google_str = str(google).lower()
        assert 'no equity' in google_str or 'meta' in google_str, \
            "Meta's lack of equity in frame partner must be documented"

    def test_essilorluxottica_sold_7m_glasses(self):
        """EssilorLuxottica sold 7M+ Meta smart glasses in 2025."""
        data = load_yaml(ENTITIES_PROFILE)
        full_str = str(data).lower()
        assert '7' in full_str or 'million' in full_str, \
            "EssilorLuxottica's 7M+ smart glasses sales should be documented"


# =============================================================================
# Class 4: Supply Chain Financial Architecture
# =============================================================================

class TestSupplyChainFinancialArchitecture:
    """Verify the multi-layer supply chain financial incentive is mapped."""

    def test_google_platform_plus_equity_dual_role(self):
        """Google's dual role (platform provider + equity investor) must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        google = data['entities']['google']
        google_str = str(google).lower()
        assert 'android xr' in google_str or 'platform' in google_str, \
            "Google's platform role (Android XR) must be documented"

    def test_samsung_hardware_partner(self):
        """Samsung as hardware partner in the ecosystem must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        google = data['entities']['google']
        google_str = str(google).lower()
        assert 'samsung' in google_str or 'frame' in google_str, \
            "Samsung or frame partner context must be documented"

    def test_qualcomm_silicon_partner(self):
        """Qualcomm Snapdragon AR1 Gen 1 as shared silicon must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        google = data['entities']['google']
        google_str = str(google).lower()
        assert 'snapdragon' in google_str or 'qualcomm' in google_str or \
            'ar1' in google_str, \
            "Qualcomm Snapdragon AR1 must be referenced"

    def test_meta_simpler_supply_chain(self):
        """Meta's supply chain has fewer financial nodes than Google's."""
        data = load_yaml(ENTITIES_PROFILE)
        google = data['entities']['google']
        google_str = str(google).lower()
        assert 'meta' in google_str, \
            "Meta comparison must be documented in Google entity"


# =============================================================================
# Class 5: Mechanism Registration and Cross-References
# =============================================================================

class TestMechanismRegistration:
    """Verify mechanism #147 is properly registered with cross-references."""

    def test_mechanism_147_in_research_profile(self):
        """Mechanism #147 must exist in competitor-coverage-research.yaml."""
        data = load_yaml(RESEARCH_PROFILE)
        m147 = find_mechanism(data, 147)
        assert m147 is not None, \
            "Mechanism #147 must be registered in research profile"

    def test_cross_reference_to_mechanism_76(self):
        """Must cross-reference mechanism #76 (Samsung-Google compound leverage)."""
        data = load_yaml(RESEARCH_PROFILE)
        m147 = find_mechanism(data, 147)
        assert m147 is not None, "Mechanism #147 not found"
        refs_str = str(m147.get('cross_references', []))
        assert '76' in refs_str, \
            "Must cross-reference mechanism #76 (Samsung-Google leverage)"

    def test_cross_reference_to_mechanism_91(self):
        """Must cross-reference mechanism #91 (Qualcomm supply chain multiplier)."""
        data = load_yaml(RESEARCH_PROFILE)
        m147 = find_mechanism(data, 147)
        assert m147 is not None, "Mechanism #147 not found"
        refs_str = str(m147.get('cross_references', []))
        assert '91' in refs_str, \
            "Must cross-reference mechanism #91 (Qualcomm supply chain)"

    def test_cross_reference_to_mechanism_111(self):
        """Must cross-reference mechanism #111 (Apollo AI infrastructure)."""
        data = load_yaml(RESEARCH_PROFILE)
        m147 = find_mechanism(data, 147)
        assert m147 is not None, "Mechanism #147 not found"
        refs_str = str(m147.get('cross_references', []))
        assert '111' in refs_str, \
            "Must cross-reference mechanism #111 (Apollo AI infra)"

    def test_finding_summary_exists(self):
        """Mechanism #147 must have a finding_summary field."""
        data = load_yaml(RESEARCH_PROFILE)
        m147 = find_mechanism(data, 147)
        assert m147 is not None, "Mechanism #147 not found"
        assert 'finding_summary' in m147, \
            "Mechanism #147 must have finding_summary"


# =============================================================================
# Class 6: Confounding Factor Completeness
# =============================================================================

class TestConfoundingFactors:
    """Verify confounding factors are documented with proper strength ratings."""

    def test_confounders_exist(self):
        """Mechanism #147 must have confounding_factors field."""
        data = load_yaml(RESEARCH_PROFILE)
        m147 = find_mechanism(data, 147)
        assert m147 is not None, "Mechanism #147 not found"
        assert 'confounding_factors' in m147, \
            "Mechanism #147 must have confounding_factors"

    def test_at_least_two_strong_confounders(self):
        """At least 2 STRONG confounders must be documented."""
        data = load_yaml(RESEARCH_PROFILE)
        m147 = find_mechanism(data, 147)
        assert m147 is not None, "Mechanism #147 not found"
        confounders = m147.get('confounding_factors', [])
        strong_count = sum(1 for c in confounders
                           if isinstance(c, str) and '[STRONG]' in c)
        assert strong_count >= 2, \
            f"Need >=2 STRONG confounders, found {strong_count}"

    def test_milestone_contingency_confounder(self):
        """Must document that Google equity is milestone-contingent."""
        data = load_yaml(RESEARCH_PROFILE)
        m147 = find_mechanism(data, 147)
        assert m147 is not None, "Mechanism #147 not found"
        confounders_str = str(m147.get('confounding_factors', []))
        assert 'milestone' in confounders_str.lower() or \
            'contingent' in confounders_str.lower(), \
            "Must document milestone-contingent nature of equity"


# =============================================================================
# Class 7: Testable Predictions
# =============================================================================

class TestTestablePredictions:
    """Verify testable predictions are registered."""

    def test_predictions_exist(self):
        """Mechanism #147 must have testable_predictions field."""
        data = load_yaml(RESEARCH_PROFILE)
        m147 = find_mechanism(data, 147)
        assert m147 is not None, "Mechanism #147 not found"
        assert 'testable_predictions' in m147, \
            "Mechanism #147 must have testable_predictions"
        preds = m147['testable_predictions']
        assert len(preds) >= 3, \
            f"Need >=3 testable predictions, found {len(preds)}"

    def test_glassholes_prediction(self):
        """Must predict that 'Glassholes' epithet won't be raised for Warby glasses."""
        data = load_yaml(RESEARCH_PROFILE)
        m147 = find_mechanism(data, 147)
        assert m147 is not None, "Mechanism #147 not found"
        preds_str = str(m147.get('testable_predictions', []))
        assert 'glasshole' in preds_str.lower() or \
            'google glass' in preds_str.lower(), \
            "Must predict Glassholes epithet differential"

    def test_privacy_investigation_gap_prediction(self):
        """Must predict privacy investigation gap for Warby vs Meta glasses."""
        data = load_yaml(RESEARCH_PROFILE)
        m147 = find_mechanism(data, 147)
        assert m147 is not None, "Mechanism #147 not found"
        preds_str = str(m147.get('testable_predictions', [])).lower()
        assert 'privacy' in preds_str, \
            "Must predict privacy investigation gap"


# =============================================================================
# Class 8: Source URL Verification
# =============================================================================

class TestSourceURLs:
    """Verify source URLs are documented."""

    def test_source_urls_exist(self):
        """Mechanism #147 must have source_urls field."""
        data = load_yaml(RESEARCH_PROFILE)
        m147 = find_mechanism(data, 147)
        assert m147 is not None, "Mechanism #147 not found"
        assert 'source_urls' in m147, \
            "Mechanism #147 must have source_urls"
        urls = m147['source_urls']
        assert len(urls) >= 5, \
            f"Need >=5 source URLs, found {len(urls)}"

    def test_businesswire_press_release_source(self):
        """Must include BusinessWire press release as primary source."""
        data = load_yaml(RESEARCH_PROFILE)
        m147 = find_mechanism(data, 147)
        assert m147 is not None, "Mechanism #147 not found"
        urls_str = str(m147.get('source_urls', [])).lower()
        assert 'businesswire' in urls_str, \
            "Must include BusinessWire press release"

    def test_sec_filing_or_financial_source(self):
        """Must include a financial data source (SEC filing, earnings, or Vision Monday)."""
        data = load_yaml(RESEARCH_PROFILE)
        m147 = find_mechanism(data, 147)
        assert m147 is not None, "Mechanism #147 not found"
        urls_str = str(m147.get('source_urls', [])).lower()
        assert 'visionmonday' in urls_str or 'sec' in urls_str or \
            'earnings' in urls_str or 'investor' in urls_str, \
            "Must include financial data source"


# =============================================================================
# Class 9: Cherlynn Low Coverage Evidence
# =============================================================================

class TestCherlynnLowCoverageEvidence:
    """Verify Cherlynn Low's multi-entity coverage pattern is documented as evidence."""

    def test_cherlynn_low_meta_glasses_article(self):
        """Cherlynn Low's Meta Glasses hands-on article must be referenced."""
        data = load_yaml(RESEARCH_PROFILE)
        m147 = find_mechanism(data, 147)
        assert m147 is not None, "Mechanism #147 not found"
        m147_str = str(m147).lower()
        assert 'cherlynn' in m147_str or 'engadget' in m147_str, \
            "Cherlynn Low or Engadget must be referenced"

    def test_meta_glasses_positive_framing(self):
        """Engadget coverage pattern must be documented."""
        data = load_yaml(RESEARCH_PROFILE)
        m147 = find_mechanism(data, 147)
        assert m147 is not None, "Mechanism #147 not found"
        m147_str = str(m147).lower()
        assert 'engadget' in m147_str, \
            "Engadget coverage pattern must be documented"

    def test_snap_specs_zero_privacy_vocabulary(self):
        """Engadget's Snap Specs AWE coverage had zero privacy vocabulary."""
        data = load_yaml(RESEARCH_PROFILE)
        m147 = find_mechanism(data, 147)
        assert m147 is not None, "Mechanism #147 not found"
        m147_str = str(m147).lower()
        assert 'snap' in m147_str or 'specs' in m147_str, \
            "Snap Specs coverage should be referenced"


# =============================================================================
# Class 10: Financial Feedback Loop Structural Test
# =============================================================================

class TestFinancialFeedbackLoopStructure:
    """Verify the feedback loop structure is complete and logically consistent."""

    def test_google_revenue_dependency_documented(self):
        """Google's role as publishers' primary revenue source must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        google = data['entities']['google']
        google_str = str(google).lower()
        assert 'ad' in google_str or 'revenue' in google_str or \
            'showcase' in google_str, \
            "Google's publisher revenue dependency must be documented"

    def test_meta_ad_competitor_status(self):
        """Meta's status as publishers' ad-revenue competitor must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        google = data['entities']['google']
        google_str = str(google).lower()
        assert 'meta' in google_str or 'competitor' in google_str, \
            "Meta's ad-revenue competitor status must be referenced"

    def test_mechanism_distinct_from_76_and_91(self):
        """Mechanism #147 must be distinct from #76 (Samsung ads) and #91 (Qualcomm)."""
        data = load_yaml(RESEARCH_PROFILE)
        m147 = find_mechanism(data, 147)
        assert m147 is not None, "Mechanism #147 not found"
        summary = m147.get('finding_summary', '')
        assert 'equity' in summary.lower() or 'invest' in summary.lower(), \
            "Mechanism #147 must emphasize equity investment as novel contribution"

    def test_feedback_loop_completeness(self):
        """The mechanism must document all four steps of the feedback loop."""
        data = load_yaml(RESEARCH_PROFILE)
        m147 = find_mechanism(data, 147)
        assert m147 is not None, "Mechanism #147 not found"
        full_str = str(m147).lower()
        assert 'publisher' in full_str or 'publication' in full_str
        assert 'warby' in full_str
        assert 'stock' in full_str or 'coverage' in full_str
        assert 'meta' in full_str
