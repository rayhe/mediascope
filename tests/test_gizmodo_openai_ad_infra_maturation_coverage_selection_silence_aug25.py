"""
Gizmodo OpenAI Ad Infrastructure Maturation Coverage Selection Silence (Aug 2026)

Mechanism #299: Gizmodo Coverage Selection Silence on OpenAI Ad Infrastructure
               Maturation — AAM Default, Conversion Pixel, 35-Country Expansion

CORE FINDING:
Between January and August 2026, OpenAI built out a full advertising
infrastructure replicating Meta's ad-tech stack:
  - Conversion tracking pixel (functionally identical to Meta Pixel, Apr 2026)
  - Conversions API (same as Meta CAPI)
  - Automatic Advanced Matching (AAM) enabled by DEFAULT on all existing
    web pixels (Aug 17, 2026) — uses hashed customer PII from website forms
  - Geographic expansion to 35 countries (31 European markets, Aug 24, 2026)
  - $100M+ annualized ad revenue within 6 weeks of launch (Reuters, Mar 2026)

Gizmodo published ZERO articles on any of these developments. Their total
ChatGPT ads coverage remains ONE sympathetic article from January 17, 2026:
"OpenAI Launches Cheaper Subscriptions, Starts Testing Ads Because It's
Time to Pay the Piper."

Meanwhile, Gizmodo continued publishing alarm-vocabulary articles about Meta's
functionally identical ad targeting practices.

EXTENDS Mechanism #291 (Gizmodo AI Chat Ad Targeting Vocabulary Bifurcation):
#291 documented the initial vocabulary bifurcation. This mechanism documents
the ESCALATION — seven months of OpenAI ad infra maturation with zero
additional coverage, while Gizmodo investigated Meta Pixel (Big Tax Prep)
and continued Meta ad targeting alarm coverage.

KEY NATURAL EXPERIMENT:
OpenAI's AAM default rollout (Aug 17) is the same technique as Meta's
Advanced Matching. Both use hashed customer information from website forms
(email, phone, name) to attribute conversions. Both are opt-out rather than
opt-in. Gizmodo investigated Meta Pixel data sharing critically but has
zero coverage of OpenAI Pixel or AAM.

Sources:
  OpenAI AAM default: https://ppc.land/chatgpt-advertisers-face-10-days-to-opt-out-of-automatic-advanced-matching/
  OpenAI pixel: https://digiday.com/marketing/openai-builds-tool-to-track-whether-chatgpt-ads-convert/
  European expansion: https://www.techrepublic.com/article/news-openai-chatgpt-ads-europe-emea/
  Revenue scale: https://www.pymnts.com/news/artificial-intelligence/2026/83percent-chatgpt-ad-triggers-dont-exist-in-traditional-search/
  Gizmodo OpenAI article: https://gizmodo.com/openai-launches-cheaper-subscriptions-starts-testing-ads-because-its-time-to-pay-the-piper-2000711284
  Gizmodo Meta article: https://gizmodo.com/metas-new-privacy-policy-opens-up-ai-chats-for-targeted-ads-2000704852
"""
import os
import yaml
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


@pytest.fixture
def competitor_research():
    path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
    with open(path) as f:
        data = yaml.safe_load(f)
    return data


@pytest.fixture
def mechanism(competitor_research):
    findings = competitor_research.get('aggregate_findings', {})
    return findings.get('gizmodo_openai_ad_infrastructure_maturation_coverage_selection_silence', {})


@pytest.fixture
def publications():
    path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
    with open(path) as f:
        data = yaml.safe_load(f)
    return data


# ── Mechanism Structure ──────────────────────────────────────────────────

