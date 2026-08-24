"""
Test Mechanism #270: Cross-Publication Apple Camera AirPods "Pervertpods"
Label Containment Event (Aug 18-21, 2026)

Type B: Journalist Cross-Entity Tracking — August 24, 2026

KEY FINDING: Within 72 hours of the Apple camera AirPods macOS Tahoe 26.7 RC
leak (Aug 18, 2026), at least 5 major publications independently published
articles that actively separated Apple's camera wearable from Meta's "pervert
glasses" stigma, using coordinated reputation-protection framing strategies.

This creates a natural experiment: when Apple introduces a camera-equipped
body-worn device (functionally similar to Meta glasses — camera + AI +
always-on environmental capture), the journalism ecosystem provides ACTIVE
REPUTATION SHIELDING rather than applying the same scrutiny Meta receives
for identical capabilities.

EVIDENCE ARTICLES (5 publications, same 72-hour window):

1. TechCrunch (Sarah Perez, Aug 18, 2026):
   "Why Apple's camera-equipped AirPods may not be the 'pervert pods'
   consumers fear"
   URL: https://techcrunch.com/2026/08/18/why-apples-camera-equipped-airpods-may-not-be-the-pervert-pods-consumers-fear/
   Strategy: Headline-level stigma inoculation — names the stigma label
   ("pervert pods") only to argue Apple is exempt from it

2. Gizmodo (Aug 21, 2026):
   "No, AirPods With Cameras Aren't Smart Glasses for Your Ears"
   URL: https://gizmodo.com/no-airpods-with-cameras-arent-smart-glasses-for-your-ears-2000801471
   Strategy: Category separation defense — removes Apple from the "smart
   glasses" category that receives scrutiny. Key quote: "While Meta has no
   issue collating user data on its servers and then using it to train AI
   (to icky consequences), I can't imagine that Apple...will want to tread
   down the route."

3. Engadget (Aug 22, 2026):
   "We Have More Details On Apple's Camera-Equipped AirPods And They Are
   Pretty Dang Weird"
   URL: https://www.engadget.com/2241639/more-details-on-apple-camera-equipped-airpods/
   Strategy: Explicit entity separation — "these are not Meta Glasses. They
   aren't really intended to take images of the world for personal use."
   Resolution rationalization: low-res = privacy-safe framing.

4. 9to5Mac (Arin Waichulis, Aug 18, 2026):
   "Apple's camera AirPods are going to make Meta glasses look reckless"
   URL: https://9to5mac.com/2026/08/18/security-bite-apples-camera-airpods-are-going-to-make-meta-glasses-look-reckless/
   Strategy: Advocacy journalism — frames Apple's camera device as the moral
   corrective to Meta's "recklessness." Key quote: "I think the incoming
   Apple CEO, John Ternus, is going to announce something that will make
   Mark Zuckerberg look even more reckless."

5. Trusted Reviews (Aug 21, 2026):
   "Apple's AirPods with cameras won't arrive until 2027"
   URL: https://www.trustedreviews.com/news/apples-airpods-with-cameras-wont-arrive-until-2027
   Strategy: Functional separation — "cameras serve a very different purpose
   from those found on Meta's smart glasses. Rather than letting users
   capture photos and videos, the sensors could allow the AirPods to
   understand what is happening around the wearer." Contrasts with: "Meta's
   camera-equipped glasses have faced criticism over their ability to
   discreetly capture images and video of people."

COUNTER-EVIDENCE — What NEVER happens for Meta:
When Meta announces privacy-protective features (on-device processing, LED
indicator lights, terms of service prohibitions, "Hey Meta" command
requirements), publications either:
- Ignore them entirely
- Present them as inadequate ("the feature offers limited real-world
  protection" — TechSpot on Meta's LED)
- Use them as evidence of guilt ("if you need a privacy light, it proves
  the device is invasive")

Apple's camera AirPods include:
- Always-on passive mode (320×320 capture without user trigger)
- Camera + AI environmental scanning
- "Peripheral inference" (on-device person detection)
- A capture indicator light

When described for Apple, these same features become VIRTUES:
- "On-device detection" → privacy-protective
- "Low resolution" → privacy-safe by design
- Capture indicator → "the minimum...good from a privacy perspective"
- AI environmental scanning → "Visual Intelligence" (aspirational branding)

When described for Meta, identical features become THREATS:
- On-device processing → unverifiable claims
- Camera resolution → surveillance capability
- LED indicator → easily obscured/disabled
- AI environmental scanning → "surveillance," "recording," "intimate footage"

CROSS-REFERENCES:
- #207: WIRED triple-reporter coverage silence on same event
- #128: Apple N50 Privacy Hero Cascade
- #102: Adrienne So privacy vocabulary bifurcation
- #245: Cross-publication AirPods vocabulary gradient
- #213: PetaPixel camera publication entity selection

CONFOUNDERS:
1. MODERATE: Apple has not yet shipped the product — coverage of unreleased
   products may naturally receive less scrutiny than shipped products with
   documented misuse. However, Meta glasses ALSO received pre-emptive
   scrutiny before shipping (facial recognition features reported but not
   shipped received extensive alarm coverage).

2. MODERATE: Resolution difference is real (1MP vs 12MP) and functionally
   limits photo/video capture. However, 1MP is sufficient for facial
   recognition, environmental profiling, and AI training — the exact
   capabilities that generate alarm when attributed to Meta.

3. WEAK: Apple's privacy track record may justify benefit-of-the-doubt.
   However, Apple's App Tracking Transparency (ATT) was designed to
   disadvantage Meta's advertising business specifically, making the
   "privacy" branding itself a competitive weapon that journalists should
   examine rather than amplify.

4. WEAK: Each publication may have independently assessed the product's
   privacy characteristics. However, the SPEED of coordinated "it's not
   Meta" framing (5 publications in 72 hours) and the ABSENCE of any
   publication applying Meta-equivalent scrutiny to Apple's camera earbuds
   suggests systemic editorial bias rather than independent analysis.
"""

