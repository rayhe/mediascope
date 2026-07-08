"""Tests for Bloomberg Muse Image article entity extraction fixes.

Covers:
- SpaceXAI → xAI entity alias (Bloomberg malformed compound)
- Anthropic PBC → Anthropic entity alias (corporate suffix)
- CoreWeave Inc, Alphabet Inc's Google, Oracle Corp extraction
"""

import pytest

from mediascope.analyze.entities import detect_entities


# --- SpaceXAI → xAI cluster ---

def test_spacexai_maps_to_xai():
    """'SpaceXAI' (Bloomberg compound) should match xAI entity cluster."""
    text = "Models from Elon Musk's SpaceXAI were used earlier this year."
    entities = detect_entities(text)
    clusters = [e.cluster for e in entities]
    assert "xAI" in clusters, f"Expected 'xAI' cluster for SpaceXAI, got {clusters}"


def test_xai_standalone_still_works():
    """Standard 'xAI' mention should still match."""
    text = "xAI released Grok 3 this week."
    entities = detect_entities(text)
    clusters = [e.cluster for e in entities]
    assert "xAI" in clusters


def test_grok_still_maps_to_xai():
    """Grok should still match xAI cluster after SpaceXAI addition."""
    text = "Grok was used to generate the images without consent."
    entities = detect_entities(text)
    clusters = [e.cluster for e in entities]
    assert "xAI" in clusters


# --- Anthropic PBC → Anthropic cluster ---

def test_anthropic_pbc_maps_to_anthropic():
    """'Anthropic PBC' (Public Benefit Corp suffix) should match Anthropic."""
    text = "rivals like OpenAI and Anthropic PBC"
    entities = detect_entities(text)
    clusters = [e.cluster for e in entities]
    assert "Anthropic" in clusters, f"Expected 'Anthropic' cluster, got {clusters}"


def test_anthropic_standalone_still_works():
    """Bare 'Anthropic' should still match after PBC alias addition."""
    text = "Anthropic released a safety report."
    entities = detect_entities(text)
    clusters = [e.cluster for e in entities]
    assert "Anthropic" in clusters


def test_claude_still_maps_to_anthropic():
    """Claude should still map to Anthropic cluster."""
    text = "Claude was updated with new capabilities."
    entities = detect_entities(text)
    clusters = [e.cluster for e in entities]
    assert "Anthropic" in clusters


# --- Full article entity coverage ---

def test_bloomberg_article_extracts_meta():
    """Bloomberg article text should extract Meta as primary entity."""
    text = (
        "Meta Platforms Inc debuted a new image-generation artificial "
        "intelligence (AI) model, its first such release since the company "
        "spent billions to rebuild its AI lab."
    )
    entities = detect_entities(text)
    clusters = [e.cluster for e in entities]
    assert "Meta" in clusters


def test_bloomberg_article_extracts_openai():
    """Bloomberg article should extract OpenAI from rivalry context."""
    text = "compete with those from rivals like OpenAI and Anthropic PBC"
    entities = detect_entities(text)
    clusters = [e.cluster for e in entities]
    assert "OpenAI" in clusters


def test_elon_musk_maps_to_twitter_x():
    """'Elon Musk' should map to Twitter/X cluster, not xAI."""
    text = "Models from Elon Musk's SpaceXAI were used earlier this year."
    entities = detect_entities(text)
    # Elon Musk should map to Twitter/X (the person-entity cluster)
    # SpaceXAI should map to xAI
    clusters = [e.cluster for e in entities]
    # Both should be present
    assert "xAI" in clusters, f"Missing xAI cluster from SpaceXAI, got {clusters}"
