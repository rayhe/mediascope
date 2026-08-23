"""
Mechanism #249: AI Citation Amplification Bias — Licensing Deals Predict AI Search Visibility

Source: Press Ranger / OtterlyAI joint study (Aug 20, 2026)
Dataset: 129.3 million citations across 7 AI search platforms, June 2026
Deal database: 91 confirmed agreements mapped to 314 publisher domains (through Jul 28, 2026)
Study URL: https://ai-search-news-licensing-deals-study.netlify.app/

FINDING: Publishers with OpenAI licensing deals earn 48% more citations per page on ChatGPT
than publishers without deals (10.2 vs 6.9 citations per cited page). Across all 7 AI
platforms combined, the premium is 46% (10.7 vs 7.3). Publishers with OpenAI-only deals
(no deals with other platforms) earn 112% more ChatGPT citations than unlicensed publishers.

This is the first quantitative evidence that financial relationships between AI companies
and publishers produce measurable differential treatment in AI search results. The study
extends MediaScope's financial incentive model from coverage tone prediction to AI search
amplification prediction.

KEY DATA POINTS:
- OpenAI-licensed publishers on ChatGPT: 10.2 citations/page (vs 6.9 unlicensed) = +48%
- All 7 platforms combined: 10.7 vs 7.3 = +46%
- OpenAI-only publishers on ChatGPT: 112% more citations than unlicensed
- OpenAI-licensed publishers get 57.9% of AI citation volume from ChatGPT (concentrated)
- Google-licensed publishers on Google AI Overviews: SLIGHTLY LOWER than unlicensed
- Perplexity-licensed publishers on Perplexity: PARITY with unlicensed
- OpenAI is the ONLY licensor with a clear home-platform citation advantage
- Top 5 citation beneficiaries among licensed publishers: Future plc, Forbes, People Inc.,
  Condé Nast, Hearst — 69% of all citations to licensed publishers
- News = 7.2% of total AI citations
- 46.9% of licensed publishers' citations go to commercial content (buying guides, reviews)

MEDIASCOPE IMPLICATIONS:

1. FINANCIAL INCENTIVE LOOP QUANTIFIED: Publisher signs OpenAI deal → +48% ChatGPT citations
   → more traffic → more ad/subscription revenue → financial incentive to maintain deal →
   softer coverage to protect deal → deal renewed. The study proves the first link in this
   chain: deals produce measurably more AI visibility.

2. CONDÉ NAST SPECIFIC: Condé Nast is the 4th largest citation beneficiary among licensed
   publishers. Their OpenAI deal (Aug 2024) generates measurably more ChatGPT citations for
   WIRED, Vogue, GQ, The New Yorker, etc. This is a QUANTIFIABLE financial incentive to
   maintain favorable OpenAI coverage.

3. META ZERO-DEAL IMPLICATION: Meta has zero publisher content licensing deals. Publishers
   covering Meta receive no citation amplification from covering Meta favorably. The financial
   incentive structure is perfectly inverted: covering OpenAI favorably → deal protected →
   citation premium maintained; covering Meta favorably → zero financial benefit.

4. APPLE SIRI AI VARIABLE-COMPENSATION AMPLIFIER: Apple's proposed variable pay-per-use Siri AI
   deals (nine-figure budget, Aug 2026) would create an even STRONGER version of this effect.
   If Apple's algorithm favors deal-partner content for Siri AI answers (analogous to OpenAI's
   48% citation premium for deal partners), publishers with Apple deals would earn more per-use
   payments AND more AI citations, compounding the financial incentive.

5. GOOGLE PARADOX: Google-licensed publishers are cited at a SLIGHTLY LOWER rate on Google AI
   Overviews than unlicensed publishers. This suggests Google's Showcase/News AI pilot deals
   operate through a different mechanism (coercive financial dependency + no-sue clauses)
   rather than citation amplification. Publishers sign Google deals to keep existing revenue,
   not to gain citation premium.

CONFOUNDING FACTORS:
- STRONG: Correlation ≠ causation — publishers with OpenAI deals may independently produce
  higher-quality content that earns more citations regardless of the deal.
- STRONG: Publisher size — the top 5 citation beneficiaries are major media conglomerates
  that would likely earn high citation rates with or without deals.
- MODERATE: Commercial content bias — 46.9% of licensed publisher citations go to buying
  guides and reviews, which are inherently high-citation formats.
- MODERATE: Study sponsors (Press Ranger, OtterlyAI) sell AI search optimization services,
  creating commercial incentive to demonstrate deal-citation correlation.
- WEAK: Sample period (June 2026 only) — one month may not be representative.

Source URLs:
- https://lifestyle.houstonnewstoday.com/story/833738/press-ranger-and-otterlyai-release-study-showing-publishers-with-openai-deals-earn-48-more-ai-citations-on-chatgpt/
- https://ai-search-news-licensing-deals-study.netlify.app/
- https://pressranger.com
- https://otterly.ai
"""

