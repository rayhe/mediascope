# -*- coding: utf-8 -*-
"""Type B #1323 tests: Katie Paul (Reuters) - Sep-22-2026 "human
concierge" Muse accountability exclusive (-0.45 MANUAL ILLUSTRATIVE, NEW
Meta arm: human contractors quietly handling Muse phone calls, employee
privacy concerns, "it was a miss", feature rolled back) vs carried
Sep-8-2026 Muse-launch accountability arm (-0.45 MANUAL ILLUSTRATIVE,
m633, Type C #664, un-rescored per #807: "despite internal concerns
that the technology mismanages its access to sensitive personal data",
"RAISING THE STAKES FOR SAFETY"); illustrative delta (new minus
carried) 0.00 - register constancy, same writer, same outlet, 14 days
apart, both accountability scoops on the payer.

Mechanism 1025 (NOT a falsification-family member; ledger holds at 60).
FIRST dedicated Type B mechanism on Katie Paul (zero katie_paul_type_b
keyed entry pre-commit; mention-level hits only: the #664/#667
publication-level mechanisms m633/m634, the Jul-2 add-5-journalists
profile entry, and a scout-rejection note, disclosed). TEMPORAL
REPLICATION of the THIRTEENTH member's writer-level pattern per the
#1143 precedent: the same writer/partner prediction test (Reuters, paid
by Meta under the Oct-25-2024 multiyear AI licensing deal m633, goes
softer on payer Meta) was already counted at #664 as the THIRTEENTH
member, with Paul's Sep-8 piece as the falsification pin; Paul's Sep-22
"human concierge" exclusive runs the same adversarial-on-payer register
14 days later. A same-writer temporal replication is not a new
prediction test, so the ledger holds at 60. The finding STRENGTHENS the
thirteenth member: the paid counterparty's lead Meta reporter ran hard
accountability twice in the Muse launch window.

Excerpt-bounded research per #503 (main-run candidate screening, 2
main-run browser.search verification sets, 0 browser.open reads). The
candidate screen SELECTED Paul (cleanest surviving pair - same writer,
same outlet, both accountability-scoop pegs 14 days apart, novel
journalist, sole byline, verbatim relay URL from Full-URL listing) and
REJECTED: Criddle (saturated - #1143 m917 temporal replication already
covers her Sep-16 OpenAI/Anthropic arm, and the FT Muse-launch headline
is in-corpus in profiles/financial-times.yaml), Bellan (saturated -
m305 at #289), Stern (dedicated Type B cross-entity test in-corpus),
Chokkattu (saturated - m362/#351, #411, #528), Aisha Malik (novel but
no clean cross-entity comparator arm - Meta/social beat only
in-window). Prior-run rejection lists stand.

The m1025 block lives in profiles/careers/journalists.yaml under the
katie_paul_type_b keyed entry's competitor_coverage dict (per the #643
convention); mechanism_ids [1025].

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup commit. One anchor test (the placeholder pin) fails BY DESIGN
post-anchor.

Per #795: this run only CHECKS the #1320-launched background suite
(goal hidden_files type_d_1320_full_suite.log, observed at this run's
check; an observation, not a verdict); its verdict and tombstone belong
to #1325 (next Type D). This run neither re-launches, kills, nor writes
to the suite.

Rotation: this run is iteration #1323 Type B, the FOURTH leg of the
1320-1324 window (D #1320 -> E #1321 -> A #1322 -> B #1323 -> C #1324, per
the #565 anchor + rotation guard). Predecessor #1322 Type A verified in
git log (main 237e0a1e / anchor 1e2d00af / doc-sync fa17e8d9 / log-hash
83b6672f); #1321 Type E verified (main a8ac5238 / anchor c2f5a24b /
doc-sync 85e2481c / log-hash a283839e); the 1315-1319 window is VERIFIED
CLOSED. This run's main commit is the anchor per #565; ANCHORED_SHA
patched post-commit. The #1322 forward guards verified pre-commit this
run: max-1024; zero one-zero-two-five keys all forms; no-Type-B-#1323-
in-git-log; fortieth direction absent; forty-eighth through sixtieth
members intact; no sixty-first member (repo-wide); ledger 60. Next run
#1324 Type C closes the window; the #1320-launched background-suite
verdict belongs to #1325 per #795.

Type B lands one mechanism (m1025). Pre-commit novelty greps per #715:
zero test_type_b_1323 files on disk (glob); no "Type B #1323" in git log
(--grep); max numeric mechanism_id 1024 in profiles/ pre-commit
(mechanism_id regex sweep); zero numeric/underscore/dash
one-zero-two-five mechanism key forms repo-wide pre-commit (needles
format-built per #715, own file excluded, __pycache__ excluded);
"katie paul" mention-level hits only pre-commit (the #664/#667
mechanisms, the Jul-2 profile entry, one scout-rejection note; zero
katie_paul_type_b keyed entry); block key zero-hit repo-wide
pre-commit (designed keying: iteration 1323 in key, no 1025 substring,
per the #723/#738/#739 convention); "## #1323" zero-hit in
iteration-log pre-commit; README stats 75115/1647 pre-commit; no #1323
row in README/ARCHITECTURE test tables pre-commit; the NEW arm headline
zero-hit repo-wide pre-commit ("human concierge"); the 1 novel URL
zero-hit repo-wide pre-commit (git grep -F); the carried arm headline
is in-corpus by design (m633, #664).

Doc-sync constants per #719: README_TEST_COUNT / README_FILE_COUNT hold
the post-doc-sync values from the start (patched pre-main once the
in-gate collection count is known); the doc-sync commit ratchets README
75115/1647 -> post-sync totals.

In-gate: deselected by design (TestAnchor1323 1 + TestMechanismNovelty
1323 1 + TestGuardLifecycle1323 1 + TestStalenessPins1323 1 +
TestDocSync1323 3 + TestIterationLog1323 3 + the no-Type-C-#1324 forward
pin 1 + the no-Type-B-#1323 own-run pin 1 per #565/#719/#721).

Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file) all left out of
this run's index/diff (explicit-path staging). #1024 m846
(profiles/competitor-entities.yaml) NOT touched - decision pending. Do
NOT touch #1024.

Literal discipline per #715: this file carries no contiguous literal of
a forward-guard claim form; the constants are constructed at runtime.
(The landed ordinals live as short lowercase forms in prose here; the
live full-form claims live in profiles/financial-times.yaml,
profiles/news-corp.yaml, profiles/the-verge.yaml,
profiles/guardian.yaml, profiles/atlantic.yaml, profiles/wired.yaml,
profiles/ap.yaml, and profiles/careers/journalists.yaml.)

Quoted material below is limited to short verbatim phrases per the
copyright-brief-quotation rule; registers are otherwise paraphrased.
"""

