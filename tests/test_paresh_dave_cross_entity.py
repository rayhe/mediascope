"""
Test cross-entity coverage analysis for Paresh Dave (WIRED).

Mechanism #8: Emotional Register Asymmetry — the same reporter applies maximally
dramatic language to Meta coverage and measured/analytical language to OpenAI
and Google coverage of comparable internal dysfunction.

Key finding: Dave's Meta coverage uses "gulag," "soul-crushing," "piece of shit,"
profanity-in-headlines. His OpenAI coverage uses "quietly scrapped," "confidentially files."
His Google coverage uses "paid off," "innovation by rivals is key." Same reporter,
same publication, systematically different emotional registers by target company.
"""
import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def get_wired_profile():
    with open(os.path.join(PROFILES_DIR, 'wired.yaml')) as f:
        return yaml.safe_load(f)


def get_paresh_dave_entry(profile):
    """Find Paresh Dave in key_journalists."""
    for j in profile.get('key_journalists', []):
        if j.get('name') == 'Paresh Dave':
            return j
    return None


def get_cross_entity(entry):
    """Get cross_entity_coverage_analysis from Dave's entry."""
    return entry.get('cross_entity_coverage_analysis', {})


class TestPareshDaveBasicProfile:
    """Verify Paresh Dave's basic profile is complete."""

    def test_paresh_dave_exists(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        assert entry is not None, "Paresh Dave must exist in key_journalists"

    def test_has_beat(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        assert 'AI' in entry.get('beat', ''), "Beat should include AI"
        assert 'Big Tech' in entry.get('beat', ''), "Beat should include Big Tech"

    def test_has_career_trajectory(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        trajectory = entry.get('career_trajectory', [])
        assert len(trajectory) >= 3, "Should have at least 3 career stops"

    def test_career_includes_reuters(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        pubs = [t.get('publication', '') for t in entry.get('career_trajectory', [])]
        assert 'Reuters' in pubs, "Career should include Reuters"

    def test_career_includes_wired(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        pubs = [t.get('publication', '') for t in entry.get('career_trajectory', [])]
        assert 'WIRED' in pubs, "Career should include WIRED"

    def test_career_includes_la_times(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        pubs = [t.get('publication', '') for t in entry.get('career_trajectory', [])]
        assert 'Los Angeles Times' in pubs, "Career should include LA Times"


class TestCrossEntityMechanismMetadata:
    """Verify mechanism metadata is complete and correctly numbered."""

    def test_has_cross_entity_analysis(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        assert analysis, "Must have cross_entity_coverage_analysis"

    def test_mechanism_name(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        assert analysis.get('mechanism_name') == 'emotional_register_asymmetry'

    def test_mechanism_number(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        assert analysis.get('mechanism_number') == 8

    def test_date_analyzed(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        assert analysis.get('date_analyzed') == '2026-08-08'

    def test_has_summary(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        summary = analysis.get('summary', '')
        assert len(summary) > 100, "Summary should be substantive"
        assert 'emotional register' in summary.lower(), "Summary should mention emotional register"


class TestMetaCoverage:
    """Verify Meta coverage analysis is complete and correctly characterized."""

    def test_meta_coverage_exists(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        meta = analysis.get('meta_coverage', {})
        assert meta, "Must have meta_coverage section"

    def test_meta_aggregate_tone_dramatic(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        meta = analysis.get('meta_coverage', {})
        tone = meta.get('aggregate_tone', '')
        assert 'dramatic' in tone.lower(), "Meta tone should be characterized as dramatic"

    def test_meta_emotional_register_extreme(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        meta = analysis.get('meta_coverage', {})
        assert meta.get('emotional_register') == 'extreme'

    def test_meta_has_articles(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        meta = analysis.get('meta_coverage', {})
        articles = meta.get('articles', [])
        assert len(articles) >= 5, "Should have at least 5 Meta articles analyzed"

    def test_meta_article_count_matches(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        meta = analysis.get('meta_coverage', {})
        assert meta.get('article_count') == len(meta.get('articles', []))

    def test_meta_headlines_include_profanity(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        meta = analysis.get('meta_coverage', {})
        headlines = meta.get('headline_language_samples', [])
        headline_text = ' '.join(headlines).lower()
        assert 'piece of shit' in headline_text or 'total mess' in headline_text, \
            "Meta headlines should include profanity/extreme language"

    def test_meta_gulag_language_documented(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        meta = analysis.get('meta_coverage', {})
        articles = meta.get('articles', [])
        all_emotional = []
        for a in articles:
            all_emotional.extend(a.get('emotional_language', []))
        assert 'gulag' in all_emotional, "Meta coverage should document 'gulag' language"

    def test_meta_soul_crushing_documented(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        meta = analysis.get('meta_coverage', {})
        articles = meta.get('articles', [])
        all_emotional = []
        for a in articles:
            all_emotional.extend(a.get('emotional_language', []))
        assert 'soul-crushing' in all_emotional

    def test_meta_all_tone_scores_negative(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        meta = analysis.get('meta_coverage', {})
        articles = meta.get('articles', [])
        for a in articles:
            if 'tone_score' in a:
                assert a['tone_score'] <= 0, \
                    f"Meta article '{a.get('title', '')}' should have negative or zero tone"


class TestOpenAICoverage:
    """Verify OpenAI coverage analysis is complete and correctly characterized."""

    def test_openai_coverage_exists(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        openai = analysis.get('openai_coverage', {})
        assert openai, "Must have openai_coverage section"

    def test_openai_aggregate_tone_measured(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        openai = analysis.get('openai_coverage', {})
        tone = openai.get('aggregate_tone', '')
        assert 'measured' in tone.lower(), "OpenAI tone should be characterized as measured"

    def test_openai_emotional_register_controlled(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        openai = analysis.get('openai_coverage', {})
        assert openai.get('emotional_register') == 'controlled'

    def test_openai_has_articles(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        openai = analysis.get('openai_coverage', {})
        articles = openai.get('articles', [])
        assert len(articles) >= 4, "Should have at least 4 OpenAI articles analyzed"

    def test_openai_no_extreme_language(self):
        """OpenAI coverage should NOT contain gulag/profanity-level language."""
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        openai = analysis.get('openai_coverage', {})
        articles = openai.get('articles', [])
        extreme_words = {'gulag', 'soul-crushing', 'piece of shit', 'total mess'}
        for a in articles:
            emotional = set(a.get('emotional_language', []))
            overlap = emotional & extreme_words
            assert not overlap, \
                f"OpenAI article should not have extreme language: {overlap}"

    def test_openai_headlines_use_measured_language(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        openai = analysis.get('openai_coverage', {})
        headlines = openai.get('headline_language_samples', [])
        headline_text = ' '.join(headlines).lower()
        # Should use measured words
        measured_indicators = ['quietly', 'confidentially', 'may be rivals']
        found = any(m in headline_text for m in measured_indicators)
        assert found, "OpenAI headlines should use measured language"

    def test_openai_has_positive_tone_articles(self):
        """OpenAI coverage includes neutral-to-positive articles unlike Meta."""
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        openai = analysis.get('openai_coverage', {})
        articles = openai.get('articles', [])
        positive = [a for a in articles if a.get('tone_score', -1) >= 0]
        assert len(positive) >= 1, "Should have at least one non-negative OpenAI article"


class TestGoogleCoverage:
    """Verify Google coverage analysis is complete and correctly characterized."""

    def test_google_coverage_exists(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        google = analysis.get('google_coverage', {})
        assert google, "Must have google_coverage section"

    def test_google_emotional_register_neutral(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        google = analysis.get('google_coverage', {})
        register = google.get('emotional_register', '')
        assert 'neutral' in register.lower(), "Google register should include 'neutral'"

    def test_google_has_positive_headline(self):
        """Google coverage includes a positive headline — no Meta equivalent exists."""
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        google = analysis.get('google_coverage', {})
        headlines = google.get('headline_language_samples', [])
        headline_text = ' '.join(headlines).lower()
        assert 'paid off' in headline_text, \
            "Google should have 'paid off' positive framing in headlines"

    def test_google_has_articles(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        google = analysis.get('google_coverage', {})
        articles = google.get('articles', [])
        assert len(articles) >= 4, "Should have at least 4 Google articles analyzed"

    def test_google_has_positive_tone_articles(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        google = analysis.get('google_coverage', {})
        articles = google.get('articles', [])
        positive = [a for a in articles if a.get('tone_score', -1) > 0]
        assert len(positive) >= 1, "Should have at least one positive-tone Google article"


class TestAsymmetryScores:
    """Verify the cross-entity asymmetry metrics."""

    def test_asymmetry_section_exists(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        asym = analysis.get('cross_entity_asymmetry', {})
        assert asym, "Must have cross_entity_asymmetry section"

    def test_meta_tone_most_negative(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        asym = analysis.get('cross_entity_asymmetry', {})
        meta = asym.get('meta_avg_tone', 0)
        openai = asym.get('openai_avg_tone', 0)
        google = asym.get('google_avg_tone', 0)
        assert meta < openai, "Meta avg tone must be more negative than OpenAI"
        assert meta < google, "Meta avg tone must be more negative than Google"

    def test_google_tone_most_positive(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        asym = analysis.get('cross_entity_asymmetry', {})
        google = asym.get('google_avg_tone', 0)
        openai = asym.get('openai_avg_tone', 0)
        assert google > openai, "Google avg tone should be more positive than OpenAI"

    def test_meta_openai_delta_significant(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        asym = analysis.get('cross_entity_asymmetry', {})
        delta = asym.get('delta_meta_vs_openai', 0)
        assert delta >= 0.3, f"Meta-OpenAI delta {delta} should be >= 0.3"

    def test_meta_google_delta_significant(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        asym = analysis.get('cross_entity_asymmetry', {})
        delta = asym.get('delta_meta_vs_google', 0)
        assert delta >= 0.4, f"Meta-Google delta {delta} should be >= 0.4"

    def test_overall_asymmetry_score_high(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        asym = analysis.get('cross_entity_asymmetry', {})
        score = asym.get('overall_asymmetry_score', 0)
        assert score >= 0.6, f"Overall asymmetry {score} should be >= 0.6 (significant)"


class TestFivePatterns:
    """Verify the five documented patterns."""

    def test_has_five_patterns(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        patterns = analysis.get('five_patterns', [])
        assert len(patterns) == 5, f"Should have exactly 5 patterns, got {len(patterns)}"

    def test_source_pipeline_escalation_pattern(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        patterns = analysis.get('five_patterns', [])
        names = [p.get('pattern_name', '') for p in patterns]
        assert 'SOURCE PIPELINE ESCALATION' in names

    def test_headline_profanity_pattern(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        patterns = analysis.get('five_patterns', [])
        names = [p.get('pattern_name', '') for p in patterns]
        assert 'HEADLINE PROFANITY ASYMMETRY' in names

    def test_multi_byline_pattern(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        patterns = analysis.get('five_patterns', [])
        names = [p.get('pattern_name', '') for p in patterns]
        assert 'MULTI-BYLINE ESCALATION ASYMMETRY' in names

    def test_positive_coverage_exclusion_pattern(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        patterns = analysis.get('five_patterns', [])
        names = [p.get('pattern_name', '') for p in patterns]
        assert 'POSITIVE COVERAGE EXCLUSION' in names

    def test_confession_framing_pattern(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        patterns = analysis.get('five_patterns', [])
        names = [p.get('pattern_name', '') for p in patterns]
        assert 'CONFESSION FRAMING vs ANALYTICAL FRAMING' in names

    def test_all_patterns_have_descriptions(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        patterns = analysis.get('five_patterns', [])
        for p in patterns:
            desc = p.get('description', '')
            assert len(desc) > 50, \
                f"Pattern '{p.get('pattern_name')}' description too short"


class TestNaturalExperimentSignificance:
    """Verify the natural experiment argument is documented."""

    def test_has_natural_experiment_note(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        note = analysis.get('natural_experiment_significance', '')
        assert len(note) > 100, "Natural experiment note should be substantive"

    def test_natural_experiment_mentions_reuters(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        note = analysis.get('natural_experiment_significance', '')
        assert 'Reuters' in note, "Should reference Reuters career for comparison"

    def test_natural_experiment_mentions_institution_driven(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        note = analysis.get('natural_experiment_significance', '')
        assert 'INSTITUTION' in note.upper(), "Should conclude institution-driven"

    def test_has_editorial_responsibility_note(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        note = analysis.get('editorial_responsibility_note', '')
        assert len(note) > 50, "Should have editorial responsibility note"

    def test_editorial_note_mentions_editors(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        note = analysis.get('editorial_responsibility_note', '')
        assert 'Drummond' in note or 'Barrett' in note, \
            "Should mention WIRED editors who co-own headline choices"


class TestTestFileReference:
    """Verify test file cross-reference."""

    def test_has_test_file_reference(self):
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        test_file = analysis.get('test_file', '')
        assert 'test_paresh_dave_cross_entity.py' in test_file

    def test_test_file_is_this_file(self):
        """Meta-test: this test file should be the one referenced."""
        profile = get_wired_profile()
        entry = get_paresh_dave_entry(profile)
        analysis = get_cross_entity(entry)
        test_file = analysis.get('test_file', '')
        assert test_file == 'tests/test_paresh_dave_cross_entity.py'
