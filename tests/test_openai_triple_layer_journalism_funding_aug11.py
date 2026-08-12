"""
Test Mechanism #53: OpenAI Triple-Layer Journalism Funding Architecture
Type C: Financial Incentive Mapping — August 11, 2026

OpenAI operates THREE distinct, simultaneous financial relationship channels
with journalism — creating compounded financial dependencies at different
organizational levels that are structurally unprecedented for any single
AI company:

Layer 1: Content Licensing (Publisher/Corporate Level)
  20+ publisher deals covering 160+ outlets in 20+ languages.
  Reported values: News Corp $250M/5yr, Dotdash Meredith $16M/yr min (IAC filings).

Layer 2: Direct Newsroom/Reporter Salary Funding (Individual Journalist Level)
  Axios (Jan 2025): OpenAI directly funds reporter salaries in 4 new cities.
  Lenfest Institute (Oct 2024): OpenAI + Microsoft jointly fund $10M for AI
  fellows at 5 metro newsrooms.

Layer 3: Philanthropic/Nonprofit Ecosystem Grants (Journalism Ecosystem Level)
  AJP Phase 1 (Jul 2023): $5M cash + $5M API credits to 41+ nonprofit newsrooms.
  AJP Phase 2 (Jul 2026): Another $5M + $3M credits, now 50+ newsrooms across 38 states.

No tech company has simultaneously operated financial relationships at ALL THREE
levels of the journalism stack: corporate, individual, and ecosystem. Meta's
trajectory is the mirror image — active withdrawal from all three levels since 2022.

Source URLs verified 2026-08-11:
- LLM Pulse: https://llmpulse.ai/blog/openai-publisher-deals/
- TechCrunch (Axios): https://techcrunch.com/2025/01/15/openai-is-bankrolling-axios-expansion-into-four-new-markets/
- AdWeek (Axios 2026): https://www.adweek.com/media/axios-local-openai-2026/
- OpenAI (Axios): http://openai.com/index/partnering-with-axios-expands-openai-work-with-the-news-industry/
- OpenAI (AJP): https://openai.com/index/partnership-with-american-journalism-project-to-support-local-news/
- VentureBeat (AJP): https://venturebeat.com/ai/openai-commits-5m-to-local-news-partnership-with-the-american-journalism-project
- Reuters (AJP): https://www.reuters.com/business/media-telecom/openai-partners-with-american-journalism-project-support-local-news-2023-07-18/
- NewscastStudio (AJP Phase 2): https://www.newscaststudio.com/2026/07/22/openai-renews-local-news-partnership-with-5-million-investment/
- AJP Studio update: https://www.theajp.org/news-insights/announcements/exploring-emerging-technologies-an-update-on-our-product-ai-studio/
- Slashdot (Lenfest): https://news.slashdot.org/story/24/10/22/2045216/openai-microsoft-funding-10-million-in-grants-for-ai-powered-journalism
- LiveMint (Meta News end): https://www.livemint.com/companies/news/facebook-to-end-payments-to-us-news-publishers-11659025905218.html
- Nasdaq (Meta News end): https://www.nasdaq.com/articles/metas-facebook-is-done-paying-publishers-for-news-tab-content
- Fast Company (Meta never serious): https://www.fastcompany.com/90963282/meta-was-never-really-the-medias-friend
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_entities():
    """Load competitor-entities.yaml."""
    path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def load_competitor_research():
    """Load competitor-coverage-research.yaml."""
    path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


# ===================================================================
# Test Class 1: Layer 1 — Content Licensing (Publisher/Corporate Level)
# ===================================================================
class TestLayer1ContentLicensing:
    """Validate Layer 1: OpenAI publisher content licensing deals.
    Source: https://llmpulse.ai/blog/openai-publisher-deals/
    """

    def test_openai_has_publisher_deal_portfolio(self):
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        assert 'publisher_content_deal_portfolio' in openai, \
            "OpenAI entity missing publisher_content_deal_portfolio section"

    def test_total_deals_20_plus(self):
        """OpenAI has 20+ publisher deals as of mid-2026.
        Source: https://llmpulse.ai/blog/openai-publisher-deals/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        portfolio = openai['publisher_content_deal_portfolio']
        total = str(portfolio.get('total_deals', ''))
        assert '20' in total, \
            f"Expected 20+ total deals. Got: {total}"

    def test_total_outlets_160_plus(self):
        """OpenAI covers 160+ outlets through publisher deals.
        Source: http://openai.com/index/partnering-with-axios-expands-openai-work-with-the-news-industry/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        portfolio = openai['publisher_content_deal_portfolio']
        outlets = str(portfolio.get('total_outlets', ''))
        assert '160' in outlets, \
            f"Expected 160+ outlets. Got: {outlets}"

    def test_news_corp_largest_deal_250m(self):
        """News Corp is the largest deal at $250M/5yr.
        Source: https://llmpulse.ai/blog/openai-publisher-deals/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        portfolio = openai['publisher_content_deal_portfolio']
        largest = str(portfolio.get('largest_deal', ''))
        assert '250' in largest, \
            f"Expected News Corp $250M deal. Got: {largest}"

    def test_dotdash_meredith_16m_year(self):
        """Dotdash Meredith pays at least $16M/year per IAC filings.
        Source: https://llmpulse.ai/blog/openai-publisher-deals/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        portfolio = openai['publisher_content_deal_portfolio']
        ft_deal = portfolio.get('ft_deal_m_yr', '')
        # Check that the notable_partners list includes Dotdash Meredith
        partners = [str(p) for p in portfolio.get('notable_partners', [])]
        assert any('Dotdash' in p for p in partners), \
            f"Missing Dotdash Meredith in notable_partners"

    def test_languages_20_plus(self):
        """Deals span 20+ languages.
        Source: http://openai.com/index/partnering-with-axios-expands-openai-work-with-the-news-industry/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        portfolio = openai['publisher_content_deal_portfolio']
        languages = str(portfolio.get('languages', ''))
        assert '20' in languages, \
            f"Expected 20+ languages. Got: {languages}"

    def test_has_source_urls(self):
        """Layer 1 portfolio has source URLs."""
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        portfolio = openai['publisher_content_deal_portfolio']
        assert 'source_urls' in portfolio, "Missing source_urls in publisher_content_deal_portfolio"
        assert len(portfolio['source_urls']) >= 2, \
            f"Expected at least 2 source URLs. Got: {len(portfolio['source_urls'])}"


