"""
Type B #477 Grace Huckins (MIT Technology Review) fortnight Google vs Meta
discipline check.

Same journalist, same AI beat, 14 days apart (2026-05-22 Google I/O piece,
2026-06-05 Meta hack piece). Google piece applies rhetoric skepticism paired
with extensive credit and long company-leadership quotes; Meta piece deploys
heavier accountability machinery (expert pile-on, refusal amplification,
alarm kicker). Driver class MIXED: event gravity leads, MIT financial nexus
is two-sided, so the mechanism bounds the financial-incentive theory rather
than confirming it. Qualitative only per Aug 28 rule.

Sources (all HTTPS, all opened or repo-archived this run or earlier):
- https://www.technologyreview.com/2026/05/22/1137813/
- https://www.technologyreview.com/2026/06/05/1138437/the-meta-hack-shows-theres-more-to-ai-security-than-mythos/
- https://www.technologyreview.com/author/grace-huckins/
- https://www.technologyreview.com/2026/05/21/1137756/roundtables-can-ai-learn-to-understand-the-world/
- https://ninedotsprize.org/winners/grace-huckins/
- https://www.nationalacademies.org/news/explaining-the-brain-scientist-writer-grace-huckins-shares-the-depth-and-wonder-of-our-minds
"""
import re
import yaml
from pathlib import Path

REPO = Path(__file__).parent.parent
MITTR = REPO / "profiles" / "mit-tech-review.yaml"
JOURNALISTS = REPO / "profiles" / "careers" / "journalists.yaml"

TEST_ITERATION = 477
MECHANISM_ID = 477
JOURNALIST = "Grace Huckins"
MECH_KEY = "mechanism_477_grace_huckins_mittr_google_meta_fortnight_discipline_check_sep02"

EXPECTED_URLS = [
    "https://www.technologyreview.com/2026/05/22/1137813/",
    "https://www.technologyreview.com/2026/06/05/1138437/the-meta-hack-shows-theres-more-to-ai-security-than-mythos/",
    "https://www.technologyreview.com/author/grace-huckins/",
    "https://www.technologyreview.com/2026/05/21/1137756/roundtables-can-ai-learn-to-understand-the-world/",
    "https://ninedotsprize.org/winners/grace-huckins/",
    "https://www.nationalacademies.org/news/explaining-the-brain-scientist-writer-grace-huckins-shares-the-depth-and-wonder-of-our-minds",
]


def load_mittr():
    return yaml.safe_load(MITTR.read_text())


def load_journalists():
    return yaml.safe_load(JOURNALISTS.read_text())


def get_mittr_mech():
    data = load_mittr()
    for j in data["key_journalists"]:
        if j.get("name") == JOURNALIST:
            cea = j.get("cross_entity_coverage_analysis", {})
            assert MECH_KEY in cea, f"mechanism key {MECH_KEY} not found in mit-tech-review.yaml"
            return cea[MECH_KEY]
    raise AssertionError("Grace Huckins not found in mit-tech-review.yaml key_journalists")


def get_career_mech():
    data = load_journalists()
    jlist = data["journalists"] if isinstance(data, dict) and "journalists" in data else data
    for entry in jlist:
        if entry.get("name") == JOURNALIST:
            assert MECH_KEY in entry, f"mechanism {MECH_KEY} not found in journalists.yaml"
            return entry[MECH_KEY]
    raise AssertionError("Grace Huckins not found in journalists.yaml")


def test_mechanism_exists_mittr():
    mech = get_mittr_mech()
    assert mech["mechanism_id"] == MECHANISM_ID
    assert mech["iteration"] == TEST_ITERATION
    assert mech["iteration_type"] == "B"


def test_mechanism_exists_career():
    mech = get_career_mech()
    assert mech["mechanism_id"] == MECHANISM_ID
    assert mech["iteration"] == TEST_ITERATION


def test_iteration_time_and_ids():
    mech = get_mittr_mech()
    assert mech["iteration_time"] == "2026-09-02 19:00 PDT"
    assert mech["scheduled_job_id"] == "mediascope-daily-iteration"
    assert mech["goal_id"] == "goal_54093bda4145"
    assert mech["discovery_date"] == "2026-09-02"


def test_journalist_same_both_stores():
    assert get_mittr_mech()["journalist"] == JOURNALIST
    assert get_career_mech()["journalist"] == JOURNALIST


def test_publication_mittr():
    mech = get_mittr_mech()
    assert "MIT Technology Review" in mech["publication_focus"]
    assert get_career_mech()["publication"] == "MIT Technology Review"


def test_type_b_label():
    mech = get_mittr_mech()
    assert mech["type"].startswith("B - Journalist Cross-Entity Tracking")


def test_status_is_baseline_not_finding():
    mech = get_mittr_mech()
    assert "BASELINE" in mech["status"]
    assert "not a completed asymmetry finding" in mech["status"]


def test_driver_class_mixed_not_clean_financial():
    mech = get_mittr_mech()
    assert "MIXED" in mech["driver_class"]
    assert "two-sided" in mech["driver_class"]


