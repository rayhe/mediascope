"""
Test Kashmir Hill cross-entity coverage analysis.

Kashmir Hill is the NYT's premier privacy/surveillance reporter (Clearview AI
investigation, "Your Face Belongs to Us" book). This suite validates the finding
that her investigative energy concentrates on Meta's smart glasses while
functionally identical or worse privacy practices at Google (Android XR),
Amazon (Ring Familiar Faces), Apple (AirTag/Vision Pro), and OpenAI (data
scraping) receive no comparable Hill investigation.

The asymmetry is a BEAT ASSIGNMENT EFFECT amplified by NYT's financial
relationships, not a personal bias issue.

Created: 2026-08-06 22:00 PT (Type B iteration — Journalist Cross-Entity Tracking)
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_nytimes_profile():
    with open(os.path.join(PROFILES_DIR, 'nytimes.yaml'), 'r') as f:
        return yaml.safe_load(f)


def load_competitor_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml'), 'r') as f:
        return yaml.safe_load(f)


def load_journalists():
    with open(os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml'), 'r') as f:
        data = yaml.safe_load(f)
        return data.get('journalists', data if isinstance(data, list) else [])


def find_hill_in_nytimes(profile):
    """Find Kashmir Hill's entry in the NYT profile key_journalists list."""
    journalists = profile.get('key_journalists', [])
    for j in journalists:
        if isinstance(j, dict) and j.get('name') == 'Kashmir Hill':
            return j
    return None


def find_hill_in_journalists(journalists):
    """Find Kashmir Hill in the careers/journalists.yaml."""
    for entry in journalists:
        if isinstance(entry, dict) and entry.get('name') == 'Kashmir Hill':
            return entry
    return None


def find_journalist_in_nytimes(profile, name):
    """Find any journalist by name in the NYT profile."""
    journalists = profile.get('key_journalists', [])
    for j in journalists:
        if isinstance(j, dict) and j.get('name') == name:
            return j
    return None


# ===================================================================
# 1. PROFILE EXISTENCE AND STRUCTURE
# ===================================================================

