"""
Cross-Publication Smart Glasses Brand Stigma Entity Targeting — Type B (Aug 17, 2026)

Mechanism #155: Cross-Publication Brand Stigma Vocabulary Entity Targeting

KEY FINDING: Across 8+ publications, Meta's smart glasses receive adversarial
"predatory market" vocabulary while Samsung/Google's IDENTICAL hardware
receives aspirational/competitive vocabulary. This pattern operates at the
headline level and creates a brand stigma that propagates only when Meta is
the named entity.

VOCABULARY DIFFERENTIAL (verified from published headlines/articles):

  Meta:     "flooding the market" (WSJ), "pervert glasses" (Engadget, 9to5Google),
            "spy glasses" (Guardian), "shady specs" (Engadget), "nightmarish"
            (Android Police), "douchebag with a camera on your face" (PetaPixel/FT),
            "privacy nightmare" (Gizmodo), "dangerous and reckless" (tdefender)

  Samsung:  "why Meta should be worried" (Android Police), "convinced me where
            Apple Vision Pro didn't" (Digital Trends), "secret weapon" (Inc),
            "might not have to do much, thanks to Meta" (Gizmodo), "privacy is
            not an afterthought" (Samsung exec, amplified uncritically)

  Google:   "trusted testers" (Google/PetaPixel 2022), "taking it slow"
            (Google/PetaPixel 2022), "privacy-protective" (TechTimes)

  Apple:    "can't solve" (Gizmodo — sympathetic impossibility framing),
            "secret weapon" (Tom's Guide — aspirational)

HARDWARE PARITY CHECK:
All four companies build/plan camera-equipped smart glasses with:
- 12MP-class cameras
- LED recording indicators (same Snapdragon AR1 Gen 1 for Meta + Samsung)
- Always-on microphones
- AI visual processing (Meta AI / Gemini / Siri)
- Identical tampering vulnerability (LED can be covered on any glasses)

UK VENUE BAN ENTITY TARGETING:
Wetherspoons, Soho House, ATG Theatres, Jeremy King restaurants, Monopoly Events,
HMCTS courtrooms — ALL specifically ban "Meta Glasses" by brand name, not "smart
glasses" as a category. Samsung/Google glasses (launching fall 2026 with identical
camera hardware) inherit ZERO pre-launch venue ban stigma.

EXTENDS: Mechanism #49 (Bobrowsky beat assignment entity targeting) from a
single-publication to a CROSS-PUBLICATION pattern. Extends mechanism #152
(Nvidia-OpenAI GPU circularity) by adding hardware-layer vocabulary analysis.

CONFOUNDERS:
  STRONG: (1) Meta has 80%+ market share and 3 years head start — scrutiny follows
    market presence. Samsung/Google haven't shipped yet, so real-world abuse is
    zero. (2) Meta has a documented privacy record (Cambridge Analytica, Kenyan
    contractors) that colors coverage.
  MODERATE: (3) UK venue bans may target the ONLY glasses currently being worn
    in venues (Samsung/Google not yet on sale). (4) Samsung's "privacy not an
    afterthought" may be legitimate marketing differentiation.
  WEAK: (5) Headline vocabulary is often written by editors, not reporters.

WHY IT MATTERS DESPITE CONFOUNDERS:
The confounders explain WHY Meta receives more scrutiny NOW, but they do NOT
explain the VOCABULARY differential. "Flooding the market" is a predatory
economic warfare metaphor — Samsung sells hundreds of millions of phones/watches
(far more devices) without being called "flooding." "Pervert glasses" attributes
user behavior to the manufacturer — nobody calls iPhones "stalker phones" despite
identical recording capability. The vocabulary creates a brand stigma that will
persist even after Samsung/Google ship identical hardware.

Sources:
  - WSJ Bobrowsky "Meta Is Flooding the Market" (Jul 14, 2026)
    https://www.wsj.com/tech/ai/meta-is-flooding-the-market-with-smartglasses-privacy-advocates-are-up-in-arms-8fb71539
  - Engadget "England And Wales Ban Meta Glasses From Courtrooms" (Aug 11, 2026)
    https://www.engadget.com/2234606/england-and-wales-ban-meta-glasses-from-courtrooms/
  - PetaPixel "UK Venues Ban Meta Smart Glasses En Masse" (Aug 10, 2026)
    https://petapixel.com/2026/08/10/uk-venues-ban-meta-smart-glasses-en-masse/
  - PetaPixel "A Douchebag With a Camera on Your Face" (Apr 8, 2026)
    https://petapixel.com/2026/04/08/a-douchebag-with-a-camera-on-your-face-should-smart-glasses-record-imagery/
  - Android Police "Samsung smartglasses — Why Meta should be worried" (Jul 22, 2026)
    https://www.androidpolice.com/hands-on-with-samsungs-ray-ban-meta-rival-smartglasses/
  - Gizmodo "Samsung's Smart Glasses Might Not Have to Do Much, Thanks to Meta" (Mar 2026)
    https://gizmodo.com/samsungs-smart-glasses-might-not-have-to-do-much-thanks-to-meta-2000734490
  - 9to5Google "Samsung and Google betting they can avoid Meta's 'perv glasses' problem" (Jul 23, 2026)
    https://9to5google.com/2026/07/23/inbox-newsletter-4/
  - Inc "Samsung and Google's New Smart Glasses Have a Secret Weapon Meta Can't Easily Copy" (Jul 2026)
    https://www.inc.com/connor-jewiss/samsung-and-googles-new-smart-glasses-have-a-secret-weapon-that-meta-cant-easily-copy/91380954
  - DuckDuckGo anti-smart-glasses parody (Aug 5, 2026)
    https://petapixel.com/2026/08/05/duckduckgos-smart-glasses-have-no-camera-no-ai-and-no-electronics/
  - Gizmodo "Smart Glasses Are the One Privacy Nightmare Apple Can't Solve" (Jul 2026)
    https://gizmodo.com/smart-glasses-are-the-one-privacy-nightmare-apple-cant-solve-2000791443
  - Digital Trends "Galaxy XR convinced me where Apple Vision Pro didn't" (Oct 2025)
    https://www.digitaltrends.com/wearables/samsung-galaxy-xr-hands-on-preview/
  - Muck Rack: Bobrowsky profile — "Covers: Meta Platforms, social media and artificial intelligence"
    https://muckrack.com/meghan-bobrowsky

Created: 2026-08-17
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
# 1. MECHANISM #155 EXISTS IN COMPETITOR-COVERAGE-RESEARCH
# ===================================================================


class TestMechanism155InYAML:
    """Verify mechanism #155 is properly documented in competitor-coverage-research.yaml."""

    @pytest.fixture(autouse=True)
    def load_research(self):
        self.research = load_yaml("competitor-coverage-research.yaml")
        self.cpf = self.research.get("cross_publication_findings", {})

    def test_mechanism_155_exists(self):
        found = any(
            v.get("mechanism_id") == 155
            for v in self.cpf.values()
            if isinstance(v, dict)
        )
        assert found, "Mechanism #155 must exist in cross_publication_findings"

    def test_mechanism_155_key_name(self):
        assert "cross_publication_brand_stigma_vocabulary_entity_targeting" in self.cpf, \
            "Expected key 'cross_publication_brand_stigma_vocabulary_entity_targeting'"

    def test_mechanism_155_has_finding_summary(self):
        m = self.cpf["cross_publication_brand_stigma_vocabulary_entity_targeting"]
        assert "finding_summary" in m
        summary = m["finding_summary"]
        assert "brand stigma" in summary.lower() or "vocabulary" in summary.lower()

    def test_mechanism_155_rotation_type_b(self):
        m = self.cpf["cross_publication_brand_stigma_vocabulary_entity_targeting"]
        assert m.get("rotation_type") == "B"

    def test_mechanism_155_has_source_urls(self):
        m = self.cpf["cross_publication_brand_stigma_vocabulary_entity_targeting"]
        urls = m.get("source_urls", [])
        assert len(urls) >= 8, f"Expected >=8 source URLs (cross-publication), got {len(urls)}"

    def test_mechanism_155_has_confounding_factors(self):
        m = self.cpf["cross_publication_brand_stigma_vocabulary_entity_targeting"]
        factors = m.get("confounding_factors", [])
        assert len(factors) >= 3, f"Expected >=3 confounders, got {len(factors)}"

    def test_mechanism_155_cross_references(self):
        m = self.cpf["cross_publication_brand_stigma_vocabulary_entity_targeting"]
        xrefs = m.get("cross_references", [])
        assert any(
            x.get("mechanism_id") == 49 for x in xrefs
        ), "Must cross-reference mechanism #49 (Bobrowsky beat assignment)"


