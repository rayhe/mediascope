"""
MIT Technology Review × Apple — WWDC 2026 PCC-to-Google-Cloud Privacy Shift Omission
Type A deep dive, Aug 11 2026

Mechanism #41: MIT TR covered Apple's 2024 WWDC PCC announcement favorably, published
a Meta-Anduril warfare glasses alarm piece 3 weeks before Apple's WWDC 2026, but did
NOT cover the major WWDC 2026 shift of Private Cloud Compute to Google Cloud — a
fundamental change to the privacy architecture MIT TR previously praised. Simultaneously,
Apple's three camera-equipped AI wearables (smart glasses, AirPods, pendant) receive
zero surveillance framing from MIT TR, while Meta's glasses receive "warfare" and
"cyborg" language.

Key governance conflict: Kate Bergeron (Apple VP Hardware Engineering) was elected
MIT Corporation term member effective July 1, 2026 — deepening the Apple-MIT
institutional tie during the exact period MIT TR skipped covering Apple's privacy shift.
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
REPO_ROOT = os.path.join(os.path.dirname(__file__), '..')


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def research():
    return load_yaml('competitor-coverage-research.yaml')


@pytest.fixture(scope='module')
def mit_profile():
    return load_yaml('mit-tech-review.yaml')


@pytest.fixture(scope='module')
def entities():
    return load_yaml('competitor-entities.yaml')


@pytest.fixture(scope='module')
def mit_tr_section(research):
    return research['publications']['mit-tech-review']


# ===================================================================
# 1. WWDC 2024 BASELINE: MIT TR COVERED APPLE PCC FAVORABLY
# ===================================================================

class TestWWDC2024Baseline:
    """MIT TR published a favorable Apple PCC piece at WWDC 2024."""

    def test_wwdc_2024_apple_article_exists(self, mit_tr_section):
        examples = mit_tr_section.get('apple_examples', [])
        wwdc_2024 = [e for e in examples if '2024-06' in str(e.get('date', ''))]
        assert len(wwdc_2024) >= 1, "Expected at least one June 2024 Apple article"

    def test_wwdc_2024_article_tone_positive(self, mit_tr_section):
        examples = mit_tr_section.get('apple_examples', [])
        wwdc_2024 = [e for e in examples if '2024-06' in str(e.get('date', ''))]
        if wwdc_2024:
            assert wwdc_2024[0]['tone'] > 0, "WWDC 2024 article should have positive tone"

    def test_wwdc_2024_article_mentions_pcc(self, mit_tr_section):
        examples = mit_tr_section.get('apple_examples', [])
        wwdc_2024 = [e for e in examples if '2024-06' in str(e.get('date', ''))]
        if wwdc_2024:
            text = str(wwdc_2024[0]).lower()
            assert 'private cloud compute' in text or 'pcc' in text or 'cloud' in text

    def test_wwdc_2024_article_explicitly_names_meta_negatively(self, mit_tr_section):
        """The 2024 piece used Meta as a privacy-negative comparator."""
        examples = mit_tr_section.get('apple_examples', [])
        wwdc_2024 = [e for e in examples if '2024-06' in str(e.get('date', ''))]
        if wwdc_2024:
            text = str(wwdc_2024[0]).lower()
            assert 'meta' in text, "2024 article named Meta as privacy counterexample"

    def test_wwdc_2024_article_source_url(self, mit_tr_section):
        examples = mit_tr_section.get('apple_examples', [])
        wwdc_2024 = [e for e in examples if '2024-06' in str(e.get('date', ''))]
        if wwdc_2024:
            url = wwdc_2024[0].get('source_url', '')
            assert 'technologyreview.com' in url


# ===================================================================
# 2. WWDC 2026 OMISSION: PCC-TO-GOOGLE-CLOUD NOT COVERED
# ===================================================================

class TestWWDC2026Omission:
    """MIT TR did not cover Apple's WWDC 2026 PCC-to-Google-Cloud shift."""

    def test_wwdc_2026_omission_documented(self, mit_tr_section):
        omission = mit_tr_section.get('wwdc_2026_pcc_omission', {})
        assert omission, "WWDC 2026 PCC omission should be documented"

    def test_wwdc_2026_event_date(self, mit_tr_section):
        omission = mit_tr_section['wwdc_2026_pcc_omission']
        assert omission['event_date'] == '2026-06-08'

    def test_wwdc_2026_pcc_shift_described(self, mit_tr_section):
        omission = mit_tr_section['wwdc_2026_pcc_omission']
        text = omission['privacy_shift_description'].lower()
        assert 'google cloud' in text or 'google' in text

    def test_wwdc_2026_coverage_status_absent(self, mit_tr_section):
        omission = mit_tr_section['wwdc_2026_pcc_omission']
        status = omission['mit_tr_coverage_status'].lower()
        assert 'not found' in status or 'absent' in status or 'none' in status

    def test_wwdc_2026_other_outlets_covered(self, mit_tr_section):
        omission = mit_tr_section['wwdc_2026_pcc_omission']
        others = omission.get('outlets_that_covered', [])
        assert len(others) >= 3, "At least 3 other outlets covered WWDC 2026 PCC shift"

    def test_wwdc_2026_privacy_shift_is_material(self, mit_tr_section):
        """PCC moving to Google Cloud is material because MIT TR praised Apple-only PCC."""
        omission = mit_tr_section['wwdc_2026_pcc_omission']
        text = omission['materiality_rationale'].lower()
        assert 'previously praised' in text or '2024' in text or 'prior coverage' in text


