"""Structural consistency tests — guards against doc/code count drift.

These tests verify that counts referenced in documentation match the
actual code.  When a new framing device, banned phrase, or other counted
feature is added, the corresponding documentation constant and these
guards must be updated together.

Added: 2026-06-27 12:00 PT, Type D iteration.
"""

import re
import subprocess
import sys
from pathlib import Path

import pytest

from mediascope.analyze.framing import detect_framing_devices, FramingDevice

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_REPO_ROOT = Path(__file__).resolve().parent.parent


def _all_device_types_from_code() -> set[str]:
    """Extract every unique device_type the framing module can produce."""
    src = (_REPO_ROOT / "mediascope" / "analyze" / "framing.py").read_text()

    # Keys assigned to _DEVICE_PATTERNS (initial dict + dynamic additions)
    pattern_keys = set(re.findall(r'_DEVICE_PATTERNS\["(\w+)"\]', src))
    initial_keys = set(re.findall(r'"(\w+)":\s*_[A-Z_]+_PATTERNS', src))
    # Post-pass structural types assigned via device_type="..."
    post_pass = set(re.findall(r'device_type="(\w+)"', src))

    return initial_keys | pattern_keys | post_pass


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestFramingDeviceTypeCount:
    """Guard: total framing device types in code match documented count.

    When a new device type is added to framing.py, these tests will fail
    and list every file that needs its count updated.  The expected count
    is derived from code, so only the 'total' test assertion needs bumping.
    """

    # --- Update ONLY this constant when adding new device types ---
    EXPECTED_TOTAL = 49
    EXPECTED_PATTERN_MATCHED = 44  # core + extended (in _DEVICE_PATTERNS)
    EXPECTED_STRUCTURAL = {"kicker_framing", "analogy_stacking",
                           "speculative_framing", "trend_bundling",
                           "social_proof_amplification"}

    def test_total_device_types(self):
        """Code should define exactly EXPECTED_TOTAL unique device types."""
        types = _all_device_types_from_code()
        assert len(types) == self.EXPECTED_TOTAL, (
            f"Expected {self.EXPECTED_TOTAL} framing device types, got {len(types)}.\n"
            f"Types: {sorted(types)}\n"
            "If you added a new device, update EXPECTED_TOTAL above AND the docs:\n"
            "  - docs/METHODOLOGY.md §4.1 total and tier counts\n"
            "  - docs/ARCHITECTURE.md framing device list\n"
            "  - docs/AGENT_GUIDE.md detect_framing_devices description\n"
            "  - mediascope/cli.py analyze command docstring\n"
            "  - README.md (if framing count is mentioned)"
        )

    def test_pattern_matched_types(self):
        """Pattern-matched types (core + extended) count matches expectation."""
        src = (_REPO_ROOT / "mediascope" / "analyze" / "framing.py").read_text()
        pattern_keys = set(re.findall(r'_DEVICE_PATTERNS\["(\w+)"\]', src))
        initial_keys = set(re.findall(r'"(\w+)":\s*_[A-Z_]+_PATTERNS', src))
        pattern_types = initial_keys | pattern_keys
        assert len(pattern_types) == self.EXPECTED_PATTERN_MATCHED, (
            f"Expected {self.EXPECTED_PATTERN_MATCHED} pattern-matched device types, "
            f"got {len(pattern_types)}.\n"
            f"Types: {sorted(pattern_types)}"
        )

    def test_structural_post_pass_types(self):
        """Structural post-pass types should be exactly the known set."""
        src = (_REPO_ROOT / "mediascope" / "analyze" / "framing.py").read_text()
        pattern_keys = set(re.findall(r'_DEVICE_PATTERNS\["(\w+)"\]', src))
        initial_keys = set(re.findall(r'"(\w+)":\s*_[A-Z_]+_PATTERNS', src))
        post_pass = set(re.findall(r'device_type="(\w+)"', src))
        structural_only = post_pass - initial_keys - pattern_keys
        assert structural_only == self.EXPECTED_STRUCTURAL, (
            f"Unexpected structural types: {structural_only}"
        )

    def test_precedent_analogy_exists(self):
        """precedent_analogy must be a registered framing device type."""
        types = _all_device_types_from_code()
        assert "precedent_analogy" in types, (
            "precedent_analogy is missing from framing device types. "
            "It was added in the Reuters insurance-defense article iteration."
        )


class TestMainModuleEntryPoint:
    """Guard: `python -m mediascope` works as a CLI entry point."""

    def test_main_module_exists(self):
        """mediascope/__main__.py must exist."""
        main_path = _REPO_ROOT / "mediascope" / "__main__.py"
        assert main_path.exists(), (
            f"Missing {main_path}. Users cannot run `python -m mediascope`."
        )

    def test_main_module_imports_cli(self):
        """__main__.py must import the CLI entry point."""
        main_path = _REPO_ROOT / "mediascope" / "__main__.py"
        src = main_path.read_text()
        assert "from mediascope.cli import cli" in src, (
            "__main__.py should import `cli` from mediascope.cli"
        )

    def test_python_m_mediascope_help(self):
        """Running `python -m mediascope --help` should succeed."""
        result = subprocess.run(
            [sys.executable, "-m", "mediascope", "--help"],
            capture_output=True, text=True, timeout=30,
            cwd=str(_REPO_ROOT),
        )
        assert result.returncode == 0, (
            f"python -m mediascope --help failed:\n{result.stderr}"
        )
        assert "MediaScope" in result.stdout