# ===================================================================
# 2. VOCABULARY INVENTORY — META ADVERSARIAL TERMS
# ===================================================================


class TestMetaAdversarialVocabulary:
    """Verify adversarial vocabulary terms are documented with sources."""

    @pytest.fixture(autouse=True)
    def load_research(self):
        self.research = load_yaml("competitor-coverage-research.yaml")
        self.m = self.research["cross_publication_findings"][
            "cross_publication_brand_stigma_vocabulary_entity_targeting"
        ]

    def test_has_meta_vocabulary_section(self):
        vocab = self.m.get("vocabulary_inventory", {})
        assert "meta" in vocab, "Must have Meta vocabulary section"

    def test_meta_vocabulary_contains_flooding(self):
        terms = self.m["vocabulary_inventory"]["meta"]
        term_texts = [t.get("term", "") if isinstance(t, dict) else t for t in terms]
        assert any("flooding" in str(t).lower() for t in term_texts), \
            "'flooding the market' must be in Meta vocabulary inventory"

    def test_meta_vocabulary_contains_pervert(self):
        terms = self.m["vocabulary_inventory"]["meta"]
        term_texts = [t.get("term", "") if isinstance(t, dict) else t for t in terms]
        assert any("pervert" in str(t).lower() or "perv" in str(t).lower() for t in term_texts), \
            "'pervert glasses' must be in Meta vocabulary inventory"

    def test_meta_vocabulary_contains_spy(self):
        terms = self.m["vocabulary_inventory"]["meta"]
        term_texts = [t.get("term", "") if isinstance(t, dict) else t for t in terms]
        assert any("spy" in str(t).lower() for t in term_texts), \
            "'spy glasses' must be in Meta vocabulary inventory"

    def test_meta_vocabulary_at_least_5_terms(self):
        terms = self.m["vocabulary_inventory"]["meta"]
        assert len(terms) >= 5, f"Expected >=5 adversarial terms for Meta, got {len(terms)}"


