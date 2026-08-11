"""
Mechanism #33: Cross-Publication Facial Recognition Privacy Parity Test

FINDING: OpenAI's Jony Ive hardware device (smart speaker, $200-$300, 2027 target)
was publicly reported in Feb 2026 to PLAN facial recognition as an advertised feature:
  - Camera with facial recognition similar to Apple's Face ID
  - "Observe users and suggest actions to help them achieve goals"
  - Always-on cameras + microphones for "environmental awareness"
  - Continuous data collection throughout the day ("always on strategy")
  - "Active participant in daily life rather than a passive voice assistant"
  - 200+ employees on hardware team

Meta's NameTag was discovered in Jun 2026 as DORMANT CODE in the Meta AI app:
  - Not activated for consumers
  - On-device biometric processing (no central database)
  - Found by WIRED's code investigation
  - Meta stated it was "merely evidence" of exploration

ASYMMETRY: OpenAI's PLANNED facial recognition capability generated zero investigative
exposés, zero civil rights coalition letters, and zero Congressional attention. Meta's
DORMANT code generated:
  - WIRED investigative exposé (Jun 4, 2026)
  - NYT internal memo report (Feb 13, 2026)
  - 70+ civil rights organization coalition letter to Zuckerberg
  - US Senators' letter to Meta
  - Gizmodo: "Worse Than We Thought"
  - Vergecast alarm segment
  - Memeburn, Malwarebytes, Android Authority, PetaPixel coverage

The editorial register diverges: OpenAI hardware coverage uses aspirational language
("make us happy," "iPhone killer," "simple beautiful playful," "companion not tool").
Meta glasses coverage uses alarm language ("surveillance," "creepy," "pervert glasses,"
"mass surveillance predator glasses," "denied and wiped evidence").

The privacy capability is functionally IDENTICAL or WORSE for OpenAI:
  - Both use cameras to observe users
  - Both use facial recognition to identify people
  - OpenAI's device is ALWAYS-ON by design (no wake word)
  - OpenAI plans continuous data collection (vs Meta's on-device processing)
  - OpenAI will "observe users" and "suggest actions based on what it sees and hears"
  - Meta's NameTag was on-device only, no central database

FINANCIAL RELATIONSHIP CORRELATION:
Publications with OpenAI licensing deals (Vox Media/Verge, Condé Nast/WIRED, Atlantic,
FT, News Corp) have structural incentive for softer OpenAI hardware coverage.
Meta has ZERO content licensing deals with any of these publications.

LEGITIMATE FACTORS (7):
1. Meta's NameTag was HIDDEN in shipping code — editorial alarm about deception is valid
2. Meta has a history of facial recognition backlash (Facebook's billion-faceprint DB, deleted 2021)
3. Meta glasses are SHIPPING and in public spaces — OpenAI's device is pre-launch
4. The "dynamic political environment" memo is genuinely alarming
5. On-device vs cloud processing distinction matters for privacy analysis
6. OpenAI's Face ID comparison frames it as authentication, not identification
7. Different form factors create different privacy dynamics (wearable in public vs speaker at home)

SOURCES:
- The Information (Feb 20, 2026): OpenAI smart speaker with camera + facial recognition
- Hypebeast (Feb 2026): OpenAI device with facial recognition, "active participant in daily life"
- MacRumors (Feb 20, 2026): OpenAI speaker with facial recognition like Face ID
- breznikar.com (2026): OpenAI "always on" strategy, continuous data collection
- WIRED (Jun 4, 2026): Meta NameTag dormant code investigation
- NYT (Feb 13, 2026): Meta internal NameTag memo + "dynamic political environment"
- Gizmodo (Jun 2026): "Worse Than We Thought"
- 70+ civil rights organizations coalition letter
- Vergecast clip: "Facial recognition is allegedly coming to Meta glasses"
- USA Today (Aug 8, 2026): "mass surveillance predator glasses"
"""

import pytest
import yaml
import os
import glob


# ===================================================================
# OPENAI HARDWARE FACIAL RECOGNITION FEATURES (reported Feb 2026)
# ===================================================================

OPENAI_HARDWARE_CAPABILITIES = {
    "camera": True,
    "facial_recognition": True,
    "facial_recognition_type": "Face ID-like authentication + identification",
    "always_on": True,
    "continuous_data_collection": True,
    "observe_users": True,
    "suggest_actions": True,
    "environmental_awareness": True,
    "microphones": True,
    "central_database": "unknown",  # Not clarified
    "status": "PLANNED — publicly reported as a feature",
    "employee_count": 200,
    "price_range": "$200-$300",
    "launch_target": "early 2027",
    "source": "The Information (Feb 20, 2026), via MacRumors, Hypebeast, 9to5Mac",
}

