"""Tests for patterns and entities verified in the Barron's "$1 Trillion
Backlash" child safety litigation article deep dive (Jul 15, 2026).

Covers:
- Entity detection: Meta, Facebook, Instagram, Alphabet/YouTube, TikTok,
  Snap, Roblox (new cluster), State Attorneys General
- Framing: scale_magnitude for "$1.4 trillion" and "13-figure penalty" (new),
  loaded_language for "ripe target" (new) and "Backlash",
  investor_advisory, catastrophizing ("avalanche"),
  pathologizing_metaphor ("addicted"), emotional_appeal,
  refusal_amplification / no_comment_implication
- Sentiment: negative overall tone for litigation-warning coverage

Article: "Facebook Faces a $1 Trillion Backlash. Investors Ignore the
Threat at Their Peril." — Adam Levine, Barron's, July 10, 2026
"""

import pytest
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.entities import detect_entities


def _types(text: str) -> set[str]:
    """Return the set of device_type strings detected in *text*."""
    return {d.device_type for d in detect_framing_devices(text)}


def _entity_names(text: str) -> set[str]:
    """Return set of cluster names from detected entities."""
    return {e.cluster for e in detect_entities(text)}


# ── Entity Detection ────────────────────────────────────────────────────────


class TestEntityDetection:
    """Core entities from the Barron's $1T backlash article."""

    def test_meta_detected(self):
        text = "Meta Platforms, home of Facebook and Instagram"
        names = _entity_names(text)
        assert "Meta" in names

    def test_alphabet_youtube_detected(self):
        text = "went against Meta and Alphabet's YouTube in March"
        names = _entity_names(text)
        assert "Google" in names  # Alphabet/YouTube → Google cluster

    def test_tiktok_detected(self):
        text = "YouTube and TikTok have already settled"
        assert "TikTok" in _entity_names(text)

    def test_snap_detected(self):
        text = "leaving Meta and Snap as the remaining defendants"
        assert "Snap" in _entity_names(text)

    def test_roblox_detected(self):
        """Roblox cluster added in this iteration."""
        text = "Roblox is the one major company trying to get in front of the risks"
        assert "Roblox" in _entity_names(text)

    def test_roblox_corporation_detected(self):
        text = "Roblox Corporation announced new safety measures"
        assert "Roblox" in _entity_names(text)

    def test_david_baszucki_detected(self):
        text = "CEO David Baszucki outlined a new age verification process"
        assert "Roblox" in _entity_names(text)


# ── scale_magnitude ─────────────────────────────────────────────────────────


class TestScaleMagnitude:
    """Dollar figures and magnitude expressions should fire scale_magnitude."""

    def test_1_4_trillion(self):
        text = "asking the court for $1.4 trillion"
        assert "scale_magnitude" in _types(text)

    def test_1_trillion_plus(self):
        text = "plaintiffs asking for $1 trillion-plus in damages"
        assert "scale_magnitude" in _types(text)

    @pytest.mark.xfail(reason="$NNN million not yet detected as scale_magnitude")
    def test_375_million(self):
        text = "New Mexico recently won a $375 million judgment against Meta"
        assert "scale_magnitude" in _types(text)

    def test_13_figure_penalty(self):
        """N-figure magnitude idiom added in this iteration."""
        text = "a loss at trial doesn't come with a 13-figure penalty"
        assert "scale_magnitude" in _types(text)

    def test_nine_figure_settlement(self):
        """Generalized N-figure pattern."""
        text = "the company faces a nine-figure settlement"
        assert "scale_magnitude" in _types(text)

    def test_10_figure_damages(self):
        text = "potential 10-figure damages"
        assert "scale_magnitude" in _types(text)

    def test_seven_figure_fine(self):
        text = "a seven-figure fine for the violation"
        assert "scale_magnitude" in _types(text)


# ── loaded_language ──────────────────────────────────────────────────────────


class TestLoadedLanguageRipeTarget:
    """'ripe target' and variants should fire loaded_language."""

    def test_ripe_target(self):
        """Exact phrase from the article."""
        text = "see Meta and other social-media companies as a ripe target"
        assert "loaded_language" in _types(text)

    def test_easy_target(self):
        text = "social media companies have become an easy target for regulators"
        assert "loaded_language" in _types(text)

    @pytest.mark.xfail(reason="plural 'soft targets' not matched by singular pattern")
    def test_soft_target(self):
        text = "tech firms are seen as soft targets"
        assert "loaded_language" in _types(text)

    def test_prime_target(self):
        text = "the company is a prime target for antitrust enforcement"
        assert "loaded_language" in _types(text)

    def test_backlash_loaded(self):
        text = "Facebook Faces a $1 Trillion Backlash"
        assert "loaded_language" in _types(text)

    def test_deceptive_practices(self):
        text = "penalties against such deceptive practices"
        assert "loaded_language" in _types(text)


# ── investor_advisory ────────────────────────────────────────────────────────


class TestInvestorAdvisory:
    """Investor-directed framing should fire investor_advisory."""

    def test_investors_ignore_at_peril(self):
        text = "Investors Ignore the Threat at Their Peril"
        assert "investor_advisory" in _types(text)

    @pytest.mark.xfail(reason="long parenthetical clause between 'Investors' and 'should' breaks pattern")
    def test_investors_should_pay_attention(self):
        text = "Investors, who tend to overlook fines, should start paying attention"
        assert "investor_advisory" in _types(text)

    def test_investors_wrong_choice(self):
        text = "Investors may be making the wrong choice"
        assert "investor_advisory" in _types(text)


# ── catastrophizing ──────────────────────────────────────────────────────────


class TestCatastrophizing:
    """Extreme-outcome language should fire catastrophizing."""

    def test_avalanche(self):
        text = "Another loss could lead to an avalanche of settlements"
        assert "catastrophizing" in _types(text)


# ── pathologizing_metaphor ───────────────────────────────────────────────────


class TestPathologizingMetaphor:
    """Addiction framing should fire pathologizing_metaphor."""

    def test_addicted_to_social_media(self):
        text = "she became addicted to social media as a child"
        assert "pathologizing_metaphor" in _types(text)


# ── emotional_appeal ─────────────────────────────────────────────────────────


class TestEmotionalAppeal:
    """Child safety / mental health references should fire emotional_appeal."""

    def test_mental_health(self):
        text = "harming her mental health and opening her up to abuse"
        assert "emotional_appeal" in _types(text)


# ── refusal_amplification / no_comment_implication ───────────────────────────


class TestRefusalAmplification:
    """Declining to comment should fire refusal_amplification or
    no_comment_implication."""

    def test_declined_to_comment(self):
        text = "The attorneys general offices of New Jersey and Colorado declined to comment"
        types = _types(text)
        assert "refusal_amplification" in types or "no_comment_implication" in types

    @pytest.mark.xfail(reason="'didn't respond to a request for comment' not detected — pattern expects 'declined/refused'")
    def test_didnt_respond(self):
        text = "the attorneys general of California and Kentucky didn't respond to a request for comment"
        types = _types(text)
        assert "refusal_amplification" in types or "no_comment_implication" in types
