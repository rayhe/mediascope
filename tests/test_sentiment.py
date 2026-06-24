"""Tests for sentiment analysis module."""

import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mediascope.analyze.sentiment import (
    SentimentResult,
    analyze_vader,
    analyze_textblob,
    analyze_composite,
    count_anonymous_sources,
    measure_speculative_language,
    _compute_framing_correction,
    _measure_source_authority_v2,
)


class TestAnalyzeVader:
    def test_positive_text(self):
        result = analyze_vader("This is an excellent product with amazing features.")
        assert result["compound"] > 0

    def test_negative_text(self):
        result = analyze_vader("This is a terrible failure with disastrous consequences.")
        assert result["compound"] < 0

    def test_neutral_text(self):
        result = analyze_vader("The company reported quarterly earnings today.")
        assert -0.3 < result["compound"] < 0.3

    def test_empty_text(self):
        result = analyze_vader("")
        assert result["compound"] == 0.0


class TestAnalyzeTextblob:
    def test_positive_text(self):
        result = analyze_textblob("This is a wonderful and beautiful achievement.")
        assert result["polarity"] > 0

    def test_negative_text(self):
        result = analyze_textblob("This is an ugly and terrible disaster.")
        assert result["polarity"] < 0

    def test_returns_subjectivity(self):
        result = analyze_textblob("I think this is amazing!")
        assert "subjectivity" in result
        assert 0.0 <= result["subjectivity"] <= 1.0


class TestAnalyzeComposite:
    def test_returns_sentiment_result(self):
        result = analyze_composite("Meta announced new AI features today.")
        assert isinstance(result, SentimentResult)

    def test_all_dimensions_present(self):
        result = analyze_composite(
            "Meta's privacy practices drew criticism from advocates.",
            "Meta Faces Privacy Backlash"
        )
        assert hasattr(result, "overall_tone")
        assert hasattr(result, "emotional_language_intensity")
        assert hasattr(result, "source_authority_framing")
        assert hasattr(result, "agency_attribution")
        assert hasattr(result, "headline_body_alignment")
        assert hasattr(result, "anonymous_source_ratio")
        assert hasattr(result, "speculative_language_ratio")
        assert hasattr(result, "comparative_framing")

    def test_tone_range(self):
        result = analyze_composite("This is extremely negative terrible horrible text.")
        assert -1.0 <= result.overall_tone <= 1.0

    def test_intensity_range(self):
        result = analyze_composite("Shocking devastating catastrophic failure!")
        assert 0.0 <= result.emotional_language_intensity <= 1.0

    def test_negative_article_scores_negative(self):
        text = (
            "Meta's reckless behavior has drawn widespread criticism. "
            "The company claimed it takes privacy seriously, but insiders "
            "admitted the practices were harmful. Critics blasted the company "
            "for its failure to protect users."
        )
        result = analyze_composite(text, "Meta Blasted for Privacy Failures")
        assert result.overall_tone < 0, "Negative article should score negative"


class TestCountAnonymousSources:
    def test_detects_anonymous_sources(self):
        text = (
            "According to sources familiar with the matter, the deal is expected "
            "to close next month. People who requested anonymity said the price "
            "was around $1 billion. John Smith confirmed the timeline."
        )
        anon, total = count_anonymous_sources(text)
        assert anon >= 2, "Should detect at least 2 anonymous sources"
        assert total >= 3, "Should detect at least 3 total sources"

    def test_no_anonymous_sources(self):
        text = (
            "CEO Jane Doe said the company is expanding. "
            "CFO Bob Smith told reporters that revenue grew 20%."
        )
        anon, total = count_anonymous_sources(text)
        assert anon == 0, "Should find no anonymous sources"

    def test_empty_text(self):
        anon, total = count_anonymous_sources("")
        assert anon == 0
        assert total == 0


