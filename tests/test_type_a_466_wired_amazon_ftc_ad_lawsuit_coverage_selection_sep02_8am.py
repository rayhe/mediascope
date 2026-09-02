"""Type A #466 (2026-09-02 08:00 PDT): WIRED x Amazon - FTC ad-auction deception
lawsuit (filed Aug 31 2026) bounded 44-hour coverage-selection observation.

Rotation: #465 was Type E (07:00 PDT) -> this run is Type A per A-B-C-D-E.

Mechanism: FTC + 22 states sued Amazon Aug 31 2026 alleging 7 years of secret
ad-auction price manipulation ($20B+ alleged harm), junk-ad boosting, and Signal
spoliation. As of Sep 2 08:00 PDT (~44h post-filing) no WIRED article is indexed.
Bounded against WIRED's own Sep 2025 precedent: Caroline Haskins covered the
$2.5B Prime dark-patterns FTC settlement same-day with 2 pieces.

Evidence discipline: absence claim is SECONDARY UNVERIFIED (search-index
absence). Scores are MANUAL ILLUSTRATIVE only. Correlation, not causation.
"""
from datetime import datetime
from pathlib import Path

import yaml

MECH_KEY = "ftc_ad_auction_lawsuit_coverage_selection_466"
PROFILE = Path("/home/hatch/workspace/repos/mediascope/profiles/wired.yaml")


def _mech():
    d = yaml.safe_load(PROFILE.read_text())
    return d["competitor_relationships"]["amazon"][MECH_KEY]


def test_mechanism_key_exists():
    assert _mech()["mechanism"] == 466


def test_iteration_type_a():
    m = _mech()
    assert m["iteration_type"] == "A"
    assert m["iteration"] == 466
    assert "Type A" in m["type"]


def test_publication_pair():
    m = _mech()
    assert m["publication"] == "WIRED"
    assert m["competitor"] == "Amazon"
    assert m["publication_pair"] == "WIRED x Amazon"


def test_goal_and_job_ids():
    m = _mech()
    assert m["goal_id"] == "goal_54093bda4145"
    assert m["job_id"] == "mediascope-daily-iteration"


def test_rotation_transparency():
    m = _mech()
    assert "465" in m["rotation_transparency"]
    assert "Type E" in m["rotation_transparency"]
    assert "Type A" in m["rotation_transparency"]


def test_event_filed_date():
    m = _mech()
    assert m["event_ftc_ad_auction_lawsuit"]["filed"] == "2026-08-31"
    assert "22" in m["event_ftc_ad_auction_lawsuit"]["plaintiffs"]


def test_event_alleged_harm():
    m = _mech()
    harm = m["event_ftc_ad_auction_lawsuit"]["alleged_harm"]
    assert "$20B" in harm
    assert "1M+" in harm


def test_event_extra_hooks():
    m = _mech()
    hooks = " ".join(m["event_ftc_ad_auction_lawsuit"]["extra_hooks"]).lower()
    assert "signal" in hooks
    assert "junk-ad" in hooks
    assert "third major ftc case" in hooks


def test_amazon_response_recorded():
    m = _mech()
    assert "Denies" in m["event_ftc_ad_auction_lawsuit"]["amazon_response"]


def test_source_urls_count_and_https():
    m = _mech()
    urls = m["source_urls"]
    assert len(urls) == 6
    for u in urls:
        assert u.startswith("https://"), u


def test_source_urls_exact():
    m = _mech()
    urls = m["source_urls"]
    assert "https://www.reuters.com/legal/litigation/ftc-file-lawsuit-alleging-amazon-deceived-advertisers-wsj-reports-2026-08-31/" in urls
    assert "https://www.wsj.com/business/media/how-amazons-secret-ad-pricing-system-worked-according-to-the-ftc-24c0d78a" in urls
    assert "https://news.bloomberglaw.com/litigation/amazon-boosted-junk-ads-hid-messages-with-signal-ftc-says" in urls
    assert "https://www.usatoday.com/story/money/personal-finance/income/2026/09/01/ftc-sues-amazon-over-alleged-hidden-ad-surcharges/91565438007/" in urls


def test_capacity_precedent_haskins():
    m = _mech()
    p = m["wired_capacity_precedent_sep2025"]
    assert p["article_1_author"] == "Caroline Haskins"
    assert "$2.5 Billion" in p["article_1_title"]
    assert "$51" in p["article_2_title"]
    assert "Same-day" in p["speed"]


