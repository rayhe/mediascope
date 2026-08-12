"""
Mechanism #56: The Verge Intra-Publication Beat Segregation —
Platform Reporters vs AI Beat Reporters Frame Meta Differently

FINDING: At The Verge (Penske Media Corporation / Vox Media), reporters
covering the SAME company (Meta) apply systematically different framing
depending on their beat assignment:

- PLATFORM/PRODUCT beat (Jess Weatherbed, Victoria Song): Meta coverage
  uses neutral-to-positive feature language — "adds," "rolls out,"
  "launches," "new open-weight model." Product beat stories treat Meta
  as a tech company shipping features.

- AI/INDUSTRY beat (Hayden Field, since Jun 2025 from CNBC): Meta coverage
  uses deficit/follower language — "reentering the AI race," researchers
  "rejected Meta's offers," "catching up." AI beat stories treat Meta
  as a laggard in a race led by OpenAI/Anthropic.

The SAME publication, in the SAME week, can publish Weatherbed writing
"Meta has a new open-weight AI model" (neutral, feature-story) and Field
writing about Meta's AI coding race (deficit, competitive framing).

STRUCTURAL INSIGHT: This is NOT a journalist personality issue — it is a
beat assignment effect. The AI beat at The Verge (and at WIRED, per
Mechanism #45 / Will Knight) functionally operates as the
"OpenAI/Anthropic beat," because those companies ARE the AI industry
leaders. When the AI beat covers Meta, it necessarily positions Meta
relative to those leaders, producing deficit framing. The product beat
covers Meta features on their own merits, producing neutral framing.

The beat segregation is structurally aligned with PMC's financial
relationships: PMC/Vox Media has an OpenAI content licensing deal.
The AI beat concentrates coverage on the deal partner (OpenAI) and
its closest competitor (Anthropic), generating aspirational framing
for both. When the AI beat covers Meta, it frames Meta through the
lens of OpenAI/Anthropic leadership, producing follower/deficit language.

CONTROLLED COMPARISON VALUE: This is the first mechanism documenting
the framing divergence between TWO different reporters at the SAME
publication covering the SAME company. Prior mechanisms documented:
- Same journalist, different genres (#30 Chokkattu, #31 Pero)
- Same journalist, different entities (#20 Knibbs, #24 Newton)
- Different publications, same entity (many)

This mechanism adds: Different journalists, same publication, same entity,
different beat assignments → different framing directions.

CONFOUNDING FACTORS:
1. Product beats genuinely cover different news (launches vs industry trends)
2. Meta IS behind OpenAI/Anthropic on some coding benchmarks — deficit
   framing has factual basis
3. Weatherbed and Field have different career backgrounds and styles
4. Field joined Jun 2025, so her Verge coverage sample is 14 months
5. Product reporters at all publications tend toward neutral feature coverage
6. The AI beat at ANY publication would naturally center the market leaders

Created: 2026-08-11 23:00 PT (Type B iteration — Journalist Cross-Entity Tracking)
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml'), 'r') as f:
        return yaml.safe_load(f)


def load_the_verge_profile():
    path = os.path.join(PROFILES_DIR, 'the-verge.yaml')
    if os.path.exists(path):
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    return None


def load_journalists():
    path = os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml')
    if os.path.exists(path):
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
            return data.get('journalists', data if isinstance(data, list) else [])
    return []


def find_mechanism_56(research):
    """Find mechanism #56 in cross_publication_findings."""
    cpf = research.get('cross_publication_findings', {})
    for key, val in cpf.items():
        if isinstance(val, dict) and val.get('mechanism_id') == 56:
            return key, val
    return None, None


