"""
Mechanism #184: SpaceX S-1 SEC-Filed Financial Architecture — X Ad Revenue ($1.8B)
+ Anthropic Colossus Compute ($45B) + Cross-Competitor Meta Adversarial Alignment

Type C: Financial Incentive Mapping — Aug 19, 2026 02:00 PM PT

CORE FINDING:

The SpaceX S-1 IPO filing (June 2026) is the FIRST SEC disclosure of both
X/Twitter's post-Musk financials AND the Anthropic compute deal terms, creating
the first verifiable primary-source evidence of a cross-competitor financial
architecture where money flowing between Meta's competitors (Anthropic → xAI/SpaceX)
strengthens a company (X/Twitter) that directly competes with Meta for advertising
revenue.

KEY S-1 DISCLOSURES:
1. Anthropic Colossus compute deal: $1.25B/month through May 2029, up to $45B total
2. X ad revenue 2025: $1.8B (down from $4.4B in 2022 pre-Musk, 59% decline)
3. xAI segment 2025 revenue: $3.2B, with $6.4B operating loss
4. X data as AI moat: ~350M daily posts as "proprietary access to real-time data inflows"
5. Colossus infrastructure economics: $2.7M/MW (4x industry improvement)

FINANCIAL CHAIN:
Anthropic success → $1.25B/month compute payments → xAI/SpaceX revenue →
X platform viability → X competes with Meta for ad dollars ($1.8B vs $243.46B)

NOVEL CONTRIBUTION:
First documentation using SEC-filed primary sources (SpaceX S-1) of a verified
cross-competitor financial flow where revenue from one Meta competitor (Anthropic)
funds another Meta competitor (xAI/X).

ASYMMETRY SCORE: 0.72 (lower because the publisher-incentive chain is indirect
and confounders are strong)

CONFOUNDERS: 5 (2 STRONG, 2 MODERATE, 1 WEAK)
CROSS-REFERENCES: #47, #140, #174
"""

import os
import unittest
import yaml


PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


class TestMechanism184Exists(unittest.TestCase):
    """Verify mechanism #184 exists in competitor-coverage-research.yaml with correct fields."""

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
            cls.data = yaml.safe_load(f)
        cls.cpf = cls.data.get('cross_publication_findings', {})

    def test_mechanism_184_exists_in_cross_publication_findings(self):
        """Mechanism #184 must exist in cross_publication_findings section."""
        self.assertIn('spacex_s1_cross_competitor_financial_architecture', self.cpf)

    def test_mechanism_id_is_184(self):
        m = self.cpf['spacex_s1_cross_competitor_financial_architecture']
        self.assertEqual(m['mechanism_id'], 184)

    def test_mechanism_type(self):
        m = self.cpf['spacex_s1_cross_competitor_financial_architecture']
        self.assertEqual(m['type'], 'financial_incentive_sec_verified_cross_competitor_chain')

    def test_date_added(self):
        m = self.cpf['spacex_s1_cross_competitor_financial_architecture']
        self.assertEqual(m['date_added'], '2026-08-19')

    def test_has_finding_summary(self):
        m = self.cpf['spacex_s1_cross_competitor_financial_architecture']
        self.assertIn('finding_summary', m)
        self.assertGreater(len(m['finding_summary']), 100)

    def test_has_primary_sources(self):
        m = self.cpf['spacex_s1_cross_competitor_financial_architecture']
        self.assertIn('primary_sources', m)
        self.assertGreaterEqual(len(m['primary_sources']), 3)

    def test_has_confounding_factors(self):
        m = self.cpf['spacex_s1_cross_competitor_financial_architecture']
        self.assertIn('confounding_factors', m)
        self.assertEqual(len(m['confounding_factors']), 5)

    def test_has_cross_references(self):
        m = self.cpf['spacex_s1_cross_competitor_financial_architecture']
        self.assertIn('cross_references', m)
        self.assertGreaterEqual(len(m['cross_references']), 3)


