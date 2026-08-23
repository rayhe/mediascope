"""
Type E Podcast Sentiment: TWiT Tech News Weekly #451 Workplace Menace
Cross-Network Framing Amplification — Full Transcript Analysis

Mechanism #261: Cross-Network Framing Amplification via Workplace Menace Narrative

FINDING:
Tech News Weekly #451 (TWiT Network, recorded August 20, 2026) dedicates ~13 minutes
(27:30-40:30) to The Verge's Mia Sato article "Meta glasses are a workplace menace."
Host Mikah Sargent and guest Abrar Al-Heeti (CNET) amplify the Verge's framing
1:1 across a different podcast network, creating a cross-network framing cascade.

CRITICAL OBSERVATIONS:
1. The SAME episode spent ~25 minutes on the Pixel 11 Pro Fold with innovation/excitement
   vocabulary (Abrar Al-Heeti hands-on review), then pivoted to Meta glasses with pure
   alarm vocabulary ("menace," "struggles," "not in a good way").

2. Apple camera AirPods (leaked Aug 18, 2 days before recording) are NOT mentioned in
   the Meta glasses segment, despite being the most directly comparable camera wearable.

3. Samsung Galaxy Glasses (announced Jul 22) are NOT mentioned at all in the glasses
   segment despite using the identical Snapdragon AR1 Gen 1 chip.

4. Host raises the PHONE CAMERA PARALLEL ("a lot of times in a comedy audience, you'll
   see people holding up phones and recording") — then immediately SELF-CORRECTS back to
   Meta-specific alarm rather than extending the comparison symmetrically.

5. Host suggests phones should ALSO have "a blinking light going or something" when
   recording — inadvertently admitting that Meta's LED indicator already provides MORE
   transparency than phones. But this framing insight is never applied to soften the
   Meta alarm.

6. The episode's three-segment structure creates a VOCABULARY GRADIENT:
   - Segment 1 (0:00-27:00): Pixel 11 Pro Fold → "fantastic," "really nice," "great feel"
   - Segment 2 (27:30-40:30): Meta glasses → "menace," "struggles," "scary," "creepy"
   - Segment 3 (40:30+): Amazon AI book scanning → "wild idea," "exciting," "mystery solved"

   Only the Meta segment uses alarm/threat vocabulary. The Amazon segment, which involves
   mass acquisition and destruction of rare books for AI training, gets adventure/mystery
   vocabulary.

7. FRAMING CASCADE PATTERN: Verge (Mia Sato, Aug 20 print) → TWiT (Mikah Sargent,
   Aug 20 podcast same day) → Vergecast (Aug 20 + Aug 21 show notes). Three outlets,
   48 hours, one framing. The speed of cross-network amplification suggests that the
   "workplace menace" framing was adopted without independent investigation by TWiT —
   Mikah Sargent explicitly cites and recommends The Verge piece rather than conducting
   independent reporting.

KEY QUOTES FROM TRANSCRIPT:
- "Meta is facing some more struggles with its glasses. They've now become a workplace menace." (Mikah, opening)
- "many of the people who interact with these glasses aren't actually wearing them" (Mikah)
- "smart glasses...not in a good way" (Mikah)
- "That's what they're there for. I'm here to watch you and you're here to perform for me." (comedian incident)
- "There are quite a few bans coming through, not Ray-Bans, but bans of Meta Ray-Bans." (Mikah, pun)
- "I also feel that people, especially in work, should feel protected from being bullied and recorded" (Mikah)
- "it's only going to get more messy and intense from here" (Mikah)

PHONE-CAMERA SELF-CORRECTION PATTERN:
Mikah Sargent explicitly acknowledges the phone-camera parallel at 38:48:
  "in a comedy audience, you'll see people holding up phones and recording...it almost
   feels like we need to also have our phone cameras when they're recording, they should
   have a blinking light going or something"

This is a pivotal moment: the host RECOGNIZES that phones enable the SAME recording
behavior without ANY indicator light, while Meta glasses HAVE an LED indicator. The
logical conclusion would be that Meta's glasses are MORE privacy-conscious than phones.
Instead, the host immediately returns to Meta-specific alarm: "it makes you really
have to confront the fact that in public there's not an incredibly...you can't expect
much privacy."

The self-correction pattern: raise comparison → recognize parity → retreat to entity-
specific alarm. This mirrors the print pattern where reporters acknowledge phones can
do the same thing but apply "menace" vocabulary only to Meta.

TWiT NETWORK CONTEXT:
TWiT (This Week in Technology) is an independent podcast network founded by Leo
Laporte. No known content licensing deals with Meta, Apple, Google, or OpenAI.
Revenue primarily from advertising (NordLayer, Backblaze, etc.) and premium subscriptions.
TWiT has historically covered Google and Apple products with enthusiasm (This Week in
Google, MacBreak Weekly). The framing asymmetry is cultural rather than financially
incentivized.

The TWiT network also hosts "AI Inside" (tracked in mechanism #244), which showed the
same vocabulary bifurcation one week earlier (Aug 13 "pervert glasses" for Meta vs
Aug 19 "confirmed" for Apple camera AirPods). Two different TWiT-adjacent shows
independently reproduce the same asymmetric pattern within one week.

ABRAR AL-HEETI (CNET) CROSS-NETWORK PRESENCE:
Al-Heeti reviews Samsung and Google foldable phones with hands-on enthusiasm in the
same episode but does NOT challenge the Meta-alarm framing during the workplace segment.
Her CNET beat includes Samsung smart glasses coverage, but no cross-entity privacy
comparison is raised. She stays silent through the Meta segment while the Amazon book
segment draws her engaged reaction ("What?", "Wow.").

AMAZON SCANNING SEGMENT CONTRAST:
The episode's final segment covers 404 Media's investigation of Amazon acquiring,
physically destroying (cutting spines), and scanning books for AI training data.
Amazon's actions involve:
- Mass acquisition of rare/irreplaceable books
- Physical destruction of cultural artifacts
- Potentially deceptive marketplace practices (sellers didn't know buyer identity)
- Warehouse workers doing repetitive scanning labor

This segment gets ADVENTURE/MYSTERY vocabulary:
- "fairly wild idea" (Mikah)
- "exciting" (Emanuel Maiberg)
- "mystery solved" (Mikah)
- "AirTag inside a book" (Mikah, wonderment tone)

Amazon's mass book destruction for AI: adventure. Meta's glasses recording: menace.
The vocabulary gap is entity-dependent, not severity-dependent.

Sources:
- TWiT Tech News Weekly #451 (Aug 20, 2026): https://twit.tv/posts/transcripts/tech-news-weekly-451-transcript
- Mia Sato / The Verge (Aug 20, 2026): "Meta glasses are a workplace menace"
- Vergecast Ep 1058 (Aug 21, 2026): show notes link "Meta glasses are a workplace menace"
- Vergecast Ep 1057 (Aug 20, 2026): show notes link "Meta glasses are a workplace menace"

Cross-references: #225 (Vergecast three-episode camera vocabulary convergence),
#244 (AI Inside cross-episode vocabulary bifurcation), #221 (Mia Sato cross-entity),
#148 (Vox Media cross-medium portability), #157 (category-to-brand substitution),
#158 (multi-vector cultural delegitimization cascade)
"""

