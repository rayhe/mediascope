"""Tests for speculative_framing quote-context suppression.

Speculative hedges inside quotation marks (direct speech from analysts,
executives, or other sources) should NOT count toward the 5-marker threshold.
Financial articles routinely contain 5+ hedging phrases in analyst quotes
("I wouldn't rule it out," "could potentially accelerate," "may be signaling")
that are professional convention, not editorial framing.

Added in Type D iteration 2026-07-09 to fix false-positive risk in
financial/analyst articles.
"""
import pytest
from mediascope.analyze.framing import (
    detect_framing_devices,
    _find_quoted_spans,
    _is_in_quoted_span,
)


# ───────────────────────────────────────────────────────────────────────
# Helper function tests
# ───────────────────────────────────────────────────────────────────────

class TestFindQuotedSpans:
    """Tests for _find_quoted_spans helper."""

    def test_straight_double_quotes(self):
        text = 'He said "I think it could work" and left.'
        spans = _find_quoted_spans(text)
        assert len(spans) == 1
        assert text[spans[0][0]:spans[0][1]] == '"I think it could work"'

    def test_smart_double_quotes(self):
        text = 'She noted \u201cthis may accelerate\u201d in her report.'
        spans = _find_quoted_spans(text)
        assert len(spans) == 1
        assert text[spans[0][0]:spans[0][1]] == '\u201cthis may accelerate\u201d'

    def test_multiple_quotes(self):
        text = '"First quote" some text "second quote" more text.'
        spans = _find_quoted_spans(text)
        assert len(spans) == 2

    def test_no_quotes(self):
        text = 'This article has no quoted speech at all.'
        spans = _find_quoted_spans(text)
        assert len(spans) == 0

    def test_mixed_quote_styles(self):
        text = '"Straight quotes" and \u201csmart quotes\u201d in one article.'
        spans = _find_quoted_spans(text)
        assert len(spans) == 2


class TestIsInQuotedSpan:
    """Tests for _is_in_quoted_span helper."""

    def test_position_inside_span(self):
        spans = [(5, 20), (30, 50)]
        assert _is_in_quoted_span(10, spans) is True

    def test_position_outside_span(self):
        spans = [(5, 20), (30, 50)]
        assert _is_in_quoted_span(25, spans) is False

    def test_position_at_span_start(self):
        spans = [(5, 20)]
        assert _is_in_quoted_span(5, spans) is True

    def test_position_at_span_end(self):
        spans = [(5, 20)]
        assert _is_in_quoted_span(20, spans) is False

    def test_empty_spans(self):
        assert _is_in_quoted_span(10, []) is False


# ───────────────────────────────────────────────────────────────────────
# Speculative framing: editorial prose triggers (should still fire)
# ───────────────────────────────────────────────────────────────────────

class TestSpeculativeFramingEditorialProse:
    """Speculative hedges in editorial prose should still fire when 5+ accumulate."""

    def test_editorial_hedges_still_fire(self):
        """5+ speculative markers in editorial prose should trigger the device."""
        text = (
            "Meta could potentially face regulatory headwinds. "
            "There is a chance the company loses its AI bet. "
            "This suggests that revenue could decline further. "
            "If Meta were to divest its VR division, the consequences "
            "could change the entire competitive landscape. "
            "The restructuring raises the possibility of further layoffs. "
            "I wouldn't rule it out as a real risk."
        )
        devices = detect_framing_devices(text)
        spec = [d for d in devices if d.device_type == "speculative_framing"]
        assert len(spec) >= 5, (
            f"Expected 5+ speculative_framing markers in editorial prose, "
            f"got {len(spec)}"
        )


# ───────────────────────────────────────────────────────────────────────
# Speculative framing: in-quote suppression (should NOT fire)
# ───────────────────────────────────────────────────────────────────────

