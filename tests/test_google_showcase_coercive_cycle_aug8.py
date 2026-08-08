"""
Type C: Financial Incentive Mapping — Google's Five-Year Coercive Dependency Cycle
Aug 8, 2026 02:00 PT

Tests documenting Google's temporal evolution from Showcase dependency creation
(2020) through AI Overviews traffic destruction (2024-2026) to forced AI training
rights surrender (Jun 2026).

KEY FINDING — THREE-STAGE COERCIVE EXTRACTION MODEL:

Stage 1 (2020-2024): DEPENDENCY CREATION
  - Google pledges $1B over 3 years for News Showcase (Oct 2020)
  - Signs 3,000+ publications with individual contracts ($25K-$250K/yr)
  - Contracts include secrecy NDAs preventing publisher coordination
  - Contracts include termination-if-sued clauses suppressing litigation
  - IP clauses allow Google to "reproduce, distribute, publicly display,
    publicly perform, and otherwise use" publisher content
  - Former Google exec Madhav Chinnappa: Showcase was designed to
    "protect ourselves" from regulatory pressure — "renting your enemies"

Stage 2 (2024-2026): ALTERNATIVE REVENUE DESTRUCTION
  - AI Overviews reduces publisher search referral traffic 33-38% globally
  - Google Network revenue (AdSense/publishers' share) declines to $7.3B
    Q2 2026 (-0.7% YoY), first sub-$7B quarter in Q1 2026
  - Publishers become MORE dependent on Showcase fees as traffic revenue falls
  - Condé Nast CEO: "plan as if search traffic will be zero"

Stage 3 (Jun 2026): FORCED RIGHTS EXTRACTION
  - Google tells publishers: join "News AI pilot" granting broad AI training
    rights OR lose Showcase annual fees when program sunsets
  - Google's coercion explicitly conditional: surrender copyright → keep fees
  - Jason Kint (DCN CEO): "There's no fair deal discussions that can happen
    with Google. It's really a matter of how much money they want to drop"
  - Initial pilot participants include The Guardian, Der Spiegel, El País

CONTRAST WITH META:
  - Meta has ZERO coercive mechanisms over publishers
  - Meta's AI deals are voluntary bilateral ($50M/yr News Corp)
  - No traffic control, no ad dependency, no fee leverage
  - No secrecy clauses, no anti-litigation clauses
  - Publishers can decline Meta deals with zero financial consequence

Sources:
  - Tech Policy Press "Invisible Hand" investigation:
    https://www.techpolicy.press/how-google-paid-the-media-millions-to-avoid-regulatory-pressure/
  - PYMNTS (Jun 25, 2026):
    https://www.pymnts.com/news/artificial-intelligence/2026/google-tells-news-publishers-to-share-content-for-ai-training-or-lose-fees/
  - Android Headlines (Jul 2026):
    https://www.androidheadlines.com/2026/07/google-forces-publishers-ai-training-rights-news-showcase.html
  - NY Post (Jun 26, 2026):
    https://nypost.com/2026/06/26/business/google-looks-to-bleed-publishers-with-new-ai-partnerships-that-would-cull-their-content/
  - Digiday (Jun 2026):
    https://digiday.com/media/googles-ai-opt-out-leaves-publishers-with-a-choice-they-cant-safely-use/
  - Fastly analysis:
    https://www.fastly.com/blog/google-ai-deal-no-publisher-wanted
  - Google Showcase $1B pledge (Oct 2020):
    https://www.reuters.com/world/americas/google-pay-publishers-1-bln-over-three-years-their-news-2020-10-01/
"""

import pytest
import yaml
import os
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return yaml.safe_load(f)


# ─────────────────────────────────────────────────────────────────
# 1. THREE-STAGE COERCIVE EXTRACTION MODEL — Temporal Ordering
# ─────────────────────────────────────────────────────────────────

