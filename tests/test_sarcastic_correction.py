"""Tests for the sarcastic_correction framing device.

Added 2026-06-26 after discovering explicit editorial sarcasm in Engadget's
coverage of the Wynn-Williams v. Meta lawsuit.
"""

import pytest

from mediascope.analyze.framing import detect_framing_devices, _DEVICE_PATTERNS


class TestSarcasticCorrectionRegistered:
    """Verify sarcastic_correction is in the device registry."""

    def test_in_registry(self):
        assert "sarcastic_correction" in _DEVICE_PATTERNS

    def test_pattern_compiles(self):
        """Pattern must compile without error and be a list of compiled regexes."""
        patterns = _DEVICE_PATTERNS["sarcastic_correction"]
        assert len(patterns) > 0
        for p in patterns:
            assert hasattr(p, "search"), f"Pattern {p} is not a compiled regex"


class TestSarcasticCorrectionDetection:
    """Detection tests using real and synthetic examples."""

    def test_engadget_real_article(self):
        """The article that prompted this device type."""
        text = (
            "Of course, when Careless People was published, it instantly "
            "caused the company to go out of business and its leaders were "
            "given the necessary scrutiny... oh hang on, wait, no. The "
            "company's share price reached a high of $785 a few months later."
        )
        results = detect_framing_devices(text)
        types = [d.device_type for d in results]
        assert "sarcastic_correction" in types, (
            f"Expected sarcastic_correction in {types}"
        )

    def test_of_course_oh_wait(self):
        """'Of course... oh wait' pattern."""
        text = (
            "Of course, the new policy immediately solved everything... "
            "oh wait, no it didn't."
        )
        results = detect_framing_devices(text)
        types = [d.device_type for d in results]
        assert "sarcastic_correction" in types

    def test_just_kidding(self):
        """'Just kidding' standalone sarcasm."""
        text = (
            "The company assured users their data was safe. "
            "Just kidding. The breach exposed 50 million accounts."
        )
        results = detect_framing_devices(text)
        types = [d.device_type for d in results]
        assert "sarcastic_correction" in types

    def test_spoiler_it_didnt(self):
        """'Spoiler: it didn't' TV-trope pattern."""
        text = (
            "Meta promised the new algorithm would reduce harmful content. "
            "Spoiler: it didn't."
        )
        results = detect_framing_devices(text)
        types = [d.device_type for d in results]
        assert "sarcastic_correction" in types

    def test_right_wrong(self):
        """'...right? Wrong.' pattern."""
        text = (
            "Surely a company this large would have proper safeguards "
            "in place, right? Wrong."
        )
        results = detect_framing_devices(text)
        types = [d.device_type for d in results]
        assert "sarcastic_correction" in types

    def test_narrator_it_did_not(self):
        """'(Narrator: it did not.)' TV-trope pattern."""
        text = (
            "The CEO assured investors the restructuring would be painless. "
            "(Narrator: it was not.)"
        )
        results = detect_framing_devices(text)
        types = [d.device_type for d in results]
        assert "sarcastic_correction" in types

    def test_color_me_surprised(self):
        """Standalone sarcastic expression."""
        text = "Color me surprised that the self-regulation pledge didn't work."
        results = detect_framing_devices(text)
        types = [d.device_type for d in results]
        assert "sarcastic_correction" in types

    def test_who_could_have_predicted(self):
        """Feigned-surprise sarcasm."""
        text = (
            "Who could have predicted that letting the fox guard "
            "the henhouse would end badly?"
        )
        results = detect_framing_devices(text)
        types = [d.device_type for d in results]
        assert "sarcastic_correction" in types

    def test_what_could_possibly_go_wrong(self):
        """Rhetorical-negative sarcasm."""
        text = (
            "Giving one company control over the global information supply. "
            "What could possibly go wrong?"
        )
        results = detect_framing_devices(text)
        types = [d.device_type for d in results]
        assert "sarcastic_correction" in types

    def test_nothing_to_see_here(self):
        """Dismissive sarcasm."""
        text = (
            "Another data breach, another apology tour. Nothing to see here."
        )
        results = detect_framing_devices(text)
        types = [d.device_type for d in results]
        assert "sarcastic_correction" in types


class TestSarcasticCorrectionFalsePositives:
    """Ensure legitimate uses don't trigger false positives."""

    def test_neutral_of_course(self):
        """'Of course' in a non-sarcastic context should not trigger."""
        text = (
            "Of course, the company has the right to enforce its contracts. "
            "The question is whether doing so is wise."
        )
        results = detect_framing_devices(text)
        types = [d.device_type for d in results]
        assert "sarcastic_correction" not in types

    def test_neutral_right(self):
        """A regular 'right' in prose should not trigger."""
        text = "The decision was right for the company at the time."
        results = detect_framing_devices(text)
        types = [d.device_type for d in results]
        assert "sarcastic_correction" not in types

    def test_neutral_surprise(self):
        """Genuine surprise should not trigger."""
        text = "Analysts were surprised by the strong quarterly results."
        results = detect_framing_devices(text)
        types = [d.device_type for d in results]
        assert "sarcastic_correction" not in types
