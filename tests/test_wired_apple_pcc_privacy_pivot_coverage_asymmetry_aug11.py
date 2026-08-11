"""
WIRED × Apple PCC-to-Google-Cloud Privacy Pivot — Coverage Selection Asymmetry
Type A deep dive, Aug 11 2026 10:00 PT

Mechanism #44: In a single 11-day window (Jun 4-15 2026), WIRED published 3+ standalone
investigative articles about Meta's DORMANT, never-activated, on-device facial recognition
code (NameTag) — including code review, EFF researcher analysis, Rank One Computing license
document procurement, and Pentagon/police supplier chain tracing — while applying ZERO
investigative resources to Apple's FUNDAMENTAL PCC architecture change announced Jun 8 at
WWDC 2026, in which Apple shifted Private Cloud Compute from Apple-only silicon servers to
Google Cloud with Nvidia GPUs.

Apple's PCC shift affects ALL Apple Intelligence users' intimate data (messages, emails,
photos, Siri queries), is actively deployed (not dormant), and routes data through
third-party infrastructure (Google). WIRED's WWDC coverage instead used "makeover" framing
(Brian Barrett, Uncanny Valley podcast Jun 11: "Siri's AI Makeover"). The same Jun 11
episode also covered WIRED's own NameTag follow-up.

Financial prediction: Condé Nast/WIRED is in negotiations for Apple Intelligence content
licensing (~$50M) and has Apple News+ revenue sharing (16 titles). Meta has $0 in Condé
Nast deals. Coverage scrutiny inversely correlates with financial relationship value.
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
def wired_profile():
    return load_yaml('wired.yaml')


@pytest.fixture(scope='module')
def entities():
    return load_yaml('competitor-entities.yaml')


@pytest.fixture(scope='module')
def mechanism(research):
    cpf = research.get('cross_publication_findings', {})
    return cpf.get('wired_apple_pcc_google_cloud_privacy_pivot', {})


# ===================================================================
# 1. MECHANISM #44 EXISTS AND IS WELL-FORMED
# ===================================================================

class TestMechanism44Exists:
    """Mechanism #44 is present in cross_publication_findings with required fields."""

    def test_mechanism_id_is_44(self, mechanism):
        assert mechanism.get('mechanism_id') == 44

    def test_mechanism_name_present(self, mechanism):
        assert 'PCC' in mechanism.get('mechanism_name', '')
        assert 'Privacy' in mechanism.get('mechanism_name', '') or 'privacy' in mechanism.get('mechanism_name', '')

    def test_finding_type(self, mechanism):
        assert mechanism.get('finding_type') == 'coverage_selection_privacy_scrutiny_inversion'

    def test_rotation_type_a(self, mechanism):
        assert mechanism.get('rotation_type') == 'A'

    def test_publication_is_wired(self, mechanism):
        assert mechanism.get('publication') == 'WIRED'

    def test_has_finding_summary(self, mechanism):
        summary = mechanism.get('finding_summary', '')
        assert len(summary) > 100
        assert 'NameTag' in summary
        assert 'PCC' in summary or 'Private Cloud Compute' in summary

    def test_has_source_urls(self, mechanism):
        urls = mechanism.get('source_urls', [])
        assert len(urls) >= 5

    def test_has_cross_references(self, mechanism):
        xrefs = mechanism.get('cross_references', [])
        assert len(xrefs) >= 3
        # Must reference mechanism #33 (facial recognition parity) and #41 (MIT TR PCC omission)
        xref_text = ' '.join(xrefs)
        assert '#33' in xref_text or '33' in xref_text
        assert '#41' in xref_text or '41' in xref_text


# ===================================================================
# 2. PRIVACY SCOPE COMPARISON — META vs APPLE
# ===================================================================

