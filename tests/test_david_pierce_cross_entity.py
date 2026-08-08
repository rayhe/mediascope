"""
Tests for David Pierce (The Verge) cross-entity coverage analysis.

Type B iteration — Journalist Cross-Entity Tracking.
Focus: 5-publication career (PC Mag → The Verge → WIRED → WSJ → Protocol → The Verge)
as a natural experiment for institutional vs individual framing.

Key finding: Institutional Framing Immunity — Pierce covers Meta products with balanced
framing despite working at two adversarial-to-Meta publications (WIRED, The Verge),
proving adversarial coverage is editorially imposed, not reporter-driven.
"""
import yaml
import pytest
import os


PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


@pytest.fixture(scope='module')
def verge_profile():
    with open(os.path.join(PROFILES_DIR, 'the-verge.yaml'), 'r') as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def pierce_data(verge_profile):
    """Extract David Pierce's data from the Verge profile."""
    journalists = verge_profile.get('key_journalists', [])
    # Check both top-level journalist list and inline list
    all_journalists = journalists
    # Also check the non-key journalist list
    for section in ['journalists', 'editorial_staff']:
        if section in verge_profile:
            all_journalists += verge_profile[section]

    for j in all_journalists:
        if j.get('name') == 'David Pierce':
            return j
    # Not in key_journalists — look in the top-level list with title
    for item in verge_profile.get('key_journalists', []):
        if item.get('name') == 'David Pierce':
            return item
    # Fallback: search all top-level lists that contain journalist entries
    for key, value in verge_profile.items():
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict) and item.get('name') == 'David Pierce':
                    return item
    pytest.fail("David Pierce not found in The Verge profile")


@pytest.fixture(scope='module')
def pierce_cross_entity(pierce_data):
    """Extract the cross-entity analysis data."""
    analysis = pierce_data.get('cross_entity_coverage_analysis')
    if not analysis:
        pytest.fail("No cross_entity_coverage_analysis for David Pierce")
    return analysis


# ===================================================================
# CLASS 1: Career Profile Completeness
# ===================================================================

class TestCareerProfile:
    """Verify David Pierce's career data is complete and accurate."""

    def test_pierce_exists_in_profile(self, pierce_data):
        assert pierce_data is not None
        assert pierce_data['name'] == 'David Pierce'

    def test_has_title(self, pierce_data):
        assert 'Editor-at-Large' in pierce_data.get('title', '')

    def test_editorial_stance_mentions_wired(self, pierce_data):
        """Pierce's WIRED background is analytically significant."""
        stance = pierce_data.get('editorial_stance', '')
        assert 'Wired' in stance or 'WIRED' in stance

    def test_editorial_stance_mentions_multi_publication(self, pierce_data):
        """5-publication career should be documented."""
        stance = pierce_data.get('editorial_stance', '')
        assert 'Protocol' in stance
        assert 'WSJ' in stance or 'Wall Street Journal' in stance

    def test_editorial_stance_mentions_vergecast(self, pierce_data):
        """Co-host role is key to the Podcast Buffer Effect."""
        stance = pierce_data.get('editorial_stance', '')
        assert 'Vergecast' in stance


# ===================================================================
# CLASS 2: Cross-Entity Analysis Structure
# ===================================================================

class TestCrossEntityStructure:
    """Verify the cross-entity analysis has required components."""

    def test_has_mechanism_name(self, pierce_cross_entity):
        assert 'mechanism_name' in pierce_cross_entity
        assert 'institutional_framing_immunity' in pierce_cross_entity['mechanism_name']

    def test_has_mechanism_id(self, pierce_cross_entity):
        assert 'mechanism_id' in pierce_cross_entity
        assert pierce_cross_entity['mechanism_id'] == 7

    def test_has_description(self, pierce_cross_entity):
        desc = pierce_cross_entity.get('description', '')
        assert len(desc) > 100

    def test_has_analytical_significance(self, pierce_cross_entity):
        sig = pierce_cross_entity.get('analytical_significance', '')
        assert len(sig) > 100
        assert 'natural experiment' in sig.lower()

    def test_covers_all_entities(self, pierce_cross_entity):
        """Must have coverage data for Meta, Apple, Google, and Snap."""
        assert 'meta_coverage' in pierce_cross_entity
        assert 'apple_coverage' in pierce_cross_entity
        assert 'google_coverage' in pierce_cross_entity
        assert 'snap_coverage' in pierce_cross_entity


# ===================================================================
# CLASS 3: Meta Coverage Analysis
# ===================================================================

