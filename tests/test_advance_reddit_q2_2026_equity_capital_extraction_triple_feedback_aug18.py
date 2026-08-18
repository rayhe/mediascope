"""
Mechanism #162: Advance Publications Reddit Q2 2026 Equity-Backed Capital Extraction —
Triple-Layer Financial Feedback Loop (Aug 18, 2026)

Type C: Financial Incentive Mapping

DISCOVERY: Advance Publications — parent of Condé Nast (WIRED, Vogue, GQ, Vanity Fair,
The New Yorker) — has constructed a TRIPLE-LAYER financial feedback loop through Reddit
that creates compounding incentives for adversarial Meta coverage.

Reddit reported Q2 2026 results on July 30, 2026:
- Total revenue: $805M (+61% YoY), 8th consecutive quarter above 60% growth
- Advertising revenue: $762M (+64% YoY)
- Net income: $253M (31% margin, +183% YoY, more than doubled)
- Adjusted EBITDA: $343M (43% margin, +106% YoY)
- Operating cash flow: $262M (+135% YoY)
- Free cash flow: $261M
- DAUq: 130.3M (+18% YoY)
- WAUq: 514.6M (+24% YoY, crossed half billion)
- ARPU: $6.18 (+36% YoY)
- Max Campaigns revenue: +150%
- Revenue per employee: $1M+ ($805M / 2,555 employees)
- Q3 2026 guidance: $860-870M revenue, $385-395M adj EBITDA

Reddit TTM (trailing twelve months as of Q2 2026):
- Revenue: $2.78B
- Net income: $871M
- Free cash flow: $1.02B

Market data (Aug 17, 2026):
- Stock price: $164.50
- Market cap: $31.65B
- Shares outstanding: 192.4M
- 52-week range: $119.27-$282.95

THE THREE LAYERS:

LAYER 1 — AD REVENUE COMPETITION (documented in mechanism #161):
Reddit's $762M quarterly ad revenue (+64% YoY) directly competes with Meta for
advertiser budgets. Reddit Max Campaigns (launched CES Jan 2026) is a direct
competitor to Meta Advantage+. Reddit COO Jen Wong explicitly named Meta as a
competitor. Meta launched Forum (May 2026) as a Reddit-rival app.

Annualized Reddit ad revenue run rate: ~$3.05B.
Reddit ad revenue acceleration: Q1 2026 +74% YoY → Q2 2026 +64% YoY.
For comparison, Meta's Q2 2026 revenue was $60.8B — Reddit is ~1.3% the size.
But Reddit is growing at 64% vs Meta's ~22%, meaning Reddit captures a
DISPROPORTIONATE share of incremental ad budgets.

LAYER 2 — EQUITY-BACKED CAPITAL EXTRACTION (NEW):
Bloomberg Law reported that Advance Magazine Publishers Inc. — the Newhouse family
entity that owns Condé Nast — established a credit facility using Reddit equity as
collateral:
- Offered 7.8M Reddit shares at $145.38-$148.54 each
- Valued at up to $1.2B
- Simultaneously purchased derivatives on the shares (likely upside collars to
  maintain exposure while borrowing)
- Discount: up to 8% from closing price of $158.02

This means Advance is DIRECTLY CONVERTING Reddit stock appreciation into corporate
capital. Reddit's stock price depends on revenue growth, which depends on ad revenue,
which depends on winning ad budgets from competitors including Meta. Every dollar of
ad revenue Reddit takes from Meta increases Reddit's stock price, which increases the
value of Advance's credit facility, which provides more capital to Advance (which
also funds Condé Nast / WIRED operations).

Advance's economic Reddit stake (~30%):
- At $164.50/share × 192.4M shares × 30% = ~$9.5B
- At peak ($282.95): ~$16.3B
- At IPO ($34/share, Mar 2024): ~$2.0B
- Appreciation since IPO: +375%

Advance's voting control: 65.2% (up from 62.0% in 2025, concentrated via insider
sales by other shareholders). This gives Advance effective CONTROL of Reddit's
strategic direction, including its advertising product roadmap that directly
competes with Meta.

LAYER 3 — BOARD GOVERNANCE INTEGRATION:
Former Condé Nast CEO Robert Sauerberg serves as Reddit Board Vice Chairperson.
This creates a direct governance link between the publication parent company and
the advertising competitor. Sauerberg's dual role means Advance's media interests
(Condé Nast / WIRED editorial direction) and Reddit's competitive interests
(taking ad dollars from Meta) are represented by the same governance structure.

COMPOUND FINANCIAL FEEDBACK LOOP:
When WIRED publishes adversarial Meta coverage:
1. Advertiser perception of Meta may shift negatively
2. Some incremental ad dollars flow from Meta to alternatives including Reddit
3. Reddit's ad revenue grows → stock price increases
4. Advance's $9.5B Reddit stake appreciates
5. Advance's $1.2B credit facility can be expanded
6. Advance capital funds Condé Nast operations (including WIRED)
7. WIRED continues its editorial posture

This is NOT a claim of conscious collusion — it's a STRUCTURAL INCENTIVE that
exists regardless of whether any individual actor is aware of it. The financial
architecture creates alignment between adversarial coverage and capital gain
through market mechanisms, not editorial directives.

MATERIALITY CALCULATION:
- Reddit Q2 2026 ad revenue growth: $762M - $465M(Q2 2025) = $297M incremental
- If even 5% of Reddit's incremental ad revenue comes at Meta's expense: ~$14.9M/q
- 30% Advance ownership × revenue multiple: modest stock impact
- But the CREDIT FACILITY mechanism means even small stock movements affect
  Advance's borrowing capacity on a $1.2B facility

CONFOUNDERS:
1. (STRONG) Editorial independence — No evidence that Advance or Sauerberg directs
   WIRED editorial decisions based on Reddit competitive interests.
2. (STRONG) Scale disparity — Reddit's ~$3B annual ad revenue is ~1.3% of Meta's
   ~$233B. Incremental shifts are tiny relative to Meta.
3. (STRONG) Multiple ad competitors — Google, Amazon, TikTok all compete with Meta
   for ad budgets. Reddit is one of many alternatives, not the sole beneficiary of
   Meta's losses.
4. (MODERATE) Credit facility is routine — Large shareholders commonly borrow against
   concentrated positions. This is standard wealth management, not evidence of
   editorial coordination.
5. (MODERATE) Stock price drivers are complex — Reddit's stock moves on many factors
   beyond Meta's coverage. User growth, product innovation, and broader market
   conditions are larger drivers.
6. (WEAK) Condé Nast union tensions — WIRED journalists are in an adversarial
   relationship with Condé Nast management over layoffs, suggesting they don't take
   direction from Advance corporate interests.

CROSS-REFERENCES:
- Mechanism #161 (Advance Reddit-Meta Advertising Direct Competition)
- Mechanism #1 (Advance-Reddit aggregate AI dependency)
- Mechanism #11 (Meta ad competitor structural antagonism)
- Mechanism #69 (Reddit deal renewal projections)

Source URLs:
- https://www.businesswire.com/news/home/20260730598707/en/Reddit-Reports-Second-Quarter-2026-Results
- https://www.zacks.com/stock/news/2965766/rddt-q2-earnings-call-highlights-ai-user-growth-push
- https://www.nasdaq.com/articles/reddit-q2-profit-more-doubles-revenue-surges-61
- https://stockanalysis.com/stocks/rddt/market-cap/
- https://www.fool.com/quote/nyse/rddt/
- https://www.thewrap.com/conde-nast-advance-publications-reddit-ipo/
- https://en.wikipedia.org/wiki/Advance_Publications
"""