def test_fortnight_pair_dates_and_window():
    pair = get_mittr_mech()["fortnight_pair"]
    assert pair["google_date"] == "2026-05-22"
    assert pair["meta_date"] == "2026-06-05"
    assert pair["window_days"] == 14


def test_fortnight_pair_headlines():
    pair = get_mittr_mech()["fortnight_pair"]
    assert "Google I/O showed how the path for AI-driven science is shifting" in pair["google_headline"]
    assert "The Meta hack shows there's more to AI security than Mythos" in pair["meta_headline"]


def test_fortnight_pair_urls():
    pair = get_mittr_mech()["fortnight_pair"]
    assert pair["google_url"] == "https://www.technologyreview.com/2026/05/22/1137813/"
    assert pair["meta_url"] == "https://www.technologyreview.com/2026/06/05/1138437/the-meta-hack-shows-theres-more-to-ai-security-than-mythos/"


def test_google_piece_opened_this_run():
    pair = get_mittr_mech()["fortnight_pair"]
    assert "browser.open" in pair["google_access"]
    assert "2026-09-02" in pair["google_access"]


def test_google_register_credit_ledger():
    markers = get_mittr_mech()["google_register_markers"]
    blob = " ".join(markers)
    assert "enormous and meaningful achievement" in blob
    assert "Nobel" in blob
    assert "3M researchers" in blob


def test_google_register_genuine_criticism_present():
    markers = get_mittr_mech()["google_register_markers"]
    blob = " ".join(markers)
    assert "reputational hit" in blob
    assert "Anthropic and OpenAI" in blob


def test_google_register_no_alarm_machinery():
    markers = get_mittr_mech()["google_register_markers"]
    blob = " ".join(markers)
    assert "Zero refusal-amplification" in blob
    assert "zero alarm kicker" in blob


def test_meta_register_machinery_markers():
    markers = get_mittr_mech()["meta_register_markers"]
    blob = " ".join(markers)
    assert "practically mindless" in blob
    assert "4/4 experts critical" in blob
    assert "did not respond to a request for comment" in blob
    assert "very dangerous thing" in blob


def test_register_delta_prose_no_numeric_claim():
    mech = get_mittr_mech()
    assert "No numeric tone delta is claimed" in mech["register_delta_prose"]
    assert "deflates a claim" in mech["register_delta_prose"]


def test_scorer_qualitative_only():
    note = get_mittr_mech()["scorer_note"]
    assert "MANUAL ILLUSTRATIVE qualitative only" in note
    assert "significant=false" in note
    assert "NOT_CALCULATED" in note


def test_financial_context_two_sided():
    ctx = get_mittr_mech()["financial_context"]
    assert "MIT-Google Program" in ctx
    assert "FAIR" in ctx
    assert "No causal claim is made" in ctx


def test_strong_confounders_event_gravity_and_genre():
    strong = get_mittr_mech()["ranked_confounders"]["strong"]
    blob = " ".join(strong)
    assert "account-takeover" in blob or "exploit" in blob
    assert "Genre difference" in blob


def test_moderate_confounders_two_sided_nexus():
    moderate = get_mittr_mech()["ranked_confounders"]["moderate"]
    blob = " ".join(moderate)
    assert "Two-sided financial nexus" in blob


def test_weak_confounder_present():
    weak = get_mittr_mech()["ranked_confounders"]["weak"]
    assert len(weak) >= 1


def test_cross_references_472_and_476():
    refs = get_mittr_mech()["cross_references"]
    blob = " ".join(refs)
    assert "#472" in blob
    assert "#476" in blob
    assert "Bhuiyan" in blob


def test_source_urls_expected():
    urls = get_mittr_mech()["source_urls"]
    for expected in EXPECTED_URLS:
        assert expected in urls, f"missing source URL {expected}"


def test_source_urls_https_only():
    for url in get_mittr_mech()["source_urls"]:
        assert url.startswith("https://"), f"non-HTTPS URL {url}"


def test_distinct_from_prior_first_huckins():
    distinct = get_mittr_mech()["distinct_from_prior"]
    assert "First Huckins mechanism" in distinct


def test_no_em_dashes_in_mech_text():
    mech = get_mittr_mech()
    text_fields = [
        mech["finding_summary"],
        mech["driver_class"],
        mech["status"],
        mech["financial_context"],
        mech["register_delta_prose"],
        mech["distinct_from_prior"],
    ]
    for field in text_fields:
        assert "\u2014" not in field, "em dash found in mechanism text"


def test_career_entry_status_and_summary():
    mech = get_career_mech()
    assert "BASELINE" in mech["status"]
    assert "significant=false" in mech["finding_summary"]
    assert "MIXED" in mech["finding_summary"]


def test_career_entry_source_urls():
    urls = get_career_mech()["source_urls"]
    assert "https://www.technologyreview.com/2026/05/22/1137813/" in urls
    assert "https://www.technologyreview.com/2026/06/05/1138437/the-meta-hack-shows-theres-more-to-ai-security-than-mythos/" in urls
    for url in urls:
        assert url.startswith("https://")
