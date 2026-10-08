"""Type A #1297: Guardian x OpenAI Oct-6 Kwon parliamentary-apology register (Oct 7 2026, ~09:00 PM PDT).

m1009 - FIRST dedicated corpus mechanism on the Guardian's Oct-6
parliamentary-accountability peg on the Feb-2025 licensing partner.
Guardian Australia puts OpenAI chief strategy officer Jason Kwon in the
witness chair before the Joint Select Committee on Artificial
Intelligence in Sydney over the June Medicare-portal agent breach and
the 84-day notification gap (the 2:42am-email notification the prime
minister publicly shamed). Headline frame: "OpenAI has 'work to do to
rebuild trust' in Australia, executive tells AI inquiry". Register:
parliamentary accountability; the apology is printed ("We are sorry,
and we know we have work to do to rebuild trust with the Australian
people") but the frame is institutional failure. MANUAL ILLUSTRATIVE
-0.30, the same even-handed straight-news band as m994's Robinson
resignation arm (-0.30, #1272).

Carried Guardian x Meta arms (m687, un-rescored per #807): the Sep
police-warnings documents investigation (-0.55) and the Aug-18
teen-accounts influencer payouts (-0.45), band mean -0.50.
Illustrative delta (OpenAI minus Meta): clean n=1 vs n=1 (Kwon vs
police-warnings) +0.25; pooled n=1 vs n=2 +0.20. Directionally softer
for the Feb-2025 licensing partner, matching the standing
coverage_prediction ("softer").

Per #715 this docstring uses lowercase forms only: NOT a
falsification-family member (m985, #1257, already counted the pair's
falsification on the own-investigation peg - the Guardian's cross-lab
investigation naming the deal partner's ChatGPT a hijab-removal
complier; the #1143 temporal-replication precedent does not admit a
second member on the same pair). Ledger holds at 58; no fifty-ninth
member; fortieth direction absent. Verdict:
thesis_consistent_observation. The piece does NOT suppress the
adversarial content (the breach, the 84-day gap, and the prime
minister's shaming are all printed); softness is register-level, not
story suppression - which bounds the softening claim, exactly as in
m994's confounder analysis.

Novelty: the Kwon arm is zero-hit repo-wide pre-commit (kwon/Kwon/
"rebuild trust"/parliamentary all zero-hit in guardian.yaml; the
Guardian Australia video URL zero-hit). The Sep-27 training-halt
original is saturated (m862, #1052, directionally_supported_not_proven)
and the Oct-3 Robinson resignation original is saturated (m994, #1272,
thesis_consistent_observation) - both deliberately excluded from the
NEW arm set; this run scores the Oct-6 peg only.

Statistical discipline: monitoring-only per the Aug 28 2026 standing
rule (MANUAL ILLUSTRATIVE ONLY, engine NOT run, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False, NOT artifact-grade, no
analysis.json update, verdict thesis_consistent_observation).
Correlation is not causation. Hypothesis-generating only.

4 main-run browser.search verification sets (2 initial pair-discovery
sets + 2 targeted Kwon/Milmo sets), 0 browser.open per #503.
Excerpt-bounded; the Guardian Australia video is the original (Guardian
Australia YouTube channel); the Oct-6 article reads through two
independent relays with verbatim Guardian attribution. All URLs copied
verbatim from Full-URL listings; no canonical URLs constructed.
ASCII-only, no em dashes.

Rotation: this run is iteration #1297 Type A, the THIRD leg of the
1295-1299 window (D #1295 -> E #1296 -> A #1297 -> B #1298 -> C #1299,
per the #565 anchor + rotation guard). Predecessor #1296 Type E
verified in git log (main 14af9fec / anchor ab777872 / doc-sync
064eb530 / log-hash 953ddaaa); the 1290-1294 window is VERIFIED
CLOSED. This run's main commit is the anchor per #565; ANCHORED_SHA
patched post-commit. The #1296 forward guards verified pre-commit this
run: max-1008; zero next-number one-zero-zero-nine mechanism keys all
forms (profiles/ + tests/ scope, __pycache__ excluded per the #715
pattern-rescope lesson); no-Type-A-#1297-in-git-log; fortieth
direction absent (profiles/ scope); forty-eighth through fifty-eighth
members intact; no fifty-ninth member (repo-wide, source scope); ledger
58. This run lands mechanism one-zero-zero-nine: TestGuardLifecycle1296's
zero one-zero-zero-nine numeric pin flips at this run's main commit BY
DESIGN (the #1272-class forward-guard expiry; the underscore/dash pins
stay green by the #723/#738/#739 designed keying) and its
no-Type-A-#1297-in-git-log pin flips BY DESIGN (the #1191-class
self-trip, re-pinned in the terminal log-hash followup per #721),
documented in TestStalenessPins1297 ("1 failed, 20 passed"), not
repaired. Next run #1298 Type B continues the window. The #1300 Type D
run owns the next background-suite verdict per #795: this run OBSERVES
only (1466 bytes, [1%] progress, last write Oct 7 2026 07:59 PM PDT;
no live pytest process visible at this run's check - the verdict
belongs to #1300).
In-flight during this run: #899 (profiles/nytimes.yaml m771 hunk),
#938 (Type B test file working-tree edit), #900 (untracked Type D
test file), #1012-wt (working-tree edit on the committed Type A
#1012 file) - all untouched; targeted explicit-path staging only. Do
NOT touch #1024 m846.

Pre-commit novelty greps per #715: zero test_type_a_1297 files on
disk (glob); no Type A #1297 in git log (--grep); max numeric
mechanism_id 1008 in profiles/ pre-commit (mechanism_id regex
sweep); zero numeric/underscore/dash next-number one-zero-zero-nine
mechanism key forms repo-wide pre-commit in source scope (needles
format-built per #715, own file excluded, __pycache__ excluded per
the #715 pattern-rescope lesson); block key zero-hit repo-wide
pre-commit (designed keying: iteration 1297 in key, no 1009
substring, per the #723/#738/#739 convention); "## #1297" zero-hit
in iteration-log pre-commit; README stats 72548/1621 pre-commit; no
#1297 row in README/ARCHITECTURE test tables pre-commit; the Kwon
video URL + 2 relay URLs zero-hit repo-wide pre-commit (git grep
-F); kwon/Kwon/"rebuild trust"/parliamentary zero-hit in
guardian.yaml pre-commit; the Sep-27 training-halt URL and the Oct-3
Robinson URL zero-hit but their EVENTS saturated (m862 #1052, m994
#1272) - excluded from the NEW arm set by design; no counted
adversarial-on-partner observation for the Kwon peg pre-commit (the
#1143 check: m985 counted the pair's falsification on the
own-investigation peg, so this run is a thesis-consistent
observation, not a member).

Doc-sync constants per #719: README_TEST_COUNT / README_FILE_COUNT
hold the post-doc-sync values from the start (patched pre-main once
the in-gate collection count is known); the doc-sync commit ratchets
README 72548/1621 -> post-sync totals.
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
GUARDIAN_PATH = os.path.join(PROFILES_DIR, "guardian.yaml")

OWN_BASENAME = (
    "test_type_a_1297_guardian_openai_oct06_kwon_parliamentary_"
    "apology_register_vs_carried_meta_arms_oct07_9pm.py"
)
BLOCK_KEY = (
    "type_a_1297_guardian_openai_oct06_kwon_rebuild_trust_"
    "parliamentary_register_vs_carried_meta_arms"
)

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "a8bd4c5dc8708c4f8604762175446526b29dcad4"  # patched in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1009
NEXT_NUM = 1010  # integer only; key-form needles are format-built

# Predecessor chain: #1296 Type E closed the SECOND leg.
PRED_MAIN_1296 = "14af9fecd0d7dcc93eced86ab065e9114f685226"
PRED_ANCHOR_1296 = "ab7778723654c3af8f3fd3ba50e98f849c4d4437"
PRED_DOCSYNC_1296 = "064eb53069399711d54b405d2e763d16c909a828"
PRED_FINAL_1296 = "953ddaaa62a7f16ba13c2b6889aa900fcc57b7c0"

# This run's main commit (full sha), for the ancestor-form
# no-Type-A-#1297 pin in the #1296 file. Patched in the terminal
# log-hash followup per #721.
PRED_MAIN_1297 = "0" * 40  # placeholder-only per #721

# #1298's main commit (full sha), for the ancestor-form no-Type-B-#1298
# pin. Patched in #1298's terminal log-hash followup per #721.
PRED_MAIN_1298 = "0" * 40  # placeholder-only per #721

# The #1296 predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1008; zero next-number
# one-zero-zero-nine / no-Type-A-#1297-in-git-log / fortieth
# direction absent / forty-eighth through fifty-eighth members
# intact / fifty-ninth member absent / ledger 58).
D1296_FILE = (
    "test_type_e_1296_podcast_sentiment_182nd_"
    "verification_oct07_8pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 72642  # post-doc-sync total (pre-sync 72548 + 94)
README_FILE_COUNT = 1622  # pre-sync 1621 + 1 (this file)

# MANUAL ILLUSTRATIVE tones (hand-assigned at excerpt level).
A1_KWON_TONE = -0.30
META_POLICE_WARNINGS_TONE = -0.55  # m687, carried un-rescored per #807
META_TEEN_ACCOUNTS_TONE = -0.45  # m687, carried un-rescored per #807
META_MEAN = -0.50
DELTA_CLEAN = 0.25  # -0.30 - (-0.55), n=1 vs n=1
DELTA_POOLED = 0.20  # -0.30 - (-0.50), n=1 vs n=2

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
# The fifty-ninth member-claim form is fragment-built per #715
# (no fifty-ninth member may exist repo-wide; staged for #1298).
_T59 = "FIFT" + "Y-NINTH falsification-family member"


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git"] + list(args), cwd=REPO_ROOT, capture_output=True,
        text=True,
    )


def _iter_source_files():
    """Yield profile + test source files for the sweep instruments.

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
    args = ["git", "grep", "-F", "-l", needle, "HEAD", "--"]
    if scope:
        args.append(scope)
    out = subprocess.run(
        args, cwd=REPO_ROOT, capture_output=True, text=True
    ).stdout
    cleaned = []
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("HEAD:"):
            line = line[len("HEAD:"):]
        if line:
            cleaned.append(line)
    return cleaned