class TestPrivacyScopeComparison:
    """The privacy scope comparison correctly captures the asymmetry."""

    def test_meta_nametag_status_dormant(self, mechanism):
        meta = mechanism.get('privacy_scope_comparison', {}).get('meta_nametag', {})
        assert 'dormant' in meta.get('status', '').lower()

    def test_meta_nametag_articles_positive(self, mechanism):
        meta = mechanism.get('privacy_scope_comparison', {}).get('meta_nametag', {})
        assert meta.get('articles_count', 0) >= 3

    def test_apple_pcc_status_active(self, mechanism):
        apple = mechanism.get('privacy_scope_comparison', {}).get('apple_pcc_shift', {})
        assert 'active' in apple.get('status', '').lower()

    def test_apple_pcc_articles_zero(self, mechanism):
        apple = mechanism.get('privacy_scope_comparison', {}).get('apple_pcc_shift', {})
        assert apple.get('articles_count', -1) == 0

    def test_apple_pcc_language_is_makeover(self, mechanism):
        apple = mechanism.get('privacy_scope_comparison', {}).get('apple_pcc_shift', {})
        assert 'makeover' in apple.get('language', '').lower()

    def test_meta_language_includes_surveillance(self, mechanism):
        meta = mechanism.get('privacy_scope_comparison', {}).get('meta_nametag', {})
        lang = meta.get('language', '').lower()
        assert 'surveillance' in lang or 'pentagon' in lang or 'police' in lang

    def test_meta_on_device_apple_cloud(self, mechanism):
        """Meta's feature was on-device; Apple's shift moves data to Google Cloud."""
        meta = mechanism.get('privacy_scope_comparison', {}).get('meta_nametag', {})
        apple = mechanism.get('privacy_scope_comparison', {}).get('apple_pcc_shift', {})
        assert 'on-device' in meta.get('processing_location', '').lower()
        assert 'google' in apple.get('processing_location', '').lower()

    def test_meta_zero_user_impact(self, mechanism):
        """Meta's code was never activated — zero actual user impact."""
        meta = mechanism.get('privacy_scope_comparison', {}).get('meta_nametag', {})
        assert 'zero' in meta.get('user_impact', '').lower() or '0' in meta.get('user_impact', '')

    def test_apple_hundreds_of_millions_impact(self, mechanism):
        """Apple's PCC shift affects all Apple Intelligence users."""
        apple = mechanism.get('privacy_scope_comparison', {}).get('apple_pcc_shift', {})
        impact = apple.get('user_impact', '').lower()
        assert 'all' in impact or 'million' in impact


# ===================================================================
# 3. TIMELINE — SAME WINDOW, OPPOSITE TREATMENT
# ===================================================================

class TestTimeline:
    """The timeline shows same-window coverage with opposite editorial treatment."""

    def test_timeline_has_events(self, mechanism):
        timeline = mechanism.get('timeline', [])
        assert len(timeline) >= 5

    def test_nametag_investigation_before_wwdc(self, mechanism):
        """WIRED's NameTag investigation (Jun 4) predates Apple WWDC (Jun 8)."""
        timeline = mechanism.get('timeline', [])
        dates = [e.get('date', '') for e in timeline]
        assert '2026-06-04' in dates
        assert '2026-06-08' in dates

    def test_same_day_coverage_jun_8(self, mechanism):
        """Jun 8: Apple WWDC + WIRED NameTag follow-up on same day."""
        timeline = mechanism.get('timeline', [])
        jun8_events = [e for e in timeline if e.get('date') == '2026-06-08']
        assert len(jun8_events) >= 2

    def test_makeover_episode_covers_both(self, mechanism):
        """Jun 11 Uncanny Valley podcast: 'Siri's AI Makeover' + NameTag in same episode."""
        timeline = mechanism.get('timeline', [])
        jun11_events = [e for e in timeline if e.get('date') == '2026-06-11']
        assert len(jun11_events) >= 1
        event_text = jun11_events[0].get('event', '').lower()
        assert 'makeover' in event_text
        assert 'nametag' in event_text or 'same episode' in event_text

    def test_rank_one_followup_jun_15(self, mechanism):
        """Jun 15: WIRED publishes Pentagon supplier investigation (Rank One)."""
        timeline = mechanism.get('timeline', [])
        jun15_events = [e for e in timeline if e.get('date') == '2026-06-15']
        assert len(jun15_events) >= 1
        assert 'rank one' in jun15_events[0].get('event', '').lower() or \
               'pentagon' in jun15_events[0].get('event', '').lower()


# ===================================================================
# 4. FINANCIAL PREDICTION ALIGNMENT
# ===================================================================

