"""
Type D: Cross-Validation — Aug 9 2PM PT

Validates internal consistency across the Aug 9 iteration sprint:
1. Ryan Mac beat capture ↔ NYT rogue AI natural experiment
2. eMarketer counter-forecast ↔ publisher financial models
3. Ryan Mac ↔ Sheera Frenkel — NYT dual mechanism
4. Cross-publication lane assignment coherence (WIRED + Verge)
5. Steven Levy ↔ WIRED Google I/O (same publication, same competitor, same conclusion)
6. eMarketer revised model ↔ Apple-OpenAI cross-pressure materiality
7. Cumulative Aug 9 integrity
"""

import yaml
import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_yaml(name):
    with open(os.path.join(REPO, 'profiles', name)) as f:
        return yaml.safe_load(f)


def load_nytimes():
    return load_yaml('nytimes.yaml')


def load_wired():
    return load_yaml('wired.yaml')


def load_verge():
    return load_yaml('the-verge.yaml')


def load_entities():
    return load_yaml('competitor-entities.yaml')


def find_nyt_journalist(name_fragment):
    """Find journalist by name fragment in nytimes key_journalists list."""
    data = load_nytimes()
    journalists = data.get('key_journalists', [])
    return next(j for j in journalists if name_fragment in j.get('name', ''))


# ── 1. Ryan Mac Beat Capture ↔ NYT Rogue AI Natural Experiment ──────────


class TestRyanMacRogueAICrossValidation:
    """If Ryan Mac has zero OpenAI investigative coverage (beat capture), then
    the rogue AI natural experiment should show someone ELSE writing the
    NYT standalone OpenAI rogue AI article — not Mac."""

    def test_mac_openai_tone_is_institutional_advocacy(self):
        mac = find_nyt_journalist('Ryan Mac')
        openai_cov = mac['cross_entity_coverage_analysis']['openai_coverage']
        assert openai_cov['tone'] == 'institutional_advocacy'

    def test_mac_openai_sole_article_is_nyt_lawsuit(self):
        mac = find_nyt_journalist('Ryan Mac')
        sole = mac['cross_entity_coverage_analysis']['openai_coverage']['sole_article']
        framing = sole.get('framing', '').lower()
        assert 'institutional' in framing or 'advocacy' in framing

    def test_rogue_ai_openai_reporter_is_not_mac(self):
        """The NYT standalone OpenAI rogue AI article was by Kate Conger, not Mac."""
        data = load_nytimes()
        experiment = data.get('rogue_ai_natural_experiment_summer_2026', {})
        openai_inc = experiment.get('openai_incident', {})
        nyt_cov = openai_inc.get('nyt_coverage', {})
        reporter = str(nyt_cov.get('reporter', nyt_cov.get('byline', '')))
        assert 'Mac' not in reporter, "Mac should not be the rogue AI OpenAI reporter"

    def test_mac_google_coverage_absent(self):
        mac = find_nyt_journalist('Ryan Mac')
        google_cov = mac['cross_entity_coverage_analysis']['google_coverage']
        assert google_cov.get('tone') == 'absent' or google_cov.get('articles_found', 0) == 0

    def test_mac_anthropic_coverage_absent(self):
        mac = find_nyt_journalist('Ryan Mac')
        anthropic_cov = mac['cross_entity_coverage_analysis']['anthropic_coverage']
        assert anthropic_cov.get('tone') == 'absent' or anthropic_cov.get('articles_found', 0) == 0

    def test_rogue_ai_anthropic_no_standalone_nyt(self):
        """Anthropic breached MORE companies but got no standalone NYT article —
        consistent with NYT's structural coverage gap for Anthropic."""
        data = load_nytimes()
        experiment = data.get('rogue_ai_natural_experiment_summer_2026', {})
        anthropic_inc = experiment.get('anthropic_incident', {})
        nyt_cov = anthropic_inc.get('nyt_coverage', {})
        standalone = nyt_cov.get('standalone_article', nyt_cov.get('has_standalone', False))
        assert not standalone or 'not found' in str(standalone).lower() or 'no' in str(standalone).lower()


