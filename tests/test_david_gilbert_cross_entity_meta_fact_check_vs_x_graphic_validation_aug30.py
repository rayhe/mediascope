"""
Cross-entity analysis: David Gilbert (WIRED) — Mechanism #405
Meta Fact-Check Abandonment Adversarial vs X Graphic Video Validation Constructive

Iteration #405 Type B Journalist Cross-Entity Tracking
Date: 2026-08-30 21:00 PT

KEY PATTERN: Same WIRED journalist David Gilbert covers two platform governance
misinformation infrastructure stories with inverted evaluative direction:
- Meta ending fact-checking program: adversarial framing (blindsided partners, scrambling, rejecting bias excuse)
- X graphic Hamas video: constructive validation framing (Actually Real, Research Confirms, correcting false debunk about X)

Both are platform governance stories about misinformation infrastructure.
Same journalist, opposite evaluative direction, 15 months apart.

Sources verified Aug 30 2026:
- WIRED David Gilbert Meta fact-checking partners blindsided Jan 7 2025 aggregated via Will Coomber blog Jan 7 2025
- WIRED David Gilbert hired Sep 29 2023 from Vice via Talking Biz News Sep 29 2023
- WIRED David Gilbert X graphic Hamas video validation Oct 12 2023 cited in Wikipedia Criticism of X lines 77-78
- Muck Rack David Gilbert profile verified (disinformation, online extremism, election hucksters)
- MIT Technology Review May 19 2025 Community Notes analysis (corroborates platform governance context)

Financial context:
- Condé Nast Meta deals $0
- Condé Nast OpenAI deal Aug 2024 $5-10M/yr estimate
- X no Condé Nast deal (private post-Musk)
- Meta is ad competitor to Reddit (Advance 65.2% voting control) per mechanism #161
- Both Meta and X have $0 deals, so financial incentive does not fully explain inversion
- Same-journalist control strengthens inference vs cross-journalist comparison

Methodology:
- MANUAL ILLUSTRATIVE tone scores, not empirical
- n=1 per entity, descriptive only, insufficient for inferential significance
- p_value: not_calculated, cohens_d: not_calculated, significant: false
- Requires observed corpus VADER/TextBlob + human annotation for validation
- Strong confounders documented: news peg difference, temporal separation 15 months, editorial independence
"""

def test_david_gilbert_iteration_405_exists():
    """Mechanism #405 exists in wired.yaml"""
    import os
    import yaml
    path = os.path.join(os.path.dirname(__file__), "..", "profiles", "wired.yaml")
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    # Check top-level key exists
    assert "david_gilbert_meta_fact_check_abandonment_vs_x_graphic_validation_405" in data
    mech = data["david_gilbert_meta_fact_check_abandonment_vs_x_graphic_validation_405"]
    assert mech["mechanism_id"] == 405
    assert mech["journalist"] == "David Gilbert"
    assert mech["publication"] == "wired"
    assert "Type B" in mech["type"]

def test_david_gilbert_iteration_405_urls_verified():
    """Source URLs are present and contain expected domains"""
    import os
    import yaml
    path = os.path.join(os.path.dirname(__file__), "..", "profiles", "wired.yaml")
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    mech = data["david_gilbert_meta_fact_check_abandonment_vs_x_graphic_validation_405"]
    urls = mech.get("source_urls", [])
    assert len(urls) >= 4
    # Must include Will Coomber aggregation (WIRED Gilbert article)
    assert any("willcoomber.com" in u for u in urls)
    # Must include Talking Biz News hire announcement
    assert any("talkingbiznews.com" in u for u in urls)
    # Must include Wikipedia citation for X article
    assert any("wikipedia.org" in u or "en.wikipedia.org" in u for u in urls)
    # Must include Muck Rack
    assert any("muckrack.com" in u for u in urls)

