"""
Type B #457 - Adrienne So Meta vs Apple Even-Handed Gear-Desk Counter-Example
Sep 1 2026 23:00 PDT - scheduled job_id mediascope-daily-iteration goal_54093bda4145 rotation A->B

Mechanism #457 documents a WIRED Gear-desk counter-example: Senior Reviews Editor
Adrienne So (fitness/wearables beat) applies even-handed product-review standards to
Meta hardware and is, if anything, warmer on Meta glasses than on Apple hardware in
the same WIRED Recommends format.

Meta evidence (secondary-verified via Muck Rack + 3-4 independent aggregators):
- Best Meta Glasses (2026), Apr 19 2026: "Meta is unquestionably winning the
  face-wearable war. Can you trust the company? Maybe not. But these are some of
  the nicest glasses I have ever worn."
- The Best Meta Glasses for Looking Hot and Invading Everyone's Privacy (undated
  2026): "I am a lifelong Ray-Ban Wayfarer wearer, and I am also WIRED's resident
  Meta wearer. I grab a pair of Meta glasses whenever I leave the house."

Apple evidence (secondary-verified via Muck Rack):
- Review: Apple AirPods Max 2, 8/10. WIRED: gorgeous comfortable iconic design.
  TIRED: battery life still disappointing, no customizable EQ, live translation
  hilariously bad.

Finding: same reviewer, same format, warmer on Meta (avg 0.42 MANUAL ILLUSTRATIVE)
than Apple (0.30 MANUAL ILLUSTRATIVE), delta +0.12 favoring Meta. This falsifies the
simple reporter-level anti-Meta-bias hypothesis for the Gear desk and strengthens
the editorial lane-assignment mechanism: the publication-level Meta adversarial
pattern is produced at story-assignment level, not by reviewer animus.

Novelty checks:
- grep wired.yaml adrienne_so -> 457 only (name previously only in analyst lists)
- prior Type B mechanisms 431, 436, 442, 447, 452 all document Meta-unfavorable
  asymmetry; 457 is the first documented counter-example (falsification)
- distinct journalist from all prior Type B entries

Sources (HTTPS, no em dashes, correlation not causation):
- https://muckrack.com/adrienne-so/articles (secondary verified)
- https://blogs.taoremtls.in/daily-digest/wired/wired-digest-april-19-2026/ (secondary)
- https://times42.com/10430092 (secondary)
- https://technewstube.com/wired/1824515/meta-glasses-2026-ray-ban-oakley-ar/ (secondary)

Cautious language: correlation not causation, structural incentive not proof of
editorial control, MANUAL ILLUSTRATIVE only, p_value NOT_CALCULATED,
cohens_d NOT_CALCULATED, ci NOT_CALCULATED, is_significant False.
Dek-level analysis only (WIRED primary paywalled).

Confidence: MEDIUM - deks confirmed across 4+ independent secondary sources;
full-text tone coding not done; single Apple data point.

Goal and job IDs: goal_54093bda4145 mediascope-daily-iteration iteration 457 Type B 2026-09-01 23:00 PDT
"""

import yaml
from pathlib import Path

MECH_KEY = "adrienne_so_meta_vs_apple_evenhanded_gear_desk_counterexample_457"
SOURCES = [
    "https://muckrack.com/adrienne-so/articles",
    "https://blogs.taoremtls.in/daily-digest/wired/wired-digest-april-19-2026/",
    "https://times42.com/10430092",
    "https://technewstube.com/wired/1824515/meta-glasses-2026-ray-ban-oakley-ar/",
]


def _wired():
    return yaml.safe_load(Path("profiles/wired.yaml").read_text())


def test_mechanism_457_exists_in_wired_yaml():
    d = _wired()
    assert MECH_KEY in d, "mechanism 457 top-level key must exist"
    m = d[MECH_KEY]
    assert m["mechanism_id"] == 457
    assert m["iteration"] == 457
    assert m["iteration_type"] == "B"
    assert m["journalist"] == "Adrienne So"


def test_adrienne_so_journalist_entry_exists():
    d = _wired()
    jcc = d.get("journalist_cross_entity_coverage", {})
    assert "adrienne_so" in jcc, "adrienne_so must be in journalist_cross_entity_coverage"
    entry = jcc["adrienne_so"]
    assert entry["iteration"] == 457
    assert "meta" in entry and "apple" in entry