class TestMechanismStructure:
    """Verify mechanism #299 exists and has required fields."""

    def test_mechanism_exists(self, mechanism):
        assert mechanism, "Mechanism gizmodo_openai_ad_infra_maturation_coverage_selection_silence must exist"

    def test_mechanism_id(self, mechanism):
        assert mechanism.get('mechanism_id') == 299

    def test_mechanism_type(self, mechanism):
        assert mechanism.get('mechanism_type') == 'coverage_selection_silence'

    def test_publication_is_gizmodo(self, mechanism):
        assert mechanism.get('publication') == 'Gizmodo'

    def test_entity_covered_is_meta(self, mechanism):
        assert mechanism.get('entity_covered') == 'Meta'

    def test_entity_silent_is_openai(self, mechanism):
        assert mechanism.get('entity_silent') == 'OpenAI'

    def test_has_title(self, mechanism):
        title = mechanism.get('title', '')
        assert 'AAM' in title or 'Automatic Advanced Matching' in title or 'Ad Infrastructure' in title

    def test_has_summary(self, mechanism):
        summary = mechanism.get('summary', '')
        assert len(summary) > 100, "Summary must be substantive"

    def test_has_sources(self, mechanism):
        sources = mechanism.get('sources', [])
        assert len(sources) >= 5, f"Expected at least 5 sources, got {len(sources)}"


# ── Key Evidence: OpenAI AAM Default ─────────────────────────────────────

class TestOpenAIAAMDefault:
    """Verify documentation of OpenAI's Automatic Advanced Matching default rollout."""

    def test_aam_evidence_exists(self, mechanism):
        evidence = mechanism.get('key_evidence', {})
        assert 'openai_aam_default' in evidence

    def test_aam_date(self, mechanism):
        aam = mechanism.get('key_evidence', {}).get('openai_aam_default', {})
        assert aam.get('date') == '2026-08-17'

    def test_aam_event_describes_default(self, mechanism):
        aam = mechanism.get('key_evidence', {}).get('openai_aam_default', {})
        event = aam.get('event', '')
        assert 'default' in event.lower(), "Must document that AAM was made DEFAULT"

    def test_aam_event_describes_hashed_data(self, mechanism):
        aam = mechanism.get('key_evidence', {}).get('openai_aam_default', {})
        event = aam.get('event', '')
        assert 'hashed' in event.lower(), "Must document hashed customer information"

    def test_aam_event_describes_opt_out(self, mechanism):
        aam = mechanism.get('key_evidence', {}).get('openai_aam_default', {})
        event = aam.get('event', '')
        assert 'opt' in event.lower(), "Must document opt-out mechanism"

    def test_aam_gizmodo_coverage_zero(self, mechanism):
        aam = mechanism.get('key_evidence', {}).get('openai_aam_default', {})
        coverage = str(aam.get('gizmodo_coverage', '')).upper()
        assert 'ZERO' in coverage or '0' in coverage

    def test_aam_has_source(self, mechanism):
        aam = mechanism.get('key_evidence', {}).get('openai_aam_default', {})
        source = aam.get('source', '')
        assert 'ppc.land' in source or 'seroundtable' in source


# ── Key Evidence: OpenAI Conversion Pixel ────────────────────────────────

class TestOpenAIConversionPixel:
    """Verify documentation of OpenAI's conversion tracking pixel."""

    def test_pixel_evidence_exists(self, mechanism):
        evidence = mechanism.get('key_evidence', {})
        assert 'openai_conversion_pixel' in evidence

    def test_pixel_date(self, mechanism):
        pixel = mechanism.get('key_evidence', {}).get('openai_conversion_pixel', {})
        assert pixel.get('date') == '2026-04-16'

    def test_pixel_event_describes_meta_equivalence(self, mechanism):
        pixel = mechanism.get('key_evidence', {}).get('openai_conversion_pixel', {})
        event = pixel.get('event', '')
        assert 'meta pixel' in event.lower(), "Must document Meta Pixel functional equivalence"

    def test_pixel_gizmodo_coverage_zero(self, mechanism):
        pixel = mechanism.get('key_evidence', {}).get('openai_conversion_pixel', {})
        coverage = str(pixel.get('gizmodo_coverage', '')).upper()
        assert 'ZERO' in coverage or '0' in coverage

    def test_pixel_documents_meta_pixel_coverage(self, mechanism):
        pixel = mechanism.get('key_evidence', {}).get('openai_conversion_pixel', {})
        meta_coverage = pixel.get('gizmodo_meta_pixel_coverage', '')
        assert 'Big Tax Prep' in meta_coverage or 'Meta Pixel' in meta_coverage, \
            "Must cross-reference Gizmodo's critical Meta Pixel coverage"


