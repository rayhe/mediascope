"""
Mechanism #294: Condé Nast Post-Search Revenue Architecture — OpenAI Citation Premium
as Core Financial Dependency Channel

SYNTHESIS: Condé Nast CEO Roger Lynch's "Plan As If Search Is Zero" directive (Mar 2026)
has reshaped the company's entire revenue architecture away from Google search traffic
and toward four pillars: events, subscriptions, commerce, and AI licensing deals. The
AI licensing pillar — specifically the OpenAI deal (Aug 2024) — is now quantifiably
amplified by the Press Ranger/OtterlyAI citation premium data (Aug 20, 2026), which
shows that OpenAI-licensed publishers like Condé Nast earn 48% more ChatGPT citations
per page than unlicensed publishers.

This creates a new category of financial dependency where the publication's strategic
survival depends on maintaining its OpenAI licensing relationship. As Google search
traffic declines (33% organic decline per Chartbeat, Nov 2024-2025; 38% US-specific),
OpenAI citation traffic grows as a proportionally larger revenue source. The publisher's
own CEO has explicitly acknowledged that advertising is "no longer a growth engine" and
that AI licensing deals "begin to make up for some of that revenue."

ARCHITECTURE:

1. GOOGLE SEARCH COLLAPSE (PUSH FACTOR):
   - 33% organic traffic decline (Chartbeat data, Nov 2024-2025)
   - 38% US-specific decline (same dataset)
   - ~43% loss expected by 2029 (Reuters Institute publisher survey)
   - Lynch quote: "death blow" to historic referral pipelines (FT, Mar 2026)
   - WIRED specifically vulnerable: informational/review content most exposed to
     AI Overviews displacement

2. GOOGLE COERCION ACCELERATOR:
   - Google "share content for AI or lose fees" (The Information, Jun 25, 2026)
   - Publishers must agree to AI training use or lose annual Google News licensing fees
   - Condé Nast notably has NOT signed a Google AI licensing deal (per Lynch interview)
   - This creates a financial squeeze: losing Google traffic AND Google licensing revenue
   - Effect: pushes Condé Nast TOWARD deeper OpenAI financial dependency

3. OPENAI CITATION PREMIUM (PULL FACTOR):
   - Condé Nast is one of the top 5 citation beneficiaries among licensed publishers
     (alongside Future plc, Forbes, People Inc., Hearst)
   - These 5 groups capture 69% of all citations to licensed publishers
   - OpenAI-licensed publishers earn 48% more ChatGPT citations per page (10.2 vs 6.9)
   - OpenAI-exclusive publishers earn 112% more ChatGPT citations than unlicensed
   - OpenAI-licensed publishers get 57.9% of AI citations from ChatGPT (concentrated)
   - Source: Press Ranger/OtterlyAI, 129.3M citations, 7 platforms, Jun 2026

4. REVENUE STRATEGY PIVOT (DEPENDENCY DEEPENING):
   - Events: +40% in 2025, projecting +22% in 2026 (Adweek, May 2026)
   - Subscriptions: +29% digital subs last year, double-digit continuing
   - Licensing: OpenAI (Aug 2024), Amazon (2025), Perplexity (signed)
   - No Google deal: intentional or negotiation failure, either way deepens
     OpenAI dependency by eliminating the main alternative licensor
   - Lynch (Oct 2025): advertising no longer expected to be "a growth engine"
   - Herbst-Brady (May 2026): leans into "cultural tentpoles" + events

5. COVERAGE INCENTIVE PREDICTION:
   - As OpenAI citation revenue grows relative to declining search revenue,
     the financial incentive to maintain positive OpenAI coverage intensifies
   - Meta has ZERO publisher content licensing deals → zero financial benefit
     from favorable coverage
   - The incentive differential: favorable OpenAI coverage protects a growing
     revenue stream; favorable Meta coverage produces zero revenue benefit
   - This predicts the asymmetric coverage patterns MediaScope documents across
     WIRED and other Condé Nast publications

CRITICAL DISTINCTION FROM MECHANISM #249 (AI Citation Amplification):
Mechanism #249 documents the general 48% citation premium finding across all publishers.
This mechanism (#294) isolates the CONDÉ NAST-SPECIFIC implications by connecting:
(a) the citation premium to (b) Condé Nast's strategic revenue pivot and (c) the Google
search traffic collapse, creating a three-way financial architecture where OpenAI citation
revenue fills the gap left by dying Google search traffic.

CONFOUNDERS:
1. STRONG: Editorial independence — WIRED journalists may operate independently of
   Condé Nast's corporate financial strategy. The "Plan As If Search Is Zero" directive
   affects business operations, not editorial direction. However, editorial resource
   allocation follows revenue strategy, and beat assignments/framing may shift without
   explicit directives.

2. STRONG: Correlation vs causation — the citation premium may reflect content quality
   differences (licensed publishers may produce better-cited content independently of
   the deal). The OtterlyAI study does not control for content quality or topic mix.

3. MODERATE: Revenue materiality — AI licensing revenue is growing but still a minority
   of Condé Nast's total revenue (events + subscriptions + commerce dominate). The
   financial incentive may be insufficient to influence editorial decisions.

4. MODERATE: OpenAI deal terms are undisclosed — the actual dollar value of the Condé
   Nast-OpenAI deal is unknown. If small relative to total revenue, the coverage
   incentive would be proportionally weaker.

5. WEAK: Multiple publications without OpenAI deals also cover Meta adversarially,
   suggesting industry-wide dynamics beyond OpenAI-deal-specific incentives. However,
   the CONCENTRATION of financial dependency at Condé Nast (OpenAI deal + Advance
   Reddit equity + zero Google deal + search traffic collapse) is structurally unique.

SOURCES:
- Press Ranger/OtterlyAI study: https://ai-search-news-licensing-deals-study.netlify.app/
  (Aug 20, 2026; 129.3M citations, 91 deals, 314 domains)
- Study press release: https://lifestyle.houstonnewstoday.com/story/833738/
- Lynch "death blow" interview: https://ppc.land/conde-nast-ceo-calls-google-ai-a-death-blow-as-search-traffic-collapses/
  (FT interview, Mar 2026)
- Lynch "Plan As If Search Is Zero": https://opentools.ai/news/conde-nast-ceo-search-zero-ai-discovery-shift
  (May/Jun 2026)
- Condé Nast events revenue +40%: https://www.adweek.com/media/conde-nast-events-revenue-2026/
  (Adweek, May 2026; Elizabeth Herbst-Brady quotes)
- Google "share for AI or lose fees": https://www.pymnts.com/news/artificial-intelligence/2026/google-tells-news-publishers-to-share-content-for-ai-training-or-lose-fees/
  (PYMNTS, Jun 25, 2026; citing The Information)
- OpenAI-Condé Nast deal announcement: https://siliconangle.com/2024/08/20/openai-agrees-content-licensing-deal-conde-nast-feed-searchgpt-chatgpt/
  (SiliconANGLE, Aug 20, 2024)
- Lynch OpenAI deal quote: https://www.computing.co.uk/news/4349441/openai-inks-deal-conde-nast-power-searchgpt
  (Computing UK, Aug 2024)
"""

