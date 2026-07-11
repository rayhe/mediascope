"""
Tests for Guardian Cohere lawsuit correction and Observer/Tortoise completion.
Type C: Ownership & Funding Deep Dive — Jul 11, 2026 03:00 PT.
"""
import yaml
import os
import re

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_guardian():
    with open(os.path.join(PROFILES_DIR, 'guardian.yaml'), 'r') as f:
        return yaml.safe_load(f)


def test_guardian_cohere_lawsuit_documented():
    """Guardian must be documented as a Cohere lawsuit plaintiff."""
    data = load_guardian()
    yaml_str = yaml.dump(data)
    assert 'Cohere' in yaml_str, "Cohere lawsuit must be referenced in Guardian profile"
    assert '1:25-cv-01305' in yaml_str, "Cohere case number must be documented"


def test_guardian_triple_path_strategy():
    """Guardian's AI strategy must be characterized as triple-path, not licensing-only."""
    data = load_guardian()
    yaml_str = yaml.dump(data)
    assert 'triple_path_ai_strategy' in yaml_str, \
        "Guardian must be classified as triple_path_ai_strategy, not strategic_licensing_over_litigation"
    assert 'strategic_licensing_over_litigation' not in yaml_str, \
        "Old incorrect classification must be removed"


def test_cohere_mtd_denied():
    """Cohere motion to dismiss denial must be documented."""
    data = load_guardian()
    yaml_str = yaml.dump(data)
    assert 'McMahon' in yaml_str, "Judge McMahon must be referenced"
    assert '2025-11-13' in yaml_str or 'Nov 13, 2025' in yaml_str, \
        "MTD denial date must be documented"


def test_observer_transfer_date():
    """Observer transfer to Tortoise must have exact completion date."""
    data = load_guardian()
    tortoise = data.get('tortoise_media_observer', {})
    assert tortoise.get('transfer_completed') == '2025-04-22', \
        "Observer transfer completion date must be April 22, 2025"
    assert tortoise.get('deal_announced') == '2024-12-06', \
        "Observer deal announcement date must be December 6, 2024"


def test_richard_furness_migration():
    """Richard Furness GMG-to-Tortoise personnel migration must be documented."""
    data = load_guardian()
    yaml_str = yaml.dump(data)
    assert 'Furness' in yaml_str, "Richard Furness must be referenced"
    # Check for co-CEO role (hyphenation varies in yaml serialization)
    lower = yaml_str.lower()
    assert 'co-ceo' in lower or 'co_ceo' in lower or 'coceo' in lower or 'co ceo' in lower, \
        "Furness role at Tortoise must be documented"


def test_brittin_bbc_channel4():
    """Brittin's BBC-Channel 4 partnership proposal must be documented."""
    data = load_guardian()
    yaml_str = yaml.dump(data)
    assert 'Channel 4' in yaml_str, "BBC-Channel 4 partnership talks must be referenced"
    assert 'subscale' in yaml_str, "Brittin's 'subscale' characterization must be included"


def test_nyt_openai_sanctions_cross_reference():
    """NYT v OpenAI sanctions motion must be cross-referenced."""
    data = load_guardian()
    yaml_str = yaml.dump(data)
    assert 'MDL 3143' in yaml_str or '1:25-md-03143' in yaml_str, \
        "NYT v OpenAI MDL case must be cross-referenced"


def test_cohere_co_plaintiffs_include_key_publications():
    """Co-plaintiffs list must include key tracked publications."""
    data = load_guardian()
    # Check in the raw YAML file since accented chars can be escaped in yaml.dump
    with open(os.path.join(PROFILES_DIR, 'guardian.yaml'), 'r') as f:
        raw = f.read()
    # Condé Nast and Atlantic are both Cohere co-plaintiffs and tracked publications
    assert 'Cond' in raw and 'Nast' in raw, "Condé Nast must be referenced"
    assert 'Atlantic' in raw, "The Atlantic must be referenced"
