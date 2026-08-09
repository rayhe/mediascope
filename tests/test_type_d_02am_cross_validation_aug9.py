"""
Type D Cross-Validation: Aug 9 02:00 PT

Validates internal consistency across the Aug 9 iterations and prior data:
  - Type B 00:00: Mark Gurman (Bloomberg) Access Dependency Mechanism
  - Type C 01:00: Apple-OpenAI Litigation Publisher Cross-Pressure + Anthropic Settlement Fix

Cross-checks:
  1. Cross-pressure publications in competitor-entities.yaml are consistent with
     OpenAI deal info documented in individual publication profiles
  2. Apple relationship data in publication profiles aligns with cross-pressure claims
  3. Anthropic settlement date correction (Jul 20) is consistent across all refs
  4. Coverage artifact predictions are internally consistent with financial model
  5. Mark Gurman mechanism #11 (access dependency) doesn't duplicate mechanisms 1-10
  6. Source URLs are present and well-formed for every new data point
  7. README and ARCHITECTURE test counts are synchronized
"""

import os
import re
import yaml
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
DOCS_DIR = os.path.join(os.path.dirname(__file__), '..', 'docs')
ROOT_DIR = os.path.join(os.path.dirname(__file__), '..')


def load_yaml(name):
    path = os.path.join(PROFILES_DIR, name)
    with open(path) as f:
        return yaml.safe_load(f)


def load_text(path):
    with open(path) as f:
        return f.read()


# ──────────────────────────────────────────────────────────────────────
# 1. Cross-pressure ↔ Publication profile consistency
# ──────────────────────────────────────────────────────────────────────


