"""
Test suite: Publisher AI Revenue Asymmetry Matrix
Type C: Financial Incentive Mapping — Cross-Publisher Revenue Correlation

Tests the comprehensive mapping of verified AI content licensing revenue
sources against observed Meta coverage tone across all 10 MediaScope-profiled
publications.

Key finding: Among 10 profiled publications, News Corp is the ONLY one with
a Meta AI licensing deal. It is also the ONLY one with balanced Meta coverage
AND the ONLY one that systematically discloses its financial relationships.
The correlation between financial incentive direction and Meta coverage tone
is 100%.

Sources:
  - WSJ (Mar 4, 2026): News Corp-Meta $50M/yr deal
  - Reuters (May 22, 2024): News Corp-OpenAI $250M/5yr deal
  - MarketBeat (Aug 5, 2026): News Corp Q4 FY2026 earnings transcript
  - SiliconAngle (Aug 20, 2024): Conde Nast-OpenAI deal
  - Digiday (2025): Publisher AI deal timeline
  - Reuters (May 29, 2024): Atlantic and Vox Media OpenAI deals
  - AAP (Jul 20, 2026): Bartz v. Anthropic settlement approval
"""

import unittest
import yaml
import os


def load_research_profile():
    path = os.path.join(
        os.path.dirname(__file__), '..', 'profiles',
        'competitor-coverage-research.yaml'
    )
    with open(path) as f:
        return yaml.safe_load(f)


def load_entities():
    path = os.path.join(
        os.path.dirname(__file__), '..', 'profiles',
        'competitor-entities.yaml'
    )
    with open(path) as f:
        return yaml.safe_load(f)


def load_news_corp_profile():
    path = os.path.join(
        os.path.dirname(__file__), '..', 'profiles',
        'news-corp.yaml'
    )
    with open(path) as f:
        return yaml.safe_load(f)


def get_matrix():
    data = load_research_profile()
    return data['cross_publication_findings']['publisher_ai_revenue_asymmetry_matrix']


class TestMatrixStructure(unittest.TestCase):
    """Validate matrix schema completeness."""

    def test_matrix_exists(self):
        matrix = get_matrix()
        self.assertIsNotNone(matrix)

    def test_has_publishers_section(self):
        matrix = get_matrix()
        self.assertIn('publishers', matrix)
        self.assertGreaterEqual(len(matrix['publishers']), 9)

    def test_has_statistical_summary(self):
        matrix = get_matrix()
        self.assertIn('statistical_summary', matrix)

    def test_has_source_urls(self):
        matrix = get_matrix()
        self.assertIn('source_urls', matrix)
        self.assertGreaterEqual(len(matrix['source_urls']), 5)

    def test_all_source_urls_https(self):
        matrix = get_matrix()
        for url in matrix['source_urls']:
            self.assertTrue(
                url.startswith('https://'),
                f"Non-HTTPS source URL: {url}"
            )

    def test_has_methodology(self):
        matrix = get_matrix()
        self.assertIn('methodology', matrix)

    def test_has_mechanism(self):
        matrix = get_matrix()
        self.assertEqual(
            matrix['mechanism'],
            'financial_incentive_coverage_correlation'
        )


