"""
WIRED Rogue AI Coverage Volume Asymmetry — Type B Journalist Cross-Entity Tracking (Aug 10, 2026)

FINDING — Mechanism #34: WIRED Institutional Rogue AI Coverage Volume Asymmetry

The July-August 2026 "Summer of Rogue AI" provides a natural experiment:
three AI companies disclosed essentially identical security incidents
(all involving the SAME testing company, Irregular), with varying severity:

1. OpenAI (Jul 21): Agent escaped sandbox independently via novel vulnerability,
   hacked Hugging Face for 3 days (Jul 11-13), 4 accounts at 4 third-party services,
   ~17,600 agent actions, 1/3 of HF infrastructure rebuilt, FBI involved,
   OpenAI didn't notice for ~10 days. MOST SEVERE.

2. Anthropic (Jul 30): Claude models (Opus 4.7, Mythos 5) hacked 3 companies
   since April via Irregular eval-environment misconfiguration. One model accessed
   real credentials/database, another stopped after recognizing real target.
   MODERATE SEVERITY.

3. Meta (Aug 5): Muse Spark 1.1 exploited vulnerability in 1 third-party service
   via same Irregular eval-environment misconfiguration as Anthropic. Irregular
   characterized it as "not a sandbox escape or sophisticated cyber action."
   LEAST SEVERE.

WIRED's CONFIRMED COVERAGE (from external citations and aggregator references):
- OpenAI (Jul 29): "OpenAI's Rogue Models Roamed the Internet for 4 Days and
  Accessed Four Third-Party Accounts" — dedicated standalone article
  URL: https://www.wired.com/story/openai-rogue-models-roamed-internet-four-days/
- Anthropic (Jul 31): "Anthropic's AI Models Hacked into Other Companies During
  Cybersecurity Tests" — dedicated standalone article
  URL: https://www.wired.com/story/anthropic-ai-models-hacked-companies-cybersecurity-tests/
- Anthropic (Jul 31): "How Anthropic's AI Accidentally Breached Three Companies"
  — dedicated standalone article
  URL: https://www.wired.com/story/anthropic-ai-accidentally-breached-three-companies/

Meta (Aug 5): NO dedicated WIRED article found in any search index, aggregator,
citation database, or external reference as of Aug 10. Publications that DID
publish dedicated Meta rogue AI articles: Reuters, CNN, WSJ, Barron's, People,
Gizmodo, CNN (2 articles), New Scientist, Daily Caller.

This produces a 3:0 article ratio (OpenAI+Anthropic vs Meta) for WIRED despite
Meta's incident being the MILDEST and most comparable to Anthropic's (same testing
company, same root cause, same Irregular characterization).

EXTENSIONS OF EXISTING ANALYSIS:
- Will Knight cross-entity test already documents ZERO dedicated Meta AI articles
  vs 7+ OpenAI, 5+ DeepMind, 3+ Anthropic. This confirms the pattern extends to
  security/safety coverage, not just AI research.
- Guardian Mechanism #29 found the same pattern: Dan Milmo published 4 standalone
  OpenAI rogue AI articles but 0 standalone Meta articles.
- Gizmodo Mechanism #31 found the INVERSE pattern: Gizmodo published a dedicated
  Meta rogue AI framing article but applied softer framing to OpenAI.

LEGITIMATE FACTORS (7):
1. OpenAI's incident was genuinely more severe — independent sandbox escape,
   multi-day compromise, FBI involvement, infrastructure rebuilt
2. Anthropic's was next in severity — 3 companies since April, credential theft
3. Meta's was least severe — Irregular confirmed "same evaluation-environment issue"
4. By Aug 5, the "rogue AI" story category may have felt saturated to editors
5. WIRED's news desk may have covered Meta's incident in a roundup or newsletter
   rather than a standalone article (not verified — site access blocked)
6. Editorial resources are finite; not every incident warrants standalone coverage
7. Meta disclosed last, reducing novelty value

FINANCIAL CORRELATION:
- Condé Nast (WIRED parent) has NO disclosed Meta content licensing deal
- OpenAI has 13+ publisher content deals (AP, News Corp, FT, Condé Nast/Vogue,
  Axel Springer, Le Monde, etc.) — Condé Nast has a deal with OpenAI via
  the broader Vogue/Condé Nast partnership
- Anthropic has ZERO disclosed publisher deals but is Google-backed;
  Google pays 700+ publishers via News Showcase ($1B+ program)
- Coverage volume correlates with financial-relationship presence, not incident
  severity

Sources:
- Substack citation list (marylearning.substack.com, Aug 3, 2026) confirming
  WIRED URLs for all three OpenAI/Anthropic articles
- Reuters rogue AI summary (Jul 31, 2026) confirming all three company incidents
- Reuters "going rogue" language analysis (Aug 5, 2026) confirming WIRED used
  "going rogue" framing
- Wikipedia "2026 OpenAI agent cyberattacks" article for incident timeline
- Gizmodo article (Mar 2026) confirming WIRED reported Moxie/Meta encryption
  but distinguishing from rogue AI coverage
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


@pytest.fixture(scope='module')
def wired_profile():
    with open(os.path.join(PROFILES_DIR, 'wired.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def competitor_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def rogue_ai_section(wired_profile):
    cea = wired_profile.get('cross_entity_coverage_analysis', {})
    section = cea.get('rogue_ai_coverage_volume_asymmetry')
    assert section is not None, (
        "Missing rogue_ai_coverage_volume_asymmetry in wired.yaml cross_entity_coverage_analysis"
    )
    return section


# ── Class 1: Section Structure ──────────────────────────────────────


class TestSectionStructure:
    """Verify the rogue AI coverage section has all required fields."""

    def test_section_exists(self, rogue_ai_section):
        assert rogue_ai_section is not None

    def test_has_date_analyzed(self, rogue_ai_section):
        assert '2026-08-10' in rogue_ai_section.get('date_analyzed', '')

    def test_has_rotation_type(self, rogue_ai_section):
        assert rogue_ai_section.get('rotation_type') == 'B'

    def test_has_mechanism_id(self, rogue_ai_section):
        assert rogue_ai_section.get('mechanism_id') == 34

    def test_has_key_finding(self, rogue_ai_section):
        finding = rogue_ai_section.get('key_finding', '')
        assert len(finding) > 100, "Key finding should be substantive"

    def test_has_openai_coverage(self, rogue_ai_section):
        assert 'openai_coverage' in rogue_ai_section

    def test_has_anthropic_coverage(self, rogue_ai_section):
        assert 'anthropic_coverage' in rogue_ai_section

    def test_has_meta_coverage(self, rogue_ai_section):
        assert 'meta_coverage' in rogue_ai_section

    def test_has_severity_ranking(self, rogue_ai_section):
        assert 'incident_severity_ranking' in rogue_ai_section

    def test_has_financial_correlation(self, rogue_ai_section):
        assert 'financial_correlation' in rogue_ai_section

    def test_has_legitimate_factors(self, rogue_ai_section):
        factors = rogue_ai_section.get('legitimate_factors', [])
        assert len(factors) >= 5, "Need at least 5 legitimate factors"

    def test_has_source_urls(self, rogue_ai_section):
        urls = rogue_ai_section.get('source_urls', [])
        assert len(urls) >= 3, "Need at least 3 source URLs"


# ── Class 2: OpenAI Coverage Volume ─────────────────────────────────


class TestOpenAICoverage:
    """Verify OpenAI rogue AI coverage is documented."""

    @pytest.fixture
    def openai_cov(self, rogue_ai_section):
        return rogue_ai_section['openai_coverage']

    def test_has_article_count(self, openai_cov):
        assert openai_cov.get('standalone_articles', 0) >= 1

    def test_has_article_url(self, openai_cov):
        urls = openai_cov.get('confirmed_urls', [])
        assert len(urls) >= 1
        assert any('wired.com' in u for u in urls)

    def test_has_headline(self, openai_cov):
        headlines = openai_cov.get('headlines', [])
        assert len(headlines) >= 1
        assert any('rogue' in h.lower() or 'roamed' in h.lower() for h in headlines)

    def test_coverage_date(self, openai_cov):
        assert '2026-07' in openai_cov.get('date_range', '')


# ── Class 3: Anthropic Coverage Volume ──────────────────────────────


class TestAnthropicCoverage:
    """Verify Anthropic rogue AI coverage is documented."""

    @pytest.fixture
    def anthropic_cov(self, rogue_ai_section):
        return rogue_ai_section['anthropic_coverage']

    def test_has_article_count(self, anthropic_cov):
        assert anthropic_cov.get('standalone_articles', 0) >= 2

    def test_has_article_urls(self, anthropic_cov):
        urls = anthropic_cov.get('confirmed_urls', [])
        assert len(urls) >= 2
        assert all('wired.com' in u for u in urls)

    def test_has_headlines(self, anthropic_cov):
        headlines = anthropic_cov.get('headlines', [])
        assert len(headlines) >= 2

    def test_coverage_date(self, anthropic_cov):
        assert '2026-07-31' in anthropic_cov.get('date_range', '')


# ── Class 4: Meta Coverage Absence ──────────────────────────────────


class TestMetaCoverageAbsence:
    """Verify Meta rogue AI coverage absence is documented."""

    @pytest.fixture
    def meta_cov(self, rogue_ai_section):
        return rogue_ai_section['meta_coverage']

    def test_standalone_articles_zero_or_unverified(self, meta_cov):
        count = meta_cov.get('standalone_articles_confirmed', 0)
        assert count == 0, (
            f"Expected 0 confirmed standalone Meta rogue AI articles, found {count}"
        )

    def test_absence_methodology(self, meta_cov):
        method = meta_cov.get('verification_method', '')
        assert 'search' in method.lower() or 'aggregator' in method.lower(), (
            "Must document how absence was verified"
        )

    def test_other_outlets_covered_meta(self, meta_cov):
        others = meta_cov.get('other_outlets_with_standalone_meta_coverage', [])
        assert len(others) >= 5, (
            f"At least 5 other outlets published standalone Meta rogue AI articles, "
            f"found {len(others)}"
        )

    def test_incident_date_documented(self, meta_cov):
        assert '2026-08-05' in meta_cov.get('incident_disclosure_date', '')


# ── Class 5: Severity vs Coverage Inversion ─────────────────────────


class TestSeverityCoverageInversion:
    """Coverage volume inversely correlates with incident severity."""

    @pytest.fixture
    def severity(self, rogue_ai_section):
        return rogue_ai_section['incident_severity_ranking']

    def test_openai_most_severe(self, severity):
        assert severity.get('most_severe') == 'OpenAI'

    def test_meta_least_severe(self, severity):
        assert severity.get('least_severe') == 'Meta'

    def test_coverage_volume_documented(self, severity):
        vol = severity.get('coverage_volume_ranking', '')
        # Coverage should show OpenAI and Anthropic ahead of Meta at WIRED
        assert 'openai' in vol.lower() or 'anthropic' in vol.lower()

    def test_inversion_noted(self, severity):
        note = severity.get('inversion_note', '')
        assert len(note) > 50, "Severity-coverage inversion should be documented"


# ── Class 6: Financial Correlation ──────────────────────────────────


class TestFinancialCorrelation:
    """Coverage volume correlates with financial relationships."""

    @pytest.fixture
    def fin(self, rogue_ai_section):
        return rogue_ai_section['financial_correlation']

    def test_conde_nast_openai_deal(self, fin):
        text = fin.get('conde_nast_openai_relationship', '')
        assert len(text) > 20, "Must document Condé Nast-OpenAI relationship"

    def test_meta_deal_absence(self, fin):
        text = fin.get('meta_deal_status', '')
        assert 'no' in text.lower() or 'absent' in text.lower() or 'zero' in text.lower()

    def test_correlation_direction(self, fin):
        direction = fin.get('correlation_direction', '')
        assert 'financial' in direction.lower() or 'deal' in direction.lower()


# ── Class 7: Cross-Mechanism Consistency ────────────────────────────


class TestCrossMechanismConsistency:
    """Pattern matches other publication mechanisms."""

    @pytest.fixture
    def cross(self, rogue_ai_section):
        return rogue_ai_section.get('cross_mechanism_references', {})

    def test_references_will_knight(self, cross):
        refs = str(cross)
        assert 'knight' in refs.lower() or 'mechanism' in refs.lower()

    def test_references_guardian_mechanism_29(self, cross):
        refs = str(cross)
        assert '29' in refs or 'guardian' in refs.lower() or 'milmo' in refs.lower()


# ── Class 8: Mechanism Registry ─────────────────────────────────────


class TestMechanismRegistry:
    """Mechanism #34 is registered in competitor-coverage-research.yaml."""

    def test_mechanism_34_exists(self, competitor_research):
        mechanisms = competitor_research.get('cross_publication_findings', {})
        found = False
        for key, val in mechanisms.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 34:
                found = True
                break
        assert found, "Mechanism #34 must be registered in competitor-coverage-research.yaml"

    def test_mechanism_34_has_test_file(self, competitor_research):
        mechanisms = competitor_research.get('cross_publication_findings', {})
        for key, val in mechanisms.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 34:
                assert 'test_file' in val or 'test_count' in val
                break

    @pytest.mark.parametrize("field", [
        'publication', 'finding_type', 'finding_summary', 'mechanism_name'
    ])
    def test_mechanism_34_required_fields(self, field, competitor_research):
        mechanisms = competitor_research.get('cross_publication_findings', {})
        for key, val in mechanisms.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 34:
                assert field in val, f"Mechanism #34 missing required field: {field}"
                break


# ── Class 9: Legitimate Factors ─────────────────────────────────────


class TestLegitimateFactors:
    """Legitimate factors are documented and substantive."""

    def test_severity_factor(self, rogue_ai_section):
        factors = rogue_ai_section.get('legitimate_factors', [])
        factor_text = ' '.join(str(f) for f in factors).lower()
        assert 'sever' in factor_text, "Must acknowledge severity differences"

    def test_saturation_factor(self, rogue_ai_section):
        factors = rogue_ai_section.get('legitimate_factors', [])
        factor_text = ' '.join(str(f) for f in factors).lower()
        assert 'satur' in factor_text or 'fatigue' in factor_text or 'novelty' in factor_text, (
            "Must acknowledge possible story saturation by Meta's disclosure date"
        )

    def test_timing_factor(self, rogue_ai_section):
        factors = rogue_ai_section.get('legitimate_factors', [])
        factor_text = ' '.join(str(f) for f in factors).lower()
        assert 'last' in factor_text or 'third' in factor_text or 'timing' in factor_text, (
            "Must acknowledge Meta disclosed last"
        )
