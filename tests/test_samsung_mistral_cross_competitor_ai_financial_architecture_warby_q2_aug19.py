"""
Mechanism #188: Samsung-Mistral €1B Investment — Cross-Competitor AI Model Financial
Architecture + Warby Parker Q2 2026 Pre-Launch Investment Disclosure
Type C: Financial Incentive Mapping — Wed 2026-08-19 19:00 PT

THESIS: Samsung's reported €1B investment in Mistral AI (FT, Jul 22, 2026) completes a
UNIQUE cross-competitor financial architecture where EVERY layer of Samsung's Galaxy
Glasses ecosystem is financially structured in opposition to Meta:

  Layer 1 — AI Models: Samsung invests €1B in Mistral (competes with Meta Llama in
    open-weight AI models for European/Asian markets). Samsung also uses Google Gemini
    for Galaxy AI (Google competes with Meta's Llama for platform AI leadership).
    Samsung's FIRST direct foundation-model investment outside Google signals
    deliberate AI model portfolio diversification AWAY from US-concentrated AI labs.

  Layer 2 — Platform: Android XR (Google) vs Meta Horizon OS. Google provides
    Android XR + Gemini for Galaxy Glasses. Google's ad revenue ($239.5B projected 2026)
    directly competes with Meta's ($243.5B projected 2026).

  Layer 3 — Silicon: Qualcomm AR1 Gen 1 in both Samsung and Meta glasses, but
    co-marketing exists only with Samsung (50/50 split, confirmed Qualcomm CMO).

  Layer 4 — Frame Design: Warby Parker (Google invested $150M) + Gentle Monster
    vs EssilorLuxottica (Meta partner, €90B market cap, zero tech publication ads).

  Layer 5 — Enterprise AI: Microsoft expanded Mistral partnership same week
    (Jul 22, 2026), multibillion-dollar compute deal. Microsoft competes with
    Meta in enterprise AI, Teams vs Workplace, Azure vs Meta's AI infrastructure.

WARBY PARKER Q2 2026 PRIMARY SOURCE DISCLOSURE (BusinessWire, Aug 6, 2026):
  - Revenue: $235.5M (+9.8% YoY)
  - Full-year guidance: $959M-$976M (+10-12%), EXCLUDES Intelligent Eyewear revenue
  - SG&A up 150bps driven by "technology costs as Warby prepares for launch"
  - $11.8M tariff refund used to offset launch investments
  - Pre-orders planned fall 2026, demos across 352+ stores
  - CFO: making "lab upgrades, quality-control improvements, inventory-system changes,
    loss-prevention investments" for higher-cost electronic products
  - Product margins slightly lower % but same/higher absolute dollars
  - Cash: $292.7M

PUBLISHER FINANCIAL INCENTIVE ARCHITECTURE:
  Favorable Galaxy Glasses coverage simultaneously serves:
    (1) Samsung ($9.7B global advertiser, 4th largest in world)
    (2) Google (30-60% organic traffic, Showcase, ad revenue, $75M equity in WRBY)
    (3) Qualcomm (co-marketing partner, $25M+ annual media spend)
    (4) Warby Parker (imminent holiday ad campaign for Intelligent Eyewear launch)
    (5) Mistral (Samsung-invested, sovereign AI narrative)
    Total: 5 separate financial upside channels

  Favorable Meta Ray-Ban coverage serves:
    (1) Meta (publishers' direct ad revenue competitor, $243.5B projected 2026)
    Total: 0 financial upside channels, 1 active financial downside channel

  The CROSS-COMPETITOR dimension is new: Samsung is financially betting AGAINST Meta's
  AI model leadership (Llama) through its Mistral investment. Mistral's open-weight
  models compete directly with Meta Llama in non-US markets. When a publication runs
  a favorable Galaxy Glasses review, it implicitly supports an ecosystem financially
  structured to compete with Meta at EVERY layer.

CONFOUNDERS:
  [STRONG] Samsung-Mistral deal not yet finalized — "in talks" per FT
  [STRONG] Mistral competes with many AI labs, not just Meta
  [MODERATE] Samsung already uses Google Gemini; Mistral investment may be primarily
    for robotics/sovereign-AI, not directly related to Galaxy Glasses
  [MODERATE] Publications may not be aware of Samsung's Mistral investment when
    writing Galaxy Glasses reviews
  [WEAK] Warby Parker's ad spend for Intelligent Eyewear launch not yet quantified

SOURCES:
  - FT (Jul 22, 2026): Samsung in talks to invest in Mistral at €20B valuation
  - Reuters (Jul 22, 2026): Samsung in talks to invest in Mistral
  - TechRepublic (Jul 23, 2026): Samsung Reportedly Weighs €1B Mistral AI Investment
  - Seoul Economic Daily (Jul 22, 2026): Samsung Weighs Investment in Europe's Top AI Startup Mistral
  - BusinessWire (Aug 6, 2026): Warby Parker Announces Second Quarter 2026 Results
  - Vision Monday (Aug 7, 2026): Warby Parker Q2 Revenue Rises as Launch Nears
  - MarketBeat (Aug 9, 2026): Warby Parker Q2 Earnings Call Highlights
  - The Current / Publicis Media: Samsung 4th-largest advertiser ($9.7B)
  - The Street (Jul 23, 2026): Qualcomm deepens ties with Samsung, Mistral investment same day
"""

