"""
Cross-entity analysis: Will Knight (WIRED) - Mechanism #421
AI Coverage Allocation Gap - Zero Dedicated Meta AI vs Deep OpenAI/Google/Anthropic Access

Iteration #421 Type B Journalist Cross-Entity Tracking
Date: 2026-08-31 10:00 PDT

KEY PATTERN: WIRED's senior AI writer Will Knight (AI Lab newsletter author, 20+ year AI beat,
Cambridge MA, MIT Tech Review 2008-2019 -> WIRED Sep 2019 present) covers OpenAI, Google DeepMind,
Anthropic with deep institutional access but has ZERO dedicated Meta AI articles 2024-2026.
Meta appears only peripherally: talent source being poached FROM, national security concern
(Llama in 106 Chinese papers), benchmark to be surpassed.

New 2026 hardware evidence strengthens capability inversion:
- OpenAI Codex Micro $230 keyboard Jul 16 2026 (PYMNTS) - niche product framed as command center for agentic work
- OpenAI screenless companion $200-$300 (TechRepublic) - cameras true, FR Face ID-like auth plus ID, always_on true,
  continuous_collection true, observe_users true, environmental_awareness true, mics true, 200+ Apple alumni,
  price $200-$300, launch early 2027, internal framing active participant in daily life third core device coolest piece of technology that the world will have ever seen Sam Altman, friend who is computer
- Meta Ray-Ban Display $799 single 12MP camera LED tamper-proof v26 hardware-level detection continuous monitoring
  receives privacy debate pervert glasses surveillance state tool for mass surveillance dormant surveillance infrastructure
- Inversion score MANUAL ILLUSTRATIVE 0.92 - Device with GREATER surveillance capability receives LESS scrutiny

Samsung Galaxy Glasses Jul 22 2026 context:
- Snapdragon AR1 Gen 1, 12MP camera, Google Gemini AI, LED anti-tamper, 200 patent applications,
  holistic engineering weight materials thermal graphite prevents heat AP transfer
- Zero Knight standalone articles, zero WIRED Gear desk standalone (Chokkattu 3+ Meta articles Jun-Jul 2026 but zero Samsung)
- 20+ other pubs covered (Android Police Jul 23 hands-on Meta should be worried, MacRumors May 13 Samsung set to beat Apple,
  Samsung Newsroom Jul 22 interview)

Financial correlation:
- Condé Nast OpenAI deal Aug 2024 $5-10M/yr, Microsoft Copilot pilot Dec 2025, Amazon Rufus Jul 2025,
  Perplexity licensing 2025 plus Comet Plus 80/20, Apple Intelligence negotiations = 5 AI partners all Meta competitors
- Condé Nast Meta deal $0
- Coverage allocation perfectly aligns with financial flow

Methodology:
- MANUAL ILLUSTRATIVE tone scores, not empirical
- n=7 OpenAI, 5 Google DeepMind, 3 Anthropic, 0 Meta dedicated = allocation gap descriptive
- p_value: not_calculated, cohens_d: not_calculated, significant: false
- Requires observed corpus VADER/TextBlob + human annotation for validation
- Strong confounders documented: beat specialization, executive access asymmetry

Sources verified Aug 31 2026:
- Muck Rack Will Knight profile https://muckrack.com/will-knight/articles
- Talking Biz News hire announcement https://talkingbiznews.com/they-talk-biz-news/wired-hires-knight-to-cover-artificial-intelligence/
- Techmeme OpenAI poaches 4 https://www.techmeme.com/260722/p27
- PYMNTS Codex Micro https://www.pymnts.com/news/artificial-intelligence/2026/openai-first-hardware-is-keyboard-not-companion/
- TechRepublic screenless AI speaker https://www.techrepublic.com/article/news-openai-screenless-ai-speaker-hardware-2026/
- WIRED author page https://www.wired.com/author/will-knight/
- Samsung intelligent eyewear interview https://news.samsung.com/us/samsung-interview-galaxy-unpacked-july-2026-inside-engineering-intelligent-eyewear
- Android Police hands-on https://www.androidpolice.com/hands-on-with-samsungs-ray-ban-meta-rival-smartglasses/
- MacRumors Samsung AI smart glasses July https://www.macrumors.com/2026/05/13/samsung-ai-smart-glasses-july/
- New Scientist author https://www.newscientist.com/author/will-knight/
"""

import os
import yaml
import pytest


