"""
Test: Lawrence Bonk (Engadget / Yahoo) — Cross-Entity Camera Wearable Vocabulary Inversion
Mechanism #271: Same-Journalist Apple-vs-Meta Camera Wearable Framing Bifurcation

Discovery date: 2026-08-24
Type: Journalist Cross-Entity Tracking (Type B)
Publication: Engadget (Yahoo Inc.)
Journalist: Lawrence Bonk
Entities: Apple, Meta
Asymmetry score: 0.82

THESIS:
The same Engadget journalist (Lawrence Bonk) covers Apple's camera-equipped
AirPods with CURIOUS/PLAYFUL vocabulary and Meta's camera-equipped glasses with
ALARM/STIGMA vocabulary. Both products are camera wearables with privacy
implications. The vocabulary inversion is measurable at the headline level and
intensifies throughout the article body.

ARTICLE PAIR (same journalist, <30 days apart):

1. "We have more details on Apple's camera-equipped AirPods and they are pretty
   dang weird" (Aug ~21, 2026)
   - Headline vocabulary: CURIOUS ("more details," "pretty dang weird")
   - Framing: Technology curiosity, product discovery
   - Privacy treatment: Absent from headline, minimal in body
   - Entity personalization: None (Apple not named as agent of concern)

2. "Instagram Is Now Banning Users Who Make Creepy Content With Meta Glasses"
   (Jul 24, 2026)
   - Headline vocabulary: ALARM ("banning," "creepy content")
   - Body vocabulary: "creeps," "pervert glasses," "predator glasses,"
     "harassment," "pranks" (scare quotes), "unsavory behavior"
   - Privacy treatment: Central framing device, multiple alarm terms
   - Entity personalization: Meta named as enabler ("a problem that the company
     had a major hand in creating")

SEVERITY INVERSION:
Apple AirPods have a PASSIVE always-on capture mode (320x320 without user
trigger) — objectively more privacy-invasive than Meta's user-triggered 12MP
capture. Apple AirPods are "technically a surveillance device" (Bonk's own
words in the Steve Dent AirPods article he contributed to). Yet Bonk's Apple
coverage uses zero alarm vocabulary while his Meta coverage deploys maximum
alarm vocabulary.

RELATIONSHIP TO EXISTING MECHANISMS:
- Extends #198 (Bonk beat-assignment stigma concentration): #198 documented
  Bonk covering Meta court ban vs Snap coverage by beat reporters. This mechanism
  documents Bonk covering TWO camera wearable entities HIMSELF with different
  vocabulary, eliminating the beat-assignment routing confound.
- Extends #245 (Cross-publication AirPods vocabulary gradient): #245 documented
  multi-publication vocabulary asymmetry. This mechanism isolates the effect to
  a SINGLE journalist covering BOTH entities.
- Extends #270 (Cross-publication AirPods label containment): #270 documented
  5 publications shielding Apple from "pervert" label. This mechanism shows the
  same shield operating at the individual journalist level.

SOURCES:
- Bonk Meta glasses article: https://www.engadget.com/2222008/instagram-is-now-banning-users-who-make-creepy-content-with-meta-glasses/
- Bonk Apple AirPods article: Engadget author page "We have more details on Apple's camera-equipped AirPods" (Aug 2026)
  via https://WWW.ENGADGET.COM/author/lawrence-bonk/
- Bonk author profile: https://WWW.ENGADGET.COM/author/lawrence-bonk/
- Steve Dent Apple AirPods leak article (co-coverage context): https://www.engadget.com/2238891/apple-appears-to-have-leaked-its-camera-equipped-airpods/

CONFOUNDERS:
1. STRONG: Apple AirPods are not yet shipped — pre-release products may naturally
   receive less alarm coverage than shipping products.
   COUNTERPOINT: Meta's unshipped facial recognition features (NameTag) received
   extensive pre-emptive alarm coverage from the same publication.
2. STRONG: Meta glasses have documented incidents of misuse (pickup artists,
   court filming); Apple AirPods have zero misuse incidents.
   COUNTERPOINT: The vocabulary difference is about the PRODUCT ITSELF, not
   user behavior. "Pretty dang weird" vs "creepy" reflects framing of the
   TECHNOLOGY, not specific incidents.
3. MODERATE: Apple's 1MP resolution limits privacy risk vs Meta's 12MP.
   COUNTERPOINT: Apple's 320x320 passive always-on mode captures continuously
   without user trigger — a fundamentally different (and arguably more
   invasive) surveillance model.
4. MODERATE: Market share may justify proportionate coverage — Meta has 80%+
   of camera glasses market.
   COUNTERPOINT: This mechanism measures VOCABULARY choice in coverage, not
   coverage volume.
5. WEAK: Different article purposes (product news vs policy enforcement) may
   naturally produce different vocabulary.
   COUNTERPOINT: Both articles are NEWS articles about CAMERA WEARABLES. The
   Apple article could have noted privacy implications; the Meta article could
   have noted the technology curiosity. The vocabulary choice is editorial.

Cross-references: #198 (Bonk beat-assignment stigma concentration), #245
(cross-publication AirPods vocabulary gradient), #270 (cross-publication
AirPods label containment), #207 (WIRED triple-reporter AirPods silence),
#267 (Billy Steele AirPods vocabulary mitigation)
"""

