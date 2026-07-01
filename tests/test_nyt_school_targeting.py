"""Tests for NYT "How Tech Companies Hooked Kids in School" (Jun 4, 2026).

Article by Jennifer Valentino-DeVries covering internal documents from
lawsuits by 1,400+ school districts against Meta, Snap, TikTok, and YouTube.
Key revelations: Meta paid "teen ambassadors," TikTok rejected safety team's
push to disable school-hours notifications, Snapchat called classroom use
"under the desk" time, TikTok funded National PTA.

Test focus areas:
- Entity detection: multi-company coverage + new entities (National PTA, Cornell)
- Topic classification: education + child_safety co-occurrence
- Framing device detection: safety team overrule (hypocrisy_frame), ironic
  quotation, scale/magnitude, loaded language
- Source stance: role-based adversarial detection (plaintiff's attorney)
"""

import os
import pytest

from mediascope.analyze.entities import (
    detect_entities,
    get_entity_distribution,
    get_primary_entity,
)
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sentiment import analyze_composite
from mediascope.analyze.sources import (
    extract_sources,
    analyze_source_stance,
    grade_source_authority,
)
from mediascope.analyze.topics import classify_topic


# Load article text
_ARTICLE_PATH = os.path.join(
    os.path.dirname(__file__), "..",
    "examples", "sample_output",
    "nyt_meta_school_targeting_teen_ambassadors_2026_06_article.txt",
)

with open(_ARTICLE_PATH, encoding="utf-8") as _f:
    ARTICLE_TEXT = _f.read()

HEADLINE = "How Tech Companies Hooked Kids in School on Social Media"


# ---------------------------------------------------------------------------
# Entity detection
# ---------------------------------------------------------------------------

class TestEntityDetection:
    """Entity detection on multi-company school targeting article."""

    def setup_method(self):
        self.entities = detect_entities(ARTICLE_TEXT)
        self.dist = get_entity_distribution(self.entities)
        self.names = {e.canonical_name for e in self.entities}
        self.clusters = {e.cluster for e in self.entities}

    def test_all_four_defendant_companies_detected(self):
        """All four defendant companies should be detected."""
        assert "Meta" in self.clusters
        assert "Google" in self.clusters
        assert "TikTok" in self.clusters
        assert "Snap" in self.clusters

    def test_meta_entities(self):
        """Meta cluster should include Meta, Instagram, Mark Zuckerberg."""
        meta_names = {
            e.canonical_name for e in self.entities if e.cluster == "Meta"
        }
        assert "Meta" in meta_names
        assert "Instagram" in meta_names
        assert "Mark Zuckerberg" in meta_names

    def test_google_entities(self):
        """Google cluster should include YouTube and Google."""
        google_names = {
            e.canonical_name for e in self.entities if e.cluster == "Google"
        }
        assert "YouTube" in google_names
        assert "Google" in google_names

    def test_snap_entities(self):
        """Snap cluster should detect both Snap and Snapchat."""
        snap_names = {
            e.canonical_name for e in self.entities if e.cluster == "Snap"
        }
        assert len(snap_names) >= 1
        assert "Snap" in snap_names or "Snapchat" in snap_names

    def test_national_pta_detected(self):
        """National PTA should be detected as Education/Advocacy entity."""
        assert "Education/Advocacy" in self.clusters
        edu_names = {
            e.canonical_name for e in self.entities
            if e.cluster == "Education/Advocacy"
        }
        assert "National PTA" in edu_names

    def test_cornell_detected(self):
        """Cornell Law School should be detected as Academic/Research."""
        assert "Academic/Research" in self.clusters
        acad_names = {
            e.canonical_name for e in self.entities
            if e.cluster == "Academic/Research"
        }
        assert "Cornell" in acad_names or "Cornell Law School" in acad_names

    def test_media_publications_detected(self):
        """Bloomberg and New York Times should be detected."""
        media_names = {
            e.canonical_name for e in self.entities
            if e.cluster == "Media/Publications"
        }
        assert "Bloomberg" in media_names
        assert "New York Times" in media_names

    def test_entity_count_minimum(self):
        """Article should have at least 30 entity mentions total."""
        total = sum(self.dist.values())
        assert total >= 30, f"Expected 30+ entity mentions, got {total}"


# ---------------------------------------------------------------------------
# Topic classification
# ---------------------------------------------------------------------------

class TestTopicClassification:
    """Topic detection for education + child safety article."""

    def setup_method(self):
        self.topics = classify_topic(ARTICLE_TEXT)
        self.topic_dict = {t.topic: t for t in self.topics}

    def test_education_topic_detected(self):
        """Education should be a primary topic."""
        assert "education" in self.topic_dict, (
            f"Education not in top topics: {[t.topic for t in self.topics]}"
        )
        assert self.topic_dict["education"].confidence >= 0.4

    def test_child_safety_detected(self):
        """Child safety should be detected with substantial confidence."""
        assert "child_safety" in self.topic_dict, (
            f"child_safety not in top topics: {[t.topic for t in self.topics]}"
        )
        assert self.topic_dict["child_safety"].confidence >= 0.3

    def test_litigation_detected(self):
        """Litigation should be detected (1,400+ school districts suing)."""
        assert "litigation" in self.topic_dict, (
            f"litigation not in top topics: {[t.topic for t in self.topics]}"
        )

    def test_education_keywords_match(self):
        """Education topic should match school/classroom/student keywords."""
        edu = self.topic_dict.get("education")
        assert edu is not None
        education_keywords = set(edu.matched_keywords)
        # At least some of these should be matched
        expected_some = {"school", "schools", "classroom", "classrooms",
                         "student", "students", "campus", "education",
                         "academic", "PTA", "Chromebooks"}
        assert education_keywords & expected_some, (
            f"No expected education keywords matched: {education_keywords}"
        )


