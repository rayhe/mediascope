"""
Test: Sara Fischer / Axios — Cross-Entity Settlement-Week vs OpenAI Ad Revenue
Publication-Level Funding Deal Coverage Vocabulary Bifurcation

Mechanism #349: Sara Fischer Axios Publication-Level OpenAI Funding Deal
Cross-Entity Coverage Vocabulary Bifurcation

CORE FINDING:
Sara Fischer, Axios' senior media reporter, covers both Meta and OpenAI's
publisher/advertising businesses. Within settlement week (Aug 26-27, 2026),
Fischer contributed to Meta settlement coverage framed as "Big Resistance"
regulatory crackdown, while her prior OpenAI ad revenue reporting used
aspirational business-growth vocabulary. Meanwhile, Axios itself has a direct
multi-year OpenAI content licensing and newsroom funding deal that is not
disclosed in Fischer's OpenAI coverage.

KEY EVIDENCE:
1. Meta settlement (Aug 27, 2026): Fischer created data table for "Big Tech
   faces Big Resistance" article positioning Meta's $17.1B settlement alongside
   European antitrust fines. Regulatory-punitive framing.
2. OpenAI $2.5B ad revenue (Apr 9, 2026): Fischer broke story that OpenAI
   projects $2.5B ad revenue in 2026, $100B by 2030. Zero child safety
   vocabulary despite OpenAI serving ads to 1B weekly users including minors.
3. OpenAI Ads Manager (May 5, 2026): Fischer reported OpenAI self-service
   ad tool launch as business milestone. Zero FTC investigation cross-reference.
4. OpenAI-Atlantic/Vox Media deals (May 2024): Fischer reported deals as
   "added momentum in quest for credible content." Aspirational framing.
5. Meta-Reuters AI deal: Fischer reported with neutral "Between the lines"
   noting unclear training component — more skeptical framing than OpenAI deals.

FINANCIAL ARCHITECTURE:
- Axios has multi-year OpenAI content licensing deal (announced Jan 2025)
- OpenAI funds Axios Local newsrooms (4 cities initially, 7-9 more in 2026)
- Axios uses OpenAI technology for "localizer" tools and AI-enabled reporter platform
- This relationship is not disclosed in Fischer's OpenAI coverage articles

VOCABULARY REGISTER INVERSION:
- Meta ad business: "money machine" (Reuters analysis Fischer contributed to),
  "Big Resistance," "regulatory reckoning," "penalties," "settlements"
- OpenAI ad business: "revenue growth," "material expansion," "ad revenue"
  (neutral-to-positive), "quest for credible content" (aspirational)

STRONG CONFOUNDERS:
- Genre convention: settlement coverage inherently uses regulatory vocabulary (-0.08)
- Meta's proven harm record: decade of documented child safety failures (-0.10)
- Different story types: legal settlement vs business earnings reporting (-0.05)
- Fischer covers media business broadly, not tech accountability specifically (-0.03)
- Axios house style ("Why it matters" / "Between the lines") is consistent (-0.02)

Asymmetry score: Raw 0.48 → Adjusted 0.20 (low-moderate after heavy confounder load)

Sources:
- https://canisgallicus.com/2026/08/27/axios-big-tech-faces-big-resistance/
  (Axios settlement coverage with Fischer data table, Aug 27, 2026)
- https://www.reuters.com/business/media-telecom/openai-projects-25-billion-ad-revenue-this-year-100-billion-by-2030-axios-2026-04-09/
  (Reuters citing Fischer's OpenAI $2.5B ad revenue scoop, Apr 9, 2026)
- https://intellectia.ai/news/stock/openai-rolls-out-a-beta-version-of-its-new-ads-manager-tool-to-advertisers-in-the-us-making-it-easier-for-smbs-to-buy-chatgpt-ads-on-a-costperclick-basis-sara-fischeraxios
  (Fischer OpenAI Ads Manager reporting, May 5, 2026)
- https://www.adweek.com/media/axios-local-openai-2026/
  (Adweek on Axios-OpenAI Local newsroom funding deal, May 2026)
- https://wwsg.com/speaker-news/sara-fischer-exclusive-product-deals-with-openai/
  (Fischer reporting on OpenAI-Atlantic/Vox Media deals, May 2024)
"""

import unittest
import yaml
import os


