"""
Ashworth WWDC PCC Privacy Framing Asymmetry — Type B Journalist Cross-Entity (Aug 11, 2026)

Mechanism #45: Journalist-Level Privacy Framing Asymmetry

KEY FINDING: WIRED's Boone Ashworth co-hosted 3 Business Wars podcast episodes
(Jun 3-11, 2026) where Meta's glasses were called "a tool for mass surveillance"
(Ep 1, Jun 3) and the episode was titled "I'm a Creep" (Ep 2, Jun 10). Between
those two episodes, on Jun 8, Ashworth authored WIRED's "Everything Apple Announced
at WWDC 2026" — covering Apple's announcement that PCC would expand to Google Cloud
with Nvidia GPUs. His framing: "some inkling on how an AI partnership with Google has
come to power Apple's products." Zero privacy scrutiny. Zero investigative language.

This is the cleanest journalist-level natural experiment in the MediaScope dataset:
same reporter, same 8-day window, differential privacy framing for different companies.

This is a journalist-level confirmation of Mechanism #44 (publication-level PCC coverage
selection asymmetry): the same individual reporter who applies "mass surveillance"
language to Meta's 1-camera glasses applies "partnership" language to Apple's
fundamental privacy architecture change.

Ashworth's broader wearables coverage confirms the pattern: Xreal xbx ($299,
Jun 11) gets "Channel Xbox Vibes," TranscribeGlass ($377, Jul 3) gets positive
accessibility framing, clip-on frames (Jul 22) get "mainstream" — none receive
surveillance language. Only Meta triggers adversarial vocabulary.

Sources:
  - Feedcast: Ashworth WWDC roundup (Jun 8, 2026)
    https://www.feedcast.news/everything-apple-announced-at-wwdc-2026-3wpswv
  - Prowly: Ashworth recent articles listing
    https://prowly.com/profiles/journalists/boone-ashworth
  - Business Wars: podcasts-online listing
    https://www.podcasts-online.org/pt/business-wars-1335814741
  - Techmeme: TranscribeGlass coverage (Jul 3)
    https://www.techmeme.com/250703/p4
  - Neowin: Apple PCC expansion to Google Cloud (Jun 9)
    https://www.neowin.net/news/apple-is-expanding-private-cloud-compute-beyond-its-own-data-centers/
  - WebProNews: Apple PCC scrutiny (Jul 2026)
    https://www.webpronews.com/apples-private-cloud-compute-faces-scrutiny-as-it-expands-beyond-its-own-servers/

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
def research():
    return load_yaml('competitor-coverage-research.yaml')


@pytest.fixture(scope='module')
def ashworth_section(wired):
    section = wired.get('ashworth_wwdc_pcc_privacy_framing_asymmetry')
    assert section is not None, (
        "wired.yaml must have ashworth_wwdc_pcc_privacy_framing_asymmetry section"
    )
    return section


@pytest.fixture(scope='module')
def cpf_mechanism(research):
    cpf = research.get('cross_publication_findings', {})
    section = cpf.get('ashworth_wwdc_pcc_privacy_framing_asymmetry')
    assert section is not None, (
        "competitor-coverage-research.yaml cross_publication_findings must have "
        "ashworth_wwdc_pcc_privacy_framing_asymmetry"
    )
    return section


# ── Class 1: Section Structure ──────────────────────────────────────


class TestSectionStructure:
    """Verify the wired.yaml section has all required fields."""

    def test_section_exists(self, ashworth_section):
        assert ashworth_section is not None

    def test_mechanism_id_is_45(self, ashworth_section):
        assert ashworth_section.get('mechanism_id') == 45

    def test_journalist_is_ashworth(self, ashworth_section):
        assert ashworth_section.get('journalist') == 'Boone Ashworth'

    def test_publication_is_wired(self, ashworth_section):
        assert ashworth_section.get('publication') == 'WIRED'

    def test_analysis_date(self, ashworth_section):
        assert '2026-08-11' in ashworth_section.get('analysis_date', '')

    def test_finding_type(self, ashworth_section):
        assert ashworth_section.get('finding_type') == 'journalist_cross_entity_privacy_framing'

    def test_extends_mechanism_44(self, ashworth_section):
        extends = ashworth_section.get('extends_mechanisms', [])
        assert 44 in extends, "Must extend Mechanism #44 (PCC coverage asymmetry)"

    def test_extends_mechanism_14(self, ashworth_section):
        extends = ashworth_section.get('extends_mechanisms', [])
        assert 14 in extends, "Must extend Mechanism #14 (Barrett Crisis/Makeover)"


# ── Class 2: Timeline Verification ─────────────────────────────────


class TestTimeline:
    """Verify the 8-day window timeline is documented correctly."""

    def test_has_timeline(self, ashworth_section):
        timeline = ashworth_section.get('timeline', [])
        assert len(timeline) >= 3, "Must have at least 3 timeline events"

    def test_first_event_is_meta_podcast(self, ashworth_section):
        timeline = ashworth_section.get('timeline', [])
        first = timeline[0]
        assert first['date'] == '2026-06-03'
        assert 'Meta' in first.get('subject', '')

    def test_second_event_is_apple_wwdc(self, ashworth_section):
        timeline = ashworth_section.get('timeline', [])
        second = timeline[1]
        assert second['date'] == '2026-06-08'
        assert 'Apple' in second.get('subject', '')

    def test_third_event_is_meta_creep(self, ashworth_section):
        timeline = ashworth_section.get('timeline', [])
        third = timeline[2]
        assert third['date'] == '2026-06-10'
        assert 'Meta' in third.get('subject', '')

    def test_meta_tones_are_negative(self, ashworth_section):
        timeline = ashworth_section.get('timeline', [])
        meta_events = [e for e in timeline if 'Meta' in e.get('subject', '')]
        for event in meta_events:
            assert event.get('tone', 0) < -0.5, (
                f"Meta event '{event.get('event')}' should have tone < -0.5, "
                f"got {event.get('tone')}"
            )

    def test_apple_tone_is_neutral_to_positive(self, ashworth_section):
        timeline = ashworth_section.get('timeline', [])
        apple_events = [e for e in timeline if 'Apple' in e.get('subject', '')]
        for event in apple_events:
            assert event.get('tone', 0) >= 0, (
                f"Apple event '{event.get('event')}' should have tone >= 0, "
                f"got {event.get('tone')}"
            )


# ── Class 3: Framing Vocabulary Comparison ──────────────────────────


class TestFramingVocabulary:
    """The same journalist uses surveillance language for Meta, partnership for Apple."""

    def test_meta_framing_uses_surveillance(self, ashworth_section):
        timeline = ashworth_section.get('timeline', [])
        meta_events = [e for e in timeline if 'Meta' in e.get('subject', '')]
        all_framing = ' '.join(e.get('framing', '') for e in meta_events).lower()
        assert 'surveillance' in all_framing or 'mass surveillance' in all_framing, (
            "Meta framing must include 'surveillance' language"
        )

    def test_apple_framing_uses_partnership(self, ashworth_section):
        timeline = ashworth_section.get('timeline', [])
        apple_events = [e for e in timeline if 'Apple' in e.get('subject', '')]
        all_framing = ' '.join(e.get('framing', '') for e in apple_events).lower()
        assert 'partnership' in all_framing, (
            "Apple framing must include 'partnership' language"
        )

    def test_apple_framing_excludes_surveillance(self, ashworth_section):
        timeline = ashworth_section.get('timeline', [])
        apple_events = [e for e in timeline if 'Apple' in e.get('subject', '')]
        all_framing = ' '.join(e.get('framing', '') for e in apple_events).lower()
        assert 'surveillance' not in all_framing, (
            "Apple PCC framing must NOT include 'surveillance' language"
        )


# ── Class 4: Tone Delta ────────────────────────────────────────────


class TestToneDelta:
    """Verify the tone swing is documented and significant."""

    def test_tone_delta_documented(self, ashworth_section):
        delta = ashworth_section.get('tone_delta', 0)
        assert delta >= 0.8, (
            f"Tone delta should be >= 0.8 (Meta adversarial vs Apple neutral), "
            f"got {delta}"
        )

    def test_window_days(self, ashworth_section):
        window = ashworth_section.get('window_days', 0)
        assert window <= 10, f"Window should be <= 10 days, got {window}"
        assert window >= 5, f"Window should be >= 5 days, got {window}"


# ── Class 5: PCC Privacy Shift Details ──────────────────────────────


class TestPCCPrivacyShift:
    """Wired.yaml must document the PCC architectural change Ashworth omitted."""

    def test_pcc_section_exists(self, ashworth_section):
        pcc = ashworth_section.get('pcc_privacy_shift')
        assert pcc is not None, "Must document the PCC privacy shift Ashworth omitted"

    def test_pcc_privacy_implications(self, ashworth_section):
        pcc = ashworth_section.get('pcc_privacy_shift', {})
        implications = pcc.get('privacy_implications', [])
        assert len(implications) >= 3, (
            f"Must list at least 3 privacy implications, got {len(implications)}"
        )

    def test_pcc_ashworth_coverage_documented(self, ashworth_section):
        pcc = ashworth_section.get('pcc_privacy_shift', {})
        coverage = pcc.get('ashworth_coverage_of_shift', '')
        assert len(coverage) > 50, "Must document what Ashworth actually wrote about PCC"

    def test_pcc_zero_privacy_language(self, ashworth_section):
        pcc = ashworth_section.get('pcc_privacy_shift', {})
        assert pcc.get('pcc_privacy_concerns_raised') is False or (
            'zero' in pcc.get('ashworth_coverage_of_shift', '').lower()
        ), "Must confirm zero privacy concerns in Ashworth's WWDC coverage"


# ── Class 6: Broader Wearables Pattern ──────────────────────────────


class TestBroaderWearablesPattern:
    """Ashworth's other wearables coverage confirms the pattern."""

    def test_broader_coverage_exists(self, ashworth_section):
        broader = ashworth_section.get('ashworth_broader_wearables_coverage', {})
        articles = broader.get('articles', [])
        assert len(articles) >= 2, (
            f"Must document at least 2 broader wearables articles, got {len(articles)}"
        )

    def test_competitor_coverage_no_surveillance(self, ashworth_section):
        broader = ashworth_section.get('ashworth_broader_wearables_coverage', {})
        articles = broader.get('articles', [])
        for article in articles:
            assert article.get('surveillance_language') is False, (
                f"Article '{article.get('title')}' should have no surveillance language"
            )

    def test_competitor_tones_positive(self, ashworth_section):
        broader = ashworth_section.get('ashworth_broader_wearables_coverage', {})
        articles = broader.get('articles', [])
        for article in articles:
            tone = article.get('tone', 0)
            assert tone >= 0, (
                f"Article '{article.get('title')}' tone should be >= 0, got {tone}"
            )

    def test_xreal_coverage_positive(self, ashworth_section):
        broader = ashworth_section.get('ashworth_broader_wearables_coverage', {})
        articles = broader.get('articles', [])
        xreal = [a for a in articles if 'xreal' in a.get('subject', '').lower()
                 or 'Xreal' in a.get('subject', '')]
        assert len(xreal) >= 1, "Must document Xreal coverage"
        assert xreal[0].get('tone', 0) > 0, "Xreal tone should be positive"


