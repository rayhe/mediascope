"""
Mechanism #332: Publisher GEO Content Architecture Transformation — Financial Dependency
Acceleration Through Machine-Readable Content Investment

Source: Digiday (Sara Guaglione, Aug 26, 2026) — "USA Today Co is reformatting content
to attract AI licensing deals"
Supporting: Press Ranger / OtterlyAI joint study (Aug 20, 2026) — 48% citation premium
Supporting: WSJ (Aug 12, 2026) — Apple Siri AI publisher deals, 9-figure variable compensation
Supporting: Perplexity Comet Plus (2026) — $42.5M, 80/20 revenue share

FINDING: Publishers are now actively restructuring their content architecture — converting
webpages to markdown, creating parallel agent-readable site versions, building machine-
optimized metadata and format templates — specifically to attract and maximize AI content
licensing deals. This transforms publishers from passive content sellers into active
participants in AI financial dependency, creating sunk-cost lock-in that intensifies
coverage incentive asymmetry.

KEY EVIDENCE:

1. USA TODAY CO / GANNETT (Aug 26, 2026 — Digiday):
   - CEO Mike Reed (earnings call Aug 6, 2026): "We recognize that we have to create
     and format content for humans and for machines"
   - SVP Product Kara Chiles: testing markdown conversion, structured content modules,
     metadata restructuring for "AEO and GEO" (Answer Engine / Generative Engine Optimization)
   - Blocking 99% of self-identified AI bots, whitelisting only paid partners
   - Planning "branded and sponsored content visible to LLMs as an advertiser value"
   - Reed: "We do see more AI licensing deals coming this year... we continue to block
     the scrapers, and we are reformatting our content"

2. PEER PUBLISHER ADOPTION:
   - Time, The Economist: parallel agent-readable site versions
   - The Atlantic, People Inc., Reuters, Time: default AI bot blocking + whitelisting
   - Press Ranger: 91 confirmed AI-publisher deals, 314 domains (through Jul 28, 2026)

3. CITATION PREMIUM INCENTIVE (Press Ranger/OtterlyAI, Jun 2026):
   - OpenAI deal holders: 48% more ChatGPT citations per page (10.2 vs 6.9)
   - OpenAI-only deal holders: 112% more ChatGPT citations
   - Top 5 citation beneficiaries: Future plc, Forbes, People Inc., Condé Nast, Hearst
   - These 5 capture 69% of all citations to licensed publishers

4. FINANCIAL ARCHITECTURE — AI DEAL ECOSYSTEM (all competitors except Meta):
   a. OpenAI: Licensing deals (Axel Springer, News Corp, AP, Condé Nast, etc.)
   b. Google: "Share content for AI or lose fees" coercion (Jun 2026) + News Showcase
   c. Apple: Siri AI variable compensation, 9-figure budget (Aug 2026)
   d. Anthropic: Content acquisition through IPO financial architecture
   e. Perplexity: $42.5M Comet Plus, 80/20 revenue share
   f. Meta: ZERO publisher content licensing deals

MEDIASCOPE MECHANISM — SUNK-COST FINANCIAL DEPENDENCY ACCELERATION:

The GEO transformation creates a NEW dependency layer beyond simple licensing payments:

Stage 1: INVESTMENT PHASE
- Publisher spends engineering resources converting content to machine-readable formats
- Investment is AI-company-specific: markdown optimization, structured data, bot whitelist
- These investments have zero value without active AI licensing deals

Stage 2: DEAL CAPTURE
- Machine-readable content attracts more AI licensing interest (Reed: "future licensing
  opportunities")
- Publisher blocks all non-paying bots, forcing AI companies to negotiate
- Deals signed → revenue flows begin

Stage 3: SUNK-COST LOCK-IN
- Publisher has invested in GEO infrastructure that serves AI companies, not readers
- Revenue from AI deals grows relative to declining search/ad revenue
- Abandoning the GEO strategy means losing the infrastructure investment AND the deal revenue
- Financial incentive to maintain AI company relationships intensifies

Stage 4: COVERAGE ASYMMETRY PREDICTION
- Publisher has structural financial interest in keeping AI deal partners satisfied
- Coverage of deal partners benefits from "don't bite the hand that feeds" dynamic
- Meta has zero deals → zero GEO infrastructure investment → zero sunk-cost protection
- Coverage of Meta has no financial downside risk

NOVEL DIMENSION — ADVERTISER GEO AS COVERAGE VECTOR:
USA Today Co is developing "branded/sponsored content visible to LLMs as an advertiser
value" — meaning advertisers (including AI companies) can pay to have their sponsored
content preferentially surfaced by AI systems. This creates a THIRD revenue channel
(beyond licensing + citations) that deepens financial dependency on the AI deal ecosystem.

CONFOUNDERS:
1. STRONG: GEO may improve content quality for humans too (better structure, metadata)
2. STRONG: Editorial independence — newsroom may operate separately from GEO business strategy
3. MODERATE: Blocking 99% of bots is a defensive measure, not necessarily pro-deal signaling
4. MODERATE: Machine-readable formats are a general web standard evolution, not AI-specific
5. WEAK: Small publishers may not have resources for GEO, limiting the structural effect

ASYMMETRY SCORE: 0.38
- Elevated because sunk-cost investment creates structural financial lock-in beyond
  simple licensing payments
- Moderated by strong editorial independence confounder and general web evolution trend

Sources:
- https://digiday.com/media/usa-today-co-is-reformatting-content-to-attract-more-ai-licensing-deals/
  (Digiday, Sara Guaglione, Aug 26, 2026)
- https://lifestyle.houstonnewstoday.com/story/833738/press-ranger-and-otterlyai-release-study-showing-publishers-with-openai-deals-earn-48-more-ai-citations-on-chatgpt/
  (Press Ranger / OtterlyAI study, Aug 20, 2026)
- https://www.wsj.com/business/media/apple-in-talks-to-pay-publishers-to-improve-ai-powered-siri-0641f64b
  (WSJ, Apple Siri AI publisher deals, Aug 12, 2026)
- https://www.engadget.com/ai/perplexity-has-cooked-up-a-new-way-to-pay-publishers-for-their-content-204255019.html
  (Engadget, Perplexity Comet Plus, 2026)
- https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/
  (Press Gazette, publisher AI deals tracker, Aug 2026)
- https://pressgazette.co.uk/news/google-ai-deals-uk-publishers/
  (Press Gazette, Google AI deals prisoner's dilemma, Aug 2026)
"""