# ===================================================================
# 3. META-ANDURIL WARFARE GLASSES CONTRAST
# ===================================================================

class TestAndurilMetaContrast:
    """MIT TR covered Meta-Anduril warfare glasses with alarm framing."""

    def test_anduril_article_exists(self, mit_tr_section):
        meta_examples = mit_tr_section.get('meta_examples', [])
        anduril = [e for e in meta_examples if 'anduril' in str(e).lower()]
        assert len(anduril) >= 1, "Meta-Anduril warfare glasses article should be documented"

    def test_anduril_article_date_before_wwdc_2026(self, mit_tr_section):
        meta_examples = mit_tr_section.get('meta_examples', [])
        anduril = [e for e in meta_examples if 'anduril' in str(e).lower()]
        if anduril:
            date = str(anduril[0].get('date', ''))
            assert '2026-05' in date, "Anduril piece was May 2026, before WWDC 2026"

    def test_anduril_article_alarm_language(self, mit_tr_section):
        meta_examples = mit_tr_section.get('meta_examples', [])
        anduril = [e for e in meta_examples if 'anduril' in str(e).lower()]
        if anduril:
            text = str(anduril[0]).lower()
            alarm_words = ['warfare', 'cyborg', 'weapon', 'drone strike', 'massive new risks']
            found = [w for w in alarm_words if w in text]
            assert len(found) >= 1, f"Expected alarm language, found: {found}"

    def test_temporal_proximity(self, mit_tr_section):
        """Anduril piece (May 18) was ~21 days before WWDC 2026 (June 8)."""
        omission = mit_tr_section.get('wwdc_2026_pcc_omission', {})
        assert omission.get('days_after_anduril_piece', 0) >= 20


# ===================================================================
# 4. APPLE WEARABLES PRIVACY SILENCE
# ===================================================================

