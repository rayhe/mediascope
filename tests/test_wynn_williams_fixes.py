"""Tests for fixes identified during Wynn-Williams lawsuit article deep dive (2026-06-25).

Covers:
- Source extraction: day name and book title false positives
- Litigation framing: complaint, suing, arbitration patterns
- Power asymmetry: adjective-modified violation/breach
- Entity detection: Joel Kaplan, Sheryl Sandberg, SEC, DOJ
"""
import pytest
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.entities import detect_entities
from mediascope.analyze.sources import extract_sources


class TestSourceExtractionFalsePositives:
    """Ensure day names and book titles don't get extracted as sources."""

    def test_thursday_not_extracted_as_source(self):
        text = "A complaint filed on Thursday argues that the ruling was unlawful."
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Thursday" not in names

    def test_monday_not_extracted(self):
        text = "On Monday confirmed that the program was still running."
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Monday" not in names

    def test_careless_people_not_extracted(self):
        text = 'Her memoir, Careless People, alleges a range of wrongdoing.'
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Careless People" not in names

    def test_january_not_extracted(self):
        text = "In January reported that the changes would take effect."
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "January" not in names


class TestLitigationFramingPatterns:
    """Test newly added litigation_framing patterns."""

    def test_filed_complaint(self):
        text = "She filed a complaint in federal court."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "litigation_framing" in types

    def test_is_suing(self):
        text = "The whistleblower is suing Meta over its efforts to silence her."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "litigation_framing" in types

    def test_sues_entity(self):
        text = "Sarah Wynn-Williams sues Meta."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "litigation_framing" in types

    def test_arbitration_ruling(self):
        text = "An arbitration ruling prevented her from speaking."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "litigation_framing" in types

    def test_severance_agreement(self):
        text = "She signed a severance agreement that included a non-disparagement clause."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "litigation_framing" in types

    def test_arbitration_clause(self):
        text = "The mandatory arbitration clause was added to the contract."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "litigation_framing" in types

    def test_filed_suit(self):
        text = "The group filed suit against the corporation."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "litigation_framing" in types


class TestPowerAsymmetryAdjective:
    """Test power_asymmetry with adjective-modified violation/breach."""

    def test_each_purported_violation(self):
        text = "penalties of $50,000 for each purported violation of the gag order"
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "power_asymmetry" in types

    def test_each_alleged_breach(self):
        text = "fines of $100,000 for each alleged breach of the agreement"
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "power_asymmetry" in types

    def test_each_violation_still_works(self):
        text = "penalty of $25,000 per violation of the order"
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "power_asymmetry" in types


class TestEntityDetectionExecutives:
    """Test that newly-added Meta executives and government agencies are detected."""

    def test_joel_kaplan_detected(self):
        text = "Joel Kaplan, Meta's president of global affairs, was cleared."
        entities = detect_entities(text)
        kaplan = [e for e in entities if "Kaplan" in e.entity]
        assert len(kaplan) > 0
        assert kaplan[0].cluster == "Meta"

    def test_sheryl_sandberg_detected(self):
        text = "Sheryl Sandberg, Meta's former chief operating officer, declined."
        entities = detect_entities(text)
        sandberg = [e for e in entities if "Sandberg" in e.entity]
        assert len(sandberg) > 0
        assert sandberg[0].cluster == "Meta"

    def test_sec_detected(self):
        text = "She filed a complaint with the Securities and Exchange Commission."
        entities = detect_entities(text)
        sec = [e for e in entities if "Securities" in e.entity or e.entity == "SEC"]
        assert len(sec) > 0
        assert sec[0].cluster == "US Government"

    def test_doj_detected(self):
        text = "She also filed with the Justice Department."
        entities = detect_entities(text)
        doj = [e for e in entities if "Justice" in e.entity]
        assert len(doj) > 0
        assert doj[0].cluster == "US Government"
