"""
Mechanism #235: Specs Inc. Activist-Investor Pre-Launch Financial Pressure Architecture

Type: Financial Incentive Mapping (Type C)
Entity: Snap Inc. / Specs Inc. subsidiary
Date: 2026-08-22

CORE FINDING:
Snap's creation of Specs Inc. as a wholly-owned subsidiary (Jan 28, 2026), combined with
Irenic Capital Management's activist pressure to kill/spin off the unit ($3.5B cumulative
burn, ~$500M/yr), creates a BINARY COVERAGE INCENTIVE in the 25-day window before the
September 16, 2026 consumer launch at $2,195:

1. POSITIVE COVERAGE → Specs Inc. attracts minority investment → survives activist challenge
   → Snap advertising platform strengthened → publishers benefit from Snap ad relationships
2. NEGATIVE COVERAGE → validates Irenic's kill thesis → Specs killed/spun off → Meta monopoly
   in smart glasses → Meta's ad dominance ($243B) intensified → publishers lose competitive leverage

This binary creates outsized financial consequences for pre-launch coverage tone. Unlike most
product launches where coverage merely affects sales, Specs coverage affects CORPORATE SURVIVAL
of the entire hardware unit.

NOVEL CONTRIBUTIONS:
1. First mechanism documenting activist-investor pressure as a coverage incentive amplifier
2. Corporate subsidiary structure (Specs Inc.) as a financial shield enabling minority investment
3. The Herbst-Brady connection: Condé Nast CRO (ex-Snap) overseeing revenue at the publication
   whose WIRED title most aggressively covers Meta glasses
4. Convergence: Irenic's $500M/yr burn figure creates a QUANTIFIED survival threshold —
   coverage that tips Specs toward failure has a calculable financial impact

SOURCES:
- Reuters: https://www.reuters.com/business/snap-seeks-investments-new-smart-glasses-unit-takes-meta-2026-01-28/
- Reuters (Spiegel defense): https://www.reuters.com/business/finance/snap-ceo-spiegel-defends-specs-long-term-bet-pushes-back-against-activist-2026-06-16/
- Irenic letter: https://www.morningstar.com/news/business-wire/20260331059373/irenic-sends-letter-to-snap-inc-co-founder-and-ceo-evan-spiegel-and-issues-presentation-outlining-actionable-steps-to-unlock-value
- Barron's: https://www.barrons.com/articles/snap-stock-surges-activist-investor-stake-6ed7192f
- Snap Q2 2026: https://www.businesswire.com/news/home/20260803600317/en/Snap-Inc.-Announces-Second-Quarter-2026-Financial-Results
- TechCrunch (Perplexity ended): https://techcrunch.com/2026/05/06/snap-says-its-400m-deal-with-perplexity-amicably-ended/
- PhoneArena (Sep 16 launch): https://www.phonearena.com/news/snaps-ar-glasses-consumer-focused-unveilng_id182255
"""

import unittest


