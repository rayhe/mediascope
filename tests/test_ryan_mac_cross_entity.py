"""
Ryan Mac Cross-Entity Framing Analysis

Type B: Journalist Cross-Entity Tracking — Ryan Mac (NYT Tech Accountability)

FINDING: Ryan Mac was hired by the NYT in 2021 for broad "tech accountability" —
the hiring memo explicitly says "all manner of tech companies, tech billionaires
and their ecosystems of influence." His actual coverage concentrates almost
exclusively on two targets: Meta/Facebook and Elon Musk's companies (X, SpaceX,
Tesla). Companies of equal or greater market power — Google, Apple, Amazon,
OpenAI, Anthropic — receive zero independent investigative coverage from Mac.

This represents BEAT CAPTURE: a structural phenomenon where sourcing lock-in,
book-deal financial incentives ('Character Limit' for Musk, paralleling Frenkel's
'An Ugly Truth' for Meta), and institutional assignment patterns concentrate a
journalist's investigative capacity on a narrow set of targets.

Mac's sole OpenAI article (Dec 2023) was the NYT's own copyright lawsuit
announcement, co-written with media reporter Michael Grynbaum — institutional
advocacy, not independent investigative work. OpenAI's motion to dismiss
explicitly cited this article as the NYT "publiciz[ing] its filing and
allegations in its own pages."

Career: Forbes → BuzzFeed News (Polk Award for Facebook, Mirror Award) →
NYT 2021 (tech accountability). Co-authored 'Character Limit' with Kate Conger.
Suspended from Twitter by Musk (Dec 2022). Maye Musk racially targeted Mac
('American Vietnamese reporter,' Nov 2024).

Sources: NYT hiring announcement (nytco.com), Talking Biz News interview,
Techmeme aggregation, OpenAI MTD filing (SDNY Case 1:23-cv-11195),
BuzzFeed News article archive, Muck Rack profile, Poynter addiction trial
coverage, Goodreads/Booktopia 'Character Limit' pages.
"""

import pytest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_nyt_profile():
    with open(os.path.join(PROFILES_DIR, 'nytimes.yaml'), 'r') as f:
        return yaml.safe_load(f)


def get_mac_section(nyt_profile):
    """Extract the Ryan Mac journalist section from nytimes.yaml."""
    reporters = nyt_profile.get('reporters', nyt_profile.get('journalists', []))
    # Try multiple paths — NYT profile structure varies
    for section_name in ['reporters', 'journalists', 'key_personnel',
                         'editorial_leadership_and_key_personnel']:
        section = nyt_profile.get(section_name, [])
        if isinstance(section, list):
            for entry in section:
                if isinstance(entry, dict) and entry.get('name') == 'Ryan Mac':
                    return entry
    # Fallback: search all lists recursively
    return _find_mac_recursive(nyt_profile)


def _find_mac_recursive(data):
    if isinstance(data, dict):
        for v in data.values():
            result = _find_mac_recursive(v)
            if result:
                return result
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and item.get('name') == 'Ryan Mac':
                return item
            result = _find_mac_recursive(item)
            if result:
                return result
    return None


def get_mac_cross_entity(mac_section):
    """Extract cross_entity_coverage_analysis from Mac's section."""
    return mac_section.get('cross_entity_coverage_analysis', {})


# === CLASS 1: Career and Hiring Mandate ===

class TestRyanMacCareerContext:
    """Verify career trajectory and hiring mandate documentation."""

    def test_mac_exists_in_nyt_profile(self):
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        assert mac is not None, "Ryan Mac must have a section in nytimes.yaml"

    def test_beat_includes_accountability(self):
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        beat = mac.get('beat', '')
        assert 'accountability' in beat.lower(), \
            "Mac's beat must reference 'accountability' — that's his hiring mandate"

    def test_beat_documents_actual_vs_official_scope(self):
        """The beat field should document BOTH the official mandate and actual scope."""
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        beat = mac.get('beat', '')
        # Should reference both the official and actual scope
        assert 'meta' in beat.lower() or 'musk' in beat.lower(), \
            "Beat field should document actual targets (Meta, Musk), not just official mandate"

    def test_hiring_context_exists(self):
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        assert 'hiring_context' in mac, "Must document hiring context"

    def test_hiring_memo_scope_documented(self):
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ctx = mac.get('hiring_context', {})
        stated = ctx.get('stated_scope', '')
        assert 'all' in stated.lower() or 'tech companies' in stated.lower(), \
            "Hiring memo's stated scope must be documented — it says 'all manner of tech companies'"

    def test_scope_gap_analysis_exists(self):
        """The gap between hiring mandate and actual coverage must be documented."""
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ctx = mac.get('hiring_context', {})
        gap = ctx.get('scope_gap_analysis', '')
        assert len(gap) > 50, "Scope gap analysis must exist with substantive content"

    def test_known_patterns_references_polk_award(self):
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        patterns = mac.get('known_patterns', '')
        assert 'polk' in patterns.lower(), \
            "Known patterns must reference Polk Award for Facebook coverage"

    def test_known_patterns_references_character_limit(self):
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        patterns = mac.get('known_patterns', '')
        assert 'character limit' in patterns.lower(), \
            "Known patterns must reference 'Character Limit' book"


