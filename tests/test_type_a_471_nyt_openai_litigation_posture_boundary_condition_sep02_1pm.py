"""Type A #471 (2026-09-02 13:00 PDT): NYT x OpenAI litigation-posture boundary
condition - adversarial financial posture does not produce blanket adversarial
coverage.

Rotation: #470 was Type E (12:00 PDT) -> this run is Type A per A-B-C-D-E.

Mechanism: The NYT is itself the plaintiff suing OpenAI for billions (Dec 2023;
Aug 2026 statement: "widespread theft of millions of The Times's works").
Naive financial determinism predicts adversarial OpenAI coverage. Observed: NYT
newsroom coverage of OpenAI OUTSIDE the lawsuit domain (Sora product review Oct
2025; Musk v. Altman trial coverage Apr/May 2026) is neutral to substantive,
while NYT Meta coverage (mechanism #69) is adversarial on execution/social.
Recorded as a scope boundary condition and partial falsification: adversarial
posture predicts tone within the relationship domain, not blanket entity tone.

Evidence discipline: two of three NYT article URLs are third-party attested
(lexblog/vogelitlawblog quotation); nytimes.com is blocked by policy in this
environment so full NYT text was not directly fetched. Scores are MANUAL
ILLUSTRATIVE only. Correlation, not causation.
"""
from datetime import datetime
from pathlib import Path

import yaml

MECH_KEY = "nyt_openai_litigation_posture_boundary_condition_471"
PROFILE = Path("/home/hatch/workspace/repos/mediascope/profiles/nytimes.yaml")


def _mech():
    d = yaml.safe_load(PROFILE.read_text())
    return d["competitor_relationships"]["openai"][MECH_KEY]


def test_mechanism_key_exists():
    assert _mech()["mechanism"] == 471


def test_iteration_type_a():
    m = _mech()
    assert m["iteration"] == 471
    assert m["iteration_type"] == "A"
    assert "Type A" in m["type"]


def test_publication_pair():
    m = _mech()
    assert m["publication"] == "New York Times"
    assert m["competitor"] == "OpenAI"
    assert m["comparison_entity"] == "Meta"
    assert m["publication_pair"] == "NYT x OpenAI"


def test_goal_and_job_ids():
    m = _mech()
    assert m["goal_id"] == "goal_54093bda4145"
    assert m["job_id"] == "mediascope-daily-iteration"


def test_rotation_transparency():
    m = _mech()
    assert "470" in m["rotation_transparency"]
    assert "Type E" in m["rotation_transparency"]
    assert "Type A #471" in m["rotation_transparency"]


def test_three_nyt_articles():
    m = _mech()
    arts = m["nyt_openai_non_lawsuit_articles"]
    assert len(arts) == 3
    titles = " ".join(a["title"] for a in arts)
    assert "OpenAI Trial Is Set to Start" in titles
    assert "Intervened When OpenAI Fired Sam Altman" in titles
    assert "Sora Video App Is Jaw-Dropping" in titles


def test_article_dates_and_authors():
    m = _mech()
    arts = {a["title"]: a for a in m["nyt_openai_non_lawsuit_articles"]}
    trial = arts["The OpenAI Trial Is Set to Start"]
    assert trial["date"] == "2026-04-27"
    assert trial["desk"] == "DealBook"
    nadella = arts["Microsoft's C.E.O. Intervened When OpenAI Fired Sam Altman, Musk's Lawyer Claims"]
    assert nadella["date"] == "2026-05-11"
    assert "Cade Metz" in nadella["authors"]
    assert "Mike Isaac" in nadella["authors"]
    sora = arts["OpenAI's Sora Video App Is Jaw-Dropping (for Better and Worse)"]
    assert sora["date"] == "2025-10-02"


def test_article_urls_https_and_provenance():
    m = _mech()
    for a in m["nyt_openai_non_lawsuit_articles"]:
        assert a["url"].startswith("https://"), a["url"]
        assert "url_provenance" in a
        assert ("blocked by policy" in a["url_provenance"]
                or "Wayback Machine" in a["url_provenance"]), a["url_provenance"]


def test_sora_url_is_archived_primary():
    m = _mech()
    arts = {a["title"]: a for a in m["nyt_openai_non_lawsuit_articles"]}
    sora = arts["OpenAI's Sora Video App Is Jaw-Dropping (for Better and Worse)"]
    assert "web.archive.org" in sora["url"]
    assert "nytimes.com/2025/10/02/technology/openai-sora-video-app.html" in sora["url"]


def test_trial_article_key_phrases():
    m = _mech()
    arts = {a["title"]: a for a in m["nyt_openai_non_lawsuit_articles"]}
    trial = arts["The OpenAI Trial Is Set to Start"]
    phrases = " ".join(trial["key_phrases"])
    assert "trial of the artificial intelligence age" in phrases
    assert "future of the A.I. industry" in phrases


