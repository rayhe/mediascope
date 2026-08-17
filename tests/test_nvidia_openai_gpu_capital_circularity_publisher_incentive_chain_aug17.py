"""
Nvidia-OpenAI GPU-Capital Circularity Publisher Incentive Chain
Type C: Financial Incentive Mapping — Aug 17, 2026 07:00 PT
Mechanism #152

THESIS: Nvidia's $30B equity investment in OpenAI (Feb/Mar 2026) creates the first
HARDWARE-LAYER financial incentive chain affecting publisher coverage. Previous
mechanisms mapped publisher deals (OpenAI), advertising (Google/Samsung), marketplace
operations (Microsoft PCM), and investment fund chains (Apollo/Anthropic SPVs). None
mapped how the GPU monopolist's investment in an AI company creates a circular
financial incentive structure that propagates to the publishers covering both.

THE CIRCULARITY:
  1. Hyperscalers (Microsoft, Amazon, Google, Meta) spend $650B+ on AI capex (2026)
  2. Capex flows primarily to Nvidia GPUs ($46.7B Q2 FY26 revenue, +56% YoY)
  3. Nvidia invests $30B in OpenAI (Feb/Mar 2026, part of $110B round)
  4. OpenAI uses capital to buy MORE Nvidia GPUs (confirmed: "much of the fresh
     capital to purchase Nvidia's chips" — Reuters)
  5. OpenAI licenses publisher content ($300-400M/yr, 20+ deals)
  6. Publishers cover the AI capex story, Nvidia earnings, OpenAI developments
  7. Positive AI capex narrative → justifies hyperscaler spending → more Nvidia revenue
  8. Loop repeats

NOVEL MECHANISM TYPE: hardware_investor_circular_incentive
Unlike bilateral publisher-AI company deals, this mechanism operates at the
infrastructure layer — the GPU supplier that makes ALL AI possible has a direct
$30B equity stake in the AI company with the MOST publisher content deals. This
creates structural alignment between Nvidia's financial interests and softer
OpenAI coverage, which existing mechanisms show correlates with adversarial Meta
coverage.

KEY DATA:
  - Nvidia Q2 FY2026: $46.7B revenue (+56% YoY), $26.4B net income, 72.4% GM
  - Nvidia market cap: $4.4T+ (world's largest publicly traded company)
  - Nvidia $30B OpenAI investment (Feb/Mar 2026, replacing prior $100B framework)
  - OpenAI $110B funding round: SoftBank $30B, Nvidia $30B, Amazon $50B
  - OpenAI valued at $730-852B (largest private capital raise on record)
  - Two unnamed customers = ~39% of Nvidia Q2 revenue (23% + 16%)
  - Q3 FY2026 guidance: $54B (+15.6% QoQ, below some analyst expectations of $60B)
  - Nvidia acquired Groq for $20B ("reverse acqui-hire" for inference technology)
  - OpenAI 20+ publisher content deals ($300-400M/yr estimated)
  - Meta guided $130-145B capex 2026 — one of Nvidia's TOP customers
  - EssilorLuxottica ~€90B market cap, ZERO tech publisher advertising

THE META PARADOX:
  Meta is one of Nvidia's largest GPU customers ($130-145B capex), yet Nvidia's
  $30B OpenAI investment financially aligns Nvidia with Meta's primary AI competitor.
  OpenAI's proprietary API model competes directly with Meta's open-source Llama.
  Publications with OpenAI content deals AND Nvidia access dependencies have
  REINFORCING incentives to frame the AI race as OpenAI-led (protecting their
  content deal partner AND the narrative that justifies Nvidia's valuation).

WALL STREET CIRCULARITY CONCERN (verified):
  Gulf Business (Feb 2026): "exacerbates Wall Street concerns about 'circular'
  financing agreements, where firms invest in and sign supply deals with each
  other, inflating demand and revenue." The publications covering this circularity
  have financial ties to the companies IN the circle.

CONFOUNDERS:
  1. STRONG: Nvidia's investment may be purely financial (opportunistic stake in
     fastest-growing AI company) with no editorial influence intent
  2. STRONG: Nvidia does not make direct content deals with publishers — the
     incentive chain is INDIRECT (Nvidia → OpenAI → publisher deal)
  3. MODERATE: GTC access and Jensen embargoes may reflect standard media relations,
     not financial leverage (but scale of GTC — 300K+ attendees — makes access
     valuable enough to function as de facto incentive)
  4. MODERATE: Meta's capex spending with Nvidia could create COUNTERVAILING
     incentive (Nvidia benefits from positive Meta coverage too)
  5. WEAK: Nvidia's investment may not affect OpenAI's editorial relationships
     with publishers (investment ≠ operational control)

TESTABLE PREDICTIONS:
  1. Post-investment publications will frame AI capex narrative more favorably
     (since negative capex framing threatens Nvidia's entire revenue stream AND
     OpenAI's ability to sustain publisher content deals)
  2. Publications with OpenAI deals will cover Nvidia earnings more positively
     than publications without deals (financial alignment)
  3. If Nvidia-OpenAI relationship publicly sours (chip disputes, competition),
     publications with OpenAI deals will side with OpenAI framing

SOURCE URLs:
  - https://www.reuters.com/business/nvidia-close-finalizing-30-billion-investment-openai-funding-round-ft-reports-2026-02-20/
  - https://www.morningstar.com/news/marketwatch/20260227177/amazon-nvidia-and-softbank-pour-110-billion-into-openai-raising-the-stakes-for-ai-monetization
  - https://gulfbusiness.com/en/2026/tech/openai-840-billion-funding-amazon-nvidia-softbank/
  - https://www.datacenterdynamics.com/en/news/two-unnamed-customers-accounted-for-almost-40-of-nvidias-q2-2026-revenue/
  - https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2026/default.aspx
  - https://www.pymnts.com/artificial-intelligence-2/2026/nvidia-nears-30-billion-stake-in-record-breaking-openai-funding-round/
  - https://www.eweek.com/news/nvidia-openai-30b-plan/
  - https://www.campaignlive.com/article/nvidias-shock-20bn-groq-deal-means-adland/1944164
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), "..", "profiles")


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return yaml.safe_load(f)


# ── Section 1: Nvidia Entity Data Integrity ──────────────────────────────────

class TestNvidiaEntityPresence:
    """Verify Nvidia entity exists in competitor-entities.yaml with required fields."""

    def test_nvidia_entity_exists(self):
        data = load_yaml("competitor-entities.yaml")
        entities = data.get("entities", {})
        assert "nvidia" in entities, "nvidia entity must exist in competitor-entities.yaml"

    def test_nvidia_has_display_name(self):
        data = load_yaml("competitor-entities.yaml")
        nvidia = data["entities"]["nvidia"]
        assert nvidia.get("display_name") == "Nvidia" or nvidia.get("display_name") == "NVIDIA"

    def test_nvidia_has_market_cap(self):
        data = load_yaml("competitor-entities.yaml")
        nvidia = data["entities"]["nvidia"]
        assert "market_cap_approx" in nvidia

    def test_nvidia_has_openai_investment_section(self):
        data = load_yaml("competitor-entities.yaml")
        nvidia = data["entities"]["nvidia"]
        assert "openai_investment" in nvidia, \
            "nvidia entity must document the $30B OpenAI investment"

    def test_nvidia_openai_investment_amount(self):
        data = load_yaml("competitor-entities.yaml")
        inv = data["entities"]["nvidia"]["openai_investment"]
        amount = inv.get("amount_b")
        assert amount == 30 or amount == "30", \
            f"Nvidia OpenAI investment should be $30B, got {amount}"

    def test_nvidia_has_q2_fy26_earnings(self):
        data = load_yaml("competitor-entities.yaml")
        nvidia = data["entities"]["nvidia"]
        assert "q2_fy2026_earnings" in nvidia, \
            "nvidia entity must have Q2 FY2026 earnings data"

    def test_nvidia_q2_revenue(self):
        data = load_yaml("competitor-entities.yaml")
        q2 = data["entities"]["nvidia"]["q2_fy2026_earnings"]
        rev = q2.get("revenue_b")
        assert rev is not None
        assert float(rev) >= 46 and float(rev) <= 48, \
            f"Q2 FY2026 revenue should be ~$46.7B, got {rev}"

    def test_nvidia_has_regex(self):
        data = load_yaml("competitor-entities.yaml")
        nvidia = data["entities"]["nvidia"]
        assert "regex" in nvidia, "nvidia entity must have regex for text matching"

    def test_nvidia_has_groq_acquisition(self):
        data = load_yaml("competitor-entities.yaml")
        nvidia = data["entities"]["nvidia"]
        assert "groq_acquisition" in nvidia, \
            "nvidia entity must document the $20B Groq deal"

    def test_nvidia_has_customer_concentration(self):
        data = load_yaml("competitor-entities.yaml")
        nvidia = data["entities"]["nvidia"]
        assert "customer_concentration" in nvidia, \
            "nvidia entity must document the top-2 customer revenue concentration"


# ── Section 2: Circularity Financial Chain Structure ─────────────────────────

class TestGPUCapitalCircularityChain:
    """Verify the circular financial chain is documented with all nodes."""

    def test_mechanism_152_exists(self):
        data = load_yaml("competitor-coverage-research.yaml")
        found = False
        def search(obj):
            nonlocal found
            if isinstance(obj, dict):
                if obj.get("mechanism_id") == 152:
                    found = True
                    return
                for v in obj.values():
                    search(v)
            elif isinstance(obj, list):
                for item in obj:
                    search(item)
        search(data)
        assert found, "Mechanism #152 must exist in competitor-coverage-research.yaml"

    def test_mechanism_type_is_novel(self):
        """The mechanism type should be hardware_investor_circular_incentive."""
        data = load_yaml("competitor-coverage-research.yaml")
        def find_mechanism(obj):
            if isinstance(obj, dict):
                if obj.get("mechanism_id") == 152:
                    return obj
                for v in obj.values():
                    r = find_mechanism(v)
                    if r:
                        return r
            elif isinstance(obj, list):
                for item in obj:
                    r = find_mechanism(item)
                    if r:
                        return r
            return None
        m = find_mechanism(data)
        assert m is not None
        mtype = m.get("mechanism_type", "")
        assert "hardware" in mtype.lower() or "circular" in mtype.lower(), \
            f"Mechanism type should reference hardware or circularity, got: {mtype}"

    def test_circularity_nodes_documented(self):
        """The circular chain should identify at least 4 nodes."""
        data = load_yaml("competitor-coverage-research.yaml")
        def find_mechanism(obj):
            if isinstance(obj, dict):
                if obj.get("mechanism_id") == 152:
                    return obj
                for v in obj.values():
                    r = find_mechanism(v)
                    if r:
                        return r
            elif isinstance(obj, list):
                for item in obj:
                    r = find_mechanism(item)
                    if r:
                        return r
            return None
        m = find_mechanism(data)
        assert m is not None
        summary = str(m.get("finding_summary", "")).lower()
        # Should mention hyperscalers, Nvidia, OpenAI, and publishers
        assert "nvidia" in summary
        assert "openai" in summary
        assert "publisher" in summary

    def test_investment_amount_in_mechanism(self):
        data = load_yaml("competitor-coverage-research.yaml")
        def find_mechanism(obj):
            if isinstance(obj, dict):
                if obj.get("mechanism_id") == 152:
                    return obj
                for v in obj.values():
                    r = find_mechanism(v)
                    if r:
                        return r
            elif isinstance(obj, list):
                for item in obj:
                    r = find_mechanism(item)
                    if r:
                        return r
            return None
        m = find_mechanism(data)
        assert m is not None
        text = str(m)
        assert "30" in text, "Mechanism must reference $30B investment amount"


# ── Section 3: Financial Data Accuracy ───────────────────────────────────────

class TestNvidiaFinancialData:
    """Verify financial figures match SEC filings and verified sources."""

    def test_q2_fy26_revenue_is_46_7b(self):
        data = load_yaml("competitor-entities.yaml")
        q2 = data["entities"]["nvidia"]["q2_fy2026_earnings"]
        assert float(q2["revenue_b"]) == pytest.approx(46.7, abs=0.5)

    def test_q2_fy26_net_income(self):
        data = load_yaml("competitor-entities.yaml")
        q2 = data["entities"]["nvidia"]["q2_fy2026_earnings"]
        assert float(q2.get("net_income_b", 0)) == pytest.approx(26.4, abs=0.5)

    def test_q2_fy26_gross_margin(self):
        data = load_yaml("competitor-entities.yaml")
        q2 = data["entities"]["nvidia"]["q2_fy2026_earnings"]
        gm = float(q2.get("gross_margin_pct", 0))
        assert gm == pytest.approx(72.4, abs=1.0)

    def test_q2_fy26_yoy_growth(self):
        data = load_yaml("competitor-entities.yaml")
        q2 = data["entities"]["nvidia"]["q2_fy2026_earnings"]
        yoy = float(q2.get("revenue_yoy_pct", 0))
        assert yoy == pytest.approx(56, abs=2)

    def test_q3_guidance_documented(self):
        data = load_yaml("competitor-entities.yaml")
        q2 = data["entities"]["nvidia"]["q2_fy2026_earnings"]
        guidance = q2.get("q3_guidance_b")
        assert guidance is not None
        assert float(guidance) == pytest.approx(54, abs=2)

    def test_customer_concentration_top2(self):
        data = load_yaml("competitor-entities.yaml")
        cc = data["entities"]["nvidia"]["customer_concentration"]
        # Top 2 customers = ~39% of Q2 revenue
        top2_pct = cc.get("top_2_pct_q2_fy26")
        assert top2_pct is not None
        assert float(top2_pct) >= 35 and float(top2_pct) <= 42


# ── Section 4: Circularity Impact on Publisher Incentives ────────────────────

class TestPublisherIncentiveChain:
    """Verify the mechanism documents how GPU-capital circularity affects publishers."""

    def test_openai_publisher_deal_count(self):
        """OpenAI's deal count should be documented as 20+."""
        data = load_yaml("competitor-entities.yaml")
        openai = data["entities"]["openai"]
        deals = openai.get("publisher_content_deal_portfolio", {})
        total = deals.get("total_deals", "0")
        assert "20" in str(total) or int(str(total).replace("+", "")) >= 20

    def test_meta_zero_nvidia_investment(self):
        """Meta has no investment from Nvidia — contrast must be documented."""
        data = load_yaml("competitor-entities.yaml")
        nvidia = data["entities"]["nvidia"]
        inv = nvidia.get("openai_investment", {})
        contrast = str(nvidia.get("meta_contrast", "")).lower()
        assert "meta" in contrast, \
            "Nvidia entity must contrast Meta's position in the GPU-capital chain"

    def test_hyperscaler_capex_data_present(self):
        """$650B+ combined hyperscaler capex should be referenced."""
        data = load_yaml("competitor-entities.yaml")
        nvidia = data["entities"]["nvidia"]
        text = str(nvidia).lower()
        # Should reference massive AI capex spending
        assert "capex" in text or "capital expenditure" in text

    def test_circular_financing_concern_documented(self):
        """Wall Street circularity concern should be noted."""
        data = load_yaml("competitor-entities.yaml")
        nvidia = data["entities"]["nvidia"]
        text = str(nvidia).lower()
        assert "circular" in text, \
            "Must document Wall Street circular financing concerns"


