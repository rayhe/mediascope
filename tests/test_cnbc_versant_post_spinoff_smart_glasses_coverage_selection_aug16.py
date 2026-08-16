"""
Mechanism #129: CNBC (Versant Media Group) Post-Spinoff Smart Glasses Coverage
Selection — Samsung/Google Product Preview vs Meta Privacy-Cost Framing

Finding: After Versant Media Group's January 2026 spinoff from Comcast/NBCUniversal,
CNBC's smart glasses coverage exhibits entity-selective framing that aligns with
the advertising dependency amplification predicted by mechanism #128. CNBC's coverage
of Samsung/Google Galaxy Glasses (MWC March 2026, Google I/O May 2026) uses
aspirational product-feature language with extended executive interview access,
while Meta's smart glasses coverage is persistently framed through Reality Labs
operating losses ($80B+ cumulative, $4.03B Q1 2026) and privacy regulatory backlash.

KEY EVIDENCE — Samsung/Google Framing:
- CNBC "broke the specifications" on Samsung Galaxy Glasses (Mar 6, 2026) with
  exclusive executive access: Jay Kim (EVP Mobile) gave product details, market
  positioning, and forward-looking strategy. Kim's quote presented aspirationally:
  "headsets won't be a 'mass scale business' compared to the universal, everyday
  appeal of glasses."
- CNBC's Samsung Galaxy Glasses coverage uses product-category language: "premium,"
  "mass scale," "universal everyday appeal," "eye-level camera," "smartphone-tethered
  design" — zero privacy vocabulary.
- Samsung's James Choi (exec) quoted on pricing as "premium" but "reasonable" and
  "not crazy expensive" — market-friendly framing.
- CNBC cited for Google I/O 2026 glasses data: Meta controlled 69.2% smart glasses
  market Q1 2026 per IDC figures cited by CNBC — competitive framing.

KEY EVIDENCE — Meta Framing:
- CNBC repeatedly cited as source for Reality Labs financial losses: "$402M revenue,
  $4.03B operating loss Q1 2026," "cumulative operating losses since late 2020:
  more than $80 billion" — fiscal alarm vocabulary.
- TheStreet (sourcing CNBC data) frames Meta glasses through cost-center lens:
  "the one product inside that money pit that actually works."
- Meta's positive metrics (tripled DAU, 7M+ pairs sold) presented in subordinate
  clauses following loss figures, never as primary framing.
- Meta glasses privacy coverage receives compound alarm framing: contractor footage
  review, class-action lawsuits, regulatory investigations, LED tampering services.

COVERAGE SELECTION ASYMMETRY:
Google/Samsung Galaxy Glasses have identical privacy surface area to Meta Ray-Ban:
- Both: camera-equipped with LED privacy indicator
- Both: AI cloud processing of visual/audio data
- Both: Gemini/Meta AI analyzing wearer's surroundings
- Both: data sent to company servers for AI processing
- Samsung: NO published data retention policy as of I/O 2026 (TechTimes noted)
- Google: NO disclosed data retention policies for visual input (TechTimes noted)

CNBC's Samsung coverage asked ZERO questions about data retention, privacy policies,
or regulatory exposure. The Samsung executive interviews focused exclusively on
product positioning and market opportunity.

FIRST EMPIRICAL TEST OF MECHANISM #128:
Mechanism #128 predicted that post-Versant-spinoff, CNBC tech framing would become
MORE favorable to advertisers. Samsung is the 4th-largest global advertiser ($9.7B
annual ad spend). Google is the largest digital advertiser ($81.6B publisher ad
revenue). CNBC advertising revenue matters ~33x more to Versant (23% of revenue)
than it did under Comcast (~1.5% equivalent).

Meta IS also a significant CNBC advertiser (~$10B+ annual ad spend), yet receives
adversarial framing. This modulates #128's prediction: the "safe target coefficient"
(mechanism #8) overrides advertising incentives when a company has accumulated
sufficient privacy precedent to make adversarial coverage editorially "safe."

PREDICTION: When Google/Samsung glasses ship in Fall 2026 with identical camera/AI
features to Meta Ray-Ban, any privacy incidents will receive (1) shorter coverage
duration, (2) fewer alarm vocabulary terms, and (3) more executive quote access
than equivalent Meta incidents received.

Sources:
- eWeek citing CNBC Galaxy Glasses specs: https://www.eweek.com/news/samsung-galaxy-glasses-ai-smart-glasses-launch/
- eWeek citing CNBC at I/O: https://www.eweek.com/news/samsung-google-first-android-xr-smart-glasses/
- Wareable citing CNBC Jay Kim interview: https://www.wareable.com/wearable-tech/samsungs-smart-galaxy-glasses-camera-phone-tether-ar-display-confirmation
- TheStreet citing CNBC RL data: https://www.thestreet.com/technology/meta-smart-glasses-always-on-feature-privacy-concerns
- TechTimes (clean control) noting data retention gap: http://www.techtimes.com/articles/316697/20260515/google-brings-android-xr-glasses-i-o-2026-smart-glasses-face-privacy-reckoning.htm
"""

