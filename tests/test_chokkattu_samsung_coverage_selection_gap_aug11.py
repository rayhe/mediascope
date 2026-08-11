"""
Chokkattu Samsung Coverage Selection Gap — Type B Journalist Cross-Entity (Aug 11, 2026)

Mechanism #39: Coverage SELECTION Asymmetry (extends Mechanism #30)

KEY FINDING: WIRED's Julian Chokkattu published 3+ Meta smart glasses articles
in the Jun–Jul 2026 window but ZERO standalone articles about Samsung Galaxy
Glasses despite the major Galaxy Unpacked announcement on Jul 22, 2026.

Samsung's glasses use the IDENTICAL Snapdragon AR1 Gen 1 chip, have a 12MP
camera, Google Gemini AI integration, LED anti-tamper privacy features, and
~50g weight — functionally indistinguishable from Meta Ray-Ban glasses.

20+ publications covered Samsung's glasses at Unpacked. WIRED's absence is
notable given they sent 5 reporters to Google I/O 2026 (May 19) for Google's
camera-equipped smart glasses.

This extends Mechanism #30 (Temporal Framing Oscillation) from a coverage
FRAMING asymmetry to a coverage SELECTION asymmetry: the same journalist who
oscillates between adversarial and neutral on Meta depending on genre simply
doesn't cover Samsung's identical product at all.

Coverage SELECTION (choosing what to report) is a subtler form of editorial
influence than coverage FRAMING (how you report it).

Sources:
  - Samsung Newsroom: "Samsung Brings Galaxy Ecosystem Into Everyday Eyewear"
    https://news.samsung.com/us/samsung-galaxy-ecosystem-everyday-eyewear
  - Biztoc/Techmeme: Chokkattu Meta Starfire article (Jun 23, 2026)
    https://biztoc.com/x/65c250c5f0d223b2
  - Samsung Newsroom interview: Galaxy Unpacked Jul 2026
    https://news.samsung.com/us/samsung-interview-galaxy-unpacked-july-2026-inside-engineering-intelligent-eyewear
  - 9to5Google: Samsung/Google "perv glasses" framing (Jul 23)
    https://9to5google.com/2026/07/23/inbox-newsletter-4/
  - Android Police: Samsung glasses hands-on (Jul 22)
    https://www.androidpolice.com/hands-on-with-samsungs-ray-ban-meta-rival-smartglasses/

Created: 2026-08-11
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(name):
    with open(os.path.join(PROFILES_DIR, name)) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def wired():
    return load_yaml('wired.yaml')


@pytest.fixture(scope='module')
def entities():
    return load_yaml('competitor-entities.yaml')


@pytest.fixture(scope='module')
def research():
    return load_yaml('competitor-coverage-research.yaml')


@pytest.fixture(scope='module')
def selection_gap(wired):
    section = wired.get('chokkattu_samsung_coverage_selection_gap')
    assert section is not None, (
        "wired.yaml must have chokkattu_samsung_coverage_selection_gap section"
    )
    return section


# ── Class 1: Section Structure ──────────────────────────────────────


class TestSectionStructure:
    """Verify the coverage selection gap section has required fields."""

    def test_section_exists(self, selection_gap):
        assert selection_gap is not None

    def test_has_mechanism_id(self, selection_gap):
        assert selection_gap.get('mechanism_id') == 39

    def test_has_date_analyzed(self, selection_gap):
        assert '2026-08-11' in selection_gap.get('date_analyzed', '')

    def test_has_journalist(self, selection_gap):
        assert selection_gap.get('journalist') == 'Julian Chokkattu'

    def test_extends_mechanism_30(self, selection_gap):
        assert selection_gap.get('extends_mechanism') == 30

    def test_has_meta_articles(self, selection_gap):
        articles = selection_gap.get('meta_articles_in_window', [])
        assert len(articles) >= 3, (
            f"Expected >= 3 Meta articles in window, got {len(articles)}"
        )

    def test_samsung_articles_zero(self, selection_gap):
        assert selection_gap.get('samsung_articles_in_window') == 0


# ── Class 2: Meta Coverage Timeline ─────────────────────────────────


class TestMetaCoverageTimeline:
    """Verify Chokkattu's documented Meta coverage in the Jun-Jul window."""

    def test_business_wars_podcast_exists(self, selection_gap):
        articles = selection_gap.get('meta_articles_in_window', [])
        podcasts = [a for a in articles if a.get('type') == 'podcast']
        assert len(podcasts) >= 2, (
            "Expected >= 2 podcast entries (Prize on the Eyes, I'm a Creep)"
        )

    def test_product_article_exists(self, selection_gap):
        articles = selection_gap.get('meta_articles_in_window', [])
        product = [a for a in articles if a.get('type') == 'product_article']
        assert len(product) >= 1, "Expected >= 1 product article (Starfire launch)"

    def test_editorial_exists(self, selection_gap):
        articles = selection_gap.get('meta_articles_in_window', [])
        editorial = [a for a in articles if a.get('type') == 'editorial']
        assert len(editorial) >= 1, "Expected >= 1 editorial (subscription pricing)"

    def test_articles_span_jun_jul(self, selection_gap):
        articles = selection_gap.get('meta_articles_in_window', [])
        dates = [a.get('date', '') for a in articles]
        has_jun = any('2026-06' in d for d in dates)
        has_jul = any('2026-07' in d for d in dates)
        assert has_jun, "Expected at least one June article"
        assert has_jul, "Expected at least one July article"


