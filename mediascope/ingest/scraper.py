"""Full article extraction with retry logic and rate limiting.

Uses newspaper3k for article parsing with exponential backoff,
configurable rate limiting, and user-agent rotation.
"""

from __future__ import annotations

import logging
import random
import time
from dataclasses import dataclass, field
from typing import Any

from newspaper import Article as NewspaperArticle
from newspaper import ArticleException

logger = logging.getLogger(__name__)

# Pool of user-agent strings to rotate through
USER_AGENTS: list[str] = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
]


@dataclass
class Article:
    """Extracted article content."""

    title: str = ""
    text: str = ""
    authors: list[str] = field(default_factory=list)
    publish_date: str = ""
    top_image: str = ""
    source_url: str = ""
    html: str = ""
    word_count: int = 0
    meta_description: str = ""


def _random_user_agent() -> str:
    """Select a random user-agent string from the pool."""
    return random.choice(USER_AGENTS)


def extract_article(
    url: str,
    max_retries: int = 3,
    base_delay: float = 1.0,
) -> Article:
    """Extract a full article from a URL using newspaper3k.

    Uses exponential backoff on failure and rotates user-agent strings.

    Args:
        url: The article URL to extract.
        max_retries: Maximum number of retry attempts.
        base_delay: Base delay in seconds for exponential backoff.

    Returns:
        An Article dataclass with extracted content.

    Raises:
        ArticleException: If extraction fails after all retries.
    """
    last_error: Exception | None = None

    for attempt in range(max_retries + 1):
        try:
            ua = _random_user_agent()
            article = NewspaperArticle(url, browser_user_agent=ua)
            article.download()
            article.parse()

            # Format publish date as ISO string if available
            pub_date = ""
            if article.publish_date:
                try:
                    pub_date = article.publish_date.isoformat()
                except (AttributeError, ValueError):
                    pub_date = str(article.publish_date)

            text = article.text or ""

            return Article(
                title=article.title or "",
                text=text,
                authors=list(article.authors) if article.authors else [],
                publish_date=pub_date,
                top_image=article.top_image or "",
                source_url=url,
                html=article.html or "",
                word_count=len(text.split()),
                meta_description=article.meta_description or "",
            )

        except ArticleException as e:
            last_error = e
            if attempt < max_retries:
                delay = base_delay * (2 ** attempt) + random.uniform(0, 0.5)
                logger.warning(
                    "Attempt %d/%d failed for %s: %s. Retrying in %.1fs",
                    attempt + 1,
                    max_retries + 1,
                    url,
                    e,
                    delay,
                )
                time.sleep(delay)
            else:
                logger.error(
                    "All %d attempts failed for %s: %s",
                    max_retries + 1,
                    url,
                    e,
                )

        except Exception as e:
            last_error = e
            if attempt < max_retries:
                delay = base_delay * (2 ** attempt) + random.uniform(0, 0.5)
                logger.warning(
                    "Unexpected error on attempt %d/%d for %s: %s. Retrying in %.1fs",
                    attempt + 1,
                    max_retries + 1,
                    url,
                    e,
                    delay,
                )
                time.sleep(delay)
            else:
                logger.error(
                    "All %d attempts failed for %s: %s",
                    max_retries + 1,
                    url,
                    e,
                )

    # Return an empty article with the URL on total failure rather than crashing
    logger.error("Returning empty article for %s after exhausting retries", url)
    return Article(source_url=url)


def extract_articles(
    urls: list[str],
    delay: float = 2.0,
    max_retries: int = 3,
) -> list[Article]:
    """Extract multiple articles with rate limiting.

    Args:
        urls: List of article URLs to extract.
        delay: Seconds to wait between requests (rate limiting).
        max_retries: Maximum retry attempts per article.

    Returns:
        List of Article objects (one per URL, may be empty on failure).
    """
    articles: list[Article] = []

    for i, url in enumerate(urls):
        logger.info("Extracting article %d/%d: %s", i + 1, len(urls), url)
        article = extract_article(url, max_retries=max_retries)
        articles.append(article)

        # Rate limiting — don't sleep after the last article
        if i < len(urls) - 1:
            jittered_delay = delay + random.uniform(0, delay * 0.25)
            logger.debug("Rate limit: sleeping %.1fs", jittered_delay)
            time.sleep(jittered_delay)

    logger.info(
        "Extracted %d articles (%d with content)",
        len(articles),
        sum(1 for a in articles if a.text),
    )
    return articles