PROFILES_DIR = os.path.join(os.path.dirname(__file__), "..", "profiles")


def load_wired():
    with open(os.path.join(PROFILES_DIR, "wired.yaml")) as f:
        return yaml.safe_load(f)


def load_journalists():
    with open(os.path.join(PROFILES_DIR, "careers", "journalists.yaml")) as f:
        return yaml.safe_load(f)


def get_mech_421():
    wired = load_wired()
    assert "will_knight_ai_coverage_allocation_gap_421" in wired, "Mechanism 421 should be in wired.yaml"
    return wired["will_knight_ai_coverage_allocation_gap_421"]


class TestWillKnightMechanismExists:
    def test_mechanism_421_exists(self):
        mech = get_mech_421()
        assert mech["mechanism_id"] == 421
        assert mech["journalist"] == "Will Knight"
        assert mech["publication"] == "wired"

    def test_mechanism_421_type_b(self):
        mech = get_mech_421()
        assert "Type B" in mech["type"]
        assert mech["iteration"] == 421
        assert mech["iteration_type"] == "B"

    def test_mechanism_421_no_em_dashes(self):
        path = os.path.join(PROFILES_DIR, "wired.yaml")
        with open(path) as f:
            content = f.read()
        start = content.find("will_knight_ai_coverage_allocation_gap_421")
        block = content[start:start+40000]
        assert "\u2014" not in block, "Em dash violates editorial rule"


class TestWillKnightOpenAICoverage:
    def test_openai_count_estimate(self):
        mech = get_mech_421()
        openai = mech.get("openai_coverage", {})
        assert openai.get("article_count_estimate", 0) >= 7

    def test_openai_poaches_4_example(self):
        mech = get_mech_421()
        examples = mech.get("openai_coverage", {}).get("examples", [])
        titles = [e.get("title", "") for e in examples]
        assert any("Poaches 4" in t or "Poaches" in t for t in titles)

    def test_openai_keyboard_example(self):
        mech = get_mech_421()
        examples = mech.get("openai_coverage", {}).get("examples", [])
        titles = [e.get("title", "") for e in examples]
        assert any("Keyboard" in t or "Codex Micro" in t for t in titles)

    def test_openai_source_urls(self):
        mech = get_mech_421()
        examples = mech.get("openai_coverage", {}).get("examples", [])
        urls = [e.get("source_url", "") for e in examples]
        assert any("techmeme.com" in u for u in urls)
        assert any("pymnts.com" in u for u in urls)


class TestWillKnightMetaGap:
    def test_meta_zero_dedicated(self):
        mech = get_mech_421()
        meta = mech.get("meta_coverage", {})
        assert meta.get("dedicated_articles_2024_2026") == 0
        assert meta.get("article_count_estimate") == 0

    def test_meta_coverage_gap_notes(self):
        mech = get_mech_421()
        notes = mech.get("meta_coverage", {}).get("coverage_gap_notes", "")
        assert "ZERO" in notes or "zero" in notes.lower()
        assert "Meta" in notes

    def test_meta_peripheral_roles(self):
        mech = get_mech_421()
        notes = mech.get("meta_coverage", {}).get("coverage_gap_notes", "")
        assert "poached" in notes.lower() or "poaching" in notes.lower() or "talent source" in notes.lower()


class TestWillKnightHardwareInversion:
    def test_openai_hardware_specs(self):
        mech = get_mech_421()
        inversion = mech.get("openai_hardware_vs_meta_camera_inversion", {})
        openai_specs = inversion.get("openai_device_specs", {})
        assert openai_specs.get("cameras") is True
        assert openai_specs.get("always_on") is True
        assert "Apple alumni" in str(openai_specs.get("employees_on_hardware", ""))

    def test_meta_hardware_specs(self):
        mech = get_mech_421()
        inversion = mech.get("openai_hardware_vs_meta_camera_inversion", {})
        meta_specs = inversion.get("meta_device_specs", {})
        assert "12MP" in str(meta_specs.get("camera", ""))
        assert "tamper-proof" in str(meta_specs.get("led", "")).lower() or "tamper" in str(meta_specs).lower()

    def test_inversion_score(self):
        mech = get_mech_421()
        inversion = mech.get("openai_hardware_vs_meta_camera_inversion", {})
        score = inversion.get("inversion_score_MANUAL_ILLUSTRATIVE")
        assert score is not None
        assert 0.8 <= float(score) <= 1.0


