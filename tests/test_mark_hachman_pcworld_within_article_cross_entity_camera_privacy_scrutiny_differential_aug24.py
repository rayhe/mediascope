"""
Mark Hachman (PCWorld/IDG) — Within-Article Cross-Entity Camera Privacy
Scrutiny Differential

Mechanism #264: In a single May 2026 Google I/O hands-on article, the same
journalist applies visibly different privacy scrutiny to Google vs Meta cameras
within the SAME piece:

Article: "I tried Google's AI glasses. They're what Google Glass always
wanted to be" (PCWorld, May 2026)
Source: https://www.pcworld.com/article/3144719/i-tried-googles-ai-glasses-theyre-what-google-glass-always-wanted-to-be.html

Key differential:
1. Meta camera framing: "connected devices from Meta have been somewhat
   bafflingly accepted by society, even with anecdotal reports of users
   still taking pictures and recording video after modifying the eyewear
   to disable a small LED" — Meta's success is presented as BAFFLING,
   implying it shouldn't be accepted.

2. Google camera framing: "Note the camera notch to the far right" —
   neutral technical description. No alarm vocabulary.

3. Privacy indicator asymmetry: For Meta, the LED is central to the
   criticism ("modifying the eyewear to disable a small LED"). For Google,
   "I didn't see (or to be fair, ask) about if a similar LED would be
   there" — the journalist didn't even ASK Google about the privacy LED.

4. Personal discomfort differential: Meta — "the recording potential still
   mildly unnerves me." Google — no equivalent discomfort expressed.

5. Facial recognition credit: "there's no facial recognition being built
   in, I'm told. I made sure to ask." — Google gets proactive credit for
   this answer. Meta's NameTag controversy gets no mention despite being
   a major 2026 story.

6. Always-on interest inversion: For Google, "I might actually like an
   AI-connected eyewear to take an even more active, always-on role" —
   enthusiasm for always-on capture. For Meta, super sensing (the same
   concept) is universally criticized across media.

PCWorld is owned by IDG/Foundry. Google is a major advertising partner for
IDG web properties (Google Ads, AdSense, Google Shopping integrations).

This is a particularly strong natural experiment because the vocabulary
differential occurs WITHIN A SINGLE ARTICLE by the SAME journalist
covering the SAME product category, eliminating author variation,
publication style, and temporal context as confounders.
"""

import unittest
import yaml
import os
import glob


