"""
Tests for Victoria Song Privacy Vocabulary Bifurcation — Mechanism #75.

Finding: Victoria Song (The Verge) applies BIFURCATED editorial standards to
camera-equipped wearables from different entities. Her PRODUCT reviews are
genuinely balanced across Meta, Apple, and Google. But she writes dedicated
privacy/surveillance/doxing pieces EXCLUSIVELY about Meta's camera-equipped
glasses, never about Apple's Vision Pro (12 cameras, 5 sensors, 6 mics),
Google's Android XR glasses (cameras + AI), or Snap Specs (4 cameras + AI).

This creates a more subtle asymmetry than WIRED's lane assignment (where
different journalists cover different entities). Here, the SAME journalist
applies two different editorial MODES — product-review vs privacy-adversarial —
but the privacy-adversarial mode is activated only for Meta. The effect:
Song appears balanced (because her product reviews ARE balanced), while
selectively amplifying privacy alarm for one entity.

Key comparison:
- Meta Ray-Ban glasses (1 camera): "dox people in real time," "eerie,"
  "privacy light hack" concerns, dedicated doxing investigation
- Apple Vision Pro (12 cameras, 5 sensors, 6 mics): zero privacy vocabulary,
  product-focused weight/keyboard/display coverage only
- Google Android XR (cameras + AI): "Tony Stark," "Jarvis," zero privacy vocabulary
- Snap Spectacles: not reviewed by Song (The Verge assigns to other staff)

Extends: Mechanism #6 (Barr Privacy Gradient), #31 (Pero Editorial Direction),
#74 (Gizmodo Snap Specs Camera Privacy), and existing Song cross-entity analysis.
Contrasts with Mechanism #63 (Zeff source access asymmetry) and
#72 (Tiku company-agnostic adversarial).
"""

import yaml
import pytest
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