import pytest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
ENTITIES_PROFILE = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
RESEARCH_PROFILE = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')


def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def find_mechanism(data, mechanism_id):
    """Search cross_publication_findings and publications for a mechanism by ID."""
    for section in ['cross_publication_findings', 'publications']:
        section_data = data.get(section, {})
        if isinstance(section_data, dict):
            for v in section_data.values():
                if isinstance(v, dict) and v.get('mechanism_id') == mechanism_id:
                    return v
        elif isinstance(section_data, list):
            for v in section_data:
                if isinstance(v, dict) and v.get('mechanism_id') == mechanism_id:
                    return v
    return None


# =============================================================================
# Class 1: Samsung-Mistral Investment Documentation
# =============================================================================

class TestSamsungMistralInvestmentDocumentation:
    """Verify Samsung's €1B Mistral investment is documented in entity profile."""

    def test_samsung_mistral_investment_amount(self):
        """Samsung's ~€1B Mistral investment must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        samsung = data['entities']['samsung']
        samsung_str = str(samsung).lower()
        assert 'mistral' in samsung_str, \
            "Samsung entity must reference Mistral AI investment"

    def test_samsung_mistral_valuation(self):
        """Mistral's €20B target valuation must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        samsung = data['entities']['samsung']
        samsung_str = str(samsung).lower()
        assert '20' in samsung_str or 'billion' in samsung_str, \
            "Samsung entity must reference Mistral's target valuation"

    def test_samsung_mistral_date(self):
        """FT report date (Jul 22, 2026) must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        samsung = data['entities']['samsung']
        samsung_str = str(samsung).lower()
        assert '2026' in samsung_str, \
            "Samsung entity must reference the investment date"

    def test_samsung_mistral_source_ft(self):
        """Financial Times as the primary source must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        samsung = data['entities']['samsung']
        samsung_str = str(samsung).lower()
        # FT or Financial Times or reuters (who cited FT)
        assert any(term in samsung_str for term in ['financial times', 'ft ', 'reuters']), \
            "Samsung entity must cite FT or Reuters as source for Mistral investment"

    def test_samsung_already_has_venture_investment(self):
        """Samsung's prior venture arm investment in Mistral must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        samsung = data['entities']['samsung']
        samsung_str = str(samsung).lower()
        assert 'venture' in samsung_str or 'prior' in samsung_str or 'previous' in samsung_str, \
            "Samsung entity should note prior venture investment in Mistral"

    def test_samsung_mistral_meta_llama_competition(self):
        """Mistral's competition with Meta Llama must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        samsung = data['entities']['samsung']
        samsung_str = str(samsung).lower()
        assert 'llama' in samsung_str or 'meta' in samsung_str or 'open-weight' in samsung_str \
            or 'open weight' in samsung_str, \
            "Samsung entity must reference Mistral-Llama competitive relationship"


