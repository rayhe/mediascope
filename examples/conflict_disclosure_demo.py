"""MediaScope Conflict Disclosure Demo.

Demonstrates the conflict disclosure pipeline: how MediaScope maps
ownership chains, revenue relationships, and litigation funding to
generate ready-to-use disclosure statements for any publication.

This is one of MediaScope's core differentiators — turning opaque
ownership structures into transparent, verifiable conflict disclosures
that readers and researchers can reference.

Usage:
    python examples/conflict_disclosure_demo.py
"""

from mediascope.conflicts.ownership import OwnershipMapper
from mediascope.conflicts.revenue import RevenueMapper
from mediascope.conflicts.litigation import LitigationMapper
from mediascope.disclosure import generate_disclosure


def demo_wired_meta_disclosure():
    """Generate a full conflict disclosure for Wired covering Meta.

    This is the canonical example: Wired (Condé Nast → Advance Publications)
    has multiple undisclosed financial conflicts when covering Meta:
    1. Advance holds 65.2% voting power in Reddit (a Meta competitor)
    2. Condé Nast has AI licensing deals with OpenAI, Amazon, Apple (Meta competitors)
    3. Meta has NO revenue relationship with Condé Nast
    """
    print("=" * 70)
    print("CONFLICT DISCLOSURE: Wired → Meta Coverage")
    print("=" * 70)
    print()

    # Step 1: Map the ownership chain
    ownership = OwnershipMapper("profiles/wired.yaml")
    chain = ownership.get_chain()

    print("1. OWNERSHIP CHAIN")
    print("-" * 40)
    for level, entity in enumerate(chain):
        indent = "  " * level
        print(f"{indent}{'└─ ' if level > 0 else ''}{entity['name']} ({entity['entity_type']})")
        if 'description' in entity:
            # Show first sentence of description
            desc = entity['description'].split('.')[0] + '.'
            print(f"{indent}   {desc}")
    print()

    # Step 2: Map revenue relationships
    revenue = RevenueMapper("profiles/wired.yaml")
    relationships = revenue.get_relationships()

    print("2. REVENUE RELATIONSHIPS")
    print("-" * 40)
    meta_relationship = None
    for rel in relationships:
        status = "✅" if rel.get('active', True) else "❌"
        print(f"  {status} {rel['entity']} — {rel['type']}: {rel.get('description', 'N/A')}")
        if rel['entity'].lower() in ('meta', 'facebook'):
            meta_relationship = rel

    if meta_relationship is None:
        print()
        print("  ⚠️  NO revenue relationship with Meta found.")
        print("     This asymmetry is itself a conflict signal: the publication")
        print("     has financial ties to Meta's competitors but not to Meta.")
    print()

    # Step 3: Map litigation connections
    litigation = LitigationMapper("profiles/wired.yaml")
    connections = litigation.get_connections()

    print("3. LITIGATION CONNECTIONS")
    print("-" * 40)
    if connections:
        for conn in connections:
            print(f"  • {conn.get('funder', 'Unknown')} → {conn.get('case', 'Unknown')}")
            if 'amount' in conn:
                print(f"    Funding: {conn['amount']}")
            if 'connection_to_coverage' in conn:
                print(f"    Coverage link: {conn['connection_to_coverage']}")
    else:
        print("  No direct litigation connections found in profile.")
    print()

    # Step 4: Generate disclosure statement
    print("4. GENERATED DISCLOSURE STATEMENTS")
    print("-" * 40)
    print()

    # Full disclosure
    full = generate_disclosure(
        publication="wired",
        target_entity="Meta",
        format="full",
        profiles_dir="profiles",
    )
    print("--- Full Disclosure ---")
    print(full)
    print()

    # Social media format (compact)
    social = generate_disclosure(
        publication="wired",
        target_entity="Meta",
        format="social",
        profiles_dir="profiles",
    )
    print("--- Social Media Format ---")
    print(social)
    print()


def demo_nyt_meta_disclosure():
    """Generate a conflict disclosure for NYT covering Meta.

    Different conflict profile: NYT (New York Times Company, publicly traded)
    has AI licensing deals and litigation connections but a different
    ownership structure than Wired.
    """
    print("=" * 70)
    print("CONFLICT DISCLOSURE: New York Times → Meta Coverage")
    print("=" * 70)
    print()

    full = generate_disclosure(
        publication="nytimes",
        target_entity="Meta",
        format="full",
        profiles_dir="profiles",
    )
    print(full)
    print()


def demo_cross_publication_comparison():
    """Compare conflict profiles across multiple publications.

    Shows how the same event covered by different publications will have
    different conflict disclosures — a key input for interpreting coverage
    asymmetry results.
    """
    print("=" * 70)
    print("CROSS-PUBLICATION CONFLICT COMPARISON")
    print("=" * 70)
    print()

    publications = ["wired", "nytimes", "guardian", "atlantic", "mit-tech-review"]

    for pub in publications:
        try:
            disclosure = generate_disclosure(
                publication=pub,
                target_entity="Meta",
                format="social",
                profiles_dir="profiles",
            )
            print(f"📰 {pub.upper()}")
            print(f"   {disclosure}")
            print()
        except Exception as e:
            print(f"📰 {pub.upper()}")
            print(f"   ⚠️  Could not generate: {e}")
            print()


def demo_disclosure_for_custom_entity():
    """Generate disclosures for a non-Meta entity.

    MediaScope is publication-agnostic. This example shows how to check
    for conflicts when Wired covers OpenAI (a company Condé Nast has
    licensing deals WITH, creating a positive-coverage conflict).
    """
    print("=" * 70)
    print("CONFLICT DISCLOSURE: Wired → OpenAI Coverage")
    print("(Positive-conflict example: publication has revenue tie TO entity)")
    print("=" * 70)
    print()

    full = generate_disclosure(
        publication="wired",
        target_entity="OpenAI",
        format="full",
        profiles_dir="profiles",
    )
    print(full)
    print()
    print("NOTE: When a publication has a revenue relationship WITH the")
    print("covered entity (rather than with its competitors), the conflict")
    print("creates incentive for *positive* coverage bias, not negative.")
    print("This is the mirror image of the Wired/Meta case.")
    print()


if __name__ == "__main__":
    print()
    print("MediaScope Conflict Disclosure Demo")
    print("====================================")
    print()
    print("This demo generates conflict of interest disclosures for")
    print("publications covering specific entities. These disclosures are")
    print("the transparency infrastructure that readers deserve but rarely")
    print("receive from the publications themselves.")
    print()
    print("Profiles directory: profiles/")
    print()

    demo_wired_meta_disclosure()
    demo_nyt_meta_disclosure()
    demo_cross_publication_comparison()
    demo_disclosure_for_custom_entity()

    print("=" * 70)
    print("DEMO COMPLETE")
    print("=" * 70)
    print()
    print("Key takeaways:")
    print("  1. Every publication has a unique conflict fingerprint")
    print("  2. Absence of a revenue relationship IS a signal")
    print("  3. Ownership chains reveal hidden competitive tensions")
    print("  4. The same entity can be a positive or negative conflict")
    print("     depending on the publication's financial ties")
    print("  5. Disclosure statements are machine-generated and verifiable")
    print()
