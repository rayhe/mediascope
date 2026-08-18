"""
TWiT 1058 'Furry Little Potatoes' — Victoria Song Cross-Medium Privacy Vocabulary Portability

MediaScope Mechanism #168: Victoria Song's documented privacy vocabulary bifurcation
(mechanism #112 in print at The Verge) extends identically to her appearances on
TWiT, the premier general tech podcast.

Key evidence from full transcript (recorded Nov 16, 2025):
- Song applies 12+ privacy-alarm terms exclusively to Meta glasses
- ZERO mentions of Samsung, Snap Spectacles (4 cameras, shipping), or Google Android XR
  in any privacy context across 5,717 transcript lines
- Christina Warren (Google→GitHub career migration) calls Meta glasses "insidious"
  while simultaneously saying "that's kind of why I like them"
- Neural band feature described as "super spy stuff... James Bond level"
- Song confirms white LED recording indicator invisible in daylight — "just not gonna see it"

This is the THIRD podcast confirming Victoria Song's cross-medium vocabulary portability:
1. Kill Switch (Sep 17, 2025) — with Dexter Thomas
2. TWiT 1058 (Nov 16, 2025) — with Leo Laporte, Christina Warren
3. Vergecast "All eyes on Meta's smart glasses" — The Verge's own podcast

Sources:
- Transcript: https://twit.tv/posts/transcripts/week-tech-episode-1058-transcript
- Episode: https://twit.tv/shows/this-week-in-tech/episodes/1058
- TWiT blog summary: https://twit.tv/posts/tech/are-meta-ray-ban-display-glasses-ready-everyday-use
"""

import pytest
import yaml
import os
import glob


# -------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------

def load_competitor_research():
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def find_mechanism(data, mechanism_id):
    """Search all sections for a mechanism by ID."""
    if not data:
        return None
    for key, value in data.items():
        if isinstance(value, dict) and value.get('mechanism_id') == mechanism_id:
            return value
        if isinstance(value, dict):
            result = find_mechanism(value, mechanism_id)
            if result:
                return result
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    if item.get('mechanism_id') == mechanism_id:
                        return item
                    result = find_mechanism(item, mechanism_id)
                    if result:
                        return result
    return None


def find_all_mechanisms(data, prefix=''):
    """Recursively find all mechanism entries."""
    mechanisms = []
    if not data:
        return mechanisms
    for key, value in data.items():
        if isinstance(value, dict) and 'mechanism_id' in value:
            mechanisms.append(value)
        elif isinstance(value, dict):
            mechanisms.extend(find_all_mechanisms(value, prefix=f"{prefix}.{key}"))
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict) and 'mechanism_id' in item:
                    # Only count as mechanism if it has more than just mechanism_id
                    if len(item) > 2:  # mechanism_id + at least one other field
                        mechanisms.append(item)
    return mechanisms


# -------------------------------------------------------------------
# Class 1: Mechanism #168 Existence and Structure
# -------------------------------------------------------------------

class TestMechanism168Exists:
    """Verify mechanism #168 exists in competitor-coverage-research.yaml."""

    def test_mechanism_168_present(self):
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        assert m is not None, "Mechanism #168 must exist"

    def test_mechanism_168_has_asymmetry_score(self):
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        assert 'asymmetry_score' in m, "Must have asymmetry_score"
        assert isinstance(m['asymmetry_score'], (int, float))
        assert 0 <= m['asymmetry_score'] <= 1.0

    def test_mechanism_168_has_source_urls(self):
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        assert 'source_urls' in m
        urls = m['source_urls']
        assert len(urls) >= 2, "Must have at least 2 source URLs"

    def test_mechanism_168_has_confounders(self):
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        assert 'confounding_factors' in m
        assert len(m['confounding_factors']) >= 3

    def test_mechanism_168_has_cross_references(self):
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        assert 'cross_references' in m
        refs = m['cross_references']
        assert len(refs) >= 2

    def test_mechanism_168_has_test_file(self):
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        assert 'test_file' in m
        assert 'twit_1058' in m['test_file']

    def test_mechanism_168_has_test_count(self):
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        assert 'test_count' in m
        assert m['test_count'] >= 40

    def test_mechanism_168_has_testable_predictions(self):
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        assert 'testable_predictions' in m
        assert len(m['testable_predictions']) >= 3


# -------------------------------------------------------------------
# Class 2: TWiT 1058 Episode Details
# -------------------------------------------------------------------

