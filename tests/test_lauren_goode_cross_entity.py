"""
Cross-entity coverage analysis for Lauren Goode (WIRED Senior Correspondent).

Key finding: WIRED's most senior consumer tech correspondent shows a systematic
framing divergence when covering wearable hardware from different manufacturers:
- Apple Vision Pro (12 cameras, 6 mics): emotional empathy, ZERO surveillance language
- Snap Spectacles (face camera): playful positive, ZERO privacy language
- Meta Ray-Ban glasses (1 camera): clinical/skeptical, then editorial avoidance post-2023
- Post-2023 beat shift to AI semiconductors coincides with Meta glasses becoming
  WIRED's most surveilled product

Executive access asymmetry: Jensen Huang (Nvidia), Lisa Su (AMD), Rene Haas (Arm),
Mike Krieger (Anthropic) — all 1-on-1 interviews — but ZERO with Meta executives
(Zuckerberg, Bosworth, LeCun) despite Meta being her former primary beat.
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_wired_profile():
    with open(os.path.join(PROFILES_DIR, 'wired.yaml')) as f:
        return yaml.safe_load(f)


def load_journalists():
    with open(os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml')) as f:
        return yaml.safe_load(f)


def get_goode_profile(journalists_data):
    for j in journalists_data.get('journalists', []):
        if j.get('name') == 'Lauren Goode':
            return j
    return None


class TestGoodeHasCompetitorCoverage:
    """Lauren Goode's journalist profile must include competitor_coverage section."""

    def test_goode_exists_in_profiles(self):
        data = load_journalists()
        profile = get_goode_profile(data)
        assert profile is not None, "Lauren Goode must be in journalists.yaml"

    def test_has_competitor_coverage_section(self):
        data = load_journalists()
        profile = get_goode_profile(data)
        assert 'competitor_coverage' in profile, \
            "Lauren Goode must have a competitor_coverage section"

    def test_has_apple_coverage(self):
        data = load_journalists()
        profile = get_goode_profile(data)
        cc = profile.get('competitor_coverage', {})
        assert 'apple' in cc, "Must document Apple coverage"

    def test_has_snap_coverage(self):
        data = load_journalists()
        profile = get_goode_profile(data)
        cc = profile.get('competitor_coverage', {})
        assert 'snap' in cc, "Must document Snap coverage"

    def test_has_meta_coverage(self):
        data = load_journalists()
        profile = get_goode_profile(data)
        cc = profile.get('competitor_coverage', {})
        assert 'meta' in cc, "Must document Meta coverage analysis"


class TestGoodeAppleFraming:
    """Apple Vision Pro coverage uses emotional empathy, zero surveillance language."""

    def test_apple_tone_is_empathetic(self):
        data = load_journalists()
        profile = get_goode_profile(data)
        apple = profile['competitor_coverage']['apple']
        assert apple['tone'] in ('empathetic_wonder', 'empathetic', 'positive_emotional'), \
            f"Apple tone must be empathetic, got {apple['tone']}"

    def test_apple_has_examples(self):
        data = load_journalists()
        profile = get_goode_profile(data)
        apple = profile['competitor_coverage']['apple']
        assert 'examples' in apple and len(apple['examples']) >= 2, \
            "Apple coverage must have at least 2 documented examples"

    def test_apple_vision_pro_review_has_emotional_framing(self):
        """The 'I Cried Inside the Apple Vision Pro' review uses first-person emotional language."""
        data = load_journalists()
        profile = get_goode_profile(data)
        examples = profile['competitor_coverage']['apple']['examples']
        vision_pro_review = None
        for ex in examples:
            title = ex.get('title', '').lower()
            if 'cried' in title or ('vision pro' in title and 'review' in title.lower()):
                vision_pro_review = ex
                break
        assert vision_pro_review is not None, \
            "Must document the 'I Cried Inside the Apple Vision Pro' review"
        notes = vision_pro_review.get('framing_notes', '')
        assert 'surveillance' not in notes.lower() or 'zero' in notes.lower() or 'no' in notes.lower(), \
            "Apple Vision Pro review framing must note absence of surveillance language"

    def test_apple_vision_pro_camera_count_not_mentioned(self):
        """Apple Vision Pro has 12 cameras but Goode never frames them as surveillance risk."""
        data = load_journalists()
        profile = get_goode_profile(data)
        examples = profile['competitor_coverage']['apple']['examples']
        for ex in examples:
            notes = ex.get('framing_notes', '').lower()
            # Notes should document the ABSENCE of surveillance framing,
            # not contain surveillance framing as a characterization
            if 'camera' in notes and 'surveillance' in notes:
                assert any(neg in notes for neg in ['zero', 'no ', 'never', 'not ', 'absence']), \
                    "Camera + surveillance mentions in Apple examples should document absence, not presence"


