"""
Test: Snap Spectacles Dual-AI Partner Publisher Financial Convergence
Mechanism #224: OpenAI + Google Partnerships Create Triple Alignment for September 16 Consumer Launch

Snap Specs ships with AI from BOTH OpenAI and Google, creating triple publisher
financial alignment: (1) Snap commercial interests (ad platform competing with Meta),
(2) OpenAI commercial interests (20+ publisher deals, $300-400M/yr), (3) Google
commercial interests (ad revenue + Showcase + AI content pilots). Meta Ray-Ban glasses
powered by Meta AI only, zero publisher deals. Coverage incentives are perfectly inverted.

Also documents: Snap-Perplexity $400M deal terminated Q1 2026, zero revenue recognized.

Type: Financial Incentive Mapping (Type C)
"""

import unittest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    filepath = os.path.join(PROFILES_DIR, filename)
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)


class TestMechanismExists(unittest.TestCase):
    """Verify mechanism #224 is properly documented."""

    def setUp(self):
        self.research = load_yaml('competitor-coverage-research.yaml')
        self.key = 'snap_specs_dual_ai_partner_publisher_financial_convergence_mechanism_224'
        pubs = self.research.get('publications', {})
        self.mechanism = pubs.get(self.key)

    def test_mechanism_224_exists(self):
        self.assertIsNotNone(self.mechanism, "Mechanism #224 must exist")

    def test_mechanism_id_is_224(self):
        self.assertEqual(self.mechanism['mechanism_id'], 224)

    def test_type_is_financial_incentive_mapping(self):
        self.assertIn('Financial Incentive Mapping', self.mechanism['type'])

    def test_asymmetry_score_documented(self):
        score = self.mechanism.get('asymmetry_score', 0)
        self.assertGreater(score, 0.7, "Asymmetry score should be > 0.7")

    def test_has_source_urls(self):
        urls = self.mechanism.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 5, "Need at least 5 source URLs")

    def test_has_test_file_reference(self):
        self.assertIn('test_file', self.mechanism)

    def test_has_confounding_factors(self):
        factors = self.mechanism.get('confounding_factors', [])
        self.assertGreaterEqual(len(factors), 4, "Need at least 4 confounding factors")


class TestSnapSpecsDualAIPartnership(unittest.TestCase):
    """Verify Snap Specs dual-AI partnership is documented in competitor-entities.yaml."""

    def setUp(self):
        self.entities = load_yaml('competitor-entities.yaml')
        self.snap = self.entities['entities']['snap']
        self.specs = self.snap['hardware_devices']['specs_consumer']

    def test_specs_has_dual_ai_partnership_section(self):
        self.assertIn('dual_ai_partnership', self.specs)

    def test_openai_partnership_documented(self):
        partnership = self.specs['dual_ai_partnership']
        self.assertIn('openai', partnership)

    def test_google_partnership_documented(self):
        partnership = self.specs['dual_ai_partnership']
        self.assertIn('google', partnership)

    def test_publisher_financial_convergence_mechanism_id(self):
        convergence = self.specs['dual_ai_partnership'].get('publisher_financial_convergence', {})
        self.assertEqual(convergence.get('mechanism_id'), 224)

    def test_specs_has_4_cameras(self):
        self.assertEqual(self.specs['cameras']['total'], 4)

    def test_specs_price_2195(self):
        self.assertEqual(self.specs['price_usd'], 2195)

    def test_consumer_launch_september_16(self):
        self.assertEqual(self.specs['consumer_launch_event_date'], '2026-09-16')

    def test_consumer_launch_los_angeles(self):
        self.assertEqual(self.specs['consumer_launch_location'], 'Los Angeles')


class TestPerplexityDealTermination(unittest.TestCase):
    """Verify Snap-Perplexity $400M deal termination is documented."""

    def setUp(self):
        self.entities = load_yaml('competitor-entities.yaml')
        self.snap = self.entities['entities']['snap']
        self.perplexity = self.snap['ai_partnerships']['perplexity']

    def test_deal_status_terminated(self):
        self.assertEqual(self.perplexity['deal_status'], 'TERMINATED')

    def test_termination_date_q1_2026(self):
        self.assertEqual(self.perplexity['termination_date'], 'Q1 2026')

    def test_termination_type_amicable(self):
        self.assertEqual(self.perplexity['termination_type'], 'amicable')

    def test_zero_revenue_recognized(self):
        self.assertEqual(self.perplexity['revenue_recognized'], '$0')

    def test_publisher_chain_broken(self):
        chain_status = self.perplexity.get('perplexity_publisher_chain_status', '')
        self.assertIn('BROKEN', chain_status)

    def test_has_termination_source_urls(self):
        urls = self.perplexity.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 3)


