"""
Type B #472 Johana Bhuiyan (Guardian) same-day OpenAI vs Meta discipline check.
Tests 31 checks covering mechanism existence in both YAML stores, iteration/date/
rotation/goal-job IDs, same journalist, same-day pair (2026-08-18), OpenAI
accountability markers from third-party full-text excerpts, Meta-side accountability
register (headline-bounded honesty), financial context (Guardian Feb 2025 OpenAI deal),
qualitative-only scorer discipline, ranked confounders, Milmo #29 cross-reference
without contradiction, 7 verbatim HTTPS source URLs, cautious language,
distinct-from-prior (first Bhuiyan mechanism), no em dashes, HTTPS-only hygiene.
"""
import re
import yaml
from pathlib import Path

REPO = Path(__file__).parent.parent
GUARDIAN = REPO / "profiles" / "guardian.yaml"
JOURNALISTS = REPO / "profiles" / "careers" / "journalists.yaml"

TEST_ITERATION = 472
MECHANISM_ID = 472
JOURNALIST = "Johana Bhuiyan"
MECH_KEY = "mechanism_472_johana_bhuiyan_guardian_openai_meta_same_day_discipline_check_sep02"

EXPECTED_URLS_GUARDIAN = [
    "https://buzzsumo.com/journalist/johana-bhuiyan-149038734/",
    "https://www.europesays.com/people/193683/",
    "https://flipboard.com/@onelife007/ai-sdbh92qhz",
    "https://en.wikipedia.org/wiki/2026_OpenAI_agent_cyberattacks",
    "https://muckrack.com/johana-bhuiyan/articles",
    "https://smartcontentreport.com/meta-removes-ai-profiles/",
    "https://thefrontierpost.com/meta-allows-ads-crowdfunding-for-idf-drones-consumer-watchdog-finds/",
]

EXPECTED_URLS_CAREER = [
    "https://buzzsumo.com/journalist/johana-bhuiyan-149038734/",
    "https://www.europesays.com/people/193683/",
    "https://flipboard.com/@onelife007/ai-sdbh92qhz",
    "https://en.wikipedia.org/wiki/2026_OpenAI_agent_cyberattacks",
    "https://muckrack.com/johana-bhuiyan/articles",
]


def load_guardian():
    return yaml.safe_load(GUARDIAN.read_text())


def load_journalists():
    return yaml.safe_load(JOURNALISTS.read_text())


def get_guardian_mech():
    data = load_guardian()
    for j in data["key_journalists"]:
        if j.get("name") == JOURNALIST:
            cea = j.get("cross_entity_coverage_analysis", {})
            assert MECH_KEY in cea, f"mechanism key {MECH_KEY} not found in guardian.yaml"
            return cea[MECH_KEY]
    raise AssertionError("Johana Bhuiyan not found in guardian.yaml key_journalists")


def get_career_mech():
    data = load_journalists()
    jlist = data["journalists"] if isinstance(data, dict) and "journalists" in data else data
    for entry in jlist:
        if entry.get("name") == JOURNALIST:
            assert MECH_KEY in entry, f"mechanism {MECH_KEY} not found in journalists.yaml"
            return entry[MECH_KEY]
    raise AssertionError("Johana Bhuiyan not found in journalists.yaml")


def test_mechanism_exists_guardian():
    mech = get_guardian_mech()
    assert mech["mechanism_id"] == MECHANISM_ID
    assert mech["iteration"] == TEST_ITERATION
    assert mech["iteration_type"] == "B"


def test_mechanism_exists_career():
    mech = get_career_mech()
    assert mech["mechanism_id"] == MECHANISM_ID
    assert mech["iteration"] == TEST_ITERATION


def test_iteration_time_and_ids():
    mech = get_guardian_mech()
    assert mech["iteration_time"] == "2026-09-02 14:00 PDT"
    assert mech["scheduled_job_id"] == "mediascope-daily-iteration"
    assert mech["goal_id"] == "goal_54093bda4145"
    assert mech["discovery_date"] == "2026-09-02"


def test_journalist_same_both_stores():
    assert get_guardian_mech()["journalist"] == JOURNALIST
    assert get_career_mech()["journalist"] == JOURNALIST


def test_publication_guardian():
    mech = get_guardian_mech()
    assert "Guardian" in mech["publication_focus"]


def test_type_b_label():
    mech = get_guardian_mech()
    assert mech["type"].startswith("B - Journalist Cross-Entity Tracking")


def test_status_is_baseline_not_finding():
    mech = get_guardian_mech()
    assert "BASELINE" in mech["status"]
    assert "not a completed asymmetry finding" in mech["status"]


def test_driver_class_not_financial():
    mech = get_guardian_mech()
    assert "NOT financial" in mech["driver_class"]


def test_same_day_pair_date_and_headlines():
    pair = get_guardian_mech()["same_day_pair"]
    assert pair["date"] == "2026-08-18"
    assert "slowing pace of development" in pair["openai_headline"]
    assert "rogue agent" in pair["openai_headline"]
    assert "paying influencers" in pair["meta_headline"]
    assert "teen accounts" in pair["meta_headline"]


