"""Tests for mediascope.quality.claims — claim extraction and evidence mapping.

Covers:
    - Statistic claim detection (percentages, dollar amounts, multipliers)
    - Quote claim detection
    - Citation signal detection
    - Assertion detection (unsupported factual claims)
    - Source attribution detection
    - Claim-to-evidence mapping
    - Unsupported claims ratio
    - Confidence scoring
    - Edge cases (empty text, no claims)
"""

import pytest
from mediascope.quality.claims import (
    Claim,
    extract_claims,
    map_claims_to_evidence,
    unsupported_claims_ratio,
)


# ── Statistic detection ─────────────────────────────────────────────

class TestStatisticDetection:
    """Detects numerical/statistical claims."""

    def test_percentage(self):
        text = "Meta's revenue grew 33% year-over-year in Q1 2026."
        claims = extract_claims(text)
        stat_claims = [c for c in claims if c.evidence_type == "statistic"]
        assert len(stat_claims) >= 1

    def test_dollar_amount_billion(self):
        text = "Reality Labs posted a $4.03 billion operating loss last quarter."
        claims = extract_claims(text)
        stat_claims = [c for c in claims if c.evidence_type == "statistic"]
        assert len(stat_claims) >= 1

    def test_dollar_amount_plain(self):
        text = "The fine was set at $5 million by the court."
        claims = extract_claims(text)
        stat_claims = [c for c in claims if c.evidence_type == "statistic"]
        assert len(stat_claims) >= 1

    def test_multiplier(self):
        text = "Smart glasses outsell VR headsets 3x in the consumer market."
        claims = extract_claims(text)
        stat_claims = [c for c in claims if c.evidence_type == "statistic"]
        assert len(stat_claims) >= 1


# ── Quote detection ──────────────────────────────────────────────────

class TestQuoteDetection:
    """Detects quoted claims."""

    def test_straight_quotes(self):
        text = 'The spokesperson said "We take user privacy very seriously and have implemented comprehensive safeguards."'
        claims = extract_claims(text)
        quote_claims = [c for c in claims if c.evidence_type == "quote"]
        assert len(quote_claims) >= 1

    def test_curly_quotes(self):
        text = 'The CEO stated \u201cThis is a transformative moment for the company and its mission.\u201d'
        claims = extract_claims(text)
        quote_claims = [c for c in claims if c.evidence_type == "quote"]
        assert len(quote_claims) >= 1


# ── Citation signal detection ────────────────────────────────────────

class TestCitationSignalDetection:
    """Detects citation-backed claims."""

    def test_according_to(self):
        text = "According to SEC filings, Advance Publications holds a 33.5% voting stake in Reddit."
        claims = extract_claims(text)
        cite_claims = [c for c in claims if c.evidence_type in ("citation", "statistic")]
        assert len(cite_claims) >= 1

    def test_as_reported_by(self):
        text = "As reported by Bloomberg, the deal includes two board seats and veto power."
        claims = extract_claims(text)
        assert len(claims) >= 1

    def test_study_by(self):
        text = "A study by Stanford HAI found that AI coverage sentiment varies by 20 percentage points across publications."
        claims = extract_claims(text)
        assert len(claims) >= 1


# ── Assertion detection ──────────────────────────────────────────────

class TestAssertionDetection:
    """Detects unsupported factual assertions."""

    def test_superlative_assertion(self):
        text = "Wired is the most adversarial publication in its coverage of Meta among major tech outlets."
        claims = extract_claims(text)
        assertion_claims = [c for c in claims if c.evidence_type == "assertion"]
        assert len(assertion_claims) >= 1

    def test_proves_assertion(self):
        text = "The pattern clearly demonstrates that editorial decisions are driven by financial interests."
        claims = extract_claims(text)
        assertion_claims = [c for c in claims if c.evidence_type == "assertion"]
        assert len(assertion_claims) >= 1

    def test_never_assertion(self):
        text = "The publication has never disclosed its parent company's competing financial interests."
        claims = extract_claims(text)
        assertion_claims = [c for c in claims if c.evidence_type == "assertion"]
        assert len(assertion_claims) >= 1


# ── Source attribution ───────────────────────────────────────────────

class TestSourceAttribution:
    """Tests has_source field on extracted claims."""

    def test_url_counts_as_source(self):
        text = "The filing is available at https://sec.gov/cgi-bin/browse-edgar with the full disclosure."
        claims = extract_claims(text)
        sourced = [c for c in claims if c.has_source]
        # URL present → has_source
        if claims:
            assert any(c.has_source for c in claims)

    def test_according_to_counts_as_source(self):
        text = "According to Reuters, the company plans to cut 10,000 positions across all divisions."
        claims = extract_claims(text)
        if claims:
            assert any(c.has_source for c in claims)

    def test_bare_assertion_no_source(self):
        text = "This is the largest conflict of interest in media history."
        claims = extract_claims(text)
        if claims:
            assert any(not c.has_source for c in claims)


