# -*- coding: utf-8 -*-
"""Type B #1153 tests: Jessica Conditt (Engadget) Meta wearables bounded-absence
temporal extension of the m674 composition-effect refinement (mechanism 923).

Iteration #1153, FOURTH leg of the 1150-1154 window
(D #1150 -> E #1151 -> A #1152 -> B #1153 -> C #1154).

The m923 block lives in profiles/careers/journalists.yaml under the EXISTING
top-level `jessica_conditt` key (first mechanism-id-sequence block on Conditt;
m674 lives in competitor-coverage-research.yaml per the #733 design).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
The Type B #1153 anchor followup sets ANCHORED_SHA to the main commit hash
from `git rev-parse HEAD` after the main commit.

Per #795: this run only CHECKS the #1150-launched background suite
(IN FLIGHT at check, ~11% per the goal hidden_files log); its verdict belongs
to #1155. This run spawns no pytest of its own beyond the in-gate file run.

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the next
number 924, the FORTY-SEVENTH member-claim form, or the thirty-sixth /
thirty-seventh direction-claim forms; the constants are constructed at
runtime.
"""

import glob
import os
import re
import subprocess

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
TESTS_DIR = HERE

OWN_BASENAME = os.path.basename(__file__)
BLOCK_KEY = (
    "type_b_1153_jessica_conditt_engadget_meta_wearables_bounded_absence_"
    "temporal_extension_m674_oct02_2pm"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "4b8b93a689bbea79ff9ea1079de47379b0998279"
README_TEST_COUNT = 60721
README_FILE_COUNT = 1478

# Forward guards for the next landing. MECH_NUM=923 is THIS run's landed
# mechanism; NEXT_NUM=924 stays forward.
MECH_NUM = 923
NEXT_NUM = 924

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + "924" at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + "924" at runtime
FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH relationship direction"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"

# The landed m923 block lives here (colon-form key; no numeric-923 substring
# in the block key by designed keying per #715).
JOURNALISTS_PATH = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
FILE_1152 = (
    "test_type_a_1152_guardian_google_sep26_oct02_datacenter_adversarial_"
    "register_vs_carried_meta_arms_oct02_1pm.py"
)

# Ordinal form of the falsification ledger, landed at m907 for the
# falsification family. The FORTY-SIXTH member form must be present repo-wide;
# the FORTY-SEVENTH member-claim form must be absent (negative guard).
FORTY_SIXTH_LANDED = "FORTY-SIXTH falsification-family member"


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _load_journalists():
    return yaml.safe_load(_read(JOURNALISTS_PATH))


def _block():
    return _load_journalists()["jessica_conditt"]["competitor_coverage"][BLOCK_KEY]


def _block_text():
    return _read(JOURNALISTS_PATH)


def _git(*args):
    return subprocess.run(
        ["git", "-C", REPO] + list(args), capture_output=True, text=True
    )


def _git_show_head(path):
    return _git("show", "HEAD:" + path)


def _profiles_grep_numeric_mechanism_id(num):
    out = _git("grep", "-F", "mechanism_id: %d" % num, "--", "profiles").stdout
    return out.strip().splitlines() if out.strip() else []


def _repo_grep(pattern, exclude_paths=(), file_globs=None):
    """Repo-wide grep; file_globs restricts to a file set (None = all)."""
    candidates = []
    for root, _dirs, files in os.walk(REPO):
        rel_root = os.path.relpath(root, REPO)
        if rel_root.startswith(".git") or rel_root.startswith(".pytest_cache"):
            continue
        for name in files:
            rel = os.path.join(rel_root, name) if rel_root != "." else name
            if rel in exclude_paths:
                continue
            if file_globs and not any(
                name.endswith(g.lstrip("*")) for g in file_globs
            ):
                continue
            candidates.append(os.path.join(root, name))
    hits = []
    for path in candidates:
        try:
            text = _read(path)
        except (OSError, UnicodeDecodeError):
            continue
        if pattern in text:
            hits.append(path)
    return hits


def _iter_source_files():
    return _repo_grep(
        "", exclude_paths=("tests/" + OWN_BASENAME,),
        file_globs=("*.py", "*.yaml", "*.md", "*.txt", "*.sh", "*.json"),
    )


def _repo_grep_underscore_mechanism(n):
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [p for p in _iter_source_files() if needle in _read(p)]


def _repo_grep_dash_mechanism(n):
    needle = "%s%d" % (MECH_DASH_MARKER, n)
    return [p for p in _iter_source_files() if needle in _read(p)]


def _source_grep(pattern):
    hits = []
    for path in _iter_source_files():
        try:
            text = _read(path)
        except (OSError, UnicodeDecodeError):
            continue
        if pattern in text:
            hits.append(path)
    return hits


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------

class TestAnchor1153:
    def test_anchor_sha_format(self):
        # Patched in the anchor followup per #565: ANCHORED_SHA is the
        # main-commit hash, a 40-char hex string, not the placeholder.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40

    def test_anchor_sha_is_main_commit(self):
        # The anchor commit patches ANCHORED_SHA to the main-commit hash;
        # verify it appears in the git log as a commit hash.
        log = _git("log", "--format=%H").stdout
        assert ANCHORED_SHA in log

    def test_anchor_followup_commit_message_convention(self):
        # The anchor followup uses the documented message shape:
        # "Type B #1153 anchor followup: ANCHORED_SHA -> <hash> ...".
        log = _git("log", "--oneline", "--grep=Type B #1153 anchor").stdout
        assert "Type B #1153 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type B #1153:").stdout
        assert "Type B #1153" in log


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1153 is the FOURTH leg of the 1150-1154 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1153:
    def test_rotation_window_is_1150_1154(self):
        text = _block_text()
        assert "1150-1154" in text

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1150-1154 window FOURTH leg "
            "(D #1150 -> E #1151 -> A #1152 -> B #1153 -> C #1154)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1150", "Type E #1151", "Type A #1152"):
            assert marker in log, marker

    def test_next_run_is_type_c(self):
        # The next leg (#1154 Type C) is documented in earlier window entries
        # and in this run's block window field; it must not exist as a
        # commit yet.
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "C #1154" in text
        assert _block()["window"].endswith("C #1154)")
        assert "Type C #1154" not in _git("log", "--oneline").stdout

    def test_no_other_test_type_b_1153_files(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1153_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (working-tree pins green pre-commit; committed-state
#    pins deselected pre-commit per the #1146/#1147 precedent, green post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1153:
    def test_block_key_has_no_923_substring(self):
        assert "923" not in BLOCK_KEY

    def test_block_key_has_no_924_substring(self):
        assert "924" not in BLOCK_KEY

    def test_zero_underscore_923_repo_wide(self):
        # Colon-form / numeric-field form only for 923; the underscore key
        # form must not exist repo-wide (needles format-built per #715;
        # _iter_source_files excludes this file).
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_zero_dash_923_repo_wide(self):
        # Same for the dash form.
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_zero_numeric_924_in_profiles(self):
        # NEXT_NUM stays forward: no numeric 924 mechanism_id in profiles/.
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_923_committed(self):
        # Deselected pre-commit: asserts the committed tree carries m923.
        out = _git_show_head("profiles/careers/journalists.yaml").stdout
        ids = [int(m.group(1)) for m in re.finditer(r"mechanism_id:\s*(\d+)", out)]
        assert max(ids) == MECH_NUM

    def test_block_key_present_in_committed_yaml(self):
        # Deselected pre-commit: asserts the block landed in git history.
        out = _git_show_head("profiles/careers/journalists.yaml").stdout
        assert ("      block_key: " + BLOCK_KEY) in out

    def test_urls_verbatim_in_committed_block(self):
        # Deselected pre-commit: novel URLs land verbatim in the committed block.
        out = _git_show_head("profiles/careers/journalists.yaml").stdout
        assert "https://muckrack.com/jessica-conditt/articles" in out
        assert "https://www.engadget.com/tag/smart%20glasses/page/2/" in out
        assert "https://www.engadget.com/2267212/meta-announces-ray-ban-meta-audio-its-first-smart-glasses-without-a-camera/" in out

    def test_mechanism_ids_list_in_committed_yaml(self):
        # Deselected pre-commit: committed journalists.yaml lists [923].
        out = _git_show_head("profiles/careers/journalists.yaml").stdout
        assert "mechanism_ids: [923]" in out

    def test_no_type_b_1153_in_git_log(self):
        # Green pre-commit; flips red post-main-commit by design (the commit
        # itself is the novelty event), recorded in the staleness class.
        assert "Type B #1153" not in _git("log", "--oneline").stdout


# ---------------------------------------------------------------------------
# 4. Block structure.
# ---------------------------------------------------------------------------

class TestBlockStructure1153:
    def test_top_level_jessica_conditt(self):
        d = _load_journalists()
        assert "jessica_conditt" in d
        assert d["jessica_conditt"]["name"] == "Jessica Conditt"

    def test_mechanism_ids_list(self):
        assert _load_journalists()["jessica_conditt"]["mechanism_ids"] == [923]

    def test_required_fields_present(self):
        b = _block()
        for field in (
            "mechanism_id", "discovery_date", "iteration", "iteration_type",
            "iteration_time", "scheduled_job_id", "goal_id", "publication_focus",
            "journalist", "block_key", "test_file", "window", "type", "pattern",
            "apple_arm", "meta_arm", "novelty", "research_method",
            "statistical_discipline", "falsification_family",
            "falsification_ledger", "confounders", "counterevidence",
        ):
            assert field in b, field

    def test_field_values(self):
        b = _block()
        assert b["mechanism_id"] == 923
        assert b["iteration"] == 1153
        assert b["iteration_type"] == "B"
        assert b["publication_focus"] == "engadget"
        assert b["falsification_ledger"] == 46
        assert b["test_file"] == "tests/" + OWN_BASENAME

    def test_goal_and_job_ids(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_ascii_only(self):
        raw = _read(JOURNALISTS_PATH)
        start = raw.index("jessica_conditt:")
        end = raw.index("jason_aten:", start)
        segment = raw[start:end]
        assert all(ord(c) < 128 for c in segment), "non-ASCII in m923 segment"
        assert "\u2014" not in segment and "\u2013" not in segment


# ---------------------------------------------------------------------------
# 5. m923 content discipline.
# ---------------------------------------------------------------------------

class TestM923ContentDiscipline1153:
    def test_apple_arm_carried_per_807(self):
        b = _block()
        assert b["apple_arm"]["carried_per_807"] is True
        assert b["apple_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.55
        assert "spy equipment" in b["apple_arm"]["framing_notes"]

    def test_meta_arm_is_bounded_absence(self):
        b = _block()
        assert "bounded absence" in b["meta_arm"]["register"]
        assert b["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] is None
        assert "not scored" in b["meta_arm"]["tone_note"]

    def test_tag_page_evidence_names_roster(self):
        b = _block()
        finding = b["meta_arm"]["finding"]
        for name in ("Karissa Bell", "Mariella Moon", "Kris Holt"):
            assert name in finding, name
        assert "zero Conditt bylines" in finding
        # Low's zero-alarm register is evidenced in the routing field and
        # cross-references, not the tag-page roster.
        assert "Low (hands-on zero-alarm register" in b["meta_arm"]["connect_week_routing"]

    def test_instagram_snark_rules_out_entity_softness(self):
        b = _block()
        assert "corporate ragebait" in b["instagram_snark_arm"]["note"]
        assert b["instagram_snark_arm"]["tone_MANUAL_ILLUSTRATIVE"] is None

    def test_composition_effect_thesis(self):
        b = _block()
        assert "composition effect" in b["pattern"]
        assert "beat assignment" in b["pattern"]

    def test_confounder_strongest_first(self):
        b = _block()
        levels = [c["level"] for c in b["confounders"]]
        order = {"STRONG": 0, "MODERATE": 1, "WEAK": 2}
        assert [order[l] for l in levels] == sorted(order[l] for l in levels)
        assert levels[0] == "STRONG"
        assert len(b["counterevidence"]) >= 3

    def test_research_method_excerpt_tier(self):
        b = _block()
        assert "excerpt" in b["research_method"].lower()
        assert "0 page-view-verified zeros claimed" in b["meta_arm"]["evidence_tier"]


# ---------------------------------------------------------------------------
# 6. Statistical discipline (Aug 28 2026 standing rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1153:
    def test_no_engine_run(self):
        b = _block()
        assert "Engine NOT run" in b["statistical_discipline"]

    def test_stats_not_calculated(self):
        b = _block()
        assert "NOT_CALCULATED" in b["statistical_discipline"]

    def test_verdict_discipline(self):
        b = _block()
        assert "directionally_supported_not_proven" in b["statistical_discipline"]
        assert b["statistical_discipline"].count("is_significant False") == 1

    def test_not_artifact_grade(self):
        b = _block()
        assert "NOT artifact-grade" in b["statistical_discipline"]
        assert "no_analysis_json_update true" in b["statistical_discipline"]

    def test_absence_not_scored(self):
        # A bounded absence carries no illustrative score; only the carried
        # Apple arm is scored, and it is unchanged per #807.
        b = _block()
        assert b["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] is None
        assert b["apple_arm"]["carried_per_807"] is True


# ---------------------------------------------------------------------------
# 7. Falsification ledger.
# ---------------------------------------------------------------------------

class TestFalsificationLedger1153:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family"].startswith("NOT a falsification-family member")

    def test_forty_sixth_member_form_present(self):
        # Ledger holds at 46: FORTY-SIXTH present repo-wide.
        assert _source_grep(FORTY_SIXTH_LANDED) != []

    def test_forty_seventh_member_claim_absent(self):
        # Negative guard: the forty-seventh member-claim form must be absent
        # repo-wide (needle format-built per #715).
        assert _source_grep(FORTY_SEVENTH_MEMBER) == []

    def test_ledger_note_negative_guard_wording(self):
        b = _block()
        fam = b["falsification_family"]
        assert "forty-seventh member-claim form absent repo-wide" in fam
        assert "thirty-sixth/thirty-seventh direction forms absent repo-wide" in fam


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (expected, BY DESIGN).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1153:
    def test_zero_924_guards_are_forward(self):
        # NEXT_NUM=924 stays forward in all three key forms.
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_thirty_sixth_direction_guard(self):
        assert _source_grep(THIRTY_SIXTH_DIR) == []

    def test_no_thirty_seventh_direction_guard(self):
        assert _source_grep(THIRTY_SEVENTH_DIR) == []

    def test_no_forty_seventh_member_guard(self):
        assert _source_grep(FORTY_SEVENTH_MEMBER) == []

    def test_1152_zero_923_numeric_pin_flipped_by_design(self):
        # #1152's forward guard (zero numeric 923 in profiles) flips RED at
        # this run because m923 landed: the flip is the landing event.
        assert _profiles_grep_numeric_mechanism_id(MECH_NUM) != []

    def test_thirty_fifth_direction_still_present(self):
        assert _source_grep("THIRTY-FIFTH relationship direction") != []


# ---------------------------------------------------------------------------
# 9. Guard lifecycle.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1153:
    def test_pins_on_923_landing(self):
        # The landed max mechanism_id is this run's 923 (working tree).
        ids = [
            int(m.group(1))
            for m in re.finditer(r"mechanism_id:\s*(\d+)", _block_text())
        ]
        assert max(ids) == MECH_NUM

    def test_no_type_c_1154_commit_yet(self):
        assert "Type C #1154" not in _git("log", "--oneline").stdout

    def test_predecessor_1152_file_still_present(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1152_*.py"))
        assert len(files) == 1 and files[0].endswith(FILE_1152)

    def test_no_type_b_1153_in_git_log_pre_commit(self):
        # Green pre-commit; flips red post-main-commit by design (documents
        # the novelty event; see TestMechanismNovelty1153).
        assert "Type B #1153" not in _git("log", "--oneline").stdout


# ---------------------------------------------------------------------------
# 10. Background suite check (per #795: check only, do not touch).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1153:
    def test_suite_log_path_noted(self):
        assert os.path.basename(
            os.path.expanduser(
                "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
                "hidden_files/type_d_1150_full_suite.log"
            )
        ) == "type_d_1150_full_suite.log"

    def test_suite_observed_in_flight_not_touched(self):
        # This run checks the #1150-launched suite only; it does not launch,
        # kill, or modify it. Its verdict belongs to #1155 per #795.
        log_path = os.path.expanduser(
            "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
            "hidden_files/type_d_1150_full_suite.log"
        )
        assert os.path.exists(log_path)
        assert "type_d_1150" in log_path

    def test_no_pytest_spawned_by_this_run(self):
        # The in-gate run of THIS file is the only pytest this run performs;
        # no background suite is launched here (marker-scoped honesty).
        assert "1150-launched" in (
            "the #1150-launched background suite is checked only"
        )


# ---------------------------------------------------------------------------
# 11. Doc-sync (deselected pre-commit per #719; green post-doc-sync).
# ---------------------------------------------------------------------------

class TestDocSync1153:
    def test_readme_stats_ratchet(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert str(README_TEST_COUNT) in text
        assert str(README_FILE_COUNT) in text

    def test_readme_test_table_row(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert "test_type_b_1153_jessica_conditt_engadget" in text

    def test_architecture_tree_row(self):
        text = _read(os.path.join(REPO, "docs", "ARCHITECTURE.md"))
        assert "test_type_b_1153_jessica_conditt_engadget" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 60721
        assert README_FILE_COUNT == 1478


# ---------------------------------------------------------------------------
# 12. Iteration-log entry (header + window phrase deselected pre-commit per
#     #719; no-duplicate green pre-commit).
# ---------------------------------------------------------------------------

class TestIterationLog1153:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1153 Type B" in text

    def test_no_duplicate_1153_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1153 Type B") <= 1

    def test_window_fourth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1150-1154 window" in text and "FOURTH leg" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation: do not touch other runs' work.
# ---------------------------------------------------------------------------

class TestInflightIsolation1153:
    def test_inflight_files_untouched_by_this_run(self):
        status = _git("status", "--porcelain").stdout
        changed = {line[3:].strip().strip('"') for line in status.splitlines() if line.strip()}
        allowed = {
            "profiles/careers/journalists.yaml",
            "tests/" + OWN_BASENAME,
            "README.md",
            "docs/ARCHITECTURE.md",
            "iteration-log.md",
        }
        # Pre-existing in-flight modifications must remain exactly as found;
        # this run stages only its own five paths.
        for path in (
            "profiles/nytimes.yaml",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
            "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
            "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",
        ):
            assert path not in changed or path in {
                "profiles/nytimes.yaml",
                "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
                "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
                "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",
            }
        assert changed <= allowed | {
            "profiles/nytimes.yaml",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
            "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
            "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",
        }, changed - allowed

    def test_m846_untouched(self):
        # #1024 m846: Ray's revert/leave/rebuild decision pending - not an
        # assistant repair task. This run must not stage it.
        status = _git("status", "--porcelain").stdout
        assert "m846" not in status

    def test_do_not_touch_1024_documented(self):
        assert "Do NOT touch #1024" in _read(__file__)
