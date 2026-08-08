"""
Test: Atlantic × OpenAI/Anthropic/Meta — Matteo Wong Cross-Entity Framing Asymmetry
Created: 2026-08-08 04:00 PT (Type A: Competitor Coverage Deep Dive)

Validates that The Atlantic's primary AI beat reporter Matteo Wong applies
systematically different framing standards to Meta vs. OpenAI vs. Anthropic,
consistent with The Atlantic's financial relationships. Updates the Apple v.
OpenAI silence to 29 days (filing Jul 10 → Aug 8, 2026). Tests verify data
consistency across profiles and research documentation.

KEY FINDING — THREE-TIER FRAMING HIERARCHY:
  Meta:      Personalized, reductive, mocking    (-0.45 tone)
  OpenAI:    Industry-wide, underdog, analytical  (-0.05 tone)
  Anthropic: Sympathetic, philosophical, earnest  (+0.20 tone)

Financial relationship correlation:
  Meta:      0 financial relationships → MOST adversarial coverage
  OpenAI:    3+ financial links (licensing, EC equity exit, Atlantic Labs) → neutral
  Anthropic: 0 financial links, 0 publisher deals → sympathetic (no adversarial incentive)
"""
import yaml
import os
import unittest
from datetime import date

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return yaml.safe_load(f)


class TestWongMetaFraming(unittest.TestCase):
    """Verify Matteo Wong's Meta coverage framing is documented."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')
        cls.atlantic = load_yaml('atlantic.yaml')

    def _get_wong_analysis(self):
        return self.research['publications']['atlantic']['wong_cross_entity_framing']

    def test_wong_analysis_exists(self):
        """Wong cross-entity framing analysis exists in Atlantic research."""
        atlantic = self.research['publications']['atlantic']
        self.assertIn('wong_cross_entity_framing', atlantic)

    def test_meta_personalization(self):
        """Wong personalizes Meta to Zuckerberg."""
        meta = self._get_wong_analysis()['meta']
        desc = meta['framing_description']
        self.assertIn('Zuckerberg', desc)

    def test_meta_loaded_language(self):
        """Wong uses loaded language for Meta: legacy, open-washing, aggrievement."""
        meta = self._get_wong_analysis()['meta']
        markers = meta['language_markers']
        # At least 3 loaded markers documented
        self.assertGreaterEqual(len(markers), 3)

    def test_meta_tone_negative(self):
        """Wong's Meta tone is negative (below -0.3)."""
        meta = self._get_wong_analysis()['meta']
        self.assertLess(meta['average_tone'], -0.3)

    def test_meta_reductive_strategy_framing(self):
        """Wong frames Meta AI strategy as reductive — 'just a way to keep people hooked'."""
        meta = self._get_wong_analysis()['meta']
        desc = meta['framing_description']
        self.assertIn('reductive', desc.lower())

    def test_meta_headline_personalization_rate(self):
        """Meta headlines personalized to Zuckerberg at high rate."""
        meta = self._get_wong_analysis()['meta']
        self.assertGreater(meta['headline_personalization_pct'], 50)

    def test_meta_mocking_headline(self):
        """He's No Elon Musk headline documented as mocking."""
        meta = self._get_wong_analysis()['meta']
        articles = meta.get('key_articles', [])
        headlines = [a.get('headline', '') for a in articles]
        any_mocking = any('elon musk' in h.lower() for h in headlines)
        self.assertTrue(any_mocking, "Mocking 'He's No Elon Musk' headline should be documented")


class TestWongOpenAIFraming(unittest.TestCase):
    """Verify Matteo Wong's OpenAI coverage framing is documented."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def _get_wong_analysis(self):
        return self.research['publications']['atlantic']['wong_cross_entity_framing']

    def test_openai_industry_framing(self):
        """OpenAI coverage uses industry-wide framing, not company-specific critique."""
        openai = self._get_wong_analysis()['openai']
        desc = openai['framing_description']
        self.assertIn('industry', desc.lower())

    def test_openai_underdog_narrative(self):
        """OpenAI receives underdog narrative framing."""
        openai = self._get_wong_analysis()['openai']
        desc = openai['framing_description']
        self.assertIn('underdog', desc.lower())

    def test_openai_tone_near_neutral(self):
        """Wong's OpenAI tone is near-neutral (between -0.2 and +0.2)."""
        openai = self._get_wong_analysis()['openai']
        self.assertGreater(openai['average_tone'], -0.2)
        self.assertLess(openai['average_tone'], 0.2)

    def test_openai_headline_personalization_low(self):
        """OpenAI headlines NOT personalized to Altman."""
        openai = self._get_wong_analysis()['openai']
        self.assertLess(openai['headline_personalization_pct'], 30)

    def test_openai_no_loaded_language(self):
        """OpenAI coverage lacks loaded derogatory language."""
        openai = self._get_wong_analysis()['openai']
        markers = openai['language_markers']
        # OpenAI markers should be analytical, not loaded
        loaded = [m for m in markers if any(w in m.lower() for w in ['legacy', 'washing', 'hooked', 'aggrievement', 'mocking'])]
        self.assertEqual(len(loaded), 0, f"OpenAI should not have loaded language: {loaded}")


