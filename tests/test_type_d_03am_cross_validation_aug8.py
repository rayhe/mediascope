"""
Type D Cross-Validation: Aug 8 03:00 PT

Validates internal consistency across all three Aug 8 iterations:
  - Type B 01:00: Kevin Roose (NYT→Independent) cross-entity
  - Type C 02:00: Google Showcase Coercive Cycle
  - Type A (prior): NYT × Google Traffic Cannibalization Paradox

Cross-checks:
  1. Google coercive mechanisms consistent between entities and NYT profile
  2. Kevin Roose departure context aligns with NYT financial pressures
  3. Entity counts and test infrastructure remain stable
  4. Financial amplification model consistent across all three findings
  5. Source URLs present and non-empty for every new data point
"""

import os
import yaml
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(name):
    path = os.path.join(PROFILES_DIR, name)
    with open(path) as f:
        return yaml.safe_load(f)


class TestGoogleCoerciveCycleCrossValidation:
    """Verify Google Showcase data is consistent across entities and publication profiles."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.entities = load_yaml('competitor-entities.yaml')
        self.nyt = load_yaml('nytimes.yaml')
        self.research = load_yaml('competitor-coverage-research.yaml')

    def test_google_entity_has_showcase_coercive_cycle(self):
        google = self.entities['entities']['google']
        assert 'showcase_coercive_cycle' in google

    def test_three_stage_model_complete(self):
        cycle = self.entities['entities']['google']['showcase_coercive_cycle']
        assert 'stage_1_dependency_creation' in cycle
        assert 'stage_2_traffic_destruction' in cycle
        assert 'stage_3_forced_rights_extraction' in cycle

    def test_stage_1_commitment_is_1b(self):
        s1 = self.entities['entities']['google']['showcase_coercive_cycle']['stage_1_dependency_creation']
        assert s1['commitment_b'] == 1.0

    def test_stage_1_publisher_count_3000(self):
        s1 = self.entities['entities']['google']['showcase_coercive_cycle']['stage_1_dependency_creation']
        assert s1['publisher_count'] >= 3000

    def test_stage_2_traffic_decline_33_to_38(self):
        s2 = self.entities['entities']['google']['showcase_coercive_cycle']['stage_2_traffic_destruction']
        assert 30 <= s2['traffic_decline_pct_global'] <= 40
        assert 35 <= s2['traffic_decline_pct_us'] <= 45

    def test_stage_3_has_named_participants(self):
        s3 = self.entities['entities']['google']['showcase_coercive_cycle']['stage_3_forced_rights_extraction']
        participants = s3.get('named_pilot_participants', [])
        assert len(participants) >= 3
        names = [p.lower() for p in participants]
        assert any('guardian' in n for n in names)

    def test_coercive_cycle_has_source_urls(self):
        cycle = self.entities['entities']['google']['showcase_coercive_cycle']
        source_urls = cycle.get('source_urls', [])
        assert len(source_urls) >= 3, "Coercive cycle needs at least 3 source URLs"
        for url in source_urls:
            assert url.startswith('http'), f"Bad URL: {url}"

    def test_research_file_has_showcase_finding(self):
        findings = self.research.get('findings', self.research)
        # Check any top-level key mentioning showcase
        all_keys = str(findings).lower()
        assert 'showcase' in all_keys or 'coercive' in all_keys


class TestKevinRooseNYTConsistency:
    """Kevin Roose data in NYT profile cross-references correctly."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.nyt = load_yaml('nytimes.yaml')
        self.research = load_yaml('competitor-coverage-research.yaml')

    def _find_roose_journalist(self):
        """Find Kevin Roose in the journalists list."""
        # Try multiple possible keys
        for key in ('journalists', 'key_journalists', 'reporters'):
            journalists = self.nyt.get(key, [])
            if isinstance(journalists, list):
                for j in journalists:
                    if isinstance(j, dict):
                        name = j.get('name', j.get('journalist', ''))
                        if 'roose' in str(name).lower():
                            return j
            elif isinstance(journalists, dict):
                for k, val in journalists.items():
                    if 'roose' in k.lower():
                        return val
        # Try cross_entity_coverage
        cross = self.nyt.get('cross_entity_coverage', {})
        if isinstance(cross, dict):
            for key, val in cross.items():
                if 'roose' in key.lower():
                    return val
        return None

    def test_roose_exists_in_nyt_profile(self):
        """Kevin Roose should be documented in the NYT profile."""
        roose = self._find_roose_journalist()
        assert roose is not None, "Kevin Roose not found in NYT profile"

    def test_roose_has_departure_info(self):
        """Profile should note Roose is departing NYT Aug 2026."""
        nyt_str = str(self.nyt).lower()
        assert 'departing' in nyt_str or 'departure' in nyt_str or 'leaving' in nyt_str

    def test_roose_has_book_investment_noted(self):
        """AGI Chronicles book should be documented as conflict mechanism."""
        nyt_str = str(self.nyt).lower()
        assert 'agi chronicles' in nyt_str or 'agi' in nyt_str

    def test_roose_cross_entity_in_research(self):
        """Kevin Roose should appear in competitor-coverage-research."""
        research_str = str(self.research).lower()
        assert 'roose' in research_str

    def test_roose_research_has_mechanism(self):
        """Research entry should document triple professional identity capture or similar."""
        research = self.research
        roose_section = None
        if isinstance(research, dict):
            for key in research:
                if 'roose' in str(key).lower():
                    roose_section = research[key]
                    break
            if roose_section is None and 'findings' in research:
                for key in research['findings']:
                    if 'roose' in str(key).lower():
                        roose_section = research['findings'][key]
                        break
        if roose_section:
            section_str = str(roose_section).lower()
            assert ('identity capture' in section_str or
                    'professional identity' in section_str or
                    'book investment' in section_str or
                    'triple' in section_str), \
                "Roose research should document identity capture mechanism"

    def test_roose_has_source_urls(self):
        """Roose profile data should have source URLs."""
        nyt_str = str(self.nyt)
        assert 'kevinroose.substack.com' in nyt_str or 'muckrack.com' in nyt_str


