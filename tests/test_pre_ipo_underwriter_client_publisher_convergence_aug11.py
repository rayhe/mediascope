"""
Test: Pre-IPO Underwriter-Client-Publisher Financial Convergence (Mechanism #46)

Finding: Anthropic's three lead IPO underwriters (Goldman Sachs, Morgan Stanley, JPMorgan Chase)
are simultaneously (a) underwriting Anthropic's ~$1T IPO (October 2026 target), (b) enterprise
Claude customers with embedded Anthropic engineers, and (c) major advertisers in financial
publications that set narrative framing for tech coverage. This triple overlap creates a
coverage incentive pipeline where the banks' institutional interests align with positive
Anthropic coverage at every layer. The timing coincides with the SEC's December 2025 termination
of the Global Research Analyst Settlement (GRAS), which had mandated structural separation of
research and investment banking since 2003.

Meta comparison: Meta IPO'd in 2012 — no bank has current IPO fee incentive for favorable
coverage. Meta has zero enterprise AI products embedded in any lead underwriter's operations.
Meta's DCEI (Dual-Channel Entanglement Index) with these three banks is zero.

Sources:
- Bloomberg/BGOV: "Anthropic Said to Pick Morgan Stanley, Goldman Sachs to Lead IPO" (Jun 2026)
- Reuters: "Goldman Sachs teams up with Anthropic to automate banking tasks" (Feb 2026)
- WebProNews: "Morgan Stanley's Bold AI Software Bet: Why Claude..." (Feb 2026)
- LinkedIn/Desai: "Claude at JPMorgan Chase: An Enterprise AI Deployment Case Study" (Jul 2026)
- WSJ: "The IPO Onslaught Is Forcing Bankers to Pick Teams" (Jun 2026)
- SEC: Statement on Global Research Analyst Settlement termination (Dec 2025)
- FINRA: "Time to Move On: The SEC Was Right to Retire the GRAS" (Jan 2026)
- Motley Fool: SpaceX IPO fees ~$500M, Goldman+MS ~$100M each (Jun 2026)
- MarketWatch: SpaceX IPO underwriter fee structure (Jun 2026)
- SEC: 2001 Testimony on analyst conflicts (Jul 2001)
- Qian, Shao & Liao: "Pre-IPO hype by affiliated analysts" (J. Corp. Finance, 2024)
"""

import os
import yaml
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")


def load_competitor_coverage():
    path = os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")
    with open(path) as f:
        return yaml.safe_load(f)


def load_competitor_entities():
    path = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
    with open(path) as f:
        return yaml.safe_load(f)


# ─── Test Class 1: Mechanism #46 Exists and Is Correctly Placed ───

class TestMechanism46Exists:
    """Verify mechanism #46 is in cross_publication_findings, not publications."""

    def setup_method(self):
        self.data = load_competitor_coverage()
        self.cpf = self.data.get("cross_publication_findings", {})
        self.pubs = self.data.get("publications", {})

    def test_mechanism_46_in_cross_pub_findings(self):
        found = any(
            v.get("mechanism_id") == 46
            for v in self.cpf.values()
            if isinstance(v, dict)
        )
        assert found, "Mechanism #46 should be in cross_publication_findings"

    def test_mechanism_46_not_in_publications(self):
        found = any(
            v.get("mechanism_id") == 46
            for v in self.pubs.values()
            if isinstance(v, dict)
        )
        assert not found, "Mechanism #46 should NOT be in publications section"

    def test_mechanism_46_has_finding_summary(self):
        for v in self.cpf.values():
            if isinstance(v, dict) and v.get("mechanism_id") == 46:
                assert "finding_summary" in v
                assert len(v["finding_summary"]) > 100
                return
        pytest.fail("Could not find mechanism #46 with finding_summary")

    def test_mechanism_46_has_source_urls(self):
        for v in self.cpf.values():
            if isinstance(v, dict) and v.get("mechanism_id") == 46:
                urls = v.get("source_urls", [])
                assert len(urls) >= 5, f"Expected >=5 source URLs, got {len(urls)}"
                return
        pytest.fail("Could not find mechanism #46 with source_urls")

    def test_mechanism_46_has_test_file(self):
        for v in self.cpf.values():
            if isinstance(v, dict) and v.get("mechanism_id") == 46:
                tf = v.get("test_file", "")
                assert tf, "mechanism #46 must have a test_file reference"
                assert os.path.exists(os.path.join(REPO_ROOT, tf)), \
                    f"Test file {tf} must exist on disk"
                return
        pytest.fail("Could not find mechanism #46")


# ─── Test Class 2: Underwriter Triple Overlap Structure ───

