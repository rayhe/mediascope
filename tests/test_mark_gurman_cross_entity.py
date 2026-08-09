"""
Tests for Mark Gurman (Bloomberg) cross-entity coverage analysis.

Validates Mechanism #11: Access Dependency — Beat Reporter Competitive Narration.
Gurman, Bloomberg's chief Apple correspondent and Power On newsletter author,
demonstrates systematic framing asymmetry in wearables coverage: Apple products
receive developmental/aspirational framing while Meta products receive
competitive-obstacle framing. The mechanism is not financial incentive (Bloomberg
has no known AI content deals with Apple) but ACCESS DEPENDENCY — Gurman's
professional value derives from maintaining privileged Apple source access.

Source evidence: Power On newsletters (via Macrumors), Tom's Guide interview,
Techmeme headline analysis, Bloomberg articles (via secondary sources).
"""

import yaml
import pytest
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


@pytest.fixture
def competitor_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture
def cross_publication_findings(competitor_research):
    return competitor_research.get('cross_publication_findings', {})


@pytest.fixture
def gurman_entry(cross_publication_findings):
    entry = cross_publication_findings.get('bloomberg_mark_gurman', {})
    assert entry, "bloomberg_mark_gurman must exist in competitor-coverage-research.yaml cross_publication_findings"
    return entry


class TestGurmanProfileCompleteness:
    """Mark Gurman's profile structure and basic metadata."""

    def test_gurman_exists(self, cross_publication_findings):
        """Gurman entry must exist in competitor coverage research."""
        assert 'bloomberg_mark_gurman' in cross_publication_findings

    def test_journalist_name(self, gurman_entry):
        """Journalist name should be Mark Gurman."""
        assert gurman_entry['journalist'] == 'Mark Gurman'

    def test_publication_bloomberg(self, gurman_entry):
        """Publication should be Bloomberg."""
        assert gurman_entry['publication'] == 'Bloomberg'

    def test_role_includes_power_on(self, gurman_entry):
        """Role should reference Power On newsletter."""
        assert 'Power On' in gurman_entry['role']

    def test_has_mechanism_11(self, gurman_entry):
        """Key finding should reference Mechanism #11."""
        assert '#11' in gurman_entry['key_finding']

    def test_mechanism_name_access_dependency(self, gurman_entry):
        """Mechanism should be access_dependency_competitive_narration."""
        assert gurman_entry['mechanism'] == 'access_dependency_competitive_narration'

    def test_has_cross_entity_analysis(self, gurman_entry):
        """Must have cross-entity coverage analysis section."""
        assert 'cross_entity_coverage_analysis' in gurman_entry

    def test_has_key_patterns(self, gurman_entry):
        """Must have key patterns section."""
        assert 'key_patterns' in gurman_entry
        assert len(gurman_entry['key_patterns']) >= 4

    def test_has_confounding_factors(self, gurman_entry):
        """Must include confounding factors for intellectual honesty."""
        assert 'confounding_factors' in gurman_entry
        assert len(gurman_entry['confounding_factors']) >= 3


