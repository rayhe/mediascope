"""Configuration loader for MediaScope.

Loads publication profiles from YAML files and global config from
environment variables.
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

logger = logging.getLogger(__name__)


@dataclass
class PublicationProfile:
    """A single publication's profile for coverage analysis."""

    name: str
    slug: str
    url: str
    rss_feeds: list[str] = field(default_factory=list)
    ownership_chain: list[str] = field(default_factory=list)
    revenue_relationships: list[str] = field(default_factory=list)
    editorial_leadership: list[str] = field(default_factory=list)
    key_journalists: list[str] = field(default_factory=list)
    known_conflicts: list[str] = field(default_factory=list)
    litigation_connections: list[str] = field(default_factory=list)
    ai_crawl_policy: str = "unknown"
    target_entities: list[str] = field(default_factory=list)


@dataclass
class MediaScopeConfig:
    """Global configuration for MediaScope."""

    db_url: str = "sqlite:///mediascope.db"
    profiles_dir: str = "profiles"
    output_dir: str = "output"
    openai_api_key: str = ""
    models: dict[str, str] = field(default_factory=lambda: {
        "analysis": "gpt-4o",
        "embedding": "text-embedding-3-small",
    })

    @classmethod
    def from_env(cls) -> MediaScopeConfig:
        """Load configuration from environment variables."""
        config = cls(
            db_url=os.environ.get("MEDIASCOPE_DB_URL", cls.db_url),
            profiles_dir=os.environ.get("MEDIASCOPE_PROFILES_DIR", cls.profiles_dir),
            output_dir=os.environ.get("MEDIASCOPE_OUTPUT_DIR", cls.output_dir),
            openai_api_key=os.environ.get("MEDIASCOPE_OPENAI_KEY", ""),
        )
        return config


def _parse_profile(data: dict[str, Any], slug: str) -> PublicationProfile:
    """Parse a raw YAML dict into a PublicationProfile."""
    return PublicationProfile(
        name=data.get("name", slug),
        slug=slug,
        url=data.get("url", ""),
        rss_feeds=data.get("rss_feeds", []),
        ownership_chain=data.get("ownership_chain", []),
        revenue_relationships=data.get("revenue_relationships", []),
        editorial_leadership=data.get("editorial_leadership", []),
        key_journalists=data.get("key_journalists", []),
        known_conflicts=data.get("known_conflicts", []),
        litigation_connections=data.get("litigation_connections", []),
        ai_crawl_policy=data.get("ai_crawl_policy", "unknown"),
        target_entities=data.get("target_entities", []),
    )


def load_profile(slug: str, profiles_dir: str | None = None) -> PublicationProfile:
    """Load a single publication profile by slug.

    Args:
        slug: The profile slug (filename without extension).
        profiles_dir: Directory containing YAML profiles. Falls back to
            MEDIASCOPE_PROFILES_DIR env var, then 'profiles/'.

    Returns:
        The loaded PublicationProfile.

    Raises:
        FileNotFoundError: If the profile YAML file does not exist.
        ValueError: If the YAML file cannot be parsed.
    """
    if profiles_dir is None:
        profiles_dir = os.environ.get("MEDIASCOPE_PROFILES_DIR", "profiles")

    path = Path(profiles_dir) / f"{slug}.yaml"
    if not path.exists():
        # Try .yml extension as fallback
        path = Path(profiles_dir) / f"{slug}.yml"

    if not path.exists():
        raise FileNotFoundError(f"Profile not found: {slug} (looked in {profiles_dir})")

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise ValueError(f"Failed to parse profile {slug}: {e}") from e

    if not isinstance(data, dict):
        raise ValueError(f"Profile {slug} must be a YAML mapping, got {type(data).__name__}")

    logger.info("Loaded profile: %s from %s", slug, path)
    return _parse_profile(data, slug)


def load_all_profiles(profiles_dir: str | None = None) -> dict[str, PublicationProfile]:
    """Load all publication profiles from the profiles directory.

    Args:
        profiles_dir: Directory containing YAML profiles. Falls back to
            MEDIASCOPE_PROFILES_DIR env var, then 'profiles/'.

    Returns:
        Dict mapping slug to PublicationProfile.
    """
    if profiles_dir is None:
        profiles_dir = os.environ.get("MEDIASCOPE_PROFILES_DIR", "profiles")

    profiles_path = Path(profiles_dir)
    if not profiles_path.exists():
        logger.warning("Profiles directory does not exist: %s", profiles_dir)
        return {}

    profiles: dict[str, PublicationProfile] = {}
    for yaml_file in sorted(profiles_path.glob("*.y*ml")):
        slug = yaml_file.stem
        try:
            profiles[slug] = load_profile(slug, profiles_dir)
        except (ValueError, FileNotFoundError) as e:
            logger.warning("Skipping profile %s: %s", slug, e)

    logger.info("Loaded %d profiles from %s", len(profiles), profiles_dir)
    return profiles
