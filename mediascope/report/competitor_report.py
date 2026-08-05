"""Competitor coverage comparison report generator.

Generates cross-entity comparison reports showing financial tie →
coverage tone correlations and identifying protected entities.

Usage::

    from mediascope.analyze.competitor import CompetitorAnalyzer
    from mediascope.report.competitor_report import CompetitorReport

    analyzer = CompetitorAnalyzer(profiles_dir="profiles")
    matrix = analyzer.build_asymmetry_matrix(articles)
    report = CompetitorReport(analyzer, matrix)
    print(report.render_text())
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from mediascope.analyze.competitor import (
    CompetitorAnalyzer,
    CoverageAsymmetryMatrix,
    ENTITY_DISPLAY_NAMES,
    COMPETITOR_ENTITIES,
)


@dataclass
class CompetitorReport:
    """Generate cross-entity coverage comparison reports."""

    analyzer: CompetitorAnalyzer
    matrix: CoverageAsymmetryMatrix

    def render_text(self) -> str:
        """Render a full text report of cross-entity coverage asymmetry."""
        lines = []
        lines.append("=" * 72)
        lines.append("MEDIASCOPE: CROSS-ENTITY COVERAGE ASYMMETRY REPORT")
        lines.append("=" * 72)
        lines.append("")

        # Section 1: Financial Relationship Summary
        lines.append("1. FINANCIAL RELATIONSHIP MATRIX")
        lines.append("-" * 40)
        lines.append("")
        lines.append(self._render_relationship_matrix())
        lines.append("")

        # Section 2: Coverage Tone Matrix
        lines.append("2. COVERAGE TONE SCORES")
        lines.append("-" * 40)
        lines.append("")
        lines.append(self._render_tone_matrix())
        lines.append("")

        # Section 3: Financial Correlation
        lines.append("3. FINANCIAL TIE → COVERAGE TONE CORRELATION")
        lines.append("-" * 40)
        lines.append("")
        correlation = self.analyzer.compute_financial_correlation(self.matrix)
        lines.append(f"  Avg tone when PAID:         {correlation['paid_avg_tone']:+.3f} (n={correlation['paid_count']})")
        lines.append(f"  Avg tone when NOT PAID:     {correlation['unpaid_avg_tone']:+.3f} (n={correlation['unpaid_count']})")
        lines.append(f"  Avg tone when ADVERSARIAL:  {correlation['adversarial_avg_tone']:+.3f} (n={correlation['adversarial_count']})")
        lines.append(f"  Gap (paid vs unpaid):       {correlation['tone_gap_paid_vs_unpaid']:+.3f}")
        lines.append(f"  Gap (paid vs adversarial):  {correlation['tone_gap_paid_vs_adversarial']:+.3f}")
        lines.append("")

        # Section 4: Protected Entities
        lines.append("4. PROTECTED ENTITIES (softer coverage from paying publishers)")
        lines.append("-" * 40)
        lines.append("")
        protected = self.analyzer.identify_protected_entities(self.matrix)
        if protected:
            for p in protected:
                lines.append(
                    f"  {p['publication']:20s} → {p['entity']:12s} "
                    f"tone={p['tone_score']:+.3f}  "
                    f"tie={p['financial_tie']}  "
                    f"value={p['estimated_value']}"
                )
        else:
            lines.append("  No protected entities detected above threshold.")
        lines.append("")

        # Section 5: Most Asymmetric Pairs
        lines.append("5. MOST ASYMMETRIC COVERAGE PAIRS")
        lines.append("-" * 40)
        lines.append("")
        asymmetric = self.matrix.most_asymmetric(10)
        for cell in asymmetric:
            if cell.coverage.article_count == 0:
                continue
            entity_name = ENTITY_DISPLAY_NAMES.get(cell.entity, cell.entity)
            lines.append(
                f"  {cell.publication:20s} × {entity_name:12s} "
                f"tone={cell.coverage.tone_score:+.3f}  "
                f"tie={cell.relationship.financial_tie}  "
                f"asymmetry={cell.asymmetry_score:+.3f}"
            )
        lines.append("")

        # Section 6: The Hypothesis Test
        lines.append("6. HYPOTHESIS TEST: DO FINANCIAL TIES PREDICT COVERAGE TONE?")
        lines.append("-" * 40)
        lines.append("")
        lines.append(self._render_hypothesis_test(correlation))
        lines.append("")

        lines.append("=" * 72)
        lines.append("END OF REPORT")
        lines.append("=" * 72)

        return "\n".join(lines)

    def _render_relationship_matrix(self) -> str:
        """Render the financial relationship matrix as text."""
        lines = []
        header = f"  {'Publication':20s}"
        for entity in COMPETITOR_ENTITIES:
            name = ENTITY_DISPLAY_NAMES.get(entity, entity)
            header += f" {name:>10s}"
        lines.append(header)
        lines.append("  " + "-" * (20 + 11 * len(COMPETITOR_ENTITIES)))

        for pub_slug in self.matrix.publications:
            row = f"  {pub_slug:20s}"
            for entity in COMPETITOR_ENTITIES:
                rel = self.analyzer.get_relationship(pub_slug, entity)
                if rel:
                    symbol = _tie_symbol(rel.financial_tie)
                else:
                    symbol = "?"
                row += f" {symbol:>10s}"
            lines.append(row)

        lines.append("")
        lines.append("  Legend: $ = licensing, $$ = investment, ⚖ = adversarial/litigation,")
        lines.append("         ~ = indirect/mixed, ○ = none, ? = unknown")
        return "\n".join(lines)

    def _render_tone_matrix(self) -> str:
        """Render the coverage tone matrix as text."""
        lines = []
        header = f"  {'Publication':20s}"
        for entity in COMPETITOR_ENTITIES:
            name = ENTITY_DISPLAY_NAMES.get(entity, entity)
            header += f" {name:>10s}"
        lines.append(header)
        lines.append("  " + "-" * (20 + 11 * len(COMPETITOR_ENTITIES)))

        for pub_slug in self.matrix.publications:
            row = f"  {pub_slug:20s}"
            for entity in COMPETITOR_ENTITIES:
                cell = self.matrix.get(pub_slug, entity)
                if cell and cell.coverage.article_count > 0:
                    row += f" {cell.coverage.tone_score:>+10.3f}"
                else:
                    row += f" {'n/a':>10s}"
            lines.append(row)

        return "\n".join(lines)

    def _render_hypothesis_test(self, correlation: dict[str, Any]) -> str:
        """Render the hypothesis test conclusion."""
        lines = []
        gap = correlation["tone_gap_paid_vs_unpaid"]

        if abs(gap) < 0.05:
            verdict = "INCONCLUSIVE"
            explanation = (
                "The tone gap between paid and unpaid coverage is minimal "
                f"({gap:+.3f}). Financial ties do not appear to significantly "
                "predict coverage tone in this sample."
            )
        elif gap > 0.15:
            verdict = "SUPPORTED"
            explanation = (
                f"Publications that receive money from an entity cover it "
                f"{gap:+.3f} points more favorably on average than entities "
                f"they have no financial tie to. This supports the hypothesis "
                f"that financial ties predict softer coverage."
            )
        elif gap > 0.05:
            verdict = "WEAKLY SUPPORTED"
            explanation = (
                f"There is a modest positive correlation ({gap:+.3f}) between "
                f"financial ties and favorable coverage, but the effect size "
                f"is small. More data needed."
            )
        elif gap < -0.05:
            verdict = "NOT SUPPORTED"
            explanation = (
                f"Financial ties appear to produce HARSHER coverage ({gap:+.3f}), "
                f"contradicting the hypothesis. This may indicate editorial "
                f"overcorrection to demonstrate independence from paying partners."
            )
        else:
            verdict = "INCONCLUSIVE"
            explanation = f"No clear pattern detected. Gap: {gap:+.3f}"

        lines.append(f"  Verdict: {verdict}")
        lines.append(f"  {explanation}")
        lines.append("")
        lines.append("  KEY COMPARISON:")
        lines.append(
            f"    WIRED covers Meta at [X] tone but covers OpenAI at [Y] tone"
        )
        lines.append(
            f"    — OpenAI pays WIRED (via Condé Nast), Meta doesn't"
        )

        return "\n".join(lines)

    def render_json(self) -> dict[str, Any]:
        """Render the report as a JSON-serializable dict."""
        correlation = self.analyzer.compute_financial_correlation(self.matrix)
        protected = self.analyzer.identify_protected_entities(self.matrix)

        cells_json = []
        for cell in self.matrix.cells.values():
            cells_json.append({
                "publication": cell.publication,
                "entity": ENTITY_DISPLAY_NAMES.get(cell.entity, cell.entity),
                "tone_score": round(cell.coverage.tone_score, 3),
                "article_count": cell.coverage.article_count,
                "framing_device_count": cell.coverage.framing_device_count,
                "financial_tie": cell.relationship.financial_tie,
                "estimated_value": cell.relationship.estimated_value,
                "asymmetry_score": round(cell.asymmetry_score, 3),
            })

        return {
            "correlation": correlation,
            "protected_entities": protected,
            "cells": cells_json,
            "relationships": self.analyzer.get_all_relationships_summary(),
        }


def _tie_symbol(tie: str) -> str:
    """Return a short symbol for a financial tie type."""
    return {
        "licensing": "$",
        "investment": "$$",
        "advertising": "$ad",
        "distribution": "$d",
        "indirect": "~",
        "mixed": "~",
        "negotiating": "?$",
        "adversarial": "⚖",
        "litigation": "⚖",
        "none": "○",
    }.get(tie, "?")
