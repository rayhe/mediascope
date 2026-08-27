"""
TechCrunch (Yahoo/Apollo) OpenAI ChatGPT Ads Europe Expansion Coverage Selection Silence (Aug 2026)

Mechanism #336: TechCrunch Coverage Selection Silence on OpenAI's Largest
                Advertising Geographic Expansion (31 European Markets)

CORE FINDING:
TechCrunch covered OpenAI's ChatGPT ads launch with three articles in
January-February 2026:
  1. "ChatGPT users are about to get hit with targeted ads" (Jan 16)
  2. "ChatGPT rolls out ads" (Feb 9)
  3. "OpenAI COO says ads will be 'an iterative process'" (Feb 25)

Then published ZERO articles on OpenAI's largest advertising geographic
expansion: 31 European markets (announced Aug 19, live Aug 24, 2026).
This expanded ChatGPT Ads to 35 countries total. OpenAI ad revenue
grew 25%+ since start of August (Adweek, Colin Fleming briefing call).

Within 48 hours of Meta's $18B settlement (Aug 26), TechCrunch published
TWO articles:
  1. "Meta settles for $18B in lawsuit brought by 29 states"
  2. "Meta's $18B child-safety deal hinges on age-verification tech
     that doesn't work well"

This creates a natural experiment in coverage selection: OpenAI's
largest ad infrastructure deployment gets zero TechCrunch coverage,
while Meta's accountability event gets immediate double coverage.

FINANCIAL ARCHITECTURE:
  - Yahoo (TechCrunch parent) has an OpenAI content licensing deal
  - Apollo Global Management (effective Yahoo parent since $5B Verizon
    Media acquisition) has AI infrastructure investments with deal-flow
    adjacency to Anthropic's pre-IPO trajectory
  - Yahoo/Meta compete directly for digital advertising revenue
  - No identified Yahoo-Meta content licensing deal

EXTENDS Mechanism #284 (TechCrunch Yahoo Apollo Anthropic/Meta data
practice vocabulary bifurcation): #284 documented vocabulary differences
when covering Anthropic vs Meta on data practices. This mechanism
documents a stronger signal: complete coverage ABSENCE for an OpenAI
business milestone that directly affects the advertising ecosystem
TechCrunch covers.

KEY CONTEXT:
Eight other outlets covered the European expansion within 48 hours:
  - TechRepublic (Aug 20), Neowin (Aug 19), Notebookcheck (Aug 22),
    Adweek (Aug 19), Digiday (Jun 8 + Aug), Le Monde (Aug 25),
    TechXplore/AFP (Aug 19), EU Perspectives (Aug 20)

The expansion includes all 27 EU member states plus Iceland,
Liechtenstein, Norway, and Switzerland. Personalized ads were NOT
initially available in the EEA (contextual only). OpenAI deployed
GDPR-compliant consent-based model rather than "legitimate interest."

Sources:
  OpenAI announcement: https://openai.com/index/chatgpt-ads-expands-across-europe/
  TechRepublic coverage: https://www.techrepublic.com/article/news-openai-chatgpt-ads-europe-emea/
  Adweek (Fleming briefing): https://www.adweek.com/media/openai-is-taking-its-ad-business-to-31-new-european-markets/
  Notebookcheck detail: https://www.notebookcheck.net/ChatGPT-ads-hit-Europe-on-Monday-but-not-the-personalized-kind.1375456.0.html
  Le Monde: https://www.lemonde.fr/en/economy/article/2026/08/25/ads-arrive-on-chatgpt-in-france_6756812_19.html
  TechCrunch initial coverage: https://techcrunch.com/2026/02/09/chatgpt-rolls-out-ads/
  TechCrunch Jan coverage: https://techcrunch.com/2026/01/16/chatgpt-users-are-about-to-get-hit-with-targeted-ads/
  TechCrunch COO: https://techcrunch.com/2026/02/25/openai-coo-says-ads-will-be-an-iterative-process/
  TechCrunch Meta settlement 1: https://techcrunch.com/2026/08/26/meta-settles-for-18-billion-in-lawsuit-brought-by-29-states-over-social-media-harms-to-children/
  TechCrunch Meta settlement 2: https://techcrunch.com/2026/08/26/metas-18b-child-safety-deal-hinges-on-age-verification-tech-that-doesnt-work-well/

Created: 2026-08-27
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
def entities():
    path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
    with open(path) as f:
        data = yaml.safe_load(f)
    return data


def _find_entry(data):
    """Find mechanism #336 entry across all top-level sections."""
    key = 'techcrunch_yahoo_openai_chatgpt_ads_europe_coverage_selection_silence'
    for section_name in ('cross_publication_findings', 'publications',
                         'aggregate_findings', 'cross_entity_leverage'):
        section = data.get(section_name, {})
        if isinstance(section, dict) and key in section:
            return section[key]
    return None


