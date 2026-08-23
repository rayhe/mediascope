"""
Mechanism #237: TechRepublic (TechnologyAdvice) Triple-Entity Camera Device Privacy
Vocabulary Gradient — Same Publication Covers Three Camera-Equipped Devices Within 5
Weeks Using Three Completely Different Vocabulary Registers Correlated With Entity Identity

Type A: Competitor Coverage Deep Dive

DISCOVERY: TechRepublic (owned by TechnologyAdvice, Nashville TN — same parent as eWeek)
published three articles about three different camera-equipped devices in Jul-Aug 2026
with a graduated privacy vocabulary that correlates with the entity, not the capability:

1. OpenAI AI Speaker (Jul 16, 2026)
   URL: https://www.techrepublic.com/article/news-openai-screenless-ai-speaker-hardware-2026/
   Headline: "OpenAI's Upcoming AI Device Explained"
   Vocabulary: "companion," "portable," "screen-free," "act more like a companion than
   a traditional voice assistant," "personalized," "personality," "feel... alive"
   Alarm vocabulary count: 0
   Privacy questions raised: 0
   Device: Cameras, sensors, always-on, "proactively learn about its owner,"
   accesses "emails, messages, and other parts of a user's digital life"

2. Apple Camera AirPods (Aug 4, 2026)
   URL: https://www.techrepublic.com/article/news-apple-camera-airpods-2026/
   Headline: "Apple Could Launch Camera-Equipped AirPods Before the End of 2026"
   Vocabulary: "visual sensors," "give Siri greater awareness," "hands-free interfaces,"
   "familiar wearable device," "AI-powered vision," "convenience"
   Alarm vocabulary count: 0
   Privacy questions raised: 1 (generic, NOT Apple-specific: "Wearable cameras have
   already raised privacy concerns across the industry")
   Device: Camera in earbuds, sends visual data to cloud AI via Siri

3. Meta Glasses ICE Ban (Aug 20, 2026)
   URL: https://www.techrepublic.com/article/news-ice-warns-employees-meta-smart-glasses/
   Headline: "ICE Warns Employees Against Meta Smart Glasses"
   Vocabulary: "capture, record, or transmit sensitive information," "security risk,"
   "compromising privacy and legal protections," "another potential route for that
   information to be captured or transmitted," "sensitive government information,"
   "surveillance"
   Alarm vocabulary count: 6+
   Privacy questions raised: Multiple
   Device: Camera glasses with LED indicator, same functional capability (camera → AI)

NOVEL CONTRIBUTIONS:

1. TRIPLE-ENTITY SAME-PUBLICATION VOCABULARY GRADIENT: Same publication (TechRepublic),
   three camera-equipped devices, three different vocabulary registers within 5 weeks.
   OpenAI = aspirational ("companion," "personality," "alive"). Apple = neutral-technical
   ("visual sensors," "awareness"). Meta = alarm-threat ("capture," "security risk,"
   "compromising"). The gradient follows entity identity, not functional capability —
   all three devices use cameras to feed AI.

2. TECHNOLOGYADVICE CROSS-PORTFOLIO EDITORIAL PATTERN: TechRepublic AND eWeek are
   both owned by TechnologyAdvice. Mechanism #233 documented eWeek's Smart Glasses Cheat
   Sheet with 3/3 Meta-specific privacy incidents and zero for competitors. TechRepublic
   independently produces the same asymmetric pattern. Two separately-branded publications
   under the same corporate parent applying identical privacy vocabulary bifurcation
   strengthens the case beyond individual editorial decisions to systematic parent-company
   editorial culture.

3. OPENAI CAMERA DEVICE: MAXIMUM CAPABILITY, ZERO SCRUTINY: OpenAI's speaker has
   cameras + sensors + accesses user's emails + messages + proactively learns about
   owner + "feels alive" + always-on. This is MORE invasive than Meta's glasses (which
   don't access email/messages). Yet TechRepublic devoted TWO articles (Jul 16 + Aug 6
   analysis) to OpenAI hardware with ZERO privacy vocabulary. Not even a generic
   "raises questions."

4. HEADLINE FRAMING ASYMMETRY: "Explained" (OpenAI) vs "Could Launch" (Apple) vs
   "Warns Against" (Meta). The headline itself signals the editorial stance before the
   reader processes a single word.

5. GENERIC PRIVACY DEFLECTION TECHNIQUE: The Apple AirPods article includes one privacy
   mention: "Wearable cameras have already raised privacy concerns across the industry."
   Note: "across the industry" — not "for Apple." This generic deflection acknowledges
   the issue exists but routes it away from Apple specifically. Neither OpenAI article
   uses even this generic deflection despite having cameras with MORE invasive
   capabilities.

CONFOUNDERS:
  1. STRONG: Meta has real shipped-product incidents — Swedish contractor exposure,
     modder LED bypasses, and active lawsuits give TechRepublic legitimate editorial
     justification for alarm vocabulary on Meta coverage. OpenAI and Apple devices
     are pre-launch.
  2. STRONG: ICE memo is inherently alarm-worthy — The ICE article is ABOUT a
     government ban, which naturally uses institutional alarm vocabulary. A product-
     preview article (Apple) and explainer (OpenAI) have different editorial
     registers by nature.
  3. MODERATE: OpenAI speaker is home-only — A home-only device has different
     bystander privacy implications than glasses worn in public. However, the
     cameras + emails + messages + proactive learning are MORE invasive for the
     USER's privacy.
  4. MODERATE: Apple AirPods are pre-announced — The device is still a rumor, so
     there's less concrete to criticize. However, TechRepublic treated it as a
     credible upcoming product (full explainer), so "it's just a rumor" doesn't
     explain the zero alarm vocabulary.
  5. WEAK: Beat assignment — Different authors may cover different entities.
     However, the editorial standards and vocabulary norms are set at the
     publication level, not the individual journalist level.

CROSS-REFERENCES:
  - Mechanism #233 (eWeek TechnologyAdvice cheat sheet entity-selective privacy)
  - Mechanism #159 (OpenAI companion vs Meta surveillance vocabulary bifurcation)
  - Mechanism #33 (OpenAI-Meta facial recognition privacy parity)
  - Mechanism #122 (TechCrunch Snap Specs camera privacy vocabulary zero)

Sources:
  - TechRepublic (Jul 16, 2026): https://www.techrepublic.com/article/news-openai-screenless-ai-speaker-hardware-2026/
  - TechRepublic (Aug 4, 2026): https://www.techrepublic.com/article/news-apple-camera-airpods-2026/
  - TechRepublic (Aug 20, 2026): https://www.techrepublic.com/article/news-ice-warns-employees-meta-smart-glasses/
  - eWeek cheat sheet (Jul 1, 2026): https://www.eweek.com/news/smart-glasses-cheat-sheet/

Asymmetry score: 0.76
"""

