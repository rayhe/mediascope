"""
Type C: Financial Incentive Mapping — Aug 6 2026
Apple-OpenAI Partnership Collapse, Google Publisher Class-Action,
CMA AI Overviews Opt-Out, Reddit Deal Instability

Tests verify the four major financial landscape developments documented
in this iteration:
1. Apple-OpenAI mutual litigation (partnership → breach threat → trade secret suit)
2. Google publisher class-action (Hachette/Cengage/Elsevier/Turow v. Google)
3. UK CMA world-first AI Overviews opt-out ruling (Jun 3 2026)
4. Reddit-Google deal instability ($60M/yr deal under review)
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_entities():
    path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


class TestAppleOpenAIPartnershipCollapse:
    """Verify the Apple-OpenAI partnership collapse is documented with
    all three phases: partnership, breach threat, trade secret suit."""

    def setup_method(self):
        self.data = load_competitor_entities()
        self.apple = self.data['entities']['apple']
        self.openai = self.data['entities']['openai']

    def test_apple_has_partnership_collapse_section(self):
        assert 'openai_partnership_collapse' in self.apple
        collapse = self.apple['openai_partnership_collapse']
        assert 'overview' in collapse
        assert 'mutual litigation' in collapse['overview'].lower()

    def test_three_phases_documented(self):
        collapse = self.apple['openai_partnership_collapse']
        assert 'phase_1_partnership' in collapse
        assert 'phase_2_openai_breach_threat' in collapse
        assert 'phase_3_apple_sues_openai' in collapse

    def test_phase_1_date(self):
        phase1 = self.apple['openai_partnership_collapse']['phase_1_partnership']
        assert str(phase1['date']) == '2024-06'

    def test_phase_2_date(self):
        phase2 = self.apple['openai_partnership_collapse']['phase_2_openai_breach_threat']
        assert str(phase2['date']) == '2026-05-14'

    def test_phase_3_date(self):
        phase3 = self.apple['openai_partnership_collapse']['phase_3_apple_sues_openai']
        assert str(phase3['date']) == '2026-07-10'

    def test_openai_exec_failure_quote(self):
        phase2 = self.apple['openai_partnership_collapse']['phase_2_openai_breach_threat']
        assert 'failure' in phase2['detail'].lower() or 'failure' in phase2.get('openai_exec_quote', '').lower()

    def test_trade_secret_lawsuit_details(self):
        phase3 = self.apple['openai_partnership_collapse']['phase_3_apple_sues_openai']
        detail = phase3['detail']
        assert 'trade secret' in detail.lower()
        assert 'io Products' in detail or 'io products' in detail.lower()
        assert '400' in detail  # 400+ former Apple employees

    def test_mediascope_relevance_documented(self):
        collapse = self.apple['openai_partnership_collapse']
        assert 'mediascope_relevance' in collapse
        relevance = collapse['mediascope_relevance']
        assert 'Condé Nast' in relevance or 'conde nast' in relevance.lower()

    def test_openai_entity_has_apple_collapse_ref(self):
        assert 'apple_partnership_collapse' in self.openai
        collapse = self.openai['apple_partnership_collapse']
        assert 'breach_threat_date' in collapse
        assert str(collapse['breach_threat_date']) == '2026-05-14'
        assert 'apple_trade_secret_suit_date' in collapse
        assert str(collapse['apple_trade_secret_suit_date']) == '2026-07-10'

    def test_source_urls_present(self):
        phase2 = self.apple['openai_partnership_collapse']['phase_2_openai_breach_threat']
        assert 'source_urls' in phase2
        assert len(phase2['source_urls']) >= 2

    def test_phase_3_source_url(self):
        phase3 = self.apple['openai_partnership_collapse']['phase_3_apple_sues_openai']
        assert 'source_url' in phase3
        assert 'macrumors.com' in phase3['source_url']


class TestGooglePublisherClassAction:
    """Verify the Hachette/Cengage/Elsevier/Turow v. Google class-action
    copyright lawsuit (Jul 10 2026) is documented."""

    def setup_method(self):
        self.data = load_competitor_entities()
        self.google = self.data['entities']['google']

    def test_publisher_litigation_section_exists(self):
        assert 'publisher_litigation_jul2026' in self.google

    def test_litigation_date(self):
        lit = self.google['publisher_litigation_jul2026']
        assert str(lit['date']) == '2026-07-10'

    def test_court_and_case_number(self):
        lit = self.google['publisher_litigation_jul2026']
        assert 'SDNY' in lit['court']
        assert '1:26-cv-05870' in lit['court']

    def test_all_plaintiffs_listed(self):
        lit = self.google['publisher_litigation_jul2026']
        plaintiffs = lit['plaintiffs']
        assert 'Hachette Book Group' in plaintiffs
        assert 'Cengage Learning' in plaintiffs
        assert 'Elsevier' in plaintiffs
        assert any('Turow' in p for p in plaintiffs)

    def test_key_allegations_documented(self):
        detail = self.google['publisher_litigation_jul2026']['detail']
        assert 'prolific infringements' in detail.lower() or 'most prolific' in detail.lower()
        assert 'Gemini' in detail
        assert 'pirate' in detail.lower()

    def test_internal_fine_estimate(self):
        detail = self.google['publisher_litigation_jul2026']['detail']
        assert '$10Bs' in detail or '10Bs' in detail

    def test_murder_mystery_stat(self):
        detail = self.google['publisher_litigation_jul2026']['detail']
        assert '100-page' in detail or '20 minutes' in detail

    def test_source_urls_present(self):
        lit = self.google['publisher_litigation_jul2026']
        assert 'source_urls' in lit
        assert len(lit['source_urls']) >= 2

    def test_mediascope_relevance_bifurcated(self):
        lit = self.google['publisher_litigation_jul2026']
        assert 'mediascope_relevance' in lit
        relevance = lit['mediascope_relevance']
        # Key insight: book publishers suing, news publishers still in deals
        assert 'book publisher' in relevance.lower() or 'news publisher' in relevance.lower()


class TestCMAOptOutRuling:
    """Verify the UK CMA AI Overviews opt-out ruling (Jun 3 2026)
    is documented in Google's entity profile."""

    def setup_method(self):
        self.data = load_competitor_entities()
        self.google = self.data['entities']['google']

    def test_cma_section_exists(self):
        assert 'cma_ai_overviews_opt_out' in self.google

    def test_cma_date(self):
        cma = self.google['cma_ai_overviews_opt_out']
        assert str(cma['date']) == '2026-06-03'

    def test_world_first_designation(self):
        cma = self.google['cma_ai_overviews_opt_out']
        ruling = cma['ruling']
        assert 'world' in ruling.lower() and 'first' in ruling.lower()

    def test_strategic_market_status(self):
        cma = self.google['cma_ai_overviews_opt_out']
        assert cma['designation'] == 'Strategic Market Status (Oct 2025)'

    def test_implementation_timeline(self):
        cma = self.google['cma_ai_overviews_opt_out']
        assert '9-month' in cma['ruling'] or '9 month' in cma['ruling']

    def test_coercion_escalation_documented(self):
        cma = self.google['cma_ai_overviews_opt_out']
        assert 'coercion_escalation' in cma
        coercion = cma['coercion_escalation']
        assert 'QUADRUPLE' in coercion or 'quadruple' in coercion

    def test_four_coercion_vectors(self):
        coercion = self.google['cma_ai_overviews_opt_out']['coercion_escalation']
        assert '(a)' in coercion
        assert '(b)' in coercion
        assert '(c)' in coercion
        assert '(d)' in coercion

    def test_ai_overviews_user_stats(self):
        cma = self.google['cma_ai_overviews_opt_out']
        assert 'stat' in cma
        assert '2.5B' in cma['stat'] or '2.5 billion' in cma['stat'].lower()

    def test_source_urls_include_techcrunch_and_reuters(self):
        cma = self.google['cma_ai_overviews_opt_out']
        urls = cma['source_urls']
        has_techcrunch = any('techcrunch.com' in u for u in urls)
        has_reuters = any('reuters.com' in u for u in urls)
        assert has_techcrunch
        assert has_reuters


