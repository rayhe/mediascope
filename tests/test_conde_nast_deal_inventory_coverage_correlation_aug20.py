"""
Mechanism #199: Condé Nast Deal Inventory Coverage Correlation

Type: Financial Incentive Mapping — Condé Nast × 7 AI Platform Companies
Discovery Date: 2026-08-20
Iteration: #205

CORE DISCOVERY: Condé Nast (WIRED's parent) has financial relationships with 5
of 7 major AI platform companies: OpenAI (active deal), Amazon/Rufus (active),
Microsoft/PCM (active), Perplexity (post-C&D, active), and Apple (negotiating
Siri AI variable-compensation deal, Aug 2026). It has ZERO deals with Meta and
an ADVERSARIAL posture toward Google (CEO Lynch: "death blow," "pernicious").

Coverage adversarialism inversely correlates with deal status:
- Meta (0 deals): most adversarial coverage
- Google (0 AI deal, but ad revenue dependency): critical but modulated
- OpenAI (active deal): soft — aspirational framing, privacy minimized
- Apple (negotiating): soft-to-neutral — privacy hero framing
- Amazon (active deal): neutral-to-soft
- Anthropic (0 deals anywhere): softest — but driven by "safety" brand, not deals

FRENCH APIG COMPLAINT (Aug 14, 2026): French press association APIG asked
competition authority to intervene over Google's AI Overviews, arguing Google
uses publisher content without payment. SAME authority ordered META to submit
payment proposal in Jul 2026 — Meta enforced FIRST despite Google causing 33-38%
traffic decline via AI Overviews. Regulatory sequence mirrors coverage asymmetry.

ANTHROPIC ZERO-DEAL CONFIRMATION (Press Gazette, Aug 2026): "While OpenAI
typically signs one AI licensing deal with a major publisher in each country,
Anthropic has not signed any licensing deals." Zero deals + $65B ARR + $1.5B
copyright settlement (scraped without permission) = softest coverage. Financial
relationships are necessary but not sufficient predictor.

SOURCES:
- https://pressgazette.co.uk/news/google-ai-deals-uk-publishers/
- https://www.medianama.com/2026/08/223-french-publishers-google-pay-ai-summaries/
- https://www.wsj.com/business/media/apple-in-talks-to-pay-publishers-to-improve-ai-powered-siri-0641f64b
- https://ppc.land/conde-nast-ceo-calls-google-ai-a-death-blow-as-search-traffic-collapses/
- https://www.condenast.com/news/conde-nast-and-openai-announce-partnership

Cross-references: #8, #33, #43, #136, #156, #196, #197, #198
"""

import unittest
import yaml
import os


def load_wired_profile():
    """Load WIRED publication profile."""
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'wired.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def load_competitor_entities():
    """Load competitor entities YAML."""
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'competitor-entities.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


class TestCondeNastDealInventoryExists(unittest.TestCase):
    """Verify the deal inventory correlation section exists in WIRED profile."""

    def setUp(self):
        self.profile = load_wired_profile()
        self.correlation = self.profile.get('conde_nast_deal_inventory_coverage_correlation', {})

    def test_correlation_section_exists(self):
        self.assertIn('conde_nast_deal_inventory_coverage_correlation', self.profile)

    def test_mechanism_id_is_199(self):
        self.assertEqual(self.correlation['mechanism_id'], 199)

    def test_deal_inventory_has_seven_entities(self):
        inventory = self.correlation['deal_inventory']
        self.assertEqual(len(inventory), 7)

    def test_overview_mentions_five_deals(self):
        self.assertIn('5 of the 7', self.correlation['overview'])


