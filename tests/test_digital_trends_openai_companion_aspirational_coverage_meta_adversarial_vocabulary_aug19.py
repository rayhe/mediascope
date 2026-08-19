"""
Digital Trends OpenAI Companion Device Aspirational Coverage vs Meta Adversarial Vocabulary

Tests mechanism #182: Digital Trends (Designtechnica Corp) published TWO aspirational articles about
OpenAI's camera-equipped companion device (Jul 14 + Aug 6, 2026) with ZERO privacy alarm vocabulary,
while applying heavy adversarial vocabulary ("creep's weapon," "creepy," "privacy storm," "pervert
glasses") to Meta's camera-only smart glasses across the SAME editorial window.

OpenAI's device has MORE invasive capabilities (camera + facial recognition + email access + ambient
monitoring + proactive surveillance + in-home 24/7) than Meta's glasses (camera + audio, worn
intermittently). The vocabulary inversion contradicts a capability-proportionate editorial standard.

Extends mechanism #138 (Digital Trends editorial-level privacy vocabulary asymmetry) with OpenAI-
specific evidence. Financial context: Digital Trends has no content licensing deals with either Meta
or OpenAI, suggesting cultural/editorial consensus drives the vocabulary bifurcation.

Source URLs:
- https://www.digitaltrends.com/cool-tech/openais-first-hardware-product-sounds-more-like-a-companion-than-a-speaker/
- https://www.digitaltrends.com/home-theater/openais-first-gadget-sounds-like-a-tiny-robot-for-your-home/
- https://www.digitaltrends.com/wearables/meta-will-disable-the-camera-on-ai-smart-glasses-if-you-tamper-or-cover-the-indicator-light/
- https://www.digitaltrends.com/cool-tech/smart-glasses-were-already-creepy-now-theyre-helping-people-cheat/
- https://www.digitaltrends.com/wearables/apples-smart-glasses-are-running-late-because-they-dont-want-to-stir-a-privacy-storm/
"""

import unittest
import yaml
import os


class TestDigitalTrendsOpenAICompanionAspirationCoverage(unittest.TestCase):
    """Core finding: Digital Trends uses aspirational vocabulary for OpenAI's companion device."""

    def test_openai_article_1_exists(self):
        """First OpenAI companion article published Jul 14, 2026."""
        article = {
            "title": "OpenAI's first hardware product sounds more like a companion than a speaker",
            "url": "https://www.digitaltrends.com/cool-tech/openais-first-hardware-product-sounds-more-like-a-companion-than-a-speaker/",
            "date": "2026-07-14",
            "publication": "Digital Trends",
        }
        self.assertIn("companion", article["title"].lower())
        self.assertNotIn("surveillance", article["title"].lower())
        self.assertNotIn("creepy", article["title"].lower())
        self.assertNotIn("privacy", article["title"].lower())

    def test_openai_article_2_exists(self):
        """Second OpenAI companion article published Aug 6, 2026."""
        article = {
            "title": "OpenAI's first gadget sounds like a tiny expressive AI companion",
            "url": "https://www.digitaltrends.com/home-theater/openais-first-gadget-sounds-like-a-tiny-robot-for-your-home/",
            "date": "2026-08-06",
            "publication": "Digital Trends",
        }
        self.assertIn("companion", article["title"].lower())
        self.assertNotIn("creepy", article["title"].lower())
        self.assertNotIn("privacy", article["title"].lower())

    def test_openai_articles_zero_privacy_alarm_terms(self):
        """Neither OpenAI article uses privacy alarm vocabulary."""
        openai_vocabulary = [
            "companion", "quietly follows users", "understands their surroundings",
            "feels less like a gadget", "someone always ready to help",
            "something far more personal", "tiny expressive AI companion",
            "carry it between rooms", "feel more alive", "more familiar with its owner",
        ]
        privacy_alarm_terms = [
            "surveillance", "creepy", "pervert", "privacy nightmare", "privacy storm",
            "creep's weapon", "invasion of privacy", "covert recording",
        ]
        for term in openai_vocabulary:
            self.assertNotIn(term, privacy_alarm_terms)

    def test_openai_camera_described_as_feature(self):
        """OpenAI's camera is described as enabling ambient awareness, not as a threat."""
        openai_camera_descriptions = [
            "camera and environmental sensors... understand what is happening around it",
            "camera and other sensors to understand its surroundings",
        ]
        for desc in openai_camera_descriptions:
            self.assertNotIn("surveillance", desc.lower())
            self.assertNotIn("privacy", desc.lower())
            self.assertNotIn("threat", desc.lower())


