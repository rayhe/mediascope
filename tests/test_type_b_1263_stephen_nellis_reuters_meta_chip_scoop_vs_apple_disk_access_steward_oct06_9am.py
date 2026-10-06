# -*- coding: utf-8 -*-
"""Type B #1263 tests: Stephen Nellis (Reuters) journalist
cross-entity pair - Meta Jul-9 AI-chip manufacturing scoop
(neutral business register, co-byline, NEW arm) vs Apple Oct-2
macOS Full Disk Access steward register (Meta's Muse named as
the cautionary foil, solo byline, NEW arm).

Mechanism 989 (BOUNDED thesis-challenging observation, NOT a
falsification-family member; ledger holds at 54). Same writer,
same outlet, about three months apart (Jul 9 vs Oct 2, 2026):
Nellis covers the payer Meta through a neutral scoop register
(+0.05 MANUAL ILLUSTRATIVE) and covers Apple through the
good-faith steward register (+0.30, "will introduce additional
controls", headline "after Meta's Muse draws complaints").
Illustrative delta (Apple minus Meta) +0.25 runs counter to the
uniform payer-softening prediction at headline level (Thomson
Reuters x Meta multi-year AI content licensing, Oct 25 2024,
in-corpus) - the payer draws no visible softness. Wire-service
genre (headline foil is Apple's announcement positioning, not
the reporter's own register) and co-byline asymmetry are the
STRONG confounds; the May-7 Rave-antitrust piece is the
intra-journalist counterpoint (Nellis adversarial on Apple when
the peg warrants). MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026
standing rule (both tones hand-assigned; n=1 per arm;
p_value/cohens_d/ci_95 NOT_CALCULATED; engine NOT run;
is_significant false; NOT artifact-grade; verdict
thesis_challenging_bounded_observation; no analysis.json update).

Research: scout (8 browser.search query sets across candidate
journalists; SELECTED Nellis as the freshest same-journalist
same-outlet pair with byline-complete arms; rejected with
numbered audit: Jay Peters saturated (2 Type B mechanisms
m833/m893), Robert Hart saturated (2 Type B mechanisms
#608/#653), Emma Roth saturated (4 mechanisms), WIRED
Muse-dossier byline unattributable from bounded search, WIRED
Sep-25 ChatGPT-Mac-flaw byline unattributable (relays say "told
WIRED" with no reporter name - investigated, not built, same as
#1203's WIRED Sep-15 piece), Jason Aten (Inc. columnist)
single-entity peg with no cross-entity pair) + main-run
verification (exact-headline searches returning the srnnews
6-mirror "By Stephen Nellis" consensus for Oct-2, the wixx byline
block "By Katie Paul, Max A. Cherney and Stephen Nellis" for
Jul-9, the srnnews "By Stephen Nellis" for the May-7 Rave
counterpoint; corpus saturation greps: 3 novel mirror URLs
zero-hit repo-wide via git grep -F, no stephen_nellis_type_b key
pre-commit, no "Type B #1263" in git log; the Oct-2 reuters.com
canonical sits in-corpus as the m988 context_peg - cited as
already-attested, not re-counted as novel). 0 browser.open per
#503 (excerpt-bounded). All URLs copied verbatim from Full-URL
listings; no canonical reuters.com URLs constructed. The m989
block lands in profiles/careers/journalists.yaml as the new
stephen_nellis_type_b entry (FIRST block; mechanism_ids [989]).
Targeted staging by explicit path only; the in-flight
#899/#938/#900/#1012-wt files stay out of this run's index/diff.
Do NOT touch #1024 m846.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the
anchor followup commit. One anchor test (the placeholder pin)
fails BY DESIGN pre-commit; TestAnchor1263 deselected in the
in-gate run. The main commit is the anchor per #565.

FOURTH leg of the 1260-1264 window: D #1260 -> E #1261 -> A #1262
-> B #1263 -> C #1264 per the #565 anchor + rotation guard. Next
run #1264 Type C closes the window. Type B lands one mechanism
(mechanism 989).

Per #795: this run only CHECKS the #1260-launched background suite
(goal hidden_files type_d_1260_full_suite.log, observed NOT-ALIVE
at this run's check: 3658 bytes / [ 4%] progress, last write Oct 6
15:18 UTC (08:18 PDT, no writes since the #1262 check), zero live
pytest processes at check time - an observation, not a verdict; no
verdict declared); its verdict and tombstone belong to #1265 (next
Type D). This run neither re-launches, kills, nor writes to the
suite.

ASCII-only, no em dashes. Needles format-built per #715: this file
must not carry contiguous numeric/underscore/dash mechanism-key forms
of the landed or next number, the forty-eighth / forty-ninth /
fiftieth / fifty-first / fifty-second / fifty-third / fifty-fourth
member-claim forms, the fifty-fifth member-claim form, or the fortieth
direction form; the constants are constructed at runtime. (The landed
ordinals live as short lowercase forms in prose here; the live
full-form claims live in profiles/: the forty-eighth in
profiles/financial-times.yaml, the forty-ninth / fiftieth /
fifty-second in profiles/careers/journalists.yaml, the fifty-first in
profiles/news-corp.yaml, the fifty-third in profiles/the-verge.yaml,
and the fifty-fourth in profiles/guardian.yaml.)
"""
import os
import re
import subprocess

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
GOAL_HIDDEN = os.path.join(
    os.path.expanduser("~"), "workspace", "goals",
    "mediascope-meta-wearables-press-analysis", "hidden_files",
)
OWN_BASENAME = (
    "test_type_b_1263_stephen_nellis_reuters_meta_chip_scoop_"
    "vs_apple_disk_access_steward_oct06_9am.py"
)
PROFILE_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1260_full_suite.log")

