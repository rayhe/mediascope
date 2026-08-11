"""
WIRED OpenAI ChatGPT Ad Business Coverage Selection Gap — Type A: Competitor Coverage Deep Dive (Aug 11, 2026)

Mechanism #48: Coverage SELECTION Gap — WIRED + OpenAI Advertising Business

KEY FINDING: WIRED (Conde Nast, OpenAI content deal partner since Aug 2024)
has ZERO standalone articles found covering OpenAI's ChatGPT advertising
business launch and growth (Jan-Aug 2026), while 20+ other outlets covered
it extensively. This is one of the most significant AI business model shifts
of 2026 — ChatGPT ads launched Feb 2026, hit $100M annualized revenue in
6 weeks, and are projected at $2.5B for 2026.

Critical details:
  - OpenAI uses "keywords in the conversation" and "chat history and past
    interactions" for ad targeting — more intimate than Meta's social data
  - Two former Meta executives (Fidji Simo, David Dugan) lead OpenAI's
    ad business — WIRED would normally cover this executive migration
  - ChatGPT uninstalls jumped 132% YoY in April, Claude downloads surged
    11x — WIRED would normally cover user backlash at this scale
  - OpenAI's ad business ($2.5B projected 2026, $100B by 2030) directly
    competes with the same publisher ad budgets Conde Nast depends on

Financial prediction: Conde Nast OpenAI deal -> coverage selection gap.
Meta has ZERO Conde Nast content licensing relationship -> no editorial
constraint on adversarial coverage.

Sources:
  - Reuters: ChatGPT $100M ad revenue in 6 weeks (Mar 26, 2026)
  - Gadgets360: ChatGPT conversation data targeting details
  - The Verge: ChatGPT uninstalls +132% YoY, Claude +11x
  - TechXplore: Fidji Simo "not optimize for time spent" quote
  - AdWeek: 600+ advertisers, self-serve Ads Manager launch
  - Sensor Tower: user backlash metrics

Created: 2026-08-11
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(name):
    with open(os.path.join(PROFILES_DIR, name)) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def research():
    return load_yaml('competitor-coverage-research.yaml')


@pytest.fixture(scope='module')
def entities():
    return load_yaml('competitor-entities.yaml')


@pytest.fixture(scope='module')
def wired():
    return load_yaml('wired.yaml')


@pytest.fixture(scope='module')
def mechanism(research):
    findings = research.get('cross_publication_findings', {})
    m = findings.get('wired_openai_chatgpt_ad_coverage_selection_gap')
    assert m is not None, (
        "cross_publication_findings must have wired_openai_chatgpt_ad_coverage_selection_gap"
    )
    return m


# == Class 1: OpenAI Ad Business Timeline ==================================


class TestOpenAIAdBusinessTimeline:
    """Verify key dates and facts about OpenAI's ad business are documented."""

    def test_mechanism_id_is_48(self, mechanism):
        assert mechanism.get('mechanism_id') == 48

    def test_has_ad_business_timeline(self, mechanism):
        timeline = mechanism.get('ad_business_timeline', [])
        assert len(timeline) >= 4, (
            f"Expected >= 4 timeline entries, got {len(timeline)}"
        )

    def test_announcement_date(self, mechanism):
        timeline = mechanism.get('ad_business_timeline', [])
        dates = [e.get('date', '') for e in timeline]
        assert any('2026-01' in d for d in dates), (
            "Timeline must include January 2026 announcement"
        )

    def test_launch_date(self, mechanism):
        timeline = mechanism.get('ad_business_timeline', [])
        dates = [e.get('date', '') for e in timeline]
        assert any('2026-02' in d for d in dates), (
            "Timeline must include February 2026 launch"
        )

    def test_100m_revenue_milestone(self, mechanism):
        timeline = mechanism.get('ad_business_timeline', [])
        events = ' '.join(e.get('event', '') for e in timeline)
        assert '100' in events or '100M' in events, (
            "Timeline must document $100M annualized revenue milestone"
        )

    def test_self_serve_ads_manager(self, mechanism):
        timeline = mechanism.get('ad_business_timeline', [])
        events = ' '.join(e.get('event', '') for e in timeline)
        assert 'self-serve' in events.lower() or 'ads manager' in events.lower() or \
               'self_serve' in events.lower(), (
            "Timeline must document self-serve Ads Manager launch"
        )


# == Class 2: Conversation Data Targeting ==================================