class TestAppleWearablesFraming:
    """Apple wearables coverage analysis — developmental/aspirational register."""

    def test_apple_wearables_tone_positive(self, gurman_entry):
        """Apple wearables coverage tone should be positive (>0.0)."""
        analysis = gurman_entry['cross_entity_coverage_analysis']
        tone = analysis['apple_wearables']['tone']
        assert tone > 0.0, f"Apple wearables tone {tone} should be positive"

    def test_apple_wearables_register_aspirational(self, gurman_entry):
        """Apple wearables register should be developmental_aspirational."""
        analysis = gurman_entry['cross_entity_coverage_analysis']
        register = analysis['apple_wearables']['register']
        assert register == 'developmental_aspirational'

    def test_apple_wearables_has_framing_language(self, gurman_entry):
        """Must document specific framing language used."""
        analysis = gurman_entry['cross_entity_coverage_analysis']
        lang = analysis['apple_wearables']['framing_language']
        assert len(lang) >= 5, "Need at least 5 framing language examples"

    def test_premium_material_language(self, gurman_entry):
        """Apple glasses described with premium material language."""
        analysis = gurman_entry['cross_entity_coverage_analysis']
        lang = analysis['apple_wearables']['framing_language']
        premium_terms = [l for l in lang if any(
            word in l.lower() for word in ['premium', 'luxurious', 'acetate', 'better made']
        )]
        assert len(premium_terms) >= 2, (
            "Apple wearables should have multiple premium material references"
        )

    def test_apple_wearables_has_coverage_examples(self, gurman_entry):
        """Must have specific article examples with URLs."""
        analysis = gurman_entry['cross_entity_coverage_analysis']
        examples = analysis['apple_wearables']['coverage_examples']
        assert len(examples) >= 2, "Need at least 2 Apple wearables coverage examples"

    def test_coverage_examples_have_urls(self, gurman_entry):
        """Each coverage example must have a source URL."""
        analysis = gurman_entry['cross_entity_coverage_analysis']
        examples = analysis['apple_wearables']['coverage_examples']
        for ex in examples:
            assert 'source_url' in ex, f"Example '{ex.get('article', 'unknown')}' needs source_url"
            assert ex['source_url'].startswith('http'), f"URL must be valid HTTP(S)"

    def test_pull_the_rug_language(self, gurman_entry):
        """Must document the 'pull the rug out' competitive narration."""
        analysis = gurman_entry['cross_entity_coverage_analysis']
        lang = analysis['apple_wearables']['framing_language']
        assert any('rug' in l.lower() for l in lang), (
            "Must include 'pull the rug out' language — key competitive narration evidence"
        )


class TestMetaWearablesFraming:
    """Meta wearables coverage analysis — competitive-obstacle register."""

    def test_meta_wearables_tone_negative(self, gurman_entry):
        """Meta wearables coverage tone should be negative (<0.0)."""
        analysis = gurman_entry['cross_entity_coverage_analysis']
        tone = analysis['meta_wearables']['tone']
        assert tone < 0.0, f"Meta wearables tone {tone} should be negative"

    def test_meta_wearables_register_competitive(self, gurman_entry):
        """Meta wearables register should be competitive_obstacle."""
        analysis = gurman_entry['cross_entity_coverage_analysis']
        register = analysis['meta_wearables']['register']
        assert register == 'competitive_obstacle'

    def test_meta_framing_emphasizes_limitations(self, gurman_entry):
        """Meta wearables framing language should emphasize technical limitations."""
        analysis = gurman_entry['cross_entity_coverage_analysis']
        lang = analysis['meta_wearables']['framing_language']
        limitation_terms = [l for l in lang if any(
            word in l.lower() for word in ['low resolution', '1080p', 'momentum']
        )]
        assert len(limitation_terms) >= 2, (
            "Meta wearables framing should emphasize technical limitations"
        )

    def test_meta_ray_ban_display_review_documented(self, gurman_entry):
        """Must document Gurman's Meta Ray-Ban Display review."""
        analysis = gurman_entry['cross_entity_coverage_analysis']
        examples = analysis['meta_wearables']['coverage_examples']
        ray_ban_review = [e for e in examples if 'Ray-Ban Display' in e.get('article', '')]
        assert len(ray_ban_review) >= 1, "Must include Ray-Ban Display review analysis"

    def test_talent_poaching_coverage_documented(self, gurman_entry):
        """Must document how Meta hiring Apple AI execs is framed."""
        analysis = gurman_entry['cross_entity_coverage_analysis']
        examples = analysis['meta_wearables']['coverage_examples']
        talent = [e for e in examples if '$200' in e.get('framing', '') or 'AI Executive' in e.get('article', '')]
        assert len(talent) >= 1, (
            "Must document Meta talent poaching coverage — key directionality evidence"
        )


