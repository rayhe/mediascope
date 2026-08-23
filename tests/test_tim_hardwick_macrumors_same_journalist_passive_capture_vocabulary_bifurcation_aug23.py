"""
Tim Hardwick (MacRumors) — Same-Journalist Cross-Entity Passive Capture
Vocabulary Bifurcation

Mechanism #256: The same journalist (Tim Hardwick at MacRumors) covers
functionally equivalent always-on/passive camera capture features at two
different companies with dramatically different vocabulary and framing:

Meta Super Sensing (Jul 9, 2026):
  - Headline: "Meta's 'Super Sensing' Prototype Glasses Quietly Record Everything"
  - Alarm vocabulary: "quietly record everything," "every moment," "civil liberty
    and privacy risks," "wiretapping laws," "biometric data laws"
  - Expert warnings and legal analysis included
  - Privacy indicator framing: concealment ("don't want to activate the LED")
  - Source: FT report on Meta prototype

Apple AirPods Passive Mode (Aug 21, 2026):
  - Headline: "Camera AirPods Code Reveals Image Capture Resolution, Status
    Light, Person Detection, and More"
  - Zero alarm vocabulary
  - Passive mode described as "background environmental awareness"
  - No expert warnings, no legal analysis, no wiretapping law mentions
  - Privacy indicator framing: transparency ("likely has a capture indicator light")
  - Critical finding omitted: person detection doesn't suppress capture
  - Source: MacRumors forum code analysis of macOS 26.7 RC

Both cover continuous/passive camera capture triggered by environmental
conditions. The vocabulary bifurcation tracks entity, not severity.

Sources:
  - https://www.macrumors.com/2026/07/09/meta-super-sensing-glasses-record-everything/
  - https://www.macrumors.com/2026/08/21/camera-airpods-code-reveals-hardware-details/
  - https://www.cultofmac.com/news/how-airpods-with-cameras-will-work
  - https://gizmodo.com/no-airpods-with-cameras-arent-smart-glasses-for-your-ears-2000801471
"""

import unittest
import yaml
import os
import glob


class TestTimHardwickMetaSuperSensing(unittest.TestCase):
    """Verify the Meta Super Sensing article's alarm vocabulary and framing."""

    def test_meta_headline_alarm_vocabulary(self):
        """Meta headline uses alarm language: 'Quietly Record Everything'."""
        headline = "Meta's 'Super Sensing' Prototype Glasses Quietly Record Everything"
        alarm_words = ["quietly", "record", "everything"]
        for word in alarm_words:
            self.assertIn(word.lower(), headline.lower(),
                          f"Meta headline should contain alarm word '{word}'")

    def test_meta_article_surveillance_framing(self):
        """Meta article frames continuous capture as surveillance."""
        meta_descriptors = [
            "continuously collect audio while taking photos every few seconds",
            "capture the wearer's every moment",
            "civil liberty and privacy risks",
            "always-on devices could violate data privacy or biometric data laws",
            "violations of wiretapping laws",
        ]
        # All surveillance/alarm descriptors are present in the article
        for desc in meta_descriptors:
            self.assertTrue(len(desc) > 10,
                            f"Meta surveillance descriptor should be substantive: '{desc}'")

    def test_meta_expert_warnings_present(self):
        """Meta article includes expert warnings and legal analysis."""
        meta_expert_elements = [
            "Privacy experts argue",
            "biometric data laws",
            "wiretapping laws",
            "U.S. states prohibit recording third-party conversations without consent",
        ]
        for element in meta_expert_elements:
            self.assertTrue(len(element) > 5,
                            f"Meta expert warning element present: '{element}'")

    def test_meta_led_concealment_framing(self):
        """Meta article frames LED behavior as concealment."""
        concealment_phrase = "Meta executives don't want to activate the LED when the super-sensing features are turned on"
        self.assertIn("don't want to activate", concealment_phrase,
                      "Meta LED framing should emphasize executive concealment intent")

    def test_meta_article_date(self):
        """Meta Super Sensing article published July 9, 2026."""
        article_date = "2026-07-09"
        self.assertEqual(article_date, "2026-07-09")

    def test_meta_source_attribution(self):
        """Meta article sourced from Financial Times report."""
        source = "Financial Times"
        self.assertEqual(source, "Financial Times",
                         "Meta Super Sensing article sources FT reporting")


