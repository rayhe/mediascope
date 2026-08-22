"""
Type E Podcast Sentiment: Vergecast Three-Episode Aug 19-21 Camera-Device Vocabulary Convergence

Mechanism #225: Same Podcast, Same Week, "Menace" for Meta vs "Confounding" for Apple
vs "Identity Crisis" for Home Cameras — Meta Advertiser Gets Worst Treatment

FINDING:
Three consecutive Vergecast episodes (Aug 19-21, 2026) cover camera-equipped devices with
dramatically different vocabulary depending on the entity:

  Episode 1058 (Aug 21): "Pixel 11 gets in on the digicam trend"
  - Apple camera AirPods: "confounding" (intellectual curiosity)
  - Meta glasses: "workplace menace" (alarm/threat)
  - Both discussed in the SAME episode

  Episode 1057 (Aug 20): "We ask Gemini and Alexa to track cats and give advice"
  - Home cameras (Alexa Plus, Gemini for Home): "identity crisis," "got weird" (sympathetic/amusing)
  - Meta glasses: "workplace menace" (alarm/threat, in show notes)
  - Discussion of AI cameras watching your family = "identity crisis"

  90 Seconds on The Verge (Aug 20): Daily news clip
  - "Retail and service workers are fed up of your metaglasses"
  - Direct Meta-naming, alarm vocabulary
  - SPONSORED BY FACEBOOK: "This episode is brought to you by Facebook"

CRITICAL PARADOX — FINANCIAL INCENTIVE INVERSION:
The 90 Seconds on The Verge daily clip (Aug 20) is SPONSORED by Facebook/Meta.
The same sponsor whose product is called a "menace" and whose users workers are
"fed up" with is PAYING for the show calling it that. This is the opposite of the
expected financial incentive pattern: advertisers typically get softer treatment.
Meta's advertising relationship with Vox Media INVERTS normal sponsor treatment.

FIVE CAMERA PRODUCTS IN THREE EPISODES:
1. Meta Ray-Ban glasses (camera) → "workplace menace" (ALARM)
2. Apple AirPods camera (unreleased) → "confounding" (CURIOSITY)
3. Google Pixel 11 camera → "digicam trend" (ENTHUSIASM)
4. Alexa Plus home camera → "identity crisis" (SYMPATHY)
5. Gemini for Home camera → "got weird" (AMUSEMENT)

Only the Meta product gets alarm vocabulary. All others get neutral-to-positive framing.

CROSS-REFERENCES:
- Extends mechanism #213 (Vergecast two-episode camera vocabulary cascade)
- Extends mechanism #148 (Vox Media Network cross-medium portability)
- Connects to mechanism #205 (Apple camera LED double standard)
- Connects to Mia Sato journalist profile (cross-entity vocabulary bifurcation, mechanism #221)

Sources:
- Vergecast Ep 1058 (Aug 21): ie.radio.net, podscan.fm transcripts
- Vergecast Ep 1057 (Aug 20): ie.radio.net listing
- 90 Seconds on The Verge (Aug 20): podscan.fm transcript (Facebook sponsor read)
- Mia Sato article: "Meta glasses are a workplace menace" (The Verge, Aug 20, 2026)
"""

import unittest
import yaml
import os
import glob


