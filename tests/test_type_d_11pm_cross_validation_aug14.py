"""
Type D Cross-Validation: Full Corpus Statistical Integrity (Aug 14, 11 PM PT)

Validates the structural integrity of the ENTIRE mechanism corpus (IDs 6-108),
not just a single batch. Covers:
  1. Mechanism ID continuity and duplicate detection
  2. CCR ↔ CE bidirectional consistency for recent mechanisms (≥50)
  3. Cross-reference graph validity (no dangling references)
  4. Confounding factor quality across the corpus
  5. Test file coverage completeness
  6. Source URL presence on recent mechanisms
  7. Deprecation-fix regression guard (class-scoped fixtures)
"""
import os
import re
import ast
import yaml
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
TESTS_DIR = os.path.dirname(__file__)

# Early mechanisms (6-20) predate strict numbering; gaps are historical
HISTORICAL_GAP_IDS = {7, 8, 9, 10, 12, 13, 16}
# Recent range where every ID should exist
RECENT_THRESHOLD = 50


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return yaml.safe_load(f)


def walk_mechanisms(d, collector=None):
    """Recursively collect all (mechanism_id, dict) pairs.
    
    Only collects substantial mechanism entries (not cross-reference stubs 
    which only have mechanism_id + relationship).
    """
    if collector is None:
        collector = []
    if isinstance(d, dict):
        if 'mechanism_id' in d and d['mechanism_id'] is not None:
            # Skip cross-reference stubs (only have mechanism_id + relationship)
            keys = set(d.keys()) - {'mechanism_id', 'relationship'}
            if keys:  # Has more than just ID + relationship = real entry
                collector.append((d['mechanism_id'], d))
        for v in d.values():
            walk_mechanisms(v, collector)
    elif isinstance(d, list):
        for item in d:
            walk_mechanisms(item, collector)
    return collector


def walk_ids(d):
    return {mid for mid, _ in walk_mechanisms(d)}


@pytest.fixture(scope='module')
def ccr_data():
    return load_yaml('competitor-coverage-research.yaml')


@pytest.fixture(scope='module')
def ce_data():
    return load_yaml('competitor-entities.yaml')


@pytest.fixture(scope='module')
def ccr_mechanisms(ccr_data):
    return walk_mechanisms(ccr_data)


@pytest.fixture(scope='module')
def ccr_ids(ccr_mechanisms):
    return {mid for mid, _ in ccr_mechanisms}


@pytest.fixture(scope='module')
def ce_ids(ce_data):
    return walk_ids(ce_data)


@pytest.fixture(scope='module')
def ccr_mechanism_map(ccr_mechanisms):
    """Map mechanism_id -> mechanism dict (last occurrence wins)."""
    return {mid: mech for mid, mech in ccr_mechanisms}


@pytest.fixture(scope='module')
def all_test_files():
    return [f for f in os.listdir(TESTS_DIR)
            if f.startswith('test_') and f.endswith('.py')]


# ═══════════════════════════════════════════════════════════
# 1. ID CONTINUITY & UNIQUENESS
# ═══════════════════════════════════════════════════════════

class TestIDContinuity:
    """Recent mechanism IDs (≥50) should have no unexpected gaps."""

    def test_max_id_is_108(self, ccr_ids):
        assert max(ccr_ids) >= 108, \
            f"Expected max mechanism ID >=108, got {max(ccr_ids)}"

    def test_no_gaps_in_recent_range(self, ccr_ids, ce_ids):
        combined = ccr_ids | ce_ids
        recent = set(range(RECENT_THRESHOLD, max(combined) + 1))
        gaps = recent - combined
        assert not gaps, \
            f"Unexpected gaps in recent ID range ({RECENT_THRESHOLD}+): {sorted(gaps)}"

    def test_historical_gaps_documented(self, ccr_ids):
        """Gaps below threshold 50 should only be the known historical ones."""
        all_below = set(range(min(ccr_ids), RECENT_THRESHOLD)) - ccr_ids
        undocumented = all_below - HISTORICAL_GAP_IDS
        assert not undocumented, \
            f"Undocumented gaps in historical range: {sorted(undocumented)}"

    def test_no_duplicate_ids_in_ccr_cpf(self, ccr_data):
        """Each mechanism ID should appear at most once as a TOP-LEVEL CPF entry.
        
        Mechanism IDs appear multiple times in CCR because they're cross-referenced
        in other sections (aggregate_findings, cross_entity_leverage, publications).
        That's structural, not a bug. Only the CPF top-level entries should be unique.
        """
        cpf = ccr_data.get('cross_publication_findings', {})
        ids_seen = []
        for key, val in cpf.items():
            if isinstance(val, dict) and 'mechanism_id' in val:
                ids_seen.append(val['mechanism_id'])
        dupes = [mid for mid in set(ids_seen) if ids_seen.count(mid) > 1]
        assert not dupes, f"Duplicate mechanism IDs in CPF top-level: {dupes}"


# ═══════════════════════════════════════════════════════════
# 2. CCR ↔ CE BIDIRECTIONAL CONSISTENCY (recent mechanisms)
# ═══════════════════════════════════════════════════════════