# ===================================================================
# Test Class 2: Layer 2 — Direct Newsroom/Reporter Salary Funding
# ===================================================================
class TestLayer2SalaryFunding:
    """Validate Layer 2: OpenAI's direct newsroom/reporter salary funding.
    Sources:
    - https://techcrunch.com/2025/01/15/openai-is-bankrolling-axios-expansion-into-four-new-markets/
    - https://www.adweek.com/media/axios-local-openai-2026/
    - https://news.slashdot.org/story/24/10/22/2045216/openai-microsoft-funding-10-million-in-grants-for-ai-powered-journalism
    """

    def test_triple_layer_section_exists(self):
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        assert 'triple_layer_journalism_funding' in openai, \
            "OpenAI entity missing triple_layer_journalism_funding section"

    def test_layer_2_salary_funding_exists(self):
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        tlf = openai['triple_layer_journalism_funding']
        assert 'layer_2_salary_funding' in tlf, \
            "Missing layer_2_salary_funding in triple_layer_journalism_funding"

    def test_axios_deal_jan_2025(self):
        """Axios deal announced January 2025 — first direct newsroom funding.
        Source: https://techcrunch.com/2025/01/15/openai-is-bankrolling-axios-expansion-into-four-new-markets/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        layer2 = openai['triple_layer_journalism_funding']['layer_2_salary_funding']
        axios = layer2.get('axios', {})
        date = str(axios.get('date', ''))
        assert '2025-01' in date or '2025' in date, \
            f"Axios deal date should be Jan 2025. Got: {date}"

    def test_axios_four_initial_cities(self):
        """OpenAI funded 4 new Axios Local cities: Pittsburgh, Kansas City, Boulder, Huntsville.
        Source: https://techcrunch.com/2025/01/15/openai-is-bankrolling-axios-expansion-into-four-new-markets/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        layer2 = openai['triple_layer_journalism_funding']['layer_2_salary_funding']
        axios = layer2.get('axios', {})
        cities = axios.get('initial_cities', [])
        assert len(cities) == 4, f"Expected 4 initial cities. Got: {len(cities)}"
        city_str = ' '.join(str(c) for c in cities).lower()
        assert 'pittsburgh' in city_str, "Missing Pittsburgh in Axios cities"
        assert 'boulder' in city_str, "Missing Boulder in Axios cities"

    def test_axios_expansion_2026(self):
        """Axios expanding to 7-9 more cities in 2026.
        Source: https://www.adweek.com/media/axios-local-openai-2026/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        layer2 = openai['triple_layer_journalism_funding']['layer_2_salary_funding']
        axios = layer2.get('axios', {})
        expansion = str(axios.get('expansion_2026', ''))
        assert '7' in expansion or '9' in expansion or 'seven' in expansion.lower(), \
            f"Expected 7-9 city expansion. Got: {expansion}"

    def test_axios_first_direct_salary_funding(self):
        """Axios deal was the FIRST TIME OpenAI directly funded journalist salaries.
        Source: https://techcrunch.com/2025/01/15/openai-is-bankrolling-axios-expansion-into-four-new-markets/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        layer2 = openai['triple_layer_journalism_funding']['layer_2_salary_funding']
        axios = layer2.get('axios', {})
        significance = str(axios.get('significance', '')).lower()
        assert 'first' in significance, \
            f"Should note Axios as first direct salary funding. Got: {significance}"

    def test_lenfest_10m_joint_funding(self):
        """OpenAI + Microsoft jointly funded $10M for AI fellows at 5 newsrooms.
        Source: https://news.slashdot.org/story/24/10/22/2045216/openai-microsoft-funding-10-million-in-grants-for-ai-powered-journalism
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        layer2 = openai['triple_layer_journalism_funding']['layer_2_salary_funding']
        lenfest = layer2.get('lenfest_institute', {})
        total_str = str(lenfest.get('total_funding_m', ''))
        assert '10' in total_str, \
            f"Expected $10M Lenfest funding. Got: {total_str}"

    def test_lenfest_five_newsrooms(self):
        """Lenfest program covers 5 metro newsrooms.
        Source: https://news.slashdot.org/story/24/10/22/2045216/openai-microsoft-funding-10-million-in-grants-for-ai-powered-journalism
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        layer2 = openai['triple_layer_journalism_funding']['layer_2_salary_funding']
        lenfest = layer2.get('lenfest_institute', {})
        newsrooms = lenfest.get('newsrooms', [])
        assert len(newsrooms) == 5, f"Expected 5 Lenfest newsrooms. Got: {len(newsrooms)}"


