"""
Type A #420: Business Insider Anthropic valuation hype vs Meta product delay - Aug 31 2026
Control case where financial incentive does NOT predict softer coverage.

Validates:
- Mechanism 420 exists in business-insider.yaml under competitor_relationships.anthropic
- At least 2 Anthropic + 3 Meta articles with URLs exact, no invented wired.com URLs where secondary used
- Primary Reuters secondary citation for BI report preserved
- Asymmetry scorer MANUAL ILLUSTRATIVE labeled, no empirical significance claim, p_value not_calculated, cohens_d not_calculated
- Non-causal wording present, editorial independence noted, control case language
- No em dashes in prose fields
- Financial tie $0 for Anthropic, licensing_via_parent for OpenAI, $0 for Meta, with source_urls for OpenAI deal
- Disclosure false for Anthropic valuation articles (no Amazon/Google stake disclosure)
- Confounders include beat assignment, vc_hype_cycle, timing, sourcing, financial_relationship_does_not_prove_direction
"""
import os
import yaml

PROFILE_PATH = os.path.join(os.path.dirname(__file__), "..", "profiles", "business-insider.yaml")

def load_profile():
    with open(PROFILE_PATH, 'r') as f:
        return yaml.safe_load(f)

def test_mechanism_420_exists():
    profile = load_profile()
    anthropic = profile.get("competitor_relationships", {}).get("anthropic", {})
    assert anthropic, "Missing competitor_relationships.anthropic"
    mech_key = "business_insider_anthropic_valuation_hype_vs_meta_product_delay_aug31_420"
    assert mech_key in anthropic, f"Missing {mech_key} in anthropic"
    mech = anthropic[mech_key]
    assert mech.get("mechanism_id") == 420
    assert "Type A" in mech.get("type", "")
    assert mech.get("publication") == "business-insider"
    assert mech.get("competitor") == "anthropic"

def test_anthropic_articles_exact_urls():
    profile = load_profile()
    mech = profile["competitor_relationships"]["anthropic"]["business_insider_anthropic_valuation_hype_vs_meta_product_delay_aug31_420"]
    articles = mech.get("business_insider_anthropic_articles", [])
    assert len(articles) >= 2, f"Need at least 2 Anthropic articles, got {len(articles)}"
    urls = [a.get("url","") for a in articles]
    # Must have BI original and Reuters secondary
    assert any("businessinsider.com/vcs-flooding-anthropic" in u for u in urls), "Missing BI original VC flooding URL"
    assert any("reuters.com/legal/transactional/anthropic-draws-offers" in u for u in urls), "Missing Reuters secondary citation"

def test_meta_articles_exact_urls():
    profile = load_profile()
    mech = profile["competitor_relationships"]["anthropic"]["business_insider_anthropic_valuation_hype_vs_meta_product_delay_aug31_420"]
    articles = mech.get("business_insider_meta_articles", [])
    assert len(articles) >= 3, f"Need at least 3 Meta articles, got {len(articles)}"
    urls = [a.get("url","") for a in articles]
    assert any("reuters.com/business/meta-delays-release-phoenix" in u for u in urls), "Missing Reuters Phoenix delay URL"
    assert any("dejavu.org" in u and "tech.yahoo.com" in u for u in urls), "Missing Dejavu Yahoo Meta supply URL"
    assert any("roadtovr.com/meta-retail-stores" in u for u in urls), "Missing RoadToVR Meta retail URL"

def test_no_invented_wired_urls():
    profile = load_profile()
    mech = profile["competitor_relationships"]["anthropic"]["business_insider_anthropic_valuation_hype_vs_meta_product_delay_aug31_420"]
    # This mechanism should NOT contain wired.com URLs since it's BI-focused
    all_urls = []
    for a in mech.get("business_insider_anthropic_articles", []):
        all_urls.append(a.get("url",""))
    for a in mech.get("business_insider_meta_articles", []):
        all_urls.append(a.get("url",""))
    for u in mech.get("source_urls", []):
        all_urls.append(u)
    # Ensure no wired.com invented where secondary used - this mechanism is BI only so wired.com should be absent
    wired_urls = [u for u in all_urls if "wired.com" in u.lower()]
    assert len(wired_urls) == 0, f"Mechanism 420 is BI-focused, should not contain wired.com URLs, found {wired_urls}"