def test_lawsuit_domain_status_three_events():
    m = _mech()
    evts = m["lawsuit_domain_status_sep02_2026"]
    assert len(evts) == 3
    blob = " ".join(str(e) for e in evts)
    assert "fair-use" in blob or "fair use" in blob
    assert "Stein" in blob
    assert "widespread theft" in blob
    assert "sanctions" in blob


def test_lawsuit_domain_sources_verbatim():
    m = _mech()
    evts = m["lawsuit_domain_status_sep02_2026"]
    sources = [e["source"] for e in evts]
    assert "https://www.reuters.com/legal/litigation/us-government-backs-openai-new-york-times-copyright-case-2026-09-02/" in sources
    assert "https://www.globallegalpost.com/news/us-judge-refuses-openais-motion-to-dismiss-new-york-times-copyright-infringement-claims-887263879" in sources
    assert "https://www.reuters.com/legal/litigation/new-york-times-led-group-asks-court-sanction-openai-us-copyright-dispute-2026-07-09/" in sources


def test_meta_contrast_references_69():
    m = _mech()
    note = m["meta_contrast_mechanism_69"]["note"]
    assert "bifurcated" in note
    assert "mechanism #69" in m["finding"]


def test_metz_science_desk_context():
    m = _mech()
    ctx = " ".join(str(c) for c in m["institutional_context"])
    assert "Cade Metz" in ctx
    assert "Science desk" in ctx
    assert "https://www.citybiz.co/article/889210/new-york-times-moves-cade-metz-to-science-desk-to-cover-ai/" in ctx


def test_financial_posture_boundary():
    m = _mech()
    f = m["financial_posture"]
    assert "plaintiff" in f["nyt_openai"]
    assert f["nyt_meta"].startswith("none")
    assert "boundary condition" in f["direction"]


def test_asymmetry_manual_illustrative():
    m = _mech()
    a = m["asymmetry_scoring_manual_illustrative"]
    assert abs(a["delta_manual_illustrative"] - 0.65) < 0.001
    assert a["delta_manual_illustrative"] > 0
    assert a["significant"] is False
    assert a["p_value"] == "NOT CALCULATED"
    assert a["cohens_d"] == "NOT CALCULATED"
    assert a["confidence_interval"] == "NOT CALCULATED"
    assert "MANUAL ILLUSTRATIVE ONLY" in a["synthetic_note"]
    assert "inversion" in a["synthetic_note"]


def test_asymmetry_scorer_run():
    from mediascope.score.asymmetry import calculate_asymmetry
    target = [0.10, 0.05, 0.15]
    peers = [-0.55, -0.60, -0.50]
    score = calculate_asymmetry(
        target, peers, "OpenAI", ["Meta"], "nytimes",
        datetime(2025, 10, 2), datetime(2026, 9, 2),
    )
    assert abs(score.asymmetry_score - 0.65) < 0.001
    assert score.article_count_target == 3
    assert score.article_count_peers == 3
    # Scorer mechanics verified on illustrative arrays only; the YAML record
    # itself claims no empirical significance.


def test_confounders_ranked():
    m = _mech()
    c = m["confounders"]
    assert len(c["strong"]) >= 3
    assert len(c["moderate"]) >= 2
    assert len(c["weak"]) >= 1
    strong = " ".join(c["strong"]).lower()
    assert "church_state_firewall" in strong
    assert "genre_norms" in strong


def test_counter_evidence_present():
    m = _mech()
    ce = " ".join(m["counter_evidence"])
    assert "widespread theft" in ce
    assert "church-state firewall" in ce


def test_cautious_language():
    m = _mech()
    cl = m["cautious_language"]
    assert cl["correlation_not_causation"] is True
    assert cl["no_editorial_control_claim"] is True
    assert cl["no_statistical_significance_claim"] is True
    assert "partial_falsification" in cl
    assert "MANUAL ILLUSTRATIVE" in cl["manual_illustrative_label"]


def test_distinct_from_prior():
    m = _mech()
    d = " ".join(m["distinct_from_prior"])
    assert "#379" in d
    assert "#416" in d
    assert "#420" in d
    assert "no prior NYT x OpenAI Type A" in d


def test_no_em_dashes_in_section():
    text = PROFILE.read_text()
    start = text.find(MECH_KEY)
    end = text.find("\n  meta:", start)
    section = text[start:end]
    assert "\u2014" not in section
    assert "\u2013" not in section


def test_finding_states_boundary():
    m = _mech()
    assert "boundary condition" in m["finding"]
    assert "partial falsification" in m["finding"]


def test_mechanism_count_unique():
    text = PROFILE.read_text()
    assert text.count("mechanism: 471") == 1
    assert text.count(MECH_KEY) == 1


def test_date_format():
    m = _mech()
    datetime.strptime(m["date"], "%Y-%m-%d")
    assert m["date"] == "2026-09-02"
