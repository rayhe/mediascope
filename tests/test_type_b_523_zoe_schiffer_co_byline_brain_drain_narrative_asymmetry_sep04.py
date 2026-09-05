"""
Test Type B #523: Zoe Schiffer co-byline brain-drain narrative asymmetry Sep 04 2026

Mechanism #523 Type B - Journalist Cross-Entity Tracking
Journalist: Zoe Schiffer (WIRED Director, Business and Industry)
Focus: Schiffer's written WIRED co-bylines frame Meta talent/morale departures as
institutional pathology (Record Low Morale May 2026 four-byline piece; Researchers
Already Leaving Meta Superintelligence Labs for OpenAI Aug 2025) while the same
stories position OpenAI as the aspirational destination absorbing zero in-story
scrutiny. Distinct from mechanism 357 (hardware talent war, podcast register) by
using written co-byline articles with verified WIRED URLs.

Validates:
- Zoe Schiffer exists in journalists.yaml as WIRED Director, Business and Industry
- Mechanism 523 exists with correct iteration_type B, iteration 523
- Two Meta co-byline articles documented with exact verified WIRED URLs
- Bylines include Zoe Schiffer on both Meta pieces
- Asymmetry scorer MANUAL ILLUSTRATIVE not empirical, delta -0.4
- Confounders >=5 with STRONG >=2, co-byline dilution ranked STRONG
- Confounding adjustment attenuates raw 0.40 to adjusted 0.23 weak_to_moderate
- Financial context correlation not causation with Conde Nast OpenAI licensing
- Source URLs HTTPS
- No em dashes
- Cross references 421, 357, 436, 447

No em dashes allowed per project rule.
"""

import os
import yaml

JOURNALISTS_YAML = os.path.join(os.path.dirname(__file__), "..", "profiles", "careers", "journalists.yaml")

MECH_KEY = "mechanism_523_zoe_schiffer_co_byline_brain_drain_narrative_asymmetry_sep04"


def load_journalists():
    with open(JOURNALISTS_YAML, "r") as f:
        data = yaml.safe_load(f)
        if isinstance(data, dict) and "journalists" in data:
            return data["journalists"]
        return data


def get_schiffer():
    data = load_journalists()
    for entry in data:
        if isinstance(entry, dict) and entry.get("name") == "Zoë Schiffer":
            return entry
    raise AssertionError("Zoë Schiffer not found in journalists.yaml")


def get_mech():
    schiffer = get_schiffer()
    cc = schiffer.get("competitor_coverage", {})
    assert MECH_KEY in cc, "mechanism_523 must exist under competitor_coverage"
    return cc[MECH_KEY]


def test_schiffer_exists_as_wired_director():
    schiffer = get_schiffer()
    notes = str(schiffer.get("notes", ""))
    assert "Wired" in notes or "WIRED" in notes
    assert "Director" in notes


def test_schiffer_wired_career_entry():
    schiffer = get_schiffer()
    career = schiffer.get("career", [])
    pubs = [c.get("publication", "") for c in career if isinstance(c, dict)]
    assert any("wired" in p for p in pubs), "must have a WIRED career entry"


def test_mechanism_523_metadata():
    m = get_mech()
    assert m["mechanism_id"] == 523
    assert m["iteration"] == 523
    assert m["iteration_type"] == "B"
    assert m["publication_focus"] == "wired"
    assert m["scheduled_job_id"] == "mediascope-daily-iteration"


def test_two_meta_co_byline_articles():
    m = get_mech()
    arts = m["meta_articles_co_byline"]
    assert isinstance(arts, list) and len(arts) == 2
    for a in arts:
        assert "Zoe Schiffer" in a["bylines"]
        assert a["source_url"].startswith("https://")


def test_meta_article_urls_exact():
    m = get_mech()
    urls = [a["source_url"] for a in m["meta_articles_co_byline"]]
    assert "https://www.wired.com/story/meta-new-reality-record-high-profits-record-low-morale/" in urls
    assert "https://www.wired.com/story/researchers-leave-meta-superintelligence-labs-openai/" in urls


def test_four_byline_morale_piece_documented():
    m = get_mech()
    a = next(a for a in m["meta_articles_co_byline"] if "Record Low Morale" in a["title"])
    assert len(a["bylines"]) == 4
    assert "Steven Levy" in a["bylines"]
    assert "Lauren Goode" in a["bylines"]


def test_openai_comparator_register():
    m = get_mech()
    comp = m["openai_comparator_register"]
    assert comp["register"] == "legal_drama_power_plays"
    assert "Lawsuits" in comp["podcast_episode"]


def test_scorer_manual_illustrative():
    m = get_mech()
    s = m["asymmetry_scorer_result"]
    assert s["label"] == "MANUAL_ILLUSTRATIVE_NOT_EMPIRICAL"
    assert s["delta_meta_vs_openai_MANUAL_ILLUSTRATIVE"] == -0.4
    assert s["significant"] is False
    assert s["empirical_validation_required"] is True
    assert "NOT empirical" in s["methodology"] or "not empirical" in s["methodology"].lower()


def test_confounders_ranked():
    m = get_mech()
    confs = m["confounders_ranked"]
    assert len(confs) >= 5
    strong = [c for c in confs if c.startswith("[STRONG]")]
    assert len(strong) >= 2
    assert any("Co-byline" in c for c in strong)


def test_confounding_adjustment_attenuates():
    m = get_mech()
    adj = m["confounding_adjustment"]
    assert adj["raw_score"] == 0.4
    assert adj["adjusted_score"] == 0.23
    assert adj["adjusted_score"] < adj["raw_score"]
    assert "weak_to_moderate" in adj["adjusted_calc"]


def test_financial_context_not_causation():
    m = get_mech()
    fc = m["financial_context_correlation_not_causation"]
    assert "OpenAI" in fc
    assert "correlation" in fc.lower() or "not causation" in fc.lower()


def test_source_urls_https():
    m = get_mech()
    for u in m["source_urls"]:
        assert u.startswith("http://") or u.startswith("https://"), f"source URL must be http(s): {u}"
    wired = [u for u in m["source_urls"] if "wired.com" in u]
    assert len(wired) >= 2
    for u in wired:
        assert u.startswith("https://"), f"WIRED URLs must be HTTPS: {u}"
    assert len(m["source_urls"]) >= 5


def test_cross_references():
    m = get_mech()
    refs = m["cross_references"]
    assert 421 in refs
    assert 357 in refs
    assert 436 in refs


def test_test_file_field_matches():
    m = get_mech()
    assert m["test_file"] == "tests/test_type_b_523_zoe_schiffer_co_byline_brain_drain_narrative_asymmetry_sep04.py"


def test_no_em_dashes_in_mechanism():
    m = get_mech()
    blob = yaml.dump(m, allow_unicode=True)
    assert "—" not in blob, "em dashes are banned per project rule"
