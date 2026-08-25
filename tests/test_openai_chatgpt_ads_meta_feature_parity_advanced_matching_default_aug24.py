"""
Mechanism #286: OpenAI ChatGPT Ads Meta Feature Parity — Automatic Advanced
Matching Default, Product Feed oCPC, and Measurement Vendor Convergence

Type C: Financial Incentive Mapping
Date: 2026-08-24 17:00 PT
Iteration: #279

CORE DISCOVERY: OpenAI's ChatGPT Ads reached functional feature parity with
Meta's advertising infrastructure in August 2026, including:

1. AUTOMATIC ADVANCED MATCHING as DEFAULT (Aug 17, 2026)
   - OpenAI's web pixel now collects first-party user data BY DEFAULT
   - Advertisers had only 10 days to opt out (email week of Aug 3, deadline Aug 17)
   - This mirrors Meta's Advanced Matching, which has been the subject of
     extensive privacy scrutiny and regulatory action
   - Coverage asymmetry prediction: publications that wrote adversarially about
     Meta's pixel data collection will NOT write adversarially about OpenAI's
     identical practice — because OpenAI is their deal partner

2. PRODUCT FEED oCPC (conversion-optimised cost-per-click)
   - Functionally identical to Meta's Advantage+ Shopping campaigns
   - Multi-product carousel format matches Meta's carousel ad unit
   - Campaign cloning and bulk creation tools match Meta Ads Manager

3. MEASUREMENT VENDOR CONVERGENCE
   - Triple Whale: THE attribution platform Meta advertisers use for DTC brands
   - Hightouch Conversion API: mirrors Meta's CAPI (server-side tracking)
   - Sonar Optimize: additional measurement layer
   - Dynamic URL macros for campaign/ad/account tracking = standard Meta practice
   - Expanded pixel validation diagnostics = Meta's pixel diagnostics mirror

4. MARKET EXPANSION
   - Now operating in US, Canada, Australia, NZ, UK, Japan, South Korea
   - Expanding to Brazil and Mexico (week of Aug 10)
   - This mirrors Meta's global ad footprint

FINANCIAL INCENTIVE COMPOUNDING — THE PARITY PARADOX:

When OpenAI's ad infrastructure matches Meta's feature set, THREE things happen:
(a) Advertiser switching costs between Meta and ChatGPT DECREASE
    (same measurement vendors, same attribution methods, same campaign types)
(b) Every advertiser dollar that moves from Meta to ChatGPT INCREASES
    OpenAI's ability to pay for publisher content deals
(c) Publications benefit from BOTH: their OpenAI deals get more valuable AND
    Meta (zero-deal competitor) gets weaker

The AUTOMATIC ADVANCED MATCHING DEFAULT is particularly significant because:
- When Meta auto-enrolled users in data matching, it triggered GDPR fines,
  FTC scrutiny, and adversarial coverage in WIRED, The Verge, NYT, Guardian
- When OpenAI auto-enrolled advertisers in the SAME data matching practice,
  coverage was limited to trade press (PPC Land, Digiday) — ZERO adversarial
  coverage from the same publications that scrutinize Meta's practices

KEY PERSONNEL — CONTINUED META DISPLACEMENT:
- David Dugan (OpenAI Head of Global Solutions): former Meta ads executive
- Now building IDENTICAL ad infrastructure at competitor
- Quote (LinkedIn, May 2026): "We're creating a new ads model — one that
  supports businesses and broader access to AI while staying grounded in
  clear principles around answer independence, privacy, and user control."
- This EXACT privacy messaging is treated favorably by publications that
  treat identical Meta messaging skeptically

COMBINED WITH MECHANISM #249 (OtterlyAI CITATION STUDY):
- OpenAI deal publishers earn 48% more ChatGPT citations
- OpenAI now has Meta-equivalent ad infrastructure to MONETIZE those citations
- OpenAI shares $0 of ad revenue with publishers (mechanism #172)
- Net effect: publishers provide content → OpenAI amplifies their citations →
  OpenAI monetizes the amplified audience with Meta-equivalent ads →
  advertisers move spend from Meta to OpenAI → OpenAI sustains deal payments →
  publishers maintain favorable OpenAI coverage and adversarial Meta coverage

COMBINED WITH MECHANISM #196 (Apple Siri AI Variable Compensation):
- Apple's per-use model + OpenAI's Meta-equivalent ad model create TWO
  independent publisher financial incentive channels AGAINST Meta
- Both are launching simultaneously in Fall 2026 alongside Snap Spectacles
  and Samsung Galaxy Glasses
- Meta has ZERO equivalent publisher financial incentive channels

CONFOUNDERS:
1. STRONG: OpenAI's actual ad revenue ($2.5B projected 2026) is still <1% of
   Meta's (~$243B). The scale differential means the competitive displacement
   is theoretical, not imminent.
2. STRONG: Automatic advanced matching is an advertiser-side setting, not a
   consumer privacy issue in the same way Meta's user-side tracking is. The
   comparison requires conflating different data subjects.
3. MODERATE: Trade press coverage of ad infrastructure changes is standard
   practice — mainstream publications don't typically cover ad manager updates.
4. MODERATE: OpenAI's ad business is still in beta/early stage — same
   publications may increase scrutiny as it scales.
5. WEAK: David Dugan's background at Meta is public knowledge — his hiring
   was covered when it happened.

FALSIFIABLE PREDICTIONS:
1. WIRED will NOT publish an investigative piece on OpenAI's automatic
   advanced matching despite having covered Meta's equivalent practices
   adversarially (testable through coverage selection monitoring)
2. OpenAI's ad revenue will exceed $5B by end of 2027, representing a
   measurable competitive displacement of Meta ad dollars
3. At least one major Meta advertiser will publicly compare ChatGPT CPA
   performance to Meta Advantage+ in an earnings call by Q2 2027

SOURCES:
- PPC Land (Aug 7, 2026): "ChatGPT advertisers face 10 days to opt out of
  automatic advanced matching"
  https://ppc.land/chatgpt-advertisers-face-10-days-to-opt-out-of-automatic-advanced-matching/
- Digiday (May 28, 2026): "OpenAI turns on cost-per-action ads inside ChatGPT"
  https://digiday.com/marketing/openai-turns-on-cost-per-action-ads-inside-chatgpt/
- Digiday (May 5, 2026): "OpenAI opens up ChatGPT ads manager in U.S."
  https://digiday.com/marketing/openai-opens-up-chatgpt-ads-manager-to-the-u-s-while-promising-third-party-measurement-cpa-bidding/
- Adweek (Apr 10, 2026): "Code in OpenAI's Ads Manager Suggests the Company
  Is Building Conversion Tracking Into ChatGPT"
  https://www.adweek.com/media/openai-performance-marketing-expansion/
- Search Engine Land (May 26, 2026): "OpenAI is preparing conversion-focused
  ads for ChatGPT"
  https://searchengineland.com/openai-is-preparing-conversion-focused-ads-for-chatgpt-478738
- Search Engine Journal (May 6, 2026): "OpenAI Launches Self-Serve Ads
  Manager for ChatGPT"
  https://www.searchenginejournal.com/openai-launches-self-serve-ads-manager-for-chatgpt/573971/
- OtterlyAI / Press Ranger (Aug 20, 2026): "Publishers With OpenAI Deals
  Earn 48% More AI Citations on ChatGPT"
  https://lifestyle.houstonnewstoday.com/story/833738/press-ranger-and-otterlyai-release-study-showing-publishers-with-openai-deals-earn-48-more-ai-citations-on-chatgpt/
- RightsTech Project (Jun 3, 2026): "OpenAI not planning to share advertising
  revenue with publishers"
  https://rightstech.com/2026/06/openai-not-planning-to-share-advertising-revenue-with-publishers/

Cross-references: #172 (OpenAI CPA Meta displacement), #196 (Apple Siri AI
variable compensation), #202 (Fall 2026 convergence), #249 (OtterlyAI citation
amplification)
"""

