"""MediaScope Quick Start Example.

Demonstrates the minimal workflow: load a profile, analyze an article,
and generate a disclosure statement.
"""

from mediascope.config import load_profile
from mediascope.analyze.entities import detect_entities, get_primary_entity, get_entity_distribution
from mediascope.analyze.sentiment import analyze_composite, measure_outsourced_intensity
from mediascope.analyze.sources import extract_sources, analyze_source_stance
from mediascope.conflicts.disclosure import generate_disclosure


def main():
    # 1. Load a publication profile
    profile = load_profile("wired")
    print(f"Loaded profile: {profile.name} ({profile.url})")
    print(f"  Owner chain: {' → '.join(n['name'] for n in profile.ownership_chain)}")
    print(f"  Known conflicts: {len(profile.known_conflicts)}")
    print()

    # 2. Analyze a sample article
    sample_text = """
    Meta's latest AI model has drawn criticism from privacy advocates who say
    the company trained it on user data without adequate consent. According to
    sources familiar with the matter, internal documents show Meta engineers
    raised concerns about the data collection practices months before launch.
    
    The move puts Meta further behind rivals like Google and Microsoft, whose
    AI models have been praised for their responsible data practices. Apple,
    meanwhile, has positioned its AI strategy around on-device processing
    that avoids the privacy pitfalls Meta faces.
    
    "This is exactly the kind of reckless behavior we've come to expect from
    Meta," claimed one former employee who requested anonymity. Critics argue
    the company has learned nothing from its Cambridge Analytica scandal.
    """

    # Detect entities
    entities = detect_entities(sample_text)
    primary = get_primary_entity(entities)
    distribution = get_entity_distribution(entities)
    print(f"Primary entity: {primary}")
    print(f"Entity distribution: {distribution}")
    print()

    # Analyze sentiment
    sentiment = analyze_composite(sample_text, "Meta AI Model Draws Privacy Backlash")
    print(f"Sentiment Analysis (8 dimensions):")
    print(f"  Overall tone:              {sentiment.overall_tone:.3f}")
    print(f"  Emotional intensity:       {sentiment.emotional_language_intensity:.3f}")
    print(f"  Source authority framing:   {sentiment.source_authority_framing:.3f}")
    print(f"  Agency attribution:        {sentiment.agency_attribution:.3f}")
    print(f"  Headline-body alignment:   {sentiment.headline_body_alignment:.3f}")
    print(f"  Anonymous source ratio:    {sentiment.anonymous_source_ratio:.3f}")
    print(f"  Speculative language:      {sentiment.speculative_language_ratio:.3f}")
    print(f"  Comparative framing:       {sentiment.comparative_framing:.3f}")
    print()

    # Source stance analysis (who are sources deployed against?)
    sources = extract_sources(sample_text)
    stance = analyze_source_stance(sources, "Meta", full_text=sample_text)
    print(f"Source Stance Analysis:")
    print(f"  Adversarial sources: {stance['adversarial_count']}")
    print(f"  Supportive sources:  {stance['supportive_count']}")
    print(f"  Neutral sources:     {stance['neutral_count']}")
    print(f"  Stance balance:      {stance['stance_balance']:.3f} (-1=adversarial, +1=supportive)")
    print()

    # Outsourced intensity (does the journalist delegate emotional language to quotes?)
    outsourced = measure_outsourced_intensity(sample_text)
    print(f"Outsourced Intensity:")
    print(f"  Outsourced ratio:    {outsourced['outsourced_ratio']:.3f}")
    print(f"  Editorial intensity: {outsourced['editorial_intensity']:.3f}")
    print(f"  Quoted intensity:    {outsourced['quoted_intensity']:.3f}")
    print(f"  Editorial words:     {outsourced['editorial_word_count']}")
    print(f"  Quoted words:        {outsourced['quoted_word_count']}")
    print()

    # 3. Generate conflict disclosure
    disclosure = generate_disclosure(
        profile=profile.to_dict(),
        target_entity="Meta",
    )
    print("=" * 60)
    print(disclosure)


if __name__ == "__main__":
    main()
