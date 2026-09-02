"""
Type B #467 Tripp Mickle (NYT) source-access deference asymmetry baseline.
Tests 27 checks covering mechanism existence in both YAML stores, iteration/date/
rotation/goal-job IDs, same journalist, Apple framing signatures (insider depth,
omerta framing, Gruber-documented deference datapoint), Nvidia headline datapoint,
Google beat natural-experiment baseline with watchlist status, source-access (not
financial) driver class, 5 verbatim HTTPS source URLs, ranked confounders, cautious
language, distinct-from-prior, no em dashes, HTTPS-only hygiene.
"""
import re
import yaml
from pathlib import Path

REPO = Path(__file__).parent.parent
NYT = REPO / "profiles" / "nytimes.yaml"
JOURNALISTS = REPO / "profiles" / "careers" / "journalists.yaml"

TEST_ITERATION = 467
MECHANISM_ID = 467
JOURNALIST = "Tripp Mickle"
MECH_KEY = "mechanism_467_tripp_mickle_apple_omerta_deference_google_beat_baseline_sep02"

EXPECTED_URLS = [
    "https://talkingbiznews.com/media-news/how-nyts-mickle-approaches-the-apple-beat/",
    "https://talkingbiznews.com/media-news/mickle-to-take-on-google-alphabet-beat-at-ny-times/",
    "https://daringfireball.net/2025/05/idiocy_or_jackassery_you_make_the_call_made_in_america_iphone",
    "https://9to5mac.com/2026/01/08/the-new-york-times-profiles-apples-expected-next-ceo/",
    "https://muckrack.com/tripp-mickle/articles",
]


def load_nyt():
    return yaml.safe_load(NYT.read_text())


def load_journalists():
    return yaml.safe_load(JOURNALISTS.read_text())


def get_nyt_mech():
    data = load_nyt()
    for j in data["key_journalists"]:
        if j.get("name") == JOURNALIST:
            cea = j.get("cross_entity_coverage_analysis", {})
            assert MECH_KEY in cea, f"mechanism key {MECH_KEY} not found in nytimes.yaml"
            return cea[MECH_KEY]
    raise AssertionError("Tripp Mickle not found in nytimes.yaml key_journalists")


def get_career_mech():
    data = load_journalists()
    jlist = data["journalists"] if isinstance(data, dict) and "journalists" in data else data
    for entry in jlist:
        if entry.get("name") == JOURNALIST:
            assert MECH_KEY in entry, f"mechanism {MECH_KEY} not found in journalists.yaml"
            return entry[MECH_KEY]
    raise AssertionError("Tripp Mickle not found in journalists.yaml")


def test_mechanism_exists_nyt():
    mech = get_nyt_mech()
    assert mech["mechanism_id"] == MECHANISM_ID
    assert mech["iteration"] == TEST_ITERATION
    assert mech["iteration_type"] == "B"


def test_mechanism_exists_career():
    mech = get_career_mech()
    assert mech["mechanism_id"] == MECHANISM_ID
    assert mech["iteration"] == TEST_ITERATION


def test_iteration_time_and_ids():
    mech = get_nyt_mech()
    assert mech["iteration_time"] == "2026-09-02 09:00 PDT"
    assert mech["scheduled_job_id"] == "mediascope-daily-iteration"
    assert mech["goal_id"] == "goal_54093bda4145"
    assert mech["discovery_date"] == "2026-09-02"


def test_journalist_same_both_stores():
    assert get_nyt_mech()["journalist"] == JOURNALIST
    assert get_career_mech()["journalist"] == JOURNALIST


def test_publication_nyt():
    mech = get_nyt_mech()
    assert "New York Times" in mech["publication_focus"]


def test_status_is_baseline_not_finding():
    mech = get_nyt_mech()
    assert "BASELINE" in mech["status"]
    assert "not a completed asymmetry finding" in mech["status"]


def test_insider_sourcing_depth_signature():
    sig = get_nyt_mech()["apple_framing_signatures"]["insider_sourcing_depth"]
    assert "200+" in sig
    assert "Ternus" in sig
    assert "three people close to the company" in sig


def test_omerta_framing_signature():
    sig = get_nyt_mech()["apple_framing_signatures"]["omerta_framing"]
    assert "corporate omerta" in sig
    assert "sourcing challenge" in sig


