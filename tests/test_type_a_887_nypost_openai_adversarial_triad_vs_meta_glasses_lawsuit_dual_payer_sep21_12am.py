"""Type A #887 (885-889 window, third leg D->E->A): NY Post x OpenAI adversarial
triad (Sep 9-19 2026) vs NY Post x Meta glasses-lawsuit arm (Sep 18 2026),
mechanism 763.

FIRST dedicated New York Post mechanism in the corpus (the only prior NY Post
item is an Aug-19 Apple AirPods coverage_example, not a mechanism). OpenAI arm
(3 pieces, all read first-hand this run, 40-77 rendered lines): Sep 19 insiders
piece accusing OpenAI+Anthropic of overselling rogue-AI breaches to manufacture
federal regulatory turf protection (-0.40); Sep 10 Senate-probe piece
("reckless", "redacting many important details", "terrifying situation", -0.50);
Sep 9 math-scoop piece (professor alleges OpenAI "cribbed his work" and a
scientist threatened "Why would you want to ruin your career?", -0.55). OpenAI
arm avg -0.483. Meta arm (first-hand, 80 lines): Sep 18 "Meta's AI glasses
accused in California lawsuit of secretly capturing sex, nudity and bathroom
footage" - 70+ plaintiffs, contractors in Kenya, Meta response carried
(-0.50). Illustrative OpenAI-minus-Meta delta +0.017: near-perfect register
symmetry between the two ~$50M/yr licensing payers AT ADVERSARIAL values -
#519's symmetry component confirmed, its softening component falsified on both
legs. The m697 deal-seniority gradient (senior leg softer, +0.60 at
MarketWatch) is CONTRADICTED at the Post: the 28-month OpenAI leg reads no
softer than the 6-month Meta leg. TWENTY-NINTH falsification-family member
(ledger 28->29): the News Corp x OpenAI ~$50M/yr May-2024 deal (NY Post content
explicitly in licensing scope; coverage_prediction: softer) is falsified at
the tabloid register by three adversarial pieces on the payer in 10 days.
Verdict directionally_supported_not_proven on the asymmetry (near-zero delta);
falsified_softer_prediction on the uniform-softening claim. MANUAL ILLUSTRATIVE
scores only; p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant false (Aug
28 2026 standing rule); engine NOT run; no analysis.json update; NOT
artifact-grade; correlation is not causation. Novelty verified pre-commit (zero
test_type_a_887 files; no Type A #887 in git log; Sep 10 and Sep 9 URL slugs
zero-hit repo-wide; Sep 19 URL carried as m757 counter-frame, not novel; Sep 18
Meta URL logged in Type E #846 press keys, not novel; block key zero-hit
repo-wide; max numeric mechanism_id 762 pre-commit; zero underscore-form 763
keys per #715); count_stats gate (patched post-collection); 885-889 window
third leg D->E->A (anchor patched post-commit per #565) - Sep 21 2026 00:00
PDT - 62 tests, 12 classes.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_a_887_nypost_openai_adversarial_triad_vs_meta_glasses_lawsuit_dual_payer_sep21_12am.py"
OWN_BASENAME = TEST_BASENAME
MECH_KEY = "nypost_openai_adversarial_triad_vs_meta_glasses_lawsuit_dual_payer_symmetry_sep21"
M_ID = 763
ITER = 887
TYPE_LETTER = "A"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_763"
NEXT_ID_MARKER = "mechanism" + "_764"
NEXT_ID_NUMERIC = "mechanism_id: 764"
NEXT_ID_DASH = "mechanism" + "-764"
MEMBER_29 = "TWENTY-NINTH falsification-family member"
MEMBER_28 = "TWENTY-EIGHTH falsification-family member"
EXPECTED_ORDER = [("A", "887"), ("E", "886"), ("D", "885"), ("B", "883")]
# Note: ("C", "884") is absent from EXPECTED_ORDER - the concurrent Type C
# #884 run is in-flight (m762 uncommitted in the working tree at this run's
# checks) and commits after this run; see test_window_is_885_889_third_leg.
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "8ed0ad0de4ee8f9f27df14435ff6f0fe72608f8c"

REPO = Path(__file__).resolve().parents[1]


def _read(rel):
    return (REPO / rel).read_text(encoding="utf-8")


def _git(*args):
    return subprocess.run(["git", "-C", str(REPO), *args],
                          capture_output=True, text=True, timeout=60)


def _profiles_text():
    return _read("profiles/news-corp.yaml")


def _get_block():
    text = _profiles_text()
    start = text.index(MECH_KEY)
    end = text.index("\n\n  meta:")
    return yaml.safe_load(text[start:end])[MECH_KEY]


def _corpus_ids():
    ids = []
    for p in (REPO / "profiles").rglob("*.yaml"):
        for m in re.finditer(r"mechanism_id:\s*(\d+)", p.read_text(errors="ignore")):
            ids.append(int(m.group(1)))
    return ids


def _repo_grep(needle, roots=("profiles", "tests")):
    hits = []
    for r in roots:
        for p in (REPO / r).rglob("*"):
            if p.is_file() and p.suffix in (".py", ".yaml", ".md", ".json"):
                try:
                    if needle in p.read_text(errors="ignore"):
                        hits.append(str(p.relative_to(REPO)))
                except OSError:
                    pass
    return hits


# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------

class TestNovelty887:
    def test_single_test_type_a_887_file(self):
        files = [f for f in os.listdir(REPO / "tests")
                 if f.startswith("test_type_a_887")]
        assert files == [OWN_BASENAME]

    def test_type_a_887_main_commit_unique_and_anchored(self):
        # DESELECTED pre-commit (per #565): the commit does not exist yet.
        proc = _git("log", "--format=%H %s", "--grep", "Type A #887")
        mains = [ln for ln in proc.stdout.splitlines()
                 if re.search(r"Type A #887(?::| )", ln)
                 and "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) == 1
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
                                    "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565")
        assert mains[0].startswith(ANCHORED_SHA + " ")

    def test_novelty_verification_claim(self):
        block = _get_block()
        novelty = block["novelty"]
        assert "test_type_a_887 files on disk pre-commit" in novelty
        assert 'no "Type A #887" in git log pre-commit' in novelty
        assert "block key unique repo-wide pre-commit" in novelty
        assert "max numeric mechanism_id 762 pre-commit" in novelty
        assert "zero underscore-form 763" in novelty

    def test_885_886_window_legs_present_prior_to_887(self):
        log = _read("iteration-log.md")
        assert "## #885 Type D:" in log
        assert "## #886 Type E:" in log
        idx_885 = log.index("## #885 Type D:")
        idx_886 = log.index("## #886 Type E:")
        assert idx_886 < idx_885

    def test_max_numeric_mechanism_id_763(self):
        """Max numeric mechanism_id in profiles/ is 763: this run's own
        addition (762 was the max pre-commit per the run's pre-commit grep)."""
        ids = _corpus_ids()
        assert max(ids) == 763, f"max mechanism_id should be 763, got {max(ids)}"
        assert ids.count(763) == 1, "mechanism_id 763 must appear exactly once"

    def test_no_underscore_764_keys(self):
        """Zero underscore-form 764 mechanism key strings repo-wide
        (format-built needle; __pycache__ excluded per #715)."""
        hits = _repo_grep(NEXT_ID_MARKER)
        assert hits == [], f"unexpected underscore-764 keys: {hits}"

    def test_no_dash_764_keys(self):
        hits = _repo_grep(NEXT_ID_DASH)
        assert hits == [], f"unexpected dash-764 keys: {hits}"

    def test_no_numeric_764_keys(self):
        hits = _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",))
        assert hits == [], f"unexpected numeric 764 keys: {hits}"


# ---------------------------------------------------------------------------
# 2. Rotation guard: 885-889 window, third leg D->E->A
#    (All rotation-guard tests DESELECTED pre-commit per #565.)
# ---------------------------------------------------------------------------

class TestRotationGuard887:
    def test_window_is_885_889_third_leg(self):
        # The concurrent Type C #884 run commits after this run; its main
        # commit is absent from git history. Match only commit SUBJECTS:
        # other commits' bodies may mention #884 (this run's own
        # concurrency note does). Iteration numbers follow the rotation
        # schedule, not commit order, so the subject sequence must read
        # 887 -> 886 -> 885 -> 883 with the in-flight 884 skipped.
        subjects = _git("log", "--format=%s", "-25").stdout.splitlines()
        nums = []
        for s in subjects:
            m = re.match(r"Type [A-E] #(\d+)", s)
            if m and (not nums or nums[-1] != m.group(1)):
                # Followups and test-fixups are not rotation legs. The
                # push-status followup commit type (introduced at #864)
                # is excluded alongside anchor/log-hash followups.
                if ("anchor followup" not in s and "log-hash followup" not in s
                        and "push-status followup" not in s and "test fixup" not in s):
                    nums.append(m.group(1))
        assert nums[:4] == ["887", "886", "885", "883"], nums[:4]
        assert "884" not in nums

    def test_rotation_adjacency_cycle_valid(self):
        cycle = ["D", "E", "A", "B", "C"]
        got = [t for t, _n in EXPECTED_ORDER]
        assert got == ["A", "E", "D", "B"]
        assert cycle[cycle.index("D") + 1] == "E"
        assert cycle[cycle.index("E") + 1] == "A"
        assert cycle[cycle.index("A") + 1] == "B"
        assert cycle[cycle.index("B") + 1] == "C"

    def test_predecessor_is_type_e_886(self):
        proc = _git("log", "--oneline", "--grep", "Type E #886", "--all")
        mains = [ln for ln in proc.stdout.splitlines()
                 if "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) >= 1

    # NOTE (per the #885/#886 convention): ANCHORED_SHA pins the MAIN commit;
    # the anchor/log-hash followups legitimately advance HEAD past it, so the
    # old assert-ANCHORED_SHA-equals-HEAD shape is retired. The live invariant
    # is ancestry: the anchored main commit must be an ancestor of HEAD.
    def test_anchor_is_ancestor_of_head(self):
        proc = _git("merge-base", "--is-ancestor", ANCHORED_SHA, "HEAD")
        assert proc.returncode == 0, (
            "anchored main commit must be an ancestor of HEAD")


# ---------------------------------------------------------------------------
# 3. Novelty anchor: block key shape
#    (DESELECTED pre-commit per #565.)
# ---------------------------------------------------------------------------

class TestNoveltyAnchor887:
    def test_block_key_shape(self):
        assert MECH_KEY.startswith("nypost_openai_adversarial_triad")
        assert MECH_KEY.endswith("dual_payer_symmetry_sep21")
        assert "meta_glasses_lawsuit" in MECH_KEY
        assert MECH_KEY == "nypost_openai_adversarial_triad_vs_meta_glasses_lawsuit_dual_payer_symmetry_sep21"


# ---------------------------------------------------------------------------
# 4. Mechanism 763 YAML structure
# ---------------------------------------------------------------------------

class TestMechanism763Structure:
    def test_block_key_unique_in_yaml(self):
        """The 887 block key appears exactly once repo-wide in yaml."""
        hits = _repo_grep(MECH_KEY)
        yaml_hits = [h for h in hits if h.endswith(".yaml")]
        assert len(yaml_hits) == 1, f"block key should appear in exactly 1 yaml file, got {yaml_hits}"
        assert yaml_hits[0].endswith("profiles/news-corp.yaml")

    def test_iteration_and_type(self):
        block = _get_block()
        assert block["iteration"] == 887
        assert block["iteration_type"] == "A"
        assert block["type"] == "competitor_coverage_deep_dive"
        assert block["type_label"] == "Competitor Coverage Deep Dive"
        assert block["rotation"] == "Type A"
        assert block["mechanism_id"] == 763

    def test_date_grounding(self):
        block = _get_block()
        assert block["date_analyzed"] == "2026-09-21"
        assert block["time_pdt"] == "00:00"
        assert block["job_id"] == "mediascope-daily-iteration"
        assert block["goal_id"] == "goal_54093bda4145"

    def test_author(self):
        assert _get_block()["author"] == "Kit (with Ray)"

    def test_first_dedicated_nypost_mechanism(self):
        block = _get_block()
        assert "FIRST dedicated New York Post mechanism" in block["distinct_from_prior"]

    def test_block_lives_under_openai(self):
        data = yaml.safe_load(_profiles_text())
        openai = data["competitor_relationships"]["openai"]
        assert MECH_KEY in openai


# ---------------------------------------------------------------------------
# 5. Mechanism 763 OpenAI arms
# ---------------------------------------------------------------------------

class TestMechanism763OpenAiArms:
    def test_three_openai_arms(self):
        arms = _get_block()["articles_openai"]
        assert len(arms) == 3

    def test_arm1_oversold_insiders(self):
        arm = _get_block()["articles_openai"][0]
        assert "oversold AI security breaches" in arm["title"]
        assert "openai-anthropic-oversold-security-breaches-to-pressure-feds-into-protecting-turf-insiders" in arm["url"]
        assert arm["date"] == "2026-09-19"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.40
        assert arm["register"] == "insider_deflation_regulatory_capture_accusation"
        assert "Don't believe the byte!" in arm["key_quotes"]

    def test_arm2_senate_probe(self):
        arm = _get_block()["articles_openai"][1]
        assert "Senate probe over Hugging Face hack" in arm["title"]
        assert "openai-faces-senate-probe-over-hugging-face-hack" in arm["url"]
        assert arm["date"] == "2026-09-10"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.50
        assert arm["register"] == "incident_accountability_senate_scrutiny"
        assert any("reckless" in q for q in arm["key_quotes"])

    def test_arm3_math_scoop(self):
        arm = _get_block()["articles_openai"][2]
        assert "cribbed his work and then threatened him" in arm["title"]
        assert "openai-says-it-cracked-decades-old-math-problem" in arm["url"]
        assert arm["date"] == "2026-09-09"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.55
        assert arm["register"] == "allegation_led_scoop"
        assert any("ruin your career" in q for q in arm["key_quotes"])

    def test_all_openai_arms_first_hand(self):
        for arm in _get_block()["articles_openai"]:
            assert "first_hand_browser_open_sep21_887" in arm["research_method"]
            assert arm["publication"] == "New York Post"

    def test_openai_arm_urls_verbatim_nypost(self):
        for arm in _get_block()["articles_openai"]:
            assert arm["url"].startswith("https://nypost.com/2026/09/")

    def test_openai_avg_minus_0_483(self):
        scorer = _get_block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["target_scores_MANUAL_ILLUSTRATIVE"] == [-0.40, -0.50, -0.55]
        assert scorer["target_avg"] == -0.483


# ---------------------------------------------------------------------------
# 6. Mechanism 763 Meta arm
# ---------------------------------------------------------------------------

class TestMechanism763MetaArm:
    def test_meta_arm_title_url(self):
        arm = _get_block()["articles_meta"][0]
        assert "secretly capturing sex, nudity and bathroom footage" in arm["title"]
        assert "california-users-among-plaintiffs-suing-meta-over-smart-glasses" in arm["url"]
        assert arm["date"] == "2026-09-18"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.50
        assert arm["register"] == "lawsuit_liability_watchdog_fair_process"

    def test_meta_response_carried(self):
        quotes = _get_block()["articles_meta"][0]["key_quotes"]
        assert any("Meta disputes the allegations" in q for q in quotes)

    def test_meta_arm_first_hand_80_lines(self):
        arm = _get_block()["articles_meta"][0]
        assert "first_hand_browser_open_sep21_887" in arm["research_method"]
        assert "80 rendered lines" in arm["research_method"]

    def test_meta_url_novelty_honest(self):
        arm = _get_block()["articles_meta"][0]
        assert "NOT mechanism-registered" in arm["url_status"]
        assert "Type E #846" in arm["url_status"]


# ---------------------------------------------------------------------------
# 7. Mechanism 763 scorer
# ---------------------------------------------------------------------------

class TestMechanism763Scorer:
    def test_peer_score_and_avgs(self):
        scorer = _get_block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["peer_scores_MANUAL_ILLUSTRATIVE"] == [-0.50]
        assert scorer["peer_avg"] == -0.50
        assert scorer["target_entity"] == "openai"
        assert scorer["peer_entity"] == "meta"

    def test_delta_plus_0_017(self):
        scorer = _get_block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["delta"] == 0.017
        assert scorer["delta_calc"] == "-0.483 - (-0.50) = +0.017"

    def test_statistical_discipline(self):
        scorer = _get_block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["p_value"] == "NOT_CALCULATED - illustrative only, standing rule Aug 28 2026"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci_95"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False
        assert "Engine NOT run" in scorer["methodology"]

    def test_dual_verdict(self):
        block = _get_block()
        assert "directionally_supported_not_proven" in block["finding"]
        assert "falsified_softer_prediction" in block["finding"]

    def test_incentive_attribution_falsified(self):
        assert "FALSIFIED_SOFTER_PREDICTION" in _get_block()["incentive_attribution"]

    def test_correlation_not_causation(self):
        block = _get_block()
        assert block["correlation_not_causation"] is True
        assert "correlation is not causation" in block["finding"].lower()


# ---------------------------------------------------------------------------
# 8. Mechanism 763 research discipline
# ---------------------------------------------------------------------------

class TestMechanism763Discipline:
    def test_confounder_classes_ranked(self):
        conf = _get_block()["confounders_ranked"]
        assert set(conf.keys()) == {"strong", "moderate", "weak"}
        assert len(conf["strong"]) >= 3
        assert any("tabloid genre" in c for c in conf["strong"])

    def test_counter_evidence_marketwatch_register_local(self):
        ce = _get_block()["counter_evidence"]
        assert any("m697" in c for c in ce)
        assert any("register-local" in c or "register local" in c for c in ce)

    def test_no_analysis_json_update_and_not_artifact_grade(self):
        block = _get_block()
        assert block["no_analysis_json_update"] is True
        assert "NOT artifact-grade" in block["statistical_discipline"]
        assert "ascii-only" in block["research_method"].lower() or "ASCII-only" in block["research_method"]


# ---------------------------------------------------------------------------
# 9. Falsification ledger transition 28 -> 29
# ---------------------------------------------------------------------------

class TestLedgerTransition887:
    def test_exactly_one_29th_member_in_profiles(self):
        count = _repo_grep(MEMBER_29, roots=("profiles",))
        assert len(count) == 1, count

    def test_29th_member_is_m763_nypost(self):
        text = _profiles_text()
        assert text.count(MEMBER_29) == 1
        assert "(ledger 28->29)" in text

    def test_28th_member_still_exactly_once(self):
        count = _repo_grep(MEMBER_28, roots=("profiles",))
        assert len(count) == 1, count

    def test_no_30th_member_form(self):
        assert _repo_grep("THIRTIETH falsification-family member", roots=("profiles",)) == []

    def test_block_ledger_28_to_29(self):
        block = _get_block()
        assert "ledger 28->29" in block["falsification_family"]
        assert "28->29" in block["ledger"]

    def test_verge_guard_advanced_to_30th(self):
        verge = _read("profiles/the-verge.yaml")
        assert "negative-guard convention continues at THIRTIETH" in verge
        assert "TWENTY-NINTH member-form landed in profiles/news-corp.yaml" in verge
        assert "Type A #887 mechanism 763" in verge


# ---------------------------------------------------------------------------
# 10. Doc sync: README + ARCHITECTURE
# ---------------------------------------------------------------------------

class TestDocSync887:
    def test_readme_test_count_gate(self):
        readme = _read("README.md")
        assert "| Tests | 45428 |" in readme
        assert "Across 1214 test files" in readme

    def test_readme_type_a_table_row(self):
        assert TEST_BASENAME in _read("README.md")

    def test_architecture_test_count_gate(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "45428" in arch and "1214" in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in _read("docs/ARCHITECTURE.md")


# ---------------------------------------------------------------------------
# 11. Iteration log
# ---------------------------------------------------------------------------

class TestIterationLog887:
    def test_log_captures_iteration_887(self):
        head = _read("iteration-log.md")[:4000]
        assert "## #887 Type A:" in head
        assert "00:00 PDT" in head
        assert "m763" in head

    def test_log_states_885_889_window(self):
        assert "885-889" in _read("iteration-log.md")[:4000]

    def test_log_ledger_28_to_29(self):
        head = _read("iteration-log.md")[:4000]
        assert "28->29" in head
        assert "TWENTY-NINTH" in head

    def test_log_first_dedicated_nypost(self):
        head = _read("iteration-log.md")[:4000]
        assert "New York Post" in head


# ---------------------------------------------------------------------------
# 12. Supersession and corpus integrity post-#886
# ---------------------------------------------------------------------------

class TestSupersessionAndCorpusPost886:
    def test_max_numeric_id_is_763_not_762(self):
        assert max(_corpus_ids()) == 763, (
            f"max numeric mechanism_id must be 763, got {max(_corpus_ids())}"
        )

    def test_zero_underscore_764_keys_repo_wide(self):
        assert _repo_grep(NEXT_ID_MARKER) == [], "no underscore-form 764 keys anywhere"

    def test_zero_numeric_764_keys_in_profiles(self):
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == [], (
            "no numeric 764 mechanism keys in the corpus"
        )

    def test_no_second_763_block_key_variant(self):
        assert _profiles_text().count(MECH_KEY) == 1

    def test_d886_zero_underscore_763_profiles_sweep_stays_green(self):
        assert _repo_grep(MECH_ID_MARKER, roots=("profiles",)) == [], (
            "#886 zero-underscore-763 profiles sweep stays green by designed keying"
        )

    def test_d886_zero_underscore_763_tests_sweep_stays_green(self):
        hits = [
            h
            for h in _repo_grep(MECH_ID_MARKER, roots=("tests",))
            if not h.endswith(TEST_BASENAME)
        ]
        assert hits == [], (
            "#886 zero-underscore-763 tests sweep stays green (own file excluded "
            "as sweep carrier per #715)"
        )

    def test_d886_zero_numeric_763_profiles_sweep_superseded_by_design(self):
        hits = _repo_grep("mechanism_id: 763", roots=("profiles",))
        assert len(hits) >= 1, (
            "#886 zero-numeric-763 sweep is superseded by design: the #887 block "
            "is the single numeric 763 key"
        )

    def test_d886_max_762_sweep_superseded_by_design(self):
        assert max(_corpus_ids()) == 763, (
            "#886 max-762 sweep is superseded by design: the corpus now maxes at 763"
        )

    def test_zero_dash_763_references_repo_wide(self):
        assert _repo_grep(NEXT_ID_DASH) == [], "no dash-form 763 references anywhere"