class TestSpecsIncSubsidiaryStructure(unittest.TestCase):
    """Tests for the Specs Inc. corporate structure and minority investment path."""

    def test_specs_inc_established_jan_28_2026(self):
        """Specs Inc. was established as a wholly-owned subsidiary on Jan 28, 2026."""
        specs_inc = {
            "name": "Specs Inc.",
            "type": "wholly-owned subsidiary",
            "parent": "Snap Inc.",
            "established_date": "2026-01-28",
            "purpose": [
                "greater operational focus and alignment",
                "new partnerships and capital flexibility",
                "potential for minority investment",
                "distinct brand identity",
                "clearer valuation of the business",
            ],
            "source_url": "https://www.reuters.com/business/snap-seeks-investments-new-smart-glasses-unit-takes-meta-2026-01-28/",
        }
        self.assertEqual(specs_inc["type"], "wholly-owned subsidiary")
        self.assertEqual(specs_inc["parent"], "Snap Inc.")
        self.assertIn("potential for minority investment", specs_inc["purpose"])

    def test_specs_inc_minority_investment_path(self):
        """Specs Inc. explicitly opened the door to minority investment."""
        investment_path = {
            "structure": "wholly-owned subsidiary with minority investment path",
            "snap_statement": (
                "Establishing Specs Inc. as a wholly-owned subsidiary provides "
                "greater operational focus and alignment, enables new partnerships "
                "and capital flexibility including the potential for minority "
                "investment, allows us to grow a distinct brand, and supports "
                "clearer valuation of the business."
            ),
            "investors_disclosed": 0,
            "investment_received_disclosed": False,
            "hiring_at_announcement": "~100 global positions",
            "coverage_incentive": (
                "Publications with relationships to potential Specs Inc. investors "
                "(venture capital, hardware funds, Qualcomm) have incentive to "
                "produce favorable coverage that supports higher Specs Inc. "
                "valuation and minority investment success."
            ),
        }
        self.assertEqual(investment_path["investors_disclosed"], 0)
        self.assertFalse(investment_path["investment_received_disclosed"])

    def test_specs_inc_cumulative_investment(self):
        """Snap has invested $3.5B+ over 11 years in AR glasses development."""
        investment = {
            "cumulative_investment_b": 3.5,
            "years": 11,
            "source": "Irenic Capital presentation, confirmed by Snap CEO Spiegel",
            "annual_burn_estimate_m": 500,
            "annual_burn_source": "Irenic Capital Management",
            "context": (
                "The $3.5B cumulative and ~$500M/yr burn rate creates a sunk cost "
                "narrative: Specs must succeed to justify the investment. This "
                "financial pressure makes the Sep 16 consumer launch existential "
                "for the Specs Inc. subsidiary, not merely commercial."
            ),
        }
        self.assertGreaterEqual(investment["cumulative_investment_b"], 3.5)
        self.assertEqual(investment["annual_burn_estimate_m"], 500)


class TestIrenicCapitalActivistPressure(unittest.TestCase):
    """Tests for Irenic Capital Management's activist pressure on Snap/Specs."""

    def test_irenic_stake_and_demands(self):
        """Irenic Capital Management built a 2.5% stake and demanded Specs changes."""
        irenic = {
            "name": "Irenic Capital Management",
            "portfolio_manager": "Adam Katz",
            "stake_pct_class_a": 2.5,
            "letter_date": "2026-03-31",
            "campaign_name": "Snap Back to Reality: Save Snap Now",
            "website": "SaveSnapNow.com",
            "current_snap_market_cap_b": 7.2,
            "target_market_cap_b": 35,
            "target_price_per_share": 26.37,
            "key_demands": [
                "Spin off or shut down Specs",
                "Cut costs through layoffs (~1,000 employees, 21% reduction)",
                "Monetize AI opportunity",
                "Buy back discounted stock",
                "Shift to performance-based equity compensation",
            ],
            "specs_characterization": "strategic liability",
            "specs_annual_cash_drain_m": 500,
            "specs_cumulative_investment_b": 3.5,
            "source_url": "https://www.morningstar.com/news/business-wire/20260331059373/irenic-sends-letter-to-snap-inc-co-founder-and-ceo-evan-spiegel-and-issues-presentation-outlining-actionable-steps-to-unlock-value",
        }
        self.assertEqual(irenic["stake_pct_class_a"], 2.5)
        self.assertIn("Spin off or shut down Specs", irenic["key_demands"])
        self.assertEqual(irenic["specs_annual_cash_drain_m"], 500)

    def test_spiegel_defense_of_specs(self):
        """CEO Spiegel publicly defended Specs against activist pressure."""
        defense = {
            "date": "2026-06-16",
            "venue": "Reuters interview at AWE / Specs consumer launch",
            "key_quote_1": (
                "While investors may want more short-term profitability, our "
                "job at Snap is to drive long-term profitability and the "
                "long-term success of the company."
            ),
            "key_quote_2": (
                "One of the things we've always been clear about as we've "
                "built Snap was that we were committed to our long-term vision. "
                "And that includes staying independent rather than selling the company."
            ),
            "partnership_hint": (
                "Spiegel said the company is expected to share 'more later "
                "this year in terms of how we're thinking about partnerships "
                "over a longer period of time.'"
            ),
            "context": (
                "Spiegel's defense came AT the consumer launch event, directly "
                "linking product viability to corporate strategy. Any coverage "
                "that undermines Specs simultaneously undermines Spiegel's "
                "corporate strategy and strengthens activist pressure."
            ),
            "source_url": "https://www.reuters.com/business/finance/snap-ceo-spiegel-defends-specs-long-term-bet-pushes-back-against-activist-2026-06-16/",
        }
        self.assertEqual(defense["date"], "2026-06-16")
        self.assertIn("long-term profitability", defense["key_quote_1"])

    def test_market_reaction_to_irenic_pressure(self):
        """Market reacted strongly to Irenic's intervention."""
        market_reaction = {
            "snap_stock_jump_on_irenic_letter_pct": 13,
            "snap_ytd_decline_at_letter_pct": 45,
            "snap_share_price_at_letter_usd": 4.54,
            "snap_ipo_return": "23 cents per dollar invested",
            "nasdaq_underperformance_pts": 444,
            "context": (
                "The 13% stock jump on Irenic's letter shows institutional "
                "investors WELCOME the pressure to kill Specs. The market is "
                "pricing Specs as value-destructive. Any positive Specs "
                "coverage that supports the product's survival runs COUNTER "
                "to market consensus, creating editorial tension."
            ),
        }
        self.assertEqual(market_reaction["snap_stock_jump_on_irenic_letter_pct"], 13)
        self.assertEqual(market_reaction["snap_ytd_decline_at_letter_pct"], 45)

    def test_irenic_snap_underperformance_framing(self):
        """Irenic characterized Snap as 'comically undervalued' but Specs as a drain."""
        irenic_framing = {
            "snap_value_thesis": (
                "nearly 1 billion MAUs, reaching 75% of users aged 13-34 globally, "
                "with 350 million AR users, 40 daily opens, 25 million paying "
                "subscribers, 5 billion+ daily snaps"
            ),
            "snap_value_characterization": "comically small sum",
            "specs_characterization": "strategic liability consuming $500M/yr",
            "paradox": (
                "Irenic sees Snapchat as undervalued at $7.2B but Specs as the "
                "reason for undervaluation. The activist's thesis is that KILLING "
                "Specs unlocks value. This means publications that cover Specs "
                "positively are working AGAINST the activist's thesis that the "
                "market has already endorsed (13% stock jump)."
            ),
        }
        self.assertIn("comically small sum", irenic_framing["snap_value_characterization"])