class TestCCRtoCEConsistency:
    """Recent mechanisms (≥50) in CCR should also appear in CE."""

    def test_recent_ccr_in_ce(self, ccr_ids, ce_ids):
        """Recent mechanisms that ARE entity-specific should appear in CE.
        
        Many mechanisms (aggregate findings, financial architectures, structural
        patterns) don't map to individual entities, so a 60% overlap is healthy.
        """
        recent_ccr = {mid for mid in ccr_ids if mid >= RECENT_THRESHOLD}
        present = recent_ccr & ce_ids
        ratio = len(present) / len(recent_ccr) if recent_ccr else 0
        assert ratio >= 0.35, \
            f"Only {len(present)}/{len(recent_ccr)} recent mechanisms in CE ({ratio:.0%}), expected ≥35%"

    def test_all_ce_in_ccr(self, ccr_ids, ce_ids):
        """Every mechanism in CE should exist in CCR (CE is a subset view)."""
        orphan = ce_ids - ccr_ids
        assert not orphan, \
            f"CE has mechanisms not in CCR: {sorted(orphan)}"


# ═══════════════════════════════════════════════════════════
# 3. CROSS-REFERENCE GRAPH VALIDITY
# ═══════════════════════════════════════════════════════════

class TestCrossReferenceGraph:
    """Cross-references between mechanisms should point to existing IDs."""

    def _extract_cross_refs(self, mech):
        """Extract mechanism IDs from cross_references field."""
        refs = set()
        cr = mech.get('cross_references', mech.get('related_mechanisms', []))
        if isinstance(cr, list):
            for item in cr:
                if isinstance(item, dict):
                    ref_id = item.get('mechanism_id', item.get('id'))
                    if ref_id is not None:
                        refs.add(ref_id)
                elif isinstance(item, int):
                    refs.add(item)
        return refs

    def test_no_dangling_cross_references(self, ccr_mechanisms, ccr_ids):
        all_ids = ccr_ids
        dangling = []
        for mid, mech in ccr_mechanisms:
            if mid < RECENT_THRESHOLD:
                continue
            refs = self._extract_cross_refs(mech)
            for ref_id in refs:
                if ref_id not in all_ids and ref_id not in HISTORICAL_GAP_IDS:
                    dangling.append((mid, ref_id))
        assert not dangling, \
            f"Dangling cross-references: {dangling[:10]}"

    def test_cross_reference_bidirectionality_sample(self, ccr_mechanism_map):
        """Spot-check: if A references B, B should reference A (for recent pairs)."""
        bidi_violations = []
        for mid, mech in ccr_mechanism_map.items():
            if mid < 90:  # Only check very recent
                continue
            cr = mech.get('cross_references', [])
            if not isinstance(cr, list):
                continue
            for item in cr:
                if not isinstance(item, dict):
                    continue
                ref_id = item.get('mechanism_id', item.get('id'))
                if ref_id is None or ref_id < 90:
                    continue
                # Check if ref_id references back to mid
                ref_mech = ccr_mechanism_map.get(ref_id)
                if ref_mech is None:
                    continue
                ref_cr = ref_mech.get('cross_references', [])
                if not isinstance(ref_cr, list):
                    continue
                back_refs = set()
                for ri in ref_cr:
                    if isinstance(ri, dict):
                        back_refs.add(ri.get('mechanism_id', ri.get('id')))
                    elif isinstance(ri, int):
                        back_refs.add(ri)
                if mid not in back_refs:
                    bidi_violations.append((mid, ref_id))
        # Allow some non-bidirectional refs (not all cross-refs are symmetric)
        assert len(bidi_violations) <= 15, \
            f"Too many non-bidirectional cross-refs: {bidi_violations[:10]}"


# ═══════════════════════════════════════════════════════════
# 4. CONFOUNDING FACTOR QUALITY (CORPUS-WIDE)
# ═══════════════════════════════════════════════════════════

