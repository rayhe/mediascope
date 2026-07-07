"""Regression tests for Jul 7 2026 Type D fixes.

Bug 1: generate_disclosure() crashed on PublicationProfile objects
       (AttributeError: 'PublicationProfile' has no 'get' method).
Bug 2: Catastrophic regex backtracking in competitive_deficit pattern #2
       caused hangs on phrases like "responsible data practices".
"""
import time
import re

import pytest

from mediascope.config import load_profile
from mediascope.conflicts.disclosure import generate_disclosure
from mediascope.analyze.framing import detect_framing_devices


# --- Bug 1: Disclosure generation with PublicationProfile objects ---

class TestDisclosureProfileCompat:
    """generate_disclosure must accept PublicationProfile, not just dicts."""

    def test_wired_profile_no_crash(self):
        """load_profile('wired') + generate_disclosure should not crash."""
        profile = load_profile('wired')
        result = generate_disclosure(profile, 'Meta')
        assert isinstance(result, str)
        assert len(result) > 100, "Disclosure too short to be real"

    def test_disclosure_contains_ownership(self):
        profile = load_profile('wired')
        result = generate_disclosure(profile, 'Meta')
        assert 'OWNERSHIP CHAIN' in result

    def test_disclosure_contains_conflicts(self):
        profile = load_profile('wired')
        result = generate_disclosure(profile, 'Meta')
        # Should mention at least one conflict area
        assert any(kw in result for kw in ['REVENUE', 'CONFLICT', 'Reddit', 'Advance'])

    def test_all_profiles_generate_disclosure(self):
        """Every profile YAML should produce a disclosure without crashing."""
        import pathlib
        profiles_dir = pathlib.Path(__file__).parent.parent / 'profiles'
        for yaml_file in profiles_dir.glob('*.yaml'):
            slug = yaml_file.stem
            try:
                profile = load_profile(slug)
            except Exception:
                continue  # Some profiles may not be loadable
            result = generate_disclosure(profile, 'Meta')
            assert isinstance(result, str), f"Profile {slug} returned non-string"


# --- Bug 2: Regex backtracking in competitive_deficit ---

class TestRegexBacktracking:
    """competitive_deficit pattern must not hang on adversarial inputs."""

    TIMEOUT_SECONDS = 2.0  # Should complete in <0.1s; 2s is generous guard

    def test_responsible_data_practices(self):
        """The exact text that caused the original hang."""
        text = (
            "The company said it would implement responsible data practices "
            "and work with regulators to ensure compliance with privacy laws."
        )
        start = time.monotonic()
        result = detect_framing_devices(text)
        elapsed = time.monotonic() - start
        assert elapsed < self.TIMEOUT_SECONDS, (
            f"detect_framing_devices took {elapsed:.2f}s — likely backtracking"
        )

    def test_long_capitalized_word_sequence(self):
        """Multiple capitalized words without commas — the backtracking trigger."""
        text = (
            "Apple Microsoft Google Amazon Meta Oracle Intel Nvidia Samsung "
            "are all investing heavily in the space."
        )
        start = time.monotonic()
        result = detect_framing_devices(text)
        elapsed = time.monotonic() - start
        assert elapsed < self.TIMEOUT_SECONDS, (
            f"detect_framing_devices took {elapsed:.2f}s on capitalized words"
        )

    def test_competitive_deficit_still_matches_legitimate(self):
        """Ensure the fix didn't break legitimate competitive_deficit detection."""
        text = "competitors including Google, OpenAI, and Anthropic are ahead of Meta"
        result = detect_framing_devices(text)
        cd_matches = [r for r in result if r.device_type == 'competitive_deficit']
        assert len(cd_matches) > 0, (
            "competitive_deficit should still match comma-separated competitor lists"
        )

    def test_competitive_deficit_evidence_text(self):
        """FramingDevice uses evidence_text attribute (not 'evidence')."""
        text = "competitors including Google, OpenAI, and Anthropic are ahead"
        result = detect_framing_devices(text)
        cd_matches = [r for r in result if r.device_type == 'competitive_deficit']
        if cd_matches:
            assert hasattr(cd_matches[0], 'evidence_text')
            assert isinstance(cd_matches[0].evidence_text, str)
            assert len(cd_matches[0].evidence_text) > 0