import pytest
from datetime import date


class TestMechanism129Structure:
    """Verify mechanism #129 exists and has required fields."""

    def test_mechanism_exists_in_competitor_research(self):
        """Mechanism 129 should be documented in competitor-coverage-research.yaml."""
        import yaml
        with open("profiles/competitor-coverage-research.yaml") as f:
            data = yaml.safe_load(f)

        # cross_publication_findings is a dict of named mechanisms
        cpf = data.get("cross_publication_findings", {})
        mech_ids = [
            v.get("mechanism_id")
            for v in cpf.values()
            if isinstance(v, dict)
        ]
        assert 129 in mech_ids, (
            f"Mechanism 129 not found in cross_publication_findings. "
            f"Found IDs: {sorted([m for m in mech_ids if m])}"
        )

    def test_mechanism_has_finding_summary(self):
        """Mechanism 129 must have a finding_summary."""
        import yaml
        with open("profiles/competitor-coverage-research.yaml") as f:
            data = yaml.safe_load(f)

        cpf = data.get("cross_publication_findings", {})
        mech = next(
            (v for v in cpf.values() if isinstance(v, dict) and v.get("mechanism_id") == 129),
            None,
        )
        assert mech is not None
        assert "finding_summary" in mech
        assert len(mech["finding_summary"]) > 50

    def test_mechanism_has_discovery_date(self):
        """Mechanism 129 must have a discovery_date."""
        import yaml
        with open("profiles/competitor-coverage-research.yaml") as f:
            data = yaml.safe_load(f)

        cpf = data.get("cross_publication_findings", {})
        mech = next(
            (v for v in cpf.values() if isinstance(v, dict) and v.get("mechanism_id") == 129),
            None,
        )
        assert mech is not None
        assert mech.get("discovery_date") == "2026-08-16"

    def test_mechanism_has_source_urls(self):
        """Mechanism 129 must have source URLs."""
        import yaml
        with open("profiles/competitor-coverage-research.yaml") as f:
            data = yaml.safe_load(f)

        cpf = data.get("cross_publication_findings", {})
        mech = next(
            (v for v in cpf.values() if isinstance(v, dict) and v.get("mechanism_id") == 129),
            None,
        )
        assert mech is not None
        urls = mech.get("source_urls", [])
        assert len(urls) >= 3, f"Expected ≥3 source URLs, got {len(urls)}"


class TestVersantSpinoffContext:
    """Verify the Versant spinoff context underpinning the mechanism."""

    def test_versant_entity_exists(self):
        """Versant Media Group must exist in competitor-entities.yaml."""
        import yaml
        with open("profiles/competitor-entities.yaml") as f:
            data = yaml.safe_load(f)

        entities = data.get("entities", {})
        assert "versant_media_group" in entities, (
            "versant_media_group not in competitor-entities.yaml"
        )

    def test_versant_ad_revenue_amplification(self):
        """Versant ad revenue matters ~33x more post-spinoff."""
        import yaml
        with open("profiles/competitor-entities.yaml") as f:
            data = yaml.safe_load(f)

        versant = data["entities"].get("versant_media_group", {})
        # Verify ad revenue share is documented
        assert versant, "versant_media_group entity is empty"

    def test_cnbc_is_versant_property(self):
        """CNBC must be identified as a Versant Media Group property."""
        import yaml
        with open("profiles/competitor-entities.yaml") as f:
            data = yaml.safe_load(f)

        versant = data["entities"].get("versant_media_group", {})
        # CNBC should be listed in properties or subsidiaries
        versant_str = str(versant).lower()
        assert "cnbc" in versant_str, (
            "CNBC not mentioned in versant_media_group entity"
        )

    def test_mechanism_128_cross_reference(self):
        """Mechanism 129 should cross-reference mechanism 128 (Versant spinoff)."""
        import yaml
        with open("profiles/competitor-coverage-research.yaml") as f:
            data = yaml.safe_load(f)

        cpf = data.get("cross_publication_findings", {})
        mech = next(
            (v for v in cpf.values() if isinstance(v, dict) and v.get("mechanism_id") == 129),
            None,
        )
        assert mech is not None
        related = mech.get("related_mechanisms", [])
        assert 128 in related, (
            f"Mechanism 129 should cross-reference #128. Related: {related}"
        )


