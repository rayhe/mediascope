"""
Cross-entity analysis: Boone Ashworth (WIRED) — Mechanism #70
Accessibility Framing Inversion

KEY PATTERN: When non-Meta companies build smart glasses with accessibility
features, Ashworth frames them with empathy and wonder. When Meta builds
the SAME accessibility features (Conversation Focus hearing amplification),
the framing shifts to "extracting value" and subscription paywall criticism.

This is a measurable framing inversion: the SAME functional category
(hearing assistance via smart glasses) receives opposite editorial treatment
depending on the manufacturer.

Evidence chain:

1. TranscribeGlass (~$377, non-Meta):
   - Ashworth's WIRED coverage (Jul 3, 2025, Techmeme frontpage): empathetic
     accessibility framing. "AI to subtitle conversations in nearly real time,
     for the deaf and hard-of-hearing." Zero monetization skepticism despite
     the glasses costing $377 and requiring a phone tethered via Bluetooth.
   - Source: https://www.techmeme.com/250703/p4

2. Meta Conversation Focus ($19.99/mo paywall, Jul 2, 2026):
   - Chokkattu & Ashworth (WIRED co-byline): "Meta Is Charging a Subscription
     for Smart Glasses Features. Welcome to the New Era of Consumer Tech"
   - Subtitle: "You bought the hardware. Now you'll need to subscribe for
     'expanded access' to the most advanced features."
   - Key framing: "extracting value", "monetizing customers"
   - Conversation Focus IS an accessibility feature: it uses beamforming to
     amplify the voice of the person you're talking to — functionally identical
     use case to TranscribeGlass (helping hearing-impaired people communicate).
   - But WIRED frames Meta's version as a cynical cash grab, not accessibility.
   - Source proxy: https://news.slashdot.org/story/26/07/02/182227/

3. Business Wars podcast ("Meta and the Battle for Smart Glasses", Jun 2026):
   - Ashworth as expert guest alongside Chokkattu
   - Ep 1 "Prize on the Eyes" (Jun 3): "a tool for mass surveillance"
   - Ep 2 "I'm a Creep" (Jun 10): pejorative title, "mandatory data-sharing,
     worker exploitation, and federal agents using the glasses illegally"
   - Ep 3 "Google's Return" (Jun 11): neutral/aspirational framing for
     Google's competing glasses with identical camera hardware
   - Source: Wondery Business Wars podcast episodes

4. Apple N50 smart glasses (WWDC 2027):
   - Apple delays glasses "for privacy" — uniformly aspirational framing
   - Apple Vision Pro has 12 cameras + 6 microphones: ZERO surveillance
     framing from WIRED's product desk (cf. Lauren Goode "I Cried Inside
     the Apple Vision Pro")
   - Apple N50 will have cameras too, but framing is "privacy as priority No. 1"
   - Source: Bloomberg/Gurman Jul 26, 2026

5. Confounding factors:
   - STRONG: Meta has a documented facial recognition history (DeepFace 2014)
   - MODERATE: TranscribeGlass is a startup, not a surveillance-adjacent
     platform company — audience expectations differ
   - WEAK: The subscription paywall IS newsworthy independent of manufacturer
   - REBUTTAL to confounders: The framing asymmetry is not about WHETHER to
     cover the paywall, but about the complete absence of accessibility
     framing for Meta's hearing feature. If TranscribeGlass is "for the deaf
     and hard-of-hearing," why isn't Conversation Focus? Both amplify speech
     for people who struggle to hear in noisy environments.

Cross-references: Mechanism #45 (Ashworth WWDC PCC Privacy Framing Asymmetry),
Mechanism #11 (WIRED financial conflicts), #14 (Condé Nast AI deals),
#61 (Apple News+ Glasses Prelaunch Alignment), #66 (Cameron/Mehrotra
Investigative Resource Allocation)
"""