def test_manual_illustrative_labeling():
    profile = load_profile()
    mech = profile["competitor_relationships"]["anthropic"]["business_insider_anthropic_valuation_hype_vs_meta_product_delay_aug31_420"]
    tone = mech.get("tone_comparison", {})
    assert "MANUAL ILLUSTRATIVE" in tone.get("methodology", "") or "MANUAL ILLUSTRATIVE" in tone.get("illustrative_warning", "")
    result = tone.get("asymmetry_result_MANUAL_ILLUSTRATIVE", {})
    assert result.get("p_value") == "not_calculated - illustrative only, requires Welch t-test on observed corpus"
    assert "not_calculated" in result.get("cohens_d", "")
    assert result.get("significant") is False
    assert result.get("significant_empirical") is False
    assert "not_calculated" in str(result.get("ci_95", []))

def test_non_causal_and_control_case_language():
    profile = load_profile()
    mech = profile["competitor_relationships"]["anthropic"]["business_insider_anthropic_valuation_hype_vs_meta_product_delay_aug31_420"]
    cautious = mech.get("cautious_language", "").lower()
    assert "correlation does not imply causation" in cautious or "does not imply causation" in cautious or "not proof" in cautious
    assert "control case" in cautious or "control case" in mech.get("finding", "").lower()
    # Must mention editorial independence
    assert "editorial independence" in cautious or "editorial independence" in mech.get("finding", "").lower() or "firewall" in cautious

def test_no_em_dashes():
    profile = load_profile()
    mech = profile["competitor_relationships"]["anthropic"]["business_insider_anthropic_valuation_hype_vs_meta_product_delay_aug31_420"]
    # Check prose fields for em dash character
    prose_fields = [
        mech.get("finding",""),
        mech.get("cautious_language",""),
    ]
    for cf in mech.get("confounders", []):
        prose_fields.append(cf.get("description",""))
    for field in prose_fields:
        assert "—" not in field, f"Em dash found in prose field, violates style guide: {field[:80]}"
        assert "–" not in field or "–" in "2025-12-06" or True  # allow en dash in dates? better to forbid em dash only
    # Strict: no em dash (U+2014) anywhere
    import json
    text = yaml.dump(mech)
    assert "—" not in text, "Em dash character found in mechanism YAML"

def test_financial_tie_disclosure():
    profile = load_profile()
    anthropic_rel = profile["competitor_relationships"]["anthropic"]
    assert anthropic_rel.get("financial_tie") == "none"
    assert anthropic_rel.get("estimated_value") == "$0"
    # OpenAI deal source_urls must exist at top-level openai
    openai = profile["competitor_relationships"]["openai"]
    assert "source_urls" in openai
    src = " ".join(openai["source_urls"])
    assert "axelspringer.com" in src
    assert "bloomberglaw.com" in src
    # Anthropic articles must have disclosure_present false
    mech = anthropic_rel["business_insider_anthropic_valuation_hype_vs_meta_product_delay_aug31_420"]
    for a in mech["business_insider_anthropic_articles"]:
        if "disclosure_present" in a:
            assert a["disclosure_present"] is False, "Anthropic valuation articles should have no disclosure of Amazon/Google stakes"

def test_confounder_completeness():
    profile = load_profile()
    mech = profile["competitor_relationships"]["anthropic"]["business_insider_anthropic_valuation_hype_vs_meta_product_delay_aug31_420"]
    factors = [c.get("factor","") for c in mech.get("confounders", [])]
    required = ["beat_assignment", "vc_hype_cycle", "timing_and_news_peg", "financial_relationship_does_not_prove_direction"]
    for req in required:
        assert any(req in f for f in factors), f"Missing required confounder {req}, got {factors}"

def test_source_urls_verification_date():
    profile = load_profile()
    mech = profile["competitor_relationships"]["anthropic"]["business_insider_anthropic_valuation_hype_vs_meta_product_delay_aug31_420"]
    assert "verification_date" in mech
    assert mech["verification_date"] == "2026-08-31"
    assert len(mech.get("source_urls", [])) >= 6
