"""Tests for latecomer_narrative and regulatory_shadow framing device types.

latecomer_narrative detects editorial framing that positions a company as
entering a space after competitors, emphasizing catch-up rather than
innovation — "exploring partnerships with," "joining the race,"
"playing catch-up."

regulatory_shadow detects the ambient technique of inserting regulatory/legal
context into stories where it is tangential to the primary subject — casting
a shadow over a product or business announcement without direct accusation.

Both identified from NYT's "Meta Explores Polymarket/Kalshi Partnerships
for Arena" article (June 26, 2026), where Meta's Arena product is framed as
a latecomer to prediction markets and regulatory scrutiny from the
broader prediction market industry is applied to Meta's product story.
"""

import pytest

from mediascope.analyze.framing import detect_framing_devices, FramingDevice


def _has(devices: list[FramingDevice], device_type: str) -> bool:
    """Check if a specific device type was detected."""
    return any(d.device_type == device_type for d in devices)


def _count(devices: list[FramingDevice], device_type: str) -> int:
    """Count occurrences of a specific device type."""
    return sum(1 for d in devices if d.device_type == device_type)


def _types(devices: list[FramingDevice]) -> list[str]:
    """Extract sorted unique device types."""
    return sorted(set(d.device_type for d in devices))


# ===================================================================
# Latecomer Narrative — Positive detections
# ===================================================================


class TestLatecomerNarrativePositive:
    """Patterns that should trigger latecomer_narrative."""

    def test_exploring_partnerships_with(self):
        """'Exploring partnerships with [established player]' — the Arena pattern."""
        text = (
            "Meta is exploring partnerships with Polymarket and Kalshi "
            "to integrate prediction markets into Arena."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "latecomer_narrative"), (
            f"Expected latecomer_narrative, got: {_types(devices)}"
        )

    def test_joining_the_race(self):
        """'Joining the race' — competitive latecomer framing."""
        text = (
            "The social media giant is joining the race to offer "
            "prediction market features to its users."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "latecomer_narrative"), (
            f"Expected latecomer_narrative, got: {_types(devices)}"
        )

    def test_entering_the_market(self):
        """'Entering a market' — market-entry framing."""
        text = (
            "Meta is entering the market for real-money prediction "
            "platforms, a space where Polymarket has operated since 2020."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "latecomer_narrative"), (
            f"Expected latecomer_narrative, got: {_types(devices)}"
        )

    def test_following_in_footsteps(self):
        """'Following in the footsteps of' — historical latecomer."""
        text = (
            "Meta is following in the footsteps of Google, which launched "
            "its own prediction market product last year."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "latecomer_narrative"), (
            f"Expected latecomer_narrative, got: {_types(devices)}"
        )

    def test_building_similar_app(self):
        """'Building a similar app' — copycat framing."""
        text = (
            "The company is building a similar app to compete with "
            "established prediction market platforms."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "latecomer_narrative"), (
            f"Expected latecomer_narrative, got: {_types(devices)}"
        )

    def test_market_already_dominated_by(self):
        """'Market already dominated by' — established competitors."""
        text = (
            "Meta enters a market already dominated by Polymarket and "
            "Kalshi, both of which processed billions in trades last year."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "latecomer_narrative"), (
            f"Expected latecomer_narrative, got: {_types(devices)}"
        )

    def test_playing_catch_up(self):
        """'Playing catch-up' — explicit latecomer language."""
        text = (
            "The move suggests Meta is playing catch-up in a category "
            "that rivals have dominated for years."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "latecomer_narrative"), (
            f"Expected latecomer_narrative, got: {_types(devices)}"
        )

    def test_late_to_the_game(self):
        """'Late to the game' — colloquial latecomer."""
        text = (
            "Critics say Meta is late to the game, with competitors "
            "having built loyal user bases well ahead of Arena's launch."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "latecomer_narrative"), (
            f"Expected latecomer_narrative, got: {_types(devices)}"
        )

    def test_behind_the_curve(self):
        """'Behind the curve' — capability gap."""
        text = (
            "The company remains behind the curve on prediction markets, "
            "a space where even smaller startups have found traction."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "latecomer_narrative"), (
            f"Expected latecomer_narrative, got: {_types(devices)}"
        )

    def test_developing_its_own_competing_version(self):
        """'Developing its own competing product' — derivative framing."""
        text = (
            "Meta is developing its own competing platform that would "
            "allow users to bet on real-world events."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "latecomer_narrative"), (
            f"Expected latecomer_narrative, got: {_types(devices)}"
        )

    def test_has_yet_to_develop(self):
        """'Has yet to develop' — capability gap framing."""
        text = (
            "Unlike Polymarket, Meta has yet to develop the regulatory "
            "relationships needed to operate a prediction market."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "latecomer_narrative"), (
            f"Expected latecomer_narrative, got: {_types(devices)}"
        )

    def test_scrambling_to_catch_up(self):
        """'Scrambling to catch up' — urgency + latecomer."""
        text = (
            "Meta is scrambling to catch up with Kalshi after the "
            "platform's breakout election-year success."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "latecomer_narrative"), (
            f"Expected latecomer_narrative, got: {_types(devices)}"
        )

    def test_taking_a_page_from(self):
        """'Taking a page from' — imitation framing."""
        text = (
            "Zuckerberg appears to be taking a page from Kalshi's "
            "playbook with the new Arena features."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "latecomer_narrative"), (
            f"Expected latecomer_narrative, got: {_types(devices)}"
        )


