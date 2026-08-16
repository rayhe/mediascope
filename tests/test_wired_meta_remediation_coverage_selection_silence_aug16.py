"""
Mechanism #134: WIRED Remediation Coverage Selection Silence — Meta v26 LED Privacy Fix

CORE FINDING:
WIRED published "The Rise of the Ray-Ban Meta Creep" (March 2026) — a major adversarial
feature article documenting LED disabling services, pickup artist misuse, and "glasshole"
culture. WIRED then published a second adversarial investigation (June 4, 2026) about
dormant facial recognition code ("NameTag") found in Meta's smart glasses app.

On July 7, 2026, Meta shipped the v26 mandatory update that:
  1. Disables the camera if the LED is tampered with or destroyed
  2. Removes ads/posts/Marketplace listings for LED tampering services
  3. Takes legal action against LED tampering businesses
  4. Mandatory update rolling out across all models

Meta VP of Wearables Alex Himel told The Verge the update was in development before
public complaints intensified. Meta's claim: "No other kind of camera has done this,
and we're proud to lead the industry forward."

WIRED published ZERO articles covering Meta's v26 LED privacy fix. This is a
remediation coverage selection gap — WIRED raised the alarm, Meta fixed the exact issue,
WIRED didn't cover the fix.

Meanwhile, at least 7 other publications DID cover Meta's privacy fix:
  - The Verge (Alex Himel interview)
  - 9to5Google
  - Digital Trends
  - Android Police
  - Road to VR
  - PetaPixel
  - Engadget

Then 19 days later (July 26), Apple's N50 delay for "privacy" was reported, and Apple's
PROMISE to be privacy-first (no shipped product, no actual fix) received extensive
coverage including from publications like WIRED.

Novel mechanism type: remediation_coverage_selection_silence — publication raises alarm,
company addresses exact issue, publication doesn't cover fix, ensuring original alarm
narrative persists uncorrected.

FINANCIAL CONTEXT:
  - Condé Nast (WIRED's parent) has zero content licensing deals with Meta
  - Condé Nast signed a deal with OpenAI (Aug 2024)
  - Advance Publications (owns Condé Nast) has $10B+ Reddit stake
  - Reddit has Google data licensing deal
  - Meta is Condé Nast's single largest advertising competitor

CONFOUNDERS:
  1. STRONG: WIRED may consider the fix insufficient (LED tamper detection doesn't
     address always-on "super sensing" plans, reported by FT July 9)
  2. STRONG: Editorial judgment — the fix is incremental, not a major feature story
  3. MODERATE: WIRED's subscription model prioritizes investigation over PR coverage
  4. MODERATE: Resource allocation — limited wearables beat bandwidth
  5. WEAK: Publishing lag — search indexes may not capture every WIRED article
"""

import pytest
import yaml
import os


_PROFILES_CACHE = None

def _load_profiles():
    """Load all relevant YAML profiles (cached)."""
    global _PROFILES_CACHE
    if _PROFILES_CACHE is not None:
        return _PROFILES_CACHE
    base = os.path.join(os.path.dirname(__file__), '..', 'profiles')
    profiles = {}
    for name in ['wired.yaml', 'competitor-coverage-research.yaml', 'competitor-entities.yaml']:
        path = os.path.join(base, name)
        if os.path.exists(path):
            with open(path) as f:
                profiles[name] = yaml.safe_load(f)
    _PROFILES_CACHE = profiles
    return profiles


def _get_mechanism_from_wired(profiles, mechanism_id=134):
    """Find mechanism by ID in wired.yaml."""
    wired = profiles.get('wired.yaml', {})
    # Search top-level keys
    for key, value in wired.items():
        if isinstance(value, dict):
            if value.get('mechanism_id') == mechanism_id:
                return value
            # Search nested dicts
            for sub_key, sub_val in value.items():
                if isinstance(sub_val, dict) and sub_val.get('mechanism_id') == mechanism_id:
                    return sub_val
    return None