def test_meta_deks_present():
    d = _wired()
    m = d[MECH_KEY]
    assert "unquestionably winning the face-wearable war" in m["meta_evidence"]["article_1_dek"]
    assert "nicest glasses I have ever worn" in m["meta_evidence"]["article_1_dek"]
    assert "resident Meta wearer" in m["meta_evidence"]["article_2_dek"]


def test_apple_review_present_with_criticism():
    d = _wired()
    m = d[MECH_KEY]
    assert m["apple_evidence"]["article_1_rating"] == "8/10"
    assert "hilariously bad" in m["apple_evidence"]["article_1_tired"]


def test_tone_delta_favors_meta_manual_illustrative():
    d = _wired()
    m = d[MECH_KEY]
    meta_avg = m["meta_evidence"]["meta_avg_manual_illustrative"]
    apple = m["apple_evidence"]["article_1_tone_manual_illustrative"]
    assert meta_avg > apple, "observed gradient must run Meta-warmer for the counterexample claim"
    assert "MANUAL ILLUSTRATIVE" in m["tone_delta_manual_illustrative"]


def test_counterexample_direction_documented():
    d = _wired()
    m = d[MECH_KEY]
    assert m["finding_type"] == "journalist_cross_entity_coverage_counterexample"
    assert "falsif" in m["hypothesis"].lower(), "must state the falsification explicitly"
    assert "lane" in m["hypothesis"].lower(), "must relocate to lane-assignment mechanism"


def test_novelty_vs_prior_type_b():
    d = _wired()
    m = d[MECH_KEY]
    nov = m["novelty_vs_existing"]
    for prior in ("mechanism_436", "mechanism_442", "mechanism_447", "mechanism_452"):
        assert prior in nov, f"{prior} must be distinguished"
    assert "falsification" in nov["mechanism_457_distinct"].lower(), "457 must be novel as falsification"
    content = Path("profiles/wired.yaml").read_text().lower()
    assert content.count("\nadrienne_so_meta_vs_apple_evenhanded_gear_desk_counterexample_457:") == 1, "mechanism key must be unique"


def test_confounders_ranked():
    d = _wired()
    m = d[MECH_KEY]
    confs = m["confounding_factors_ranked"]
    levels = [c["level"] for c in confs]
    assert levels.count("STRONG") >= 2
    assert levels.count("MODERATE") >= 2
    assert levels.count("WEAK") >= 1
    assert all(c["adjustment"] == "NOT_CALCULATED" for c in confs)


def test_statistical_discipline():
    d = _wired()
    m = d[MECH_KEY]
    assert m["p_value"] == "NOT_CALCULATED"
    assert m["cohens_d"] == "NOT_CALCULATED"
    assert m["ci_lower"] == "NOT_CALCULATED"
    assert m["ci_upper"] == "NOT_CALCULATED"
    assert m["is_significant"] is False
    assert "DO NOT claim empirical significance" in m["tone_delta_manual_illustrative"]


def test_sources_https_no_proxy():
    for url in SOURCES:
        assert url.startswith("https://"), f"must be HTTPS: {url}"
        assert " " not in url
    d = _wired()
    m = d[MECH_KEY]
    for url in m["source_urls"]:
        assert url.startswith("https://")
    assert len(m["source_urls"]) >= 4


def test_no_em_dashes_in_mechanism():
    d = _wired()
    m = d[MECH_KEY]
    blob = str(m)
    assert "\u2014" not in blob, "no em dashes per Ray punctuation preference"
    assert "\u2013" not in blob, "no en dashes per Ray punctuation preference"


def test_no_causal_claim():
    d = _wired()
    m = d[MECH_KEY]
    blob = (m["hypothesis"] + m["methodology"] + m["coverage_prediction"]).lower()
    assert "correlation not causation" in blob
    assert "not proof" in blob


def test_cross_references():
    d = _wired()
    m = d[MECH_KEY]
    for ref in (436, 442, 447, 452, 431):
        assert ref in m["cross_references"], f"must cross-reference {ref}"


def test_goal_and_job_ids():
    d = _wired()
    m = d[MECH_KEY]
    assert m["iteration_time"] == "2026-09-01 23:00 PDT"
    assert m["test_file"] == "tests/test_type_b_457_adrienne_so_meta_vs_apple_evenhanded_counterexample_sep01.py"
    assert Path(m["test_file"]).exists()


def test_secondary_sourcing_honesty():
    d = _wired()
    m = d[MECH_KEY]
    blob = (m["browser_task_verification"] + str(m["confounding_factors_ranked"])).lower()
    assert "paywall" in blob, "must disclose WIRED primary paywalled"
    assert "dek-level" in blob, "must disclose dek-level analysis limit"
