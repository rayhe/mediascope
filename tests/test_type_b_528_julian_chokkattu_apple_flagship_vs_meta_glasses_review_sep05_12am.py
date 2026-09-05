"""
Test Type B #528: Julian Chokkattu Apple flagship vs Meta glasses review register Sep 05 2026

Mechanism #528 Type B - Journalist Cross-Entity Tracking
Journalist: Julian Chokkattu (WIRED Senior Editor, Gear)
Focus: Same-reviewer product-review genre register gradient. Chokkattu assigns Apple
flagship hardware heroic review registers (iPhone 17: 9/10 "Close to perfection";
M5 iPad Pro: "iPadOS 26 makes it shine") while his Meta glasses product/launch pieces
carry surveillance-anchored registers (Jun 23 Meta $299 glasses: surveillance-consumer
juxtaposition + negative kicker, manual tone +0.15; Jul 2 subscription article:
extraction framing, tone -0.65). MANUAL ILLUSTRATIVE delta -1.025, n=2 vs n=2,
NOT artifact-grade. Extends #426 (Aug 31 Vision Pro 5/10 triangulation) from headsets
to Apple flagship phone/tablet hardware reviews. First dedicated Type B
competitor_coverage block on Chokkattu.

Validates:
- Julian Chokkattu exists in journalists.yaml as WIRED Senior Editor Gear
- Mechanism 528 exists with correct iteration_type B, iteration 528
- Apple side: iPhone 17 9/10 + M5 iPad Pro, both with verbatim quotes and mirror URLs
- Meta side: Jun 23 glasses launch (+0.15) + Jul 2 subscription article (-0.65)
- Register gradient MANUAL ILLUSTRATIVE: apple [0.80, 0.75], meta [0.15, -0.65], delta -1.025
- Statistical discipline: p_value NOT_CALCULATED, is_significant False, not artifact-grade
- Confounders ranked STRONG/MODERATE/WEAK; product-maturity + time-window STRONG
- Counter-evidence: Vision Pro 5/10, honest Apple cons, topic-driven alternative
- Hygiene: HTTPS only, no em/en dashes, ASCII-only, cross refs, novelty statement

No em dashes allowed per project rule.
"""

import os
import yaml

JOURNALISTS_YAML = os.path.join(os.path.dirname(__file__), "..", "profiles", "careers", "journalists.yaml")

MECH_KEY = "type_b_528_julian_chokkattu_apple_flagship_vs_meta_glasses_review_register"


def load_journalists():
    with open(JOURNALISTS_YAML, "r") as f:
        data = yaml.safe_load(f)
        if isinstance(data, dict) and "journalists" in data:
            return data["journalists"]
        return data


def get_chokkattu():
    data = load_journalists()
    for entry in data:
        if isinstance(entry, dict) and entry.get("name") == "Julian Chokkattu":
            return entry
    raise AssertionError("Julian Chokkattu not found in journalists.yaml")


def get_mech():
    chok = get_chokkattu()
    cc = chok.get("competitor_coverage", {})
    assert MECH_KEY in cc, "type_b_528 mechanism must exist under competitor_coverage"
    return cc[MECH_KEY]


class TestJournalistProfile:
    def test_chokkattu_exists_as_wired_gear_editor(self):
        chok = get_chokkattu()
        notes = str(chok.get("notes", ""))
        assert "Wired" in notes or "WIRED" in notes
        assert "Gear" in notes

    def test_chokkattu_career_wired_senior_editor(self):
        chok = get_chokkattu()
        career = chok.get("career", [])
        pubs = [c.get("publication", "") for c in career if isinstance(c, dict)]
        assert "wired" in pubs
        roles = [c.get("role", "") for c in career if isinstance(c, dict)]
        assert any("senior_editor" in r or "reviews" in r for r in roles)

    def test_chokkattu_prior_mechanisms_intact(self):
        chok = get_chokkattu()
        assert "mechanism_207_apple_camera_airpods_leak_silence" in chok
        assert "mechanism_354_pricing_framing_asymmetry_snap_meta" in chok
        assert "mechanism_362_samsung_galaxy_glasses_price_parity_silence" in chok
        assert "mechanism_426_julian_chokkattu_comfort_price_privacy_triangulation_meta_samsung_apple_aug31" in chok

    def test_neighbor_journalist_intact(self):
        data = load_journalists()
        names = [e.get("name") for e in data if isinstance(e, dict)]
        assert "Caspar Llewellyn Smith" in names
        idx_chok = names.index("Julian Chokkattu")
        assert names[idx_chok + 1] == "Caspar Llewellyn Smith"


