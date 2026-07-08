"""
Regression tests for editorial deflation, rhetorical question, and latecomer
narrative patterns added during the iPhone-in-Canada Muse Image analysis
(2026-07-07, Type A iteration).

Discovery article: "Meta Is Adding AI Image Creation to Instagram, WhatsApp and More"
https://www.iphoneincanada.ca/2026/07/07/meta-is-adding-ai-image-creation-to-instagram-whatsapp-and-more/
"""

import re
import pytest
from mediascope.analyze.framing import _DEVICE_PATTERNS


class TestEditorialDeflationNewPatterns:
    """Tests for the 5 new editorial_deflation patterns."""

    patterns = _DEVICE_PATTERNS["editorial_deflation"]

    def _matches_any(self, text):
        """Return True if any editorial_deflation pattern matches text."""
        return any(p.search(text) for p in self.patterns)

    def test_better_late_than_never(self):
        """'Better late than never' idiom triggers editorial_deflation."""
        assert self._matches_any(
            "Better late than never, I guess, if you're seeking to use Meta AI."
        )

    def test_better_late_than_never_lowercase(self):
        """Case-insensitive 'better late than never'."""
        assert self._matches_any(
            "It's better late than never for this feature rollout."
        )

    def test_i_guess_hedge(self):
        """', I guess,' parenthetical hedge triggers editorial_deflation."""
        assert self._matches_any(
            "Better late than never, I guess, if you're seeking to use it."
        )

    def test_i_suppose_hedge(self):
        """', I suppose,' parenthetical hedge triggers editorial_deflation."""
        assert self._matches_any(
            "The update is welcome, I suppose, for those who want it."
        )

    def test_if_youre_seeking_to(self):
        """'if you're seeking to' conditional triggers editorial_deflation."""
        assert self._matches_any(
            "if you're seeking to use Meta AI to edit images in the company's apps"
        )

    def test_if_youre_even_seeking_to(self):
        """'if you're even seeking to' (with intensifier) triggers."""
        assert self._matches_any(
            "if you're even seeking to get value from this product"
        )

    def test_and_such_trailing_minimizer(self):
        """'and such' trailing minimizer triggers editorial_deflation."""
        assert self._matches_any(
            "Who's actually using AI to change their backgrounds to golden hour and such?"
        )

    def test_or_whatever_trailing_minimizer(self):
        """'or whatever' trailing minimizer triggers editorial_deflation."""
        assert self._matches_any(
            "They added filters and effects or whatever."
        )

    # --- False-positive guards ---

    def test_no_false_positive_neutral_product(self):
        """Neutral product description should not trigger editorial_deflation."""
        assert not self._matches_any(
            "Meta launched Muse Image, a new AI image generation model, across "
            "Instagram and WhatsApp today."
        )

    def test_no_false_positive_factual_feature(self):
        """Straightforward feature listing should not trigger."""
        assert not self._matches_any(
            "Users can describe an image in conversational language, restore an "
            "old family photo, or erase a photobomber."
        )


class TestRhetoricalQuestionNewPatterns:
    """Tests for the 2 new rhetorical_question contraction patterns."""

    patterns = _DEVICE_PATTERNS["rhetorical_question"]

    def _matches_any(self, text):
        return any(p.search(text) for p in self.patterns)

    def test_whos_actually_using(self):
        """'Who's actually using...' contraction rhetorical question."""
        assert self._matches_any(
            "Who's actually using AI to change their backgrounds to golden hour and such?"
        )

    def test_whos_actually_buying(self):
        """'Who's actually buying...' variant."""
        assert self._matches_any(
            "Who's actually buying these overpriced headsets?"
        )

    def test_whats_the_point_of(self):
        """'What's the point of...' contraction rhetorical question."""
        assert self._matches_any(
            "What's the point of adding another AI chatbot to the mix?"
        )

    # --- False-positive guards ---

    def test_no_false_positive_genuine_question(self):
        """A genuine information-seeking question should not trigger
        rhetorical_question (testing that our new patterns don't over-fire).
        Note: some genuine questions may still match broader existing patterns;
        this tests only that the new contraction patterns are reasonably scoped."""
        # Simple factual question without dismissive framing
        text = "What's the release date for the new model?"
        # This tests the "What's the point of" pattern specifically doesn't fire
        # on "What's the release date"
        whos_patterns = [p for p in self.patterns if "who" in p.pattern.lower() or "what.*point" in p.pattern.lower()]
        assert not any(p.search(text) for p in whos_patterns)


class TestLatecomerNarrativeNewPatterns:
    """Tests for the 2 new latecomer_narrative patterns."""

    patterns = _DEVICE_PATTERNS["latecomer_narrative"]

    def _matches_any(self, text):
        return any(p.search(text) for p in self.patterns)

    def test_saving_steps_from_jumping_back(self):
        """'saving you steps from jumping back from' implicit latecomer."""
        assert self._matches_any(
            "saving you steps from jumping back from other AI models such as "
            "those from Gemini and ChatGPT"
        )

    def test_saving_steps_from_switching_back(self):
        """'saving you steps from switching back from' variant."""
        assert self._matches_any(
            "saving you steps from switching back from competing services"
        )

    def test_other_ai_models_such_as(self):
        """'other AI models such as [X] and [Y]' competitor listing."""
        assert self._matches_any(
            "other AI models such as those from Gemini and ChatGPT"
        )

    def test_other_ai_models_like(self):
        """'other AI models like [X]' competitor listing variant."""
        assert self._matches_any(
            "other AI models like ChatGPT and Claude"
        )

    # --- False-positive guards ---

    def test_no_false_positive_neutral_comparison(self):
        """Neutral technical comparison should not trigger latecomer_narrative."""
        assert not self._matches_any(
            "The model performs comparably to Gemini on image generation benchmarks."
        )

    def test_no_false_positive_product_listing(self):
        """Simple product listing without latecomer framing should not trigger."""
        assert not self._matches_any(
            "Meta AI, Google Gemini, and ChatGPT all offer image generation features."
        )


class TestMuseImageArticleIntegration:
    """End-to-end integration: run the full article text through framing detection
    and verify the expected devices are found."""

    ARTICLE_CLOSING = (
        "Better late than never, I guess, if you're seeking to use Meta AI to "
        "edit images in the company's apps, saving you steps from jumping back "
        "from other AI models such as those from Gemini and ChatGPT. Who's "
        "actually using AI to change their backgrounds to golden hour and such?"
    )

    def test_closing_paragraph_device_count(self):
        """The closing paragraph should trigger at least 7 device matches
        across editorial_deflation, latecomer_narrative, and rhetorical_question."""
        matches = []
        for device_type in ("editorial_deflation", "latecomer_narrative", "rhetorical_question"):
            for p in _DEVICE_PATTERNS[device_type]:
                if p.search(self.ARTICLE_CLOSING):
                    matches.append(device_type)
        assert len(matches) >= 7, (
            f"Expected ≥7 device matches in closing paragraph, got {len(matches)}: {matches}"
        )

    def test_closing_paragraph_type_diversity(self):
        """The closing paragraph should trigger all 3 target device types."""
        types_found = set()
        for device_type in ("editorial_deflation", "latecomer_narrative", "rhetorical_question"):
            for p in _DEVICE_PATTERNS[device_type]:
                if p.search(self.ARTICLE_CLOSING):
                    types_found.add(device_type)
        assert types_found == {"editorial_deflation", "latecomer_narrative", "rhetorical_question"}, (
            f"Expected all 3 types, found: {types_found}"
        )
