"""Tests for Gizmodo Meta AI Layoff Discrimination article analysis (Jul 15, 2026).

Validates three fixes from this iteration:
1. Entity: "Metamate" added to Meta cluster
2. Framing: "away from" preposition in humanization timing pattern
3. Framing: "selected" termination verb in humanization pregnancy pattern

Article: Gizmodo "Meta Sued For Allegedly Using Discriminatory AI In Layoff
Decisions" (July 15, 2026).
"""

import pytest

from mediascope.analyze.entities import detect_entities
from mediascope.analyze.framing import detect_framing_devices


# ── Entity: Metamate ─────────────────────────────────────────────────────

class TestMetamateEntity:
    """Metamate is Meta's internal LLM assistant, cited in the AI layoff
    discrimination lawsuit (Jul 2026). It should be detected as a Meta entity."""

    def test_metamate_detected_as_meta_entity(self):
        text = (
            "These systems allegedly included an internal large-language "
            "model assistant called Metamate, a 'second brain' that was "
            "trained on employee communications and documents."
        )
        entities = detect_entities(text)
        meta_entities = [e for e in entities if e.cluster == "Meta"]
        entity_names = {e.entity for e in meta_entities}
        assert "Metamate" in entity_names

    def test_metamate_in_meta_cluster_not_standalone(self):
        text = "Metamate was used to score employee productivity."
        entities = detect_entities(text)
        meta_entities = [e for e in entities if e.cluster == "Meta"]
        assert len(meta_entities) >= 1
        # Must not appear in a different cluster
        non_meta = [e for e in entities if e.entity == "Metamate" and e.cluster != "Meta"]
        assert len(non_meta) == 0


# ── Framing: humanization "away from" ────────────────────────────────────

class TestHumanizationAwayFrom:
    """The phrase 'X days away from giving birth' uses 'away from' rather
    than 'before' — must be caught by the humanization timing pattern."""

    def test_days_away_from_giving_birth(self):
        text = (
            "According to the lawsuit, a scientist that was just two days "
            "away from giving birth was selected for layoff."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "humanization" in types

    def test_weeks_away_from_delivery(self):
        text = (
            "She was just three weeks away from her delivery date when "
            "the notification arrived."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "humanization" in types

    def test_hours_away_from_surgery(self):
        text = (
            "He received the termination notice hours away from his "
            "surgery, scheduled for the following morning."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "humanization" in types


# ── Framing: humanization "selected" verb ────────────────────────────────

class TestHumanizationSelectedVerb:
    """'Selected by the system' / 'selected for layoff' is a termination
    synonym used in AI-assisted layoff coverage. Must trigger humanization
    when near pregnancy/disability context."""

    def test_pregnancy_leave_selected(self):
        text = (
            "Another employee, a manager, was on approved pregnancy-related "
            "disability leave when she became the only person on her team "
            "that was selected by the system."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "humanization" in types

    def test_maternity_leave_selected_for_layoff(self):
        text = (
            "Multiple employees that were on maternity leave at the time "
            "were selected for inclusion on the termination list."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "humanization" in types

    def test_selected_without_pregnancy_context_not_humanization(self):
        """'selected' alone without pregnancy/disability context should
        NOT trigger humanization."""
        text = (
            "Employees were selected based on rolling 12-month performance "
            "ratings and productivity scores."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "humanization" not in types


# ── Full article integration ─────────────────────────────────────────────

class TestGizmodoLayoffFullArticle:
    """Integration test: run the full Gizmodo Jul 15 article through
    both entity detection and framing detection."""

    @pytest.fixture
    def article_text(self):
        import os
        path = os.path.join(
            os.path.dirname(__file__), "..",
            "examples", "sample_output",
            "gizmodo_meta_ai_layoff_discrimination_2026_07_15_article.txt"
        )
        with open(path) as f:
            return f.read()

    def test_metamate_in_full_article(self, article_text):
        entities = detect_entities(article_text)
        entity_names = {e.entity for e in entities if e.cluster == "Meta"}
        assert "Metamate" in entity_names

    def test_humanization_in_full_article(self, article_text):
        devices = detect_framing_devices(article_text)
        humanization = [d for d in devices if d.device_type == "humanization"]
        assert len(humanization) >= 2, (
            f"Expected ≥2 humanization devices, got {len(humanization)}: "
            f"{[d.evidence_text[:60] for d in humanization]}"
        )

    def test_framing_count_at_least_9(self, article_text):
        devices = detect_framing_devices(article_text)
        assert len(devices) >= 9, (
            f"Expected ≥9 framing devices, got {len(devices)}: "
            f"{[d.device_type for d in devices]}"
        )

    def test_surveillance_enumeration_detected(self, article_text):
        devices = detect_framing_devices(article_text)
        types = {d.device_type for d in devices}
        assert "surveillance_enumeration" in types