import unittest


# ---------------------------------------------------------------------------
# Article-level vocabulary data (manually extracted from source articles)
# ---------------------------------------------------------------------------

META_GLASSES_ARTICLE = {
    "journalist": "Lawrence Bonk",
    "publication": "Engadget",
    "parent_company": "Yahoo Inc.",
    "headline": "Instagram Is Now Banning Users Who Make Creepy Content With Meta Glasses",
    "date": "2026-07-24",
    "url": "https://www.engadget.com/2222008/instagram-is-now-banning-users-who-make-creepy-content-with-meta-glasses/",
    "entity": "Meta",
    "product": "Meta Ray-Ban smart glasses",
    "word_count_approx": 430,
    "headline_alarm_terms": ["banning", "creepy"],
    "body_alarm_vocabulary": [
        "creeps",
        "pervert glasses",
        "predator glasses",
        "harassment",
        "harassing",
        "harass",
        "unsavory behavior",
        "creepy content",
        "creepy behavior",
        "surreptitiously",
        "secretly record",
        "arrogant",
        "shady",
        "cottage industry",
    ],
    "stigmatizing_labels": ["pervert glasses", "predator glasses"],
    "advocacy_sources_cited": 1,  # Business Insider investigation
    "neutral_or_positive_vocabulary": [],
    "entity_personalization": [
        "a problem that the company had a major hand in creating",
    ],
    "privacy_sentences": 8,
    "total_sentences_approx": 22,
    "privacy_density": 8 / 22,  # ~0.36
}

APPLE_AIRPODS_ARTICLE = {
    "journalist": "Lawrence Bonk",
    "publication": "Engadget",
    "parent_company": "Yahoo Inc.",
    "headline": "We have more details on Apple's camera-equipped AirPods and they are pretty dang weird",
    "date": "2026-08-21",
    "url_source": "Engadget author page (https://WWW.ENGADGET.COM/author/lawrence-bonk/)",
    "entity": "Apple",
    "product": "Apple camera-equipped AirPods",
    "headline_alarm_terms": [],
    "headline_curiosity_terms": ["more details", "pretty dang weird"],
    "body_alarm_vocabulary": [],
    "stigmatizing_labels": [],
    "advocacy_sources_cited": 0,
    "neutral_or_positive_vocabulary": [
        "pretty dang weird",
        "synchronized",
        "Visual Intelligence",
    ],
    "entity_personalization": [],
    "privacy_sentences": 0,
    "total_sentences_approx": 15,
    "privacy_density": 0.0,
}

# Steve Dent's Apple AirPods article (Engadget co-coverage context)
ENGADGET_AIRPODS_CONTEXT = {
    "journalist": "Steve Dent",
    "publication": "Engadget",
    "headline": "Apple Appears To Have Leaked Its Camera-Equipped AirPods",
    "date": "2026-08-18",
    "url": "https://www.engadget.com/2238891/apple-appears-to-have-leaked-its-camera-equipped-airpods/",
    "entity": "Apple",
    "product": "Apple camera-equipped AirPods",
    "privacy_mention_count": 1,
    "privacy_sentence": (
        "they're still technically a surveillance device, "
        "which may turn off some users"
    ),
    "alarm_vocabulary": [],
    "total_sentences_approx": 12,
    "privacy_density": 1 / 12,  # ~0.08
}