class TestRedditDealInstability:
    """Verify the Reddit-Google deal instability (late Jul 2026)
    is documented."""

    def setup_method(self):
        self.data = load_competitor_entities()
        self.google = self.data['entities']['google']

    def test_reddit_section_exists(self):
        assert 'reddit_deal_instability' in self.google

    def test_reddit_deal_value(self):
        reddit = self.google['reddit_deal_instability']
        assert '$60M' in reddit['detail'] or '60 million' in reddit['detail'].lower()

    def test_stock_impact(self):
        reddit = self.google['reddit_deal_instability']
        assert '8%' in reddit['detail']

    def test_other_publishers_considering_blocks(self):
        detail = self.google['reddit_deal_instability']['detail']
        assert 'Reuters' in detail or 'Politico' in detail or 'Economist' in detail

    def test_paradox_documented(self):
        detail = self.google['reddit_deal_instability']['detail']
        assert 'paradox' in detail.lower()

    def test_source_url_present(self):
        reddit = self.google['reddit_deal_instability']
        assert 'source_urls' in reddit
        assert len(reddit['source_urls']) >= 1


class TestCoercionDetailUpdated:
    """Verify the cross_platform_summary coercion_detail is updated
    with CMA ruling, class-action, and Reddit instability."""

    def setup_method(self):
        self.data = load_competitor_entities()
        meta_ai = self.data.get('meta_ai_deals', {})
        self.summary = meta_ai.get('cross_platform_summary', {})
        self.google_pilot = self.summary.get('google_news_ai_pilot', {})

    def test_coercion_detail_mentions_quadruple(self):
        coercion = self.google_pilot.get('coercion_detail', '')
        assert 'QUADRUPLE' in coercion or 'quadruple' in coercion

    def test_coercion_mentions_cma(self):
        coercion = self.google_pilot.get('coercion_detail', '')
        assert 'CMA' in coercion

    def test_coercion_mentions_class_action(self):
        coercion = self.google_pilot.get('coercion_detail', '')
        assert 'class-action' in coercion.lower() or 'Hachette' in coercion

    def test_coercion_mentions_reddit_instability(self):
        coercion = self.google_pilot.get('coercion_detail', '')
        assert 'Reddit' in coercion

    def test_meta_contrast_preserved(self):
        coercion = self.google_pilot.get('coercion_detail', '')
        assert 'Meta' in coercion and 'voluntary' in coercion.lower()


