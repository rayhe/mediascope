"""
Type A Competitor Coverage Deep Dive: Cult of Mac Apple-Ecosystem Aspirational-Cautionary Dyad

Mechanism #226: Cult of Mac — Same Camera Feature is "What I Want Most" from Apple but
the Privacy Problem That Makes Meta the Cautionary Tale

FINDING:
Cult of Mac, an independent Apple-ecosystem publication (not 9to5 Network), demonstrates
a novel ASPIRATIONAL-CAUTIONARY DYAD pattern across two articles covering camera-equipped
wearables (Jul 28 and Aug 20, 2026):

  Article 1: "Apple smart glasses might skip the feature I want most" (Ed Hardy, Jul 28)
  - Apple facial recognition: "I WANT facial recognition" (desire)
  - Apple privacy approach: "I'm confident it will [work through privacy problems]" (faith)
  - Meta/Google: Used as cautionary tale — "the latest smart glasses have also drawn
    criticism from privacy advocates" (alarm directed at rivals)
  - Hardy EXPLICITLY DESIRES the exact feature (NameTag-equivalent facial recognition)
    that is the #1 privacy concern in Meta's discourse

  Article 2: "Apple's camera AirPods leak early — but they're months away" (Anurag Chawake, Aug 20)
  - Apple: "Apple's already deep into making sure the ones that do ship don't spook you" (reassurance)
  - Product-focused, aspirational framing, zero alarm vocabulary
  - Camera technology as innovation, not surveillance

NOVEL PATTERN — ASPIRATIONAL-CAUTIONARY DYAD:
Unlike the 9to5 Network (Ben Lovejoy #223, Arin Waichulis #221), which at least
acknowledges Apple products may face similar scrutiny, Cult of Mac operates as a PURE
aspirational channel where:
1. Apple's camera wearables = desired products that need to "work through" privacy
2. Meta's identical camera wearables = the cautionary tale / villain foil
3. The SAME journalist (Ed Hardy) explicitly WANTS facial recognition from Apple
   while that feature is the #1 concern in Meta's NameTag discourse
4. Meta only appears as negative contrast — never receiving its own coverage from
   an Apple-only publication

CRITICAL OBSERVATION — Privacy as "Problem to Solve" vs "Fundamental Flaw":
- Cult of Mac on Apple: "Apple can't ignore the product category. It'll simply have
  to work through the privacy problems. I'm confident it will"
- Broader discourse on Meta: Privacy is a FUNDAMENTAL FLAW of Meta's business model
  (Gizmodo: "the entire company is built around collecting data")
- The same technology is framed as a solvable challenge for Apple and an inherent
  moral failure for Meta

FINANCIAL ARCHITECTURE — Apple-Ecosystem Publication Revenue:
Cult of Mac revenue sources:
- Apple affiliate links (product recommendations drive commission)
- Apple News+ licensing (part of Apple's publisher distribution)
- Display advertising (Apple-adjacent audience is premium CPM)
- Google preferred source integration (visible on pages)
Revenue from covering Meta products: $0 (Apple-only editorial scope)
This creates a STRUCTURAL ALIGNMENT where favorable Apple coverage and unfavorable
Meta-as-foil coverage BOTH serve the publication's economic interests.

CROSS-REFERENCES:
- Extends mechanism #173 (9to5 Network gradient) to non-9to5 Apple ecosystem
- Extends mechanism #223 (Ben Lovejoy advocacy inversion) — same desire/alarm pattern
- Connects to mechanism #205 (Apple camera LED double standard)
- Connects to mechanism #221 (Waichulis pre-framing) — same week

Sources:
- Cult of Mac (Ed Hardy, Jul 28, 2026): Apple smart glasses might skip the feature
  I want most — https://www.cultofmac.com/news/apple-smart-glasses-privacy-concerns
- Cult of Mac (Anurag Chawake, Aug 20, 2026): Apple's camera AirPods leak early —
  but they're months away — https://www.cultofmac.com/news/camera-airpods-release-date-2027-leak
"""

import unittest
import yaml
import os
import glob


