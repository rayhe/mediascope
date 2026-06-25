"""Tests for mediascope.quality.citations — citation extraction and grading.

Covers:
    - URL extraction from text
    - Source grading (primary/secondary/tertiary)
    - Domain extraction
    - Attribution extraction ("according to" patterns)
    - Formal citation extraction ([1], (Author 2024))
    - Citation report statistics
    - Edge cases (no URLs, malformed URLs, duplicate URLs)
"""

import pytest
from mediascope.quality.citations import (
    PRIMARY_DOMAINS,
    SECONDARY_DOMAINS,
    Citation,
    extract_citations,
    grade_source,
    citation_report,
    _extract_domain,
)


# ── Source grading ───────────────────────────────────────────────────

class TestSourceGrading:
    """Test grade_source() domain-based classification."""

    def test_sec_gov_is_primary(self):
        assert grade_source("https://www.sec.gov/cgi-bin/browse-edgar") == "primary"

    def test_sec_subdomain_is_primary(self):
        assert grade_source("https://efts.sec.gov/LATEST/search-index") == "primary"

    def test_ftc_gov_is_primary(self):
        assert grade_source("https://www.ftc.gov/legal-library/browse/cases") == "primary"

    def test_arxiv_is_primary(self):
        assert grade_source("https://arxiv.org/abs/2301.12345") == "primary"

    def test_pubmed_is_primary(self):
        assert grade_source("https://pubmed.ncbi.nlm.nih.gov/12345678/") == "primary"

    def test_courtlistener_is_primary(self):
        assert grade_source("https://www.courtlistener.com/opinion/12345/") == "primary"

    def test_doi_org_is_primary(self):
        assert grade_source("https://doi.org/10.1234/example") == "primary"

    def test_reuters_is_secondary(self):
        assert grade_source("https://www.reuters.com/technology/article-123") == "secondary"

    def test_nytimes_is_secondary(self):
        assert grade_source("https://www.nytimes.com/2026/01/15/technology/meta-ai.html") == "secondary"

    def test_wsj_is_secondary(self):
        assert grade_source("https://www.wsj.com/articles/some-article") == "secondary"

    def test_bbc_is_secondary(self):
        assert grade_source("https://www.bbc.com/news/technology-12345") == "secondary"

    def test_guardian_is_secondary(self):
        assert grade_source("https://www.theguardian.com/technology/article") == "secondary"

    def test_bloomberg_is_secondary(self):
        assert grade_source("https://www.bloomberg.com/news/articles/story") == "secondary"

    def test_random_blog_is_tertiary(self):
        assert grade_source("https://myblog.wordpress.com/post/123") == "tertiary"

    def test_substack_is_tertiary(self):
        assert grade_source("https://someone.substack.com/p/hot-take") == "tertiary"

    def test_twitter_is_tertiary(self):
        assert grade_source("https://twitter.com/user/status/123456") == "tertiary"

    def test_medium_is_tertiary(self):
        assert grade_source("https://medium.com/@user/some-article-abc123") == "tertiary"

    def test_wikipedia_is_tertiary(self):
        assert grade_source("https://en.wikipedia.org/wiki/Meta_Platforms") == "tertiary"


# ── Domain extraction ────────────────────────────────────────────────

class TestDomainExtraction:
    """Test _extract_domain() helper."""

    def test_strips_www(self):
        assert _extract_domain("https://www.sec.gov/path") == "sec.gov"

    def test_preserves_subdomain(self):
        assert _extract_domain("https://efts.sec.gov/path") == "efts.sec.gov"

    def test_no_scheme(self):
        # urlparse handles scheme-less URLs poorly but shouldn't crash
        result = _extract_domain("not-a-url")
        assert isinstance(result, str)

    def test_empty_string(self):
        result = _extract_domain("")
        assert result == ""

    def test_complex_url(self):
        url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=reddit&type=SC+13D"
        assert _extract_domain(url) == "sec.gov"


# ── Citation extraction ─────────────────────────────────────────────

