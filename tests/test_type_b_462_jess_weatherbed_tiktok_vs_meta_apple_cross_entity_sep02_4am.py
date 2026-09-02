"""
Type B #462 - Jess Weatherbed same-journalist cross-entity discipline check:
TikTok (adversarial) vs Meta (neutral) vs Apple (neutral)
Sep 2 2026 04:00 PDT - scheduled job_id mediascope-daily-iteration
goal_54093bda4145 rotation A->B (461 A to 462 B)

Mechanism #462 documents a same-journalist, different-entity counter-example.
The Verge news writer Jess Weatherbed applies her hardest accountability
framing to TikTok ("TikTok's policy for AI ads isn't working", Mar 28 2026,
first-person: "What irks me is that someone knows for sure if the content is
AI-generated. They are just not telling the rest of us."), while her Meta
items (mechanism 56 coding: neutral "adds"/"rolls out") and Apple items
(Mar 5 2026 AI Transparency Tags; Feb 24 2026 US Mac Mini, both neutral)
stay in product-news register. TikTok has no PMC financial relationship,
same $0 posture as Meta, so the financial-tie theory does not predict
TikTok receiving her hardest treatment. Finding strengthens the
lane-assignment account (mechanisms 56, 457): genre and news peg dominate
entity identity at the individual-journalist level.

Novelty checks:
- grep the-verge.yaml jess_weatherbed -> 56 (beat segregation) and 462 only;
  no prior same-journalist different-entity Weatherbed entry
- distinct from 457 (different publication/journalist/direction),
  436/442/447/452 (Meta-unfavorable gradients; 462 runs the other way)
- first same-topic (AI labeling) same-month controlled pair in Type B corpus

Sources (HTTPS only, no em dashes, correlation not causation):
- https://techiemag.co.uk/tiktoks-policy-for-ai-ads-isnt-working/
- https://newsatw.com/tiktoks-policy-for-ai-ads-isnt-working/
- https://blogs.taoremtls.in/daily-digest/the-verge/the-verge-digest-march-28-2026/
- https://blogs.taoremtls.in/daily-digest/the-verge/the-verge-digest-march-5-2026/
- https://blogs.taoremtls.in/daily-digest/the-verge/the-verge-digest-february-24-2026/
- https://www.techmeme.com/251015/p33

Cautious language: MANUAL ILLUSTRATIVE only, p_value NOT_CALCULATED,
cohens_d NOT_CALCULATED, ci NOT_CALCULATED, is_significant False.
Dek/excerpt-level analysis; Verge primary not directly fetched this run.
"""

import yaml
from datetime import datetime
from pathlib import Path

MECH_KEY = "jess_weatherbed_tiktok_vs_meta_apple_same_journalist_cross_entity_462"
TEST_FILE = "tests/test_type_b_462_jess_weatherbed_tiktok_vs_meta_apple_cross_entity_sep02_4am.py"


def _mech():
    data = yaml.safe_load(Path("profiles/the-verge.yaml").read_text())
    return data[MECH_KEY]


def test_yaml_parsable():
    data = yaml.safe_load(Path("profiles/the-verge.yaml").read_text())
    assert isinstance(data, dict)


def test_mechanism_462_exists_with_ids():
    m = _mech()
    assert m["mechanism_id"] == 462
    assert m["iteration"] == 462
    assert m["iteration_type"] == "B"
    assert m["iteration_time"] == "2026-09-02 04:00 PDT"
    assert m["journalist"] == "Jess Weatherbed"
    assert m["publication"] == "The Verge"
    assert m["goal_id"] == "goal_54093bda4145"
    assert m["scheduled_job_id"] == "mediascope-daily-iteration"
    assert m["finding_type"] == "journalist_cross_entity_coverage_counterexample"


def test_tiktok_evidence_quotes():
    m = _mech()
    t = m["tiktok_evidence"]
    assert t["article_date"] == "2026-03-28"
    assert "isn't working" in t["article_title"]
    assert "What irks me" in t["dek_quote_2"]
    assert "not telling the rest of us" in t["dek_quote_2"]
    assert any("did not respond" in s for s in t["accountability_markers"])
    assert any("declined" in s for s in t["accountability_markers"])


def test_apple_evidence_neutral():
    m = _mech()
    a = m["apple_evidence"]
    assert a["article_1_date"] == "2026-03-05"
    assert "Transparency Tags" in a["article_1_title"] or "labels" in a["article_1_title"].lower()
    assert a["article_2_date"] == "2026-02-24"
    assert a["apple_avg_manual_illustrative"] == 0.10


def test_meta_evidence_neutral_basis():
    m = _mech()
    e = m["meta_evidence"]
    assert "mechanism 56" in e["basis"]
    assert "group chats to Threads" in str(e["items"])
    assert "Glimmer" in str(e["items"])
    assert e["meta_avg_manual_illustrative"] == 0.05
    assert "self-inflicted DDoS" in e["within_sample_counterpoint"]