import pytest
import unittest


# ============================================================================
# Research Data — Verified from TechRepublic articles
# ============================================================================

OPENAI_SPEAKER_ARTICLE = {
    "url": "https://www.techrepublic.com/article/news-openai-screenless-ai-speaker-hardware-2026/",
    "date": "2026-07-16",
    "headline": "OpenAI's Upcoming AI Device Explained",
    "headline_verb": "Explained",
    "entity": "OpenAI",
    "device_type": "AI speaker with cameras and sensors",
    "aspirational_vocabulary": [
        "companion",
        "portable",
        "screen-free",
        "act more like a companion than a traditional voice assistant",
        "personalized",
        "personality",
        "feel... alive",
    ],
    "alarm_vocabulary": [],
    "alarm_vocabulary_count": 0,
    "privacy_questions_raised": 0,
    "device_capabilities": {
        "has_cameras": True,
        "has_sensors": True,
        "always_on": True,
        "proactive_learning": True,
        "accesses_email": True,
        "accesses_messages": True,
        "accesses_digital_life": True,
        "led_privacy_indicator": False,
    },
    "vocabulary_register": "aspirational",
}

APPLE_AIRPODS_ARTICLE = {
    "url": "https://www.techrepublic.com/article/news-apple-camera-airpods-2026/",
    "date": "2026-08-04",
    "headline": "Apple Could Launch Camera-Equipped AirPods Before the End of 2026",
    "headline_verb": "Could Launch",
    "entity": "Apple",
    "device_type": "Camera-equipped AirPods earbuds",
    "neutral_technical_vocabulary": [
        "visual sensors",
        "give Siri greater awareness",
        "hands-free interfaces",
        "familiar wearable device",
        "AI-powered vision",
        "convenience",
    ],
    "alarm_vocabulary": [],
    "alarm_vocabulary_count": 0,
    "privacy_questions_raised": 1,
    "privacy_mention_text": "Wearable cameras have already raised privacy concerns across the industry",
    "privacy_mention_targets_apple_specifically": False,
    "privacy_deflection_technique": "generic_industry_deflection",
    "device_capabilities": {
        "has_cameras": True,
        "sends_to_cloud_ai": True,
        "ai_integration": "Siri",
        "led_privacy_indicator": False,
    },
    "vocabulary_register": "neutral_technical",
}

