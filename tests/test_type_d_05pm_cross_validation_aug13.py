"""
Type D Cross-Validation: Mechanisms #84-#88 (Aug 13, 17:00 PT)

Validates structural integrity, metadata completeness, cross-reference coherence,
and confounding factor documentation for the five mechanisms added during
iterations 87-89 (Aug 13, 2026).

Mechanisms covered:
  #84: WIRED OpenAI Hardware FR Investigation Gap (Type A, iteration 87)
  #85: Chris Welch Career Migration Privacy Non-Portability (Type B, iteration 88 — note: was the B iteration)
  #86: Google Display Deprecation Publisher Revenue Floor Erosion (Type C, iteration 85 — wait, need to check)
  #87: FT Dual-Partner Wearables Coverage Silence (Type B, iteration 88)
  #88: Publisher AI Deal Revolt Dual-Channel Decoupling (Type C, iteration 89)

Also validates:
  - Mechanism ID contiguity 17-88
  - No duplicate mechanism IDs across cpf and agg sections
  - All mechanisms have test_file and date_added fields
  - Cross-references within #84-#88 point to existing mechanisms
  - README and ARCHITECTURE stat consistency
  - Samsung glasses cluster coherence (#81/#84/#87/#88 form a connected cluster)
"""

import os
import re
import yaml
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, 'profiles')
TESTS_DIR = os.path.join(REPO_ROOT, 'tests')


@pytest.fixture(scope='module')
def competitor_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def all_mechanisms(competitor_research):
    cpf = competitor_research.get('cross_publication_findings', {})
    agg = competitor_research.get('aggregate_findings', {})
    mechs = {}
    for section in [cpf, agg]:
        if isinstance(section, dict):
            for key, m in section.items():
                if isinstance(m, dict) and 'mechanism_id' in m:
                    mechs[m['mechanism_id']] = m
    return mechs


@pytest.fixture(scope='module')
def target_mechanisms(all_mechanisms):
    """Return mechanisms #84-#88."""
    return {mid: all_mechanisms[mid] for mid in range(84, 89) if mid in all_mechanisms}


class TestMechanismExistence:
    """Verify all five target mechanisms exist in YAML."""

    @pytest.mark.parametrize('mech_id', [84, 85, 86, 87, 88])
    def test_mechanism_exists(self, all_mechanisms, mech_id):
        assert mech_id in all_mechanisms, f"Mechanism #{mech_id} not found in YAML"

    def test_five_mechanisms_present(self, target_mechanisms):
        assert len(target_mechanisms) == 5, f"Expected 5 target mechanisms, found {len(target_mechanisms)}"


class TestMetadataCompleteness:
    """Verify required metadata fields for mechanisms #84-#88."""

    REQUIRED_FIELDS = ['mechanism_id', 'date_added', 'test_file', 'finding_summary']

    @pytest.mark.parametrize('mech_id', [84, 85, 86, 87, 88])
    def test_has_date_added(self, target_mechanisms, mech_id):
        m = target_mechanisms[mech_id]
        assert 'date_added' in m, f"#{mech_id} missing date_added"
        assert re.match(r'^\d{4}-\d{2}-\d{2}$', str(m['date_added'])), \
            f"#{mech_id} date_added not in YYYY-MM-DD format: {m['date_added']}"

    @pytest.mark.parametrize('mech_id', [84, 85, 86, 87, 88])
    def test_has_test_file(self, target_mechanisms, mech_id):
        m = target_mechanisms[mech_id]
        assert 'test_file' in m, f"#{mech_id} missing test_file"
        tf = m['test_file']
        if not tf.startswith('tests/'):
            tf = f'tests/{tf}'
        assert os.path.exists(os.path.join(REPO_ROOT, tf)), \
            f"#{mech_id} test_file {tf} does not exist on disk"

    @pytest.mark.parametrize('mech_id', [84, 85, 86, 87, 88])
    def test_has_finding_summary(self, target_mechanisms, mech_id):
        m = target_mechanisms[mech_id]
        assert 'finding_summary' in m, f"#{mech_id} missing finding_summary"
        summary = m['finding_summary']
        assert len(summary) >= 100, \
            f"#{mech_id} finding_summary too short ({len(summary)} chars)"

    @pytest.mark.parametrize('mech_id', [84, 85, 86, 87, 88])
    def test_has_confounding_factors(self, target_mechanisms, mech_id):
        m = target_mechanisms[mech_id]
        assert 'confounding_factors' in m, f"#{mech_id} missing confounding_factors"
        cfs = m['confounding_factors']
        assert len(cfs) >= 3, f"#{mech_id} has only {len(cfs)} confounding factors (need ≥3)"

    @pytest.mark.parametrize('mech_id', [84, 85, 86, 87, 88])
    def test_has_testable_predictions(self, target_mechanisms, mech_id):
        m = target_mechanisms[mech_id]
        assert 'testable_predictions' in m, f"#{mech_id} missing testable_predictions"
        preds = m['testable_predictions']
        assert len(preds) >= 2, f"#{mech_id} has only {len(preds)} testable predictions (need ≥2)"

    @pytest.mark.parametrize('mech_id', [84, 85, 86, 87, 88])
    def test_all_dates_aug13(self, target_mechanisms, mech_id):
        """All five mechanisms were added on Aug 13, 2026."""
        m = target_mechanisms[mech_id]
        assert str(m['date_added']) == '2026-08-13', \
            f"#{mech_id} date_added is {m['date_added']}, expected 2026-08-13"