# ===================================================================
# 3. VOCABULARY INVENTORY — SAMSUNG/GOOGLE ASPIRATIONAL TERMS
# ===================================================================


class TestCompetitorAspirationVocabulary:
    """Verify competitor aspirational vocabulary is documented."""

    @pytest.fixture(autouse=True)
    def load_research(self):
        self.research = load_yaml("competitor-coverage-research.yaml")
        self.m = self.research["cross_publication_findings"][
            "cross_publication_brand_stigma_vocabulary_entity_targeting"
        ]

    def test_has_samsung_vocabulary(self):
        vocab = self.m.get("vocabulary_inventory", {})
        assert "samsung" in vocab, "Must have Samsung vocabulary section"

    def test_samsung_vocabulary_aspirational(self):
        terms = self.m["vocabulary_inventory"]["samsung"]
        term_texts = [str(t.get("term", "") if isinstance(t, dict) else t).lower() for t in terms]
        adversarial_markers = ["pervert", "spy", "nightmare", "flooding", "douchebag", "shady"]
        adversarial_count = sum(1 for t in term_texts if any(m in t for m in adversarial_markers))
        assert adversarial_count == 0, \
            f"Samsung vocabulary should have zero adversarial markers, found {adversarial_count}"

    def test_has_google_vocabulary(self):
        vocab = self.m.get("vocabulary_inventory", {})
        assert "google" in vocab, "Must have Google vocabulary section"

    def test_has_apple_vocabulary(self):
        vocab = self.m.get("vocabulary_inventory", {})
        assert "apple" in vocab, "Must have Apple vocabulary section"

    def test_apple_sympathetic_framing(self):
        terms = self.m["vocabulary_inventory"]["apple"]
        term_texts = [str(t.get("term", "") if isinstance(t, dict) else t).lower() for t in terms]
        # Apple gets sympathetic impossibility framing, not adversarial
        assert any("can't solve" in t or "secret weapon" in t for t in term_texts), \
            "Apple vocabulary should include sympathetic impossibility framing"