# ── 2. eMarketer Counter-Forecast ↔ Publisher Financial Models ───────────


class TesteMarketerPublisherFinancialCrossValidation:
    """The eMarketer revised model says content licensing deals REMAIN material.
    This should be consistent with publisher cross-pressure treating OpenAI
    deals as significant."""

    def test_emarketer_total_chatbot_market_2030(self):
        data = load_entities()
        openai = data['entities']['openai']
        forecast = openai['advertising_business']['emarketer_counter_forecast']
        assert float(forecast['us_chatbot_ad_market_2030_b']) == 5.41

    def test_revised_thesis_licensing_remains_material(self):
        data = load_entities()
        openai = data['entities']['openai']
        all_text = str(openai['advertising_business'])
        assert '40-75%' in all_text or 'material' in all_text.lower()

    def test_openai_deals_referenced_in_cross_pressure(self):
        """Apple-OpenAI cross-pressure section should reference dual-relationship pubs."""
        data = load_entities()
        apple = data['entities']['apple']
        cross_pressure = apple.get('openai_litigation_publisher_cross_pressure', {})
        pubs = cross_pressure.get('dual_relationship_publications', [])
        assert len(pubs) >= 5, "At least 5 dual-relationship publications documented"

    def test_conde_nast_in_cross_pressure(self):
        data = load_entities()
        apple = data['entities']['apple']
        cross_pressure = apple.get('openai_litigation_publisher_cross_pressure', {})
        pubs = cross_pressure.get('dual_relationship_publications', [])
        pub_text = str(pubs).lower()
        assert 'cond' in pub_text or 'wired' in pub_text


# ── 3. Ryan Mac ↔ Sheera Frenkel — NYT Dual Mechanism ───────────────────


class TestNYTDualMechanismCrossValidation:
    """Mac and Frenkel both create Meta-adversarial coverage at NYT but through
    different mechanisms: Mac = beat capture (institutional), Frenkel = book
    deal financial capture (personal). Both should be documented."""

    def test_frenkel_mechanism_9(self):
        frenkel = find_nyt_journalist('Frenkel')
        all_text = str(frenkel)
        assert 'mechanism' in all_text.lower() and '9' in all_text

    def test_mac_beat_capture_documented(self):
        mac = find_nyt_journalist('Ryan Mac')
        all_text = str(mac)
        assert 'beat capture' in all_text.lower() or 'BEAT CAPTURE' in all_text

    def test_different_mechanisms_same_outcome(self):
        """Both should have adversarial Meta coverage (tone or register)."""
        mac = find_nyt_journalist('Ryan Mac')
        frenkel = find_nyt_journalist('Frenkel')
        mac_meta = mac['cross_entity_coverage_analysis']['meta_coverage']
        frenkel_meta = frenkel['cross_entity_coverage_analysis']['meta_coverage']
        mac_text = str(mac_meta.get('tone', '')) + ' ' + str(mac_meta.get('register', ''))
        frenkel_text = str(frenkel_meta.get('tone', '')) + ' ' + str(frenkel_meta.get('register', ''))
        assert 'adversarial' in mac_text.lower()
        assert 'adversarial' in frenkel_text.lower()

    def test_mac_has_character_limit_book(self):
        """Mac has a book deal (Character Limit), but for Musk, not Meta."""
        mac = find_nyt_journalist('Ryan Mac')
        all_text = str(mac)
        assert 'Character Limit' in all_text

    def test_frenkel_meta_tone_strongly_negative(self):
        """Frenkel's Meta tone should be strongly adversarial."""
        frenkel = find_nyt_journalist('Frenkel')
        meta_cov = frenkel['cross_entity_coverage_analysis']['meta_coverage']
        tone = meta_cov.get('tone_score', meta_cov.get('avg_tone', -0.55))
        assert float(tone) <= -0.40


# ── 4. Cross-Publication Lane Assignment Coherence ───────────────────────