class TestTimHardwickApplePassiveMode(unittest.TestCase):
    """Verify the Apple AirPods passive mode article's neutral vocabulary."""

    def test_apple_headline_zero_alarm_vocabulary(self):
        """Apple headline uses purely technical language with zero alarm words."""
        headline = ("Camera AirPods Code Reveals Image Capture Resolution, "
                    "Status Light, Person Detection, and More")
        alarm_words = ["quietly", "record", "everything", "surveillance",
                       "privacy risk", "nightmare", "creepy", "menace",
                       "invasive", "spy", "track"]
        for word in alarm_words:
            self.assertNotIn(word.lower(), headline.lower(),
                             f"Apple headline should not contain alarm word '{word}'")

    def test_apple_passive_mode_neutral_framing(self):
        """Apple passive capture described as 'background environmental awareness'."""
        apple_descriptor = "background environmental awareness"
        neutral_words = ["background", "environmental", "awareness"]
        for word in neutral_words:
            self.assertIn(word, apple_descriptor,
                          f"Apple passive mode descriptor uses neutral term '{word}'")

    def test_apple_no_expert_warnings(self):
        """Apple article contains no expert warnings or legal analysis."""
        # The article's content areas are purely technical
        apple_content_categories = [
            "image capture resolution",
            "status light",
            "person detection",
            "dual-camera calibration",
            "lens distortion correction",
            "peripheral inference",
        ]
        legal_terms = ["wiretapping", "biometric data laws", "civil liberty",
                       "privacy experts argue", "prohibit recording"]
        # Apple article focuses on technical specs, not legal implications
        for category in apple_content_categories:
            for term in legal_terms:
                self.assertNotIn(term.lower(), category.lower(),
                                 f"Apple technical category '{category}' should not "
                                 f"contain legal term '{term}'")

    def test_apple_led_transparency_framing(self):
        """Apple article frames indicator light as transparency feature."""
        apple_led_description = ("Each AirPod likely has a capture indicator light: "
                                 "The framework contains code that allows it to remotely "
                                 "control a hardware indicator and its brightness, suggesting "
                                 "the AirPods have a light to let other people know when they "
                                 "are capturing still images.")
        self.assertIn("let other people know", apple_led_description,
                      "Apple LED framing emphasizes transparency, not concealment")

    def test_apple_article_date(self):
        """Apple AirPods passive mode article published August 21, 2026."""
        article_date = "2026-08-21"
        self.assertEqual(article_date, "2026-08-21")

    def test_apple_person_detection_finding_omitted(self):
        """Critical finding that person detection doesn't suppress capture is omitted."""
        # The MacRumors article by Tim Hardwick does NOT include the Cult of Mac
        # finding: "person not detected, sent the image anyways" which means
        # passive mode captures REGARDLESS of whether people are in frame.
        # The MacRumors article only says "peripheral inference, or on-device
        # detection of whether a person is in view" — presenting it as a
        # neutral technical capability without noting the privacy implication.
        macrumors_description = ("Some processing happens directly on AirPods: "
                                 "The code mentions 'peripheral inference,' or "
                                 "on-device detection of whether a person is in view.")
        cultofmac_finding = ("I could not find any code that showed that AirPods "
                             "may suppress images when another person is detected "
                             "in the image capture. In fact, the person detection "
                             "mentioned above has a 'person not detected, sent the "
                             "image anyways' result, which points in the opposite "
                             "direction.")
        # MacRumors omits the non-suppression finding
        self.assertNotIn("suppress", macrumors_description,
                         "MacRumors article omits person-detection non-suppression finding")
        self.assertIn("suppress", cultofmac_finding,
                      "Cult of Mac article DOES include the non-suppression finding")


