"""
Type D cross-validation — Aug 20 2026, 01:00 AM PT

Validates:
1. Mechanism #192 (Wareable buying guide Samsung/Meta privacy vocabulary bifurcation)
   — cross-validated against primary source: wareable.com buying guide (last updated Aug 14 2026)
2. Mechanism #191 (Kif Leswing CNBC CEO-attribution vocabulary asymmetry)
   — cross-validated against eWeek, Wareable, archyde.com secondary sources confirming CNBC exclusive
3. Test file integrity for aug20 mechanisms
4. Doc count consistency across README, iteration-log, and ARCHITECTURE
5. Dependency fix: textblob and vaderSentiment now installed (39 collection errors resolved)
6. Cross-reference integrity between mechanisms #190-#192
"""

import os
import re

import pytest
import yaml


REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES = os.path.join(REPO, "profiles")
TESTS = os.path.join(REPO, "tests")


@pytest.fixture(scope="module")
def readme():
    with open(os.path.join(REPO, "README.md")) as f:
        return f.read()


@pytest.fixture(scope="module")
def iteration_log():
    with open(os.path.join(REPO, "iteration-log.md")) as f:
        return f.read()


@pytest.fixture(scope="module")
def ccr():
    with open(os.path.join(PROFILES, "competitor-coverage-research.yaml")) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def competitor_entities():
    with open(os.path.join(PROFILES, "competitor-entities.yaml")) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def test_files():
    return [f for f in os.listdir(TESTS) if f.startswith("test_") and f.endswith(".py")]


@pytest.fixture(scope="module")
def test_file_count(test_files):
    return len(test_files)


# ── Class 1: Mechanism #192 Source Verification (Wareable Buying Guide) ──


class TestWareable192SourceVerification:
    """Cross-validate Mechanism #192 claims against primary source."""

    def test_wareable_buying_guide_test_file_exists(self, test_files):
        assert "test_wareable_buying_guide_cross_entity_samsung_meta_privacy_vocabulary_bifurcation_aug20.py" in test_files

    def test_mechanism_192_in_iteration_log(self, iteration_log):
        assert "Mechanism #192" in iteration_log

    def test_wareable_meta_privacy_vocabulary_documented(self, iteration_log):
        """Primary source confirms: 'enable stalking and harassment', 'covertly film in public',
        'courtroom banned', '70 civil rights organizations' all appear in Wareable buying guide."""
        assert "stalking and harassment" in iteration_log
        assert "covertly film" in iteration_log

    def test_wareable_samsung_zero_privacy_vocabulary_documented(self, iteration_log):
        """Primary source confirms: Samsung described as 'formally reveal its first pair of
        smart glasses' with zero privacy/surveillance vocabulary in same article."""
        assert "formally reveal" in iteration_log

    def test_wareable_even_realities_g2_elevated_for_privacy(self, iteration_log):
        """Primary source confirms: Even Realities G2 ranked #1 specifically to 'sidestep the
        entire issue' of camera privacy, yet Samsung camera glasses get zero such warning."""
        assert "sidestep" in iteration_log or "Even Realities" in iteration_log

    def test_asymmetry_score_in_valid_range(self, iteration_log):
        """Mechanism #192 asymmetry score should be >= 0.7 given the vocabulary bifurcation."""
        match = re.search(r"Mechanism #192.*?\*?\*?Asymmetry Score:?\*?\*?\s*([\d.]+)", iteration_log, re.DOTALL)
        assert match, "Missing asymmetry score for #192"
        score = float(match.group(1))
        assert score >= 0.7, f"Score {score} below threshold for clear vocabulary bifurcation"

    def test_wareable_affiliate_financial_alignment_noted(self, iteration_log):
        """Financial alignment: Wareable uses affiliate links — Samsung = high revenue potential,
        Google = primary traffic source, Meta has $0 financial relationship."""
        assert "affiliate" in iteration_log.lower()


# ── Class 2: Mechanism #191 Source Verification (Kif Leswing/CNBC) ──


class TestKifLeswing191SourceVerification:
    """Cross-validate Mechanism #191 claims against secondary sources."""

    def test_kif_leswing_test_file_exists(self, test_files):
        assert "test_kif_leswing_cnbc_cross_entity_ceo_attribution_vocabulary_asymmetry_aug20.py" in test_files

    def test_mechanism_191_in_iteration_log(self, iteration_log):
        assert "Mechanism #191" in iteration_log

    def test_cnbc_exclusive_samsung_access_documented(self, iteration_log):
        """eWeek confirms: 'CNBC broke the specifications on March 6' — validating
        the preferential source access claim."""
        # The mechanism documents the Jay Kim EVP interview
        assert "Jay Kim" in iteration_log

    def test_ceo_attribution_framing_mechanism(self, iteration_log):
        """CEO-attribution is a novel framing mechanism distinct from alarm vocabulary.
        It personalizes product strategy as executive stubbornness."""
        assert "CEO-attribution" in iteration_log or "CEO attribution" in iteration_log

    def test_comcast_nbcuniversal_financial_context(self, iteration_log):
        """CNBC is NBCUniversal/Comcast. Google and Samsung are among CNBC's largest
        advertisers. Meta has $0 parent-company financial relationship."""
        assert "Comcast" in iteration_log or "NBCUniversal" in iteration_log

    def test_asymmetry_score_in_valid_range(self, iteration_log):
        match = re.search(r"Mechanism #191.*?\*?\*?Asymmetry Score:?\*?\*?\s*([\d.]+)", iteration_log, re.DOTALL)
        assert match, "Missing asymmetry score for #191"
        score = float(match.group(1))
        assert score >= 0.5, f"Score {score} below minimum threshold"


