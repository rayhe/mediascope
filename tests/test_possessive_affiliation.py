"""Tests for possessive affiliation extraction in source detection.

Validates the fix for the "Org's Person Name verb" pattern in
_extract_direct_possessive and _extract_affiliation, ensuring that
"Nvidia's Jensen Huang said" extracts "Nvidia" as the affiliation,
not "AI job displacement" from the surrounding context.
"""

import pytest
from mediascope.analyze.sources import extract_sources, _extract_direct_possessive, _extract_affiliation


class TestDirectPossessiveExtraction:
    """Test _extract_direct_possessive for Org's Person patterns."""

    def test_nvidias_jensen_huang(self):
        text = 'Nvidia\'s Jensen Huang said that AI has been used as a lazy excuse.'
        # "Jensen Huang" starts at index 9
        assert _extract_direct_possessive(text, 9) == "Nvidia"

    def test_openais_sam_altman(self):
        text = 'OpenAI\'s Sam Altman said that AI would make jobs disappear.'
        assert _extract_direct_possessive(text, 9) == "OpenAI"

    def test_anthropics_dario_amodei(self):
        text = 'Anthropic\'s Dario Amodei said that AI could wipe out entry-level jobs.'
        assert _extract_direct_possessive(text, 12) == "Anthropic"

    def test_metas_mark_zuckerberg(self):
        text = 'Meta\'s Mark Zuckerberg told employees the restructuring was necessary.'
        assert _extract_direct_possessive(text, 7) == "Meta"

    def test_no_possessive(self):
        text = 'Mark Zuckerberg said the restructuring was necessary.'
        assert _extract_direct_possessive(text, 0) == ""

    def test_smart_quote_possessive(self):
        text = 'Nvidia\u2019s Jensen Huang said AI is transforming the industry.'
        assert _extract_direct_possessive(text, 9) == "Nvidia"


class TestPossessiveInAffiliationPatterns:
    """Test _extract_affiliation with possessive person-name patterns."""

    def test_nvidia_jensen_huang_context(self):
        ctx = 'topic of AI job displacement. Nvidia\'s Jensen Huang said that AI'
        assert _extract_affiliation(ctx) == "Nvidia"

    def test_anthropic_dario_amodei_context(self):
        ctx = 'his prediction. And last year, Anthropic\'s Dario Amodei said that AI could'
        assert _extract_affiliation(ctx) == "Anthropic"

    def test_possessive_person_beats_of_phrase(self):
        """Possessive-person pattern must fire before 'of [Organization]'."""
        ctx = 'head of Applied Sciences. Google\'s Sundar Pichai said the company'
        # Should extract "Google" from the possessive, not "Applied Sciences"
        assert _extract_affiliation(ctx) == "Google"


class TestEndToEndPossessiveAffiliation:
    """Integration tests with extract_sources on realistic article text."""

    def test_multi_source_paragraph(self):
        """Three consecutive Org's Person attributions should each get correct org."""
        text = (
            'Nvidia\'s Jensen Huang said that AI has been used as a "lazy" excuse '
            'for layoffs. OpenAI\'s Sam Altman said that AI would make jobs '
            'disappear. And last year, Anthropic\'s Dario Amodei said that AI '
            'could wipe out 50% of entry-level white-collar jobs.'
        )
        srcs = extract_sources(text)
        by_name = {s.name: s for s in srcs}
        assert by_name["Jensen Huang"].affiliation == "Nvidia"
        assert by_name["Sam Altman"].affiliation == "OpenAI"
        assert by_name["Dario Amodei"].affiliation == "Anthropic"

    def test_no_cross_contamination(self):
        """Source B should not inherit Org from Source A's possessive when
        Source B has its own possessive."""
        text = (
            'Apple\'s Tim Cook said privacy matters. '
            'Google\'s Sundar Pichai said AI is transformative.'
        )
        srcs = extract_sources(text)
        by_name = {s.name: s for s in srcs}
        assert by_name["Tim Cook"].affiliation == "Apple"
        # Sundar Pichai's own possessive should take priority
        assert by_name["Sundar Pichai"].affiliation == "Google"

    def test_source_without_possessive_gets_context_fallback(self):
        """Sources without a possessive fall back to _extract_affiliation context.
        Note: 'Meta CEO' without possessive is not matched by current patterns
        (CEO is only in possessive Pattern 0), so affiliation may be empty.
        This is a known limitation of the title-matching patterns."""
        text = (
            'Meta CEO Mark Zuckerberg said AI would create more jobs.'
        )
        srcs = extract_sources(text)
        by_name = {s.name: s for s in srcs}
        # Currently empty — CEO without possessive is not in Pattern 0b
        # This test documents the current behavior, not the ideal behavior
        assert "Mark Zuckerberg" in by_name