# === CLASS 2: Meta Coverage Analysis ===

class TestRyanMacMetaCoverage:
    """Verify Meta coverage documentation — Mac's primary beat target."""

    def test_meta_coverage_tone_adversarial(self):
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        meta = ce.get('meta_coverage', {})
        assert meta.get('tone') == 'adversarial_investigative', \
            "Meta coverage tone should be adversarial_investigative"

    def test_meta_career_investment_documented(self):
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        meta = ce.get('meta_coverage', {})
        investment = meta.get('career_investment', '')
        assert 'polk award' in investment.lower(), \
            "Career investment must reference Polk Award as evidence of depth"

    def test_smart_glasses_early_coverage(self):
        """Mac covered Meta glasses at BuzzFeed — facial recognition alarm framing."""
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        meta = ce.get('meta_coverage', {})
        glasses = meta.get('smart_glasses_early_coverage', {})
        assert 'bosworth' in glasses.get('title', '').lower() or \
               'facial recognition' in glasses.get('title', '').lower(), \
            "Smart glasses coverage must document the BuzzFeed facial recognition article"

    def test_smart_glasses_no_equivalent_for_competitors(self):
        """Mac covered Meta glasses as privacy alarm — did NOT cover Google/Snap glasses equivalently."""
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        meta = ce.get('meta_coverage', {})
        glasses = meta.get('smart_glasses_early_coverage', {})
        sig = glasses.get('significance', '')
        assert 'google' in sig.lower() or 'snap' in sig.lower(), \
            "Significance must note absence of equivalent coverage for Google/Snap glasses"

    def test_addiction_trial_documented(self):
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        meta = ce.get('meta_coverage', {})
        trial = meta.get('social_media_addiction_trial', {})
        articles = trial.get('articles', [])
        assert len(articles) >= 1, "Addiction trial coverage must be documented"


# === CLASS 3: Musk Coverage and Book-Deal Incentives ===

class TestRyanMacMuskCoverage:
    """Verify Musk/X/SpaceX coverage documentation and book-deal dynamics."""

    def test_musk_coverage_tone_adversarial(self):
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        musk = ce.get('musk_coverage', {})
        assert musk.get('tone') == 'adversarial_investigative', \
            "Musk coverage tone should be adversarial_investigative"

    def test_book_deal_documented(self):
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        musk = ce.get('musk_coverage', {})
        book = musk.get('book_deal', {})
        assert book.get('title') == 'Character Limit: How Elon Musk Destroyed Twitter', \
            "Book deal must reference 'Character Limit'"

    def test_book_co_author_conger(self):
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        musk = ce.get('musk_coverage', {})
        book = musk.get('book_deal', {})
        assert 'conger' in book.get('co_author', '').lower(), \
            "Kate Conger must be documented as co-author"

    def test_book_financial_incentive_noted(self):
        """Book deals create financial lock-in for continued coverage of the subject."""
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        musk = ce.get('musk_coverage', {})
        book = musk.get('book_deal', {})
        note = book.get('financial_note', '')
        assert 'financial' in note.lower() or 'incentive' in note.lower(), \
            "Book deal's financial incentive must be documented"

    def test_frenkel_parallel_noted(self):
        """Mac-Musk book deal parallels Frenkel-Meta book deal."""
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        musk = ce.get('musk_coverage', {})
        book = musk.get('book_deal', {})
        note = book.get('financial_note', '')
        assert 'frenkel' in note.lower() or 'ugly truth' in note.lower(), \
            "Must note parallel to Frenkel's 'An Ugly Truth' book-deal dynamic"

    def test_personal_adversarial_dynamic_documented(self):
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        musk = ce.get('musk_coverage', {})
        personal = musk.get('personal_adversarial_dynamic', {})
        assert 'twitter_suspension' in personal or 'suspension' in str(personal).lower(), \
            "Twitter suspension must be documented"

    def test_maye_musk_racial_attack(self):
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        musk = ce.get('musk_coverage', {})
        personal = musk.get('personal_adversarial_dynamic', {})
        attack = personal.get('maye_musk_racial_attack', '')
        assert 'vietnamese' in attack.lower() or 'racial' in str(personal).lower(), \
            "Maye Musk racial targeting must be documented"

    def test_recent_spacex_articles(self):
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        musk = ce.get('musk_coverage', {})
        articles = musk.get('recent_articles', [])
        assert len(articles) >= 2, "Must document at least 2 recent SpaceX/Musk articles"

    def test_spacex_mars_article_framing(self):
        """SpaceX Mars de-emphasis article: adversarial framing."""
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        musk = ce.get('musk_coverage', {})
        articles = musk.get('recent_articles', [])
        mars_articles = [a for a in articles if 'mars' in a.get('title', '').lower()
                         or 'de-emphasis' in a.get('title', '').lower()
                         or 'de-emphasiz' in a.get('title', '').lower()]
        assert len(mars_articles) >= 1, \
            "Must document SpaceX Mars de-emphasis article"