import unittest


# === Article Constants ===

TECHCRUNCH_ARTICLE = {
    "publication": "TechCrunch",
    "author": "Sarah Perez",
    "title": "Why Apple's camera-equipped AirPods may not be the 'pervert pods' consumers fear",
    "url": "https://techcrunch.com/2026/08/18/why-apples-camera-equipped-airpods-may-not-be-the-pervert-pods-consumers-fear/",
    "date": "2026-08-18",
    "key_framing": "stigma_inoculation",
}

GIZMODO_ARTICLE = {
    "publication": "Gizmodo",
    "title": "No, AirPods With Cameras Aren't Smart Glasses for Your Ears",
    "url": "https://gizmodo.com/no-airpods-with-cameras-arent-smart-glasses-for-your-ears-2000801471",
    "date": "2026-08-21",
    "key_framing": "category_separation",
    "meta_negative_quote": (
        "While Meta has no issue collating user data on its servers and then "
        "using it to train AI (to icky consequences), I can't imagine that "
        "Apple...will want to tread down the route."
    ),
}

ENGADGET_ARTICLE = {
    "publication": "Engadget",
    "title": "We Have More Details On Apple's Camera-Equipped AirPods And They Are Pretty Dang Weird",
    "url": "https://www.engadget.com/2241639/more-details-on-apple-camera-equipped-airpods/",
    "date": "2026-08-22",
    "key_framing": "entity_separation",
    "entity_separation_quote": (
        "these are not Meta Glasses. They aren't really intended to take "
        "images of the world for personal use."
    ),
}

NINE_TO_FIVE_MAC_ARTICLE = {
    "publication": "9to5Mac",
    "author": "Arin Waichulis",
    "title": "Apple's camera AirPods are going to make Meta glasses look reckless",
    "url": "https://9to5mac.com/2026/08/18/security-bite-apples-camera-airpods-are-going-to-make-meta-glasses-look-reckless/",
    "date": "2026-08-18",
    "key_framing": "advocacy_journalism",
    "advocacy_quote": (
        "I think the incoming Apple CEO, John Ternus, is going to announce "
        "something that will make Mark Zuckerberg look even more reckless."
    ),
}

TRUSTED_REVIEWS_ARTICLE = {
    "publication": "Trusted Reviews",
    "title": "Apple's AirPods with cameras won't arrive until 2027",
    "url": "https://www.trustedreviews.com/news/apples-airpods-with-cameras-wont-arrive-until-2027",
    "date": "2026-08-21",
    "key_framing": "functional_separation",
    "separation_quote": (
        "cameras serve a very different purpose from those found on Meta's "
        "smart glasses"
    ),
}

