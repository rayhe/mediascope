"""Tests for policy_reversal, competitive_deficit framing devices
and documentary source type.

Added: 2026-07-03, Type A iteration.
Covers three new features discovered from Reuters and Barron's
Zuckerberg town hall analyses.
"""

from __future__ import annotations

import pytest

from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sources import extract_sources
from mediascope.analyze.sentiment import _ADVERSARIAL_DEVICE_TYPES


# ---------------------------------------------------------------------------
# policy_reversal framing device
# ---------------------------------------------------------------------------

class TestPolicyReversal:
    """Tests for the policy_reversal framing device."""

    def test_originally_now_pattern(self):
        """Detects 'originally X ... now Y' reversal language."""
        text = (
            "Meta originally had no way for users to opt out of facial "
            "recognition on its glasses. The company will now offer the "
            "feature on an opt-in basis."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "policy_reversal" in types

    def test_reversed_policy_pattern(self):
        """Detects 'reversed its policy' language."""
        text = (
            "The company reversed its earlier policy on data collection, "
            "which had required all users to submit biometric data."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "policy_reversal" in types

    def test_walked_back_pattern(self):
        """Detects 'walked back' reversal language."""
        text = (
            "Facebook walked back its controversial decision to make "
            "all posts public by default."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "policy_reversal" in types

    def test_mandatory_to_voluntary(self):
        """Detects mandatory → voluntary transition."""
        text = (
            "The mouse-tracking feature was mandatory for all MCI users "
            "but will be changed to voluntary after the backlash."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "policy_reversal" in types

    def test_opt_out_to_opt_in(self):
        """Detects opt-out → opt-in transition."""
        text = (
            "The facial recognition system switched from opt-out "
            "to opt-in after regulators intervened."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "policy_reversal" in types

    def test_no_longer_requires(self):
        """Detects 'no longer requires' cessation language."""
        text = (
            "Meta will no longer require users to share their "
            "location data with advertisers."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "policy_reversal" in types

    def test_scrapped_plan(self):
        """Detects 'scrapped its plan' reversal."""
        text = (
            "Google scrapped its existing plan to eliminate "
            "third-party cookies from Chrome."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "policy_reversal" in types

    def test_is_adversarial(self):
        """policy_reversal IS adversarial — frames subject as forced to
        reverse course under pressure, positioning capitulation as an
        admission of wrongdoing.  Reclassified Jul 14 2026 after NY Post
        Muse Image article showed that consent_alarm + policy_reversal
        creates a 'corporate humiliation' narrative that VADER misreads
        as positive."""
        assert "policy_reversal" in _ADVERSARIAL_DEVICE_TYPES

    def test_no_false_positive_future_plans(self):
        """Should not fire on simple future plans without a prior policy."""
        text = (
            "Meta said it will offer users a new privacy dashboard "
            "in the next software update."
        )
        devices = detect_framing_devices(text)
        pr_devices = [d for d in devices if d.device_type == "policy_reversal"]
        assert len(pr_devices) == 0


# ---------------------------------------------------------------------------
# competitive_deficit framing device
# ---------------------------------------------------------------------------

class TestCompetitiveDeficit:
    """Tests for the competitive_deficit framing device."""

    def test_failed_to_launch_rival_list(self):
        """Detects 'failed to launch rival to [A], [B], and [C]'."""
        text = (
            "Meta has failed to launch a successful rival to OpenAI's "
            "ChatGPT, Google's Gemini, and Anthropic's Claude."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "competitive_deficit" in types

    def test_struggling_to_compete(self):
        """Detects 'struggling to compete' with competitor listing."""
        text = (
            "The company is struggling to compete in AI, trailing behind "
            "OpenAI in conversational AI and Google in search integration, "
            "while Anthropic has captured the enterprise market."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "competitive_deficit" in types

    def test_competitors_including_list(self):
        """Detects 'competitors including [A], [B], and [C]'."""
        text = (
            "Meta faces stiff competition from rivals including "
            "OpenAI, Google, and Anthropic in the AI assistant space."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "competitive_deficit" in types

    def test_while_rivals_have_shipped(self):
        """Detects contrast listing: 'while [A] and [B] have launched...'."""
        text = (
            "Meta's AI assistant remains limited, while OpenAI has "
            "launched advanced reasoning and Google has shipped Gemini "
            "into every Android device, and Apple has already integrated "
            "its intelligence suite into iOS."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "competitive_deficit" in types

    def test_is_adversarial(self):
        """competitive_deficit SHOULD be in adversarial device types."""
        assert "competitive_deficit" in _ADVERSARIAL_DEVICE_TYPES

    def test_no_false_positive_single_competitor(self):
        """Should not fire on single competitor comparison (that's competitive_positioning)."""
        text = (
            "Meta's AI assistant is not as advanced as OpenAI's "
            "ChatGPT in reasoning tasks."
        )
        devices = detect_framing_devices(text)
        cd_devices = [d for d in devices if d.device_type == "competitive_deficit"]
        assert len(cd_devices) == 0


# ---------------------------------------------------------------------------
# documentary source type
# ---------------------------------------------------------------------------

class TestDocumentarySourceType:
    """Tests for the documentary source type in source extraction."""

    def test_recording_heard_by(self):
        """Detects 'a recording heard by [Outlet]'."""
        text = (
            "According to a recording of the meeting heard by Reuters, "
            "Zuckerberg told staff that AI agents had been disappointing."
        )
        sources = extract_sources(text)
        doc_sources = [s for s in sources if s.source_type == "documentary"]
        assert len(doc_sources) >= 1

    def test_documents_obtained_by(self):
        """Detects 'documents obtained by [Outlet]'."""
        text = (
            "Internal documents obtained by The Guardian reveal that "
            "the company was aware of the privacy risks for years."
        )
        sources = extract_sources(text)
        doc_sources = [s for s in sources if s.source_type == "documentary"]
        assert len(doc_sources) >= 1

    def test_documents_seen_by(self):
        """Detects 'internal documents seen by [Outlet]'."""
        text = (
            "Internal documents seen by Wired show that engineers "
            "flagged safety concerns months before launch."
        )
        sources = extract_sources(text)
        doc_sources = [s for s in sources if s.source_type == "documentary"]
        assert len(doc_sources) >= 1

    def test_filing_obtained_by(self):
        """Detects 'a filing obtained by [Outlet]'."""
        text = (
            "A filing obtained by Bloomberg details the company's "
            "plans to restructure its AI division."
        )
        sources = extract_sources(text)
        doc_sources = [s for s in sources if s.source_type == "documentary"]
        assert len(doc_sources) >= 1

    def test_according_to_recording(self):
        """Detects 'according to a recording' pattern."""
        text = (
            "According to a recording of the all-hands meeting, the "
            "CEO expressed frustration with the pace of AI development."
        )
        sources = extract_sources(text)
        doc_sources = [s for s in sources if s.source_type == "documentary"]
        assert len(doc_sources) >= 1

    def test_court_records_show(self):
        """Detects 'court records show' pattern."""
        text = (
            "Court records show that the company settled with the "
            "plaintiff for an undisclosed amount."
        )
        sources = extract_sources(text)
        doc_sources = [s for s in sources if s.source_type == "documentary"]
        assert len(doc_sources) >= 1

    def test_copy_of_which(self):
        """Detects 'a copy of which was obtained by' pattern."""
        text = (
            "The memo, a copy of which was obtained by The New York "
            "Times, outlined three possible restructuring scenarios."
        )
        sources = extract_sources(text)
        doc_sources = [s for s in sources if s.source_type == "documentary"]
        assert len(doc_sources) >= 1

    def test_documents_which_outlet_reviewed(self):
        """Detects 'documents which [Outlet] has reviewed' pattern."""
        text = (
            "The leaked emails which The Atlantic has reviewed suggest "
            "executives knew about the vulnerability before it was exploited."
        )
        sources = extract_sources(text)
        doc_sources = [s for s in sources if s.source_type == "documentary"]
        assert len(doc_sources) >= 1

    def test_not_anonymous(self):
        """Documentary sources should not be marked as anonymous."""
        text = (
            "A recording heard by Reuters captures the CEO saying "
            "that agents are not ready for consumer use."
        )
        sources = extract_sources(text)
        doc_sources = [s for s in sources if s.source_type == "documentary"]
        for s in doc_sources:
            assert not s.is_anonymous, (
                f"Documentary source '{s.name}' should not be anonymous"
            )

    def test_sec_filings_show(self):
        """Detects 'SEC filings show' pattern."""
        text = (
            "SEC filings show that the company's executive compensation "
            "tripled over the past fiscal year."
        )
        sources = extract_sources(text)
        doc_sources = [s for s in sources if s.source_type == "documentary"]
        assert len(doc_sources) >= 1

    def test_internal_memo_reviewed(self):
        """Detects 'an internal memo reviewed by [Outlet]'."""
        text = (
            "An internal memo reviewed by The Wall Street Journal "
            "describes the plan as 'highly experimental'."
        )
        sources = extract_sources(text)
        doc_sources = [s for s in sources if s.source_type == "documentary"]
        assert len(doc_sources) >= 1