# ===================================================================
# Latecomer Narrative — Negative detections
# ===================================================================


class TestLatecomerNarrativeNegative:
    """Patterns that should NOT trigger latecomer_narrative."""

    def test_neutral_partnership_announcement(self):
        """Neutral partnership language without latecomer framing."""
        text = (
            "Meta announced a partnership with Microsoft to improve "
            "AI model interoperability."
        )
        devices = detect_framing_devices(text)
        assert not _has(devices, "latecomer_narrative"), (
            "Neutral partnership announcement should not fire latecomer_narrative"
        )

    def test_launching_new_product_innovator(self):
        """Launching a genuinely new product (innovation, not catch-up)."""
        text = (
            "Meta launched a new feature that lets users create "
            "custom AI characters for group chats."
        )
        devices = detect_framing_devices(text)
        assert not _has(devices, "latecomer_narrative"), (
            "Innovation language should not fire latecomer_narrative"
        )


# ===================================================================
# Regulatory Shadow — Positive detections
# ===================================================================


class TestRegulatoryShadowPositive:
    """Patterns that should trigger regulatory_shadow."""

    def test_increasing_scrutiny(self):
        """'Increasing scrutiny' — ambient regulatory atmosphere."""
        text = (
            "The move comes at a time of increasing scrutiny of "
            "prediction market platforms by federal regulators."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "regulatory_shadow"), (
            f"Expected regulatory_shadow, got: {_types(devices)}"
        )

    def test_drawn_scrutiny_from_regulators(self):
        """'Drawn scrutiny from' — attracting regulatory attention."""
        text = (
            "Polymarket has drawn scrutiny from the Commodity Futures "
            "Trading Commission over its election contracts."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "regulatory_shadow"), (
            f"Expected regulatory_shadow, got: {_types(devices)}"
        )

    def test_facing_regulatory_challenges(self):
        """'Facing regulatory challenges' — explicit regulatory framing."""
        text = (
            "The prediction market industry is facing regulatory "
            "challenges as states consider new gambling legislation."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "regulatory_shadow"), (
            f"Expected regulatory_shadow, got: {_types(devices)}"
        )

    def test_regulators_investigating(self):
        """'Regulators have investigated' — active regulatory agents."""
        text = (
            "Regulators have investigated several prediction market "
            "platforms for potential violations of commodities law."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "regulatory_shadow"), (
            f"Expected regulatory_shadow, got: {_types(devices)}"
        )

    def test_amid_antitrust(self):
        """'Amid antitrust' — product news shadowed by regulatory context."""
        text = (
            "Meta announced the Arena expansion amid antitrust "
            "concerns and ongoing FTC litigation."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "regulatory_shadow"), (
            f"Expected regulatory_shadow, got: {_types(devices)}"
        )

    def test_raised_concerns_about(self):
        """'Raised concerns about' — unattributed worry."""
        text = (
            "The partnership has raised concerns about whether Meta "
            "could use prediction market data for targeted advertising."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "regulatory_shadow"), (
            f"Expected regulatory_shadow, got: {_types(devices)}"
        )

    def test_potential_fine(self):
        """'Potential fine' — implied legal consequences."""
        text = (
            "Companies operating without proper licenses could face "
            "potential fines of up to $1 million per violation."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "regulatory_shadow"), (
            f"Expected regulatory_shadow, got: {_types(devices)}"
        )

    def test_could_face_regulatory(self):
        """'Could face regulatory' — speculative regulatory consequence."""
        text = (
            "Meta could face regulatory backlash if Arena allows users "
            "to bet on election outcomes."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "regulatory_shadow"), (
            f"Expected regulatory_shadow, got: {_types(devices)}"
        )

    def test_growing_scrutiny(self):
        """'Growing scrutiny' — escalating attention variant."""
        text = (
            "Prediction markets have come under growing scrutiny after "
            "allegations of insider trading on Polymarket."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "regulatory_shadow"), (
            f"Expected regulatory_shadow, got: {_types(devices)}"
        )

    def test_despite_investigation(self):
        """'Despite investigation' — shadow via concessive clause."""
        text = (
            "Meta pressed ahead with the Arena launch despite an "
            "ongoing investigation into prediction market manipulation."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "regulatory_shadow"), (
            f"Expected regulatory_shadow, got: {_types(devices)}"
        )

    def test_sparked_concerns_over(self):
        """'Sparked concerns over' — worry ignition."""
        text = (
            "The announcement sparked concerns over data privacy and "
            "the potential for market manipulation."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "regulatory_shadow"), (
            f"Expected regulatory_shadow, got: {_types(devices)}"
        )

    def test_regulators_warned(self):
        """'Regulators warned' — active regulatory voice."""
        text = (
            "Regulators warned that prediction markets could become "
            "vehicles for money laundering without proper oversight."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "regulatory_shadow"), (
            f"Expected regulatory_shadow, got: {_types(devices)}"
        )

    def test_mounting_scrutiny(self):
        """'Mounting scrutiny' — intensifying attention."""
        text = (
            "The deal comes amid mounting regulatory scrutiny of "
            "social media companies entering financial services."
        )
        devices = detect_framing_devices(text)
        assert _has(devices, "regulatory_shadow"), (
            f"Expected regulatory_shadow, got: {_types(devices)}"
        )


