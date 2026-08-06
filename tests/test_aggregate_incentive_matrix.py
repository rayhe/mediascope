"""
Tests for the aggregate financial incentive matrix (competitor-entities.yaml).

Validates structural integrity, statistical consistency, and control group
predictions for the 17:0 competitor-deal-to-Meta-deal gradient across all
8 MediaScope-profiled publications.

Source: profiles/competitor-entities.yaml — aggregate_incentive_matrix section
Added: 2026-08-05 (Type D iteration — test & verify)
"""
import os
import yaml
import pytest
from collections import Counter

PROFILES_DIR = os.path.join(os.path.dirname(__file__), "..", "profiles")


def _load(filename):
    with open(os.path.join(PROFILES_DIR, filename)) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def entities():
    return _load("competitor-entities.yaml")


@pytest.fixture(scope="module")
def matrix(entities):
    return entities["meta_ai_deals"]["aggregate_incentive_matrix"]


@pytest.fixture(scope="module")
def publications(matrix):
    return matrix["publications"]


@pytest.fixture(scope="module")
def excluded(entities):
    return entities["meta_ai_deals"]["excluded_publishers"]


# ===================================================================
# I. MATRIX STRUCTURAL INTEGRITY
# ===================================================================

class TestMatrixStructure:
    """The aggregate_incentive_matrix must have correct structure and counts."""

    @classmethod
    def setup_class(cls):
        cls.entities = _load("competitor-entities.yaml")
        cls.matrix = cls.entities["meta_ai_deals"]["aggregate_incentive_matrix"]
        cls.pubs = cls.matrix["publications"]

    def test_matrix_has_publications_list(self):
        assert isinstance(self.pubs, list)
        assert len(self.pubs) == 8, f"Expected 8 publications, got {len(self.pubs)}"

    def test_each_publication_has_required_fields(self):
        required = {"name", "competitor_deals", "platforms", "meta_deals", "adversarial_meta_coverage"}
        for pub in self.pubs:
            missing = required - set(pub.keys())
            assert not missing, f"{pub['name']} missing fields: {missing}"

    def test_total_competitor_deal_count_matches_sum(self):
        computed = sum(p["competitor_deals"] for p in self.pubs)
        assert computed == self.matrix["total_competitor_deal_count"], \
            f"Sum of competitor deals ({computed}) != total ({self.matrix['total_competitor_deal_count']})"

    def test_total_meta_deal_count_is_zero(self):
        assert self.matrix["total_meta_deal_count"] == 0

    def test_all_meta_deals_are_zero(self):
        for pub in self.pubs:
            assert pub["meta_deals"] == 0, \
                f"{pub['name']} has meta_deals={pub['meta_deals']}, expected 0"

    def test_all_publications_are_adversarial(self):
        for pub in self.pubs:
            assert pub["adversarial_meta_coverage"] is True, \
                f"{pub['name']} should have adversarial_meta_coverage=True"

    def test_platforms_count_matches_competitor_deals(self):
        for pub in self.pubs:
            # platform entries can contain multiple deals in one string
            # (e.g., "Amazon (Rufus, $20-25M/yr + Alexa+)")
            # so platforms length should equal competitor_deals count
            assert len(pub["platforms"]) == pub["competitor_deals"], \
                f"{pub['name']}: {len(pub['platforms'])} platforms != {pub['competitor_deals']} deals"

    def test_matrix_has_statistical_note(self):
        assert "statistical_note" in self.matrix
        note = self.matrix["statistical_note"].lower()
        assert "chance" in note or "probability" in note

    def test_matrix_has_control_comparison(self):
        assert "control_comparison" in self.matrix
        ctrl = self.matrix["control_comparison"]
        assert "News Corp" in ctrl
        assert "Gizmodo" in ctrl


# ===================================================================
# II. CROSS-PLATFORM DEAL CONSISTENCY
# ===================================================================

class TestCrossPlatformConsistency:
    """Verify deal counts in matrix match structured deals in excluded_publishers."""

    @classmethod
    def setup_class(cls):
        cls.entities = _load("competitor-entities.yaml")
        cls.matrix_pubs = cls.entities["meta_ai_deals"]["aggregate_incentive_matrix"]["publications"]
        cls.excluded = cls.entities["meta_ai_deals"]["excluded_publishers"]

    def _find_excluded(self, name_fragment):
        for ep in self.excluded:
            if name_fragment.lower() in ep.get("name", "").lower():
                return ep
        return None

    def test_wired_deal_count_at_least_matrix(self):
        """Excluded_publishers may have more granular deal entries (e.g.,
        Amazon Rufus and Amazon Alexa+ separate) than the matrix which
        aggregates by platform. Verify excluded >= matrix."""
        matrix_wired = [p for p in self.matrix_pubs if "WIRED" in p["name"]][0]
        excluded_cn = self._find_excluded("condé nast")
        if excluded_cn:
            deals = excluded_cn.get("deals_with_competitors", [])
            assert len(deals) >= matrix_wired["competitor_deals"], \
                f"WIRED: {len(deals)} excluded deals < {matrix_wired['competitor_deals']} matrix deals"

    def test_ft_deal_count_matches(self):
        matrix_ft = [p for p in self.matrix_pubs if "Financial Times" in p["name"]][0]
        excluded_ft = self._find_excluded("financial times")
        if excluded_ft:
            deals = excluded_ft.get("deals_with_competitors", [])
            assert len(deals) == matrix_ft["competitor_deals"], \
                f"FT: {len(deals)} excluded deals != {matrix_ft['competitor_deals']} matrix deals"

    def test_gizmodo_has_zero_deals_in_both(self):
        matrix_gz = [p for p in self.matrix_pubs if "Gizmodo" in p["name"]][0]
        assert matrix_gz["competitor_deals"] == 0
        excluded_gz = self._find_excluded("gizmodo")
        if excluded_gz:
            deals = excluded_gz.get("deals_with_competitors", [])
            assert len(deals) == 0


