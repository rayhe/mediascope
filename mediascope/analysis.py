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


def analyze_text(text: str, title: str = "", target_entity: str = "Meta") -> dict:
    """Convenience function: analyse *text* and return a plain dict.

    This wraps :class:`ArticleAnalyzer` for quick one-shot analysis in tests
    and scripts that don't need the full pipeline configuration.

    Returns a dict with keys ``entities``, ``framing_devices``, ``sentiment``,
    ``topics``, ``sources``, ``primary_entity``, and ``anonymous_source_count``.
    Each value is a plain dict/list of dicts for easy ``.get()`` access.
    """
    from dataclasses import asdict, fields as dc_fields

    def _to_dict(obj):
        """Convert a dataclass instance to a dict, or return obj if already a dict."""
        if isinstance(obj, dict):
            return obj
        if hasattr(obj, "__dataclass_fields__"):
            return {f.name: getattr(obj, f.name) for f in dc_fields(obj)}
        return obj

    analyzer = ArticleAnalyzer(target_entity=target_entity)
    result = analyzer.analyze(text, title=title)

    # Entities: could be a list of EntityMention or a dict of clusters
    raw_entities = result.entities
    if isinstance(raw_entities, dict):
        entity_list = []
        for cluster_name, mentions in raw_entities.items():
            if isinstance(mentions, list):
                entity_list.extend([_to_dict(m) for m in mentions])
            else:
                entity_list.append({"name": cluster_name, "cluster": cluster_name})
    elif isinstance(raw_entities, list):
        entity_list = [_to_dict(e) for e in raw_entities]
    else:
        entity_list = []

    # Normalise entity dicts: ensure "name" key exists (alias for canonical_name or entity)
    for e in entity_list:
        if "name" not in e:
            e["name"] = e.get("canonical_name", e.get("entity", ""))

    return {
        "entities": entity_list,
        "framing_devices": [_to_dict(d) for d in result.framing_devices],
        "sentiment": _to_dict(result.sentiment) if result.sentiment else {},
        "topics": [_to_dict(t) for t in result.topics] if result.topics else [],
        "sources": [_to_dict(s) for s in result.sources] if result.sources else [],
        "primary_entity": result.primary_entity,
        "anonymous_source_count": result.anonymous_source_count,
    }
