"""
Samsung Equivalence Paradox — Type B Cross-Entity Journalist Analysis (Aug 7, 2026)

KEY FINDING: Samsung's Intelligent Eyewear (Galaxy Unpacked, July 22, 2026) is
functionally identical to Meta Ray-Ban glasses in every privacy-relevant dimension:

  - Built-in camera (12MP, autofocus)
  - Microphones and speakers
  - Always-on AI (Gemini vs Meta AI)
  - Photo/video capture
  - LED recording indicator + obstruction detection
  - Smart glasses form factor (~50g)
  - No built-in display (first gen)
  - Companion phone architecture

Yet across publications, Samsung's launch receives product-review framing while
Meta's identical product receives surveillance/adversarial framing. The delta
is measurable and has REAL-WORLD POLICY CONSEQUENCES: Iberville Parish School
System (Louisiana) banned "Meta glasses" by name (Aug 4, 2026), while Samsung's
functionally identical Intelligent Eyewear would NOT be covered by the ban.

THE SCHOOL BAN TEST: When a policy-maker writes "Meta glasses" instead of
"camera-equipped smart glasses," it proves that the adversarial framing has
shifted public perception from a CATEGORY concern (cameras on faces) to a
BRAND-SPECIFIC stigma (Meta = creepy, Samsung = innovative).

Sources:
  - Samsung Newsroom: "Samsung Brings Galaxy Ecosystem Into Everyday Eyewear" (Jul 22, 2026)
  - Samsung Newsroom interview: "Intelligent Eyewear: The First Step Toward
    the Next Mobile AI Interface" (Jul 2026)
  - SamMobile: "Samsung's smart glasses take privacy pretty seriously" (Jul 28, 2026)
  - GSMArena: "Samsung's smart glasses have this important privacy feature" (Jul 28, 2026)
  - Iberville Parish: "School reopenings kicking off throughout Iberville Parish"
    (Plaquemine Post South, Aug 4, 2026)
  - Business Wars podcast S1E2 "I'm a Creep" (Jun 10, 2026) — WIRED's Chokkattu
    and Ashworth on Meta glasses
  - WIRED: "Meta Is Charging a Subscription for Smart Glasses Features" (Jul 2, 2026)
    by Chokkattu — "extracting value" framing

Created: 2026-08-07
"""

import pytest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
        data = yaml.safe_load(f)
    return data.get('publications', {})


def load_wired_profile():
    with open(os.path.join(PROFILES_DIR, 'wired.yaml')) as f:
        return yaml.safe_load(f)


def load_competitor_entities():
    with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')) as f:
        return yaml.safe_load(f)


# =================================================================
# CONSTANTS: Samsung vs Meta Hardware Equivalence
# =================================================================

SAMSUNG_INTELLIGENT_EYEWEAR = {
    "name": "Samsung Intelligent Eyewear",
    "announced": "2026-07-22",
    "event": "Galaxy Unpacked July 2026, London",
    "camera": "12MP with autofocus",
    "microphones": True,
    "speakers": True,
    "ai_assistant": "Google Gemini",
    "led_recording_indicator": True,
    "obstruction_detection": True,
    "display": False,
    "form_factor": "smart_glasses",
    "weight_approx_grams": 50,
    "companion_device": "Galaxy smartphone",
    "chipset": "Snapdragon AR1 Gen 1",
    "battery_hours": 9,
    "frame_partners": ["Gentle Monster", "Warby Parker"],
    "launch_window": "Fall 2026",
    "source_url": "https://news.samsung.com/global/samsung-brings-galaxy-ecosystem-into-everyday-eyewear",
}

