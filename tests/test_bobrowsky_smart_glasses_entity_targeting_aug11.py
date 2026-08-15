"""
Bobrowsky Smart Glasses Privacy Entity-Targeting Concentration — Type B Journalist (Aug 11, 2026)

Mechanism #49: Beat-Assignment Entity-Targeting Concentration

KEY FINDING: WSJ Meta beat reporter Meghan Bobrowsky published a deep privacy
investigation of Meta's smart glasses ("Meta Is Flooding the Market With
Smartglasses. Privacy Advocates Are Up in Arms," Jul 14, 2026) covering
NameTag facial recognition, LED disabling, constant-capture features, and
mood-tracking patents. Eight days later (Jul 22), Samsung unveiled Galaxy
Glasses at Galaxy Unpacked with IDENTICAL privacy-relevant hardware: same
Snapdragon AR1 Gen 1 chip, 12MP camera, LED recording indicator, and Google
Gemini AI visual processing. Bobrowsky has ZERO privacy investigations of
Samsung/Google Galaxy Glasses.

In the same 3-week window (Jun 26), WSJ COLUMNIST Christopher Mims published
"Smartglasses Are Inevitable" covering ALL companies (Meta, Samsung, Google,
Snap, Apple, Xreal) with consistent privacy framing — applying the SAME
privacy skepticism ("why should we be OK with everyone we meet pointing
internet-connected cameras at us?") to all cameras and praising Meta's design.

The Mims-Bobrowsky divergence at the SAME publication, on the SAME topic,
in the SAME 3-week window, isolates BEAT ASSIGNMENT as the mechanism.
Financial context: News Corp has BALANCED financial ties ($50M/yr Meta +
$50M/yr OpenAI), so the asymmetry is NOT financially driven — it is structural.

Sources:
  - WSJ: Bobrowsky "Meta Is Flooding the Market" (Jul 14, 2026)
    https://www.wsj.com/tech/ai/meta-is-flooding-the-market-with-smartglasses-privacy-advocates-are-up-in-arms-8fb71539
  - WSJ: Mims "Smartglasses Are Inevitable" (Jun 26, 2026)
    https://www.wsj.com/tech/ai/smart-glasses-market-meta-ai-8e6510b8
  - Wikipedia: Samsung Galaxy Glasses (LED anti-tamper, AR1 Gen 1)
    https://en.wikipedia.org/wiki/Samsung_Galaxy_Glasses
  - Samsung Newsroom: Galaxy Unpacked Jul 2026
    https://news.samsung.com/us/samsung-galaxy-ecosystem-everyday-eyewear
  - Talking Biz News: Bobrowsky assigned to Meta beat
    https://talkingbiznews.com/media-news/wsj-taps-bobrowsky-to-cover-meta/
  - Gizmodo: Samsung glasses hands-on (identical hardware)
    https://gizmodo.com/samsung-let-me-touch-its-warby-parker-x-gentle-monster-smart-glasses-but-not-wear-them-2000788835

Created: 2026-08-11
"""

import yaml
import os
import pytest
from pathlib import Path

PROFILES_DIR = Path(__file__).parent.parent / "profiles"


def load_yaml(name: str) -> dict:
    with open(PROFILES_DIR / name) as f:
        return yaml.safe_load(f)


# ===================================================================
# 1. MECHANISM #49 EXISTS IN COMPETITOR-COVERAGE-RESEARCH
# ===================================================================