class TestDocCountConsistency:
    """Guard: documented counts match across files.

    All documentation files must reference the same framing device count.
    The expected count string is derived from TestFramingDeviceTypeCount
    constants so there is exactly ONE place to update when types are added.
    """

    # Derived from the single source of truth above
    _EXPECTED_TOTAL = TestFramingDeviceTypeCount.EXPECTED_TOTAL
    _EXPECTED_EXTENDED = (_EXPECTED_TOTAL
                          - 10  # core devices (stable)
                          - len(TestFramingDeviceTypeCount.EXPECTED_STRUCTURAL))

    def test_architecture_device_count(self):
        """ARCHITECTURE.md framing device count matches code."""
        doc = (_REPO_ROOT / "docs" / "ARCHITECTURE.md").read_text()
        expected = f"**{self._EXPECTED_TOTAL} framing device types**"
        assert expected in doc, (
            f"ARCHITECTURE.md framing device count is stale. "
            f"Should contain '{expected}'."
        )

    def test_methodology_device_count(self):
        """METHODOLOGY.md framing device count matches code."""
        doc = (_REPO_ROOT / "docs" / "METHODOLOGY.md").read_text()
        expected = f"{self._EXPECTED_TOTAL} framing device types"
        assert expected in doc, (
            f"METHODOLOGY.md framing device count is stale. "
            f"Should contain '{expected}'."
        )

    def test_agent_guide_device_count(self):
        """AGENT_GUIDE.md framing device count matches code."""
        doc = (_REPO_ROOT / "docs" / "AGENT_GUIDE.md").read_text()
        expected = f"{self._EXPECTED_TOTAL} device types"
        assert expected in doc, (
            f"AGENT_GUIDE.md framing device count is stale. "
            f"Should contain '{expected}'."
        )

    def test_cli_analyze_device_count(self):
        """CLI analyze docstring framing device count matches code."""
        cli_src = (_REPO_ROOT / "mediascope" / "cli.py").read_text()
        expected = f"{self._EXPECTED_TOTAL} types"
        assert expected in cli_src, (
            f"CLI analyze command docstring framing device count is stale. "
            f"Should contain '{expected}'."
        )

    def test_readme_banned_phrases_count(self):
        """README.md must reference 25 total banned phrases."""
        doc = (_REPO_ROOT / "README.md").read_text()
        assert "25 total" in doc, (
            "README.md banned phrase count is stale. Should say '25 total'."
        )

    def test_readme_advance_voting_power(self):
        """README.md must reference 65.2% voting power (not stale 33.5%)."""
        doc = (_REPO_ROOT / "README.md").read_text()
        assert "33.5%" not in doc, (
            "README.md still references stale 33.5% Advance/Reddit voting power. "
            "Should be 65.2% per 2026 proxy / Schedule 13G."
        )
        assert "65.2%" in doc


class TestTopicBucketConsistency:
    """Guard: topic bucket counts match across code and docs."""

    def test_topic_count_in_code(self):
        """Code should define exactly 21 topic buckets."""
        from mediascope.analyze.topics import TOPIC_KEYWORDS
        assert len(TOPIC_KEYWORDS) == 21, (
            f"Expected 21 topic buckets, got {len(TOPIC_KEYWORDS)}.\n"
            f"Buckets: {sorted(TOPIC_KEYWORDS.keys())}\n"
            "If you added a new topic, update this test AND the docs:\n"
            "  - docs/METHODOLOGY.md §3.1 topic count and table\n"
            "  - docs/ARCHITECTURE.md topics list\n"
            "  - docs/AGENT_GUIDE.md classify_topic description"
        )

    def test_methodology_topic_count(self):
        """METHODOLOGY.md must say 21 topic buckets."""
        doc = (_REPO_ROOT / "docs" / "METHODOLOGY.md").read_text()
        assert "21 topic buckets" in doc, (
            "METHODOLOGY.md topic count is stale. Should be 17."
        )

    def test_agent_guide_topic_count(self):
        """AGENT_GUIDE.md must list 21 topic buckets."""
        doc = (_REPO_ROOT / "docs" / "AGENT_GUIDE.md").read_text()
        assert "21 topic buckets" in doc, (
            "AGENT_GUIDE.md topic count is stale. Should be 17."
        )

    def test_architecture_topic_count(self):
        """ARCHITECTURE.md must say 21 topic buckets."""
        doc = (_REPO_ROOT / "docs" / "ARCHITECTURE.md").read_text()
        assert "21 topic buckets" in doc, (
            "ARCHITECTURE.md topic count is stale. Should be 17."
        )