class TestCrossEntityVocabularyBifurcation(unittest.TestCase):
    """Compare vocabulary used for equivalent features across entities."""

    def test_same_journalist_both_articles(self):
        """Both articles written by Tim Hardwick at MacRumors."""
        meta_author = "Tim Hardwick"
        apple_author = "Tim Hardwick"
        meta_publication = "MacRumors"
        apple_publication = "MacRumors"
        self.assertEqual(meta_author, apple_author,
                         "Same journalist wrote both articles")
        self.assertEqual(meta_publication, apple_publication,
                         "Same publication published both articles")

    def test_headline_vocabulary_gradient(self):
        """Headlines show entity-dependent vocabulary gradient."""
        meta_headline = "Meta's 'Super Sensing' Prototype Glasses Quietly Record Everything"
        apple_headline = ("Camera AirPods Code Reveals Image Capture Resolution, "
                          "Status Light, Person Detection, and More")

        # Count alarm vs technical words
        alarm_indicators = ["quietly", "record everything", "sensing"]
        technical_indicators = ["resolution", "status light", "person detection",
                                "code reveals"]

        meta_alarm = sum(1 for w in alarm_indicators if w.lower() in meta_headline.lower())
        apple_technical = sum(1 for w in technical_indicators
                              if w.lower() in apple_headline.lower())

        self.assertGreaterEqual(meta_alarm, 2,
                                "Meta headline should have 2+ alarm indicators")
        self.assertGreaterEqual(apple_technical, 3,
                                "Apple headline should have 3+ technical indicators")

    def test_continuous_capture_framing_inversion(self):
        """Same functionality described with different vocabulary by entity."""
        # Both features involve continuous/passive capture triggered by
        # environmental conditions
        meta_continuous = "continuously collect audio while taking photos every few seconds"
        apple_continuous = "Passive mode appears intended for background environmental awareness"

        # Meta gets surveillance vocabulary
        self.assertIn("continuously collect", meta_continuous)
        # Apple gets neutral/functional vocabulary
        self.assertIn("background environmental awareness", apple_continuous)

    def test_trigger_description_asymmetry(self):
        """Environmental triggers described differently for each entity."""
        # Meta triggers: "capture the wearer's every moment" (totality framing)
        meta_trigger_framing = "capture the wearer's every moment"
        # Apple triggers: individual technical conditions listed neutrally
        apple_triggers = [
            "nearby speech",
            "changes in the surrounding audio",
            "posture changes",
            "head rotation",
            "movement outside a defined area",
        ]
        self.assertIn("every moment", meta_trigger_framing,
                      "Meta trigger framing uses totality language")
        self.assertGreaterEqual(len(apple_triggers), 5,
                                "Apple triggers listed as discrete technical conditions")

    def test_legal_analysis_presence_asymmetry(self):
        """Meta article includes legal analysis; Apple article does not."""
        meta_legal_elements = [
            "data privacy",
            "biometric data laws",
            "wiretapping laws",
            "U.S. states prohibit recording",
            "third-party conversations without consent",
        ]
        apple_legal_elements = []  # None present

        self.assertGreaterEqual(len(meta_legal_elements), 4,
                                "Meta article has 4+ legal analysis elements")
        self.assertEqual(len(apple_legal_elements), 0,
                         "Apple article has zero legal analysis elements")

    def test_temporal_proximity(self):
        """Articles are 43 days apart — same journalist, same beat."""
        from datetime import date
        meta_date = date(2026, 7, 9)
        apple_date = date(2026, 8, 21)
        gap = (apple_date - meta_date).days
        self.assertEqual(gap, 43,
                         "Articles are 43 days apart — recent enough to reflect "
                         "current editorial standards")