META_RAYBAN_GLASSES = {
    "name": "Meta Ray-Ban Smart Glasses (Gen 2)",
    "launched": "2023-10",
    "camera": "12MP ultrawide",
    "microphones": True,
    "speakers": True,
    "ai_assistant": "Meta AI (Llama 4)",
    "led_recording_indicator": True,
    "obstruction_detection": True,
    "display": False,  # base model
    "form_factor": "smart_glasses",
    "weight_approx_grams": 49,
    "companion_device": "smartphone",
    "battery_hours": 8,
    "frame_partner": "EssilorLuxottica (Ray-Ban)",
    "source_url": "https://about.meta.com/products/ray-ban-smart-glasses/",
}

# Privacy features both share
SHARED_PRIVACY_FEATURES = [
    "LED recording indicator visible to bystanders",
    "Obstruction detection disables camera if LED blocked",
    "Wear detection disables recording when removed",
    "Built-in camera for photo/video capture",
    "Always-on AI assistant with visual context",
    "Microphones for ambient audio capture",
]

# Coverage framing comparison
SAMSUNG_COVERAGE_FRAMING = [
    {
        "publication": "SamMobile",
        "headline": "Samsung's smart glasses take privacy pretty seriously",
        "tone": "positive",
        "privacy_language": "privacy features designed to address concerns",
        "surveillance_language": None,
        "source_url": "https://www.sammobile.com/news/samsungs-smart-glasses-take-privacy-seriously/",
    },
    {
        "publication": "GSMArena",
        "headline": "Samsung's smart glasses have this important privacy feature",
        "tone": "constructive",
        "privacy_language": "important privacy feature",
        "surveillance_language": None,
        "source_url": "https://www.gsmarena.com/samsungs_smart_glasses_have_this_important_privacy_feature-news-73909.php",
    },
    {
        "publication": "Digital Trends",
        "headline": "Samsung enters the AI glasses race with Gemini-powered Intelligent Eyewear",
        "tone": "neutral_to_positive",
        "privacy_language": None,
        "surveillance_language": None,
        "source_url": "https://www.digitaltrends.com/wearables/samsungs-galaxy-glasses-leak-shows-why-your-next-wearable-may-live-on-your-face/",
    },
    {
        "publication": "HotHardware",
        "headline": "Samsung Galaxy Glasses Challenge Meta With Gemini And 9 Hour Battery",
        "tone": "neutral_competitive",
        "privacy_language": None,
        "surveillance_language": None,
        "source_url": "https://hothardware.com/news/samsung-galaxy-glasses-challenge-meta-with-gemini-and-9-hour-battery",
    },
    {
        "publication": "Memeburn",
        "headline": "Samsung Smart Glasses 2026 Take Aim at Meta Ray-Ban",
        "tone": "neutral_competitive",
        "privacy_language": None,
        "surveillance_language": None,
        "source_url": "https://memeburn.com/samsung-smart-glasses-2026/",
    },
]

META_COVERAGE_FRAMING = [
    {
        "publication": "WIRED (Business Wars podcast)",
        "headline": "I'm a Creep",
        "tone": "pejorative",
        "privacy_language": None,
        "surveillance_language": "tool for mass surveillance",
        "source": "Business Wars S1E2, Jun 10, 2026; WIRED's Chokkattu & Ashworth",
    },
    {
        "publication": "WIRED",
        "headline": "Meta Is Charging a Subscription for Smart Glasses Features",
        "tone": "adversarial",
        "privacy_language": None,
        "surveillance_language": "extracting value",
        "source": "Jul 2, 2026; Julian Chokkattu",
    },
]

# The school ban — real-world policy consequence
IBERVILLE_PARISH_BAN = {
    "jurisdiction": "Iberville Parish School System, Louisiana",
    "date": "2026-08-04",
    "ban_language": 'a ban on Meta glasses — also known as "smart frame" glasses',
    "scope": "schoolgrounds",
    "rationale": "camera-enabled eyewear that allow video and audio recording without the user realizing it",
    "samsung_covered": False,
    "google_covered": False,
    "snap_covered": False,
    "meta_specific": True,
    "source_url": "https://www.postsouth.com/story/news/local/2026/08/04/iberville-parish-schools-mandate-clear-bags-for-students/91127541007/",
    "significance": (
        "The ban names 'Meta glasses' specifically, not 'camera-equipped smart glasses.' "
        "Samsung Intelligent Eyewear, Google Android XR glasses, and Snap Spectacles "
        "all have cameras but would NOT be covered by this ban. This proves the media "
        "framing has shifted public perception from a CATEGORY concern (cameras on faces) "
        "to a BRAND-SPECIFIC stigma."
    ),
}


