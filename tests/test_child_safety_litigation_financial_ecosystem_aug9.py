"""
Type C: Financial Incentive Mapping — Children's Safety Litigation Coverage Financial Ecosystem
Date: 2026-08-09 21:00 PT

KEY FINDING: Meta faces disproportionate litigation coverage intensity compared to
Google/YouTube despite both platforms being found liable in the SAME bellwether trial
(KGM v. Meta & Google, LA March 2026). The asymmetry is structurally predictable from
publisher financial dependencies.

MECHANISM: Google's "Settle-and-Silence" Strategy
Google/YouTube systematically settles children's safety cases early (KGM bellwether,
$30M YouTube privacy class action, $170M FTC COPPA settlement), removing itself from
the litigation narrative and concentrating ALL media attention on Meta. This is not
necessarily coordinated — it may be rational litigation strategy — but the EFFECT is a
massive asymmetry in public perception that aligns perfectly with publisher financial
incentive predictions.

DATA:
- LA bellwether (Mar 2026): Meta 70% / YouTube 30% liability split, $6M total. YouTube
  settled separately (terms undisclosed, Jun 2026). Meta continued litigating.
- New Mexico (Aug 2026): $942M ruling — Meta-only defendant. No YouTube/Google involvement.
- Oakland (Aug 12, 2026): $1.4T state AG demand — Meta-only defendant. 29 states.
  YouTube NOT named despite being found liable in the SAME type of harm 5 months earlier.
- Meta Q2 2026 legal costs: $2.4B. Google's youth safety litigation costs: undisclosed,
  presumably minimal due to early settlement strategy.

PUBLISHER FINANCIAL INCENTIVE ALIGNMENT:
- Adversarial Meta coverage costs publishers $0 (no Meta ad dependency)
- Adversarial Google coverage risks $81.6B/yr in publisher advertising revenue
- The "safe target coefficient" predicts publishers will cover Meta's litigation
  extensively while minimizing Google/YouTube's identical exposure
- YouTube's early settlements make this EASY — no YouTube trial → no YouTube coverage

PLAINTIFFS' LAW FIRM ECOSYSTEM:
- MDL 3047 Co-Lead: Lieff Cabraser + Motley Rice + Seeger Weiss
- Working on contingency (est. 25-33% of recovery)
- Active PR operations (Motley Rice blog posts celebrating verdicts)
- Financial incentive to generate adverse media coverage → public pressure → higher
  settlements/verdicts → higher contingency fees
- These firms represent 2,600+ individual plaintiffs + support state AG cases

Sources:
- MDL 3047 docket: https://assets.alm.com/7f/b9/e4659b1943ad912e11f78cebfa78/in-re-social-media-adolescent-candce-22-03047-2332-0.pdf
- Motley Rice victory blog: https://www.motleyrice.com/news/social-media-lawsuit-verdict-jury-send-message-protect-children
- YouTube KGM settlement: https://WWW.Engadget.com/2200409/youtube-settles-early-test-case-over-social-media-harm-to-children/
- NM $942M ruling: https://www.wsj.com/tech/meta-ordered-to-pay-942-million-to-address-harm-to-kids-from-social-media-8ba5aab7
- NM Reuters analysis: https://www.reuters.com/legal/government/how-could-new-mexicos-567-million-ruling-change-meta-2026-08-07/
- States $1.4T: https://www.reuters.com/business/meta-says-us-states-are-seeking-14-trillion-penalties-august-youth-safety-trial-2026-07-07/
- Google $170M FTC COPPA: https://www.ftc.gov/news-events/news/press-releases/2019/09/google-youtube-will-pay-record-170-million-alleged-violations-childrens-privacy-law?t
- Google $30M YouTube privacy settlement: https://www.reuters.com/sustainability/boards-policy-regulation/google-settles-youtube-childrens-privacy-lawsuit-2025-08-19/
- Fast Company trial comparison: https://www.fastcompany.com/91516835/social-media-meta-youtube-instagram-trials
- The Times $1T: https://www.thetimes.com/business/companies-markets/article/big-tech-meta-courts-youtube-flnx9xzlk
"""