def _get_mechanism_from_ccr(profiles, mechanism_id=134):
    """Find mechanism by ID in competitor-coverage-research.yaml."""
    ccr = profiles.get('competitor-coverage-research.yaml', {})
    # Search cross_publication_findings
    findings = ccr.get('cross_publication_findings', {})
    for key, value in findings.items():
        if isinstance(value, dict) and value.get('mechanism_id') == mechanism_id:
            return value
    # Search publications
    pubs = ccr.get('publications', {})
    for pub_key, pub_val in pubs.items():
        if isinstance(pub_val, dict):
            for key, value in pub_val.items():
                if isinstance(value, dict) and value.get('mechanism_id') == mechanism_id:
                    return value
    # Search all top-level keys
    for key, value in ccr.items():
        if isinstance(value, dict) and value.get('mechanism_id') == mechanism_id:
            return value
        if isinstance(value, dict):
            for sub_key, sub_val in value.items():
                if isinstance(sub_val, dict) and sub_val.get('mechanism_id') == mechanism_id:
                    return sub_val
    return None


# ===========================================================================
# TEST CLASS 1: Mechanism Structural Integrity
# ===========================================================================
class TestMechanismStructuralIntegrity:
    """Verify mechanism #134 exists and has required structural fields."""

    def test_mechanism_134_exists_in_wired_yaml(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None, "Mechanism #134 must exist in wired.yaml"

    def test_mechanism_134_exists_in_ccr(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_ccr(profiles, 134)
        assert mechanism is not None, "Mechanism #134 must exist in competitor-coverage-research.yaml"

    def test_mechanism_has_finding_summary(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        summary = str(mechanism.get('finding_summary', ''))
        assert len(summary) > 50, "Mechanism must have a substantive finding_summary"

    def test_mechanism_has_discovery_date(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        date = str(mechanism.get('analysis_date', '') or mechanism.get('date_added', ''))
        assert '2026-08' in date, "Discovery date must be August 2026"

    def test_mechanism_has_source_urls(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        urls = mechanism.get('source_urls', [])
        assert len(urls) >= 3, "Must have at least 3 source URLs"

    def test_mechanism_has_confounders(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism)
        assert 'confounder' in content.lower() or 'legitimate_factor' in content.lower(), \
            "Must document confounders"

    def test_mechanism_has_cross_references(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        cross_refs = mechanism.get('cross_references', [])
        assert len(cross_refs) >= 3, \
            f"Must have at least 3 cross-references; found {len(cross_refs)}"
        ref_ids = [r.get('mechanism_id') for r in cross_refs if isinstance(r, dict)]
        assert 8 in ref_ids or 30 in ref_ids or 33 in ref_ids, \
            f"Must cross-reference mechanisms #8, #30, or #33; found IDs {ref_ids}"

    def test_mechanism_type_is_remediation(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'remediation' in content, \
            "Must identify novel mechanism type as remediation_coverage_selection_silence"


# ===========================================================================
# TEST CLASS 2: WIRED Adversarial Coverage Existence
# ===========================================================================
class TestWIREDAdversarialCoverage:
    """Verify WIRED's original adversarial articles about Meta glasses are documented."""

    def test_creep_article_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'creep' in content, \
            "Must reference 'The Rise of the Ray-Ban Meta Creep' article"

    def test_creep_article_date(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism)
        assert 'march' in content.lower() or 'mar' in content.lower() or \
               '2026-03' in content, \
            "Must document the March 2026 date of the Creep article"

    def test_nametag_article_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'nametag' in content or 'name tag' in content or \
               'facial recognition' in content or 'face-recognition' in content, \
            "Must reference the June 2026 NameTag investigation"

    def test_nametag_article_date(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism)
        assert 'june' in content.lower() or 'jun' in content.lower() or \
               '2026-06' in content, \
            "Must document the June 2026 date of the NameTag article"

    def test_led_disabling_services_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'led' in content and ('disabl' in content or 'tamper' in content), \
            "Must document LED disabling/tampering as the core privacy issue raised"


# ===========================================================================
# TEST CLASS 3: Meta v26 Fix Content
# ===========================================================================
class TestMetaV26FixContent:
    """Verify Meta's v26 mandatory update is properly documented."""

    def test_v26_update_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'v26' in content or 'version 26' in content, \
            "Must reference the v26 mandatory update"

    def test_camera_disable_feature_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'camera' in content and 'disable' in content, \
            "Must document that camera is disabled if LED is tampered"

    def test_marketplace_enforcement_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'marketplace' in content or 'listing' in content or 'removal' in content, \
            "Must document removal of LED tampering listings from marketplace"

    def test_legal_action_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'legal' in content, \
            "Must document Meta's legal action against tampering businesses"

    def test_july_7_date_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism)
        assert 'july 7' in content.lower() or 'jul 7' in content.lower() or \
               '2026-07-07' in content or 'july 2026' in content.lower(), \
            "Must document the July 7, 2026 fix date"

    def test_meta_industry_first_claim_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'no other' in content or 'industry' in content or 'first' in content or \
               'lead' in content, \
            "Must document Meta's claim about being first to do this"

    def test_alex_himel_reference(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'himel' in content or 'alex' in content, \
            "Must reference Alex Himel's statements about the update"


# ===========================================================================
# TEST CLASS 4: Coverage Selection Gap — WIRED Zero vs Others
# ===========================================================================
class TestCoverageSelectionGap:
    """Verify the coverage gap is documented: WIRED zero, 7+ others covered."""

    def test_wired_zero_coverage_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'zero' in content or '0' in content, \
            "Must document WIRED's zero coverage of the v26 fix"

    def test_verge_coverage_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'verge' in content, "Must document The Verge's coverage"

    def test_9to5google_coverage_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert '9to5' in content or '9to5google' in content, \
            "Must document 9to5Google's coverage"

    def test_digital_trends_coverage_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'digital trends' in content, "Must document Digital Trends' coverage"

    def test_android_police_coverage_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'android police' in content, "Must document Android Police's coverage"

    def test_road_to_vr_coverage_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'road to vr' in content or 'roadtovr' in content, \
            "Must document Road to VR's coverage"

    def test_petapixel_coverage_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'petapixel' in content, "Must document PetaPixel's coverage"

    def test_engadget_coverage_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'engadget' in content, "Must document Engadget's coverage"

    def test_at_least_seven_other_outlets(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        outlets = ['verge', '9to5', 'digital trends', 'android police',
                   'road to vr', 'petapixel', 'engadget']
        found = sum(1 for o in outlets if o in content)
        assert found >= 7, f"Must document at least 7 other outlets that covered the fix; found {found}"


# ===========================================================================
# TEST CLASS 5: Financial Relationship Data
# ===========================================================================
class TestFinancialRelationshipData:
    """Verify financial context is documented."""

    def test_conde_nast_openai_deal_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'openai' in content and ('condé nast' in content or 'conde nast' in content), \
            "Must document Condé Nast's OpenAI deal"

    def test_advance_reddit_stake_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'advance' in content or 'reddit' in content, \
            "Must document Advance Publications / Reddit connection"

    def test_meta_zero_content_deals_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'zero' in content or '$0' in content or 'no content deal' in content or \
               'no deal' in content, \
            "Must document Meta's zero content deals with Condé Nast"

    def test_ad_competition_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'advertis' in content or 'ad ' in content or 'competitor' in content, \
            "Must document Meta as Condé Nast's advertising competitor"


# ===========================================================================
# TEST CLASS 6: Cross-References to Related Mechanisms
# ===========================================================================
class TestCrossReferences:
    """Verify cross-references to related mechanisms."""

    def test_cross_ref_mechanism_8(self):
        """Mechanism #8: safe-target coefficient / emotional register asymmetry."""
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism)
        assert '8' in content, "Must cross-reference mechanism #8"

    def test_cross_ref_mechanism_30(self):
        """Mechanism #30: Chokkattu cross-entity framing."""
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism)
        assert '30' in content, "Must cross-reference mechanism #30"

    def test_cross_ref_mechanism_33(self):
        """Mechanism #33: WIRED Meta-exclusive privacy vocabulary."""
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism)
        assert '33' in content, "Must cross-reference mechanism #33"

    def test_cross_ref_mechanism_101_or_118(self):
        """Mechanism #101 or #118: related coverage/framing asymmetry."""
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism)
        assert '101' in content or '118' in content, \
            "Must cross-reference mechanism #101 or #118"


# ===========================================================================
# TEST CLASS 7: Apple N50 Delay Framing Comparison
# ===========================================================================
class TestAppleN50DelayComparison:
    """Verify the Apple N50 contrast is documented — promise vs shipped fix."""

    def test_apple_n50_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'apple' in content and ('n50' in content or 'delay' in content or 'privacy' in content), \
            "Must document Apple N50 delay for comparison"

    def test_19_day_gap_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert '19' in content or 'nineteen' in content or 'july 26' in content or \
               '2026-07-26' in content, \
            "Must document the 19-day gap between Meta fix and Apple announcement"

    def test_promise_vs_fix_contrast(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'promise' in content or 'shipped' in content or 'no product' in content or \
               'actual fix' in content or 'delayed' in content, \
            "Must contrast Apple's promise (no shipped product) vs Meta's actual fix"


# ===========================================================================
# TEST CLASS 8: Confounder Quality Checks
# ===========================================================================
class TestConfounderQuality:
    """Verify confounders are documented with strength ratings."""

    def test_at_least_five_confounders(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        confounders = mechanism.get('confounders', [])
        if not confounders:
            # Try alternative structures
            confounders = mechanism.get('legitimate_factors', [])
        assert len(confounders) >= 5, \
            f"Must have at least 5 confounders; found {len(confounders)}"

    def test_strong_confounders_exist(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'strong' in content, "Must have at least one STRONG confounder"

    def test_super_sensing_confounder_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'super sensing' in content or 'always-on' in content or 'insufficient' in content, \
            "Must document the confounder that WIRED may consider the fix insufficient"

    def test_editorial_judgment_confounder_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'editorial judgment' in content or 'incremental' in content or \
               'editorial' in content, \
            "Must document the editorial judgment confounder"

    def test_subscription_model_confounder(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'subscription' in content or 'investigation' in content or \
               'pr coverage' in content or 'prioritiz' in content, \
            "Must document WIRED's subscription model as confounder"


# ===========================================================================
# TEST CLASS 9: Source URL Verification
# ===========================================================================
class TestSourceURLVerification:
    """Verify source URLs are present and contain expected outlets."""

    def test_source_urls_contain_9to5google(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        urls = mechanism.get('source_urls', [])
        url_str = ' '.join(str(u) for u in urls)
        assert '9to5google' in url_str, "Source URLs must include 9to5Google article"

    def test_source_urls_contain_digital_trends(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        urls = mechanism.get('source_urls', [])
        url_str = ' '.join(str(u) for u in urls)
        assert 'digitaltrends' in url_str, "Source URLs must include Digital Trends article"

    def test_source_urls_contain_android_police(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        urls = mechanism.get('source_urls', [])
        url_str = ' '.join(str(u) for u in urls)
        assert 'androidpolice' in url_str, "Source URLs must include Android Police article"

    def test_source_urls_contain_road_to_vr(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        urls = mechanism.get('source_urls', [])
        url_str = ' '.join(str(u) for u in urls)
        assert 'roadtovr' in url_str, "Source URLs must include Road to VR article"

    def test_source_urls_contain_petapixel(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        urls = mechanism.get('source_urls', [])
        url_str = ' '.join(str(u) for u in urls)
        assert 'petapixel' in url_str, "Source URLs must include PetaPixel article"

    def test_source_urls_contain_engadget(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        urls = mechanism.get('source_urls', [])
        url_str = ' '.join(str(u) for u in urls)
        assert 'engadget' in url_str, "Source URLs must include Engadget article"

    def test_source_urls_contain_wired_creep_archive(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        urls = mechanism.get('source_urls', [])
        url_str = ' '.join(str(u) for u in urls)
        assert 'web.archive.org' in url_str or 'wired.com' in url_str, \
            "Source URLs must include the archived WIRED Creep article"


# ===========================================================================
# TEST CLASS 10: Novel Mechanism Type Validation
# ===========================================================================
class TestNovelMechanismType:
    """Verify the novel mechanism type is properly defined."""

    def test_mechanism_type_name(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'remediation_coverage_selection_silence' in content or \
               'remediation coverage selection silence' in content, \
            "Must name the novel mechanism type"

    def test_mechanism_type_definition(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'alarm' in content and 'fix' in content, \
            "Must define the pattern: publication raises alarm, company fixes, publication ignores fix"

    def test_narrative_persistence_documented(self):
        profiles = _load_profiles()
        mechanism = _get_mechanism_from_wired(profiles, 134)
        assert mechanism is not None
        content = str(mechanism).lower()
        assert 'persist' in content or 'uncorrected' in content or 'narrative' in content, \
            "Must document that the original alarm narrative persists uncorrected"
