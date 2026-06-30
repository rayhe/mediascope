"""Topic classification for media coverage analysis.

Classifies articles into standardized topic buckets using keyword-based
matching with confidence scoring.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)


@dataclass
class TopicScore:
    """A topic classification result with confidence score."""

    topic: str
    confidence: float  # 0.0 to 1.0
    matched_keywords: list[str] = field(default_factory=list)


# Standardized topic buckets with associated keyword sets
# Each keyword set is designed to detect the topic reliably via
# word-boundary matching. Phrases are matched as-is; single words
# use word boundaries.
TOPIC_KEYWORDS: dict[str, list[str]] = {
    "layoffs": [
        "layoff", "layoffs", "laid off", "fired", "firing", "firings",
        "cut jobs", "cutting jobs", "job cuts", "job losses",
        "reduction in force", "restructuring", "workforce reduction",
        "headcount reduction", "headcount cut", "downsizing",
        "eliminated positions", "eliminating roles", "severance",
        "mass layoff", "let go", "pink slip",
    ],
    "ai_development": [
        "artificial intelligence", "machine learning", "deep learning",
        "large language model", "LLM", "generative AI", "gen AI",
        "neural network", "AI model", "AI models", "AI system", "AI systems",
        "AI safety", "AI regulation", "AI ethics", "foundation model",
        "foundation models", "training data", "AI assistant", "chatbot",
        "AI agent", "AI agents", "AI research", "transformer model",
        "diffusion model", "reinforcement learning",
        "natural language processing", "NLP",
        "computer vision", "AGI", "artificial general intelligence",
        "AI infrastructure", "AI services", "AI projects",
        "AI tokens", "AI usage", "AI capacity", "computing capacity",
        "computing power", "AI training", "inference",
        "AI hackathon", "AI Innovation", "AI-focused",
    ],
    "privacy_data": [
        "privacy", "data breach", "data leak", "personal data",
        "user data", "data collection", "surveillance", "tracking",
        "GDPR", "data protection", "consent", "data sharing",
        "data harvesting", "end-to-end encryption", "E2EE",
        "biometric data", "facial recognition", "location tracking",
        "cookies", "third-party tracking", "data privacy",
        "privacy policy", "data retention", "right to be forgotten",
    ],
    "antitrust_regulation": [
        "antitrust", "anti-trust", "monopoly", "monopolistic",
        "anti-competitive", "anticompetitive", "market dominance",
        "FTC", "Federal Trade Commission", "DOJ", "Department of Justice",
        "European Commission", "DMA", "Digital Markets Act",
        "DSA", "Digital Services Act", "competition law",
        "consent decree", "regulatory scrutiny", "breakup",
        "market concentration", "merger review", "remedies",
    ],
    "child_safety": [
        "child safety", "children's safety", "child exploitation",
        "CSAM", "child abuse material", "COPPA", "underage",
        "minor", "minors", "teen", "teens", "teenager",
        "youth safety", "parental controls", "age verification",
        "online predator", "grooming", "sextortion",
        "kids online", "children online", "youth mental health",
        "social media and kids", "social media and children",
    ],
    "content_moderation": [
        "content moderation", "misinformation", "disinformation",
        "hate speech", "harmful content", "content policy",
        "takedown", "fact-check", "fact check", "censorship",
        "free speech", "deplatform", "deplatformed", "banned",
        "suspended account", "community standards", "content removal",
        "trust and safety", "trust & safety", "deepfake", "deepfakes",
        "election interference", "election integrity", "propaganda",
    ],
    "ai_generated_content": [
        "slop", "AI slop", "synthetic content", "AI-generated",
        "AI generated", "generative AI content", "generated content",
        "generated video", "generated image", "generated text",
        "generated article", "AI art", "AI video", "AI image",
        "model collapse", "training data", "feedback loop",
        "ultra-processed", "frictionless", "dopamine",
        "engagement bait", "engagement", "viral",
        "spam", "spammy", "junk", "meaninglessness",
        "hallucination", "hallucinations",
        "watermark", "deepfake",
    ],
    "financial_results": [
        "earnings", "quarterly results", "revenue", "profit",
        "net income", "operating income", "earnings per share", "EPS",
        "quarterly earnings", "annual report", "fiscal year",
        "beat expectations", "missed expectations", "guidance",
        "forecast", "stock price", "share price", "market cap",
        "investor", "shareholders", "dividend", "buyback",
        "stock buyback", "Wall Street", "analyst expectations",
    ],
    "product_launch": [
        "launch", "launched", "launching", "release", "released",
        "releasing", "unveil", "unveiled", "unveiling", "announce",
        "announced", "announcement", "introduce", "introduced",
        "introducing", "rollout", "rolling out", "new feature",
        "new product", "beta", "early access", "general availability",
        "coming soon", "now available", "ships", "shipping",
    ],
    "executive_behavior": [
        "CEO", "chief executive", "executive", "founder",
        "board of directors", "boardroom", "leadership",
        "resignation", "stepped down", "fired CEO", "ousted",
        "executive compensation", "golden parachute", "stock options",
        "executive misconduct", "scandal", "controversy",
        "leadership change", "succession", "interim CEO",
        "corporate governance", "fiduciary duty",
    ],
    "litigation": [
        "lawsuit", "sued", "suing", "litigation", "legal action",
        "court", "judge", "ruling", "verdict", "settlement",
        "class action", "injunction", "subpoena", "deposition",
        "plaintiff", "defendant", "complaint", "filed suit",
        "damages", "penalty", "fined", "consent order",
        "appeals court", "Supreme Court", "district court",
    ],
    "government_oversight": [
        "national security", "export control", "export controls",
        "government intervention", "federal regulation", "federal regulations",
        "executive order", "executive orders", "government ban",
        "government oversight", "regulatory action", "regulatory crackdown",
        "nonproliferation", "non-proliferation", "arms control",
        "sanctions", "sanctioned", "embargo", "embargoed",
        "classified", "declassified", "security clearance",
        "defense department", "pentagon", "state department",
        "intelligence community", "national intelligence",
        "homeland security", "CFIUS", "ITAR",
        "congressional hearing", "congressional review",
        "bipartisan bill", "federal bill", "federal legislation",
        "government officials", "lawmakers", "policymakers",
        "military AI", "defense AI", "AI regulation",
        "AI governance", "AI safety regulation",
        "government crackdown", "government scrutiny",
        "threat to national security", "risk to national security",
    ],
    "prediction_markets": [
        "prediction market", "prediction markets", "event contract",
        "event contracts", "betting market", "betting markets",
        "Polymarket", "Kalshi", "PredictIt", "Metaculus",
        "election betting", "event betting", "wagering",
        "wager", "wagered", "gamble", "gambling",
        "odds market", "futures market", "binary option",
        "binary options", "sports betting", "real-money gaming",
        "prediction platform", "betting platform",
        "CFTC", "Commodity Futures Trading Commission",
        "regulated exchange", "event exchange",
    ],
    "corporate_strategy": [
        "acquisition", "acquisitions", "acquired", "acquiring",
        "merger", "mergers", "M&A", "joint venture",
        "partnership", "strategic partnership", "investment",
        "diversification", "diversifying", "pivot", "pivoting",
        "expansion", "expanding into", "entering the market",
        "rival", "competitor", "competitive", "market entry",
        "strategic move", "strategic shift", "business model",
        "vertical integration", "horizontal expansion",
        "spin-off", "spinoff", "subsidiary",
        "supply chain", "supplier", "vendor",
        "computing capacity", "capacity constraints",
        "infrastructure spending", "capex", "capital expenditure",
        "data centre", "data center", "data centres", "data centers",
    ],
    "defense_military": [
        "military", "defense contractor", "defense contract",
        "warfare", "warfighter", "battlefield", "combat",
        "Army", "Navy", "Air Force", "Marines", "Marine Corps",
        "Pentagon", "Department of Defense", "DoD",
        "soldier", "soldiers", "troops", "infantry",
        "Special Operations", "special forces", "SOCOM",
        "drone", "drones", "drone strike", "drone strikes",
        "weapons system", "weapons systems", "weapon system",
        "munitions", "ordnance", "armament", "armaments",
        "tactical", "tactical AI", "defense technology",
        "prototyping contract", "defense budget",
        "IVAS", "Integrated Visual Augmentation System",
        "Anduril", "Palantir", "Northrop Grumman", "Raytheon",
        "Lockheed Martin", "General Dynamics", "L3Harris",
        "BAE Systems", "defense industry", "military AI",
        "counter-drone", "autonomous weapons", "lethal autonomous",
        "military application", "military applications",
        "defense spending", "arms deal", "arms deals",
    ],
    "labor_market": [
        "labor market", "employment growth", "unemployment",
        "unemployment rate", "job market", "workforce",
        "hiring rate", "hiring rates", "job growth", "job loss",
        "job losses", "entry-level jobs", "occupations",
        "labor statistics", "BLS", "Bureau of Labor Statistics",
        "payroll", "reskill", "reskilling", "retrain",
        "labor economist", "labor economists", "macroeconomic",
        "wage growth", "wages", "labor transition",
        "job displacement", "jobs apocalypse", "job woes",
        "head count", "head counts", "employment effects",
        "labor market conditions", "working fates",
        "career model", "career ladder", "entry-level work",
        "job upheaval", "labor market statistics",
    ],
    "workplace_culture": [
        "morale", "employee morale", "employees", "workers",
        "dissatisfaction", "frustration", "burnout", "turnover",
        "soul-crushing", "soul crushing", "draftees", "drudge",
        "drudgery", "menial", "attrition", "retention",
        "workplace", "culture", "toxic culture", "work environment",
        "internal revolt", "petition", "union", "union drive",
        "reassignment", "reassigned", "laid off", "layoffs",
        "internal memo", "all-hands", "livestream",
        "remote work", "return to office", "RTO",
        "team morale", "job satisfaction", "disgruntled",
        "demoralizing", "demoralized", "onboarding",
        "manager ratio", "direct reports",
    ],
    "infrastructure_impact": [
        "data center", "data centers", "data centre", "data centres",
        "hyperscale", "hyperscaler", "hyperscalers",
        "power grid", "power grids", "electricity demand",
        "power bills", "power bill", "electricity bills",
        "rate hike", "rate hikes", "rate increase",
        "water usage", "water consumption", "cooling water",
        "NIMBY", "rezoning", "rezone", "rezoned",
        "environmental impact", "environmental concerns",
        "community opposition", "community impact",
        "local consumers", "local residents",
        "tax breaks", "tax incentives", "tax abatement",
        "construction boom", "building boom",
        "noise pollution", "constant hum",
        "power-hungry", "energy-hungry",
        "megawatt", "megawatts", "gigawatt", "gigawatts",
        "nuclear energy", "nuclear power", "nuclear plant",
        "grid capacity", "grid strain", "grid infrastructure",
        "cooling system", "cooling infrastructure",
        "public opposition", "organized opposition",
        "resource-intensive", "land use",
    ],
    "worker_ai_displacement": [
        "automate themselves", "train their replacement",
        "training their replacement", "train their replacements",
        "training their own replacement", "replace them",
        "replacing workers", "replacing coworkers", "replace workers",
        "worker dignity", "workers dignity",
        "alienation", "disempowerment", "alienating",
        "dehumanizing", "reduce to modules",
        "distill colleagues", "distill their colleagues",
        "anti-distillation", "human replacement",
        "AI double", "AI doubles", "AI clone", "AI clones",
        "sabotage", "countermeasure", "countermeasures",
        "worker resistance", "pushing back",
        "self-automation", "automate myself",
        "value is being cheapened", "easier to replace",
        "flattened into modules", "digital labor",
        "AI replacement", "replaced by AI",
    ],
}


def _compile_keyword_patterns(
    keywords: list[str],
) -> list[tuple[re.Pattern, str]]:
    """Compile keywords into regex patterns with word boundaries.

    Returns list of (compiled_pattern, original_keyword) tuples.
    """
    patterns: list[tuple[re.Pattern, str]] = []
    for kw in keywords:
        escaped = re.escape(kw)
        pattern = re.compile(rf"\b{escaped}\b", re.IGNORECASE)
        patterns.append((pattern, kw))
    return patterns


# Pre-compile all topic patterns at module load time
_COMPILED_TOPICS: dict[str, list[tuple[re.Pattern, str]]] = {
    topic: _compile_keyword_patterns(keywords)
    for topic, keywords in TOPIC_KEYWORDS.items()
}


def classify_topic(
    text: str,
    top_n: int = 3,
    custom_topics: dict[str, list[str]] | None = None,
) -> list[TopicScore]:
    """Classify text into topic buckets using keyword matching.

    Confidence is calculated as a normalized score based on the number
    of unique keyword matches and total match count, relative to the
    keyword set size.

    Args:
        text: The article text to classify.
        top_n: Number of top topics to return.
        custom_topics: Optional additional topic keyword sets to include.

    Returns:
        Top N TopicScore objects sorted by confidence (descending).
    """
    if not text:
        return []

    # Use pre-compiled patterns plus any custom topics
    topic_patterns = dict(_COMPILED_TOPICS)
    if custom_topics:
        for topic, keywords in custom_topics.items():
            topic_patterns[topic] = _compile_keyword_patterns(keywords)

    scores: list[TopicScore] = []

    for topic, patterns in topic_patterns.items():
        matched_keywords: list[str] = []
        total_matches = 0

        for pattern, keyword in patterns:
            matches = pattern.findall(text)
            if matches:
                matched_keywords.append(keyword)
                total_matches += len(matches)

        if not matched_keywords:
            continue

        # Confidence formula:
        # - keyword_coverage: fraction of the keyword set that matched (0-1)
        # - density: total matches normalized by text length (capped at 1)
        # - Combined with weighted average favoring coverage
        keyword_coverage = len(matched_keywords) / len(patterns)
        word_count = max(len(text.split()), 1)
        density = min(total_matches / (word_count / 100), 1.0)  # matches per 100 words, capped

        confidence = 0.6 * keyword_coverage + 0.4 * density
        confidence = min(confidence, 1.0)

        scores.append(
            TopicScore(
                topic=topic,
                confidence=round(confidence, 4),
                matched_keywords=sorted(set(matched_keywords)),
            )
        )

    # Sort by confidence descending, return top N
    scores.sort(key=lambda s: s.confidence, reverse=True)
    return scores[:top_n]
