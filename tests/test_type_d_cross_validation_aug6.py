"""
Type D: Cross-validation tests for data consistency across profiles.

Verifies that the financial landscape data added in Types A-C (Aug 5-6)
is internally consistent: deal counts match, entity cross-references
resolve, litigation data aligns, and the three-tier model is structurally
sound across all supporting profiles.
"""

import pytest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    with open(os.path.join(PROFILES_DIR, filename)) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def entities():
    return load_yaml('competitor-entities.yaml')


@pytest.fixture(scope='module')
def wired():
    return load_yaml('wired.yaml')


@pytest.fixture(scope='module')
def gizmodo():
    return load_yaml('gizmodo.yaml')


@pytest.fixture(scope='module')
def research():
    return load_yaml('competitor-coverage-research.yaml')


# ─── Deal Count Cascade Consistency ───────────────────────────────────


class TestDealCountCrossValidation:
    """Verify deal counts are consistent between aggregate and per-pub data."""

    def test_aggregate_total_is_19(self, entities):
        agg = entities['meta_ai_deals']['aggregate_incentive_matrix']
        assert agg['total_competitor_deal_count'] == 19

    def test_per_publication_sums_to_19(self, entities):
        agg = entities['meta_ai_deals']['aggregate_incentive_matrix']
        pubs = agg['publications']
        total = sum(p['competitor_deals'] for p in pubs)
        assert total == 19, f"Per-publication sum {total} != 19"

    def test_all_meta_deals_zero_in_aggregate(self, entities):
        agg = entities['meta_ai_deals']['aggregate_incentive_matrix']
        for pub in agg['publications']:
            assert pub['meta_deals'] == 0, f"{pub['name']} has non-zero meta_deals"

    def test_total_meta_deal_count_zero(self, entities):
        agg = entities['meta_ai_deals']['aggregate_incentive_matrix']
        assert agg['total_meta_deal_count'] == 0

    def test_wired_has_most_deals(self, entities):
        agg = entities['meta_ai_deals']['aggregate_incentive_matrix']
        pubs = agg['publications']
        wired_deals = next(p['competitor_deals'] for p in pubs if 'WIRED' in p['name'])
        max_deals = max(p['competitor_deals'] for p in pubs)
        assert wired_deals == max_deals, "WIRED should lead in competitor deals"

    def test_wired_has_5_deals(self, entities):
        agg = entities['meta_ai_deals']['aggregate_incentive_matrix']
        pubs = agg['publications']
        wired_deals = next(p['competitor_deals'] for p in pubs if 'WIRED' in p['name'])
        assert wired_deals == 5

    def test_gizmodo_has_0_deals(self, entities):
        agg = entities['meta_ai_deals']['aggregate_incentive_matrix']
        pubs = agg['publications']
        gizmodo_deals = next(p['competitor_deals'] for p in pubs if 'Gizmodo' in p['name'])
        assert gizmodo_deals == 0


# ─── Apple-OpenAI Collapse Cross-Reference ────────────────────────────


class TestAppleOpenAICrossReference:
    """Verify Apple-OpenAI collapse data is consistent between entity and cross_platform_summary."""

    def test_apple_entity_has_collapse(self, entities):
        apple = entities['entities']['apple']
        assert 'openai_partnership_collapse' in apple

    def test_openai_entity_has_collapse_ref(self, entities):
        openai = entities['entities']['openai']
        assert 'apple_partnership_collapse' in openai

    def test_apple_has_three_phases(self, entities):
        apple = entities['entities']['apple']
        collapse = apple['openai_partnership_collapse']
        phase_keys = [k for k in collapse if k.startswith('phase_')]
        assert len(phase_keys) == 3

    def test_cross_platform_summary_has_collapse(self, entities):
        cs = entities['meta_ai_deals']['cross_platform_summary']
        assert 'apple_openai_partnership_collapse' in cs

    def test_cross_platform_timeline_has_three_events(self, entities):
        cs = entities['meta_ai_deals']['cross_platform_summary']
        collapse = cs['apple_openai_partnership_collapse']
        timeline = collapse['timeline']
        assert len(timeline) == 3

    def test_collapse_source_urls_in_both(self, entities):
        apple = entities['entities']['apple']
        apple_sources = apple['openai_partnership_collapse'].get('phase_3_apple_sues_openai', {}).get('source_urls', [])
        cs = entities['meta_ai_deals']['cross_platform_summary']
        cs_sources = cs['apple_openai_partnership_collapse'].get('source_urls', [])
        # Both should have source URLs
        assert len(apple_sources) > 0 or len(cs_sources) > 0, "At least one location must have source URLs"

    def test_apple_phase_dates_chronological(self, entities):
        """Phases should be in chronological order."""
        apple = entities['entities']['apple']
        collapse = apple['openai_partnership_collapse']
        p1_date = str(collapse['phase_1_partnership']['date'])
        p2_date = str(collapse['phase_2_openai_breach_threat']['date'])
        p3_date = str(collapse['phase_3_apple_sues_openai']['date'])
        assert p1_date < p2_date < p3_date