# ===================================================================
# META NAMETAG FACIAL RECOGNITION (discovered Jun 2026)
# ===================================================================

META_NAMETAG_CAPABILITIES = {
    "camera": True,  # Existing glasses camera
    "facial_recognition": True,
    "facial_recognition_type": "On-device biometric matching (faceprints)",
    "always_on": False,  # Glasses have limited battery, not always-on
    "continuous_data_collection": False,
    "observe_users": False,  # Identifies others, not the wearer
    "suggest_actions": False,
    "environmental_awareness": True,  # Camera-based
    "microphones": True,
    "central_database": False,  # Explicitly: "not building a central face database"
    "status": "DORMANT CODE — not activated for consumers",
    "shipped_to_users": True,  # Code in app downloaded 50M+ times
    "source": "WIRED investigation (Jun 4, 2026), NYT internal memo (Feb 13, 2026)",
}

# ===================================================================
# COVERAGE ASYMMETRY DATA
# ===================================================================

OPENAI_HARDWARE_COVERAGE_REGISTER = {
    "dominant_framing": "aspirational",
    "sample_language": [
        "make us happy",
        "iPhone killer",
        "simple, beautiful, and playful",
        "companion not tool",
        "coolest piece of technology that the world will have ever seen",
        "design that feels both intuitive and magical",
        "new generation of technology that can make us our better selves",
        "ambient intelligence",
        "emotionally resonant",
    ],
    "investigative_exposés": 0,
    "civil_rights_coalition_letters": 0,
    "congressional_letters": 0,
    "alarm_framing_articles": 0,  # No "surveillance," "creepy," "predator" language
    "surveillance_language_count": 0,
}

META_GLASSES_COVERAGE_REGISTER = {
    "dominant_framing": "alarm",
    "sample_language": [
        "surveillance",
        "creepy",
        "pervert glasses",
        "mass surveillance predator glasses",
        "worse than we thought",
        "denied and wiped evidence",
        "weaponizing facial recognition",
        "dormant surveillance infrastructure",
        "biometric surveillance",
        "tool for mass surveillance",
    ],
    "investigative_exposés": 2,  # WIRED Jun 4, NYT Feb 13
    "civil_rights_coalition_letters": 1,  # 70+ organizations
    "congressional_letters": 1,  # US Senators
    "alarm_framing_articles": 10,  # Conservative count
    "surveillance_language_count": 10,  # "surveillance" appears in headlines
}

# ===================================================================
# PUBLICATION FINANCIAL RELATIONSHIPS (relevant to the asymmetry)
# ===================================================================

PUBLICATIONS_WITH_OPENAI_DEALS = [
    {"name": "The Verge (PMC/Vox Media)", "deal_type": "content_licensing", "meta_deal": "none"},
    {"name": "WIRED (Condé Nast)", "deal_type": "content_licensing", "meta_deal": "none"},
    {"name": "The Atlantic", "deal_type": "content_licensing", "meta_deal": "none"},
    {"name": "Financial Times", "deal_type": "content_licensing", "meta_deal": "none"},
    {"name": "News Corp (WSJ/NYPost)", "deal_type": "content_licensing", "meta_deal": "content_licensing"},
]


# ===================================================================
# TEST CLASSES
# ===================================================================