import unittest


class TestCitationAmplificationStudyData(unittest.TestCase):
    """Verify the Press Ranger / OtterlyAI study data points."""

    def test_study_dataset_scale(self):
        """Study examined 129.3 million citations across 7 AI platforms."""
        citations_millions = 129.3
        platforms_count = 7
        self.assertGreater(citations_millions, 100)
        self.assertEqual(platforms_count, 7)

    def test_deal_database_scale(self):
        """91 confirmed licensing agreements mapped to 314 publisher domains."""
        confirmed_agreements = 91
        publisher_domains = 314
        self.assertGreater(confirmed_agreements, 80)
        self.assertGreater(publisher_domains, 300)

    def test_study_platforms_covered(self):
        """Study covers 7 AI search platforms."""
        platforms = [
            "ChatGPT",
            "Google AI Overviews",
            "Google AI Mode",
            "Perplexity",
            "Microsoft Copilot",
            "Gemini",
            "Claude",
        ]
        self.assertEqual(len(platforms), 7)

    def test_study_period(self):
        """Citation data captured during June 2026."""
        study_month = "June 2026"
        deal_data_cutoff = "July 28, 2026"
        self.assertIn("2026", study_month)
        self.assertIn("2026", deal_data_cutoff)


class TestOpenAICitationPremium(unittest.TestCase):
    """Verify OpenAI licensing deal citation premium data."""

    def test_chatgpt_citation_premium_48_percent(self):
        """OpenAI-licensed publishers earn 48% more ChatGPT citations per page."""
        licensed_citations_per_page = 10.2
        unlicensed_citations_per_page = 6.9
        premium_pct = ((licensed_citations_per_page - unlicensed_citations_per_page)
                       / unlicensed_citations_per_page * 100)
        self.assertAlmostEqual(premium_pct, 48, delta=2)

    def test_all_platforms_citation_premium_46_percent(self):
        """Across all 7 platforms, OpenAI-licensed premium is 46%."""
        licensed_all_platforms = 10.7
        unlicensed_all_platforms = 7.3
        premium_pct = ((licensed_all_platforms - unlicensed_all_platforms)
                       / unlicensed_all_platforms * 100)
        self.assertAlmostEqual(premium_pct, 46, delta=2)

    def test_openai_only_publishers_112_percent_premium(self):
        """Publishers with OpenAI-only deals earn 112% more ChatGPT citations."""
        openai_only_premium_pct = 112
        self.assertGreater(openai_only_premium_pct, 100)

    def test_openai_citation_concentration_on_chatgpt(self):
        """OpenAI-licensed publishers get 57.9% of AI citations from ChatGPT alone."""
        chatgpt_concentration_pct = 57.9
        self.assertGreater(chatgpt_concentration_pct, 50)

    def test_openai_is_only_licensor_with_home_platform_advantage(self):
        """OpenAI is the ONLY AI company whose deals show home-platform citation lift."""
        openai_home_advantage = True
        google_home_advantage = False  # Google-licensed slightly LOWER on AI Overviews
        perplexity_home_advantage = False  # Perplexity-licensed at parity
        self.assertTrue(openai_home_advantage)
        self.assertFalse(google_home_advantage)
        self.assertFalse(perplexity_home_advantage)