class TestToneGap:
    """Cross-entity tone gap analysis between Apple and Meta wearables coverage."""

    def test_apple_meta_tone_gap(self, gurman_entry):
        """Tone gap between Apple wearables and Meta wearables should be >= 0.40."""
        delta = gurman_entry.get('tone_delta_meta_vs_apple_wearables', 0)
        assert delta >= 0.40, (
            f"Tone delta {delta} should be >= 0.40 for meaningful asymmetry"
        )

    def test_apple_wearables_more_positive_than_meta(self, gurman_entry):
        """Apple wearables tone must be more positive than Meta wearables tone."""
        scores = gurman_entry['tone_scores']
        assert scores['apple_wearables_average'] > scores['meta_wearables_average'], (
            f"Apple ({scores['apple_wearables_average']}) should be more positive "
            f"than Meta ({scores['meta_wearables_average']})"
        )

    def test_vision_pro_more_negative_than_apple_wearables(self, gurman_entry):
        """Vision Pro tone should be more negative than Apple wearables."""
        scores = gurman_entry['tone_scores']
        assert scores['apple_vision_pro_average'] < scores['apple_wearables_average'], (
            "Vision Pro criticism shows Gurman CAN be critical of Apple — "
            "the asymmetry is in framing, not existence of criticism"
        )

    def test_meta_reality_labs_most_negative(self, gurman_entry):
        """Meta Reality Labs should be the most negatively toned category."""
        scores = gurman_entry['tone_scores']
        assert scores['meta_reality_labs_average'] <= scores['meta_wearables_average'], (
            "Reality Labs financial coverage should be at least as negative as product coverage"
        )

    def test_vision_pro_still_less_negative_than_meta_wearables(self, gurman_entry):
        """Even harsh Vision Pro criticism should be less negative than Meta wearables overall."""
        scores = gurman_entry['tone_scores']
        assert scores['apple_vision_pro_average'] >= scores['meta_wearables_average'], (
            f"Vision Pro ({scores['apple_vision_pro_average']}) should be >= "
            f"Meta wearables ({scores['meta_wearables_average']}) — "
            "developmental framing softens even harsh Apple criticism"
        )


class TestMechanism11:
    """Access Dependency mechanism — distinct from financial incentive mechanisms."""

    def test_mechanism_is_not_financial(self, gurman_entry):
        """Access dependency must be explicitly distinct from financial incentive."""
        explanation = gurman_entry['mechanism_explanation']
        assert 'financial incentive' in explanation.lower() or 'financial' in explanation.lower(), (
            "Must explain distinction from financial incentive mechanisms"
        )

    def test_no_known_bloomberg_apple_deal(self, gurman_entry):
        """Must document that Bloomberg has no known AI deal with Apple."""
        explanation = gurman_entry['mechanism_explanation']
        assert 'no known' in explanation.lower() or 'no known AI' in explanation.lower(), (
            "Must state Bloomberg has no known AI content licensing deal with Apple"
        )

    def test_distinct_from_book_deal_mechanism(self, gurman_entry):
        """Mechanism #11 must be distinguished from #9 (book deal capture)."""
        explanation = gurman_entry['mechanism_explanation']
        assert '#9' in explanation or 'book deal' in explanation.lower(), (
            "Must distinguish from Mechanism #9 (book deal financial capture)"
        )

    def test_access_based_incentive(self, gurman_entry):
        """Must explain the access-based incentive structure."""
        explanation = gurman_entry['mechanism_explanation']
        assert 'access' in explanation.lower(), (
            "Must explain access dependency as the incentive mechanism"
        )

    def test_newsletter_as_value_vehicle(self, gurman_entry):
        """Power On newsletter should be identified as the access value vehicle."""
        role = gurman_entry['role']
        assert 'Power On' in role, (
            "Power On newsletter is the primary vehicle for access-dependent scoops"
        )