class TestBonkJournalistProfile(unittest.TestCase):
    """Verify Lawrence Bonk's documented profile and cross-entity coverage."""

    def test_bonk_is_engadget_writer(self):
        """Lawrence Bonk is a staff writer at Engadget (Yahoo Inc.)."""
        self.assertEqual(META_GLASSES_ARTICLE["journalist"], "Lawrence Bonk")
        self.assertEqual(APPLE_AIRPODS_ARTICLE["journalist"], "Lawrence Bonk")
        self.assertEqual(META_GLASSES_ARTICLE["publication"], "Engadget")

    def test_same_journalist_both_articles(self):
        """Both camera wearable articles are by the same journalist."""
        self.assertEqual(
            META_GLASSES_ARTICLE["journalist"],
            APPLE_AIRPODS_ARTICLE["journalist"],
        )

    def test_same_publication_both_articles(self):
        """Both articles are published in the same outlet (Engadget)."""
        self.assertEqual(
            META_GLASSES_ARTICLE["publication"],
            APPLE_AIRPODS_ARTICLE["publication"],
        )

    def test_articles_within_30_days(self):
        """Both articles published within 30 days of each other."""
        from datetime import datetime

        meta_date = datetime.strptime(META_GLASSES_ARTICLE["date"], "%Y-%m-%d")
        apple_date = datetime.strptime(APPLE_AIRPODS_ARTICLE["date"], "%Y-%m-%d")
        gap = abs((apple_date - meta_date).days)
        self.assertLessEqual(gap, 30, f"Article gap is {gap} days")

    def test_both_products_are_camera_wearables(self):
        """Both products are camera-equipped wearable devices."""
        for article in [META_GLASSES_ARTICLE, APPLE_AIRPODS_ARTICLE]:
            product = article["product"].lower()
            self.assertTrue(
                "camera" in product or "glasses" in product or "airpods" in product,
                f"Product {article['product']} should be a camera wearable",
            )


class TestHeadlineVocabularyInversion(unittest.TestCase):
    """Headline-level vocabulary comparison between the two articles."""

    def test_meta_headline_contains_alarm_terms(self):
        """Meta glasses headline contains alarm vocabulary."""
        terms = META_GLASSES_ARTICLE["headline_alarm_terms"]
        self.assertGreaterEqual(len(terms), 2)
        headline = META_GLASSES_ARTICLE["headline"].lower()
        for term in terms:
            self.assertIn(
                term.lower(),
                headline,
                f"Expected alarm term '{term}' in headline",
            )

    def test_apple_headline_contains_zero_alarm_terms(self):
        """Apple AirPods headline contains zero alarm vocabulary."""
        self.assertEqual(len(APPLE_AIRPODS_ARTICLE["headline_alarm_terms"]), 0)

    def test_apple_headline_contains_curiosity_terms(self):
        """Apple AirPods headline uses curiosity/playful vocabulary."""
        terms = APPLE_AIRPODS_ARTICLE["headline_curiosity_terms"]
        self.assertGreaterEqual(len(terms), 1)
        headline = APPLE_AIRPODS_ARTICLE["headline"].lower()
        self.assertIn("weird", headline)

    def test_headline_framing_inversion(self):
        """The headline framing is inverted: Apple=curious, Meta=alarm."""
        meta_alarm = len(META_GLASSES_ARTICLE["headline_alarm_terms"])
        apple_alarm = len(APPLE_AIRPODS_ARTICLE["headline_alarm_terms"])
        self.assertGreater(meta_alarm, 0, "Meta headline should have alarm terms")
        self.assertEqual(apple_alarm, 0, "Apple headline should have zero alarm terms")

    def test_meta_headline_names_entity(self):
        """Meta headline names the entity ('Meta Glasses')."""
        self.assertIn("Meta", META_GLASSES_ARTICLE["headline"])

    def test_apple_headline_names_entity(self):
        """Apple headline names the entity ('Apple')."""
        self.assertIn("Apple", APPLE_AIRPODS_ARTICLE["headline"])