class TestSpaceXS1FinancialData(unittest.TestCase):
    """Verify S-1 financial data in xAI entity."""

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')) as f:
            cls.data = yaml.safe_load(f)
        cls.xai = cls.data['entities']['xai']

    def test_spacex_s1_financials_section_exists(self):
        self.assertIn('spacex_s1_financials', self.xai)

    def test_filing_date(self):
        self.assertEqual(self.xai['spacex_s1_financials']['filing_date'], '2026-06-12')

    def test_filing_type_is_s1(self):
        self.assertIn('S-1', self.xai['spacex_s1_financials']['filing_type'])

    def test_x_ad_revenue_2025(self):
        self.assertEqual(self.xai['spacex_s1_financials']['x_ad_revenue_2025_b'], 1.8)

    def test_x_ad_revenue_2022(self):
        self.assertEqual(self.xai['spacex_s1_financials']['x_ad_revenue_2022_b'], 4.4)

    def test_x_ad_revenue_decline_pct(self):
        self.assertEqual(self.xai['spacex_s1_financials']['x_ad_revenue_decline_pct'], 59)

    def test_x_daily_posts(self):
        self.assertEqual(self.xai['spacex_s1_financials']['x_daily_posts_m'], 350)

    def test_xai_segment_revenue(self):
        self.assertEqual(self.xai['spacex_s1_financials']['xai_segment_revenue_2025_b'], 3.2)

    def test_xai_segment_operating_loss(self):
        self.assertEqual(self.xai['spacex_s1_financials']['xai_segment_operating_loss_2025_b'], 6.4)

    def test_spacex_net_loss(self):
        self.assertEqual(self.xai['spacex_s1_financials']['spacex_net_loss_2025_b'], 4.94)

    def test_spacex_ipo_raised(self):
        self.assertEqual(self.xai['spacex_s1_financials']['spacex_ipo_raised_b'], 75)

    def test_spacex_valuation(self):
        self.assertEqual(self.xai['spacex_s1_financials']['spacex_valuation_t'], 1.75)

    def test_ai_term_frequency(self):
        self.assertEqual(self.xai['spacex_s1_financials']['ai_term_frequency_pct'], 47)

    def test_source_urls_exist(self):
        self.assertIn('source_urls', self.xai['spacex_s1_financials'])
        self.assertGreaterEqual(len(self.xai['spacex_s1_financials']['source_urls']), 3)


class TestAnthropicColossusDealTerms(unittest.TestCase):
    """Verify Anthropic Colossus compute deal terms in xAI entity."""

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')) as f:
            cls.data = yaml.safe_load(f)
        cls.deal = cls.data['entities']['xai']['anthropic_colossus_compute_deal']

    def test_deal_section_exists(self):
        self.assertIsNotNone(self.deal)

    def test_monthly_payment(self):
        self.assertEqual(self.deal['monthly_payment_b'], 1.25)

    def test_annual_payment(self):
        self.assertEqual(self.deal['annual_payment_b'], 15)

    def test_total_potential(self):
        self.assertEqual(self.deal['total_potential_b'], 45)

    def test_term_end(self):
        self.assertEqual(self.deal['term_end'], '2029-05')

    def test_termination_notice_days(self):
        self.assertEqual(self.deal['termination_notice_days'], 90)

    def test_facilities_location(self):
        self.assertIn('Memphis', self.deal['facilities'])

    def test_capacity_mw(self):
        self.assertEqual(self.deal['capacity_mw'], 300)

    def test_construction_cost_per_mw(self):
        self.assertEqual(self.deal['construction_cost_per_mw_m'], 2.7)

    def test_industry_benchmark_per_mw(self):
        self.assertEqual(self.deal['industry_benchmark_per_mw_m'], 10.8)

    def test_musk_contradiction_exists(self):
        self.assertIn('musk_contradiction', self.deal)
        self.assertIn('180 day lease', self.deal['musk_contradiction'])

    def test_source_urls(self):
        self.assertGreaterEqual(len(self.deal['source_urls']), 3)


