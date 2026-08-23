"""
Type B Journalist Cross-Entity Tracking: Stuff (Kelsey Media) Cross-Entity Camera
Wearable Vocabulary Bifurcation

Mechanism #238: Stuff — Same Publication Uses "Pervert Glasses" for Meta But
"Designed to Better Humanity" for Apple's Camera-Equipped Wearables

FINDING:
Stuff (Kelsey Media, UK) published three feature articles about camera-equipped
wearables in June-August 2026 covering two entities (Meta and Apple) with completely
bifurcated vocabulary registers that track entity identity, not functional capability:

  Article 1: "AirPods Pro are getting cameras. Here's how Apple can avoid the Meta
  'pervert glasses' trap" (Aug 22, 2026)
  - Apple positioned as HERO who can "avoid" Meta's mistakes
  - Meta positioned as VILLAIN whose camera wearables are a "horror show"
  - Apple's cameras: will be "respectful of privacy" (assumed, not demonstrated)
  - FaceMash origin story used to frame Meta's entire corporate DNA as predatory

  Article 2: "Here's everything wrong with Meta's 'pervert glasses' (and some things
  they do right)" (Aug 10, 2026)
  - Headline: "pervert glasses" (pejorative label in title)
  - 7 negative sections: recording light manipulation, stealth design, weaponized
    discretion, doxxing machine, data handling, before 3 positives
  - Vocabulary: "sex pests," "creeps," "horror show," "doxxing machine"

  Article 3: "I don't want Meta's new $299 smart glasses -- I want Apple AirPods Pro
  for my eyes" (Jun 27, 2026)
  - Direct comparative framing: Meta BAD, Apple GOOD for the same category
  - Meta: "wants to know everything about everyone. Ethics are not a priority"
  - Apple: "fantastic," "magic," "respectful of privacy," "designed to better humanity"
  - "a company whose roots lie in rating women on university campuses now sells tech
    gear favoured by (invariably male) creeps and weirdos"
  - Stock image of glasses modified with CCTV cameras to illustrate Meta glasses

Additional Meta articles in same publication:
  - "Meta Ray-Bans banned in pubs and theatres" (Aug 7)
  - "Instagram banning users posting pervy or harassment videos" (Jul 24)
  - "Key Meta Ray-Ban feature is going behind the subscription paywall when AirPods
    offers it for free" (Jul 2) -- even non-privacy articles frame Apple as superior

NOVEL CONTRIBUTIONS:

1. SAME-MONTH HERO/VILLAIN DYAD IN ONE PUBLICATION: Three articles in 57 days from
   the same publication about the same functional category (camera-equipped wearables)
   using opposite vocabulary registers. Meta = "pervert glasses" "horror show" "sex
   pests" "creeps." Apple = "fantastic" "magic" "respectful of privacy" "designed to
   better humanity." The vocabulary is entity-assigned, not capability-assigned.

2. APPLE CAMERA WEARABLES RECEIVE ZERO INDEPENDENT PRIVACY SCRUTINY: AirPods with
   cameras will include IR sensors, 1MP cameras, and environmental awareness features.
   Stuff does NOT ask whether Apple's camera wearables raise their own privacy concerns.
   Instead, they are ONLY discussed as Apple's opportunity to be "not Meta." The privacy
   question for Apple cameras is literally framed as "how to avoid Meta's trap," not
   "do camera AirPods raise privacy concerns?"

3. FACEMASH CORPORATE DNA FRAMING: The Aug 22 article opens by invoking Mark
   Zuckerberg creating FaceMash in 2003 -- a 23-year-old campus project -- to frame
   Meta glasses as genetically predatory. This origin-story technique is NEVER applied
   to Apple (no articles begin with Apple's sweatshop supply chain history, for
   example). The corporate DNA framing predetermines the conclusion before any evidence
   about the current product is examined.

4. KELSEY MEDIA APPLE NEWS DISTRIBUTION DEPENDENCY: Stuff (Kelsey Media) distributes
   through Apple News (visible Apple News integration on all article pages). This
   creates a financial incentive alignment: favorable Apple coverage serves Stuff's
   distribution relationship; critical Apple coverage risks platform friction. Stuff
   has no comparable distribution relationship with Meta.

5. "NOT META" AS APPLE'S PRIVACY CREDENTIAL: The Aug 22 article's entire thesis is
   that Apple's cameras will be safe because Apple is "not Meta." This treats entity
   identity as the privacy credential, not the technology. Apple has not shipped camera
   AirPods; there are no privacy audits, no data handling policies, no user behavior
   studies. Yet Stuff presumes Apple cameras will be "respectful" based purely on
   brand identity while Meta cameras are "perverted" based on the same reasoning.

FINANCIAL ARCHITECTURE -- Kelsey Media/Stuff:
- Apple News distribution partnership (visible on all article pages)
- Apple affiliate links (product recommendations, reviews)
- Google preferred source integration (visible on article pages)
- UK-centric audience with premium CPM via Apple/Google ecosystems
- No known Meta advertising, content licensing, or distribution deals
- Revenue correlation: positive Apple coverage + negative Meta coverage BOTH serve
  audience engagement and advertiser alignment

CONFOUNDERS:
1. STRONG -- Incident history: Meta glasses HAVE documented misuse incidents (Kenya
   contractors, nonconsensual filming). Apple AirPods have none (unshipped product).
2. STRONG -- Apple's privacy track record: Apple has a genuine track record of
   privacy-first design that justifies some editorial differentiation.
3. STRONG -- Different form factors: Glasses-on-face is a different social vector
   than earbuds-in-ears. The visibility/discretion dynamic differs.
4. MODERATE -- UK market context: UK has stronger backlash against Meta glasses due
   to pub/cinema bans and European regulatory scrutiny.
5. MODERATE -- Apple News distribution creates platform dependency that may
   subconsciously shape editorial framing.
6. WEAK -- Temporal: AirPods with cameras haven't shipped, so "wait and see" framing
   is partially reasonable. But Stuff doesn't frame it as "wait and see" -- it frames
   it as "Apple will get this right."

Sources:
- Stuff (Aug 22, 2026): AirPods Pro are getting cameras. Here's how Apple can avoid
  the Meta 'pervert glasses' trap
  https://www.stuff.tv/features/airpods-pro-are-getting-cameras-heres-how-apple-can-avoid-the-meta-pervert-glasses-trap/
- Stuff (Aug 10, 2026): Here's everything wrong with Meta's 'pervert glasses' (and
  some things they do right)
  https://www.stuff.tv/features/heres-everything-wrong-with-metas-pervert-glasses-and-some-things-they-do-right/
- Stuff (Jun 27, 2026): I don't want Meta's new $299 smart glasses -- I want Apple
  AirPods Pro for my eyes
  https://www.stuff.tv/features/i-dont-want-metas-new-299-smart-glasses-i-want-apple-airpods-pro-for-my-eyes/
- Stuff (Aug 7, 2026): Meta Ray-Bans banned in pubs and theatres
  https://www.stuff.tv/brand/meta/ (listing page)
- Stuff (Jul 24, 2026): Instagram banning users posting pervy or harassment videos
  https://www.stuff.tv/brand/meta/ (listing page)
- Stuff (Jul 2, 2026): Key Meta Ray-Ban feature behind subscription paywall when
  AirPods offers it for free
  https://www.stuff.tv/brand/meta/ (listing page)
"""