class TestUnderwriterTripleOverlap:
    """The three banks (GS, MS, JPM) each have three simultaneous Anthropic roles."""

    def setup_method(self):
        self.data = load_competitor_coverage()
        self.cpf = self.data.get("cross_publication_findings", {})
        self.mech = None
        for v in self.cpf.values():
            if isinstance(v, dict) and v.get("mechanism_id") == 46:
                self.mech = v
                break

    def test_mechanism_found(self):
        assert self.mech is not None, "Mechanism #46 must exist"

    def test_three_underwriters_listed(self):
        banks = self.mech.get("underwriter_banks", [])
        assert len(banks) >= 3
        bank_names = [b.get("name", "").lower() for b in banks]
        assert any("goldman" in n for n in bank_names)
        assert any("morgan stanley" in n for n in bank_names)
        assert any("jpmorgan" in n for n in bank_names)

    @pytest.mark.parametrize("role", [
        "ipo_underwriter",
        "enterprise_customer",
        "publisher_advertiser",
    ])
    def test_each_bank_has_triple_role(self, role):
        banks = self.mech.get("underwriter_banks", [])
        for bank in banks:
            roles = bank.get("anthropic_roles", [])
            assert role in roles, \
                f"{bank.get('name')} missing role '{role}': has {roles}"

    def test_estimated_ipo_fees(self):
        fees = self.mech.get("estimated_combined_ipo_fees_m")
        assert fees is not None
        assert fees >= 200, "Combined IPO fees should be >= $200M"


# ─── Test Class 3: GRAS Termination Timing ───

class TestGRASTerminationTiming:
    """The Global Research Analyst Settlement termination coincides with IPO preparation."""

    def setup_method(self):
        self.data = load_competitor_coverage()
        self.cpf = self.data.get("cross_publication_findings", {})
        self.mech = None
        for v in self.cpf.values():
            if isinstance(v, dict) and v.get("mechanism_id") == 46:
                self.mech = v
                break

    def test_gras_termination_documented(self):
        gras = self.mech.get("gras_termination", {})
        assert gras, "GRAS termination section must exist"

    def test_gras_termination_date(self):
        gras = self.mech.get("gras_termination", {})
        assert gras.get("date") == "2025-12-05"

    def test_gras_predecessor_regime(self):
        gras = self.mech.get("gras_termination", {})
        assert "2003" in str(gras.get("original_settlement_year", ""))

    def test_gras_successor_regime(self):
        gras = self.mech.get("gras_termination", {})
        successor = gras.get("successor_regime", "")
        assert "2241" in successor, "FINRA Rule 2241 should be noted as successor"

    def test_gras_relevance_to_ipo(self):
        gras = self.mech.get("gras_termination", {})
        relevance = gras.get("ipo_relevance", "")
        assert len(relevance) > 50, "Should explain relevance to Anthropic IPO timing"

    def test_gras_timing_months_before_ipo(self):
        """GRAS terminated Dec 2025, Anthropic IPO target Oct 2026 = 10 months."""
        gras = self.mech.get("gras_termination", {})
        months_gap = gras.get("months_before_anthropic_ipo", 0)
        assert months_gap >= 10, "GRAS termination should be documented as ~10 months pre-IPO"


# ─── Test Class 4: Goldman Sachs Dual Role ───

class TestGoldmanSachsDualRole:
    """Goldman is both IPO underwriter AND Claude enterprise customer with embedded engineers."""

    def setup_method(self):
        self.data = load_competitor_coverage()
        self.cpf = self.data.get("cross_publication_findings", {})
        self.mech = None
        for v in self.cpf.values():
            if isinstance(v, dict) and v.get("mechanism_id") == 46:
                self.mech = v
                break

    def test_goldman_enterprise_deployment(self):
        banks = self.mech.get("underwriter_banks", [])
        gs = [b for b in banks if "goldman" in b.get("name", "").lower()][0]
        deployment = gs.get("enterprise_claude_deployment", {})
        assert deployment, "Goldman Claude deployment details required"

    def test_goldman_embedded_engineers(self):
        banks = self.mech.get("underwriter_banks", [])
        gs = [b for b in banks if "goldman" in b.get("name", "").lower()][0]
        deployment = gs.get("enterprise_claude_deployment", {})
        assert deployment.get("embedded_anthropic_engineers") is True

    def test_goldman_cio_on_record(self):
        banks = self.mech.get("underwriter_banks", [])
        gs = [b for b in banks if "goldman" in b.get("name", "").lower()][0]
        deployment = gs.get("enterprise_claude_deployment", {})
        assert "Argenti" in str(deployment.get("executive_on_record", ""))

    def test_goldman_use_cases(self):
        banks = self.mech.get("underwriter_banks", [])
        gs = [b for b in banks if "goldman" in b.get("name", "").lower()][0]
        deployment = gs.get("enterprise_claude_deployment", {})
        use_cases = deployment.get("use_cases", [])
        assert len(use_cases) >= 2


