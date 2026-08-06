"""
MIT Technology Review × Apple — Governance-Level Conflict Analysis
Type A deep dive, Aug 6 2026

Tests verifying the Apple-MIT governance conflict findings:
(1) Kate Bergeron (Apple VP Hardware Eng) elected MIT Corporation term member Jul 1 2026
(2) Apple is a CSAIL Alliance member
(3) MIT TR's Apple coverage is privacy-positive while Meta coverage is adversarial
(4) Sensor-count paradox extends to MIT TR (third publication after WIRED and FT)
(5) Three-tier influence hierarchy: governance > research funding > no relationship
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def research():
    return load_yaml('competitor-coverage-research.yaml')


@pytest.fixture(scope='module')
def mit_profile():
    return load_yaml('mit-tech-review.yaml')


@pytest.fixture(scope='module')
def entities():
    return load_yaml('competitor-entities.yaml')


@pytest.fixture(scope='module')
def mit_tr_section(research):
    return research['publications']['mit-tech-review']


# ===================================================================
# 1. KATE BERGERON — MIT CORPORATION GOVERNANCE CONFLICT
# ===================================================================

class TestBergeronGovernanceConflict:
    """Verify the Kate Bergeron MIT Corporation finding is documented."""

    def test_bergeron_election_documented(self, mit_tr_section):
        gov = mit_tr_section['apple_governance_conflict']['bergeron_election']
        assert gov is not None

    def test_bergeron_effective_date(self, mit_tr_section):
        gov = mit_tr_section['apple_governance_conflict']['bergeron_election']
        assert gov['effective_date'] == '2026-07-01'

    def test_bergeron_apple_title(self, mit_tr_section):
        gov = mit_tr_section['apple_governance_conflict']['bergeron_election']
        assert 'Vice President' in gov['title_at_apple']
        assert 'Hardware Engineering' in gov['title_at_apple']

    def test_bergeron_mit_degrees(self, mit_tr_section):
        gov = mit_tr_section['apple_governance_conflict']['bergeron_election']
        assert '1993' in gov['mit_degrees']
        assert 'Sloan' in gov['mit_degrees'] or 'MBA' in gov['mit_degrees']

    def test_bergeron_source_url(self, mit_tr_section):
        gov = mit_tr_section['apple_governance_conflict']['bergeron_election']
        assert 'news.mit.edu' in gov['source_url']
        assert '2026' in gov['source_url']

    def test_bergeron_position_is_term_member(self, mit_tr_section):
        gov = mit_tr_section['apple_governance_conflict']['bergeron_election']
        assert 'term member' in gov['position'].lower()

    def test_bergeron_wearables_relevance_documented(self, mit_tr_section):
        gov = mit_tr_section['apple_governance_conflict']['bergeron_election']
        assert 'wearables_relevance' in gov
        # Should mention Apple's smart glasses or Vision Products Group
        text = gov['wearables_relevance'].lower()
        assert 'glasses' in text or 'vision' in text or 'wearable' in text

    def test_bergeron_apple_tenure(self, mit_tr_section):
        gov = mit_tr_section['apple_governance_conflict']['bergeron_election']
        assert '2002' in gov['apple_tenure']


# ===================================================================
# 2. CSAIL ALLIANCE MEMBERSHIP
# ===================================================================

class TestCSAILAlliance:
    """Verify Apple's CSAIL Alliance membership is documented."""

    def test_csail_alliance_status(self, mit_tr_section):
        csail = mit_tr_section['apple_governance_conflict']['csail_alliance']
        assert csail['status'].lower() in ('active member', 'active')

    def test_csail_alliance_source(self, mit_tr_section):
        csail = mit_tr_section['apple_governance_conflict']['csail_alliance']
        assert 'csail.mit.edu' in csail['source_url']

    def test_csail_alliance_confirmation(self, mit_tr_section):
        csail = mit_tr_section['apple_governance_conflict']['csail_alliance']
        assert 'apple' in csail['confirmation'].lower()


# ===================================================================
# 3. APPLE COVERAGE TONE AND EXAMPLES
# ===================================================================