class TestCondeNastDealStatusAccuracy(unittest.TestCase):
    """Verify deal status for each entity is correctly documented."""

    def setUp(self):
        self.profile = load_wired_profile()
        self.inventory = self.profile['conde_nast_deal_inventory_coverage_correlation']['deal_inventory']
        self.by_entity = {item['entity']: item for item in self.inventory}

    def test_openai_deal_active(self):
        self.assertEqual(self.by_entity['OpenAI']['deal_status'], 'active')

    def test_amazon_deal_active(self):
        self.assertEqual(self.by_entity['Amazon']['deal_status'], 'active')

    def test_microsoft_deal_active(self):
        self.assertEqual(self.by_entity['Microsoft']['deal_status'], 'active')

    def test_perplexity_deal_active(self):
        self.assertEqual(self.by_entity['Perplexity']['deal_status'], 'active')

    def test_apple_deal_negotiating(self):
        self.assertEqual(self.by_entity['Apple']['deal_status'], 'negotiating')

    def test_google_no_deal(self):
        self.assertEqual(self.by_entity['Google']['deal_status'], 'no_deal')

    def test_meta_no_deal(self):
        self.assertEqual(self.by_entity['Meta']['deal_status'], 'no_deal')

    def test_meta_coverage_most_adversarial(self):
        self.assertIn('most adversarial', self.by_entity['Meta']['coverage_tone'])

    def test_openai_coverage_soft(self):
        self.assertIn('soft', self.by_entity['OpenAI']['coverage_tone'].lower())

    def test_apple_siri_ai_in_deal_type(self):
        self.assertIn('Siri AI', self.by_entity['Apple']['deal_type'])


class TestCondeNastConfounders(unittest.TestCase):
    """Verify confounders are documented (intellectual honesty)."""

    def setUp(self):
        self.profile = load_wired_profile()
        self.correlation = self.profile['conde_nast_deal_inventory_coverage_correlation']

    def test_confounders_exist(self):
        self.assertIn('confounders', self.correlation)

    def test_at_least_three_confounders(self):
        self.assertGreaterEqual(len(self.correlation['confounders']), 3)

    def test_reverse_causality_confounder_documented(self):
        confounders_text = ' '.join(self.correlation['confounders'])
        self.assertIn('reverse causality', confounders_text.lower())

    def test_editorial_independence_confounder_documented(self):
        confounders_text = ' '.join(self.correlation['confounders'])
        self.assertTrue(
            'editorial' in confounders_text.lower() or
            'journalist' in confounders_text.lower()
        )


class TestCondeNastFalsificationTest(unittest.TestCase):
    """Verify the hypothesis includes a falsification test."""

    def setUp(self):
        self.profile = load_wired_profile()
        self.correlation = self.profile['conde_nast_deal_inventory_coverage_correlation']

    def test_falsification_test_exists(self):
        self.assertIn('falsification_test', self.correlation)

    def test_falsification_mentions_openai(self):
        self.assertIn('OpenAI', self.correlation['falsification_test'])

    def test_falsification_references_facial_recognition_parity(self):
        ft = self.correlation['falsification_test']
        self.assertTrue(
            'facial recognition' in ft.lower() or
            'NameTag' in ft
        )


class TestAppleSiriAIDealInRevenueRelationships(unittest.TestCase):
    """Verify Apple revenue relationship updated with Aug 2026 Siri AI deal."""

    def setUp(self):
        self.profile = load_wired_profile()
        self.apple_rel = None
        for r in self.profile.get('revenue_relationships', []):
            if r.get('partner') == 'Apple':
                self.apple_rel = r
                break

    def test_apple_relationship_exists(self):
        self.assertIsNotNone(self.apple_rel)

    def test_mentions_siri_ai(self):
        self.assertIn('Siri AI', self.apple_rel['description'])

    def test_mentions_variable_compensation(self):
        desc = self.apple_rel['description'].lower()
        self.assertIn('variable', desc)

    def test_mentions_nine_figure_budget(self):
        desc = self.apple_rel['description']
        self.assertTrue(
            'nine-figure' in desc.lower() or
            'Nine-figure' in desc
        )

    def test_mentions_aug_2026(self):
        self.assertIn('Aug 2026', self.apple_rel['description'])

    def test_mentions_ios_27(self):
        self.assertIn('iOS 27', self.apple_rel['description'])

    def test_has_wsj_source(self):
        sources = self.apple_rel.get('source_urls', [])
        wsj_found = any('wsj.com' in s for s in sources)
        self.assertTrue(wsj_found, "WSJ source URL required for Apple Siri AI deal")

    def test_mentions_per_use_structural_distinction(self):
        desc = self.apple_rel['description'].lower()
        self.assertTrue(
            'per-use' in desc or
            'per use' in desc
        )