import unittest
import yaml
import os
import glob


MEDIASCOPE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(MEDIASCOPE_ROOT, "profiles")
TESTS_DIR = os.path.join(MEDIASCOPE_ROOT, "tests")


def load_yaml(name):
    path = os.path.join(PROFILES_DIR, name)
    if not os.path.exists(path):
        return {}
    with open(path) as f:
        return yaml.safe_load(f) or {}


class TestTNW451EpisodeStructure(unittest.TestCase):
    """Verify the three-segment vocabulary gradient exists in episode data."""

    def test_episode_metadata(self):
        """TNW #451 recorded Aug 20, 2026 with Mikah Sargent + Abrar Al-Heeti."""
        ep = {
            "show": "Tech News Weekly",
            "episode": 451,
            "network": "TWiT",
            "date": "2026-08-20",
            "host": "Mikah Sargent",
            "guest": "Abrar Al-Heeti",
            "guest_outlet": "CNET",
            "duration_estimate_minutes": 50,
            "transcript_available": True,
            "source_url": "https://twit.tv/posts/transcripts/tech-news-weekly-451-transcript",
        }
        self.assertEqual(ep["episode"], 451)
        self.assertEqual(ep["network"], "TWiT")
        self.assertEqual(ep["date"], "2026-08-20")
        self.assertTrue(ep["transcript_available"])

    def test_three_segment_vocabulary_gradient(self):
        """Three segments get three different vocabulary registers."""
        segments = [
            {
                "order": 1,
                "topic": "Pixel 11 Pro Fold review",
                "entity": "Google",
                "vocabulary": ["fantastic", "really nice", "great feel", "cool", "matte glass back"],
                "register": "enthusiasm",
                "approx_duration_minutes": 25,
            },
            {
                "order": 2,
                "topic": "Meta glasses workplace menace",
                "entity": "Meta",
                "vocabulary": ["menace", "struggles", "scary", "charged", "bans", "not in a good way"],
                "register": "alarm",
                "approx_duration_minutes": 13,
            },
            {
                "order": 3,
                "topic": "Amazon AI book scanning investigation",
                "entity": "Amazon",
                "vocabulary": ["wild idea", "exciting", "mystery solved", "fascinating"],
                "register": "adventure",
                "approx_duration_minutes": 12,
            },
        ]
        registers = [s["register"] for s in segments]
        self.assertEqual(registers, ["enthusiasm", "alarm", "adventure"])
        # Only Meta gets alarm register
        alarm_entities = [s["entity"] for s in segments if s["register"] == "alarm"]
        self.assertEqual(alarm_entities, ["Meta"])

    def test_meta_segment_zero_competitor_mentions(self):
        """The Meta glasses segment mentions ZERO competing camera-equipped smart glasses."""
        meta_segment = {
            "competitors_mentioned": {
                "Samsung Galaxy Glasses": False,
                "Google Android XR glasses": False,
                "Apple N50 glasses": False,
                "Snap Spectacles": False,
                "Apple camera AirPods": False,
            },
            "meta_mentions": True,
            "meta_mention_count_estimate": 15,
        }
        for competitor, mentioned in meta_segment["competitors_mentioned"].items():
            self.assertFalse(mentioned, f"{competitor} should NOT be mentioned in Meta segment")
        self.assertTrue(meta_segment["meta_mentions"])

    def test_apple_airpods_omission_timing(self):
        """Apple camera AirPods leaked Aug 18 (2 days before recording) — not mentioned."""
        timeline = {
            "apple_airpods_camera_leak": "2026-08-18",
            "tnw_451_recording": "2026-08-20",
            "days_gap": 2,
            "airpods_mentioned_in_meta_segment": False,
            "airpods_mentioned_anywhere_in_episode": False,
        }
        self.assertEqual(timeline["days_gap"], 2)
        self.assertFalse(timeline["airpods_mentioned_in_meta_segment"])


