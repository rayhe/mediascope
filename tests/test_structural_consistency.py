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
    """Guard: total framing device types in code match documented count."""

    def test_total_device_types_is_34(self):
        """Code should define exactly 34 unique framing device types."""
        types = _all_device_types_from_code()
        assert len(types) == 34, (
            f"Expected 34 framing device types, got {len(types)}.\n"
            f"Types: {sorted(types)}\n"
            "If you added a new device, update this test AND the docs:\n"
            "  - docs/METHODOLOGY.md §4.1 total and tier counts\n"
            "  - docs/ARCHITECTURE.md framing device list\n"
            "  - docs/AGENT_GUIDE.md detect_framing_devices description\n"
            "  - mediascope/cli.py analyze command docstring\n"
            "  - README.md (if framing count is mentioned)"
        )

    def test_pattern_matched_types_is_30(self):
        """30 types should come from regex patterns (core + extended)."""
        src = (_REPO_ROOT / "mediascope" / "analyze" / "framing.py").read_text()
        pattern_keys = set(re.findall(r'_DEVICE_PATTERNS\["(\w+)"\]', src))
        initial_keys = set(re.findall(r'"(\w+)":\s*_[A-Z_]+_PATTERNS', src))
        pattern_types = initial_keys | pattern_keys
        assert len(pattern_types) == 30, (
            f"Expected 30 pattern-matched device types, got {len(pattern_types)}.\n"
            f"Types: {sorted(pattern_types)}"
        )

    def test_structural_post_pass_types_is_4(self):
        """4 types should come from structural post-pass (not pattern dict)."""
        src = (_REPO_ROOT / "mediascope" / "analyze" / "framing.py").read_text()
        pattern_keys = set(re.findall(r'_DEVICE_PATTERNS\["(\w+)"\]', src))
        initial_keys = set(re.findall(r'"(\w+)":\s*_[A-Z_]+_PATTERNS', src))
        post_pass = set(re.findall(r'device_type="(\w+)"', src))
        structural_only = post_pass - initial_keys - pattern_keys
        assert structural_only == {"kicker_framing", "analogy_stacking", "speculative_framing", "trend_bundling"}, (
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
    """Guard: documented counts match across files."""

    def test_architecture_device_count(self):
        """ARCHITECTURE.md must say 34 framing device types."""
        doc = (_REPO_ROOT / "docs" / "ARCHITECTURE.md").read_text()
        assert "**34 framing device types**" in doc, (
            "ARCHITECTURE.md framing device count is stale. Should be 34."
        )

    def test_methodology_device_count(self):
        """METHODOLOGY.md must say 34 framing device types."""
        doc = (_REPO_ROOT / "docs" / "METHODOLOGY.md").read_text()
        assert "34 framing device types" in doc, (
            "METHODOLOGY.md framing device count is stale. Should be 34."
        )

    def test_agent_guide_device_count(self):
        """AGENT_GUIDE.md must say 34 device types."""
        doc = (_REPO_ROOT / "docs" / "AGENT_GUIDE.md").read_text()
        assert "34 device types" in doc, (
            "AGENT_GUIDE.md framing device count is stale. Should be 34."
        )

    def test_cli_analyze_device_count(self):
        """CLI analyze docstring must say 34 types."""
        cli_src = (_REPO_ROOT / "mediascope" / "cli.py").read_text()
        assert "34 types" in cli_src, (
            "CLI analyze command docstring framing device count is stale. Should be 34."
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
        """Code should define exactly 15 topic buckets."""
        from mediascope.analyze.topics import TOPIC_KEYWORDS
        assert len(TOPIC_KEYWORDS) == 15, (
            f"Expected 15 topic buckets, got {len(TOPIC_KEYWORDS)}.\n"
            f"Buckets: {sorted(TOPIC_KEYWORDS.keys())}\n"
            "If you added a new topic, update this test AND the docs:\n"
            "  - docs/METHODOLOGY.md §3.1 topic count and table\n"
            "  - docs/ARCHITECTURE.md topics list\n"
            "  - docs/AGENT_GUIDE.md classify_topic description"
        )

    def test_methodology_topic_count(self):
        """METHODOLOGY.md must say 15 topic buckets."""
        doc = (_REPO_ROOT / "docs" / "METHODOLOGY.md").read_text()
        assert "15 topic buckets" in doc, (
            "METHODOLOGY.md topic count is stale. Should be 15."
        )

    def test_agent_guide_topic_count(self):
        """AGENT_GUIDE.md must list 15 topic buckets."""
        doc = (_REPO_ROOT / "docs" / "AGENT_GUIDE.md").read_text()
        assert "15 topic buckets" in doc, (
            "AGENT_GUIDE.md topic count is stale. Should be 15."
        )

    def test_architecture_topic_count(self):
        """ARCHITECTURE.md must say 15 topic buckets."""
        doc = (_REPO_ROOT / "docs" / "ARCHITECTURE.md").read_text()
        assert "15 topic buckets" in doc, (
            "ARCHITECTURE.md topic count is stale. Should be 15."
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