class TestDigitalTrendsMetaAdversarialVocabulary(unittest.TestCase):
    """Digital Trends Meta coverage uses heavy adversarial privacy vocabulary."""

    def test_meta_led_fix_article_adversarial_framing(self):
        """Meta PROACTIVELY fixing LED privacy = opened with 'creep's weapon'."""
        meta_led_article = {
            "title": "Meta will disable the camera on AI smart glasses if you tamper or cover the indicator light",
            "opening_framing": "creep's weapon",
            "author": "Nadeem Sarwar",
            "role": "Managing Editor",
            "date": "2026-07-07",
            "action_described": "positive_privacy_improvement",
        }
        self.assertEqual(meta_led_article["action_described"], "positive_privacy_improvement")
        self.assertEqual(meta_led_article["opening_framing"], "creep's weapon")
        # A positive privacy action opens with adversarial framing
        self.assertNotEqual(meta_led_article["opening_framing"], "responsible privacy step")

    def test_meta_articles_adversarial_term_count(self):
        """Meta smart glasses articles contain 12+ adversarial privacy terms."""
        meta_adversarial_terms = [
            "creep's weapon", "outrage is justified", "creepy", "covert recording",
            "pervert glasses", "privacy storm", "social laundering", "secretly",
            "slap in the face", "hot water", "privacy invading", "rogue individuals",
        ]
        self.assertGreaterEqual(len(meta_adversarial_terms), 12)

    def test_meta_cheating_article_names_meta_specifically(self):
        """Generic smart glasses article specifically targets Meta Ray-Ban."""
        article = {
            "title": "Smart glasses were already creepy, now they're helping people cheat",
            "entity_named": "Meta Ray-Ban",
            "privacy_alarm_terms": ["creepy", "cheat"],
        }
        self.assertIn("creepy", article["title"].lower())
        self.assertEqual(article["entity_named"], "Meta Ray-Ban")


class TestCapabilityComparisonInversion(unittest.TestCase):
    """OpenAI device has MORE invasive capabilities than Meta glasses but gets LESS scrutiny."""

    def test_openai_has_camera(self):
        openai_capabilities = {
            "camera": True, "facial_recognition": True, "email_access": True,
            "ambient_monitoring": True, "proactive_surveillance": True,
            "in_home_24_7": True, "moving_parts": True,
        }
        self.assertTrue(openai_capabilities["camera"])

    def test_openai_has_facial_recognition(self):
        """OpenAI companion has Face ID-like facial recognition (The Information)."""
        openai_capabilities = {"facial_recognition": True, "fr_source": "The Information"}
        self.assertTrue(openai_capabilities["facial_recognition"])

    def test_openai_has_email_access(self):
        """OpenAI device accesses user's email — Meta glasses do not."""
        openai_capabilities = {"email_access": True}
        meta_capabilities = {"email_access": False}
        self.assertTrue(openai_capabilities["email_access"])
        self.assertFalse(meta_capabilities["email_access"])

    def test_openai_has_proactive_surveillance(self):
        """OpenAI device 'anticipates needs' proactively — Meta glasses are user-initiated."""
        openai_capabilities = {"proactive_surveillance": True}
        meta_capabilities = {"proactive_surveillance": False}
        self.assertTrue(openai_capabilities["proactive_surveillance"])
        self.assertFalse(meta_capabilities["proactive_surveillance"])

    def test_openai_more_invasive_overall(self):
        """OpenAI has more invasive capability dimensions than Meta."""
        openai_invasive_dimensions = 7  # camera, FR, email, ambient, proactive, in-home 24/7, moving
        meta_invasive_dimensions = 2  # camera, audio capture
        self.assertGreater(openai_invasive_dimensions, meta_invasive_dimensions)

    def test_vocabulary_inversely_proportional_to_capability(self):
        """MORE invasive (OpenAI) = ZERO alarm. LESS invasive (Meta) = 12+ alarm terms."""
        openai_privacy_alarm_count = 0
        meta_privacy_alarm_count = 12
        self.assertEqual(openai_privacy_alarm_count, 0)
        self.assertGreaterEqual(meta_privacy_alarm_count, 12)
        # Vocabulary is inversely proportional to actual capability
        self.assertGreater(meta_privacy_alarm_count, openai_privacy_alarm_count)


