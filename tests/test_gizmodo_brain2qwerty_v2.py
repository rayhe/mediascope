"""Tests for Gizmodo Brain2Qwerty v2 false-positive suppression.

Validates four context-aware filters added during the Gizmodo Brain2Qwerty v2
article analysis (Jun 30, 2026 / Type A iteration Jul 2, 2026):

1. Catastrophizing: "nightmare" in dream/sleep narrative context → suppressed
2. Loaded language: "invasive" in medical/surgical context → suppressed
3. Emotional appeal: "unable to speak" as factual medical description → suppressed
4. Ironic quotation: definitional introduction with explanatory clause → suppressed

These filters prevent a false-positive framing correction on genuinely positive
medical/health technology articles.
"""

import pytest

from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sentiment import analyze_composite


# --- Gizmodo Brain2Qwerty v2 excerpts ---

NIGHTMARE_DREAM_CONTEXT = (
    "Most of us have at one point or another had a dream in which we were "
    "unable to speak or move; to wake up from such a nightmare—and to recall "
    "what it's like to be able to freely use your voice—feels like a liberation."
)

INVASIVE_MEDICAL_CONTEXT = (
    "patients suffering from anarthria, locked-in syndrome, amyotrophic "
    "lateral sclerosis (ALS), and other paralyzing neurodegenerative disorders "
    "are able to communicate via thought without the need for neuroprosthetics, "
    "which typically require extremely invasive, complex, and expensive "
    "brain surgery."
)

NONINVASIVE_CONTEXT = (
    "Brain2Qwerty v2, its latest effort to translate noisy brain activity "
    "into coherent text: think of it like a rudimentary form of "
    "algorithmically mediated mind-reading. While the research is still in "
    "its early stages, non-invasive brain-computer interfaces offer a "
    "glimpse of a perhaps not-so-distant future."
)

AUTO_RESEARCH_DEFINITIONAL = (
    'Brain2Qwerty also relies upon a contingent of "auto-research" AI agents, '
    "whose task is to autonomously hone the decoding process in order to boost "
    "its accuracy and efficiency; think of them like worker bees continually "
    "making structural refinements to the hive."
)


class TestCatastrophizingDreamContext:
    """'nightmare' in dream/sleep narrative → NOT catastrophizing."""

    def test_nightmare_in_dream_suppressed(self):
        devices = detect_framing_devices(NIGHTMARE_DREAM_CONTEXT)
        cat_devices = [d for d in devices if d.device_type == "catastrophizing"]
        assert len(cat_devices) == 0, (
            f"'nightmare' in dream context should be suppressed; got: "
            f"{[d.evidence_text for d in cat_devices]}"
        )

    def test_nightmare_without_dream_context_fires(self):
        """'nightmare' outside dream/sleep context should still fire."""
        text = (
            "The latest data breach has become a nightmare for Meta, "
            "exposing millions of user records."
        )
        devices = detect_framing_devices(text)
        cat_devices = [d for d in devices if d.device_type == "catastrophizing"]
        assert len(cat_devices) >= 1, (
            "'nightmare' without dream context should still fire as catastrophizing"
        )

    def test_nightmarish_in_dream_suppressed(self):
        text = (
            "She fell asleep and had a dream—a nightmarish vision of "
            "being trapped, unable to call for help."
        )
        devices = detect_framing_devices(text)
        cat_devices = [d for d in devices if d.device_type == "catastrophizing"]
        assert len(cat_devices) == 0


class TestLoadedLanguageMedicalContext:
    """'invasive' in medical/surgical context → NOT loaded language."""

    def test_invasive_surgery_suppressed(self):
        devices = detect_framing_devices(INVASIVE_MEDICAL_CONTEXT)
        ll_devices = [
            d for d in devices
            if d.device_type == "loaded_language" and "invasive" in d.evidence_text.lower()
        ]
        assert len(ll_devices) == 0, (
            f"'invasive' in medical context should be suppressed; got: "
            f"{[d.evidence_text for d in ll_devices]}"
        )

    def test_noninvasive_bci_suppressed(self):
        devices = detect_framing_devices(NONINVASIVE_CONTEXT)
        ll_devices = [
            d for d in devices
            if d.device_type == "loaded_language" and "invasive" in d.evidence_text.lower()
        ]
        assert len(ll_devices) == 0

    def test_invasive_surveillance_fires(self):
        """'invasive' in surveillance/privacy context should still fire."""
        text = (
            "The company's invasive tracking practices have drawn criticism "
            "from privacy advocates, who call the data collection dystopian."
        )
        devices = detect_framing_devices(text)
        ll_devices = [
            d for d in devices
            if d.device_type == "loaded_language" and "invasive" in d.evidence_text.lower()
        ]
        assert len(ll_devices) >= 1, (
            "'invasive' in surveillance/privacy context should still fire"
        )


