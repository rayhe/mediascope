"""
Type C (10:00 PT Aug 8 2026): Meta Q2 2026 Earnings + Anthropic Compute Deal +
Inverse Financial Leverage Paradox

Tests validating Meta's entity profile expansion:
1. Q2 2026 earnings data completeness and accuracy
2. Anthropic compute deal documentation
3. Inverse financial leverage model — Meta has simplest publisher relationship
   (1 mechanism) yet receives harshest coverage
4. Comparison table consistency with other entities' documented mechanisms
5. Source URL presence for all claims

Primary sources:
- Meta Q2 2026 press release: https://www.prnewswire.com/news-releases/meta-reports-second-quarter-2026-results-302838214.html
- Reuters Meta-Anthropic: https://www.reuters.com/technology/meta-talks-10-billion-anthropic-compute-deal-nyt-reports-2026-07-17/
- Reuters Meta publisher deals: https://www.reuters.com/business/meta-strikes-multiple-ai-deals-with-news-publishers-axios-reports-2025-12-05/
"""
import unittest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_entities():
    path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


class TestMetaQ2_2026Earnings(unittest.TestCase):
    """Validate Meta Q2 2026 earnings data in entity profile."""

    @classmethod
    def setUpClass(cls):
        data = load_competitor_entities()
        cls.meta = data['entities']['meta']
        cls.q2 = cls.meta.get('q2_2026_earnings', {})

    def test_q2_earnings_section_exists(self):
        """Meta entity must have q2_2026_earnings section."""
        self.assertIn('q2_2026_earnings', self.meta)

    def test_report_date(self):
        self.assertEqual(self.q2['report_date'], '2026-07-29')

    def test_total_revenue(self):
        """Total revenue $60.8B — from Meta press release."""
        self.assertAlmostEqual(self.q2['total_revenue_b'], 60.8, places=1)

    def test_total_revenue_yoy(self):
        """Revenue grew 28% YoY."""
        self.assertEqual(self.q2['total_revenue_yoy_pct'], 28)

    def test_advertising_revenue(self):
        """Advertising revenue $59.363B."""
        self.assertAlmostEqual(self.q2['advertising_revenue_b'], 59.363, places=2)

    def test_reality_labs_revenue(self):
        """RL revenue $431M, driven by AI glasses."""
        self.assertAlmostEqual(self.q2['rl_revenue_b'], 0.431, places=3)

    def test_reality_labs_loss(self):
        """RL operating loss $4.619B — record quarter."""
        self.assertAlmostEqual(self.q2['rl_operating_loss_b'], 4.619, places=3)

    def test_rl_cumulative_loss(self):
        """Cumulative RL losses since Q4 2020 approaching $88B."""
        self.assertGreaterEqual(self.q2['rl_cumulative_loss_since_q4_2020_b'], 85)

    def test_eps_miss(self):
        """First EPS miss in 13 quarters — $6.18 vs consensus."""
        self.assertAlmostEqual(self.q2['eps_diluted'], 6.18, places=2)

    def test_capex(self):
        """Q2 capex $31.08B."""
        self.assertAlmostEqual(self.q2['capex_b'], 31.08, places=1)

    def test_capex_guidance_range(self):
        """2026 capex guidance $125-145B."""
        self.assertEqual(self.q2['capex_2026_guidance_low_b'], 125)
        self.assertEqual(self.q2['capex_2026_guidance_high_b'], 145)

    def test_free_cash_flow_collapse(self):
        """FCF collapsed 91% YoY to $784M."""
        self.assertAlmostEqual(self.q2['free_cash_flow_b'], 0.784, places=3)
        self.assertEqual(self.q2['free_cash_flow_yoy_decline_pct'], 91)

    def test_foa_other_revenue_milestone(self):
        """FoA other revenue hit $1B for first time (WhatsApp)."""
        self.assertGreaterEqual(self.q2['foa_other_revenue_b'], 1.0)

    def test_headcount(self):
        """Headcount 75,472 after May 2026 reduction."""
        self.assertEqual(self.q2['headcount'], 75472)

    def test_source_urls_present(self):
        """Must have source URLs for earnings data."""
        urls = self.q2.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 1)
        self.assertTrue(any('prnewswire.com' in u for u in urls),
                        "Must include Meta's official press release")

    def test_stock_afterhours_reaction(self):
        """Stock dropped 8.6% after hours."""
        self.assertAlmostEqual(self.q2['stock_afterhours_pct'], -8.6, places=1)


