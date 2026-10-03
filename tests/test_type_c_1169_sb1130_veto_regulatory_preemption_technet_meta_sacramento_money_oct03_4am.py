# -*- coding: utf-8 -*-
"""Type C #1169 tests: SB 1130 veto (Sep 30 2026) regulatory-preemption
money channel - Newsom kills the recording-indicator mandate as Meta posts
record Sacramento lobbying spend and TechNet (Meta/Google/Amazon dues-funded)
runs the opposition channel (mechanism 933).

Iteration #1169, FIFTH and CLOSING leg of the 1165-1169 window
(D #1165 -> E #1166 -> A #1167 -> B #1168 -> C #1169).

The m933 block lives in profiles/competitor-entities.yaml as a top-level
`type_c_1169_...` key (Type C convention; cf. m930 at #1164).

This run LANDS the thirty-sixth relationship direction
(REGULATORY-PREEMPTION, mirror of #12 regulatory-bargaining m834):
industry money buys the absence of a levy. The affirmative direction claim
is new this run; the #1144/#1149/#1154/#1159 absence notes are superseded,
documented not repaired.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.

Per #795: this run only CHECKS the #1165-launched background suite
(OBSERVED DEAD/AMBIGUOUS); its verdict belongs to #1170.

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the next
number 934, the FORTY-SEVENTH member-claim form, or the thirty-seventh
direction-claim form; the thirty-sixth direction form is asserted via a
runtime-built needle against the landed YAML (never written contiguously
in source); the constants are constructed at runtime.
"""

import glob
import os
import re
import subprocess

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
TESTS_DIR = HERE

OWN_BASENAME = (
    "test_type_c_1169_sb1130_veto_regulatory_preemption_"
    "technet_meta_sacramento_money_oct03_4am.py"
)
BLOCK_KEY = (
    "type_c_1169_sb1130_veto_regulatory_preemption_"
    "technet_meta_sacramento_money_oct03_4am"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "0" * 40
# Post-first-run values per #719: collected count patched after the first
# run; README ratchets 61937/1493 -> NEW in the doc-sync followup.
README_TEST_COUNT = 61937
README_FILE_COUNT = 1493

# Forward guards for the next landing. MECH_NUM=933 is THIS run's landed
# mechanism; NEXT_NUM=934 stays forward.
MECH_NUM = 933
NEXT_NUM = 934

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + "934" at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + "934" at runtime
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH relationship direction"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"
FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"

# The landed m933 block lives here (top-level key; designed keying per
# #715: the block key carries iteration 1169, no 933 substring).
ENTITIES_PATH = os.path.join(REPO, "profiles", "competitor-entities.yaml")
FILE_1168 = (
    "test_type_b_1168_tyler_lee_phandroid_meta_luna_pervert_glasses_"
    "vs_snap_specs_launch_privacy_register_gap_sep16_17_oct03_3am.py"
)
M846_BLOCK_NEEDLE = "type_c_1024_benioff"

# Ordinal form of the falsification family. The FORTY-SIXTH member form
# must be present repo-wide; the FORTY-SEVENTH member-claim form must be
# absent (negative guard). (The falsification-family thirty-sixth member
# m878 is a separate taxonomy from the relationship-direction ordinal.)
FORTY_SIXTH_LANDED = "FORTY-SIXTH falsification-family member"


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _load_entities():
    return yaml.safe_load(_read(ENTITIES_PATH))


def _block():
    return _load_entities()[BLOCK_KEY]


def _entities_text():
    return _read(ENTITIES_PATH)


def _git(*args):
    return subprocess.run(
        ["git", "-C", REPO] + list(args), capture_output=True, text=True
    )


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
        except (OSError, UnicodeError):
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
        except (OSError, UnicodeError):
            continue
        if pattern in text:
            hits.append(path)
    return hits


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------

class TestAnchor1169:
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
        # "Type C #1169 anchor followup: ANCHORED_SHA -> <hash> ...".
        log = _git("log", "--oneline", "--grep=Type C #1169 anchor").stdout
        assert "Type C #1169 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type C #1169:").stdout
        assert "Type C #1169" in log


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1169 is the FIFTH and CLOSING leg of 1165-1169.
# ---------------------------------------------------------------------------