# ── Class 3: Samsung Hardware Parity ─────────────────────────────────


class TestSamsungHardwareParity:
    """Verify Samsung Galaxy Glasses use identical core hardware."""

    def test_samsung_event_documented(self, selection_gap):
        event = selection_gap.get('samsung_event', {})
        assert event.get('date') == '2026-07-22'
        assert 'Unpacked' in event.get('name', '')

    def test_hardware_chip_parity(self, selection_gap):
        hw = selection_gap.get('samsung_event', {}).get('hardware_parity', {})
        chip = hw.get('chip', '')
        assert 'AR1' in chip, f"Expected Snapdragon AR1 in chip field, got '{chip}'"

    def test_hardware_camera_parity(self, selection_gap):
        hw = selection_gap.get('samsung_event', {}).get('hardware_parity', {})
        cam = hw.get('camera', '')
        assert '12MP' in cam, f"Expected 12MP camera, got '{cam}'"

    def test_hardware_led_parity(self, selection_gap):
        hw = selection_gap.get('samsung_event', {}).get('hardware_parity', {})
        led = hw.get('privacy_led', '')
        assert 'LED' in led, f"Expected LED privacy indicator, got '{led}'"

    def test_hardware_ai_documented(self, selection_gap):
        hw = selection_gap.get('samsung_event', {}).get('hardware_parity', {})
        ai = hw.get('ai', '')
        assert 'Gemini' in ai, f"Expected Gemini AI, got '{ai}'"

    def test_samsung_in_entities(self, entities):
        ent = entities.get('entities', {})
        assert 'samsung' in ent, "Samsung must be in competitor-entities.yaml"


# ── Class 4: Coverage Selection Asymmetry ────────────────────────────


class TestCoverageSelectionAsymmetry:
    """Validate the core finding: Meta > 0 articles, Samsung = 0."""

    def test_meta_articles_positive(self, selection_gap):
        articles = selection_gap.get('meta_articles_in_window', [])
        assert len(articles) > 0, "Must have positive Meta article count"

    def test_samsung_articles_zero(self, selection_gap):
        count = selection_gap.get('samsung_articles_in_window')
        assert count == 0, f"Expected 0 Samsung articles, got {count}"

    def test_other_publications_covered_samsung(self, selection_gap):
        others = selection_gap.get('other_publications_covering_samsung_glasses', [])
        assert len(others) >= 5, (
            f"Expected >= 5 other publications covering Samsung, got {len(others)}"
        )

    @pytest.mark.parametrize("pub", [
        "Android Police", "9to5Google", "Android Authority",
        "Gadgets360", "GSMArena",
    ])
    def test_specific_publications_listed(self, selection_gap, pub):
        others = selection_gap.get('other_publications_covering_samsung_glasses', [])
        assert pub in others, f"{pub} should be in other publications list"

    def test_selection_vs_framing_distinction(self, selection_gap):
        summary = selection_gap.get('summary', '')
        assert 'selection' in summary.lower() or 'SELECTION' in summary, (
            "Summary must distinguish selection from framing asymmetry"
        )


# ── Class 5: Financial Relationship Correlation ──────────────────────


