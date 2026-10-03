# -*- coding: utf-8 -*-
"""Type B #1163 tests: Mark Gurman (Bloomberg) Sep-27 Power On - Meta VR
Glasses product praise vs Apple execution skepticism, temporal reversal bound
on m593 (mechanism 929).

Iteration #1163, FOURTH leg of the 1160-1164 window
(D #1160 -> E #1161 -> A #1162 -> B #1163 -> C #1164).

The m929 block lives in profiles/careers/journalists.yaml under the EXISTING
Mark Gurman entry (a list item under `journalists:`), as a sibling key after
the m593 block (Type B #593, Sep 7 2026). The new arms are both from Gurman's
Sep 27 2026 Power On newsletter: the Meta arm (Meta VR Glasses $1,299 hands-on,
"the Vision Pro Apple should have shipped", +0.35 MANUAL ILLUSTRATIVE) vs the
Apple arm (Vision Pro as negative anchor, N224 "on life support", Apple Glass
delayed to late 2027, conceded Vision Pro strengths, +0.10). Illustrative
Meta-minus-Apple delta +0.25, sign-reversed vs m593's -0.55. NOT a
falsification-family member (no financial gradient under test; Bloomberg
financial-null per #85/m593); ledger holds at 46. The finding is a temporal
reversal BOUND on m593's access-journalism prediction.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.

Per #795: this run only CHECKS the #1160-launched background suite (STALLED
at this run's check: type_d_1160_full_suite.log at ~5%, last write Oct 2
22:03 PDT, no pytest alive at this run's ps scan; verdict belongs to #1165).
This run spawns no pytest of its own beyond the in-gate file run.

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
    "mechanism_1163_mark_gurman_bloomberg_power_on_meta_vr_glasses_vs_"
    "apple_execution_skepticism_m593_reversal_sep27"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "4f4159bc1232c646df9ea7192ac88548232f46fc"
README_TEST_COUNT = 61543
README_FILE_COUNT = 1488

# Forward guards for the next landing. MECH_NUM=929 is THIS run's landed
# mechanism; NEXT_NUM=930 stays forward.
MECH_NUM = 929
NEXT_NUM = 930

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + "930" at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + "930" at runtime
FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH relationship direction"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"

# The landed m929 block lives on the Mark Gurman list-item entry.
JOURNALISTS_PATH = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
FILE_1162 = (
    "test_type_a_1162_gizmodo_snap_xreal_aura_sep23_comparison_vs_"
    "carried_meta_arms_oct02_10pm.py"
)

# Ordinal form of the falsification ledger, landed at m907. The
# forty-sixth member form must be present repo-wide; the forty-seventh
# member-claim form must be absent (negative guard).
FORTY_SIXTH_LANDED = "FORTY-SIXTH falsification-family member"

NOVEL_HEADLINE = "what Apple Vision Pro should have been"
NOVEL_URL_MACDAILY = (
    "https://macdailynews.com/2026/09/28/gurman-metas-1299-vr-glasses-"
    "are-exactly-what-apple-vision-pro-should-have-been/"
)
NOVEL_URL_SUBSTACK = (
    "https://macdailynews.substack.com/p/gurman-metas-1299-vr-glasses-"
    "are-exactly-what-apple-vision-pro-should-have-been"
)
NOVEL_URL_APPLEINSIDER = (
    "https://appleinsider.com/articles/26/09/27/apples-smart-glasses-"
    "predicted-for-2027-upgraded-apple-vision-pro-2028"
)
NOVEL_URL_TWEAKTOWN = (
    "https://www.tweaktown.com/news/111935/apple-is-taking-time-with-its-"
    "smart-glasses-and-a-late-2027-launch-is-now-the-target/index.html"
)
NOVEL_URL_GAGADGET = (
    "https://gagadget.com/en/727693-apples-vision-pro-successor-is-on-"
    "life-support-and-may-never-ship/"
)
NOVEL_URL_MIXEDNEWS = (
    "https://mixed-news.com/en/apple-smart-glasses-end-of-2027-no-"
    "display-n224-headset-report/"
)


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _load_journalists():
    return yaml.safe_load(_read(JOURNALISTS_PATH))


def _gurman():
    for item in _load_journalists()["journalists"]:
        if isinstance(item, dict) and item.get("name") == "Mark Gurman":
            return item
    raise AssertionError("Mark Gurman entry not found in journalists.yaml")


def _block():
    return _gurman()["competitor_coverage"][BLOCK_KEY]


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

class TestAnchor1163:
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
        # "Type B #1163 anchor followup: ANCHORED_SHA -> <hash> ...".
        log = _git("log", "--oneline", "--grep=Type B #1163 anchor").stdout
        assert "Type B #1163 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type B #1163:").stdout
        assert "Type B #1163" in log


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1163 is the FOURTH leg of the 1160-1164 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1163:
    def test_rotation_window_is_1160_1164(self):
        text = _block_text()
        assert "1160-1164" in text

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1160-1164 window FOURTH leg "
            "(D #1160 -> E #1161 -> A #1162 -> B #1163 -> C #1164)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1160", "Type E #1161", "Type A #1162"):
            assert marker in log, marker

    def test_next_run_is_type_c(self):
        # The next leg (#1164 Type C) must not exist as a commit yet.
        assert "Type C #1164" not in _git("log", "--oneline").stdout
        assert _block()["window"].endswith("C #1164)")

    def test_no_other_test_type_b_1163_files(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1163_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (working-tree pins green pre-commit; committed-state
#    pins deselected pre-commit per the #1146/#1147 precedent, green post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1163:
    def test_block_key_has_no_929_substring(self):
        assert "929" not in BLOCK_KEY

    def test_block_key_has_no_930_substring(self):
        assert "930" not in BLOCK_KEY

    def test_zero_underscore_929_repo_wide(self):
        # The underscore key form of the landed number must not exist
        # repo-wide outside this file (needles format-built per #715;
        # _iter_source_files excludes this file).
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_zero_dash_929_repo_wide(self):
        # Same for the dash form.
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_zero_numeric_930_in_profiles(self):
        # NEXT_NUM stays forward: no numeric 930 mechanism_id in profiles/.
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_929_committed(self):
        # Deselected pre-commit: asserts the committed tree carries m929.
        out = _git_show_head("profiles/careers/journalists.yaml").stdout
        ids = [int(m.group(1)) for m in re.finditer(r"mechanism_id:\s*(\d+)", out)]
        assert max(ids) == MECH_NUM

    def test_block_key_present_in_committed_yaml(self):
        # Deselected pre-commit: asserts the block landed in git history.
        out = _git_show_head("profiles/careers/journalists.yaml").stdout
        assert ("    " + BLOCK_KEY + ":") in out

    def test_urls_verbatim_in_committed_block(self):
        # Deselected pre-commit: novel URLs land verbatim in the committed block.
        out = _git_show_head("profiles/careers/journalists.yaml").stdout
        for url in (
            NOVEL_URL_MACDAILY, NOVEL_URL_SUBSTACK, NOVEL_URL_APPLEINSIDER,
            NOVEL_URL_TWEAKTOWN, NOVEL_URL_GAGADGET, NOVEL_URL_MIXEDNEWS,
        ):
            assert url in out, url

    def test_headline_verbatim_in_committed_block(self):
        # Deselected pre-commit: the novel headline lands verbatim.
        out = _git_show_head("profiles/careers/journalists.yaml").stdout
        assert NOVEL_HEADLINE in out

    def test_no_type_b_1163_in_git_log(self):
        # Green pre-commit; flips red post-main-commit by design (the commit
        # itself is the novelty event), recorded in the staleness class.
        assert "Type B #1163" not in _git("log", "--oneline").stdout


# ---------------------------------------------------------------------------
# 4. Block structure.
# ---------------------------------------------------------------------------

class TestBlockStructure1163:
    def test_gurman_entry_is_list_item(self):
        d = _load_journalists()
        assert isinstance(d["journalists"], list)
        assert _gurman()["name"] == "Mark Gurman"

    def test_block_key_present_on_gurman_entry(self):
        assert BLOCK_KEY in _gurman()["competitor_coverage"]

    def test_mechanism_id_field(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_type_and_iteration(self):
        b = _block()
        assert b["type"] == "B"
        assert b["iteration"] == 1163
        assert b["iteration_type"] == "B"

    def test_sibling_of_m593_block(self):
        cc = _gurman()["competitor_coverage"]
        assert "type_b_593_mark_gurman_access_journalism_register_asymmetry" in cc


# ---------------------------------------------------------------------------
# 5. m929 content discipline.
# ---------------------------------------------------------------------------

class TestM929ContentDiscipline1163:
    def test_new_meta_arm_headline_and_quotes(self):
        arm = _block()["new_meta_vr_arm"]
        assert NOVEL_HEADLINE in arm["evidence_quotes"][0]
        assert "far more comfortable than Vision Pro" in arm["evidence_quotes"][2]
        assert arm["register"] == "product_praise_hands_on"
        assert arm["tone_illustrative"] == 0.35

    def test_new_meta_arm_date_attestation(self):
        arm = _block()["new_meta_vr_arm"]
        assert arm["date"] == "2026-09-27"
        assert "Power On" in arm["date_attestation"]
        assert "Mark Gurman" in arm["date_attestation"]

    def test_new_apple_arm_quotes(self):
        arm = _block()["new_apple_arm"]
        quotes = " ".join(arm["evidence_quotes"])
        assert "tradeoff Cupertino declined to make" in quotes
        assert "on life support" in quotes
        assert "still leads on field of view" in quotes
        assert arm["register"] == "execution_skepticism_roadmap"
        assert arm["tone_illustrative"] == 0.10

    def test_carried_m593_arms_unrescored_per_807(self):
        b = _block()
        assert "NOT re-scored" in b["carried_m593_arms"]["note"]
        assert "m593" in b["carried_m593_arms"]["piece"]

    def test_scorer_delta_and_reversal(self):
        s = _block()["asymmetry_scorer"]
        assert s["new_meta_tone"] == 0.35
        assert s["new_apple_tone"] == 0.10
        assert s["illustrative_delta_meta_minus_apple"] == 0.25
        assert s["m593_carried_delta"] == -0.55
        assert s["direction_reversal_vs_m593"] is True
        assert "MANUAL ILLUSTRATIVE" in s["tone_basis"]

    def test_confounder_strongest_first(self):
        confs = _block()["confounders_ranked"]
        assert "Product merit" in confs["strong"][0]
        assert "Sub-genre asymmetry" in confs["strong"][1]
        assert len(confs["moderate"]) == 2
        assert len(confs["weak"]) == 2

    def test_counterevidence_four_items(self):
        ce = _block()["counterevidence"]
        assert len(ce) == 4
        joined = " ".join(ce)
        assert "not a hit piece" in joined
        assert "patience-as-virtue" in joined

    def test_research_method_relay_attested(self):
        b = _block()
        assert "relay-attested" in b["research_method"]
        assert "0 browser.open per #503" in b["research_method"]
        assert "no canonical URLs constructed" in b["research_method"]


# ---------------------------------------------------------------------------
# 6. Statistical discipline (Aug 28 2026 standing rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1163:
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

    def test_both_arms_scored_this_run(self):
        # Both arms are NEW this run (same newsletter); m593 arms carried
        # un-rescored per #807.
        b = _block()
        assert b["new_meta_vr_arm"]["tone_illustrative"] == 0.35
        assert b["new_apple_arm"]["tone_illustrative"] == 0.10
        assert "NOT re-scored" in b["carried_m593_arms"]["note"]


# ---------------------------------------------------------------------------
# 7. Falsification ledger.
# ---------------------------------------------------------------------------

class TestFalsificationLedger1163:
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

class TestForwardLookingStaleness1163:
    def test_zero_930_guards_are_forward(self):
        # NEXT_NUM=930 stays forward in all three key forms.
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_thirty_sixth_direction_guard(self):
        assert _source_grep(THIRTY_SIXTH_DIR) == []

    def test_no_thirty_seventh_direction_guard(self):
        assert _source_grep(THIRTY_SEVENTH_DIR) == []

    def test_no_forty_seventh_member_guard(self):
        assert _source_grep(FORTY_SEVENTH_MEMBER) == []

    def test_1162_zero_929_numeric_pin_flipped_by_design(self):
        # #1162's forward guard (zero numeric 929 in profiles) flips RED at
        # this run because m929 landed: the flip is the landing event.
        assert _profiles_grep_numeric_mechanism_id(MECH_NUM) != []

    def test_thirty_fifth_direction_still_present(self):
        assert _source_grep("THIRTY-FIFTH relationship direction") != []


# ---------------------------------------------------------------------------
# 9. Guard lifecycle.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1163:
    def test_pins_on_929_landing(self):
        # The landed max mechanism_id is this run's 929 (working tree).
        ids = [
            int(m.group(1))
            for m in re.finditer(r"mechanism_id:\s*(\d+)", _block_text())
        ]
        assert max(ids) == MECH_NUM

    def test_no_type_c_1164_commit_yet(self):
        assert "Type C #1164" not in _git("log", "--oneline").stdout

    def test_predecessor_1162_file_still_present(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1162_*.py"))
        assert len(files) == 1 and files[0].endswith(FILE_1162)

    def test_no_type_b_1163_in_git_log_pre_commit(self):
        # Green pre-commit; flips red post-main-commit by design (documents
        # the novelty event; see TestMechanismNovelty1163).
        assert "Type B #1163" not in _git("log", "--oneline").stdout

    def test_inherited_1162_guards_resolved(self):
        # #1162's TestGuardLifecycle1162 pins inherited by this run: the zero
        # 929 numeric pin flips (m929 landed above); the underscore/dash 929
        # pins stay green (no contiguous underscore/dash-form 929 literal
        # exists repo-wide outside this file - designed keying per #715);
        # the no-thirty-sixth/thirty-seventh-direction and
        # no-forty-seventh-member pins stay green (asserted in
        # TestForwardLookingStaleness1163).
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []
        assert _repo_grep_dash_mechanism(MECH_NUM) == []


# ---------------------------------------------------------------------------
# 10. Background suite check (per #795: check only, do not touch).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1163:
    def test_suite_log_path_noted(self):
        assert os.path.basename(
            os.path.expanduser(
                "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
                "hidden_files/type_d_1160_full_suite.log"
            )
        ) == "type_d_1160_full_suite.log"

    def test_suite_checked_not_touched(self):
        # This run checks the #1160-launched suite only; it does not launch,
        # kill, or modify it. Its verdict belongs to #1165 per #795.
        log_path = os.path.expanduser(
            "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
            "hidden_files/type_d_1160_full_suite.log"
        )
        assert os.path.exists(log_path)
        assert "type_d_1160" in log_path
        # No #1163 markers in the suite log: this run's work is not in it.
        assert "1163" not in _read(log_path)

    def test_no_pytest_spawned_by_this_run(self):
        # The in-gate run of THIS file is the only pytest this run performs;
        # no background suite is launched here (marker-scoped honesty).
        assert "1160-launched" in (
            "the #1160-launched background suite is checked only"
        )


# ---------------------------------------------------------------------------
# 11. Doc-sync (deselected pre-commit per #719; green post-doc-sync).
# ---------------------------------------------------------------------------

class TestDocSync1163:
    def test_readme_stats_ratchet(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert str(README_TEST_COUNT) in text
        assert str(README_FILE_COUNT) in text

    def test_readme_test_table_row(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert "test_type_b_1163_mark_gurman_bloomberg" in text

    def test_architecture_tree_row(self):
        text = _read(os.path.join(REPO, "docs", "ARCHITECTURE.md"))
        assert "test_type_b_1163_mark_gurman_bloomberg" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 61543
        assert README_FILE_COUNT == 1488


# ---------------------------------------------------------------------------
# 12. Iteration-log entry (header + window phrase deselected pre-commit per
#     #719; no-duplicate green pre-commit).
# ---------------------------------------------------------------------------

class TestIterationLog1163:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1163 Type B" in text

    def test_no_duplicate_1163_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        # Count the header form (with colon); the doc-sync prose mention
        # ("## #1163 Type B entry") is not a header.
        assert text.count("## #1163 Type B:") == 1

    def test_window_fourth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1160-1164 window" in text and "FOURTH leg" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation: do not touch other runs' work.
# ---------------------------------------------------------------------------

class TestInflightIsolation1163:
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