def test_controlled_pair_ai_labeling():
    m = _mech()
    cp = m["controlled_pair_ai_labeling"]
    assert "same journalist" in cp["description"].lower()
    assert "same month" in cp["description"].lower()
    assert "Mar 28 2026" in cp["tiktok_side"]
    assert "Mar 5 2026" in cp["apple_side"]
    assert "voluntary" in cp["irony_noted"].lower()


def test_tone_gradient_counterexample_direction():
    m = _mech()
    t = m["tiktok_evidence"]["article_tone_manual_illustrative"]
    meta = m["meta_evidence"]["meta_avg_manual_illustrative"]
    apple = m["apple_evidence"]["apple_avg_manual_illustrative"]
    assert t < meta < apple or (t < meta and t < apple), \
        "hardest treatment must go to TikTok for the counterexample claim"
    assert "MANUAL ILLUSTRATIVE" in m["tone_delta_manual_illustrative"]
    assert "DO NOT claim empirical significance" in m["tone_delta_manual_illustrative"]


def test_hypothesis_states_falsification():
    m = _mech()
    h = m["hypothesis"].lower()
    assert "falsif" in h
    assert "tiktok" in h
    assert "lane" in h


def test_financial_context_disciplines_theory():
    m = _mech()
    blob = " ".join(str(x) for x in m["financial_context"]).lower()
    assert "$0" in blob
    assert "does not predict" in blob or "no prediction" in blob


def test_confounders_ranked():
    m = _mech()
    confs = m["confounding_factors_ranked"]
    levels = [c["level"] for c in confs]
    assert levels.count("STRONG") >= 2
    assert levels.count("MODERATE") >= 2
    assert levels.count("WEAK") >= 1
    assert all(c["adjustment"] == "NOT_CALCULATED" for c in confs)
    blob = str(confs).lower()
    assert "genre" in blob or "story-type" in blob


def test_statistical_discipline():
    m = _mech()
    s = m["asymmetry_scoring_manual_illustrative"]
    assert s["p_value"] == "NOT_CALCULATED"
    assert s["cohens_d"] == "NOT_CALCULATED"
    assert s["ci_lower"] == "NOT_CALCULATED"
    assert s["ci_upper"] == "NOT_CALCULATED"
    assert s["is_significant"] is False
    assert s["correlation_not_causation"] is True


def test_asymmetry_scorer_run_synthetic():
    from mediascope.score.asymmetry import calculate_asymmetry
    target = [-0.55]
    peer = [0.05, 0.05, 0.10, 0.10]
    score = calculate_asymmetry(target, peer, "TikTok", ["Meta", "Apple"],
                                "the-verge", datetime(2026, 2, 24), datetime(2026, 3, 28))
    assert score.asymmetry_score < 0, "synthetic run must show negative delta (harder on TikTok)"
    assert "MANUAL ILLUSTRATIVE" in _mech()["asymmetry_scoring_manual_illustrative"]["synthetic_note"]


def test_novelty_unique_key():
    content = Path("profiles/the-verge.yaml").read_text()
    assert content.count("\n" + MECH_KEY + ":") == 1
    m = _mech()
    nov = m["novelty_vs_existing"]
    assert "mechanism_56" in nov
    assert "mechanism_457" in nov
    assert "same-journalist" in nov["mechanism_462_distinct"]


def test_cross_references():
    m = _mech()
    for ref in (56, 431, 436, 442, 447, 452, 457):
        assert ref in m["cross_references"], f"must cross-reference {ref}"


def test_sources_https():
    m = _mech()
    urls = m["source_urls"]
    assert len(urls) >= 6
    for url in urls:
        assert url.startswith("https://"), f"must be HTTPS: {url}"
        assert "http://" not in url.replace("https://", "")
        assert " " not in url
        assert "proxy" not in url.lower()


def test_no_em_dashes():
    blob = str(_mech())
    assert "\u2014" not in blob, "no em dashes per punctuation preference"
    assert "\u2013" not in blob, "no en dashes per punctuation preference"


def test_no_causal_claim():
    m = _mech()
    blob = (m["hypothesis"] + m["methodology"]).lower()
    assert "correlation not causation" in blob
    assert "not proof" in blob


def test_methodology_honesty():
    m = _mech()
    blob = m["methodology"].lower()
    assert "dek" in blob or "excerpt" in blob
    assert "not directly fetched" in blob


def test_test_file_self_reference():
    m = _mech()
    assert m["test_file"] == TEST_FILE
    assert Path(TEST_FILE).exists()
    assert m["test_count"] == 20


def test_iteration_log_rotation():
    log = Path("iteration-log.md").read_text()
    assert "#461 Type A:" in log
    assert "#462 Type B:" in log
    assert "461 A -> 462 B" in log or "461 A to 462 B" in log
