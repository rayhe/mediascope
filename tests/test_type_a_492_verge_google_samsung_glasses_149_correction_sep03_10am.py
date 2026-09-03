"""
Type A 492: The Verge x Google/Samsung glasses - correction of #149 binary
zero-claim (privacy-equivalence dek reframes asymmetry as escalation gradient)
Sep 3 2026 10:00 PDT
Mechanism 492

Validates:
- YAML parsability of the-verge.yaml
- Mechanism 492 exists with required fields under
  competitor_relationships.google
- Preston Jul 22 2026 Verge hands-on evidence: title, author, date, verbatim
  dek, three independent HTTPS mirrors (theverge.com policy-blocked)
- Corrected counts: #81 standalone_glasses_articles_count 0 -> 1,
  #149 samsung_standalone_articles_total 0 -> 1, vocabulary_gap binary ->
  gradient, correction_492 note present on #149
- MANUAL ILLUSTRATIVE scorer delta -0.35, p_value 1.0, is_significant False,
  reproduced by live scorer run this iteration
- Financial context: PMC dual Google lawsuits + ad dependency + Warby Parker
  equity, correlate-only
- Ranked confounders: 3 STRONG, 2 MODERATE, 1 WEAK; counter-evidence recorded
- Cautious language: correlation_not_causation, correction-not-falsification
  of the escalation asymmetry
- No em dashes in new mechanism text, ASCII-only, HTTPS-only URLs
- Distinct from #149 (corrected), #112 (different Google item), #81
  (beat-assignment count), #431 (URL listed, framing never analyzed),
  #471/#472 (precedent family only)
- Iteration log rotation A correct (previous 491 E -> 492 A)
- Goal and job IDs present
"""

import re
from pathlib import Path

import yaml

MECH_KEY = "mechanism_492_verge_google_samsung_glasses_149_correction_privacy_equivalence_dek"
PROFILE = Path("profiles/the-verge.yaml")
ITER_LOG = Path("iteration-log.md")
TEST_FILE = Path("tests/test_type_a_492_verge_google_samsung_glasses_149_correction_sep03_10am.py")

DEK = "With a camera on every pair, Google's and Samsung's AI glasses face the same privacy problems as Meta's."


def _data():
    return yaml.safe_load(PROFILE.read_text())


def _mech():
    return _data()["competitor_relationships"]["google"][MECH_KEY]


def _mech_text():
    text = PROFILE.read_text()
    start = text.index(MECH_KEY)
    end = text.index("\n  microsoft:", start)
    return text[start:end]


def test_yaml_parsable():
    data = _data()
    assert "competitor_relationships" in data
    assert "google" in data["competitor_relationships"]


def test_mechanism_492_exists():
    text = PROFILE.read_text()
    assert MECH_KEY in text
    assert "mechanism_id: 492" in text
    assert "iteration: 492" in text
    assert 'iteration_type: "A"' in text
    assert "2026-09-03 10:00 PDT" in text
    assert "mediascope-daily-iteration" in text
    assert "goal_54093bda4145" in text


def test_publication_and_pair():
    mech = _mech()
    assert mech["publication_focus"] == "The Verge"
    assert mech["entity_pair"] == "Google/Samsung vs Meta"
    assert "Correction of #149" in mech["type"]


def test_preston_evidence_complete():
    mech = _mech()
    ev = mech["new_evidence"]
    assert ev["author"] == "Dominic Preston"
    assert ev["date"] == "2026-07-22"
    assert "Samsung's smart glasses actually look like" in ev["title"]
    assert ev["dek_verbatim"] == DEK
    assert "names Google" in ev["dek_significance"]


def test_three_independent_mirrors_https():
    mech = _mech()
    mirrors = mech["new_evidence"]["mirror_urls"]
    assert len(mirrors) == 3
    for url in mirrors:
        assert url.startswith("https://"), url
    assert any("technewstube.com" in u for u in mirrors)
    assert any("amkio.com" in u for u in mirrors)
    assert any("thetechstreetnow.com" in u for u in mirrors)


