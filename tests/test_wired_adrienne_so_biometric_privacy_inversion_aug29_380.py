"""
Test Mechanism #380: WIRED Adrienne So Biometric Privacy Inversion + Proactive Remediation Silence

Type B: Journalist Cross-Entity Tracking Extension — Aug 29, 2026

KEY FINDING: WIRED wearables reporter Adrienne So demonstrates entity-selective
privacy vocabulary that inverts biometric sensitivity ranking, and extends coverage
selection silence to proactive Meta privacy engineering (Aug 27-28 second LED fix).

- Meta Oakley Vanguard (camera glasses, 12-MP, 32GB, NO biometric health sensors) receives
  explicit parenthetical privacy attack "(which are garbage)" in Oct 2025 review.
  Techmeme headline: "camera specs aren't too impressive" despite positive body
  ("sound amazing," "might just replace your action cam").

- Google Pixel Watch 4 (heart rate, blood oxygen, sleep stages, GPS, menstrual cycles
  feeding Health Connect / advertising ecosystem) receives ZERO privacy caveats and
  promotional "Surprisingly Close" framing to Apple Watch Ultra.

- Meta Aug 27-28 2026 second LED-cover loophole closure (Ray-Ban Meta / Oakley Meta
  now stop recording when LED covered, per Alex Himel quote) — proactive privacy
  engineering, second fix in <2 months — receives ZERO WIRED Adrienne So coverage
  Aug 27-29, despite wearables / smart glasses beat.

- Same zero-coverage pattern for Samsung Galaxy Glasses (Jul 22 2026 launch, identical
  camera hardware), OpenAI ambient camera device (2026 development), Apple camera
  AirPods macOS Tahoe leak Aug 18 (mechanism #207, 4.6M views).

This extends WIRED privacy vocabulary bifurcation pattern (Chokkattu #93, Ashworth
#73/#87, Rogers #97) to include proactive remediation silence, establishing
that adversarial framing is not just tone but coverage selection: fix ignored,
competitor equivalent ignored, only Meta receives privacy attack.

FINANCIAL CAUTION: No causal claim from financial relationships. WIRED Condé Nast
$0 Meta licensing reported, Google search traffic dependence (CNET precedent #106)
may predict softer Google coverage, but structural incentive not proof of capture.
All asymmetry scores are SYNTHETIC ILLUSTRATIVE ONLY — manual approximations.

CONFOUNDERS: See journalists.yaml entry for full list.
"""

import yaml
from pathlib import Path
import pytest

JOURNALISTS_YAML = Path(__file__).parent.parent / "profiles" / "careers" / "journalists.yaml"

def load_journalists():
    with open(JOURNALISTS_YAML) as f:
        data = yaml.safe_load(f)
    return data.get('journalists', data)

def get_adrienne_so():
    js = load_journalists()
    for j in js:
        if j.get('name') == 'Adrienne So':
            return j
    raise AssertionError("Adrienne So not found in journalists.yaml")

def test_yaml_parseable():
    js = load_journalists()
    assert len(js) >= 4

def test_adrienne_so_exists():
    j = get_adrienne_so()
    assert j['name'] == 'Adrienne So'
    assert 'WIRED' in [p['name'] for p in j['publications']]

def test_mechanism_380_exists():
    j = get_adrienne_so()
    key = 'mechanism_380_meta_led_fix_proactive_privacy_silence_aug29'
    assert key in j, f"Missing {key}"
    m = j[key]
    assert m['discovery_date'] == '2026-08-29'
    assert m['iteration'] == 380
    assert 'biometric_privacy_inversion' in m['pattern']

def test_mechanism_380_primary_source_url_exact():
    j = get_adrienne_so()
    m = j['mechanism_380_meta_led_fix_proactive_privacy_silence_aug29']
    primary = m['meta_coverage_aug27_28']['source_url_primary']
    assert primary == 'https://www.engadget.com/2245776/meta-closing-loophole-that-allowed-people-to-record-with-smart-glasses-light-covered/'
    assert primary.startswith('https://')

