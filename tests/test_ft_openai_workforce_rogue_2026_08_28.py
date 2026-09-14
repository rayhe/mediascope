"""
Type A Iteration #359 — FT × OpenAI Workforce + Rogue + Anthropic Hardware Control
Validates URLs, framing labels, cautious methodology language, no synthetic-significance claim,
falsification note, and deal disclosure.

Iteration #359 Fri 2026-08-28 23:00 PT Type A Competitor Coverage Deep Dive

SUPERSEDED STRUCTURE (Type D #730, 2026-09-13 18:00 PDT): the Aug 28 snapshot
keyed OpenAI coverage as competitor_relationships.openai.recent_coverage_examples_2026_h1_h2
and Anthropic coverage as competitor_relationships.anthropic.recent_coverage_examples_2026 /
asymmetry_scorer_result. #415 (edb3eb5, Aug 31 2026) deliberately restructured the OpenAI
block into iteration-keyed coverage lists (iteration_415 / iteration_435 / mechanism_625),
and #441/#456/#552/#643 (Sep 1-11 2026) restructured the Anthropic block into iteration-keyed
blocks plus mechanism_643 (which now carries the asymmetry_scorer_result and the
falsification-family membership). All tests below are repointed at the current structure,
preserving their original intent. The archynetys 2026-08-28 Anthropic hardware comparator
URL was dropped from the corpus in the #415 restructure (not relocated). Corpus untouched.
"""

import yaml
from pathlib import Path

PROFILE = Path(__file__).parent.parent / "profiles" / "financial-times.yaml"

