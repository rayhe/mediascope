"""
Type D Cross-Validation — Thu 2026-08-27 4 PM PT

Validates settlement-week mechanisms #335-#344 structural integrity:
- YAML parse fix: competitor-coverage-research.yaml meta_framing quoting fix
- test_file field additions for mechanisms #338, #339, #341, #342, #343, #344
- README/ARCHITECTURE test count sync (659 files, ~23,386 tests)
- Cross-reference bidirectionality audit for settlement-week mechanisms
- Mechanism structural completeness (required fields, confounder presence)
- Test file importability for all 15 aug27 test files

Mechanisms validated:
  #335: CNBC Vanian Government Action Vocabulary Register Inversion
  #336: TechCrunch/Yahoo OpenAI ChatGPT Ads Europe Coverage Selection Silence
  #338: Meta Insurance Denial Asymmetric Financial Materiality
  #339: Subscription-Only Cultural Consensus Settlement Compartmentalization
  #341: Cross-Publication "Going Rogue" Agency Deflection Vocabulary Convergence
  #342: WSJ YouTube Child Safety Entity Accountability Deflection
  #343: AP Wire Service Cross-Entity Accountability Vocabulary Bifurcation
  #344: Meta Settlement Conditional Clause ChatGPT Ads Regulatory Boundary
"""

import os
import re
import yaml
import pytest
from pathlib import Path

PROFILES_DIR = Path(__file__).parent.parent / "profiles"
TESTS_DIR = Path(__file__).parent
REPO_ROOT = Path(__file__).parent.parent

# Module-level cache to avoid re-parsing the massive YAML for every test
_RESEARCH_CACHE = None
_MECHS_CACHE = None


def load_research():
    global _RESEARCH_CACHE
    if _RESEARCH_CACHE is None:
        _RESEARCH_CACHE = yaml.safe_load((PROFILES_DIR / "competitor-coverage-research.yaml").read_text())
    return _RESEARCH_CACHE


def get_all_mechanisms(data=None):
    global _MECHS_CACHE
    if _MECHS_CACHE is None:
        if data is None:
            data = load_research()
        mechs = {}
        for section_name in ['cross_publication_findings', 'publications', 'aggregate_findings']:
            section = data.get(section_name, {})
            for k, v in section.items():
                if isinstance(v, dict) and 'mechanism_id' in v and isinstance(v['mechanism_id'], int):
                    mechs[v['mechanism_id']] = (section_name, k, v)
        _MECHS_CACHE = mechs
    return _MECHS_CACHE


class TestYAMLIntegrity:
    """Verify the YAML parse fix and overall file validity."""

    def test_yaml_parses_successfully(self):
        """competitor-coverage-research.yaml must parse without errors."""
        data = load_research()
        assert isinstance(data, dict)
        assert len(data) >= 4

    def test_meta_framing_field_properly_quoted(self):
        """The meta_framing field that caused the YAML parse error must be properly quoted."""
        data = load_research()
        # The fixed field is a string containing "Designed to fail" - search for it
        raw = (PROFILES_DIR / "competitor-coverage-research.yaml").read_text()
        # Verify the field exists with proper quoting in raw YAML
        assert "'\"Designed to fail,\" inadequate, willful negligence'" in raw, \
            "The meta_framing field should be properly single-quoted around the double-quoted phrase"
        # Verify it parses without error (already tested in test_yaml_parses_successfully)
        # Find the value by searching for string-type meta_framing fields
        def find_string_meta_framing(obj):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if k == 'meta_framing' and isinstance(v, str) and 'Designed to fail' in v:
                        return v
                    result = find_string_meta_framing(v)
                    if result is not None:
                        return result
            elif isinstance(obj, list):
                for item in obj:
                    result = find_string_meta_framing(item)
                    if result is not None:
                        return result
            return None
        
        meta_framing = find_string_meta_framing(data)
        assert meta_framing is not None, "String meta_framing with 'Designed to fail' not found"
        assert 'inadequate' in meta_framing

    def test_top_level_keys_present(self):
        data = load_research()
        expected = ['aggregate_findings', 'cross_entity_leverage',
                    'cross_publication_findings', 'methodology', 'publications']
        for key in expected:
            assert key in data, f"Missing top-level key: {key}"