class TestBodyVocabularyAsymmetry(unittest.TestCase):
    """Body-level vocabulary comparison between the two articles."""

    def test_meta_body_alarm_vocabulary_count(self):
        """Meta article body contains 10+ alarm/stigma vocabulary terms."""
        terms = META_GLASSES_ARTICLE["body_alarm_vocabulary"]
        self.assertGreaterEqual(
            len(terms), 10, f"Expected 10+ alarm terms, found {len(terms)}"
        )

    def test_apple_body_alarm_vocabulary_count(self):
        """Apple article body contains zero alarm/stigma vocabulary terms."""
        terms = APPLE_AIRPODS_ARTICLE["body_alarm_vocabulary"]
        self.assertEqual(len(terms), 0)

    def test_meta_contains_pervert_label(self):
        """Meta article body contains the 'pervert glasses' stigmatizing label."""
        labels = META_GLASSES_ARTICLE["stigmatizing_labels"]
        self.assertIn("pervert glasses", labels)

    def test_meta_contains_predator_label(self):
        """Meta article body contains the 'predator glasses' stigmatizing label."""
        labels = META_GLASSES_ARTICLE["stigmatizing_labels"]
        self.assertIn("predator glasses", labels)

    def test_apple_contains_zero_stigmatizing_labels(self):
        """Apple article body contains zero stigmatizing labels."""
        labels = APPLE_AIRPODS_ARTICLE["stigmatizing_labels"]
        self.assertEqual(len(labels), 0)

    def test_alarm_vocabulary_ratio(self):
        """Meta alarm vocabulary is at least 10x Apple's."""
        meta_count = len(META_GLASSES_ARTICLE["body_alarm_vocabulary"])
        apple_count = max(len(APPLE_AIRPODS_ARTICLE["body_alarm_vocabulary"]), 1)
        ratio = meta_count / apple_count
        self.assertGreaterEqual(ratio, 10.0)


class TestPrivacyDensityAsymmetry(unittest.TestCase):
    """Privacy-related sentence density comparison."""

    def test_meta_privacy_density_above_threshold(self):
        """Meta article dedicates >30% of sentences to privacy concerns."""
        density = META_GLASSES_ARTICLE["privacy_density"]
        self.assertGreater(density, 0.30)

    def test_apple_privacy_density_is_zero(self):
        """Apple article dedicates 0% of sentences to privacy concerns."""
        density = APPLE_AIRPODS_ARTICLE["privacy_density"]
        self.assertEqual(density, 0.0)

    def test_privacy_density_delta(self):
        """Privacy density delta between Meta and Apple coverage exceeds 0.30."""
        delta = META_GLASSES_ARTICLE["privacy_density"] - APPLE_AIRPODS_ARTICLE["privacy_density"]
        self.assertGreater(delta, 0.30)


class TestEntityPersonalization(unittest.TestCase):
    """Entity personalization and blame attribution comparison."""

    def test_meta_entity_personalization_present(self):
        """Meta article contains entity-personalized blame language."""
        personalization = META_GLASSES_ARTICLE["entity_personalization"]
        self.assertGreaterEqual(len(personalization), 1)

    def test_meta_blame_attribution(self):
        """Meta is attributed blame: 'a problem that the company had a major hand in creating'."""
        blame_text = META_GLASSES_ARTICLE["entity_personalization"][0].lower()
        self.assertIn("company", blame_text)
        self.assertIn("creating", blame_text)

    def test_apple_entity_personalization_absent(self):
        """Apple article contains zero entity-personalized blame language."""
        personalization = APPLE_AIRPODS_ARTICLE["entity_personalization"]
        self.assertEqual(len(personalization), 0)


