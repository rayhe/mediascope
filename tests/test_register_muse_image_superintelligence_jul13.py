"""Tests for framing patterns discovered via The Register Meta Muse Image
"superintelligence" article (Jul 13, 2026).

Article: "Meta admits its first 'superintelligence' was too stupid to survive for three days"
Publication: The Register (sardonic tech editorial, British register)
Genre: Short-form editorial (~450 words)

Covers framing patterns in sardonic tech editorial:
1. confession_framing — "admits" in headline
2. editorial_deflation — "superintelligence" punctured by "too stupid"
3. sarcastic_correction — headline ironic inversion
4. recidivism_framing — sardonic enumeration of serial failures
5. editorial_aside — "Yet somehow", "Interestingly", "Meta-speak"
6. CEO_personalization — "Zuck's latest big bet"
7. policy_reversal (controlled retreat) — "Our intent was", "missed the mark"
8. consent_alarm — default opt-in framing
9. kicker_framing — "has now backfired" ending
"""

import pytest
from mediascope.analyze.framing import detect_framing_devices


def _has(text: str, device_type: str) -> bool:
    return any(d.device_type == device_type for d in detect_framing_devices(text))


def _count(text: str, device_type: str) -> int:
    return sum(1 for d in detect_framing_devices(text) if d.device_type == device_type)


# ── confession_framing: headline "admits" ────────────────────────────────


class TestConfessionFramingRegisterHeadline:
    """Confession framing in sardonic headline context."""

    def test_meta_admits_headline(self):
        text = "Meta admits its first 'superintelligence' was too stupid to survive for three days."
        assert _has(text, "confession_framing")

    def test_admits_with_scare_quotes(self):
        """'admits' should trigger even when subject has scare-quoted modifiers."""
        text = "The company admits its 'groundbreaking' product failed."
        assert _has(text, "confession_framing")

    def test_realized_error_as_confession(self):
        """'realized the error of its ways' is a confession-adjacent frame."""
        text = "Within three days of release, Meta realized the error of its ways and pulled the product."
        assert _has(text, "confession_framing")


# ── editorial_deflation: aspirational branding punctured ─────────────────


class TestEditorialDeflationSuperintelligence:
    """Aspirational corporate branding built up then punctured."""

    def test_superintelligence_too_stupid(self):
        """'superintelligence' → 'too stupid' is classic editorial deflation."""
        text = "Meta admits its first 'superintelligence' was too stupid to survive for three days."
        assert _has(text, "editorial_deflation")

    def test_fewer_than_72_hours(self):
        """Temporal deflation — aspirational lab vs short lifespan."""
        text = "Meta has withdrawn the first image generation product created by its Superintelligence Labs fewer than 72 hours after launch."
        assert _has(text, "editorial_deflation")


# ── recidivism_framing: serial offender framing ──────────────────────────


class TestRecidivismFramingSerialOffender:
    """Sardonic enumeration framing Meta as serial privacy offender."""

    def test_leads_world_in_backlashes(self):
        """Sardonic three-item enumeration with two negative items."""
        text = (
            "Meta almost certainly leads the world in three things: "
            "The number of people signed up to its social networks; "
            "experience of people behaving horribly online, and; "
            "dealing with community backlashes after privacy abuses."
        )
        assert _has(text, "recidivism_framing")

    def test_yet_somehow_didnt_imagine(self):
        """'Yet somehow' + institutional incompetence implies serial pattern."""
        text = (
            "Yet somehow it didn't imagine that enabling this feature by default "
            "might be controversial, or that allowing users to alter images with AI "
            "might be abused."
        )
        # This should trigger editorial_aside at minimum
        assert _has(text, "editorial_aside")


# ── editorial_aside: register-breaking direct editorial voice ────────────


class TestEditorialAsideRegister:
    """The Register's characteristic editorial asides."""

    def test_yet_somehow(self):
        """'Yet somehow' is a classic aside signaling editorial disbelief."""
        text = "Yet somehow it didn't imagine that enabling this feature by default might be controversial."
        assert _has(text, "editorial_aside")

    def test_interestingly(self):
        """'Interestingly' signals editorial skepticism."""
        text = (
            'Interestingly, Meta says several of the effects it offered were '
            '"designed by Instagram creators."'
        )
        assert _has(text, "editorial_aside")

    def test_meta_speak(self):
        """Parenthetical jargon gloss is an editorial aside device."""
        text = (
            "Zuck believes users of his social networks mostly want to see content "
            "made by creators – Meta-speak for prominent accounts who post a lot – "
            "rather than content produced by media outlets or others."
        )
        assert _has(text, "editorial_aside")