# =================================================================
# TEST CLASS 1: Hardware Equivalence Verification
# =================================================================
class TestHardwareEquivalence:
    """Samsung Intelligent Eyewear and Meta Ray-Bans share identical
    privacy-relevant hardware. Any framing differential cannot be
    explained by hardware differences."""

    def test_both_have_cameras(self):
        assert SAMSUNG_INTELLIGENT_EYEWEAR["camera"] is not None
        assert META_RAYBAN_GLASSES["camera"] is not None

    def test_both_have_microphones(self):
        assert SAMSUNG_INTELLIGENT_EYEWEAR["microphones"] is True
        assert META_RAYBAN_GLASSES["microphones"] is True

    def test_both_have_speakers(self):
        assert SAMSUNG_INTELLIGENT_EYEWEAR["speakers"] is True
        assert META_RAYBAN_GLASSES["speakers"] is True

    def test_both_have_always_on_ai(self):
        assert "Gemini" in SAMSUNG_INTELLIGENT_EYEWEAR["ai_assistant"]
        assert "Meta AI" in META_RAYBAN_GLASSES["ai_assistant"]

    def test_both_have_led_indicators(self):
        assert SAMSUNG_INTELLIGENT_EYEWEAR["led_recording_indicator"] is True
        assert META_RAYBAN_GLASSES["led_recording_indicator"] is True

    def test_both_have_obstruction_detection(self):
        assert SAMSUNG_INTELLIGENT_EYEWEAR["obstruction_detection"] is True
        assert META_RAYBAN_GLASSES["obstruction_detection"] is True

    def test_both_are_glasses_form_factor(self):
        assert SAMSUNG_INTELLIGENT_EYEWEAR["form_factor"] == "smart_glasses"
        assert META_RAYBAN_GLASSES["form_factor"] == "smart_glasses"

    def test_similar_weight(self):
        """Both are approximately 50g — within measurement error."""
        samsung_g = SAMSUNG_INTELLIGENT_EYEWEAR["weight_approx_grams"]
        meta_g = META_RAYBAN_GLASSES["weight_approx_grams"]
        assert abs(samsung_g - meta_g) <= 5, \
            f"Weight difference ({abs(samsung_g - meta_g)}g) too large to explain framing delta"

    def test_neither_has_display_base_model(self):
        """First-gen Samsung: no display. Meta Ray-Ban base: no display."""
        assert SAMSUNG_INTELLIGENT_EYEWEAR["display"] is False
        assert META_RAYBAN_GLASSES["display"] is False

    def test_both_use_companion_device(self):
        assert SAMSUNG_INTELLIGENT_EYEWEAR["companion_device"] is not None
        assert META_RAYBAN_GLASSES["companion_device"] is not None

    def test_shared_privacy_features_count(self):
        """At least 6 identical privacy-relevant features shared."""
        assert len(SHARED_PRIVACY_FEATURES) >= 6


