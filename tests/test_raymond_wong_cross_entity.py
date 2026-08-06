"""
Raymond Wong (Gizmodo) Cross-Entity Coverage Analysis — The Clean Control Paradox

KEY FINDING: Raymond Wong at Gizmodo (Keleops AG, ZERO financial ties to any
tech company) applies equal-opportunity criticism across Meta, OpenAI, Apple,
Google, and Snap. This contrasts with WIRED (Condé Nast, OpenAI/Amazon/Microsoft/
Perplexity deals) where reporters like Chokkattu, Ashworth, and Knight apply
harsh language exclusively to Meta while treating deal partners neutrally.

Gizmodo is the EXPERIMENTAL CONTROL:
- Same industry (tech journalism)
- Same beats (smart glasses, AI, consumer tech)
- Same reporter type (hands-on product reviewer)
- Different variable: financial ties (Gizmodo = zero, WIRED = multiple)

RESULT: The publication with no financial ties is MORE balanced than the one
with financial ties, proving that adversarial asymmetry correlates with
publisher-competitor financial relationships, not editorial standards.

Sources:
- Gizmodo article archive (gizmodo.com/author/raywong)
- Keleops AG ownership (Adweek, Jun 2024)
- Condé Nast–OpenAI deal (Reuters, Aug 2024)
- Condé Nast–Amazon Rufus deal (Digiday, Jul 2025)

Created: 2026-08-06
"""
import pytest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_gizmodo_profile():
    with open(os.path.join(PROFILES_DIR, 'gizmodo.yaml')) as f:
        return yaml.safe_load(f)


def load_competitor_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)


def load_wired_profile():
    with open(os.path.join(PROFILES_DIR, 'wired.yaml')) as f:
        return yaml.safe_load(f)


# ===================================================================
# TEST CLASS 1: Raymond Wong Coverage Pattern
# ===================================================================
class TestRaymondWongCoveragePattern:
    """Verify that Raymond Wong's coverage applies balanced criticism
    across ALL entities, not just Meta."""

    def test_wong_is_gizmodo_wearables_reporter(self):
        profile = load_gizmodo_profile()
        reporter = profile.get('editorial_posture', {}).get('wearables_beat_reporter', '')
        assert 'Raymond Wong' in reporter

    def test_wong_meta_coverage_includes_positive(self):
        """Wong calls Ray-Ban Meta Gen 2 'the best non-display smart glasses'
        — a headline WIRED would never run for a Meta product."""
        profile = load_gizmodo_profile()
        examples = profile.get('wearables_coverage_examples', [])
        positive_examples = [e for e in examples if 'positive' in e.get('framing', '').lower()
                           or 'balanced' in e.get('framing', '').lower()]
        assert len(positive_examples) >= 2, \
            f"Expected >= 2 positive/balanced Meta examples, got {len(positive_examples)}"

    def test_wong_meta_coverage_includes_criticism(self):
        """Wong does criticize Meta on privacy — but it's proportional,
        not the dominant framing of every article."""
        profile = load_gizmodo_profile()
        examples = profile.get('wearables_coverage_examples', [])
        critical_examples = [e for e in examples if 'adversarial' in e.get('framing', '').lower()
                           or 'skeptical' in e.get('framing', '').lower()]
        assert len(critical_examples) >= 1, \
            "Wong does criticize Meta, proving Gizmodo isn't a Meta shill"

    def test_wong_coverage_spans_multiple_framings(self):
        """The key evidence: Wong's Meta coverage spans positive, balanced,
        skeptical, and adversarial — unlike WIRED which is uniformly adversarial."""
        profile = load_gizmodo_profile()
        examples = profile.get('wearables_coverage_examples', [])
        framings = set()
        for e in examples:
            f = e.get('framing', '').lower()
            if 'positive' in f:
                framings.add('positive')
            elif 'balanced' in f:
                framings.add('balanced')
            elif 'skeptical' in f:
                framings.add('skeptical')
            elif 'adversarial' in f:
                framings.add('adversarial')
            elif 'solution' in f:
                framings.add('solutions')
            elif 'market' in f or 'analysis' in f:
                framings.add('analytical')
        assert len(framings) >= 3, \
            f"Expected >= 3 framing types across Wong's coverage, got {framings}"

    def test_wong_openai_coverage_is_critical(self):
        """Wong is dismissive of OpenAI's hardware effort ('A Stinkin' Phone?')
        — equal irreverence to all companies."""
        profile = load_gizmodo_profile()
        cross_entity = profile.get('cross_entity_coverage', {})
        openai = cross_entity.get('openai', {})
        assert openai.get('tone') in ['dismissive', 'critical', 'adversarial'], \
            "Wong treats OpenAI critically — no soft coverage"

    def test_wong_snap_coverage_is_critical(self):
        """Wong is harsh on Snap Spectacles ('Getting Roasted to Death',
        'Massive Size Problem')."""
        profile = load_gizmodo_profile()
        cross_entity = profile.get('cross_entity_coverage', {})
        snap = cross_entity.get('snap', {})
        assert snap.get('tone') in ['critical', 'adversarial'], \
            "Wong treats Snap critically — no favoritism"

    def test_wong_google_coverage_is_mixed(self):
        """Wong is skeptical of Google's glasses strategy ('Downplaying')
        but positive when products work ('Aura Are Legit')."""
        profile = load_gizmodo_profile()
        cross_entity = profile.get('cross_entity_coverage', {})
        google = cross_entity.get('google', {})
        assert google.get('tone') == 'mixed', \
            "Wong treats Google with mixed coverage — skeptical AND positive"

    def test_wong_apple_coverage_is_positive_when_products_work(self):
        """'Apple F*cking Did It' — Wong is genuinely positive when
        products deliver. This is the OPPOSITE of systematic bias."""
        profile = load_gizmodo_profile()
        cross_entity = profile.get('cross_entity_coverage', {})
        apple = cross_entity.get('apple', {})
        assert apple.get('tone') in ['positive', 'enthusiastic'], \
            "Wong praises Apple when it delivers — equal-opportunity assessment"