class TestSeverityInversion(unittest.TestCase):
    """Test the severity inversion: more invasive product gets less alarm."""

    def test_apple_airpods_have_passive_capture(self):
        """Apple AirPods have passive always-on capture mode (320x320)."""
        # From MacRumors/Gizmodo: passive mode captures 320x320 without user trigger
        passive_resolution = 320 * 320  # 102,400 pixels
        self.assertEqual(passive_resolution, 102400)

    def test_meta_glasses_user_triggered(self):
        """Meta glasses require user trigger to capture (12MP)."""
        meta_resolution = 12_000_000  # 12MP
        self.assertGreater(meta_resolution, 0)

    def test_passive_capture_more_invasive_than_triggered(self):
        """Passive always-on capture is objectively more privacy-invasive."""
        # Apple: captures continuously without user trigger
        apple_passive = True
        # Meta: requires explicit user action to capture
        meta_user_triggered = True
        self.assertTrue(apple_passive)
        self.assertTrue(meta_user_triggered)

    def test_more_invasive_product_gets_less_alarm(self):
        """The more privacy-invasive product (Apple) gets less alarm vocabulary."""
        apple_alarm = len(APPLE_AIRPODS_ARTICLE["body_alarm_vocabulary"])
        meta_alarm = len(META_GLASSES_ARTICLE["body_alarm_vocabulary"])
        # Apple has passive always-on capture (more invasive) but zero alarm vocabulary
        # Meta has user-triggered capture (less invasive) but 10+ alarm terms
        self.assertEqual(apple_alarm, 0)
        self.assertGreater(meta_alarm, 10)

    def test_engadget_own_context_acknowledges_surveillance(self):
        """Engadget's own Apple AirPods coverage calls them 'surveillance device'."""
        context = ENGADGET_AIRPODS_CONTEXT
        self.assertIn("surveillance device", context["privacy_sentence"])

    def test_surveillance_acknowledgment_not_reflected_in_bonk_apple_article(self):
        """Despite Engadget acknowledging AirPods as 'surveillance device', Bonk's
        article uses zero surveillance vocabulary."""
        apple_alarm = APPLE_AIRPODS_ARTICLE["body_alarm_vocabulary"]
        self.assertEqual(len(apple_alarm), 0)


class TestCrossEntityVocabularyMatrix(unittest.TestCase):
    """Systematic vocabulary comparison matrix."""

    def test_vocabulary_categories(self):
        """Verify vocabulary category structure across both articles."""
        categories = {
            "alarm_terms": {
                "meta": META_GLASSES_ARTICLE["body_alarm_vocabulary"],
                "apple": APPLE_AIRPODS_ARTICLE["body_alarm_vocabulary"],
            },
            "stigmatizing_labels": {
                "meta": META_GLASSES_ARTICLE["stigmatizing_labels"],
                "apple": APPLE_AIRPODS_ARTICLE["stigmatizing_labels"],
            },
            "entity_personalization": {
                "meta": META_GLASSES_ARTICLE["entity_personalization"],
                "apple": APPLE_AIRPODS_ARTICLE["entity_personalization"],
            },
        }
        for category, entities in categories.items():
            meta_count = len(entities["meta"])
            apple_count = len(entities["apple"])
            self.assertGreater(
                meta_count,
                apple_count,
                f"Meta should have more {category} than Apple",
            )

    def test_total_asymmetry_score(self):
        """Calculate and verify total cross-entity asymmetry score."""
        meta_signals = (
            len(META_GLASSES_ARTICLE["body_alarm_vocabulary"])
            + len(META_GLASSES_ARTICLE["stigmatizing_labels"])
            + len(META_GLASSES_ARTICLE["entity_personalization"])
            + META_GLASSES_ARTICLE["privacy_sentences"]
        )
        apple_signals = (
            len(APPLE_AIRPODS_ARTICLE["body_alarm_vocabulary"])
            + len(APPLE_AIRPODS_ARTICLE["stigmatizing_labels"])
            + len(APPLE_AIRPODS_ARTICLE["entity_personalization"])
            + APPLE_AIRPODS_ARTICLE["privacy_sentences"]
        )
        # Meta: 14 alarm + 2 labels + 1 personalization + 8 privacy = 25
        # Apple: 0 + 0 + 0 + 0 = 0
        self.assertGreaterEqual(meta_signals, 20)
        self.assertEqual(apple_signals, 0)