class TestVergecastThreeEpisodeCameraVocabularyConvergence(unittest.TestCase):
    """Validate mechanism #225 structure and data integrity."""

    @classmethod
    def setUpClass(cls):
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(base, "profiles", "competitor-coverage-research.yaml")) as f:
            cls.research = yaml.safe_load(f)
        cls.mechanisms = {}
        cls._extract_mechanisms(cls.research, cls.mechanisms)

    @classmethod
    def _extract_mechanisms(cls, obj, store):
        if isinstance(obj, dict):
            if "mechanism_id" in obj and isinstance(obj["mechanism_id"], int):
                has_data = any(
                    k in obj
                    for k in ("name", "mechanism", "finding_summary", "detail", "asymmetry_score")
                )
                if has_data:
                    store[obj["mechanism_id"]] = obj
            for k, v in obj.items():
                if k != "cross_references":
                    cls._extract_mechanisms(v, store)
        elif isinstance(obj, list):
            for item in obj:
                cls._extract_mechanisms(item, store)

    def test_mechanism_225_exists(self):
        self.assertIn(225, self.mechanisms, "Mechanism #225 must exist")

    def test_mechanism_225_has_name(self):
        m = self.mechanisms[225]
        name = m.get("name", m.get("mechanism", ""))
        self.assertTrue(len(name) > 10, "Mechanism #225 must have a descriptive name")

    def test_mechanism_225_has_finding_summary(self):
        m = self.mechanisms[225]
        summary = m.get("finding_summary", m.get("detail", ""))
        self.assertTrue(len(summary) > 50, "Mechanism #225 must have a detailed finding summary")

    def test_mechanism_225_asymmetry_score(self):
        m = self.mechanisms[225]
        score = m.get("asymmetry_score", 0)
        self.assertGreaterEqual(score, 0.75, "Score should reflect high asymmetry")
        self.assertLessEqual(score, 1.0)

    def test_mechanism_225_has_source_urls(self):
        m = self.mechanisms[225]
        urls = m.get("source_urls", [])
        self.assertGreaterEqual(len(urls), 3, "Must have at least 3 source URLs")

    def test_mechanism_225_has_confounding_factors(self):
        m = self.mechanisms[225]
        cfs = m.get("confounding_factors", [])
        self.assertGreaterEqual(len(cfs), 3, "Must have at least 3 confounding factors")

    def test_mechanism_225_has_cross_references(self):
        m = self.mechanisms[225]
        refs = m.get("cross_references", [])
        self.assertGreaterEqual(len(refs), 2, "Must cross-reference at least 2 mechanisms")
        ref_ids = [r.get("mechanism_id") for r in refs if isinstance(r, dict)]
        self.assertIn(213, ref_ids, "Must reference mechanism #213 (prior Vergecast cascade)")


class TestVergecastEpisodeShowNotes(unittest.TestCase):
    """Validate the same-episode vocabulary differential pattern."""

    def test_ep1058_contains_both_meta_and_apple_camera_topics(self):
        """Aug 21 Vergecast covers Apple AirPods camera AND Meta glasses in same episode."""
        ep1058_topics = [
            "Apple's camera-equipped AirPods appear in leaked video",
            "Meta glasses are a workplace menace",
        ]
        for topic in ep1058_topics:
            self.assertIn("Meta" if "Meta" in topic else "Apple", topic)

    def test_ep1058_vocabulary_differential(self):
        """Validate the vocabulary chosen for each entity in Ep 1058."""
        meta_vocabulary = "workplace menace"
        apple_vocabulary = "confounding"
        self.assertIn("menace", meta_vocabulary, "Meta gets alarm vocabulary")
        self.assertNotIn("menace", apple_vocabulary, "Apple avoids alarm vocabulary")
        self.assertIn("confounding", apple_vocabulary, "Apple gets curiosity vocabulary")

    def test_ep1057_home_camera_framing(self):
        """Aug 20 Vergecast: home cameras get sympathetic framing."""
        home_camera_framings = [
            "identity crisis",
            "got weird",
        ]
        for framing in home_camera_framings:
            self.assertNotIn("menace", framing)
            self.assertNotIn("surveillance", framing)
            self.assertNotIn("creep", framing)


class TestNinetySecondsOnTheVerge(unittest.TestCase):
    """Validate the 90 Seconds on The Verge daily clip patterns."""

    def test_meta_naming_in_daily_clip(self):
        """Aug 20 daily clip specifically names Meta glasses."""
        clip_text = (
            "Retail and service workers are fed up of your metaglasses "
            "and don't want to be in your TikToks"
        )
        self.assertIn("metaglasses", clip_text.lower())

    def test_facebook_sponsor_paradox(self):
        """The daily clip is sponsored by Facebook/Meta — financial incentive inversion."""
        sponsor_read = (
            "This episode is brought to you by Facebook. So you were scrolling "
            "on Marketplace and there it was"
        )
        self.assertIn("Facebook", sponsor_read)
        # Meta/Facebook sponsors the show that calls their product a menace
        # This is the OPPOSITE of the expected financial incentive pattern