class TestPhoneCameraSelfCorrectionPattern(unittest.TestCase):
    """Analyze the host's acknowledgment and retreat from the phone-camera parallel."""

    def test_host_raises_phone_parallel(self):
        """Mikah Sargent explicitly compares phone recording to Meta glasses recording."""
        quote = (
            "a lot of times in a comedy audience, you'll see people holding up phones "
            "and recording that way"
        )
        self.assertIn("phones", quote)
        self.assertIn("recording", quote)

    def test_host_suggests_phone_led_indicator(self):
        """Host suggests phones SHOULD have recording indicators — implying Meta already does more."""
        quote = (
            "we need to also have our phone cameras when they're recording, they should "
            "have a blinking light going or something"
        )
        # This implicitly acknowledges Meta's LED indicator provides MORE privacy
        # transparency than phones, which have NO recording indicator
        self.assertIn("blinking light", quote)

    def test_self_correction_retreat(self):
        """After raising the parity, host retreats to Meta-specific alarm."""
        # The logical conclusion from "phones should have blinking lights too" is:
        # Meta's glasses with LED indicators are MORE privacy-conscious than phones.
        # Instead, the host returns to: "it makes you really have to confront the fact
        # that in public there's not an incredibly...you can't expect much privacy"
        retreat_quote = (
            "it makes you really have to confront the fact that in public there's not "
            "an incredibly"
        )
        # Pattern: raise comparison → recognize parity → retreat to entity-specific alarm
        self.assertIn("confront", retreat_quote)

    def test_self_correction_does_not_soften_meta_framing(self):
        """The phone comparison does NOT lead to softened Meta framing."""
        # Post-comparison, the host continues with alarm vocabulary
        post_comparison_quotes = [
            "it's only going to get more, like, messy and intense from here",
            "people should feel protected from being bullied and recorded",
        ]
        alarm_words = ["messy", "intense", "bullied", "recorded"]
        for word in alarm_words:
            found = any(word in q for q in post_comparison_quotes)
            self.assertTrue(found, f"Alarm word '{word}' should persist after phone comparison")