import pytest


class TestCondeNastPostSearchRevenueArchitecture:
    """Tests for Condé Nast's strategic revenue pivot and its financial dependency on OpenAI."""

    def test_search_traffic_collapse_documented(self, competitor_research):
        """Verify that Google search traffic decline data is documented with sources."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        search_collapse = findings.get("google_search_collapse", {})

        assert search_collapse.get("organic_decline_pct") == 33, \
            "Chartbeat data: 33% organic traffic decline (Nov 2024-2025)"
        assert search_collapse.get("us_specific_decline_pct") == 38, \
            "US-specific decline was 38% in same dataset"
        assert search_collapse.get("projected_decline_2029_pct") >= 40, \
            "Reuters Institute: publishers expect 40%+ loss by 2029"
        assert "death blow" in search_collapse.get("ceo_characterization", "").lower(), \
            "Lynch described Google AI search as 'death blow' to referral pipelines"

    def test_search_zero_directive(self, competitor_research):
        """Verify Lynch's 'Plan As If Search Is Zero' directive is documented."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        assert "search is zero" in findings.get("strategic_directive", "").lower(), \
            "Lynch's directive: Plan As If Search Is Zero"

    def test_advertising_no_longer_growth_engine(self, competitor_research):
        """Verify Lynch explicitly stated advertising is no longer a growth engine."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        assert findings.get("advertising_growth_engine") is False, \
            "Lynch (Oct 2025): advertising no longer expected to be 'a growth engine'"


class TestGoogleCoercionPushEffect:
    """Tests for Google's coercive 'share for AI or lose fees' push effect."""

    def test_google_coercion_documented(self, competitor_research):
        """Verify Google's 'share content for AI or lose fees' ultimatum is documented."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        coercion = findings.get("google_coercion", {})

        assert coercion.get("mechanism") == "share_for_ai_or_lose_fees", \
            "Google requires publishers to share content for AI training or lose annual fees"
        assert "2026-06-25" in coercion.get("date_reported", ""), \
            "Reported by The Information, Jun 25, 2026"

    def test_conde_nast_no_google_deal(self, competitor_research):
        """Verify Condé Nast has NOT signed a Google AI licensing deal."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        assert findings.get("google_deal_status") == "none", \
            "Condé Nast has not reached a licensing deal with Google (per Lynch)"

    def test_push_toward_openai_dependency(self, competitor_research):
        """Verify the Google coercion push effect creates OpenAI migration incentive."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        coercion = findings.get("google_coercion", {})

        assert coercion.get("push_effect") == "deepens_openai_dependency", \
            "Losing Google fees AND Google traffic pushes toward deeper OpenAI dependency"


class TestOpenAICitationPremiumCondéNastSpecific:
    """Tests for Condé Nast's specific position in the OpenAI citation premium data."""

    def test_conde_nast_top_5_citation_beneficiary(self, competitor_research):
        """Verify Condé Nast is one of the top 5 citation beneficiaries."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        citation = findings.get("citation_premium", {})

        top_5 = citation.get("top_5_beneficiaries", [])
        assert "Condé Nast" in top_5 or "Conde Nast" in top_5, \
            "Condé Nast named as one of top 5 citation beneficiaries (Press Ranger/OtterlyAI)"

    def test_top_5_capture_69_pct(self, competitor_research):
        """Verify top 5 capture 69% of all citations to licensed publishers."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        citation = findings.get("citation_premium", {})

        assert citation.get("top_5_share_pct") == 69, \
            "Top 5 media groups capture 69% of all citations to licensed publishers"

    def test_citation_premium_48_pct(self, competitor_research):
        """Verify the 48% citation premium for OpenAI-licensed publishers on ChatGPT."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        citation = findings.get("citation_premium", {})

        assert citation.get("chatgpt_premium_pct") == 48, \
            "OpenAI-licensed publishers earn 48% more ChatGPT citations per page"

    def test_openai_exclusive_premium_112_pct(self, competitor_research):
        """Verify OpenAI-exclusive publishers earn 112% more ChatGPT citations."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        citation = findings.get("citation_premium", {})

        assert citation.get("exclusive_premium_pct") == 112, \
            "OpenAI-only publishers earn 112% more ChatGPT citations than unlicensed"