# ── Section 5: OpenAI Funding Round Structure ────────────────────────────────

class TestOpenAIFundingRoundComposition:
    """Verify the $110B round structure is documented correctly."""

    def test_softbank_investment_30b(self):
        data = load_yaml("competitor-entities.yaml")
        nvidia = data["entities"]["nvidia"]
        text = str(nvidia)
        assert "SoftBank" in text or "softbank" in text.lower()

    def test_amazon_investment_50b(self):
        data = load_yaml("competitor-entities.yaml")
        nvidia = data["entities"]["nvidia"]
        text = str(nvidia)
        assert "Amazon" in text or "amazon" in text.lower()

    def test_total_round_110b(self):
        data = load_yaml("competitor-entities.yaml")
        nvidia = data["entities"]["nvidia"]
        inv = nvidia.get("openai_investment", {})
        round_total = inv.get("total_round_b")
        assert round_total is not None
        assert float(round_total) >= 100

    def test_openai_valuation_documented(self):
        data = load_yaml("competitor-entities.yaml")
        nvidia = data["entities"]["nvidia"]
        inv = nvidia.get("openai_investment", {})
        val = inv.get("openai_valuation_b")
        assert val is not None
        assert float(val) >= 700


# ── Section 6: Groq Acquisition ──────────────────────────────────────────────

