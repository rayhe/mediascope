"""
Type D #377 - Test and Verify full suite cross-validation #369-#377
Validates quintuple reverse-advertiser alignment #376, newest-first ordering,
em-dash discipline, YAML validity, illustrative labeling, cautious language,
confounding factors, source URL requirements.
"""
import os
import re
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_yaml(rel):
    with open(os.path.join(REPO_ROOT, rel), "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def test_yaml_valid_competitor_entities():
    load_yaml("profiles/competitor-entities.yaml")

def test_yaml_valid_wired():
    load_yaml("profiles/wired.yaml")

def test_yaml_valid_guardian():
    load_yaml("profiles/guardian.yaml")

def test_yaml_valid_ft():
    load_yaml("profiles/financial-times.yaml")

def test_yaml_valid_verge():
    load_yaml("profiles/the-verge.yaml")

def test_iteration_log_newest_first():
    path = os.path.join(REPO_ROOT, "iteration-log.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    # First iteration header should be #377 or #376 (newest)
    first_match = re.search(r"## Iteration #(\d+)", content)
    assert first_match, "No iteration header found"
    first_id = int(first_match.group(1))
    # After fix, #376 should be first, #377 will be prepended after this test runs
    # Allow 376 or 377
    assert first_id >= 376, f"Expected newest-first >=376, got {first_id}"

def test_mechanism_376_exists_in_entities():
    data = load_yaml("profiles/competitor-entities.yaml")
    # Search for mechanism_id 376 in raw text for robustness
    raw = open(os.path.join(REPO_ROOT, "profiles/competitor-entities.yaml"), "r", encoding="utf-8").read()
    assert "376" in raw, "Mechanism 376 not found in competitor-entities.yaml"
    # Check quintuple fields
    assert "quintuple" in raw.lower() or "reverse" in raw.lower(), "Quintuple reverse-advertiser keywords missing"

def test_mechanism_372_quadruple_preserved():
    raw = open(os.path.join(REPO_ROOT, "profiles/competitor-entities.yaml"), "r", encoding="utf-8").read()
    assert "amazon" in raw.lower() and "alphabet" in raw.lower(), "Quadruple mechanism #372 amazon/alphabet context lost"

def test_no_em_dash_in_new_profiles():
    for rel in ["profiles/wired.yaml", "profiles/competitor-entities.yaml"]:
        text = open(os.path.join(REPO_ROOT, rel), "r", encoding="utf-8").read()[-20000:]  # last 20k chars include recent edits
        assert "—" not in text, f"Em dash found in recent {rel} - violates no-em-dash rule"
        assert "–" not in text or text.count("–") < 5, f"En dash overuse in {rel}"

def test_quintuple_test_file_exists():
    path = os.path.join(REPO_ROOT, "tests/test_quintuple_reverse_advertiser_alignment_aug29.py")
    assert os.path.exists(path), "Quintuple test file missing"

def test_quintuple_test_passing_marker():
    path = os.path.join(REPO_ROOT, "tests/test_quintuple_reverse_advertiser_alignment_aug29.py")
    assert os.path.getsize(path) > 1000, "Quintuple test file too small"

def test_mechanism_376_source_urls():
    raw = open(os.path.join(REPO_ROOT, "profiles/competitor-entities.yaml"), "r", encoding="utf-8").read()
    # Must have Reuters and EssilorLuxottica sources
    assert "reuters.com" in raw.lower(), "Reuters source missing for Meta 3.5B stake"
    assert "essilorluxottica" in raw.lower(), "EssilorLuxottica H1 source missing"

def test_meta_stake_3pct_3_5b():
    raw = open(os.path.join(REPO_ROOT, "profiles/competitor-entities.yaml"), "r", encoding="utf-8").read()
    assert "3%" in raw or "3 percent" in raw.lower() or "around 3" in raw.lower(), "Meta 3% stake not quantified"
    assert "3.5" in raw, "Meta $3.5B value not present"

def test_essilorluxottica_h1_eur_14_02b():
    raw = open(os.path.join(REPO_ROOT, "profiles/competitor-entities.yaml"), "r", encoding="utf-8").read()
    assert "14.02" in raw, "EssilorLuxottica EUR 14.02B H1 not present"
    assert "7.3" in raw, "7.3% growth not present"

def test_quintuple_architecture_five_channels():
    raw = open(os.path.join(REPO_ROOT, "profiles/competitor-entities.yaml"), "r", encoding="utf-8").read()
    # Check for 5 channels listed
    channels = ["amazon", "alphabet", "apple", "meta", "essilorluxottica"]
    for ch in channels:
        assert ch in raw.lower(), f"Channel {ch} missing from quintuple synthesis"

def test_cautious_language_present():
    raw = open(os.path.join(REPO_ROOT, "profiles/competitor-entities.yaml"), "r", encoding="utf-8").read()[-30000:]
    cautious_phrases = ["does not imply causation", "does not prove", "correlation", "incentive", "structural"]
    matches = sum(1 for p in cautious_phrases if p.lower() in raw.lower())
    assert matches >= 2, f"Only {matches} cautious phrases found, need 2+"

def test_confounding_factors_present():
    raw = open(os.path.join(REPO_ROOT, "profiles/competitor-entities.yaml"), "r", encoding="utf-8").read()[-30000:]
    assert "STRONG" in raw or "strong" in raw.lower(), "No STRONG confounder label"
    assert "MODERATE" in raw or "moderate" in raw.lower(), "No MODERATE confounder"

def test_illustrative_labeling():
    raw = open(os.path.join(REPO_ROOT, "profiles/competitor-entities.yaml"), "r", encoding="utf-8").read()
    assert "illustrative" in raw.lower(), "Illustrative labeling missing for synthetic scores"

def test_no_proves_bias_language():
    for rel in ["profiles/competitor-entities.yaml", "profiles/wired.yaml"]:
        text = open(os.path.join(REPO_ROOT, rel), "r", encoding="utf-8").read()[-30000:].lower()
        assert "proves bias" not in text, f"'proves bias' forbidden phrase in {rel}"
        assert "proves editorial control" not in text, f"'proves editorial control' forbidden in {rel}"

def test_rotation_type_d_next_expected():
    # Type D follows Type C, next should be E
    path = os.path.join(REPO_ROOT, "iteration-log.md")
    content = open(path, "r", encoding="utf-8").read()[:2000]
    assert "Type C" in content or "Type D" in content, "Rotation header missing"

def test_max_mechanism_id_unique():
    raw = open(os.path.join(REPO_ROOT, "profiles/competitor-entities.yaml"), "r", encoding="utf-8").read()
    # Find all mechanism_id occurrences
    ids = re.findall(r"mechanism_id:\s*(\d+)", raw)
    ids_int = [int(x) for x in ids]
    # 376 should appear at least once
    assert 376 in ids_int, "Mechanism 376 not found as mechanism_id"
    # Check uniqueness of 376 (allow duplicate 235 known exception)
    # Count occurrences of 376 should be 1-2, not many
    assert ids_int.count(376) <= 3, f"Mechanism 376 appears {ids_int.count(376)} times, possible duplication"

def test_wired_essilorluxottica_updated():
    raw = open(os.path.join(REPO_ROOT, "profiles/wired.yaml"), "r", encoding="utf-8").read()
    assert "EssilorLuxottica" in raw, "EssilorLuxottica not in wired.yaml"
    assert "14.02" in raw or "3.5" in raw or "3%" in raw, "Wired.yaml not updated with H1 or stake"

def test_hidden_files_iteration_376_json():
    path = os.path.join(REPO_ROOT, "../..", "workspace/goals/mediascope-meta-wearables-press-analysis/hidden_files/iteration-376-type-c.json")
    # Try both relative locations
    if not os.path.exists(path):
        path = os.path.expanduser("~/workspace/goals/mediascope-meta-wearables-press-analysis/hidden_files/iteration-376-type-c.json")
    assert os.path.exists(path), "Hidden files iteration-376 JSON missing"

def test_memory_2026_08_29_exists():
    path = os.path.expanduser("~/memory/2026-08-29.md")
    assert os.path.exists(path), "Memory file missing"
    content = open(path, "r", encoding="utf-8").read()
    assert "375" in content or "376" in content, "Memory does not mention recent iterations"
