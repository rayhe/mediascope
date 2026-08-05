"""
Tests for Mike Isaac cross-entity coverage analysis and Eli Tan succession at the NYT.

Key finding: When the SAME journalist (Isaac) covers multiple entities after a beat
expansion, framing is remarkably consistent across Meta, Anthropic, SpaceX, and OpenAI.
The NYT's Meta coverage asymmetry is an INSTITUTIONAL ASSIGNMENT pattern — the editorial
choice to maintain a dedicated adversarial Meta beat (12+ years) while covering
OpenAI/Anthropic through a technology-progress lens (Cade Metz). The variable controlling
framing is beat assignment, not individual reporter bias.

The Eli Tan succession analysis shows the NYT immediately placed a junior replacement
on the dedicated Meta beat (into the child safety addiction trial) — perpetuating the
adversarial lane structure.

Sources:
- Talking Biz News beat change announcement:
  https://talkingbiznews.com/media-news/ny-times-taps-tan-to-cover-meta-isaac-to-cover-silicon-valley/
- NYT official announcement (nytco.com):
  https://www.nytco.com/press/staff-news-from-business/
- Techmeme citations for article sourcing
- Muck Rack portfolio: https://muckrack.com/MikeIsaac
- Marquette Zuckerberg Files archive:
  https://epublications.marquette.edu/zuckerberg_files_transcripts/2266
"""

import yaml
import pathlib

PROFILES = pathlib.Path(__file__).resolve().parent.parent / "profiles"


def _load_yaml(name: str) -> dict:
    with open(PROFILES / name, encoding="utf-8") as f:
        return yaml.safe_load(f)


# ===================================================================
# Mike Isaac — Profile Exists with Cross-Entity Analysis
# ===================================================================

class TestMikeIsaacProfile:
    """Mike Isaac journalist entry has cross-entity coverage analysis."""

    @classmethod
    def setup_class(cls):
        cls.profile = _load_yaml("nytimes.yaml")
        journalists = cls.profile.get("key_journalists", [])
        cls.isaac = next(
            (j for j in journalists if j.get("name") == "Mike Isaac"), None
        )

    def test_isaac_exists(self):
        assert self.isaac is not None, "Mike Isaac must be in key_journalists"

    def test_beat_reflects_expansion(self):
        beat = self.isaac.get("beat", "")
        assert "silicon valley" in beat.lower() or "formerly" in beat.lower(), \
            "Beat should reflect 2026 expansion beyond dedicated Meta role"

    def test_has_cross_entity_analysis(self):
        assert "cross_entity_coverage_analysis" in self.isaac, \
            "Isaac must have cross_entity_coverage_analysis section"

    def test_has_beat_change_record(self):
        assert "beat_change" in self.isaac, \
            "Isaac must have beat_change section documenting the transition"

    def test_beat_change_has_replacement(self):
        bc = self.isaac.get("beat_change", {})
        replacement = bc.get("replacement", "")
        assert "eli tan" in replacement.lower(), \
            "Beat change must record Eli Tan as replacement"

    def test_beat_change_has_source(self):
        bc = self.isaac.get("beat_change", {})
        source = bc.get("source_url", "")
        assert "talkingbiznews" in source or "nytco" in source, \
            "Beat change must cite source URL"


# ===================================================================
# Mike Isaac — Cross-Entity Coverage (Post Beat Change)
# ===================================================================

class TestIsaacCrossEntityCoverage:
    """Isaac's cross-entity coverage demonstrates consistent framing."""

    @classmethod
    def setup_class(cls):
        cls.profile = _load_yaml("nytimes.yaml")
        journalists = cls.profile.get("key_journalists", [])
        isaac = next(
            (j for j in journalists if j.get("name") == "Mike Isaac"), None
        )
        cls.analysis = isaac.get("cross_entity_coverage_analysis", {})

    def test_has_meta_post_beat_change(self):
        assert "meta_coverage_post_beat_change" in self.analysis, \
            "Must document Meta coverage after beat expansion"

    def test_meta_post_beat_change_tone_not_adversarial(self):
        meta = self.analysis.get("meta_coverage_post_beat_change", {})
        tone = meta.get("tone", "").lower()
        assert "adversarial" not in tone, \
            "Isaac's post-expansion Meta coverage should not be adversarial"

    def test_meta_post_beat_change_has_examples(self):
        meta = self.analysis.get("meta_coverage_post_beat_change", {})
        examples = meta.get("examples", [])
        assert len(examples) >= 3, \
            "Must have at least 3 examples of post-expansion Meta coverage"

    def test_has_anthropic_coverage(self):
        assert "anthropic_coverage" in self.analysis, \
            "Must document Isaac's Anthropic coverage"

    def test_anthropic_tone_neutral(self):
        anthropic = self.analysis.get("anthropic_coverage", {})
        tone = anthropic.get("tone", "").lower()
        assert "neutral" in tone or "business" in tone, \
            "Isaac's Anthropic coverage should be neutral/business-oriented"

    def test_has_spacex_coverage(self):
        assert "spacex_coverage" in self.analysis, \
            "Must document Isaac's SpaceX coverage"

    def test_has_openai_coverage(self):
        assert "openai_coverage" in self.analysis, \
            "Must document Isaac's OpenAI coverage"

    def test_cross_entity_significance_documented(self):
        assert "cross_entity_significance" in self.analysis, \
            "Must have cross_entity_significance explaining the pattern"

    def test_significance_mentions_beat_assignment(self):
        sig = self.analysis.get("cross_entity_significance", "")
        assert "beat assignment" in sig.lower() or "beat" in sig.lower(), \
            "Significance must identify beat assignment as the variable"


