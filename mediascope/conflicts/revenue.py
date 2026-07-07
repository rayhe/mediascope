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


def load_revenue_data(profile) -> list[RevenueRelationship]:
    """Load revenue relationships from a publication's YAML profile.

    Accepts both raw YAML dicts and PublicationProfile objects.  The
    YAML key is ``revenue_relationships`` (a flat list at the top
    level).  For backward compatibility the function also checks the
    legacy nested ``revenue.relationships`` path.

    Args:
        profile: Parsed YAML dict **or** PublicationProfile.

    Returns:
        List of RevenueRelationship objects.
    """
    # Support flat YAML key and legacy nested path
    relationships_data = profile.get("revenue_relationships", None)
    if relationships_data is None:
        revenue_section = profile.get("revenue", {})
        if isinstance(revenue_section, dict):
            relationships_data = revenue_section.get("relationships", [])
        else:
            relationships_data = []

    # Derive parent name
    ownership_section = profile.get("ownership", {})
    if isinstance(ownership_section, dict):
        parent = ownership_section.get("ultimate_parent", "Unknown")
    else:
        # Fall back to last ownership_chain node
        chain = profile.get("ownership_chain", [])
        parent = chain[-1].get("name", "Unknown") if chain else "Unknown"

    relationships: list[RevenueRelationship] = []
    for rel in relationships_data:
        # Coerce estimated_value to float; strings like "undisclosed"
        # become None so arithmetic in calculate_financial_exposure
        # stays safe.
        raw_value = rel.get("estimated_value")
        if isinstance(raw_value, (int, float)):
            est_value: float | None = float(raw_value)
        elif isinstance(raw_value, str):
            # Try to extract a number (e.g. "~$50M+")
            import re
            m = re.search(r"[\d,.]+", raw_value.replace(",", ""))
            if m:
                try:
                    num = float(m.group())
                    # Heuristic: if "M" or "million" in string, multiply
                    if "m" in raw_value.lower() or "million" in raw_value.lower():
                        num *= 1_000_000
                    elif "b" in raw_value.lower() or "billion" in raw_value.lower():
                        num *= 1_000_000_000
                    est_value = num
                except ValueError:
                    est_value = None
            else:
                est_value = None
        else:
            est_value = None

        relationships.append(RevenueRelationship(
            publication_parent=parent,
            partner=rel.get("partner", "Unknown"),
            relationship_type=rel.get("type", "unknown"),
            estimated_value=est_value,
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
