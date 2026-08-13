"""Type D cross-validation — Aug 13, 9 AM PT

Validates integrity after iterations 83-85 (mechanisms #80-#82):

1. Samsung Unpacked cluster coherence: mechanisms #80 (Gizmodo 4-entity clean control),
   #81 (multi-journalist beat assignment paradox), and #77 (NYT coverage selection silence)
   form a linked cluster. Cross-validate that they reference each other correctly.

2. Revenue collapse spiral (#82) chains properly to pre-existing financial mechanisms
   (#58 Condé Nast Portfolio, #47 Google Ad Dependency, #41 Microsoft Septuple Leverage).

3. Mechanism ID contiguity 17-82 (no gaps).

4. Test file existence and minimum test counts for #80-#82.

5. Confounding factors documented for all three mechanisms (scholarly rigor check).

6. Source URL coverage: each mechanism has verifiable URLs.

7. Testable predictions exist for all three (falsifiability requirement).

8. No duplicate mechanism IDs across cross_publication_findings and aggregate_findings.

9. YAML structural integrity after 82 mechanisms (methodology key, not hypothesis).
"""

import os
import re
import sys

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_ROOT)


def load_research():
    with open(os.path.join(REPO_ROOT, 'profiles', 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def research():
    return load_research()


@pytest.fixture(scope='module')
def cpf(research):
    return research.get('cross_publication_findings', {})


@pytest.fixture(scope='module')
def agg(research):
    return research.get('aggregate_findings', {})


@pytest.fixture(scope='module')
def all_mechanisms(cpf, agg):
    mechs = {}
    for section in (cpf, agg):
        for key, m in section.items():
            if isinstance(m, dict) and 'mechanism_id' in m:
                mid = m['mechanism_id']
                if isinstance(mid, int):
                    mechs[mid] = m
    return mechs


# ===================================================================
# 1. Samsung Unpacked cluster cross-references
# ===================================================================

class TestSamsungUnpackedClusterCoherence:
    """Mechanisms #77, #80, #81 form the Samsung Unpacked analysis cluster.
    Each should reference the others via cross_references or related_mechanisms."""

    CLUSTER_IDS = {77, 80, 81}

    def _get_references(self, mechanism):
        """Extract all referenced mechanism IDs from a mechanism entry."""
        refs = set()
        for field in ('cross_references', 'related_mechanisms'):
            val = mechanism.get(field, [])
            if isinstance(val, list):
                for item in val:
                    if isinstance(item, int):
                        refs.add(item)
                    elif isinstance(item, dict) and 'mechanism_id' in item:
                        refs.add(item['mechanism_id'])
        return refs

    def test_mechanism_80_references_77(self, all_mechanisms):
        """Gizmodo 4-entity (#80) should reference NYT coverage selection (#77)."""
        m = all_mechanisms.get(80, {})
        refs = self._get_references(m)
        assert 77 in refs, (
            f"Mechanism #80 should cross-reference #77 (NYT Samsung silence). "
            f"Current refs: {refs}"
        )

    def test_mechanism_81_references_77(self, all_mechanisms):
        """Multi-journalist beat assignment (#81) should reference NYT coverage selection (#77)."""
        m = all_mechanisms.get(81, {})
        refs = self._get_references(m)
        assert 77 in refs, (
            f"Mechanism #81 should cross-reference #77 (NYT Samsung silence). "
            f"Current refs: {refs}"
        )

    def test_mechanism_81_references_80(self, all_mechanisms):
        """Multi-journalist beat assignment (#81) should reference 4-entity control (#80)."""
        m = all_mechanisms.get(81, {})
        refs = self._get_references(m)
        assert 80 in refs, (
            f"Mechanism #81 should cross-reference #80 (Gizmodo 4-entity control). "
            f"Current refs: {refs}"
        )

    def test_mechanism_80_references_74(self, all_mechanisms):
        """Gizmodo 4-entity (#80) should reference #74 (Snap Specs) as predecessor."""
        m = all_mechanisms.get(80, {})
        refs = self._get_references(m)
        assert 74 in refs, (
            f"Mechanism #80 extends Snap Specs analysis — should reference #74. "
            f"Current refs: {refs}"
        )

    def test_all_cluster_mechanisms_exist(self, all_mechanisms):
        for mid in self.CLUSTER_IDS:
            assert mid in all_mechanisms, f"Samsung cluster mechanism #{mid} missing"

    def test_cluster_mechanisms_share_samsung_unpacked_context(self, all_mechanisms):
        """All cluster mechanisms should mention Samsung Galaxy Unpacked or Samsung glasses."""
        for mid in self.CLUSTER_IDS:
            m = all_mechanisms[mid]
            summary = m.get('finding_summary', '')
            title = m.get('title', '')
            combined = (summary + title).lower()
            assert 'samsung' in combined, (
                f"Mechanism #{mid} in Samsung cluster but doesn't mention Samsung"
            )


# ===================================================================
# 2. Revenue collapse spiral (#82) financial chain validation
# ===================================================================

class TestRevenueCollapseSpiralChain:
    """Mechanism #82 should chain to pre-existing financial mechanisms."""

    def test_mechanism_82_exists(self, all_mechanisms):
        assert 82 in all_mechanisms, "Mechanism #82 (Revenue Collapse Spiral) missing"

    def test_references_conde_nast_portfolio(self, all_mechanisms):
        m = all_mechanisms.get(82, {})
        refs = set()
        for field in ('cross_references', 'related_mechanisms'):
            val = m.get(field, [])
            if isinstance(val, list):
                for item in val:
                    if isinstance(item, int):
                        refs.add(item)
                    elif isinstance(item, dict) and 'mechanism_id' in item:
                        refs.add(item['mechanism_id'])
        assert 58 in refs, (
            f"Mechanism #82 should reference #58 (Condé Nast Portfolio Dependency). "
            f"Current refs: {refs}"
        )

    def test_references_google_ad_dependency(self, all_mechanisms):
        m = all_mechanisms.get(82, {})
        refs = set()
        for field in ('cross_references', 'related_mechanisms'):
            val = m.get(field, [])
            if isinstance(val, list):
                for item in val:
                    if isinstance(item, int):
                        refs.add(item)
                    elif isinstance(item, dict) and 'mechanism_id' in item:
                        refs.add(item['mechanism_id'])
        assert 47 in refs, (
            f"Mechanism #82 should reference #47 (Google Ad Dependency Paradox). "
            f"Current refs: {refs}"
        )

    def test_references_microsoft_leverage(self, all_mechanisms):
        m = all_mechanisms.get(82, {})
        refs = set()
        for field in ('cross_references', 'related_mechanisms'):
            val = m.get(field, [])
            if isinstance(val, list):
                for item in val:
                    if isinstance(item, int):
                        refs.add(item)
                    elif isinstance(item, dict) and 'mechanism_id' in item:
                        refs.add(item['mechanism_id'])
        assert 41 in refs, (
            f"Mechanism #82 should reference #41 (Microsoft Septuple Leverage). "
            f"Current refs: {refs}"
        )

    def test_revenue_spiral_mentions_traffic_collapse(self, all_mechanisms):
        m = all_mechanisms.get(82, {})
        summary = m.get('finding_summary', '')
        assert 'traffic' in summary.lower() or 'revenue' in summary.lower(), (
            "Revenue collapse spiral must discuss traffic or revenue decline"
        )

    def test_has_conde_nast_deal_data(self, all_mechanisms):
        m = all_mechanisms.get(82, {})
        summary = m.get('finding_summary', '')
        assert 'condé nast' in summary.lower() or 'conde nast' in summary.lower(), (
            "Mechanism #82 must include Condé Nast as primary case study"
        )

    def test_has_quantified_traffic_data(self, all_mechanisms):
        """Revenue spiral should include quantified traffic decline evidence."""
        m = all_mechanisms.get(82, {})
        summary = m.get('finding_summary', '')
        # Should have percentage figures for traffic decline
        pct_pattern = re.compile(r'\d+%')
        matches = pct_pattern.findall(summary)
        assert len(matches) >= 3, (
            f"Mechanism #82 should cite multiple traffic decline percentages, "
            f"found {len(matches)}"
        )


# ===================================================================
# 3. Mechanism ID contiguity (17-82)
# ===================================================================

class TestMechanismContiguity:
    """No gaps in mechanism ID sequence from 17 to 82."""

    def test_no_gaps_in_mechanism_ids(self, all_mechanisms):
        expected = set(range(17, 83))
        present = set(all_mechanisms.keys())
        gaps = expected - present
        assert not gaps, (
            f"Missing mechanism IDs in contiguous range 17-82: {sorted(gaps)}"
        )

    def test_no_ids_above_82(self, all_mechanisms):
        above = {mid for mid in all_mechanisms if mid > 82}
        assert not above, (
            f"Mechanism IDs above 82 found (unexpected): {sorted(above)}"
        )


# ===================================================================
# 4. Test file existence and minimum counts for #80-82
# ===================================================================

class TestRecentMechanismTestFiles:
    """Each mechanism #80-82 must have a real test file with substantial tests."""

    @pytest.mark.parametrize("mid", [80, 81, 82])
    def test_mechanism_has_test_file(self, all_mechanisms, mid):
        m = all_mechanisms[mid]
        tf = m.get('test_file', '')
        assert tf, f"Mechanism #{mid} missing test_file field"
        full = os.path.join(REPO_ROOT, tf)
        assert os.path.isfile(full), f"Test file {tf} for mechanism #{mid} does not exist"

    @pytest.mark.parametrize("mid", [80, 81, 82])
    def test_test_file_has_test_classes(self, all_mechanisms, mid):
        m = all_mechanisms[mid]
        tf = m.get('test_file', '')
        if not tf:
            pytest.skip(f"No test_file for #{mid}")
        full = os.path.join(REPO_ROOT, tf)
        content = open(full).read()
        classes = re.findall(r'^class Test\w+', content, re.MULTILINE)
        assert len(classes) >= 3, (
            f"Mechanism #{mid} test file should have ≥3 test classes, "
            f"found {len(classes)}: {classes}"
        )

    @pytest.mark.parametrize("mid", [80, 81, 82])
    def test_test_file_has_minimum_test_methods(self, all_mechanisms, mid):
        m = all_mechanisms[mid]
        tf = m.get('test_file', '')
        if not tf:
            pytest.skip(f"No test_file for #{mid}")
        full = os.path.join(REPO_ROOT, tf)
        content = open(full).read()
        methods = re.findall(r'def test_\w+', content)
        assert len(methods) >= 10, (
            f"Mechanism #{mid} test file should have ≥10 test methods, "
            f"found {len(methods)}"
        )


# ===================================================================
# 5. Confounding factors for #80-82 (scholarly rigor)
# ===================================================================

class TestConfoundingFactorsDocumented:
    """Each mechanism must document at least 3 confounding factors
    with strength ratings (STRONG, MODERATE, WEAK)."""

    @pytest.mark.parametrize("mid", [80, 81, 82])
    def test_has_confounding_factors(self, all_mechanisms, mid):
        m = all_mechanisms[mid]
        cf = m.get('confounding_factors', [])
        assert len(cf) >= 3, (
            f"Mechanism #{mid} should have ≥3 confounding factors, has {len(cf)}"
        )

    @pytest.mark.parametrize("mid", [80, 81, 82])
    def test_confounding_factors_have_strength(self, all_mechanisms, mid):
        m = all_mechanisms[mid]
        cf = m.get('confounding_factors', [])
        for i, factor in enumerate(cf):
            if isinstance(factor, dict):
                assert 'strength' in factor, (
                    f"Mechanism #{mid} confounding factor {i} missing strength rating"
                )
                assert factor['strength'] in ('STRONG', 'MODERATE', 'WEAK'), (
                    f"Mechanism #{mid} factor {i} invalid strength: {factor.get('strength')}"
                )

    @pytest.mark.parametrize("mid", [80, 81, 82])
    def test_has_at_least_one_strong_confound(self, all_mechanisms, mid):
        """Scholarly rigor: every mechanism must honestly acknowledge at least
        one STRONG confounding factor."""
        m = all_mechanisms[mid]
        cf = m.get('confounding_factors', [])
        strong = [f for f in cf if isinstance(f, dict) and f.get('strength') == 'STRONG']
        assert len(strong) >= 1, (
            f"Mechanism #{mid} must acknowledge at least one STRONG confounding factor"
        )


# ===================================================================
# 6. Source URL coverage
# ===================================================================

class TestSourceURLs:
    """Each mechanism must have verifiable source URLs."""

    @pytest.mark.parametrize("mid", [80, 81, 82])
    def test_has_sources(self, all_mechanisms, mid):
        m = all_mechanisms[mid]
        sources = m.get('sources', m.get('source_urls', []))
        assert len(sources) >= 2, (
            f"Mechanism #{mid} should have ≥2 sources, has {len(sources)}"
        )

    @pytest.mark.parametrize("mid", [80, 81, 82])
    def test_sources_have_urls(self, all_mechanisms, mid):
        m = all_mechanisms[mid]
        sources = m.get('sources', [])
        for i, s in enumerate(sources):
            if isinstance(s, dict):
                url = s.get('url', '')
                assert url.startswith('http'), (
                    f"Mechanism #{mid} source {i} has invalid URL: {url}"
                )
            elif isinstance(s, str):
                assert s.startswith('http'), (
                    f"Mechanism #{mid} source {i} has invalid URL: {s}"
                )


# ===================================================================
# 7. Testable predictions (falsifiability)
# ===================================================================

class TestTestablePredictions:
    """Each mechanism must include testable predictions for falsifiability."""

    @pytest.mark.parametrize("mid", [80, 81, 82])
    def test_has_testable_predictions(self, all_mechanisms, mid):
        m = all_mechanisms[mid]
        preds = m.get('testable_predictions', [])
        assert len(preds) >= 2, (
            f"Mechanism #{mid} should have ≥2 testable predictions, has {len(preds)}"
        )

    @pytest.mark.parametrize("mid", [80, 81, 82])
    def test_predictions_are_specific(self, all_mechanisms, mid):
        m = all_mechanisms[mid]
        preds = m.get('testable_predictions', [])
        for i, p in enumerate(preds):
            text = p if isinstance(p, str) else p.get('prediction', p.get('text', ''))
            assert len(text) > 30, (
                f"Mechanism #{mid} prediction {i} too vague ({len(text)} chars)"
            )


# ===================================================================
# 8. No duplicate mechanism IDs
# ===================================================================

class TestNoDuplicateMechanismIDs:
    """No mechanism_id should appear in both cpf and agg sections."""

    def test_no_duplicates_across_sections(self, cpf, agg):
        cpf_ids = set()
        agg_ids = set()
        for key, m in cpf.items():
            if isinstance(m, dict) and 'mechanism_id' in m:
                cpf_ids.add(m['mechanism_id'])
        for key, m in agg.items():
            if isinstance(m, dict) and 'mechanism_id' in m:
                agg_ids.add(m['mechanism_id'])
        dupes = cpf_ids & agg_ids
        assert not dupes, (
            f"Mechanism IDs appear in BOTH cpf and agg: {sorted(dupes)}"
        )


# ===================================================================
# 9. YAML structural integrity
# ===================================================================

class TestYAMLIntegrity:
    """The research YAML must load cleanly and have expected top-level keys."""

    def test_yaml_loads(self, research):
        assert research is not None, "YAML failed to load"

    def test_has_cross_publication_findings(self, research):
        assert 'cross_publication_findings' in research

    def test_has_aggregate_findings(self, research):
        assert 'aggregate_findings' in research

    def test_has_methodology(self, research):
        assert 'methodology' in research

    def test_mechanism_count_minimum(self, all_mechanisms):
        assert len(all_mechanisms) >= 66, (
            f"Expected ≥66 mechanisms (17-82), found {len(all_mechanisms)}"
        )

    def test_date_added_format(self, all_mechanisms):
        """All date_added fields should be YYYY-MM-DD format."""
        date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
        for mid, m in all_mechanisms.items():
            d = m.get('date_added', '')
            if d:
                assert date_pattern.match(str(d)), (
                    f"Mechanism #{mid} date_added not YYYY-MM-DD format: {d}"
                )


# ===================================================================
# 10. Samsung Unpacked entity consistency
# ===================================================================

class TestSamsungEntityConsistency:
    """Samsung must be a documented entity in competitor-entities.yaml."""

    def test_samsung_in_competitor_entities(self):
        path = os.path.join(REPO_ROOT, 'profiles', 'competitor-entities.yaml')
        if not os.path.isfile(path):
            pytest.skip("competitor-entities.yaml not found")
        with open(path) as f:
            entities = yaml.safe_load(f)
        # Samsung should appear somewhere in the entities
        content = open(path).read().lower()
        assert 'samsung' in content, (
            "Samsung must be documented in competitor-entities.yaml given "
            "mechanisms #77, #80, #81 all analyze Samsung coverage"
        )

    def test_google_gemini_in_competitor_entities(self):
        """Google/Gemini should be documented given Samsung glasses use Gemini AI."""
        path = os.path.join(REPO_ROOT, 'profiles', 'competitor-entities.yaml')
        if not os.path.isfile(path):
            pytest.skip("competitor-entities.yaml not found")
        content = open(path).read().lower()
        assert 'google' in content, (
            "Google must be in competitor-entities.yaml"
        )


# ===================================================================
# 11. Revenue collapse mechanism #82 statistical rigor
# ===================================================================

class TestRevenueCollapseStatisticalRigor:
    """Mechanism #82 claims traffic decline percentages. Verify the sources
    section documents at least 4 distinct evidence sources."""

    def test_has_minimum_source_diversity(self, all_mechanisms):
        m = all_mechanisms.get(82, {})
        sources = m.get('sources', m.get('source_urls', []))
        assert len(sources) >= 4, (
            f"Revenue collapse spiral needs ≥4 diverse sources, has {len(sources)}"
        )

    def test_mentions_roger_lynch_admission(self, all_mechanisms):
        """The Condé Nast CEO admission is a key primary source."""
        m = all_mechanisms.get(82, {})
        summary = m.get('finding_summary', '')
        assert 'lynch' in summary.lower() or 'condé nast ceo' in summary.lower(), (
            "Mechanism #82 should cite Roger Lynch (Condé Nast CEO) admission"
        )

    def test_has_deal_count_data(self, all_mechanisms):
        """Should quantify the AI content licensing deal landscape."""
        m = all_mechanisms.get(82, {})
        summary = m.get('finding_summary', '')
        # Should mention deal counts
        assert 'deal' in summary.lower(), (
            "Mechanism #82 should discuss AI content licensing deals"
        )