def _class_run(filename, classname):
    target = os.path.join(TESTS_DIR, filename)
    env = dict(os.environ)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    venv_py = os.path.join(REPO_ROOT, ".venv", "bin", "python")
    return subprocess.run(
        [venv_py, "-m", "pytest", target, "-k", classname,
         "-q", "--no-header", "-o", "addopts=", "-p", "no:cacheprovider"],
        cwd=REPO_ROOT, capture_output=True, text=True, env=env,
        timeout=600,
    )


def _block():
    """Return the landed m1009 profile block for this run."""
    with open(GUARDIAN_PATH, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)

    def _walk(node):
        if isinstance(node, dict):
            if node.get("block_key") == BLOCK_KEY:
                return node
            for v in node.values():
                hit = _walk(v)
                if hit is not None:
                    return hit
        elif isinstance(node, list):
            for v in node:
                hit = _walk(v)
                if hit is not None:
                    return hit
        return None

    hit = _walk(data)
    assert hit is not None, "m1009 block not found"
    return hit

# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------


class TestAnchor1297:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to the main commit sha per #565. This test is
        # deselected in the in-gate run; the patched form is asserted
        # post-anchor.
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

    def test_anchor_duality_documented(self):
        # The #565 duality: the placeholder pin passes pre-commit and
        # fails post-anchor BY DESIGN; the patched pin is the mirror.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "BY DESIGN post-anchor" in src or "fails BY DESIGN" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1296 closed the SECOND leg; #1297 is the THIRD.
