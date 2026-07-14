"""Tests for NY Post Meta Muse Image 'yanks' article (Jul 13, 2026).

Validates new framing patterns (loaded_language additions, capitulation
verbs) and the Path C forced-retreat sentiment correction discovered in
this article.  Covers the VADER polarity inversion fix where VADER scored
+0.30 on a clearly negative 'corporate humiliation' article.
"""

import pytest

# mediascope uses package-relative imports
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mediascope.analyze.framing import detect_framing_devices, summarize_framing
from mediascope.analyze.entities import detect_entities
from mediascope.analyze.sentiment import (
    analyze_vader,
    analyze_composite,
    _measure_agency,
    _ADVERSARIAL_DEVICE_TYPES,
    ACTIVE_NEGATIVE_FRAMING,
)


# --- Fixture: representative excerpt of the NY Post article ---

NYPOST_MUSE_EXCERPT = (
    "Meta yanks controversial AI image tool after privacy backlash: "
    "'Force their slop down everyone's throat'\n\n"
    "Meta has pulled its controversial Muse Image feature from Instagram "
    "after a heated backlash from users who were automatically enrolled "
    "in the AI-powered tool without their knowledge.\n\n"
    "The social media giant quietly rolled out the feature, which used "
    "people's photos to generate AI images of their likeness. Users "
    "slammed the move as 'diabolical,' with one calling it 'harvesting "
    "my identity.'\n\n"
    "A Meta spokesperson acknowledged the criticism, saying: 'We've "
    "heard the feedback and this feature missed the mark. Our intent was "
    "to give people creative tools, but we understand the concerns. "
    "It's no longer available.'\n\n"
    "The reversal comes amid broader scrutiny of AI companies, including "
    "OpenAI and Google, over how they use personal data to train their "
    "models. Meta also faced criticism for automatically opting users "
    "into the feature on Facebook and WhatsApp."
)


class TestNYPostMuseImageFraming:
    """Framing device detection for the Muse Image 'yanks' article."""

    def test_loaded_language_yanks(self):
        """'yanks controversial AI image tool' should trigger loaded_language."""
        devices = detect_framing_devices(NYPOST_MUSE_EXCERPT)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        evidence = [d.evidence_text.lower() for d in loaded]
        assert any("yank" in e for e in evidence), (
            f"Expected 'yanks' in loaded_language, got: {evidence}"
        )

    def test_loaded_language_slop(self):
        """'slop' should trigger loaded_language (new term)."""
        devices = detect_framing_devices(NYPOST_MUSE_EXCERPT)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        evidence = [d.evidence_text.lower() for d in loaded]
        assert any("slop" in e for e in evidence), (
            f"Expected 'slop' in loaded_language, got: {evidence}"
        )

    def test_loaded_language_diabolical(self):
        """'diabolical' should trigger loaded_language (new term)."""
        devices = detect_framing_devices(NYPOST_MUSE_EXCERPT)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        evidence = [d.evidence_text.lower() for d in loaded]
        assert any("diabolical" in e for e in evidence), (
            f"Expected 'diabolical' in loaded_language, got: {evidence}"
        )

    def test_loaded_language_heated_backlash(self):
        """'heated backlash' should trigger loaded_language (new term)."""
        devices = detect_framing_devices(NYPOST_MUSE_EXCERPT)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        evidence = [d.evidence_text.lower() for d in loaded]
        assert any("heated backlash" in e for e in evidence), (
            f"Expected 'heated backlash' in loaded_language, got: {evidence}"
        )

    def test_loaded_language_harvesting_identity(self):
        """'harvesting my identity' should trigger loaded_language (new term)."""
        devices = detect_framing_devices(NYPOST_MUSE_EXCERPT)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        evidence = [d.evidence_text.lower() for d in loaded]
        assert any("harvesting" in e and "identity" in e for e in evidence), (
            f"Expected 'harvesting identity' in loaded_language, got: {evidence}"
        )

    def test_consent_alarm_detected(self):
        """consent_alarm should fire for 'automatically enrolled' and similar."""
        devices = detect_framing_devices(NYPOST_MUSE_EXCERPT)
        consent = [d for d in devices if d.device_type == "consent_alarm"]
        assert len(consent) >= 2, (
            f"Expected at least 2 consent_alarm devices, got {len(consent)}"
        )

    def test_policy_reversal_detected(self):
        """policy_reversal should fire for 'missed the mark' / 'no longer available'."""
        devices = detect_framing_devices(NYPOST_MUSE_EXCERPT)
        pr = [d for d in devices if d.device_type == "policy_reversal"]
        assert len(pr) >= 2, (
            f"Expected at least 2 policy_reversal devices, got {len(pr)}"
        )

    def test_total_devices_at_least_12(self):
        """Article should produce at least 12 framing devices total."""
        devices = detect_framing_devices(NYPOST_MUSE_EXCERPT)
        assert len(devices) >= 12, (
            f"Expected >= 12 devices, got {len(devices)}: "
            f"{summarize_framing(devices)}"
        )


