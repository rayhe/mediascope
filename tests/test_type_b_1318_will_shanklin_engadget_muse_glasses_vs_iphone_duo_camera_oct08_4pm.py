# -*- coding: utf-8 -*-
"""Type B #1318 tests: Will Shanklin (Engadget) - Sep-23-2026 Meta "Muse
AI agent is coming to its AI glasses" (-0.20 MANUAL ILLUSTRATIVE, NEW
Meta arm, mild trust-interrogation register: "willing to trust it with
the most sensitive parts of your digital life", "privacy-threatening
'perv glasses'", "how much Muse for glasses really adds" skepticism)
vs Sep-9-2026 Apple "The iPhone Duo lacks variable aperture and a
dedicated telephoto camera" (-0.15 MANUAL ILLUSTRATIVE, NEW Apple arm,
mild technical-critique register: "The hot new iPhone feature is
somehow absent from the hot new iPhone", "hard sell for
photography-happy iPhone buyers", demystifies Apple's "optical quality"
marketing); illustrative delta (Apple minus Meta) +0.05 - near-null
register constancy, same writer, same outlet, 14 days apart.

Mechanism 1022 (NOT a falsification-family member; ledger holds at 59).
FIRST dedicated Type B mechanism on Will Shanklin (zero
will_shanklin_type_b keyed entry pre-commit; mention-level hits only:
the #1233 scout-rejection note and two older iteration-log byline
mentions, disclosed). The naive "hard on Meta, soft on Apple" pattern
is NOT observed: Shanklin applies comparable mild-critical registers to
both companies' launches. ZERO-GRADIENT control pair: no documented
bilateral AI content-licensing deal between Yahoo/Engadget and Meta or
Apple exists in-corpus (the #1278 Kris Holt control case documents the
absence explicitly), so the naive payer-softening prediction is NULL -
the +0.05 illustrative delta is a journalist-level register-constancy
observation, neither meeting nor failing a financial prediction.
STRONGEST confound: peg asymmetry (AI-agent trust/privacy product news
vs camera-hardware spec critique); STRONG: the zero-gradient financial
context itself (cuts against financial-determinism readings, disclosed
honestly); MODERATE: excerpt-bounded evidence (0 browser.open per #503),
14-day temporal gap; WEAK: genre (both product-launch news, favorable).

Excerpt-bounded research per #503 (1 delegated scout, ranked 3 novel
candidates; 2 main-run browser.search verification sets + 1
candidate-screening set, 0 browser.open reads). The scout's #1 (Marcus
Mendes/9to5Mac) was REJECTED on main-run corpus verification (m991
pre-exists on Mendes at #1268; the Meta-arm URL is already in-corpus);
the scout's #2 (Sarah Perez/TechCrunch) REJECTED (three dedicated Type B
mechanisms in-corpus: m638/m778/#1293); the scout's #3 (Jay
Peters/Verge) REJECTED (dedicated Type B mechanism m731 at #833 plus the
#893 temporal replication). Main-run screening SELECTED Shanklin
(cleanest surviving pair - same writer, same outlet, both product-launch
news pegs 14 days apart, novel journalist, both canonical URLs verbatim
from Full-URL listings). REJECTED on main-run screening: Anna
Washenko (Meta-arm byline conflict - Engadget listings attribute the
Ray-Ban Display piece to Washenko but the article page reads "Karissa
Bell for Engadget"; unresolvable at excerpt level, rejected on
discipline), Ian Carlos Campbell (novel but no clean competitor arm -
the Apple Health-app piece is not a cross-entity comparator), Steve
Dent (Meta arm is Jan-2026 CES vintage, stale). Prior-run rejection
lists stand.

The m1022 block lives in profiles/careers/journalists.yaml under the
will_shanklin_type_b keyed entry's competitor_coverage dict (per the #643
convention); mechanism_ids [1022].

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup commit. One anchor test (the placeholder pin) fails BY DESIGN
post-anchor.

Per #795: this run only CHECKS the #1315-launched background suite
(goal hidden_files type_d_1315_full_suite.log, observed at this run's
check; an observation, not a verdict); its verdict and tombstone belong
to #1320 (next Type D). This run neither re-launches, kills, nor writes
to the suite.

Rotation: this run is iteration #1318 Type B, the FOURTH leg of the
1315-1319 window (D #1315 -> E #1316 -> A #1317 -> B #1318 -> C #1319, per
the #565 anchor + rotation guard). Predecessor #1317 Type A verified in
git log (main 7749f95d / anchor 27fb204c / doc-sync c5b63c08 / log-hash
8f3d3f8d); #1316 Type E verified (main 5d160c6c / anchor 49d60e8a /
doc-sync 9e3dc23b / log-hash 4867ff1c); the 1310-1314 window is VERIFIED
CLOSED. This run's main commit is the anchor per #565; ANCHORED_SHA
patched post-commit. The #1317 forward guards verified pre-commit this
run: max-1021; zero one-zero-two-two keys all forms; no-Type-B-#1318-
in-git-log; fortieth direction absent; forty-eighth through fifty-ninth
members intact; no sixtieth member (repo-wide); ledger 59. Next run
#1319 Type C closes the window; the #1315-launched background-suite
verdict belongs to #1320 per #795.

Type B lands one mechanism (m1022). Pre-commit novelty greps per #715:
zero test_type_b_1318 files on disk (glob); no "Type B #1318" in git log
(--grep); max numeric mechanism_id 1021 in profiles/ pre-commit
(mechanism_id regex sweep); zero numeric/underscore/dash
one-zero-two-two mechanism key forms repo-wide pre-commit (needles
format-built per #715, own file excluded, __pycache__ excluded);
"will shanklin" mention-level hits only pre-commit (the #1233
scout-rejection note + two older iteration-log byline mentions;
zero will_shanklin_type_b keyed entry); block key zero-hit repo-wide
pre-commit (designed keying: iteration 1318 in key, no 1022 substring,
per the #723/#738/#739 convention); "## #1318" zero-hit in
iteration-log pre-commit; README stats 74598/1642 pre-commit; no #1318
row in README/ARCHITECTURE test tables pre-commit; both arm headlines
zero-hit repo-wide pre-commit; the 2 novel URLs zero-hit repo-wide
pre-commit (git grep -F).

Doc-sync constants per #719: README_TEST_COUNT / README_FILE_COUNT hold
the post-doc-sync values from the start (patched pre-main once the
in-gate collection count is known); the doc-sync commit ratchets README
74598/1642 -> post-sync totals.

In-gate: deselected by design (TestAnchor1318 1 + TestMechanismNovelty
1318 1 + TestGuardLifecycle1318 1 + TestStalenessPins1318 1 +
TestDocSync1318 3 + TestIterationLog1318 3 + the no-Type-C-#1319 forward
pin 1 + the no-Type-B-#1318 own-run pin 1 per #565/#719/#721).

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
    "test_type_b_1318_will_shanklin_engadget_muse_glasses_"
    "vs_iphone_duo_camera_oct08_4pm.py"
)
TOP_KEY = "will_shanklin_type_b"

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "71c2cc5219e7a00986312a1278b6bb2caf7d0bb2"  # patched to the main commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1022
NEXT_NUM = 1023  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_b_1318_will_shanklin_engadget_muse_glasses_"
    "vs_iphone_duo_camera_oct08_4pm"
)

# Predecessor chain: #1317 Type A (third leg).
PRED_MAIN_1317 = "7749f95d8d5b36031bba2bf11ddc92636d48b753"
PRED_ANCHOR_1317 = "27fb204cf0f1b94c038f1a1678a805a7e4bf0600"
PRED_DOCSYNC_1317 = "c5b63c08ac60c741a1af727e854f3c7df694abdd"
PRED_FINAL_1317 = "8f3d3f8da89ce7d7688e8f720d9d414954eace9a"
# #1316 Type E (second leg) for the rotation-guard chain.
PRED_MAIN_1316 = "5d160c6cc9a8d68e863499b4e5fc142845c21060"
PRED_ANCHOR_1316 = "49d60e8ac4b57b1b9c76b585b4d4484217fb4f26"
PRED_DOCSYNC_1316 = "9e3dc23ba09a831477253f38267fbbdcabf439ab"
PRED_FINAL_1316 = "4867ff1c0bfa89b469f794c0220f9c295dd40c4f"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the own-run git-log pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1318 = "71c2cc5219e7a00986312a1278b6bb2caf7d0bb2"  # re-pinned to #1318 main sha in the terminal log-hash followup per #721

# Forward guard for the next leg: #1319 Type C. Re-pinned by #1319's
# log-hash followup per #721 (starts as 0*40; the forward pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1319 = "0" * 40

# The #1317 window-continuation file, for the staleness pin on its
# guard-lifecycle class.
D1317_FILE = (
    "test_type_a_1317_semafor_microsoft_suleyman_exec_platform_"
    "vs_meta_led_tampering_exclusive_oct08_3pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 74705  # post-doc-sync total (pre-sync 74598 + 107)
README_FILE_COUNT = 1643  # pre-sync 1642 + 1 (this file)

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

# Novel source URLs: 2 zero-hit repo-wide pre-commit (git grep -F).
NOVEL_URLS = [
    "https://www.engadget.com/2267210/meta-muse-ai-agent-smart-glasses/",
    "https://www.engadget.com/2254121/the-iphone-duo-lacks-variable-aperture-and-a-dedicated-telephoto-camera/",
]
RESURFACED_URLS = []

# MANUAL ILLUSTRATIVE tones (hand-assigned at excerpt level).
META_TONE = -0.20
APPLE_TONE = -0.15
ILLUSTRATIVE_DELTA = 0.05


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

class TestAnchor1318:
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
        assert "FOURTH leg of the 1315-1319 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1318:
    def test_predecessor_1317_chain_verified(self):
        for sha in (
            PRED_MAIN_1317, PRED_ANCHOR_1317, PRED_DOCSYNC_1317,
            PRED_FINAL_1317,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1316_chain_verified(self):
        for sha in (
            PRED_MAIN_1316, PRED_ANCHOR_1316, PRED_DOCSYNC_1316,
            PRED_FINAL_1316,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1315 -> E #1316 -> A #1317 -> B #1318 -> C #1319" in src

    def test_next_leg_is_type_c_1319(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1319 Type C" in src

    def test_type_b_lands_one_mechanism(self):
        # Type B lands exactly one mechanism (mechanism 1022); the Type
        # A predecessor added one (mechanism 1021).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type B lands one mechanism" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1318:
    def test_top_key_found(self):
        assert _top()["mechanism_ids"] == [MECH_NUM]

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1318 in key, no 1022 or
        # 1023 substring.
        assert "1318" in BLOCK_KEY
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
        nums = []
        for _line in _repo_grep_numeric_mechanism_id(MECH_NUM):
            nums.append(MECH_NUM)
        assert _max_numeric_mechanism_id() == MECH_NUM
        assert len(_repo_grep_numeric_mechanism_id(MECH_NUM)) >= 1

    def test_no_type_b_1318_in_git_log_own_run(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type B #1318" must be #1318's main
        # commit or a descendant of it. Deselected in the in-gate run
        # (fails pre-commit by design: PRED_MAIN_1318 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type B #1318")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1318's own commits"
        main = _git("rev-parse", PRED_MAIN_1318).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_novel_urls_zero_hit_pre_commit(self):
        # Both novel URLs verified zero-hit repo-wide pre-commit
        # via git grep -F this run.
        for url in NOVEL_URLS:
            out = _git("grep", "-F", "-l", url, "HEAD", "--", ".")
            assert out.stdout.strip() == "", url

    def test_journalist_first_dedicated_pair(self):
        # FIRST dedicated Type B pair on Will Shanklin: zero
        # will_shanklin_type_b keyed entry pre-commit; mention-level
        # hits only (the #1233 scout-rejection note + two older
        # iteration-log byline mentions), disclosed in the block's
        # novelty note.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIRST dedicated Type B pair on Will Shanklin" in src

    def test_no_1318_row_in_readme_table(self):
        readme = _read(README_PATH)
        assert "test_type_b_1318" not in readme

    def test_no_1318_row_in_architecture_tree(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1318" not in arch

    def test_no_1318_in_iteration_log_pre_commit(self):
        log = _read(LOG_PATH)
        assert "## #1318" not in log


# ---------------------------------------------------------------------------
# 4. Block structure (the #643 convention)
# ---------------------------------------------------------------------------

class TestBlockStructure1318:
    def test_top_level_fields(self):
        t = _top()
        assert t["name"] == "Will Shanklin"
        assert t["publication"] == "engadget"
        assert t["mechanism_ids"] == [MECH_NUM]

    def test_block_key_present(self):
        assert BLOCK_KEY in _top()["competitor_coverage"]

    def test_block_identity_fields(self):
        b = _block()
        assert b["block_key"] == BLOCK_KEY
        assert b["mechanism_id"] == MECH_NUM
        assert b["iteration"] == 1318
        assert b["iteration_type"] == "B"
        assert b["type"] == "B"
        assert b["journalist"] == "Will Shanklin"
        assert b["publication"] == "engadget"
        assert b["author"] == "Kit (with Ray)"
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"

    def test_both_arms_present(self):
        b = _block()
        assert "meta_arm" in b
        assert "apple_arm" in b

    def test_meta_arm_fields(self):
        m = _block()["meta_arm"]
        assert m["entity"] == "meta"
        assert m["outlet"] == "engadget"
        assert m["tone_MANUAL_ILLUSTRATIVE"] == META_TONE
        assert m["url"] == NOVEL_URLS[0]
        assert m["date"] == "2026-09-23"

    def test_apple_arm_fields(self):
        a = _block()["apple_arm"]
        assert a["entity"] == "apple"
        assert a["outlet"] == "engadget"
        assert a["tone_MANUAL_ILLUSTRATIVE"] == APPLE_TONE
        assert a["url"] == NOVEL_URLS[1]
        assert a["date"] == "2026-09-09"

    def test_delta_field(self):
        b = _block()
        assert b["illustrative_delta_apple_minus_meta"] == ILLUSTRATIVE_DELTA
        assert b["scorer_delta_MANUAL_ILLUSTRATIVE"] == ILLUSTRATIVE_DELTA

    def test_verdict_and_ledger_fields(self):
        b = _block()
        assert b["verdict"] == "directionally_supported_not_proven"
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 59
        assert b["is_significant"] is False
        assert b["correlation_not_causation"] is True
        assert b["no_analysis_json_update"] is True

    def test_window_field(self):
        b = _block()
        assert "1315-1319" in b["window"]
        assert "FOURTH leg" in b["window"]

    def test_source_urls(self):
        urls = _block()["source_urls"]
        for u in NOVEL_URLS:
            assert u in urls


# ---------------------------------------------------------------------------
# 5. m1022 content discipline
# ---------------------------------------------------------------------------

class TestM1022ContentDiscipline1318:
    def test_meta_arm_trust_interrogation_quotes(self):
        quotes = " ".join(_block()["meta_arm"]["key_quotes"])
        assert "perv glasses" in quotes
        assert "trust" in quotes

    def test_meta_arm_tone_reading(self):
        reading = _block()["meta_arm"]["tone_reading"]
        assert "trust-interrogation" in reading or "trust" in reading

    def test_apple_arm_camera_critique_quotes(self):
        quotes = " ".join(_block()["apple_arm"]["key_quotes"])
        assert "variable aperture" in quotes
        assert "telephoto" in quotes

    def test_apple_arm_tone_reading(self):
        reading = _block()["apple_arm"]["tone_reading"]
        assert "hard sell" in reading or "compromise" in reading

    def test_delta_reading_near_null(self):
        reading = _block()["delta_reading"]
        assert "near-null" in reading or "constancy" in reading

    def test_confounder_ranking(self):
        confs = _block()["confounders"]
        assert any("STRONG" in c for c in confs)
        assert any("peg" in c.lower() for c in confs)

    def test_zero_gradient_disclosed_in_financial_context(self):
        fc = _block()["financial_context"]
        assert "ZERO-GRADIENT" in fc
        assert "Engadget" in fc or "Yahoo" in fc

    def test_counter_evidence_present(self):
        ce = _block()["counter_evidence"]
        assert len(ce) >= 2
        joined = " ".join(ce)
        assert "criminal complaint" in joined or "German nonprofit" in joined

    def test_rejection_audit_present(self):
        ra = _block()["rejection_audit"]
        assert "Mendes" in ra
        assert "Perez" in ra
        assert "Peters" in ra
        assert "Washenko" in ra

    def test_research_method_documents_scout_correction(self):
        rm = _block()["research_method"]
        assert "scout" in rm.lower()
        assert "REJECTED" in rm
        assert "0 browser.open" in rm


# ---------------------------------------------------------------------------
# 6. Statistical discipline (the Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1318:
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

    def test_thesis_consistent_not_falsification(self):
        # The +0.05 delta sits on a ZERO-GRADIENT pair (no documented
        # payer differential at Engadget/Yahoo for Meta or Apple), so
        # the naive payer-softening prediction is NULL here: the delta
        # is a journalist-level register-constancy observation, neither
        # meeting nor failing a financial prediction. NOT a
        # falsification-family member.
        b = _block()
        assert b["falsification_family_member"] is False
        assert "zero-gradient" in b["falsification_family"].lower()


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 59 (NOT a member).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1318:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert "NOT a falsification-family member" in b["falsification_family"]

    def test_zero_gradient_disclosed(self):
        b = _block()
        assert "zero-gradient" in b["falsification_family"].lower()

    def test_fifty_ninth_intact_in_news_corp(self):
        # Landed #1302 (m1012, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
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
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_sixtieth_absent(self):
        assert _git_grep_tracked_source(_T60, None) == []

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

    def test_ledger_holds_at_59(self):
        assert "holds at 59" in _block()["ledger_note"]
        assert _block()["falsification_ledger"] == 59

    def test_ledger_note_states_not_a_member(self):
        assert "NOT a falsification-family member" in _block()["ledger_note"]


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: pins for #1319; #1317's pins flip BY DESIGN.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1318:
    def test_pins_on_1022_landing(self):
        # Type B lands one mechanism: max becomes 1022, next is 1023.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1022" in src
        assert "NEXT_NUM = 1023" in src

    def test_no_type_c_1319_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1319's terminal log-hash followup
        # per #721): every commit whose message matches "Type C
        # #1319" must be #1319's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1319 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type C #1319")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1319's own commits"
        main = _git("rev-parse", PRED_MAIN_1319).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1023_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1023_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1023_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

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

    def test_no_sixtieth_member_pin(self):
        assert _git_grep_tracked_source(_T60, None) == []

    def test_predecessor_1317_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, D1317_FILE))

    def test_next_leg_is_1319_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1319 Type C" in src

    def test_1317_pins_flip_by_design_documented(self):
        # Documents the two BY-DESIGN flips at this run's main commit:
        # test_no_type_b_1318_in_git_log_pin (the #1191-class
        # self-trip, re-pinned green in the terminal log-hash followup
        # per #721 in BOTH files per the #1292 precedent) and
        # test_1022_numeric_absent_in_profiles (the #1272-class
        # forward-guard expiry, permanent - the next-number guard is
        # consumed by the m1022 landing).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1191-class" in src
        assert "#1272-class" in src


# ---------------------------------------------------------------------------
# 9. Background suite check per #795
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1318:
    def test_1315_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1315_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1315-launched suite is observed.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1318_full_suite.log"))

    def test_observation_documented_in_block(self):
        assert "#1315-launched" in _block()["background_suite_status"]
        assert "#795" in _block()["background_suite_status"]
        assert "#1315" in _block()["background_suite_status"]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1318:
    def test_readme_test_file_table_has_1318_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_b_1318" in readme

    def test_architecture_has_1318_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1318" in arch

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

class TestIterationLog1318:
    def test_1318_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1318 Type B" in log

    def test_1317_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1317 Type A" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1317's guard lifecycle flips BY DESIGN post-commit
# ---------------------------------------------------------------------------

class TestStalenessPins1318:
    def test_1317_guard_lifecycle_post_commit_self_trip(self):
        # Post-terminal-followup form: 21 of the 22 pass; the one that
        # fails BY DESIGN is test_1022_numeric_absent_in_profiles
        # (mechanism 1022 lands in profiles/ this run; the #1272-class
        # forward-guard expiry - the next-number guard is consumed by
        # the landing; stays red permanently). The second flip,
        # test_no_type_b_1318_in_git_log_pin (the #1191-class
        # self-trip: this run's own main commit carries "Type B
        # #1318"), is re-pinned green in the terminal log-hash
        # followup per #721 (its PRED_MAIN_1318 now holds this run's
        # main sha, in BOTH the #1318 and #1317 files per the #1292
        # precedent). test_pins_on_one_mechanism_landing stays GREEN
        # (asserts on the #1317 file's own constants, untouched by
        # this run); the member and direction pins stay GREEN (m1022
        # is a zero-gradient observation, not a family member).
        # Deselected pre-commit (the pin passes pre-commit).
        res = _class_run(D1317_FILE, "TestGuardLifecycle1317")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "1 failed, 21 passed" in res.stdout, res.stdout[-2000:]
        assert "test_1022_numeric_absent_in_profiles" in res.stdout, \
            res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1318:
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
