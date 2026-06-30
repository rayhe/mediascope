"""Tests for new framing patterns discovered via MIT TR 'Resistance' article.

Covers:
- catastrophizing: 'threat to humanity' pattern
- emotional_appeal: alarm/anxiety idioms
- loaded_language: intensity idioms, polemical nouns, violence references
- social_proof_amplification: poll/survey-based social proof
- scale_magnitude: stalled dollar amounts, percentage-based workforce impact
"""

import pytest

from mediascope.analyze.framing import detect_framing_devices


# --- Helpers ---


def _device_types(text: str) -> set[str]:
    return {d.device_type for d in detect_framing_devices(text)}


def _devices_of_type(text: str, device_type: str) -> list:
    return [d for d in detect_framing_devices(text) if d.device_type == device_type]


# ============================================================
# catastrophizing — threat to humanity/civilization
# ============================================================


class TestCatastrophizingThreatToHumanity:
    def test_threat_to_humanity(self):
        text = "Three-quarters of Americans worry AI could pose a threat to humanity."
        assert "catastrophizing" in _device_types(text)

    def test_threat_to_civilization(self):
        text = "Critics say this technology poses a threat to civilization."
        assert "catastrophizing" in _device_types(text)

    def test_threat_to_democracy(self):
        text = "The report warned AI poses a grave threat to democracy."
        assert "catastrophizing" in _device_types(text)

    def test_threat_to_our_future(self):
        text = "Experts believe it poses a serious threat to our future."
        assert "catastrophizing" in _device_types(text)

    def test_generic_threat_no_match(self):
        """Generic 'threat' without the humanity/civilization target should not match."""
        text = "The storm poses a threat to crops in the region."
        # Should NOT fire catastrophizing for agricultural threats
        devices = _devices_of_type(text, "catastrophizing")
        assert len(devices) == 0


# ============================================================
# emotional_appeal — alarm/anxiety idioms
# ============================================================


class TestEmotionalAppealAlarmIdioms:
    def test_sounding_the_alarm(self):
        text = "Parents are sounding the alarm about chatbot safety."
        assert "emotional_appeal" in _device_types(text)

    def test_deep_anxieties(self):
        text = "The backlash reflects deep anxieties about the future of work."
        assert "emotional_appeal" in _device_types(text)

    def test_fierce_blowback(self):
        text = "The UK government backtracked after fierce blowback from artists."
        assert "emotional_appeal" in _device_types(text)

    def test_widespread_anger(self):
        text = "The decision triggered widespread anger among employees."
        assert "emotional_appeal" in _device_types(text)

    def test_sparked_outrage(self):
        text = "The policy change sparked outrage on social media."
        assert "emotional_appeal" in _device_types(text)

    def test_growing_unease(self):
        text = "There is growing unease about the pace of AI deployment."
        assert "emotional_appeal" in _device_types(text)

    def test_raised_the_alarm(self):
        text = "Regulators raised the alarm about data practices."
        assert "emotional_appeal" in _device_types(text)


# ============================================================
# loaded_language — intensity idioms
# ============================================================


class TestLoadedLanguageIntensityIdioms:
    def test_in_droves(self):
        text = "Users uninstalled ChatGPT in droves."
        assert "loaded_language" in _device_types(text)

    def test_en_masse(self):
        text = "Employees left the company en masse."
        assert "loaded_language" in _device_types(text)

    def test_in_spades(self):
        text = "The company delivered controversy in spades."
        assert "loaded_language" in _device_types(text)


# ============================================================
# loaded_language — polemical nouns
# ============================================================


class TestLoadedLanguagePolemicalNouns:
    def test_diatribe(self):
        text = "He was found carrying an anti-AI diatribe."
        assert "loaded_language" in _device_types(text)

    def test_screed(self):
        text = "The manifesto was a 50-page screed against automation."
        assert "loaded_language" in _device_types(text)

    def test_tirade(self):
        text = "The CEO went on a tirade about government regulation."
        assert "loaded_language" in _device_types(text)