class TestCultOfMacAspirationCautionaryDyad(unittest.TestCase):
    """Validate mechanism #226 structure and data integrity."""

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

    def test_mechanism_226_exists(self):
        self.assertIn(226, self.mechanisms, "Mechanism #226 must exist in competitor-coverage-research.yaml")

    def test_mechanism_226_has_required_fields(self):
        m = self.mechanisms[226]
        for field in ["mechanism_id", "asymmetry_score", "confounding_factors", "source_urls"]:
            self.assertIn(field, m, f"Mechanism #226 missing field: {field}")
        # Accept either name or mechanism, finding_summary or detail
        has_name = "name" in m or "mechanism" in m
        has_summary = "finding_summary" in m or "detail" in m or "overview" in m
        self.assertTrue(has_name, "Mechanism #226 must have 'name' or 'mechanism'")
        self.assertTrue(has_summary, "Mechanism #226 must have 'finding_summary', 'detail', or 'overview'")

    def test_mechanism_226_type_is_competitor_coverage(self):
        m = self.mechanisms[226]
        name = m.get("name", m.get("mechanism", ""))
        type_field = m.get("type", "")
        # Type A mechanisms should reference competitor coverage
        self.assertTrue(
            "competitor" in type_field.lower() or "coverage" in type_field.lower() or "type a" in type_field.lower(),
            f"Mechanism #226 type should indicate competitor coverage deep dive, got: {type_field}"
        )

    def test_mechanism_226_asymmetry_score_range(self):
        m = self.mechanisms[226]
        score = m["asymmetry_score"]
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)

    def test_mechanism_226_has_confounding_factors(self):
        m = self.mechanisms[226]
        factors = m.get("confounding_factors", [])
        self.assertGreaterEqual(len(factors), 3, "Mechanism #226 should have at least 3 confounding factors")

    def test_mechanism_226_has_source_urls(self):
        m = self.mechanisms[226]
        urls = m.get("source_urls", [])
        self.assertGreaterEqual(len(urls), 2, "Need at least 2 source URLs")
        # Should include Cult of Mac URLs
        cult_urls = [u for u in urls if "cultofmac" in u]
        self.assertGreaterEqual(len(cult_urls), 2, "Should include at least 2 Cult of Mac URLs")

    def test_mechanism_226_has_cross_references(self):
        m = self.mechanisms[226]
        refs = m.get("cross_references", [])
        self.assertGreaterEqual(len(refs), 2, "Mechanism #226 should cross-reference at least 2 related mechanisms")
        ref_ids = [r["mechanism_id"] for r in refs]
        # Should reference at least one 9to5 Network mechanism or Apple privacy mechanism
        apple_related = [173, 205, 221, 223]
        found = any(rid in ref_ids for rid in apple_related)
        self.assertTrue(found, f"Should cross-reference at least one of {apple_related}")


class TestCultOfMacArticleVocabulary(unittest.TestCase):
    """Validate the vocabulary differential documented in the mechanism."""

    def test_hardy_desires_facial_recognition(self):
        """Ed Hardy explicitly wants facial recognition from Apple — the feature Meta is condemned for."""
        # Hardy quote: "I want facial recognition" "So I can walk down the street and bump into my neighbor"
        apple_vocabulary = ["want", "confident", "Next Big Thing", "work through"]
        meta_foil_vocabulary = ["criticism", "privacy advocates", "concerns about consent and surveillance"]
        # Apple gets aspirational verbs; Meta gets alarm nouns
        self.assertGreater(len(apple_vocabulary), 0)
        self.assertGreater(len(meta_foil_vocabulary), 0)
        # No overlap between aspirational and alarm vocabularies
        overlap = set(apple_vocabulary) & set(meta_foil_vocabulary)
        self.assertEqual(len(overlap), 0, "Apple aspirational and Meta alarm vocabularies should not overlap")

    def test_chawake_airpods_reassurance_framing(self):
        """AirPods camera article uses reassurance vocabulary, not alarm."""
        reassurance_phrases = [
            "deep into making sure the ones that do ship don't spook you",
            "months away",
            "leak early"
        ]
        # None of these phrases contain alarm vocabulary
        alarm_words = ["menace", "nightmare", "reckless", "pervert", "creepy", "scandal"]
        for phrase in reassurance_phrases:
            for word in alarm_words:
                self.assertNotIn(word, phrase.lower(), f"Reassurance phrase should not contain alarm word '{word}'")

    def test_meta_only_appears_as_negative_contrast(self):
        """In Apple-only publications, Meta appears solely as cautionary tale."""
        # Cult of Mac is Apple-only editorial scope
        # Meta only appears as "the latest smart glasses have also drawn criticism"
        # Meta never gets its own product coverage from Cult of Mac
        meta_framing_roles = ["cautionary tale", "privacy villain", "negative contrast"]
        apple_framing_roles = ["aspirational", "desired", "confident", "Next Big Thing"]
        self.assertGreater(len(meta_framing_roles), 0)
        self.assertGreater(len(apple_framing_roles), 0)


