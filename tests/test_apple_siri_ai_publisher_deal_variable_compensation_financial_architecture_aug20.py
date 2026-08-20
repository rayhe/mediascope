"""
Mechanism #196: Apple Siri AI Variable-Compensation Publisher Financial Architecture
(Extending mechanism #156 with structural analysis)

Type: Financial Incentive Mapping — Apple × Publishers × Siri AI
Discovery Date: 2026-08-20
Iteration: #200

CORE DISCOVERY: Apple's per-use model creates ONGOING dependency

Apple's Siri AI publisher deal proposal (WSJ, Aug 12, 2026) uses VARIABLE
PER-USE compensation — structurally distinct from every other AI-publisher
financial arrangement. OpenAI, Google, Amazon, and Microsoft all use fixed-fee
models where publishers receive guaranteed payments regardless of usage.
Apple's model ties publisher revenue DIRECTLY to Siri AI usage volume,
creating an ongoing dependency where publishers benefit from Apple product
success (more Siri users = more per-use payments).

This structural distinction has direct implications for Apple N50 smart glasses
coverage: publishers with Siri AI deals have three incentive channels to
produce favorable Apple glasses coverage and adversarial Meta glasses coverage.

COMPANION UPDATE: Anthropic revenue trajectory updated to $65B ARR (Jul 2026,
Reuters Aug 17), projected $190-200B by 2028. Pre-IPO credit facility >$10B.
Decart AI acquisition talks ($6B).

SOURCES:
- https://www.macrumors.com/2026/08/12/apple-siri-ai-publisher-talks/
- https://www.thewrap.com/industry-news/tech/apple-ai-siri-news-media-publishing-deals/
- https://www.editorandpublisher.com/stories/untitled,263027
- https://9to5mac.com/2026/08/12/report-apple-seeks-publisher-deals-to-give-siri-ai-better-access-to-current-events/
- https://www.reuters.com/technology/anthropic-revenue-run-rate-tops-65-billion-source-says-2026-08-17/
- https://www.reuters.com/legal/transactional/anthropics-pre-ipo-credit-facility-set-exceed-10-billion-bloomberg-news-reports-2026-08-18/
- https://www.reuters.com/technology/anthropic-talks-buy-decart-ai-source-says-2026-08-13/

Cross-references: #43, #80, #117, #156, #194
"""

import unittest
import yaml
import os


def load_competitor_entities():
    """Load competitor entities YAML."""
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'competitor-entities.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


class TestAppleSiriAIDealStructuralDistinction(unittest.TestCase):
    """Verify the variable-compensation structural analysis is documented."""

    def setUp(self):
        self.entities = load_competitor_entities()
        self.apple = self.entities['entities']['apple']
        self.deals = self.apple.get('siri_ai_publisher_deals', {})

    def test_siri_ai_deals_section_exists(self):
        self.assertIn('siri_ai_publisher_deals', self.apple)

    def test_structural_distinction_section(self):
        self.assertIn('structural_distinction', self.deals)

    def test_fixed_fee_comparison_documents_openai(self):
        distinction = self.deals['structural_distinction']
        self.assertIn('openai', distinction['fixed_fee_comparison'].lower())

    def test_fixed_fee_comparison_documents_google(self):
        distinction = self.deals['structural_distinction']
        self.assertIn('google', distinction['fixed_fee_comparison'].lower())

    def test_ongoing_dependency_mechanism_described(self):
        distinction = self.deals['structural_distinction']
        self.assertIn('ongoing_dependency', distinction)
        self.assertIn('siri', distinction['ongoing_dependency'].lower())

    def test_algorithm_control_risk_documented(self):
        distinction = self.deals['structural_distinction']
        self.assertIn('algorithm_control', distinction)
        self.assertIn('ranking', distinction['algorithm_control'].lower())


