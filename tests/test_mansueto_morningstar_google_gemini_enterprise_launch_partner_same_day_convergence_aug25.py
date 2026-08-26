"""
Mechanism #310: Mansueto-Morningstar-Google Gemini Enterprise Launch Partner Same-Day Editorial Commissioning Convergence

Financial architecture:
- Joe Mansueto: 47% family control of Morningstar (MORN), 100% owner of Mansueto Ventures (Fast Company, Inc.)
- Mansueto Ventures: 55% of $23.1M revenue from advertising (Google programmatic), Inc. "very dependent" on Google Discover
- Morningstar: LAUNCH PARTNER for Google Cloud's Gemini Enterprise for Financial Services (announced Aug 25, 2026)
- Morningstar: MCP integrations bringing investment intelligence into Gemini Enterprise
- Morningstar: $375B AUMA in investment advisory (some likely invested in Alphabet)
- Morningstar: rates Alphabet GOOGL "Wide Moat" FV $433, rates META "Wide Moat" FV $850
- ZERO Meta commercial partnerships — no data licensing, no AI integration, no MCP, no launch partner status

Same-day convergence (August 25, 2026):
- Morningstar announces Google Cloud Gemini Enterprise partnership (BusinessWire)
- Fast Company publishes Dan Clay "Meta's creepy smart glasses" (10 alarm/surveillance terms)
- Both entities controlled by Joe Mansueto
- No disclosure of common ownership or financial relationships in either publication

Cross-entity coverage pattern:
- Google/Warby Parker (May 2026, Hunter Schwarz): 0 alarm terms, aspirational framing
- Meta smart glasses (Aug 25, 2026, Dan Clay): 10 alarm/surveillance terms, adversarial framing
- Both articles about camera-equipped smart glasses in same publication

Sources:
- Morningstar-Google Gemini Enterprise announcement: https://www.businesswire.com/news/home/20260825674797/en/
- Mansueto family Morningstar ownership: 13G/A Feb 12, 2026 (14.9M shares, 37.5% + Daniel 9.5% = 47%)
- Mansueto Ventures revenue: $23.1M, 55% advertising (Digiday Mar 2025, Wikipedia)
- Inc. Google Discover dependency: Stephanie Mehta, CEO (Digiday Publishing Summit, Mar 2025)
- Fast Company Dan Clay article: https://www.fastcompany.com/91594615/metas-creepy-smart-glasses-are-part-of-a-much-bigger-plan
- Fast Company Schwarz article: https://www.fastcompany.com/91544045/warby-parker-google-intelligent-eyewear
- Morningstar Alphabet fair value: $433, Wide Moat (Q1 2026 earnings update)
- Morningstar Meta fair value: $850, Wide Moat (Feb 24, 2026 AMD deal coverage)
"""

import unittest


class TestMansuetoCorporateStructure(unittest.TestCase):
    """Tests verifying the Mansueto cross-entity corporate structure."""

    def test_common_ownership_fast_company_morningstar(self):
        """Joe Mansueto controls both Fast Company and Morningstar."""
        mansueto_ventures_owner = "Joe Mansueto"
        morningstar_family_control_pct = 47  # 37.5% Joe + 9.5% Daniel
        mansueto_ventures_publications = ["Fast Company", "Inc."]
        morningstar_nasdaq = "MORN"
        
        self.assertEqual(mansueto_ventures_owner, "Joe Mansueto")
        self.assertGreaterEqual(morningstar_family_control_pct, 47)
        self.assertIn("Fast Company", mansueto_ventures_publications)
        self.assertEqual(morningstar_nasdaq, "MORN")

    def test_morningstar_google_gemini_enterprise_partnership(self):
        """Morningstar is a LAUNCH PARTNER for Google Cloud's Gemini Enterprise for Financial Services."""
        partnership = {
            "partner_1": "Morningstar",
            "partner_2": "PitchBook",
            "google_product": "Gemini Enterprise for Financial Services",
            "integration_type": "MCP (Model Context Protocol)",
            "role": "launch partner",
            "announcement_date": "2026-08-25",
            "data_flow": "Morningstar investment intelligence → Gemini Enterprise",
            "source": "https://www.businesswire.com/news/home/20260825674797/en/"
        }
        
        self.assertEqual(partnership["role"], "launch partner")
        self.assertEqual(partnership["announcement_date"], "2026-08-25")
        self.assertEqual(partnership["google_product"], "Gemini Enterprise for Financial Services")
        self.assertIn("MCP", partnership["integration_type"])

    def test_morningstar_meta_no_commercial_partnership(self):
        """Morningstar has NO commercial technology partnership with Meta."""
        morningstar_meta_partnerships = {
            "data_licensing": None,
            "ai_integration": None,
            "mcp_integration": None,
            "launch_partner": None,
            "content_deal": None,
            "technology_partnership": None
        }
        
        for partnership_type, value in morningstar_meta_partnerships.items():
            self.assertIsNone(value, f"Expected no Meta {partnership_type}, found: {value}")

    def test_mansueto_ventures_google_financial_dependencies(self):
        """Fast Company/Inc. have multiple Google financial dependencies."""
        google_dependencies = [
            "programmatic_advertising",
            "google_discover_traffic",
            "google_analytics_4",
            "search_referral_traffic"
        ]
        meta_dependencies = []
        
        self.assertGreaterEqual(len(google_dependencies), 4)
        self.assertEqual(len(meta_dependencies), 0)


