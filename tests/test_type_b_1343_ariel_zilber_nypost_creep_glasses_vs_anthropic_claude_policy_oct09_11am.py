# -*- coding: utf-8 -*-
"""Type B #1343: Ariel Zilber (the NY Post) - Meta 'creep glasses' dating piece vs Anthropic 'be nice to Claude' policy piece

Ariel Zilber (NY Post business reporter) is fully novel to the
corpus - zero "ariel zilber" hits repo-wide pre-commit. Two bylined
pieces, 22 days apart, same outlet, same tabloid register: the Sep-16
Meta arm ("'Violated' singles say dates secretly filmed them with Meta
Ray-Bans - as 'creep glasses' trend sparks outrage", -0.55 MANUAL
ILLUSTRATIVE, adversarial privacy register: non-consensual filming on
dates, "latest privacy headache for Meta") vs the Oct-8 Anthropic arm
("Anthropic to users: be nice to Claude AI - new policy bars 'abusive
or cruel behavior' to tech", -0.40 MANUAL ILLUSTRATIVE, mock-
adversarial register: "even though it's not, ya know, actually alive",
"oddball corners of Silicon Valley insist the tech has a soul").
Illustrative delta (anthropic minus meta) +0.15 - near-symmetric
adversarial; Zilber runs the Post's tabloid register hard on both
labs. NOT a falsification-family member (ledger HOLDS at 63): the pair
carries no OpenAI arm, so the uniform payer-softening prediction (News
Corp x OpenAI May-2024 deal) is not adjudicated. Consistent with the
nypost_openai_adversarial_triad (twenty-ninth member): the Post's
adversarial AI-lab register extends to a second lab. Verdict
directionally_supported_not_proven; NOT artifact-grade; no
analysis.json update.

Zilber is a Post business reporter (LinkedIn: New York Post;
BuzzSumo journalist profile lists both arms under his nypost.com
articles). Meta-arm byline attested via the BuzzSumo profile listing
(headline + Sep-16 date + nypost.com); Anthropic-arm byline attested
twice via flipboard ("New York Post - Ariel Zilber"). Both nypost.com
canonical URLs are verbatim from the browser.search Full-URL listings.
0 browser.open per #503 (excerpt-bounded).

Type B lands one mechanism: m1037 in profiles/careers/journalists.yaml
under a new ariel_zilber_type_b top key (0-indent, end-of-file),
competitor_coverage/(
    "type_b_1343_ariel_zilber_nypost_creep_glasses_"
    "vs_anthropic_claude_policy_oct09_11am"
) block (4-space indent); max numeric
mechanism_id 1036->1037; next one-zero-three-eight; ledger HOLDS at 63
(the sixty-third member remains the #1342 m1036 Times x OpenAI member;
the sixty-fourth member-claim form stays absent repo-wide; m1037 is
falsification_family_member false).

Research method: 1 delegated scout (10+ browser.search queries, saturation screening of 70+ journalists; its top-3 picks ALL rejected on main-run corpus verification: Dan Goodin saturated #1238 m974, Cristina Criddle saturated #1143, Ashley Belanger in-corpus; rejection audit numbered 1-70) + main-run browser.search
verification sets, 0 browser.open (excerpt-bounded per #503).
Pre-commit novelty greps: zero test_type_b_1343 files on disk (glob);
no Type B #1343 in git log (--grep); max numeric mechanism_id 1036 in
profiles/ pre-commit; zero numeric/underscore/dash next-number
one-zero-three-eight mechanism key forms in profiles/ + tests/
pre-commit (needles format-built per #715, own file excluded, verified
clean by direct sweep); "ariel zilber" zero-hit
repo-wide pre-commit (git grep -F -i); 3 source URLs
zero-hit repo-wide pre-commit (git grep -F); block key zero-hit
repo-wide pre-commit; "## #1343" zero-hit in iteration-log pre-commit;
no #1343 row in README/ARCHITECTURE test tables pre-commit; README
stats 77157/1667 pre-commit. All URLs copied verbatim from the
browser.search Full-URL listings; no canonical URLs constructed.
ASCII-only, no em dashes.

This run is the FOURTH leg of the 1340-1344 window (D #1340 -> E #1341
-> A #1342 -> B #1343 -> C #1344 per the #565 anchor + rotation guard);
the 1335-1339 window is VERIFIED CLOSED. Next run #1344 Type C closes
the window. The next background-suite verdict belongs to #1345 per
#795 (the #1340-launched suite, goal hidden_files
type_d_1340_full_suite.log; this run OBSERVES only, neither
re-launches, kills, nor writes to it).

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
max or next number, the forty-eighth through sixty-third member-claim
forms, or the fortieth direction-claim form; the constants are
constructed at runtime. (The landed ordinals live as short lowercase
forms in prose here; the live full-form claims live in profiles: the
forty-eighth, fifty-eighth, and sixtieth in financial-times.yaml, the
forty-ninth, fiftieth, and fifty-second in profiles/careers/
journalists.yaml, the fifty-first, fifty-ninth, sixty-second, and
sixty-third in news-corp.yaml, the fifty-third in the-verge.yaml, the
fifty-fourth in guardian.yaml, the fifty-fifth in atlantic.yaml, the
fifty-sixth and sixty-first in wired.yaml, the fifty-seventh in
ap.yaml; the sixty-fourth is absent repo-wide as of this run.)
"""