class TestMechanism49InYAML:
    """Verify mechanism #49 is properly documented in competitor-coverage-research.yaml."""

    @pytest.fixture(scope="class")
    @classmethod
    def research(cls):
        return load_yaml("competitor-coverage-research.yaml")

    def test_mechanism_49_exists(self, research):
        cpf = research.get("cross_publication_findings", {})
        found = any(
            v.get("mechanism_id") == 49
            for v in cpf.values()
            if isinstance(v, dict)
        )
        assert found, "Mechanism #49 must exist in cross_publication_findings"

    def test_mechanism_49_key_name(self, research):
        cpf = research.get("cross_publication_findings", {})
        assert "bobrowsky_smart_glasses_privacy_entity_targeting" in cpf, \
            "Expected key 'bobrowsky_smart_glasses_privacy_entity_targeting'"

    def test_mechanism_49_has_finding_summary(self, research):
        m = research["cross_publication_findings"]["bobrowsky_smart_glasses_privacy_entity_targeting"]
        assert "finding_summary" in m, "Mechanism #49 must have finding_summary"
        assert "Bobrowsky" in m["finding_summary"]

    def test_mechanism_49_rotation_type_b(self, research):
        m = research["cross_publication_findings"]["bobrowsky_smart_glasses_privacy_entity_targeting"]
        assert m.get("rotation_type") == "B", "Mechanism #49 should be Type B (journalist tracking)"

    def test_mechanism_49_has_source_urls(self, research):
        m = research["cross_publication_findings"]["bobrowsky_smart_glasses_privacy_entity_targeting"]
        urls = m.get("source_urls", [])
        assert len(urls) >= 4, f"Expected >=4 source URLs, got {len(urls)}"

    def test_mechanism_49_has_confounding_factors(self, research):
        m = research["cross_publication_findings"]["bobrowsky_smart_glasses_privacy_entity_targeting"]
        factors = m.get("confounding_factors", [])
        assert len(factors) >= 5, f"Expected >=5 confounding factors, got {len(factors)}"


# ===================================================================
# 2. BOBROWSKY META ARTICLE DOCUMENTATION
# ===================================================================


class TestBobrowskyMetaArticle:
    """Verify the Meta 'flooding the market' article is fully documented."""

    @pytest.fixture(scope="class")
    @classmethod
    def mechanism(cls):
        data = load_yaml("competitor-coverage-research.yaml")
        return data["cross_publication_findings"]["bobrowsky_smart_glasses_privacy_entity_targeting"]

    def test_bobrowsky_article_has_url(self, mechanism):
        article = mechanism.get("bobrowsky_meta_article", {})
        assert "url" in article, "Bobrowsky article must have URL"
        assert "wsj.com" in article["url"]

    def test_bobrowsky_article_date(self, mechanism):
        article = mechanism.get("bobrowsky_meta_article", {})
        assert article.get("date") == "2026-07-14"

    def test_bobrowsky_article_has_investigation_topics(self, mechanism):
        article = mechanism.get("bobrowsky_meta_article", {})
        topics = article.get("investigation_topics", [])
        assert len(topics) >= 4, f"Expected >=4 investigation topics, got {len(topics)}"
        topic_str = " ".join(topics).lower()
        assert "nametag" in topic_str, "Must include NameTag"
        assert "led" in topic_str or "stealth" in topic_str, "Must include LED disabling"

    def test_bobrowsky_article_tone_adversarial(self, mechanism):
        article = mechanism.get("bobrowsky_meta_article", {})
        tone = article.get("tone", 0)
        assert tone < -0.3, f"Bobrowsky Meta article tone should be adversarial (<-0.3), got {tone}"

    def test_bobrowsky_article_has_loaded_language(self, mechanism):
        article = mechanism.get("bobrowsky_meta_article", {})
        loaded = article.get("loaded_language", [])
        assert len(loaded) >= 2, f"Expected >=2 loaded language terms, got {len(loaded)}"


# ===================================================================
# 3. MIMS BALANCED CONTROL ARTICLE
# ===================================================================


class TestMimsBalancedArticle:
    """Verify the Mims control article is documented with balanced framing."""

    @pytest.fixture(scope="class")
    @classmethod
    def mechanism(cls):
        data = load_yaml("competitor-coverage-research.yaml")
        return data["cross_publication_findings"]["bobrowsky_smart_glasses_privacy_entity_targeting"]

    def test_mims_article_exists(self, mechanism):
        assert "mims_balanced_article" in mechanism, "Mims balanced article must be documented"

    def test_mims_article_has_url(self, mechanism):
        article = mechanism.get("mims_balanced_article", {})
        assert "url" in article
        assert "wsj.com" in article["url"]

    def test_mims_article_date_precedes_bobrowsky(self, mechanism):
        mims_date = mechanism.get("mims_balanced_article", {}).get("date", "")
        bobrowsky_date = mechanism.get("bobrowsky_meta_article", {}).get("date", "")
        assert mims_date < bobrowsky_date, \
            f"Mims ({mims_date}) should precede Bobrowsky ({bobrowsky_date})"

    def test_mims_covers_multiple_entities(self, mechanism):
        article = mechanism.get("mims_balanced_article", {})
        entities = article.get("entities_covered", [])
        assert len(entities) >= 4, f"Mims should cover >=4 entities, got {len(entities)}"

    def test_mims_tone_near_neutral(self, mechanism):
        article = mechanism.get("mims_balanced_article", {})
        tone = article.get("tone", -1)
        assert -0.2 <= tone <= 0.2, f"Mims tone should be near-neutral, got {tone}"

    def test_mims_privacy_framing_applied_equally(self, mechanism):
        article = mechanism.get("mims_balanced_article", {})
        framing = article.get("privacy_framing", "")
        assert "ALL" in framing or "all" in framing.lower(), \
            "Mims privacy framing should apply to ALL camera glasses"