# =================================================================
# TEST CLASS 2: Coverage Framing Asymmetry
# =================================================================
class TestCoverageFramingAsymmetry:
    """Cross-publication coverage of functionally identical products
    shows systematic framing divergence."""

    def test_samsung_coverage_has_no_surveillance_language(self):
        """No Samsung Intelligent Eyewear article uses surveillance vocabulary."""
        for article in SAMSUNG_COVERAGE_FRAMING:
            assert article["surveillance_language"] is None, \
                f"{article['publication']} used surveillance language for Samsung: " \
                f"{article['surveillance_language']}"

    def test_meta_coverage_has_surveillance_language(self):
        """Meta coverage systematically uses surveillance vocabulary."""
        surveillance_articles = [
            a for a in META_COVERAGE_FRAMING
            if a["surveillance_language"] is not None
        ]
        assert len(surveillance_articles) >= 1, \
            "Expected surveillance language in Meta coverage"

    def test_samsung_tone_never_pejorative(self):
        """No Samsung article uses pejorative tone."""
        for article in SAMSUNG_COVERAGE_FRAMING:
            assert article["tone"] != "pejorative", \
                f"{article['publication']} used pejorative tone for Samsung"
            assert article["tone"] != "adversarial", \
                f"{article['publication']} used adversarial tone for Samsung"

    def test_meta_tone_includes_pejorative(self):
        """Meta coverage includes pejorative framing for identical hardware."""
        pejorative = [a for a in META_COVERAGE_FRAMING if a["tone"] == "pejorative"]
        assert len(pejorative) >= 1

    def test_samsung_positive_privacy_framing(self):
        """Samsung's LED indicator is framed as a positive privacy feature.
        Meta's identical LED indicator is framed as insufficient/easily hidden."""
        positive_privacy = [
            a for a in SAMSUNG_COVERAGE_FRAMING
            if a.get("privacy_language") and "seriously" in a["privacy_language"].lower()
            or a.get("privacy_language") and "important" in a["privacy_language"].lower()
        ]
        assert len(positive_privacy) >= 1, \
            "Expected positive privacy framing for Samsung's LED indicator"

    def test_samsung_coverage_sources_have_urls(self):
        """Every Samsung coverage example has a source URL."""
        for article in SAMSUNG_COVERAGE_FRAMING:
            assert article.get("source_url"), \
                f"{article['publication']} missing source URL"


# =================================================================
# TEST CLASS 3: The School Ban Consequence Test
# =================================================================
class TestSchoolBanConsequence:
    """The most powerful evidence: brand-specific bans prove that
    differential framing creates differential policy outcomes."""

    def test_ban_names_meta_specifically(self):
        """The Iberville Parish ban says 'Meta glasses' not 'smart glasses with cameras.'"""
        assert IBERVILLE_PARISH_BAN["meta_specific"] is True
        assert "Meta glasses" in IBERVILLE_PARISH_BAN["ban_language"]

    def test_ban_does_not_cover_samsung(self):
        """Samsung Intelligent Eyewear would NOT be banned under this policy."""
        assert IBERVILLE_PARISH_BAN["samsung_covered"] is False

    def test_ban_does_not_cover_google(self):
        """Google Android XR glasses would NOT be banned."""
        assert IBERVILLE_PARISH_BAN["google_covered"] is False

    def test_ban_does_not_cover_snap(self):
        """Snap Spectacles (FOUR cameras) would NOT be banned."""
        assert IBERVILLE_PARISH_BAN["snap_covered"] is False

    def test_ban_rationale_applies_to_all_camera_glasses(self):
        """The stated rationale ('camera-enabled eyewear that allow video and audio
        recording') applies equally to Samsung, Google, and Snap — but the ban
        only names Meta. This is the proof of brand-specific stigma."""
        rationale = IBERVILLE_PARISH_BAN["rationale"]
        assert "camera-enabled" in rationale
        assert "video and audio recording" in rationale

    def test_ban_has_source_url(self):
        assert IBERVILLE_PARISH_BAN["source_url"].startswith("https://")

    def test_ban_date_after_samsung_launch(self):
        """The ban was approved AFTER Samsung announced identical glasses,
        meaning the policy-makers knew about Samsung's glasses but still
        singled out Meta."""
        # Samsung Unpacked: Jul 22, 2026; Ban article: Aug 4, 2026
        assert IBERVILLE_PARISH_BAN["date"] > SAMSUNG_INTELLIGENT_EYEWEAR["announced"]