# ── Key Evidence: European Expansion ─────────────────────────────────────

class TestEuropeanExpansion:
    """Verify documentation of ChatGPT Ads 31-country European expansion."""

    def test_european_evidence_exists(self, mechanism):
        evidence = mechanism.get('key_evidence', {})
        assert 'openai_european_expansion' in evidence

    def test_european_date(self, mechanism):
        eu = mechanism.get('key_evidence', {}).get('openai_european_expansion', {})
        assert eu.get('date') == '2026-08-24'

    def test_european_event_describes_31_markets(self, mechanism):
        eu = mechanism.get('key_evidence', {}).get('openai_european_expansion', {})
        event = eu.get('event', '')
        assert '31' in event, "Must specify 31 European markets"

    def test_european_gizmodo_coverage_zero(self, mechanism):
        eu = mechanism.get('key_evidence', {}).get('openai_european_expansion', {})
        coverage = str(eu.get('gizmodo_coverage', '')).upper()
        assert 'ZERO' in coverage or '0' in coverage


# ── Vocabulary Analysis ──────────────────────────────────────────────────

class TestVocabularyAnalysis:
    """Verify vocabulary bifurcation documentation."""

    def test_vocabulary_analysis_exists(self, mechanism):
        assert 'vocabulary_analysis' in mechanism

    def test_openai_jan17_alarm_terms_zero(self, mechanism):
        vocab = mechanism.get('vocabulary_analysis', {}).get('gizmodo_openai_jan17', {})
        assert vocab.get('alarm_terms') == 0

    def test_openai_jan17_sympathy_terms_nonzero(self, mechanism):
        vocab = mechanism.get('vocabulary_analysis', {}).get('gizmodo_openai_jan17', {})
        assert vocab.get('sympathy_terms', 0) > 0

    def test_openai_jan17_privacy_citations_zero(self, mechanism):
        vocab = mechanism.get('vocabulary_analysis', {}).get('gizmodo_openai_jan17', {})
        assert vocab.get('privacy_group_citations') == 0

    def test_openai_jan17_surveillance_vocab_zero(self, mechanism):
        vocab = mechanism.get('vocabulary_analysis', {}).get('gizmodo_openai_jan17', {})
        assert vocab.get('surveillance_vocabulary') == 0

    def test_meta_jan06_alarm_terms_nonzero(self, mechanism):
        vocab = mechanism.get('vocabulary_analysis', {}).get('gizmodo_meta_jan06', {})
        assert vocab.get('alarm_terms', 0) > 0

    def test_meta_jan06_privacy_groups_count_36(self, mechanism):
        vocab = mechanism.get('vocabulary_analysis', {}).get('gizmodo_meta_jan06', {})
        assert vocab.get('privacy_groups_count') == 36

    def test_meta_jan06_surveillance_vocab_nonzero(self, mechanism):
        vocab = mechanism.get('vocabulary_analysis', {}).get('gizmodo_meta_jan06', {})
        assert vocab.get('surveillance_vocabulary', 0) > 0

    def test_meta_jan06_ftc_references_nonzero(self, mechanism):
        vocab = mechanism.get('vocabulary_analysis', {}).get('gizmodo_meta_jan06', {})
        assert vocab.get('ftc_references', 0) > 0

    def test_vocabulary_delta_alarm(self, mechanism):
        vocab = mechanism.get('vocabulary_analysis', {})
        openai_alarm = vocab.get('gizmodo_openai_jan17', {}).get('alarm_terms', 0)
        meta_alarm = vocab.get('gizmodo_meta_jan06', {}).get('alarm_terms', 0)
        assert meta_alarm > openai_alarm, \
            f"Meta alarm ({meta_alarm}) must exceed OpenAI alarm ({openai_alarm})"

    def test_vocabulary_delta_sympathy(self, mechanism):
        vocab = mechanism.get('vocabulary_analysis', {})
        openai_sympathy = vocab.get('gizmodo_openai_jan17', {}).get('sympathy_terms', 0)
        meta_sympathy = vocab.get('gizmodo_meta_jan06', {}).get('sympathy_terms', 0)
        assert openai_sympathy > meta_sympathy, \
            f"OpenAI sympathy ({openai_sympathy}) must exceed Meta sympathy ({meta_sympathy})"