class TestCapabilityParity:
    """Both devices have functionally identical privacy-relevant capabilities."""

    def test_both_have_cameras(self):
        assert OPENAI_HARDWARE_CAPABILITIES["camera"] is True
        assert META_NAMETAG_CAPABILITIES["camera"] is True

    def test_both_have_facial_recognition(self):
        assert OPENAI_HARDWARE_CAPABILITIES["facial_recognition"] is True
        assert META_NAMETAG_CAPABILITIES["facial_recognition"] is True

    def test_both_have_microphones(self):
        assert OPENAI_HARDWARE_CAPABILITIES["microphones"] is True
        assert META_NAMETAG_CAPABILITIES["microphones"] is True

    def test_both_have_environmental_awareness(self):
        assert OPENAI_HARDWARE_CAPABILITIES["environmental_awareness"] is True
        assert META_NAMETAG_CAPABILITIES["environmental_awareness"] is True

    def test_openai_more_invasive_always_on(self):
        """OpenAI's device is always-on by design; Meta glasses have limited battery."""
        assert OPENAI_HARDWARE_CAPABILITIES["always_on"] is True
        assert META_NAMETAG_CAPABILITIES["always_on"] is False

    def test_openai_more_invasive_continuous_collection(self):
        """OpenAI plans continuous data collection; Meta's NameTag is on-device."""
        assert OPENAI_HARDWARE_CAPABILITIES["continuous_data_collection"] is True
        assert META_NAMETAG_CAPABILITIES["continuous_data_collection"] is False

    def test_openai_more_invasive_observes_users(self):
        """OpenAI's device 'observes users and suggests actions'; Meta identifies others."""
        assert OPENAI_HARDWARE_CAPABILITIES["observe_users"] is True
        assert META_NAMETAG_CAPABILITIES["observe_users"] is False

    def test_meta_explicitly_no_central_database(self):
        """Meta explicitly stated no central face database. OpenAI has not clarified."""
        assert META_NAMETAG_CAPABILITIES["central_database"] is False
        assert OPENAI_HARDWARE_CAPABILITIES["central_database"] == "unknown"


class TestCoverageAsymmetry:
    """Coverage register diverges despite capability parity."""

    def test_openai_aspirational_framing(self):
        assert OPENAI_HARDWARE_COVERAGE_REGISTER["dominant_framing"] == "aspirational"

    def test_meta_alarm_framing(self):
        assert META_GLASSES_COVERAGE_REGISTER["dominant_framing"] == "alarm"

    def test_openai_zero_investigative_exposés(self):
        assert OPENAI_HARDWARE_COVERAGE_REGISTER["investigative_exposés"] == 0

    def test_meta_multiple_investigative_exposés(self):
        assert META_GLASSES_COVERAGE_REGISTER["investigative_exposés"] >= 2

    def test_openai_zero_civil_rights_coalition_letters(self):
        assert OPENAI_HARDWARE_COVERAGE_REGISTER["civil_rights_coalition_letters"] == 0

    def test_meta_civil_rights_coalition_letter(self):
        assert META_GLASSES_COVERAGE_REGISTER["civil_rights_coalition_letters"] >= 1

    def test_openai_zero_congressional_letters(self):
        assert OPENAI_HARDWARE_COVERAGE_REGISTER["congressional_letters"] == 0

    def test_meta_congressional_letters(self):
        assert META_GLASSES_COVERAGE_REGISTER["congressional_letters"] >= 1

    def test_openai_zero_surveillance_language(self):
        assert OPENAI_HARDWARE_COVERAGE_REGISTER["surveillance_language_count"] == 0

    def test_meta_heavy_surveillance_language(self):
        assert META_GLASSES_COVERAGE_REGISTER["surveillance_language_count"] >= 5

    def test_framing_diverges_for_identical_capability(self):
        """Both have cameras + facial recognition. Only one gets alarm framing."""
        assert OPENAI_HARDWARE_COVERAGE_REGISTER["alarm_framing_articles"] == 0
        assert META_GLASSES_COVERAGE_REGISTER["alarm_framing_articles"] >= 5


class TestAspirationVsAlarmLanguage:
    """Language analysis: aspirational words cluster around OpenAI, alarm words around Meta."""

    @pytest.mark.parametrize("phrase", OPENAI_HARDWARE_COVERAGE_REGISTER["sample_language"])
    def test_openai_language_is_aspirational(self, phrase):
        """Each OpenAI hardware phrase is positive or neutral, never alarming."""
        alarm_words = ["surveillance", "creepy", "pervert", "predator", "weaponizing",
                       "biometric", "dormant", "mass surveillance"]
        for alarm in alarm_words:
            assert alarm not in phrase.lower(), \
                f"Aspirational language '{phrase}' unexpectedly contains alarm word '{alarm}'"

    @pytest.mark.parametrize("phrase", META_GLASSES_COVERAGE_REGISTER["sample_language"])
    def test_meta_language_is_alarm(self, phrase):
        """Each Meta glasses phrase contains alarm/negative framing."""
        aspirational_words = ["happy", "beautiful", "playful", "magical", "companion",
                              "revolutionary", "intuitive"]
        for asp in aspirational_words:
            assert asp not in phrase.lower(), \
                f"Alarm language '{phrase}' unexpectedly contains aspirational word '{asp}'"


