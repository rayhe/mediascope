"""MediaScope Topic Classification Demo.

Demonstrates the 27-bucket topic classification system with real-world
article snippets. Topic classification is used for:

1. Apples-to-apples asymmetry comparison within topic (§3 methodology)
2. Genre detection pipeline (financial_results → VADER inflation warning)
3. Topic-controlled DiD analysis (journalist coverage shift within a topic)

Each bucket is designed for cross-entity comparison: does publication X
cover Company A's privacy events differently from Company B's?

See METHODOLOGY.md §3 for the full framework and AGENT_GUIDE.md for
the function calling schema.
"""

from mediascope.analyze.topics import classify_topic, TopicScore


# --------------------------------------------------------------------------- #
# Snippets drawn from real annotated articles in examples/sample_output/       #
# --------------------------------------------------------------------------- #

SAMPLE_ARTICLES: list[dict[str, str]] = [
    {
        "name": "Child safety litigation",
        "source": "Reuters Meta $1.4T penalty 2026-07-07",
        "text": (
            "Meta Platforms said in a regulatory filing on Monday that it "
            "faces up to $1.4 trillion in combined penalties from lawsuits "
            "alleging its social media platforms are addictive and harmful "
            "to children's mental health. Attorneys general from dozens of "
            "states sued Meta last year accusing the company of designing "
            "features that hook teens and adolescents."
        ),
        "expected_top_topic": "child_safety",
    },
    {
        "name": "AI development strategy",
        "source": "Reuters Zuckerberg town hall 2026-07-02",
        "text": (
            "Meta CEO Mark Zuckerberg told employees that AI agents 'hadn't "
            "progressed as quickly as he'd expected' and that some of the "
            "company's AI bets 'haven't come to fruition yet.' The company "
            "is pouring billions into large language models, inference "
            "infrastructure, and agentic AI development."
        ),
        "expected_top_topic": "ai_development",
    },
    {
        "name": "Financial results / earnings",
        "source": "Barron's BofA AI spending watermelon 2026-07-07",
        "text": (
            "Bank of America analysts estimate Meta will spend $145 billion "
            "on capital expenditures in 2026 and $185 billion in 2027, "
            "driven by its next-generation 'Watermelon' AI model. Revenue "
            "for the first quarter topped $56 billion, beating estimates. "
            "The stock fell 8% after Reality Labs posted a $4 billion loss."
        ),
        "expected_top_topic": "financial_results",
    },
    {
        "name": "Privacy / surveillance",
        "source": "Wired MCI data exposure 2026-06-22",
        "text": (
            "Meta quietly ran an internal surveillance program that tracked "
            "when and where employees swiped their badges, which buildings "
            "they entered, and how long they stayed. A configuration error "
            "exposed employee data far beyond its intended audience. The "
            "program, internally called MCI, was part of its push to enforce "
            "return-to-office mandates and involved mouse tracking and "
            "keystroke monitoring."
        ),
        "expected_top_topic": "privacy_data",
    },
    {
        "name": "Workplace culture / morale",
        "source": "Wired Applied AI soul-crushing 2026-06",
        "text": (
            "Engineers described the work environment as 'soul-crushing.' "
            "Employee morale has cratered amid mandatory return-to-office "
            "policies, performance-based firings, and what workers call "
            "a culture of fear. Internal surveys show engagement scores "
            "at historic lows. Burnout is widespread across the Applied "
            "AI division."
        ),
        "expected_top_topic": "workplace_culture",
    },
    {
        "name": "Antitrust / regulation",
        "source": "Reuters EU WhatsApp AI antitrust 2026-06-10",
        "text": (
            "The European Commission issued interim measures against Meta "
            "under the Digital Markets Act, citing abuse of dominance in "
            "messaging. The competition enforcer's Statement of Objections "
            "accused Meta of self-preferencing its AI assistant inside "
            "WhatsApp. The FTC is monitoring the case for parallels to its "
            "own antitrust proceedings."
        ),
        "expected_top_topic": "antitrust_regulation",
    },
    {
        "name": "Hardware / wearables",
        "source": "Wired Meta glasses launch 2026-06-23",
        "text": (
            "Meta launched its Ray-Ban Display smart glasses with a built-in "
            "heads-up display, bone conduction audio, and an onboard neural "
            "processing unit. The wearable device features an AR overlay "
            "and pairs with Meta's AI assistant. The company also announced "
            "a Neural Band wrist accessory using EMG input."
        ),
        "expected_top_topic": "hardware_wearables",
    },
    {
        "name": "Subscription monetization",
        "source": "Wired Meta glasses subscription era 2026-07-02",
        "text": (
            "Meta's decision to gate premium AI features behind a monthly "
            "subscription drew criticism from users who expected the hardware "
            "they already paid for to include full functionality. The $7.99 "
            "Meta AI Plus tier rate-limits free users and locks out advanced "
            "features like real-time translation. The paywall approach mirrors "
            "Apple Intelligence's pricing tiers."
        ),
        "expected_top_topic": "subscription_monetization",
    },
    {
        "name": "Cybersecurity",
        "source": "MIT TR Meta AI agent hack 2026-06-05",
        "text": (
            "Researchers demonstrated a prompt injection attack that hijacked "
            "Meta's AI agent, exfiltrating user credentials and session tokens "
            "through a crafted exploit. The vulnerability allowed account "
            "takeover with a single message. Security researchers called "
            "it 'the most serious agentic AI breach we've seen.'"
        ),
        "expected_top_topic": "cybersecurity",
    },
    {
        "name": "Infrastructure impact",
        "source": "MIT TR Meta Louisiana natural gas 2026-05",
        "text": (
            "Meta's proposed data center in Richland Parish would consume "
            "2.3 gigawatts of power, equivalent to powering 750,000 homes. "
            "The facility would burn natural gas around the clock. Community "
            "opposition has mounted over water usage, noise pollution, and "
            "the environmental footprint. NIMBY protests blocked the initial "
            "permit hearing."
        ),
        "expected_top_topic": "infrastructure_impact",
    },
    {
        "name": "Litigation (general)",
        "source": "Reuters Meta insurance defense 2026-06-23",
        "text": (
            "Meta's insurers are mounting a legal challenge to avoid covering "
            "the company's defense costs in child safety lawsuits. The "
            "dispute centers on whether Meta's policies exclude social media "
            "addiction claims. Multiple court filings from the ongoing MDL "
            "3047 proceeding show 2,527 individual claims and 42 state "
            "attorneys general."
        ),
        "expected_top_topic": "litigation",
    },
    {
        "name": "Worker AI displacement",
        "source": "WebProNews Meta Dublin contractors 2026-05-29",
        "text": (
            "Content moderators in Dublin who spent years training their "
            "replacement AI models now face self-automation. The workers "
            "trained the classifiers on millions of examples, effectively "
            "training their own replacement. The cruel irony of digital "
            "labor: replaced by AI systems they built themselves. Worker "
            "resistance is growing as contractors realize their value is "
            "being cheapened."
        ),
        "expected_top_topic": "worker_ai_displacement",
    },
    {
        "name": "Consumer protection",
        "source": "Gizmodo Meta $1.4T penalty analysis 2026-07-07",
        "text": (
            "State attorneys general are pursuing deceptive practices "
            "allegations under consumer fraud statutes, arguing Meta's dark "
            "patterns and UDAP violations deliberately misled users about "
            "data collection. The consumer protection enforcement actions "
            "are separate from the federal antitrust case."
        ),
        "expected_top_topic": "consumer_protection",
    },
]