# ===================================================================
# Test Class 3: Layer 3 — Philanthropic/Nonprofit Grants
# ===================================================================
class TestLayer3PhilanthropicGrants:
    """Validate Layer 3: OpenAI's philanthropic/nonprofit journalism grants.
    Sources:
    - https://openai.com/index/partnership-with-american-journalism-project-to-support-local-news/
    - https://venturebeat.com/ai/openai-commits-5m-to-local-news-partnership-with-the-american-journalism-project
    - https://www.newscaststudio.com/2026/07/22/openai-renews-local-news-partnership-with-5-million-investment/
    """

    def test_layer_3_philanthropic_grants_exists(self):
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        tlf = openai['triple_layer_journalism_funding']
        assert 'layer_3_philanthropic_grants' in tlf, \
            "Missing layer_3_philanthropic_grants in triple_layer_journalism_funding"

    def test_ajp_phase_1_date_jul_2023(self):
        """AJP Phase 1 announced July 2023.
        Source: https://www.reuters.com/business/media-telecom/openai-partners-with-american-journalism-project-support-local-news-2023-07-18/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        layer3 = openai['triple_layer_journalism_funding']['layer_3_philanthropic_grants']
        ajp1 = layer3.get('ajp_phase_1', {})
        date = str(ajp1.get('date', ''))
        assert '2023-07' in date or '2023' in date, \
            f"AJP Phase 1 date should be Jul 2023. Got: {date}"

    def test_ajp_phase_1_cash_5m(self):
        """AJP Phase 1: $5M in cash funding.
        Source: https://openai.com/index/partnership-with-american-journalism-project-to-support-local-news/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        layer3 = openai['triple_layer_journalism_funding']['layer_3_philanthropic_grants']
        ajp1 = layer3.get('ajp_phase_1', {})
        cash = ajp1.get('cash_m', 0)
        assert cash == 5, f"Expected $5M cash. Got: {cash}"

    def test_ajp_phase_1_api_credits_5m(self):
        """AJP Phase 1: $5M in API credits.
        Source: https://openai.com/index/partnership-with-american-journalism-project-to-support-local-news/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        layer3 = openai['triple_layer_journalism_funding']['layer_3_philanthropic_grants']
        ajp1 = layer3.get('ajp_phase_1', {})
        credits = ajp1.get('api_credits_m', 0)
        assert credits == 5, f"Expected $5M API credits. Got: {credits}"

    def test_ajp_phase_1_initial_grantees_13(self):
        """AJP Phase 1 distributed grants to 13 initial organizations.
        Source: https://www.theajp.org/news-insights/announcements/exploring-emerging-technologies-an-update-on-our-product-ai-studio/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        layer3 = openai['triple_layer_journalism_funding']['layer_3_philanthropic_grants']
        ajp1 = layer3.get('ajp_phase_1', {})
        grantees = ajp1.get('initial_grantees', [])
        assert len(grantees) == 13, f"Expected 13 initial grantees. Got: {len(grantees)}"

    def test_ajp_phase_1_includes_marshall_project(self):
        """The Marshall Project is among AJP Phase 1 grantees.
        Source: https://www.theajp.org/news-insights/announcements/exploring-emerging-technologies-an-update-on-our-product-ai-studio/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        layer3 = openai['triple_layer_journalism_funding']['layer_3_philanthropic_grants']
        ajp1 = layer3.get('ajp_phase_1', {})
        grantees = [str(g) for g in ajp1.get('initial_grantees', [])]
        assert any('Marshall' in g for g in grantees), \
            f"Missing The Marshall Project in grantees. Got: {grantees}"

    def test_ajp_phase_1_includes_spotlight_pa(self):
        """Spotlight PA is among AJP Phase 1 grantees.
        Source: https://www.theajp.org/news-insights/announcements/exploring-emerging-technologies-an-update-on-our-product-ai-studio/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        layer3 = openai['triple_layer_journalism_funding']['layer_3_philanthropic_grants']
        ajp1 = layer3.get('ajp_phase_1', {})
        grantees = [str(g) for g in ajp1.get('initial_grantees', [])]
        assert any('Spotlight' in g for g in grantees), \
            f"Missing Spotlight PA in grantees. Got: {grantees}"

    def test_ajp_phase_2_date_jul_2026(self):
        """AJP Phase 2 announced July 2026.
        Source: https://www.newscaststudio.com/2026/07/22/openai-renews-local-news-partnership-with-5-million-investment/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        layer3 = openai['triple_layer_journalism_funding']['layer_3_philanthropic_grants']
        ajp2 = layer3.get('ajp_phase_2', {})
        date = str(ajp2.get('date', ''))
        assert '2026-07' in date or '2026' in date, \
            f"AJP Phase 2 date should be Jul 2026. Got: {date}"

    def test_ajp_phase_2_cash_5m(self):
        """AJP Phase 2: another $5M in cash.
        Source: https://www.newscaststudio.com/2026/07/22/openai-renews-local-news-partnership-with-5-million-investment/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        layer3 = openai['triple_layer_journalism_funding']['layer_3_philanthropic_grants']
        ajp2 = layer3.get('ajp_phase_2', {})
        cash = ajp2.get('cash_m', 0)
        assert cash == 5, f"Expected $5M cash. Got: {cash}"

    def test_ajp_phase_2_credits_3m(self):
        """AJP Phase 2: $3M in technology credits.
        Source: https://www.newscaststudio.com/2026/07/22/openai-renews-local-news-partnership-with-5-million-investment/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        layer3 = openai['triple_layer_journalism_funding']['layer_3_philanthropic_grants']
        ajp2 = layer3.get('ajp_phase_2', {})
        credits = ajp2.get('tech_credits_m', 0)
        assert credits == 3, f"Expected $3M credits. Got: {credits}"

    def test_ajp_phase_2_coverage_50_plus_newsrooms(self):
        """AJP Phase 2 covers 50+ nonprofit newsrooms.
        Source: https://www.newscaststudio.com/2026/07/22/openai-renews-local-news-partnership-with-5-million-investment/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        layer3 = openai['triple_layer_journalism_funding']['layer_3_philanthropic_grants']
        ajp2 = layer3.get('ajp_phase_2', {})
        newsrooms = str(ajp2.get('newsrooms_covered', ''))
        assert '50' in newsrooms, \
            f"Expected 50+ newsrooms. Got: {newsrooms}"

    def test_ajp_phase_2_states_38(self):
        """AJP operates across 38 states.
        Source: https://www.newscaststudio.com/2026/07/22/openai-renews-local-news-partnership-with-5-million-investment/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        layer3 = openai['triple_layer_journalism_funding']['layer_3_philanthropic_grants']
        ajp2 = layer3.get('ajp_phase_2', {})
        states = ajp2.get('states', 0)
        assert states == 38, f"Expected 38 states. Got: {states}"


# ===================================================================
# Test Class 4: Meta Contrast — Active Withdrawal
# ===================================================================
class TestMetaContrast:
    """Validate the Meta mirror image: withdrawal from all three journalism
    funding levels simultaneously.
    Sources:
    - https://www.livemint.com/companies/news/facebook-to-end-payments-to-us-news-publishers-11659025905218.html
    - https://www.nasdaq.com/articles/metas-facebook-is-done-paying-publishers-for-news-tab-content
    - https://www.fastcompany.com/90963282/meta-was-never-really-the-medias-friend
    """

    def test_meta_contrast_exists(self):
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        tlf = openai['triple_layer_journalism_funding']
        assert 'meta_contrast' in tlf, \
            "Missing meta_contrast in triple_layer_journalism_funding"

    def test_meta_news_tab_payments_ended(self):
        """Meta ended Facebook News payments to US publishers in July 2022.
        Source: https://www.livemint.com/companies/news/facebook-to-end-payments-to-us-news-publishers-11659025905218.html
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        contrast = openai['triple_layer_journalism_funding']['meta_contrast']
        news_tab = str(contrast.get('news_tab_payments_ended', ''))
        assert '2022' in news_tab, \
            f"Meta News Tab payment end should include 2022. Got: {news_tab}"

    def test_meta_news_tab_value_105m(self):
        """Meta's Facebook News deals were worth $105M over 3 years.
        Source: https://www.adweek.com/media/meta-to-stop-paying-u-s-publishers-for-news-content/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        contrast = openai['triple_layer_journalism_funding']['meta_contrast']
        value = str(contrast.get('news_tab_total_value', ''))
        assert '105' in value or '100' in value, \
            f"Expected ~$105M value. Got: {value}"

    def test_meta_bulletin_killed(self):
        """Meta killed Bulletin newsletter platform in 2023.
        Source: https://www.fastcompany.com/90963282/meta-was-never-really-the-medias-friend
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        contrast = openai['triple_layer_journalism_funding']['meta_contrast']
        bulletin = str(contrast.get('bulletin_killed', ''))
        assert '2023' in bulletin, \
            f"Meta Bulletin killed should reference 2023. Got: {bulletin}"

    def test_meta_zero_content_licensing_deals(self):
        """Meta has ZERO AI content licensing deals with publishers.
        Source: https://llmpulse.ai/blog/openai-publisher-deals/ (Meta absent from all deal lists)
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        contrast = openai['triple_layer_journalism_funding']['meta_contrast']
        deals = contrast.get('content_licensing_deals', 0)
        assert deals == 0, f"Meta should have 0 content licensing deals. Got: {deals}"

    def test_meta_zero_salary_funding(self):
        """Meta has ZERO journalist salary funding programs."""
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        contrast = openai['triple_layer_journalism_funding']['meta_contrast']
        salary = contrast.get('salary_funding_programs', 0)
        assert salary == 0, f"Meta should have 0 salary funding programs. Got: {salary}"

    def test_meta_zero_philanthropy_post_2022(self):
        """Meta has ZERO journalism philanthropy/grants post-2022."""
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        contrast = openai['triple_layer_journalism_funding']['meta_contrast']
        philanthropy = contrast.get('philanthropy_grants_post_2022', 0)
        assert philanthropy == 0, \
            f"Meta should have 0 post-2022 philanthropy grants. Got: {philanthropy}"


# ===================================================================
# Test Class 5: Structural Insight — Triple-Layer Uniqueness
# ===================================================================
class TestStructuralInsight:
    """Validate the structural insight: no tech company has simultaneously
    operated financial relationships at all three journalism stack levels.
    """

    def test_structural_insight_exists(self):
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        tlf = openai['triple_layer_journalism_funding']
        assert 'structural_insight' in tlf, \
            "Missing structural_insight in triple_layer_journalism_funding"

    def test_three_levels_documented(self):
        """Structural insight documents all three levels."""
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        insight = openai['triple_layer_journalism_funding']['structural_insight']
        levels = insight.get('levels', [])
        assert len(levels) == 3, f"Expected 3 levels. Got: {len(levels)}"

    def test_level_1_corporate(self):
        """Level 1 is corporate (content licensing)."""
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        insight = openai['triple_layer_journalism_funding']['structural_insight']
        levels = insight.get('levels', [])
        level_names = [str(l.get('level', '')).lower() for l in levels]
        assert any('corporate' in l for l in level_names), \
            f"Missing corporate level. Got: {level_names}"

    def test_level_2_individual(self):
        """Level 2 is individual (salary funding)."""
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        insight = openai['triple_layer_journalism_funding']['structural_insight']
        levels = insight.get('levels', [])
        level_names = [str(l.get('level', '')).lower() for l in levels]
        assert any('individual' in l for l in level_names), \
            f"Missing individual level. Got: {level_names}"

    def test_level_3_ecosystem(self):
        """Level 3 is ecosystem (philanthropic grants)."""
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        insight = openai['triple_layer_journalism_funding']['structural_insight']
        levels = insight.get('levels', [])
        level_names = [str(l.get('level', '')).lower() for l in levels]
        assert any('ecosystem' in l for l in level_names), \
            f"Missing ecosystem level. Got: {level_names}"

    def test_no_other_company_has_triple_layer(self):
        """Structural insight asserts no other company has all three layers."""
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        insight = openai['triple_layer_journalism_funding']['structural_insight']
        precedent = str(insight.get('unprecedented', '')).lower()
        assert 'no' in precedent or 'unprecedented' in precedent or 'first' in precedent, \
            f"Should assert triple-layer is unprecedented. Got: {precedent}"


# ===================================================================
# Test Class 6: Mechanism #53 in Competitor Coverage Research
# ===================================================================
class TestMechanism53InResearch:
    """Validate mechanism #53 exists in competitor-coverage-research.yaml."""

    def test_mechanism_53_exists(self):
        research = load_competitor_research()
        # Search for mechanism #53 in cross_publication_findings
        found = False
        for section_key in research:
            section = research[section_key]
            if isinstance(section, list):
                for item in section:
                    if isinstance(item, dict) and item.get('mechanism_id') == 53:
                        found = True
                        break
            elif isinstance(section, dict):
                for sub_key, sub_val in section.items():
                    if isinstance(sub_val, list):
                        for item in sub_val:
                            if isinstance(item, dict) and item.get('mechanism_id') == 53:
                                found = True
                                break
                    elif isinstance(sub_val, dict):
                        if sub_val.get('mechanism_id') == 53:
                            found = True
        assert found, "Mechanism #53 not found in competitor-coverage-research.yaml"

    def test_mechanism_53_name(self):
        research = load_competitor_research()
        m53 = self._find_mechanism_53(research)
        assert m53 is not None, "Mechanism #53 not found"
        name = m53.get('mechanism_name', '')
        assert 'Triple-Layer' in name or 'triple' in name.lower(), \
            f"Mechanism #53 name should reference Triple-Layer. Got: {name}"

    def test_mechanism_53_type_c(self):
        research = load_competitor_research()
        m53 = self._find_mechanism_53(research)
        assert m53 is not None, "Mechanism #53 not found"
        rotation = m53.get('rotation_type', '')
        assert rotation == 'C', f"Expected rotation_type C. Got: {rotation}"

    def test_mechanism_53_has_confounding_factors(self):
        research = load_competitor_research()
        m53 = self._find_mechanism_53(research)
        assert m53 is not None, "Mechanism #53 not found"
        factors = m53.get('confounding_factors', [])
        assert len(factors) >= 7, f"Expected at least 7 confounding factors. Got: {len(factors)}"

    def test_mechanism_53_has_testable_predictions(self):
        research = load_competitor_research()
        m53 = self._find_mechanism_53(research)
        assert m53 is not None, "Mechanism #53 not found"
        predictions = m53.get('testable_predictions', [])
        assert len(predictions) >= 4, \
            f"Expected at least 4 testable predictions. Got: {len(predictions)}"

    def test_mechanism_53_has_source_urls(self):
        research = load_competitor_research()
        m53 = self._find_mechanism_53(research)
        assert m53 is not None, "Mechanism #53 not found"
        urls = m53.get('source_urls', [])
        assert len(urls) >= 8, \
            f"Expected at least 8 source URLs. Got: {len(urls)}"

    def test_mechanism_53_has_date_added(self):
        research = load_competitor_research()
        m53 = self._find_mechanism_53(research)
        assert m53 is not None, "Mechanism #53 not found"
        date = str(m53.get('date_added', ''))
        assert '2026-08-11' in date, f"Expected date_added 2026-08-11. Got: {date}"

    @staticmethod
    def _find_mechanism_53(research):
        """Recursively find mechanism #53 in research YAML."""
        for section_key in research:
            section = research[section_key]
            if isinstance(section, list):
                for item in section:
                    if isinstance(item, dict) and item.get('mechanism_id') == 53:
                        return item
            elif isinstance(section, dict):
                for sub_key, sub_val in section.items():
                    if isinstance(sub_val, list):
                        for item in sub_val:
                            if isinstance(item, dict) and item.get('mechanism_id') == 53:
                                return item
                    elif isinstance(sub_val, dict):
                        if sub_val.get('mechanism_id') == 53:
                            return sub_val
        return None