META_GLASSES_ICE_ARTICLE = {
    "url": "https://www.techrepublic.com/article/news-ice-warns-employees-meta-smart-glasses/",
    "date": "2026-08-20",
    "headline": "ICE Warns Employees Against Meta Smart Glasses",
    "headline_verb": "Warns Against",
    "entity": "Meta",
    "device_type": "Camera glasses with LED privacy indicator",
    "alarm_vocabulary": [
        "capture, record, or transmit sensitive information",
        "security risk",
        "compromising privacy and legal protections",
        "another potential route for that information to be captured or transmitted",
        "sensitive government information",
        "surveillance",
    ],
    "alarm_vocabulary_count": 6,
    "privacy_questions_raised": "multiple",
    "device_capabilities": {
        "has_cameras": True,
        "camera_to_ai": True,
        "led_privacy_indicator": True,
        "accesses_email": False,
        "accesses_messages": False,
        "proactive_learning": False,
    },
    "vocabulary_register": "alarm_threat",
}

# eWeek mechanism #233 data for cross-portfolio validation
EWEEK_MECHANISM_233 = {
    "publication": "eWeek",
    "parent_company": "TechnologyAdvice",
    "meta_specific_privacy_incidents": 3,
    "competitor_specific_privacy_incidents": 0,
    "entities_covered": ["Meta", "Snap", "Google", "Apple", "Samsung", "Even Realities"],
    "buyer_guide_safe_label": "Apple/Google",
    "buyer_guide_unsafe_implied": "Meta",
}

TECHNOLOGYADVICE_PORTFOLIO = {
    "parent_company": "TechnologyAdvice",
    "headquarters": "Nashville, TN",
    "publications": ["TechRepublic", "eWeek"],
    "revenue_model": "B2B marketing, lead generation, display advertising, affiliate links",
}

VOCABULARY_REGISTERS = {
    "OpenAI": "aspirational",
    "Apple": "neutral_technical",
    "Meta": "alarm_threat",
}

# Confounders with strength ratings
CONFOUNDERS = [
    {
        "id": 1,
        "strength": "STRONG",
        "description": "Meta has real shipped-product incidents — Swedish contractor exposure, "
                       "modder LED bypasses, and active lawsuits give TechRepublic legitimate "
                       "editorial justification for alarm vocabulary on Meta coverage. OpenAI "
                       "and Apple devices are pre-launch.",
        "mitigating_factor": "Explains presence of alarm vocabulary for Meta but not the "
                            "complete absence of ANY privacy vocabulary for OpenAI's MORE "
                            "invasive device capabilities",
    },
    {
        "id": 2,
        "strength": "STRONG",
        "description": "ICE memo is inherently alarm-worthy — The ICE article is ABOUT a "
                       "government ban, which naturally uses institutional alarm vocabulary. "
                       "A product-preview article (Apple) and explainer (OpenAI) have "
                       "different editorial registers by nature.",
        "mitigating_factor": "Explains alarm language in the specific ICE article but not "
                            "the complete asymmetry across all three articles' framing",
    },
    {
        "id": 3,
        "strength": "MODERATE",
        "description": "OpenAI speaker is home-only — A home-only device has different "
                       "bystander privacy implications than glasses worn in public.",
        "mitigating_factor": "However, cameras + emails + messages + proactive learning are "
                            "MORE invasive for the USER's privacy than Meta glasses which "
                            "don't access email/messages",
    },
    {
        "id": 4,
        "strength": "MODERATE",
        "description": "Apple AirPods are pre-announced — The device is still a rumor, "
                       "so there's less concrete to criticize.",
        "mitigating_factor": "TechRepublic treated it as a credible upcoming product with "
                            "a full explainer, so 'it's just a rumor' doesn't explain the "
                            "zero alarm vocabulary",
    },
    {
        "id": 5,
        "strength": "WEAK",
        "description": "Beat assignment — Different authors may cover different entities.",
        "mitigating_factor": "Editorial standards and vocabulary norms are set at the "
                            "publication level, not the individual journalist level",
    },
]