@pytest.fixture
def verge_profile():
    with open(os.path.join(PROFILES_DIR, 'the-verge.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture
def competitor_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture
def competitor_entities():
    with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')) as f:
        return yaml.safe_load(f)


class TestSongPrivacyVocabularyBifurcation:
    """Core mechanism: same journalist, different privacy vocabulary by entity."""

    def test_meta_has_privacy_adversarial_pieces(self, verge_profile):
        """Song should have documented privacy/adversarial pieces for Meta."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        critical = analysis.get('meta_coverage', {}).get('critical_pieces', [])
        assert len(critical) >= 2, (
            f"Found {len(critical)} critical Meta pieces, expected >= 2 "
            "(doxing story + LED tamper-proof + Live AI critique)"
        )

    def test_meta_doxing_piece_documented(self, verge_profile):
        """Song's Oct 2024 doxing piece about Meta glasses should be documented."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        privacy = analysis.get('privacy_vocabulary_bifurcation', {})
        meta_pieces = privacy.get('meta_privacy_pieces', [])
        doxing = [p for p in meta_pieces
                  if 'dox' in p.get('title', '').lower()
                  or 'dox' in p.get('framing', '').lower()]
        assert len(doxing) >= 1, (
            "Song's Oct 2024 'College students used Meta's smart glasses to dox people' "
            "piece should be documented as a Meta-specific privacy piece"
        )

    def test_apple_zero_privacy_vocabulary(self, verge_profile):
        """Song's Apple Vision Pro coverage should have ZERO privacy/surveillance vocabulary."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        apple = analysis.get('apple_coverage', {})
        # Apple Vision Pro has 12 cameras, 5 sensors, 6 mics — more sensors than Meta
        privacy_terms = apple.get('surveillance_vocabulary_count', 0)
        assert privacy_terms == 0, (
            f"Apple coverage has {privacy_terms} surveillance vocabulary instances. "
            "Expected 0 — Song writes no privacy/surveillance pieces about Apple "
            "despite Vision Pro having 12 cameras, 5 sensors, and 6 mics."
        )

    def test_google_zero_privacy_vocabulary(self, verge_profile):
        """Song's Google Android XR coverage should have zero privacy vocabulary."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        google = analysis.get('google_android_xr_coverage', {})
        privacy_terms = google.get('surveillance_vocabulary_count', 0)
        assert privacy_terms == 0, (
            f"Google coverage has {privacy_terms} surveillance vocabulary instances. "
            "Expected 0 — Song describes Google's camera-equipped glasses as 'Tony Stark' "
            "and 'Jarvis' with zero privacy concern."
        )

    def test_meta_nonzero_privacy_vocabulary(self, verge_profile):
        """Song's Meta privacy coverage should have nonzero surveillance vocabulary."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        privacy = analysis.get('privacy_vocabulary_bifurcation', {})
        meta_count = privacy.get('meta_surveillance_vocabulary_count', 0)
        assert meta_count > 0, (
            "Meta coverage should have nonzero surveillance vocabulary. "
            "Song's doxing piece + LED/privacy light coverage + podcast appearances "
            "all deploy privacy alarm language specifically for Meta."
        )

    def test_bifurcation_documented(self, verge_profile):
        """The privacy vocabulary bifurcation mechanism should be documented."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        bifurcation = analysis.get('privacy_vocabulary_bifurcation', {})
        assert bifurcation, (
            "privacy_vocabulary_bifurcation section should exist documenting "
            "the asymmetric application of surveillance language across entities"
        )

    def test_bifurcation_has_mechanism_reference(self, verge_profile):
        """The bifurcation section should reference the mechanism number."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        bifurcation = analysis.get('privacy_vocabulary_bifurcation', {})
        mechanism = bifurcation.get('mechanism_ref', '')
        assert '#75' in str(mechanism), (
            f"Mechanism reference '{mechanism}' should include '#75'"
        )


class TestSongDualModeEditorial:
    """Song operates in two editorial modes; privacy mode activates only for Meta."""

    def test_product_mode_balanced_across_entities(self, verge_profile):
        """In product-review mode, Song is balanced across Meta, Apple, Google."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})

        meta_tone = analysis.get('meta_coverage', {}).get('tone', '')
        apple_tone = analysis.get('apple_coverage', {}).get('tone', '')
        google_tone = analysis.get('google_android_xr_coverage', {}).get('tone', '')

        balanced_tones = ('balanced', 'balanced_to_positive', 'positive', 'neutral')
        assert meta_tone in balanced_tones, f"Meta product tone '{meta_tone}' should be balanced"
        assert apple_tone in balanced_tones, f"Apple product tone '{apple_tone}' should be balanced"
        assert google_tone in balanced_tones, f"Google product tone '{google_tone}' should be balanced"

    def test_privacy_mode_meta_only(self, verge_profile):
        """Privacy-adversarial articles exist for Meta but not Apple or Google."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})

        # Meta has critical/privacy pieces
        meta_critical = analysis.get('meta_coverage', {}).get('critical_pieces', [])
        assert len(meta_critical) >= 2, "Meta should have >= 2 critical pieces"

        # Apple should have no critical privacy pieces
        apple_critical = analysis.get('apple_coverage', {}).get('critical_privacy_pieces', [])
        assert len(apple_critical) == 0, (
            f"Apple has {len(apple_critical)} critical privacy pieces — expected 0. "
            "Song does not write privacy-adversarial pieces about Apple despite 12 cameras."
        )

        # Google should have no critical privacy pieces
        google_critical = analysis.get('google_android_xr_coverage', {}).get('critical_privacy_pieces', [])
        assert len(google_critical) == 0, (
            f"Google has {len(google_critical)} critical privacy pieces — expected 0. "
            "Song does not write privacy-adversarial pieces about Google's camera glasses."
        )

    def test_camera_count_mismatch(self, verge_profile):
        """Documents the camera-to-privacy-scrutiny paradox."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        bifurcation = analysis.get('privacy_vocabulary_bifurcation', {})

        camera_data = bifurcation.get('camera_count_vs_scrutiny', {})
        assert camera_data, "camera_count_vs_scrutiny section should exist"

        meta_cameras = camera_data.get('meta_cameras', 0)
        apple_cameras = camera_data.get('apple_cameras', 0)
        meta_privacy_pieces = camera_data.get('meta_privacy_piece_count', 0)
        apple_privacy_pieces = camera_data.get('apple_privacy_piece_count', 0)

        # Apple has 12x cameras but 0 privacy pieces; Meta has 1 camera but 3+ privacy pieces
        assert apple_cameras > meta_cameras, (
            f"Apple cameras ({apple_cameras}) should exceed Meta cameras ({meta_cameras})"
        )
        assert meta_privacy_pieces > apple_privacy_pieces, (
            f"Meta privacy pieces ({meta_privacy_pieces}) should exceed Apple ({apple_privacy_pieces})"
        )


class TestSongPodcastSurveillanceFraming:
    """Song's podcast appearances deploy surveillance framing specifically for Meta."""

    def test_kill_switch_podcast_meta_specific(self, verge_profile):
        """The kill switch podcast appearance raises privacy concerns about Meta glasses."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        bifurcation = analysis.get('privacy_vocabulary_bifurcation', {})
        podcast_privacy = bifurcation.get('podcast_privacy_appearances', [])

        meta_specific = [p for p in podcast_privacy
                         if 'meta' in p.get('entity_discussed', '').lower()]
        assert len(meta_specific) >= 1, (
            "At least one podcast appearance should discuss Meta-specific privacy concerns. "
            "Kill switch podcast: Song discusses LED hacking, social etiquette, recording fears."
        )

    def test_no_apple_google_podcast_privacy_concerns(self, verge_profile):
        """No podcast appearances raise privacy concerns about Apple or Google wearables."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        bifurcation = analysis.get('privacy_vocabulary_bifurcation', {})
        podcast_privacy = bifurcation.get('podcast_privacy_appearances', [])

        apple_privacy = [p for p in podcast_privacy
                         if 'apple' in p.get('entity_discussed', '').lower()]
        google_privacy = [p for p in podcast_privacy
                          if 'google' in p.get('entity_discussed', '').lower()]
        assert len(apple_privacy) == 0, (
            "No podcast appearances should raise privacy concerns about Apple's "
            "camera-equipped wearable (Vision Pro, 12 cameras)"
        )
        assert len(google_privacy) == 0, (
            "No podcast appearances should raise privacy concerns about Google's "
            "camera-equipped Android XR glasses"
        )


class TestSongVergecastBedroomQuestion:
    """The 'do smart glasses belong in the bedroom' question is Meta-specific."""

    def test_bedroom_question_documented(self, verge_profile):
        """Vergecast 'bedroom question' should be documented as Meta-specific framing."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        bifurcation = analysis.get('privacy_vocabulary_bifurcation', {})
        intimate = bifurcation.get('intimate_scenario_framing', {})
        assert intimate, (
            "intimate_scenario_framing section should document the Vergecast "
            "'do smart glasses belong in the bedroom' segment"
        )
        assert intimate.get('entity', '') == 'meta', (
            "The 'bedroom' surveillance question is posed specifically about Meta glasses, "
            "not about Apple Vision Pro (which also has cameras and could be used in a bedroom)"
        )

    def test_no_apple_bedroom_equivalent(self, verge_profile):
        """No equivalent intimate-scenario question asked about Apple or Google wearables."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        bifurcation = analysis.get('privacy_vocabulary_bifurcation', {})
        intimate = bifurcation.get('intimate_scenario_framing', {})
        entity = intimate.get('entity', '')
        assert entity != 'apple', "No bedroom/intimate scenario question for Apple"
        assert entity != 'google', "No bedroom/intimate scenario question for Google"


class TestSongConfoundingFactors:
    """Honest documentation of why the bifurcation might not be entity bias."""

    CONFOUNDING_FACTORS = [
        ("market_share", "Meta has 7M+ glasses sold; Apple/Google have near-zero consumer glasses — "
         "privacy scrutiny scales with deployed units"),
        ("form_factor", "Meta glasses look like normal glasses (covert recording potential); "
         "Vision Pro is an obvious face computer (recording is visible)"),
        ("doxing_news_peg", "I-XRAY demo used Meta glasses specifically — Song reported on the "
         "demo as presented, not by choosing to investigate Meta"),
        ("instagram_livestream", "Meta's Instagram livestream integration enables the specific "
         "doxing workflow; Apple/Google lack equivalent consumer streaming"),
        ("beat_assignment", "The Verge may assign privacy pieces to Song for Meta because she's "
         "the primary Meta wearables reviewer — editorial assignment, not personal bias"),
        ("chronological_exposure", "Meta glasses launched years before Apple/Google consumer "
         "glasses — more time to generate privacy incidents"),
    ]

    @pytest.mark.parametrize("factor_name,factor_description", CONFOUNDING_FACTORS)
    def test_confounding_factor_documented(self, factor_name, factor_description, verge_profile):
        """Each confounding factor should be documented in the profile."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        bifurcation = analysis.get('privacy_vocabulary_bifurcation', {})
        confounders = bifurcation.get('confounding_factors', [])
        factor_names = [c.get('factor', '') for c in confounders]
        assert factor_name in factor_names, (
            f"Confounding factor '{factor_name}' should be documented: {factor_description}"
        )


class TestSongCrossEntitySignificance:
    """Significance within the broader MediaScope framework."""

    def test_significance_references_wired_contrast(self, verge_profile):
        """The significance section should contrast Song with WIRED's lane assignment."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        significance = analysis.get('cross_entity_analytical_significance', '')
        assert 'wired' in significance.lower() or 'lane' in significance.lower(), (
            "Cross-entity significance should contrast Song's dual-mode bifurcation "
            "with WIRED's lane assignment asymmetry (Goode covers Apple/Snap, not Meta)"
        )

    def test_significance_notes_subtlety(self, verge_profile):
        """The significance section should note this is MORE subtle than lane assignment."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        bifurcation = analysis.get('privacy_vocabulary_bifurcation', {})
        subtlety = bifurcation.get('subtlety_note', '')
        assert subtlety, (
            "subtlety_note should explain why same-journalist bifurcation is harder "
            "to detect than different-journalist lane assignment"
        )


class TestCompetitorResearchMechanism75:
    """Mechanism #75 should be documented in competitor-coverage-research.yaml."""

    def test_mechanism_75_exists(self, competitor_research):
        """Mechanism #75 should exist in aggregate_findings."""
        findings = competitor_research.get('aggregate_findings', {})
        m75 = [v for v in findings.values() if isinstance(v, dict) and
               (v.get('mechanism_id') == 75 or '#75' in str(v.get('mechanism_id', '')))]
        assert len(m75) >= 1, "Mechanism #75 should be documented"

    def test_mechanism_75_has_confounders(self, competitor_research):
        """Mechanism #75 should document confounding factors."""
        findings = competitor_research.get('aggregate_findings', {})
        m75 = [v for v in findings.values() if isinstance(v, dict) and
               (v.get('mechanism_id') == 75 or '#75' in str(v.get('mechanism_id', '')))]
        assert len(m75) >= 1, "Mechanism #75 should exist"
        confounders = m75[0].get('confounding_factors', [])
        assert len(confounders) >= 5, (
            f"Found {len(confounders)} confounders, expected >= 5"
        )

    def test_mechanism_75_extends_prior_mechanisms(self, competitor_research):
        """Mechanism #75 should reference related mechanisms."""
        findings = competitor_research.get('aggregate_findings', {})
        m75 = [v for v in findings.values() if isinstance(v, dict) and
               (v.get('mechanism_id') == 75 or '#75' in str(v.get('mechanism_id', '')))]
        assert len(m75) >= 1, "Mechanism #75 should exist"
        refs = m75[0].get('cross_references', [])
        ref_ids = [r.get('mechanism_id', 0) for r in refs]
        # Should reference Gizmodo Snap Specs (#74) and Barr Privacy Gradient (#6)
        assert any(r in ref_ids for r in [6, 74]), (
            f"Cross-references {ref_ids} should include #6 (Barr Privacy Gradient) "
            "or #74 (Gizmodo Snap Specs Camera Privacy)"
        )

    def test_mechanism_75_journal_is_song(self, competitor_research):
        """Mechanism #75 should identify Victoria Song as the journalist."""
        findings = competitor_research.get('aggregate_findings', {})
        m75 = [v for v in findings.values() if isinstance(v, dict) and
               (v.get('mechanism_id') == 75 or '#75' in str(v.get('mechanism_id', '')))]
        assert len(m75) >= 1, "Mechanism #75 should exist"
        journalist = m75[0].get('journalist', '')
        assert 'victoria song' in journalist.lower(), (
            f"Mechanism #75 journalist '{journalist}' should be Victoria Song"
        )

    def test_mechanism_75_publication_is_verge(self, competitor_research):
        """Mechanism #75 should identify The Verge as the publication."""
        findings = competitor_research.get('aggregate_findings', {})
        m75 = [v for v in findings.values() if isinstance(v, dict) and
               (v.get('mechanism_id') == 75 or '#75' in str(v.get('mechanism_id', '')))]
        assert len(m75) >= 1, "Mechanism #75 should exist"
        pub = m75[0].get('publication', '')
        assert 'verge' in pub.lower(), (
            f"Mechanism #75 publication '{pub}' should be The Verge"
        )


class TestSongFramingEvolution:
    """Track Song's framing evolution from product-positive to privacy-critical."""

    def test_framing_evolution_documented(self, verge_profile):
        """Song's framing evolution timeline should be documented."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        bifurcation = analysis.get('privacy_vocabulary_bifurcation', {})
        evolution = bifurcation.get('framing_evolution', [])
        assert len(evolution) >= 3, (
            f"Found {len(evolution)} evolution stages, expected >= 3. "
            "Should track: product-positive (2022-24) → mixed (2024) → "
            "privacy-critical for Meta only (2025-26)"
        )

    def test_evolution_entity_specificity(self, verge_profile):
        """The privacy-critical evolution should be specifically Meta-targeted."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        bifurcation = analysis.get('privacy_vocabulary_bifurcation', {})
        evolution = bifurcation.get('framing_evolution', [])
        if evolution:
            latest = evolution[-1]
            affected_entity = latest.get('primary_entity', '')
            assert 'meta' in affected_entity.lower(), (
                f"Latest evolution stage targets '{affected_entity}' — "
                "should be Meta (privacy-critical mode activated only for Meta)"
            )


class TestSongDoxingStoryEntitySpecificity:
    """The doxing story specifically names Meta — analyze why."""

    def test_doxing_story_could_apply_to_any_camera(self, verge_profile):
        """The I-XRAY technique works with ANY camera device, not just Meta glasses."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        bifurcation = analysis.get('privacy_vocabulary_bifurcation', {})
        doxing = bifurcation.get('doxing_story_analysis', {})
        assert doxing, "Doxing story analysis section should exist"
        universality = doxing.get('technique_universality_noted', False)
        assert universality is True, (
            "Should document that the I-XRAY technique (face recognition + "
            "public database lookup) works with ANY camera device — laptops, "
            "phones, any smart glasses — not uniquely Meta's."
        )

    def test_doxing_headline_names_meta(self, verge_profile):
        """The headline specifically names Meta despite technique being universal."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        bifurcation = analysis.get('privacy_vocabulary_bifurcation', {})
        doxing = bifurcation.get('doxing_story_analysis', {})
        headline_entity = doxing.get('headline_entity', '')
        assert 'meta' in headline_entity.lower(), (
            "Headline 'College students used META'S smart glasses to dox people' "
            "specifically names Meta despite universal applicability"
        )
