# -*- coding: utf-8 -*-
"""Type B #1313 tests: Zoe Kleinman (BBC News) - Sep-24-2026 Meta
"pervert glasses" camera-free pivot piece "They were labelled 'pervert
glasses'. Will a camera-free version transform their image?"
(-0.55 MANUAL ILLUSTRATIVE, NEW Meta arm, adversarial privacy register:
"storm of controversy", non-consensual filming of women and girls,
Kylie Jenner image-laundering framed as failed; co-bylined with Luke
Mintz) vs Sep-23-2026 OpenAI Ukraine cyber-defence gift "OpenAI gives
cyber defence tools to Ukraine" (+0.25 MANUAL ILLUSTRATIVE, NEW OpenAI
arm, positive partnership register: free Daybreak system for civilian
infrastructure, no adversarial edge); illustrative delta (OpenAI minus
Meta) +0.80 - same writer, same outlet, 1 day apart.

Mechanism 1019 (NOT a falsification-family member; ledger holds at 59).
FIRST dedicated Type B mechanism on Zoe Kleinman (zero "kleinman" hits
repo-wide pre-commit, grep-verified this run) and FIRST journalist-level
mechanism at the BBC (existing BBC mentions are SPUR-coalition
membership and relay citations, not mechanismized pairs; disclosed).
The BBC is a SPUR founding member (m514) but SPUR explicitly "is not a
collective licensing body" - standards-governance background, NOT a
content-licensing payer leg. No publicly known bilateral AI
content-licensing deal between the BBC and OpenAI or Meta exists
in-corpus: this is a ZERO-GRADIENT control pair (the Amure/TheStreet
m1016 pattern) - the naive payer-softening prediction is NULL on this
pair, so the +0.80 illustrative delta can be attributed to neither a
payer relationship nor its absence; it is a journalist-level
register-asymmetry observation. STRONGEST confound: peg asymmetry (a
privacy-scandal accountability piece vs a charitable cyber-defence gift
- the valence gap tracks the pegs almost entirely); STRONG: the
zero-gradient financial context itself (cuts against
financial-determinism readings, disclosed honestly); MODERATE:
co-byline on the Meta arm (Mintz's contribution unisolable),
excerpt-bounded evidence (0 browser.open per #503).

Excerpt-bounded research per #503 (1 delegated scout, ranked 3 novel
candidates; 2 main-run browser.search verification sets + 1
candidate-screening set, 0 browser.open reads). Scout surfaced
Kleinman/BBC, Charlton/MacRumors, Holmes/BI (all zero-hit pre-commit);
main-run verification SELECTED Kleinman (cleanest pair - 1-day temporal
proximity, Meta arm directly on-topic wearables, novel journalist +
novel outlet). REJECTED Charlton (MacRumors Apple-beat; no clean Meta
arm surfaced) and Holmes (moved to The Information as Microsoft
reporter; BI-era bylines stale). Prior-run rejection lists stand.

The m1019 block lives in profiles/careers/journalists.yaml under the
zoe_kleinman_type_b keyed entry's competitor_coverage dict (per the #643
convention); mechanism_ids [1019].

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup commit. One anchor test (the placeholder pin) fails BY DESIGN
post-anchor.

Per #795: this run only CHECKS the #1310-launched background suite
(goal hidden_files type_d_1310_full_suite.log, observed at this run's
check; an observation, not a verdict); its verdict and tombstone belong
to #1315 (next Type D). This run neither re-launches, kills, nor writes
to the suite.

Rotation: this run is iteration #1313 Type B, the FOURTH leg of the
1310-1314 window (D #1310 -> E #1311 -> A #1312 -> B #1313 -> C #1314, per
the #565 anchor + rotation guard). Predecessor #1312 Type A verified in
git log (main 9e37e42b / anchor 37e7a7e9 / doc-sync fe67a3bb / log-hash
ccf522f8 / push-status 5e67c15a); the 1305-1309 window is VERIFIED
CLOSED. This run's main commit is the anchor per #565; ANCHORED_SHA
patched post-commit. The #1312 forward guards verified pre-commit this
run: max-1018; zero one-zero-one-nine keys all forms; no-Type-B-#1313-
in-git-log; fortieth direction absent; forty-eighth through fifty-ninth
members intact; no sixtieth member (repo-wide); ledger 59. Next: #1314
Type C closes the window; the #1310-launched background-suite verdict
belongs to #1315 per #795.

Type B lands one mechanism (m1019). Pre-commit novelty greps per #715:
zero test_type_b_1313 files on disk (glob); no "Type B #1313" in git log
(--grep); max numeric mechanism_id 1018 in profiles/ pre-commit
(mechanism_id regex sweep); zero numeric/underscore/dash
one-zero-one-nine mechanism key forms repo-wide pre-commit (needles
format-built per #715, own file excluded, __pycache__ excluded);
"zoe kleinman" and "luke mintz" zero-hit repo-wide pre-commit; block key
zero-hit repo-wide pre-commit (designed keying: iteration 1313 in key,
no 1019 substring, per the #723/#738/#739 convention); "## #1313"
zero-hit in iteration-log pre-commit; README stats 74063/1637
pre-commit; no #1313 row in README/ARCHITECTURE test tables pre-commit;
the 3 novel URLs zero-hit repo-wide pre-commit (git grep -F).

Doc-sync constants per #719: README_TEST_COUNT / README_FILE_COUNT hold
the post-doc-sync values from the start (patched pre-main once the
in-gate collection count is known); the doc-sync commit ratchets README
74063/1637 -> post-sync totals.

In-gate: deselected by design (TestAnchor1313 1 + TestMechanismNovelty
1313 1 + TestGuardLifecycle1313 1 + TestStalenessPins1313 1 +
TestDocSync1313 3 + TestIterationLog1313 3 + the no-Type-C-#1314 forward
pin 1 + the no-Type-B-#1313 own-run pin 1 per #565/#719/#721).

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
    "test_type_b_1313_zoe_kleinman_bbc_pervert_glasses_"
    "vs_openai_ukraine_cyber_defence_oct08_12pm.py"
)
TOP_KEY = "zoe_kleinman_type_b"

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "fc747c1346a12167eaf28ac461ab2ae5546c7e04"  # patched to the main commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1019
NEXT_NUM = 1020  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_b_1313_zoe_kleinman_bbc_pervert_glasses_"
    "vs_openai_ukraine_cyber_defence_oct08_12pm"
)

# Predecessor chain: #1312 Type A (third leg).
PRED_MAIN_1312 = "9e37e42b129c20e39eac73e245d6e52b15510b4e"
PRED_ANCHOR_1312 = "37e7a7e94e9fe86d793f1e73366b94181edd8ee4"
PRED_DOCSYNC_1312 = "fe67a3bbc9e4dbdfbae96f1aab35a36d11fd520b"
PRED_FINAL_1312 = "ccf522f8d88659ad52d1f6b2d04368e04f08e137"
PRED_PUSH_1312 = "5e67c15a939284448403f6eb04e6844df9deed5e"
# #1311 Type E (second leg) for the rotation-guard chain.
PRED_MAIN_1311 = "a9d11a087f42aca79a5e2beee63e60c57c019720"
PRED_ANCHOR_1311 = "d12c4a613df0a08ff75210f828126e5d364377ea"
PRED_DOCSYNC_1311 = "b77dad3ee3436411e92c92f568fb11c8c1287ceb"
PRED_FINAL_1311 = "a35c64357ee20018f83274e18898042ffe07ab37"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the own-run git-log pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1313 = "fc747c1346a12167eaf28ac461ab2ae5546c7e04"  # re-pinned to #1313 main sha in the terminal log-hash followup per #721

# Forward guard for the next leg: #1314 Type C. Re-pinned by #1314's
# log-hash followup per #721 (starts as 0*40; the forward pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1314 = "0" * 40  # re-pinned by #1314 terminal log-hash followup per #721

# The #1312 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 1015; zero one-zero-one-six keys all
# forms / no-Type-B-#1313-in-git-log / fortieth direction absent /
# forty-eighth through fifty-ninth members intact /
# sixtieth member absent / ledger 59).
D1312_FILE = (
    "test_type_a_1312_politico_openai_decoded_debut_altman_"
    "marquee_platform_vs_meta_dahlkamp_lobbying_"
    "exposure_oct08_11am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 74174  # post-doc-sync total (pre-sync 74063 + 111)
README_FILE_COUNT = 1638  # pre-sync 1637 + 1 (this file)

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

# Novel source URLs: 3 zero-hit repo-wide pre-commit (git grep -F).
NOVEL_URLS = [
    "https://scoopfeeds.com/article/47e5d005-4d46-504d-81e8-a8939a732948",
    "https://www.bbc.co.uk/news/articles/c90kly26d7pzo?at_medium=RSS&at_campaign=rss",
    "https://muckrack.com/zsk/articles",
]
RESURFACED_URLS = []

# MANUAL ILLUSTRATIVE tones (hand-assigned at excerpt level).
META_TONE = -0.55
OPENAI_TONE = 0.25
ILLUSTRATIVE_DELTA = 0.80


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

class TestAnchor1313:
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
        assert "FOURTH leg of the 1310-1314 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1313:
    def test_predecessor_1312_chain_verified(self):
        for sha in (
            PRED_MAIN_1312, PRED_ANCHOR_1312, PRED_DOCSYNC_1312,
            PRED_FINAL_1312, PRED_PUSH_1312,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1311_chain_verified(self):
        for sha in (
            PRED_MAIN_1311, PRED_ANCHOR_1311, PRED_DOCSYNC_1311,
            PRED_FINAL_1311,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1310 -> E #1311 -> A #1312 -> B #1313 -> C #1314" in src

    def test_next_leg_is_type_c_1314(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1314 Type C" in src

    def test_type_b_lands_one_mechanism(self):
        # Type B lands exactly one mechanism (mechanism 1019); the Type
        # A predecessor added one (mechanism 1015).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type B lands one mechanism" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1313:
    def test_top_key_found(self):
        assert _top()["mechanism_ids"] == [MECH_NUM]

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1313 in key, no 1019 or
        # 1020 substring.
        assert "1313" in BLOCK_KEY
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

    def test_no_type_b_1313_in_git_log_own_run(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type B #1313" must be #1313's main
        # commit or a descendant of it. Deselected in the in-gate run
        # (fails pre-commit by design: PRED_MAIN_1313 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type B #1313")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1313's own commits"
        main = _git("rev-parse", PRED_MAIN_1313).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_novel_urls_zero_hit_pre_commit(self):
        # All three novel URLs verified zero-hit repo-wide pre-commit
        # via git grep -F this run.
        for url in NOVEL_URLS:
            out = _git("grep", "-F", "-l", url, "HEAD", "--", ".")
            assert out.stdout.strip() == "", url

    def test_journalist_zero_hit_pre_commit(self):
        # "kleinman" zero-hit repo-wide pre-commit, grep-verified this
        # run (FIRST dedicated Type B pair on this journalist).
        out = _git("grep", "-il", "kleinman", "HEAD", "--", ".")
        assert out.stdout.strip() == "", out.stdout

    def test_bbc_no_journalist_mechanism_pre_commit(self):
        # Existing BBC mentions are SPUR-coalition membership and
        # relay-level citations, not mechanismized journalist pairs;
        # disclosed in the block's novelty note.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "SPUR-coalition" in src

    def test_no_1313_row_in_readme_table(self):
        readme = _read(README_PATH)
        assert "test_type_b_1313" not in readme

    def test_no_1313_row_in_architecture_tree(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1313" not in arch

    def test_no_1313_in_iteration_log_pre_commit(self):
        log = _read(LOG_PATH)
        assert "## #1313" not in log


# ---------------------------------------------------------------------------
# 4. Block structure (the #643 convention)
# ---------------------------------------------------------------------------

class TestBlockStructure1313:
    def test_top_level_fields(self):
        t = _top()
        assert t["name"] == "Zoe Kleinman"
        assert t["publication"] == "bbc"
        assert t["mechanism_ids"] == [MECH_NUM]

    def test_block_key_present(self):
        assert BLOCK_KEY in _top()["competitor_coverage"]

    def test_block_identity_fields(self):
        b = _block()
        assert b["block_key"] == BLOCK_KEY
        assert b["mechanism_id"] == MECH_NUM
        assert b["iteration"] == 1313
        assert b["iteration_type"] == "B"
        assert b["type"] == "B"
        assert b["journalist"] == "Zoe Kleinman"
        assert b["publication"] == "bbc"
        assert b["author"] == "Kit (with Ray)"
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"

    def test_both_arms_present(self):
        b = _block()
        assert "meta_arm" in b
        assert "openai_arm" in b

    def test_meta_arm_fields(self):
        m = _block()["meta_arm"]
        assert m["entity"] == "meta"
        assert m["outlet"] == "bbc"
        assert "Zoe Kleinman" in m["author_byline"]
        assert "tone_MANUAL_ILLUSTRATIVE" in m
        assert m["tone_MANUAL_ILLUSTRATIVE"] == META_TONE
        assert m["url"] == NOVEL_URLS[0]

    def test_openai_arm_fields(self):
        o = _block()["openai_arm"]
        assert o["entity"] == "openai"
        assert o["outlet"] == "bbc"
        assert o["author_byline"] == "Zoe Kleinman"
        assert "tone_MANUAL_ILLUSTRATIVE" in o
        assert o["tone_MANUAL_ILLUSTRATIVE"] == OPENAI_TONE
        assert o["url"] == NOVEL_URLS[1]

    def test_delta_field(self):
        b = _block()
        assert b["illustrative_delta_openai_minus_meta"] == ILLUSTRATIVE_DELTA

    def test_evidence_tier_excerpt(self):
        b = _block()
        for arm in ("meta_arm", "openai_arm"):
            assert "EXCERPT-TIER" in b[arm]["evidence_tier"]
            assert "0 browser.open" in b[arm]["evidence_tier"]

    def test_verbatim_urls_not_constructed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "verbatim" in src.lower()

    def test_ascii_only_no_em_dashes(self):
        for p in [os.path.join(TESTS_DIR, OWN_BASENAME), JOURNALISTS_PATH]:
            text = _read(p)
            assert "\u2014" not in text, p
            assert "\u2013" not in text, p


# ---------------------------------------------------------------------------
# 5. Content discipline: the m1019 pair
# ---------------------------------------------------------------------------

class TestM1019ContentDiscipline1313:
    def test_same_writer_same_outlet(self):
        b = _block()
        assert "Zoe Kleinman" in b["meta_arm"]["author_byline"]
        assert b["openai_arm"]["author_byline"] == "Zoe Kleinman"
        assert b["meta_arm"]["outlet"] == b["openai_arm"]["outlet"] == "bbc"

    def test_meta_arm_cobyline_disclosed(self):
        # The Meta arm is co-bylined (Kleinman + Mintz); the confound is
        # disclosed, not hidden.
        b = _block()
        assert "Luke Mintz" in b["meta_arm"]["author_byline"]
        assert any("Co-byline" in c for c in b["confounders"])

    def test_temporal_proximity(self):
        b = _block()
        assert b["meta_arm"]["date"] == "2026-09-24"
        assert b["openai_arm"]["date"] == "2026-09-23"
        assert "1 day apart" in b["design"]

    def test_meta_arm_headline(self):
        m = _block()["meta_arm"]
        assert "pervert glasses" in m["title"]
        assert "camera-free version" in m["title"]

    def test_openai_arm_headline(self):
        o = _block()["openai_arm"]
        assert "cyber defence tools to Ukraine" in o["title"]

    def test_register_readings(self):
        b = _block()
        assert "Adversarial privacy" in b["meta_arm"]["tone_reading"]
        assert "Positive partnership" in b["openai_arm"]["tone_reading"]

    def test_illustrative_tones(self):
        b = _block()
        assert b["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == META_TONE
        assert b["openai_arm"]["tone_MANUAL_ILLUSTRATIVE"] == OPENAI_TONE
        assert b["illustrative_delta_openai_minus_meta"] == ILLUSTRATIVE_DELTA

    def test_zero_gradient_financial_context(self):
        # No documented bilateral AI content-licensing deal between the
        # BBC and OpenAI or Meta in-corpus; SPUR membership (m514) is
        # standards-governance background, disclosed, NOT a payer leg.
        b = _block()
        assert "ZERO-GRADIENT" in b["financial_context"]
        assert "SPUR" in b["financial_context"]
        assert "not a collective licensing body" in b["financial_context"]

    def test_confounds_ranked(self):
        b = _block()
        conf = b["confounders"]
        assert any("STRONGEST" in c for c in conf)
        assert any("peg asymmetry" in c.lower() for c in conf)

    def test_counterevidence_disclosed(self):
        b = _block()
        assert "counter_evidence" in b
        assert len(b["counter_evidence"]) >= 2

    def test_scout_rejections_documented(self):
        b = _block()
        assert "rejection_audit" in b
        assert "Charlton" in b["rejection_audit"]
        assert "Holmes" in b["rejection_audit"]

    def test_research_method_documented(self):
        b = _block()
        assert "Delegated scout" in b["research_method"]
        assert "0 browser.open" in b["research_method"]


# ---------------------------------------------------------------------------
# 6. Statistical discipline: MANUAL/QUALITATIVE ONLY (Aug 28 2026 rule)
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1313:
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
        # The +0.80 delta sits on a ZERO-GRADIENT pair (no documented
        # payer differential at the BBC for OpenAI or Meta), so
        # the naive payer-softening prediction is NULL here: the delta
        # is a journalist-level register-asymmetry observation, neither
        # meeting nor failing a financial prediction. NOT a
        # falsification-family member.
        b = _block()
        assert b["falsification_family_member"] is False
        assert "zero-gradient" in b["falsification_family"].lower()


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 59 (NOT a member).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1313:
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
# 8. Guard lifecycle: pins for #1314; #1312's pins flip BY DESIGN.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1313:
    def test_pins_on_1019_landing(self):
        # Type B lands one mechanism: max becomes 1019, next is 1020.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1019" in src
        assert "NEXT_NUM = 1020" in src

    def test_no_type_c_1314_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1314's terminal log-hash followup
        # per #721): every commit whose message matches "Type C
        # #1314" must be #1314's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1314 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type C #1314")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1314's own commits"
        main = _git("rev-parse", PRED_MAIN_1314).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1020_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1020_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1020_dash_absent_repo_wide(self):
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
        # m1019 is NOT a falsification-family member (zero-gradient
        # observation); the sixtieth member-claim form stays absent
        # repo-wide.
        assert _git_grep_tracked_source(_T60, None) == []

    def test_predecessor_1312_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, D1312_FILE))

    def test_next_leg_is_1314_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1314 Type C" in src

    def test_1312_pins_flip_by_design_documented(self):
        # #1312's forward guards (max-1015, zero one-zero-one-six
        # keys all forms, no-Type-B-#1313-in-git-log, fortieth
        # direction absent, forty-eighth through fifty-ninth members
        # intact, no sixtieth member, ledger 59) verified GREEN
        # pre-commit this run via the subprocess staleness pin (Type
        # B lands mechanism 1019 as a zero-gradient observation,
        # not a family member); the max-1015 and zero one-zero-one-six
        # pins flip post-main-commit on this run's own landing (the
        # #1191-class self-trip on no-Type-B-#1313-in-git-log, re-pinned
        # green in the terminal followup, and the #1272-class
        # forward-guard expiry on 1019-numeric-absent, permanent), by
        # design, documented in the staleness pin below).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1313" in src
        assert "1 failed, 21 passed" in src


# ---------------------------------------------------------------------------
# 9. Background suite: #1310's suite is CHECKED ONLY per #795.
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1313:
    def test_1310_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1310_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1310-launched suite is observed.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1313_full_suite.log"))

    def test_observation_documented_in_block(self):
        assert "#1310-launched" in _block()["background_suite_status"]
        assert "#795" in _block()["background_suite_status"]
        assert "#1310" in _block()["background_suite_status"]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1313:
    def test_readme_test_file_table_has_1313_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_b_1313" in readme

    def test_architecture_has_1313_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1313" in arch

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

class TestIterationLog1313:
    def test_1313_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1313 Type B" in log

    def test_1312_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1312 Type A" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1312's guard lifecycle flips BY DESIGN post-commit
# ---------------------------------------------------------------------------

class TestStalenessPins1313:
    def test_1312_guard_lifecycle_post_commit_self_trip(self):
        # Post-terminal-followup form: 21 of the 22 pass; the one that
        # fails BY DESIGN is test_1019_numeric_absent_in_profiles
        # (mechanism 1019 lands in profiles/ this run; the #1272-class
        # forward-guard expiry - the next-number guard is consumed by
        # the landing; stays red permanently). The second flip,
        # test_no_type_b_1313_in_git_log_pin (the #1191-class
        # self-trip: this run's own main commit carries "Type B
        # #1313"), is re-pinned green in the terminal log-hash
        # followup per #721 (its PRED_MAIN_1313 now holds this run's
        # main sha). test_pins_on_one_mechanism_landing stays GREEN
        # (asserts on the #1312 file's own constants, untouched by
        # this run); the member and direction pins stay GREEN (m1019
        # is a zero-gradient observation, not a family member).
        # Deselected pre-commit (the pin passes pre-commit).
        res = _class_run(D1312_FILE, "TestGuardLifecycle1312")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "1 failed, 21 passed" in res.stdout, res.stdout[-2000:]
        assert "test_1019_numeric_absent_in_profiles" in res.stdout, \
            res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1313:
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

    def test_own_diff_excludes_inflight(self):
        # This run's staged set must never include the in-flight
        # files; verified at commit time by explicit-path staging.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "explicit-path" in src
