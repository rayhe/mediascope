"""Editorial Histories — journalist migration tracking and bias decomposition.

This module implements a difference-in-differences (DiD) framework for causal
attribution of media bias.  When a journalist moves from Publication A to
Publication B, three natural experiments emerge:

1. **Source-side effect** — Does Publication A's coverage change after the
   journalist leaves?  (Institutional vs. individual bias.)
2. **Portable bias** — Does the journalist's tone change at Publication B?
   (Editorial capture vs. portable bias.)
3. **Destination effect** — Does Publication B's coverage shift after the
   journalist arrives?  (Editorial influence.)

For the first time, agentic AI tooling makes it practical to run these
experiments systematically across hundreds of journalists and dozens of
publications.
"""

from mediascope.careers.models import (
    BiasDecomposition,
    CareerEvent,
    EditorialLeadershipChange,
    JournalistProfile,
    MigrationEvent,
)
from mediascope.careers.tracker import CareerTracker
from mediascope.careers.migrations import MigrationAnalyzer
from mediascope.careers.editorial_leadership import LeadershipAnalyzer
from mediascope.careers.influence import InfluenceScorer

__all__ = [
    "BiasDecomposition",
    "CareerEvent",
    "CareerTracker",
    "EditorialLeadershipChange",
    "InfluenceScorer",
    "JournalistProfile",
    "LeadershipAnalyzer",
    "MigrationAnalyzer",
    "MigrationEvent",
]