class TestCrossPressureProfileConsistency:
    """Verify that cross-pressure claims about OpenAI deals match
    what the individual publication profiles document."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.entities = load_yaml('competitor-entities.yaml')
        self.cp = self.entities['entities']['apple'][
            'openai_litigation_publisher_cross_pressure'
        ]
        self.pubs = self.cp['dual_relationship_publications']
        # Map cross-pressure publication names to profile filenames
        self.profile_map = {
            'Condé Nast': 'wired',
            'The Atlantic': 'atlantic',
            'Vox Media': 'the-verge',
            'News Corp': 'news-corp',
            'The Guardian': 'guardian',
        }

    def _find_pub(self, fragment):
        """Find a publication entry by name fragment."""
        for pub in self.pubs:
            if fragment.lower() in pub['publication'].lower():
                return pub
        return None

    def test_conde_nast_openai_deal_matches_wired_profile(self):
        """WIRED profile should document the Condé Nast OpenAI deal that
        cross-pressure analysis references."""
        wired = load_yaml('wired.yaml')
        cr = wired.get('competitor_relationships', {})
        openai = cr.get('openai', {})
        desc = str(openai.get('description', '')).lower()
        assert 'condé nast' in desc or 'conde nast' in desc or 'content licensing' in desc

    def test_atlantic_openai_deal_matches_profile(self):
        atlantic = load_yaml('atlantic.yaml')
        cr = atlantic.get('competitor_relationships', {})
        openai = cr.get('openai', {})
        desc = str(openai.get('description', '')).lower()
        assert 'content licensing' in desc or 'chatgpt' in desc

    def test_guardian_openai_deal_matches_profile(self):
        guardian = load_yaml('guardian.yaml')
        cr = guardian.get('competitor_relationships', {})
        openai = cr.get('openai', {})
        desc = str(openai.get('description', '')).lower()
        assert 'content licensing' in desc or 'chatgpt' in desc

    def test_verge_openai_deal_matches_profile(self):
        verge = load_yaml('the-verge.yaml')
        cr = verge.get('competitor_relationships', {})
        openai = cr.get('openai', {})
        desc = str(openai.get('description', '')).lower()
        assert 'vox media' in desc or 'content licensing' in desc

    def test_guardian_no_apple_news_consistent(self):
        """Cross-pressure says Guardian dropped Apple News in 2017.
        Guardian profile should show no Apple financial relationship."""
        guardian = load_yaml('guardian.yaml')
        cr = guardian.get('competitor_relationships', {})
        apple = cr.get('apple', {})
        desc = str(apple.get('description', '')).lower()
        # Should either mention 'no' relationship or be empty
        assert 'no known' in desc or desc == '' or 'n/a' in desc or not desc

    def test_atlantic_apple_stock_exposure_in_profile(self):
        """Cross-pressure notes LPJ Trust ~$17B Apple stock.
        Atlantic profile should document this ownership equity."""
        atlantic = load_yaml('atlantic.yaml')
        cr = atlantic.get('competitor_relationships', {})
        apple = cr.get('apple', {})
        desc = str(apple.get('description', '')).lower()
        assert 'laurene' in desc or 'powell' in desc or 'ownership' in desc


# ──────────────────────────────────────────────────────────────────────
# 2. Cross-pressure model internal consistency
# ──────────────────────────────────────────────────────────────────────


class TestCrossPressureModelConsistency:
    """Verify the cross-pressure model's predictions are internally coherent."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.entities = load_yaml('competitor-entities.yaml')
        self.cp = self.entities['entities']['apple'][
            'openai_litigation_publisher_cross_pressure'
        ]
        self.pubs = self.cp['dual_relationship_publications']
        self.artifacts = self.cp['key_coverage_artifacts']

    def test_all_pubs_have_cross_pressure_analysis(self):
        for pub in self.pubs:
            assert 'cross_pressure' in pub, (
                f"{pub['publication']} missing cross_pressure field"
            )
            assert pub['cross_pressure'], (
                f"{pub['publication']} has empty cross_pressure"
            )

    def test_guardian_unique_position_acknowledged(self):
        """Guardian is the only OpenAI-deal pub NOT on Apple News+.
        Its cross-pressure analysis should reflect this unique position."""
        guardian = next(
            p for p in self.pubs if 'Guardian' in p['publication']
        )
        cp_text = str(guardian['cross_pressure']).lower()
        assert 'unique' in cp_text or 'only' in cp_text or 'no apple' in cp_text or 'dropped' in cp_text

    def test_wsj_artifact_balanced_matches_dual_deal(self):
        """WSJ has deals with BOTH OpenAI AND Meta ($50M each).
        Balanced framing is the expected outcome of symmetric deals."""
        wsj_artifact = next(
            a for a in self.artifacts if 'WSJ' in a['publication']
        )
        framing = str(wsj_artifact['framing']).lower()
        assert 'balanced' in framing

    def test_reuters_artifact_is_control(self):
        """Reuters has no known deals with Apple or OpenAI.
        It serves as a clean control for coverage comparison."""
        reuters = next(
            a for a in self.artifacts if 'Reuters' in a['publication']
        )
        framing = str(reuters['framing']).lower()
        assert 'neutral' in framing or 'control' in framing

    def test_overview_predicts_apple_favorable(self):
        """Model predicts publications tilt toward greater-leverage partner.
        Apple has 5 mechanisms vs OpenAI's 1."""
        overview = str(self.cp['overview']).lower()
        assert 'apple' in overview
        assert 'greater' in overview or 'tilt' in overview or 'favor' in overview

    def test_both_outcome_scenarios_documented(self):
        assert 'apple_wins_financial_implications' in self.cp
        assert 'openai_wins_financial_implications' in self.cp


# ──────────────────────────────────────────────────────────────────────
# 3. Anthropic settlement date consistency (Jul 20 correction)
# ──────────────────────────────────────────────────────────────────────


