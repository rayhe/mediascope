"""
Steve Dent (Engadget) — Cross-Entity Camera Wearable Privacy Vocabulary Gradient

Mechanism #272: Same Engadget contributing writer covers Meta glasses privacy
AND Apple camera AirPods with dramatically different framing:

Article 1 — Meta (Mar 3, 2026):
  - Headline: "Meta's AI display glasses reportedly share intimate videos with
    human moderators"
  - Alarm vocabulary: "unknowingly sharing intimate video," "sensitive financial
    information," "moderators outside of the bloc," "underpaid workers,"
    descriptions of "nude, using the toilet and engaging in sexual activity,
    along with credit card numbers"
  - Framing: Privacy alarm / investigative exposure
  - Source: Svenska Dagbladet investigation
  - Alarm vocabulary count: 8+ terms

Article 2 — Apple (Aug 18, 2026):
  - Headline: "Apple appears to have leaked its camera-equipped AirPods"
  - Key vocabulary: "low-res imagery," "Visual Intelligence," "your world becomes
    saveable"
  - Privacy treatment: Single paragraph with hedging — "some privacy concerns,"
    "technically a surveillance device" (diminishing "technically"), "may turn off
    some users" (passive), "minimum for such a wearable"
  - Framing: Product news / tech leak
  - Alarm vocabulary count: ~1 (technically surveillance device, heavily hedged)

The Natural Experiment:
  Both articles cover camera-equipped wearable devices from the SAME journalist
  at the SAME publication. The key asymmetry:
  - Meta article: leads with privacy, alarm vocabulary dominates, contractor
    abuse detailed, no product enthusiasm
  - Apple article: leads with product features, single paragraph of hedged
    privacy concern, no exploration of contractor review implications
  - Apple AirPods have "passive mode" (320x320 always-on capture) — arguably
    MORE surveillance-like than Meta's user-triggered 12MP — but this receives
    zero alarm vocabulary
  - Apple's Visual Intelligence processing pipeline would ALSO likely involve
    human review for AI training, but this isn't mentioned

Sources:
  - Meta article: https://www.engadget.com/wearables/metas-ai-display-glasses-reportedly-share-intimate-videos-with-human-moderators-135939560.html
  - Apple article: https://www.engadget.com/2238891/apple-appears-to-have-leaked-its-camera-equipped-airpods/

Cross-references: #256 (Tim Hardwick MacRumors same-journalist), #252
(Chokkattu temporal adjacency), #246 (Engadget vocabulary mitigation)
"""

import unittest
import os


# ---------------------------------------------------------------------------
# Article-level data fixtures (manually extracted from source articles)
# ---------------------------------------------------------------------------

META_ARTICLE = {
    "journalist": "Steve Dent",
    "publication": "Engadget",
    "parent_company": "Yahoo Inc.",
    "headline": "Meta's AI display glasses reportedly share intimate videos with human moderators",
    "date": "2026-03-03",
    "url": "https://www.engadget.com/wearables/metas-ai-display-glasses-reportedly-share-intimate-videos-with-human-moderators-135939560.html",
    "entity": "Meta",
    "product": "Meta AI display glasses",
    "source_investigation": "Svenska Dagbladet",
    "alarm_terms": [
        "unknowingly sharing",
        "intimate video",
        "sensitive financial information",
        "moderators outside of the bloc",
        "underpaid workers",
        "nude",
        "sexual activity",
        "credit card numbers",
    ],
    "hedging_terms": [],
    "product_enthusiasm_terms": [],
    "privacy_framing": "alarm_investigative",
    "leads_with_privacy": True,
    "contractor_abuse_detailed": True,
    "advocacy_sources_cited": 1,
}

APPLE_ARTICLE = {
    "journalist": "Steve Dent",
    "publication": "Engadget",
    "parent_company": "Yahoo Inc.",
    "headline": "Apple appears to have leaked its camera-equipped AirPods",
    "date": "2026-08-18",
    "url": "https://www.engadget.com/2238891/apple-appears-to-have-leaked-its-camera-equipped-airpods/",
    "entity": "Apple",
    "product": "Apple camera-equipped AirPods",
    "source_investigation": None,
    "alarm_terms": [
        "technically a surveillance device",
    ],
    "hedging_terms": [
        "some privacy concerns",
        "technically",
        "may turn off some users",
        "minimum for such a wearable",
    ],
    "product_enthusiasm_terms": [
        "low-res imagery",
        "Visual Intelligence",
        "your world becomes saveable",
    ],
    "privacy_framing": "neutral_product_news",
    "leads_with_privacy": False,
    "contractor_abuse_detailed": False,
    "advocacy_sources_cited": 0,
    "passive_mode_resolution": "320x320",
    "passive_mode_always_on": True,
}