import unittest
import yaml
import os


def load_competitor_research():
    """Load the competitor coverage research YAML."""
    path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "profiles",
        "competitor-coverage-research.yaml",
    )
    with open(path) as f:
        return yaml.safe_load(f)


def load_competitor_entities():
    """Load the competitor entities YAML."""
    path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "profiles",
        "competitor-entities.yaml",
    )
    with open(path) as f:
        return yaml.safe_load(f)


class TestMechanismExists(unittest.TestCase):
    """Verify mechanism #162 exists and has required structural fields."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        mechanisms = cls.data.get("aggregate_findings", {})
        cls.mechanism = mechanisms.get(
            "advance_reddit_q2_2026_equity_capital_extraction"
        )

    def test_mechanism_exists(self):
        self.assertIsNotNone(
            self.mechanism, "Mechanism advance_reddit_q2_2026_equity_capital_extraction must exist"
        )

    def test_mechanism_id(self):
        self.assertEqual(self.mechanism.get("mechanism_id"), 162)

    def test_has_finding_summary(self):
        self.assertIn("finding_summary", self.mechanism)

    def test_has_source_urls(self):
        urls = self.mechanism.get("source_urls", [])
        self.assertGreaterEqual(len(urls), 4)

    def test_has_confounders(self):
        confounders = self.mechanism.get("confounders", [])
        self.assertGreaterEqual(len(confounders), 5)

    def test_has_cross_references(self):
        refs = self.mechanism.get("cross_references", [])
        self.assertGreaterEqual(len(refs), 3)

    def test_has_triple_layer_structure(self):
        self.assertIn("layers", self.mechanism)
        layers = self.mechanism["layers"]
        self.assertIn("ad_revenue_competition", layers)
        self.assertIn("equity_capital_extraction", layers)
        self.assertIn("board_governance_integration", layers)


class TestRedditQ2_2026Financials(unittest.TestCase):
    """Verify Reddit Q2 2026 financial data is accurately documented."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        mechanisms = cls.data.get("aggregate_findings", {})
        cls.mechanism = mechanisms.get(
            "advance_reddit_q2_2026_equity_capital_extraction"
        )
        cls.q2 = cls.mechanism.get("reddit_q2_2026", {}) if cls.mechanism else {}

    def test_revenue(self):
        self.assertEqual(self.q2.get("revenue_m"), 805)

    def test_revenue_yoy_growth_pct(self):
        self.assertEqual(self.q2.get("revenue_yoy_growth_pct"), 61)

    def test_ad_revenue(self):
        self.assertEqual(self.q2.get("ad_revenue_m"), 762)

    def test_ad_revenue_yoy_growth_pct(self):
        self.assertEqual(self.q2.get("ad_revenue_yoy_growth_pct"), 64)

    def test_net_income(self):
        self.assertEqual(self.q2.get("net_income_m"), 253)

    def test_net_income_margin_pct(self):
        self.assertEqual(self.q2.get("net_income_margin_pct"), 31)

    def test_adj_ebitda(self):
        self.assertEqual(self.q2.get("adj_ebitda_m"), 343)

    def test_operating_cash_flow(self):
        self.assertEqual(self.q2.get("operating_cash_flow_m"), 262)

    def test_dauq(self):
        self.assertEqual(self.q2.get("dauq_m"), 130.3)

    def test_wauq(self):
        self.assertEqual(self.q2.get("wauq_m"), 514.6)

    def test_arpu(self):
        self.assertEqual(self.q2.get("arpu"), 6.18)

    def test_max_campaigns_growth_pct(self):
        self.assertGreaterEqual(self.q2.get("max_campaigns_growth_pct", 0), 150)

    def test_consecutive_60pct_growth_quarters(self):
        self.assertEqual(self.q2.get("consecutive_60pct_growth_quarters"), 8)

    def test_q3_guidance_revenue_low(self):
        self.assertEqual(self.q2.get("q3_2026_guidance_revenue_low_m"), 860)

    def test_q3_guidance_revenue_high(self):
        self.assertEqual(self.q2.get("q3_2026_guidance_revenue_high_m"), 870)

    def test_earnings_date(self):
        self.assertEqual(self.q2.get("earnings_date"), "2026-07-30")


