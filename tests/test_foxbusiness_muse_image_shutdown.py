r"""
Test editorial_cross_promotion detection on Fox Business Meta Muse Image
shutdown article (Jul 11, 2026).

Regression target: the all-caps interstitial callout regex previously
failed on callouts containing dollar signs and digits (e.g. "$1.4 TRILLION").
The fix extends the character class to include [0-9\$,\.].
"""
from __future__ import annotations

import pytest
from mediascope.analyze.framing import detect_framing_devices


FOXBUSINESS_MUSE_IMAGE_SHUTDOWN = """
Meta shuts down AI tool after backlash over public Instagram accounts

Meta on Friday discontinued an artificial intelligence feature that allowed
users to generate images by referencing public Instagram accounts, days after
introducing the tool as part of a broader rollout of AI-powered creative
features on Instagram.

The company announced the decision in an update to its Instagram blog.

"Earlier this week, we announced that one way for people to generate images
in Meta AI is by @-mentioning public Instagram accounts that they want to
reference," the company wrote. "Our intent was to provide a useful creative
tool and to give people control over whether their public content could be
referenced in this way. We've heard the feedback that this feature missed
the mark, so it's no longer available."

FOUR STATES SEEKING $1.4 TRILLION IN PENALTIES IN CHILD SOCIAL MEDIA ADDICTION TRIAL, META SAYS

The feature was announced Tuesday alongside more than 30 new AI-powered
effects for Instagram Stories using Muse Image, the first image-generation
model from Meta Superintelligence Labs.

JUDGE LETS STATES PURSUE CLAIMS THAT META DESIGNED FACEBOOK AND INSTAGRAM TO ADDICT CHILDREN

SAG-AFTRA urged members Thursday to opt out of the feature, writing on
social media, "Take action to protect your likeness."

CLICK HERE TO GET FOX BUSINESS ON THE GO

Meta has made artificial intelligence a central focus of its business.
"""


class TestFoxBusinessMuseImageShutdown:
    """Tests for framing detection on the Fox Business Muse Image article."""

    def test_editorial_cross_promotion_detected(self):
        """editorial_cross_promotion must fire on all-caps callout blocks
        containing dollar signs and digits."""
        results = detect_framing_devices(FOXBUSINESS_MUSE_IMAGE_SHUTDOWN)
        device_names = {d.device_type for d in results}
        assert "editorial_cross_promotion" in device_names, (
            "editorial_cross_promotion not detected — the regex may still "
            "be failing on dollar signs and digits in all-caps callouts"
        )

    def test_editorial_cross_promotion_count(self):
        """Should detect at least 2 distinct editorial cross-promotion
        callouts (the $1.4T callout and the addictive design callout)."""
        results = detect_framing_devices(FOXBUSINESS_MUSE_IMAGE_SHUTDOWN)
        ecp_hits = [d for d in results if d.device_type == "editorial_cross_promotion"]
        assert len(ecp_hits) >= 2, (
            f"Expected at least 2 editorial_cross_promotion hits, got {len(ecp_hits)}"
        )

    def test_policy_reversal_controlled_retreat(self):
        """Should detect policy_reversal from controlled retreat language:
        'missed the mark', 'heard the feedback', 'no longer available'."""
        results = detect_framing_devices(FOXBUSINESS_MUSE_IMAGE_SHUTDOWN)
        device_names = {d.device_type for d in results}
        assert "policy_reversal" in device_names, (
            "policy_reversal not detected — controlled retreat language "
            "'missed the mark' / 'no longer available' should trigger it"
        )

    def test_loaded_language_misuse(self):
        """The term 'misuse' should now be in the loaded language list."""
        text = "AI-generated ads misuse his likeness to promote supplements."
        results = detect_framing_devices(text)
        device_names = {d.device_type for d in results}
        assert "loaded_language" in device_names, (
            "'misuse' should trigger loaded_language detection"
        )

    def test_dollar_sign_in_callout_not_missed(self):
        """Regression: '$1.4 TRILLION' in an all-caps block must not
        break the editorial_cross_promotion regex."""
        text = "\nFOUR STATES SEEKING $1.4 TRILLION IN PENALTIES IN CHILD SOCIAL MEDIA ADDICTION TRIAL, META SAYS\n"
        results = detect_framing_devices(text)
        device_names = {d.device_type for d in results}
        assert "editorial_cross_promotion" in device_names, (
            "Dollar sign in all-caps callout block breaks editorial_cross_promotion regex"
        )
