"""Citation extraction, grading, and verification.

Extracts citations from text, grades source authority, and optionally
verifies that URLs resolve.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Optional
from urllib.parse import urlparse

import requests


@dataclass
class Citation:
    """A citation or attribution extracted from text."""

    text: str  # the citation text or surrounding context
    url: str = ""
    source_type: str = ""  # "primary", "secondary", "tertiary"
    verified: bool = False
    verification_method: str = ""
    domain: str = ""


# ── Domain authority lists ───────────────────────────────────────────

PRIMARY_DOMAINS: list[str] = [
    "sec.gov",
    "courtlistener.com",
    "pacer.gov",
    "congress.gov",
    "supremecourt.gov",
    "uscourts.gov",
    "federalregister.gov",
    "gao.gov",
    "cbo.gov",
    "bls.gov",
    "census.gov",
    "treasury.gov",
    "whitehouse.gov",
    "justice.gov",
    "ftc.gov",
    "fcc.gov",
    "fda.gov",
    "epa.gov",
    "nih.gov",
    "cdc.gov",
    "who.int",
    "worldbank.org",
    "imf.org",
    "ecfr.gov",
    "regulations.gov",
    "data.gov",
    "patents.google.com",
    "scholar.google.com",
    "pubmed.ncbi.nlm.nih.gov",
    "arxiv.org",
    "doi.org",
    "ssrn.com",
]

SECONDARY_DOMAINS: list[str] = [
    "reuters.com",
    "apnews.com",
    "wsj.com",
    "nytimes.com",
    "washingtonpost.com",
    "ft.com",
    "bloomberg.com",
    "economist.com",
    "bbc.com",
    "bbc.co.uk",
    "theguardian.com",
    "politico.com",
    "propublica.org",
    "theintercept.com",
    "cnbc.com",
    "fortune.com",
    "forbes.com",
    "theatlantic.com",
    "newyorker.com",
    "time.com",
    "latimes.com",
    "chicagotribune.com",
    "npr.org",
    "pbs.org",
    "nature.com",
    "science.org",
    "thelancet.com",
    "nejm.org",
    "bmj.com",
]

_URL_PATTERN = re.compile(
    r"https?://[^\s\)\]\>,\"']+",
    re.IGNORECASE,
)

_ATTRIBUTION_PATTERN = re.compile(
    r"(?:according to|as reported by|per|citing|said|told)\s+([^,\.;]{3,80})",
    re.IGNORECASE,
)

_FORMAL_CITE_PATTERN = re.compile(
    r"\[(\d+)\]|\(([A-Z][a-z]+(?:\s(?:et al\.?|&\s[A-Z][a-z]+))?(?:,?\s*\d{4})?)\)",
)


def extract_citations(text: str) -> list[Citation]:
    """Extract citations from text: URLs, attributions, and formal references.

    Args:
        text: Article or report text.

    Returns:
        List of Citation objects.
    """
    citations: list[Citation] = []
    seen_urls: set[str] = set()

    # Extract URLs
    for match in _URL_PATTERN.finditer(text):
        url = match.group(0).rstrip(".,;:!?)")
        if url in seen_urls:
            continue
        seen_urls.add(url)

        domain = _extract_domain(url)
        citations.append(Citation(
            text=_get_context(text, match.start(), 80),
            url=url,
            source_type=grade_source(url),
            domain=domain,
        ))

    # Extract "according to" attributions
    for match in _ATTRIBUTION_PATTERN.finditer(text):
        attribution = match.group(1).strip()
        citations.append(Citation(
            text=attribution,
            source_type="secondary",  # attributions are inherently secondary
            verification_method="attribution_extraction",
        ))

    # Extract formal citations [1], (Author 2024)
    for match in _FORMAL_CITE_PATTERN.finditer(text):
        ref = match.group(1) or match.group(2)
        citations.append(Citation(
            text=ref,
            source_type="secondary",
            verification_method="formal_citation_extraction",
        ))

    return citations


def grade_source(url: str) -> str:
    """Grade a URL's source authority level.

    Returns:
        "primary" for government, court, regulatory, academic sources.
        "secondary" for major wire services and newspapers of record.
        "tertiary" for everything else.
    """
    domain = _extract_domain(url).lower()

    for primary in PRIMARY_DOMAINS:
        if domain == primary or domain.endswith("." + primary):
            return "primary"

    for secondary in SECONDARY_DOMAINS:
        if domain == secondary or domain.endswith("." + secondary):
            return "secondary"

    return "tertiary"


def _extract_domain(url: str) -> str:
    """Extract the registered domain from a URL."""
    try:
        parsed = urlparse(url)
        hostname = parsed.hostname or ""
        # Strip www.
        if hostname.startswith("www."):
            hostname = hostname[4:]
        return hostname
    except Exception:
        return ""


def _get_context(text: str, position: int, window: int = 80) -> str:
    """Get surrounding context for a match position."""
    start = max(0, position - window)
    end = min(len(text), position + window)
    snippet = text[start:end].strip()
    if start > 0:
        snippet = "..." + snippet
    if end < len(text):
        snippet = snippet + "..."
    return snippet


def verify_url_exists(url: str, timeout: float = 10.0) -> bool:
    """Verify that a URL resolves by sending a HEAD request.

    Args:
        url: URL to verify.
        timeout: Request timeout in seconds.

    Returns:
        True if the URL returns an HTTP 2xx or 3xx status.
    """
    try:
        resp = requests.head(url, timeout=timeout, allow_redirects=True, headers={
            "User-Agent": "MediaScope/0.1 citation-checker"
        })
        return resp.status_code < 400
    except (requests.RequestException, Exception):
        return False


def citation_report(citations: list[Citation]) -> dict:
    """Generate summary statistics from a list of citations.

    Returns:
        Dict with counts by source type, verification stats, and domain breakdown.
    """
    total = len(citations)
    by_type: dict[str, int] = {"primary": 0, "secondary": 0, "tertiary": 0}
    verified_count = 0
    domains: dict[str, int] = {}

    for cit in citations:
        if cit.source_type in by_type:
            by_type[cit.source_type] += 1
        if cit.verified:
            verified_count += 1
        if cit.domain:
            domains[cit.domain] = domains.get(cit.domain, 0) + 1

    return {
        "total": total,
        "by_source_type": by_type,
        "verified": verified_count,
        "unverified": total - verified_count,
        "primary_ratio": by_type["primary"] / total if total > 0 else 0.0,
        "domains": domains,
    }
