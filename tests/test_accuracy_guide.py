"""Tests for ACCURACY_GUIDE.md documentation consistency.

Ensures accuracy statistics, correction path counts, and cross-references
stay in sync with the codebase and annotated example corpus.
"""
import os
import re
import glob

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ACCURACY_GUIDE = os.path.join(REPO_ROOT, "docs", "ACCURACY_GUIDE.md")
README = os.path.join(REPO_ROOT, "README.md")
AGENT_GUIDE = os.path.join(REPO_ROOT, "docs", "AGENT_GUIDE.md")
ARCHITECTURE = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
SAMPLE_OUTPUT = os.path.join(REPO_ROOT, "examples", "sample_output")


def _read(path):
    with open(path, "r") as f:
        return f.read()


class TestAccuracyGuideExists:
    def test_accuracy_guide_exists(self):
        assert os.path.exists(ACCURACY_GUIDE), "docs/ACCURACY_GUIDE.md must exist"

    def test_accuracy_guide_not_empty(self):
        content = _read(ACCURACY_GUIDE)
        assert len(content) > 5000, "ACCURACY_GUIDE.md should be substantial (>5KB)"


class TestAccuracyGuideCrossReferences:
    def test_readme_links_accuracy_guide(self):
        content = _read(README)
        assert "ACCURACY_GUIDE.md" in content, (
            "README.md must reference ACCURACY_GUIDE.md in the documentation table"
        )

    def test_agent_guide_links_accuracy_guide(self):
        content = _read(AGENT_GUIDE)
        assert "ACCURACY_GUIDE.md" in content, (
            "AGENT_GUIDE.md must reference ACCURACY_GUIDE.md"
        )

    def test_architecture_links_accuracy_guide(self):
        content = _read(ARCHITECTURE)
        assert "ACCURACY_GUIDE.md" in content, (
            "ARCHITECTURE.md must reference ACCURACY_GUIDE.md"
        )


class TestAccuracyGuideContent:
    def test_has_vader_polarity_section(self):
        content = _read(ACCURACY_GUIDE)
        assert "polarity inversion" in content.lower(), (
            "ACCURACY_GUIDE must document VADER polarity inversion"
        )

    def test_has_genre_accuracy_table(self):
        content = _read(ACCURACY_GUIDE)
        assert "Wire service" in content and "Sardonic" in content, (
            "ACCURACY_GUIDE must have genre-specific accuracy data"
        )

    def test_has_decision_tree(self):
        content = _read(ACCURACY_GUIDE)
        assert "Decision Tree" in content, (
            "ACCURACY_GUIDE must include a decision tree for interpreting results"
        )

    def test_has_correction_path_table(self):
        content = _read(ACCURACY_GUIDE)
        # Should reference all 12 paths
        for path in ["Path A", "Path B", "Path C", "Path D", "Path E", "Path F",
                      "Path H", "Path I", "Path J", "Path K", "Path L"]:
            assert path in content, (
                f"ACCURACY_GUIDE must document {path}"
            )

    def test_has_misinterpretation_patterns(self):
        content = _read(ACCURACY_GUIDE)
        assert "Mistake 1" in content and "Mistake 2" in content, (
            "ACCURACY_GUIDE must document common misinterpretation patterns"
        )

    def test_has_validation_checklist(self):
        content = _read(ACCURACY_GUIDE)
        assert "Validation Checklist" in content, (
            "ACCURACY_GUIDE must include an accuracy validation checklist"
        )

    def test_has_known_gaps(self):
        content = _read(ACCURACY_GUIDE)
        assert "not covered" in content.lower() or "known gaps" in content.lower(), (
            "ACCURACY_GUIDE must document known gaps in correction coverage"
        )


class TestAccuracyGuideAnnotatedCount:
    """Ensure the annotated article count in ACCURACY_GUIDE matches the actual corpus."""

    def test_annotated_count_matches_corpus(self):
        content = _read(ACCURACY_GUIDE)
        # Count actual analysis files
        analysis_files = glob.glob(os.path.join(SAMPLE_OUTPUT, "*_analysis.md"))
        actual_count = len(analysis_files)

        # Find the count mentioned in the guide (pattern: "176 annotated" or "176 manually annotated")
        match = re.search(r"(\d+)\s+(?:manually\s+)?annotated\s+article", content)
        assert match, "ACCURACY_GUIDE must state the annotated article count"
        stated_count = int(match.group(1))

        assert stated_count == actual_count, (
            f"ACCURACY_GUIDE states {stated_count} annotated articles but "
            f"corpus has {actual_count}. Update the guide."
        )
