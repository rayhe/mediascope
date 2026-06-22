"""Tests for the careers module — tracker, migrations, and influence scoring."""

import json
from datetime import date
from pathlib import Path

import pytest
import numpy as np

from datetime import date, timedelta

from mediascope.careers.models import (
    BiasDecomposition,
    CareerEvent,
    DifferenceInDifferencesResult,
    EditorialLeadershipChange,
    JournalistProfile,
    MigrationEvent,
)
from mediascope.careers.tracker import CareerTracker
from mediascope.careers.migrations import MigrationAnalyzer, _window_scores, _portable_bias
from mediascope.careers.influence import InfluenceScorer


# ---------------------------------------------------------------------------
# Model tests
# ---------------------------------------------------------------------------

class TestCareerEvent:
    def test_valid_creation(self):
        ev = CareerEvent(
            journalist_name="Test Writer",
            event_type="hired",
            publication_slug="wired",
            role="staff_writer",
            date_start=date(2020, 1, 1),
        )
        assert ev.journalist_name == "Test Writer"
        assert ev.event_type == "hired"

    def test_invalid_event_type(self):
        with pytest.raises(ValueError, match="Invalid event_type"):
            CareerEvent(
                journalist_name="Test",
                event_type="fired",  # not valid
                publication_slug="wired",
                role="staff_writer",
                date_start=date(2020, 1, 1),
            )

    def test_to_dict(self):
        ev = CareerEvent(
            journalist_name="Test",
            event_type="hired",
            publication_slug="wired",
            role="staff_writer",
            date_start=date(2020, 1, 15),
            date_end=date(2022, 6, 30),
        )
        d = ev.to_dict()
        assert d["date_start"] == "2020-01-15"
        assert d["date_end"] == "2022-06-30"


class TestMigrationEvent:
    def test_lateral_move(self):
        m = MigrationEvent(
            journalist_name="Test",
            from_publication="pub_a",
            to_publication="pub_b",
            departure_date=date(2022, 6, 1),
            arrival_date=date(2022, 7, 1),
            from_role="staff_writer",
            to_role="senior_writer",
        )
        assert m.is_lateral is True
        assert m.is_promotion is False

    def test_promotion(self):
        m = MigrationEvent(
            journalist_name="Test",
            from_publication="pub_a",
            to_publication="pub_b",
            departure_date=date(2022, 6, 1),
            arrival_date=date(2022, 7, 1),
            from_role="staff_writer",
            to_role="eic",
        )
        assert m.is_promotion is True
        assert m.is_lateral is False


class TestJournalistProfile:
    def test_properties(self):
        events = [
            CareerEvent("J", "hired", "pub_a", "staff_writer", date(2018, 1, 1), date(2020, 6, 1)),
            CareerEvent("J", "hired", "pub_b", "senior_writer", date(2020, 7, 1)),
        ]
        p = JournalistProfile(name="J", events=events)
        assert p.current_publication == "pub_b"
        assert p.current_role == "senior_writer"
        assert p.n_publications == 2
        assert p.publications_worked_at == ["pub_a", "pub_b"]
        assert p.career_span_years > 0

    def test_tenure_at(self):
        events = [
            CareerEvent("J", "hired", "wired", "staff_writer", date(2018, 1, 1), date(2020, 6, 1)),
        ]
        p = JournalistProfile(name="J", events=events)
        tenure = p.tenure_at("wired")
        assert tenure is not None
        assert tenure[0] == date(2018, 1, 1)
        assert tenure[1] == date(2020, 6, 1)


# ---------------------------------------------------------------------------
# Migration analyzer tests
# ---------------------------------------------------------------------------

class TestWindowScores:
    def test_basic_windowing(self):
        articles = [
            {"published_date": date(2022, 3, 15), "overall_tone": -0.3},
            {"published_date": date(2022, 5, 1), "overall_tone": -0.5},
            {"published_date": date(2022, 7, 1), "overall_tone": -0.1},
            {"published_date": date(2022, 9, 15), "overall_tone": 0.2},
        ]
        pivot = date(2022, 6, 1)

        pre = _window_scores(articles, pivot, -180, 0)
        post = _window_scores(articles, pivot, 0, 180)

        assert len(pre) == 2  # March and May
        assert len(post) == 2  # July and September

    def test_empty_window(self):
        articles = [
            {"published_date": date(2022, 1, 1), "overall_tone": -0.3},
        ]
        pivot = date(2023, 6, 1)
        scores = _window_scores(articles, pivot, -30, 30)
        assert len(scores) == 0


