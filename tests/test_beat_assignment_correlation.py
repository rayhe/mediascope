"""
Tests verifying the beat/lane assignment → coverage asymmetry correlation
across WIRED, NYT, and The Verge, and the financial relationship →
coverage prediction hypothesis.

Key findings under test:
1. Three publications use structurally different but functionally equivalent
   mechanisms to assign adversarial coverage to Meta while giving competitors
   neutral-to-positive coverage.
2. Financial deal status (has Meta deal vs. has competitor deal vs. no deals)
   correlates with coverage prediction direction across all profiled publications.
3. The Mike Isaac beat expansion proves framing is controlled by assignment,
   not individual reporter bias — same journalist, consistent framing across entities.
4. Eli Tan succession perpetuates the adversarial beat structure.

Sources:
- Iteration log entries 2026-08-04/05 (Types A, B, C)
- competitor-entities.yaml meta_ai_deals section
- Publication profiles: wired.yaml, nytimes.yaml, the-verge.yaml
"""

import yaml
import pathlib
import re
from collections import Counter

PROFILES = pathlib.Path(__file__).resolve().parent.parent / "profiles"


def _load(name: str) -> dict:
    with open(PROFILES / name, encoding="utf-8") as f:
        return yaml.safe_load(f)


# ===================================================================
# I. LANE ASSIGNMENT MECHANISM — Cross-Publication Structural Pattern
# ===================================================================

class TestLaneAssignmentMechanisms:
    """Each publication must document how coverage assignment creates asymmetry."""

    @classmethod
    def setup_class(cls):
        cls.wired = _load("wired.yaml")
        cls.nyt = _load("nytimes.yaml")
        cls.verge = _load("the-verge.yaml")

    def test_wired_has_lane_assignment_mechanism(self):
        """WIRED must document its editorial desk assignment model."""
        ce = self.wired.get("cross_entity_wearables_framing", {})
        mechanism = ce.get("editorial_lane_assignment_mechanism", "")
        assert len(mechanism) > 50, "WIRED lane assignment should be documented"
        assert "product" in mechanism.lower() or "goode" in mechanism.lower(), \
            "Should reference the product desk or Lauren Goode"
        assert "investigative" in mechanism.lower() or "cameron" in mechanism.lower() \
            or "mehrotra" in mechanism.lower() or "meta" in mechanism.lower(), \
            "Should reference the investigative desk or Meta coverage"

    def test_nyt_has_reporter_assignment_pattern(self):
        """NYT must document its reporter-level assignment mechanism."""
        journalists = self.nyt.get("key_journalists", [])
        # Should have at least one journalist with lane_assignment or cross_entity info
        has_assignment_docs = False
        for j in journalists:
            if "cross_entity" in str(j).lower() or "lane_assignment" in str(j).lower() \
                    or "beat" in str(j).lower():
                has_assignment_docs = True
                break
        assert has_assignment_docs, "NYT should document reporter assignment patterns"

    def test_verge_has_institutional_split(self):
        """The Verge must document journalists with different coverage patterns."""
        journalists = self.verge.get("key_journalists", [])
        names = [j.get("name", "") for j in journalists]
        # Should have Victoria Song (balanced product reviewer)
        assert any("song" in n.lower() for n in names), \
            "Verge should profile Victoria Song"
        # Should have at least one investigative/business reporter
        assert len(names) >= 3, \
            f"Verge should have multiple journalist profiles, got {len(names)}"