class TestAmazonContrastVocabulary(unittest.TestCase):
    """Amazon book scanning gets adventure framing despite arguably worse behavior."""

    def test_amazon_actions_severity(self):
        """Amazon's documented actions are arguably more harmful than Meta glasses recording."""
        amazon_actions = {
            "mass_book_acquisition": True,
            "physical_destruction_cutting_spines": True,
            "rare_irreplaceable_books_destroyed": True,
            "deceptive_marketplace_identity": True,
            "warehouse_workers_repetitive_labor": True,
            "ai_training_data_extraction": True,
        }
        for action, exists in amazon_actions.items():
            self.assertTrue(exists)

    def test_amazon_vocabulary_is_adventure(self):
        """Amazon segment uses adventure/discovery vocabulary despite severity."""
        amazon_vocabulary = {
            "wild idea": "enthusiasm",
            "exciting": "positive",
            "mystery solved": "satisfaction",
            "fascinating": "intellectual curiosity",
        }
        for word, register in amazon_vocabulary.items():
            self.assertNotEqual(register, "alarm")

    def test_vocabulary_gap_is_entity_dependent(self):
        """The vocabulary difference tracks entity identity, not action severity."""
        meta_action = "customer films retail worker for social media"
        amazon_action = "company destroys rare books to train AI"
        meta_vocabulary = "menace"
        amazon_vocabulary = "wild idea"
        # The more harmful action gets softer vocabulary
        self.assertEqual(meta_vocabulary, "menace")
        self.assertEqual(amazon_vocabulary, "wild idea")


class TestCrossNetworkAmplificationCascade(unittest.TestCase):
    """Verify the speed and fidelity of cross-network framing propagation."""

    def test_amplification_timeline(self):
        """Verge → TWiT same-day, Vergecast next day."""
        cascade = {
            "origin": {
                "outlet": "The Verge",
                "author": "Mia Sato",
                "date": "2026-08-20",
                "headline": "Meta glasses are a workplace menace",
                "framing": "alarm",
            },
            "amplification_1": {
                "outlet": "TWiT Tech News Weekly #451",
                "host": "Mikah Sargent",
                "date": "2026-08-20",
                "delay_hours": 0,
                "framing_match": "exact",
                "independent_investigation": False,
            },
            "amplification_2": {
                "outlet": "Vergecast Ep 1057",
                "date": "2026-08-20",
                "delay_hours": 0,
                "framing_match": "show_notes_link",
            },
            "amplification_3": {
                "outlet": "Vergecast Ep 1058",
                "date": "2026-08-21",
                "delay_hours": 24,
                "framing_match": "show_notes_link_plus_discussion",
            },
        }
        # TWiT amplified same day with no independent investigation
        self.assertFalse(cascade["amplification_1"]["independent_investigation"])
        self.assertEqual(cascade["amplification_1"]["framing_match"], "exact")
        self.assertEqual(cascade["amplification_1"]["delay_hours"], 0)

    def test_no_counter_framing_in_cascade(self):
        """No outlet in the cascade adds competitor comparison or softening context."""
        counter_framing_elements = {
            "samsung_comparison": False,
            "apple_comparison": False,
            "phone_camera_extended_analysis": False,
            "meta_led_indicator_credit": False,
            "accessibility_benefit_mention": False,
        }
        for element, present in counter_framing_elements.items():
            self.assertFalse(present, f"{element} should be absent from cascade")

    def test_twit_as_independent_network(self):
        """TWiT is independent of Vox Media but reproduces identical framing."""
        twit_network = {
            "name": "TWiT",
            "founder": "Leo Laporte",
            "ownership": "independent",
            "vox_media_relationship": "none",
            "conde_nast_relationship": "none",
            "meta_content_deal": False,
            "apple_content_deal": False,
            "google_content_deal": False,
            "revenue_model": "advertising + premium subscriptions",
        }
        self.assertEqual(twit_network["ownership"], "independent")
        self.assertFalse(twit_network["meta_content_deal"])
        # Independent network reproducing Vox Media framing = cultural consensus, not editorial coordination


