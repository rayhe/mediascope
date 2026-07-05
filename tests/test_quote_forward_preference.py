"""Test that _extract_nearby_quote prefers forward quotes over backward quotes.

Regression test for the Ji/Gong misattribution bug where a preceding
speaker's quote was incorrectly assigned to the next speaker.
"""
import pytest
from mediascope.analyze.sources import _extract_nearby_quote, extract_sources


class TestQuoteForwardPreference:
    """Ensure nearby-quote extraction prefers forward matches."""

    def test_forward_quote_preferred_over_backward(self):
        """When both forward and backward quotes exist, forward wins."""
        text = (
            '"This is speaker A quote," says A. '
            'Speaker B, a professor, agrees. "This is speaker B quote."'
        )
        # Reference position points at "Speaker B"
        ref_start = text.index("Speaker B, a professor")
        ref_end = ref_start + len("Speaker B, a professor")
        quote = _extract_nearby_quote(text, ref_start, ref_end)
        assert "speaker B quote" in quote

    def test_backward_fallback_when_no_forward_quote(self):
        """When only a backward quote exists, it is used."""
        text = '"This is the quote," says SpeakerName. And the article continues without more quotes.'
        ref_start = text.index("SpeakerName")
        ref_end = ref_start + len("SpeakerName")
        quote = _extract_nearby_quote(text, ref_start, ref_end)
        assert "This is the quote" in quote

    def test_mittr_ji_gong_misattribution_fixed(self):
        """Specific regression: Ji should NOT get Gong's quote."""
        text = (
            'Gong says, it should have been uncovered easily, before the agent '
            'was deployed. "It\'s really surprising," he says. '
            '"I don\'t understand why they didn\'t find this simple problem."\n\n'
            'Jessica Ji, a senior research analyst at Georgetown\'s Center for '
            'Security and Emerging Technology, agrees. '
            '"It raises questions like: Were there even guardrails in place?" '
            'she says. "Did anyone think to test for this kind of scenario?"'
        )
        sources = extract_sources(text)
        ji_sources = [s for s in sources if s.name == "Jessica Ji"]
        assert ji_sources, "Jessica Ji should be detected as a source"
        ji = ji_sources[0]
        assert "guardrails" in ji.quote, (
            f"Ji should have her own quote about guardrails, got: {ji.quote!r}"
        )
        assert "really surprising" not in ji.quote, (
            "Ji should NOT have Gong's 'really surprising' quote"
        )
