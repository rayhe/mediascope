"""Ownership chain mapping for conflict-of-interest detection.

Maps corporate ownership hierarchies from publication profiles and
identifies potential conflicts of interest with coverage targets.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class OwnershipNode:
    """A node in an ownership hierarchy."""

    name: str
    entity_type: str  # "publisher", "parent_company", "holding_company", "family_office", "individual"
    subsidiaries: list[str] = field(default_factory=list)
    investments: list[str] = field(default_factory=list)
    board_seats: list[str] = field(default_factory=list)
    financial_interests: list[str] = field(default_factory=list)


@dataclass
class OwnershipChain:
    """Complete ownership chain from publication to ultimate parent."""

    nodes: list[OwnershipNode]
    ultimate_parent: Optional[str] = None
    total_levels: int = 0


@dataclass
class Conflict:
    """A detected conflict of interest."""

    conflict_type: str  # "revenue", "investment", "board_seat", "competitive", "litigation"
    source_entity: str
    target_entity: str
    description: str
    severity: int  # 1 (minor) to 5 (critical)
    evidence: str = ""
    source_url: str = ""


def parse_ownership_chain(profile) -> OwnershipChain:
    """Parse an ownership chain from a publication's YAML profile data.

    Accepts both raw YAML dicts and PublicationProfile objects.  The YAML
    key is ``ownership_chain`` (a flat list of node dicts at the top
    level).  For backward compatibility with code that passed a nested
    ``ownership.chain`` structure, the function also checks that path.

    Args:
        profile: Parsed YAML dict **or** PublicationProfile.

    Returns:
        OwnershipChain with all nodes and metadata.
    """
    # Support both flat YAML key and legacy nested path
    chain_data = profile.get("ownership_chain", None)
    if chain_data is None:
        ownership = profile.get("ownership", {})
        if isinstance(ownership, dict):
            chain_data = ownership.get("chain", [])
        else:
            chain_data = []

    nodes: list[OwnershipNode] = []
    for node_data in chain_data:
        node = OwnershipNode(
            name=node_data.get("name", "Unknown"),
            entity_type=node_data.get("entity_type", "unknown"),
            subsidiaries=node_data.get("subsidiaries", []),
            investments=[
                (i.get("entity", str(i)) if isinstance(i, dict) else str(i))
                for i in node_data.get("investments", [])
            ],
            board_seats=node_data.get("board_seats", []),
            financial_interests=node_data.get("financial_interests", []),
        )
        nodes.append(node)

    # Derive ultimate_parent: check legacy nested path first, then last node
    ownership_section = profile.get("ownership", {})
    ultimate_parent = (
        ownership_section.get("ultimate_parent")
        if isinstance(ownership_section, dict)
        else None
    )
    if not ultimate_parent and nodes:
        ultimate_parent = nodes[-1].name

    return OwnershipChain(
        nodes=nodes,
        ultimate_parent=ultimate_parent,
        total_levels=len(nodes),
    )


def find_conflicts(
    chain: OwnershipChain,
    target_entity: str,
    entity_data: dict,
) -> list[Conflict]:
    """Find conflicts of interest between an ownership chain and a target entity.

    Checks for:
        - Investment overlaps (owner invests in target's competitor)
        - Board seat conflicts (owner has board seats at related companies)
        - Competitive relationships (owner subsidiaries compete with target)
        - Revenue dependencies (financial interests tied to target)
        - Litigation connections (owner involved in legal action against target)

    Args:
        chain: Parsed ownership chain.
        target_entity: Entity to check conflicts against.
        entity_data: Additional data about the target entity, expected keys:
            - "competitors" (list[str])
            - "partners" (list[str])
            - "litigation_targets" (list[str])
            - "industry" (str)

    Returns:
        List of detected Conflict objects.
    """
    conflicts: list[Conflict] = []
    target_lower = target_entity.lower()
    competitors = [c.lower() for c in entity_data.get("competitors", [])]
    partners = [p.lower() for p in entity_data.get("partners", [])]
    litigation_targets = [lt.lower() for lt in entity_data.get("litigation_targets", [])]

    for node in chain.nodes:
        # Check investments for conflicts
        for investment in node.investments:
            inv_lower = investment.lower()
            if inv_lower in competitors:
                conflicts.append(Conflict(
                    conflict_type="investment",
                    source_entity=node.name,
                    target_entity=target_entity,
                    description=(
                        f"{node.name} has investments in {investment}, "
                        f"which is a competitor of {target_entity}."
                    ),
                    severity=4,
                    evidence=f"Investment by {node.name} in {investment}",
                ))
            if inv_lower == target_lower:
                conflicts.append(Conflict(
                    conflict_type="investment",
                    source_entity=node.name,
                    target_entity=target_entity,
                    description=(
                        f"{node.name} has a direct investment in {target_entity}."
                    ),
                    severity=5,
                    evidence=f"Direct investment by {node.name}",
                ))

        # Check board seats
        for seat in node.board_seats:
            seat_lower = seat.lower()
            if seat_lower == target_lower or seat_lower in competitors:
                conflicts.append(Conflict(
                    conflict_type="board_seat",
                    source_entity=node.name,
                    target_entity=target_entity,
                    description=(
                        f"{node.name} holds a board seat at {seat}, "
                        f"which is {'the target entity' if seat_lower == target_lower else 'a competitor of ' + target_entity}."
                    ),
                    severity=4 if seat_lower == target_lower else 3,
                    evidence=f"Board seat at {seat}",
                ))

        # Check subsidiaries for competitive conflicts
        for sub in node.subsidiaries:
            sub_lower = sub.lower()
            if sub_lower in competitors:
                conflicts.append(Conflict(
                    conflict_type="competitive",
                    source_entity=node.name,
                    target_entity=target_entity,
                    description=(
                        f"{node.name} owns {sub}, which competes with {target_entity}."
                    ),
                    severity=4,
                    evidence=f"Subsidiary {sub} competes with {target_entity}",
                ))

        # Check financial interests
        for interest in node.financial_interests:
            int_lower = interest.lower()
            if target_lower in int_lower or any(c in int_lower for c in competitors):
                conflicts.append(Conflict(
                    conflict_type="revenue",
                    source_entity=node.name,
                    target_entity=target_entity,
                    description=(
                        f"{node.name} has financial interest: {interest}, "
                        f"which may conflict with coverage of {target_entity}."
                    ),
                    severity=3,
                    evidence=f"Financial interest: {interest}",
                ))

        # Check litigation connections
        if target_lower in [lt.lower() for lt in node.financial_interests + node.investments]:
            if target_lower in litigation_targets:
                conflicts.append(Conflict(
                    conflict_type="litigation",
                    source_entity=node.name,
                    target_entity=target_entity,
                    description=(
                        f"{node.name} has financial ties to entities involved in "
                        f"litigation against {target_entity}."
                    ),
                    severity=5,
                    evidence="Litigation funding connection",
                ))

    return conflicts


def format_ownership_text(chain: OwnershipChain) -> str:
    """Format an ownership chain as human-readable text.

    Args:
        chain: Parsed ownership chain.

    Returns:
        Multi-line string describing the chain.
    """
    if not chain.nodes:
        return "No ownership information available."

    lines: list[str] = []
    for i, node in enumerate(chain.nodes):
        indent = "  " * i
        arrow = "→ " if i > 0 else ""
        lines.append(f"{indent}{arrow}{node.name} ({node.entity_type})")

        detail_indent = "  " * (i + 1)
        if node.subsidiaries:
            lines.append(f"{detail_indent}Subsidiaries: {', '.join(node.subsidiaries)}")
        if node.investments:
            lines.append(f"{detail_indent}Investments: {', '.join(node.investments)}")
        if node.board_seats:
            lines.append(f"{detail_indent}Board seats: {', '.join(node.board_seats)}")
        if node.financial_interests:
            lines.append(f"{detail_indent}Financial interests: {', '.join(node.financial_interests)}")

    if chain.ultimate_parent:
        lines.append(f"\nUltimate parent: {chain.ultimate_parent}")
        lines.append(f"Total ownership levels: {chain.total_levels}")

    return "\n".join(lines)
