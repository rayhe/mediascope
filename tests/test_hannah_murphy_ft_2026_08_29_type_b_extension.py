"""
Iteration #360 Type B extension — Hannah Murphy cross-entity verification Aug 29 2026.

Validates:
- FT July 8 2026 super-sensing prototype still present and corroborated via WSJ + Gizmodo
- Snap SPECS June 2026 control uses business framing, 0 surveillance terms
- FT site search for Hannah Murphy Snap returns no recent results (no counterexamples)
- Diagnostic 6:0 surveillance asymmetry persists after 2026 updates

Sources (always keep references — every fact needs URL):
- FT via Techmeme July 8 2026: https://www.techmeme.com/260708/p2
- Gizmodo July 8 aggregation: https://gizmodo.com/tag/smart-glasses/page/2?startIndex=40
- WSJ Aug 26 2026 corroboration FT previously reported: https://www.wsj.com/tech/ai/meta-is-flooding-the-market-with-smartglasses-privacy-advocates-are-up-in-arms-8fb71539
- Snap SPECS Retail Gazette June 2026: https://www.retailgazette.co.uk/blog/2026/06/snap-mocked-over-1995-smart-glasses-as-investors-question-consumer-appeal/
- Snap SPECS Fool June 23 2026: https://www.fool.com/investing/2026/06/23/will-snaps-augmented-reality-glasses-help-or-hurt/
- FastCompany Aug 25 2026 context: https://fastcompany.co.za/tech/2026-08-25-whats-the-plan-with-metas-creepy-smart-glasses/
- FT site search no results: search-results://query?query=site:ft.com%20Hannah%20Murphy%20Snap (verified Aug 29 2026)
"""

import yaml
import os
import pytest


PROFILES_DIR = os.path.join(os.path.dirname(__file__), "..", "profiles")


def load_ft():
    with open(os.path.join(PROFILES_DIR, "financial-times.yaml")) as f:
        return yaml.safe_load(f)