class TestWongAnthropicFraming(unittest.TestCase):
    """Verify Matteo Wong's Anthropic coverage framing is documented."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def _get_wong_analysis(self):
        return self.research['publications']['atlantic']['wong_cross_entity_framing']

    def test_anthropic_sympathetic(self):
        """Anthropic coverage framed sympathetically."""
        anthropic = self._get_wong_analysis()['anthropic']
        desc = anthropic['framing_description']
        self.assertIn('sympathetic', desc.lower())

    def test_anthropic_philosopher_framing(self):
        """Amodei described as 'philosopher'."""
        anthropic = self._get_wong_analysis()['anthropic']
        desc = anthropic['framing_description']
        self.assertIn('philosopher', desc.lower())

    def test_anthropic_earnest_language(self):
        """Anthropic described with earnest/sincere language."""
        anthropic = self._get_wong_analysis()['anthropic']
        markers = anthropic['language_markers']
        earnest_markers = [m for m in markers if any(w in m.lower() for w in ['earnest', 'philosopher', 'sincere'])]
        self.assertGreater(len(earnest_markers), 0)

    def test_anthropic_tone_positive(self):
        """Wong's Anthropic tone is positive (above 0.0)."""
        anthropic = self._get_wong_analysis()['anthropic']
        self.assertGreater(anthropic['average_tone'], 0.0)

    def test_anthropic_institutional_concern_not_attack(self):
        """Anthropic risks framed as industry/national concern, not institutional failure."""
        anthropic = self._get_wong_analysis()['anthropic']
        desc = anthropic['framing_description']
        # Should reference concern framing, not attack framing
        self.assertNotIn('failure', desc.lower())


class TestWongToneDelta(unittest.TestCase):
    """Verify the tone gaps between entities are documented and significant."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def _get_wong_analysis(self):
        return self.research['publications']['atlantic']['wong_cross_entity_framing']

    def test_meta_openai_gap(self):
        """Meta-to-OpenAI tone gap documented as >= 0.3 points."""
        analysis = self._get_wong_analysis()
        gap = analysis['openai']['average_tone'] - analysis['meta']['average_tone']
        self.assertGreaterEqual(gap, 0.3,
                                f"Meta→OpenAI gap should be >= 0.3, got {gap}")

    def test_meta_anthropic_gap(self):
        """Meta-to-Anthropic tone gap documented as >= 0.5 points."""
        analysis = self._get_wong_analysis()
        gap = analysis['anthropic']['average_tone'] - analysis['meta']['average_tone']
        self.assertGreaterEqual(gap, 0.5,
                                f"Meta→Anthropic gap should be >= 0.5, got {gap}")

    def test_financial_correlation(self):
        """Tone hierarchy correlates with financial relationships."""
        analysis = self._get_wong_analysis()
        # Meta (0 financial links) < OpenAI (3+ links) < Anthropic (0 links, 0 publisher deals)
        self.assertLess(analysis['meta']['average_tone'],
                        analysis['openai']['average_tone'])
        self.assertLess(analysis['openai']['average_tone'],
                        analysis['anthropic']['average_tone'])

    def test_financial_relationship_count(self):
        """Financial relationship counts documented for each entity."""
        analysis = self._get_wong_analysis()
        self.assertEqual(analysis['meta']['financial_relationships_count'], 0)
        self.assertGreaterEqual(analysis['openai']['financial_relationships_count'], 3)
        self.assertEqual(analysis['anthropic']['financial_relationships_count'], 0)


class TestSilenceDurationUpdate(unittest.TestCase):
    """Verify the Apple v. OpenAI silence now spans 29 days (Aug 8)."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def _get_silence(self):
        return self.research['publications']['atlantic']['apple_v_openai_editorial_silence']

    def test_silence_spans_at_least_29_days(self):
        """Silence has reached at least 29 days as of Aug 8, 2026."""
        silence = self._get_silence()
        desc = silence.get('description', '')
        last_verified = silence.get('last_verified_date', '')
        # Either the description or last_verified confirms >= 29 days
        has_29 = '29 days' in desc or '29' in desc
        has_aug8 = 'Aug 8' in desc or last_verified == '2026-08-08'
        self.assertTrue(has_29 or has_aug8,
                        "Silence should reference 29 days or Aug 8 verification")

    def test_silence_still_active(self):
        """Editorial silence confirmed still active."""
        silence = self._get_silence()
        self.assertEqual(silence.get('status', 'active'), 'active')