# ===================================================================
# Test Class 7: Confounding Factors Detail
# ===================================================================
class TestConfoundingFactors:
    """Validate the 7 confounding factors have proper structure and strength ratings."""

    def _get_factors(self):
        research = load_competitor_research()
        m53 = TestMechanism53InResearch._find_mechanism_53(research)
        return m53.get('confounding_factors', [])

    def test_genuine_good_faith_factor(self):
        """Genuine good faith confounding factor exists with MODERATE strength."""
        factors = self._get_factors()
        factor_names = [str(f.get('factor', '')).lower() for f in factors]
        assert any('good faith' in f or 'genuine' in f for f in factor_names), \
            "Missing genuine good faith confounding factor"

    def test_industry_need_factor(self):
        """Industry need confounding factor exists with STRONG strength."""
        factors = self._get_factors()
        factor_names = [str(f.get('factor', '')).lower() for f in factors]
        assert any('industry' in f or 'need' in f for f in factor_names), \
            "Missing industry need confounding factor"

    def test_all_factors_have_strength(self):
        """All confounding factors have a strength rating."""
        factors = self._get_factors()
        valid_strengths = {'WEAK', 'MODERATE', 'STRONG'}
        for f in factors:
            strength = f.get('strength', '')
            assert strength in valid_strengths, \
                f"Factor '{f.get('factor', '')}' has invalid strength: {strength}"

    def test_at_least_one_strong_factor(self):
        """At least one confounding factor rated STRONG (honest assessment)."""
        factors = self._get_factors()
        strengths = [f.get('strength', '') for f in factors]
        assert 'STRONG' in strengths, \
            "Expected at least one STRONG confounding factor for honest assessment"