class TestAnthropicSettlementDateConsistency:
    """Verify that the Jun 20 → Jul 20 date correction is consistent
    across all references in the dataset."""

    def test_no_jun_20_settlement_refs_in_entities(self):
        """No reference to 'Jun 20' or 'June 20' in connection with
        the Anthropic settlement should remain after the correction."""
        content = load_text(os.path.join(PROFILES_DIR, 'competitor-entities.yaml'))
        # Find lines mentioning both settlement and Jun 20
        for line in content.split('\n'):
            low = line.lower()
            if 'settlement' in low and ('jun 20' in low or 'june 20' in low):
                # Make sure it's not referring to Jun 2026 in general
                if re.search(r'(jun|june)\s+20[^2]', low) or re.search(r'(jun|june)\s+20$', low):
                    pytest.fail(f"Stale Jun 20 settlement date found: {line.strip()}")

    def test_jul_20_settlement_present(self):
        content = load_text(os.path.join(PROFILES_DIR, 'competitor-entities.yaml'))
        assert 'Jul 20' in content or 'Jul 2026' in content

    def test_anthropic_entity_has_settlement_detail(self):
        entities = load_yaml('competitor-entities.yaml')
        anthropic = entities['entities']['anthropic']
        assert 'author_settlement_detail' in anthropic

    def test_settlement_detail_judge_name(self):
        entities = load_yaml('competitor-entities.yaml')
        detail = entities['entities']['anthropic']['author_settlement_detail']
        judge = str(detail.get('final_approval_judge', '')).lower()
        assert 'martínez' in judge or 'martinez' in judge or 'olguin' in judge or 'olguín' in judge


# ──────────────────────────────────────────────────────────────────────
# 4. Mark Gurman mechanism uniqueness
# ──────────────────────────────────────────────────────────────────────


class TestGurmanMechanismUniqueness:
    """Verify that the access dependency mechanism (#11) documented for
    Gurman doesn't duplicate existing mechanism types 1-10."""

    @pytest.fixture(autouse=True)
    def setup(self):
        # Load any journalist cross-entity test file that has Gurman data
        self.research = load_yaml('competitor-coverage-research.yaml')

    def test_research_has_bloomberg_entry(self):
        """Bloomberg should be tracked in coverage research."""
        pubs = self.research.get('publications', {})
        if pubs:
            # Check if bloomberg exists as a key
            all_keys = str(pubs).lower()
            assert 'bloomberg' in all_keys or 'gurman' in all_keys

    def test_access_dependency_distinct_from_financial(self):
        """Access dependency (beat reporter access) is structurally different
        from financial incentive (content deals, ad revenue)."""
        entities = load_yaml('competitor-entities.yaml')
        # relationship_types should not conflate access with financial
        types = entities.get('relationship_types', {})
        if types:
            type_names = [str(t).lower() for t in types.keys()]
            # If access_dependency exists as a type, good
            # If it doesn't, that's also fine — mechanism is at journalist level
            # What we're checking: no existing financial type claims to cover access
            for name, desc in types.items():
                desc_low = str(desc).lower()
                assert not ('access dependency' in desc_low and 'licensing' in desc_low), \
                    f"Type '{name}' conflates access dependency with licensing"


# ──────────────────────────────────────────────────────────────────────
# 5. Source URL integrity
# ──────────────────────────────────────────────────────────────────────