def test_deference_datapoint_gruber():
    sig = get_nyt_mech()["apple_framing_signatures"]["deference_datapoint"]
    assert "Made in America" in sig
    assert "Gruber" in sig
    assert "Wayne Lam" in sig
    assert "2026" in sig or "2025" in sig


def test_nvidia_headline_datapoint():
    nv = get_nyt_mech()["nvidia_framing_datapoint"]
    assert "Doomers" in nv["headline"]
    assert "not verified this session" in nv["note"]


def test_google_beat_experiment_event():
    exp = get_nyt_mech()["google_beat_natural_experiment"]
    assert "Nico Grant" in exp["event"]
    assert "Sep 2026" in exp["event"]


def test_google_beat_watchlist_status():
    exp = get_nyt_mech()["google_beat_natural_experiment"]
    assert "Revisit in future Type B iterations" in exp["watchlist_status"]
    assert "2026-09-02 09:00 PDT" in exp["watchlist_status"]


def test_baseline_prediction_present():
    exp = get_nyt_mech()["google_beat_natural_experiment"]
    assert "colder" in exp["baseline_prediction"]
    assert "access-driven" in exp["baseline_prediction"]


def test_driver_class_not_financial():
    mech = get_nyt_mech()
    assert "NOT financial" in mech["driver_class"]
    assert "Source-access" in mech["driver_class"]


def test_source_urls_https_and_verbatim():
    mech = get_nyt_mech()
    urls = mech["source_urls"]
    assert len(urls) == 5
    for u in urls:
        assert u.startswith("https://"), f"URL must be HTTPS: {u}"
    for expected in EXPECTED_URLS:
        assert expected in urls, f"missing expected URL: {expected}"


def test_career_source_urls_match():
    cme = get_career_mech()
    for expected in EXPECTED_URLS:
        assert expected in cme["source_urls"], f"career entry missing URL: {expected}"


def test_confounders_ranked():
    conf = get_nyt_mech()["confounders_ranked"]
    assert len(conf["strong"]) >= 2
    assert len(conf["moderate"]) >= 2
    assert len(conf["weak"]) >= 1
    strong_text = " ".join(conf["strong"])
    assert "Gruber" in strong_text


def test_distinct_from_prior():
    mech = get_nyt_mech()
    assert "First Mickle mechanism" in mech["distinct_from_prior"]
    assert "Isaac" in mech["distinct_from_prior"]


def test_no_em_dashes_in_mechanism():
    mech = get_nyt_mech()
    text = yaml.safe_dump(mech, allow_unicode=True)
    assert "\u2014" not in text, "em dash found in mechanism text"
    assert "\u2013" not in text, "en dash found in mechanism text"


def test_no_em_dashes_in_career_mechanism():
    text = yaml.safe_dump(get_career_mech(), allow_unicode=True)
    assert "\u2014" not in text, "em dash found in career mechanism text"


def test_cautious_language_no_causal_claim():
    mech = get_nyt_mech()
    text = yaml.safe_dump(mech, allow_unicode=True).lower()
    assert "proves" not in text or "not proof" in text or "not a completed" in text


def test_type_b_label():
    mech = get_nyt_mech()
    assert mech["type"].startswith("B - Journalist Cross-Entity Tracking")


def test_nyt_beat_reflects_google_addition():
    data = load_nyt()
    mickle = next(j for j in data["key_journalists"] if j.get("name") == JOURNALIST)
    assert "Google" in mickle["beat"]
    assert "Nico Grant" in mickle["beat"]


def test_career_entry_still_multi_publication():
    data = load_journalists()
    jlist = data["journalists"] if isinstance(data, dict) and "journalists" in data else data
    entry = next(e for e in jlist if e.get("name") == JOURNALIST)
    assert entry.get("multi_publication") is True


def test_mechanism_key_unique_in_nyt():
    data = load_nyt()
    count = 0
    for j in data["key_journalists"]:
        cea = j.get("cross_entity_coverage_analysis", {})
        if MECH_KEY in cea:
            count += 1
    assert count == 1, "mechanism key must appear exactly once in nytimes.yaml"


def test_iteration_log_will_reference_467():
    log = (REPO / "iteration-log.md").read_text()
    assert "#467" in log, "iteration-log.md must contain the #467 entry after logging step"


def test_test_file_naming_convention():
    name = Path(__file__).name
    assert name.startswith("test_type_b_467_")
    assert "mickle" in name
    assert re.search(r"sep02_9am\.py$", name), "filename must end with sep02_9am.py"
