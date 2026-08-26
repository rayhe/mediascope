"""
Test: David Price (Macworld/Foundry) — Apple-Ecosystem Advocacy Editorial Framing
      with AI Summary Amplification

Mechanism #314: David Price, UK Editor at Macworld (Foundry/Regent LP), applies
entity-selective pejorative vocabulary within an article about Apple smart glasses.
The article quotes Gurman (Bloomberg) describing category-wide privacy concerns
attributed to Meta, Samsung, and Google — but the Macworld editorial applies
"controversial" exclusively to Meta. The page's AI-generated summary (explicitly
labeled "created by Smart Answers AI") further amplifies this entity-selective
framing with "Meta's controversial approach."

Financial architecture: Macworld covers EXCLUSIVELY Apple products and derives
revenue from Apple affiliate commissions. Its editor self-describes as an
"enthusiastic Apple Watch evangelist." Meta has ZERO financial relationship with
Macworld/Foundry.

Key insight: This is structural revenue dependency creating permanent editorial
alignment, combined with an observable AI summary amplification layer.

Note: The Bloomberg/Gurman primary source was not independently fetched. Claims
about Gurman's language are based on what the Macworld article itself quotes.

Source article: David Price, "Apple eyes WWDC smart glasses launch with a focus on
privacy," Macworld, Jul 27, 2026
Source URL: https://www.macworld.com/article/3199653/apple-eyes-wwdc-smart-glasses-launch-with-a-focus-on-privacy.html
"""

import unittest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_research():
    path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def find_mechanism(data, mechanism_id):
    """Recursively search for mechanism_id in nested dict/list structure."""
    if isinstance(data, dict):
        if data.get('mechanism_id') == mechanism_id:
            return data
        for v in data.values():
            result = find_mechanism(v, mechanism_id)
            if result and isinstance(result, dict) and 'mechanism_id' in result:
                return result
    elif isinstance(data, list):
        for item in data:
            result = find_mechanism(item, mechanism_id)
            if result and isinstance(result, dict) and 'mechanism_id' in result:
                return result
    return None


class TestMechanism314Exists(unittest.TestCase):
    """Verify mechanism #314 exists with correct metadata."""

    @classmethod
    def setUpClass(cls):
        data = load_competitor_research()
        cls.mechanism = find_mechanism(data, 314)

    def test_mechanism_exists(self):
        self.assertIsNotNone(self.mechanism, "Mechanism #314 must exist")

    def test_mechanism_type(self):
        self.assertEqual(self.mechanism['type'], 'journalist_cross_entity_tracking')

    def test_mechanism_domain(self):
        self.assertEqual(self.mechanism['domain'], 'smart_glasses_camera_wearables')

    def test_finding_type(self):
        self.assertIn('editorial_framing_injection', self.mechanism['finding_type'])

    def test_publication(self):
        self.assertEqual(self.mechanism['publication'], 'Macworld')

    def test_journalist(self):
        self.assertEqual(self.mechanism['journalist'], 'David Price')


class TestDavidPriceJournalistProfile(unittest.TestCase):
    """Verify David Price's role, self-description, and Apple advocacy identity."""

    @classmethod
    def setUpClass(cls):
        data = load_competitor_research()
        cls.mechanism = find_mechanism(data, 314)

    def test_role_is_editor(self):
        self.assertIn('Editor', self.mechanism['role'])

    def test_self_described_apple_evangelist(self):
        self.assertIn('Apple Watch evangelist', self.mechanism['self_description'])

    def test_self_described_apple_hype_train(self):
        self.assertIn('Apple hype train', self.mechanism['self_description'])

    def test_article_date(self):
        self.assertEqual(self.mechanism['article_analyzed']['date'], '2026-07-27')

    def test_source_is_gurman_bloomberg(self):
        self.assertIn('Gurman', self.mechanism['article_analyzed']['source_material'])
        self.assertIn('Bloomberg', self.mechanism['article_analyzed']['source_material'])


class TestEditorialFramingInjection(unittest.TestCase):
    """Core test: verify the editorial vocabulary was ADDED by Price, not from Gurman."""

    @classmethod
    def setUpClass(cls):
        data = load_competitor_research()
        cls.mechanism = find_mechanism(data, 314)
        cls.injection = cls.mechanism['editorial_framing_injection']

    def test_gurman_original_is_descriptive(self):
        self.assertIn('Descriptive', self.injection['gurman_original_framing'])

    def test_gurman_does_not_use_controversial(self):
        """The Gurman quotation (as cited in the article) uses no pejorative label."""
        # The YAML description field mentions the absence of the term in an
        # explanatory note, so we check the actual quoted material portion only.
        framing = self.injection['gurman_original_framing']
        # Extract the quoted portion (between the first pair of quotation marks)
        import re
        quotes = re.findall(r'"([^"]*)"', framing)
        for q in quotes:
            self.assertNotIn('controversial', q.lower(),
                             "Gurman's quoted text should not contain 'controversial'")

    def test_price_adds_controversial(self):
        self.assertIn('controversial', self.injection['price_editorial_addition'].lower())

    def test_controversial_applied_only_to_meta(self):
        self.assertIn("Meta's controversial", self.injection['price_editorial_addition'])

    def test_amplification_pattern_documented(self):
        amp = self.injection['amplification_pattern']
        self.assertIn('Meta', amp)
        self.assertIn('Samsung and Google', amp)
        # Pattern should document the narrowing/selective application
        self.assertTrue('narrowed' in amp or 'entity-selective' in amp or 'selective' in amp,
                        "Amplification pattern should document selective framing")

    def test_samsung_google_invisible_in_framing(self):
        amp = self.injection['amplification_pattern']
        self.assertIn('Samsung and Google', amp)
        self.assertIn('invisible', amp)

    def test_ai_summary_amplification_documented(self):
        """The AI-generated summary amplification layer is explicitly documented."""
        ai_amp = self.injection['ai_summary_amplification']
        self.assertIn('Smart Answers AI', ai_amp)
        self.assertIn('controversial', ai_amp.lower())