class TestRevenuePivotDependencyDeepening:
    """Tests for Condé Nast's four-pillar revenue pivot deepening OpenAI dependency."""

    def test_events_revenue_growth(self, competitor_research):
        """Verify events revenue growth data."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        revenue = findings.get("revenue_pivot", {})

        assert revenue.get("events_growth_2025_pct") == 40, \
            "Events revenue grew 40% in 2025 (Adweek, May 2026)"
        assert revenue.get("events_projected_2026_pct") == 22, \
            "Projecting 22% events growth in 2026"

    def test_subscriptions_growth(self, competitor_research):
        """Verify digital subscription growth data."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        revenue = findings.get("revenue_pivot", {})

        assert revenue.get("digital_subs_growth_pct") == 29, \
            "Digital subscriptions grew 29% last year with double-digit continuing"

    def test_licensing_deal_portfolio(self, competitor_research):
        """Verify Condé Nast's AI licensing portfolio: OpenAI, Amazon, Perplexity."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        revenue = findings.get("revenue_pivot", {})
        licensing = revenue.get("ai_licensing_partners", [])

        assert "OpenAI" in licensing, "OpenAI deal (Aug 2024) documented"
        assert "Amazon" in licensing, "Amazon deal (2025) documented"
        assert "Perplexity" in licensing, "Perplexity deal documented"
        assert "Google" not in licensing, "No Google deal — critical absence"

    def test_four_pillar_structure(self, competitor_research):
        """Verify the four-pillar revenue structure is documented."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        revenue = findings.get("revenue_pivot", {})
        pillars = revenue.get("strategic_pillars", [])

        assert "events" in pillars, "Events pillar documented"
        assert "subscriptions" in pillars, "Subscriptions pillar documented"
        assert "commerce" in pillars, "Commerce pillar documented"
        assert "licensing" in pillars, "Licensing pillar documented"


