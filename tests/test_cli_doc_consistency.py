"""
Structural consistency test: documented CLI examples vs. actual CLI flags.

Catches "phantom flags" — options documented in docs/*.md and README.md
that don't exist in the actual CLI. Discovered during Type D iteration
2026-07-14: TOPIC_REFERENCE.md documented --show-topics, --text, and --topic
flags that were never implemented.
"""

import re
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent


def _get_cli_flags():
    """Extract real CLI flags by running --help on every command."""
    flags_by_command = {}

    # Top-level commands
    top_commands = [
        "analyze", "score", "ingest", "report", "disclose",
        "add-publication", "list-publications", "status",
    ]
    for cmd in top_commands:
        out = subprocess.run(
            [sys.executable, "-m", "mediascope", cmd, "--help"],
            capture_output=True, text=True, cwd=str(REPO_ROOT),
        )
        found = set(re.findall(r"--[\w-]+", out.stdout))
        found.discard("--help")
        found.discard("--version")
        flags_by_command[cmd] = found

    # Careers subcommands
    careers_subs = ["list", "show", "migrations", "leadership", "diff", "analyze"]
    for sub in careers_subs:
        out = subprocess.run(
            [sys.executable, "-m", "mediascope", "careers", sub, "--help"],
            capture_output=True, text=True, cwd=str(REPO_ROOT),
        )
        found = set(re.findall(r"--[\w-]+", out.stdout))
        found.discard("--help")
        flags_by_command[f"careers {sub}"] = found

    return flags_by_command


def _extract_doc_cli_examples():
    """
    Parse all docs/*.md and README.md for lines starting with `mediascope`.
    Returns list of (file, line_number, command, flags_used).
    """
    examples = []
    doc_files = list((REPO_ROOT / "docs").glob("*.md")) + [REPO_ROOT / "README.md"]

    # Pattern: line starting with mediascope (possibly inside a code block)
    cli_pattern = re.compile(r"^\s*mediascope\s+(.+)$")
    flag_pattern = re.compile(r"--[\w-]+")

    # Map short flags to their long equivalents
    short_to_long = {
        "-p": "--publication",
        "-t": "--target",
        "-o": "--output",
        "-n": "--name",
        "-s": "--slug",
        "-u": "--url",
        "-i": "--interactive",
    }

    for doc_file in doc_files:
        if not doc_file.exists():
            continue
        lines = doc_file.read_text().splitlines()
        for i, line in enumerate(lines, 1):
            m = cli_pattern.match(line)
            if not m:
                continue
            rest = m.group(1).strip()

            # Determine the command
            # Handle "careers <sub>" as a compound command
            tokens = rest.split()
            if not tokens:
                continue

            if tokens[0] == "careers" and len(tokens) > 1:
                cmd = f"careers {tokens[1]}"
            else:
                cmd = tokens[0]

            # Extract flags
            flags = set(flag_pattern.findall(rest))
            # Convert short flags
            resolved_flags = set()
            for f in flags:
                if f in short_to_long:
                    resolved_flags.add(short_to_long[f])
                else:
                    resolved_flags.add(f)
            resolved_flags.discard("--help")
            resolved_flags.discard("--version")

            if resolved_flags:
                examples.append((
                    doc_file.name,
                    i,
                    cmd,
                    resolved_flags,
                ))

    return examples


# Cache expensive CLI introspection
_CLI_FLAGS = None


def _get_cached_cli_flags():
    global _CLI_FLAGS
    if _CLI_FLAGS is None:
        _CLI_FLAGS = _get_cli_flags()
    return _CLI_FLAGS


def test_no_phantom_cli_flags_in_docs():
    """
    Every --flag used in a documented CLI example must exist in the
    actual CLI command's --help output.

    Catches documentation drift where flags are documented but never
    implemented, or removed from the CLI without updating docs.
    """
    cli_flags = _get_cached_cli_flags()
    doc_examples = _extract_doc_cli_examples()

    phantom_flags = []
    for doc_file, line_num, cmd, flags in doc_examples:
        if cmd not in cli_flags:
            # Unknown command — skip (could be a different kind of doc bug)
            continue
        valid = cli_flags[cmd]
        for flag in flags:
            if flag not in valid:
                phantom_flags.append(
                    f"  {doc_file}:{line_num} — `{cmd}` has no `{flag}` flag "
                    f"(valid: {sorted(valid)})"
                )

    assert not phantom_flags, (
        f"Found {len(phantom_flags)} phantom CLI flag(s) in documentation:\n"
        + "\n".join(phantom_flags)
        + "\n\nFix the docs to use real flags, or add the flags to the CLI."
    )


def test_documented_commands_are_real():
    """
    Every command referenced in a documented CLI example must be a real
    CLI command (top-level or careers subcommand).
    """
    cli_flags = _get_cached_cli_flags()
    doc_examples = _extract_doc_cli_examples()

    # Also collect zero-flag examples (commands without options)
    doc_files = list((REPO_ROOT / "docs").glob("*.md")) + [REPO_ROOT / "README.md"]
    cli_pattern = re.compile(r"^\s*mediascope\s+(\S+)")

    all_doc_commands = set()
    for doc_file in doc_files:
        if not doc_file.exists():
            continue
        for line in doc_file.read_text().splitlines():
            m = cli_pattern.match(line)
            if m:
                cmd = m.group(1).strip()
                all_doc_commands.add(cmd)

    # "careers" alone is a group, not a command — skip it
    all_doc_commands.discard("careers")

    unknown = all_doc_commands - set(cli_flags.keys())
    # careers subcommands show up as bare words, which is expected
    # Filter out things that are compound commands handled above
    truly_unknown = {c for c in unknown if c not in (
        "list", "show", "migrations", "leadership", "diff",
        # These are valid subcommands parsed as top-level in the regex
    )}

    # We only flag truly unknown top-level commands
    assert not truly_unknown, (
        f"Documentation references unknown CLI commands: {sorted(truly_unknown)}"
    )