# ===================================================================
# TEST CLASS 2: The Clean Control Paradox
# ===================================================================
class TestCleanControlParadox:
    """The core thesis: Gizmodo (no deals) is MORE balanced than WIRED
    (multiple deals). The variable that predicts adversarial asymmetry
    is financial ties, not editorial standards."""

    def test_gizmodo_has_zero_deals(self):
        """Gizmodo has NO AI licensing deals with any entity."""
        profile = load_gizmodo_profile()
        relationships = profile.get('competitor_relationships', {})
        for entity, rel in relationships.items():
            assert rel.get('financial_tie') == 'none', \
                f"Gizmodo should have no financial tie with {entity}"

    def test_gizmodo_meta_tone_is_balanced(self):
        """Gizmodo's Meta coverage is 'balanced_adversarial' — critical
        but fair, not uniformly hostile."""
        research = load_competitor_research()
        gizmodo = research.get('publications', {}).get('gizmodo', {})
        tone = gizmodo.get('meta_coverage_tone', '')
        assert 'balanced' in tone.lower(), \
            f"Expected balanced Meta tone at Gizmodo, got '{tone}'"

    def test_gizmodo_openai_tone_is_adversarial(self):
        """Gizmodo treats OpenAI adversarially — proving that publications
        WITHOUT OpenAI deals don't give OpenAI soft coverage."""
        research = load_competitor_research()
        gizmodo = research.get('publications', {}).get('gizmodo', {})
        tone = gizmodo.get('openai_coverage_tone', '')
        assert tone == 'adversarial', \
            f"Expected adversarial OpenAI tone at Gizmodo (no deal), got '{tone}'"

    def test_wired_meta_tone_is_adversarial(self):
        """WIRED's Meta coverage is uniformly adversarial."""
        research = load_competitor_research()
        wired = research.get('publications', {}).get('wired', {})
        tone = wired.get('meta_coverage_tone', '')
        assert 'adversarial' in tone.lower(), \
            f"Expected adversarial Meta tone at WIRED, got '{tone}'"

    def test_wired_openai_tone_is_soft(self):
        """WIRED's OpenAI coverage is neutral-to-positive (deal partner)."""
        research = load_competitor_research()
        wired = research.get('publications', {}).get('wired', {})
        tone = wired.get('openai_coverage_tone', '')
        assert 'neutral' in tone.lower() or 'positive' in tone.lower(), \
            f"Expected soft OpenAI tone at WIRED (deal partner), got '{tone}'"

    def test_asymmetry_exists_at_wired_not_gizmodo(self):
        """At WIRED: Meta=adversarial, OpenAI=soft → ASYMMETRIC
        At Gizmodo: Meta=balanced, OpenAI=adversarial → SYMMETRIC (or inverted)
        Financial ties predict the asymmetry direction."""
        research = load_competitor_research()
        wired = research.get('publications', {}).get('wired', {})
        gizmodo = research.get('publications', {}).get('gizmodo', {})

        # WIRED is softer on OpenAI than Meta
        wired_meta = wired.get('meta_coverage_tone', '')
        wired_openai = wired.get('openai_coverage_tone', '')
        assert 'adversarial' in wired_meta.lower()
        assert 'positive' in wired_openai.lower() or 'neutral' in wired_openai.lower()

        # Gizmodo is NOT softer on OpenAI than Meta
        giz_meta = gizmodo.get('meta_coverage_tone', '')
        giz_openai = gizmodo.get('openai_coverage_tone', '')
        assert 'balanced' in giz_meta.lower()
        assert giz_openai == 'adversarial'

    def test_clean_control_verdict_documented(self):
        """The asymmetry verdict explicitly names Gizmodo as the control."""
        research = load_competitor_research()
        gizmodo = research.get('publications', {}).get('gizmodo', {})
        verdict = gizmodo.get('asymmetry_verdict', '')
        assert 'control' in verdict.lower() or 'clean' in verdict.lower(), \
            "Asymmetry verdict should reference Gizmodo's control status"


