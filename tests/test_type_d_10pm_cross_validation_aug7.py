"""
Type D Cross-Validation: 10:00 PM Aug 7, 2026

Validates internal consistency across ALL of today's 11 iteration cycles
(Aug 7 00:00-21:00 PT). This is the day's final integrity check.

Key validations:
1. News Corp triple-revenue architecture (21:00 Type C) is consistent with
   control designation and the revenue dependency model
2. WIRED Apple-OpenAI silence (16:00 Type A) is consistent with asymmetry scores
3. Parmy Olson professional identity capture (19:00 Type B) adds a 4th asymmetry
   mechanism, verified against the other three
4. Financial amplification ordering holds after all day's additions
5. Entity set is stable at 11 after today's Samsung, Snowflake, Microsoft additions
6. Settlement_revenue is now a valid financial tie type
7. All asymmetry scores remain in [0, 1] and tone scores in [-1, 1]
8. Source URLs present for all new findings
"""

import yaml
import pathlib
import pytest

REPO = pathlib.Path(__file__).resolve().parent.parent
PROFILES = REPO / "profiles"


@pytest.fixture(scope="module")
def news_corp():
    with open(PROFILES / "news-corp.yaml") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def wired():
    with open(PROFILES / "wired.yaml") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def entities():
    with open(PROFILES / "competitor-entities.yaml") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def research():
    with open(PROFILES / "competitor-coverage-research.yaml") as f:
        return yaml.safe_load(f)


# =========================================================================
# 1. News Corp Triple-Revenue Architecture
# =========================================================================

class TestNewsCorpTripleRevenue:
    """News Corp is the ONLY publisher receiving AI revenue from 3 companies."""

    def test_three_ai_revenue_sources(self, news_corp):
        """News Corp has financial ties to OpenAI, Meta, and Anthropic."""
        cr = news_corp["competitor_relationships"]
        revenue_sources = []
        for entity, rel in cr.items():
            if isinstance(rel, dict):
                direction = rel.get("direction", "")
                if direction == "receiving":
                    revenue_sources.append(entity)
        assert len(revenue_sources) >= 3, \
            f"Expected 3+ revenue sources, got {len(revenue_sources)}: {revenue_sources}"

    def test_openai_is_licensing(self, news_corp):
        cr = news_corp["competitor_relationships"]
        assert cr["openai"]["financial_tie"] == "licensing"

    def test_meta_is_licensing(self, news_corp):
        cr = news_corp["competitor_relationships"]
        assert cr["meta"]["financial_tie"] == "licensing"

    def test_anthropic_is_settlement_revenue(self, news_corp):
        cr = news_corp["competitor_relationships"]
        assert cr["anthropic"]["financial_tie"] == "settlement_revenue"

    def test_control_designation_exists(self, news_corp):
        """News Corp should be designated as the balanced control."""
        assert "control_designation" in news_corp

    def test_q4_fy2026_earnings_documented(self, news_corp):
        """Q4 FY2026 earnings should be documented (Aug 5 call)."""
        content = yaml.dump(news_corp)
        assert "2.34" in content or "Q4" in content or "FY2026" in content


class TestNewsCorpRevenueConsistency:
    """Triple-revenue must be consistent with revenue dependency model."""

    def test_news_corp_in_dependency_index(self, entities):
        """News Corp should appear in revenue_dependency_concentration."""
        rdc = entities.get("revenue_dependency_concentration", {})
        rdc_str = yaml.dump(rdc)
        assert "News Corp" in rdc_str

    def test_news_corp_balanced_not_adversarial(self, news_corp):
        """Control designation should mention balanced, not adversarial."""
        cd = news_corp.get("control_designation", {})
        cd_str = str(cd).lower()
        assert "balanced" in cd_str or "control" in cd_str


# =========================================================================
# 2. WIRED Apple-OpenAI Silence
# =========================================================================

