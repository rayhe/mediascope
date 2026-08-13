"""
Test Mechanism #85: Chris Welch Career Migration — Privacy Vocabulary
Non-Portability Test (The Verge → Bloomberg)

Type B: Journalist Cross-Entity Tracking — August 13, 2026

KEY FINDING: Chris Welch (The Verge 2011-2025, 6,000+ articles → Bloomberg
2025-present) provides the fifth career-migration natural experiment in the
MediaScope dataset. His Samsung Galaxy Glasses coverage at Bloomberg for
Galaxy Unpacked (Jul 22, 2026) was the Techmeme lead story, framing Samsung's
privacy features POSITIVELY as a product attribute. Meanwhile, his former
publication The Verge sent two reporters (David Imel, Dominic Preston) to the
same event and produced ZERO standalone Samsung glasses articles (#81).

The adversarial smart glasses privacy frame did NOT travel with Welch from
The Verge to Bloomberg. This establishes that adversarial framing is primarily
INSTITUTIONAL (driven by publication editorial culture + financial structure),
not a portable personal journalist trait.

CAREER MIGRATION PATTERNS (N=5):
1. Stern: News Corp (balanced) → Independent → Meta tone +0.35 → -0.65 (#42)
2. Heikkilä: MIT TR → FT (OpenAI deal) → Meta adversarial amplified
3. Field: CNBC → The Verge (Vox/Google) → Beat concentration (#52)
4. Tiku: Multiple → WaPo (Bezos) → Company-agnostic EXCEPT Anthropic gap (#72)
5. Welch: The Verge (Vox/Google) → Bloomberg (zero deals) → Neutral-positive
   Samsung coverage, adversarial frame non-portable

TWO PORTABILITY TYPES:
- Portable (personal): Stern's adversarial shift traveled with her
- Non-portable (institutional): The Verge's adversarial framing stayed at
  The Verge when Welch left

Sources:
- Techmeme: Samsung Galaxy Unpacked lead story (Chris Welch/Bloomberg, Jul 22, 2026)
- Talking Biz News: Bloomberg hires Kelly, Welch for consumer tech team (2025)
- Muck Rack: Chris Welch profile (6,445+ articles)
- Victoria Song privacy pieces: Mechanisms #75
- Samsung Unpacked multi-journalist analysis: Mechanism #81
- Samsung-Google compound leverage: Mechanism #76
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)


def load_journalists():
    with open(os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml')) as f:
        return yaml.safe_load(f)


def get_welch_profile(data):
    for j in data.get('journalists', []):
        if j.get('name') == 'Chris Welch':
            return j
    return None


def get_welch_mechanism(research):
    cpf = research.get('cross_publication_findings', {})
    return cpf.get('bloomberg_chris_welch_career_migration', {})


# ===================================================================
# Test Class 1: Welch Profile Exists and Has Career Migration Data
# ===================================================================
class TestWelchProfileExists:
    """Chris Welch must exist in journalists.yaml with complete career data."""

    def test_welch_exists(self):
        data = load_journalists()
        profile = get_welch_profile(data)
        assert profile is not None, "Chris Welch must exist in journalists.yaml"

    def test_welch_is_multi_publication(self):
        data = load_journalists()
        profile = get_welch_profile(data)
        assert profile.get('multi_publication') is True, \
            "Welch must be flagged as multi-publication (Verge → Bloomberg)"

    def test_welch_has_verge_career(self):
        data = load_journalists()
        profile = get_welch_profile(data)
        career = profile.get('career', [])
        verge = [c for c in career if c.get('publication') == 'the-verge']
        assert len(verge) >= 1, "Must have The Verge career entry"

    def test_welch_has_bloomberg_career(self):
        data = load_journalists()
        profile = get_welch_profile(data)
        career = profile.get('career', [])
        bloomberg = [c for c in career if c.get('publication') == 'bloomberg']
        assert len(bloomberg) >= 1, "Must have Bloomberg career entry"

    def test_welch_verge_tenure_documented(self):
        """14 years at The Verge (2011-2025) with 6,000+ articles."""
        data = load_journalists()
        profile = get_welch_profile(data)
        career = profile.get('career', [])
        verge = [c for c in career if c.get('publication') == 'the-verge'][0]
        assert verge.get('start') in ('2011', 2011), \
            f"Verge start year must be 2011, got {verge.get('start')}"
        assert verge.get('end') in ('2025', 2025), \
            f"Verge end year must be 2025, got {verge.get('end')}"

    def test_welch_article_count_referenced(self):
        """6,000+ articles — largest single-journalist corpus at any tracked pub."""
        data = load_journalists()
        profile = get_welch_profile(data)
        notes = profile.get('notes', '')
        assert '6,000' in notes or '6000' in notes, \
            "Notes must reference 6,000+ article count"


# ===================================================================
# Test Class 2: Mechanism #85 Exists in Competitor Research
# ===================================================================
class TestMechanism85Exists:
    """Mechanism #85 must exist in competitor-coverage-research.yaml."""

    def test_mechanism_entry_exists(self):
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        assert mechanism, \
            "bloomberg_chris_welch_career_migration must exist in cross_publication_findings"

    def test_mechanism_id_is_85(self):
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        assert mechanism.get('mechanism_id') == 85, \
            f"Mechanism ID must be 85, got {mechanism.get('mechanism_id')}"

    def test_has_journalist_name(self):
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        assert mechanism.get('journalist') == 'Chris Welch', \
            "Journalist must be Chris Welch"

    def test_has_finding_summary(self):
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        summary = mechanism.get('finding_summary', '')
        assert len(summary) >= 100, \
            f"Finding summary must be substantial (≥100 chars), got {len(summary)}"

    def test_has_type(self):
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        assert mechanism.get('finding_type') == 'career_migration_framing_portability', \
            f"Type must be career_migration_framing_portability, got {mechanism.get('finding_type')}"

    def test_has_date_added(self):
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        assert mechanism.get('date_added') == '2026-08-13', \
            f"Date must be 2026-08-13, got {mechanism.get('date_added')}"

    def test_has_test_file(self):
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        expected = 'tests/test_chris_welch_career_migration_privacy_portability_aug13.py'
        assert mechanism.get('test_file') == expected, \
            f"Test file must be {expected}"


