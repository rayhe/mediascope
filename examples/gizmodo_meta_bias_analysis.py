"""
Gizmodo Meta Bias Analysis — Runs the full MediaScope pipeline on all
fetched Gizmodo articles mentioning Meta, comparing treatment of Meta
vs other tech companies (Google, Apple, Microsoft, Amazon).

Produces:
  - Per-article sentiment + framing analysis
  - Cross-article asymmetry summary
  - Gizmodo ownership/funding conflict disclosure
  - Bias pattern summary
"""

from __future__ import annotations

import os
import sys
import json
import glob
from pathlib import Path
from datetime import datetime

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from mediascope.analyze.entities import detect_entities, get_primary_entity, get_entity_distribution
from mediascope.analyze.sentiment import analyze_composite, measure_outsourced_intensity
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sources import extract_sources, analyze_source_stance
from mediascope.analyze.topics import classify_topic

SAMPLE_DIR = Path(__file__).parent / "sample_output"

# All Gizmodo articles about Meta
META_ARTICLES = [
    "gizmodo_meta_brain_decode_jun2026_article.txt",
    "gizmodo_meta_google_ai_tokens_2026_06_29_article.txt",
    "gizmodo_meta_police_surveillance_glasses_2026_06_15_article.txt",
    "gizmodo_meta_facial_recognition_worse_2026_06_05_article.txt",
    "gizmodo_meta_removes_facerec_mad_2026_06_08_article.txt",
    "gizmodo_meta_instagram_breach_ai_2026_06_08_article.txt",
    "gizmodo_meta_minor_safety_restrictions_2026_06_02_article.txt",
    "gizmodo_trump_admin_meta_ai_vet_2026_06_24_article.txt",
    "gizmodo_meta_glasses_kylie_jenner_2026_06_23_article.txt",
    "gizmodo_meta_arena_prediction_markets_2026_06_23_article.txt",
    "gizmodo_meta_arena_worst_instincts_2026_06_24_article.txt",
    "gizmodo_meta_fury_review_2026_06_29_article.txt",
    "gizmodo_meta_glasses_launch_2026_06_23_article.txt",
]

# Non-Meta articles for comparison
COMPARISON_ARTICLES = [
    "gizmodo_australia_social_ban_2026_06_29_article.txt",
    "gizmodo_uk_social_ban_2026_06_15_article.txt",
    "gizmodo_whatsapp_new_ceo_2026_06_22_article.txt",
    "gizmodo_smart_glasses_recording_law_2026_06_08_article.txt",
    "gizmodo_project2029_kids_over_clicks_2026_06_29_article.txt",
]


def load_article(filename: str) -> tuple[str, str]:
    """Load article text and extract title from first line."""
    path = SAMPLE_DIR / filename
    if not path.exists():
        print(f"  WARNING: {filename} not found, skipping")
        return "", ""
    text = path.read_text()
    # Try to extract a headline from the first meaningful line
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    headline = lines[0] if lines else ""
    # Clean up the headline
    headline = headline.replace("Security Notice:", "").strip()
    return text, headline


def analyze_article(text: str, headline: str, target: str = "Meta") -> dict:
    """Run the full MediaScope analysis pipeline on one article."""
    # Entity detection
    entities = detect_entities(text)
    entity_dist = get_entity_distribution(entities)
    primary = get_primary_entity(entities)

    # Sentiment (8-dimension composite)
    sentiment = analyze_composite(text, headline)

    # Framing devices
    framing = detect_framing_devices(text)
    device_types = {}
    for d in framing:
        device_types.setdefault(d.device_type, []).append(d.evidence_text)

    # Source analysis
    sources = extract_sources(text)
    stance = analyze_source_stance(sources, target, full_text=text)

    # Outsourced intensity
    outsourced = measure_outsourced_intensity(text)

    # Topic
    topic = classify_topic(text)

    return {
        "headline": headline[:120],
        "target_entity": target,
        "primary_entity_detected": primary,
        "entity_distribution": entity_dist,
        "sentiment": {
            "overall_tone": round(sentiment.overall_tone, 3),
            "raw_overall_tone": round(sentiment.raw_overall_tone, 3) if hasattr(sentiment, 'raw_overall_tone') else None,
            "emotional_intensity": round(sentiment.emotional_language_intensity, 3),
            "source_authority": round(sentiment.source_authority_framing, 3),
            "agency_attribution": round(sentiment.agency_attribution, 3),
            "headline_body_alignment": round(sentiment.headline_body_alignment, 3),
            "anonymous_source_ratio": round(sentiment.anonymous_source_ratio, 3),
            "speculative_language": round(sentiment.speculative_language_ratio, 3),
            "comparative_framing": round(sentiment.comparative_framing, 3),
        },
        "framing_devices": {k: len(v) for k, v in device_types.items()},
        "framing_evidence": device_types,
        "total_framing_devices": len(framing),
        "source_analysis": {
            "total_sources": len(sources),
            "adversarial": stance.get("adversarial_count", 0),
            "supportive": stance.get("supportive_count", 0),
            "neutral": stance.get("neutral_count", 0),
            "stance_balance": round(stance.get("stance_balance", 0), 3),
        },
        "outsourced_intensity": {
            "ratio": round(outsourced.get("outsourced_ratio", 0), 3),
            "editorial_intensity": round(outsourced.get("editorial_intensity", 0), 3),
            "quoted_intensity": round(outsourced.get("quoted_intensity", 0), 3),
        },
        "topic": topic,
        "word_count": len(text.split()),
    }