# ─── Test Class 5: Morgan Stanley Research Pipeline ───

class TestMorganStanleyResearchPipeline:
    """Morgan Stanley published Claude research while preparing to underwrite Anthropic IPO."""

    def setup_method(self):
        self.data = load_competitor_coverage()
        self.cpf = self.data.get("cross_publication_findings", {})
        self.mech = None
        for v in self.cpf.values():
            if isinstance(v, dict) and v.get("mechanism_id") == 46:
                self.mech = v
                break

    def test_ms_research_report_documented(self):
        banks = self.mech.get("underwriter_banks", [])
        ms = [b for b in banks if "morgan stanley" in b.get("name", "").lower()][0]
        research = ms.get("pre_ipo_research", {})
        assert research, "Morgan Stanley pre-IPO research documented"

    def test_ms_research_mentions_claude(self):
        banks = self.mech.get("underwriter_banks", [])
        ms = [b for b in banks if "morgan stanley" in b.get("name", "").lower()][0]
        research = ms.get("pre_ipo_research", {})
        desc = str(research.get("description", "")).lower()
        assert "claude" in desc, "Research should mention Claude"

    def test_ms_research_predates_ipo(self):
        banks = self.mech.get("underwriter_banks", [])
        ms = [b for b in banks if "morgan stanley" in b.get("name", "").lower()][0]
        research = ms.get("pre_ipo_research", {})
        date = research.get("date", "")
        assert date < "2026-06-08", "Research should predate S-1 filing"


# ─── Test Class 6: JPMorgan Enterprise Scale ───

class TestJPMorganEnterpriseScale:
    """JPMorgan deployed Claude to 200K+ employees, largest known enterprise deployment."""

    def setup_method(self):
        self.data = load_competitor_coverage()
        self.cpf = self.data.get("cross_publication_findings", {})
        self.mech = None
        for v in self.cpf.values():
            if isinstance(v, dict) and v.get("mechanism_id") == 46:
                self.mech = v
                break

    def test_jpmorgan_employee_deployment_scale(self):
        banks = self.mech.get("underwriter_banks", [])
        jpm = [b for b in banks if "jpmorgan" in b.get("name", "").lower()][0]
        deployment = jpm.get("enterprise_claude_deployment", {})
        employees = deployment.get("employees_with_access", 0)
        assert employees >= 200000

    def test_jpmorgan_tech_budget(self):
        banks = self.mech.get("underwriter_banks", [])
        jpm = [b for b in banks if "jpmorgan" in b.get("name", "").lower()][0]
        deployment = jpm.get("enterprise_claude_deployment", {})
        budget_b = deployment.get("annual_tech_budget_b", 0)
        assert budget_b >= 15


# ─── Test Class 7: Meta Zero-IPO-Incentive Comparison ───

class TestMetaZeroIPOIncentive:
    """Meta has zero IPO fee incentive across all three underwriter banks."""

    def setup_method(self):
        self.data = load_competitor_coverage()
        self.cpf = self.data.get("cross_publication_findings", {})
        self.mech = None
        for v in self.cpf.values():
            if isinstance(v, dict) and v.get("mechanism_id") == 46:
                self.mech = v
                break

    def test_meta_ipo_year_documented(self):
        meta = self.mech.get("meta_comparison", {})
        assert meta.get("ipo_year") == 2012

    def test_meta_current_ipo_fee_incentive_zero(self):
        meta = self.mech.get("meta_comparison", {})
        assert meta.get("current_ipo_fee_incentive_m") == 0

    def test_meta_enterprise_ai_in_underwriter_banks_zero(self):
        meta = self.mech.get("meta_comparison", {})
        assert meta.get("enterprise_ai_products_in_underwriter_banks") == 0

    def test_meta_underwriter_entanglement_index_zero(self):
        meta = self.mech.get("meta_comparison", {})
        assert meta.get("underwriter_entanglement_index") == 0


# ─── Test Class 8: Legitimate Factors ───

class TestLegitimateFactors:
    """Every mechanism must document confounding / legitimate editorial factors."""

    def setup_method(self):
        self.data = load_competitor_coverage()
        self.cpf = self.data.get("cross_publication_findings", {})
        self.mech = None
        for v in self.cpf.values():
            if isinstance(v, dict) and v.get("mechanism_id") == 46:
                self.mech = v
                break

    def test_legitimate_factors_exist(self):
        factors = self.mech.get("legitimate_factors", [])
        assert len(factors) >= 4, f"Expected >=4 legitimate factors, got {len(factors)}"

    def test_finra_rule_2241_acknowledged(self):
        factors = self.mech.get("legitimate_factors", [])
        factors_text = " ".join(str(f) for f in factors).lower()
        assert "2241" in factors_text or "finra" in factors_text, \
            "Should acknowledge FINRA Rule 2241 as a mitigating factor"

    def test_chinese_wall_acknowledged(self):
        factors = self.mech.get("legitimate_factors", [])
        factors_text = " ".join(str(f) for f in factors).lower()
        has_wall = "information barrier" in factors_text or "chinese wall" in factors_text \
            or "firewall" in factors_text or "wall" in factors_text
        assert has_wall, "Should acknowledge information barriers"