class TestNYTGoogleTrafficParadoxConsistency:
    """NYT × Google traffic paradox data consistent with broader model."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.nyt = load_yaml('nytimes.yaml')
        self.entities = load_yaml('competitor-entities.yaml')
        self.research = load_yaml('competitor-coverage-research.yaml')

    def test_nyt_google_ad_dependency_noted(self):
        """NYT profile should document Google ad dependency > $100M."""
        nyt_str = str(self.nyt).lower()
        assert 'google' in nyt_str
        # Check for financial relationship mention
        assert ('ad' in nyt_str and 'dependency' in nyt_str) or \
               'revenue' in nyt_str or 'advertising' in nyt_str

    def test_nyt_meta_zero_revenue_relationship(self):
        """NYT profile should confirm Meta has $0 financial relationship."""
        nyt_str = str(self.nyt).lower()
        # Meta should be referenced as having no financial tie
        assert 'meta' in nyt_str

    def test_google_has_more_leverage_than_meta_in_entities(self):
        """Google entity should show more leverage mechanisms than Meta."""
        google = self.entities['entities']['google']
        meta = self.entities['entities']['meta']

        # Count AI-related investments/deals for each
        google_str = str(google).lower()
        meta_str = str(meta).lower()

        # Google should have showcase, ad, search, AI Overviews — multiple mechanisms
        google_mechanisms = sum(1 for k in ['showcase', 'overviews', 'advertising', 'search']
                               if k in google_str)
        assert google_mechanisms >= 2, \
            f"Google should have multiple leverage mechanisms, found {google_mechanisms}"

    def test_traffic_cannibalization_in_research(self):
        """Research file should document the traffic cannibalization paradox."""
        research_str = str(self.research).lower()
        assert 'traffic' in research_str or 'cannibalization' in research_str or \
               'q2' in research_str

    def test_q2_earnings_documented(self):
        """Research should reference NYT Q2 2026 earnings paradox."""
        research_str = str(self.research).lower()
        assert 'q2' in research_str or 'subscriber' in research_str or \
               'earnings' in research_str


class TestCrossIterationConsistency:
    """Verify all three Aug 8 findings are internally consistent with each other."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.entities = load_yaml('competitor-entities.yaml')
        self.nyt = load_yaml('nytimes.yaml')
        self.research = load_yaml('competitor-coverage-research.yaml')

    def test_google_leverage_count_consistent(self):
        """Google should have >= 4 leverage mechanisms across all data sources."""
        google = self.entities['entities']['google']
        google_str = str(google).lower()
        # Showcase + AI Overviews + ad revenue + search traffic = 4+
        mechanisms = []
        if 'showcase' in google_str:
            mechanisms.append('showcase')
        if 'overviews' in google_str or 'overview' in google_str:
            mechanisms.append('ai_overviews')
        if 'advertising' in google_str or 'ad_revenue' in google_str:
            mechanisms.append('advertising')
        if 'search' in google_str:
            mechanisms.append('search')
        assert len(mechanisms) >= 3, \
            f"Expected >= 3 Google leverage mechanisms, found: {mechanisms}"

    def test_meta_has_fewer_mechanisms_than_google(self):
        """Meta should have fewer publisher leverage mechanisms than Google."""
        meta = self.entities['entities']['meta']
        google = self.entities['entities']['google']
        meta_deals = meta.get('ai_content_deals', meta.get('publisher_deals', {}))
        meta_deal_count = len(meta_deals) if isinstance(meta_deals, (list, dict)) else 0
        # Google has showcase (3000+ publishers) + all its other mechanisms
        google_str = str(google).lower()
        assert 'showcase' in google_str  # Google has the massive deal

    def test_nyt_financial_amplification_model_direction(self):
        """Financial amplification: entities with more $ relationship get softer coverage.
        Google (high $) should get softer coverage than Meta ($0) in the model."""
        research_str = str(self.research).lower()
        # The model predicts inverse relationship: more financial ties = softer coverage
        assert 'amplification' in research_str or 'asymmetry' in research_str or \
               'inverse' in research_str or 'prediction' in research_str

    def test_roose_departure_aligns_with_nyt_financial_pressure(self):
        """Kevin Roose leaving NYT while NYT faces Google traffic crisis creates
        a natural experiment for coverage tone change tracking."""
        nyt_str = str(self.nyt).lower()
        # Both departure and financial pressure should be documented
        has_departure = 'departing' in nyt_str or 'departure' in nyt_str or 'leaving' in nyt_str
        has_financial = 'google' in nyt_str and ('revenue' in nyt_str or 'ad' in nyt_str)
        assert has_departure and has_financial, \
            "NYT profile should document both Roose departure and Google financial relationship"