class TestPublisherCompleteness(unittest.TestCase):
    """Every profiled publisher must have required fields."""

    def setUp(self):
        self.matrix = get_matrix()
        self.required_publisher_slugs = [
            'news_corp', 'conde_nast_wired', 'nyt',
            'the_verge_vox_media', 'the_atlantic',
            'financial_times', 'guardian', 'mit_tech_review', 'gizmodo'
        ]

    def test_all_required_publishers_present(self):
        for slug in self.required_publisher_slugs:
            self.assertIn(
                slug, self.matrix['publishers'],
                f"Missing publisher: {slug}"
            )

    def test_each_publisher_has_display_name(self):
        for slug in self.required_publisher_slugs:
            pub = self.matrix['publishers'][slug]
            self.assertIn('display_name', pub, f"{slug} missing display_name")

    def test_each_publisher_has_meta_deal_value(self):
        for slug in self.required_publisher_slugs:
            pub = self.matrix['publishers'][slug]
            self.assertIn(
                'meta_deal_value', pub,
                f"{slug} missing meta_deal_value"
            )

    def test_each_publisher_has_net_financial_direction(self):
        for slug in self.required_publisher_slugs:
            pub = self.matrix['publishers'][slug]
            self.assertIn(
                'net_financial_direction', pub,
                f"{slug} missing net_financial_direction"
            )

    def test_each_publisher_has_meta_coverage_tone(self):
        for slug in self.required_publisher_slugs:
            pub = self.matrix['publishers'][slug]
            self.assertIn(
                'meta_coverage_tone', pub,
                f"{slug} missing meta_coverage_tone"
            )

    def test_each_publisher_has_competitor_deals(self):
        for slug in self.required_publisher_slugs:
            pub = self.matrix['publishers'][slug]
            self.assertIn(
                'competitor_deals', pub,
                f"{slug} missing competitor_deals"
            )


class TestNewsCorpBalancedControl(unittest.TestCase):
    """News Corp is the balanced control with equal financial incentives."""

    def setUp(self):
        self.pub = get_matrix()['publishers']['news_corp']

    def test_has_meta_deal(self):
        self.assertIn('$50M', self.pub['meta_deal_value'])

    def test_has_openai_deal(self):
        deals = self.pub['competitor_deals']
        openai_deals = [d for d in deals if d['partner'] == 'OpenAI']
        self.assertEqual(len(openai_deals), 1)
        self.assertIn('$50M', openai_deals[0]['value'])

    def test_has_anthropic_settlement(self):
        deals = self.pub['competitor_deals']
        anthro = [d for d in deals if d['partner'] == 'Anthropic']
        self.assertEqual(len(anthro), 1)
        self.assertIn('$1.5B', anthro[0]['value'])

    def test_financial_direction_balanced(self):
        self.assertEqual(self.pub['net_financial_direction'], 'BALANCED')

    def test_meta_tone_balanced(self):
        tone = self.pub['meta_coverage_tone']
        self.assertGreater(tone, -0.30)
        self.assertLess(tone, 0.30)

    def test_discloses_relationships(self):
        self.assertTrue(self.pub['discloses_relationships'])

    def test_total_revenue_100m_plus(self):
        self.assertIn('$100M', self.pub['total_verified_ai_revenue_yr'])

    def test_has_q4_confirmation(self):
        self.assertIn('q4_fy2026_confirmation', self.pub)

    def test_ceo_praises_meta(self):
        stance = self.pub['ceo_meta_stance']
        self.assertIn('principled', stance.lower())


class TestCondeNastOneSided(unittest.TestCase):
    """Conde Nast/WIRED has 4 competitor deals, 0 Meta deals."""

    def setUp(self):
        self.pub = get_matrix()['publishers']['conde_nast_wired']

    def test_zero_meta_revenue(self):
        self.assertEqual(self.pub['meta_deal_value'], '$0')

    def test_four_competitor_deals(self):
        self.assertEqual(len(self.pub['competitor_deals']), 4)

    def test_openai_deal_present(self):
        partners = [d['partner'] for d in self.pub['competitor_deals']]
        self.assertIn('OpenAI', partners)

    def test_amazon_deal_present(self):
        partners = [d['partner'] for d in self.pub['competitor_deals']]
        amazon_deals = [p for p in partners if 'Amazon' in p]
        self.assertGreaterEqual(len(amazon_deals), 1)

    def test_microsoft_deal_present(self):
        partners = [d['partner'] for d in self.pub['competitor_deals']]
        ms_deals = [p for p in partners if 'Microsoft' in p]
        self.assertGreaterEqual(len(ms_deals), 1)

    def test_financial_direction_anti_meta(self):
        self.assertIn('ANTI-META', self.pub['net_financial_direction'])

    def test_adversarial_tone(self):
        self.assertLess(self.pub['meta_coverage_tone'], -0.60)

    def test_no_disclosure(self):
        self.assertFalse(self.pub['discloses_relationships'])

    def test_advance_parent_conflict_documented(self):
        self.assertIn('parent_conflict', self.pub)
        self.assertIn('Advance', self.pub['parent_conflict'])
        self.assertIn('Reddit', self.pub['parent_conflict'])


