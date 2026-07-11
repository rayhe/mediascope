"""Tests for recidivism_framing device detection.

Recidivism framing constructs a serial-offender narrative through temporal
recurrence markers — distinct from repeated_disruption (organizational
instability) and loaded_language (individual word choices).
"""

import pytest
from mediascope.analyze.framing import detect_framing_devices


def _has_device(text: str, device: str) -> bool:
    results = detect_framing_devices(text)
    return any(d.device_type == device for d in results)


def _get_devices(text: str, device: str):
    results = detect_framing_devices(text)
    return [d for d in results if d.device_type == device]


# ── Positive cases ─────────────────────────────────────────────────────


class TestRecidivismFramingPositive:
    """Sentences that SHOULD trigger recidivism_framing."""

    def test_once_again_caught(self):
        text = (
            "Meta was once again caught violating its own privacy commitments, "
            "according to regulators who announced the latest enforcement action."
        )
        assert _has_device(text, "recidivism_framing")

    def test_yet_again_fined(self):
        text = (
            "The company was yet again fined by European regulators for "
            "mishandling user data under GDPR."
        )
        assert _has_device(text, "recidivism_framing")

    def test_time_and_again(self):
        text = (
            "Critics point out that time and again the platform has failed "
            "to protect minors from harmful content."
        )
        assert _has_device(text, "recidivism_framing")

    def test_for_the_second_time(self):
        text = (
            "For the second time in three years, the FTC accused Meta of "
            "violating a consent decree."
        )
        assert _has_device(text, "recidivism_framing")

    def test_continues_to_violate(self):
        text = (
            "The report found that the company continues to violate its "
            "data-sharing agreements with partner developers."
        )
        assert _has_device(text, "recidivism_framing")

    def test_not_the_first_time(self):
        text = (
            "This is not the first time the social media giant has faced "
            "such allegations."
        )
        assert _has_device(text, "recidivism_framing")

    def test_not_for_the_first_time(self):
        text = (
            "Not for the first time, regulators are questioning whether "
            "the company's promises mean anything."
        )
        assert _has_device(text, "recidivism_framing")

    def test_long_history_of_violations(self):
        text = (
            "Meta has a long history of privacy violations dating back "
            "to the Cambridge Analytica scandal."
        )
        assert _has_device(text, "recidivism_framing")

    def test_troubled_history(self):
        text = (
            "The platform has a troubled history of regulatory clashes "
            "in the European Union."
        )
        assert _has_device(text, "recidivism_framing")

    def test_well_documented_history(self):
        text = (
            "Google has a well-documented history of antitrust violations "
            "across multiple jurisdictions."
        )
        assert _has_device(text, "recidivism_framing")

    def test_serial_violator(self):
        text = (
            "Privacy advocates labeled the company a serial violator of "
            "its own stated principles."
        )
        assert _has_device(text, "recidivism_framing")

    def test_repeat_offender(self):
        text = (
            "As a repeat offender under EU data protection law, the "
            "company faces escalating penalties."
        )
        assert _has_device(text, "recidivism_framing")

    def test_habitual_non_compliance(self):
        text = (
            "Regulators described a pattern of habitual non-compliance "
            "spanning more than a decade."
        )
        assert _has_device(text, "recidivism_framing")

    def test_pattern_of_violations(self):
        text = (
            "The complaint describes a pattern of violations that began "
            "well before the current enforcement action."
        )
        assert _has_device(text, "recidivism_framing")

    def test_track_record_of_failures(self):
        text = (
            "With a track record of failures to comply with consent decrees, "
            "the FTC argues stronger measures are warranted."
        )
        assert _has_device(text, "recidivism_framing")

    def test_track_record_broken_promises(self):
        text = (
            "The company's track record of broken promises on child safety "
            "leaves little room for trust."
        )
        assert _has_device(text, "recidivism_framing")

    def test_chronic_misconduct(self):
        text = (
            "European commissioners characterized the situation as chronic "
            "misconduct that required structural remedies."
        )
        assert _has_device(text, "recidivism_framing")

    def test_persistent_abuse(self):
        text = (
            "The ruling cited persistent abuse of dominant market position "
            "over a seven-year period."
        )
        assert _has_device(text, "recidivism_framing")

    def test_again_and_again(self):
        text = (
            "Again and again the company has been caught misleading users "
            "about the extent of data collection."
        )
        assert _has_device(text, "recidivism_framing")

    def test_keeps_violating(self):
        text = (
            "The platform keeps violating the same consent decree that "
            "was supposed to prevent exactly this behavior."
        )
        assert _has_device(text, "recidivism_framing")


# ── Negative / boundary cases ─────────────────────────────────────────


class TestRecidivismFramingNegative:
    """Sentences that should NOT trigger recidivism_framing or should be
    handled by a different device type."""

    def test_once_again_neutral_context(self):
        """'once again' in a non-violation context should not fire."""
        text = (
            "Apple once again reported record quarterly revenue, "
            "beating analyst expectations for the sixth straight quarter."
        )
        assert not _has_device(text, "recidivism_framing")

    def test_history_of_innovation(self):
        """Positive 'history of' should not fire."""
        text = (
            "Google has a long history of innovation in search technology "
            "and artificial intelligence research."
        )
        assert not _has_device(text, "recidivism_framing")

    def test_repeated_disruption_not_recidivism(self):
        """Organizational restructuring is repeated_disruption, not
        recidivism_framing."""
        text = (
            "Meta shakes up its AI division, again. The latest reorganization "
            "comes after months of tumult and restructuring."
        )
        devices = detect_framing_devices(text)
        device_types = {d.device_type for d in devices}
        # Should fire repeated_disruption, not recidivism_framing
        assert "repeated_disruption" in device_types

    def test_track_record_positive(self):
        """Positive track record should not fire."""
        text = (
            "The company's track record of delivering strong earnings "
            "has made it a favorite among institutional investors."
        )
        assert not _has_device(text, "recidivism_framing")

    def test_continues_to_grow(self):
        """'continues to' with positive verb should not fire."""
        text = (
            "The platform continues to grow its user base, adding "
            "50 million monthly active users in the last quarter."
        )
        assert not _has_device(text, "recidivism_framing")
