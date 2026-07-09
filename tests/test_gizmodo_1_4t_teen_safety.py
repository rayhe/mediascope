"""Tests for Gizmodo $1.4T Meta teen safety article analysis.

Type A deep dive — Jul 9, 2026.
Article: "Meta's Teen Safety Case Just Became a $1.4 Trillion Existential Threat"
Source: Gizmodo, Jul 8, 2026
URL: https://gizmodo.com/metas-teen-safety-case-just-became-a-1-4-trillion-existential-threat-2000782306

Tests new framing devices (litigation_cascade, defensive_verb_framing)
and validates existing pipeline accuracy against manual annotation.
"""

import sys
sys.path.insert(0, '.')

from mediascope.analysis import (
    detect_entities,
    detect_framing_devices,
    extract_sources,
    classify_topics,
    analyze_composite,
    count_anonymous_sources,
)
from mediascope.quality.standards import check_quality


HEADLINE = (
    "Meta's Teen Safety Case Just Became a $1.4 Trillion "
    "Existential Threat"
)

ARTICLE = """Meta's Teen Safety Case Just Became a $1.4 Trillion Existential Threat

Meta is facing $1.4 trillion in damages in a social media addiction case brought by four states.

Thirty-three states have banded together to sue Meta, alleging that the company was exploiting its young users on Instagram and Facebook for profit, including by collecting data from children without parental consent. Four of those states\u2014California, New Jersey, Colorado and Kentucky\u2014also claim that the company misled consumers about the addictive design features on the platforms, thereby causing mental health problems in children who got hooked from an early age.

The damages requested by those four states add up to a whopping $1.4 trillion, Meta said in a recent court filing, a figure that would allegedly go even higher with the other penalties the attorneys general seek to add. The number is high by many standards but especially when compared to the company's market capitalization, which is just above $1.5 trillion.

Meta has denied the allegations, and recently attempted yet failed to get the addiction claims dismissed. In the latest court submission, the attorneys for Meta argued that the $1.4 trillion in damages was unsubstantiated and disproportionate.

"Meta has not found any case, under any cause of action, where one defendant was ordered to pay over one trillion dollars\u2014or any number remotely close to that staggering figure," the attorneys claim.

The states' filings are sealed, but per Reuters, the penalties were calculated by multiplying the number of violations, aka the rough amount of young users impacted by the addictive design choices, by the fine amounts designated by state law.

Meta argues that the number is so high that it has no parallel "in the history of consumer protection enforcement."

"Indeed, the Federal Trade Commission recently described a '$1 billion penalty' as the 'largest ever in a case involving an FTC rule violation,'" the filing states. "The AGs' demand exceeds even those record figures by several orders of magnitude, and is in gross disproportion to the specified violations alleged here."

The case is now going to court in August, and if the judge rules against Meta, it could prove to be a substantial financial problem for the company. For months now, Meta executives have admitted to investors that they were anticipating some material loss this year due to "scrutiny on youth-related issues." But the $1.4 trillion number was previously unknown, and it is far from the only youth-related headache the tech giant is bracing for.

Meta has been plagued with mounting litigation over alleged deceptive social media practices targeting young users. In a watershed verdict delivered earlier this year, a judge found Meta and Google liable and ordered them to pay $6 million in damages to a now 20-year-old who said that deliberate addictive design features on social media platforms like Instagram got her hooked from a young age and exacerbated mental health problems like depression and anxiety. Prior to that verdict, platform operators were protected from liability for third-party content under Section 230 of the Communications Decency Act.

The March verdict marked just the beginning of Meta's legal troubles. The company still has more than 3,000 similar cases pending in California state court. Another 14 states have also brought claims similar to the one led by the four states, with the case set to go to trial early next year."""


# ---------------------------------------------------------------------------
# Entity detection
# ---------------------------------------------------------------------------

def test_meta_entity_detected():
    """Meta should be detected as the primary entity."""
    entities = detect_entities(ARTICLE)
    meta_mentions = [e for e in entities if e.canonical_name == "Meta"]
    assert len(meta_mentions) >= 8, (
        f"Expected >=8 Meta mentions, got {len(meta_mentions)}"
    )


def test_instagram_facebook_clustered_under_meta():
    """Instagram and Facebook should be clustered under Meta."""
    entities = detect_entities(ARTICLE)
    ig = [e for e in entities if e.entity == "Instagram"]
    fb = [e for e in entities if e.entity == "Facebook"]
    assert len(ig) >= 1
    assert len(fb) >= 1
    assert ig[0].cluster == "Meta"
    assert fb[0].cluster == "Meta"