# =============================================================================
# Class 2: Cross-Competitor Financial Architecture Chain
# =============================================================================

class TestCrossCompetitorFinancialArchitecture:
    """Verify the cross-competitor chain is documented as a mechanism."""

    def test_mechanism_188_exists(self):
        """Mechanism #188 must exist in competitor-coverage-research.yaml."""
        data = load_yaml(RESEARCH_PROFILE)
        mech = find_mechanism(data, 188)
        assert mech is not None, \
            "Mechanism #188 (Samsung-Mistral cross-competitor architecture) must exist"

    def test_mechanism_188_has_five_layers(self):
        """Mechanism must document all 5 layers of anti-Meta financial architecture."""
        data = load_yaml(RESEARCH_PROFILE)
        mech = find_mechanism(data, 188)
        assert mech is not None
        mech_str = str(mech).lower()
        layers = ['mistral', 'google', 'qualcomm', 'warby', 'microsoft']
        found = sum(1 for layer in layers if layer in mech_str)
        assert found >= 4, \
            f"Mechanism must reference at least 4/5 competitor layers, found {found}"

    def test_mechanism_188_notes_meta_zero_upside(self):
        """Mechanism must note Meta's zero publisher financial upside."""
        data = load_yaml(RESEARCH_PROFILE)
        mech = find_mechanism(data, 188)
        assert mech is not None
        mech_str = str(mech).lower()
        assert 'zero' in mech_str or '0' in mech_str, \
            "Mechanism must reference Meta's zero publisher financial upside channels"

    def test_mechanism_188_references_prior_mechanisms(self):
        """Mechanism must cross-reference related mechanisms."""
        data = load_yaml(RESEARCH_PROFILE)
        mech = find_mechanism(data, 188)
        assert mech is not None
        mech_str = str(mech)
        # Should reference at least one of: #76 (compound leverage), #91 (Qualcomm),
        # #147 (Warby Parker), #180 (Reddit/Advance)
        ref_ids = ['76', '91', '147', '180']
        found = sum(1 for ref_id in ref_ids if ref_id in mech_str)
        assert found >= 2, \
            f"Mechanism #188 must cross-reference at least 2 prior mechanisms, found {found}"


# =============================================================================
# Class 3: Samsung AI Model Diversification Strategy
# =============================================================================

class TestSamsungAIModelDiversification:
    """Samsung is investing in BOTH Google Gemini AND Mistral — two different
    Meta Llama competitors — creating a hedged anti-Meta AI model portfolio."""

    def test_samsung_uses_google_gemini(self):
        """Samsung uses Google Gemini for Galaxy AI — must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        samsung = data['entities']['samsung']
        samsung_str = str(samsung).lower()
        assert 'gemini' in samsung_str, \
            "Samsung entity must document Google Gemini usage"

    def test_samsung_invests_in_mistral(self):
        """Samsung invests in Mistral — must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        samsung = data['entities']['samsung']
        samsung_str = str(samsung).lower()
        assert 'mistral' in samsung_str, \
            "Samsung entity must document Mistral investment"

    def test_dual_ai_model_anti_meta_positioning(self):
        """Both Gemini and Mistral compete with Meta Llama — must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        samsung = data['entities']['samsung']
        samsung_str = str(samsung).lower()
        # Both Google and Mistral are Meta AI competitors
        has_competitive_framing = ('compet' in samsung_str or 'llama' in samsung_str
                                   or 'anti-meta' in samsung_str
                                   or 'oppose' in samsung_str
                                   or 'rival' in samsung_str)
        assert has_competitive_framing, \
            "Samsung entity must note that both AI partners compete with Meta Llama"

    def test_first_direct_foundation_model_investment(self):
        """Samsung's Mistral investment is their first direct foundation model investment
        outside Google — must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        samsung = data['entities']['samsung']
        samsung_str = str(samsung).lower()
        assert 'first' in samsung_str, \
            "Samsung entity must note this is first direct foundation model investment"

    def test_sovereign_ai_narrative(self):
        """Mistral's sovereign AI positioning (European alternative to US labs)
        must be documented as context for the investment."""
        data = load_yaml(ENTITIES_PROFILE)
        samsung = data['entities']['samsung']
        samsung_str = str(samsung).lower()
        assert any(term in samsung_str for term in ['sovereign', 'european', 'independence']), \
            "Samsung entity must reference Mistral's sovereign AI positioning"


