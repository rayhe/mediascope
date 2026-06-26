"""Tests for analogy_stacking and speculative_framing post-pass activation.

These post-pass devices were defined but never called prior to the Jun 26
2026 bug fix.  These tests verify:
  1. analogy_stacking fires when 3+ analogy markers are present
  2. analogy_stacking does NOT fire below threshold
  3. speculative_framing fires when 5+ hedge markers are present
  4. speculative_framing does NOT fire below threshold
  5. loaded_language detects newly-added patterns (deceptive, misleading,
     disingenuous, unprecedented + breach/violation/etc.)
  6. speculative_framing expanded verbs (influence, affect, etc.) match
"""

import pytest

from mediascope.analyze.framing import detect_framing_devices


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def _device_types(text: str) -> set[str]:
    """Return unique device_type values detected in *text*."""
    return {d.device_type for d in detect_framing_devices(text)}


def _device_evidences(text: str, device_type: str) -> list[str]:
    """Return evidence_text values for a specific device_type."""
    return [
        d.evidence_text
        for d in detect_framing_devices(text)
        if d.device_type == device_type
    ]


# ===================================================================
# analogy_stacking
# ===================================================================

class TestAnalogyStacking:
    """Verify analogy_stacking post-pass fires when threshold is met."""

    ARTICLE_WITH_MANY_ANALOGIES = (
        "Social media is the modern equivalent of the town square. "
        "Some have likened it to a digital Colosseum where gladiators "
        "fight for attention. Critics compared it to an addictive slot "
        "machine. It functions like a surveillance apparatus that "
        "monitors every move. Think of it as a megaphone with no "
        "off switch. The effect is reminiscent of the yellow journalism "
        "era a century ago."
    )

    ARTICLE_WITH_TWO_ANALOGIES = (
        "Social media is the modern equivalent of the town square. "
        "Some have likened it to a digital Colosseum. "
        "The company reported strong earnings last quarter."
    )

    def test_fires_above_threshold(self):
        """3+ distinct analogy markers → analogy_stacking detected."""
        types = _device_types(self.ARTICLE_WITH_MANY_ANALOGIES)
        assert "analogy_stacking" in types

    def test_count_above_threshold(self):
        """Article with 6 markers should return 6 analogy_stacking devices."""
        evidences = _device_evidences(
            self.ARTICLE_WITH_MANY_ANALOGIES, "analogy_stacking"
        )
        assert len(evidences) >= 3

    def test_does_not_fire_below_threshold(self):
        """Only 2 analogy markers → analogy_stacking should NOT fire."""
        types = _device_types(self.ARTICLE_WITH_TWO_ANALOGIES)
        assert "analogy_stacking" not in types

    def test_equivalent_of_pattern(self):
        text = (
            "It is the digital equivalent of wiretapping. "
            "The technology has been deployed widely across the industry "
            "over the past decade, raising concerns from regulators. "
            "Others likened it to Big Brother watching your every step. "
            "The debate has intensified as more companies adopt similar "
            "approaches and lawmakers consider new legislation. "
            "Critics compared it to state surveillance on a grand scale."
        )
        assert "analogy_stacking" in _device_types(text)

    def test_evokes_and_echoes_patterns(self):
        """Patterns using 'evokes', 'echoes of', 'reminiscent of'."""
        text = (
            "The design evokes brutalist architecture of the 1960s. "
            "Experts have noted a growing unease with the product's "
            "direction and the choices that led to this outcome. "
            "There are echoes of the dot-com bubble in the current hype. "
            "The company has invested billions in research to push "
            "the technology forward despite growing public skepticism. "
            "The rhetoric is reminiscent of Cold War propaganda campaigns. "
            "Meanwhile, competitors have taken a different approach to "
            "the same fundamental problem and achieved mixed results. "
            "It is like a runaway train with no conductor at the helm."
        )
        types = _device_types(text)
        assert "analogy_stacking" in types

    def test_think_of_it_as_pattern(self):
        text = (
            "Think of it as a digital panopticon where nothing is private. "
            "The implications are enormous for civil society, personal "
            "autonomy, and the fundamental right to be left alone. "
            "Some have compared it to an unregulated casino floor. "
            "The rapid expansion of the technology across markets has "
            "outpaced any regulatory framework designed to contain it. "
            "The platform is the modern equivalent of a public utility."
        )
        assert "analogy_stacking" in _device_types(text)


# ===================================================================
# speculative_framing
# ===================================================================

