"""
Type D: Test & Verify — 07:00 PT Aug 8 Cross-Validation Suite

Validates structural fixes from the 07:00 PT iteration:
1. Cross-publication findings correctly placed under cross_publication_findings key
   (NOT under publications, which caused test_competitor_coverage and
   test_financial_relationships failures)
2. All source URLs use HTTPS (Shacknews HTTP→HTTPS fix in competitor-entities.yaml)
3. YAML structural integrity after automated migration
4. Cross-publication findings schema completeness
5. No publication-key pollution from non-publication entries
"""

import pytest
import yaml
import os
import glob
import re
from pathlib import Path

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return yaml.safe_load(f)


# =====================================================================
# CLASS 1: Publications Key Integrity
# =====================================================================

class TestPublicationsKeyIntegrity:
    """Verify publications key contains only actual publication profiles."""

    VALID_PUBLICATION_SLUGS = {
        'wired', 'the-verge', 'atlantic', 'nytimes', 'financial-times',
        'guardian', 'mit-tech-review', 'gizmodo', 'news-corp', 'financial_times'
    }

    def test_no_cross_publication_findings_in_publications(self):
        """Cross-publication findings must NOT appear under publications key."""
        data = load_yaml('competitor-coverage-research.yaml')
        pubs = set(data.get('publications', {}).keys())
        cross_pub_patterns = [
            'nyt_google_q2_2026',
            'google_showcase',
            'advance_dual_asset',
        ]
        for key in pubs:
            for pattern in cross_pub_patterns:
                assert pattern not in key, \
                    f"Cross-publication finding '{key}' incorrectly placed under publications"

    def test_publications_only_contain_known_slugs(self):
        """Publications key should only contain known publication slugs."""
        data = load_yaml('competitor-coverage-research.yaml')
        pubs = set(data.get('publications', {}).keys())
        assert pubs == self.VALID_PUBLICATION_SLUGS, \
            f"Unexpected publications: {pubs - self.VALID_PUBLICATION_SLUGS}"

    def test_each_publication_has_meta_coverage_tone(self):
        """Every publication must have meta_coverage_tone field."""
        data = load_yaml('competitor-coverage-research.yaml')
        for slug, pub_data in data['publications'].items():
            assert 'meta_coverage_tone' in pub_data, \
                f"{slug} missing meta_coverage_tone"

    def test_each_publication_has_asymmetry_verdict(self):
        """Every publication must have asymmetry_verdict field."""
        data = load_yaml('competitor-coverage-research.yaml')
        for slug, pub_data in data['publications'].items():
            assert 'asymmetry_verdict' in pub_data, \
                f"{slug} missing asymmetry_verdict"


# =====================================================================
# CLASS 2: Cross-Publication Findings Structure
# =====================================================================

class TestCrossPublicationFindings:
    """Verify cross_publication_findings key exists and is well-formed."""

    EXPECTED_FINDINGS = {
        'nyt_google_q2_2026_traffic_cannibalization_paradox',
        'google_showcase_coercive_cycle',
        'advance_dual_asset_monetization',
    }

    def test_cross_publication_findings_key_exists(self):
        """cross_publication_findings should be a top-level key."""
        data = load_yaml('competitor-coverage-research.yaml')
        assert 'cross_publication_findings' in data, \
            "Missing cross_publication_findings top-level key"

    def test_expected_findings_present(self):
        """All three Aug 8 cross-publication findings should exist."""
        data = load_yaml('competitor-coverage-research.yaml')
        findings = set(data['cross_publication_findings'].keys())
        for expected in self.EXPECTED_FINDINGS:
            assert expected in findings, f"Missing finding: {expected}"

    def test_each_finding_has_summary(self):
        """Each cross-publication finding must have a finding_summary."""
        data = load_yaml('competitor-coverage-research.yaml')
        for key, finding in data['cross_publication_findings'].items():
            assert 'finding_summary' in finding, \
                f"{key} missing finding_summary"
            assert len(finding['finding_summary']) > 50, \
                f"{key} finding_summary too short"

    def test_each_finding_has_test_file(self):
        """Each finding should reference its test file."""
        data = load_yaml('competitor-coverage-research.yaml')
        for key, finding in data['cross_publication_findings'].items():
            assert 'test_file' in finding, f"{key} missing test_file"
            test_path = os.path.join(
                os.path.dirname(__file__), '..', finding['test_file']
            )
            assert os.path.exists(test_path), \
                f"{key} references non-existent test: {finding['test_file']}"

    def test_each_finding_has_date(self):
        """Each finding should have a date_added."""
        data = load_yaml('competitor-coverage-research.yaml')
        for key, finding in data['cross_publication_findings'].items():
            assert 'date_added' in finding, f"{key} missing date_added"

    def test_nyt_google_has_key_evidence(self):
        """NYT-Google cannibalization finding must have key_evidence."""
        data = load_yaml('competitor-coverage-research.yaml')
        finding = data['cross_publication_findings']['nyt_google_q2_2026_traffic_cannibalization_paradox']
        assert 'key_evidence' in finding
        assert len(finding['key_evidence']) >= 3

    def test_google_showcase_has_mechanisms(self):
        """Google Showcase finding must quantify coercion mechanisms."""
        data = load_yaml('competitor-coverage-research.yaml')
        finding = data['cross_publication_findings']['google_showcase_coercive_cycle']
        assert 'google_coercion_mechanisms' in finding
        assert finding['google_coercion_mechanisms'] >= 5
        assert 'meta_coercion_mechanisms' in finding
        assert finding['meta_coercion_mechanisms'] == 0

    def test_advance_dual_asset_has_entities(self):
        """Advance dual-asset finding must list involved entities."""
        data = load_yaml('competitor-coverage-research.yaml')
        finding = data['cross_publication_findings']['advance_dual_asset_monetization']
        assert 'entities_involved' in finding
        entities = finding['entities_involved']
        assert any('Reddit' in e for e in entities)
        assert any('Condé Nast' in e or 'Conde Nast' in e for e in entities)