# ─── Test Class 9: Pre-IPO Timeline ───

class TestPreIPOTimeline:
    """Key dates in the underwriter-IPO pipeline are documented."""

    def setup_method(self):
        self.data = load_competitor_coverage()
        self.cpf = self.data.get("cross_publication_findings", {})
        self.mech = None
        for v in self.cpf.values():
            if isinstance(v, dict) and v.get("mechanism_id") == 46:
                self.mech = v
                break

    def test_timeline_has_entries(self):
        timeline = self.mech.get("timeline", [])
        assert len(timeline) >= 5

    def test_timeline_includes_s1_filing(self):
        timeline = self.mech.get("timeline", [])
        dates = [t.get("date", "") for t in timeline]
        assert "2026-06-01" in dates, "Should include Anthropic S-1 filing date"

    def test_timeline_includes_gras_termination(self):
        timeline = self.mech.get("timeline", [])
        dates = [t.get("date", "") for t in timeline]
        assert "2025-12-05" in dates, "Should include GRAS termination date"

    def test_timeline_includes_ipo_target(self):
        timeline = self.mech.get("timeline", [])
        events = [t.get("event", "").lower() for t in timeline]
        has_ipo = any("ipo" in e and "october" in e for e in events)
        assert has_ipo, "Should include October 2026 IPO target"


# ─── Test Class 10: SpaceX Fee Precedent ───

class TestSpaceXFeePrecedent:
    """SpaceX IPO fee data provides precedent for estimating Anthropic fees."""

    def setup_method(self):
        self.data = load_competitor_coverage()
        self.cpf = self.data.get("cross_publication_findings", {})
        self.mech = None
        for v in self.cpf.values():
            if isinstance(v, dict) and v.get("mechanism_id") == 46:
                self.mech = v
                break

    def test_spacex_precedent_documented(self):
        precedent = self.mech.get("fee_precedent", {})
        assert precedent, "SpaceX fee precedent should be documented"

    def test_spacex_total_fees(self):
        precedent = self.mech.get("fee_precedent", {})
        assert precedent.get("spacex_total_fees_m") >= 500

    def test_spacex_lead_bank_fees(self):
        precedent = self.mech.get("fee_precedent", {})
        assert precedent.get("spacex_lead_bank_fee_each_m") >= 100

    def test_anthropic_fee_estimate_provided(self):
        precedent = self.mech.get("fee_precedent", {})
        estimate = precedent.get("anthropic_estimated_total_fees_m")
        assert estimate is not None
        assert estimate >= 200


# ─── Test Class 11: Coverage Prediction ───

class TestCoveragePrediction:
    """Mechanism should make testable coverage predictions."""

    def setup_method(self):
        self.data = load_competitor_coverage()
        self.cpf = self.data.get("cross_publication_findings", {})
        self.mech = None
        for v in self.cpf.values():
            if isinstance(v, dict) and v.get("mechanism_id") == 46:
                self.mech = v
                break

    def test_coverage_prediction_exists(self):
        pred = self.mech.get("coverage_prediction", {})
        assert pred, "Coverage prediction should exist"

    def test_prediction_is_testable(self):
        pred = self.mech.get("coverage_prediction", {})
        assert "testable_hypothesis" in pred

    def test_prediction_has_timeframe(self):
        pred = self.mech.get("coverage_prediction", {})
        assert "verification_window" in pred


# ─── Test Class 12: Cross-References to Prior Mechanisms ───

class TestCrossReferences:
    """Mechanism #46 should reference relevant prior mechanisms."""

    def setup_method(self):
        self.data = load_competitor_coverage()
        self.cpf = self.data.get("cross_publication_findings", {})
        self.mech = None
        for v in self.cpf.values():
            if isinstance(v, dict) and v.get("mechanism_id") == 46:
                self.mech = v
                break

    def test_references_investor_triangle(self):
        refs = self.mech.get("cross_references", [])
        assert any(r.get("mechanism_id") in [28, 34, 35, 36] for r in refs), \
            "Should reference investor-publisher triangle mechanisms"

    def test_references_at_least_two_prior_mechanisms(self):
        refs = self.mech.get("cross_references", [])
        assert len(refs) >= 2