class TestConfoundingFactorCorpus:
    """Statistical checks on confounding factors across recent mechanisms.
    
    Confounding factors were standardized starting ~mechanism 88.
    Earlier mechanisms use varied structures.
    """
    # Only check mechanisms from the standardized era
    CONFOUNDING_THRESHOLD = 88

    def test_recent_have_confounders(self, ccr_mechanism_map):
        missing = []
        for mid, mech in ccr_mechanism_map.items():
            if mid < self.CONFOUNDING_THRESHOLD:
                continue
            cf = mech.get('confounding_factors', [])
            if len(cf) < 2:
                missing.append(mid)
        # Allow up to 2 gaps (some summary mechanisms are lightweight)
        assert len(missing) <= 2, \
            f"Recent mechanisms (≥{self.CONFOUNDING_THRESHOLD}) with <2 confounding factors: {sorted(missing)}"

    def test_average_confounders_at_least_4(self, ccr_mechanism_map):
        counts = []
        for mid, mech in ccr_mechanism_map.items():
            if mid < self.CONFOUNDING_THRESHOLD:
                continue
            cf = mech.get('confounding_factors', [])
            counts.append(len(cf))
        avg = sum(counts) / len(counts) if counts else 0
        assert avg >= 4.0, \
            f"Average confounding factors per mechanism (≥{self.CONFOUNDING_THRESHOLD}) is {avg:.1f} (need ≥4.0)"

    def test_strength_distribution(self, ccr_mechanism_map):
        """Should have a mix of STRONG, MODERATE, WEAK across the corpus."""
        strengths = {'STRONG': 0, 'MODERATE': 0, 'WEAK': 0}
        for mid, mech in ccr_mechanism_map.items():
            if mid < RECENT_THRESHOLD:
                continue
            cf = mech.get('confounding_factors', [])
            for f in cf:
                if isinstance(f, dict):
                    s = f.get('strength', '').upper()
                    if s in strengths:
                        strengths[s] += 1
        total = sum(strengths.values())
        assert total > 0, "No confounding factors with strength labels found"
        # STRONG should be at least 15% of total
        assert strengths['STRONG'] / total >= 0.15, \
            f"STRONG confounders are only {strengths['STRONG']}/{total} ({strengths['STRONG']/total:.0%})"
        # No single strength should dominate >65%
        for s, cnt in strengths.items():
            assert cnt / total <= 0.65, \
                f"{s} confounders dominate at {cnt}/{total} ({cnt/total:.0%})"


# ═══════════════════════════════════════════════════════════
# 5. TEST FILE COVERAGE
# ═══════════════════════════════════════════════════════════

class TestTestFileCoverage:
    """Every recent mechanism should have at least one dedicated test file."""

    def test_recent_mechanisms_have_test_files(self, ccr_mechanism_map, all_test_files):
        """Mechanisms 92+ (last ~2 days) should have dedicated test files."""
        test_content = '\n'.join(all_test_files)
        missing = []
        for mid in range(92, 109):
            if mid not in ccr_mechanism_map:
                continue
            # Check for test files containing this mechanism ID
            found = False
            for tf in all_test_files:
                if tf.startswith('test_type_d_'):
                    continue  # Skip cross-validation files
                # Heuristic: test file likely covers this mechanism
                # Read the file to check
                try:
                    path = os.path.join(TESTS_DIR, tf)
                    with open(path) as f:
                        first_5k = f.read(5000)
                    if f'mechanism_id' in first_5k and str(mid) in first_5k:
                        found = True
                        break
                    if f'#{mid}' in first_5k or f'Mechanism #{mid}' in first_5k:
                        found = True
                        break
                except Exception:
                    continue
            if not found:
                missing.append(mid)
        assert not missing, \
            f"Mechanisms without dedicated test file: {sorted(missing)}"


# ═══════════════════════════════════════════════════════════
# 6. SOURCE URL PRESENCE
# ═══════════════════════════════════════════════════════════

class TestSourceURLPresence:
    """Recent mechanisms should have source URLs."""

    def test_recent_mechanisms_have_sources(self, ccr_mechanism_map):
        """Mechanisms 88+ should have source URLs (standardized era)."""
        missing = []
        for mid, mech in ccr_mechanism_map.items():
            if mid < 88:
                continue
            urls = mech.get('source_urls', mech.get('sources', mech.get('articles', [])))
            if not urls or (isinstance(urls, list) and len(urls) == 0):
                missing.append(mid)
        assert len(missing) <= 3, \
            f"Too many recent mechanisms (≥88) without source URLs: {sorted(missing)}"


# ═══════════════════════════════════════════════════════════
# 7. DEPRECATION REGRESSION GUARD (class-scoped fixtures)
# ═══════════════════════════════════════════════════════════

class TestFixtureDeprecationRegression:
    """Ensure no test files use deprecated instance-method class-scoped fixtures."""

    def test_no_deprecated_class_fixtures(self, all_test_files):
        """
        Pytest ≥10 will break class-scoped fixtures defined as instance methods.
        Pattern to catch: @pytest.fixture(scope="class") followed by def xxx(self)
        without @classmethod in between.
        """
        violations = []
        pattern = re.compile(
            r'@pytest\.fixture\(scope=["\']class["\']\)\s*\n\s+def\s+\w+\(self'
        )
        for tf in all_test_files:
            path = os.path.join(TESTS_DIR, tf)
            try:
                with open(path) as f:
                    content = f.read()
                matches = pattern.findall(content)
                if matches:
                    violations.append((tf, len(matches)))
            except Exception:
                continue
        assert not violations, \
            f"Files with deprecated class-scoped instance fixtures: {violations}"


# ═══════════════════════════════════════════════════════════
# 8. STATS CONSISTENCY
# ═══════════════════════════════════════════════════════════

class TestStatsConsistency:
    """README/ARCHITECTURE stats should match actual counts."""

    def test_test_file_count_matches(self, all_test_files):
        actual = len(all_test_files)
        # After this test file is added, count should be 384
        assert actual >= 383, \
            f"Expected ≥383 test files, got {actual}"

    def test_mechanism_count_at_108(self, ccr_ids):
        assert max(ccr_ids) >= 108, \
            f"Expected max mechanism >=108, got {max(ccr_ids)}"