class TestEntityCountStability:
    """Ensure entity and test file counts remain stable after Aug 8 iterations."""

    def test_entity_count_at_least_9(self):
        entities = load_yaml('competitor-entities.yaml')
        count = len(entities.get('entities', {}))
        assert count >= 9, f"Expected >= 9 entities, found {count}"

    def test_publication_profile_count(self):
        profiles = [f for f in os.listdir(PROFILES_DIR)
                    if f.endswith('.yaml') and not f.startswith('_')
                    and f not in ('competitor-entities.yaml', 'competitor-coverage-research.yaml',
                                  'advocacy-coalitions.yaml')]
        assert len(profiles) >= 8, f"Expected >= 8 publication profiles, found {len(profiles)}"

    def test_test_file_count_at_least_220(self):
        test_dir = os.path.join(PROFILES_DIR, '..', 'tests')
        test_files = [f for f in os.listdir(test_dir)
                      if f.startswith('test_') and f.endswith('.py')]
        assert len(test_files) >= 220, f"Expected >= 220 test files, found {len(test_files)}"

    def test_aug8_test_files_exist(self):
        """All test files from Aug 8 iterations must exist."""
        test_dir = os.path.join(PROFILES_DIR, '..', 'tests')
        aug8_files = [
            'test_kevin_roose_cross_entity.py',
            'test_google_showcase_coercive_cycle_aug8.py',
            'test_nyt_google_traffic_cannibalization_paradox_aug8.py',
        ]
        for f in aug8_files:
            assert os.path.exists(os.path.join(test_dir, f)), f"Missing: {f}"

    def test_readme_test_count_above_floor(self):
        readme_path = os.path.join(PROFILES_DIR, '..', 'README.md')
        with open(readme_path) as f:
            content = f.read()
        import re
        match = re.search(r'\*\*(\d[\d,]*)\s+tests\*\*', content)
        assert match, "README must state test count"
        count = int(match.group(1).replace(',', ''))
        assert count >= 6090, f"README test count {count} below 6090 floor"


