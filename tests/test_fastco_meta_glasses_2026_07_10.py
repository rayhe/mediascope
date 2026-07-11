"""Regression tests for Fast Company Meta glasses controversies article.

Article: "The many controversies of Meta's AI glasses"
Published: July 10, 2026 — Fast Company
URL: https://www.fastcompany.com/91571430/the-many-controversies-of-metas-ai-glasses

Bugs discovered during Type A deep dive, July 11 2026 iteration:
- Bug 1: Pattern 0b missing C-suite title acronyms (CTO/CFO/etc.)
- Bug 2: "Electronic Frontier Foundation" truncated to "Frontier Foundation"
- Bug 3: "Kassaby" duplicated alongside "Dina El-Kassaby"
- Bug 4: Bosworth quote misattribution (lower priority, not yet fixed)
"""

import pytest

from mediascope.analyze.sources import extract_sources


# --- Fixtures ---

ARTICLE_SNIPPET_EFF = (
    "By far, the most controversial aspects of Meta glasses center on its "
    "embedded camera, which can be used to take pictures or video of others "
    "without permission. Given that some users leave the camera on all the "
    "time, The Electronic Frontier Foundation points out that the camera "
    "could capture someone entering their passcode or password into their "
    "phone, computer, or an ATM.\n"
    'The EFF has warned that the idea of adding a facial recognition '
    'functionality to the glasses "is a monumentally bad idea that should '
    'be abandoned by Meta and any of its competitors considering a similar '
    "feature.\"\n"
)

ARTICLE_SNIPPET_ELKASSABY = (
    'In a statement, Meta spokesperson Dina El-Kassaby wrote that "The '
    "people who use [Meta Glasses] and those around them need to trust them. "
    "That's why we built privacy into our AI glasses from the ground up.\"\n"
    "\n"
    "El-Kassaby wrote that Meta has \"a very thoughtful approach\" to "
    "privacy features.\n"
)

ARTICLE_SNIPPET_CTO = (
    "Meta CTO Andrew Bosworth said the company is taking \"a very "
    'thoughtful approach" to identifying people.\n'
)


# --- Bug 2: EFF name truncation ---

class TestEFFNameExtraction:
    """Electronic Frontier Foundation must be extracted as a 3-word org,
    not truncated to 'Frontier Foundation' as a person name."""

    def test_eff_extracted_as_organizational(self):
        sources = extract_sources(ARTICLE_SNIPPET_EFF)
        names = [s.name for s in sources]
        assert "Electronic Frontier Foundation" in names

    def test_frontier_foundation_not_extracted_as_person(self):
        sources = extract_sources(ARTICLE_SNIPPET_EFF)
        names = [s.name for s in sources]
        assert "Frontier Foundation" not in names

    def test_eff_source_type_is_organizational(self):
        sources = extract_sources(ARTICLE_SNIPPET_EFF)
        eff = [s for s in sources if s.name == "Electronic Frontier Foundation"]
        assert len(eff) == 1
        assert eff[0].source_type == "organizational"


# --- Bug 3: Hyphenated surname dedup ---

class TestHyphenatedSurnameDedup:
    """'Kassaby' must not appear as a separate source when
    'Dina El-Kassaby' is already extracted."""

    def test_elkassaby_extracted(self):
        sources = extract_sources(ARTICLE_SNIPPET_ELKASSABY)
        names = [s.name for s in sources]
        assert "Dina El-Kassaby" in names

    def test_kassaby_not_duplicated(self):
        sources = extract_sources(ARTICLE_SNIPPET_ELKASSABY)
        names = [s.name for s in sources]
        assert "Kassaby" not in names

    def test_elkassaby_dedup_count(self):
        """Only one source entry for El-Kassaby, not two."""
        sources = extract_sources(ARTICLE_SNIPPET_ELKASSABY)
        kassaby_sources = [s for s in sources if "Kassaby" in s.name or "kassaby" in s.name.lower()]
        assert len(kassaby_sources) == 1


# --- Bug 1: CTO title in Pattern 0b ---

class TestCTOTitleExtraction:
    """'Meta CTO Andrew Bosworth said' must extract Bosworth with
    affiliation 'Meta', not with junk like 'LED light'."""

    def test_bosworth_extracted(self):
        sources = extract_sources(ARTICLE_SNIPPET_CTO)
        names = [s.name for s in sources]
        assert "Andrew Bosworth" in names

    def test_bosworth_affiliation_is_meta(self):
        sources = extract_sources(ARTICLE_SNIPPET_CTO)
        boz = [s for s in sources if s.name == "Andrew Bosworth"]
        assert len(boz) == 1
        assert boz[0].affiliation == "Meta"


# --- General hyphenated dedup edge cases ---

class TestHyphenatedDedup:
    """Generalized tests for hyphen-aware surname dedup."""

    def test_hyphen_suffix_first_word(self):
        """'Smith' should be deduped if 'Jane Cooper-Smith' exists."""
        text = (
            'Analyst Jane Cooper-Smith noted that "the market is shifting." '
            'Later, Cooper-Smith confirmed the trend was accelerating.'
        )
        sources = extract_sources(text)
        names = [s.name for s in sources]
        # "Smith" alone should not appear
        assert "Smith" not in names

    def test_hyphen_full_name_preserved(self):
        """The full hyphenated name should be preserved."""
        text = (
            'Analyst Jane Cooper-Smith noted that "the market is shifting." '
            'Later, Cooper-Smith confirmed the trend was accelerating.'
        )
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Jane Cooper-Smith" in names