def test_google_entity_detected():
    """Google should be detected as a separate entity (co-defendant)."""
    entities = detect_entities(ARTICLE)
    google = [e for e in entities if e.canonical_name == "Google"]
    assert len(google) >= 1


def test_ftc_entity_detected():
    """FTC should be detected."""
    entities = detect_entities(ARTICLE)
    ftc = [e for e in entities if e.entity == "FTC"]
    assert len(ftc) >= 1


def test_section_230_detected():
    """Section 230 should be detected as a legal entity."""
    entities = detect_entities(ARTICLE)
    s230 = [e for e in entities if "Section 230" in e.entity]
    assert len(s230) >= 1


# ---------------------------------------------------------------------------
# Topic classification
# ---------------------------------------------------------------------------

def test_primary_topic_litigation():
    """Primary topic should be litigation."""
    topics = classify_topics(ARTICLE)
    assert topics[0].topic == "litigation"
    assert topics[0].confidence >= 0.4


def test_child_safety_in_top_3():
    """child_safety should be in the top 3 topics."""
    topics = classify_topics(ARTICLE)
    topic_names = [t.topic for t in topics[:3]]
    assert "child_safety" in topic_names


def test_consumer_protection_in_top_3():
    """consumer_protection should be in the top 3 topics."""
    topics = classify_topics(ARTICLE)
    topic_names = [t.topic for t in topics[:3]]
    assert "consumer_protection" in topic_names


# ---------------------------------------------------------------------------
# Sentiment
# ---------------------------------------------------------------------------

def test_overall_tone_negative():
    """Article tone toward Meta should be negative."""
    result = analyze_composite(ARTICLE, headline=HEADLINE)
    assert result.overall_tone < -0.3, (
        f"Expected negative tone, got {result.overall_tone}"
    )


def test_emotional_intensity_high():
    """Emotional language intensity should be high."""
    result = analyze_composite(ARTICLE, headline=HEADLINE)
    assert result.emotional_language_intensity >= 0.7


# ---------------------------------------------------------------------------
# Framing device detection — existing types
# ---------------------------------------------------------------------------

def test_catastrophizing_existential_threat():
    """'Existential Threat' in headline should trigger catastrophizing."""
    devices = detect_framing_devices(ARTICLE)
    cat = [d for d in devices if d.device_type == "catastrophizing"]
    assert len(cat) >= 1
    assert any("Existential Threat" in d.evidence_text for d in cat)


def test_scale_magnitude_detected():
    """Multiple dollar figures should trigger scale_magnitude."""
    devices = detect_framing_devices(ARTICLE)
    sm = [d for d in devices if d.device_type == "scale_magnitude"]
    assert len(sm) >= 4, f"Expected >=4 scale_magnitude, got {len(sm)}"


def test_loaded_language_detected():
    """'exploiting', 'hooked', 'plagued', 'whopping' should trigger loaded_language."""
    devices = detect_framing_devices(ARTICLE)
    ll = [d for d in devices if d.device_type == "loaded_language"]
    evidence_texts = [d.evidence_text.lower() for d in ll]
    # At least some of these high-intensity words should be caught
    expected_words = {"exploiting", "hooked", "plagued", "whopping", "staggering"}
    found = {w for w in expected_words if any(w in e for e in evidence_texts)}
    assert len(found) >= 3, (
        f"Expected >=3 of {expected_words} as loaded_language, found {found}"
    )


def test_confession_framing_admitted():
    """'Meta executives have admitted to' should trigger confession_framing."""
    devices = detect_framing_devices(ARTICLE)
    cf = [d for d in devices if d.device_type == "confession_framing"]
    assert len(cf) >= 1
    assert any("admitted" in d.evidence_text.lower() for d in cf)


def test_escalation_amplification_mounting():
    """'mounting litigation' should trigger escalation_amplification."""
    devices = detect_framing_devices(ARTICLE)
    ea = [d for d in devices if d.device_type == "escalation_amplification"]
    assert len(ea) >= 1
    assert any("mounting" in d.evidence_text.lower() for d in ea)


def test_valuation_comparison():
    """Comparison to market capitalization should trigger valuation_comparison."""
    devices = detect_framing_devices(ARTICLE)
    vc = [d for d in devices if d.device_type == "valuation_comparison"]
    assert len(vc) >= 1


# ---------------------------------------------------------------------------
# Framing device detection — NEW types (#84, #85)
# ---------------------------------------------------------------------------