# ── Class 7: Tone Comparison ────────────────────────────────────────


class TestToneComparison:
    """Verify the full tone comparison data."""

    def test_tone_comparison_exists(self, ashworth_section):
        tc = ashworth_section.get('tone_comparison')
        assert tc is not None, "Must have tone_comparison section"

    def test_meta_tone_strongly_negative(self, ashworth_section):
        tc = ashworth_section.get('tone_comparison', {})
        meta_tone = tc.get('meta_glasses_tone', 0)
        assert meta_tone <= -0.5, f"Meta tone should be <= -0.5, got {meta_tone}"

    def test_apple_tone_neutral_to_positive(self, ashworth_section):
        tc = ashworth_section.get('tone_comparison', {})
        apple_tone = tc.get('apple_pcc_shift_tone', 0)
        assert apple_tone >= -0.1, f"Apple tone should be >= -0.1, got {apple_tone}"

    def test_meta_vocabulary_has_surveillance(self, ashworth_section):
        tc = ashworth_section.get('tone_comparison', {})
        vocab = tc.get('meta_framing_vocabulary', [])
        assert any('surveillance' in v.lower() for v in vocab), (
            "Meta vocabulary must include surveillance"
        )

    def test_apple_vocabulary_has_partnership(self, ashworth_section):
        tc = ashworth_section.get('tone_comparison', {})
        vocab = tc.get('apple_framing_vocabulary', [])
        assert any('partnership' in v.lower() for v in vocab), (
            "Apple vocabulary must include partnership"
        )

    def test_tone_delta_large(self, ashworth_section):
        tc = ashworth_section.get('tone_comparison', {})
        delta = tc.get('tone_delta_meta_vs_apple', 0)
        assert delta >= 0.8, f"Meta-vs-Apple tone delta should be >= 0.8, got {delta}"


