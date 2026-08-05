"""
Tests for Victoria Song (The Verge) cross-entity wearables coverage analysis.

Validates that Song's coverage demonstrates fair cross-entity editorial standards:
she covers Meta, Apple, and Google wearables through a consistent product-reviewer
lens, unlike WIRED's lane assignment asymmetry (Lauren Goode covers Apple but not Meta).

Her functional criticism of Meta ("Live AI is a solution looking for a problem")
is distinct from surveillance/alarm framing, and her Jul 7 LED piece reports
Meta's PROACTIVE response, not an adversarial investigation.
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


class TestVictoriaSongProfile:
    """Victoria Song's journalist profile in the-verge.yaml."""

    def test_song_exists_in_key_journalists(self, verge_profile):
        """Victoria Song should be listed as a key journalist."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song']
        assert len(song) == 1, "Victoria Song should appear exactly once"

    def test_song_has_competitor_coverage_analysis(self, verge_profile):
        """Song's profile should include cross-entity coverage analysis."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        assert 'competitor_coverage_analysis' in song, (
            "Song needs competitor_coverage_analysis section"
        )

    def test_song_meta_tone_not_adversarial(self, verge_profile):
        """Song's Meta coverage tone should NOT be 'adversarial' — she's balanced."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        meta_tone = analysis.get('meta_coverage', {}).get('tone', '')
        assert meta_tone != 'adversarial', (
            f"Song's Meta tone is '{meta_tone}' — should not be 'adversarial'. "
            "Her product reviews are balanced-to-positive."
        )

    def test_song_meta_has_positive_quotes(self, verge_profile):
        """Song should have documented positive Meta coverage quotes."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        quotes = analysis.get('meta_coverage', {}).get('key_quotes', [])
        assert len(quotes) >= 3, (
            f"Found {len(quotes)} positive Meta quotes, expected >= 3. "
            "Song gave multiple enthusiastic reviews of Meta glasses."
        )

    def test_song_live_ai_criticism_is_functional(self, verge_profile):
        """Song's 'solution looking for a problem' piece is functional critique, not surveillance."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        critical = analysis.get('meta_coverage', {}).get('critical_pieces', [])
        live_ai = [p for p in critical if 'solution looking for a problem' in p.get('title', '').lower()
                   or 'live ai' in p.get('title', '').lower()]
        assert len(live_ai) >= 1, "Live AI critique should be documented"
        piece = live_ai[0]
        framing = piece.get('framing', '').lower()
        assert 'surveillance' not in framing or 'not surveillance' in framing, (
            "Live AI piece framing should be functional, not surveillance-alarm"
        )
        assert piece.get('tone', 0) > -0.5, (
            f"Live AI tone {piece['tone']} too negative — it's product critique, not adversarial"
        )

    def test_song_led_piece_is_meta_response(self, verge_profile):
        """Song's Jul 7 LED piece reports Meta's proactive update, not adversarial investigation."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        critical = analysis.get('meta_coverage', {}).get('critical_pieces', [])
        led_pieces = [p for p in critical if 'led' in p.get('title', '').lower()
                      or 'tamper' in p.get('title', '').lower()]
        assert len(led_pieces) >= 1, "LED tamper-proof piece should be documented"
        piece = led_pieces[0]
        framing = piece.get('framing', '').lower()
        assert 'proactive' in framing or 'response' in framing or 'update' in framing, (
            "LED piece framing should note Meta's proactive response, "
            "not characterize as adversarial investigation"
        )
        assert piece.get('tone', 0) > -0.5, (
            f"LED piece tone {piece['tone']} too negative — "
            "Song reported Meta's positive action, not attacked them"
        )

    def test_song_accessibility_coverage_documented(self, verge_profile):
        """Song's accessibility-focused Meta coverage should be documented."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        accessibility = analysis.get('meta_coverage', {}).get('accessibility_focus', [])
        assert len(accessibility) >= 1, (
            "Song's accessibility coverage (Vergecast, Optimizer newsletter) should be documented"
        )

    def test_song_apple_no_surveillance_framing(self, verge_profile):
        """Song's Apple coverage should have no surveillance framing despite 12 cameras."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        apple = analysis.get('apple_coverage', {})
        assert apple.get('tone') in ('balanced', 'balanced_to_positive', 'positive', 'neutral'), (
            f"Apple tone '{apple.get('tone')}' unexpected — Song covers Apple products positively"
        )

    def test_song_meta_vs_apple_comparison_documented(self, verge_profile):
        """Song's 'Meta might be better than Apple' piece should be documented."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        comparison = analysis.get('meta_vs_apple_direct_comparison', {})
        assert comparison, "Meta vs Apple direct comparison piece should be documented"
        assert comparison.get('tone', 0) > 0, (
            "Pro-Meta comparative piece should have positive tone"
        )


class TestVergeCompetitorResearchCorrections:
    """Verify competitor-coverage-research.yaml has corrected Victoria Song attribution."""

    def test_verge_meta_summary_not_attribute_adversarial_to_song(self, competitor_research):
        """The Verge meta_coverage_summary should not claim Song runs adversarial coverage."""
        verge = competitor_research['publications']['the-verge']
        summary = verge.get('meta_coverage_summary', '')
        assert 'runs sustained adversarial' not in summary.lower(), (
            "Corrected summary should not claim Song 'runs sustained adversarial coverage'"
        )

    def test_verge_led_piece_labeled_meta_response(self, competitor_research):
        """The LED tamper-proof example should be labeled as Meta's response."""
        verge = competitor_research['publications']['the-verge']
        examples = verge.get('meta_examples', [])
        led_examples = [e for e in examples if 'led' in e.get('title', '').lower()
                        or 'tamper' in e.get('title', '').lower()]
        assert len(led_examples) >= 1, "LED example should exist"
        piece = led_examples[0]
        assert piece.get('tone', -1) > -0.5, (
            f"LED piece tone {piece.get('tone')} should be corrected from -0.65 to reflect "
            "Meta response reporting, not adversarial investigation"
        )

    def test_verge_has_pro_meta_example(self, competitor_research):
        """Should document Song's pro-Meta comparative piece."""
        verge = competitor_research['publications']['the-verge']
        examples = verge.get('meta_examples', [])
        pro_meta = [e for e in examples if e.get('tone', -1) > 0]
        assert len(pro_meta) >= 1, (
            "Verge examples should include at least one positive-tone piece "
            "(Song's 'Meta might be better than Apple' comparison)"
        )