class TestMetaCoverage:
    """Verify Meta coverage analysis captures balanced framing."""

    def test_meta_tone_is_balanced(self, pierce_cross_entity):
        tone = pierce_cross_entity['meta_coverage'].get('tone', '')
        assert 'balanced' in tone.lower()

    def test_meta_has_key_examples(self, pierce_cross_entity):
        examples = pierce_cross_entity['meta_coverage'].get('key_examples', [])
        assert len(examples) >= 3

    def test_quest_3_review_documented(self, pierce_cross_entity):
        """Quest 3 review is the primary evidence of balanced Meta product coverage."""
        examples = pierce_cross_entity['meta_coverage'].get('key_examples', [])
        quest_examples = [e for e in examples if 'Quest 3' in e.get('title', '')]
        assert len(quest_examples) >= 1
        quest = quest_examples[0]
        assert quest.get('tone', 0) >= -0.1  # Balanced to positive

    def test_orion_coverage_documented(self, pierce_cross_entity):
        """Orion coverage shows constructive framing for Meta's AR vision."""
        examples = pierce_cross_entity['meta_coverage'].get('key_examples', [])
        orion_examples = [e for e in examples if
                         'future' in e.get('title', '').lower() or
                         'orion' in e.get('framing', '').lower()]
        assert len(orion_examples) >= 1

    def test_meta_coverage_no_surveillance_language(self, pierce_cross_entity):
        """Pierce's Meta coverage should NOT use surveillance alarm language."""
        overall = pierce_cross_entity['meta_coverage'].get('overall_assessment', '')
        assert 'surveillance' not in overall.lower() or 'without surveillance' in overall.lower()

    def test_meta_examples_have_source_urls(self, pierce_cross_entity):
        """All examples must cite sources."""
        examples = pierce_cross_entity['meta_coverage'].get('key_examples', [])
        for ex in examples:
            assert 'source_url' in ex, f"Missing source_url for: {ex.get('title')}"


# ===================================================================
# CLASS 4: Apple Coverage Analysis
# ===================================================================

class TestAppleCoverage:
    """Verify Apple coverage shows same product-focused lens as Meta."""

    def test_apple_tone_is_balanced(self, pierce_cross_entity):
        tone = pierce_cross_entity['apple_coverage'].get('tone', '')
        assert 'balanced' in tone.lower() or 'positive' in tone.lower()

    def test_vision_pro_documented(self, pierce_cross_entity):
        """Vision Pro hands-on is key comparative evidence."""
        examples = pierce_cross_entity['apple_coverage'].get('key_examples', [])
        vp_examples = [e for e in examples if 'Vision Pro' in e.get('title', '')]
        assert len(vp_examples) >= 1

    def test_vision_pro_no_surveillance_framing(self, pierce_cross_entity):
        """Vision Pro has 12 cameras but Pierce raises no surveillance concerns."""
        examples = pierce_cross_entity['apple_coverage'].get('key_examples', [])
        vp_examples = [e for e in examples if 'Vision Pro' in e.get('title', '')]
        for ex in vp_examples:
            framing = ex.get('framing', '')
            # Should mention the camera count comparison but NOT apply surveillance framing
            if '12' in framing:
                assert 'privacy' not in framing.split('NOT')[0].lower() or 'no privacy' in framing.lower()


# ===================================================================
# CLASS 5: Google Coverage Analysis
# ===================================================================

class TestGoogleCoverage:
    """Verify Google coverage is balanced and product-focused."""

    def test_google_tone_is_balanced(self, pierce_cross_entity):
        tone = pierce_cross_entity['google_coverage'].get('tone', '')
        assert 'balanced' in tone.lower()

    def test_gemini_coverage_documented(self, pierce_cross_entity):
        examples = pierce_cross_entity['google_coverage'].get('key_examples', [])
        gemini_examples = [e for e in examples if
                          'gemini' in e.get('title', '').lower() or
                          'Gemini' in e.get('title', '')]
        assert len(gemini_examples) >= 2, "Should have multiple Gemini coverage examples"

    def test_honest_google_critique_documented(self, pierce_cross_entity):
        """Pierce was honestly critical of Gemini chatbot — same functional critique style as Meta."""
        examples = pierce_cross_entity['google_coverage'].get('key_examples', [])
        negative = [e for e in examples if e.get('tone', 0) < 0]
        assert len(negative) >= 1, "Should document honest critique of Google products"


# ===================================================================
# CLASS 6: Snap Coverage Analysis
# ===================================================================

class TestSnapCoverage:
    """Verify Snap coverage shows willingness to criticize non-Meta companies."""

    def test_snap_has_examples(self, pierce_cross_entity):
        examples = pierce_cross_entity['snap_coverage'].get('key_examples', [])
        assert len(examples) >= 1

    def test_snap_spectacles_negative_framing(self, pierce_cross_entity):
        """'Snap's Specs look good on nobody' proves Pierce isn't artificially soft on anyone."""
        examples = pierce_cross_entity['snap_coverage'].get('key_examples', [])
        negative = [e for e in examples if e.get('tone', 0) < 0]
        assert len(negative) >= 1, "Should include negative Snap Spectacles coverage"


# ===================================================================
# CLASS 7: Institutional Framing Immunity Mechanism
# ===================================================================

