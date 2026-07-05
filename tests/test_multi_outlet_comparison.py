"""Tests for the N-way cross-outlet same-event comparison.

Validates ``compare_multi_articles()`` in ``examples/same_event_comparison.py``
and the 4-way Zuckerberg town hall cross-analysis file.
"""

import re
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parent.parent


class TestMultiOutletComparison:
    """Tests for the compare_multi_articles() function."""

    def test_compare_multi_articles_import(self):
        """compare_multi_articles is importable from examples module."""
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            "same_event_comparison",
            _REPO_ROOT / "examples" / "same_event_comparison.py",
        )
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        assert hasattr(mod, "compare_multi_articles")

    def test_compare_multi_articles_requires_min_2(self):
        """compare_multi_articles raises on <2 articles."""
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            "same_event_comparison",
            _REPO_ROOT / "examples" / "same_event_comparison.py",
        )
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)

        with pytest.raises(ValueError, match="at least 2"):
            mod.compare_multi_articles(
                [{}], ["Only One"], "test event"
            )

    def test_compare_multi_articles_length_mismatch(self):
        """compare_multi_articles raises on mismatched list lengths."""
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            "same_event_comparison",
            _REPO_ROOT / "examples" / "same_event_comparison.py",
        )
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)

        with pytest.raises(ValueError, match="same length"):
            mod.compare_multi_articles(
                [{}, {}], ["A", "B", "C"], "test event"
            )

    def test_compare_multi_articles_generates_matrix(self):
        """compare_multi_articles generates a comparison matrix with all outlets."""
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            "same_event_comparison",
            _REPO_ROOT / "examples" / "same_event_comparison.py",
        )
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)

        # Minimal mock articles using the analyze_article function
        from mediascope.analyze.sentiment import analyze_composite
        from mediascope.analyze.framing import detect_framing_devices

        text_a = "Meta CEO said progress is slower than expected."
        text_b = "The company admitted a catastrophic failure in AI development."
        text_c = "Zuckerberg's candid assessment reveals industry maturation."

        headlines = [
            "Meta says AI progress slower",
            "Meta admits AI failure",
            "Zuckerberg: AI industry maturing",
        ]
        pubs = ["Wire", "TechBlog", "Financial"]

        articles = []
        for text, headline in zip([text_a, text_b, text_c], headlines):
            sentiment = analyze_composite(text, headline)
            framing = detect_framing_devices(text)
            articles.append({
                "word_count": len(text.split()),
                "sentiment": sentiment,
                "framing_devices": framing,
                "framing_device_count": len(framing),
                "framing_device_types": sorted(set(d.device_type for d in framing)),
                "source_count": 0,
                "stance": {
                    "adversarial_count": 0,
                    "supportive_count": 0,
                    "neutral_count": 0,
                    "stance_balance": 0.0,
                },
                "outsourced_intensity": {"outsourced_ratio": 0.0},
            })

        report = mod.compare_multi_articles(
            articles, pubs, "Test Event",
            editorial_modes={"Wire": "wire", "TechBlog": "tech-editorial"},
        )

        # Should contain all publication names
        for pub in pubs:
            assert pub in report, f"Missing publication {pub} in report"

        # Should contain matrix headers
        assert "Tone Comparison Matrix" in report
        assert "Framing Device Comparison" in report
        assert "Source Deployment Comparison" in report
        assert "Interpretation" in report
        assert "Limitations" in report

        # Should contain tone range
        assert "Tone range:" in report


class TestTownHallCrossAnalysis:
    """Tests for the 4-way Zuckerberg town hall cross-analysis file."""

    _CROSS_FILE = (
        _REPO_ROOT / "examples" / "sample_output"
        / "town_hall_4way_cross_analysis_2026_07_02.md"
    )

    def test_cross_analysis_file_exists(self):
        """The 4-way cross-analysis file exists."""
        assert self._CROSS_FILE.exists(), (
            "Expected town_hall_4way_cross_analysis_2026_07_02.md "
            "in examples/sample_output/"
        )

    def test_cross_analysis_references_all_outlets(self):
        """The cross-analysis references all 4 outlets."""
        text = self._CROSS_FILE.read_text()
        for outlet in ["Reuters", "TechCrunch", "Barron's", "PYMNTS"]:
            assert outlet in text, (
                f"Cross-analysis missing outlet {outlet}"
            )

    def test_cross_analysis_has_comparison_matrix(self):
        """The cross-analysis has a tone comparison matrix."""
        text = self._CROSS_FILE.read_text()
        assert "Tone Comparison Matrix" in text
        assert "Framing Device Comparison" in text
        assert "Source Deployment Comparison" in text

    def test_cross_analysis_has_cross_publication_import(self):
        """The cross-analysis documents the TechCrunch cross-publication import."""
        text = self._CROSS_FILE.read_text()
        assert "cross_publication_import" in text.lower() or "Cross-Publication Import" in text

    def test_cross_analysis_tone_values_are_numeric(self):
        """Tone values in the comparison matrix are valid numbers."""
        text = self._CROSS_FILE.read_text()
        # Find the Overall tone row
        tone_match = re.search(
            r"\*\*Overall tone\*\*\s*\|([^\n]+)",
            text,
        )
        assert tone_match, "Missing Overall tone row in comparison matrix"
        values = tone_match.group(1).split("|")
        numeric_values = []
        for v in values:
            v = v.strip()
            if v and v != "---":
                # Replace Unicode minus (U+2212) with ASCII hyphen
                v = v.replace("\u2212", "-")
                # Should be parseable as float
                try:
                    numeric_values.append(float(v))
                except ValueError:
                    pytest.fail(f"Non-numeric tone value: {v!r}")
        assert len(numeric_values) == 4, (
            f"Expected 4 tone values, got {len(numeric_values)}"
        )

    def test_quality_standards_tier1_updated(self):
        """QUALITY_STANDARDS.md Tier 1 table includes PYMNTS in town hall cluster."""
        doc = (_REPO_ROOT / "docs" / "QUALITY_STANDARDS.md").read_text()
        # Find the town hall row
        town_hall_match = re.search(
            r"Zuckerberg town hall.*PYMNTS",
            doc,
        )
        assert town_hall_match, (
            "QUALITY_STANDARDS.md Tier 1 table missing PYMNTS in "
            "Zuckerberg town hall cluster"
        )