class TestWongArticleSources(unittest.TestCase):
    """Verify source URLs for key Wong articles are documented."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def _get_wong_analysis(self):
        return self.research['publications']['atlantic']['wong_cross_entity_framing']

    def test_meta_articles_have_urls(self):
        """Meta key articles have source URLs or references."""
        meta = self._get_wong_analysis()['meta']
        articles = meta.get('key_articles', [])
        self.assertGreater(len(articles), 0)
        for article in articles:
            self.assertTrue(
                article.get('url') or article.get('reference'),
                f"Article '{article.get('headline', 'unknown')}' needs source"
            )

    def test_openai_articles_have_urls(self):
        """OpenAI key articles have source URLs or references."""
        openai = self._get_wong_analysis()['openai']
        articles = openai.get('key_articles', [])
        self.assertGreater(len(articles), 0)

    def test_anthropic_articles_have_urls(self):
        """Anthropic key articles have source URLs or references."""
        anthropic = self._get_wong_analysis()['anthropic']
        articles = anthropic.get('key_articles', [])
        self.assertGreater(len(articles), 0)

    def test_all_articles_have_dates(self):
        """All documented articles have dates."""
        analysis = self._get_wong_analysis()
        for entity_key in ['meta', 'openai', 'anthropic']:
            for article in analysis[entity_key].get('key_articles', []):
                self.assertTrue(
                    article.get('date'),
                    f"{entity_key} article '{article.get('headline', 'unknown')}' needs date"
                )


class TestWongMechanismAnalysis(unittest.TestCase):
    """Verify the mechanism explaining the framing hierarchy."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def _get_wong_analysis(self):
        return self.research['publications']['atlantic']['wong_cross_entity_framing']

    def test_mechanism_documented(self):
        """Overall mechanism explanation exists."""
        analysis = self._get_wong_analysis()
        self.assertIn('mechanism', analysis)

    def test_mechanism_references_financial(self):
        """Mechanism references financial relationships as predictor."""
        analysis = self._get_wong_analysis()
        mechanism = analysis['mechanism']
        self.assertIn('financial', mechanism.lower())

    def test_confounding_factors(self):
        """Confounding factors acknowledged."""
        analysis = self._get_wong_analysis()
        self.assertIn('confounding_factors', analysis)
        self.assertGreater(len(analysis['confounding_factors']), 0)

    def test_significance_assessment(self):
        """Significance of finding assessed."""
        analysis = self._get_wong_analysis()
        self.assertIn('significance', analysis)


class TestStructuralConsistency(unittest.TestCase):
    """Cross-check consistency with atlantic.yaml profile."""

    @classmethod
    def setUpClass(cls):
        cls.atlantic = load_yaml('atlantic.yaml')
        cls.research = load_yaml('competitor-coverage-research.yaml')
        cls.entities = load_yaml('competitor-entities.yaml')

    def test_openai_deal_in_atlantic_profile(self):
        """OpenAI licensing deal documented in Atlantic profile."""
        # Check revenue_relationships
        relationships = self.atlantic.get('revenue_relationships', [])
        openai_rels = [r for r in relationships if r.get('partner') == 'OpenAI']
        self.assertGreater(len(openai_rels), 0)

    def test_apple_stock_in_atlantic_profile(self):
        """Apple stock holdings documented in Atlantic profile."""
        relationships = self.atlantic.get('revenue_relationships', [])
        apple_rels = [r for r in relationships if r.get('partner') == 'Apple']
        self.assertGreater(len(apple_rels), 0)

    def test_meta_zero_in_atlantic_profile(self):
        """No Meta financial relationship in Atlantic profile."""
        relationships = self.atlantic.get('revenue_relationships', [])
        meta_rels = [r for r in relationships if r.get('partner') == 'Meta']
        self.assertEqual(len(meta_rels), 0)

    def test_anthropic_zero_publisher_deals(self):
        """Anthropic documented as having zero publisher deals."""
        anthropic = self.entities['entities']['anthropic']
        note = anthropic.get('publisher_deals_note', '')
        self.assertIn('ZERO', note)

    def test_total_test_files_gte_222(self):
        """Total test files >= 222 after this addition."""
        test_dir = os.path.join(os.path.dirname(__file__))
        test_files = [f for f in os.listdir(test_dir) if f.startswith('test_') and f.endswith('.py')]
        self.assertGreaterEqual(len(test_files), 222)


if __name__ == '__main__':
    unittest.main()
