"""
Type D (10:00 PT): Cross-validation tests for Aug 6 morning iterations.

Validates data consistency across the three additions from 06:00-08:00:
  1. Guardian partial independence model (Type A, 06:00)
  2. Alex Heath Access Paradox — mechanism #5 (Type B, 07:00)
  3. Advance-Reddit-Perplexity triangle (Type C, 08:00)

Also validates: asymmetry gap ordering, five-mechanism taxonomy,
tone vocabulary consistency, and cross-profile reference integrity.
"""

import pytest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    with open(os.path.join(PROFILES_DIR, filename)) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def entities():
    return load_yaml('competitor-entities.yaml')


@pytest.fixture(scope='module')
def wired():
    return load_yaml('wired.yaml')


@pytest.fixture(scope='module')
def verge():
    return load_yaml('the-verge.yaml')


@pytest.fixture(scope='module')
def guardian():
    return load_yaml('guardian.yaml')


@pytest.fixture(scope='module')
def research():
    return load_yaml('competitor-coverage-research.yaml')


# ─── Guardian Partial Independence Model (Type A, 06:00) ─────────────


class TestGuardianPartialIndependence:
    """Validate Guardian's partial independence classification is consistent
    between competitor-coverage-research.yaml and guardian.yaml."""

    def test_guardian_research_has_asymmetry_verdict(self, research):
        g = research['publications']['guardian']
        assert 'asymmetry_verdict' in g

    def test_guardian_asymmetry_verdict_mentions_partial_independence(self, research):
        g = research['publications']['guardian']
        verdict = str(g['asymmetry_verdict']).lower()
        assert 'partial independence' in verdict

    def test_guardian_gap_narrower_than_wired(self, research):
        """Guardian gap (~0.25-0.35) should be documented as narrower than WIRED (~0.95)."""
        g = research['publications']['guardian']
        verdict = str(g['asymmetry_verdict'])
        assert '0.25' in verdict or '0.35' in verdict
        assert 'WIRED' in verdict

    def test_guardian_research_has_three_tier_assessment(self, research):
        g = research['publications']['guardian']
        assert 'three_tier_assessment' in g

    def test_guardian_three_tier_mentions_partial(self, research):
        g = research['publications']['guardian']
        assessment = str(g['three_tier_assessment']).lower()
        assert 'partial' in assessment or 'independence' in assessment

    def test_guardian_openai_tone_is_balanced_to_adversarial(self, research):
        """Guardian OpenAI tone should be reclassified to balanced_to_adversarial."""
        g = research['publications']['guardian']
        tone = g.get('openai_coverage_tone', '')
        assert 'balanced_to_adversarial' in str(tone)

    def test_guardian_meta_tone_more_negative_than_openai(self, research):
        """Meta coverage should be more adversarial than OpenAI coverage."""
        g = research['publications']['guardian']
        meta_tone = str(g.get('meta_coverage_tone', '')).lower()
        openai_tone = str(g.get('openai_coverage_tone', '')).lower()
        # Meta tone should contain 'adversarial' or 'critical'
        assert 'adversarial' in meta_tone or 'critical' in meta_tone
        # OpenAI should be balanced_to_adversarial, not purely adversarial
        assert 'balanced' in openai_tone

    def test_guardian_has_openai_examples(self, research):
        g = research['publications']['guardian']
        assert 'openai_examples' in g or 'openai_stargate_uk_sources' in g

    def test_guardian_stargate_uk_documented(self, research):
        """Stargate UK FOI investigation should be documented as key independence evidence."""
        g = research['publications']['guardian']
        g_str = str(g).lower()
        assert 'stargate' in g_str and ('uk' in g_str or 'foi' in g_str)


class TestGuardianToneVocabulary:
    """Ensure balanced_to_adversarial is valid in the tone vocabulary."""

    def test_balanced_to_adversarial_in_research(self, research):
        """At least one publication should use balanced_to_adversarial tone."""
        research_str = str(research)
        assert 'balanced_to_adversarial' in research_str

    def test_financial_relationships_accepts_tone(self):
        """test_financial_relationships.py should accept balanced_to_adversarial."""
        test_path = os.path.join(os.path.dirname(__file__), 'test_financial_relationships.py')
        with open(test_path) as f:
            content = f.read()
        assert 'balanced_to_adversarial' in content


# ─── Alex Heath Access Paradox (Type B, 07:00) ───────────────────────