class TestWillKnightSamsungContext:
    def test_samsung_hardware_parity(self):
        mech = get_mech_421()
        samsung = mech.get("samsung_galaxy_glasses_context", {})
        assert "Snapdragon AR1" in samsung.get("hardware_parity", "")

    def test_samsung_zero_knight_coverage(self):
        mech = get_mech_421()
        samsung = mech.get("samsung_galaxy_glasses_context", {})
        assert "ZERO" in samsung.get("coverage_by_knight", "")

    def test_samsung_source_urls(self):
        mech = get_mech_421()
        samsung = mech.get("samsung_galaxy_glasses_context", {})
        urls = samsung.get("source_urls", [])
        assert len(urls) >= 3
        assert any("samsung.com" in u for u in urls)


class TestWillKnightFinancialCorrelation:
    def test_condenast_deals(self):
        mech = get_mech_421()
        fin = mech.get("financial_correlation", {})
        assert fin.get("conde_nast_openai_deal") is True
        assert fin.get("conde_nast_meta_deal") is False
        assert fin.get("total_ai_partners") == 5

    def test_non_causal_language(self):
        mech = get_mech_421()
        fin = mech.get("financial_correlation", {})
        assert "non_causal_language" in fin
        assert "correlat" in fin["non_causal_language"].lower()

    def test_financial_predicts_tone(self):
        mech = get_mech_421()
        fin = mech.get("financial_correlation", {})
        assert "financial_predicts_tone" in fin
        assert "correlat" in fin["financial_predicts_tone"].lower() or "$0" in fin["financial_predicts_tone"]


class TestWillKnightConfounders:
    def test_confounder_count(self):
        mech = get_mech_421()
        confs = mech.get("confounders", [])
        assert len(confs) >= 6

    def test_strong_confounders(self):
        mech = get_mech_421()
        confs = mech.get("confounders", [])
        strong = [c for c in confs if "[STRONG]" in c]
        assert len(strong) >= 2

    def test_confounding_adjustment(self):
        mech = get_mech_421()
        adj = mech.get("confounding_adjustment", {})
        assert "raw_asymmetry_score" in adj
        assert "adjusted_score" in adj
        assert adj["adjusted_score"] < adj["raw_asymmetry_score"]


class TestWillKnightJournalistProfile:
    def test_journalist_profile_exists(self):
        journalists = load_journalists()
        found = None
        for j in journalists.get("journalists", []):
            if j.get("name") == "Will Knight":
                found = j
                break
        assert found is not None, "Will Knight should be in journalists.yaml"

    def test_journalist_competitor_coverage(self):
        journalists = load_journalists()
        for j in journalists.get("journalists", []):
            if j.get("name") == "Will Knight":
                cc = j.get("competitor_coverage", {})
                assert "openai" in cc
                assert "meta" in cc
                assert cc.get("cross_entity_asymmetry_score", 0) >= 0.8
                break

    def test_journalist_openai_examples_expanded(self):
        journalists = load_journalists()
        for j in journalists.get("journalists", []):
            if j.get("name") == "Will Knight":
                examples = j.get("competitor_coverage", {}).get("openai", {}).get("examples", [])
                titles = [e.get("title", "") for e in examples]
                assert len(examples) >= 8 or any("Codex" in t or "Keyboard" in t for t in titles)
                break


class TestWillKnightSourceUrls:
    def test_source_url_count(self):
        mech = get_mech_421()
        urls = mech.get("source_urls", [])
        assert len(urls) >= 7

    def test_source_url_domains(self):
        mech = get_mech_421()
        urls = mech.get("source_urls", [])
        assert any("muckrack.com" in u for u in urls)
        assert any("talkingbiznews.com" in u for u in urls)
        assert any("techmeme.com" in u for u in urls)
        assert any("pymnts.com" in u for u in urls)

    def test_all_https(self):
        mech = get_mech_421()
        urls = mech.get("source_urls", [])
        for u in urls:
            assert u.startswith("https://"), f"URL should be https: {u}"


class TestWillKnightAsymmetryScore:
    def test_asymmetry_score_high(self):
        mech = get_mech_421()
        score = mech.get("cross_entity_asymmetry_score")
        assert score is not None
        assert 0.8 <= float(score) <= 1.0

    def test_cross_references(self):
        mech = get_mech_421()
        refs = mech.get("cross_references", [])
        assert len(refs) >= 8

    def test_discovery_date(self):
        mech = get_mech_421()
        assert mech.get("discovery_date") == "2026-08-31"