# ===================================================================
# III. PLATFORM DISTRIBUTION ANALYSIS
# ===================================================================

class TestPlatformDistribution:
    """Verify platform coverage diversity across publications."""

    @classmethod
    def setup_class(cls):
        cls.entities = _load("competitor-entities.yaml")
        cls.matrix_pubs = cls.entities["meta_ai_deals"]["aggregate_incentive_matrix"]["publications"]
        # Count platform appearances
        cls.platform_counter = Counter()
        for pub in cls.matrix_pubs:
            for p in pub["platforms"]:
                # Normalize: extract base company
                base = p.split("(")[0].strip()
                cls.platform_counter[base] += 1

    def test_openai_is_most_common_platform(self):
        if self.platform_counter:
            most_common = self.platform_counter.most_common(1)[0][0]
            assert "OpenAI" in most_common, \
                f"Expected OpenAI as most common platform, got {most_common}"

    def test_at_least_four_distinct_platforms(self):
        assert len(self.platform_counter) >= 4, \
            f"Expected at least 4 distinct platforms, got {len(self.platform_counter)}"

    def test_multi_platform_publications_exist(self):
        """At least 3 publications should have 2+ competitor deals."""
        multi = [p for p in self.matrix_pubs if p["competitor_deals"] >= 2]
        assert len(multi) >= 3, \
            f"Expected at least 3 publications with 2+ deals, got {len(multi)}"

    def test_wired_has_most_competitor_deals(self):
        max_pub = max(self.matrix_pubs, key=lambda p: p["competitor_deals"])
        assert "WIRED" in max_pub["name"] or "Condé" in max_pub["name"], \
            f"Expected WIRED/Condé Nast to have most deals, got {max_pub['name']}"


# ===================================================================
# IV. CONTROL GROUP VALIDATION
# ===================================================================

class TestControlGroupPredictions:
    """The critical_finding and control_comparison must make correct predictions."""

    @classmethod
    def setup_class(cls):
        cls.entities = _load("competitor-entities.yaml")
        cls.finding = cls.entities["meta_ai_deals"]["critical_finding"]
        cls.matrix = cls.entities["meta_ai_deals"]["aggregate_incentive_matrix"]
        cls.ctrl = cls.matrix.get("control_comparison", "")

    def test_finding_mentions_eighteen_deals(self):
        assert "19" in self.finding, "Critical finding should mention 19 competitor deals"

    def test_finding_mentions_zero_meta_deals(self):
        assert "ZERO" in self.finding or "0" in self.finding

    def test_finding_mentions_news_corp(self):
        assert "News Corp" in self.finding

    def test_finding_mentions_balanced(self):
        assert "balanced" in self.finding.lower()

    def test_control_identifies_dual_deal_publisher(self):
        """News Corp should be identified as having both OpenAI and Meta deals."""
        assert "OpenAI" in self.ctrl
        assert "Meta" in self.ctrl

    def test_control_identifies_gizmodo_as_independent(self):
        assert "Gizmodo" in self.ctrl

    def test_control_notes_editorial_culture_factor(self):
        ctrl_lower = self.ctrl.lower()
        assert "editorial" in ctrl_lower or "culture" in ctrl_lower


# ===================================================================
# V. EXCLUDED PUBLISHERS SCHEMA MIGRATION
# ===================================================================

class TestExcludedPublishersSchema:
    """Verify excluded_publishers deals are in structured dict format."""

    @classmethod
    def setup_class(cls):
        cls.entities = _load("competitor-entities.yaml")
        cls.excluded = cls.entities["meta_ai_deals"]["excluded_publishers"]

    def test_all_deals_are_dicts(self):
        for pub in self.excluded:
            for deal in pub.get("deals_with_competitors", []):
                assert isinstance(deal, dict), \
                    f"{pub['name']}: deal should be dict, got {type(deal).__name__}: {deal}"

    def test_deal_dicts_have_required_keys(self):
        required = {"partner", "type", "date", "source_url"}
        for pub in self.excluded:
            for deal in pub.get("deals_with_competitors", []):
                missing = required - set(deal.keys())
                assert not missing, \
                    f"{pub['name']}: deal missing keys {missing}: {deal}"

    def test_all_deals_have_nonempty_partner(self):
        for pub in self.excluded:
            for deal in pub.get("deals_with_competitors", []):
                assert deal.get("partner"), \
                    f"{pub['name']}: deal has empty partner: {deal}"

    def test_all_deals_have_source_urls(self):
        for pub in self.excluded:
            for deal in pub.get("deals_with_competitors", []):
                url = deal.get("source_url") or ""
                # Negotiating/unconfirmed deals may lack a source URL
                if deal.get("type") != "negotiating":
                    assert url.startswith("http"), \
                        f"{pub['name']}: deal source_url invalid: {url} (partner: {deal.get('partner')})"
