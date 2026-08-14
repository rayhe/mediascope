"""
Qualcomm Co-Marketing Supply Chain Financial Multiplier
Type C: Financial Incentive Mapping — Aug 13, 2026 21:00 PT
Mechanism #91

THESIS: Samsung Galaxy Glasses create a TRIPLE-entity financial incentive chain
that is unique among smart glasses products and structurally absent from Meta's.
The three entities in the Galaxy Glasses supply chain — Samsung (OEM), Google
(Android XR/Gemini platform), and Qualcomm (Snapdragon AR1 Gen 1 silicon) — each
independently have financial relationships with the publications reviewing smart
glasses. Qualcomm specifically operates a CO-MARKETING model with Samsung (50/50
budget split, confirmed by Qualcomm CMO Don McGuire) that AMPLIFIES Samsung's
already-massive $9.7B global advertising footprint into tech publications. This
mechanism is distinct from Mechanism #76 (Samsung-Google compound leverage)
because it identifies Qualcomm as a third financial node with its own $25M+
annual media spend, active co-marketing with Samsung, and independent brand-
building campaign ("Snapdragon. That's How") running across digital, CTV, and
social media at the same publications that review smart glasses.

TRIPLE-ENTITY FINANCIAL CHAIN (Galaxy Glasses):
  Node 1: Samsung ($9.7B global measured media, 250+ media properties, 4th-
           largest global advertiser)
  Node 2: Google (Android XR + Gemini — $239.54B projected 2026 ad revenue,
           News Showcase, content licensing deals with FT, Guardian, etc.)
  Node 3: Qualcomm ($25M+ media spend 2024, co-marketing with Samsung via
           50/50 budget split, Snapdragon brand campaigns in same publications)

META'S SUPPLY CHAIN (no equivalent triple chain):
  Node 1: Meta ($243.46B projected 2026 ad revenue — but this makes Meta a
           COMPETITOR to publishers, not a financial partner)
  Node 2: EssilorLuxottica (frame design only — ZERO advertising relationship
           with tech publications reviewing smart glasses)
  No Node 3: Meta designs its own AI (Llama) and uses custom/Qualcomm silicon
              but has NO co-marketing with Qualcomm for Ray-Ban Meta glasses.

KEY NEW EVIDENCE:
  - Qualcomm spent $25M on media in 2024 (COMvergence estimate via Adweek)
  - Qualcomm CMO Don McGuire: "50% will be Qualcomm's Snapdragon, 50% will be
    the partner" (bestmediainfo.com, co-marketing budget structure)
  - Samsung-Qualcomm co-branded TV ads in US (Galaxy S24 series had Snapdragon
    branding, confirmed McGuire at Snapdragon Summit 2024, SamMobile)
  - Qualcomm expanded partnership with Samsung (Jul 2026) now covers phones,
    watches, AND smart glasses — Snapdragon AR1 Gen 1 (The Street)
  - Samsung spent 13.8 trillion won ($9.2B) on Qualcomm chips in 2025, up
    26.5% YoY (The Investor, Korea) — procurement dependency
  - Qualcomm's "Snapdragon. That's How" campaign (72andSunny, launched Q1 2026)
    runs across broadcast, CTV, online, social, TikTok, Instagram — same
    channels as Galaxy Glasses launch coverage (Marketing Dive)
  - Qualcomm's Snapdragon ads were "shot on a Snapdragon-powered Samsung S25
    Ultra and edited on Snapdragon-powered computers" (Marketing Dive)
  - Snap also has multi-year Snapdragon XR partnership (Apr 2026) but Snap
    Specs receive MORE adversarial coverage than Samsung — suggesting co-
    marketing amplification is Samsung-specific, not Qualcomm-generic
  - Meta's Ray-Ban Meta glasses use Qualcomm Snapdragon AR1 Gen 1 too, but
    Meta has NO known co-marketing arrangement with Qualcomm for wearables

CONFOUNDING FACTORS:
  1. [STRONG] Meta's camera glasses have been on market since 2021 (Ray-Ban
     Stories), accumulating more negative coverage history. Samsung's are
     pre-launch, naturally receiving more neutral framing.
  2. [STRONG] Qualcomm's $25M media spend is small relative to Samsung's $9.7B
     or Google's $239B. The marginal influence of Qualcomm alone may be minimal.
  3. [MODERATE] Meta also uses Qualcomm AR1 Gen 1 — so the chip supplier is
     shared. The difference is the CO-MARKETING relationship, not the chip.
  4. [MODERATE] Publications may cover Samsung more favorably simply because
     Samsung is launching a competitor to Meta's dominant product, and
     competition stories are inherently positive-framed.
  5. [WEAK] Qualcomm co-marketing may target consumer electronics sites more
     than specialist tech journalism covering smart glasses.
  6. [WEAK] Samsung's frame partners (Gentle Monster, Warby Parker) add a
     fourth potential financial node in fashion/lifestyle publications, not
     covered in this mechanism.

TESTABLE PREDICTIONS:
  1. Publications with higher Samsung ad revenue dependency will show measurably
     softer Galaxy Glasses coverage than those with lower dependency.
  2. When Galaxy Glasses ship (Fall 2026), Qualcomm will run co-branded launch
     campaigns with Samsung that appear in the same publications reviewing
     the product — creating a temporal advertising-editorial overlap.
  3. Camera privacy concerns for Galaxy Glasses (identical hardware to Meta's)
     will be framed as "addressed" rather than "alarming" in publications where
     all three supply chain entities advertise.
  4. Snap Specs (Snapdragon XR, but WITHOUT Samsung's ad spend or Google's
     platform/deal leverage) will receive MORE adversarial privacy coverage
     than Samsung's glasses despite similar Qualcomm partnership, isolating
     the Samsung+Google amplifier effect.

Sources:
  - Adweek (Qualcomm $25M media spend): https://www.adweek.com/agencies/72andsunny-agency-of-record-qualcomm-snapdragon/?itm_source=homepage&itm_medium=agencies-edge&itm_campaign=5
  - SamMobile (Qualcomm CMO co-marketing): https://www.sammobile.com/news/qualcomm-cmo-sheds-light-on-the-regional-co-marketing-wins-with-samsung/
  - bestmediainfo.com (50/50 co-marketing): https://bestmediainfo.com/mediainfo/mediainfo-marketing/snapdragon-wants-consumers-to-demand-the-chip-not-just-the-phone-10620176
  - The Street (expanded Snapdragon partnership Jul 2026): https://www.thestreet.com/technology/qualcomm-samsung-expanded-chip-partnership
  - Marketing Dive (Snapdragon campaign): https://www.marketingdive.com/news/how-qualcomm-is-building-an-iconic-consumer-brand-for-the-ai-era/819041/
  - The Investor (Samsung $9.2B Qualcomm spend 2025): https://www.theinvestor.co.kr/article/10702659
  - The Current (Samsung 4th-largest global advertiser): https://www.thecurrent.com/samsung-is-the-fourth-largest-advertiser-in-the-world-heres-why-its-betting-on-outcome-based-marketing-with-publicis-media
  - MediaRadar (Samsung 250+ properties): https://advertisers.mediaradar.com/samsung-group-advertising-profile
"""

