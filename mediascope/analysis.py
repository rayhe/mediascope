"""High-level article analysis orchestrator.

Wraps the lower-level ``analyze`` subpackage modules (entities,
sentiment, framing, sources, topics) into a single pipeline class
used by the CLI.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from mediascope.analyze.entities import detect_entities, get_primary_entity
from mediascope.analyze.sentiment import analyze_composite, count_anonymous_sources
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sources import extract_sources
from mediascope.analyze.topics import classify_topic as classify_topics


@dataclass
class AnalysisResult:
    """Container for a single article's analysis output."""

    title: str = ""
    url: str = ""
    primary_entity: str | None = None
    entities: dict[str, Any] = field(default_factory=dict)
    sentiment: Any = None
    framing_devices: list[Any] = field(default_factory=list)
    sources: list[Any] = field(default_factory=list)
    topics: list[Any] = field(default_factory=list)
    anonymous_source_count: int = 0


class ArticleAnalyzer:
    """Run the full analysis pipeline on one or more articles.

    Usage::

        analyzer = ArticleAnalyzer(target_entity="Meta")
        result = analyzer.analyze(title="...", text="...")
    """

    def __init__(self, target_entity: str = "Meta", clusters: dict | None = None):
        self.target_entity = target_entity
        self.clusters = clusters

    def analyze(self, text: str, title: str = "", url: str = "") -> AnalysisResult:
        """Analyse a single article and return an ``AnalysisResult``."""
        entities = detect_entities(text, clusters=self.clusters)
        primary = get_primary_entity(entities)
        sentiment = analyze_composite(text, title)
        devices = detect_framing_devices(text)
        sources = extract_sources(text)
        anon_count = count_anonymous_sources(text)
        topics = classify_topics(text, headline=title)

        return AnalysisResult(
            title=title,
            url=url,
            primary_entity=primary,
            entities=entities,
            sentiment=sentiment,
            framing_devices=devices,
            sources=sources,
            topics=topics,
            anonymous_source_count=anon_count,
        )

    def analyze_batch(
        self, articles: list[dict[str, str]]
    ) -> list[AnalysisResult]:
        """Analyse a list of ``{"title": ..., "text": ..., "url": ...}`` dicts."""
        return [
            self.analyze(
                text=a.get("text", ""),
                title=a.get("title", ""),
                url=a.get("url", ""),
            )
            for a in articles
        ]