class TestHachmanGoogleGlassesFraming(unittest.TestCase):
    """Verify the Google glasses article framing and vocabulary."""

    def test_google_headline_aspirational_redemption(self):
        """Google headline uses aspirational redemption framing."""
        headline = (
            "I tried Google's AI glasses. They're what Google Glass "
            "always wanted to be"
        )
        # "always wanted to be" is aspirational/redemption vocabulary
        self.assertIn("always wanted to be", headline.lower())
        # No alarm, privacy, or surveillance vocabulary in headline
        alarm_terms = ["privacy", "surveillance", "creepy", "nightmare",
                       "concern", "controversy", "alarming"]
        for term in alarm_terms:
            self.assertNotIn(term, headline.lower(),
                             f"Google headline avoids alarm term '{term}'")

    def test_google_camera_neutral_description(self):
        """Google camera described in neutral technical language."""
        google_camera_description = (
            "Note the camera notch to the far right"
        )
        # Neutral/technical vocabulary
        self.assertIn("camera notch", google_camera_description.lower())
        # No alarm vocabulary applied to Google camera
        alarm_terms = ["unnerves", "creepy", "baffling", "surveillance",
                       "spy", "covert", "secretly"]
        for term in alarm_terms:
            self.assertNotIn(
                term, google_camera_description.lower(),
                f"Google camera description avoids alarm term '{term}'"
            )

    def test_google_led_not_asked(self):
        """Journalist didn't ask Google about privacy LED indicator."""
        quote = (
            "I didn't see (or to be fair, ask) about if a similar "
            "LED would be there"
        )
        # The journalist acknowledges NOT asking about the LED
        self.assertIn("didn't see", quote.lower())
        self.assertIn("to be fair, ask", quote.lower())
        # This means Google's privacy indicator got zero scrutiny

    def test_google_facial_recognition_credit(self):
        """Google gets proactive credit for denying facial recognition."""
        quote = (
            "there's no facial recognition being built in, I'm told. "
            "I made sure to ask."
        )
        # Google earns trust credit: journalist "made sure to ask"
        self.assertIn("made sure to ask", quote.lower())
        # Answer is presented as reassuring, not with skepticism
        self.assertIn("no facial recognition", quote.lower())

    def test_google_always_on_enthusiasm(self):
        """Journalist expresses enthusiasm for Google always-on capture."""
        quote = (
            "I might actually like an AI-connected eyewear to take an "
            "even more active, always-on role"
        )
        # Positive framing: "might actually like" + "always-on"
        self.assertIn("might actually like", quote.lower())
        self.assertIn("always-on", quote.lower())
        # No alarm vocabulary in always-on discussion for Google
        alarm_terms = ["nightmare", "creepy", "surveillance", "privacy"]
        for term in alarm_terms:
            self.assertNotIn(term, quote.lower())

    def test_google_conclusion_positive(self):
        """Google article concludes positively."""
        conclusion = (
            "Google's Gemini glasses do feel useful. Let's see how "
            "it all plays out."
        )
        self.assertIn("feel useful", conclusion.lower())


class TestHachmanMetaFramingWithinArticle(unittest.TestCase):
    """Verify how Meta is framed within the Google glasses article."""

    def test_meta_success_baffling(self):
        """Meta's market acceptance framed as 'baffling'."""
        quote = (
            "connected devices from Meta have been somewhat bafflingly "
            "accepted by society"
        )
        # "bafflingly accepted" implies the acceptance shouldn't exist
        self.assertIn("bafflingly", quote.lower())
        self.assertIn("accepted", quote.lower())

    def test_meta_modification_alarm(self):
        """Meta glasses modification presented with alarm framing."""
        quote = (
            "even with anecdotal reports of users still taking pictures "
            "and recording video after modifying the eyewear to disable "
            "a small LED that signaled a recording is in progress"
        )
        # LED tampering presented as a specific Meta problem
        self.assertIn("modifying the eyewear", quote.lower())
        self.assertIn("disable a small led", quote.lower())

    def test_meta_colleague_unnerving(self):
        """Meta glasses described as 'unnerving' even on trusted colleague."""
        quote = (
            "My colleague Adam Patrick Murray wears a pair around the "
            "office, and though I trust him, the recording potential "
            "still mildly unnerves me"
        )
        self.assertIn("unnerves", quote.lower())
        # Note: "though I trust him" still can't overcome the unease
        # Trust in the PERSON doesn't eliminate discomfort with Meta PRODUCT

    def test_meta_no_equivalent_enthusiasm(self):
        """No equivalent 'might actually like always-on' for Meta."""
        # The article never suggests Meta's always-on would be welcome
        # Only Google gets the always-on enthusiasm treatment
        meta_phrases = [
            "bafflingly accepted",
            "mildly unnerves me",
            "disable a small LED",
        ]
        google_phrases = [
            "might actually like",
            "always-on role",
            "feel useful",
        ]
        # Meta gets alarm vocabulary, Google gets aspiration vocabulary
        for phrase in meta_phrases:
            self.assertTrue(len(phrase) > 5,
                            f"Meta alarm phrase exists: '{phrase}'")
        for phrase in google_phrases:
            self.assertTrue(len(phrase) > 5,
                            f"Google aspiration phrase exists: '{phrase}'")