class TestAppleCoverageTone:
    """Verify Apple coverage framing analysis."""

    def test_apple_tone_positive(self, mit_tr_section):
        assert mit_tr_section['apple_coverage_tone'] == 'positive'

    def test_apple_examples_exist(self, mit_tr_section):
        assert len(mit_tr_section['apple_examples']) >= 2

    def test_apple_intelligence_article_documented(self, mit_tr_section):
        titles = [e['title'] for e in mit_tr_section['apple_examples']]
        ai_articles = [t for t in titles if 'apple' in t.lower() and ('intelligence' in t.lower() or 'ai' in t.lower() or 'private cloud' in t.lower())]
        assert len(ai_articles) >= 1, "Apple Intelligence article should be documented"

    def test_apple_intelligence_positive_tone(self, mit_tr_section):
        for ex in mit_tr_section['apple_examples']:
            if 'private cloud' in ex['title'].lower() or 'intelligence' in ex['title'].lower():
                assert ex['tone'] > 0, "Apple Intelligence article should have positive tone"

    def test_apple_intelligence_has_source_url(self, mit_tr_section):
        for ex in mit_tr_section['apple_examples']:
            if 'private cloud' in ex['title'].lower():
                assert 'technologyreview.com' in ex['source_url']

    def test_meta_named_unfavorably_in_apple_article(self, mit_tr_section):
        """Apple Intelligence article explicitly contrasts Apple with Meta negatively."""
        for ex in mit_tr_section['apple_examples']:
            if 'private cloud' in ex['title'].lower():
                notes = ex.get('notes', '')
                assert 'meta' in notes.lower(), "Notes should reference Meta comparison"


# ===================================================================
# 4. META COVERAGE TONE AND EXAMPLES
# ===================================================================

class TestMetaCoverageTone:
    """Verify Meta coverage framing analysis."""

    def test_meta_tone_adversarial(self, mit_tr_section):
        assert mit_tr_section['meta_coverage_tone'] == 'adversarial'

    def test_meta_examples_exist(self, mit_tr_section):
        assert len(mit_tr_section['meta_examples']) >= 2

    def test_warfare_article_documented(self, mit_tr_section):
        titles = [e['title'].lower() for e in mit_tr_section['meta_examples']]
        warfare = [t for t in titles if 'warfare' in t or 'anduril' in t]
        assert len(warfare) >= 1, "Anduril/warfare article should be documented"

    def test_stake_a_claim_article_documented(self, mit_tr_section):
        titles = [e['title'].lower() for e in mit_tr_section['meta_examples']]
        face_claim = [t for t in titles if 'faces' in t or 'face' in t or 'stake' in t]
        assert len(face_claim) >= 1, "Ray-Ban faces article should be documented"

    def test_meta_examples_have_negative_tone(self, mit_tr_section):
        """At least one Meta example should have adversarial tone."""
        tones = [e['tone'] for e in mit_tr_section['meta_examples']]
        assert min(tones) <= -0.40, f"Expected at least one Meta tone <= -0.40, got {min(tones)}"

    def test_meta_examples_have_source_urls(self, mit_tr_section):
        for ex in mit_tr_section['meta_examples']:
            assert 'source_url' in ex, f"Meta example '{ex['title']}' missing source_url"


# ===================================================================
# 5. SENSOR-COUNT PARADOX
# ===================================================================

class TestSensorCountParadox:
    """Verify the MIT TR sensor-count paradox is documented."""

    def test_sensor_paradox_exists(self, mit_tr_section):
        assert 'sensor_count_paradox' in mit_tr_section

    def test_sensor_paradox_mentions_apple_vision_pro(self, mit_tr_section):
        text = mit_tr_section['sensor_count_paradox'].lower()
        assert 'apple vision pro' in text or 'vision pro' in text

    def test_sensor_paradox_mentions_meta_glasses(self, mit_tr_section):
        text = mit_tr_section['sensor_count_paradox'].lower()
        assert 'meta' in text and ('ray-ban' in text or 'glasses' in text)

    def test_sensor_paradox_mentions_camera_counts(self, mit_tr_section):
        text = mit_tr_section['sensor_count_paradox']
        assert '12 camera' in text.lower() or '12 cameras' in text.lower()
        assert '1 camera' in text.lower()

    def test_sensor_paradox_cross_references_wired_ft(self, mit_tr_section):
        """Should reference WIRED and FT as other publications showing same pattern."""
        text = mit_tr_section['sensor_count_paradox'].lower()
        assert 'wired' in text
        assert 'ft' in text or 'financial times' in text

    def test_sensor_paradox_mentions_governance_dimension(self, mit_tr_section):
        """MIT TR's paradox has a governance angle that WIRED/FT don't."""
        text = mit_tr_section['sensor_count_paradox'].lower()
        assert 'governance' in text or 'board' in text or 'fiduciary' in text