class TestMechanism336Exists:
    """Verify mechanism #336 is documented in competitor-coverage-research.yaml."""

    def test_mechanism_entry_exists(self, competitor_research):
        entry = _find_entry(competitor_research)
        assert entry is not None, (
            "Missing 'techcrunch_yahoo_openai_chatgpt_ads_europe_coverage_selection_silence' "
            "in competitor-coverage-research.yaml"
        )

    def test_mechanism_id(self, competitor_research):
        entry = _find_entry(competitor_research)
        assert entry['mechanism_id'] == 336

    def test_type_is_a(self, competitor_research):
        entry = _find_entry(competitor_research)
        assert entry['type'] == 'A'


class TestCoverageSelectionPattern:
    """Verify the coverage selection silence pattern is documented."""

    @pytest.fixture
    def entry(self, competitor_research):
        return _find_entry(competitor_research)

    def test_publication_is_techcrunch(self, entry):
        assert entry['publication'] == 'TechCrunch'

    def test_competitor_is_openai(self, entry):
        assert entry['competitor'] == 'openai'

    def test_initial_coverage_count(self, entry):
        """TechCrunch published 3 articles on ChatGPT ads in Jan-Feb 2026."""
        evidence = entry.get('evidence', [])
        initial_articles = [
            e for e in evidence
            if 'initial_coverage' in e.get('category', '')
            or 'Jan' in e.get('date', '') or 'Feb' in e.get('date', '')
            or '2026-01' in e.get('date', '') or '2026-02' in e.get('date', '')
        ]
        assert len(initial_articles) >= 2, (
            "Should document at least 2 initial TechCrunch ChatGPT ads articles"
        )

    def test_europe_expansion_coverage_zero(self, entry):
        """The finding must document zero TechCrunch coverage of Europe expansion."""
        desc = entry.get('description', '')
        assert 'zero' in desc.lower() or 'ZERO' in desc or '0' in desc, (
            "Finding must document zero TechCrunch coverage of Europe expansion"
        )

    def test_meta_settlement_coverage_documented(self, entry):
        """Must document TechCrunch's Meta settlement coverage for contrast."""
        evidence = entry.get('evidence', [])
        settlement_evidence = [
            e for e in evidence
            if 'settlement' in e.get('observation', '').lower()
            or 'settlement' in e.get('source', '').lower()
            or '$18' in e.get('observation', '')
        ]
        assert len(settlement_evidence) >= 1, (
            "Must document TechCrunch Meta settlement coverage as comparison"
        )


class TestFinancialArchitecture:
    """Verify financial relationships are documented."""

    @pytest.fixture
    def entry(self, competitor_research):
        return _find_entry(competitor_research)

    def test_yahoo_ownership_documented(self, entry):
        desc = entry.get('description', '') + str(entry.get('entities', []))
        assert 'yahoo' in desc.lower() or 'Yahoo' in str(entry), (
            "Must document Yahoo as TechCrunch parent"
        )

    def test_openai_content_deal_documented(self, entry):
        desc = entry.get('description', '')
        assert 'licensing' in desc.lower() or 'content deal' in desc.lower() or 'deal' in desc.lower(), (
            "Must document Yahoo-OpenAI content licensing relationship"
        )

    def test_apollo_documented(self, entry):
        desc = entry.get('description', '') + str(entry.get('entities', []))
        assert 'apollo' in desc.lower() or 'Apollo' in str(entry), (
            "Must document Apollo Global Management ownership context"
        )


