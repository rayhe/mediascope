"""Tests for the strategic_disclosure framing device.

Validates that the toolkit correctly detects party-originated strategic
disclosure of unfavorable figures/demands, and correctly rejects editorial
magnitude language that isn't party-strategic.

Also tests the expert_consensus_authority (?-i:) fix for the [A-Z]{2,5}
IGNORECASE false-positive bug (discovered in same Reuters article).
"""

import re
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mediascope.analyze.framing import (
    _STRATEGIC_DISCLOSURE_PATTERNS,
    _EXPERT_CONSENSUS_PATTERNS,
)


# ---------------------------------------------------------------------------
# strategic_disclosure: true positives
# ---------------------------------------------------------------------------

class TestStrategicDisclosureTruePositives:
    """Sentences where a party strategically discloses an opponent's demand."""

    def _matches(self, text: str) -> bool:
        return any(p.search(text) for p in _STRATEGIC_DISCLOSURE_PATTERNS)

    def test_meta_put_forward_figure(self):
        assert self._matches(
            "Meta put forward the figure in its response to the "
            "attorneys general's filings on how penalties should be calculated."
        )

    def test_meta_said_amount_unsupported(self):
        assert self._matches(
            "Meta said the amount was unsupported by the evidence."
        )

    def test_has_no_analog(self):
        assert self._matches(
            "A sanction of that size has no analog in the history of "
            "consumer protection enforcement."
        )

    def test_company_disclosed_penalty(self):
        assert self._matches(
            "Google disclosed the figure in a securities filing late Friday."
        )

    def test_described_demand_as_excessive(self):
        assert self._matches(
            "Apple described the regulator's demand as disproportionate "
            "to any alleged harm."
        )

    def test_characterized_fine_as_unprecedented(self):
        assert self._matches(
            "Amazon characterized the regulator's fine as unprecedented "
            "in European competition history."
        )

    def test_said_calculation_was_baseless(self):
        assert self._matches(
            "Meta said the calculation was baseless and unsupported."
        )

    def test_highlighted_the_sum(self):
        assert self._matches(
            "The company highlighted the total in its quarterly earnings call."
        )

    def test_has_no_precedent(self):
        assert self._matches(
            "This has no precedent in the history of antitrust enforcement."
        )


# ---------------------------------------------------------------------------
# strategic_disclosure: true negatives
# ---------------------------------------------------------------------------

class TestStrategicDisclosureTrueNegatives:
    """Sentences that are NOT strategic disclosure."""

    def _matches(self, text: str) -> bool:
        return any(p.search(text) for p in _STRATEGIC_DISCLOSURE_PATTERNS)

    def test_editorial_scale(self):
        """Pure editorial magnitude language should not match."""
        assert not self._matches(
            "The penalty of $1.4 trillion dwarfs the company's annual revenue."
        )

    def test_neutral_reporting(self):
        """Neutral reporting of a number shouldn't match."""
        assert not self._matches(
            "The states are seeking $1.4 trillion in penalties."
        )

    def test_journalist_emphasis(self):
        """Journalist's own framing shouldn't match."""
        assert not self._matches(
            "The staggering sum exceeds the GDP of many countries."
        )


# ---------------------------------------------------------------------------
# expert_consensus_authority: IGNORECASE fix for [A-Z]{2,5}
# ---------------------------------------------------------------------------

class TestExpertConsensusFalsePositiveFix:
    """Verify that lowercase words no longer match the acronym slot."""

    def _matches(self, text: str) -> bool:
        return any(p.search(text) for p in _EXPERT_CONSENSUS_PATTERNS)

    def test_court_hearing_false_positive_eliminated(self):
        """The Reuters sentence that triggered the bug should NOT match."""
        assert not self._matches(
            "The states' filings are sealed, but at a court hearing "
            "in June they said they were calculating the penalties."
        )

    def test_lowercase_but_no_match(self):
        """'but' should not match [A-Z]{2,5} under IGNORECASE fix."""
        assert not self._matches(
            "Documents are sealed, but at a press conference the lawyers said "
            "they planned to appeal."
        )

    def test_legitimate_ceo_still_matches(self):
        """Actual CEO attribution should still match."""
        assert self._matches("said John Smith, CEO at TechCorp")

    def test_legitimate_cto_still_matches(self):
        assert self._matches(
            "Maria Garcia, CTO of DataCo, said the approach was sound"
        )

    def test_legitimate_ciso_still_matches(self):
        assert self._matches("said Kim Lee, CISO at Acme Corp")

    def test_legitimate_director_still_matches(self):
        assert self._matches("said Jane Doe, a senior director at Google")
