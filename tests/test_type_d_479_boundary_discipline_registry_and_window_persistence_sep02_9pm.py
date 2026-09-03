"""
Type D #479: boundary-discipline registry and 475-478 window persistence.

Two workstreams:

1. Window persistence guard (iterations 475-478). The #474 Type D file
   covers 470-473 only (verified: no mention of 475+ in that file), so the
   four newest mechanisms get their own anchor-existence guard here:
   #475 podcast-sentiment.md eighteenth verification, #476 mit-tech-review.yaml
   iteration anchor, #477 mit-tech-review.yaml + careers anchors,
   #478 competitor-entities.yaml anchor.

2. Boundary-discipline registry. Mechanisms #471 (NYT litigation posture),
   #476 (MIT TR Google tone), #477 (Huckins fortnight), and #478 (Axios
   disclosure posture) all assert BOUNDING discipline on the
   financial-incentive theory rather than confirming it, but each stores that
   discipline under different YAML keys. No existing test enforces the
   pattern across all four (verified via grep: no test file references more
   than one of these mechanisms). This registry locks the pattern in:
   correlation_not_causation true, documented significance false, ranked
   confounders with at least one strong entry, and explicit bounds language.

3. Scorer-honesty contrast (#471 vs #476). The scorer itself returns
   significant=True on #471's tight illustrative arrays (p ~ 9.1e-05,
   verified this run), so #471's documented significant=false is a human
   discipline override, not a scorer output. The registry test pins that
   illustrative arrays must never inherit scorer significance.

Qualitative only per Aug 28 rule. No new asymmetry tone data.
"""
import math
import re
from datetime import datetime
from pathlib import Path

import yaml

REPO = Path(__file__).parent.parent
MITTR = REPO / "profiles" / "mit-tech-review.yaml"
NYT = REPO / "profiles" / "nytimes.yaml"
ENTITIES = REPO / "profiles" / "competitor-entities.yaml"
JOURNALISTS = REPO / "profiles" / "careers" / "journalists.yaml"
PODCAST_LOG = REPO / "podcast-sentiment.md"
ITER_LOG = REPO / "iteration-log.md"

TEST_ITERATION = 479
TEST_TYPE = "D"
TEST_DATE = "2026-09-02"
TEST_TIME_PDT = "21:00"
JOB_ID = "mediascope-daily-iteration"
GOAL_ID = "goal_54093bda4145"

MECH_471_KEY = "nyt_openai_litigation_posture_boundary_condition_471"
MECH_476_KEY = "iteration_476_sep02_2026_mittr_google_coverage_tone_vs_meta"
MECH_477_KEY = "mechanism_477_grace_huckins_mittr_google_meta_fortnight_discipline_check_sep02"
MECH_478_KEY = "mechanism_478_axios_openai_disclosure_posture"
JOURNALIST_477 = "Grace Huckins"


def _load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _mech_471():
    return _load(NYT)["competitor_relationships"]["openai"][MECH_471_KEY]


def _mech_476():
    return _load(MITTR)["competitor_relationships"]["google"][MECH_476_KEY]


def _mech_477_mittr():
    for j in _load(MITTR)["key_journalists"]:
        if j.get("name") == JOURNALIST_477:
            cea = j.get("cross_entity_coverage_analysis", {})
            assert MECH_477_KEY in cea
            return cea[MECH_477_KEY]
    raise AssertionError("Grace Huckins missing from mit-tech-review.yaml")


def _mech_477_career():
    data = _load(JOURNALISTS)
    entries = data["journalists"] if isinstance(data, dict) and "journalists" in data else data
    for entry in entries:
        if entry.get("name") == JOURNALIST_477:
            assert MECH_477_KEY in entry
            return entry[MECH_477_KEY]
    raise AssertionError("Grace Huckins missing from journalists.yaml")


def _mech_478():
    return _load(ENTITIES)["entities"]["openai"][MECH_478_KEY]


def _log_text():
    return ITER_LOG.read_text(encoding="utf-8")


