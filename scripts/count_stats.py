#!/usr/bin/env python3
"""Auto-count MediaScope pipeline statistics for README verification.

Run this script to check whether README.md stats are current:

    python3 scripts/count_stats.py          # print current counts
    python3 scripts/count_stats.py --check  # exit 1 if README is stale

All counts are derived from the codebase — no manual maintenance needed.
"""

import argparse
import glob
import os
import re
import sys

# Ensure the repo root is importable
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_ROOT)


def count_entity_clusters():
    """Count entity clusters, aliases, regex patterns, and auto-generated clusters."""
    from mediascope.analyze.entities import DEFAULT_ENTITY_CLUSTERS as ec

    cluster_count = len(ec)
    alias_count = sum(len(v.get("aliases", [])) for v in ec.values())
    regex_count = sum(1 for v in ec.values() if v.get("regex"))
    auto_count = cluster_count - regex_count  # clusters without custom regex (alias-only)
    return {
        "entity_clusters": cluster_count,
        "entity_aliases": alias_count,
        "entity_regex": regex_count,
        "entity_auto": auto_count,
    }


def count_framing_devices():
    """Count framing device types and compiled regex patterns."""
    framing_path = os.path.join(REPO_ROOT, "mediascope", "analyze", "framing.py")
    with open(framing_path) as f:
        content = f.read()

    # Count entries in the _DEVICE_PATTERNS dispatch dict
    initial = re.findall(r'"(\w+)"\s*:\s*_\w+_PATTERNS', content)
    additions = re.findall(r'_DEVICE_PATTERNS\["(\w+)"\]', content)
    pattern_based = len(set(initial + additions))

    # Count structural post-pass types (device_type="..." in detect function)
    structural = re.findall(r'device_type="(\w+)"', content)
    structural_types = set(structural) - set(initial + additions)

    # Count compiled regex patterns
    compiled = len(re.findall(r"re\.compile\(", content))

    return {
        "framing_pattern_based": pattern_based,
        "framing_structural": len(structural_types),
        "framing_total": pattern_based + len(structural_types),
        "framing_compiled_patterns": compiled,
    }


def count_emotional_language():
    """Count emotional language terms in the sentiment lexicon."""
    from mediascope.analyze.sentiment import EMOTIONAL_LANGUAGE

    return len(EMOTIONAL_LANGUAGE)


def count_adversarial_devices():
    """Count adversarial device types used by sentiment correction."""
    from mediascope.analyze.sentiment import _ADVERSARIAL_DEVICE_TYPES

    return len(_ADVERSARIAL_DEVICE_TYPES)


def count_sentiment_correction_paths():
    """Count sentiment correction paths (A, B, C, ...) in the sentiment module."""
    sentiment_path = os.path.join(REPO_ROOT, "mediascope", "analyze", "sentiment.py")
    with open(sentiment_path) as f:
        content = f.read()
    paths = set(re.findall(r"Path ([A-Z])", content))
    return len(paths)


def count_annotated_articles():
    """Count annotated article analyses in examples/sample_output/."""
    sample_dir = os.path.join(REPO_ROOT, "examples", "sample_output")
    if not os.path.isdir(sample_dir):
        return 0
    return len(glob.glob(os.path.join(sample_dir, "*_analysis.md")))


def count_journalists():
    """Count journalists, migrations, and publications from career YAML files."""
    try:
        import yaml
    except ImportError:
        return {"journalists": "?", "migrations": "?", "publications": "?"}

    careers_dir = os.path.join(REPO_ROOT, "profiles", "careers")
    total_journalists = 0
    total_migrations = 0
    total_pubs = set()

    for f in glob.glob(os.path.join(careers_dir, "*.yaml")):
        with open(f) as fh:
            data = yaml.safe_load(fh)
        if not isinstance(data, dict):
            continue
        journalists = data.get("journalists", [])
        total_journalists += len(journalists)
        for j in journalists:
            entries = j.get("career", [])
            if len(entries) > 1:
                total_migrations += len(entries) - 1
            for e in entries:
                pub = e.get("publication")
                if pub:
                    total_pubs.add(pub)

    return {
        "journalists": total_journalists,
        "migrations": total_migrations,
        "publications": len(total_pubs),
    }


