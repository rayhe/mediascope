"""
Test: Dell Cameron Severity Framing Inversion  -  OpenAI Rogue Agent Actual Hacking vs Meta NameTag Dormant Code
Type B: Journalist Cross-Entity Tracking  -  Same journalist, different entities, severity inversion
Date: 2026-08-28 19:00 PT (Iteration #355  -  Type B, mechanism #366)
"""
import pytest
import yaml
import os

PROFILE_PATH = os.path.expanduser("~/workspace/repos/mediascope/profiles/wired.yaml")
JOURNALISTS_PATH = os.path.expanduser("~/workspace/repos/mediascope/profiles/careers/journalists.yaml")

def load_wired():
    with open(PROFILE_PATH) as f:
        return yaml.safe_load(f)

def load_journalists():
    with open(JOURNALISTS_PATH) as f:
        return yaml.safe_load(f)

# Exact URLs confirmed via browser task Aug 28 2026
OPENAI_URL = "https://www.wired.com/story/openais-rogue-ai-agent-hacked-more-than-just-hugging-face/"
META_NAMETAG_URL = "https://www.wired.com/story/meta-smart-glasses-face-recognition-nametag-connections/"
META_NAMETAG_ALT_TITLE = "Meta Silently Added Face-Recognition Code for Its Smart Glasses to Millions of Phones"

def test_mechanism_366_exists():
    """Mechanism 366 exists in wired.yaml journalist_cross_entity_coverage.dell_cameron"""
    data = load_wired()
    assert "journalist_cross_entity_coverage" in data
    assert "dell_cameron" in data["journalist_cross_entity_coverage"]
    mech = data["journalist_cross_entity_coverage"]["dell_cameron"]
    assert mech["mechanism_id"] == 366
    assert mech["date_analyzed"] == "2026-08-28"
    assert "finding_type" in mech
    assert "severity_framing_inversion" in mech["finding_type"] or "cross_entity" in mech["finding_type"]

def test_openai_article_verified():
    """OpenAI rogue agent article verified with exact URL, date, authors"""
    data = load_wired()
    mech = data["journalist_cross_entity_coverage"]["dell_cameron"]
    openai = mech["openai_rogue_agent"]
    assert openai["url"] == OPENAI_URL
    assert "Dell Cameron" in openai["authors"]
    assert openai["date"] == "2026-07-28"  # 8:15 PM Jul 28 per WIRED header
    assert openai["title"] == "OpenAI's Rogue AI Agent Hacked More Than Just Hugging Face"
    assert "rogue" in openai["title"].lower()
    assert openai["severity"] == "most_severe" or "severe" in openai["severity"].lower()

def test_openai_article_adversarial_counterexample():
    """OpenAI article is strongly adversarial  -  counterexample to universal softening claim"""
    data = load_wired()
    mech = data["journalist_cross_entity_coverage"]["dell_cameron"]
    openai = mech["openai_rogue_agent"]
    # Headline itself uses rogue/hacked  -  adversarial
    assert openai["headline_adversarial"] is True
    assert openai["tone_approx"] <= -0.3  # negative/adversarial
    # Must note language markers
    assert "rogue" in openai["language_markers"]
    assert "hacked" in openai["language_markers"]
    assert "unhinged" in openai["dek"].lower()  # dek contains unhinged quest

def test_meta_nametag_article_verified():
    """Meta NameTag article verified  -  dormant code, not active hacking"""
    data = load_wired()
    mech = data["journalist_cross_entity_coverage"]["dell_cameron"]
    meta = mech["meta_nametag"]
    assert meta["url"] == META_NAMETAG_URL or META_NAMETAG_ALT_TITLE.lower() in meta["title"].lower()
    assert "Dell Cameron" in meta["authors"]
    assert meta["date"].startswith("2026-06")
    assert meta["code_status"] == "dormant_never_activated"
    assert meta["severity"] == "least_severe" or "dormant" in meta["severity"].lower()