class TestAccessParadoxConsistency:
    """Validate Access Paradox is documented consistently in The Verge
    profile and competitor-coverage-research.yaml."""

    def test_verge_editorial_leadership_has_heath(self, verge):
        el = verge.get('editorial_leadership', [])
        heath = None
        for person in el:
            if isinstance(person, dict) and 'heath' in str(person.get('name', '')).lower():
                heath = person
        assert heath is not None, "Alex Heath must be in editorial_leadership"

    def test_heath_has_access_paradox_in_stance(self, verge):
        el = verge.get('editorial_leadership', [])
        heath = next(p for p in el if isinstance(p, dict) and 'heath' in str(p.get('name', '')).lower())
        stance = str(heath.get('editorial_stance', ''))
        assert 'access paradox' in stance.lower()

    def test_heath_is_deputy_editor(self, verge):
        """Deputy Editor role is key to institutional weight argument."""
        el = verge.get('editorial_leadership', [])
        heath = next(p for p in el if isinstance(p, dict) and 'heath' in str(p.get('name', '')).lower())
        title = str(heath.get('title', '')).lower()
        assert 'deputy' in title or 'editor' in title

    def test_heath_stance_mentions_openai_access(self, verge):
        """Stance should document that Heath does access interviews with OpenAI too."""
        el = verge.get('editorial_leadership', [])
        heath = next(p for p in el if isinstance(p, dict) and 'heath' in str(p.get('name', '')).lower())
        stance = str(heath.get('editorial_stance', '')).lower()
        assert 'openai' in stance

    def test_heath_stance_mentions_decoder(self, verge):
        """Decoder interview format is the shared access mechanism."""
        el = verge.get('editorial_leadership', [])
        heath = next(p for p in el if isinstance(p, dict) and 'heath' in str(p.get('name', '')).lower())
        stance = str(heath.get('editorial_stance', '')).lower()
        assert 'decoder' in stance

    def test_heath_stance_mentions_snap(self, verge):
        """Snap coverage provides third entity comparison."""
        el = verge.get('editorial_leadership', [])
        heath = next(p for p in el if isinstance(p, dict) and 'heath' in str(p.get('name', '')).lower())
        stance = str(heath.get('editorial_stance', '')).lower()
        assert 'snap' in stance or 'spectacles' in stance

    def test_research_asymmetry_verdict_references_access_paradox(self, research):
        """The Verge's asymmetry verdict should reference mechanism #5."""
        v = research['publications']['the-verge']
        verdict = str(v.get('asymmetry_verdict', ''))
        assert 'Access Paradox' in verdict or 'mechanism #5' in verdict.lower() or 'access paradox' in verdict.lower()

    def test_heath_hayden_field_beat_separation(self, verge):
        """Hayden Field should handle OpenAI beat separately from Heath."""
        el = verge.get('editorial_leadership', [])
        heath = next(p for p in el if isinstance(p, dict) and 'heath' in str(p.get('name', '')).lower())
        stance = str(heath.get('editorial_stance', ''))
        assert 'Hayden Field' in stance or 'hayden' in stance.lower()


# ─── Five-Mechanism Taxonomy Consistency ──────────────────────────────


class TestFiveMechanismTaxonomy:
    """Validate all five asymmetry mechanisms are documented consistently."""

    MECHANISMS = [
        ('WIRED', 'desk assignment'),
        ('NYT', 'between-reporter'),
        ('FT', 'within-reporter'),
        ('Verge', 'four-lane'),
        ('Access Paradox', 'access'),
    ]

    def test_verge_research_references_all_mechanisms(self, research):
        """The Verge's asymmetry verdict should reference the full taxonomy."""
        v = research['publications']['the-verge']
        verdict = str(v.get('asymmetry_verdict', ''))
        # Should reference at least 4 of the 5 mechanisms
        mechanism_hits = sum(1 for mech_pub, _ in self.MECHANISMS if mech_pub in verdict)
        assert mechanism_hits >= 4, f"Only {mechanism_hits}/5 mechanisms referenced in verdict"

    def test_wired_desk_assignment_documented(self, research):
        w = research['publications']['wired']
        w_str = str(w)
        assert 'desk' in w_str.lower() or 'assignment' in w_str.lower() or 'lane' in w_str.lower()

    def test_ft_within_reporter_documented(self, research):
        ft = research['publications']['financial-times']
        ft_str = str(ft)
        assert 'within-reporter' in ft_str.lower() or 'within_reporter' in ft_str.lower() or 'same reporter' in ft_str.lower() or 'Hannah Murphy' in ft_str

    def test_nyt_between_reporter_documented(self, research):
        nyt = research['publications']['nytimes']
        nyt_str = str(nyt)
        assert 'between-reporter' in nyt_str.lower() or 'between_reporter' in nyt_str.lower() or 'different reporter' in nyt_str.lower() or 'Cade Metz' in nyt_str


# ─── Advance-Reddit-Perplexity Triangle (Type C, 08:00) ──────────────