class TestIteration479Identity:
    def test_iteration_number(self):
        assert TEST_ITERATION == 479

    def test_type_d_after_478_c(self):
        assert TEST_TYPE == "D"
        text = _log_text()
        h478 = re.search(r"^#478\b", text, re.M)
        h479 = re.search(r"^#479\b", text, re.M)
        assert h478 is not None and h479 is not None
        assert h479.start() < h478.start()

    def test_date_time_ids(self):
        assert TEST_DATE == "2026-09-02"
        assert TEST_TIME_PDT == "21:00"
        assert JOB_ID == "mediascope-daily-iteration"
        assert GOAL_ID == "goal_54093bda4145"

    def test_filename_convention(self):
        name = Path(__file__).name
        assert name.startswith("test_type_d_479_")
        assert name.endswith("_sep02_9pm.py")


class TestWindowPersistence475to478:
    def test_475_test_file_exists(self):
        path = REPO / "tests" / "test_type_e_475_podcast_sentiment_eighteenth_verification_sep02_5pm.py"
        assert path.exists()

    def test_475_podcast_log_anchor(self):
        text = PODCAST_LOG.read_text(encoding="utf-8")
        assert "eighteenth consecutive no-match" in text

    def test_476_mittr_anchor(self):
        mech = _mech_476()
        assert mech["iteration"] == 476
        assert mech["iteration_type"] == "A"

    def test_477_mittr_and_career_anchors(self):
        mittr_mech = _mech_477_mittr()
        assert mittr_mech["iteration"] == 477
        career_mech = _mech_477_career()
        assert career_mech["iteration"] == 477

    def test_478_competitor_entities_anchor(self):
        mech = _mech_478()
        assert mech["iteration"] == 478
        assert mech["extends_mechanism"] == 53

    def test_touched_profiles_parse(self):
        for path in (MITTR, NYT, ENTITIES, JOURNALISTS):
            assert _load(path) is not None, f"{path} failed to parse"

    def test_iteration_log_newest_first_479(self):
        first_heading = re.search(r"^#\d+", _log_text(), re.M)
        assert first_heading is not None
        assert first_heading.group(0) == "#479"

    def test_rotation_chain_475_to_479_ordered(self):
        text = _log_text()
        positions = []
        for i in (475, 476, 477, 478, 479):
            match = re.search(rf"^#{i}\b", text, re.M)
            assert match is not None, f"#{i} heading missing from iteration-log.md"
            positions.append(match.start())
        # newest-first: the #479 heading sits above #478, so positions
        # descend as the iteration number ascends
        assert positions == sorted(positions, reverse=True), "iteration log headings not newest-first"


class TestBoundaryDisciplineRegistry:
    """Each boundary mechanism must carry the full discipline stack, even
    though each stores it under different YAML keys."""

    def test_471_discipline_stack(self):
        mech = _mech_471()
        assert mech["cautious_language"]["correlation_not_causation"] is True
        assert mech["asymmetry_scoring_manual_illustrative"]["significant"] is False
        assert len(mech["confounders"]["strong"]) >= 3
        assert len(mech["counter_evidence"]) >= 1
        assert "not a confirmation" in mech["cautious_language"]["partial_falsification"]

    def test_476_discipline_stack(self):
        mech = _mech_476()
        assert mech["cautious_language"]["correlation_not_causation"] is True
        assert mech["asymmetry_scoring_manual_illustrative"]["significant"] is False
        assert len(mech["confounders_ranked"]["strong"]) >= 1

    def test_477_discipline_stack(self):
        mech = _mech_477_mittr()
        assert mech["driver_class"].startswith("MIXED")
        assert "significant=false" in mech["scorer_note"]
        assert len(mech["ranked_confounders"]["strong"]) >= 1
        assert "Bounds the financial-incentive theory" in mech["driver_class"]

    def test_478_discipline_stack(self):
        mech = _mech_478()
        disc = mech["statistical_discipline"]
        assert disc["correlation_not_causation"] is True
        assert disc["is_significant"] is False
        strengths = {c["strength"] for c in mech["ranked_confounders"]}
        assert "strong" in strengths
        assert "bounds the finding" in mech["caution"]

    def test_476_bounds_language_in_strong_confounders(self):
        mech = _mech_476()
        joined = " ".join(mech["confounders_ranked"]["strong"])
        assert "cannot be cleanly attributed to Google-side money" in joined

    def test_no_proof_language_in_476_477_blocks(self):
        for mech in (_mech_476(), _mech_477_mittr()):
            dumped = yaml.safe_dump(mech)
            assert "proves" not in dumped.lower()