class TestRedditTTMFinancials(unittest.TestCase):
    """Verify Reddit trailing twelve month financial data."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        mechanisms = cls.data.get("aggregate_findings", {})
        cls.mechanism = mechanisms.get(
            "advance_reddit_q2_2026_equity_capital_extraction"
        )
        cls.ttm = cls.mechanism.get("reddit_ttm", {}) if cls.mechanism else {}

    def test_ttm_revenue_b(self):
        self.assertAlmostEqual(self.ttm.get("revenue_b"), 2.78, places=1)

    def test_ttm_net_income_m(self):
        self.assertAlmostEqual(self.ttm.get("net_income_m"), 871, delta=10)

    def test_ttm_fcf_b(self):
        self.assertAlmostEqual(self.ttm.get("fcf_b"), 1.02, places=1)


class TestRedditMarketData(unittest.TestCase):
    """Verify Reddit market data as of August 2026."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        mechanisms = cls.data.get("aggregate_findings", {})
        cls.mechanism = mechanisms.get(
            "advance_reddit_q2_2026_equity_capital_extraction"
        )
        cls.market = cls.mechanism.get("reddit_market_data", {}) if cls.mechanism else {}

    def test_market_cap_b(self):
        self.assertAlmostEqual(self.market.get("market_cap_b"), 31.65, delta=1.0)

    def test_shares_outstanding_m(self):
        self.assertAlmostEqual(self.market.get("shares_outstanding_m"), 192.4, delta=5)

    def test_stock_price_date(self):
        self.assertEqual(self.market.get("as_of_date"), "2026-08-17")

    def test_pe_ratio(self):
        pe = self.market.get("pe_ratio")
        self.assertIsNotNone(pe)
        self.assertGreater(pe, 30)
        self.assertLess(pe, 50)


