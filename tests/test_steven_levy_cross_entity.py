"""
Steven Levy Cross-Entity Framing Analysis

Type B: Journalist Cross-Entity Tracking — Steven Levy (WIRED Editor at Large)

FINDING: Levy applies systematically different headline framing to Meta vs. competitors.
Meta receives institutional-pathology language ("relentless," "self-defeating," "dark mood,"
"punish a defector"). Google receives neutral enterprise framing. Other competitors receive
personality-driven curiosity framing ("wild hunt," "dream house," platforming CEO quotes).

This is significant because Levy IS Wired's institutional voice — longest-tenured, most
CEO access, effectively sets the publication's editorial posture. His Meta framing patterns
are therefore WIRED's Meta framing patterns.

KEY ACCESS DYNAMIC: Levy wrote books requiring deep access to both Google leadership
(In the Plex, 2011) and Facebook/Meta leadership (Facebook: The Inside Story, 2020).
Post-Google-book: warm relationship maintained, continued I/O attendance, no adversarial turn.
Post-Facebook-book: shift to adversarial coverage — Wynn-Williams sympathy, whistleblower
amplification, "dark mood" institutional diagnosis.

FINANCIAL CORRELATION: Condé Nast parent Advance Publications owns 65.2% voting power in
Reddit, a direct Meta competitor. Levy's adversarial Meta coverage and protective Google/other
coverage correlates with Advance's competitive interests.

Source: BuzzSumo journalist profile, Techmeme aggregation of Levy articles (2026),
WIRED Google I/O 2026 live blog analysis (from Type A 03:00 iteration).
"""

import pytest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_wired_profile():
    with open(os.path.join(PROFILES_DIR, 'wired.yaml'), 'r') as f:
        return yaml.safe_load(f)


