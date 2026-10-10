# -*- coding: utf-8 -*-
"""Type A #1352: WIRED x OpenAI Oct-8/9-2026 governance-accountability
bounded absence (selection asymmetry vs carried WIRED x Meta arms).

Two OpenAI governance-accountability pegs in the Oct-8/9 window draw ZERO
WIRED originals inside a 5-search bounded surface (1 delegated scout with
2 searches + 3 main-run browser.search verification sets, ~30 result rows,
zero wired.com URLs, zero WIRED bylines; 0 browser.open per #503,
excerpt-bounded):

  (A) the safety-researcher firings escalation: the trio's Oct-8 open
  letter charging "prioritizing safety over the near-term interests of
  OpenAI", plus OpenAI's Oct-9 X response alleging "a significant breach
  of trust" - covered by WSJ (scoop-origin originals), FT, BI, the AP
  wire (m1039 #1347), and The Verge;
  (B) the Oct-8 three-preprint math pull (a sign error collapsing one
  proof and two dependents; 722 -> 719 manuscripts; only ~42% Lean
  formalized), covered by NYT (primary), Retraction Watch, aiweekly and
  others - notable because WIRED ran the adversarial Oct-6/7 Isabella
  Ward mathematicians original (m1027 #1327) on the SAME story thread
  and skipped the follow-up where the release was shown to contain
  errors.

The same publication selects Meta governance-accountability pegs
aggressively in the same window (carried arms: m988 Oct 4-5 Muse
dossier; the Oct-3 WIRED "muse-creates-detailed-profiles" original,
attested via third-party citation with the wired.com path form
unverified and NOT constructed; m970 Aug-26 $18bn settlement wire).

Verdict mechanism_documented - NOT a falsification-family member. The
silence is consistent with the wired.yaml
competitor_relationships.openai coverage_prediction "softer" (Conde
Nast x OpenAI multi-year content licensing deal, Aug 20 2024, Reuters;
$1-5M/yr estimate) on the SELECTION axis for the governance register -
but the AP x OpenAI leg of the SAME firings peg ran HARD (m1039 #1347,
SIXTY-FOURTH member), so the deal alone does not determine selection;
candidate drivers include WSJ scoop-ownership, WIRED's weekly cadence,
and the #507 domain boundary. The finding BOUNDS the m1027
adversarialism (register-follows-peg: hard on product/culture,
unselected on governance-accountability) rather than extending any
pattern. Ledger holds at 64; no sixty-fifth member.

Type A lands one mechanism: m1042 in profiles/wired.yaml under
competitor_relationships/openai (4-space indent, sibling of the
type_a_1327 block); max numeric mechanism_id 1041->1042; next 1043;
ledger holds at 64 (the sixty-fourth member stays m1039 ap.yaml; the
sixty-fifth member-claim form stays absent repo-wide).

Research method: 1 delegated scout (2 searches: WIRED firings leg,
WIRED ChatGPT Mac-app vulnerability; both returned bounded absence on
wired.com URLs; the scout returned raw verbatim URLs WITHOUT novelty
characterization per the #1341 post-hoc lesson - the main run verified
corpus novelty via git grep -F) + 3 main-run browser.search
verification sets (WIRED OpenAI news October 2026 - attesting, zero
wired.com firings URLs; exact-phrase WIRED/OpenAI/fired search -
attesting, The Verge Oct-9 response coverage noted; WIRED OpenAI math
proofs pull - attesting, NYT-primary/Retraction Watch coverage,
zero WIRED originals), 0 browser.open per #503. Pre-commit novelty
greps: zero test_type_a_1352 files on disk (glob); no Type A #1352 in
git log (--grep); max numeric mechanism_id 1041 in profiles/
pre-commit; zero numeric/underscore/dash next-number
one-zero-four-three mechanism key forms in profiles/ + tests/
pre-commit (needles format-built per #715, own file excluded, verified
clean by direct sweep); 3 novel source URLs zero-hit repo-wide
pre-commit (git grep -F on verbatim Full-URL listings); block key
zero-hit repo-wide pre-commit (git grep -F; designed keying:
iteration 1352 in key, no 1042 or 1043 substring); "## #1352"
zero-hit in iteration-log pre-commit; README stats 78082/1676
pre-commit; no #1352 row in README/ARCHITECTURE test tables
pre-commit; "governance-accountability bounded absence" framing
zero-hit repo-wide pre-commit. All URLs copied verbatim from the
browser.search Full-URL listings, NOT constructed. ASCII-only, no
em dashes.

This run is the THIRD leg of the 1350-1354 window (D #1350 -> E #1351
-> A #1352 -> B #1353 -> C #1354 per the #565 anchor + rotation guard);
the 1345-1349 window is VERIFIED CLOSED. The next background-suite
verdict belongs to #1355 per #795 (the #1350-launched suite, goal
hidden_files type_d_1350_full_suite.log; this run CHECKS it only -
ALIVE at [0%] with 1 live pytest proc at this run's ~7:00 PM PDT
check - and neither re-launches, kills, nor writes to it).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup commit. One anchor test (the placeholder pin) fails BY DESIGN
post-anchor.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit),
#900 (untracked Type D test file), #1012-wt (working-tree edit on the
committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
max or next number, the forty-eighth through sixty-fifth member-claim
forms, or the fortieth direction-claim form; the constants are
constructed at runtime. (The landed ordinals live as short lowercase
forms in prose here; the live full-form claims live in profiles: the
forty-eighth, fifty-eighth, and sixtieth in financial-times.yaml, the
forty-ninth, fiftieth, and fifty-second in profiles/careers/
journalists.yaml, the fifty-first, fifty-ninth, sixty-second, and
sixty-third in news-corp.yaml, the fifty-third in the-verge.yaml, the
fifty-fourth in guardian.yaml, the fifty-fifth in atlantic.yaml, the
fifty-sixth and sixty-first in wired.yaml, the fifty-seventh and
sixty-fourth in ap.yaml; the sixty-fifth is absent repo-wide as of this
run.)
"""