def test_openai_dek_present():
    pair = get_guardian_mech()["same_day_pair"]
    assert "Anthropic" in pair["openai_dek"]


def test_openai_evasiveness_marker():
    markers = get_guardian_mech()["openai_accountability_markers"]
    text = " ".join(markers)
    assert "did not reply to questions" in text


def test_openai_glaese_quote_marker():
    markers = get_guardian_mech()["openai_accountability_markers"]
    text = " ".join(markers)
    assert "Glaese" in text
    assert "very far from" in text


def test_openai_race_context_marker():
    markers = get_guardian_mech()["openai_accountability_markers"]
    text = " ".join(markers)
    assert "Anthropic" in text
    assert "IPO" in text


def test_meta_markers_include_three_headlines():
    markers = get_guardian_mech()["meta_accountability_markers"]
    text = " ".join(markers)
    assert "Reel-ing it in" in text
    assert "misses earnings forecasts" in text
    assert "lavishes" in text


def test_meta_markers_include_historical_pieces():
    markers = get_guardian_mech()["meta_accountability_markers"]
    text = " ".join(markers)
    assert "AI profiles" in text
    assert "IDF" in text


def test_meta_headline_only_honesty():
    markers = get_guardian_mech()["meta_accountability_markers"]
    text = " ".join(markers)
    assert "headline only" in text


def test_financial_context_names_deal():
    mech = get_guardian_mech()
    assert "Feb 2025" in mech["financial_context"]
    assert "OpenAI" in mech["financial_context"]


def test_scorer_note_qualitative_only():
    note = get_guardian_mech()["scorer_note"]
    assert "MANUAL ILLUSTRATIVE" in note
    assert "significant=false" in note
    assert "no numeric delta" in note


def test_confounders_ranked():
    conf = get_guardian_mech()["ranked_confounders"]
    assert len(conf["strong"]) >= 2
    assert len(conf["moderate"]) >= 2
    assert len(conf["weak"]) >= 1
    strong_text = " ".join(conf["strong"])
    assert "Beat-driven null" in strong_text
    assert "Headline-only" in strong_text


def test_cross_reference_milmo_29_no_contradiction():
    refs = get_guardian_mech()["cross_references"]
    text = " ".join(refs)
    assert "#29" in text
    assert "Milmo" in text
    assert "distinct journalist" in text
    assert "does not contradict" in text


def test_cross_reference_boundary_parallels():
    refs = get_guardian_mech()["cross_references"]
    text = " ".join(refs)
    assert "#471" in text
    assert "#462" in text


def test_source_urls_https_and_verbatim():
    mech = get_guardian_mech()
    urls = mech["source_urls"]
    assert len(urls) == 7
    for u in urls:
        assert u.startswith("https://"), f"URL must be HTTPS: {u}"
    for expected in EXPECTED_URLS_GUARDIAN:
        assert expected in urls, f"missing expected URL: {expected}"


def test_career_source_urls_match():
    cme = get_career_mech()
    for expected in EXPECTED_URLS_CAREER:
        assert expected in cme["source_urls"], f"career entry missing URL: {expected}"


def test_distinct_from_prior():
    mech = get_guardian_mech()
    assert "First Bhuiyan mechanism" in mech["distinct_from_prior"]


def test_no_em_dashes_in_mechanism():
    mech = get_guardian_mech()
    text = yaml.safe_dump(mech, allow_unicode=True)
    assert "—" not in text, "em dash found in mechanism text"
    assert "–" not in text, "en dash found in mechanism text"


def test_no_em_dashes_in_career_mechanism():
    text = yaml.safe_dump(get_career_mech(), allow_unicode=True)
    assert "—" not in text, "em dash found in career mechanism text"


def test_cautious_language_no_causal_claim():
    mech = get_guardian_mech()
    text = yaml.safe_dump(mech, allow_unicode=True).lower()
    assert "proves" not in text or "not a completed" in text


def test_mechanism_key_unique_in_guardian():
    data = load_guardian()
    count = 0
    for j in data["key_journalists"]:
        cea = j.get("cross_entity_coverage_analysis", {})
        if MECH_KEY in cea:
            count += 1
    assert count == 1, "mechanism key must appear exactly once in guardian.yaml"


def test_career_entry_still_multi_publication():
    data = load_journalists()
    jlist = data["journalists"] if isinstance(data, dict) and "journalists" in data else data
    entry = next(e for e in jlist if e.get("name") == JOURNALIST)
    assert entry.get("multi_publication") is True


def test_iteration_log_will_reference_472():
    log = (REPO / "iteration-log.md").read_text()
    assert "#472" in log, "iteration-log.md must contain the #472 entry after logging step"


def test_test_file_naming_convention():
    name = Path(__file__).name
    assert name.startswith("test_type_b_472_")
    assert "bhuiyan" in name
    assert re.search(r"sep02_2pm\.py$", name), "filename must end with sep02_2pm.py"