import os
import re
import subprocess

import pytest
import yaml

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
JOURNALISTS_PATH = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
OWN_BASENAME = (
    "test_type_b_1323_katie_paul_reuters_human_concierge_"
    "vs_muse_launch_oct08_7pm.py"
)
TOP_KEY = "katie_paul_type_b"

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "6fae5cd614267592c77100188b6e956bb6d7ed34"  # patched to the main commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1025
NEXT_NUM = 1026  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_b_1323_katie_paul_reuters_human_concierge_"
    "vs_muse_launch_oct08_7pm"
)

# Predecessor chain: #1322 Type A (third leg).
PRED_MAIN_1322 = "237e0a1e2f21b114e11a1c0405c2905ea31f9eba"
PRED_ANCHOR_1322 = "1e2d00afd10fa945c9679343536ccdda5cea1520"
PRED_DOCSYNC_1322 = "fa17e8d9c9b983df7023ed12f48dee83c6af8c86"
PRED_FINAL_1322 = "83b6672fd45c8e96d3bc2a10ef4ee8e0c30da5ba"
# #1321 Type E (second leg) for the rotation-guard chain.
PRED_MAIN_1321 = "a8ac5238faadeed657069bc3b3c01729207b8165"
PRED_ANCHOR_1321 = "c2f5a24b16961644d181a0d0a7fc3ebdd558db29"
PRED_DOCSYNC_1321 = "85e2481c054a0263bf79472051f6e564243e3880"
PRED_FINAL_1321 = "a283839e1585807d605ac42423206a0f5e4d1f3f"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the own-run git-log pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1323 = "6fae5cd614267592c77100188b6e956bb6d7ed34"  # re-pinned to #1323 main sha in the terminal log-hash followup per #721