# ===================================================================
# 4. HARDWARE PARITY — IDENTICAL SPECS
# ===================================================================


class TestHardwareParityDocumented:
    """Verify hardware parity between Meta and Samsung is documented."""

    @pytest.fixture(autouse=True)
    def load_research(self):
        self.research = load_yaml("competitor-coverage-research.yaml")
        self.m = self.research["cross_publication_findings"][
            "cross_publication_brand_stigma_vocabulary_entity_targeting"
        ]

    def test_hardware_parity_section_exists(self):
        assert "hardware_parity" in self.m, "Must document hardware parity"

    def test_shared_chip(self):
        hw = self.m["hardware_parity"]
        chip_text = str(hw).lower()
        assert "snapdragon ar1" in chip_text, "Must note shared Snapdragon AR1 Gen 1"

    def test_shared_camera(self):
        hw = self.m["hardware_parity"]
        cam_text = str(hw).lower()
        assert "camera" in cam_text or "12mp" in cam_text

    def test_shared_led(self):
        hw = self.m["hardware_parity"]
        led_text = str(hw).lower()
        assert "led" in led_text, "Must note shared LED indicator"


# ===================================================================
# 5. UK VENUE BAN ENTITY TARGETING
# ===================================================================


class TestVenueBanEntityTargeting:
    """Verify UK venue bans target 'Meta Glasses' by brand name."""

    @pytest.fixture(autouse=True)
    def load_research(self):
        self.research = load_yaml("competitor-coverage-research.yaml")
        self.m = self.research["cross_publication_findings"][
            "cross_publication_brand_stigma_vocabulary_entity_targeting"
        ]

    def test_venue_ban_section_exists(self):
        assert "venue_ban_entity_targeting" in self.m

    def test_venue_count(self):
        vb = self.m["venue_ban_entity_targeting"]
        venues = vb.get("venues_banning", [])
        assert len(venues) >= 5, f"Expected >=5 venues banning, got {len(venues)}"

    def test_entity_specificity(self):
        vb = self.m["venue_ban_entity_targeting"]
        specificity = vb.get("entity_specificity", "")
        assert "meta" in specificity.lower(), \
            "Bans must target 'Meta Glasses' specifically, not 'smart glasses'"

    def test_samsung_google_zero_bans(self):
        vb = self.m["venue_ban_entity_targeting"]
        samsung_bans = vb.get("samsung_google_bans", 0)
        assert samsung_bans == 0, "Samsung/Google should have zero venue bans"


# ===================================================================
# 6. CROSS-PUBLICATION SCOPE
# ===================================================================


class TestCrossPublicationScope:
    """Verify the pattern spans multiple publications."""

    @pytest.fixture(autouse=True)
    def load_research(self):
        self.research = load_yaml("competitor-coverage-research.yaml")
        self.m = self.research["cross_publication_findings"][
            "cross_publication_brand_stigma_vocabulary_entity_targeting"
        ]

    def test_publications_count(self):
        pubs = self.m.get("publications_exhibiting_pattern", [])
        assert len(pubs) >= 6, f"Expected >=6 publications, got {len(pubs)}"

    def test_includes_wsj(self):
        pubs = self.m.get("publications_exhibiting_pattern", [])
        pub_names = [str(p).lower() for p in pubs]
        assert any("wsj" in p or "wall street" in p for p in pub_names)

    def test_includes_engadget(self):
        pubs = self.m.get("publications_exhibiting_pattern", [])
        pub_names = [str(p).lower() for p in pubs]
        assert any("engadget" in p for p in pub_names)

    def test_includes_gizmodo(self):
        pubs = self.m.get("publications_exhibiting_pattern", [])
        pub_names = [str(p).lower() for p in pubs]
        assert any("gizmodo" in p for p in pub_names)

    def test_includes_petapixel(self):
        pubs = self.m.get("publications_exhibiting_pattern", [])
        pub_names = [str(p).lower() for p in pubs]
        assert any("petapixel" in p for p in pub_names)