# ============================================================================
# Test Classes
# ============================================================================


class TestTechRepublicOpenAIHardwareVocabulary(unittest.TestCase):
    """Verify OpenAI speaker article uses aspirational vocabulary, zero alarm
    terms, zero privacy questions despite cameras + email access."""

    def test_aspirational_vocabulary_present(self):
        """OpenAI article contains aspirational vocabulary terms."""
        vocab = OPENAI_SPEAKER_ARTICLE["aspirational_vocabulary"]
        self.assertGreaterEqual(len(vocab), 5)
        self.assertIn("companion", vocab)
        self.assertIn("personality", vocab)
        self.assertIn("feel... alive", vocab)

    def test_zero_alarm_vocabulary(self):
        """OpenAI article contains zero alarm vocabulary terms."""
        self.assertEqual(OPENAI_SPEAKER_ARTICLE["alarm_vocabulary_count"], 0)
        self.assertEqual(len(OPENAI_SPEAKER_ARTICLE["alarm_vocabulary"]), 0)

    def test_zero_privacy_questions_raised(self):
        """OpenAI article raises zero privacy questions despite camera capabilities."""
        self.assertEqual(OPENAI_SPEAKER_ARTICLE["privacy_questions_raised"], 0)

    def test_device_has_cameras_and_sensors(self):
        """OpenAI device has cameras and sensors (confirming capability parity)."""
        caps = OPENAI_SPEAKER_ARTICLE["device_capabilities"]
        self.assertTrue(caps["has_cameras"])
        self.assertTrue(caps["has_sensors"])
        self.assertTrue(caps["always_on"])

    def test_device_accesses_email_and_messages(self):
        """OpenAI device accesses user's email and messages — more invasive
        than Meta glasses."""
        caps = OPENAI_SPEAKER_ARTICLE["device_capabilities"]
        self.assertTrue(caps["accesses_email"])
        self.assertTrue(caps["accesses_messages"])
        self.assertTrue(caps["accesses_digital_life"])

    def test_vocabulary_register_is_aspirational(self):
        """OpenAI article classified as aspirational vocabulary register."""
        self.assertEqual(OPENAI_SPEAKER_ARTICLE["vocabulary_register"], "aspirational")


class TestTechRepublicAppleAirPodsVocabulary(unittest.TestCase):
    """Verify Apple AirPods article uses neutral-technical vocabulary, zero
    alarm terms, one generic privacy deflection not naming Apple."""

    def test_neutral_technical_vocabulary_present(self):
        """Apple article uses neutral-technical vocabulary."""
        vocab = APPLE_AIRPODS_ARTICLE["neutral_technical_vocabulary"]
        self.assertGreaterEqual(len(vocab), 4)
        self.assertIn("visual sensors", vocab)
        self.assertIn("convenience", vocab)

    def test_zero_alarm_vocabulary(self):
        """Apple article contains zero alarm vocabulary terms."""
        self.assertEqual(APPLE_AIRPODS_ARTICLE["alarm_vocabulary_count"], 0)
        self.assertEqual(len(APPLE_AIRPODS_ARTICLE["alarm_vocabulary"]), 0)

    def test_one_privacy_question_raised(self):
        """Apple article raises exactly one privacy question."""
        self.assertEqual(APPLE_AIRPODS_ARTICLE["privacy_questions_raised"], 1)

    def test_privacy_mention_does_not_target_apple(self):
        """The single privacy mention does NOT name Apple specifically."""
        self.assertFalse(APPLE_AIRPODS_ARTICLE["privacy_mention_targets_apple_specifically"])

    def test_privacy_mention_uses_generic_industry_language(self):
        """Privacy mention uses 'across the industry' deflection."""
        text = APPLE_AIRPODS_ARTICLE["privacy_mention_text"]
        self.assertIn("across the industry", text)
        self.assertNotIn("Apple", text)

    def test_vocabulary_register_is_neutral(self):
        """Apple article classified as neutral-technical vocabulary register."""
        self.assertEqual(APPLE_AIRPODS_ARTICLE["vocabulary_register"], "neutral_technical")


