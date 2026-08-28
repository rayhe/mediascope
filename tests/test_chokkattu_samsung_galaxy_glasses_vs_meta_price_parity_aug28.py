"""
Iteration #351 — Type B Journalist Cross-Entity Tracking
Mechanism #362 — WIRED Gear Desk Samsung Galaxy Glasses Price-Parity Silence

Same journalist (Julian Chokkattu) covers identical hardware across 3 manufacturers with manufacturer-dependent framing:
- May 19 Google Android XR playful (Nano Banana bananas!)
- Jun 3 Meta mass surveillance (15-day swing)
- Jul 22 Samsung silence (49-day post-Meta, 64-day post-Google, 70-day 3-competitor pattern)

Samsung Galaxy Glasses: $379-499 (same as Meta $379), 50g, 12MP Sony IMX681 autofocus (BETTER than Meta fixed-focus = higher privacy risk), Snapdragon AR1 Gen 1 same as Meta, Android XR + Gemini, Gentle Monster/Warby Parker, iOS compatible, audio-only first model, monocular 2026, binocular 2027.
"""

import yaml
from pathlib import Path

WIRED_YAML = Path("profiles/wired.yaml")
JOURNALISTS_YAML = Path("profiles/careers/journalists.yaml")


def load_wired():
    with open(WIRED_YAML) as f:
        return yaml.safe_load(f)


def load_journalists():
    with open(JOURNALISTS_YAML) as f:
        return yaml.safe_load(f)