# ============================================================
# loaded_language — violence references
# ============================================================


class TestLoadedLanguageViolenceReferences:
    def test_molotov_cocktail(self):
        text = "A man threw a Molotov cocktail at the CEO's home."
        assert "loaded_language" in _device_types(text)

    def test_death_threats(self):
        text = "The researcher received death threats after publication."
        assert "loaded_language" in _device_types(text)

    def test_arson(self):
        text = "Police investigated the fire as a possible arson."
        assert "loaded_language" in _device_types(text)

    def test_swatting(self):
        text = "The executive was swatted at his home address."
        assert "loaded_language" in _device_types(text)


# ============================================================
# social_proof_amplification — poll/survey-based
# ============================================================


class TestSocialProofPollBased:
    def test_pew_poll_half_of_americans(self):
        text = "A Pew poll found that half of Americans are concerned about AI."
        assert "social_proof_amplification" in _device_types(text)

    def test_three_quarters_of_americans_worry(self):
        text = "Three-quarters of Americans worry AI could threaten jobs."
        assert "social_proof_amplification" in _device_types(text)

    def test_two_thirds_of_respondents(self):
        text = "Two-thirds of respondents said they feared job losses."
        assert "social_proof_amplification" in _device_types(text)

    def test_a_majority_of_adults(self):
        text = "A majority of adults believe AI should be regulated."
        assert "social_proof_amplification" in _device_types(text)

    def test_survey_found_percentage(self):
        text = "A YouGov survey found that 72% of UK adults are worried."
        assert "social_proof_amplification" in _device_types(text)


# ============================================================
# scale_magnitude — stalled dollar amounts
# ============================================================


class TestScaleMagnitudeStalled:
    def test_stalled_dollar_amount(self):
        text = "Activists stalled $98 billion in data center development."
        assert "scale_magnitude" in _device_types(text)

    def test_blocked_dollar_amount(self):
        text = "Regulators blocked $12 billion in proposed mergers."
        assert "scale_magnitude" in _device_types(text)

    def test_halted_dollar_amount(self):
        text = "The court halted $5.2 billion in planned construction."
        assert "scale_magnitude" in _device_types(text)


# ============================================================
# scale_magnitude — percentage workforce impact
# ============================================================


class TestScaleMagnitudeWorkforcePercentage:
    def test_lay_off_40_percent(self):
        text = "Block said it would lay off 40% of its staff."
        assert "scale_magnitude" in _device_types(text)

    def test_cutting_percent_of_workforce(self):
        text = "The company is cutting 15% of its workforce."
        assert "scale_magnitude" in _device_types(text)

    def test_slashing_headcount(self):
        text = "Meta is slashing approximately 10% of its headcount."
        assert "scale_magnitude" in _device_types(text)


# ============================================================
# Integration test: full MIT TR Resistance article
# ============================================================


class TestMITTRResistanceArticle:
    """End-to-end detection on the actual article text."""

    @pytest.fixture
    def article_body(self):
        import pathlib
        path = pathlib.Path(__file__).parent.parent / (
            "examples/sample_output/"
            "mit_tr_resistance_ai_backlash_2026_04_21_article.txt"
        )
        text = path.read_text()
        return text.split("---\n", 1)[1] if "---" in text else text

    def test_minimum_device_count(self, article_body):
        devices = detect_framing_devices(article_body)
        assert len(devices) >= 12, (
            f"Expected >=12 devices, got {len(devices)}: "
            f"{[d.device_type for d in devices]}"
        )

    def test_expected_device_types_present(self, article_body):
        types = _device_types(article_body)
        expected = {
            "catastrophizing",
            "emotional_appeal",
            "loaded_language",
            "social_proof_amplification",
            "scale_magnitude",
        }
        missing = expected - types
        assert not missing, f"Missing expected device types: {missing}"