# ---------------------------------------------------------------------------
# Test classes
# ---------------------------------------------------------------------------


class TestMetaArticleHeadlineAlarm(unittest.TestCase):
    """Verify Meta headline contains alarm vocabulary."""

    article_data = META_ARTICLE

    def test_headline_contains_intimate(self):
        """Meta headline uses alarm word 'intimate'."""
        self.assertIn("intimate", self.article_data["headline"].lower())

    def test_headline_contains_moderators(self):
        """Meta headline uses alarm word 'moderators'."""
        self.assertIn("moderators", self.article_data["headline"].lower())

    def test_headline_contains_reportedly(self):
        """Meta headline uses investigative framing word 'reportedly'."""
        self.assertIn("reportedly", self.article_data["headline"].lower())

    def test_headline_privacy_framing(self):
        """Meta headline frames the story as a privacy alarm."""
        headline = self.article_data["headline"].lower()
        alarm_indicators = ["intimate", "share", "moderators"]
        matches = sum(1 for word in alarm_indicators if word in headline)
        self.assertGreaterEqual(matches, 2,
                                "Meta headline should contain at least 2 alarm indicators")


class TestAppleArticleHeadlineNeutral(unittest.TestCase):
    """Verify Apple headline is product-focused with no alarm vocabulary."""

    article_data = APPLE_ARTICLE

    def test_headline_no_privacy_alarm(self):
        """Apple headline contains zero privacy alarm vocabulary."""
        headline = self.article_data["headline"].lower()
        alarm_words = ["intimate", "surveillance", "moderators", "nude",
                       "creepy", "pervert", "privacy", "monitoring"]
        for word in alarm_words:
            self.assertNotIn(word, headline,
                             f"Apple headline should not contain alarm word '{word}'")

    def test_headline_is_product_focused(self):
        """Apple headline is framed as product news ('leaked', 'camera-equipped')."""
        headline = self.article_data["headline"].lower()
        product_words = ["leaked", "camera-equipped", "airpods"]
        matches = sum(1 for word in product_words if word in headline)
        self.assertGreaterEqual(matches, 2,
                                "Apple headline should contain product-focused terms")

    def test_headline_uses_leaked_framing(self):
        """Apple headline frames story as 'leak' — excitement, not alarm."""
        self.assertIn("leaked", self.article_data["headline"].lower())

    def test_headline_entity_named_neutrally(self):
        """Apple is named without negative attribution in headline."""
        headline = self.article_data["headline"]
        self.assertIn("Apple", headline)
        # No blame attribution in headline
        blame_words = ["reportedly", "share", "intimate", "creepy"]
        for word in blame_words:
            self.assertNotIn(word, headline.lower())


class TestMetaAlarmVocabularyCount(unittest.TestCase):
    """Verify Meta article uses 8+ alarm terms."""

    article_data = META_ARTICLE

    def test_alarm_term_count_minimum(self):
        """Meta article contains at least 8 alarm terms."""
        self.assertGreaterEqual(len(self.article_data["alarm_terms"]), 8)

    def test_alarm_terms_include_unknowingly(self):
        """Meta alarm terms include 'unknowingly sharing'."""
        terms_lower = [t.lower() for t in self.article_data["alarm_terms"]]
        self.assertTrue(any("unknowingly" in t for t in terms_lower))

    def test_alarm_terms_include_nude(self):
        """Meta alarm terms include 'nude'."""
        terms_lower = [t.lower() for t in self.article_data["alarm_terms"]]
        self.assertTrue(any("nude" in t for t in terms_lower))

    def test_zero_product_enthusiasm(self):
        """Meta article contains zero product enthusiasm vocabulary."""
        self.assertEqual(len(self.article_data["product_enthusiasm_terms"]), 0)


class TestAppleAlarmVocabularyCount(unittest.TestCase):
    """Verify Apple article uses <=2 alarm terms, mostly hedged."""

    article_data = APPLE_ARTICLE

    def test_alarm_term_count_maximum(self):
        """Apple article contains at most 2 alarm terms."""
        self.assertLessEqual(len(self.article_data["alarm_terms"]), 2)

    def test_alarm_terms_are_hedged(self):
        """Apple's alarm terms are hedged with diminishing language."""
        # The single alarm term 'technically a surveillance device' uses 'technically'
        if self.article_data["alarm_terms"]:
            for term in self.article_data["alarm_terms"]:
                self.assertIn("technically", term.lower(),
                              f"Apple alarm term '{term}' should be hedged")

    def test_hedging_terms_outnumber_alarm_terms(self):
        """Apple hedging terms outnumber alarm terms."""
        alarm_count = len(self.article_data["alarm_terms"])
        hedge_count = len(self.article_data["hedging_terms"])
        self.assertGreater(hedge_count, alarm_count,
                           f"Hedging terms ({hedge_count}) should exceed alarm terms ({alarm_count})")