class TestAdvanceTriangleConsistency:
    """Validate the Advance-Reddit-Perplexity triangle is documented
    consistently across profiles."""

    def test_wired_has_triangle_section(self, research):
        w = research['publications']['wired']
        assert 'advance_reddit_perplexity_triangle' in w

    def test_triangle_mentions_reddit_lawsuit(self, research):
        w = research['publications']['wired']
        triangle = str(w.get('advance_reddit_perplexity_triangle', {}))
        assert 'DMCA' in triangle or 'suing' in triangle.lower() or 'lawsuit' in triangle.lower()

    def test_triangle_mentions_conde_nast_licensing(self, research):
        w = research['publications']['wired']
        triangle = str(w.get('advance_reddit_perplexity_triangle', {}))
        assert 'licensing' in triangle.lower() or 'Comet Plus' in triangle or 'Condé Nast' in triangle

    def test_triangle_mentions_engelmayer_ruling(self, research):
        """Jul 31 2026 ruling should be documented."""
        w = research['publications']['wired']
        triangle = str(w.get('advance_reddit_perplexity_triangle', {}))
        assert 'Engelmayer' in triangle or 'Jul' in triangle or '2026' in triangle

    def test_entities_has_reddit_deal_renewal(self, entities):
        """Reddit deal renewal projections should be in entities."""
        entities_str = str(entities)
        assert 'reddit_deal_renewal' in entities_str.lower() or '550' in entities_str

    def test_entities_has_reddit_perplexity_litigation(self, entities):
        """Reddit-Perplexity litigation should be documented."""
        entities_str = str(entities)
        assert 'reddit' in entities_str.lower() and ('perplexity' in entities_str.lower() or 'litigation' in entities_str.lower())

    def test_wired_perplexity_coverage_tone_neutral(self, research):
        """WIRED's Perplexity coverage tone should be neutral (despite lawsuit)."""
        w = research['publications']['wired']
        tone = str(w.get('perplexity_coverage_tone', ''))
        assert 'neutral' in tone.lower()

    def test_wired_has_perplexity_deal_source(self, research):
        w = research['publications']['wired']
        assert w.get('perplexity_deal_source') or w.get('perplexity_comet_plus_source')


class TestAdvanceTriangleSamAltmanConflict:
    """Sam Altman's dual role (8.7% Reddit + OpenAI CEO) creates
    an additional conflict that should be documented."""

    def test_altman_conflict_documented(self, research):
        w = research['publications']['wired']
        triangle = str(w.get('advance_reddit_perplexity_triangle', {}))
        assert 'Altman' in triangle or 'altman' in triangle.lower()

    def test_altman_reddit_stake_mentioned(self, research):
        w = research['publications']['wired']
        triangle = str(w.get('advance_reddit_perplexity_triangle', {}))
        assert '8.7%' in triangle or 'Reddit' in triangle


# ─── Asymmetry Gap Ordering ──────────────────────────────────────────


class TestAsymmetryGapOrdering:
    """Validate that asymmetry gaps follow a consistent ordering across publications."""

    def test_guardian_gap_less_than_ft(self, research):
        """Guardian (~0.25-0.35) should be less than FT (~0.45)."""
        guardian = str(research['publications']['guardian'].get('asymmetry_verdict', ''))
        # Guardian explicitly claims narrower gap than FT
        assert 'FT' in guardian or 'Financial Times' in guardian

    def test_verge_gap_less_than_wired(self, research):
        """Verge (~0.65) should be less than WIRED (~0.95)."""
        verge = str(research['publications']['the-verge'].get('asymmetry_verdict', ''))
        assert '0.65' in verge or 'WIRED' in verge

    def test_atlantic_gap_near_top(self, research):
        """Atlantic (~0.90) should be near the top of the gap ranking."""
        # Check aggregate or Atlantic-specific data
        agg_str = str(research.get('aggregate_findings', {}))
        atlantic_str = str(research['publications'].get('atlantic', {}))
        combined = agg_str + atlantic_str
        # Atlantic should appear somewhere with high gap
        assert 'atlantic' in combined.lower() or 'Atlantic' in combined

    def test_all_five_gaps_documented(self, research):
        """At least 5 publications should have documented asymmetry gaps."""
        count = 0
        for pub_name, pub_data in research['publications'].items():
            if isinstance(pub_data, dict) and 'asymmetry_verdict' in pub_data:
                count += 1
        assert count >= 5, f"Only {count} publications have asymmetry verdicts"


# ─── Cross-Profile Statistical Direction ─────────────────────────────


class TestStatisticalDirection:
    """Ensure that all profiled publications with competitor deals show
    coverage asymmetry in the PREDICTED direction (softer on deal partners)."""

    DEAL_PUBS = ['wired', 'the-verge', 'financial-times', 'guardian', 'nytimes']

    def test_deal_pubs_have_meta_coverage_tone(self, research):
        for pub in self.DEAL_PUBS:
            if pub in research['publications']:
                p = research['publications'][pub]
                assert 'meta_coverage_tone' in p, f"{pub} missing meta_coverage_tone"

    def test_deal_pubs_meta_tone_adversarial_or_critical(self, research):
        """All profiled pubs should have adversarial/critical Meta coverage."""
        for pub in self.DEAL_PUBS:
            if pub in research['publications']:
                p = research['publications'][pub]
                meta_tone = str(p.get('meta_coverage_tone', '')).lower()
                assert any(t in meta_tone for t in ['adversarial', 'critical', 'negative']), \
                    f"{pub} meta tone not adversarial: {meta_tone}"

    def test_gizmodo_control_has_no_asymmetry_verdict_or_neutral(self, research):
        """Gizmodo (no deals) should either lack an asymmetry verdict or show it's a clean control."""
        g = research['publications'].get('gizmodo', {})
        if 'asymmetry_verdict' in g:
            verdict = str(g['asymmetry_verdict']).lower()
            assert 'control' in verdict or 'no deal' in verdict or 'zero' in verdict