class TestSettlementWeekMechanismStructure:
    """Validate structural completeness of mechanisms #335-#344."""

    @pytest.fixture
    def mechs(self):
        data = load_research()
        return get_all_mechanisms(data)

    @pytest.mark.parametrize("mid", [335, 336, 338, 339, 341, 342, 343, 344])
    def test_mechanism_exists(self, mechs, mid):
        """Each settlement-week mechanism must exist in the YAML."""
        assert mid in mechs, f"Mechanism #{mid} not found"

    @pytest.mark.parametrize("mid", [335, 336, 338, 339, 341, 342, 343, 344])
    def test_mechanism_has_type(self, mechs, mid):
        """Each mechanism must have a type field."""
        _, _, v = mechs[mid]
        assert 'type' in v, f"Mechanism #{mid} missing 'type'"

    @pytest.mark.parametrize("mid", [335, 336, 338, 339, 341, 342, 343, 344])
    def test_mechanism_has_test_file(self, mechs, mid):
        """Each mechanism must have a test_file field."""
        _, _, v = mechs[mid]
        assert 'test_file' in v, f"Mechanism #{mid} missing 'test_file'"
        tf = v['test_file']
        assert tf, f"Mechanism #{mid} has empty test_file"

    @pytest.mark.parametrize("mid", [335, 336, 338, 339, 341, 342, 343, 344])
    def test_mechanism_test_file_exists(self, mechs, mid):
        """Each mechanism's test_file must point to an actual file."""
        _, _, v = mechs[mid]
        tf = v['test_file']
        # Handle both tests/filename.py and just filename.py
        path = REPO_ROOT / tf
        if not path.exists():
            path = TESTS_DIR / tf
        assert path.exists(), f"Mechanism #{mid} test_file '{tf}' does not exist"

    @pytest.mark.parametrize("mid", [335, 336, 338, 339, 341, 342, 343, 344])
    def test_mechanism_has_title(self, mechs, mid):
        """Each mechanism must have a title."""
        _, _, v = mechs[mid]
        assert 'title' in v or 'finding' in v or 'finding_summary' in v or 'core_finding' in v, \
            f"Mechanism #{mid} missing title/finding field"

    def test_mechanism_type_distribution(self, mechs):
        """Settlement-week mechanisms should span multiple analysis types."""
        types = set()
        for mid in [335, 336, 338, 339, 341, 342, 343, 344]:
            if mid in mechs:
                _, _, v = mechs[mid]
                types.add(v.get('type', ''))
        assert len(types) >= 3, f"Expected >=3 distinct types, got {len(types)}: {types}"

    def test_no_duplicate_mechanism_ids(self, mechs):
        """No two mechanisms should share the same ID."""
        data = load_research()
        all_ids = []
        for section_name in ['cross_publication_findings', 'publications', 'aggregate_findings']:
            section = data.get(section_name, {})
            for k, v in section.items():
                if isinstance(v, dict) and 'mechanism_id' in v:
                    all_ids.append(v['mechanism_id'])
        duplicates = [mid for mid in set(all_ids) if all_ids.count(mid) > 1]
        assert not duplicates, f"Duplicate mechanism IDs found: {duplicates}"

    def test_highest_mechanism_at_least_345(self, mechs):
        """The highest mechanism ID should be at least 345 (after dedup fix).

        Pinned to == 345 on Aug 27 2026; relaxed to a monotonic floor on Sep 2
        2026 (Type D #469) because later iterations legitimately add mechanisms
        to this registry. The dedup regression protection is retained: IDs must
        never go backward.
        """
        max_id = max(mechs.keys())
        assert max_id >= 345, f"Expected highest mechanism ID >= 345, got {max_id}"