class TestAppleOpenAICollapseCrossPlatform:
    """Verify the apple_openai_partnership_collapse section exists
    in cross_platform_summary."""

    def setup_method(self):
        self.data = load_competitor_entities()
        meta_ai = self.data.get('meta_ai_deals', {})
        self.summary = meta_ai.get('cross_platform_summary', {})

    def test_collapse_section_exists(self):
        assert 'apple_openai_partnership_collapse' in self.summary

    def test_timeline_has_three_events(self):
        collapse = self.summary['apple_openai_partnership_collapse']
        assert 'timeline' in collapse
        assert len(collapse['timeline']) >= 3

    def test_timeline_chronological(self):
        timeline = self.summary['apple_openai_partnership_collapse']['timeline']
        dates = [str(e['date']) for e in timeline]
        assert dates[0] < dates[1] < dates[2]

    def test_mediascope_relevance_mentions_conde_nast(self):
        collapse = self.summary['apple_openai_partnership_collapse']
        relevance = collapse.get('mediascope_relevance', '')
        assert 'Condé Nast' in relevance or 'CN' in relevance

    def test_source_urls_present(self):
        collapse = self.summary['apple_openai_partnership_collapse']
        assert 'source_urls' in collapse
        assert len(collapse['source_urls']) >= 2