class TestGoodeSnapFraming:
    """Snap Spectacles coverage uses playful positive framing, zero privacy language."""

    def test_snap_tone_is_positive(self):
        data = load_journalists()
        profile = get_goode_profile(data)
        snap = profile['competitor_coverage']['snap']
        assert snap['tone'] in ('playful_positive', 'positive', 'enthusiastic'), \
            f"Snap tone must be playful/positive, got {snap['tone']}"

    def test_snap_face_camera_framing(self):
        """'The face camera we've been waiting for' — language unthinkable for Meta glasses at WIRED."""
        data = load_journalists()
        profile = get_goode_profile(data)
        snap = profile['competitor_coverage']['snap']
        examples = snap.get('examples', [])
        assert len(examples) >= 1, "Must have at least 1 Snap example"
        face_camera = any('face camera' in ex.get('title', '').lower() for ex in examples)
        assert face_camera, \
            "Must document the 'face camera we've been waiting for' video"


class TestGoodeMetaCoverageGap:
    """Meta hardware coverage disappears from Goode's bylines after 2023."""

    def test_meta_tone_is_avoidance(self):
        data = load_journalists()
        profile = get_goode_profile(data)
        meta = profile['competitor_coverage']['meta']
        assert 'avoidance' in meta.get('tone', '').lower() or \
               'unknown' in meta.get('tone', '').lower() or \
               'absent' in meta.get('tone', '').lower() or \
               'gap' in meta.get('tone', '').lower(), \
            f"Meta tone must reflect editorial avoidance or coverage gap, got {meta.get('tone')}"

    def test_meta_has_coverage_gap_notes(self):
        data = load_journalists()
        profile = get_goode_profile(data)
        meta = profile['competitor_coverage']['meta']
        assert 'coverage_gap_notes' in meta, \
            "Meta section must have coverage_gap_notes explaining the absence"

    def test_coverage_gap_mentions_lane_assignment(self):
        """Gap notes must explain that Meta glasses go to investigative reporters, not Goode."""
        data = load_journalists()
        profile = get_goode_profile(data)
        notes = profile['competitor_coverage']['meta'].get('coverage_gap_notes', '')
        has_lane = any(term in notes.lower() for term in [
            'lane assignment', 'cameron', 'mehrotra', 'investigative',
            'surveillance', 'other wired'
        ])
        assert has_lane, \
            "Coverage gap notes must reference the lane assignment to investigative reporters"


class TestGoodeBeatShift:
    """Goode's beat shifted from consumer tech/wearables to AI semiconductors in 2024-2026,
    coinciding with Meta glasses becoming WIRED's most surveillance-framed product."""

    def test_beat_shift_documented(self):
        data = load_journalists()
        profile = get_goode_profile(data)
        cc = profile.get('competitor_coverage', {})
        # Check for beat shift documentation in meta coverage gap notes or top-level notes
        meta_notes = cc.get('meta', {}).get('coverage_gap_notes', '')
        top_notes = profile.get('notes', '')
        has_shift = any('beat' in text.lower() and any(
            term in text.lower() for term in ['shift', 'expand', 'evolution', 'pivot']
        ) for text in [meta_notes, top_notes])
        assert has_shift, \
            "Must document Goode's beat shift from wearables to AI semiconductors"

    def test_semiconductor_coverage_exists(self):
        """Post-2024 coverage includes Nvidia, AMD, Intel, Arm — all AI semiconductor companies."""
        data = load_journalists()
        profile = get_goode_profile(data)
        cc = profile.get('competitor_coverage', {})
        # Should have semiconductor/chip coverage documented or referenced
        all_text = str(cc) + str(profile.get('notes', ''))
        chip_companies = ['nvidia', 'amd', 'intel', 'arm']
        found = sum(1 for c in chip_companies if c in all_text.lower())
        assert found >= 2, \
            f"Must reference at least 2 chip companies in beat shift documentation, found {found}"


class TestGoodeExecutiveAccessAsymmetry:
    """Goode has 1-on-1 executive interviews with Nvidia, AMD, Arm, Anthropic CEOs
    but ZERO with Meta executives despite Meta being her former primary beat."""

    def test_has_executive_access_section(self):
        data = load_journalists()
        profile = get_goode_profile(data)
        cc = profile.get('competitor_coverage', {})
        # Check for executive_access or interview documentation
        all_text = str(cc)
        has_exec = any(term in all_text.lower() for term in [
            'executive', 'interview', 'jensen', 'lisa su', 'haas', 'krieger'
        ])
        assert has_exec, \
            "Must document executive access patterns across entities"

    def test_nvidia_executive_access(self):
        """Jensen Huang: SIGGRAPH 2024 interview, Jan 2026 Vera Rubin coverage."""
        data = load_journalists()
        profile = get_goode_profile(data)
        cc = profile.get('competitor_coverage', {})
        all_text = str(cc) + str(profile.get('notes', ''))
        assert 'nvidia' in all_text.lower() or 'jensen' in all_text.lower() or \
               'huang' in all_text.lower(), \
            "Must document Nvidia/Jensen Huang executive access"

    def test_anthropic_executive_access(self):
        """Mike Krieger (Anthropic Labs head) co-interview at Big Technology AI Summit Jun 2026."""
        data = load_journalists()
        profile = get_goode_profile(data)
        cc = profile.get('competitor_coverage', {})
        all_text = str(cc) + str(profile.get('notes', ''))
        assert 'anthropic' in all_text.lower() or 'krieger' in all_text.lower(), \
            "Must document Anthropic/Krieger executive access"

    def test_meta_executive_access_zero(self):
        """ZERO 1-on-1 Goode interviews with Zuckerberg, Bosworth, or LeCun."""
        data = load_journalists()
        profile = get_goode_profile(data)
        meta = profile['competitor_coverage']['meta']
        notes = meta.get('coverage_gap_notes', '') + str(meta)
        # Should note the absence of Meta executive interviews
        has_absence = any(term in notes.lower() for term in [
            'zero', 'no ', 'absence', 'never', 'none'
        ])
        assert has_absence, \
            "Must note the absence of Meta executive interviews"