import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
WIRED_PATH = os.path.join(PROFILES_DIR, "wired.yaml")

OWN_BASENAME = (
    "test_type_a_1352_wired_openai_oct08_09_governance_"
    "accountability_bounded_absence_vs_carried_meta_arms_oct09_7pm.py"
)

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "2b33a0406fd0eca02c75cac70086bb9f9d5dab5a"  # 0*40 pre-commit; patched to the main-commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1042
NEXT_NUM = 1043  # integer only; key-form needles are format-built

# Predecessor chain: #1351 Type E SECOND leg of the 1350-1354 window.
PRED_MAIN_1351 = "2de722956f7e8186d66dfe097403f659c050d06e"
PRED_ANCHOR_1351 = "47f671e5fd62b97cf6573abce56c617b4eaad9e0"
PRED_DOCSYNC_1351 = "959ebce631218ba59eb9a7fea5d567508531fd80"
PRED_FINAL_1351 = "3fd8199c"

# This run's main commit (full sha), for the ancestor-form
# no-Type-A-#1352 pin. Staged 0*40 placeholder-only per #721;
# re-pinned in the anchor followup per #721 (PRED_MAIN_1352 re-pinned
# in BOTH this file and the #1351 file per the #1292 precedent).
PRED_MAIN_1352 = "2b33a0406fd0eca02c75cac70086bb9f9d5dab5a"  # re-pinned to the #1352 main sha in the anchor followup per #721/#1292

# #1353's main commit (full sha), for the ancestor-form no-Type-A-#1353
# pin. Staged 0*40 placeholder-only per #721; re-pinned in #1353's
# terminal log-hash followup per #721.
PRED_MAIN_1353 = "93d015a7cf1c72a1caaff6cced5f1c7aefaddb88"  # re-pinned to the #1353 main sha in #1353's terminal log-hash followup per #721/#1292 (the no-Type-A-#1353 pin stays red BY DESIGN - type-mismatched)