# ===================================================================
# 4. SAMSUNG HARDWARE PARITY
# ===================================================================


class TestSamsungHardwareParity:
    """Verify Samsung Galaxy Glasses have identical privacy-relevant hardware."""

    @pytest.fixture(scope="class")
    @classmethod
    def mechanism(cls):
        data = load_yaml("competitor-coverage-research.yaml")
        return data["cross_publication_findings"]["bobrowsky_smart_glasses_privacy_entity_targeting"]

    def test_samsung_parity_section_exists(self, mechanism):
        assert "samsung_hardware_parity" in mechanism, \
            "Samsung hardware parity comparison must be documented"

    def test_samsung_same_chip(self, mechanism):
        parity = mechanism.get("samsung_hardware_parity", {})
        chip = parity.get("chip", "").lower()
        assert "ar1 gen 1" in chip, "Samsung must use same Snapdragon AR1 Gen 1"

    def test_samsung_same_camera(self, mechanism):
        parity = mechanism.get("samsung_hardware_parity", {})
        camera = parity.get("camera", "").lower()
        assert "12mp" in camera, "Samsung must have 12MP camera"

    def test_samsung_led_indicator_documented(self, mechanism):
        parity = mechanism.get("samsung_hardware_parity", {})
        led = parity.get("led_indicator", "").lower()
        assert "led" in led, "Samsung LED recording indicator must be documented"
        assert "obscured" in led or "disabled" in led, \
            "Samsung LED anti-tamper behavior must be noted"

    def test_samsung_ai_processing(self, mechanism):
        parity = mechanism.get("samsung_hardware_parity", {})
        ai = parity.get("ai_processing", "").lower()
        assert "gemini" in ai, "Samsung Gemini AI processing must be documented"

    def test_samsung_has_source_url(self, mechanism):
        parity = mechanism.get("samsung_hardware_parity", {})
        assert "led_source_url" in parity, "Samsung parity must cite source"


# ===================================================================
# 5. BEAT ASSIGNMENT MECHANISM
# ===================================================================


class TestBeatAssignmentMechanism:
    """Verify the beat-assignment entity-targeting mechanism is documented."""

    @pytest.fixture(scope="class")
    @classmethod
    def mechanism(cls):
        data = load_yaml("competitor-coverage-research.yaml")
        return data["cross_publication_findings"]["bobrowsky_smart_glasses_privacy_entity_targeting"]

    def test_mechanism_name_includes_beat(self, mechanism):
        name = mechanism.get("mechanism_name", "").lower()
        assert "beat" in name or "entity-targeting" in name, \
            "Mechanism name should reference beat assignment or entity targeting"

    def test_mechanism_type_is_beat_assignment(self, mechanism):
        mech = mechanism.get("mechanism", "").lower()
        assert "beat" in mech or "entity" in mech, \
            f"Mechanism type should reference beat assignment, got '{mech}'"

    def test_bobrowsky_samsung_coverage_zero(self, mechanism):
        samsung = mechanism.get("bobrowsky_samsung_coverage", "")
        assert "zero" in samsung.lower() or "0" in samsung, \
            "Bobrowsky Samsung coverage must be documented as zero"

    def test_tone_delta_documented(self, mechanism):
        delta = mechanism.get("tone_delta_bobrowsky_mims", 0)
        assert delta >= 0.4, f"Tone delta should be >=0.4, got {delta}"


# ===================================================================
# 6. BOBROWSKY EXISTS IN NEWS CORP PROFILE
# ===================================================================