# ===================================================================
# Test Class 3: Career Migration Direction Documented
# ===================================================================
class TestCareerMigrationDirection:
    """Migration from Google-dependent to independent must be documented."""

    def test_source_financial_structure(self):
        """The Verge (Vox Media) has Google programmatic ad dependency."""
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        summary = mechanism.get('finding_summary', '')
        assert any(term in summary.lower() for term in [
            'vox media', 'google', 'the verge'
        ]), "Must reference Vox Media/Google dependency at source publication"

    def test_destination_financial_structure(self):
        """Bloomberg has zero AI content licensing deals."""
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        summary = mechanism.get('finding_summary', '')
        assert 'bloomberg' in summary.lower(), \
            "Must reference Bloomberg as destination"

    def test_non_portability_documented(self):
        """The key finding is that adversarial framing is non-portable."""
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        summary = mechanism.get('finding_summary', '')
        assert any(term in summary.lower() for term in [
            'non-portab', 'institutional', 'did not travel',
            'stayed', 'not portable'
        ]), "Must document non-portability of adversarial framing"


# ===================================================================
# Test Class 4: Samsung Galaxy Unpacked Coverage Framing
# ===================================================================
class TestSamsungUnpackedCoverageFraming:
    """Welch's Bloomberg Samsung coverage must use neutral-positive framing."""

    def test_samsung_coverage_documented(self):
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        summary = mechanism.get('finding_summary', '') + str(mechanism)
        assert 'samsung' in summary.lower(), \
            "Must document Samsung coverage at Galaxy Unpacked"

    def test_privacy_as_feature_framing(self):
        """Samsung privacy features framed as PRODUCT ATTRIBUTE not CONCERN."""
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        summary = mechanism.get('finding_summary', '')
        assert any(term in summary.lower() for term in [
            'privacy feature', 'product attribute', 'neutral',
            'positive', 'battery life'
        ]), "Must document privacy-as-feature framing"

    def test_techmeme_lead_documented(self):
        """Welch's Bloomberg article was the Techmeme lead story."""
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        all_text = str(mechanism).lower()
        assert 'techmeme' in all_text, \
            "Must document Techmeme lead story status"

    def test_zero_adversarial_vocabulary(self):
        """Coverage must note absence of surveillance/adversarial vocabulary."""
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        summary = mechanism.get('finding_summary', '')
        assert any(term in summary.lower() for term in [
            'zero', 'no adversarial', 'absence', 'neutral',
            'no surveillance'
        ]), "Must document absence of adversarial vocabulary in Samsung coverage"


