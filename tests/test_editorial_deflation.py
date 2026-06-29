"""Tests for editorial_deflation framing device detection.

Editorial deflation is a technique where the writer builds up an ambitious
vision and then deflates it with a brief dismissive phrase, implying failure
without explicit argument.

Discovered via MIT Technology Review "Inside Anduril and Meta's quest to make
smart glasses for warfare" (May 18, 2026), where "That's the idea, anyway"
follows three paragraphs of ambitious AR battlefield vision.
"""

import pytest
from mediascope.analyze.framing import detect_framing_devices


# ---------------------------------------------------------------------------
#  Positive cases — should detect editorial_deflation
# ---------------------------------------------------------------------------

class TestEditorialDeflationPositive:
    """Texts that should trigger editorial_deflation detection."""

    def test_thats_the_idea_anyway(self):
        """Classic construction from MIT TR Anduril article."""
        text = (
            "A soldier might send a drone to surveil an area and instruct it to "
            "come back once it's found something that looks like an artillery unit; "
            "then the system would recommend courses of action, like sending a "
            "nearby drone to strike. That's the idea, anyway. It's worked on "
            "early prototypes, but there aren't yet versions ready to test."
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" in types

    def test_thats_the_plan_anyway(self):
        text = "The company aims to replace all its servers by 2028. That's the plan, anyway."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" in types

    def test_thats_the_hope_at_least(self):
        text = "AI agents will handle all customer service. That's the hope, at least."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" in types

    def test_thats_the_vision_for_now(self):
        text = "The headset will overlay battle intelligence in real time. That's the vision, for now."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" in types

    def test_or_so_he_claims(self):
        text = "The system will be ready by next quarter, or so he claims."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" in types

    def test_or_so_the_company_insists(self):
        text = "The data is fully encrypted, or so the company insists."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" in types

    def test_or_so_zuckerberg_hopes(self):
        text = "Meta will have 100 million predictors by year end, or so Zuckerberg hopes."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" in types

    def test_so_the_argument_goes(self):
        text = "Open-source AI benefits everyone. So the argument goes."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" in types

    def test_so_the_thinking_goes(self):
        text = "More compute will solve alignment. Or so the thinking goes."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" in types

    def test_if_it_ever_actually_works(self):
        text = "The glasses will give soldiers superhuman perception, if it ever actually works."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" in types

    def test_if_it_ever_actually_ships(self):
        text = "The product could change how we interact with AI, if it ever actually ships."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" in types

    def test_if_it_ever_actually_materializes(self):
        text = "The partnership could transform defense procurement, if it ever actually materializes."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" in types

    def test_in_theory_anyway(self):
        text = "The AI should be able to handle the complexity. In theory, anyway."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" in types

    def test_in_theory_at_least(self):
        text = "Open models let anyone audit for bias. In theory, at least."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" in types

    def test_thats_a_big_if(self):
        text = "Meta could dominate the prediction market space. But that's a big if."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" in types

    def test_thats_a_big_assumption(self):
        text = "Users will switch from Polymarket. But that's a big assumption."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" in types

    def test_whether_that_actually_works(self):
        text = "The company believes AI agents will handle all interactions. Whether that actually works is another matter."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" in types

    def test_whether_it_actually_pans_out(self):
        text = "Meta is investing billions in the metaverse. Whether it actually pans out remains unclear."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" in types


# ---------------------------------------------------------------------------
#  Negative cases — should NOT detect editorial_deflation
# ---------------------------------------------------------------------------

class TestEditorialDeflationNegative:
    """Texts that should NOT trigger editorial_deflation."""

    def test_neutral_hedging_remains_to_be_seen(self):
        """Generic hedging should not trigger."""
        text = "The results of the trial remain to be seen."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" not in types

    def test_neutral_time_will_tell(self):
        """Generic hedging should not trigger."""
        text = "Time will tell whether the policy succeeds."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" not in types

    def test_neutral_in_theory(self):
        """'in theory' without deflating qualifier should not trigger."""
        text = "In theory, small modular reactors will make fission cheaper."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" not in types

    def test_neutral_plan_statement(self):
        """Straightforward plan statement should not trigger."""
        text = "The plan is to deploy the system by Q4 2027."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" not in types

    def test_neutral_idea(self):
        """Neutral use of 'idea' should not trigger."""
        text = "That's the idea behind the new architecture."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" not in types


# ---------------------------------------------------------------------------
#  Integration test — MIT TR Anduril article excerpt
# ---------------------------------------------------------------------------

class TestEditorialDeflationIntegration:
    """Integration test with real article text."""

    def test_mit_tr_anduril_article(self):
        """Full MIT TR article passage should detect editorial_deflation."""
        text = (
            "Barnett's team is designing the headset to carry out multi-step tasks. "
            "A soldier might send a drone to surveil an area and instruct it to come "
            "back once it's found something that looks like an artillery unit; then "
            "the system would recommend courses of action, like sending a nearby drone "
            "to strike, that would have to be approved by the normal chain of command. "
            "Leading the system through this, if all goes to plan, might not even "
            "require speech; the soldier could instead communicate through tracked eye "
            "movements and subtle taps.\n\n"
            "That's the idea, anyway. It's worked on early prototypes, Barnett says, "
            "but there aren't yet versions ready for the Army to test at scale."
        )
        devices = detect_framing_devices(text)
        deflation = [d for d in devices if d.device_type == "editorial_deflation"]
        assert len(deflation) >= 1
        assert "idea, anyway" in deflation[0].evidence_text.lower()

    def test_no_false_positives_on_neutral_hedging(self):
        """Reuters-style factual hedging should not trigger."""
        text = (
            "Meta and Kalshi did not immediately respond to requests for comment, "
            "while Polymarket declined to comment when contacted by Reuters. "
            "Reuters could not independently verify the report. "
            "The social media company's executives have said Arena will differ from "
            "Polymarket and Kalshi because it will instead rely on video-game-like "
            "'points', the report said."
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" not in types
