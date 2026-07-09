"""Tests for market_verdict and overbuilding_narrative framing devices,
and the three new speculative_framing pattern expansions.

Added: Jul 8 2026 Type A deep dive — WSJ AI Spending article gap fixes.
"""

import pytest

from mediascope.analyze.framing import detect_framing_devices


# ── market_verdict ──────────────────────────────────────────────────────


class TestMarketVerdict:
    """market_verdict: market drops framed as editorial judgment."""

    def test_wall_street_sent_signal(self):
        text = "Wall Street has sent a clear signal about AI spending."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "market_verdict" in types

    def test_investors_have_spoken(self):
        text = "Investors have spoken: the capex party is over."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "market_verdict" in types

    def test_the_market_delivered_verdict(self):
        text = "The market has delivered its verdict on Meta's spending plans."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "market_verdict" in types

    def test_fell_percent_as_causal(self):
        """Percentage drop + causal 'as' triggers market_verdict."""
        text = "PHLX fell 11 percent as concerns about overcapacity mounted."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "market_verdict" in types

    def test_dropped_percent_amid(self):
        text = "SK Hynix dropped 17% amid fears of an AI spending slowdown."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "market_verdict" in types

    def test_tumbled_percent_after(self):
        text = "Shares tumbled 9% after the company disclosed rising capex."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "market_verdict" in types

    def test_selloff_amid_concerns(self):
        text = "The sell-off came amid concerns about overinvestment in AI."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "market_verdict" in types

    def test_wiping_value(self):
        text = "The crash wiped $200 billion in market capitalization."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "market_verdict" in types

    def test_spooked_investors(self):
        text = "Spooked investors fled the semiconductor sector."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "market_verdict" in types

    def test_investors_grew_rattled(self):
        text = "Investors grew rattled by the escalating capex forecasts."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "market_verdict" in types

    def test_neutral_drop_no_causal_no_fire(self):
        """Plain percentage drop without causal framing should not fire."""
        text = "Revenue declined 3% in the quarter."
        devices = detect_framing_devices(text)
        mv = [d for d in devices if d.device_type == "market_verdict"]
        assert len(mv) == 0

    def test_neutral_market_mention_no_fire(self):
        """Neutral market context without verdict language should not fire."""
        text = "The stock market opened higher on Monday morning."
        devices = detect_framing_devices(text)
        mv = [d for d in devices if d.device_type == "market_verdict"]
        assert len(mv) == 0


# ── overbuilding_narrative ──────────────────────────────────────────────


class TestOverbuildingNarrative:
    """overbuilding_narrative: infrastructure-as-excess framing."""

    def test_spending_war(self):
        text = "The AI spending war shows no signs of abating."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "overbuilding_narrative" in types

    def test_capex_arms_race(self):
        text = "The capex arms race between Big Tech companies continues."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "overbuilding_narrative" in types

    def test_arms_race_standalone(self):
        text = "Critics call it an arms race with no clear finish line."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "overbuilding_narrative" in types

    def test_overcapacity(self):
        text = "There are growing warnings about overcapacity in data centers."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "overbuilding_narrative" in types

    def test_infrastructure_glut(self):
        text = "Some analysts fear an infrastructure glut is forming."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "overbuilding_narrative" in types

    def test_overbuilding(self):
        text = "The risk of overbuilding is real and underappreciated."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "overbuilding_narrative" in types

    def test_unsustainable_spending(self):
        text = "The trajectory is unsustainable for spending at this pace."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "overbuilding_narrative" in types

    def test_spending_unsustainable_reverse(self):
        text = "Spending at this rate cannot be sustained indefinitely."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "overbuilding_narrative" in types

    def test_when_will_someone_blink(self):
        text = "When will someone blink in this high-stakes poker game?"
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "overbuilding_narrative" in types

    def test_ai_bubble(self):
        text = "The AI bubble could burst just like the dot-com crash."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "overbuilding_narrative" in types

    def test_tech_euphoria(self):
        text = "The tech euphoria around AI investment may be peaking."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "overbuilding_narrative" in types

    def test_throwing_money(self):
        text = "Companies are throwing money at AI infrastructure."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "overbuilding_narrative" in types

    def test_pouring_billions_into(self):
        text = "Big Tech is pouring billions into data centers."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "overbuilding_narrative" in types

    def test_neutral_investment_no_fire(self):
        """Neutral investment language without excess framing should not fire."""
        text = "Meta announced plans to invest in new data centers."
        devices = detect_framing_devices(text)
        ob = [d for d in devices if d.device_type == "overbuilding_narrative"]
        assert len(ob) == 0

    def test_neutral_spending_no_fire(self):
        """Plain spending mention without war/bubble/excess should not fire."""
        text = "Capital expenditures rose to $30 billion in the quarter."
        devices = detect_framing_devices(text)
        ob = [d for d in devices if d.device_type == "overbuilding_narrative"]
        assert len(ob) == 0


# ── speculative_framing new patterns ────────────────────────────────────


class TestSpeculativeFramingExpansion:
    """Tests for the three new speculative_framing patterns added Jul 8."""

    def test_may_be_getting(self):
        """'may be [verb]ing' pattern catches hedged progressive."""
        text = (
            "Meta may be getting in on that action. The move may be signaling "
            "a shift. This may be setting the stage. It could alter dynamics. "
            "In theory the returns are uncertain. It is possible that growth "
            "will stall. The suggests that margins could shrink."
        )
        devices = detect_framing_devices(text)
        spec = [d for d in devices if d.device_type == "speculative_framing"]
        evidence = [d.evidence_text for d in spec]
        assert any("may be getting" in e for e in evidence)

    def test_would_effectively(self):
        """'would [adverb] [verb]' catches hypothetical confirmation."""
        text = (
            "This would effectively confirm the cloud pivot. It would "
            "essentially validate the thesis. The deal would arguably "
            "demonstrate scale. In theory the market agrees. It is possible "
            "the trend continues. Playing this forward, the result suggests "
            "that prices could rise."
        )
        devices = detect_framing_devices(text)
        spec = [d for d in devices if d.device_type == "speculative_framing"]
        evidence = [d.evidence_text for d in spec]
        assert any("would effectively" in e for e in evidence)

    def test_could_be_tripped(self):
        """'could be [past participle]' catches passive speculative."""
        text = (
            "The strategy could be tripped up by overcapacity. Revenue "
            "could be undermined by competition. Growth could be derailed "
            "by regulation. In theory the risk is real. It is possible that "
            "margins will compress. This suggests that returns could decline."
        )
        devices = detect_framing_devices(text)
        spec = [d for d in devices if d.device_type == "speculative_framing"]
        evidence = [d.evidence_text for d in spec]
        assert any("could be tripped" in e for e in evidence)

    def test_may_be_verb_standalone_below_threshold_no_fire(self):
        """Single 'may be [verb]ing' below 5-marker threshold doesn't fire."""
        text = "Meta may be getting in on that action."
        devices = detect_framing_devices(text)
        spec = [d for d in devices if d.device_type == "speculative_framing"]
        assert len(spec) == 0, "Single hedge below threshold should not fire"

    def test_would_adverb_standalone_below_threshold_no_fire(self):
        """Single 'would effectively' below threshold doesn't fire."""
        text = "This would effectively confirm the deal."
        devices = detect_framing_devices(text)
        spec = [d for d in devices if d.device_type == "speculative_framing"]
        assert len(spec) == 0, "Single hedge below threshold should not fire"