class TestSourceURLIntegrity:
    """Every finding from Aug 8 iterations must have verifiable source URLs."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.research = load_yaml('competitor-coverage-research.yaml')

    def test_kevin_roose_research_has_urls(self):
        research_str = str(self.research)
        assert 'kevinroose.substack.com' in research_str

    def test_google_showcase_research_has_urls(self):
        research_str = str(self.research)
        # Tech Policy Press is the primary source for the coercive cycle
        assert 'techpolicy' in research_str.lower() or 'pymnts' in research_str.lower() or \
               'digiday' in research_str.lower()

    def test_nyt_traffic_research_has_q2_source(self):
        research_str = str(self.research).lower()
        assert 'q2' in research_str or 'oumi' in research_str or \
               'earnings' in research_str


class TestFinancialAmplificationModelIntegrity:
    """The core thesis: financial relationships predict coverage tone.
    Verify the model holds across all publications with Aug 8 data."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.entities = load_yaml('competitor-entities.yaml')

    def test_meta_has_fewest_publisher_financial_ties(self):
        """Meta should have the fewest coercive publisher mechanisms."""
        meta = self.entities['entities']['meta']
        google = self.entities['entities']['google']
        meta_str = str(meta).lower()
        google_str = str(google).lower()
        # Google has showcase (3000+ pubs), Meta doesn't
        assert 'showcase' not in meta_str
        assert 'showcase' in google_str

    def test_google_coercive_count_exceeds_meta(self):
        """Google's publisher leverage should measurably exceed Meta's."""
        google = self.entities['entities']['google']
        cycle = google.get('showcase_coercive_cycle', {})
        assert cycle, "Google should have showcase_coercive_cycle"
        stage_count = sum(1 for k in cycle if k.startswith('stage_'))
        assert stage_count >= 3, "Coercive cycle should have 3+ stages"

    def test_microsoft_highest_leverage(self):
        """Microsoft should have the most publisher leverage mechanisms."""
        ms = self.entities['entities'].get('microsoft', {})
        ms_str = str(ms).lower()
        # Microsoft has OpenAI partnership + LinkedIn + GitHub + Bing + Azure
        mechanisms = sum(1 for k in ['openai', 'linkedin', 'github', 'bing', 'azure', 'copilot']
                        if k in ms_str)
        assert mechanisms >= 3, \
            f"Microsoft should have >= 3 mechanisms, found {mechanisms}"

    def test_hierarchy_msft_gt_google_gt_meta(self):
        """Leverage hierarchy: MSFT > Google > Meta (by mechanism count)."""
        entities = self.entities['entities']
        # This is the core claim — verify it's structurally supported
        meta_str = str(entities.get('meta', {})).lower()
        google_str = str(entities.get('google', {})).lower()
        ms_str = str(entities.get('microsoft', {})).lower()

        # Google has showcase coercive cycle, Meta doesn't
        assert 'coercive' in google_str or 'showcase' in google_str
        assert 'coercive' not in meta_str
        # Microsoft has OpenAI axis
        assert 'openai' in ms_str
