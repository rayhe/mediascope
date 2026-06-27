"""Regression tests for fixes applied during Jun 27 2026 Type A iteration.

Tests:
  1. Topic "fine" ambiguity — "fine-tuned" should NOT match litigation topic
  2. Source extraction — "Any" should NOT be extracted as a person name
  3. Topic keyword precision — "fined" (unambiguous penalty) still matches
"""

import pytest

from mediascope.analyze.topics import classify_topic
from mediascope.analyze.sources import extract_sources


class TestTopicFineAmbiguity:
    """Verify 'fine' removal prevents false-positive litigation classification.

    The word 'fine' in the litigation topic keywords matched 'fine-tuned'
    via word-boundary regex (\\bfine\\b matches the 'fine' in 'fine-tuned'
    because the hyphen is a non-word character). Removing 'fine' and
    keeping 'fined' fixes this without losing penalty-sense coverage.
    """

    def test_fine_tuned_no_litigation(self):
        """Article about AI fine-tuning should NOT classify as litigation."""
        text = (
            "The model was fine-tuned on a diverse dataset. "
            "Fine-tuning is essential for adapting large language models. "
            "Researchers fine-tuned the system to be fine-grained."
        )
        topics = classify_topic(text)
        topic_names = {t.topic for t in topics}
        assert "litigation" not in topic_names

    def test_fined_still_matches_litigation(self):
        """'fined' (unambiguous penalty sense) should still classify as litigation."""
        text = (
            "The company was fined $400 million by EU regulators. "
            "The penalty followed a year-long investigation into "
            "anti-competitive practices and data protection violations."
        )
        topics = classify_topic(text)
        topic_names = {t.topic for t in topics}
        assert "litigation" in topic_names

    def test_adjective_fine_no_litigation(self):
        """'fine' used as an adjective should NOT trigger litigation."""
        text = (
            "The weather is fine today. "
            "That is a fine distinction. "
            "He is doing fine after the operation. "
            "Everything is fine with the project timeline."
        )
        topics = classify_topic(text)
        topic_names = {t.topic for t in topics}
        assert "litigation" not in topic_names


class TestSourceExtractionStopWords:
    """Verify common words like 'Any' are not extracted as person names."""

    def test_any_not_extracted_as_source(self):
        """'Any comments?' should NOT extract 'Any' as a source name."""
        text = (
            "Q: I heard about the new project. Any comments?\n\n"
            "We are excited about the progress so far."
        )
        sources = extract_sources(text)
        names = {s.name for s in sources}
        assert "Any" not in names, f"'Any' falsely extracted as source: {names}"

    def test_all_not_extracted_as_source(self):
        """'All' at sentence start should NOT be extracted as a source."""
        text = "All noted that the results were encouraging."
        sources = extract_sources(text)
        names = {s.name for s in sources}
        assert "All" not in names

    def test_real_names_still_extracted(self):
        """Actual person names should still be detected."""
        text = 'John Smith told reporters that the project was on track.'
        sources = extract_sources(text)
        names = {s.name for s in sources}
        assert "John Smith" in names