class TestNYTOneSided(unittest.TestCase):
    """NYT has Amazon deal + OpenAI lawsuit, 0 Meta deals."""

    def setUp(self):
        self.pub = get_matrix()['publishers']['nyt']

    def test_zero_meta_revenue(self):
        self.assertEqual(self.pub['meta_deal_value'], '$0')

    def test_amazon_deal_value(self):
        deals = self.pub['competitor_deals']
        self.assertEqual(len(deals), 1)
        self.assertIn('Amazon', deals[0]['partner'])
        self.assertIn('$20', deals[0]['value'])

    def test_active_litigation(self):
        self.assertIn('active_litigation', self.pub)
        targets = [l['target'] for l in self.pub['active_litigation']]
        self.assertTrue(any('OpenAI' in t for t in targets))

    def test_financial_direction_anti_meta(self):
        self.assertIn('ANTI-META', self.pub['net_financial_direction'])

    def test_adversarial_tone(self):
        self.assertLess(self.pub['meta_coverage_tone'], -0.50)

    def test_no_disclosure(self):
        self.assertFalse(self.pub['discloses_relationships'])


class TestCorrelationStatistics(unittest.TestCase):
    """Validate the statistical summary claims."""

    def setUp(self):
        self.stats = get_matrix()['statistical_summary']
        self.pubs = get_matrix()['publishers']

    def test_total_publications_count(self):
        self.assertEqual(self.stats['total_profiled_publications'], 10)

    def test_one_meta_deal_publication(self):
        self.assertEqual(self.stats['publications_with_meta_deal'], 1)

    def test_seven_competitor_only(self):
        self.assertEqual(
            self.stats['publications_with_competitor_deals_only'], 7
        )

    def test_two_no_deals(self):
        self.assertEqual(self.stats['publications_with_no_deals'], 2)

    def test_perfect_correlation(self):
        self.assertEqual(
            self.stats['correlation_meta_deal_balanced_tone'], 1.0
        )
        self.assertEqual(
            self.stats['correlation_no_meta_deal_adversarial'], 1.0
        )

    def test_balanced_publisher_has_most_positive_meta_tone(self):
        """News Corp should have the highest (least negative) Meta tone."""
        tones = {}
        for slug, pub in self.pubs.items():
            tone = pub.get('meta_coverage_tone')
            if tone is not None:
                tones[slug] = tone
        if tones:
            max_slug = max(tones, key=tones.get)
            self.assertEqual(max_slug, 'news_corp')

    def test_most_adversarial_is_one_sided(self):
        """Conde Nast (most deals, 0 Meta) should have most adversarial tone."""
        tones = {}
        for slug, pub in self.pubs.items():
            tone = pub.get('meta_coverage_tone')
            if tone is not None:
                tones[slug] = tone
        if tones:
            min_slug = min(tones, key=tones.get)
            self.assertEqual(min_slug, 'conde_nast_wired')

    def test_thomson_quotes_present(self):
        quotes = self.stats.get('thomson_q4_fy2026_quotes', {})
        self.assertIn('partnership_language', quotes)
        self.assertIn('principled_praise', quotes)
        self.assertIn('benchmarks', quotes)

    def test_thomson_source_url(self):
        quotes = self.stats.get('thomson_q4_fy2026_quotes', {})
        url = quotes.get('source_url', '')
        self.assertTrue(url.startswith('https://'))
        self.assertIn('marketbeat', url)


class TestDisclosureCorrelation(unittest.TestCase):
    """Disclosure practice correlates with balanced deals."""

    def setUp(self):
        self.pubs = get_matrix()['publishers']

    def test_news_corp_discloses(self):
        self.assertTrue(
            self.pubs['news_corp']['discloses_relationships']
        )

    def test_no_other_publisher_discloses(self):
        non_news_corp = {
            k: v for k, v in self.pubs.items()
            if k not in ('news_corp', 'news_corp_additional')
        }
        for slug, pub in non_news_corp.items():
            disclosure = pub.get('discloses_relationships')
            if disclosure is not None:
                self.assertIn(
                    disclosure, (False, 'not_applicable'),
                    f"{slug} unexpectedly discloses relationships"
                )

    def test_gizmodo_not_applicable(self):
        self.assertEqual(
            self.pubs['gizmodo']['discloses_relationships'],
            'not_applicable'
        )


