"""
Financial Journalism Analysis Demo
===================================

Demonstrates how to analyze financial/investor journalism with awareness
of the VADER positive-bias inflation problem documented in METHODOLOGY.md §16.

Financial articles (Motley Fool, Barron's, MarketWatch, Seeking Alpha, etc.)
systematically inflate VADER compound scores by 0.3-0.5 points due to:
  1. Investment recommendation boosterism ("strong buy", "cash cow", "upside")
  2. Financial reassurance language ("fears ease", "soothe concerns")
  3. Analyst-debate format neutralizing bearish signals

This demo shows how to detect, flag, and work around the inflation.

Usage:
    python examples/financial_journalism_demo.py
"""

from mediascope.analyze.entities import detect_entities, get_primary_entity
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sentiment import analyze_composite
from mediascope.analyze.topics import classify_topic
from mediascope.analyze.sources import extract_sources

# ── Example: MarketWatch analyst-debate article ──────────────────────────
# This is a condensed version of a real article (Jul 1, 2026) that the
# toolkit scores at +0.63 composite despite a manual assessment of -0.15.

ARTICLE_HEADLINE = (
    'Is Meta "giving up" on cutting-edge AI? '
    "Wall Street is divided over potential cloud pivot."
)

ARTICLE_TEXT = """
Meta Platforms may be throwing in the towel on its ambitions to build
cutting-edge AI models, some analysts believe. The company's stock has been
beaten down, falling roughly 15% from its February highs amid concerns that
its massive AI spending hasn't produced a competitive frontier model.

Bloomberg reported that Meta is exploring the launch of a cloud computing
business to sell excess AI infrastructure capacity. Dow Jones also confirmed
the discussions. The move could unlock significant revenue potential from
Meta's estimated $135 billion in AI infrastructure investments, analysts say.

"It certainly looks like they're giving up on frontier AI," said Gil Luria,
an analyst at D.A. Davidson. "If Meta's best option is to sell compute, that
means they couldn't find a way to use it productively themselves."

Not everyone agrees. Brent Thill, a Jefferies analyst, called the
overbuilding concerns "backward," arguing that demand for AI compute will
only accelerate. "Companies that underinvest now will regret it. Meta has
the scale, the infrastructure, and the talent to dominate this space," he
wrote in a recent note. "We see significant upside from current levels."

Colin Sebastian at Baird described the potential cloud pivot as "rational"
given the economics. "Meta's core advertising business remains incredibly
strong, generating over $40 billion in quarterly revenue. The company has
the financial firepower to fund AI investments while maintaining strong
free cash flow," Sebastian wrote. "This is a company with a fortress
balance sheet and a clear path to AI monetization."

Meta's AI efforts have lagged behind Anthropic and OpenAI in delivering
cutting-edge foundation models. The company's Muse Spark, which CEO Mark
Zuckerberg once described as a breakthrough, has not matched the performance
of ChatGPT or Claude in third-party benchmarks.

However, Meta's advertising business continues to show strong momentum. The
company reported revenue growth of 33% in Q1 2026, with AI-powered ad
targeting improvements driving higher engagement and advertiser returns.
Meta AI now reaches over 640 million monthly active users globally, and
the company's Reality Labs division has seen glasses shipments surge 167%
year-over-year.

Unlike peers such as Amazon and Alphabet, which have built successful cloud
businesses over the past decade, Meta has no enterprise cloud infrastructure
or customer relationships. Entering a market already dominated by AWS,
Azure, and Google Cloud could face steep headwinds. But cloud computing is
a $500 billion total addressable market growing at 20% annually, and Meta's
compute assets could generate attractive margins with minimal incremental
investment.

Meta's capital expenditure guidance of up to $145 billion has raised
concerns among investors about whether the company has overbuilt its AI
infrastructure. Andrew Graham, a portfolio manager at Jackson Square Capital,
warned that Meta may face an "overbuilt" scenario if demand doesn't
materialize. But with the stock trading at just 22 times forward earnings
— a significant discount to the broader S&P 500 — many investors see the
risk-reward as favorable.

Meta declined to comment on the report.
"""