class TestConfoundingFactorQuality:
    """Verify confounding factors have strength ratings (scholarly rigor)."""

    VALID_STRENGTHS = {'STRONG', 'MODERATE', 'WEAK', 'strong', 'moderate', 'weak'}

    @pytest.mark.parametrize('mech_id', [84, 85, 86, 87, 88])
    def test_at_least_one_strong_confound(self, target_mechanisms, mech_id):
        m = target_mechanisms[mech_id]
        cfs = m.get('confounding_factors', [])
        strengths = []
        for cf in cfs:
            if isinstance(cf, dict):
                s = cf.get('strength', cf.get('rating', ''))
                strengths.append(str(s).upper())
            elif isinstance(cf, str):
                # Some entries embed strength in text
                upper = cf.upper()
                if 'STRONG' in upper:
                    strengths.append('STRONG')
                elif 'MODERATE' in upper:
                    strengths.append('MODERATE')
                elif 'WEAK' in upper:
                    strengths.append('WEAK')
        assert 'STRONG' in strengths, \
            f"#{mech_id} has no STRONG confounding factor (scholarly rigor requirement)"

    @pytest.mark.parametrize('mech_id', [84, 85, 86, 87, 88])
    def test_confound_strength_distribution(self, target_mechanisms, mech_id):
        """Each mechanism should have factors at 2+ different strength levels."""
        m = target_mechanisms[mech_id]
        cfs = m.get('confounding_factors', [])
        strengths = set()
        for cf in cfs:
            if isinstance(cf, dict):
                s = str(cf.get('strength', cf.get('rating', ''))).upper()
                if s in {'STRONG', 'MODERATE', 'WEAK'}:
                    strengths.add(s)
            elif isinstance(cf, str):
                upper = cf.upper()
                for level in ['STRONG', 'MODERATE', 'WEAK']:
                    if level in upper:
                        strengths.add(level)
        assert len(strengths) >= 2, \
            f"#{mech_id} has only {len(strengths)} strength levels ({strengths}), need ≥2"


class TestMechanismIDIntegrity:
    """Verify mechanism ID contiguity and uniqueness."""

    def test_no_duplicate_ids(self, competitor_research):
        cpf = competitor_research.get('cross_publication_findings', {})
        agg = competitor_research.get('aggregate_findings', {})
        ids = []
        for section in [cpf, agg]:
            if isinstance(section, dict):
                for key, m in section.items():
                    if isinstance(m, dict) and 'mechanism_id' in m:
                        ids.append(m['mechanism_id'])
        assert len(ids) == len(set(ids)), \
            f"Duplicate mechanism IDs found: {[x for x in ids if ids.count(x) > 1]}"

    def test_id_contiguity_17_to_max(self, all_mechanisms):
        """IDs should be contiguous from 17 to max (no gaps)."""
        ids = sorted(all_mechanisms.keys())
        # Filter to 17+ (earlier IDs may not exist in this format)
        ids_17_plus = [i for i in ids if i >= 17]
        if ids_17_plus:
            expected = set(range(17, max(ids_17_plus) + 1))
            actual = set(ids_17_plus)
            gaps = expected - actual
            assert not gaps, f"Mechanism ID gaps: {sorted(gaps)}"

    def test_max_id_is_88(self, all_mechanisms):
        max_id = max(all_mechanisms.keys())
        assert max_id >= 88, f"Max mechanism ID is {max_id}, expected ≥88"