class TestSaraFischerAxiosCrossEntityMechanismStructure(unittest.TestCase):
    """Verify mechanism #349 exists and is structurally sound."""

    @classmethod
    def setUpClass(cls):
        yaml_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "profiles",
            "competitor-coverage-research.yaml",
        )
        with open(yaml_path) as f:
            cls.data = yaml.safe_load(f)

    def test_mechanism_349_exists(self):
        """Mechanism #349 must exist in competitor-coverage-research.yaml."""
        found = False
        for section in self.data.values():
            if isinstance(section, dict):
                for key, val in section.items():
                    if isinstance(val, dict) and val.get("mechanism_id") == 349:
                        found = True
                        break
            if found:
                break
        self.assertTrue(found, "Mechanism #349 not found in YAML")

    def test_mechanism_349_has_required_fields(self):
        """Mechanism #349 must have title, type, and test_file."""
        mechanism = None
        for section in self.data.values():
            if isinstance(section, dict):
                for key, val in section.items():
                    if isinstance(val, dict) and val.get("mechanism_id") == 349:
                        mechanism = val
                        break
            if mechanism:
                break
        self.assertIsNotNone(mechanism, "Mechanism #349 not found")
        self.assertIn("title", mechanism)
        self.assertIn("type", mechanism)
        self.assertIn("test_file", mechanism)

    def test_mechanism_349_type_is_journalist_cross_entity(self):
        """Mechanism #349 should be journalist cross-entity type."""
        mechanism = None
        for section in self.data.values():
            if isinstance(section, dict):
                for key, val in section.items():
                    if isinstance(val, dict) and val.get("mechanism_id") == 349:
                        mechanism = val
                        break
            if mechanism:
                break
        self.assertIsNotNone(mechanism, "Mechanism #349 not found")
        mtype = mechanism.get("type", "").lower()
        self.assertTrue(
            "journalist" in mtype or "cross_entity" in mtype or "cross-entity" in mtype,
            f"Expected journalist/cross-entity type, got: {mtype}",
        )


class TestSaraFischerAxiosPublicationFundingDeal(unittest.TestCase):
    """Test the Axios-OpenAI financial relationship documentation."""

    @classmethod
    def setUpClass(cls):
        yaml_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "profiles",
            "competitor-coverage-research.yaml",
        )
        with open(yaml_path) as f:
            cls.data = yaml.safe_load(f)
        # Find mechanism 349
        cls.mechanism = None
        for section in cls.data.values():
            if isinstance(section, dict):
                for key, val in section.items():
                    if isinstance(val, dict) and val.get("mechanism_id") == 349:
                        cls.mechanism = val
                        break
            if cls.mechanism:
                break

    def test_mechanism_documents_axios_openai_deal(self):
        """Mechanism must document the Axios-OpenAI financial relationship."""
        self.assertIsNotNone(self.mechanism, "Mechanism #349 not found")
        text = yaml.dump(self.mechanism).lower()
        self.assertTrue(
            "axios" in text and "openai" in text,
            "Mechanism must reference both Axios and OpenAI",
        )

    def test_mechanism_documents_newsroom_funding(self):
        """Mechanism must document OpenAI funding Axios Local newsrooms."""
        self.assertIsNotNone(self.mechanism, "Mechanism #349 not found")
        text = yaml.dump(self.mechanism).lower()
        self.assertTrue(
            "local" in text or "newsroom" in text or "fund" in text,
            "Mechanism must document newsroom funding relationship",
        )

    def test_mechanism_documents_content_licensing(self):
        """Mechanism must document the Axios-OpenAI content licensing deal."""
        self.assertIsNotNone(self.mechanism, "Mechanism #349 not found")
        text = yaml.dump(self.mechanism).lower()
        self.assertTrue(
            "licens" in text or "content deal" in text or "multi-year" in text,
            "Mechanism must document content licensing relationship",
        )

    def test_mechanism_documents_non_disclosure(self):
        """Mechanism must note that the financial relationship is not disclosed in coverage."""
        self.assertIsNotNone(self.mechanism, "Mechanism #349 not found")
        text = yaml.dump(self.mechanism).lower()
        self.assertTrue(
            "disclos" in text or "undisclosed" in text or "not disclosed" in text,
            "Mechanism must document non-disclosure of financial relationship",
        )


