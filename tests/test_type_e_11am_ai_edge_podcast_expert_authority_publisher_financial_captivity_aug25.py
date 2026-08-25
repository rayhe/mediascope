"""
Type E (Podcast Sentiment): AI Edge Podcast Expert Authority Publisher-AI Financial
Captivity Cross-Entity Coverage Incentive Architecture

Tests for mechanism #303: AI Edge Podcast Ep 32 (~Aug 20, 2026) with Brian Wieser
(CEO, Madison and Wall) examining publisher-AI financial captivity, ChatGPT agent ads,
investor devaluation of advertising revenue, and Zuckerberg AI manifesto coverage
asymmetry. Expert authority from the most-cited independent ad industry analyst
amplifies cross-entity vocabulary differential.

Iteration #283 — Tue 2026-08-25 11:00 PT
"""

import os
import unittest

import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
PODCAST_SENTIMENT_PATH = os.path.join(
    os.path.dirname(__file__), '..', 'podcast-sentiment.md'
)


def load_competitor_research():
    path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def get_publications(data):
    return data.get('publications', data)


class TestMechanismStructure(unittest.TestCase):
    """Verify mechanism #303 exists and has all required fields."""

    def setUp(self):
        self.data = load_competitor_research()
        pubs = get_publications(self.data)
        self.key = 'ai_edge_podcast_expert_authority_publisher_ai_financial_captivity_coverage_incentive'
        self.mechanism = pubs.get(self.key, {})

    def test_mechanism_exists(self):
        pubs = get_publications(self.data)
        self.assertIn(self.key, pubs)

    def test_mechanism_id(self):
        self.assertEqual(self.mechanism.get('mechanism_id'), 303)

    def test_mechanism_type(self):
        self.assertEqual(
            self.mechanism.get('type'), 'cross_entity_coverage_incentive'
        )

    def test_has_description(self):
        desc = self.mechanism.get('description', '')
        self.assertGreater(len(desc), 100)

    def test_has_date_added(self):
        self.assertEqual(self.mechanism.get('date_added'), '2026-08-25')

    def test_has_asymmetry_score(self):
        score = self.mechanism.get('asymmetry_score', 0)
        self.assertGreater(score, 0)
        self.assertLessEqual(score, 1.0)

    def test_has_confounders(self):
        confounders = self.mechanism.get('confounders', [])
        self.assertGreaterEqual(len(confounders), 3)

    def test_has_cross_references(self):
        xrefs = self.mechanism.get('cross_references', [])
        self.assertGreaterEqual(len(xrefs), 4)

    def test_has_sources(self):
        sources = self.mechanism.get('sources', [])
        self.assertGreaterEqual(len(sources), 1)
        self.assertTrue(any('youtube.com' in s for s in sources))

    def test_has_test_file(self):
        tf = self.mechanism.get('test_file', '')
        self.assertIn('test_type_e_11am_ai_edge_podcast', tf)

    def test_has_entity_coverage(self):
        ec = self.mechanism.get('entity_coverage', {})
        self.assertIn('meta', ec)
        self.assertIn('openai', ec)

    def test_has_financial_incentive_chain(self):
        chain = self.mechanism.get('financial_incentive_chain', [])
        self.assertGreaterEqual(len(chain), 3)


class TestExpertAuthorityPublisherFinancialCaptivity(unittest.TestCase):
    """Verify the publisher financial captivity thesis in mechanism #303."""

    def setUp(self):
        self.data = load_competitor_research()
        pubs = get_publications(self.data)
        self.key = 'ai_edge_podcast_expert_authority_publisher_ai_financial_captivity_coverage_incentive'
        self.mechanism = pubs.get(self.key, {})
        self.desc = self.mechanism.get('description', '')

    def test_publisher_ai_financial_captivity_discussed(self):
        self.assertIn('monetize AI crawlers', self.desc)

    def test_publisher_revenue_dependency_documented(self):
        self.assertIn('revenue replacement', self.desc.lower()
                       if 'revenue replacement' in self.desc.lower()
                       else self.desc)
        # Alternative: check for publisher dependency language
        self.assertTrue(
            'revenue' in self.desc.lower() and 'publisher' in self.desc.lower()
        )

    def test_validates_mechanism_8(self):
        self.assertIn('#8', self.desc)

    def test_validates_mechanism_9(self):
        self.assertIn('#9', self.desc)

    def test_validates_mechanism_35(self):
        self.assertIn('#35', self.desc)

    def test_expert_is_brian_wieser(self):
        expert = self.mechanism.get('expert', '')
        self.assertIn('Brian Wieser', expert)
        self.assertIn('Madison and Wall', expert)

    def test_cross_ref_to_mechanism_8(self):
        xrefs = self.mechanism.get('cross_references', [])
        mech_ids = [x.get('mechanism_id') for x in xrefs]
        self.assertIn(8, mech_ids)