class TestXMetaAdRevenueComparison(unittest.TestCase):
    """Verify Meta vs X ad revenue scale comparison."""

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')) as f:
            cls.data = yaml.safe_load(f)
        cls.xai = cls.data['entities']['xai']

    def test_x_ad_revenue_2025(self):
        self.assertEqual(self.xai['spacex_s1_financials']['x_ad_revenue_2025_b'], 1.8)

    def test_meta_is_135x_larger(self):
        """Meta $243.46B projected vs X $1.8B = ~135x."""
        x_rev = self.xai['spacex_s1_financials']['x_ad_revenue_2025_b']
        meta_rev = 243.46
        ratio = meta_rev / x_rev
        self.assertGreater(ratio, 130)
        self.assertLess(ratio, 140)

    def test_x_ad_revenue_declined_59_pct(self):
        s1 = self.xai['spacex_s1_financials']
        decline = ((s1['x_ad_revenue_2022_b'] - s1['x_ad_revenue_2025_b'])
                   / s1['x_ad_revenue_2022_b'] * 100)
        self.assertAlmostEqual(decline, 59, delta=1)

    def test_x_ad_revenue_decline_field_matches_calculation(self):
        s1 = self.xai['spacex_s1_financials']
        calculated = round(((s1['x_ad_revenue_2022_b'] - s1['x_ad_revenue_2025_b'])
                           / s1['x_ad_revenue_2022_b'] * 100))
        self.assertEqual(s1['x_ad_revenue_decline_pct'], calculated)


class TestPublisherDealZeroVerification(unittest.TestCase):
    """Verify xAI has zero publisher deals."""

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')) as f:
            cls.data = yaml.safe_load(f)
        cls.xai = cls.data['entities']['xai']

    def test_publisher_deals_note_exists(self):
        self.assertIn('publisher_deals_note', self.xai)

    def test_zero_publisher_deals_stated(self):
        note = self.xai['publisher_deals_note']
        self.assertIn('ZERO', note)

    def test_publisher_invisible_status(self):
        note = self.xai['publisher_deals_note']
        self.assertIn('publisher-invisible', note)

    def test_no_publisher_copyright_suits(self):
        note = self.xai['publisher_deals_note']
        self.assertIn('No publisher has sued xAI for copyright infringement', note)


class TestCrossCompetitorFinancialChain(unittest.TestCase):
    """Verify the Anthropic → xAI → X chain is fully documented."""

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
            cls.data = yaml.safe_load(f)
        cls.m = cls.data['cross_publication_findings']['spacex_s1_cross_competitor_financial_architecture']

    def test_entities_include_xai(self):
        self.assertIn('xai', self.m['entities'])

    def test_entities_include_anthropic(self):
        self.assertIn('anthropic', self.m['entities'])

    def test_entities_include_meta(self):
        self.assertIn('meta', self.m['entities'])

    def test_finding_mentions_colossus(self):
        self.assertIn('Colossus', self.m['finding_summary'])

    def test_finding_mentions_1_25b_monthly(self):
        self.assertIn('$1.25B/month', self.m['finding_summary'])

    def test_finding_mentions_45b_total(self):
        self.assertIn('$45B total', self.m['finding_summary'])

    def test_finding_mentions_x_ad_revenue(self):
        self.assertIn('$1.8B', self.m['finding_summary'])

    def test_finding_mentions_sec_primary_source(self):
        self.assertIn('SEC', self.m['finding_summary'])

    def test_finding_mentions_zero_publisher_deals(self):
        self.assertIn('ZERO publisher content licensing deals', self.m['finding_summary'])

    def test_primary_sources_reference_s1_pages(self):
        pages_source = [s for s in self.m['primary_sources'] if 'pages 13' in s]
        self.assertGreaterEqual(len(pages_source), 1)


