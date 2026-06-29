"""Tests for source extraction fixes from MIT TR DeepMind multi-agent article.

Three bugs were found and fixed:
  1. Pattern 3 case-sensitivity: "According to" at sentence start was missed
  2. Missing Pattern 5c: verb before single surname ("says Shah")
  3. Missing attribution verbs: "thinks", "believes", "considers", "cautions"
"""

from mediascope.analyze.sources import extract_sources, ALL_VERBS


class TestPattern3CaseFix:
    """Pattern 3 should handle sentence-initial 'According' capitalization."""

    def test_capital_according_to_detects_name(self):
        text = (
            "According to Rohin Shah, who directs the company's AGI "
            "safety and alignment research, multi-agent risks are growing."
        )
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Rohin Shah" in names

    def test_lowercase_according_to_still_works(self):
        text = (
            "The matter has been reviewed, according to Jane Smith, "
            "who oversees the compliance department."
        )
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Jane Smith" in names

    def test_capital_according_does_not_match_lowercase_names(self):
        """Ensure [Aa] prefix doesn't weaken name pattern case sensitivity."""
        text = (
            "According to four people familiar with the matter, "
            "the deal is expected to close next month."
        )
        sources = extract_sources(text)
        named_sources = [s for s in sources if not s.is_anonymous]
        # "four people" should NOT appear as a named source
        assert not any(s.name == "four people" for s in named_sources)


class TestPattern5cVerbBeforeSingleSurname:
    """Pattern 5c: 'verb [SingleName]' catches 'says Shah' style attribution."""

    def test_says_surname(self):
        text = (
            '"The strength of academia is that it can look far into '
            'the future," says Shah.'
        )
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Shah" in names

    def test_notes_surname(self):
        text = (
            "And yet, Fox notes, risks that were hypothetical a few "
            "years ago are now very real."
        )
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Fox" in names

    def test_cautions_surname(self):
        text = (
            "But he cautions that safety researchers can overlook "
            "boring problems, says Angel."
        )
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Angel" in names

    def test_verb_before_org_name_not_matched(self):
        """Org names in _SINGLE_NAME_ORG_STOPS should not be extracted."""
        text = '"We will address this," says Google.'
        sources = extract_sources(text)
        names = [s.name for s in sources if s.source_type == "named"]
        assert "Google" not in names

    def test_dedup_with_full_name(self):
        """If full name already captured, single surname should be skipped."""
        text = (
            "Rohin Shah told reporters the risks are real. "
            '"We need to act now," says Shah.'
        )
        sources = extract_sources(text)
        # Should have only one entry, not duplicates
        shah_entries = [s for s in sources if "Shah" in s.name]
        assert len(shah_entries) == 1
        assert shah_entries[0].name == "Rohin Shah"


class TestAttributionVerbExpansion:
    """New cognitive/opinion verbs should be in ALL_VERBS."""

    def test_thinks_in_verbs(self):
        assert "thinks" in ALL_VERBS

    def test_believes_in_verbs(self):
        assert "believes" in ALL_VERBS

    def test_considers_in_verbs(self):
        assert "considers" in ALL_VERBS

    def test_cautions_in_verbs(self):
        assert "cautions" in ALL_VERBS

    def test_thinks_extracts_source(self):
        text = "Shah thinks we have a few more months before agents deploy widely."
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Shah" in names

    def test_believes_extracts_source(self):
        text = "Miranda Chen believes the framework needs significant revision."
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Miranda Chen" in names