# ── Claim-to-evidence mapping ───────────────────────────────────────

class TestClaimMapping:
    """Tests map_claims_to_evidence() aggregation."""

    def test_maps_sourced_and_unsourced(self):
        text = (
            "According to SEC filings, Advance holds a 33.5% stake in Reddit. "
            "This is the largest undisclosed conflict in tech media."
        )
        claims = extract_claims(text)
        mapping = map_claims_to_evidence(claims)
        assert "sourced" in mapping
        assert "unsourced" in mapping
        assert mapping["total"] == len(claims)

    def test_by_type_populated(self):
        text = (
            "Revenue grew 33% year-over-year. "
            'The CEO said "We are committed to transparency." '
            "According to Bloomberg, the deal was worth $2B."
        )
        claims = extract_claims(text)
        mapping = map_claims_to_evidence(claims)
        assert "by_type" in mapping
        assert isinstance(mapping["by_type"], dict)

    def test_sourced_ratio_between_0_and_1(self):
        text = (
            "According to the FTC, Meta violated antitrust law. "
            "This proves Meta is a monopoly. "
            "The fine was $5 billion, per court records."
        )
        claims = extract_claims(text)
        mapping = map_claims_to_evidence(claims)
        assert 0.0 <= mapping["sourced_ratio"] <= 1.0

    def test_empty_claims_returns_zeroes(self):
        mapping = map_claims_to_evidence([])
        assert mapping["total"] == 0
        assert mapping["sourced_ratio"] == 0.0


# ── Unsupported claims ratio ─────────────────────────────────────────

class TestUnsupportedClaimsRatio:
    """Tests unsupported_claims_ratio() calculation."""

    def test_all_sourced_returns_0(self):
        claims = [
            Claim(text="a", evidence_type="statistic", has_source=True),
            Claim(text="b", evidence_type="citation", has_source=True),
        ]
        assert unsupported_claims_ratio(claims) == 0.0

    def test_all_unsourced_returns_1(self):
        claims = [
            Claim(text="a", evidence_type="assertion", has_source=False),
            Claim(text="b", evidence_type="assertion", has_source=False),
        ]
        assert unsupported_claims_ratio(claims) == 1.0

    def test_mixed_returns_correct_ratio(self):
        claims = [
            Claim(text="a", evidence_type="statistic", has_source=True),
            Claim(text="b", evidence_type="assertion", has_source=False),
            Claim(text="c", evidence_type="statistic", has_source=True),
            Claim(text="d", evidence_type="assertion", has_source=False),
        ]
        assert unsupported_claims_ratio(claims) == 0.5

    def test_empty_returns_0(self):
        assert unsupported_claims_ratio([]) == 0.0


# ── Confidence scoring ───────────────────────────────────────────────

class TestConfidenceScoring:
    """Tests confidence scoring on extracted claims."""

    def test_statistics_get_higher_confidence(self):
        text = "Revenue grew 33% year-over-year to $56.3 billion."
        claims = extract_claims(text)
        stat_claims = [c for c in claims if c.evidence_type == "statistic"]
        for claim in stat_claims:
            assert claim.confidence >= 0.5

    def test_confidence_between_0_and_1(self):
        text = (
            "According to SEC filings, revenue was $56B. "
            "This is the best quarter ever. "
            'The analyst said "Results exceeded expectations."'
        )
        claims = extract_claims(text)
        for claim in claims:
            assert 0.0 <= claim.confidence <= 1.0


# ── Edge cases ───────────────────────────────────────────────────────

class TestEdgeCases:
    """Edge cases for claim extraction."""

    def test_empty_text_returns_empty(self):
        assert extract_claims("") == []

    def test_short_sentences_skipped(self):
        text = "Hi.\nOk.\nYes."
        claims = extract_claims(text)
        assert len(claims) == 0

    def test_no_claims_in_narrative(self):
        text = "The sun was setting behind the hills as the wind blew gently through the trees."
        claims = extract_claims(text)
        # Pure narrative should have 0 or near-0 claims
        assertion_claims = [c for c in claims if c.evidence_type == "assertion"]
        stat_claims = [c for c in claims if c.evidence_type == "statistic"]
        assert len(stat_claims) == 0