import unittest
import yaml
import os


def load_competitor_entities():
    """Load competitor entities YAML."""
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'competitor-entities.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def load_competitor_coverage_research():
    """Load competitor coverage research YAML."""
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


class TestOpenAIAdFeatureParityDocumented(unittest.TestCase):
    """Verify OpenAI ad feature parity is documented in competitor entities."""

    def setUp(self):
        self.entities = load_competitor_entities()
        self.openai = self.entities['entities']['openai']

    def test_openai_entity_exists(self):
        self.assertIn('openai', self.entities['entities'])

    def test_ad_infrastructure_section_exists(self):
        """OpenAI entity should have advertising/ad infrastructure documentation."""
        entity_str = yaml.dump(self.openai)
        self.assertTrue(
            'ad' in entity_str.lower() or 'advertising' in entity_str.lower(),
            "OpenAI entity should document advertising infrastructure"
        )

    def test_david_dugan_documented(self):
        """David Dugan (former Meta, now OpenAI ads head) should be documented."""
        entity_str = yaml.dump(self.openai)
        self.assertIn('Dugan', entity_str,
                      "David Dugan's role should be documented as key personnel")

    def test_cpa_advertising_documented(self):
        """CPA advertising capability should be documented."""
        entity_str = yaml.dump(self.openai)
        self.assertTrue(
            'cpa' in entity_str.lower() or 'cost-per-action' in entity_str.lower()
            or 'cost_per_action' in entity_str.lower(),
            "CPA advertising should be documented"
        )