class TestKashmirHillProfileExists:
    """Verify Kashmir Hill has a cross-entity analysis in NYT profile."""

    def test_hill_in_nytimes_profile(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        assert hill is not None, "Kashmir Hill should be in NYT profile journalists list"

    def test_hill_has_cross_entity_analysis(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        assert hill is not None
        assert 'cross_entity_coverage_analysis' in hill, \
            "Kashmir Hill should have cross_entity_coverage_analysis"

    def test_hill_beat_is_privacy(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        assert hill is not None
        beat = hill.get('beat', '').lower()
        assert 'privacy' in beat, "Hill's beat should include 'privacy'"
        assert 'facial recognition' in beat or 'surveillance' in beat, \
            "Hill's beat should include facial recognition or surveillance"

    def test_hill_in_careers_journalists(self):
        journalists = load_journalists()
        hill = find_hill_in_journalists(journalists)
        assert hill is not None, "Kashmir Hill should be in careers/journalists.yaml"

    def test_hill_clearview_documented(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        assert hill is not None
        patterns = hill.get('known_patterns', '')
        assert 'clearview' in patterns.lower(), "Hill's Clearview AI work should be documented"


# ===================================================================
# 2. META COVERAGE — ADVERSARIAL INVESTIGATION
# ===================================================================

class TestHillMetaCoverage:
    """Verify Hill's Meta coverage is documented as adversarial/investigative."""

    def test_meta_coverage_exists(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        assert hill is not None
        analysis = hill.get('cross_entity_coverage_analysis', {})
        assert 'meta_coverage' in analysis, "Meta coverage section should exist"

    def test_meta_tone_adversarial(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        meta = analysis.get('meta_coverage', {})
        tone = meta.get('tone', '')
        assert 'adversarial' in tone.lower(), \
            f"Meta tone should be adversarial, got: {tone}"

    def test_meta_has_name_tag_article(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        meta = analysis.get('meta_coverage', {})
        articles = meta.get('recent_articles', [])
        has_name_tag = any('name tag' in str(a).lower() or 'facial recognition' in str(a).lower()
                          for a in articles)
        assert has_name_tag, "Meta coverage should include Name Tag/facial recognition article"

    def test_meta_article_has_source(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        meta = analysis.get('meta_coverage', {})
        articles = meta.get('recent_articles', [])
        assert len(articles) > 0, "Should have at least one meta article"
        for article in articles:
            if isinstance(article, dict):
                assert 'source_url' in article, f"Article should have source_url: {article}"

    def test_meta_framing_pattern_documented(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        meta = analysis.get('meta_coverage', {})
        framing = meta.get('framing_pattern', '')
        assert len(framing) > 50, "Framing pattern should be substantive"
        assert 'clearview' in framing.lower() or 'surveillance' in framing.lower(), \
            "Framing pattern should reference surveillance narrative framework"


# ===================================================================
# 3. GOOGLE COVERAGE ABSENCE
# ===================================================================

class TestHillGoogleAbsence:
    """Verify Hill's absence from Google Android XR privacy coverage."""

    def test_google_coverage_section_exists(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        assert 'google_coverage' in analysis, "Google coverage section should exist"

    def test_google_tone_absent(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        google = analysis.get('google_coverage', {})
        tone = google.get('tone', '')
        assert 'absent' in tone.lower(), \
            f"Google tone should indicate absence, got: {tone}"

    def test_google_android_xr_parallel(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        google = analysis.get('google_coverage', {})
        google_analysis = google.get('analysis', '')
        assert 'android xr' in google_analysis.lower(), \
            "Analysis should mention Google Android XR as parallel"

    def test_google_historical_context(self):
        """Hill's own book documents Google choosing not to deploy facial recognition in 2017."""
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        google = analysis.get('google_coverage', {})
        google_analysis = google.get('analysis', '')
        assert '2017' in google_analysis or 'book' in google_analysis.lower(), \
            "Should reference Hill's book documenting Google's 2017 facial recognition decision"


# ===================================================================
# 4. AMAZON COVERAGE ABSENCE — THE STRONGEST CASE
# ===================================================================

class TestHillAmazonAbsence:
    """Verify Hill's absence from Ring facial recognition coverage.

    This is the strongest asymmetry because Ring's Familiar Faces is
    DEPLOYED consumer-facing facial recognition (worse than Meta's
    unreleased Name Tag code) AND Amazon pays NYT $20-25M/yr."""

    def test_amazon_coverage_section_exists(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        assert 'amazon_coverage' in analysis, "Amazon coverage section should exist"

    def test_amazon_tone_absent(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        amazon = analysis.get('amazon_coverage', {})
        tone = amazon.get('tone', '')
        assert 'absent' in tone.lower(), \
            f"Amazon tone should indicate absence, got: {tone}"

    def test_amazon_ring_parallel_documented(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        amazon = analysis.get('amazon_coverage', {})
        amazon_analysis = amazon.get('analysis', '')
        assert 'ring' in amazon_analysis.lower() or 'familiar faces' in amazon_analysis.lower(), \
            "Analysis should mention Ring and Familiar Faces"

    def test_amazon_ftc_settlement_documented(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        amazon = analysis.get('amazon_coverage', {})
        amazon_analysis = amazon.get('analysis', '')
        assert 'ftc' in amazon_analysis.lower() or 'settlement' in amazon_analysis.lower(), \
            "Analysis should mention FTC settlement"

    def test_amazon_financial_context_documented(self):
        """The $20-25M/yr NYT-Amazon deal is the financial context."""
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        amazon = analysis.get('amazon_coverage', {})
        # Check for financial context in analysis or dedicated field
        amazon_text = str(amazon)
        assert '20' in amazon_text or 'licensing' in amazon_text.lower(), \
            "Amazon section should reference the financial relationship"

    def test_amazon_has_source_urls(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        amazon = analysis.get('amazon_coverage', {})
        source_urls = amazon.get('source_urls', [])
        assert len(source_urls) >= 2, \
            f"Amazon section should have at least 2 source URLs, got {len(source_urls)}"

    def test_amazon_ring_worse_than_meta(self):
        """Ring's facial recognition is DEPLOYED; Meta's Name Tag is unreleased code."""
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        amazon = analysis.get('amazon_coverage', {})
        amazon_analysis = amazon.get('analysis', '')
        assert ('deployed' in amazon_analysis.lower() or
                'live' in amazon_analysis.lower() or
                'in use' in amazon_analysis.lower()), \
            "Analysis should note Ring's facial recognition is deployed/live"


# ===================================================================
# 5. APPLE AND OPENAI COVERAGE ABSENCES
# ===================================================================

class TestHillAppleOpenAIAbsence:
    """Verify coverage gaps for Apple and OpenAI are documented."""

    def test_apple_coverage_section_exists(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        assert 'apple_coverage' in analysis, "Apple coverage section should exist"

    def test_apple_tone_absent(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        apple = analysis.get('apple_coverage', {})
        tone = apple.get('tone', '')
        assert 'absent' in tone.lower(), \
            f"Apple tone should indicate absence, got: {tone}"

    def test_openai_coverage_section_exists(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        assert 'openai_coverage' in analysis, "OpenAI coverage section should exist"

    def test_openai_clearview_parallel_documented(self):
        """OpenAI's data scraping is directly parallel to Clearview AI's scraping."""
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        openai = analysis.get('openai_coverage', {})
        openai_analysis = openai.get('analysis', '')
        assert 'clearview' in openai_analysis.lower() or 'scrap' in openai_analysis.lower(), \
            "OpenAI analysis should reference Clearview AI parallel or scraping"


# ===================================================================
# 6. ASYMMETRY SCORES
# ===================================================================

class TestHillAsymmetryScores:
    """Verify cross-entity asymmetry scores are present and reasonable."""

    def test_asymmetry_scores_exist(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        assert 'cross_entity_asymmetry_score' in analysis, \
            "Asymmetry scores section should exist"

    def test_all_four_scores_present(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        scores = analysis.get('cross_entity_asymmetry_score', {})
        for key in ['meta_vs_google', 'meta_vs_amazon', 'meta_vs_apple', 'meta_vs_openai']:
            assert key in scores, f"Missing asymmetry score: {key}"

    def test_amazon_highest_asymmetry(self):
        """Amazon should have the highest asymmetry — worst privacy record + biggest deal."""
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        scores = analysis.get('cross_entity_asymmetry_score', {})
        amazon_score = scores.get('meta_vs_amazon', 0)
        assert amazon_score >= 0.85, \
            f"Amazon asymmetry should be >= 0.85 (worst privacy + biggest deal), got {amazon_score}"

    def test_all_scores_above_threshold(self):
        """All asymmetry scores should be substantial (> 0.7)."""
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        scores = analysis.get('cross_entity_asymmetry_score', {})
        for key, value in scores.items():
            if isinstance(value, (int, float)):
                assert value > 0.7, \
                    f"Asymmetry score {key} should be > 0.7, got {value}"

    def test_methodology_documented(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        scores = analysis.get('cross_entity_asymmetry_score', {})
        methodology = scores.get('methodology', '')
        assert len(methodology) > 50, "Methodology should be documented"


# ===================================================================
# 7. INSTITUTIONAL MECHANISM — BEAT ASSIGNMENT EFFECT
# ===================================================================

class TestHillInstitutionalMechanism:
    """Verify the institutional mechanism is documented (not personal bias)."""

    def test_institutional_mechanism_documented(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        assert 'institutional_mechanism' in analysis, \
            "Institutional mechanism section should exist"

    def test_beat_assignment_identified(self):
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        mechanism = analysis.get('institutional_mechanism', '')
        # "BEAT\nASSIGNMENT" in YAML block literal — check for both words
        mech_lower = mechanism.lower()
        assert ('beat' in mech_lower and 'assignment' in mech_lower), \
            "Mechanism should identify beat assignment as the cause"

    def test_karen_weise_referenced(self):
        """Karen Weise covers Amazon — the separation is the mechanism."""
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        mechanism = analysis.get('institutional_mechanism', '')
        assert 'weise' in mechanism.lower() or 'karen' in mechanism.lower(), \
            "Mechanism should reference Karen Weise as the Amazon reporter"

    def test_not_personal_bias_framing(self):
        """The finding should be framed as institutional, not personal."""
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        summary = analysis.get('summary', '')
        assert 'beat assignment' in summary.lower() or 'institutional' in summary.lower(), \
            "Summary should frame this as institutional/structural, not personal bias"

    def test_cade_metz_connection_documented(self):
        """Should connect to the Cade Metz beat-assignment finding."""
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        analysis = hill.get('cross_entity_coverage_analysis', {})
        # Check across all text fields for Metz reference
        mechanism = analysis.get('institutional_mechanism', '')
        summary = analysis.get('summary', '')
        all_text = (mechanism + summary).lower()
        assert 'metz' in all_text or 'reinforc' in all_text or 'beat' in all_text, \
            "Should reference the beat-assignment finding that connects to Metz"


# ===================================================================
# 8. COMPETITOR RESEARCH FILE CONSISTENCY
# ===================================================================

class TestHillInCompetitorResearch:
    """Verify Kashmir Hill analysis is also in competitor-coverage-research.yaml."""

    def test_hill_in_nytimes_research(self):
        research = load_competitor_research()
        nytimes = research.get('publications', {}).get('nytimes', {})
        assert 'kashmir_hill_cross_entity' in nytimes, \
            "Kashmir Hill cross-entity should be in competitor research nytimes section"

    def test_research_has_overview(self):
        research = load_competitor_research()
        nytimes = research.get('publications', {}).get('nytimes', {})
        hill = nytimes.get('kashmir_hill_cross_entity', {})
        overview = hill.get('overview', '')
        assert len(overview) > 100, "Research overview should be substantive"

    def test_research_has_meta_investigation(self):
        research = load_competitor_research()
        nytimes = research.get('publications', {}).get('nytimes', {})
        hill = nytimes.get('kashmir_hill_cross_entity', {})
        assert 'meta_investigation' in hill, "Should have meta_investigation section"

    def test_research_has_google_absence(self):
        research = load_competitor_research()
        nytimes = research.get('publications', {}).get('nytimes', {})
        hill = nytimes.get('kashmir_hill_cross_entity', {})
        assert 'google_absence' in hill, "Should have google_absence section"

    def test_research_has_amazon_absence(self):
        research = load_competitor_research()
        nytimes = research.get('publications', {}).get('nytimes', {})
        hill = nytimes.get('kashmir_hill_cross_entity', {})
        assert 'amazon_absence' in hill, "Should have amazon_absence section"

    def test_research_has_apple_absence(self):
        research = load_competitor_research()
        nytimes = research.get('publications', {}).get('nytimes', {})
        hill = nytimes.get('kashmir_hill_cross_entity', {})
        assert 'apple_absence' in hill, "Should have apple_absence section"

    def test_research_has_openai_absence(self):
        research = load_competitor_research()
        nytimes = research.get('publications', {}).get('nytimes', {})
        hill = nytimes.get('kashmir_hill_cross_entity', {})
        assert 'openai_absence' in hill, "Should have openai_absence section"

    def test_research_has_asymmetry_mechanism(self):
        research = load_competitor_research()
        nytimes = research.get('publications', {}).get('nytimes', {})
        hill = nytimes.get('kashmir_hill_cross_entity', {})
        assert 'asymmetry_mechanism' in hill, "Should have asymmetry_mechanism section"

    def test_research_meta_has_source_url(self):
        research = load_competitor_research()
        nytimes = research.get('publications', {}).get('nytimes', {})
        hill = nytimes.get('kashmir_hill_cross_entity', {})
        meta = hill.get('meta_investigation', {})
        assert 'source_url' in meta, "Meta investigation should have source_url"

    def test_research_amazon_has_source_urls(self):
        research = load_competitor_research()
        nytimes = research.get('publications', {}).get('nytimes', {})
        hill = nytimes.get('kashmir_hill_cross_entity', {})
        amazon = hill.get('amazon_absence', {})
        urls = amazon.get('source_urls', [])
        assert len(urls) >= 2, f"Amazon absence should have 2+ source URLs, got {len(urls)}"

    def test_research_amazon_financial_context(self):
        research = load_competitor_research()
        nytimes = research.get('publications', {}).get('nytimes', {})
        hill = nytimes.get('kashmir_hill_cross_entity', {})
        amazon = hill.get('amazon_absence', {})
        financial = amazon.get('financial_context', '')
        assert '20' in financial or 'licensing' in financial.lower(), \
            "Amazon absence should reference financial relationship"


# ===================================================================
# 9. CROSS-VALIDATION WITH EXISTING FINDINGS
# ===================================================================

class TestHillCrossValidation:
    """Validate consistency with existing NYT beat-assignment findings."""

    def test_consistent_with_metz_finding(self):
        """Hill finding should complement (not contradict) Cade Metz beat-assignment finding."""
        profile = load_nytimes_profile()
        hill = find_hill_in_nytimes(profile)
        hill_analysis = hill.get('cross_entity_coverage_analysis', {})

        # Both should identify beat assignment as the mechanism
        hill_mechanism = hill_analysis.get('institutional_mechanism', '')
        mech_lower = hill_mechanism.lower()
        assert 'beat' in mech_lower and 'assignment' in mech_lower, \
            "Hill mechanism should identify beat assignment"

        # Find Metz's analysis
        metz = find_journalist_in_nytimes(profile, 'Cade Metz')
        assert metz is not None, "Cade Metz should be in NYT profile"
        metz_analysis = metz.get('cross_entity_coverage_analysis', {})
        assert len(metz_analysis) > 0, "Metz should have cross-entity analysis"

    def test_nyt_amazon_deal_documented_in_publication(self):
        """The NYT-Amazon deal should be documented at the publication level."""
        research = load_competitor_research()
        nytimes = research.get('publications', {}).get('nytimes', {})
        amazon_tone = nytimes.get('amazon_coverage_tone', '')
        assert 'neutral' in amazon_tone.lower() or 'positive' in amazon_tone.lower(), \
            "NYT Amazon coverage tone should reflect the financial relationship"

    def test_karen_weise_conflict_note_exists(self):
        """Karen Weise's CONFLICT NOTE should be in the NYT profile."""
        profile = load_nytimes_profile()
        weise = find_journalist_in_nytimes(profile, 'Karen Weise')
        assert weise is not None, "Karen Weise should be in NYT profile"
        patterns = weise.get('known_patterns', '')
        assert 'conflict' in patterns.lower(), \
            "Karen Weise should have CONFLICT NOTE documented"
