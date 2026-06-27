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

    def test_total_device_types_is_32(self):
        """Code should define exactly 32 unique framing device types."""
        types = _all_device_types_from_code()
        assert len(types) == 32, (
            f"Expected 32 framing device types, got {len(types)}.\n"
            f"Types: {sorted(types)}\n"
            "If you added a new device, update this test AND the docs:\n"
            "  - docs/METHODOLOGY.md §4.1 total and tier counts\n"
            "  - docs/ARCHITECTURE.md framing device list\n"
            "  - docs/AGENT_GUIDE.md detect_framing_devices description\n"
            "  - mediascope/cli.py analyze command docstring\n"
            "  - README.md (if framing count is mentioned)"
        )

    def test_pattern_matched_types_is_29(self):
        """29 types should come from regex patterns (core + extended)."""
        src = (_REPO_ROOT / "mediascope" / "analyze" / "framing.py").read_text()
        pattern_keys = set(re.findall(r'_DEVICE_PATTERNS\["(\w+)"\]', src))
        initial_keys = set(re.findall(r'"(\w+)":\s*_[A-Z_]+_PATTERNS', src))
        pattern_types = initial_keys | pattern_keys
        assert len(pattern_types) == 29, (
            f"Expected 29 pattern-matched device types, got {len(pattern_types)}.\n"
            f"Types: {sorted(pattern_types)}"
        )

    def test_structural_post_pass_types_is_3(self):
        """3 types should come from structural post-pass (not pattern dict)."""
        src = (_REPO_ROOT / "mediascope" / "analyze" / "framing.py").read_text()
        pattern_keys = set(re.findall(r'_DEVICE_PATTERNS\["(\w+)"\]', src))
        initial_keys = set(re.findall(r'"(\w+)":\s*_[A-Z_]+_PATTERNS', src))
        post_pass = set(re.findall(r'device_type="(\w+)"', src))
        structural_only = post_pass - initial_keys - pattern_keys
        assert structural_only == {"kicker_framing", "analogy_stacking", "speculative_framing"}, (
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
        """ARCHITECTURE.md must say 32 framing device types."""
        doc = (_REPO_ROOT / "docs" / "ARCHITECTURE.md").read_text()
        assert "**32 framing device types**" in doc, (
            "ARCHITECTURE.md framing device count is stale. Should be 32."
        )

    def test_methodology_device_count(self):
        """METHODOLOGY.md must say 32 framing device types."""
        doc = (_REPO_ROOT / "docs" / "METHODOLOGY.md").read_text()
        assert "32 framing device types" in doc, (
            "METHODOLOGY.md framing device count is stale. Should be 32."
        )

    def test_agent_guide_device_count(self):
        """AGENT_GUIDE.md must say 32 device types."""
        doc = (_REPO_ROOT / "docs" / "AGENT_GUIDE.md").read_text()
        assert "32 device types" in doc, (
            "AGENT_GUIDE.md framing device count is stale. Should be 32."
        )

    def test_cli_analyze_device_count(self):
        """CLI analyze docstring must say 32 types."""
        cli_src = (_REPO_ROOT / "mediascope" / "cli.py").read_text()
        assert "32 types" in cli_src, (
            "CLI analyze command docstring framing device count is stale. Should be 32."
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