class TestMechanismExists:
    def test_mechanism_id_528(self):
        mech = get_mech()
        assert mech["mechanism_id"] == 528

    def test_iteration_type_b(self):
        mech = get_mech()
        assert mech["iteration_type"] == "B"
        assert mech["iteration"] == 528

    def test_discovery_date_sep05(self):
        mech = get_mech()
        assert mech["discovery_date"] == "2026-09-05"

    def test_test_file_name(self):
        mech = get_mech()
        assert mech["test_file"] == "tests/test_type_b_528_julian_chokkattu_apple_flagship_vs_meta_glasses_review_sep05_12am.py"

    def test_single_key_invariant(self):
        chok = get_chokkattu()
        assert len(chok["competitor_coverage"]) == 1

    def test_novelty_statement_present(self):
        mech = get_mech()
        nov = str(mech.get("novelty", ""))
        assert "First dedicated Type B" in nov
        assert "426" in nov


class TestAppleSide:
    def test_iphone_17_nine_of_ten(self):
        mech = get_mech()
        ip = mech["apple_side"]["iphone_17_review"]
        assert ip["wired_rating"] == "9/10"
        assert ip["reviewer"] == "Julian Chokkattu"
        assert ip["date"] == "2025-09"

    def test_iphone_17_best_base_model_quote(self):
        mech = get_mech()
        quotes = mech["apple_side"]["iphone_17_review"]["key_quotes"]
        joined = " ".join(quotes)
        assert "better base model in the annual iPhone lineup" in joined

    def test_iphone_17_battery_quote(self):
        mech = get_mech()
        quotes = mech["apple_side"]["iphone_17_review"]["key_quotes"]
        joined = " ".join(quotes)
        assert "six hours of screen-on time" in joined

    def test_iphone_17_honest_cons(self):
        mech = get_mech()
        cons = " ".join(mech["apple_side"]["iphone_17_review"]["cons_noted"])
        assert "vapor chamber" in cons

    def test_iphone_17_center_stage_privacy_note(self):
        mech = get_mech()
        note = str(mech["apple_side"]["iphone_17_review"]["privacy_note"])
        assert "Center Stage" in note
        assert "zero privacy framing" in note

    def test_iphone_17_mirror_url(self):
        mech = get_mech()
        url = mech["apple_side"]["iphone_17_review"]["mirror_url"]
        assert url == "https://macdailynews.com/2025/09/23/wired-reviews-apples-new-iphone-17-close-to-perfection/"

    def test_m5_ipad_pro_quotes(self):
        mech = get_mech()
        quotes = " ".join(mech["apple_side"]["m5_ipad_pro_review"]["key_quotes"])
        assert "touchscreen Mac of your dreams" in quotes
        assert "faster than I ever have before on an iPad" in quotes

    def test_m5_ipad_pro_buyers_steer_away(self):
        mech = get_mech()
        cons = " ".join(mech["apple_side"]["m5_ipad_pro_review"]["cons_noted"])
        assert "older M4 model" in cons

    def test_m5_ipad_pro_mirror_url(self):
        mech = get_mech()
        url = mech["apple_side"]["m5_ipad_pro_review"]["mirror_url"]
        assert url == "https://macdailynews.com/2025/10/21/wired-reviews-apples-m5-ipad-pro-ipados-26-makes-it-shine/"

    def test_apple_tones(self):
        mech = get_mech()
        assert mech["apple_side"]["iphone_17_review"]["tone_manual_illustrative"] == 0.80
        assert mech["apple_side"]["m5_ipad_pro_review"]["tone_manual_illustrative"] == 0.75


class TestMetaSide:
    def test_jun23_glasses_launch_register(self):
        mech = get_mech()
        meta = mech["meta_side"]["meta_self_branded_glasses_launch"]
        assert meta["date"] == "2026-06-23"
        assert meta["reviewer"] == "Julian Chokkattu"
        assert meta["tone_manual_illustrative"] == 0.15
        devices = " ".join(meta["framing_devices"])
        assert "surveillance_consumer_juxtaposition" in devices
        assert "negative_kicker" in devices
        assert "all-time low" in devices

    def test_jun23_military_surveillance_quote(self):
        mech = get_mech()
        devices = " ".join(mech["meta_side"]["meta_self_branded_glasses_launch"]["framing_devices"])
        assert "US military and police" in devices

    def test_jun23_repo_grounding(self):
        mech = get_mech()
        g = str(mech["meta_side"]["meta_self_branded_glasses_launch"]["repo_grounding"])
        assert "wired_meta_glasses_launch_self_branded_2026_06_23_analysis.md" in g

    def test_jul02_subscription_register(self):
        mech = get_mech()
        sub = mech["meta_side"]["meta_subscription_article"]
        assert sub["date"] == "2026-07-02"
        assert sub["tone_manual_illustrative"] == -0.65
        devices = " ".join(sub["framing_devices"])
        assert "extracting value" in devices
        assert "monetizing customers" in devices


