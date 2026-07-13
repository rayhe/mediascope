"""Tests for the Fox Business Meta Louisiana data center article analysis
(Jul 13, 2026).

Covers:
- recovery_narrative: "transforming our schools" (broadened pattern, possessive + institution noun)
- loaded_language: "life-altering" (positive magnitude idiom)
- scale_magnitude: dollar figures ($50B, $1.6B, $1B, $2B)
- kicker_framing: "Workforce" section label

These tests validate the recovery_narrative pattern broadening from this
iteration. The prior pattern required "transforming the local/rural/regional
economy/community" — too narrow for possessive constructions and non-economy
nouns like "schools" and "district".
"""

import pytest
from mediascope.analyze.framing import detect_framing_devices


class TestRecoveryNarrativeBroadenedPatterns:
    """Tests for the broadened recovery_narrative patterns added for Fox
    Business-style community benefit language."""

    def test_transforming_our_schools(self):
        """'transforming our schools' — possessive + institution noun."""
        text = "It's transforming our schools."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "recovery_narrative" in types

    def test_transforming_our_district(self):
        """'transforming our district' — possessive + institution noun."""
        text = "The investment is transforming our district."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "recovery_narrative" in types

    def test_reshaping_richland_parish(self):
        """'reshaping Richland Parish' — reshape + proper noun."""
        text = "The project is already reshaping Richland Parish."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "recovery_narrative" in types

    def test_transforming_the_town(self):
        """'transforming the town' — article + institution noun."""
        text = "Meta's data center is transforming the town."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "recovery_narrative" in types

    def test_reshaping_the_parish(self):
        """'reshaping the parish' — article + institution noun."""
        text = "The expansion is reshaping the parish."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "recovery_narrative" in types

    def test_transformed_their_schools(self):
        """'transformed their schools' — past tense + possessive."""
        text = "The revenue has transformed their schools."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "recovery_narrative" in types


class TestFoxBusinessLoadedLanguage:
    """Tests for loaded_language patterns present in the Fox Business article."""

    def test_life_altering(self):
        """'life-altering' — positive magnitude idiom from Sheldon Jones quote."""
        text = "It's life-altering for our teachers and their families."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" in types

    def test_life_changing(self):
        """'life-changing' — synonym for life-altering."""
        text = "The bonuses are life-changing for rural educators."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" in types

    def test_life_transforming(self):
        """'life-transforming' — synonym for life-altering."""
        text = "A life-transforming opportunity for the community."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" in types


class TestFoxBusinessScaleMagnitude:
    """Tests for scale_magnitude detections in the Fox Business article."""

    def test_50_billion(self):
        """'$50 billion' — headline cost anchor."""
        text = "Meta's total investment in the region to more than $50 billion."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "scale_magnitude" in types

    def test_1_6_billion_contracts(self):
        """'$1.6 billion' — local contract value."""
        text = "Louisiana businesses have already received more than $1.6 billion in contracts."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "scale_magnitude" in types

    def test_1_billion_infrastructure(self):
        """'$1 billion' — infrastructure upgrade commitment."""
        text = "plans to spend more than $1 billion on local infrastructure upgrades."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "scale_magnitude" in types

    def test_2_billion_savings(self):
        """'$2 billion' — customer savings claim."""
        text = "expected to save Entergy Louisiana customers more than $2 billion over 20 years."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "scale_magnitude" in types


class TestFoxBusinessKickerFraming:
    """Tests for kicker_framing in the Fox Business article."""

    def test_workforce_kicker(self):
        """'Workforce' — section label directing interpretation of scholarship news."""
        text = "Workforce\n\nMeta is also donating $5 million to Louisiana Delta Community College."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "kicker_framing" in types


class TestFoxBusinessFullArticle:
    """Integration tests running the full Fox Business article through the toolkit."""

    @pytest.fixture
    def fox_article(self):
        with open("examples/sample_output/foxbusiness_meta_louisiana_datacenter_50b_2026_07_13_article.txt") as f:
            return f.read()

    def test_full_article_device_count(self, fox_article):
        """Full article should detect exactly 8 framing devices."""
        devices = detect_framing_devices(fox_article)
        assert len(devices) == 8

    def test_full_article_device_types(self, fox_article):
        """Full article device type distribution."""
        devices = detect_framing_devices(fox_article)
        type_counts = {}
        for d in devices:
            type_counts[d.device_type] = type_counts.get(d.device_type, 0) + 1
        assert type_counts.get("scale_magnitude", 0) == 4
        assert type_counts.get("loaded_language", 0) == 1
        assert type_counts.get("recovery_narrative", 0) == 2
        assert type_counts.get("kicker_framing", 0) == 1

    def test_full_article_no_critical_devices(self, fox_article):
        """Full article should have zero critical framing devices."""
        devices = detect_framing_devices(fox_article)
        critical_types = {"regulatory_shadow", "escalation_amplification"}
        critical_devices = [d for d in devices if d.device_type in critical_types]
        assert len(critical_devices) == 0

    def test_recovery_narrative_evidence_text(self, fox_article):
        """recovery_narrative devices should include 'transforming our schools' and 'reshaping Richland Parish'."""
        devices = detect_framing_devices(fox_article)
        rn_devices = [d for d in devices if d.device_type == "recovery_narrative"]
        assert len(rn_devices) == 2
        evidence = [d.evidence_text.lower() for d in rn_devices]
        assert any("transforming our schools" in e for e in evidence)
        assert any("reshaping" in e for e in evidence)