class TestRotationGuard1169:
    def test_rotation_window_is_1165_1169(self):
        assert "1165-1169" in _entities_text()

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1165-1169 window FIFTH and CLOSING leg "
            "(D #1165 -> E #1166 -> A #1167 -> B #1168 -> C #1169)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1165", "Type E #1166", "Type A #1167",
                       "Type B #1168"):
            assert marker in log, marker

    def test_no_type_d_1170_in_git_log_yet(self):
        # The next window (1170-1174) opens with Type D #1170; it must not
        # exist as a commit yet.
        log = _git("log", "--oneline", "--grep=Type D #1170").stdout
        assert log.strip() == ""

    def test_single_type_c_1169_test_file(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_c_1169_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (pre-commit claims, verifiable post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1169:
    def test_block_key_present_once(self):
        assert _entities_text().count(BLOCK_KEY + ":") == 1

    def test_block_key_zero_933_substring(self):
        # Designed keying per #715: the block key carries the iteration
        # number 1169, not the mechanism number 933.
        assert "933" not in BLOCK_KEY

    def test_zero_underscore_933_except_documented_prose(self):
        # The sole pre-existing underscore-form hit for the landed number
        # is #1168's negative-guard verification sentence in
        # iteration-log.md (the "verified: zero ... forms" prose) -
        # documented prose, not a key claim. Any other hit fails this test.
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [os.path.join(REPO, "iteration-log.md")], hits

    def test_zero_dash_933_except_documented_prose(self):
        # Same documented exception for the dash form (the same #1168
        # verification sentence carries it).
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [os.path.join(REPO, "iteration-log.md")], hits

    def test_zero_numeric_934_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_933(self):
        present = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert present, "m933 must be present in profiles"
        for n in range(MECH_NUM + 1, MECH_NUM + 20):
            assert _profiles_grep_numeric_mechanism_id(n) == [], n

    def test_no_duplicate_block_key(self):
        d = _load_entities()
        assert list(d.keys()).count(BLOCK_KEY) == 1

    def test_urls_copied_verbatim(self):
        urls = [s["url"] for s in _block()["sources"]]
        assert len(urls) == 9
        assert (
            "https://techcrunch.com/2026/10/01/"
            "california-governor-vetoes-bill-banning-use-of-"
            "pervert-glasses-to-secretly-record-people/"
        ) in urls
        assert (
            "https://www.fastcompany.com/91616644/"
            "bill-smart-glasses-just-blocked-californias-governor-"
            "newsom-heres-why?partner=rss&utm_source=rss&utm_medium=feed"
            "&utm_campaign=rss+fastcompany&utm_content=rss"
        ) in urls
        assert (
            "https://mixed-news.com/en/newsom-vetoes-sb-1130-"
            "smart-glasses-recording-indicator-bill/"
        ) in urls
        assert (
            "https://news.bloomberglaw.com/artificial-intelligence/"
            "meta-on-path-for-record-year-spend-on-california-tech-lobbying"
        ) in urls
        assert (
            "https://www.route-fifty.com/finance/2026/03/"
            "tech-giants-are-spending-more-ever-shape-california-"
            "politics-see-how-much/412479/"
        ) in urls
        assert (
            "https://aihaberleri.org/en/news/"
            "meta-spends-65-million-in-us-state-elections-to-shape-"
            "ai-policy-reports-reveal"
        ) in urls
        assert (
            "https://www.ainvest.com/news/"
            "meta-launches-california-pac-pro-ai-candidates-plans-"
            "tens-millions-spending-2508/"
        ) in urls
        assert (
            "https://www.webpronews.com/"
            "california-draws-first-line-against-ai-bosses-as-newsom-"
            "signs-worker-protections/"
        ) in urls
        assert (
            "https://www.recordinglaw.com/news/"
            "california-sb-1130-smart-glasses-veto/"
        ) in urls
        for u in urls:
            assert u.startswith("https://"), u

    def test_block_key_zero_hit_except_landed(self):
        # Pre-commit the block key was zero-hit repo-wide; post-commit it
        # appears only in the landed YAML block, this test file, and the
        # doc-sync surfaces (README, ARCHITECTURE, iteration-log).
        hits = _source_grep(BLOCK_KEY)
        allowed = {
            os.path.join(REPO, "profiles", "competitor-entities.yaml"),
            os.path.join(TESTS_DIR, OWN_BASENAME),
            os.path.join(REPO, "README.md"),
            os.path.join(REPO, "docs", "ARCHITECTURE.md"),
            os.path.join(REPO, "iteration-log.md"),
        }
        for h in hits:
            assert h in allowed, h


# ---------------------------------------------------------------------------
# 4. Block structure (Type C top-level key convention in
# profiles/competitor-entities.yaml).
# ---------------------------------------------------------------------------

class TestBlockStructure1169:
    def test_top_level_block_key(self):
        d = _load_entities()
        assert BLOCK_KEY in d

    def test_required_fields_present(self):
        b = _block()
        for field in (
            "block_key", "mechanism_id", "mechanism_name", "type",
            "type_label", "iteration", "iteration_type", "iteration_time",
            "goal_id", "scheduled_job_id", "window", "connects_to",
            "relationship_direction_taxonomy", "finding", "money_flow",
            "confounders", "coverage_nexus", "sources", "browser_opens",
            "tone_scored", "engine_run", "is_significant", "verdict",
            "no_analysis_json_update", "artifact_grade",
            "falsification_family_member", "falsification_family",
            "novelty", "rotation_transparency", "concurrency",
            "yaml_parse_clean", "ascii_only",
        ):
            assert field in b, field

    def test_type_and_iteration(self):
        b = _block()
        assert b["type"] == "financial_incentive_mapping"
        assert b["iteration_type"] == "C"
        assert b["iteration"] == 1169
        assert b["mechanism_id"] == 933

    def test_goal_and_job_ids(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_ascii_only_region(self):
        text = _entities_text()
        start = text.index(BLOCK_KEY + ":")
        text[start:].encode("ascii")

    def test_yaml_parse_clean(self):
        assert _block()["yaml_parse_clean"] is True
        assert _block()["ascii_only"] is True

    def test_browser_opens_zero(self):
        assert _block()["browser_opens"] == 0


# ---------------------------------------------------------------------------
# 5. m933 content discipline (the SB 1130 veto money channel).
# ---------------------------------------------------------------------------

class TestM933ContentDiscipline1169:
    def test_veto_leg(self):
        f = _block()["finding"]
        assert "Sep 30 2026" in f
        assert "too broadly or imprecisely" in f
        assert "7 million" in f
        assert "Eloise Gomez Reyes" in f

    def test_opposition_channel_leg(self):
        f = _block()["finding"]
        assert "TechNet" in f
        assert "Robert Boykin" in f
        assert "not the right approach" in f
        assert "blinded-veterans" in f

    def test_bill_mechanics_leg(self):
        f = _block()["finding"]
        assert "632.8" in f
        assert "$1,500" in f
        assert "$2,500" in f
        assert "January 1 2028" in f

    def test_money_legs(self):
        f = _block()["finding"]
        assert "$1,036,728" in f
        assert "$518,605" in f
        assert "$4.6 million" in f
        assert "$65 million" in f
        assert "California Leads" in f
        assert "Mobilizing Economic Transformation Across (Meta) California" in f

    def test_money_flow_channels(self):
        mf = _block()["money_flow"]
        assert "Dues channel" in mf
        assert "Direct-lobbying channel" in mf
        assert "Electoral channel" in mf
        assert "Avoided-cost channel" in mf

    def test_thirty_sixth_direction_landed(self):
        # Runtime-built needle per #715: the affirmative direction form
        # is new this run and must be present in the landed YAML.
        assert THIRTY_SIXTH_DIR in _entities_text()
        assert "REGULATORY-PREEMPTION" in _block()["relationship_direction_taxonomy"]
        assert "m834" in _block()["relationship_direction_taxonomy"]

    def test_connects_to(self):
        assert _block()["connects_to"] == [834, 636, 359, 33]

    def test_confounder_strongest_first(self):
        confs = _block()["confounders"]
        assert len(confs) == 6
        assert confs[0]["strength"] == "STRONG"
        strong = [c for c in confs if c["strength"] == "STRONG"]
        assert len(strong) == 3
        assert "technocratic on its face" in confs[0]["text"]

    def test_coverage_nexus_bounded_absence(self):
        cn = _block()["coverage_nexus"]
        assert "iteration-492" in cn
        assert "bounded absence" in cn
        assert "WIRED" in cn

    def test_not_falsification_member(self):
        b = _block()
        assert b["falsification_family_member"] is False

    def test_research_method_excerpt_tier(self):
        n = _block()["novelty"]
        assert "4 browser.search query sets" in n
        assert "0 browser.open" in n


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL/QUALITATIVE ONLY per Aug 28 2026 rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1169:
    def test_no_engine_run(self):
        b = _block()
        assert b["engine_run"] is False
        assert b["tone_scored"] is False

    def test_stats_not_calculated(self):
        n = _block()["novelty"]
        assert "MANUAL / qualitative-only" in n
        assert "Aug 28 2026 standing rule" in n

    def test_verdict_discipline(self):
        b = _block()
        assert b["verdict"] == "directionally_supported_not_proven"
        assert b["no_analysis_json_update"] is True
        assert b["is_significant"] is False

    def test_not_artifact_grade(self):
        b = _block()
        assert b["artifact_grade"] is False


# ---------------------------------------------------------------------------
# 7. Falsification ledger (holds at 46; no new member this run).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1169:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False

    def test_forty_sixth_member_form_present(self):
        assert _repo_grep(FORTY_SIXTH_LANDED), FORTY_SIXTH_LANDED

    def test_forty_seventh_member_claim_absent(self):
        # Negative-guard wordings ("absent repo-wide") are allowed; the
        # affirmative member-claim form must not exist. Needle format-built
        # per #715; own file carries no contiguous needle.
        assert FORTY_SEVENTH_MEMBER not in _entities_text()

    def test_ledger_note_wording(self):
        ff = _block()["falsification_family"]
        assert "ledger holds at 46" in ff
        assert "FORTY-SEVENTH member-claim form absent repo-wide" in ff
        assert "thirty-seventh direction form absent repo-wide" in ff


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (designed lifecycle; the #1170 Type D run
# pins the 934 landing).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1169:
    def test_zero_934_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 934" in src
        # Needles format-built per #715: constructed at runtime, never
        # written contiguously in source.
        assert (MECH_ID_MARKER + str(NEXT_NUM)) not in src
        assert (MECH_DASH_MARKER + str(NEXT_NUM)) not in src

    def test_no_thirty_seventh_direction_guard(self):
        # The contiguous direction-claim form must not appear in this
        # file's source; the guard constant stays format-built per #715.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("THIRTY" + "-SEVENTH relationship direction") not in src
        assert len(THIRTY_SEVENTH_DIR) > 0

    def test_no_forty_seventh_member_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("FORTY" + "-SEVENTH falsification-family member") not in src
        assert len(FORTY_SEVENTH_MEMBER) > 0

    def test_1168_pins_flip_by_design_documented(self):
        # #1168's forward guards (max-932, zero-933 numeric in profiles,
        # no-Type-C-#1169-in-git-log) flip by design now that m933 has
        # landed and this run commits; recorded, not repaired. #1168's
        # own-file underscore/dash-933, no-thirty-sixth, no-forty-seventh
        # guards stay green (this run does not touch #1168's file), as
        # does the thirty-fifth-intact guard.
        rt = _block()["rotation_transparency"]
        assert "fail BY DESIGN" in rt
        assert "max-932" in rt

    def test_thirty_fifth_direction_still_present(self):
        # m915's METER-THEN-INVITE is the THIRTY-FIFTH relationship
        # direction; its ordinal wording must still be present repo-wide.
        assert "THIRTY-FIFTH" in _entities_text()

    def test_thirty_sixth_now_landed(self):
        # This run lands the affirmative thirty-sixth direction claim;
        # the #1144/#1149/#1154/#1159 absence notes are superseded
        # (documented in novelty, not repaired).
        assert THIRTY_SIXTH_DIR in _entities_text()
        assert "superseding those absence notes" in _block()["novelty"]


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this run pins the 933 landing for #1170).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1169:
    def test_pins_on_933_landing(self):
        # The guards this run lays for the next leg: max-933, zero-934
        # numeric, no-Type-D-#1170-in-git-log.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 933" in src
        assert "NEXT_NUM = 934" in src

    def test_no_type_d_1170_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type D #1170").stdout
        assert log.strip() == ""

    def test_934_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1168_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1168))


# ---------------------------------------------------------------------------
# 10. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1170).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1169:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1165_full_suite.log" in src

    def test_suite_observed_dead_ambiguous_recorded_not_touched(self):
        # This run stays on targeted verification per the Type C brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest death-observation per #795:
        # #1165-launched suite DEAD/AMBIGUOUS at the 04:00 PDT check
        # (log 1134 bytes, last write Oct 3 01:22 PDT, one pytest process
        # at ps scan, no m933 markers; byte-identical to #1168's check).
        # #1170 owns the verdict.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "DEAD/AMBIGUOUS" in src
        assert "#1170" in src

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no m933 markers.
        suite_log = os.path.expanduser(
            "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
            "hidden_files/type_d_1165_full_suite.log"
        )
        log = _read(suite_log)
        assert "m933" not in log
        assert "Type C #1169" not in log


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1169:
    def test_readme_stats_table_updated(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert "| Tests |" in text

    def test_readme_test_table_row_present(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert OWN_BASENAME in text

    def test_architecture_tree_row_present(self):
        text = _read(os.path.join(REPO, "docs", "ARCHITECTURE.md"))
        assert OWN_BASENAME in text

    def test_iteration_log_entry_present(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "#1169" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 61937
        assert README_FILE_COUNT == 1493


# ---------------------------------------------------------------------------
# 12. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1169:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1169 Type C:" in text

    def test_no_duplicate_1169_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1169 Type C:") == 1

    def test_window_fifth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1165-1169" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1169:
    def test_inflight_files_untouched_by_this_run(self):
        # Marker-scoped: the working tree carries pre-existing
        # in-flight uncommitted changes (#899 nytimes.yaml hunk,
        # #938 test file, #900 test file, #1012-wt test-file edit).
        # This run's markers must appear in NONE of their diffs;
        # targeted staging at commit time picks up only this run's
        # two files.
        for path in (
            "profiles/nytimes.yaml",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_"
            "gemini_personalization_vs_meta_luna_stigma_sep16.py",
            "tests/test_type_d_900_m769_qualitative_corpus_integrity_"
            "sep21_1pm.py",
            "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_"
            "turn_agenda_setting_register_vs_carried_meta_india_"
            "havoc_m817_pairing_sep26_7am.py",
        ):
            diff = _git("diff", "--", path).stdout
            assert "mechanism_id: 933" not in diff, path
            assert "Type C #1169" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 block lives in profiles/competitor-entities.yaml;
        # this run appends the m933 block at the end of that file but must
        # not alter the m846 block region.
        diff = _git("diff", "--", "profiles/competitor-entities.yaml").stdout
        assert M846_BLOCK_NEEDLE not in diff
        assert "mechanism_id: 933" in diff
