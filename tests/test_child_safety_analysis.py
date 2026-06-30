"""Tests for new entity clusters, source extraction fixes, and framing devices
added in the child safety study analysis iteration (Jun 30, 2026)."""

import sys
sys.path.insert(0, ".")

import pytest
from mediascope.analyze.entities import detect_entities
from mediascope.analyze.framing import detect_framing_devices, summarize_framing
from mediascope.analyze.sources import extract_sources
from mediascope.analyze.sentiment import analyze_composite


# ---- Entity cluster tests ----

class TestNewEntityClusters:
    """Tests for entity clusters added Jun 30, 2026."""

    def test_us_congress_detected(self):
        text = "Congress passed the bill. The Senate Judiciary Committee held hearings."
        entities = detect_entities(text)
        clusters = {e.cluster for e in entities}
        assert "US Congress" in clusters

    def test_academic_research_detected(self):
        text = "Researchers at NYU and Northeastern University conducted the study."
        entities = detect_entities(text)
        clusters = {e.cluster for e in entities}
        assert "Academic/Research" in clusters

    def test_research_centers_detected(self):
        text = "The Cybersafety Research Center published its findings."
        entities = detect_entities(text)
        names = {e.canonical_name for e in entities}
        assert "Cybersafety Research Center" in names

    def test_child_safety_researchers_detected(self):
        text = "Arturo Béjar and Laura Edelson co-authored the report."
        entities = detect_entities(text)
        names = {e.canonical_name for e in entities}
        assert "Arturo Béjar" in names
        assert "Laura Edelson" in names

    def test_child_safety_legislation_detected(self):
        text = "The KIDS Act and KOSA are pending in Congress."
        entities = detect_entities(text)
        clusters = {e.cluster for e in entities}
        assert "Child Safety Legislation" in clusters

    def test_australia_detected(self):
        text = "Australia recently doubled its penalties for social media companies."
        entities = detect_entities(text)
        names = {e.canonical_name for e in entities}
        assert "Australia" in names


# ---- Source extraction fix tests ----

class TestSourceExtractionFixes:
    """Tests for source extraction improvements Jun 30, 2026."""

    def test_meta_spokesperson_said_uppercase_a(self):
        """'A Meta spokesperson said' — uppercase A must match."""
        text = 'A Meta spokesperson said that "the company invests heavily in safety."'
        sources = extract_sources(text)
        # Should find at least the organizational or anonymous spokesperson source
        assert len(sources) >= 1
        source_names = [s.name.lower() for s in sources]
        has_meta = any("meta" in n for n in source_names)
        assert has_meta, f"Expected Meta-related source, got: {source_names}"

    def test_instagram_said_as_org_source(self):
        """'Instagram said' — organizational source via _KNOWN_ORGS."""
        text = 'Instagram said the feature was not designed for that use case.'
        sources = extract_sources(text)
        org_sources = [s for s in sources if s.source_type == "organizational"]
        assert len(org_sources) >= 1
        assert any("Instagram" in s.name for s in org_sources)

    def test_reuters_reported_as_org_source(self):
        """'Reuters reported' — single-word org via expanded _KNOWN_ORGS."""
        text = "Meta lobbied for legal immunity, Reuters reported."
        sources = extract_sources(text)
        org_sources = [s for s in sources if s.source_type == "organizational"]
        assert any("Reuters" in s.name for s in org_sources)


# ---- Framing device tests ----

class TestNewFramingDevices:
    """Tests for analogy_metaphor and taxonomy_framing devices."""

    def test_taxonomy_framing_broken_buried_missing(self):
        text = 'Features were classified as "broken, buried, or missing."'
        frames = detect_framing_devices(text)
        types = {f.device_type for f in frames}
        assert "taxonomy_framing" in types

    def test_taxonomy_framing_failed_or_missing(self):
        text = "The tools were either failed or missing entirely."
        frames = detect_framing_devices(text)
        types = {f.device_type for f in frames}
        assert "taxonomy_framing" in types

    def test_analogy_metaphor_like_crash_testing(self):
        text = "The study was like crash-testing safety features on a car."
        frames = detect_framing_devices(text)
        types = {f.device_type for f in frames}
        assert "analogy_metaphor" in types

    def test_analogy_metaphor_akin_to(self):
        text = "The methodology was akin to a product safety audit."
        frames = detect_framing_devices(text)
        types = {f.device_type for f in frames}
        assert "analogy_metaphor" in types


# ---- Agency attribution dampening tests ----

class TestAgencyDampening:
    """Tests for sparse-data dampening in agency attribution."""

    def test_single_active_neg_dampened(self):
        """Single active-negative hit should be dampened, not -1.0."""
        sent = analyze_composite("The company is requiring employees to relocate.", "")
        # Should be negative but not -1.0 (dampened because total < 3)
        assert sent.agency_attribution < 0
        assert sent.agency_attribution > -1.0

    def test_multiple_hits_not_dampened(self):
        """3+ hits should not be dampened."""
        sent = analyze_composite(
            "They announced the launch and unveiled a new product. "
            "The team accelerated the timeline and delivered results.",
            "",
        )
        # With 4+ active hits, score should be 1.0 (all positive, no dampening)
        assert sent.agency_attribution > 0.5

    def test_zero_hits_returns_zero(self):
        """No agency hits should return 0.0."""
        sent = analyze_composite("The weather was nice today.", "")
        assert sent.agency_attribution == 0.0