class TestPreLaunchCoverageIncentiveWindow(unittest.TestCase):
    """Tests for the 25-day pre-launch coverage incentive window."""

    def test_september_16_consumer_launch(self):
        """Consumer launch on Sep 16, 2026 creates a coverage event window."""
        launch = {
            "date": "2026-09-16",
            "location": "Los Angeles",
            "price_usd": 2195,
            "deposit_usd": 200,
            "deposit_type": "refundable",
            "shipping_markets": ["US", "UK", "France"],
            "shipping_window": "Fall 2026",
            "host": "Evan Spiegel, CEO",
            "format": "livestream",
            "days_from_aug_22": 25,
            "source_url": "https://www.phonearena.com/news/snaps-ar-glasses-consumer-focused-unveilng_id182255",
        }
        self.assertEqual(launch["price_usd"], 2195)
        self.assertEqual(launch["days_from_aug_22"], 25)

    def test_coverage_window_binary_incentive(self):
        """Pre-launch coverage has BINARY corporate survival implications."""
        binary_incentive = {
            "positive_coverage_chain": [
                "Positive reviews and previews",
                "Consumer interest and pre-order deposits",
                "Minority investment attracted to Specs Inc.",
                "Activist pressure diminished",
                "Specs survives as a business unit",
                "Snap ad platform strengthened (more competition for Meta)",
                "Publishers benefit from competitive ad market",
            ],
            "negative_coverage_chain": [
                "Negative reviews and privacy concerns",
                "Consumer hesitancy and weak pre-orders",
                "Minority investors deterred",
                "Activist pressure intensified",
                "Specs killed or spun off at fire-sale valuation",
                "Meta monopoly in smart glasses strengthened",
                "Meta ad dominance further concentrated",
                "Publishers lose competitive leverage vs Meta",
            ],
            "key_distinction": (
                "Unlike most product launches where coverage affects SALES, "
                "Specs coverage in this window affects CORPORATE SURVIVAL of "
                "the entire hardware unit. The Irenic activist pressure creates "
                "a binary where the unit lives or dies based partly on market "
                "and coverage reception."
            ),
        }
        self.assertEqual(len(binary_incentive["positive_coverage_chain"]), 7)
        self.assertEqual(len(binary_incentive["negative_coverage_chain"]), 8)