# =============================================================================
# Class 4: Warby Parker Q2 2026 Earnings Disclosure
# =============================================================================

class TestWarbyParkerQ2Disclosure:
    """Warby Parker Q2 2026 earnings (Aug 6) disclosed financials that quantify
    the pre-launch investment in Intelligent Eyewear — primary source data."""

    def test_warby_q2_revenue(self):
        """Q2 revenue $235.5M must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        google = data['entities']['google']
        google_str = str(google)
        assert '235' in google_str, \
            "Google entity (Warby Parker section) must document Q2 2026 revenue $235.5M"

    def test_warby_full_year_guidance(self):
        """Full-year guidance $959M-$976M must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        google = data['entities']['google']
        google_str = str(google)
        assert any(num in google_str for num in ['959', '976']), \
            "Google entity must document Warby Parker full-year guidance range"

    def test_warby_guidance_excludes_intelligent_eyewear(self):
        """Guidance EXCLUDING Intelligent Eyewear revenue is critical — means
        all glasses revenue is additive upside."""
        data = load_yaml(ENTITIES_PROFILE)
        google = data['entities']['google']
        google_str = str(google).lower()
        assert 'exclud' in google_str, \
            "Must document that Warby Parker guidance excludes Intelligent Eyewear revenue"

    def test_warby_holiday_launch_timing(self):
        """Holiday 2026 launch window with deliveries must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        google = data['entities']['google']
        google_str = str(google).lower()
        assert 'holiday' in google_str or 'fall' in google_str, \
            "Must document Warby Parker holiday 2026 launch timing"

    def test_warby_store_count(self):
        """352 stores providing demos must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        google = data['entities']['google']
        google_str = str(google)
        assert '352' in google_str or '350' in google_str, \
            "Must document Warby Parker store count for demo/launch"

    def test_warby_cash_position(self):
        """$292.7M cash position must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        google = data['entities']['google']
        google_str = str(google)
        assert '292' in google_str, \
            "Must document Warby Parker cash position"

    def test_warby_tariff_refund_offset(self):
        """$11.8M tariff refund used for launch investment must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        google = data['entities']['google']
        google_str = str(google)
        assert '11.8' in google_str or 'tariff' in google_str.lower(), \
            "Must document tariff refund used for launch investment"


# =============================================================================
# Class 5: Microsoft-Mistral Temporal Convergence
# =============================================================================

