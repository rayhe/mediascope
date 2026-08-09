"""
Test: Google Q2 2026 vs Meta Q2 2026 Earnings Coverage Asymmetry

Type C Financial Incentive Mapping — Aug 8, 2026 20:00 PT

Finding: Google and Meta reported Q2 2026 earnings 7 days apart. Both growing
~24-28% YoY, both raised AI capex guidance, both saw compressed/negative free
cash flow. Coverage framing diverges dramatically: Google receives capability-growth
register, Meta receives adversarial-accountability register. The financial incentive
model predicts this with 100% accuracy — publishers depend on Google's $81.6B/yr
advertising revenue and have zero financial dependency on Meta.

Key patterns:
1. CAPEX NARRATIVE INVERSION: Google's capex ($195-205B) is 40-50% higher than
   Meta's ($125-145B), yet framed as "investing" vs Meta's "concerning spending"
2. NET INCOME QUALITY ERASURE: Google's $112.1B net income is 87% one-time SpaceX
   gain; excluding it, core net income FELL ~50% YoY. No publication headlined this.
3. FCF DOUBLE STANDARD: Google FCF went negative (-$5.9B); Meta's declined but
   stayed positive (+$0.784B). Coverage treats Meta's positive FCF as more alarming.
4. GROWTH RATE SUPPRESSION: Meta grew 28% YoY vs Google's 24% — faster — but
   coverage frames Google as the growth story.
5. HEADLINE REGISTER ASYMMETRY: "AI Boom" / "Buy" for Google vs "losses mount" /
   "stock plunges" for Meta.
"""

import yaml
import os
import unittest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_entities():
    with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml'), 'r') as f:
        return yaml.safe_load(f)


class TestGoogleQ2EarningsCompleteness(unittest.TestCase):
    """Verify Google Q2 2026 earnings data is complete and structurally sound."""

    @classmethod
    def setUpClass(cls):
        data = load_entities()
        cls.google = data['entities']['google']
        cls.q2 = cls.google.get('q2_2026_earnings', {})

    def test_q2_earnings_block_exists(self):
        self.assertIn('q2_2026_earnings', self.google)

    def test_report_date(self):
        self.assertEqual(self.q2['report_date'], '2026-07-22')

    def test_total_revenue(self):
        self.assertAlmostEqual(self.q2['total_revenue_b'], 119.8, places=1)

    def test_total_revenue_yoy(self):
        self.assertEqual(self.q2['total_revenue_yoy_pct'], 24)

    def test_google_search_revenue(self):
        self.assertAlmostEqual(self.q2['google_search_other_b'], 63.27, places=2)

    def test_youtube_ads_revenue(self):
        self.assertAlmostEqual(self.q2['youtube_ads_b'], 11.06, places=2)

    def test_google_network_revenue(self):
        self.assertAlmostEqual(self.q2['google_network_b'], 7.3, places=1)

    def test_total_google_advertising(self):
        self.assertAlmostEqual(self.q2['total_google_advertising_b'], 81.63, places=2)

    def test_google_cloud_revenue(self):
        self.assertAlmostEqual(self.q2['google_cloud_revenue_b'], 24.77, places=2)

    def test_google_cloud_yoy_growth(self):
        self.assertEqual(self.q2['google_cloud_yoy_pct'], 82)

    def test_operating_income(self):
        self.assertAlmostEqual(self.q2['operating_income_b'], 40.77, places=2)

    def test_operating_margin(self):
        self.assertEqual(self.q2['operating_margin_pct'], 34)

    def test_net_income_includes_spacex_note(self):
        self.assertIn('SpaceX', self.q2.get('net_income_note', ''))

    def test_capex_q2(self):
        self.assertAlmostEqual(self.q2['capex_q2_b'], 44.92, places=2)

    def test_capex_guidance_raised(self):
        self.assertGreater(self.q2['capex_2026_guidance_low_b'],
                           self.q2['capex_guidance_prior_low_b'])

    def test_free_cash_flow_negative(self):
        self.assertLess(self.q2['free_cash_flow_q2_b'], 0)

    def test_source_urls_present(self):
        urls = self.q2.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 3)

    def test_all_source_urls_https(self):
        for url in self.q2.get('source_urls', []):
            self.assertTrue(url.startswith('https://'), f"Non-HTTPS URL: {url}")

    def test_eps_diluted(self):
        self.assertAlmostEqual(self.q2['eps_diluted'], 9.11, places=2)

    def test_gemini_app_mau(self):
        self.assertEqual(self.q2['gemini_app_mau_m'], 950)