class TestAppleWearablesPrivacySilence:
    """MIT TR has not applied surveillance language to Apple's AI wearables."""

    def test_apple_wearables_section_exists(self, mit_tr_section):
        section = mit_tr_section.get('apple_wearables_privacy_silence', {})
        assert section, "Apple wearables privacy silence should be documented"

    def test_apple_three_camera_wearables_listed(self, mit_tr_section):
        section = mit_tr_section['apple_wearables_privacy_silence']
        devices = section.get('apple_camera_wearables', [])
        assert len(devices) >= 3, "Should list at least 3 Apple camera wearables"

    def test_apple_smart_glasses_in_list(self, mit_tr_section):
        section = mit_tr_section['apple_wearables_privacy_silence']
        devices = section.get('apple_camera_wearables', [])
        names = [d.get('name', '').lower() for d in devices]
        assert any('glass' in n for n in names), "Smart glasses should be listed"

    def test_apple_airpods_camera_in_list(self, mit_tr_section):
        section = mit_tr_section['apple_wearables_privacy_silence']
        devices = section.get('apple_camera_wearables', [])
        names = [d.get('name', '').lower() for d in devices]
        assert any('airpod' in n for n in names), "Camera AirPods should be listed"

    def test_apple_pendant_in_list(self, mit_tr_section):
        section = mit_tr_section['apple_wearables_privacy_silence']
        devices = section.get('apple_camera_wearables', [])
        names = [d.get('name', '').lower() for d in devices]
        assert any('pendant' in n or 'pin' in n for n in names), "AI pendant should be listed"

    def test_zero_surveillance_language_from_mit_tr(self, mit_tr_section):
        section = mit_tr_section['apple_wearables_privacy_silence']
        status = section.get('mit_tr_surveillance_language_applied', '')
        assert status.lower() in ('none', 'zero', 'absent')

    def test_meta_glasses_receive_surveillance_language(self, mit_tr_section):
        section = mit_tr_section['apple_wearables_privacy_silence']
        meta_lang = section.get('meta_glasses_surveillance_language_examples', [])
        assert len(meta_lang) >= 1, "Meta glasses received surveillance/alarm language"


# ===================================================================
# 5. GOVERNANCE TIMING — BERGERON ELECTION + COVERAGE GAP
# ===================================================================

class TestGovernanceTimingConflict:
    """Kate Bergeron's election deepens conflict during the coverage gap period."""

    def test_bergeron_election_date_during_gap(self, mit_tr_section):
        gov = mit_tr_section.get('apple_governance_conflict', {}).get('bergeron_election', {})
        assert gov.get('effective_date') == '2026-07-01'

    def test_bergeron_is_hardware_engineering_vp(self, mit_tr_section):
        gov = mit_tr_section['apple_governance_conflict']['bergeron_election']
        assert 'Hardware Engineering' in gov.get('title_at_apple', '')

    def test_bergeron_wearables_relevance(self, mit_tr_section):
        gov = mit_tr_section['apple_governance_conflict']['bergeron_election']
        text = gov.get('wearables_relevance', '').lower()
        assert 'glass' in text or 'wearable' in text or 'vision' in text

    def test_csail_alliance_undisclosed(self, mit_tr_section):
        csail = mit_tr_section['apple_governance_conflict'].get('csail_alliance', {})
        assert csail.get('disclosed_in_coverage', False) is False

    def test_governance_deepens_during_omission_window(self, mit_tr_section):
        """Bergeron election (Jul 1) is AFTER WWDC 2026 (Jun 8) but during the
        period MIT TR would have published follow-up analysis."""
        omission = mit_tr_section.get('wwdc_2026_pcc_omission', {})
        text = omission.get('governance_timing_note', '').lower()
        assert 'bergeron' in text or 'governance' in text


# ===================================================================
# 6. CONFOUNDING FACTORS
# ===================================================================

class TestConfoundingFactors:
    """Document legitimate editorial factors."""

    def test_confounding_factors_listed(self, mit_tr_section):
        omission = mit_tr_section.get('wwdc_2026_pcc_omission', {})
        factors = omission.get('confounding_factors', [])
        assert len(factors) >= 3, "Should have at least 3 confounding factors"

    @pytest.mark.parametrize("keyword", [
        "newsletter",
        "editorial",
        "pre-announcement",
    ])
    def test_confounding_factor_types(self, mit_tr_section, keyword):
        omission = mit_tr_section.get('wwdc_2026_pcc_omission', {})
        factors = omission.get('confounding_factors', [])
        text = ' '.join(str(f).lower() for f in factors)
        assert keyword in text, f"Confounding factors should mention '{keyword}'"