def run_analysis():
    """Run the full Gizmodo Meta bias analysis."""
    print("=" * 80)
    print("GIZMODO META BIAS ANALYSIS — MediaScope Toolkit")
    print(f"Run: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 80)

    meta_results = []
    comparison_results = []

    # Analyze all Meta articles
    print(f"\n📊 Analyzing {len(META_ARTICLES)} Gizmodo Meta articles...")
    for fname in META_ARTICLES:
        text, headline = load_article(fname)
        if not text:
            continue
        print(f"  • {fname[:60]}... ({len(text.split())} words)")
        result = analyze_article(text, headline, target="Meta")
        result["filename"] = fname
        meta_results.append(result)

    # Analyze comparison articles
    print(f"\n📊 Analyzing {len(COMPARISON_ARTICLES)} comparison articles...")
    for fname in COMPARISON_ARTICLES:
        text, headline = load_article(fname)
        if not text:
            continue
        print(f"  • {fname[:60]}... ({len(text.split())} words)")
        result = analyze_article(text, headline, target="Meta")
        result["filename"] = fname
        comparison_results.append(result)

    # Compute aggregate statistics
    print("\n" + "=" * 80)
    print("AGGREGATE RESULTS")
    print("=" * 80)

    def avg(items, key_path):
        """Get nested average."""
        vals = []
        for item in items:
            v = item
            for k in key_path.split("."):
                v = v.get(k, {}) if isinstance(v, dict) else None
            if isinstance(v, (int, float)):
                vals.append(v)
        return sum(vals) / len(vals) if vals else 0.0

    meta_tones = [r["sentiment"]["overall_tone"] for r in meta_results]
    meta_intensity = [r["sentiment"]["emotional_intensity"] for r in meta_results]
    meta_framing = [r["total_framing_devices"] for r in meta_results]

    print(f"\nMeta Articles ({len(meta_results)}):")
    print(f"  Avg overall tone:       {sum(meta_tones)/len(meta_tones):.3f}")
    print(f"  Avg emotional intensity: {sum(meta_intensity)/len(meta_intensity):.3f}")
    print(f"  Avg framing devices:     {sum(meta_framing)/len(meta_framing):.1f}")
    print(f"  Tone range:              [{min(meta_tones):.3f}, {max(meta_tones):.3f}]")

    # Peer entity mentions across Meta articles
    peer_mentions = {"Google": 0, "Apple": 0, "Microsoft": 0, "Amazon": 0, "OpenAI": 0}
    for r in meta_results:
        for entity, count in r["entity_distribution"].items():
            if entity in peer_mentions:
                peer_mentions[entity] += count
    print(f"\n  Peer entity mentions in Meta articles: {peer_mentions}")

    # Framing device frequency
    device_freq = {}
    for r in meta_results:
        for dtype, count in r["framing_devices"].items():
            device_freq[dtype] = device_freq.get(dtype, 0) + count
    print(f"\n  Top framing devices across Meta articles:")
    for dtype, count in sorted(device_freq.items(), key=lambda x: -x[1])[:10]:
        print(f"    {dtype}: {count}")

    # Per-article summary
    print("\n" + "=" * 80)
    print("PER-ARTICLE SUMMARY (Meta Coverage)")
    print("=" * 80)
    for r in meta_results:
        tone = r["sentiment"]["overall_tone"]
        tone_label = "🔴 negative" if tone < -0.2 else ("🟢 positive" if tone > 0.2 else "🟡 neutral")
        print(f"\n  {r['headline'][:80]}")
        print(f"    Tone: {tone:+.3f} {tone_label}  |  Intensity: {r['sentiment']['emotional_intensity']:.3f}  |  Devices: {r['total_framing_devices']}")
        print(f"    Sources: {r['source_analysis']['total_sources']} (adv: {r['source_analysis']['adversarial']}, sup: {r['source_analysis']['supportive']})  |  Outsourced: {r['outsourced_intensity']['ratio']:.3f}")
        top_devices = sorted(r["framing_devices"].items(), key=lambda x: -x[1])[:3]
        if top_devices:
            print(f"    Top devices: {', '.join(f'{k}({v})' for k, v in top_devices)}")

    # Output JSON for programmatic use
    output = {
        "analysis_date": datetime.now().isoformat(),
        "publication": "Gizmodo",
        "target_entity": "Meta",
        "meta_articles_analyzed": len(meta_results),
        "comparison_articles_analyzed": len(comparison_results),
        "aggregate": {
            "avg_tone": round(sum(meta_tones) / len(meta_tones), 3) if meta_tones else 0,
            "avg_emotional_intensity": round(sum(meta_intensity) / len(meta_intensity), 3) if meta_intensity else 0,
            "avg_framing_devices": round(sum(meta_framing) / len(meta_framing), 1) if meta_framing else 0,
            "tone_range": [round(min(meta_tones), 3), round(max(meta_tones), 3)] if meta_tones else [0, 0],
            "peer_mentions_in_meta_articles": peer_mentions,
            "framing_device_frequency": device_freq,
        },
        "articles": meta_results,
        "comparison_articles": comparison_results,
    }

    out_path = SAMPLE_DIR / "gizmodo_meta_bias_analysis.json"
    out_path.write_text(json.dumps(output, indent=2, default=str))
    print(f"\n\n📁 Full JSON results saved to {out_path}")

    return output


if __name__ == "__main__":
    run_analysis()