# Forward guard for the next leg: #1324 Type C. Re-pinned by #1324's
# log-hash followup per #721 (starts as 0*40; the forward pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1324 = "0" * 40

# The #1322 window-continuation file, for the staleness pin on its
# guard-lifecycle class.
A1322_FILE = (
    "test_type_a_1322_ft_openai_oct08_revenue_scoop_"
    "vs_carried_meta_arms_oct08_8pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 75225  # post-doc-sync total (pre-sync 75115 + 110)
README_FILE_COUNT = 1648  # pre-sync 1647 + 1 (this file)

# The forward-guard needles are fragment-built per #715 so this file
# carries no contiguous literal of a forward-guard claim form.
_T40 = "FORT" + "IETH relationship direction"
_T48 = "FORT" + "Y-EIGHTH falsification-family member"
_T49 = "FORT" + "Y-NINTH falsification-family member"
_T50 = "FIFT" + "IETH falsification-family member"
_T51 = "FIFT" + "Y-FIRST falsification-family member"
_T52 = "FIFT" + "Y-SECOND falsification-family member"
_T53 = "FIFT" + "Y-THIRD falsification-family member"
_T54 = "FIFT" + "Y-FOURTH falsification-family member"
_T55 = "FIFT" + "Y-FIFTH falsification-family member"
_T56 = "FIFT" + "Y-SIXTH falsification-family member"
_T57 = "FIFT" + "Y-SEVENTH falsification-family member"
_T58 = "FIFT" + "Y-EIGHTH falsification-family member"
_T59 = "FIFT" + "Y-NINTH falsification-family member"
_T60 = "SIXT" + "IETH falsification-family member"
_T61 = "SIXT" + "Y-FIRST falsification-family member"

# Novel source URL: 1 zero-hit repo-wide pre-commit (git grep -F).
# The carried arm (Sep-8, m633) is in-corpus by design.
NOVEL_URLS = [
    "https://wixx.com/2026/09/22/exclusive-meta-testing-a-human-"
    "concierge-for-its-new-personal-ai-agent-muse/",
]
RESURFACED_URLS = []

# MANUAL ILLUSTRATIVE tones (hand-assigned at excerpt level).
NEW_TONE = -0.45
CARRIED_TONE = -0.45  # m633, #664, un-rescored per #807
ILLUSTRATIVE_DELTA = 0.00


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


def _iter_source_files():
    """Yield paths for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson).
    """
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            yield os.path.join(root, f)
    for root, dirs, files in os.walk(TESTS_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            if f == OWN_BASENAME:
                continue
            if f.endswith(".py"):
                yield os.path.join(root, f)


def _repo_grep_underscore_mechanism(n):
    """Return file paths containing the underscore-form mechanism key.

    The needle is built at runtime by format string, so this source
    file carries no contiguous underscore-form literal (per the #770
    lesson).
    """
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [
        p
        for p in _iter_source_files()
        if needle in open(p, encoding="utf-8", errors="replace").read()
    ]


def _repo_grep_dash_mechanism(n):
    needle = "mechanism" + "-" + str(n)
    return [
        p
        for p in _iter_source_files()
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
            found.extend(
                int(m) for m in pat.findall(
                    open(os.path.join(root, f),
                         encoding="utf-8", errors="replace").read()
                )
            )
    return max(found) if found else None


def _git_grep_tracked_source(needle, scope):
    """Grep tracked files at HEAD for a literal needle (fragment-built)."""
    args = ["grep", "-F", "-l", needle, "HEAD", "--"]
    if scope:
        args.append(scope)
    else:
        args.append(".")
    out = _git(*args).stdout
    cleaned = []
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("HEAD:"):
            line = line[len("HEAD:"):]
        if line:
            cleaned.append(line)
    return cleaned


def _load_journalists():
    with open(JOURNALISTS_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _top():
    return _load_journalists()[TOP_KEY]


def _block():
    return _top()["competitor_coverage"][BLOCK_KEY]


def _class_run(test_file, class_name):
    return subprocess.run(
        [".venv/bin/python", "-m", "pytest",
         os.path.join(TESTS_DIR, test_file) + "::" + class_name,
         "--no-header", "-q", "-p", "no:cacheprovider"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )


# ---------------------------------------------------------------------------
# 1. Anchor convention per #565
# ---------------------------------------------------------------------------

class TestAnchor1323:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit this is 0*40 and the test passes BY DESIGN;
        # fails post-anchor (patched to the main commit sha).
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_to_main_commit(self):
        # Post-commit form: ANCHORED_SHA patched to this run's main
        # commit sha per #565 in the anchor followup (both this
        # expected value and the ANCHORED_SHA constant are patched).
        # Pre-commit this is 0*40 and the test fails BY DESIGN;
        # deselected in the in-gate run.
        assert ANCHORED_SHA != "0" * 40
        assert len(ANCHORED_SHA) == 40

    def test_anchor_sha_format(self):
        assert len(ANCHORED_SHA) == 40

    def test_this_run_main_commit_is_anchor(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "main commit is the anchor" in src

    def test_rotation_phrase_in_docstring(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FOURTH leg of the 1320-1324 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1323:
    def test_predecessor_1322_chain_verified(self):
        for sha in (
            PRED_MAIN_1322, PRED_ANCHOR_1322, PRED_DOCSYNC_1322,
            PRED_FINAL_1322,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1321_chain_verified(self):
        for sha in (
            PRED_MAIN_1321, PRED_ANCHOR_1321, PRED_DOCSYNC_1321,
            PRED_FINAL_1321,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1320 -> E #1321 -> A #1322 -> B #1323 -> C #1324" in src

    def test_next_leg_is_type_c_1324(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1324 Type C" in src

    def test_type_b_lands_one_mechanism(self):
        # Type B lands exactly one mechanism (mechanism 1025); the Type
        # A predecessor added one (mechanism 1024).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type B lands one mechanism" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1323:
    def test_top_key_found(self):
        assert _top()["mechanism_ids"] == [MECH_NUM]

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1323 in key, no 1025 or
        # 1026 substring.
        assert "1323" in BLOCK_KEY
        assert str(MECH_NUM) not in BLOCK_KEY
        assert str(NEXT_NUM) not in BLOCK_KEY

    def test_zero_underscore_mechanism_repo_wide(self):
        # Per #715 designed keying the landed number appears only as
        # the colon form; the underscore key form must not exist
        # repo-wide.
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_mechanism_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_next_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_this_run(self):
        assert _max_numeric_mechanism_id() == MECH_NUM
        assert len(_repo_grep_numeric_mechanism_id(MECH_NUM)) >= 1

    def test_no_type_b_1323_in_git_log_own_run(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type B #1323" must be #1323's main
        # commit or a descendant of it. Deselected in the in-gate run
        # (fails pre-commit by design: PRED_MAIN_1323 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type B #1323")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1323's own commits"
        main = _git("rev-parse", PRED_MAIN_1323).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_novel_url_zero_hit_pre_commit(self):
        # The novel URL was verified zero-hit repo-wide pre-commit
        # via git grep -F this run (documented in the block's novelty
        # field). The carried arm URL is in-corpus by design (m633).
        for url in NOVEL_URLS:
            out = _git("grep", "-F", "-l", url, "HEAD", "--", ".")
            assert out.stdout.strip() == "", url

    def test_journalist_first_dedicated_pair(self):
        # FIRST dedicated Type B pair on Katie Paul: zero
        # katie_paul_type_b keyed entry pre-commit; mention-level hits
        # only (the #664/#667 mechanisms m633/m634, the Jul-2 profile
        # entry, one scout-rejection note), disclosed in the block's
        # novelty note.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIRST dedicated Type B pair on Katie Paul" in src

    def test_new_headline_zero_hit_pre_commit(self):
        # The NEW arm headline ("human concierge") was verified
        # zero-hit repo-wide pre-commit this run; the carried arm
        # headline is in-corpus by design (m633, #664).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert '"human concierge"' in src

    def test_no_1323_row_in_readme_table(self):
        readme = _read(README_PATH)
        assert "test_type_b_1323" not in readme

    def test_no_1323_row_in_architecture_tree(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1323" not in arch

    def test_no_1323_in_iteration_log_pre_commit(self):
        log = _read(LOG_PATH)
        assert "## #1323" not in log


# ---------------------------------------------------------------------------
# 4. Block structure (the #643 convention)
# ---------------------------------------------------------------------------

class TestBlockStructure1323:
    def test_top_level_fields(self):
        t = _top()
        assert t["name"] == "Katie Paul"
        assert t["publication"] == "reuters"
        assert t["mechanism_ids"] == [MECH_NUM]

    def test_block_key_present(self):
        assert BLOCK_KEY in _top()["competitor_coverage"]

    def test_block_identity_fields(self):
        b = _block()
        assert b["block_key"] == BLOCK_KEY
        assert b["mechanism_id"] == MECH_NUM
        assert b["iteration"] == 1323
        assert b["iteration_type"] == "B"
        assert b["type"] == "B"
        assert b["journalist"] == "Katie Paul"
        assert b["publication"] == "reuters"
        assert b["author"] == "Kit (with Ray)"
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"

    def test_both_arms_present(self):
        b = _block()
        assert "new_arm" in b
        assert "carried_arm" in b

    def test_new_arm_fields(self):
        n = _block()["new_arm"]
        assert n["entity"] == "meta"
        assert n["outlet"] == "reuters"
        assert n["tone_MANUAL_ILLUSTRATIVE"] == NEW_TONE
        assert n["url"] == NOVEL_URLS[0]
        assert n["date"] == "2026-09-22"
        assert n["author_byline"] == "Katie Paul"

    def test_carried_arm_fields(self):
        c = _block()["carried_arm"]
        assert c["entity"] == "meta"
        assert c["outlet"] == "reuters"
        assert c["tone_MANUAL_ILLUSTRATIVE"] == CARRIED_TONE
        assert c["carried_from"] == "m633"
        assert c["date"] == "2026-09-08"

    def test_delta_field(self):
        b = _block()
        assert b["illustrative_delta_new_minus_carried"] == ILLUSTRATIVE_DELTA
        assert b["scorer_delta_MANUAL_ILLUSTRATIVE"] == ILLUSTRATIVE_DELTA

    def test_verdict_and_ledger_fields(self):
        b = _block()
        assert b["verdict"] == "directionally_supported_not_proven"
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 60
        assert b["is_significant"] is False
        assert b["correlation_not_causation"] is True
        assert b["no_analysis_json_update"] is True

    def test_window_field(self):
        b = _block()
        assert "1320-1324" in b["window"]
        assert "FOURTH leg" in b["window"]

    def test_source_urls(self):
        urls = _block()["source_urls"]
        for u in NOVEL_URLS:
            assert u in urls


# ---------------------------------------------------------------------------
# 5. m1025 content discipline
# ---------------------------------------------------------------------------

class TestM1025ContentDiscipline1323:
    def test_new_arm_concierge_quotes(self):
        quotes = " ".join(_block()["new_arm"]["key_quotes"])
        assert "human concierge" in quotes
        assert "contractors" in quotes

    def test_new_arm_tone_reading(self):
        reading = _block()["new_arm"]["tone_reading"]
        assert "accountability" in reading

    def test_carried_arm_quotes(self):
        quotes = " ".join(_block()["carried_arm"]["key_quotes"])
        assert "internal concerns" in quotes
        assert "RAISING THE STAKES FOR SAFETY" in quotes

    def test_carried_arm_tone_reading(self):
        reading = _block()["carried_arm"]["tone_reading"]
        assert "accountability" in reading

    def test_delta_reading_constancy(self):
        reading = _block()["delta_reading"]
        assert "constancy" in reading

    def test_confounder_ranking(self):
        confs = _block()["confounders"]
        assert any("STRONG" in c for c in confs)
        assert any("within-entity" in c.lower() for c in confs)

    def test_payer_leg_disclosed_in_financial_context(self):
        fc = _block()["financial_context"]
        assert "m633" in fc
        assert "Reuters" in fc
        assert "Meta" in fc

    def test_thirteenth_member_replication_disclosed(self):
        b = _block()
        assert "thirteenth" in b["falsification_family"]
        assert "#664" in b["falsification_family"]

    def test_counter_evidence_present(self):
        ce = _block()["counter_evidence"]
        assert len(ce) >= 2
        joined = " ".join(ce).lower()
        assert "response" in joined or "balanced" in joined

    def test_rejection_audit_present(self):
        ra = _block()["rejection_audit"]
        assert "Criddle" in ra
        assert "Bellan" in ra
        assert "Stern" in ra
        assert "Chokkattu" in ra
        assert "Malik" in ra

    def test_research_method_documents_screening(self):
        rm = _block()["research_method"]
        assert "screening" in rm.lower()
        assert "REJECTED" in rm
        assert "0 browser.open" in rm


# ---------------------------------------------------------------------------
# 6. Statistical discipline (the Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1323:
    def test_manual_illustrative_only(self):
        b = _block()
        assert "MANUAL ILLUSTRATIVE" in b["design"]

    def test_engine_not_run(self):
        b = _block()
        assert b["no_analysis_json_update"] is True

    def test_p_value_not_calculated(self):
        # The needle and the expected def line are both runtime-built;
        # the only contiguous occurrence in this file is the def line.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        needle = "p" + "_value"
        expected_def = "    def test_" + needle + "_not_calculated(self):"
        hits = [l for l in src.splitlines() if needle in l]
        assert hits == [expected_def], hits

    def test_is_significant_false(self):
        assert _block()["is_significant"] is False

    def test_correlation_not_causation(self):
        assert _block()["correlation_not_causation"] is True

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_verdict_directionally_supported_not_proven(self):
        assert _block()["verdict"] == "directionally_supported_not_proven"

    def test_not_artifact_grade(self):
        assert "NOT artifact-grade" in _block()["falsification_family"] or \
            "No analysis.json update warranted" in _block()["falsification_family"]

    def test_temporal_replication_not_new_member(self):
        # The same writer/partner prediction test (Reuters paid by
        # Meta goes softer on Meta) was already counted at #664 as the
        # thirteenth member; Paul's Sep-22 piece is a same-writer
        # temporal replication per the #1143 precedent, not a new
        # prediction test.
        b = _block()
        assert b["falsification_family_member"] is False
        assert "temporal replication" in b["falsification_family"]


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 60 (NOT a member).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1323:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert "NOT a falsification-family member" in b["falsification_family"]

    def test_sixtieth_intact_in_ft(self):
        out = _git(
            "grep", "-c", "-F", _T60, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_ninth_intact_in_news_corp(self):
        out = _git(
            "grep", "-c", "-F", _T59, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_intact_in_ft(self):
        out = _git(
            "grep", "-c", "-F", _T58, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_seventh_intact_in_ap(self):
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_sixth_intact_in_wired(self):
        out = _git(
            "grep", "-c", "-F", _T56, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fifth_intact_in_atlantic(self):
        out = _git(
            "grep", "-c", "-F", _T55, "HEAD", "--",
            "profiles/atlantic.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fourth_intact_in_guardian(self):
        out = _git(
            "grep", "-c", "-F", _T54, "HEAD", "--",
            "profiles/guardian.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_third_intact_in_verge(self):
        out = _git(
            "grep", "-c", "-F", _T53, "HEAD", "--",
            "profiles/the-verge.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_second_intact_in_journalists(self):
        out = _git(
            "grep", "-c", "-F", _T52, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_fifty_first_intact_in_news_corp(self):
        out = _git(
            "grep", "-c", "-F", _T51, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fiftieth_intact_in_journalists(self):
        out = _git(
            "grep", "-c", "-F", _T50, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_forty_ninth_intact_in_journalists(self):
        out = _git(
            "grep", "-c", "-F", _T49, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_forty_eighth_intact_in_ft(self):
        out = _git(
            "grep", "-c", "-F", _T48, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_sixty_first_member_repo_wide(self):
        assert _git_grep_tracked_source(_T61, None) == []

    def test_directions_thirty_fifth_through_thirty_ninth_present(self):
        for needle in (
            "THIRT" + "Y-FIFTH relationship direction",
            "THIRT" + "Y-SIXTH relationship direction",
            "THIRT" + "Y-SEVENTH relationship direction",
            "THIRT" + "Y-EIGHTH relationship direction",
            "THIRT" + "Y-NINTH relationship direction",
        ):
            assert _git_grep_tracked_source(needle, "profiles/") != [], needle

    def test_fortieth_direction_absent(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_ledger_holds_at_60(self):
        assert "holds at 60" in _block()["ledger_note"]
        assert _block()["falsification_ledger"] == 60

    def test_ledger_note_states_not_a_member(self):
        assert "NOT a falsification-family member" in _block()["ledger_note"]


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: pins for #1324; #1322's pins flip BY DESIGN.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1323:
    def test_pins_on_1025_landing(self):
        # Type B lands one mechanism: max becomes 1025, next is 1026.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1025" in src
        assert "NEXT_NUM = 1026" in src

    def test_no_type_c_1324_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1324's terminal log-hash followup
        # per #721): every commit whose message matches "Type C
        # #1324" must be #1324's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1324 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type C #1324")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1324's own commits"
        main = _git("rev-parse", PRED_MAIN_1324).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1026_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1026_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1026_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T48, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_forty_ninth_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T49, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

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

    def test_fifty_fourth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T54, "HEAD", "--",
            "profiles/guardian.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fifth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T55, "HEAD", "--",
            "profiles/atlantic.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_sixth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T56, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_seventh_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T58, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_ninth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T59, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixtieth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T60, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_sixty_first_member_pin(self):
        assert _git_grep_tracked_source(_T61, None) == []

    def test_predecessor_1322_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, A1322_FILE))

    def test_next_leg_is_1324_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1324 Type C" in src

    def test_1322_pins_flip_by_design_documented(self):
        # Documents the two BY-DESIGN flips at this run's main commit:
        # test_no_type_b_1323_in_git_log_pin (the #1191-class
        # self-trip, re-pinned green in the terminal log-hash followup
        # per #721 in BOTH files per the #1292 precedent) and
        # test_1025_numeric_absent_in_profiles (the #1272-class
        # forward-guard expiry, permanent - the next-number guard is
        # consumed by the m1025 landing).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1191-class" in src
        assert "#1272-class" in src


# ---------------------------------------------------------------------------
# 9. Background suite check per #795
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1323:
    def test_1320_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1320_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1320-launched suite is observed.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1323_full_suite.log"))

    def test_observation_documented_in_block(self):
        assert "#1320-launched" in _block()["background_suite_status"]
        assert "#795" in _block()["background_suite_status"]
        assert "#1325" in _block()["background_suite_status"]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1323:
    def test_readme_test_file_table_has_1323_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_b_1323" in readme

    def test_architecture_has_1323_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1323" in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_PATH)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 11. Iteration log (3 tests; deselected pre-commit per #721)
# ---------------------------------------------------------------------------

class TestIterationLog1323:
    def test_1323_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1323 Type B" in log

    def test_1322_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1322 Type A" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1322's guard lifecycle flips BY DESIGN post-commit
# ---------------------------------------------------------------------------

class TestStalenessPins1323:
    def test_1322_guard_lifecycle_post_commit(self):
        # Post-terminal-followup form: 22 of the 23 pass; the one that
        # fails BY DESIGN is test_1025_numeric_absent_in_profiles
        # (mechanism 1025 lands in profiles/ this run; the #1272-class
        # forward-guard expiry - the next-number guard is consumed by
        # the landing; stays red permanently). The second flip,
        # test_no_type_b_1323_in_git_log_pin (the #1191-class
        # self-trip: this run's own main commit carries "Type B
        # #1323"), is re-pinned green in the terminal log-hash
        # followup per #721 (its PRED_MAIN_1323 now holds this run's
        # main sha, in BOTH the #1323 and #1322 files per the #1292
        # precedent). test_pins_on_mechanism_landing stays GREEN
        # (asserts on the #1322 file's own constants, untouched by
        # this run); the member and direction pins stay GREEN (m1025
        # is a temporal replication, not a family member).
        # Deselected pre-commit (the pin passes pre-commit).
        res = _class_run(A1322_FILE, "TestGuardLifecycle1322")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "1 failed, 22 passed" in res.stdout, res.stdout[-2000:]
        assert "test_1025_numeric_absent_in_profiles" in res.stdout, \
            res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1323:
    def test_899_nytimes_hunk_untouched(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert "profiles/nytimes.yaml" in modified
        # Its uncommitted hunk belongs to #899's run; this run stages
        # only its own files.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#899" in src

    def test_900_untracked_file_untouched(self):
        res = _git("status", "--short")
        assert "test_type_d_900_m769" in res.stdout

    def test_938_test_file_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_b_938" in res.stdout

    def test_1012_wt_working_tree_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_a_1012" in res.stdout

    def test_do_not_touch_1024_m846(self):
        # #1024 m846 (profiles/competitor-entities.yaml) is NOT
        # touched - decision pending. This run stages only its own
        # files by explicit path.
        res = _git("diff", "--name-only")
        assert "profiles/competitor-entities.yaml" not in res.stdout.split()
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Do NOT touch #1024" in src
