"""
Mechanism #216: Conde Nast Meta-Origin CBO France + Snap Q2 2026 Financial Foundation —
Reverse Personnel Flow & Spectacles Launch Financial Architecture

Type C: Financial Incentive Mapping
Discovery Date: 2026-08-21
Iteration: #225

TWO FINANCIAL ARCHITECTURE UPDATES:

1. CONDE NAST META REVERSE PERSONNEL FLOW:

Violaine Gressier, formerly Meta's Global Head of Luxury, joined Conde Nast France
as Chief Business Officer effective June 22, 2026. She reports to CRO Elizabeth
Herbst-Brady (ex-Snap). This is the FIRST documented reverse personnel flow from
Meta to Conde Nast, updating the "zero Meta personnel ties" claim in mechanism #208.

Key financial implications:
- Gressier managed luxury brand partnerships at Meta — same brands advertising in
  Vogue France, GQ, Vanity Fair, AD
- She now controls revenue for those properties, with a mandate to "accelerate
  revenue growth" — potentially redirecting luxury budgets FROM Meta TO Conde Nast
- She contributes to Conde Nast's Global Fashion & Luxury agenda, meaning her
  Meta-origin knowledge influences not just French but GLOBAL luxury ad strategy
- Reports to Herbst-Brady (ex-Snap) → Lynch (CEO): the revenue chain from French
  luxury through ex-Snap CRO creates a compound personnel-financial nexus

The net incentive effect is AMBIGUOUS (scored 0.45): Gressier may bring personal
goodwill toward Meta (softening coverage), OR may leverage insider knowledge to
compete more effectively for luxury ad budgets (sharpening the adversarial incentive).
This ambiguity itself is analytically valuable — it's the first mechanism in MediaScope
where the direction of incentive is genuinely uncertain rather than structurally clear.

Source: https://fashionunited.uk/news/people/former-meta-executive-violaine-gressier-joins-conde-nast-france/2026060388396

2. SNAP Q2 2026 COMPREHENSIVE FINANCIAL DATA UPDATE:

Snap reported Q2 2026 on August 3, 2026, revealing a financial inflection point
that fundamentally changes the Spectacles September 16 launch calculus:

- Total revenue: $1,599M (+19% YoY)
- Advertising revenue: $1,283M (+9% YoY)
- Other revenue: $316M (+85% YoY) — Snapchat+, Memories, Lens+
- Adjusted EBITDA: $249.6M (vs $41.3M prior year — 505% YoY)
- Free cash flow: $120.5M (vs $24M — 402% YoY)
- MAU: 971M, DAU: 493M
- Gross margin: 58%
- Restructuring charges: $128.5M (April 2026 layoffs, ~1,000 jobs)
- Q3 guidance: $1.70-$1.74B revenue, $300-350M EBITDA
- Spectacles September 16 consumer launch confirmed on earnings call

The EBITDA explosion validates Snap's financial viability at the exact moment
it launches consumer Spectacles ($2,195). Publications reviewing Spectacles
review a product from a financially IMPROVING company with 971M MAU — not
a company in distress. Compare to Meta's Q2 2026: $60.8B revenue but EPS miss,
-8.6% after-hours, $4.619B RL loss. Publication framing predictably follows
financial trajectory: Snap's trajectory invites "turnaround" narratives while
Meta's invites "wasteful spending" narratives.

For Conde Nast specifically, the financial architecture for Spectacles launch
(Sep 16) includes:
- CRO from Snap (mechanism #208, Herbst-Brady)
- CBO France from Meta (mechanism #216, Gressier — ambiguous direction)
- OpenAI deal funding Snap's My AI API costs (mechanism #43)
- Perplexity chain ($400M → Perplexity → Conde Nast, mechanism #133)
- Discover platform history with Snap
- Zero direct Meta ad revenue relationship

The entity-selective financial architecture predicts that Conde Nast/WIRED
will cover Snap Spectacles (4 cameras, $2,195) with significantly less
privacy scrutiny than Meta glasses (1 camera, $299-$379), despite the
functional camera parity making privacy concerns identical.

SOURCES:
- https://fashionunited.uk/news/people/former-meta-executive-violaine-gressier-joins-conde-nast-france/2026060388396
- https://investor.snap.com/news/news-details/2026/Snap-Inc--Announces-Second-Quarter-2026-Financial-Results/default.aspx
- https://www.marketbeat.com/instant-alerts/snap-q2-earnings-call-highlights-2026-08-03/
- https://www.techtimes.com/articles/322885/20260803/snap-q2-2026-earnings-prove-restructuring-worked-stock-jumps-ebitda-surge.htm
- https://www.zacks.com/stock/news/2967567/snap-q2-earnings-call-highlights-ad-gains-and-cash-discipline
- https://www.tradingview.com/news/tradingview:87a35dee58c43:0-snap-reports-q2-2026-revenue-1-599b-adjusted-ebitda-250m-and-positive-free-cash-flow/

Cross-references: #202, #208, #133, #43, #8
"""