class TestTripleAlignmentVsMetaInversion(unittest.TestCase):
    """Verify the triple alignment for Snap Specs vs zero alignment for Meta glasses."""

    def setUp(self):
        self.entities = load_yaml('competitor-entities.yaml')
        self.snap = self.entities['entities']['snap']
        self.openai = self.entities['entities']['openai']

    def test_openai_has_20_plus_publisher_deals(self):
        deals = self.openai['publisher_content_deal_portfolio']
        total_deals = deals.get('total_deals', '0')
        # "20+" as string
        self.assertIn('20', str(total_deals))

    def test_openai_deals_300_400m_annual(self):
        deals = self.openai['publisher_content_deal_portfolio']
        value = deals.get('estimated_total_annual_value_m', '')
        self.assertIn('300', str(value))

    def test_snap_q2_revenue_1_6b(self):
        q2 = self.snap['q2_2026_earnings']
        self.assertEqual(q2['total_revenue_b'], 1.6)

    def test_snap_revenue_growth_19_pct(self):
        q2 = self.snap['q2_2026_earnings']
        self.assertEqual(q2['revenue_yoy_pct'], 19)

    def test_snap_meta_contrast_updated(self):
        relationships = self.snap['publisher_financial_relationships']
        contrast = relationships.get('meta_contrast', '')
        self.assertIn('DISSOLVED', contrast)

    def test_snap_meta_contrast_mentions_dual_ai(self):
        relationships = self.snap['publisher_financial_relationships']
        contrast = relationships.get('meta_contrast', '')
        self.assertIn('OpenAI', contrast)
        self.assertIn('Google', contrast)


class TestSnapQ2FinancialData(unittest.TestCase):
    """Verify Q2 2026 financial data accuracy."""

    def setUp(self):
        self.entities = load_yaml('competitor-entities.yaml')
        self.snap = self.entities['entities']['snap']
        self.q2 = self.snap['q2_2026_earnings']

    def test_q2_revenue_1599m(self):
        self.assertEqual(self.q2['total_revenue_m'], 1599)

    def test_adjusted_ebitda_249_6m(self):
        self.assertEqual(self.q2['adjusted_ebitda_m'], 249.6)

    def test_ebitda_yoy_505_pct(self):
        self.assertEqual(self.q2['adjusted_ebitda_yoy_pct'], 505)

    def test_free_cash_flow_120_5m(self):
        self.assertEqual(self.q2['free_cash_flow_m'], 120.5)

    def test_mau_971m(self):
        self.assertEqual(self.q2['mau_m'], 971)

    def test_dau_493m(self):
        self.assertEqual(self.q2['dau_m'], 493)

    def test_specs_launch_september_16_confirmed(self):
        specs_text = self.q2.get('spectacles_launch_confirmed', '')
        self.assertIn('September 16', specs_text)


class TestCoverageEvidencePreLaunch(unittest.TestCase):
    """Verify pre-launch coverage evidence for Snap Specs September 16 event."""

    def setUp(self):
        self.research = load_yaml('competitor-coverage-research.yaml')
        pubs = self.research.get('publications', {})
        self.mechanism = pubs.get(
            'snap_specs_dual_ai_partner_publisher_financial_convergence_mechanism_224'
        )

    def test_detail_mentions_openai(self):
        detail = self.mechanism.get('detail', '')
        self.assertIn('OpenAI', detail)

    def test_detail_mentions_google(self):
        detail = self.mechanism.get('detail', '')
        self.assertIn('Google', detail)

    def test_detail_mentions_triple_alignment(self):
        detail = self.mechanism.get('detail', '')
        self.assertIn('TRIPLE', detail)

    def test_detail_mentions_september_16(self):
        detail = self.mechanism.get('detail', '')
        self.assertIn('September 16', detail)

    def test_detail_mentions_perplexity_dissolution(self):
        detail = self.mechanism.get('detail', '')
        self.assertIn('DISSOLVED', detail)

    def test_detail_mentions_meta_zero_deals(self):
        detail = self.mechanism.get('detail', '')
        self.assertIn('ZERO', detail)

    def test_detail_mentions_inverted(self):
        detail = self.mechanism.get('detail', '')
        self.assertIn('INVERTED', detail)

    def test_engadget_source_confirms_dual_ai(self):
        urls = self.mechanism.get('source_urls', [])
        engadget_urls = [u for u in urls if 'engadget' in u]
        self.assertGreater(len(engadget_urls), 0, "Engadget source confirming dual AI partnership required")


class TestMechanism224Exists(unittest.TestCase):
    """Verify mechanism #224 exists in the research corpus."""

    def setUp(self):
        self.research = load_yaml('competitor-coverage-research.yaml')

    def test_mechanism_224_exists(self):
        max_id = 0
        pubs = self.research.get('publications', {})
        for key, value in pubs.items():
            if isinstance(value, dict) and 'mechanism_id' in value:
                mid = value['mechanism_id']
                if isinstance(mid, int) and mid > max_id:
                    max_id = mid
        self.assertGreaterEqual(max_id, 224, "Mechanism #224 should exist in corpus")


if __name__ == '__main__':
    unittest.main()
