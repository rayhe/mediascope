"""
WSJ × OpenAI Ad Cannibalization — Content Licensee Self-Demonetization Paradox

Type A: Competitor Coverage Deep Dive (Aug 10, 2026 05:00 PT)

Validates Mechanism #22: News Corp/WSJ licenses content to OpenAI ($50M/yr) →
OpenAI uses that content to build an ad-supported chatbot → ChatGPT ads directly
compete with publisher ad revenue → Paywall Penalty study shows WSJ gets 0% AI
citations → WSJ doesn't investigate this self-demonetization cycle.

The paradox: OpenAI's ad business is a MORE existential threat to publishers than
Meta's ad business (which doesn't use publisher content at all), yet WSJ covers
OpenAI ads with neutral business framing and applies zero investigative resources
to the structural threat from its own content licensing partner.
"""

import yaml
import os
import pytest

PROFILE_PATH = os.path.join(
    os.path.dirname(__file__), '..', 'profiles', 'news-corp.yaml'
)


@pytest.fixture(scope='module')
def news_corp_profile():
    with open(PROFILE_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def competitor_rels(news_corp_profile):
    cr = news_corp_profile.get('competitor_relationships', {})
    assert cr, "Missing competitor_relationships in news-corp.yaml"
    return cr


@pytest.fixture(scope='module')
def mechanism(news_corp_profile):
    cr = news_corp_profile.get('competitor_relationships', {})
    section = cr.get('wsj_openai_ad_cannibalization_silence')
    assert section is not None, (
        "Missing wsj_openai_ad_cannibalization_silence in news-corp.yaml"
    )
    return section


# ── Class 1: Mechanism Structure ─────────────────────────────────────


class TestMechanismStructure:
    """Verify the mechanism section has all required fields."""

    def test_mechanism_id(self, mechanism):
        assert mechanism.get('mechanism_id') == 22

    def test_mechanism_name(self, mechanism):
        name = mechanism.get('mechanism_name', '')
        assert 'Self-Demonetization' in name or 'Cannibalization' in name

    def test_date_analyzed(self, mechanism):
        assert mechanism.get('date_analyzed') == '2026-08-10'

    def test_has_description(self, mechanism):
        desc = mechanism.get('description', '')
        assert len(desc) > 100

    def test_description_mentions_50m(self, mechanism):
        desc = mechanism.get('description', '')
        assert '$50M' in desc

    def test_description_mentions_paywall_penalty(self, mechanism):
        desc = mechanism.get('description', '')
        assert 'Paywall Penalty' in desc or '0%' in desc


# ── Class 2: Financial Chain ─────────────────────────────────────────


class TestFinancialChain:
    """Verify the complete financial chain from content licensing to ad cannibalization."""

    def test_chain_exists(self, mechanism):
        chain = mechanism.get('financial_chain')
        assert chain is not None

    def test_step_1_content_licensing(self, mechanism):
        chain = mechanism['financial_chain']
        step1 = chain.get('step_1', '')
        assert 'News Corp' in step1 or 'WSJ' in step1
        assert 'OpenAI' in step1
        assert '$50M' in step1

    def test_step_2_training(self, mechanism):
        chain = mechanism['financial_chain']
        step2 = chain.get('step_2', '')
        assert 'content' in step2.lower()
        assert 'ChatGPT' in step2 or 'train' in step2.lower()

    def test_step_3_ad_launch(self, mechanism):
        chain = mechanism['financial_chain']
        step3 = chain.get('step_3', '')
        assert 'ad' in step3.lower()
        assert '2026' in step3

    def test_step_4_revenue_projections(self, mechanism):
        chain = mechanism['financial_chain']
        step4 = chain.get('step_4', '')
        assert '$2.5B' in step4 or '$100B' in step4

    def test_step_5_paywall_penalty(self, mechanism):
        chain = mechanism['financial_chain']
        step5 = chain.get('step_5', '')
        assert '0%' in step5 or 'Paywall Penalty' in step5

    def test_step_6_financial_disincentive(self, mechanism):
        chain = mechanism['financial_chain']
        step6 = chain.get('step_6', '')
        assert '$50M' in step6 or 'disincentive' in step6.lower()

    def test_net_effect_described(self, mechanism):
        chain = mechanism['financial_chain']
        net = chain.get('net_effect', '')
        assert len(net) > 50


# ── Class 3: OpenAI Ad Business Facts ─────────────────────────────────


class TestOpenAIAdBusinessFacts:
    """Verify documented facts about OpenAI's advertising business."""

    def test_facts_section_exists(self, mechanism):
        facts = mechanism.get('openai_ad_business_facts')
        assert facts is not None

    def test_launch_date(self, mechanism):
        facts = mechanism['openai_ad_business_facts']
        assert facts.get('launched') == '2026-01'

    def test_pilot_100m_speed(self, mechanism):
        facts = mechanism['openai_ad_business_facts']
        assert facts.get('pilot_100m_arr_weeks') == 6

    def test_2026_projection(self, mechanism):
        facts = mechanism['openai_ad_business_facts']
        assert facts.get('projected_2026_b') == 2.5

    def test_2030_projection(self, mechanism):
        facts = mechanism['openai_ad_business_facts']
        assert facts.get('projected_2030_b') == 100

    def test_ads_head_from_meta(self, mechanism):
        facts = mechanism['openai_ad_business_facts']
        head = facts.get('ads_head', '')
        assert 'Dugan' in head
        assert 'Meta' in head

    def test_source_urls(self, mechanism):
        facts = mechanism['openai_ad_business_facts']
        urls = facts.get('source_urls', [])
        assert len(urls) >= 2
        assert all(url.startswith('http') for url in urls)


# ── Class 4: Paywall Penalty Study ───────────────────────────────────


class TestPaywallPenaltyStudy:
    """Verify documentation of the Paywall Penalty study findings."""

    def test_study_section_exists(self, mechanism):
        study = mechanism.get('paywall_penalty_study')
        assert study is not None

    def test_study_title(self, mechanism):
        study = mechanism['paywall_penalty_study']
        title = study.get('title', '')
        assert 'Paywall Penalty' in title

    def test_study_date(self, mechanism):
        study = mechanism['paywall_penalty_study']
        assert '2026' in str(study.get('date', ''))

    def test_zero_citation_finding(self, mechanism):
        study = mechanism['paywall_penalty_study']
        finding = study.get('finding', '')
        assert '0%' in finding
        assert 'WSJ' in finding

    def test_scoop_paradox(self, mechanism):
        study = mechanism['paywall_penalty_study']
        paradox = study.get('paradox', '')
        assert 'WSJ' in paradox
        assert 'OpenAI' in paradox or 'AI' in paradox

    def test_source_url(self, mechanism):
        study = mechanism['paywall_penalty_study']
        url = study.get('source_url', '')
        assert url.startswith('http')


# ── Class 5: WSJ Coverage of OpenAI Ads ──────────────────────────────


class TestWSJCoverageOpenAIAds:
    """Verify documented examples of WSJ's coverage of OpenAI's ad business."""

    def test_coverage_examples_exist(self, mechanism):
        examples = mechanism.get('wsj_coverage_of_openai_ads', [])
        assert len(examples) >= 2

    def test_no_publisher_threat_framing(self, mechanism):
        """Key finding: WSJ does not frame OpenAI ads as a publisher threat."""
        examples = mechanism.get('wsj_coverage_of_openai_ads', [])
        for ex in examples:
            assert ex.get('threat_to_publishers_mentioned') is False, (
                f"Expected no publisher threat framing in: {ex.get('title')}"
            )

    def test_no_deal_disclosure(self, mechanism):
        """WSJ doesn't disclose its own $50M/yr OpenAI deal in ad coverage."""
        examples = mechanism.get('wsj_coverage_of_openai_ads', [])
        for ex in examples:
            assert ex.get('news_corp_deal_disclosed') is False, (
                f"Expected no deal disclosure in: {ex.get('title')}"
            )

    def test_neutral_to_positive_tone(self, mechanism):
        """WSJ covers OpenAI ads with neutral-to-mildly-negative tone (business reporting)."""
        examples = mechanism.get('wsj_coverage_of_openai_ads', [])
        for ex in examples:
            tone = ex.get('tone', 0)
            # Even the critical article is only -0.3 (internal dynamics, not existential)
            assert tone >= -0.5, (
                f"Tone {tone} too negative for neutral business framing: {ex.get('title')}"
            )


# ── Class 6: WSJ Coverage of Meta Ads ────────────────────────────────


class TestWSJCoverageMetaAds:
    """Compare WSJ's coverage of Meta's ad business — structurally, Meta's ads
    are LESS threatening to publishers than OpenAI's because Meta doesn't use
    publisher content in its ad products."""

    def test_meta_ad_coverage_exists(self, mechanism):
        examples = mechanism.get('wsj_coverage_of_meta_ads', [])
        assert len(examples) >= 1

    def test_meta_ad_coverage_source_url(self, mechanism):
        examples = mechanism.get('wsj_coverage_of_meta_ads', [])
        for ex in examples:
            url = ex.get('source_url', '')
            assert url.startswith('http')

    def test_meta_coverage_is_neutral(self, mechanism):
        """Meta ad coverage is also neutral — the asymmetry is in depth, not tone."""
        examples = mechanism.get('wsj_coverage_of_meta_ads', [])
        for ex in examples:
            tone = ex.get('tone', 0)
            assert -0.5 <= tone <= 0.5


# ── Class 7: Asymmetry Analysis ──────────────────────────────────────


class TestAsymmetryAnalysis:
    """Verify the core asymmetry finding: investigative depth gap, not tone gap."""

    def test_analysis_section_exists(self, mechanism):
        analysis = mechanism.get('asymmetry_analysis')
        assert analysis is not None

    def test_key_finding(self, mechanism):
        analysis = mechanism['asymmetry_analysis']
        finding = analysis.get('key_finding', '')
        assert len(finding) > 100
        assert 'OpenAI' in finding

    def test_uninvestigated_stories(self, mechanism):
        """WSJ has at least 4 stories it COULD investigate but hasn't."""
        analysis = mechanism['asymmetry_analysis']
        stories = analysis.get('what_wsj_could_investigate_but_hasnt', [])
        assert len(stories) >= 4

    def test_traffic_displacement_on_list(self, mechanism):
        analysis = mechanism['asymmetry_analysis']
        stories = analysis.get('what_wsj_could_investigate_but_hasnt', [])
        topics = ' '.join(stories).lower()
        assert 'traffic' in topics or 'displaced' in topics

    def test_paywall_penalty_on_list(self, mechanism):
        analysis = mechanism['asymmetry_analysis']
        stories = analysis.get('what_wsj_could_investigate_but_hasnt', [])
        topics = ' '.join(stories).lower()
        assert 'paywall' in topics or '0%' in topics or 'citation' in topics

    def test_comparison_to_meta_coverage(self, mechanism):
        analysis = mechanism['asymmetry_analysis']
        comparison = analysis.get('comparison_to_meta_coverage', '')
        assert 'Meta' in comparison
        assert 'investigative' in comparison.lower() or 'depth' in comparison.lower()

    def test_asymmetry_is_depth_not_tone(self, mechanism):
        """The key insight: the asymmetry is in investigative DEPTH, not in tone."""
        analysis = mechanism['asymmetry_analysis']
        finding = analysis.get('key_finding', '')
        comparison = analysis.get('comparison_to_meta_coverage', '')
        combined = finding + comparison
        assert 'depth' in combined.lower() or 'investigative' in combined.lower()


# ── Class 8: Counter-Arguments ───────────────────────────────────────


class TestCounterArguments:
    """Ensure legitimate counter-arguments are documented."""

    def test_counter_arguments_exist(self, mechanism):
        counters = mechanism.get('counter_arguments')
        assert counters is not None
        assert len(counters) >= 3

    def test_business_reporting_norms(self, mechanism):
        counters = mechanism['counter_arguments']
        assert 'business_reporting_norms' in counters

    def test_deal_may_be_net_positive(self, mechanism):
        counters = mechanism['counter_arguments']
        assert 'deal_may_be_net_positive' in counters

    def test_editorial_independence(self, mechanism):
        counters = mechanism['counter_arguments']
        assert 'editorial_independence' in counters

    def test_early_market(self, mechanism):
        counters = mechanism['counter_arguments']
        assert 'early_market' in counters

    def test_barrons_mentioned_as_independence_evidence(self, mechanism):
        counters = mechanism['counter_arguments']
        independence = counters.get('editorial_independence', '')
        assert "Barron" in independence


# ── Class 9: Corroboration Sources ───────────────────────────────────


class TestCorroborationSources:
    """Verify external corroboration for mechanism claims."""

    def test_corroboration_exists(self, mechanism):
        sources = mechanism.get('corroboration_sources', [])
        assert len(sources) >= 4

    def test_all_have_urls(self, mechanism):
        sources = mechanism.get('corroboration_sources', [])
        for src in sources:
            url = src.get('url', '')
            assert url.startswith('http'), f"Missing URL for: {src.get('source')}"

    def test_paywall_penalty_study_corroborated(self, mechanism):
        sources = mechanism.get('corroboration_sources', [])
        source_names = [s.get('source', '') for s in sources]
        assert any('Paywall' in s or '5W' in s for s in source_names)

    def test_emarketer_corroborated(self, mechanism):
        sources = mechanism.get('corroboration_sources', [])
        source_names = [s.get('source', '') for s in sources]
        assert any('eMarketer' in s or 'Elliot' in s for s in source_names)


# ── Class 10: Cross-Entity Scoring ───────────────────────────────────


class TestCrossEntityScoring:
    """Verify scoring methodology and bounds."""

    def test_asymmetry_score_exists(self, mechanism):
        score = mechanism.get('cross_entity_asymmetry_score')
        assert score is not None

    def test_score_in_valid_range(self, mechanism):
        score = mechanism['cross_entity_asymmetry_score']
        assert 0 <= score <= 1

    def test_score_below_wired(self, mechanism):
        """Score should be below WIRED (0.82) since asymmetry is in depth, not tone."""
        score = mechanism['cross_entity_asymmetry_score']
        assert score < 0.82

    def test_score_above_trivial(self, mechanism):
        """Score should be above 0.5 given the documented financial chain."""
        score = mechanism['cross_entity_asymmetry_score']
        assert score > 0.5

    def test_methodology_exists(self, mechanism):
        methodology = mechanism.get('methodology', '')
        assert len(methodology) > 100

    def test_methodology_explains_lower_score(self, mechanism):
        methodology = mechanism.get('methodology', '')
        assert 'depth' in methodology.lower() or 'tone' in methodology.lower()


# ── Class 11: Structural Consistency ─────────────────────────────────


class TestStructuralConsistency:
    """Verify consistency with existing News Corp profile data."""

    def test_openai_deal_in_revenue_relationships(self, news_corp_profile):
        """The $250M deal should be documented in revenue_relationships."""
        rev_rels = news_corp_profile.get('revenue_relationships', [])
        openai_deals = [r for r in rev_rels if r.get('partner') == 'OpenAI']
        assert len(openai_deals) >= 1
        deal = openai_deals[0]
        assert '$250M' in deal.get('value', '')

    def test_openai_in_competitor_relationships(self, competitor_rels):
        """OpenAI should be in competitor_relationships."""
        assert 'openai' in competitor_rels

    def test_meta_in_competitor_relationships(self, competitor_rels):
        """Meta should be in competitor_relationships for comparison."""
        assert 'meta' in competitor_rels

    def test_openai_deal_value_consistent(self, competitor_rels):
        """OpenAI deal value should be consistent between sections."""
        openai = competitor_rels.get('openai', {})
        value = openai.get('estimated_value', '')
        assert '$50M' in value or '$250M' in value

    def test_meta_deal_value_documented(self, competitor_rels):
        """Meta deal should document the ~$50M/yr value for comparison."""
        meta = competitor_rels.get('meta', {})
        value = meta.get('estimated_value', '')
        assert '$50M' in value