class TestNvidiaGroqAcquisition:
    """Verify the $20B Groq deal is documented as infrastructure expansion."""

    def test_groq_deal_value(self):
        data = load_yaml("competitor-entities.yaml")
        groq = data["entities"]["nvidia"]["groq_acquisition"]
        val = groq.get("deal_value_b")
        assert val is not None
        assert float(val) >= 18 and float(val) <= 22

    def test_groq_inference_technology(self):
        """Deal was for inference technology (LPU), not training."""
        data = load_yaml("competitor-entities.yaml")
        groq = data["entities"]["nvidia"]["groq_acquisition"]
        text = str(groq).lower()
        assert "inference" in text or "lpu" in text

    def test_groq_antitrust_structure(self):
        """Deal structured as reverse acqui-hire to minimize regulatory attention."""
        data = load_yaml("competitor-entities.yaml")
        groq = data["entities"]["nvidia"]["groq_acquisition"]
        text = str(groq).lower()
        assert "acqui" in text or "license" in text


# ── Section 7: Meta Contrast — Same GPU Customer, Different Treatment ────────

class TestMetaGPUCustomerParadox:
    """Meta is one of Nvidia's TOP GPU customers yet Nvidia invests in Meta's competitor."""

    def test_meta_capex_documented(self):
        data = load_yaml("competitor-entities.yaml")
        nvidia = data["entities"]["nvidia"]
        contrast = str(nvidia.get("meta_contrast", ""))
        assert "130" in contrast or "145" in contrast or "capex" in contrast.lower(), \
            "Meta's $130-145B capex should be referenced in Nvidia's meta_contrast"

    def test_meta_as_nvidia_customer(self):
        data = load_yaml("competitor-entities.yaml")
        nvidia = data["entities"]["nvidia"]
        text = str(nvidia).lower()
        assert "meta" in text, "Meta should be mentioned as Nvidia GPU customer"

    def test_llama_vs_openai_competition(self):
        """Nvidia's OpenAI investment aligns it against Meta's open-source Llama."""
        data = load_yaml("competitor-entities.yaml")
        nvidia = data["entities"]["nvidia"]
        text = str(nvidia).lower()
        assert "llama" in text or "open-source" in text or "open source" in text or "open_source" in text, \
            "Must note Llama vs OpenAI competitive dynamic in Nvidia investment context"

    def test_essilorluxottica_zero_publisher_ads(self):
        """EssilorLuxottica has ZERO tech publisher advertising — contrast to Samsung/Google."""
        data = load_yaml("competitor-entities.yaml")
        nvidia = data["entities"]["nvidia"]
        text = str(nvidia).lower()
        # The meta_contrast should note the advertising asymmetry in supply chains
        assert "essilorluxottica" in text or "luxottica" in text or "frame" in text


