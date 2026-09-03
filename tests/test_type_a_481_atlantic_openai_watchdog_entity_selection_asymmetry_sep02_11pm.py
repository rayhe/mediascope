"""
Type A 481: The Atlantic x OpenAI AI Watchdog entity-selection asymmetry vs Meta
Sep 2 2026 23:00 PDT
Mechanism 481

Validates:
- YAML parsability of atlantic.yaml
- Mechanism 481 exists with required fields under competitor_relationships.openai
- 2 Meta AI Watchdog articles with URLs (Strike-3 porn piece opened first-hand
  via Wayback this run; Reisner pirated-books Mar 2025)
- OpenAI side: bounded absence of entity-targeted Watchdog investigation,
  industry-context mention, Hugging Face swarm + Astra stories with no Atlantic
  byline surfaced
- MANUAL ILLUSTRATIVE scorer delta -0.6, p 0.0613, significant False,
  reproduced by live scorer run this iteration
- Financial context: OpenAI licensing deal May 2024 vs Meta $0, correlate-only
- Confounders ranked STRONG>=2 MODERATE>=2 WEAK>=1, counter-evidence recorded
- Cautious language: correlation_not_causation, no editorial control claim
- No em dashes in new mechanism text, HTTPS-only URLs
- Distinct from mechanism 404 (Anthropic mitigation credit) and 16 (Reisner gradient)
- Iteration log rotation A correct (previous 480 E -> 481 A)
- Goal and job IDs present
"""

import re
from pathlib import Path

import yaml

MECH_KEY = "mechanism_481_atlantic_openai_watchdog_entity_selection_asymmetry"
PROFILE = Path("profiles/atlantic.yaml")


def _data():
    return yaml.safe_load(PROFILE.read_text())


def _mech():
    return _data()["competitor_relationships"]["openai"][MECH_KEY]


def _mech_text():
    text = PROFILE.read_text()
    start = text.index(MECH_KEY)
    end = text.index("\n  meta:", start)
    return text[start:end]


def test_yaml_parsable():
    data = _data()
    assert "competitor_relationships" in data
    assert "openai" in data["competitor_relationships"]


def test_mechanism_481_exists():
    text = PROFILE.read_text()
    assert MECH_KEY in text
    assert "mechanism: 481" in text
    assert "iteration: 481" in text
    assert "iteration_type: A" in text
    assert "Type A: Competitor Coverage Deep Dive" in text
    assert "The Atlantic x OpenAI" in text


def test_meta_articles_two_with_urls():
    mech = _mech()
    arts = mech["meta_articles"]
    assert len(arts) == 2
    titles = [a["title"] for a in arts]
    assert any("Porn" in t for t in titles)
    assert any("Pirated-Books" in t for t in titles)
    strike3 = arts[0]
    assert strike3["url"].startswith("https://web.archive.org/")
    assert "meta-strike-3-porn-lawsuit" in strike3["url"]
    assert strike3["opened_first_hand"] is not None
    assert "AI Watchdog" in strike3["series"]


def test_strike3_framing_markers():
    mech = _mech()
    strike3 = mech["meta_articles"][0]
    assert "Meta in headline" in strike3["headline_frame"]
    assert "pirated millions of books" in strike3["lede_quote"]
    assert "passwords" in strike3["allegation_list"]
    assert "bogus" in strike3["balance_markers"]


def test_openai_side_bounded_absence():
    mech = _mech()
    side = mech["openai_side"]
    assert "none found" in side["entity_targeted_watchdog_investigation"]
    assert "bounded" in side["entity_targeted_watchdog_investigation"]
    assert "BitTorrent" in side["industry_context_mention"]
    stories = side["openai_safety_stories_in_window"]
    assert len(stories) == 2
    hf = stories[0]
    assert "700" in hf["event"] and "Hugging Face" in hf["event"]
    assert hf["atlantic_watchdog_coverage_found"] == "none"
    assert "Scientific American" in hf["other_outlets"]
    astra = stories[1]
    assert "Astra" in astra["event"] and "critical" in astra["event"]
    assert astra["atlantic_watchdog_coverage_found"] == "none"


def test_scorer_manual_illustrative():
    mech = _mech()
    sc = mech["scorer_manual_illustrative"]
    assert sc["target_scores"] == [-0.75, -0.55]
    assert sc["peer_scores"] == [0.0, -0.1]
    assert sc["target_avg"] == -0.65
    assert sc["peer_avg"] == -0.05
    assert sc["asymmetry_delta"] == -0.6
    assert abs(sc["p_value"] - 0.0613) < 1e-4
    assert sc["is_significant"] is False
    assert "MANUAL ILLUSTRATIVE" in sc["note"]
    assert "live scorer run" in sc["note"]


def test_scorer_reproduces_delta():
    from mediascope.scoring import AsymmetryScorer

    s = AsymmetryScorer(target_entity="Meta")
    r = s.score(
        target_scores=[-0.75, -0.55],
        peer_scores=[0.0, -0.1],
        peer_entities=["OpenAI"],
        publication_slug="atlantic",
        period_start="2025-03-01",
        period_end="2026-09-02",
    )
    text = str(r)
    assert "asymmetry_score=-0.6" in text
    assert "is_significant=False" in text


def test_financial_context_correlate_only():
    mech = _mech()
    fin = mech["financial_context"]
    assert "May 29 2024" in fin["openai_deal"]
    assert "$0" in fin["meta_deal"]
    assert "correlate only" in fin["status"]


def test_confounders_ranked_counts():
    mech = _mech()
    conf = mech["confounders_ranked"]
    assert len(conf["strong"]) >= 2
    assert len(conf["moderate"]) >= 2
    assert len(conf["weak"]) >= 1
    strong_text = " ".join(conf["strong"])
    assert "Beat-lane mismatch" in strong_text or "beat" in strong_text.lower()


def test_counter_evidence_recorded():
    mech = _mech()
    ce = " ".join(mech["counter_evidence"])
    assert "bogus" in ce or "denial" in ce
    assert "March 2025" in ce


def test_cautious_language():
    mech = _mech()
    assert mech["correlation_not_causation"] is True
    assert "Correlation only" in mech["cautious_language"]
    assert "editorial control" in mech["cautious_language"]


def test_no_em_dashes_in_mechanism():
    text = _mech_text()
    assert "\u2014" not in text


def test_https_only_urls_in_mechanism():
    text = _mech_text()
    urls = re.findall(r"https?://[^\s\"']+", text)
    assert len(urls) >= 5
    for u in urls:
        assert u.startswith("https://"), u


def test_source_urls_count():
    mech = _mech()
    urls = mech["source_urls"]
    assert len(urls) == 5
    assert any("web.archive.org" in u for u in urls)
    assert any("venturebeat.com" in u for u in urls)
    assert any("reuters.com" in u for u in urls)


def test_distinct_from_404_and_16():
    mech = _mech()
    assert 404 in mech["cross_references"]
    assert 16 in mech["cross_references"]
    assert MECH_KEY != "mechanism_404_mitigation_credit_asymmetry"


def test_job_and_goal_ids():
    mech = _mech()
    assert mech["scheduled_job_id"] == "mediascope-daily-iteration"
    assert mech["goal_id"] == "goal_54093bda4145"


def test_rotation_a_after_480_e():
    log = Path("iteration-log.md").read_text()
    assert "#480 Type E" in log
    assert "480 E -> 481 A" in log or "#481 Type A" in log
