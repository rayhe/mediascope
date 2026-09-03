"""
Type A 476: MIT Technology Review x Google coverage tone vs Meta
Sep 2 2026 18:00 PDT
Mechanism 476

Validates:
- YAML parsability of mit-tech-review.yaml
- Mechanism 476 exists with required fields under competitor_relationships.google
- 2 Google articles with technologyreview.com HTTPS URLs, both opened via
  browser.open this run (Jun 11 DeepMind multi-agent safety, May 18 I/O preview)
- 2 Meta baseline articles same window (Jun 5 hack, May 18 Anduril warfare)
- Same-day natural experiment May 18 2026 documented
- Six-day proximity pair Jun 5 vs Jun 11 documented
- Asymmetry scoring MANUAL ILLUSTRATIVE delta -0.65, scorer run reproduces it,
  significant False, p 0.2085, illustrative-only labeling
- Financial triangulation: MIT-Google Program, Schmidt two-sided nexus,
  Meta-also-funds-MIT confounder (internal tension flagged, not hidden)
- Confounders ranked STRONG>=3 MODERATE>=2 WEAK>=1
- Cautious language: correlation_not_causation, no editorial control claim
- No em dashes in new mechanism text, HTTPS-only URLs
- Distinct from mechanism 15 (Anthropic pre-IPO, same file) and Aug 8 Wong test
- Iteration log rotation A correct (previous 475 E -> 476 A)
- Goal and job IDs present
"""

import re
from datetime import datetime
from pathlib import Path

import yaml

MECH_KEY = "iteration_476_sep02_2026_mittr_google_coverage_tone_vs_meta"
PROFILE = Path("profiles/mit-tech-review.yaml")


def _data():
    return yaml.safe_load(PROFILE.read_text())


def _mech():
    return _data()["competitor_relationships"]["google"][MECH_KEY]


def _mech_text():
    text = PROFILE.read_text()
    start = text.index(MECH_KEY)
    end = text.index("\n  x_twitter:", start)
    return text[start:end]


def test_yaml_parsable():
    data = _data()
    assert "competitor_relationships" in data
    assert "google" in data["competitor_relationships"]


def test_mechanism_476_exists():
    text = PROFILE.read_text()
    assert MECH_KEY in text
    assert "mechanism: 476" in text
    assert "iteration: 476" in text
    assert "iteration_type: A" in text
    assert "Type A: Competitor Coverage Deep Dive" in text or "Type A #476" in text
    assert "MIT TR x Google" in text


def test_google_articles_two_with_urls():
    mech = _mech()
    arts = mech["google_articles"]
    assert len(arts) == 2
    urls = [a["url"] for a in arts]
    assert any("1138794" in u for u in urls)
    assert any("1137439" in u for u in urls)
    for u in urls:
        assert u.startswith("https://www.technologyreview.com/2026/")


def test_google_article_registers():
    mech = _mech()
    regs = [a["register"] for a in mech["google_articles"]]
    assert "responsible_steward" in regs
    assert "mixed_competitive_critical_plus_science_validating" in regs


def test_google_articles_verified_this_run():
    mech = _mech()
    for a in mech["google_articles"]:
        assert "browser.open this run" in a["verified"]
        assert "tone_manual_illustrative" in a


def test_meta_baseline_same_window():
    mech = _mech()
    arts = mech["meta_articles_same_window"]
    assert len(arts) == 2
    urls = [a["url"] for a in arts]
    assert any("1138437" in u for u in urls)
    assert any("1137412" in u for u in urls)


def test_same_day_natural_experiment():
    mech = _mech()
    exp = mech["same_day_natural_experiment"]
    assert "2026-05-18" in exp or "May 18, 2026" in exp
    assert "warfare" in exp or "weapons" in exp


def test_six_day_proximity_pair():
    mech = _mech()
    pair = mech["six_day_proximity_pair"]
    assert "Jun 5" in pair
    assert "Jun 11" in pair
    assert "mindless" in pair or "embarrassing" in pair


def test_asymmetry_delta_documented():
    mech = _mech()
    asym = mech["asymmetry_scoring_manual_illustrative"]
    assert abs(asym["delta_manual_illustrative"] - (-0.65)) < 0.001
    assert asym["significant"] is False
    assert abs(asym["p_value"] - 0.2085) < 0.0001
    assert abs(asym["target_avg_tone"] - (-0.525)) < 0.001
    assert abs(asym["peer_avg_tone"] - 0.125) < 0.001
    assert "MANUAL ILLUSTRATIVE" in asym["synthetic_note"]


def test_scorer_reproduces_delta():
    from mediascope.score.asymmetry import calculate_asymmetry
    mech = _mech()
    asym = mech["asymmetry_scoring_manual_illustrative"]
    score = calculate_asymmetry(
        asym["target_tones"], asym["peer_tones"],
        "Meta", ["Google"], "mit-technology-review",
        datetime(2026, 5, 18), datetime(2026, 6, 11),
    )
    assert abs(score.asymmetry_score - asym["delta_manual_illustrative"]) < 0.001
    assert score.is_significant is False


def test_financial_triangulation_keys():
    mech = _mech()
    fin = mech["financial_triangulation"]
    assert "mit_google_program" in fin
    assert "relevance to Google" in fin["mit_google_program"]
    assert "schmidt_two_sided_nexus" in fin
    assert "meta_also_funds_mit" in fin
    assert "FAIR" in fin["meta_also_funds_mit"]


def test_confounders_ranked_counts():
    mech = _mech()
    conf = mech["confounders_ranked"]
    assert len(conf["strong"]) >= 3
    assert len(conf["moderate"]) >= 2
    assert len(conf["weak"]) >= 1


def test_cautious_language():
    mech = _mech()
    caut = mech["cautious_language"]
    assert caut["correlation_not_causation"] is True
    assert caut["no_editorial_control_claim"] is True
    assert "MANUAL ILLUSTRATIVE" in caut["manual_illustrative_label"]


def test_no_em_dashes_in_mechanism():
    text = _mech_text()
    assert "\u2014" not in text


def test_https_only_urls_in_mechanism():
    text = _mech_text()
    urls = re.findall(r"https?://[^\s\"']+", text)
    assert len(urls) >= 4
    for u in urls:
        assert u.startswith("https://"), u


def test_distinct_from_mechanism_15():
    mech = _mech()
    refs = " ".join(mech["cross_references"])
    assert "Mechanism #15" in refs
    assert MECH_KEY != "iteration_15_mittr_anthropic_preipo_product_validation"


def test_cross_reference_471_boundary():
    mech = _mech()
    refs = " ".join(mech["cross_references"])
    assert "#471" in refs


def test_job_and_goal_ids():
    mech = _mech()
    assert mech["job_id"] == "mediascope-daily-iteration"
    assert mech["goal_id"] == "goal_54093bda4145"


def test_rotation_a_after_475_e():
    log = Path("iteration-log.md").read_text()
    assert "#475 Type E" in log
    assert "475 E -> 476 A" in log or "476 A" in log