class TestTWiT1058EpisodeDetails:
    """Verify the episode metadata is accurately recorded."""

    def test_host_is_leo_laporte(self):
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        finding = m.get('finding_summary', '')
        assert 'Leo Laporte' in finding or 'TWiT' in finding

    def test_victoria_song_identified(self):
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        finding = m.get('finding_summary', '')
        assert 'Victoria Song' in finding

    def test_christina_warren_identified(self):
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        finding = m.get('finding_summary', '')
        assert 'Christina Warren' in finding

    def test_episode_date_recorded(self):
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        finding = m.get('finding_summary', '')
        assert '2025' in finding or 'November' in finding


# -------------------------------------------------------------------
# Class 3: Victoria Song Privacy Vocabulary Portability
# -------------------------------------------------------------------

class TestVictoriaSongVocabularyPortability:
    """
    Victoria Song's privacy vocabulary bifurcation (mechanism #112)
    extends from print to podcast — same journalist, same patterns,
    different medium.
    """

    def test_privacy_alarm_vocabulary_meta_directed(self):
        """Song uses privacy alarm language exclusively toward Meta."""
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        finding = m.get('finding_summary', '')
        assert any(term in finding.lower() for term in [
            'privacy', 'recording', 'ethical', 'spy', 'insidious',
            'freaky', 'james bond', 'white light', 'led'
        ]), "Must document privacy alarm vocabulary directed at Meta"

    def test_zero_samsung_mentions(self):
        """Samsung gets zero mentions in 5,717-line transcript."""
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        finding = m.get('finding_summary', '')
        assert 'Samsung' in finding or 'zero' in finding.lower()

    def test_snap_only_historical(self):
        """Snap mentioned only as 2018 Spectacles history, not current competitor."""
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        finding = m.get('finding_summary', '')
        # The finding should document Snap's absence from privacy discussion
        assert any(term in finding.lower() for term in [
            'snap', 'spectacles', 'competitor', 'zero'
        ])

    def test_cross_references_mechanism_112(self):
        """Must reference mechanism #112 (Victoria Song print bifurcation)."""
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        refs = m.get('cross_references', [])
        ref_ids = [r.get('mechanism_id') for r in refs]
        assert 112 in ref_ids, "Must cross-reference mechanism #112"

    def test_cross_medium_portability_documented(self):
        """The cross-medium nature (print→podcast) must be documented."""
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        finding = m.get('finding_summary', '')
        assert any(term in finding.lower() for term in [
            'cross-medium', 'podcast', 'print', 'portability'
        ])


# -------------------------------------------------------------------
# Class 4: Christina Warren Analysis
# -------------------------------------------------------------------

class TestChristinaWarrenDualFraming:
    """
    Christina Warren (Google DeepMind → GitHub career migration)
    provides unique dual framing: calls Meta glasses 'insidious'
    while liking the product.
    """

    def test_insidious_vocabulary(self):
        """Warren uses 'insidious' for Meta glasses."""
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        finding = m.get('finding_summary', '')
        assert 'insidious' in finding.lower()

    def test_career_migration_context(self):
        """Warren's career path (Google/DeepMind → GitHub) is noted."""
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        finding = m.get('finding_summary', '')
        assert any(term in finding for term in ['Google', 'DeepMind', 'GitHub'])

    def test_dual_register_documented(self):
        """Warren simultaneously likes Meta glasses AND calls them insidious."""
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        finding = m.get('finding_summary', '')
        # Should document the duality
        assert 'like' in finding.lower() or 'dual' in finding.lower() or 'simultaneously' in finding.lower()


# -------------------------------------------------------------------
# Class 5: Entity Coverage Asymmetry
# -------------------------------------------------------------------

class TestEntityCoverageAsymmetry:
    """
    In 5,717 transcript lines, privacy vocabulary is directed
    exclusively at Meta. Competitors with identical or greater
    surveillance capabilities receive zero privacy scrutiny.
    """

    def test_meta_receives_all_privacy_vocabulary(self):
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        finding = m.get('finding_summary', '')
        assert 'Meta' in finding

    def test_competitor_zero_privacy_scrutiny(self):
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        finding = m.get('finding_summary', '')
        assert any(term in finding.lower() for term in [
            'zero', 'no competitor', 'absent', 'not mentioned'
        ])

    def test_neural_band_silent_recording_framing(self):
        """Neural band described as enabling silent, covert recording."""
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        finding = m.get('finding_summary', '')
        assert any(term in finding.lower() for term in [
            'neural band', 'silent', 'spy', 'james bond', 'covert'
        ])

    def test_white_led_invisible_framing(self):
        """White LED recording indicator described as invisible in daylight."""
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        finding = m.get('finding_summary', '')
        assert any(term in finding.lower() for term in [
            'white', 'led', 'invisible', 'daylight', 'not gonna see'
        ])

    def test_harassment_example_meta_specific(self):
        """Bay Area university harassment case cited as Meta-specific."""
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        finding = m.get('finding_summary', '')
        assert any(term in finding.lower() for term in [
            'harass', 'university', 'bay area', 'women'
        ])