class TestCrossEntityVocabularyGradient(unittest.TestCase):
    """Compare alarm vocabulary density between Meta and Apple articles."""

    def test_alarm_vocabulary_ratio_at_least_8_to_1(self):
        """Meta-to-Apple alarm vocabulary ratio is at least 8:1."""
        meta_count = len(META_ARTICLE["alarm_terms"])
        apple_count = max(len(APPLE_ARTICLE["alarm_terms"]), 1)
        ratio = meta_count / apple_count
        self.assertGreaterEqual(ratio, 8.0,
                                f"Alarm ratio {ratio:.1f}:1 should be >= 8:1")

    def test_meta_leads_with_privacy(self):
        """Meta article leads with privacy concerns."""
        self.assertTrue(META_ARTICLE["leads_with_privacy"])

    def test_apple_does_not_lead_with_privacy(self):
        """Apple article does NOT lead with privacy concerns."""
        self.assertFalse(APPLE_ARTICLE["leads_with_privacy"])

    def test_same_journalist_same_publication(self):
        """Both articles are by the same journalist at the same publication."""
        self.assertEqual(META_ARTICLE["journalist"], APPLE_ARTICLE["journalist"])
        self.assertEqual(META_ARTICLE["publication"], APPLE_ARTICLE["publication"])


class TestApplePassiveModeOmission(unittest.TestCase):
    """Verify Apple passive/always-on camera mode receives zero privacy scrutiny."""

    def test_apple_has_passive_always_on_capture(self):
        """Apple AirPods have a passive always-on capture mode (320x320)."""
        self.assertTrue(APPLE_ARTICLE["passive_mode_always_on"])
        self.assertEqual(APPLE_ARTICLE["passive_mode_resolution"], "320x320")

    def test_passive_mode_receives_zero_alarm_vocabulary(self):
        """Apple's passive capture mode receives zero dedicated alarm vocabulary.
        The single alarm term ('technically a surveillance device') is hedged
        and refers to the product generically, not the passive mode specifically."""
        # None of the alarm terms specifically address passive/always-on mode
        passive_alarm_terms = [
            t for t in APPLE_ARTICLE["alarm_terms"]
            if "passive" in t.lower() or "always-on" in t.lower() or "continuous" in t.lower()
        ]
        self.assertEqual(len(passive_alarm_terms), 0)

    def test_passive_more_invasive_than_user_triggered(self):
        """Apple passive always-on capture (320x320) is arguably more
        surveillance-like than Meta's user-triggered 12MP capture."""
        apple_passive = APPLE_ARTICLE["passive_mode_always_on"]
        meta_user_triggered = not META_ARTICLE.get("passive_mode_always_on", False)
        self.assertTrue(apple_passive, "Apple has passive always-on capture")
        self.assertTrue(meta_user_triggered, "Meta requires user trigger")


class TestContractorReviewOmission(unittest.TestCase):
    """Verify Apple article doesn't explore whether Apple would also use
    contractors to review camera footage."""

    def test_meta_contractor_abuse_detailed(self):
        """Meta article details contractor abuse in content review."""
        self.assertTrue(META_ARTICLE["contractor_abuse_detailed"])

    def test_apple_contractor_review_not_explored(self):
        """Apple article does not explore whether Apple would also use
        contractors to review camera/AI footage for training."""
        self.assertFalse(APPLE_ARTICLE["contractor_abuse_detailed"])

    def test_apple_visual_intelligence_pipeline_not_questioned(self):
        """Apple's Visual Intelligence processing pipeline would likely
        involve human review for AI training, but this isn't mentioned.
        Product enthusiasm terms reference Visual Intelligence without
        questioning the review pipeline."""
        vi_terms = [t for t in APPLE_ARTICLE["product_enthusiasm_terms"]
                    if "visual intelligence" in t.lower()]
        self.assertGreaterEqual(len(vi_terms), 1,
                                "Apple article mentions Visual Intelligence positively")
        # But no alarm terms about the pipeline
        pipeline_alarm = [t for t in APPLE_ARTICLE["alarm_terms"]
                          if "review" in t.lower() or "contractor" in t.lower()
                          or "pipeline" in t.lower() or "training" in t.lower()]
        self.assertEqual(len(pipeline_alarm), 0,
                         "Apple article should have zero alarm terms about review pipeline")


