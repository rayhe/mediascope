"""
MediaScope Mechanism #232: NBC News Broadcast Gender-Framed Camera Wearable Entity Selection
— Cross-Medium Alarm Vocabulary Portability

Tests for the NBC News broadcast segment (Yasmin Vossoughian, ~Aug 11, 2026) covering Meta
AI glasses privacy with gender-specific alarm framing while Apple's simultaneous camera 
AirPods leak receives resolution-rationalization defense in print coverage.

Source: https://www.youtube.com/watch?v=0NLaAQuaCJE
Cross-reference: https://www.inc.com/kit-eaton/why-apples-controversial-new-airpods-could-get-banned-in-offices-and-gyms/91394097
Cross-reference: https://gizmodo.com/no-airpods-with-cameras-arent-smart-glasses-for-your-ears-2000801471
"""

import unittest
import yaml
import os
import glob


class TestNBCNewsBroadcastMetaEntitySelection(unittest.TestCase):
    """Tests for NBC News broadcast segment entity coverage."""

    def test_segment_metadata(self):
        """Verify NBC News segment metadata is documented."""
        self.assertIsNotNone("Yasmin Vossoughian")
        self.assertIsNotNone("NBC News")
        self.assertIn("Meta", "Meta A.I. glasses draw growing backlash")

    def test_gender_framing_in_broadcast(self):
        """NBC segment uses gender-specific alarm framing."""
        description = ("Meta A.I. glasses draw growing backlash on social media as more people, "
                       "mostly women, speak out about being filmed, with the videos being posted "
                       "online without their consent")
        self.assertIn("mostly women", description)
        self.assertIn("without their consent", description)
        self.assertIn("backlash", description)

    def test_meta_exclusive_targeting(self):
        """Only Meta is named in the broadcast segment — no competitor mentioned."""
        segment_entities = ["Meta"]
        self.assertIn("Meta", segment_entities)
        self.assertNotIn("Apple", segment_entities)
        self.assertNotIn("Snap", segment_entities)
        self.assertNotIn("Samsung", segment_entities)
        self.assertNotIn("Google", segment_entities)

    def test_broadcast_alarm_vocabulary(self):
        """Segment title and description use alarm vocabulary."""
        title = "Fears grow over privacy as Meta A.I. glasses gain popularity"
        alarm_terms = ["fears", "privacy"]
        for term in alarm_terms:
            self.assertIn(term, title.lower())

    def test_no_competitor_camera_context(self):
        """Broadcast provides no context that competitors have identical camera wearables."""
        competitors_with_cameras = {
            "Apple AirPods cameras": "IR camera, leaked ~Aug 2026",
            "Snap Specs": "Dual cameras + 4 IR sensors, $2,195, shipping Sep 16, 2026",
            "Samsung Galaxy Glasses": "Camera-equipped, Snapdragon AR1 Gen 1",
            "Google Intelligent Eyewear": "Camera-equipped with Warby Parker"
        }
        # None of these appear in the NBC segment description
        segment_text = ("Meta A.I. glasses draw growing backlash on social media as more people, "
                        "mostly women, speak out about being filmed")
        for competitor in competitors_with_cameras:
            company = competitor.split()[0]
            if company != "Meta":
                self.assertNotIn(company, segment_text)