# === CLASS 4: OpenAI Coverage — Institutional vs Investigative ===

class TestRyanMacOpenAICoverage:
    """Verify that Mac's sole OpenAI article is correctly categorized as institutional."""

    def test_openai_tone_institutional(self):
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        openai = ce.get('openai_coverage', {})
        assert openai.get('tone') == 'institutional_advocacy', \
            "OpenAI coverage tone must be 'institutional_advocacy' — not independent investigative"

    def test_sole_article_is_nyt_lawsuit(self):
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        openai = ce.get('openai_coverage', {})
        article = openai.get('sole_article', {})
        title = article.get('title', '')
        assert 'sues' in title.lower() or 'lawsuit' in title.lower() or 'copyrighted' in title.lower(), \
            "Sole OpenAI article must be the NYT v OpenAI lawsuit announcement"

    def test_co_byline_grynbaum_not_tech_reporter(self):
        """Co-byline with media reporter Grynbaum confirms institutional intent."""
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        openai = ce.get('openai_coverage', {})
        article = openai.get('sole_article', {})
        co = article.get('co_byline', '')
        assert 'grynbaum' in co.lower(), \
            "Co-byline must document Grynbaum — a MEDIA reporter, not tech accountability"

    def test_openai_mtd_citation_documented(self):
        """OpenAI's motion to dismiss cited Mac's article as NYT self-publicity."""
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        openai = ce.get('openai_coverage', {})
        article = openai.get('sole_article', {})
        sig = article.get('significance', '')
        assert 'motion to dismiss' in sig.lower() or 'publicized' in sig.lower(), \
            "Must document that OpenAI's MTD cited this as institutional self-publicity"

    def test_no_independent_openai_investigation(self):
        """Mac has NOT written independent investigative articles about OpenAI."""
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        openai = ce.get('openai_coverage', {})
        sig = openai.get('sole_article', {}).get('significance', '')
        assert 'no evidence' in sig.lower() or 'control test' in sig.lower(), \
            "Must note absence of independent OpenAI investigative coverage"


# === CLASS 5: Coverage Gaps — Google, Apple, Amazon, Anthropic ===

class TestRyanMacCoverageGaps:
    """Verify documentation of zero-coverage for major tech companies."""

    @pytest.mark.parametrize("company", [
        "google_coverage",
        "apple_coverage",
        "amazon_coverage",
        "anthropic_coverage",
    ])
    def test_absent_coverage_documented(self, company):
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        section = ce.get(company, {})
        assert section.get('tone') == 'absent', \
            f"{company} tone must be 'absent' — Mac has no investigative coverage"

    @pytest.mark.parametrize("company", [
        "google_coverage",
        "apple_coverage",
        "amazon_coverage",
        "anthropic_coverage",
    ])
    def test_zero_articles_documented(self, company):
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        section = ce.get(company, {})
        assert section.get('articles_found', -1) == 0, \
            f"{company} must document 0 articles found"

    def test_google_gap_notes_antitrust_verdict(self):
        """Google antitrust verdict (Aug 2024) — no Mac coverage despite being 'tech accountability.'"""
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        google = ce.get('google_coverage', {})
        note = google.get('note', '')
        assert 'antitrust' in note.lower(), \
            "Google coverage gap must note the antitrust verdict — a major accountability story Mac missed"

    def test_google_gap_notes_buzzfeed_claim(self):
        """Mac's BuzzFeed bio said 'Facebook, Google, Tesla' — Google coverage vanished at NYT."""
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        google = ce.get('google_coverage', {})
        note = google.get('note', '')
        assert 'buzzfeed' in note.lower() or 'all manner' in note.lower(), \
            "Must note gap between claimed scope and actual coverage"


# === CLASS 6: Beat Capture Structural Analysis ===