# ===================================================================
# Eli Tan — Succession Analysis
# ===================================================================

class TestEliTanSuccession:
    """Eli Tan entry documents the Meta beat succession and its significance."""

    @classmethod
    def setup_class(cls):
        cls.profile = _load_yaml("nytimes.yaml")
        journalists = cls.profile.get("key_journalists", [])
        cls.tan = next(
            (j for j in journalists if j.get("name") == "Eli Tan"), None
        )

    def test_tan_exists(self):
        assert self.tan is not None, "Eli Tan must be in key_journalists"

    def test_beat_is_meta(self):
        beat = self.tan.get("beat", "").lower()
        assert "meta" in beat, "Tan's beat should be Meta"

    def test_has_succession_analysis(self):
        assert "succession_analysis" in self.tan, \
            "Tan must have succession_analysis section"

    def test_replaced_isaac(self):
        sa = self.tan.get("succession_analysis", {})
        replaced = sa.get("replaced", "").lower()
        assert "mike isaac" in replaced or "isaac" in replaced, \
            "Succession must record Isaac as predecessor"

    def test_has_first_major_assignments(self):
        sa = self.tan.get("succession_analysis", {})
        assignments = sa.get("first_major_assignments", [])
        assert len(assignments) >= 3, \
            "Must document at least 3 first major assignments"

    def test_first_assignments_include_addiction_trial(self):
        sa = self.tan.get("succession_analysis", {})
        assignments = sa.get("first_major_assignments", [])
        titles = [a.get("title", "").lower() for a in assignments]
        addiction_coverage = any("addiction" in t or "negligent" in t for t in titles)
        assert addiction_coverage, \
            "First assignments must include the social media addiction trial"

    def test_has_analytical_significance(self):
        sa = self.tan.get("succession_analysis", {})
        assert "analytical_significance" in sa, \
            "Succession must have analytical_significance section"

    def test_significance_mentions_adversarial_lane(self):
        sa = self.tan.get("succession_analysis", {})
        sig = sa.get("analytical_significance", "").lower()
        assert "adversarial" in sig or "accountability" in sig, \
            "Significance must identify the adversarial lane perpetuation"


# ===================================================================
# Cross-Entity Comparison: Isaac vs Metz
# ===================================================================

class TestIsaacMetzComparison:
    """Compare Isaac and Metz's cross-entity patterns."""

    @classmethod
    def setup_class(cls):
        cls.profile = _load_yaml("nytimes.yaml")
        journalists = cls.profile.get("key_journalists", [])
        cls.isaac = next(
            (j for j in journalists if j.get("name") == "Mike Isaac"), None
        )
        cls.metz = next(
            (j for j in journalists if j.get("name") == "Cade Metz"), None
        )

    def test_both_have_cross_entity_analysis(self):
        assert "cross_entity_coverage_analysis" in self.isaac, \
            "Isaac must have cross-entity analysis"
        assert "cross_entity_coverage_analysis" in self.metz, \
            "Metz must have cross-entity analysis"

    def test_isaac_covers_meta_and_competitors(self):
        """Isaac's post-expansion coverage spans Meta AND other entities."""
        analysis = self.isaac.get("cross_entity_coverage_analysis", {})
        has_meta = "meta_coverage_post_beat_change" in analysis
        has_anthropic = "anthropic_coverage" in analysis
        has_spacex = "spacex_coverage" in analysis
        assert has_meta and has_anthropic and has_spacex, \
            "Isaac must document Meta, Anthropic, and SpaceX coverage"

    def test_metz_avoids_meta(self):
        """Metz's coverage shows near-zero standalone Meta AI articles."""
        analysis = self.metz.get("cross_entity_coverage_analysis", {})
        meta = analysis.get("meta_coverage", {})
        volume = meta.get("volume", "").lower()
        assert "zero" in volume or "near-zero" in volume, \
            "Metz's Meta coverage should be near-zero"

    def test_lane_assignment_documented(self):
        """Both analyses together document the lane assignment mechanism."""
        metz_analysis = self.metz.get("cross_entity_coverage_analysis", {})
        isaac_analysis = self.isaac.get("cross_entity_coverage_analysis", {})
        metz_sig = metz_analysis.get("lane_assignment_significance", "")
        isaac_sig = isaac_analysis.get("cross_entity_significance", "")
        assert len(metz_sig) > 50 and len(isaac_sig) > 50, \
            "Both must have substantial significance analysis"


