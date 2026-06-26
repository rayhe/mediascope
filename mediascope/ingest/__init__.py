"""Article ingestion modules."""

try:
    from mediascope.ingest.rss import fetch_feed, fetch_all_feeds, FeedEntry
    from mediascope.ingest.scraper import extract_article, extract_articles, Article
except (ImportError, ModuleNotFoundError):
    # Dependencies (feedparser, newspaper3k) not installed — stubs for CLI loading
    fetch_feed = fetch_all_feeds = FeedEntry = None  # type: ignore[assignment]
    extract_article = extract_articles = Article = None  # type: ignore[assignment]


class ArticleIngester:
    """High-level ingestion orchestrator for the CLI.

    Combines RSS feed fetching and article text extraction into a
    single pipeline.

    Usage::

        ingester = ArticleIngester(publication_slug="wired")
        articles = ingester.ingest(since="2025-01-01")
    """

    def __init__(self, publication_slug: str = "", profile=None):
        self.publication_slug = publication_slug
        self.profile = profile

    def ingest(self, since: str = "", until: str = "", limit: int = 0):
        """Fetch RSS feeds and extract article text.

        Returns a list of ``Article`` objects with full text extracted.
        """
        if fetch_all_feeds is None:
            raise ImportError(
                "Ingestion requires feedparser and newspaper3k. "
                "Run: pip install feedparser newspaper3k"
            )
        if self.profile is None:
            from mediascope.config import load_profile
            self.profile = load_profile(self.publication_slug)

        entries = fetch_all_feeds(self.profile)

        if since:
            from mediascope.ingest.rss import filter_by_date
            from datetime import datetime
            since_dt = datetime.fromisoformat(since)
            until_dt = datetime.fromisoformat(until) if until else None
            entries = filter_by_date(entries, since=since_dt, until=until_dt)

        if limit and limit > 0:
            entries = entries[:limit]

        urls = [e.url for e in entries if e.url]
        articles = extract_articles(urls)
        return articles