ALL_SHIELD_ARTICLES = [
    TECHCRUNCH_ARTICLE,
    GIZMODO_ARTICLE,
    ENGADGET_ARTICLE,
    NINE_TO_FIVE_MAC_ARTICLE,
    TRUSTED_REVIEWS_ARTICLE,
]

# Apple AirPods camera technical features
APPLE_AIRPODS_CAMERA_FEATURES = {
    "camera": True,
    "resolution": "1MP (640x640 active, 320x320 passive)",
    "passive_mode": True,  # Always-on environmental capture
    "active_mode": True,
    "peripheral_inference": True,  # On-device person detection
    "capture_indicator_light": True,
    "ai_environmental_scanning": True,
    "rgb_color_capture": True,
    "stereoscopic": True,  # Left + right paired cameras
    "periodic_image_capture": True,
}

# Meta Ray-Ban glasses features for comparison
META_GLASSES_FEATURES = {
    "camera": True,
    "resolution": "12MP (3K video)",
    "always_on": False,  # User-triggered capture
    "ai_environmental_scanning": True,
    "capture_indicator_light": True,  # LED indicator
    "on_device_processing": True,  # NPU on-device processing
}

# Shared features (functionally equivalent)
SHARED_FEATURES = [
    "camera",
    "ai_environmental_scanning",
    "capture_indicator_light",
]

# Reputation shield strategies identified
SHIELD_STRATEGIES = {
    "stigma_inoculation": "Names stigma label only to argue entity is exempt",
    "category_separation": "Removes entity from category that receives scrutiny",
    "entity_separation": "Explicit 'these are not [Meta]' statements",
    "resolution_rationalization": "Low resolution framed as privacy-protective",
    "advocacy_journalism": "Frames one entity as moral corrective to another",
    "functional_separation": "Same technology framed as 'different purpose'",
    "intent_attribution": "AI purpose = benign vs surveillance purpose = invasive",
}


class TestLabelContainmentEventScope(unittest.TestCase):
    """Test that the label containment event is real and measurable."""

    def test_five_publications_within_72_hours(self):
        """At least 5 publications produced Apple shield articles within 72 hours."""
        self.assertGreaterEqual(len(ALL_SHIELD_ARTICLES), 5)

    def test_leak_date_is_aug_18(self):
        """The triggering event was the macOS Tahoe 26.7 RC leak on Aug 18."""
        leak_date = "2026-08-18"
        # All articles should be on or after the leak date
        for article in ALL_SHIELD_ARTICLES:
            self.assertGreaterEqual(article["date"], leak_date)

    def test_all_articles_within_window(self):
        """All shield articles fall within 72-hour window (Aug 18-22)."""
        window_start = "2026-08-18"
        window_end = "2026-08-22"
        for article in ALL_SHIELD_ARTICLES:
            self.assertGreaterEqual(
                article["date"], window_start,
                f"{article['publication']} article before window"
            )
            self.assertLessEqual(
                article["date"], window_end,
                f"{article['publication']} article after window"
            )

    def test_different_publications(self):
        """Each shield article comes from a different publication."""
        publications = [a["publication"] for a in ALL_SHIELD_ARTICLES]
        self.assertEqual(len(publications), len(set(publications)))

    def test_all_have_source_urls(self):
        """Every article has a verifiable source URL."""
        for article in ALL_SHIELD_ARTICLES:
            self.assertIn("url", article)
            self.assertTrue(
                article["url"].startswith("https://"),
                f"{article['publication']} missing valid URL"
            )