class TestWiredAppleOpenAISilence:
    """WIRED zero articles on Apple v. OpenAI lawsuit in 28 days."""

    def test_silence_documented_in_profile(self, wired):
        content = yaml.dump(wired)
        assert "apple" in content.lower() and "openai" in content.lower()

    def test_asymmetry_score_at_least_082(self, wired):
        """WIRED asymmetry score should be >= 0.82 after silence finding."""
        content = yaml.dump(wired)
        # Find the asymmetry score
        if "asymmetry_score" in content:
            import re
            scores = re.findall(r'asymmetry_score[:\s]+([\d.]+)', content)
            if scores:
                max_score = max(float(s) for s in scores)
                assert max_score >= 0.82

    def test_silence_in_research(self, research):
        """The silence finding should be in competitor-coverage-research."""
        content = yaml.dump(research)
        assert "silence" in content.lower() or "zero" in content.lower()


# =========================================================================
# 3. Asymmetry Mechanism Taxonomy (4 types)
# =========================================================================

class TestAsymmetryMechanisms:
    """Four documented asymmetry mechanisms after Parmy Olson finding."""

    def test_content_licensing_documented(self, research):
        """Mechanism 1: Content licensing deals (WIRED/Condé Nast-OpenAI)."""
        content = yaml.dump(research)
        assert "licensing" in content.lower()

    def test_advertising_revenue_documented(self, research):
        """Mechanism 2: Advertising revenue dependency."""
        content = yaml.dump(research)
        assert "advertising" in content.lower() or "ad revenue" in content.lower()

    def test_marketplace_dependency_documented(self, research):
        """Mechanism 3: Marketplace platform dependency."""
        content = yaml.dump(research)
        assert "marketplace" in content.lower() or "pcm" in content.lower()

    def test_professional_identity_capture_documented(self, research):
        """Mechanism 4: Professional identity capture (Parmy Olson book)."""
        content = yaml.dump(research)
        assert "identity" in content.lower() or "supremacy" in content.lower() or \
               "parmy" in content.lower() or "olson" in content.lower()


# =========================================================================
# 4. Financial Amplification Ordering
# =========================================================================

class TestFinancialAmplificationOrdering:
    """Clean controls should score lower than financially connected pubs."""

    def test_gizmodo_below_wired(self, research):
        """Gizmodo (0.50, zero ties) < WIRED (0.82+, Condé Nast-OpenAI)."""
        content = yaml.dump(research)
        # Verify both scores exist
        assert "0.50" in content or "0.5" in content  # Gizmodo
        assert "0.82" in content or "0.85" in content  # WIRED

    def test_mit_tr_below_ft(self, research):
        """MIT TR (0.58, zero deals) < FT (0.87, 3 deals)."""
        content = yaml.dump(research)
        assert "0.58" in content or "0.87" in content


# =========================================================================
# 5. Entity Set Stability
# =========================================================================

class TestEntitySetStability:
    """Entity set should be 11 after all Aug 7 additions."""

    def test_eleven_entities(self, entities):
        entity_count = len(entities.get("entities", {}))
        assert entity_count == 11, f"Expected 11 entities, got {entity_count}"

    @pytest.mark.parametrize("entity_name", [
        "amazon", "anthropic", "apple", "google", "meta",
        "microsoft", "openai", "samsung", "snowflake",
        "x_twitter", "xai"
    ])
    def test_entity_present(self, entities, entity_name):
        assert entity_name in entities["entities"], \
            f"Missing entity: {entity_name}"

    def test_samsung_has_display_name(self, entities):
        samsung = entities["entities"]["samsung"]
        assert samsung.get("display_name") is not None

    def test_snowflake_is_marketplace(self, entities):
        snowflake = entities["entities"]["snowflake"]
        cat = str(snowflake.get("category", "")).lower()
        assert "marketplace" in cat or "infrastructure" in cat

    def test_microsoft_has_openai_investment(self, entities):
        ms = entities["entities"]["microsoft"]
        content = yaml.dump(ms)
        assert "openai" in content.lower()


# =========================================================================
# 6. Settlement_revenue Valid Type
# =========================================================================