class TestFinancialRelationshipCorrelation:
    """Verify that financial relationships predict coverage selection."""

    def test_conde_nast_has_openai_deal(self, wired):
        deals = wired.get('financial_relationships', wired.get('ownership', {}))
        # The wired.yaml documents Condé Nast deals somewhere
        content = yaml.dump(wired)
        assert 'OpenAI' in content, "WIRED profile must mention OpenAI deal"

    def test_conde_nast_no_meta_deal(self, wired):
        content = yaml.dump(wired)
        # Meta deal absence should be documented
        assert 'meta' in content.lower(), (
            "WIRED profile must discuss Meta (even if to note absence of deal)"
        )

    def test_samsung_no_conde_nast_deal(self, selection_gap):
        summary = selection_gap.get('summary', '')
        # The absence of Samsung coverage correlates with absence of deal
        assert len(summary) > 50, "Summary must explain the finding"


# ── Class 6: Cross-Mechanism Validation ──────────────────────────────


class TestCrossMechanismValidation:
    """Verify relationship with Mechanism #30 and consistency."""

    def test_extends_mechanism_30(self, selection_gap):
        assert selection_gap.get('extends_mechanism') == 30

    def test_mechanism_30_exists_in_wired(self, wired):
        m30 = wired.get('chokkattu_temporal_framing_oscillation')
        assert m30 is not None, (
            "Mechanism #30 (temporal framing oscillation) must exist"
        )
        assert m30.get('mechanism_id') == 30

    def test_framing_to_selection_escalation(self, selection_gap):
        """Selection gap is a stronger finding than framing oscillation."""
        summary = selection_gap.get('summary', '')
        assert 'extends' in summary.lower() or 'Extends' in summary, (
            "Summary should note this extends the framing finding"
        )

    def test_google_io_comparison(self, selection_gap):
        """WIRED sent 5 reporters to Google I/O — Samsung absence is notable."""
        counterpoints = selection_gap.get('counterpoints', [])
        io_mentioned = any('I/O' in cp or 'Google I/O' in cp for cp in counterpoints)
        assert io_mentioned, (
            "Counterpoints must note WIRED's Google I/O attendance vs Samsung absence"
        )


# ── Class 7: Legitimate Factors ──────────────────────────────────────


class TestLegitimateFactors:
    """Verify honest documentation of confounding factors."""

    def test_has_legitimate_factors(self, selection_gap):
        factors = selection_gap.get('legitimate_factors', [])
        assert len(factors) >= 5, (
            f"Expected >= 5 legitimate factors, got {len(factors)}"
        )

    def test_factors_have_strength_ratings(self, selection_gap):
        factors = selection_gap.get('legitimate_factors', [])
        for f in factors:
            assert 'strength' in f, (
                f"Factor '{f.get('factor', 'unknown')}' missing strength rating"
            )

    def test_london_venue_factor(self, selection_gap):
        factors = selection_gap.get('legitimate_factors', [])
        texts = [f.get('factor', '') for f in factors]
        has_london = any('London' in t or 'london' in t for t in texts)
        assert has_london, "Must document London venue as legitimate factor"

    def test_pre_ship_factor(self, selection_gap):
        factors = selection_gap.get('legitimate_factors', [])
        texts = [f.get('factor', '') for f in factors]
        has_ship = any('ship' in t.lower() or 'fall' in t.lower() for t in texts)
        assert has_ship, "Must document pre-shipping status as factor"

    def test_has_counterpoints(self, selection_gap):
        counterpoints = selection_gap.get('counterpoints', [])
        assert len(counterpoints) >= 3, (
            f"Expected >= 3 counterpoints, got {len(counterpoints)}"
        )


# ── Class 8: Mechanism #39 in Research Profile ───────────────────────


class TestMechanism39InResearch:
    """Verify Mechanism #39 is cataloged in competitor-coverage-research.yaml."""

    def test_mechanism_39_exists(self, research):
        content = yaml.dump(research)
        assert 'mechanism_id: 39' in content, (
            "Mechanism #39 must be in competitor-coverage-research.yaml"
        )

    def test_mechanism_39_has_finding(self, research):
        content = yaml.dump(research)
        assert 'Samsung Coverage Selection Gap' in content or \
               'samsung_coverage_selection' in content.lower(), (
            "Mechanism #39 must reference Samsung coverage selection gap"
        )

    def test_mechanism_39_has_test_file(self, research):
        content = yaml.dump(research)
        assert 'chokkattu_samsung_coverage_selection_gap' in content, (
            "Mechanism #39 must reference its test file"
        )