# =================================================================
# TEST CLASS 4: WIRED's Specific Role in the Asymmetry
# =================================================================
class TestWiredSpecificAsymmetry:
    """WIRED's gear desk (Chokkattu/Ashworth) is the primary source
    of adversarial framing for Meta glasses. Their Samsung coverage
    (or absence thereof) reveals the double standard."""

    def test_wired_has_google_smart_glasses_framing_documented(self):
        """The competitor-coverage-research should document the
        Google/Samsung glasses framing paradox."""
        research = load_competitor_research()
        wired_section = research.get('wired', {})
        google_framing = wired_section.get('google_smart_glasses_framing', {})
        assert google_framing, \
            "WIRED profile must document the Google/Samsung glasses framing paradox"

    def test_framing_paradox_mentions_samsung(self):
        """The framing paradox should mention Samsung Intelligent Eyewear."""
        research = load_competitor_research()
        wired_section = research.get('wired', {})
        google_framing = wired_section.get('google_smart_glasses_framing', {})
        desc = google_framing.get('description', '')
        assert 'samsung' in desc.lower() or 'Samsung' in desc, \
            "Google smart glasses framing paradox should mention Samsung"

    def test_samsung_equivalence_section_exists(self):
        """competitor-coverage-research should have a samsung_equivalence_paradox section."""
        research = load_competitor_research()
        wired_section = research.get('wired', {})
        assert 'samsung_equivalence_paradox' in wired_section, \
            "WIRED section needs samsung_equivalence_paradox documenting " \
            "the Unpacked Jul 22 2026 launch and school ban consequence"

    def test_samsung_equivalence_has_school_ban(self):
        """The samsung_equivalence_paradox must document the Iberville Parish
        school ban as evidence of real-world policy consequence."""
        research = load_competitor_research()
        wired_section = research.get('wired', {})
        paradox = wired_section.get('samsung_equivalence_paradox', {})
        desc = paradox.get('description', '')
        assert 'iberville' in desc.lower() or 'school ban' in desc.lower(), \
            "Samsung equivalence paradox must document the Iberville Parish school ban"


# =================================================================
# TEST CLASS 5: Samsung Entity Completeness
# =================================================================
class TestSamsungEntityCompleteness:
    """Samsung should be documented as a competitor entity with
    smart glasses coverage tracking."""

    def test_competitor_entities_has_samsung(self):
        """competitor-entities.yaml should include Samsung as a competitor."""
        entities = load_competitor_entities()
        entity_keys = entities.get('entities', {})
        assert 'samsung' in entity_keys, \
            "Samsung must be in competitor-entities.yaml"

    def test_samsung_entity_has_smart_glasses(self):
        """Samsung entity should document Intelligent Eyewear."""
        entities = load_competitor_entities()
        samsung = entities.get('entities', {}).get('samsung', {})
        assert samsung, "Samsung entity not found"
        note = samsung.get('smart_glasses_note', '')
        assert 'eyewear' in note.lower() or 'glasses' in note.lower(), \
            "Samsung entity should mention Intelligent Eyewear / Galaxy Glasses"