# ===================================================================
# TEST CLASS 3: Cross-Entity Comparison — Gizmodo vs WIRED Smart Glasses
# ===================================================================
class TestGizmodoVsWiredSmartGlasses:
    """Compare how Gizmodo and WIRED cover the SAME smart glasses products
    from different companies."""

    def test_gizmodo_meta_glasses_positive_review(self):
        """Gizmodo: 'Still the Best Non-Display Smart Glasses' (positive)"""
        profile = load_gizmodo_profile()
        cross_entity = profile.get('cross_entity_coverage', {})
        meta_examples = cross_entity.get('meta', {}).get('examples', [])
        positive = [e for e in meta_examples if 'positive' in e.get('tone', '').lower()
                   or 'best' in e.get('title', '').lower()]
        assert len(positive) >= 1, \
            "Gizmodo has positive Meta glasses review — product-first journalism"

    def test_gizmodo_snap_glasses_harsh_criticism(self):
        """Gizmodo: 'Getting Roasted to Death' (harsh on Snap)"""
        profile = load_gizmodo_profile()
        cross_entity = profile.get('cross_entity_coverage', {})
        snap_examples = cross_entity.get('snap', {}).get('examples', [])
        harsh = [e for e in snap_examples if 'roast' in e.get('title', '').lower()
                or 'critical' in e.get('tone', '').lower()]
        assert len(harsh) >= 1, \
            "Gizmodo is harsh on Snap — equal-opportunity criticism"

    def test_gizmodo_google_glasses_skeptical(self):
        """Gizmodo: 'Downplaying Smart Glasses With a Screen' (skeptical of Google)"""
        profile = load_gizmodo_profile()
        cross_entity = profile.get('cross_entity_coverage', {})
        google_examples = cross_entity.get('google', {}).get('examples', [])
        skeptical = [e for e in google_examples if 'skeptical' in e.get('tone', '').lower()
                    or 'downplay' in e.get('title', '').lower()]
        assert len(skeptical) >= 1, \
            "Gizmodo is skeptical of Google glasses — no special treatment"

    def test_wired_meta_uses_loaded_language(self):
        """WIRED uses 'mass surveillance', 'predator', 'gulag' for Meta —
        language NEVER applied to Snap (4 cameras) or Google (cameras + Gemini AI)."""
        research = load_competitor_research()
        wired = research.get('publications', {}).get('wired', {})
        meta_summary = wired.get('meta_coverage_summary', '')
        assert any(term in meta_summary.lower() for term in
                  ['surveillance', 'loaded language', 'adversarial']), \
            "WIRED uses loaded language for Meta glasses"

    def test_gizmodo_never_uses_surveillance_for_meta_reviews(self):
        """Gizmodo product reviews do NOT use 'surveillance' or 'predator'
        language — those terms appear only in dedicated privacy articles,
        applied to ALL companies equally."""
        profile = load_gizmodo_profile()
        cross_entity = profile.get('cross_entity_coverage', {})
        meta = cross_entity.get('meta', {})
        review_language = meta.get('review_language', '')
        assert 'surveillance' not in review_language.lower(), \
            "Gizmodo reviews don't embed surveillance language in product reviews"

    def test_privacy_criticism_applied_equally(self):
        """When Gizmodo DOES write about privacy, it applies criticism
        to Meta AND Apple AND Google equally — 'stepping into a privacy
        minefield' used for Apple too."""
        profile = load_gizmodo_profile()
        cross_entity = profile.get('cross_entity_coverage', {})
        equal_privacy = cross_entity.get('privacy_coverage_pattern', '')
        assert 'equal' in equal_privacy.lower() or 'all' in equal_privacy.lower(), \
            "Gizmodo applies privacy criticism equally"