class TestConfounders(unittest.TestCase):
    """Verify confounders are documented and assessed."""

    confounders = [
        {
            "id": 1,
            "strength": "STRONG",
            "description": "Different news events — Meta article covers a specific "
                           "contractor abuse scandal; Apple article covers a product leak.",
            "counterpoint": "Both are about camera-equipped wearable devices with "
                            "privacy implications.",
        },
        {
            "id": 2,
            "strength": "MODERATE",
            "description": "Temporal distance — 5.5 months apart; editorial "
                           "priorities may shift.",
            "counterpoint": "Privacy scrutiny for camera wearables arguably "
                            "intensified, not decreased, over this period.",
        },
        {
            "id": 3,
            "strength": "MODERATE",
            "description": "Source material — Meta article based on investigative "
                           "report (Svenska Dagbladet); Apple article based on "
                           "product leak (code discovery).",
            "counterpoint": "Journalist chose alarm framing beyond what the source "
                            "material required.",
        },
        {
            "id": 4,
            "strength": "WEAK",
            "description": "Form factor difference — glasses vs earbuds — but "
                           "both are camera-equipped wearables.",
            "counterpoint": "The privacy concern is the camera, not the form factor.",
        },
    ]

    def test_confounder_count(self):
        """Four confounders are documented."""
        self.assertEqual(len(self.confounders), 4)

    def test_strong_confounder_present(self):
        """At least one STRONG confounder is documented."""
        strong = [c for c in self.confounders if c["strength"] == "STRONG"]
        self.assertGreaterEqual(len(strong), 1)

    def test_each_confounder_has_counterpoint(self):
        """Each confounder includes a counterpoint."""
        for conf in self.confounders:
            self.assertTrue(len(conf["counterpoint"]) > 10,
                            f"Confounder {conf['id']} should have a substantive counterpoint")

    def test_confounder_strengths_are_valid(self):
        """All confounder strengths are valid values."""
        valid = {"STRONG", "MODERATE", "WEAK"}
        for conf in self.confounders:
            self.assertIn(conf["strength"], valid,
                          f"Confounder {conf['id']} strength '{conf['strength']}' invalid")


class TestMechanismInYAML(unittest.TestCase):
    """Verify mechanism #272 is registered in competitor-coverage-research.yaml."""

    @classmethod
    def setUpClass(cls):
        yaml_path = os.path.join(
            os.path.dirname(__file__), "..",
            "profiles", "competitor-coverage-research.yaml"
        )
        if os.path.exists(yaml_path):
            with open(yaml_path, "r") as f:
                cls.yaml_text = f.read()
        else:
            cls.yaml_text = None

    def test_yaml_file_exists(self):
        """competitor-coverage-research.yaml exists and is readable."""
        self.assertIsNotNone(self.yaml_text)
        self.assertGreater(len(self.yaml_text), 0)

    def test_mechanism_272_exists_with_steve_dent(self):
        """A mechanism for Steve Dent Engadget cross-entity exists in YAML."""
        self.assertIn("Steve Dent", self.yaml_text)
        self.assertIn("Steve Dent Engadget Cross-Entity Camera Wearable Privacy Vocabulary Gradient",
                       self.yaml_text)

    def test_mechanism_has_journalist_cross_entity_type(self):
        """The Steve Dent mechanism should be type journalist_cross_entity."""
        # Find the Steve Dent entry section and verify type
        idx = self.yaml_text.find("Steve Dent Engadget Cross-Entity")
        self.assertGreater(idx, 0, "Steve Dent mechanism should be in YAML")
        # Check nearby text for type field
        section = self.yaml_text[max(0, idx - 200):idx + 500]
        self.assertIn("journalist_cross_entity", section)


class TestSourceURLValidity(unittest.TestCase):
    """Verify source URLs are properly formatted."""

    def test_meta_url_format(self):
        """Meta article URL is a valid Engadget URL."""
        url = META_ARTICLE["url"]
        self.assertTrue(url.startswith("https://www.engadget.com/"),
                        f"Meta URL should start with https://www.engadget.com/")
        self.assertIn("moderators", url)

    def test_apple_url_format(self):
        """Apple article URL is a valid Engadget URL."""
        url = APPLE_ARTICLE["url"]
        self.assertTrue(url.startswith("https://www.engadget.com/"),
                        f"Apple URL should start with https://www.engadget.com/")
        self.assertIn("airpods", url)


if __name__ == "__main__":
    unittest.main()