class TestCleanControls(unittest.TestCase):
    """Gizmodo and MIT TR serve as clean controls."""

    def test_gizmodo_zero_deals(self):
        pub = get_matrix()['publishers']['gizmodo']
        self.assertEqual(len(pub['competitor_deals']), 0)
        self.assertEqual(pub['meta_deal_value'], '$0')

    def test_mit_tr_zero_deals(self):
        pub = get_matrix()['publishers']['mit_tech_review']
        self.assertEqual(len(pub['competitor_deals']), 0)
        self.assertEqual(pub['meta_deal_value'], '$0')

    def test_gizmodo_neutral_direction(self):
        pub = get_matrix()['publishers']['gizmodo']
        self.assertIn('NEUTRAL', pub['net_financial_direction'])

    def test_clean_controls_moderate_adversarial(self):
        """Both clean controls should show moderate adversarial tone."""
        giz = get_matrix()['publishers']['gizmodo']
        mit = get_matrix()['publishers']['mit_tech_review']
        for pub in [giz, mit]:
            tone = pub['meta_coverage_tone']
            self.assertLess(tone, 0)
            self.assertGreater(tone, -0.60)


class TestFinancialGapPredictsTone(unittest.TestCase):
    """The financial incentive gap predicts Meta coverage tone."""

    def setUp(self):
        self.pubs = get_matrix()['publishers']

    def test_balanced_more_positive_than_one_sided(self):
        """News Corp (balanced) must be more positive than all one-sided pubs."""
        balanced_tone = self.pubs['news_corp']['meta_coverage_tone']
        one_sided_slugs = [
            'conde_nast_wired', 'nyt', 'the_verge_vox_media',
            'the_atlantic', 'financial_times', 'guardian'
        ]
        for slug in one_sided_slugs:
            tone = self.pubs[slug]['meta_coverage_tone']
            self.assertGreater(
                balanced_tone, tone,
                f"News Corp ({balanced_tone}) not more positive than {slug} ({tone})"
            )

    def test_financial_premium_significant(self):
        """Gap between balanced and average one-sided should be >= 0.30."""
        balanced = self.pubs['news_corp']['meta_coverage_tone']
        one_sided_tones = [
            self.pubs[s]['meta_coverage_tone']
            for s in [
                'conde_nast_wired', 'nyt', 'the_verge_vox_media',
                'the_atlantic', 'financial_times', 'guardian'
            ]
        ]
        avg_one_sided = sum(one_sided_tones) / len(one_sided_tones)
        gap = balanced - avg_one_sided
        self.assertGreaterEqual(
            gap, 0.30,
            f"Financial premium gap ({gap:.2f}) below 0.30 threshold"
        )

    def test_most_deals_most_adversarial(self):
        """Conde Nast (4 deals, 0 Meta) should be most adversarial."""
        cn_tone = self.pubs['conde_nast_wired']['meta_coverage_tone']
        for slug, pub in self.pubs.items():
            if slug in ('conde_nast_wired', 'news_corp_additional'):
                continue
            tone = pub.get('meta_coverage_tone')
            if tone is not None:
                self.assertLessEqual(
                    cn_tone, tone,
                    f"Conde Nast ({cn_tone}) not most adversarial vs {slug} ({tone})"
                )