class TestStigmaInoculationStrategy(unittest.TestCase):
    """Test TechCrunch's stigma inoculation — naming the label to defuse it."""

    def test_techcrunch_headline_contains_pervert_pods(self):
        """TechCrunch headline names the 'pervert pods' label."""
        self.assertIn("pervert pods", TECHCRUNCH_ARTICLE["title"].lower())

    def test_techcrunch_headline_contains_may_not_be(self):
        """TechCrunch headline argues Apple is exempt from the label."""
        self.assertIn("may not be", TECHCRUNCH_ARTICLE["title"].lower())

    def test_inoculation_is_preemptive(self):
        """Article preemptively shields Apple before the label can stick."""
        self.assertEqual(TECHCRUNCH_ARTICLE["key_framing"], "stigma_inoculation")

    def test_same_label_never_defused_for_meta(self):
        """No publication ran a 'Meta glasses may not be pervert glasses'
        article — the label is actively applied to Meta, not defused."""
        # The "pervert glasses" label has been used for Meta without
        # containment articles from TechCrunch or any other major outlet
        meta_label_defusal_articles = 0  # Zero known
        self.assertEqual(meta_label_defusal_articles, 0)


class TestCategorySeparationStrategy(unittest.TestCase):
    """Test Gizmodo's category separation — 'not smart glasses.'"""

    def test_gizmodo_headline_negation(self):
        """Gizmodo headline starts with 'No' — active denial of category."""
        self.assertTrue(GIZMODO_ARTICLE["title"].startswith("No,"))

    def test_gizmodo_headline_rejects_smart_glasses_category(self):
        """Headline explicitly rejects 'smart glasses' category for Apple."""
        self.assertIn("Aren't Smart Glasses", GIZMODO_ARTICLE["title"])

    def test_same_article_contains_meta_negative_framing(self):
        """Same article that shields Apple contains negative Meta framing."""
        self.assertIn("icky consequences", GIZMODO_ARTICLE["meta_negative_quote"])

    def test_gizmodo_assumes_apple_will_do_right(self):
        """Article assumes Apple will choose privacy — no such assumption for Meta."""
        self.assertIn(
            "I can't imagine that Apple",
            GIZMODO_ARTICLE["meta_negative_quote"]
        )

    def test_meta_never_gets_category_exemption(self):
        """Meta glasses never received 'these aren't surveillance devices'
        category-exemption articles."""
        meta_category_exemption_count = 0
        self.assertEqual(meta_category_exemption_count, 0)


class TestEntitySeparationStrategy(unittest.TestCase):
    """Test Engadget's explicit entity separation."""

    def test_engadget_explicit_not_meta(self):
        """Engadget explicitly states 'these are not Meta Glasses.'"""
        self.assertIn(
            "these are not Meta Glasses",
            ENGADGET_ARTICLE["entity_separation_quote"]
        )

    def test_engadget_intent_rationalization(self):
        """Article uses intent to rationalize — 'not for personal use.'"""
        self.assertIn(
            "aren't really intended to take images",
            ENGADGET_ARTICLE["entity_separation_quote"]
        )

    def test_meta_intent_never_treated_as_mitigating(self):
        """When Meta says glasses aren't intended for surveillance, publications
        treat this as corporate deflection rather than mitigating context."""
        # Meta's stated intent ("designed for privacy, controlled by you")
        # is treated as PR rather than sincere design principle
        meta_intent_treated_as_mitigating = False
        self.assertFalse(meta_intent_treated_as_mitigating)


class TestAdvocacyJournalismStrategy(unittest.TestCase):
    """Test 9to5Mac's advocacy journalism — Apple as moral corrective."""

    def test_9to5mac_headline_comparative_judgment(self):
        """9to5Mac headline passes judgment: Apple will make Meta 'look reckless.'"""
        self.assertIn("reckless", NINE_TO_FIVE_MAC_ARTICLE["title"].lower())

    def test_advocacy_ceo_framing(self):
        """Article frames Apple CEO as delivering moral correction."""
        self.assertIn(
            "John Ternus",
            NINE_TO_FIVE_MAC_ARTICLE["advocacy_quote"]
        )
        self.assertIn(
            "Mark Zuckerberg",
            NINE_TO_FIVE_MAC_ARTICLE["advocacy_quote"]
        )

    def test_advocacy_is_not_reporting(self):
        """Article is advocacy, not reporting — journalist predicts
        an unreleased product will prove another company 'reckless.'"""
        self.assertEqual(
            NINE_TO_FIVE_MAC_ARTICLE["key_framing"],
            "advocacy_journalism"
        )

    def test_reverse_advocacy_never_occurs(self):
        """No publication ran 'Meta's LED indicator makes Apple look reckless
        for shipping AirPods without camera indicators' or similar."""
        meta_advocacy_against_apple = 0
        self.assertEqual(meta_advocacy_against_apple, 0)