class TestMeasureSpeculativeLanguage:
    def test_speculative_text(self):
        text = (
            "The deal could potentially reshape the industry. "
            "It might lead to significant changes. Sources reportedly "
            "said the company may be considering a merger."
        )
        ratio = measure_speculative_language(text)
        assert ratio > 0.0, "Speculative text should have non-zero ratio"

    def test_definitive_text(self):
        text = (
            "The company reported $10 billion in revenue. "
            "The CEO stated that operations will continue as planned. "
            "The board approved the acquisition unanimously."
        )
        ratio = measure_speculative_language(text)
        assert ratio < 0.3, "Definitive text should have low speculative ratio"

    def test_empty_text(self):
        ratio = measure_speculative_language("")
        assert ratio == 0.0


class TestFramingCorrection:
    """Tests for the framing-aware tone correction that overrides VADER
    when investigative journalism produces false-positive sentiment."""

    def test_no_correction_when_raw_negative(self):
        """When raw tone is already negative, correction does not fire."""
        tone, corrected = _compute_framing_correction(
            raw_tone=-0.5,
            agency=-1.0,
            emotional_intensity=1.0,
            framing_summary={"loaded_language": 10, "timeline_implication": 5},
        )
        assert tone == -0.5
        assert corrected is False

    def test_no_correction_without_framing_devices(self):
        """Positive raw tone without adversarial framing is not corrected."""
        tone, corrected = _compute_framing_correction(
            raw_tone=0.5,
            agency=-0.5,
            emotional_intensity=0.5,
            framing_summary={"loaded_language": 1},  # Below threshold of 3
        )
        assert tone == 0.5
        assert corrected is False

    def test_no_correction_with_positive_agency(self):
        """Positive agency (subject framed as active/powerful) blocks correction."""
        tone, corrected = _compute_framing_correction(
            raw_tone=0.5,
            agency=0.2,  # Positive — not adversarial
            emotional_intensity=0.5,
            framing_summary={"loaded_language": 10},
        )
        assert tone == 0.5
        assert corrected is False

    def test_correction_fires_on_adversarial_framing(self):
        """Positive raw + adversarial framing triggers correction to negative."""
        tone, corrected = _compute_framing_correction(
            raw_tone=0.6,
            agency=-1.0,
            emotional_intensity=0.4,
            framing_summary={"loaded_language": 6, "timeline_implication": 2},
        )
        assert corrected is True
        assert tone < 0, f"Expected negative corrected tone, got {tone}"
        assert -1.0 <= tone <= 0.0

    def test_correction_proportional_to_agency(self):
        """Stronger adversarial agency produces more negative correction."""
        _, _ = _compute_framing_correction(  # Suppress lint
            raw_tone=0.5,
            agency=-0.4,
            emotional_intensity=0.5,
            framing_summary={"loaded_language": 5},
        )
        tone_weak, _ = _compute_framing_correction(
            raw_tone=0.5,
            agency=-0.4,
            emotional_intensity=0.5,
            framing_summary={"loaded_language": 5},
        )
        tone_strong, _ = _compute_framing_correction(
            raw_tone=0.5,
            agency=-1.0,
            emotional_intensity=0.5,
            framing_summary={"loaded_language": 5},
        )
        assert tone_strong < tone_weak, (
            f"Stronger agency ({tone_strong}) should be more negative "
            f"than weaker ({tone_weak})"
        )

    def test_correction_proportional_to_emotional_intensity(self):
        """Higher emotional intensity produces more negative correction."""
        tone_low_emotion, _ = _compute_framing_correction(
            raw_tone=0.5,
            agency=-0.8,
            emotional_intensity=0.1,
            framing_summary={"loaded_language": 5},
        )
        tone_high_emotion, _ = _compute_framing_correction(
            raw_tone=0.5,
            agency=-0.8,
            emotional_intensity=1.0,
            framing_summary={"loaded_language": 5},
        )
        assert tone_high_emotion < tone_low_emotion

    def test_real_investigative_article_scores_negative(self):
        """Integration: a real adversarial investigative article should
        score negative overall after framing correction."""
        text = (
            "Code discreetly added to Meta's app over multiple updates "
            "this year shows that the feature, internally called NameTag, "
            "identifies people captured by the glasses' camera. "
            "The system was quietly embedded without disclosure. "
            "Security researchers who reviewed the code said the system "
            "was 'nearly ready to go.' Meta had publicly described facial "
            "recognition as something the company was still 'thinking through' "
            "before rolling anything out. However, the investigation shows "
            "code was already added as early as January — before Meta made "
            "its official comment. Meta was forced to respond to the "
            "investigation. The company declined to comment on the timeline "
            "discrepancy. A coalition of over 70 civil liberties organizations "
            "blasted Meta for its surveillance practices and demanded the "
            "company kill the facial recognition feature."
        )
        result = analyze_composite(text, "Meta Quietly Embedded Facial Recognition in AI App")
        assert result.overall_tone < 0, (
            f"Investigative article should score negative, got {result.overall_tone} "
            f"(raw: {result.raw_tone}, corrected: {result.framing_corrected})"
        )