class TestConfounders:
    """Verify confounders are documented with proper adjustments."""

    @pytest.fixture
    def entry(self, competitor_research):
        return _find_entry(competitor_research)

    def test_confounders_exist(self, entry):
        confounders = entry.get('confounders', [])
        assert len(confounders) >= 3, "Need at least 3 confounders"

    def test_strong_confounder_exists(self, entry):
        confounders = entry.get('confounders', [])
        strong = [c for c in confounders if c.get('strength') == 'STRONG']
        assert len(strong) >= 1, "Need at least one STRONG confounder"

    def test_editorial_independence_confounder(self, entry):
        """Must address possibility that editorial decisions are independent."""
        confounders = entry.get('confounders', [])
        descs = ' '.join(c.get('description', '') for c in confounders)
        assert (
            'editorial' in descs.lower()
            or 'independence' in descs.lower()
            or 'newsroom' in descs.lower()
        ), "Must include editorial independence confounder"

    def test_news_value_confounder(self, entry):
        """Must address Meta settlement being higher news value than ad expansion."""
        confounders = entry.get('confounders', [])
        descs = ' '.join(c.get('description', '') for c in confounders)
        assert (
            'news value' in descs.lower()
            or 'newsworthiness' in descs.lower()
            or 'settlement' in descs.lower()
            or 'audience' in descs.lower()
        ), "Must address differential news value between events"


class TestAsymmetryScore:
    """Verify asymmetry scoring follows methodology."""

    @pytest.fixture
    def entry(self, competitor_research):
        return _find_entry(competitor_research)

    def test_raw_score_exists(self, entry):
        assert 'raw_score' in entry
        assert 0 < entry['raw_score'] <= 1.0

    def test_adjusted_score_exists(self, entry):
        assert 'adjusted_score' in entry
        assert 0 < entry['adjusted_score'] <= 1.0

    def test_adjusted_less_than_raw(self, entry):
        assert entry['adjusted_score'] < entry['raw_score'], (
            "Adjusted score should be lower than raw after confounder adjustments"
        )

    def test_adjusted_score_reasonable(self, entry):
        """Coverage selection silence with strong confounders should land 0.15-0.50."""
        assert 0.15 <= entry['adjusted_score'] <= 0.50, (
            f"Adjusted score {entry['adjusted_score']} outside reasonable range"
        )


class TestCrossReferences:
    """Verify cross-references to related mechanisms."""

    @pytest.fixture
    def entry(self, competitor_research):
        return _find_entry(competitor_research)

    def test_cross_references_exist(self, entry):
        refs = entry.get('cross_references', [])
        assert len(refs) >= 2, "Need at least 2 cross-references"

    def test_references_mechanism_284(self, entry):
        """Must reference the prior TechCrunch Yahoo Apollo data practice mechanism."""
        refs = entry.get('cross_references', [])
        ref_ids = [r.get('mechanism_id') for r in refs]
        assert 284 in ref_ids, (
            "Must cross-reference mechanism #284 (TechCrunch Yahoo Apollo "
            "Anthropic/Meta data practice vocabulary bifurcation)"
        )


class TestEvidenceSources:
    """Verify all evidence has proper source URLs."""

    @pytest.fixture
    def entry(self, competitor_research):
        return _find_entry(competitor_research)

    def test_evidence_has_urls(self, entry):
        evidence = entry.get('evidence', [])
        for e in evidence:
            assert 'url' in e or 'source' in e, (
                f"Evidence entry missing url or source: {e}"
            )

    def test_evidence_has_dates(self, entry):
        evidence = entry.get('evidence', [])
        for e in evidence:
            assert 'date' in e, f"Evidence entry missing date: {e}"

    def test_evidence_count(self, entry):
        evidence = entry.get('evidence', [])
        assert len(evidence) >= 5, (
            "Need at least 5 evidence entries (3 initial + settlement + expansion)"
        )


class TestOpenAIEntityExists:
    """Verify OpenAI entity is in competitor-entities.yaml."""

    def test_openai_in_entities(self, entities):
        assert 'openai' in entities.get('entities', {}), (
            "OpenAI must be in competitor-entities.yaml"
        )
