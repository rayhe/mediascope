"""Tests for ironic_quotation suppression in analyst/financial coverage.

Verifies that:
1. Short analyst-attributed quotes (≤3 words) with firm-level post-
   attribution ("Jefferies said") are NOT flagged as ironic_quotation.
2. Longer analyst-attributed quotes (>3 words) with pre- or post-
   attribution ("Mizuho said", "the research firm added") are NOT
   flagged as ironic_quotation.
3. Cross-publication citations ("Bloomberg reported") are NOT flagged
   as self_referential_investigation when no source_publication is set.
4. Genuine scare quotes and self-referential patterns are still caught.

Discovered in Stocktwits Meta cloud analyst reactions article (Jul 2026).
"""

import pytest

from mediascope.analyze.framing import detect_framing_devices


def _device_types(text: str, **kwargs) -> set[str]:
    """Return the set of device_type values detected in *text*."""
    return {d.device_type for d in detect_framing_devices(text, **kwargs)}


def _device_type_list(text: str, **kwargs) -> list[str]:
    """Return list of device_type values (preserving duplicates)."""
    return [d.device_type for d in detect_framing_devices(text, **kwargs)]


# -----------------------------------------------------------------------
# 1. Short analyst-attributed quotes — firm-level post-attribution
# -----------------------------------------------------------------------

class TestShortAnalystQuotePostAttribution:
    """Short quoted terms with firm attribution after the quote."""

    def test_strategic_jefferies_said(self):
        """'\"strategic\" ... Jefferies said' should NOT be ironic_quotation."""
        text = (
            'The cloud business is "strategic" to Meta\'s longer-term '
            'AI ambitions, Jefferies said, adding that it appears to '
            "mirror Amazon's AWS playbook."
        )
        assert "ironic_quotation" not in _device_types(text)

    def test_positive_mizuho_noted(self):
        """'\"positive\" ... Mizuho noted' should NOT be ironic_quotation."""
        text = (
            'Analysts view the development as "positive" for Meta\'s '
            "long-term margins, Mizuho noted."
        )
        assert "ironic_quotation" not in _device_types(text)

    def test_material_bmo_said(self):
        """'\"material\" ... BMO Capital said' should NOT be ironic_quotation."""
        text = (
            'The revenue impact would be "material" to Meta\'s bottom '
            "line, BMO Capital said in a research note."
        )
        assert "ironic_quotation" not in _device_types(text)

    def test_accretive_analysts_added(self):
        """'\"accretive\" ... analysts added' with firm post-attribution."""
        text = (
            'The cloud business would be "accretive" to earnings, '
            "Morgan Stanley added in a note."
        )
        assert "ironic_quotation" not in _device_types(text)


# -----------------------------------------------------------------------
# 2. Longer analyst-attributed quotes — firm attribution in wider context
# -----------------------------------------------------------------------

class TestLongerAnalystQuoteAttribution:
    """Longer quoted phrases with firm attribution nearby."""

    def test_margin_of_safety_mizuho_said(self):
        """Post-attribution: '\"a margin of safety...\" Mizuho said.'"""
        text = (
            'If Meta goes ahead with the plans, the business would add '
            '"a margin of safety to medium-term EPS," Mizuho said.'
        )
        assert "ironic_quotation" not in _device_types(text)

    def test_long_quote_pre_attribution(self):
        """Pre-attribution: 'Mizuho said it sees it \"more as planning...\"'"""
        text = (
            "Mizuho said it does not believe cloud is a near-term "
            "business line and sees it "
            '"more as planning for all potential scenarios" rather than '
            "an imminent product launch."
        )
        assert "ironic_quotation" not in _device_types(text)

    def test_research_firm_added_that(self):
        """'The research firm added that ... \"a positive, adding a
        margin of safety to medium-term EPS.\"'"""
        text = (
            "The research firm added that investors continue to struggle "
            "to see a credible path to monetizing AI investment at Meta, "
            'and as such, the development is "a positive, adding a '
            'margin of safety to medium-term EPS."'
        )
        assert "ironic_quotation" not in _device_types(text)


# -----------------------------------------------------------------------
# 3. Cross-publication citation — self_referential_investigation
# -----------------------------------------------------------------------

class TestWireCrossCitation:
    """Wire service citations should NOT be self_referential_investigation."""

    def test_bloomberg_reported_no_source(self):
        """'Bloomberg reported' without source_publication should be
        suppressed as a wire cross-citation."""
        text = (
            "The company is exploring a cloud computing business, "
            "Bloomberg reported last week, in a move that could generate "
            "billions in new revenue."
        )
        assert "self_referential_investigation" not in _device_types(text)

    def test_reuters_reported_no_source(self):
        """'Reuters reported' without source_publication."""
        text = (
            "Plans are still in development, Reuters reported, citing "
            "people familiar with the matter."
        )
        assert "self_referential_investigation" not in _device_types(text)

    def test_bloomberg_with_source_publication_match(self):
        """'Bloomberg reported' SHOULD be self-referential when the
        article is FROM Bloomberg."""
        text = (
            "The company is exploring a cloud computing business, "
            "Bloomberg reported last week."
        )
        types = _device_types(text, source_publication="Bloomberg")
        assert "self_referential_investigation" in types

    def test_our_investigation_always_kept(self):
        """Reflexive 'our investigation' is always self-referential."""
        text = (
            "Our investigation revealed that the company had been "
            "quietly building cloud infrastructure for months."
        )
        assert "self_referential_investigation" in _device_types(text)


# -----------------------------------------------------------------------
# 4. Genuine scare quotes should still be caught
# -----------------------------------------------------------------------

class TestGenuineScarequotesPreserved:
    """Real ironic/scare quotes should still fire."""

    def test_genuine_scare_quote_no_attribution(self):
        """'\"safe\" technology' with no attribution = scare quote."""
        text = (
            "The company insists its platform is completely "
            '"safe" technology, despite mounting evidence to the '
            "contrary. Critics point to numerous documented harms."
        )
        assert "ironic_quotation" in _device_types(text)

    def test_editorial_scare_quote_undermining(self):
        """'\"responsible\" AI' used editorially to undercut."""
        text = (
            "Meta's so-called \"responsible\" AI practices have come "
            "under fire from regulators and advocacy groups alike."
        )
        assert "ironic_quotation" in _device_types(text)