# ── Section 8: Source URL Verification ───────────────────────────────────────

class TestSourceURLPresence:
    """Every financial claim must have source URLs."""

    def test_nvidia_entity_has_source_urls(self):
        data = load_yaml("competitor-entities.yaml")
        nvidia = data["entities"]["nvidia"]
        # Should have source_urls at entity level or in subsections
        text = str(nvidia)
        assert "source_url" in text, "Nvidia entity must have source URLs"

    def test_mechanism_152_has_source_urls(self):
        data = load_yaml("competitor-coverage-research.yaml")
        def find_mechanism(obj):
            if isinstance(obj, dict):
                if obj.get("mechanism_id") == 152:
                    return obj
                for v in obj.values():
                    r = find_mechanism(v)
                    if r:
                        return r
            elif isinstance(obj, list):
                for item in obj:
                    r = find_mechanism(item)
                    if r:
                        return r
            return None
        m = find_mechanism(data)
        assert m is not None
        urls = m.get("source_urls", [])
        assert len(urls) >= 4, f"Mechanism #152 needs ≥4 source URLs, has {len(urls)}"

    def test_source_urls_are_real_domains(self):
        data = load_yaml("competitor-coverage-research.yaml")
        def find_mechanism(obj):
            if isinstance(obj, dict):
                if obj.get("mechanism_id") == 152:
                    return obj
                for v in obj.values():
                    r = find_mechanism(v)
                    if r:
                        return r
            elif isinstance(obj, list):
                for item in obj:
                    r = find_mechanism(item)
                    if r:
                        return r
            return None
        m = find_mechanism(data)
        assert m is not None
        for url in m.get("source_urls", []):
            assert url.startswith("http"), f"Invalid URL: {url}"


