"""
Type C Financial Incentive Mapping - Perplexity Comet Plus 80/20 Revenue Share - Iteration 391

Tests for mechanism perplexity_comet_plus_revenue_share_aug30_391
- Validates schema, uniqueness, provenance, cautious wording, no em dash, no significance claim
- Does NOT claim execution results - validation via allowed non-terminal mechanisms only
"""

import os
import yaml

REPO_ROOT = os.path.expanduser("~/workspace/repos/mediascope")
COMPETITOR_YAML = os.path.join(REPO_ROOT, "profiles/competitor-entities.yaml")
WIRED_YAML = os.path.join(REPO_ROOT, "profiles/wired.yaml")

MECHANISM_KEY = "perplexity_comet_plus_revenue_share_aug30_391"
MECHANISM_ID = 391

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def test_mechanism_exists_in_competitor_entities():
    data = load_yaml(COMPETITOR_YAML)
    # entities.perplexity.perplexity_comet_plus_revenue_share_aug30_391
    assert "entities" in data
    assert "perplexity" in data["entities"], "perplexity entity should exist"
    entity = data["entities"]["perplexity"]
    assert MECHANISM_KEY in entity, f"{MECHANISM_KEY} should be under entities.perplexity"
    mech = entity[MECHANISM_KEY]
    assert mech["mechanism_id"] == MECHANISM_ID
    assert mech["iteration"] == 391
    assert mech["type"] == "C"
    assert mech["type_label"] == "financial_incentive_mapping"

def test_wired_yaml_mechanism_exists():
    data = load_yaml(WIRED_YAML)
    assert "competitor_relationships" in data
    cr = data["competitor_relationships"]
    assert MECHANISM_KEY in cr, f"{MECHANISM_KEY} should be in competitor_relationships"
    mech = cr[MECHANISM_KEY]
    assert mech["mechanism_id"] == MECHANISM_ID
    assert mech["iteration"] == 391

def test_source_provenance_https():
    data = load_yaml(COMPETITOR_YAML)
    mech = data["entities"]["perplexity"][MECHANISM_KEY]
    urls = mech.get("source_urls", [])
    assert len(urls) >= 3, "should have at least 3 source URLs"
    for url in urls:
        assert url.startswith("https://"), f"source URL should be https: {url}"
        assert "digiday.com" in url or "pymnts.com" in url or "ppc.land" in url or "adweek.com" in url, f"unexpected source domain: {url}"

def test_cautious_language_no_causal_claim():
    data = load_yaml(COMPETITOR_YAML)
    mech = data["entities"]["perplexity"][MECHANISM_KEY]
    note = mech.get("correlational_note", "")
    assert "correlational" in note.lower() or "does not by themselves demonstrate" in note or "does not imply" in note.lower()
    assert "causation" in note.lower() or "causal" in note.lower() or "editorial control" in note.lower()

def test_manual_illustrative_labeling_and_no_significance():
    data = load_yaml(WIRED_YAML)
    mech = data["competitor_relationships"][MECHANISM_KEY]
    # tone analysis should be labeled MANUAL ILLUSTRATIVE
    tone_result = mech.get("asymmetry_scorer_result", {})
    # Check methodology contains MANUAL ILLUSTRATIVE
    methodology = tone_result.get("methodology", "")
    assert "MANUAL ILLUSTRATIVE" in methodology or "MANUAL ILLUSTRATIVE" in str(tone_result.get("target_avg", "")) or "MANUAL ILLUSTRATIVE" in str(tone_result)
    # statistical claims should be not_calculated
    assert tone_result.get("p_value") == "not_calculated" or "not_calculated" in str(tone_result.get("p_value", ""))
    assert tone_result.get("significant") is False
    # No em dash in cautious_language (check for — character)
    cautious = mech.get("cautious_language", "")
    assert "—" not in cautious, "cautious_language should not contain em dash"
    assert "—" not in mech.get("overview", ""), "overview should not contain em dash"