class TestConversationDataTargeting:
    """Verify OpenAI uses conversation data for ad targeting."""

    def test_has_targeting_section(self, mechanism):
        targeting = mechanism.get('conversation_data_targeting')
        assert targeting is not None, "Must document conversation data targeting"

    def test_keywords_in_conversation(self, mechanism):
        targeting = mechanism.get('conversation_data_targeting', {})
        methods = targeting.get('methods', [])
        methods_str = ' '.join(str(m) for m in methods)
        assert 'keyword' in methods_str.lower() or 'conversation' in methods_str.lower(), (
            "Must document keyword-in-conversation targeting"
        )

    def test_chat_history_targeting(self, mechanism):
        targeting = mechanism.get('conversation_data_targeting', {})
        methods = targeting.get('methods', [])
        methods_str = ' '.join(str(m) for m in methods)
        assert 'history' in methods_str.lower() or 'past interaction' in methods_str.lower(), (
            "Must document chat history / past interactions targeting"
        )

    def test_intimacy_comparison_to_meta(self, mechanism):
        targeting = mechanism.get('conversation_data_targeting', {})
        comparison = targeting.get('meta_comparison', '')
        assert len(comparison) > 20, (
            "Must include comparison to Meta's data practices"
        )

    def test_opt_out_documented(self, mechanism):
        targeting = mechanism.get('conversation_data_targeting', {})
        opt_out = targeting.get('opt_out', '')
        assert len(str(opt_out)) > 0, "Must document opt-out mechanism"


# == Class 3: Former Meta Executives at OpenAI =============================


class TestFormerMetaExecutivesAtOpenAI:
    """Verify Fidji Simo and David Dugan connections are documented."""

    def test_has_executives_section(self, mechanism):
        execs = mechanism.get('former_meta_executives', [])
        assert len(execs) >= 2, f"Expected >= 2 executives, got {len(execs)}"

    def test_fidji_simo_documented(self, mechanism):
        execs = mechanism.get('former_meta_executives', [])
        names = [e.get('name', '') for e in execs]
        assert any('Simo' in n for n in names), "Must document Fidji Simo"

    def test_fidji_simo_role(self, mechanism):
        execs = mechanism.get('former_meta_executives', [])
        simo = [e for e in execs if 'Simo' in e.get('name', '')]
        assert len(simo) >= 1
        assert 'CEO' in simo[0].get('openai_role', '') or \
               'Applications' in simo[0].get('openai_role', ''), (
            "Simo role must mention CEO of Applications"
        )

    def test_david_dugan_documented(self, mechanism):
        execs = mechanism.get('former_meta_executives', [])
        names = [e.get('name', '') for e in execs]
        assert any('Dugan' in n for n in names), "Must document David Dugan"

    def test_dugan_meta_background(self, mechanism):
        execs = mechanism.get('former_meta_executives', [])
        dugan = [e for e in execs if 'Dugan' in e.get('name', '')]
        assert len(dugan) >= 1
        meta_role = dugan[0].get('meta_role', '')
        assert 'Meta' in meta_role or 'meta' in meta_role or 'ad' in meta_role.lower(), (
            "Dugan must have Meta ads background documented"
        )

    def test_simo_meta_contrast_quote(self, mechanism):
        execs = mechanism.get('former_meta_executives', [])
        simo = [e for e in execs if 'Simo' in e.get('name', '')]
        assert len(simo) >= 1
        quote = simo[0].get('meta_contrast_quote', '')
        assert 'time spent' in quote.lower() or len(quote) > 20, (
            "Must include Simo's quote contrasting OpenAI with Meta"
        )


# == Class 4: Coverage Comparison Matrix ===================================


class TestCoverageComparisonMatrix:
    """Verify per-outlet coverage is documented."""

    def test_has_coverage_matrix(self, mechanism):
        matrix = mechanism.get('coverage_comparison_matrix', [])
        assert len(matrix) >= 6, (
            f"Expected >= 6 outlets in coverage matrix, got {len(matrix)}"
        )

    @pytest.mark.parametrize("outlet", [
        "Reuters", "The Verge", "TechCrunch", "AdWeek", "Engadget",
    ])
    def test_outlet_covered(self, mechanism, outlet):
        matrix = mechanism.get('coverage_comparison_matrix', [])
        names = [e.get('outlet', '') for e in matrix]
        assert any(outlet.lower() in n.lower() for n in names), (
            f"{outlet} must be in coverage comparison matrix"
        )

    def test_wired_absent(self, mechanism):
        matrix = mechanism.get('coverage_comparison_matrix', [])
        wired_entries = [e for e in matrix if 'WIRED' in e.get('outlet', '') or
                         'Wired' in e.get('outlet', '')]
        if wired_entries:
            for entry in wired_entries:
                assert entry.get('standalone_articles', 0) == 0, (
                    "WIRED must have 0 standalone articles on OpenAI ad business"
                )

    def test_minimum_outlets_covering(self, mechanism):
        matrix = mechanism.get('coverage_comparison_matrix', [])
        covered = [e for e in matrix if e.get('standalone_articles', 0) > 0]
        assert len(covered) >= 5, (
            f"Expected >= 5 outlets that covered the story, got {len(covered)}"
        )