class TestTestFileListingConsistency:
    """Guard: every test file on disk must appear in ARCHITECTURE.md listing."""

    def _test_files_on_disk(self) -> set[str]:
        """Get all test_*.py filenames from the tests/ directory."""
        tests_dir = _REPO_ROOT / "tests"
        return {f.name for f in tests_dir.glob("test_*.py")}

    def _test_files_in_architecture(self) -> set[str]:
        """Extract test file names listed in ARCHITECTURE.md tree."""
        doc = (_REPO_ROOT / "docs" / "ARCHITECTURE.md").read_text()
        return set(re.findall(r"(test_\w+\.py)", doc))

    def _test_files_in_readme(self) -> set[str]:
        """Extract test file names listed in README.md test table."""
        doc = (_REPO_ROOT / "README.md").read_text()
        return set(re.findall(r"`(test_\w+\.py)`", doc))

    def test_architecture_lists_all_test_files(self):
        """Every test file on disk must appear in ARCHITECTURE.md tree."""
        on_disk = self._test_files_on_disk()
        in_docs = self._test_files_in_architecture()
        missing = on_disk - in_docs
        assert not missing, (
            f"Test files on disk but missing from ARCHITECTURE.md:\n"
            f"  {sorted(missing)}\n"
            "Add an entry for each missing file in the tests/ tree section."
        )

    def test_architecture_has_no_phantom_test_files(self):
        """ARCHITECTURE.md should not list test files that don't exist."""
        on_disk = self._test_files_on_disk()
        in_docs = self._test_files_in_architecture()
        phantom = in_docs - on_disk
        assert not phantom, (
            f"Test files in ARCHITECTURE.md but not on disk:\n"
            f"  {sorted(phantom)}\n"
            "Remove stale entries from the tests/ tree section."
        )

    def test_architecture_test_file_count_header(self):
        """The '# tests across N test files' header must match actual count."""
        on_disk = self._test_files_on_disk()
        doc = (_REPO_ROOT / "docs" / "ARCHITECTURE.md").read_text()
        match = re.search(r"(\d+) tests across (\d+) test files", doc)
        assert match, (
            "ARCHITECTURE.md is missing the 'N tests across M test files' header."
        )
        claimed_file_count = int(match.group(2))
        actual_file_count = len(on_disk)
        assert claimed_file_count == actual_file_count, (
            f"ARCHITECTURE.md claims {claimed_file_count} test files, "
            f"but {actual_file_count} exist on disk."
        )

    def test_readme_lists_all_test_files(self):
        """Every test file on disk must appear in README.md test table."""
        on_disk = self._test_files_on_disk()
        in_readme = self._test_files_in_readme()
        missing = on_disk - in_readme
        assert not missing, (
            f"Test files on disk but missing from README.md test table:\n"
            f"  {sorted(missing)}\n"
            "Add an entry for each missing file in the README.md Testing section."
        )

    def test_readme_has_no_phantom_test_files(self):
        """README.md should not list test files that don't exist."""
        on_disk = self._test_files_on_disk()
        in_readme = self._test_files_in_readme()
        phantom = in_readme - on_disk
        assert not phantom, (
            f"Test files in README.md but not on disk:\n"
            f"  {sorted(phantom)}\n"
            "Remove stale entries from the README.md Testing section."
        )

    def test_readme_test_count_header(self):
        """README.md 'N tests across M test files' must match actual counts."""
        on_disk = self._test_files_on_disk()
        doc = (_REPO_ROOT / "README.md").read_text()
        match = re.search(r"\*\*(\d+) tests\*\* across (\d+) test files", doc)
        assert match, (
            "README.md is missing the '**N tests** across M test files' header."
        )
        claimed_file_count = int(match.group(2))
        actual_file_count = len(on_disk)
        assert claimed_file_count == actual_file_count, (
            f"README.md claims {claimed_file_count} test files, "
            f"but {actual_file_count} exist on disk."
        )


    def test_readme_per_file_test_counts(self):
        """README.md per-file test counts must match actual test function counts."""
        readme = (_REPO_ROOT / "README.md").read_text()
        tests_dir = _REPO_ROOT / "tests"
        # Parse README table: | `test_foo.py` | 42 | description |
        readme_counts = {}
        for m in re.finditer(r"\| `(test_\w+\.py)` \| (\d+) \|", readme):
            readme_counts[m.group(1)] = int(m.group(2))
        assert readme_counts, "No per-file test counts found in README.md table."
        mismatches = []
        # Split pattern to avoid self-matching when scanning this file
        _TEST_FUNC = "def " + "test_"
        for filename, claimed in sorted(readme_counts.items()):
            path = tests_dir / filename
            if not path.exists():
                continue  # phantom-file guard handles this
            content = path.read_text()
            actual = content.count(_TEST_FUNC)
            if actual != claimed:
                mismatches.append(
                    f"  {filename}: README says {claimed}, actual {actual}"
                )
        assert not mismatches, (
            "README.md per-file test counts are stale:\n"
            + "\n".join(mismatches)
            + "\nUpdate the test count column in the README.md Testing table."
        )


class TestVotingPowerConsistency:
    """Guard: stale Advance/Reddit voting power (33.5%) is purged from all docs."""

    def test_adding_publications_no_stale_voting_power(self):
        """ADDING_PUBLICATIONS.md must not reference stale 33.5% voting power."""
        doc = (_REPO_ROOT / "docs" / "ADDING_PUBLICATIONS.md").read_text()
        assert "33.5%" not in doc, (
            "ADDING_PUBLICATIONS.md still references stale 33.5% Advance/Reddit "
            "voting power. Should be 65.2% per 2026 proxy / Schedule 13G."
        )

    def test_agent_guide_no_stale_voting_power(self):
        """AGENT_GUIDE.md must not reference stale 33.5% voting power."""
        doc = (_REPO_ROOT / "docs" / "AGENT_GUIDE.md").read_text()
        assert "33.5%" not in doc, (
            "AGENT_GUIDE.md still references stale 33.5% Advance/Reddit "
            "voting power. Should be 65.2% per 2026 proxy / Schedule 13G."
        )

    def test_methodology_no_stale_voting_power(self):
        """METHODOLOGY.md must not reference stale 33.5% voting power."""
        doc = (_REPO_ROOT / "docs" / "METHODOLOGY.md").read_text()
        assert "33.5%" not in doc, (
            "METHODOLOGY.md still references stale 33.5% Advance/Reddit "
            "voting power. Should be 65.2% per 2026 proxy / Schedule 13G."
        )

    def test_editorial_histories_no_stale_voting_power(self):
        """EDITORIAL_HISTORIES.md must not reference stale 33.5% voting power."""
        doc = (_REPO_ROOT / "docs" / "EDITORIAL_HISTORIES.md").read_text()
        assert "33.5%" not in doc, (
            "EDITORIAL_HISTORIES.md still references stale 33.5% Advance/Reddit "
            "voting power. Should be 65.2% per 2026 proxy / Schedule 13G."
        )