class TestMetaAnthropicComputeDeal(unittest.TestCase):
    """Validate Meta-Anthropic $10B compute deal documentation."""

    @classmethod
    def setUpClass(cls):
        data = load_competitor_entities()
        cls.meta = data['entities']['meta']
        cls.deal = cls.meta.get('anthropic_compute_deal', {})

    def test_deal_section_exists(self):
        self.assertIn('anthropic_compute_deal', self.meta)

    def test_deal_status_early_talks(self):
        """Deal is in early talks, not confirmed."""
        self.assertEqual(self.deal['status'], 'early_talks')

    def test_reported_value(self):
        """Reported potential value $10B."""
        self.assertEqual(self.deal['reported_value_b'], 10)

    def test_term_years(self):
        """Two-year proposed term."""
        self.assertEqual(self.deal['term_years'], 2)

    def test_early_exit_clause(self):
        """Both parties can exit early."""
        self.assertTrue(self.deal['early_exit_clause'])

    def test_proposed_by_anthropic(self):
        """Anthropic proposed the deal in June 2026."""
        self.assertIn('Anthropic', self.deal['proposed_by'])

    def test_mediascope_relevance_documents_publisher_neutral(self):
        """Analysis must note that Meta-Anthropic axis is publisher-neutral."""
        relevance = self.deal.get('mediascope_relevance', '')
        self.assertIn('ZERO publisher', relevance.lower() if not relevance else relevance)

    def test_source_urls_include_reuters(self):
        """Must cite Reuters or NYT as primary source."""
        urls = self.deal.get('source_urls', [])
        self.assertTrue(any('reuters.com' in u for u in urls))

    def test_overview_mentions_cloud_entry(self):
        """Overview must discuss Meta's entry into cloud computing."""
        overview = self.deal.get('overview', '')
        self.assertIn('cloud', overview.lower())


class TestMetaInverseFinancialLeverage(unittest.TestCase):
    """Validate the Inverse Financial Leverage Paradox analysis."""

    @classmethod
    def setUpClass(cls):
        data = load_competitor_entities()
        cls.meta = data['entities']['meta']
        cls.leverage = cls.meta.get('inverse_financial_leverage', {})
        cls.entities = data['entities']

    def test_inverse_leverage_section_exists(self):
        self.assertIn('inverse_financial_leverage', self.meta)

    def test_mechanism_count_is_one(self):
        """Meta has exactly 1 publisher financial mechanism."""
        self.assertEqual(self.leverage['mechanism_count'], 1)

    def test_mechanism_is_voluntary_licensing(self):
        """The single mechanism is voluntary AI content licensing."""
        self.assertEqual(self.leverage['mechanism_name'], 'voluntary_ai_content_licensing')

    def test_comparison_table_exists(self):
        """Must have a comparison table of mechanism counts."""
        table = self.leverage.get('comparison_table', {})
        self.assertGreaterEqual(len(table), 5)

    def test_comparison_table_ordering(self):
        """Microsoft (7) > Amazon (6) > Apple (5) > Google (4) > Meta (1)."""
        table = self.leverage['comparison_table']
        self.assertGreater(table['microsoft'], table['amazon'])
        self.assertGreater(table['amazon'], table['apple'])
        self.assertGreater(table['apple'], table['google'])
        self.assertGreater(table['google'], table['meta'])

    def test_meta_lower_than_all_others(self):
        """Meta's mechanism count is lower than all other big tech."""
        table = self.leverage['comparison_table']
        for entity in ['microsoft', 'amazon', 'apple', 'google']:
            self.assertGreater(table[entity], table['meta'],
                               f"Meta should have fewer mechanisms than {entity}")

    def test_mechanisms_meta_lacks_documented(self):
        """Must document specific mechanisms Meta lacks."""
        lacks = self.leverage.get('mechanisms_meta_lacks', {})
        # Handle both dict and list-of-dicts YAML structures
        if isinstance(lacks, list):
            all_keys = set()
            for item in lacks:
                if isinstance(item, dict):
                    all_keys.update(item.keys())
        else:
            all_keys = set(lacks.keys())
        expected = ['cloud_hosting', 'advertising_platform_for_publishers',
                    'content_marketplace', 'ownership_of_newspapers',
                    'search_traffic_dependency']
        for mechanism in expected:
            self.assertIn(mechanism, all_keys,
                          f"Missing documentation of Meta lacking: {mechanism}")

    def test_inverse_correlation_finding_present(self):
        """Must have the inverse correlation finding."""
        finding = self.leverage.get('inverse_correlation_finding', '')
        self.assertIn('inverse', finding.lower())

    def test_source_urls_present(self):
        """Must cite sources for deal portfolio claims."""
        urls = self.leverage.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 1)


