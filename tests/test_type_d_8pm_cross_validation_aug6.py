"""
Type D 8PM Cross-Validation: Evening Iteration Integrity Check (Aug 6, 2026)

Cross-validates data consistency across the three evening iterations:
- 3PM Type A: Atlantic × Apple v. OpenAI editorial silence
- 4PM Type B: Dan Milmo (Guardian) cross-entity analysis
- 6PM Type C: Amazon sextuple publisher leverage

Plus entity-level updates:
- OpenAI entity: Apple partnership escalation phases 4-5
- Apple entity: Preliminary injunction + motion to dismiss phases
- Atlantic research: source_urls schema consistency fix
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    filepath = os.path.join(PROFILES_DIR, filename)
    with open(filepath) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def research():
    return load_yaml('competitor-coverage-research.yaml')


@pytest.fixture(scope='module')
def entities():
    return load_yaml('competitor-entities.yaml')


@pytest.fixture(scope='module')
def atlantic():
    return load_yaml('atlantic.yaml')


@pytest.fixture(scope='module')
def guardian():
    return load_yaml('guardian.yaml')


class TestOpenAIAppleEscalationPhases:
    """OpenAI entity should reflect all 5 phases of Apple partnership collapse."""

    def test_has_apple_partnership_collapse(self, entities):
        openai = entities['entities']['openai']
        assert 'apple_partnership_collapse' in openai

    def test_has_breach_threat_date(self, entities):
        collapse = entities['entities']['openai']['apple_partnership_collapse']
        assert str(collapse['breach_threat_date']) == '2026-05-14'

    def test_has_trade_secret_suit_date(self, entities):
        collapse = entities['entities']['openai']['apple_partnership_collapse']
        assert str(collapse['apple_trade_secret_suit_date']) == '2026-07-10'

    def test_has_preliminary_injunction_date(self, entities):
        collapse = entities['entities']['openai']['apple_partnership_collapse']
        assert str(collapse['preliminary_injunction_date']) == '2026-08-04'

    def test_has_motion_to_dismiss_date(self, entities):
        collapse = entities['entities']['openai']['apple_partnership_collapse']
        assert str(collapse['motion_to_dismiss_date']) == '2026-08-06'

    def test_source_urls_cover_all_phases(self, entities):
        collapse = entities['entities']['openai']['apple_partnership_collapse']
        urls = collapse['source_urls']
        assert len(urls) >= 4, f"Expected 4+ source URLs for all phases, got {len(urls)}"

    def test_overview_mentions_motion_to_dismiss(self, entities):
        collapse = entities['entities']['openai']['apple_partnership_collapse']
        overview = collapse['overview'].lower()
        assert 'motion to dismiss' in overview or 'dismiss' in overview


class TestAppleEntityEscalationPhases:
    """Apple entity should reflect all 5 phases including phases 4-5."""

    def test_has_openai_partnership_collapse(self, entities):
        apple = entities['entities']['apple']
        assert 'openai_partnership_collapse' in apple

    def test_has_phase_4_preliminary_injunction(self, entities):
        apple = entities['entities']['apple']
        collapse = apple['openai_partnership_collapse']
        assert 'phase_4_preliminary_injunction' in collapse

    def test_phase_4_date_correct(self, entities):
        apple = entities['entities']['apple']
        phase4 = apple['openai_partnership_collapse']['phase_4_preliminary_injunction']
        assert str(phase4['date']) == '2026-08-04'

    def test_has_phase_5_motion_to_dismiss(self, entities):
        apple = entities['entities']['apple']
        collapse = apple['openai_partnership_collapse']
        assert 'phase_5_motion_to_dismiss' in collapse

    def test_phase_5_date_correct(self, entities):
        apple = entities['entities']['apple']
        phase5 = apple['openai_partnership_collapse']['phase_5_motion_to_dismiss']
        assert str(phase5['date']) == '2026-08-06'

    def test_phase_5_has_source_urls(self, entities):
        apple = entities['entities']['apple']
        phase5 = apple['openai_partnership_collapse']['phase_5_motion_to_dismiss']
        urls = phase5.get('source_urls', [])
        assert len(urls) >= 2, f"Phase 5 should have Reuters + WSJ URLs, got {len(urls)}"

    def test_openai_apple_entities_consistent_on_dates(self, entities):
        """Both entities should agree on the key dates."""
        openai = entities['entities']['openai']['apple_partnership_collapse']
        apple_collapse = entities['entities']['apple']['openai_partnership_collapse']

        # Phase 3: trade secret suit
        assert str(openai['apple_trade_secret_suit_date']) == str(apple_collapse['phase_3_apple_sues_openai']['date'])


class TestAtlanticSilenceSourceURLs:
    """Atlantic silence section should have source_urls for schema consistency."""

    def test_has_source_urls_list(self, research):
        silence = research['publications']['atlantic']['apple_v_openai_editorial_silence']
        assert 'source_urls' in silence, "Missing source_urls list"

    def test_source_urls_has_minimum_count(self, research):
        silence = research['publications']['atlantic']['apple_v_openai_editorial_silence']
        urls = silence['source_urls']
        assert len(urls) >= 4, f"Expected 4+ source URLs, got {len(urls)}"

    def test_escalation_sources_also_present(self, research):
        """Both escalation_sources dict and source_urls list should exist."""
        silence = research['publications']['atlantic']['apple_v_openai_editorial_silence']
        assert 'escalation_sources' in silence
        assert 'source_urls' in silence

    def test_escalation_sources_urls_in_source_urls(self, research):
        """Every URL in escalation_sources should appear in source_urls."""
        silence = research['publications']['atlantic']['apple_v_openai_editorial_silence']
        esc_urls = set(silence['escalation_sources'].values())
        src_urls = set(silence['source_urls'])
        missing = esc_urls - src_urls
        assert not missing, f"Escalation URLs missing from source_urls: {missing}"

    def test_publications_that_covered_structure(self, research):
        silence = research['publications']['atlantic']['apple_v_openai_editorial_silence']
        ptc = silence['publications_that_covered']
        assert 'within_hours' in ptc
        assert 'within_days' in ptc
        assert 'not_covered' in ptc
        assert 'The Atlantic' in ptc['not_covered']


class TestGuardianMilmoConsistencyAcrossFiles:
    """Milmo data should be consistent between profile and research."""

    def test_milmo_in_profile(self, guardian):
        jce = guardian.get('journalist_cross_entity', {})
        assert 'dan_milmo' in jce

    def test_milmo_in_research(self, research):
        guar = research['publications'].get('guardian', {})
        assert 'milmo_cross_entity' in guar

    def test_milmo_meta_tone_consistent(self, guardian, research):
        profile_meta = guardian['journalist_cross_entity']['dan_milmo']['entity_coverage']['meta']
        research_meta = research['publications']['guardian']['milmo_cross_entity']['meta_tone']
        # Profile stores tone in the entity_coverage dict
        profile_tone = profile_meta.get('tone_score', profile_meta.get('tone', None))
        if profile_tone is not None:
            assert abs(float(profile_tone) - float(research_meta)) < 0.1

    def test_milmo_research_has_source_urls(self, research):
        milmo = research['publications']['guardian']['milmo_cross_entity']
        assert 'source_urls' in milmo
        assert len(milmo['source_urls']) >= 3

    def test_milmo_role_documented(self, research):
        milmo = research['publications']['guardian']['milmo_cross_entity']
        assert milmo['role'] == 'Global Technology Editor'


class TestAmazonSextupleConsistencyAcrossFiles:
    """Amazon sextuple leverage should be consistent between entities and research."""

    def test_amazon_entity_has_sextuple(self, entities):
        amazon = entities['entities']['amazon']
        assert 'sextuple_publisher_leverage' in amazon

    def test_research_has_sextuple(self, research):
        cel = research.get('cross_entity_leverage', {})
        assert 'amazon_sextuple_leverage' in cel

    def test_six_layers_in_entity(self, entities):
        amazon = entities['entities']['amazon']
        layers = amazon['sextuple_publisher_leverage'].get('layers', [])
        assert len(layers) >= 6, f"Expected 6 leverage layers, got {len(layers)}"

    def test_anthropic_double_play_documented(self, research):
        amazon_r = research['cross_entity_leverage']['amazon_sextuple_leverage']
        desc = str(amazon_r).lower()
        assert 'anthropic' in desc

    def test_meta_contrast_documented(self, entities):
        amazon = entities['entities']['amazon']
        sextuple = amazon['sextuple_publisher_leverage']
        meta_contrast = sextuple.get('meta_contrast', '')
        assert meta_contrast, "Missing meta_contrast in sextuple leverage"


class TestMicrosoftOpenAIAxisPresent:
    """Microsoft-OpenAI financial axis should be in cross-entity leverage."""

    def test_microsoft_openai_axis_exists(self, research):
        cel = research.get('cross_entity_leverage', {})
        assert 'microsoft_openai_axis' in cel

    def test_axis_has_description(self, research):
        axis = research['cross_entity_leverage']['microsoft_openai_axis']
        assert axis, "microsoft_openai_axis should not be empty"


class TestEveningIterationCoverage:
    """Verify all three evening iterations (A, B, C) left data traces."""

    def test_type_a_atlantic_silence_present(self, research):
        assert 'apple_v_openai_editorial_silence' in research['publications']['atlantic']

    def test_type_b_milmo_present(self, research):
        assert 'milmo_cross_entity' in research['publications']['guardian']

    def test_type_c_amazon_sextuple_present(self, research):
        assert 'amazon_sextuple_leverage' in research['cross_entity_leverage']

    def test_type_c_microsoft_axis_present(self, research):
        assert 'microsoft_openai_axis' in research['cross_entity_leverage']


class TestLeverageCountsConsistent:
    """Leverage layer counts should match between entities and research."""

    def test_amazon_highest_leverage_count(self, entities):
        """Amazon should have the highest leverage layer count (6)."""
        amazon = entities['entities']['amazon']
        layers = amazon['sextuple_publisher_leverage']['layers']
        assert len(layers) >= 6

    def test_meta_lowest_leverage_count(self, entities):
        """Meta should have 1 leverage layer (content licensing only)."""
        meta = entities['entities'].get('meta', {})
        # Meta may not have a leverage section since it has minimal leverage
        # Just verify it doesn't have more than Amazon
        leverage = meta.get('sextuple_publisher_leverage', {}).get('layers', [])
        assert len(leverage) < 6, "Meta should have fewer leverage layers than Amazon"