def analyze_financial_article(headline: str, text: str) -> dict:
    """
    Analyze a financial article and flag potential VADER inflation.

    Returns a dict with standard toolkit results plus financial-specific
    diagnostic signals.
    """
    # ── Standard toolkit pipeline ────────────────────────────────────
    entities = detect_entities(text)
    primary = get_primary_entity(entities)
    sentiment = analyze_composite(text, headline)
    framing = detect_framing_devices(text)
    topics = classify_topic(text)
    sources = extract_sources(text)

    # ── Financial inflation diagnostics ──────────────────────────────
    # Check if this article is likely a financial piece
    fin_topic_score = 0.0
    for topic_result in topics:
        if topic_result.topic == "financial_results":
            fin_topic_score = topic_result.confidence
            break

    # Extract diagnostic signals from METHODOLOGY.md §16.5
    is_financial = fin_topic_score >= 0.4
    vader_compound = sentiment.raw_tone  # uncorrected VADER+TextBlob blend
    spec_ratio = sentiment.speculative_language_ratio
    hb_alignment = sentiment.headline_body_alignment
    agency = sentiment.agency_attribution

    # Count adversarial framing devices
    adversarial_types = {
        "loaded_language", "emotional_appeal", "guilt_by_association",
        "catastrophizing", "power_asymmetry", "isolation_framing",
        "pressure_language", "ironic_quotation", "competitive_deficit",
        "financial_reassurance", "editorial_deflation", "kicker_framing",
        "assumed_consensus", "refusal_amplification", "absence_as_evidence",
    }
    adversarial_count = sum(
        1 for d in framing if d.device_type in adversarial_types
    )

    # ── Financial inflation flag ─────────────────────────────────────
    # Per METHODOLOGY.md §16.5, flag when:
    #   financial topic >= 0.4 AND raw composite >= 0.5 AND spec_ratio >= 0.25
    # Note: vader_compound here is the raw composite (VADER+TextBlob blend
    # before framing correction), not the raw VADER compound score.
    # Real failure cases show raw composites of 0.57-0.65 on articles
    # manually assessed at -0.15 to -0.25.
    inflation_risk = (
        is_financial
        and vader_compound >= 0.5
        and spec_ratio >= 0.25
    )

    # Headline-body divergence diagnostic (§16.5 item 2)
    headline_body_divergent = is_financial and hb_alignment < 0.4

    # Framing-over-sentiment diagnostic (§16.5 item 3)
    framing_contradicts_sentiment = (
        adversarial_count >= 3
        and sentiment.overall_tone > 0.3
    )

    return {
        "primary_entity": primary,
        "composite_tone": sentiment.overall_tone,
        "raw_vader": vader_compound,
        "emotional_intensity": sentiment.emotional_language_intensity,
        "speculative_ratio": spec_ratio,
        "headline_body_alignment": hb_alignment,
        "agency": agency,
        "framing_correction_applied": sentiment.overall_tone != vader_compound,
        "framing_devices": [(d.device_type, d.evidence_text[:60]) for d in framing],
        "adversarial_device_count": adversarial_count,
        "topics": [(t.topic, t.confidence) for t in topics[:3]],
        "source_count": len(sources),
        "financial_topic_score": fin_topic_score,
        # ── Diagnostics ──
        "inflation_risk": inflation_risk,
        "headline_body_divergent": headline_body_divergent,
        "framing_contradicts_sentiment": framing_contradicts_sentiment,
    }


def print_report(result: dict) -> None:
    """Print a human-readable analysis report with financial diagnostics."""
    print("=" * 72)
    print("FINANCIAL JOURNALISM ANALYSIS REPORT")
    print("=" * 72)

    print(f"\nPrimary Entity: {result['primary_entity']}")
    print(f"Topics: {', '.join(f'{t[0]} ({t[1]:.2f})' for t in result['topics'])}")

    print("\n── Sentiment ──")
    print(f"  Composite tone:    {result['composite_tone']:+.3f}")
    print(f"  Raw VADER:         {result['raw_vader']:+.3f}")
    print(f"  Emotional intens.: {result['emotional_intensity']:.3f}")
    print(f"  Speculative ratio: {result['speculative_ratio']:.3f}")
    print(f"  Headline-body:     {result['headline_body_alignment']:+.3f}")
    print(f"  Agency:            {result['agency']:+.3f}")
    print(f"  Correction fired:  {result['framing_correction_applied']}")

    print(f"\n── Framing Devices ({result['adversarial_device_count']} adversarial) ──")
    for device_type, evidence in result['framing_devices']:
        marker = "⚠️" if device_type in {
            "ironic_quotation", "competitive_deficit", "financial_reassurance",
            "isolation_framing", "refusal_amplification",
        } else "  "
        print(f"  {marker} {device_type}: {evidence}...")

    print(f"\n── Sources ──")
    print(f"  Total sources: {result['source_count']}")

    # ── Financial inflation diagnostics ──
    print("\n── Financial Inflation Diagnostics (METHODOLOGY §16) ──")

    if result['inflation_risk']:
        print("  ⚠️  INFLATION RISK: Financial topic + high VADER + high")
        print("     speculative ratio. Composite score is likely 0.3-0.5")
        print("     points too positive. Trust framing devices over sentiment.")
    else:
        print("  ✅ No inflation risk detected.")

    if result['headline_body_divergent']:
        print("  ⚠️  HEADLINE-BODY DIVERGENCE: Headline is more negative than")
        print("     VADER-measured body. Strong signal of financial inflation")
        print("     (§16.5 item 2).")

    if result['framing_contradicts_sentiment']:
        print("  ⚠️  FRAMING CONTRADICTS SENTIMENT: 3+ adversarial devices with")
        print("     positive composite tone. Framing-based assessment is more")
        print("     reliable than sentiment score for this article (§16.5 item 3).")

    if not any([result['inflation_risk'], result['headline_body_divergent'],
                result['framing_contradicts_sentiment']]):
        print("  ✅ No financial-specific flags raised.")

    print()
    print("── Interpretation Guidance ──")
    if result['inflation_risk'] or result['framing_contradicts_sentiment']:
        print("  For this article, weight framing devices (especially")
        print("  financial_reassurance, competitive_deficit, ironic_quotation,")
        print("  editorial_deflation) over the composite sentiment score.")
        print("  The editorial stance is better captured by device density")
        print("  and headline-body alignment than by VADER-based scoring.")
        print()
        print("  If cross-comparing with a wire-service article on the same")
        print("  event, the wire score provides the neutral baseline. The gap")
        print("  between wire and financial article — combined with framing")
        print("  device differential — isolates editorial contribution more")
        print("  reliably than absolute sentiment scoring.")
    else:
        print("  Standard analysis applies. Composite score is a reasonable")
        print("  estimate of editorial tone.")

    print("\n" + "=" * 72)


if __name__ == "__main__":
    result = analyze_financial_article(ARTICLE_HEADLINE, ARTICLE_TEXT)
    print_report(result)