import pytest
import yaml
import os


PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


@pytest.fixture(scope="module")
def competitor_entities():
    path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def competitor_research():
    path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def google_entity(competitor_entities):
    return competitor_entities['entities']['google']


@pytest.fixture(scope="module")
def ecosystem(competitor_research):
    return competitor_research.get('cross_publication_findings', {}).get(
        'child_safety_litigation_financial_ecosystem', {}
    )


# =====================================================================
# CLASS 1: Google/YouTube Youth Safety Settlement History
# =====================================================================

class TestGoogleYouthSafetySettlements:
    """Google/YouTube systematically settles children's safety cases early."""

    def test_google_has_youth_safety_settlement_history(self, google_entity):
        """Google entity must document its youth safety settlement history."""
        yss = google_entity.get('youth_safety_settlement_history')
        assert yss is not None, "Missing youth_safety_settlement_history in Google entity"

    def test_ftc_coppa_settlement_2019(self, google_entity):
        """$170M FTC COPPA settlement (2019) must be documented."""
        yss = google_entity['youth_safety_settlement_history']
        ftc = yss.get('ftc_coppa_2019')
        assert ftc is not None, "Missing ftc_coppa_2019 settlement"
        assert ftc['amount_m'] == 170

    def test_youtube_privacy_class_action_2025(self, google_entity):
        """$30M YouTube children's privacy class action settlement (2025) must be documented."""
        yss = google_entity['youth_safety_settlement_history']
        privacy = yss.get('youtube_privacy_class_action_2025')
        assert privacy is not None, "Missing youtube_privacy_class_action_2025"
        assert privacy['amount_m'] == 30

    def test_kgm_bellwether_settlement_2026(self, google_entity):
        """YouTube KGM bellwether settlement (Jun 2026) must be documented."""
        yss = google_entity['youth_safety_settlement_history']
        kgm = yss.get('kgm_bellwether_2026')
        assert kgm is not None, "Missing kgm_bellwether_2026 settlement"
        assert 'undisclosed' in str(kgm.get('terms', '')).lower()

    def test_total_known_settlements(self, google_entity):
        """Google's total known youth safety settlement costs must be at least $200M."""
        yss = google_entity['youth_safety_settlement_history']
        total = yss.get('total_known_settlements_m', 0)
        assert total >= 200, f"Total known settlements should be >= $200M, got {total}"

    def test_settlement_strategy_documented(self, google_entity):
        """The 'settle-and-silence' strategy must be documented."""
        yss = google_entity['youth_safety_settlement_history']
        strategy = yss.get('settle_and_silence_strategy')
        assert strategy is not None, "Missing settle_and_silence_strategy documentation"
        assert 'narrative' in str(strategy).lower() or 'coverage' in str(strategy).lower()


# =====================================================================
# CLASS 2: Meta vs Google Litigation Exposure Asymmetry
# =====================================================================