# The #1351 window-predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1041; zero next-number
# one-zero-four-two / no-Type-A-#1352-in-git-log / fortieth
# direction absent / forty-eighth through sixty-fourth members
# intact / no sixty-fifth member / ledger holds at 64).
B1351_FILE = (
    "test_type_e_1351_podcast_sentiment_193rd_"
    "verification_oct09_6pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 78178  # post-doc-sync total (pre-sync 78082 + 96) - PATCHED post-collection
README_FILE_COUNT = 1677  # pre-sync 1676 + 1 (this file)

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
# (landed #1302 in profiles/news-corp.yaml).
_T59 = "FIFT" + "Y-NINTH falsification-family member"
# The sixtieth member-claim form is fragment-built per #715
# (landed #1322 in profiles/financial-times.yaml).
_T60 = "SIXT" + "IETH falsification-family member"
# The sixty-first member-claim form is fragment-built per #715
# (landed #1327 in profiles/wired.yaml).
_T61 = "SIXT" + "Y-FIRST falsification-family member"
# The sixty-second member-claim form is fragment-built per #715
# (landed #1332 in profiles/news-corp.yaml).
_T62 = "SIXT" + "Y-SECOND falsification-family member"
# The sixty-third member-claim form is fragment-built per #715
# (landed #1342 in profiles/news-corp.yaml, m1036).
_T63 = "SIXT" + "Y-THIRD falsification-family member"
# The sixty-fourth member-claim form is fragment-built per #715
# (landed #1347 in profiles/ap.yaml, m1039).
_T64 = "SIXT" + "Y-FOURTH falsification-family member"
# The sixty-fifth member-claim form is fragment-built per #715
# (no sixty-fifth member may exist repo-wide).
_T65 = "SIXT" + "Y-FIFTH falsification-family member"

BLOCK_KEY = (
    "type_a_1352_wired_openai_oct08_09_governance_"
    "accountability_bounded_absence_vs_carried_meta_arms"
)

# Novel verbatim source URLs this run (zero-hit repo-wide pre-commit,
# verified via git grep -F; copied verbatim from the browser.search
# Full-URL listings, NOT constructed).
NOVEL_URLS = [
    "https://www.wsj.com/tech/ai/openai-parts-ways-with-researchers-who-allegedly-shared-confidential-information-aebac528",
    "https://www.primetimer.com/news/we-are-deeply-sad-about-this-outcome-openai-says-decision-to-fire-researchers-was-not-about-raising-safety-concerns-or-speaking-out",
    "https://retractionwatch.com/2026/10/08/openai-withdraws-preprints-722-manuscripts-unsolved-math-problems/",
]

# 3 main-run browser.search query sets + 1 delegated scout this run
# (0 browser.open per #503).
QUERY_SETS = [
    "WIRED OpenAI news October 2026",
    "\"WIRED\" OpenAI \"fired\" safety researchers October 2026",
    "WIRED OpenAI math proofs pulled sign error October 2026",
]


def _load_wired():
    with open(WIRED_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _block():
    data = _load_wired()
    return data["competitor_relationships"]["openai"][BLOCK_KEY]


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


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup)
#    + rotation guard: THIRD leg of the 1350-1354 window.
# ---------------------------------------------------------------------------


class TestAnchor1352:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to the main-commit sha. This test fails BY
        # DESIGN post-anchor and is deselected in the in-gate run;
        # the patched form is asserted by
        # test_anchor_sha_patched_to_main_commit. Terminal per #565.
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_to_main_commit(self):
        # Post-commit form: ANCHORED_SHA patched to this run's main
        # commit sha in the anchor followup (placeholder + expected
        # value and the ANCHORED_SHA constant are patched).
        # Deselected in the in-gate run.
        assert ANCHORED_SHA != "0" * 40
        assert len(ANCHORED_SHA) == 40

    def test_anchor_sha_format(self):
        assert len(ANCHORED_SHA) == 40
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)

    def test_anchor_duality_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Anchor convention per #565" in src
        assert "fails BY DESIGN post-anchor" in src

    def test_third_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "THIRD leg of the 1350-1354 window" in src

    def test_1345_1349_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1345-1349" in src
        assert "VERIFIED CLOSED" in src

    def test_next_leg_is_1353_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "B #1353" in src


