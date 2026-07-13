"""MediaScope Sarcastic Editorial Detection Demo (Path H).

Demonstrates the newest correction path in MediaScope's sentiment
pipeline: detecting when VADER/TextBlob misscores short sarcastic
editorial opinion pieces as positive.

The Problem:
    Short opinion pieces (typically <500 words) use a sarcastic
    editorial register — direct reader address, assumed consensus,
    sardonic asides — that is invisible to lexical sentiment models.
    An article stating "People hate Meta's smart glasses for quite
    a few reasons" and "brace yourself" scores POSITIVE on VADER
    because the vocabulary is active and declarative, and the
    sentence structure is confident.

    Unlike Path D (sardonic contempt, which requires ≥7 loaded
    language devices and strongly positive agency ≥0.3), Path H
    fires on shorter articles with concentrated sarcastic
    indicators and neutral agency (the company IS doing things,
    they're just doing them badly).

The Fix:
    Path H detects the sarcastic editorial register through
    editorial_aside and assumed_consensus devices, then overrides
    the VADER score with a tone derived from sarcasm density and
    emotional intensity.

Trigger conditions (all must be met):
    - Raw tone ≥ 0.3 (VADER inflated positive)
    - ≥2 editorial_aside devices ("brace yourself", "let's be honest")
    - ≥4 total adversarial devices
    - Emotional intensity ≥ 0.5
    - Agency ≥ -0.1 (neutral to slightly positive)

Blend: 15% raw + 85% target, where:
    target = -(0.30 + 0.20 × sarcasm_density + 0.10 × EI)
    sarcasm_density = min((editorial_aside + assumed_consensus) / 5, 1.0)
    Clamped to [-0.7, 0.0]

Discovery article: Gizmodo "Meta Is Slapping Subscriptions on Its Smart
Glasses" (Jul 1, 2026). VADER scored +0.65 on a clearly negative
article with "People hate", "brace yourself", "let's be honest",
"something tells me", and consumer-frustration vocabulary.

See METHODOLOGY.md §9.2 (Path H) for the full theoretical framework.
"""

from mediascope.analyze.sentiment import analyze_composite
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sources import extract_sources, analyze_source_stance


# -------------------------------------------------------------------
# Article 1: Gizmodo "Meta Is Slapping Subscriptions on Its Smart Glasses"
# (Jul 1, 2026) — the discovery article for Path H
# -------------------------------------------------------------------
# A short, sarcastic editorial opinion piece. The author:
# - Uses "People hate" (assumed consensus — no evidence offered)
# - Uses "brace yourself" (editorial aside — breaking journalistic register)
# - Uses "let's be honest" (editorial aside — solidarity-building)
# - Uses "something tells me" (editorial aside — reader-address sarcasm)
# - Deploys consumer-frustration vocabulary ("slapping", "paywall", "hate")
#
# VADER reads the active vocabulary as positive. Path H catches the
# sarcastic register and corrects.

GIZMODO_SUBS_HEADLINE = "Meta Is Slapping Subscriptions on Its Smart Glasses"

GIZMODO_SUBS_TEXT = """
People hate Meta's smart glasses for quite a few reasons, but brace
yourself: the company is now slapping a subscription paywall on some
of the features that made them worth considering in the first place.

Starting next month, AI-powered features like live translation and
real-time object identification will require a Meta One Premium
subscription — $19.99 per month. That's on top of the $299 you
already paid for the glasses.

Let's be honest here: this was always the plan. Meta didn't build
a consumer hardware division to sell you one pair of glasses. They
built it to sell you a recurring revenue stream attached to your
face.

The company says the subscription "unlocks the full potential" of
the glasses. Something tells me that potential was already there —
it was just held hostage behind a paywall.

For what it's worth, the free tier still includes basic photo and
video capture, voice commands for music, and phone calls. So your
$299 glasses will still function as a slightly overpriced Bluetooth
headset with a camera. Congrats.
"""


# -------------------------------------------------------------------
# Article 2: Sarcastic editorial about AI product limitations
# -------------------------------------------------------------------
# Another short editorial demonstrating the sarcastic register.
# Uses editorial asides, assumed consensus, and emotional language
# while maintaining neutral agency (the company is described as
# actively doing things, just doing them poorly).

EDITORIAL_AI_HEADLINE = "Another AI Feature Nobody Asked For Is Here"