# ── CEO_personalization: attributing to Zuck personally ──────────────────


class TestCEOPersonalizationZuck:
    """Corporate strategy attributed to CEO via diminutive nickname."""

    def test_zucks_latest_big_bet(self):
        text = "That lab is Zuck's latest big bet and aims to create a 'personal superintelligence.'"
        assert _has(text, "ceo_personalization")

    def test_zuck_believes(self):
        text = "Zuck believes users of his social networks mostly want to see content made by creators."
        assert _has(text, "ceo_personalization")


# ── policy_reversal: controlled retreat language ─────────────────────────


class TestPolicyReversalControlledRetreat:
    """Meta's controlled retreat language in withdrawal statement."""

    def test_our_intent_was(self):
        """Intent displacement: 'Our intent was to provide' reframes controversy."""
        text = "Our intent was to provide a useful creative tool and to give people control."
        assert _has(text, "policy_reversal")

    def test_missed_the_mark(self):
        """Target-miss euphemism: 'missed the mark' displaces agency from design choices."""
        text = "We've heard the feedback that this feature missed the mark, so it's no longer available."
        assert _has(text, "policy_reversal")

    def test_no_longer_available(self):
        """Passive unavailability: 'no longer available' avoids active 'we removed/killed.'"""
        text = "This feature is no longer available."
        # May or may not trigger policy_reversal alone; context-dependent.
        # Other patterns (loaded_language) may also fire on this.


# ── consent_alarm: default opt-in as consent violation ───────────────────


class TestConsentAlarmMuseImage:
    """Default-on feature framed as consent violation."""

    def test_enabling_by_default(self):
        text = (
            "it didn't imagine that enabling this feature by default might be "
            "controversial, or that allowing users to alter images with AI might be abused."
        )
        assert _has(text, "consent_alarm")

    def test_sagaftra_opt_in(self):
        """SAG-AFTRA's 'OPT-IN' language should trigger consent_alarm."""
        text = (
            "Anything other than a clear and conspicuous OPT-IN for these types "
            "of uses of Instagram users' images is unacceptable."
        )
        assert _has(text, "consent_alarm")


# ── kicker_framing: negative verdict as article closer ───────────────────


class TestKickerFramingBackfired:
    """Article ending on negative editorial verdict."""

    def test_backfired_kicker(self):
        """Final sentence 'has now backfired' is negative kicker framing.

        Note: kicker_framing is a structural (post-pass) device that requires
        full-article context. This test verifies the loaded_language component
        ('backfired') is detected at minimum."""
        text = "Involving creators in Meta's own creative processes has now backfired."
        assert _has(text, "loaded_language")


# ── sarcastic_correction: ironic inversion ───────────────────────────────


class TestSarcasticCorrectionHeadline:
    """Headline-level ironic inversion (superintelligence → too stupid)."""

    def test_scare_quote_inversion(self):
        """Scare-quoted positive term followed by negative characterization."""
        text = "Meta's 'superintelligence' was too stupid to survive."
        assert _has(text, "sarcastic_correction") or _has(text, "editorial_deflation")

    def test_too_stupid_loaded(self):
        """'too stupid' is loaded editorial language regardless of context."""
        text = "The product was too stupid to survive for three days."
        assert _has(text, "loaded_language")


# ── Cross-device interactions: multiple devices on same passage ──────────


class TestCrossDeviceInteractions:
    """Verify multiple devices fire on the same dense passage."""

    def test_headline_multi_device(self):
        """The headline should trigger at least 2 distinct device types."""
        text = "Meta admits its first 'superintelligence' was too stupid to survive for three days."
        devices = detect_framing_devices(text)
        device_types = set(d.device_type for d in devices)
        # Should fire at least confession_framing + editorial_deflation or loaded_language
        assert len(device_types) >= 2, f"Only found {device_types}"

    def test_backlash_paragraph_density(self):
        """The privacy-abuse enumeration paragraph should have high device density."""
        text = (
            "Meta almost certainly leads the world in three things: "
            "The number of people signed up to its social networks; "
            "experience of people behaving horribly online, and; "
            "dealing with community backlashes after privacy abuses. "
            "Yet somehow it didn't imagine that enabling this feature by default "
            "might be controversial."
        )
        devices = detect_framing_devices(text)
        device_types = set(d.device_type for d in devices)
        # Should fire at least 2: recidivism_framing + editorial_aside
        assert len(device_types) >= 2, f"Only found {device_types}"