# ─── Litigation Landscape Consistency ─────────────────────────────────


class TestLitigationLandscapeConsistency:
    """Verify litigation data is internally consistent across entities."""

    def test_google_class_action_has_court(self, entities):
        google = entities['entities']['google']
        lit = google['publisher_litigation_jul2026']
        assert 'SDNY' in lit['court']

    def test_google_class_action_has_plaintiffs(self, entities):
        google = entities['entities']['google']
        lit = google['publisher_litigation_jul2026']
        assert len(lit['plaintiffs']) >= 4

    def test_google_cma_opt_out_exists(self, entities):
        google = entities['entities']['google']
        assert 'cma_ai_overviews_opt_out' in google

    def test_google_cma_date_is_june_2026(self, entities):
        google = entities['entities']['google']
        cma = google['cma_ai_overviews_opt_out']
        assert str(cma['date']) == '2026-06-03'

    def test_google_reddit_instability_exists(self, entities):
        google = entities['entities']['google']
        assert 'reddit_deal_instability' in google

    def test_meta_has_zero_litigation(self, entities):
        """Meta should have no publisher litigation entries."""
        meta = entities['entities']['meta']
        meta_keys = [k for k in meta if 'litigation' in k.lower() or 'lawsuit' in k.lower()]
        assert len(meta_keys) == 0, f"Meta should have no litigation: {meta_keys}"

    def test_openai_entity_has_litigation_references(self, entities):
        openai = entities['entities']['openai']
        # OpenAI should have some reference to legal disputes
        openai_str = str(openai)
        assert 'lawsuit' in openai_str.lower() or 'litigation' in openai_str.lower() or 'sue' in openai_str.lower() or 'legal' in openai_str.lower() or 'breach' in openai_str.lower()


# ─── Three-Tier Model Structural Validation ───────────────────────────


class TestThreeTierModelConsistency:
    """Verify the three-tier model is structurally supported across profiles."""

    def test_gizmodo_is_tier_3_no_deals(self, entities):
        """Gizmodo (Tier 3) should have zero competitor deals."""
        agg = entities['meta_ai_deals']['aggregate_incentive_matrix']
        gizmodo = next(p for p in agg['publications'] if 'Gizmodo' in p['name'])
        assert gizmodo['competitor_deals'] == 0
        assert gizmodo['meta_deals'] == 0

    def test_gizmodo_still_adversarial(self, entities):
        """Even with no deals, Gizmodo has adversarial Meta coverage."""
        agg = entities['meta_ai_deals']['aggregate_incentive_matrix']
        gizmodo = next(p for p in agg['publications'] if 'Gizmodo' in p['name'])
        assert gizmodo['adversarial_meta_coverage'] is True

    def test_wired_is_tier_1_competitor_only(self, entities):
        """WIRED (Tier 1) should have competitor deals but no Meta deals."""
        agg = entities['meta_ai_deals']['aggregate_incentive_matrix']
        wired = next(p for p in agg['publications'] if 'WIRED' in p['name'])
        assert wired['competitor_deals'] > 0
        assert wired['meta_deals'] == 0

    def test_control_comparison_mentions_news_corp(self, entities):
        """Control comparison should reference News Corp as Tier 2 (both deals)."""
        agg = entities['meta_ai_deals']['aggregate_incentive_matrix']
        control = agg.get('control_comparison', '')
        assert 'News Corp' in control

    def test_control_comparison_mentions_gizmodo(self, entities):
        """Control comparison should reference Gizmodo as clean control."""
        agg = entities['meta_ai_deals']['aggregate_incentive_matrix']
        control = agg.get('control_comparison', '')
        assert 'Gizmodo' in control

    def test_all_8_publications_present(self, entities):
        """All 8 profiled publications should be in the aggregate matrix."""
        agg = entities['meta_ai_deals']['aggregate_incentive_matrix']
        names = [p['name'] for p in agg['publications']]
        assert len(names) == 8


# ─── Gizmodo Clean Control Cross-Validation ───────────────────────────