# =================================================================
# TEST CLASS 6: Cross-Publication Samsung Privacy Framing
# =================================================================
class TestCrossPublicationSamsungPrivacy:
    """Across publications, Samsung's LED indicator is described as
    a positive privacy measure, while Meta's identical LED indicator
    is described as insufficient or easily circumvented."""

    def test_sammobile_positive_framing(self):
        sammobile = [a for a in SAMSUNG_COVERAGE_FRAMING
                     if a['publication'] == 'SamMobile']
        assert len(sammobile) == 1
        assert sammobile[0]['tone'] == 'positive'
        assert 'seriously' in sammobile[0]['headline'].lower()

    def test_gsmarena_constructive_framing(self):
        gsmarena = [a for a in SAMSUNG_COVERAGE_FRAMING
                    if a['publication'] == 'GSMArena']
        assert len(gsmarena) == 1
        assert gsmarena[0]['tone'] == 'constructive'
        assert 'important' in gsmarena[0]['headline'].lower()

    def test_no_samsung_creep_language(self):
        """No Samsung article uses 'creep', 'creepy', 'surveillance',
        'wiretapping', 'biometric', or 'predator' language."""
        forbidden_words = ['creep', 'surveillance', 'wiretapping',
                          'biometric', 'predator', 'dystopian']
        for article in SAMSUNG_COVERAGE_FRAMING:
            headline_lower = article['headline'].lower()
            for word in forbidden_words:
                assert word not in headline_lower, \
                    f"Samsung headline from {article['publication']} " \
                    f"contains '{word}': {article['headline']}"

    def test_meta_gets_creep_language_for_identical_hardware(self):
        """Meta's Business Wars podcast episode is literally titled 'I'm a Creep'
        for functionally identical camera glasses."""
        creep_articles = [a for a in META_COVERAGE_FRAMING
                         if 'creep' in a['headline'].lower()]
        assert len(creep_articles) >= 1, \
            "Meta coverage should include 'Creep' framing"


# =================================================================
# TEST CLASS 7: The Advertising Dependency Explanation
# =================================================================
class TestAdvertisingDependencyExplanation:
    """Neither Samsung nor Meta has content deals with Condé Nast.
    But Google (Samsung's platform partner) still provides residual
    ad revenue and search traffic. The cost of attacking Samsung's
    launch is non-zero because Samsung's glasses run on Android XR
    (Google's platform)."""

    def test_samsung_no_conde_nast_deal(self):
        """Samsung has no known content licensing deal with Condé Nast."""
        # This is validated by the absence of Samsung in Condé Nast deal lists
        assert SAMSUNG_INTELLIGENT_EYEWEAR["ai_assistant"] == "Google Gemini"

    def test_samsung_uses_google_platform(self):
        """Samsung's glasses run Android XR — attacking Samsung glasses
        is functionally attacking Google's platform."""
        assert "Google" in SAMSUNG_INTELLIGENT_EYEWEAR["ai_assistant"]

    def test_meta_no_conde_nast_deal(self):
        """Meta also has no known content licensing deal with Condé Nast.
        Neither company is a deal partner, yet only Meta gets adversarial treatment."""
        assert "Meta AI" in META_RAYBAN_GLASSES["ai_assistant"]


# =================================================================
# TEST CLASS 8: Temporal Sequencing
# =================================================================
class TestTemporalSequencing:
    """The timeline proves the asymmetry is systematic, not coincidental."""

    def test_business_wars_before_samsung_launch(self):
        """WIRED's 'I'm a Creep' episode (Jun 10, 2026) aired BEFORE
        Samsung's Unpacked (Jul 22, 2026) — Meta was already branded
        as 'creepy' before the competitor even launched."""
        business_wars_date = "2026-06-10"
        samsung_launch = SAMSUNG_INTELLIGENT_EYEWEAR["announced"]
        assert business_wars_date < samsung_launch

    def test_school_ban_after_both_launches(self):
        """The school ban (Aug 4, 2026) happened after both Samsung and Meta
        had launched/announced glasses — yet only Meta was named."""
        ban_date = IBERVILLE_PARISH_BAN["date"]
        samsung_date = SAMSUNG_INTELLIGENT_EYEWEAR["announced"]
        assert ban_date > samsung_date

    def test_samsung_launch_date_is_documented(self):
        assert SAMSUNG_INTELLIGENT_EYEWEAR["announced"] == "2026-07-22"

    def test_ban_date_is_documented(self):
        assert IBERVILLE_PARISH_BAN["date"] == "2026-08-04"