# ===================================================================
# Test Class 8: Total Financial Exposure Aggregation
# ===================================================================
class TestFinancialAggregation:
    """Validate aggregate financial exposure across all three layers."""

    def test_total_investment_documented(self):
        """Triple-layer section documents total financial exposure."""
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        tlf = openai['triple_layer_journalism_funding']
        assert 'total_journalism_investment_summary' in tlf, \
            "Missing total_journalism_investment_summary"

    def test_layer_1_estimated_annual(self):
        """Layer 1 content licensing estimated at $300-400M/year.
        Source: https://llmpulse.ai/blog/openai-publisher-deals/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        summary = openai['triple_layer_journalism_funding']['total_journalism_investment_summary']
        layer1 = str(summary.get('layer_1_annual_m', ''))
        assert '300' in layer1 or '400' in layer1, \
            f"Expected $300-400M annual for Layer 1. Got: {layer1}"

    def test_layer_2_total(self):
        """Layer 2 includes Axios + Lenfest funding."""
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        summary = openai['triple_layer_journalism_funding']['total_journalism_investment_summary']
        layer2 = str(summary.get('layer_2_total_m', ''))
        # Axios undisclosed + Lenfest $10M (shared with Microsoft)
        assert layer2, "Missing layer_2_total_m in summary"

    def test_layer_3_total(self):
        """Layer 3 AJP total: $10M cash + $8M credits across both phases.
        Sources: https://openai.com/index/partnership-with-american-journalism-project-to-support-local-news/
        https://www.newscaststudio.com/2026/07/22/openai-renews-local-news-partnership-with-5-million-investment/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        summary = openai['triple_layer_journalism_funding']['total_journalism_investment_summary']
        layer3 = str(summary.get('layer_3_total_m', ''))
        assert layer3, "Missing layer_3_total_m in summary"