class TestMechanism362Exists:
    def test_wired_yaml_parseable(self):
        data = load_wired()
        assert data is not None

    def test_mechanism_362_exists(self):
        data = load_wired()
        assert "samsung_galaxy_glasses_vs_meta_price_parity_coverage_silence" in data
        mech = data["samsung_galaxy_glasses_vs_meta_price_parity_coverage_silence"]
        assert mech["mechanism_id"] == 362

    def test_mechanism_362_iteration_351_type_b(self):
        mech = load_wired()["samsung_galaxy_glasses_vs_meta_price_parity_coverage_silence"]
        assert mech["iteration"] == 351
        assert mech["iteration_type"] == "B"
        assert "15:00" in mech["iteration_time"]

    def test_samsung_specs_price_parity(self):
        mech = load_wired()["samsung_galaxy_glasses_vs_meta_price_parity_coverage_silence"]
        samsung = mech["samsung_galaxy_glasses"]
        # Price $379-499 same bracket as Meta $379
        assert "379" in str(samsung["msrp_usd"])
        assert "499" in str(samsung["msrp_usd"])
        meta = mech["meta_comparator"]
        assert meta["msrp_usd"] == 379

    def test_samsung_camera_autofocus_better_than_meta(self):
        mech = load_wired()["samsung_galaxy_glasses_vs_meta_price_parity_coverage_silence"]
        samsung = mech["samsung_galaxy_glasses"]
        assert "autofocus" in samsung["camera"].lower()
        assert "IMX681" in samsung["camera"]
        meta = mech["meta_comparator"]
        assert "fixed-focus" in meta["camera"]

    def test_wired_gear_desk_zero_samsung_articles(self):
        mech = load_wired()["samsung_galaxy_glasses_vs_meta_price_parity_coverage_silence"]
        wired = mech["wired_gear_desk"]
        assert wired["standalone_articles_samsung_galaxy_glasses"]["count"] == 0
        assert wired["standalone_articles_meta_same_window"]["count"] >= 3

    def test_camera_capability_privacy_inversion(self):
        mech = load_wired()["samsung_galaxy_glasses_vs_meta_price_parity_coverage_silence"]
        inv = mech["camera_capability_privacy_inversion"]
        assert inv["vocabulary_count_samsung"] == 0
        assert inv["vocabulary_count_meta"] >= 6
        assert "autofocus" in inv["samsung_camera"].lower() or "autofocus" in str(inv)

    def test_chokkattu_3_competitor_70_day_pattern(self):
        mech = load_wired()["samsung_galaxy_glasses_vs_meta_price_parity_coverage_silence"]
        pattern = mech["cross_entity_scoring"]["chokkattu_15_day_swing_extended"]
        # Must have all three dates
        assert "May 19" in pattern["google_io_2026"] or "May 19" in str(pattern)
        assert "Jun 3" in pattern["business_wars_meta"] or "Jun 3" in str(pattern)
        assert "Jul 22" in pattern["samsung_unpacked_2026"] or "Jul 22" in str(pattern)

    def test_asymmetry_scorer_synthetic(self):
        mech = load_wired()["samsung_galaxy_glasses_vs_meta_price_parity_coverage_silence"]
        result = mech["asymmetry_scorer_result"]
        assert result["target_entity"] == "Meta"
        assert result["peer_entity"] == "Samsung"
        assert abs(result["delta"] - (-0.654)) < 0.001
        assert result["cohens_d"] < -5  # huge effect
        assert result["significant"] is True
        assert "synthetic" in result["methodology"].lower() or "synthetic" in result["p_value"].lower()

    def test_confounder_adjustment(self):
        mech = load_wired()["samsung_galaxy_glasses_vs_meta_price_parity_coverage_silence"]
        adj = mech["confounding_adjustment"]
        assert abs(adj["raw_score"] - 0.654) < 0.01
        assert abs(adj["adjusted_score"] - 0.434) < 0.01
        assert len(adj["adjustments"]) >= 4

    def test_source_urls_https_minimum(self):
        mech = load_wired()["samsung_galaxy_glasses_vs_meta_price_parity_coverage_silence"]
        urls = mech["source_urls"]
        https_count = sum(1 for u in urls if u.startswith("https://"))
        assert https_count >= 7, f"Expected >=7 HTTPS URLs, got {https_count}"
        # Must include TechTimes Samsung price parity source
        assert any("techtimes.com" in u for u in urls)
        # Must include Samsung Newsroom interview
        assert any("news.samsung.com" in u for u in urls)
        # Must include MacRumors July launch date
        assert any("macrumors.com" in u for u in urls)

    def test_no_duplicate_mechanism_ids(self):
        # Ensure 362 is not duplicated elsewhere in wired.yaml
        import re
        text = WIRED_YAML.read_text()
        ids = re.findall(r"mechanism_id:\s*362\b", text)
        assert len(ids) == 1, f"mechanism_id 362 appears {len(ids)} times, expected 1"


class TestJournalistsYamlChokkattu362:
    def test_journalists_yaml_parseable(self):
        data = load_journalists()
        assert data is not None

    def test_chokkattu_mechanism_362_exists(self):
        data = load_journalists()
        # journalists is list of dicts each with single key?
        # Actually structure is {'journalists': [{'name': ..., ...}, ...]}
        journalists = data["journalists"] if "journalists" in data else data
        if isinstance(journalists, dict):
            journalists = [journalists]
        # Find Chokkattu
        chokkattu = None
        for j in journalists:
            if isinstance(j, dict) and j.get("name") == "Julian Chokkattu":
                chokkattu = j
                break
            # Sometimes nested under different key
            if isinstance(j, dict) and "name" in j:
                if j["name"] == "Julian Chokkattu":
                    chokkattu = j
                    break
        # Fallback: search raw text
        if chokkattu is None:
            text = JOURNALISTS_YAML.read_text()
            assert "mechanism_362_samsung_galaxy_glasses" in text
            return
        assert "mechanism_362_samsung_galaxy_glasses_price_parity_silence" in chokkattu

    def test_mechanism_362_test_file_reference(self):
        mech = load_wired()["samsung_galaxy_glasses_vs_meta_price_parity_coverage_silence"]
        assert mech["test_file"] == "tests/test_chokkattu_samsung_galaxy_glasses_vs_meta_price_parity_aug28.py"