def test_verification_method_states_block():
    mech = _mech()
    vm = mech["new_evidence"]["verification_method"]
    assert "policy-blocked" in vm
    assert "Secondary verification" in vm


def test_corrected_claims_documented():
    mech = _mech()
    claims = {c["claim"]: c for c in mech["corrected_claims"]}
    assert any("samsung_standalone_articles_total" in k for k in claims)
    assert any("ZERO privacy vocabulary" in k for k in claims)
    assert any("standalone_glasses_articles_count" in k for k in claims)
    assert any("vocabulary_gap binary" in k for k in claims)
    statuses = " ".join(c["status"] for c in mech["corrected_claims"])
    assert "falsified" in statuses
    assert "reframed" in statuses


def test_81_count_corrected_in_yaml():
    cea = _data()["cross_entity_coverage_analysis"]
    paradox = cea["samsung_unpacked_beat_assignment_paradox"]
    assert paradox["standalone_glasses_articles_count"] == 1
    assert "correction_492_note" in paradox
    assert "0 -> 1" in paradox["correction_492_note"]


def test_149_count_and_gap_corrected_in_yaml():
    cea = _data()["cross_entity_coverage_analysis"]
    m149 = cea["pmc_google_double_incentive_samsung_glasses"]
    cc = m149["coverage_comparison"]
    assert cc["samsung_standalone_articles_total"] == 1
    assert "samsung_standalone_article_correction_492" in cc
    assert "gradient" in cc["vocabulary_gap"]
    assert "binary" in cc["vocabulary_gap"]
    assert "correction_492_sep03_2026" in m149
    assert m149["correction_492_sep03_2026"]["mechanism_ref"] == "#492"


def test_meta_comparator_set_three_articles():
    mech = _mech()
    meta_set = mech["meta_comparator_set"]
    assert len(meta_set) == 3
    assert all(a["author"] == "Victoria Song" for a in meta_set)
    assert all(a["tone_illustrative"] < 0 for a in meta_set)


def test_scorer_manual_illustrative_documented():
    mech = _mech()
    sc = mech["scorer_manual_illustrative"]
    assert sc["target_scores"] == [-0.55, -0.6, -0.5]
    assert sc["peer_scores"] == [-0.2]
    assert sc["target_avg"] == -0.55
    assert sc["peer_avg"] == -0.2
    assert sc["asymmetry_delta"] == -0.35
    assert sc["p_value"] == 1.0
    assert sc["is_significant"] is False
    assert "MANUAL ILLUSTRATIVE" in sc["note"]
    assert "n=1 peer side" in sc["note"]


def test_scorer_reproduces_live():
    from mediascope.scoring import AsymmetryScorer

    scorer = AsymmetryScorer(target_entity="Meta")
    res = scorer.score(
        target_scores=[-0.55, -0.6, -0.5],
        peer_scores=[-0.2],
        peer_entities=["Google/Samsung"],
        publication_slug="the-verge",
        period_start="2026-07-07",
        period_end="2026-07-31",
    )
    assert abs(res.asymmetry_score - (-0.35)) < 1e-9
    assert res.is_significant is False
    s = str(res)
    assert "peer_avg_tone=-0.2" in s
    assert "p_value=1.0" in s
    # Documented finding agrees with live scorer: not significant.
    assert _mech()["scorer_manual_illustrative"]["is_significant"] is False


def test_financial_context_correlate_only():
    mech = _mech()
    fc = mech["financial_context"]
    assert "dual Google lawsuits" in fc
    assert "Warby" in fc
    assert "Correlate only" in fc
    assert "Correlation not causation" in fc