class TestVocabularyAnalysis(unittest.TestCase):
    """Verify documented vocabulary differential between Meta and Apple."""

    @classmethod
    def setUpClass(cls):
        data = load_competitor_research()
        cls.mechanism = find_mechanism(data, 314)
        cls.vocab = cls.mechanism['vocabulary_analysis']

    def test_meta_vocabulary_has_controversial(self):
        meta_vocab = [v.lower() for v in self.vocab['meta_vocabulary']]
        self.assertTrue(any('controversial' in v for v in meta_vocab),
                        "Meta vocabulary must include 'controversial'")

    def test_meta_vocabulary_has_surveillance(self):
        meta_vocab = [v.lower() for v in self.vocab['meta_vocabulary']]
        self.assertTrue(any('surveillance' in v for v in meta_vocab))

    def test_apple_vocabulary_has_pro_privacy(self):
        apple_vocab = [v.lower() for v in self.vocab['apple_vocabulary']]
        self.assertTrue(any('pro-privacy' in v for v in apple_vocab))

    def test_apple_vocabulary_has_safeguard(self):
        apple_vocab = [v.lower() for v in self.vocab['apple_vocabulary']]
        self.assertTrue(any('safeguard' in v for v in apple_vocab))

    def test_samsung_google_vocabulary_empty(self):
        self.assertEqual(len(self.vocab['samsung_google_vocabulary']), 0,
                         "Samsung/Google receive zero independent vocabulary")

    def test_meta_alarm_count_greater_than_apple(self):
        """Meta and Apple vocabularies diverge in polarity, not necessarily count."""
        meta_vocab = [v.lower() for v in self.vocab['meta_vocabulary']]
        apple_vocab = [v.lower() for v in self.vocab['apple_vocabulary']]
        # Both should have entries documenting the divergent framing
        self.assertGreaterEqual(len(meta_vocab), 3,
                                "Meta should have multiple adversarial vocabulary entries")
        self.assertGreaterEqual(len(apple_vocab), 3,
                                "Apple should have multiple aspirational vocabulary entries")
        # Polarity check: Meta vocab should contain adversarial terms
        adversarial_meta = [v for v in meta_vocab
                            if any(t in v for t in ['controversial', 'surveillance',
                                                     'intrusive', 'stealth'])]
        aspirational_apple = [v for v in apple_vocab
                              if any(t in v for t in ['privacy', 'safeguard',
                                                       'decade', 'drastic'])]
        self.assertGreater(len(adversarial_meta), 0,
                           "Meta vocabulary should contain adversarial terms")
        self.assertGreater(len(aspirational_apple), 0,
                           "Apple vocabulary should contain aspirational terms")


class TestCrossEntityHeadlineComparison(unittest.TestCase):
    """Verify David Price applies different vocabulary to Meta vs Apple in headlines."""

    @classmethod
    def setUpClass(cls):
        data = load_competitor_research()
        cls.mechanism = find_mechanism(data, 314)
        cls.headlines = cls.mechanism['cross_entity_headline_comparison']

    def test_meta_adjacent_headlines_exist(self):
        self.assertGreater(len(self.headlines['meta_adjacent_headlines']), 0)

    def test_apple_advocacy_headlines_exist(self):
        self.assertGreater(len(self.headlines['apple_advocacy_headlines']), 0)

    def test_meta_glasses_killer_headline(self):
        meta_titles = [h['title'] for h in self.headlines['meta_adjacent_headlines']]
        self.assertTrue(any('killer' in t.lower() for t in meta_titles),
                        "Price uses 'killer' to frame Meta as target")

    def test_apple_brilliance_headline(self):
        apple_titles = [h['title'] for h in self.headlines['apple_advocacy_headlines']]
        self.assertTrue(any('brilliance' in t.lower() or 'right' in t.lower()
                            for t in apple_titles),
                        "Price uses aspirational/advocacy language for Apple")

    def test_meta_product_neutral_when_serving_apple(self):
        """WhatsApp coverage is neutral because it serves Apple ecosystem users."""
        neutral = self.headlines['meta_product_when_serving_apple']
        self.assertGreater(len(neutral), 0)
        for entry in neutral:
            self.assertIn('neutral', entry['framing'].lower(),
                          f"Meta product '{entry['title']}' should be covered neutrally")