class TestPerplexityDealCancellationImpact(unittest.TestCase):
    """Tests for how the Perplexity deal cancellation reshapes the financial landscape."""

    def test_perplexity_deal_canceled_q1_2026(self):
        """$400M Perplexity deal amicably ended Q1 2026 with zero revenue."""
        deal_cancellation = {
            "deal_value_m": 400,
            "structure": "cash + equity",
            "announced": "2025-11-05",
            "terminated": "Q1 2026",
            "termination_type": "amicable",
            "revenue_recognized": 0,
            "snap_q1_guidance_statement": (
                "Our revenue guidance range assumes no contribution from "
                "Perplexity as we amicably ended the relationship in Q1."
            ),
            "stock_impact_on_cancel_pct": -10,
            "stock_impact_on_announce_pct": 16,
            "source_url": "https://techcrunch.com/2026/05/06/snap-says-its-400m-deal-with-perplexity-amicably-ended/",
        }
        self.assertEqual(deal_cancellation["revenue_recognized"], 0)
        self.assertEqual(deal_cancellation["termination_type"], "amicable")

    def test_perplexity_cancellation_weakens_specs_revenue_diversification(self):
        """Without Perplexity revenue, Snap's financial case for Specs is weakened."""
        revenue_impact = {
            "perplexity_lost_annual_revenue_m": 400,
            "specs_annual_burn_m": 500,
            "ratio": 0.8,
            "analysis": (
                "The Perplexity deal ($400M/yr) would have almost fully offset "
                "Specs' estimated annual burn ($500M/yr). Its cancellation "
                "removes the financial cushion that would have made Specs "
                "sustainable without external investment. This AMPLIFIES the "
                "importance of: (1) minority investment in Specs Inc., and "
                "(2) positive coverage that supports pre-order/sales."
            ),
        }
        self.assertAlmostEqual(
            revenue_impact["perplexity_lost_annual_revenue_m"]
            / revenue_impact["specs_annual_burn_m"],
            revenue_impact["ratio"],
            places=1,
        )


class TestQ2FinancialContext(unittest.TestCase):
    """Tests for Q2 2026 financial context surrounding the Specs launch."""

    def test_snap_q2_2026_financial_inflection(self):
        """Q2 2026 showed dramatic EBITDA improvement but continued net loss."""
        q2 = {
            "revenue_m": 1599,
            "revenue_yoy_pct": 19,
            "advertising_revenue_m": 1283,
            "advertising_revenue_yoy_pct": 9,
            "other_revenue_m": 316,
            "other_revenue_yoy_pct": 85,
            "adjusted_ebitda_m": 250,
            "adjusted_ebitda_yoy_pct": 505,
            "net_loss_m": -164,
            "free_cash_flow_m": 121,
            "gross_margin_pct": 58,
            "restructuring_charges_m": 128.5,
            "dau_m": 493,
            "mau_m": 971,
            "north_america_dau_decline_pct": 7,
            "europe_dau_decline_pct": 2,
            "source_url": "https://www.businesswire.com/news/home/20260803600317/en/Snap-Inc.-Announces-Second-Quarter-2026-Financial-Results",
        }
        self.assertEqual(q2["adjusted_ebitda_yoy_pct"], 505)
        self.assertLess(q2["net_loss_m"], 0)
        self.assertGreater(q2["free_cash_flow_m"], 0)

    def test_snap_restructuring_validates_irenic_thesis_partially(self):
        """April 2026 restructuring (~1,000 jobs) aligned with Irenic's cost-cut demand."""
        restructuring = {
            "date": "April 2026",
            "jobs_eliminated": "~1,000",
            "irenic_demanded_cuts": "~1,000 employees (21% reduction)",
            "alignment": (
                "Snap's April restructuring eliminated roughly the same number "
                "of employees Irenic demanded. This partial capitulation to "
                "activist pressure occurred WHILE Spiegel defended Specs. "
                "Snap gave Irenic the cost cuts but NOT the Specs shutdown."
            ),
            "restructuring_charges_q2_m": 128.5,
        }
        self.assertIn("1,000", restructuring["jobs_eliminated"])

    def test_world_cup_ad_boost_masks_core_weakness(self):
        """FIFA World Cup boosted Q2 ad revenue, creating temporary financial strength."""
        world_cup = {
            "event": "FIFA World Cup 2026",
            "impact": "Increased advertising spending during the quarter",
            "spiegel_quote": (
                "The World Cup-related spending contributed during the quarter, "
                "alongside continued strength among small- and medium-sized businesses."
            ),
            "temporal_nature": (
                "World Cup is a one-time ad boost in Q2. Q3 guidance ($1.70-1.74B) "
                "is only modestly above Q2 ($1.6B) suggesting the underlying "
                "growth rate is lower than the 19% headline. The financial "
                "foundation for Specs' launch is more fragile than Q2 suggests."
            ),
            "source_url": "https://www.reuters.com/business/snap-beats-revenue-estimates-ad-boost-world-cup-2026-08-03/",
        }
        self.assertIn("World Cup", world_cup["event"])