# ── Confounders ──────────────────────────────────────────────────────────

class TestConfounders:
    """Verify confounders are documented with appropriate strength ratings."""

    def test_confounders_exist(self, mechanism):
        confounders = mechanism.get('confounders', [])
        assert len(confounders) >= 3, "Need at least 3 confounders"

    def test_strong_confounder_exists(self, mechanism):
        confounders = mechanism.get('confounders', [])
        strong = [c for c in confounders if c.get('strength') == 'STRONG']
        assert len(strong) >= 1, "Need at least one STRONG confounder"

    def test_ad_tech_trade_press_confounder(self, mechanism):
        """The strongest confounder: ad infra may be trade press territory."""
        confounders = mechanism.get('confounders', [])
        trade_press = [c for c in confounders
                       if 'trade' in c.get('description', '').lower()
                       or 'b2b' in c.get('description', '').lower()]
        assert len(trade_press) >= 1, "Must document trade press territory confounder"

    def test_confounder_addresses_meta_pixel_precedent(self, mechanism):
        """Confounder must note Gizmodo DID cover Meta Pixel (trade press territory rebuttal)."""
        confounders = mechanism.get('confounders', [])
        meta_pixel = [c for c in confounders
                      if 'meta pixel' in c.get('description', '').lower()
                      or 'Big Tax Prep' in c.get('description', '')]
        assert len(meta_pixel) >= 1, \
            "Must note Gizmodo covers ad infra when Meta is involved (Big Tax Prep / Meta Pixel)"


# ── Cross References ─────────────────────────────────────────────────────

class TestCrossReferences:
    """Verify cross-references to related mechanisms."""

    def test_extends_mechanism_291(self, mechanism):
        refs = mechanism.get('cross_references', [])
        extends_291 = [r for r in refs if r.get('mechanism_id') == 291
                       and r.get('relationship') == 'extends']
        assert len(extends_291) >= 1, "Must extend mechanism #291 (initial vocabulary bifurcation)"

    def test_cross_ref_descriptions(self, mechanism):
        refs = mechanism.get('cross_references', [])
        for ref in refs:
            desc = ref.get('description', '')
            assert len(desc) > 20, f"Cross-reference to {ref.get('mechanism_id')} needs substantive description"


# ── Meta Alarm Coverage in Same Window ───────────────────────────────────

class TestMetaAlarmCoverageInWindow:
    """Verify documentation of Gizmodo's continued Meta alarm coverage."""

    def test_meta_coverage_examples_exist(self, mechanism):
        evidence = mechanism.get('key_evidence', {})
        meta_alarm = evidence.get('meta_gizmodo_alarm_coverage', [])
        assert len(meta_alarm) >= 1, "Must document Gizmodo Meta alarm coverage in same window"

    def test_meta_coverage_has_vocabulary(self, mechanism):
        evidence = mechanism.get('key_evidence', {})
        meta_alarm = evidence.get('meta_gizmodo_alarm_coverage', [])
        for article in meta_alarm:
            vocab = article.get('vocabulary', [])
            assert len(vocab) >= 2, f"Article '{article.get('title')}' needs vocabulary examples"

    def test_meta_coverage_has_external_critics(self, mechanism):
        evidence = mechanism.get('key_evidence', {})
        meta_alarm = evidence.get('meta_gizmodo_alarm_coverage', [])
        has_critics = any(article.get('external_critics')
                        for article in meta_alarm)
        assert has_critics, "At least one Meta alarm article must cite external critics"