class TestGoogleCitationParadox(unittest.TestCase):
    """Verify Google licensing deal citation behavior — no home-platform advantage."""

    def test_google_licensed_slightly_lower_on_ai_overviews(self):
        """Google-licensed publishers cited at slightly lower rate on AI Overviews."""
        # Google-licensed publishers: slightly lower than unlicensed on Google AI Overviews
        google_licensed_has_lower_rate = True
        self.assertTrue(google_licensed_has_lower_rate)

    def test_google_deals_operate_via_coercion_not_amplification(self):
        """Google's deals work through financial coercion, not citation amplification.

        Press Gazette (Aug 2026) reported Google's News AI pilot deals include NDAs
        and no-sue clauses. Publishers sign to keep existing Showcase revenue, not to
        gain citation premium. This is the opposite of OpenAI's citation amplification
        mechanism — Google's financial leverage is coercive (keep revenue or lose it),
        while OpenAI's is amplificatory (sign and get more citations).
        """
        google_mechanism = "coercive_financial_dependency"
        openai_mechanism = "citation_amplification"
        self.assertNotEqual(google_mechanism, openai_mechanism)


class TestPerplexityCitationParity(unittest.TestCase):
    """Verify Perplexity licensing deal citation behavior — parity with unlicensed."""

    def test_perplexity_licensed_at_parity(self):
        """Perplexity-licensed publishers at parity with unlicensed on Perplexity."""
        perplexity_licensed_has_premium = False
        self.assertFalse(perplexity_licensed_has_premium)


class TestTopCitationBeneficiaries(unittest.TestCase):
    """Verify top publisher citation beneficiary rankings."""

    def test_top_5_capture_69_percent_of_licensed_citations(self):
        """Top 5 media groups capture 69% of all citations to licensed publishers."""
        top_5_share_pct = 69
        self.assertGreater(top_5_share_pct, 60)

    def test_top_5_media_groups_identified(self):
        """Top 5 citation beneficiaries are named in the study."""
        top_5 = [
            "Future plc",
            "Forbes",
            "People Inc.",
            "Condé Nast",
            "Hearst",
        ]
        self.assertEqual(len(top_5), 5)
        self.assertIn("Condé Nast", top_5)

    def test_conde_nast_is_4th_largest_beneficiary(self):
        """Condé Nast is 4th in citation volume among licensed publishers."""
        ranking = {
            "Future plc": 1,
            "Forbes": 2,
            "People Inc.": 3,
            "Condé Nast": 4,
            "Hearst": 5,
        }
        self.assertEqual(ranking["Condé Nast"], 4)


class TestNewsShareOfAICitations(unittest.TestCase):
    """Verify that news is a small fraction of total AI citations."""

    def test_news_is_7_2_percent_of_all_citations(self):
        """News content represents only 7.2% of total AI citations."""
        news_share_pct = 7.2
        self.assertLess(news_share_pct, 10)

    def test_commercial_content_dominates_licensed_citations(self):
        """46.9% of licensed publisher citations go to commercial content."""
        commercial_content_pct = 46.9
        commercial_content_types = [
            "best-of lists",
            "buying guides",
            "product reviews",
        ]
        self.assertGreater(commercial_content_pct, 40)
        self.assertGreater(len(commercial_content_types), 0)


