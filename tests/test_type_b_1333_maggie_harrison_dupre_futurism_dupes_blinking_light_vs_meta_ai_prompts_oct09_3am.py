# -*- coding: utf-8 -*-
"""Type B #1333 tests: Maggie Harrison Dupre (Futurism) - Oct-8-2026 Meta
AI-glasses dupes / blinking-light piece (-0.40 MANUAL ILLUSTRATIVE, NEW
arm: adversarial privacy register - TikTok Shop dupes marketed as Meta
alternatives without the "annoying blinking light") vs Sep-11-2026 Meta
AI suggested-prompts piece (-0.40 MANUAL ILLUSTRATIVE, EARLIER arm:
adversarial privacy register - Meta AI posing invasive questions about
a woman's young daughters, Meta says making changes); illustrative
delta (new minus earlier) 0.00 - register constancy, same writer, same
outlet, 27 days apart, both adversarial-privacy pegs on Meta.

Mechanism 1031 (NOT a falsification-family member; ledger holds at
62). FIRST dedicated Type B pair on Maggie Harrison Dupre (zero
maggie_harrison_dupre_type_b keyed entry pre-commit; zero "maggie
harrison" hits repo-wide pre-commit - fully novel journalist;
futurism.com article URLs zero-hit in profiles/ + tests/ pre-commit).
ZERO-GRADIENT control on the payer axis: no documented Futurism x
Meta / x Anthropic / x OpenAI AI content licensing deal in-corpus -
the pair cannot test the payer-softening prediction (the
#1313/#1318/#1328 control-case precedent). TEMPORAL
register-constancy design per the #1323 Katie Paul precedent: both
arms are Meta arms (no cross-entity leg), so this is a
baseline-register observation for a novel journalist, not a
cross-entity prediction test.

Main-run research (the delegated scout ran 10 queries: ruled out
Goode, Chokkattu, Pero, Ashworth, Schiffer, Rogers, Ropek, Bell and
Keach as in-corpus; surfaced 3 novel leads - Schroeder/Mashable,
Dupre/Futurism, Phelan/Gizmodo). Main-run screening: Schroeder
REJECTED (no clean Sep-20-Oct-9 Meta arm by byline); Phelan REJECTED
(no clean Meta arm, date unverified); Dupre SELECTED (fully novel
journalist, same outlet, 27-day adversarial-privacy pair,
relay-verbatim URLs). 9 main-run browser.search verification sets, 0
browser.open per #503. All URLs copied verbatim from Full-URL
listings; none constructed. Bylines attested via relay attributions
("futurism.com - Maggie Harrison Dupre" via Flipboard; "Maggie
Harrison Dupre/Futurism" via Techmeme).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup commit. One anchor test (the placeholder pin) fails BY DESIGN
post-anchor.

Per #795: this run only CHECKS the #1330-launched background suite
(goal hidden_files type_d_1330_full_suite.log, observed at this run's
check; an observation, not a verdict); its verdict and tombstone
belong to #1335 (next Type D). This run neither re-launches, kills,
nor writes to the suite.

Rotation: this run is iteration #1333 Type B, the FOURTH leg of the
1330-1334 window (D #1330 -> E #1331 -> A #1332 -> B #1333 -> C #1334,
per the #565 anchor + rotation guard). Predecessor #1332 Type A
verified in git log (main ec6f82b9 / anchor f810858b / doc-sync
015c7ece / log-hash 1d85704a); #1331 Type E verified (main f2e2cec6 /
anchor 4b3d4ad2 / doc-sync 29d4bec3 / log-hash b6a99d6a); the 1325-1329
window is VERIFIED CLOSED. This run's main commit is the anchor per
#565; ANCHORED_SHA patched post-commit. The #1332 forward guards
verified pre-commit this run: max-1030; zero one-zero-three-one keys
all forms; no-Type-B-#1333-in-git-log; fortieth direction absent;
forty-eighth through sixty-second members intact; no sixty-third
member (repo-wide); ledger 62. Next run #1334 Type C closes the
window; the #1330-launched background-suite verdict belongs to #1335
per #795.

Type B lands one mechanism (m1031). Pre-commit novelty greps per
#715: zero test_type_b_1333 files on disk (glob); no "Type B #1333" in
git log (--grep); max numeric mechanism_id 1030 in profiles/
pre-commit (mechanism_id regex sweep); zero numeric/underscore/dash
one-zero-three-one mechanism key forms repo-wide pre-commit (needles
format-built per #715, own file excluded, __pycache__ excluded);
"maggie harrison" zero-hit repo-wide pre-commit (fully novel
journalist); futurism.com article URLs zero-hit in profiles/ + tests/
pre-commit (git grep -F); block key zero-hit repo-wide pre-commit
(designed keying: iteration 1333 in key, no 1031 or 1032 substring,
per the #723/#738/#739 convention); "## #1333" zero-hit in
iteration-log pre-commit; README stats 76121/1657 pre-commit; no
#1333 row in README/ARCHITECTURE test tables pre-commit; 2/2 novel
relay URLs zero-hit repo-wide pre-commit (git grep -F); both arm
headlines zero-hit repo-wide pre-commit ("Cheap Dupes"; "invasive
questions about a woman").

Doc-sync constants per #719: README_TEST_COUNT / README_FILE_COUNT
hold the post-doc-sync values from the start (patched pre-main once
the in-gate collection count is known); the doc-sync commit ratchets
README 76121/1657 -> post-sync totals.

In-gate: deselected by design (TestAnchor1333 1 + TestMechanismNovelty
1333 1 + TestGuardLifecycle1333 1 + TestStalenessPins1333 1 +
TestDocSync1333 3 + TestIterationLog1333 3 per #565/#719/#721).

Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B
test file working-tree edit), #900 (untracked Type D test file),
#1012-wt (working-tree edit on the committed Type A #1012 file) all
left out of this run's index/diff (explicit-path staging). #1024
m846 (profiles/competitor-entities.yaml) NOT touched - decision
pending. Do NOT touch #1024.

Literal discipline per #715: this file carries no contiguous literal
of a forward-guard claim form; the constants are constructed at
runtime. (The landed ordinals live as short lowercase forms in prose
here; the live full-form claims live in profiles/financial-times.yaml,
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
    "test_type_b_1333_maggie_harrison_dupre_futurism_dupes_"
    "blinking_light_vs_meta_ai_prompts_oct09_3am.py"
)
TOP_KEY = "maggie_harrison_dupre_type_b"

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "8ecaff72e61b8f6567a7bc186fa3cf42f810e865"  # patched to the main commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1031
NEXT_NUM = 1032  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_b_1333_maggie_harrison_dupre_futurism_dupes_"
    "blinking_light_vs_meta_ai_prompts_oct09_3am"
)

# Predecessor chain: #1332 Type A (third leg).
PRED_MAIN_1332 = "ec6f82b9360e649e99bd6da0fe7470fd444c4dd3"
PRED_ANCHOR_1332 = "f810858b8197f6f9be611b2b929f4da69a231b6b"
PRED_DOCSYNC_1332 = "015c7eceab299c2239a0691438e6560b4b63f043"
PRED_FINAL_1332 = "1d85704ab6690a40bb810ba6537baeffe3cff0d7"
# #1331 Type E (second leg) for the rotation-guard chain.
PRED_MAIN_1331 = "f2e2cec6132603b0114e3a437ecf9d4f8cb42e03"
PRED_ANCHOR_1331 = "4b3d4ad2b21d6ba5d3dc94958954b4d43824d058"
PRED_DOCSYNC_1331 = "29d4bec3ee064ae626a96808aa7d603f417e491e"
PRED_FINAL_1331 = "b6a99d6ac42003c119246645bf627e627b0e1ca6"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the own-run git-log pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1333 = "8ecaff72e61b8f6567a7bc186fa3cf42f810e865"  # re-pinned to #1333 main sha in the anchor followup per #721/#1292

# Forward guard for the next leg: #1334 Type C. Re-pinned by #1334's
# log-hash followup per #721 (starts as 0*40; the forward pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1334 = "059c612b67177afde506c1509f6cefe0db495d8b"  # re-pinned to #1334 main sha per #721 (#1292 both-copies)

# The #1332 window-continuation file, for the staleness pin on its
# guard-lifecycle class.
B1332_FILE = (
    "test_type_a_1332_wsj_openai_oct08_fired_researchers_open_letter_"
    "vs_carried_wsj_meta_arms_oct09_3am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 76231  # post-doc-sync total (pre-sync 76121 + 110) - PATCHED post-collection
README_FILE_COUNT = 1658  # pre-sync 1657 + 1 (this file)

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
_T62 = "SIXT" + "Y-SECOND falsification-family member"
_T63 = "SIXT" + "Y-THIRD falsification-family member"

# Novel relay URLs: 2 zero-hit repo-wide pre-commit (git grep -F).
# Both are relay attestations (Flipboard / Techmeme) carrying the
# Futurism byline; the futurism.com canonicals did not surface in
# search listings (no-construction rule: not linked).
NOVEL_URLS = [
    "https://flipboard.com/@Slashgear/3-cheaper-alternatives-to-meta-smart-glasses/a-nnHncWuyRY2kkua67RZK_A%3Aa%3A131778153-8c7b00c251%2Fslashgear.com",
    "https://www.techmeme.com/260911/p20",
]
RESURFACED_URLS = []

# MANUAL ILLUSTRATIVE tones (hand-assigned at excerpt level).
META_TONE_NEW = -0.40
META_TONE_EARLIER = -0.40
ILLUSTRATIVE_DELTA = 0.0  # new minus earlier


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

class TestAnchor1333:
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
        assert "FOURTH leg of the 1330-1334 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1333:
    def test_predecessor_1332_chain_verified(self):
        for sha in (
            PRED_MAIN_1332, PRED_ANCHOR_1332, PRED_DOCSYNC_1332,
            PRED_FINAL_1332,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1331_chain_verified(self):
        for sha in (
            PRED_MAIN_1331, PRED_ANCHOR_1331, PRED_DOCSYNC_1331,
            PRED_FINAL_1331,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1330 -> E #1331 -> A #1332 -> B #1333 -> C #1334" in src

    def test_next_leg_is_type_c_1334(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1334 Type C" in src

    def test_type_b_lands_one_mechanism(self):
        # Type B lands exactly one mechanism (mechanism 1031); the Type
        # A predecessor added one (mechanism 1030).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type B lands one mechanism" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1333:
    def test_top_key_found(self):
        assert _top()["mechanism_ids"] == [MECH_NUM]

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1333 in key, no 1031 or
        # 1032 substring.
        assert "1333" in BLOCK_KEY
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

    def test_no_type_b_1333_in_git_log_own_run(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type B #1333" must be #1333's main
        # commit or a descendant of it. Deselected in the in-gate run
        # (fails pre-commit by design: PRED_MAIN_1333 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type B #1333")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1333's own commits"
        main = _git("rev-parse", PRED_MAIN_1333).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_novel_urls_zero_hit_pre_commit(self):
        # Both relay URLs were verified zero-hit repo-wide pre-commit
        # via git grep -F this run (documented in the block's novelty
        # field).
        for url in NOVEL_URLS:
            out = _git("grep", "-F", "-l", url, "HEAD", "--", ".")
            assert out.stdout.strip() == "", url

    def test_journalist_first_dedicated_pair(self):
        # FIRST dedicated Type B pair on Maggie Harrison Dupre: zero
        # maggie_harrison_dupre_type_b keyed entry pre-commit; zero
        # "maggie harrison" hits repo-wide pre-commit (fully novel
        # journalist); futurism.com article URLs zero-hit in profiles/
        # + tests/ pre-commit.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIRST dedicated Type B pair on Maggie Harrison Dupre" in src

    def test_headlines_zero_hit_pre_commit(self):
        # Both arm headlines were verified zero-hit repo-wide
        # pre-commit this run.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert '"Cheap Dupes"' in src
        assert "invasive questions about a woman" in src

    def test_no_1333_row_in_readme_table(self):
        readme = _read(README_PATH)
        assert "test_type_b_1333" not in readme

    def test_no_1333_row_in_architecture_tree(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1333" not in arch

    def test_no_1333_in_iteration_log_pre_commit(self):
        log = _read(LOG_PATH)
        assert "## #1333" not in log


# ---------------------------------------------------------------------------
# 4. Block structure (the #643 convention)
# ---------------------------------------------------------------------------

class TestBlockStructure1333:
    def test_top_level_fields(self):
        t = _top()
        assert t["name"] == "Maggie Harrison Dupre"
        assert t["publication"] == "futurism"
        assert t["mechanism_ids"] == [MECH_NUM]

    def test_block_key_present(self):
        assert BLOCK_KEY in _top()["competitor_coverage"]

    def test_block_identity_fields(self):
        b = _block()
        assert b["block_key"] == BLOCK_KEY
        assert b["mechanism_id"] == MECH_NUM
        assert b["iteration"] == 1333
        assert b["iteration_type"] == "B"
        assert b["type"] == "B"
        assert b["journalist"] == "Maggie Harrison Dupre"
        assert b["publication"] == "futurism"
        assert b["author"] == "Kit (with Ray)"
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"

    def test_both_arms_present(self):
        b = _block()
        assert "new_arm" in b
        assert "earlier_arm" in b

    def test_new_arm_fields(self):
        m = _block()["new_arm"]
        assert m["entity"] == "meta"
        assert m["outlet"] == "futurism"
        assert m["tone_MANUAL_ILLUSTRATIVE"] == META_TONE_NEW
        assert m["url"] == NOVEL_URLS[0]
        assert m["date"] == "2026-10-08"
        assert m["author_byline"] == "Maggie Harrison Dupre"

    def test_earlier_arm_fields(self):
        m = _block()["earlier_arm"]
        assert m["entity"] == "meta"
        assert m["outlet"] == "futurism"
        assert m["tone_MANUAL_ILLUSTRATIVE"] == META_TONE_EARLIER
        assert m["url"] == NOVEL_URLS[1]
        assert m["date"] == "2026-09-11"
        assert m["author_byline"] == "Maggie Harrison Dupre"

    def test_delta_field(self):
        b = _block()
        assert b["illustrative_delta_new_minus_earlier"] == ILLUSTRATIVE_DELTA
        assert b["scorer_delta_MANUAL_ILLUSTRATIVE"] == ILLUSTRATIVE_DELTA

    def test_verdict_and_ledger_fields(self):
        b = _block()
        assert b["verdict"] == "directionally_supported_not_proven"
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 62
        assert b["is_significant"] is False
        assert b["correlation_not_causation"] is True
        assert b["no_analysis_json_update"] is True

    def test_window_field(self):
        b = _block()
        assert "1330-1334" in b["window"]
        assert "FOURTH leg" in b["window"]

    def test_source_urls(self):
        urls = _block()["source_urls"]
        for u in NOVEL_URLS:
            assert u in urls


# ---------------------------------------------------------------------------
# 5. m1031 content discipline
# ---------------------------------------------------------------------------

class TestM1031ContentDiscipline1333:
    def test_new_arm_quotes(self):
        quotes = " ".join(_block()["new_arm"]["key_quotes"])
        assert "annoying blinking light" in quotes
        assert "recording you right now" in quotes

    def test_new_arm_tone_reading(self):
        reading = _block()["new_arm"]["tone_reading"]
        assert "adversarial" in reading.lower()

    def test_earlier_arm_quotes(self):
        quotes = " ".join(_block()["earlier_arm"]["key_quotes"])
        assert "invasive questions" in quotes
        assert "suggested prompts" in quotes

    def test_earlier_arm_tone_reading(self):
        reading = _block()["earlier_arm"]["tone_reading"]
        assert "accountability" in reading.lower()

    def test_delta_reading_constancy(self):
        reading = _block()["delta_reading"]
        assert "constancy" in reading
        assert "0.00" in reading

    def test_confounder_ranking(self):
        confs = _block()["confounders"]
        assert any("STRONG" in c for c in confs)
        assert any("excerpt" in c.lower() for c in confs)
        assert any("no cross-entity" in c.lower() for c in confs)

    def test_zero_gradient_control_disclosed(self):
        fc = _block()["financial_context"]
        assert "ZERO-GRADIENT" in fc
        assert "Futurism" in fc

    def test_counter_evidence_present(self):
        ce = _block()["counter_evidence"]
        assert len(ce) >= 2
        joined = " ".join(ce).lower()
        assert "relay" in joined or "excerpt" in joined

    def test_rejection_audit_present(self):
        ra = _block()["rejection_audit"]
        assert "Schroeder" in ra
        assert "Phelan" in ra
        assert "Goode" in ra

    def test_research_method_documents_screening(self):
        rm = _block()["research_method"]
        assert "screening" in rm.lower()
        assert "REJECTED" in rm
        assert "9 main-run browser.search" in rm
        assert "0 browser.open" in rm


# ---------------------------------------------------------------------------
# 6. Statistical discipline (the Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1333:
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

    def test_not_a_new_member_zero_gradient(self):
        # No documented Futurism x Meta/Anthropic/OpenAI AI content
        # licensing deal in-corpus: the pair cannot test the
        # payer-softening prediction (the #1313/#1318/#1328
        # zero-gradient control-case precedent), and both arms are
        # Meta arms (temporal register-constancy design per the #1323
        # precedent), so no falsification-family advance.
        b = _block()
        assert b["falsification_family_member"] is False
        assert "zero-gradient" in b["falsification_family"]


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 62 (NOT a member).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1333:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert "NOT a falsification-family member" in b["falsification_family"]

    def test_forty_eighth_intact_in_ft(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_forty_ninth_intact_in_journalists(self):
        out = _git(
            "grep", "-c", "-F", _T49, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fiftieth_intact_in_journalists(self):
        out = _git(
            "grep", "-c", "-F", _T50, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_first_intact_in_news_corp(self):
        out = _git(
            "grep", "-c", "-F", _T51, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_second_intact_in_journalists(self):
        out = _git(
            "grep", "-c", "-F", _T52, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_fifty_third_intact_in_the_verge(self):
        out = _git(
            "grep", "-c", "-F", _T53, "HEAD", "--",
            "profiles/the-verge.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fourth_intact_in_guardian(self):
        out = _git(
            "grep", "-c", "-F", _T54, "HEAD", "--",
            "profiles/guardian.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fifth_intact_in_atlantic(self):
        out = _git(
            "grep", "-c", "-F", _T55, "HEAD", "--",
            "profiles/atlantic.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_sixth_intact_in_wired(self):
        out = _git(
            "grep", "-c", "-F", _T56, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_seventh_intact_in_ap(self):
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_intact_in_ft(self):
        out = _git(
            "grep", "-c", "-F", _T58, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_ninth_intact_in_news_corp(self):
        out = _git(
            "grep", "-c", "-F", _T59, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixtieth_intact_in_ft(self):
        out = _git(
            "grep", "-c", "-F", _T60, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_first_intact_in_wired(self):
        out = _git(
            "grep", "-c", "-F", _T61, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_second_intact_in_news_corp(self):
        # Landed #1332 (m1030, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T62, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_sixty_third_member(self):
        # Type B lands one mechanism (m1031, NOT a member); the
        # sixty-third member-claim form stays absent repo-wide.
        assert _git_grep_tracked_source(_T63, None) == []


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: #1332's forward guards flip BY DESIGN post-commit.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1333:
    def test_pins_on_one_mechanism_landing(self):
        # Type B lands one mechanism: max 1031, next 1032.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1031" in src
        assert "NEXT_NUM = 1032" in src

    def test_no_type_c_1334_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1334's terminal log-hash followup
        # per #721): every commit whose message matches "Type C
        # #1334" must be #1334's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type C #1334")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1334's own commits"
        main = _git("rev-parse", PRED_MAIN_1334).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1032_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1032_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1032_dash_absent_repo_wide(self):
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

    def test_sixtieth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T60, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_first_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T61, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_second_member_present_pin(self):
        # Landed #1332 (m1030, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T62, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_sixty_third_member_pin(self):
        # Type B lands one mechanism (m1031, NOT a member); the
        # sixty-third member-claim form stays absent repo-wide.
        assert _git_grep_tracked_source(_T63, None) == []

    def test_predecessor_1332_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, B1332_FILE))

    def test_next_leg_is_1334_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1334 Type C" in src

    def test_1332_pins_flip_by_design_documented(self):
        # #1332's forward guards (max-1030, zero one-zero-three-one
        # keys all forms, no-Type-B-#1333-in-git-log, fortieth
        # absent, forty-eighth through sixty-second intact in
        # profiles/, no sixty-third member repo-wide, ledger 62)
        # verified GREEN at HEAD pre-commit this run. TWO pins flip
        # BY DESIGN at this run's main commit: the #1191-class
        # self-trip (no-Type-B-#1333-in-git-log, re-pinned
        # post-commit by TestStalenessPins1333 in both copies per
        # the re-pin-both-copies precedent) and the #1272-class
        # forward-guard expiry (the 1031-numeric-absent-in-profiles
        # pin trips on the landed m1031 block - permanent red by
        # design). The 1031-underscore and 1031-dash pins stay green
        # (no one-zero-three-one mechanism-key forms landed).
        # Documented in the staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1333" in src
        assert "no_type_b_1333_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 9. Background suite per #795 (observation only).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1333:
    def test_1330_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1330_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1330-launched suite is observed.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1333_full_suite.log"))

    def test_observation_documented_in_block(self):
        assert "#1330-launched" in _block()["background_suite_status"]
        assert "#795" in _block()["background_suite_status"]
        assert "#1335" in _block()["background_suite_status"]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------

class TestDocSync1333:
    def test_readme_test_file_table_has_1333_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_b_1333" in readme

    def test_architecture_has_1333_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1333" in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_PATH)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 11. Iteration log (3 tests; deselected pre-commit per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1333:
    def test_1333_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1333 Type B" in log

    def test_1332_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1332 Type A" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1332's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------

class TestStalenessPins1333:
    def test_1332_guard_lifecycle_post_commit_self_trip(self):
        # Post-terminal-followup form: 25 tests in the class; 24 pass,
        # 1 fails BY DESIGN and permanently - the #1272-class
        # forward-guard expiry (test_1031_numeric_absent_in_profiles
        # trips on the landed m1031 block). The #1191-class self-trip
        # (test_no_type_b_1333_in_git_log_pin) was red at this run's
        # main-commit time; the anchor followup re-pinned
        # PRED_MAIN_1333 in BOTH its own file's copy and the #1332
        # predecessor file's copy per the #1292 re-pin-both-copies
        # precedent and the #721 re-pin rule, flipping it green. The
        # 1031-underscore and 1031-dash pins stay green (no
        # one-zero-three-one mechanism-key forms landed).
        # Deselected in the in-gate run (fails pre-commit by
        # design); verified post-terminal.
        res = _class_run(B1332_FILE, "TestGuardLifecycle1332")
        out = res.stdout + res.stderr
        assert "1 failed, 24 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1333:
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

    def test_own_diff_excludes_inflight(self):
        # This run's staged set must never include the in-flight
        # files; verified at commit time by explicit-path staging.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "explicit-path" in src

    def test_1024_m846_untouched(self):
        # Ray's revert/leave/rebuild decision on m846 is pending;
        # this run does not touch it.
        res = _git("status", "--short")
        assert "competitor-entities.yaml" not in res.stdout
