"""Top-level database access shim for the CLI.

Re-exports the storage subpackage's DB class and helpers when the
storage dependencies (SQLAlchemy) are available.  Falls back to a
minimal stub so the CLI can still load and display ``--help``.
"""

try:
    from mediascope.storage.db import *  # noqa: F401,F403
    # Re-export MediaScopeDB if the storage module defines it
    try:
        from mediascope.storage.db import MediaScopeDB  # noqa: F811
    except ImportError:
        pass
except (ImportError, ModuleNotFoundError):
    pass

# Ensure MediaScopeDB is always available (stub if storage deps missing)
if "MediaScopeDB" not in dir():
    class MediaScopeDB:  # type: ignore[no-redef]
        """Stub database class — install storage dependencies for full use."""

        def __init__(self, db_url: str = "sqlite:///mediascope.db"):
            self.db_url = db_url

        def connect(self):
            raise NotImplementedError(
                "MediaScopeDB requires SQLAlchemy. "
                "Run: pip install sqlalchemy"
            )