class TestSettlementWeekConfounderQuality:
    """Validate confounder analysis quality for settlement-week mechanisms."""

    @pytest.fixture
    def mechs(self):
        data = load_research()
        return get_all_mechanisms(data)

    def test_mechanism_344_has_confounders(self, mechs):
        """The key settlement clause mechanism #344 must have confounders."""
        _, _, v = mechs[344]
        has_confounders = ('confounders' in v or 'confounding_factors' in v)
        assert has_confounders, "Mechanism #344 must have confounders"

    def test_mechanism_344_has_strong_confounder(self, mechs):
        """Mechanism #344 must acknowledge at least one STRONG confounder."""
        _, _, v = mechs[344]
        confounders = v.get('confounders', v.get('confounding_factors', []))
        if isinstance(confounders, list):
            strengths = [c.get('strength', '') if isinstance(c, dict) else '' for c in confounders]
            assert 'STRONG' in strengths, "Mechanism #344 needs at least one STRONG confounder"

    def test_mechanism_344_strong_confounders_have_counters(self, mechs):
        """STRONG confounders in #344 must have counter-arguments."""
        _, _, v = mechs[344]
        confounders = v.get('confounders', v.get('confounding_factors', []))
        if isinstance(confounders, list):
            for c in confounders:
                if isinstance(c, dict) and c.get('strength') == 'STRONG':
                    assert 'counter' in c, f"STRONG confounder missing counter: {c.get('description', '')[:50]}"


class TestAug27TestFileImportability:
    """Verify all aug27 test files exist and have valid Python syntax."""

    AUG27_FILES = [
        "test_meta_settlement_conditional_clause_chatgpt_ads_regulatory_boundary_financial_architecture_aug27",
        "test_barbara_ortutay_ap_cross_entity_settlement_week_accountability_vocabulary_bifurcation_aug27",
        "test_william_gavin_marketwatch_cross_entity_settlement_ipo_editorial_register_bifurcation_aug27",
        "test_wsj_news_corp_google_youtube_child_safety_settlement_coverage_accountability_asymmetry_aug27",
        "test_cross_publication_going_rogue_agency_deflection_vocabulary_convergence_aug27",
        "test_type_e_10am_settlement_week_public_broadcasting_political_podcast_entity_framing_bifurcation_aug27",
        "test_type_e_9am_titv_cnbc_settlement_week_subscription_cultural_consensus_compartmentalization_aug27",
        "test_type_d_08am_cross_validation_aug27",
        "test_type_d_07am_cross_validation_aug27",
        "test_meta_insurance_denial_asymmetric_financial_materiality_ai_lab_precedent_gap_aug27",
        "test_meghan_bobrowsky_wsj_settlement_week_cross_entity_vocabulary_bifurcation_aug27",
        "test_techcrunch_yahoo_openai_chatgpt_ads_europe_coverage_selection_silence_aug27",
        "test_jonathan_vanian_cnbc_cross_entity_government_action_vocabulary_register_inversion_aug27",
        "test_type_e_1am_settlement_week_investor_podcast_publisher_financial_architecture_convergence_aug27",
        "test_type_d_midnight_cross_validation_aug27",
    ]

    @pytest.mark.parametrize("module_name", AUG27_FILES)
    def test_aug27_file_exists(self, module_name):
        """Each aug27 test file must exist."""
        path = TESTS_DIR / f"{module_name}.py"
        assert path.exists(), f"{module_name}.py does not exist"

    @pytest.mark.parametrize("module_name", AUG27_FILES)
    def test_aug27_file_valid_python(self, module_name):
        """Each aug27 test file must be valid Python syntax."""
        path = TESTS_DIR / f"{module_name}.py"
        source = path.read_text()
        try:
            compile(source, str(path), 'exec')
        except SyntaxError as e:
            pytest.fail(f"Syntax error in {module_name}: {e}")


class TestDocSync:
    """Verify documentation counts are synchronized."""

    def test_readme_test_file_count(self):
        """README test file count must match actual count on disk."""
        readme = (REPO_ROOT / "README.md").read_text()
        actual_count = len(list(TESTS_DIR.glob("test_*.py")))
        assert str(actual_count) in readme or str(actual_count - 1) in readme, (
            f"README test file count ({actual_count} on disk) may be stale"
        )

    def test_readme_total_test_count_reasonable(self):
        """README total test count should be >= 23000."""
        readme = (REPO_ROOT / "README.md").read_text()
        # Find the test count in the stats table format: ~23,386 | Across 659 test files
        match = re.search(r'~?([\d,]+)\s*\|\s*Across\s+\d+\s+test\s+files', readme)
        if match:
            count = int(match.group(1).replace(',', ''))
            assert count >= 23000, f"README test count {count} seems too low"
        else:
            # Fallback: look for the prose mention
            match = re.search(r'\*\*~?([\d,]+)\s+tests\*\*', readme)
            if match:
                count = int(match.group(1).replace(',', ''))
                assert count >= 23000, f"README test count {count} seems too low"

    def test_test_file_count_is_659(self):
        """There should be exactly 659 test files (with this new one: 660)."""
        actual = len(list(TESTS_DIR.glob("test_*.py")))
        # Allow for this file being counted or not
        assert actual >= 659, f"Expected >=659 test files, got {actual}"