EDITORIAL_AI_TEXT = """
Brace yourself for yet another AI feature that solves a problem nobody
had. The latest update to your favorite social media app now uses AI
to auto-generate captions for your stories. Because apparently typing
three words was just too much work.

Let's be honest: these AI features exist not because users want them,
but because companies need to justify their billions in AI spending to
shareholders. People are tired of being guinea pigs for half-baked
AI experiments.

Something tells me the engineers who built this know it's unnecessary.
But hey, at least the quarterly earnings deck will have a nice slide
about "AI-powered experiences."

The feature is opt-out, naturally. Because when has Big Tech ever
defaulted to asking permission? If you want to go back to writing
your own captions like some kind of digital Luddite, you'll need
to navigate three menus deep into settings. Good luck finding it.
"""


# -------------------------------------------------------------------
# Contrast: A genuinely positive product announcement (NOT sarcastic)
# -------------------------------------------------------------------
# This article uses similar active language but without the sarcastic
# register. VADER's positive score should be correct here — no
# correction should fire.

POSITIVE_HEADLINE = "New Smart Glasses Get Major AI Upgrade"

POSITIVE_TEXT = """
Smart glasses users are getting a significant upgrade this month.
The latest software update brings real-time translation in 12
languages, object identification for accessibility, and improved
battery optimization that extends usage to 6 hours.

The company has been investing heavily in on-device AI processing,
which means these features work without a constant internet
connection. Early reviews from beta testers have been overwhelmingly
positive, with many praising the translation accuracy.

The update rolls out automatically to all existing devices over the
next two weeks. No additional subscription is required — all features
are included with the hardware purchase.
"""


def analyze_with_path_h_details(
    text: str,
    headline: str,
    label: str,
) -> None:
    """Run analysis with detailed Path H diagnostic output."""

    sentiment = analyze_composite(text, headline)
    framing_devices = detect_framing_devices(text)

    # Canonical adversarial device types (must match sentiment.py exactly)
    adversarial_types = {
        "loaded_language", "emotional_appeal", "guilt_by_association",
        "catastrophizing", "power_asymmetry", "isolation_framing",
        "pressure_language", "hypocrisy_frame", "timeline_implication",
        "juxtaposition", "refusal_amplification",
        "self_referential_investigation", "kicker_framing",
        "military_techno_optimism", "assumed_consensus", "editorial_aside",
        "failure_precedent", "editorial_deflation",
        "competitive_positioning", "consumer_ownership", "slippery_slope",
        "competitive_deficit", "competitive_displacement",
        "absence_as_evidence", "silence_as_guilt",
        "expert_contradiction", "loss_leader_framing",
        "recidivism_framing", "sarcastic_correction",
        "consent_alarm", "precedent_analogy",
    }

    print(f"\n{'=' * 70}")
    print(f"  {label}")
    print(f"  Headline: {headline}")
    print(f"{'=' * 70}")

    # Raw vs corrected
    raw = sentiment.raw_tone
    corrected = sentiment.overall_tone
    correction_fired = sentiment.framing_corrected

    print(f"\n  VADER raw tone:       {raw:+.3f}")
    print(f"  Corrected tone:       {corrected:+.3f}")
    if correction_fired:
        gap = abs(raw - corrected)
        print(f"  *** CORRECTION FIRED (gap = {gap:.3f}) ***")
    else:
        print(f"  (no correction needed — VADER score preserved)")

    # Word count
    word_count = len(text.split())
    print(f"\n  Word count:           {word_count}")

    # Framing devices — full breakdown
    device_types = {}
    for d in framing_devices:
        device_types[d.device_type] = device_types.get(d.device_type, 0) + 1

    print(f"\n  Framing devices:      {len(framing_devices)} total")
    for dtype, count in sorted(device_types.items(), key=lambda x: -x[1]):
        marker = " ← adversarial" if dtype in adversarial_types else ""
        sarcasm_marker = " ← PATH H SIGNAL" if dtype in ("editorial_aside", "assumed_consensus") else ""
        print(f"    • {dtype}: {count}{marker}{sarcasm_marker}")

    # Path H diagnostic: the specific signals
    adversarial_count = sum(
        1 for d in framing_devices if d.device_type in adversarial_types
    )
    aside_count = device_types.get("editorial_aside", 0)
    consensus_count = device_types.get("assumed_consensus", 0)

    print(f"\n  PATH H TRIGGER DIAGNOSTIC:")
    print(f"    Raw tone ≥ 0.3?              {raw:+.3f} → {'YES' if raw >= 0.3 else 'NO'}")
    print(f"    Editorial asides ≥ 2?        {aside_count} → {'YES' if aside_count >= 2 else 'NO'}")
    print(f"    Adversarial devices ≥ 4?     {adversarial_count} → {'YES' if adversarial_count >= 4 else 'NO'}")

    ei = sentiment.emotional_language_intensity
    agency = sentiment.agency_attribution
    print(f"    Emotional intensity ≥ 0.5?   {ei:.3f} → {'YES' if ei >= 0.5 else 'NO'}")
    print(f"    Agency ≥ -0.1?               {agency:+.3f} → {'YES' if agency >= -0.1 else 'NO'}")

    all_met = (
        raw >= 0.3
        and aside_count >= 2
        and adversarial_count >= 4
        and ei >= 0.5
        and agency >= -0.1
    )
    print(f"    ALL CONDITIONS MET?          {'YES → Path H fires' if all_met else 'NO → Path H does not fire'}")

    if all_met:
        sarcasm_density = min((aside_count + consensus_count) / 5.0, 1.0)
        target_tone = -(0.30 + 0.20 * sarcasm_density + 0.10 * ei)
        expected = 0.15 * raw + 0.85 * target_tone
        expected = max(-0.7, min(0.0, round(expected, 4)))
        print(f"\n    Sarcasm density:             {sarcasm_density:.3f}")
        print(f"      (editorial_aside + assumed_consensus) / 5.0")
        print(f"    Target tone:                 {target_tone:+.3f}")
        print(f"      = -(0.30 + 0.20×{sarcasm_density:.2f} + 0.10×{ei:.2f})")
        print(f"    Expected corrected:          {expected:+.3f}")
        print(f"      = 15% × {raw:.2f} + 85% × {target_tone:.2f}, clamped to [-0.7, 0.0]")