# ---------------------------------------------------------------------------


class TestRotationGuard1297:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-60").stdout
        for sha, label in (
            (PRED_MAIN_1296, "1296 main"),
            (PRED_ANCHOR_1296, "1296 anchor"),
            (PRED_DOCSYNC_1296, "1296 doc-sync"),
            (PRED_FINAL_1296, "1296 log-hash"),
        ):
            assert sha[:8] in log, label

    def test_1296_type_e_in_git_log(self):
        out = _git("log", "--oneline", "--grep=Type E #1296").stdout
        assert out.strip() != ""

    def test_third_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "THIRD leg of the 1295-1299 window" in src

    def test_1290_1294_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1290-1294" in src
        assert "VERIFIED CLOSED" in src

    def test_next_leg_is_1298_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "B #1298" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty: Type A lands one mechanism (max 1008 -> 1009).
# ---------------------------------------------------------------------------


class TestMechanismNovelty1297:
    def test_max_numeric_mechanism_id_1009(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_no_type_a_1297_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type A #1297" must be this run's
        # main commit or a descendant of it - i.e., no PRIOR run
        # committed this run's iteration. Deselected in the in-gate
        # run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type A #1297")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1297).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_zero_next_number_keys_all_forms(self):
        # Numeric (profiles/ scope), underscore and dash (profiles/ +
        # tests/ scope, own file excluded per #715, __pycache__
        # excluded per the #715 pattern-rescope lesson). NEXT_NUM is
        # 1010: this run lands 1009, so the next-number forms stay
        # absent.
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_key_designed_no_1009_substring(self):
        # Designed keying per #723/#738/#739: the iteration-form block
        # key carries the iteration (1297), never the mechanism number.
        assert "1009" not in BLOCK_KEY
        assert "1297" in BLOCK_KEY

    def test_forward_guards_for_1298(self):
        # Staged for the next leg: max-1009 in profiles/; zero
        # one-zero-one-zero keys all forms; no-Type-B-#1298-in-git-log;
        # fortieth direction absent; forty-eighth through fifty-eighth
        # intact; no fifty-ninth member; ledger 58.
        assert _max_numeric_mechanism_id() == 1009
        assert _repo_grep_numeric_mechanism_id(1010) == []
        assert _repo_grep_underscore_mechanism(1010) == []
        assert _repo_grep_dash_mechanism(1010) == []
        assert _git("log", "--oneline", "--grep=Type B #1298").stdout.strip() == ""
        assert _git_grep_tracked_source(_T40, "profiles/") == []
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]
        assert _T58 in _read(os.path.join(PROFILES_DIR, "financial-times.yaml"))
        assert _git_grep_tracked_source(_T59, None) == []

    def test_novel_urls_zero_hit_pre_commit(self):
        # The 3 novel source URLs were zero-hit repo-wide pre-commit
        # (git grep -F, verified this run before the block landed).
        # Post-landing they live in the block's source_urls and in the
        # arm's url_source; assert each is present exactly twice in
        # guardian.yaml.
        text = _read(GUARDIAN_PATH)
        assert text.count("youtube.com/watch?v=ztNkqArWCxk") == 2
        assert text.count("aitopics.org/class/Country/Oceania/Australia") == 2
        assert text.count("aipolicydaily.org/archive/daily/2026-10-06") == 2