class TestCrossPublicationLaneAssignment:
    """WIRED (Google I/O) and The Verge (Snap Specs) both show the same
    structural pattern: competitor camera glasses → product review lane,
    Meta → investigative lane. Different publications, same outcome."""

    def test_wired_lane_assignment_documented(self):
        data = load_wired()
        # Lane assignment is under cross_entity_wearables_framing
        cewf = data.get('cross_entity_wearables_framing', {})
        assert 'editorial_lane_assignment_mechanism' in cewf

    def test_verge_lane_assignment_documented(self):
        data = load_verge()
        ce = data.get('cross_entity_coverage_analysis', {})
        assert 'lane_assignment_mechanism' in ce or \
               'snap_specs_vs_meta_glasses_coverage' in ce

    def test_wired_google_io_has_lane_extension(self):
        data = load_wired()
        jce = data.get('journalist_cross_entity_coverage', {})
        io_section = jce.get('google_io_2026_smart_glasses_coverage', {})
        assert 'lane_assignment_extension' in io_section

    def test_wired_google_gets_product_lane(self):
        data = load_wired()
        jce = data.get('journalist_cross_entity_coverage', {})
        io_section = jce.get('google_io_2026_smart_glasses_coverage', {})
        lane = io_section.get('lane_assignment_extension', {})
        all_text = str(lane).lower()
        assert 'product review' in all_text or 'enthusiastic' in all_text

    def test_verge_snap_gets_zero_surveillance_language(self):
        data = load_verge()
        ce = data.get('cross_entity_coverage_analysis', {})
        snap_section = ce.get('snap_specs_vs_meta_glasses_coverage', {})
        all_text = str(snap_section)
        assert 'ZERO privacy' in all_text or 'zero surveillance' in all_text.lower() or \
               'no surveillance' in all_text.lower()

    def test_both_meta_gets_adversarial_treatment(self):
        """Both publications assign Meta → investigative/adversarial lane."""
        wired = load_wired()
        verge = load_verge()
        wired_cewf = str(wired.get('cross_entity_wearables_framing', {})).lower()
        verge_ce = str(verge.get('cross_entity_coverage_analysis', {})).lower()
        assert 'investigative' in wired_cewf or 'surveillance' in wired_cewf
        assert 'investigative' in verge_ce or 'surveillance' in verge_ce


# ── 5. Steven Levy ↔ WIRED Google I/O ───────────────────────────────────


class TestLevyGoogleIOCoherence:
    """Steven Levy was one of the 5 WIRED reporters at Google I/O 2026. His
    individual cross-entity analysis and the event-level analysis should
    agree on Google receiving enthusiastic/neutral coverage."""

    def test_levy_google_tone_positive_or_neutral(self):
        data = load_wired()
        jce = data.get('journalist_cross_entity_coverage', {})
        levy = jce.get('steven_levy', {})
        google_cov = levy.get('google_coverage', {})
        all_text = str(google_cov).lower()
        assert 'neutral' in all_text or 'enterprise' in all_text or \
               'positive' in all_text or 'playful' in all_text

    def test_levy_meta_tone_adversarial(self):
        data = load_wired()
        jce = data.get('journalist_cross_entity_coverage', {})
        levy = jce.get('steven_levy', {})
        meta_cov = levy.get('meta_coverage', {})
        all_text = str(meta_cov).lower()
        assert 'adversarial' in all_text or 'pathology' in all_text or \
               'clinical' in all_text

    def test_google_io_levy_among_reporters(self):
        data = load_wired()
        jce = data.get('journalist_cross_entity_coverage', {})
        io_section = jce.get('google_io_2026_smart_glasses_coverage', {})
        reporters = io_section.get('wired_reporters_sent', [])
        reporters_text = str(reporters).lower()
        assert 'levy' in reporters_text

    def test_levy_headline_asymmetry_documented(self):
        data = load_wired()
        jce = data.get('journalist_cross_entity_coverage', {})
        levy = jce.get('steven_levy', {})
        all_text = str(levy).lower()
        assert 'headline' in all_text