# == Class 5: WIRED Coverage Gap Documentation ============================


class TestWIREDCoverageGap:
    """Verify the gap is documented with outlet count and financial prediction."""

    def test_has_finding_summary(self, mechanism):
        summary = mechanism.get('finding_summary', '')
        assert len(summary) > 100, "Finding summary must be substantive"

    def test_summary_mentions_zero_articles(self, mechanism):
        summary = mechanism.get('finding_summary', '')
        assert 'zero' in summary.lower() or '0' in summary, (
            "Summary must mention zero WIRED standalone articles"
        )

    def test_summary_mentions_other_outlets(self, mechanism):
        summary = mechanism.get('finding_summary', '')
        assert '20' in summary or 'other outlet' in summary.lower() or \
               'other publication' in summary.lower(), (
            "Summary must reference the 20+ other outlets that covered the story"
        )

    def test_has_finding_type(self, mechanism):
        ft = mechanism.get('finding_type', '')
        assert 'coverage' in ft.lower() or 'selection' in ft.lower() or \
               'competitor' in ft.lower(), (
            f"Finding type must relate to coverage/selection, got '{ft}'"
        )

    def test_has_discovery_date(self, mechanism):
        date = mechanism.get('discovery_date', mechanism.get('date_added', ''))
        assert '2026-08-11' in str(date), "Must have Aug 11 2026 discovery date"


# == Class 6: Financial Prediction =========================================


class TestFinancialPrediction:
    """Verify the financial relationship prediction maps."""

    def test_has_financial_prediction(self, mechanism):
        fp = mechanism.get('financial_prediction')
        assert fp is not None, "Must have financial_prediction section"

    def test_conde_nast_openai_deal(self, mechanism):
        fp = mechanism.get('financial_prediction', {})
        content = str(fp)
        assert 'Cond' in content or 'conde' in content.lower() or \
               'OpenAI' in content, (
            "Financial prediction must reference Conde Nast-OpenAI deal"
        )

    def test_meta_zero_relationship(self, mechanism):
        fp = mechanism.get('financial_prediction', {})
        content = str(fp)
        assert 'Meta' in content or 'zero' in content.lower(), (
            "Financial prediction must note Meta has zero Conde Nast deal"
        )

    def test_openai_ad_revenue_projection(self, mechanism):
        fp = mechanism.get('financial_prediction', {})
        content = str(fp)
        assert '2.5' in content or '2.5B' in content or 'billion' in content.lower(), (
            "Must document OpenAI projected 2026 ad revenue"
        )

    def test_publisher_ad_competition(self, mechanism):
        fp = mechanism.get('financial_prediction', {})
        content = str(fp)
        assert 'compet' in content.lower() or 'publisher' in content.lower() or \
               'ad' in content.lower(), (
            "Must document OpenAI ads competing with publisher ad revenue"
        )


# == Class 7: Legitimate Factors ===========================================


class TestLegitimateFactors:
    """Verify at least 6 legitimate factors are documented."""

    def test_has_at_least_6_factors(self, mechanism):
        factors = mechanism.get('legitimate_factors', [])
        assert len(factors) >= 6, (
            f"Expected >= 6 legitimate factors, got {len(factors)}"
        )

    def test_newsletter_factor(self, mechanism):
        factors = mechanism.get('legitimate_factors', [])
        factors_str = ' '.join(str(f) for f in factors)
        assert 'newsletter' in factors_str.lower() or 'subscriber' in factors_str.lower(), (
            "Must document newsletter/subscriber-only coverage possibility"
        )

    def test_editorial_priority_factor(self, mechanism):
        factors = mechanism.get('legitimate_factors', [])
        factors_str = ' '.join(str(f) for f in factors)
        assert 'editorial' in factors_str.lower() or 'priority' in factors_str.lower() or \
               'focus' in factors_str.lower(), (
            "Must document editorial priorities as legitimate factor"
        )

    def test_business_story_factor(self, mechanism):
        factors = mechanism.get('legitimate_factors', [])
        factors_str = ' '.join(str(f) for f in factors)
        assert 'business' in factors_str.lower() or 'industry' in factors_str.lower() or \
               'consumer' in factors_str.lower(), (
            "Must document industry/business story angle as factor"
        )

    def test_search_index_gap_factor(self, mechanism):
        factors = mechanism.get('legitimate_factors', [])
        factors_str = ' '.join(str(f) for f in factors)
        assert 'search' in factors_str.lower() or 'index' in factors_str.lower() or \
               'paywall' in factors_str.lower(), (
            "Must document search index gaps or paywall as factor"
        )

    def test_competitive_scoop_factor(self, mechanism):
        factors = mechanism.get('legitimate_factors', [])
        factors_str = ' '.join(str(f) for f in factors)
        assert 'scoop' in factors_str.lower() or 'exclusive' in factors_str.lower() or \
               'Decoder' in factors_str or 'decoder' in factors_str.lower() or \
               'Verge' in factors_str, (
            "Must document competitive scoop factor (Decoder podcast)"
        )

    def test_bundled_coverage_factor(self, mechanism):
        factors = mechanism.get('legitimate_factors', [])
        factors_str = ' '.join(str(f) for f in factors)
        assert 'bundled' in factors_str.lower() or 'roundup' in factors_str.lower() or \
               'broader' in factors_str.lower(), (
            "Must document possible bundled/roundup coverage"
        )