def demo_single_classification():
    """Classify each sample article and show top-3 topic matches."""
    print("=" * 72)
    print("TOPIC CLASSIFICATION DEMO — 27-Bucket System")
    print("=" * 72)
    print()

    correct = 0
    total = len(SAMPLE_ARTICLES)

    for article in SAMPLE_ARTICLES:
        results: list[TopicScore] = classify_topic(article["text"])
        top = results[0] if results else None
        match = "✅" if top and top.topic == article["expected_top_topic"] else "❌"
        if top and top.topic == article["expected_top_topic"]:
            correct += 1

        print(f"  {match} {article['name']}")
        print(f"     Source: {article['source']}")
        print(f"     Expected: {article['expected_top_topic']}")
        if results:
            for r in results[:3]:
                marker = "→ " if r.topic == article["expected_top_topic"] else "  "
                kw_sample = ", ".join(r.matched_keywords[:4])
                print(
                    f"     {marker}{r.topic}: {r.confidence:.3f} "
                    f"(keywords: {kw_sample})"
                )
        else:
            print("     (no topic matched)")
        print()

    print("-" * 72)
    print(f"  Accuracy: {correct}/{total} ({correct / total * 100:.0f}%)")
    print()


def demo_multi_topic_article():
    """Show how articles can match multiple topics simultaneously.

    Real articles often span multiple topic buckets — a child safety
    article may also be an antitrust/regulation piece and a litigation
    piece. The top-3 retention policy captures this overlap.
    """
    multi_topic_text = (
        "The Federal Trade Commission is weighing antitrust action against "
        "Meta after new evidence emerged that the company's algorithms "
        "deliberately targeted teenagers with addictive content. The child "
        "safety concerns overlap with the agency's ongoing monopoly "
        "investigation, as Meta's market dominance in social media for "
        "minors may constitute abuse of market power under the Digital "
        "Markets Act. Attorneys general from 42 states have filed separate "
        "consumer protection lawsuits alleging deceptive practices."
    )

    print("=" * 72)
    print("MULTI-TOPIC CLASSIFICATION — Overlapping Buckets")
    print("=" * 72)
    print()
    print("  Article: FTC + child safety + antitrust + consumer protection")
    print()

    results = classify_topic(multi_topic_text)
    for r in results:
        kw_sample = ", ".join(r.matched_keywords[:5])
        print(f"  {r.topic}: {r.confidence:.3f} (keywords: {kw_sample})")
    print()

    print("  Note: This article legitimately spans 3-4 topic buckets.")
    print("  Asymmetry analysis can compare within ANY of these buckets:")
    print("  - Is Meta's child_safety coverage more negative than Google's?")
    print("  - Is Meta's antitrust coverage more negative than Apple's?")
    print("  - Each comparison is apples-to-apples within the same topic.")
    print()