class TestCrossReferenceConsistency:
    """Guard: cross-reference counts within doc sections stay in sync.

    The primary count guards (TestDocCountConsistency, TestTopicBucketConsistency)
    check the canonical declaration sites. These tests catch stale counts in
    *secondary* references — tables, comparison sections, and inline mentions
    that are easy to miss when the primary count is updated.

    Added: 2026-06-28 10:00 PT, Type D iteration.
    """

    def test_methodology_same_event_table_uses_34_type(self):
        """METHODOLOGY.md §13 same-event comparison must reference 49-type taxonomy."""
        doc = (_REPO_ROOT / "docs" / "METHODOLOGY.md").read_text()
        assert "33-type" not in doc, (
            "METHODOLOGY.md still references stale '33-type' taxonomy in §13 "
            "(same-event comparison). Should be '49-type' after anthropomorphization "
            "was added."
        )
        assert "34-type" not in doc, (
            "METHODOLOGY.md still references stale '34-type' taxonomy. "
            "Should be '49-type' after anthropomorphization "
            "was added."
        )
        assert "35-type" not in doc, (
            "METHODOLOGY.md still references stale '35-type' taxonomy. "
            "Should be '49-type' after anthropomorphization "
            "was added."
        )
        assert "36-type" not in doc, (
            "METHODOLOGY.md still references stale '36-type' taxonomy. "
            "Should be '49-type' after anthropomorphization "
            "was added."
        )
        assert "37-type" not in doc, (
            "METHODOLOGY.md still references stale '37-type' taxonomy. "
            "Should be '49-type' after anthropomorphization was added."
        )
        assert "38-type" not in doc, (
            "METHODOLOGY.md still references stale '38-type' taxonomy. "
            "Should be '49-type' after anthropomorphization was added."
        )

    def test_readme_test_topics_description_says_16(self):
        """README.md test_topics.py description must reference 21 topic buckets."""
        doc = (_REPO_ROOT / "README.md").read_text()
        # Find the test_topics.py row in the test table
        match = re.search(r"test_topics\.py.*?(\d+)\s+standardized topic buckets", doc)
        assert match, (
            "README.md test_topics.py row is missing topic bucket count reference."
        )
        claimed = int(match.group(1))
        assert claimed == 19, (
            f"README.md test_topics.py description references {claimed} topic buckets, "
            f"should be 19. The count is stale — worker_ai_displacement was added."
        )

    def test_no_stale_33_type_in_any_doc(self):
        """No documentation file should reference stale framing count X-type strings."""
        for doc_file in (_REPO_ROOT / "docs").glob("*.md"):
            content = doc_file.read_text()
            for stale in ("33-type", "34-type", "35-type", "36-type", "37-type",
                          "38-type", "39-type", "40-type", "41-type", "42-type",
                          "43-type", "44-type", "45-type", "46-type", "47-type",
                          "48-type"):
                assert stale not in content, (
                    f"{doc_file.name} contains stale '{stale}' reference. "
                    f"Should be '49-type' after anthropomorphization was added."
                )

    def test_no_stale_33_framing_device_in_readme(self):
        """README.md should not reference stale framing device counts."""
        doc = (_REPO_ROOT / "README.md").read_text()
        stale_refs = re.findall(r"\b(?:3[3-9]|4[0-6])[- ](?:type|framing|device)", doc)
        assert not stale_refs, (
            f"README.md contains stale framing reference(s): {stale_refs}. "
            f"Should be 47 after failure_precedent was added."
        )

    def test_readme_topic_count_in_description(self):
        """README.md publication profiles table must reference correct topic patterns."""
        doc = (_REPO_ROOT / "README.md").read_text()
        # Ensure no "13 topic" reference anywhere in README
        stale_refs = re.findall(r"\ball\s+13\s+(?:standardized\s+)?topic", doc, re.IGNORECASE)
        assert not stale_refs, (
            f"README.md contains stale 'all 13 topic' reference(s): {stale_refs}. "
            f"Should be 'all 15' — prediction_markets and corporate_strategy were added."
        )