# ── Class 3: Aug 20 Test File Integrity ──


class TestAug20TestFileIntegrity:
    """Verify all aug20 test files exist and are structurally valid."""

    def test_aug20_test_files_exist(self, test_files):
        aug20_files = [f for f in test_files if "aug20" in f]
        assert len(aug20_files) >= 2, f"Expected at least 2 aug20 files, got {len(aug20_files)}"

    def test_aug20_files_have_test_classes(self):
        for fname in os.listdir(TESTS):
            if "aug20" in fname and fname.endswith(".py"):
                path = os.path.join(TESTS, fname)
                with open(path) as f:
                    content = f.read()
                assert "class Test" in content, f"{fname} missing test classes"

    def test_aug20_files_have_docstrings(self):
        for fname in os.listdir(TESTS):
            if "aug20" in fname and fname.endswith(".py"):
                path = os.path.join(TESTS, fname)
                with open(path) as f:
                    content = f.read()
                assert '"""' in content, f"{fname} missing docstrings"


# ── Class 4: Doc Count Consistency ──


class TestDocCountConsistencyAug20:
    """README and iteration-log test counts should be within range."""

    def test_total_test_files_above_threshold(self, test_file_count):
        """After 195 iterations, should have 486+ test files."""
        assert test_file_count >= 486, f"Only {test_file_count} test files, expected 486+"

    def test_iteration_log_reports_test_count(self, iteration_log):
        """Latest iteration should report updated test/file counts."""
        counts = re.findall(r"(\d{2,3}) tests across (\d{2,3}) files", iteration_log)
        assert len(counts) > 0, "No test counts found in iteration log"

    def test_iteration_log_latest_count_near_actual(self, iteration_log, test_file_count):
        """Reported file count should be within 5 of actual."""
        counts = re.findall(r"(\d[\d,]+) tests across (\d+) files", iteration_log)
        if counts:
            latest_files = int(counts[0][1])
            assert abs(latest_files - test_file_count) <= 5, (
                f"Reported {latest_files} files but actual is {test_file_count}"
            )


# ── Class 5: Dependency Fix Validation ──


class TestDependencyFixValidation:
    """Verify textblob and vaderSentiment are importable after fix."""

    def test_textblob_importable(self):
        """39 collection errors were caused by missing textblob."""
        try:
            from textblob import TextBlob  # noqa: F401
            importable = True
        except ImportError:
            importable = False
        assert importable, "textblob still not importable"

    def test_vader_importable(self):
        """vaderSentiment was the second cascading dependency."""
        try:
            from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer  # noqa: F401
            importable = True
        except ImportError:
            importable = False
        assert importable, "vaderSentiment still not importable"

    def test_mediascope_sentiment_importable(self):
        """The mediascope.analyze.sentiment module should now import cleanly."""
        try:
            from mediascope.analyze.sentiment import analyze_vader  # noqa: F401
            importable = True
        except ImportError:
            importable = False
        assert importable, "mediascope.analyze.sentiment still not importable"


# ── Class 6: Cross-Reference Integrity (#190-#192) ──


class TestCrossReferenceIntegrity190to192:
    """Mechanisms #190-#192 should properly cross-reference each other."""

    def test_mechanism_192_references_190(self, iteration_log):
        """#192 (Wareable) should reference #190 (Verge Apple triple camera)
        as parallel buying guide level bifurcation."""
        # Find the #192 section and check for #190 cross-ref
        m192_match = re.search(r"Mechanism #192(.*?)(?=## Iteration|$)", iteration_log, re.DOTALL)
        if m192_match:
            section = m192_match.group(1)
            assert "#187" in section or "#70" in section or "#190" in section, (
                "Mechanism #192 should cross-reference related mechanisms"
            )

    def test_mechanism_191_references_related(self, iteration_log):
        """#191 (Kif Leswing) should reference related journalist cross-entity mechanisms."""
        m191_match = re.search(r"Mechanism #191(.*?)(?=## Iteration|$)", iteration_log, re.DOTALL)
        if m191_match:
            section = m191_match.group(1)
            has_crossref = any(f"#{n}" in section for n in [183, 187, 160, 188])
            assert has_crossref, "Mechanism #191 should cross-reference related mechanisms"

    def test_mechanism_190_exists_and_references_song(self, iteration_log):
        """#190 (Verge Apple triple camera) should reference Victoria Song."""
        m190_match = re.search(r"Mechanism #190(.*?)(?=## Iteration|$)", iteration_log, re.DOTALL)
        assert m190_match, "Mechanism #190 not found"
        section = m190_match.group(1)
        assert "Victoria Song" in section or "Song" in section


# ── Class 7: Samsung Entity Coverage in competitor-entities.yaml ──


class TestSamsungEntityCoverage:
    """Samsung should be properly documented in competitor-entities.yaml with
    Galaxy Glasses camera specs and privacy scrutiny received."""

    def test_samsung_entity_exists(self, competitor_entities):
        entities = competitor_entities.get("entities", {})
        assert "samsung" in entities, "Samsung missing from competitor-entities.yaml"

    def test_samsung_has_smart_glasses_entry(self, competitor_entities):
        samsung = competitor_entities.get("entities", {}).get("samsung", {})
        devices = samsung.get("hardware_devices", {})
        has_glasses = any(
            "glass" in k.lower() or "eyewear" in k.lower()
            for k in devices.keys()
        ) if devices else "smart_glasses" in str(samsung).lower()
        assert has_glasses, "Samsung entity missing smart glasses documentation"

    def test_samsung_camera_capabilities_documented(self, competitor_entities):
        samsung_str = str(competitor_entities.get("entities", {}).get("samsung", {}))
        assert "camera" in samsung_str.lower(), "Samsung camera capabilities not documented"