class TestLitigationExposureAsymmetry:
    """Meta faces disproportionate litigation despite shared liability."""

    def test_la_bellwether_both_liable(self, ecosystem):
        """LA bellwether found BOTH Meta and YouTube liable."""
        la = ecosystem.get('la_bellwether_kgm')
        assert la is not None, "Missing la_bellwether_kgm data"
        assert la.get('meta_liability_pct') == 70
        assert la.get('youtube_liability_pct') == 30

    def test_new_mexico_meta_only(self, ecosystem):
        """New Mexico $942M ruling is Meta-only."""
        nm = ecosystem.get('new_mexico_ruling')
        assert nm is not None, "Missing new_mexico_ruling"
        assert nm.get('total_amount_m') == 942
        assert nm.get('youtube_involvement') == 'none'

    def test_oakland_trial_meta_only(self, ecosystem):
        """Oakland $1.4T trial is Meta-only despite YouTube's shared liability type."""
        oakland = ecosystem.get('oakland_state_ag_trial')
        assert oakland is not None, "Missing oakland_state_ag_trial"
        assert oakland.get('youtube_named') is False
        assert oakland.get('states_count') >= 4

    def test_financial_exposure_gap(self, ecosystem):
        """Meta's total children's safety litigation exposure must exceed Google's by >10x."""
        meta_exposure = ecosystem.get('meta_total_exposure_b', 0)
        google_exposure = ecosystem.get('google_total_exposure_b', 0)
        assert meta_exposure > 0, "Meta exposure must be documented"
        assert google_exposure > 0, "Google exposure must be documented"
        ratio = meta_exposure / google_exposure if google_exposure > 0 else float('inf')
        assert ratio > 10, f"Meta/Google exposure ratio should be >10x, got {ratio:.1f}x"

    def test_youtube_kgm_settlement_timing(self, ecosystem):
        """YouTube settled KGM AFTER the verdict — timing demonstrates exit strategy."""
        la = ecosystem.get('la_bellwether_kgm')
        assert la is not None
        youtube_settled = la.get('youtube_settled_date', '')
        verdict_date = la.get('verdict_date', '')
        assert youtube_settled >= verdict_date, \
            "YouTube settlement should be on or after the verdict date"


# =====================================================================
# CLASS 3: Plaintiffs' Law Firm Financial Ecosystem
# =====================================================================

class TestPlaintiffsLawFirmEcosystem:
    """MDL co-lead counsel firms and their financial incentive structure."""

    def test_mdl_co_lead_firms_documented(self, ecosystem):
        """MDL 3047 co-lead counsel firms must be documented."""
        firms = ecosystem.get('plaintiffs_law_firm_ecosystem', {}).get('mdl_co_lead_counsel', [])
        assert len(firms) >= 3, f"Expected >= 3 co-lead counsel firms, got {len(firms)}"

    def test_lieff_cabraser_present(self, ecosystem):
        """Lieff Cabraser Heimann & Bernstein must be in co-lead counsel."""
        firms = ecosystem.get('plaintiffs_law_firm_ecosystem', {}).get('mdl_co_lead_counsel', [])
        firm_names = [f.get('name', '') for f in firms]
        assert any('Lieff' in n for n in firm_names), \
            f"Lieff Cabraser not found in co-lead counsel: {firm_names}"

    def test_motley_rice_present(self, ecosystem):
        """Motley Rice must be in co-lead counsel."""
        firms = ecosystem.get('plaintiffs_law_firm_ecosystem', {}).get('mdl_co_lead_counsel', [])
        firm_names = [f.get('name', '') for f in firms]
        assert any('Motley' in n for n in firm_names), \
            f"Motley Rice not found in co-lead counsel: {firm_names}"

    def test_seeger_weiss_present(self, ecosystem):
        """Seeger Weiss must be in co-lead counsel."""
        firms = ecosystem.get('plaintiffs_law_firm_ecosystem', {}).get('mdl_co_lead_counsel', [])
        firm_names = [f.get('name', '') for f in firms]
        assert any('Seeger' in n for n in firm_names), \
            f"Seeger Weiss not found in co-lead counsel: {firm_names}"

    def test_contingency_fee_structure(self, ecosystem):
        """Contingency fee structure must be documented."""
        pf = ecosystem.get('plaintiffs_law_firm_ecosystem', {})
        fee = pf.get('contingency_fee_range_pct', '')
        assert fee, "Missing contingency_fee_range_pct"

    def test_plaintiff_count(self, ecosystem):
        """MDL must document 2,600+ individual plaintiffs."""
        pf = ecosystem.get('plaintiffs_law_firm_ecosystem', {})
        count = pf.get('total_individual_plaintiffs', 0)
        assert count >= 2600, f"Expected >= 2,600 plaintiffs, got {count}"

    def test_pr_operations_documented(self, ecosystem):
        """Plaintiffs' firms' PR/media operations must be documented."""
        pf = ecosystem.get('plaintiffs_law_firm_ecosystem', {})
        pr = pf.get('pr_and_media_operations')
        assert pr is not None, "Missing pr_and_media_operations documentation"