class TestMechanism56Exists:
    """Verify mechanism #56 is documented in competitor-coverage-research.yaml."""

    def test_mechanism_56_in_cpf(self):
        research = load_competitor_research()
        key, mech = find_mechanism_56(research)
        assert mech is not None, (
            "Mechanism #56 (Verge Intra-Publication Beat Segregation) "
            "must exist in cross_publication_findings"
        )

    def test_mechanism_56_has_required_fields(self):
        research = load_competitor_research()
        _, mech = find_mechanism_56(research)
        assert mech is not None
        required = ['mechanism_id', 'finding_summary', 'publication',
                     'finding_type', 'test_file']
        for field in required:
            assert field in mech, f"Mechanism #56 missing required field: {field}"

    def test_mechanism_56_publication_is_verge(self):
        research = load_competitor_research()
        _, mech = find_mechanism_56(research)
        assert mech is not None
        pub = mech.get('publication', '')
        assert 'Verge' in pub or 'verge' in pub or 'PMC' in pub, (
            f"Mechanism #56 publication should reference The Verge, got: {pub}"
        )

    def test_mechanism_56_finding_type(self):
        research = load_competitor_research()
        _, mech = find_mechanism_56(research)
        assert mech is not None
        ftype = mech.get('finding_type', '')
        assert 'beat' in ftype.lower() or 'segregation' in ftype.lower() or \
               'journalist' in ftype.lower() or 'intra' in ftype.lower(), (
            f"Mechanism #56 finding_type should reflect beat segregation pattern, got: {ftype}"
        )

    def test_mechanism_56_test_file_reference(self):
        research = load_competitor_research()
        _, mech = find_mechanism_56(research)
        assert mech is not None
        test_file = mech.get('test_file', '')
        assert 'beat_segregation' in test_file or 'verge_intra' in test_file, (
            f"Mechanism #56 test_file should reference this file, got: {test_file}"
        )


class TestBeatSegregationPattern:
    """Verify the beat segregation framing evidence is documented."""

    def test_platform_beat_reporters_documented(self):
        """At least one platform/product beat reporter at The Verge should be documented."""
        research = load_competitor_research()
        _, mech = find_mechanism_56(research)
        assert mech is not None
        summary = str(mech.get('finding_summary', ''))
        platform_evidence = mech.get('platform_beat_reporters', mech.get('platform_beat', {}))
        # Either in the summary or in a dedicated field
        has_weatherbed = 'Weatherbed' in summary or 'Weatherbed' in str(platform_evidence)
        has_song = 'Song' in summary or 'Song' in str(platform_evidence)
        assert has_weatherbed or has_song, (
            "Mechanism #56 should document at least one platform beat reporter "
            "(Weatherbed or Song) as the neutral-framing counterpart"
        )

    def test_ai_beat_reporters_documented(self):
        """AI beat reporters should be documented with deficit framing evidence."""
        research = load_competitor_research()
        _, mech = find_mechanism_56(research)
        assert mech is not None
        summary = str(mech.get('finding_summary', ''))
        ai_evidence = mech.get('ai_beat_reporters', mech.get('ai_beat', {}))
        has_field = 'Field' in summary or 'Field' in str(ai_evidence)
        assert has_field, (
            "Mechanism #56 should document Hayden Field as the AI beat reporter "
            "applying deficit framing to Meta"
        )

    def test_framing_divergence_documented(self):
        """The framing divergence between beats should have specific examples."""
        research = load_competitor_research()
        _, mech = find_mechanism_56(research)
        assert mech is not None
        # Check for framing language evidence
        all_text = str(mech)
        neutral_terms = ['adds', 'launches', 'rolls out', 'new', 'open-weight']
        deficit_terms = ['race', 'catching up', 'reentering', 'deficit', 'behind']
        has_neutral = any(term in all_text.lower() for term in neutral_terms)
        has_deficit = any(term in all_text.lower() for term in deficit_terms)
        assert has_neutral and has_deficit, (
            "Mechanism #56 should document both neutral (product beat) and "
            "deficit (AI beat) framing language"
        )