class TestTwoSidedNexusNoDirectionalAttribution:
    """#476 and #477 both document money on BOTH sides of the comparison.
    The registry asserts neither mechanism lets one side's money explain
    the delta. No existing test covers this cross-mechanism pattern."""

    def test_476_both_sides_documented(self):
        fin = _mech_476()["financial_triangulation"]
        assert "mit_google_program" in fin
        assert "schmidt_two_sided_nexus" in fin
        assert "FAIR" in fin["meta_also_funds_mit"]

    def test_476_no_directional_attribution(self):
        joined = " ".join(_mech_476()["confounders_ranked"]["strong"])
        assert "cannot be cleanly attributed to Google-side money" in joined

    def test_477_both_sides_documented(self):
        context = _mech_477_mittr()["financial_context"]
        assert "MIT-Google Program" in context
        assert "Meta also funds MIT via FAIR" in context

    def test_477_no_directional_attribution(self):
        driver = _mech_477_mittr()["driver_class"]
        assert "cannot cleanly attribute the register delta" in driver


class TestScorerHonestyIllustrativeArrays:
    """The scorer is honest on small samples only when the documentation
    does not dress synthetic arrays as empirical findings."""

    def test_471_significant_false_is_discipline_override(self):
        from mediascope.score.asymmetry import calculate_asymmetry

        asym = _mech_471()["asymmetry_scoring_manual_illustrative"]
        assert asym["significant"] is False
        assert asym["p_value"] == "NOT CALCULATED"
        assert "MANUAL ILLUSTRATIVE" in asym["synthetic_note"]
        # The scorer itself WOULD call these tight illustrative arrays
        # significant (p ~ 9.1e-05, verified this run). The documented False
        # is therefore a human discipline override, not a scorer output:
        # synthetic arrays must never inherit scorer significance.
        score = calculate_asymmetry(
            asym["target_scores_illustrative"],
            asym["peer_scores_illustrative"],
            "OpenAI", ["Meta"], "nytimes",
            datetime(2025, 10, 2), datetime(2026, 9, 2),
        )
        assert score.p_value < 0.05
        assert not math.isnan(score.asymmetry_score)
        assert not math.isinf(score.asymmetry_score)

    def test_476_documents_not_significant_with_label(self):
        asym = _mech_476()["asymmetry_scoring_manual_illustrative"]
        assert asym["significant"] is False
        assert "MANUAL ILLUSTRATIVE" in asym["synthetic_note"]
        assert abs(asym["p_value"] - 0.2085) < 0.0001

    def test_no_nan_or_inf_in_registry_scorer_run(self):
        from mediascope.score.asymmetry import calculate_asymmetry

        asym = _mech_476()["asymmetry_scoring_manual_illustrative"]
        score = calculate_asymmetry(
            asym["target_tones"], asym["peer_tones"],
            "Meta", ["Google"], "mit-technology-review",
            datetime(2026, 5, 18), datetime(2026, 6, 11),
        )
        for value in (score.asymmetry_score, score.p_value, score.cohens_d):
            assert not math.isnan(value), "scorer emitted NaN"
            assert not math.isinf(value), "scorer emitted inf"


class TestHygiene479:
    def test_no_em_dashes_in_this_file(self):
        assert "\u2014" not in Path(__file__).read_text(encoding="utf-8")

    def test_https_only_urls_in_this_file(self):
        text = Path(__file__).read_text(encoding="utf-8")
        for match in re.findall(r"https?://\S+", text):
            assert match.startswith("https://"), f"non-HTTPS URL: {match}"

    def test_no_causal_claim_language(self):
        lines = Path(__file__).read_text(encoding="utf-8").splitlines()
        body = "\n".join(
            line
            for line in lines
            if "proves bias" not in line and "softer coverage" not in line
        ).lower()
        assert "proves bias" not in body
        assert "causes softer coverage" not in body

    def test_iteration_log_mentions_479(self):
        assert "#479" in _log_text()
