"""Litigation funding network mapper.

Tracks third-party litigation funding, maps connections between funders
and media ownership chains, and identifies potential conflicts.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class LitigationFunder:
    """A third-party litigation funder entity."""

    name: str
    fund_size: Optional[float] = None  # USD
    parent_entity: str = ""
    known_cases: list[str] = field(default_factory=list)
    target_entities: list[str] = field(default_factory=list)
    connections: list[str] = field(default_factory=list)  # linked entities


@dataclass
class LitigationCase:
    """A litigation case relevant to the analysis."""

    case_name: str
    case_number: str = ""
    court: str = ""
    target_entity: str = ""
    plaintiff: str = ""
    amount: Optional[float] = None  # USD
    status: str = ""  # "active", "settled", "dismissed", "pending"
    funder: str = ""
    source_url: str = ""


def load_litigation_data(
    profile,
) -> tuple[list[LitigationFunder], list[LitigationCase]]:
    """Load litigation data from a publication's YAML profile.

    Accepts both raw YAML dicts and PublicationProfile objects.  The
    YAML key is ``litigation_connections`` (a flat list at the top
    level).  For backward compatibility the function also checks the
    legacy nested ``litigation.funders`` / ``litigation.cases`` path.

    When using the flat ``litigation_connections`` format, each entry is
    examined for either funder-style keys (``fund_size``,
    ``known_cases``) or case-style keys (``case_name``,
    ``case_number``).

    Args:
        profile: Parsed YAML dict **or** PublicationProfile.

    Returns:
        Tuple of (funders, cases).
    """
    # Try legacy nested path first
    litigation = profile.get("litigation", None)
    if isinstance(litigation, dict) and ("funders" in litigation or "cases" in litigation):
        funder_data = litigation.get("funders", [])
        case_data = litigation.get("cases", [])
    else:
        # Flat YAML key — partition entries by structure
        connections = profile.get("litigation_connections", [])
        funder_data = []
        case_data = []
        for entry in connections:
            if not isinstance(entry, dict):
                continue
            if "case_name" in entry or "case_number" in entry:
                case_data.append(entry)
            else:
                funder_data.append(entry)

    funders: list[LitigationFunder] = []
    for f in funder_data:
        funders.append(LitigationFunder(
            name=f.get("name", "Unknown"),
            fund_size=f.get("fund_size"),
            parent_entity=f.get("parent_entity", ""),
            known_cases=f.get("known_cases", []),
            target_entities=f.get("target_entities", []),
            connections=f.get("connections", []),
        ))

    cases: list[LitigationCase] = []
    for c in case_data:
        cases.append(LitigationCase(
            case_name=c.get("case_name", "Unknown"),
            case_number=c.get("case_number", ""),
            court=c.get("court", ""),
            target_entity=c.get("target_entity", ""),
            plaintiff=c.get("plaintiff", ""),
            amount=c.get("amount"),
            status=c.get("status", "unknown"),
            funder=c.get("funder", ""),
            source_url=c.get("source_url", ""),
        ))

    return funders, cases


def find_media_litigation_links(
    funders: list[LitigationFunder],
    cases: list[LitigationCase],
    ownership_chain: object,  # OwnershipChain — avoid circular import
) -> list[dict]:
    """Cross-reference litigation funders with media ownership to find links.

    Checks whether any litigation funder has connections to entities in the
    publication's ownership chain. A link exists when:
        - A funder's parent_entity matches an ownership node
        - A funder's connections list contains an ownership node
        - An ownership node's investments include a funder

    Args:
        funders: Litigation funders.
        cases: Litigation cases.
        ownership_chain: OwnershipChain object (from ownership module).

    Returns:
        List of dicts describing each discovered link:
            {"funder", "ownership_node", "link_type", "cases_affected", "description"}
    """
    # Extract ownership entity names (duck-typing to avoid circular import)
    ownership_names: set[str] = set()
    ownership_investments: set[str] = set()
    if hasattr(ownership_chain, "nodes"):
        for node in ownership_chain.nodes:
            ownership_names.add(node.name.lower())
            for inv in getattr(node, "investments", []):
                ownership_investments.add(inv.lower())

    # Build case lookup by funder
    cases_by_funder: dict[str, list[LitigationCase]] = {}
    for case in cases:
        if case.funder:
            cases_by_funder.setdefault(case.funder.lower(), []).append(case)

    links: list[dict] = []

    for funder in funders:
        funder_lower = funder.name.lower()

        # Check parent entity match
        if funder.parent_entity and funder.parent_entity.lower() in ownership_names:
            affected = cases_by_funder.get(funder_lower, [])
            links.append({
                "funder": funder.name,
                "ownership_node": funder.parent_entity,
                "link_type": "parent_entity",
                "cases_affected": [c.case_name for c in affected],
                "description": (
                    f"Litigation funder {funder.name}'s parent entity "
                    f"({funder.parent_entity}) is part of the publication's "
                    f"ownership chain."
                ),
            })

        # Check connections
        for connection in funder.connections:
            if connection.lower() in ownership_names:
                affected = cases_by_funder.get(funder_lower, [])
                links.append({
                    "funder": funder.name,
                    "ownership_node": connection,
                    "link_type": "connection",
                    "cases_affected": [c.case_name for c in affected],
                    "description": (
                        f"Litigation funder {funder.name} lists {connection} "
                        f"as a connected entity; {connection} is in the "
                        f"publication's ownership chain."
                    ),
                })

        # Check if ownership chain invests in funder
        if funder_lower in ownership_investments:
            affected = cases_by_funder.get(funder_lower, [])
            links.append({
                "funder": funder.name,
                "ownership_node": "(investor in chain)",
                "link_type": "investment",
                "cases_affected": [c.case_name for c in affected],
                "description": (
                    f"An entity in the publication's ownership chain has "
                    f"investments in litigation funder {funder.name}."
                ),
            })

    return links


def format_litigation_network(
    funders: list[LitigationFunder],
    cases: list[LitigationCase],
) -> str:
    """Format litigation network as human-readable text.

    Args:
        funders: Litigation funders.
        cases: Litigation cases.

    Returns:
        Multi-line description of the litigation network.
    """
    if not funders and not cases:
        return "No litigation data available."

    lines: list[str] = []

    if funders:
        lines.append("LITIGATION FUNDERS:")
        for funder in funders:
            size_str = f" (fund size: ${funder.fund_size:,.0f})" if funder.fund_size else ""
            lines.append(f"  • {funder.name}{size_str}")
            if funder.parent_entity:
                lines.append(f"    Parent: {funder.parent_entity}")
            if funder.target_entities:
                lines.append(f"    Targets: {', '.join(funder.target_entities)}")
            if funder.connections:
                lines.append(f"    Connected to: {', '.join(funder.connections)}")
            if funder.known_cases:
                lines.append(f"    Known cases: {', '.join(funder.known_cases)}")
        lines.append("")

    if cases:
        lines.append("ACTIVE CASES:")
        for case in cases:
            amount_str = f" (${case.amount:,.0f})" if case.amount else ""
            lines.append(f"  • {case.case_name}{amount_str}")
            if case.case_number:
                lines.append(f"    Case #: {case.case_number}")
            if case.court:
                lines.append(f"    Court: {case.court}")
            lines.append(f"    Target: {case.target_entity}")
            lines.append(f"    Status: {case.status}")
            if case.funder:
                lines.append(f"    Funder: {case.funder}")

    return "\n".join(lines)