class TestFramingCorrectionMetadata:
    """Verify the SentimentResult carries correction metadata."""

    def test_result_has_framing_fields(self):
        result = analyze_composite("Meta announced new AI features today.")
        assert hasattr(result, "framing_corrected")
        assert hasattr(result, "raw_tone")

    def test_uncorrected_raw_equals_overall(self):
        """When no correction fires, raw_tone and overall_tone match."""
        result = analyze_composite("The company reported quarterly earnings today.")
        if not result.framing_corrected:
            assert result.raw_tone == result.overall_tone


class TestSourceAuthorityV2:
    """Tests for the improved source authority scoring that includes
    attribution verb stance analysis."""

    def test_loaded_verbs_lower_score(self):
        """Heavy use of loaded verbs should produce lower authority score."""
        # Neutral attribution
        neutral_text = (
            "John Smith said the project is on track. "
            "Jane Doe noted the team has expanded. "
            "Bob Jones explained the timeline."
        )
        # Loaded attribution
        loaded_text = (
            "John Smith claimed the project is on track. "
            "Jane Doe insisted the team has expanded. "
            "Bob Jones admitted the timeline slipped."
        )
        neutral_score = _measure_source_authority_v2(neutral_text)
        loaded_score = _measure_source_authority_v2(loaded_text)
        assert neutral_score > loaded_score, (
            f"Neutral verbs ({neutral_score}) should score higher than "
            f"loaded verbs ({loaded_score})"
        )

    def test_empty_text_returns_zero(self):
        assert _measure_source_authority_v2("") == 0.0


class TestPathCEmbeddedAnchorCorrection:
    """Tests for Path C: product reviews with positive agency but embedded
    adversarial anchor devices (kicker_framing, self_referential_investigation,
    juxtaposition) that shift the reader's final impression."""

    def test_wired_glasses_review_triggers_path_c(self):
        """The Wired glasses launch review (Jun 23) has positive agency (+0.67)
        but kicker_framing + self_referential_investigation + juxtaposition
        should trigger Path C correction."""
        import os
        article_path = os.path.join(
            os.path.dirname(__file__), "..",
            "examples", "sample_output",
            "wired_meta_glasses_launch_self_branded_2026_06_23_article.txt"
        )
        if not os.path.exists(article_path):
            import pytest
            pytest.skip("Article file not found")

        with open(article_path) as f:
            text = f.read()
        result = analyze_composite(text)

        # Path C should fire: corrected tone < raw tone
        assert result.framing_corrected, "Path C should have fired"
        assert result.overall_tone < result.raw_tone, (
            f"Corrected tone ({result.overall_tone}) should be less "
            f"than raw tone ({result.raw_tone})"
        )
        # Should still be positive (it IS partly a positive review)
        assert result.overall_tone > 0, (
            f"Corrected tone should stay positive, got {result.overall_tone}"
        )
        # But significantly less positive than raw
        assert result.overall_tone < 0.55, (
            f"Corrected tone ({result.overall_tone}) should be < 0.55"
        )

    def test_path_c_does_not_fire_on_negative_agency_article(self):
        """Articles with negative agency should use Path A/B, not Path C."""
        import os
        article_path = os.path.join(
            os.path.dirname(__file__), "..",
            "examples", "sample_output",
            "wired_meta_mci_data_exposure_2026_06_22_article.txt"
        )
        if not os.path.exists(article_path):
            import pytest
            pytest.skip("Article file not found")

        with open(article_path) as f:
            text = f.read()
        result = analyze_composite(text)

        # Path A should fire (negative agency), result should be negative
        assert result.framing_corrected, "Framing correction should fire"
        assert result.overall_tone < 0, (
            f"MCI article should have negative corrected tone, got {result.overall_tone}"
        )