def demo_genre_detection():
    """Show how topic classification feeds genre detection.

    Financial articles (financial_results confidence ≥ 0.4) trigger the
    VADER inflation warning in the sentiment pipeline. This is the
    bridge between topic classification and sentiment correction.
    """
    financial_text = (
        "Meta Platforms reported first-quarter revenue of $56.31 billion, "
        "beating analyst estimates of $55.3 billion. Earnings per share "
        "came in at $6.43 versus the $6.21 consensus. Reality Labs posted "
        "a quarterly loss of $4.03 billion. Bank of America raised its "
        "price target to $680 from $650, maintaining a Buy rating. The "
        "stock rose 3.2% in after-hours trading."
    )

    print("=" * 72)
    print("GENRE DETECTION VIA TOPIC CLASSIFICATION")
    print("=" * 72)
    print()

    results = classify_topic(financial_text)
    financial_score = next(
        (r for r in results if r.topic == "financial_results"), None
    )

    if financial_score and financial_score.confidence >= 0.4:
        print(f"  ⚠️  FINANCIAL GENRE DETECTED")
        print(f"     financial_results confidence: {financial_score.confidence:.3f}")
        print(f"     Trigger threshold: 0.4")
        print()
        print("  ACTION: Flag VADER sentiment scores as potentially inflated.")
        print("  Financial journalism uses confident, aspirational language that")
        print("  VADER scores as positive even when editorial stance is bearish.")
        print("  See METHODOLOGY.md §16 for recommended correction workflow.")
    else:
        print("  Financial genre NOT detected.")
    print()


