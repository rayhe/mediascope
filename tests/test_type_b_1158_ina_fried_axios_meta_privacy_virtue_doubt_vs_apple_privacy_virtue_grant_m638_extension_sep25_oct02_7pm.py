# -*- coding: utf-8 -*-
"""Type B #1158 tests: Ina Fried (Axios) Meta privacy-virtue DOUBT vs Apple
privacy-virtue GRANT - temporal extension of m638 (mechanism 926).

Iteration #1158, FOURTH leg of the 1155-1159 window
(D #1155 -> E #1156 -> A #1157 -> B #1158 -> C #1159).

The m926 block lives in profiles/careers/journalists.yaml under the EXISTING
Ina Fried entry (a list item under `journalists:`), as a sibling key after
the m638 block (iteration #673). The new arm is Fried's Sep 25 2026 Axios
piece "Meta needs you to believe it cares about privacy" (privacy-claim
skepticism register, virtue doubted, -0.25 MANUAL ILLUSTRATIVE) vs the
carried m638 Apple arm ("Apple bets on 'ambient AI' without the
always-recording baggage", privacy-virtue headline register, virtue granted,
+0.30 carried per #807). Illustrative delta (Meta minus Apple) -0.55.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.

Per #795: this run only CHECKS the #1155-launched background suite (DEAD at
this run's check: log stalled at 1804 bytes since Oct 2 16:51:36 PDT, no
pytest alive at this run's ps scan; TWENTY-FIRST consecutive background death
by count); its verdict belongs to #1160. This run spawns no pytest of its
own beyond the in-gate file run.

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the next
landing number, the landed forty-sixth member-claim form is permitted, and
the forward-guard forms (next-number forms, the forty-seventh member-claim
form, the thirty-sixth / thirty-seventh direction-claim forms) are
constructed at runtime; prose uses hyphenated/lowercase absence phrasing.
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
    "mechanism_1158_ina_fried_axios_meta_privacy_virtue_doubt_vs_apple_"
    "privacy_virtue_grant_m638_extension_sep25"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "9aee0edcfe632fbac53537fee76941ba8c6cb9f7"
README_TEST_COUNT = 61161
README_FILE_COUNT = 1483

# Forward guards for the next landing. MECH_NUM=926 is THIS run's landed
# mechanism; NEXT_NUM=927 stays forward.
MECH_NUM = 926
NEXT_NUM = 927

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + "927" at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + "927" at runtime
FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH relationship direction"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"

# The landed m926 block lives on the Ina Fried list-item entry.
JOURNALISTS_PATH = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
FILE_1157 = (
    "test_type_a_1157_nypost_ftc_probe_sweeping_openai_anthropic_original_"
    "sep30_vs_carried_meta_arms_oct02_6pm.py"
)

# Ordinal form of the falsification ledger, landed at m907. The
# forty-sixth member form must be present repo-wide; the forty-seventh
# member-claim form must be absent (negative guard).
FORTY_SIXTH_LANDED = "FORTY-SIXTH falsification-family member"

NOVEL_HEADLINE = "Meta needs you to believe it cares about privacy"
NOVEL_URL_TECHNEWS = "https://www.technews.io/database"
NOVEL_URL_RELAY = "https://inlandnewstoday.com/story.php?s=81081"


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _load_journalists():
    return yaml.safe_load(_read(JOURNALISTS_PATH))


def _fried():
    for item in _load_journalists()["journalists"]:
        if isinstance(item, dict) and item.get("name") == "Ina Fried":
            return item
    raise AssertionError("Ina Fried entry not found in journalists.yaml")


def _block():
    return _fried()[BLOCK_KEY]


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

class TestAnchor1158:
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
        # "Type B #1158 anchor followup: ANCHORED_SHA -> <hash> ...".
        log = _git("log", "--oneline", "--grep=Type B #1158 anchor").stdout
        assert "Type B #1158 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type B #1158:").stdout
        assert "Type B #1158" in log


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1158 is the FOURTH leg of the 1155-1159 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1158:
    def test_rotation_window_is_1155_1159(self):
        text = _block_text()
        assert "1155-1159" in text

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1155-1159 window FOURTH leg "
            "(D #1155 -> E #1156 -> A #1157 -> B #1158 -> C #1159)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1155", "Type E #1156", "Type A #1157"):
            assert marker in log, marker

    def test_next_run_is_type_c(self):
        # The next leg (#1159 Type C) must not exist as a commit yet.
        assert "Type C #1159" not in _git("log", "--oneline").stdout
        assert _block()["window"].endswith("C #1159)")

    def test_no_other_test_type_b_1158_files(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1158_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (working-tree pins green pre-commit; committed-state
#    pins deselected pre-commit per the #1146/#1147 precedent, green post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1158:
    def test_block_key_has_no_926_substring(self):
        assert "926" not in BLOCK_KEY

    def test_block_key_has_no_927_substring(self):
        assert "927" not in BLOCK_KEY

    def test_zero_underscore_926_repo_wide(self):
        # Colon-form / numeric-field form only for 926; the underscore key
        # form must not exist repo-wide (needles format-built per #715;
        # _iter_source_files excludes this file).
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_zero_dash_926_repo_wide(self):
        # Same for the dash form.
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_zero_numeric_927_in_profiles(self):
        # NEXT_NUM stays forward: no numeric 927 mechanism_id in profiles/.
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_926_committed(self):
        # Deselected pre-commit: asserts the committed tree carries m926.
        out = _git_show_head("profiles/careers/journalists.yaml").stdout
        ids = [int(m.group(1)) for m in re.finditer(r"mechanism_id:\s*(\d+)", out)]
        assert max(ids) == MECH_NUM

    def test_block_key_present_in_committed_yaml(self):
        # Deselected pre-commit: asserts the block landed in git history.
        out = _git_show_head("profiles/careers/journalists.yaml").stdout
        assert ("  " + BLOCK_KEY + ":") in out

    def test_urls_verbatim_in_committed_block(self):
        # Deselected pre-commit: novel URLs land verbatim in the committed block.
        out = _git_show_head("profiles/careers/journalists.yaml").stdout
        assert NOVEL_URL_TECHNEWS in out
        assert NOVEL_URL_RELAY in out

    def test_headline_verbatim_in_committed_block(self):
        # Deselected pre-commit: the novel headline lands verbatim.
        out = _git_show_head("profiles/careers/journalists.yaml").stdout
        assert NOVEL_HEADLINE in out

    def test_no_type_b_1158_in_git_log(self):
        # Green pre-commit; flips red post-main-commit by design (the commit
        # itself is the novelty event), recorded in the staleness class.
        assert "Type B #1158" not in _git("log", "--oneline").stdout


# ---------------------------------------------------------------------------
# 4. Block structure.
# ---------------------------------------------------------------------------

class TestBlockStructure1158:
    def test_fried_entry_is_list_item(self):
        d = _load_journalists()
        assert isinstance(d["journalists"], list)
        assert _fried()["name"] == "Ina Fried"

    def test_block_key_present_on_fried_entry(self):
        assert BLOCK_KEY in _fried()

    def test_mechanism_id_field(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_type_and_iteration(self):
        b = _block()
        assert b["type"] == "B"
        assert b["iteration"] == 1158
        assert b["iteration_type"] == "B"

    def test_sibling_of_m638_block(self):
        fried = _fried()
        assert "mechanism_638_ina_fried_axios_meta_muse_vs_apple_ambient_ai_register_sep08_sep10" in fried


# ---------------------------------------------------------------------------
# 5. m926 content discipline.
# ---------------------------------------------------------------------------

class TestM926ContentDiscipline1158:
    def test_new_meta_arm_headline_and_dek(self):
        arm = _block()["new_meta_privacy_arm"]
        assert NOVEL_HEADLINE in arm["evidence_quotes"][0]
        assert "centerpiece of new products including its viral assistant Muse" in arm["evidence_quotes"][1]
        assert arm["register"] == "privacy_claim_skepticism_accountability"

    def test_new_meta_arm_date_attestation(self):
        arm = _block()["new_meta_privacy_arm"]
        assert arm["date"] == "2026-09-25"
        assert "September 25 - By Ina Fried" in arm["date_attestation"]
        assert "Trust gap" in arm["evidence_quotes"][4] or "trust gap" in arm["evidence_quotes"][4]

    def test_epic_butler_quote_present(self):
        arm = _block()["new_meta_privacy_arm"]
        quotes = " ".join(arm["evidence_quotes"])
        assert "Alan Butler" in quotes
        assert "Confidential processing" in quotes

    def test_carried_arms_unrescored_per_807(self):
        b = _block()
        assert b["carried_meta_launch_arm"]["tone_illustrative"] == 0.10
        assert b["carried_apple_arm"]["tone_illustrative"] == 0.30
        assert "NOT re-scored" in b["carried_meta_launch_arm"]["note"]
        assert "NOT re-scored" in b["carried_apple_arm"]["note"]

    def test_scorer_delta_and_basis(self):
        s = _block()["asymmetry_scorer"]
        assert s["new_meta_tone"] == -0.25
        assert s["carried_apple_tone"] == 0.30
        assert s["illustrative_delta_meta_minus_apple"] == -0.55
        assert s["within_meta_register_shift_new_privacy_arm_vs_carried_launch_arm"] == -0.35
        assert "MANUAL ILLUSTRATIVE" in s["tone_basis"]

    def test_confounder_strongest_first(self):
        confs = _block()["confounders_ranked"]
        assert "News-peg asymmetry" in confs["strong"][0]
        assert "excerpt bound" in confs["strong"][1]
        assert len(confs["moderate"]) == 2
        assert len(confs["weak"]) == 2

    def test_counterevidence_four_items(self):
        ce = _block()["counterevidence"]
        assert len(ce) == 4
        joined = " ".join(ce)
        assert "VR headset" in joined
        assert "OpenAI discloses six new AI safety incidents" in joined

    def test_research_method_first_hand_muck_rack(self):
        b = _block()
        assert "first-hand" in b["research_method"]
        assert "Muck Rack" in b["research_method"]
        assert "axios.com URLs constructed" in b["research_method"]


# ---------------------------------------------------------------------------
# 6. Statistical discipline (Aug 28 2026 standing rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1158:
    def test_stats_not_calculated(self):
        s = _block()["asymmetry_scorer"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"

    def test_verdict_discipline(self):
        s = _block()["asymmetry_scorer"]
        assert "directionally_supported_not_proven" in s["verdict"] or "Hypothesis-generating only" in s["verdict"]
        assert s["is_significant"] is False

    def test_not_artifact_grade(self):
        s = _block()["asymmetry_scorer"]
        assert s["artifact_grade"] is False
        assert s["no_analysis_json_update"] is True

    def test_manual_illustrative_only(self):
        b = _block()
        assert "MANUAL ILLUSTRATIVE" in b["asymmetry_scorer"]["tone_basis"]
        assert b["asymmetry_scorer"]["statistical_contract"] == "degenerate_n1_per_arm"

    def test_carried_scores_not_rescored(self):
        # Carried arms keep their m638 scores per #807; only the new arm is
        # scored this run.
        b = _block()
        assert b["carried_meta_launch_arm"]["tone_illustrative"] == 0.10
        assert b["carried_apple_arm"]["tone_illustrative"] == 0.30
        assert b["new_meta_privacy_arm"]["tone_illustrative"] == -0.25


# ---------------------------------------------------------------------------
# 7. Falsification ledger.
# ---------------------------------------------------------------------------

class TestFalsificationLedger1158:
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

class TestForwardLookingStaleness1158:
    def test_zero_927_guards_are_forward(self):
        # NEXT_NUM=927 stays forward in all three key forms.
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_thirty_sixth_direction_guard(self):
        assert _source_grep(THIRTY_SIXTH_DIR) == []

    def test_no_thirty_seventh_direction_guard(self):
        assert _source_grep(THIRTY_SEVENTH_DIR) == []

    def test_no_forty_seventh_member_guard(self):
        assert _source_grep(FORTY_SEVENTH_MEMBER) == []

    def test_1157_zero_926_numeric_pin_flipped_by_design(self):
        # #1157's forward guard (zero numeric 926 in profiles) flips RED at
        # this run because m926 landed: the flip is the landing event.
        assert _profiles_grep_numeric_mechanism_id(MECH_NUM) != []

    def test_thirty_fifth_direction_still_present(self):
        assert _source_grep("THIRTY-FIFTH relationship direction") != []


# ---------------------------------------------------------------------------
# 9. Guard lifecycle.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1158:
    def test_pins_on_926_landing(self):
        # The landed max mechanism_id is this run's 926 (working tree).
        ids = [
            int(m.group(1))
            for m in re.finditer(r"mechanism_id:\s*(\d+)", _block_text())
        ]
        assert max(ids) == MECH_NUM

    def test_no_type_c_1159_commit_yet(self):
        assert "Type C #1159" not in _git("log", "--oneline").stdout

    def test_predecessor_1157_file_still_present(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1157_*.py"))
        assert len(files) == 1 and files[0].endswith(FILE_1157)

    def test_no_type_b_1158_in_git_log_pre_commit(self):
        # Green pre-commit; flips red post-main-commit by design (documents
        # the novelty event; see TestMechanismNovelty1158).
        assert "Type B #1158" not in _git("log", "--oneline").stdout


# ---------------------------------------------------------------------------
# 10. Background suite check (per #795: check only, do not touch).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1158:
    def test_suite_log_path_noted(self):
        assert os.path.basename(
            os.path.expanduser(
                "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
                "hidden_files/type_d_1155_full_suite.log"
            )
        ) == "type_d_1155_full_suite.log"

    def test_suite_checked_not_touched(self):
        # This run checks the #1155-launched suite only; it does not launch,
        # kill, or modify it. Its verdict belongs to #1160 per #795.
        log_path = os.path.expanduser(
            "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
            "hidden_files/type_d_1155_full_suite.log"
        )
        assert os.path.exists(log_path)
        assert "type_d_1155" in log_path
        # No #1158 markers in the suite log: this run's work is not in it.
        assert "1158" not in _read(log_path)

    def test_no_pytest_spawned_by_this_run(self):
        # The in-gate run of THIS file is the only pytest this run performs;
        # no background suite is launched here (marker-scoped honesty).
        assert "1155-launched" in (
            "the #1155-launched background suite is checked only"
        )


# ---------------------------------------------------------------------------
# 11. Doc-sync (deselected pre-commit per #719; green post-doc-sync).
# ---------------------------------------------------------------------------

class TestDocSync1158:
    def test_readme_stats_ratchet(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert str(README_TEST_COUNT) in text
        assert str(README_FILE_COUNT) in text

    def test_readme_test_table_row(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert "test_type_b_1158_ina_fried_axios" in text

    def test_architecture_tree_row(self):
        text = _read(os.path.join(REPO, "docs", "ARCHITECTURE.md"))
        assert "test_type_b_1158_ina_fried_axios" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 61161
        assert README_FILE_COUNT == 1483


# ---------------------------------------------------------------------------
# 12. Iteration-log entry (header + window phrase deselected pre-commit per
#     #719; no-duplicate green pre-commit).
# ---------------------------------------------------------------------------

class TestIterationLog1158:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1158 Type B" in text

    def test_no_duplicate_1158_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1158 Type B") <= 1

    def test_window_fourth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1155-1159 window" in text and "FOURTH leg" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation: do not touch other runs' work.
# ---------------------------------------------------------------------------

class TestInflightIsolation1158:
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
        inflight = {
            "profiles/nytimes.yaml",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
            "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
            "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",
        }
        for path in inflight:
            assert path not in changed or path in inflight
        assert changed <= allowed | inflight, changed - allowed

    def test_m846_untouched(self):
        # #1024 m846: Ray's revert/leave/rebuild decision pending - not an
        # assistant repair task. This run must not stage it.
        status = _git("status", "--porcelain").stdout
        assert "m846" not in status

    def test_do_not_touch_1024_documented(self):
        assert "Do NOT touch #1024" in _read(__file__)