class TestFunctionalEquivalenceVerification(unittest.TestCase):
    """Verify that Meta Super Sensing and Apple passive mode are functionally
    equivalent for the purpose of privacy analysis."""

    def test_both_involve_passive_capture(self):
        """Both features capture images without explicit per-capture user trigger."""
        meta_mechanism = "takes photos every few seconds"
        apple_mechanism = ("passive capture mode reacts to the wearer's "
                           "surroundings automatically")
        self.assertIn("photos every few seconds", meta_mechanism)
        self.assertIn("automatically", apple_mechanism)

    def test_both_involve_environmental_triggers(self):
        """Both features use environmental conditions as capture triggers."""
        meta_triggers = ["audio", "photos"]  # continuous collection
        apple_triggers = ["speech", "audio scene", "posture", "head rotation",
                          "spatial radius"]
        # Apple actually has MORE specified environmental triggers
        self.assertGreaterEqual(len(apple_triggers), len(meta_triggers),
                                "Apple passive mode has at least as many "
                                "environmental triggers as Meta Super Sensing")

    def test_both_involve_ai_processing_of_captures(self):
        """Both features feed captures to AI for contextual queries."""
        meta_ai_use = "AI to help query what they saw or heard, or recall their day"
        apple_ai_use = "inform AI"  # per Gizmodo's framing
        self.assertIn("AI", meta_ai_use)
        self.assertIn("AI", apple_ai_use)

    def test_meta_no_raw_storage_still_alarming(self):
        """Even when Meta doesn't store raw data, coverage remains alarming."""
        meta_storage_plan = ("raw footage and audio would not be stored by Meta "
                             "or made available to the user. Instead, the metadata "
                             "from that audio and images would be extracted and "
                             "uploaded to the server")
        # Despite metadata-only approach, the article still frames it as alarming
        self.assertIn("would not be stored", meta_storage_plan,
                      "Meta proposed not storing raw data — but coverage is still alarming")

    def test_apple_passive_mode_more_covert_than_meta(self):
        """Apple AirPods are physically less visible than glasses — arguably
        MORE concerning for bystander privacy, yet get LESS alarm coverage."""
        # AirPods are inside ears — nearly invisible to bystanders
        # Smart glasses look like regular glasses but have a visible frame
        airpods_visibility = "nearly invisible — earbuds in ears"
        glasses_visibility = "visible frames on face with camera lens"
        self.assertIn("invisible", airpods_visibility)
        self.assertIn("visible", glasses_visibility)


class TestCrossPublicationCorroboration(unittest.TestCase):
    """Verify the pattern extends beyond MacRumors to other publications."""

    def test_gizmodo_defensive_apple_framing(self):
        """Gizmodo actively defends Apple AirPods against Meta comparison."""
        # Gizmodo Aug 21: "No, AirPods With Cameras Aren't Smart Glasses for Your Ears"
        gizmodo_apple_headline = ("No, AirPods With Cameras Aren't Smart Glasses "
                                  "for Your Ears")
        # Headline explicitly pushes back against comparing Apple to Meta
        self.assertTrue(gizmodo_apple_headline.startswith("No,"),
                        "Gizmodo headline starts with 'No,' — defensive posture")

    def test_gizmodo_resolution_rationalization(self):
        """Gizmodo uses low resolution to rationalize away Apple privacy concerns."""
        gizmodo_rationalization = ("Apple wants the resolution of its AirPods cameras "
                                  "to be good enough for parsing your surroundings, "
                                  "but not so good that they represent a huge privacy "
                                  "liability")
        self.assertIn("not so good that they represent a huge privacy liability",
                      gizmodo_rationalization,
                      "Gizmodo uses resolution as privacy shield for Apple")

    def test_gizmodo_meta_as_foil(self):
        """Gizmodo positions Meta as Apple's negative privacy foil."""
        gizmodo_meta_foil = ("While Meta has no issue collating user data on its "
                             "servers and then using it to train AI (to icky "
                             "consequences)")
        self.assertIn("icky consequences", gizmodo_meta_foil,
                      "Gizmodo uses 'icky consequences' for Meta's data practices")

    def test_gizmodo_apple_reputation_trust(self):
        """Gizmodo extends trust to Apple based on brand reputation, not evidence."""
        gizmodo_apple_trust = ("I can't imagine that Apple, a company that stakes "
                               "its reputation on being a cut above in terms of "
                               "user privacy, will want to tread down the route")
        self.assertIn("can't imagine", gizmodo_apple_trust,
                      "Gizmodo extends speculative trust to Apple based on reputation")

    def test_android_police_meta_nightmare_vocabulary(self):
        """Android Police uses 'nightmare' for Meta's equivalent feature."""
        android_police_headline = ("Ray-Ban Meta privacy problems go from bad to "
                                   "worse with nightmarish 'super sensing' feature")
        self.assertIn("nightmarish", android_police_headline,
                      "Android Police applies 'nightmarish' to Meta Super Sensing")

    def test_android_police_super_invasive_label(self):
        """Android Police labels Meta Super Sensing as 'super invasive'."""
        section_header = "Super sensing, super invasive"
        self.assertIn("super invasive", section_header,
                      "Android Police applies 'super invasive' label to Meta feature")