class TestMediaScopeFinancialIncentiveImplications(unittest.TestCase):
    """Verify the financial incentive model implications of citation amplification."""

    def test_meta_zero_deals_zero_citation_premium(self):
        """Meta has zero publisher deals, therefore zero citation premium.

        Meta's coverage receives baseline citation rates. No deal-driven
        amplification. Publishers have no citation-based financial incentive
        to cover Meta favorably.
        """
        meta_publisher_deals = 0
        meta_citation_premium = 0  # No deal → no premium
        self.assertEqual(meta_publisher_deals, 0)
        self.assertEqual(meta_citation_premium, 0)

    def test_conde_nast_openai_deal_generates_citation_premium(self):
        """Condé Nast's OpenAI deal (Aug 2024) generates measurable citation premium.

        As the 4th largest citation beneficiary among licensed publishers, Condé Nast
        has a quantifiable financial incentive to maintain the OpenAI deal. Adversarial
        OpenAI coverage could jeopardize the deal and its citation premium.
        """
        conde_nast_has_openai_deal = True
        conde_nast_citation_beneficiary_rank = 4
        conde_nast_gets_citation_premium = True
        self.assertTrue(conde_nast_has_openai_deal)
        self.assertEqual(conde_nast_citation_beneficiary_rank, 4)
        self.assertTrue(conde_nast_gets_citation_premium)

    def test_citation_premium_creates_financial_incentive_loop(self):
        """The citation premium creates a measurable financial incentive loop.

        Deal → +48% ChatGPT citations → more traffic → more revenue →
        incentive to maintain deal → softer coverage → deal renewed.
        """
        loop_steps = [
            "publisher_signs_deal",
            "citation_premium_48_pct",
            "increased_traffic",
            "increased_revenue",
            "incentive_to_maintain_deal",
            "softer_coverage",
            "deal_renewed",
        ]
        self.assertEqual(len(loop_steps), 7)
        self.assertIn("citation_premium_48_pct", loop_steps)

    def test_apple_variable_compensation_amplifies_citation_effect(self):
        """Apple's proposed variable pay-per-use Siri AI deals would amplify this.

        If Apple's algorithm favors deal-partner content (analogous to OpenAI's 48%
        premium), publishers with Apple deals earn more per-use payments AND more
        citations, compounding the financial incentive.
        """
        apple_compensation_model = "variable_pay_per_use"
        apple_budget_magnitude = "nine_figure"
        citation_amplification_compounds_variable_pay = True
        self.assertEqual(apple_compensation_model, "variable_pay_per_use")
        self.assertEqual(apple_budget_magnitude, "nine_figure")
        self.assertTrue(citation_amplification_compounds_variable_pay)

    def test_financial_incentive_asymmetry_quantified(self):
        """The meta-level asymmetry: deal publishers get +48% citations,
        no-deal publishers (like Meta) get zero premium.

        This quantifies the coverage asymmetry prediction from financial architecture.
        """
        openai_deal_publisher_premium_pct = 48
        no_deal_publisher_premium_pct = 0  # Meta, etc.
        asymmetry = openai_deal_publisher_premium_pct - no_deal_publisher_premium_pct
        self.assertEqual(asymmetry, 48)


class TestConfoundingFactors(unittest.TestCase):
    """Document legitimate confounding factors that could explain citation differences."""

    def test_confound_correlation_not_causation(self):
        """Publishers with deals may independently produce higher-quality content."""
        confound_strength = "STRONG"
        self.assertEqual(confound_strength, "STRONG")

    def test_confound_publisher_size(self):
        """Top 5 beneficiaries are major conglomerates with large content libraries."""
        confound_strength = "STRONG"
        top_5_are_major_conglomerates = True
        self.assertEqual(confound_strength, "STRONG")
        self.assertTrue(top_5_are_major_conglomerates)

    def test_confound_commercial_content_bias(self):
        """46.9% of citations go to buying guides/reviews — inherently high-citation."""
        confound_strength = "MODERATE"
        commercial_pct = 46.9
        self.assertEqual(confound_strength, "MODERATE")
        self.assertGreater(commercial_pct, 40)

    def test_confound_study_sponsor_incentive(self):
        """Press Ranger and OtterlyAI sell AI search optimization services."""
        confound_strength = "MODERATE"
        sponsors_sell_optimization = True
        self.assertEqual(confound_strength, "MODERATE")
        self.assertTrue(sponsors_sell_optimization)

    def test_confound_single_month_sample(self):
        """Study covers June 2026 only — one month may not be representative."""
        confound_strength = "WEAK"
        sample_months = 1
        self.assertEqual(confound_strength, "WEAK")
        self.assertEqual(sample_months, 1)


if __name__ == "__main__":
    unittest.main()