# ===================================================================
# 6. NON-DISCLOSURE
# ===================================================================

class TestNonDisclosure:
    """Verify non-disclosure documentation."""

    def test_non_disclosure_documented(self, mit_tr_section):
        gov = mit_tr_section['apple_governance_conflict']
        assert 'non_disclosure' in gov

    def test_non_disclosure_mentions_bergeron(self, mit_tr_section):
        text = mit_tr_section['apple_governance_conflict']['non_disclosure'].lower()
        assert 'bergeron' in text

    def test_non_disclosure_mentions_csail(self, mit_tr_section):
        text = mit_tr_section['apple_governance_conflict']['non_disclosure'].lower()
        assert 'csail' in text


# ===================================================================
# 7. THREE-TIER INFLUENCE HIERARCHY
# ===================================================================

class TestThreeTierHierarchy:
    """Verify the governance > research > none influence hierarchy."""

    def test_verdict_mentions_three_tiers(self, mit_tr_section):
        text = mit_tr_section['asymmetry_verdict'].lower()
        assert 'tier 1' in text or 'tier' in text

    def test_apple_governance_tier_highest(self, mit_tr_section):
        text = mit_tr_section['asymmetry_verdict'].lower()
        # Apple with governance link should be the most favorable
        assert 'governance' in text
        assert 'apple' in text

    def test_meta_no_relationship_tier_lowest(self, mit_tr_section):
        text = mit_tr_section['asymmetry_verdict'].lower()
        assert 'no relationship' in text or 'zero' in text

    def test_google_amazon_middle_tier(self, mit_tr_section):
        text = mit_tr_section['asymmetry_verdict'].lower()
        assert 'research' in text and ('funding' in text or 'partnership' in text)

    def test_tone_ordering_correct(self, mit_tr_section):
        """Apple tone > Google tone > Meta tone."""
        apple_tone = mit_tr_section['apple_coverage_tone']
        google_tone = mit_tr_section['google_coverage_tone']
        meta_tone = mit_tr_section['meta_coverage_tone']
        tone_order = {'positive': 3, 'neutral_to_positive': 2, 'balanced': 1, 'adversarial': 0, 'balanced_adversarial': 0.5}
        assert tone_order.get(apple_tone, 0) > tone_order.get(google_tone, 0) > tone_order.get(meta_tone, 0)


# ===================================================================
# 8. CROSS-VALIDATION WITH MIT PROFILE
# ===================================================================

class TestMITProfileCrossValidation:
    """Cross-validate with mit-tech-review.yaml profile data."""

    def test_mit_profile_has_bergeron_in_board_or_governance(self, mit_profile):
        """MIT profile's governance/board section or corporate partnerships
        should reference the Apple-MIT relationship."""
        # Check if Apple appears anywhere in the profile
        text = yaml.dump(mit_profile).lower()
        assert 'apple' in text, "MIT profile should mention Apple somewhere"

    def test_mit_profile_has_csail(self, mit_profile):
        """MIT profile should mention CSAIL."""
        text = yaml.dump(mit_profile).lower()
        assert 'csail' in text

    def test_mit_profile_corporate_partnerships_exist(self, mit_profile):
        """MIT profile should document corporate research partnerships."""
        assert 'mit_corporate_research_partnerships' in mit_profile or \
               'corporate_structure' in mit_profile


# ===================================================================
# 9. STATISTICAL DIRECTION
# ===================================================================

class TestStatisticalDirection:
    """Verify the statistical direction is consistent across MIT TR findings."""

    def test_deal_holder_positive(self, mit_tr_section):
        """Apple (governance + CSAIL) gets positive coverage."""
        assert mit_tr_section['apple_coverage_tone'] == 'positive'

    def test_research_partners_neutral_to_positive(self, mit_tr_section):
        """Google and Amazon (research partners) get neutral-to-positive."""
        assert mit_tr_section['google_coverage_tone'] == 'neutral_to_positive'
        assert mit_tr_section['amazon_coverage_tone'] == 'neutral_to_positive'

    def test_no_relationship_adversarial(self, mit_tr_section):
        """Meta (no institutional tie) gets adversarial coverage."""
        assert mit_tr_section['meta_coverage_tone'] == 'adversarial'

    def test_openai_balanced(self, mit_tr_section):
        """OpenAI (ProRata partner, not research partner) gets balanced."""
        assert mit_tr_section['openai_coverage_tone'] == 'balanced'