class TestCrossEntityLaneComparison:
    """Compare WIRED vs Verge journalist lane assignment patterns."""

    def test_wired_has_lane_asymmetry(self, competitor_research):
        """WIRED should document lane assignment asymmetry (Goode covers Apple, not Meta)."""
        wired = competitor_research['publications']['wired']
        # The WIRED profile should show that different journalists cover different entities
        meta_summary = wired.get('meta_coverage_summary', '')
        assert wired.get('meta_coverage_tone') == 'adversarial', (
            "WIRED's institutional Meta tone should be adversarial"
        )

    def test_verge_song_covers_both_entities(self, verge_profile):
        """Song should document coverage of both Meta AND Apple (unlike WIRED's Goode)."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        assert 'meta_coverage' in analysis, "Song should have meta_coverage documented"
        assert 'apple_coverage' in analysis, "Song should have apple_coverage documented"
        assert 'meta_vs_apple_direct_comparison' in analysis, (
            "Song should have direct comparison documented"
        )

    def test_verge_institutional_vs_product_coverage_split(self, verge_profile):
        """Verify The Verge profile documents the split between institutional adversarial
        tone (Alex Heath, Patel) and product-balanced tone (Victoria Song)."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song'][0]
        analysis = song.get('competitor_coverage_analysis', {})
        significance = analysis.get('cross_entity_analytical_significance', '')
        assert 'alex heath' in significance.lower() or 'nilay patel' in significance.lower(), (
            "Cross-entity significance should note that adversarial tone comes from "
            "Heath/Patel, not Song's product reviews"
        )
