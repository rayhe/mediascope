"""Database operations for MediaScope data storage.

Provides engine/session management and CRUD helpers for articles,
sentiment scores, asymmetry results, and conflict records.
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlalchemy import create_engine, select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from mediascope.storage.models import (
    Article,
    AsymmetryResult,
    Base,
    ConflictRecord,
    EntityMention,
    SentimentScore,
)


def init_db(url: str = "sqlite:///mediascope.db") -> Engine:
    """Create the database engine and initialize all tables.

    Args:
        url: SQLAlchemy connection URL. Defaults to a local SQLite file.

    Returns:
        Configured Engine instance.
    """
    engine = create_engine(url, echo=False)
    Base.metadata.create_all(engine)
    return engine


def get_session(engine: Engine) -> Session:
    """Create a new database session.

    Args:
        engine: SQLAlchemy Engine.

    Returns:
        A new Session bound to the engine.
    """
    factory = sessionmaker(bind=engine)
    return factory()


def store_article(session: Session, article_data: dict) -> int:
    """Store an article and return its ID.

    If an article with the same URL already exists, returns the existing ID.

    Args:
        session: Active database session.
        article_data: Dict with keys matching Article columns:
            - "url" (required)
            - "title", "text", "author", "published_date",
              "publication_slug", "word_count" (optional)

    Returns:
        The article's database ID.
    """
    url = article_data["url"]

    # Check for existing
    existing = session.execute(
        select(Article).where(Article.url == url)
    ).scalar_one_or_none()

    if existing is not None:
        return existing.id

    article = Article(
        url=url,
        title=article_data.get("title", ""),
        text=article_data.get("text", ""),
        author=article_data.get("author"),
        published_date=article_data.get("published_date"),
        publication_slug=article_data.get("publication_slug", "unknown"),
        word_count=article_data.get("word_count", 0),
    )
    session.add(article)
    session.flush()  # populate article.id
    return article.id


def store_sentiment(session: Session, article_id: int, sentiment: dict) -> None:
    """Store sentiment analysis results for an article.

    Args:
        session: Active database session.
        article_id: ID of the article.
        sentiment: Dict with sentiment dimension values:
            - "overall_tone", "emotional_intensity", "source_authority",
              "agency_attribution", "headline_alignment",
              "anonymous_source_ratio", "speculative_language_ratio",
              "comparative_framing", "model_used" (all optional, have defaults)
    """
    score = SentimentScore(
        article_id=article_id,
        overall_tone=sentiment.get("overall_tone", 0.0),
        emotional_intensity=sentiment.get("emotional_intensity", 0.0),
        source_authority=sentiment.get("source_authority", 0.0),
        agency_attribution=sentiment.get("agency_attribution", 0.0),
        headline_alignment=sentiment.get("headline_alignment", 0.0),
        anonymous_source_ratio=sentiment.get("anonymous_source_ratio", 0.0),
        speculative_language_ratio=sentiment.get("speculative_language_ratio", 0.0),
        comparative_framing=sentiment.get("comparative_framing", 0.0),
        model_used=sentiment.get("model_used", "unknown"),
    )
    session.add(score)
    session.flush()


def store_asymmetry_result(session: Session, result: dict) -> None:
    """Store an asymmetry calculation result.

    Args:
        session: Active database session.
        result: Dict with keys:
            - "publication_slug", "target_entity", "period_start",
              "period_end", "asymmetry_score", "p_value", "cohens_d",
              "article_count"
    """
    record = AsymmetryResult(
        publication_slug=result["publication_slug"],
        target_entity=result["target_entity"],
        period_start=result["period_start"],
        period_end=result["period_end"],
        asymmetry_score=result.get("asymmetry_score", 0.0),
        p_value=result.get("p_value", 1.0),
        cohens_d=result.get("cohens_d", 0.0),
        article_count=result.get("article_count", 0),
    )
    session.add(record)
    session.flush()


def get_articles(
    session: Session,
    publication_slug: str,
    since: datetime | None = None,
    until: datetime | None = None,
) -> list[Article]:
    """Retrieve articles for a publication, optionally filtered by date range.

    Args:
        session: Active database session.
        publication_slug: Publication identifier.
        since: If set, only return articles published on or after this date.
        until: If set, only return articles published on or before this date.

    Returns:
        List of Article objects.
    """
    stmt = select(Article).where(Article.publication_slug == publication_slug)

    if since is not None:
        stmt = stmt.where(Article.published_date >= since)
    if until is not None:
        stmt = stmt.where(Article.published_date <= until)

    stmt = stmt.order_by(Article.published_date.desc())
    return list(session.scalars(stmt).all())


def get_asymmetry_history(
    session: Session,
    publication_slug: str,
    target_entity: str,
) -> list[AsymmetryResult]:
    """Retrieve historical asymmetry results for a publication + target entity.

    Args:
        session: Active database session.
        publication_slug: Publication identifier.
        target_entity: Entity name.

    Returns:
        List of AsymmetryResult objects, ordered by period_start descending.
    """
    stmt = (
        select(AsymmetryResult)
        .where(
            AsymmetryResult.publication_slug == publication_slug,
            AsymmetryResult.target_entity == target_entity,
        )
        .order_by(AsymmetryResult.period_start.desc())
    )
    return list(session.scalars(stmt).all())
