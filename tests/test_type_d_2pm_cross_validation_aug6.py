"""
Type D Cross-Validation — Aug 6, 2026 2:00 PM PT
Validates data consistency across afternoon iterations:
  - 11:00 Type A: MIT TR × Apple governance conflict
  - 12:00 Type B: Christopher Mims / WSJ cross-entity & disclosure
  - 13:00 Type C: Google advertising dependency coercion

Cross-checks:
1. Sensor-count paradox: MIT TR (11:00) should be consistent with
   existing WIRED/FT paradox data in competitor-coverage-research.yaml
2. WSJ balanced control (12:00) should reinforce aggregate findings
3. Google coercion structure (13:00) should be consistent with
   Condé Nast traffic data added to WIRED section
4. NYT Q2 2026 earnings (13:00) should match nytimes.yaml profile data
5. Cross-track: advertising dependency paradox should reference
   the same Condé Nast data as WIRED google_traffic_collapse
6. Mims tone inversion direction should be opposite from WIRED journalists
"""

import os
import pathlib
import yaml
import pytest

_REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
_PROFILES = _REPO_ROOT / "profiles"


def _load(name):
    with open(_PROFILES / name) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def research():
    return _load("competitor-coverage-research.yaml")


@pytest.fixture(scope="module")
def entities():
    return _load("competitor-entities.yaml")


@pytest.fixture(scope="module")
def news_corp():
    return _load("news-corp.yaml")


@pytest.fixture(scope="module")
def nytimes():
    return _load("nytimes.yaml")


@pytest.fixture(scope="module")
def mit_tr():
    return _load("mit-tech-review.yaml")


# ===================================================================
# Class 1: Sensor-Count Paradox Cross-Publication Consistency
# ===================================================================

class TestSensorCountParadoxConsistency:
    """MIT TR (11:00 addition) should be the THIRD publication with
    sensor-count paradox after WIRED and FT."""

    def test_mit_tr_apple_coverage_in_research(self, research):
        mittr = research["publications"]["mit-tech-review"]
        assert "apple_coverage_tone" in mittr

    def test_mit_tr_apple_tone_positive(self, research):
        mittr = research["publications"]["mit-tech-review"]
        assert mittr["apple_coverage_tone"] == "positive"

    def test_mit_tr_meta_tone_adversarial(self, research):
        mittr = research["publications"]["mit-tech-review"]
        assert mittr["meta_coverage_tone"] == "adversarial"

    def test_mit_tr_apple_coverage_mentions_governance(self, research):
        mittr = research["publications"]["mit-tech-review"]
        apple_summary = mittr["apple_coverage_summary"]
        assert "bergeron" in apple_summary.lower() or "governance" in apple_summary.lower()

    def test_wired_also_has_meta_adversarial(self, research):
        """WIRED should match MIT TR's meta tone direction."""
        wired = research["publications"]["wired"]
        assert wired["meta_coverage_tone"] == "adversarial"

    def test_wired_openai_not_adversarial(self, research):
        """WIRED's OpenAI tone should differ from Meta tone."""
        wired = research["publications"]["wired"]
        assert wired["openai_coverage_tone"] != "adversarial"

    def test_sensor_paradox_not_just_one_pub(self, research):
        """At least 2 publications should show adversarial Meta + positive Apple."""
        count = 0
        for pub_key, pub in research["publications"].items():
            meta_tone = pub.get("meta_coverage_tone", "")
            apple_tone = pub.get("apple_coverage_tone", "")
            if "adversarial" in meta_tone and "positive" in apple_tone:
                count += 1
        assert count >= 2, f"Only {count} publications show sensor-count paradox pattern"


# ===================================================================
# Class 2: WSJ Balanced Control ↔ Aggregate Findings Consistency
# ===================================================================