def demo_topic_bucket_reference():
    """Print the complete 27-bucket reference table.

    Useful for agents that need to look up what each bucket captures
    and which buckets are adjacent/confusable.
    """
    BUCKET_DESCRIPTIONS = {
        "layoffs": "Formal workforce actions: layoffs, firings, headcount cuts, severance",
        "ai_development": "AI technology creation: LLMs, training, inference, AI strategy",
        "privacy_data": "Data collection, surveillance, tracking, GDPR, encryption",
        "antitrust_regulation": "Competition law, monopoly, FTC/EC enforcement, DMA/DSA",
        "child_safety": "Youth protection: CSAM, addiction, parental controls, teen mental health",
        "content_moderation": "Platform governance: content removal, misinformation, policy enforcement",
        "ai_generated_content": "AI output quality: deepfakes, generative artifacts, AI slop",
        "financial_results": "Earnings, revenue, stock performance, analyst ratings, market cap",
        "product_launch": "Specific product releases, announcements, launch events",
        "executive_behavior": "Leadership decisions, CEO statements, executive departures",
        "litigation": "Lawsuits, court filings, legal proceedings, settlements",
        "prediction_markets": "Betting platforms, event contracts, wagering",
        "corporate_strategy": "M&A, partnerships, pivots, market entry decisions",
        "defense_military": "Military applications, defense contracts, dual-use technology",
        "labor_market": "Macroeconomic employment, wage dynamics, BLS data, job displacement",
        "workplace_culture": "Internal morale, burnout, culture, return-to-office policies",
        "government_oversight": "Regulatory hearings, government audits, policy reviews",
        "infrastructure_impact": "Data centers, energy/water usage, NIMBY, environmental footprint",
        "worker_ai_displacement": "Workers training AI that replaces them — recursive self-automation",
        "health_tech": "Medical devices, brain-computer interfaces, clinical AI, health apps",
        "cybersecurity": "Hacking, security breaches, exploits, vulnerability disclosure",
        "ai_ethics_safety": "AI alignment, existential risk, algorithmic bias, responsible AI",
        "education": "Technology impact on schools, classrooms, academic performance",
        "subscription_monetization": "Paywalls, subscription pricing, rate-limiting, monetization",
        "energy_climate": "Fossil fuel dependency, carbon emissions, renewable energy, climate policy",
        "hardware_wearables": "Smart glasses, VR/AR headsets, fitness trackers, wearable computing",
        "consumer_protection": "AG enforcement, deceptive practices, UDAP, dark patterns, consumer fraud",
    }

    # Adjacency warnings: commonly confused bucket pairs
    ADJACENCY = [
        ("layoffs", "workplace_culture", "Layoffs = formal workforce actions; workplace_culture = internal morale"),
        ("layoffs", "labor_market", "Layoffs = specific actions; labor_market = macro employment trends"),
        ("ai_development", "ai_ethics_safety", "ai_development = technology; ai_ethics_safety = moral dimensions"),
        ("ai_development", "ai_generated_content", "ai_development = creation; ai_generated_content = output quality"),
        ("privacy_data", "cybersecurity", "privacy_data = collection/surveillance; cybersecurity = hacking/exploits"),
        ("child_safety", "consumer_protection", "child_safety = youth-specific; consumer_protection = general AG enforcement"),
        ("litigation", "consumer_protection", "litigation = general legal; consumer_protection = deceptive practices/UDAP"),
        ("antitrust_regulation", "government_oversight", "antitrust = competition law; government_oversight = regulatory hearings"),
        ("financial_results", "subscription_monetization", "financial_results = earnings/stock; subscription = pricing/paywall"),
        ("corporate_strategy", "product_launch", "corporate_strategy = M&A/partnerships; product_launch = specific releases"),
        ("infrastructure_impact", "energy_climate", "infrastructure = data center construction/NIMBY; energy_climate = emissions/renewables"),
        ("worker_ai_displacement", "labor_market", "worker_ai_displacement = recursive self-automation; labor_market = macro trends"),
    ]

    print("=" * 72)
    print("TOPIC BUCKET REFERENCE — 27 Standardized Buckets")
    print("=" * 72)
    print()

    for i, (bucket, desc) in enumerate(BUCKET_DESCRIPTIONS.items(), 1):
        print(f"  {i:2d}. {bucket}")
        print(f"      {desc}")

    print()
    print("-" * 72)
    print("ADJACENCY WARNINGS — Commonly Confused Pairs")
    print("-" * 72)
    print()
    for a, b, explanation in ADJACENCY:
        print(f"  {a} ↔ {b}")
        print(f"    {explanation}")
    print()


if __name__ == "__main__":
    demo_single_classification()
    demo_multi_topic_article()
    demo_genre_detection()
    demo_topic_bucket_reference()