import unittest
import yaml
import os


def load_competitor_entities():
    """Load competitor entities YAML."""
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'competitor-entities.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def load_wired_profile():
    """Load WIRED profile YAML."""
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'wired.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


class TestSnapQ2_2026ComprehensiveFinancials(unittest.TestCase):
    """Verify comprehensive Snap Q2 2026 financial data is documented."""

    def setUp(self):
        self.entities = load_competitor_entities()
        self.snap = self.entities['entities']['snap']
        self.q2 = self.snap.get('q2_2026_earnings', {})

    def test_total_revenue_precise(self):
        """Revenue is $1,599M, not just $1.6B."""
        self.assertEqual(self.q2.get('total_revenue_m'), 1599)

    def test_advertising_revenue_breakdown(self):
        """Advertising revenue is $1,283M (+9% YoY)."""
        self.assertEqual(self.q2.get('advertising_revenue_m'), 1283)

    def test_other_revenue_breakdown(self):
        """Other revenue is $316M (+85% YoY)."""
        self.assertEqual(self.q2.get('other_revenue_m'), 316)
        self.assertEqual(self.q2.get('other_revenue_yoy_pct'), 85)

    def test_adjusted_ebitda_explosion(self):
        """EBITDA was $249.6M — 505% YoY increase from $41.3M."""
        self.assertAlmostEqual(self.q2.get('adjusted_ebitda_m'), 249.6, places=1)
        self.assertEqual(self.q2.get('adjusted_ebitda_yoy_pct'), 505)

    def test_free_cash_flow_positive(self):
        """Free cash flow turned decisively positive at $120.5M."""
        self.assertAlmostEqual(self.q2.get('free_cash_flow_m'), 120.5, places=1)

    def test_mau_971m(self):
        """MAU reached 971M — approaching 1 billion milestone."""
        self.assertEqual(self.q2.get('mau_m'), 971)

    def test_restructuring_charges_documented(self):
        """Restructuring charges of $128.5M are documented."""
        self.assertAlmostEqual(self.q2.get('restructuring_charges_m'), 128.5, places=1)

    def test_spectacles_launch_confirmed(self):
        """September 16 Spectacles consumer launch confirmed on Q2 call."""
        launch = self.q2.get('spectacles_launch_confirmed', '')
        self.assertIn('September 16', launch)

    def test_q3_guidance_documented(self):
        """Q3 guidance: $1.70-$1.74B revenue."""
        self.assertIsNotNone(self.q2.get('q3_guidance_revenue_b'))

    def test_gross_margin(self):
        """Gross margin at 58%."""
        self.assertEqual(self.q2.get('gross_margin_pct'), 58)

    def test_h1_revenue(self):
        """H1 2026 revenue was $3,128M (+15% YoY)."""
        self.assertEqual(self.q2.get('h1_2026_revenue_m'), 3128)

    def test_source_urls_primary(self):
        """Source URLs include Snap investor relations (primary)."""
        urls = self.q2.get('source_urls', [])
        investor_url = any('investor.snap.com' in u for u in urls)
        self.assertTrue(investor_url, "Missing Snap IR primary source URL")


class TestSnapMetaRevenueComparison(unittest.TestCase):
    """Verify the Snap/Meta revenue contrast is documented."""

    def setUp(self):
        self.entities = load_competitor_entities()
        self.snap = self.entities['entities']['snap']
        self.q2 = self.snap.get('q2_2026_earnings', {})

    def test_financial_inflection_analysis_exists(self):
        """Financial inflection analysis comparing Snap and Meta is present."""
        analysis = self.q2.get('financial_inflection_analysis', '')
        self.assertIn('Meta', analysis)
        self.assertIn('$60.8B', analysis)

    def test_revenue_ratio_documented(self):
        """The 38:1 revenue ratio is noted."""
        analysis = self.q2.get('financial_inflection_analysis', '')
        self.assertIn('38:1', analysis)

    def test_coverage_inversion_noted(self):
        """Notes that coverage ratio inverts the revenue ratio."""
        analysis = self.q2.get('financial_inflection_analysis', '')
        self.assertIn('inverts', analysis.lower())