class TestHerbstBradyConvergence(unittest.TestCase):
    """Tests for the Herbst-Brady Snap→Condé Nast personnel convergence
    in the context of the Sep 16 launch."""

    def test_herbst_brady_snap_career_timeline(self):
        """CRO Herbst-Brady's Snap career creates a personnel bridge
        to the publication group covering Specs most aggressively."""
        career = {
            "name": "Elizabeth Herbst-Brady",
            "current_role": "Chief Revenue Officer, Condé Nast",
            "start_date": "end of September 2024",
            "prior_roles_include": [
                "Yahoo (CRO and GM, Yahoo DSP)",
                "Snap",
                "Viacom (MTV Networks)",
                "MAGNA Global",
                "20th Television",
                "Starcom Worldwide",
                "Universal Television",
                "Fox",
            ],
            "snap_role": "Senior revenue/advertising leadership",
            "reports_to": "Roger Lynch (CEO, Condé Nast)",
            "direct_reports_include": "Violaine Gressier (CBO France, ex-Meta)",
            "publications_under_revenue_umbrella": [
                "WIRED",
                "GQ",
                "Vogue",
                "Vanity Fair",
                "The New Yorker",
                "Architectural Digest",
                "Bon Appétit",
                "Condé Nast Traveler",
            ],
        }
        self.assertIn("Snap", career["prior_roles_include"])
        self.assertIn("WIRED", career["publications_under_revenue_umbrella"])

    def test_herbst_brady_sep_16_convergence(self):
        """The Sep 16 Specs launch occurs while Herbst-Brady (ex-Snap)
        controls Condé Nast revenue — including WIRED's ad relationships."""
        convergence = {
            "event": "Snap Specs consumer launch, Sep 16, 2026",
            "herbst_brady_role": "CRO, Condé Nast (controls all revenue)",
            "herbst_brady_snap_history": True,
            "wired_meta_glasses_coverage": "most adversarial among major publications",
            "wired_snap_specs_coverage_predicted": "less adversarial than Meta coverage",
            "mechanism": (
                "Herbst-Brady's career at Snap does NOT mean she directs "
                "editorial. But as CRO she shapes the commercial context: "
                "which advertisers are prioritized, which deals are pursued, "
                "which partnerships are valued. If Snap ad revenue matters to "
                "Condé Nast, WIRED editorial operates in a commercial "
                "environment that values Snap's success."
            ),
            "confounders": [
                "Editorial independence from commercial",
                "Herbst-Brady's career spans 8+ employers — Snap is one of many",
                "She joined Condé Nast BEFORE the current coverage cycle",
                "No evidence of editorial direction from Herbst-Brady",
            ],
        }
        self.assertTrue(convergence["herbst_brady_snap_history"])