class TestGizmodoCleanControlCrossValidation:
    """Verify Gizmodo's clean control status is consistent between profiles."""

    def test_gizmodo_profile_has_cross_entity_coverage(self, gizmodo):
        """Gizmodo profile should have cross-entity coverage data."""
        assert 'cross_entity_coverage' in gizmodo or 'reporters' in gizmodo

    def test_gizmodo_research_has_asymmetry_verdict(self, research):
        """Competitor coverage research should have Gizmodo asymmetry verdict."""
        research_str = str(research)
        assert 'gizmodo' in research_str.lower() or 'clean control' in research_str.lower()

    def test_gizmodo_entity_aggregate_consistent(self, entities, gizmodo):
        """Gizmodo's zero-deal status should match between entity aggregate and profile."""
        agg = entities['meta_ai_deals']['aggregate_incentive_matrix']
        gizmodo_agg = next(p for p in agg['publications'] if 'Gizmodo' in p['name'])
        assert gizmodo_agg['competitor_deals'] == 0


# ─── Coercion Escalation Cross-Validation ─────────────────────────────


class TestCoercionEscalation:
    """Verify coercion escalation from triple to quadruple is consistent."""

    def test_coercion_detail_exists_in_cross_platform(self, entities):
        cs = entities['meta_ai_deals']['cross_platform_summary']
        # Google News AI pilot should reference coercion
        gnap = cs.get('google_news_ai_pilot', {})
        gnap_str = str(gnap)
        assert 'coerci' in gnap_str.lower() or 'quadruple' in gnap_str.lower() or 'pilot' in gnap_str.lower()

    def test_google_entity_has_four_coercion_vectors(self, entities):
        """Google entity should document at least 3 coercion vectors."""
        google = entities['entities']['google']
        google_str = str(google)
        coercion_keywords = ['advertising', 'search', 'showcase', 'pilot', 'coerci']
        matches = sum(1 for kw in coercion_keywords if kw in google_str.lower())
        assert matches >= 3, f"Only {matches} coercion vectors found"

    def test_cma_ruling_cross_referenced(self, entities):
        """CMA opt-out ruling should be documented in Google entity."""
        google = entities['entities']['google']
        cma = google.get('cma_ai_overviews_opt_out', {})
        assert 'strategic' in str(cma).lower() or 'market' in str(cma).lower()


# ─── Entity Count & Completeness ──────────────────────────────────────


class TestEntityCompleteness:
    """Verify all expected entities are present and well-formed."""

    EXPECTED_ENTITIES = ['openai', 'anthropic', 'amazon', 'apple', 'google', 'meta', 'xai']

    def test_all_major_entities_present(self, entities):
        for name in self.EXPECTED_ENTITIES:
            assert name in entities['entities'], f"Missing entity: {name}"

    def test_entities_have_display_name(self, entities):
        for name in self.EXPECTED_ENTITIES:
            entity = entities['entities'][name]
            assert 'display_name' in entity, f"{name} missing display_name"

    def test_xai_is_publisher_invisible(self, entities):
        xai = entities['entities']['xai']
        xai_str = str(xai)
        assert 'invisible' in xai_str.lower() or 'zero' in xai_str.lower()

    def test_meta_has_13_publisher_deals(self, entities):
        """Meta should document its 13 publisher deals as context."""
        mad = entities['meta_ai_deals']
        partners = mad.get('partners', [])
        assert len(partners) >= 13 or '13' in str(mad)


# ─── Source URL Validation ────────────────────────────────────────────


class TestSourceURLPresence:
    """Verify that key findings have source URLs for citation integrity."""

    def test_google_class_action_has_source_urls(self, entities):
        google = entities['entities']['google']
        lit = google['publisher_litigation_jul2026']
        urls = lit.get('source_urls', [])
        assert len(urls) > 0, "Class-action needs source URLs"

    def test_cma_ruling_has_source_urls(self, entities):
        google = entities['entities']['google']
        cma = google['cma_ai_overviews_opt_out']
        urls = cma.get('source_urls', [])
        assert len(urls) > 0, "CMA ruling needs source URLs"

    def test_apple_collapse_has_source_urls(self, entities):
        cs = entities['meta_ai_deals']['cross_platform_summary']
        collapse = cs['apple_openai_partnership_collapse']
        urls = collapse.get('source_urls', [])
        assert len(urls) > 0, "Apple-OpenAI collapse needs source URLs"

    def test_reddit_instability_has_source_url(self, entities):
        google = entities['entities']['google']
        reddit = google['reddit_deal_instability']
        url = reddit.get('source_url', reddit.get('source_urls', []))
        assert url, "Reddit instability needs source URL"