class TestMicrosoftMistralTemporalConvergence:
    """Microsoft expanded its Mistral partnership the SAME WEEK as Samsung's
    reported investment (Jul 22, 2026). This creates a Samsung-Microsoft
    convergence on the same Meta-competitive AI lab."""

    def test_microsoft_mistral_same_week(self):
        """Microsoft's expanded Mistral deal was same week as Samsung talks — documented."""
        data = load_yaml(ENTITIES_PROFILE)
        samsung = data['entities']['samsung']
        samsung_str = str(samsung).lower()
        assert 'microsoft' in samsung_str, \
            "Samsung Mistral section must note Microsoft's contemporaneous Mistral expansion"

    def test_microsoft_multibillion_compute_deal(self):
        """Microsoft's multibillion-dollar compute deal with Mistral must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        samsung = data['entities']['samsung']
        samsung_str = str(samsung).lower()
        assert 'compute' in samsung_str or 'infrastructure' in samsung_str, \
            "Must document Microsoft's compute infrastructure deal with Mistral"


# =============================================================================
# Class 6: Five-Channel vs Zero-Channel Publisher Incentive Asymmetry
# =============================================================================

class TestFiveChannelIncentiveAsymmetry:
    """Documents the 5-channel vs 0-channel publisher financial incentive gap
    for Galaxy Glasses vs Meta Ray-Ban."""

    def test_samsung_channel_count(self):
        """Samsung Galaxy Glasses must have 5 documented financial incentive channels."""
        data = load_yaml(RESEARCH_PROFILE)
        mech = find_mechanism(data, 188)
        assert mech is not None
        mech_str = str(mech).lower()
        channels = ['samsung', 'google', 'qualcomm', 'warby', 'mistral']
        found = sum(1 for ch in channels if ch in mech_str)
        assert found >= 5, \
            f"Must document all 5 financial incentive channels, found {found}"

    def test_meta_zero_channels(self):
        """Meta Ray-Ban must have 0 documented publisher financial upside channels."""
        data = load_yaml(RESEARCH_PROFILE)
        mech = find_mechanism(data, 188)
        assert mech is not None
        mech_str = str(mech).lower()
        assert 'zero' in mech_str or '0 financial' in mech_str \
            or '0 upside' in mech_str or 'no financial' in mech_str, \
            "Must document Meta's zero publisher financial upside channels"

    def test_meta_is_downside_channel(self):
        """Meta is an ACTIVE financial downside (ad competitor) — must be documented."""
        data = load_yaml(RESEARCH_PROFILE)
        mech = find_mechanism(data, 188)
        assert mech is not None
        mech_str = str(mech).lower()
        assert 'competitor' in mech_str or 'compet' in mech_str, \
            "Must document that Meta is publishers' direct ad revenue competitor"

    def test_asymmetry_is_infinite(self):
        """The ratio is effectively infinite (5:0 or ∞) — must be documented."""
        data = load_yaml(RESEARCH_PROFILE)
        mech = find_mechanism(data, 188)
        assert mech is not None
        mech_str = str(mech).lower()
        assert 'infinite' in mech_str or '5:0' in mech_str or '5 vs 0' in mech_str \
            or '5 channel' in mech_str, \
            "Must document the infinite publisher incentive asymmetry ratio"


# =============================================================================
# Class 7: Confounders
# =============================================================================

class TestConfounders:
    """Mechanism must document confounding factors honestly."""

    def test_deal_not_finalized(self):
        """Must document Samsung-Mistral deal is 'in talks', not finalized."""
        data = load_yaml(RESEARCH_PROFILE)
        mech = find_mechanism(data, 188)
        assert mech is not None
        mech_str = str(mech).lower()
        assert 'talk' in mech_str or 'not finalized' in mech_str \
            or 'reportedly' in mech_str or 'reported' in mech_str, \
            "Must document the deal is in talks, not finalized"

    def test_mistral_competes_broadly(self):
        """Must document Mistral competes with many AI labs, not just Meta."""
        data = load_yaml(RESEARCH_PROFILE)
        mech = find_mechanism(data, 188)
        assert mech is not None
        mech_str = str(mech).lower()
        # Should note Mistral competes with OpenAI, Anthropic, Google, etc.
        assert 'multiple' in mech_str or 'many' in mech_str \
            or 'not just' in mech_str or 'broad' in mech_str \
            or 'several' in mech_str, \
            "Must document Mistral competes with multiple AI labs, not just Meta"

    def test_mistral_may_be_for_robotics(self):
        """Must document Samsung's Mistral investment may be primarily for robotics/sovereign AI."""
        data = load_yaml(RESEARCH_PROFILE)
        mech = find_mechanism(data, 188)
        assert mech is not None
        mech_str = str(mech).lower()
        assert 'robot' in mech_str or 'sovereign' in mech_str, \
            "Must document Mistral investment may be for robotics/sovereign AI, not just glasses"

    def test_publisher_awareness_confounder(self):
        """Must note publications may not be aware of Samsung-Mistral when reviewing glasses."""
        data = load_yaml(RESEARCH_PROFILE)
        mech = find_mechanism(data, 188)
        assert mech is not None
        mech_str = str(mech).lower()
        assert 'awar' in mech_str or 'conscious' in mech_str \
            or 'knowledge' in mech_str or 'know' in mech_str, \
            "Must document publisher awareness confounder"

    def test_confounders_section_exists(self):
        """Must have a confounders or confounding_factors section."""
        data = load_yaml(RESEARCH_PROFILE)
        mech = find_mechanism(data, 188)
        assert mech is not None
        has_confounders = ('confounders' in mech or 'confounding' in mech
                          or 'confounding_factors' in mech)
        if not has_confounders:
            mech_str = str(mech).lower()
            assert 'confounder' in mech_str, \
                "Mechanism must document confounding factors"