class TestCoverageAsymmetryPrediction(unittest.TestCase):
    """Tests for predicted coverage asymmetry during Sep 16 launch."""

    def test_meta_vs_snap_publisher_financial_alignment_count(self):
        """Meta has ZERO publisher financial alignment axes; Snap has FOUR."""
        alignment = {
            "snap_specs_alignment_axes": {
                "openai": "AI partner; 20+ publisher content deals ($300-400M/yr)",
                "google": "AI partner; dominant publisher ad revenue + Showcase",
                "qualcomm": "Hardware partner; $25M+ media spend + co-marketing",
                "snap_advertising": "Snap ad platform competes with Meta for publisher budgets",
            },
            "meta_rayban_alignment_axes": {},
            "snap_axis_count": 4,
            "meta_axis_count": 0,
            "privacy_vocabulary_prediction": (
                "Publications will apply LESS privacy-alarm vocabulary to "
                "Snap Specs (4 cameras, $2,195) than to Meta Ray-Ban "
                "(1 camera, $299). The 4:0 alignment ratio predicts this. "
                "If privacy vocabulary IS proportionate to camera count "
                "and price (making Specs more scrutinized), the financial "
                "incentive hypothesis is FALSIFIED."
            ),
        }
        self.assertEqual(alignment["snap_axis_count"], 4)
        self.assertEqual(alignment["meta_axis_count"], 0)

    def test_meta_ad_competition_incentive(self):
        """Meta's $243B ad revenue makes negative Meta coverage serve publisher interests."""
        competition = {
            "meta_annual_ad_revenue_b": 243.46,
            "snap_annual_ad_revenue_b": 5.1,  # ~$1.28B/quarter × 4
            "ratio": 47.7,
            "publisher_incentive": (
                "Meta competes with publishers for the SAME advertising budgets. "
                "Negative Meta coverage can redirect ad spend to competitors "
                "including Snap, Reddit, and traditional publishers. No publisher "
                "benefits from Meta's ad success. This creates a structural "
                "adversarial incentive REGARDLESS of editorial quality."
            ),
        }
        self.assertGreater(competition["ratio"], 40)


class TestConfoundingFactors(unittest.TestCase):
    """Tests for confounding factors that could explain coverage differences."""

    def test_market_share_confounder(self):
        """Meta's dominant market share legitimately attracts more scrutiny."""
        confounder = {
            "strength": "STRONG",
            "meta_smart_glasses_market_share_pct": 84,
            "meta_units_shipped_m": 7,
            "snap_specs_units_shipped": 0,
            "explanation": (
                "Meta has 84% smart glasses market share with 7M+ units. "
                "Specs has zero (not yet shipped). Higher scrutiny for "
                "dominant market leaders is legitimate journalistic practice. "
                "However, if the scrutiny is DISPROPORTIONATE — 100% of "
                "privacy alarm vocabulary going to the 1-camera product "
                "while the 4-camera product gets zero — then market share "
                "alone cannot explain the vocabulary distribution."
            ),
        }
        self.assertEqual(confounder["strength"], "STRONG")

    def test_incident_history_confounder(self):
        """Meta has documented incidents; Snap Specs has none (product not shipped)."""
        confounder = {
            "strength": "STRONG",
            "meta_documented_incidents": True,
            "snap_specs_documented_incidents": False,
            "explanation": (
                "Meta Ray-Ban glasses have real-world incident history "
                "(privacy complaints, facial recognition fears, Harvard "
                "student experiment). Snap Specs has NO incident history "
                "because it hasn't shipped. This legitimately explains "
                "SOME of the coverage differential. However, Apple Glass "
                "(also unshipped, zero incidents) receives PRIVACY-HERO "
                "framing, not zero framing. The entity receiving zero "
                "scrutiny despite more cameras is Snap, not Apple."
            ),
        }
        self.assertEqual(confounder["strength"], "STRONG")

    def test_price_niche_confounder(self):
        """$2,195 price targets early adopters, limiting mass privacy risk."""
        confounder = {
            "strength": "MODERATE",
            "specs_price_usd": 2195,
            "meta_rayban_price_usd": 299,
            "ratio": 7.3,
            "explanation": (
                "At $2,195 Snap Specs targets early adopters/developers, "
                "not mass market. Lower adoption = lower aggregate privacy "
                "risk = less journalistic urgency. However, publications "
                "still cover Apple Vision Pro ($3,499) and Magic Leap ($3,299) "
                "with full privacy analysis. Price alone does not explain "
                "zero privacy vocabulary."
            ),
        }
        self.assertEqual(confounder["strength"], "MODERATE")

    def test_activist_legitimacy_confounder(self):
        """Irenic's concerns about Specs financial viability are legitimate."""
        confounder = {
            "strength": "MODERATE",
            "explanation": (
                "Irenic's $500M/yr burn estimate and 'not working' "
                "characterization may be accurate. The activist pressure "
                "is a legitimate market force, not a media manipulation. "
                "Coverage that accurately reports Specs' financial challenges "
                "is not bias — it's journalism. The confounder is whether "
                "PRIVACY coverage (not financial coverage) is proportionate "
                "across entities."
            ),
        }
        self.assertEqual(confounder["strength"], "MODERATE")

    def test_dual_class_stock_confounder(self):
        """Snap's dual-class stock structure limits activist influence."""
        confounder = {
            "strength": "WEAK",
            "explanation": (
                "Spiegel controls Snap through Class C shares with 10 votes "
                "each. Irenic's 2.5% Class A stake gives it limited "
                "governance power. The activist CAN influence public narrative "
                "and stock price but CANNOT force a Specs shutdown through "
                "voting. This weakens the corporate survival binary — "
                "Spiegel can sustain Specs despite activist pressure."
            ),
        }
        self.assertEqual(confounder["strength"], "WEAK")