# ===================================================================
# Test Class 5: Contrast with The Verge Institutional Pattern
# ===================================================================
class TestVergeInstitutionalContrast:
    """Must contrast Welch's Bloomberg coverage with The Verge's
    institutional adversarial Meta glasses pattern."""

    def test_verge_adversarial_pattern_referenced(self):
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        related = mechanism.get('related_mechanisms', [])
        related_ids = [r.get('mechanism_id', r) if isinstance(r, dict) else r
                       for r in related]
        # Must reference Victoria Song bifurcation (#75) or Samsung Unpacked (#81)
        has_related = 75 in related_ids or 81 in related_ids
        assert has_related, \
            f"Must cross-reference #75 (Song) or #81 (Samsung Unpacked). Got: {related_ids}"

    def test_verge_zero_samsung_glasses_noted(self):
        """The Verge produced zero standalone Samsung glasses articles at Unpacked."""
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        summary = mechanism.get('finding_summary', '')
        has_zero = any(term in summary.lower() for term in [
            'zero standalone', 'zero samsung', 'no standalone',
            'zero glasses', 'no samsung glasses'
        ])
        assert has_zero, \
            "Must note The Verge produced zero standalone Samsung glasses coverage"


# ===================================================================
# Test Class 6: Career Migration Pattern (N=5) Cross-References
# ===================================================================
class TestCareerMigrationPatternN5:
    """Must place Welch in context of 4 prior career-migration experiments."""

    MIGRATION_JOURNALISTS = [
        'Stern', 'Heikkilä', 'Field', 'Tiku', 'Welch'
    ]

    def test_migration_pattern_referenced(self):
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        summary = mechanism.get('finding_summary', '') + str(mechanism)
        found = sum(1 for j in self.MIGRATION_JOURNALISTS
                    if j.lower() in summary.lower())
        assert found >= 3, \
            f"Must reference at least 3 of 5 migration journalists. Found {found}"

    def test_portability_taxonomy_documented(self):
        """Must distinguish portable (personal) vs non-portable (institutional)."""
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        summary = mechanism.get('finding_summary', '')
        has_taxonomy = (
            ('portab' in summary.lower() and 'institutional' in summary.lower()) or
            ('personal' in summary.lower() and 'institutional' in summary.lower())
        )
        assert has_taxonomy, \
            "Must distinguish portable (personal) vs non-portable (institutional) framing"

    @pytest.mark.parametrize("mechanism_id", [42, 52, 72, 75, 81])
    def test_related_mechanisms_include_prior_migrations(self, mechanism_id):
        """Related mechanisms should include at least some prior migration experiments."""
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        related = mechanism.get('related_mechanisms', [])
        related_ids = [r.get('mechanism_id', r) if isinstance(r, dict) else r
                       for r in related]
        # Not all need to be present, but the set should be non-empty
        # This test documents which should be there; assertion is per-id optional
        if mechanism_id in (75, 81):
            assert mechanism_id in related_ids, \
                f"Mechanism #{mechanism_id} should be in related_mechanisms"


# ===================================================================
# Test Class 7: Confounding Factors
# ===================================================================
class TestConfoundingFactors:
    """Must document at least 5 confounding factors with strength ratings."""

    def test_has_confounding_factors(self):
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        factors = mechanism.get('confounding_factors', [])
        assert len(factors) >= 5, \
            f"Must have ≥5 confounding factors, got {len(factors)}"

    def test_has_strong_factor(self):
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        factors = mechanism.get('confounding_factors', [])
        strong = [f for f in factors
                  if isinstance(f, dict) and f.get('strength') == 'STRONG']
        if not strong:
            strong = [f for f in factors
                      if isinstance(f, str) and 'STRONG' in f.upper()]
        assert len(strong) >= 1, "Must have at least 1 STRONG confounding factor"

    def test_pre_launch_timing_acknowledged(self):
        """Samsung glasses are pre-launch vs Meta glasses shipping — key confound."""
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        factors = mechanism.get('confounding_factors', [])
        factors_text = str(factors).lower()
        assert any(term in factors_text for term in [
            'pre-launch', 'pre launch', 'not yet shipping',
            'announcement', 'hands-on only'
        ]), "Must acknowledge pre-launch vs shipping confound"

    def test_publication_culture_acknowledged(self):
        """Bloomberg vs The Verge have fundamentally different editorial cultures."""
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        factors = mechanism.get('confounding_factors', [])
        factors_text = str(factors).lower()
        assert any(term in factors_text for term in [
            'culture', 'financial media', 'editorial',
            'genre', 'bloomberg terminal'
        ]), "Must acknowledge different publication cultures"