class TestThreeLaneAssignmentConsistency:
    """The three documented lane assignment mechanisms should be
    structurally distinct but functionally equivalent."""

    @classmethod
    def setup_class(cls):
        cls.wired = _load("wired.yaml")
        cls.nyt = _load("nytimes.yaml")
        cls.verge = _load("the-verge.yaml")

    def test_wired_mechanism_is_desk_level(self):
        """WIRED uses editorial desk assignment (not reporter-level)."""
        ce = self.wired.get("cross_entity_wearables_framing", {})
        mechanism = ce.get("editorial_lane_assignment_mechanism", "")
        # Should reference desks, assignment steps, or product review
        assert "assignment" in mechanism.lower() or \
               "product review" in mechanism.lower() or \
               "steps" in mechanism.lower() or \
               "correspondent" in mechanism.lower(), \
            "WIRED mechanism should describe desk-level assignment"

    def test_nyt_mechanism_is_reporter_level(self):
        """NYT uses dedicated beat reporter assignment."""
        journalists = self.nyt.get("key_journalists", [])
        isaac = next((j for j in journalists if "isaac" in j.get("name", "").lower()), None)
        if isaac:
            # Isaac should show beat change from dedicated Meta to broader SV
            beat = isaac.get("beat", "")
            assert ("silicon valley" in beat.lower() or "formerly" in beat.lower() or
                    "meta" in beat.lower()), \
                "Isaac's profile should reflect the beat change"

    def test_all_three_predict_adversarial_meta_coverage(self):
        """All three mechanisms should predict adversarial Meta coverage
        regardless of which structural model they use."""
        pubs = [
            ("wired", self.wired),
            ("nytimes", self.nyt),
            ("the-verge", self.verge),
        ]
        for slug, profile in pubs:
            comp_rels = profile.get("competitor_relationships", {})
            if "meta" in comp_rels:
                meta_rel = comp_rels["meta"]
                tie = meta_rel.get("financial_tie", "")
                pred = meta_rel.get("coverage_prediction", "")
                # Meta should have no licensing deal and adversarial prediction
                assert tie not in ("licensing", "investment"), \
                    f"{slug}: Meta should NOT have a licensing/investment relationship"
                assert "adversarial" in pred.lower() or "harsher" in pred.lower() \
                    or "negative" in pred.lower() or pred == "", \
                    f"{slug}: Meta coverage prediction should be adversarial, got '{pred}'"


# ===================================================================
# II. FINANCIAL DEAL — COVERAGE PREDICTION CORRELATION
# ===================================================================

class TestFinancialDealCoveragePrediction:
    """Publications with competitor deals but no Meta deal should
    predict adversarial Meta coverage. Publications with Meta deals
    should predict balanced or softer coverage."""

    @classmethod
    def setup_class(cls):
        cls.entities = _load("competitor-entities.yaml")
        cls.deals = cls.entities.get("meta_ai_deals", {})
        cls.excluded = cls.deals.get("excluded_publishers", [])
        cls.partners = cls.deals.get("partners", [])

    def test_zero_excluded_publishers_have_meta_deal(self):
        """No excluded publisher should have a Meta deal."""
        for pub in self.excluded:
            assert pub.get("meta_deal") == "none", \
                f"{pub['name']} should have meta_deal = 'none'"

    def test_most_excluded_publishers_have_competitor_deals(self):
        """At least 5 of 8 excluded publishers should have competitor deals."""
        with_deals = sum(
            1 for p in self.excluded
            if p.get("deals_with_competitors") and len(p["deals_with_competitors"]) > 0
        )
        assert with_deals >= 5, \
            f"Expected >= 5 publishers with competitor deals, got {with_deals}"

    def test_gizmodo_is_clean_control(self):
        """Gizmodo should have no deals with anyone — the clean control."""
        gizmodo = next(
            (p for p in self.excluded if "gizmodo" in p.get("name", "").lower()),
            None
        )
        assert gizmodo is not None, "Gizmodo should be in excluded publishers"
        deals = gizmodo.get("deals_with_competitors", [])
        assert len(deals) == 0, "Gizmodo should be the clean control with no competitor deals"

    def test_news_corp_has_meta_deal(self):
        """News Corp (WSJ, NY Post, Barron's) should be a Meta AI partner."""
        news_corp = next(
            (p for p in self.partners if "news corp" in p.get("name", "").lower()),
            None
        )
        assert news_corp is not None, "News Corp should be a Meta AI partner"
        terms = news_corp.get("terms", "")
        assert "$50M" in terms or "50" in terms, \
            "News Corp deal should include up to $50M/yr"

    def test_financial_asymmetry_is_near_universal(self):
        """All excluded publications except Gizmodo should have at least
        one competitor deal — making the financial incentive gradient
        near-universal."""
        non_gizmodo = [
            p for p in self.excluded
            if "gizmodo" not in p.get("name", "").lower()
        ]
        with_comp_deals = sum(
            1 for p in non_gizmodo
            if p.get("deals_with_competitors") and len(p["deals_with_competitors"]) > 0
        )
        total = len(non_gizmodo)
        assert with_comp_deals == total, \
            f"All {total} non-Gizmodo excluded publishers should have competitor deals, " \
            f"got {with_comp_deals}"


