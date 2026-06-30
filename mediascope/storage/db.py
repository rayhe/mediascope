"""Database operations for MediaScope data storage.

Provides engine/session management, CRUD helpers for articles,
sentiment scores, asymmetry results, and conflict records,
and the ``MediaScopeDB`` class consumed by the CLI.
"""

from __future__ import annotations

import os
from contextlib import contextmanager
from datetime import datetime
from typing import Optional

from sqlalchemy import create_engine, func, select
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


# ======================================================================
# Low-level helpers (engine / session factories)
# ======================================================================


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


# ======================================================================
# MediaScopeDB — high-level wrapper for the CLI
# ======================================================================


class MediaScopeDB:
    """High-level database wrapper used by the CLI and scoring pipeline.

    Manages its own engine and session lifecycle so callers don't have
    to deal with SQLAlchemy directly.  Accepts either a file path
    (``mediascope.db``, ``/abs/path.db``) or a full SQLAlchemy URL
    (``sqlite:///mediascope.db``).
    """

    def __init__(self, db_url_or_path: str = "sqlite:///mediascope.db"):
        url = db_url_or_path
        # Accept a plain file path and turn it into a sqlite URL.
        if not url.startswith(("sqlite:", "postgresql:", "mysql:")):
            url = f"sqlite:///{url}"
        self._url = url
        self._engine: Engine | None = None
        self._session_factory: sessionmaker | None = None

    # ------------------------------------------------------------------
    # Connection helpers
    # ------------------------------------------------------------------

    def _ensure_engine(self) -> Engine:
        if self._engine is None:
            self._engine = create_engine(self._url, echo=False)
            Base.metadata.create_all(self._engine)
            self._session_factory = sessionmaker(bind=self._engine)
        return self._engine

    @contextmanager
    def session(self):
        """Yield a session; auto-commits on success, rolls back on error."""
        self._ensure_engine()
        sess = self._session_factory()  # type: ignore[misc]
        try:
            yield sess
            sess.commit()
        except Exception:
            sess.rollback()
            raise
        finally:
            sess.close()

    def connect(self) -> Engine:
        """Explicitly initialise the engine and return it."""
        return self._ensure_engine()

    # ------------------------------------------------------------------
    # Article CRUD
    # ------------------------------------------------------------------

    def store_article(self, article_data: dict) -> int:
        """Store an article and return its ID (idempotent on URL)."""
        with self.session() as sess:
            return _store_article_impl(sess, article_data)

    def get_articles(
        self,
        publication_slug: str,
        since: datetime | None = None,
        until: datetime | None = None,
    ) -> list[Article]:
        """Retrieve articles for a publication, optionally filtered by date."""
        with self.session() as sess:
            return _get_articles_impl(sess, publication_slug, since, until)

    # ------------------------------------------------------------------
    # Sentiment / asymmetry
    # ------------------------------------------------------------------

    def store_sentiment(self, article_id: int, sentiment: dict) -> None:
        with self.session() as sess:
            _store_sentiment_impl(sess, article_id, sentiment)

    def store_asymmetry_result(self, result: dict) -> None:
        with self.session() as sess:
            _store_asymmetry_impl(sess, result)

    def get_asymmetry_history(
        self, publication_slug: str, target_entity: str,
    ) -> list[AsymmetryResult]:
        with self.session() as sess:
            return _get_asymmetry_history_impl(
                sess, publication_slug, target_entity,
            )

    # ------------------------------------------------------------------
    # Stats (used by CLI ``status`` command)
    # ------------------------------------------------------------------

    def get_stats(self) -> dict:
        """Return aggregate statistics about the database.

        Returns a dict with:
            total_articles, total_analyses, db_size_mb,
            publications (keyed by slug with article_count,
            analysed_count, first_article_date, last_article_date,
            last_ingest).
        """
        self._ensure_engine()

        stats: dict = {
            "total_articles": 0,
            "total_analyses": 0,
            "db_size_mb": 0.0,
            "publications": {},
        }

        with self.session() as sess:
            stats["total_articles"] = (
                sess.scalar(select(func.count(Article.id))) or 0
            )
            stats["total_analyses"] = (
                sess.scalar(select(func.count(SentimentScore.id))) or 0
            )

            slugs = list(
                sess.scalars(select(Article.publication_slug).distinct()).all()
            )

            for slug in slugs:
                article_count = (
                    sess.scalar(
                        select(func.count(Article.id)).where(
                            Article.publication_slug == slug,
                        )
                    )
                    or 0
                )
                analysed_count = (
                    sess.scalar(
                        select(func.count(SentimentScore.id))
                        .join(Article)
                        .where(Article.publication_slug == slug)
                    )
                    or 0
                )
                first_date = sess.scalar(
                    select(func.min(Article.published_date)).where(
                        Article.publication_slug == slug,
                    )
                )
                last_date = sess.scalar(
                    select(func.max(Article.published_date)).where(
                        Article.publication_slug == slug,
                    )
                )
                last_ingest = sess.scalar(
                    select(func.max(Article.created_at)).where(
                        Article.publication_slug == slug,
                    )
                )

                stats["publications"][slug] = {
                    "article_count": article_count,
                    "analysed_count": analysed_count,
                    "first_article_date": (
                        first_date.strftime("%Y-%m-%d")
                        if first_date
                        else "—"
                    ),
                    "last_article_date": (
                        last_date.strftime("%Y-%m-%d")
                        if last_date
                        else "—"
                    ),
                    "last_ingest": (
                        last_ingest.strftime("%Y-%m-%d %H:%M")
                        if last_ingest
                        else "—"
                    ),
                }

        # Database file size (SQLite only)
        db_path = self._url.replace("sqlite:///", "")
        if os.path.isfile(db_path):
            stats["db_size_mb"] = os.path.getsize(db_path) / (1024 * 1024)

        return stats