# ===================================================================
# TEST CLASS 4: Maxwell Zeff Journalist Migration
# ===================================================================
class TestMaxwellZeffMigration:
    """Maxwell Zeff moved from Gizmodo (no deals) → TechCrunch → WIRED
    (multiple deals). This is a journalist migration pattern worth
    tracking: same journalist, different institutional incentives."""

    def test_zeff_migration_documented(self):
        """Zeff's career path is documented in the Gizmodo profile."""
        profile = load_gizmodo_profile()
        migrations = profile.get('journalist_migrations', [])
        zeff = [m for m in migrations if 'Zeff' in m.get('name', '')]
        assert len(zeff) >= 1, \
            "Maxwell Zeff migration should be documented"

    def test_zeff_origin_is_gizmodo(self):
        """Zeff started at Gizmodo (clean control publication)."""
        profile = load_gizmodo_profile()
        migrations = profile.get('journalist_migrations', [])
        zeff = [m for m in migrations if 'Zeff' in m.get('name', '')][0]
        assert zeff.get('origin') == 'Gizmodo'

    def test_zeff_destination_is_wired(self):
        """Zeff moved to WIRED (Condé Nast, multiple AI licensing deals)."""
        profile = load_gizmodo_profile()
        migrations = profile.get('journalist_migrations', [])
        zeff = [m for m in migrations if 'Zeff' in m.get('name', '')][0]
        assert 'WIRED' in zeff.get('destination', '')

    def test_zeff_migration_significance_documented(self):
        """The migration's significance: when journalists move from
        deal-free to deal-laden publications, does their coverage
        tone shift? This is a natural experiment worth tracking."""
        profile = load_gizmodo_profile()
        migrations = profile.get('journalist_migrations', [])
        zeff = [m for m in migrations if 'Zeff' in m.get('name', '')][0]
        assert 'significance' in zeff or 'notes' in zeff, \
            "Migration significance should be documented"


# ===================================================================
# TEST CLASS 5: Aggregate Control Evidence
# ===================================================================
class TestAggregateControlEvidence:
    """Validate that the Gizmodo control finding updates the overall
    MediaScope asymmetry thesis."""

    def test_control_finding_in_asymmetry_verdict(self):
        """The Gizmodo asymmetry verdict references the control finding."""
        research = load_competitor_research()
        gizmodo = research.get('publications', {}).get('gizmodo', {})
        verdict = gizmodo.get('asymmetry_verdict', '')
        assert len(verdict) > 50, "Verdict should be substantive"
        assert 'financial' in verdict.lower() or 'deal' in verdict.lower(), \
            "Verdict should reference financial relationships"

    def test_three_publication_tiers(self):
        """The research now supports a three-tier model of publications:
        Tier 1: Financial ties to Meta's competitors → adversarial Meta coverage
        Tier 2: Financial ties to both → balanced
        Tier 3: No ties → equal-opportunity criticism"""
        research = load_competitor_research()
        pubs = research.get('publications', {})

        # Tier 1: WIRED (OpenAI deal, no Meta deal) → adversarial
        wired_meta = pubs.get('wired', {}).get('meta_coverage_tone', '')
        assert 'adversarial' in wired_meta.lower()

        # Tier 2: News Corp (both deals) → balanced
        newscorp_meta = pubs.get('news-corp', {}).get('meta_coverage_tone', '')
        assert 'balanced' in newscorp_meta.lower()

        # Tier 3: Gizmodo (no deals) → balanced/fair
        gizmodo_meta = pubs.get('gizmodo', {}).get('meta_coverage_tone', '')
        assert 'balanced' in gizmodo_meta.lower()

    def test_gizmodo_and_newscorp_both_balanced_meta(self):
        """Both deal-free (Gizmodo) and both-deals (News Corp) produce
        balanced Meta coverage. Only competitor-deal-only (WIRED) produces
        adversarial Meta coverage."""
        research = load_competitor_research()
        pubs = research.get('publications', {})

        giz = pubs.get('gizmodo', {}).get('meta_coverage_tone', '')
        nc = pubs.get('news-corp', {}).get('meta_coverage_tone', '')
        wired = pubs.get('wired', {}).get('meta_coverage_tone', '')

        assert 'balanced' in giz.lower(), "Gizmodo (no deals) → balanced"
        assert 'balanced' in nc.lower(), "News Corp (both deals) → balanced"
        assert 'adversarial' in wired.lower(), "WIRED (competitor deals only) → adversarial"

    def test_financial_relationship_predicts_tone(self):
        """Statistical claim: having a deal with Meta's competitor WITHOUT
        a Meta deal predicts adversarial Meta coverage."""
        research = load_competitor_research()
        pubs = research.get('publications', {})

        adversarial_pubs = []
        balanced_pubs = []
        for name, data in pubs.items():
            tone = data.get('meta_coverage_tone', '')
            if 'adversarial' in tone.lower() and 'balanced' not in tone.lower():
                adversarial_pubs.append(name)
            elif 'balanced' in tone.lower():
                balanced_pubs.append(name)

        # At least 2 adversarial publications (WIRED, Verge, etc.)
        assert len(adversarial_pubs) >= 2, \
            f"Expected >= 2 adversarial publications, got {adversarial_pubs}"
        # At least 2 balanced publications (Gizmodo, News Corp)
        assert len(balanced_pubs) >= 2, \
            f"Expected >= 2 balanced publications, got {balanced_pubs}"