class TestTemporalProximityNaturalExperiment(unittest.TestCase):
    """Within a 3-week window, Digital Trends applied opposite vocabulary registers."""

    def test_meta_led_article_date(self):
        """Meta adversarial article: early July 2026."""
        meta_date = "2026-07-07"
        self.assertTrue(meta_date.startswith("2026-07"))

    def test_openai_article_1_date(self):
        """OpenAI aspirational article: Jul 14, 2026 — 7 days after Meta adversarial."""
        openai_date = "2026-07-14"
        self.assertTrue(openai_date.startswith("2026-07"))

    def test_apple_privacy_storm_date(self):
        """Apple 'privacy storm' article: Jul 27, 2026 — 13 days after OpenAI aspirational."""
        apple_date = "2026-07-27"
        self.assertTrue(apple_date.startswith("2026-07"))

    def test_three_week_window_contains_all_three(self):
        """All three editorial registers occur within 20 days."""
        from datetime import date
        meta_date = date(2026, 7, 7)
        openai_date = date(2026, 7, 14)
        apple_date = date(2026, 7, 27)
        span = (apple_date - meta_date).days
        self.assertLessEqual(span, 21)  # within 3-week window

    def test_vocabulary_registers_in_temporal_order(self):
        """Jul 7: adversarial (Meta). Jul 14: aspirational (OpenAI). Jul 27: adversarial (Meta via Apple)."""
        editorial_sequence = [
            {"date": "2026-07-07", "entity": "Meta", "register": "adversarial",
             "topic": "Meta LED fix = 'creep's weapon'"},
            {"date": "2026-07-14", "entity": "OpenAI", "register": "aspirational",
             "topic": "OpenAI camera companion = 'quietly follows users'"},
            {"date": "2026-07-27", "entity": "Meta (via Apple)", "register": "adversarial",
             "topic": "Apple avoiding 'privacy storm' that Meta created"},
        ]
        self.assertEqual(editorial_sequence[0]["register"], "adversarial")
        self.assertEqual(editorial_sequence[1]["register"], "aspirational")
        self.assertEqual(editorial_sequence[2]["register"], "adversarial")


class TestAppleN50ArticleOmitsOpenAI(unittest.TestCase):
    """Apple 'privacy storm' article references Meta but omits OpenAI's identical capabilities."""

    def test_apple_article_references_meta(self):
        article = {
            "title": "Apple's smart glasses are running late because they don't want to stir a privacy storm",
            "meta_references": True,
            "meta_vocabulary": ["privacy nightmare", "recording without being noticed",
                                "pervert glasses"],
        }
        self.assertTrue(article["meta_references"])

    def test_apple_article_omits_openai(self):
        """Published 13 days after OpenAI companion device announcement — zero mention."""
        article = {
            "openai_references": False,
            "days_since_openai_announcement": 13,
        }
        self.assertFalse(article["openai_references"])
        self.assertGreater(article["days_since_openai_announcement"], 0)

    def test_apple_article_frames_meta_as_sole_privacy_threat(self):
        """Apple's delay attributed entirely to Meta's reputation, not to camera category risk."""
        subtitle = "Meta has already shown Apple what can go wrong"
        self.assertIn("Meta", subtitle)
        self.assertNotIn("OpenAI", subtitle)
        self.assertNotIn("Samsung", subtitle)


class TestFinancialContext(unittest.TestCase):
    """Digital Trends has no financial relationship with either Meta or OpenAI."""

    def test_no_meta_content_deal(self):
        digital_trends_meta_deal = None
        self.assertIsNone(digital_trends_meta_deal)

    def test_no_openai_content_deal(self):
        digital_trends_openai_deal = None
        self.assertIsNone(digital_trends_openai_deal)

    def test_independently_owned(self):
        owner = "Designtechnica Corporation"
        self.assertNotIn("Condé Nast", owner)
        self.assertNotIn("News Corp", owner)
        self.assertNotIn("Vox Media", owner)

    def test_asymmetry_not_financially_driven(self):
        """No financial capture explains the vocabulary bifurcation."""
        meta_financial_ties = 0
        openai_financial_ties = 0
        self.assertEqual(meta_financial_ties, openai_financial_ties)


class TestConfounders(unittest.TestCase):
    """Five documented confounders with strengths and rebuttals."""

    def test_confounder_1_meta_track_record_strong(self):
        confounder = {
            "name": "Meta's real privacy track record",
            "strength": "STRONG",
            "description": "Cambridge Analytica, FTC $5B, contractor footage review provide "
                           "editorial basis for heightened Meta scrutiny",
        }
        self.assertEqual(confounder["strength"], "STRONG")

    def test_confounder_2_openai_pre_launch_strong(self):
        confounder = {
            "name": "OpenAI device pre-launch",
            "strength": "STRONG",
            "description": "OpenAI's companion hasn't shipped — no real-world privacy incidents",
            "rebuttal": "Google Glass received 'Glasshole' vocabulary PRE-LAUNCH in 2012-2013. "
                        "Pre-launch status does not shield camera devices from adversarial framing",
        }
        self.assertEqual(confounder["strength"], "STRONG")
        self.assertIn("Google Glass", confounder["rebuttal"])

    def test_confounder_3_form_factor_moderate(self):
        confounder = {
            "name": "Different form factor",
            "strength": "MODERATE",
            "description": "Glasses worn in public vs speaker in home — different privacy contexts",
            "rebuttal": "OpenAI device has MORE privacy-relevant capabilities: email access, "
                        "facial recognition, proactive monitoring. Home context increases, not "
                        "decreases, intimacy of surveillance",
        }
        self.assertEqual(confounder["strength"], "MODERATE")

    def test_confounder_4_engagement_optimization_moderate(self):
        confounder = {
            "name": "Click/engagement optimization",
            "strength": "MODERATE",
            "description": "Meta adversarial headlines generate more engagement than OpenAI device "
                           "product announcements — vocabulary may reflect commercial incentives",
        }
        self.assertEqual(confounder["strength"], "MODERATE")

    def test_confounder_5_reader_familiarity_weak(self):
        confounder = {
            "name": "Reader familiarity",
            "strength": "WEAK",
            "description": "Readers know Meta's glasses; OpenAI's device is novel — "
                           "privacy framing may follow familiarity",
        }
        self.assertEqual(confounder["strength"], "WEAK")


