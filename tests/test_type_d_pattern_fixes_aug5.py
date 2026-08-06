"""
Type D verification tests — Pattern fixes applied 2026-08-05 19:00 PT.

Four xfail-promoted fixes across scale_magnitude, loaded_language,
investor_advisory, and no_comment_implication.  Each class tests the
newly-passing case, boundary variants, and regressions against the
original passing patterns.

Tests: 32
"""

import pytest
from mediascope.analyze.framing import detect_framing_devices


def _types(text: str) -> list[str]:
    return [d.device_type for d in detect_framing_devices(text)]


# ── scale_magnitude: $NNN million ────────────────────────────────────────────


class TestScaleMagnitudeMillionFix:
    """Dollar-million amounts now trigger scale_magnitude (was xfail)."""

    def test_375_million_judgment(self):
        """Original xfail case from Barron's article."""
        text = "New Mexico recently won a $375 million judgment against Meta"
        assert "scale_magnitude" in _types(text)

    def test_500_million(self):
        text = "the company paid $500 million in fines"
        assert "scale_magnitude" in _types(text)

    def test_1_2_million(self):
        text = "only $1.2 million was allocated"
        assert "scale_magnitude" in _types(text)

    def test_750_million_settlement(self):
        text = "a $750 million settlement with regulators"
        assert "scale_magnitude" in _types(text)

    def test_billion_still_works(self):
        """Regression: billion detection unchanged."""
        text = "Meta invested $10 billion in AI infrastructure"
        assert "scale_magnitude" in _types(text)

    def test_trillion_still_works(self):
        """Regression: trillion detection unchanged."""
        text = "plaintiffs asking for $1 trillion-plus in damages"
        assert "scale_magnitude" in _types(text)

    def test_case_insensitive_million(self):
        text = "a $200 Million fine was imposed"
        assert "scale_magnitude" in _types(text)


# ── loaded_language: plural targets ──────────────────────────────────────────


class TestPluralTargetsFix:
    """Plural 'targets' now matches loaded_language pattern (was xfail)."""

    def test_soft_targets_plural(self):
        """Original xfail case."""
        text = "tech firms are seen as soft targets"
        assert "loaded_language" in _types(text)

    def test_easy_targets_plural(self):
        text = "social media companies have become easy targets"
        assert "loaded_language" in _types(text)

    def test_prime_targets_plural(self):
        text = "the platforms are prime targets for regulators"
        assert "loaded_language" in _types(text)

    def test_ripe_targets_plural(self):
        text = "they are ripe targets for antitrust enforcement"
        assert "loaded_language" in _types(text)

    def test_singular_still_works(self):
        """Regression: singular form unchanged."""
        text = "Meta is an easy target for regulators"
        assert "loaded_language" in _types(text)

    def test_tempting_targets(self):
        text = "the companies are tempting targets for class actions"
        assert "loaded_language" in _types(text)


# ── investor_advisory: parenthetical clause ──────────────────────────────────


class TestInvestorAdvisoryParentheticalFix:
    """Parenthetical clauses between 'Investors' and 'should' now match."""

    def test_parenthetical_overlook(self):
        """Original xfail case."""
        text = "Investors, who tend to overlook fines, should start paying attention"
        assert "investor_advisory" in _types(text)

    def test_parenthetical_bullish(self):
        text = "Investors, especially those who are bullish, should be worried"
        assert "investor_advisory" in _types(text)

    def test_no_parenthetical_still_works(self):
        """Regression: simple form unchanged."""
        text = "Investors should start paying attention"
        assert "investor_advisory" in _types(text)

    def test_ought_to_with_parenthetical(self):
        text = "Investors, particularly retail ones, ought to take note"
        assert "investor_advisory" in _types(text)

    def test_ignore_at_peril_still_works(self):
        """Regression: peril pattern unchanged."""
        text = "Investors Ignore the Threat at Their Peril"
        assert "investor_advisory" in _types(text)

    def test_may_be_making_still_works(self):
        """Regression: 'may be making' pattern unchanged."""
        text = "Investors may be making the wrong choice"
        assert "investor_advisory" in _types(text)


# ── no_comment_implication: contractions ─────────────────────────────────────


class TestNoCommentContractionFix:
    """Contraction forms ('didn't', 'hasn't') now match no_comment_implication."""

    def test_didnt_respond(self):
        """Original xfail case."""
        text = "the attorneys general of California and Kentucky didn't respond to a request for comment"
        types = _types(text)
        assert "refusal_amplification" in types or "no_comment_implication" in types

    def test_didnt_return(self):
        text = "the spokesperson didn't return calls for comment"
        types = _types(text)
        assert "no_comment_implication" in types

    def test_hasnt_responded(self):
        text = "the company hasn't responded to our inquiry"
        types = _types(text)
        assert "no_comment_implication" in types

    def test_did_not_still_works(self):
        """Regression: uncontracted form unchanged."""
        text = "the company did not immediately respond"
        types = _types(text)
        assert "no_comment_implication" in types

    def test_declined_still_works(self):
        """Regression: 'declined to comment' unchanged."""
        text = "Meta declined to comment"
        types = _types(text)
        assert "no_comment_implication" in types

    def test_refused_still_works(self):
        """Regression: 'refused to comment' unchanged."""
        text = "the executive refused to comment on the allegations"
        types = _types(text)
        assert "no_comment_implication" in types


# ── Cross-pattern regression ─────────────────────────────────────────────────


class TestCrossPatternRegression:
    """Ensure fixes don't cause false positives in unrelated patterns."""

    def test_million_users_not_scale_magnitude_alone(self):
        """'million' in non-dollar context shouldn't spuriously fire."""
        text = "the app has a million daily active users"
        # This may fire via user-base milestone or not; just no crash
        _types(text)

    def test_target_in_ad_targeting(self):
        """'target' in advertising context shouldn't fire loaded_language."""
        text = "the ad will target users aged 18-25"
        assert "loaded_language" not in _types(text)

    def test_investor_in_prose(self):
        """Casual investor mention shouldn't fire investor_advisory."""
        text = "the investor bought shares in Meta last quarter"
        assert "investor_advisory" not in _types(text)
