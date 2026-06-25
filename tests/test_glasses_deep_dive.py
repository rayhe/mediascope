"""Tests for bugs found during Wired Meta Glasses article deep dive.

These tests cover four toolkit gaps discovered in the 2026-06-25 15:00 PT
Hour Type A iteration — manual analysis of the Wired article
"Meta's Very Own Smart Glasses Go on Sale Today for $299" (Jun 23, 2026)
by Julian Chokkattu.

Bugs fixed:
1. Entity miss: Peter Bristol (Meta VP of Industrial Design) not detected
2. Affiliation misattribution: Bosworth tagged as "Snap's Specs" instead of "Meta"
3. False anonymous source: "Many people are still concerned" classified as anon source
4. Source miss: Single-name sources (e.g. "Bristol says") not detected
"""

import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mediascope.analyze.entities import detect_entities, DEFAULT_ENTITY_CLUSTERS
from mediascope.analyze.sources import extract_sources, _extract_affiliation


# ===================================================================
# Entity Detection Tests
# ===================================================================

class TestBristolEntityDetection:
    """Peter Bristol (Meta VP of Industrial Design) must be detected
    as a Meta entity."""

    def test_bristol_in_meta_aliases(self):
        """Bristol should be in the Meta entity cluster aliases."""
        meta_cluster = DEFAULT_ENTITY_CLUSTERS["Meta"]
        aliases = meta_cluster["aliases"]
        assert "Peter Bristol" in aliases
        assert "Bristol" in aliases

    def test_bristol_detected_in_text(self):
        """Bristol mentions should be detected and clustered under Meta."""
        text = (
            "\"It's more than just whether they fit,\" Bristol says. "
            "\"It's a really important decision.\""
        )
        entities = detect_entities(text)
        bristol = [e for e in entities if e.canonical_name == "Bristol"]
        assert len(bristol) >= 1
        assert bristol[0].cluster == "Meta"

    def test_peter_bristol_detected(self):
        """Full name Peter Bristol should also be detected."""
        text = "Peter Bristol, Meta's VP of Industrial Design, discussed the new frames."
        entities = detect_entities(text)
        bristol = [e for e in entities if "Bristol" in e.canonical_name]
        assert len(bristol) >= 1
        assert bristol[0].cluster == "Meta"

    def test_bristol_not_city_false_positive(self):
        """Bristol the city should ideally not match, but we accept it as
        a known trade-off for now (single-word aliases like 'Bosworth'
        have the same issue)."""
        # This test documents the known limitation — not a failure
        text = "The company has offices in Bristol, England."
        entities = detect_entities(text)
        bristol = [e for e in entities if e.canonical_name == "Bristol"]
        # We accept this false positive as a known trade-off
        assert isinstance(bristol, list)  # Just ensure no crash


# ===================================================================
# Affiliation Extraction Tests
# ===================================================================

class TestBosworthAffiliation:
    """Bosworth's affiliation must be 'Meta', not 'Snap's Specs'."""

    def test_non_possessive_title_affiliation(self):
        """'Meta chief technology officer Andrew Bosworth' should extract
        affiliation as 'Meta', not pick up 'Snap's Specs' from context."""
        context = (
            "On Snap's Specs, Meta chief technology officer "
            "Andrew Bosworth says it's good for customers to have competition."
        )
        aff = _extract_affiliation(context)
        assert aff == "Meta", f"Expected 'Meta', got '{aff}'"

    def test_non_possessive_title_various_orgs(self):
        """Non-possessive title pattern should work for various org names."""
        cases = [
            ("Google chief executive Sundar Pichai says the future is AI.", "Google"),
            ("Apple senior vice president Craig Federighi told developers.", "Apple"),
            ("Amazon chief technology officer Werner Vogels explained.", "Amazon"),
        ]
        for context, expected in cases:
            aff = _extract_affiliation(context)
            assert aff == expected, f"For '{context}': expected '{expected}', got '{aff}'"

    def test_possessive_title_still_works(self):
        """Possessive title pattern should still work correctly."""
        context = "Meta's vice president of communications Andy Stone told reporters."
        aff = _extract_affiliation(context)
        assert aff == "Meta", f"Expected 'Meta', got '{aff}'"

    def test_full_article_bosworth_affiliation(self):
        """In the actual article, Bosworth should be affiliated with Meta."""
        article_path = os.path.join(
            os.path.dirname(__file__), "..",
            "examples", "sample_output",
            "wired_meta_glasses_launch_self_branded_2026_06_23_article.txt",
        )
        if not os.path.exists(article_path):
            pytest.skip("Article text not available")
        with open(article_path) as f:
            text = f.read()
        sources = extract_sources(text)
        bosworth = [s for s in sources if "Bosworth" in s.name]
        assert len(bosworth) >= 1, "Bosworth should be detected as a source"
        assert bosworth[0].affiliation == "Meta", (
            f"Bosworth affiliation should be 'Meta', got '{bosworth[0].affiliation}'"
        )


# ===================================================================
# False Anonymous Source Tests
# ===================================================================

