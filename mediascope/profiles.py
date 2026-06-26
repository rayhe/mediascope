"""Publication profile helpers — re-exports from ``mediascope.config``.

The CLI imports ``load_profile``, ``load_all_profiles``, and
``validate_profile`` from this module.  The first two are implemented
in ``config.py``; ``validate_profile`` is a lightweight checker
added here.
"""

from mediascope.config import load_profile, load_all_profiles, PublicationProfile

__all__ = ["load_profile", "load_all_profiles", "validate_profile"]


def validate_profile(profile: PublicationProfile) -> list[str]:
    """Return a list of validation warnings for *profile*.

    An empty list means the profile passes all checks.
    """
    warnings: list[str] = []
    if not profile.name:
        warnings.append("Missing required field: name")
    if not profile.slug:
        warnings.append("Missing required field: slug")
    if not profile.url:
        warnings.append("Missing required field: url")
    if not profile.rss_feeds:
        warnings.append("No RSS feeds configured — ingestion will have no sources")
    if not profile.ownership_chain:
        warnings.append("No ownership chain — conflict disclosure will be incomplete")
    return warnings