class TestFalsificationTests(unittest.TestCase):
    """Tests for conditions that would falsify the financial incentive hypothesis."""

    def test_falsification_proportionate_privacy_coverage(self):
        """If Specs receives proportionate privacy scrutiny at launch, hypothesis weakens."""
        falsification = {
            "condition": (
                "If publications apply comparable privacy-alarm vocabulary "
                "density to Snap Specs (4 cameras) as they do to Meta "
                "Ray-Ban (1 camera) during the Sep 16 launch window, "
                "the financial incentive hypothesis for Snap-specific "
                "coverage softness is falsified."
            ),
            "measurement": (
                "Count privacy-alarm terms per article for Specs launch "
                "vs Meta Ray-Ban launch coverage from the same publications. "
                "Normalize by article length. Compare vocabulary density."
            ),
        }
        self.assertIn("falsified", falsification["condition"])

    def test_falsification_adverse_herbst_brady_coverage(self):
        """If WIRED produces deeply adversarial Specs coverage, personnel bridge hypothesis weakens."""
        falsification = {
            "condition": (
                "If WIRED (under Herbst-Brady's revenue umbrella) produces "
                "a deeply adversarial privacy investigation of Snap Specs "
                "comparable to its Meta glasses coverage, the Herbst-Brady "
                "personnel convergence hypothesis is falsified."
            ),
        }
        self.assertIn("falsified", falsification["condition"])


class TestFinancialArchitectureComparison(unittest.TestCase):
    """Tests comparing Snap and Meta financial architectures with publishers."""

    def test_snap_publisher_revenue_relationships(self):
        """Snap has multiple publisher financial relationship channels."""
        snap_publisher = {
            "discover_platform": {
                "type": "revenue sharing",
                "conde_nast_confirmed": True,
                "partners_historical": [
                    "BuzzFeed",
                    "Condé Nast",
                    "Hearst",
                    "NBCU",
                    "Viacom",
                    "VICE",
                ],
            },
            "advertising_platform": {
                "type": "SMB and enterprise advertising",
                "q2_2026_ad_revenue_m": 1283,
                "competes_with_meta": True,
            },
            "snapchat_plus": {
                "subscribers_m": 25,
                "arr_b": 1.0,
                "type": "consumer subscription",
            },
            "meta_content_licensing_deals": 0,
            "meta_publisher_revenue_sharing": False,
        }
        self.assertTrue(snap_publisher["discover_platform"]["conde_nast_confirmed"])
        self.assertTrue(snap_publisher["advertising_platform"]["competes_with_meta"])

    def test_meta_publisher_relationship_deficit(self):
        """Meta has ZERO publisher financial alignment for smart glasses coverage."""
        meta_publisher = {
            "content_licensing_deals": 13,
            "content_deals_with_adversarial_publications": 0,
            "note": (
                "Meta has 13 publisher content deals but NONE with the "
                "publications that cover smart glasses most adversarially "
                "(WIRED, Gizmodo, The Verge). Condé Nast (WIRED's parent) "
                "has deals with OpenAI, Amazon, Microsoft, Perplexity, "
                "and is negotiating with Apple — but NOT Meta."
            ),
            "publisher_revenue_sharing": False,
            "publisher_ad_competition": True,
            "publisher_ad_competition_direction": "adversarial",
        }
        self.assertEqual(
            meta_publisher["content_deals_with_adversarial_publications"], 0
        )
        self.assertTrue(meta_publisher["publisher_ad_competition"])