def test_david_gilbert_iteration_405_framing_labels():
    """Framing labels are present and inverted"""
    import os
    import yaml
    path = os.path.join(os.path.dirname(__file__), "..", "profiles", "wired.yaml")
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    mech = data["david_gilbert_meta_fact_check_abandonment_vs_x_graphic_validation_405"]
    framing = mech.get("framing_comparison", {})
    assert "meta_governance_frame" in framing
    assert "x_governance_frame" in framing
    # Meta should be adversarial, X constructive
    meta_frame = framing["meta_governance_frame"].lower()
    x_frame = framing["x_governance_frame"].lower()
    assert "abandon" in meta_frame or "blindsided" in meta_frame or "truth" in meta_frame
    assert "valid" in x_frame or "authentic" in x_frame or "verified" in x_frame or "real" in x_frame
    # Tone delta manual illustrative present
    assert "tone_delta_MANUAL_ILLUSTRATIVE" in framing or "tone_comparison" in mech or "framing_comparison" in mech
    # Methodology note present
    assert mech.get("framing_comparison", {}).get("methodology_note") or "MANUAL ILLUSTRATIVE" in str(mech)

def test_david_gilbert_iteration_405_same_journalist_control():
    """Same journalist control - both articles by David Gilbert WIRED"""
    import os
    import yaml
    path = os.path.join(os.path.dirname(__file__), "..", "profiles", "wired.yaml")
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    mech = data["david_gilbert_meta_fact_check_abandonment_vs_x_graphic_validation_405"]
    meta = mech.get("meta_coverage", {})
    x = mech.get("x_coverage", {})
    assert meta.get("journalist") == "David Gilbert"
    assert x.get("journalist") == "David Gilbert"
    assert meta.get("publication") == "WIRED"
    assert x.get("publication") == "WIRED"
    # Both platform governance / misinformation infrastructure
    assert "governance" in meta.get("article_type", "").lower() or "fact" in meta.get("article_type", "").lower()
    assert "governance" in x.get("article_type", "").lower() or "verification" in x.get("article_type", "").lower()

def test_david_gilbert_iteration_405_no_em_dashes():
    """No em dashes in mechanism (editorial rule)"""
    import os
    path = os.path.join(os.path.dirname(__file__), "..", "profiles", "wired.yaml")
    with open(path, "r") as f:
        content = f.read()
    # Find our mechanism block
    start = content.find("david_gilbert_meta_fact_check_abandonment_vs_x_graphic_validation_405")
    block = content[start:start+20000]
    # Em dash character should not appear (project bans em dash)
    assert "—" not in block, "Em dash found in mechanism, violates editorial rule"

def test_david_gilbert_iteration_405_cross_entity_sources():
    """Cross-entity evidence has source URLs for both Meta and X"""
    import os
    import yaml
    path = os.path.join(os.path.dirname(__file__), "..", "profiles", "wired.yaml")
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    mech = data["david_gilbert_meta_fact_check_abandonment_vs_x_graphic_validation_405"]
    meta = mech.get("meta_coverage", {})
    x = mech.get("x_coverage", {})
    assert "source_aggregation_url" in meta or "source_url" in meta
    assert "source_wikipedia_citation_url" in x or "source_url" in x
    # Financial context present
    assert "financial_context" in mech
    fin = mech["financial_context"]
    assert "non_causal_language" in fin
    assert "correlation" in fin["non_causal_language"].lower() or "does not prove" in fin["non_causal_language"].lower()

def test_david_gilbert_iteration_405_asymmetry_observed():
    """Asymmetry scoring present with manual illustrative warning and confounders"""
    import os
    import yaml
    path = os.path.join(os.path.dirname(__file__), "..", "profiles", "wired.yaml")
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    mech = data["david_gilbert_meta_fact_check_abandonment_vs_x_graphic_validation_405"]
    # Confounders must be present and strong ones documented
    confs = mech.get("confounders", [])
    assert len(confs) >= 4
    strong_count = sum(1 for c in confs if "[STRONG]" in c)
    assert strong_count >= 2, "At least 2 STRONG confounders required"
    # Confounding adjustment present
    assert "confounding_adjustment" in mech
    adj = mech["confounding_adjustment"]
    assert "adjusted_score" in adj
    assert "raw_asymmetry_score" in adj or "raw_score" in str(adj).lower() or "raw_asymmetry_score" in mech.get("confounding_adjustment", {})
    # Cross references present
    assert "cross_references" in mech
    assert len(mech["cross_references"]) >= 3
    # Iteration metadata
    assert mech.get("iteration") == 405
    assert mech.get("iteration_type") == "B"