class TestBeatCaptureAnalysis:
    """Verify the structural analysis of beat capture dynamics."""

    def test_summary_exists(self):
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        summary = ce.get('summary', '')
        assert len(summary) > 100, "Summary must exist with substantive analysis"

    def test_summary_uses_beat_capture_term(self):
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        summary = ce.get('summary', '')
        assert 'beat capture' in summary.lower(), \
            "Summary must use the term 'beat capture' — this is the key analytical frame"

    def test_three_structural_mechanisms(self):
        """Three mechanisms drive beat capture: sourcing, book-deal, institutional."""
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        summary = ce.get('summary', '')
        assert 'sourcing' in summary.lower(), "Must identify sourcing lock-in mechanism"
        assert 'book' in summary.lower(), "Must identify book-deal financial incentive"
        assert 'institutional' in summary.lower() or 'assignment' in summary.lower(), \
            "Must identify institutional assignment mechanism"

    def test_cross_entity_significance_quantitative(self):
        """Significance section must include quantitative coverage gap."""
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        sig = ce.get('cross_entity_significance', '')
        # Should count articles per entity
        assert 'google: 0' in sig.lower() or 'apple: 0' in sig.lower(), \
            "Must quantify coverage gap with article counts"

    def test_significance_notes_financial_relationship_correlation(self):
        """Coverage tracks AWAY from companies with NYT financial relationships."""
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        sig = ce.get('cross_entity_significance', '')
        assert 'financial relationship' in sig.lower() or \
               'no financial relationship' in sig.lower() or \
               'advertiser' in sig.lower() or \
               'litigation' in sig.lower(), \
            "Must note correlation between coverage and financial relationships"

    def test_not_individual_bias_claim(self):
        """Analysis must distinguish structural/institutional from individual bias."""
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        summary = ce.get('summary', '')
        assert 'not a criticism' in summary.lower() or \
               'individual' in summary.lower() or \
               'structural' in summary.lower(), \
            "Must clarify this is structural/institutional analysis, not individual bias claim"


# === CLASS 7: Cross-Validation Against Other NYT Journalists ===

class TestCrossValidationWithNYTDesk:
    """Verify consistency with other NYT journalist profiles."""

    def test_mac_parallels_frenkel_book_dynamic(self):
        """Mac's Character Limit for Musk should parallel Frenkel's An Ugly Truth for Meta."""
        profile = load_nyt_profile()
        mac = get_mac_section(profile)
        ce = get_mac_cross_entity(mac)
        # Check if Frenkel parallel is documented in book-deal section
        musk = ce.get('musk_coverage', {})
        book = musk.get('book_deal', {})
        note = book.get('financial_note', '')
        assert 'frenkel' in note.lower(), \
            "Must explicitly parallel with Frenkel's book-deal dynamic"

    def test_eli_tan_succession_context(self):
        """Mac's beat capture is part of the broader NYT Meta beat structure
        (Isaac → Tan succession, Frenkel adversarial lane)."""
        profile = load_nyt_profile()
        # Verify Eli Tan exists as Mac's institutional context
        tan = _find_mac_recursive(profile)  # reuse helper
        # Actually just check that Eli Tan exists in profile
        found_tan = False
        for section_name in ['reporters', 'journalists', 'key_personnel',
                             'editorial_leadership_and_key_personnel']:
            section = profile.get(section_name, [])
            if isinstance(section, list):
                for entry in section:
                    if isinstance(entry, dict) and entry.get('name') == 'Eli Tan':
                        found_tan = True
        if not found_tan:
            found_tan = _find_by_name(profile, 'Eli Tan') is not None
        assert found_tan, "Eli Tan must exist in profile — Mac's beat capture is part of NYT Meta beat structure"

    def test_kate_conger_linked(self):
        """Mac and Conger are co-authors — must both exist in profile."""
        profile = load_nyt_profile()
        conger = _find_by_name(profile, 'Kate Conger')
        assert conger is not None, "Kate Conger must exist — co-author of 'Character Limit'"

    def test_conger_patterns_reference_character_limit(self):
        """Kate Conger's profile should reference 'Character Limit' too."""
        profile = load_nyt_profile()
        conger = _find_by_name(profile, 'Kate Conger')
        if conger:
            patterns = conger.get('known_patterns', '')
            assert 'character limit' in patterns.lower(), \
                "Conger's known_patterns should reference their shared book"


def _find_by_name(data, name):
    """Recursively find a journalist entry by name."""
    if isinstance(data, dict):
        for v in data.values():
            result = _find_by_name(v, name)
            if result:
                return result
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and item.get('name') == name:
                return item
            result = _find_by_name(item, name)
            if result:
                return result
    return None