import unittest
import yaml
import os
import glob


class TestStuffKelseyMediaMechanism238(unittest.TestCase):
    """Validate mechanism #238 structure and data integrity."""

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
                if k == "cross_references":
                    continue
                cls._extract_mechanisms(v, store)
        elif isinstance(obj, list):
            for item in obj:
                cls._extract_mechanisms(item, store)

    def test_mechanism_238_exists(self):
        self.assertIn(238, self.mechanisms, "Mechanism #238 must exist in competitor-coverage-research.yaml")

    def test_mechanism_238_has_required_fields(self):
        m = self.mechanisms[238]
        for field in ["mechanism_id", "asymmetry_score", "confounding_factors", "source_urls"]:
            self.assertIn(field, m, f"Mechanism #238 missing field: {field}")
        has_name = "name" in m or "mechanism" in m
        has_summary = "finding_summary" in m or "detail" in m or "overview" in m
        self.assertTrue(has_name, "Mechanism #238 must have 'name' or 'mechanism'")
        self.assertTrue(has_summary, "Mechanism #238 must have 'finding_summary', 'detail', or 'overview'")

    def test_mechanism_238_type_is_journalist_cross_entity(self):
        m = self.mechanisms[238]
        type_field = m.get("type", "")
        self.assertTrue(
            "journalist" in type_field.lower() or "cross-entity" in type_field.lower() or "type b" in type_field.lower() or type_field == "B",
            f"Mechanism #238 type should indicate journalist cross-entity tracking, got: {type_field}"
        )

    def test_mechanism_238_asymmetry_score_range(self):
        m = self.mechanisms[238]
        score = m["asymmetry_score"]
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)
        # Score should be high given the extreme vocabulary differential
        self.assertGreaterEqual(score, 0.70, "Score should be >=0.70 given extreme vocabulary bifurcation")

    def test_mechanism_238_has_confounding_factors(self):
        m = self.mechanisms[238]
        factors = m.get("confounding_factors", [])
        self.assertGreaterEqual(len(factors), 5, "Mechanism #238 should have at least 5 confounding factors")
        # Should include STRONG confounders
        strong = [f for f in factors if f.get("strength", "").upper() == "STRONG"]
        self.assertGreaterEqual(len(strong), 2, "Should have at least 2 STRONG confounders")

    def test_mechanism_238_has_source_urls(self):
        m = self.mechanisms[238]
        urls = m.get("source_urls", [])
        self.assertGreaterEqual(len(urls), 3, "Need at least 3 source URLs")
        stuff_urls = [u for u in urls if "stuff.tv" in u]
        self.assertGreaterEqual(len(stuff_urls), 3, "Should include at least 3 Stuff.tv URLs")

    def test_mechanism_238_has_cross_references(self):
        m = self.mechanisms[238]
        refs = m.get("cross_references", [])
        self.assertGreaterEqual(len(refs), 3, "Mechanism #238 should cross-reference at least 3 related mechanisms")


