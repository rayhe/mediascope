"""
Tests for WIRED's Apple wearables lane assignment analysis.

Validates the structural finding that WIRED assigns its senior consumer tech
correspondent (Lauren Goode) to review Apple and Snap wearables with empathetic/
playful framing, while Meta wearables are assigned to investigative reporters
(Dell Cameron, Dhruv Mehrotra) who produce surveillance-alarm framing.

Key paradox: Apple Vision Pro has 12 cameras, 5 sensors, 6 microphones (the most
surveillance-capable consumer wearable ever sold) yet receives ZERO surveillance
framing — while Meta Ray-Ban with a single 12MP camera receives sustained
investigative surveillance framing.
"""

import yaml
import pytest
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


@pytest.fixture
def wired_profile():
    with open(os.path.join(PROFILES_DIR, 'wired.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture
def competitor_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)


class TestWiredCrossEntityFramingExists:
    """Verify the cross-entity wearables framing section exists with required structure."""

    def test_cross_entity_section_exists(self, wired_profile):
        assert 'cross_entity_wearables_framing' in wired_profile

    def test_evidence_section_has_three_entities(self, wired_profile):
        evidence = wired_profile['cross_entity_wearables_framing']['evidence']
        assert 'apple_vision_pro' in evidence
        assert 'snap_spectacles' in evidence
        assert 'meta_glasses' in evidence

    def test_date_analyzed_is_current(self, wired_profile):
        date = wired_profile['cross_entity_wearables_framing']['date_analyzed']
        assert date.startswith('2026-08'), f"Analysis date should be Aug 2026: {date}"

    def test_analytical_significance_documented(self, wired_profile):
        sig = wired_profile['cross_entity_wearables_framing'].get('analytical_significance', '')
        assert len(sig) > 100, "Analytical significance should be substantive"


class TestAppleVisionProFraming:
    """Apple Vision Pro: 12 cameras, empathetic framing, ZERO surveillance."""

    def test_apple_reviewer_is_goode(self, wired_profile):
        avp = wired_profile['cross_entity_wearables_framing']['evidence']['apple_vision_pro']
        assert 'Lauren Goode' in avp['reviewer']

    def test_apple_tone_is_positive(self, wired_profile):
        avp = wired_profile['cross_entity_wearables_framing']['evidence']['apple_vision_pro']
        assert avp['tone'] in ('empathetic wonder', 'positive', 'neutral_to_positive')

    def test_apple_no_privacy_concerns_raised(self, wired_profile):
        avp = wired_profile['cross_entity_wearables_framing']['evidence']['apple_vision_pro']
        assert avp['privacy_concerns_raised'] is False

    def test_apple_no_surveillance_framing(self, wired_profile):
        avp = wired_profile['cross_entity_wearables_framing']['evidence']['apple_vision_pro']
        assert avp['camera_surveillance_framing'] is False

    def test_apple_has_source_urls(self, wired_profile):
        avp = wired_profile['cross_entity_wearables_framing']['evidence']['apple_vision_pro']
        urls = avp.get('source_urls', [])
        assert len(urls) > 0, "Apple Vision Pro evidence must have source URLs"

    def test_apple_framing_mentions_crying(self, wired_profile):
        avp = wired_profile['cross_entity_wearables_framing']['evidence']['apple_vision_pro']
        framing = avp.get('framing_language', '')
        assert 'cried' in framing.lower(), "Apple review 'I cried' quote should be documented"

    def test_apple_hardware_specs_documented(self, wired_profile):
        avp = wired_profile['cross_entity_wearables_framing']['evidence']['apple_vision_pro']
        specs = avp.get('hardware_specs', '')
        assert '12' in specs, "Should document Apple Vision Pro's 12 cameras"

    def test_apple_has_podcast_source(self, wired_profile):
        avp = wired_profile['cross_entity_wearables_framing']['evidence']['apple_vision_pro']
        assert 'podcast_source_url' in avp or 'wired_podcast' in avp


class TestSnapSpectaclesFraming:
    """Snap Spectacles: 1 camera, playful framing, ZERO surveillance."""

    def test_snap_reviewer_is_goode(self, wired_profile):
        snap = wired_profile['cross_entity_wearables_framing']['evidence']['snap_spectacles']
        assert 'Lauren Goode' in snap['reviewer']

    def test_snap_tone_is_positive(self, wired_profile):
        snap = wired_profile['cross_entity_wearables_framing']['evidence']['snap_spectacles']
        assert snap['tone'] in ('playful positive', 'positive', 'neutral_to_positive')

    def test_snap_no_privacy_concerns(self, wired_profile):
        snap = wired_profile['cross_entity_wearables_framing']['evidence']['snap_spectacles']
        assert snap['privacy_concerns_raised'] is False

    def test_snap_no_surveillance_framing(self, wired_profile):
        snap = wired_profile['cross_entity_wearables_framing']['evidence']['snap_spectacles']
        assert snap['camera_surveillance_framing'] is False

    def test_snap_has_source_url(self, wired_profile):
        snap = wired_profile['cross_entity_wearables_framing']['evidence']['snap_spectacles']
        url = snap.get('source_url', '')
        assert 'youtube.com' in url, "Snap Spectacles source should be YouTube video"

    def test_snap_face_camera_title(self, wired_profile):
        """The title 'Face Camera We've Been Waiting For' frames face cameras positively."""
        snap = wired_profile['cross_entity_wearables_framing']['evidence']['snap_spectacles']
        framing = snap.get('framing_language', '')
        assert 'Face Camera' in framing, "Should document the positive 'Face Camera' framing"


class TestMetaGlassesFraming:
    """Meta glasses: 1 camera, surveillance framing, NOT Lauren Goode."""

    def test_meta_reviewer_is_not_goode(self, wired_profile):
        meta = wired_profile['cross_entity_wearables_framing']['evidence']['meta_glasses']
        reviewer = meta['reviewer']
        # Goode should NOT be the reviewer
        assert 'Lauren Goode' not in reviewer or 'NOT' in reviewer

    def test_meta_reviewer_is_investigative(self, wired_profile):
        meta = wired_profile['cross_entity_wearables_framing']['evidence']['meta_glasses']
        reviewer = meta['reviewer']
        investigative_names = ['Dell Cameron', 'Dhruv Mehrotra', 'investigative']
        assert any(name in reviewer for name in investigative_names)

    def test_meta_tone_is_adversarial(self, wired_profile):
        meta = wired_profile['cross_entity_wearables_framing']['evidence']['meta_glasses']
        assert 'surveillance' in meta['tone'].lower() or 'alarm' in meta['tone'].lower()

    def test_meta_privacy_concerns_raised(self, wired_profile):
        meta = wired_profile['cross_entity_wearables_framing']['evidence']['meta_glasses']
        assert meta['privacy_concerns_raised'] is True

    def test_meta_surveillance_framing_present(self, wired_profile):
        meta = wired_profile['cross_entity_wearables_framing']['evidence']['meta_glasses']
        assert meta['camera_surveillance_framing'] is True

    def test_meta_has_key_articles(self, wired_profile):
        meta = wired_profile['cross_entity_wearables_framing']['evidence']['meta_glasses']
        articles = meta.get('key_articles', [])
        assert len(articles) >= 2, "Should document at least 2 Meta glasses articles"

    def test_meta_nametag_investigation_documented(self, wired_profile):
        meta = wired_profile['cross_entity_wearables_framing']['evidence']['meta_glasses']
        articles = meta.get('key_articles', [])
        nametag_articles = [a for a in articles if 'NameTag' in a.get('title', '') or 'Name Tag' in a.get('title', '')]
        assert len(nametag_articles) >= 1, "NameTag investigation should be documented"

    def test_meta_hardware_specs_documented(self, wired_profile):
        meta = wired_profile['cross_entity_wearables_framing']['evidence']['meta_glasses']
        specs = meta.get('hardware_specs', '')
        assert '12MP' in specs or 'single' in specs.lower() or '1' in specs


class TestCameraCountParadox:
    """The camera count paradox: more cameras = less surveillance framing."""

    def test_camera_count_paradox_documented(self, wired_profile):
        cef = wired_profile['cross_entity_wearables_framing']
        paradox = cef.get('camera_count_paradox', '')
        assert len(paradox) > 100, "Camera count paradox should be substantively documented"

    def test_paradox_mentions_twelve_vs_one(self, wired_profile):
        cef = wired_profile['cross_entity_wearables_framing']
        paradox = cef.get('camera_count_paradox', '')
        assert '12' in paradox or 'twelve' in paradox.lower()
        assert 'ONE' in paradox or 'one camera' in paradox.lower() or '1-camera' in paradox

    def test_paradox_identifies_manufacturer_identity(self, wired_profile):
        """The variable is manufacturer identity, not hardware capability."""
        cef = wired_profile['cross_entity_wearables_framing']
        paradox = cef.get('camera_count_paradox', '')
        assert 'manufacturer' in paradox.lower() or 'identity' in paradox.lower()


class TestFinancialAlignment:
    """Lane assignments align with financial incentive predictions."""

    def test_financial_alignment_documented(self, wired_profile):
        cef = wired_profile['cross_entity_wearables_framing']
        alignment = cef.get('financial_alignment', '')
        assert len(alignment) > 50, "Financial alignment should be documented"

    def test_financial_alignment_mentions_apple_deal(self, wired_profile):
        cef = wired_profile['cross_entity_wearables_framing']
        alignment = cef.get('financial_alignment', '')
        assert 'Apple' in alignment and ('licensing' in alignment.lower() or 'negotiat' in alignment.lower())

    def test_financial_alignment_mentions_no_meta_deal(self, wired_profile):
        cef = wired_profile['cross_entity_wearables_framing']
        alignment = cef.get('financial_alignment', '')
        assert 'Meta' in alignment and 'no' in alignment.lower()


class TestCompetitorResearchAppleExamples:
    """Competitor coverage research file has Apple wearables examples."""

    def test_apple_has_examples(self, competitor_research):
        wired = competitor_research['publications']['wired']
        examples = wired.get('apple_examples', [])
        assert len(examples) >= 3, f"Should have at least 3 Apple examples, got {len(examples)}"

    def test_apple_examples_have_source_urls(self, competitor_research):
        wired = competitor_research['publications']['wired']
        examples = wired.get('apple_examples', [])
        for ex in examples:
            url = ex.get('source_url', '') or ''
            urls = ex.get('source_urls', []) or []
            assert url or urls, f"Example '{ex.get('title', '?')}' must have source URL(s)"

    def test_apple_vision_pro_review_documented(self, competitor_research):
        wired = competitor_research['publications']['wired']
        examples = wired.get('apple_examples', [])
        avp_examples = [e for e in examples if 'Vision Pro' in e.get('title', '') or 'cried' in e.get('title', '').lower()]
        assert len(avp_examples) >= 1, "Apple Vision Pro 'I cried' review should be documented"

    def test_apple_tones_are_positive(self, competitor_research):
        wired = competitor_research['publications']['wired']
        examples = wired.get('apple_examples', [])
        for ex in examples:
            assert ex.get('tone', 0) > 0, f"Apple example '{ex.get('title', '?')}' should have positive tone"

    def test_apple_coverage_summary_mentions_lane_assignment(self, competitor_research):
        wired = competitor_research['publications']['wired']
        summary = wired.get('apple_coverage_summary', '')
        assert 'lane' in summary.lower() or 'Goode' in summary, \
            "Apple coverage summary should mention the lane assignment or Goode"

    def test_snap_spectacles_example_documented(self, competitor_research):
        wired = competitor_research['publications']['wired']
        examples = wired.get('apple_examples', [])
        snap_examples = [e for e in examples if 'Snap' in e.get('title', '') or 'Spectacles' in e.get('title', '')]
        assert len(snap_examples) >= 1, "Snap Spectacles positive framing should be documented as contrast"


class TestEditorialLaneMechanism:
    """The editorial lane mechanism should be documented as structural, not conspiratorial."""

    def test_lane_mechanism_documented(self, wired_profile):
        cef = wired_profile['cross_entity_wearables_framing']
        mechanism = cef.get('editorial_lane_assignment_mechanism', '')
        assert len(mechanism) > 100

    def test_mechanism_identifies_three_steps(self, wired_profile):
        cef = wired_profile['cross_entity_wearables_framing']
        mechanism = cef.get('editorial_lane_assignment_mechanism', '')
        # Should describe the structural steps, not allege conspiracy
        assert 'assignment' in mechanism.lower()
        assert 'Drummond' in mechanism or 'editorial' in mechanism.lower()

    def test_mechanism_is_structural_not_conspiratorial(self, wired_profile):
        """The mechanism should be described as structural, not requiring conscious bias."""
        cef = wired_profile['cross_entity_wearables_framing']
        mechanism = cef.get('editorial_lane_assignment_mechanism', '')
        assert "doesn't require conscious" in mechanism.lower() or \
               "doesn't require" in mechanism.lower() or \
               'structural' in mechanism.lower()