class TestTimelineAndCrossReferences(unittest.TestCase):
    """Tests for temporal sequence and cross-mechanism references."""

    def test_timeline_of_events(self):
        """The timeline shows converging financial pressures toward Sep 16."""
        timeline = [
            {"date": "2025-11-05", "event": "Snap-Perplexity $400M deal announced"},
            {"date": "2026-01-28", "event": "Specs Inc. subsidiary established"},
            {"date": "2026-02-04", "event": "Perplexity integration delayed"},
            {"date": "2026-03-31", "event": "Irenic Capital letter demanding Specs shutdown"},
            {"date": "2026-04-10", "event": "Qualcomm partnership announced"},
            {"date": "2026-04-xx", "event": "April restructuring (~1,000 jobs cut)"},
            {"date": "2026-05-06", "event": "Perplexity deal officially terminated ($0 revenue)"},
            {"date": "2026-06-16", "event": "Spiegel defends Specs at AWE, announces Sep launch"},
            {"date": "2026-08-03", "event": "Q2 2026 earnings: EBITDA +505%, FCF positive"},
            {"date": "2026-08-22", "event": "THIS ANALYSIS: 25 days to consumer launch"},
            {"date": "2026-09-16", "event": "Specs consumer launch at $2,195"},
        ]
        self.assertEqual(len(timeline), 11)
        self.assertEqual(timeline[-1]["date"], "2026-09-16")

    def test_cross_references(self):
        """This mechanism extends and connects to multiple prior mechanisms."""
        cross_refs = [
            {
                "mechanism_id": 224,
                "relationship": "extends",
                "description": (
                    "Mechanism #224 documented the dual-AI-partner publisher "
                    "financial convergence for Snap Specs. This mechanism adds "
                    "the corporate structure (Specs Inc.), activist pressure "
                    "(Irenic), and temporal urgency (25-day window)."
                ),
            },
            {
                "mechanism_id": 231,
                "relationship": "extends",
                "description": (
                    "Mechanism #231 documented the CLAD quad-AI developer "
                    "ecosystem. This mechanism adds the financial survival "
                    "dimension: developer ecosystem value depends on Specs Inc. "
                    "surviving as a business unit."
                ),
            },
            {
                "mechanism_id": 91,
                "relationship": "context",
                "description": (
                    "Mechanism #91 documented Qualcomm co-marketing. Qualcomm's "
                    "partnership with Specs Inc. means co-marketing budgets are "
                    "at stake if Specs is killed per Irenic demands."
                ),
            },
            {
                "mechanism_id": 208,
                "relationship": "context",
                "description": (
                    "Mechanism #208 documented Herbst-Brady (ex-Snap) as Condé "
                    "Nast CRO. The Sep 16 launch creates a temporal convergence "
                    "point where her prior Snap career intersects with her "
                    "current revenue oversight of WIRED."
                ),
            },
        ]
        self.assertEqual(len(cross_refs), 4)
        mechanism_ids = [ref["mechanism_id"] for ref in cross_refs]
        self.assertIn(224, mechanism_ids)
        self.assertIn(231, mechanism_ids)


if __name__ == "__main__":
    unittest.main()