class TestThreeStageCoerciveModel:
    """Validates the three-stage temporal dependency cycle."""

    def test_stage_1_showcase_launched_2020(self):
        """Stage 1: Google launched Showcase Oct 2020 with $1B commitment."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        coercion = google["showcase_coercive_cycle"]
        assert coercion["stage_1_dependency_creation"]["launch_date"] == "2020-10-01"

    def test_stage_1_billion_dollar_commitment(self):
        """Stage 1: Google pledged $1B over 3 years."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        coercion = google["showcase_coercive_cycle"]
        assert coercion["stage_1_dependency_creation"]["commitment_b"] == 1.0

    def test_stage_1_publisher_count(self):
        """Stage 1: Over 3,000 publications signed."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        coercion = google["showcase_coercive_cycle"]
        assert coercion["stage_1_dependency_creation"]["publisher_count"] >= 3000

    def test_stage_1_contract_range(self):
        """Stage 1: Individual contracts $25K-$250K/yr."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        coercion = google["showcase_coercive_cycle"]
        s1 = coercion["stage_1_dependency_creation"]
        assert s1["contract_floor_k"] == 25
        assert s1["contract_ceiling_k"] == 250

    def test_stage_1_secrecy_clauses(self):
        """Stage 1: Contracts include NDA preventing coordination."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        coercion = google["showcase_coercive_cycle"]
        s1 = coercion["stage_1_dependency_creation"]
        assert s1["secrecy_clauses"] is True

    def test_stage_1_anti_litigation_clauses(self):
        """Stage 1: Contracts include termination-if-sued clause."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        coercion = google["showcase_coercive_cycle"]
        s1 = coercion["stage_1_dependency_creation"]
        assert s1["anti_litigation_clauses"] is True

    def test_stage_2_traffic_decline_pct(self):
        """Stage 2: AI Overviews reduced publisher traffic 33-38%."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        coercion = google["showcase_coercive_cycle"]
        s2 = coercion["stage_2_traffic_destruction"]
        assert s2["traffic_decline_pct_global"] >= 33
        assert s2["traffic_decline_pct_us"] >= 38

    def test_stage_2_network_revenue_decline(self):
        """Stage 2: Google Network revenue declining YoY."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        coercion = google["showcase_coercive_cycle"]
        s2 = coercion["stage_2_traffic_destruction"]
        assert s2["network_revenue_q2_2026_b"] == 7.3
        assert s2["network_revenue_q2_yoy_pct"] < 0

    def test_stage_3_ultimatum_date(self):
        """Stage 3: License-or-lose ultimatum reported Jun 25, 2026."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        coercion = google["showcase_coercive_cycle"]
        s3 = coercion["stage_3_forced_rights_extraction"]
        assert s3["ultimatum_date"] == "2026-06-25"

    def test_stage_3_showcase_sunset_announced(self):
        """Stage 3: Google announced Showcase will be ended."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        coercion = google["showcase_coercive_cycle"]
        s3 = coercion["stage_3_forced_rights_extraction"]
        assert s3["showcase_sunset"] is True

    def test_stage_3_ai_training_required(self):
        """Stage 3: New pilot requires broad AI training rights."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        coercion = google["showcase_coercive_cycle"]
        s3 = coercion["stage_3_forced_rights_extraction"]
        assert s3["ai_training_required"] is True


# ─────────────────────────────────────────────────────────────────
# 2. CONTRACT CLAUSE ANALYSIS — "Invisible Hand" Investigation
# ─────────────────────────────────────────────────────────────────

class TestShowcaseContractClauses:
    """Validates contract clause findings from cross-border investigation."""

    def test_ip_clause_scope(self):
        """IP clauses allow Google to reproduce, distribute, display, perform publisher content."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        clauses = google["showcase_coercive_cycle"]["contract_clauses"]
        ip = clauses["ip_rights"]
        for verb in ["reproduce", "distribute", "publicly display", "publicly perform"]:
            assert verb in ip["scope"].lower()

    def test_secrecy_clause_bilateral(self):
        """Secrecy clause prevents both parties from disclosing terms."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        clauses = google["showcase_coercive_cycle"]["contract_clauses"]
        assert clauses["secrecy"]["bilateral"] is True

    def test_secrecy_survives_termination(self):
        """Secrecy clause persists even after contract termination."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        clauses = google["showcase_coercive_cycle"]["contract_clauses"]
        assert clauses["secrecy"]["survives_termination"] is True

    def test_anti_litigation_termination_trigger(self):
        """Google can terminate if publisher files legal claim."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        clauses = google["showcase_coercive_cycle"]["contract_clauses"]
        assert clauses["termination_triggers"]["publisher_litigation"] is True

    def test_anti_legislation_termination_trigger(self):
        """Google can terminate if legislation mandating payment passes."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        clauses = google["showcase_coercive_cycle"]["contract_clauses"]
        assert clauses["termination_triggers"]["legislation_passed"] is True

    def test_corint_media_refused_ip_clarification(self):
        """Google refused to confirm IP clause isn't a shield for AI training."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        clauses = google["showcase_coercive_cycle"]["contract_clauses"]
        assert clauses["ip_rights"]["google_refused_ai_training_clarification"] is True


# ─────────────────────────────────────────────────────────────────
# 3. ANTI-COORDINATION MECHANISM — Secrecy as Strategy
# ─────────────────────────────────────────────────────────────────

class TestAntiCoordinationMechanism:
    """Validates secrecy clauses as anti-coordination weapons."""

    def test_prevents_publisher_learning(self):
        """NDAs prevent publishers from learning each other's terms."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        anti_coord = google["showcase_coercive_cycle"]["anti_coordination"]
        assert "collaboration" in anti_coord["effect"].lower() or "learning" in anti_coord["effect"].lower()

    def test_pipa_chairman_quote(self):
        """Nelson Yap (PIPA) called it a 'strategy to inhibit collaboration.'"""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        anti_coord = google["showcase_coercive_cycle"]["anti_coordination"]
        assert "inhibit" in anti_coord["pipa_assessment"].lower() or "strategy" in anti_coord["pipa_assessment"].lower()

    def test_global_strategy(self):
        """Google uses NDA strategy globally, not just in one market."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        anti_coord = google["showcase_coercive_cycle"]["anti_coordination"]
        assert anti_coord["global"] is True

    def test_meta_no_secrecy_clauses(self):
        """Meta's AI deals have no known secrecy/NDA preventing coordination."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        contrast = google["showcase_coercive_cycle"]["meta_contrast"]
        assert "secrecy" in contrast.lower() or "nda" in contrast.lower()


