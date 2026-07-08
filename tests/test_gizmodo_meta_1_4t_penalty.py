"""Tests for source extraction improvements from Gizmodo $1.4T article.

Discovered in MediaScope Type A iteration 2026-07-07 13:00 PT.
Tests: "per [Source]" attribution, "the filing states", "attorneys for [Entity]".
"""

import pytest
from mediascope.analyze.sources import extract_sources


class TestPerSourceAttribution:
    """Test "per [Source]" compact indirect attribution pattern."""

    def test_per_reuters(self):
        text = (
            "The penalties were calculated by multiplying "
            "the number of affected users by the statutory damages, per Reuters."
        )
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Reuters" in names
        reuters = next(s for s in sources if s.name == "Reuters")
        assert reuters.attribution_verb == "per"
        assert reuters.source_type == "news_outlet"

    def test_per_bloomberg(self):
        text = "The deal closed at $4.2 billion, per Bloomberg."
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Bloomberg" in names

    def test_per_the_company(self):
        text = "Revenue grew 15% year-over-year, per the company."
        sources = extract_sources(text)
        # "the company" should not match — requires capital letter after "per [the]"
        # Actually "company" is lowercase so it shouldn't match
        names = [s.name for s in sources]
        assert "company" not in " ".join(names).lower() or len(sources) == 0

    def test_per_wall_street_journal(self):
        text = "Three executives were let go, per The Wall Street Journal."
        sources = extract_sources(text)
        names = [s.name for s in sources]
        # Should capture multi-word source
        matched = [n for n in names if "Wall Street" in n]
        assert len(matched) >= 1


class TestFilingAsSource:
    """Test "the filing/complaint states/says" document-as-source pattern."""

    def test_the_filing_states(self):
        text = (
            'The filing states. "The AGs\' demand exceeds even those '
            'record figures by several orders of magnitude."'
        )
        sources = extract_sources(text)
        # Should detect documentary source
        doc_sources = [s for s in sources if s.source_type == "documentary"]
        assert len(doc_sources) >= 1

    def test_the_complaint_alleges(self):
        text = (
            "The complaint alleges that the company engaged in "
            "systematic deception of consumers."
        )
        sources = extract_sources(text)
        doc_sources = [s for s in sources if s.source_type == "documentary"]
        assert len(doc_sources) >= 1

    def test_the_lawsuit_claims(self):
        text = "The lawsuit claims damages exceeding $500 million."
        sources = extract_sources(text)
        doc_sources = [s for s in sources if s.source_type == "documentary"]
        assert len(doc_sources) >= 1

    def test_the_ruling_notes(self):
        text = (
            "The ruling notes that the defendant failed to meet "
            "the burden of proof on three of five counts."
        )
        sources = extract_sources(text)
        doc_sources = [s for s in sources if s.source_type == "documentary"]
        assert len(doc_sources) >= 1


class TestAttorneysForEntity:
    """Test "the attorneys/lawyers for [Entity]" legal party pattern."""

    def test_attorneys_for_meta_argued(self):
        text = (
            "The attorneys for Meta argued that the penalty was "
            "disproportionate to the alleged violations."
        )
        sources = extract_sources(text)
        legal = [s for s in sources if s.source_type == "legal_party"]
        assert len(legal) >= 1
        assert any("attorneys for Meta" in s.name for s in legal)

    def test_lawyers_for_google_claimed(self):
        text = (
            "Lawyers for Google claimed the search data was "
            "anonymized before any processing occurred."
        )
        sources = extract_sources(text)
        legal = [s for s in sources if s.source_type == "legal_party"]
        assert len(legal) >= 1

    def test_counsel_representing_apple(self):
        text = (
            "Counsel representing Apple argued that the patent "
            "claims were invalid under prior art."
        )
        sources = extract_sources(text)
        legal = [s for s in sources if s.source_type == "legal_party"]
        assert len(legal) >= 1


class TestGizmodoFullArticle:
    """Integration test: full Gizmodo $1.4T penalty article."""

    @pytest.fixture
    def article_text(self):
        try:
            return open(
                "examples/sample_output/"
                "gizmodo_meta_1_4t_penalty_2026_07_07_article.txt"
            ).read()
        except FileNotFoundError:
            pytest.skip("Article text not available")

    def test_detects_at_least_3_sources(self, article_text):
        sources = extract_sources(article_text)
        assert len(sources) >= 3, (
            f"Expected >= 3 sources, got {len(sources)}: "
            f"{[s.name for s in sources]}"
        )

    def test_detects_reuters(self, article_text):
        sources = extract_sources(article_text)
        names = [s.name for s in sources]
        assert any("Reuters" in n for n in names), (
            f"Expected Reuters in sources, got: {names}"
        )

    def test_detects_legal_party(self, article_text):
        sources = extract_sources(article_text)
        legal = [s for s in sources if s.source_type == "legal_party"]
        assert len(legal) >= 1, (
            f"Expected >= 1 legal_party source, got: "
            f"{[s.name for s in sources]}"
        )

    def test_detects_documentary_source(self, article_text):
        sources = extract_sources(article_text)
        doc = [s for s in sources if s.source_type == "documentary"]
        assert len(doc) >= 1, (
            f"Expected >= 1 documentary source, got: "
            f"{[s.name for s in sources]}"
        )