# ======================================================================
# Module-level convenience functions (backward-compatible API)
# ======================================================================


def store_article(session: Session, article_data: dict) -> int:
    """Store an article and return its ID (idempotent on URL)."""
    return _store_article_impl(session, article_data)


def store_sentiment(
    session: Session, article_id: int, sentiment: dict,
) -> None:
    """Store sentiment analysis results for an article."""
    _store_sentiment_impl(session, article_id, sentiment)


def store_asymmetry_result(session: Session, result: dict) -> None:
    """Store an asymmetry calculation result."""
    _store_asymmetry_impl(session, result)


def get_articles(
    session: Session,
    publication_slug: str,
    since: datetime | None = None,
    until: datetime | None = None,
) -> list[Article]:
    """Retrieve articles for a publication, optionally filtered by date."""
    return _get_articles_impl(session, publication_slug, since, until)


def get_asymmetry_history(
    session: Session,
    publication_slug: str,
    target_entity: str,
) -> list[AsymmetryResult]:
    """Retrieve historical asymmetry results for a pub + target entity."""
    return _get_asymmetry_history_impl(session, publication_slug, target_entity)


# ======================================================================
# Internal implementations
# ======================================================================


def _store_article_impl(session: Session, article_data: dict) -> int:
    url = article_data["url"]

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


def _store_sentiment_impl(
    session: Session, article_id: int, sentiment: dict,
) -> None:
    score = SentimentScore(
        article_id=article_id,
        overall_tone=sentiment.get("overall_tone", 0.0),
        emotional_intensity=sentiment.get("emotional_intensity", 0.0),
        source_authority=sentiment.get("source_authority", 0.0),
        agency_attribution=sentiment.get("agency_attribution", 0.0),
        headline_alignment=sentiment.get("headline_alignment", 0.0),
        anonymous_source_ratio=sentiment.get("anonymous_source_ratio", 0.0),
        speculative_language_ratio=sentiment.get(
            "speculative_language_ratio", 0.0,
        ),
        comparative_framing=sentiment.get("comparative_framing", 0.0),
        model_used=sentiment.get("model_used", "unknown"),
    )
    session.add(score)
    session.flush()


def _store_asymmetry_impl(session: Session, result: dict) -> None:
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


def _get_articles_impl(
    session: Session,
    publication_slug: str,
    since: datetime | None = None,
    until: datetime | None = None,
) -> list[Article]:
    stmt = select(Article).where(Article.publication_slug == publication_slug)

    if since is not None:
        stmt = stmt.where(Article.published_date >= since)
    if until is not None:
        stmt = stmt.where(Article.published_date <= until)

    stmt = stmt.order_by(Article.published_date.desc())
    return list(session.scalars(stmt).all())


def _get_asymmetry_history_impl(
    session: Session,
    publication_slug: str,
    target_entity: str,
) -> list[AsymmetryResult]:
    stmt = (
        select(AsymmetryResult)
        .where(
            AsymmetryResult.publication_slug == publication_slug,
            AsymmetryResult.target_entity == target_entity,
        )
        .order_by(AsymmetryResult.period_start.desc())
    )
    return list(session.scalars(stmt).all())