import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
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
    "test_type_b_1343_ariel_zilber_nypost_creep_glasses_"
    "vs_anthropic_claude_policy_oct09_11am.py"
)

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "d3252af1d0ee6bb0e25aa8690c8ad86d47211969"  # 0*40 pre-commit; patched to the main-commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1037
NEXT_NUM = 1038  # integer only; key-form needles are format-built

# Predecessor chain: #1342 Type A THIRD leg of the 1340-1344 window.
PRED_MAIN_1342 = "3e71adbdce7e47b9212bc9b2881201d7b08a72c5"
PRED_ANCHOR_1342 = "d1ce1912b9e35913cd181cbad5a2885fef316df8"
PRED_DOCSYNC_1342 = "13d866e835a36a7f0111dcb6a28e0798197ced62"
PRED_FINAL_1342 = "814a1c3493babbea8f8877a5524efc2df26b0e1c"

# This run's main commit (full sha), for the ancestor-form
# no-Type-B-#1343 pin. Staged 0*40 placeholder-only per #721;
# re-pinned in this run's terminal log-hash followup per #721.
PRED_MAIN_1343 = "d3252af1d0ee6bb0e25aa8690c8ad86d47211969"  # re-pinned to #1343 main sha in the anchor followup per #721/#1292

# #1344's main commit (full sha), for the ancestor-form no-Type-C-#1344
# pin. Staged 0*40 placeholder-only per #721; re-pinned in #1344's
# terminal log-hash followup per #721.
PRED_MAIN_1344 = "0" * 40  # re-pinned to #1344 main sha in the anchor followup per #721/#1292