class TestConfoundingFactors(unittest.TestCase):
    """Verify 5 confounders with at least 2 STRONG."""

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
            cls.data = yaml.safe_load(f)
        cls.m = cls.data['cross_publication_findings']['spacex_s1_cross_competitor_financial_architecture']
        cls.confounders = cls.m['confounding_factors']

    def test_exactly_5_confounders(self):
        self.assertEqual(len(self.confounders), 5)

    def test_at_least_2_strong(self):
        strong = [c for c in self.confounders if c['strength'] == 'STRONG']
        self.assertGreaterEqual(len(strong), 2)

    def test_at_least_1_moderate(self):
        moderate = [c for c in self.confounders if c['strength'] == 'MODERATE']
        self.assertGreaterEqual(len(moderate), 1)

    def test_at_least_1_weak(self):
        weak = [c for c in self.confounders if c['strength'] == 'WEAK']
        self.assertGreaterEqual(len(weak), 1)

    def test_each_confounder_has_description(self):
        for c in self.confounders:
            self.assertIn('description', c)
            self.assertGreater(len(c['description']), 20)


class TestCrossReferences(unittest.TestCase):
    """Verify cross-references to mechanisms 47, 140, 174."""

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
            cls.data = yaml.safe_load(f)
        cls.m = cls.data['cross_publication_findings']['spacex_s1_cross_competitor_financial_architecture']
        cls.refs = cls.m['cross_references']

    def test_at_least_3_cross_references(self):
        self.assertGreaterEqual(len(self.refs), 3)

    def test_mechanism_47_referenced(self):
        ids = [r['mechanism_id'] for r in self.refs]
        self.assertIn(47, ids)

    def test_mechanism_140_referenced(self):
        ids = [r['mechanism_id'] for r in self.refs]
        self.assertIn(140, ids)

    def test_mechanism_174_referenced(self):
        ids = [r['mechanism_id'] for r in self.refs]
        self.assertIn(174, ids)

    def test_each_reference_has_relationship(self):
        for r in self.refs:
            self.assertIn('relationship', r)

    def test_each_reference_has_description(self):
        for r in self.refs:
            self.assertIn('description', r)
            self.assertGreater(len(r['description']), 20)


class TestAsymmetryScore(unittest.TestCase):
    """Verify asymmetry score is 0.72 and within valid range."""

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
            cls.data = yaml.safe_load(f)
        cls.m = cls.data['cross_publication_findings']['spacex_s1_cross_competitor_financial_architecture']

    def test_asymmetry_score_is_0_72(self):
        self.assertEqual(self.m['asymmetry_score'], 0.72)

    def test_score_within_valid_range(self):
        score = self.m['asymmetry_score']
        self.assertGreaterEqual(score, 0.5)
        self.assertLessEqual(score, 1.0)

    def test_score_is_float(self):
        self.assertIsInstance(self.m['asymmetry_score'], float)


class TestSourceURLs(unittest.TestCase):
    """Verify source URLs are present and valid."""

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
            cls.data = yaml.safe_load(f)
        cls.m = cls.data['cross_publication_findings']['spacex_s1_cross_competitor_financial_architecture']

    def test_at_least_4_source_urls(self):
        self.assertGreaterEqual(len(self.m['source_urls']), 4)

    def test_all_urls_start_with_https(self):
        for url in self.m['source_urls']:
            self.assertTrue(url.startswith('https://'), f"URL does not start with https: {url}")

    def test_techcrunch_url_present(self):
        tc_urls = [u for u in self.m['source_urls'] if 'techcrunch.com' in u]
        self.assertGreaterEqual(len(tc_urls), 1)

    def test_morningstar_url_present(self):
        ms_urls = [u for u in self.m['source_urls'] if 'morningstar.com' in u]
        self.assertGreaterEqual(len(ms_urls), 1)

    def test_socialmediatoday_url_present(self):
        smt_urls = [u for u in self.m['source_urls'] if 'socialmediatoday.com' in u]
        self.assertGreaterEqual(len(smt_urls), 1)

    def test_at_least_6_source_urls(self):
        self.assertGreaterEqual(len(self.m['source_urls']), 6)


if __name__ == '__main__':
    unittest.main()