class TestWSJBalancedControlAggregate:
    """Mims data (12:00) should reinforce the News Corp balanced
    control finding already in aggregate_findings."""

    def test_aggregate_has_news_corp_control(self, research):
        key_ev = research["aggregate_findings"]["key_evidence"]
        findings = [e["finding"] for e in key_ev]
        assert any("news corp" in f.lower() for f in findings), \
            f"Aggregate findings missing News Corp control: {findings}"

    def test_news_corp_has_journalist_profiles(self, news_corp):
        assert "journalist_profiles" in news_corp

    def test_mims_in_journalist_profiles(self, news_corp):
        jp = news_corp["journalist_profiles"]
        names = [j.get("name", "") for j in jp] if isinstance(jp, list) else list(jp.keys())
        assert any("mims" in n.lower() for n in names)

    def test_news_corp_control_designation_exists(self, news_corp):
        assert "control_designation" in news_corp

    def test_news_corp_has_both_deals(self, news_corp):
        """News Corp should have both Meta and OpenAI deals documented."""
        rev = news_corp.get("revenue_relationships", {})
        rev_text = str(rev).lower()
        assert "meta" in rev_text
        assert "openai" in rev_text

    def test_mims_meta_tone_positive_direction(self, research):
        """Mims should show positive/constructive Meta tone (opposite WIRED)."""
        nc = research["publications"]["news-corp"]
        mims = nc.get("mims_cross_entity", {})
        desc = mims.get("description", "").lower()
        assert "+0.3" in desc or "constructive" in desc or "positive" in desc or "softer on meta" in desc


# ===================================================================
# Class 3: Google Coercion ↔ Condé Nast Traffic Data Consistency
# ===================================================================

class TestGoogleCoercionCondeNastConsistency:
    """Google coercion structure (13:00 Type C) should be consistent
    with Condé Nast traffic collapse data added to WIRED section."""

    def test_google_entity_has_coercion(self, entities):
        google = entities["entities"]["google"]
        assert "advertising_dependency_coercion" in google

    def test_coercion_has_four_layers(self, entities):
        coercion = entities["entities"]["google"]["advertising_dependency_coercion"]
        assert len(coercion["layers"]) == 4

    def test_coercion_meta_contrast_present(self, entities):
        coercion = entities["entities"]["google"]["advertising_dependency_coercion"]
        assert coercion.get("meta_contrast") is not None

    def test_wired_google_traffic_collapse(self, research):
        """WIRED section should have google_traffic_collapse from 13:00."""
        wired = research["publications"]["wired"]
        assert "google_traffic_collapse" in wired

    def test_wired_traffic_collapse_mentions_25pct(self, research):
        wired = research["publications"]["wired"]
        desc = wired["google_traffic_collapse"].get("description", "")
        assert "25%" in desc or "25 percent" in desc.lower()

    def test_advertising_paradox_exists(self, research):
        wired = research["publications"]["wired"]
        assert "advertising_dependency_paradox" in wired

    def test_paradox_references_zero_meta_leverage(self, research):
        wired = research["publications"]["wired"]
        paradox = wired["advertising_dependency_paradox"]
        desc = paradox.get("description", "").lower()
        assert "zero" in desc and "meta" in desc

    def test_coercion_search_traffic_layer_exists(self, entities):
        coercion = entities["entities"]["google"]["advertising_dependency_coercion"]
        layer_names = [l.get("name", "").lower() for l in coercion["layers"]]
        assert any("search" in n or "traffic" in n for n in layer_names), \
            f"No search/traffic layer in: {layer_names}"


# ===================================================================
# Class 4: NYT Q2 2026 Profile ↔ Research Data Consistency
# ===================================================================

class TestNYTQ2EarningsConsistency:
    """NYT Q2 2026 data in nytimes.yaml should match research file data.
    Note: sec_filings is nested under ownership_chain[1], not top-level."""

    @staticmethod
    def _get_q2_filing(nytimes):
        """Navigate to sec_filings via ownership_chain."""
        oc = nytimes.get("ownership_chain", [])
        for entry in oc:
            if isinstance(entry, dict):
                filings = entry.get("sec_filings", [])
                for f in filings:
                    if "Q2 2026" in str(f.get("period", "")):
                        return f
        return None

    def test_nyt_profile_has_q2_2026_filing(self, nytimes):
        """nytimes.yaml should have Q2 2026 10-Q entry."""
        q2 = self._get_q2_filing(nytimes)
        assert q2 is not None, "No Q2 2026 filing in nytimes.yaml"

    def test_nyt_q2_revenue_762(self, nytimes):
        """Q2 revenue should be $762.5M in profile."""
        q2 = self._get_q2_filing(nytimes)
        assert q2 is not None, "No Q2 2026 filing"
        notes = q2.get("notes", "")
        assert "762" in notes

    def test_nyt_q2_stock_crash(self, nytimes):
        """Q2 stock decline should be documented."""
        q2 = self._get_q2_filing(nytimes)
        assert q2 is not None, "No Q2 2026 filing"
        notes = q2.get("notes", "")
        assert "13%" in notes or "plunged" in notes.lower()

    def test_nyt_q2_levien_quote_in_profile(self, nytimes):
        """CEO Levien traffic quote should be in profile."""
        q2 = self._get_q2_filing(nytimes)
        assert q2 is not None, "No Q2 2026 filing"
        notes = q2.get("notes", "")
        assert "levien" in notes.lower() or "traffic" in notes.lower()

    def test_research_paradox_cites_nyt_q2(self, research):
        """Advertising dependency paradox should reference NYT Q2 data."""
        wired = research["publications"]["wired"]
        paradox = wired["advertising_dependency_paradox"]
        desc = paradox.get("description", "")
        assert "NYT" in desc or "nyt" in desc.lower() or "New York Times" in desc


