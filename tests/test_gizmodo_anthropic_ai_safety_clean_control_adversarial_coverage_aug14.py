"""
Gizmodo Clean Control — Anthropic AI Safety Adversarial Coverage Consistency

Type A: Competitor Coverage Deep Dive (Aug 14, 2026 07:00 PT)
Mechanism #98: Gizmodo Anthropic AI Safety Adversarial Coverage Consistency

Finding: Gizmodo (Keleops AG, Luxembourg, ZERO financial ties to any tech company)
published 6+ standalone adversarial articles about Anthropic's AI safety and security
incidents from Aug 2025 to Jun 2026. These use adversarial vocabulary, adversarial
headlines, and skeptical editorial framing comparable to Gizmodo's Meta coverage.
This validates the clean-control thesis: a publication without financial ties covers
ALL AI labs with proportionate adversarial scrutiny when genuine safety incidents occur.

Cross-entity comparison matrix:
  - Meta glasses privacy:     6+ articles, tone ~ -0.75, "surveillance," "eerie"
  - Anthropic AI safety:      6+ articles, tone ~ -0.60, "crime spree," "unprecedented risks"
  - OpenAI litigation/ethics: 6+ articles, tone ~ -0.35, "rogue," lawsuit coverage
  - Samsung glasses privacy:  0 surveillance vocab,  tone ~ +0.2, "light," "ecosystem"
  - Google glasses/AI:        0 surveillance vocab,  tone ~ +0.4, "Legit," "Tony Stark"

Samsung/Google softness is incident-proportionate: no comparable incidents pre-launch.
The clean-control thesis predicts adversarial coverage will follow incidents, not entities.

Distinct from:
  - #74 (Gizmodo Snap Specs): glasses privacy vocabulary suppression
  - #80 (Gizmodo Samsung 4-entity): glasses domain clean control
  - #95 (Gizmodo Samsung same-chip): privacy presupposition in glasses
  - #96 (Gizmodo OpenAI litigation): litigation/ethics domain
  - #92 (WIRED AISI trajectory break): WIRED's Anthropic coverage gap

#98 covers: AI SAFETY/SECURITY domain — Gizmodo's longitudinal adversarial Anthropic
coverage (10 months, 6+ articles) across Claude exploitation, Mythos leaks, Claude Code
leak, and NSA penetration. Validates clean control in a NEW domain (AI safety) with a
NEW entity (Anthropic) and LONGITUDINAL timeframe (not single-event).

6 confounding factors (2 STRONG, 2 MODERATE, 2 WEAK).
4 testable predictions.
5 cross-references (#74, #80, #95, #96, #92).
"""

import yaml
import os
import pytest

PROFILE_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
GIZMODO_PATH = os.path.join(PROFILE_DIR, 'gizmodo.yaml')
RESEARCH_PATH = os.path.join(PROFILE_DIR, 'competitor-coverage-research.yaml')
ENTITIES_PATH = os.path.join(PROFILE_DIR, 'competitor-entities.yaml')