class TestCitationExtraction:
    """Test extract_citations() on real-world-like text."""

    def test_extracts_url(self):
        text = "According to SEC filings (https://www.sec.gov/cgi-bin/browse-edgar), Reddit has 47.9M Class B shares."
        citations = extract_citations(text)
        urls = [c.url for c in citations if c.url]
        assert any("sec.gov" in u for u in urls)

    def test_url_graded_correctly(self):
        text = "Source: https://www.sec.gov/cgi-bin/browse-edgar?CIK=reddit"
        citations = extract_citations(text)
        url_cits = [c for c in citations if c.url]
        assert len(url_cits) >= 1
        assert url_cits[0].source_type == "primary"

    def test_extracts_according_to_attribution(self):
        text = "According to Bloomberg, the deal was valued at $2B."
        citations = extract_citations(text)
        attr_cits = [c for c in citations if c.verification_method == "attribution_extraction"]
        assert len(attr_cits) >= 1
        assert any("Bloomberg" in c.text for c in attr_cits)

    def test_extracts_as_reported_by(self):
        text = "The merger is pending, as reported by Reuters in its evening dispatch."
        citations = extract_citations(text)
        attr_cits = [c for c in citations if c.verification_method == "attribution_extraction"]
        assert len(attr_cits) >= 1

    def test_extracts_formal_bracketed_citation(self):
        text = "The effect size was medium [1]. Previous studies found similar results [2]."
        citations = extract_citations(text)
        formal = [c for c in citations if c.verification_method == "formal_citation_extraction"]
        assert len(formal) >= 2

    def test_extracts_parenthetical_citation(self):
        text = "This follows the VADER methodology (Hutto & Gilbert, 2014)."
        citations = extract_citations(text)
        formal = [c for c in citations if c.verification_method == "formal_citation_extraction"]
        assert len(formal) >= 1

    def test_deduplicates_urls(self):
        text = (
            "See https://sec.gov/filing for details. "
            "The same filing at https://sec.gov/filing confirms this."
        )
        citations = extract_citations(text)
        url_cits = [c for c in citations if c.url]
        urls = [c.url for c in url_cits]
        assert len(urls) == len(set(urls))

    def test_empty_text_returns_empty(self):
        assert extract_citations("") == []

    def test_no_citations_returns_empty(self):
        text = "This is a plain sentence with no sources or references whatsoever."
        citations = extract_citations(text)
        # Might have 0 or very few — no URLs, no attributions, no formal cites
        url_cits = [c for c in citations if c.url]
        assert len(url_cits) == 0

    def test_multiple_citation_types_combined(self):
        text = (
            "According to SEC filings (https://sec.gov/edgar), Advance holds a 33.5% stake. "
            "This aligns with prior research (Gentzkow & Shapiro, 2010). "
            "As reported by the Financial Times, the deal includes board seats [3]."
        )
        citations = extract_citations(text)
        # Should have at least: 1 URL, 1+ attribution, 1+ formal cite
        assert len(citations) >= 3

    def test_url_trailing_punctuation_stripped(self):
        text = "See https://www.sec.gov/filing. Also check https://www.ftc.gov/case, which confirms."
        citations = extract_citations(text)
        url_cits = [c for c in citations if c.url]
        for c in url_cits:
            assert not c.url.endswith(".")
            assert not c.url.endswith(",")


# ── Citation report ──────────────────────────────────────────────────

class TestCitationReport:
    """Test citation_report() statistics generation."""

    def test_empty_list_returns_zeroes(self):
        report = citation_report([])
        assert report["total"] == 0
        assert report["primary_ratio"] == 0.0
        assert report["verified"] == 0

    def test_counts_by_source_type(self):
        citations = [
            Citation(text="SEC filing", url="https://sec.gov/f", source_type="primary", domain="sec.gov"),
            Citation(text="Reuters", url="https://reuters.com/a", source_type="secondary", domain="reuters.com"),
            Citation(text="Blog post", url="https://blog.example.com/p", source_type="tertiary", domain="blog.example.com"),
        ]
        report = citation_report(citations)
        assert report["total"] == 3
        assert report["by_source_type"]["primary"] == 1
        assert report["by_source_type"]["secondary"] == 1
        assert report["by_source_type"]["tertiary"] == 1

    def test_primary_ratio_calculated(self):
        citations = [
            Citation(text="a", source_type="primary"),
            Citation(text="b", source_type="primary"),
            Citation(text="c", source_type="secondary"),
            Citation(text="d", source_type="tertiary"),
        ]
        report = citation_report(citations)
        assert report["primary_ratio"] == 0.5  # 2/4

    def test_domain_breakdown(self):
        citations = [
            Citation(text="a", domain="sec.gov"),
            Citation(text="b", domain="sec.gov"),
            Citation(text="c", domain="reuters.com"),
        ]
        report = citation_report(citations)
        assert report["domains"]["sec.gov"] == 2
        assert report["domains"]["reuters.com"] == 1

    def test_verified_count(self):
        citations = [
            Citation(text="a", verified=True),
            Citation(text="b", verified=False),
            Citation(text="c", verified=True),
        ]
        report = citation_report(citations)
        assert report["verified"] == 2
        assert report["unverified"] == 1
