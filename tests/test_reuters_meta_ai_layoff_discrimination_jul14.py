"""Tests for patterns discovered via Reuters Meta AI layoff discrimination
article (Jul 14, 2026).

Covers:
1. Entity resolution: "District of Columbia" should NOT match Columbia University
2. Legal-context loaded_language suppression: "violating", "retaliation" are
   legal vocabulary, not editorial loaded language, when in lawsuit context
3. Legal-context absence_as_evidence suppression: "failed to test" is a
   plaintiff allegation, not journalistic absence-framing
4. Standalone "slashed" as loaded_language verb
"""

import pytest
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.entities import detect_entities


def _has(text: str, device_type: str) -> bool:
    return any(d.device_type == device_type for d in detect_framing_devices(text))


def _evidence(text: str, device_type: str) -> list[str]:
    return [d.evidence_text for d in detect_framing_devices(text) if d.device_type == device_type]


# ── Entity Resolution: District of Columbia ─────────────────────────────


class TestDistrictOfColumbia:
    """'District of Columbia' should NOT resolve to Columbia University."""

    def test_district_of_columbia_not_university(self):
        text = "The plaintiffs come from six states, including California and New York, and the District of Columbia."
        entities = detect_entities(text)
        columbia_entities = [e for e in entities if "columbia" in e.canonical_name.lower()]
        for e in columbia_entities:
            assert e.cluster != "Academic/Research", (
                f"'Columbia' in 'District of Columbia' incorrectly mapped to "
                f"Academic/Research cluster (canonical: {e.canonical_name})"
            )

    def test_british_columbia_not_university(self):
        text = "The court in British Columbia ruled against the company."
        entities = detect_entities(text)
        columbia_entities = [e for e in entities if "columbia" in e.canonical_name.lower()]
        for e in columbia_entities:
            assert e.cluster != "Academic/Research", (
                f"'Columbia' in 'British Columbia' incorrectly mapped to "
                f"Academic/Research cluster"
            )

    def test_columbia_university_still_detected(self):
        """Columbia University (without 'District of' prefix) should still work."""
        text = "A Columbia University professor provided expert testimony."
        entities = detect_entities(text)
        columbia_entities = [e for e in entities if "columbia" in e.entity.lower()]
        assert len(columbia_entities) > 0, "Columbia University should still be detected"
        assert columbia_entities[0].cluster == "Academic/Research"


# ── Legal-Context Loaded Language Suppression ────────────────────────────


class TestLegalContextSuppression:
    """Legal terms of art in lawsuit articles should not trigger loaded_language."""

    def test_violating_in_lawsuit_context(self):
        text = (
            "The plaintiffs are accusing Meta of violating federal and state "
            "laws that ban discrimination. The lawsuit was filed in Oakland."
        )
        evidence = _evidence(text, "loaded_language")
        assert "violating" not in evidence, (
            "'violating' in legal-context lawsuit reporting should be suppressed"
        )

    def test_retaliation_in_lawsuit_context(self):
        text = (
            "The complaint alleges violation of federal laws that ban "
            "discrimination or retaliation against workers with disabilities."
        )
        evidence = _evidence(text, "loaded_language")
        assert "retaliation" not in evidence, (
            "'retaliation' as a legal cause of action should be suppressed in legal context"
        )

    def test_violating_without_legal_context_still_fires(self):
        """'violating' without legal context should still be detected."""
        text = (
            "The company's approach involves violating basic privacy norms "
            "that most people take for granted."
        )
        assert _has(text, "loaded_language"), (
            "'violating' without legal context should still trigger loaded_language"
        )


# ── Legal-Context Absence-as-Evidence Suppression ────────────────────────


class TestAbsenceAsEvidenceLegalSuppression:
    """'failed to' as plaintiff allegation should not trigger absence_as_evidence."""

    def test_meta_failed_to_test_in_lawsuit(self):
        text = (
            "They claim that Meta failed to test its AI systems for bias "
            "in violation of recently adopted California law. The lawsuit "
            "was filed in Oakland federal court."
        )
        assert not _has(text, "absence_as_evidence"), (
            "'Meta failed to test' in lawsuit context is a plaintiff allegation, "
            "not journalistic absence-framing"
        )

    def test_failed_to_without_legal_context_still_fires(self):
        """'failed to' without legal context should still be detected."""
        text = "Meta failed to disclose the full extent of data collection."
        assert _has(text, "absence_as_evidence"), (
            "'Meta failed to disclose' without legal context should still trigger"
        )


# ── Standalone "slashed" as loaded_language ──────────────────────────────


class TestSlashedLoadedLanguage:
    """'slashed' is a violent metaphor for layoffs/cuts."""

    def test_slashed_thousands_of_jobs(self):
        text = "The company slashed thousands of jobs earlier this year."
        assert _has(text, "loaded_language"), (
            "'slashed' should trigger loaded_language as a violent metaphor for layoffs"
        )

    def test_slashed_standalone(self):
        text = "The CEO slashed the budget by 40 percent."
        assert _has(text, "loaded_language"), (
            "'slashed' should trigger loaded_language even without job/layoff context"
        )