class TestSelfReferentialInvestigation:
    """Tests for the self_referential_investigation framing device."""

    def test_detects_wired_discovered(self):
        """'WIRED discovered code' should be detected as
        self_referential_investigation."""
        from mediascope.analyze.framing import detect_framing_devices
        text = (
            "Earlier this month, WIRED discovered code in the public-facing "
            "Meta AI app, suggesting that Meta was gearing up to debut a "
            "face-recognition feature."
        )
        devices = detect_framing_devices(text)
        device_types = {d.device_type for d in devices}
        assert "self_referential_investigation" in device_types, (
            f"Expected 'self_referential_investigation' in {device_types}"
        )

    def test_detects_after_publication_report(self):
        """'After WIRED's report' should be detected."""
        from mediascope.analyze.framing import detect_framing_devices
        text = (
            "After WIRED's report, Meta deleted the code, and none of "
            "this technology is present in the new Meta Glasses."
        )
        devices = detect_framing_devices(text)
        device_types = {d.device_type for d in devices}
        assert "self_referential_investigation" in device_types, (
            f"Expected 'self_referential_investigation' in {device_types}"
        )

    def test_detects_guardian_learned(self):
        """'The Guardian has learned' should be detected."""
        from mediascope.analyze.framing import detect_framing_devices
        text = "The Guardian has learned that the company planned to expand."
        devices = detect_framing_devices(text)
        device_types = {d.device_type for d in devices}
        assert "self_referential_investigation" in device_types

    def test_detects_nyt_first_reported(self):
        """'The New York Times first reported' should be detected."""
        from mediascope.analyze.framing import detect_framing_devices
        text = "The New York Times first reported the internal program."
        devices = detect_framing_devices(text)
        device_types = {d.device_type for d in devices}
        assert "self_referential_investigation" in device_types

    def test_detects_our_investigation(self):
        """Reflexive 'our investigation' should be detected."""
        from mediascope.analyze.framing import detect_framing_devices
        text = "Our investigation found that the data was stored unencrypted."
        devices = detect_framing_devices(text)
        device_types = {d.device_type for d in devices}
        assert "self_referential_investigation" in device_types

    def test_no_false_positive_simple_mention(self):
        """Simple 'Wired reports' (no investigative verb) should NOT trigger."""
        from mediascope.analyze.framing import detect_framing_devices
        text = "Wired reports that Meta has launched new glasses."
        devices = detect_framing_devices(text)
        device_types = {d.device_type for d in devices}
        # 'reports' is not in the first pattern's verb list (it's in the
        # second pattern but only after 'as/after' prepositions)
        # Actually 'reported' IS in the list. Let me check.
        # The first pattern includes 'reported' as an investigative verb.
        # 'reports' (present tense) — let me check if the regex matches
        # both. The pattern uses (?:discovered|...reported...) which
        # matches 'reported' but not 'reports'.
        # So 'Wired reports' should NOT match.
        assert "self_referential_investigation" not in device_types, (
            "Simple 'Wired reports' should not trigger self_referential_investigation"
        )