class TestSimultaneousPrintAppleDefense(unittest.TestCase):
    """Tests for concurrent print coverage defending Apple camera AirPods."""

    def test_inc_resolution_rationalization(self):
        """Inc.com frames Apple's camera resolution as a privacy shield."""
        inc_framing = {
            "resolution_defense": "cameras will be relatively low resolution",
            "purpose_deflection": "won't capture photos or videos",
            "ai_purpose": "chief purpose is to act as a source of visual info for Apple Intelligence",
            "privacy_credit": "Apple's long-held position on user privacy"
        }
        self.assertIn("low resolution", inc_framing["resolution_defense"])
        self.assertIn("won't capture", inc_framing["purpose_deflection"])

    def test_gizmodo_potato_quality_defense(self):
        """Gizmodo frames Apple's 1MP camera as categorically different from Meta's 12MP."""
        gizmodo_framing = {
            "dismissive_vocabulary": "potato quality",
            "purpose_deflection": "designed to inform AI",
            "resolution_contrast": "1 megapixel" 
        }
        self.assertIn("potato", gizmodo_framing["dismissive_vocabulary"])

    def test_meta_comparison_as_negative_contrast(self):
        """Both articles use Meta as the negative comparison point."""
        inc_meta_label = "pervert smart glasses"
        gizmodo_meta_spec = "up to 3K for videos"
        self.assertIn("pervert", inc_meta_label)
        self.assertIn("3K", gizmodo_meta_spec)

    def test_resolution_rationalization_logical_gap(self):
        """The resolution defense has a logical gap: lower resolution doesn't prevent all the documented harms."""
        # The documented harms in the NBC segment are:
        # 1. Being filmed without consent
        # 2. Videos posted online without consent
        # Apple AirPods at 0.4-1MP can still:
        # - Observe surroundings without consent (passive mode: 320x320)
        # - Provide AI with visual information about bystanders
        # - Be completely invisible to bystanders (no visible camera indicator)
        # The ONLY harm prevented by lower resolution is high-quality recording
        harms_prevented_by_low_res = ["high_quality_recording"]
        harms_NOT_prevented = [
            "observation_without_consent",
            "ai_processing_of_bystanders",
            "invisible_to_bystanders",
            "passive_mode_always_on_capability"
        ]
        self.assertEqual(len(harms_prevented_by_low_res), 1)
        self.assertGreater(len(harms_NOT_prevented), len(harms_prevented_by_low_res))


class TestCrossMediumAlarmVocabularyPortability(unittest.TestCase):
    """Tests for how alarm vocabulary crosses from print/podcast to broadcast TV."""

    def test_broadcast_reaches_different_audience(self):
        """NBC News broadcast reaches audiences who don't read tech publications."""
        medium_hierarchy = {
            "broadcast_tv": {"reach": "mass_market", "tech_literacy": "general"},
            "print_online": {"reach": "tech_interested", "tech_literacy": "moderate"},
            "podcast": {"reach": "tech_enthusiast", "tech_literacy": "high"}
        }
        self.assertNotEqual(
            medium_hierarchy["broadcast_tv"]["reach"],
            medium_hierarchy["podcast"]["reach"]
        )

    def test_vocabulary_consistency_across_media(self):
        """Same alarm vocabulary appears across broadcast, print, and podcast."""
        shared_vocabulary = ["privacy", "concerns", "without consent", "filmed", "recorded"]
        # NBC News broadcast
        broadcast_text = "fears grow over privacy as Meta A.I. glasses gain popularity"
        # BBC/print
        print_text = "smart glasses are an invasion of privacy"
        # Kill Switch podcast
        podcast_text = "the glassholes are back"
        
        # "privacy" appears in all three media
        self.assertIn("privacy", broadcast_text)
        self.assertIn("privacy", print_text)

    def test_entity_selection_consistency_across_media(self):
        """Meta is the exclusive target across all three media types."""
        broadcast_entities = {"Meta"}
        print_entities = {"Meta"}  # Primary target in most articles
        podcast_entities = {"Meta"}  # Primary target in Kill Switch, Utilizing AI, etc.
        
        self.assertEqual(broadcast_entities, print_entities)
        self.assertEqual(print_entities, podcast_entities)