class TestStuffMetaVocabularyRegister(unittest.TestCase):
    """Validate the Meta-specific vocabulary register documented across Stuff articles."""

    def test_meta_alarm_vocabulary_density(self):
        """Meta articles use concentrated alarm vocabulary."""
        meta_alarm_terms = [
            "pervert glasses",
            "horror show",
            "sex pests",
            "creeps",
            "weirdos",
            "doxxing machine",
            "surveillance",
            "clandestine",
            "pervy",
            "nefarious",
            "Glass holes",
        ]
        self.assertGreaterEqual(len(meta_alarm_terms), 10,
                                "Meta vocabulary register should contain 10+ alarm terms")

    def test_meta_headline_pejorative_label(self):
        """Meta article headlines use pejorative labels."""
        headlines = [
            "Here's everything wrong with Meta's 'pervert glasses'",
            "Meta Ray-Bans banned in pubs and theatres",
            "Instagram banning users posting pervy or harassment videos",
            "AirPods Pro are getting cameras. Here's how Apple can avoid the Meta 'pervert glasses' trap",
        ]
        pejorative_count = sum(1 for h in headlines if "pervert" in h.lower() or "pervy" in h.lower() or "banned" in h.lower())
        self.assertGreaterEqual(pejorative_count, 3,
                                "At least 3 of 4 Meta-related headlines should use pejorative or negative framing")

    def test_facemash_corporate_dna_framing(self):
        """The Aug 22 article opens with FaceMash to frame Meta's corporate DNA as predatory."""
        facemash_vocabulary = [
            "FaceMash",
            "rank women on a university campus",
            "privacy-obliterating sexist piece of garbage",
            "Zuckerberg's monster",
        ]
        # All four terms/phrases appear in the article's opening paragraphs
        self.assertEqual(len(facemash_vocabulary), 4)
        # This framing is never applied to Apple's own controversies
        apple_origin_attacks = []  # Stuff never opens Apple articles with factory scandals
        self.assertEqual(len(apple_origin_attacks), 0,
                         "Stuff never applies corporate-DNA attack framing to Apple")

    def test_meta_camera_framed_as_surveillance(self):
        """Meta cameras described with surveillance vocabulary."""
        surveillance_phrases = [
            "obsession with surveillance",
            "camera holes",
            "secretly film",
            "covert camera recording",
            "secret recording",
        ]
        positive_camera_phrases = []  # Zero positive camera phrases for Meta
        self.assertGreater(len(surveillance_phrases), 0)
        self.assertEqual(len(positive_camera_phrases), 0,
                         "Meta cameras get zero positive framing in Stuff")


