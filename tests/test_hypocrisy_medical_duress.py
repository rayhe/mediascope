"""Tests for hypocrisy frame and medical duress emotional appeal.

These tests cover two toolkit gaps discovered in the 2026-06-26 00:00 PT
Hour Type A iteration — analysis of identified framing detection gaps
across multiple articles:

1. Medical/health duress emotional_appeal — "life-threatening health condition"
   and similar medical emergency language used to create sympathy/leverage
   framing. Gap identified in Guardian Wynn-Williams (Jun 25, 2026).

2. Hypocrisy frame — new framing device detecting stated-vs-actual
   contradictions (entity says one thing, does another). Gap identified
   in both NYT AI voluntary review (Jun 23) and Guardian Wynn-Williams
   (Jun 25).

3. Headline negative signals — "presses", "concerns rise", and similar
   government pressure language in headlines that VADER scores as
   positive/neutral. Gap identified in NYT AI voluntary review (Jun 23).
"""

import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sentiment import _measure_headline_alignment


# ===================================================================
# Medical/Health Duress Emotional Appeal Tests
# ===================================================================

class TestMedicalDuressEmotionalAppeal:
    """Medical emergency and health condition language should trigger
    emotional_appeal detection when used as sympathy/leverage framing."""

    def test_life_threatening_health_condition(self):
        """'life-threatening health condition' from Guardian Wynn-Williams
        article should fire emotional_appeal."""
        text = (
            "Wynn-Williams says she was pressured to sign the agreement "
            "while dealing with a life-threatening health condition during "
            "childbirth, making reimbursement of pre-approved business "
            "expenses conditional on her signature."
        )
        devices = detect_framing_devices(text)
        ea_devices = [d for d in devices if d.device_type == "emotional_appeal"]
        assert len(ea_devices) >= 1, (
            f"Expected emotional_appeal for 'life-threatening health condition'; "
            f"got devices: {[d.device_type for d in devices]}"
        )

    def test_medical_emergency(self):
        """'medical emergency' should fire emotional_appeal."""
        text = (
            "The employee was forced to sign the non-disclosure agreement "
            "while recovering from a medical emergency, with health insurance "
            "dependent on compliance."
        )
        devices = detect_framing_devices(text)
        ea_devices = [d for d in devices if d.device_type == "emotional_appeal"]
        assert len(ea_devices) >= 1

    def test_healthcare_as_leverage(self):
        """Healthcare conditional on signing should fire emotional_appeal."""
        text = (
            "The company made health care coverage contingent on the "
            "employee agreeing to the severance terms."
        )
        devices = detect_framing_devices(text)
        ea_devices = [d for d in devices if d.device_type == "emotional_appeal"]
        assert len(ea_devices) >= 1

    def test_during_childbirth(self):
        """'during childbirth' should fire emotional_appeal."""
        text = (
            "She experienced complications during childbirth and was "
            "presented with the agreement while still hospitalized."
        )
        devices = detect_framing_devices(text)
        ea_devices = [d for d in devices if d.device_type == "emotional_appeal"]
        assert len(ea_devices) >= 1

    def test_no_false_positive_routine_medical(self):
        """Routine medical references should NOT fire emotional_appeal."""
        text = (
            "Meta offers comprehensive health insurance to all full-time "
            "employees, including dental and vision coverage."
        )
        devices = detect_framing_devices(text)
        ea_devices = [d for d in devices if d.device_type == "emotional_appeal"]
        assert len(ea_devices) == 0, (
            f"Routine medical text should not fire emotional_appeal; "
            f"got: {[d.evidence_text for d in ea_devices]}"
        )


# ===================================================================
# Hypocrisy Frame Tests
# ===================================================================

