"""
Test framing detection for Kotaku "Meta Removes Default AI Integration On Instagram"
(~Jul 11, 2026).

Covers:
- New `editorial_character_attack` device type (3 patterns)
- New loaded_language terms (encroachment, regurgitated, cloak and daggery,
  cause for alarm/worry, unsavory, unnerving, curtly, quell suspicions)
- Entity detection for Meta, Instagram, SAG-AFTRA, Muse Image
- policy_reversal detection

Discovery article for device #102 (editorial_character_attack).
"""

import pathlib

import pytest

from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.entities import detect_entities

_ARTICLE_PATH = (
    pathlib.Path(__file__).resolve().parent.parent
    / "examples"
    / "sample_output"
    / "kotaku_meta_muse_image_removed_2026_07_11_article.txt"
)


@pytest.fixture(scope="module")
def article_text() -> str:
    return _ARTICLE_PATH.read_text()


@pytest.fixture(scope="module")
def devices(article_text):
    return detect_framing_devices(article_text)


@pytest.fixture(scope="module")
def entities(article_text):
    return detect_entities(article_text)


# ---------- editorial_character_attack ----------


class TestEditorialCharacterAttack:
    """Tests for the new editorial_character_attack device type."""

    def test_best_known_for_unethical(self, devices):
        """'best known for unethical' is editorial character judgment."""
        matches = [
            d for d in devices
            if d.device_type == "editorial_character_attack"
            and "best known for" in d.evidence_text.lower()
        ]
        assert matches, (
            "Expected editorial_character_attack for 'best known for unethical'"
        )

    def test_hes_the_guy_for_that(self, devices):
        """'he's the guy for that' is casual editorial character dismissal."""
        matches = [
            d for d in devices
            if d.device_type == "editorial_character_attack"
            and "the guy" in d.evidence_text.lower()
        ]
        assert matches, (
            "Expected editorial_character_attack for 'he's the guy for that'"
        )

    def test_editorial_character_attack_count(self, devices):
        """Article should produce exactly 2 editorial_character_attack hits."""
        count = sum(
            1 for d in devices if d.device_type == "editorial_character_attack"
        )
        assert count == 2, f"Expected 2 editorial_character_attack, got {count}"


# ---------- loaded_language new terms ----------


class TestNewLoadedLanguageTerms:
    """Tests for loaded_language terms added in this iteration."""

    @pytest.mark.parametrize(
        "term",
        [
            "encroachment",
            "regurgitated",
            "cloak and daggery",
            "cause for alarm",
            "cause for worry",
            "unsavory",
            "unnerving",
            "curtly",
            "quell suspicions",
        ],
    )
    def test_loaded_language_term_detected(self, devices, term):
        """Each new loaded_language term should be detected in this article."""
        matches = [
            d for d in devices
            if d.device_type == "loaded_language"
            and term.lower() in d.evidence_text.lower()
        ]
        assert matches, f"Expected loaded_language detection for '{term}'"

    def test_loaded_language_count(self, devices):
        """Article should produce at least 10 loaded_language hits."""
        count = sum(
            1 for d in devices if d.device_type == "loaded_language"
        )
        assert count >= 10, f"Expected ≥10 loaded_language, got {count}"


# ---------- policy_reversal ----------


class TestPolicyReversal:
    """Tests for policy_reversal detection."""

    def test_no_longer_available(self, devices):
        """'it's no longer available' triggers policy_reversal."""
        matches = [
            d for d in devices
            if d.device_type == "policy_reversal"
            and "no longer available" in d.evidence_text.lower()
        ]
        assert matches, (
            "Expected policy_reversal for 'it's no longer available'"
        )


# ---------- Entity detection ----------


class TestEntityDetection:
    """Tests for entity extraction on this article."""

    def test_meta_cluster_present(self, entities):
        """Meta cluster should be detected with multiple mentions."""
        meta_ents = [e for e in entities if e.cluster == "Meta"]
        assert len(meta_ents) >= 10, (
            f"Expected ≥10 Meta cluster mentions, got {len(meta_ents)}"
        )

    def test_sagaftra_detected(self, entities):
        """SAG-AFTRA should be detected in Labor/Unions cluster."""
        sag = [
            e for e in entities
            if "sag" in e.canonical_name.lower()
            or "sag-aftra" in e.entity.lower()
        ]
        assert sag, "Expected SAG-AFTRA entity detection"

    def test_instagram_detected(self, entities):
        """Instagram should be detected as Meta cluster entity."""
        ig = [
            e for e in entities
            if e.canonical_name == "Instagram"
        ]
        assert len(ig) >= 3, (
            f"Expected ≥3 Instagram mentions, got {len(ig)}"
        )

    def test_muse_image_detected(self, entities):
        """Muse Image should be detected as Meta cluster entity."""
        muse = [
            e for e in entities
            if "muse" in e.entity.lower()
        ]
        assert muse, "Expected Muse Image entity detection"


# ---------- Overall detection quality ----------


class TestOverallDetection:
    """Tests for overall detection quality on this article."""

    def test_total_device_count(self, devices):
        """Article should produce at least 13 framing devices total."""
        assert len(devices) >= 13, (
            f"Expected ≥13 total devices, got {len(devices)}"
        )

    def test_unique_device_types(self, devices):
        """Article should produce at least 3 unique device types."""
        unique = len(set(d.device_type for d in devices))
        assert unique >= 3, f"Expected ≥3 unique types, got {unique}"
