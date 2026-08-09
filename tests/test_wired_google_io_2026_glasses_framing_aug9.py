"""
WIRED Google I/O 2026 Smart Glasses Coverage — Lane Assignment Extended

Type A: Competitor Coverage Deep Dive (Aug 9, 2026 03:00 PT)

Publication: WIRED (Condé Nast / Advance Publications)
Competitor: Google (Android XR smart glasses)
Comparison: Same publication's Meta Ray-Ban coverage

Finding: WIRED sent 5 reporters including Lauren Goode to Google I/O 2026 to cover
Google's camera-equipped, Gemini AI-integrated smart glasses. The coverage used
playful/enthusiastic framing — "Nano Banana on smart glasses is actually bananas.
The demo worked!" — for hardware functionally identical to Meta's Ray-Ban glasses,
which receive "dormant surveillance infrastructure" and "mass surveillance" framing
from the same publication. This extends the documented lane assignment pattern from
Apple/Snap to include Google: EVERY competitor gets product-review treatment, Meta
alone gets investigative-alarm treatment.

Sources:
- WIRED I/O 2026 live blog (rehosted at technologytangle.com)
- Business Wars podcast "Meta and the Battle for Smart Glasses" (Jun 2026)
- WIRED "The Rise of the Ray-Ban Meta Creep" (archive.org)
- Fox News analysis of Google Nano Banana deepfake capability
"""

import yaml
import os

PROFILE_PATH = os.path.join(
    os.path.dirname(__file__), '..', 'profiles', 'wired.yaml'
)

def _load_profile():
    with open(PROFILE_PATH) as f:
        return yaml.safe_load(f)


def _get_google_io_section():
    """Extract the google_io_2026_smart_glasses_coverage section."""
    profile = _load_profile()
    # Navigate to the section — it's a top-level key within the wired profile
    # or nested under a wearables/competitor section
    # Try multiple paths since YAML structure varies
    section = profile.get('google_io_2026_smart_glasses_coverage')
    if section:
        return section

    # Check nested structures
    for key in ['wearables_coverage_analysis', 'competitor_relationships',
                'cross_entity_coverage_analysis', 'competitor_coverage']:
        container = profile.get(key)
        if isinstance(container, dict):
            section = container.get('google_io_2026_smart_glasses_coverage')
            if section:
                return section

    # Deep search through all values
    def _find_key(d, target):
        if isinstance(d, dict):
            if target in d:
                return d[target]
            for v in d.values():
                result = _find_key(v, target)
                if result:
                    return result
        elif isinstance(d, list):
            for item in d:
                result = _find_key(item, target)
                if result:
                    return result
        return None

    return _find_key(profile, 'google_io_2026_smart_glasses_coverage')


class TestGoogleIO2026Coverage:
    """Verify the Google I/O 2026 smart glasses coverage section exists with key fields."""

    def test_section_exists(self):
        section = _get_google_io_section()
        assert section is not None, "google_io_2026_smart_glasses_coverage section must exist in wired.yaml"

    def test_event_date(self):
        section = _get_google_io_section()
        assert section['date'] == '2026-05-19', "Google I/O 2026 was May 19, 2026"

    def test_event_name(self):
        section = _get_google_io_section()
        assert 'Google I/O' in section['event']

    def test_key_finding_mentions_lane_assignment(self):
        section = _get_google_io_section()
        finding = section.get('key_finding', '')
        assert 'Lane Assignment' in finding, "Key finding must reference the lane assignment pattern"

    def test_five_reporters_sent(self):
        section = _get_google_io_section()
        reporters = section.get('wired_reporters_sent', [])
        assert len(reporters) == 5, f"WIRED sent 5 reporters to I/O 2026, got {len(reporters)}"

    def test_lauren_goode_present(self):
        section = _get_google_io_section()
        reporters = section.get('wired_reporters_sent', [])
        names = [r['name'] for r in reporters]
        assert 'Lauren Goode' in names, "Lauren Goode must be among the I/O reporters"

    def test_julian_chokkattu_present(self):
        section = _get_google_io_section()
        reporters = section.get('wired_reporters_sent', [])
        names = [r['name'] for r in reporters]
        assert 'Julian Chokkattu' in names, "Julian Chokkattu must be among the I/O reporters"

    def test_boone_ashworth_present(self):
        section = _get_google_io_section()
        reporters = section.get('wired_reporters_sent', [])
        names = [r['name'] for r in reporters]
        assert 'Boone Ashworth' in names, "Boone Ashworth must be among the I/O reporters"