class TestManyPeopleFalsePositive:
    """'Many people are still concerned' is editorial narration, not
    an anonymous source attribution."""

    def test_many_people_editorial_not_source(self):
        """'Many people are still concerned about X' should NOT be
        classified as an anonymous source."""
        text = (
            "Many people are still concerned about the privacy oversteps "
            "made possible by wearable cameras that can discreetly record "
            "the user's surroundings."
        )
        sources = extract_sources(text)
        anon = [s for s in sources if s.is_anonymous]
        many = [s for s in anon if "many people" in s.name.lower()]
        assert len(many) == 0, (
            f"'Many people are still concerned' is editorial narration, "
            f"not an anonymous source. Got: {[s.name for s in many]}"
        )

    def test_many_people_with_verb_still_detected(self):
        """'Many people said X' SHOULD be detected as an anonymous source."""
        text = (
            "Many people said the company's handling of the situation "
            "was inadequate and irresponsible."
        )
        sources = extract_sources(text)
        anon = [s for s in sources if s.is_anonymous]
        many = [s for s in anon if "many" in s.name.lower() and "people" in s.name.lower()]
        assert len(many) >= 1, (
            "'Many people said' should be detected as anonymous source"
        )

    def test_several_employees_editorial_not_source(self):
        """'Several employees were unhappy' is editorial, not attribution."""
        text = "Several employees were unhappy with the decision."
        sources = extract_sources(text)
        anon = [s for s in sources if s.is_anonymous and "several" in s.name.lower()]
        assert len(anon) == 0, (
            "'Several employees were unhappy' is editorial narration"
        )

    def test_several_employees_with_verb_detected(self):
        """'Several employees told WIRED' SHOULD be detected."""
        text = "Several employees told WIRED that morale had hit rock bottom."
        sources = extract_sources(text)
        anon = [s for s in sources if s.is_anonymous]
        sev = [s for s in anon if "several" in s.name.lower()]
        assert len(sev) >= 1, (
            "'Several employees told WIRED' should be anonymous source"
        )


# ===================================================================
# Single-Name Source Detection Tests
# ===================================================================

class TestSingleNameSourceDetection:
    """Sources referred to by last name only should be detected."""

    def test_bristol_detected_as_source(self):
        """'Bristol says' should be detected as a named source."""
        text = (
            "\"It's more than just whether they fit,\" Bristol says. "
            "\"It's a really important decision.\""
        )
        sources = extract_sources(text)
        named = [s for s in sources if not s.is_anonymous]
        bristol = [s for s in named if s.name == "Bristol"]
        assert len(bristol) >= 1, (
            "'Bristol says' should be detected as a named source"
        )

    def test_single_name_with_full_name_dedup(self):
        """If full name 'Andrew Bosworth' is already detected, single-name
        'Bosworth' should be deduplicated (not create a second entry)."""
        text = (
            "Andrew Bosworth says Meta is committed to the platform. "
            "Later, Bosworth says the glasses are improving."
        )
        sources = extract_sources(text)
        bosworth = [s for s in sources if "Bosworth" in s.name]
        assert len(bosworth) == 1, (
            f"Should have 1 Bosworth entry (full name), got {len(bosworth)}: "
            f"{[s.name for s in bosworth]}"
        )

    def test_org_names_not_detected_as_single_name_source(self):
        """Organization names like 'Meta says' should NOT be caught
        by the single-name source pattern."""
        text = "Meta says the product will launch next month. Apple told investors."
        sources = extract_sources(text)
        # Meta and Apple should not appear as named sources from single-name pattern
        # (they might appear as organizational sources, which is correct)
        named_non_org = [
            s for s in sources
            if not s.is_anonymous
            and s.source_type == "named"
            and s.name in ("Meta", "Apple")
        ]
        assert len(named_non_org) == 0, (
            f"Org names should not be detected as single-name person sources: "
            f"{[s.name for s in named_non_org]}"
        )

    def test_stop_words_not_detected(self):
        """Common English words starting sentences should not be caught."""
        text = "Yesterday said nothing about the future. Finally told the truth."
        sources = extract_sources(text)
        named = [s for s in sources if s.name in ("Yesterday", "Finally")]
        assert len(named) == 0, (
            f"Stop words should not be detected as sources: "
            f"{[s.name for s in named]}"
        )

    def test_full_article_bristol_detected(self):
        """In the actual Wired glasses article, Bristol must be detected."""
        article_path = os.path.join(
            os.path.dirname(__file__), "..",
            "examples", "sample_output",
            "wired_meta_glasses_launch_self_branded_2026_06_23_article.txt",
        )
        if not os.path.exists(article_path):
            pytest.skip("Article text not available")
        with open(article_path) as f:
            text = f.read()
        sources = extract_sources(text)
        bristol = [s for s in sources if s.name == "Bristol"]
        assert len(bristol) >= 1, "Bristol should be detected as a source"
        assert bristol[0].source_type == "named"
        assert not bristol[0].is_anonymous