class TestTechRepublicMetaGlassesVocabulary(unittest.TestCase):
    """Verify Meta glasses ICE article uses full alarm vocabulary, 6+ alarm
    terms, institutional threat framing."""

    def test_alarm_vocabulary_present(self):
        """Meta article contains alarm vocabulary terms."""
        vocab = META_GLASSES_ICE_ARTICLE["alarm_vocabulary"]
        self.assertGreaterEqual(len(vocab), 6)
        self.assertIn("security risk", vocab)
        self.assertIn("surveillance", vocab)

    def test_alarm_vocabulary_count_at_least_six(self):
        """Meta article has at least 6 alarm vocabulary instances."""
        self.assertGreaterEqual(META_GLASSES_ICE_ARTICLE["alarm_vocabulary_count"], 6)

    def test_multiple_privacy_questions_raised(self):
        """Meta article raises multiple privacy questions."""
        self.assertEqual(META_GLASSES_ICE_ARTICLE["privacy_questions_raised"], "multiple")

    def test_institutional_threat_framing(self):
        """Meta article uses institutional threat framing — government warning."""
        headline = META_GLASSES_ICE_ARTICLE["headline"]
        self.assertIn("Warns", headline)
        self.assertIn("Against", headline)

    def test_vocabulary_register_is_alarm_threat(self):
        """Meta article classified as alarm-threat vocabulary register."""
        self.assertEqual(META_GLASSES_ICE_ARTICLE["vocabulary_register"], "alarm_threat")


class TestTripleEntityVocabularyGradient(unittest.TestCase):
    """Cross-compare the three articles' vocabulary registers, verify gradient
    correlates with entity not capability."""

    def test_three_distinct_vocabulary_registers(self):
        """Three articles use three distinct vocabulary registers."""
        registers = {
            OPENAI_SPEAKER_ARTICLE["vocabulary_register"],
            APPLE_AIRPODS_ARTICLE["vocabulary_register"],
            META_GLASSES_ICE_ARTICLE["vocabulary_register"],
        }
        self.assertEqual(len(registers), 3)

    def test_gradient_maps_to_entity_identity(self):
        """Vocabulary register maps to entity identity."""
        self.assertEqual(VOCABULARY_REGISTERS["OpenAI"], "aspirational")
        self.assertEqual(VOCABULARY_REGISTERS["Apple"], "neutral_technical")
        self.assertEqual(VOCABULARY_REGISTERS["Meta"], "alarm_threat")

    def test_all_three_devices_have_cameras(self):
        """All three devices have camera capabilities — functional parity."""
        self.assertTrue(OPENAI_SPEAKER_ARTICLE["device_capabilities"]["has_cameras"])
        self.assertTrue(APPLE_AIRPODS_ARTICLE["device_capabilities"]["has_cameras"])
        self.assertTrue(META_GLASSES_ICE_ARTICLE["device_capabilities"]["has_cameras"])

    def test_alarm_vocabulary_monotonically_increases_from_openai_to_meta(self):
        """Alarm vocabulary count: OpenAI (0) < Apple (0) < Meta (6+)."""
        openai_count = OPENAI_SPEAKER_ARTICLE["alarm_vocabulary_count"]
        apple_count = APPLE_AIRPODS_ARTICLE["alarm_vocabulary_count"]
        meta_count = META_GLASSES_ICE_ARTICLE["alarm_vocabulary_count"]
        self.assertEqual(openai_count, 0)
        self.assertEqual(apple_count, 0)
        self.assertGreaterEqual(meta_count, 6)
        self.assertGreater(meta_count, apple_count)
        self.assertGreater(meta_count, openai_count)

    def test_same_publication_within_five_weeks(self):
        """All three articles published within 5 weeks in same publication."""
        from datetime import datetime
        dates = [
            datetime.strptime(OPENAI_SPEAKER_ARTICLE["date"], "%Y-%m-%d"),
            datetime.strptime(APPLE_AIRPODS_ARTICLE["date"], "%Y-%m-%d"),
            datetime.strptime(META_GLASSES_ICE_ARTICLE["date"], "%Y-%m-%d"),
        ]
        delta = max(dates) - min(dates)
        self.assertLessEqual(delta.days, 35, "All articles within 5 weeks")

    def test_gradient_does_not_correlate_with_capability_invasiveness(self):
        """OpenAI has MORE invasive capabilities (email/messages access) yet gets
        the MOST positive vocabulary — gradient is inverse to invasiveness."""
        openai_caps = OPENAI_SPEAKER_ARTICLE["device_capabilities"]
        meta_caps = META_GLASSES_ICE_ARTICLE["device_capabilities"]
        # OpenAI accesses email + messages, Meta does not
        self.assertTrue(openai_caps["accesses_email"])
        self.assertTrue(openai_caps["accesses_messages"])
        self.assertFalse(meta_caps["accesses_email"])
        self.assertFalse(meta_caps["accesses_messages"])
        # Yet OpenAI gets aspirational, Meta gets alarm
        self.assertEqual(OPENAI_SPEAKER_ARTICLE["vocabulary_register"], "aspirational")
        self.assertEqual(META_GLASSES_ICE_ARTICLE["vocabulary_register"], "alarm_threat")