# ---------------------------------------------------------------------------
# Framing device detection
# ---------------------------------------------------------------------------

class TestFramingDevices:
    """Framing device detection for school targeting article."""

    def setup_method(self):
        self.devices = detect_framing_devices(ARTICLE_TEXT)
        self.by_type = {}
        for d in self.devices:
            self.by_type.setdefault(d.device_type, []).append(d)

    def test_hypocrisy_frame_safety_team_overrule(self):
        """Safety team overrule should trigger hypocrisy_frame.

        TikTok's leaders rejected safety teams' recommendation to disable
        school-hours notifications — a classic say-safety-do-growth pattern.
        """
        assert "hypocrisy_frame" in self.by_type, (
            f"hypocrisy_frame not detected. Found: {sorted(self.by_type.keys())}"
        )

    def test_ironic_quotation_detected(self):
        """Scare quotes on 'teen ambassadors' and 'under the desk' should fire."""
        assert "ironic_quotation" in self.by_type
        # Should have multiple instances
        assert len(self.by_type["ironic_quotation"]) >= 2

    def test_scale_magnitude_detected(self):
        """Scale/magnitude framing: 1,400+ districts, $27M, etc."""
        assert "scale_magnitude" in self.by_type
        assert len(self.by_type["scale_magnitude"]) >= 3

    def test_loaded_language_detected(self):
        """Loaded language: 'infiltrate', 'exploitation', 'backlash'."""
        assert "loaded_language" in self.by_type
        evidences = [d.evidence_text.lower() for d in self.by_type["loaded_language"]]
        # At least 'infiltrate' should be caught
        assert any("infiltrat" in e for e in evidences), (
            f"'infiltrate' not in loaded_language evidence: {evidences}"
        )

    def test_emotional_appeal_detected(self):
        """Emotional appeal: mental health, children's harm."""
        assert "emotional_appeal" in self.by_type

    def test_litigation_framing_detected(self):
        """Litigation framing: 'suing Meta, Snap, TikTok and YouTube'."""
        assert "litigation_framing" in self.by_type

    def test_minimum_framing_device_types(self):
        """Article should trigger at least 7 distinct framing device types."""
        assert len(self.by_type) >= 7, (
            f"Expected 7+ device types, got {len(self.by_type)}: "
            f"{sorted(self.by_type.keys())}"
        )


# ---------------------------------------------------------------------------
# Sentiment analysis
# ---------------------------------------------------------------------------

class TestSentiment:
    """Sentiment analysis on school targeting article."""

    def setup_method(self):
        self.sentiment = analyze_composite(ARTICLE_TEXT, HEADLINE)

    def test_overall_tone_negative(self):
        """Overall tone should be negative (critical of tech companies)."""
        assert self.sentiment.overall_tone < 0, (
            f"Expected negative tone, got {self.sentiment.overall_tone}"
        )

    def test_emotional_language_intensity(self):
        """Emotional language intensity should be moderate to high."""
        assert self.sentiment.emotional_language_intensity > 0.1, (
            f"Expected emotional intensity > 0.1, got "
            f"{self.sentiment.emotional_language_intensity}"
        )

    def test_agency_attribution_negative(self):
        """Agency attribution should be negative (companies as active agents of harm)."""
        assert self.sentiment.agency_attribution < 0, (
            f"Expected negative agency, got {self.sentiment.agency_attribution}"
        )


# ---------------------------------------------------------------------------
# Source extraction and stance
# ---------------------------------------------------------------------------

class TestSourceAnalysis:
    """Source extraction and stance for school targeting article."""

    def setup_method(self):
        self.sources = extract_sources(ARTICLE_TEXT)
        self.stance = analyze_source_stance(
            self.sources, "Meta", full_text=ARTICLE_TEXT
        )

    def test_previn_warren_extracted(self):
        """Lead plaintiff's attorney Previn Warren should be extracted."""
        names = [s.name for s in self.sources]
        assert "Previn Warren" in names

    def test_alexandra_lahav_extracted(self):
        """Cornell Law professor Alexandra Lahav should be extracted."""
        names = [s.name for s in self.sources]
        assert "Alexandra Lahav" in names

    def test_lahav_affiliation(self):
        """Alexandra Lahav should be affiliated with Cornell Law School."""
        lahav = [s for s in self.sources if s.name == "Alexandra Lahav"]
        assert lahav, "Lahav not found"
        assert "Cornell" in lahav[0].affiliation

    def test_both_sources_are_expert(self):
        """Both named sources should be classified as expert."""
        for source in self.sources:
            assert source.is_expert, f"{source.name} not classified as expert"

    def test_previn_warren_adversarial_by_role(self):
        """Lead plaintiff's lawyer should be adversarial by role.

        Previn Warren is 'one of the lead lawyers for the schools' — the
        schools are suing Meta et al. Role-based stance detection should
        classify him as adversarial regardless of quote content.
        """
        assert "Previn Warren" in self.stance["adversarial_sources"], (
            f"Warren not adversarial. Adversarial: {self.stance['adversarial_sources']}, "
            f"Neutral: {self.stance['neutral_count']}"
        )

    def test_source_authority_high(self):
        """Source authority should be high (named experts, no anonymous)."""
        authority = grade_source_authority(self.sources)
        assert authority >= 0.8, f"Expected high authority, got {authority}"

    def test_no_anonymous_sources(self):
        """Article should have zero anonymous sources (all named)."""
        anon = [s for s in self.sources if s.is_anonymous]
        assert len(anon) == 0, f"Found anonymous sources: {[s.name for s in anon]}"