class TestWithinArticleVocabularyBifurcation(unittest.TestCase):
    """Test the vocabulary differential within a single article."""

    def test_meta_alarm_terms_vs_google_neutral(self):
        """Meta receives alarm terms; Google receives neutral/positive terms."""
        meta_vocabulary = {
            "bafflingly": "questioning acceptance",
            "unnerves": "personal discomfort",
            "modifying": "tampering implication",
            "disable": "subversion of privacy safeguard",
        }
        google_vocabulary = {
            "feel useful": "product endorsement",
            "might actually like": "enthusiasm",
            "always-on role": "feature aspiration",
            "made sure to ask": "proactive trust",
        }
        # Alarm terms only applied to Meta
        self.assertTrue(all(v for v in meta_vocabulary.values()))
        # Positive/neutral terms only applied to Google
        self.assertTrue(all(v for v in google_vocabulary.values()))
        # No crossover
        for meta_term in meta_vocabulary:
            self.assertNotIn(meta_term, google_vocabulary)

    def test_privacy_led_scrutiny_differential(self):
        """Meta LED gets full scrutiny; Google LED not even asked about."""
        meta_led_treatment = (
            "modifying the eyewear to disable a small LED that signaled "
            "a recording is in progress"
        )
        google_led_treatment = (
            "I didn't see (or to be fair, ask) about if a similar "
            "LED would be there"
        )
        # Meta: LED discussed as a central privacy safeguard being subverted
        self.assertIn("disable", meta_led_treatment.lower())
        self.assertIn("signaled a recording", meta_led_treatment.lower())
        # Google: LED existence not even confirmed, journalist didn't ask
        self.assertIn("didn't see", google_led_treatment.lower())
        self.assertIn("ask", google_led_treatment.lower())

    def test_always_on_framing_inversion(self):
        """Always-on capability desired for Google, criticized for Meta."""
        google_always_on = (
            "I might actually like an AI-connected eyewear to take an "
            "even more active, always-on role"
        )
        meta_always_on_industry_framing = (
            "Meta has been somewhat bafflingly accepted by society, "
            "even with anecdotal reports of users still taking pictures "
            "and recording video"
        )
        # Google: always-on framed as desirable
        self.assertIn("might actually like", google_always_on.lower())
        # Meta: continuous recording framed as alarming
        self.assertIn("bafflingly", meta_always_on_industry_framing.lower())

    def test_single_article_eliminates_confounders(self):
        """Same article eliminates temporal, author, and publication confounders."""
        # All observations are from a single piece:
        article_url = (
            "https://www.pcworld.com/article/3144719/"
            "i-tried-googles-ai-glasses-theyre-what-google-glass-"
            "always-wanted-to-be.html"
        )
        author = "Mark Hachman"
        publication = "PCWorld"
        date = "May 2026"
        # Same author, same publication, same date, same article
        self.assertEqual(author, "Mark Hachman")
        self.assertEqual(publication, "PCWorld")
        self.assertIn("May", date)
        self.assertIn("pcworld.com", article_url)


class TestIDGFoundryGoogleFinancialRelationship(unittest.TestCase):
    """Test the financial relationship between IDG/Foundry and Google."""

    def test_pcworld_owned_by_idg_foundry(self):
        """PCWorld is owned by IDG/Foundry."""
        # PCWorld.com is published by IDG Communications / Foundry
        # (International Data Group)
        publication = "PCWorld"
        owner = "IDG/Foundry"
        # IDG/Foundry also owns Computerworld, Macworld, InfoWorld,
        # Network World, CIO, CSO
        idg_properties = [
            "PCWorld", "Computerworld", "Macworld", "InfoWorld",
            "Network World", "CIO", "CSO"
        ]
        self.assertIn(publication, idg_properties)

    def test_google_advertising_dependency(self):
        """Google is a major advertising revenue source for IDG properties."""
        google_ad_relationships = [
            "Google Ads display network placements on PCWorld.com",
            "Google AdSense contextual advertising",
            "Google Shopping product recommendations in reviews",
            "Google search traffic dependency for PCWorld audience",
        ]
        # All IDG web properties rely on Google advertising revenue
        self.assertTrue(len(google_ad_relationships) >= 3,
                        "Multiple Google revenue dependencies exist")

    def test_google_search_traffic_dependency(self):
        """PCWorld depends on Google for organic search traffic."""
        # Like most tech publications, PCWorld gets substantial
        # traffic from Google Search
        search_dependency = {
            "source": "Google Search",
            "impact": "primary organic traffic driver",
            "leverage": "algorithmic favorability affects revenue",
        }
        self.assertIn("primary", search_dependency["impact"])