# ─────────────────────────────────────────────────────────────────
# 4. AUSTRALIA TERMINATION PRECEDENT
# ─────────────────────────────────────────────────────────────────

class TestAustraliaTermination:
    """Validates Google's unilateral Australian contract termination."""

    def test_australia_termination_date(self):
        """Google terminated Australian Showcase contracts Jun 2025."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        australia = google["showcase_coercive_cycle"]["australia_termination"]
        assert "2025" in str(australia["date"])

    def test_pipa_publishers_count(self):
        """24 PIPA publishers had negotiated 5-year renewable contracts."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        australia = google["showcase_coercive_cycle"]["australia_termination"]
        assert australia["pipa_publishers_affected"] == 24

    def test_contract_duration_broken(self):
        """Contracts were 5-year but terminated after 3 years."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        australia = google["showcase_coercive_cycle"]["australia_termination"]
        assert australia["contract_years"] == 5
        assert australia["terminated_after_years"] == 3

    def test_no_consultation(self):
        """Termination came with no prior notice or consultation."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        australia = google["showcase_coercive_cycle"]["australia_termination"]
        assert australia["no_notice"] is True


# ─────────────────────────────────────────────────────────────────
# 5. "RENTING YOUR ENEMIES" — Former Google Exec Admission
# ─────────────────────────────────────────────────────────────────

class TestRentingEnemiesAdmission:
    """Validates admissions from former Google News executives."""

    def test_chinnappa_protective_framing(self):
        """Madhav Chinnappa described Showcase as protecting Google from regulation."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        admissions = google["showcase_coercive_cycle"]["former_exec_admissions"]
        assert "protect" in admissions["chinnappa_quote"].lower()

    def test_blecher_renting_enemies(self):
        """Ludovic Blecher characterized it as 'renting your enemies.'"""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        admissions = google["showcase_coercive_cycle"]["former_exec_admissions"]
        assert "renting" in admissions["blecher_characterization"].lower()

    def test_chinnappa_predicted_worsening(self):
        """Chinnappa predicted Showcase would make things worse, not better."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        admissions = google["showcase_coercive_cycle"]["former_exec_admissions"]
        assert "worse" in admissions["chinnappa_prediction"].lower()


# ─────────────────────────────────────────────────────────────────
# 6. MEDIASCOPE PROFILED PUBLICATION EXPOSURE
# ─────────────────────────────────────────────────────────────────