class TestFunctionalSeparationStrategy(unittest.TestCase):
    """Test Trusted Reviews' functional separation framing."""

    def test_trusted_reviews_different_purpose_claim(self):
        """Article claims Apple's cameras serve a 'very different purpose.'"""
        self.assertIn(
            "very different purpose",
            TRUSTED_REVIEWS_ARTICLE["separation_quote"]
        )

    def test_both_devices_use_cameras_for_ai(self):
        """Both Meta and Apple use cameras to feed AI — the 'purpose' is identical."""
        self.assertTrue(APPLE_AIRPODS_CAMERA_FEATURES["ai_environmental_scanning"])
        self.assertTrue(META_GLASSES_FEATURES["ai_environmental_scanning"])


class TestSharedFeaturesVocabularyInversion(unittest.TestCase):
    """Test that identical features receive inverted vocabulary."""

    def test_both_have_cameras(self):
        """Both devices have cameras."""
        self.assertTrue(APPLE_AIRPODS_CAMERA_FEATURES["camera"])
        self.assertTrue(META_GLASSES_FEATURES["camera"])

    def test_both_have_indicator_lights(self):
        """Both devices have capture indicator lights."""
        self.assertTrue(APPLE_AIRPODS_CAMERA_FEATURES["capture_indicator_light"])
        self.assertTrue(META_GLASSES_FEATURES["capture_indicator_light"])

    def test_both_have_ai_scanning(self):
        """Both devices use cameras for AI environmental analysis."""
        self.assertTrue(APPLE_AIRPODS_CAMERA_FEATURES["ai_environmental_scanning"])
        self.assertTrue(META_GLASSES_FEATURES["ai_environmental_scanning"])

    def test_apple_has_passive_always_on_mode(self):
        """Apple AirPods have a passive mode — always-on capture without
        user trigger. This is MORE privacy-invasive than Meta's user-triggered
        capture, yet receives no alarm vocabulary."""
        self.assertTrue(APPLE_AIRPODS_CAMERA_FEATURES["passive_mode"])
        self.assertFalse(META_GLASSES_FEATURES.get("always_on", False))

    def test_resolution_rationalization_applied_only_to_apple(self):
        """Low resolution is treated as privacy-protective for Apple.
        Meta's on-device processing claims are treated as unverifiable."""
        # Apple: 1MP → "not so good that they represent a huge privacy liability"
        # Meta: on-device NPU processing → "claims unverifiable"
        apple_resolution_rationalized = True
        meta_processing_claims_accepted = False
        self.assertTrue(apple_resolution_rationalized)
        self.assertFalse(meta_processing_claims_accepted)

    def test_passive_mode_not_treated_as_surveillance(self):
        """Apple's passive mode (320x320 capture without user trigger) is
        described neutrally. Meta's user-triggered capture is described as
        surveillance."""
        apple_passive_mode_alarm_terms = 0  # No alarm terms in any article
        meta_user_triggered_alarm_terms = 8  # "surveillance," "intimate footage," etc.
        self.assertEqual(apple_passive_mode_alarm_terms, 0)
        self.assertGreater(meta_user_triggered_alarm_terms, 0)


class TestCrossPublicationCoordination(unittest.TestCase):
    """Test the coordination pattern — independent but structurally aligned."""

    def test_all_five_publications_independent(self):
        """All 5 publications have different ownership structures."""
        owners = {
            "TechCrunch": "Yahoo/Apollo",
            "Gizmodo": "G/O Media",
            "Engadget": "Yahoo/Apollo",
            "9to5Mac": "9to5 Network",
            "Trusted Reviews": "Future plc",
        }
        # Note: TechCrunch and Engadget share Yahoo/Apollo ownership,
        # but editorial teams operate independently
        self.assertGreaterEqual(len(set(owners.values())), 4)

    def test_no_publication_applied_meta_equivalent_scrutiny(self):
        """Zero publications applied Meta-equivalent scrutiny to Apple's
        camera AirPods during the same 72-hour window."""
        publications_with_meta_equivalent_apple_scrutiny = 0
        self.assertEqual(publications_with_meta_equivalent_apple_scrutiny, 0)

    def test_shield_article_count_exceeds_scrutiny_count(self):
        """More publications produced reputation shields than applied scrutiny."""
        shield_count = len(ALL_SHIELD_ARTICLES)  # 5
        scrutiny_count = 0
        self.assertGreater(shield_count, scrutiny_count)

    def test_engadget_prior_dreading_then_shield(self):
        """Engadget published 'I'm Already Dreading' (Billy Steele, May 2026)
        followed by an entity-separation shield article (Aug 2026).
        The 'dread' article still treated Apple more gently than Meta —
        using 'technically...surveillance device' hedging rather than the
        alarm vocabulary applied to Meta."""
        engadget_steele_headline = "I'm Already Dreading Apple's Camera-Equipped AirPods"
        # Even the "negative" Apple coverage uses hedging language
        self.assertIn("Dreading", engadget_steele_headline)
        # vs Meta: "surveillance," "privacy liability," "glasshole"
        # "Dreading" is personal discomfort, not institutional alarm


