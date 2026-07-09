"""Regression tests for Reuters Rust Belt data centers article (Jul 9, 2026).

Article: "Big Tech data centers are driving up power bills at America's
Rust Belt factories" (Reuters, July 7, 2026).

Covers:
- Source extraction: false positives eliminated (Capacity, Energy Consumers,
  White House, Smart Electric Power, Synergy Research), affiliations improved
- Entity extraction: Mid-Atlantic homograph filter (from prior iteration)
- Heritage/nostalgia framing device (new device type #83)
"""

import pytest
from pathlib import Path

ARTICLE_PATH = Path(__file__).parent.parent / (
    "examples/sample_output/"
    "reuters_big_tech_data_centers_rust_belt_factories_2026_07_09_article.txt"
)

ARTICLE_TEXT = ARTICLE_PATH.read_text() if ARTICLE_PATH.exists() else ""

# ---------------------------------------------------------------------------
# Source extraction
# ---------------------------------------------------------------------------


class TestSourceExtraction:
    """Source extraction improvements from Reuters Rust Belt article."""

    @pytest.fixture(autouse=True)
    def _extract(self):
        from mediascope.analyze.sources import extract_sources
        self.sources = extract_sources(ARTICLE_TEXT)
        self.names = {s.name for s in self.sources}
        self.named_sources = {
            s.name: s for s in self.sources if s.source_type == "named"
        }

    # --- False positives eliminated ---

    def test_capacity_not_extracted_as_source(self):
        """'Capacity charges at...' should not extract 'Capacity' as a source."""
        assert "Capacity" not in self.names

    def test_energy_consumers_not_extracted(self):
        """'Industrial Energy Consumers of America' should not extract
        'Energy Consumers' as a person name."""
        assert "Energy Consumers" not in self.names

    def test_white_house_not_extracted_as_named(self):
        """'The White House said' should not extract 'White House' as a
        named person source."""
        assert "White House" not in self.named_sources

    def test_smart_electric_power_not_extracted(self):
        """'Smart Electric Power Alliance' should not be extracted as a
        person name."""
        assert "Smart Electric Power" not in self.names

    def test_synergy_research_not_extracted_as_person(self):
        """'Synergy Research Group' should not be extracted as a person."""
        assert "Synergy Research" not in self.names

    def test_house_not_extracted_as_single_word_source(self):
        """Single-word 'House' (from White House) should not be a source."""
        assert "House" not in self.names

    # --- Correct sources extracted ---

    def test_brad_belden_extracted(self):
        """Brad Belden should be extracted as a named source."""
        assert "Brad Belden" in self.named_sources

    def test_paul_cicio_extracted(self):
        """Paul Cicio should be extracted as a named source."""
        assert "Paul Cicio" in self.named_sources

    def test_aaron_tinjum_extracted(self):
        """Aaron Tinjum should be extracted as a named source."""
        assert "Aaron Tinjum" in self.named_sources

    def test_timothy_ling_extracted(self):
        """Timothy Ling should be extracted as a named source."""
        assert "Timothy Ling" in self.named_sources

    def test_john_holeman_extracted(self):
        """John Holeman should be extracted as a named source."""
        assert "John Holeman" in self.named_sources

    # --- Affiliations ---

    def test_paul_cicio_affiliation(self):
        """Paul Cicio's affiliation should be 'Industrial Energy Consumers
        of America', not truncated to 'America'."""
        s = self.named_sources["Paul Cicio"]
        assert "Industrial Energy Consumers" in s.affiliation

    def test_aaron_tinjum_affiliation(self):
        """Aaron Tinjum's affiliation should be 'Data Center Coalition'."""
        s = self.named_sources["Aaron Tinjum"]
        assert "Data Center Coalition" in s.affiliation

    def test_timothy_ling_affiliation(self):
        """Timothy Ling's affiliation should be 'Plaskolite'."""
        s = self.named_sources["Timothy Ling"]
        assert "Plaskolite" in s.affiliation

    def test_john_holeman_affiliation(self):
        """John Holeman's affiliation should include 'Tosoh'."""
        s = self.named_sources["John Holeman"]
        assert "Tosoh" in s.affiliation

    # --- Meta no-comment ---

    def test_meta_no_comment(self):
        """'Meta declined to comment' should produce a no_comment source."""
        meta_sources = [s for s in self.sources if s.name == "Meta"]
        assert any(s.source_type == "no_comment" for s in meta_sources)


# ---------------------------------------------------------------------------
# Source extraction — stop-list additions (unit tests)
# ---------------------------------------------------------------------------


class TestStopListAdditions:
    """Unit tests for new stop-list entries."""

    def test_capacity_in_name_stop_first_words(self):
        from mediascope.analyze.sources import _NAME_STOP_FIRST_WORDS
        assert "Capacity" in _NAME_STOP_FIRST_WORDS

    def test_white_house_in_name_stop_names(self):
        from mediascope.analyze.sources import _NAME_STOP_NAMES
        assert "White House" in _NAME_STOP_NAMES

    def test_energy_consumers_in_name_stop_names(self):
        from mediascope.analyze.sources import _NAME_STOP_NAMES
        assert "Energy Consumers" in _NAME_STOP_NAMES

    def test_smart_electric_power_in_name_stop_names(self):
        from mediascope.analyze.sources import _NAME_STOP_NAMES
        assert "Smart Electric Power" in _NAME_STOP_NAMES