class TestCrossEntityAdvertisingVocabularyAsymmetry(unittest.TestCase):
    """Verify vocabulary differential between Meta/OpenAI ad framing."""

    def setUp(self):
        self.data = load_competitor_research()
        pubs = get_publications(self.data)
        self.key = 'ai_edge_podcast_expert_authority_publisher_ai_financial_captivity_coverage_incentive'
        self.mechanism = pubs.get(self.key, {})
        self.entity_coverage = self.mechanism.get('entity_coverage', {})

    def test_meta_sentiment_negative(self):
        meta = self.entity_coverage.get('meta', {})
        self.assertLess(meta.get('sentiment_score', 0), 0)

    def test_openai_sentiment_non_negative(self):
        openai = self.entity_coverage.get('openai', {})
        self.assertGreaterEqual(openai.get('sentiment_score', -1), 0)

    def test_meta_vocabulary_includes_defensive_language(self):
        meta = self.entity_coverage.get('meta', {})
        vocab = meta.get('vocabulary', [])
        defensive_terms = ['established', 'mature', 'incumbent']
        self.assertTrue(
            any(any(term in v.lower() for term in defensive_terms) for v in vocab),
            f"Expected defensive vocabulary in Meta framing, got: {vocab}"
        )

    def test_openai_vocabulary_includes_innovation_language(self):
        openai = self.entity_coverage.get('openai', {})
        vocab = openai.get('vocabulary', [])
        innovation_terms = ['experiment', 'agent', 'innovation']
        self.assertTrue(
            any(any(term in v.lower() for term in innovation_terms) for v in vocab),
            f"Expected innovation vocabulary in OpenAI framing, got: {vocab}"
        )

    def test_meta_receives_less_segment_time(self):
        meta = self.entity_coverage.get('meta', {})
        openai = self.entity_coverage.get('openai', {})
        meta_treatment = meta.get('segment_treatment', '')
        openai_treatment = openai.get('segment_treatment', '')
        self.assertIn('quick', meta_treatment.lower())
        self.assertIn('dedicated', openai_treatment.lower())

    def test_asymmetry_score_moderate_to_high(self):
        score = self.mechanism.get('asymmetry_score', 0)
        self.assertGreaterEqual(score, 0.5)

    def test_agent_ads_framing_in_description(self):
        desc = self.mechanism.get('description', '')
        self.assertIn('agent ads', desc.lower())


class TestInvestorDevaluationAdRevenueNarrative(unittest.TestCase):
    """Verify investor devaluation of ad revenue creates coverage pressure."""

    def setUp(self):
        self.data = load_competitor_research()
        pubs = get_publications(self.data)
        self.key = 'ai_edge_podcast_expert_authority_publisher_ai_financial_captivity_coverage_incentive'
        self.mechanism = pubs.get(self.key, {})
        self.desc = self.mechanism.get('description', '')

    def test_investor_devaluation_discussed(self):
        self.assertIn('devaluing advertising revenue', self.desc.lower()
                       if 'devaluing advertising revenue' in self.desc.lower()
                       else self.desc)
        self.assertTrue(
            'investor' in self.desc.lower() or 'devaluing' in self.desc.lower()
        )

    def test_pre_ipo_benefit_documented(self):
        self.assertTrue(
            'pre-ipo' in self.desc.lower() or 'pre-IPO' in self.desc
        )

    def test_financial_incentive_chain_has_steps(self):
        chain = self.mechanism.get('financial_incentive_chain', [])
        self.assertGreaterEqual(len(chain), 3)
        # Verify steps have descriptions
        for step in chain:
            self.assertIn('description', step)
            self.assertGreater(len(step['description']), 10)

    def test_cross_ref_to_mechanism_302(self):
        xrefs = self.mechanism.get('cross_references', [])
        mech_ids = [x.get('mechanism_id') for x in xrefs]
        self.assertIn(302, mech_ids)

    def test_cross_ref_to_mechanism_35(self):
        xrefs = self.mechanism.get('cross_references', [])
        mech_ids = [x.get('mechanism_id') for x in xrefs]
        self.assertIn(35, mech_ids)

    def test_zuckerberg_manifesto_compressed_treatment(self):
        self.assertIn('quick hits', self.desc.lower()
                       if 'quick hits' in self.desc.lower()
                       else self.desc)
        self.assertTrue(
            'manifesto' in self.desc.lower() or 'Zuckerberg' in self.desc
        )


class TestPodcastSentimentDocHasEntry71(unittest.TestCase):
    """Verify entry #71 exists in podcast-sentiment.md."""

    def setUp(self):
        with open(PODCAST_SENTIMENT_PATH, 'r') as f:
            self.content = f.read()

    def test_entry_71_header_exists(self):
        self.assertIn('### 71.', self.content)

    def test_ai_edge_podcast_mentioned(self):
        self.assertIn('AI Edge Podcast', self.content)

    def test_brian_wieser_mentioned(self):
        self.assertIn('Brian Wieser', self.content)

    def test_madison_and_wall_mentioned(self):
        self.assertIn('Madison and Wall', self.content)

    def test_source_url_present(self):
        self.assertIn('https://www.youtube.com/watch?v=1IR_LtHZ6NU', self.content)

    def test_mechanism_303_referenced(self):
        self.assertIn('#303', self.content)

    def test_sentiment_score_documented(self):
        # Meta should have negative sentiment
        self.assertIn('-3/10', self.content)

    def test_cross_references_present(self):
        self.assertIn('Mechanism #24', self.content)
        self.assertIn('Mechanism #8', self.content)
        self.assertIn('Mechanism #302', self.content)


if __name__ == '__main__':
    unittest.main()