# ===================================================================
# Regulatory Shadow — Negative detections
# ===================================================================


class TestRegulatoryShadowNegative:
    """Patterns that should NOT trigger regulatory_shadow."""

    def test_neutral_regulation_reporting(self):
        """Straightforward regulation reporting (no shadow framing)."""
        text = (
            "The SEC published new guidelines for digital asset "
            "custody requirements on Tuesday."
        )
        devices = detect_framing_devices(text)
        assert not _has(devices, "regulatory_shadow"), (
            "Neutral regulation reporting should not fire regulatory_shadow"
        )

    def test_company_compliance_positive(self):
        """Company proactively seeking compliance — not a shadow."""
        text = (
            "Meta said it would work with regulators to ensure Arena "
            "complied with all applicable laws."
        )
        devices = detect_framing_devices(text)
        assert not _has(devices, "regulatory_shadow"), (
            "Proactive compliance language should not fire regulatory_shadow"
        )


# ===================================================================
# Integration: both devices on reconstructed Arena article text
# ===================================================================


class TestArenaArticleIntegration:
    """Both devices should fire on Arena article-derived text."""

    ARENA_EXCERPT = (
        "Mark Zuckerberg has asked Meta executives to explore partnerships "
        "with Polymarket and Kalshi, according to three people with knowledge "
        "of the discussions, as the company seeks to expand Arena beyond "
        "sports prediction games. The move would put Meta into a market "
        "already dominated by Polymarket, which processed more than $9 billion "
        "in trades during the 2024 election cycle. Prediction markets have "
        "drawn increasing scrutiny from regulators, with the CFTC pursuing "
        "enforcement actions against several platforms. Meta could face "
        "regulatory challenges if it moves forward with real-money prediction "
        "contracts, given the company's existing antitrust litigation."
    )

    def test_arena_latecomer_narrative(self):
        """Arena excerpt should trigger latecomer_narrative."""
        devices = detect_framing_devices(self.ARENA_EXCERPT)
        assert _has(devices, "latecomer_narrative"), (
            f"Expected latecomer_narrative in Arena excerpt, got: {_types(devices)}"
        )

    def test_arena_regulatory_shadow(self):
        """Arena excerpt should trigger regulatory_shadow."""
        devices = detect_framing_devices(self.ARENA_EXCERPT)
        assert _has(devices, "regulatory_shadow"), (
            f"Expected regulatory_shadow in Arena excerpt, got: {_types(devices)}"
        )

    def test_arena_both_devices(self):
        """Arena excerpt should trigger both latecomer_narrative and regulatory_shadow."""
        devices = detect_framing_devices(self.ARENA_EXCERPT)
        detected_types = set(d.device_type for d in devices)
        assert "latecomer_narrative" in detected_types, (
            f"Missing latecomer_narrative in Arena excerpt"
        )
        assert "regulatory_shadow" in detected_types, (
            f"Missing regulatory_shadow in Arena excerpt"
        )