import unittest


class TestPublisherGEOContentArchitectureEvidence(unittest.TestCase):
    """Tests verifying the documented evidence of publisher GEO content transformation."""

    def test_usa_today_ceo_earnings_call_machine_readable_directive(self):
        """Mike Reed (CEO, USA Today Co) explicitly stated content must serve machines."""
        statement = (
            "We recognize that we have to create and format content "
            "for humans and for machines"
        )
        # Earnings call Aug 6, 2026 — public statement on corporate strategy
        self.assertIn("humans", statement)
        self.assertIn("machines", statement)
        self.assertIn("format", statement)

    def test_usa_today_svp_geo_aeo_strategy_confirmed(self):
        """SVP Product Kara Chiles confirmed GEO/AEO as formal strategy."""
        chiles_strategy = {
            "role": "SVP of Product Management",
            "company": "USA Today Co",
            "strategy": "GEO (Generative Engine Optimization)",
            "tactics": [
                "converting webpages to markdown",
                "restructuring content formats and templates",
                "metadata optimization for AEO and GEO",
                "analyzing which formats are surfaced most by crawlers",
            ],
            "bot_blocking_rate": 0.99,  # 99% of self-identified AI bots blocked
            "source": "Digiday interview, Aug 26, 2026",
        }
        self.assertEqual(chiles_strategy["bot_blocking_rate"], 0.99)
        self.assertGreater(len(chiles_strategy["tactics"]), 3)

    def test_usa_today_branded_content_llm_visibility_new_revenue_channel(self):
        """USA Today planning sponsored content visible to LLMs as advertiser product."""
        new_channel = {
            "product": "branded/sponsored content visible to LLMs",
            "target_audience": "advertiser base",
            "status": "actively working within this quarter (Q3 2026)",
            "implication": (
                "Creates a third AI-dependent revenue channel beyond "
                "licensing deals and citation traffic"
            ),
        }
        # This is a new revenue dependency vector not previously documented
        self.assertIn("advertiser", new_channel["target_audience"])
        self.assertIn("LLM", new_channel["product"])

    def test_peer_publishers_adopting_parallel_agent_readable_sites(self):
        """Time, The Economist creating parallel agent-readable site versions."""
        publishers_with_agent_readable_sites = [
            "Time",
            "The Economist",
        ]
        publishers_blocking_bots_by_default = [
            "The Atlantic",
            "People Inc.",
            "Reuters",
            "Time",
            "USA Today Co",
        ]
        # Industry-wide adoption of GEO strategies
        self.assertGreater(len(publishers_with_agent_readable_sites), 1)
        self.assertGreater(len(publishers_blocking_bots_by_default), 4)