class TestCondeNastMetaReversePersonnelFlow(unittest.TestCase):
    """Verify the Violaine Gressier reverse personnel flow is documented."""

    def setUp(self):
        data = load_wired_profile()
        self.gressier = data.get('conde_nast_meta_reverse_personnel_flow', {})

    def test_mechanism_id(self):
        """Mechanism has correct ID."""
        self.assertEqual(self.gressier.get('mechanism_id'), 216)

    def test_hire_name(self):
        """Gressier name is documented."""
        hire = self.gressier.get('hire_details', {})
        self.assertEqual(hire.get('name'), 'Violaine Gressier')

    def test_previous_role_meta(self):
        """Previous role was at Meta."""
        hire = self.gressier.get('hire_details', {})
        self.assertIn('Meta', hire.get('previous_role', ''))

    def test_new_role_cbo_france(self):
        """New role is CBO Conde Nast France."""
        hire = self.gressier.get('hire_details', {})
        self.assertIn('Chief Business Officer', hire.get('role', ''))

    def test_effective_date(self):
        """Effective date is June 22, 2026."""
        hire = self.gressier.get('hire_details', {})
        self.assertEqual(hire.get('effective_date'), '2026-06-22')

    def test_reports_to_herbst_brady(self):
        """Reports to Elizabeth Herbst-Brady (CRO)."""
        hire = self.gressier.get('hire_details', {})
        self.assertIn('Herbst-Brady', hire.get('reports_to', ''))

    def test_titles_overseen(self):
        """Oversees Vogue France, GQ, Vanity Fair, AD."""
        hire = self.gressier.get('hire_details', {})
        titles = hire.get('titles_overseen', [])
        self.assertIn('Vogue France', titles)
        self.assertIn('AD (Architectural Digest, France)', titles)

    def test_ambiguous_asymmetry_score(self):
        """Asymmetry score is moderate (ambiguous direction)."""
        score = self.gressier.get('asymmetry_score', 0)
        self.assertGreater(score, 0.3)
        self.assertLess(score, 0.6)

    def test_meta_contrast_update(self):
        """Updates the 'zero Meta personnel ties' claim."""
        update = self.gressier.get('meta_contrast_update', '')
        self.assertIn('no longer true', update.lower())

    def test_source_url(self):
        """Has FashionUnited source URL."""
        urls = self.gressier.get('source_urls', [])
        self.assertTrue(any('fashionunited' in u for u in urls))

    def test_confounders_include_luxury_vs_tech_distinction(self):
        """Confounders note French luxury advertising is distinct from US tech coverage."""
        confounders = self.gressier.get('confounding_factors', [])
        luxury_confounder = any('luxury' in c.lower() and 'fashion' in c.lower() for c in confounders)
        self.assertTrue(luxury_confounder, "Missing luxury/fashion market distinction confounder")

    def test_cross_references_mechanism_208(self):
        """Cross-references the CRO career migration mechanism."""
        refs = self.gressier.get('cross_references', [])
        self.assertIn(208, refs)


class TestSnapSpecsLaunchFinancialFoundation(unittest.TestCase):
    """Verify the Spectacles September launch financial foundation is documented."""

    def setUp(self):
        self.entities = load_competitor_entities()
        self.snap = self.entities['entities']['snap']
        self.specs = self.snap.get('hardware_devices', {}).get('specs_consumer', {})
        self.q2 = self.snap.get('q2_2026_earnings', {})

    def test_launch_date_sept_16(self):
        """Consumer launch event is September 16, 2026."""
        self.assertEqual(self.specs.get('consumer_launch_event_date'), '2026-09-16')

    def test_launch_location_la(self):
        """Launch location is Los Angeles."""
        self.assertEqual(self.specs.get('consumer_launch_location'), 'Los Angeles')

    def test_price_2195(self):
        """Price is $2,195."""
        self.assertEqual(self.specs.get('price_usd'), 2195)

    def test_four_cameras(self):
        """Snap Specs has 4 cameras (2 RGB + 2 IR)."""
        cameras = self.specs.get('cameras', {})
        self.assertEqual(cameras.get('total'), 4)

    def test_privacy_scrutiny_zero(self):
        """Snap Specs has received zero privacy scrutiny."""
        self.assertEqual(self.specs.get('privacy_scrutiny_received'), 'zero')

    def test_financial_foundation_validated(self):
        """Q2 EBITDA explosion validates hardware investment."""
        ebitda = self.q2.get('adjusted_ebitda_m', 0)
        self.assertGreater(ebitda, 200, "EBITDA should exceed $200M, validating hardware bet")

    def test_free_cash_flow_positive_at_launch(self):
        """Snap is free-cash-flow positive entering the launch period."""
        fcf = self.q2.get('free_cash_flow_m', 0)
        self.assertGreater(fcf, 100, "FCF should be >$100M entering Specs launch")


if __name__ == '__main__':
    unittest.main()