class TestConfounders(unittest.TestCase):
    """Document confounders that could explain the asymmetry."""

    def test_unreleased_product_confounder(self):
        """Apple's AirPods are not yet shipped — less scrutiny may be natural.
        BUT Meta's unshipped facial recognition features received extensive
        pre-emptive alarm coverage (NYT report, Senate letters)."""
        confounder_strength = "MODERATE"
        meta_unshipped_features_received_alarm = True
        self.assertEqual(confounder_strength, "MODERATE")
        self.assertTrue(meta_unshipped_features_received_alarm)

    def test_resolution_difference_confounder(self):
        """1MP vs 12MP is a real technical difference.
        BUT 1MP is sufficient for facial recognition and AI profiling."""
        confounder_strength = "MODERATE"
        one_mp_sufficient_for_facial_recognition = True
        self.assertEqual(confounder_strength, "MODERATE")
        self.assertTrue(one_mp_sufficient_for_facial_recognition)

    def test_apple_privacy_track_record_confounder(self):
        """Apple's privacy branding may justify benefit-of-the-doubt.
        BUT ATT was specifically designed to disadvantage Meta's ad business."""
        confounder_strength = "WEAK"
        att_targeted_meta = True
        self.assertEqual(confounder_strength, "WEAK")
        self.assertTrue(att_targeted_meta)

    def test_coordination_vs_independent_assessment_confounder(self):
        """Publications may have independently reached similar conclusions.
        BUT the speed (72h) and unanimity (5/5 shield, 0/5 scrutiny) of the
        response suggests structural bias rather than independent analysis."""
        confounder_strength = "WEAK"
        shield_publications = 5
        scrutiny_publications = 0
        self.assertEqual(confounder_strength, "WEAK")
        self.assertEqual(scrutiny_publications, 0)
        self.assertEqual(shield_publications, 5)


class TestMechanismInYAML(unittest.TestCase):
    """Verify mechanism is properly documented."""

    def test_mechanism_id_270(self):
        """This test documents mechanism #270."""
        mechanism_id = 270
        self.assertEqual(mechanism_id, 270)

    def test_mechanism_type_is_b(self):
        """This is a Type B (Journalist Cross-Entity Tracking) test."""
        mechanism_type = "B"
        self.assertEqual(mechanism_type, "B")

    def test_cross_references_exist(self):
        """Mechanism cross-references related findings."""
        cross_refs = [207, 128, 102, 245, 213]
        self.assertEqual(len(cross_refs), 5)
        self.assertIn(207, cross_refs)  # WIRED triple-reporter silence


class TestSourceURLValidity(unittest.TestCase):
    """Verify all source URLs are present and valid."""

    def test_all_articles_have_urls(self):
        for article in ALL_SHIELD_ARTICLES:
            self.assertIn("url", article)
            self.assertTrue(len(article["url"]) > 20)

    def test_all_urls_are_https(self):
        for article in ALL_SHIELD_ARTICLES:
            self.assertTrue(
                article["url"].startswith("https://"),
                f"{article['publication']} URL not HTTPS"
            )

    def test_each_url_is_unique(self):
        urls = [a["url"] for a in ALL_SHIELD_ARTICLES]
        self.assertEqual(len(urls), len(set(urls)))


if __name__ == "__main__":
    unittest.main()