# =====================================================================
# CLASS 4: Publisher Coverage Incentive Alignment
# =====================================================================

class TestPublisherCoverageIncentiveAlignment:
    """Publisher financial dependencies predict children's safety coverage direction."""

    def test_meta_coverage_cost_to_publishers(self, ecosystem):
        """Adversarial Meta coverage must cost publishers $0."""
        incentive = ecosystem.get('publisher_coverage_incentive')
        assert incentive is not None, "Missing publisher_coverage_incentive"
        assert incentive.get('adversarial_meta_coverage_cost_to_publishers') == 0

    def test_google_coverage_risk_documented(self, ecosystem):
        """Adversarial Google coverage risk ($81.6B/yr) must be documented."""
        incentive = ecosystem.get('publisher_coverage_incentive')
        assert incentive is not None
        risk = incentive.get('adversarial_google_coverage_risk_b_yr', 0)
        assert risk >= 80, f"Google coverage risk should be >= $80B/yr, got {risk}"

    def test_safe_target_prediction_stated(self, ecosystem):
        """Safe target coefficient prediction must be explicitly stated."""
        incentive = ecosystem.get('publisher_coverage_incentive')
        assert incentive is not None
        prediction = incentive.get('safe_target_prediction', '')
        assert 'meta' in prediction.lower() and 'google' in prediction.lower(), \
            "Prediction must reference both Meta and Google"

    def test_coverage_ratio_meta_vs_youtube(self, ecosystem):
        """Coverage ratio for $942M NM ruling must show Meta vs YouTube asymmetry."""
        incentive = ecosystem.get('publisher_coverage_incentive')
        assert incentive is not None
        ratio = incentive.get('nm_942m_meta_vs_youtube_coverage_ratio')
        assert ratio is not None, "Missing NM $942M coverage ratio"


# =====================================================================
# CLASS 5: The "Settle-and-Silence" Mechanism
# =====================================================================

class TestSettleAndSilenceMechanism:
    """Google's settlement strategy systematically removes YouTube from narratives."""

    def test_mechanism_documented(self, ecosystem):
        """Settle-and-silence mechanism must be formally documented."""
        mechanism = ecosystem.get('settle_and_silence_mechanism')
        assert mechanism is not None, "Missing settle_and_silence_mechanism"

    def test_mechanism_id(self, ecosystem):
        """Mechanism must have a unique ID."""
        mechanism = ecosystem.get('settle_and_silence_mechanism')
        assert mechanism is not None
        mid = mechanism.get('mechanism_id')
        assert mid is not None and mid > 0, f"Expected positive mechanism_id, got {mid}"

    def test_three_settlement_stages(self, ecosystem):
        """Must document at least 3 stages of Google's settlement pattern."""
        mechanism = ecosystem.get('settle_and_silence_mechanism')
        assert mechanism is not None
        stages = mechanism.get('settlement_stages', [])
        assert len(stages) >= 3, f"Expected >= 3 settlement stages, got {len(stages)}"

    def test_narrative_concentration_effect(self, ecosystem):
        """Must document the narrative concentration effect on Meta."""
        mechanism = ecosystem.get('settle_and_silence_mechanism')
        assert mechanism is not None
        effect = mechanism.get('narrative_concentration_effect', '')
        assert 'meta' in effect.lower(), "Effect must reference Meta as narrative target"

    def test_not_coordination_claim(self, ecosystem):
        """Analysis must explicitly state this is structural, not coordinated."""
        mechanism = ecosystem.get('settle_and_silence_mechanism')
        assert mechanism is not None
        caveat = mechanism.get('coordination_caveat', '')
        assert 'not' in caveat.lower() or 'structural' in caveat.lower(), \
            "Must explicitly disclaim coordination and note structural mechanism"


# =====================================================================
# CLASS 6: Meta Q2 2026 Legal Cost Disclosure
# =====================================================================