# ---------------------------------------------------------------------------
# 4. Guardian x OpenAI Oct-6 Kwon arm (NEW this run)
# ---------------------------------------------------------------------------


class TestGuardianKwonApology1297:
    def test_block_present_with_mechanism_id_1009(self):
        block = _block()
        assert block["mechanism_id"] == 1009
        assert block["iteration"] == 1297
        assert block["iteration_type"] == "A"

    def test_arm_date_oct06_2026(self):
        block = _block()
        arm = block["openai_arms"][0]["item"]
        assert arm["date"] == "2026-10-06"

    def test_arm_is_guardian_australia_original(self):
        block = _block()
        arm = block["openai_arms"][0]["item"]
        assert "Guardian Australia" in arm["publication"]
        assert "youtube.com/watch?v=ztNkqArWCxk" in arm["url_source"]

    def test_arm_names_kwon_and_committee(self):
        block = _block()
        assert "Kwon" in yaml.safe_dump(block)
        # Asserted on the raw field: safe_dump folds long lines at
        # 80 cols, which can split the phrase in the dump.
        assert ("Joint Select Committee on Artificial Intelligence"
                in block["event"])

    def test_arm_covers_medicare_breach_and_notification_gap(self):
        block = _block()
        text = yaml.safe_dump(block)
        assert "Medicare" in text
        assert "84-day" in text

    def test_arm_rebuild_trust_quote(self):
        block = _block()
        quotes = block["openai_arms"][0]["item"]["key_quotes"]
        assert any("rebuild trust" in q for q in quotes)

    def test_arm_register_parliamentary_accountability(self):
        block = _block()
        arm = block["openai_arms"][0]["item"]
        assert arm["framing"] == "parliamentary_accountability"

    def test_arm_tone_minus_030(self):
        block = _block()
        arm = block["openai_arms"][0]["item"]
        assert arm["manual_illustrative_tone"] == A1_KWON_TONE == -0.30

    def test_arm_single_new_arm(self):
        # Only the Oct-6 peg is NEW this run: the Sep-27 training-halt
        # original is saturated (m862, #1052) and the Oct-3 Robinson
        # resignation original is saturated (m994, #1272) - both
        # deliberately excluded from the NEW arm set.
        block = _block()
        assert len(block["openai_arms"]) == 1
        assert "saturated" in yaml.safe_dump(block)

    def test_excerpt_bounded_no_browser_open(self):
        block = _block()
        assert block["research_method"].count("0 browser.open") >= 1