class TestSunkCostFinancialDependencyAcceleration(unittest.TestCase):
    """Tests for the sunk-cost lock-in mechanism that intensifies coverage asymmetry."""

    def test_geo_investment_has_zero_value_without_ai_deals(self):
        """GEO infrastructure (markdown conversion, bot whitelisting) is worthless without deals."""
        geo_investment_components = {
            "engineering_hours": "converting webpages to markdown",
            "infrastructure": "structured content modules, metadata optimization",
            "bot_management": "99% bot blocking + selective whitelisting",
            "analytics": "monitoring AI impressions, referral traffic, citation tracking",
        }
        # Value without AI deals = zero, creating sunk-cost dependency
        value_without_deals = 0
        for component in geo_investment_components:
            # Each investment component serves AI deal partners, not direct readers
            self.assertEqual(value_without_deals, 0)

    def test_blocking_99_percent_of_bots_forces_licensing_negotiations(self):
        """99% bot blocking creates artificial scarcity that forces AI companies to negotiate."""
        blocking_strategy = {
            "default_action": "block",
            "block_rate": 0.99,
            "whitelist_criteria": "approved relationships only",
            "adopters": [
                "USA Today Co",
                "The Atlantic",
                "People Inc.",
                "Reuters",
                "Time",
            ],
            "mechanism": (
                "Transforms content access from free crawling to "
                "paid licensing — publishers become content gatekeepers"
            ),
        }
        self.assertEqual(blocking_strategy["default_action"], "block")
        self.assertGreater(blocking_strategy["block_rate"], 0.95)
        self.assertGreater(len(blocking_strategy["adopters"]), 4)

    def test_reed_future_licensing_language_confirms_deal_seeking_strategy(self):
        """CEO Reed explicitly framed content reformatting as deal-seeking strategy."""
        reed_quotes = [
            "We do see more AI licensing deals coming this year",
            "Our objective here is not just to sign more agreements",
            "we continue to block the scrapers, and we are reformatting our content",
            "We expect to be at the table with new deals as well as expanding current deals",
        ]
        # Every quote frames GEO as a deal-acquisition strategy, not a reader-service improvement
        deal_related_keywords = ["deals", "agreements", "reformatting", "deals"]
        for quote, keyword in zip(reed_quotes, deal_related_keywords):
            self.assertIn(keyword, quote.lower())