class TestMetaLegalCostDisclosure:
    """Meta's $2.4B Q2 2026 legal costs as coverage catalyst."""

    def test_q2_legal_costs_documented(self, ecosystem):
        """Meta's $2.4B Q2 2026 legal costs must be documented."""
        legal = ecosystem.get('meta_q2_2026_legal_costs')
        assert legal is not None, "Missing meta_q2_2026_legal_costs"
        assert legal.get('amount_b') == 2.4

    def test_google_legal_costs_comparison(self, ecosystem):
        """Google's youth safety legal costs must be compared."""
        legal = ecosystem.get('meta_q2_2026_legal_costs')
        assert legal is not None
        google_note = legal.get('google_comparison', '')
        assert google_note, "Missing Google legal cost comparison"

    def test_legal_cost_as_coverage_catalyst(self, ecosystem):
        """Must document how legal cost disclosure feeds adverse coverage cycle."""
        legal = ecosystem.get('meta_q2_2026_legal_costs')
        assert legal is not None
        catalyst = legal.get('coverage_catalyst_effect', '')
        assert catalyst, "Missing coverage_catalyst_effect"


# =====================================================================
# CLASS 7: Cross-Validation with Safe Target Coefficient
# =====================================================================

class TestCrossValidationSafeTarget:
    """Children's safety litigation findings must be consistent with safe target model."""

    def test_safe_target_coefficient_reference(self, ecosystem):
        """Must reference the safe target coefficient (mechanism from Aug 8)."""
        xref = ecosystem.get('cross_validation')
        assert xref is not None, "Missing cross_validation section"
        assert 'safe_target' in str(xref).lower()

    def test_litigation_confirms_safe_target(self, ecosystem):
        """Litigation asymmetry must be stated as confirming safe target prediction."""
        xref = ecosystem.get('cross_validation')
        assert xref is not None
        confirms = xref.get('confirms_safe_target', False)
        assert confirms is True, "Litigation asymmetry should confirm safe target model"

    def test_source_urls_present(self, ecosystem):
        """At least 5 source URLs must be provided."""
        urls = ecosystem.get('source_urls', [])
        assert len(urls) >= 5, f"Expected >= 5 source URLs, got {len(urls)}"


# =====================================================================
# CLASS 8: Quantitative Summary
# =====================================================================

class TestQuantitativeSummary:
    """Hard numbers that summarize the litigation financial ecosystem."""

    def test_meta_cumulative_youth_safety_liability_m(self, ecosystem):
        """Meta's cumulative youth safety liability must be at least $942M."""
        summary = ecosystem.get('quantitative_summary', {})
        meta_liability = summary.get('meta_cumulative_liability_m', 0)
        assert meta_liability >= 942, f"Expected >= $942M, got {meta_liability}"

    def test_google_cumulative_settlements_m(self, ecosystem):
        """Google's cumulative youth safety settlements must be at least $200M."""
        summary = ecosystem.get('quantitative_summary', {})
        google_settlements = summary.get('google_cumulative_settlements_m', 0)
        assert google_settlements >= 200, f"Expected >= $200M, got {google_settlements}"

    def test_liability_ratio(self, ecosystem):
        """Meta/Google liability ratio must be documented and significant."""
        summary = ecosystem.get('quantitative_summary', {})
        ratio = summary.get('meta_to_google_liability_ratio')
        assert ratio is not None and ratio > 3, \
            f"Meta/Google liability ratio should be >3x, got {ratio}"

    def test_pending_meta_exposure_b(self, ecosystem):
        """Meta's pending exposure ($1.4T Oakland) must be documented."""
        summary = ecosystem.get('quantitative_summary', {})
        pending = summary.get('meta_pending_exposure_b', 0)
        assert pending >= 1400, f"Expected >= $1,400B pending, got {pending}"

    def test_coverage_density_ratio(self, ecosystem):
        """Coverage density ratio (Meta vs Google child safety) must be documented."""
        summary = ecosystem.get('quantitative_summary', {})
        density = summary.get('coverage_density_ratio')
        assert density is not None, "Missing coverage_density_ratio"