# =====================================================================
# CLASS 3: Source URL HTTPS Enforcement
# =====================================================================

class TestSourceURLHTTPS:
    """All source URLs across all profiles must use HTTPS."""

    def _collect_urls(self, obj, path=""):
        """Recursively collect all URL strings from a YAML structure."""
        urls = []
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, str) and v.startswith('http'):
                    urls.append((f"{path}.{k}", v))
                else:
                    urls.extend(self._collect_urls(v, f"{path}.{k}"))
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                if isinstance(item, str) and item.startswith('http'):
                    urls.append((f"{path}[{i}]", item))
                else:
                    urls.extend(self._collect_urls(item, f"{path}[{i}]"))
        return urls

    def test_competitor_entities_all_https(self):
        """All URLs in competitor-entities.yaml must be HTTPS."""
        data = load_yaml('competitor-entities.yaml')
        urls = self._collect_urls(data)
        non_https = [(path, url) for path, url in urls if url.startswith('http://')]
        assert not non_https, \
            f"Non-HTTPS URLs in competitor-entities.yaml: {non_https}"

    def test_competitor_research_all_https(self):
        """All URLs in competitor-coverage-research.yaml must be HTTPS."""
        data = load_yaml('competitor-coverage-research.yaml')
        urls = self._collect_urls(data)
        non_https = [(path, url) for path, url in urls if url.startswith('http://')]
        assert not non_https, \
            f"Non-HTTPS URLs in competitor-coverage-research.yaml: {non_https}"

    def test_advance_shacknews_url_fixed(self):
        """Specific regression: Shacknews URL must be HTTPS (was HTTP)."""
        data = load_yaml('competitor-entities.yaml')
        urls = self._collect_urls(data)
        shacknews_urls = [url for _, url in urls if 'shacknews.com' in url]
        for url in shacknews_urls:
            assert url.startswith('https://'), \
                f"Shacknews URL still HTTP: {url}"


# =====================================================================
# CLASS 4: YAML Top-Level Structure
# =====================================================================

class TestYAMLTopLevelStructure:
    """Validate top-level keys of key YAML files."""

    def test_research_yaml_top_keys(self):
        """competitor-coverage-research.yaml must have expected top-level keys."""
        data = load_yaml('competitor-coverage-research.yaml')
        required = {'publications', 'aggregate_findings', 'research_period'}
        for key in required:
            assert key in data, f"Missing top-level key: {key}"

    def test_research_yaml_has_cross_publication_findings(self):
        """cross_publication_findings should be top-level after migration."""
        data = load_yaml('competitor-coverage-research.yaml')
        assert 'cross_publication_findings' in data

    def test_no_duplicate_findings_across_sections(self):
        """Findings should not appear in both publications and cross_publication_findings."""
        data = load_yaml('competitor-coverage-research.yaml')
        pub_keys = set(data.get('publications', {}).keys())
        cross_keys = set(data.get('cross_publication_findings', {}).keys())
        overlap = pub_keys & cross_keys
        assert not overlap, f"Keys appear in both sections: {overlap}"


# =====================================================================
# CLASS 5: Test File Count Integrity
# =====================================================================

class TestFileCountIntegrity:
    """Verify test file counts haven't regressed."""

    def test_minimum_test_files(self):
        """Should have at least 224 test files."""
        test_dir = os.path.dirname(__file__)
        test_files = glob.glob(os.path.join(test_dir, 'test_*.py'))
        assert len(test_files) >= 224, \
            f"Only {len(test_files)} test files, expected >= 224"

    def test_structural_consistency_exists(self):
        """Core structural consistency test must exist."""
        path = os.path.join(os.path.dirname(__file__), 'test_structural_consistency.py')
        assert os.path.exists(path)

    def test_all_aug8_test_files_exist(self):
        """All test files created on Aug 8 should exist."""
        expected = [
            'test_atlantic_wong_cross_entity_framing_aug8.py',
            'test_type_d_03am_cross_validation_aug8.py',
            'test_google_showcase_coercive_cycle_aug8.py',
            'test_advance_dual_asset_monetization_aug8.py',
            'test_nyt_google_traffic_cannibalization_paradox_aug8.py',
            'test_type_d_07am_cross_validation_aug8.py',
        ]
        test_dir = os.path.dirname(__file__)
        for f in expected:
            assert os.path.exists(os.path.join(test_dir, f)), f"Missing: {f}"