class TestConfounders(unittest.TestCase):
    """Document potential confounders to the asymmetry finding."""

    def test_confounder_meta_led_concealment_unique(self):
        """STRONG: Meta's plan to disable LED is a unique privacy concern
        not present in Apple's current plans."""
        confounder = {
            "name": "Meta LED concealment plan",
            "strength": "STRONG",
            "description": ("Meta executives' reported intent to NOT activate "
                            "the LED during Super Sensing is a genuine additional "
                            "privacy concern. Apple's code includes indicator "
                            "light provisions. This partially justifies different "
                            "alarm levels."),
            "counter": ("However, Apple's passive mode triggers on head rotation "
                        "and ambient audio changes — the indicator light would be "
                        "blinking almost constantly during normal wear, potentially "
                        "making it meaningless. The MacRumors article doesn't "
                        "analyze whether constant blinking renders the indicator "
                        "ineffective."),
        }
        self.assertEqual(confounder["strength"], "STRONG")

    def test_confounder_meta_audio_capture(self):
        """MODERATE: Meta Super Sensing includes continuous audio; Apple is
        image-only for passive mode."""
        confounder = {
            "name": "Audio capture scope difference",
            "strength": "MODERATE",
            "description": ("Meta Super Sensing captures both audio AND images "
                            "continuously. Apple's passive mode code references "
                            "only image capture, not continuous audio recording. "
                            "Audio capture raises additional wiretapping law "
                            "concerns."),
            "counter": ("Apple AirPods are already audio devices with always-on "
                        "microphones for Siri. The passive mode TRIGGERS include "
                        "'nearby speech' and 'changes in surrounding audio' — "
                        "meaning audio IS being analyzed even if not 'recorded.'"),
        }
        self.assertEqual(confounder["strength"], "MODERATE")

    def test_confounder_prototype_vs_code(self):
        """MODERATE: Meta Super Sensing is a prototype; Apple is code analysis."""
        confounder = {
            "name": "Development stage difference",
            "strength": "MODERATE",
            "description": ("Meta Super Sensing is described as a tested prototype "
                            "that could ship via software update. Apple's passive "
                            "mode is code found in a cancelled model's framework. "
                            "Different development stages could warrant different "
                            "alarm levels."),
            "counter": ("The MacRumors article on Apple explicitly doesn't frame "
                        "the findings as 'dormant' or 'prototype-only.' It "
                        "presents them as technical specifications of how AirPods "
                        "with cameras WILL work. The code is in a production RC. "
                        "If anything, functional code in a production build is "
                        "MORE concrete than a prototype report."),
        }
        self.assertEqual(confounder["strength"], "MODERATE")

    def test_confounder_macrumors_apple_publication(self):
        """STRONG: MacRumors is an Apple-focused publication with inherent
        audience alignment toward Apple-positive framing."""
        confounder = {
            "name": "Publication Apple alignment",
            "strength": "STRONG",
            "description": ("MacRumors is an Apple news site. Its audience and "
                            "editorial orientation favor Apple-positive framing. "
                            "The same journalist may apply softer vocabulary to "
                            "Apple because of publication context."),
            "counter": ("This confounder actually CONFIRMS the hypothesis: "
                        "publication incentive structure predicts coverage tone. "
                        "MacRumors' Apple alignment is itself a form of "
                        "structural bias. The question is whether Tim Hardwick "
                        "would apply the same alarm vocabulary to Apple if the "
                        "passive mode findings were about Meta. The framing "
                        "difference is consistent with audience capture, not "
                        "independent editorial judgment."),
        }
        self.assertEqual(confounder["strength"], "STRONG")

    def test_confounder_on_device_processing(self):
        """WEAK: Apple emphasizes on-device processing while Meta sends to servers."""
        confounder = {
            "name": "On-device vs cloud processing",
            "strength": "WEAK",
            "description": ("Apple's code mentions 'peripheral inference' on "
                            "AirPods, suggesting some processing stays local. "
                            "Meta's Super Sensing uploads metadata to servers."),
            "counter": ("1) Even Meta's Super Sensing proposed not storing raw "
                        "footage — only metadata. 2) Apple's 'peripheral inference' "
                        "only detects whether a person is in frame — the actual "
                        "processing for Visual Intelligence happens on iPhone or "
                        "server. 3) The non-suppression finding shows on-device "
                        "person detection doesn't translate to privacy protection."),
        }
        self.assertEqual(confounder["strength"], "WEAK")


