"""
Type A 487: Guardian x Google DeepMind leadership-transition renewal register
vs Meta deficit register (Aug 2026 window)
Sep 3 2026 05:00 PDT
Mechanism 487

Validates:
- YAML parsability of guardian.yaml
- Mechanism 487 exists with required fields under competitor_relationships.google
- 2 Google articles (Aug 5 "Big shake-up", Aug 8 "new era") with dates, journalists,
  URLs, headline-frame and canonization markers, verified via BuzzSumo/Muck Rack
  excerpts and three full-text mirrors (theguardian.com blocked by policy)
- 2 Meta comparator articles (Jul 29 earnings miss, Aug 18 teen accounts)
- MANUAL ILLUSTRATIVE scorer delta -0.375, p 0.0445, significant False as human
  discipline override, reproduced by live scorer run this iteration
- Financial context: Google News AI pilot initial partner (Dec 2025) plus
  programmatic ad dependency vs Meta $0, correlate-only
- Ranked confounders: 3 STRONG (UK national halo, different journalists/desks,
  event-structure difference), 2 MODERATE, 1 WEAK; counter-evidence recorded
- Cautious language: correlation_not_causation, register-not-suppression
- No em dashes in new mechanism text, HTTPS-only URLs
- Distinct from #59 (structural), Milmo journalist cross-entity (journalist-level
  regulatory lens), #29 (allocation dimension, OpenAI pair), #472 (Type B boundary)
- Iteration log rotation A correct (previous 486 E -> 487 A)
- Goal and job IDs present
"""

import re
from pathlib import Path

import yaml

MECH_KEY = "mechanism_487_guardian_google_deepmind_leadership_renewal_vs_meta_deficit_framing"
PROFILE = Path("profiles/guardian.yaml")
ITER_LOG = Path("iteration-log.md")


def _data():
    return yaml.safe_load(PROFILE.read_text())


def _mech():
    return _data()["competitor_relationships"]["google"][MECH_KEY]


def _mech_text():
    text = PROFILE.read_text()
    start = text.index(MECH_KEY)
    end = text.index("\n  samsung:", start)
    return text[start:end]


def test_yaml_parsable():
    data = _data()
    assert "competitor_relationships" in data
    assert "google" in data["competitor_relationships"]


def test_mechanism_487_exists():
    text = PROFILE.read_text()
    assert MECH_KEY in text
    assert "mechanism_id: 487" in text
    assert "iteration: 487" in text
    assert "iteration_type: \"A\"" in text
    assert "2026-09-03 05:00 PDT" in text
    assert "mediascope-daily-iteration" in text
    assert "goal_54093bda4145" in text


def test_publication_and_pair():
    mech = _mech()
    assert mech["publication_focus"] == "The Guardian"
    assert mech["entity_pair"] == "Google vs Meta"
    assert "Guardian x Google" in mech["type"]


def test_google_articles_two_with_dates_and_urls():
    mech = _mech()
    arts = mech["google_articles"]
    assert len(arts) == 2
    titles = [a["title"] for a in arts]
    assert any("Big shake-up" in t for t in titles)
    assert any("new era" in t for t in titles)
    dates = [a["date"] for a in arts]
    assert "2026-08-05" in dates
    assert "2026-08-08" in dates
    for a in arts:
        assert a["journalist"] == "Dan Milmo"
        assert a["url"].startswith("https://www.theguardian.com/technology/2026/aug/")
        assert "blocked by policy" in a["url_verification"]


def test_google_aug5_framing_markers():
    mech = _mech()
    aug5 = [a for a in mech["google_articles"] if a["date"] == "2026-08-05"][0]
    assert "shake-up" in aug5["headline_frame"]
    assert "falling behind in AI race" in aug5["dek"]
    assert "totemic figure" in aug5["canonization_markers"]
    assert "statesmanlike" in aug5["canonization_markers"]
    assert "chief scientist of Alphabet" in aug5["elevation_markers"]
    assert "4%" in aug5["negative_facts_printed"]
    assert aug5["illustrative_tone"] == -0.15


def test_google_aug8_renewal_frame_with_counterweight():
    mech = _mech()
    aug8 = [a for a in mech["google_articles"] if a["date"] == "2026-08-08"][0]
    assert "new era" in aug8["headline_frame"]
    assert "pivotal moment in human history" in aug8["lede"]
    assert "lost its independence" in aug8["counterweight_printed"]
    assert aug8["illustrative_tone"] == -0.05