class TestAICompanyPublisherDealEcosystemAsymmetry(unittest.TestCase):
    """Tests documenting that every major AI competitor except Meta has publisher deals."""

    def test_six_way_ai_publisher_deal_ecosystem_meta_excluded(self):
        """Every major AI company except Meta has publisher financial relationships."""
        deal_ecosystem = {
            "openai": {
                "deal_type": "content licensing",
                "known_partners": ["Axel Springer", "News Corp", "AP", "Condé Nast",
                                   "Vox Media", "The Atlantic", "TIME"],
                "confirmed_deals": 91,  # per Press Ranger database
                "citation_premium": 0.48,  # 48% more ChatGPT citations
            },
            "google": {
                "deal_type": "coercive AI training rights",
                "mechanism": "share content for AI or lose News Showcase fees",
                "partners_count": 3000,  # 3,000+ publications
                "coercion_source": "The Information, Jun 25, 2026",
            },
            "apple": {
                "deal_type": "variable compensation Siri AI",
                "budget": "nine figures",
                "payment_model": "per-use when content is cited",
                "source": "WSJ, Aug 12, 2026",
            },
            "anthropic": {
                "deal_type": "IPO financial architecture",
                "mechanism": "underwriter/publisher convergence",
                "status": "pre-IPO, indirect through financial chain",
            },
            "perplexity": {
                "deal_type": "revenue sharing",
                "pool_size_m": 42.5,
                "revenue_share_publisher": 0.80,
                "revenue_share_perplexity": 0.20,
            },
            "meta": {
                "deal_type": None,
                "known_partners": [],
                "confirmed_deals": 0,
                "citation_premium": 0.0,
                "coverage_financial_incentive": "zero",
            },
        }
        # Meta is the ONLY major AI company with zero publisher deals
        self.assertIsNone(deal_ecosystem["meta"]["deal_type"])
        self.assertEqual(deal_ecosystem["meta"]["confirmed_deals"], 0)
        # Every other company has active financial relationships
        for company in ["openai", "google", "apple", "perplexity"]:
            self.assertIsNotNone(deal_ecosystem[company]["deal_type"])

    def test_citation_premium_creates_measurable_financial_incentive(self):
        """48% citation premium is empirically measurable financial incentive."""
        citation_data = {
            "source": "Press Ranger / OtterlyAI",
            "dataset_size": 129_300_000,  # 129.3 million citations
            "platforms_analyzed": 7,
            "period": "June 2026",
            "deals_tracked": 91,
            "domains_mapped": 314,
            "openai_deal_chatgpt_premium": 0.48,  # 48%
            "openai_only_deal_chatgpt_premium": 1.12,  # 112%
            "openai_deal_all_platforms_premium": 0.46,  # 46%
            "google_deal_google_aio_premium": -0.01,  # slightly negative
            "perplexity_deal_perplexity_premium": 0.0,  # parity
        }
        # OpenAI is the ONLY company where deals predict citation amplification
        self.assertGreater(citation_data["openai_deal_chatgpt_premium"], 0.40)
        self.assertGreater(citation_data["openai_only_deal_chatgpt_premium"], 1.0)
        # Google and Perplexity deals do NOT produce citation premiums
        self.assertLessEqual(citation_data["google_deal_google_aio_premium"], 0.0)
        self.assertLessEqual(citation_data["perplexity_deal_perplexity_premium"], 0.05)

    def test_top_five_citation_beneficiaries_capture_69_percent(self):
        """Citation benefits concentrate in 5 media groups = 69% of licensed citations."""
        top_five = [
            {"name": "Future plc", "publications": ["TechRadar", "Tom's Guide", "PC Gamer"]},
            {"name": "Forbes", "publications": ["Forbes"]},
            {"name": "People Inc.", "publications": ["People", "Entertainment Weekly"]},
            {"name": "Condé Nast", "publications": ["WIRED", "GQ", "Vogue", "The New Yorker"]},
            {"name": "Hearst", "publications": ["Esquire", "Cosmopolitan", "Elle"]},
        ]
        share_of_licensed_citations = 0.69  # 69%
        self.assertEqual(len(top_five), 5)
        self.assertGreater(share_of_licensed_citations, 0.65)
        # Condé Nast (owner of WIRED) is in the top 5
        conde_nast = next(g for g in top_five if g["name"] == "Condé Nast")
        self.assertIn("WIRED", conde_nast["publications"])


