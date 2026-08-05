"""Competitor coverage analysis — cross-entity asymmetry detection.

Extends MediaScope's single-entity analysis pipeline to compare how
each profiled publication covers Meta's competitors (OpenAI, Anthropic,
Amazon, Apple, Google, X/Twitter). Loads financial relationship data
from profile YAML ``competitor_relationships`` sections and correlates
with measured coverage tone.

Usage::

    from mediascope.analyze.competitor import CompetitorAnalyzer

    analyzer = CompetitorAnalyzer(profiles_dir="profiles")
    matrix = analyzer.build_asymmetry_matrix(articles)
    report = analyzer.generate_correlation_report(matrix)
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from mediascope.analysis import ArticleAnalyzer, AnalysisResult
from mediascope.config import load_all_profiles, load_profile, PublicationProfile

logger = logging.getLogger(__name__)

# Target entities for cross-entity analysis
COMPETITOR_ENTITIES = [
    "meta", "openai", "anthropic", "amazon", "apple", "google", "x_twitter"
]

ENTITY_DISPLAY_NAMES = {
    "meta": "Meta",
    "openai": "OpenAI",
    "anthropic": "Anthropic",
    "amazon": "Amazon",
    "apple": "Apple",
    "google": "Google",
    "x_twitter": "X / Twitter",
}

# Financial tie severity weights (higher = stronger financial incentive)
FINANCIAL_TIE_WEIGHTS = {
    "licensing": 0.6,
    "investment": 0.9,
    "advertising": 0.4,
    "distribution": 0.3,
    "indirect": 0.2,
    "mixed": 0.4,
    "negotiating": 0.3,
    "none": 0.0,
    "adversarial": -0.7,
    "litigation": -0.8,
}


@dataclass
class CompetitorRelationship:
    """A publication's financial relationship with one competitor entity."""
    entity: str
    financial_tie: str = "none"
    estimated_value: str = "$0"
    direction: str = "none"
    description: str = ""
    source_url: str = ""
    coverage_prediction: str = "unknown"

    @property
    def financial_weight(self) -> float:
        """Numeric weight representing financial tie strength."""
        return FINANCIAL_TIE_WEIGHTS.get(self.financial_tie, 0.0)


@dataclass
class CoverageScore:
    """Coverage tone score for one publication × entity pair."""
    publication: str
    entity: str
    tone_score: float = 0.0  # -1.0 (adversarial) to +1.0 (favorable)
    article_count: int = 0
    framing_device_count: int = 0
    anonymous_source_ratio: float = 0.0
    loaded_language_count: int = 0


@dataclass
class AsymmetryCell:
    """One cell of the coverage asymmetry matrix."""
    publication: str
    entity: str
    coverage: CoverageScore
    relationship: CompetitorRelationship
    asymmetry_score: float = 0.0  # Positive = softer than predicted


@dataclass
class CoverageAsymmetryMatrix:
    """Matrix of [publication × entity] asymmetry scores."""
    cells: dict[tuple[str, str], AsymmetryCell] = field(default_factory=dict)
    publications: list[str] = field(default_factory=list)
    entities: list[str] = field(default_factory=list)

    def get(self, publication: str, entity: str) -> AsymmetryCell | None:
        return self.cells.get((publication, entity))

    def get_row(self, publication: str) -> list[AsymmetryCell]:
        return [c for (p, _), c in self.cells.items() if p == publication]

    def get_column(self, entity: str) -> list[AsymmetryCell]:
        return [c for (_, e), c in self.cells.items() if e == entity]

    def most_asymmetric(self, n: int = 10) -> list[AsymmetryCell]:
        """Return the N most asymmetric cells (biggest gap between
        financial tie and coverage tone)."""
        return sorted(
            self.cells.values(),
            key=lambda c: abs(c.asymmetry_score),
            reverse=True,
        )[:n]


