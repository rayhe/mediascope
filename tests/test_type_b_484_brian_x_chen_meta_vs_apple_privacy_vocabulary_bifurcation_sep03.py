"""
Type B #484 - Brian X. Chen Meta vs Apple Privacy Vocabulary Bifurcation
Sep 3 2026 02:00 PDT - scheduled job_id mediascope-daily-iteration goal_54093bda4145 rotation A->B

Mechanism #484 documents a within-journalist privacy-standard bifurcation at the
NYT: lead consumer tech columnist Brian X. Chen evaluated two camera-equipped
face computers about seven weeks apart with sharply different privacy registers.

Meta evidence (Dec 2023, NYT Tech Fix column, secondary-verified via Pixel Envy
linklog quoting the column verbatim):
- Shot 200 photos and videos in public (BART trains, hiking trails, parks) to
  test whether bystanders notice the LED recording indicator
- Interviewed surveillance critic Chris Gilliard on private-space implications
- Framing: privacy alarm around the LED indicator and mainstreaming of
  camera glasses ("spy glasses" characterization in secondary coverage)

Apple evidence (Jan 27 2024 "Making VR Headsets Cool Won't Be Easy, Even for
Apple" + Feb 2024 Vision Pro review; secondary-verified via DNS Africa mirror,
TidBITS roundup, Cult of Mac):
- Device: 12 cameras, LiDAR scanner, eye tracking, Optic ID iris authentication
- Chen's criticisms were product-utility only: "lacks purpose", "impressive but
  incomplete first-generation product", "a computer for people to use alone"
- His discomfort with face-scan Personas was coded as aesthetic uncanny-valley
  "ick", not as a biometric consent issue
- Zero privacy vocabulary in the quoted review text; no surveillance critic
  interviewed

Finding: the device with roughly 12x the cameras plus iris biometrics received
none of the privacy scrutiny the same reviewer applied to the single-camera
device (MANUAL ILLUSTRATIVE quote-level counts: Meta 5+, Apple 0).

Novelty checks:
- grep nytimes.yaml brian_x_chen -> 484 only (no prior Chen mechanism)
- grep tests/ brian_x_chen -> no prior test file
- distinct journalist from all prior Type B entries (457 Adrienne So, 452 Simon
  Hill, 447/442/436/431 earlier)
- complements mechanism #457's counter-example: asymmetry here is not reviewer
  animus either, but the privacy-register bifurcation is real at the article
  level and survives the STRONG confounder (Meta's genuine privacy history)

Sources (secondary-verified; NYT primary paywalled):
- https://pxlnv.com/linklog/meta-ray-bans-privacy/
- https://www.resource.dnsafrica.org/2024/01/27/making-vr-headsets-cool-wont-be-easy-even-for-apple-the-new-york-times/
- https://talk.tidbits.com/t/impressions-and-thoughts-from-early-vision-pro-reviews/26653?page=3
- https://www.cultofmac.com/news/first-look-apple-vision-pro

Cautious language: correlation not causation, MANUAL ILLUSTRATIVE only,
p_value NOT_CALCULATED, cohens_d NOT_CALCULATED, ci NOT_CALCULATED,
is_significant False. Dek/quote-level analysis only; full-text tone coding not
done.

Confidence: MEDIUM - quotes confirmed across 4 independent secondary sources;
timing proximity (7 weeks) strengthens comparability.

Goal and job IDs: goal_54093bda4145 mediascope-daily-iteration iteration 484 Type B 2026-09-03 02:00 PDT
"""

import yaml
from pathlib import Path

MECH_KEY = "brian_x_chen_meta_vs_apple_privacy_vocabulary_bifurcation_484"
SOURCES = [
    "https://pxlnv.com/linklog/meta-ray-bans-privacy/",
    "https://www.resource.dnsafrica.org/2024/01/27/making-vr-headsets-cool-wont-be-easy-even-for-apple-the-new-york-times/",
    "https://talk.tidbits.com/t/impressions-and-thoughts-from-early-vision-pro-reviews/26653?page=3",
    "https://www.cultofmac.com/news/first-look-apple-vision-pro",
]


def _nyt():
    return yaml.safe_load(Path("profiles/nytimes.yaml").read_text())


def test_mechanism_484_exists_in_nyt_yaml():
    d = _nyt()
    assert MECH_KEY in d, "mechanism 484 top-level key must exist"
    m = d[MECH_KEY]
    assert m["mechanism_id"] == 484
    assert m["iteration"] == 484
    assert m["iteration_type"] == "B"
    assert m["journalist"] == "Brian X. Chen"


def test_brian_x_chen_journalist_entry_exists():
    d = _nyt()
    names = [j.get("name") for j in d.get("key_journalists", [])]
    assert "Brian X. Chen" in names
    entry = next(j for j in d["key_journalists"] if j.get("name") == "Brian X. Chen")
    cca = entry["cross_entity_coverage_analysis"]
    assert cca["mechanism_id"] == 484
    assert "Gilliard" in cca["summary"]
    assert "200" in cca["summary"]


def test_mechanism_484_meta_evidence():
    m = _nyt()[MECH_KEY]
    assert m["manual_illustrative"]["meta_privacy_terms_in_quotes"] >= 5
    assert m["manual_illustrative"]["apple_privacy_terms_in_quotes"] == 0
    assert m["is_significant"] is False
    assert m["p_value"] == "NOT_CALCULATED"


def test_mechanism_484_sources_present():
    m = _nyt()[MECH_KEY]
    for s in SOURCES:
        assert s in m["sources"], f"missing source {s}"


def test_mechanism_484_confounder_documented():
    d = _nyt()
    entry = next(j for j in d["key_journalists"] if j.get("name") == "Brian X. Chen")
    confounders = entry["cross_entity_coverage_analysis"]["confounders"]
    assert any("STRONG" in c for c in confounders), "strong confounder must be documented"
    assert any("Cambridge" in c or "privacy history" in c for c in confounders)


def test_mechanism_484_cautious_language():
    m = _nyt()[MECH_KEY]
    assert m["cohens_d"] == "NOT_CALCULATED"
    assert m["ci"] == "NOT_CALCULATED"
    assert m["confidence"] == "MEDIUM"
    d = _nyt()
    entry = next(j for j in d["key_journalists"] if j.get("name") == "Brian X. Chen")
    cl = entry["cross_entity_coverage_analysis"]["cautious_language"]
    assert "Correlation not causation" in cl


def test_mechanism_484_cross_references():
    m = _nyt()[MECH_KEY]
    refs = " ".join(m["cross_references"])
    assert "457" in refs
    assert "121" in refs