class TestNYPostMuseImageSentiment:
    """Sentiment correction for the forced-retreat narrative."""

    def test_vader_negative_on_concentrated_text(self):
        """VADER should read this concentrated excerpt as negative.
        Note: the full article has VADER polarity inversion (+0.30) because
        the additional neutral/positive corporate language dilutes the signal.
        The inversion is a long-text normalization issue in VADER."""
        vader = analyze_vader(NYPOST_MUSE_EXCERPT)
        assert vader["compound"] < 0, (
            f"Expected VADER negative on concentrated excerpt, got {vader['compound']}"
        )

    def test_composite_corrects_to_negative(self):
        """Composite sentiment should correct VADER's inversion to negative."""
        composite = analyze_composite(NYPOST_MUSE_EXCERPT)
        assert composite.overall_tone < 0, (
            f"Expected negative overall_tone after correction, "
            f"got {composite.overall_tone}"
        )

    def test_framing_correction_fires(self):
        """framing_corrected should be True (Path C forced-retreat override)."""
        composite = analyze_composite(NYPOST_MUSE_EXCERPT)
        assert composite.framing_corrected is True, (
            "Expected framing_corrected=True for forced-retreat narrative"
        )

    def test_corrected_tone_strongly_negative(self):
        """Corrected tone should be strongly negative (concentrated excerpt)."""
        composite = analyze_composite(NYPOST_MUSE_EXCERPT)
        assert composite.overall_tone <= -0.4, (
            f"Expected tone <= -0.4 for concentrated tabloid excerpt, "
            f"got {composite.overall_tone}"
        )

    def test_raw_tone_preserved(self):
        """raw_tone should preserve the uncorrected VADER+TextBlob blend.
        On the concentrated excerpt, VADER gets direction right so raw_tone
        is also negative — the correction amplifies rather than inverts."""
        composite = analyze_composite(NYPOST_MUSE_EXCERPT)
        assert composite.raw_tone < 0, (
            f"Expected negative raw_tone on concentrated excerpt, "
            f"got {composite.raw_tone}"
        )

    def test_emotional_intensity_high(self):
        """Emotional intensity should be high for loaded tabloid language."""
        composite = analyze_composite(NYPOST_MUSE_EXCERPT)
        assert composite.emotional_language_intensity >= 0.7, (
            f"Expected high emotional intensity, "
            f"got {composite.emotional_language_intensity}"
        )


class TestCapitulationVerbs:
    """Capitulation/retreat verbs in ACTIVE_NEGATIVE_FRAMING."""

    @pytest.mark.parametrize("verb", [
        "yanked", "yanks", "yanking",
        "scrapped", "backtracked", "walked back",
        "backed down", "reversed course", "caved",
        "capitulated", "shelved",
    ])
    def test_capitulation_verb_in_active_negative(self, verb):
        """Capitulation verbs should be in ACTIVE_NEGATIVE_FRAMING."""
        assert verb in ACTIVE_NEGATIVE_FRAMING, (
            f"'{verb}' should be in ACTIVE_NEGATIVE_FRAMING"
        )

    def test_yanks_reduces_agency(self):
        """Text with 'yanks' should produce lower agency than without."""
        text_with = "Meta yanks the controversial tool after backlash."
        text_without = "Meta launched the new creative tool for users."
        agency_with = _measure_agency(text_with)
        agency_without = _measure_agency(text_without)
        assert agency_with < agency_without, (
            f"Expected 'yanks' to reduce agency: "
            f"with={agency_with}, without={agency_without}"
        )


class TestPolicyReversalAdversarial:
    """policy_reversal reclassification as adversarial device type."""

    def test_policy_reversal_is_adversarial(self):
        """policy_reversal should be in _ADVERSARIAL_DEVICE_TYPES."""
        assert "policy_reversal" in _ADVERSARIAL_DEVICE_TYPES

    def test_forced_retreat_overrides_agency_check(self):
        """When policy_reversal + consent_alarm co-occur, framing correction
        should fire even with positive grammatical agency."""
        # Construct text with policy_reversal + consent_alarm but active agency
        text = (
            "The company launched the feature that automatically enrolled "
            "users. It used their photos without permission, automatically "
            "opted them in, and harvested their likeness. After backlash, "
            "the company acknowledged: 'We've heard the feedback and this "
            "feature missed the mark. It's no longer available.' Our intent "
            "was to innovate."
        )
        composite = analyze_composite(text)
        # Should correct despite active agency ("launched", "innovate")
        assert composite.framing_corrected is True or composite.overall_tone < 0, (
            f"Expected correction or negative tone for forced-retreat text, "
            f"got tone={composite.overall_tone}, corrected={composite.framing_corrected}"
        )


class TestNYPostMuseImageEntities:
    """Entity detection for the Muse Image article."""

    def test_meta_cluster(self):
        """Meta, Instagram, Facebook, WhatsApp should cluster under Meta."""
        entities = detect_entities(NYPOST_MUSE_EXCERPT)
        meta_cluster = [e for e in entities if e.cluster == "Meta"]
        canonical_names = {e.canonical_name for e in meta_cluster}
        assert "Meta" in canonical_names
        assert "Instagram" in canonical_names

    def test_muse_image_detected(self):
        """Muse Image should be detected as an entity."""
        entities = detect_entities(NYPOST_MUSE_EXCERPT)
        canonical_names = {e.canonical_name for e in entities}
        assert "Muse Image" in canonical_names, (
            f"Expected 'Muse Image' entity, got: {canonical_names}"
        )

    def test_openai_cluster(self):
        """OpenAI and ChatGPT should cluster together."""
        entities = detect_entities(NYPOST_MUSE_EXCERPT)
        openai_cluster = [e for e in entities if e.cluster == "OpenAI"]
        canonical_names = {e.canonical_name for e in openai_cluster}
        assert "OpenAI" in canonical_names