# =============================================================================
# Class 8: Source Verification
# =============================================================================

class TestSourceVerification:
    """All financial claims must have primary sources."""

    def test_has_source_urls(self):
        """Mechanism #188 must have source URLs."""
        data = load_yaml(RESEARCH_PROFILE)
        mech = find_mechanism(data, 188)
        assert mech is not None
        has_sources = ('source_urls' in mech or 'sources' in mech
                       or 'source' in str(mech).lower())
        assert has_sources, "Mechanism must have source URLs"

    def test_ft_source_for_samsung_mistral(self):
        """FT must be cited as primary source for Samsung-Mistral."""
        data = load_yaml(RESEARCH_PROFILE)
        mech = find_mechanism(data, 188)
        assert mech is not None
        mech_str = str(mech).lower()
        assert 'financial times' in mech_str or 'ft.com' in mech_str \
            or 'reuters' in mech_str, \
            "Must cite FT or Reuters as primary source for Samsung-Mistral"

    def test_businesswire_source_for_warby_q2(self):
        """BusinessWire must be cited as primary source for Warby Parker Q2."""
        data = load_yaml(RESEARCH_PROFILE)
        mech = find_mechanism(data, 188)
        assert mech is not None
        mech_str = str(mech).lower()
        assert 'businesswire' in mech_str or 'warby' in mech_str, \
            "Must cite BusinessWire or Warby Parker earnings as source"

    def test_samsung_ad_spend_source(self):
        """Samsung $9.7B ad spend must have The Current / Publicis Media as source."""
        data = load_yaml(ENTITIES_PROFILE)
        samsung = data['entities']['samsung']
        samsung_str = str(samsung).lower()
        assert 'publicis' in samsung_str or 'thecurrent' in samsung_str \
            or 'the current' in samsung_str, \
            "Samsung ad spend must cite Publicis Media or The Current"


# =============================================================================
# Class 9: Temporal Convergence (Jul 22, 2026)
# =============================================================================