def _count_top_level_items(text: str) -> int:
    """Count top-level comma-separated items in a parametrize list.

    Tracks parenthesis/bracket depth so commas inside tuples like
    ``("phrase", True)`` are not counted as item separators.
    """
    text = text.strip()
    if not text:
        return 0
    count = 1
    depth = 0
    in_string = None
    last_comma_at_depth_zero = False
    i = 0
    while i < len(text):
        c = text[i]
        if in_string is not None:
            if c == "\\" and i + 1 < len(text):
                i += 2
                continue
            if c == in_string:
                in_string = None
        else:
            if c == "#":
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
    if last_comma_at_depth_zero:
        count -= 1
    return count


def _resolve_variable_list(var_name, content):
    """Resolve a variable to its list items count.

    Looks for ``VAR_NAME = [...]`` at module level OR class level (indented)
    and counts top-level items.  Returns the item count, or 0 if the variable
    cannot be resolved.
    """
    # Try module scope first (no leading whitespace), then class scope (indented)
    for scope_prefix in (r"^", r"^\s+"):
        pattern = re.compile(
            scope_prefix + re.escape(var_name) + r"\s*=\s*\[(.*?)\]",
            re.MULTILINE | re.DOTALL,
        )
        m = pattern.search(content)
        if m:
            items_text = m.group(1).strip()
            if not items_text:
                return 0
            return _count_top_level_items(items_text)
    return 0


def count_tests():
    """Count test files and total test cases (def test_ + parametrize expansions).

    Handles both inline ``@pytest.mark.parametrize("x", [...])`` and
    variable-reference ``@pytest.mark.parametrize("x", MY_LIST, ...)`` patterns,
    with both single- and double-quoted parameter names.
    """
    test_dir = os.path.join(REPO_ROOT, "tests")
    test_files = glob.glob(os.path.join(test_dir, "test_*.py"))
    file_count = len(test_files)

    # Count def test_ functions
    total = 0
    for tf in test_files:
        with open(tf) as f:
            content = f.read()
        total += len(re.findall(r"^\s+def test_", content, re.MULTILINE))

    # Count parametrize expansions — inline lists (single or double quotes)
    extra = 0
    for tf in test_files:
        with open(tf) as f:
            content = f.read()

        # Pattern 1: inline list  @pytest.mark.parametrize("x", [...])
        for m in re.finditer(
            r"""@pytest\.mark\.parametrize\(\s*["'][^"']+["'],\s*\[(.*?)\]""",
            content,
            re.DOTALL,
        ):
            items_text = m.group(1).strip()
            if not items_text:
                continue
            n_items = _count_top_level_items(items_text)
            if n_items > 1:
                extra += n_items - 1

        # Pattern 2: variable reference  @pytest.mark.parametrize("x", VAR_NAME)
        # or  @pytest.mark.parametrize("x", VAR_NAME, indirect=...)
        for m in re.finditer(
            r"""@pytest\.mark\.parametrize\(\s*["'][^"']+["'],\s*([A-Z_][A-Z0-9_]+)""",
            content,
        ):
            var_name = m.group(1)
            # Skip if this is actually an inline list (already counted above)
            # by checking if the char after var_name is a comma, paren, or newline
            n_items = _resolve_variable_list(var_name, content)
            if n_items > 1:
                extra += n_items - 1

    return {"test_files": file_count, "total_tests": total + extra}


def count_tests_pytest():
    """Count tests using pytest --collect-only (authoritative, slower).

    Falls back to regex-based count_tests() if pytest collection fails.
    Returns the same dict shape as count_tests().
    """
    import subprocess

    test_dir = os.path.join(REPO_ROOT, "tests")
    test_files = glob.glob(os.path.join(test_dir, "test_*.py"))
    file_count = len(test_files)

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "--collect-only", "-q"],
            capture_output=True,
            text=True,
            timeout=120,
            cwd=REPO_ROOT,
        )
        for line in result.stdout.strip().split("\n"):
            m = re.search(r"(\d+)\s+tests?\s+collected", line)
            if m:
                return {"test_files": file_count, "total_tests": int(m.group(1))}
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
        pass

    # Fall back to regex count
    return count_tests()


def count_topics():
    """Count topic buckets from the topic classification module."""
    try:
        from mediascope.analyze.topics import TOPIC_TAXONOMY

        return len(TOPIC_TAXONOMY)
    except (ImportError, AttributeError):
        # Fall back to counting from docs
        topic_ref = os.path.join(REPO_ROOT, "docs", "TOPIC_REFERENCE.md")
        if os.path.isfile(topic_ref):
            with open(topic_ref) as f:
                content = f.read()
            buckets = re.findall(r"^\|\s*\d+\s*\|", content, re.MULTILINE)
            return len(buckets)
        return "?"