# ===================================================================
# 7. MECHANISM #41 STRUCTURAL VALIDATION
# ===================================================================

class TestMechanism41Structure:
    """Validate mechanism #41 is properly registered."""

    def test_mechanism_id_is_41(self, mit_tr_section):
        omission = mit_tr_section.get('wwdc_2026_pcc_omission', {})
        assert omission.get('mechanism_id') == 41

    def test_finding_summary_exists(self, mit_tr_section):
        omission = mit_tr_section.get('wwdc_2026_pcc_omission', {})
        assert len(omission.get('finding_summary', '')) > 50

    def test_test_file_reference(self, mit_tr_section):
        omission = mit_tr_section.get('wwdc_2026_pcc_omission', {})
        assert 'test_mit_tr_apple_wwdc_2026' in omission.get('test_file', '')

    def test_finding_type_is_coverage_selection(self, mit_tr_section):
        omission = mit_tr_section.get('wwdc_2026_pcc_omission', {})
        ftype = omission.get('finding_type', '').lower()
        assert 'coverage_selection' in ftype or 'omission' in ftype


# ===================================================================
# 8. CROSS-MECHANISM VALIDATION
# ===================================================================

class TestCrossMechanismValidation:
    """Validate mechanism #41 extends existing MIT TR Apple findings."""

    def test_extends_governance_conflict(self, mit_tr_section):
        """Mechanism #41 should reference the existing governance conflict."""
        omission = mit_tr_section.get('wwdc_2026_pcc_omission', {})
        refs = omission.get('cross_references', [])
        text = ' '.join(str(r).lower() for r in refs)
        assert 'governance' in text or 'bergeron' in text

    def test_extends_sensor_count_paradox(self, mit_tr_section):
        """Should reference the sensor-count paradox (Apple Vision Pro 12 cameras)."""
        omission = mit_tr_section.get('wwdc_2026_pcc_omission', {})
        refs = omission.get('cross_references', [])
        text = ' '.join(str(r).lower() for r in refs)
        assert 'sensor' in text or 'vision pro' in text or 'camera' in text

    def test_mechanism_count_at_least_41(self, research):
        """Total mechanism IDs should be at least 41."""
        import re
        text = yaml.dump(research, default_flow_style=False)
        ids = set()
        for m in re.finditer(r'mechanism_id:\s*(\d+)', text):
            ids.add(int(m.group(1)))
        assert max(ids) >= 41


# ===================================================================
# 9. COVERAGE SELECTION PATTERN
# ===================================================================

class TestCoverageSelectionPattern:
    """Validate the coverage selection pattern across MIT TR."""

    def test_meta_coverage_count_exceeds_apple(self, mit_tr_section):
        """MIT TR covers Meta more than Apple (quantity asymmetry)."""
        meta_count = len(mit_tr_section.get('meta_examples', []))
        apple_count = len(mit_tr_section.get('apple_examples', []))
        assert meta_count >= apple_count, "Meta coverage quantity should exceed Apple"

    def test_meta_tone_negative_apple_positive(self, mit_tr_section):
        """Overall tone delta: Meta negative, Apple positive."""
        meta_tone = float(mit_tr_section.get('meta_coverage_tone_score', 0) or 0)
        apple_tone = float(mit_tr_section.get('apple_coverage_tone_score', 0) or 0)
        # Meta tone should be more negative than Apple tone
        assert meta_tone < apple_tone or (
            mit_tr_section.get('meta_coverage_tone', '').lower() in ('negative', 'adversarial') and
            mit_tr_section.get('apple_coverage_tone', '').lower() in ('positive', 'neutral')
        )

    def test_apple_wwdc_coverage_rate(self, mit_tr_section):
        """MIT TR covered Apple WWDC 2024 but not 2026."""
        omission = mit_tr_section.get('wwdc_2026_pcc_omission', {})
        rate = omission.get('apple_wwdc_coverage_rate', '')
        assert '2024' in str(rate) or '50%' in str(rate) or '1 of 2' in str(rate)