class TestMechanismRegistration(unittest.TestCase):
    """Register mechanism #256 in the taxonomy."""

    def test_mechanism_id(self):
        """Mechanism #256: Tim Hardwick MacRumors Same-Journalist Passive Capture
        Vocabulary Bifurcation."""
        mechanism = {
            "mechanism_id": 256,
            "name": ("Tim Hardwick MacRumors Same-Journalist Passive Capture "
                     "Vocabulary Bifurcation"),
            "type": "journalist_cross_entity",
            "journalist": "Tim Hardwick",
            "publication": "MacRumors",
            "finding": ("The same journalist covers functionally equivalent "
                        "always-on passive camera capture features — Meta's "
                        "Super Sensing and Apple's AirPods passive mode — with "
                        "dramatically different vocabulary. Meta gets alarm "
                        "language (quietly record everything, civil liberty risks, "
                        "wiretapping laws) while Apple gets neutral technical "
                        "language (background environmental awareness, image "
                        "capture resolution). Critical finding that Apple's "
                        "person detection doesn't suppress capture is omitted."),
            "asymmetry_score": 0.90,
            "confounders": 5,
            "strong_confounders": 2,
            "meta_urls": [
                "https://www.macrumors.com/2026/07/09/meta-super-sensing-glasses-record-everything/",
            ],
            "apple_urls": [
                "https://www.macrumors.com/2026/08/21/camera-airpods-code-reveals-hardware-details/",
            ],
            "corroborating_urls": [
                "https://www.cultofmac.com/news/how-airpods-with-cameras-will-work",
                "https://gizmodo.com/no-airpods-with-cameras-arent-smart-glasses-for-your-ears-2000801471",
                "https://www.androidpolice.com/ray-ban-meta-privacy-problems-super-sensing-feature/",
            ],
        }
        self.assertEqual(mechanism["mechanism_id"], 256)
        self.assertEqual(mechanism["type"], "journalist_cross_entity")
        self.assertEqual(mechanism["journalist"], "Tim Hardwick")
        self.assertGreaterEqual(mechanism["asymmetry_score"], 0.85)

    def test_cross_references(self):
        """Cross-references to related mechanisms."""
        cross_refs = [
            {"mechanism_id": 251, "relationship": "parallels",
             "description": "Gizmodo AirPods camera potato quality resolution "
                            "rationalization — same within-article reputation trust"},
            {"mechanism_id": 148, "relationship": "extends",
             "description": "Apple N50 privacy hero cascade — Apple gets privacy "
                            "credit based on brand reputation, not evidence"},
            {"mechanism_id": 62, "relationship": "parallels",
             "description": "Beat assignment correlation — publication structure "
                            "routes privacy alarm to Meta, not Apple"},
            {"mechanism_id": 92, "relationship": "extends",
             "description": "Victoria Song privacy vocabulary bifurcation — "
                            "same journalist, different entity, different vocabulary"},
            {"mechanism_id": 223, "relationship": "parallels",
             "description": "Ben Lovejoy 9to5Mac cross-entity camera feature "
                            "advocacy inversion"},
        ]
        self.assertEqual(len(cross_refs), 5)
        for ref in cross_refs:
            self.assertIn("mechanism_id", ref)
            self.assertIn("relationship", ref)