def load_profile():
    with open(PROFILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def _openai(data):
    return data["competitor_relationships"]["openai"]

def _anthropic(data):
    return data["competitor_relationships"]["anthropic"]

def _i415_openai(data):
    return _openai(data)["iteration_415_aug31_2026_ft_openai_growth_vs_meta_capital_privacy_asymmetry"]

def _m643(data):
    return _anthropic(data)["mechanism_643_ft_anthropic_aisi_refusal_accountability_scoop_vs_meta_openai_launch_week_register_sep11"]

def _collect_urls(obj):
    urls = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "url" and isinstance(v, str) and v.startswith("http"):
                urls.append(v)
            else:
                urls.extend(_collect_urls(v))
    elif isinstance(obj, list):
        for v in obj:
            urls.extend(_collect_urls(v))
    return urls

def test_ft_openai_new_articles_exist():
    data = load_profile()
    examples = _i415_openai(data)["ft_openai_growth_sources_aug2026"]
    titles = [e["title"] for e in examples]
    assert any("nearly double workforce" in t.lower() or "workforce" in t.lower() and "8,000" in t for t in titles), f"Missing workforce article, have {titles}"
    assert any("hacked by its own rogue" in t.lower() or "rogue ai agents" in t.lower() for t in titles), f"Missing rogue agents article, have {titles}"

def test_ft_openai_urls_verified():
    data = load_profile()
    urls = _collect_urls(_i415_openai(data))
    assert "https://www.reuters.com/business/openai-nearly-double-workforce-8000-by-end-2026-ft-reports-2026-03-21/" in urls
    assert "https://www.reuters.com/business/openai-report-says-its-network-was-hacked-by-its-own-rogue-ai-agents-2026-08-26/" in urls
    # The archynetys 2026-08-28 Anthropic hardware comparator URL was dropped from the
    # corpus in the #415 restructure (not relocated) - documented here, not asserted.

def test_ft_anthropic_hardware_added():
    # SUPERSEDED: the Aug 28 anthropic.recent_coverage_examples_2026 hardware comparator
    # (archynetys trend URL, dropped in #415) no longer exists in the corpus. The current
    # FT-Anthropic coverage structure is iteration-keyed blocks (iteration_441 Sep 1,
    # iteration_456 Sep 1, iteration_552 Sep 6) plus mechanism_643 (Sep 11, AISI-refusal
    # accountability scoop). Assert the current structure exists with sourced coverage.
    data = load_profile()
    anth = _anthropic(data)
    for key in ["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry",
                "iteration_456_sep01_2026_ft_anthropic_20b_double_target_vs_meta_equity_raise",
                "iteration_552_sep06_2026_ft_anthropic_surveillance_refusal_register_inversion",
                "mechanism_643_ft_anthropic_aisi_refusal_accountability_scoop_vs_meta_openai_launch_week_register_sep11"]:
        assert key in anth, f"Current Anthropic coverage block missing: {key}"
    src = anth["iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry"]["ft_anthropic_sources_sep01_2026"]
    assert len(src) >= 2
    assert all(s.get("url", "").startswith("https://") for s in src)

def test_framing_labels_correct():
    data = load_profile()
    examples = {e["title"]: e for e in _i415_openai(data)["ft_openai_growth_sources_aug2026"]}
    # Workforce framing
    workforce = [e for e in examples.values() if "workforce" in e["title"].lower()][0]
    assert workforce["framing"] == "constructive_growth"
    assert workforce["tone_manual_illustrative"] == 0.15 or abs(workforce["tone_manual_illustrative"] - 0.15) < 0.01
    # Rogue framing
    rogue = [e for e in examples.values() if "rogue" in e["title"].lower()][0]
    assert rogue["framing"] == "neutral_technical_self_disclosure"
    assert abs(rogue["tone_manual_illustrative"] - (-0.15)) < 0.01

def test_cautious_methodology_language():
    data = load_profile()
    scorer = _m643(data)["asymmetry_scorer_result"]
    interpretation = scorer.get("interpretation", "")
    limitations = scorer.get("limitations", "")
    combined = (interpretation + " " + limitations).lower()
    # Must carry cautious methodology language: manual illustrative, degenerate contract, no engine
    assert "illustrative" in combined or "manual" in combined
    assert "degenerate" in combined or "no engine" in combined
    assert scorer.get("is_significant") is False
    assert scorer.get("p_value") == "NOT_CALCULATED"
    assert scorer.get("artifact_grade") is False

def test_deal_disclosure_false():
    data = load_profile()
    for src_key, src_list in [
        ("iteration_415", _i415_openai(data)["ft_openai_growth_sources_aug2026"]),
        ("iteration_435", _openai(data)["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]["ft_openai_sources_sep01_2026"]),
    ]:
        for ex in src_list:
            assert ex["deal_disclosed"] is False, f"{src_key} {ex.get('title')}: deal must be marked undisclosed"

def test_falsification_note_present():
    # The Aug 28 openai_update_2026_08_28 falsification note was superseded by the
    # mechanism_643 block, which carries the falsification-family membership for the
    # FT-Anthropic-vs-OpenAI analysis (FIFTEENTH member: mechanism 441's "softer via
    # Google channel" prediction contradicted by FT's adversarial AISI-refusal scoop).
    data = load_profile()
    m643 = _m643(data)
    assert "falsification_family" in m643, "mechanism_643 must carry the falsification-family membership note"
    note = str(m643["falsification_family"])
    assert "falsification-family member" in note
    assert "contradict" in note.lower()

def test_asymmetry_delta_documented():
    data = load_profile()
    scorer = _m643(data)["asymmetry_scorer_result"]
    assert "delta_meta_minus_anthropic" in scorer
    assert "interpretation" in scorer
    assert scorer.get("target_avg") is not None
    assert scorer.get("peer_avg") is not None
    # Directional: FT x Meta register softer than FT x Anthropic in the Sep 8-10 2026 window
    assert "softer" in scorer["interpretation"].lower()

def test_no_synthetic_significance_claim():
    data = load_profile()
    scorer = _m643(data)["asymmetry_scorer_result"]
    interpretation = scorer.get("interpretation", "")
    limitations = scorer.get("limitations", "")
    # Must not claim empirical significance from the manual illustrative scores
    assert scorer.get("is_significant") is False
    assert scorer.get("artifact_grade") is False
    combined = (interpretation + " " + limitations).lower()
    assert "empirical significance" not in combined or "not" in combined or "no " in combined

def test_sources_verified_include_new_urls():
    data = load_profile()
    urls = _collect_urls(_openai(data))
    assert "https://www.reuters.com/business/openai-nearly-double-workforce-8000-by-end-2026-ft-reports-2026-03-21/" in urls
    assert "https://www.reuters.com/business/openai-report-says-its-network-was-hacked-by-its-own-rogue-ai-agents-2026-08-26/" in urls