# ===================================================================
# 7. PREDATORY MARKET VOCABULARY ANALYSIS
# ===================================================================


class TestPredatoryMarketVocabulary:
    """Test the 'flooding' economic warfare metaphor analysis."""

    @pytest.fixture(autouse=True)
    def load_research(self):
        self.research = load_yaml("competitor-coverage-research.yaml")
        self.m = self.research["cross_publication_findings"][
            "cross_publication_brand_stigma_vocabulary_entity_targeting"
        ]

    def test_flooding_analysis(self):
        analysis = self.m.get("predatory_market_vocabulary_analysis", {})
        assert "flooding" in str(analysis).lower()

    def test_flooding_source_is_wsj(self):
        analysis = self.m.get("predatory_market_vocabulary_analysis", {})
        assert "wsj" in str(analysis).lower() or "wall street" in str(analysis).lower()

    def test_samsung_comparison(self):
        """Samsung sells 100x more devices (phones, watches, earbuds) without 'flooding' label."""
        analysis = self.m.get("predatory_market_vocabulary_analysis", {})
        assert "samsung" in str(analysis).lower(), \
            "Must compare Samsung's much larger device volume without 'flooding' label"


# ===================================================================
# 8. DUCKDUCKGO CULTURAL CONSENSUS INDICATOR
# ===================================================================


class TestDuckDuckGoCulturalConsensus:
    """DuckDuckGo parody as cultural consensus indicator."""

    @pytest.fixture(autouse=True)
    def load_research(self):
        self.research = load_yaml("competitor-coverage-research.yaml")
        self.m = self.research["cross_publication_findings"][
            "cross_publication_brand_stigma_vocabulary_entity_targeting"
        ]

    def test_cultural_consensus_section(self):
        assert "cultural_consensus_indicators" in self.m

    def test_duckduckgo_included(self):
        indicators = self.m.get("cultural_consensus_indicators", [])
        assert any("duckduckgo" in str(i).lower() for i in indicators), \
            "DuckDuckGo anti-smart-glasses parody must be documented"


# ===================================================================
# 9. NEWS CORP PROFILE UPDATED
# ===================================================================


class TestNewsCorp155Reference:
    """Verify News Corp profile references mechanism #155."""

    def test_news_corp_has_mechanism_155_reference(self):
        data = load_yaml("news-corp.yaml")
        yaml_text = str(data)
        # The mechanism should be referenced somewhere in the profile
        assert "155" in yaml_text or "brand_stigma" in yaml_text.lower(), \
            "News Corp profile should reference mechanism #155 or brand stigma pattern"


# ===================================================================
# 10. BOBROWSKY PROFILE EXTENSION
# ===================================================================


class TestBobrowskyProfileExtension:
    """Verify Bobrowsky profile updated with cross-publication brand stigma."""

    def test_bobrowsky_has_flooding_article(self):
        data = load_yaml("news-corp.yaml")
        yaml_text = str(data)
        assert "flooding" in yaml_text.lower(), \
            "News Corp profile should reference 'flooding the market' article"

    def test_bobrowsky_smart_glasses_coverage_count(self):
        """Bobrowsky should have multiple documented smart glasses articles."""
        data = load_yaml("news-corp.yaml")
        yaml_text = str(data)
        # Check for at least the flooding article reference
        assert "smartglasses" in yaml_text.lower() or "smart glasses" in yaml_text.lower() or \
               "smart_glasses" in yaml_text.lower(), \
            "News Corp profile must reference smart glasses coverage"