class TestSaraFischerVocabularyBifurcation(unittest.TestCase):
    """Test that the vocabulary register inversion is documented with specific examples."""

    @classmethod
    def setUpClass(cls):
        yaml_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "profiles",
            "competitor-coverage-research.yaml",
        )
        with open(yaml_path) as f:
            cls.data = yaml.safe_load(f)
        cls.mechanism = None
        for section in cls.data.values():
            if isinstance(section, dict):
                for key, val in section.items():
                    if isinstance(val, dict) and val.get("mechanism_id") == 349:
                        cls.mechanism = val
                        break
            if cls.mechanism:
                break

    def test_meta_vocabulary_documented(self):
        """Must document adversarial vocabulary used for Meta coverage."""
        self.assertIsNotNone(self.mechanism, "Mechanism #349 not found")
        text = yaml.dump(self.mechanism).lower()
        meta_adversarial = any(
            term in text
            for term in [
                "resistance",
                "reckoning",
                "penalt",
                "settlement",
                "fine",
            ]
        )
        self.assertTrue(
            meta_adversarial,
            "Must document adversarial vocabulary used for Meta",
        )

    def test_openai_vocabulary_documented(self):
        """Must document aspirational vocabulary used for OpenAI coverage."""
        self.assertIsNotNone(self.mechanism, "Mechanism #349 not found")
        text = yaml.dump(self.mechanism).lower()
        openai_aspirational = any(
            term in text
            for term in [
                "revenue growth",
                "momentum",
                "expansion",
                "aspirational",
                "business",
            ]
        )
        self.assertTrue(
            openai_aspirational,
            "Must document aspirational vocabulary used for OpenAI",
        )

    def test_child_safety_gap_documented(self):
        """Must document zero child safety vocabulary in OpenAI ad coverage."""
        self.assertIsNotNone(self.mechanism, "Mechanism #349 not found")
        text = yaml.dump(self.mechanism).lower()
        self.assertTrue(
            "child safety" in text or "child" in text or "minor" in text,
            "Must document child safety coverage gap in OpenAI reporting",
        )

    def test_ftc_investigation_gap_documented(self):
        """Must document absence of FTC AI chatbot investigation in OpenAI coverage."""
        self.assertIsNotNone(self.mechanism, "Mechanism #349 not found")
        text = yaml.dump(self.mechanism).lower()
        self.assertTrue(
            "ftc" in text or "federal trade" in text,
            "Must document FTC investigation gap in OpenAI coverage",
        )


class TestSaraFischerConfounderQuality(unittest.TestCase):
    """Test that confounders are documented and STRONG ones have counters."""

    @classmethod
    def setUpClass(cls):
        yaml_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "profiles",
            "competitor-coverage-research.yaml",
        )
        with open(yaml_path) as f:
            cls.data = yaml.safe_load(f)
        cls.mechanism = None
        for section in cls.data.values():
            if isinstance(section, dict):
                for key, val in section.items():
                    if isinstance(val, dict) and val.get("mechanism_id") == 349:
                        cls.mechanism = val
                        break
            if cls.mechanism:
                break

    def test_confounders_present(self):
        """Mechanism must have confounding_factors."""
        self.assertIsNotNone(self.mechanism, "Mechanism #349 not found")
        self.assertIn(
            "confounding_factors",
            self.mechanism,
            "Mechanism must include confounding_factors",
        )

    def test_at_least_three_confounders(self):
        """Must have at least 3 confounders for a low-moderate score."""
        self.assertIsNotNone(self.mechanism, "Mechanism #349 not found")
        confounders = self.mechanism.get("confounding_factors", [])
        self.assertGreaterEqual(
            len(confounders),
            3,
            f"Expected at least 3 confounders, got {len(confounders)}",
        )

    def test_strong_confounders_exist(self):
        """At least one confounder must be STRONG."""
        self.assertIsNotNone(self.mechanism, "Mechanism #349 not found")
        confounders = self.mechanism.get("confounding_factors", [])
        strong = [c for c in confounders if c.get("strength") == "STRONG"]
        self.assertGreater(
            len(strong),
            0,
            "Must have at least one STRONG confounder",
        )

    def test_genre_convention_confounder(self):
        """Must document genre convention difference (settlement vs business reporting)."""
        self.assertIsNotNone(self.mechanism, "Mechanism #349 not found")
        confounders = self.mechanism.get("confounding_factors", [])
        text = yaml.dump(confounders).lower()
        self.assertTrue(
            "genre" in text or "story type" in text or "settlement" in text,
            "Must document genre convention confounder",
        )

    def test_harm_record_confounder(self):
        """Must document Meta's proven harm record as confounder."""
        self.assertIsNotNone(self.mechanism, "Mechanism #349 not found")
        confounders = self.mechanism.get("confounding_factors", [])
        text = yaml.dump(confounders).lower()
        self.assertTrue(
            "harm record" in text or "proven" in text or "decade" in text,
            "Must document Meta's proven harm record as confounder",
        )