import pytest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
ENTITIES_PROFILE = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')


def load_entities():
    with open(ENTITIES_PROFILE, 'r') as f:
        return yaml.safe_load(f)


class TestQualcommCoMarketingRelationship:
    """Verify Qualcomm's co-marketing relationship with Samsung is documented."""

    def test_qualcomm_media_spend_documented(self):
        """Qualcomm's $25M media spend should be tracked."""
        data = load_entities()
        samsung = data['entities']['samsung']
        # Check that Qualcomm co-marketing is documented under Samsung
        assert 'qualcomm_comarketing' in samsung, \
            "Samsung profile must document Qualcomm co-marketing relationship"

    def test_qualcomm_media_spend_value(self):
        """Qualcomm's annual media spend should be documented with source."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        assert qc.get('qualcomm_annual_media_spend_m', 0) >= 25, \
            "Qualcomm annual media spend must be >= $25M (COMvergence 2024)"

    def test_comarketing_budget_split_documented(self):
        """50/50 co-marketing budget split should be recorded."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        assert 'budget_split' in qc or 'comarketing_split' in qc, \
            "Qualcomm-Samsung co-marketing budget split must be documented"

    def test_comarketing_has_source_urls(self):
        """Co-marketing section must have verifiable source URLs."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        assert 'source_urls' in qc and len(qc['source_urls']) >= 3, \
            "Qualcomm co-marketing must have at least 3 source URLs"

    def test_qualcomm_cmo_quote_documented(self):
        """Don McGuire's co-marketing confirmation should be referenced."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        overview = str(qc.get('overview', ''))
        assert 'McGuire' in overview or 'CMO' in overview, \
            "Qualcomm CMO Don McGuire's co-marketing confirmation must be referenced"