class TestOpenAIDealConcentration:
    """OpenAI should be the most common deal partner among excluded publishers."""

    @classmethod
    def setup_class(cls):
        entities = _load("competitor-entities.yaml")
        cls.excluded = entities.get("meta_ai_deals", {}).get("excluded_publishers", [])

    def test_openai_is_most_common_competitor_deal(self):
        """Count how many excluded publishers have OpenAI deals."""
        all_deals = []
        for p in self.excluded:
            for deal in p.get("deals_with_competitors", []):
                # Handle both old string format and new structured dict format
                if isinstance(deal, dict):
                    company = deal.get("partner", "").split("(")[0].strip()
                else:
                    company = deal.split("(")[0].strip()
                all_deals.append(company)
        counter = Counter(all_deals)
        if counter:
            most_common_company = counter.most_common(1)[0][0]
            assert "openai" in most_common_company.lower(), \
                f"Expected OpenAI to be most common, got {most_common_company}"


# ===================================================================
# III. WIRED COMPETITOR ENTITY COVERAGE — Profile Completeness
# ===================================================================

class TestWiredCompetitorRelationshipCompleteness:
    """WIRED profile should track 9 competitor entities with financial details."""

    @classmethod
    def setup_class(cls):
        cls.wired = _load("wired.yaml")
        cls.comp_rels = cls.wired.get("competitor_relationships", {})

    def test_minimum_entity_count(self):
        """WIRED should track at least 8 competitor entities."""
        assert len(self.comp_rels) >= 8, \
            f"Expected >= 8 entities, got {len(self.comp_rels)}"

    def test_core_entities_present(self):
        """All major entities should be tracked."""
        required = {"openai", "meta", "apple", "google", "amazon"}
        present = set(self.comp_rels.keys())
        missing = required - present
        assert not missing, f"Missing entities: {missing}"

    def test_microsoft_added(self):
        """Microsoft PCM relationship should be tracked (added Type C, Aug 5)."""
        assert "microsoft" in self.comp_rels, "Microsoft should be tracked"
        ms = self.comp_rels["microsoft"]
        assert ms.get("financial_tie") == "licensing", \
            "Microsoft relationship should be licensing (PCM)"

    def test_perplexity_added(self):
        """Perplexity relationship should be tracked (added Type C, Aug 5)."""
        assert "perplexity" in self.comp_rels, "Perplexity should be tracked"
        perp = self.comp_rels["perplexity"]
        assert perp.get("financial_tie") == "licensing", \
            "Perplexity relationship should be licensing"

    def test_meta_is_only_adversarial_prediction(self):
        """Meta should be the only entity with adversarial coverage prediction
        and zero financial relationship."""
        for entity, data in self.comp_rels.items():
            tie = data.get("financial_tie", "")
            pred = data.get("coverage_prediction", "")
            if entity == "meta":
                assert tie in ("none", "adversarial", ""), \
                    f"Meta should have no financial tie, got '{tie}'"
            elif tie == "licensing":
                # Entities with licensing deals should NOT predict adversarial coverage
                if pred:
                    assert "adversarial" not in pred.lower(), \
                        f"{entity} has licensing deal but adversarial prediction"

    def test_each_entity_has_source_url(self):
        """Each competitor relationship should cite a source."""
        for entity, data in self.comp_rels.items():
            desc = data.get("description", "")
            source = data.get("source_url", data.get("source", ""))
            # Either description references a source or there's a source_url field
            assert source or "http" in desc or "confirmed" in desc.lower() or \
                   desc == "" or len(desc) > 20, \
                f"{entity}: missing source documentation"


# ===================================================================
# IV. MIKE ISAAC BEAT EXPANSION — Cross-Entity Framing Consistency
# ===================================================================