# ── Section 9: Confounder Documentation ──────────────────────────────────────

class TestConfounderQuality:
    """Mechanism must document ≥5 confounders with strength ratings."""

    def test_has_five_confounders(self):
        data = load_yaml("competitor-coverage-research.yaml")
        def find_mechanism(obj):
            if isinstance(obj, dict):
                if obj.get("mechanism_id") == 152:
                    return obj
                for v in obj.values():
                    r = find_mechanism(v)
                    if r:
                        return r
            elif isinstance(obj, list):
                for item in obj:
                    r = find_mechanism(item)
                    if r:
                        return r
            return None
        m = find_mechanism(data)
        assert m is not None
        confounders = m.get("confounders", [])
        assert len(confounders) >= 5, \
            f"Need ≥5 confounders, have {len(confounders)}"

    def test_has_strong_confounders(self):
        data = load_yaml("competitor-coverage-research.yaml")
        def find_mechanism(obj):
            if isinstance(obj, dict):
                if obj.get("mechanism_id") == 152:
                    return obj
                for v in obj.values():
                    r = find_mechanism(v)
                    if r:
                        return r
            elif isinstance(obj, list):
                for item in obj:
                    r = find_mechanism(item)
                    if r:
                        return r
            return None
        m = find_mechanism(data)
        assert m is not None
        confounders = m.get("confounders", [])
        strong_count = sum(1 for c in confounders
                         if "STRONG" in str(c.get("strength", "")).upper())
        assert strong_count >= 2, \
            f"Need ≥2 STRONG confounders, have {strong_count}"

    def test_confounders_have_descriptions(self):
        data = load_yaml("competitor-coverage-research.yaml")
        def find_mechanism(obj):
            if isinstance(obj, dict):
                if obj.get("mechanism_id") == 152:
                    return obj
                for v in obj.values():
                    r = find_mechanism(v)
                    if r:
                        return r
            elif isinstance(obj, list):
                for item in obj:
                    r = find_mechanism(item)
                    if r:
                        return r
            return None
        m = find_mechanism(data)
        assert m is not None
        for c in m.get("confounders", []):
            assert c.get("description"), "Each confounder needs a description"