class TestDealArchitectureBasics(unittest.TestCase):
    """Verify basic deal architecture facts are documented."""

    def setUp(self):
        self.entities = load_competitor_entities()
        self.apple = self.entities['entities']['apple']
        self.deals = self.apple.get('siri_ai_publisher_deals', {})

    def test_report_date(self):
        self.assertEqual(self.deals['report_date'], '2026-08-12')

    def test_budget_magnitude(self):
        self.assertEqual(self.deals['budget_magnitude'], 'nine_figure')

    def test_compensation_model_variable(self):
        self.assertIn('variable', self.deals['compensation_model'])

    def test_deal_duration_multiyear(self):
        self.assertEqual(self.deals['deal_duration'], 'multiyear')

    def test_mechanism_id(self):
        self.assertEqual(self.deals['mechanism_id'], 156)


class TestBypassReversalTimeline(unittest.TestCase):
    """Verify the bypass → reversal timeline is documented."""

    def setUp(self):
        self.entities = load_competitor_entities()
        self.apple = self.entities['entities']['apple']
        self.deals = self.apple.get('siri_ai_publisher_deals', {})

    def test_reversal_timeline_exists(self):
        self.assertIn('reversal_timeline', self.deals)

    def test_phase_1_fixed_fee_failure(self):
        timeline = self.deals['reversal_timeline']
        self.assertIn('phase_1_approach', timeline)

    def test_phase_2_gemini_bypass(self):
        timeline = self.deals['reversal_timeline']
        self.assertIn('phase_2_bypass', timeline)

    def test_phase_3_siri_ai_return(self):
        timeline = self.deals['reversal_timeline']
        self.assertIn('phase_3_return', timeline)

    def test_hallucination_driver(self):
        self.assertIn('hallucination_motivator', self.deals)


class TestConfounderDocumentation(unittest.TestCase):
    """Verify confounders are documented for scholarly rigor."""

    def setUp(self):
        self.entities = load_competitor_entities()
        self.apple = self.entities['entities']['apple']
        self.deals = self.apple.get('siri_ai_publisher_deals', {})

    def test_confounders_exist(self):
        self.assertIn('confounders', self.deals)

    def test_at_least_five_confounders(self):
        self.assertGreaterEqual(len(self.deals['confounders']), 5)

    def test_strong_confounders_present(self):
        confounders = self.deals['confounders']
        strong = [c for c in confounders if c.get('strength') == 'STRONG']
        self.assertGreaterEqual(len(strong), 2)

    def test_no_deals_signed_confounder(self):
        confounders = self.deals['confounders']
        negotiation_confounder = [c for c in confounders
                                  if 'negotiation' in str(c.get('description', '')).lower()
                                  or 'signed' in str(c.get('description', '')).lower()]
        self.assertGreater(len(negotiation_confounder), 0)

    def test_variable_lower_payments_confounder(self):
        confounders = self.deals['confounders']
        lower_pay = [c for c in confounders
                     if 'lower' in str(c.get('description', '')).lower()
                     or 'weaker' in str(c.get('description', '')).lower()]
        self.assertGreater(len(lower_pay), 0)


class TestCondeNastImplication(unittest.TestCase):
    """Verify Condé Nast-specific implications are documented."""

    def setUp(self):
        self.entities = load_competitor_entities()
        self.apple = self.entities['entities']['apple']
        self.deals = self.apple.get('siri_ai_publisher_deals', {})

    def test_conde_nast_implication_exists(self):
        self.assertIn('conde_nast_implication', self.deals)

    def test_simultaneous_deals_documented(self):
        cn = self.deals['conde_nast_implication']
        self.assertIn('simultaneous_deals', cn)
        self.assertIn('openai', cn['simultaneous_deals'].lower())

    def test_existing_news_plus_noted(self):
        cn = self.deals['conde_nast_implication']
        self.assertIn('existing_relationship', cn)
        self.assertIn('news+', cn['existing_relationship'].lower())

    def test_meta_zero_deal_in_contrast(self):
        cn = self.deals['conde_nast_implication']
        self.assertIn('meta', cn['simultaneous_deals'].lower())


class TestMetaContrast(unittest.TestCase):
    """Verify Meta contrast is documented."""

    def setUp(self):
        self.entities = load_competitor_entities()
        self.apple = self.entities['entities']['apple']
        self.deals = self.apple.get('siri_ai_publisher_deals', {})

    def test_meta_contrast_exists(self):
        self.assertIn('meta_contrast', self.deals)

    def test_meta_zero_deals_noted(self):
        self.assertIn('zero', self.deals['meta_contrast'].lower())