class TestEquityCapitalExtraction(unittest.TestCase):
    """Verify the equity-backed credit facility mechanism."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        mechanisms = cls.data.get("aggregate_findings", {})
        cls.mechanism = mechanisms.get(
            "advance_reddit_q2_2026_equity_capital_extraction"
        )
        layers = cls.mechanism.get("layers", {}) if cls.mechanism else {}
        cls.equity = layers.get("equity_capital_extraction", {})

    def test_credit_facility_exists(self):
        self.assertIn("credit_facility_value_b", self.equity)

    def test_credit_facility_value(self):
        self.assertAlmostEqual(self.equity.get("credit_facility_value_b"), 1.2, places=1)

    def test_shares_offered(self):
        self.assertAlmostEqual(self.equity.get("shares_offered_m"), 7.8, places=1)

    def test_share_price_range(self):
        low = self.equity.get("share_price_range_low")
        high = self.equity.get("share_price_range_high")
        self.assertIsNotNone(low)
        self.assertIsNotNone(high)
        self.assertAlmostEqual(low, 145.38, places=1)
        self.assertAlmostEqual(high, 148.54, places=1)

    def test_derivatives_purchase(self):
        self.assertTrue(self.equity.get("derivatives_purchased"))

    def test_source_bloomberg(self):
        source = self.equity.get("source")
        self.assertIn("Bloomberg", source)


class TestAdvanceOwnership(unittest.TestCase):
    """Verify Advance Publications ownership data."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        mechanisms = cls.data.get("aggregate_findings", {})
        cls.mechanism = mechanisms.get(
            "advance_reddit_q2_2026_equity_capital_extraction"
        )
        cls.ownership = cls.mechanism.get("advance_ownership", {}) if cls.mechanism else {}

    def test_economic_stake_pct(self):
        self.assertAlmostEqual(self.ownership.get("economic_stake_pct"), 30, delta=2)

    def test_voting_control_pct(self):
        self.assertAlmostEqual(self.ownership.get("voting_control_pct"), 65.2, delta=1)

    def test_stake_value_b(self):
        # 30% of $31.65B = ~$9.5B
        value = self.ownership.get("stake_value_b")
        self.assertIsNotNone(value)
        self.assertGreater(value, 8.0)
        self.assertLess(value, 12.0)

    def test_board_governance(self):
        board = self.ownership.get("board_governance", {})
        self.assertEqual(board.get("former_conde_nast_ceo_role"), "Vice Chairperson")
        self.assertEqual(board.get("name"), "Robert Sauerberg")


class TestBoardGovernanceLayer(unittest.TestCase):
    """Verify the board governance integration layer."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        mechanisms = cls.data.get("aggregate_findings", {})
        cls.mechanism = mechanisms.get(
            "advance_reddit_q2_2026_equity_capital_extraction"
        )
        layers = cls.mechanism.get("layers", {}) if cls.mechanism else {}
        cls.board = layers.get("board_governance_integration", {})

    def test_sauerberg_role(self):
        self.assertEqual(self.board.get("person"), "Robert Sauerberg")

    def test_sauerberg_former_role(self):
        self.assertEqual(self.board.get("former_role"), "CEO, Condé Nast")

    def test_sauerberg_reddit_role(self):
        self.assertEqual(self.board.get("reddit_role"), "Board Vice Chairperson")

    def test_governance_link_documented(self):
        desc = self.board.get("governance_link_description", "")
        self.assertIn("Condé Nast", desc)
        self.assertIn("Reddit", desc)


class TestAdRevenueLayer(unittest.TestCase):
    """Verify the ad revenue competition layer with Q2 2026 data."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        mechanisms = cls.data.get("aggregate_findings", {})
        cls.mechanism = mechanisms.get(
            "advance_reddit_q2_2026_equity_capital_extraction"
        )
        layers = cls.mechanism.get("layers", {}) if cls.mechanism else {}
        cls.ad = layers.get("ad_revenue_competition", {})

    def test_reddit_annualized_ad_revenue_b(self):
        val = self.ad.get("reddit_annualized_ad_revenue_b")
        self.assertIsNotNone(val)
        self.assertGreater(val, 2.5)

    def test_meta_q2_2026_revenue_b(self):
        self.assertAlmostEqual(self.ad.get("meta_q2_2026_revenue_b"), 60.8, delta=1)

    def test_reddit_meta_revenue_ratio_pct(self):
        ratio = self.ad.get("reddit_meta_revenue_ratio_pct")
        self.assertIsNotNone(ratio)
        self.assertGreater(ratio, 1.0)
        self.assertLess(ratio, 2.0)

    def test_max_campaigns_competitor_named(self):
        competitors = self.ad.get("max_campaigns_competes_with", [])
        self.assertIn("Meta Advantage+", competitors)

    def test_meta_forum_competition(self):
        self.assertTrue(self.ad.get("meta_forum_launched"))


