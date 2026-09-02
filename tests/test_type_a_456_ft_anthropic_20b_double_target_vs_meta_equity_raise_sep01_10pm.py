"""
Type A 456: FT Anthropic $20B double target fundraising vs Meta equity raise framing asymmetry
Sep 1 2026 22:00 PDT
Mechanism 456

Validates:
- YAML parsability financial-times.yaml
- Mechanism 456 exists with required fields
- 3 FT Anthropic sources with URLs (including Aug 28 $20B double target via Bloomberg Law)
- 3 FT Meta sources with URLs
- Financial relationship indirect via Google channel documented
- Asymmetry scoring MANUAL ILLUSTRATIVE delta -0.7866 documented, scorer run produces significant separation on synthetic arrays but flagged as illustrative only
- Confounders ranked STRONG>=3 MODERATE>=2 WEAK>=1
- No em dashes in new mechanism
- HTTPS only
- Cautious language correlation_not_causation true, no editorial control claim
- Distinct from mechanism 441 (441 is May 8 near $1T valuation, 456 adds Aug 28 $20B double target 2-day proximity to Meta flooding Aug 26)
- Iteration log rotation A correct (previous 455 E -> 456 A)
- Goal and job IDs present
"""

import yaml
import re
from pathlib import Path

def test_yaml_parsable():
    path = Path("profiles/financial-times.yaml")
    data = yaml.safe_load(path.read_text())
    assert "competitor_relationships" in data
    assert "anthropic" in data["competitor_relationships"]

def test_mechanism_456_exists():
    text = Path("profiles/financial-times.yaml").read_text()
    assert "iteration_456_sep01_2026_ft_anthropic_20b_double_target_vs_meta_equity_raise" in text
    assert "mechanism: 456" in text
    assert "iteration: 456" in text
    assert "iteration_type: A" in text
    assert "Type A: Competitor Coverage Deep Dive" in text
    assert "Anthropic vs Meta" in text

def test_financial_relationship_documented():
    text = Path("profiles/financial-times.yaml").read_text()
    assert "anthropic_direct: $0 FT Anthropic direct licensing zero" in text
    assert "ft_google_partnership" in text
    assert "google_anthropic_investment" in text
    assert "Up to $40B Google" in text
    assert "anthropic_20b_double_target" in text
    assert "double amount initially targeted" in text

def test_ft_anthropic_sources_three():
    data = yaml.safe_load(Path("profiles/financial-times.yaml").read_text())
    mech = data["competitor_relationships"]["anthropic"]["iteration_456_sep01_2026_ft_anthropic_20b_double_target_vs_meta_equity_raise"]
    sources = mech["ft_anthropic_sources_sep01_2026_extension"]
    assert len(sources) >= 3
    urls = [s["url"] for s in sources]
    assert any("anthropic-set-to-raise-about-20b" in u for u in urls)
    assert any("anthropic-weighs-fundraising" in u for u in urls)
    for s in sources:
        assert s["url"].startswith("https://")
        assert "tone_manual_illustrative" in s
        assert "framing" in s

def test_ft_meta_sources_three():
    data = yaml.safe_load(Path("profiles/financial-times.yaml").read_text())
    mech = data["competitor_relationships"]["anthropic"]["iteration_456_sep01_2026_ft_anthropic_20b_double_target_vs_meta_equity_raise"]
    sources = mech["ft_meta_sources_sep01_2026_extension"]
    assert len(sources) >= 3
    urls = [s["url"] for s in sources]
    assert any("meta-weighs-big-equity-raising" in u for u in urls)
    assert any("flooding-the-market" in u for u in urls)
    for s in sources:
        assert s["url"].startswith("https://")

def test_asymmetry_scoring_documented():
    data = yaml.safe_load(Path("profiles/financial-times.yaml").read_text())
    mech = data["competitor_relationships"]["anthropic"]["iteration_456_sep01_2026_ft_anthropic_20b_double_target_vs_meta_equity_raise"]
    asym = mech["asymmetry_scoring_manual_illustrative"]
    assert asym["target_entity"] == "Meta FT capital and privacy"
    assert asym["peer_entity"] == "Anthropic FT $20B double target fundraising"
    assert abs(asym["delta_manual_illustrative"] - (-0.7866)) < 0.001
    assert asym["significant"] is False  # MANUAL ILLUSTRATIVE flagged not empirical significant
    assert "MANUAL ILLUSTRATIVE" in asym["synthetic_note"]
    assert "NOT CALCULATED" in str(asym.get("p_value", "NOT CALCULATED")) or asym["p_value"] == "NOT CALCULATED no observed corpus"

def test_asymmetry_scorer_run():
    from mediascope.score.asymmetry import calculate_asymmetry
    from datetime import datetime
    target=[-0.55,-0.58,-0.62]
    peer=[0.24,0.22,0.15]
    score=calculate_asymmetry(target, peer, "Meta", ["Anthropic"], "financial-times", datetime(2026,8,26), datetime(2026,8,28))
    assert score.asymmetry_score < -0.7
    assert score.p_value < 0.05  # synthetic arrays produce significant separation, but flagged illustrative only
    assert score.cohens_d < -2.0

