"""High-level disclosure statement orchestrator.

Re-exports the conflicts.disclosure module for CLI use.
"""

from __future__ import annotations

from mediascope.conflicts.disclosure import generate_disclosure


class DisclosureGenerator:
    """Generate conflict-of-interest disclosure statements.

    Usage::

        gen = DisclosureGenerator(publication_slug="wired", target_entity="Meta")
        text = gen.generate(format="full")
    """

    def __init__(self, publication_slug: str = "", target_entity: str = "Meta"):
        self.publication_slug = publication_slug
        self.target_entity = target_entity

    def generate(self, fmt: str = "full", **kwargs) -> str:
        """Generate a disclosure in the given format ('full', 'social', 'json')."""
        return generate_disclosure(
            publication_slug=self.publication_slug,
            target_entity=self.target_entity,
            fmt=fmt,
            **kwargs,
        )
