"""Tests for safeguard_inadequacy framing device (#111).

Validates detection of the editorial pattern where a technical or policy
safeguard (privacy LED, opt-out, data deletion, recording indicator) is
introduced and then systematically undermined as insufficient, easily
circumvented, or performative.

Discovered from multiple Jul 2026 wearables privacy articles:
- 9to5Google (Jul 7): "Meta Ray-Ban glasses now disable the camera if
  privacy light breaks" — workarounds to avoid the light
- Northeastern (Jun 22): "people might not see it or know what it means"
- LiveMint: "The option to disable voice recordings storage is no longer
  available"
- Laptop Mag: "you run the risk of your data being misused"

Source URLs:
- https://9to5google.com/2026/07/07/meta-ray-ban-smart-glasses-privacy-light-camera-update/
- https://news.northeastern.edu/2026/06/22/meta-smart-glasses-privacy/
- https://www.laptopmag.com/ai/best-smart-glasses-meta-ray-ban-privacy-policy
"""

import pytest

from mediascope.analyze.framing import detect_framing_devices


class TestSafeguardInadequacyPositive:
    """Positive detection: real editorial phrases that exhibit safeguard_inadequacy."""

    @pytest.mark.parametrize(
        "text,description",
        [
            # Pattern 1: safeguard + but/however + inadequacy
            (
                "The privacy light on the glasses is there to indicate when the "
                "camera is active, but people might not see it or know what it means.",
                "privacy light inadequacy — people might not see it",
            ),
            (
                "Meta's glasses have a recording indicator, however it is easily "
                "circumvented by users who want to record covertly.",
                "recording indicator circumvented",
            ),
            (
                "The capture LED is designed to alert bystanders, yet there "
                "were workarounds to avoid the light being seen.",
                "capture LED workarounds",
            ),
            (
                "Users have an opt-out option, but it is meaningless when "
                "the default behavior already captures everything.",
                "opt-out meaningless",
            ),
            (
                "The consent toggle exists in settings, although the problem "
                "is that most users don't know it's there and it is inadequate "
                "to protect bystanders.",
                "consent toggle inadequate",
            ),
            # Pattern 2: growing market for defeating safeguards
            (
                "There is a growing market for disabling these light indicators, "
                "according to reports.",
                "growing market for disabling indicators",
            ),
            (
                "An emerging industry of services exists for defeating the "
                "privacy LEDs on smart glasses.",
                "emerging industry for defeating LEDs",
            ),
            # Pattern 3: option removed / no longer available
            (
                "The option to disable voice recordings storage is no longer "
                "available, but you can delete recordings anytime in Settings.",
                "opt-out option removed",
            ),
            (
                "The ability to opt out of data collection has been removed "
                "in the latest update.",
                "opt-out ability removed",
            ),
            (
                "The setting to turn off cloud processing was quietly dropped "
                "from the app.",
                "setting quietly dropped",
            ),
            # Pattern 4: services offered to alter/modify
            (
                "Some have even offered up services to alter the glasses for "
                "this purpose, as has been reported on.",
                "services to alter glasses",
            ),
            (
                "Multiple companies now sell kits to disable the recording "
                "indicator light.",
                "sell kits to disable indicator",
            ),
            # Pattern 5: no real opt-out
            (
                "There is no real opt-out option for voice recording with "
                "these glasses.",
                "no real opt-out",
            ),
            (
                "Users cannot opt out of having their voice data stored by "
                "the AI assistant.",
                "cannot opt-out of voice data",
            ),
            (
                "There's no way to prevent the glasses from collecting "
                "ambient audio data.",
                "no way to prevent collection",
            ),
            # Pattern 6: safeguard as theater/performative
            (
                "The privacy light is window dressing — a cosmetic measure "
                "that provides no real protection.",
                "privacy light as window dressing",
            ),
            (
                "Critics argue these privacy controls are nothing more than "
                "security theater designed to pacify regulators.",
                "privacy controls as security theater",
            ),
        ],
        ids=lambda x: x if isinstance(x, str) and len(x) < 60 else None,
    )
    def test_positive_detection(self, text: str, description: str) -> None:
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "safeguard_inadequacy" in types, (
            f"Expected safeguard_inadequacy for: {description}\n"
            f"Detected: {sorted(types)}"
        )


class TestSafeguardInadequacyNegative:
    """Negative cases: text that should NOT trigger safeguard_inadequacy."""

    @pytest.mark.parametrize(
        "text,description",
        [
            # Pure factual description of a safeguard without undermining
            (
                "Meta's smart glasses feature a privacy LED that illuminates "
                "when the camera is recording.",
                "factual safeguard description without dismissal",
            ),
            # consent_alarm territory — not safeguard dismissal
            (
                "The feature was enabled by default without clear user consent.",
                "consent alarm — not safeguard dismissal",
            ),
            # surveillance_creep territory
            (
                "The glasses constantly capture audio and visuals throughout "
                "the day.",
                "surveillance creep — not safeguard dismissal",
            ),
            # Positive framing of safeguard working
            (
                "Meta has updated the glasses to disable the camera entirely "
                "if the privacy LED is tampered with.",
                "safeguard working as intended — positive framing",
            ),
        ],
        ids=lambda x: x if isinstance(x, str) and len(x) < 60 else None,
    )
    def test_negative_detection(self, text: str, description: str) -> None:
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "safeguard_inadequacy" not in types, (
            f"False positive safeguard_inadequacy for: {description}\n"
            f"Text: {text}"
        )