class TestFinancialPrediction:
    """Coverage scrutiny inversely correlates with financial relationship value."""

    def test_conde_nast_has_apple_deals(self, mechanism):
        fp = mechanism.get('financial_prediction', {})
        apple_deals = fp.get('conde_nast_apple_deals', [])
        assert len(apple_deals) >= 2
        deal_text = ' '.join(apple_deals).lower()
        assert 'apple news+' in deal_text or 'news+' in deal_text
        assert 'intelligence' in deal_text or 'negotiat' in deal_text

    def test_conde_nast_zero_meta_deals(self, mechanism):
        fp = mechanism.get('financial_prediction', {})
        meta_deals = fp.get('conde_nast_meta_deals', '')
        assert '$0' in meta_deals

    def test_prediction_states_inverse_correlation(self, mechanism):
        fp = mechanism.get('financial_prediction', {})
        prediction = fp.get('prediction', '').lower()
        assert 'inverse' in prediction or 'correlat' in prediction


# ===================================================================
# 5. LEGITIMATE FACTORS — INTELLECTUAL HONESTY
# ===================================================================

class TestLegitimateFactors:
    """Mechanism documents legitimate editorial reasons for the asymmetry."""

    def test_has_at_least_7_legitimate_factors(self, mechanism):
        factors = mechanism.get('legitimate_factors', [])
        assert len(factors) >= 7

    def test_nvidia_confidential_computing_acknowledged(self, mechanism):
        factors = mechanism.get('legitimate_factors', [])
        factor_text = ' '.join(factors).lower()
        assert 'nvidia' in factor_text or 'confidential' in factor_text or 'hardware' in factor_text

    def test_apple_privacy_track_record_acknowledged(self, mechanism):
        factors = mechanism.get('legitimate_factors', [])
        factor_text = ' '.join(factors).lower()
        assert 'track record' in factor_text or 'privacy' in factor_text

    def test_original_reporting_value_acknowledged(self, mechanism):
        """WIRED's NameTag investigation was genuine original reporting."""
        factors = mechanism.get('legitimate_factors', [])
        factor_text = ' '.join(factors).lower()
        assert 'original' in factor_text or 'genuine' in factor_text

    def test_facial_recognition_more_invasive(self, mechanism):
        """Acknowledges facial recognition is generally considered more privacy-invasive."""
        factors = mechanism.get('legitimate_factors', [])
        factor_text = ' '.join(factors).lower()
        assert 'facial recognition' in factor_text and 'invasive' in factor_text

    def test_gizmodo_covered_apple_pcc_concerns(self, mechanism):
        """Other publications (Gizmodo) DID raise Apple PCC privacy concerns."""
        factors = mechanism.get('legitimate_factors', [])
        factor_text = ' '.join(factors).lower()
        assert 'gizmodo' in factor_text


# ===================================================================
# 6. CROSS-VALIDATION WITH WIRED PROFILE
# ===================================================================

class TestCrossValidationWithWiredProfile:
    """Mechanism #44 findings are consistent with the WIRED publication profile."""

    def test_wired_profile_has_makeover_headline(self, wired_profile):
        """WIRED profile documents 'Siri's AI Makeover' headline."""
        found = False
        # Check key_journalists (where Barrett's cross-entity analysis lives)
        for j in wired_profile.get('key_journalists', []):
            cea = j.get('cross_entity_coverage_analysis', {})
            headlines = cea.get('competitor_headlines_2026', {}).get('examples', [])
            for h in headlines:
                if 'makeover' in h.get('headline', '').lower() and 'siri' in h.get('headline', '').lower():
                    found = True
        # Also check full profile text as fallback
        if not found:
            profile_text = str(wired_profile).lower()
            found = 'siri' in profile_text and 'makeover' in profile_text
        assert found, "WIRED profile should document 'Siri's AI Makeover' headline"

    def test_wired_profile_has_apple_news_plus_deal(self, wired_profile):
        """WIRED profile documents Apple News+ distribution deal."""
        financial = wired_profile.get('financial_relationships', {})
        if isinstance(financial, dict):
            deals = financial.get('ai_content_deals', [])
        else:
            deals = []
        # Also check known_conflicts or ownership_chain or broader profile
        profile_text = str(wired_profile).lower()
        assert 'apple news' in profile_text or 'news+' in profile_text

    def test_wired_profile_has_apple_intelligence_negotiations(self, wired_profile):
        """WIRED profile documents Apple Intelligence content licensing negotiations."""
        profile_text = str(wired_profile).lower()
        assert 'apple intelligence' in profile_text
        assert 'negotiat' in profile_text

    def test_wired_profile_has_zero_meta_deals(self, wired_profile):
        """WIRED profile confirms $0 in Meta content deals."""
        profile_text = str(wired_profile)
        # Should mention Meta having $0 or no deal
        assert '$0' in profile_text or 'zero' in profile_text.lower()