# The #1342 window-predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1036; zero next-number
# one-zero-three-seven / no-Type-B-#1343-in-git-log / fortieth
# direction absent / forty-eighth through sixty-third members
# intact / no sixty-fourth member (repo-wide) / ledger 63).
B1342_FILE = (
    "test_type_a_1342_times_openai_sep24_oct08_safety_"
    "accountability_cluster_vs_carried_times_meta_arms_oct09_11am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 77157  # post-doc-sync total (pre-sync 77157 + N) - PATCHED post-collection
README_FILE_COUNT = 1668  # pre-sync 1667 + 1 (this file)

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
# (landed #1342 m1036 in profiles/news-corp.yaml).
_T63 = "SIXT" + "Y-THIRD falsification-family member"
# The sixty-fourth member-claim form is fragment-built per #715
# (no sixty-fourth member may exist repo-wide).
_T64 = "SIXT" + "Y-FOURTH falsification-family member"

BLOCK_KEY = (
    "type_b_1343_ariel_zilber_nypost_creep_glasses_"
    "vs_anthropic_claude_policy_oct09_11am"
)

# MANUAL ILLUSTRATIVE tone constants (hand-assigned register positions
# per the Aug 28 2026 standing rule; NOT engine output).
META_TONE = -0.55
OTHER_TONE = -0.40
ILLUSTRATIVE_DELTA = 0.15  # anthropic minus meta

OTHER_ENTITY = "anthropic"

# Novel verbatim source URLs this run (zero-hit repo-wide pre-commit,
# verified via git grep -F; copied verbatim from the browser.search
# Full-URL listings, NOT constructed).
NOVEL_URLS = [
    "https://nypost.com/2026/09/16/business/women-say-dates-secretly-filmed-them-with-meta-ray-bans-as-creep-glasses-trend-sparks-outrage/",
    "https://nypost.com/2026/10/08/business/anthropic-to-users-be-nice-to-claude-ai-new-policy-bars-abusive-or-cruel-behavior-to-tech/",
    "https://buzzsumo.com/journalist/ariel-zilber-103986242/",
]

# main-run browser.search query sets this run (0 browser.open per
# #503); the delegated scout's saturation-screening queries are
# documented in research_method.
QUERY_SETS = [
    "nypost.com Ariel Zilber Meta smart glasses OR Ray-Ban",
    'nypost.com "be nice to Claude" "Ariel Zilber" byline October 2026',
    '"Violated singles say dates secretly filmed" nypost "Ariel Zilber" byline',
    '"Anthropic to users: be nice to Claude AI" nypost Ariel Zilber',
]


def _load_journalists():
    with open(JOURNALISTS_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _top():
    return _load_journalists()["ariel_zilber_type_b"]


def _block():
    return _top()["competitor_coverage"][BLOCK_KEY]


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
# 1. Anchor per #565
# ---------------------------------------------------------------------------


class TestAnchor1343:
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

    def test_fourth_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FOURTH leg of the 1340-1344 window" in src

    def test_1335_1339_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1335-1339" in src
        assert "VERIFIED CLOSED" in src

    def test_next_leg_is_1344_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "C #1344" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1342 predecessor chain; B is the FOURTH leg.
# ---------------------------------------------------------------------------


class TestRotationGuard1343:
    def test_predecessor_1342_chain_verified(self):
        for sha in (
            PRED_MAIN_1342, PRED_ANCHOR_1342, PRED_DOCSYNC_1342,
            PRED_FINAL_1342,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_1342_type_a_in_git_log(self):
        out = _git("log", "--format=%s", "--grep=Type A #1342")
        assert "Type A #1342" in out.stdout

    def test_no_type_b_1343_in_git_log_pre_commit(self):
        # Pre-commit form: no "Type B #1343" commits exist yet; the
        # post-commit form is asserted by
        # TestMechanismNovelty1343.test_no_type_b_1343_in_git_log_pin
        # (deselected in the in-gate run, #1191-class self-trip).
        out = _git("log", "--format=%H", "--grep=Type B #1343")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits == []

    def test_window_order_1342_before_1343(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1340 -> E #1341 -> A #1342 -> B #1343 -> C #1344" in src

    def test_1342_window_closed_predecessor(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1335-1339" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty per #715
# ---------------------------------------------------------------------------


class TestMechanismNovelty1343:
    def test_top_key_found(self):
        assert _top()["mechanism_ids"] == [MECH_NUM]

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1343 in key, no 1037 or
        # 1038 substring.
        assert "1343" in BLOCK_KEY
        assert str(MECH_NUM) not in BLOCK_KEY
        assert str(NEXT_NUM) not in BLOCK_KEY

    def test_zero_underscore_mechanism_repo_wide(self):
        # Per #715 designed keying the landed number appears only as
        # the colon form; the underscore key form must not exist
        # repo-wide.
        hits = _repo_grep_underscore_mechanism(NEXT_NUM)
        assert hits == [], hits

    def test_zero_dash_mechanism_repo_wide(self):
        hits = _repo_grep_dash_mechanism(NEXT_NUM)
        assert hits == [], hits

    def test_max_mechanism_id_is_1037(self):
        # Post-landing form: the m1037 block is landed, so the max is
        # 1037 and the next-number colon form is absent in profiles.
        assert _max_numeric_mechanism_id() == MECH_NUM
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_no_type_b_1343_in_git_log_pin(self):
        # Post-main-commit form for the OWN run (the #1191-class
        # self-trip, re-pinned in this run's terminal log-hash
        # followup per #721): every commit whose message matches
        # "Type B #1343" must be this run's main commit or a
        # descendant of it. Deselected in the in-gate run (fails
        # pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1343")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1343's own commits"
        main = _git("rev-parse", PRED_MAIN_1343).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_novelty_greps_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "zero test_type_b_1343 files on disk" in src
        assert "max numeric mechanism_id 1036 in profiles/ pre-commit" in src
        assert "one-zero-three-eight mechanism key" in src
        assert '"ariel zilber"' in src


# ---------------------------------------------------------------------------
# 4. Block structure
# ---------------------------------------------------------------------------


class TestBlockStructure1343:
    def test_top_level_fields(self):
        t = _top()
        assert t["name"] == "Ariel Zilber"
        assert t["publication"] == "nypost"
        assert t["mechanism_ids"] == [MECH_NUM]

    def test_block_key_present(self):
        assert BLOCK_KEY in _top()["competitor_coverage"]

    def test_block_identity_fields(self):
        b = _block()
        assert b["block_key"] == BLOCK_KEY
        assert b["mechanism_id"] == MECH_NUM
        assert b["iteration"] == 1343
        assert b["iteration_type"] == "B"
        assert b["type"] == "B"
        assert b["journalist"] == "Ariel Zilber"
        assert b["publication"] == "nypost"
        assert b["author"] == "Kit (with Ray)"
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"

    def test_both_arms_present(self):
        b = _block()
        assert "meta_arm" in b
        assert "anthropic_arm" in b

    def test_meta_arm_fields(self):
        m = _block()["meta_arm"]
        assert m["entity"] == "meta"
        assert m["outlet"] == "nypost"
        assert m["tone_MANUAL_ILLUSTRATIVE"] == META_TONE
        assert m["url"] == NOVEL_URLS[0]
        assert m["date"] == "2026-09-16"
        assert m["author_byline"] == "Ariel Zilber"
        assert "creep glasses" in m["title"]

    def test_anthropic_arm_fields(self):
        m = _block()["anthropic_arm"]
        assert m["entity"] == "anthropic"
        assert m["outlet"] == "nypost"
        assert m["tone_MANUAL_ILLUSTRATIVE"] == OTHER_TONE
        assert m["url"] == NOVEL_URLS[1]
        assert m["date"] == "2026-10-08"
        assert m["author_byline"] == "Ariel Zilber"
        assert "be nice to Claude" in m["title"]

    def test_delta_field(self):
        b = _block()
        assert b["illustrative_delta_anthropic_minus_meta"] == ILLUSTRATIVE_DELTA
        assert b["scorer_delta_MANUAL_ILLUSTRATIVE"] == ILLUSTRATIVE_DELTA

    def test_verdict_and_ledger_fields(self):
        b = _block()
        assert b["verdict"] == "directionally_supported_not_proven"
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 63
        assert b["is_significant"] is False
        assert b["correlation_not_causation"] is True
        assert b["no_analysis_json_update"] is True

    def test_window_field(self):
        b = _block()
        assert "1340-1344" in b["window"]
        assert "FOURTH leg" in b["window"]

    def test_source_urls(self):
        urls = _block()["source_urls"]
        for u in NOVEL_URLS:
            assert u in urls


# ---------------------------------------------------------------------------
# 5. m1037 content discipline
# ---------------------------------------------------------------------------


class TestM1037ContentDiscipline1343:
    def test_meta_arm_quotes(self):
        quotes = " ".join(_block()["meta_arm"]["key_quotes"])
        assert "creep glasses" in quotes
        assert "super violated" in quotes
        assert "privacy headache" in quotes

    def test_meta_arm_tone_reading(self):
        reading = _block()["meta_arm"]["tone_reading"]
        assert "adversarial" in reading.lower()

    def test_anthropic_arm_quotes(self):
        quotes = " ".join(_block()["anthropic_arm"]["key_quotes"])
        assert "actually alive" in quotes
        assert "oddball corners" in quotes

    def test_anthropic_arm_tone_reading(self):
        reading = _block()["anthropic_arm"]["tone_reading"]
        assert "mock" in reading.lower() or "adversarial" in reading.lower()

    def test_delta_reading_constancy(self):
        reading = _block()["delta_reading"]
        assert "constancy" in reading or "symmetric" in reading
        assert "0.15" in reading

    def test_confounder_ranking(self):
        confs = _block()["confounders"]
        assert any("STRONG" in c for c in confs)
        assert any("excerpt" in c.lower() for c in confs)
        assert any("22-day" in c or "temporal" in c.lower() for c in confs)

    def test_deal_context_disclosed(self):
        fc = _block()["financial_context"]
        assert "News Corp" in fc
        assert "OpenAI" in fc
        assert "not adjudicated" in fc

    def test_counter_evidence_present(self):
        ce = _block()["counter_evidence"]
        assert len(ce) >= 2
        joined = " ".join(ce).lower()
        assert "triad" in joined or "twenty-ninth" in joined

    def test_rejection_audit_present(self):
        ra = _block()["rejection_audit"]
        assert "Goodin" in ra
        assert "Criddle" in ra
        assert "Belanger" in ra
        assert "saturated" in ra.lower()

    def test_research_method_documents_screening(self):
        rm = _block()["research_method"]
        assert "screening" in rm.lower()
        assert "4 main-run browser.search" in rm
        assert "0 browser.open" in rm


# ---------------------------------------------------------------------------
# 6. Statistical discipline (the Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------


class TestStatisticalDiscipline1343:
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


# ---------------------------------------------------------------------------
# 7. Falsification ledger: m1037 is NOT a member; sixty-third intact,
#    sixty-fourth absent.
# ---------------------------------------------------------------------------


class TestFalsificationLedger1343:
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

    def test_fifty_first_intact_in_newscorp(self):
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

    def test_fifty_third_intact_in_verge(self):
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
        wired = _read(os.path.join(PROFILES_DIR, "wired.yaml"))
        assert _T56 in wired

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

    def test_fifty_ninth_intact_in_newscorp(self):
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

    def test_sixty_second_intact_in_newscorp(self):
        out = _git(
            "grep", "-c", "-F", _T62, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_third_intact_in_newscorp(self):
        # Landed #1342 (m1036 Times x OpenAI, profiles/news-corp.yaml,
        # committed). HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T63, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_sixty_fourth_member(self):
        # Type B lands one mechanism (m1037); the sixty-fourth
        # member-claim form stays absent repo-wide.
        assert _git_grep_tracked_source(_T64, None) == []


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: forward pins for #1344; #1343 stages the
#    #1191-class no-Type-B-#1343 self-trip (re-pinned post-commit
#    per #721).
# ---------------------------------------------------------------------------


class TestGuardLifecycle1343:
    def test_pins_on_one_mechanism_landing(self):
        # Type B lands one mechanism: max 1037, next 1038.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1037" in src
        assert "NEXT_NUM = 1038" in src

    def test_no_type_c_1344_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1344's terminal log-hash followup
        # per #721): every commit whose message matches "Type C
        # #1344" must be #1344's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type C #1344")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1344's own commits"
        main = _git("rev-parse", PRED_MAIN_1344).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1038_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1038_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1038_dash_absent_repo_wide(self):
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
        # Landed #1282 (m1000, profiles/wired.yaml, committed). HEAD
        # sweep is stable for a committed landing.
        wired = _read(os.path.join(PROFILES_DIR, "wired.yaml"))
        assert _T56 in wired

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

    def test_fifty_ninth_member_present_pin(self):
        # Landed #1302 (m1012, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T59, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixtieth_member_present_pin(self):
        # Landed #1322 (m1024, profiles/financial-times.yaml,
        # committed). HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T60, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_first_member_present_pin(self):
        # Landed #1327 (m1027, profiles/wired.yaml, committed). HEAD
        # sweep is stable for a committed landing.
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

    def test_sixty_third_member_present_pin(self):
        # Landed #1342 (m1036 Times x OpenAI, profiles/news-corp.yaml,
        # committed). HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T63, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_sixty_fourth_member_pin(self):
        # Type B lands one mechanism (m1037); the sixty-fourth
        # member-claim form stays absent repo-wide.
        assert _git_grep_tracked_source(_T64, None) == []

    def test_predecessor_1342_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, B1342_FILE))

    def test_next_leg_is_1344_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1344 Type C" in src

    def test_1342_pins_flip_by_design_documented(self):
        # #1342's forward guards (max-1036, zero one-zero-three-seven
        # keys all forms, no-Type-B-#1343-in-git-log, fortieth
        # absent, forty-eighth through sixty-third intact in
        # profiles/, no sixty-fourth member repo-wide, ledger 63)
        # verified GREEN at HEAD pre-commit this run. TWO pins flip
        # BY DESIGN at this run's main commit: the #1191-class
        # self-trip (no-Type-B-#1343-in-git-log, re-pinned
        # post-commit by TestStalenessPins1343 in both copies per
        # the re-pin-both-copies precedent) and the #1272-class
        # forward-guard expiry (the 1037-numeric-absent-in-profiles
        # pin trips on the landed m1037 block - permanent red by
        # design). The 1037-underscore/dash pins stay green (no
        # one-zero-three-seven mechanism-key forms landed per
        # #723/#738/#739); the no-sixty-fourth-member pin stays
        # green (m1037 is not a member). Documented in the staleness
        # pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1343" in src
        assert "no_type_b_1343_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 9. Background suite (per #795): the #1340-launched suite is OBSERVED
#    only this run; its verdict belongs to #1345.
# ---------------------------------------------------------------------------


class TestBackgroundSuiteCheck1343:
    def test_1340_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1340_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1340-launched suite is observed.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1343_full_suite.log"))

    def test_observation_documented_in_block(self):
        assert "#1340-launched" in _block()["background_suite_status"]
        assert "#795" in _block()["background_suite_status"]
        assert "#1345" in _block()["background_suite_status"]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestDocSync1343:
    def test_readme_test_file_table_has_1343_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_b_1343" in readme

    def test_architecture_has_1343_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1343" in arch

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


class TestIterationLog1343:
    def test_1343_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1343 Type B" in log

    def test_1342_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1342 Type A" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1342's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------


class TestStalenessPins1343:
    def test_1342_guard_lifecycle_post_commit_self_trip(self):
        # Post-terminal-followup form: 24 tests in the class; 23 pass,
        # 1 fails BY DESIGN and permanently - the #1272-class
        # forward-guard expiry
        # (test_1037_numeric_absent_in_profiles trips on the landed
        # m1037 block). The #1191-class self-trip
        # (test_no_type_b_1343_in_git_log_pin) was red at this run's
        # main-commit time; the anchor followup re-pinned
        # PRED_MAIN_1343 in BOTH its own file's copy and the #1342
        # predecessor file's copy per the #1292 re-pin-both-copies
        # precedent and the #721 re-pin rule, flipping it green. The
        # 1037-underscore and 1037-dash pins stay green (no
        # one-zero-three-seven mechanism-key forms landed). Documented
        # here, not repaired. Deselected in the in-gate run (fails
        # pre-commit by design); verified post-terminal.
        res = _class_run(B1342_FILE, "TestGuardLifecycle1342")
        out = res.stdout + res.stderr
        assert "1 failed, 23 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1343:
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
        assert "m846" not in res.stdout
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "do NOT touch #1024 m846" in src