# ===================================================================
# Competitor Coverage Research — NYT Section
# ===================================================================

class TestNYTCompetitorResearch:
    """competitor-coverage-research.yaml has NYT cross-entity findings."""

    @classmethod
    def setup_class(cls):
        cls.research = _load_yaml("competitor-coverage-research.yaml")
        cls.nyt = cls.research.get("publications", {}).get("nytimes", {})

    def test_nyt_section_exists(self):
        assert self.nyt, "competitor-coverage-research must have nytimes section"

    def test_has_beat_assignment_analysis(self):
        assert "cross_entity_beat_assignment" in self.nyt, \
            "NYT section must have cross_entity_beat_assignment analysis"

    def test_beat_assignment_has_finding(self):
        ba = self.nyt.get("cross_entity_beat_assignment", {})
        finding = ba.get("finding", "")
        assert len(finding) > 100, \
            "Beat assignment finding must be substantive"

    def test_beat_assignment_mentions_metz_and_isaac(self):
        ba = self.nyt.get("cross_entity_beat_assignment", {})
        finding = ba.get("finding", "").lower()
        assert "metz" in finding and "isaac" in finding, \
            "Finding must reference both Metz and Isaac"

    def test_has_metz_openai_examples(self):
        ba = self.nyt.get("cross_entity_beat_assignment", {})
        examples = ba.get("metz_openai_examples", [])
        assert len(examples) >= 2, \
            "Must have at least 2 Metz OpenAI examples"

    def test_has_isaac_meta_examples(self):
        ba = self.nyt.get("cross_entity_beat_assignment", {})
        examples = ba.get("isaac_meta_examples", [])
        assert len(examples) >= 1, \
            "Must have at least 1 Isaac Meta example"

    def test_analytical_significance_present(self):
        ba = self.nyt.get("cross_entity_beat_assignment", {})
        sig = ba.get("analytical_significance", "")
        assert "structural" in sig.lower() or "institutional" in sig.lower(), \
            "Significance must identify structural/institutional mechanism"


# ===================================================================
# Cross-Publication Lane Comparison
# ===================================================================

class TestCrossPublicationLaneComparison:
    """Compare NYT lane assignment with WIRED and Verge patterns."""

    @classmethod
    def setup_class(cls):
        cls.nyt = _load_yaml("nytimes.yaml")
        cls.wired = _load_yaml("wired.yaml")
        cls.verge = _load_yaml("the-verge.yaml")

    def test_nyt_has_dedicated_meta_beat(self):
        """NYT maintains a dedicated Meta beat reporter position."""
        journalists = self.nyt.get("key_journalists", [])
        meta_reporters = [
            j for j in journalists
            if "meta" in j.get("beat", "").lower()
        ]
        assert len(meta_reporters) >= 1, \
            "NYT must have at least 1 dedicated Meta beat reporter"

    def test_nyt_no_dedicated_openai_beat(self):
        """NYT has no dedicated OpenAI beat reporter — covered as part of broader AI."""
        journalists = self.nyt.get("key_journalists", [])
        openai_reporters = [
            j for j in journalists
            if "openai" in j.get("beat", "").lower()
            and "meta" not in j.get("beat", "").lower()
        ]
        assert len(openai_reporters) == 0, \
            "NYT should NOT have a dedicated OpenAI-specific beat reporter"

    def test_three_mechanisms_documented(self):
        """The toolkit now documents three distinct lane assignment mechanisms."""
        # WIRED: editorial desk assignment (product vs investigative)
        wired_journalists = self.wired.get("key_journalists", [])
        has_wired_cross = any(
            "cross_entity" in str(j).lower()
            for j in wired_journalists
        )

        # The Verge: individual consistency (Song balanced), institutional adversarial (Heath)
        verge_journalists = self.verge.get("key_journalists", [])
        has_verge_cross = any(
            "competitor_coverage" in str(j).lower() or "cross_entity" in str(j).lower()
            for j in verge_journalists
        )

        # NYT: reporter assignment (Metz=progress, Isaac/Tan=adversarial)
        nyt_journalists = self.nyt.get("key_journalists", [])
        has_nyt_cross = any(
            "cross_entity_coverage_analysis" in j
            for j in nyt_journalists
        )

        assert has_nyt_cross, "NYT must have cross-entity analysis"
        # At least 2 of 3 publications should have cross-entity documentation
        documented = sum([has_wired_cross, has_verge_cross, has_nyt_cross])
        assert documented >= 2, \
            f"At least 2 publications should have cross-entity documentation, got {documented}"