def test_litigation_cascade_thirty_three_states():
    """'Thirty-three states have banded together' should trigger litigation_cascade."""
    devices = detect_framing_devices(ARTICLE)
    lc = [d for d in devices if d.device_type == "litigation_cascade"]
    assert len(lc) >= 1, (
        "Expected litigation_cascade for '33 states banded together'"
    )


def test_litigation_cascade_3000_cases():
    """'more than 3,000 similar cases pending' should trigger litigation_cascade."""
    devices = detect_framing_devices(ARTICLE)
    lc = [d for d in devices if d.device_type == "litigation_cascade"]
    found_3000 = any("3,000" in d.evidence_text for d in lc)
    assert found_3000, (
        "Expected litigation_cascade matching '3,000 similar cases pending'"
    )


def test_litigation_cascade_another_14_states():
    """'Another 14 states have also brought claims' should trigger litigation_cascade."""
    devices = detect_framing_devices(ARTICLE)
    lc = [d for d in devices if d.device_type == "litigation_cascade"]
    found_14 = any("14 states" in d.evidence_text for d in lc)
    assert found_14, (
        "Expected litigation_cascade matching 'Another 14 states'"
    )


def test_defensive_verb_attempted_yet_failed():
    """'attempted yet failed to' should trigger defensive_verb_framing."""
    devices = detect_framing_devices(ARTICLE)
    dvf = [d for d in devices if d.device_type == "defensive_verb_framing"]
    assert len(dvf) >= 1, (
        "Expected defensive_verb_framing for 'attempted yet failed'"
    )
    assert any("attempted yet failed" in d.evidence_text.lower() for d in dvf)


def test_defensive_verb_standalone_example():
    """Standalone 'struggled to' should trigger defensive_verb_framing."""
    text = "The company struggled to regain consumer trust after the breach."
    devices = detect_framing_devices(text)
    dvf = [d for d in devices if d.device_type == "defensive_verb_framing"]
    assert len(dvf) >= 1


def test_defensive_verb_forced_to():
    """'was forced to' should trigger defensive_verb_framing."""
    text = "Meta was forced to pay $375 million in damages."
    devices = detect_framing_devices(text)
    dvf = [d for d in devices if d.device_type == "defensive_verb_framing"]
    assert len(dvf) >= 1


def test_litigation_cascade_standalone():
    """Standalone cascade example should fire."""
    text = (
        "More than 2,500 similar lawsuits pending in federal court. "
        "Another 40 states have also filed enforcement actions."
    )
    devices = detect_framing_devices(text)
    lc = [d for d in devices if d.device_type == "litigation_cascade"]
    assert len(lc) >= 2, f"Expected >=2 cascade hits, got {len(lc)}"


# ---------------------------------------------------------------------------
# Source extraction
# ---------------------------------------------------------------------------

def test_reuters_source_detected():
    """Reuters should be detected as a news_outlet source."""
    sources = extract_sources(ARTICLE)
    reuters = [s for s in sources if s.name == "Reuters"]
    assert len(reuters) >= 1
    assert reuters[0].source_type == "news_outlet"


def test_meta_organizational_source():
    """Meta should be detected as an organizational source."""
    sources = extract_sources(ARTICLE)
    meta_src = [s for s in sources if s.name == "Meta"]
    assert len(meta_src) >= 1
    assert meta_src[0].source_type == "organizational"


def test_legal_party_source_detected():
    """Attorneys for Meta should be detected as a legal_party source."""
    sources = extract_sources(ARTICLE)
    legal = [s for s in sources if s.source_type == "legal_party"]
    assert len(legal) >= 1


def test_no_named_human_sources():
    """Article has zero named human individual sources."""
    anon, total = count_anonymous_sources(ARTICLE)
    # All sources are organizational or documentary, not named individuals
    assert anon == 0  # no anonymous, but also no named humans


# ---------------------------------------------------------------------------
# Quality check
# ---------------------------------------------------------------------------

def test_quality_zero_named_sources_warning():
    """Quality check should flag zero named human sources."""
    quality = check_quality(ARTICLE)
    issues_text = " ".join(str(i) for i in quality.issues)
    assert "zero_named_sources" in issues_text, (
        f"Expected zero_named_sources warning, got issues: {quality.issues}"
    )


def test_quality_score_below_75():
    """Quality score should reflect the zero-named-sources penalty."""
    quality = check_quality(ARTICLE)
    assert quality.score < 75, (
        f"Expected quality score < 75 due to sourcing, got {quality.score}"
    )