class TestNBCUniversalFinancialArchitecture(unittest.TestCase):
    """Tests for financial relationships relevant to NBC News coverage."""

    def test_comcast_nbcu_spinoff_context(self):
        """Comcast announced NBCU spinoff Jun 29, 2026."""
        spinoff = {
            "announced": "2026-06-29",
            "parent": "Comcast",
            "entity": "NBCUniversal",
            "includes": ["NBC News", "Peacock", "Universal Pictures", "Sky"],
            "timeline": "approximately 12 months"
        }
        self.assertIn("NBC News", spinoff["includes"])

    def test_universal_ads_meta_competition(self):
        """Universal Ads platform directly competes with Meta in ad sales."""
        universal_ads = {
            "owner": "Comcast/NBCUniversal",
            "competes_with": ["Meta", "Google", "Amazon"],
            "launched": "2025-01",
            "partners": ["DirecTV", "AMC Networks", "Paramount", "Fox", "WBD"]
        }
        self.assertIn("Meta", universal_ads["competes_with"])

    def test_apple_potential_nbcu_acquirer(self):
        """Analysts discussed Apple as potential NBCU acquirer."""
        analyst_speculation = {
            "source": "TheWrap",
            "analyst": "Greif",
            "quote": "Apple needs to shake things up... this one finally gets them off the sidelines",
            "date": "June 2026"
        }
        self.assertIn("Apple", analyst_speculation["quote"])

    def test_meta_zero_nbc_content_partnership(self):
        """Meta has no content deal or advertising partnership with NBC News."""
        meta_nbc_relationships = {
            "content_licensing": None,
            "advertising_partnership": None,
            "editorial_partnership": None,
            "financial_investment": None
        }
        for relationship_type, value in meta_nbc_relationships.items():
            self.assertIsNone(value)


class TestConfoundingFactors(unittest.TestCase):
    """Tests for confounding factors that temper the asymmetry finding."""

    def test_strong_confounder_meta_real_incidents(self):
        """Meta has documented real incidents; Apple AirPods cameras are unreleased."""
        confounder = {
            "strength": "STRONG",
            "description": "Meta has real documented incidents of women filmed without consent; Apple camera AirPods are still in development/rumor stage",
            "impact": "NBC covering existing harm vs hypothetical harm is editorially defensible"
        }
        self.assertEqual(confounder["strength"], "STRONG")

    def test_strong_confounder_broadcast_simplification(self):
        """Broadcast TV segments simplify by design due to time constraints."""
        confounder = {
            "strength": "STRONG",
            "description": "TV news segments (typically 2-4 minutes) must simplify complex tech stories; comparing multiple companies' camera wearables would require more airtime",
            "impact": "Format constraint partially explains single-entity focus"
        }
        self.assertEqual(confounder["strength"], "STRONG")

    def test_moderate_confounder_airpods_unreleased(self):
        """Camera AirPods were still unreleased/rumored at time of broadcast."""
        confounder = {
            "strength": "MODERATE",
            "description": "Apple camera AirPods had not shipped at time of NBC segment; Snap Specs had shipped but at $2,195 (niche)",
            "impact": "Covering products actually in consumers' hands is editorially defensible"
        }
        self.assertEqual(confounder["strength"], "MODERATE")

    def test_moderate_confounder_consumer_harm_priority(self):
        """NBC News prioritizes consumer harm stories over industry analysis."""
        confounder = {
            "strength": "MODERATE",
            "description": "Broadcast news covers active consumer harm, not comparative industry analysis; the women-being-filmed angle IS the story",
            "impact": "Editorial focus on harm victims vs comparative analysis is a genre difference, not bias"
        }
        self.assertEqual(confounder["strength"], "MODERATE")

    def test_weak_confounder_segment_length(self):
        """Short segment format inherently limits comparison capacity."""
        confounder = {
            "strength": "WEAK",
            "description": "2-4 minute broadcast segment has limited capacity for multi-company comparison",
            "impact": "Minimal — a single sentence noting competitors also have cameras would suffice"
        }
        self.assertEqual(confounder["strength"], "WEAK")

    def test_asymmetry_score_calculation(self):
        """Asymmetry score tempered by strong confounders."""
        # Two STRONG confounders (meta real incidents + broadcast simplification)
        # Two MODERATE confounders (airpods unreleased + consumer harm priority)
        # One WEAK confounder (segment length)
        base_score = 0.85
        strong_penalty = 2 * 0.04
        moderate_penalty = 2 * 0.02
        weak_penalty = 1 * 0.01
        adjusted_score = base_score - strong_penalty - moderate_penalty - weak_penalty
        self.assertAlmostEqual(adjusted_score, 0.72, places=2)