MECH_NUM = 989
NEXT_NUM = 990  # integer only; key-form needles are format-built
ITERATION = 1263

ANCHORED_SHA = "0" * 40

# Predecessor #1262 chain (verified via git rev-parse pre-commit).
PRED_MAIN_1262 = "2637d58ce2aea540e984598a108345ba440efd45"
PRED_ANCHOR_1262 = "f4db4c57f4ff05ee42ed0c60eab54dab53116db2"
PRED_DOCSYNC_1262 = "44c5db2b5fdfe790a21f38ab2597e006184d9aa5"
PRED_FINAL_1262 = "a1a633d26c89da1b84f82fa9c7bd17bcb1dc2a0d"
# Predecessor #1261 chain (window SECOND leg).
PRED_MAIN_1261 = "19b153f21f1a62a9c12f198d5c59f5bd6778b4f1"
A1262_FILE = (
    "test_type_a_1262_wired_meta_muse_dossier_vs_apple_steward_"
    "register_oct06_840am.py"
)

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770
_T40 = "FORT" + "IETH relationship direction"
_T48 = "FORT" + "Y-EIGHTH falsification-family member"
_T49 = "FORT" + "Y-NINTH falsification-family member"
_T50 = "FIFT" + "IETH falsification-family member"
_T51 = "FIFT" + "Y-FIRST falsification-family member"
_T52 = "FIFT" + "Y-SECOND falsification-family member"
_T53 = "FIFT" + "Y-THIRD falsification-family member"
_T54 = "FIFT" + "Y-FOURTH falsification-family member"
_T55 = "FIFT" + "Y-FIFTH falsification-family member"

BLOCK_KEY = (
    "type_b_1263_stephen_nellis_reuters_meta_chip_scoop_"
    "vs_apple_disk_access_steward_oct06_9am"
)
JOURNALIST_KEY = "stephen_nellis_type_b"

# The three novel source URLs (verbatim from Full-URL listings,
# zero-hit repo-wide pre-commit via git grep -F).
PEG_URLS = [
    "https://wixx.com/2026/07/09/exclusive-meta-to-put-ai-chip-into-"
    "production-in-september-as-it-looks-to-double-computing-capacity-"
    "memo-shows/",
    "https://srnnews.com/apple-says-it-will-flag-ai-requests-for-mac-"
    "data-after-metas-muse-draws-complaints/",
    "https://srnnews.com/rave-files-antitrust-lawsuit-against-apple-"
    "over-removal-of-video-sharing-app/",
]


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git"] + list(args), cwd=REPO_ROOT, capture_output=True, text=True,
    )