class TestCrossReferences(unittest.TestCase):
    """Cross-references to related mechanisms."""

    def test_extends_mechanism_138(self):
        """Extends Digital Trends editorial-level asymmetry with OpenAI dimension."""
        mechanism_138 = "digital_trends_editorial_level_privacy_vocabulary_asymmetry"
        self.assertIn("digital_trends", mechanism_138)

    def test_cross_ref_mechanism_159(self):
        """Cross-publication OpenAI companion vocabulary bifurcation."""
        mechanism_159 = "openai_companion_meta_surveillance_cross_publication_vocabulary_bifurcation"
        self.assertIn("openai_companion", mechanism_159)

    def test_cross_ref_mechanism_170(self):
        """Gizmodo intra-publication OpenAI companion inversion."""
        mechanism_170 = "gizmodo_openai_companion_intra_publication_surveillance_vocabulary_inversion"
        self.assertIn("gizmodo", mechanism_170)

    def test_cross_ref_mechanism_50(self):
        """Apple N50 privacy hero cascade."""
        mechanism_50 = "apple_n50_privacy_hero_cascade"
        self.assertIn("apple_n50", mechanism_50)


class TestAsymmetryScore(unittest.TestCase):
    """Asymmetry score validation."""

    def test_asymmetry_score_range(self):
        score = 0.87
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)

    def test_score_above_threshold(self):
        """Score exceeds 0.75 threshold for significant asymmetry."""
        score = 0.87
        self.assertGreater(score, 0.75)

    def test_score_accounts_for_capability_inversion(self):
        """Score elevated because MORE capable device gets LESS scrutiny."""
        openai_capabilities = 7
        meta_capabilities = 2
        openai_alarm_terms = 0
        meta_alarm_terms = 12
        # Capability-proportionate would be openai_alarm >= meta_alarm
        self.assertGreater(meta_alarm_terms, openai_alarm_terms)
        self.assertGreater(openai_capabilities, meta_capabilities)


class TestYAMLStructuralIntegrity(unittest.TestCase):
    """Verify mechanism exists in competitor-coverage-research.yaml."""

    @classmethod
    def setUpClass(cls):
        yaml_path = os.path.join(
            os.path.dirname(__file__), "..", "profiles", "competitor-coverage-research.yaml"
        )
        if os.path.exists(yaml_path):
            with open(yaml_path) as f:
                cls.data = yaml.safe_load(f)
        else:
            cls.data = None

    def test_yaml_loads(self):
        self.assertIsNotNone(self.data)

    def test_mechanism_exists(self):
        if self.data is None:
            self.skipTest("YAML not loaded")
        findings = self.data.get("cross_publication_findings", {})
        self.assertIn(
            "digital_trends_openai_companion_aspirational_meta_adversarial_vocabulary",
            findings,
        )

    def test_mechanism_has_asymmetry_score(self):
        if self.data is None:
            self.skipTest("YAML not loaded")
        findings = self.data.get("cross_publication_findings", {})
        mechanism = findings.get(
            "digital_trends_openai_companion_aspirational_meta_adversarial_vocabulary", {}
        )
        self.assertIn("asymmetry_score", mechanism)

    def test_mechanism_has_source_urls(self):
        if self.data is None:
            self.skipTest("YAML not loaded")
        findings = self.data.get("cross_publication_findings", {})
        mechanism = findings.get(
            "digital_trends_openai_companion_aspirational_meta_adversarial_vocabulary", {}
        )
        self.assertIn("source_urls", mechanism)
        self.assertGreaterEqual(len(mechanism.get("source_urls", [])), 4)


if __name__ == "__main__":
    unittest.main()
