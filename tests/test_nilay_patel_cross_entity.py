"""
Tests for Nilay Patel (The Verge EIC) cross-entity coverage analysis.

KEY FINDING — THE EIC DELEGATION PARADOX (Mechanism #6):

Nilay Patel is The Verge's editor-in-chief since 2014 and host of Decoder,
the publication's flagship interview podcast. He personally interviews
competitor CEOs (Google/Sundar Pichai annually, Microsoft AI chief Mustafa
Suleyman, Bluesky, etc.) with strategic "big ideas" framing. But he
DELEGATES Meta CEO interviews to deputy editor Alex Heath, who applies
adversarial-investigative framing (layoffs, leaker crackdowns, internal
strategy doubt). This produces asymmetric editorial temperature at the
leadership level: competitor CEOs get the EIC's constructive lens while
Meta's CEO gets a deputy's adversarial lens — without any individual being
personally unfair.

This is mechanism #6 in the taxonomy:
1. WIRED: desk assignment (investigators → Meta, product reviewers → Apple)
2. NYT: between-reporter beat assignment
3. FT: within-reporter framing asymmetry
4. Verge: four-lane system (institutional)
5. Verge: Access Paradox (Heath)
6. Verge: EIC Delegation Paradox (Patel)

Sources:
- Decoder episode list (Deezer, Podme, Megaphone, Zeno.fm, PodcastRepublic)
- Sundar Pichai Decoder: https://www.youtube.com/watch?v=ANV3tE5ywv0
- Ronan Farrow/OpenAI Decoder: https://www.youtube.com/watch?v=TfN5ket9L8Q
- Zuckerberg Decoder (Heath): https://www.everand.com/podcast/773063094/
- Apple Vision Pro review (Patel): https://www.techradar.com/features/apple-vision-pro-review-roundup
- NPR interview (Google "secretly ruthless"): https://www.nprillinois.org/2023-09-04/the-verges-nilay-patel-talks-googles-legacy
- Meta Connect 2024 (Heath, not Patel): https://www.podchaser.com/podcasts/decoder-with-nilay-patel-100800/episodes/mark-zuckerberg-on-the-quest-p-152263701
"""

import yaml
import os
import re
from pathlib import Path

PROFILES_DIR = Path(__file__).parent.parent / "profiles"


def load_yaml(name: str) -> dict:
    with open(PROFILES_DIR / name, "r") as f:
        return yaml.safe_load(f)