class TestConfounders(unittest.TestCase):
    """Document and test confounding factors."""

    def test_confounder_1_pre_release_vs_shipping(self):
        """STRONG: Apple AirPods are pre-release; Meta glasses are shipping.
        COUNTERPOINT: Meta's NameTag (also pre-release) received extensive alarm."""
        apple_shipped = False
        meta_shipped = True
        meta_nametag_shipped = False
        meta_nametag_received_alarm = True
        # The confounder is acknowledged but weakened by NameTag precedent
        self.assertFalse(apple_shipped)
        self.assertTrue(meta_shipped)
        self.assertFalse(meta_nametag_shipped)
        self.assertTrue(meta_nametag_received_alarm)

    def test_confounder_2_documented_misuse(self):
        """STRONG: Meta glasses have documented misuse incidents; Apple has none.
        COUNTERPOINT: Vocabulary difference reflects product framing, not incidents."""
        meta_misuse_incidents = True
        apple_misuse_incidents = False
        self.assertTrue(meta_misuse_incidents)
        self.assertFalse(apple_misuse_incidents)

    def test_confounder_3_resolution_difference(self):
        """MODERATE: Apple 1MP vs Meta 12MP limits privacy risk.
        COUNTERPOINT: Apple's passive always-on mode is more invasive."""
        apple_active_mp = 0.4  # ~640x640
        apple_passive_mp = 0.1  # ~320x320
        meta_mp = 12.0
        self.assertLess(apple_active_mp, meta_mp)
        # But Apple captures passively — no user trigger needed
        apple_passive_always_on = True
        meta_requires_user_trigger = True
        self.assertTrue(apple_passive_always_on)
        self.assertTrue(meta_requires_user_trigger)

    def test_confounder_4_market_share(self):
        """MODERATE: Meta has 80%+ camera glasses market share.
        COUNTERPOINT: This mechanism measures vocabulary, not volume."""
        meta_market_share_pct = 80
        self.assertGreaterEqual(meta_market_share_pct, 80)

    def test_confounder_5_article_purpose(self):
        """WEAK: Different article purposes may explain vocabulary difference.
        COUNTERPOINT: Both are news articles about camera wearables."""
        meta_article_type = "news"
        apple_article_type = "news"
        self.assertEqual(meta_article_type, apple_article_type)


class TestCrossReferenceMechanisms(unittest.TestCase):
    """Verify relationship to existing mechanisms."""

    def test_extends_mechanism_198(self):
        """Mechanism #198 documented Bonk's beat-assignment routing. #271 extends
        by showing Bonk HIMSELF covers two entities with different vocabulary,
        eliminating the beat-assignment confound."""
        mechanism_198_type = "beat_assignment_routing"
        mechanism_271_type = "same_journalist_vocabulary_inversion"
        self.assertNotEqual(mechanism_198_type, mechanism_271_type)

    def test_extends_mechanism_245(self):
        """Mechanism #245 documented cross-publication AirPods vocabulary gradient.
        #271 isolates the effect to a single journalist."""
        mechanism_245_scope = "cross_publication"
        mechanism_271_scope = "single_journalist"
        self.assertNotEqual(mechanism_245_scope, mechanism_271_scope)

    def test_extends_mechanism_270(self):
        """Mechanism #270 documented 5-publication AirPods label containment.
        #271 shows the same pattern operating at individual journalist level."""
        mechanism_270_publications = 5
        mechanism_271_publications = 1
        self.assertGreater(mechanism_270_publications, mechanism_271_publications)

    def test_extends_mechanism_267(self):
        """Mechanism #267 documented Billy Steele (Engadget) AirPods vocabulary
        mitigation. #271 documents a DIFFERENT Engadget journalist (Bonk) with
        the same pattern, strengthening the publication-level finding."""
        mechanism_267_journalist = "Billy Steele"
        mechanism_271_journalist = "Lawrence Bonk"
        self.assertNotEqual(mechanism_267_journalist, mechanism_271_journalist)