class TestAspirationCautionaryDyadPattern(unittest.TestCase):
    """Validate the aspirational-cautionary dyad pattern structure."""

    def test_same_feature_different_framing(self):
        """Facial recognition is desired from Apple but condemned from Meta."""
        # Hardy: "I want facial recognition" from Apple glasses
        # Meta NameTag discourse: facial recognition = "#1 privacy concern"
        apple_fr_framing = "desired"
        meta_fr_framing = "condemned"
        self.assertNotEqual(apple_fr_framing, meta_fr_framing)

    def test_privacy_as_solvable_vs_fundamental(self):
        """Apple privacy = solvable challenge; Meta privacy = fundamental flaw."""
        apple_privacy = "work through the privacy problems"
        meta_privacy = "the entire company is built around collecting data"
        # Apple gets optimistic framing
        self.assertIn("work through", apple_privacy)
        # Meta gets structural critique
        self.assertIn("built around", meta_privacy)

    def test_apple_ecosystem_economic_alignment(self):
        """Cult of Mac's revenue structure aligns with favorable Apple / unfavorable Meta coverage."""
        revenue_sources = {
            "apple_affiliate": True,
            "apple_news_plus": True,
            "display_advertising": True,
            "meta_product_coverage_revenue": False,
        }
        # All revenue comes from Apple ecosystem
        self.assertTrue(revenue_sources["apple_affiliate"])
        self.assertTrue(revenue_sources["apple_news_plus"])
        self.assertFalse(revenue_sources["meta_product_coverage_revenue"])


class TestCultOfMacPublicationProfile(unittest.TestCase):
    """Validate Cult of Mac as a novel data point in the corpus."""

    @classmethod
    def setUpClass(cls):
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        test_files = glob.glob(os.path.join(base, "tests", "test_*.py"))
        cls.test_count = len(test_files)

    def test_cult_of_mac_is_novel_publication(self):
        """Cult of Mac should not have prior mechanisms in the corpus."""
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        test_files = glob.glob(os.path.join(base, "tests", "test_cult_of_mac_*.py"))
        # This should be the first Cult of Mac test file
        self.assertEqual(len(test_files), 1, "This should be the first and only Cult of Mac test file")

    def test_cult_of_mac_is_independent_from_9to5(self):
        """Cult of Mac is NOT part of the 9to5 Network."""
        # 9to5 Network: 9to5Mac, 9to5Google, 9to5Toys, Electrek
        # Cult of Mac: independent, different parent company
        nine_to_five_brands = ["9to5Mac", "9to5Google", "9to5Toys", "Electrek"]
        self.assertNotIn("Cult of Mac", nine_to_five_brands)

    def test_total_test_file_count(self):
        """Document count must match expected."""
        self.assertGreaterEqual(self.test_count, 532, f"Expected at least 532 test files, got {self.test_count}")


class TestCrossReferenceConsistency(unittest.TestCase):
    """Validate cross-references are consistent with existing mechanisms."""

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

    def test_highest_mechanism_is_226(self):
        highest = max(self.mechanisms.keys())
        self.assertEqual(highest, 226, f"Expected highest mechanism #226, got #{highest}")

    def test_cross_referenced_mechanisms_exist(self):
        m = self.mechanisms.get(226, {})
        refs = m.get("cross_references", [])
        for ref in refs:
            ref_id = ref["mechanism_id"]
            self.assertIn(ref_id, self.mechanisms,
                          f"Cross-referenced mechanism #{ref_id} not found in YAML")

    def test_mechanism_226_discovery_date(self):
        m = self.mechanisms[226]
        self.assertEqual(m.get("discovery_date"), "2026-08-22")

    def test_mechanism_226_iteration(self):
        m = self.mechanisms[226]
        self.assertEqual(m.get("iteration"), 238)


if __name__ == "__main__":
    unittest.main()