def test_capacity_precedent_honesty_note():
    m = _mech()
    p = m["wired_capacity_precedent_sep2025"]
    assert "not directly verified" in p["note"]
    assert len(p["attesting_secondaries"]) == 3
    for u in p["attesting_secondaries"]:
        assert u.startswith("https://")


def test_coverage_observation_bounded():
    m = _mech()
    o = m["coverage_selection_observation"]
    assert o["wired_articles_indexed"] == 0
    assert o["bounded"] is True
    assert "44 hours" in o["window"]


def test_evidence_status_secondary_unverified():
    m = _mech()
    o = m["coverage_selection_observation"]
    assert "SECONDARY UNVERIFIED" in o["evidence_status"]
    assert "search-index absence" in o["evidence_status"]


def test_financial_tie_two_deals():
    m = _mech()
    f = m["financial_tie"]
    assert f["conde_nast_amazon_deals"] == 2
    assert f["meta_deals"] == 0
    assert "Rufus" in f["deal_1"]
    assert "Alexa" in f["deal_2"]
    assert "not proof" in f["direction"]


def test_asymmetry_manual_illustrative():
    m = _mech()
    a = m["asymmetry_scoring_manual_illustrative"]
    assert abs(a["delta_manual_illustrative"] - (-0.75)) < 0.001
    assert a["significant"] is False
    assert a["p_value"] == "NOT CALCULATED"
    assert a["cohens_d"] == "NOT CALCULATED"
    assert a["confidence_interval"] == "NOT CALCULATED"
    assert "MANUAL ILLUSTRATIVE" in a["synthetic_note"]


def test_asymmetry_scorer_run():
    from mediascope.score.asymmetry import calculate_asymmetry
    target = [0.0]
    peer = [0.8, 0.7]
    score = calculate_asymmetry(
        target, peer, "Amazon", ["Amazon-Sep2025-precedent"], "wired",
        datetime(2026, 8, 31), datetime(2026, 9, 2),
    )
    assert abs(score.asymmetry_score - (-0.75)) < 0.001
    assert score.article_count_target == 1
    assert score.article_count_peers == 2
    # Scorer mechanics verified on illustrative arrays only; the YAML record
    # itself claims no empirical significance.


def test_confounders_ranked():
    m = _mech()
    c = m["confounders"]
    assert len(c["strong"]) >= 3
    assert len(c["moderate"]) >= 2
    assert len(c["weak"]) >= 1
    strong = " ".join(c["strong"]).lower()
    assert "search_index_lag" in strong
    assert "scoop_ownership" in strong
    assert "window_too_short" in strong


def test_counter_evidence_present():
    m = _mech()
    ce = " ".join(m["counter_evidence"])
    assert "Haskins" in ce
    assert "No evidence of an editorial directive" in ce


def test_cautious_language():
    m = _mech()
    cl = m["cautious_language"]
    assert cl["correlation_not_causation"] is True
    assert cl["no_editorial_control_claim"] is True
    assert cl["no_statistical_significance_claim"] is True
    assert "MANUAL ILLUSTRATIVE" in cl["manual_illustrative_label"]
    assert "re-check required" in cl["bounded_absence"]


def test_distinct_from_surveillance_parity():
    m = _mech()
    d = " ".join(m["distinct_from_prior"])
    assert "surveillance_parity_paradox" in d
    assert "Ring" in d


def test_distinct_from_prior_wired_type_a():
    m = _mech()
    d = " ".join(m["distinct_from_prior"])
    assert "#430" in d and "#451" in d


def test_novelty_verification_note():
    m = _mech()
    d = " ".join(m["distinct_from_prior"])
    assert "Aug 31 2026 FTC Amazon advertiser lawsuit" in d


def test_no_em_dashes_in_section():
    text = PROFILE.read_text()
    start = text.find(MECH_KEY)
    section = text[start:start + 22000]
    assert "\u2014" not in section
    assert "\u2013" not in section


def test_finding_mentions_44h_and_unverified():
    m = _mech()
    assert "44 hours" in m["finding"]
    assert "SECONDARY UNVERIFIED" in m["finding"]


def test_finding_mentions_8x_scale():
    m = _mech()
    assert "8x" in m["finding"]


def test_mechanism_count_unique():
    text = PROFILE.read_text()
    assert text.count("mechanism: 466") == 1
    assert text.count(MECH_KEY) == 1


def test_date_format():
    m = _mech()
    datetime.strptime(m["date"], "%Y-%m-%d")
    assert m["date"] == "2026-09-02"


def test_first_reported_by_wsj():
    m = _mech()
    assert m["event_ftc_ad_auction_lawsuit"]["first_reported_by"] == "Wall Street Journal"