def main():
    """Run the sarcastic editorial detection demo."""

    print("MediaScope Sarcastic Editorial Detection Demo (Path H)")
    print("=" * 70)
    print()
    print("VADER misscores short sarcastic opinion pieces as positive because")
    print("the sarcastic register — editorial asides, assumed consensus, direct")
    print("reader address — is invisible to lexical sentiment models.")
    print()
    print("Path H detects this register and corrects the score.")
    print()
    print("Three articles demonstrate the detection:")
    print("  1. Gizmodo subscription paywall editorial (sarcastic → correction)")
    print("  2. AI feature nobody asked for (sarcastic → correction)")
    print("  3. Genuine positive announcement (no sarcasm → no correction)")

    # Sarcastic article 1: Gizmodo subscriptions
    analyze_with_path_h_details(
        GIZMODO_SUBS_TEXT,
        GIZMODO_SUBS_HEADLINE,
        "Article 1: Gizmodo — Meta Subscription Paywall (SARCASTIC)",
    )

    # Sarcastic article 2: AI feature nobody asked for
    analyze_with_path_h_details(
        EDITORIAL_AI_TEXT,
        EDITORIAL_AI_HEADLINE,
        "Article 2: Sarcastic Editorial — AI Feature Nobody Asked For (SARCASTIC)",
    )

    # Genuine positive: no sarcasm, VADER should be correct
    analyze_with_path_h_details(
        POSITIVE_TEXT,
        POSITIVE_HEADLINE,
        "Article 3: Genuine Positive Announcement (NOT SARCASTIC)",
    )

    # Summary
    print(f"\n{'=' * 70}")
    print("  SUMMARY: WHY PATH H MATTERS")
    print(f"{'=' * 70}")
    print()
    print("  Short sarcastic editorials are a growing genre in tech journalism.")
    print("  Sites like Gizmodo, The Verge, and Ars Technica frequently publish")
    print("  <500-word opinion pieces where the editorial stance is conveyed")
    print("  entirely through register — breaking the journalistic fourth wall")
    print("  with 'brace yourself', 'let's be honest', and 'something tells me'.")
    print()
    print("  VADER reads this as confident, active prose and scores it positive.")
    print("  Path H catches the sarcastic register by detecting concentrated")
    print("  editorial_aside and assumed_consensus devices alongside high")
    print("  emotional intensity, then corrects toward the actual editorial stance.")
    print()
    print("  KEY DISTINCTION FROM OTHER PATHS:")
    print("    Path A: Wrong direction, negative agency (passive/targeted)")
    print("    Path D: Sardonic contempt, high loaded_language, positive agency")
    print("    Path H: Sarcastic register, editorial asides, neutral agency")
    print()
    print("  The subject IS doing things (neutral agency), but the editorial")
    print("  voice signals disapproval through register-breaking, not through")
    print("  loaded vocabulary (Path D) or passive framing (Path A).")
    print()
    print("  See METHODOLOGY.md §9.2 (Path H) for the full framework.")
    print("  See tests/ for 1402 regression tests covering all 12 correction paths.")


if __name__ == "__main__":
    main()