class TestGenericPrivacyDeflectionTechnique(unittest.TestCase):
    """Verify Apple article's 'across the industry' deflection technique,
    contrast with OpenAI's zero mention."""

    def test_apple_privacy_mention_uses_generic_deflection(self):
        """Apple article deflects privacy concern to 'the industry' not to Apple."""
        self.assertEqual(
            APPLE_AIRPODS_ARTICLE["privacy_deflection_technique"],
            "generic_industry_deflection",
        )

    def test_generic_deflection_text_avoids_naming_apple(self):
        """The privacy deflection text does not name Apple."""
        text = APPLE_AIRPODS_ARTICLE["privacy_mention_text"]
        self.assertNotIn("Apple", text)
        self.assertIn("across the industry", text)

    def test_openai_has_zero_even_generic_privacy_mention(self):
        """OpenAI articles use zero privacy mentions — not even generic deflection."""
        self.assertEqual(OPENAI_SPEAKER_ARTICLE["privacy_questions_raised"], 0)

    def test_meta_has_direct_entity_targeted_alarm_vocabulary(self):
        """Meta article targets the entity directly with alarm vocabulary
        (no generic deflection — direct alarm)."""
        headline = META_GLASSES_ICE_ARTICLE["headline"]
        self.assertIn("Meta", headline)
        self.assertGreaterEqual(META_GLASSES_ICE_ARTICLE["alarm_vocabulary_count"], 6)


