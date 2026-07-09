"""Regression tests for Reuters Meta Iris chip production article (Jul 9, 2026).

Article: "Meta to put AI chip into production in September as it looks to
double computing capacity, memo shows" (Reuters, July 9, 2026).

Covers:
- Entity extraction: Sumitomo Electric (new cluster), Samsung, TSMC, Broadcom,
  Nvidia, AMD, SanDisk, Apple, Morgan Stanley
- Source extraction: inverted analyst attribution ("Morgan Stanley analysts
  said"), compound no-comment subjects ("Samsung Electronics and Sumitomo
  Electric did not respond")
- Sentiment: "floundered" emotional language detection
- Topic classification: ai_development, corporate_strategy
"""

import pytest
from pathlib import Path

ARTICLE_PATH = Path(__file__).parent.parent / (
    "examples/sample_output/"
    "reuters_meta_iris_chip_production_2026_07_09_article.txt"
)

ARTICLE_TEXT = ARTICLE_PATH.read_text() if ARTICLE_PATH.exists() else ""


# ---------------------------------------------------------------------------
# Entity extraction
# ---------------------------------------------------------------------------


class TestEntityExtraction:
    """Entity detection for Reuters Iris chip article."""

    @pytest.fixture(autouse=True)
    def _detect(self):
        from mediascope.analyze.entities import detect_entities
        self.entities = detect_entities(ARTICLE_TEXT)
        self.clusters = {e.cluster for e in self.entities}
        self.canonical_names = {e.canonical_name for e in self.entities}

    def test_meta_detected(self):
        assert "Meta" in self.clusters

    def test_broadcom_detected(self):
        assert "Broadcom" in self.clusters

    def test_tsmc_detected(self):
        assert "TSMC" in self.clusters

    def test_nvidia_detected(self):
        assert "Nvidia" in self.clusters

    def test_amd_detected(self):
        assert "AMD" in self.clusters

    def test_samsung_detected(self):
        assert "Samsung" in self.clusters

    def test_apple_detected(self):
        assert "Apple" in self.clusters

    def test_sumitomo_electric_detected(self):
        """Sumitomo Electric — new entity cluster added for this article."""
        assert "Sumitomo Electric" in self.clusters

    def test_sumitomo_electric_count(self):
        """Sumitomo Electric appears twice in the article."""
        sumitomo_mentions = [
            e for e in self.entities if e.cluster == "Sumitomo Electric"
        ]
        assert len(sumitomo_mentions) >= 2

    def test_sandisk_detected(self):
        """SanDisk (via Storage/Memory cluster) appears in supply chain context."""
        storage = [e for e in self.entities if e.cluster == "Storage/Memory"]
        assert len(storage) >= 1

    def test_morgan_stanley_detected(self):
        """Morgan Stanley detected via Financial Services cluster."""
        assert "Financial Services" in self.clusters
        ms_mentions = [
            e for e in self.entities
            if e.canonical_name == "Morgan Stanley"
        ]
        assert len(ms_mentions) >= 1


# ---------------------------------------------------------------------------
# Source extraction
# ---------------------------------------------------------------------------


class TestSourceExtraction:
    """Source extraction for Reuters Iris chip article."""

    @pytest.fixture(autouse=True)
    def _extract(self):
        from mediascope.analyze.sources import extract_sources
        self.sources = extract_sources(ARTICLE_TEXT)
        self.names = {s.name for s in self.sources}
        self.by_type = {}
        for s in self.sources:
            self.by_type.setdefault(s.source_type, []).append(s)

    def test_morgan_stanley_inverted_analyst(self):
        """'Morgan Stanley analysts said' — inverted analyst attribution.
        
        The org name precedes the role descriptor, unlike the standard
        'Analysts with/at/from [Org]' pattern.
        """
        org_sources = self.by_type.get("organizational", [])
        ms = [s for s in org_sources if "Morgan Stanley" in s.name]
        assert len(ms) >= 1, (
            f"Morgan Stanley not found in organizational sources. "
            f"All sources: {[(s.name, s.source_type) for s in self.sources]}"
        )

    def test_meta_no_comment(self):
        """'Meta declined to comment' detected as no_comment source."""
        no_comments = self.by_type.get("no_comment", [])
        meta_nc = [s for s in no_comments if s.name == "Meta"]
        assert len(meta_nc) >= 1

    def test_sandisk_no_comment(self):
        """'Sandisk declined to comment' detected as no_comment source."""
        no_comments = self.by_type.get("no_comment", [])
        sandisk_nc = [s for s in no_comments if "andisk" in s.name]
        assert len(sandisk_nc) >= 1

    def test_samsung_compound_no_comment(self):
        """'Samsung Electronics and Sumitomo Electric did not respond'
        — compound no-comment subjects must both be extracted."""
        no_comments = self.by_type.get("no_comment", [])
        samsung_nc = [
            s for s in no_comments if "Samsung" in s.name
        ]
        assert len(samsung_nc) >= 1, (
            f"Samsung not in no_comment sources. "
            f"no_comment: {[s.name for s in no_comments]}"
        )

    def test_sumitomo_compound_no_comment(self):
        """Second entity in compound no-comment also extracted."""
        no_comments = self.by_type.get("no_comment", [])
        sumitomo_nc = [
            s for s in no_comments if "Sumitomo" in s.name
        ]
        assert len(sumitomo_nc) >= 1, (
            f"Sumitomo Electric not in no_comment sources. "
            f"no_comment: {[s.name for s in no_comments]}"
        )

    def test_documentary_source(self):
        """Internal memo referenced as documentary source."""
        docs = self.by_type.get("documentary", [])
        assert len(docs) >= 1, "No documentary sources found"


# ---------------------------------------------------------------------------
# Sentiment / emotional language
# ---------------------------------------------------------------------------


class TestSentiment:
    """Emotional language detection for Reuters Iris chip article."""

    def test_floundered_detected(self):
        """'floundered' should be in the passive framing term list."""
        from mediascope.analyze.sentiment import PASSIVE_FRAMING
        terms_lower = {t.lower() for t in PASSIVE_FRAMING}
        assert "floundered" in terms_lower


# ---------------------------------------------------------------------------
# Topic classification
# ---------------------------------------------------------------------------


class TestTopicClassification:
    """Topic classification for Reuters Iris chip article."""

    @pytest.fixture(autouse=True)
    def _classify(self):
        from mediascope.analyze.topics import classify_topic
        results = classify_topic(ARTICLE_TEXT)
        self.topics = [r.topic for r in results]

    def test_ai_development_topic(self):
        """Article about AI chip production should classify as ai_development."""
        assert "ai_development" in self.topics

    def test_corporate_strategy_topic(self):
        """Custom chip effort is a corporate_strategy story."""
        assert "corporate_strategy" in self.topics