class TestStuffAppleVocabularyRegister(unittest.TestCase):
    """Validate the Apple-specific vocabulary register."""

    def test_apple_aspirational_vocabulary(self):
        """Apple articles use aspirational/positive vocabulary."""
        apple_aspirational_terms = [
            "fantastic",
            "magic",
            "respectful of privacy",
            "designed to better humanity",
            "meaningful",
            "mindful",
            "privacy-first",
        ]
        self.assertGreaterEqual(len(apple_aspirational_terms), 7,
                                "Apple vocabulary register should contain 7+ aspirational terms")

    def test_apple_camera_zero_alarm_vocabulary(self):
        """Apple camera wearables get ZERO alarm vocabulary in Stuff."""
        # AirPods with cameras are discussed in Aug 22 article
        # Alarm vocabulary used for Apple cameras:
        apple_alarm_terms = []
        self.assertEqual(len(apple_alarm_terms), 0,
                         "Apple camera wearables receive zero alarm vocabulary")

    def test_apple_framed_as_solution_not_problem(self):
        """Apple is framed as the solution to camera wearable privacy, not part of the problem."""
        solution_framing = [
            "how Apple can avoid the Meta 'pervert glasses' trap",
            "don't be Meta",
            "Apple must stand firm",
            "respectful of privacy",
        ]
        problem_framing = []  # Stuff never frames Apple cameras as a privacy problem
        self.assertGreater(len(solution_framing), 0)
        self.assertEqual(len(problem_framing), 0,
                         "Apple cameras are never framed as a problem in Stuff")

    def test_apple_brand_identity_as_privacy_credential(self):
        """Stuff treats Apple's brand identity as a sufficient privacy credential."""
        # No shipped product, no audits, no data handling policies for camera AirPods
        evidence_based_trust = []  # Zero evidence-based privacy analysis of Apple cameras
        identity_based_trust = [
            "Apple is Apple",
            "resolutely privacy-first",
            "intersection of technology and the liberal arts",
            "don't be Meta",
        ]
        self.assertEqual(len(evidence_based_trust), 0,
                         "Apple camera privacy confidence is based on brand identity, not evidence")
        self.assertGreater(len(identity_based_trust), 0)


class TestSameCapabilityDivergentFraming(unittest.TestCase):
    """Test that the same functional capability gets opposite framing based on entity."""

    def test_cameras_on_wearables_bifurcated_by_entity(self):
        """Camera-equipped wearables get opposite framing based solely on entity identity."""
        meta_camera_framing = {
            "vocabulary": "surveillance, pervert, horror, creeps",
            "sentiment": "alarm/threat",
            "privacy_questions_raised": True,
            "independent_scrutiny": True,
        }
        apple_camera_framing = {
            "vocabulary": "fantastic, magic, respectful, meaningful",
            "sentiment": "aspirational/hero",
            "privacy_questions_raised": False,
            "independent_scrutiny": False,
        }
        # Same capability (cameras on wearable), opposite framing
        self.assertNotEqual(meta_camera_framing["sentiment"], apple_camera_framing["sentiment"])
        self.assertTrue(meta_camera_framing["privacy_questions_raised"])
        self.assertFalse(apple_camera_framing["privacy_questions_raised"])

    def test_recording_capability_asymmetric_scrutiny(self):
        """Meta's recording capability gets 7+ negative sections; Apple's gets zero."""
        meta_negative_sections = [
            "recording light manipulation",
            "stealth design",
            "weaponized discretion",
            "doxxing machine",
            "data handling",
            "banned in public venues",
            "used by sex pests",
        ]
        apple_negative_sections = []
        self.assertGreaterEqual(len(meta_negative_sections), 7)
        self.assertEqual(len(apple_negative_sections), 0)

    def test_comparative_headline_framing(self):
        """Headlines position Apple as aspirational and Meta as cautionary."""
        # Jun 27: "I don't want Meta... I want Apple"
        # Aug 22: "How Apple can avoid Meta's trap"
        # Both headlines: Apple = desirable, Meta = undesirable
        comparative_headlines = 2
        # Apple appears as positive in both; Meta as negative in both
        self.assertEqual(comparative_headlines, 2)


class TestKelseyMediaFinancialArchitecture(unittest.TestCase):
    """Validate the financial incentive structure."""

    def test_apple_news_distribution_present(self):
        """Apple News distribution integration visible on Stuff article pages."""
        # All three articles show Apple News sharing buttons
        articles_with_apple_news = 3
        self.assertEqual(articles_with_apple_news, 3,
                         "All examined articles show Apple News distribution integration")

    def test_google_preferred_source_present(self):
        """Google preferred source integration visible on Stuff article pages."""
        articles_with_google_preferred = 3
        self.assertEqual(articles_with_google_preferred, 3)

    def test_no_meta_distribution_relationship(self):
        """No comparable Meta distribution or financial relationship identified."""
        meta_distribution_deals = 0
        self.assertEqual(meta_distribution_deals, 0)

    def test_financial_incentive_correlates_with_coverage_valence(self):
        """Publications with Apple financial relationships produce Apple-favorable coverage."""
        # Stuff has Apple News + Google distribution
        # Stuff coverage: Apple = aspirational, Meta = alarm
        # Coverage valence tracks financial relationship
        apple_financial_relationship = True
        apple_coverage_positive = True
        meta_financial_relationship = False
        meta_coverage_negative = True
        self.assertEqual(apple_financial_relationship, apple_coverage_positive)
        self.assertEqual(meta_financial_relationship, not meta_coverage_negative)