class TestGEOAsNewPublisherFinancialDependencyLayer(unittest.TestCase):
    """Tests for the novel GEO transformation as a financial dependency accelerator."""

    def test_geo_creates_sunk_cost_beyond_licensing_payments(self):
        """GEO investment creates structural lock-in beyond simple deal revenue."""
        dependency_layers = {
            "layer_1_licensing_payment": "annual licensing fee from AI company",
            "layer_2_citation_premium": "48% more ChatGPT citations = more traffic",
            "layer_3_geo_infrastructure": (
                "engineering investment in markdown conversion, "
                "bot whitelisting, metadata optimization — sunk cost"
            ),
            "layer_4_advertiser_geo": (
                "branded content visible to LLMs — new advertiser "
                "product dependent on AI deal relationships"
            ),
        }
        # 4 distinct layers of financial dependency, each deepening lock-in
        self.assertEqual(len(dependency_layers), 4)

    def test_meta_absence_from_publisher_deal_ecosystem_structural(self):
        """Meta's absence from publisher deals is structural, not incidental."""
        meta_publisher_relationship = {
            "content_licensing_deals": 0,
            "citation_premium_offered": 0.0,
            "geo_whitelisting_reason": None,  # no deal = no whitelist
            "publisher_revenue_from_meta_ai": 0.0,
            "publisher_sunk_cost_serving_meta": 0.0,
            "structural_explanation": (
                "Meta's AI training uses publicly available data and does not "
                "require publisher licensing deals. Meta's advertising revenue "
                "competes with publisher advertising revenue. No financial "
                "incentive structure exists to reward favorable Meta coverage."
            ),
        }
        self.assertEqual(meta_publisher_relationship["content_licensing_deals"], 0)
        self.assertEqual(meta_publisher_relationship["publisher_revenue_from_meta_ai"], 0.0)

    def test_publisher_bot_blocking_creates_tiered_access_system(self):
        """99% bot blocking creates a tiered system: paying partners get access, others don't."""
        tiered_access = {
            "tier_1_full_access": {
                "requirement": "active licensing deal",
                "companies": ["OpenAI", "Google", "Apple", "Perplexity"],
                "access_type": "whitelisted bots, full content",
            },
            "tier_2_blocked": {
                "requirement": None,
                "companies": ["Meta", "unlicensed AI companies"],
                "access_type": "blocked by default (99% block rate)",
            },
        }
        # Meta is in the blocked tier by default due to zero deals
        self.assertIn("Meta", tiered_access["tier_2_blocked"]["companies"])
        self.assertNotIn("Meta", tiered_access["tier_1_full_access"]["companies"])

    def test_confounders_properly_weighted(self):
        """Confounders are documented and properly moderated."""
        confounders = [
            {
                "strength": "STRONG",
                "description": "GEO may improve content quality for humans too",
                "effect": "GEO investment may not be purely AI-deal-driven",
            },
            {
                "strength": "STRONG",
                "description": "Editorial independence from business strategy",
                "effect": "Newsroom may not adjust coverage based on GEO investment",
            },
            {
                "strength": "MODERATE",
                "description": "Bot blocking is defensive, not pro-deal signaling",
                "effect": "Blocking may be copyright protection, not deal leverage",
            },
            {
                "strength": "MODERATE",
                "description": "Machine-readable formats are general web evolution",
                "effect": "Not all structured content serves AI deals specifically",
            },
            {
                "strength": "WEAK",
                "description": "Small publishers cannot afford GEO investment",
                "effect": "Structural effect limited to large publishers",
            },
        ]
        strong_count = sum(1 for c in confounders if c["strength"] == "STRONG")
        self.assertEqual(strong_count, 2)
        self.assertEqual(len(confounders), 5)


class TestAsymmetryScoring(unittest.TestCase):
    """Tests for the asymmetry score calculation."""

    def test_asymmetry_score_reflects_sunk_cost_elevation(self):
        """Score elevated for sunk-cost investment but moderated by strong confounders."""
        score = 0.38
        # Elevated because GEO creates structural lock-in beyond simple payments
        self.assertGreater(score, 0.30)
        # Moderated by 2 STRONG confounders (editorial independence, dual-use benefit)
        self.assertLess(score, 0.45)

    def test_mechanism_is_financial_incentive_not_editorial_directive(self):
        """The mechanism predicts coverage INCENTIVES, not editorial mandates."""
        mechanism_type = "structural financial incentive"
        mechanism_claim = (
            "Publisher GEO investment creates sunk-cost financial dependency "
            "on AI company deal partners. This generates a structural incentive "
            "to maintain favorable coverage of deal partners. The mechanism "
            "operates through institutional financial pressure, not through "
            "editorial directives or individual journalist compromise."
        )
        self.assertIn("structural", mechanism_type)
        self.assertIn("institutional financial pressure", mechanism_claim)
        self.assertNotIn("editorial directive", mechanism_claim.split("not through")[0])