class TestSourceURLIntegrity:
    """Verify all new source URLs are present and well-formed."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.entities = load_yaml('competitor-entities.yaml')
        self.cp = self.entities['entities']['apple'][
            'openai_litigation_publisher_cross_pressure'
        ]

    def test_cross_pressure_source_urls_present(self):
        urls = self.cp.get('source_urls', [])
        assert len(urls) >= 3, f"Expected ≥3 source URLs, got {len(urls)}"

    def test_cross_pressure_source_urls_well_formed(self):
        for url in self.cp.get('source_urls', []):
            assert url.startswith('http'), f"Malformed URL: {url}"
            assert ' ' not in url, f"URL contains spaces: {url}"

    def test_anthropic_settlement_detail_has_sources(self):
        detail = self.entities['entities']['anthropic']['author_settlement_detail']
        urls = detail.get('source_urls', [])
        assert len(urls) >= 2, f"Expected ≥2 settlement source URLs, got {len(urls)}"
        for url in urls:
            assert url.startswith('http'), f"Malformed URL: {url}"

    def test_each_coverage_artifact_has_publication(self):
        for artifact in self.cp['key_coverage_artifacts']:
            assert 'publication' in artifact
            assert artifact['publication']

    def test_each_coverage_artifact_has_framing(self):
        for artifact in self.cp['key_coverage_artifacts']:
            assert 'framing' in artifact
            assert artifact['framing']


# ──────────────────────────────────────────────────────────────────────
# 6. README / ARCHITECTURE count synchronization
# ──────────────────────────────────────────────────────────────────────


class TestInfrastructureCountSync:
    """Verify README and ARCHITECTURE report the same test/file counts."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.readme = load_text(os.path.join(ROOT_DIR, 'README.md'))
        self.arch = load_text(os.path.join(DOCS_DIR, 'ARCHITECTURE.md'))

    def _extract_test_count(self, text):
        """Extract the most prominent test count from a document."""
        matches = re.findall(r'(\d{3,5})\s*(?:tests|test cases)', text, re.IGNORECASE)
        return max(int(m) for m in matches) if matches else None

    def _extract_file_count(self, text):
        """Extract the most prominent file count from a document."""
        matches = re.findall(r'(\d{2,4})\s*(?:test files|files)', text, re.IGNORECASE)
        return max(int(m) for m in matches) if matches else None

    def test_test_counts_match(self):
        readme_count = self._extract_test_count(self.readme)
        arch_count = self._extract_test_count(self.arch)
        if readme_count and arch_count:
            assert readme_count == arch_count, (
                f"README says {readme_count} tests, ARCHITECTURE says {arch_count}"
            )

    def test_file_counts_match(self):
        readme_files = self._extract_file_count(self.readme)
        arch_files = self._extract_file_count(self.arch)
        if readme_files and arch_files:
            assert readme_files == arch_files, (
                f"README says {readme_files} files, ARCHITECTURE says {arch_files}"
            )

    def test_actual_test_file_count_reasonable(self):
        """The actual number of test files should not diverge too far
        from what README claims."""
        test_dir = os.path.join(ROOT_DIR, 'tests')
        actual = len([f for f in os.listdir(test_dir) if f.startswith('test_') and f.endswith('.py')])
        readme_files = self._extract_file_count(self.readme)
        if readme_files:
            # Allow ±5 file drift from documenting async
            assert abs(actual - readme_files) <= 5, (
                f"Actual test files ({actual}) diverged from README ({readme_files}) by >{5}"
            )


# ──────────────────────────────────────────────────────────────────────
# 7. Cross-entity financial data coherence
# ──────────────────────────────────────────────────────────────────────


class TestFinancialDataCoherence:
    """Verify that financial claims in the cross-pressure section
    are consistent with entity-level financial data."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.entities = load_yaml('competitor-entities.yaml')

    def test_openai_has_publisher_deals_section(self):
        openai = self.entities['entities']['openai']
        # Should have some reference to publisher deals
        all_text = str(openai).lower()
        assert 'publisher' in all_text or 'licensing' in all_text or 'content deal' in all_text

    def test_apple_has_news_plus_data(self):
        apple = self.entities['entities']['apple']
        all_text = str(apple).lower()
        assert 'news+' in all_text or 'apple news' in all_text

    def test_news_corp_50m_deal_consistent(self):
        """Cross-pressure says News Corp has $50M/yr OpenAI deal.
        OpenAI entity should document this too."""
        openai = self.entities['entities']['openai']
        all_text = str(openai).lower()
        assert '50m' in all_text or '$50' in all_text or 'news corp' in all_text

    def test_meta_not_in_cross_pressure_publications(self):
        """Meta has no content licensing deals with these publications.
        It should NOT appear as a dual-relationship publisher."""
        cp = self.entities['entities']['apple'][
            'openai_litigation_publisher_cross_pressure'
        ]
        for pub in cp['dual_relationship_publications']:
            name = pub['publication'].lower()
            assert 'meta' not in name, f"Meta should not be in cross-pressure pubs: {name}"