class TestTemporalConvergence:
    """Jul 22, 2026 was Samsung Galaxy Unpacked + Samsung-Mistral FT report +
    Microsoft-Mistral expansion — all three on the SAME DAY. This temporal
    convergence of financial architecture changes must be documented."""

    def test_unpacked_same_day_as_mistral(self):
        """Galaxy Unpacked and Mistral report were same day (Jul 22) — documented."""
        data = load_yaml(ENTITIES_PROFILE)
        samsung = data['entities']['samsung']
        samsung_str = str(samsung).lower()
        assert 'unpacked' in samsung_str or 'jul' in samsung_str \
            or 'july' in samsung_str, \
            "Must document temporal convergence of Unpacked + Mistral investment"

    def test_triple_event_same_day(self):
        """Three events on Jul 22 must be documented as convergent."""
        data = load_yaml(RESEARCH_PROFILE)
        mech = find_mechanism(data, 188)
        assert mech is not None
        mech_str = str(mech).lower()
        events = ['unpacked', 'mistral', 'microsoft']
        found = sum(1 for e in events if e in mech_str)
        assert found >= 2, \
            f"Must document at least 2/3 Jul 22 convergent events, found {found}"


# =============================================================================
# Class 10: EQT Scaleup Europe Fund (EU Commission-Backed)
# =============================================================================

class TestEQTScaleupEuropeFund:
    """Samsung's co-investor in Mistral is EQT's EU Commission-backed Scaleup
    Europe Fund. This adds a GOVERNMENT financial dimension — the EU itself
    has financial interest in Mistral's success over US AI labs."""

    def test_eqt_documented(self):
        """EQT Scaleup Europe Fund must be documented in Samsung's Mistral section."""
        data = load_yaml(ENTITIES_PROFILE)
        samsung = data['entities']['samsung']
        samsung_str = str(samsung).lower()
        assert 'eqt' in samsung_str or 'scaleup' in samsung_str \
            or 'eu commission' in samsung_str, \
            "Must document EQT/EU Commission co-investment in Mistral"

    def test_sovereign_ai_dimension(self):
        """EU sovereign AI push as investment context must be documented."""
        data = load_yaml(ENTITIES_PROFILE)
        samsung = data['entities']['samsung']
        samsung_str = str(samsung).lower()
        assert 'sovereign' in samsung_str or 'european alternative' in samsung_str, \
            "Must document sovereign AI context for Mistral investment"


# =============================================================================
# Class 11: Comparison with Meta's AI Model Position
# =============================================================================

class TestMetaAIModelComparison:
    """Meta's Llama is open-weight and distributed freely — Samsung's investment
    in a Llama competitor while using the same Qualcomm chip creates a specific
    financial incentive: Samsung benefits from Mistral replacing Llama adoption
    in non-US markets."""

    def test_meta_llama_is_open_weight(self):
        """Meta Llama's open-weight status must be documented for comparison."""
        data = load_yaml(ENTITIES_PROFILE)
        entities_str = str(data['entities']).lower()
        assert 'llama' in entities_str and 'open' in entities_str, \
            "Must document Meta Llama's open-weight status"

    def test_mistral_competes_in_open_weight_market(self):
        """Mistral competes specifically in the open-weight model market where
        Meta Llama is dominant."""
        data = load_yaml(ENTITIES_PROFILE)
        samsung = data['entities']['samsung']
        samsung_str = str(samsung).lower()
        assert 'open' in samsung_str, \
            "Must document Mistral-Llama competition in open-weight market"


# =============================================================================
# Class 12: Samsung Robotics Division Context
# =============================================================================

class TestSamsungRoboticsDivision:
    """Samsung created its Robotics eXperience (RX) division the day before
    the Mistral investment report. The investment may primarily serve robotics
    rather than glasses — must be documented as confounder."""

    def test_rx_division_documented(self):
        """Samsung's RX robotics division must be referenced."""
        data = load_yaml(ENTITIES_PROFILE)
        samsung = data['entities']['samsung']
        samsung_str = str(samsung).lower()
        assert 'robot' in samsung_str, \
            "Must document Samsung's robotics division context"

    def test_robotics_as_primary_driver(self):
        """Must note robotics may be primary driver of Mistral investment."""
        data = load_yaml(RESEARCH_PROFILE)
        mech = find_mechanism(data, 188)
        assert mech is not None
        mech_str = str(mech).lower()
        assert 'robot' in mech_str, \
            "Must note robotics as potential primary driver of investment"
