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


def count_tests():
    """Count test files and (by convention) total test count from last pytest run."""
    test_dir = os.path.join(REPO_ROOT, "tests")
    test_files = glob.glob(os.path.join(test_dir, "test_*.py"))
    return len(test_files)


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
    args = parser.parse_args()

    # Gather all counts
    entities = count_entity_clusters()
    framing = count_framing_devices()
    el_terms = count_emotional_language()
    adv_devices = count_adversarial_devices()
    correction_paths = count_sentiment_correction_paths()
    annotated = count_annotated_articles()
    careers = count_journalists()
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
        "Test files": test_files,
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
        }

        for label, pattern in checks:
            m = re.search(pattern, readme, re.IGNORECASE)
            if m:
                readme_val = int(m.group(1))
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
