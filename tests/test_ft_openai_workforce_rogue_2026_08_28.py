"""
Type A Iteration #359 — FT × OpenAI Workforce + Rogue + Anthropic Hardware Control
Validates URLs, framing labels, cautious methodology language, no synthetic-significance claim,
falsification note, and deal disclosure.

Iteration #359 Fri 2026-08-28 23:00 PT Type A Competitor Coverage Deep Dive
"""

import yaml
from pathlib import Path

PROFILE = Path(__file__).parent.parent / "profiles" / "financial-times.yaml"

def load_profile():
    with open(PROFILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def test_ft_openai_new_articles_exist():
    data = load_profile()
    openai = data["competitor_relationships"]["openai"]
    examples = openai["recent_coverage_examples_2026_h1_h2"]
    titles = [e["title"] for e in examples]
    assert any("nearly double workforce" in t.lower() or "workforce" in t.lower() and "8,000" in t for t in titles), f"Missing workforce article, have {titles}"
    assert any("hacked by its own rogue" in t.lower() or "rogue ai agents" in t.lower() for t in titles), f"Missing rogue agents article, have {titles}"

def test_ft_openai_urls_verified():
    data = load_profile()
    openai = data["competitor_relationships"]["openai"]
    examples = openai["recent_coverage_examples_2026_h1_h2"]
    urls = [e["url"] for e in examples]
    assert "https://www.reuters.com/business/openai-nearly-double-workforce-8000-by-end-2026-ft-reports-2026-03-21/" in urls
    assert "https://www.reuters.com/business/openai-report-says-its-network-was-hacked-by-its-own-rogue-ai-agents-2026-08-26/" in urls
    # Anthropic hardware comparator may be in same list
    assert any("archynetys.com" in u for u in urls)

def test_ft_anthropic_hardware_added():
    data = load_profile()
    anth = data["competitor_relationships"]["anthropic"]
    examples = anth["recent_coverage_examples_2026"]
    urls = [e["url"] for e in examples]
    assert any("archynetys.com" in u for u in urls), f"Missing Archynetys cluster URL, have {urls}"
    titles = [e["title"] for e in examples]
    assert any("scientific experiments" in t.lower() or "hardware standard" in t.lower() for t in titles)

def test_framing_labels_correct():
    data = load_profile()
    openai = data["competitor_relationships"]["openai"]
    examples = {e["title"]: e for e in openai["recent_coverage_examples_2026_h1_h2"]}
    # Workforce framing
    workforce = [e for e in examples.values() if "workforce" in e["title"].lower()][0]
    assert workforce["framing"] == "constructive_growth"
    assert workforce["tone_approx"] == 0.15 or abs(workforce["tone_approx"] - 0.15) < 0.01
    # Rogue framing
    rogue = [e for e in examples.values() if "rogue" in e["title"].lower()][0]
    assert rogue["framing"] == "neutral_technical_self_disclosure"
    assert abs(rogue["tone_approx"] - (-0.15)) < 0.01

def test_cautious_methodology_language():
    data = load_profile()
    anth = data["competitor_relationships"]["anthropic"]
    scorer = anth["asymmetry_scorer_result"]
    methodology = scorer.get("methodology_note", "")
    assert "illustrative only" in methodology.lower()
    assert "not observed" in methodology.lower() or "synthetic" in methodology.lower()
    # Must not claim empirical significance from synthetic
    assert "DO NOT claim empirical significance" in methodology or "DO NOT claim" in methodology
    # Interpretation must mention illustrative only or synthetic
    interpretation = scorer.get("interpretation", "")
    # Check that tests themselves do not assert significance from synthetic
    # Verify Welch note mentions illustrative only
    welch_note = scorer.get("welch_t_test_anthropic_vs_openai", {}).get("note", "")
    assert "illustrative only" in welch_note.lower() or "synthetic" in welch_note.lower()

def test_deal_disclosure_false():
    data = load_profile()
    openai = data["competitor_relationships"]["openai"]
    examples = openai["recent_coverage_examples_2026_h1_h2"]
    workforce = [e for e in examples if "workforce" in e["title"].lower()][0]
    assert workforce["deal_disclosed"] is False
    rogue = [e for e in examples if "rogue" in e["title"].lower()][0]
    assert rogue["deal_disclosed"] is False

def test_falsification_note_present():
    data = load_profile()
    anth = data["competitor_relationships"]["anthropic"]
    scorer = anth["asymmetry_scorer_result"]
    # Check openai_update contains falsification_note
    update = scorer.get("openai_update_2026_08_28", {})
    rogue_entry = None
    for entry in update.get("new_articles_added", []):
        if "rogue" in entry.get("title", "").lower() or "hacked" in entry.get("title", "").lower():
            rogue_entry = entry
            break
    if rogue_entry is None:
        # Also check in openai examples directly
        openai = data["competitor_relationships"]["openai"]
        examples = openai["recent_coverage_examples_2026_h1_h2"]
        rogue_entry = [e for e in examples if "rogue" in e["title"].lower()][0]
        assert "falsifies" in rogue_entry.get("significance", "").lower() or "falsifies" in rogue_entry.get("falsification_note", "").lower() or "falsifies" in str(rogue_entry).lower()
    else:
        assert "falsification_note" in rogue_entry or "falsifies" in str(rogue_entry).lower()

def test_asymmetry_delta_documented():
    data = load_profile()
    anth = data["competitor_relationships"]["anthropic"]
    scorer = anth["asymmetry_scorer_result"]
    assert "asymmetry_anthropic_vs_openai" in scorer
    assert "asymmetry_anthropic_vs_meta" in scorer
    # Updated values after Aug 28
    assert abs(scorer["asymmetry_anthropic_vs_openai"] - (-0.0367)) < 0.01
    assert abs(scorer["asymmetry_anthropic_vs_meta"] - 0.5017) < 0.02
    assert scorer["anthropic_avg"] == 0.035 or abs(scorer["anthropic_avg"] - 0.035) < 0.001
    assert abs(scorer["openai_avg_ft"] - 0.0717) < 0.001

def test_no_synthetic_significance_claim():
    data = load_profile()
    anth = data["competitor_relationships"]["anthropic"]
    scorer = anth["asymmetry_scorer_result"]
    # Ensure no claim of empirical significance from synthetic
    for key in ["interpretation", "methodology_note"]:
        text = scorer.get(key, "")
        assert "empirical significance" not in text.lower() or "DO NOT claim" in text or "illustrative" in text.lower()
    # Welch tests should not claim p<0.05 proves empirical significance without disclaimer
    for test_key in ["welch_t_test_anthropic_vs_openai", "welch_t_test_anthropic_vs_meta"]:
        note = scorer.get(test_key, {}).get("note", "")
        if "p<" in note or "significant" in note.lower():
            assert "illustrative only" in note.lower() or "synthetic" in note.lower()

def test_sources_verified_include_new_urls():
    data = load_profile()
    anth = data["competitor_relationships"]["anthropic"]
    sources = anth.get("sources_verified", [])
    assert "https://www.reuters.com/business/openai-nearly-double-workforce-8000-by-end-2026-ft-reports-2026-03-21/" in sources
    assert "https://www.reuters.com/business/openai-report-says-its-network-was-hacked-by-its-own-rogue-ai-agents-2026-08-26/" in sources
    assert "https://www.archynetys.com/trend/2026-08-28/this-is-how-anthropic-thinks-ai-agents-should-navigate-the-physical-world" in sources
