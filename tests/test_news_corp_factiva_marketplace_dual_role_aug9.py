"""
Type C: Financial Incentive Mapping — News Corp Factiva AI Marketplace Dual-Role Analysis
Date: 2026-08-09 05:00 PT

KEY FINDING: News Corp operates a unique DUAL ROLE in the AI content licensing ecosystem:
(1) As a PUBLISHER selling content directly to OpenAI ($50M/yr) and Meta (up to $50M/yr)
(2) As a MARKETPLACE OPERATOR through Factiva (Dow Jones subsidiary) selling AI licensing
    rights to 8,100+ news sources — more than 25% of all Factiva sources.

This makes News Corp the only MediaScope-profiled entity that is simultaneously a
content seller AND a marketplace operator, with editorial coverage (WSJ) that directly
affects both businesses. The WSJ is the only profiled publication that discloses this
conflict — its Jul 2, 2026 article on AI marketplaces included: "Factiva and The Wall
Street Journal are both part of News Corp's Dow Jones unit."

MEDIASCOPE SIGNIFICANCE: News Corp profits from BOTH its own content deals AND the
growth of the broader AI licensing market. This creates a 4th financial incentive
dimension beyond bilateral deals: News Corp's editorial coverage of AI content licensing
directly affects the market that its Factiva subsidiary operates in.

MARKETPLACE LANDSCAPE (as of Aug 9, 2026):
- Microsoft PCM: 8 publishers (Condé Nast, Hearst, etc.), >$10M invested, dual role (buyer + operator)
- Snowflake Cortex: 17 publishers (WashPost, AP, etc.), pure infrastructure, lowest conflict
- Amazon: Building marketplace, dual role (buyer + operator), $13B+ Anthropic investment
- Factiva: 8,100+ sources with AI rights, dual role (parent is publisher), unique publisher-operator conflict

Sources:
- WSJ (Jul 2, 2026): https://www.wsj.com/business/media/marketplaces-are-the-next-frontier-in-publisher-deals-with-ai-companies-11515b00
- News Corp Q4 FY2026 earnings call transcript (Aug 5, 2026): https://www.marketbeat.com/earnings/reports/2026-8-5-news-co-stock-1/
- Microsoft PCM launch: https://searchengineland.com/microsoft-launches-publisher-content-marketplace-for-ai-licensing-468191
- Amazon marketplace plans: https://hypebeast.com/2026/2/amazon-plans-aws-ai-content-marketplace-for-publishers
"""