# ── Class 8: Cross-Publication Findings Entry ───────────────────────


class TestCPFEntry:
    """Verify mechanism #45 exists in competitor-coverage-research.yaml."""

    def test_cpf_mechanism_id(self, cpf_mechanism):
        assert cpf_mechanism.get('mechanism_id') == 45

    def test_cpf_journalist(self, cpf_mechanism):
        assert cpf_mechanism.get('journalist') == 'Boone Ashworth'

    def test_cpf_extends_44(self, cpf_mechanism):
        extends = cpf_mechanism.get('extends_mechanisms', [])
        assert 44 in extends

    def test_cpf_rotation_type(self, cpf_mechanism):
        assert cpf_mechanism.get('rotation_type') == 'B'

    def test_cpf_has_source_urls(self, cpf_mechanism):
        urls = cpf_mechanism.get('source_urls', [])
        assert len(urls) >= 3, f"Must have at least 3 source URLs, got {len(urls)}"

    def test_cpf_has_timeline(self, cpf_mechanism):
        timeline = cpf_mechanism.get('timeline', [])
        assert len(timeline) >= 3


# ── Class 9: Cross-References ──────────────────────────────────────


class TestCrossReferences:
    """Verify mechanism is properly linked to related mechanisms."""

    def test_has_cross_references(self, ashworth_section):
        refs = ashworth_section.get('cross_references', [])
        assert len(refs) >= 3, f"Must have at least 3 cross references, got {len(refs)}"

    def test_references_mechanism_44(self, ashworth_section):
        refs = ashworth_section.get('cross_references', [])
        text = ' '.join(refs)
        assert '44' in text, "Must reference Mechanism #44"

    def test_references_mechanism_42(self, ashworth_section):
        refs = ashworth_section.get('cross_references', [])
        text = ' '.join(refs)
        assert '42' in text, "Must reference Mechanism #42"

    def test_references_chokkattu_ashworth_test(self, ashworth_section):
        refs = ashworth_section.get('cross_references', [])
        text = ' '.join(refs)
        assert 'chokkattu_ashworth' in text.lower(), (
            "Must reference the existing chokkattu_ashworth cross-entity test"
        )


# ── Class 10: Legitimate Factors ────────────────────────────────────


class TestLegitimateFactors:
    """Verify legitimate counterarguments are documented."""

    def test_has_legitimate_factors(self, ashworth_section):
        factors = ashworth_section.get('legitimate_factors', [])
        assert len(factors) >= 2, f"Must have at least 2 legitimate factors, got {len(factors)}"

    def test_format_difference_acknowledged(self, ashworth_section):
        factors = ashworth_section.get('legitimate_factors', [])
        text = ' '.join(f.get('description', '') if isinstance(f, dict) else str(f)
                        for f in factors).lower()
        assert 'podcast' in text or 'format' in text, (
            "Must acknowledge podcast vs article format difference"
        )

    def test_wwdc_scope_acknowledged(self, ashworth_section):
        factors = ashworth_section.get('legitimate_factors', [])
        text = ' '.join(f.get('description', '') if isinstance(f, dict) else str(f)
                        for f in factors).lower()
        assert 'wwdc' in text or 'roundup' in text or 'compress' in text, (
            "Must acknowledge WWDC roundup scope limitations"
        )