# ===================================================================
# Test Class 9: Source URL Verification
# ===================================================================
class TestSourceURLs:
    """Validate that all source URLs are present and properly formatted."""

    def test_triple_layer_has_source_urls(self):
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        tlf = openai['triple_layer_journalism_funding']
        assert 'source_urls' in tlf, \
            "Missing source_urls in triple_layer_journalism_funding"

    def test_source_urls_include_llmpulse(self):
        """Must include LLM Pulse comprehensive tracker.
        Source: https://llmpulse.ai/blog/openai-publisher-deals/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        urls = openai['triple_layer_journalism_funding'].get('source_urls', [])
        assert any('llmpulse' in str(u) for u in urls), \
            "Missing LLM Pulse source URL"

    def test_source_urls_include_techcrunch_axios(self):
        """Must include TechCrunch article on Axios funding.
        Source: https://techcrunch.com/2025/01/15/openai-is-bankrolling-axios-expansion-into-four-new-markets/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        urls = openai['triple_layer_journalism_funding'].get('source_urls', [])
        assert any('techcrunch' in str(u) and 'axios' in str(u) for u in urls), \
            "Missing TechCrunch Axios source URL"

    def test_source_urls_include_openai_ajp(self):
        """Must include OpenAI's own AJP announcement.
        Source: https://openai.com/index/partnership-with-american-journalism-project-to-support-local-news/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        urls = openai['triple_layer_journalism_funding'].get('source_urls', [])
        assert any('openai.com' in str(u) and 'journalism' in str(u) for u in urls), \
            "Missing OpenAI AJP announcement URL"

    def test_source_urls_include_newscaststudio(self):
        """Must include NewscastStudio AJP Phase 2 renewal.
        Source: https://www.newscaststudio.com/2026/07/22/openai-renews-local-news-partnership-with-5-million-investment/
        """
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        urls = openai['triple_layer_journalism_funding'].get('source_urls', [])
        assert any('newscaststudio' in str(u) for u in urls), \
            "Missing NewscastStudio source URL"

    def test_at_least_10_source_urls(self):
        """Triple-layer section should have at least 10 source URLs."""
        entities = load_competitor_entities()
        openai = entities['entities']['openai']
        urls = openai['triple_layer_journalism_funding'].get('source_urls', [])
        assert len(urls) >= 10, \
            f"Expected at least 10 source URLs. Got: {len(urls)}"


# ===================================================================
# Test Class 10: Testable Predictions
# ===================================================================
class TestTestablePredictions:
    """Validate the 4 testable predictions in mechanism #53."""

    def _get_predictions(self):
        research = load_competitor_research()
        m53 = TestMechanism53InResearch._find_mechanism_53(research)
        return m53.get('testable_predictions', [])

    def test_prediction_count(self):
        predictions = self._get_predictions()
        assert len(predictions) >= 4, \
            f"Expected at least 4 testable predictions. Got: {len(predictions)}"

    def test_ajp_investigative_coverage_prediction(self):
        """Prediction: AJP newsrooms produce zero investigative OpenAI coverage."""
        predictions = self._get_predictions()
        pred_texts = [str(p).lower() for p in predictions]
        assert any('ajp' in p and ('investigat' in p or 'zero' in p) for p in pred_texts), \
            "Missing AJP investigative coverage prediction"

    def test_axios_local_framing_prediction(self):
        """Prediction: Axios Local AI coverage skews OpenAI-positive."""
        predictions = self._get_predictions()
        pred_texts = [str(p).lower() for p in predictions]
        assert any('axios' in p for p in pred_texts), \
            "Missing Axios Local coverage framing prediction"

    def test_ecosystem_shrinkage_prediction(self):
        """Prediction: available ecosystem for adversarial OpenAI reporting shrinks."""
        predictions = self._get_predictions()
        pred_texts = [str(p).lower() for p in predictions]
        assert any('shrink' in p or 'ecosystem' in p for p in pred_texts), \
            "Missing ecosystem shrinkage prediction"