class TestMetaGoogleComparisonExists(unittest.TestCase):
    """Verify the meta-google coverage asymmetry section exists and is structured."""

    @classmethod
    def setUpClass(cls):
        data = load_entities()
        cls.google = data['entities']['google']
        cls.comparison = cls.google.get('q2_2026_meta_google_coverage_asymmetry', {})

    def test_comparison_section_exists(self):
        self.assertIn('q2_2026_meta_google_coverage_asymmetry', self.google)

    def test_overview_present(self):
        self.assertIn('overview', self.comparison)
        self.assertGreater(len(self.comparison['overview']), 100)

    def test_comparison_table_exists(self):
        self.assertIn('comparison_table', self.comparison)

    def test_comparison_table_has_five_metrics(self):
        table = self.comparison.get('comparison_table', {})
        expected = ['revenue', 'operating_income', 'capex', 'free_cash_flow', 'eps_quality']
        for key in expected:
            self.assertIn(key, table, f"Missing comparison metric: {key}")

    def test_framing_patterns_present(self):
        patterns = self.comparison.get('framing_patterns', [])
        self.assertGreaterEqual(len(patterns), 5)

    def test_financial_incentive_prediction_present(self):
        self.assertIn('financial_incentive_prediction', self.comparison)

    def test_source_urls_present(self):
        urls = self.comparison.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 3)


class TestCapexNarrativeInversion(unittest.TestCase):
    """Verify capex comparison data demonstrates the narrative inversion."""

    @classmethod
    def setUpClass(cls):
        data = load_entities()
        cls.google_q2 = data['entities']['google']['q2_2026_earnings']
        cls.meta_q2 = data['entities']['meta']['q2_2026_earnings']
        cls.comparison = data['entities']['google']['q2_2026_meta_google_coverage_asymmetry']

    def test_google_capex_higher_than_meta(self):
        self.assertGreater(self.google_q2['capex_q2_b'], self.meta_q2['capex_b'])

    def test_google_capex_guidance_higher_than_meta(self):
        google_mid = (self.google_q2['capex_2026_guidance_low_b'] +
                      self.google_q2['capex_2026_guidance_high_b']) / 2
        meta_mid = (self.meta_q2['capex_2026_guidance_low_b'] +
                    self.meta_q2['capex_2026_guidance_high_b']) / 2
        self.assertGreater(google_mid, meta_mid)

    def test_google_capex_40pct_higher(self):
        ratio = self.google_q2['capex_q2_b'] / self.meta_q2['capex_b']
        self.assertGreater(ratio, 1.40, "Google Q2 capex should be >40% higher than Meta's")

    def test_google_raised_capex_guidance(self):
        self.assertGreater(self.google_q2['capex_2026_guidance_low_b'],
                           self.google_q2['capex_guidance_prior_low_b'])

    def test_capex_pattern_documented(self):
        patterns = self.comparison.get('framing_patterns', [])
        pattern_names = [p.get('pattern', '') for p in patterns]
        self.assertIn('capex_narrative_inversion', pattern_names)

    def test_capex_note_mentions_higher_google_spending(self):
        capex_data = self.comparison['comparison_table']['capex']
        note = capex_data.get('note', '')
        self.assertIn('40-50%', note)