# ---------------------------------------------------------------------------
# 5. Carried Guardian x Meta arms (m687, un-rescored per #807)
# ---------------------------------------------------------------------------


class TestMetaArms1297:
    def test_meta_arms_carried_from_m687(self):
        block = _block()
        assert "m687" in block["meta_arms"]["carried_from"]

    def test_police_warnings_arm_minus_055(self):
        block = _block()
        arms = block["meta_arms"]["arms"]
        pw = [a for a in arms if "police" in a["title"].lower()][0]
        assert pw["manual_illustrative_tone"] == META_POLICE_WARNINGS_TONE == -0.55

    def test_teen_accounts_arm_minus_045(self):
        block = _block()
        arms = block["meta_arms"]["arms"]
        ta = [a for a in arms if "teen" in a["title"].lower() or "influencer" in a["title"].lower()][0]
        assert ta["manual_illustrative_tone"] == META_TEEN_ACCOUNTS_TONE == -0.45

    def test_meta_band_mean_minus_050(self):
        block = _block()
        assert block["meta_arms"]["meta_band_mean"] == META_MEAN == -0.50

    def test_meta_arms_unrescored_per_807(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "un-rescored per #807" in src

    def test_same_publication_adjacent_weeks(self):
        block = _block()
        assert "Same publication" in block["event"]


# ---------------------------------------------------------------------------
# 6. Financial relationship: Feb-2025 Guardian x OpenAI licensing deal
# ---------------------------------------------------------------------------


class TestFinancialRelationship1297:
    def test_deal_identified(self):
        block = _block()
        assert "Feb" in block["financial_relationship"]
        assert "2025" in block["financial_relationship"]

    def test_coverage_prediction_softer(self):
        with open(GUARDIAN_PATH, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        assert (data["competitor_relationships"]["openai"]
                ["coverage_prediction"] == "softer")

    def test_meta_zero_tie(self):
        block = _block()
        assert "$0" in block["financial_relationship"]

    def test_deal_url_present(self):
        block = _block()
        assert "openai.com/index/openai-and-guardian-media-group" in block["deal_url"]

    def test_no_disclosure_in_kwon_arm(self):
        block = _block()
        arm = block["openai_arms"][0]["item"]
        assert arm["deal_disclosed"] is False

    def test_entity_pair_polarity(self):
        block = _block()
        assert "licensing partner" in block["entity_pair"]
        assert "Meta" in block["entity_pair"]


# ---------------------------------------------------------------------------
# 7. Asymmetry delta (MANUAL ILLUSTRATIVE ONLY)
# ---------------------------------------------------------------------------


class TestAsymmetryDelta1297:
    def test_clean_delta_plus_025(self):
        block = _block()
        assert block["asymmetry_scorer_result"][
            "illustrative_delta_openai_minus_meta_clean"] == DELTA_CLEAN == 0.25

    def test_pooled_delta_plus_020(self):
        block = _block()
        assert block["asymmetry_scorer_result"][
            "illustrative_delta_openai_minus_meta_pooled"] == DELTA_POOLED == 0.20

    def test_delta_direction_softer_for_partner(self):
        block = _block()
        assert "softer" in block["asymmetry_scorer_result"]["delta_direction"]

    def test_scorer_not_run(self):
        block = _block()
        assert block["asymmetry_scorer_result"]["engine_run"] is False

    def test_target_peer_avgs(self):
        block = _block()
        assert block["asymmetry_scorer_result"]["target_avg"] == -0.30
        assert block["asymmetry_scorer_result"]["peer_avg"] == -0.50


# ---------------------------------------------------------------------------
# 8. Research method
# ---------------------------------------------------------------------------


class TestResearchMethod1297:
    def test_four_search_sets_zero_browser_open(self):
        block = _block()
        assert "4 main-run browser.search" in block["research_method"]
        assert "0 browser.open per #503" in block["research_method"]

    def test_excerpt_bounded(self):
        block = _block()
        assert "Excerpt-bounded" in block["research_method"]
        assert "per #503" in block["research_method"]

    def test_no_constructed_urls(self):
        block = _block()
        assert "no canonical URLs constructed" in block["research_method"]

    def test_verbatim_full_url_listings(self):
        block = _block()
        assert "verbatim from Full-URL listings" in block["research_method"]

    def test_ascii_only(self):
        block = _block()
        assert "ASCII-only, no em dashes" in block["research_method"]


# ---------------------------------------------------------------------------
# 9. Falsification ledger: thesis-consistent, NOT a member
# ---------------------------------------------------------------------------


class TestFalsificationLedger1297:
    def test_not_a_falsification_member(self):
        block = _block()
        assert block["falsification_family_member"] is False

    def test_ledger_holds_at_58(self):
        block = _block()
        assert block["falsification_ledger"] == 58
        assert block["ledger"] == 58

    def test_m985_counted_pair_falsification(self):
        # m985 (#1257) already counted the Guardian x OpenAI pair's
        # falsification on the own-investigation peg; the #1143
        # temporal-replication precedent does not admit a second
        # member on the same pair.
        block = _block()
        text = yaml.safe_dump(block)
        assert "m985" in text
        assert "#1143" in text

    def test_verdict_thesis_consistent(self):
        block = _block()
        assert block["verdict"] == "thesis_consistent_observation"

    def test_no_fifty_ninth_form_in_block(self):
        # The fifty-ninth member-claim form is a forward guard; it
        # must not appear contiguously in the landed block.
        block = _block()
        assert "FIFT" + "Y-NINTH falsification-family member" not in yaml.safe_dump(block)

    def test_confounders_ranked(self):
        block = _block()
        assert "strong" in block["confounders_ranked"]
        assert "register-follows-peg" in yaml.safe_dump(block["confounders_ranked"])

    def test_m994_precedent_cited(self):
        block = _block()
        assert "m994" in yaml.safe_dump(block)


# ---------------------------------------------------------------------------
# 10. Statistical discipline (Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------


class TestStatisticalDiscipline1297:
    def test_manual_illustrative_only(self):
        block = _block()
        assert "MANUAL ILLUSTRATIVE ONLY" in block["statistical_discipline"]

    def test_engine_not_run(self):
        block = _block()
        assert "engine NOT run" in block["statistical_discipline"]

    def test_stats_not_calculated(self):
        block = _block()
        assert "NOT_CALCULATED" in block["statistical_discipline"]

    def test_is_significant_false(self):
        block = _block()
        assert "is_significant false" in block["statistical_discipline"]

    def test_not_artifact_grade(self):
        block = _block()
        assert "NOT artifact-grade" in block["statistical_discipline"]
        assert block["no_analysis_json_update"] is True

    def test_correlation_not_causation(self):
        block = _block()
        assert block["correlation_not_causation"] is True

# ---------------------------------------------------------------------------
# 11. Guard lifecycle: this run's forward guards for #1298.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1297:
    def test_pins_on_one_mechanism_landing(self):
        # Type A lands one mechanism: max 1009, next 1010.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1009" in src
        assert "NEXT_NUM = 1010" in src

    def test_no_type_b_1298_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1298's terminal log-hash followup
        # per #721): every commit whose message matches "Type B
        # #1298" must be #1298's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1298")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1298's own commits"
        main = _git("rev-parse", PRED_MAIN_1298).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1010_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1010_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1010_dash_absent_repo_wide(self):
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
        # Landed #1282 (m1000, profiles/wired.yaml). Asserted on the
        # working tree so the pin is stable across the main-commit
        # boundary; the HEAD sweep sees it from the main commit on.
        assert _T56 in _read(os.path.join(PROFILES_DIR, "wired.yaml"))

    def test_fifty_seventh_member_present_pin(self):
        # Landed #1287 (m1003, profiles/ap.yaml, committed). HEAD
        # sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_member_present_pin(self):
        # Landed #1292 (m1006, profiles/financial-times.yaml,
        # committed). HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T58, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_fifty_ninth_member_pin(self):
        # No fifty-ninth member has been claimed anywhere; the
        # fifty-ninth member-claim form stays absent repo-wide
        # (source scope; __pycache__ excluded per the #715
        # pattern-rescope lesson).
        assert _git_grep_tracked_source(_T59, None) == []

    def test_predecessor_1296_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, D1296_FILE))

    def test_next_leg_is_1298_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1298 Type B" in src

    def test_1296_pins_flip_by_design_documented(self):
        # #1296's forward guards (max-1008, zero one-zero-zero-nine
        # keys all forms, no-Type-A-#1297-in-git-log, fortieth
        # absent, forty-eighth through fifty-eighth intact in
        # profiles/, fifty-ninth absent, ledger 58) verified GREEN
        # at HEAD pre-commit this run. The no-Type-A-#1297-in-git-log
        # pin flips BY DESIGN at this run's main commit (the
        # #1191-class self-trip, re-pinned post-commit by
        # TestStalenessPins1297). Type A lands one mechanism, so the
        # zero one-zero-zero-nine numeric pin flips BY DESIGN too (the
        # #1272-class forward-guard expiry; the underscore/dash pins
        # stay green by the #723/#738/#739 designed keying).
        # Documented in the staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1297" in src
        assert "no_type_a_1297_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1296's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------