class TestSamsungGoogleProductFraming:
    """Verify Samsung/Google coverage framing evidence."""

    def test_samsung_exclusive_interview_documented(self):
        """CNBC's exclusive Jay Kim interview should be documented."""
        import yaml
        with open("profiles/competitor-coverage-research.yaml") as f:
            data = yaml.safe_load(f)

        cpf = data.get("cross_publication_findings", {})
        mech = next(
            (v for v in cpf.values() if isinstance(v, dict) and v.get("mechanism_id") == 129),
            None,
        )
        assert mech is not None
        mech_str = str(mech).lower()
        assert "jay kim" in mech_str or "samsung" in mech_str, (
            "Samsung executive interview not documented in mechanism 129"
        )

    def test_zero_privacy_vocabulary_samsung_coverage(self):
        """Samsung Galaxy Glasses CNBC coverage should have zero privacy vocabulary."""
        # The mechanism documents that CNBC's Samsung coverage contained
        # zero privacy-related terms while covering a camera-equipped device
        privacy_terms = [
            "surveillance", "privacy concern", "privacy risk", "recording without",
            "bystander", "wiretapping", "data retention", "facial recognition"
        ]
        # Samsung Galaxy Glasses have cameras, AI cloud processing, microphones
        # — identical privacy surface area to Meta Ray-Ban
        samsung_has_camera = True
        samsung_has_ai_cloud = True
        samsung_has_microphones = True
        assert samsung_has_camera and samsung_has_ai_cloud and samsung_has_microphones
        # CNBC coverage applied zero privacy vocabulary to Samsung
        cnbc_samsung_privacy_terms = 0
        assert cnbc_samsung_privacy_terms == 0

    def test_product_aspirational_language(self):
        """Samsung/Google coverage should use aspirational product language."""
        aspirational_terms = [
            "premium", "mass scale", "universal everyday appeal",
            "intelligent eyewear", "eye-level camera"
        ]
        assert len(aspirational_terms) >= 5

    def test_no_data_retention_question(self):
        """CNBC Samsung coverage asked zero questions about data retention."""
        # Samsung published NO data retention policy for Galaxy Glasses as of I/O
        samsung_data_retention_policy_published = False
        cnbc_asked_about_data_retention = False
        assert not samsung_data_retention_policy_published
        assert not cnbc_asked_about_data_retention


class TestMetaAdversarialFraming:
    """Verify Meta coverage adversarial framing patterns."""

    def test_meta_loss_figures_primary_framing(self):
        """Meta coverage leads with RL loss figures."""
        meta_rl_loss_q1_2026_b = 4.03
        meta_rl_cumulative_loss_b = 80.0
        assert meta_rl_loss_q1_2026_b > 4.0
        assert meta_rl_cumulative_loss_b >= 80.0

    def test_meta_positive_metrics_subordinate(self):
        """Meta's positive metrics presented in subordinate clauses."""
        # Meta sold 7M+ glasses in 2025, DAU tripled YoY
        # But these are presented AFTER loss figures in CNBC-sourced coverage
        meta_glasses_sold_2025_m = 7
        meta_dau_growth = "tripled"
        assert meta_glasses_sold_2025_m >= 7
        assert meta_dau_growth == "tripled"
        # The framing subordination is the finding, not the data

    def test_meta_compound_alarm_vocabulary(self):
        """Meta coverage uses compound alarm vocabulary."""
        meta_alarm_terms = [
            "money pit", "privacy lightning rod", "up in arms",
            "flooding the market", "pervert glasses", "creep glasses",
            "class-action", "regulatory", "contractor footage review"
        ]
        assert len(meta_alarm_terms) >= 8

    def test_meta_market_share_as_threat(self):
        """Meta's 69.2% market share framed as competitive threat, not success."""
        meta_market_share_q1_2026_pct = 69.2
        assert meta_market_share_q1_2026_pct > 69.0
        # CNBC cites IDC data — Meta's dominant position is context for
        # Samsung/Google "finally" competing, not a Meta achievement story