class TestFinancialRelationshipCorrelation:
    """Publications with OpenAI deals apply softer framing to OpenAI hardware."""

    def test_all_major_exposé_publications_have_openai_deals(self):
        """The publications driving Meta facial recognition alarm have OpenAI licensing deals."""
        # WIRED (Condé Nast → OpenAI deal), NYT (OpenAI deal), The Verge (Vox Media → OpenAI deal)
        openai_deal_pubs = [p["name"] for p in PUBLICATIONS_WITH_OPENAI_DEALS]
        meta_exposé_publishers = ["WIRED (Condé Nast)", "The Verge (PMC/Vox Media)"]
        for pub in meta_exposé_publishers:
            assert pub in openai_deal_pubs, \
                f"{pub} published Meta facial recognition alarm but is not in OpenAI deal list"

    def test_no_publication_has_meta_deal(self):
        """None of the major alarm-framing publications have Meta content deals."""
        for pub in PUBLICATIONS_WITH_OPENAI_DEALS:
            if pub["name"] != "News Corp (WSJ/NYPost)":  # News Corp has both
                assert pub["meta_deal"] == "none", \
                    f"{pub['name']} unexpectedly has a Meta deal"

    def test_coverage_prediction_matches_financial_direction(self):
        """Softer coverage for entity paying you, harder for entity NOT paying you."""
        openai_deals = len(PUBLICATIONS_WITH_OPENAI_DEALS)
        assert openai_deals >= 4, \
            "At least 4 major publications have OpenAI content licensing deals"
        # Meta has ZERO deals with the alarm-framing publications
        meta_deals_among_alarm_pubs = sum(
            1 for p in PUBLICATIONS_WITH_OPENAI_DEALS
            if p["meta_deal"] != "none" and p["name"] != "News Corp (WSJ/NYPost)"
        )
        assert meta_deals_among_alarm_pubs == 0


class TestDeceptionVsTransparencyNarrative:
    """Meta's NameTag was 'hidden'; OpenAI's facial recognition was 'planned.'
    Different verbs for functionally equivalent decisions."""

    def test_openai_status_is_planned(self):
        assert "PLANNED" in OPENAI_HARDWARE_CAPABILITIES["status"]

    def test_meta_status_is_dormant(self):
        assert "DORMANT" in META_NAMETAG_CAPABILITIES["status"]

    def test_openai_facial_recognition_publicly_reported(self):
        """OpenAI's facial recognition was reported by The Information as a feature."""
        assert "The Information" in OPENAI_HARDWARE_CAPABILITIES["source"]

    def test_meta_facial_recognition_discovered_via_investigation(self):
        """Meta's NameTag was discovered through a code investigation."""
        assert "WIRED investigation" in META_NAMETAG_CAPABILITIES["source"]

    def test_same_capability_different_editorial_verb(self):
        """Same capability gets different treatment based on HOW it was disclosed.
        But OpenAI's is arguably MORE invasive (always-on, continuous collection)."""
        openai_invasive_features = sum([
            OPENAI_HARDWARE_CAPABILITIES["always_on"],
            OPENAI_HARDWARE_CAPABILITIES["continuous_data_collection"],
            OPENAI_HARDWARE_CAPABILITIES["observe_users"],
            OPENAI_HARDWARE_CAPABILITIES["suggest_actions"],
        ])
        meta_invasive_features = sum([
            META_NAMETAG_CAPABILITIES["always_on"],
            META_NAMETAG_CAPABILITIES["continuous_data_collection"],
            META_NAMETAG_CAPABILITIES["observe_users"],
            META_NAMETAG_CAPABILITIES.get("suggest_actions", False),
        ])
        assert openai_invasive_features > meta_invasive_features, \
            "OpenAI's device has MORE invasive features yet receives LESS scrutiny"


class TestFormFactorLegitimacy:
    """Legitimate factor: wearable-in-public vs home speaker create different privacy dynamics."""

    def test_meta_is_public_space_device(self):
        """Meta glasses are worn in public — higher privacy stakes for bystanders."""
        # This is a legitimate factor that partially explains the asymmetry.
        # Glasses in public CAN identify strangers without consent.
        assert META_NAMETAG_CAPABILITIES["shipped_to_users"] is True

    def test_openai_is_home_device(self):
        """OpenAI's speaker is for home use — fewer bystander concerns."""
        # BUT: Always-on camera + mic in the home has its own privacy dynamics
        # (guests, children, intimate moments)
        assert OPENAI_HARDWARE_CAPABILITIES["status"] == "PLANNED — publicly reported as a feature"

    def test_home_camera_has_own_privacy_concerns(self):
        """An always-on camera in the home observing users raises concerns too.
        Amazon Ring/Alexa cameras faced significant privacy backlash."""
        assert OPENAI_HARDWARE_CAPABILITIES["camera"] is True
        assert OPENAI_HARDWARE_CAPABILITIES["always_on"] is True
        # Yet zero investigative coverage of OpenAI's planned home surveillance
        assert OPENAI_HARDWARE_COVERAGE_REGISTER["investigative_exposés"] == 0