def test_severity_inversion_documented():
    """Severity inversion: OpenAI actual hacking (more severe) vs Meta dormant code (less severe)"""
    data = load_wired()
    mech = data["journalist_cross_entity_coverage"]["dell_cameron"]
    inversion = mech["severity_inversion"]
    assert inversion["openai_severity_rank"] == 1  # most severe
    assert inversion["meta_severity_rank"] == 3  # least severe
    assert inversion["openai_actual_harm"] is True  # accessed 4 services, used exposed logins
    assert inversion["meta_actual_harm"] is False  # dormant, never activated, removed in 48h
    assert "inversion" in inversion["finding"].lower() or "more severe" in inversion["finding"].lower()

def test_tone_delta_descriptive_only():
    """Tone delta is descriptive only  -  no inferential claims from n=1 per entity"""
    data = load_wired()
    mech = data["journalist_cross_entity_coverage"]["dell_cameron"]
    tone = mech["tone_comparison"]
    assert "descriptive_only" in tone["methodology_note"].lower() or "n=1" in tone["methodology_note"].lower() or "insufficient" in tone["methodology_note"].lower()
    # Must NOT claim p<0.05 as empirical
    assert tone["is_inferential"] is False
    # If synthetic arrays present, must be labeled illustrative
    if "synthetic_tone_arrays" in tone:
        assert "illustrative" in tone["synthetic_tone_arrays"]["label"].lower()
        assert tone["synthetic_tone_arrays"]["is_empirical"] is False

def test_financial_disclosure_checked():
    """Condé Nast-OpenAI deal disclosure checked for both articles"""
    data = load_wired()
    mech = data["journalist_cross_entity_coverage"]["dell_cameron"]
    assert "conde_nast_openai_deal_disclosed" in mech["openai_rogue_agent"]
    # OpenAI article should NOT disclose deal (based on prior pattern)
    assert isinstance(mech["openai_rogue_agent"]["conde_nast_openai_deal_disclosed"], bool)
    assert "financial_tie" in mech
    assert mech["financial_tie"]["type"] == "content_licensing"
    assert "OpenAI" in mech["financial_tie"]["entity"]

def test_counterevidence_preserved():
    """Mechanism explicitly notes counterevidence to financial softening thesis"""
    data = load_wired()
    mech = data["journalist_cross_entity_coverage"]["dell_cameron"]
    assert "counterevidence" in mech
    ce = mech["counterevidence"]
    ce_text = ce if isinstance(ce, str) else str(ce).lower()
    assert "softening" in ce_text.lower() or "financial" in ce_text.lower()
    # Must note that Dell Cameron can be aggressive on OpenAI in security lane
    assert "security" in ce_text.lower() or "cybersecurity" in ce_text.lower()

def test_journalist_profile_updated():
    """Dell Cameron journalist profile includes cross-entity severity comparison"""
    data = load_journalists()
    # Handle both list and dict-with-journalists-key formats
    if isinstance(data, dict):
        entries = data.get("journalists", [])
    else:
        entries = data
    dell = None
    for entry in entries:
        if isinstance(entry, dict) and entry.get("name") == "Dell Cameron":
            dell = entry
            break
    assert dell is not None, "Dell Cameron not found in journalists.yaml"
    assert "competitor_coverage" in dell
    assert "openai_vs_meta_severity_aug28" in dell["competitor_coverage"]
    cov = dell["competitor_coverage"]["openai_vs_meta_severity_aug28"]
    assert cov["mechanism_id"] == 366
    assert OPENAI_URL in cov["source_urls"] or OPENAI_URL.rstrip("/") in [u.rstrip("/") for u in cov["source_urls"]]
    assert META_NAMETAG_URL in cov["source_urls"] or any("nametag" in u.lower() or "face-recognition" in u.lower() for u in cov["source_urls"])

def test_no_unsupported_universal_softening_claim():
    """Mechanism does not claim financial ties universally produce softer coverage"""
    data = load_wired()
    mech = data["journalist_cross_entity_coverage"]["dell_cameron"]
    finding_text = str(mech).lower()
    # Must not contain universal softening language without qualification
    assert "universally softer" not in finding_text
    assert "always softer" not in finding_text
    # Must qualify with wearables vs security lanes if preserving narrower finding
    if "wearables investigative resources" in finding_text:
        assert "security" in finding_text or "cybersecurity" in finding_text or "lane" in finding_text