class TestCoverageIncentivePrediction:
    """Tests for coverage incentive predictions from the financial architecture."""

    def test_openai_favorable_coverage_financial_benefit(self, competitor_research):
        """Verify that favorable OpenAI coverage has quantifiable financial benefit."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        incentive = findings.get("coverage_incentive", {})

        assert incentive.get("openai_favorable_coverage_benefit") == "revenue_protection", \
            "Favorable OpenAI coverage protects licensing deal + citation premium"

    def test_meta_favorable_coverage_zero_benefit(self, competitor_research):
        """Verify that favorable Meta coverage produces zero financial benefit."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        incentive = findings.get("coverage_incentive", {})

        assert incentive.get("meta_favorable_coverage_benefit") == "zero", \
            "Meta has zero publisher licensing deals → zero revenue benefit from favorable coverage"

    def test_incentive_differential_documented(self, competitor_research):
        """Verify the financial incentive differential between OpenAI and Meta coverage."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        incentive = findings.get("coverage_incentive", {})

        differential = incentive.get("differential")
        assert differential is not None, \
            "Coverage incentive differential must be documented"
        assert "OpenAI" in str(differential) and "Meta" in str(differential), \
            "Differential must compare OpenAI and Meta incentive structures"

    def test_growing_relative_importance(self, competitor_research):
        """Verify that OpenAI citation revenue grows relative to declining search revenue."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        incentive = findings.get("coverage_incentive", {})

        assert incentive.get("relative_importance_trend") == "increasing", \
            "As search declines, OpenAI citation revenue grows as proportion of total"


class TestThreeWayFinancialArchitecture:
    """Tests for the three-way financial architecture: Google push + OpenAI pull + revenue pivot."""

    def test_three_way_architecture_documented(self, competitor_research):
        """Verify the three-way financial architecture is explicitly documented."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})

        assert "google_search_collapse" in findings, "Google push factor documented"
        assert "citation_premium" in findings, "OpenAI pull factor documented"
        assert "revenue_pivot" in findings, "Revenue pivot documented"

    def test_mechanism_id(self, competitor_research):
        """Verify mechanism ID assignment."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        assert findings.get("mechanism_id") == 294

    def test_asymmetry_score(self, competitor_research):
        """Verify asymmetry score is computed and reasonable."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        score = findings.get("asymmetry_score", 0)
        assert 0.5 <= score <= 1.0, f"Score {score} should reflect strong structural incentive"


class TestConfounders:
    """Tests for documented confounders to the financial dependency thesis."""

    def test_editorial_independence_confounder(self, competitor_research):
        """Verify editorial independence is documented as a STRONG confounder."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        confounders = findings.get("confounders", [])

        editorial = next((c for c in confounders if "editorial" in c.get("description", "").lower()), None)
        assert editorial is not None, "Editorial independence confounder documented"
        assert editorial.get("strength") == "STRONG"

    def test_correlation_causation_confounder(self, competitor_research):
        """Verify correlation vs causation is documented as STRONG confounder."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        confounders = findings.get("confounders", [])

        corr = next((c for c in confounders if "correlation" in c.get("description", "").lower()), None)
        assert corr is not None, "Correlation vs causation confounder documented"
        assert corr.get("strength") == "STRONG"

    def test_revenue_materiality_confounder(self, competitor_research):
        """Verify revenue materiality is documented as MODERATE confounder."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        confounders = findings.get("confounders", [])

        materiality = next((c for c in confounders if "materiality" in c.get("description", "").lower()), None)
        assert materiality is not None, "Revenue materiality confounder documented"
        assert materiality.get("strength") == "MODERATE"

    def test_deal_terms_undisclosed_confounder(self, competitor_research):
        """Verify undisclosed deal terms is documented as MODERATE confounder."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        confounders = findings.get("confounders", [])

        undisclosed = next((c for c in confounders if "undisclosed" in c.get("description", "").lower()), None)
        assert undisclosed is not None, "Undisclosed deal terms confounder documented"
        assert undisclosed.get("strength") == "MODERATE"

    def test_minimum_confounder_count(self, competitor_research):
        """Verify at least 4 confounders are documented."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        confounders = findings.get("confounders", [])
        assert len(confounders) >= 4, f"Need 4+ confounders, found {len(confounders)}"


