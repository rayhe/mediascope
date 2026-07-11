"""Tests for ultimatum_framing (#96) framing device.

Discovered from NY Post "European Union warns Meta to change 'addictive'
Facebook, Instagram features — or get big fines" (Jul 10, 2026).
"""

import pytest
from mediascope.analyze.framing import detect_framing_devices


def _has_device(text: str, device_type: str = "ultimatum_framing") -> bool:
    """Return True if *device_type* fires on *text*."""
    devices = detect_framing_devices(text)
    return any(d.device_type == device_type for d in devices)


def _device_count(text: str, device_type: str = "ultimatum_framing") -> int:
    """Return the number of *device_type* matches in *text*."""
    devices = detect_framing_devices(text)
    return sum(1 for d in devices if d.device_type == device_type)


# ── Positive cases ─────────────────────────────────────────────────────────


class TestEmDashOrConstruction:
    """The canonical pattern: "change X — or get/face Y"."""

    def test_nypost_headline(self):
        """NY Post EU DSA headline — the discovery article."""
        text = (
            "European Union warns Meta to change 'addictive' Facebook, "
            "Instagram features — or get big fines"
        )
        assert _has_device(text)

    def test_em_dash_face(self):
        text = "The regulator told the company to fix the privacy violations — or face massive penalties."
        assert _has_device(text)

    def test_en_dash_variant(self):
        text = "They must stop collecting data from minors – or risk litigation."
        assert _has_device(text)

    def test_double_dash_variant(self):
        text = "Remove the addictive features -- or suffer the consequences."
        assert _has_device(text)

    def test_overhaul_variant(self):
        text = "Overhaul the recommendation algorithm — or face regulatory action."
        assert _has_device(text)


class TestMustOrFace:
    """Regulatory imperative: "must [action] or face [consequence]"."""

    def test_must_change_or_face(self):
        text = "Meta must change its advertising practices or face fines of up to 6% of global revenue."
        assert _has_device(text)

    def test_has_to_comply_or_risk(self):
        text = "The company has to comply with the new rules or risk being shut out of the EU market."
        assert _has_device(text)

    def test_needs_to_act_or_face(self):
        text = "The platform needs to act on the commission's findings or face escalating penalties."
        assert _has_device(text)


class TestComplyOrFace:
    """Direct regulatory ultimatum: "comply or [consequence]"."""

    def test_comply_or_face_fines(self):
        text = "Tech companies must comply with the Digital Services Act or face fines."
        assert _has_device(text)

    def test_comply_or_be_sanctioned(self):
        text = "Platforms that fail to comply with the new rules or be sanctioned by the commission."
        assert _has_device(text)


class TestDeadlineUltimatum:
    """Deadline + consequence: "by [deadline] or [consequence]"."""

    def test_by_march_or_face(self):
        text = "The company must act by March 2027 or face fines of billions of euros."
        assert _has_device(text)

    def test_within_six_months_or_face(self):
        text = "Platforms have within six months or face penalties from the commission."
        assert _has_device(text)


class TestEitherOrConstruction:
    """Explicit binary: "either [action] or [consequence]"."""

    def test_either_fix_or_face(self):
        text = "Meta can either fix its algorithmic recommendations or face further regulatory scrutiny."
        assert _has_device(text)

    def test_either_comply_or_pay(self):
        text = "The company must either comply with the requirements or pay substantial fines."
        assert _has_device(text)


# ── Negative cases ─────────────────────────────────────────────────────────


class TestNegativeCases:
    """Text that should NOT trigger ultimatum_framing."""

    def test_neutral_or_clause(self):
        """Ordinary 'or' with no regulatory ultimatum structure."""
        text = "Users can choose to share their data or keep it private."
        assert not _has_device(text)

    def test_soft_risk_language(self):
        """Risk language without the imperative+consequence structure."""
        text = "The company faces risks from regulatory changes."
        assert not _has_device(text)

    def test_regulatory_shadow_not_ultimatum(self):
        """Ambient regulatory fear, not a binary ultimatum."""
        text = "Regulatory uncertainty continues to weigh on Meta's stock price."
        assert not _has_device(text)

    def test_pressure_language_not_ultimatum(self):
        """Coercive verbs without the binary construction."""
        text = "Regulators are pressing Meta to improve its content moderation."
        assert not _has_device(text)

    def test_business_choice_not_ultimatum(self):
        """Business decisions framed as choices, not regulatory demands."""
        text = "The company could either expand into new markets or focus on profitability."
        assert not _has_device(text)

    def test_simple_conditional(self):
        """Simple if-then, not an ultimatum construction."""
        text = "If Meta does not comply, it could face penalties."
        assert not _has_device(text)


# ── Cross-device differentiation ───────────────────────────────────────────


class TestCrossDeviceDifferentiation:
    """Ensure ultimatum_framing doesn't overlap with adjacent devices."""

    def test_regulatory_shadow_only(self):
        """Should fire regulatory_shadow, NOT ultimatum_framing."""
        text = "The specter of regulation looms over the tech industry."
        assert not _has_device(text, "ultimatum_framing")

    def test_nypost_headline_not_pressure_language_only(self):
        """The NY Post headline should fire ultimatum_framing specifically."""
        text = (
            "European Union warns Meta to change 'addictive' Facebook, "
            "Instagram features — or get big fines"
        )
        assert _has_device(text, "ultimatum_framing")


# ── Signal level / genre awareness ─────────────────────────────────────────


class TestReliabilityVariants:
    """Cross-publication comparisons: same event, different framings."""

    def test_reuters_softer_variant(self):
        """Reuters 'or risk fines' — softer but still matches the pattern."""
        text = "EU tells Instagram, Facebook to change how they deal with minors or risk fines."
        assert _has_device(text)

    def test_cnn_hedged_no_ultimatum(self):
        """CNN 'may violate' — hedged possibility, not an ultimatum."""
        text = "Meta's practices may violate European law designed to protect minors."
        assert not _has_device(text)

    def test_wsj_failure_attribution_no_ultimatum(self):
        """WSJ 'failed to protect' — failure attribution, not ultimatum."""
        text = "Meta Failed to Protect Users From Instagram's Addictive Design, EU Says."
        assert not _has_device(text)
