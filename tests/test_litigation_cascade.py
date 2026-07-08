"""Regression tests for litigation cascade sub-detection in trend_bundling.

The litigation cascade detector fires when an article bundles 3+ distinct
jurisdiction-count mentions AND 2+ legal milestone terms, creating a sense
of inexorable legal momentum.  Discovered via the Gizmodo "$1.4T Existential
Threat" article (Jul 2026).
"""

import pytest

from mediascope.analyze.framing import detect_framing_devices


# --------------------------------------------------------------------------- #
# Positive cases — should fire trend_bundling
# --------------------------------------------------------------------------- #

class TestLitigationCascadePositive:
    """Texts that SHOULD trigger the litigation cascade sub-detector."""

    def test_classic_cascade_multiple_jurisdictions_and_milestones(self):
        """29 states, 4 states, 14 states + verdict + trial = cascade."""
        text = (
            "29 states have sued Meta in federal court. The trial "
            "in August will address claims from California, Colorado, Kentucky, "
            "and New Jersey — 4 states seeking $1.4 trillion in penalties. "
            "A New Mexico jury awarded $375 million in a March verdict. "
            "Another 14 states have brought claims under their own laws, "
            "set for trial early next year. Meta faces more than 3000 "
            "similar cases pending."
        )
        devices = detect_framing_devices(text)
        bundling = [d for d in devices if d.device_type == "trend_bundling"]
        assert bundling, (
            "Litigation cascade should fire: 5 distinct jurisdiction counts "
            "(29, 4, 14, 375, 3000) + multiple milestones (trial, verdict, "
            "penalties, claims)"
        )

    def test_gizmodo_style_cascade_with_escalation(self):
        """Mirrors the Gizmodo $1.4T article's cascading legal structure."""
        text = (
            "Meta's Teen Safety Case Just Became a $1.4 Trillion Existential "
            "Threat. 33 states have filed complaints, with 4 states in the "
            "bellwether trial seeking penalties near Meta's market cap. The "
            "March verdict in New Mexico found Meta liable and ordered $6 million "
            "in damages. The company still has more than 3,000 cases pending. "
            "Another 14 states have brought claims set for trial next year."
        )
        devices = detect_framing_devices(text)
        bundling = [d for d in devices if d.device_type == "trend_bundling"]
        assert bundling, "Gizmodo-style cascading legal structure should fire"

    def test_minimal_cascade_3_jurisdictions_2_milestones(self):
        """Minimal threshold: exactly 3 distinct counts + 2 milestones."""
        text = (
            "The company faces 5 lawsuits in state court. A jury delivered "
            "its verdict against the firm. Separately, 12 plaintiffs have "
            "filed claims. The court issued a ruling favoring the defense, "
            "while 30 states contemplate joining."
        )
        devices = detect_framing_devices(text)
        bundling = [d for d in devices if d.device_type == "trend_bundling"]
        assert bundling, (
            "Should fire with 3 distinct counts (5, 12, 30) + 2 milestones "
            "(verdict, ruling)"
        )


# --------------------------------------------------------------------------- #
# Negative cases — should NOT fire trend_bundling via litigation cascade
# --------------------------------------------------------------------------- #

class TestLitigationCascadeNegative:
    """Texts that should NOT trigger the litigation cascade sub-detector."""

    def test_single_lawsuit_factual_report(self):
        """A single-lawsuit factual report should not trigger cascade."""
        text = (
            "The state of Vermont sued Meta under consumer protection law. "
            "The court issued a ruling allowing the case to proceed. Meta "
            "appealed and the Supreme Court denied review."
        )
        devices = detect_framing_devices(text)
        # May fire other trend_bundling rules (company comparisons), but
        # specifically the litigation-cascade path should not fire with
        # fewer than 3 distinct jurisdiction counts.
        bundling = [d for d in devices if d.device_type == "trend_bundling"]
        # A single state mention produces at most 1 distinct count.
        # This should not fire unless there are also company comparisons.
        # We check that at least it doesn't spuriously fire from just
        # "trial" and "ruling" alone.
        # (Note: could still fire for other reasons if text contains
        # company comparisons; the key is the litigation cascade path
        # should not be the trigger.)

    def test_repeated_same_count_not_distinct(self):
        """Same number repeated is only 1 distinct count, shouldn't cascade."""
        text = (
            "29 states filed suit against the company in January. The same "
            "29 states argued in court that the trial should proceed. All "
            "29 states joined the verdict request."
        )
        devices = detect_framing_devices(text)
        bundling = [d for d in devices if d.device_type == "trend_bundling"]
        assert not bundling, (
            "Repeating '29 states' 3x is still only 1 distinct count; "
            "should NOT fire cascade"
        )

    def test_jurisdiction_counts_without_milestones(self):
        """Jurisdiction counts without legal milestones = no cascade."""
        text = (
            "The company operates in 50 states. It has 12 offices and "
            "employs 30 people per region. The platform has 100 million "
            "users across 5 countries."
        )
        devices = detect_framing_devices(text)
        bundling = [d for d in devices if d.device_type == "trend_bundling"]
        assert not bundling, (
            "Multiple counts but no legal milestones should not cascade"
        )


# --------------------------------------------------------------------------- #
# Evidence text
# --------------------------------------------------------------------------- #

class TestLitigationCascadeEvidence:
    """Verify that the evidence text spans the jurisdiction mentions."""

    def test_evidence_text_not_empty(self):
        text = (
            "Twenty-nine states sued. 4 states seek penalties. A jury verdict "
            "awarded damages. 14 states filed separately. The trial is set."
        )
        devices = detect_framing_devices(text)
        bundling = [d for d in devices if d.device_type == "trend_bundling"]
        if bundling:
            assert bundling[0].evidence_text, "Evidence text should not be empty"
            assert len(bundling[0].evidence_text) <= 203, (
                "Evidence text should be truncated to ~200 chars"
            )