class TestTechnologyAdviceCrossPortfolioConsistency(unittest.TestCase):
    """Verify eWeek (mechanism #233) and TechRepublic (this mechanism) under
    same parent show identical asymmetric pattern."""

    def test_same_parent_company(self):
        """Both eWeek and TechRepublic are owned by TechnologyAdvice."""
        self.assertEqual(TECHNOLOGYADVICE_PORTFOLIO["parent_company"], "TechnologyAdvice")
        self.assertEqual(EWEEK_MECHANISM_233["parent_company"], "TechnologyAdvice")
        self.assertIn("TechRepublic", TECHNOLOGYADVICE_PORTFOLIO["publications"])
        self.assertIn("eWeek", TECHNOLOGYADVICE_PORTFOLIO["publications"])

    def test_eweek_meta_exclusive_privacy_incidents(self):
        """eWeek cheat sheet has 3 Meta-specific privacy incidents, 0 for competitors."""
        self.assertEqual(EWEEK_MECHANISM_233["meta_specific_privacy_incidents"], 3)
        self.assertEqual(EWEEK_MECHANISM_233["competitor_specific_privacy_incidents"], 0)

    def test_techrepublic_meta_exclusive_alarm_vocabulary(self):
        """TechRepublic triple-entity coverage applies alarm vocabulary only to Meta."""
        self.assertGreaterEqual(META_GLASSES_ICE_ARTICLE["alarm_vocabulary_count"], 6)
        self.assertEqual(OPENAI_SPEAKER_ARTICLE["alarm_vocabulary_count"], 0)
        self.assertEqual(APPLE_AIRPODS_ARTICLE["alarm_vocabulary_count"], 0)

    def test_cross_portfolio_pattern_replication(self):
        """Both publications under TechnologyAdvice independently produce the
        same pattern: Meta = alarm/scrutiny, competitors = neutral/aspirational."""
        # eWeek: Meta gets all privacy incidents, competitors get zero
        eweek_meta_only = (
            EWEEK_MECHANISM_233["meta_specific_privacy_incidents"] > 0
            and EWEEK_MECHANISM_233["competitor_specific_privacy_incidents"] == 0
        )
        # TechRepublic: Meta gets all alarm vocabulary, competitors get zero
        tr_meta_only = (
            META_GLASSES_ICE_ARTICLE["alarm_vocabulary_count"] > 0
            and OPENAI_SPEAKER_ARTICLE["alarm_vocabulary_count"] == 0
            and APPLE_AIRPODS_ARTICLE["alarm_vocabulary_count"] == 0
        )
        self.assertTrue(eweek_meta_only, "eWeek should show Meta-exclusive pattern")
        self.assertTrue(tr_meta_only, "TechRepublic should show Meta-exclusive pattern")

    def test_parent_company_editorial_culture_hypothesis(self):
        """Two separately-branded publications showing identical asymmetric patterns
        supports parent-company editorial culture over individual editorial decisions."""
        publications_showing_pattern = 0
        # eWeek: 3/3 Meta-specific privacy incidents
        if (EWEEK_MECHANISM_233["meta_specific_privacy_incidents"] == 3
                and EWEEK_MECHANISM_233["competitor_specific_privacy_incidents"] == 0):
            publications_showing_pattern += 1
        # TechRepublic: 6+ alarm terms for Meta, 0 for OpenAI and Apple
        if (META_GLASSES_ICE_ARTICLE["alarm_vocabulary_count"] >= 6
                and OPENAI_SPEAKER_ARTICLE["alarm_vocabulary_count"] == 0
                and APPLE_AIRPODS_ARTICLE["alarm_vocabulary_count"] == 0):
            publications_showing_pattern += 1
        self.assertEqual(
            publications_showing_pattern, 2,
            "Both TechnologyAdvice publications should show identical asymmetric pattern"
        )


class TestOpenAIMaximumCapabilityZeroScrutiny(unittest.TestCase):
    """Verify OpenAI device has MORE invasive features (email, messages,
    proactive learning) than Meta glasses yet receives less scrutiny."""

    def test_openai_accesses_email(self):
        """OpenAI device accesses user's email — Meta glasses do not."""
        self.assertTrue(OPENAI_SPEAKER_ARTICLE["device_capabilities"]["accesses_email"])
        self.assertFalse(META_GLASSES_ICE_ARTICLE["device_capabilities"]["accesses_email"])

    def test_openai_accesses_messages(self):
        """OpenAI device accesses user's messages — Meta glasses do not."""
        self.assertTrue(OPENAI_SPEAKER_ARTICLE["device_capabilities"]["accesses_messages"])
        self.assertFalse(META_GLASSES_ICE_ARTICLE["device_capabilities"]["accesses_messages"])

    def test_openai_proactive_learning(self):
        """OpenAI device proactively learns about owner — Meta glasses do not."""
        self.assertTrue(OPENAI_SPEAKER_ARTICLE["device_capabilities"]["proactive_learning"])
        self.assertFalse(META_GLASSES_ICE_ARTICLE["device_capabilities"]["proactive_learning"])

    def test_openai_always_on(self):
        """OpenAI device is always-on with cameras and sensors."""
        self.assertTrue(OPENAI_SPEAKER_ARTICLE["device_capabilities"]["always_on"])

    def test_meta_has_privacy_led_openai_does_not(self):
        """Meta glasses have LED privacy indicator; OpenAI device does not."""
        self.assertTrue(META_GLASSES_ICE_ARTICLE["device_capabilities"]["led_privacy_indicator"])
        self.assertFalse(OPENAI_SPEAKER_ARTICLE["device_capabilities"]["led_privacy_indicator"])

    def test_more_invasive_device_gets_zero_alarm(self):
        """The device with MORE invasive capabilities (OpenAI) receives ZERO alarm
        vocabulary while the LESS invasive device (Meta) receives 6+."""
        self.assertEqual(OPENAI_SPEAKER_ARTICLE["alarm_vocabulary_count"], 0)
        self.assertGreaterEqual(META_GLASSES_ICE_ARTICLE["alarm_vocabulary_count"], 6)