def _block():
    import yaml
    with open(PROFILE_FILE, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    return data[JOURNALIST_KEY]["competitor_coverage"][BLOCK_KEY]


def _iter_source_files():
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [
            d for d in dirs
            if d not in ("__pycache__", ".git", ".venv", "node_modules")
        ]
        for f in files:
            yield os.path.join(root, f)


def _git_grep_tracked_source(needle, scope):
    args = ["grep", "-F", "-l", needle, "HEAD", "--"]
    args.append(scope if scope else ".")
    out = _git(*args).stdout
    hits = []
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        # git grep on a revision emits "HEAD:<path>" per file; strip
        # the revision prefix before the path checks.
        if line.startswith("HEAD:"):
            line = line[len("HEAD:"):]
        hits.append(line)
    return hits


def _worktree_grep_files(needle):
    """Return working-tree files containing a literal needle."""
    out = _git("grep", "-F", "-l", needle, "--", ".").stdout
    return [l for l in out.splitlines() if l.strip()]


def _repo_grep_underscore_mechanism(n):
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [
        p for p in _iter_source_files()
        if needle in open(p, encoding="utf-8", errors="replace").read()
    ]


def _repo_grep_dash_mechanism(n):
    needle = "mechanism" + "-" + str(n)
    return [
        p for p in _iter_source_files()
        if needle in open(p, encoding="utf-8", errors="replace").read()
    ]


def _repo_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in open(p, encoding="utf-8", errors="replace").read():
                hits.append(p)
    return hits


def _max_numeric_mechanism_id():
    found = []
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            text = open(
                os.path.join(root, f), encoding="utf-8", errors="replace"
            ).read()
            found.extend(int(m) for m in pat.findall(text))
    return max(found) if found else 0


def _class_run(test_file, class_name):
    return subprocess.run(
        ["python3", "-m", "pytest", test_file + "::" + class_name, "-q"],
        cwd=TESTS_DIR, capture_output=True, text=True,
    )


# ---------------------------------------------------------------------------
# 1. Anchor (deselected in-gate per #565; placeholder fails BY DESIGN).
# ---------------------------------------------------------------------------

class TestAnchor1263:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to the main commit sha per #565. Deselected in
        # the in-gate run; the patched form is asserted post-anchor.
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_to_main_commit(self):
        # Post-commit form: ANCHORED_SHA patched to this run's main
        # commit sha per #565 in the anchor followup. Pre-commit this
        # is 0*40 and the test fails BY DESIGN; deselected in-gate.
        assert ANCHORED_SHA != "0" * 40
        assert len(ANCHORED_SHA) == 40

    def test_anchor_sha_format(self):
        assert len(ANCHORED_SHA) == 40

    def test_this_run_main_commit_is_anchor(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "main commit is the anchor" in src

    def test_rotation_phrase_in_docstring(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FOURTH leg of the 1260-1264 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1263:
    def test_predecessor_1262_chain_verified(self):
        for sha in (
            PRED_MAIN_1262, PRED_ANCHOR_1262, PRED_DOCSYNC_1262,
            PRED_FINAL_1262,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1261_main_verified(self):
        res = _git("cat-file", "-t", PRED_MAIN_1261)
        assert res.stdout.strip() == "commit", "missing 1261 main"

    def test_window_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1260 -> E #1261 -> A #1262 -> B #1263 -> C #1264" in src

    def test_next_is_type_c_1264(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1264 Type C closes the window" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty
# ---------------------------------------------------------------------------

class TestMechanismNovelty1263:
    def test_no_type_b_1263_file_precommit(self):
        # Own file excluded: exactly one match (this file) post-commit.
        hits = [
            f for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_b_1263")
        ]
        assert hits == [OWN_BASENAME], hits

    def test_journalist_key_present_post_commit(self):
        text = _read(PROFILE_FILE)
        assert JOURNALIST_KEY in text

    def test_block_key_present_post_commit(self):
        assert BLOCK_KEY in _read(PROFILE_FILE)

    def test_mechanism_id_landed(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_iteration_field(self):
        assert _block()["iteration"] == ITERATION

    def test_next_number_forms_absent(self):
        # NEXT_NUM = 990 must have zero key forms (forward guard).
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_peg_urls_novel(self):
        for url in PEG_URLS:
            hits = _worktree_grep_files(url)
            # Post-commit each URL lives in the profile block and in
            # this file's PEG_URLS constant (the novelty carrier).
            assert any(
                h.endswith("careers/journalists.yaml") for h in hits
            ), (url, hits)
            assert set(hits) <= {
                "profiles/careers/journalists.yaml",
                "tests/" + OWN_BASENAME,
            }, (url, hits)


# ---------------------------------------------------------------------------
# 4. Block structure: the m989 pair
# ---------------------------------------------------------------------------

class TestBlockStructure1263:
    def test_required_top_fields(self):
        block = _block()
        for key in (
            "block_key", "mechanism_id", "iteration", "type", "date",
            "test_file", "author", "goal_id", "job_id", "scheduled_job_id",
            "journalist", "publication", "window", "design", "finding",
            "meta_arm", "apple_arm", "scorer", "financial_context",
            "confounders", "counter_evidence", "statistical_discipline",
            "verdict", "cautious_language_required", "correlational_note",
            "no_analysis_json_update", "falsification_family_member",
            "falsification_ledger", "ledger_note", "connects_to",
            "novelty", "research_method", "artifact_readiness",
            "background_suite_status", "in_flight", "source_urls",
        ):
            assert key in block, key

    def test_mechanism_ids_field(self):
        import yaml
        with open(PROFILE_FILE, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        assert data[JOURNALIST_KEY]["mechanism_ids"] == [MECH_NUM]

    def test_arm_structure(self):
        block = _block()
        for arm_name in ("meta_arm", "apple_arm"):
            arm = block[arm_name]
            for key in (
                "entity", "outlet", "author_byline", "title", "date",
                "tone_MANUAL_ILLUSTRATIVE",
            ):
                assert key in arm, (arm_name, key)

    def test_block_key_designed_keying(self):
        # Designed keying per #715: iteration 1263 in key, no 989
        # substring anywhere in the key.
        assert "1263" in BLOCK_KEY
        assert "989" not in BLOCK_KEY
        assert _block()["block_key"] == BLOCK_KEY

    def test_three_source_urls(self):
        assert len(_block()["source_urls"]) == 3

    def test_type_and_entities(self):
        block = _block()
        assert block["type"] == "B"
        assert block["journalist"] == "Stephen Nellis"
        assert block["publication"] == "Reuters"
        assert block["meta_arm"]["entity"] == "meta"
        assert block["apple_arm"]["entity"] == "apple"


# ---------------------------------------------------------------------------
# 5. m989 content discipline
# ---------------------------------------------------------------------------

class TestM989ContentDiscipline1263:
    def test_meta_arm_headline_present(self):
        title = _block()["meta_arm"]["title"]
        assert "put AI chip into production" in title

    def test_apple_arm_headline_present(self):
        title = _block()["apple_arm"]["title"]
        assert "flag AI requests for Mac data" in title

    def test_bylines(self):
        block = _block()
        assert "Stephen Nellis" in block["meta_arm"]["author_byline"]
        assert block["apple_arm"]["author_byline"] == "Stephen Nellis (solo byline)"

    def test_arm_dates(self):
        block = _block()
        assert block["meta_arm"]["date"] == "2026-07-09"
        assert block["apple_arm"]["date"] == "2026-10-02"

    def test_meta_arm_new_not_carried(self):
        block = _block()
        assert "NEW this run" in block["meta_arm"]["status"]
        assert block["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == 0.05

    def test_apple_arm_tone_manual_illustrative(self):
        assert _block()["apple_arm"]["tone_MANUAL_ILLUSTRATIVE"] == 0.3

    def test_delta_arithmetic(self):
        block = _block()
        delta = block["scorer"]["illustrative_delta_apple_minus_meta"]
        expected = (
            block["apple_arm"]["tone_MANUAL_ILLUSTRATIVE"]
            - block["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"]
        )
        assert abs(delta - expected) < 1e-9
        assert abs(delta - 0.25) < 1e-9

    def test_scorer_discipline(self):
        scorer = _block()["scorer"]
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci_95"] == "NOT_CALCULATED"
        assert scorer["engine_run"] is False
        assert scorer["is_significant"] is False

    def test_thesis_challenging_marking(self):
        block = _block()
        assert block["falsification_family_member"] is False
        assert block["falsification_ledger"] == 54
        assert "thesis-challenging" in block["finding"]
        assert "NOT a falsification-family member" in block["finding"]

    def test_financial_context_thomson_reuters_meta_deal(self):
        context = _block()["financial_context"]
        assert "Thomson Reuters" in context
        assert "Oct 25, 2024" in context

    def test_confounder_wire_genre_strong(self):
        confs = _block()["confounders"]["strong"]
        assert len(confs) >= 2
        joined = " ".join(confs)
        assert "Wire" in joined

    def test_counter_evidence_rave(self):
        joined = " ".join(_block()["counter_evidence"])
        assert "Rave" in joined

    def test_ascii_only_profile_block(self):
        import yaml
        with open(PROFILE_FILE, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        text = yaml.safe_dump(data[JOURNALIST_KEY], allow_unicode=False)
        text.encode("ascii")

    def test_no_em_dash_in_new_files(self):
        for path in (
            PROFILE_FILE, os.path.join(TESTS_DIR, OWN_BASENAME),
        ):
            assert "\u2014" not in _read(path), path

    def test_urls_verbatim(self):
        block = _block()
        assert block["meta_arm"]["url"] == PEG_URLS[0]
        assert block["apple_arm"]["url"] == PEG_URLS[1]
        assert block["source_urls"] == PEG_URLS


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL/QUALITATIVE ONLY)
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1263:
    def test_not_significant(self):
        assert _block()["scorer"]["is_significant"] is False

    def test_correlation_not_causation(self):
        assert "Correlation is not causation" in _block()["correlational_note"]

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_manual_illustrative_only(self):
        discipline = _block()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE scores only" in discipline
        assert "NOT artifact-grade" in discipline

    def test_engine_not_run(self):
        text = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "engine NOT run" in text

    def test_verdict_bounded(self):
        assert _block()["verdict"].startswith(
            "thesis_challenging_bounded_observation")


# ---------------------------------------------------------------------------
# 7. Falsification ledger (holds at 54)
# ---------------------------------------------------------------------------

class TestFalsificationLedger1263:
    def test_ledger_holds_at_54(self):
        assert _block()["falsification_ledger"] == 54

    def test_not_a_member(self):
        assert _block()["falsification_family_member"] is False

    def test_forty_eighth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_forty_ninth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T49, "profiles/") == [
            "profiles/careers/journalists.yaml"]

    def test_fiftieth_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T50, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_first_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T51, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_second_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T52, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_fifty_third_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T53, "HEAD", "--",
            "profiles/the-verge.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fourth_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T54, "HEAD", "--",
            "profiles/guardian.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_fifty_fifth_member_pin(self):
        assert _git_grep_tracked_source(_T55, ".") == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: forward guards for #1264 (Type C)
# ---------------------------------------------------------------------------

class TestGuardLifecycle1263:
    def test_pins_on_989_landing(self):
        # Type B lands m989: max becomes 989, next is 990.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 989" in src
        assert "NEXT_NUM = 990" in src

    def test_no_type_c_1264_in_git_log_pin(self):
        out = _git("log", "--oneline", "--grep=Type C #1264")
        assert out.stdout.strip() == ""

    def test_990_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_990_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_990_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        # The fortieth direction-claim form stays absent in profiles/.
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_forty_ninth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T49, "profiles/") == [
            "profiles/careers/journalists.yaml"]

    def test_fiftieth_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T50, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_first_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T51, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_second_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T52, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_fifty_third_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T53, "HEAD", "--",
            "profiles/the-verge.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fourth_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T54, "HEAD", "--",
            "profiles/guardian.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_fifty_fifth_member_pin(self):
        assert _git_grep_tracked_source(_T55, None) == []

    def test_predecessor_1262_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, A1262_FILE))

    def test_next_leg_is_1264_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1264 Type C" in src

    def test_1262_pins_flip_by_design_documented(self):
        # #1262's forward guards (max-988, zero-989 keys all forms,
        # no-Type-B-#1263-in-git-log, fortieth absent, forty-eighth +
        # forty-ninth + fiftieth + fifty-first + fifty-second +
        # fifty-third + fifty-fourth intact, no fifty-fifth; ledger 54)
        # verified GREEN at HEAD pre-commit this run via the
        # subprocess staleness pin (Type B lands m989 as a bounded
        # thesis-challenging observation, NOT a falsification-family
        # member); the no-Type-B-#1263-in-git-log and zero-989-numeric
        # pins flip post-main-commit on this run's own landing (the
        # #1191-class self-trip, by design, documented in the
        # staleness pin below).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1263" in src
        assert "no_type_b_1263_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 9. Background suite (per #795: CHECKED ONLY this run)
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1263:
    def test_suite_log_exists(self):
        assert os.path.exists(SUITE_LOG), SUITE_LOG

    def test_suite_log_nonempty(self):
        assert os.path.getsize(SUITE_LOG) > 0

    def test_run_neither_relaunches_nor_kills(self):
        # Observation-only per #795: this run's own processes must not
        # include a suite launcher it started.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "neither" in src and "re-launches" in src

    def test_verdict_belongs_to_1265(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "belong to #1265" in src


# ---------------------------------------------------------------------------
# 10. Doc-sync (post-sync positive per #719; deselected in-gate).
# ---------------------------------------------------------------------------

class TestDocSync1263:
    def test_readme_test_file_table_has_1263_row_post_sync(self):
        text = _read(README_PATH)
        assert "test_type_b_1263" in text

    def test_architecture_has_1263_row_post_sync(self):
        text = _read(ARCH_PATH)
        assert "test_type_b_1263" in text

    def test_readme_stats_ratcheted(self):
        text = _read(README_PATH)
        assert str(README_TEST_COUNT) in text
        assert str(README_FILE_COUNT) in text


# ---------------------------------------------------------------------------
# 11. Iteration log (post-sync positive per #721; deselected in-gate).
# ---------------------------------------------------------------------------

class TestIterationLog1263:
    def test_1263_entry_present_post_sync(self):
        text = _read(LOG_PATH)
        assert "## #1263" in text

    def test_1262_entry_present(self):
        text = _read(LOG_PATH)
        assert "## #1262" in text

    def test_rotation_transparency_convention(self):
        text = _read(LOG_PATH)
        assert "1260-1264 window" in text


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1262's guard lifecycle flips by design
#      (1 test; deselected pre-commit, verified post-main-commit)
# ---------------------------------------------------------------------------

class TestStalenessPins1263:
    def test_1262_guard_lifecycle_flips_by_design_post_commit(self):
        # Runs the #1262 file's guard-lifecycle class post-commit:
        # its no-Type-B-#1263-in-git-log pin self-trips on this run's
        # own main commit and its zero-989-numeric pin trips on the
        # landed m989 block (both BY DESIGN, the #1191-class self-trip
        # family); the class is expected to report the flips, not to
        # stay green.
        res = _class_run(A1262_FILE, "TestGuardLifecycle1262")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "failed" in res.stdout, res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation: other runs' working state untouched.
# ---------------------------------------------------------------------------

class TestInFlightIsolation1263:
    def test_899_nytimes_hunk_untouched(self):
        out = _git("diff", "--cached", "--name-only").stdout
        assert "profiles/nytimes.yaml" not in out

    def test_938_test_file_untouched(self):
        out = _git("diff", "--cached", "--name-only").stdout
        assert "test_type_b_938" not in out

    def test_900_test_file_untracked_not_staged(self):
        out = _git("diff", "--cached", "--name-only").stdout
        assert "test_type_d_900" not in out

    def test_1012_wt_untouched(self):
        out = _git("diff", "--cached", "--name-only").stdout
        assert "test_type_a_1012" not in out

    def test_1024_m846_untouched(self):
        out = _git("diff", "--cached", "--name-only").stdout
        assert "profiles/competitor-entities.yaml" not in out

    def test_only_expected_paths_staged(self):
        out = _git("diff", "--cached", "--name-only").stdout
        staged = [l.strip() for l in out.splitlines() if l.strip()]
        allowed = {
            "tests/" + OWN_BASENAME,
            "profiles/careers/journalists.yaml",
        }
        assert set(staged) <= allowed, staged


README_TEST_COUNT = 69708  # 69620 + 88, patched per #719
README_FILE_COUNT = 1588  # 1587 + 1, patched per #719