# ===================================================================
# Class 5: Mims Tone Inversion ↔ WIRED Direction Check
# ===================================================================

class TestMimsToneInversion:
    """Mims should show OPPOSITE tone direction from WIRED journalists."""

    def test_wired_meta_negative(self, research):
        wired = research["publications"]["wired"]
        assert wired["meta_coverage_tone"] == "adversarial"

    def test_wired_openai_positive(self, research):
        wired = research["publications"]["wired"]
        tone = wired["openai_coverage_tone"]
        assert tone in ("neutral_to_positive", "positive", "neutral")

    def test_mims_meta_positive_direction(self, research):
        """Mims Meta coverage should be constructive (opposite WIRED)."""
        nc = research["publications"]["news-corp"]
        mims = nc["mims_cross_entity"]
        desc = mims.get("description", "").lower()
        # Mims should be described as positive/constructive on Meta
        assert any(w in desc for w in ["constructive", "+0.3", "softer on meta", "balanced_to_constructive"])

    def test_mims_openai_skeptical(self, research):
        """Mims OpenAI coverage should be skeptical (opposite WIRED)."""
        nc = research["publications"]["news-corp"]
        mims = nc["mims_cross_entity"]
        desc = mims.get("description", "").lower()
        assert any(w in desc for w in ["skeptical", "-0.3", "critical"])

    def test_tone_gap_direction_opposite(self, research):
        """WIRED gap: Meta(-) OpenAI(+). Mims gap: Meta(+) OpenAI(-).
        The directions should be opposite."""
        # WIRED: adversarial Meta, neutral_to_positive OpenAI
        wired = research["publications"]["wired"]
        wired_meta = wired["meta_coverage_tone"]
        wired_openai = wired["openai_coverage_tone"]
        # Mims: constructive Meta, skeptical OpenAI
        nc = research["publications"]["news-corp"]
        mims_desc = nc["mims_cross_entity"]["description"].lower()
        # WIRED is Meta-negative, Mims is Meta-positive
        assert wired_meta == "adversarial"
        assert "constructive" in mims_desc or "+0.3" in mims_desc


# ===================================================================
# Class 6: WSJ Disclosure ↔ Other Publications Non-Disclosure
# ===================================================================

class TestWSJDisclosureUniqueness:
    """WSJ should be the ONLY publication with systematic disclosure."""

    def test_disclosure_practice_in_profile(self, news_corp):
        dp = news_corp["disclosure_practice"]
        assert dp["unique_in_dataset"] is True

    def test_at_least_5_reporters_observed(self, news_corp):
        dp = news_corp["disclosure_practice"]
        assert len(dp["observed_reporters"]) >= 5

    def test_meta_disclosure_text_present(self, news_corp):
        dp = news_corp["disclosure_practice"]
        assert "News Corp" in dp.get("meta_disclosure_text", "")

    def test_openai_disclosure_text_present(self, news_corp):
        dp = news_corp["disclosure_practice"]
        assert dp.get("openai_disclosure_text") is not None

    def test_research_documents_disclosure(self, research):
        nc = research["publications"]["news-corp"]
        assert "wsj_disclosure_practice" in nc

    def test_disclosure_irony_documented(self, research):
        """The irony that least-biased pub is only one that discloses."""
        nc = research["publications"]["news-corp"]
        desc = nc["wsj_disclosure_practice"]["description"].lower()
        assert "irony" in desc or "only" in desc


# ===================================================================
# Class 7: Google Network Revenue ↔ Coercion Structural Integrity
# ===================================================================