def main():
    parser = argparse.ArgumentParser(description="Count MediaScope pipeline statistics")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check README.md stats against actual counts; exit 1 if stale",
    )
    parser.add_argument(
        "--pytest",
        action="store_true",
        help="Use pytest --collect-only for authoritative test count (slower but exact)",
    )
    args = parser.parse_args()

    # Gather all counts
    entities = count_entity_clusters()
    framing = count_framing_devices()
    el_terms = count_emotional_language()
    adv_devices = count_adversarial_devices()
    correction_paths = count_sentiment_correction_paths()
    annotated = count_annotated_articles()
    careers = count_journalists()
    if args.pytest or args.check:
        test_files = count_tests_pytest()
    else:
        test_files = count_tests()
    topics = count_topics()

    stats = {
        "Entity clusters": entities["entity_clusters"],
        "Entity aliases": entities["entity_aliases"],
        "Entity regex": entities["entity_regex"],
        "Entity auto-generated": entities["entity_auto"],
        "Framing device types (total)": framing["framing_total"],
        "  Pattern-based": framing["framing_pattern_based"],
        "  Structural (post-pass)": framing["framing_structural"],
        "Compiled framing patterns": framing["framing_compiled_patterns"],
        "Emotional language terms": el_terms,
        "Adversarial device types": adv_devices,
        "Sentiment correction paths": correction_paths,
        "Annotated articles": annotated,
        "Journalists tracked": careers["journalists"],
        "Career-entry migrations": careers["migrations"],
        "Distinct publications": careers["publications"],
        "Topic buckets": topics,
        "Test files": test_files["test_files"],
        "Total tests": test_files["total_tests"],
    }

    # Print table
    max_label = max(len(k) for k in stats)
    print("\nMediaScope Pipeline Statistics")
    print("=" * (max_label + 12))
    for label, value in stats.items():
        print(f"  {label:<{max_label}}  {value:>6}")
    print()

    if args.check:
        readme_path = os.path.join(REPO_ROOT, "README.md")
        with open(readme_path) as f:
            readme = f.read()

        # Extract stats from the README table
        stale = []
        checks = [
            ("Entity clusters", r"\|\s*Entity clusters\s*\|\s*(\d+)"),
            ("Framing device types", r"\|\s*Framing device types\s*\|\s*(\d+)"),
            ("Framing patterns", r"\|\s*Framing patterns\s*\|\s*(\d+)"),
            ("Emotional language terms", r"\|\s*Emotional language terms\s*\|\s*(\d+)"),
            ("Adversarial device types", r"\|\s*Adversarial device types\s*\|\s*(\d+)"),
            ("Sentiment correction paths", r"\|\s*Sentiment correction paths\s*\|\s*(\d+)"),
            ("Annotated articles", r"\|\s*Annotated articles\s*\|\s*(\d+)"),
            ("Journalists tracked", r"\|\s*Journalists tracked\s*\|\s*(\d+)"),
            ("Career-entry migrations", r"\|\s*Career-entry migrations\s*\|\s*(\d+)"),
            ("Tests", r"\|\s*Tests\s*\|\s*([\d,]+)"),
        ]

        actual_map = {
            "Entity clusters": entities["entity_clusters"],
            "Framing device types": framing["framing_total"],
            "Framing patterns": framing["framing_compiled_patterns"],
            "Emotional language terms": el_terms,
            "Adversarial device types": adv_devices,
            "Sentiment correction paths": correction_paths,
            "Annotated articles": annotated,
            "Journalists tracked": careers["journalists"],
            "Career-entry migrations": careers["migrations"],
            "Tests": test_files["total_tests"],
        }

        for label, pattern in checks:
            m = re.search(pattern, readme, re.IGNORECASE)
            if m:
                readme_val = int(m.group(1).replace(",", ""))
                actual_val = actual_map[label]
                if readme_val != actual_val:
                    stale.append(f"  {label}: README={readme_val}, actual={actual_val}")

        if stale:
            print("❌ README stats are STALE:")
            for s in stale:
                print(s)
            sys.exit(1)
        else:
            print("✅ README stats are current.")
            sys.exit(0)


if __name__ == "__main__":
    main()