# == Class 8: Meta Ad Coverage Contrast ====================================


class TestMetaAdCoverageContrast:
    """Verify WIRED's Meta ad coverage vocabulary is documented for comparison."""

    def test_has_meta_ad_vocabulary(self, mechanism):
        vocab = mechanism.get('wired_meta_ad_vocabulary', {})
        assert vocab is not None and len(str(vocab)) > 20, (
            "Must document WIRED's vocabulary when covering Meta ad practices"
        )

    def test_surveillance_vocabulary(self, mechanism):
        vocab = mechanism.get('wired_meta_ad_vocabulary', {})
        terms = vocab.get('adversarial_terms', [])
        terms_str = ' '.join(str(t) for t in terms)
        assert 'surveillance' in terms_str.lower() or 'tracking' in terms_str.lower() or \
               'spy' in terms_str.lower(), (
            "Must include surveillance/tracking/spy vocabulary used for Meta"
        )

    def test_contrast_with_openai(self, mechanism):
        vocab = mechanism.get('wired_meta_ad_vocabulary', {})
        contrast = vocab.get('openai_contrast', '')
        assert len(str(contrast)) > 10, (
            "Must document the contrast in vocabulary for OpenAI vs Meta ads"
        )


# == Class 9: Conde Nast Financial Relationships ===========================


class TestCondeNastFinancialRelationships:
    """Verify Conde Nast deal data is documented."""

    def test_conde_nast_openai_deal_date(self, mechanism):
        fp = mechanism.get('financial_prediction', {})
        content = str(fp)
        assert '2024' in content or 'Aug' in content, (
            "Must document OpenAI deal date (Aug 2024)"
        )

    def test_conde_nast_apple_negotiations(self, mechanism):
        fp = mechanism.get('financial_prediction', {})
        content = str(fp)
        assert 'Apple' in content or '50M' in content or 'apple' in content.lower(), (
            "Must document Apple Intelligence negotiations (~$50M)"
        )

    def test_conde_nast_ad_revenue(self, mechanism):
        fp = mechanism.get('financial_prediction', {})
        content = str(fp)
        assert 'advertising' in content.lower() or 'ad revenue' in content.lower() or \
               'revenue' in content.lower(), (
            "Must document Conde Nast advertising revenue context"
        )


# == Class 10: User Backlash Uncovered =====================================


class TestUserBacklashUncovered:
    """Verify ChatGPT uninstall/boycott data is documented."""

    def test_has_user_backlash_section(self, mechanism):
        backlash = mechanism.get('user_backlash_data')
        assert backlash is not None, "Must have user_backlash_data section"

    def test_uninstall_spike(self, mechanism):
        backlash = mechanism.get('user_backlash_data', {})
        content = str(backlash)
        assert '132' in content or 'uninstall' in content.lower(), (
            "Must document 132% YoY uninstall spike"
        )

    def test_claude_surge(self, mechanism):
        backlash = mechanism.get('user_backlash_data', {})
        content = str(backlash)
        assert '11x' in content.lower() or 'claude' in content.lower() or \
               'Claude' in content, (
            "Must document Claude download surge"
        )

    def test_boycott_data(self, mechanism):
        backlash = mechanism.get('user_backlash_data', {})
        content = str(backlash)
        assert '2.5' in content or 'boycott' in content.lower() or \
               'million' in content.lower(), (
            "Must document user boycott data"
        )

    def test_sensor_tower_source(self, mechanism):
        sources = mechanism.get('source_urls', [])
        sources_str = ' '.join(str(s) for s in sources)
        backlash = mechanism.get('user_backlash_data', {})
        backlash_str = str(backlash)
        assert 'Sensor Tower' in backlash_str or 'sensor' in backlash_str.lower() or \
               'sensorto' in sources_str.lower() or 'verge' in sources_str.lower(), (
            "Must cite Sensor Tower or The Verge for backlash metrics"
        )
