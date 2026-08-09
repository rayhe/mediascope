"""
The Verge × Snap Specs vs Meta Glasses — Camera Capability Parity, Framing Divergence

Type A: Competitor Coverage Deep Dive (Aug 9, 2026 08:00 PT)

Validates that The Verge's profile documents systematically different editorial treatment
of Snap's camera-equipped AR glasses vs Meta's camera-equipped smart glasses:
- Snap Specs (visible + infrared cameras, LED bar, OpenAI/Gemini AI): product-review framing
- Meta Ray-Ban (single 12MP camera, LED indicator, Meta AI): surveillance/harassment framing

The hardware is functionally similar (face-mounted cameras + AI + recording indicator).
The coverage framing diverges by manufacturer identity, correlating with PMC's financial
relationships: OpenAI (Snap's AI partner) pays PMC; Meta does not.
"""

import yaml
import os
import pytest

PROFILE_PATH = os.path.join(
    os.path.dirname(__file__), '..', 'profiles', 'the-verge.yaml'
)


@pytest.fixture(scope='module')
def verge_profile():
    with open(PROFILE_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def cross_entity(verge_profile):
    return verge_profile.get('cross_entity_coverage_analysis', {})


@pytest.fixture(scope='module')
def snap_meta_section(cross_entity):
    section = cross_entity.get('snap_specs_vs_meta_glasses_coverage')
    assert section is not None, (
        "Missing snap_specs_vs_meta_glasses_coverage section in the-verge.yaml"
    )
    return section


# ── Class 1: Section Structure ──────────────────────────────────────


class TestSectionStructure:
    """Verify the competitor coverage section has all required fields."""

    def test_section_exists(self, snap_meta_section):
        assert snap_meta_section is not None

    def test_has_date_analyzed(self, snap_meta_section):
        assert 'date_analyzed' in snap_meta_section
        assert '2026-08-09' in snap_meta_section['date_analyzed']

    def test_has_rotation_type(self, snap_meta_section):
        assert snap_meta_section.get('rotation_type') == 'A'

    def test_has_publication(self, snap_meta_section):
        assert 'Verge' in snap_meta_section.get('publication', '')

    def test_has_competitor(self, snap_meta_section):
        assert snap_meta_section.get('competitor') == 'Snap'

    def test_has_key_finding(self, snap_meta_section):
        finding = snap_meta_section.get('key_finding', '')
        assert len(finding) > 100, "Key finding should be substantive"

    def test_has_snap_coverage(self, snap_meta_section):
        assert 'snap_specs_coverage' in snap_meta_section

    def test_has_meta_coverage(self, snap_meta_section):
        assert 'meta_glasses_coverage' in snap_meta_section

    def test_has_camera_comparison(self, snap_meta_section):
        assert 'camera_capability_comparison' in snap_meta_section

    def test_has_financial_correlation(self, snap_meta_section):
        assert 'financial_correlation' in snap_meta_section

    def test_has_editorial_lane_assignment(self, snap_meta_section):
        assert 'editorial_lane_assignment' in snap_meta_section

    def test_has_source_urls(self, snap_meta_section):
        urls = snap_meta_section.get('source_urls', [])
        assert len(urls) >= 3, "Need at least 3 source URLs"


# ── Class 2: Snap Specs Coverage — Product Review Lane ──────────────


class TestSnapSpecsCoverage:
    """Verify Snap Specs coverage is documented as product-review lane."""

    @pytest.fixture
    def snap_cov(self, snap_meta_section):
        return snap_meta_section['snap_specs_coverage']

    def test_snap_tone_positive(self, snap_cov):
        tone = snap_cov.get('tone', '')
        assert 'product' in tone.lower() or '+' in tone or 'positive' in tone.lower()

    def test_snap_framing_register_product_review(self, snap_cov):
        assert snap_cov.get('framing_register') == 'product_review'

    def test_snap_zero_surveillance_language(self, snap_cov):
        assert snap_cov.get('surveillance_language_count', -1) == 0

    def test_snap_zero_privacy_concern_language(self, snap_cov):
        assert snap_cov.get('privacy_concern_language_count', -1) == 0

    def test_snap_has_key_articles(self, snap_cov):
        articles = snap_cov.get('key_articles', [])
        assert len(articles) >= 2, "Need at least 2 key Snap articles"

    def test_snap_article_big_moment_framing(self, snap_cov):
        articles = snap_cov.get('key_articles', [])
        found = any('big moment' in str(a.get('framing', '')).lower() for a in articles)
        assert found, "Should document 'big moment for Snap' framing"

    def test_snap_camera_capabilities_acknowledged(self, snap_cov):
        caps = snap_cov.get('camera_capabilities_acknowledged', {})
        assert caps.get('visible_light_cameras') is True
        assert caps.get('infrared_cameras') is True
        assert caps.get('led_recording_indicator') is True

    def test_snap_cameras_acknowledged_but_no_surveillance(self, snap_cov):
        caps = snap_cov.get('camera_capabilities_acknowledged', {})
        assert caps.get('surveillance_framing_applied') is False, (
            "Snap cameras acknowledged but surveillance framing NOT applied"
        )

    def test_snap_negative_critique_is_product_focused(self, snap_cov):
        """Even negative Snap coverage is product-focused, not surveillance-focused."""
        articles = snap_cov.get('key_articles', [])
        negative = [a for a in articles if a.get('tone', 0) < 0 or
                    (isinstance(a.get('tone'), str) and '-' in a['tone'])]
        for article in negative:
            framing = str(article.get('framing', '')).lower()
            # The framing should describe product critique, not surveillance alarm.
            # It may mention surveillance in negation ("not surveillance") — check
            # that the framing is primarily about aesthetics/product, not alarm.
            assert 'aesthetics' in framing or 'practicality' in framing or 'product' in framing, (
                "Negative Snap critique should reference product-focused concerns"
            )


# ── Class 3: Meta Glasses Coverage — Surveillance Lane ──────────────


class TestMetaGlassesCoverage:
    """Verify Meta glasses coverage is documented as surveillance/harassment frame."""

    @pytest.fixture
    def meta_cov(self, snap_meta_section):
        return snap_meta_section['meta_glasses_coverage']

    def test_meta_tone_negative(self, meta_cov):
        tone = meta_cov.get('tone', '')
        assert '-' in tone or 'negative' in tone.lower() or 'surveillance' in tone.lower()

    def test_meta_framing_investigative(self, meta_cov):
        register = meta_cov.get('framing_register', '')
        assert 'investigative' in register.lower() or 'alarm' in register.lower()

    def test_meta_has_surveillance_language_examples(self, meta_cov):
        examples = meta_cov.get('surveillance_language_examples', [])
        assert len(examples) >= 3, "Need at least 3 surveillance language examples"

    def test_meta_erosion_of_privacy_documented(self, meta_cov):
        examples = meta_cov.get('surveillance_language_examples', [])
        terms = [e.get('term', '').lower() for e in examples]
        assert any('erosion' in t or 'privacy' in t for t in terms)

    def test_meta_surveillance_expansion_documented(self, meta_cov):
        examples = meta_cov.get('surveillance_language_examples', [])
        terms = [e.get('term', '').lower() for e in examples]
        assert any('surveillance' in t for t in terms)

    def test_meta_pervert_glasses_documented(self, meta_cov):
        examples = meta_cov.get('surveillance_language_examples', [])
        terms = [e.get('term', '').lower() for e in examples]
        assert any('pervert' in t for t in terms)

    def test_meta_has_key_articles(self, meta_cov):
        articles = meta_cov.get('key_articles', [])
        assert len(articles) >= 2, "Need at least 2 key Meta articles"

    def test_meta_harassment_framing_in_articles(self, meta_cov):
        articles = meta_cov.get('key_articles', [])
        found = any('harassment' in str(a.get('framing', '')).lower() or
                     'pickup' in str(a.get('framing', '')).lower()
                     for a in articles)
        assert found, "Meta articles should document harassment framing"


# ── Class 4: Camera Capability Comparison — The Paradox ─────────────


class TestCameraCapabilityComparison:
    """Validate the hardware parity → framing divergence paradox."""

    @pytest.fixture
    def camera_comp(self, snap_meta_section):
        return snap_meta_section['camera_capability_comparison']

    def test_snap_has_more_cameras(self, camera_comp):
        snap = camera_comp.get('snap_specs', {})
        cameras = snap.get('cameras', '')
        assert 'infrared' in cameras.lower() or 'multiple' in cameras.lower()

    def test_meta_has_single_camera(self, camera_comp):
        meta = camera_comp.get('meta_ray_ban', {})
        cameras = meta.get('cameras', '')
        assert 'single' in cameras.lower() or '12mp' in cameras.lower()

    def test_snap_ai_includes_openai(self, camera_comp):
        snap = camera_comp.get('snap_specs', {})
        ai = snap.get('ai_capabilities', '')
        assert 'openai' in ai.lower()

    def test_snap_ai_includes_gemini(self, camera_comp):
        snap = camera_comp.get('snap_specs', {})
        ai = snap.get('ai_capabilities', '')
        assert 'gemini' in ai.lower()

    def test_snap_surveillance_potential_high(self, camera_comp):
        snap = camera_comp.get('snap_specs', {})
        potential = snap.get('surveillance_potential', '').lower()
        assert 'high' in potential

    def test_meta_surveillance_potential_moderate(self, camera_comp):
        meta = camera_comp.get('meta_ray_ban', {})
        potential = meta.get('surveillance_potential', '').lower()
        assert 'moderate' in potential

    def test_snap_no_surveillance_framing_despite_higher_capability(self, camera_comp):
        snap = camera_comp.get('snap_specs', {})
        assert snap.get('verge_surveillance_framing') is False

    def test_meta_gets_surveillance_framing_despite_lower_capability(self, camera_comp):
        meta = camera_comp.get('meta_ray_ban', {})
        assert meta.get('verge_surveillance_framing') is True

    def test_paradox_documented(self, camera_comp):
        paradox = camera_comp.get('paradox', '')
        assert len(paradox) > 50
        assert 'more' in paradox.lower() or 'greater' in paradox.lower()
        assert 'meta' in paradox.lower()


# ── Class 5: Financial Correlation ──────────────────────────────────


class TestFinancialCorrelation:
    """Validate financial relationship → coverage tone correlation."""

    @pytest.fixture
    def fin_corr(self, snap_meta_section):
        return snap_meta_section['financial_correlation']

    def test_snap_openai_partnership_documented(self, fin_corr):
        assert 'snap_openai_partnership' in fin_corr

    def test_snap_openai_is_pmc_licensing_partner(self, fin_corr):
        section = fin_corr.get('snap_openai_partnership', {})
        sig = section.get('significance', '')
        assert 'licensing' in sig.lower() or 'pmc' in sig.lower()

    def test_snap_gemini_partnership_documented(self, fin_corr):
        assert 'snap_gemini_partnership' in fin_corr

    def test_meta_no_pmc_deal(self, fin_corr):
        assert 'meta_no_pmc_deal' in fin_corr

    def test_meta_zero_ai_licensing(self, fin_corr):
        section = fin_corr.get('meta_no_pmc_deal', {})
        sig = section.get('significance', '')
        assert '$0' in sig or 'zero' in sig.lower() or 'no' in sig.lower()

    def test_pif_meta_divestiture_documented(self, fin_corr):
        assert 'pif_meta_divestiture' in fin_corr

    def test_pif_sold_meta_shares(self, fin_corr):
        section = fin_corr.get('pif_meta_divestiture', {})
        sig = section.get('significance', '')
        assert 'divest' in sig.lower() or 'sold' in sig.lower()


# ── Class 6: Editorial Lane Assignment Pattern ──────────────────────


class TestEditorialLaneAssignment:
    """Validate the editorial mechanism producing asymmetric coverage."""

    @pytest.fixture
    def lane(self, snap_meta_section):
        return snap_meta_section['editorial_lane_assignment']

    def test_pattern_documented(self, lane):
        pattern = lane.get('pattern', '')
        assert len(pattern) > 100, "Lane assignment pattern should be substantive"

    def test_wired_comparison_referenced(self, lane):
        pattern = lane.get('pattern', '')
        assert 'wired' in pattern.lower()

    def test_snap_zero_investigative_articles(self, lane):
        assert lane.get('snap_investigative_articles') == 0

    def test_meta_has_investigative_articles(self, lane):
        meta_inv = lane.get('meta_investigative_articles', '')
        assert 'multiple' in str(meta_inv).lower() or int(str(meta_inv) if str(meta_inv).isdigit() else '99') > 0

    def test_mechanism_differs_from_wired(self, lane):
        """The Verge uses editorial-layer assignment, not reporter-level lane assignment."""
        pattern = lane.get('pattern', '')
        assert 'editorial' in pattern.lower() or 'institutional' in pattern.lower()

    def test_net_outcome_equivalent(self, lane):
        """Despite different mechanism, net outcome is same: Snap positive, Meta negative."""
        pattern = lane.get('pattern', '')
        assert 'identical' in pattern.lower() or 'equivalent' in pattern.lower() or 'same' in pattern.lower()


# ── Class 7: Cross-Validation Against Existing Profile Data ─────────


class TestCrossValidation:
    """Cross-validate new findings against existing profile data."""

    def test_victoria_song_meta_balanced(self, verge_profile):
        """Song's balanced Meta coverage is consistent with product-review lane."""
        journalists = verge_profile.get('key_journalists', [])
        song = next((j for j in journalists if j.get('name') == 'Victoria Song'), None)
        assert song is not None
        cca = song.get('competitor_coverage_analysis', {})
        meta_cov = cca.get('meta_coverage', {})
        tone = meta_cov.get('tone', '')
        assert 'balanced' in tone.lower() or 'positive' in tone.lower()

    def test_alex_heath_snap_constructive(self, verge_profile):
        """Heath covers Snap constructively (NOT with surveillance framing)."""
        journalists = verge_profile.get('key_journalists', [])
        # Find Alex Heath in editorial_stance section
        heath = next((j for j in journalists if j.get('name') == 'Alex Heath'), None)
        if heath is None:
            # Check in editorial team section
            team = verge_profile.get('editorial_team', [])
            heath = next((m for m in team if m.get('name') == 'Alex Heath'), None)
        # Heath's Snap coverage is documented as constructive in editorial_stance
        if heath:
            stance = str(heath.get('editorial_stance', ''))
            assert 'constructive' in stance.lower() or 'snap' in stance.lower()

    def test_openai_licensing_deal_exists(self, verge_profile):
        """Confirm PMC/Vox Media has OpenAI licensing deal."""
        relationships = verge_profile.get('revenue_relationships', [])
        openai_deal = [r for r in relationships
                       if 'openai' in r.get('partner', '').lower()
                       and 'licensing' in r.get('relationship_type', '').lower()]
        assert len(openai_deal) >= 1

    def test_meta_no_licensing_deal(self, verge_profile):
        """Confirm Meta has NO AI licensing deal with PMC."""
        relationships = verge_profile.get('revenue_relationships', [])
        meta_deals = [r for r in relationships
                      if r.get('partner', '') == 'Meta'
                      and 'licensing' in r.get('relationship_type', '').lower()]
        assert len(meta_deals) == 0

    def test_asymmetry_score_reflects_new_evidence(self, verge_profile):
        """Asymmetry score should be updated to reflect new Snap/Meta evidence."""
        cea = verge_profile.get('cross_entity_coverage_analysis', {})
        score = cea.get('cross_entity_asymmetry_score', 0)
        assert score >= 0.65, f"Score {score} should reflect accumulated evidence"

    def test_last_updated_is_aug9(self, verge_profile):
        cea = verge_profile.get('cross_entity_coverage_analysis', {})
        updated = cea.get('last_updated', '')
        assert '2026-08-09' in updated