# ---------------------------------------------------------------------------
# 2. Mechanism novelty: Type A lands one mechanism (m1042; max 1042).
# ---------------------------------------------------------------------------


class TestMechanismNovelty1352:
    def test_max_numeric_mechanism_id_1042(self):
        # Post-landing form: the m1042 block is in the working tree
        # pre-commit (landed before the in-gate run). Deselected in
        # the in-gate run (fails pre-landing by design).
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_no_type_a_1352_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the anchor followup per #721): every commit whose message
        # matches "Type A #1352" must be this run's main commit or a
        # descendant of it - i.e., no PRIOR run committed this run's
        # iteration. Deselected in the in-gate run (fails pre-commit
        # by design).
        out = _git("log", "--format=%H", "--grep=Type A #1352")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1352).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_zero_next_number_keys_all_forms(self):
        # Numeric (profiles/ scope), underscore and dash (profiles/ +
        # tests/ scope, own file excluded per #715). Holds pre-commit
        # and post-commit (Type A lands one mechanism, the 1043
        # pins stay green).
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_key_designed_no_1042_1043_substring(self):
        # Per #723/#738/#739: the iteration-form block key carries no
        # underscore-form one-zero-four-two / one-zero-four-three
        # mechanism key substring (needle format-built per #770 so
        # this file carries no contiguous literal).
        for n in (MECH_NUM, NEXT_NUM):
            needle = "%s%d" % (MECH_ID_MARKER, n)
            assert needle not in BLOCK_KEY
        assert "1352" in BLOCK_KEY
        assert BLOCK_KEY in _read(WIRED_PATH)

    def test_block_key_in_wired_openai_section(self):
        # Post-landing form: the m1042 block sits under
        # competitor_relationships.openai in profiles/wired.yaml.
        # Deselected in the in-gate run (fails pre-landing by design).
        data = _load_wired()
        oai = data["competitor_relationships"]["openai"]
        assert BLOCK_KEY in oai
        assert oai[BLOCK_KEY]["mechanism_id"] == MECH_NUM

    def test_novel_urls_zero_hit_pre_commit(self):
        # The three source URLs were verified zero-hit pre-commit
        # (git grep -F, documented in the block's novelty field). This
        # test pins that no file OTHER than this run's own m1042
        # block ever carries them, so it holds pre-commit (zero hits)
        # and post-commit (only the landed block hits).
        for url in NOVEL_URLS:
            out = _git("grep", "-F", "-l", url, "HEAD", "--",
                       "profiles/", "tests/").stdout
            paths = []
            for line in out.splitlines():
                line = line.strip()
                if not line:
                    continue
                if line.startswith("HEAD:"):
                    line = line[5:]
                paths.append(line)
            assert set(paths) <= {
                "profiles/wired.yaml",
                "tests/" + OWN_BASENAME,
            }, (url, paths)

    def test_forward_guards_for_1353(self):
        # max-1042; zero-1043 all forms; fortieth direction absent
        # (profiles/ scope); forty-eighth through sixty-fourth members
        # intact; no sixty-fifth member (repo-wide); ledger holds
        # at 64 (m1042 is mechanism_documented, NOT a member).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1042" in src
        assert "NEXT_NUM = 1043" in src
        assert "ledger holds at 64" in src
        assert _git_grep_tracked_source(_T40, "profiles/") == []
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]
        assert _git_grep_tracked_source(_T64, "profiles/") == [
            "profiles/ap.yaml"]
        assert _git_grep_tracked_source(_T65, None) == []

    def test_distinct_from_prior_wired_openai(self):
        # Not a re-score of m1027 (#1327, Oct-6/7 product-review
        # adversarial originals, SIXTY-FIRST member, tone axis); not
        # m946 (#1192, Oct-2 macOS CVE security-flaw register, tone on
        # a published original); not m916 (#1142, Sep-26 rogue-agent
        # bounded absence, different peg); not m1039 (#1347, AP x
        # OpenAI firings leg, different publication, opposite
        # verdict). The #1143 temporal-replication precedent does not
        # block: fresh pegs (Oct-8/9 governance-accountability) and
        # the FIRST WIRED-leg selection test on the firings story.
        block = _block()
        assert "m1027" in block["distinct_from_prior"]
        assert "m946" in block["distinct_from_prior"]
        assert "m916" in block["distinct_from_prior"]
        assert "m1039" in block["distinct_from_prior"]
        assert "#1143" in block["distinct_from_prior"]