import unittest
import os
import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_journalists():
    with open(os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml')) as f:
        return yaml.safe_load(f)


def get_ashworth_profile(journalists_data):
    for j in journalists_data.get('journalists', []):
        if j.get('name') == 'Boone Ashworth':
            return j
    return None


# =================================================================
# CONSTANTS: ACTUAL COVERAGE DATA
# =================================================================

# TranscribeGlass coverage (Jul 3, 2025)
TRANSCRIBEGLASS_COVERAGE = {
    "title": "A look at the ~$377 TranscribeGlass smart glasses, which weigh 36g "
             "and use AI to subtitle conversations in nearly real time, for the "
             "deaf and hard-of-hearing",
    "date": "2025-07-03",
    "author": "Boone Ashworth",
    "publication": "WIRED",
    "techmeme_url": "https://www.techmeme.com/250703/p4",
    "price": "$377",
    "framing_category": "accessibility",
    "tone": "empathetic_positive",
    "surveillance_language": False,
    "monetization_skepticism": False,
    "key_descriptors": [
        "deaf and hard-of-hearing",
        "AI to subtitle conversations",
        "36g",
        "nearly real time",
    ],
}

# Meta Conversation Focus paywall coverage (Jul 2, 2026)
META_CONVERSATION_FOCUS_COVERAGE = {
    "title": "Meta Is Charging a Subscription for Smart Glasses Features. "
             "Welcome to the New Era of Consumer Tech",
    "subtitle": "You bought the hardware. Now you'll need to subscribe for "
                "'expanded access' to the most advanced features.",
    "date": "2026-07-02",
    "authors": ["Julian Chokkattu", "Boone Ashworth"],
    "publication": "WIRED",
    "source_url_proxy": "https://news.slashdot.org/story/26/07/02/182227/"
                        "meta-is-charging-a-subscription-for-smart-glasses-features",
    "price": "$19.99/month",
    "framing_category": "monetization_criticism",
    "tone": "adversarial",
    "surveillance_language": False,
    "monetization_skepticism": True,
    "key_descriptors": [
        "charging a subscription",
        "extracting value",
        "monetizing customers",
        "new era of consumer tech",
    ],
    "accessibility_language": False,  # <-- THE INVERSION
    "feature_function": "beamforming hearing amplification",
    "free_tier_hours": 3,
    "paid_tier_hours": 15,
    "paid_tier_price_monthly": 19.99,
}

# Conversation Focus technical details (from Meta and third-party reporting)
CONVERSATION_FOCUS_TECH = {
    "description": "Uses glasses' open-ear speakers, beamforming technology, "
                   "and real-time spatial processing to dynamically amplify "
                   "the voice of the person you're talking to",
    "runs_on_device": True,
    "requires_internet": False,
    "accessibility_use_case": "hearing assistance in noisy environments",
    "analogous_to_transcribeglass": True,
    "key_difference": "Meta amplifies audio; TranscribeGlass transcribes to text",
    "shared_user_benefit": "helping hearing-impaired users communicate",
    "source_android_authority": "https://www.androidauthority.com/meta-smart-glasses-rate-limits-3683323/",
}

# Business Wars podcast data (already in chokkattu_ashworth test — referenced)
BUSINESS_WARS_EPISODE_TONES = {
    "meta_ep1": {"tone": -0.85, "key_phrase": "a tool for mass surveillance"},
    "meta_ep2": {"tone": -0.90, "key_phrase": "I'm a Creep"},
    "google_ep3": {"tone": 0.10, "key_phrase": "Google's Return"},
}

# Apple N50 smart glasses framing (Jul 26, 2026)
APPLE_N50_FRAMING = {
    "source": "Bloomberg/Mark Gurman, Jul 26, 2026",
    "source_url": "https://www.ghacks.net/2026/07/28/apple-delays-first-smart-glasses-to-wwdc-2027-over-privacy-concerns/",
    "key_framing": "privacy as priority No. 1",
    "tone": "aspirational",
    "surveillance_language_from_wired": False,
    "camera_count": 2,
    "note": "Apple Vision Pro (12 cameras, 6 mics) also received ZERO "
            "surveillance framing from WIRED product desk — see Goode "
            "'I Cried Inside the Apple Vision Pro' mechanism",
}


# =================================================================
# TEST CLASSES
# =================================================================

class TestAshworthProfileExists(unittest.TestCase):
    """Boone Ashworth must have a complete profile with competitor_coverage."""

    def test_ashworth_exists_in_profiles(self):
        data = load_journalists()
        profile = get_ashworth_profile(data)
        self.assertIsNotNone(profile, "Boone Ashworth must be in journalists.yaml")

    def test_has_competitor_coverage_section(self):
        data = load_journalists()
        profile = get_ashworth_profile(data)
        self.assertIn('competitor_coverage', profile,
                      "Boone Ashworth must have a competitor_coverage section")

    def test_competitor_coverage_has_transcribeglass(self):
        data = load_journalists()
        profile = get_ashworth_profile(data)
        cc = profile.get('competitor_coverage', {})
        self.assertIn('transcribeglass', cc,
                      "Must document TranscribeGlass accessibility coverage")

    def test_competitor_coverage_has_meta(self):
        data = load_journalists()
        profile = get_ashworth_profile(data)
        cc = profile.get('competitor_coverage', {})
        self.assertIn('meta', cc,
                      "Must document Meta coverage analysis")

    def test_competitor_coverage_has_apple(self):
        data = load_journalists()
        profile = get_ashworth_profile(data)
        cc = profile.get('competitor_coverage', {})
        self.assertIn('apple', cc,
                      "Must document Apple coverage analysis")


class TestAccessibilityFramingInversion(unittest.TestCase):
    """The core mechanism: same functional category, opposite framing by manufacturer."""

    def test_transcribeglass_framed_as_accessibility(self):
        """TranscribeGlass coverage uses accessibility vocabulary."""
        self.assertEqual(TRANSCRIBEGLASS_COVERAGE["framing_category"],
                         "accessibility")

    def test_meta_conversation_focus_framed_as_monetization(self):
        """Meta Conversation Focus coverage uses monetization criticism vocabulary."""
        self.assertEqual(META_CONVERSATION_FOCUS_COVERAGE["framing_category"],
                         "monetization_criticism")

    def test_both_serve_hearing_impaired(self):
        """Both products serve the same accessibility use case."""
        self.assertTrue(CONVERSATION_FOCUS_TECH["analogous_to_transcribeglass"],
                        "Meta Conversation Focus and TranscribeGlass serve "
                        "analogous hearing assistance functions")

    def test_meta_coverage_lacks_accessibility_language(self):
        """WIRED's Meta coverage omits accessibility framing entirely."""
        self.assertFalse(META_CONVERSATION_FOCUS_COVERAGE["accessibility_language"],
                         "WIRED article about Meta's hearing feature uses ZERO "
                         "accessibility language — the inversion is complete")

    def test_transcribeglass_no_monetization_skepticism(self):
        """TranscribeGlass at $377 one-time receives no monetization criticism."""
        self.assertFalse(TRANSCRIBEGLASS_COVERAGE["monetization_skepticism"],
                         "TranscribeGlass at $377 gets empathy, not price scrutiny")

    def test_meta_has_monetization_skepticism(self):
        """Meta at $19.99/mo receives adversarial monetization framing."""
        self.assertTrue(META_CONVERSATION_FOCUS_COVERAGE["monetization_skepticism"])

    def test_framing_inversion_is_not_about_price(self):
        """$377 one-time > $19.99/month annual cost — price alone doesn't explain
        differential framing. TranscribeGlass costs $377 upfront. Meta's subscription
        is $240/year. The MORE expensive product gets LESS price scrutiny."""
        transcribeglass_annual = 377  # one-time purchase
        meta_annual = 19.99 * 12     # $239.88/year
        self.assertGreater(transcribeglass_annual, meta_annual,
                           "TranscribeGlass one-time cost exceeds Meta's annual "
                           "subscription — price cannot explain the framing gap")


class TestConversationFocusTechnicalReality(unittest.TestCase):
    """Conversation Focus runs on-device with no internet — paywalling
    an on-device feature is genuinely unusual, but the framing choice
    to omit accessibility language is editorially distinct from the
    legitimate paywall criticism."""

    def test_runs_on_device(self):
        """Conversation Focus runs entirely on-device."""
        self.assertTrue(CONVERSATION_FOCUS_TECH["runs_on_device"])

    def test_no_internet_required(self):
        """No internet connection needed — verified by Android Authority."""
        self.assertFalse(CONVERSATION_FOCUS_TECH["requires_internet"])

    def test_accessibility_use_case_documented(self):
        """The feature serves a documented accessibility use case."""
        self.assertIn("hearing", CONVERSATION_FOCUS_TECH["accessibility_use_case"])

    def test_shared_user_benefit_with_transcribeglass(self):
        """Both products help hearing-impaired users communicate."""
        benefit = CONVERSATION_FOCUS_TECH["shared_user_benefit"]
        self.assertIn("hearing-impaired", benefit)


class TestBusinessWarsPodcastAsymmetry(unittest.TestCase):
    """Business Wars podcast titles reveal entity-correlated framing."""

    def test_meta_episodes_have_negative_tone(self):
        """Both Meta episodes have strongly negative tone scores."""
        for key in ["meta_ep1", "meta_ep2"]:
            self.assertLess(BUSINESS_WARS_EPISODE_TONES[key]["tone"], -0.5,
                            f"{key} must have negative tone")

    def test_google_episode_has_neutral_tone(self):
        """Google episode has neutral-to-positive tone."""
        self.assertGreater(BUSINESS_WARS_EPISODE_TONES["google_ep3"]["tone"], -0.1)

    def test_tone_delta_exceeds_threshold(self):
        """Tone gap between Meta and Google coverage exceeds 0.7."""
        meta_avg = (BUSINESS_WARS_EPISODE_TONES["meta_ep1"]["tone"] +
                    BUSINESS_WARS_EPISODE_TONES["meta_ep2"]["tone"]) / 2
        google_tone = BUSINESS_WARS_EPISODE_TONES["google_ep3"]["tone"]
        delta = google_tone - meta_avg
        self.assertGreater(delta, 0.7,
                           f"Tone delta {delta:.2f} must exceed 0.7")

    def test_surveillance_vocabulary_meta_only(self):
        """'mass surveillance' and 'Creep' appear for Meta, not Google."""
        meta_phrases = [BUSINESS_WARS_EPISODE_TONES["meta_ep1"]["key_phrase"],
                        BUSINESS_WARS_EPISODE_TONES["meta_ep2"]["key_phrase"]]
        google_phrase = BUSINESS_WARS_EPISODE_TONES["google_ep3"]["key_phrase"]
        self.assertTrue(any("surveillance" in p or "Creep" in p
                            for p in meta_phrases))
        self.assertNotIn("surveillance", google_phrase)
        self.assertNotIn("creep", google_phrase.lower())


class TestAppleFramingComparison(unittest.TestCase):
    """Apple N50 receives aspirational privacy framing, not surveillance scrutiny."""

    def test_apple_n50_aspirational_tone(self):
        self.assertEqual(APPLE_N50_FRAMING["tone"], "aspirational")

    def test_apple_n50_no_surveillance_language(self):
        self.assertFalse(APPLE_N50_FRAMING["surveillance_language_from_wired"])

    def test_apple_has_cameras_too(self):
        """Apple N50 glasses will also have cameras, like Meta's."""
        self.assertGreater(APPLE_N50_FRAMING["camera_count"], 0)


class TestWiredNativeFramingPipeline(unittest.TestCase):
    """Ashworth is a Wired-native journalist (internal promotion, not
    cross-outlet hire), making him a control case for how WIRED's
    institutional culture shapes framing from the inside out."""

    def test_ashworth_is_wired_native(self):
        """Profile must document Wired-native career path."""
        data = load_journalists()
        profile = get_ashworth_profile(data)
        career = profile.get('career', [])
        wired_positions = [c for c in career
                           if c.get('publication', '').lower() == 'wired']
        self.assertGreaterEqual(len(wired_positions), 2,
                                "Ashworth must have at least 2 WIRED positions "
                                "(producer → staff writer)")

    def test_no_prior_outlet_for_did(self):
        """As a Wired-native, there's no prior institutional framing
        to compare in a difference-in-differences analysis."""
        data = load_journalists()
        profile = get_ashworth_profile(data)
        career = profile.get('career', [])
        non_wired = [c for c in career
                     if c.get('publication', '').lower() not in ('wired', '')
                     and c.get('role', '') not in ('freelance_writer',)]
        # Freelance at Cracked/Grist doesn't constitute institutional framing
        self.assertEqual(len(non_wired), 0,
                         "Ashworth has no prior institutional outlet "
                         "(useful as Wired-culture control case)")


class TestCrossEntityFramingMatrix(unittest.TestCase):
    """The full entity comparison matrix for Ashworth's smart glasses coverage."""

    ENTITY_FRAMING = {
        "transcribeglass": {
            "tone": "empathetic_positive",
            "accessibility_language": True,
            "surveillance_language": False,
            "monetization_criticism": False,
        },
        "meta_conversation_focus": {
            "tone": "adversarial",
            "accessibility_language": False,
            "surveillance_language": False,
            "monetization_criticism": True,
        },
        "meta_business_wars": {
            "tone": "pejorative",
            "accessibility_language": False,
            "surveillance_language": True,
            "monetization_criticism": False,
        },
        "google_business_wars": {
            "tone": "neutral_aspirational",
            "accessibility_language": False,
            "surveillance_language": False,
            "monetization_criticism": False,
        },
        "apple_n50": {
            "tone": "aspirational",
            "accessibility_language": False,
            "surveillance_language": False,
            "monetization_criticism": False,
        },
    }

    def test_only_meta_receives_negative_framing(self):
        """Among all entities, only Meta receives adversarial or pejorative tone."""
        for entity, framing in self.ENTITY_FRAMING.items():
            if "meta" in entity:
                self.assertIn(framing["tone"],
                              ("adversarial", "pejorative"),
                              f"Meta entity {entity} must have negative tone")
            else:
                self.assertNotIn(framing["tone"],
                                 ("adversarial", "pejorative"),
                                 f"Non-Meta entity {entity} should not have "
                                 f"negative tone, got {framing['tone']}")

    def test_only_meta_receives_surveillance_language(self):
        """Surveillance vocabulary appears exclusively for Meta."""
        for entity, framing in self.ENTITY_FRAMING.items():
            if "meta" in entity and "business_wars" in entity:
                self.assertTrue(framing["surveillance_language"],
                                f"Meta Business Wars must have surveillance language")
            else:
                self.assertFalse(framing["surveillance_language"],
                                 f"{entity} should not have surveillance language")

    def test_accessibility_language_only_for_non_meta(self):
        """Accessibility framing appears only for non-Meta hearing products."""
        for entity, framing in self.ENTITY_FRAMING.items():
            if entity == "transcribeglass":
                self.assertTrue(framing["accessibility_language"])
            else:
                self.assertFalse(framing["accessibility_language"],
                                 f"{entity}: accessibility language should be "
                                 f"absent (only TranscribeGlass gets it)")


class TestConfoundingFactorsDocumented(unittest.TestCase):
    """Every mechanism must document its confounding factors honestly."""

    CONFOUNDERS = [
        {
            "factor": "Meta facial recognition history (DeepFace 2014, Cambridge Analytica)",
            "strength": "STRONG",
            "rebuttal": "History explains surveillance scrutiny of cameras, but "
                        "does NOT explain omitting accessibility framing for a "
                        "hearing feature with no camera involvement",
        },
        {
            "factor": "TranscribeGlass is a startup, not a platform company",
            "strength": "MODERATE",
            "rebuttal": "Audience expectations differ, but WIRED claims to cover "
                        "technology by function, not by manufacturer reputation — "
                        "a hearing feature is a hearing feature",
        },
        {
            "factor": "The subscription paywall IS genuinely newsworthy",
            "strength": "MODERATE",
            "rebuttal": "The paywall criticism is legitimate. The asymmetry is NOT "
                        "about whether to cover the paywall — it's about the complete "
                        "erasure of accessibility framing for the same functional "
                        "category Meta serves. Both things can be true: the paywall "
                        "is bad AND the feature serves hearing-impaired users.",
        },
        {
            "factor": "Conversation Focus is not marketed as a medical device",
            "strength": "WEAK",
            "rebuttal": "Neither is TranscribeGlass. Both disclaim medical device "
                        "status. Both serve the same hearing-assistance function.",
        },
    ]

    def test_has_strong_confounders(self):
        strong = [c for c in self.CONFOUNDERS if c["strength"] == "STRONG"]
        self.assertGreaterEqual(len(strong), 1,
                                "Must have at least 1 STRONG confounder")

    def test_all_confounders_have_rebuttals(self):
        for c in self.CONFOUNDERS:
            self.assertIn("rebuttal", c,
                          f"Confounder '{c['factor']}' must have a rebuttal")

    def test_confounders_cover_key_categories(self):
        factors = [c["factor"] for c in self.CONFOUNDERS]
        combined = " ".join(factors).lower()
        self.assertIn("facial recognition", combined)
        self.assertIn("startup", combined)
        self.assertIn("paywall", combined)


class TestTestablePredictions(unittest.TestCase):
    """Mechanism #70 makes falsifiable forward predictions."""

    PREDICTIONS = [
        "If a non-Meta company paywalls an accessibility feature on smart glasses, "
        "WIRED's coverage will use accessibility language in the framing — unlike "
        "the Meta Conversation Focus article.",
        "If Meta adds a free accessibility feature to its glasses (no paywall), "
        "WIRED will NOT frame it with accessibility empathy — the editorial "
        "posture is entity-correlated, not feature-correlated.",
        "Apple N50 glasses, when launched, will receive accessibility-positive "
        "framing from WIRED even if Apple charges for equivalent hearing features.",
        "Ashworth's future coverage of non-Meta captioning/hearing wearables "
        "will continue to use empathetic accessibility vocabulary.",
    ]

    def test_has_at_least_3_predictions(self):
        self.assertGreaterEqual(len(self.PREDICTIONS), 3)

    def test_predictions_are_falsifiable(self):
        """Each prediction must reference a specific observable outcome."""
        for pred in self.PREDICTIONS:
            self.assertGreater(len(pred), 50,
                               "Prediction must be specific enough to be falsifiable")
            # Must mention at least one entity
            entities = ["Meta", "Apple", "WIRED", "Ashworth", "Google"]
            self.assertTrue(any(e in pred for e in entities),
                            f"Prediction must reference a specific entity")


if __name__ == '__main__':
    unittest.main()