class TestSaraFischerSpecificArticleEvidence(unittest.TestCase):
    """Test that specific article URLs and dates are documented."""

    @classmethod
    def setUpClass(cls):
        yaml_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "profiles",
            "competitor-coverage-research.yaml",
        )
        with open(yaml_path) as f:
            cls.data = yaml.safe_load(f)
        cls.mechanism = None
        for section in cls.data.values():
            if isinstance(section, dict):
                for key, val in section.items():
                    if isinstance(val, dict) and val.get("mechanism_id") == 349:
                        cls.mechanism = val
                        break
            if cls.mechanism:
                break

    def test_settlement_coverage_evidence(self):
        """Must include evidence of Meta settlement coverage."""
        self.assertIsNotNone(self.mechanism, "Mechanism #349 not found")
        text = yaml.dump(self.mechanism).lower()
        self.assertTrue(
            "big tech" in text or "big resistance" in text or "settlement" in text,
            "Must document Meta settlement coverage",
        )

    def test_openai_ad_revenue_evidence(self):
        """Must include evidence of OpenAI $2.5B ad revenue reporting."""
        self.assertIsNotNone(self.mechanism, "Mechanism #349 not found")
        text = yaml.dump(self.mechanism).lower()
        self.assertTrue(
            "2.5 billion" in text or "2.5b" in text or "$2.5" in text or "ad revenue" in text,
            "Must document OpenAI ad revenue reporting",
        )

    def test_temporal_proximity(self):
        """Must document temporal proximity of coverage within settlement week."""
        self.assertIsNotNone(self.mechanism, "Mechanism #349 not found")
        text = yaml.dump(self.mechanism).lower()
        self.assertTrue(
            "august" in text or "aug" in text or "settlement week" in text,
            "Must document temporal context",
        )

    def test_cross_references_exist(self):
        """Must cross-reference related mechanisms."""
        self.assertIsNotNone(self.mechanism, "Mechanism #349 not found")
        self.assertIn(
            "cross_references",
            self.mechanism,
            "Mechanism must include cross-references to related mechanisms",
        )


class TestSaraFischerAsymmetryScore(unittest.TestCase):
    """Test that asymmetry score is calibrated with confounder adjustments."""

    @classmethod
    def setUpClass(cls):
        yaml_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "profiles",
            "competitor-coverage-research.yaml",
        )
        with open(yaml_path) as f:
            cls.data = yaml.safe_load(f)
        cls.mechanism = None
        for section in cls.data.values():
            if isinstance(section, dict):
                for key, val in section.items():
                    if isinstance(val, dict) and val.get("mechanism_id") == 349:
                        cls.mechanism = val
                        break
            if cls.mechanism:
                break

    def test_asymmetry_score_present(self):
        """Must have an asymmetry_score field."""
        self.assertIsNotNone(self.mechanism, "Mechanism #349 not found")
        self.assertIn(
            "asymmetry_score",
            self.mechanism,
            "Mechanism must include asymmetry_score",
        )

    def test_asymmetry_score_range(self):
        """Score must be between 0.0 and 1.0."""
        self.assertIsNotNone(self.mechanism, "Mechanism #349 not found")
        score = self.mechanism.get("asymmetry_score", -1)
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)

    def test_asymmetry_score_reflects_heavy_confounders(self):
        """Adjusted score should be low-moderate given heavy confounder load."""
        self.assertIsNotNone(self.mechanism, "Mechanism #349 not found")
        score = self.mechanism.get("asymmetry_score", -1)
        # With genre convention, proven harm record, different story types:
        # raw ~0.48, adjusted should be under 0.30
        self.assertLessEqual(
            score,
            0.35,
            f"Score {score} too high given heavy confounder load",
        )


if __name__ == "__main__":
    unittest.main()