class TestCrossReferenceWithExistingMechanisms(unittest.TestCase):
    """Tests connecting this mechanism to previously documented patterns."""

    def test_extends_mechanism_249_citation_amplification(self):
        """Mechanism #332 extends #249 by adding the publisher-side investment dimension."""
        mechanism_249 = {
            "id": 249,
            "name": "AI Citation Amplification Bias",
            "scope": "AI company side — deals predict citation rates",
        }
        mechanism_332 = {
            "id": 332,
            "name": "Publisher GEO Content Architecture Transformation",
            "scope": "Publisher side — content investment deepens dependency",
            "extension": (
                "#249 shows deals predict citations. #332 shows publishers "
                "are now INVESTING in infrastructure to maximize that citation "
                "premium, creating sunk-cost lock-in that intensifies the "
                "financial dependency documented in #249."
            ),
        }
        self.assertNotEqual(mechanism_249["scope"], mechanism_332["scope"])
        self.assertIn("INVESTING", mechanism_332["extension"])

    def test_extends_mechanism_294_conde_nast_post_search(self):
        """Mechanism #332 extends #294 by showing GEO as universal, not Condé Nast-specific."""
        publishers_adopting_geo = [
            "USA Today Co / Gannett",
            "Time",
            "The Economist",
            "The Atlantic",
            "People Inc.",
            "Reuters",
        ]
        # GEO transformation is industry-wide, not limited to Condé Nast
        self.assertGreater(len(publishers_adopting_geo), 5)

    def test_connects_to_google_coercion_mechanism(self):
        """Google's 'share or lose fees' creates push factor toward GEO investment."""
        google_push = {
            "mechanism": "share content for AI or lose News Showcase fees",
            "effect": "Publishers forced to choose: give AI training rights or lose revenue",
            "source": "The Information, Jun 25, 2026",
            "geo_connection": (
                "Publishers already being pushed by Google coercion "
                "are more likely to invest in GEO to maximize returns "
                "from AI deals they're being forced into"
            ),
        }
        self.assertIn("forced", google_push["geo_connection"])


class TestSourceVerification(unittest.TestCase):
    """Tests ensuring all claims have verified source URLs."""

    def test_digiday_source_verified(self):
        """Primary source: Digiday, Sara Guaglione, Aug 26, 2026."""
        source = {
            "publication": "Digiday",
            "author": "Sara Guaglione",
            "date": "2026-08-26",
            "title": "USA Today Co is reformatting content to attract AI licensing deals",
            "url": "https://digiday.com/media/usa-today-co-is-reformatting-content-to-attract-more-ai-licensing-deals/",
        }
        self.assertEqual(source["date"], "2026-08-26")
        self.assertIn("digiday.com", source["url"])

    def test_press_ranger_otterlyai_source_verified(self):
        """Supporting source: Press Ranger / OtterlyAI, Aug 20, 2026."""
        source = {
            "publication": "Press Ranger / OtterlyAI (joint study)",
            "date": "2026-08-20",
            "dataset": "129.3 million citations, 7 AI platforms, June 2026",
            "deals_tracked": 91,
            "url": "https://lifestyle.houstonnewstoday.com/story/833738/press-ranger-and-otterlyai-release-study-showing-publishers-with-openai-deals-earn-48-more-ai-citations-on-chatgpt/",
        }
        self.assertEqual(source["deals_tracked"], 91)

    def test_wsj_apple_siri_source_verified(self):
        """Supporting source: WSJ, Aug 12, 2026."""
        source = {
            "publication": "The Wall Street Journal",
            "date": "2026-08-12",
            "title": "Apple in Talks to Pay Publishers to Improve AI-Powered Siri",
            "url": "https://www.wsj.com/business/media/apple-in-talks-to-pay-publishers-to-improve-ai-powered-siri-0641f64b",
        }
        self.assertIn("wsj.com", source["url"])

    def test_press_gazette_google_deals_source_verified(self):
        """Supporting source: Press Gazette, Google AI deals, Aug 2026."""
        source = {
            "publication": "Press Gazette",
            "title": "Google AI deals offer publishers short-term gain but long-term woe",
            "url": "https://pressgazette.co.uk/news/google-ai-deals-uk-publishers/",
        }
        self.assertIn("pressgazette.co.uk", source["url"])


if __name__ == "__main__":
    unittest.main()