class TestHannahMurphy2026_08_29Verification:
    def test_ft_profile_loads(self):
        profile = load_ft()
        assert profile["slug"] == "financial-times"

    def test_murphy_exists(self):
        profile = load_ft()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"]
        assert len(murphy) == 1
        assert murphy[0]["beat"]

    def test_diagnostic_persists(self):
        profile = load_ft()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        comp = murphy["cross_entity_coverage_analysis"]["diagnostic_comparison_ar_glasses"]
        assert comp["surveillance_term_count_meta"] >= 5
        assert comp["surveillance_term_count_snap"] == 0

    def test_verification_block_exists(self):
        profile = load_ft()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        comp = murphy["cross_entity_coverage_analysis"]["diagnostic_comparison_ar_glasses"]
        assert "verification_2026_08_29" in comp
        v = comp["verification_2026_08_29"]
        assert v["iteration"] == 360
        assert v["date"] == "2026-08-29"

    def test_meta_july_8_2026_ft_original_via_techmeme(self):
        profile = load_ft()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        v = murphy["cross_entity_coverage_analysis"]["diagnostic_comparison_ar_glasses"]["verification_2026_08_29"]
        meta = v["meta_prototype_july_8_2026"]
        assert meta["ft_original_via_techmeme"] == "https://www.techmeme.com/260708/p2"
        assert meta["gizmodo_aggregation_july_8"] == "https://gizmodo.com/tag/smart-glasses/page/2?startIndex=40"
        assert meta["wsj_corroboration"] == "https://www.wsj.com/tech/ai/meta-is-flooding-the-market-with-smartglasses-privacy-advocates-are-up-in-arms-8fb71539"
        assert "Financial Times previously reported" in meta["wsj_line"]
        assert meta["framing"] == "adversarial_surveillance"

    def test_meta_language_verified_2026(self):
        profile = load_ft()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        v = murphy["cross_entity_coverage_analysis"]["diagnostic_comparison_ar_glasses"]["verification_2026_08_29"]
        lang = v["meta_prototype_july_8_2026"]["language_verified"]
        # Must include legal-threat vocabulary that distinguishes Meta from Snap
        assert any("wiretapping" in t for t in lang)
        assert any("biometric" in t for t in lang)
        assert any("civil" in t for t in lang)

    def test_snap_specs_june_2026_control(self):
        profile = load_ft()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        v = murphy["cross_entity_coverage_analysis"]["diagnostic_comparison_ar_glasses"]["verification_2026_08_29"]
        snap = v["snap_specs_june_2026_control"]
        assert snap["price"] == "$2,195 / £1,995"
        assert snap["weight"] == "136g (vs ~30g typical glasses, ~4.5x heavier)"
        assert snap["battery"] == "4-hour mixed-use"
        # Both Snap sources must have 0 surveillance terms
        for src in snap["sources"]:
            assert src["surveillance_terms"] == 0
            assert src["url"].startswith("https://")

    def test_snap_sources_are_business_framing(self):
        profile = load_ft()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        v = murphy["cross_entity_coverage_analysis"]["diagnostic_comparison_ar_glasses"]["verification_2026_08_29"]
        snap = v["snap_specs_june_2026_control"]
        framings = [s["framing"] for s in snap["sources"]]
        assert any("business" in f or "viability" in f or "gamble" in f for f in framings)
        # Ensure no surveillance language in any Snap source language list
        for src in snap["sources"]:
            combined = " ".join(src["language"]).lower()
            assert "wiretap" not in combined
            assert "biometric" not in combined
            assert "surveillance" not in combined

    def test_ft_site_search_no_recent_snap(self):
        profile = load_ft()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        v = murphy["cross_entity_coverage_analysis"]["diagnostic_comparison_ar_glasses"]["verification_2026_08_29"]
        search = v["ft_site_search_2026_08_29"]
        assert search["result"] == "No results found (2026-08-29 search)"
        assert "Snap" in search["query"]

    def test_fastcompany_context_url_valid(self):
        profile = load_ft()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        v = murphy["cross_entity_coverage_analysis"]["diagnostic_comparison_ar_glasses"]["verification_2026_08_29"]
        fc = v["fastcompany_aug_25_2026_context"]
        assert fc["url"] == "https://fastcompany.co.za/tech/2026-08-25-whats-the-plan-with-metas-creepy-smart-glasses/"
        assert fc["date"] == "2026-08-25 (3 days ago as of Aug 29)"

    def test_overall_implication_mentions_controls(self):
        profile = load_ft()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        v = murphy["cross_entity_coverage_analysis"]["diagnostic_comparison_ar_glasses"]["verification_2026_08_29"]
        impl = v["overall_implication"]
        assert "6:0" in impl or "6" in impl
        assert "same journalist" in impl.lower() or "same reporter" in impl.lower()
        assert "Snap" in impl
        assert "Meta" in impl

    def test_methodology_note_no_em_dash_and_cautious(self):
        profile = load_ft()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        v = murphy["cross_entity_coverage_analysis"]["diagnostic_comparison_ar_glasses"]["verification_2026_08_29"]
        meta = v["meta_prototype_july_8_2026"]
        note = meta["methodology_note"]
        assert "—" not in note, "em dash banned in all docs"
        assert "Techmeme" in note or "discovery" in note.lower()

    def test_no_em_dash_anywhere_in_verification(self):
        profile = load_ft()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        v = murphy["cross_entity_coverage_analysis"]["diagnostic_comparison_ar_glasses"]["verification_2026_08_29"]
        # Serialize to string and check
        import json
        dumped = json.dumps(v)
        assert "—" not in dumped, "em dash found in verification block — replace with comma or hyphen"

    def test_source_urls_always_keep_references(self):
        """Every fact needs source URL — ensure all claims have URLs."""
        profile = load_ft()
        murphy = [j for j in profile["key_journalists"] if j["name"] == "Hannah Murphy"][0]
        v = murphy["cross_entity_coverage_analysis"]["diagnostic_comparison_ar_glasses"]["verification_2026_08_29"]
        # Meta side 3 URLs
        meta = v["meta_prototype_july_8_2026"]
        assert meta["ft_original_via_techmeme"].startswith("https://")
        assert meta["gizmodo_aggregation_july_8"].startswith("https://")
        assert meta["wsj_corroboration"].startswith("https://")
        # Snap side 2 URLs
        snap = v["snap_specs_june_2026_control"]
        assert len(snap["sources"]) >= 2
        for s in snap["sources"]:
            assert s["url"].startswith("https://")
