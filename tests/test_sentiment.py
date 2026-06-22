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
