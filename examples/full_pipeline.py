"""MediaScope Full Pipeline Example.

Demonstrates the complete workflow: ingest articles from RSS,
analyze sentiment and entities, calculate asymmetry scores,
and generate a weekly report with disclosure.
"""

from datetime import datetime, timedelta

from mediascope.config import load_profile
from mediascope.ingest.rss import fetch_all_feeds, filter_by_date
from mediascope.ingest.scraper import extract_articles
from mediascope.analyze.entities import detect_entities, get_primary_entity
from mediascope.analyze.sentiment import analyze_composite
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sources import extract_sources, grade_source_authority
from mediascope.analyze.topics import classify_topic
from mediascope.score.asymmetry import calculate_asymmetry, generate_asymmetry_report
from mediascope.score.byline import build_journalist_profiles, rank_by_asymmetry
from mediascope.conflicts.disclosure import generate_disclosure
from mediascope.quality.standards import check_quality
from mediascope.storage.db import init_db, get_session, store_article, store_sentiment


def main():
    # Configuration
    PUBLICATION = "wired"
    TARGET_ENTITY = "Meta"
    DAYS_BACK = 7

    # 1. Setup
    print("=" * 60)
    print("MediaScope Full Pipeline")
    print("=" * 60)

    profile = load_profile(PUBLICATION)
    period_end = datetime.now()
    period_start = period_end - timedelta(days=DAYS_BACK)

    # Initialize database
    engine = init_db()
    session = get_session(engine)

    # 2. Ingest
    print(f"\n[INGEST] Fetching RSS feeds for {profile.name}...")
    entries = fetch_all_feeds(profile)
    recent = filter_by_date(entries, since=period_start, until=period_end)
    print(f"  Found {len(recent)} articles in the last {DAYS_BACK} days")

    if not recent:
        print("  No articles found. Try a longer time range.")
        return

    # Extract full article text (with rate limiting)
    print(f"  Extracting full text for {len(recent)} articles...")
    urls = [e.url for e in recent[:20]]  # Limit to 20 for demo
    articles = extract_articles(urls, delay=2.0)
    print(f"  Successfully extracted {len(articles)} articles")

    # 3. Analyze
    print(f"\n[ANALYZE] Running analysis pipeline...")
    analyzed = []

    for article in articles:
        # Entity detection
        entities = detect_entities(article.text)
        primary = get_primary_entity(entities)

        if not primary:
            continue

        # Sentiment analysis
        sentiment = analyze_composite(article.text, article.title)

        # Framing devices
        framing = detect_framing_devices(article.text)

        # Source analysis
        sources = extract_sources(article.text)
        authority = grade_source_authority(sources)

        # Topic classification
        topics = classify_topic(article.text)

        analyzed.append({
            "title": article.title,
            "url": article.source_url,
            "author": article.authors[0] if article.authors else "Unknown",
            "published": article.publish_date,
            "primary_entity": primary,
            "sentiment": sentiment,
            "framing_devices": framing,
            "sources": sources,
            "source_authority": authority,
            "topics": topics,
        })

        # Store in database
        article_id = store_article(session, {
            "url": article.source_url,
            "title": article.title,
            "text": article.text,
            "author": article.authors[0] if article.authors else None,
            "published_date": article.publish_date,
            "publication_slug": PUBLICATION,
            "word_count": article.word_count,
        })
        store_sentiment(session, article_id, sentiment.__dict__)

    session.commit()
    print(f"  Analyzed {len(analyzed)} articles")

    # 4. Score
    print(f"\n[SCORE] Calculating asymmetry scores...")

    # Group by entity
    target_scores = [
        a["sentiment"].overall_tone
        for a in analyzed
        if a["primary_entity"] == TARGET_ENTITY
    ]
    peer_scores = [
        a["sentiment"].overall_tone
        for a in analyzed
        if a["primary_entity"] != TARGET_ENTITY
    ]

    if target_scores and peer_scores:
        result = calculate_asymmetry(
            target_scores=target_scores,
            peer_scores=peer_scores,
            target_entity=TARGET_ENTITY,
            peer_entities=list(set(
                a["primary_entity"] for a in analyzed
                if a["primary_entity"] != TARGET_ENTITY
            )),
            publication_slug=PUBLICATION,
            period_start=period_start,
            period_end=period_end,
        )

        print(f"  Target ({TARGET_ENTITY}) avg tone: {result.target_avg_tone:.3f}")
        print(f"  Peer avg tone: {result.peer_avg_tone:.3f}")
        print(f"  Asymmetry score: {result.asymmetry_score:.3f}")
        print(f"  p-value: {result.p_value:.4f}")
        print(f"  Cohen's d: {result.cohens_d:.3f}")
        print(f"  Significant: {result.is_significant}")

    # Journalist profiles
    profiles = build_journalist_profiles(analyzed)
    rankings = rank_by_asymmetry(profiles, TARGET_ENTITY)
    if rankings:
        print(f"\n  Journalist Asymmetry Rankings:")
        for name, score in rankings[:5]:
            print(f"    {name}: {score:.3f}")

    # 5. Disclosure
    print(f"\n[DISCLOSE] Generating conflict disclosure...")
    disclosure = generate_disclosure(
        profile=profile.to_dict(),
        target_entity=TARGET_ENTITY,
    )
    print(disclosure)

    # 6. Quality Check
    print(f"\n[QUALITY] Checking output quality...")
    quality = check_quality(disclosure)
    print(f"  Score: {quality.score}/100")
    print(f"  Passed: {quality.passed}")
    for issue in quality.issues:
        print(f"  [{issue.severity}] {issue.description}")

    print("\n" + "=" * 60)
    print("Pipeline complete.")
    print("=" * 60)


if __name__ == "__main__":
    main()