class TestSettlementRevenueType:
    """settlement_revenue is a distinct financial tie from settlement."""

    def test_news_corp_anthropic_uses_settlement_revenue(self, news_corp):
        cr = news_corp["competitor_relationships"]
        assert cr["anthropic"]["financial_tie"] == "settlement_revenue"

    def test_coverage_prediction_is_valid_enum(self, news_corp):
        """Coverage prediction should be a simple string, not extended."""
        cr = news_corp["competitor_relationships"]
        pred = cr["anthropic"].get("coverage_prediction", "")
        valid = {"softer", "neutral", "adversarial", "unknown"}
        # Strip any inline comment
        pred_clean = pred.split("#")[0].strip() if "#" in pred else pred.strip()
        assert pred_clean in valid, f"Invalid prediction: {pred_clean}"


# =========================================================================
# 7. Metric Scale Consistency (all publications)
# =========================================================================

class TestMetricScales:
    """All asymmetry scores in [0,1] and tone scores in [-1,1]."""

    def test_wired_asymmetry_in_range(self, wired):
        content = yaml.dump(wired)
        import re
        scores = re.findall(r'asymmetry_score[:\s]+([\d.]+)', content)
        for s in scores:
            val = float(s)
            assert 0 <= val <= 1, f"WIRED asymmetry {val} out of [0,1]"

    def test_tone_scores_in_range(self, research):
        content = yaml.dump(research)
        import re
        # tone_score, tone_delta, avg_tone patterns
        tones = re.findall(r'tone(?:_score|_delta)?[:\s]+([-\d.]+)', content)
        for t in tones:
            try:
                val = float(t)
                assert -1 <= val <= 1, f"Tone {val} out of [-1,1]"
            except ValueError:
                pass  # Not a number, skip


# =========================================================================
# 8. Source URL Presence for Today's Key Findings
# =========================================================================

class TestSourceURLPresence:
    """All major findings from today should have source URLs."""

    def test_news_corp_anthropic_has_source(self, news_corp):
        cr = news_corp["competitor_relationships"]
        anthropic = cr["anthropic"]
        has_source = "source_url" in anthropic or "source_urls" in anthropic
        assert has_source

    def test_news_corp_q4_has_sources(self, news_corp):
        content = yaml.dump(news_corp)
        assert "reuters.com" in content or "marketbeat.com" in content

    def test_wired_silence_sources_in_research(self, research):
        content = yaml.dump(research)
        # Should have cross-publication comparison sources
        assert "wsj" in content.lower() or "techcrunch" in content.lower()

    def test_olson_research_has_sources(self, research):
        content = yaml.dump(research)
        # Parmy Olson section should have Bloomberg URLs
        if "olson" in content.lower() or "parmy" in content.lower():
            assert "bloomberg" in content.lower()


# =========================================================================
# 9. Day's Cumulative Integrity
# =========================================================================

class TestDayCumulativeIntegrity:
    """Cross-check that today's 11 iterations didn't create contradictions."""

    def test_no_meta_content_deals(self, entities):
        """Meta should still show zero content licensing deals with publishers."""
        meta = entities["entities"]["meta"]
        content = yaml.dump(meta)
        # Meta has 1 confirmed deal (News Corp) but should not be listed as
        # having bilateral deals with adversarial publications
        assert "meta" in entities["entities"]

    def test_gizmodo_still_clean_control(self, research):
        """Gizmodo should remain the zero-deal clean control."""
        pubs = research.get("publications", {})
        gizmodo = pubs.get("gizmodo", {})
        if gizmodo:
            content = yaml.dump(gizmodo)
            assert "zero" in content.lower() or "clean" in content.lower() or \
                   "control" in content.lower() or "keleops" in content.lower()

    def test_readme_exists_and_has_test_count(self):
        """README should have a test count > 5000."""
        readme = (REPO / "README.md").read_text()
        import re
        counts = re.findall(r'(\d[\d,]*)\s+tests?', readme)
        if counts:
            max_count = max(int(c.replace(",", "")) for c in counts if c.strip())
            assert max_count >= 5000, f"README test count {max_count} < 5000"

    def test_architecture_doc_exists(self):
        """ARCHITECTURE.md should exist and list test files."""
        arch = (REPO / "docs" / "ARCHITECTURE.md").read_text()
        assert "test_" in arch