class TestCompoundFeedbackLoop(unittest.TestCase):
    """Verify the compound financial feedback loop is documented."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        mechanisms = cls.data.get("aggregate_findings", {})
        cls.mechanism = mechanisms.get(
            "advance_reddit_q2_2026_equity_capital_extraction"
        )
        cls.loop = cls.mechanism.get("compound_feedback_loop", {}) if cls.mechanism else {}

    def test_loop_steps_documented(self):
        steps = self.loop.get("steps", [])
        self.assertGreaterEqual(len(steps), 5)

    def test_loop_is_structural(self):
        self.assertTrue(self.loop.get("structural_not_conspiratorial"))

    def test_materiality_calculation_exists(self):
        mat = self.loop.get("materiality", {})
        self.assertIn("incremental_ad_revenue_q2_m", mat)


class TestConfounders(unittest.TestCase):
    """Verify all confounders are documented with strength ratings."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        mechanisms = cls.data.get("aggregate_findings", {})
        cls.mechanism = mechanisms.get(
            "advance_reddit_q2_2026_equity_capital_extraction"
        )

    def test_confounder_count(self):
        confounders = self.mechanism.get("confounders", [])
        self.assertGreaterEqual(len(confounders), 5)

    def test_confounders_have_strength(self):
        for c in self.mechanism.get("confounders", []):
            self.assertIn("strength", c, f"Confounder missing strength: {c}")

    def test_strong_confounders_present(self):
        confounders = self.mechanism.get("confounders", [])
        strong = [c for c in confounders if c.get("strength") == "STRONG"]
        self.assertGreaterEqual(len(strong), 3)

    def test_editorial_independence_confounder(self):
        confounders = self.mechanism.get("confounders", [])
        editorial = [c for c in confounders if "editorial" in c.get("description", "").lower()]
        self.assertGreaterEqual(len(editorial), 1)


class TestCrossReferences(unittest.TestCase):
    """Verify cross-references to related mechanisms."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_research()
        mechanisms = cls.data.get("aggregate_findings", {})
        cls.mechanism = mechanisms.get(
            "advance_reddit_q2_2026_equity_capital_extraction"
        )

    def test_references_mechanism_161(self):
        refs = self.mechanism.get("cross_references", [])
        self.assertIn(161, refs)

    def test_references_mechanism_1(self):
        refs = self.mechanism.get("cross_references", [])
        self.assertIn(1, refs)

    def test_references_mechanism_11(self):
        refs = self.mechanism.get("cross_references", [])
        self.assertIn(11, refs)


class TestDocSync(unittest.TestCase):
    """Verify README and ARCHITECTURE docs are in sync."""

    def test_test_file_in_readme(self):
        readme_path = os.path.join(
            os.path.dirname(__file__), "..", "README.md"
        )
        with open(readme_path) as f:
            content = f.read()
        self.assertIn(
            "test_advance_reddit_q2_2026_equity_capital_extraction_triple_feedback_aug18",
            content,
        )

    def test_test_file_in_architecture(self):
        arch_path = os.path.join(
            os.path.dirname(__file__), "..", "docs", "ARCHITECTURE.md"
        )
        with open(arch_path) as f:
            content = f.read()
        self.assertIn(
            "test_advance_reddit_q2_2026_equity_capital_extraction_triple_feedback_aug18",
            content,
        )


if __name__ == "__main__":
    unittest.main()