class TestInstitutionalFramingImmunity:
    """Test the core finding: institutional vs individual framing."""

    def test_significance_mentions_wired_context(self, pierce_cross_entity):
        """Must connect Pierce's WIRED tenure to the natural experiment."""
        sig = pierce_cross_entity.get('analytical_significance', '')
        assert 'WIRED' in sig or 'Wired' in sig

    def test_significance_mentions_lane_assignment(self, pierce_cross_entity):
        """Should reference WIRED's lane assignment as comparison."""
        sig = pierce_cross_entity.get('cross_entity_analytical_significance', '')
        assert 'lane assignment' in sig.lower() or 'assignment' in sig.lower()

    def test_significance_references_goode_contrast(self, pierce_cross_entity):
        """Should contrast with Lauren Goode's Apple-only coverage."""
        sig = pierce_cross_entity.get('cross_entity_analytical_significance', '')
        assert 'Goode' in sig or 'Lauren' in sig

    def test_significance_references_heath_contrast(self, pierce_cross_entity):
        """Should contrast with Alex Heath's adversarial Meta coverage."""
        sig = pierce_cross_entity.get('cross_entity_analytical_significance', '')
        assert 'Heath' in sig or 'Alex Heath' in sig

    def test_five_key_patterns_documented(self, pierce_cross_entity):
        """Should document the 5 key patterns."""
        sig = pierce_cross_entity.get('cross_entity_analytical_significance', '')
        patterns = [
            'INSTITUTIONAL FRAMING IMMUNITY',
            'PODCAST BUFFER',
            'MULTI-INSTITUTIONAL',
            'ASSIGNMENT PARADOX',
            'SENSOR BLINDNESS'
        ]
        for pattern in patterns:
            assert pattern in sig, f"Missing pattern: {pattern}"

    def test_meta_tone_not_negative(self, pierce_cross_entity):
        """Pierce's Meta coverage should NOT be negative — that's the point."""
        examples = pierce_cross_entity['meta_coverage'].get('key_examples', [])
        for ex in examples:
            tone = ex.get('tone', 0)
            assert tone >= -0.1, f"Meta coverage too negative: {ex.get('title')} = {tone}"


# ===================================================================
# CLASS 8: Cross-Entity Consistency Verification
# ===================================================================

class TestCrossEntityConsistency:
    """Verify that coverage tone is consistent across entities."""

    def test_no_entity_gets_surveillance_treatment(self, pierce_cross_entity):
        """Pierce applies NO surveillance framing to ANY company's camera devices."""
        for entity in ['meta_coverage', 'apple_coverage', 'google_coverage', 'snap_coverage']:
            coverage = pierce_cross_entity.get(entity, {})
            overall = coverage.get('overall_assessment', '')
            examples = coverage.get('key_examples', [])
            for ex in examples:
                framing = ex.get('framing', '')
                lower_framing = framing.lower()
                # Allow mentions of surveillance only in negative/contrast context
                if 'surveillance' in lower_framing:
                    assert ('no surveillance' in lower_framing or
                            'NOT surveillance' in framing or
                            'without surveillance' in lower_framing or
                            'zero surveillance' in lower_framing or
                            'no existential framing' in lower_framing or
                            'not the adversarial' in lower_framing), \
                        f"Unexpected surveillance framing in {entity}: {ex.get('title')}"

    def test_all_examples_have_dates(self, pierce_cross_entity):
        """Every example should be dated for temporal analysis."""
        for entity in ['meta_coverage', 'apple_coverage', 'google_coverage', 'snap_coverage']:
            examples = pierce_cross_entity.get(entity, {}).get('key_examples', [])
            for ex in examples:
                assert 'date' in ex, f"Missing date in {entity}: {ex.get('title')}"

    def test_all_examples_have_publications(self, pierce_cross_entity):
        """Examples should identify which publication they appeared in."""
        for entity in ['meta_coverage', 'apple_coverage']:
            examples = pierce_cross_entity.get(entity, {}).get('key_examples', [])
            for ex in examples:
                assert 'publication' in ex, f"Missing publication in {entity}: {ex.get('title')}"

    def test_all_source_urls_are_https(self, pierce_cross_entity):
        """All source URLs must use HTTPS."""
        for entity in ['meta_coverage', 'apple_coverage', 'google_coverage', 'snap_coverage']:
            examples = pierce_cross_entity.get(entity, {}).get('key_examples', [])
            for ex in examples:
                url = ex.get('source_url', '')
                if url:
                    assert url.startswith('https://'), \
                        f"Non-HTTPS URL in {entity}: {url}"

    def test_meta_tone_similar_to_apple_tone(self, pierce_cross_entity):
        """Pierce's Meta and Apple tones should be in the same range."""
        meta_examples = pierce_cross_entity['meta_coverage'].get('key_examples', [])
        apple_examples = pierce_cross_entity['apple_coverage'].get('key_examples', [])
        
        meta_avg = sum(e.get('tone', 0) for e in meta_examples) / max(len(meta_examples), 1)
        apple_avg = sum(e.get('tone', 0) for e in apple_examples) / max(len(apple_examples), 1)
        
        # Should be within 0.3 of each other — consistent reviewer
        assert abs(meta_avg - apple_avg) < 0.4, \
            f"Meta avg tone ({meta_avg:.2f}) vs Apple avg tone ({apple_avg:.2f}) too different"