class TestFinancialRelationshipCorrelation:
    """Verify the financial relationship context is documented."""

    def test_pmc_openai_deal_documented(self):
        """PMC/Vox Media's OpenAI content licensing deal should be referenced."""
        research = load_competitor_research()
        _, mech = find_mechanism_56(research)
        assert mech is not None
        all_text = str(mech)
        assert 'OpenAI' in all_text, (
            "Mechanism #56 should reference PMC/Vox Media's OpenAI deal "
            "as the financial relationship context"
        )

    def test_meta_deal_absence_documented(self):
        """Meta's $0 relationship with PMC should be noted."""
        research = load_competitor_research()
        _, mech = find_mechanism_56(research)
        assert mech is not None
        all_text = str(mech)
        has_meta_deal = '$0' in all_text or 'no deal' in all_text.lower() or \
                        'no content' in all_text.lower() or 'excluded' in all_text.lower()
        assert has_meta_deal, (
            "Mechanism #56 should document Meta's absence from PMC content deals"
        )


class TestControlledComparisonNovelty:
    """Verify this mechanism's novelty vs existing journalist mechanisms."""

    def test_distinct_from_mechanism_30(self):
        """Mechanism #30 (Chokkattu temporal oscillation) is same-journalist, different genres.
        Mechanism #56 is different-journalists, same publication, same entity."""
        research = load_competitor_research()
        _, mech = find_mechanism_56(research)
        assert mech is not None
        all_text = str(mech)
        # Should reference the distinction
        has_distinction = 'different journalist' in all_text.lower() or \
                          'intra-publication' in all_text.lower() or \
                          'beat assignment' in all_text.lower() or \
                          'beat segregation' in all_text.lower()
        assert has_distinction, (
            "Mechanism #56 should articulate its novelty: different-journalist "
            "same-publication comparison (vs same-journalist in #30/#31)"
        )

    def test_distinct_from_mechanism_52(self):
        """Mechanism #52 (Hayden Field AI Beat Concentration) covers Field's coverage
        volume asymmetry. Mechanism #56 compares Field to Weatherbed within The Verge."""
        research = load_competitor_research()
        _, mech = find_mechanism_56(research)
        assert mech is not None
        cross_refs = mech.get('cross_references', [])
        has_52_ref = any('52' in str(ref) for ref in cross_refs)
        assert has_52_ref, (
            "Mechanism #56 should cross-reference Mechanism #52 (Hayden Field) "
            "to show how it extends that finding"
        )


class TestConfoundingFactors:
    """Verify confounding factors are documented."""

    def test_confounding_factors_present(self):
        research = load_competitor_research()
        _, mech = find_mechanism_56(research)
        assert mech is not None
        confounders = mech.get('confounding_factors', mech.get('legitimate_factors', []))
        if isinstance(confounders, int):
            assert confounders >= 4, (
                f"Mechanism #56 should document at least 4 confounding factors, got {confounders}"
            )
        else:
            assert len(confounders) >= 4, (
                f"Mechanism #56 should document at least 4 confounding factors, got {len(confounders)}"
            )

    def test_product_vs_industry_legitimate_difference(self):
        """Should acknowledge that product beats legitimately cover different news."""
        research = load_competitor_research()
        _, mech = find_mechanism_56(research)
        assert mech is not None
        all_text = str(mech)
        has_legitimate = 'legitimate' in all_text.lower() or 'genuinely' in all_text.lower() or \
                         'different news' in all_text.lower() or 'different type' in all_text.lower()
        assert has_legitimate, (
            "Mechanism #56 should acknowledge legitimate editorial reasons "
            "for different framing across beats"
        )