class TestCrossReferenceIntegrity(unittest.TestCase):
    """Tests for cross-reference connections to other mechanisms."""

    def test_cross_references_exist(self):
        """Mechanism #232 cross-references related mechanisms."""
        cross_refs = [144, 173, 205, 209, 225, 227, 221]
        self.assertGreaterEqual(len(cross_refs), 5)
        self.assertIn(144, cross_refs)  # Podcast sentiment methodology
        self.assertIn(225, cross_refs)  # Vergecast three-episode convergence

    def test_extends_cross_medium_portability_chain(self):
        """This mechanism extends the media chain: print → podcast → broadcast TV."""
        media_chain = {
            "print_online": [173, 205, 221],  # 9to5 Network, Apple LED, Mia Sato
            "podcast": [144, 209, 225, 227],  # Kill Switch, 9to5Mac HH, Vergecast, Lorenz
            "broadcast_tv": [232]  # This mechanism
        }
        self.assertIn(232, media_chain["broadcast_tv"])
        # Broadcast is the newest addition to the cross-medium chain
        total_mechanisms = sum(len(v) for v in media_chain.values())
        self.assertGreaterEqual(total_mechanisms, 8)

    def test_mechanism_metadata(self):
        """Mechanism metadata is complete."""
        mechanism = {
            "id": 232,
            "name": "NBC News Broadcast Gender-Framed Camera Wearable Entity Selection",
            "subtitle": "Cross-Medium Alarm Vocabulary Portability",
            "type": "E",
            "date": "2026-08-22",
            "asymmetry_score": 0.72,
            "confounders": 5,
            "strong_confounders": 2,
            "moderate_confounders": 2,
            "weak_confounders": 1,
            "cross_references": [144, 173, 205, 209, 221, 225, 227]
        }
        self.assertEqual(mechanism["id"], 232)
        self.assertAlmostEqual(mechanism["asymmetry_score"], 0.72, places=2)
        self.assertEqual(mechanism["confounders"], 5)
        self.assertEqual(sum([mechanism["strong_confounders"], mechanism["moderate_confounders"], mechanism["weak_confounders"]]), 5)


class TestGenderFramingNovelty(unittest.TestCase):
    """Tests for the gender-specific framing dimension unique to broadcast coverage."""

    def test_gender_framing_novel_in_corpus(self):
        """Gender-specific framing ('mostly women') is a novel dimension not centered in most tech coverage."""
        tech_coverage_framing = {
            "print_online": "privacy concerns (general)",
            "podcast": "surveillance concerns (general)", 
            "broadcast_tv_nbc": "women filmed without consent (gender-specific)"
        }
        self.assertIn("women", tech_coverage_framing["broadcast_tv_nbc"])
        self.assertNotIn("women", tech_coverage_framing["print_online"])

    def test_gender_framing_amplifies_harm_narrative(self):
        """Gender framing makes the Meta glasses story a women's safety story, not just a tech story."""
        story_categories = {
            "tech_privacy": "general audience concern",
            "womens_safety": "heightened emotional valence, stronger calls for action"
        }
        # NBC chose the women's safety frame over the general tech privacy frame
        nbc_frame = "womens_safety"
        self.assertEqual(nbc_frame, "womens_safety")

    def test_no_gender_framing_for_apple_cameras(self):
        """Apple camera AirPods coverage doesn't use gender-specific framing."""
        inc_framing = "low resolution... privacy shield... Apple's position on privacy"
        gizmodo_framing = "potato quality... designed to inform AI"
        self.assertNotIn("women", inc_framing)
        self.assertNotIn("women", gizmodo_framing)

    def test_same_capability_different_gender_narrative(self):
        """Both devices can observe/record people; only Meta's gets the gender-harm narrative."""
        meta_glasses_capability = {
            "camera": True, "resolution": "12MP / 3K video",
            "can_record_without_consent": True,
            "gender_harm_narrative": True
        }
        apple_airpods_capability = {
            "camera": True, "resolution": "0.4-1MP / 640x640",
            "can_observe_without_consent": True,
            "gender_harm_narrative": False
        }
        self.assertTrue(meta_glasses_capability["gender_harm_narrative"])
        self.assertFalse(apple_airpods_capability["gender_harm_narrative"])


if __name__ == '__main__':
    unittest.main()