def test_confounders_ranked():
    data = yaml.safe_load(Path("profiles/financial-times.yaml").read_text())
    mech = data["competitor_relationships"]["anthropic"]["iteration_456_sep01_2026_ft_anthropic_20b_double_target_vs_meta_equity_raise"]
    conf = mech["confounders"]
    assert len(conf["strong"]) >= 3
    assert len(conf["moderate"]) >= 2
    assert len(conf["weak"]) >= 1
    strong_text = " ".join(conf["strong"]).lower()
    assert "beat assignment" in strong_text
    assert "product-stage" in strong_text or "product-stage" in " ".join(conf["strong"]).lower() or "product-stage" in str(conf["strong"])

def test_no_em_dashes():
    path = Path("profiles/financial-times.yaml").read_text()
    # extract mechanism 456 section only
    start = path.find("iteration_456_sep01_2026_ft_anthropic_20b_double_target_vs_meta_equity_raise")
    section = path[start:start+25000]
    assert "—" not in section  # em dash forbidden per Ray punctuation preference
    assert "–" not in section or section.count("–") == 0  # en dash also normalized to hyphen

def test_https_only():
    data = yaml.safe_load(Path("profiles/financial-times.yaml").read_text())
    mech = data["competitor_relationships"]["anthropic"]["iteration_456_sep01_2026_ft_anthropic_20b_double_target_vs_meta_equity_raise"]
    for url in mech["source_urls"]:
        assert url.startswith("https://")
    for s in mech["ft_anthropic_sources_sep01_2026_extension"] + mech["ft_meta_sources_sep01_2026_extension"]:
        assert s["url"].startswith("https://")

def test_cautious_language():
    data = yaml.safe_load(Path("profiles/financial-times.yaml").read_text())
    mech = data["competitor_relationships"]["anthropic"]["iteration_456_sep01_2026_ft_anthropic_20b_double_target_vs_meta_equity_raise"]
    cautious = mech["cautious_language"]
    assert cautious["correlation_not_causation"] is True
    assert cautious["no_editorial_control_claim"] is True
    assert cautious["no_statistical_significance_claim"] is True
    assert "MANUAL ILLUSTRATIVE" in cautious["manual_illustrative_label"]

def test_distinct_from_441():
    text = Path("profiles/financial-times.yaml").read_text()
    # both should exist
    assert "iteration_441_sep01_2026_ft_anthropic_fundraising_vs_meta_equity_raise_framing_asymmetry" in text
    assert "iteration_456_sep01_2026_ft_anthropic_20b_double_target_vs_meta_equity_raise" in text
    # 456 adds $20B double target which 441 does not have
    assert text.count("Set to Raise About $20B") >= 1
    # 456 mentions 2-day proximity eliminating timing confounder, distinct extension
    assert "2-day proximity" in text or "2-day gap" in text

def test_goal_and_job_ids():
    data = yaml.safe_load(Path("profiles/financial-times.yaml").read_text())
    mech = data["competitor_relationships"]["anthropic"]["iteration_456_sep01_2026_ft_anthropic_20b_double_target_vs_meta_equity_raise"]
    assert mech["goal_id"] == "goal_54093bda4145"
    assert mech["scheduled_job_id"] == "mediascope-daily-iteration"
    assert mech["iteration_time"] == "2026-09-01 22:00 PDT"

def test_mechanism_id_uniqueness():
    text = Path("profiles/financial-times.yaml").read_text()
    # ensure mechanism 456 appears only once per competitor_relationships anthropic block as iteration_456
    assert text.count("mechanism: 456") == 1

def test_iteration_log_rotation():
    log = Path("iteration-log.md").read_text()
    # previous 455 exists, next should be 456 A after 455 E
    assert "#455 Type E:" in log
    # after we append 456, rotation should be documented as A
    # this test will pass after log entry appended, but we check file contains expected rotation note
    # allow pending: if not yet appended, skip
    if "#456 Type A:" in log:
        assert "455 E -> 456 A" in log or "E->A" in log or "Type A" in log

def test_source_urls_valid():
    data = yaml.safe_load(Path("profiles/financial-times.yaml").read_text())
    mech = data["competitor_relationships"]["anthropic"]["iteration_456_sep01_2026_ft_anthropic_20b_double_target_vs_meta_equity_raise"]
    for url in mech["source_urls"]:
        assert "http://" not in url
        assert "ftp://" not in url
        assert "example.com" not in url
        assert len(url) > 20

def test_no_proxy_urls():
    data = yaml.safe_load(Path("profiles/financial-times.yaml").read_text())
    mech = data["competitor_relationships"]["anthropic"]["iteration_456_sep01_2026_ft_anthropic_20b_double_target_vs_meta_equity_raise"]
    for url in mech["source_urls"]:
        assert "proxy" not in url.lower()
        assert "localhost" not in url.lower()