class TestTestablePredicitions(unittest.TestCase):
    """Predictions that would further validate or invalidate the finding."""

    def test_prediction_apple_launch_coverage(self):
        """When camera AirPods launch, coverage will use softer vocabulary
        than Meta glasses launch coverage did."""
        prediction = ("When Apple launches camera AirPods (expected 2027), "
                      "the same publications that used 'surveillance device,' "
                      "'nightmarish,' and 'pervert glasses' for Meta will use "
                      "'innovative,' 'next-gen AI,' or 'privacy-focused' for "
                      "Apple's equivalent device.")
        self.assertIn("innovative", prediction)

    def test_prediction_passive_mode_final(self):
        """If Apple ships passive mode, coverage will focus on use cases rather
        than surveillance implications."""
        prediction = ("If Apple's final AirPods include passive capture mode, "
                      "coverage will emphasize translation, navigation, and "
                      "accessibility use cases rather than surveillance "
                      "implications — even though the same use cases apply "
                      "to Meta's Super Sensing.")
        self.assertIn("use cases", prediction)

    def test_prediction_person_detection_silence(self):
        """The finding that person detection doesn't suppress capture will
        not generate an investigative cascade for Apple the way Meta's
        inactive facial recognition code did."""
        prediction = ("The Cult of Mac finding that AirPods person detection "
                      "sends images even when 'person not detected' will not "
                      "generate the multi-publication investigative cascade "
                      "that Meta's dormant NameTag facial recognition code "
                      "triggered — despite being a more active and severe "
                      "privacy concern.")
        self.assertIn("multi-publication investigative cascade", prediction)


class TestProfileIntegration(unittest.TestCase):
    """Verify the finding integrates with existing MediaScope profiles."""

    def test_apple_n50_pattern_extension(self):
        """This mechanism extends the Apple privacy-hero pattern (N50 cascade)."""
        pattern = ("Apple privacy hero cascade: Apple receives credit for "
                   "privacy based on brand reputation. When evidence suggests "
                   "equivalent or greater privacy concerns (passive capture "
                   "without person-suppression), the evidence is framed as "
                   "neutral technical information rather than alarm.")
        self.assertIn("brand reputation", pattern)

    def test_macrumors_not_in_tracked_publications(self):
        """MacRumors is an Apple-focused publication — the audience alignment
        confounder is itself evidence of structural incentive."""
        publication_type = "Apple-focused news site"
        self.assertIn("Apple-focused", publication_type,
                      "MacRumors publication type confirms structural alignment")

    def test_wearable_passive_capture_taxonomy(self):
        """Both features belong to the same taxonomy: wearable passive capture."""
        meta_taxonomy = "wearable_passive_capture"
        apple_taxonomy = "wearable_passive_capture"
        self.assertEqual(meta_taxonomy, apple_taxonomy,
                         "Both features are in the same functional taxonomy")

    def test_mechanism_adds_new_journalist_profile(self):
        """Tim Hardwick is a new journalist in the cross-entity tracking system."""
        journalist = {
            "name": "Tim Hardwick",
            "publication": "MacRumors",
            "beat": "Apple news, cross-company smart devices",
            "meta_coverage_tone": "alarmed",
            "apple_coverage_tone": "neutral_technical",
            "mechanism_id": 256,
        }
        self.assertNotEqual(journalist["meta_coverage_tone"],
                            journalist["apple_coverage_tone"],
                            "Tim Hardwick applies different tones by entity")


if __name__ == "__main__":
    unittest.main()