@pytest.fixture(scope='module')
def gizmodo_profile():
    with open(GIZMODO_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def research_data():
    with open(RESEARCH_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def entities_data():
    with open(ENTITIES_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def gizmodo_anthropic_safety(gizmodo_profile):
    cross = gizmodo_profile.get('cross_entity_coverage', {})
    section = cross.get('anthropic_ai_safety_adversarial_coverage')
    assert section is not None, (
        "Missing anthropic_ai_safety_adversarial_coverage in gizmodo.yaml cross_entity_coverage"
    )
    return section


@pytest.fixture(scope='module')
def mechanism_98(research_data):
    findings = research_data.get('cross_publication_findings', {})
    section = findings.get('gizmodo_anthropic_ai_safety_clean_control_adversarial_coverage')
    assert section is not None, (
        "Missing gizmodo_anthropic_ai_safety_clean_control_adversarial_coverage in "
        "competitor-coverage-research.yaml cross_publication_findings"
    )
    return section


# -- Class 1: Gizmodo Anthropic Article Count and Structure --------------------


class TestGizmodoAnthropicArticleCount:
    """Verify Gizmodo produced 6+ standalone adversarial Anthropic articles."""

    def test_section_exists(self, gizmodo_anthropic_safety):
        assert gizmodo_anthropic_safety is not None

    def test_mechanism_id(self, gizmodo_anthropic_safety):
        assert gizmodo_anthropic_safety.get('mechanism_id') == 98

    def test_minimum_article_count(self, gizmodo_anthropic_safety):
        articles = gizmodo_anthropic_safety.get('articles', [])
        assert len(articles) >= 6, f"Expected >= 6 articles, got {len(articles)}"

    def test_articles_span_aug_2025_to_jun_2026(self, gizmodo_anthropic_safety):
        """Articles should span ~10 months (Aug 2025 to Jun 2026)."""
        articles = gizmodo_anthropic_safety.get('articles', [])
        dates = [a.get('date', '') for a in articles]
        has_early = any('2025' in d or '2026-01' in d or '2026-02' in d or '2026-03' in d for d in dates)
        has_late = any('2026-05' in d or '2026-06' in d for d in dates)
        assert has_early, "Expected at least one article from 2025 or early 2026"
        assert has_late, "Expected at least one article from May-Jun 2026"

    def test_all_articles_have_urls(self, gizmodo_anthropic_safety):
        articles = gizmodo_anthropic_safety.get('articles', [])
        for a in articles:
            url = a.get('url', '')
            assert url.startswith('https://gizmodo.com/'), (
                f"Invalid or missing URL for article: {a.get('title', 'unknown')}"
            )

    def test_all_articles_have_titles(self, gizmodo_anthropic_safety):
        articles = gizmodo_anthropic_safety.get('articles', [])
        for a in articles:
            assert len(a.get('title', '')) > 10, (
                f"Missing or too-short title: {a.get('title', '')}"
            )

    def test_crime_spree_article_present(self, gizmodo_anthropic_safety):
        """The 'crime spree' Claude exploitation article should be present."""
        articles = gizmodo_anthropic_safety.get('articles', [])
        titles = [a.get('title', '').lower() for a in articles]
        assert any('crime spree' in t for t in titles), (
            "Missing 'Chatbot's Crime Spree' article"
        )

    def test_mythos_nsa_article_present(self, gizmodo_anthropic_safety):
        """The Mythos NSA penetration article should be present."""
        articles = gizmodo_anthropic_safety.get('articles', [])
        titles = [a.get('title', '').lower() for a in articles]
        assert any('nsa' in t or 'sensitive systems' in t for t in titles), (
            "Missing Mythos NSA penetration article"
        )

    def test_claude_code_leak_article_present(self, gizmodo_anthropic_safety):
        """The Claude Code source leak article should be present."""
        articles = gizmodo_anthropic_safety.get('articles', [])
        titles = [a.get('title', '').lower() for a in articles]
        assert any('claude code' in t or 'source code' in t for t in titles), (
            "Missing Claude Code source leak article"
        )


# -- Class 2: Gizmodo Anthropic Adversarial Vocabulary -------------------------


class TestGizmodoAnthropicAdversarialVocabulary:
    """Verify adversarial vocabulary consistent across Anthropic articles."""

    def test_aggregate_tone_negative(self, gizmodo_anthropic_safety):
        tone = gizmodo_anthropic_safety.get('aggregate_tone', 0)
        assert tone < 0, f"Expected negative tone, got {tone}"

    def test_aggregate_tone_range(self, gizmodo_anthropic_safety):
        tone = gizmodo_anthropic_safety.get('aggregate_tone', 0)
        assert -0.80 <= tone <= -0.40, (
            f"Anthropic aggregate tone {tone} outside expected range [-0.80, -0.40]"
        )

    def test_articles_contain_adversarial_language(self, gizmodo_anthropic_safety):
        articles = gizmodo_anthropic_safety.get('articles', [])
        all_language = ' '.join(
            a.get('key_language', '') for a in articles
        ).lower()
        adversarial_markers = [
            'crime spree', 'unprecedented', "can't cover up",
            'panic', 'dangerous', 'hacked', 'leaked', 'too dangerous'
        ]
        found = [m for m in adversarial_markers if m in all_language]
        assert len(found) >= 3, (
            f"Expected >= 3 adversarial language markers, found: {found}"
        )

    def test_individual_articles_all_negative(self, gizmodo_anthropic_safety):
        """Every article in the set should have negative tone."""
        articles = gizmodo_anthropic_safety.get('articles', [])
        for a in articles:
            tone = a.get('tone', 0)
            assert tone < 0, (
                f"Article '{a.get('title', '')[:50]}' has non-negative tone: {tone}"
            )


# -- Class 3: Crime Spree Framing Analysis ------------------------------------


class TestGizmodoAnthropicCrimeSpreeFraming:
    """Verify the 'Chatbot's Crime Spree' article framing analysis."""

    def test_crime_spree_details(self, gizmodo_anthropic_safety):
        articles = gizmodo_anthropic_safety.get('articles', [])
        crime_spree = next(
            (a for a in articles if 'crime spree' in a.get('title', '').lower()),
            None
        )
        assert crime_spree is not None

    def test_crime_spree_url(self, gizmodo_anthropic_safety):
        articles = gizmodo_anthropic_safety.get('articles', [])
        crime_spree = next(
            (a for a in articles if 'crime spree' in a.get('title', '').lower()),
            None
        )
        assert 'gizmodo.com' in crime_spree.get('url', '')

    def test_crime_spree_adversarial_vocabulary(self, gizmodo_anthropic_safety):
        articles = gizmodo_anthropic_safety.get('articles', [])
        crime_spree = next(
            (a for a in articles if 'crime spree' in a.get('title', '').lower()),
            None
        )
        lang = crime_spree.get('key_language', '').lower()
        assert 'crime spree' in lang or 'breach' in lang or 'ssn' in lang or 'ransom' in lang


# -- Class 4: Mythos NSA Penetration Framing -----------------------------------


class TestGizmodoAnthropicMythosNSAFraming:
    """Verify the Mythos NSA penetration article framing analysis."""

    def test_nsa_article_details(self, gizmodo_anthropic_safety):
        articles = gizmodo_anthropic_safety.get('articles', [])
        nsa = next(
            (a for a in articles if 'nsa' in a.get('title', '').lower()
             or 'sensitive systems' in a.get('title', '').lower()),
            None
        )
        assert nsa is not None

    def test_nsa_article_url(self, gizmodo_anthropic_safety):
        articles = gizmodo_anthropic_safety.get('articles', [])
        nsa = next(
            (a for a in articles if 'nsa' in a.get('title', '').lower()
             or 'sensitive systems' in a.get('title', '').lower()),
            None
        )
        assert 'gizmodo.com' in nsa.get('url', '')

    def test_nsa_article_adversarial_tone(self, gizmodo_anthropic_safety):
        articles = gizmodo_anthropic_safety.get('articles', [])
        nsa = next(
            (a for a in articles if 'nsa' in a.get('title', '').lower()
             or 'sensitive systems' in a.get('title', '').lower()),
            None
        )
        assert nsa.get('tone', 0) < 0

    def test_nsa_article_references_five_eyes(self, gizmodo_anthropic_safety):
        articles = gizmodo_anthropic_safety.get('articles', [])
        nsa = next(
            (a for a in articles if 'nsa' in a.get('title', '').lower()
             or 'sensitive systems' in a.get('title', '').lower()),
            None
        )
        lang = nsa.get('key_language', '').lower()
        assert 'five eyes' in lang or 'classified' in lang or 'hours' in lang


# -- Class 5: Claude Code Leak Framing ----------------------------------------


class TestGizmodoAnthropicCodeLeakFraming:
    """Verify Claude Code source leak coverage framing."""

    def test_code_leak_article_present(self, gizmodo_anthropic_safety):
        articles = gizmodo_anthropic_safety.get('articles', [])
        code_leak = next(
            (a for a in articles if 'source code' in a.get('title', '').lower()
             or 'claude code' in a.get('title', '').lower()),
            None
        )
        assert code_leak is not None

    def test_code_leak_dmca_followup_present(self, gizmodo_anthropic_safety):
        """Verify the DMCA takedown follow-up article is present."""
        articles = gizmodo_anthropic_safety.get('articles', [])
        dmca = next(
            (a for a in articles if "can't cover up" in a.get('title', '').lower()
             or 'cover up' in a.get('title', '').lower()),
            None
        )
        assert dmca is not None, "Missing DMCA takedown follow-up article"

    def test_code_leak_ipo_timing_noted(self, gizmodo_anthropic_safety):
        """Gizmodo noted the irony of the leak timing relative to IPO."""
        articles = gizmodo_anthropic_safety.get('articles', [])
        code_articles = [
            a for a in articles
            if 'source code' in a.get('title', '').lower()
            or 'cover up' in a.get('title', '').lower()
            or 'claude code' in a.get('title', '').lower()
        ]
        all_lang = ' '.join(a.get('key_language', '') for a in code_articles).lower()
        assert 'ipo' in all_lang or 'timing' in all_lang or 'vibe coding' in all_lang


# -- Class 6: Cross-Entity Adversarial Consistency ----------------------------


class TestCrossEntityAdversarialConsistency:
    """Verify Gizmodo applies adversarial framing across ALL entities with incidents."""

    def test_cross_entity_matrix_present(self, gizmodo_anthropic_safety):
        matrix = gizmodo_anthropic_safety.get('cross_entity_comparison_matrix', {})
        assert len(matrix) >= 3, (
            f"Expected >= 3 entities in comparison matrix, got {len(matrix)}"
        )

    def test_meta_adversarial(self, gizmodo_anthropic_safety):
        matrix = gizmodo_anthropic_safety.get('cross_entity_comparison_matrix', {})
        meta = matrix.get('meta', {})
        assert meta.get('tone', 0) < 0, "Meta should have adversarial (negative) tone"

    def test_anthropic_adversarial(self, gizmodo_anthropic_safety):
        matrix = gizmodo_anthropic_safety.get('cross_entity_comparison_matrix', {})
        anthropic = matrix.get('anthropic', {})
        assert anthropic.get('tone', 0) < 0, "Anthropic should have adversarial (negative) tone"

    def test_openai_adversarial(self, gizmodo_anthropic_safety):
        matrix = gizmodo_anthropic_safety.get('cross_entity_comparison_matrix', {})
        openai_entry = matrix.get('openai', {})
        assert openai_entry.get('tone', 0) < 0, "OpenAI should have adversarial (negative) tone"

    def test_samsung_neutral_or_positive(self, gizmodo_anthropic_safety):
        matrix = gizmodo_anthropic_safety.get('cross_entity_comparison_matrix', {})
        samsung = matrix.get('samsung', {})
        assert samsung.get('tone', 0) >= 0, "Samsung should have neutral/positive tone (no incidents)"

    def test_google_neutral_or_positive(self, gizmodo_anthropic_safety):
        matrix = gizmodo_anthropic_safety.get('cross_entity_comparison_matrix', {})
        google = matrix.get('google', {})
        assert google.get('tone', 0) >= 0, "Google should have neutral/positive tone (no incidents)"

    def test_incident_responsive_pattern(self, gizmodo_anthropic_safety):
        """Adversarial framing correlates with incidents, not entity identity."""
        matrix = gizmodo_anthropic_safety.get('cross_entity_comparison_matrix', {})
        # Entities WITH incidents should all be negative
        incident_entities = ['meta', 'anthropic', 'openai']
        for entity in incident_entities:
            entry = matrix.get(entity, {})
            assert entry.get('tone', 0) < 0, (
                f"{entity} has incidents but non-negative tone: {entry.get('tone')}"
            )
        # Entities WITHOUT incidents should be neutral/positive
        no_incident_entities = ['samsung', 'google']
        for entity in no_incident_entities:
            entry = matrix.get(entity, {})
            assert entry.get('tone', 0) >= 0, (
                f"{entity} has no incidents but negative tone: {entry.get('tone')}"
            )


# -- Class 7: Clean Control Incident Proportionality ---------------------------


class TestCleanControlIncidentProportionality:
    """Validate that Gizmodo's framing is proportionate to incident severity."""

    def test_meta_most_adversarial(self, gizmodo_anthropic_safety):
        """Meta gets harshest framing due to Cambridge Analytica legacy + glasses privacy."""
        matrix = gizmodo_anthropic_safety.get('cross_entity_comparison_matrix', {})
        meta_tone = matrix.get('meta', {}).get('tone', 0)
        anthropic_tone = matrix.get('anthropic', {}).get('tone', 0)
        assert meta_tone < anthropic_tone, (
            f"Meta ({meta_tone}) should be more adversarial than Anthropic ({anthropic_tone})"
        )

    def test_anthropic_more_adversarial_than_openai(self, gizmodo_anthropic_safety):
        """Anthropic gets harsher coverage than OpenAI at Gizmodo (more/worse safety incidents)."""
        matrix = gizmodo_anthropic_safety.get('cross_entity_comparison_matrix', {})
        anthropic_tone = matrix.get('anthropic', {}).get('tone', 0)
        openai_tone = matrix.get('openai', {}).get('tone', 0)
        assert anthropic_tone <= openai_tone, (
            f"Anthropic ({anthropic_tone}) should be at least as adversarial as OpenAI ({openai_tone})"
        )

    def test_anthropic_article_count_matches_incident_volume(self, gizmodo_anthropic_safety):
        """6+ articles proportionate to 6+ major Anthropic incidents."""
        articles = gizmodo_anthropic_safety.get('articles', [])
        assert len(articles) >= 6, (
            f"Article count {len(articles)} should match incident volume (≥6)"
        )

    def test_longitudinal_coverage(self, gizmodo_anthropic_safety):
        """Coverage spans 10+ months — not a single-event spike."""
        timespan = gizmodo_anthropic_safety.get('coverage_timespan_months', 0)
        assert timespan >= 8, (
            f"Coverage timespan {timespan} months should be >= 8"
        )


# -- Class 8: Confounding Factor Quality --------------------------------------


class TestConfoundingFactorQuality:
    """Verify 6 confounding factors with proper strength labels."""

    def test_six_confounding_factors(self, mechanism_98):
        factors = mechanism_98.get('confounding_factors', [])
        assert len(factors) >= 6, f"Expected >= 6 confounding factors, got {len(factors)}"

    def test_factors_have_strength_labels(self, mechanism_98):
        factors = mechanism_98.get('confounding_factors', [])
        for f in factors:
            strength = f.get('strength', '')
            assert strength in ('STRONG', 'MODERATE', 'WEAK'), (
                f"Factor missing valid strength label: {f.get('factor', '')[:60]}"
            )

    def test_two_strong_factors(self, mechanism_98):
        factors = mechanism_98.get('confounding_factors', [])
        strong = [f for f in factors if f.get('strength') == 'STRONG']
        assert len(strong) == 2, f"Expected 2 STRONG factors, got {len(strong)}"

    def test_two_moderate_factors(self, mechanism_98):
        factors = mechanism_98.get('confounding_factors', [])
        moderate = [f for f in factors if f.get('strength') == 'MODERATE']
        assert len(moderate) == 2, f"Expected 2 MODERATE factors, got {len(moderate)}"

    def test_two_weak_factors(self, mechanism_98):
        factors = mechanism_98.get('confounding_factors', [])
        weak = [f for f in factors if f.get('strength') == 'WEAK']
        assert len(weak) == 2, f"Expected 2 WEAK factors, got {len(weak)}"

    def test_editorial_identity_confound(self, mechanism_98):
        """Gizmodo's inherently skeptical editorial DNA is a STRONG confound."""
        factors = mechanism_98.get('confounding_factors', [])
        text = ' '.join(f.get('factor', '') for f in factors).lower()
        assert 'editorial' in text or 'skeptical' in text or 'site dna' in text or 'identity' in text

    def test_incident_proportionality_confound(self, mechanism_98):
        """Anthropic genuinely had more/worse incidents is a STRONG confound."""
        factors = mechanism_98.get('confounding_factors', [])
        text = ' '.join(f.get('factor', '') for f in factors).lower()
        assert 'incident' in text or 'proportionate' in text or 'worse' in text

    def test_hypocrisy_angle_confound(self, mechanism_98):
        """Anthropic's safety-first branding creates hypocrisy angle (MODERATE)."""
        factors = mechanism_98.get('confounding_factors', [])
        text = ' '.join(f.get('factor', '') for f in factors).lower()
        assert 'hypocrisy' in text or 'safety-first' in text or 'branding' in text or 'positioning' in text


# -- Class 9: Source URL Presence ----------------------------------------------


class TestSourceURLPresence:
    """Verify source URLs are present and properly formatted."""

    def test_source_urls_present(self, mechanism_98):
        urls = mechanism_98.get('source_urls', [])
        assert len(urls) >= 6, f"Expected >= 6 source URLs, got {len(urls)}"

    def test_gizmodo_urls_present(self, mechanism_98):
        urls = mechanism_98.get('source_urls', [])
        gizmodo_urls = [u for u in urls if 'gizmodo.com' in u]
        assert len(gizmodo_urls) >= 6, f"Expected >= 6 Gizmodo URLs, got {len(gizmodo_urls)}"

    def test_all_urls_valid_format(self, mechanism_98):
        urls = mechanism_98.get('source_urls', [])
        for url in urls:
            assert url.startswith('https://'), f"URL must start with https://: {url}"

    def test_anthropic_coverage_in_entities(self, entities_data):
        """Verify Anthropic entity in competitor-entities.yaml has gizmodo_clean_control field."""
        anthropic = entities_data.get('entities', {}).get('anthropic', {})
        giz = anthropic.get('gizmodo_clean_control_adversarial_coverage', {})
        assert giz, (
            "Anthropic entity should have gizmodo_clean_control_adversarial_coverage section"
        )

    def test_mechanism_98_test_file(self, mechanism_98):
        tf = mechanism_98.get('test_file', '')
        assert 'gizmodo_anthropic_ai_safety_clean_control_adversarial_coverage_aug14' in tf


# -- Class 10: Mechanism Distinctiveness ----------------------------------------


class TestMechanismDistinctiveness:
    """Verify mechanism #98 is distinct from related mechanisms (#74, #80, #95, #96, #92)."""

    def test_distinct_from_mechanism_74(self, mechanism_98):
        """#74 covers Snap Specs camera privacy vocabulary; #98 covers AI safety/security."""
        summary = mechanism_98.get('finding_summary', '')
        assert 'ai safety' in summary.lower() or 'security' in summary.lower()

    def test_distinct_from_mechanism_80(self, mechanism_98):
        """#80 covers Samsung 4-entity glasses clean control; #98 covers Anthropic AI safety."""
        summary = mechanism_98.get('finding_summary', '')
        assert 'anthropic' in summary.lower()

    def test_distinct_from_mechanism_96(self, mechanism_98):
        """#96 covers OpenAI litigation; #98 covers Anthropic AI safety incidents."""
        domain = mechanism_98.get('domain', '')
        assert 'ai_safety' in domain.lower() or 'security' in domain.lower()

    def test_domain_is_ai_safety_security(self, mechanism_98):
        domain = mechanism_98.get('domain', '')
        assert 'ai_safety' in domain.lower() or 'security' in domain.lower()

    def test_mechanism_id_98(self, mechanism_98):
        assert mechanism_98.get('mechanism_id') == 98

    def test_distinct_from_mechanism_92(self, mechanism_98):
        """#92 covers WIRED AISI trajectory break; #98 covers Gizmodo adversarial Anthropic."""
        summary = mechanism_98.get('finding_summary', '')
        assert 'gizmodo' in summary.lower()

    def test_longitudinal_scope(self, mechanism_98):
        """#98 is LONGITUDINAL (10 months) not single-event like most mechanisms."""
        summary = mechanism_98.get('finding_summary', '')
        assert '10 months' in summary or 'longitudinal' in summary.lower() or \
               'aug 2025' in summary.lower() or 'months' in summary.lower()

    def test_new_entity_coverage(self, mechanism_98):
        """#98 targets Anthropic — first Gizmodo clean-control in AI safety domain."""
        entities = mechanism_98.get('entities', [])
        assert 'anthropic' in entities


# -- Cross-References (from research data) ------------------------------------


class TestCrossReferences:
    """Verify cross-references to #74, #80, #95, #96, #92."""

    def _get_refs(self, mechanism_98):
        refs = mechanism_98.get('cross_references', [])
        ref_ids = []
        for r in refs:
            if isinstance(r, dict):
                ref_ids.append(r.get('mechanism_id', 0))
            elif isinstance(r, int):
                ref_ids.append(r)
        return ref_ids

    def test_references_mechanism_74(self, mechanism_98):
        assert 74 in self._get_refs(mechanism_98), "Missing cross-reference to #74"

    def test_references_mechanism_80(self, mechanism_98):
        assert 80 in self._get_refs(mechanism_98), "Missing cross-reference to #80"

    def test_references_mechanism_95(self, mechanism_98):
        assert 95 in self._get_refs(mechanism_98), "Missing cross-reference to #95"

    def test_references_mechanism_96(self, mechanism_98):
        assert 96 in self._get_refs(mechanism_98), "Missing cross-reference to #96"

    def test_references_mechanism_92(self, mechanism_98):
        assert 92 in self._get_refs(mechanism_98), "Missing cross-reference to #92"

    def test_at_least_five_references(self, mechanism_98):
        refs = mechanism_98.get('cross_references', [])
        assert len(refs) >= 5, f"Expected >= 5 cross-references, got {len(refs)}"


# -- Testable Predictions -----------------------------------------------------


class TestTestablePredictions:
    """Verify 4 specific, falsifiable testable predictions."""

    def test_four_predictions(self, mechanism_98):
        preds = mechanism_98.get('testable_predictions', [])
        assert len(preds) >= 4, f"Expected >= 4 predictions, got {len(preds)}"

    def test_samsung_google_incident_prediction(self, mechanism_98):
        """When Samsung/Google have incidents, Gizmodo will cover adversarially."""
        preds = mechanism_98.get('testable_predictions', [])
        text = ' '.join(
            p if isinstance(p, str) else p.get('prediction', '') for p in preds
        ).lower()
        assert 'samsung' in text or 'google' in text

    def test_anthropic_fewer_incidents_prediction(self, mechanism_98):
        """If Anthropic has fewer incidents, Gizmodo adversarial count decreases."""
        preds = mechanism_98.get('testable_predictions', [])
        text = ' '.join(
            p if isinstance(p, str) else p.get('prediction', '') for p in preds
        ).lower()
        assert 'fewer' in text or 'decrease' in text or 'proportional' in text

    def test_amazon_nyt_prediction(self, mechanism_98):
        """Amazon-investor publications will show softer Anthropic coverage."""
        preds = mechanism_98.get('testable_predictions', [])
        text = ' '.join(
            p if isinstance(p, str) else p.get('prediction', '') for p in preds
        ).lower()
        assert 'amazon' in text or 'investor' in text or 'softer' in text

    def test_gemini_breach_prediction(self, mechanism_98):
        """If Google Gemini has a breach, Gizmodo covers adversarially."""
        preds = mechanism_98.get('testable_predictions', [])
        text = ' '.join(
            p if isinstance(p, str) else p.get('prediction', '') for p in preds
        ).lower()
        assert 'gemini' in text or 'breach' in text or 'google' in text