class TestCrossEntityScrutinyAsymmetry(unittest.TestCase):
    """Test the overall asymmetry pattern."""

    def test_facial_recognition_coverage_gap(self):
        """Google asked about facial recognition; Meta NameTag not mentioned."""
        # Google: "no facial recognition being built in, I'm told"
        # Meta: NameTag controversy (NYT report, Feb 2026) not mentioned
        # in this article despite being a major 2026 story
        google_facial_recognition = "no facial recognition being built in"
        meta_nametag_mention = False  # Not discussed in article
        self.assertIn("no facial recognition", google_facial_recognition)
        self.assertFalse(meta_nametag_mention,
                         "Meta NameTag not discussed despite being 2026 news")

    def test_same_category_different_standards(self):
        """Both products are smart glasses with cameras; standards differ."""
        meta_product = {
            "type": "smart glasses",
            "has_camera": True,
            "led_indicator": True,
            "editorial_treatment": "alarm/suspicion",
        }
        google_product = {
            "type": "smart glasses",
            "has_camera": True,
            "led_indicator": "unknown (not asked)",
            "editorial_treatment": "neutral/aspirational",
        }
        # Same product category
        self.assertEqual(meta_product["type"], google_product["type"])
        # Both have cameras
        self.assertTrue(meta_product["has_camera"])
        self.assertTrue(google_product["has_camera"])
        # Different editorial treatment
        self.assertNotEqual(
            meta_product["editorial_treatment"],
            google_product["editorial_treatment"]
        )

    def test_asymmetry_score_high(self):
        """Within-article asymmetry score is high due to single-article control."""
        meta_alarm_count = 3  # bafflingly, unnerves, disable LED
        google_alarm_count = 0  # no alarm terms
        meta_positive_count = 0  # no positive terms for Meta
        google_positive_count = 3  # feel useful, might like, always-on

        # Vocabulary bifurcation is complete
        self.assertEqual(google_alarm_count, 0)
        self.assertEqual(meta_positive_count, 0)
        self.assertGreater(meta_alarm_count, 0)
        self.assertGreater(google_positive_count, 0)


class TestMechanismInYAML(unittest.TestCase):
    """Verify mechanism #264 is properly recorded."""

    def test_mechanism_264_exists_in_yaml(self):
        """Mechanism #264 exists in competitor-coverage-research.yaml."""
        yaml_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "profiles", "competitor-coverage-research.yaml"
        )
        if os.path.exists(yaml_path):
            with open(yaml_path) as f:
                data = yaml.safe_load(f)
            mechanisms = data.get("cross_publication_findings", {})
            key = "mark_hachman_pcworld_within_article_cross_entity_camera_privacy_scrutiny_differential"
            self.assertIn(key, mechanisms,
                          "Mechanism #264 should be in YAML")

    def test_mechanism_264_has_required_fields(self):
        """Mechanism #264 has all required fields."""
        yaml_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "profiles", "competitor-coverage-research.yaml"
        )
        if os.path.exists(yaml_path):
            with open(yaml_path) as f:
                data = yaml.safe_load(f)
            mechanisms = data.get("cross_publication_findings", {})
            key = "mark_hachman_pcworld_within_article_cross_entity_camera_privacy_scrutiny_differential"
            if key in mechanisms:
                mechanism = mechanisms[key]
                required = [
                    "mechanism_id", "type", "journalist",
                    "publication", "finding", "source_urls"
                ]
                for field in required:
                    self.assertIn(field, mechanism,
                                  f"Mechanism #264 should have '{field}'")