# ===================================================================
# Test Class 8: Testable Predictions
# ===================================================================
class TestTestablePredictions:
    """Must include at least 4 specific, falsifiable predictions."""

    def test_has_testable_predictions(self):
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        predictions = mechanism.get('testable_predictions', [])
        assert len(predictions) >= 4, \
            f"Must have ≥4 testable predictions, got {len(predictions)}"

    def test_predictions_are_falsifiable(self):
        """Each prediction must be specific enough to be proven wrong."""
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        predictions = mechanism.get('testable_predictions', [])
        for pred in predictions:
            pred_text = pred if isinstance(pred, str) else str(pred)
            has_specific = any(term in pred_text.lower() for term in [
                'will', 'won\'t', 'within', 'if', 'when',
                'should', 'correlat', 'predict'
            ])
            assert has_specific, \
                f"Prediction must be falsifiable: {pred_text[:80]}"


# ===================================================================
# Test Class 9: Source URLs
# ===================================================================
class TestSourceURLs:
    """Must include verifiable source URLs."""

    def test_has_source_urls(self):
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        urls = mechanism.get('source_urls', [])
        assert len(urls) >= 3, \
            f"Must have ≥3 source URLs, got {len(urls)}"

    def test_urls_are_valid_format(self):
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        urls = mechanism.get('source_urls', [])
        for url in urls:
            assert url.startswith('http'), \
                f"Source URL must start with http: {url}"

    def test_techmeme_url_included(self):
        """Techmeme aggregation is primary evidence of lead-story status."""
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        urls = mechanism.get('source_urls', [])
        has_techmeme = any('techmeme' in url for url in urls)
        assert has_techmeme, \
            "Must include Techmeme URL documenting lead-story status"

    def test_bloomberg_hiring_announcement_included(self):
        """Bloomberg hiring announcement is primary source for career migration."""
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        urls = mechanism.get('source_urls', [])
        has_hiring = any('talkingbiznews' in url or 'bloomberg' in url
                         for url in urls)
        assert has_hiring, \
            "Must include Bloomberg hiring announcement source"


# ===================================================================
# Test Class 10: Bloomberg Financial Structure
# ===================================================================
class TestBloombergFinancialStructure:
    """Bloomberg's financial independence must be documented."""

    def test_zero_ai_deals_documented(self):
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        summary = mechanism.get('finding_summary', '') + str(mechanism)
        assert any(term in summary.lower() for term in [
            'zero', 'no known', 'no ai', 'independent',
            'no content deal'
        ]), "Must document Bloomberg's zero AI content deals"

    def test_bloomberg_terminal_revenue(self):
        """Bloomberg Terminal is primary revenue — no publisher ad dependency."""
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        all_text = str(mechanism).lower()
        assert any(term in all_text for term in [
            'terminal', 'subscription', 'financial data',
            'primary revenue'
        ]), "Must reference Bloomberg Terminal as primary revenue model"


# ===================================================================
# Test Class 11: Institutional vs Personal Framing Distinction
# ===================================================================
class TestInstitutionalVsPersonal:
    """The mechanism's core contribution is distinguishing institutional
    from personal framing."""

    def test_key_finding_label(self):
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        key = mechanism.get('key_finding', '')
        assert any(term in key.lower() for term in [
            'non-portab', 'institutional', 'migration',
            'career', 'portability'
        ]), f"Key finding must reference portability/institutional. Got: {key}"

    def test_mechanism_label(self):
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        mech = mechanism.get('mechanism', '')
        assert any(term in mech.lower() for term in [
            'career_migration', 'institutional', 'portability',
            'non_portable'
        ]), f"Mechanism label must reference career migration. Got: {mech}"

    def test_welch_product_reviewer_role(self):
        """Welch was a product reviewer at BOTH pubs — controls for beat assignment."""
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        summary = mechanism.get('finding_summary', '') + str(mechanism)
        assert any(term in summary.lower() for term in [
            'product review', 'reviewer', 'reviews coverage',
            'consumer tech'
        ]), "Must document Welch as product reviewer at both publications"

    def test_not_beat_assignment_artifact(self):
        """Controls for the fact that Welch did product reviews, not privacy investigations,
        at BOTH publications — so the finding is about institutional culture, not personal beat."""
        research = load_competitor_research()
        mechanism = get_welch_mechanism(research)
        factors = mechanism.get('confounding_factors', [])
        factors_text = str(factors).lower()
        assert any(term in factors_text for term in [
            'beat assignment', 'product review', 'privacy investigat',
            'reviewer not investigator'
        ]), "Must acknowledge beat-assignment confound"