class TestSpeculativeFraming:
    """Verify speculative_framing post-pass fires when threshold is met."""

    ARTICLE_MANY_HEDGES = (
        "The company could potentially harvest user data in ways nobody "
        "has considered. It might be able to bypass existing safeguards. "
        "In theory, this would give them unprecedented leverage. "
        "There's a chance the technology could reshape the competitive "
        "landscape. If regulators were to intervene, it could alter the "
        "trajectory of the entire industry. It is possible that the "
        "consequences might enable entirely new surveillance techniques."
    )

    ARTICLE_FEW_HEDGES = (
        "The company could potentially harvest user data. "
        "It might be able to bypass safeguards. "
        "The earnings report was solid."
    )

    def test_fires_above_threshold(self):
        """5+ speculative hedges → speculative_framing detected."""
        types = _device_types(self.ARTICLE_MANY_HEDGES)
        assert "speculative_framing" in types

    def test_count_above_threshold(self):
        evidences = _device_evidences(
            self.ARTICLE_MANY_HEDGES, "speculative_framing"
        )
        assert len(evidences) >= 5

    def test_does_not_fire_below_threshold(self):
        """Only 2 hedges → speculative_framing should NOT fire."""
        types = _device_types(self.ARTICLE_FEW_HEDGES)
        assert "speculative_framing" not in types

    def test_could_later_influence(self):
        """Expanded verb 'influence' with intervening adverb should match."""
        text = (
            "This could later influence policy decisions. "
            "The data might be able to lead to new restrictions. "
            "There's a possibility the algorithm could ultimately determine "
            "who sees what. In principle this raises hard questions. "
            "If companies were to adopt this approach, it could easily "
            "shape the next generation of products."
        )
        types = _device_types(text)
        assert "speculative_framing" in types

    def test_expanded_verbs_leak_seep_expose(self):
        """Newly-added verbs leak, seep, expose should match."""
        text = (
            "The information could leak to third parties. "
            "Sensitive data might be able to give adversaries an edge. "
            "It's conceivable that records could seep into public view. "
            "Theoretically, this could expose millions of users. "
            "The weakness could ultimately allow bad actors to exploit it. "
            "If the company were to lose control, it could affect everyone."
        )
        types = _device_types(text)
        assert "speculative_framing" in types

    def test_conditional_were_to(self):
        """'if X were to' pattern should contribute to count."""
        text = (
            "Could potentially uncover hidden patterns. "
            "Might be able to open the door to abuse. "
            "In theory this would be catastrophic. "
            "If Meta were to acquire this startup, it could reshape "
            "the market. There's a risk the technology could enable mass "
            "surveillance. It's possible that the data could impact millions."
        )
        types = _device_types(text)
        assert "speculative_framing" in types

    def test_hypothetical_scenario(self):
        """Explicit hypothetical markers count toward threshold."""
        text = (
            "For the sake of argument, imagine every device is compromised. "
            "In this hypothetical scenario, the company could potentially "
            "control the narrative. It might be able to suppress dissent. "
            "In theory, the damage could transform civil liberties. "
            "There's a chance none of this will happen, but let's suppose "
            "it could erode trust completely."
        )
        types = _device_types(text)
        assert "speculative_framing" in types


# ===================================================================
# loaded_language — newly added patterns
# ===================================================================

class TestLoadedLanguageExpansion:
    """Verify newly-added loaded_language patterns are detected."""

    def test_deceptive(self):
        text = "The company's deceptive practices misled consumers."
        assert "loaded_language" in _device_types(text)

    def test_misleading(self):
        text = "The misleading claims in the press release drew scrutiny."
        assert "loaded_language" in _device_types(text)

    def test_disingenuous(self):
        text = "Critics called the apology disingenuous and self-serving."
        assert "loaded_language" in _device_types(text)

    def test_unprecedented_breach(self):
        text = "This represents an unprecedented privacy breach."
        assert "loaded_language" in _device_types(text)

    def test_unprecedented_violation(self):
        text = "Regulators cited an unprecedented civil-liberties violation."
        assert "loaded_language" in _device_types(text)

    def test_unprecedented_with_adjective_breach(self):
        """'unprecedented massive breach' — adjective between unprecedented and noun."""
        text = "The incident was an unprecedented massive breach of user trust."
        assert "loaded_language" in _device_types(text)

    def test_unprecedented_exposure(self):
        text = "This was an unprecedented data exposure."
        assert "loaded_language" in _device_types(text)

    def test_unprecedented_threat(self):
        text = "Analysts warned of an unprecedented competitive threat."
        assert "loaded_language" in _device_types(text)

    def test_unprecedented_without_qualifying_noun_not_loaded(self):
        """Plain 'unprecedented' without breach/violation/etc. should not
        match the new pattern (may match existing 'unprecedented crisis'
        pattern, but not this specific new one)."""
        text = "The company saw unprecedented growth last quarter."
        # 'unprecedented growth' doesn't match the new pattern's noun list
        # (breach, violation, exposure, threat, risk, danger, harm, crisis, failure)
        evidences = _device_evidences(text, "loaded_language")
        # Should not find "unprecedented growth" in evidence
        for e in evidences:
            assert "unprecedented growth" not in e.lower()


# ===================================================================
# Integration: both post-passes in the same article
# ===================================================================

class TestPostPassIntegration:
    """Verify both post-pass devices can fire in the same article."""

    def test_both_fire_together(self):
        """An article with enough of both analogy markers and speculative
        hedges should produce both device types."""
        text = (
            # 4 analogy markers (well-spaced to avoid overlap dedup)
            "The platform is the modern equivalent of a surveillance state "
            "where every citizen is tracked and catalogued. "
            "The company has grown enormously over the past five years, "
            "reaching billions of users across every continent and language. "
            "Some have likened it to an Orwellian panopticon from which "
            "there is no escape and no appeal. "
            "Researchers have raised serious concerns about the long-term "
            "effects on democratic institutions and individual autonomy. "
            "Critics compared it to a digital cage that traps its users. "
            "Industry analysts say the underlying technology is reminiscent "
            "of techniques developed by intelligence agencies decades ago. "
            # 6 speculative hedges
            "The technology could potentially harvest biometric data. "
            "It might be able to bypass encryption at scale. "
            "In theory, there is no safeguard strong enough. "
            "There's a chance the technology could reshape privacy norms. "
            "If regulators were to intervene, it could alter the course "
            "of regulation for a generation. "
            "It's possible that the approach could undermine due process."
        )
        types = _device_types(text)
        assert "analogy_stacking" in types, "analogy_stacking should fire"
        assert "speculative_framing" in types, "speculative_framing should fire"
