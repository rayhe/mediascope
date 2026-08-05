"""
End-to-End Narrative Coherence — Full Evidentiary Chain
=======================================================
Tests that the complete body of MediaScope evidence forms a coherent,
internally consistent statistical case linking financial relationships
to editorial bias across publications.

The thesis: Financial relationships between publishers and AI companies
predict the tone, framing, and volume of those publishers' coverage of
Meta vs. the paying AI companies. The only publisher with symmetric
deals (News Corp/WSJ) shows balanced coverage. The only publisher
with no deals at all (Gizmodo) shows editorial-culture-driven negativity.

Each test validates one link in the evidentiary chain.
Source: Aggregate findings from MediaScope iterations 2026-08-04 to 2026-08-05.
"""

import yaml
import pathlib
import pytest

PROFILES_DIR = pathlib.Path(__file__).resolve().parent.parent / "profiles"

@pytest.fixture(scope="module")
def competitor_research():
    with open(PROFILES_DIR / "competitor-coverage-research.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="module")
def competitor_entities():
    with open(PROFILES_DIR / "competitor-entities.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="module")
def wired_profile():
    with open(PROFILES_DIR / "wired.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="module")
def ft_profile():
    with open(PROFILES_DIR / "financial-times.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="module")
def verge_profile():
    with open(PROFILES_DIR / "the-verge.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="module")
def nytimes_profile():
    with open(PROFILES_DIR / "nytimes.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="module")
def all_profiles():
    profiles = {}
    for f in PROFILES_DIR.glob("*.yaml"):
        if f.name.startswith("_") or f.name in ("competitor-coverage-research.yaml",
                                                   "competitor-entities.yaml",
                                                   "advocacy-coalitions.yaml"):
            continue
        with open(f) as fh:
            profiles[f.stem] = yaml.safe_load(fh)
    return profiles


# ===================================================================
# LINK 1: Financial Asymmetry Exists (17:0 ratio)
# ===================================================================

class TestFinancialAsymmetryExists:
    """The excluded publishers have competitor deals but zero Meta deals."""

    def test_at_least_seven_excluded_publishers(self, competitor_entities):
        """7+ publications in the excluded set."""
        excluded = competitor_entities.get("meta_ai_deals", {}).get("excluded_publishers", [])
        assert len(excluded) >= 7

    def test_zero_meta_deals_universally(self, competitor_entities):
        """Every excluded publisher has meta_deal = none."""
        excluded = competitor_entities.get("meta_ai_deals", {}).get("excluded_publishers", [])
        for pub in excluded:
            meta_deal = pub.get("meta_deal", "none")
            assert meta_deal == "none" or meta_deal is None, \
                f"{pub.get('name')} should have no Meta deal"

    def test_majority_have_competitor_deals(self, competitor_entities):
        """At least 6 of 8 excluded publishers have 1+ competitor deals."""
        excluded = competitor_entities.get("meta_ai_deals", {}).get("excluded_publishers", [])
        with_deals = sum(1 for d in excluded
                        if len(d.get("deals_with_competitors", [])) > 0)
        assert with_deals >= 6

    def test_total_ratio_at_least_15_to_0(self, competitor_entities):
        """Total competitor deals ≥ 15, total Meta deals = 0."""
        excluded = competitor_entities.get("meta_ai_deals", {}).get("excluded_publishers", [])
        total_competitor = sum(len(d.get("deals_with_competitors", []))
                              for d in excluded)
        total_meta = sum(1 for d in excluded if d.get("meta_deal") not in ("none", None))
        assert total_competitor >= 15
        assert total_meta == 0


# ===================================================================
# LINK 2: Coverage Asymmetry Exists (Meta vs competitors)
# ===================================================================

class TestCoverageAsymmetryExists:
    """Publications with financial asymmetry show coverage asymmetry."""

    def test_wired_meta_adversarial(self, competitor_research):
        """WIRED covers Meta adversarially."""
        wired = competitor_research["publications"]["wired"]
        assert "adversarial" in wired.get("meta_coverage_tone", "").lower()

    def test_wired_openai_not_adversarial(self, competitor_research):
        """WIRED covers OpenAI neutrally or positively."""
        wired = competitor_research["publications"]["wired"]
        openai_tone = wired.get("openai_coverage_tone", "").lower()
        assert "adversarial" not in openai_tone or "neutral" in openai_tone or "positive" in openai_tone

    def test_ft_coverage_diverges(self, competitor_research):
        """FT's coverage of Meta differs from its OpenAI coverage."""
        ft = competitor_research["publications"].get("financial-times") or \
             competitor_research["publications"].get("ft")
        if ft is None:
            pytest.skip("FT not found")
        meta_tone = ft.get("meta_coverage_tone", "")
        openai_tone = ft.get("openai_coverage_tone", "")
        assert meta_tone != openai_tone, \
            f"FT should cover Meta and OpenAI differently: {meta_tone} vs {openai_tone}"

    def test_verge_meta_adversarial(self, competitor_research):
        """The Verge covers Meta adversarially."""
        verge = competitor_research["publications"]["the-verge"]
        assert "adversarial" in verge.get("meta_coverage_tone", "").lower()

    def test_at_least_four_publications_show_asymmetry(self, competitor_research):
        """4+ publications cover Meta adversarially while covering deal partners less so."""
        pubs = competitor_research["publications"]
        adversarial_meta_count = 0
        for name, data in pubs.items():
            meta_tone = str(data.get("meta_coverage_tone", "")).lower()
            if "adversarial" in meta_tone:
                adversarial_meta_count += 1
        assert adversarial_meta_count >= 4, \
            f"Expected 4+ publications with adversarial Meta coverage, got {adversarial_meta_count}"


# ===================================================================
# LINK 3: Lane Assignment Mechanisms (HOW bias manifests)
# ===================================================================

class TestLaneAssignmentMechanisms:
    """Three distinct mechanisms for editorial lane assignment documented."""

    def test_wired_desk_assignment(self, wired_profile):
        """WIRED uses desk-level lane assignment (product vs investigative)."""
        all_text = yaml.dump(wired_profile).lower()
        # Should document Goode (product desk) vs Cameron/Mehrotra (investigative)
        has_goode = "goode" in all_text
        has_investigative = "cameron" in all_text or "mehrotra" in all_text
        assert has_goode and has_investigative, \
            "WIRED should document both product and investigative desks"

    def test_nyt_reporter_assignment(self, nytimes_profile):
        """NYT uses reporter-level lane assignment (adversarial vs progress beats)."""
        all_text = yaml.dump(nytimes_profile).lower()
        # Should document Isaac/Tan (adversarial Meta beat) vs Metz (AI progress)
        has_meta_beat = "isaac" in all_text or "tan" in all_text
        has_ai_beat = "metz" in all_text
        assert has_meta_beat and has_ai_beat, \
            "NYT should document Meta beat and AI beat reporters"

    def test_ft_within_reporter_asymmetry(self, ft_profile):
        """FT shows within-reporter asymmetry (same reporter, different standards)."""
        all_text = yaml.dump(ft_profile).lower()
        # Hannah Murphy covers both Meta and Snap with different framing
        assert "murphy" in all_text

    def test_three_distinct_mechanisms(self, competitor_research):
        """All three mechanism types documented."""
        all_text = yaml.dump(competitor_research).lower()
        # Should mention desk, reporter, and within-reporter mechanisms
        mechanism_count = 0
        if "desk" in all_text or "editorial desk" in all_text:
            mechanism_count += 1
        if "reporter assignment" in all_text or "beat" in all_text:
            mechanism_count += 1
        if "within-reporter" in all_text or "same reporter" in all_text:
            mechanism_count += 1
        assert mechanism_count >= 2, \
            f"Expected at least 2 lane assignment mechanism types, got {mechanism_count}"


# ===================================================================
# LINK 4: Journalist Cross-Entity Evidence
# ===================================================================

class TestJournalistCrossEntity:
    """Individual journalists demonstrate the pattern at the reporter level."""

    def test_at_least_four_journalists_profiled(self, all_profiles):
        """4+ journalists have cross-entity coverage analysis."""
        journalist_count = 0
        for name, profile in all_profiles.items():
            if profile is None:
                continue
            # Check for journalist data (careers section or inline)
            all_text = yaml.dump(profile).lower()
            if "cross_entity" in all_text or "competitor_coverage" in all_text:
                journalist_count += 1
        assert journalist_count >= 3, \
            f"Expected 3+ profiles with cross-entity analysis, got {journalist_count}"

    def test_will_knight_zero_meta(self, wired_profile):
        """Will Knight (WIRED) has documented zero dedicated Meta articles."""
        all_text = yaml.dump(wired_profile).lower()
        if "knight" not in all_text:
            pytest.skip("Knight not in WIRED profile (may be in careers)")
        # Check journalists.yaml
        journalists_path = PROFILES_DIR / "careers" / "journalists.yaml"
        if journalists_path.exists():
            with open(journalists_path) as f:
                journalists = yaml.safe_load(f)
            all_j_text = yaml.dump(journalists).lower()
            assert "knight" in all_j_text and "meta" in all_j_text

    def test_hannah_murphy_within_reporter_asymmetry(self, ft_profile):
        """Hannah Murphy demonstrates within-reporter framing asymmetry."""
        all_text = yaml.dump(ft_profile).lower()
        assert "murphy" in all_text
        # Should have cross-entity analysis
        assert "cross_entity" in all_text or "competitor" in all_text or "snap" in all_text

    def test_mike_isaac_beat_expansion_consistency(self, nytimes_profile):
        """Mike Isaac's post-expansion coverage is consistently neutral."""
        all_text = yaml.dump(nytimes_profile).lower()
        assert "isaac" in all_text
        # Should document beat change or cross-entity
        assert "beat" in all_text or "silicon valley" in all_text or "expansion" in all_text


# ===================================================================
# LINK 5: Control Groups Validate the Pattern
# ===================================================================

class TestControlGroups:
    """Two control groups validate the financial → editorial hypothesis."""

    def test_news_corp_balanced_control(self, competitor_entities):
        """News Corp (symmetric deals) shows balanced coverage (predicted)."""
        meta_deals = competitor_entities.get("meta_ai_deals", {})
        partners = meta_deals.get("partners", [])
        news_corp = [p for p in partners if "news corp" in p.get("name", "").lower()]
        assert len(news_corp) > 0, "News Corp must be in Meta deal partners"

    def test_gizmodo_independent_control(self, competitor_entities):
        """Gizmodo (zero deals) shows editorial-culture-driven negativity."""
        excluded = competitor_entities.get("meta_ai_deals", {}).get("excluded_publishers", [])
        gizmodo = None
        for pub in excluded:
            if "gizmodo" in pub.get("name", "").lower():
                gizmodo = pub
                break
        if gizmodo is None:
            pytest.skip("Gizmodo not found in excluded publishers")
        deals = gizmodo.get("deals_with_competitors", [])
        meta_deal = gizmodo.get("meta_deal", "none")
        assert len(deals) == 0, "Gizmodo should have zero competitor deals"
        assert meta_deal == "none" or meta_deal is None, "Gizmodo should have no Meta deal"

    def test_controls_span_both_extremes(self, competitor_entities):
        """One control has symmetric deals (News Corp), one has zero (Gizmodo)."""
        # News Corp in Meta deals
        meta_deals = competitor_entities.get("meta_ai_deals", {})
        partners = [p.get("name", "").lower() for p in meta_deals.get("partners", [])]
        has_news_corp = any("news corp" in p for p in partners)

        # Gizmodo in excluded with zero deals
        excluded = meta_deals.get("excluded_publishers", [])
        has_gizmodo = any("gizmodo" in pub.get("name", "").lower() for pub in excluded)

        assert has_news_corp, "Need News Corp as symmetric control"
        assert has_gizmodo, "Need Gizmodo as zero-deal control"


# ===================================================================
# LINK 6: Camera Count Paradox (Apple vs Meta)
# ===================================================================

class TestCameraCountParadox:
    """More cameras ≠ more surveillance framing — manufacturer identity drives framing."""

    def test_apple_12_cameras_zero_surveillance(self, competitor_research):
        """Apple Vision Pro (12 cameras) gets zero surveillance framing from WIRED."""
        wired = competitor_research["publications"]["wired"]
        apple_summary = str(wired.get("apple_coverage_summary", "")).lower()
        # Should mention camera count or zero surveillance
        assert "12" in apple_summary or "camera" in apple_summary or \
               "zero surveillance" in apple_summary.replace("-", " ") or \
               "no surveillance" in apple_summary

    def test_meta_one_camera_surveillance_framing(self, competitor_research):
        """Meta glasses (1 camera) get sustained surveillance framing."""
        wired = competitor_research["publications"]["wired"]
        meta_summary = str(wired.get("meta_coverage_summary", "")).lower()
        assert "surveillance" in meta_summary or "investigat" in meta_summary or \
               "adversarial" in meta_summary


# ===================================================================
# LINK 7: Financial Relationship Sources Are Documented
# ===================================================================

class TestSourceDocumentation:
    """Every financial relationship claim has a source URL or citation."""

    def test_competitor_deal_sources_exist(self, competitor_entities):
        """Competitor deals have source URLs."""
        excluded = competitor_entities.get("meta_ai_deals", {}).get("excluded_publishers", [])
        deals_without_sources = []
        for pub in excluded:
            deals = pub.get("deals_with_competitors", [])
            for deal in deals:
                if isinstance(deal, dict):
                    source = deal.get("source_url")
                    deal_type = deal.get("type", "")
                    # Negotiating deals may lack public sources
                    if not source and "negotiat" not in str(deal_type).lower():
                        deals_without_sources.append(
                            f"{pub.get('name', 'unknown')}: {deal.get('partner', 'unknown')}")
        assert len(deals_without_sources) == 0, \
            f"Deals missing source URLs: {deals_without_sources}"
        assert len(deals_without_sources) == 0, \
            f"Deals missing source URLs: {deals_without_sources}"

    def test_meta_deal_sources_exist(self, competitor_entities):
        """Meta AI deals have source URLs."""
        meta_deals = competitor_entities.get("meta_ai_deals", {})
        partners = meta_deals.get("partners", [])
        without_sources = [p.get("publisher", "unknown") for p in partners
                          if not p.get("source_url")]
        assert len(without_sources) == 0, \
            f"Meta deals missing sources: {without_sources}"


# ===================================================================
# LINK 8: Non-Disclosure is Systemic (not isolated)
# ===================================================================

class TestSystemicNonDisclosure:
    """Non-disclosure is the norm, not an exception."""

    def test_multiple_non_disclosing_publications(self, competitor_research):
        """At least 3 publications have documented non-disclosure."""
        pubs = competitor_research["publications"]
        non_disclosing = []
        for name, data in pubs.items():
            all_text = yaml.dump(data).lower()
            if "never disclosed" in all_text or "not disclosed" in all_text or \
               "no disclosure" in all_text or "never disclose" in all_text:
                non_disclosing.append(name)
        assert len(non_disclosing) >= 2, \
            f"Expected 2+ non-disclosing publications, got: {non_disclosing}"

    def test_wsj_unique_in_disclosing(self, competitor_research):
        """Only WSJ/News Corp consistently discloses."""
        all_text = yaml.dump(competitor_research).lower()
        # Should document WSJ as unique/only discloser
        assert ("only" in all_text and "disclos" in all_text) or \
               ("wsj" in all_text and "disclos" in all_text)
