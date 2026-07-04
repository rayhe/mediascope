"""Tests for MarketWatch Meta cloud pivot article (Jul 1, 2026).

Regression tests confirming:
1. Financial-defeat emotional language terms are detected.
2. ironic_quotation false positives for attributed analyst quotes are
   suppressed ("rational", "to fund more, not less, capex.").
3. Simple competitive_deficit pattern fires for "lagged behind [Company]
   and [Company]" without requiring "competitors including" preamble.

Discovery: Type A article deep dive, 2026-07-04 00:00 PT.
"""

import pytest

from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sentiment import EMOTIONAL_LANGUAGE


# ---------------------------------------------------------------------------
# Article fragment fixtures
# ---------------------------------------------------------------------------

RATIONAL_FRAGMENT = (
    'Dow Jones Institutional News also reported on the initiative on Wednesday, '
    'citing a person familiar.\n\n'
    'Creating a cloud platform is a "rational" move as Meta continues to raise '
    'its AI spending, Baird analyst Colin Sebastian wrote in a Wednesday note. '
    'Meta plans to devote up to $145 billion toward capital expenditures this year.'
)

FUND_MORE_FRAGMENT = (
    'However, Jefferies analyst Brent Thill had a different perspective. '
    'In a Wednesday note, Thill called overbuilding concerns "backward," '
    'highlighting that demand for computing power continues to outstrip supply. '
    'He believes a new cloud business will increase utilization, improve '
    'return on invested capital and boost cash flow '
    '"to fund more, not less, capex."'
)

LAGGED_BEHIND_FRAGMENT = (
    'Since the inception of Meta Superintelligence Labs last year, the company '
    'has released a new Muse Spark model but has still lagged behind Anthropic '
    'and OpenAI.'
)

GIVING_UP_FRAGMENT = (
    'D.A. Davidson analyst Gil Luria sees Meta\'s reported cloud ambitions as '
    'a sign that the company is "giving up on frontier AI" to sell computing '
    'power instead.'
)


# ---------------------------------------------------------------------------
# Financial-defeat emotional language
# ---------------------------------------------------------------------------

class TestFinancialDefeatTerms:
    """Financial-defeat terms added to EMOTIONAL_LANGUAGE list."""

    @pytest.mark.parametrize("term", [
        "throwing in the towel",
        "beaten down",
        "giving up",
        "overspending",
        "overbuilt",
        "lagged behind",
        "playing catch-up",
        "scaling back",
        "cash burn",
        "retreat",
        "white flag",
        "pulled back",
        "reined in",
        "fallen behind",
    ])
    def test_financial_defeat_term_in_list(self, term):
        """Each financial-defeat term should be in EMOTIONAL_LANGUAGE."""
        assert term in EMOTIONAL_LANGUAGE, (
            f"Financial-defeat term {term!r} missing from EMOTIONAL_LANGUAGE"
        )


# ---------------------------------------------------------------------------
# ironic_quotation attribution filtering
# ---------------------------------------------------------------------------

class TestIronicQuotationAttribution:
    """Analyst-attributed quotes should not be flagged as scare quotes."""

    def test_rational_suppressed(self):
        """'rational' is Colin Sebastian's direct assessment, not a scare quote."""
        devices = detect_framing_devices(RATIONAL_FRAGMENT)
        ironic = [d for d in devices if d.device_type == "ironic_quotation"]
        matched_texts = [d.evidence_text.strip('" \u201c\u201d') for d in ironic]
        assert "rational" not in matched_texts, (
            '"rational" should be suppressed as analyst-attributed quote '
            '(Colin Sebastian, Baird)'
        )

    def test_fund_more_suppressed(self):
        """'to fund more, not less, capex.' is Thill's direct quote."""
        devices = detect_framing_devices(FUND_MORE_FRAGMENT)
        ironic = [d for d in devices if d.device_type == "ironic_quotation"]
        matched_texts = [d.evidence_text.strip('" \u201c\u201d') for d in ironic]
        assert "to fund more, not less, capex." not in matched_texts, (
            '"to fund more, not less, capex." should be suppressed as '
            'analyst-attributed quote (Brent Thill, Jefferies)'
        )

    def test_giving_up_preserved(self):
        """'giving up on frontier AI' IS a genuine editorial framing device."""
        devices = detect_framing_devices(GIVING_UP_FRAGMENT)
        ironic = [d for d in devices if d.device_type == "ironic_quotation"]
        assert len(ironic) >= 1, (
            '"giving up on frontier AI" should be detected as ironic_quotation'
        )


# ---------------------------------------------------------------------------
# competitive_deficit simple pattern
# ---------------------------------------------------------------------------

class TestCompetitiveDeficitSimple:
    """Simple 'lagged behind [Company] and [Company]' pattern detection."""

    def test_lagged_behind_named_companies(self):
        """'lagged behind Anthropic and OpenAI' should trigger competitive_deficit."""
        devices = detect_framing_devices(LAGGED_BEHIND_FRAGMENT)
        cd = [d for d in devices if d.device_type == "competitive_deficit"]
        assert len(cd) >= 1, (
            "'lagged behind Anthropic and OpenAI' should trigger "
            "competitive_deficit without 'competitors including' preamble"
        )

    @pytest.mark.parametrize("phrase,expected_match", [
        ("has lagged behind Google and Microsoft in AI", True),
        ("trails behind OpenAI and Anthropic", True),
        ("fallen behind Apple and Samsung", True),
        ("playing catch-up with Google and Amazon", True),
        ("lagged behind the pack", False),  # No named companies
    ])
    def test_competitive_deficit_variants(self, phrase, expected_match):
        """Various simple competitive_deficit phrasings with named companies."""
        devices = detect_framing_devices(phrase)
        cd = [d for d in devices if d.device_type == "competitive_deficit"]
        if expected_match:
            assert len(cd) >= 1, (
                f"{phrase!r} should trigger competitive_deficit"
            )
        else:
            assert len(cd) == 0, (
                f"{phrase!r} should NOT trigger competitive_deficit "
                "(no named companies)"
            )


# ---------------------------------------------------------------------------
# Attribution filter: "wrote" verb
# ---------------------------------------------------------------------------

class TestWroteAttribution:
    """'wrote' as attribution verb should suppress ironic_quotation."""

    def test_wrote_in_lookback(self):
        """Short quoted term with 'wrote' in lookback should be suppressed."""
        text = (
            'The analyst wrote in a Wednesday note that Meta\'s strategy is '
            '"rational" given the current market dynamics.'
        )
        devices = detect_framing_devices(text)
        ironic = [d for d in devices if d.device_type == "ironic_quotation"]
        matched = [d.evidence_text.strip('" \u201c\u201d') for d in ironic]
        assert "rational" not in matched, (
            '"rational" preceded by "wrote" should be suppressed'
        )

    def test_wrote_in_lookahead(self):
        """Org + analyst name + 'wrote' in post-quote context should suppress."""
        text = (
            'The cloud platform is a "rational" move, Morgan Stanley '
            'analyst FirstName LastName wrote in a research note.'
        )
        devices = detect_framing_devices(text)
        ironic = [d for d in devices if d.device_type == "ironic_quotation"]
        matched = [d.evidence_text.strip('" \u201c\u201d') for d in ironic]
        assert "rational" not in matched, (
            '"rational" with post-quote "[org] [analyst] wrote" should '
            'be suppressed'
        )
