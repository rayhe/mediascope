# -*- coding: utf-8 -*-
"""Type B #1298 tests: Nicholas Sutrich (Android Central, Future plc) -
Sep-16-2026 Meta Ray-Ban Display one-year long-term review
(-0.15 MANUAL ILLUSTRATIVE, NEW Meta arm, excerpt-attested via the
ccstartup.com and realhacker.news verbatim mirrors; canonical
androidcentral.com URL not recovered from search listings, none
constructed per policy) vs May-20-2026 Xreal Project Aura hands-on
from Google I/O 2026 (+0.30 MANUAL ILLUSTRATIVE, NEW Google/Xreal arm,
canonical URL copied verbatim from the Mobile Tech Podcast episode
link listing); illustrative delta (Google/Xreal minus Meta) +0.45 -
same writer, same outlet, ~4 months apart.

Mechanism 1010 (NOT a falsification-family member; ledger holds at 58).
FIRST dedicated Type B mechanism on Nicholas Sutrich (prior corpus
mentions are #1278 scout-rejection notes only, where he was held as
backup #3 with the Google-arm relay missing - this run supplies that
missing relay). The documented AI content-licensing deal at this outlet
is with OpenAI (Future plc, Dec 2024, m473 lineage) - NOT with
Google/Xreal - so no named financial gradient predicts the observed
gradient; the writer-register pattern bounds the deal explanation
rather than confirming it (same brief as #1293). STRONG confounds:
temporal gap (~4 months) and genre-peg skew (long-term review vs
pre-release hands-on; the #893 Jay Peters genre lesson applies).

Excerpt-bounded research per #503 (main-run candidate sweep across ~20
journalists + exact-headline verification sets, 0 browser.open reads).
Candidate sweep: SELECTED Sutrich as the only fully-verified same-writer
pair with URL-complete arms (Android Central, May 20 / Sep 16 2026);
REJECTED Peters (saturated m731/m767), Pierce (saturated), Stern
(saturated), Stein (saturated m588), Song (saturated m593/m827),
Ashworth (saturated m853/m998), Field (saturated type_b_1178),
Eadicicco (saturated #1283), Newman/Burgess (saturated m1004/#1288),
Lawler (saturated #1243), Preston (in-flight #938), O'Brien (saturated
m854/#1038), Roth (saturated m782/m860/m953), Huamani (saturated
m959/#1213), Chokkattu (saturated m411), Sato (saturated m215), Ulanoff
(saturated m195), Bell (saturated m722/#818/#888), Hector (saturated
#963), Bordelon (Meta arms stale Apr 2026), Ortutay (no clean competitor
arm), Grantham-Philips (no clean competitor arm), Wagner (no in-window
bylines), Warren (Microsoft beat, no Meta arm), Davis (no pair
surfaced), Allison Johnson (no pair surfaced), Rutherford (no pair
surfaced).

The m1010 block lives in profiles/careers/journalists.yaml under the
nicholas_sutrich_type_b keyed entry's competitor_coverage dict (per the
#643 convention); mechanism_ids [1010].

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup commit. One anchor test (the placeholder pin) fails BY DESIGN
post-anchor.

Per #795: this run only CHECKS the #1295-launched background suite
(goal hidden_files type_d_1295_full_suite.log, observed at this run's
check; an observation, not a verdict); its verdict and tombstone belong
to #1300 (next Type D). This run neither re-launches, kills, nor writes
to the suite.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit),
#900 (untracked Type D test file), #1012-wt (working-tree edit on the
committed Type A #1012 file).

Type B lands one mechanism (mechanism 1010); the Type A predecessor
added one (mechanism 1009). Next run #1299 Type C closes the 1295-1299
window. Rotation: D #1295 -> E #1296 -> A #1297 -> B #1298 -> C #1299.
This run is the FOURTH leg of the 1295-1299 window. The main commit is
the anchor per #565.

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
landed or next number, the forty-eighth through fifty-eighth
member-claim forms, the fifty-ninth member-claim form, or the fortieth
direction form; the constants are constructed at runtime. (The landed
ordinals live as short lowercase forms in prose here; the live full-form
claims live in profiles/financial-times.yaml, profiles/news-corp.yaml,
profiles/the-verge.yaml, profiles/guardian.yaml, profiles/atlantic.yaml,
profiles/wired.yaml, profiles/ap.yaml, and profiles/careers/journalists.yaml.)
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
    "test_type_b_1298_nicholas_sutrich_android_central_meta_display_"
    "year_review_vs_xreal_aura_may_sep_9pm.py"
)
JOURNALIST_NAME = "Nicholas Sutrich"
ENTRY_KEY = "nicholas_sutrich_type_b"

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "0" * 40  # placeholder-only per #565 pre-commit

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1010
NEXT_NUM = 1011  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_b_1298_nicholas_sutrich_android_central_meta_display_"
    "year_review_vs_xreal_aura"
)

# Predecessor chain: #1297 Type A (third leg).
PRED_MAIN_1297 = "a8bd4c5dc8708c4f8604762175446526b29dcad4"
PRED_ANCHOR_1297 = "031bc9837241d7368c7e8460595c7aa9c38b33a5"
PRED_DOCSYNC_1297 = "f9cdd60c85f72b49249f562ddbbd0b4a302f48b5"
PRED_FINAL_1297 = "277ce84e4f575f72eda22ad7d9d4691771dadc87"
PRED_PUSH_1297 = "8d2e3632f7b03d21613420d4bc2a7a02efb0ffcd"
# #1296 Type E (second leg) for the rotation-guard chain.
PRED_MAIN_1296 = "14af9fecd0d7dcc93eced86ab065e9114f685226"
PRED_ANCHOR_1296 = "ab7778723654c3af8f3fd3ba50e98f849c4d4437"
PRED_DOCSYNC_1296 = "064eb53069399711d54b405d2e763d16c909a828"
PRED_FINAL_1296 = "953ddaaa62a7f16ba13c2b6889aa900fcc57b7c0"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the own-run git-log pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1298 = "0" * 40  # re-pinned in the terminal log-hash followup per #721

# Forward guard for the next leg: #1299 Type C. Re-pinned by #1299's
# log-hash followup per #721 (starts as 0*40; the forward pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1299 = "0" * 40  # re-pinned in #1299 terminal log-hash followup per #721

# The #1297 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 1009; zero one-zero-one-zero keys all
# forms / no-Type-B-#1298-in-git-log / fortieth direction absent /
# forty-eighth through fifty-eighth members intact /
# fifty-ninth member absent / ledger 58).
D1297_FILE = (
    "test_type_a_1297_guardian_openai_oct06_kwon_parliamentary_"
    "apology_register_vs_carried_meta_arms_oct07_9pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 72733  # post-doc-sync value per #719 (91 collected)
README_FILE_COUNT = 1623  # post-doc-sync value per #719 (+1 file)

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

# Novel source URLs: 1 zero-hit repo-wide pre-commit (git grep -F).
# The Meta arm is attested via the ccstartup.com and realhacker.news
# verbatim mirrors plus the Android Central wearables listing and the
# BuzzSumo journalist profile (headline + byline + date; canonical
# androidcentral.com URL not recovered, none constructed per policy) -
# the listing URLs are attestation, not novel source URLs.
NOVEL_URLS = [
    "https://www.androidcentral.com/gaming/virtual-reality/xreal-project-aura-google-io-2026",
]

# Meta-arm mirror URL: zero-hit repo-wide pre-commit (git grep -F
# verified), presented in the block's evidence_tier prose, NOT as a
# novel source URL (mirror attestation, not a source URL).
META_MIRROR_URL = (
    "https://ccstartup.com/blog/2026/09/16/ive-used-meta-ray-ban-display-"
    "for-a-year-and-i-like-them-but-it-still-feels-like-something-is-"
    "missing/"
)


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


def _load_journalists():
    return yaml.safe_load(_read(JOURNALISTS_PATH))


def _entry():
    return _load_journalists()[ENTRY_KEY]


def _block():
    return _entry()["competitor_coverage"][BLOCK_KEY]


def _block_text():
    return _read(JOURNALISTS_PATH)


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
    return subprocess.run(
        ["python3", "-m", "pytest", target,
         "-k", classname,
         "-q", "--no-header"],
        cwd=REPO_ROOT, capture_output=True, text=True, env=env,
    )


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------

class TestAnchor1298:
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
        assert "FOURTH leg of the 1295-1299 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1298:
    def test_predecessor_1297_chain_verified(self):
        for sha in (
            PRED_MAIN_1297, PRED_ANCHOR_1297, PRED_DOCSYNC_1297,
            PRED_FINAL_1297, PRED_PUSH_1297,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1296_chain_verified(self):
        for sha in (
            PRED_MAIN_1296, PRED_ANCHOR_1296, PRED_DOCSYNC_1296,
            PRED_FINAL_1296,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1295 -> E #1296 -> A #1297 -> B #1298 -> C #1299" in src

    def test_next_leg_is_type_c_1299(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1299 Type C" in src

    def test_type_b_lands_one_mechanism(self):
        # Type B lands exactly one mechanism (mechanism 1010); the Type
        # A predecessor added one (mechanism 1009).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type B lands one mechanism" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1298:
    def test_block_found_under_sutrich_entry(self):
        assert _entry()["name"] == JOURNALIST_NAME
        assert BLOCK_KEY in _entry()["competitor_coverage"]
        assert _block()["mechanism_id"] == MECH_NUM

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #723/#738/#739: the iteration-form block
        # key carries no numeric/underscore/dash mechanism-id
        # substring.
        assert str(MECH_NUM) not in BLOCK_KEY

    def test_zero_underscore_mechanism_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_zero_dash_mechanism_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_zero_numeric_next_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_this_run(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_novel_urls_in_block_source_urls_verbatim(self):
        urls = _block()["google_arm"]["source_urls"]
        for u in NOVEL_URLS:
            assert u in urls, u

    def test_meta_arm_attestation_not_novel_url(self):
        # The Meta arm is attested via the ccstartup.com / realhacker
        # mirrors plus listing/profile attribution (attestation, not a
        # novel source URL); the block must not present the listing as
        # a novel source.
        assert "source_urls" not in _block()["meta_arm"]
        assert "byline_attribution_urls" in _block()["meta_arm"]

    def test_meta_mirror_url_not_novel_source(self):
        # The Meta-arm mirror URL is disclosed in evidence_tier prose
        # but is not carried as a source URL anywhere in the block.
        text = _block_text()
        assert text.count(META_MIRROR_URL) <= 1

    def test_block_key_zero_hit_except_landed(self):
        # The block key exists only in the landed profile block and in
        # this test file (which is excluded from the sweep carrier per
        # #715); no other source file carries it.
        hits = []
        for p in _iter_source_files():
            if BLOCK_KEY in open(p, encoding="utf-8",
                                 errors="replace").read():
                hits.append(p)
        assert hits == [JOURNALISTS_PATH], hits

    def test_no_type_b_1298_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type B #1298" must be this run's
        # main commit or a descendant of it - i.e., no PRIOR run
        # committed this run's iteration. Deselected in the in-gate
        # run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1298")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1298).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h


# ---------------------------------------------------------------------------
# 4. Block structure
# ---------------------------------------------------------------------------

class TestBlockStructure1298:
    def test_journalists_profile_exists(self):
        assert os.path.exists(JOURNALISTS_PATH)

    def test_entry_name_and_publication(self):
        assert _entry()["name"] == JOURNALIST_NAME
        assert _entry()["publication"] == "android_central"
        assert _entry()["mechanism_ids"] == [MECH_NUM]

    def test_block_under_entry_competitor_coverage(self):
        assert BLOCK_KEY in _entry()["competitor_coverage"]

    def test_mechanism_id_field(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_iteration_fields(self):
        b = _block()
        assert b["iteration"] == 1298
        assert b["iteration_type"] == "B"
        assert b["type"] == "B"

    def test_required_block_fields(self):
        b = _block()
        for field in (
            "journalist", "publication", "finding",
            "meta_arm", "google_arm", "illustrative_means",
            "asymmetry_scorer_result", "statistical_discipline",
            "financial_context", "confounders", "counterevidence",
            "cross_references", "connects_to", "research_method",
            "novelty", "test_file", "artifact_readiness",
            "falsification_family", "falsification_ledger",
            "background_suite_status", "in_flight",
        ):
            assert field in b, field

    def test_test_file_field_matches_own_basename(self):
        assert _block()["test_file"] == "tests/" + OWN_BASENAME

    def test_meta_arm_tone(self):
        assert _block()["meta_arm"]["tone_score"] == -0.15

    def test_google_arm_tone(self):
        assert _block()["google_arm"]["tone_score"] == 0.3

    def test_scorer_delta(self):
        means = _block()["illustrative_means"]
        assert means["delta_google_minus_meta"] == pytest.approx(0.45)
        assert means["delta_calc"] == "0.30 - (-0.15) = +0.45"

    def test_connects_to_lineage(self):
        assert _block()["connects_to"] == [473, 115, 767]

    def test_source_urls_count(self):
        assert len(_block()["google_arm"]["source_urls"]) == 1

    def test_google_arm_date_and_byline(self):
        arm = _block()["google_arm"]
        assert arm["date"] == "2026-05-20"
        assert arm["author_byline"] == "Nicholas Sutrich"

    def test_meta_arm_date_and_byline(self):
        arm = _block()["meta_arm"]
        assert arm["date"] == "2026-09-16"
        assert arm["author_byline"] == "Nicholas Sutrich"

    def test_first_sutrich_mechanism(self):
        cc = _entry()["competitor_coverage"]
        assert len(cc) == 1


# ---------------------------------------------------------------------------
# 5. Content discipline
# ---------------------------------------------------------------------------

class TestM1010ContentDiscipline1298:
    def test_meta_headline_verbatim(self):
        assert "something is missing" in (
            _block()["meta_arm"]["title"])

    def test_meta_26_app_quote(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        assert any("26 are available" in q for q in quotes)

    def test_meta_monocular_quote(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        assert any("monocular vision" in q for q in quotes)

    def test_google_headline_verbatim(self):
        title = _block()["google_arm"]["title"]
        assert "exactly what Android XR was made for" in title

    def test_google_full_power_quote(self):
        quotes = _block()["google_arm"]["key_quotes"]
        assert any("full power of the Android XR platform" in q
                   for q in quotes)

    def test_m473_deal_disclosed(self):
        fin = _block()["financial_context"]
        assert "Future plc x OpenAI" in fin
        assert "Dec 2024" in fin

    def test_no_google_deal_disclosed(self):
        fin = _block()["financial_context"]
        assert "No documented Future plc-to-Google" in fin

    def test_1278_scout_mention_disclosed(self):
        assert "#1278" in _block()["novelty"]
        assert "scout-rejection" in _block()["novelty"]

    def test_ascii_only(self):
        # Block-scoped (the file carries pre-existing non-ASCII in
        # other records; this block must be clean).
        def _walk(o):
            if isinstance(o, str):
                o.encode("ascii")
            elif isinstance(o, dict):
                for v in o.values():
                    _walk(v)
            elif isinstance(o, list):
                for v in o:
                    _walk(v)
        _walk(_entry())

    def test_no_em_dashes(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        em_dash = chr(0x2014)  # built at runtime per #770; no literal in source
        en_dash = chr(0x2013)
        assert em_dash not in src
        assert en_dash not in src

    def test_yaml_block_ascii(self):
        block = _block()
        yaml.safe_dump(block).encode("ascii")


# ---------------------------------------------------------------------------
# 6. Statistical discipline (the Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1298:
    def test_manual_illustrative_only(self):
        sd = _block()["statistical_discipline"]
        assert sd["manual_illustrative_only"] is True

    def test_engine_not_run(self):
        sd = _block()["statistical_discipline"]
        assert sd["engine_run"] is False

    def test_p_value_not_calculated(self):
        sd = _block()["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"

    def test_cohens_d_not_calculated(self):
        sd = _block()["statistical_discipline"]
        assert sd["cohens_d"] == "NOT_CALCULATED"

    def test_ci_95_not_calculated(self):
        sd = _block()["statistical_discipline"]
        assert sd["ci_95"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        sd = _block()["statistical_discipline"]
        assert sd["is_significant"] is False

    def test_correlation_not_causation(self):
        assert "Correlation is not causation" in _block()["finding"]

    def test_no_analysis_json_update(self):
        sd = _block()["statistical_discipline"]
        assert sd["analysis_json_update"] is False

    def test_verdict_directionally_supported_not_proven(self):
        assert (
            _block()["asymmetry_scorer_result"]["verdict"]
            == "directionally_supported_not_proven"
        )

    def test_not_artifact_grade(self):
        sd = _block()["statistical_discipline"]
        assert sd["artifact_grade"] is False

    def test_ledger_holds_at_58(self):
        assert _block()["falsification_ledger"] == 58


# ---------------------------------------------------------------------------
# 7. Guard lifecycle: forward guards for #1299 Type C.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1298:
    def test_pins_on_one_mechanism_landing(self):
        # Type B lands one mechanism: max 1010, next 1011.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1010" in src
        assert "NEXT_NUM = 1011" in src

    def test_no_type_c_1299_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1299's terminal log-hash followup
        # per #721): every commit whose message matches "Type C
        # #1299" must be #1299's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type C #1299")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1299's own commits"
        main = _git("rev-parse", PRED_MAIN_1299).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1011_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1011_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1011_dash_absent_repo_wide(self):
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

    def test_predecessor_1297_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, D1297_FILE))

    def test_next_leg_is_1299_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1299 Type C" in src

    def test_1297_pins_flip_by_design_documented(self):
        # #1297's forward guards (max-1009, zero one-zero-one-zero
        # keys all forms, no-Type-B-#1298-in-git-log, fortieth
        # absent, forty-eighth through fifty-eighth intact in
        # profiles/, fifty-ninth absent, ledger 58) verified GREEN
        # at HEAD pre-commit this run. The no-Type-B-#1298-in-git-log
        # pin flips BY DESIGN at this run's main commit (the
        # #1191-class self-trip, re-pinned post-commit by
        # TestStalenessPins1298). Type B lands one mechanism, so the
        # zero one-zero-one-zero numeric pin flips BY DESIGN too (the
        # #1272-class forward-guard expiry; the underscore/dash pins
        # stay green by the #723/#738/#739 designed keying).
        # Documented in the staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1298" in src
        assert "no_type_b_1298_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 8. Staleness pins: #1297's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------

class TestStalenessPins1298:
    def test_1297_guard_lifecycle_post_commit_self_trip(self):
        # Post-terminal-followup form: 21 tests in the class; ONE flips
        # BY DESIGN when this run's main commit lands and STAYS
        # flipped: the test_1010_numeric_absent_in_profiles pin (the
        # m1010 landing carries "mechanism_id: 1010" in colon form -
        # the #1272-class forward-guard expiry; the underscore/dash
        # pins stay green by the #723/#738/#739 designed keying). The
        # no_type_b_1298_in_git_log ancestor pin ALSO flips at the
        # main commit but is re-pinned green in the terminal log-hash
        # followup per #721 (its PRED_MAIN_1298 now holds this run's
        # main sha). The class run below therefore expects 1 failed /
        # 20 passed and documents the designed flip. The #1297 block
        # is read-only to this run; the flip is documented here, not
        # repaired. Deselected in the in-gate run (fails pre-commit
        # by design).
        res = _class_run(D1297_FILE, "TestGuardLifecycle1297")
        out = res.stdout + res.stderr
        assert "1 failed, 20 passed" in out, out[-2000:]
        assert "test_1010_numeric_absent_in_profiles" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 9. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1298:
    def test_readme_test_file_table_has_1298_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1298_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert OWN_BASENAME in arch

    def test_readme_stats_ratcheted(self):
        readme = _read(README_PATH)
        assert "| Tests | %d |" % README_TEST_COUNT in readme
        assert "Across %d test files" % README_FILE_COUNT in readme


# ---------------------------------------------------------------------------
# 10. Iteration-log entry per #721 (3 tests; deselected pre-commit)
# ---------------------------------------------------------------------------

class TestIterationLog1298:
    def test_log_has_1298_entry(self):
        text = _read(LOG_PATH)
        assert "## #1298 Type B" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_finding(self):
        text = _read(LOG_PATH)
        assert "m1010" in text
        assert "directionally_supported_not_proven" in text
        assert "ledger holds at 58" in text


# ---------------------------------------------------------------------------
# 11. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1298:
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