class TestInlineTopicListConsistency:
    """Guard: inline topic name lists in docs match actual code topics.

    The primary count guards (TestTopicBucketConsistency) check numeric counts
    like '15 topic buckets'. These tests validate the *actual topic names*
    listed inline in documentation against the TOPIC_KEYWORDS dict in code.
    Catches cases where a count is updated but the inline list isn't.

    Added: 2026-06-28 14:00 PT, Type D iteration.
    """

    def _code_topic_names(self) -> set[str]:
        """Get all topic bucket names from code."""
        from mediascope.analyze.topics import TOPIC_KEYWORDS
        return set(TOPIC_KEYWORDS.keys())

    def test_architecture_inline_topics_complete(self):
        """ARCHITECTURE.md topics.py description must list all topic buckets."""
        doc = (_REPO_ROOT / "docs" / "ARCHITECTURE.md").read_text()
        code_topics = self._code_topic_names()
        # Find the inline topics list (comma-separated after "Topics:")
        match = re.search(r"Topics:\s*(.+)", doc)
        assert match, (
            "ARCHITECTURE.md is missing the 'Topics: ...' inline list "
            "in the topics.py section."
        )
        listed_topics = {t.strip() for t in match.group(1).split(",")}
        missing = code_topics - listed_topics
        extra = listed_topics - code_topics
        assert not missing, (
            f"ARCHITECTURE.md topics.py inline list is missing topic(s): "
            f"{sorted(missing)}.\nAll code topics: {sorted(code_topics)}"
        )
        assert not extra, (
            f"ARCHITECTURE.md topics.py inline list has extra topic(s) not in code: "
            f"{sorted(extra)}.\nAll code topics: {sorted(code_topics)}"
        )

    def test_agent_guide_inline_topics_complete(self):
        """AGENT_GUIDE.md classify_topic schema must list all topic buckets."""
        doc = (_REPO_ROOT / "docs" / "AGENT_GUIDE.md").read_text()
        code_topics = self._code_topic_names()
        # Find the topic list in the classify_topic JSON schema description
        match = re.search(
            r"21 topic buckets:\s*([\w_]+(?:,\s*[\w_]+)*)\.",
            doc,
        )
        assert match, (
            "AGENT_GUIDE.md classify_topic description is missing the "
            "inline topic bucket list."
        )
        listed_topics = {t.strip() for t in match.group(1).split(",")}
        missing = code_topics - listed_topics
        extra = listed_topics - code_topics
        assert not missing, (
            f"AGENT_GUIDE.md classify_topic inline list is missing topic(s): "
            f"{sorted(missing)}.\nAll code topics: {sorted(code_topics)}"
        )
        assert not extra, (
            f"AGENT_GUIDE.md classify_topic inline list has extra topic(s) "
            f"not in code: {sorted(extra)}.\n"
            f"All code topics: {sorted(code_topics)}"
        )

    def test_methodology_topic_table_complete(self):
        """METHODOLOGY.md §3.1 topic table must have a row for every topic bucket."""
        doc = (_REPO_ROOT / "docs" / "METHODOLOGY.md").read_text()
        code_topics = self._code_topic_names()
        # Extract topic names from the table rows (backtick-enclosed names)
        table_topics = set(re.findall(r"`(\w+)`\s*\|", doc))
        # Filter to only actual topic names (intersection with code)
        # The table has other backtick values; check coverage
        missing = code_topics - table_topics
        assert not missing, (
            f"METHODOLOGY.md §3.1 topic table is missing row(s) for: "
            f"{sorted(missing)}.\nAll code topics: {sorted(code_topics)}"
        )


class TestQualityStandardsConsistency:
    """Guard: QUALITY_STANDARDS.md banned phrases match code.

    Added: 2026-06-28 14:00 PT, Type D iteration.
    """

    def test_banned_phrase_count_matches_doc(self):
        """QUALITY_STANDARDS.md must reference the correct banned phrase count."""
        from mediascope.quality.standards import BANNED_PHRASES
        doc = (_REPO_ROOT / "docs" / "QUALITY_STANDARDS.md").read_text()
        match = re.search(r"(\d+)\s+phrases?\s+are\s+markers", doc)
        assert match, (
            "QUALITY_STANDARDS.md is missing the banned phrase count declaration."
        )
        claimed = int(match.group(1))
        actual = len(BANNED_PHRASES)
        assert claimed == actual, (
            f"QUALITY_STANDARDS.md claims {claimed} banned phrases but code "
            f"has {actual}. Update the doc or the code."
        )

    def test_all_banned_phrases_documented(self):
        """Every banned phrase in code should appear in QUALITY_STANDARDS.md."""
        from mediascope.quality.standards import BANNED_PHRASES
        doc = (_REPO_ROOT / "docs" / "QUALITY_STANDARDS.md").read_text()
        missing = []
        for phrase in BANNED_PHRASES:
            # Case-sensitive check for capitalized phrases, insensitive for others
            if phrase[0].isupper():
                if phrase not in doc:
                    missing.append(phrase)
            else:
                if phrase.lower() not in doc.lower():
                    missing.append(phrase)
        assert not missing, (
            f"Banned phrases in code but missing from QUALITY_STANDARDS.md: "
            f"{missing}"
        )