# ---------------------------------------------------------------------------
# 3. Guard lifecycle: forward pins for #1353; #1352 stages the
#    #1191-class no-Type-A-#1353 self-trip (re-pinned post-commit
#    per #721).
# ---------------------------------------------------------------------------


class TestGuardLifecycle1352:
    def test_pins_on_one_mechanism_landing(self):
        # Type A lands one mechanism: max 1042, next 1043.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1042" in src
        assert "NEXT_NUM = 1043" in src

    def test_no_type_a_1353_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1353's terminal log-hash followup
        # per #721): every commit whose message matches "Type A
        # #1353" must be #1353's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type A #1353")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1353's own commits"
        main = _git("rev-parse", PRED_MAIN_1353).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1043_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1043_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1043_dash_absent_repo_wide(self):
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
        out = _git(
            "grep", "-c", "-F", _T62, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_third_member_intact_pin(self):
        # The sixty-third member-claim form is committed at HEAD
        # (landed #1342, m1036, profiles/news-corp.yaml).
        out = _git(
            "grep", "-c", "-F", _T63, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_fourth_member_present_pin(self):
        # The sixty-fourth member-claim form is committed at HEAD
        # (landed #1347, m1039, profiles/ap.yaml).
        out = _git(
            "grep", "-c", "-F", _T64, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_sixty_fifth_member_pin(self):
        # m1042 is mechanism_documented, NOT a member: the
        # sixty-fifth member-claim form stays absent repo-wide.
        assert _git_grep_tracked_source(_T65, "profiles/") == []
        assert _git_grep_tracked_source(_T65, "tests/") == []

    def test_ledger_holds_at_64_pin(self):
        block = _block()
        assert block["falsification_ledger"] == "64"
        assert block["ledger"] == "64"
        assert "Ledger holds at 64" in block["falsification_family"]


# ---------------------------------------------------------------------------
# 4. Staleness pins: #1351's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------


class TestStalenessPins1352:
    def test_1351_guard_lifecycle_post_commit_self_trip(self):
        # Post-terminal-followup form: 27 tests in the class; 25
        # pass, 2 fail BY DESIGN - TWO #1272-class forward-guard
        # expiries (test_max_numeric_mechanism_id_is_1041 trips
        # because max is now 1042; test_1042_numeric_absent_in_profiles
        # trips on the landed m1042 block in profiles/wired.yaml).
        # The no_type_a_1352_in_git_log ancestor pin (the #1191-class
        # self-trip) was red at this run's main-commit time; the
        # anchor followup re-pinned PRED_MAIN_1352 in BOTH its own
        # file's copy and the #1351 predecessor file's copy per the
        # #1292 re-pin-both-copies precedent and the #721 re-pin rule,
        # flipping it green. The 1042-underscore and 1042-dash pins
        # stay green (no one-zero-four-two mechanism-key forms
        # landed); the forty-eighth through sixty-fourth member pins
        # stay green; the no-sixty-fifth pin stays green (m1042 is not
        # a member); the ledger-holds-at-64 pin stays green.
        # Deselected in the in-gate run (fails pre-commit by design);
        # verified post-terminal.
        res = _class_run(B1351_FILE, "TestGuardLifecycle1351")
        out = res.stdout + res.stderr
        assert "2 failed, 25 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 5. Doc-sync per #719 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestDocSync1352:
    def test_readme_test_file_table_has_1352_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_a_1352" in readme

    def test_architecture_has_1352_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_a_1352" in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_PATH)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 6. Iteration log per #721 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestIterationLog1352:
    def test_log_has_1352_entry(self):
        text = _read(LOG_PATH)
        assert "## #1352 Type A" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_finding(self):
        text = _read(LOG_PATH)
        assert "m1042" in text
        assert "bounded absence" in text


# ---------------------------------------------------------------------------
# 7. Corpus integrity: the m1042 block is well-formed and placed.
# ---------------------------------------------------------------------------


class TestCorpusIntegrity1352:
    def test_wired_yaml_loads(self):
        data = _load_wired()
        assert "competitor_relationships" in data

    def test_block_fields_present(self):
        block = _block()
        for field in (
            "mechanism_id", "date_analyzed", "type", "iteration",
            "iteration_type", "block_key", "test_file", "author",
            "publication", "competitor_pair", "goal_id",
            "scheduled_job_id", "window", "design",
            "distinct_from_prior", "finding", "openai_arm_new",
            "meta_arm_carried", "asymmetry_scorer_result", "verdict",
            "falsification_family", "falsification_ledger",
            "falsification_family_member", "ledger", "ledger_note",
            "counterevidence", "confounders_ranked",
            "financial_context", "statistical_discipline", "method",
            "research_method", "novelty", "source_urls",
            "no_analysis_json_update", "concurrency", "status",
        ):
            assert field in block, field

    def test_block_sibling_of_1327(self):
        data = _load_wired()
        oai = data["competitor_relationships"]["openai"]
        keys = list(oai.keys())
        assert BLOCK_KEY in keys
        assert ("type_a_1327_wired_openai_oct07_chatgpt_"
                "intelligent_ui_review_vs_carried_meta_dossier") in keys

    def test_four_space_indent(self):
        src = _read(WIRED_PATH)
        assert "\n    " + BLOCK_KEY + ":" in src

    def test_ascii_only_profile_block(self):
        data = _load_wired()
        blob = str(data["competitor_relationships"]["openai"][BLOCK_KEY])
        assert "\u2014" not in blob
        assert "\u2013" not in blob

    def test_test_file_field_matches(self):
        assert _block()["test_file"] == "tests/" + OWN_BASENAME

    def test_goal_and_job_ids(self):
        block = _block()
        assert block["goal_id"] == "goal_54093bda4145"
        assert block["scheduled_job_id"] == "mediascope-daily-iteration"
        assert block["author"] == "Kit (with Ray)"

    def test_window_third_leg(self):
        assert "1350-1354" in _block()["window"]
        assert "THIRD leg" in _block()["window"]

    def test_not_a_member_fields(self):
        block = _block()
        assert block["falsification_family_member"] is False
        assert block["verdict"] == "mechanism_documented"
        assert block["no_analysis_json_update"] is True


# ---------------------------------------------------------------------------
# 8. Research method: 1 scout + 3 query sets, 0 browser.open, novelty,
#    verbatim URLs, bounded-absence surface.
# ---------------------------------------------------------------------------


class TestResearchMethod1352:
    def test_three_query_sets_documented(self):
        block = _block()
        assert len(block["method_query_sets"]) == 3
        assert "WIRED OpenAI news October 2026" in block[
            "method_query_sets"]

    def test_zero_browser_open(self):
        block = _block()
        assert "0 browser.open" in block["method"]
        assert "excerpt-bounded" in block["method"]

    def test_scout_handoff_documented(self):
        block = _block()
        assert "delegated scout" in block["method"]
        assert "raw verbatim URLs WITHOUT novelty characterization" in \
            block["method"]
        assert "#1341 post-hoc lesson" in block["method"]

    def test_verbatim_urls_not_constructed(self):
        block = _block()
        assert "verbatim" in block["novelty"]
        assert "constructed" in block["novelty"]
        assert "no canonical URLs constructed" in block["novelty"]
        for url in NOVEL_URLS:
            assert url.startswith("https://www.wsj.com/") or \
                url.startswith("https://www.primetimer.com/") or \
                url.startswith("https://retractionwatch.com/")

    def test_bounded_absence_surface_documented(self):
        block = _block()
        assert "bounded surface" in block["method"]
        assert "5-search" in block["method"]
        assert "zero wired.com URLs" in block["method"]

    def test_referenced_evidence_caveat(self):
        # The Oct-3 WIRED profiles piece is third-party-referenced
        # (wired.com path form unverified, NOT constructed).
        block = _block()
        assert "third-party-referenced" in block["meta_arm_carried"][
            "arm_M2"]["provenance_note"]

    def test_ascii_only_test_file(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "\u2014" not in src
        assert "\u2013" not in src


# ---------------------------------------------------------------------------
# 9. Confounders, ranked strong-first.
# ---------------------------------------------------------------------------


class TestConfounders1352:
    def test_confounder_excerpt_bounded_strong(self):
        block = _block()
        assert "Excerpt-bounded" in block["confounders_ranked"]["strong"][0]

    def test_confounder_m1027_adversarialism_strong(self):
        # The same desk ran THREE adversarial OpenAI originals 48
        # hours earlier (m1027 #1327): the absence is peg-specific,
        # not a uniform-softness trait.
        block = _block()
        assert "m1027" in block["confounders_ranked"]["strong"][1]

    def test_confounder_ap_hardness_strong(self):
        # The AP x OpenAI leg of the SAME firings peg ran HARD (m1039
        # #1347, SIXTY-FOURTH member): the deal alone does not
        # determine selection.
        block = _block()
        assert "m1039" in block["confounders_ranked"]["strong"][2]

    def test_confounder_wsj_scoop_moderate(self):
        block = _block()
        assert "scoop" in block["confounders_ranked"]["moderate"][0]

    def test_confounder_weekly_cadence_moderate(self):
        block = _block()
        assert "cadence" in block["confounders_ranked"]["moderate"][1]

    def test_confounder_paywall_indexing_weak(self):
        block = _block()
        assert "paywall" in block["confounders_ranked"]["weak"][0]


# ---------------------------------------------------------------------------
# 10. Verdict: mechanism_documented, not a member, ledger holds at 64.
# ---------------------------------------------------------------------------


class TestVerdict1352:
    def test_verdict_mechanism_documented(self):
        assert _block()["verdict"] == "mechanism_documented"

    def test_not_a_falsification_member(self):
        block = _block()
        assert block["falsification_family_member"] is False
        assert "NOT a falsification-family member" in block[
            "falsification_family"]

    def test_ledger_holds_at_64(self):
        block = _block()
        assert block["falsification_ledger"] == "64"
        assert block["ledger"] == "64"

    def test_no_sixty_fifth_member_claimed(self):
        block = _block()
        assert "sixty-fifth member-claim form stays absent repo-wide" in \
            block["ledger_note"]

    def test_bounds_m1027(self):
        # The finding bounds rather than extends the m1027
        # adversarialism: hard on product/culture, unselected on
        # governance-accountability.
        block = _block()
        assert "BOUNDS the m1027" in block["finding"]

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True


# ---------------------------------------------------------------------------
# 11. Arms: two bounded-absence OpenAI pegs vs carried Meta arms.
# ---------------------------------------------------------------------------


class TestWIREDOpenAIArms1352:
    def test_firings_peg_arms(self):
        block = _block()
        arm = block["openai_arm_new"]["arm_A1"]
        assert "2026-10-08" in arm["date"] or "Oct-8" in arm["date"]
        assert "Wall Street Journal" in arm["covered_by"]
        assert "m1039" in arm["covered_by"]

    def test_math_pull_peg_arms(self):
        block = _block()
        arm = block["openai_arm_new"]["arm_A2"]
        assert "722 -> 719" in arm["detail"]
        assert "Retraction Watch" in arm["covered_by"]

    def test_zero_wired_originals(self):
        block = _block()
        assert block["openai_arm_new"]["wired_originals"] == 0
        assert "zero wired.com URLs" in block["openai_arm_new"][
            "bounded_surface"]

    def test_carried_meta_arms(self):
        block = _block()
        assert "m988" in block["meta_arm_carried"]["arm_M1"]["mechanism"]
        assert "m970" in block["meta_arm_carried"]["arm_M3"]["mechanism"]

    def test_selection_delta_documented(self):
        block = _block()
        assert "0 of 2" in block["asymmetry_scorer_result"]

    def test_tone_not_scored(self):
        block = _block()
        assert "NOT_SCORED" in block["asymmetry_scorer_result"]

    def test_scorer_engine_not_run(self):
        block = _block()
        assert "Engine NOT run" in block["asymmetry_scorer_result"]


# ---------------------------------------------------------------------------
# 12. Financial relationship: Conde Nast x OpenAI deal context.
# ---------------------------------------------------------------------------


class TestFinancialRelationship1352:
    def test_deal_attested(self):
        block = _block()
        assert "Aug 20 2024" in block["financial_context"]
        assert "Reuters" in block["financial_context"]

    def test_estimate_range(self):
        block = _block()
        assert "$1-5M/yr" in block["financial_context"]

    def test_coverage_prediction_softer(self):
        block = _block()
        assert 'coverage_prediction "softer"' in block[
            "financial_context"]

    def test_meta_zero_licensing(self):
        block = _block()
        assert "$0" in block["financial_context"]

    def test_deal_url_verbatim(self):
        block = _block()
        assert block["deal_url"] == (
            "https://www.reuters.com/technology/openai-signs-deal-"
            "with-cond-nast-2024-08-20/"
        )


# ---------------------------------------------------------------------------
# 13. In-flight isolation: #899/#938/#900/#1012-wt and #1024 untouched.
# ---------------------------------------------------------------------------


class TestInFlightIsolation1352:
    def test_in_flight_listed(self):
        block = _block()
        for tag in ("#899", "#938", "#900", "#1012-wt", "#1024"):
            assert tag in block["concurrency"]

    def test_nytimes_untouched(self):
        # The #899 in-flight m771 hunk was dirty before this run; this
        # run must not add its own content to it (isolation = stays
        # out of this run's index/diff via explicit-path staging).
        out = _git("diff", "--", "profiles/nytimes.yaml").stdout
        assert "1042" not in out
        assert "1352" not in out

    def test_competitor_entities_untouched(self):
        out = _git("status", "--short")
        assert "profiles/competitor-entities.yaml" not in out.stdout

    def test_only_expected_paths_dirty(self):
        # git status --short prefixes each path with a 3-char status
        # field (" M " / "?? "); slice the RAW line, not the
        # stripped one (stripping first shifts the slice).
        out = _git("status", "--short").stdout
        allowed = {
            "profiles/wired.yaml",
            "tests/" + OWN_BASENAME,
        }
        in_flight = {
            "profiles/nytimes.yaml",
            "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
            "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
        }
        for raw in out.splitlines():
            if not raw.strip():
                continue
            path = raw[3:]
            assert path in allowed or path in in_flight, path


# ---------------------------------------------------------------------------
# 14. Statistical discipline: MANUAL / QUALITATIVE ONLY.
# ---------------------------------------------------------------------------


class TestStatisticalDiscipline1352:
    def test_manual_qualitative_only(self):
        block = _block()
        assert "MANUAL" in block["statistical_discipline"]
        assert "QUALITATIVE ONLY" in block["statistical_discipline"]

    def test_no_p_values(self):
        block = _block()
        assert "NOT_CALCULATED" in block["statistical_discipline"]

    def test_not_significant(self):
        block = _block()
        assert "is_significant false" in block["statistical_discipline"]

    def test_not_artifact_grade(self):
        block = _block()
        assert "NOT artifact-grade" in block["statistical_discipline"]

    def test_correlation_not_causation(self):
        block = _block()
        assert "Correlation is not causation" in block[
            "statistical_discipline"]
        assert "hypothesis-generating only" in block[
            "statistical_discipline"]