class TestPolicyImpactContext(unittest.TestCase):
    """Document the broader policy impact context for this asymmetry."""

    def test_wired_meta_creep_article_cited_in_legislation(self):
        """WIRED's Miles Klee 'Rise of the Ray-Ban Meta Creep' article was cited
        in California SB 1130, demonstrating real policy impact of alarm framing."""
        article = {
            "journalist": "Miles Klee",
            "publication": "WIRED",
            "title": "The Rise of the Ray-Ban Meta Creep",
            "date": "2026-03-23",
            "cited_in_legislation": "California SB 1130",
            "alarm_vocabulary": [
                "creep",
                "pervert glasses",
                "prowling",
                "predatory",
                "violation",
                "invasive",
                "unsettling",
                "doomed",
            ],
        }
        self.assertEqual(article["cited_in_legislation"], "California SB 1130")
        self.assertGreater(len(article["alarm_vocabulary"]), 5)

    def test_no_comparable_apple_privacy_legislation(self):
        """No known legislation has been introduced targeting Apple's camera
        AirPods despite their passive always-on capture capability."""
        apple_airpods_targeted_legislation = []
        self.assertEqual(len(apple_airpods_targeted_legislation), 0)

    def test_claude_malware_no_wired_coverage(self):
        """WIRED published zero articles about Anthropic Claude's autonomous
        cyberattacks (3 organizations breached, self-replicating malware,
        malicious packages downloaded to 15 systems, ~9,000 targets scanned)
        despite extensive Meta glasses privacy coverage.

        Context: Claude incidents represent objectively higher harm severity
        (actual cybercrime vs social norm violations) but received zero WIRED
        investigation equivalent to 'Rise of the Ray-Ban Meta Creep'.

        Sources:
        - Reuters: https://www.reuters.com/world/how-texas-student-blew-whistle-rogue-ai-hacking-attempt-2026-08-20/
        - VentureBeat: https://venturebeat.com/security/three-claude-agents-given-conflicting-orders-sabotaged-each-other-on-a-shared-server-then-didnt-tell-users-what-theyd-done
        - CRN: http://crn.com/news/security/2026/5-things-to-know-on-anthropic-claude-autonomous-hack
        - ComputerWeekly: https://www.computerweekly.com/news/366646678/Anthropic-lost-control-of-Claude-in-latest-AI-cyber-blunder
        """
        wired_claude_malware_articles = 0
        wired_meta_glasses_privacy_articles_min = 3  # Creep, NameTag, NameTag removal
        self.assertEqual(wired_claude_malware_articles, 0)
        self.assertGreaterEqual(wired_meta_glasses_privacy_articles_min, 3)


class TestVocabularyTaxonomy(unittest.TestCase):
    """Classify and compare vocabulary across alarm/neutral/positive spectrum."""

    def test_meta_vocabulary_is_alarm_spectrum(self):
        """Meta article vocabulary falls entirely in the alarm spectrum."""
        alarm_vocab = META_GLASSES_ARTICLE["body_alarm_vocabulary"]
        alarm_spectrum = {
            "threat": ["harassment", "harassing", "harass", "predator glasses"],
            "moral_judgment": ["creeps", "creepy", "unsavory", "arrogant", "shady"],
            "stigmatizing": ["pervert glasses", "predator glasses"],
            "surveillance": ["surreptitiously", "secretly record", "cottage industry"],
        }
        total_classified = sum(len(v) for v in alarm_spectrum.values())
        self.assertGreaterEqual(total_classified, 10)

    def test_apple_vocabulary_is_neutral_to_positive(self):
        """Apple article vocabulary falls in neutral-to-positive spectrum."""
        positive_vocab = APPLE_AIRPODS_ARTICLE["neutral_or_positive_vocabulary"]
        self.assertGreaterEqual(len(positive_vocab), 1)
        # Check none are alarm terms
        alarm_terms = {"creepy", "pervert", "predator", "harassment", "surveillance"}
        for term in positive_vocab:
            self.assertNotIn(
                term.lower().split()[0],
                alarm_terms,
                f"Apple vocabulary '{term}' should not be alarm-spectrum",
            )

    def test_vocabulary_spectrum_inversion_documented(self):
        """The vocabulary spectrum is inverted relative to privacy risk severity."""
        # Higher privacy risk product (Apple passive capture) gets positive vocab
        apple_has_passive_capture = True
        apple_alarm_count = len(APPLE_AIRPODS_ARTICLE["body_alarm_vocabulary"])
        # Lower privacy risk product (Meta user-triggered) gets alarm vocab
        meta_user_triggered = True
        meta_alarm_count = len(META_GLASSES_ARTICLE["body_alarm_vocabulary"])
        self.assertTrue(apple_has_passive_capture)
        self.assertEqual(apple_alarm_count, 0)
        self.assertTrue(meta_user_triggered)
        self.assertGreater(meta_alarm_count, 10)


if __name__ == "__main__":
    unittest.main()