class TestTripleEntityFinancialChain:
    """Verify the Samsung-Google-Qualcomm triple-entity incentive chain."""

    def test_three_financial_nodes_identified(self):
        """The three financial nodes should be explicitly labeled."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        overview = str(qc.get('overview', ''))
        # Check all three entities are mentioned in the context of financial incentives
        assert 'Samsung' in overview
        assert 'Google' in overview or 'Android XR' in overview
        assert 'Qualcomm' in overview or 'Snapdragon' in overview

    def test_mechanism_id_assigned(self):
        """Mechanism should have an ID >= 91."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        assert qc.get('mechanism_id', 0) >= 91, \
            "Mechanism ID should be 91 or higher"

    def test_meta_supply_chain_contrast(self):
        """Meta's supply chain should be contrasted (no co-marketing)."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        overview = str(qc.get('overview', ''))
        assert 'Meta' in overview, \
            "Must contrast Meta's supply chain (no Qualcomm co-marketing for wearables)"

    def test_snap_comparison_documented(self):
        """Snap/Specs comparison should isolate the Samsung amplifier effect."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        overview = str(qc.get('overview', ''))
        assert 'Snap' in overview or 'Specs' in overview, \
            "Must compare Snap/Specs (Snapdragon XR but no Samsung ad multiplier)"

    def test_compound_leverage_cross_reference(self):
        """Should cross-reference mechanism #76 (Samsung-Google compound leverage)."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        related = qc.get('related_mechanisms', [])
        assert 76 in related, \
            "Must cross-reference mechanism #76 (Samsung-Google compound leverage)"


class TestQualcommMediaSpendDetails:
    """Verify granular Qualcomm advertising details."""

    def test_qualcomm_agency_documented(self):
        """Qualcomm's creative agency should be documented."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        assert '72andSunny' in str(qc) or 'McCann' in str(qc), \
            "Qualcomm's agency (72andSunny/McCann) should be documented"

    def test_snapdragon_campaign_name(self):
        """The 'Snapdragon. That's How' campaign should be recorded."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        assert "That's How" in str(qc) or 'brand campaign' in str(qc).lower(), \
            "Qualcomm's 'Snapdragon. That's How' campaign should be documented"

    def test_campaign_channels_overlap_with_reviews(self):
        """Campaign channels should show overlap with review publication channels."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        overview = str(qc.get('overview', ''))
        # Must mention that Qualcomm campaigns run in same channels as glass reviews
        channel_terms = ['digital', 'CTV', 'online', 'social', 'broadcast']
        matches = [t for t in channel_terms if t.lower() in overview.lower()]
        assert len(matches) >= 2, \
            f"Must document campaign channel overlap with review publications (found: {matches})"

    def test_samsung_qualcomm_procurement_value(self):
        """Samsung's $9.2B chip procurement from Qualcomm should be documented."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        overview = str(qc.get('overview', ''))
        assert '9.2' in overview or '13.8 trillion' in overview or 'procurement' in overview.lower(), \
            "Samsung's chip procurement from Qualcomm ($9.2B/13.8T won) must be documented"


class TestCoMarketingAmplificationForGlasses:
    """Verify the co-marketing applies specifically to glasses, not just phones."""

    def test_snapdragon_ar1_covered(self):
        """Snapdragon AR1 Gen 1 should be explicitly mentioned."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        assert 'AR1' in str(qc) or 'smart glasses' in str(qc).lower(), \
            "Snapdragon AR1 Gen 1 (glasses chip) must be mentioned"

    def test_expanded_partnership_jul_2026(self):
        """The Jul 2026 expanded Snapdragon partnership should be referenced."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        overview = str(qc.get('overview', ''))
        assert '2026' in overview and ('expanded' in overview.lower() or 'watches' in overview.lower() or 'glasses' in overview.lower()), \
            "Jul 2026 expansion to phones + watches + glasses must be documented"

    def test_cobranded_tv_ads_evidence(self):
        """Samsung TV ads with Snapdragon branding should be cited."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        overview = str(qc.get('overview', ''))
        assert 'co-branded' in overview.lower() or 'television' in overview.lower() or 'TV ads' in overview, \
            "Co-branded Samsung TV ads with Snapdragon tag must be cited"

    def test_meta_also_uses_qualcomm_but_no_comarketing(self):
        """Meta uses Qualcomm AR1 but has NO co-marketing — must be documented."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        overview = str(qc.get('overview', ''))
        assert 'no co-marketing' in overview.lower() or 'no known co-marketing' in overview.lower() or \
               'absent' in overview.lower(), \
            "Must document that Meta uses same chip but has no Qualcomm co-marketing"


class TestConfoundingFactors:
    """Verify scholarly confounding factors are documented."""

    def test_has_confounding_factors(self):
        """Must have confounding factors list."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        cf = qc.get('confounding_factors', [])
        assert len(cf) >= 4, \
            f"Must have at least 4 confounding factors (has {len(cf)})"

    def test_has_strong_confounding_factor(self):
        """Must have at least one STRONG confounding factor."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        cf = qc.get('confounding_factors', [])
        strong = [f for f in cf if 'STRONG' in str(f).upper()]
        assert len(strong) >= 1, \
            "Must have at least 1 STRONG confounding factor"

    def test_meta_installed_base_confound(self):
        """Meta's longer market presence as confounding factor."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        cf_text = str(qc.get('confounding_factors', []))
        assert 'market' in cf_text.lower() or '2021' in cf_text or 'installed' in cf_text.lower() or \
               'history' in cf_text.lower(), \
            "Must include Meta's longer market history as a confounding factor"

    def test_qualcomm_spend_small_confound(self):
        """Qualcomm's small spend relative to Samsung/Google as confounding factor."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        cf_text = str(qc.get('confounding_factors', []))
        assert 'small' in cf_text.lower() or 'relative' in cf_text.lower() or \
               'marginal' in cf_text.lower() or '$25M' in cf_text, \
            "Must include Qualcomm's small relative spend as a confounding factor"


class TestTestablePredictions:
    """Verify mechanism has testable predictions."""

    def test_has_testable_predictions(self):
        """Must have testable predictions list."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        tp = qc.get('testable_predictions', [])
        assert len(tp) >= 2, \
            f"Must have at least 2 testable predictions (has {len(tp)})"

    def test_prediction_launch_cobranding(self):
        """Should predict co-branded launch campaigns at Galaxy Glasses ship."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        tp_text = str(qc.get('testable_predictions', []))
        assert 'launch' in tp_text.lower() or 'ship' in tp_text.lower(), \
            "Must predict co-branded launch campaigns when Galaxy Glasses ship"

    def test_prediction_snap_comparison(self):
        """Should predict Snap/Specs receive more adversarial coverage."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        tp_text = str(qc.get('testable_predictions', []))
        assert 'Snap' in tp_text or 'Specs' in tp_text or 'adversarial' in tp_text.lower(), \
            "Must predict Snap/Specs will receive more adversarial coverage than Samsung"