class TestGoodeFramingDivergence:
    """Same journalist, same product category (face-mounted cameras), radically different framing."""

    def test_asymmetry_score_exists(self):
        data = load_journalists()
        profile = get_goode_profile(data)
        cc = profile.get('competitor_coverage', {})
        assert 'cross_entity_asymmetry_score' in cc, \
            "Must have a cross_entity_asymmetry_score"

    def test_asymmetry_score_is_high(self):
        data = load_journalists()
        profile = get_goode_profile(data)
        cc = profile.get('competitor_coverage', {})
        score = cc['cross_entity_asymmetry_score']
        assert score >= 0.7, \
            f"Cross-entity asymmetry score must be >= 0.7 (high divergence), got {score}"

    def test_framing_divergence_documented(self):
        """Must document that identical hardware (cameras on face) receives
        different narrative frames based on manufacturer identity."""
        data = load_journalists()
        profile = get_goode_profile(data)
        cc = profile.get('competitor_coverage', {})
        notes = cc.get('asymmetry_notes', '')
        has_comparison = any(term in notes.lower() for term in [
            'same hardware', 'camera', 'manufacturer', 'narrative frame',
            'face-mounted', 'identical', 'surveillance'
        ])
        assert has_comparison, \
            "Asymmetry notes must document that same hardware gets different frames by manufacturer"


class TestGoodeMetaConnect2023Framing:
    """Meta Connect 2023 article framing is clinical/skeptical — contrasts with Apple empathy."""

    def test_meta_connect_framing_documented(self):
        """The Oct 2023 'Meta's Quest 3 VR Headset and Ray-Ban Smart Glasses' article
        uses clinical language: 'face-computing metaverse still hasn't gone mainstream',
        'most of us would rather bury our faces in the glass slabs in our hands'."""
        data = load_journalists()
        profile = get_goode_profile(data)
        meta = profile['competitor_coverage']['meta']
        all_meta = str(meta).lower()
        # Must reference the Meta Connect 2023 coverage
        has_connect = any(term in all_meta for term in [
            'connect', 'quest 3', '2023', 'face-computing', 'mainstream'
        ])
        assert has_connect, \
            "Must document Meta Connect 2023 article and its clinical framing"

    def test_tone_contrast_with_apple(self):
        """Same journalist's Meta coverage is clinical/skeptical vs Apple's emotional/empathetic."""
        data = load_journalists()
        profile = get_goode_profile(data)
        cc = profile.get('competitor_coverage', {})
        apple_tone = cc.get('apple', {}).get('tone', '')
        meta_tone = cc.get('meta', {}).get('tone', '')
        assert apple_tone != meta_tone, \
            f"Apple tone ({apple_tone}) must differ from Meta tone ({meta_tone})"


class TestGoodeGoogleIO2026:
    """Goode was on-ground at Google I/O 2026 covering Android XR — playful tone,
    zero adversarial/surveillance framing despite Google's smart glasses having cameras."""

    def test_google_io_coverage_documented(self):
        data = load_journalists()
        profile = get_goode_profile(data)
        cc = profile.get('competitor_coverage', {})
        all_text = str(cc) + str(profile.get('notes', ''))
        has_google_io = any(term in all_text.lower() for term in [
            'google i/o', 'android xr', 'intelligent eyewear'
        ])
        assert has_google_io, \
            "Must document Goode's Google I/O 2026 coverage"

    def test_google_glasses_no_surveillance_language(self):
        """Google's Android XR smart glasses (cameras, Gemini AI) get no surveillance framing
        from Goode despite being functionally similar to Meta Ray-Ban glasses."""
        data = load_journalists()
        profile = get_goode_profile(data)
        cc = profile.get('competitor_coverage', {})
        google = cc.get('google', {})
        if google:
            tone = google.get('tone', '').lower()
            assert 'adversarial' not in tone and 'surveillance' not in tone, \
                "Google smart glasses coverage must not use adversarial/surveillance framing"