class TestPortableBias:
    def test_identical_distributions(self):
        """Identical tone distributions → high portability."""
        pre = [-0.3, -0.4, -0.35, -0.28, -0.32]
        post = [-0.31, -0.39, -0.34, -0.29, -0.33]
        score = _portable_bias(pre, post)
        assert score > 0.8

    def test_very_different_distributions(self):
        """Very different distributions → low portability."""
        pre = [-0.8, -0.9, -0.85, -0.75, -0.82]
        post = [0.3, 0.4, 0.35, 0.28, 0.32]
        score = _portable_bias(pre, post)
        assert score < 0.3

    def test_insufficient_data(self):
        """Insufficient data → agnostic default."""
        assert _portable_bias([0.1], [0.2]) == 0.5


class TestMigrationAnalyzer:
    def test_basic_did(self):
        """Test DiD with synthetic data where the effect is clear."""
        np.random.seed(42)

        migration = MigrationEvent(
            journalist_name="Test",
            from_publication="pub_a",
            to_publication="pub_b",
            departure_date=date(2022, 6, 1),
            arrival_date=date(2022, 7, 1),
            from_role="staff_writer",
            to_role="staff_writer",
        )

        # Source pub: tone was negative, becomes neutral after journalist leaves
        src_articles = []
        for i in range(20):
            d = date(2022, 1, 1) + timedelta(days=i * 9)
            tone = -0.4 + np.random.normal(0, 0.05)
            src_articles.append({"published_date": d, "overall_tone": tone, "author": "Other"})
        for i in range(20):
            d = date(2022, 7, 1) + timedelta(days=i * 9)
            tone = -0.1 + np.random.normal(0, 0.05)
            src_articles.append({"published_date": d, "overall_tone": tone, "author": "Other"})

        # Destination pub: neutral, stays neutral
        dst_articles = []
        for i in range(20):
            d = date(2022, 1, 1) + timedelta(days=i * 9)
            tone = -0.05 + np.random.normal(0, 0.05)
            dst_articles.append({"published_date": d, "overall_tone": tone, "author": "Other"})
        for i in range(20):
            d = date(2022, 7, 1) + timedelta(days=i * 9)
            tone = -0.05 + np.random.normal(0, 0.05)
            dst_articles.append({"published_date": d, "overall_tone": tone, "author": "Other"})

        # Journalist articles
        j_articles = []
        for i in range(10):
            d = date(2022, 1, 1) + timedelta(days=i * 15)
            tone = -0.5 + np.random.normal(0, 0.05)
            j_articles.append({"published_date": d, "overall_tone": tone, "author": "Test"})
        for i in range(10):
            d = date(2022, 7, 1) + timedelta(days=i * 15)
            tone = -0.45 + np.random.normal(0, 0.05)
            j_articles.append({"published_date": d, "overall_tone": tone, "author": "Test"})

        analyzer = MigrationAnalyzer(window_days=180)
        result = analyzer.analyze_migration(
            migration=migration,
            source_articles=src_articles,
            dest_articles=dst_articles,
            journalist_articles=j_articles,
        )

        # Source should show positive change (less negative after journalist left)
        assert result.source_raw_change > 0.1
        assert result.n_articles_pre > 0
        assert result.n_articles_post > 0


# ---------------------------------------------------------------------------
# Influence scorer tests
# ---------------------------------------------------------------------------