class TestFramingDocstringConsistency:
    """Guard: framing.py detect_framing_devices docstring counts match code.

    The docstring in framing.py states "Scans for N pattern-matched device
    types plus M structural post-pass types (T total)". These counts must
    match the actual device types registered in the module.

    Added: 2026-06-28 21:00 PT, Type D iteration.
    """

    def test_docstring_pattern_count_matches_code(self):
        """framing.py docstring must claim correct pattern-matched count."""
        src = (_REPO_ROOT / "mediascope" / "analyze" / "framing.py").read_text()
        # Extract actual pattern-matched types
        pattern_keys = set(re.findall(r'_DEVICE_PATTERNS\["(\w+)"\]', src))
        initial_keys = set(re.findall(r'"(\w+)":\s*_[A-Z_]+_PATTERNS', src))
        actual_pattern = len(initial_keys | pattern_keys)
        # Extract docstring claim
        match = re.search(r"Scans for (\d+) pattern-matched", src)
        assert match, (
            "framing.py docstring is missing the 'Scans for N pattern-matched' line."
        )
        claimed = int(match.group(1))
        assert claimed == actual_pattern, (
            f"framing.py docstring claims {claimed} pattern-matched types but "
            f"code has {actual_pattern}. Update the docstring."
        )

    def test_docstring_total_count_matches_code(self):
        """framing.py docstring must claim correct total count."""
        src = (_REPO_ROOT / "mediascope" / "analyze" / "framing.py").read_text()
        all_types = _all_device_types_from_code()
        actual_total = len(all_types)
        match = re.search(r"\((\d+) total\)", src)
        assert match, (
            "framing.py docstring is missing the '(N total)' count."
        )
        claimed = int(match.group(1))
        assert claimed == actual_total, (
            f"framing.py docstring claims {claimed} total types but "
            f"code has {actual_total}. Update the docstring."
        )


class TestMethodologyDeviceTableConsistency:
    """Guard: METHODOLOGY.md §4.1 Extended and Structural device tables
    contain all device types from code.

    The numeric count guards (TestDocCountConsistency) catch stale totals.
    These tests catch missing *table rows*: a count can be updated to 22
    while the table still has only 20 entries.

    Added: 2026-06-28 21:00 PT, Type D iteration.
    """

    def _extended_types_from_code(self) -> set[str]:
        """Get pattern-matched types that are NOT in the core 10."""
        src = (_REPO_ROOT / "mediascope" / "analyze" / "framing.py").read_text()
        # Core types: those defined in the initial _DEVICE_PATTERNS dict literal
        initial_keys = set(re.findall(r'"(\w+)":\s*_[A-Z_]+_PATTERNS', src))
        # Dynamically added pattern types
        dynamic_keys = set(re.findall(r'_DEVICE_PATTERNS\["(\w+)"\]', src))
        return dynamic_keys - initial_keys

    def _structural_types_from_code(self) -> set[str]:
        """Get structural post-pass device types (not in _DEVICE_PATTERNS)."""
        src = (_REPO_ROOT / "mediascope" / "analyze" / "framing.py").read_text()
        pattern_keys = set(re.findall(r'_DEVICE_PATTERNS\["(\w+)"\]', src))
        initial_keys = set(re.findall(r'"(\w+)":\s*_[A-Z_]+_PATTERNS', src))
        post_pass = set(re.findall(r'device_type="(\w+)"', src))
        return post_pass - initial_keys - pattern_keys

    def _device_names_in_methodology_table(self, section_header: str) -> set[str]:
        """Extract bold device names from a METHODOLOGY.md table section."""
        doc = (_REPO_ROOT / "docs" / "METHODOLOGY.md").read_text()
        # Find the section
        start = doc.find(section_header)
        assert start != -1, f"Section '{section_header}' not found in METHODOLOGY.md"
        # Find the next section header (#### or ###)
        remaining = doc[start + len(section_header):]
        next_section = re.search(r"\n#{3,4} ", remaining)
        section_text = remaining[:next_section.start()] if next_section else remaining
        # Extract bold names from table rows: | **Name** |
        names_raw = re.findall(r"\*\*(.+?)\*\*", section_text)
        # Convert display names to code-style names for comparison
        # e.g., "Latecomer Narrative" -> "latecomer_narrative"
        # Handle hyphens ("Techno-Optimism" -> "techno_optimism")
        # Handle slashes ("Scale/Magnitude" -> "scale_magnitude")
        result = set()
        for n in names_raw:
            code_name = n.lower().replace(" ", "_").replace("/", "_").replace("-", "_")
            result.add(code_name)
        return result

    def _normalize_for_matching(self, code_name: str, doc_names: set[str]) -> bool:
        """Check if a code device name matches any doc device name,
        handling suffix differences (e.g. 'scale_magnitude' vs 'scale_magnitude_framing')."""
        if code_name in doc_names:
            return True
        # Check if code_name is a prefix of any doc name or vice versa
        for dn in doc_names:
            if dn.startswith(code_name) or code_name.startswith(dn):
                return True
        return False

    def test_extended_table_has_all_extended_types(self):
        """METHODOLOGY.md Extended Devices table must have a row for every
        extended device type in code."""
        code_extended = self._extended_types_from_code()
        doc_extended = self._device_names_in_methodology_table("#### Extended Devices")
        missing = {t for t in code_extended
                   if not self._normalize_for_matching(t, doc_extended)}
        assert not missing, (
            f"METHODOLOGY.md Extended Devices table is missing row(s) for: "
            f"{sorted(missing)}.\n"
            f"All code extended types: {sorted(code_extended)}\n"
            f"Found in doc table: {sorted(doc_extended)}"
        )

    def test_structural_table_has_all_structural_types(self):
        """METHODOLOGY.md Structural Devices table must have a row for every
        structural device type in code."""
        code_structural = self._structural_types_from_code()
        doc_structural = self._device_names_in_methodology_table(
            "#### Structural Devices (Post-Pass)"
        )
        missing = {t for t in code_structural
                   if not self._normalize_for_matching(t, doc_structural)}
        assert not missing, (
            f"METHODOLOGY.md Structural Devices table is missing row(s) for: "
            f"{sorted(missing)}.\n"
            f"All code structural types: {sorted(code_structural)}\n"
            f"Found in doc table: {sorted(doc_structural)}"
        )