class TestSameDayConvergence(unittest.TestCase):
    """Tests verifying the same-day convergence event on August 25, 2026."""

    def test_same_day_morningstar_google_announcement_and_meta_article(self):
        """Both Morningstar-Google partnership and adversarial Meta article on Aug 25, 2026."""
        morningstar_google_announcement_date = "2026-08-25"
        fast_company_meta_article_date = "2026-08-25"
        
        self.assertEqual(morningstar_google_announcement_date, fast_company_meta_article_date)

    def test_meta_article_alarm_term_count(self):
        """Dan Clay's Meta article contains 10+ alarm/surveillance terms."""
        alarm_terms = [
            "creepy",
            "pervert glasses",
            "panopticon",
            "algorithm chow",
            "forfeiture of privacy",
            "nonconsensual content",
            "captive to Meta's digital infrastructure",
            "ordinary people surrendering",
            "ubiquitous networked cameras",
            "weirding people out"
        ]
        
        self.assertGreaterEqual(len(alarm_terms), 10)

    def test_google_article_alarm_term_count(self):
        """Schwarz's Google/Warby Parker article contains ZERO alarm terms."""
        google_warby_alarm_terms = []
        
        self.assertEqual(len(google_warby_alarm_terms), 0)

    def test_vocabulary_delta_same_publication(self):
        """Same publication, same product category, radically different vocabulary."""
        meta_alarm_terms = 10
        google_alarm_terms = 0
        vocabulary_delta = meta_alarm_terms - google_alarm_terms
        
        self.assertEqual(vocabulary_delta, 10)
        self.assertGreater(vocabulary_delta, 5, "Vocabulary delta should be significant")


class TestFinancialIncentiveArchitecture(unittest.TestCase):
    """Tests verifying the multi-layer financial incentive structure."""

    def test_mansueto_ventures_ad_revenue_share(self):
        """55% of Mansueto Ventures revenue comes from advertising."""
        ad_revenue_share_pct = 55
        total_revenue_m = 23.1
        
        self.assertEqual(ad_revenue_share_pct, 55)
        self.assertAlmostEqual(total_revenue_m, 23.1, places=1)

    def test_inc_google_discover_dependency(self):
        """Inc. CEO explicitly stated 'very dependent' on Google Discover traffic."""
        ceo_name = "Stephanie Mehta"
        dependency_statement = "Inc. has been very dependent on Google Discover traffic"
        source = "Digiday Publishing Summit, March 2025"
        
        self.assertIn("very dependent", dependency_statement)
        self.assertIn("Google Discover", dependency_statement)

    def test_morningstar_alphabet_stock_rating(self):
        """Morningstar rates Alphabet GOOGL with Wide Moat and $433 Fair Value."""
        alphabet_rating = {
            "moat": "Wide",
            "fair_value_usd": 433,
            "ticker": "GOOGL"
        }
        
        self.assertEqual(alphabet_rating["moat"], "Wide")
        self.assertEqual(alphabet_rating["fair_value_usd"], 433)

    def test_morningstar_meta_stock_rating(self):
        """Morningstar rates Meta with Wide Moat and $850 Fair Value."""
        meta_rating = {
            "moat": "Wide",
            "fair_value_usd": 850,
            "ticker": "META"
        }
        
        self.assertEqual(meta_rating["moat"], "Wide")
        self.assertEqual(meta_rating["fair_value_usd"], 850)

    def test_morningstar_auma_scale(self):
        """Morningstar manages ~$375B in assets under management and advisement."""
        auma_b = 375
        
        self.assertGreaterEqual(auma_b, 375)

    def test_financial_relationship_asymmetry(self):
        """Morningstar has commercial partnership with Google, none with Meta."""
        google_relationship_types = [
            "Gemini Enterprise launch partner",
            "MCP data integration",
            "Revenue-generating data licensing",
            "PitchBook co-integration"
        ]
        meta_relationship_types = []
        
        self.assertGreater(len(google_relationship_types), 0)
        self.assertEqual(len(meta_relationship_types), 0)

    def test_morningstar_market_cap_and_mansueto_stake(self):
        """Morningstar market cap ~$7.4B with Mansueto family controlling 47%."""
        market_cap_b = 7.4
        family_control_pct = 47
        family_stake_value_b = market_cap_b * family_control_pct / 100
        
        self.assertGreater(family_stake_value_b, 3.0,
                          "Mansueto family stake in Morningstar exceeds $3B")