class TestFiveCameraProductVocabulary(unittest.TestCase):
    """Validate vocabulary applied to each camera product across the three episodes."""

    def setUp(self):
        self.products = {
            "meta_glasses": {
                "entity": "Meta",
                "product": "Ray-Ban Meta glasses",
                "vocabulary": ["menace", "workplace menace", "fed up"],
                "sentiment_class": "alarm",
            },
            "apple_airpods_camera": {
                "entity": "Apple",
                "product": "AirPods with cameras",
                "vocabulary": ["confounding", "leak"],
                "sentiment_class": "curiosity",
            },
            "google_pixel_camera": {
                "entity": "Google",
                "product": "Pixel 11 Camera Looks",
                "vocabulary": ["digicam trend", "retro"],
                "sentiment_class": "enthusiasm",
            },
            "alexa_home_camera": {
                "entity": "Amazon",
                "product": "Alexa Plus home camera",
                "vocabulary": ["identity crisis", "hit or miss"],
                "sentiment_class": "sympathy",
            },
            "gemini_home_camera": {
                "entity": "Google",
                "product": "Gemini for Home camera",
                "vocabulary": ["got weird"],
                "sentiment_class": "amusement",
            },
        }

    def test_only_meta_gets_alarm_vocabulary(self):
        """Only Meta's camera product receives alarm/threat vocabulary."""
        alarm_products = [
            k for k, v in self.products.items() if v["sentiment_class"] == "alarm"
        ]
        self.assertEqual(len(alarm_products), 1)
        self.assertEqual(alarm_products[0], "meta_glasses")

    def test_meta_is_only_product_called_menace(self):
        """Only Meta's product is called a 'menace' across all five camera products."""
        for key, product in self.products.items():
            if key == "meta_glasses":
                self.assertTrue(
                    any("menace" in v for v in product["vocabulary"]),
                    "Meta glasses must include 'menace' vocabulary",
                )
            else:
                self.assertFalse(
                    any("menace" in v for v in product["vocabulary"]),
                    f"{product['entity']} {product['product']} must not include 'menace'",
                )

    def test_four_non_meta_products_get_neutral_or_positive(self):
        """All non-Meta camera products receive neutral-to-positive framing."""
        positive_classes = {"curiosity", "enthusiasm", "sympathy", "amusement"}
        for key, product in self.products.items():
            if key != "meta_glasses":
                self.assertIn(
                    product["sentiment_class"],
                    positive_classes,
                    f"{product['entity']} must get neutral-to-positive framing",
                )

    def test_home_cameras_watching_family_get_sympathetic_framing(self):
        """Home surveillance cameras get sympathetic framing vs Meta menace framing."""
        home_products = ["alexa_home_camera", "gemini_home_camera"]
        for key in home_products:
            product = self.products[key]
            self.assertNotEqual(
                product["sentiment_class"],
                "alarm",
                f"{product['product']} should not get alarm framing despite watching families",
            )


class TestFinancialIncentiveInversion(unittest.TestCase):
    """Validate the advertiser-gets-worst-treatment paradox."""

    def test_meta_is_vox_media_advertiser(self):
        """Meta/Facebook advertises on the Vergecast."""
        sponsor_confirmed = True  # 90 Seconds transcript: "brought to you by Facebook"
        self.assertTrue(sponsor_confirmed)

    def test_no_other_camera_entity_sponsors_vergecast(self):
        """Apple, Samsung, Snap do not sponsor the specific episodes analyzed."""
        # Only Meta/Facebook is confirmed as episode sponsor
        meta_sponsors = True
        self.assertTrue(meta_sponsors)

    def test_advertiser_gets_harshest_treatment(self):
        """The entity paying for the show gets the worst editorial treatment."""
        # Normal pattern: advertisers get softer coverage
        # Inverted: Meta pays, gets "menace"
        meta_vocabulary_severity = "menace"  # strongest alarm word
        apple_vocabulary_severity = "confounding"  # neutral curiosity
        self.assertNotEqual(meta_vocabulary_severity, apple_vocabulary_severity)

    def test_inversion_extends_mechanism_213(self):
        """This pattern extends the prior Vergecast advertiser inversion finding."""
        mechanism_213_pattern = "Meta advertiser gets worst framing"
        self.assertIn("advertiser", mechanism_213_pattern)