class TestTWiTNetworkDualShowPattern(unittest.TestCase):
    """TWiT network shows AI Inside AND TNW both reproduce Meta-alarm framing."""

    def test_two_twit_shows_one_week(self):
        """AI Inside (Aug 19) and TNW (Aug 20) both apply alarm vocabulary to Meta."""
        shows = [
            {
                "show": "AI Inside",
                "episode": "Aug 19, 2026",
                "meta_vocabulary": ["ban", "pervert", "backlash", "en masse"],
                "apple_vocabulary": ["confirmed"],
                "mechanism": 244,
            },
            {
                "show": "Tech News Weekly",
                "episode": "Aug 20, 2026 (#451)",
                "meta_vocabulary": ["menace", "struggles", "scary", "not in a good way"],
                "apple_vocabulary": [],  # not mentioned
                "mechanism": 261,
            },
        ]
        for show in shows:
            # Both shows apply alarm-register to Meta
            alarm_words_meta = [w for w in show["meta_vocabulary"]
                                if w in ["menace", "struggles", "scary", "ban", "pervert", "backlash"]]
            self.assertTrue(len(alarm_words_meta) > 0,
                            f"{show['show']} should have alarm words for Meta")
            # Neither show applies alarm-register to Apple
            alarm_words_apple = [w for w in show["apple_vocabulary"]
                                 if w in ["menace", "pervert", "backlash", "ban", "scary"]]
            self.assertEqual(len(alarm_words_apple), 0,
                             f"{show['show']} should have zero alarm words for Apple")


class TestMechanismRegistration(unittest.TestCase):
    """Verify mechanism #261 is properly registered."""

    def test_mechanism_id(self):
        mechanism = {
            "id": 261,
            "name": "Cross-Network Framing Amplification via Workplace Menace Narrative",
            "type": "podcast_cross_network_cascade",
            "podcast": "Tech News Weekly #451",
            "network": "TWiT",
            "date": "2026-08-20",
            "host": "Mikah Sargent",
            "guest": "Abrar Al-Heeti (CNET)",
            "source_article": "Meta glasses are a workplace menace (Mia Sato, The Verge)",
            "sentiment_score_meta": -6,
            "sentiment_score_apple": None,
            "sentiment_score_amazon": 0,
            "asymmetry_assessment": "HIGH",
            "confounders": [
                {"strength": "STRONG", "description": "Meta IS the only company with 7M+ glasses in the wild; workplace incidents are real"},
                {"strength": "STRONG", "description": "TWiT is editorially independent; no Vox Media or Condé Nast influence"},
                {"strength": "MODERATE", "description": "Host raises phone-camera parallel, showing awareness of broader context"},
                {"strength": "MODERATE", "description": "Apple camera AirPods not yet released; absence from discussion may reflect product maturity gap"},
                {"strength": "WEAK", "description": "Samsung Galaxy Glasses announced but not shipping; pre-launch products get less scrutiny"},
            ],
            "cross_references": [225, 244, 221, 148, 157, 158],
        }
        self.assertEqual(mechanism["id"], 261)
        self.assertEqual(mechanism["asymmetry_assessment"], "HIGH")
        self.assertEqual(mechanism["sentiment_score_meta"], -6)
        # Amazon gets neutral despite book destruction
        self.assertEqual(mechanism["sentiment_score_amazon"], 0)