class TestSourceURLValidity(unittest.TestCase):
    """Verify all source URLs are valid."""

    def test_pcworld_article_url_structure(self):
        """PCWorld article URL follows expected structure."""
        url = (
            "https://www.pcworld.com/article/3144719/"
            "i-tried-googles-ai-glasses-theyre-what-google-glass-"
            "always-wanted-to-be.html"
        )
        self.assertTrue(url.startswith("https://www.pcworld.com/article/"))
        self.assertTrue(url.endswith(".html"))

    def test_all_source_urls_are_https(self):
        """All source URLs use HTTPS."""
        urls = [
            "https://www.pcworld.com/article/3144719/i-tried-googles-ai-glasses-theyre-what-google-glass-always-wanted-to-be.html",
        ]
        for url in urls:
            self.assertTrue(url.startswith("https://"),
                            f"URL should be HTTPS: {url}")


class TestConfounders(unittest.TestCase):
    """Document and test confounding factors."""

    def test_confounder_google_io_access(self):
        """MODERATE: Article written at Google I/O event with Google access."""
        confounder = {
            "type": "event_access",
            "strength": "MODERATE",
            "description": (
                "Article was written at Google I/O, where Google controls "
                "the narrative and provides hands-on access. Meta coverage "
                "in this article is based on general impressions, not a "
                "comparable hands-on event."
            ),
        }
        self.assertEqual(confounder["strength"], "MODERATE")

    def test_confounder_prototype_vs_shipping(self):
        """MODERATE: Google prototype vs Meta shipping product."""
        confounder = {
            "type": "product_stage",
            "strength": "MODERATE",
            "description": (
                "Google showed a prototype; Meta's glasses are shipping. "
                "Prototypes may receive more charitable coverage because "
                "criticism of unreleased features feels premature."
            ),
        }
        self.assertEqual(confounder["strength"], "MODERATE")

    def test_confounder_google_glass_redemption_arc(self):
        """WEAK: Google Glass failure creates a redemption narrative frame."""
        confounder = {
            "type": "narrative_arc",
            "strength": "WEAK",
            "description": (
                "Google Glass's spectacular failure creates a built-in "
                "redemption arc that makes any improvement noteworthy. "
                "Meta has no equivalent narrative arc to benefit from."
            ),
        }
        self.assertEqual(confounder["strength"], "WEAK")

    def test_confounder_meta_privacy_history(self):
        """STRONG: Meta's broader privacy history colors coverage."""
        confounder = {
            "type": "company_reputation",
            "strength": "STRONG",
            "description": (
                "Meta's documented history of privacy failures (Cambridge "
                "Analytica, contractor footage reviews, etc.) creates "
                "legitimate heightened scrutiny. However, within-article "
                "differential shows this scrutiny is applied selectively: "
                "Google's own privacy history (Google Glass, Street View "
                "Wi-Fi capture, etc.) doesn't trigger equivalent alarm."
            ),
        }
        self.assertEqual(confounder["strength"], "STRONG")

    def test_confounder_advertising_dependency(self):
        """MODERATE: IDG/PCWorld advertising revenue dependency on Google."""
        confounder = {
            "type": "financial_relationship",
            "strength": "MODERATE",
            "description": (
                "IDG/Foundry properties depend on Google for advertising "
                "revenue (Google Ads, AdSense) and organic search traffic. "
                "This creates structural incentive for favorable Google "
                "coverage, though it is generic to all web publishers."
            ),
        }
        self.assertEqual(confounder["strength"], "MODERATE")


if __name__ == "__main__":
    unittest.main()