class TestLiveBlogFramingAnalysis:
    """Verify live blog quote analysis and framing comparison."""

    def test_live_blog_source_url_present(self):
        section = _get_google_io_section()
        blog = section.get('live_blog_framing', {})
        url = blog.get('source_url_proxy', '')
        assert 'technologytangle.com' in url, "Live blog source must reference technologytangle.com rehost"

    def test_nano_banana_quote_present(self):
        section = _get_google_io_section()
        quotes = section.get('live_blog_framing', {}).get('key_quotes', [])
        quote_texts = [q['quote'] for q in quotes]
        assert any('bananas' in q.lower() for q in quote_texts), \
            "Must include the 'Nano Banana is actually bananas' quote"

    def test_doctoring_photos_quote_present(self):
        section = _get_google_io_section()
        quotes = section.get('live_blog_framing', {}).get('key_quotes', [])
        quote_texts = [q['quote'] for q in quotes]
        assert any('doctoring' in q.lower() for q in quote_texts), \
            "Must include the 'doctoring photos in real time' quote"

    def test_google_glass_nostalgia_quote_present(self):
        section = _get_google_io_section()
        quotes = section.get('live_blog_framing', {}).get('key_quotes', [])
        quote_texts = [q['quote'] for q in quotes]
        assert any('14 years' in q for q in quote_texts), \
            "Must include the '14 years (!) after Sergey' quote"

    def test_intelligent_eyewear_quote_present(self):
        section = _get_google_io_section()
        quotes = section.get('live_blog_framing', {}).get('key_quotes', [])
        quote_texts = [q['quote'] for q in quotes]
        assert any('intelligent eyewear' in q.lower() for q in quote_texts), \
            "Must include the 'Intelligent Eyewear' marketing quote"

    def test_all_quotes_have_meta_equivalent(self):
        section = _get_google_io_section()
        quotes = section.get('live_blog_framing', {}).get('key_quotes', [])
        for q in quotes:
            assert 'meta_equivalent_framing' in q, \
                f"Quote '{q['quote'][:40]}...' must have meta_equivalent_framing comparison"

    def test_all_quotes_have_tone(self):
        section = _get_google_io_section()
        quotes = section.get('live_blog_framing', {}).get('key_quotes', [])
        for q in quotes:
            assert 'tone' in q, f"Quote '{q['quote'][:40]}...' must have tone classification"


class TestLaneAssignmentExtension:
    """Verify the lane assignment pattern extends to Google."""

    def test_lane_assignment_section_exists(self):
        section = _get_google_io_section()
        assert 'lane_assignment_extension' in section

    def test_lane_assignment_mentions_every_competitor(self):
        section = _get_google_io_section()
        finding = section.get('lane_assignment_extension', {}).get('finding', '')
        for entity in ['Apple', 'Snap', 'Google', 'Meta']:
            assert entity in finding, f"Lane assignment finding must mention {entity}"

    def test_camera_count_comparison_present(self):
        section = _get_google_io_section()
        comp = section.get('lane_assignment_extension', {}).get('camera_count_comparison', {})
        assert 'google_android_xr' in comp
        assert 'meta_ray_ban' in comp
        assert 'apple_vision_pro' in comp
        assert 'snap_spectacles' in comp

    def test_meta_is_only_entity_with_privacy_framing(self):
        section = _get_google_io_section()
        comp = section.get('lane_assignment_extension', {}).get('camera_count_comparison', {})
        assert comp.get('meta_privacy_framing_count', 0) > 0, "Meta must have nonzero privacy framing count"
        assert comp.get('google_privacy_framing_count', 0) == 0, "Google must have zero privacy framing"
        assert comp.get('snap_privacy_framing_count', 0) == 0, "Snap must have zero privacy framing"
        assert comp.get('apple_privacy_framing_count', 0) == 0, "Apple must have zero privacy framing"

    def test_product_review_lane_includes_google(self):
        section = _get_google_io_section()
        finding = section.get('lane_assignment_extension', {}).get('finding', '')
        # Google should be in the product review lane, not the investigative lane
        assert 'Google Android XR' in finding
        # Verify Google is listed in the product review section
        lines = finding.split('\n')
        product_review_section = False
        investigative_section = False
        google_in_product = False
        google_in_investigative = False
        for line in lines:
            if 'PRODUCT REVIEW LANE' in line:
                product_review_section = True
                investigative_section = False
            elif 'INVESTIGATIVE LANE' in line:
                product_review_section = False
                investigative_section = True
            if 'Google' in line:
                if product_review_section:
                    google_in_product = True
                if investigative_section:
                    google_in_investigative = True
        assert google_in_product, "Google must be in the product review lane"
        assert not google_in_investigative, "Google must NOT be in the investigative lane"

    def test_meta_only_in_investigative_lane(self):
        section = _get_google_io_section()
        finding = section.get('lane_assignment_extension', {}).get('finding', '')
        lines = finding.split('\n')
        investigative_section = False
        meta_in_investigative = False
        for line in lines:
            if 'INVESTIGATIVE LANE' in line:
                investigative_section = True
            elif 'PRODUCT REVIEW LANE' in line:
                investigative_section = False
            if 'Meta' in line and investigative_section:
                meta_in_investigative = True
        assert meta_in_investigative, "Meta must be in the investigative lane"