class CompetitorAnalyzer:
    """Cross-entity coverage asymmetry analyzer.

    Loads competitor_relationships from publication profiles and runs
    the existing ArticleAnalyzer pipeline to score coverage tone for
    each target entity.
    """

    def __init__(self, profiles_dir: str | None = None):
        self.profiles_dir = profiles_dir or "profiles"
        self._profiles: dict[str, PublicationProfile] = {}
        self._relationships: dict[str, dict[str, CompetitorRelationship]] = {}
        self._entity_definitions: dict[str, dict] = {}
        self._load_profiles()
        self._load_entity_definitions()

    def _load_profiles(self) -> None:
        """Load all publication profiles and extract competitor_relationships."""
        self._profiles = load_all_profiles(self.profiles_dir)
        for slug, profile in self._profiles.items():
            raw = profile._raw
            cr = raw.get("competitor_relationships", {})
            if cr:
                self._relationships[slug] = {}
                for entity_key, rel_data in cr.items():
                    if isinstance(rel_data, dict):
                        self._relationships[slug][entity_key] = CompetitorRelationship(
                            entity=entity_key,
                            financial_tie=rel_data.get("financial_tie", "none"),
                            estimated_value=rel_data.get("estimated_value", "$0"),
                            direction=rel_data.get("direction", "none"),
                            description=rel_data.get("description", ""),
                            source_url=rel_data.get("source_url", ""),
                            coverage_prediction=rel_data.get("coverage_prediction", "unknown"),
                        )

    def _load_entity_definitions(self) -> None:
        """Load competitor entity definitions from YAML."""
        path = Path(self.profiles_dir) / "competitor-entities.yaml"
        if path.exists():
            with open(path, "r") as f:
                data = yaml.safe_load(f)
            self._entity_definitions = data.get("entities", {})

    def get_relationship(
        self, publication_slug: str, entity: str
    ) -> CompetitorRelationship | None:
        """Get the financial relationship between a publication and entity."""
        pub_rels = self._relationships.get(publication_slug, {})
        return pub_rels.get(entity)

    def get_entity_clusters(self, entity: str) -> dict[str, Any] | None:
        """Get entity detection clusters for a competitor."""
        defn = self._entity_definitions.get(entity)
        if not defn:
            return None
        return {
            defn["display_name"]: {
                "aliases": defn.get("aliases", []),
                "regex": defn.get("regex", ""),
            }
        }

    def analyze_article_for_entity(
        self, text: str, title: str, entity: str
    ) -> AnalysisResult:
        """Analyze an article's coverage of a specific competitor entity."""
        display_name = ENTITY_DISPLAY_NAMES.get(entity, entity)
        clusters = self.get_entity_clusters(entity)
        analyzer = ArticleAnalyzer(target_entity=display_name, clusters=clusters)
        return analyzer.analyze(text=text, title=title)

    def score_coverage_tone(
        self, result: AnalysisResult
    ) -> float:
        """Compute a composite tone score from an AnalysisResult.

        Returns a float from -1.0 (very adversarial) to +1.0 (very favorable).
        """
        if result.sentiment is None:
            return 0.0

        # Use composite sentiment score as base
        sent = result.sentiment
        if hasattr(sent, 'compound'):
            base_score = sent.compound
        elif hasattr(sent, 'overall_tone'):
            base_score = sent.overall_tone
        elif isinstance(sent, dict):
            base_score = sent.get('compound', sent.get('overall_tone', 0.0))
        else:
            base_score = 0.0

        # Adjust for framing devices (negative devices push score down)
        neg_devices = sum(
            1 for d in result.framing_devices
            if hasattr(d, 'category') and d.category in (
                'loaded_language', 'fear_appeal', 'catastrophizing',
                'speculation', 'editorial_dramatization',
            )
        )
        device_penalty = min(neg_devices * 0.05, 0.3)

        # Adjust for anonymous sources (higher ratio = more skeptical framing)
        anon_penalty = min(result.anonymous_source_count * 0.02, 0.1)

        return max(-1.0, min(1.0, base_score - device_penalty - anon_penalty))

    def build_asymmetry_matrix(
        self, articles: list[dict[str, str]]
    ) -> CoverageAsymmetryMatrix:
        """Build a [publication × entity] asymmetry matrix.

        Each article dict should have keys:
            - publication_slug: str
            - title: str
            - text: str
            - target_entity: str (one of COMPETITOR_ENTITIES)
        """
        matrix = CoverageAsymmetryMatrix(
            publications=list(self._relationships.keys()),
            entities=COMPETITOR_ENTITIES,
        )

        # Group articles by (publication, entity)
        grouped: dict[tuple[str, str], list[dict]] = {}
        for article in articles:
            key = (article["publication_slug"], article["target_entity"])
            grouped.setdefault(key, []).append(article)

        for (pub_slug, entity), pub_articles in grouped.items():
            # Analyze each article
            results = []
            for a in pub_articles:
                result = self.analyze_article_for_entity(
                    text=a["text"], title=a["title"], entity=entity
                )
                results.append(result)

            # Compute aggregate coverage score
            tone_scores = [self.score_coverage_tone(r) for r in results]
            avg_tone = sum(tone_scores) / len(tone_scores) if tone_scores else 0.0

            total_devices = sum(len(r.framing_devices) for r in results)
            total_anon = sum(r.anonymous_source_count for r in results)

            coverage = CoverageScore(
                publication=pub_slug,
                entity=entity,
                tone_score=avg_tone,
                article_count=len(results),
                framing_device_count=total_devices,
                anonymous_source_ratio=total_anon / max(len(results), 1),
            )

            # Get financial relationship
            relationship = self.get_relationship(pub_slug, entity) or CompetitorRelationship(
                entity=entity
            )

            # Compute asymmetry: difference between financial-tie prediction and actual tone
            # Positive asymmetry = softer coverage than expected (financial tie working)
            # Negative asymmetry = harsher coverage despite financial tie
            predicted_tone = relationship.financial_weight
            asymmetry = avg_tone - predicted_tone

            cell = AsymmetryCell(
                publication=pub_slug,
                entity=entity,
                coverage=coverage,
                relationship=relationship,
                asymmetry_score=asymmetry,
            )
            matrix.cells[(pub_slug, entity)] = cell

        return matrix

    def compute_financial_correlation(
        self, matrix: CoverageAsymmetryMatrix
    ) -> dict[str, Any]:
        """Compute correlation between financial ties and coverage tone.

        Returns stats on whether publications that receive money from an entity
        cover that entity more favorably.
        """
        paid_tones: list[float] = []
        unpaid_tones: list[float] = []
        adversarial_tones: list[float] = []

        for cell in matrix.cells.values():
            if cell.coverage.article_count == 0:
                continue

            if cell.relationship.financial_tie in ("licensing", "investment", "distribution"):
                paid_tones.append(cell.coverage.tone_score)
            elif cell.relationship.financial_tie in ("adversarial", "litigation"):
                adversarial_tones.append(cell.coverage.tone_score)
            else:
                unpaid_tones.append(cell.coverage.tone_score)

        def _avg(lst: list[float]) -> float:
            return sum(lst) / len(lst) if lst else 0.0

        return {
            "paid_avg_tone": _avg(paid_tones),
            "unpaid_avg_tone": _avg(unpaid_tones),
            "adversarial_avg_tone": _avg(adversarial_tones),
            "paid_count": len(paid_tones),
            "unpaid_count": len(unpaid_tones),
            "adversarial_count": len(adversarial_tones),
            "tone_gap_paid_vs_unpaid": _avg(paid_tones) - _avg(unpaid_tones),
            "tone_gap_paid_vs_adversarial": _avg(paid_tones) - _avg(adversarial_tones),
        }

    def identify_protected_entities(
        self, matrix: CoverageAsymmetryMatrix, threshold: float = 0.15
    ) -> list[dict[str, Any]]:
        """Identify entities that get measurably softer coverage from
        publications that pay them or have financial ties to them.

        Returns a list of {entity, publication, tone_score, financial_tie,
        asymmetry} dicts for pairs that exceed the threshold.
        """
        protected = []
        for cell in matrix.cells.values():
            if cell.coverage.article_count == 0:
                continue
            if (
                cell.relationship.financial_weight > 0
                and cell.coverage.tone_score > threshold
            ):
                protected.append({
                    "entity": ENTITY_DISPLAY_NAMES.get(cell.entity, cell.entity),
                    "publication": cell.publication,
                    "tone_score": round(cell.coverage.tone_score, 3),
                    "financial_tie": cell.relationship.financial_tie,
                    "estimated_value": cell.relationship.estimated_value,
                    "asymmetry": round(cell.asymmetry_score, 3),
                })

        return sorted(protected, key=lambda x: x["asymmetry"], reverse=True)

    def get_all_relationships_summary(self) -> list[dict[str, Any]]:
        """Return a flat summary of all publication × entity relationships."""
        rows = []
        for pub_slug, rels in self._relationships.items():
            for entity, rel in rels.items():
                rows.append({
                    "publication": pub_slug,
                    "entity": ENTITY_DISPLAY_NAMES.get(entity, entity),
                    "financial_tie": rel.financial_tie,
                    "estimated_value": rel.estimated_value,
                    "direction": rel.direction,
                    "coverage_prediction": rel.coverage_prediction,
                    "source_url": rel.source_url,
                })
        return rows