class TestEmotionalLanguageCount:
    """Guard: EMOTIONAL_LANGUAGE set size must stay in sync.

    When terms are added to or removed from the EMOTIONAL_LANGUAGE set in
    sentiment.py, this guard ensures the count is updated deliberately,
    preventing accidental drift or duplicate additions.

    Added: 2026-06-28 22:00 PT, Type A iteration (Fast Company analysis).
    """

    def test_emotional_language_count(self):
        """EMOTIONAL_LANGUAGE should contain exactly 612 unique terms."""
        from mediascope.analyze.sentiment import EMOTIONAL_LANGUAGE

        assert len(EMOTIONAL_LANGUAGE) == 680, (
            f"Expected 669 emotional language terms, got {len(EMOTIONAL_LANGUAGE)}.\n"
            "If you added or removed terms, update this test to the new count.\n"
            "Also check for duplicates: len(set(EMOTIONAL_LANGUAGE)) should match."
        )

    def test_emotional_language_no_duplicates(self):
        """EMOTIONAL_LANGUAGE should have no duplicate entries."""
        from mediascope.analyze.sentiment import EMOTIONAL_LANGUAGE

        if isinstance(EMOTIONAL_LANGUAGE, set):
            return  # Sets can't have duplicates
        seen = set()
        dupes = []
        for term in EMOTIONAL_LANGUAGE:
            if term in seen:
                dupes.append(term)
            seen.add(term)
        assert not dupes, (
            f"EMOTIONAL_LANGUAGE has duplicate entries: {dupes}"
        )


class TestAdversarialDeviceListConsistency:
    """Guard: adversarial device type lists in docs match code.

    The tone correction pipeline uses a specific set of adversarial device
    types (_ADVERSARIAL_DEVICE_TYPES in sentiment.py). Documentation that
    enumerates these types must stay in sync.

    Added: 2026-06-28 21:00 PT, Type D iteration.
    """

    # --- Total regex pattern count guard ---
    # Track the total number of compiled regex patterns across all device
    # types in _DEVICE_PATTERNS.  When patterns are added, this test fails
    # and forces a deliberate count update, preventing undocumented drift.
    EXPECTED_TOTAL_PATTERNS = 293  # sum(len(v) for v in _DEVICE_PATTERNS.values())

    def test_total_regex_pattern_count(self):
        """Total compiled regex patterns must match expected count."""
        from mediascope.analyze.framing import _DEVICE_PATTERNS
        actual = sum(len(v) for v in _DEVICE_PATTERNS.values())
        assert actual == self.EXPECTED_TOTAL_PATTERNS, (
            f"Expected {self.EXPECTED_TOTAL_PATTERNS} total regex patterns, "
            f"got {actual}. If you added or removed patterns, update "
            f"EXPECTED_TOTAL_PATTERNS in this test class.\n"
            f"Per-type counts: {', '.join(f'{k}={len(v)}' for k, v in sorted(_DEVICE_PATTERNS.items()))}"
        )

    def _adversarial_types_from_code(self) -> set[str]:
        """Get the adversarial device type set from sentiment.py."""
        src = (_REPO_ROOT / "mediascope" / "analyze" / "sentiment.py").read_text()
        # Find the _ADVERSARIAL_DEVICE_TYPES set definition
        match = re.search(
            r"_ADVERSARIAL_DEVICE_TYPES:\s*set\[str\]\s*=\s*\{(.*?)\}",
            src,
            re.DOTALL,
        )
        assert match, "Cannot find _ADVERSARIAL_DEVICE_TYPES in sentiment.py"
        return set(re.findall(r'"(\w+)"', match.group(1)))

    def test_methodology_adversarial_list_complete(self):
        """METHODOLOGY.md §9 must list all adversarial device types from code."""
        code_types = self._adversarial_types_from_code()
        doc = (_REPO_ROOT / "docs" / "METHODOLOGY.md").read_text()
        # Find the adversarial set enumeration
        match = re.search(
            r"adversarial device type set \(([^)]+)\)",
            doc,
        )
        assert match, (
            "METHODOLOGY.md is missing the adversarial device type set enumeration."
        )
        doc_types = set(re.findall(r"(\w+)", match.group(1)))
        missing = code_types - doc_types
        assert not missing, (
            f"METHODOLOGY.md adversarial device list is missing: {sorted(missing)}.\n"
            f"Code has: {sorted(code_types)}\n"
            f"Doc has: {sorted(doc_types)}"
        )

    def test_quality_standards_adversarial_list_complete(self):
        """QUALITY_STANDARDS.md must list all adversarial device types from code."""
        code_types = self._adversarial_types_from_code()
        doc = (_REPO_ROOT / "docs" / "QUALITY_STANDARDS.md").read_text()
        match = re.search(
            r"adversarial set \(([^)]+)\)",
            doc,
        )
        assert match, (
            "QUALITY_STANDARDS.md is missing the adversarial device set enumeration."
        )
        doc_types = set(re.findall(r"(\w+)", match.group(1)))
        missing = code_types - doc_types
        assert not missing, (
            f"QUALITY_STANDARDS.md adversarial device list is missing: {sorted(missing)}.\n"
            f"Code has: {sorted(code_types)}\n"
            f"Doc has: {sorted(doc_types)}"
        )