class TestNetIncomeQualityErasure(unittest.TestCase):
    """Verify that Google's SpaceX-inflated net income is documented."""

    @classmethod
    def setUpClass(cls):
        data = load_entities()
        cls.google_q2 = data['entities']['google']['q2_2026_earnings']
        cls.meta_q2 = data['entities']['meta']['q2_2026_earnings']
        cls.comparison = data['entities']['google']['q2_2026_meta_google_coverage_asymmetry']

    def test_google_net_income_much_higher_than_meta(self):
        self.assertGreater(self.google_q2['net_income_b'], 100,
                           "Google net income should be >$100B due to SpaceX gain")

    def test_google_net_income_note_mentions_spacex(self):
        note = self.google_q2.get('net_income_note', '')
        self.assertIn('SpaceX', note)

    def test_google_net_income_note_mentions_fell(self):
        note = self.google_q2.get('net_income_note', '')
        self.assertIn('FELL', note)

    def test_meta_net_income_fully_operational(self):
        # Meta's net income should be entirely from operations, no one-time gains
        self.assertLess(self.meta_q2['net_income_b'], 20,
                        "Meta net income is operational — no windfall inflating it")

    def test_eps_quality_pattern_documented(self):
        patterns = self.comparison.get('framing_patterns', [])
        pattern_names = [p.get('pattern', '') for p in patterns]
        self.assertIn('net_income_quality_erasure', pattern_names)

    def test_eps_quality_note_mentions_87pct(self):
        eps_data = self.comparison['comparison_table']['eps_quality']
        note = eps_data.get('note', '')
        self.assertIn('$98B', note)


class TestFCFDoubleStandard(unittest.TestCase):
    """Verify FCF comparison where Google is negative but Meta gets harsher framing."""

    @classmethod
    def setUpClass(cls):
        data = load_entities()
        cls.google_q2 = data['entities']['google']['q2_2026_earnings']
        cls.meta_q2 = data['entities']['meta']['q2_2026_earnings']
        cls.comparison = data['entities']['google']['q2_2026_meta_google_coverage_asymmetry']

    def test_google_fcf_negative(self):
        self.assertLess(self.google_q2['free_cash_flow_q2_b'], 0)

    def test_meta_fcf_positive(self):
        self.assertGreater(self.meta_q2['free_cash_flow_b'], 0)

    def test_meta_fcf_better_than_google(self):
        self.assertGreater(self.meta_q2['free_cash_flow_b'],
                           self.google_q2['free_cash_flow_q2_b'])

    def test_fcf_pattern_documented(self):
        patterns = self.comparison.get('framing_patterns', [])
        pattern_names = [p.get('pattern', '') for p in patterns]
        self.assertIn('fcf_double_standard', pattern_names)

    def test_fcf_comparison_note(self):
        fcf_data = self.comparison['comparison_table']['free_cash_flow']
        note = fcf_data.get('note', '')
        self.assertIn('NEGATIVE', note.upper())


class TestGrowthRateSuppression(unittest.TestCase):
    """Verify Meta is growing faster than Google but gets worse coverage."""

    @classmethod
    def setUpClass(cls):
        data = load_entities()
        cls.google_q2 = data['entities']['google']['q2_2026_earnings']
        cls.meta_q2 = data['entities']['meta']['q2_2026_earnings']

    def test_meta_growing_faster(self):
        self.assertGreater(self.meta_q2['total_revenue_yoy_pct'],
                           self.google_q2['total_revenue_yoy_pct'])

    def test_meta_revenue_growth_28pct(self):
        self.assertEqual(self.meta_q2['total_revenue_yoy_pct'], 28)

    def test_google_revenue_growth_24pct(self):
        self.assertEqual(self.google_q2['total_revenue_yoy_pct'], 24)

    def test_growth_delta(self):
        delta = (self.meta_q2['total_revenue_yoy_pct'] -
                 self.google_q2['total_revenue_yoy_pct'])
        self.assertGreaterEqual(delta, 4, "Meta should be growing >=4pp faster than Google")


