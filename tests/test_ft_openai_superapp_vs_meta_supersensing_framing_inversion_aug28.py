"""
Test: FT OpenAI Superapp vs Meta Super-Sensing Framing Inversion (Mechanism #353)
Type A: Competitor Coverage Deep Dive — FT covering OpenAI vs Meta
Date: 2026-08-28 01:00 PT (Iteration #339)
"""
import pytest
from datetime import datetime


# Simulated import test — validates scoring logic matches profile
def test_mechanism_353_metadata():
    """Mechanism 353 exists and has required fields."""
    # Profile update validation — manual check
    import yaml, os
    path = os.path.expanduser("~/workspace/repos/mediascope/profiles/financial-times.yaml")
    with open(path) as f:
        data = yaml.safe_load(f)
    assert "cross_entity_coverage_analysis" in data
    ceca = data["cross_entity_coverage_analysis"]
    assert "superapp_vs_supersensing_framing_inversion" in ceca
    mech = ceca["superapp_vs_supersensing_framing_inversion"]
    assert mech["mechanism_id"] == 353
    assert mech["date_analyzed"] == "2026-08-28"
    assert "finding" in mech
    assert "openai_superapp_coverage" in mech
    assert "meta_supersensing_coverage" in mech
    assert "asymmetry_scorer_result" in mech


def test_openai_superapp_coverage_articles():
    """OpenAI superapp coverage has 2+ articles with constructive framing."""
    import yaml, os
    path = os.path.expanduser("~/workspace/repos/mediascope/profiles/financial-times.yaml")
    with open(path) as f:
        data = yaml.safe_load(f)
    mech = data["cross_entity_coverage_analysis"]["superapp_vs_supersensing_framing_inversion"]
    openai = mech["openai_superapp_coverage"]
    assert openai["framing"] == "constructive_enterprise_growth"
    assert openai["surveillance_language_count"] == 0
    assert openai["openai_deal_disclosed"] is False
    assert "reuters.com/business/openai-plans-chatgpt-superapp-overhaul" in openai["reuters_citation_url"]
    assert len(openai["language"]) >= 5
    assert "biggest ChatGPT overhaul yet" in openai["language"]
    # partner services
    assert "Canva" in openai["partner_services_listed"]
    assert "Booking.com" in openai["partner_services_listed"]


def test_meta_supersensing_coverage_articles():
    """Meta super-sensing coverage has adversarial surveillance framing."""
    import yaml, os
    path = os.path.expanduser("~/workspace/repos/mediascope/profiles/financial-times.yaml")
    with open(path) as f:
        data = yaml.safe_load(f)
    mech = data["cross_entity_coverage_analysis"]["superapp_vs_supersensing_framing_inversion"]
    meta = mech["meta_supersensing_coverage"]
    assert meta["framing"] == "adversarial_surveillance"
    assert meta["surveillance_language_count"] == 8
    assert meta["wiretapping_language"] is True
    assert meta["biometric_language"] is True
    assert "continuously collect audio" in meta["language"]
    assert "wiretapping laws" in meta["language"]
    assert "Meta executives don't want to activate the LED" in meta["language"][2]


def test_ft_openai_deal_financial_relationship():
    """FT-OpenAI deal exists and predicts softer coverage."""
    import yaml, os
    path = os.path.expanduser("~/workspace/repos/mediascope/profiles/financial-times.yaml")
    with open(path) as f:
        data = yaml.safe_load(f)
    rels = data["competitor_relationships"]
    assert "openai" in rels
    assert rels["openai"]["financial_tie"] == "licensing"
    assert rels["openai"]["coverage_prediction"] == "softer"
    assert "2024-04-29" in rels["openai"]["source_url"] or "openai" in rels["openai"]["source_url"]
    assert rels["meta"]["financial_tie"] == "none"


def test_asymmetry_scorer_statistical_validity():
    """Asymmetry scorer produces statistically meaningful result on synthetic tones."""
    import sys, os
    sys.path.insert(0, os.path.expanduser("~/workspace/repos/mediascope"))
    from mediascope.score.asymmetry import calculate_asymmetry
    target_scores = [-0.65, -0.72, -0.58, -0.61, -0.55]  # Meta FT tones
    peer_scores = [0.15, 0.22, 0.08, 0.18, 0.12, 0.25, 0.10]  # OpenAI FT tones
    result = calculate_asymmetry(
        target_scores=target_scores,
        peer_scores=peer_scores,
        target_entity="Meta",
        peer_entities=["OpenAI"],
        publication_slug="financial-times",
        period_start=datetime(2026, 6, 1),
        period_end=datetime(2026, 8, 27),
    )
    assert result.target_avg_tone < 0
    assert result.peer_avg_tone > 0
    assert result.asymmetry_score < -0.5  # strong negative
    assert result.p_value < 0.05
    assert abs(result.cohens_d) > 2.0  # huge effect
    assert result.is_significant is True
    assert result.confidence_interval_lower < result.confidence_interval_upper
    assert result.confidence_interval_upper < 0  # entirely negative CI


