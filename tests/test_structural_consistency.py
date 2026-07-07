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
    EXPECTED_TOTAL = 75
    EXPECTED_PATTERN_MATCHED = 69  # core + extended (in _DEVICE_PATTERNS)
    EXPECTED_STRUCTURAL = {"kicker_framing", "analogy_stacking",
                           "speculative_framing", "trend_bundling",
                           "social_proof_amplification",
                           "delayed_defense"}

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

    def test_methodology_tier_breakdown(self):
        """METHODOLOGY.md intro tier counts (core/extended/structural) match code."""
        doc = (_REPO_ROOT / "docs" / "METHODOLOGY.md").read_text()
        match = re.search(
            r"core devices \((\d+) pattern-matched",
            doc,
        )
        assert match, (
            "METHODOLOGY.md is missing the 'core devices (N pattern-matched' "
            "tier breakdown in the §4.1 intro."
        )
        claimed_core = int(match.group(1))
        assert claimed_core == 10, (
            f"METHODOLOGY.md claims {claimed_core} core devices but code has 10."
        )

        match = re.search(
            r"extended devices \((\d+) added from real-article analysis\)",
            doc,
        )
        assert match, (
            "METHODOLOGY.md is missing the 'extended devices (N added from "
            "real-article analysis)' tier breakdown."
        )
        claimed_extended = int(match.group(1))
        assert claimed_extended == self._EXPECTED_EXTENDED, (
            f"METHODOLOGY.md claims {claimed_extended} extended devices "
            f"but code has {self._EXPECTED_EXTENDED} "
            f"(total {self._EXPECTED_TOTAL} - 10 core - "
            f"{len(TestFramingDeviceTypeCount.EXPECTED_STRUCTURAL)} structural)."
        )

        match = re.search(
            r"structural devices \((\d+) detected via post-pass",
            doc,
        )
        assert match, (
            "METHODOLOGY.md is missing the 'structural devices (N detected "
            "via post-pass' tier breakdown."
        )
        claimed_structural = int(match.group(1))
        expected_structural = len(TestFramingDeviceTypeCount.EXPECTED_STRUCTURAL)
        assert claimed_structural == expected_structural, (
            f"METHODOLOGY.md claims {claimed_structural} structural devices "
            f"but code has {expected_structural}."
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

    def test_no_stale_device_type_count_in_docs(self):
        """No doc should reference an old total device-type count that isn't current.

        Catches stale references like '56-type taxonomy' or '69-type taxonomy'
        that slip through when only positive presence tests (e.g. '72 framing
        device types') are used.

        Added: 2026-07-05 02:00 PT, Type D iteration.
        Updated: 2026-07-06 00:00 PT, Type D — expanded from manual list
        [33,43,53,56,63,65,67,68] to cover range 30..current-1, using
        patterns specific to TOTAL counts ("-type taxonomy", "N framing device
        type") to avoid false positives on subset counts like "26 adversarial
        types". Previous manual list missed 69 which survived in
        METHODOLOGY.md §13.2.
        """
        current = self._EXPECTED_TOTAL
        # Scan any count from 30 up to (current-1). Lower bound 30 avoids
        # false positives on small numbers that appear in other contexts
        # (e.g. "10 core devices", "6 structural devices").
        stale_counts = list(range(30, current))

        # Patterns that unambiguously refer to the TOTAL device count:
        # - "N-type taxonomy" (e.g., "69-type taxonomy")
        # - "N framing device type" (e.g., "56 framing device types")
        # - "N device type" preceded by "total" context
        # - "(N device type" in parenthetical annotations (e.g., diagrams)
        stale_patterns = [
            r"\b{n}-type\s+taxonomy",           # "69-type taxonomy"
            r"\b{n}\s+framing\s+device\s+type",  # "56 framing device types"
            r"total[^.]*\b{n}\s+device",         # "total of 56 device types"
            r"\({n}\s+device\s+type",            # "(73 device types, ..." in diagrams
        ]

        doc_files = [
            "docs/METHODOLOGY.md", "docs/ARCHITECTURE.md",
            "docs/AGENT_GUIDE.md", "docs/QUALITY_STANDARDS.md",
            "README.md",
        ]
        for doc_path in doc_files:
            doc = (_REPO_ROOT / doc_path).read_text()
            for stale in stale_counts:
                for pat_template in stale_patterns:
                    pattern = pat_template.format(n=stale)
                    match = re.search(pattern, doc)
                    assert match is None, (
                        f"{doc_path} contains stale device count reference "
                        f"'{match.group()}' (current total is {current}). "
                        f"Update to {current}."
                    )


class TestTopicBucketConsistency:
    """Guard: topic bucket counts match across code and docs."""

    def test_topic_count_in_code(self):
        """Code should define exactly 26 topic buckets."""
        from mediascope.analyze.topics import TOPIC_KEYWORDS
        assert len(TOPIC_KEYWORDS) == 26, (
            f"Expected 26 topic buckets, got {len(TOPIC_KEYWORDS)}.\n"
            f"Buckets: {sorted(TOPIC_KEYWORDS.keys())}\n"
            "If you added a new topic, update this test AND the docs:\n"
            "  - docs/METHODOLOGY.md §3.1 topic count and table\n"
            "  - docs/ARCHITECTURE.md topics list\n"
            "  - docs/AGENT_GUIDE.md classify_topic description"
        )

    def test_methodology_topic_count(self):
        """METHODOLOGY.md must say 26 topic buckets."""
        doc = (_REPO_ROOT / "docs" / "METHODOLOGY.md").read_text()
        assert "26 topic buckets" in doc, (
            "METHODOLOGY.md topic count is stale. Should be 26."
        )

    def test_agent_guide_topic_count(self):
        """AGENT_GUIDE.md must list 26 topic buckets."""
        doc = (_REPO_ROOT / "docs" / "AGENT_GUIDE.md").read_text()
        assert "26 topic buckets" in doc, (
            "AGENT_GUIDE.md topic count is stale. Should be 26."
        )

    def test_architecture_topic_count(self):
        """ARCHITECTURE.md must say 26 topic buckets."""
        doc = (_REPO_ROOT / "docs" / "ARCHITECTURE.md").read_text()
        assert "26 topic buckets" in doc, (
            "ARCHITECTURE.md topic count is stale. Should be 26."
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
        claimed_total = int(match.group(1))
        claimed_file_count = int(match.group(2))
        actual_file_count = len(on_disk)
        assert claimed_file_count == actual_file_count, (
            f"ARCHITECTURE.md claims {claimed_file_count} test files, "
            f"but {actual_file_count} exist on disk."
        )
        actual_total = self._count_pytest_tests()
        assert claimed_total == actual_total, (
            f"ARCHITECTURE.md header claims {claimed_total} tests, "
            f"but actual pytest-collected count is {actual_total}. "
            f"Update the header."
        )

    def test_architecture_test_topics_bucket_count(self):
        """ARCHITECTURE.md test_topics.py description must reference 26 topic buckets."""
        doc = (_REPO_ROOT / "docs" / "ARCHITECTURE.md").read_text()
        match = re.search(r"test_topics\.py.*?all\s+(\d+)\s+buckets", doc)
        assert match, (
            "ARCHITECTURE.md test_topics.py row is missing topic bucket count "
            "reference (expected 'all 26 buckets')."
        )
        claimed = int(match.group(1))
        assert claimed == 26, (
            f"ARCHITECTURE.md test_topics.py description references {claimed} "
            f"topic buckets, should be 26."
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
        claimed_total = int(match.group(1))
        claimed_file_count = int(match.group(2))
        actual_file_count = len(on_disk)
        assert claimed_file_count == actual_file_count, (
            f"README.md claims {claimed_file_count} test files, "
            f"but {actual_file_count} exist on disk."
        )
        actual_total = self._count_pytest_tests()
        assert claimed_total == actual_total, (
            f"README.md header claims {claimed_total} tests, "
            f"but actual pytest-collected count is {actual_total} "
            f"({self._count_def_tests()} def test_ + parametrize expansions). "
            f"Update the header."
        )

    def _count_def_tests(self) -> int:
        """Count actual test function definitions across all test files.

        Uses a regex anchored to line-start (after optional whitespace) so
        occurrences of 'def test_' inside strings, docstrings, or comments
        are not counted.
        """
        tests_dir = _REPO_ROOT / "tests"
        total = 0
        for f in tests_dir.glob("test_*.py"):
            total += len(re.findall(r"^\s+def test_", f.read_text(), re.MULTILINE))
        return total

    @staticmethod
    def _count_top_level_items(text: str) -> int:
        """Count top-level comma-separated items in a parametrize list.

        Tracks parenthesis/bracket depth so commas inside tuples like
        ``("phrase", True)`` are not counted as item separators.  This
        fixes a bug where naive ``str.split(",")`` overcounted tuple-
        valued parametrize entries (e.g. 5 tuples of 2 elements were
        counted as 10 items instead of 5).

        Handles trailing commas (standard Python style) and ``# comments``
        after the last item.
        """
        text = text.strip()
        if not text:
            return 0
        count = 1
        depth = 0
        in_string: str | None = None
        last_comma_at_depth_zero = False
        i = 0
        while i < len(text):
            c = text[i]
            if in_string is not None:
                if c == "\\" and i + 1 < len(text):
                    i += 2  # skip escaped character
                    continue
                if c == in_string:
                    in_string = None
            else:
                if c == "#":
                    # Skip to end of line (Python line comment)
                    while i < len(text) and text[i] != "\n":
                        i += 1
                    continue
                if c in ('"', "'"):
                    in_string = c
                    last_comma_at_depth_zero = False
                elif c in ("(", "[", "{"):
                    depth += 1
                    last_comma_at_depth_zero = False
                elif c in (")", "]", "}"):
                    depth -= 1
                    last_comma_at_depth_zero = False
                elif c == "," and depth == 0:
                    count += 1
                    last_comma_at_depth_zero = True
                elif not c.isspace():
                    last_comma_at_depth_zero = False
            i += 1
        # If the last top-level comma was trailing (no non-whitespace/comment
        # content after it), subtract 1.
        if last_comma_at_depth_zero:
            count -= 1
        return count

    def _count_parametrize_expansions(self) -> int:
        """Count extra tests from @pytest.mark.parametrize decorators.

        Each parametrize decorator with N items produces N tests from 1 def,
        so the expansion is (N - 1) per decorator.  Uses depth-aware item
        counting to correctly handle tuple-valued parametrize entries.
        """
        tests_dir = _REPO_ROOT / "tests"
        extra = 0
        for f in tests_dir.glob("test_*.py"):
            content = f.read_text()
            for m in re.finditer(
                r"@pytest\.mark\.parametrize\(\s*\"[^\"]+\",\s*\[(.*?)\]",
                content,
                re.DOTALL,
            ):
                items_text = m.group(1).strip()
                if not items_text:
                    continue
                n_items = self._count_top_level_items(items_text)
                if n_items > 1:
                    extra += n_items - 1
        return extra

    def _count_pytest_tests(self) -> int:
        """Total pytest-collected test count (def test_ + parametrize expansions)."""
        return self._count_def_tests() + self._count_parametrize_expansions()


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
        for filename, claimed in sorted(readme_counts.items()):
            path = tests_dir / filename
            if not path.exists():
                continue  # phantom-file guard handles this
            content = path.read_text()
            # Use regex anchored to line-start to avoid counting
            # occurrences in strings, docstrings, or comments.
            actual = len(re.findall(r"^\s+def test_", content, re.MULTILINE))
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
        """METHODOLOGY.md §13 same-event comparison must reference 53-type taxonomy."""
        doc = (_REPO_ROOT / "docs" / "METHODOLOGY.md").read_text()
        assert "33-type" not in doc, (
            "METHODOLOGY.md still references stale '33-type' taxonomy in §13 "
            "(same-event comparison). Should be '53-type' after editorial_aside "
            "was added."
        )
        assert "34-type" not in doc, (
            "METHODOLOGY.md still references stale '34-type' taxonomy. "
            "Should be '53-type' after editorial_aside "
            "was added."
        )
        assert "35-type" not in doc, (
            "METHODOLOGY.md still references stale '35-type' taxonomy. "
            "Should be '53-type' after editorial_aside "
            "was added."
        )
        assert "36-type" not in doc, (
            "METHODOLOGY.md still references stale '36-type' taxonomy. "
            "Should be '53-type' after editorial_aside "
            "was added."
        )
        assert "37-type" not in doc, (
            "METHODOLOGY.md still references stale '37-type' taxonomy. "
            "Should be '53-type' after editorial_aside was added."
        )
        assert "38-type" not in doc, (
            "METHODOLOGY.md still references stale '38-type' taxonomy. "
            "Should be '53-type' after editorial_aside was added."
        )

    def test_readme_test_topics_description_says_25(self):
        """README.md test_topics.py description must reference 26 topic buckets."""
        doc = (_REPO_ROOT / "README.md").read_text()
        # Find the test_topics.py row in the test table
        match = re.search(r"test_topics\.py.*?(\d+)\s+standardized topic buckets", doc)
        assert match, (
            "README.md test_topics.py row is missing topic bucket count reference."
        )
        claimed = int(match.group(1))
        assert claimed == 26, (
            f"README.md test_topics.py description references {claimed} topic buckets, "
            f"should be 26. The count is stale."
        )

    def test_no_stale_33_type_in_any_doc(self):
        """No documentation file should reference stale framing count X-type strings."""
        for doc_file in (_REPO_ROOT / "docs").glob("*.md"):
            content = doc_file.read_text()
            for stale in ("33-type", "34-type", "35-type", "36-type", "37-type",
                          "38-type", "39-type", "40-type", "41-type", "42-type",
                          "43-type", "44-type", "45-type", "46-type", "47-type",
                          "48-type", "49-type", "50-type"):
                assert stale not in content, (
                    f"{doc_file.name} contains stale '{stale}' reference. "
                    f"Should be '53-type' after editorial_aside was added."
                )

    def test_no_stale_33_framing_device_in_readme(self):
        """README.md should not reference stale framing device counts."""
        doc = (_REPO_ROOT / "README.md").read_text()
        stale_refs = re.findall(r"\b(?:3[3-9]|4[0-9]|5[0-8])[- ](?:type|framing|device)", doc)
        assert not stale_refs, (
            f"README.md contains stale framing reference(s): {stale_refs}. "
            f"Should be 61 after policy_reversal + competitive_deficit added (55 pattern + 6 structural)."
        )

    def test_readme_topic_count_in_description(self):
        """README.md publication profiles table must reference correct topic patterns."""
        doc = (_REPO_ROOT / "README.md").read_text()
        # Ensure no "13 topic" reference anywhere in README
        stale_refs = re.findall(r"\ball\s+13\s+(?:standardized\s+)?topic", doc, re.IGNORECASE)
        assert not stale_refs, (
            f"README.md contains stale 'all 13 topic' reference(s): {stale_refs}. "
            f"Should be 'all 26' — 26 topic buckets defined in code."
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
            r"26 topic buckets:\s*([\w_]+(?:,\s*[\w_]+)*)\.",
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

    def test_structural_table_has_no_phantom_types(self):
        """METHODOLOGY.md Structural Devices table must NOT contain
        pattern-matched types that are not actual structural post-pass devices.
        Prevents accidental duplication (e.g. financial_reassurance listed in
        both Extended and Structural tables)."""
        code_structural = self._structural_types_from_code()
        doc_structural = self._device_names_in_methodology_table(
            "#### Structural Devices (Post-Pass)"
        )
        phantom = {dn for dn in doc_structural
                   if not self._normalize_for_matching(dn, code_structural)}
        assert not phantom, (
            f"METHODOLOGY.md Structural Devices table has row(s) for types "
            f"that are NOT structural post-pass devices in code: "
            f"{sorted(phantom)}.\n"
            f"These may be pattern-matched types accidentally duplicated in "
            f"the structural table. Code structural types: "
            f"{sorted(code_structural)}"
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

        assert len(EMOTIONAL_LANGUAGE) == 836, (
            f"Expected 836 emotional language terms, got {len(EMOTIONAL_LANGUAGE)}.\n"
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

    def test_quality_standards_el_count_matches_code(self):
        """QUALITY_STANDARDS.md emotional language term count must match code.

        The doc references the EL lexicon size in §8.1 and §8.4.  When terms
        are added, the doc count drifts.  This guard catches the drift.
        Added: 2026-07-04, Type D iteration.
        """
        from mediascope.analyze.sentiment import EMOTIONAL_LANGUAGE

        doc = (_REPO_ROOT / "docs" / "QUALITY_STANDARDS.md").read_text()
        # §8.1: "**N emotional language terms**"
        match = re.search(r"\*\*(\d+) emotional language terms\*\*", doc)
        assert match, (
            "QUALITY_STANDARDS.md §8.1 is missing the "
            "'**N emotional language terms**' reference."
        )
        claimed = int(match.group(1))
        actual = len(EMOTIONAL_LANGUAGE)
        assert claimed == actual, (
            f"QUALITY_STANDARDS.md §8.1 claims {claimed} emotional language "
            f"terms, but code has {actual}. Update the doc."
        )
        # §8.4: "has grown to N"
        match2 = re.search(r"has grown to (\d+)", doc)
        assert match2, (
            "QUALITY_STANDARDS.md §8.4 is missing the 'has grown to N' reference."
        )
        claimed2 = int(match2.group(1))
        assert claimed2 == actual, (
            f"QUALITY_STANDARDS.md §8.4 says 'has grown to {claimed2}', "
            f"but code has {actual}. Update the doc."
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
    EXPECTED_TOTAL_PATTERNS = 420  # sum(len(v) for v in _DEVICE_PATTERNS.values())

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

    @pytest.mark.parametrize("demo_file", [
        "framing_correction_demo.py",
        "sarcastic_editorial_demo.py",
    ])
    def test_example_demo_adversarial_set_complete(self, demo_file):
        """Example demo scripts must list all adversarial device types from code.

        Demo scripts duplicate the adversarial type set for diagnostic output.
        When new types are added to _ADVERSARIAL_DEVICE_TYPES in sentiment.py,
        the demo scripts' inline copies silently go stale.

        Added: 2026-07-03 18:00 PT, Type D iteration.
        """
        code_types = self._adversarial_types_from_code()
        demo_path = _REPO_ROOT / "examples" / demo_file
        src = demo_path.read_text()
        # Find the adversarial_types = { ... } set literal
        match = re.search(
            r"adversarial_types\s*=\s*\{(.*?)\}",
            src,
            re.DOTALL,
        )
        assert match, (
            f"{demo_file} is missing the adversarial_types set literal."
        )
        demo_types = set(re.findall(r'"(\w+)"', match.group(1)))
        missing = code_types - demo_types
        extra = demo_types - code_types
        assert not missing and not extra, (
            f"{demo_file} adversarial_types set is out of sync with code.\n"
            f"Missing from demo: {sorted(missing)}\n"
            f"Extra in demo: {sorted(extra)}\n"
            f"Code has: {sorted(code_types)}"
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



class TestArchitectureDeviceNameListCompleteness:
    """Guard: ARCHITECTURE.md framing.py section inline device name lists
    contain all device types from code, not just the correct count labels.

    TestArchitectureExtendedDeviceCount validates the 'Extended (N):' count
    label.  This test validates the individual device names in the Core and
    Extended inline lists, catching cases where a new device type is added
    to code and the count label is updated but the device name and description
    are never appended to the ARCHITECTURE.md section text.

    Closes the gap identified in the 2026-06-30 17:00 PT Type D iteration:
    "Coverage gap remaining: ARCHITECTURE.md inline device *names* list is
    not validated against code (only the Extended count label is guarded now,
    not the individual names in the list)."

    Added: 2026-07-01 06:00 PT, Type D iteration.
    """

    CORE_TYPES = {
        "guilt_by_association", "anonymous_authority", "catastrophizing",
        "false_balance", "selective_omission_signal", "emotional_appeal",
        "loaded_language", "power_asymmetry", "ceo_personalization",
        "litigation_framing",
    }

    @staticmethod
    def _code_name_to_display_variants(code_name: str) -> list[str]:
        """Convert a code device name to display variants for matching.

        'straw_man' -> ['straw man']
        'scale_magnitude' -> ['scale magnitude', 'scale/magnitude']
        'analogy_metaphor' -> ['analogy metaphor', 'analogy/metaphor']
        'ceo_personalization' -> ['ceo personalization']
        'military_techno_optimism' -> ['military techno-optimism', 'military techno optimism']
        """
        base = code_name.replace("_", " ")
        variants = [base]
        # Also try replacing one space with "/" (for scale/magnitude, analogy/metaphor)
        parts = code_name.split("_")
        if len(parts) >= 2:
            for i in range(len(parts) - 1):
                slash_variant = " ".join(parts[:i] + [parts[i] + "/" + parts[i+1]] + parts[i+2:])
                variants.append(slash_variant)
        # Also try replacing one space with "-" (for techno-optimism)
        for i in range(len(parts) - 1):
            hyphen_variant = " ".join(parts[:i] + [parts[i] + "-" + parts[i+1]] + parts[i+2:])
            if hyphen_variant != base:
                variants.append(hyphen_variant)
        return variants

    def _extract_architecture_extended_section(self) -> str:
        """Extract the Extended device list text from ARCHITECTURE.md."""
        doc = (_REPO_ROOT / "docs" / "ARCHITECTURE.md").read_text()
        # Find "**Extended (N):**" and capture until the next "**Structural" or "###"
        match = re.search(
            r"\*\*Extended \(\d+\):\*\*(.*?)(?:\*\*Structural|#{3,4}\s)",
            doc,
            re.DOTALL,
        )
        assert match, (
            "ARCHITECTURE.md is missing the Extended device section."
        )
        return match.group(1).lower()

    def _extract_architecture_core_section(self) -> str:
        """Extract the Core device list text from ARCHITECTURE.md."""
        doc = (_REPO_ROOT / "docs" / "ARCHITECTURE.md").read_text()
        # Find "**Core (N):**" and capture until "**Extended"
        match = re.search(
            r"\*\*Core \(\d+\):\*\*(.*?)\*\*Extended",
            doc,
            re.DOTALL,
        )
        assert match, (
            "ARCHITECTURE.md is missing the Core device section."
        )
        return match.group(1).lower()

    def test_extended_names_complete(self):
        """ARCHITECTURE.md Extended section must name every extended device type."""
        from mediascope.analyze.framing import _DEVICE_PATTERNS
        extended_types = set(_DEVICE_PATTERNS.keys()) - self.CORE_TYPES
        section_text = self._extract_architecture_extended_section()

        missing = []
        for code_name in sorted(extended_types):
            variants = self._code_name_to_display_variants(code_name)
            if not any(v in section_text for v in variants):
                missing.append(code_name)

        assert not missing, (
            f"ARCHITECTURE.md Extended device section is missing names for: "
            f"{missing}.\n"
            f"Expected {len(extended_types)} extended types; "
            f"{len(extended_types) - len(missing)} found.\n"
            f"Add each missing device name and description to the Extended "
            f"inline list."
        )

    def test_core_names_complete(self):
        """ARCHITECTURE.md Core section must name every core device type."""
        section_text = self._extract_architecture_core_section()

        missing = []
        for code_name in sorted(self.CORE_TYPES):
            variants = self._code_name_to_display_variants(code_name)
            if not any(v in section_text for v in variants):
                missing.append(code_name)

        assert not missing, (
            f"ARCHITECTURE.md Core device section is missing names for: "
            f"{missing}.\n"
            f"Expected {len(self.CORE_TYPES)} core types; "
            f"{len(self.CORE_TYPES) - len(missing)} found."
        )


class TestAgentGuideConsistency:
    """Guard: AGENT_GUIDE.md references to code counts and enumerations
    stay in sync.

    METHODOLOGY.md and QUALITY_STANDARDS.md have adversarial device list
    guards. AGENT_GUIDE.md also enumerates these types in the 'When
    Correction Fires' section, and states framing device tier counts in
    the detect_framing_devices function calling schema.

    Added: 2026-07-01 06:00 PT, Type D iteration.
    """

    def _adversarial_types_from_code(self) -> set[str]:
        """Get the adversarial device type set from sentiment.py."""
        src = (_REPO_ROOT / "mediascope" / "analyze" / "sentiment.py").read_text()
        match = re.search(
            r"_ADVERSARIAL_DEVICE_TYPES:\s*set\[str\]\s*=\s*\{(.*?)\}",
            src,
            re.DOTALL,
        )
        assert match, "Cannot find _ADVERSARIAL_DEVICE_TYPES in sentiment.py"
        return set(re.findall(r'"(\w+)"', match.group(1)))

    def test_agent_guide_adversarial_list_complete(self):
        """AGENT_GUIDE.md adversarial device list must match code."""
        code_types = self._adversarial_types_from_code()
        doc = (_REPO_ROOT / "docs" / "AGENT_GUIDE.md").read_text()
        # The list appears either as:
        # Old: "adversarial framing devices detected (list)"
        # New: "**Adversarial device types** (N types trigger Paths A/B): list."
        match = re.search(
            r"adversarial framing devices detected \(([^)]+)\)",
            doc,
        )
        if not match:
            match = re.search(
                r"\*\*Adversarial device types\*\*[^:]*:\s*([^.]+)\.",
                doc,
            )
        assert match, (
            "AGENT_GUIDE.md is missing the adversarial framing devices "
            "enumeration."
        )
        doc_types = set(re.findall(r"(\w+)", match.group(1)))
        # Remove stray words that aren't device types
        doc_types -= {"and", "or", "3"}
        missing = code_types - doc_types
        extra = doc_types - code_types
        assert not missing, (
            f"AGENT_GUIDE.md adversarial device list is missing: "
            f"{sorted(missing)}.\n"
            f"Code has: {sorted(code_types)}\n"
            f"Doc has: {sorted(doc_types)}"
        )
        assert not extra, (
            f"AGENT_GUIDE.md adversarial device list has extra types not "
            f"in code: {sorted(extra)}.\n"
            f"Code has: {sorted(code_types)}\n"
            f"Doc has: {sorted(doc_types)}"
        )

    # Canonical core types — same set used by TestArchitectureExtendedDeviceCount.
    # The "Core 10" is a documentation concept (the foundational device types),
    # not a code-structural distinction (the initial dict has more keys because
    # some Extended types were later moved into it for organization).
    CORE_TYPES = {
        "guilt_by_association", "anonymous_authority", "catastrophizing",
        "false_balance", "selective_omission_signal", "emotional_appeal",
        "loaded_language", "power_asymmetry", "ceo_personalization",
        "litigation_framing",
    }

    def test_agent_guide_total_device_count(self):
        """AGENT_GUIDE.md detect_framing_devices schema must state correct total."""
        from mediascope.analyze.framing import _DEVICE_PATTERNS
        src = (_REPO_ROOT / "mediascope" / "analyze" / "framing.py").read_text()
        pattern_keys = set(_DEVICE_PATTERNS.keys())
        initial_keys = set(re.findall(r'"(\w+)":\s*_[A-Z_]+_PATTERNS', src))
        dynamic_keys = set(re.findall(r'_DEVICE_PATTERNS\["(\w+)"\]', src))
        post_pass = set(re.findall(r'device_type="(\w+)"', src))
        structural = post_pass - initial_keys - dynamic_keys
        total = len(pattern_keys) + len(structural)

        doc = (_REPO_ROOT / "docs" / "AGENT_GUIDE.md").read_text()
        match = re.search(
            r"Detects (\d+) device types across three tiers:\s*"
            r"core \((\d+) pattern-matched\),\s*"
            r"extended \((\d+) from real-article analysis\),\s*"
            r".*?structural post-pass \((\d+)",
            doc,
        )
        assert match, (
            "AGENT_GUIDE.md detect_framing_devices schema is missing the "
            "'Detects N device types across three tiers' description."
        )
        claimed_total = int(match.group(1))
        claimed_core = int(match.group(2))
        claimed_extended = int(match.group(3))
        claimed_structural = int(match.group(4))

        core_count = len(self.CORE_TYPES)
        extended_count = len(pattern_keys) - core_count

        assert claimed_total == total, (
            f"AGENT_GUIDE.md claims {claimed_total} total device types "
            f"but code has {total}."
        )
        assert claimed_core == core_count, (
            f"AGENT_GUIDE.md claims {claimed_core} core types "
            f"but code has {core_count}."
        )
        assert claimed_extended == extended_count, (
            f"AGENT_GUIDE.md claims {claimed_extended} extended types "
            f"but code has {extended_count}."
        )
        assert claimed_structural == len(structural), (
            f"AGENT_GUIDE.md claims {claimed_structural} structural types "
            f"but code has {len(structural)}."
        )



class TestCorrectionPathDocumentation:
    """Validate that all 10 sentiment correction paths (A-J) are documented
    across METHODOLOGY.md, ARCHITECTURE.md, and AGENT_GUIDE.md.

    The 10 paths are defined in ``_compute_framing_correction`` (Paths A-F, H, I, J)
    and ``analyze_composite`` (Path G) in sentiment.py.  Each path has a
    ``# --- Path X: ...`` comment in code.  These tests ensure documentation
    stays in sync with code when paths are added, removed, or renamed.
    """

    EXPECTED_PATHS = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"}

    @staticmethod
    def _extract_code_paths():
        """Extract path labels from sentiment.py comment markers."""
        code = (
            _REPO_ROOT / "mediascope" / "analyze" / "sentiment.py"
        ).read_text()
        # Match patterns like "# --- Path A: Full correction ..."
        return set(re.findall(r"#\s*---\s*Path\s+([A-Z]):", code))

    def test_code_has_all_expected_paths(self):
        """sentiment.py should have comment markers for all 10 paths."""
        code_paths = self._extract_code_paths()
        missing = self.EXPECTED_PATHS - code_paths
        assert not missing, (
            f"Expected correction paths {missing} not found in sentiment.py "
            f"comment markers. Found: {sorted(code_paths)}"
        )

    def test_methodology_documents_all_paths(self):
        """METHODOLOGY.md section 9.2 should document all 10 correction paths."""
        doc = (_REPO_ROOT / "docs" / "METHODOLOGY.md").read_text()
        # Each path should appear as "#### Path X:" or "Path X" in text
        documented = set(re.findall(r"(?:####\s+)?Path\s+([A-J])[\s:.]", doc))
        missing = self.EXPECTED_PATHS - documented
        assert not missing, (
            f"METHODOLOGY.md is missing documentation for correction "
            f"paths: {sorted(missing)}. Documented: {sorted(documented)}"
        )

    def test_architecture_documents_all_paths(self):
        """ARCHITECTURE.md should reference all 10 correction paths."""
        doc = (_REPO_ROOT / "docs" / "ARCHITECTURE.md").read_text()
        documented = set(re.findall(r"Path\s+([A-J])[\s:.\|]", doc))
        missing = self.EXPECTED_PATHS - documented
        assert not missing, (
            f"ARCHITECTURE.md is missing references to correction "
            f"paths: {sorted(missing)}. Referenced: {sorted(documented)}"
        )

    def test_agent_guide_documents_all_paths(self):
        """AGENT_GUIDE.md should reference all 10 correction paths."""
        doc = (_REPO_ROOT / "docs" / "AGENT_GUIDE.md").read_text()
        documented = set(re.findall(r"Path\s+([A-J])[\s:.\|]", doc))
        # Also check for "**G**" table format
        table_paths = set(re.findall(r"\*\*([A-J])\*\*", doc))
        all_documented = documented | table_paths
        missing = self.EXPECTED_PATHS - all_documented
        assert not missing, (
            f"AGENT_GUIDE.md is missing references to correction "
            f"paths: {sorted(missing)}. Referenced: {sorted(all_documented)}"
        )

    def test_summary_table_in_methodology(self):
        """METHODOLOGY.md should have a summary table with all 10 paths."""
        doc = (_REPO_ROOT / "docs" / "METHODOLOGY.md").read_text()
        # Find the summary table by looking for "| **A**" through "| **G**"
        table_paths = set(re.findall(r"\|\s*\*\*([A-J])\*\*\s*\|", doc))
        missing = self.EXPECTED_PATHS - table_paths
        assert not missing, (
            f"METHODOLOGY.md summary table is missing paths: {sorted(missing)}. "
            f"Table has: {sorted(table_paths)}"
        )

    def test_path_count_consistent(self):
        """Code path count should match expected count of 10."""
        code_paths = self._extract_code_paths()
        assert len(code_paths) == len(self.EXPECTED_PATHS), (
            f"Expected {len(self.EXPECTED_PATHS)} correction paths but "
            f"code has {len(code_paths)}: {sorted(code_paths)}. "
            f"If a path was added or removed, update EXPECTED_PATHS and "
            f"all three documentation files."
        )

    def test_readme_correction_path_count(self):
        """README.md example table should reference correct path count (A-J)."""
        readme = (_REPO_ROOT / "README.md").read_text()
        expected_count = len(self.EXPECTED_PATHS)
        # The README example table describes the framing_correction_demo.py
        # and should reference the correct correction path count and range.
        assert f"{expected_count} distinct correction paths (A–J)" in readme, (
            f"README.md example table should reference "
            f"'{expected_count} distinct correction paths (A–J)' but does not. "
            f"Update the framing_correction_demo.py description in README.md."
        )

    def test_framing_demo_correction_path_count(self):
        """framing_correction_demo.py summary should reference correct path count."""
        demo = (
            _REPO_ROOT / "examples" / "framing_correction_demo.py"
        ).read_text()
        expected_count = len(self.EXPECTED_PATHS)
        # The demo prints "Ten correction paths (A-J)" in its summary
        count_word = {10: "Ten", 9: "Nine", 8: "Eight", 11: "Eleven"}.get(
            expected_count, str(expected_count)
        )
        assert f"{count_word} correction paths (A-J)" in demo, (
            f"framing_correction_demo.py summary should reference "
            f"'{count_word} correction paths (A-J)' but does not. "
            f"Update line ~314 in framing_correction_demo.py."
        )

    def test_sarcastic_demo_correction_path_count(self):
        """sarcastic_editorial_demo.py should reference correct correction path count."""
        demo = (
            _REPO_ROOT / "examples" / "sarcastic_editorial_demo.py"
        ).read_text()
        expected_count = len(self.EXPECTED_PATHS)
        assert f"all {expected_count} correction paths" in demo, (
            f"sarcastic_editorial_demo.py should reference "
            f"'all {expected_count} correction paths' but does not. "
            f"Update the test count line in sarcastic_editorial_demo.py."
        )


class TestJournalistCountConsistency:
    """Guard against stale journalist counts across documentation files.

    When journalists are added to profiles/careers/journalists.yaml,
    all documentation files that reference the journalist count or
    multi-publication count must be updated in the same commit.

    This test class reads the authoritative count from the YAML data
    and verifies that README.md, EDITORIAL_HISTORIES.md, and
    careers_demo.py all reference the correct numbers.
    """

    @staticmethod
    def _load_yaml_counts() -> tuple[int, int]:
        """Return (total_journalists, multi_pub_journalists) from YAML."""
        import yaml
        yaml_path = _REPO_ROOT / "profiles" / "careers" / "journalists.yaml"
        with open(yaml_path) as f:
            data = yaml.safe_load(f)
        journalists = data["journalists"]
        total = len(journalists)
        multi_pub = 0
        for j in journalists:
            pubs = set()
            for ev in j.get("career", []):
                pubs.add(ev.get("publication", ""))
            if len(pubs) >= 2:
                multi_pub += 1
        return total, multi_pub

    def test_readme_journalist_count(self):
        """README.md must reference correct total journalist count."""
        total, _ = self._load_yaml_counts()
        doc = (_REPO_ROOT / "README.md").read_text()
        expected = f"**{total} journalists**"
        assert expected in doc, (
            f"README.md should reference '{expected}' but doesn't. "
            f"YAML has {total} journalists. Update the README to match."
        )

    def test_editorial_histories_total_count(self):
        """EDITORIAL_HISTORIES.md must reference correct total count."""
        total, _ = self._load_yaml_counts()
        doc = (_REPO_ROOT / "docs" / "EDITORIAL_HISTORIES.md").read_text()
        expected = f"**{total} journalists**"
        assert expected in doc, (
            f"EDITORIAL_HISTORIES.md should reference '{expected}' but doesn't. "
            f"YAML has {total} journalists. Update the doc to match."
        )

    def test_editorial_histories_multi_pub_count(self):
        """EDITORIAL_HISTORIES.md must reference correct multi-pub count."""
        total, multi_pub = self._load_yaml_counts()
        doc = (_REPO_ROOT / "docs" / "EDITORIAL_HISTORIES.md").read_text()
        # Check for "{multi_pub} of these have multi-publication"
        expected_phrase = f"{multi_pub} of these have multi-publication"
        # Also check academic novelty: "with {multi_pub} having multi-publication"
        alt_phrase = f"with {multi_pub} having multi-publication"
        assert expected_phrase in doc or alt_phrase in doc, (
            f"EDITORIAL_HISTORIES.md should reference {multi_pub} multi-pub "
            f"journalists (from {total} total) but doesn't. "
            f"Searched for '{expected_phrase}' and '{alt_phrase}'."
        )

    def test_editorial_histories_no_stale_journalist_count(self):
        """All '**N journalists**' references in EDITORIAL_HISTORIES.md must use the current count."""
        total, _ = self._load_yaml_counts()
        doc = (_REPO_ROOT / "docs" / "EDITORIAL_HISTORIES.md").read_text()
        import re
        stale = []
        for m in re.finditer(r"\*\*(\d+)\s+journalists?\*\*", doc):
            stated = int(m.group(1))
            if stated != total:
                # Get line number for context
                line_no = doc[:m.start()].count("\n") + 1
                stale.append(f"  line {line_no}: **{stated} journalists** (should be {total})")
        assert not stale, (
            f"EDITORIAL_HISTORIES.md has stale journalist count(s):\n"
            + "\n".join(stale)
            + f"\nAll references should use {total} to match YAML data."
        )

    def test_editorial_histories_no_stale_multi_pub_count(self):
        """All multi-pub references in EDITORIAL_HISTORIES.md must use the current count."""
        _, multi_pub = self._load_yaml_counts()
        doc = (_REPO_ROOT / "docs" / "EDITORIAL_HISTORIES.md").read_text()
        import re
        stale = []
        # Check "N of these have multi-publication" pattern
        for m in re.finditer(r"(\d+)\s+of these have multi-publication", doc):
            stated = int(m.group(1))
            if stated != multi_pub:
                line_no = doc[:m.start()].count("\n") + 1
                stale.append(f"  line {line_no}: '{stated} of these' (should be {multi_pub})")
        # Check "with N having multi-publication" pattern
        for m in re.finditer(r"with\s+(\d+)\s+having multi-publication", doc):
            stated = int(m.group(1))
            if stated != multi_pub:
                line_no = doc[:m.start()].count("\n") + 1
                stale.append(f"  line {line_no}: 'with {stated} having' (should be {multi_pub})")
        assert not stale, (
            f"EDITORIAL_HISTORIES.md has stale multi-pub count(s):\n"
            + "\n".join(stale)
            + f"\nAll references should use {multi_pub} to match YAML data."
        )

    def test_careers_demo_count(self):
        """careers_demo.py docstring must reference correct journalist count."""
        total, _ = self._load_yaml_counts()
        demo = (_REPO_ROOT / "examples" / "careers_demo.py").read_text()
        expected = f"{total} tracked journalists"
        assert expected in demo, (
            f"careers_demo.py should reference '{expected}' but doesn't. "
            f"YAML has {total} journalists. Update the docstring to match."
        )

    def test_careers_demo_count_in_readme_table(self):
        """README.md careers_demo row must reference correct count."""
        total, _ = self._load_yaml_counts()
        doc = (_REPO_ROOT / "README.md").read_text()
        expected = f"{total} journalists"
        # The README table row for careers_demo.py should contain the count
        assert expected in doc, (
            f"README.md should reference '{expected}' but doesn't. "
            f"YAML has {total} journalists."
        )

    def test_tracker_loads_all_journalists(self):
        """CareerTracker.load() should parse all YAML journalists without error."""
        from mediascope.careers.tracker import CareerTracker
        t = CareerTracker()
        t.load()
        total_yaml, multi_pub_yaml = self._load_yaml_counts()
        journalists = t.all_journalists()
        assert len(journalists) == total_yaml, (
            f"CareerTracker loaded {len(journalists)} journalists but "
            f"YAML has {total_yaml}. Check for parse errors."
        )
        multi_pub_tracker = sum(
            1 for j in journalists if j.n_publications >= 2
        )
        assert multi_pub_tracker == multi_pub_yaml, (
            f"CareerTracker reports {multi_pub_tracker} multi-pub journalists "
            f"but YAML counting yields {multi_pub_yaml}. Check publication "
            f"slug consistency."
        )

    @staticmethod
    def _compute_migration_count() -> int:
        """Return total auto-detected migration count from CareerTracker."""
        from mediascope.careers.tracker import CareerTracker
        t = CareerTracker()
        t.load()
        return len(t.find_migrations())

    @staticmethod
    def _compute_publication_slug_count() -> int:
        """Return count of unique publication slugs across all career events."""
        import yaml
        yaml_path = _REPO_ROOT / "profiles" / "careers" / "journalists.yaml"
        with open(yaml_path) as f:
            data = yaml.safe_load(f)
        slugs = set()
        for j in data["journalists"]:
            for ev in j.get("career", []):
                pub = ev.get("publication", "")
                if pub:
                    slugs.add(pub)
        return len(slugs)

    def test_readme_careers_demo_migration_count(self):
        """README.md careers_demo table row must reference correct migration count."""
        migration_count = self._compute_migration_count()
        doc = (_REPO_ROOT / "README.md").read_text()
        expected = f"{migration_count} auto-detected migrations"
        assert expected in doc, (
            f"README.md careers_demo row should reference '{expected}' "
            f"but doesn't. CareerTracker finds {migration_count} migrations. "
            f"Update the careers_demo description in README.md."
        )

    def test_editorial_histories_migration_count(self):
        """EDITORIAL_HISTORIES.md must reference correct migration count."""
        migration_count = self._compute_migration_count()
        doc = (_REPO_ROOT / "docs" / "EDITORIAL_HISTORIES.md").read_text()
        expected = f"**{migration_count} migrations**"
        assert expected in doc, (
            f"EDITORIAL_HISTORIES.md should reference '{expected}' "
            f"but doesn't. CareerTracker finds {migration_count} migrations. "
            f"Update the migration count in EDITORIAL_HISTORIES.md."
        )

    def test_readme_publication_count_floor(self):
        """README.md publication count floor must not understate actual count by >20."""
        import re
        slug_count = self._compute_publication_slug_count()
        doc = (_REPO_ROOT / "README.md").read_text()
        # Look for patterns like "210+ publications" or "across 210+ publications"
        match = re.search(r"across (\d+)\+ publications", doc)
        assert match, (
            "README.md should contain 'across N+ publications' but doesn't."
        )
        stated_floor = int(match.group(1))
        assert stated_floor <= slug_count, (
            f"README.md claims '{stated_floor}+ publications' but only "
            f"{slug_count} unique publication slugs exist in YAML."
        )
        # Floor shouldn't understate by more than 20 (keep it reasonably current)
        assert slug_count - stated_floor <= 20, (
            f"README.md claims '{stated_floor}+ publications' but YAML has "
            f"{slug_count} unique slugs — floor is stale by "
            f"{slug_count - stated_floor}. Update to {slug_count // 10 * 10}+."
        )

    def test_editorial_histories_publication_count_floor(self):
        """EDITORIAL_HISTORIES.md publication count floor must not understate by >20."""
        import re
        slug_count = self._compute_publication_slug_count()
        doc = (_REPO_ROOT / "docs" / "EDITORIAL_HISTORIES.md").read_text()
        match = re.search(r"across (\d+)\+ publications", doc)
        assert match, (
            "EDITORIAL_HISTORIES.md should contain 'across N+ publications'."
        )
        stated_floor = int(match.group(1))
        assert stated_floor <= slug_count, (
            f"EDITORIAL_HISTORIES.md claims '{stated_floor}+ publications' "
            f"but only {slug_count} unique slugs exist."
        )
        assert slug_count - stated_floor <= 20, (
            f"EDITORIAL_HISTORIES.md claims '{stated_floor}+ publications' "
            f"but YAML has {slug_count}. Floor is stale by "
            f"{slug_count - stated_floor}. Update to {slug_count // 10 * 10}+."
        )


class TestEntityClusterConsistency:
    """Validate entity cluster reference documentation stays in sync with code."""

    def test_methodology_cluster_count(self):
        """METHODOLOGY.md §15 cluster count must match code."""
        import re
        from mediascope.analyze.entities import DEFAULT_ENTITY_CLUSTERS

        code_count = len(DEFAULT_ENTITY_CLUSTERS)
        doc = (_REPO_ROOT / "docs" / "METHODOLOGY.md").read_text()
        # Match "59 entity clusters" or "**59 entity clusters**"
        match = re.search(r"\*{0,2}(\d+) entity clusters\*{0,2}", doc)
        assert match, (
            "METHODOLOGY.md should contain 'N entity clusters' in §15."
        )
        stated_count = int(match.group(1))
        assert stated_count == code_count, (
            f"METHODOLOGY.md says {stated_count} entity clusters but "
            f"DEFAULT_ENTITY_CLUSTERS has {code_count}. "
            f"Update §15 to match."
        )

    def test_methodology_cluster_table_completeness(self):
        """Every cluster in code must appear in METHODOLOGY.md §15.3 reference table."""
        from mediascope.analyze.entities import DEFAULT_ENTITY_CLUSTERS

        doc = (_REPO_ROOT / "docs" / "METHODOLOGY.md").read_text()
        missing = []
        for cluster_name in DEFAULT_ENTITY_CLUSTERS:
            # Clusters appear as "| **Name** |" in the Markdown table
            if f"**{cluster_name}**" not in doc:
                missing.append(cluster_name)
        assert not missing, (
            f"METHODOLOGY.md §15.3 is missing {len(missing)} entity cluster(s) "
            f"that exist in code: {missing}. Add them to the reference table."
        )

    def test_no_phantom_clusters_in_docs(self):
        """METHODOLOGY.md §15.3 should not reference clusters that don't exist in code."""
        import re
        from mediascope.analyze.entities import DEFAULT_ENTITY_CLUSTERS

        doc = (_REPO_ROOT / "docs" / "METHODOLOGY.md").read_text()
        # Extract all bold items from §15.3 cluster tables
        # Pattern: "| **ClusterName** |"
        section_match = re.search(
            r"### 15\.3 Complete Cluster Reference(.+?)### 15\.4",
            doc,
            re.DOTALL,
        )
        if not section_match:
            return  # Section not yet structured — skip

        section_text = section_match.group(1)
        table_clusters = re.findall(r"\| \*\*([^*]+)\*\* \|", section_text)
        code_clusters = set(DEFAULT_ENTITY_CLUSTERS.keys())
        phantoms = [c for c in table_clusters if c not in code_clusters]
        assert not phantoms, (
            f"METHODOLOGY.md §15.3 references {len(phantoms)} cluster(s) "
            f"not in code: {phantoms}. Remove them or add to entities.py."
        )

    def test_cluster_alias_count_accuracy(self):
        """Alias counts in METHODOLOGY.md §15.3 must match code within reason."""
        import re
        from mediascope.analyze.entities import DEFAULT_ENTITY_CLUSTERS

        doc = (_REPO_ROOT / "docs" / "METHODOLOGY.md").read_text()
        section_match = re.search(
            r"### 15\.3 Complete Cluster Reference(.+?)### 15\.4",
            doc,
            re.DOTALL,
        )
        if not section_match:
            return

        section_text = section_match.group(1)
        # Extract "| **Name** | count |" patterns
        rows = re.findall(
            r"\| \*\*([^*]+)\*\* \| (\d+) \|",
            section_text,
        )
        mismatches = []
        for name, stated_str in rows:
            stated = int(stated_str)
            if name not in DEFAULT_ENTITY_CLUSTERS:
                continue
            cluster = DEFAULT_ENTITY_CLUSTERS[name]
            if isinstance(cluster, dict):
                actual = len(cluster.get("aliases", []))
            elif isinstance(cluster, list):
                actual = len(cluster)
            else:
                actual = 1
            if stated != actual:
                mismatches.append(
                    f"{name}: doc says {stated}, code has {actual}"
                )
        assert not mismatches, (
            f"Alias count mismatches in METHODOLOGY.md §15.3:\n"
            + "\n".join(mismatches)
        )



class TestAnnotatedArticleCountConsistency:
    """Guards: annotated article count in QUALITY_STANDARDS.md matches disk.

    QUALITY_STANDARDS.md §7 references the number of annotated articles in
    examples/sample_output/.  This count drifts silently whenever a Type A
    iteration adds a new article analysis — this test catches the drift.

    Added: 2026-07-03 15:00 PT, Type D iteration.
    """

    def test_quality_standards_annotated_article_count(self):
        """QUALITY_STANDARDS.md annotated article count matches actual files."""
        # Count *_analysis.md files on disk
        sample_dir = _REPO_ROOT / "examples" / "sample_output"
        actual = len(list(sample_dir.glob("*_analysis.md")))

        # Extract stated count from QUALITY_STANDARDS.md
        doc = (_REPO_ROOT / "docs" / "QUALITY_STANDARDS.md").read_text()
        match = re.search(r"All (\d+) annotated articles", doc)
        assert match, (
            "QUALITY_STANDARDS.md missing 'All N annotated articles' pattern. "
            "Expected in §7 Scoring Calibration Validation section."
        )
        stated = int(match.group(1))
        assert stated == actual, (
            f"QUALITY_STANDARDS.md says {stated} annotated articles but "
            f"examples/sample_output/ has {actual} *_analysis.md files. "
            f"Update the count in §7."
        )

    def test_methodology_annotated_article_count(self):
        """METHODOLOGY.md §17 annotated article count matches actual files.

        Added: 2026-07-06 14:00 PT, Type D iteration.
        """
        sample_dir = _REPO_ROOT / "examples" / "sample_output"
        actual = len(list(sample_dir.glob("*_analysis.md")))

        doc = (_REPO_ROOT / "docs" / "METHODOLOGY.md").read_text()
        # Match the §17.1 overview pattern
        match = re.search(
            r"corpus of \*\*(\d+) real articles\*\*", doc
        )
        assert match, (
            "METHODOLOGY.md §17.1 missing 'corpus of **N real articles**' pattern."
        )
        stated = int(match.group(1))
        assert stated == actual, (
            f"METHODOLOGY.md §17.1 says {stated} real articles but "
            f"examples/sample_output/ has {actual} *_analysis.md files. "
            f"Update §17 counts (§17.1, §17.2 tables, §17.3 trajectory, §17.5)."
        )

    def test_methodology_publication_count(self):
        """METHODOLOGY.md §17.2 publication count matches actual corpus diversity.

        Added: 2026-07-06 14:00 PT, Type D iteration.
        """
        sample_dir = _REPO_ROOT / "examples" / "sample_output"
        pubs = set()
        # Known publication prefixes → canonical name
        _PUB_PREFIXES = [
            # Tracked publications
            ("wired", "wired"),
            ("mit_tr", "mit_tech_review"),
            ("mittr", "mit_tech_review"),
            ("mit_tech_review", "mit_tech_review"),
            ("nyt", "nyt"),
            ("guardian", "guardian"),
            ("atlantic", "atlantic"),
            # Wire
            ("reuters", "reuters"),
            ("ap", "ap"),
            # Tech editorial
            ("gizmodo", "gizmodo"),
            ("memeburn", "memeburn"),
            ("engadget", "engadget"),
            ("register", "register"),
            ("techcrunch", "techcrunch"),
            ("techtimes", "techtimes"),
            ("techtarget", "techtarget"),
            ("9to5mac", "9to5mac"),
            ("android_authority", "android_authority"),
            ("digitaltrends", "digitaltrends"),
            ("malwarebytes", "malwarebytes"),
            ("livemint", "livemint"),
            # Financial
            ("barchart", "barchart"),
            ("barrons", "barrons"),
            ("marketwatch", "marketwatch"),
            ("motley_fool", "motley_fool"),
            ("pymnts", "pymnts"),
            ("stocktwits", "stocktwits"),
            ("thestreet", "thestreet"),
            # General interest
            ("fastco", "fast_company"),
            ("fastcompany", "fast_company"),
            ("avclub", "avclub"),
            ("cnn", "cnn"),
            ("futurism", "futurism"),
            ("iphoneincanada", "iphoneincanada"),
            ("kotaku", "kotaku"),
            ("newzlet", "newzlet"),
            ("webpronews", "webpronews"),
            ("multi_source", "multi_source"),
        ]
        for f in sample_dir.glob("*_analysis.md"):
            name = f.stem.replace("_analysis", "")
            matched = False
            for prefix, canonical in _PUB_PREFIXES:
                if name.startswith(prefix):
                    pubs.add(canonical)
                    matched = True
                    break
            if not matched:
                # Fallback: extract up to first year token
                parts = name.split("_")
                pub_parts = []
                for p in parts:
                    if re.match(r"^20\d{2}$", p):
                        break
                    pub_parts.append(p)
                pubs.add("_".join(pub_parts))

        # Exclude multi_source — it's a cross-outlet aggregation, not a publication
        pubs.discard("multi_source")

        doc = (_REPO_ROOT / "docs" / "METHODOLOGY.md").read_text()
        match = re.search(
            r"spans \*\*(\d+) distinct publications\*\*", doc
        )
        assert match, (
            "METHODOLOGY.md §17.2 missing '**N distinct publications**' pattern."
        )
        stated = int(match.group(1))
        assert stated == len(pubs), (
            f"METHODOLOGY.md §17.2 says {stated} distinct publications but "
            f"corpus has {len(pubs)} unique publication slugs. "
            f"Publications: {sorted(pubs)}"
        )

    def test_same_event_cluster_count(self):
        """QUALITY_STANDARDS.md same-event cluster count matches §10.2 tables."""
        doc = (_REPO_ROOT / "docs" / "QUALITY_STANDARDS.md").read_text()
        match = re.search(r"(\d+) distinct event clusters", doc)
        assert match, (
            "QUALITY_STANDARDS.md missing 'N distinct event clusters' pattern. "
            "Expected in §10.2 Validated Comparisons section."
        )
        stated = int(match.group(1))

        # Count data rows in the Tier 1 table (rows starting with "| "
        # that contain a date pattern like "(Jun 22)" or "(Jul 2–3)")
        tier1_section = doc.split("Tier 2")[0]
        tier1_section = tier1_section.split("Tier 1")[1] if "Tier 1" in tier1_section else tier1_section
        tier1_count = len(re.findall(
            r"^\| (?!Event|---|File)",
            tier1_section,
            re.MULTILINE,
        ))

        # Count data rows in the Tier 2 table
        tier2_start = doc.split("Tier 2")[1] if "Tier 2" in doc else ""
        tier2_section = tier2_start.split("Statistical Summary")[0] if "Statistical Summary" in tier2_start else tier2_start
        tier2_count = len(re.findall(
            r"^\| (?!Event|---|Notes|Outlets)",
            tier2_section,
            re.MULTILINE,
        ))

        total_clusters = tier1_count + tier2_count
        assert stated == total_clusters, (
            f"QUALITY_STANDARDS.md claims {stated} event clusters but "
            f"Tier 1 ({tier1_count}) + Tier 2 ({tier2_count}) tables "
            f"document {total_clusters} clusters. Update the stated count."
        )


# --- Atlantic pipeline and MIT TR partnership tests (2026-07-04 21:00 PT) ---

def _load_editorial_changes():
    """Load editorial_changes.yaml."""
    import yaml
    path = _REPO_ROOT / "profiles" / "careers" / "editorial_changes.yaml"
    with open(path) as f:
        return yaml.safe_load(f).get("editorial_changes", {})


def _load_journalists():
    """Load journalists.yaml."""
    import yaml
    path = _REPO_ROOT / "profiles" / "careers" / "journalists.yaml"
    with open(path) as f:
        return yaml.safe_load(f).get("journalists", [])


class TestAtlanticPipeline:
    """Tests for WaPo → Atlantic talent pipeline documentation."""

    def test_atlantic_editorial_changes_count(self):
        """Atlantic should have at least 24 editorial changes after spring 2026 batch."""
        ec = _load_editorial_changes()
        atlantic = ec.get("atlantic", [])
        assert len(atlantic) >= 24, f"Expected ≥24 Atlantic editorial changes, got {len(atlantic)}"

    def test_wapo_pipeline_hires_in_editorial_changes(self):
        """Spring 2026 WaPo → Atlantic batch hires should be tracked."""
        ec = _load_editorial_changes()
        atlantic = ec.get("atlantic", [])
        wapo_batch = [
            c for c in atlantic
            if isinstance(c, dict) and "WAPO" in str(c.get("notes", "")).upper()
            and str(c.get("date", "")).startswith("2026")
        ]
        assert len(wapo_batch) >= 3, (
            f"Expected ≥3 WaPo → Atlantic pipeline entries dated 2026, got {len(wapo_batch)}"
        )

    def test_theo_balcomb_migration_documented(self):
        """Theo Balcomb (NPR → NYT → WaPo → Atlantic) should be in Atlantic editorial changes."""
        ec = _load_editorial_changes()
        atlantic = ec.get("atlantic", [])
        balcomb = [c for c in atlantic if isinstance(c, dict) and c.get("incoming") == "Theo Balcomb"]
        assert len(balcomb) >= 1, "Theo Balcomb hire not found in Atlantic editorial changes"
        assert "NPR" in str(balcomb[0].get("notes", "")), "Balcomb notes should mention NPR migration origin"

    def test_caity_weaver_nyt_migration(self):
        """Caity Weaver (NYT Magazine → Atlantic) should be documented."""
        ec = _load_editorial_changes()
        atlantic = ec.get("atlantic", [])
        weaver = [c for c in atlantic if isinstance(c, dict) and c.get("incoming") == "Caity Weaver"]
        assert len(weaver) >= 1, "Caity Weaver hire not found in Atlantic editorial changes"
        assert "NYT" in str(weaver[0].get("notes", "")), "Weaver notes should mention NYT migration"


class TestMITTechReviewPartnership:
    """Tests for MIT TR × FT editorial partnership and Amy Nordrum promotion."""

    def test_nordrum_executive_editor_role(self):
        """Amy Nordrum should have executive_editor role at MIT TR."""
        journalists = _load_journalists()
        nordrum = next(
            (j for j in journalists if isinstance(j, dict) and j.get("name") == "Amy Nordrum"),
            None
        )
        assert nordrum is not None, "Amy Nordrum not found in journalists"
        exec_ed = [
            c for c in nordrum.get("career", [])
            if isinstance(c, dict)
            and c.get("publication") == "mit-tech-review"
            and c.get("role") == "executive_editor"
        ]
        assert len(exec_ed) >= 1, "Nordrum should have executive_editor role at MIT TR"

    def test_nordrum_career_progression(self):
        """Amy Nordrum should show commissioning_editor → executive_editor progression."""
        journalists = _load_journalists()
        nordrum = next(
            (j for j in journalists if isinstance(j, dict) and j.get("name") == "Amy Nordrum"),
            None
        )
        assert nordrum is not None
        mit_roles = [
            c.get("role") for c in nordrum.get("career", [])
            if isinstance(c, dict) and c.get("publication") == "mit-tech-review"
        ]
        assert "commissioning_editor" in mit_roles, "Missing commissioning_editor stage"
        assert "executive_editor" in mit_roles, "Missing executive_editor promotion"