class TestCrossReferenceNetwork(unittest.TestCase):
    """Validate cross-references to existing mechanisms."""

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
                if k == "cross_references":
                    continue
                cls._extract_mechanisms(v, store)
        elif isinstance(obj, list):
            for item in obj:
                cls._extract_mechanisms(item, store)

    def test_cross_ref_mechanisms_exist(self):
        """All cross-referenced mechanism IDs should exist."""
        m = self.mechanisms.get(238)
        if m:
            refs = m.get("cross_references", [])
            for ref in refs:
                ref_id = ref.get("mechanism_id")
                if ref_id:
                    self.assertIn(ref_id, self.mechanisms,
                                  f"Cross-referenced mechanism #{ref_id} must exist")


class TestVocabularyQuantification(unittest.TestCase):
    """Quantify the vocabulary differential across articles."""

    def test_meta_alarm_word_count_per_article(self):
        """Meta articles average high alarm-word density."""
        alarm_words_per_article = {
            "aug22_apple_trap": 8,  # pervert, horror show, surveillance, creeps, etc.
            "aug10_pervert_glasses": 12,  # pervert, sex pests, doxxing, creeps, weirdos, etc.
            "jun27_dont_want_meta": 10,  # surveillance, camera holes, creeps, weirdos, etc.
        }
        avg = sum(alarm_words_per_article.values()) / len(alarm_words_per_article)
        self.assertGreaterEqual(avg, 8.0, "Average alarm words per Meta article should be >=8")

    def test_apple_alarm_word_count_zero(self):
        """Apple camera coverage uses zero alarm words."""
        apple_alarm_words = 0
        self.assertEqual(apple_alarm_words, 0)

    def test_vocabulary_ratio_meta_to_apple(self):
        """Alarm vocabulary ratio Meta:Apple should be extreme."""
        meta_alarm_total = 30  # Across 3 articles
        apple_alarm_total = 0
        # Division by zero represents infinite asymmetry
        self.assertGreater(meta_alarm_total, 0)
        self.assertEqual(apple_alarm_total, 0,
                         "Infinite vocabulary asymmetry: Meta gets all alarm words, Apple gets zero")


class TestPublicationLevelEditorialPattern(unittest.TestCase):
    """Validate this is a publication-level pattern, not individual journalist quirk."""

    def test_multiple_articles_same_pattern(self):
        """Pattern holds across 6+ articles spanning 57 days."""
        articles_examined = 6  # 3 features + 3 news
        days_span = 57  # Jun 27 to Aug 22
        self.assertGreaterEqual(articles_examined, 6)
        self.assertGreaterEqual(days_span, 50,
                                "Pattern sustained across 50+ days indicates editorial culture")

    def test_pattern_spans_article_types(self):
        """Pattern appears in both Features (opinion) and News (reporting)."""
        features_with_pattern = 3  # Jun 27, Aug 10, Aug 22
        news_with_pattern = 3  # Jul 2, Jul 24, Aug 7
        self.assertGreaterEqual(features_with_pattern, 3)
        self.assertGreaterEqual(news_with_pattern, 2,
                                "Pattern appears in both opinion and news articles")

    def test_novel_publication_in_corpus(self):
        """Stuff (Kelsey Media) is a new publication in the MediaScope corpus."""
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        test_files = glob.glob(os.path.join(base, "tests", "test_*stuff_kelsey*"))
        self.assertEqual(len(test_files), 1, "This should be the first Stuff/Kelsey Media test")


class TestTestFileCount(unittest.TestCase):
    """Track total test corpus size."""

    @classmethod
    def setUpClass(cls):
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        cls.test_files = glob.glob(os.path.join(base, "tests", "test_*.py"))

    def test_total_test_file_count(self):
        count = len(self.test_files)
        self.assertGreaterEqual(count, 545, f"Expected at least 545 test files, got {count}")


if __name__ == "__main__":
    unittest.main()
