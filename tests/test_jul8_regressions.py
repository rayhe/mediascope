"""
Regression tests for Jul 8, 2026 pattern additions (Type A deep dive).

Three patterns added/improved from the Gizmodo "$1.4 Trillion" article analysis:

1. escalation_amplification: "mounting" + legal nouns
2. confession_framing: auxiliary verb constructions ("have admitted to")
3. precedent_framing: "largest ever" without temporal anchor
"""

import pytest
from mediascope.analyze.framing import detect_framing_devices


def _has(devices, device_type):
    return any(d.device_type == device_type for d in devices)


def _count(devices, device_type):
    return sum(1 for d in devices if d.device_type == device_type)


# ─── Escalation Amplification: "mounting" + legal nouns ──────────────────────


class TestMountingEscalation:
    """Tests for 'mounting' as an escalation verb with legal/threat nouns."""

    def test_mounting_litigation(self):
        """Original missed case from Gizmodo $1.4T article."""
        text = "Meta faces mounting litigation over its handling of teen safety."
        devices = detect_framing_devices(text)
        assert _has(devices, "escalation_amplification"), (
            "'mounting litigation' should trigger escalation_amplification"
        )

    def test_mounting_scrutiny(self):
        text = "The company is under mounting scrutiny from regulators."
        devices = detect_framing_devices(text)
        assert _has(devices, "escalation_amplification"), (
            "'mounting scrutiny' should trigger escalation_amplification"
        )

    def test_mounting_legal_challenges(self):
        text = "Apple confronts mounting legal challenges in the EU market."
        devices = detect_framing_devices(text)
        assert _has(devices, "escalation_amplification"), (
            "'mounting legal challenges' should trigger escalation_amplification"
        )

    def test_mounting_legal_trouble(self):
        text = "The startup faces mounting legal trouble over patent claims."
        devices = detect_framing_devices(text)
        assert _has(devices, "escalation_amplification"), (
            "'mounting legal trouble' should trigger escalation_amplification"
        )

    def test_mounting_unrelated_noun_no_match(self):
        """'mounting' with non-escalation nouns should not trigger."""
        text = "The team spent weeks mounting the display on the wall."
        devices = detect_framing_devices(text)
        # Should NOT trigger escalation_amplification for physical mounting
        esc_hits = [d for d in devices if d.device_type == "escalation_amplification"
                    and "mounting" in d.evidence_text.lower()]
        assert len(esc_hits) == 0, (
            "'mounting the display' should not trigger escalation_amplification"
        )


# ─── Confession Framing: auxiliary verb constructions ────────────────────────


class TestConfessionAuxiliaryVerb:
    """Tests for auxiliary verb confession patterns like 'have admitted to'."""

    def test_have_admitted_to_investors(self):
        """Original missed case from Gizmodo $1.4T article."""
        text = (
            "Meta executives have admitted to investors that the platform's "
            "safety measures were insufficient."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "confession_framing"), (
            "'have admitted to investors' should trigger confession_framing"
        )

    def test_has_acknowledged(self):
        text = (
            "The CEO has acknowledged that the product launched before "
            "adequate testing was completed."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "confession_framing"), (
            "'has acknowledged' should trigger confession_framing"
        )

    def test_had_conceded(self):
        text = (
            "Google engineers had conceded that "
            "the privacy controls were largely cosmetic."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "confession_framing"), (
            "'had conceded that' should trigger confession_framing"
        )

    def test_company_lowercase_role_subject(self):
        """Company + lowercase role (e.g., 'Apple engineers') as subject."""
        text = (
            "Apple engineers admitted that the "
            "encryption backdoor had been considered."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "confession_framing"), (
            "'Apple engineers admitted that' should trigger confession_framing"
        )

    def test_meta_executives_have_admitted(self):
        """Full compound subject with auxiliary."""
        text = (
            "Meta executives have admitted that their content moderation "
            "systems failed to catch the majority of harmful posts."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "confession_framing"), (
            "'Meta executives have admitted' should trigger confession_framing"
        )


# ─── Precedent Framing: "largest ever" without temporal anchor ───────────────


class TestLargestEverPrecedent:
    """Tests for 'largest/biggest/most severe... ever' without 'since YYYY'."""

    def test_largest_ever_in_a_case(self):
        """Original missed case from Gizmodo $1.4T article (FTC quote)."""
        text = (
            "The penalty is the largest ever in a case involving an "
            "FTC rule violation."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "precedent_framing"), (
            "'largest ever in a case' should trigger precedent_framing"
        )

    def test_biggest_fine_ever_imposed(self):
        text = "It was the biggest fine ever imposed on a social media company."
        devices = detect_framing_devices(text)
        assert _has(devices, "precedent_framing"), (
            "'biggest fine ever imposed' should trigger precedent_framing"
        )

    def test_most_severe_penalty_ever(self):
        text = (
            "Regulators called it the most severe penalty ever handed "
            "down for a data privacy violation."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "precedent_framing"), (
            "'most severe penalty ever' should trigger precedent_framing"
        )

    def test_largest_ever_recall(self):
        text = "The agency ordered the largest ever recall of a consumer device."
        devices = detect_framing_devices(text)
        assert _has(devices, "precedent_framing"), (
            "'largest ever recall' should trigger precedent_framing"
        )

    def test_largest_since_yyyy_still_works(self):
        """Existing temporal-anchor patterns should still fire."""
        text = "It was the largest antitrust ruling since 2001."
        devices = detect_framing_devices(text)
        assert _has(devices, "precedent_framing"), (
            "'largest...since 2001' should still trigger precedent_framing"
        )

    def test_no_false_positive_largest_generic(self):
        """'largest' without 'ever' or temporal anchor in generic context."""
        text = "It is the largest park in the city."
        devices = detect_framing_devices(text)
        # This may or may not fire depending on other patterns,
        # but should NOT fire as precedent_framing
        prec_hits = [d for d in devices if d.device_type == "precedent_framing"]
        assert len(prec_hits) == 0, (
            "'largest park in the city' should not trigger precedent_framing"
        )