class TestGoogleFrenchAPIG(unittest.TestCase):
    """Verify French APIG AI Overviews complaint is documented in Google entity."""

    def setUp(self):
        self.entities = load_competitor_entities()
        self.google = self.entities['entities']['google']
        self.apig = self.google.get('french_apig_ai_overviews_complaint_aug2026', {})

    def test_apig_section_exists(self):
        self.assertIn('french_apig_ai_overviews_complaint_aug2026', self.google)

    def test_complainant_is_apig(self):
        self.assertIn('APIG', self.apig['complainant'])

    def test_meta_contrast_documented(self):
        self.assertIn('meta_contrast', self.apig)

    def test_meta_enforced_first(self):
        mc = self.apig['meta_contrast']
        self.assertTrue(
            'July 2026' in mc or
            'Jul 2026' in mc
        )

    def test_traffic_decline_quantified(self):
        complaint = self.apig['complaint']
        self.assertTrue(
            '33' in complaint and '38' in complaint
        )

    def test_regulatory_sequence_documented(self):
        self.assertIn('regulatory_sequence', self.apig)
        seq = self.apig['regulatory_sequence']
        self.assertIn('meta_jul_2026', seq)
        self.assertIn('google_aug_2026', seq)

    def test_has_source_urls(self):
        self.assertIn('source_urls', self.apig)
        self.assertGreaterEqual(len(self.apig['source_urls']), 1)


class TestAnthropicZeroDealUpdate(unittest.TestCase):
    """Verify Anthropic zero-deal status updated with Press Gazette confirmation."""

    def setUp(self):
        self.entities = load_competitor_entities()
        self.anthropic = self.entities['entities']['anthropic']

    def test_publisher_deals_note_updated(self):
        note = self.anthropic['publisher_deals_note']
        self.assertIn('PRESS GAZETTE CONFIRMATION', note)

    def test_confirms_zero_deals(self):
        note = self.anthropic['publisher_deals_note']
        self.assertIn('ZERO', note)

    def test_cites_press_gazette_url(self):
        note = self.anthropic['publisher_deals_note']
        self.assertIn('pressgazette.co.uk', note)

    def test_documents_65b_arr(self):
        note = self.anthropic['publisher_deals_note']
        self.assertTrue(
            '$65B' in note or
            '65B' in note
        )

    def test_documents_pre_ipo_credit(self):
        note = self.anthropic['publisher_deals_note']
        self.assertIn('$10B', note)

    def test_paradox_section_present(self):
        note = self.anthropic['publisher_deals_note']
        self.assertIn('PARADOX', note)


class TestMetaDealAbsenceSignificance(unittest.TestCase):
    """Verify Meta's deal absence significance is documented."""

    def setUp(self):
        self.profile = load_wired_profile()
        self.correlation = self.profile['conde_nast_deal_inventory_coverage_correlation']

    def test_meta_deal_absence_section_exists(self):
        self.assertIn('meta_deal_absence_significance', self.correlation)

    def test_documents_13_meta_deals(self):
        text = self.correlation['meta_deal_absence_significance']
        self.assertIn('13 deals', text)

    def test_documents_adversarial_publications_excluded(self):
        text = self.correlation['meta_deal_absence_significance']
        self.assertTrue(
            'adversarial publications' in text.lower() or
            'Condé Nast' in text
        )


class TestCorrelationSourceUrls(unittest.TestCase):
    """Verify source URLs are present and valid."""

    def setUp(self):
        self.profile = load_wired_profile()
        self.correlation = self.profile['conde_nast_deal_inventory_coverage_correlation']

    def test_has_source_urls(self):
        self.assertIn('source_urls', self.correlation)

    def test_at_least_three_sources(self):
        self.assertGreaterEqual(len(self.correlation['source_urls']), 3)

    def test_includes_press_gazette(self):
        urls = self.correlation['source_urls']
        self.assertTrue(any('pressgazette' in u for u in urls))

    def test_includes_conde_nast_official(self):
        urls = self.correlation['source_urls']
        self.assertTrue(any('condenast.com' in u for u in urls))


if __name__ == '__main__':
    unittest.main()