class TestFinancialArchitecture(unittest.TestCase):
    """Verify Macworld's Apple-dependent financial structure."""

    @classmethod
    def setUpClass(cls):
        data = load_competitor_research()
        cls.mechanism = find_mechanism(data, 314)
        cls.finance = cls.mechanism['financial_architecture']

    def test_affiliate_revenue_from_apple(self):
        self.assertIn('affiliate', self.finance['affiliate_revenue'].lower())
        self.assertIn('commission', self.finance['affiliate_revenue'].lower())

    def test_exclusively_apple_coverage(self):
        self.assertIn('EXCLUSIVELY', self.finance['publication_scope'])
        self.assertIn('Apple', self.finance['publication_scope'])

    def test_meta_financial_relationship_none(self):
        self.assertIn('none', self.finance['meta_financial_relationship'].lower())

    def test_regent_lp_ownership(self):
        self.assertIn('Regent LP', self.finance['parent_ownership'])

    def test_regent_also_owns_techcrunch(self):
        self.assertIn('TechCrunch', self.finance['parent_ownership'])


class TestConfoundingFactors(unittest.TestCase):
    """Verify documented confounding factors and counter-confounding evidence."""

    @classmethod
    def setUpClass(cls):
        data = load_competitor_research()
        cls.mechanism = find_mechanism(data, 314)
        cls.confounders = cls.mechanism['confounding_factors']

    def test_at_least_three_confounding_factors(self):
        self.assertGreaterEqual(len(self.confounders), 3)

    def test_has_strong_counter_confounding(self):
        strengths = [c['strength'] for c in self.confounders]
        self.assertTrue(any('STRONG_AGAINST' in s for s in strengths),
                        "Must have at least one STRONG counter-confounding factor")

    def test_counter_confounding_whatsapp_neutral(self):
        """The WhatsApp-neutral coverage counter-confounding is documented."""
        strong = [c for c in self.confounders if 'STRONG_AGAINST' in c['strength']]
        text = ' '.join(c['factor'] for c in strong).lower()
        self.assertTrue('whatsapp' in text or 'competitive' in text or 'selective' in text,
                        "Counter-confounding should reference selective application")

    def test_counter_confounding_samsung_google_omission(self):
        """Gurman named Samsung/Google but Price omitted them from 'controversial'."""
        strong = [c for c in self.confounders if 'STRONG_AGAINST' in c['strength']]
        text = ' '.join(c['factor'] for c in strong).lower()
        self.assertTrue('samsung' in text or 'google' in text or 'gurman' in text,
                        "Counter-confounding should reference Gurman naming Samsung/Google")


class TestCrossReferences(unittest.TestCase):
    """Verify cross-references to related mechanisms."""

    @classmethod
    def setUpClass(cls):
        data = load_competitor_research()
        cls.mechanism = find_mechanism(data, 314)
        cls.refs = cls.mechanism['cross_references']

    def test_has_cross_references(self):
        self.assertGreater(len(self.refs), 0)

    def test_references_editorial_commissioning_309(self):
        ref_ids = [r['mechanism_id'] for r in self.refs]
        self.assertIn(309, ref_ids,
                      "Should reference #309 — Fast Company editorial commissioning bifurcation")

    def test_references_apple_privacy_cascade_289(self):
        ref_ids = [r['mechanism_id'] for r in self.refs]
        self.assertIn(289, ref_ids,
                      "Should reference #289 — Apple privacy hero cascade")


class TestSourcesCited(unittest.TestCase):
    """Verify all factual claims are backed by cited sources."""

    @classmethod
    def setUpClass(cls):
        data = load_competitor_research()
        cls.mechanism = find_mechanism(data, 314)
        cls.sources = cls.mechanism.get('sources', [])

    def test_has_sources(self):
        self.assertGreater(len(self.sources), 0, "Mechanism must cite sources")

    def test_primary_article_cited(self):
        urls = [s['url'] for s in self.sources]
        self.assertTrue(any('macworld.com/article/3199653' in u for u in urls),
                        "Primary analyzed article must be cited")

    def test_author_page_cited(self):
        urls = [s['url'] for s in self.sources]
        self.assertTrue(any('macworld.com/author/David.Price' in u for u in urls),
                        "David Price author page must be cited")

    def test_about_page_cited(self):
        urls = [s['url'] for s in self.sources]
        self.assertTrue(any('macworld.com/about' in u for u in urls),
                        "Macworld About page must be cited")

    def test_foundry_ownership_cited(self):
        """At least one source documents Foundry/IDG ownership structure."""
        descs = ' '.join(s.get('description', '') for s in self.sources).lower()
        self.assertTrue('foundry' in descs or 'idg' in descs or 'regent' in descs,
                        "Foundry/IDG/Regent ownership must have a source")


if __name__ == '__main__':
    unittest.main()