class TestN50CoverageImplication(unittest.TestCase):
    """Verify N50 wearables coverage implications."""

    def setUp(self):
        self.entities = load_competitor_entities()
        self.apple = self.entities['entities']['apple']
        self.deals = self.apple.get('siri_ai_publisher_deals', {})

    def test_n50_implication_exists(self):
        self.assertIn('n50_coverage_implication', self.deals)

    def test_three_incentive_channels(self):
        channels = self.deals['n50_coverage_implication']['incentive_channels']
        self.assertGreaterEqual(len(channels), 3)

    def test_privacy_channel_present(self):
        channels = self.deals['n50_coverage_implication']['incentive_channels']
        privacy = [c for c in channels if 'privacy' in str(c).lower()]
        self.assertGreater(len(privacy), 0)

    def test_competitive_displacement_channel(self):
        channels = self.deals['n50_coverage_implication']['incentive_channels']
        competitive = [c for c in channels if 'meta' in str(c.get('description', '')).lower()]
        self.assertGreater(len(competitive), 0)


class TestCrossReferences(unittest.TestCase):
    """Verify mechanism cross-references."""

    def setUp(self):
        self.entities = load_competitor_entities()
        self.apple = self.entities['entities']['apple']
        self.deals = self.apple.get('siri_ai_publisher_deals', {})

    def test_cross_references_exist(self):
        self.assertIn('cross_references', self.deals)

    def test_minimum_cross_references(self):
        self.assertGreaterEqual(len(self.deals['cross_references']), 3)

    def test_mechanism_43_referenced(self):
        ids = [r.get('mechanism_id') for r in self.deals['cross_references']]
        self.assertIn(43, ids)

    def test_mechanism_80_referenced(self):
        ids = [r.get('mechanism_id') for r in self.deals['cross_references']]
        self.assertIn(80, ids)

    def test_mechanism_117_referenced(self):
        ids = [r.get('mechanism_id') for r in self.deals['cross_references']]
        self.assertIn(117, ids)


class TestSourceDocumentation(unittest.TestCase):
    """Verify source URLs are documented."""

    def setUp(self):
        self.entities = load_competitor_entities()
        self.apple = self.entities['entities']['apple']
        self.deals = self.apple.get('siri_ai_publisher_deals', {})

    def test_source_urls_exist(self):
        self.assertIn('source_urls', self.deals)

    def test_minimum_sources(self):
        self.assertGreaterEqual(len(self.deals['source_urls']), 4)

    def test_wsj_primary_source(self):
        urls = self.deals['source_urls']
        wsj = [u for u in urls if 'wsj' in u]
        self.assertGreater(len(wsj), 0)

    def test_macrumors_secondary_source(self):
        urls = self.deals['source_urls']
        mac = [u for u in urls if 'macrumors' in u]
        self.assertGreater(len(mac), 0)


class TestAnthropicRevenueUpdate(unittest.TestCase):
    """Verify Anthropic revenue figures updated to Jul 2026."""

    def setUp(self):
        self.entities = load_competitor_entities()
        self.anthropic = self.entities['entities']['anthropic']

    def test_arr_jul_2026_documented(self):
        self.assertIn('arr_jul_2026_b', self.anthropic.get('ipo_filing', {}))

    def test_arr_jul_2026_value(self):
        self.assertGreaterEqual(self.anthropic['ipo_filing']['arr_jul_2026_b'], 65)

    def test_projected_revenue_2028(self):
        self.assertIn('projected_revenue_2028_b', self.anthropic.get('ipo_filing', {}))

    def test_pre_ipo_credit_facility(self):
        self.assertIn('pre_ipo_credit_facility_b', self.anthropic.get('ipo_filing', {}))
        self.assertGreaterEqual(self.anthropic['ipo_filing']['pre_ipo_credit_facility_b'], 10)

    def test_decart_acquisition(self):
        self.assertIn('decart_acquisition', self.anthropic.get('ipo_filing', {}))

    def test_revenue_trajectory_note_updated(self):
        note = self.anthropic['ipo_filing'].get('revenue_trajectory_note', '')
        self.assertIn('65B', note)


if __name__ == '__main__':
    unittest.main()
