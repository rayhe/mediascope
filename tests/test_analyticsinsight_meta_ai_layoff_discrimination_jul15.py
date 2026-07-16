"""Tests for Analytics Insight Meta AI Layoff Discrimination article (Jul 15, 2026).

Article: "Did Meta Use AI to Decide on Layoffs? Company Responds"

Key bugs fixed in this iteration:
1. Source name extraction: group expert names included trailing attribution
   verb phrases ("Legal analysts noted that" → "Legal analysts").
2. Source deduplication: truncated names ("Legal") survived alongside the
   full group expert name ("Legal analysts").
3. Source stance: documentary complaint/lawsuit sources scored neutral
   instead of adversarial toward the defendant.
4. Hypocrisy frame false positive: "Set a Precedent" section heading in
   a legal-precedent article triggered hypocrisy_frame.
"""

import pathlib

import pytest

from mediascope.analyze.sources import extract_sources, analyze_source_stance
from mediascope.analyze.framing import detect_framing_devices

_ARTICLE_PATH = (
    pathlib.Path(__file__).resolve().parent.parent
    / "examples"
    / "sample_output"
    / "analyticsinsight_meta_ai_layoff_discrimination_2026_07_15_article.txt"
)

ARTICLE = _ARTICLE_PATH.read_text()


# --------------------------------------------------------------------------- #
# Source extraction
# --------------------------------------------------------------------------- #


class TestSourceExtraction:

    def test_legal_analysts_name_clean(self):
        """Group expert name should NOT include trailing verb phrase."""
        sources = extract_sources(ARTICLE)
        group_experts = [s for s in sources if s.source_type == "group_expert"]
        assert group_experts, "Expected at least one group_expert source"
        for ge in group_experts:
            # Name must not contain trailing attribution verbs
            assert "noted that" not in ge.name.lower(), (
                f"Group expert name includes verb phrase: {ge.name!r}"
            )
            assert "said that" not in ge.name.lower()
            assert "argued that" not in ge.name.lower()

    def test_legal_analysts_extracted(self):
        """'Legal analysts' should be extracted as a group_expert source."""
        sources = extract_sources(ARTICLE)
        legal_analysts = [
            s for s in sources
            if "legal analysts" in s.name.lower()
            and s.source_type == "group_expert"
        ]
        assert len(legal_analysts) == 1, (
            f"Expected exactly 1 'Legal analysts' group_expert, got: "
            f"{[s.name for s in legal_analysts]}"
        )

    def test_no_truncated_duplicate_legal(self):
        """Truncated 'Legal' should not survive alongside 'Legal analysts'."""
        sources = extract_sources(ARTICLE)
        names_lower = [s.name.lower().strip() for s in sources]
        if "legal analysts" in names_lower:
            assert "legal" not in names_lower, (
                "Truncated 'Legal' survived alongside 'Legal analysts'"
            )

    def test_documentary_complaint_sources(self):
        """Complaint/lawsuit documentary sources should be extracted."""
        sources = extract_sources(ARTICLE)
        docs = [s for s in sources if s.source_type == "documentary"]
        assert len(docs) >= 2, (
            f"Expected >=2 documentary sources, got {len(docs)}"
        )

    def test_source_count(self):
        """Should extract a reasonable number of sources."""
        sources = extract_sources(ARTICLE)
        assert 3 <= len(sources) <= 8


# --------------------------------------------------------------------------- #
# Source stance
# --------------------------------------------------------------------------- #


class TestSourceStance:

    def test_complaint_sources_adversarial(self):
        """Documentary complaint sources should be adversarial toward Meta."""
        sources = extract_sources(ARTICLE)
        stance = analyze_source_stance(sources, target_entity="Meta",
                                       full_text=ARTICLE)
        assert stance["adversarial_count"] >= 1, (
            f"Expected >=1 adversarial source (complaint docs), got: "
            f"{stance}"
        )

    def test_adversarial_sources_include_complaint(self):
        """At least one adversarial source should be a complaint/filing."""
        sources = extract_sources(ARTICLE)
        stance = analyze_source_stance(sources, target_entity="Meta",
                                       full_text=ARTICLE)
        adversarial_names = [n.lower() for n in stance["adversarial_sources"]]
        assert any(
            "complaint" in name or "filing" in name or "lawsuit" in name
            for name in adversarial_names
        ), f"No complaint source in adversarial list: {adversarial_names}"


# --------------------------------------------------------------------------- #
# Framing devices
# --------------------------------------------------------------------------- #


class TestFramingDevices:

    def test_no_hypocrisy_frame(self):
        """Legal-precedent article should NOT trigger hypocrisy_frame."""
        devices = detect_framing_devices(ARTICLE)
        hypocrisy = [d for d in devices if d.device_type == "hypocrisy_frame"]
        assert len(hypocrisy) == 0, (
            f"hypocrisy_frame should be suppressed in legal context, got: "
            f"{[d.evidence_text[:60] for d in hypocrisy]}"
        )

    def test_precedent_framing_detected(self):
        """Should detect precedent_framing ('first of its kind', etc.)."""
        devices = detect_framing_devices(ARTICLE)
        precedent = [d for d in devices if d.device_type == "precedent_framing"]
        assert len(precedent) >= 1

    def test_litigation_framing_detected(self):
        """Should detect litigation_framing ('filed suit')."""
        devices = detect_framing_devices(ARTICLE)
        litigation = [d for d in devices if d.device_type == "litigation_framing"]
        assert len(litigation) >= 1

    def test_loaded_language_detected(self):
        """Should detect loaded_language ('quietly')."""
        devices = detect_framing_devices(ARTICLE)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        assert len(loaded) >= 1

    def test_total_device_count(self):
        """Total device count should be 6 (no hypocrisy false positive)."""
        devices = detect_framing_devices(ARTICLE)
        assert len(devices) == 6, (
            f"Expected 6 devices, got {len(devices)}: "
            f"{[d.device_type for d in devices]}"
        )
