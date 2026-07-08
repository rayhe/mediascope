"""Tests for compound negative attribution verb detection.

Compound phrases like "attempted yet failed", "reluctantly conceded",
"was forced to admit" carry loaded framing that single-word verb
classification would miss (since "attempted" alone is neutral).
"""

import pytest

from mediascope.analyze.sources import (
    classify_attribution_verb,
    _find_attribution_verb,
    COMPOUND_LOADED_PHRASES,
)


class TestCompoundVerbClassification:
    """classify_attribution_verb should detect compound loaded phrases."""

    @pytest.mark.parametrize("phrase", [
        "attempted yet failed",
        "tried and failed",
        "sought but was denied",
        "reluctantly admitted",
        "was forced to concede",
        "grudgingly acknowledged",
        "finally admitted",
        "belatedly acknowledged",
        "denied but was found",
        "claimed but was contradicted",
    ])
    def test_compound_loaded_phrases_classified_loaded(self, phrase):
        assert classify_attribution_verb(phrase) == "loaded", (
            f"Compound phrase '{phrase}' should classify as loaded"
        )

    def test_single_neutral_verb_still_neutral(self):
        assert classify_attribution_verb("said") == "neutral"
        assert classify_attribution_verb("noted") == "neutral"
        assert classify_attribution_verb("explained") == "neutral"

    def test_single_loaded_verb_still_loaded(self):
        assert classify_attribution_verb("slammed") == "loaded"
        assert classify_attribution_verb("blasted") == "loaded"
        assert classify_attribution_verb("denied") == "loaded"


class TestCompoundVerbExtraction:
    """_find_attribution_verb should prefer compound phrases over single words."""

    def test_finds_compound_in_context(self):
        context = 'Meta attempted yet failed to get the case dismissed'
        verb = _find_attribution_verb(context)
        assert verb == "attempted yet failed", (
            f"Should extract compound phrase, got '{verb}'"
        )

    def test_finds_reluctantly_admitted(self):
        context = 'the company reluctantly admitted the data existed'
        verb = _find_attribution_verb(context)
        assert verb == "reluctantly admitted", (
            f"Should extract 'reluctantly admitted', got '{verb}'"
        )

    def test_finds_was_forced_to_concede(self):
        context = 'the CEO was forced to concede that growth had slowed'
        verb = _find_attribution_verb(context)
        assert verb == "was forced to concede", (
            f"Should extract 'was forced to concede', got '{verb}'"
        )

    def test_falls_back_to_single_verb_when_no_compound(self):
        context = 'the company said it would comply'
        verb = _find_attribution_verb(context)
        assert verb == "said", (
            f"Should fall back to single-word 'said', got '{verb}'"
        )


class TestCompoundPhrasesNonEmpty:
    """Sanity check that the compound phrases list is populated."""

    def test_has_entries(self):
        assert len(COMPOUND_LOADED_PHRASES) >= 30, (
            f"Expected >=30 compound phrases, got {len(COMPOUND_LOADED_PHRASES)}"
        )

    def test_all_lowercase(self):
        for phrase in COMPOUND_LOADED_PHRASES:
            assert phrase == phrase.lower(), (
                f"Compound phrase '{phrase}' should be lowercase"
            )

    def test_all_multiword(self):
        for phrase in COMPOUND_LOADED_PHRASES:
            assert " " in phrase, (
                f"Compound phrase '{phrase}' should be multi-word"
            )