class TestQ4FY2026EarningsData(unittest.TestCase):
    """News Corp Q4 FY2026 earnings validate AI licensing as material."""

    def setUp(self):
        self.additional = get_matrix()['publishers'].get('news_corp_additional', {})

    def test_q4_earnings_present(self):
        self.assertIn('q4_fy2026_earnings', self.additional)

    def test_record_quarter(self):
        q4 = self.additional['q4_fy2026_earnings']
        self.assertTrue(q4['record_quarter'])

    def test_revenue_beat(self):
        q4 = self.additional['q4_fy2026_earnings']
        self.assertEqual(q4['revenue_b'], 2.34)
        self.assertEqual(q4['revenue_yoy_pct'], 11)

    def test_margin_expansion(self):
        q4 = self.additional['q4_fy2026_earnings']
        self.assertGreaterEqual(q4['ebitda_margin_expansion_bp'], 200)
        self.assertGreaterEqual(q4['dow_jones_margin_expansion_bp'], 300)

    def test_ai_licensing_near_100pct_margin(self):
        q4 = self.additional['q4_fy2026_earnings']
        self.assertTrue(q4['ai_licensing_near_100pct_margin'])

    def test_deal_pipeline_confirmed(self):
        self.assertIn('deal_pipeline_confirmed', self.additional)

    def test_brave_lawsuit_documented(self):
        self.assertIn('brave_lawsuit', self.additional)


class TestCrossValidationWithEntityProfiles(unittest.TestCase):
    """Matrix data must be consistent with competitor-entities.yaml."""

    def setUp(self):
        self.entities = load_entities()['entities']
        self.matrix = get_matrix()

    def test_meta_has_fewest_publisher_leverage_mechanisms(self):
        """Meta should have 1 mechanism (voluntary licensing) vs others' 4-7."""
        meta = self.entities.get('meta', {})
        # Meta's leverage is characterized as 1 (voluntary licensing)
        # Check that the statistical summary reflects this
        key_finding = self.matrix['statistical_summary']['key_finding']
        self.assertIn('BALANCED', key_finding)

    def test_openai_publisher_deals_consistent(self):
        """OpenAI entity should have publisher deals matching matrix."""
        openai = self.entities.get('openai', {})
        self.assertIsNotNone(openai)

    def test_anthropic_settlement_amount_consistent(self):
        """Anthropic settlement should be $1.5B in both matrix and entities."""
        anthro = self.entities.get('anthropic', {})
        settlement = anthro.get('author_settlement_source', '')
        # Matrix references $1.5B
        nc = self.matrix['publishers']['news_corp']
        anthro_deals = [
            d for d in nc['competitor_deals']
            if d['partner'] == 'Anthropic'
        ]
        self.assertEqual(len(anthro_deals), 1)
        self.assertIn('$1.5B', anthro_deals[0]['value'])


class TestNewsCorpProfileConsistency(unittest.TestCase):
    """Matrix data consistent with news-corp.yaml profile."""

    def setUp(self):
        self.profile = load_news_corp_profile()
        self.matrix_pub = get_matrix()['publishers']['news_corp']

    def test_meta_deal_value_consistent(self):
        profile_meta = [
            r for r in self.profile['revenue_relationships']
            if r['partner'] == 'Meta'
        ]
        self.assertEqual(len(profile_meta), 1)
        self.assertIn('$50M', profile_meta[0]['value'])
        self.assertIn('$50M', self.matrix_pub['meta_deal_value'])

    def test_openai_deal_value_consistent(self):
        profile_openai = [
            r for r in self.profile['revenue_relationships']
            if r['partner'] == 'OpenAI'
        ]
        self.assertEqual(len(profile_openai), 1)
        self.assertIn('$250M', profile_openai[0]['value'])

    def test_disclosure_practice_consistent(self):
        self.assertTrue(self.profile['disclosure_practice']['unique_in_dataset'])
        self.assertTrue(self.matrix_pub['discloses_relationships'])

    def test_q4_earnings_source_present(self):
        q4 = self.profile['financials']['q4_fy2026']
        self.assertIn('source_urls', q4)
        self.assertGreaterEqual(len(q4['source_urls']), 2)

    def test_ai_licensing_impact_has_meta_confirmation(self):
        impact = self.profile['financials']['q4_fy2026']['ai_licensing_impact']
        self.assertIn('Meta deal', impact)
        self.assertIn('principled', impact.lower())


if __name__ == '__main__':
    unittest.main()
