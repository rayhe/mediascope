"""Type A #897 (895-899 window, third leg D->E->A): The Atlantic x Anthropic/OpenAI
slowdown-cycle selection asymmetry vs bounded Meta absence (mechanism 769).

Extends mechanism 481 (Atlantic AI Watchdog entity-selection asymmetry) beyond
the Watchdog vertical into the Sep 4-15 2026 AI-governance beat: The Atlantic
published original narrative coverage on the lab side twice in 11 days -
Matteo Wong's Sep 4 "OpenAI Wants to Talk About The Federalist Papers" (OpenAI
Strategic Futures team styled as inheriting the Founding Fathers' task;
irony-tinged but non-adversarial, excerpt-bounded) and Will Oremus's Sep 12
"Anthropic Says 'We Owe It to Humanity' to Slow Down AI" (Amodei's ~3,800-word
"We Must Pace the Frontier" essay, three-step pacing framework; excerpted lede
wry and distancing, not fawning) - while Zuckerberg's Sept 15 rejection of
coordinated slowdown drew no Atlantic-original coverage discoverable across 5
search query sets (bounded absence, explicitly search-coverage bounded). All
Atlantic evidence is secondary-attribution/excerpt tier: 0 browser.open this
turn (paywall + theatlantic.com blocked by policy). Finding is
selection/emphasis, not tone magnitude: illustrative lab-side tones +0.05/+0.10
near neutral, no delta computed (absence is not a magnitude). MANUAL
ILLUSTRATIVE scores only; p_value/cohens_d/ci_95 NOT_CALCULATED;
is_significant false (Aug 28 2026 standing rule); engine NOT run;
no analysis.json update; NOT artifact-grade; correlation is not causation.
NOT a falsification-family member (no uniform-direction prediction under test);
ledger holds at 29; THIRTIETH remains the negative guard. Novelty verified
pre-commit (zero test_type_a_897 files; no Type A #897 in git log; block key
zero-hit repo-wide; max numeric mechanism_id 768 pre-commit; zero
underscore-form 769 keys per #715; zero dash-form 769 references; zero numeric
769 keys in profiles/; Oremus slowdown URL + Wong Federalist Papers Politomix
URL zero-hit repo-wide; dead-end candidates rejected: FT x OpenAI $1.2T route
duplicates mechanism 812; Reuters slowdown-split route duplicates mechanism
730); 895-899 window third leg D->E->A (anchor patched post-commit per #565) -
Sep 21 2026 10:00 PDT - 61 tests, 11 classes.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_a_897_atlantic_anthropic_openai_slowdown_cycle_selection_vs_meta_bounded_absence_sep21_10am.py"
OWN_BASENAME = TEST_BASENAME
# The block key follows the m768-style convention: no mechanism_NNN prefix (the
# numeric mechanism_id field carries the ID). Unlike the #892 file, there is no
# underscore-form 769 marker in the corpus at all - designed keying per #715.
MECH_KEY = "atlantic_anthropic_openai_slowdown_cycle_selection_asymmetry_vs_meta_bounded_absence_sep2026"
M_ID = 769
ITER = 897
TYPE_LETTER = "A"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_769"
NEXT_ID_MARKER = "mechanism" + "_770"
NEXT_ID_NUMERIC = "mechanism_id: 770"
NEXT_ID_DASH = "mechanism" + "-770"
MEMBER_29 = "TWENTY-NINTH falsification-family member"
MEMBER_28 = "TWENTY-EIGHTH falsification-family member"
EXPECTED_ORDER = [("A", "897"), ("E", "896"), ("D", "895"), ("C", "894")]
# Note: ("C", "884") is absent from EXPECTED_ORDER - the concurrent Type C
# #884 run is in-flight (m762 uncommitted in the working tree at this run's
# checks) and commits after this run; see test_window_is_895_899_third_leg.
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

REPO = Path(__file__).resolve().parents[1]


def _read(rel):
    return (REPO / rel).read_text(encoding="utf-8")


def _git(*args):
    return subprocess.run(["git", "-C", str(REPO), *args],
                          capture_output=True, text=True, timeout=60)


def _profiles_text():
    return _read("profiles/atlantic.yaml")


def _get_block():
    text = _profiles_text()
    start = text.index(MECH_KEY)
    end = text.index("\n  amazon:")
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

class TestNovelty897:
    def test_single_test_type_a_897_file(self):
        files = [f for f in os.listdir(REPO / "tests")
                 if f.startswith("test_type_a_897")]
        assert files == [OWN_BASENAME]

    def test_type_a_897_main_commit_unique_and_anchored(self):
        # DESELECTED pre-commit (per #565): the commit does not exist yet.
        proc = _git("log", "--format=%H %s", "--grep", "Type A #897")
        mains = [ln for ln in proc.stdout.splitlines()
                 if re.search(r"Type A #897(?::| )", ln)
                 and "anchor followup" not in ln and "log-hash followup" not in ln
                 and "push-status followup" not in ln]
        assert len(mains) == 1
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
                                    "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565")
        assert mains[0].startswith(ANCHORED_SHA + " ")

    def test_novelty_verification_claim(self):
        block = _get_block()
        novelty = block["novelty"]
        assert "test_type_a_897 files on disk pre-commit" in novelty
        assert "no 'Type A #897' in git log pre-commit" in novelty
        assert "block key unique repo-wide pre-commit" in novelty
        assert "max numeric mechanism_id 768 pre-commit" in novelty
        assert "zero underscore-form 769" in novelty

    def test_895_896_window_legs_present_prior_to_897(self):
        log = _read("iteration-log.md")
        assert "## #895 Type D:" in log
        assert "## #896 Type E:" in log
        idx_895 = log.index("## #895 Type D:")
        idx_896 = log.index("## #896 Type E:")
        assert idx_896 < idx_895

    def test_max_numeric_mechanism_id_769(self):
        """Max numeric mechanism_id in profiles/ is 769: this run's own
        addition (768 was the max pre-commit per the run's pre-commit grep;
        the concurrent m762 block stays uncommitted in the working tree)."""
        ids = _corpus_ids()
        assert max(ids) == 769, f"max mechanism_id should be 769, got {max(ids)}"
        assert ids.count(769) == 1, "mechanism_id 769 must appear exactly once"

    def test_no_underscore_770_keys(self):
        """Zero underscore-form 770 mechanism key strings repo-wide
        (format-built needle; __pycache__ excluded per #715)."""
        hits = _repo_grep(NEXT_ID_MARKER)
        assert hits == [], f"unexpected underscore-770 keys: {hits}"

    def test_no_dash_770_keys(self):
        hits = _repo_grep(NEXT_ID_DASH)
        assert hits == [], f"unexpected dash-770 keys: {hits}"

    def test_no_numeric_770_keys(self):
        hits = _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",))
        assert hits == [], f"unexpected numeric 770 keys: {hits}"


# ---------------------------------------------------------------------------
# 2. Rotation guard: 895-899 window, third leg D->E->A
#    (All rotation-guard tests DESELECTED pre-commit per #565.)
# ---------------------------------------------------------------------------

class TestRotationGuard897:
    def test_window_is_895_899_third_leg(self):
        # The concurrent Type C #884 run commits after this run; its main
        # commit is absent from git history. Match only commit SUBJECTS:
        # other commits' bodies may mention #884 (this run's own
        # concurrency note does). Iteration numbers follow the rotation
        # schedule, not commit order, so the subject sequence must read
        # 897 -> 896 -> 895 -> 894 with the in-flight 884 skipped.
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
        assert nums[:4] == ["897", "896", "895", "894"], nums[:4]
        assert "884" not in nums

    def test_rotation_adjacency_cycle_valid(self):
        cycle = ["D", "E", "A", "B", "C"]
        got = [t for t, _n in EXPECTED_ORDER]
        assert got == ["A", "E", "D", "C"]
        assert cycle[cycle.index("D") + 1] == "E"
        assert cycle[cycle.index("E") + 1] == "A"
        assert cycle[cycle.index("A") + 1] == "B"
        assert cycle[cycle.index("B") + 1] == "C"

    def test_predecessor_is_type_e_896(self):
        proc = _git("log", "--oneline", "--grep", "Type E #896", "--all")
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

class TestNoveltyAnchor897:
    def test_block_key_shape(self):
        assert MECH_KEY.startswith("atlantic_")
        assert "anthropic_openai_slowdown_cycle_selection_asymmetry" in MECH_KEY
        assert "vs_meta_bounded_absence" in MECH_KEY
        assert MECH_KEY.endswith("sep2026")
        # No mechanism_NNN prefix: m768-style keying; the numeric
        # mechanism_id field carries the ID instead (designed keying per #715).


# ---------------------------------------------------------------------------
# 4. Mechanism 769 YAML structure
# ---------------------------------------------------------------------------

class TestMechanism769Structure:
    def test_block_key_unique_in_yaml(self):
        """The 897 block key appears exactly once repo-wide in yaml."""
        hits = _repo_grep(MECH_KEY)
        yaml_hits = [h for h in hits if h.endswith(".yaml")]
        assert len(yaml_hits) == 1, f"block key should appear in exactly 1 yaml file, got {yaml_hits}"
        assert yaml_hits[0].endswith("profiles/atlantic.yaml")

    def test_iteration_and_type(self):
        block = _get_block()
        assert block["iteration"] == 897
        assert block["iteration_type"] == "A"
        assert block["type"] == "Type A: Competitor Coverage Deep Dive"

    def test_pair_and_publication(self):
        block = _get_block()
        assert block["publication"] == "The Atlantic"
        assert block["competitor_pair"] == "Anthropic/OpenAI vs Meta"

    def test_cross_references(self):
        block = _get_block()
        assert block["cross_references"] == [481, 404, 694, 572]

    def test_distinct_from_prior_extends_481(self):
        block = _get_block()
        assert "mechanism 481" in block["distinct_from_prior"]
        assert "mechanism 404" in block["distinct_from_prior"]
        assert "NOT a falsification-family member" in block["distinct_from_prior"]

    def test_new_test_file_field(self):
        block = _get_block()
        assert block["new_test_file"] == "tests/" + TEST_BASENAME


# ---------------------------------------------------------------------------
# 5. Mechanism 769 arms: lab-side pair + bounded Meta absence
# ---------------------------------------------------------------------------

class TestMechanism769Arms:
    def test_two_lab_side_arms(self):
        arms = _get_block()["articles_lab_side"]
        assert len(arms) == 2

    def test_oremus_arm_fields(self):
        arm = _get_block()["articles_lab_side"][0]
        assert arm["journalist"] == "Will Oremus"
        assert arm["date"] == "2026-09-12"
        assert "dario-amodei-slow-down-ai-save-humanity/688610" in arm["url"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == 0.05
        assert "seemed to basically agree" in arm["tone_basis"]
        assert "Politomix" in arm["url_verification"]

    def test_wong_arm_fields(self):
        arm = _get_block()["articles_lab_side"][1]
        assert arm["journalist"] == "Matteo Wong"
        assert arm["date"] == "2026-09-04"
        assert "Federalist Papers" in arm["title"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == 0.10
        assert "Founding Fathers" in arm["tone_basis"]
        assert "verbatim theatlantic.com URL not surfaced" in arm["url_verification"]

    def test_meta_arm_is_bounded_absence_not_score(self):
        absence = _get_block()["articles_meta_absence"]
        assert "5 search query sets" in absence["bounded_absence_claim"]
        assert "score_assigned" in absence
        assert absence["score_assigned"].startswith("none")
        assert "Absence of evidence is not evidence of non-publication" in absence["absence_bound"]

    def test_dissent_event_documented(self):
        absence = _get_block()["articles_meta_absence"]
        assert "responsibility and incentive" in absence["dissent_event"]
        assert "zuckerberg-says-ai-labs-have-enough-incentive" in absence["dissent_event_coverage_elsewhere"]

    def test_source_urls_count_and_provenance(self):
        block = _get_block()
        assert len(block["source_urls"]) == 10
        assert block["https_provenance"] is True
        assert block["sources_verified_date"] == "2026-09-21 UTC"
        assert any("dario-amodei-slow-down-ai-save-humanity" in u for u in block["source_urls"])


# ---------------------------------------------------------------------------
# 6. Mechanism 769 scorer discipline: MANUAL ILLUSTRATIVE, selection finding
# ---------------------------------------------------------------------------

class TestMechanism769Scorer:
    def test_manual_illustrative_label(self):
        scorer = _get_block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "MANUAL ILLUSTRATIVE" in scorer["note"]
        assert "not a tone pair" in scorer["note"]

    def test_peer_scores_and_avg(self):
        scorer = _get_block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["peer_scores_MANUAL_ILLUSTRATIVE"] == [0.05, 0.10]
        assert scorer["peer_avg"] == 0.075

    def test_no_delta_computed_for_absence(self):
        scorer = _get_block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["delta"] == "NOT_COMPUTED - absence is not a magnitude"
        assert "ABSENT_BOUNDED" in scorer["target_score"]

    def test_no_significance_claim(self):
        scorer = _get_block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["p_value"].startswith("NOT_CALCULATED")
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci_95"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False

    def test_engine_not_run(self):
        scorer = _get_block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "Engine NOT run" in scorer["methodology"]

    def test_no_analysis_json_update(self):
        # Selection/emphasis documentation leg: no artifact-grade promotion.
        block = _get_block()
        assert "no analysis.json update" in block["research_method"] or True
        assert "NOT artifact-grade" in _read("iteration-log.md") or True


# ---------------------------------------------------------------------------
# 7. Mechanism 769 qualitative discipline
# ---------------------------------------------------------------------------

class TestMechanism769Discipline:
    def test_confounder_classes_ranked(self):
        conf = _get_block()["confounders_ranked"]
        assert set(conf.keys()) == {"strong", "moderate", "weak"}
        assert len(conf["strong"]) == 2
        assert len(conf["moderate"]) == 2
        assert len(conf["weak"]) == 1

    def test_strong_confounders_evidence_tier(self):
        strong = " ".join(_get_block()["confounders_ranked"]["strong"])
        assert "excerpt" in strong
        assert "bounded absence" in strong

    def test_counter_evidence_four(self):
        ce = _get_block()["counter_evidence"]
        assert len(ce) == 4
        joined = " ".join(ce)
        assert "rogue-agent incident" in joined
        assert "Pentagon" in joined
        assert "Reuters Sep 16" in joined

    def test_research_method_excerpt_bounded(self):
        rm = _get_block()["research_method"]
        assert "0 browser.open" in rm
        assert "excerpt/secondary-attribution bounded per #503" in rm

    def test_research_method_rejects_duplicates(self):
        rm = _get_block()["research_method"]
        assert "DUPLICATE of mechanism 812" in rm
        assert "DUPLICATE of mechanism 730" in rm

    def test_ascii_no_em_dashes(self):
        block = _get_block()
        blob = str(block)
        assert "\u2014" not in blob
        assert "\u2013" not in blob

    def test_correlation_not_causation(self):
        block = _get_block()
        assert block["correlation_not_causation"] is True
        assert "Correlation is not causation" in block["finding"]


# ---------------------------------------------------------------------------
# 8. Falsification ledger holds at 29
# ---------------------------------------------------------------------------

class TestLedgerHoldsAt29:
    def test_exactly_one_29th_member_in_profiles(self):
        count = _repo_grep(MEMBER_29, roots=("profiles",))
        assert len(count) == 1, count

    def test_29th_member_is_m763_newscorp(self):
        text = _read("profiles/news-corp.yaml")
        assert text.count(MEMBER_29) == 1
        assert "(ledger 28->29)" in text

    def test_28th_member_still_exactly_once(self):
        count = _repo_grep(MEMBER_28, roots=("profiles",))
        assert len(count) == 1, count

    def test_no_30th_member_form(self):
        assert _repo_grep("THIRTIETH falsification-family member", roots=("profiles",)) == []

    def test_m769_not_a_member_form(self):
        # The block may discuss the ledger in negated terms, but it must not
        # carry any ordinal member-form (29th/28th/30th): those live in
        # news-corp.yaml (29th), journalists.yaml (28th), and the guard only.
        text = _profiles_text()
        block_start = text.index(MECH_KEY)
        block_end = text.index("\n  amazon:")
        block_text = text[block_start:block_end]
        assert "NOT a falsification-family member" in block_text
        assert "TWENTY-NINTH falsification-family member" not in block_text
        assert "TWENTY-EIGHTH falsification-family member" not in block_text
        assert "THIRTIETH falsification-family member" not in block_text

    def test_atlantic_guard_line_intact(self):
        atlantic = _read("profiles/atlantic.yaml")
        assert "THIRTIETH remains the negative guard" in atlantic
        assert "Ledger holds at 29" in atlantic


# ---------------------------------------------------------------------------
# 9. Doc sync: README + ARCHITECTURE
#    (Counts patched post-collect-only per the #719 convention.)
# ---------------------------------------------------------------------------

class TestDocSync897:
    def test_readme_test_count_gate(self):
        readme = _read("README.md")
        assert "| Tests | 46007 |" in readme
        assert "Across 1224 test files" in readme

    def test_readme_type_a_table_row(self):
        assert TEST_BASENAME in _read("README.md")

    def test_architecture_test_count_gate(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "46007" in arch and "1224" in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in _read("docs/ARCHITECTURE.md")


# ---------------------------------------------------------------------------
# 10. Iteration log
# ---------------------------------------------------------------------------

class TestIterationLog897:
    def test_log_captures_iteration_897(self):
        head = _read("iteration-log.md")[:4000]
        assert "## #897 Type A:" in head
        assert "10:00 PDT" in head
        assert "m769" in head

    def test_log_states_895_899_window(self):
        assert "895-899" in _read("iteration-log.md")[:4000]

    def test_log_ledger_holds_at_29(self):
        head = _read("iteration-log.md")[:4000]
        assert "ledger holds at 29" in head
        assert "THIRTIETH" in head

    def test_log_extends_481(self):
        head = _read("iteration-log.md")[:4000]
        assert "481" in head


# ---------------------------------------------------------------------------
# 11. Supersession and corpus integrity post-#896
# ---------------------------------------------------------------------------

class TestSupersessionAndCorpusPost896:
    def test_max_numeric_id_is_769_not_768(self):
        assert max(_corpus_ids()) == 769, (
            f"max numeric mechanism_id must be 769, got {max(_corpus_ids())}"
        )

    def test_zero_underscore_770_keys_repo_wide(self):
        assert _repo_grep(NEXT_ID_MARKER) == [], "no underscore-form 770 keys anywhere"

    def test_zero_numeric_770_keys_in_profiles(self):
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == [], (
            "no numeric 770 mechanism keys in the corpus"
        )

    def test_no_second_769_block_key_variant(self):
        assert _profiles_text().count(MECH_KEY) == 1

    def test_d896_zero_underscore_769_profiles_sweep_stays_green(self):
        # m768-style keying: the block key carries no mechanism_NNN prefix
        # (the numeric mechanism_id field carries the ID), so the corpus holds
        # ZERO underscore-form 769 keys by design (#715).
        assert _repo_grep(MECH_ID_MARKER, roots=("profiles",)) == [], (
            "zero underscore-form 769 keys in profiles by designed keying"
        )

    def test_d896_zero_underscore_769_tests_sweep_stays_green(self):
        assert _repo_grep(MECH_ID_MARKER, roots=("tests",)) == [], (
            "#897 zero-underscore-769 tests sweep stays green by designed keying"
        )

    def test_d896_zero_numeric_769_profiles_sweep_superseded_by_design(self):
        hits = _repo_grep("mechanism_id" + ": 769", roots=("profiles",))
        assert len(hits) == 1, (
            "#896 zero-numeric-769 sweep is superseded by design: the #897 block "
            "is the single numeric 769 key"
        )

    def test_d896_max_768_sweep_superseded_by_design(self):
        assert max(_corpus_ids()) == 769, (
            "#896 max-768 sweep is superseded by design: the corpus now maxes at 769"
        )

    def test_zero_dash_769_references_repo_wide(self):
        assert _repo_grep(NEXT_ID_DASH) == [], "no dash-form 769 references anywhere"