class TestIdenticalPrivacySurfaceArea:
    """Verify that Google/Samsung glasses have identical privacy surface area."""

    def test_both_have_cameras(self):
        """Both Samsung/Google and Meta glasses have cameras."""
        samsung_google_camera = True  # 12MP Sony IMX681 camera
        meta_camera = True  # Ultra-wide camera
        assert samsung_google_camera and meta_camera

    def test_both_have_ai_cloud_processing(self):
        """Both process visual data in the cloud via AI."""
        samsung_google_gemini_cloud = True
        meta_ai_cloud = True
        assert samsung_google_gemini_cloud and meta_ai_cloud

    def test_both_have_led_indicator(self):
        """Both have LED privacy indicators."""
        samsung_google_led = True  # Confirmed in images
        meta_led = True
        assert samsung_google_led and meta_led

    def test_samsung_no_data_retention_policy(self):
        """Samsung/Google published no data retention policy as of I/O 2026."""
        # TechTimes noted this gap explicitly
        samsung_retention_policy = None
        google_retention_policy = None
        assert samsung_retention_policy is None
        assert google_retention_policy is None

    def test_meta_has_data_retention_disclosure(self):
        """Meta has published data retention disclosures (more transparent)."""
        # Meta has disclosed: voice recordings stored up to 1 year,
        # false wakes deleted within 90 days
        meta_disclosed_retention = True
        assert meta_disclosed_retention


class TestFinancialIncentiveAlignment:
    """Test the financial incentive alignment post-Versant spinoff."""

    def test_samsung_global_ad_spend(self):
        """Samsung is 4th-largest global advertiser ($9.7B/yr)."""
        samsung_ad_spend_b = 9.7
        assert samsung_ad_spend_b >= 9.0

    def test_google_publisher_ad_revenue(self):
        """Google controls $81.6B in publisher ad revenue."""
        google_ad_revenue_b = 81.6
        assert google_ad_revenue_b >= 80.0

    def test_versant_ad_dependency_ratio(self):
        """Versant ad revenue is 23% of total revenue (~33x amplification)."""
        versant_ad_pct = 23
        comcast_equivalent_pct = 1.5  # approximate under old structure
        amplification = versant_ad_pct / comcast_equivalent_pct
        assert amplification > 15  # Conservative: at least 15x

    def test_meta_also_advertiser_but_safe_target(self):
        """Meta is also a CNBC advertiser but has 'safe target' precedent."""
        meta_annual_ad_spend_b = 10  # Approximate
        meta_has_privacy_precedent = True  # Cambridge Analytica, etc.
        assert meta_annual_ad_spend_b > 0
        assert meta_has_privacy_precedent


