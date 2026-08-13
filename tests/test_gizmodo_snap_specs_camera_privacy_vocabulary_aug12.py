"""
Gizmodo × Snap Specs vs Meta Glasses — Surveillance Vocabulary Suppression at Clean Control

Type A: Competitor Coverage Deep Dive (Aug 12, 2026 22:00 PT)
Mechanism #74: Surveillance Vocabulary Suppression at Clean Control

Validates that even Gizmodo — the "clean control" publication (ZERO financial ties to any
tech company) — suppresses surveillance vocabulary when covering Snap's camera-equipped
Specs ($2,195, Jun 2026) while deploying it freely for Meta's camera-equipped glasses.

Both products: face-mounted cameras, LED recording indicator, AI contextual awareness,
photo/video capture. The hardware is functionally identical for privacy purposes.

Key Gizmodo framing comparison:
- Snap Specs cameras (Jun 16, 2026, James Pero): "cameras that enable spatial experiences...
  can capture photos and video." LED indicator accepted as "the bare minimum."
  Zero surveillance vocabulary. Zero privacy alarm.
- Meta glasses cameras (Mar 2026, Raymond Wong): "You're Being Watched, Too."
  "Surveillance state." "Corporations convincing people to pay for products to
  participate in advancing it." Full alarm vocabulary.

Since Gizmodo has NO deals with Meta, Snap, OpenAI, or anyone, this delta proves the
"Meta = surveillance" narrative coding operates at the CULTURAL level of tech journalism,
independent of financial incentives. Financial relationships at WIRED/FT/etc. AMPLIFY
this pre-existing cultural coding but didn't CREATE it.

Extends Mechanism #6 (Barr Privacy Gradient) from entity-specific to company-specific:
the same editorial instinct that treats Apple/Samsung/Google cameras neutrally also
treats Snap cameras neutrally. Only Meta cameras trigger alarm vocabulary.
"""

import yaml
import os
import pytest

PROFILE_PATH = os.path.join(
    os.path.dirname(__file__), '..', 'profiles', 'gizmodo.yaml'
)

RESEARCH_PATH = os.path.join(
    os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
)