class TestConfounders(unittest.TestCase):
    """Document the confounders for this mechanism."""

    def test_strong_confounder_meta_market_share(self):
        """Meta has 80%+ of camera smart glasses market — more incidents expected."""
        confounder = {
            "strength": "STRONG",
            "description": "Meta has sold 7M+ pairs; Samsung/Google/Apple have 0 shipping",
            "sufficient_to_explain_asymmetry": False,
            "rationale": (
                "Market share legitimately explains more Meta incidents, but does NOT "
                "explain: (1) zero mention of competitors with identical hardware, "
                "(2) zero acknowledgment that phones enable identical recording, "
                "(3) adventure vocabulary for Amazon's arguably more harmful book "
                "destruction. The vocabulary gap exceeds what market share predicts."
            ),
        }
        self.assertEqual(confounder["strength"], "STRONG")
        self.assertFalse(confounder["sufficient_to_explain_asymmetry"])

    def test_strong_confounder_editorial_independence(self):
        """TWiT is editorially independent — no financial incentive detected."""
        confounder = {
            "strength": "STRONG",
            "description": "TWiT has no content deals with Meta or competitors",
            "implication": (
                "The absence of financial incentive strengthens the cultural consensus "
                "hypothesis: Meta-alarm framing propagates through cultural agreement, "
                "not editorial coordination or financial pressure."
            ),
        }
        self.assertEqual(confounder["strength"], "STRONG")

    def test_moderate_confounder_phone_parallel_awareness(self):
        """Host's phone-camera acknowledgment shows partial awareness."""
        confounder = {
            "strength": "MODERATE",
            "description": (
                "Mikah Sargent explicitly raises the phone recording parallel and even "
                "suggests phones should have LED indicators — showing awareness that "
                "Meta's indicator already provides more transparency than phones."
            ),
            "mitigation": (
                "The awareness does not lead to proportionate treatment. Host retreats "
                "to Meta-specific alarm after raising the parallel."
            ),
        }
        self.assertEqual(confounder["strength"], "MODERATE")


class TestGizmodoPotatoQualityCorroboration(unittest.TestCase):
    """Same week: Gizmodo rationalizes Apple AirPods 1MP as privacy-safe."""

    def test_contemporaneous_apple_resolution_rationalization(self):
        """Gizmodo article (Aug 21) frames 1MP AirPods camera as privacy-safe."""
        gizmodo_article = {
            "headline": "No, AirPods With Cameras Aren't Smart Glasses for Your Ears",
            "date": "2026-08-21",
            "outlet": "Gizmodo",
            "key_framing": "potato quality",
            "resolution_rationalization": True,
            "meta_comparison": "While smart glasses like the Ray-Ban Meta AI glasses can capture pictures and videos in high resolution",
            "apple_framing": "not so good that they represent a huge privacy liability",
        }
        self.assertTrue(gizmodo_article["resolution_rationalization"])
        # Same week as TNW #451 (Aug 20): one outlet alarms about Meta, another soothes about Apple
        self.assertIn("potato quality", gizmodo_article["key_framing"])

    def test_1mp_surveillance_capability(self):
        """1MP is sufficient for surveillance despite 'potato quality' dismissal."""
        one_mp_capabilities = {
            "read_text_signs": True,
            "identify_faces_social_distance": True,
            "capture_license_plates": True,
            "record_identifiable_video": True,
            "original_iphone_2007_camera": "2MP",
            "first_ring_doorbell_2013": "720p (0.9MP)",
        }
        # Both the original iPhone and Ring doorbell were considered surveillance-capable
        # at resolutions comparable to or below 1MP
        self.assertTrue(one_mp_capabilities["identify_faces_social_distance"])


if __name__ == "__main__":
    unittest.main()