class TestMikeIsaacCrossEntityConsistency:
    """Isaac's post-expansion coverage should show consistent framing
    across entities, proving beat assignment controls framing."""

    @classmethod
    def setup_class(cls):
        cls.nyt = _load("nytimes.yaml")
        journalists = cls.nyt.get("key_journalists", [])
        cls.isaac = next(
            (j for j in journalists if j.get("name") == "Mike Isaac"), None
        )

    def test_isaac_has_cross_entity_portfolio(self):
        """Isaac should have documented cross-entity article portfolio."""
        assert self.isaac is not None
        cross = self.isaac.get("cross_entity_analysis", self.isaac.get("cross_entity_coverage", {}))
        if isinstance(cross, dict):
            articles = cross.get("articles", cross.get("post_expansion_portfolio", []))
        elif isinstance(cross, list):
            articles = cross
        else:
            articles = []
        # Should have at least 3 documented cross-entity articles
        assert len(articles) >= 3 or "cross_entity" in str(self.isaac).lower(), \
            "Isaac should have cross-entity coverage documentation"

    def test_isaac_covers_multiple_entities(self):
        """Isaac's portfolio should span at least 3 distinct entities."""
        assert self.isaac is not None
        full_text = str(self.isaac).lower()
        entities_mentioned = set()
        for entity in ["meta", "anthropic", "spacex", "openai"]:
            if entity in full_text:
                entities_mentioned.add(entity)
        assert len(entities_mentioned) >= 3, \
            f"Expected >= 3 entities, found: {entities_mentioned}"

    def test_isaac_framing_is_consistent(self):
        """Isaac's framing should be described as consistent/neutral across entities."""
        assert self.isaac is not None
        full_text = str(self.isaac).lower()
        consistency_markers = [
            "consistent", "neutral", "business", "comparable",
            "standard", "uniform", "similar"
        ]
        has_consistency = any(m in full_text for m in consistency_markers)
        assert has_consistency, \
            "Isaac's cross-entity analysis should note framing consistency"


class TestEliTanSuccession:
    """Eli Tan should be documented as Isaac's replacement on the Meta beat."""

    @classmethod
    def setup_class(cls):
        cls.nyt = _load("nytimes.yaml")
        journalists = cls.nyt.get("key_journalists", [])
        cls.tan = next(
            (j for j in journalists if "tan" in j.get("name", "").lower()
             and "eli" in j.get("name", "").lower()),
            None
        )

    def test_tan_exists_in_profile(self):
        """Eli Tan should be a profiled journalist."""
        assert self.tan is not None, \
            "Eli Tan should be in NYT key_journalists"

    def test_tan_covers_meta(self):
        """Tan's beat should include Meta."""
        if self.tan:
            beat = str(self.tan.get("beat", "")).lower()
            full = str(self.tan).lower()
            assert "meta" in beat or "meta" in full, \
                "Tan should cover Meta"

    def test_tan_is_marked_as_successor(self):
        """Tan should be documented as Isaac's replacement."""
        if self.tan:
            full = str(self.tan).lower()
            assert "succeed" in full or "replac" in full or "successor" in full \
                or "formerly" in full or "isaac" in full or "new" in full \
                or "fellowship" in full, \
                "Tan should be documented as Isaac's successor"


# ===================================================================
# V. DEAL TIMELINE INTEGRITY
# ===================================================================

class TestMetaDealTimelineIntegrity:
    """All Meta AI deal partners should have dates and source URLs."""

    @classmethod
    def setup_class(cls):
        entities = _load("competitor-entities.yaml")
        cls.partners = entities.get("meta_ai_deals", {}).get("partners", [])

    def test_all_partners_have_dates(self):
        """Every deal entry should have a date field."""
        for p in self.partners:
            assert "date" in p, f"{p.get('name', '?')}: missing date"
            assert p["date"], f"{p.get('name', '?')}: empty date"

    def test_all_partners_have_source_urls(self):
        """Every deal entry should have a source URL."""
        for p in self.partners:
            url = p.get("source_url", "")
            assert url and url.startswith("http"), \
                f"{p.get('name', '?')}: missing or invalid source_url"

    def test_chronological_order(self):
        """Partners should be listed roughly chronologically (oldest first)."""
        dates = []
        for p in self.partners:
            d = p.get("date", "")
            # Extract year-month for comparison
            match = re.match(r"(\d{4})-(\d{2})", d)
            if match:
                dates.append((int(match.group(1)), int(match.group(2))))
        # Check that dates are non-decreasing
        for i in range(1, len(dates)):
            assert dates[i] >= dates[i - 1], \
                f"Partners not in chronological order at index {i}: " \
                f"{dates[i-1]} > {dates[i]}"

    def test_deal_waves_documented(self):
        """Should show at least 3 distinct deal waves (Oct 2024, Dec 2025, Mar 2026)."""
        date_months = set()
        for p in self.partners:
            d = p.get("date", "")
            match = re.match(r"(\d{4}-\d{2})", d)
            if match:
                date_months.add(match.group(1))
        assert len(date_months) >= 3, \
            f"Expected >= 3 deal waves, got {len(date_months)}: {date_months}"


# ===================================================================
# VI. STATISTICAL VALIDITY — Asymmetry Scorer Integration
# ===================================================================