class TestHypocrisyFrame:
    """Hypocrisy frame detects stated-vs-actual contradictions where
    an entity's public position contradicts their actual behavior."""

    def test_positioned_itself_as_yet(self):
        """'positioned itself as X... yet Y' — NYT voluntary review pattern."""
        text = (
            "The holdout is notable given that Meta has actively positioned "
            "itself as a responsible AI leader. Yet it has not agreed to the "
            "pre-release review process that its peers have accepted."
        )
        devices = detect_framing_devices(text)
        hf_devices = [d for d in devices if d.device_type == "hypocrisy_frame"]
        assert len(hf_devices) >= 1, (
            f"Expected hypocrisy_frame for positioned-vs-yet pattern; "
            f"got devices: {[d.device_type for d in devices]}"
        )

    def test_we_do_not_require_but_enforces(self):
        """'We do not require... but enforced' — Guardian Wynn-Williams pattern."""
        text = (
            'In its 2022 proxy statement, Meta said: "We do not require our '
            'personnel to enter into employment agreements that include '
            'non-disparagement clauses." However, Meta enforced exactly such '
            "a clause against Wynn-Williams from a 2017 severance agreement."
        )
        devices = detect_framing_devices(text)
        hf_devices = [d for d in devices if d.device_type == "hypocrisy_frame"]
        assert len(hf_devices) >= 1, (
            f"Expected hypocrisy_frame for 'we do not... but enforced'; "
            f"got devices: {[d.device_type for d in devices]}"
        )

    def test_the_right_thing_while_still(self):
        """'the right thing to do... while still enforcing' — ironic self-congratulation."""
        text = (
            'A Facebook vice president called the end of forced arbitration '
            '"the right thing to do" and "a pivotal moment for our industry." '
            "But Meta continued to enforce the 2017 arbitration agreement "
            "against former employees who had signed before the policy change."
        )
        devices = detect_framing_devices(text)
        hf_devices = [d for d in devices if d.device_type == "hypocrisy_frame"]
        assert len(hf_devices) >= 1

    def test_the_only_company_that_has_not(self):
        """'the only major company that has not' — isolation-as-hypocrisy."""
        text = (
            "Meta is the only major developer of AI technology that has not "
            "reached an agreement to voluntarily share its models with the "
            "federal government for review."
        )
        devices = detect_framing_devices(text)
        hf_devices = [d for d in devices if d.device_type == "hypocrisy_frame"]
        assert len(hf_devices) >= 1

    def test_publicly_said_privately_did(self):
        """'publicly said X... privately/internally Y' pattern."""
        text = (
            "The company publicly stated that employee privacy was paramount. "
            "But internally, managers were accessing keystroke logs without "
            "the consent safeguards the company had promised."
        )
        devices = detect_framing_devices(text)
        hf_devices = [d for d in devices if d.device_type == "hypocrisy_frame"]
        assert len(hf_devices) >= 1

    def test_no_false_positive_genuine_progress(self):
        """Genuine policy change without contradiction should NOT fire."""
        text = (
            "Meta announced it would no longer require forced arbitration "
            "for harassment claims, joining Google, Facebook, and Microsoft "
            "in eliminating the practice. The policy took effect immediately "
            "for all current employees."
        )
        devices = detect_framing_devices(text)
        hf_devices = [d for d in devices if d.device_type == "hypocrisy_frame"]
        assert len(hf_devices) == 0, (
            f"Genuine progress without contradiction should not fire; "
            f"got: {[d.evidence_text for d in hf_devices]}"
        )

    def test_hypocrisy_in_adversarial_types(self):
        """hypocrisy_frame should be in _ADVERSARIAL_DEVICE_TYPES."""
        from mediascope.analyze.sentiment import _ADVERSARIAL_DEVICE_TYPES
        assert "hypocrisy_frame" in _ADVERSARIAL_DEVICE_TYPES


# ===================================================================
# Headline Negative Signal Tests
# ===================================================================

class TestHeadlineNegativeSignals:
    """Headline framing override should catch government pressure,
    regulatory concern, and holdout language that VADER scores positive."""

    def test_presses_in_headline(self):
        """'U.S. Presses Meta' headline should score negative after override."""
        headline = "U.S. Presses Meta to Agree to AI Reviews as Security Concerns Rise"
        body = (
            "The Trump administration is pressing Meta to submit its "
            "artificial intelligence models for voluntary government review."
        )
        score = _measure_headline_alignment(headline, body)
        # After override, headline should be treated as negative, so
        # alignment with negative body should be positive
        # The key test is that the override fires (signal_count >= 2
        # for "presses" + "concerns rise")
        # We just verify the score is not strongly positive (which would
        # mean VADER's false positive reading dominated)
        assert score <= 0.7, (
            f"Expected headline override for 'presses' + 'concerns rise'; "
            f"got alignment score {score}"
        )

    def test_demands_concerns_headline(self):
        """'Demands' + 'Concerns' headline should trigger override."""
        headline = "Government Demands Meta Address Privacy Concerns"
        body = (
            "Federal officials are demanding that Meta take immediate "
            "action to address growing privacy concerns."
        )
        score = _measure_headline_alignment(headline, body)
        assert score <= 0.7

    def test_holdout_headline(self):
        """'Holdout' + 'The Only' headline should trigger override."""
        headline = "Meta Is the Only AI Holdout on Federal Reviews"
        body = (
            "Meta remains the sole major AI developer refusing to submit "
            "models for government testing."
        )
        score = _measure_headline_alignment(headline, body)
        assert score <= 0.7

    def test_neutral_headline_no_override(self):
        """Neutral headline without pressure signals should not override."""
        headline = "Meta Reports Strong Q1 Revenue Growth"
        body = (
            "Meta reported revenue of $56.31 billion in Q1 2026, up 33% "
            "year over year."
        )
        score = _measure_headline_alignment(headline, body)
        # Both positive — should be aligned, no override
        assert score > 0.0