# ---------------------------------------------------------------------------
# Affiliation extraction — Pattern 0f (title of [descriptor] [Org])
# ---------------------------------------------------------------------------


class TestTitleOfDescriptorOrg:
    """Test Pattern 0f in _extract_affiliation: title + of + descriptors + Org."""

    def test_president_of_trade_group(self):
        from mediascope.analyze.sources import _extract_affiliation
        ctx = (
            'said Paul Cicio, president of the trade group '
            'Industrial Energy Consumers of America.'
        )
        aff = _extract_affiliation(ctx)
        assert "Industrial Energy Consumers" in aff

    def test_director_of_nonprofit(self):
        from mediascope.analyze.sources import _extract_affiliation
        ctx = (
            'according to Jane Smith, director of the nonprofit '
            'Clean Energy Foundation.'
        )
        aff = _extract_affiliation(ctx)
        assert "Clean Energy Foundation" in aff

    def test_vice_president_of_energy_for(self):
        from mediascope.analyze.sources import _extract_affiliation
        ctx = (
            'said Aaron Tinjum, vice president of energy for '
            'Data Center Coalition, a trade group.'
        )
        aff = _extract_affiliation(ctx)
        assert "Data Center Coalition" in aff


# ---------------------------------------------------------------------------
# Affiliation extraction — environmental domain keyword
# ---------------------------------------------------------------------------


class TestEnvironmentalDomainKeyword:
    """Test that 'environmental' is recognized as a domain keyword in
    possessive affiliation patterns (Pattern 0)."""

    def test_plaskolite_senior_environmental_director(self):
        from mediascope.analyze.sources import _extract_affiliation
        ctx = "said Timothy Ling, Plaskolite's senior environmental director."
        aff = _extract_affiliation(ctx)
        assert "Plaskolite" in aff

    def test_facilities_domain_keyword(self):
        from mediascope.analyze.sources import _extract_affiliation
        ctx = "said John Holeman, Tosoh's director of facilities and maintenance."
        aff = _extract_affiliation(ctx)
        assert "Tosoh" in aff


# ---------------------------------------------------------------------------
# Heritage/nostalgia framing device
# ---------------------------------------------------------------------------


class TestHeritageNostalgiaFraming:
    """Test the new heritage_nostalgia framing device type."""

    def test_heritage_device_exists(self):
        from mediascope.analyze.framing import _DEVICE_PATTERNS
        assert "heritage_nostalgia" in _DEVICE_PATTERNS

    def test_year_old_manufacturer(self):
        from mediascope.analyze.framing import detect_framing_devices
        text = "The 141-year-old brick manufacturer is struggling."
        devices = detect_framing_devices(text)
        heritage = [d for d in devices if d.device_type == "heritage_nostalgia"]
        assert len(heritage) >= 1

    def test_generation_reference(self):
        from mediascope.analyze.framing import detect_framing_devices
        text = "Brad Belden, part of the fifth generation working at the company."
        devices = detect_framing_devices(text)
        heritage = [d for d in devices if d.device_type == "heritage_nostalgia"]
        assert len(heritage) >= 1

    def test_iconic_building(self):
        from mediascope.analyze.framing import detect_framing_devices
        text = "Products can be found in iconic buildings including the Alamo."
        devices = detect_framing_devices(text)
        heritage = [d for d in devices if d.device_type == "heritage_nostalgia"]
        assert len(heritage) >= 1

    def test_family_owned_since(self):
        from mediascope.analyze.framing import detect_framing_devices
        text = "The family-owned bakery has been running since 1892."
        devices = detect_framing_devices(text)
        heritage = [d for d in devices if d.device_type == "heritage_nostalgia"]
        assert len(heritage) >= 1

    def test_century_old_factory(self):
        from mediascope.analyze.framing import detect_framing_devices
        text = "The century-old factory faces closure."
        devices = detect_framing_devices(text)
        heritage = [d for d in devices if d.device_type == "heritage_nostalgia"]
        assert len(heritage) >= 1

    def test_for_decades(self):
        from mediascope.analyze.framing import detect_framing_devices
        text = "They have served the community for over 50 years."
        devices = detect_framing_devices(text)
        heritage = [d for d in devices if d.device_type == "heritage_nostalgia"]
        assert len(heritage) >= 1

    def test_full_article_heritage_count(self):
        """The Reuters Rust Belt article should have at least 3 heritage
        framing instances."""
        from mediascope.analyze.framing import detect_framing_devices
        devices = detect_framing_devices(ARTICLE_TEXT)
        heritage = [d for d in devices if d.device_type == "heritage_nostalgia"]
        assert len(heritage) >= 3
