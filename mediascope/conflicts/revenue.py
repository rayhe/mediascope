"""Revenue relationship tracking for conflict-of-interest analysis.

Maps financial relationships between publication parent companies and
entities that may create coverage conflicts.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class RevenueRelationship:
    """A financial relationship between a publication's parent and another entity."""

    publication_parent: str
    partner: str
    relationship_type: str  # "licensing", "advertising", "partnership", "investment"
    estimated_value: Optional[float] = None  # USD
    description: str = ""
    date_established: Optional[str] = None  # ISO date string
    source_url: str = ""
    is_competitor_of_target: bool = False


def load_revenue_data(profile: dict) -> list[RevenueRelationship]:
    """Load revenue relationships from a publication's YAML profile.

    Expected profile structure:
        revenue:
          relationships:
            - partner: "Company X"
              type: "licensing"
              estimated_value: 50000000
              description: "Content licensing deal"
              date_established: "2023-01-15"
              source_url: "https://..."
            - partner: "Company Y"
              type: "advertising"
              ...
        ownership:
          ultimate_parent: "Parent Corp"

    Args:
        profile: Parsed YAML profile dictionary.

    Returns:
        List of RevenueRelationship objects.
    """
    revenue_section = profile.get("revenue", {})
    relationships_data = revenue_section.get("relationships", [])
    parent = profile.get("ownership", {}).get("ultimate_parent", "Unknown")

    relationships: list[RevenueRelationship] = []
    for rel in relationships_data:
        relationships.append(RevenueRelationship(
            publication_parent=parent,
            partner=rel.get("partner", "Unknown"),
            relationship_type=rel.get("type", "unknown"),
            estimated_value=rel.get("estimated_value"),
            description=rel.get("description", ""),
            date_established=rel.get("date_established"),
            source_url=rel.get("source_url", ""),
            is_competitor_of_target=rel.get("is_competitor_of_target", False),
        ))

    return relationships


def find_revenue_conflicts(
    relationships: list[RevenueRelationship],
    target_entity: str,
) -> list[RevenueRelationship]:
    """Filter revenue relationships to those involving the target entity's competitors.

    A relationship is a conflict if:
        - The partner IS the target entity (direct financial dependency)
        - The partner is a competitor of the target (is_competitor_of_target=True)
        - The partner name partially matches the target entity name

    Args:
        relationships: All revenue relationships for the publication.
        target_entity: Entity to check conflicts against.

    Returns:
        List of conflicting RevenueRelationship objects.
    """
    target_lower = target_entity.lower()
    conflicts: list[RevenueRelationship] = []

    for rel in relationships:
        partner_lower = rel.partner.lower()

        is_conflict = (
            rel.is_competitor_of_target
            or partner_lower == target_lower
            or target_lower in partner_lower
            or partner_lower in target_lower
        )

        if is_conflict:
            conflicts.append(rel)

    return conflicts


def calculate_financial_exposure(
    relationships: list[RevenueRelationship],
) -> dict:
    """Calculate total financial exposure by relationship type.

    Args:
        relationships: Revenue relationships to aggregate.

    Returns:
        Dictionary with:
            - "by_type": {type: total_value}
            - "total": sum of all estimated values
            - "count_by_type": {type: count}
            - "unknown_value_count": relationships with no estimated value
    """
    by_type: dict[str, float] = defaultdict(float)
    count_by_type: dict[str, int] = defaultdict(int)
    unknown_value_count = 0
    total = 0.0

    for rel in relationships:
        count_by_type[rel.relationship_type] += 1

        if rel.estimated_value is not None:
            by_type[rel.relationship_type] += rel.estimated_value
            total += rel.estimated_value
        else:
            unknown_value_count += 1

    return {
        "by_type": dict(by_type),
        "total": total,
        "count_by_type": dict(count_by_type),
        "unknown_value_count": unknown_value_count,
    }