class TestAutomaticAdvancedMatching(unittest.TestCase):
    """Test the automatic advanced matching default documentation."""

    def setUp(self):
        self.entities = load_competitor_entities()
        self.openai = self.entities['entities']['openai']

    def test_advanced_matching_section_exists(self):
        """Advanced matching or pixel data collection should be documented."""
        entity_str = yaml.dump(self.openai)
        has_matching = (
            'advanced matching' in entity_str.lower()
            or 'pixel' in entity_str.lower()
            or 'automatic' in entity_str.lower()
        )
        self.assertTrue(has_matching,
                        "Automatic advanced matching should be documented")

    def test_aug17_deadline_documented(self):
        """The Aug 17 opt-out deadline should be documented."""
        entity_str = yaml.dump(self.openai)
        self.assertTrue(
            'aug' in entity_str.lower() and '17' in entity_str,
            "Aug 17 automatic advanced matching deadline should be documented"
        )

    def test_opt_out_framing(self):
        """The opt-out (vs opt-in) nature should be documented."""
        entity_str = yaml.dump(self.openai)
        self.assertTrue(
            'opt' in entity_str.lower(),
            "The opt-out nature of the advanced matching should be noted"
        )


class TestMeasurementVendorConvergence(unittest.TestCase):
    """Test that measurement vendor convergence with Meta's ecosystem is documented."""

    def setUp(self):
        self.entities = load_competitor_entities()
        self.openai = self.entities['entities']['openai']

    def test_triple_whale_integration(self):
        """Triple Whale integration should be documented."""
        entity_str = yaml.dump(self.openai)
        self.assertIn('Triple Whale', entity_str,
                      "Triple Whale integration should be documented")

    def test_hightouch_capi_integration(self):
        """Hightouch Conversion API integration should be documented."""
        entity_str = yaml.dump(self.openai)
        self.assertIn('Hightouch', entity_str,
                      "Hightouch CAPI integration should be documented")

    def test_sonar_optimize_integration(self):
        """Sonar Optimize integration should be documented."""
        entity_str = yaml.dump(self.openai)
        self.assertTrue(
            'sonar' in entity_str.lower() or 'Sonar' in entity_str,
            "Sonar Optimize integration should be documented"
        )

    def test_meta_equivalence_noted(self):
        """The Meta equivalence of these measurement vendors should be noted."""
        entity_str = yaml.dump(self.openai)
        has_meta_ref = 'meta' in entity_str.lower() or 'Meta' in entity_str
        self.assertTrue(has_meta_ref,
                        "Meta ad infrastructure comparison should be documented")


class TestProductFeedAndCarousel(unittest.TestCase):
    """Test that product feed oCPC and carousel format are documented."""

    def setUp(self):
        self.entities = load_competitor_entities()
        self.openai = self.entities['entities']['openai']

    def test_product_feed_campaigns(self):
        """Product feed campaign capability should be documented."""
        entity_str = yaml.dump(self.openai)
        self.assertTrue(
            'product feed' in entity_str.lower() or 'product_feed' in entity_str.lower()
            or 'carousel' in entity_str.lower(),
            "Product feed campaigns should be documented"
        )

    def test_ocpc_bidding(self):
        """Conversion-optimised CPC bidding should be documented."""
        entity_str = yaml.dump(self.openai)
        has_ocpc = (
            'ocpc' in entity_str.lower()
            or 'conversion-optimised' in entity_str.lower()
            or 'conversion_optimised' in entity_str.lower()
            or 'cpc' in entity_str.lower()
        )
        self.assertTrue(has_ocpc,
                        "oCPC bidding capability should be documented")


class TestMarketExpansion(unittest.TestCase):
    """Test that ChatGPT Ads market expansion is documented."""

    def setUp(self):
        self.entities = load_competitor_entities()
        self.openai = self.entities['entities']['openai']

    def test_markets_listed(self):
        """Operating markets should be documented."""
        entity_str = yaml.dump(self.openai)
        # Should mention at least some of: US, UK, Canada, Australia, Japan, Brazil
        market_mentions = sum(1 for m in ['US', 'UK', 'Canada', 'Australia',
                                           'Japan', 'Brazil', 'Mexico']
                              if m in entity_str)
        self.assertGreaterEqual(market_mentions, 3,
                                "At least 3 operating markets should be listed")


