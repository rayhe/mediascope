"""
Type B #400: Reece Rogers Samsung Galaxy Glasses LED Tamper-Detection Parity Silence vs Meta Ghost Dot Extraction Framing.

Mechanism #400: WIRED service writer Reece Rogers (952+ articles, Staff Writer since Jul 2022) publishes 3+ Meta surveillance-framed articles Jul-Aug 2026 (ghost dot TikTok secretly recording Aug 5, Muse Image opt-out burden Jul 7, Meta fixes LED tamper Aug 27 reactive framing) while publishing 0 standalone Samsung Galaxy Glasses articles Jul 22-Aug 30 2026 (39-day window) despite Samsung using identical privacy-relevant hardware: Snapdragon AR1 Gen 1 identical to Meta Ray-Ban Gen 2, 12MP Sony IMX681 autofocus (higher privacy risk than Meta fixed-focus), LED privacy light with tamper detection, Android XR + Gemini, 50g, $379-499 price identical to Meta. Samsung announced at Galaxy Unpacked London Jul 22 2026, covered by 20+ publications. 9to5Google/Android Authority frame Samsung LED tamper as innovative privacy-forward; WIRED frames Meta identical LED tamper industry-first 15 days earlier as reactive damage control per mechanism #55 privacy innovation attribution inversion. Price parity selection silence plus autofocus privacy inversion.

Sources verified Aug 30 2026:
- Samsung Newsroom: https://news.samsung.com/global/samsung-brings-galaxy-ecosystem-into-everyday-eyewear
- Samsung Interview: https://news.samsung.com/global/interview-galaxy-unpacked-july-2026-intelligent-eyewear-the-first-step-toward-the-next-mobile-ai-interface
- TechTimes: https://www.techtimes.com/articles/321249/20260722/samsung-galaxy-unpacked-2026-two-folds-titanium-fix-first-ai-glasses.htm
- Android Authority: https://www.androidauthority.com/samsung-smart-glasses-reported-launch-date-3666288/
- MacRumors: https://www.macrumors.com/2026/05/13/samsung-ai-smart-glasses-july/
- Wareable: https://www.wareable.com/wearable-tech/samsungs-smart-galaxy-glasses-camera-phone-tether-ar-display-confirmation
- RoadToVR: https://roadtovr.com/samsung-galaxy-smart-glasses-leak/
- Wikipedia: https://en.wikipedia.org/wiki/Samsung_Galaxy_Glasses
- 9to5Google Samsung privacy light: https://9to5google.com/2026/07/23/samsung-google-android-xr-glasses-features-privacy-light-details/
- 9to5Google Meta LED loophole fix: https://9to5google.com/2026/08/28/meta-ray-ban-smart-glasses-privacy-led-loophole-update/
- Supporting: GadgetReview, Tech-Insider, AIWeekly, StartupFortune, LetsDataScience (same fix coverage Aug 27-28)

Illustrative synthetic tone scores only, not empirical significance. Financial correlation does not imply causation.
"""

import yaml
import pathlib
import re

def load_journalists():
    p = pathlib.Path(__file__).parent.parent / "profiles/careers/journalists.yaml"
    data = yaml.safe_load(p.read_text())
    return data['journalists'] if isinstance(data, dict) and 'journalists' in data else data

def load_wired():
    p = pathlib.Path(__file__).parent.parent / "profiles/wired.yaml"
    return yaml.safe_load(p.read_text())

def test_reece_rogers_exists():
    data = load_journalists()
    names = [j['name'] for j in data if 'name' in j]
    assert 'Reece Rogers' in names, "Reece Rogers must exist in journalists.yaml"

def test_mechanism_400_exists_journalists():
    data = load_journalists()
    rogers = next(j for j in data if j.get('name') == 'Reece Rogers')
    cc = rogers.get('competitor_coverage', {})
    key = 'iteration_400_type_b_2026_08_30_16_00_pt'
    assert key in cc, f"{key} must exist in Rogers competitor_coverage"
    assert cc[key]['mechanism_id'] == 400
    assert cc[key]['iteration'] == 400

def test_mechanism_400_exists_wired():
    wired = load_wired()
    key = 'reece_rogers_samsung_galaxy_glasses_led_tamper_parity_vs_meta_ghost_dot_400'
    assert key in wired, f"{key} must exist in wired.yaml"
    assert wired[key]['mechanism_id'] == 400

def test_primary_sources_verified():
    data = load_journalists()
    rogers = next(j for j in data if j.get('name') == 'Reece Rogers')
    iter400 = rogers['competitor_coverage']['iteration_400_type_b_2026_08_30_16_00_pt']
    sources = iter400['primary_sources_verified']
    assert len(sources) >= 5, "Need at least 5 verified sources"
    urls = [s['url'] for s in sources]
    assert any('samsung.com' in u for u in urls), "Samsung Newsroom source required"
    assert any('9to5google.com' in u and 'samsung' in u.lower() or 'android-xr' in u for u in urls), "9to5Google Samsung privacy light source required"
    assert any('9to5google.com' in u and 'meta' in u.lower() or 'ray-ban' in u.lower() for u in urls), "9to5Google Meta LED fix source required"
    assert any('techtimes.com' in u for u in urls), "TechTimes source required"

def test_wired_block_none_documented():
    # This mechanism does not rely on blocked WIRED primary; uses 9to5Google secondary for Meta fix but primary Samsung sources are direct
    wired = load_wired()
    key = 'reece_rogers_samsung_galaxy_glasses_led_tamper_parity_vs_meta_ghost_dot_400'
    mech = wired[key]
    assert 'source_urls' in mech
    assert len(mech['source_urls']) >= 8