class TestInfluenceScorer:
    def test_decompose_two_pubs(self):
        """Test decomposition with two publications."""
        scorer = InfluenceScorer(min_articles_per_pub=3)

        articles_by_pub = {
            "pub_a": [
                {"overall_tone": -0.4},
                {"overall_tone": -0.3},
                {"overall_tone": -0.35},
                {"overall_tone": -0.5},
                {"overall_tone": -0.45},
            ],
            "pub_b": [
                {"overall_tone": -0.38},
                {"overall_tone": -0.32},
                {"overall_tone": -0.36},
                {"overall_tone": -0.42},
                {"overall_tone": -0.39},
            ],
        }

        result = scorer.decompose("Test Writer", articles_by_pub)

        assert result.n_publications == 2
        assert result.n_articles == 10
        assert 0 <= result.portable_bias_score <= 1
        assert result.institutional_component >= 0
        assert result.individual_component >= 0
        assert result.confidence > 0

    def test_insufficient_pubs(self):
        """Single pub → insufficient data."""
        scorer = InfluenceScorer()
        articles_by_pub = {
            "pub_a": [{"overall_tone": -0.4}] * 10,
        }
        result = scorer.decompose("Test", articles_by_pub)
        assert result.confidence == 0.0
        assert "Insufficient" in result.methodology_note

    def test_high_portable_bias(self):
        """Journalist with identical tone at both pubs → high portable score."""
        scorer = InfluenceScorer(min_articles_per_pub=3)
        np.random.seed(42)

        articles_by_pub = {
            "pub_a": [{"overall_tone": -0.5 + np.random.normal(0, 0.02)} for _ in range(20)],
            "pub_b": [{"overall_tone": -0.5 + np.random.normal(0, 0.02)} for _ in range(20)],
        }

        result = scorer.decompose(
            "Consistent Writer",
            articles_by_pub,
            pub_baselines={"pub_a": -0.1, "pub_b": 0.1},
        )
        assert result.portable_bias_score > 0.7

    def test_low_portable_bias(self):
        """Journalist who adapts to each pub → low portable score."""
        scorer = InfluenceScorer(min_articles_per_pub=3)
        np.random.seed(42)

        articles_by_pub = {
            "pub_a": [{"overall_tone": -0.8 + np.random.normal(0, 0.02)} for _ in range(20)],
            "pub_b": [{"overall_tone": 0.3 + np.random.normal(0, 0.02)} for _ in range(20)],
        }

        result = scorer.decompose("Adaptive Writer", articles_by_pub)
        assert result.portable_bias_score < 0.4


# ---------------------------------------------------------------------------
# Tracker integration test (requires YAML file)
# ---------------------------------------------------------------------------

class TestCareerTracker:
    def test_load_from_fixture(self, tmp_path):
        """Test loading from a minimal YAML fixture."""
        yaml_content = """
journalists:
  - name: "Test Writer"
    career:
      - publication: "pub_a"
        event_type: "hired"
        role: "staff_writer"
        start: "2018-01"
        end: "2020-06"
        beat: "tech"
      - publication: "pub_b"
        event_type: "hired"
        role: "senior_writer"
        start: "2020-07"
        beat: "AI"
"""
        yaml_path = tmp_path / "journalists.yaml"
        yaml_path.write_text(yaml_content)

        tracker = CareerTracker(profiles_dir=tmp_path)
        tracker.load(journalists_file=yaml_path)

        profile = tracker.get("Test Writer")
        assert profile is not None
        assert profile.name == "Test Writer"
        assert len(profile.events) == 2
        assert len(profile.migrations) == 1
        assert profile.migrations[0].from_publication == "pub_a"
        assert profile.migrations[0].to_publication == "pub_b"

    def test_by_publication(self, tmp_path):
        yaml_content = """
journalists:
  - name: "Writer A"
    career:
      - publication: "wired"
        event_type: "hired"
        role: "staff_writer"
        start: "2020-01"
  - name: "Writer B"
    career:
      - publication: "nytimes"
        event_type: "hired"
        role: "correspondent"
        start: "2019-06"
  - name: "Writer C"
    career:
      - publication: "wired"
        event_type: "hired"
        role: "senior_writer"
        start: "2018-01"
"""
        yaml_path = tmp_path / "journalists.yaml"
        yaml_path.write_text(yaml_content)

        tracker = CareerTracker(profiles_dir=tmp_path)
        tracker.load(journalists_file=yaml_path)

        wired = tracker.by_publication("wired")
        assert len(wired) == 2
        nyt = tracker.by_publication("nytimes")
        assert len(nyt) == 1