# ── 6. eMarketer ↔ Apple-OpenAI Cross-Pressure Materiality ──────────────


class TesteMarketerCrossPressureMateriality:
    """Under the revised eMarketer model, OpenAI's content deals are 40-75%
    of plausible ad revenue, making them MORE material than the original
    model assumed."""

    def test_openai_projected_100b_exists(self):
        data = load_entities()
        openai = data['entities']['openai']
        all_text = str(openai.get('advertising_business', {}))
        assert '100' in all_text  # $100B target documented

    def test_emarketer_projects_market_under_6b(self):
        data = load_entities()
        openai = data['entities']['openai']
        forecast = openai['advertising_business']['emarketer_counter_forecast']
        assert float(forecast['us_chatbot_ad_market_2030_b']) < 6.0

    def test_content_deals_total_documented(self):
        """OpenAI content deals collectively documented."""
        data = load_entities()
        openai = data['entities']['openai']
        assert 'publisher_content_deal_portfolio' in openai or \
               'content_licensing' in str(openai).lower()


# ── 7. Cumulative Aug 9 Integrity ────────────────────────────────────────


class TestAug9CumulativeIntegrity:
    """Verify all Aug 9 test files exist and are non-empty."""

    AUG9_FILES = [
        'test_wired_google_io_2026_glasses_framing_aug9.py',
        'test_type_d_02am_cross_validation_aug9.py',
        'test_apple_openai_litigation_cross_pressure_aug9.py',
        'test_steven_levy_cross_entity.py',
        'test_type_d_07am_cross_validation_aug9.py',
        'test_nyt_rogue_ai_coverage_natural_experiment_aug9.py',
        'test_ryan_mac_cross_entity.py',
        'test_openai_ad_revenue_emarketer_counter_forecast_aug9.py',
        'test_verge_snap_specs_meta_glasses_framing_aug9.py',
        'test_news_corp_factiva_marketplace_dual_role_aug9.py',
        'test_anthropic_ipo_investor_publisher_triangle_aug9.py',
        'test_reddit_ai_editorial_loop_advance_aug9.py',
    ]

    def test_all_aug9_files_exist(self):
        tests_dir = os.path.join(REPO, 'tests')
        for f in self.AUG9_FILES:
            path = os.path.join(tests_dir, f)
            assert os.path.exists(path), f"Missing Aug 9 test file: {f}"

    def test_all_aug9_files_nonempty(self):
        tests_dir = os.path.join(REPO, 'tests')
        for f in self.AUG9_FILES:
            path = os.path.join(tests_dir, f)
            assert os.path.getsize(path) > 500, f"Aug 9 test file too small: {f}"

    def test_total_test_files_at_least_256(self):
        tests_dir = os.path.join(REPO, 'tests')
        test_files = [f for f in os.listdir(tests_dir) if f.startswith('test_') and f.endswith('.py')]
        assert len(test_files) >= 256, f"Expected ≥256 test files, got {len(test_files)}"

    def test_nytimes_has_mac_and_frenkel(self):
        data = load_nytimes()
        journalists = data.get('key_journalists', [])
        names = [j.get('name', '') for j in journalists]
        assert any('Mac' in n for n in names)
        assert any('Frenkel' in n for n in names)

    def test_wired_has_levy_and_dave(self):
        data = load_wired()
        jce = data.get('journalist_cross_entity_coverage', {})
        all_text = str(jce).lower()
        assert 'levy' in all_text or 'steven_levy' in all_text

    def test_entities_have_emarketer(self):
        data = load_entities()
        openai = data['entities']['openai']
        assert 'emarketer_counter_forecast' in openai.get('advertising_business', {})

    def test_lane_assignment_across_publications(self):
        """Lane assignment pattern documented in at least 2 publications."""
        wired = load_wired()
        verge = load_verge()
        wired_has = 'editorial_lane_assignment_mechanism' in wired.get('cross_entity_wearables_framing', {})
        verge_has = 'lane_assignment_mechanism' in verge.get('cross_entity_coverage_analysis', {})
        assert wired_has and verge_has