def test_confounders_ranked_counts():
    mech = _mech()
    conf = mech["ranked_confounders"]
    assert len(conf["strong"]) == 3
    assert len(conf["moderate"]) == 2
    assert len(conf["weak"]) == 1
    strong_text = " ".join(conf["strong"])
    assert "news-peg" in strong_text or "news peg" in strong_text
    assert "Preston" in strong_text
    assert "lawsuits" in strong_text or "litigation" in strong_text


def test_counter_evidence_recorded():
    mech = _mech()
    ce = " ".join(mech["counter_evidence"])
    assert "names Google with privacy problems" in ce
    assert "J.A.R.V.I.S." in ce
    assert "wear-detection" in ce


def test_statistical_discipline():
    mech = _mech()
    sd = mech["statistical_discipline"]
    assert "correlation_not_causation" in sd
    assert "MANUAL ILLUSTRATIVE" in sd
    assert "is_significant false" in sd


def test_surviving_asymmetry_is_escalation_not_existence():
    mech = _mech()
    sa = mech["surviving_asymmetry"]
    assert "escalation" in sa
    assert "3+" in sa
    assert "dek" in sa


def test_cross_references_distinct_units():
    mech = _mech()
    cr = " ".join(mech["cross_references"])
    assert "#149" in cr
    assert "#112" in cr
    assert "#81" in cr
    assert "#431" in cr
    assert "#471" in cr
    assert "#472" in cr
    distinct = mech["distinct_from_prior"]
    assert "First Verge x Google Type A correction" in distinct
    assert "0 -> 1" in distinct
    assert "Microsoft PCM" in distinct


def test_no_em_dash_ascii_only_in_mechanism_text():
    seg = _mech_text()
    seg.encode("ascii")
    assert "\u2014" not in seg
    assert "\u2013" not in seg


def test_https_only_urls_in_mechanism_text():
    seg = _mech_text()
    for m in re.finditer(r'https?://[^\s"\']+', seg):
        assert m.group(0).startswith("https://"), m.group(0)


def test_testable_predictions_present():
    mech = _mech()
    preds = mech["testable_predictions"]
    assert len(preds) == 2
    assert any("fall 2026" in p for p in preds)


def test_artifact_readiness_no_update():
    mech = _mech()
    assert "No analysis.json update warranted" in mech["artifact_readiness"]


def _heading_pos(marker):
    # Line-anchored search (fixed #495b): plain str.index() matched quoted
    # mentions of the heading literal inside newer entries' prose (the #495
    # entry quotes "#492 Type A:" when describing the repaired assertion).
    m = re.search(r"^" + re.escape(marker), ITER_LOG.read_text(), re.MULTILINE)
    assert m, f"heading not found: {marker}"
    return m.start()


def _segment_between(start_marker, end_marker):
    log = ITER_LOG.read_text()
    start = _heading_pos(start_marker)
    end = _heading_pos(end_marker)
    assert start < end
    return log[start:end]


def test_iteration_log_rotation():
    # Relative newest-first ordering (fixed #495): the absolute
    # log.startswith("#492 Type A:") assertion broke when #493 was
    # legitimately prepended. The rotation invariant is relative order.
    i493 = _heading_pos("#493 Type B:")
    i492 = _heading_pos("#492 Type A:")
    i491 = _heading_pos("#491 Type E:")
    assert i493 < i492 < i491
    seg = _segment_between("#492 Type A:", "#491 Type E:")
    assert "Previous entry #491 Type E at 09:00 PDT Sep 3 2026" in seg
    assert "next after E is A" in seg


def test_novelty_block_present():
    # Scoped to the #492 entry segment (fixed #495): the old head-slice
    # check broke once newer entries pushed #492 past 6000 chars.
    seg = _segment_between("#492 Type A:", "#491 Type E:")
    assert "Novelty Verification" in seg
    assert "#149" in seg
    assert "Zero test_type_a files pair Verge with Google" in seg


def test_self_reference():
    content = TEST_FILE.read_text()
    assert "test_type_a_492_verge_google_samsung_glasses_149_correction_sep03_10am" in content