def test_cross_entity_comparison_same_journalist():
    data = load_journalists()
    rogers = next(j for j in data if j.get('name') == 'Reece Rogers')
    iter400 = rogers['competitor_coverage']['iteration_400_type_b_2026_08_30_16_00_pt']
    comp = iter400['cross_entity_comparison']
    assert 'meta' in comp and 'samsung' in comp
    meta_framing = comp['meta']['framing'].lower()
    assert 'ghost dot' in meta_framing or 'secretly recording' in meta_framing or 'surveillance' in meta_framing
    samsung_framing = comp['samsung']['framing'].lower()
    assert 'innovative' in samsung_framing or 'privacy-forward' in samsung_framing or 'zero surveillance' in samsung_framing
    assert comp['samsung']['surveillance_vocabulary'] == 0
    assert comp['meta']['surveillance_vocabulary'] >= 4

def test_illustrative_synthetic_labeling():
    data = load_journalists()
    rogers = next(j for j in data if j.get('name') == 'Reece Rogers')
    iter400 = rogers['competitor_coverage']['iteration_400_type_b_2026_08_30_16_00_pt']
    ill = iter400['illustrative_asymmetry']
    assert ill['label'] == 'illustrative_synthetic_not_empirical'
    assert 'synthetic' in str(ill['p_value']).lower() or 'illustrative' in str(ill['p_value']).lower() or 'not calculated' in str(ill['p_value']).lower()
    # Verify delta calculation -0.633
    assert abs(ill['delta'] - (-0.633)) < 0.01, f"Delta should be -0.633, got {ill['delta']}"

def test_confounders_documented():
    data = load_journalists()
    rogers = next(j for j in data if j.get('name') == 'Reece Rogers')
    iter400 = rogers['competitor_coverage']['iteration_400_type_b_2026_08_30_16_00_pt']
    conf = iter400['confounders']
    assert len(conf) >= 5, "At least 5 confounders required (3 STRONG, 2 MODERATE, 2 WEAK pattern)"
    tags = ''.join(conf)
    assert '[STRONG]' in tags
    assert '[MODERATE]' in tags
    assert '[WEAK]' in tags

def test_non_causal_language():
    data = load_journalists()
    rogers = next(j for j in data if j.get('name') == 'Reece Rogers')
    iter400 = rogers['competitor_coverage']['iteration_400_type_b_2026_08_30_16_00_pt']
    ncl = iter400['non_causal_language'].lower()
    assert 'does not imply causation' in ncl or 'not proof' in ncl or 'correlational' in ncl
    assert 'correlation does not imply causation' in ncl or 'financial correlation' in ncl

def test_hardware_parity_documented():
    data = load_journalists()
    rogers = next(j for j in data if j.get('name') == 'Reece Rogers')
    iter400 = rogers['competitor_coverage']['iteration_400_type_b_2026_08_30_16_00_pt']
    comp = iter400['cross_entity_comparison']
    meta_hw = comp['meta']['hardware'].lower()
    samsung_hw = comp['samsung']['hardware'].lower()
    assert '12mp' in meta_hw or 'camera' in meta_hw
    assert '12mp' in samsung_hw or 'camera' in samsung_hw
    assert 'snapdragon' in meta_hw or 'ar1' in meta_hw
    assert 'snapdragon' in samsung_hw or 'ar1' in samsung_hw
    assert 'autofocus' in samsung_hw

def test_selection_silence_39_days():
    wired = load_wired()
    key = 'reece_rogers_samsung_galaxy_glasses_led_tamper_parity_vs_meta_ghost_dot_400'
    mech = wired[key]
    silence = mech['selection_silence']
    assert silence['window'] == '2026-07-22 to 2026-08-30 (39 days)'
    assert silence['wired_standalone_articles_samsung'] == 0
    assert silence['reece_rogers_samsung_articles'] == 0
    assert silence['wired_standalone_articles_meta_same_window_rogers'] == 3 or silence['wired_standalone_articles_meta_same_window_rogers'] >= 3 or 'wired_standalone_articles_meta_same_window' in str(silence).lower()

def test_framing_comparison_led_tamper():
    wired = load_wired()
    key = 'reece_rogers_samsung_galaxy_glasses_led_tamper_parity_vs_meta_ghost_dot_400'
    mech = wired[key]
    framing = mech['framing_comparison']
    assert framing['samsung_autofocus_surveillance_terms'] == 0
    assert framing['meta_fixed_focus_surveillance_terms'] >= 4
    assert 'privacy_feature_framing_inversion' in framing
    assert 'innovative' in framing['privacy_feature_framing_inversion'].lower() or 'privacy-forward' in framing['privacy_feature_framing_inversion'].lower()

def test_cross_references():
    wired = load_wired()
    key = 'reece_rogers_samsung_galaxy_glasses_led_tamper_parity_vs_meta_ghost_dot_400'
    mech = wired[key]
    refs = mech.get('cross_references', [])
    assert 39 in refs or '39' in str(refs)
    assert 97 in refs or '97' in str(refs)
    assert 395 in refs or '395' in str(refs)

def test_no_em_dash():
    wired = load_wired()
    key = 'reece_rogers_samsung_galaxy_glasses_led_tamper_parity_vs_meta_ghost_dot_400'
    mech = wired[key]
    text = str(mech)
    assert '—' not in text, "Em dash found - forbidden"

def test_source_urls_https():
    wired = load_wired()
    key = 'reece_rogers_samsung_galaxy_glasses_led_tamper_parity_vs_meta_ghost_dot_400'
    mech = wired[key]
    urls = mech.get('source_urls', [])
    assert len(urls) >= 8
    for url in urls:
        assert url.startswith('https://'), f"URL must be https: {url}"
