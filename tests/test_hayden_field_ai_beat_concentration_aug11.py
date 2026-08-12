"""
Test Mechanism #52: Hayden Field AI Beat Concentration at The Verge
Type B: Journalist Cross-Entity Tracking — August 11, 2026

Hayden Field joined The Verge from CNBC as senior AI reporter (Jun 2, 2025).
Her hiring announcement stated she would "lead coverage of the biggest names
in AI — including OpenAI, Anthropic, Google, Meta, Apple, and others."

Actual portfolio (Jun 2025 – Aug 2026) reveals massive beat concentration
toward OpenAI and Anthropic. Meta AI receives ~10% of coverage volume with
systematically different framing (follower/deficit vs aspiration/underdog).

This is the THIRD documented "AI reporter beat concentration" pattern after
Metz/NYT (#15) and Knight/WIRED (#22), establishing it as INDUSTRY-WIDE.
"""

import yaml
import os
import re

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_verge_profile():
    """Load The Verge publication profile."""
    path = os.path.join(PROFILES_DIR, 'the-verge.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def load_competitor_research():
    """Load competitor coverage research profile."""
    path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


# ===================================================================
# Test Class 1: Field Profile Exists in The Verge profile
# ===================================================================
class TestFieldProfileExists:
    """Verify Hayden Field exists in the-verge.yaml with cross_entity_coverage_analysis."""

    def test_field_in_key_journalists(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        names = [j['name'] for j in journalists]
        assert 'Hayden Field' in names, \
            f"Hayden Field not found in key_journalists. Found: {names}"

    def test_field_has_beat(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        assert 'beat' in field, "Hayden Field entry missing 'beat' field"
        assert 'AI' in field['beat'] or 'ai' in field['beat'].lower(), \
            f"Hayden Field beat should include AI. Got: {field['beat']}"

    def test_field_has_cross_entity_coverage_analysis(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        assert 'cross_entity_coverage_analysis' in field, \
            "Hayden Field missing cross_entity_coverage_analysis section"

    def test_field_has_openai_anthropic_coverage(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        assert 'openai_anthropic_coverage' in cea, \
            "Missing openai_anthropic_coverage in cross_entity_coverage_analysis"

    def test_field_has_meta_coverage(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        assert 'meta_coverage' in cea, \
            "Missing meta_coverage in cross_entity_coverage_analysis"

    def test_field_has_mandate_vs_reality_gap(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        assert 'mandate_vs_reality_gap' in cea, \
            "Missing mandate_vs_reality_gap in cross_entity_coverage_analysis"


# ===================================================================
# Test Class 2: Coverage Volume Asymmetry
# ===================================================================
class TestFieldCoverageVolumeAsymmetry:
    """Verify OpenAI/Anthropic article count significantly exceeds Meta article count."""

    def test_openai_anthropic_volume_documented(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        oa_coverage = cea.get('openai_anthropic_coverage', {})
        assert 'volume' in oa_coverage or 'article_count' in oa_coverage or \
            'coverage_volume' in oa_coverage, \
            "OpenAI/Anthropic coverage must document volume"

    def test_meta_volume_documented(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        meta_coverage = cea.get('meta_coverage', {})
        assert 'volume' in meta_coverage or 'article_count' in meta_coverage or \
            'coverage_volume' in meta_coverage, \
            "Meta coverage must document volume"

    def test_openai_anthropic_examples_present(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        oa_coverage = cea.get('openai_anthropic_coverage', {})
        examples = oa_coverage.get('examples', oa_coverage.get('article_examples', []))
        assert len(examples) >= 5, \
            f"Expected at least 5 OpenAI/Anthropic article examples, got {len(examples)}"

    def test_meta_examples_present(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        meta_coverage = cea.get('meta_coverage', {})
        examples = meta_coverage.get('examples', meta_coverage.get('article_examples', []))
        assert len(examples) >= 2, \
            f"Expected at least 2 Meta article examples, got {len(examples)}"

    def test_volume_ratio_documented(self):
        """The volume ratio (OpenAI/Anthropic vs Meta) should be at least 5:1."""
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        # Check the summary or finding mentions the ratio
        summary = str(cea)
        assert any(term in summary.lower() for term in [
            '5:1', '10%', 'near-zero', 'fraction', '~15', '~2-3',
            'dominated', 'concentrated', 'asymmetry'
        ]), "Volume ratio between OpenAI/Anthropic and Meta coverage should be documented"


# ===================================================================
# Test Class 3: Meta Framing Indicators
# ===================================================================
class TestFieldMetaFramingIndicators:
    """Verify Meta coverage uses follower/deficit framing language."""

    def test_reentering_framing_documented(self):
        """'Reentering the AI race' implies Meta LEFT the race (follower framing)."""
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        meta_coverage = cea.get('meta_coverage', {})
        content = str(meta_coverage).lower()
        assert 'reentering' in content or 're-entering' in content or \
            'reenter' in content, \
            "Meta 'reentering the AI race' framing must be documented"

    def test_follower_framing_noted(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        meta_coverage = cea.get('meta_coverage', {})
        content = str(meta_coverage).lower()
        assert any(term in content for term in [
            'follower', 'deficit', 'behind', 'catching up', 'reentry'
        ]), "Meta coverage must document follower/deficit framing"

    def test_rejected_offers_framing_documented(self):
        """Framing Meta as employer whose values researchers reject."""
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        meta_coverage = cea.get('meta_coverage', {})
        content = str(meta_coverage).lower()
        assert any(term in content for term in [
            'rejected', 'values', 'offers', 'defected'
        ]), "Meta talent war 'rejected offers' framing must be documented"

    def test_framing_indicators_list(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        meta_coverage = cea.get('meta_coverage', {})
        indicators = meta_coverage.get('framing_indicators', meta_coverage.get('framing', ''))
        assert indicators, "Meta coverage must have framing_indicators or framing field"


# ===================================================================
# Test Class 4: Anthropic Framing Indicators
# ===================================================================
class TestFieldAnthropicFramingIndicators:
    """Verify Anthropic coverage uses aspiration/victim framing language."""

    def test_aspiration_framing_documented(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        oa_coverage = cea.get('openai_anthropic_coverage', {})
        content = str(oa_coverage).lower()
        assert any(term in content for term in [
            'aspiration', 'betting its future', 'milestone', 'solidarity'
        ]), "Anthropic aspiration/milestone framing must be documented"

    def test_victim_framing_documented(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        oa_coverage = cea.get('openai_anthropic_coverage', {})
        content = str(oa_coverage).lower()
        assert any(term in content for term in [
            'victim', 'overreach', 'underdog', 'regulatory drama',
            'pentagon', 'government order'
        ]), "Anthropic victim/underdog framing must be documented"

    def test_business_milestone_framing_examples(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        oa_coverage = cea.get('openai_anthropic_coverage', {})
        content = str(oa_coverage).lower()
        assert any(term in content for term in [
            'ipo', 'filed', 'public', 'valuation', 'raises'
        ]), "Anthropic IPO/business milestone framing should be documented"

    def test_decoder_podcast_examples(self):
        """Decoder podcast appearances indicate prominent placement."""
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        oa_coverage = cea.get('openai_anthropic_coverage', {})
        content = str(oa_coverage).lower()
        assert 'decoder' in content, \
            "Decoder podcast appearances for OpenAI/Anthropic topics should be documented"


# ===================================================================
# Test Class 5: Mandate vs Reality Gap
# ===================================================================
class TestFieldMandateVsRealityGap:
    """Verify hiring description listed 6 companies but actual coverage dominated by 2."""

    def test_hiring_announcement_documented(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        mandate = cea.get('mandate_vs_reality_gap', {})
        content = str(mandate).lower()
        assert any(term in content for term in [
            'hiring', 'announcement', 'lead coverage', 'biggest names',
            'talkingbiznews', 'mandate'
        ]), "Hiring announcement and stated mandate must be documented"

    def test_six_companies_listed(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        mandate = cea.get('mandate_vs_reality_gap', {})
        content = str(mandate).lower()
        companies = ['openai', 'anthropic', 'google', 'meta', 'apple']
        found = [c for c in companies if c in content]
        assert len(found) >= 4, \
            f"Mandate should list multiple companies from job description. Found: {found}"

    def test_reality_gap_described(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        mandate = cea.get('mandate_vs_reality_gap', {})
        content = str(mandate).lower()
        assert any(term in content for term in [
            'dominated', 'concentrated', 'actual', 'gap', 'reality'
        ]), "Must describe the gap between mandate and actual coverage"

    def test_join_date_documented(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        content = str(cea).lower()
        assert any(term in content for term in [
            'june 2025', 'jun 2025', '2025-06', 'june 2, 2025'
        ]), "Field's join date (June 2025) must be documented"


# ===================================================================
# Test Class 6: Financial Correlation
# ===================================================================
class TestFieldFinancialCorrelation:
    """Verify financial relationship correlation is documented."""

    def test_openai_deal_noted(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        fc = cea.get('financial_correlation_note', cea.get('financial_correlation', ''))
        content = str(cea).lower()
        assert any(term in content for term in [
            'openai deal', 'content deal', 'licensing', 'pmc',
            'financial relationship', 'openai content'
        ]), "OpenAI content deal with PMC/Vox Media must be noted as financial correlation"

    def test_meta_no_deal_noted(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        content = str(cea).lower()
        assert any(term in content for term in [
            'no meta deal', 'meta has not', 'meta excluded',
            'no deal with meta', 'meta deal', 'no meta'
        ]), "Absence of Meta deal must be documented"

    def test_coverage_correlates_with_financial_interest(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        content = str(cea).lower()
        assert any(term in content for term in [
            'correlat', 'aligns', 'predicts', 'financial-relationship'
        ]), "Financial relationship → coverage correlation must be explicitly stated"


# ===================================================================
# Test Class 7: Cross-Platform Pattern (Industry-Wide)
# ===================================================================
class TestFieldCrossPlatformPattern:
    """Verify this is the THIRD instance of AI reporter beat concentration pattern."""

    def test_metz_nyt_parallel_documented(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        pattern = cea.get('industry_pattern_match', cea.get('cross_platform_pattern', ''))
        content = str(cea).lower()
        assert any(term in content for term in [
            'metz', 'nyt', 'new york times', 'cade metz'
        ]), "Cade Metz / NYT parallel must be documented"

    def test_knight_wired_parallel_documented(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        content = str(cea).lower()
        assert any(term in content for term in [
            'knight', 'wired', 'will knight'
        ]), "Will Knight / WIRED parallel must be documented"

    def test_industry_wide_pattern_described(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        content = str(cea).lower()
        assert any(term in content for term in [
            'industry-wide', 'industry wide', 'third instance',
            'third documented', 'cross-publication', 'pattern'
        ]), "Must explicitly note this is an industry-wide pattern"

    def test_third_instance_claimed(self):
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        content = str(cea).lower()
        assert any(term in content for term in [
            'third', '3rd', 'three'
        ]), "Must claim this is the third instance of the pattern"

    def test_victoria_song_counter_example(self):
        """Song is a COUNTER-example: wearables reporter covers Meta balanced-to-positive."""
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        content = str(cea).lower()
        assert any(term in content for term in [
            'song', 'counter', 'wearables', 'product'
        ]), "Victoria Song as counter-example should be mentioned"


# ===================================================================
# Test Class 8: Mechanism in Research Profile
# ===================================================================
class TestMechanismInResearchProfile:
    """Verify mechanism #52 exists in competitor-coverage-research.yaml."""

    def test_mechanism_52_exists(self):
        research = load_competitor_research()
        findings = research.get('cross_publication_findings', {})
        found = False
        for key, value in findings.items():
            if isinstance(value, dict) and value.get('mechanism_id') == 52:
                found = True
                break
        assert found, "Mechanism #52 not found in cross_publication_findings"

    def test_mechanism_52_has_correct_name(self):
        research = load_competitor_research()
        findings = research.get('cross_publication_findings', {})
        for key, value in findings.items():
            if isinstance(value, dict) and value.get('mechanism_id') == 52:
                name = value.get('mechanism_name', '')
                assert 'hayden field' in name.lower() or 'beat concentration' in name.lower(), \
                    f"Mechanism #52 name should reference Hayden Field or beat concentration. Got: {name}"
                break

    def test_mechanism_52_has_finding_type(self):
        research = load_competitor_research()
        findings = research.get('cross_publication_findings', {})
        for key, value in findings.items():
            if isinstance(value, dict) and value.get('mechanism_id') == 52:
                assert 'finding_type' in value, "Mechanism #52 must have finding_type"
                assert 'beat' in value['finding_type'].lower() or \
                    'journalist' in value['finding_type'].lower(), \
                    f"finding_type should relate to beat/journalist. Got: {value['finding_type']}"
                break

    def test_mechanism_52_has_rotation_type_B(self):
        research = load_competitor_research()
        findings = research.get('cross_publication_findings', {})
        for key, value in findings.items():
            if isinstance(value, dict) and value.get('mechanism_id') == 52:
                assert value.get('rotation_type') == 'B', \
                    f"Mechanism #52 should be rotation_type B. Got: {value.get('rotation_type')}"
                break

    def test_mechanism_52_has_discovery_date(self):
        research = load_competitor_research()
        findings = research.get('cross_publication_findings', {})
        for key, value in findings.items():
            if isinstance(value, dict) and value.get('mechanism_id') == 52:
                assert value.get('discovery_date') == '2026-08-11', \
                    f"Discovery date should be 2026-08-11. Got: {value.get('discovery_date')}"
                break

    def test_mechanism_52_has_journalist(self):
        research = load_competitor_research()
        findings = research.get('cross_publication_findings', {})
        for key, value in findings.items():
            if isinstance(value, dict) and value.get('mechanism_id') == 52:
                assert value.get('journalist') == 'Hayden Field', \
                    f"Journalist should be Hayden Field. Got: {value.get('journalist')}"
                break

    def test_mechanism_52_has_publication(self):
        research = load_competitor_research()
        findings = research.get('cross_publication_findings', {})
        for key, value in findings.items():
            if isinstance(value, dict) and value.get('mechanism_id') == 52:
                pub = value.get('publication', '')
                assert 'verge' in pub.lower(), \
                    f"Publication should reference The Verge. Got: {pub}"
                break

    def test_mechanism_52_has_test_file(self):
        research = load_competitor_research()
        findings = research.get('cross_publication_findings', {})
        for key, value in findings.items():
            if isinstance(value, dict) and value.get('mechanism_id') == 52:
                assert 'test_file' in value, "Mechanism #52 must reference its test file"
                assert 'hayden_field' in value['test_file'], \
                    f"Test file should reference hayden_field. Got: {value['test_file']}"
                break


# ===================================================================
# Test Class 9: Legitimate Factors
# ===================================================================
class TestLegitimateFactors:
    """Verify at least 6 legitimate confounding factors are documented."""

    def test_at_least_6_legitimate_factors(self):
        research = load_competitor_research()
        findings = research.get('cross_publication_findings', {})
        for key, value in findings.items():
            if isinstance(value, dict) and value.get('mechanism_id') == 52:
                factors = value.get('legitimate_factors',
                    value.get('confounding_factors', []))
                assert len(factors) >= 6, \
                    f"Expected at least 6 legitimate factors, got {len(factors)}"
                break

    def test_legitimate_factors_have_strength_ratings(self):
        research = load_competitor_research()
        findings = research.get('cross_publication_findings', {})
        for key, value in findings.items():
            if isinstance(value, dict) and value.get('mechanism_id') == 52:
                factors = value.get('legitimate_factors',
                    value.get('confounding_factors', []))
                content = str(factors).lower()
                strength_terms = ['strong', 'moderate', 'weak']
                found = [t for t in strength_terms if t in content]
                assert len(found) >= 2, \
                    f"Factors should have strength ratings (strong/moderate/weak). Found: {found}"
                break

    def test_newsworthy_events_factor_present(self):
        """OpenAI/Anthropic having more dramatic news events is a legitimate factor."""
        research = load_competitor_research()
        findings = research.get('cross_publication_findings', {})
        for key, value in findings.items():
            if isinstance(value, dict) and value.get('mechanism_id') == 52:
                factors_str = str(value.get('legitimate_factors',
                    value.get('confounding_factors', []))).lower()
                assert any(term in factors_str for term in [
                    'dramatic', 'newsworthy', 'news events', 'pentagon',
                    'unprecedented', 'crisis'
                ]), "News event volume factor should be present"
                break

    def test_beat_assignment_factor_present(self):
        """Beat reporters are supposed to go deep on their assigned companies."""
        research = load_competitor_research()
        findings = research.get('cross_publication_findings', {})
        for key, value in findings.items():
            if isinstance(value, dict) and value.get('mechanism_id') == 52:
                factors_str = str(value.get('legitimate_factors',
                    value.get('confounding_factors', []))).lower()
                assert any(term in factors_str for term in [
                    'beat', 'assignment', 'editorial choice', 'product reviewer',
                    'dedicated', 'reporter'
                ]), "Beat assignment editorial choice factor should be present"
                break


# ===================================================================
# Test Class 10: Source URLs
# ===================================================================
class TestSourceUrls:
    """Verify adequate source documentation."""

    def test_at_least_5_source_urls_in_research(self):
        research = load_competitor_research()
        findings = research.get('cross_publication_findings', {})
        for key, value in findings.items():
            if isinstance(value, dict) and value.get('mechanism_id') == 52:
                urls = value.get('source_urls', [])
                assert len(urls) >= 5, \
                    f"Expected at least 5 source URLs, got {len(urls)}"
                break

    def test_talkingbiznews_source_present(self):
        """TalkingBizNews hiring announcement is primary source for mandate."""
        research = load_competitor_research()
        findings = research.get('cross_publication_findings', {})
        for key, value in findings.items():
            if isinstance(value, dict) and value.get('mechanism_id') == 52:
                urls = value.get('source_urls', [])
                urls_str = str(urls).lower()
                assert 'talkingbiznews' in urls_str, \
                    "TalkingBizNews hiring announcement URL must be present"
                break

    def test_techmeme_source_present(self):
        """Techmeme tracks article reach and is a key source."""
        research = load_competitor_research()
        findings = research.get('cross_publication_findings', {})
        for key, value in findings.items():
            if isinstance(value, dict) and value.get('mechanism_id') == 52:
                urls = value.get('source_urls', [])
                urls_str = str(urls).lower()
                assert 'techmeme' in urls_str, \
                    "At least one Techmeme source URL must be present"
                break

    def test_source_urls_are_valid_format(self):
        """All source URLs should be well-formed HTTP(S) URLs."""
        research = load_competitor_research()
        findings = research.get('cross_publication_findings', {})
        for key, value in findings.items():
            if isinstance(value, dict) and value.get('mechanism_id') == 52:
                urls = value.get('source_urls', [])
                for url in urls:
                    assert url.startswith('http://') or url.startswith('https://'), \
                        f"Invalid URL format: {url}"
                break

    def test_source_urls_in_verge_profile(self):
        """Source URLs should also be present in the Verge profile."""
        profile = load_verge_profile()
        journalists = profile.get('key_journalists', [])
        field = next(j for j in journalists if j['name'] == 'Hayden Field')
        cea = field.get('cross_entity_coverage_analysis', {})
        content = str(cea).lower()
        assert 'http' in content, \
            "Cross-entity coverage analysis should include source URLs"