def test_meta_comparator_articles():
    mech = _mech()
    arts = mech["meta_articles"]
    assert len(arts) == 2
    titles = [a["title"] for a in arts]
    assert any("misses earnings forecasts" in t for t in titles)
    assert any("paying influencers" in t for t in titles)
    assert all(a["journalist"] == "Johana Bhuiyan" for a in arts)
    assert any("media push" in a["headline_frame"] for a in arts)


def test_register_not_suppression_nuance():
    mech = _mech()
    assert "REGISTER finding, not a suppression finding" in mech["finding_summary"]
    assert "no fact was buried" in mech["finding_summary"]


def test_scorer_manual_illustrative_documented():
    mech = _mech()
    sc = mech["scorer_manual_illustrative"]
    assert sc["target_scores"] == [-0.45, -0.5]
    assert sc["peer_scores"] == [-0.15, -0.05]
    assert sc["target_avg"] == -0.475
    assert sc["peer_avg"] == -0.1
    assert sc["asymmetry_delta"] == -0.375
    assert abs(sc["p_value"] - 0.0445) < 1e-3
    assert sc["is_significant"] is False
    assert "MANUAL ILLUSTRATIVE" in sc["note"]
    assert "human discipline override" in sc["note"]
    assert "#479" in sc["note"]


def test_scorer_reproduces_delta_live():
    from mediascope.scoring import AsymmetryScorer

    scorer = AsymmetryScorer(target_entity="Meta")
    res = scorer.score(
        target_scores=[-0.45, -0.5],
        peer_scores=[-0.15, -0.05],
        peer_entities=["Google", "Google"],
        publication_slug="guardian",
        period_start="2026-07-29",
        period_end="2026-08-18",
    )
    s = str(res)
    assert "target_avg_tone=-0.475" in s
    assert "peer_avg_tone=-0.1" in s
    assert "asymmetry_score=-0.375" in s
    # Live scorer says significant on tight synthetic arrays; the documented
    # finding overrides to False per #479 honesty precedent.
    assert "is_significant=True" in s
    assert _mech()["scorer_manual_illustrative"]["is_significant"] is False


def test_financial_context_correlate_only():
    mech = _mech()
    fc = mech["financial_context"]
    assert "News AI pilot" in fc
    assert "Dec 2025" in fc
    assert "$0" in fc
    assert "correlate only" in fc


def test_confounders_ranked_counts():
    mech = _mech()
    conf = mech["ranked_confounders"]
    assert len(conf["strong"]) >= 3
    assert len(conf["moderate"]) >= 2
    assert len(conf["weak"]) >= 1
    strong_text = " ".join(conf["strong"])
    assert "national halo" in strong_text or "Halo" in strong_text
    assert "Milmo" in strong_text and "Bhuiyan" in strong_text


def test_counter_evidence_recorded():
    mech = _mech()
    ce = " ".join(mech["counter_evidence"])
    assert "falling behind" in ce
    assert "lost its independence" in ce
    assert "890M" in ce


def test_statistical_discipline():
    mech = _mech()
    sd = mech["statistical_discipline"]
    assert "correlation_not_causation" in sd
    assert "is_significant false" in sd


def test_cross_references_distinct_units():
    mech = _mech()
    cr = " ".join(mech["cross_references"])
    assert "#59" in cr
    assert "dan_milmo" in cr
    assert "#29" in cr
    assert "#472" in cr
    distinct = mech["distinct_from_prior"]
    assert "First Guardian x Google Type A" in distinct
    assert "hassabis" in distinct
    assert "Microsoft PCM" in distinct


def test_source_urls_https_and_count():
    mech = _mech()
    urls = mech["source_urls"]
    assert len(urls) >= 8
    for u in urls:
        assert u.startswith("https://"), u
    joined = " ".join(urls)
    assert "buzzsumo.com/journalist/dan-milmo" in joined
    assert "muckrack.com/danmilmo" in joined
    assert "europesays.com" in joined


def test_hygiene_no_em_dash_in_new_block():
    block = _mech_text()
    assert "\u2014" not in block
    assert "\u2019" not in block
    assert all(ord(c) < 128 for c in block)


def test_hygiene_no_causal_claim():
    block = _mech_text()
    lowered = block.lower()
    assert "proves editorial influence" not in lowered
    assert "caused softer coverage" not in lowered


def test_rotation_a_after_486_e():
    log = ITER_LOG.read_text()
    assert "#486 Type E" in log
    assert "#487 Type A" in log
    assert log.index("#487 Type A") < log.index("#486 Type E")


def test_mechanism_id_unique_in_profile():
    text = PROFILE.read_text()
    assert text.count("mechanism_id: 487") == 1
