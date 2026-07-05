"""Tests for patterns discovered in Wired Conversation Focus paywall article.

Wired article: "Meta Is Charging a Subscription for Smart Glasses Features.
Welcome to the New Era of Consumer Tech" (Jul 2, 2026, Julian Chokkattu).

Gap discoveries:
- consumer_ownership: "runs on-device" without adverb (entirely/completely)
  didn't match the forward pattern, which required an adverb group.
- expert_contradiction: named expert (Chris Harrison, Carnegie Mellon)
  directly contradicting Meta's stated justification with "It's not about
  recovering AI costs; it's about monetizing customers."
- loss_leader_framing: "sold at cost" + "subscription service grows revenue"
  revealing razor/blade business model.
- editorial_aside: sarcastic "Guess..." sentence opener.
- emotional_language: "monetize", "pay up", "extracting value", "sold at cost"
  missing from the emotional language list.
- sentiment correction Path J: expert-driven structural critique where VADER
  scores +0.69 because corporate PR quotes dominate lexically, but structural
  framing is editorially critical.
"""

import re

import pytest

from mediascope.analyze.framing import (
    FramingDevice,
    detect_framing_devices,
    _DEVICE_PATTERNS,
)
from mediascope.analyze.sentiment import (
    EMOTIONAL_LANGUAGE,
    analyze_composite,
)


class TestConsumerOwnershipNoAdverb:
    """consumer_ownership must fire on 'runs on-device' without adverb."""

    def test_runs_on_device_no_adverb(self):
        text = (
            "the Conversation Focus feature runs on-device, meaning it "
            "doesn't need to head to Meta's servers for AI processing. "
            "There's no real reason to charge a subscription for it."
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "consumer_ownership" in types, (
            f"Expected consumer_ownership for 'runs on-device' (no adverb), "
            f"got: {types}"
        )

    def test_runs_on_device_with_adverb_still_works(self):
        text = (
            "the model runs entirely on-device with no cloud dependency. "
            "Users must pay a monthly subscription to access it."
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "consumer_ownership" in types

    def test_runs_on_device_reverse_doesnt_need_servers(self):
        """Reverse pattern: subscription near 'doesn't need to head to servers'."""
        text = (
            "Despite the new subscription requirement, the feature "
            "doesn't need to head to the company's servers at all."
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "consumer_ownership" in types, (
            f"Expected consumer_ownership for reverse "
            f"'doesn't need to head to servers', got: {types}"
        )


class TestExpertContradiction:
    """expert_contradiction: named expert contradicts corporate justification."""

    def test_its_not_about_x_its_about_y(self):
        text = (
            'Harrison doesn\'t think the subscription is to help pay for '
            'anything. "It\'s not about recovering AI costs; it\'s about '
            'monetizing customers," he says.'
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "expert_contradiction" in types, (
            f"Expected expert_contradiction for 'It's not about X; "
            f"it's about Y', got: {types}"
        )

    def test_doesnt_think_subscription_is_to_help(self):
        text = (
            "He doesn't think the new subscription is to help pay for "
            "compute costs."
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "expert_contradiction" in types

    def test_no_false_positive_on_regular_statement(self):
        """A normal 'doesn't think' in non-subscription context should not fire."""
        text = "She doesn't think the weather will improve tomorrow."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "expert_contradiction" not in types

    def test_its_not_about_with_smart_quotes(self):
        text = (
            '\u201cIt\u2019s not about innovation; it\u2019s about '
            'extracting value from users.\u201d'
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "expert_contradiction" in types


class TestLossLeaderFraming:
    """loss_leader_framing: sold at cost + subscription revenue model."""

    def test_sold_at_cost(self):
        text = (
            "The company's glasses are typically sold at cost, like the "
            "new $299 Meta-branded glasses."
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loss_leader_framing" in types

    def test_user_base_subscription_grows(self):
        text = (
            "This helps get the glasses out in the world and increases "
            "the user base \u2014 then the subscription service grows "
            "revenue significantly."
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loss_leader_framing" in types

    def test_sold_below_cost(self):
        text = "The headsets are sold below cost to build market share."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loss_leader_framing" in types


class TestEditorialAsideGuess:
    """editorial_aside: sarcastic 'Guess...' sentence opener."""

    def test_guess_sarcastic_aside(self):
        text = (
            "The AI couldn't reliably identify speakers in noisy rooms. "
            "Guess humans are better at some things after all."
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_aside" in types

    def test_guess_apparently(self):
        text = (
            "Meta removed the feature from the free tier. "
            "Guess they needed the money apparently."
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_aside" in types

    def test_no_false_positive_guess_what(self):
        """'Guess what' is not sarcastic editorial, it's exclamation."""
        text = "Guess what the new feature does."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        # Should not fire editorial_aside for "Guess what"
        guess_asides = [
            d for d in devices
            if d.device_type == "editorial_aside" and "Guess" in (d.evidence_text or "")
        ]
        assert len(guess_asides) == 0


class TestEmotionalLanguageTerms:
    """Verify new emotional language terms are in the list."""

    @pytest.mark.parametrize("term", [
        "monetize", "monetizing", "monetized", "monetization",
        "extracting value",
        "pay up",
        "sold at cost",
    ])
    def test_term_in_emotional_language(self, term):
        assert term in EMOTIONAL_LANGUAGE, (
            f"'{term}' should be in EMOTIONAL_LANGUAGE list"
        )


class TestSentimentPathJ:
    """Path J: expert-driven structural critique correction."""

    def test_wired_subscription_article_correction(self):
        """Full Wired article should trigger framing correction."""
        with open(
            "examples/sample_output/"
            "wired_meta_glasses_subscription_era_2026_07_02_article.txt"
        ) as f:
            text = f.read()

        headline = (
            "Meta Is Charging a Subscription for Smart Glasses Features. "
            "Welcome to the New Era of Consumer Tech"
        )
        sr = analyze_composite(text, headline=headline)
        assert sr.framing_corrected, (
            f"Expected framing_corrected=True, raw_tone={sr.raw_tone}, "
            f"overall_tone={sr.overall_tone}, EI={sr.emotional_language_intensity}"
        )
        # Corrected tone should be <= 0 (not positive)
        assert sr.overall_tone <= 0.0, (
            f"Expected non-positive corrected tone, got {sr.overall_tone}"
        )
        # Raw tone should remain positive (VADER sees corporate quotes)
        assert sr.raw_tone > 0.5

    def test_synthetic_expert_structural_critique(self):
        """Synthetic article with expert contradiction + loss-leader."""
        text = (
            'The $299 headset is sold at cost to build adoption. '
            '"We\'re investing in the future," the CEO said. '
            'But Professor Smith at MIT doesn\'t think the new '
            'subscription is to help pay for compute. '
            '"It\'s not about recovering costs; it\'s about monetizing '
            'the user base," Smith told reporters. '
            'The feature runs on-device and doesn\'t need cloud servers. '
            'Google doesn\'t charge for the same capability. '
            'Once the user base grows, the subscription service grows '
            'revenue. "Worth $10 a month? Probably," he added.'
        )
        headline = "Company Charges Subscription for On-Device Feature"
        sr = analyze_composite(text, headline=headline)
        # Should trigger correction (may be Path J or I)
        assert sr.framing_corrected, (
            f"Expected framing correction on expert-structural critique. "
            f"raw_tone={sr.raw_tone}, EI={sr.emotional_language_intensity}"
        )