def test_mechanism_380_language_verbatim_no_em_dashes():
    j = get_adrienne_so()
    m = j['mechanism_380_meta_led_fix_proactive_privacy_silence_aug29']
    phrases = m['meta_coverage_aug27_28']['framing_in_sources']['language_verbatim']
    assert 'yet another change' in phrases
    assert 'second time in less than two months' in phrases
    assert 'growing backlash' in phrases
    # No em dashes in any stored string
    for p in phrases:
        assert '—' not in p, f"Em dash found in phrase: {p}"
    desc = m['description']
    assert '—' not in desc

def test_mechanism_380_competitor_zero_coverage():
    j = get_adrienne_so()
    m = j['mechanism_380_meta_led_fix_proactive_privacy_silence_aug29']
    comp = m['competitor_coverage_zero']
    assert comp['samsung_galaxy_glasses']['wired_adrienne_so_coverage'] == 'ZERO (Jul 22 - Aug 29 2026)'
    assert comp['openai_ambient_device']['wired_adrienne_so_coverage'] == 'ZERO'
    assert 'ZERO' in comp['apple_camera_airpods']['wired_adrienne_so_coverage']

def test_mechanism_380_existing_bifurcation_referenced():
    j = get_adrienne_so()
    m = j['mechanism_380_meta_led_fix_proactive_privacy_silence_aug29']
    ref = m['existing_bifurcation_referenced']
    assert 'mechanism_102' in ref
    assert 'mechanism_207' in ref
    assert '(which are garbage)' in ref['mechanism_102'] or 'garbage' in ref['mechanism_102']

def test_mechanism_380_synthetic_labeling_present():
    j = get_adrienne_so()
    m = j['mechanism_380_meta_led_fix_proactive_privacy_silence_aug29']
    scorer = m['asymmetry_scorer_result_2026_08_29']
    assert 'SYNTHETIC ILLUSTRATIVE ONLY' in scorer['label']
    assert 'Synthetic illustrative only' in scorer['methodology'] or 'Synthetic illustrative' in scorer['methodology']
    assert scorer['target_entity'] == 'meta'
    assert 'google' in scorer['peer_entities']
    assert scorer['period_start'] == '2025-10-01'

def test_mechanism_380_financial_caution_and_confounders():
    j = get_adrienne_so()
    m = j['mechanism_380_meta_led_fix_proactive_privacy_silence_aug29']
    assert 'No causal claim' in m['financial_relationship_caution']
    assert 'structural incentives' in m['financial_relationship_caution'] or 'structural incentive' in m['financial_relationship_caution']
    confs = m['confounders']
    assert len(confs) >= 3
    # Must include strong confounder about editorial cycle or installed base
    joined = ' '.join(confs)
    assert 'editorial cycle' in joined or 'installed base' in joined or 'public interest' in joined
    counters = m['counterexamples']
    assert len(counters) >= 2

def test_mechanism_380_source_urls_exact():
    j = get_adrienne_so()
    m = j['mechanism_380_meta_led_fix_proactive_privacy_silence_aug29']
    urls = m['source_urls']
    assert 'https://www.techmeme.com/251021/p19' in urls
    assert 'https://www.engadget.com/2245776/meta-closing-loophole-that-allowed-people-to-record-with-smart-glasses-light-covered/' in urls
    for u in urls:
        assert u.startswith('https://'), f"URL must be https: {u}"
        assert '—' not in u

def test_asymmetry_scorer_pipeline_valid():
    """Validate asymmetry scorer runs with synthetic data, illustrative only."""
    from mediascope.score.asymmetry import calculate_asymmetry
    from datetime import datetime
    j = get_adrienne_so()
    m = j['mechanism_380_meta_led_fix_proactive_privacy_silence_aug29']
    scorer = m['asymmetry_scorer_result_2026_08_29']
    result = calculate_asymmetry(
        target_scores=scorer['target_scores_synthetic'],
        peer_scores=scorer['peer_scores_synthetic'],
        target_entity=scorer['target_entity'],
        peer_entities=scorer['peer_entities'],
        publication_slug=scorer['publication'],
        period_start=datetime(2025, 10, 1),
        period_end=datetime(2026, 8, 29),
    )
    # Illustrative check: target avg should be negative relative to peers in this synthetic set
    assert result.asymmetry_score < 0
    assert result.article_count_target == len(scorer['target_scores_synthetic'])
    assert result.article_count_peers == len(scorer['peer_scores_synthetic'])