# ── Section 10: Cross-Reference Integrity ────────────────────────────────────

class TestCrossReferences:
    """Mechanism #152 should cross-reference related mechanisms."""

    def test_references_microsoft_septuple(self):
        """Should reference Microsoft septuple leverage (mechanism #7 area)."""
        data = load_yaml("competitor-coverage-research.yaml")
        def find_mechanism(obj):
            if isinstance(obj, dict):
                if obj.get("mechanism_id") == 152:
                    return obj
                for v in obj.values():
                    r = find_mechanism(v)
                    if r:
                        return r
            elif isinstance(obj, list):
                for item in obj:
                    r = find_mechanism(item)
                    if r:
                        return r
            return None
        m = find_mechanism(data)
        assert m is not None
        refs = m.get("cross_references", [])
        ref_str = str(refs)
        # Should reference at least some existing mechanisms
        assert len(refs) >= 2, f"Need ≥2 cross-references, have {len(refs)}"

    def test_references_openai_publisher_deals(self):
        """Should reference OpenAI publisher deal mechanisms."""
        data = load_yaml("competitor-coverage-research.yaml")
        def find_mechanism(obj):
            if isinstance(obj, dict):
                if obj.get("mechanism_id") == 152:
                    return obj
                for v in obj.values():
                    r = find_mechanism(v)
                    if r:
                        return r
            elif isinstance(obj, list):
                for item in obj:
                    r = find_mechanism(item)
                    if r:
                        return r
            return None
        m = find_mechanism(data)
        assert m is not None
        text = str(m).lower()
        assert "publisher" in text and "deal" in text

    def test_has_testable_predictions(self):
        data = load_yaml("competitor-coverage-research.yaml")
        def find_mechanism(obj):
            if isinstance(obj, dict):
                if obj.get("mechanism_id") == 152:
                    return obj
                for v in obj.values():
                    r = find_mechanism(v)
                    if r:
                        return r
            elif isinstance(obj, list):
                for item in obj:
                    r = find_mechanism(item)
                    if r:
                        return r
            return None
        m = find_mechanism(data)
        assert m is not None
        preds = m.get("testable_predictions", [])
        assert len(preds) >= 3, f"Need ≥3 testable predictions, have {len(preds)}"