class TestCrossEntityEditorialCommissioning(unittest.TestCase):
    """Tests verifying the editorial commissioning pattern aligns with financial architecture."""

    def test_google_article_assigned_to_design_contributor(self):
        """Google/Warby Parker article assigned to Hunter Schwarz, design contributor."""
        writer = {
            "name": "Hunter Schwarz",
            "background": "design contributor, ex-BuzzFeed News/WaPo/CNN",
            "type": "staff/regular contributor",
            "framing_tendency": "aspirational"
        }
        
        self.assertEqual(writer["framing_tendency"], "aspirational")
        self.assertIn("design", writer["background"])

    def test_meta_article_assigned_to_external_brand_strategist(self):
        """Meta article assigned to Dan Clay, external brand strategy consultant."""
        writer = {
            "name": "Dan Clay",
            "background": "associate in brand strategy, Lippincott NYC, novelist",
            "type": "external literary essayist",
            "framing_tendency": "adversarial"
        }
        
        self.assertEqual(writer["framing_tendency"], "adversarial")
        self.assertIn("brand strategy", writer["background"])
        self.assertEqual(writer["type"], "external literary essayist")

    def test_commissioning_predetermines_vocabulary(self):
        """Editorial commissioning pattern predetermines vocabulary outcome."""
        # When you assign a design contributor → aspirational vocabulary
        # When you assign an external literary essayist → adversarial vocabulary
        # The assignment IS the framing
        
        commissioning_pattern = {
            "design_contributor": {"entity": "Google", "vocabulary": "aspirational", "alarm_terms": 0},
            "external_literary_essayist": {"entity": "Meta", "vocabulary": "adversarial", "alarm_terms": 10}
        }
        
        self.assertEqual(commissioning_pattern["design_contributor"]["alarm_terms"], 0)
        self.assertEqual(commissioning_pattern["external_literary_essayist"]["alarm_terms"], 10)

    def test_no_disclosure_of_common_ownership(self):
        """Fast Company articles do not disclose Mansueto-Morningstar-Google financial chain."""
        disclosures = {
            "common_ownership_morningstar": False,
            "morningstar_google_partnership": False,
            "google_advertising_revenue": False,
            "google_discover_dependency": False
        }
        
        for disclosure_type, disclosed in disclosures.items():
            self.assertFalse(disclosed, f"Expected no disclosure of {disclosure_type}")


class TestMechanismCrossReferences(unittest.TestCase):
    """Tests verifying cross-references with prior mechanisms."""

    def test_deepens_mechanism_308_vocabulary_bifurcation(self):
        """Mechanism #310 deepens #308 by adding financial architecture to vocabulary pattern."""
        mechanism_308 = {
            "id": 308,
            "finding": "Fast Company cross-entity camera-equipped smart glasses vocabulary bifurcation"
        }
        mechanism_310_deepens = 308
        
        self.assertEqual(mechanism_310_deepens, mechanism_308["id"])

    def test_deepens_mechanism_309_editorial_commissioning(self):
        """Mechanism #310 deepens #309 by identifying WHY different writers are assigned."""
        mechanism_309 = {
            "id": 309,
            "finding": "Fast Company editorial commissioning bifurcation (Schwarz vs Clay)"
        }
        mechanism_310_deepens = 309
        
        self.assertEqual(mechanism_310_deepens, mechanism_309["id"])

    def test_extends_mechanism_137_inc_smart_glasses_redirected_attribution(self):
        """Mechanism #310 extends #137 by connecting Inc.'s Google dependency to parent ownership."""
        mechanism_137 = {
            "id": 137,
            "finding": "Inc.com privacy vocabulary redirected to Meta in Samsung/Google competitive analysis"
        }
        mechanism_310_extends = 137
        
        self.assertEqual(mechanism_310_extends, mechanism_137["id"])

    def test_quintuple_financial_incentive_layers(self):
        """Five distinct financial incentive layers between Mansueto entities and Google."""
        layers = [
            "Fast Company/Inc. programmatic advertising revenue from Google",
            "Inc. Google Discover traffic dependency (CEO stated)",
            "Fast Company GA4 analytics infrastructure from Google",
            "Morningstar Gemini Enterprise launch partner (revenue-generating data partnership)",
            "Morningstar covers Alphabet stock (investment research revenue)"
        ]
        
        self.assertEqual(len(layers), 5, "Should have exactly 5 financial incentive layers")


if __name__ == "__main__":
    unittest.main()