class TestMetaVsCompetitorEntityParity(unittest.TestCase):
    """Validate Meta entity profile is now at parity with competitors."""

    @classmethod
    def setUpClass(cls):
        data = load_competitor_entities()
        cls.entities = data['entities']
        cls.meta = cls.entities['meta']

    def test_meta_has_earnings_like_amazon(self):
        """Meta entity now has Q2 2026 earnings like Amazon."""
        self.assertIn('q2_2026_earnings', self.meta)
        amazon = self.entities.get('amazon', {})
        self.assertIn('q2_2026_earnings', amazon)

    def test_meta_has_earnings_like_microsoft(self):
        """Meta entity now has earnings data like Microsoft."""
        self.assertIn('q2_2026_earnings', self.meta)
        microsoft = self.entities.get('microsoft', {})
        self.assertIn('fy26_q4_earnings', microsoft)

    def test_meta_earnings_has_key_fields(self):
        """Meta earnings must have the same key fields as Amazon's."""
        q2 = self.meta['q2_2026_earnings']
        required = ['report_date', 'total_revenue_b', 'total_revenue_yoy_pct',
                     'advertising_revenue_b', 'capex_b', 'source_urls']
        for field in required:
            self.assertIn(field, q2, f"Meta Q2 earnings missing field: {field}")

    def test_all_eleven_entities_present(self):
        """All 11 tracked entities must still be present."""
        expected = ['openai', 'anthropic', 'amazon', 'apple', 'google',
                    'x_twitter', 'meta', 'xai', 'samsung', 'microsoft', 'snowflake']
        for entity in expected:
            self.assertIn(entity, self.entities,
                          f"Entity {entity} missing from competitor-entities.yaml")


class TestMetaPublisherDealPortfolioIntegrity(unittest.TestCase):
    """Cross-validate Meta deal portfolio in meta_ai_deals section."""

    @classmethod
    def setUpClass(cls):
        data = load_competitor_entities()
        cls.meta_deals = data.get('meta_ai_deals', {})
        cls.meta_entity = data['entities']['meta']

    def test_meta_ai_deals_section_exists(self):
        """Top-level meta_ai_deals section must exist."""
        self.assertTrue(bool(self.meta_deals))

    def test_partner_count_at_least_13(self):
        """Meta has at least 13 known AI content partners."""
        partners = self.meta_deals.get('partners', [])
        self.assertGreaterEqual(len(partners), 13)

    def test_news_corp_is_largest_disclosed(self):
        """News Corp ($50M/yr) must be identified as largest disclosed deal."""
        partners = self.meta_deals.get('partners', [])
        news_corp = [p for p in partners if 'News Corp' in p.get('name', '')]
        self.assertTrue(news_corp, "News Corp must be in partner list")
        self.assertIn('50M', news_corp[0].get('terms', ''))

    def test_excluded_publishers_documented(self):
        """Must document which MediaScope publications are excluded."""
        excluded = self.meta_deals.get('excluded_publishers', [])
        self.assertGreaterEqual(len(excluded), 4)

    def test_no_mediascope_profiled_publication_has_meta_deal(self):
        """None of the 7 profiled publications should have Meta deals."""
        excluded = self.meta_deals.get('excluded_publishers', [])
        for pub in excluded:
            self.assertEqual(pub.get('meta_deal', 'none'), 'none',
                             f"{pub.get('name', 'unknown')} should not have Meta deal")


if __name__ == '__main__':
    unittest.main()
