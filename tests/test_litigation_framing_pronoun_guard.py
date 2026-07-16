"""Test litigation_framing pronoun guard — colloquial "sue me" suppression.

Discovered via Atlantic emotion-AI workplace surveillance article (May 2026):
  "sue me — occasionally impatient" (Cushing's humor, not litigation framing).

The suing pattern used re.IGNORECASE, which made [A-Z]\\w+ match lowercase
pronouns like "me", "him", "us". A negative lookahead for personal pronouns
now prevents colloquial "sue me/him/us" from triggering litigation_framing
while preserving detection of genuine legal constructions like "sued Meta"
or "suing the Federal Trade Commission".

Fix committed 2026-07-16 (Type D iteration).
"""

import pytest
from mediascope.analyze.framing import detect_framing_devices


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _has_litigation_framing(text: str) -> bool:
    """Return True if any litigation_framing device fires on *text*."""
    devices = detect_framing_devices(text)
    return any(d.device_type == "litigation_framing" for d in devices)


def _litigation_framing_count(text: str) -> int:
    """Return count of litigation_framing devices fired on *text*."""
    devices = detect_framing_devices(text)
    return sum(1 for d in devices if d.device_type == "litigation_framing")


# ---------------------------------------------------------------------------
# Part 1: Colloquial "sue me" must NOT trigger litigation_framing
# ---------------------------------------------------------------------------

class TestColloquialSueMeSuppression:
    """Colloquial/idiomatic uses of 'sue' with pronoun objects."""

    def test_sue_me_dash_essay_prose(self):
        """Atlantic-style essay humor: 'sue me — occasionally impatient'."""
        text = (
            "The computer thinks I have a nice personality — attentive, "
            "calm, empathetic. Also occasionally impatient, though — sue "
            "me — and showing traces of anxiety."
        )
        assert not _has_litigation_framing(text)

    def test_sue_me_colloquial_standalone(self):
        """Standalone 'sue me' as casual dismissal."""
        text = "I prefer the old design. Sue me."
        assert not _has_litigation_framing(text)

    def test_so_sue_me(self):
        """'So sue me' idiom."""
        text = "So sue me if I think that's a terrible idea."
        assert not _has_litigation_framing(text)

    def test_sue_me_for_gerund(self):
        """'Sue me for [gerund]' — casual deflection."""
        text = "Sure, sue me for thinking regulation might help."
        assert not _has_litigation_framing(text)

    def test_sued_him_colloquial(self):
        """Pronoun object 'him' — not a named legal target."""
        text = "They sued him personally but the case went nowhere."
        assert not _has_litigation_framing(text)

    def test_sue_us(self):
        """Pronoun object 'us'."""
        text = "Go ahead and sue us if you don't like it."
        assert not _has_litigation_framing(text)

    def test_sue_them(self):
        """Pronoun object 'them'."""
        text = "Nobody bothered to sue them over the breach."
        assert not _has_litigation_framing(text)

    def test_suing_her(self):
        """Pronoun object 'her'."""
        text = "The company considered suing her but dropped it."
        assert not _has_litigation_framing(text)

    def test_sue_yourself(self):
        """Reflexive pronoun."""
        text = "You can't exactly sue yourself."
        assert not _has_litigation_framing(text)


# ---------------------------------------------------------------------------
# Part 2: Genuine litigation framing MUST still trigger
# ---------------------------------------------------------------------------

class TestGenuineLitigationFramingPreserved:
    """Real litigation framing with named entities must still detect."""

    def test_sued_named_company(self):
        """Standard legal reporting: 'Facebook sued Apple'."""
        text = "Facebook sued Apple over app store fees last October."
        assert _has_litigation_framing(text)

    def test_suing_named_entity(self):
        """'Is suing Meta' — active litigation."""
        text = "The FTC is suing Meta over antitrust violations."
        assert _has_litigation_framing(text)

    def test_sues_named_entity(self):
        """Present tense: 'Meta sues Apple'."""
        text = "Meta sues Apple over fees in new court filing."
        assert _has_litigation_framing(text)

    def test_sued_the_government(self):
        """'sued the Federal Trade Commission' — the-prefixed entity."""
        text = "Amazon has sued the Federal Trade Commission."
        assert _has_litigation_framing(text)

    def test_filed_lawsuit(self):
        """'filed a lawsuit' — other litigation pattern."""
        text = "Thirty states filed a lawsuit against Meta."
        assert _has_litigation_framing(text)

    def test_seeking_legal_action(self):
        """'seeking legal action' pattern."""
        text = "Consumer groups are seeking legal action against the platform."
        assert _has_litigation_framing(text)

    def test_took_to_court(self):
        """'took Meta to court' — idiomatic but genuine."""
        text = "The plaintiff took Meta to court over privacy violations."
        assert _has_litigation_framing(text)

    def test_lawsuit_lodged_against(self):
        """Reversed construction: 'lawsuit lodged against'."""
        text = "A lawsuit lodged against Meta Platforms accuses the company of discrimination."
        assert _has_litigation_framing(text)

    def test_arbitration_ruling(self):
        """Legal mechanism framing: 'arbitration ruling'."""
        text = "The arbitration ruling went against the company."
        assert _has_litigation_framing(text)

    def test_legal_challenge_against(self):
        """'legal challenge against' — adversarial preposition."""
        text = "The legal challenge against Google could reshape the industry."
        assert _has_litigation_framing(text)


# ---------------------------------------------------------------------------
# Part 3: Edge cases — mixed contexts
# ---------------------------------------------------------------------------

class TestLitigationFramingEdgeCases:
    """Boundary cases where context determines whether it's genuine."""

    def test_sue_me_plus_real_litigation_same_article(self):
        """Article with both colloquial 'sue me' AND real litigation.

        The colloquial use should not fire, but the real one should.
        """
        text = (
            "Sure, sue me for being skeptical. But Meta actually filed "
            "a lawsuit against the FTC last month, and the legal challenge "
            "against the agency could reshape oversight."
        )
        devices = detect_framing_devices(text)
        lit_devices = [d for d in devices if d.device_type == "litigation_framing"]
        # Should have at least one device from the real litigation language
        assert len(lit_devices) >= 1
        # None of the matches should contain "sue me"
        for d in lit_devices:
            assert "sue me" not in d.evidence_text.lower()

    def test_capitalized_sue_me_still_blocked(self):
        """'Sue Me' at start of sentence — still colloquial."""
        text = "Sue me for caring about data privacy."
        assert not _has_litigation_framing(text)