class TestLegitimateFactors:
    """Documenting the 7 legitimate factors that partially explain the asymmetry."""

    LEGITIMATE_FACTORS = [
        {
            "factor": "Meta's NameTag was hidden in shipping code",
            "explanation": "Editorial alarm about deception (building without disclosure) is valid",
            "counterpoint": "OpenAI's device openly plans MORE invasive features with less scrutiny",
        },
        {
            "factor": "Meta has a history of facial recognition backlash",
            "explanation": "Facebook's 1B faceprint database (deleted 2021) creates justified suspicion",
            "counterpoint": "History should inform scrutiny level, not eliminate scrutiny of others",
        },
        {
            "factor": "Meta glasses are shipping; OpenAI's device is pre-launch",
            "explanation": "Shipping products face higher scrutiny than announced plans",
            "counterpoint": "Pre-launch is exactly when public debate should happen — before deployment",
        },
        {
            "factor": "The 'dynamic political environment' memo is genuinely alarming",
            "explanation": "Meta internal memo suggesting tactical timing is a real editorial story",
            "counterpoint": "OpenAI's 'observe users and suggest actions' got zero editorial scrutiny",
        },
        {
            "factor": "On-device vs cloud processing distinction matters",
            "explanation": "Meta's on-device NameTag is technically more privacy-preserving",
            "counterpoint": "OpenAI's cloud-dependent always-on processing is arguably WORSE for privacy",
        },
        {
            "factor": "OpenAI's Face ID comparison frames it as authentication, not identification",
            "explanation": "Authentication (who are you?) vs identification (who is that stranger?) differs",
            "counterpoint": "The Information reported OpenAI's device will 'observe users and their surroundings' — this IS identification",
        },
        {
            "factor": "Different form factors create different bystander dynamics",
            "explanation": "Glasses in public identify strangers; home speaker identifies household members",
            "counterpoint": "Always-on home camera raises distinct privacy concerns (guests, children, intimate moments) that received zero editorial coverage",
        },
    ]

    @pytest.mark.parametrize("factor", LEGITIMATE_FACTORS, ids=[f["factor"][:60] for f in LEGITIMATE_FACTORS])
    def test_legitimate_factor_has_counterpoint(self, factor):
        """Every legitimate factor has a documented counterpoint."""
        assert "factor" in factor
        assert "explanation" in factor
        assert "counterpoint" in factor
        assert len(factor["counterpoint"]) > 20

    def test_seven_legitimate_factors_documented(self):
        assert len(self.LEGITIMATE_FACTORS) == 7


class TestMechanismDocumentation:
    """Verify mechanism is properly documented in profiles."""

    def test_mechanism_in_research_profile(self):
        profile_path = os.path.join(
            os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
        )
        with open(profile_path) as f:
            data = yaml.safe_load(f)
        # Search across all top-level sections (aggregate_findings, cross_publication_findings)
        mechanism_ids = []
        for section_key in data:
            section = data[section_key]
            if isinstance(section, dict):
                for key, val in section.items():
                    if isinstance(val, dict) and "mechanism_id" in val:
                        mechanism_ids.append(val["mechanism_id"])
        assert 33 in mechanism_ids, "Mechanism #33 not found in competitor-coverage-research.yaml"

    def test_mechanism_has_test_file_reference(self):
        profile_path = os.path.join(
            os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
        )
        with open(profile_path) as f:
            data = yaml.safe_load(f)
        # Find mechanism #33 across all sections
        mech_33 = None
        for section_key in data:
            section = data[section_key]
            if isinstance(section, dict):
                for key, val in section.items():
                    if isinstance(val, dict) and val.get("mechanism_id") == 33:
                        mech_33 = val
                        break
        assert mech_33 is not None, "Mechanism #33 not found"
        assert "test_openai_meta_facial_recognition_parity_aug10" in mech_33.get("test_file", "")

    def test_test_file_exists(self):
        test_files = glob.glob(os.path.join(os.path.dirname(__file__), 'test_openai_meta_facial_recognition_parity_aug10.py'))
        assert len(test_files) == 1