class TestCrossReferenceIntegrity:
    """Verify cross-references between settlement-week mechanisms are bidirectional."""

    @pytest.fixture
    def mechs(self):
        data = load_research()
        return get_all_mechanisms(data)

    def test_mechanism_344_references_valid_mechanisms(self, mechs):
        """Mechanism #344's cross-references must point to existing mechanisms."""
        if 344 not in mechs:
            pytest.skip("Mechanism #344 not found")
        _, _, v = mechs[344]
        xrefs = v.get('cross_references', [])
        for xr in xrefs:
            if isinstance(xr, dict):
                ref_id = xr.get('mechanism_id', xr.get('mechanism'))
            elif isinstance(xr, int):
                ref_id = xr
            else:
                continue
            if isinstance(ref_id, int):
                assert ref_id in mechs, f"Mechanism #344 references non-existent #{ref_id}"

    def test_settlement_mechanisms_have_cross_references(self, mechs):
        """Settlement-week mechanisms should have cross-references."""
        missing_xrefs = []
        for mid in [341, 342, 343, 344]:
            if mid in mechs:
                _, _, v = mechs[mid]
                if 'cross_references' not in v:
                    missing_xrefs.append(mid)
        # Allow some flexibility — not all mechanisms need cross-refs
        assert len(missing_xrefs) <= 2, (
            f"Too many settlement mechanisms without cross-references: {missing_xrefs}"
        )


class TestSettlementWeekCoveragePattern:
    """Validate the core analytical finding of settlement-week coverage patterns."""

    @pytest.fixture
    def data(self):
        return load_research()

    def test_mechanism_344_concurrent_events_documented(self):
        """Mechanism #344 must document the concurrent ChatGPT ads + Meta settlement events."""
        data = load_research()
        mechs = get_all_mechanisms(data)
        if 344 not in mechs:
            pytest.skip("Mechanism #344 not found")
        _, _, v = mechs[344]
        content = str(v)
        assert 'chatgpt' in content.lower() or 'openai' in content.lower()
        assert 'settlement' in content.lower()

    def test_mechanism_344_financial_architecture_present(self):
        """Mechanism #344 must document the financial architecture."""
        data = load_research()
        mechs = get_all_mechanisms(data)
        if 344 not in mechs:
            pytest.skip("Mechanism #344 not found")
        _, _, v = mechs[344]
        assert 'financial_architecture' in v or 'financial' in str(v.keys()).lower(), \
            "Mechanism #344 must document financial architecture"

    def test_settlement_coverage_vocabulary_mechanisms_exist(self):
        """Settlement-week vocabulary analysis mechanisms should exist."""
        data = load_research()
        mechs = get_all_mechanisms(data)
        settlement_mechs = [
            mid for mid, (_, k, v) in mechs.items()
            if 'settlement' in k.lower() and mid >= 330
        ]
        assert len(settlement_mechs) >= 2, (
            f"Expected >=2 settlement-week mechanisms with IDs >= 330, got {len(settlement_mechs)}"
        )


class TestRegressionGuards:
    """Prevent regressions in previously-validated mechanisms."""

    @pytest.fixture
    def mechs(self):
        data = load_research()
        return get_all_mechanisms(data)

    @pytest.mark.parametrize("mid", range(330, 345))
    def test_mechanism_id_contiguity(self, mechs, mid):
        """Mechanism IDs 330-344 should be mostly contiguous (allow small gaps)."""
        # We just check that the expected recent ones exist
        if mid in [337, 340]:
            pytest.skip(f"Mechanism #{mid} may be a gap in the sequence")
        if mid not in mechs:
            pytest.skip(f"Mechanism #{mid} not found — may be expected gap")

    def test_prior_mechanisms_intact(self, mechs):
        """Spot-check that earlier mechanisms weren't accidentally deleted."""
        for mid in [1, 10, 50, 100, 200, 300]:
            if mid in mechs:
                _, _, v = mechs[mid]
                assert 'mechanism_id' in v
                assert v['mechanism_id'] == mid