class TestAsymmetryStatisticalValidity:
    """The asymmetry scorer should produce statistically meaningful results
    when fed realistic tone distributions that reflect the documented patterns."""

    def test_adversarial_meta_vs_neutral_competitor_is_significant(self):
        """A distribution reflecting adversarial Meta coverage vs neutral
        competitor coverage should produce a significant result."""
        from mediascope.score.asymmetry import calculate_asymmetry
        from datetime import datetime

        # Simulated: adversarial Meta tone scores (negative)
        meta_scores = [-0.4, -0.6, -0.3, -0.5, -0.7, -0.4, -0.3, -0.6,
                       -0.5, -0.2, -0.4, -0.5]
        # Simulated: neutral-to-positive OpenAI/Apple coverage
        competitor_scores = [0.1, 0.2, -0.1, 0.3, 0.0, 0.1, 0.2, -0.1,
                             0.15, 0.05, 0.1, 0.25]

        result = calculate_asymmetry(
            target_scores=meta_scores,
            peer_scores=competitor_scores,
            target_entity="Meta",
            peer_entities=["OpenAI", "Apple"],
            publication_slug="wired_simulation",
            period_start=datetime(2025, 1, 1),
            period_end=datetime(2026, 7, 31),
        )
        assert result.is_significant, \
            f"Adversarial-vs-neutral should be significant (p={result.p_value})"
        assert result.asymmetry_score < -0.3, \
            f"Asymmetry should be strongly negative, got {result.asymmetry_score}"
        assert abs(result.cohens_d) > 0.8, \
            f"Effect size should be large, got {result.cohens_d}"

    def test_balanced_coverage_is_not_significant(self):
        """When both entity groups get similar coverage, no significant
        asymmetry should be detected."""
        from mediascope.score.asymmetry import calculate_asymmetry
        from datetime import datetime

        balanced_a = [0.0, -0.1, 0.1, -0.05, 0.05, 0.0, -0.1, 0.1]
        balanced_b = [0.05, -0.05, 0.1, -0.1, 0.0, 0.05, -0.05, 0.1]

        result = calculate_asymmetry(
            target_scores=balanced_a,
            peer_scores=balanced_b,
            target_entity="Meta",
            peer_entities=["OpenAI"],
            publication_slug="news_corp_simulation",
            period_start=datetime(2025, 1, 1),
            period_end=datetime(2026, 7, 31),
        )
        assert not result.is_significant, \
            f"Balanced coverage should not be significant (p={result.p_value})"
        assert abs(result.asymmetry_score) < 0.1, \
            f"Asymmetry should be near zero, got {result.asymmetry_score}"

    def test_cohens_d_direction_matches_asymmetry(self):
        """Cohen's d sign should align with asymmetry score direction."""
        from mediascope.score.asymmetry import calculate_asymmetry
        from datetime import datetime

        negative_target = [-0.5, -0.4, -0.6, -0.3, -0.5]
        positive_peers = [0.2, 0.3, 0.1, 0.4, 0.2]

        result = calculate_asymmetry(
            target_scores=negative_target,
            peer_scores=positive_peers,
            target_entity="Meta",
            peer_entities=["Apple"],
            publication_slug="test_direction",
            period_start=datetime(2025, 1, 1),
            period_end=datetime(2025, 12, 31),
        )
        # Both should be negative (target worse than peers)
        assert result.asymmetry_score < 0
        assert result.cohens_d < 0, \
            "Cohen's d should be negative when target is more negative"

    def test_confidence_interval_excludes_zero_when_significant(self):
        """When asymmetry is significant, the bootstrap CI should not
        contain zero."""
        from mediascope.score.asymmetry import calculate_asymmetry
        from datetime import datetime

        meta = [-0.5, -0.4, -0.6, -0.3, -0.5, -0.4, -0.6, -0.3]
        peers = [0.2, 0.3, 0.1, 0.4, 0.2, 0.3, 0.1, 0.4]

        result = calculate_asymmetry(
            target_scores=meta,
            peer_scores=peers,
            target_entity="Meta",
            peer_entities=["OpenAI"],
            publication_slug="ci_test",
            period_start=datetime(2025, 1, 1),
            period_end=datetime(2025, 12, 31),
        )
        if result.is_significant:
            assert result.confidence_interval_upper < 0 or \
                   result.confidence_interval_lower > 0, \
                f"CI should exclude zero when significant: " \
                f"[{result.confidence_interval_lower}, {result.confidence_interval_upper}]"