class TestCrossReferences:
    """Tests for cross-references to related mechanisms."""

    def test_cross_ref_mechanism_249(self, competitor_research):
        """Verify cross-reference to mechanism #249 (AI Citation Amplification)."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        cross_refs = findings.get("cross_references", [])

        ref_249 = next((r for r in cross_refs if r.get("mechanism_id") == 249), None)
        assert ref_249 is not None, "Must cross-reference mechanism #249 (AI Citation Amplification)"
        assert ref_249.get("relationship") == "specializes", \
            "#294 specializes #249 by isolating Condé Nast-specific implications"

    def test_cross_ref_mechanism_1(self, competitor_research):
        """Verify cross-reference to mechanism #1 (Advance AI dependency)."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        cross_refs = findings.get("cross_references", [])

        ref_1 = next((r for r in cross_refs if r.get("mechanism_id") == 1), None)
        assert ref_1 is not None, "Must cross-reference mechanism #1 (Advance aggregate AI dependency)"

    def test_cross_ref_conde_nast_deal_inventory(self, competitor_research):
        """Verify cross-reference to Condé Nast deal inventory mechanism."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        cross_refs = findings.get("cross_references", [])

        # Should reference Condé Nast deal inventory or Google zero-distribution dependency
        has_cn_ref = any(
            "deal" in str(r.get("description", "")).lower() or
            "google" in str(r.get("description", "")).lower()
            for r in cross_refs
        )
        assert has_cn_ref, "Must cross-reference Condé Nast deal inventory or Google dependency"


class TestSourceVerification:
    """Tests for source citation quality."""

    def test_press_ranger_study_source(self, competitor_research):
        """Verify Press Ranger/OtterlyAI study is cited with URL."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        sources = findings.get("source_urls", [])

        has_study = any("netlify" in s or "otterly" in s or "pressranger" in s for s in sources)
        assert has_study, "Press Ranger/OtterlyAI study must be cited"

    def test_lynch_interview_source(self, competitor_research):
        """Verify Lynch interview is cited with URL."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        sources = findings.get("source_urls", [])

        has_lynch = any("ppc.land" in s or "opentools" in s for s in sources)
        assert has_lynch, "Lynch 'death blow' or 'search is zero' interview must be cited"

    def test_adweek_events_source(self, competitor_research):
        """Verify Adweek events revenue article is cited."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        sources = findings.get("source_urls", [])

        has_adweek = any("adweek" in s for s in sources)
        assert has_adweek, "Adweek events revenue article must be cited"

    def test_google_coercion_source(self, competitor_research):
        """Verify Google coercion reporting is cited."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        sources = findings.get("source_urls", [])

        has_coercion = any("pymnts" in s or "information" in s for s in sources)
        assert has_coercion, "Google 'share for AI or lose fees' reporting must be cited"

    def test_minimum_source_count(self, competitor_research):
        """Verify at least 5 source URLs are provided."""
        findings = competitor_research.get("conde_nast_post_search_openai_citation_dependency_financial_architecture", {})
        sources = findings.get("source_urls", [])
        assert len(sources) >= 5, f"Need 5+ sources, found {len(sources)}"