import pytest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_news_corp():
    path = os.path.join(PROFILES_DIR, 'news-corp.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def load_competitor_entities():
    path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


# ==============================================================================
# Test Suite 1: Factiva Marketplace Role in News Corp Profile
# ==============================================================================

class TestFactivaMarketplaceRole:
    """Verify the Factiva marketplace role section exists and has correct data."""

    def test_factiva_section_exists(self):
        data = load_news_corp()
        assert 'factiva_marketplace_role' in data, \
            "News Corp profile must have factiva_marketplace_role section"

    def test_factiva_ai_licensing_sources_count(self):
        data = load_news_corp()
        fac = data['factiva_marketplace_role']['factiva_ai_licensing']
        assert fac['news_sources_with_ai_rights'] >= 8100, \
            f"Factiva AI-licensed sources should be >=8100, got {fac['news_sources_with_ai_rights']}"

    def test_factiva_pct_of_total_sources(self):
        data = load_news_corp()
        fac = data['factiva_marketplace_role']['factiva_ai_licensing']
        assert fac['pct_of_total_factiva_sources'] >= 25, \
            f"Factiva AI sources should be >=25% of total, got {fac['pct_of_total_factiva_sources']}"

    def test_factiva_parent_unit_is_dow_jones(self):
        data = load_news_corp()
        fac = data['factiva_marketplace_role']['factiva_ai_licensing']
        assert fac['parent_unit'] == 'Dow Jones', \
            f"Factiva parent should be Dow Jones, got {fac['parent_unit']}"

    def test_factiva_has_use_cases(self):
        data = load_news_corp()
        fac = data['factiva_marketplace_role']['factiva_ai_licensing']
        assert len(fac['use_cases']) >= 3, \
            f"Factiva should have >=3 use cases, got {len(fac['use_cases'])}"

    def test_factiva_overview_mentions_dual_role(self):
        data = load_news_corp()
        overview = data['factiva_marketplace_role']['overview']
        assert 'DUAL' in overview.upper() or 'dual' in overview, \
            "Overview should mention dual role"

    def test_factiva_has_source_urls(self):
        data = load_news_corp()
        urls = data['factiva_marketplace_role']['source_urls']
        assert len(urls) >= 1, "Must have at least one source URL"
        assert any('wsj.com' in u for u in urls), \
            "Should cite WSJ marketplace article"


# ==============================================================================
# Test Suite 2: Dual Role Financial Implications
# ==============================================================================

class TestDualRoleImplications:
    """Verify the dual role implications section captures the financial incentive analysis."""

    def test_dual_role_section_exists(self):
        data = load_news_corp()
        assert 'dual_role_implications' in data['factiva_marketplace_role'], \
            "Must have dual_role_implications section"

    def test_dual_role_lists_marketplace_competitors(self):
        data = load_news_corp()
        competitors = data['factiva_marketplace_role']['dual_role_implications']['marketplace_competitors']
        assert len(competitors) >= 3, \
            f"Should list >=3 marketplace competitors, got {len(competitors)}"

    def test_dual_role_mentions_microsoft_pcm(self):
        data = load_news_corp()
        competitors = data['factiva_marketplace_role']['dual_role_implications']['marketplace_competitors']
        assert any('Microsoft' in c or 'PCM' in c for c in competitors), \
            "Should mention Microsoft PCM as competitor"

    def test_dual_role_mentions_snowflake(self):
        data = load_news_corp()
        competitors = data['factiva_marketplace_role']['dual_role_implications']['marketplace_competitors']
        assert any('Snowflake' in c for c in competitors), \
            "Should mention Snowflake Cortex as competitor"

    def test_wsj_self_disclosure_documented(self):
        data = load_news_corp()
        disclosure = data['factiva_marketplace_role']['dual_role_implications']['wsj_self_disclosure']
        assert 'Factiva' in disclosure and 'Wall Street Journal' in disclosure, \
            "Should document WSJ's self-disclosure about Factiva conflict"

    def test_mediascope_significance_exists(self):
        data = load_news_corp()
        sig = data['factiva_marketplace_role']['mediascope_significance']
        assert len(sig) > 100, \
            "mediascope_significance should have substantial analysis"


# ==============================================================================
# Test Suite 3: Factiva in Competitor Entities Marketplace Landscape
# ==============================================================================

class TestFactivaInMarketplaceLandscape:
    """Verify Factiva is properly listed in the marketplace intermediary landscape."""

    def test_factiva_in_tier_2_operators(self):
        data = load_competitor_entities()
        landscape = data.get('marketplace_intermediary_landscape', {})
        tier_2 = landscape.get('tier_2_marketplace', {})
        operators = tier_2.get('operators', [])
        names = [op['name'] for op in operators]
        assert any('Factiva' in n for n in names), \
            f"Factiva should be in tier_2_marketplace operators, got: {names}"

    def test_factiva_dual_role_flagged(self):
        data = load_competitor_entities()
        operators = data['marketplace_intermediary_landscape']['tier_2_marketplace']['operators']
        factiva = [op for op in operators if 'Factiva' in op['name']][0]
        assert factiva['dual_role'] is True, \
            "Factiva should have dual_role=true (parent is publisher)"

    def test_factiva_not_buyer(self):
        data = load_competitor_entities()
        operators = data['marketplace_intermediary_landscape']['tier_2_marketplace']['operators']
        factiva = [op for op in operators if 'Factiva' in op['name']][0]
        assert factiva['is_buyer'] is False, \
            "Factiva is not an AI content buyer itself"

    def test_factiva_parent_is_publisher_flag(self):
        data = load_competitor_entities()
        operators = data['marketplace_intermediary_landscape']['tier_2_marketplace']['operators']
        factiva = [op for op in operators if 'Factiva' in op['name']][0]
        assert factiva.get('parent_is_publisher') is True, \
            "Factiva should have parent_is_publisher=true"

    def test_factiva_source_count(self):
        data = load_competitor_entities()
        operators = data['marketplace_intermediary_landscape']['tier_2_marketplace']['operators']
        factiva = [op for op in operators if 'Factiva' in op['name']][0]
        assert factiva['news_sources_with_ai_rights'] >= 8100, \
            f"Factiva sources should be >=8100, got {factiva['news_sources_with_ai_rights']}"

    def test_factiva_has_source_url(self):
        data = load_competitor_entities()
        operators = data['marketplace_intermediary_landscape']['tier_2_marketplace']['operators']
        factiva = [op for op in operators if 'Factiva' in op['name']][0]
        assert 'source_url' in factiva, "Factiva entry should have source_url"

    def test_four_marketplace_operators_total(self):
        """There should now be at least 4 marketplace operators: MS PCM, Snowflake, Amazon, Factiva."""
        data = load_competitor_entities()
        operators = data['marketplace_intermediary_landscape']['tier_2_marketplace']['operators']
        assert len(operators) >= 4, \
            f"Should have >=4 marketplace operators, got {len(operators)}"


# ==============================================================================
# Test Suite 4: News Corp as Balanced Control with Marketplace Revenue
# ==============================================================================

class TestNewsCorpControlDesignation:
    """Verify News Corp control designation accounts for marketplace role."""

    def test_control_designation_exists(self):
        data = load_news_corp()
        assert 'control_designation' in data, \
            "News Corp must have control_designation section"

    def test_control_is_balanced(self):
        data = load_news_corp()
        assert data['control_designation']['type'] == 'balanced_control', \
            "News Corp should be designated as balanced_control"

    def test_triple_revenue_note_exists(self):
        data = load_news_corp()
        note = data['control_designation'].get('triple_revenue_note', '')
        assert 'THREE' in note.upper() or 'triple' in note.lower() or '3' in note, \
            "Control designation should note triple revenue sources"

    def test_bilateral_deals_on_both_sides(self):
        """News Corp must have deals with both Meta AND OpenAI."""
        data = load_news_corp()
        relationships = data.get('revenue_relationships', [])
        partners = [r['partner'] for r in relationships]
        assert 'OpenAI' in partners, "Must have OpenAI deal"
        assert 'Meta' in partners, "Must have Meta deal"


# ==============================================================================
# Test Suite 5: WSJ Disclosure Practice Consistency
# ==============================================================================

class TestWSJDisclosurePractice:
    """Verify WSJ disclosure practice section is consistent with Factiva findings."""

    def test_disclosure_section_exists(self):
        data = load_news_corp()
        assert 'disclosure_practice' in data, \
            "News Corp must have disclosure_practice section"

    def test_unique_in_dataset(self):
        data = load_news_corp()
        assert data['disclosure_practice']['unique_in_dataset'] is True, \
            "WSJ should be unique in dataset for systematic disclosure"

    def test_has_meta_disclosure_text(self):
        data = load_news_corp()
        text = data['disclosure_practice'].get('meta_disclosure_text', '')
        assert 'Meta' in text, "Should have Meta disclosure template text"

    def test_has_openai_disclosure_text(self):
        data = load_news_corp()
        text = data['disclosure_practice'].get('openai_disclosure_text', '')
        assert 'OpenAI' in text, "Should have OpenAI disclosure template text"


# ==============================================================================
# Test Suite 6: Cross-Validation with Existing Financial Data
# ==============================================================================

class TestCrossValidation:
    """Cross-validate Factiva data with existing financial and earnings data."""

    def test_q4_fy2026_earnings_exist(self):
        data = load_news_corp()
        assert 'q4_fy2026' in data.get('financials', {}), \
            "Q4 FY2026 earnings data must exist"

    def test_dow_jones_revenue_consistent(self):
        """Dow Jones Q4 revenue should match earnings report ($644M)."""
        data = load_news_corp()
        dj_rev = data['financials']['q4_fy2026']['dow_jones_revenue_m']
        assert dj_rev == 644, \
            f"Dow Jones Q4 revenue should be $644M, got ${dj_rev}M"

    def test_dow_jones_b2b_pct(self):
        """Dow Jones B2B should be ~50% of EBITDA (where Factiva sits)."""
        data = load_news_corp()
        b2b_pct = data['financials']['q4_fy2026']['dow_jones_b2b_ebitda_pct']
        assert b2b_pct >= 50, \
            f"Dow Jones B2B EBITDA should be >=50%, got {b2b_pct}%"

    def test_full_year_fy2026_exists(self):
        data = load_news_corp()
        assert 'full_year_fy2026' in data.get('financials', {}), \
            "Full year FY2026 data must exist"

    def test_revenue_beat(self):
        data = load_news_corp()
        q4 = data['financials']['q4_fy2026']
        assert q4['revenue_beat'] is True, \
            "Q4 FY2026 should show revenue beat"

    def test_eps_beat(self):
        data = load_news_corp()
        q4 = data['financials']['q4_fy2026']
        assert q4['eps_beat'] is True, \
            "Q4 FY2026 should show EPS beat"


# ==============================================================================
# Test Suite 7: Marketplace Operator Conflict Level Ranking
# ==============================================================================

class TestMarketplaceConflictLevels:
    """Verify conflict levels are properly ranked across marketplace operators."""

    def _get_operators(self):
        data = load_competitor_entities()
        return data['marketplace_intermediary_landscape']['tier_2_marketplace']['operators']

    def test_microsoft_highest_conflict(self):
        operators = self._get_operators()
        ms = [op for op in operators if 'Microsoft' in op['name']][0]
        assert ms['conflict_level'] == 'highest', \
            f"Microsoft PCM conflict should be 'highest', got {ms['conflict_level']}"

    def test_snowflake_lowest_conflict(self):
        operators = self._get_operators()
        sf = [op for op in operators if 'Snowflake' in op['name']][0]
        assert sf['conflict_level'] == 'lowest', \
            f"Snowflake conflict should be 'lowest', got {sf['conflict_level']}"

    def test_factiva_medium_conflict(self):
        """Factiva has a unique conflict (parent is publisher) but no AI lab investments."""
        operators = self._get_operators()
        fac = [op for op in operators if 'Factiva' in op['name']][0]
        assert fac['conflict_level'] == 'medium', \
            f"Factiva conflict should be 'medium', got {fac['conflict_level']}"

    def test_amazon_high_conflict(self):
        operators = self._get_operators()
        amz = [op for op in operators if 'Amazon' in op['name']][0]
        assert amz['conflict_level'] == 'high', \
            f"Amazon conflict should be 'high', got {amz['conflict_level']}"


# ==============================================================================
# Test Suite 8: Source URL Completeness
# ==============================================================================

class TestSourceURLs:
    """Verify all new data points have source URLs."""

    def test_factiva_wsj_source(self):
        data = load_news_corp()
        urls = data['factiva_marketplace_role']['source_urls']
        assert any('wsj.com' in u for u in urls), \
            "Factiva section must cite WSJ source"

    def test_factiva_earnings_source(self):
        data = load_news_corp()
        urls = data['factiva_marketplace_role']['source_urls']
        assert any('marketbeat.com' in u for u in urls), \
            "Factiva section should cite earnings transcript"

    def test_factiva_entity_source_url(self):
        data = load_competitor_entities()
        operators = data['marketplace_intermediary_landscape']['tier_2_marketplace']['operators']
        factiva = [op for op in operators if 'Factiva' in op['name']][0]
        assert 'wsj.com' in factiva['source_url'], \
            "Factiva entity entry should cite WSJ source"