class TestMetaCompetitorEntityComparison:
    """Verify Meta's contrasting supply chain is documented in entities."""

    def test_meta_no_qualcomm_comarketing_noted(self):
        """Meta section should note absence of Qualcomm co-marketing."""
        data = load_entities()
        # Check Meta entity has a wearables supply chain note
        meta = data['entities'].get('meta', {})
        # If meta entity doesn't exist at the entities level, check the
        # Samsung qualcomm_comarketing overview for the contrast
        qc = data['entities']['samsung']['qualcomm_comarketing']
        overview = str(qc.get('overview', ''))
        assert 'Meta' in overview, \
            "Samsung's co-marketing section must contrast with Meta's supply chain"

    def test_essilorluxottica_zero_tech_ad_noted(self):
        """EssilorLuxottica's zero tech publication advertising should be noted."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        overview = str(qc.get('overview', ''))
        assert 'EssilorLuxottica' in overview or 'frame partner' in overview.lower(), \
            "Must note EssilorLuxottica has zero advertising relationship with tech publications"


class TestSourceVerification:
    """Verify all financial claims have verifiable sources."""

    def test_qualcomm_spend_source(self):
        """Qualcomm $25M spend must cite COMvergence/Adweek."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        urls = qc.get('source_urls', [])
        url_text = str(urls)
        assert 'adweek.com' in url_text or 'comvergence' in url_text.lower(), \
            "Qualcomm $25M media spend must cite Adweek/COMvergence source"

    def test_comarketing_model_source(self):
        """50/50 co-marketing model must cite bestmediainfo or SamMobile."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        urls = qc.get('source_urls', [])
        url_text = str(urls)
        assert 'sammobile.com' in url_text or 'bestmediainfo' in url_text, \
            "Co-marketing model must cite SamMobile or bestmediainfo source"

    def test_expanded_partnership_source(self):
        """Jul 2026 expanded partnership must cite The Street or Qualcomm PR."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        urls = qc.get('source_urls', [])
        url_text = str(urls)
        assert 'thestreet.com' in url_text or 'qualcomm.com' in url_text, \
            "Jul 2026 expanded partnership must cite The Street or Qualcomm source"

    def test_samsung_procurement_source(self):
        """Samsung $9.2B chip procurement must cite The Investor."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        urls = qc.get('source_urls', [])
        url_text = str(urls)
        assert 'theinvestor' in url_text or 'procurement' in str(qc.get('overview', '')).lower(), \
            "Samsung chip procurement must cite The Investor source"

    def test_campaign_details_source(self):
        """Campaign details must cite Marketing Dive."""
        data = load_entities()
        qc = data['entities']['samsung']['qualcomm_comarketing']
        urls = qc.get('source_urls', [])
        url_text = str(urls)
        assert 'marketingdive.com' in url_text, \
            "'Snapdragon. That's How' campaign must cite Marketing Dive source"


class TestDataIntegrity:
    """Cross-validation with existing mechanisms and data."""

    def test_mechanism_76_still_exists(self):
        """Mechanism #76 (Samsung-Google compound leverage) must still exist."""
        data = load_entities()
        samsung = data['entities']['samsung']
        # Check advertising_leverage has mechanism_id 76
        adv = samsung.get('advertising_leverage', {})
        compound = adv.get('compound_leverage_with_google', {})
        assert compound.get('mechanism_id') == 76, \
            "Mechanism #76 must still exist in Samsung advertising_leverage"

    def test_no_duplicate_mechanism_id(self):
        """New mechanism ID should not duplicate existing ones."""
        data = load_entities()
        samsung = data['entities']['samsung']
        qc = samsung.get('qualcomm_comarketing', {})
        new_id = qc.get('mechanism_id', 0)
        # Ensure it doesn't conflict with #76
        adv = samsung.get('advertising_leverage', {})
        compound = adv.get('compound_leverage_with_google', {})
        existing_id = compound.get('mechanism_id', 0)
        assert new_id != existing_id, \
            f"New mechanism ID {new_id} must not duplicate existing ID {existing_id}"

    def test_samsung_ad_spend_consistent(self):
        """Samsung $9.7B ad spend should be consistent across sections."""
        data = load_entities()
        samsung = data['entities']['samsung']
        adv = samsung.get('advertising_leverage', {})
        qc = samsung.get('qualcomm_comarketing', {})
        # Both should reference $9.7B
        assert '9.7' in str(adv) and '9.7' in str(qc), \
            "Samsung $9.7B ad spend must be consistent in both advertising_leverage and qualcomm_comarketing"

    def test_test_file_count_in_directory(self):
        """Test directory should have 360+ test files."""
        test_dir = os.path.dirname(__file__)
        test_files = [f for f in os.listdir(test_dir) if f.startswith('test_') and f.endswith('.py')]
        assert len(test_files) >= 360, \
            f"Expected 360+ test files, found {len(test_files)}"
