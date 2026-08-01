"""Test framing device detection for Gizmodo article on Meta smart glasses
harassment Instagram ban (Jul 23, 2026).

Article: "Meta Toes the Line on Smart Glasses Harassment With New Instagram Ban"
Author: Raymond Wong
Source: Gizmodo (Keleops AG, Swiss-owned — ZERO Condé Nast connection)

Significance: Control-case convergence article — Gizmodo produces framing
devices nearly identical to WIRED coverage despite no financial incentive
connection, supporting the hypothesis of editorial escape velocity in the
anti-glasses narrative.

This article drove 5 new regex patterns:
- escalation_amplification Pattern 8: "reached entirely new heights"
- escalation_amplification Pattern 9: "reached a fever pitch"
- recidivism_framing: "[Entity]'s always been good at [negative]"
- recidivism_framing: "We can expect plenty more [negative noun]"
- editorial_aside: parenthetical "meanwhile" contrast
"""

from pathlib import Path

import pytest

from mediascope.analyze.framing import detect_framing_devices

_ARTICLE_PATH = (
    Path(__file__).resolve().parent.parent
    / "examples"
    / "sample_output"
    / "gizmodo_meta_glasses_harassment_instagram_ban_2026_07_23_article.txt"
)

_TEXT = _ARTICLE_PATH.read_text()


def _device_types(text: str = _TEXT) -> list[str]:
    return [d.device_type for d in detect_framing_devices(text, source_publication="gizmodo")]


def _device_evidence(text: str = _TEXT) -> list[tuple[str, str]]:
    return [
        (d.device_type, d.evidence_text)
        for d in detect_framing_devices(text, source_publication="gizmodo")
    ]


class TestGizmodoGlassesHarassmentBan:
    """Framing device detection for Gizmodo Jul 23 glasses harassment ban article."""

    def test_total_device_count(self):
        """Article should detect at least 14 framing devices (8 distinct types)."""
        types = _device_types()
        assert len(types) >= 14, f"Expected ≥14 devices, got {len(types)}: {types}"

    def test_distinct_device_types(self):
        """At least 7 distinct framing device types should be detected."""
        types = set(_device_types())
        assert len(types) >= 7, f"Expected ≥7 types, got {len(types)}: {types}"

    def test_loaded_language_detected(self):
        """Multiple loaded language instances should be detected."""
        loaded = [t for t in _device_types() if t == "loaded_language"]
        assert len(loaded) >= 5, (
            f"Expected ≥5 loaded_language, got {len(loaded)}"
        )

    def test_pervert_loaded_language(self):
        """'pervert' should be detected as loaded_language."""
        evidence = _device_evidence()
        pervert_hits = [
            ev for dtype, ev in evidence
            if dtype == "loaded_language" and "pervert" in ev.lower()
        ]
        assert pervert_hits, "Expected 'pervert' to be caught as loaded_language"

    def test_consent_alarm(self):
        """'without their permission' should trigger consent_alarm."""
        types = _device_types()
        assert "consent_alarm" in types

    def test_safeguard_inadequacy(self):
        """LED light workaround framing should trigger safeguard_inadequacy."""
        evidence = _device_evidence()
        safeguard_hits = [
            ev for dtype, ev in evidence
            if dtype == "safeguard_inadequacy" and "recording light" in ev.lower()
        ]
        assert safeguard_hits, "Expected safeguard_inadequacy for LED workaround"

    def test_surveillance_creep(self):
        """'record everything all the time' should trigger surveillance_creep."""
        evidence = _device_evidence()
        surveillance_hits = [
            ev for dtype, ev in evidence
            if dtype == "surveillance_creep" and "record everything" in ev.lower()
        ]
        assert surveillance_hits, "Expected surveillance_creep for 'record everything all the time'"


class TestNewPatterns:
    """Validate the 5 new patterns discovered from this article."""

    def test_escalation_reached_new_heights(self):
        """'reached entirely new heights' should trigger escalation_amplification."""
        evidence = _device_evidence()
        hits = [
            ev for dtype, ev in evidence
            if dtype == "escalation_amplification" and "new heights" in ev.lower()
        ]
        assert hits, "Expected escalation_amplification for 'reached entirely new heights'"

    def test_escalation_reached_new_heights_variants(self):
        """Escalation pattern should match related phrasings."""
        for phrase in [
            "backlash has reached entirely new heights",
            "concerns have hit unprecedented levels",
            "outrage has climbed to historic proportions",
            "anxiety has reached all-time highs",
            "criticism has soared to new levels",
        ]:
            devices = detect_framing_devices(phrase)
            types = [d.device_type for d in devices]
            assert "escalation_amplification" in types, (
                f"escalation_amplification should match: '{phrase}'"
            )

    def test_fever_pitch_variant(self):
        """'reached a fever pitch' should trigger escalation_amplification."""
        devices = detect_framing_devices("public anger has reached a fever pitch over smart glasses")
        types = [d.device_type for d in devices]
        assert "escalation_amplification" in types

    def test_recidivism_always_been_good_at(self):
        """Sardonic 'always been good at' should trigger recidivism_framing."""
        evidence = _device_evidence()
        hits = [
            ev for dtype, ev in evidence
            if dtype == "recidivism_framing" and "always been good at" in ev.lower()
        ]
        assert hits, "Expected recidivism_framing for 'Meta's always been good at'"

    def test_recidivism_predictive_mixed_messaging(self):
        """'We can expect plenty more mixed messaging' should trigger recidivism_framing."""
        evidence = _device_evidence()
        hits = [
            ev for dtype, ev in evidence
            if dtype == "recidivism_framing" and "expect" in ev.lower()
        ]
        assert hits, "Expected recidivism_framing for predictive mixed messaging closing"

    def test_editorial_aside_meanwhile_parenthetical(self):
        """Parenthetical '(X, meanwhile, ...)' should trigger editorial_aside."""
        evidence = _device_evidence()
        hits = [
            ev for dtype, ev in evidence
            if dtype == "editorial_aside" and "meanwhile" in ev.lower()
        ]
        assert hits, "Expected editorial_aside for '(Kylie Jenner, meanwhile, ...)'"

    def test_editorial_aside_meanwhile_standalone(self):
        """The parenthetical meanwhile pattern should work on standalone text."""
        text = "(Apple, meanwhile, is taking a very different approach to privacy.)"
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_aside" in types, (
            "parenthetical 'meanwhile' pattern should match standalone text"
        )

    def test_no_false_positive_meanwhile_without_parens(self):
        """'meanwhile' without parentheses should not trigger the aside pattern."""
        text = "Meta, meanwhile, continues to push smart glasses sales."
        devices = detect_framing_devices(text)
        aside_hits = [
            d for d in devices if d.device_type == "editorial_aside"
            and "meanwhile" in d.evidence_text.lower()
        ]
        assert not aside_hits, (
            "Non-parenthetical 'meanwhile' should not trigger editorial_aside"
        )