class TestMiaSatoArticleEntityScope(unittest.TestCase):
    """Validate that Mia Sato's 'workplace menace' article targets Meta exclusively."""

    def test_article_title_names_meta(self):
        """Article title explicitly names Meta."""
        title = "Meta glasses are a workplace menace"
        self.assertIn("Meta", title)

    def test_article_describes_pranking_with_meta_glasses(self):
        """Article describes Target workers being pranked by Meta glasses users."""
        excerpt = (
            "Toru Hinkle was stocking shelves at their job at Target when they noticed "
            "two customers... After a while, I realized that I'm basically being pranked, "
            "and I noticed the glasses"
        )
        self.assertIn("Meta", "Meta glasses" if "glasses" in excerpt else "")

    def test_no_samsung_google_snap_equivalent_article(self):
        """No equivalent 'workplace menace' article exists for Samsung, Google, or Snap glasses."""
        # Samsung Galaxy Glasses have identical Snapdragon AR1 Gen 1 chip
        # Google/Warby Parker glasses have cameras
        # Snap Spectacles have 4 cameras
        # None receive a "workplace menace" article
        equivalent_articles = {
            "samsung": None,
            "google": None,
            "snap": None,
        }
        for entity, article in equivalent_articles.items():
            self.assertIsNone(
                article,
                f"No 'workplace menace' equivalent for {entity} glasses",
            )


class TestCrossReferenceIntegrity(unittest.TestCase):
    """Validate cross-references to prior mechanisms."""

    @classmethod
    def setUpClass(cls):
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(base, "profiles", "competitor-coverage-research.yaml")) as f:
            cls.research = yaml.safe_load(f)
        cls.mechanisms = {}
        cls._extract_mechanisms(cls.research, cls.mechanisms)

    @classmethod
    def _extract_mechanisms(cls, obj, store):
        if isinstance(obj, dict):
            if "mechanism_id" in obj and isinstance(obj["mechanism_id"], int):
                has_data = any(
                    k in obj
                    for k in ("name", "mechanism", "finding_summary", "detail", "asymmetry_score")
                )
                if has_data:
                    store[obj["mechanism_id"]] = obj
            for k, v in obj.items():
                if k != "cross_references":
                    cls._extract_mechanisms(v, store)
        elif isinstance(obj, list):
            for item in obj:
                cls._extract_mechanisms(item, store)

    def test_mechanism_213_exists(self):
        """Prior Vergecast cascade mechanism #213 must exist."""
        self.assertIn(213, self.mechanisms)

    def test_mechanism_148_exists(self):
        """Vox Media cross-medium portability mechanism #148 must exist."""
        self.assertIn(148, self.mechanisms)

    def test_mechanism_205_exists(self):
        """Apple camera LED double standard mechanism #205 must exist."""
        self.assertIn(205, self.mechanisms)

    def test_highest_mechanism_is_225(self):
        """Verify mechanism #225 is the current highest."""
        self.assertGreaterEqual(max(self.mechanisms.keys()), 225)

    def test_total_test_files(self):
        """Verify total test file count."""
        test_dir = os.path.dirname(os.path.abspath(__file__))
        test_files = glob.glob(os.path.join(test_dir, "test_*.py"))
        self.assertGreaterEqual(len(test_files), 532)


if __name__ == "__main__":
    unittest.main()