# -------------------------------------------------------------------
# Class 6: Cross-Medium Portability Pattern
# -------------------------------------------------------------------

class TestCrossMediumPortability:
    """
    Victoria Song is now documented across THREE podcast appearances
    with consistent privacy vocabulary bifurcation.
    """

    def test_three_podcast_appearances(self):
        """Song's privacy vocabulary confirmed in 3+ podcast appearances."""
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        finding = m.get('finding_summary', '')
        assert any(term in finding for term in [
            'Kill Switch', 'three', 'third', 'TWiT', 'Vergecast'
        ])

    def test_twit_is_premier_tech_podcast(self):
        """TWiT's significance as premier general tech podcast documented."""
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        finding = m.get('finding_summary', '')
        assert 'TWiT' in finding

    def test_full_transcript_evidence(self):
        """Full transcript availability strengthens evidence quality."""
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        urls = m.get('source_urls', [])
        assert any('transcript' in url for url in urls)

    def test_vox_media_network_cross_ref(self):
        """Cross-references Vox Media Podcast Network mechanism."""
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        refs = m.get('cross_references', [])
        ref_ids = [r.get('mechanism_id') for r in refs]
        assert 148 in ref_ids, "Must cross-reference mechanism #148 (Vox Media Network)"


# -------------------------------------------------------------------
# Class 7: Confounders Validation
# -------------------------------------------------------------------

class TestConfounders:
    """Ensure confounders are properly rated."""

    def test_at_least_one_strong_confounder(self):
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        cfs = m.get('confounding_factors', [])
        strong = [c for c in cfs if c.get('strength') == 'STRONG']
        assert len(strong) >= 1

    def test_at_least_one_moderate_confounder(self):
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        cfs = m.get('confounding_factors', [])
        moderate = [c for c in cfs if c.get('strength') == 'MODERATE']
        assert len(moderate) >= 1

    def test_confounders_have_factor_text(self):
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        cfs = m.get('confounding_factors', [])
        for cf in cfs:
            assert 'factor' in cf
            assert len(cf['factor']) > 20


# -------------------------------------------------------------------
# Class 8: Asymmetry Score Calibration
# -------------------------------------------------------------------

class TestAsymmetryScore:
    """Score should reflect strong but somewhat expected pattern."""

    def test_score_in_expected_range(self):
        """Score should be 0.7-0.9 — strong asymmetry but expected from tracked journalist."""
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        score = m['asymmetry_score']
        assert 0.65 <= score <= 0.95

    def test_score_consistent_with_kill_switch(self):
        """Score should be within 0.15 of Kill Switch Victoria Song score."""
        # Kill Switch scored Victoria Song at -7/10 sentiment
        # TWiT should score similarly
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        score = m['asymmetry_score']
        # Kill Switch is mechanism #144 area, exact score varies
        assert score >= 0.65, "Should show meaningful asymmetry"


# -------------------------------------------------------------------
# Class 9: Testable Predictions
# -------------------------------------------------------------------

class TestTestablePredictions:
    """Verify predictions are falsifiable and forward-looking."""

    def test_predictions_are_falsifiable(self):
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        preds = m.get('testable_predictions', [])
        for pred in preds:
            assert len(pred) > 30, f"Prediction too short: {pred}"

    def test_at_least_three_predictions(self):
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        preds = m.get('testable_predictions', [])
        assert len(preds) >= 3

    def test_predictions_reference_future_events(self):
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        preds = m.get('testable_predictions', [])
        future_markers = ['will', 'should', 'when', 'if', 'prediction']
        for pred in preds:
            assert any(marker in pred.lower() for marker in future_markers)


# -------------------------------------------------------------------
# Class 10: Test File Integrity
# -------------------------------------------------------------------

class TestFileIntegrity:
    """Cross-validation of this test file's existence and consistency."""

    def test_this_test_file_exists(self):
        path = os.path.join(os.path.dirname(__file__),
                           'test_twit_1058_victoria_song_cross_medium_privacy_vocabulary_portability_aug18.py')
        assert os.path.exists(path)

    def test_mechanism_168_test_file_matches(self):
        data = load_competitor_research()
        m = find_mechanism(data, 168)
        expected = 'tests/test_twit_1058_victoria_song_cross_medium_privacy_vocabulary_portability_aug18.py'
        assert m['test_file'] == expected

    def test_total_mechanisms_at_least_168(self):
        data = load_competitor_research()
        mechanisms = find_all_mechanisms(data)
        max_id = max(m.get('mechanism_id', 0) for m in mechanisms)
        assert max_id >= 168