class TestAIPhotoManipulationAsymmetry:
    """Verify the AI photo manipulation framing asymmetry is documented."""

    def test_ai_manipulation_section_exists(self):
        section = _get_google_io_section()
        assert 'ai_photo_manipulation_asymmetry' in section

    def test_nano_banana_mentioned(self):
        section = _get_google_io_section()
        finding = section.get('ai_photo_manipulation_asymmetry', {}).get('finding', '')
        assert 'Nano Banana' in finding

    def test_deepfake_capability_noted(self):
        section = _get_google_io_section()
        finding = section.get('ai_photo_manipulation_asymmetry', {}).get('finding', '')
        assert 'deepfake' in finding.lower() or 'AI-ALTERED' in finding or 'manipulation' in finding.lower()

    def test_meta_comparison_present(self):
        section = _get_google_io_section()
        finding = section.get('ai_photo_manipulation_asymmetry', {}).get('finding', '')
        assert 'dormant surveillance infrastructure' in finding or 'surveillance' in finding.lower()

    def test_source_urls_present(self):
        section = _get_google_io_section()
        urls = section.get('ai_photo_manipulation_asymmetry', {}).get('source_urls', [])
        assert len(urls) >= 1, "AI photo manipulation section must have source URLs"


class TestGoogleGlassPrecedentReversal:
    """Verify the Google Glass precedent reversal pattern is documented."""

    def test_precedent_section_exists(self):
        section = _get_google_io_section()
        assert 'google_glass_precedent_reversal' in section

    def test_glasshole_reference(self):
        section = _get_google_io_section()
        finding = section.get('google_glass_precedent_reversal', {}).get('finding', '')
        assert 'Glasshole' in finding or 'glasshole' in finding.lower()

    def test_meta_creep_article_referenced(self):
        section = _get_google_io_section()
        urls = section.get('google_glass_precedent_reversal', {}).get('source_urls', [])
        url_text = ' '.join(urls)
        assert 'ray-ban-meta-creep' in url_text or 'archive.org' in url_text

    def test_redemption_vs_revival_contrast(self):
        section = _get_google_io_section()
        finding = section.get('google_glass_precedent_reversal', {}).get('finding', '')
        # Must contrast how Google gets redemption while Meta gets revival of backlash
        assert 'redemption' in finding.lower() or 'nostalgi' in finding.lower() or 'milestone' in finding.lower()
        assert 'backlash' in finding.lower() or 'revival' in finding.lower()


class TestChokkattuDualStandard:
    """Verify Chokkattu's dual standard between Google I/O and Business Wars is documented."""

    def test_dual_standard_section_exists(self):
        section = _get_google_io_section()
        assert 'chokkattu_dual_standard_evidence' in section

    def test_business_wars_reference(self):
        section = _get_google_io_section()
        finding = section.get('chokkattu_dual_standard_evidence', {}).get('finding', '')
        assert 'mass surveillance' in finding.lower() or 'Business Wars' in finding

    def test_timeline_documented(self):
        section = _get_google_io_section()
        finding = section.get('chokkattu_dual_standard_evidence', {}).get('finding', '')
        # Must document the May 19 → Jun 3 timeline
        assert 'May 19' in finding or '15-day' in finding or '15 day' in finding

    def test_identical_hardware_noted(self):
        section = _get_google_io_section()
        finding = section.get('chokkattu_dual_standard_evidence', {}).get('finding', '')
        assert 'identical' in finding.lower() or 'same' in finding.lower()

    def test_meta_io_framing_contrast(self):
        section = _get_google_io_section()
        finding = section.get('chokkattu_dual_standard_evidence', {}).get('finding', '')
        # Must contrast Google coverage (zero surveillance) with Meta coverage (mass surveillance)
        assert 'zero' in finding.lower() or 'no surveillance' in finding.lower() or \
               'without' in finding.lower()


class TestCondeNastFinancialCorrelation:
    """Verify the Condé Nast financial relationship correlation is documented."""

    def test_financial_section_exists(self):
        section = _get_google_io_section()
        assert 'conde_nast_financial_correlation' in section

    def test_google_ad_revenue_noted(self):
        section = _get_google_io_section()
        finding = section.get('conde_nast_financial_correlation', {}).get('finding', '')
        assert 'advertising' in finding.lower() or 'ad revenue' in finding.lower()

    def test_meta_zero_revenue_noted(self):
        section = _get_google_io_section()
        finding = section.get('conde_nast_financial_correlation', {}).get('finding', '')
        assert 'ZERO' in finding or 'zero' in finding.lower() or 'no revenue' in finding.lower()

    def test_all_four_entities_compared(self):
        section = _get_google_io_section()
        finding = section.get('conde_nast_financial_correlation', {}).get('finding', '')
        for entity in ['Google', 'Snap', 'Apple', 'Meta']:
            assert entity in finding, f"Financial correlation must compare {entity}"

    def test_framing_tracks_financial(self):
        section = _get_google_io_section()
        finding = section.get('conde_nast_financial_correlation', {}).get('finding', '')
        # Must document the correlation between financial relationship and coverage tone
        assert 'surveillance' in finding.lower() or 'creep' in finding.lower() or \
               'alarm' in finding.lower()
