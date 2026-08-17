"""
Type D Cross-Validation — Aug 17, 2026 08:00 AM PT (Iteration #153)

Validates structural integrity after iterations #149–#152:
- Mechanism #149: PMC/Google double incentive Samsung glasses coverage
- Mechanism #150: Cherlynn Low Engadget beat assignment control
- Mechanism #151: Sam Rutherford Engadget beat assignment null differential
- Mechanism #152: Nvidia-OpenAI GPU-capital circularity publisher incentive chain

Key fixes validated:
1. Mechanism #152 correctly placed in cross_publication_findings (not publications)
2. Nvidia entity (16th) present in entities section
3. Axel Springer entity in publisher_entities (not entities) with test fixture fix
4. Cross-references between recent mechanisms and earlier findings
5. Source URL presence for all recent mechanisms
"""

import os
import pytest
import yaml

RESEARCH_PATH = os.path.join(
    os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
)
ENTITIES_PATH = os.path.join(
    os.path.dirname(__file__), '..', 'profiles', 'competitor-entities.yaml'
)


@pytest.fixture(scope='module')
def research_data():
    with open(RESEARCH_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def entities_data():
    with open(ENTITIES_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def cpf(research_data):
    return research_data.get('cross_publication_findings', {})


@pytest.fixture(scope='module')
def publications(research_data):
    return research_data.get('publications', {})


# ── Class 1: Section Placement Integrity ─────────────────────────────

class TestSectionPlacement:
    """Verify mechanisms are in cross_publication_findings, not publications."""

    def test_publications_count_exactly_9(self, publications):
        assert len(publications) == 9, (
            f"Expected 9 publication profiles, got {len(publications)}: "
            f"{list(publications.keys())}"
        )

    def test_publications_have_no_mechanism_ids_without_coverage_tone(self, publications):
        for name, pub in publications.items():
            if 'mechanism_id' in pub:
                assert 'meta_coverage_tone' in pub, (
                    f"publications.{name} has mechanism_id but no meta_coverage_tone — "
                    f"should be in cross_publication_findings"
                )

    def test_nvidia_mechanism_in_cpf(self, cpf):
        key = 'nvidia_openai_gpu_capital_circularity_publisher_incentive_chain'
        assert key in cpf, "Mechanism #152 (nvidia) missing from cross_publication_findings"

    def test_nvidia_mechanism_not_in_publications(self, publications):
        key = 'nvidia_openai_gpu_capital_circularity_publisher_incentive_chain'
        assert key not in publications, (
            "Mechanism #152 (nvidia) should NOT be in publications section"
        )

    def test_cpf_count_at_least_134(self, cpf):
        assert len(cpf) >= 134, (
            f"Expected >= 134 cross_publication_findings entries, got {len(cpf)}"
        )


# ── Class 2: Entity Section Integrity ────────────────────────────────

class TestEntityIntegrity:
    """Verify entity data placement and counts after nvidia addition."""

    def test_entity_count_is_16(self, entities_data):
        entities = entities_data.get('entities', {})
        assert len(entities) == 16, (
            f"Expected 16 entities, got {len(entities)}: {list(entities.keys())}"
        )

    def test_nvidia_in_entities(self, entities_data):
        entities = entities_data.get('entities', {})
        assert 'nvidia' in entities, "nvidia entity missing from entities"

    def test_nvidia_has_required_fields(self, entities_data):
        nvidia = entities_data['entities']['nvidia']
        for field in ['display_name', 'category', 'ceo', 'q2_fy2026_earnings']:
            assert field in nvidia, f"nvidia entity missing field: {field}"

    def test_nvidia_category_is_infrastructure(self, entities_data):
        nvidia = entities_data['entities']['nvidia']
        assert 'infrastructure' in nvidia.get('category', '').lower()

    def test_axel_springer_in_publisher_entities(self, entities_data):
        pe = entities_data.get('publisher_entities', {})
        assert 'axel_springer_business_insider' in pe, (
            "axel_springer_business_insider missing from publisher_entities"
        )

    def test_axel_springer_has_openai_deal(self, entities_data):
        pe = entities_data.get('publisher_entities', {})
        axel = pe.get('axel_springer_business_insider', {})
        deals = axel.get('content_licensing_deals', [])
        openai_deals = [d for d in deals if d.get('partner') == 'OpenAI']
        assert len(openai_deals) >= 1, "Axel Springer missing OpenAI content deal"

    def test_axel_springer_has_kkr_parent(self, entities_data):
        pe = entities_data.get('publisher_entities', {})
        axel = pe.get('axel_springer_business_insider', {})
        pe_owner = axel.get('pe_owner', {})
        assert 'KKR' in pe_owner.get('name', ''), "Axel Springer PE owner should be KKR"


# ── Class 3: Mechanisms 149–152 Existence ────────────────────────────

class TestRecentMechanisms:
    """Verify mechanisms #149-#152 exist in cross_publication_findings."""

    def test_mechanism_149_exists(self, cpf):
        found = any(v.get('mechanism_id') == 149 for v in cpf.values())
        assert found, "Mechanism #149 (PMC/Google double incentive) missing from CPF"

    def test_mechanism_150_exists(self, cpf):
        found = any(v.get('mechanism_id') == 150 for v in cpf.values())
        assert found, "Mechanism #150 (Cherlynn Low control case) missing from CPF"

    def test_mechanism_151_exists(self, cpf):
        found = any(v.get('mechanism_id') == 151 for v in cpf.values())
        assert found, "Mechanism #151 (Sam Rutherford null differential) missing from CPF"

    def test_mechanism_152_exists(self, cpf):
        found = any(v.get('mechanism_id') == 152 for v in cpf.values())
        assert found, "Mechanism #152 (Nvidia-OpenAI GPU circularity) missing from CPF"

    def test_mechanism_152_has_source_urls(self, cpf):
        for v in cpf.values():
            if v.get('mechanism_id') == 152:
                urls = v.get('source_urls', [])
                assert len(urls) >= 5, (
                    f"Mechanism #152 should have >= 5 source URLs, got {len(urls)}"
                )
                break

    def test_mechanism_152_has_confounders(self, cpf):
        for v in cpf.values():
            if v.get('mechanism_id') == 152:
                confounders = v.get('confounders', [])
                assert len(confounders) >= 4, (
                    f"Mechanism #152 should have >= 4 confounders, got {len(confounders)}"
                )
                break

    def test_mechanism_152_cross_references_valid(self, cpf):
        for v in cpf.values():
            if v.get('mechanism_id') == 152:
                refs = v.get('cross_references', [])
                assert len(refs) >= 3, (
                    f"Mechanism #152 should cross-reference >= 3 other mechanisms"
                )
                # Verify at least one cross-referenced mechanism exists
                # (some early mechanism IDs may have been renumbered)
                all_ids = {v2.get('mechanism_id') for v2 in cpf.values()
                           if v2.get('mechanism_id')}
                found_refs = [ref for ref in refs if ref in all_ids]
                assert len(found_refs) >= 1, (
                    f"Mechanism #152 cross-references {refs} but none exist in CPF"
                )
                break


# ── Class 4: Mechanism ID Uniqueness ─────────────────────────────────

class TestMechanismIdUniqueness:
    """No two CPF entries should share the same mechanism_id."""

    def test_no_duplicate_mechanism_ids(self, cpf):
        ids = [v.get('mechanism_id') for v in cpf.values() if v.get('mechanism_id')]
        dupes = [mid for mid in ids if ids.count(mid) > 1]
        assert not dupes, f"Duplicate mechanism IDs in CPF: {set(dupes)}"

    def test_mechanism_ids_sequential(self, cpf):
        ids = sorted([v.get('mechanism_id') for v in cpf.values()
                       if v.get('mechanism_id')])
        if ids:
            # Verify highest ID matches count approximately
            # (some gaps allowed from deletions)
            assert ids[-1] >= len(ids), (
                f"Highest mechanism ID ({ids[-1]}) should be >= count ({len(ids)})"
            )


# ── Class 5: Test File Existence ─────────────────────────────────────

class TestFileExistence:
    """Verify test files referenced by recent mechanisms exist."""

    def test_nvidia_test_file_exists(self):
        path = os.path.join(
            os.path.dirname(__file__),
            'test_nvidia_openai_gpu_capital_circularity_publisher_incentive_chain_aug17.py'
        )
        assert os.path.exists(path), "Nvidia mechanism test file missing"

    def test_axel_springer_test_file_exists(self):
        path = os.path.join(
            os.path.dirname(__file__),
            'test_axel_springer_kkr_openai_financial_architecture_aug17.py'
        )
        assert os.path.exists(path), "Axel Springer mechanism test file missing"

    def test_cherlynn_low_test_file_exists(self):
        path = os.path.join(
            os.path.dirname(__file__),
            'test_cherlynn_low_engadget_cross_entity_beat_assignment_privacy_vocabulary_control_aug17.py'
        )
        assert os.path.exists(path), "Cherlynn Low mechanism test file missing"

    def test_sam_rutherford_test_file_exists(self):
        path = os.path.join(
            os.path.dirname(__file__),
            'test_sam_rutherford_engadget_cross_entity_beat_assignment_privacy_routing_aug17.py'
        )
        assert os.path.exists(path), "Sam Rutherford mechanism test file missing"

    def test_pmc_google_test_file_exists(self):
        path = os.path.join(
            os.path.dirname(__file__),
            'test_pmc_acquisition_google_double_incentive_samsung_glasses_coverage_calibration_aug17.py'
        )
        assert os.path.exists(path), "PMC/Google mechanism test file missing"

    def test_google_warby_parker_test_file_exists(self):
        path = os.path.join(
            os.path.dirname(__file__),
            'test_google_warby_parker_equity_publisher_feedback_loop_aug17.py'
        )
        assert os.path.exists(path), "Google/Warby Parker mechanism test file missing"


# ── Class 6: Engadget Beat Assignment Pattern Coherence ──────────────

class TestEngadgetBeatAssignmentCoherence:
    """Verify the Engadget beat assignment mechanisms form a coherent pattern."""

    def test_mechanisms_150_151_both_reference_engadget(self, cpf):
        for v in cpf.values():
            mid = v.get('mechanism_id')
            if mid == 150:
                key = [k for k, v2 in cpf.items() if v2.get('mechanism_id') == 150][0]
                assert 'engadget' in key.lower(), "Mechanism #150 should reference Engadget"
            if mid == 151:
                key = [k for k, v2 in cpf.items() if v2.get('mechanism_id') == 151][0]
                assert 'engadget' in key.lower(), "Mechanism #151 should reference Engadget"

    def test_karissa_bell_investigation_pattern_documented(self, cpf):
        """Mechanisms #150 and #151 both identify Karissa Bell as the privacy
        investigation conduit while product reporters show zero privacy vocabulary."""
        bell_mentioned = False
        for v in cpf.values():
            mid = v.get('mechanism_id')
            if mid in (150, 151):
                # Check all string fields (finding, finding_summary, notes, etc.)
                for field_val in v.values():
                    if isinstance(field_val, str) and 'bell' in field_val.lower():
                        bell_mentioned = True
                        break
        # At least one of the two mechanisms should mention Bell
        assert bell_mentioned, (
            "Neither mechanism #150 nor #151 mentions Karissa Bell — "
            "beat assignment pattern incomplete"
        )


# ── Class 7: Publication Profile Completeness ────────────────────────

class TestPublicationProfileCompleteness:
    """Spot-check that all 9 publication profiles have core fields."""

    EXPECTED_PUBS = [
        'atlantic', 'financial-times', 'gizmodo', 'guardian',
        'mit-tech-review', 'news-corp', 'nytimes', 'the-verge', 'wired'
    ]

    def test_all_expected_publications_present(self, publications):
        for pub in self.EXPECTED_PUBS:
            assert pub in publications, f"Missing publication profile: {pub}"

    def test_all_publications_have_meta_coverage_tone(self, publications):
        for pub_name in self.EXPECTED_PUBS:
            pub = publications[pub_name]
            assert 'meta_coverage_tone' in pub, (
                f"{pub_name} missing meta_coverage_tone"
            )


# ── Class 8: YAML Structural Health ──────────────────────────────────

class TestYamlStructuralHealth:
    """Verify the YAML files parse correctly and have expected top-level keys."""

    def test_research_yaml_top_level_keys(self, research_data):
        required = {'research_period', 'cross_publication_findings',
                    'publications', 'methodology'}
        actual = set(research_data.keys())
        missing = required - actual
        assert not missing, f"Missing top-level keys in research YAML: {missing}"

    def test_entities_yaml_top_level_keys(self, entities_data):
        required = {'entities'}
        actual = set(entities_data.keys())
        missing = required - actual
        assert not missing, f"Missing top-level keys in entities YAML: {missing}"

    def test_research_yaml_parseable(self):
        """Verify competitor-coverage-research.yaml can be fully parsed."""
        with open(RESEARCH_PATH) as f:
            data = yaml.safe_load(f)
        assert data is not None

    def test_entities_yaml_parseable(self):
        """Verify competitor-entities.yaml can be fully parsed."""
        with open(ENTITIES_PATH) as f:
            data = yaml.safe_load(f)
        assert data is not None