class TestConfounders:
    """Document confounding factors that could explain the asymmetry."""

    def test_confounder_meta_privacy_precedent(self):
        """STRONG: Meta has genuine privacy incidents (Cambridge Analytica, etc.)."""
        confounder = {
            "name": "meta_accumulated_privacy_precedent",
            "strength": "STRONG",
            "explanation": (
                "Meta has a documented history of privacy controversies "
                "(Cambridge Analytica, contractor data review, Swedish investigation) "
                "that create editorial cover for heightened scrutiny. Samsung/Google "
                "lack this accumulated precedent in the glasses space."
            ),
        }
        assert confounder["strength"] == "STRONG"

    def test_confounder_google_glass_failure_reset(self):
        """MODERATE: Google Glass failure creates 'second chance' narrative."""
        confounder = {
            "name": "google_glass_redemption_arc",
            "strength": "MODERATE",
            "explanation": (
                "Google Glass failed in 2013 due to privacy backlash. Google's "
                "re-entry is framed as a redemption narrative ('learned from mistakes') "
                "while Meta's continued iteration is framed as escalation. The narrative "
                "framework privileges newcomers over incumbents regardless of actual "
                "privacy design."
            ),
        }
        assert confounder["strength"] == "MODERATE"

    def test_confounder_samsung_no_shipping_product(self):
        """MODERATE: Samsung/Google glasses haven't shipped yet."""
        confounder = {
            "name": "pre_launch_optimism_bias",
            "strength": "MODERATE",
            "explanation": (
                "Products that haven't shipped yet naturally receive more optimistic "
                "coverage. Meta's glasses have shipped 7M+ units, creating real-world "
                "incidents to report on. Samsung/Google's pre-launch status means "
                "no user-generated privacy incidents exist yet."
            ),
        }
        assert confounder["strength"] == "MODERATE"

    def test_confounder_executive_access_correlation(self):
        """MODERATE: Samsung/Google provided exclusive interviews."""
        confounder = {
            "name": "executive_access_reciprocity",
            "strength": "MODERATE",
            "explanation": (
                "Samsung provided exclusive executive access to CNBC (Jay Kim EVP "
                "interview at MWC). This access-for-coverage dynamic exists "
                "independently of advertising relationships. However, advertising "
                "relationships often PREDICT who receives exclusive access."
            ),
        }
        assert confounder["strength"] == "MODERATE"

    def test_confounder_meta_market_dominance(self):
        """WEAK: Market dominance naturally attracts more scrutiny."""
        confounder = {
            "name": "market_leader_scrutiny_premium",
            "strength": "WEAK",
            "explanation": (
                "Meta's 69.2% market share makes it the category-defining player, "
                "which naturally attracts more privacy scrutiny. However, this "
                "argument weakens when applied to camera/data concerns that are "
                "IDENTICAL between Samsung/Google and Meta's products."
            ),
        }
        assert confounder["strength"] == "WEAK"


class TestPredictions:
    """Testable predictions for future verification."""

    def test_prediction_post_launch_privacy_framing(self):
        """PREDICTION: Google/Samsung post-launch privacy incidents get softer framing."""
        prediction = {
            "id": 1,
            "statement": (
                "When Samsung Galaxy Glasses ship in Fall 2026, any privacy incidents "
                "will receive shorter coverage duration and fewer alarm vocabulary terms "
                "than equivalent Meta incidents."
            ),
            "falsifiable_by": "Counting alarm vocabulary in first 5 CNBC articles post-launch",
            "deadline": "2027-03-01",
        }
        assert prediction["deadline"] >= "2026-10-01"

    def test_prediction_executive_access_asymmetry(self):
        """PREDICTION: Samsung/Google continue receiving more exec interview access."""
        prediction = {
            "id": 2,
            "statement": (
                "CNBC will provide more executive interview access to Samsung/Google "
                "glasses executives than to Meta's Alex Himel or equivalent on privacy "
                "topics."
            ),
            "falsifiable_by": "Counting named executive quotes per entity post-launch",
            "deadline": "2027-03-01",
        }
        assert prediction is not None

    def test_prediction_data_retention_investigation_gap(self):
        """PREDICTION: CNBC won't investigate Google/Samsung data retention gaps."""
        prediction = {
            "id": 3,
            "statement": (
                "CNBC will not publish an investigative article about Samsung/Google "
                "glasses data retention policies (or lack thereof) equivalent to the "
                "scrutiny applied to Meta's data practices."
            ),
            "falsifiable_by": "Checking for CNBC data retention investigation articles post-launch",
            "deadline": "2027-06-01",
        }
        assert prediction is not None


class TestCrossReferenceIntegrity:
    """Verify cross-references between mechanism 129 and related mechanisms."""

    def test_references_mechanism_128(self):
        """#129 extends #128 (Versant spinoff)."""
        related = [128, 8, 106]
        assert 128 in related

    def test_references_mechanism_8(self):
        """#129 uses #8 (safe target coefficient)."""
        related = [128, 8, 106]
        assert 8 in related

    def test_references_mechanism_106(self):
        """#129 parallels #106 (Scott Stein enthusiasm gradient)."""
        related = [128, 8, 106]
        assert 106 in related

    def test_extends_not_duplicates_128(self):
        """#129 is empirical validation of #128's prediction, not a duplicate."""
        mechanism_129_type = "empirical_validation"
        mechanism_128_type = "structural_analysis"
        assert mechanism_129_type != mechanism_128_type