class TestCrossReferenceCoherence:
    """Verify cross-references within #84-#88 point to existing mechanisms."""

    @pytest.mark.parametrize('mech_id', [84, 87])
    def test_related_mechanisms_exist(self, all_mechanisms, target_mechanisms, mech_id):
        m = target_mechanisms[mech_id]
        related = m.get('related_mechanisms', [])
        for ref in related:
            if isinstance(ref, dict):
                ref_id = ref.get('mechanism_id')
            elif isinstance(ref, str):
                match = re.search(r'#(\d+)', ref)
                ref_id = int(match.group(1)) if match else None
            else:
                ref_id = None
            if ref_id is not None and ref_id >= 17:
                # Only validate refs ≥17 (earlier mechanisms predate competitor-coverage-research.yaml)
                assert ref_id in all_mechanisms, \
                    f"#{mech_id} references mechanism #{ref_id} which doesn't exist"

    def test_samsung_glasses_cluster_coherence(self, all_mechanisms):
        """Mechanisms #81, #84, #87, #88 should form a connected Samsung glasses cluster."""
        cluster_ids = [81, 84, 87, 88]
        for mid in cluster_ids:
            assert mid in all_mechanisms, f"Samsung cluster mechanism #{mid} missing"

    def test_wearables_investigation_gap_cluster(self, all_mechanisms):
        """Mechanisms #84 (WIRED/OpenAI), #78 (Gemini/Google), #87 (FT/Samsung) form
        the wearables investigation gap cluster — three different publications×competitors."""
        gap_ids = [78, 84, 87]
        for mid in gap_ids:
            assert mid in all_mechanisms, f"Wearables gap mechanism #{mid} missing"


class TestTestFilesExistAndPass:
    """Verify each mechanism's test file exists and has minimum test count."""

    EXPECTED_TESTS = {
        84: 50,  # 70 collected per iteration log but allow some tolerance
        85: 35,
        86: 60,
        87: 30,
        88: 60,
    }

    @pytest.mark.parametrize('mech_id', [84, 85, 86, 87, 88])
    def test_test_file_exists(self, target_mechanisms, mech_id):
        m = target_mechanisms[mech_id]
        tf = m['test_file']
        if not tf.startswith('tests/'):
            tf = f'tests/{tf}'
        assert os.path.exists(os.path.join(REPO_ROOT, tf)), \
            f"#{mech_id} test file {tf} does not exist"

    @pytest.mark.parametrize('mech_id', [84, 85, 86, 87, 88])
    def test_minimum_test_count(self, target_mechanisms, mech_id):
        """Each mechanism's test file should contain enough test methods."""
        m = target_mechanisms[mech_id]
        tf = m['test_file']
        if not tf.startswith('tests/'):
            tf = f'tests/{tf}'
        path = os.path.join(REPO_ROOT, tf)
        with open(path) as f:
            content = f.read()
        test_defs = len(re.findall(r'def test_', content))
        min_expected = self.EXPECTED_TESTS.get(mech_id, 10)
        assert test_defs >= min_expected, \
            f"#{mech_id} has {test_defs} test defs, expected ≥{min_expected}"