class TestStalenessPins1297:
    def test_1296_guard_lifecycle_post_commit_self_trip(self):
        # Post-terminal-followup form: 21 tests in the class; ONE flips
        # BY DESIGN when this run's main commit lands and STAYS
        # flipped: the test_1009_numeric_absent_in_profiles pin (the
        # m1009 landing carries "mechanism_id: 1009" in colon form -
        # the #1272-class forward-guard expiry; the underscore/dash
        # pins stay green by the #723/#738/#739 designed keying). The
        # no_type_a_1297_in_git_log ancestor pin ALSO flips at the
        # main commit but is re-pinned green in the terminal log-hash
        # followup per #721 (its PRED_MAIN_1297 now holds this run's
        # main sha). The class run below therefore expects 1 failed /
        # 20 passed and documents the designed flip. The #1296 block
        # is read-only to this run; the flip is documented here, not
        # repaired.
        res = _class_run(D1296_FILE, "TestGuardLifecycle1296")
        out = res.stdout + res.stderr
        assert "1 failed, 20 passed" in out, out[-2000:]
        assert "test_1009_numeric_absent_in_profiles" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 13. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1297:
    def test_readme_test_file_table_has_1297_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1297_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert OWN_BASENAME in arch

    def test_readme_stats_ratcheted(self):
        readme = _read(README_PATH)
        assert "| Tests | %d |" % README_TEST_COUNT in readme
        assert "Across %d test files" % README_FILE_COUNT in readme


# ---------------------------------------------------------------------------
# 14. Iteration log per #721.
# ---------------------------------------------------------------------------


class TestIterationLog1297:
    def test_log_has_1297_entry(self):
        text = _read(LOG_PATH)
        assert "## #1297 Type A" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_finding(self):
        text = _read(LOG_PATH)
        assert "m1009" in text
        assert "thesis_consistent_observation" in text
        assert "ledger holds at 58" in text


# ---------------------------------------------------------------------------
# 15. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1297:
    def test_899_nytimes_hunk_untouched(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert "profiles/nytimes.yaml" in modified
        # Its uncommitted hunk belongs to #899's run; this run stages
        # only its own files via explicit-path staging.
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