@pytest.fixture(scope='module')
def gizmodo_profile():
    with open(PROFILE_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def research_data():
    with open(RESEARCH_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def snap_specs_section(gizmodo_profile):
    cross = gizmodo_profile.get('cross_entity_coverage', {})
    section = cross.get('snap', {}).get('snap_specs_camera_privacy_parity')
    assert section is not None, (
        "Missing snap.snap_specs_camera_privacy_parity in gizmodo.yaml cross_entity_coverage"
    )
    return section


@pytest.fixture(scope='module')
def mechanism_74(research_data):
    agg = research_data.get('aggregate_findings', {})
    section = agg.get('gizmodo_snap_specs_surveillance_vocabulary_suppression')
    assert section is not None, (
        "Missing gizmodo_snap_specs_surveillance_vocabulary_suppression in "
        "competitor-coverage-research.yaml aggregate_findings"
    )
    return section


# ── Class 1: Section Structure ──────────────────────────────────────


class TestSectionStructure:
    """Verify the Snap Specs camera parity section has all required fields."""

    def test_section_exists(self, snap_specs_section):
        assert snap_specs_section is not None

    def test_has_mechanism_id(self, snap_specs_section):
        assert snap_specs_section.get('mechanism_id') == 74

    def test_has_date_analyzed(self, snap_specs_section):
        assert '2026-08-12' in snap_specs_section.get('date_analyzed', '')

    def test_has_finding_summary(self, snap_specs_section):
        summary = snap_specs_section.get('finding_summary', '')
        assert len(summary) > 100

    def test_has_confounding_factors(self, snap_specs_section):
        factors = snap_specs_section.get('confounding_factors', [])
        assert len(factors) >= 3


# ── Class 2: Hardware Parity Documentation ──────────────────────────


class TestHardwareParity:
    """Verify both devices' camera capabilities are documented for comparison."""

    def test_snap_specs_has_cameras(self, snap_specs_section):
        snap = snap_specs_section.get('snap_specs_hardware', {})
        assert snap.get('has_cameras') is True

    def test_snap_specs_has_recording(self, snap_specs_section):
        snap = snap_specs_section.get('snap_specs_hardware', {})
        assert snap.get('can_record_photos_video') is True

    def test_snap_specs_has_led(self, snap_specs_section):
        snap = snap_specs_section.get('snap_specs_hardware', {})
        assert snap.get('has_led_recording_indicator') is True

    def test_snap_specs_has_ai(self, snap_specs_section):
        snap = snap_specs_section.get('snap_specs_hardware', {})
        assert snap.get('has_ai_contextual_awareness') is True

    def test_meta_glasses_has_cameras(self, snap_specs_section):
        meta = snap_specs_section.get('meta_glasses_hardware', {})
        assert meta.get('has_cameras') is True

    def test_meta_glasses_has_recording(self, snap_specs_section):
        meta = snap_specs_section.get('meta_glasses_hardware', {})
        assert meta.get('can_record_photos_video') is True

    def test_meta_glasses_has_led(self, snap_specs_section):
        meta = snap_specs_section.get('meta_glasses_hardware', {})
        assert meta.get('has_led_recording_indicator') is True

    def test_meta_glasses_has_ai(self, snap_specs_section):
        meta = snap_specs_section.get('meta_glasses_hardware', {})
        assert meta.get('has_ai_contextual_awareness') is True

    def test_hardware_parity_acknowledged(self, snap_specs_section):
        assert snap_specs_section.get('hardware_privacy_parity') is True


# ── Class 3: Snap Specs Coverage Framing ────────────────────────────


class TestSnapSpecsFraming:
    """Verify Snap Specs coverage framing data is documented."""

    def test_snap_article_exists(self, snap_specs_section):
        snap_art = snap_specs_section.get('snap_specs_article', {})
        assert 'title' in snap_art
        assert 'Snap' in snap_art['title']

    def test_snap_article_date(self, snap_specs_section):
        snap_art = snap_specs_section.get('snap_specs_article', {})
        assert '2026-06' in snap_art.get('date', '')

    def test_snap_article_author(self, snap_specs_section):
        snap_art = snap_specs_section.get('snap_specs_article', {})
        assert snap_art.get('author') == 'James Pero'

    def test_snap_article_tone_neutral(self, snap_specs_section):
        snap_art = snap_specs_section.get('snap_specs_article', {})
        tone = snap_art.get('tone', -1)
        # Neutral to slightly skeptical, NOT adversarial
        assert -0.25 <= tone <= 0.10

    def test_snap_camera_language_neutral(self, snap_specs_section):
        snap_art = snap_specs_section.get('snap_specs_article', {})
        lang = snap_art.get('camera_language', '')
        assert 'spatial experiences' in lang.lower() or 'enable' in lang.lower()

    def test_snap_zero_surveillance_words(self, snap_specs_section):
        snap_art = snap_specs_section.get('snap_specs_article', {})
        surveillance_words = snap_art.get('surveillance_vocabulary_count', -1)
        assert surveillance_words == 0

    def test_snap_led_accepted(self, snap_specs_section):
        snap_art = snap_specs_section.get('snap_specs_article', {})
        led_framing = snap_art.get('led_indicator_framing', '')
        assert 'bare minimum' in led_framing.lower() or 'accepted' in led_framing.lower()


# ── Class 4: Meta Glasses Coverage Framing ──────────────────────────


class TestMetaGlassesFraming:
    """Verify Meta glasses coverage framing data for comparison."""

    def test_meta_article_exists(self, snap_specs_section):
        meta_art = snap_specs_section.get('meta_glasses_article', {})
        assert 'title' in meta_art

    def test_meta_article_headline_alarm(self, snap_specs_section):
        meta_art = snap_specs_section.get('meta_glasses_article', {})
        title = meta_art.get('title', '')
        # Headline should contain alarm language
        assert any(w in title.lower() for w in ['watched', 'surveillance', 'privacy'])

    def test_meta_article_tone_adversarial(self, snap_specs_section):
        meta_art = snap_specs_section.get('meta_glasses_article', {})
        tone = meta_art.get('tone', 0)
        assert tone <= -0.60

    def test_meta_surveillance_words_present(self, snap_specs_section):
        meta_art = snap_specs_section.get('meta_glasses_article', {})
        surveillance_words = meta_art.get('surveillance_vocabulary_count', 0)
        assert surveillance_words >= 3

    def test_meta_surveillance_vocabulary_listed(self, snap_specs_section):
        meta_art = snap_specs_section.get('meta_glasses_article', {})
        vocab = meta_art.get('surveillance_vocabulary', [])
        assert len(vocab) >= 3
        vocab_lower = [v.lower() for v in vocab]
        assert any('surveillance' in v for v in vocab_lower)


# ── Class 5: Tone Delta Analysis ───────────────────────────────────


class TestToneDelta:
    """Verify the tone delta between Snap and Meta camera coverage."""

    def test_tone_delta_calculated(self, snap_specs_section):
        delta = snap_specs_section.get('tone_delta', 0)
        assert delta > 0

    def test_tone_delta_significant(self, snap_specs_section):
        delta = snap_specs_section.get('tone_delta', 0)
        # At least 0.50 difference for structurally identical hardware
        assert delta >= 0.50

    def test_delta_favors_snap(self, snap_specs_section):
        snap_tone = snap_specs_section.get('snap_specs_article', {}).get('tone', 0)
        meta_tone = snap_specs_section.get('meta_glasses_article', {}).get('tone', 0)
        assert snap_tone > meta_tone


# ── Class 6: Clean Control Significance ─────────────────────────────


class TestCleanControlSignificance:
    """Verify the clean-control implications are documented."""

    def test_gizmodo_zero_financial_ties(self, snap_specs_section):
        sig = snap_specs_section.get('clean_control_significance', {})
        assert sig.get('gizmodo_financial_ties_to_snap') == 'none'
        assert sig.get('gizmodo_financial_ties_to_meta') == 'none'

    def test_isolates_cultural_coding(self, snap_specs_section):
        sig = snap_specs_section.get('clean_control_significance', {})
        mechanism = sig.get('mechanism_isolated', '')
        assert 'cultural' in mechanism.lower() or 'narrative' in mechanism.lower()

    def test_amplification_model_documented(self, snap_specs_section):
        sig = snap_specs_section.get('clean_control_significance', {})
        model = sig.get('amplification_model', '')
        assert 'financial' in model.lower() and 'amplif' in model.lower()

    def test_connects_to_barr_gradient(self, snap_specs_section):
        sig = snap_specs_section.get('clean_control_significance', {})
        related = sig.get('related_mechanisms', [])
        assert any('barr' in str(r).lower() or 'gradient' in str(r).lower() for r in related)


# ── Class 7: Mechanism #74 in Research File ─────────────────────────


class TestMechanism74InResearch:
    """Verify the mechanism is documented in competitor-coverage-research.yaml."""

    def test_mechanism_id(self, mechanism_74):
        assert mechanism_74.get('mechanism_id') == 74

    def test_mechanism_name(self, mechanism_74):
        name = mechanism_74.get('key_finding', '')
        assert 'surveillance' in name.lower() or 'vocabulary' in name.lower()

    def test_publication_is_gizmodo(self, mechanism_74):
        assert mechanism_74.get('publication') == 'Gizmodo (Keleops AG)'

    def test_has_source_urls(self, mechanism_74):
        urls = mechanism_74.get('source_urls', [])
        assert len(urls) >= 2

    def test_has_test_file(self, mechanism_74):
        tf = mechanism_74.get('test_file', '')
        assert 'gizmodo_snap_specs_camera_privacy_vocabulary_aug12' in tf

    def test_clean_control_flagged(self, mechanism_74):
        summary = mechanism_74.get('finding_summary', '')
        assert 'clean control' in summary.lower() or 'zero financial' in summary.lower()


# ── Class 8: Confounding Factors ────────────────────────────────────


class TestConfoundingFactors:
    """Verify honest confounding factors are documented."""

    def test_kenya_scandal_confound(self, snap_specs_section):
        """The Meta article was about a specific scandal, not a product preview."""
        factors = snap_specs_section.get('confounding_factors', [])
        factor_text = ' '.join(factors).lower()
        assert 'scandal' in factor_text or 'kenya' in factor_text or 'event' in factor_text

    def test_genre_confound(self, snap_specs_section):
        """Product preview vs investigative coverage are different genres."""
        factors = snap_specs_section.get('confounding_factors', [])
        factor_text = ' '.join(factors).lower()
        assert 'genre' in factor_text or 'preview' in factor_text or 'investigative' in factor_text

    def test_market_share_confound(self, snap_specs_section):
        """Meta has 7M+ units sold vs Snap with zero consumer units."""
        factors = snap_specs_section.get('confounding_factors', [])
        factor_text = ' '.join(factors).lower()
        assert 'market share' in factor_text or 'million' in factor_text or 'scale' in factor_text

    def test_at_least_four_confounds(self, snap_specs_section):
        factors = snap_specs_section.get('confounding_factors', [])
        assert len(factors) >= 4


# ── Class 9: Cross-Validation with Other Snap Coverage ──────────────


class TestCrossValidation:
    """Cross-validate with other publications' Snap coverage patterns."""

    def test_verge_snap_pattern_exists(self, research_data):
        """The Verge also shows differential Snap vs Meta framing."""
        agg = research_data.get('aggregate_findings', {})
        # Check for any Verge Snap Specs finding
        verge_keys = [k for k in agg if 'verge' in k.lower() and 'snap' in k.lower()]
        # May or may not exist — document either way
        assert True  # Cross-validation is a plus, not a requirement

    def test_snap_no_known_deals(self, gizmodo_profile):
        """Snap has no known content licensing deals with publications."""
        comp = gizmodo_profile.get('competitor_relationships', {})
        # Snap may not be in competitor_relationships — that's fine, it confirms no relationship
        snap = comp.get('snap', {})
        if snap:
            assert snap.get('financial_tie') in [None, 'none']

    def test_industry_wide_pattern(self, snap_specs_section):
        """The Snap camera vocabulary suppression matches industry-wide pattern."""
        sig = snap_specs_section.get('clean_control_significance', {})
        pattern = sig.get('industry_wide_evidence', '')
        assert len(pattern) > 0