def load_journalists():
    with open(os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml'), 'r') as f:
        return yaml.safe_load(f)


def get_levy_career(journalists_data):
    for entry in journalists_data.get('journalists', []):
        if entry.get('name') == 'Steven Levy':
            return entry
    return None


def get_levy_cross_entity(wired_profile):
    """Extract the Steven Levy cross-entity section from wired.yaml."""
    ce = wired_profile.get('journalist_cross_entity_coverage', {})
    return ce.get('steven_levy', {})


# === CLASS 1: Career and Institutional Position ===

class TestLevyInstitutionalPosition:
    """Validates that Levy's unique institutional role is documented."""

    def test_levy_exists_in_journalists_yaml(self):
        data = load_journalists()
        levy = get_levy_career(data)
        assert levy is not None, "Steven Levy must exist in journalists.yaml"

    def test_levy_is_editor_at_large(self):
        data = load_journalists()
        levy = get_levy_career(data)
        career = levy.get('career', [])
        current_roles = [c for c in career if c.get('end', '') == 'present' or str(c.get('end', '')).startswith('20') and int(str(c.get('end', ''))[:4]) >= 2026]
        wired_roles = [c for c in career if 'wired' in str(c.get('publication', '')).lower()]
        assert any('editor' in str(c.get('role', '')).lower() for c in wired_roles), \
            "Levy should have an editor role at WIRED"

    def test_levy_has_multi_decade_tenure(self):
        data = load_journalists()
        levy = get_levy_career(data)
        notes = levy.get('notes', '')
        assert '45+' in notes or 'longest' in notes.lower() or 'institutional' in notes.lower(), \
            "Levy's notes should reflect his uniquely long tenure"

    def test_levy_wrote_google_book(self):
        data = load_journalists()
        levy = get_levy_career(data)
        notes = levy.get('notes', '')
        assert 'In the Plex' in notes, \
            "Levy's Google book (In the Plex) must be documented — it establishes access dependency"

    def test_levy_wrote_facebook_book(self):
        data = load_journalists()
        levy = get_levy_career(data)
        notes = levy.get('notes', '')
        assert 'Facebook' in notes or 'Inside Story' in notes, \
            "Levy's Facebook book must be documented — it establishes the pre/post access shift"

    def test_levy_is_wired_institutional_voice(self):
        data = load_journalists()
        levy = get_levy_career(data)
        notes = levy.get('notes', '')
        assert 'institutional voice' in notes.lower() or 'institutional' in notes.lower(), \
            "Levy should be documented as WIRED's institutional voice"


# === CLASS 2: Meta Headline Framing ===

class TestLevyMetaHeadlineFraming:
    """Validates that Levy's adversarial Meta headline patterns are documented."""

    def test_cross_entity_section_exists(self):
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        assert levy_ce, "Steven Levy cross-entity section must exist in wired.yaml"

    def test_meta_coverage_documented(self):
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        meta = levy_ce.get('meta_coverage', {})
        assert meta, "Meta coverage section must exist"

    def test_wynn_williams_article_documented(self):
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        meta = levy_ce.get('meta_coverage', {})
        articles = meta.get('articles', [])
        titles = [a.get('title', '') for a in articles]
        assert any('careless people' in t.lower() or 'wynn-williams' in t.lower() or 'relentless' in t.lower()
                    for t in titles), \
            "The Wynn-Williams/Careless People article must be documented"

    def test_dark_mood_article_documented(self):
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        meta = levy_ce.get('meta_coverage', {})
        articles = meta.get('articles', [])
        titles = [a.get('title', '') for a in articles]
        assert any('dark mood' in t.lower() for t in titles), \
            "The 'Dark Mood Inside Meta' article must be documented"

    @pytest.mark.parametrize("loaded_term", [
        "relentless",
        "self-defeating",
        "dark mood",
    ])
    def test_meta_loaded_language_documented(self, loaded_term):
        """Each loaded language term used in Meta headlines must be documented."""
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        meta = levy_ce.get('meta_coverage', {})
        meta_str = str(meta).lower()
        assert loaded_term.lower() in meta_str, \
            f"Loaded term '{loaded_term}' in Levy's Meta coverage must be documented"

    def test_meta_framing_classified_as_institutional_pathology(self):
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        meta = levy_ce.get('meta_coverage', {})
        framing_type = meta.get('dominant_framing', '')
        assert 'institutional' in framing_type.lower() or 'pathology' in framing_type.lower() or \
               'adversarial' in framing_type.lower(), \
            "Meta framing should be classified as institutional-pathology or adversarial"


# === CLASS 3: Google Headline Framing ===

class TestLevyGoogleHeadlineFraming:
    """Validates that Levy's neutral Google framing is documented and contrasted."""

    def test_google_coverage_documented(self):
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        google = levy_ce.get('google_coverage', {})
        assert google, "Google coverage section must exist"

    def test_google_brain_drain_article_documented(self):
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        google = levy_ce.get('google_coverage', {})
        articles = google.get('articles', [])
        titles = [a.get('title', '') for a in articles]
        assert any('discovery loop' in t.lower() or 'brains' in t.lower() or 'leaving' in t.lower()
                    for t in titles), \
            "The Google brain drain/Discovery Loop article must be documented"

    def test_google_io_presence_documented(self):
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        google = levy_ce.get('google_coverage', {})
        google_str = str(google).lower()
        assert 'i/o' in google_str or 'io 2026' in google_str or 'google i' in google_str, \
            "Levy's presence at Google I/O 2026 must be documented"

    def test_google_framing_classified_as_neutral(self):
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        google = levy_ce.get('google_coverage', {})
        framing_type = google.get('dominant_framing', '')
        assert 'neutral' in framing_type.lower() or 'enterprise' in framing_type.lower() or \
               'curiosity' in framing_type.lower(), \
            "Google framing should be classified as neutral/enterprise — no institutional pathology"

    def test_no_loaded_language_in_google_headlines(self):
        """Google headlines should lack the loaded terms used for Meta."""
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        google = levy_ce.get('google_coverage', {})
        articles = google.get('articles', [])
        meta_loaded_terms = ['relentless', 'self-defeating', 'dark mood', 'punish', 'defector']
        for article in articles:
            title = article.get('title', '').lower()
            for term in meta_loaded_terms:
                assert term not in title, \
                    f"Google headline '{article.get('title', '')}' should not contain Meta-loaded term '{term}'"


# === CLASS 4: Other Competitor Framing ===

class TestLevyOtherCompetitorFraming:
    """Validates that Levy's personality-driven competitor framing is documented."""

    def test_other_competitor_coverage_documented(self):
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        other = levy_ce.get('other_competitor_coverage', {})
        assert other, "Other competitor coverage section must exist"

    def test_bezos_article_documented(self):
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        other = levy_ce.get('other_competitor_coverage', {})
        articles = other.get('articles', [])
        titles = [a.get('title', '') for a in articles]
        assert any('bezos' in t.lower() or 'wild hunt' in t.lower() or 'core algorithm' in t.lower()
                    for t in titles), \
            "The Bezos 'Wild Hunt' article must be documented"

    def test_microsoft_article_documented(self):
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        other = levy_ce.get('other_competitor_coverage', {})
        articles = other.get('articles', [])
        titles = [a.get('title', '') for a in articles]
        assert any('microsoft' in t.lower() or 'mojo' in t.lower()
                    for t in titles), \
            "The Microsoft 'Lost Its Mojo' article must be documented"

    def test_lyft_article_documented(self):
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        other = levy_ce.get('other_competitor_coverage', {})
        articles = other.get('articles', [])
        titles = [a.get('title', '') for a in articles]
        assert any('lyft' in t.lower() or 'good uber' in t.lower()
                    for t in titles), \
            "The Lyft CEO-platforming article must be documented"

    def test_competitor_framing_classified_as_personality_driven(self):
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        other = levy_ce.get('other_competitor_coverage', {})
        framing_type = other.get('dominant_framing', '')
        assert 'personality' in framing_type.lower() or 'curiosity' in framing_type.lower() or \
               'platform' in framing_type.lower(), \
            "Other competitor framing should be classified as personality-driven/curiosity"


# === CLASS 5: Headline Diagnostic Asymmetry ===

class TestLevyHeadlineDiagnosticAsymmetry:
    """Tests the core finding: Meta gets institutional diagnosis, competitors don't."""

    def test_asymmetry_finding_documented(self):
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        finding = levy_ce.get('key_finding', '')
        assert finding, "A key finding must be documented"
        finding_lower = finding.lower()
        assert 'meta' in finding_lower and ('asymmetr' in finding_lower or 'different' in finding_lower or
               'institutional' in finding_lower), \
            "Key finding must describe the Meta framing asymmetry"

    def test_meta_dark_mood_vs_microsoft_mojo(self):
        """Same editorial concept (company struggling) — different register.
        Meta: 'Dark Mood' (clinical pathology). Microsoft: 'Lost Its Mojo' (affectionate/playful)."""
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        comparisons = levy_ce.get('headline_comparisons', [])
        assert len(comparisons) >= 1, "At least one headline comparison must exist"
        comp_str = str(comparisons).lower()
        assert 'dark mood' in comp_str or 'mojo' in comp_str, \
            "Dark Mood vs Mojo comparison should be documented"

    def test_meta_defector_framing_vs_google_brain_drain(self):
        """Same editorial concept (people leaving) — different register.
        Meta: 'punish a defector' (institutional retribution).
        Google: 'Top AI Brains Are Leaving to Launch' (entrepreneurial opportunity)."""
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        comparisons = levy_ce.get('headline_comparisons', [])
        comp_str = str(comparisons).lower()
        assert 'defector' in comp_str or 'brain' in comp_str or 'leaving' in comp_str, \
            "Defector vs brain drain framing comparison should be documented"

    def test_meta_never_gets_ceo_platform(self):
        """Competitors get CEO-platforming headlines (Lyft CEO's own quote as headline).
        Meta's CEO voice is filtered through adversarial editorial framing."""
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        finding_detail = levy_ce.get('ceo_platforming_asymmetry', '')
        assert finding_detail or any(
            'platform' in str(c).lower() for c in levy_ce.get('headline_comparisons', [])
        ), "CEO-platforming asymmetry should be documented"


# === CLASS 6: Access Dependency and Book Trajectory ===

class TestLevyAccessDependency:
    """Tests the access-book-coverage trajectory for Google vs Meta."""

    def test_access_trajectory_documented(self):
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        access = levy_ce.get('access_dependency_analysis', {})
        assert access, "Access dependency analysis must exist"

    def test_google_post_book_warm(self):
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        access = levy_ce.get('access_dependency_analysis', {})
        google = access.get('google_trajectory', '')
        assert 'warm' in google.lower() or 'maintained' in google.lower() or 'no adversarial' in google.lower(), \
            "Post-In the Plex, Levy's Google relationship remained warm"

    def test_meta_post_book_adversarial(self):
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        access = levy_ce.get('access_dependency_analysis', {})
        meta = access.get('meta_trajectory', '')
        assert 'adversarial' in meta.lower() or 'shift' in meta.lower() or 'critical' in meta.lower(), \
            "Post-Facebook book, Levy's Meta coverage shifted adversarial"

    def test_advance_financial_correlation(self):
        """The post-book divergence correlates with Advance's competitive position:
        Reddit (Advance-owned) competes with Meta, not with Google."""
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        access = levy_ce.get('access_dependency_analysis', {})
        advance = access.get('advance_financial_correlation', '')
        assert 'advance' in advance.lower() or 'reddit' in advance.lower() or \
               'condé nast' in advance.lower() or 'conde nast' in advance.lower(), \
            "Advance/Reddit competitive correlation must be documented"


# === CLASS 7: Whistleblower Amplification Pattern ===

class TestLevyWhistleblowerAmplification:
    """Tests whether Levy amplifies Meta whistleblowers more than competitors'."""

    def test_haugen_coverage_documented(self):
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        whistleblower = levy_ce.get('whistleblower_amplification', {})
        wb_str = str(whistleblower).lower()
        assert 'haugen' in wb_str, "Frances Haugen coverage must be documented"

    def test_wynn_williams_sympathy_documented(self):
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        whistleblower = levy_ce.get('whistleblower_amplification', {})
        wb_str = str(whistleblower).lower()
        assert 'wynn' in wb_str or 'careless people' in wb_str, \
            "Wynn-Williams sympathy framing must be documented"

    def test_google_whistleblower_absence_noted(self):
        """Google has had whistleblowers (Timnit Gebru, Blake Lemoine, etc.)
        but Levy's coverage of Google whistleblowers differs in tone."""
        profile = load_wired_profile()
        levy_ce = get_levy_cross_entity(profile)
        whistleblower = levy_ce.get('whistleblower_amplification', {})
        wb_str = str(whistleblower).lower()
        assert 'google' in wb_str or 'competitor' in wb_str or 'asymmetr' in wb_str, \
            "Google/competitor whistleblower treatment comparison must be documented"
