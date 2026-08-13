"""
Multi-Journalist Samsung Unpacked Beat Assignment Paradox — Type B (Aug 13, 2026)

Mechanism #81: Coverage SELECTION Asymmetry Across Multiple Journalists at a
Single Event — Samsung Galaxy Unpacked (Jul 22, 2026, London)

KEY FINDING: At Samsung Galaxy Unpacked (Jul 22, 2026), publications with
financial dependency on Google/Samsung advertising sent multiple reporters
who published standalone foldable phone articles but ZERO standalone smart
glasses articles — despite Samsung's glasses using identical camera hardware
to Meta Ray-Ban (same Snapdragon AR1 Gen 1, 12MP camera, LED anti-tamper).

The Verge (Vox Media, Google programmatic ad dependency):
- David Imel: Fold 8 Ultra hands-on (standalone article)
- Dominic Preston: Fold 8 hands-on (standalone article)
  + pre-event analysis ("Samsung can't afford to play it safe")
- YouTube team: "Samsung Galaxy Unpacked in 15 minutes" — smart glasses
  get 67 seconds (13:53–15:00) out of a 15-minute video
- Samsung smart glasses standalone written article: ZERO

WIRED (Condé Nast, OpenAI/Amazon/Microsoft/Perplexity deals):
- Listed on Techmeme for Fold 8 Ultra coverage (Jul 22)
- Julian Chokkattu: ZERO Samsung glasses articles (documented: Mechanism #39)
- Samsung smart glasses standalone article: ZERO

Gizmodo (Keleops AG, ZERO financial ties to ANY tech company):
- Raymond Wong: Standalone Samsung glasses hands-on article
  + live blog with detailed glasses commentary
- Kyle Barr: Samsung glasses commentary in Unpacked live blog
- Matt Wille: Samsung glasses commentary in Unpacked live blog
- Samsung smart glasses standalone article: YES (multiple)

This is a SAME-EVENT NATURAL EXPERIMENT: all three publications sent
reporters to London for Galaxy Unpacked. Same press conference, same demo
area, same product availability. The variable is financial ties.

The paradox: The Verge and WIRED reporters were PHYSICALLY PRESENT with
Samsung's identical-to-Meta camera glasses, could have examined them,
and chose to write about foldable phones instead. Gizmodo reporters were
at the same event and chose to write about the glasses.

Prior Meta glasses coverage from the same reporters/publications:
- The Verge (Victoria Song): 3+ standalone Meta glasses privacy pieces
  (doxing story Oct 2024, LED tamper piece Jul 2026, bedroom question Jul 2025)
- WIRED (Chokkattu): Multiple standalone Meta glasses articles
  (subscription piece Jul 2026, Business Wars podcast episodes Jun 2026)

Samsung hardware parity:
- Same Snapdragon AR1 Gen 1 chip as Meta Ray-Ban
- Same 12MP camera resolution
- Same LED anti-tamper privacy feature
- Same audio-only (no display) form factor
- Same ~50g weight class
- Google Gemini AI (vs. Meta AI) — same capability class

Sources:
  - Techmeme river Jul 22, 2026 (David Imel/Verge, Dominic Preston/Verge,
    WIRED all listed for Fold 8 coverage):
    https://www.techmeme.com/260722/h1525 and https://www.techmeme.com/260722/h1610
  - The Verge YouTube "Samsung Galaxy Unpacked in 15 minutes" (glasses at 13:53):
    https://www.youtube.com/watch?v=c-MWq-DFTwo
  - Gizmodo Raymond Wong hands-on:
    https://gizmodo.com/samsung-let-me-touch-its-warby-parker-x-gentle-monster-smart-glasses-but-not-wear-them-2000788835
  - Gizmodo Live blog (Kyle Barr, Matt Wille, Raymond Wong):
    https://gizmodo.com/live-updates-from-samsungs-july-2026-galaxy-unpacked-2000785539
  - Cult of Mac recap citing Dominic Preston/Verge, Chris Welch/Bloomberg:
    https://www.cultofmac.com/news/samsung-galaxy-z-fold8-launch
  - Dominic Preston/Verge pre-event analysis (Daily Guardian syndication):
    https://dailyguardian.ca/samsung-cant-afford-to-play-it-safe-with-apples-first-foldable-looming/

Created: 2026-08-13
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(name):
    with open(os.path.join(PROFILES_DIR, name)) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def verge():
    return load_yaml('the-verge.yaml')


@pytest.fixture(scope='module')
def wired():
    return load_yaml('wired.yaml')


@pytest.fixture(scope='module')
def gizmodo():
    return load_yaml('gizmodo.yaml')


@pytest.fixture(scope='module')
def entities():
    return load_yaml('competitor-entities.yaml')


@pytest.fixture(scope='module')
def research():
    return load_yaml('competitor-coverage-research.yaml')


@pytest.fixture(scope='module')
def unpacked_gap(verge):
    cea = verge.get('cross_entity_coverage_analysis', {})
    section = cea.get('samsung_unpacked_beat_assignment_paradox')
    assert section is not None, (
        "the-verge.yaml cross_entity_coverage_analysis must have "
        "samsung_unpacked_beat_assignment_paradox section"
    )
    return section


# ── Class 1: Section Structure ──────────────────────────────────────


class TestSectionStructure:
    """Verify the YAML section exists and has required fields."""

    def test_section_exists(self, unpacked_gap):
        assert unpacked_gap is not None

    def test_has_event_info(self, unpacked_gap):
        assert unpacked_gap.get('event') is not None
        assert 'Galaxy Unpacked' in unpacked_gap['event']

    def test_has_event_date(self, unpacked_gap):
        assert unpacked_gap.get('date') == '2026-07-22'

    def test_has_event_location(self, unpacked_gap):
        assert 'London' in unpacked_gap.get('location', '')

    def test_has_reporters_present(self, unpacked_gap):
        reporters = unpacked_gap.get('reporters_present', [])
        assert len(reporters) >= 2, (
            f"Expected at least 2 Verge reporters at Unpacked, found {len(reporters)}"
        )

    def test_has_foldable_articles(self, unpacked_gap):
        articles = unpacked_gap.get('foldable_articles_published', [])
        assert len(articles) >= 2, (
            f"Expected at least 2 Verge foldable articles from Unpacked, "
            f"found {len(articles)}"
        )

    def test_has_glasses_article_count(self, unpacked_gap):
        count = unpacked_gap.get('standalone_glasses_articles_count', -1)
        assert count == 0, (
            f"The Verge published {count} standalone Samsung glasses articles "
            "from Unpacked. Expected 0."
        )


# ── Class 2: Reporter Coverage Choices ──────────────────────────────


class TestReporterCoverageChoices:
    """Track what each reporter chose to cover."""

    def test_david_imel_covered_foldable(self, unpacked_gap):
        reporters = unpacked_gap.get('reporters_present', [])
        imel = [r for r in reporters if 'Imel' in r.get('name', '')]
        assert len(imel) >= 1, "David Imel should be listed as present"
        imel = imel[0]
        articles = imel.get('articles_published', [])
        foldable = [a for a in articles if 'fold' in a.get('topic', '').lower()
                    or 'Fold' in a.get('title', '')]
        assert len(foldable) >= 1, (
            "David Imel published a Fold 8 Ultra hands-on but no glasses article"
        )

    def test_dominic_preston_covered_foldable(self, unpacked_gap):
        reporters = unpacked_gap.get('reporters_present', [])
        preston = [r for r in reporters if 'Preston' in r.get('name', '')]
        assert len(preston) >= 1, "Dominic Preston should be listed as present"
        preston = preston[0]
        articles = preston.get('articles_published', [])
        foldable = [a for a in articles if 'fold' in a.get('topic', '').lower()
                    or 'Fold' in a.get('title', '')]
        assert len(foldable) >= 1, (
            "Dominic Preston published a Fold 8 hands-on but no glasses article"
        )

    def test_no_reporter_published_glasses_article(self, unpacked_gap):
        reporters = unpacked_gap.get('reporters_present', [])
        for reporter in reporters:
            articles = reporter.get('articles_published', [])
            glasses = [a for a in articles if 'glass' in a.get('topic', '').lower()
                       or 'eyewear' in a.get('topic', '').lower()]
            assert len(glasses) == 0, (
                f"{reporter.get('name')} published a glasses article at Unpacked — "
                "expected zero from Verge reporters"
            )

    def test_youtube_video_glasses_timestamp(self, unpacked_gap):
        video = unpacked_gap.get('youtube_roundup_video', {})
        glasses_start = video.get('glasses_timestamp_seconds', 0)
        total_duration = video.get('total_duration_seconds', 1)
        glasses_fraction = glasses_start / total_duration if total_duration > 0 else 0
        assert glasses_fraction >= 0.9, (
            f"Glasses segment starts at {glasses_fraction:.0%} of video, "
            "confirming it was relegated to the last ~7% of the roundup"
        )

    def test_youtube_video_glasses_duration(self, unpacked_gap):
        video = unpacked_gap.get('youtube_roundup_video', {})
        duration = video.get('glasses_segment_seconds', 0)
        total = video.get('total_duration_seconds', 1)
        ratio = duration / total if total > 0 else 0
        assert ratio < 0.10, (
            f"Glasses got {ratio:.0%} of video time — confirms minimal coverage"
        )


# ── Class 3: Cross-Publication Comparison ───────────────────────────


class TestCrossPublicationComparison:
    """Compare coverage choices across publications at the same event."""

    def test_gizmodo_published_standalone_glasses(self, gizmodo):
        samsung_coverage = gizmodo.get('samsung_unpacked_glasses_coverage', {})
        articles = samsung_coverage.get('standalone_articles', [])
        assert len(articles) >= 1, (
            "Gizmodo (zero financial ties) should have published at least 1 "
            "standalone Samsung glasses article from Unpacked"
        )

    def test_gizmodo_multiple_reporters_covered_glasses(self, gizmodo):
        samsung_coverage = gizmodo.get('samsung_unpacked_glasses_coverage', {})
        reporters = samsung_coverage.get('reporters_covering_glasses', [])
        assert len(reporters) >= 2, (
            "Gizmodo had at least 3 reporters (Wong, Barr, Wille) covering "
            "Samsung glasses in standalone or live-blog format"
        )

    def test_verge_zero_glasses_vs_gizmodo(self, unpacked_gap, gizmodo):
        verge_count = unpacked_gap.get('standalone_glasses_articles_count', -1)
        gizmodo_count = len(
            gizmodo.get('samsung_unpacked_glasses_coverage', {})
            .get('standalone_articles', [])
        )
        assert verge_count == 0, "Verge published 0 standalone glasses articles"
        assert gizmodo_count >= 1, "Gizmodo published 1+ standalone glasses articles"

    def test_wired_zero_glasses_at_unpacked(self, wired):
        chokkattu = wired.get('chokkattu_samsung_coverage_selection_gap', {})
        gap_count = chokkattu.get('samsung_unpacked_glasses_articles', 0)
        assert gap_count == 0, (
            "WIRED (Condé Nast) published 0 standalone Samsung glasses articles "
            "from Unpacked, consistent with Mechanism #39"
        )


# ── Class 4: Hardware Parity Documentation ──────────────────────────


class TestHardwareParity:
    """Verify the documented hardware parity between Samsung and Meta glasses."""

    def test_same_chip(self, unpacked_gap):
        parity = unpacked_gap.get('hardware_parity', {})
        assert parity.get('chip') == 'Snapdragon AR1 Gen 1', (
            "Samsung uses the same Snapdragon AR1 Gen 1 as Meta Ray-Ban"
        )

    def test_same_camera_resolution(self, unpacked_gap):
        parity = unpacked_gap.get('hardware_parity', {})
        assert parity.get('camera_megapixels') == 12

    def test_same_led_tamper_feature(self, unpacked_gap):
        parity = unpacked_gap.get('hardware_parity', {})
        assert parity.get('led_anti_tamper') is True

    def test_same_form_factor(self, unpacked_gap):
        parity = unpacked_gap.get('hardware_parity', {})
        assert parity.get('display') is False, (
            "Both Samsung and Meta are audio-only, no-display form factor"
        )

    def test_ai_platform_parity(self, unpacked_gap):
        parity = unpacked_gap.get('hardware_parity', {})
        assert 'Gemini' in parity.get('ai_platform', ''), (
            "Samsung glasses use Google Gemini — same capability class as Meta AI"
        )


# ── Class 5: Financial Context ──────────────────────────────────────


class TestFinancialContext:
    """Verify the financial relationships that predict coverage selection."""

    def test_verge_google_ad_dependency_documented(self, unpacked_gap):
        financial = unpacked_gap.get('financial_context', {})
        verge = financial.get('the_verge', {})
        assert verge.get('google_ad_dependency') is True, (
            "Vox Media (The Verge) has Google programmatic ad dependency"
        )

    def test_wired_deal_portfolio_documented(self, unpacked_gap):
        financial = unpacked_gap.get('financial_context', {})
        wired = financial.get('wired', {})
        deals = wired.get('conde_nast_ai_deals', [])
        assert len(deals) >= 3, (
            "Condé Nast has deals with OpenAI, Amazon, Microsoft, Perplexity"
        )

    def test_gizmodo_zero_ties(self, unpacked_gap):
        financial = unpacked_gap.get('financial_context', {})
        gizmodo = financial.get('gizmodo', {})
        assert gizmodo.get('financial_ties_count') == 0, (
            "Gizmodo (Keleops AG) has zero financial ties to any tech company"
        )

    def test_samsung_is_major_advertiser(self, unpacked_gap):
        financial = unpacked_gap.get('financial_context', {})
        samsung = financial.get('samsung', {})
        assert samsung.get('global_ad_spend_billions') >= 9, (
            "Samsung is among the world's largest advertisers (~$9.7B/yr)"
        )


# ── Class 6: Prior Meta Coverage From Same Publications ─────────────


class TestPriorMetaCoverage:
    """Document that the SAME publications that skipped Samsung glasses
    produce extensive Meta glasses coverage."""

    def test_verge_has_meta_glasses_privacy_pieces(self, verge):
        journalists = verge.get('key_journalists', [])
        song = [j for j in journalists if j.get('name') == 'Victoria Song']
        assert len(song) >= 1, "Victoria Song should be in Verge profile"
        song = song[0]
        analysis = song.get('competitor_coverage_analysis', {})
        meta = analysis.get('meta_coverage', {})
        critical = meta.get('critical_pieces', [])
        assert len(critical) >= 2, (
            "Victoria Song has 2+ standalone Meta glasses privacy pieces — "
            "but zero standalone Samsung glasses articles from Unpacked"
        )

    def test_wired_has_meta_glasses_pieces(self, wired):
        chokkattu = wired.get('chokkattu_samsung_coverage_selection_gap', {})
        meta_articles = chokkattu.get('meta_articles_same_period', 0)
        assert meta_articles >= 3, (
            "Chokkattu published 3+ Meta glasses articles in the Jun-Jul window — "
            "but zero Samsung glasses articles from Unpacked"
        )


# ── Class 7: Mechanism Cross-References ─────────────────────────────


class TestMechanismCrossReferences:
    """Verify this mechanism connects to the right prior findings."""

    @pytest.fixture
    def m81(self, research):
        af = research.get('aggregate_findings', {})
        m = af.get('multi_journalist_samsung_unpacked_beat_assignment_paradox')
        assert m is not None, (
            "multi_journalist_samsung_unpacked_beat_assignment_paradox "
            "must exist in aggregate_findings"
        )
        return m

    def test_mechanism_id(self, m81):
        assert m81.get('mechanism_id') == 81

    def test_has_test_file(self, m81):
        tf = m81.get('test_file', '')
        assert 'multi_journalist_samsung_unpacked_beat_assignment_aug13' in tf

    def test_references_chokkattu_gap(self, m81):
        refs = m81.get('related_mechanisms', [])
        assert 39 in refs, "Should reference Mechanism #39 (Chokkattu Samsung gap)"

    def test_references_song_bifurcation(self, m81):
        refs = m81.get('related_mechanisms', [])
        assert 75 in refs, "Should reference Mechanism #75 (Song privacy bifurcation)"

    def test_references_gizmodo_control(self, m81):
        refs = m81.get('related_mechanisms', [])
        assert 80 in refs, "Should reference Mechanism #80 (Gizmodo 4-entity control)"

    def test_references_nyt_samsung_silence(self, m81):
        refs = m81.get('related_mechanisms', [])
        assert 77 in refs, "Should reference Mechanism #77 (NYT Samsung silence)"


# ── Class 8: Confounding Factors ────────────────────────────────────


class TestConfoundingFactors:
    """Verify confounding factors are documented with appropriate strengths."""

    @pytest.fixture
    def m81(self, research):
        af = research.get('aggregate_findings', {})
        return af.get('multi_journalist_samsung_unpacked_beat_assignment_paradox', {})

    def test_has_confounding_factors(self, m81):
        factors = m81.get('confounding_factors', [])
        assert len(factors) >= 5, (
            f"Found {len(factors)} confounding factors, expected >= 5"
        )

    def test_has_strong_factor(self, m81):
        factors = m81.get('confounding_factors', [])
        strong = [f for f in factors if f.get('strength') == 'STRONG']
        assert len(strong) >= 2, "Should have at least 2 STRONG confounding factors"

    @pytest.mark.parametrize("expected_topic", [
        "pre-launch timing",
        "editorial priority",
        "beat assignment",
    ])
    def test_key_confounding_topics_present(self, m81, expected_topic):
        factors = m81.get('confounding_factors', [])
        labels = [f.get('factor', '').lower() for f in factors]
        found = any(expected_topic.lower() in label for label in labels)
        assert found, (
            f"Confounding factor '{expected_topic}' not found in {labels}"
        )


# ── Class 9: Testable Predictions ───────────────────────────────────


class TestTestablePredictions:
    """Verify testable predictions are documented."""

    @pytest.fixture
    def m81(self, research):
        af = research.get('aggregate_findings', {})
        return af.get('multi_journalist_samsung_unpacked_beat_assignment_paradox', {})

    def test_has_predictions(self, m81):
        predictions = m81.get('testable_predictions', [])
        assert len(predictions) >= 3, (
            f"Found {len(predictions)} predictions, expected >= 3"
        )

    @pytest.mark.parametrize("keyword", [
        "Samsung",
        "review",
        "privacy",
    ])
    def test_predictions_cover_key_scenarios(self, m81, keyword):
        predictions = m81.get('testable_predictions', [])
        texts = ' '.join(p.get('prediction', '') for p in predictions)
        assert keyword.lower() in texts.lower(), (
            f"Predictions should reference '{keyword}'"
        )