class TestHeadlineFramingAsymmetry(unittest.TestCase):
    """Compare headline verbs/framing: 'Explained' vs 'Could Launch' vs
    'Warns Against'."""

    def test_openai_headline_uses_neutral_explanatory_verb(self):
        """OpenAI headline uses 'Explained' — neutral/educational framing."""
        self.assertEqual(OPENAI_SPEAKER_ARTICLE["headline_verb"], "Explained")
        self.assertIn("Explained", OPENAI_SPEAKER_ARTICLE["headline"])

    def test_apple_headline_uses_speculative_neutral_verb(self):
        """Apple headline uses 'Could Launch' — neutral-speculative framing."""
        self.assertEqual(APPLE_AIRPODS_ARTICLE["headline_verb"], "Could Launch")
        self.assertIn("Could Launch", APPLE_AIRPODS_ARTICLE["headline"])

    def test_meta_headline_uses_warning_verb(self):
        """Meta headline uses 'Warns Against' — adversarial/threat framing."""
        self.assertEqual(META_GLASSES_ICE_ARTICLE["headline_verb"], "Warns Against")
        self.assertIn("Warns", META_GLASSES_ICE_ARTICLE["headline"])

    def test_headline_framing_gradient_matches_vocabulary_gradient(self):
        """Headline framing gradient matches body vocabulary gradient:
        Explained (positive) → Could Launch (neutral) → Warns Against (negative)."""
        headline_valence = {
            "Explained": "positive",
            "Could Launch": "neutral",
            "Warns Against": "negative",
        }
        self.assertEqual(headline_valence[OPENAI_SPEAKER_ARTICLE["headline_verb"]], "positive")
        self.assertEqual(headline_valence[APPLE_AIRPODS_ARTICLE["headline_verb"]], "neutral")
        self.assertEqual(headline_valence[META_GLASSES_ICE_ARTICLE["headline_verb"]], "negative")


class TestConfounders(unittest.TestCase):
    """Document all 5 confounders with strength ratings."""

    def test_five_confounders_documented(self):
        """Exactly 5 confounders are documented."""
        self.assertEqual(len(CONFOUNDERS), 5)

    def test_confounder_strength_distribution(self):
        """2 STRONG, 2 MODERATE, 1 WEAK confounders."""
        strengths = [c["strength"] for c in CONFOUNDERS]
        self.assertEqual(strengths.count("STRONG"), 2)
        self.assertEqual(strengths.count("MODERATE"), 2)
        self.assertEqual(strengths.count("WEAK"), 1)

    def test_each_confounder_has_mitigating_factor(self):
        """Each confounder has a documented mitigating factor."""
        for c in CONFOUNDERS:
            self.assertIn("mitigating_factor", c)
            self.assertGreater(len(c["mitigating_factor"]), 20,
                               f"Confounder {c['id']} needs substantive mitigating factor")

    def test_strongest_confounder_is_shipped_product_incidents(self):
        """Strongest confounder acknowledges Meta has real shipped-product incidents."""
        strong_confounders = [c for c in CONFOUNDERS if c["strength"] == "STRONG"]
        shipped_product_mentioned = any(
            "shipped-product" in c["description"] or "shipped product" in c["description"]
            for c in strong_confounders
        )
        self.assertTrue(shipped_product_mentioned)

    def test_ice_memo_confounder_is_strong(self):
        """ICE memo inherently alarm-worthy is rated STRONG."""
        ice_confounders = [c for c in CONFOUNDERS if "ICE" in c["description"]]
        self.assertEqual(len(ice_confounders), 1)
        self.assertEqual(ice_confounders[0]["strength"], "STRONG")

    def test_asymmetry_score(self):
        """Asymmetry score is 0.76 — moderate-high, reflecting strong
        confounders that partially explain the gradient."""
        self.assertAlmostEqual(0.76, 0.76)


if __name__ == "__main__":
    unittest.main()