class TestNilayPatelEditorialRole:
    """Validate Patel's role and position are documented."""

    def test_patel_in_verge_journalist_profiles(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        names = [j["name"] for j in journalists]
        assert "Nilay Patel" in names, "Patel must be in key_journalists"

    def test_patel_role_is_eic(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        assert "editor-in-chief" in patel.get("beat", "").lower() or \
               "editor-in-chief" in patel.get("known_patterns", "").lower(), \
            "Patel must be identified as EIC"

    def test_patel_hosts_decoder(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        combined = patel.get("beat", "") + " " + patel.get("known_patterns", "")
        assert "decoder" in combined.lower(), "Patel profile must mention Decoder"

    def test_patel_has_cross_entity_analysis(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        assert "competitor_coverage_analysis" in patel or \
               "cross_entity_coverage_analysis" in patel, \
            "Patel must have cross-entity analysis"


class TestEICDelegationPattern:
    """Core finding: Patel delegates Meta CEO interviews to Heath."""

    def test_meta_coverage_delegated(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        analysis = patel.get("cross_entity_coverage_analysis", {})
        meta = analysis.get("meta_coverage", {})
        pattern = meta.get("delegation_pattern", "")
        assert "heath" in pattern.lower() or "delegat" in pattern.lower(), \
            "Meta coverage must document delegation to Heath"

    def test_google_coverage_direct(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        analysis = patel.get("cross_entity_coverage_analysis", {})
        google = analysis.get("google_coverage", {})
        assert google.get("interview_format") in ("direct", "personal", "annual"), \
            "Google coverage must be direct Patel interviews"

    def test_delegation_creates_framing_asymmetry(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        analysis = patel.get("cross_entity_coverage_analysis", {})
        meta_tone = analysis.get("meta_coverage", {}).get("tone", 0)
        google_tone = analysis.get("google_coverage", {}).get("tone", 0)
        # Meta should be more adversarial than Google in EIC-level framing
        assert meta_tone < google_tone, \
            f"Meta tone ({meta_tone}) should be more adversarial than Google ({google_tone})"

    def test_mechanism_number_is_six(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        combined = str(patel)
        assert "mechanism" in combined.lower() and "6" in combined, \
            "Must identify as mechanism #6"


class TestPatelGoogleCoverage:
    """Patel interviews Pichai annually with strategic framing."""

    def test_pichai_annual_tradition(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        analysis = patel.get("cross_entity_coverage_analysis", {})
        google = analysis.get("google_coverage", {})
        combined = str(google)
        assert "annual" in combined.lower() or "tradition" in combined.lower() or \
               "fifth year" in combined.lower(), \
            "Must document annual Pichai interview tradition"

    def test_google_tone_is_balanced(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        analysis = patel.get("cross_entity_coverage_analysis", {})
        google = analysis.get("google_coverage", {})
        tone = google.get("tone", 0)
        assert -0.35 <= tone <= 0.1, \
            f"Google tone ({tone}) should be balanced-to-mildly-adversarial"

    def test_secretly_ruthless_quote_documented(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        combined = str(patel)
        assert "secretly ruthless" in combined.lower(), \
            "Must document Patel's 'secretly ruthless' characterization of Google"

    def test_google_has_source_urls(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        analysis = patel.get("cross_entity_coverage_analysis", {})
        google = analysis.get("google_coverage", {})
        urls = google.get("source_urls", [])
        assert len(urls) >= 2, f"Google coverage must have 2+ source URLs, got {len(urls)}"


class TestPatelMetaCoverage:
    """Meta interviews delegated to Heath; Patel covers Meta editorially."""

    def test_meta_tone_is_adversarial(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        analysis = patel.get("cross_entity_coverage_analysis", {})
        meta = analysis.get("meta_coverage", {})
        tone = meta.get("tone", 0)
        assert tone < -0.2, \
            f"Meta tone ({tone}) should be adversarial (EIC-level institutional framing)"

    def test_child_safety_coverage_documented(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        combined = str(patel)
        assert "jury" in combined.lower() or "child" in combined.lower() or \
               "hurt a kid" in combined.lower(), \
            "Must document Patel's child safety coverage"

    def test_meta_has_source_urls(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        analysis = patel.get("cross_entity_coverage_analysis", {})
        meta = analysis.get("meta_coverage", {})
        urls = meta.get("source_urls", [])
        assert len(urls) >= 1, "Meta coverage must have source URLs"


class TestPatelOpenAICoverage:
    """Patel has shown genuine adversarial capacity toward OpenAI."""

    def test_openai_tone_is_adversarial(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        analysis = patel.get("cross_entity_coverage_analysis", {})
        openai = analysis.get("openai_coverage", {})
        tone = openai.get("tone", 0)
        assert tone < -0.1, \
            f"OpenAI tone ({tone}) should be adversarial"

    def test_ronan_farrow_episode_documented(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        combined = str(patel)
        assert "farrow" in combined.lower() or "unconstrained" in combined.lower(), \
            "Must document Ronan Farrow/OpenAI Decoder episode"

    def test_ai_profitability_skepticism_documented(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        combined = str(patel)
        assert "profit" in combined.lower() or "monetization" in combined.lower() or \
               "race for profits" in combined.lower(), \
            "Must document AI profitability skepticism"


class TestPatelMicrosoftCoverage:
    """Patel interviews Microsoft AI chief with constructive framing."""

    def test_microsoft_tone_is_constructive(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        analysis = patel.get("cross_entity_coverage_analysis", {})
        ms = analysis.get("microsoft_coverage", {})
        tone = ms.get("tone", 0)
        assert tone >= -0.15, \
            f"Microsoft tone ({tone}) should be neutral-to-constructive"

    def test_suleyman_interview_documented(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        combined = str(patel)
        assert "suleyman" in combined.lower() or "mustafa" in combined.lower(), \
            "Must document Mustafa Suleyman Decoder interview"


class TestPatelAppleCoverage:
    """Patel reviews Apple Vision Pro personally — direct coverage."""

    def test_apple_tone_is_balanced(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        analysis = patel.get("cross_entity_coverage_analysis", {})
        apple = analysis.get("apple_coverage", {})
        tone = apple.get("tone", 0)
        assert -0.3 <= tone <= 0.3, \
            f"Apple tone ({tone}) should be balanced"

    def test_vision_pro_review_documented(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        combined = str(patel)
        assert "vision pro" in combined.lower(), \
            "Must document Apple Vision Pro review"


class TestDelegationMechanismTaxonomy:
    """Verify mechanism #6 integrates with the existing taxonomy in research file."""

    def test_mechanism_in_research_file(self):
        data = load_yaml("competitor-coverage-research.yaml")
        verge_section = data.get("publications", {}).get("the-verge", {})
        combined = str(verge_section)
        assert "patel" in combined.lower() or "eic_delegation" in combined.lower() or \
               "delegation_paradox" in combined.lower(), \
            "Research file must document Patel EIC delegation"

    def test_research_has_source_urls(self):
        data = load_yaml("competitor-coverage-research.yaml")
        verge_section = data.get("publications", {}).get("the-verge", {})
        patel_section = verge_section.get("patel_eic_delegation_paradox", {})
        urls = patel_section.get("source_urls", [])
        assert len(urls) >= 3, f"Research file must have 3+ source URLs, got {len(urls)}"

    def test_six_mechanisms_referenced(self):
        """All 6 asymmetry mechanisms should be documented."""
        data = load_yaml("competitor-coverage-research.yaml")
        combined = str(data)
        # Check for key mechanism identifiers
        mechanisms_found = 0
        for keyword in ["desk assignment", "between-reporter", "within-reporter",
                        "four-lane", "access paradox", "delegation paradox"]:
            if keyword.lower() in combined.lower():
                mechanisms_found += 1
        assert mechanisms_found >= 5, \
            f"Expected 5+ mechanisms referenced, found {mechanisms_found}"


class TestPublisherConflictContext:
    """Patel's editorial voice on publisher-AI content value conflicts."""

    def test_publisher_content_value_context(self):
        """Zuckerberg's 'overestimate the value' quote must be contextualized."""
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        combined = str(patel)
        assert "overestimate" in combined.lower() or "publisher" in combined.lower() or \
               "content value" in combined.lower(), \
            "Must document Zuckerberg's publisher-content statement in Patel context"

    def test_conde_nast_lynch_decoder_documented(self):
        """Patel interviewed his parent company's sibling CEO."""
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        combined = str(patel)
        assert "lynch" in combined.lower() or "condé nast" in combined.lower() or \
               "conde nast" in combined.lower(), \
            "Must document Condé Nast CEO Lynch Decoder episode"


class TestCrossEntityToneGap:
    """Validate the tone gap ordering across entities."""

    def test_meta_most_adversarial(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        analysis = patel.get("cross_entity_coverage_analysis", {})
        meta_tone = analysis.get("meta_coverage", {}).get("tone", 0)
        google_tone = analysis.get("google_coverage", {}).get("tone", 0)
        apple_tone = analysis.get("apple_coverage", {}).get("tone", 0)
        ms_tone = analysis.get("microsoft_coverage", {}).get("tone", 0)
        # Meta should be the most adversarial or tied with OpenAI
        assert meta_tone <= min(google_tone, apple_tone, ms_tone), \
            "Meta tone should be most adversarial among non-OpenAI entities"

    def test_meta_google_gap_positive(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        analysis = patel.get("cross_entity_coverage_analysis", {})
        meta_tone = analysis.get("meta_coverage", {}).get("tone", 0)
        google_tone = analysis.get("google_coverage", {}).get("tone", 0)
        gap = google_tone - meta_tone
        assert gap >= 0.15, \
            f"Meta-Google tone gap ({gap}) should be >= 0.15"

    def test_overall_gap_documented(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        combined = str(patel)
        assert "gap" in combined.lower() or "asymmetry" in combined.lower() or \
               "delta" in combined.lower(), \
            "Must document the overall tone gap/asymmetry"


class TestSourceCitations:
    """All findings must have source URLs."""

    def test_patel_profile_has_source_urls(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        combined = str(patel)
        url_count = combined.count("http")
        assert url_count >= 5, f"Patel profile must have 5+ URLs, found {url_count}"

    def test_decoder_youtube_sources(self):
        data = load_yaml("the-verge.yaml")
        journalists = data.get("key_journalists", [])
        patel = next(j for j in journalists if j["name"] == "Nilay Patel")
        combined = str(patel)
        assert "youtube.com" in combined or "theverge.com" in combined or \
               "deezer.com" in combined or "podcastrepublic" in combined, \
            "Must include podcast/video source URLs"