class TestGoogleRevenueCoercionLink:
    """Network revenue decline data should support the coercion thesis."""

    def test_network_revenue_q2_present(self, entities):
        google = entities["entities"]["google"]
        nrd = google["network_revenue_decline"]
        assert "q2_2026_network_revenue_b" in nrd

    def test_network_revenue_declining(self, entities):
        google = entities["entities"]["google"]
        nrd = google["network_revenue_decline"]
        # Q2 should show decline
        q2_yoy = nrd.get("q2_2026_network_yoy_pct", 0)
        # Should be negative (decline)
        assert float(str(q2_yoy).replace('%', '')) < 0

    def test_total_google_ad_growing(self, entities):
        google = entities["entities"]["google"]
        nrd = google["network_revenue_decline"]
        total_yoy = nrd.get("q2_2026_total_google_ad_yoy_pct", 0)
        assert float(str(total_yoy).replace('%', '').replace('+', '')) > 0

    def test_divergence_documented(self, entities):
        """Network declining while total grows = Google squeezing publishers."""
        google = entities["entities"]["google"]
        nrd = google["network_revenue_decline"]
        desc = nrd.get("description", "").lower()
        # Should mention the divergence or squeeze
        assert any(w in desc for w in ["decline", "shrink", "squeeze", "publisher", "all-time low"])

    def test_coercion_references_ad_dependency(self, entities):
        google = entities["entities"]["google"]
        coercion = google["advertising_dependency_coercion"]
        layer_names = [l.get("name", "").lower() for l in coercion["layers"]]
        assert any("advertising" in n or "ad" in n for n in layer_names)


# ===================================================================
# Class 8: MIT TR Governance ↔ Competitor-Entities Apple Consistency
# ===================================================================

class TestMITTRGovernanceAppleEntity:
    """MIT TR's Apple governance conflict should reference the Apple
    entity and be documented in MIT TR's competitor_relationships."""

    def test_apple_in_competitor_entities(self, entities):
        assert "apple" in entities["entities"]

    def test_mit_tr_has_apple_competitor_relationship(self, mit_tr):
        cr = mit_tr["competitor_relationships"]
        assert "apple" in cr

    def test_mit_tr_apple_relationship_has_governance(self, mit_tr):
        apple = mit_tr["competitor_relationships"]["apple"]
        txt = str(apple).lower()
        assert "bergeron" in txt or "governance" in txt or "corporation" in txt or \
               "board" in txt or "csail" in txt
        # Also verify financial_tie is valid schema type
        assert apple["financial_tie"] in ("indirect", "governance", "none")

    def test_mit_tr_apple_not_disclosed(self, research):
        """MIT TR should NOT disclose Apple connections."""
        mittr = research["publications"]["mit-tech-review"]
        apple_summary = mittr.get("apple_coverage_summary", "")
        assert "never disclosed" in apple_summary.lower() or \
               "not disclose" in apple_summary.lower() or \
               "no disclosure" in apple_summary.lower()


# ===================================================================
# Class 9: Source URL Presence Across All Three Additions
# ===================================================================

class TestSourceURLPresence:
    """Each afternoon addition should have source URLs."""

    def test_mit_tr_apple_examples_have_urls(self, research):
        mittr = research["publications"]["mit-tech-review"]
        examples = mittr.get("apple_examples", [])
        for ex in examples:
            assert "source_url" in ex, f"Missing source_url in apple example: {ex.get('title')}"

    def test_mims_cross_entity_has_urls(self, research):
        nc = research["publications"]["news-corp"]
        mims = nc["mims_cross_entity"]
        # Source URLs should be in source_urls list
        source_urls = mims.get("source_urls", [])
        txt = str(source_urls).lower()
        assert "http" in txt, "Mims cross-entity data has no source URLs"

    def test_google_coercion_has_source(self, entities):
        google = entities["entities"]["google"]
        nrd = google["network_revenue_decline"]
        txt = str(nrd).lower()
        assert "http" in txt or "source" in txt or "zacks" in txt or "earnings" in txt

    def test_nyt_q2_has_source_url(self, nytimes):
        """Navigate to sec_filings via ownership_chain."""
        oc = nytimes.get("ownership_chain", [])
        q2 = None
        for entry in oc:
            if isinstance(entry, dict):
                for f in entry.get("sec_filings", []):
                    if "Q2 2026" in str(f.get("period", "")):
                        q2 = f
                        break
        assert q2 is not None, "No Q2 2026 filing found"
        assert "source_url" in q2
        assert "http" in q2["source_url"]