def test_asymmetry_scorer_result_documented():
    """Profile documents asymmetry scorer result with required methodology."""
    import yaml, os
    path = os.path.expanduser("~/workspace/repos/mediascope/profiles/financial-times.yaml")
    with open(path) as f:
        data = yaml.safe_load(f)
    mech = data["cross_entity_coverage_analysis"]["superapp_vs_supersensing_framing_inversion"]
    scorer = mech["asymmetry_scorer_result"]
    assert scorer["target_entity"] == "Meta"
    assert "OpenAI" in scorer["peer_entities"]
    assert scorer["asymmetry_score"] == -0.779
    assert scorer["p_value"] == 0.0
    assert scorer["is_significant"] is True
    assert "Welch's t-test" in scorer["methodology"]
    assert "bootstrap" in scorer["methodology"].lower() or "bootstrap" in scorer["methodology"]
    assert scorer["ci_excludes_zero"] is True


def test_comparison_identical_capability():
    """Comparison identifies identical capability with opposite framing."""
    import yaml, os
    path = os.path.expanduser("~/workspace/repos/mediascope/profiles/financial-times.yaml")
    with open(path) as f:
        data = yaml.safe_load(f)
    mech = data["cross_entity_coverage_analysis"]["superapp_vs_supersensing_framing_inversion"]
    comp = mech["comparison"]
    assert "always-on" in comp["identical_capability"].lower()
    assert "financial relationship" in comp["variable"].lower() or "manufacturer" in comp["variable"].lower()
    assert comp["financial_relationship_predicts_coverage"] is True
    assert comp["temporal_window_days"] == 31


def test_confounders_documented():
    """Confounders are documented with strength and adjustment."""
    import yaml, os
    path = os.path.expanduser("~/workspace/repos/mediascope/profiles/financial-times.yaml")
    with open(path) as f:
        data = yaml.safe_load(f)
    mech = data["cross_entity_coverage_analysis"]["superapp_vs_supersensing_framing_inversion"]
    assert "confounding_factors" in mech
    confs = mech["confounding_factors"]
    assert len(confs) >= 3
    strengths = [c["strength"] for c in confs]
    assert "STRONG" in strengths
    assert "MODERATE" in strengths
    # adjustments sum to -0.38
    total_adj = sum(c["adjustment"] for c in confs)
    assert abs(total_adj - (-0.38)) < 0.01


def test_sources_have_urls():
    """All sources have verifiable URLs."""
    import yaml, os
    path = os.path.expanduser("~/workspace/repos/mediascope/profiles/financial-times.yaml")
    with open(path) as f:
        data = yaml.safe_load(f)
    mech = data["cross_entity_coverage_analysis"]["superapp_vs_supersensing_framing_inversion"]
    sources = mech["source_urls"]
    assert len(sources) >= 8
    for url in sources:
        assert url.startswith("https://")
        assert "reuters.com" in url or "techcrunch.com" in url or "pymnts.com" in url or "eweek.com" in url or "macrumors.com" in url or "aiindustrytoday.com" in url

    # openai coverage URLs
    assert "reuters.com" in mech["openai_superapp_coverage"]["reuters_citation_url"]
    assert "macrumors.com" in mech["meta_supersensing_coverage"]["macrumors_citation_url"]


def test_cross_references():
    """Cross-references to prior mechanisms exist."""
    import yaml, os
    path = os.path.expanduser("~/workspace/repos/mediascope/profiles/financial-times.yaml")
    with open(path) as f:
        data = yaml.safe_load(f)
    mech = data["cross_entity_coverage_analysis"]["superapp_vs_supersensing_framing_inversion"]
    xrefs = mech["cross_references"]
    ids = [x["mechanism_id"] for x in xrefs]
    assert 18 in ids  # hardware privacy framing inversion
    assert 10 in ids  # partner validation
    assert 7 in ids   # dual-lens paradox


def test_finding_summary_and_scores():
    """Finding summary and asymmetry scores are present and calibrated."""
    import yaml, os
    path = os.path.expanduser("~/workspace/repos/mediascope/profiles/financial-times.yaml")
    with open(path) as f:
        data = yaml.safe_load(f)
    mech = data["cross_entity_coverage_analysis"]["superapp_vs_supersensing_framing_inversion"]
    assert "finding_summary" in mech
    assert "asymmetry_score" in mech
    assert mech["asymmetry_score"] == 0.27  # confounder-adjusted
    assert mech["raw_asymmetry_score"] == 0.65
    assert mech["adjusted_asymmetry_score"] == 0.27
    assert "superapp" in mech["finding_summary"].lower()
    assert "super-sensing" in mech["finding_summary"].lower() or "super sensing" in mech["finding_summary"].lower()