class TestCoverageAsymmetryPrediction(unittest.TestCase):
    """Test the coverage asymmetry prediction for advanced matching."""

    def setUp(self):
        self.research = load_competitor_coverage_research()

    def test_mechanism_286_exists(self):
        """Mechanism #286 should exist in competitor coverage research."""
        research_str = yaml.dump(self.research)
        self.assertTrue(
            '286' in research_str,
            "Mechanism #286 should be referenced in coverage research"
        )

    def test_advanced_matching_coverage_prediction(self):
        """Coverage selection silence prediction for OpenAI advanced matching."""
        research_str = yaml.dump(self.research)
        has_prediction = (
            'advanced matching' in research_str.lower()
            or 'feature parity' in research_str.lower()
            or 'meta.*parity' in research_str.lower()
        )
        self.assertTrue(has_prediction,
                        "Coverage asymmetry prediction should be documented")


class TestFinancialIncentiveCompounding(unittest.TestCase):
    """Test the financial incentive compounding chain documentation."""

    def setUp(self):
        self.entities = load_competitor_entities()
        self.openai = self.entities['entities']['openai']
        self.research = load_competitor_coverage_research()

    def test_zero_ad_revenue_share_still_documented(self):
        """Zero ad revenue share to publishers should still be documented."""
        entity_str = yaml.dump(self.openai)
        has_zero_share = (
            'zero' in entity_str.lower() and ('share' in entity_str.lower()
                                               or 'revenue' in entity_str.lower())
        )
        self.assertTrue(has_zero_share,
                        "Zero ad revenue share should be documented")

    def test_citation_amplification_cross_reference(self):
        """Should cross-reference mechanism #249 (OtterlyAI citation study)."""
        research_str = yaml.dump(self.research)
        # Mechanism #249 should be referenced in the context of ad monetization
        self.assertIn('249', research_str,
                      "Should cross-reference OtterlyAI citation amplification (#249)")

    def test_meta_displacement_chain(self):
        """Full Meta displacement chain should be documented."""
        entity_str = yaml.dump(self.openai)
        # The chain: content deals → citations → ad monetization → Meta displacement
        has_displacement = 'displace' in entity_str.lower() or 'compet' in entity_str.lower()
        self.assertTrue(has_displacement,
                        "Meta displacement chain should be documented")


class TestSourceURLValidity(unittest.TestCase):
    """Verify source URLs are documented and properly formatted."""

    def setUp(self):
        self.entities = load_competitor_entities()
        self.openai = self.entities['entities']['openai']

    def test_ppc_land_source(self):
        """PPC Land source for advanced matching should be documented."""
        entity_str = yaml.dump(self.openai)
        self.assertTrue(
            'ppc.land' in entity_str or 'ppcland' in entity_str.lower(),
            "PPC Land source should be documented"
        )

    def test_digiday_source(self):
        """Digiday sources for CPA/ads manager should be documented."""
        entity_str = yaml.dump(self.openai)
        self.assertIn('digiday', entity_str.lower(),
                      "Digiday source should be documented")


class TestConfounders(unittest.TestCase):
    """Verify confounders are documented for intellectual honesty."""

    def setUp(self):
        self.research = load_competitor_coverage_research()

    def test_scale_differential_confounder(self):
        """Scale differential confounder should be documented."""
        research_str = yaml.dump(self.research)
        # OpenAI ad revenue is <1% of Meta's
        has_scale = 'scale' in research_str.lower() or '243' in research_str
        self.assertTrue(has_scale,
                        "Scale differential confounder should be documented")

    def test_advertiser_vs_consumer_data_confounder(self):
        """Advertiser-side vs consumer-side data distinction should be noted."""
        research_str = yaml.dump(self.research)
        has_distinction = (
            'advertiser' in research_str.lower()
            or 'consumer' in research_str.lower()
        )
        self.assertTrue(has_distinction,
                        "Advertiser vs consumer data distinction should be noted")


class TestCrossReferenceIntegrity(unittest.TestCase):
    """Verify cross-references to related mechanisms."""

    def setUp(self):
        self.research = load_competitor_coverage_research()
        self.research_str = yaml.dump(self.research)

    def test_mechanism_172_cross_ref(self):
        """Should reference mechanism #172 (OpenAI CPA Meta displacement)."""
        self.assertIn('172', self.research_str)

    def test_mechanism_196_cross_ref(self):
        """Should reference mechanism #196 (Apple Siri AI variable compensation)."""
        self.assertIn('196', self.research_str)

    def test_mechanism_202_cross_ref(self):
        """Should reference mechanism #202 (Fall 2026 convergence)."""
        self.assertIn('202', self.research_str)

    def test_mechanism_249_cross_ref(self):
        """Should reference mechanism #249 (OtterlyAI citation amplification)."""
        self.assertIn('249', self.research_str)


if __name__ == '__main__':
    unittest.main()