# ===================================================================
# 7. COMPETITOR ENTITY VALIDATION
# ===================================================================

class TestCompetitorEntityValidation:
    """Apple entity is properly defined in competitor-entities.yaml."""

    def test_apple_entity_exists(self, entities):
        """Apple should be in the entities list."""
        entity_keys = list(entities.get('entities', {}).keys())
        assert 'apple' in entity_keys

    def test_apple_has_hardware_devices(self, entities):
        """Apple entity should have hardware_devices section."""
        apple = entities.get('entities', {}).get('apple', {})
        # Apple should have wearables or hardware info
        entity_text = str(apple).lower()
        assert 'glasses' in entity_text or 'hardware' in entity_text or \
               'vision' in entity_text or 'wearable' in entity_text or \
               'airpods' in entity_text


# ===================================================================
# 8. SCOPE ASYMMETRY RATIO
# ===================================================================

class TestScopeAsymmetryRatio:
    """Quantitative comparison shows massive scrutiny inversion."""

    def test_article_count_ratio(self, mechanism):
        """Meta gets 3+ articles for dormant code; Apple gets 0 for active architecture change."""
        meta = mechanism.get('privacy_scope_comparison', {}).get('meta_nametag', {})
        apple = mechanism.get('privacy_scope_comparison', {}).get('apple_pcc_shift', {})
        meta_count = meta.get('articles_count', 0)
        apple_count = apple.get('articles_count', 1)  # default 1 to avoid false positive
        assert meta_count >= 3
        assert apple_count == 0
        # Ratio is infinite (3/0), but we just verify the absolute gap
        assert meta_count - apple_count >= 3

    def test_source_diversity_gap(self, mechanism):
        """Meta coverage cites multiple independent sources; Apple coverage cites Apple PR only."""
        meta = mechanism.get('privacy_scope_comparison', {}).get('meta_nametag', {})
        apple = mechanism.get('privacy_scope_comparison', {}).get('apple_pcc_shift', {})
        meta_sources = meta.get('sources_cited', '').lower()
        apple_sources = apple.get('sources_cited', '').lower()
        # Meta has EFF, ACLU, etc.
        assert 'eff' in meta_sources or 'aclu' in meta_sources or 'security' in meta_sources
        # Apple has only Apple PR
        assert 'apple pr' in apple_sources or 'pr only' in apple_sources


# ===================================================================
# 9. CROSS-REFERENCE INTEGRITY
# ===================================================================

class TestCrossReferenceIntegrity:
    """Cross-referenced mechanisms exist and have test files."""

    @pytest.mark.parametrize("mech_id", [33, 41, 42])
    def test_cross_referenced_mechanisms_have_test_files(self, research, mech_id):
        """Each cross-referenced mechanism should have a test_file that exists on disk."""
        cpf = research.get('cross_publication_findings', {})
        agg = research.get('aggregate_findings', {})
        all_findings = {}
        all_findings.update(cpf)
        all_findings.update(agg)
        found = False
        for key, val in all_findings.items():
            if isinstance(val, dict) and val.get('mechanism_id') == mech_id:
                test_file = val.get('test_file', '')
                if test_file:
                    path = os.path.join(REPO_ROOT, test_file)
                    assert os.path.exists(path), \
                        f"Mechanism #{mech_id} test_file {test_file} should exist on disk"
                found = True
        # Also check publications section
        pubs = research.get('publications', {})
        for pub_key, pub_val in pubs.items():
            if isinstance(pub_val, dict):
                for sub_key, sub_val in pub_val.items():
                    if isinstance(sub_val, dict) and sub_val.get('mechanism_id') == mech_id:
                        test_file = sub_val.get('test_file', '')
                        if test_file:
                            path = os.path.join(REPO_ROOT, test_file)
                            assert os.path.exists(path), \
                                f"Mechanism #{mech_id} test_file {test_file} should exist on disk"
                        found = True
        assert found, f"Mechanism #{mech_id} should exist in research YAML"

    def test_mechanism_44_test_file_exists(self, mechanism):
        """This mechanism's own test file should exist."""
        test_file = mechanism.get('test_file', '')
        assert test_file
        path = os.path.join(REPO_ROOT, test_file)
        assert os.path.exists(path), f"Mechanism #44 test_file {test_file} should exist"