class TestProfiledPublicationExposure:
    """Checks which MediaScope-profiled publications are in the Showcase/pilot."""

    @pytest.mark.parametrize("pub", [
        "guardian",
    ])
    def test_guardian_in_ai_pilot(self, pub):
        """The Guardian is named as an early News AI pilot participant."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        pilot = google["showcase_coercive_cycle"]["stage_3_forced_rights_extraction"]
        participants = [p.lower() for p in pilot["named_pilot_participants"]]
        assert any("guardian" in p for p in participants)

    def test_ft_showcase_participation(self):
        """FT has a confirmed Google News AI pilot deal (Feb 2026)."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        cycle = google["showcase_coercive_cycle"]
        profiled = cycle["profiled_publication_exposure"]
        ft_entry = [p for p in profiled if "ft" in p["slug"].lower() or "financial" in p.get("name", "").lower()]
        assert len(ft_entry) > 0

    def test_guardian_openai_deal_plus_google_pilot(self):
        """Guardian has BOTH an OpenAI deal (Feb 2025) AND a Google News AI pilot."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        cycle = google["showcase_coercive_cycle"]
        profiled = cycle["profiled_publication_exposure"]
        guardian_entry = [p for p in profiled if "guardian" in p["slug"].lower()]
        assert len(guardian_entry) > 0
        assert guardian_entry[0]["dual_deal"] is True


# ─────────────────────────────────────────────────────────────────
# 7. META CONTRAST — Zero Coercive Mechanisms
# ─────────────────────────────────────────────────────────────────

class TestMetaContrastZeroCoercion:
    """Validates Meta has zero coercive publisher mechanisms."""

    def test_meta_no_showcase_equivalent(self):
        """Meta has no Showcase-like program creating dependency."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        contrast = google["showcase_coercive_cycle"]["meta_contrast"]
        assert "voluntary" in contrast.lower()

    def test_meta_no_traffic_control(self):
        """Meta doesn't control web search traffic to publishers."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        contrast = google["showcase_coercive_cycle"]["meta_contrast"]
        assert "traffic" in contrast.lower() or "search" in contrast.lower()

    def test_meta_no_secrecy_requirement(self):
        """Meta deals have no known secrecy/NDA clauses."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        contrast = google["showcase_coercive_cycle"]["meta_contrast"]
        assert "secrecy" in contrast.lower() or "nda" in contrast.lower()

    def test_meta_no_anti_litigation_clause(self):
        """Meta deals don't terminate if publishers sue."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        contrast = google["showcase_coercive_cycle"]["meta_contrast"]
        assert "litigation" in contrast.lower() or "sue" in contrast.lower()


# ─────────────────────────────────────────────────────────────────
# 8. DEPENDENCY METRICS
# ─────────────────────────────────────────────────────────────────

class TestDependencyMetrics:
    """Validates reported publisher dependency statistics."""

    def test_small_publisher_15pct_revenue(self):
        """A small publisher reported Showcase = 15% of revenue."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        metrics = google["showcase_coercive_cycle"]["dependency_metrics"]
        assert metrics["small_publisher_revenue_pct"] == 15

    def test_australian_publisher_5pct(self):
        """An Australian publisher reported Showcase = 5% of annual budget."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        metrics = google["showcase_coercive_cycle"]["dependency_metrics"]
        assert metrics["australian_publisher_budget_pct"] == 5

    def test_brazilian_publisher_40pct(self):
        """A Brazilian publisher reported Showcase = 40% of revenue."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        metrics = google["showcase_coercive_cycle"]["dependency_metrics"]
        assert metrics["brazilian_publisher_revenue_pct"] == 40


# ─────────────────────────────────────────────────────────────────
# 9. SOURCE CITATIONS
# ─────────────────────────────────────────────────────────────────

class TestSourceCitations:
    """Validates all findings have source URLs."""

    def test_showcase_cycle_has_sources(self):
        """The coercive cycle section has source URLs."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        sources = google["showcase_coercive_cycle"]["source_urls"]
        assert len(sources) >= 5

    def test_techpolicy_source_present(self):
        """Tech Policy Press cross-border investigation cited."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        sources = google["showcase_coercive_cycle"]["source_urls"]
        assert any("techpolicy" in s for s in sources)

    def test_pymnts_source_present(self):
        """PYMNTS Jun 25, 2026 report cited."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        sources = google["showcase_coercive_cycle"]["source_urls"]
        assert any("pymnts" in s for s in sources)

    def test_nypost_source_present(self):
        """NY Post Jun 26, 2026 report cited."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        sources = google["showcase_coercive_cycle"]["source_urls"]
        assert any("nypost" in s for s in sources)


# ─────────────────────────────────────────────────────────────────
# 10. COERCION MECHANISM COMPARISON — Google vs Meta
# ─────────────────────────────────────────────────────────────────

class TestCoercionMechanismComparison:
    """Validates the structural comparison between Google and Meta."""

    GOOGLE_COERCION_MECHANISMS = [
        "showcase_dependency",
        "traffic_destruction",
        "forced_rights_extraction",
        "secrecy_clauses",
        "anti_litigation_clauses",
    ]

    @pytest.mark.parametrize("mechanism", GOOGLE_COERCION_MECHANISMS)
    def test_google_has_mechanism(self, mechanism):
        """Google has each documented coercive mechanism."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        cycle = google["showcase_coercive_cycle"]
        mechanisms = cycle.get("coercion_mechanisms", [])
        mechanism_names = [m["name"] for m in mechanisms]
        assert mechanism in mechanism_names

    def test_meta_coercion_count_zero(self):
        """Meta has zero coercive mechanisms."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        cycle = google["showcase_coercive_cycle"]
        assert cycle["meta_coercion_count"] == 0

    def test_google_coercion_count_five(self):
        """Google has five documented coercive mechanisms."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        cycle = google["showcase_coercive_cycle"]
        assert cycle["google_coercion_count"] == 5

    def test_coverage_asymmetry_direction(self):
        """Despite 5:0 coercion ratio, Meta gets more adversarial coverage."""
        entities = load_yaml("competitor-entities.yaml")
        google = entities["entities"]["google"]
        cycle = google["showcase_coercive_cycle"]
        assert "meta" in cycle["coverage_paradox"].lower()
        assert "adversarial" in cycle["coverage_paradox"].lower()