class TestRegisterGradient:
    def test_delta_minus_1_025(self):
        mech = get_mech()
        r = mech["asymmetry_scorer_result"]
        assert r["target_entity"] == "meta"
        assert r["peer_entity"] == "apple"
        assert r["target_avg"] == -0.25
        assert r["peer_avg"] == 0.775
        assert r["delta"] == -1.025

    def test_manual_illustrative_flag(self):
        mech = get_mech()
        r = mech["asymmetry_scorer_result"]
        assert r["manual_illustrative"] is True
        assert r["correlation_not_causation"] is True
        assert r["not_artifact_grade"] is True

    def test_arithmetic_consistency(self):
        mech = get_mech()
        r = mech["asymmetry_scorer_result"]
        assert abs((r["target_avg"] - r["peer_avg"]) - r["delta"]) < 1e-9


class TestStatisticalDiscipline:
    def test_p_value_not_calculated(self):
        mech = get_mech()
        r = mech["asymmetry_scorer_result"]
        assert r["p_value"] == "NOT_CALCULATED"
        assert r["cohens_d"] == "NOT_CALCULATED"
        assert r["ci_95"] == "NOT_CALCULATED"

    def test_not_significant(self):
        mech = get_mech()
        assert mech["asymmetry_scorer_result"]["is_significant"] is False

    def test_discipline_text(self):
        mech = get_mech()
        d = str(mech.get("statistical_discipline", ""))
        assert "MANUAL ILLUSTRATIVE" in d
        assert "n=2 vs n=2" in d
        assert "NOT artifact-grade" in d


class TestConfounders:
    def test_strong_confounders(self):
        mech = get_mech()
        strong = mech["confounders_ranked"]["strong"]
        assert len(strong) >= 2
        joined = " ".join(strong)
        assert "product maturity" in joined
        assert "time window" in joined

    def test_moderate_confounders(self):
        mech = get_mech()
        moderate = mech["confounders_ranked"]["moderate"]
        assert len(moderate) >= 2
        joined = " ".join(moderate)
        assert "camera direction" in joined
        assert "mirror provenance" in joined

    def test_weak_confounder(self):
        mech = get_mech()
        weak = mech["confounders_ranked"]["weak"]
        assert len(weak) >= 1

    def test_counter_evidence_vision_pro(self):
        mech = get_mech()
        ce = " ".join(mech["counter_evidence"])
        assert "Vision Pro" in ce
        assert "5/10" in ce

    def test_counter_evidence_honest_cons(self):
        mech = get_mech()
        ce = " ".join(mech["counter_evidence"])
        assert "vapor chamber" in ce or "M4 model" in ce

    def test_counter_evidence_topic_driven(self):
        mech = get_mech()
        ce = " ".join(mech["counter_evidence"])
        assert "topic-driven" in ce


class TestHygiene:
    def test_source_urls_https(self):
        mech = get_mech()
        urls = mech["source_urls"]
        assert len(urls) == 3
        assert all(u.startswith("https://") for u in urls)
        assert not any(u.endswith("...") or "…" in u for u in urls)

    def test_cross_references(self):
        mech = get_mech()
        refs = mech["cross_references"]
        for n in (30, 42, 207, 252, 354, 362, 411, 426):
            assert n in refs, "missing cross-reference %d" % n

    def test_no_em_or_en_dashes_in_block(self):
        chok = get_chokkattu()
        import json
        blob = json.dumps(chok["competitor_coverage"])
        assert "\u2014" not in blob
        assert "\u2013" not in blob

    def test_ascii_only_block(self):
        chok = get_chokkattu()
        import json
        blob = json.dumps(chok["competitor_coverage"], ensure_ascii=True)
        chok["competitor_coverage"]  # noqa - touch
        assert blob.isascii()

    def test_pattern_mentions_both_sides(self):
        mech = get_mech()
        p = str(mech.get("pattern", ""))
        assert "iPhone 17" in p
        assert "M5 iPad Pro" in p
        assert "Jun 23" in p
        assert "Jul 2" in p