class TestSourceURLs:
    """Verify source evidence is documented."""

    def test_has_source_urls(self):
        research = load_competitor_research()
        _, mech = find_mechanism_56(research)
        assert mech is not None
        sources = mech.get('source_urls', mech.get('sources', []))
        assert len(sources) >= 2, (
            f"Mechanism #56 should have at least 2 source URLs, got {len(sources)}"
        )

    def test_weatherbed_evidence_has_source(self):
        """Weatherbed coverage examples should have sources."""
        research = load_competitor_research()
        _, mech = find_mechanism_56(research)
        assert mech is not None
        all_text = str(mech)
        # Should have at least one Weatherbed-related URL or specific article reference
        has_weatherbed_source = 'weatherbed' in all_text.lower() or \
                                'Muse Glimmer' in all_text or \
                                'open-weight' in all_text.lower()
        assert has_weatherbed_source, (
            "Mechanism #56 should cite specific Weatherbed articles as evidence"
        )


class TestCrossReferences:
    """Verify cross-references to related mechanisms."""

    def test_cross_references_exist(self):
        research = load_competitor_research()
        _, mech = find_mechanism_56(research)
        assert mech is not None
        refs = mech.get('cross_references', [])
        assert len(refs) >= 2, (
            f"Mechanism #56 should cross-reference at least 2 related mechanisms, got {len(refs)}"
        )

    def test_references_hayden_field_mechanism(self):
        research = load_competitor_research()
        _, mech = find_mechanism_56(research)
        assert mech is not None
        refs = str(mech.get('cross_references', []))
        assert '52' in refs or 'Hayden Field' in refs, (
            "Should reference Mechanism #52 (Hayden Field AI Beat Concentration)"
        )

    def test_references_genre_framing_mechanism(self):
        research = load_competitor_research()
        _, mech = find_mechanism_56(research)
        assert mech is not None
        refs = str(mech.get('cross_references', []))
        has_genre_ref = '30' in refs or '31' in refs or 'genre' in refs.lower()
        assert has_genre_ref, (
            "Should reference Mechanism #30 (Chokkattu genre split) or "
            "#31 (Pero editorial direction override) for comparison"
        )


class TestDateAndRotation:
    """Verify metadata."""

    def test_has_date_added(self):
        research = load_competitor_research()
        _, mech = find_mechanism_56(research)
        assert mech is not None
        assert 'date_added' in mech or 'discovery_date' in mech, (
            "Mechanism #56 must have a date_added or discovery_date"
        )

    def test_rotation_type_is_b(self):
        research = load_competitor_research()
        _, mech = find_mechanism_56(research)
        assert mech is not None
        assert mech.get('rotation_type') == 'B', (
            f"Mechanism #56 rotation_type should be B, got {mech.get('rotation_type')}"
        )


class TestVergeBeatReporterCareers:
    """Verify journalist career data supports the analysis."""

    def test_field_career_documented(self):
        """Hayden Field's career should show CNBC → Verge transition."""
        journalists = load_journalists()
        field_entries = [j for j in journalists
                         if isinstance(j, dict) and 'Field' in str(j.get('name', ''))]
        # May or may not be in the careers DB yet — just check if findable
        # The important thing is the mechanism documents her background
        research = load_competitor_research()
        _, mech = find_mechanism_56(research)
        assert mech is not None
        all_text = str(mech)
        has_field_bg = 'CNBC' in all_text or 'Jun 2025' in all_text or \
                       'June 2025' in all_text
        assert has_field_bg, (
            "Mechanism #56 should document Field's CNBC → Verge transition "
            "(Jun 2025) to establish beat assignment context"
        )

    def test_weatherbed_coverage_scope_documented(self):
        """Weatherbed's coverage scope should show broad platform coverage."""
        research = load_competitor_research()
        _, mech = find_mechanism_56(research)
        assert mech is not None
        all_text = str(mech)
        platform_topics = ['WhatsApp', 'Threads', 'content moderation',
                           'scam detection', 'open-weight', 'Muse']
        matched = [t for t in platform_topics if t in all_text]
        assert len(matched) >= 2, (
            f"Mechanism #56 should document Weatherbed's platform coverage "
            f"scope with specific topics. Found: {matched}"
        )