class TestBobrowskyInNewsCorp:
    """Cross-reference with existing news-corp.yaml journalist profiles."""

    @pytest.fixture(scope="class")
    @classmethod
    def news_corp(cls):
        return load_yaml("news-corp.yaml")

    def test_bobrowsky_profile_exists(self, news_corp):
        profiles = news_corp.get("journalist_profiles", [])
        names = [p.get("name", "") for p in profiles]
        assert "Meghan Bobrowsky" in names, "Bobrowsky must be in News Corp profiles"

    def test_bobrowsky_is_meta_beat(self, news_corp):
        profiles = news_corp.get("journalist_profiles", [])
        bobrowsky = next(
            (p for p in profiles if p.get("name") == "Meghan Bobrowsky"), None
        )
        assert bobrowsky is not None
        # Check current_role or explicitly_assigned_to_meta
        role = str(bobrowsky.get("current_role", "")).lower()
        assigned = bobrowsky.get("explicitly_assigned_to_meta", False)
        assert "meta" in role or assigned, \
            "Bobrowsky must be identified as Meta beat reporter"


# ===================================================================
# 7. MIMS EXISTS IN NEWS CORP PROFILE
# ===================================================================


class TestMimsInNewsCorp:
    """Cross-reference with existing news-corp.yaml Christopher Mims profile."""

    @pytest.fixture(scope="class")
    @classmethod
    def news_corp(cls):
        return load_yaml("news-corp.yaml")

    def test_mims_profile_exists(self, news_corp):
        profiles = news_corp.get("journalist_profiles", [])
        names = [p.get("name", "") for p in profiles]
        assert "Christopher Mims" in names, "Mims must be in News Corp profiles"


# ===================================================================
# 8. CROSS-VALIDATION WITH EXISTING MECHANISMS
# ===================================================================


class TestCrossValidation:
    """Verify mechanism #49 integrates with the broader mechanism taxonomy."""

    @pytest.fixture(scope="class")
    @classmethod
    def research(cls):
        return load_yaml("competitor-coverage-research.yaml")

    def test_mechanism_49_id_unique(self, research):
        cpf = research.get("cross_publication_findings", {})
        ids = [
            v.get("mechanism_id")
            for v in cpf.values()
            if isinstance(v, dict) and "mechanism_id" in v
        ]
        assert ids.count(49) == 1, f"Mechanism ID 49 should appear exactly once, found {ids.count(49)}"

    def test_mechanism_count_at_least_49(self, research):
        cpf = research.get("cross_publication_findings", {})
        ids = set(
            v.get("mechanism_id")
            for v in cpf.values()
            if isinstance(v, dict) and "mechanism_id" in v
        )
        assert max(ids) >= 49, f"Maximum mechanism ID should be >=49, got {max(ids)}"

    def test_test_file_count_at_least_304(self, research):
        """Test file count should have grown by 1."""
        test_dir = Path(__file__).parent
        test_files = list(test_dir.glob("test_*.py"))
        assert len(test_files) >= 304, \
            f"Expected >=304 test files, got {len(test_files)}"


# ===================================================================
# 9. REBUTTAL TO CONFOUNDS
# ===================================================================


class TestRebuttalDocumented:
    """Verify that the rebuttal section addresses the confounding factors."""

    @pytest.fixture(scope="class")
    @classmethod
    def mechanism(cls):
        data = load_yaml("competitor-coverage-research.yaml")
        return data["cross_publication_findings"]["bobrowsky_smart_glasses_privacy_entity_targeting"]

    def test_rebuttal_exists(self, mechanism):
        assert "rebuttal_to_confounds" in mechanism, \
            "Rebuttal to confounding factors must be documented"

    def test_rebuttal_mentions_prediction(self, mechanism):
        rebuttal = mechanism.get("rebuttal_to_confounds", "")
        assert "prediction" in rebuttal.lower() or "predict" in rebuttal.lower(), \
            "Rebuttal should make a testable prediction about Samsung coverage"

    def test_rebuttal_mentions_mims_control(self, mechanism):
        rebuttal = mechanism.get("rebuttal_to_confounds", "")
        assert "mims" in rebuttal.lower(), \
            "Rebuttal should reference Mims as a control comparison"