class TestEmotionalAppealMedicalCondition:
    """'unable to speak' as factual medical description → NOT emotional appeal."""

    def test_unable_to_speak_medical_suppressed(self):
        devices = detect_framing_devices(NIGHTMARE_DREAM_CONTEXT)
        ea_devices = [
            d for d in devices
            if d.device_type == "emotional_appeal" and "unable" in d.evidence_text.lower()
        ]
        assert len(ea_devices) == 0, (
            f"'unable to speak' in medical context should be suppressed; got: "
            f"{[d.evidence_text for d in ea_devices]}"
        )

    def test_unable_to_speak_bci_article(self):
        """Full BCI research context with factual condition description."""
        text = (
            "The brain-computer interface is designed for patients with ALS "
            "and locked-in syndrome who are unable to speak due to "
            "progressive neuromuscular degeneration."
        )
        devices = detect_framing_devices(text)
        ea_devices = [
            d for d in devices
            if d.device_type == "emotional_appeal" and "unable" in d.evidence_text.lower()
        ]
        assert len(ea_devices) == 0

    def test_unable_to_speak_editorial_fires(self):
        """'unable to speak' in editorial coercion context should still fire."""
        text = (
            "The whistleblower, shaking, was unable to speak during the "
            "Senate hearing as Meta's lawyers filed yet another injunction."
        )
        devices = detect_framing_devices(text)
        ea_devices = [
            d for d in devices
            if d.device_type == "emotional_appeal" and "unable" in d.evidence_text.lower()
        ]
        assert len(ea_devices) >= 1, (
            "'unable to speak' in editorial coercion context should still fire"
        )


class TestIronicQuotationDefinitional:
    """Coined terms with definitional clause → NOT ironic quotation."""

    def test_auto_research_definitional_suppressed(self):
        devices = detect_framing_devices(AUTO_RESEARCH_DEFINITIONAL)
        iq_devices = [d for d in devices if d.device_type == "ironic_quotation"]
        assert len(iq_devices) == 0, (
            f"'auto-research' with definitional 'whose' should be suppressed; got: "
            f"{[d.evidence_text for d in iq_devices]}"
        )

    def test_coined_term_which_suppressed(self):
        text = (
            'Meta calls them "alignment agents", which are designed to '
            "monitor and correct model outputs in real time."
        )
        devices = detect_framing_devices(text)
        iq_devices = [d for d in devices if d.device_type == "ironic_quotation"]
        assert len(iq_devices) == 0

    def test_scare_quotes_after_sentence_break_fires(self):
        """Quoted term followed by sentence break + 'which' = NOT definitional."""
        text = (
            'Meta\'s "points" are meaningless tokens. Which suggests that '
            "the company wants to avoid gambling regulations."
        )
        devices = detect_framing_devices(text)
        iq_devices = [d for d in devices if d.device_type == "ironic_quotation"]
        assert len(iq_devices) >= 1, (
            "Scare quotes with cross-sentence 'Which' should still fire"
        )


class TestFramingCorrectionFalsePositive:
    """Genuinely positive medical article should NOT trigger framing correction."""

    def test_positive_article_not_corrected(self):
        """Gizmodo Brain2Qwerty v2: genuinely positive medical tech article."""
        text = open(
            "examples/sample_output/"
            "gizmodo_meta_brain2qwerty_v2_2026_06_30_article.txt"
        ).read()
        body = text.split("---", 1)[1].strip() if "---" in text else text
        headline = (
            "Meta's AI Is Getting Better at Reading Your Thoughts—"
            "Without Cracking Open Your Skull"
        )
        result = analyze_composite(body, headline=headline)
        assert not result.framing_corrected, (
            f"Framing correction should NOT fire on genuinely positive article; "
            f"overall_tone={result.overall_tone}, raw_tone={result.raw_tone}"
        )
        assert result.overall_tone > 0.4, (
            f"Overall tone should be positive (>0.4) for this article; "
            f"got {result.overall_tone}"
        )