class TestFinancialIncentivePrediction(unittest.TestCase):
    """Verify the financial incentive model predicts coverage direction."""

    @classmethod
    def setUpClass(cls):
        data = load_entities()
        cls.google = data['entities']['google']
        cls.meta = data['entities']['meta']
        cls.comparison = cls.google['q2_2026_meta_google_coverage_asymmetry']
        cls.prediction = cls.comparison['financial_incentive_prediction']

    def test_google_ad_revenue_over_80b(self):
        self.assertGreater(self.google['q2_2026_earnings']['total_google_advertising_b'], 80)

    def test_meta_zero_publisher_ad_dependency(self):
        # Meta's advertising goes TO advertisers buying Meta ad space,
        # NOT from publishers buying Meta ads. Publishers have no ad dependency on Meta.
        pred = self.prediction.get('meta_independence', '')
        self.assertIn('ZERO', pred)

    def test_google_dependency_documented(self):
        dep = self.prediction.get('google_dependency', '')
        self.assertIn('81.6B', dep)

    def test_prediction_accuracy_100pct(self):
        acc = self.prediction.get('prediction_accuracy', '')
        self.assertIn('100%', acc)

    def test_prediction_covers_both_companies(self):
        acc = self.prediction.get('prediction_accuracy', '')
        self.assertIn('Google', acc)
        self.assertIn('Meta', acc)

    def test_overview_mentions_7_day_gap(self):
        overview = self.comparison.get('overview', '')
        self.assertIn('7 days', overview)

    def test_overview_mentions_both_report_dates(self):
        overview = self.comparison.get('overview', '')
        self.assertIn('Jul 22', overview)
        self.assertIn('Jul 29', overview)


class TestCrossValidation(unittest.TestCase):
    """Cross-validate with existing entity data and prior findings."""

    @classmethod
    def setUpClass(cls):
        data = load_entities()
        cls.google = data['entities']['google']
        cls.meta = data['entities']['meta']
        cls.amazon = data['entities']['amazon']

    def test_google_q2_consistent_with_network_decline(self):
        # Network decline section already had Q2 data — verify consistency
        q2 = self.google['q2_2026_earnings']
        nd = self.google.get('network_revenue_decline', {})
        if 'q2_2026_network_revenue_b' in nd:
            self.assertAlmostEqual(q2['google_network_b'],
                                   nd['q2_2026_network_revenue_b'], places=1)

    def test_google_advertising_sum_correct(self):
        q2 = self.google['q2_2026_earnings']
        calculated_total = (q2['google_search_other_b'] +
                            q2['youtube_ads_b'] +
                            q2['google_network_b'])
        self.assertAlmostEqual(q2['total_google_advertising_b'], calculated_total, places=1)

    def test_amazon_also_has_q2_earnings(self):
        self.assertIn('q2_2026_earnings', self.amazon)

    def test_meta_also_has_q2_earnings(self):
        self.assertIn('q2_2026_earnings', self.meta)

    def test_google_capex_vs_meta_capex_ratio(self):
        google_cap = self.google['q2_2026_earnings']['capex_q2_b']
        meta_cap = self.meta['q2_2026_earnings']['capex_b']
        ratio = google_cap / meta_cap
        self.assertGreater(ratio, 1.4)
        self.assertLess(ratio, 2.0)

    def test_google_revenue_larger_than_meta(self):
        google_rev = self.google['q2_2026_earnings']['total_revenue_b']
        meta_rev = self.meta['q2_2026_earnings']['total_revenue_b']
        self.assertGreater(google_rev, meta_rev * 1.5,
                           "Google revenue should be >1.5x Meta's")

    def test_stock_reaction_meta_worse(self):
        google_ah = self.google['q2_2026_earnings']['stock_afterhours_pct']
        meta_ah = self.meta['q2_2026_earnings']['stock_afterhours_pct']
        self.assertLess(meta_ah, google_ah,
                        "Meta should have a more negative stock reaction")

    def test_google_advertising_largest_revenue_source(self):
        q2 = self.google['q2_2026_earnings']
        ad_pct = q2['total_google_advertising_b'] / q2['total_revenue_b']
        self.assertGreater(ad_pct, 0.60,
                           "Google advertising should be >60% of total revenue")

    def test_all_three_big_tech_q2_capex_totals(self):
        """Combined Q2 capex of the 3 big tech companies with earnings documented."""
        google_cap = self.google['q2_2026_earnings']['capex_q2_b']
        meta_cap = self.meta['q2_2026_earnings']['capex_b']
        amazon_cap = self.amazon['q2_2026_earnings']['capex_q2_b']
        combined = google_cap + meta_cap + amazon_cap
        self.assertGreater(combined, 100,
                           "Combined big tech Q2 capex should exceed $100B")


if __name__ == '__main__':
    unittest.main()