class TestStaleRegexPatternCountPurge:
    """Guard: stale regex pattern counts are purged from doc descriptions.

    When patterns are added/removed, EXPECTED_TOTAL_PATTERNS is updated in
    TestTotalRegexPatternCount, but secondary references in ARCHITECTURE.md
    and README.md test descriptions can lag behind.  These tests catch stale
    counts by scanning for any old count that is not the current one.

    Added: 2026-06-30 17:00 PT, Type D iteration.
    """

    def _current_pattern_count(self) -> int:
        from mediascope.analyze.framing import _DEVICE_PATTERNS
        return sum(len(v) for v in _DEVICE_PATTERNS.values())

    def test_architecture_test_description_pattern_count(self):
        """ARCHITECTURE.md test_structural_consistency description must use current pattern count."""
        current = self._current_pattern_count()
        doc = (_REPO_ROOT / "docs" / "ARCHITECTURE.md").read_text()
        match = re.search(
            r"test_structural_consistency\.py.*?(\d+)\s+patterns",
            doc,
        )
        assert match, (
            "ARCHITECTURE.md test_structural_consistency.py row is missing "
            "the regex pattern count."
        )
        claimed = int(match.group(1))
        assert claimed == current, (
            f"ARCHITECTURE.md test_structural_consistency description says "
            f"{claimed} patterns but code has {current}. Update the "
            f"description."
        )

    def test_readme_test_description_pattern_count(self):
        """README.md test_structural_consistency description must use current pattern count."""
        current = self._current_pattern_count()
        doc = (_REPO_ROOT / "README.md").read_text()
        match = re.search(
            r"test_structural_consistency\.py.*?(\d+)\s+patterns",
            doc,
        )
        assert match, (
            "README.md test_structural_consistency.py row is missing "
            "the regex pattern count."
        )
        claimed = int(match.group(1))
        assert claimed == current, (
            f"README.md test_structural_consistency description says "
            f"{claimed} patterns but code has {current}. Update the "
            f"description."
        )


class TestDocstringDeviceListCompleteness:
    """Guard: framing.py docstring inline device list matches code types.

    TestDocstringCountConsistency validates the numeric count in the
    docstring header ("Scans for N pattern-matched").  This test validates
    the actual device names enumerated in the list, catching cases where
    the count is updated but a new type isn't added to the inline list.

    Added: 2026-06-30 17:00 PT, Type D iteration.
    """

    def test_docstring_lists_all_pattern_matched_types(self):
        """framing.py docstring must enumerate every pattern-matched device type."""
        src = (_REPO_ROOT / "mediascope" / "analyze" / "framing.py").read_text()
        # Extract actual pattern-matched types from code
        actual_types = set(re.findall(r'_DEVICE_PATTERNS\["(\w+)"\]', src))
        initial_types = set(re.findall(r'"(\w+)":\s*_[A-Z_]+_PATTERNS', src))
        code_types = actual_types | initial_types

        # Extract the docstring's Pattern-matched list
        docstring_match = re.search(
            r"Pattern-matched \(\d+\):\s*(.*?)\.\s*\n\s*\n",
            src,
            re.DOTALL,
        )
        assert docstring_match, (
            "framing.py docstring is missing the 'Pattern-matched (N): ...' "
            "enumeration block."
        )
        listed_raw = docstring_match.group(1)
        # Extract all snake_case identifiers from the list
        listed_types = set(re.findall(r"(\w+)", listed_raw))
        # Filter out non-type words (and, etc.)
        listed_types -= {"and", "including", "the", "a", "an"}

        missing = code_types - listed_types
        assert not missing, (
            f"framing.py docstring Pattern-matched list is missing: "
            f"{sorted(missing)}.\n"
            f"Code has {len(code_types)} types; docstring lists "
            f"{len(listed_types & code_types)} of them."
        )


class TestArchitectureExtendedDeviceCount:
    """Guard: ARCHITECTURE.md framing.py section extended device count matches code.

    The ARCHITECTURE.md framing.py detail section lists device types by tier
    (Core, Extended, Structural).  The Extended count label must match the
    actual number of non-core pattern-matched types.

    Added: 2026-06-30 17:00 PT, Type D iteration.
    """

    CORE_TYPES = {
        "guilt_by_association", "anonymous_authority", "catastrophizing",
        "false_balance", "selective_omission_signal", "emotional_appeal",
        "loaded_language", "power_asymmetry", "ceo_personalization",
        "litigation_framing",
    }

    def test_extended_count_label_matches_code(self):
        """ARCHITECTURE.md 'Extended (N):' label must match actual extended type count."""
        from mediascope.analyze.framing import _DEVICE_PATTERNS
        actual_extended = len(set(_DEVICE_PATTERNS.keys()) - self.CORE_TYPES)
        doc = (_REPO_ROOT / "docs" / "ARCHITECTURE.md").read_text()
        match = re.search(r"\*\*Extended \((\d+)\):\*\*", doc)
        assert match, (
            "ARCHITECTURE.md is missing the 'Extended (N):' label in the "
            "framing.py section."
        )
        claimed = int(match.group(1))
        assert claimed == actual_extended, (
            f"ARCHITECTURE.md says 'Extended ({claimed}):' but code has "
            f"{actual_extended} extended device types (42 pattern-matched "
            f"minus 10 core). Update the label."
        )
