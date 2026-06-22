"""SQLAlchemy 2.0 models for MediaScope data storage.

Defines the schema for articles, entity mentions, sentiment scores,
asymmetry results, and conflict records.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import (
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)


class Base(DeclarativeBase):
    """SQLAlchemy declarative base for all MediaScope models."""
    pass


class Article(Base):
    """A scraped and analyzed article."""

    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    url: Mapped[str] = mapped_column(String(2048), unique=True, nullable=False)
    title: Mapped[str] = mapped_column(String(1024), nullable=False, default="")
    text: Mapped[str] = mapped_column(Text, nullable=False, default="")
    author: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    published_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    publication_slug: Mapped[str] = mapped_column(String(128), nullable=False, index=True)
    word_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now(),
    )

    # Relationships
    entity_mentions: Mapped[list["EntityMention"]] = relationship(
        back_populates="article", cascade="all, delete-orphan",
    )
    sentiment_scores: Mapped[list["SentimentScore"]] = relationship(
        back_populates="article", cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<Article(id={self.id}, slug={self.publication_slug!r}, title={self.title[:50]!r})>"


class EntityMention(Base):
    """A mention of a named entity within an article."""

    __tablename__ = "entity_mentions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    article_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("articles.id", ondelete="CASCADE"), nullable=False, index=True,
    )
    entity: Mapped[str] = mapped_column(String(512), nullable=False)
    canonical_name: Mapped[str] = mapped_column(String(512), nullable=False, default="")
    cluster: Mapped[Optional[str]] = mapped_column(String(256), nullable=True)
    mention_count: Mapped[int] = mapped_column(Integer, nullable=False, default=1)

    article: Mapped["Article"] = relationship(back_populates="entity_mentions")

    def __repr__(self) -> str:
        return f"<EntityMention(id={self.id}, entity={self.entity!r}, count={self.mention_count})>"


class SentimentScore(Base):
    """Multi-dimensional sentiment analysis result for an article."""

    __tablename__ = "sentiment_scores"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    article_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("articles.id", ondelete="CASCADE"), nullable=False, index=True,
    )
    overall_tone: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    emotional_intensity: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    source_authority: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    agency_attribution: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    headline_alignment: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    anonymous_source_ratio: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    speculative_language_ratio: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    comparative_framing: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    model_used: Mapped[str] = mapped_column(String(128), nullable=False, default="unknown")

    article: Mapped["Article"] = relationship(back_populates="sentiment_scores")

    def __repr__(self) -> str:
        return f"<SentimentScore(id={self.id}, article_id={self.article_id}, tone={self.overall_tone:.2f})>"


class AsymmetryResult(Base):
    """Stored result of an asymmetry calculation."""

    __tablename__ = "asymmetry_results"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    publication_slug: Mapped[str] = mapped_column(String(128), nullable=False, index=True)
    target_entity: Mapped[str] = mapped_column(String(512), nullable=False, index=True)
    period_start: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    period_end: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    asymmetry_score: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    p_value: Mapped[float] = mapped_column(Float, nullable=False, default=1.0)
    cohens_d: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    article_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now(),
    )

    def __repr__(self) -> str:
        return (
            f"<AsymmetryResult(id={self.id}, slug={self.publication_slug!r}, "
            f"target={self.target_entity!r}, score={self.asymmetry_score:.3f})>"
        )


class ConflictRecord(Base):
    """A recorded conflict of interest."""

    __tablename__ = "conflict_records"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    publication_slug: Mapped[str] = mapped_column(String(128), nullable=False, index=True)
    conflict_type: Mapped[str] = mapped_column(String(64), nullable=False)
    source_entity: Mapped[str] = mapped_column(String(512), nullable=False)
    target_entity: Mapped[str] = mapped_column(String(512), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    severity: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    evidence_url: Mapped[Optional[str]] = mapped_column(String(2048), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now(),
    )

    def __repr__(self) -> str:
        return (
            f"<ConflictRecord(id={self.id}, type={self.conflict_type!r}, "
            f"source={self.source_entity!r}, severity={self.severity})>"
        )
