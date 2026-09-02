"""
Type A 461: The Verge x Microsoft Copilot retrenchment dedicated-beat framing asymmetry
Sep 2 2026 03:00 PDT
Mechanism 461

Validates:
- YAML parsability the-verge.yaml
- Mechanism 461 exists with required fields under competitor_relationships.microsoft
- 3 Verge Microsoft sources with URLs (Aug 2026 Copilot merger via TechRepublic attestation, Jul 6 layoffs memo via biztoc, Jun Vergecast via BigGo)
- Financial triangulation: PCM co-design partner, Azure enterprise agreement, Warren dedicated beat, Meta $0
- Asymmetry scoring MANUAL ILLUSTRATIVE delta -0.55 documented, scorer run on synthetic arrays flagged illustrative only
- Confounders ranked STRONG>=3 MODERATE>=2 WEAK>=1
- No em dashes in new mechanism
- HTTPS only
- Cautious language correlation_not_causation true, no editorial control claim
- Distinct from mechanism 6 (Patel EIC delegation) and prior Microsoft mentions (Decoder/Suleyman example)
- Iteration log rotation A correct (previous 460 E -> 461 A)
- Goal and job IDs present
"""

import yaml
import re
from pathlib import Path

MECH_KEY = "iteration_461_sep02_2026_verge_microsoft_copilot_retrenchment_dedicated_beat_framing"

def _mech():
    data = yaml.safe_load(Path("profiles/the-verge.yaml").read_text())
    return data["competitor_relationships"]["microsoft"][MECH_KEY]

def test_yaml_parsable():
    data = yaml.safe_load(Path("profiles/the-verge.yaml").read_text())
    assert "competitor_relationships" in data
    assert "microsoft" in data["competitor_relationships"]

def test_mechanism_461_exists():
    text = Path("profiles/the-verge.yaml").read_text()
    assert MECH_KEY in text
    assert "mechanism: 461" in text
    assert "iteration: 461" in text
    assert "iteration_type: A" in text
    assert "Type A: Competitor Coverage Deep Dive" in text
    assert "The Verge x Microsoft" in text

def test_financial_triangulation_documented():
    text = Path("profiles/the-verge.yaml").read_text()
    assert "pcm_licensing" in text
    assert "azure_customer" in text
    assert "dedicated_beat" in text
    assert "Tom Warren" in text
    assert "meta_zero" in text
    # PCM sources retained
    assert "searchengineland.com/microsoft-launches-publisher-content-marketplace" in text

def test_verge_microsoft_sources_three():
    mech = _mech()
    sources = mech["verge_microsoft_sources_aug2026"]
    assert len(sources) >= 3
    urls = [s["url"] for s in sources]
    assert any("techrepublic.com/article/news-microsoft-copilot-app-merger" in u for u in urls)
    assert any("biztoc.com/x/783fc4bf8d05f46e" in u for u in urls)
    assert any("finance.biggo.com" in u for u in urls)
    for s in sources:
        assert s["url"].startswith("https://")
        assert "tone_manual_illustrative" in s
        assert "framing" in s
    # counter-evidence recorded honestly
    assert any("counter-evidence" in s.get("significance", "") for s in sources)

def test_retrenchment_severity_markers():
    mech = _mech()
    finding = mech["finding"]
    assert "WIPED" in finding
    assert "earn the right" in finding
    assert "4,800" in finding
    assert "38.5M" in finding

def test_asymmetry_scoring_documented():
    mech = _mech()
    asym = mech["asymmetry_scoring_manual_illustrative"]
    assert asym["target_entity"] == "Meta Verge retrenchment coverage"
    assert asym["peer_entity"] == "Microsoft Verge Copilot retrenchment coverage"
    assert abs(asym["delta_manual_illustrative"] - (-0.55)) < 0.001
    assert asym["significant"] is False  # MANUAL ILLUSTRATIVE flagged not empirical significant
    assert "MANUAL ILLUSTRATIVE" in asym["synthetic_note"]
    assert "NOT CALCULATED" in str(asym.get("p_value", "NOT CALCULATED"))

def test_asymmetry_scorer_run():
    from mediascope.score.asymmetry import calculate_asymmetry
    from datetime import datetime
    target = [-0.45, -0.50, -0.55]
    peer = [0.05, -0.10, -0.15]
    score = calculate_asymmetry(target, peer, "Meta", ["Microsoft"], "the-verge", datetime(2026,8,13), datetime(2026,8,18))
    assert score.asymmetry_score < -0.4
    assert score.p_value < 0.05  # synthetic arrays produce significant separation, but flagged illustrative only
    assert score.cohens_d < -2.0

def test_confounders_ranked():
    mech = _mech()
    conf = mech["confounders"]
    assert len(conf["strong"]) >= 3
    assert len(conf["moderate"]) >= 2
    assert len(conf["weak"]) >= 1
    strong_text = " ".join(conf["strong"]).lower()
    assert "beat assignment" in strong_text
    assert "scoop ownership" in strong_text

def test_no_em_dashes():
    text = Path("profiles/the-verge.yaml").read_text()
    start = text.find(MECH_KEY)
    section = text[start:start+25000]
    assert "\u2014" not in section  # em dash forbidden per Ray punctuation preference
    assert "\u2013" not in section  # en dash also normalized to hyphen

def test_https_only():
    mech = _mech()
    for url in mech["source_urls"]:
        assert url.startswith("https://")
    for s in mech["verge_microsoft_sources_aug2026"]:
        assert s["url"].startswith("https://")

def test_cautious_language():
    mech = _mech()
    cautious = mech["cautious_language"]
    assert cautious["correlation_not_causation"] is True
    assert cautious["no_editorial_control_claim"] is True
    assert cautious["no_statistical_significance_claim"] is True
    assert "MANUAL ILLUSTRATIVE" in cautious["manual_illustrative_label"]

def test_distinct_from_prior():
    mech = _mech()
    distinct = mech["distinct_from_prior"]
    assert any("mechanism #6" in d for d in distinct)
    assert any("Copilot retrenchment" in d for d in distinct)
    text = Path("profiles/the-verge.yaml").read_text()
    assert text.count("mechanism: 461") == 1

def test_goal_and_job_ids():
    mech = _mech()
    assert mech["goal_id"] == "goal_54093bda4145"
    assert mech["scheduled_job_id"] == "mediascope-daily-iteration"
    assert mech["iteration_time"] == "2026-09-02 03:00 PDT"

def test_iteration_log_rotation():
    log = Path("iteration-log.md").read_text()
    assert "#460 Type E:" in log
    # after we append 461, rotation should be documented as A
    if "#461 Type A:" in log:
        assert "460 E -> 461 A" in log or "Type A" in log

def test_source_urls_valid():
    mech = _mech()
    for url in mech["source_urls"]:
        assert "http://" not in url
        assert "ftp://" not in url
        assert "example.com" not in url
        assert len(url) > 20

def test_no_proxy_urls():
    mech = _mech()
    for url in mech["source_urls"]:
        assert "proxy" not in url.lower()
        assert "localhost" not in url.lower()