class TestSpeculativeFramingQuoteSuppression:
    """Speculative hedges inside quotes should not count toward threshold."""

    def test_analyst_quotes_suppressed(self):
        """Financial article with analyst hedges inside quotes should not
        trigger speculative_framing even with 7+ quoted hedges."""
        text = (
            'BofA analyst Sarah Chen wrote: "We could potentially see '
            'a rerating. There is a chance revenue accelerates in H2. '
            'This suggests that margins could improve. '
            'I wouldn\'t rule it out as a real possibility. '
            'If management were to announce a buyback, it '
            'could change the trajectory. The results raise the '
            'possibility of a sustainable beat-and-raise cycle." '
            "Meta reported quarterly results Tuesday."
        )
        devices = detect_framing_devices(text)
        spec = [d for d in devices if d.device_type == "speculative_framing"]
        assert len(spec) == 0, (
            f"Expected 0 speculative_framing in all-quoted hedges, "
            f"got {len(spec)}: {[d.evidence_text for d in spec]}"
        )

    def test_smart_quotes_suppressed(self):
        """Same suppression works with smart quotes."""
        text = (
            '\u201cWe could potentially see a major shift,\u201d said the analyst. '
            '\u201cThere is a chance this is the turning point.\u201d '
            '\u201cI wouldn\u2019t bet against Meta here,\u201d she added. '
            '\u201cThis suggests that revenue could be accelerating.\u201d '
            '\u201cIf they were to cut capex, it could change everything.\u201d '
            '\u201cThe results raise the possibility of a rerating.\u201d '
            "The stock closed up 3%."
        )
        devices = detect_framing_devices(text)
        spec = [d for d in devices if d.device_type == "speculative_framing"]
        assert len(spec) == 0, (
            f"Expected 0 speculative_framing in smart-quoted hedges, "
            f"got {len(spec)}"
        )

    def test_mixed_editorial_and_quoted(self):
        """Only editorial-prose hedges should count, not quoted ones."""
        text = (
            "Meta could potentially face headwinds. "  # editorial — counts
            '"I wouldn\'t rule it out," the analyst said. '  # quoted — skip
            "The stock might decline further. "  # editorial — counts
            '"Revenue may be improving," Chen noted. '  # quoted — skip
            '"This could be the turning point," she added. '  # quoted — skip
            "Results were mixed."
        )
        devices = detect_framing_devices(text)
        spec = [d for d in devices if d.device_type == "speculative_framing"]
        # Only 2 editorial hedges, well below threshold of 5
        assert len(spec) == 0, (
            f"Expected 0 speculative_framing with only 2 editorial hedges, "
            f"got {len(spec)}"
        )


# ───────────────────────────────────────────────────────────────────────
# Real-world financial article pattern
# ───────────────────────────────────────────────────────────────────────

class TestFinancialArticlePattern:
    """Realistic financial article with analyst commentary."""

    def test_bofa_research_note_style(self):
        """BofA-style research note with frequent hedging should not trigger."""
        text = (
            "Bank of America published a new research note on Meta Wednesday. "
            '"We could potentially see upside to our $700 target," analyst '
            'Justin Post wrote. "There is a chance revenue surprises to the '
            'upside. This suggests that margins could improve faster than '
            'consensus expects. I wouldn\'t rule out a beat-and-raise quarter. '
            'If management were to announce a buyback, it could change the '
            'trajectory. The AI progress raises the possibility of a '
            'sustainable rerating." '
            "Meta shares rose 2.4% in premarket trading."
        )
        devices = detect_framing_devices(text)
        spec = [d for d in devices if d.device_type == "speculative_framing"]
        assert len(spec) == 0, (
            f"BofA research note style should not trigger speculative_framing, "
            f"got {len(spec)} markers"
        )

    def test_motley_fool_editorial_hedging(self):
        """Motley Fool editorial with 5+ unquoted hedges should still fire."""
        text = (
            "Meta could potentially be overbuilding its AI infrastructure. "
            "There is a chance the company has bitten off more than it can chew. "
            "This suggests that margins could decline in the near term. "
            "If Meta were to lose its AI bet, shareholders would pay the price. "
            "The capex spree raises the possibility of a capex trap. "
            "I wouldn't bet against a major strategic reversal."
        )
        devices = detect_framing_devices(text)
        spec = [d for d in devices if d.device_type == "speculative_framing"]
        assert len(spec) >= 5, (
            f"Editorial hedging (no quotes) should trigger speculative_framing, "
            f"got {len(spec)}"
        )
