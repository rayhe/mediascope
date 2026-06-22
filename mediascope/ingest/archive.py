"""Historical article retrieval via the Internet Archive Wayback Machine.

Uses the CDX API for searching archived snapshots and fetches
archived versions of articles.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass

import requests

logger = logging.getLogger(__name__)

CDX_API_URL = "https://web.archive.org/cdx/search/cdx"
WAYBACK_BASE = "https://web.archive.org/web"


def search_wayback(
    url: str,
    from_date: str,
    to_date: str,
    limit: int = 100,
    match_type: str = "exact",
) -> list[str]:
    """Search the Wayback Machine for archived snapshots of a URL.

    Uses the CDX Server API to find available snapshots within a date range.

    Args:
        url: The original URL to search for.
        from_date: Start date in YYYYMMDD format (e.g., "20240101").
        to_date: End date in YYYYMMDD format (e.g., "20241231").
        limit: Maximum number of results to return.
        match_type: CDX match type — "exact", "prefix", "host", or "domain".

    Returns:
        List of Wayback Machine URLs for archived snapshots, sorted by date.
    """
    params = {
        "url": url,
        "from": from_date,
        "to": to_date,
        "output": "json",
        "limit": str(limit),
        "matchType": match_type,
        # Only successful captures
        "filter": "statuscode:200",
        # Fields: urlkey, timestamp, original, mimetype, statuscode, digest, length
        "fl": "timestamp,original",
    }

    try:
        resp = requests.get(CDX_API_URL, params=params, timeout=30)
        resp.raise_for_status()
    except requests.RequestException as e:
        logger.error("Wayback CDX API request failed for %s: %s", url, e)
        return []

    try:
        data = resp.json()
    except ValueError:
        logger.error("Failed to parse CDX response as JSON for %s", url)
        return []

    if not data or len(data) < 2:
        logger.info("No Wayback snapshots found for %s (%s–%s)", url, from_date, to_date)
        return []

    # First row is the header; remaining rows are results
    wayback_urls: list[str] = []
    for row in data[1:]:
        if len(row) >= 2:
            timestamp, original_url = row[0], row[1]
            wb_url = f"{WAYBACK_BASE}/{timestamp}/{original_url}"
            wayback_urls.append(wb_url)

    logger.info(
        "Found %d Wayback snapshots for %s (%s–%s)",
        len(wayback_urls),
        url,
        from_date,
        to_date,
    )
    return wayback_urls


def fetch_archived(url: str) -> dict:
    """Fetch an article from the Wayback Machine.

    Accepts either a direct Wayback URL (web.archive.org/web/...) or
    an original URL (which will be looked up for the latest snapshot).

    Args:
        url: A Wayback Machine URL or an original URL.

    Returns:
        Dict with keys: title, text, source_url, archived_url, timestamp.
        Returns an empty-ish dict on failure.
    """
    # If it's not already a Wayback URL, get the latest snapshot
    if "web.archive.org" not in url:
        archived_url = _get_latest_snapshot(url)
        if not archived_url:
            logger.warning("No Wayback snapshot available for %s", url)
            return {
                "title": "",
                "text": "",
                "source_url": url,
                "archived_url": "",
                "timestamp": "",
            }
    else:
        archived_url = url

    try:
        resp = requests.get(archived_url, timeout=30)
        resp.raise_for_status()
    except requests.RequestException as e:
        logger.error("Failed to fetch archived page %s: %s", archived_url, e)
        return {
            "title": "",
            "text": "",
            "source_url": url,
            "archived_url": archived_url,
            "timestamp": "",
        }

    html = resp.text

    # Basic title extraction from HTML
    title = ""
    import re
    title_match = re.search(r"<title[^>]*>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if title_match:
        title = title_match.group(1).strip()

    # Extract timestamp from Wayback URL
    timestamp = ""
    ts_match = re.search(r"/web/(\d{14})/", archived_url)
    if ts_match:
        timestamp = ts_match.group(1)

    # Simple text extraction: strip HTML tags
    text = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    return {
        "title": title,
        "text": text,
        "source_url": url,
        "archived_url": archived_url,
        "timestamp": timestamp,
    }


def _get_latest_snapshot(url: str) -> str:
    """Look up the most recent Wayback snapshot for a URL.

    Uses the Wayback Availability API.

    Args:
        url: The original URL.

    Returns:
        The Wayback Machine URL for the latest snapshot, or empty string.
    """
    api_url = "https://archive.org/wayback/available"
    try:
        resp = requests.get(api_url, params={"url": url}, timeout=15)
        resp.raise_for_status()
        data = resp.json()
    except (requests.RequestException, ValueError) as e:
        logger.error("Wayback availability check failed for %s: %s", url, e)
        return ""

    snapshots = data.get("archived_snapshots", {})
    closest = snapshots.get("closest", {})
    if closest.get("available"):
        return closest.get("url", "")

    return ""