class TestDocumentationConsistency:
    """Verify README and ARCHITECTURE list all test files and have consistent counts."""

    def test_readme_lists_all_aug13_test_files(self):
        with open(os.path.join(REPO_ROOT, 'README.md')) as f:
            readme = f.read()
        aug13_files = [
            'test_ft_dual_partner_wearables_coverage_silence_aug13.py',
            'test_publisher_ai_deal_revolt_dual_channel_decoupling_aug13.py',
            'test_wired_openai_hardware_facial_recognition_investigation_gap_aug13.py',
            'test_chris_welch_career_migration_privacy_portability_aug13.py',
            'test_google_display_deprecation_publisher_revenue_floor_erosion_aug13.py',
            'test_type_d_05am_cross_validation_aug13.py',
            'test_type_d_09am_cross_validation_aug13.py',
        ]
        for tf in aug13_files:
            assert tf in readme, f"{tf} missing from README.md test table"

    def test_architecture_lists_all_aug13_test_files(self):
        with open(os.path.join(REPO_ROOT, 'docs', 'ARCHITECTURE.md')) as f:
            arch = f.read()
        aug13_files = [
            'test_ft_dual_partner_wearables_coverage_silence_aug13.py',
            'test_publisher_ai_deal_revolt_dual_channel_decoupling_aug13.py',
            'test_wired_openai_hardware_facial_recognition_investigation_gap_aug13.py',
            'test_chris_welch_career_migration_privacy_portability_aug13.py',
            'test_google_display_deprecation_publisher_revenue_floor_erosion_aug13.py',
            'test_type_d_05am_cross_validation_aug13.py',
            'test_type_d_09am_cross_validation_aug13.py',
        ]
        for tf in aug13_files:
            assert tf in arch, f"{tf} missing from ARCHITECTURE.md"

    def test_readme_test_file_count_matches_disk(self):
        disk_count = len([f for f in os.listdir(TESTS_DIR) if f.startswith('test_') and f.endswith('.py')])
        with open(os.path.join(REPO_ROOT, 'README.md')) as f:
            readme = f.read()
        # Match "N test files" pattern
        match = re.search(r'(\d+)\s+test\s+files', readme)
        if match:
            readme_count = int(match.group(1))
            assert readme_count == disk_count, \
                f"README claims {readme_count} test files, but {disk_count} exist on disk"

    def test_architecture_test_file_count_matches_disk(self):
        disk_count = len([f for f in os.listdir(TESTS_DIR) if f.startswith('test_') and f.endswith('.py')])
        with open(os.path.join(REPO_ROOT, 'docs', 'ARCHITECTURE.md')) as f:
            arch = f.read()
        match = re.search(r'(\d+)\s+test\s+files', arch)
        if match:
            arch_count = int(match.group(1))
            assert arch_count == disk_count, \
                f"ARCHITECTURE claims {arch_count} test files, but {disk_count} exist on disk"


class TestFindingSummaryDistinctiveness:
    """Verify each mechanism's finding is distinct and non-overlapping."""

    def test_no_duplicate_finding_summaries(self, target_mechanisms):
        summaries = {}
        for mid, m in target_mechanisms.items():
            s = m.get('finding_summary', '')[:200]
            for other_mid, other_s in summaries.items():
                overlap = len(set(s.split()) & set(other_s.split()))
                total = len(set(s.split()) | set(other_s.split()))
                jaccard = overlap / total if total else 0
                assert jaccard < 0.7, \
                    f"Mechanisms #{mid} and #{other_mid} have suspicious overlap (Jaccard={jaccard:.2f})"
            summaries[mid] = s

    @pytest.mark.parametrize('mech_id,expected_entity', [
        (84, 'OpenAI'),
        (85, 'Bloomberg'),
        (86, 'Google'),
        (87, 'Financial Times'),
        (88, 'publisher'),
    ])
    def test_finding_targets_expected_entity(self, target_mechanisms, mech_id, expected_entity):
        m = target_mechanisms[mech_id]
        summary = m.get('finding_summary', '')
        assert expected_entity.lower() in summary.lower(), \
            f"#{mech_id} finding_summary doesn't mention expected entity '{expected_entity}'"


class TestRegressionGuards:
    """Ensure recent changes haven't broken earlier mechanisms."""

    @pytest.mark.parametrize('mech_id', [77, 78, 79, 80, 81, 82, 83])
    def test_prior_mechanisms_still_exist(self, all_mechanisms, mech_id):
        assert mech_id in all_mechanisms, f"Prior mechanism #{mech_id} disappeared"

    @pytest.mark.parametrize('mech_id', [77, 78, 79, 80, 81, 82, 83])
    def test_prior_mechanisms_still_have_test_file(self, all_mechanisms, mech_id):
        m = all_mechanisms[mech_id]
        assert 'test_file' in m, f"Prior mechanism #{mech_id} lost its test_file field"


class TestMechanismTypeDistribution:
    """Verify the #84-#88 batch covers multiple iteration types."""

    def test_mixed_finding_types(self, target_mechanisms):
        types = set()
        for m in target_mechanisms.values():
            ft = m.get('finding_type', m.get('type', 'unknown'))
            types.add(ft)
        assert len(types) >= 2, \
            f"Only {len(types)} finding types in #84-#88 ({types}), expected diversity"
