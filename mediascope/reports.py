"""High-level report generation orchestrator.

Re-exports the report subpackage modules for CLI use.
"""

from __future__ import annotations

from mediascope.report.weekly import generate_weekly_report
from mediascope.report.dashboard import generate_dashboard


class ReportGenerator:
    """Generate formatted bias reports.

    Usage::

        gen = ReportGenerator(publication_slug="wired", target_entity="Meta")
        md = gen.generate(format="md")
    """

    def __init__(self, publication_slug: str = "", target_entity: str = "Meta"):
        self.publication_slug = publication_slug
        self.target_entity = target_entity

    def generate(self, fmt: str = "md", **kwargs) -> str:
        """Generate a report in the given format ('md' or 'html')."""
        if fmt == "html":
            return generate_dashboard(
                publication_slug=self.publication_slug,
                target_entity=self.target_entity,
                **kwargs,
            )
        return generate_weekly_report(
            publication_slug=self.publication_slug,
            target_entity=self.target_entity,
            **kwargs,
        )