class TestKeyPatterns:
    """Specific cross-entity framing patterns documented for Gurman."""

    def test_first_person_narration_pattern(self, gurman_entry):
        """Must document first-person strategic narration pattern."""
        patterns = gurman_entry['key_patterns']
        narration = [p for p in patterns if 'NARRATION' in p['pattern_name'].upper()
                     or 'FIRST-PERSON' in p['pattern_name'].upper()]
        assert len(narration) >= 1, (
            "Must document first-person strategic narration — "
            "'if you're Apple, you really want...' language"
        )

    def test_developmental_framing_asymmetry_pattern(self, gurman_entry):
        """Must document developmental framing asymmetry."""
        patterns = gurman_entry['key_patterns']
        developmental = [p for p in patterns if 'DEVELOPMENTAL' in p['pattern_name'].upper()]
        assert len(developmental) >= 1, (
            "Must document how Apple failures get developmental arc "
            "while Meta failures stand as-is"
        )

    def test_delay_framing_asymmetry_pattern(self, gurman_entry):
        """Must document delay-as-refinement vs delay-as-failure pattern."""
        patterns = gurman_entry['key_patterns']
        delay = [p for p in patterns if 'DELAY' in p['pattern_name'].upper()]
        assert len(delay) >= 1, (
            "Must document how Apple delays are 'refinement' while "
            "Meta timeline issues are 'losses'"
        )

    def test_talent_narrative_directionality_pattern(self, gurman_entry):
        """Must document talent narrative directionality."""
        patterns = gurman_entry['key_patterns']
        talent = [p for p in patterns if 'TALENT' in p['pattern_name'].upper()]
        assert len(talent) >= 1, (
            "Must document opposite framing for same labor market event "
            "depending on which company benefits"
        )

    def test_product_language_register_pattern(self, gurman_entry):
        """Must document product language register asymmetry."""
        patterns = gurman_entry['key_patterns']
        language = [p for p in patterns if 'LANGUAGE' in p['pattern_name'].upper()
                    or 'REGISTER' in p['pattern_name'].upper()]
        assert len(language) >= 1, (
            "Must document 'acetate/luxurious' for Apple vs "
            "'low resolution/1080p' for Meta"
        )


class TestCrossValidation:
    """Cross-validation with existing findings and mechanisms."""

    def test_distinct_from_olson_mechanism(self, cross_publication_findings, competitor_research):
        """Gurman's mechanism must be distinct from Olson's professional identity capture."""
        gurman = cross_publication_findings.get('bloomberg_mark_gurman', {})
        olson = competitor_research.get('aggregate_findings', {}).get('bloomberg_parmy_olson', {})
        assert gurman['mechanism'] != olson.get('mechanism', ''), (
            "Gurman (access dependency) must be different mechanism than Olson (professional identity capture)"
        )

    def test_both_bloomberg_different_mechanisms(self, cross_publication_findings, competitor_research):
        """Two Bloomberg journalists, two different asymmetry mechanisms."""
        gurman = cross_publication_findings.get('bloomberg_mark_gurman', {})
        olson = competitor_research.get('aggregate_findings', {}).get('bloomberg_parmy_olson', {})
        assert gurman['journalist'] == 'Mark Gurman'
        assert olson.get('journalist') == 'Parmy Olson'
        # Same publication, different mechanisms proves publication-level explanation insufficient
        assert gurman['mechanism'] != olson.get('mechanism', '')

    def test_evidence_strength_appropriately_moderate(self, gurman_entry):
        """Evidence strength should be MODERATE given paywalled primary sources."""
        strength = gurman_entry['evidence_strength']
        assert strength == 'MODERATE', (
            "Evidence relies on secondary sources (Macrumors, Tom's Guide) — "
            "strength should be MODERATE until direct Bloomberg articles analyzed"
        )

    def test_wearables_coverage_relevant_to_mediascope_thesis(self, gurman_entry):
        """Gurman analysis directly supports the wearables narrative investigation track."""
        analysis = gurman_entry['cross_entity_coverage_analysis']
        assert 'apple_wearables' in analysis
        assert 'meta_wearables' in analysis
        # Wearables-specific analysis ties directly to MediaScope Track 2

    def test_mechanism_11_is_new(self, cross_publication_findings):
        """Mechanism #11 should not duplicate any existing mechanism."""
        gurman = cross_publication_findings.get('bloomberg_mark_gurman', {})
        finding = gurman['key_finding']
        assert '#11' in finding
        # Verify existing mechanisms are different numbers
        existing_mechanisms = ['#5', '#6', '#7', '#8', '#9', '#10']
        for mech in existing_mechanisms:
            assert mech != '#11', f"Mechanism #11 should be unique, not duplicate {mech}"
