"""Tests for Washington Examiner Meta Louisiana $50B data center article.

Discovered fixes (Jul 13, 2026 Type A iteration):
- scale_magnitude: physical-unit patterns (10 million-square-foot, five-gigawatt)
- scale_magnitude: analogical energy comparisons (as much energy as New York)
- sovereignty_framing: American patriotic patterns (America's future)
- anonymous_authority: singular "a person familiar with" (was only "people familiar")
- source extraction: corporate title words (Vice, Deputy, Chief) as stop words
  preventing "Vice President" from being mis-parsed as a person name
"""

import pathlib
import unittest

from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sources import extract_sources

_ARTICLE_PATH = (
    pathlib.Path(__file__).resolve().parent.parent
    / "examples"
    / "sample_output"
    / "washexaminer_meta_louisiana_datacenter_50b_2026_07_13_article.txt"
)


def _load_article() -> str:
    return _ARTICLE_PATH.read_text()


class TestScaleMagnitudePhysicalUnits(unittest.TestCase):
    """Physical-unit scale_magnitude patterns added Jul 13 2026."""

    def setUp(self):
        self.devices = detect_framing_devices(_load_article())
        self.scale_mags = [d for d in self.devices if d.device_type == "scale_magnitude"]
        self.evidence_texts = [d.evidence_text for d in self.scale_mags]

    def test_million_square_foot_detected(self):
        """'10 million-square-foot' should trigger scale_magnitude."""
        assert any("million-square-foot" in e for e in self.evidence_texts), (
            f"Expected 'million-square-foot' in scale_magnitude evidence, "
            f"got: {self.evidence_texts}"
        )

    def test_five_gigawatt_detected(self):
        """'five-gigawatt' should trigger scale_magnitude."""
        assert any("five-gigawatt" in e for e in self.evidence_texts), (
            f"Expected 'five-gigawatt' in scale_magnitude evidence, "
            f"got: {self.evidence_texts}"
        )

    def test_as_much_energy_as_new_york(self):
        """'as much energy as New York' should trigger scale_magnitude."""
        assert any("as much energy as New York" in e for e in self.evidence_texts), (
            f"Expected 'as much energy as New York' in scale_magnitude evidence, "
            f"got: {self.evidence_texts}"
        )


class TestSovereigntyFramingAmericanPatriotic(unittest.TestCase):
    """American patriotic sovereignty_framing patterns added Jul 13 2026."""

    def setUp(self):
        self.devices = detect_framing_devices(_load_article())
        self.sov = [d for d in self.devices if d.device_type == "sovereignty_framing"]

    def test_americas_future_detected(self):
        """'America's future' should trigger sovereignty_framing."""
        evidence_texts = [d.evidence_text for d in self.sov]
        assert any("America's future" in e or "Americas future" in e for e in evidence_texts), (
            f"Expected 'America's future' in sovereignty_framing evidence, "
            f"got: {evidence_texts}"
        )


class TestAnonymousAuthorityPersonFamiliar(unittest.TestCase):
    """Singular 'a person familiar with' anonymous_authority — Jul 13 2026."""

    def setUp(self):
        self.devices = detect_framing_devices(_load_article())
        self.anon = [d for d in self.devices if d.device_type == "anonymous_authority"]

    def test_a_person_familiar_with_detected(self):
        """'A person familiar with' (singular) should trigger anonymous_authority."""
        evidence_texts = [d.evidence_text for d in self.anon]
        assert any("person familiar with" in e.lower() for e in evidence_texts), (
            f"Expected 'person familiar with' in anonymous_authority evidence, "
            f"got: {evidence_texts}"
        )


class TestAnonymousAuthorityIsolated(unittest.TestCase):
    """Regression: singular 'a person familiar with' must match in isolation."""

    def test_standalone_singular(self):
        text = "A person familiar with the deal told reporters it was finalized."
        devices = detect_framing_devices(text)
        anon = [d for d in devices if d.device_type == "anonymous_authority"]
        assert len(anon) >= 1, (
            f"Expected anonymous_authority for 'A person familiar with', "
            f"got: {[d.device_type for d in devices]}"
        )


class TestSourceExtractionVicePresidentFix(unittest.TestCase):
    """Corporate title stop-words preventing 'Vice President' as person name."""

    def setUp(self):
        self.sources = extract_sources(_load_article())

    def test_rachel_peterson_single_entry(self):
        """Rachel Peterson should appear exactly once, not split by title."""
        peterson_entries = [s for s in self.sources if "Peterson" in s.name]
        assert len(peterson_entries) == 1, (
            f"Expected 1 Peterson entry, got {len(peterson_entries)}: "
            f"{[s.name for s in peterson_entries]}"
        )

    def test_no_vice_president_as_name(self):
        """'Vice President' should never appear as a source name."""
        names = [s.name for s in self.sources]
        assert "Vice President" not in names, (
            f"'Vice President' should be filtered by _NAME_STOP_FIRST_WORDS, "
            f"but found in source names: {names}"
        )


class TestPhysicalUnitIsolated(unittest.TestCase):
    """Regression tests for physical-unit scale_magnitude in isolation."""

    def _check(self, text: str, expected_in_evidence: str):
        devices = detect_framing_devices(text)
        scale = [d for d in devices if d.device_type == "scale_magnitude"]
        evidence = [d.evidence_text for d in scale]
        assert any(expected_in_evidence in e for e in evidence), (
            f"Expected '{expected_in_evidence}' in scale_magnitude for "
            f"'{text[:60]}...', got: {evidence}"
        )

    def test_million_square_foot(self):
        self._check(
            "The facility spans 10 million-square-foot of land.",
            "million-square-foot",
        )

    def test_billion_gallons(self):
        self._check(
            "The plant processes 2.5 billion gallons of water annually.",
            "billion gallons",
        )

    def test_five_gigawatt(self):
        self._check(
            "A five-gigawatt power plant was proposed for the site.",
            "five-gigawatt",
        )

    def test_enough_to_power_homes(self):
        self._check(
            "The plant generates enough to power 4 million homes.",
            "enough to power 4 million homes",
        )

    def test_as_much_energy_as_city(self):
        self._check(
            "It consumes as much energy as Los Angeles in a year.",
            "as much energy as Los Angeles",
        )


class TestSovereigntyIsolated(unittest.TestCase):
    """Regression tests for American sovereignty patterns in isolation."""

    def _check(self, text: str, expected_in_evidence: str):
        devices = detect_framing_devices(text)
        sov = [d for d in devices if d.device_type == "sovereignty_framing"]
        evidence = [d.evidence_text for d in sov]
        assert any(expected_in_evidence in e for e in evidence), (
            f"Expected '{expected_in_evidence}' in sovereignty_framing for "
            f"'{text[:60]}...', got: {evidence}"
        )

    def test_americas_future(self):
        self._check(
            "This investment secures America's future in AI leadership.",
            "America's future",
        )

    def test_our_nations_competitiveness(self):
        self._check(
            "We must protect our nation's competitiveness in technology.",
            "our nation's competitiveness",
        )

    def test_helping_nation_compete(self):
        self._check(
            "This is about helping the nation compete and lead globally.",
            "helping the nation compete",
        )


if __name__ == "__main__":
    unittest.main()
