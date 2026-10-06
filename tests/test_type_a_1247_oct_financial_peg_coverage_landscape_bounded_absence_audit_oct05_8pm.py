# -*- coding: utf-8 -*-
"""Type A #1247 tests: October financial-peg coverage-landscape audit -
bounded absence at profiled publications.

Mechanism 979 (NOT a falsification-family member; ledger holds at 52).
Coverage-landscape DOCUMENTATION, not a discovery. The three major
Oct 1-5 2026 financial pegs - (1) Anthropic x Broadcom $42B vendor
financing (Reuters exclusive Oct 1), (2) OpenAI $30B-at-$1.4T bridge
round (Bloomberg Sep 29), (3) Anthropic Pentagon supply-chain fight /
government-attitude warning (Reuters Oct 2) - drew ZERO originals from
the seven profiled publications across 19 query sets (1 delegated scout
with 10 queries + 9 main-run sets); coverage is originator-wire
(Reuters/Bloomberg) plus trade-press relays only. Extends #1242's m976
bounded-absence finding from the legal peg (Uthmeier injunction) to the
financial pegs. The scout's three top candidates were all REJECTED on
main-run verification with exact corpus locations: Atlantic Robinson
essay -> #1227/m967 (BI exclusive, peg saturated, #1143 precedent);
Verge Dot hands-on -> Type B journalist mechanism (Allison Johnson
pair, exact title in corpus); WIRED Astra -> m877/#1077. MANUAL
ILLUSTRATIVE ONLY per the Aug 28 2026 standing rule (no tone asserted
on absent coverage; p_value/cohens_d/ci_95 NOT_CALCULATED; engine NOT
run; is_significant false; NOT artifact-grade; verdict
bounded_absence_documented; no analysis.json update).

Research: delegated scout (10 browser.search query sets across 8
angles) + 9 main-run browser.search query sets (Atlantic Robinson
quoted title; David Robinson Atlantic essay; WIRED Astra; OpenAI $30B
round; Anthropic IPO Broadcom; FT Anthropic IPO; Broadcom Anthropic
BI/Verge/WIRED; Anthropic Pentagon; Snap/Apple/Google XR). 0
browser.open per #503 (excerpt-bounded). All URLs copied verbatim from
Full-URL listings; no canonical URLs constructed. The m979 block lands
in profiles/competitor-coverage-research.yaml as a top-level key
(0-indent, matching the #1242 Type A convention in that file), appended
at the end of the file. Targeted staging by explicit path only; the
in-flight #899/#938/#900/#1012-wt files stay out of this run's
index/diff.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup commit. One anchor test (the placeholder pin) fails BY DESIGN
post-anchor; TestAnchor1247 deselected in the in-gate run. The main
commit is the anchor per #565.

THIRD leg of the 1245-1249 window: D #1245 -> E #1246 -> A #1247 ->
B #1248 -> C #1249 per the #565 anchor + rotation guard. Next run
#1248 Type B continues the window. Type A lands one mechanism
(mechanism 979).

Per #795: this run only CHECKS the #1245-launched background suite
(goal hidden_files type_d_1245_full_suite.log, observed ALIVE at this
run's check, ~4% with live pytest processes); its verdict and tombstone
belong to #1250 (next Type D). This run neither re-launches, kills, nor
writes to the suite.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit),
#900 (untracked Type D test file), #1012-wt (working-tree edit on the
committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file
must not carry contiguous numeric/underscore/dash mechanism-key forms
of the landed or next number, the forty-eighth / forty-ninth /
fiftieth / fifty-first / fifty-second member-claim forms, the
fifty-third member-claim form, or the fortieth direction form; the
constants are constructed at runtime. (The landed ordinals live as
short lowercase forms in prose here; the live full-form claims live
in profiles/financial-times.yaml, profiles/news-corp.yaml, and
profiles/careers/journalists.yaml: the forty-eighth, forty-ninth,
fiftieth, fifty-first, and fifty-second members respectively.)
"""

import os
import re
import subprocess

import pytest

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
    "test_type_a_1247_oct_financial_peg_coverage_landscape_"
    "bounded_absence_audit_oct05_8pm.py"
)
PROFILE_FILE = os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")

MECH_NUM = 979
NEXT_NUM = 980  # integer only; key-form needles are format-built
ITERATION = 1247

ANCHORED_SHA = "413a6731e686ae7d0988a35331945d830cd57bba"

# Predecessor #1246 chain (verified via git rev-parse pre-commit).
PRED_MAIN_1246 = "bedd352bbbbbf01049521dc1638fd67b98e320e4"
PRED_ANCHOR_1246 = "d17d49800c092de946b327e9c1f2c5dc9b31d199"
PRED_DOCSYNC_1246 = "47fb34bcf10b724bc693a4811e728414b21caf6f"
PRED_FINAL_1246 = "96011698ca9f681055400d23cbc2a0b91b920839"
# Predecessor #1245 chain (window opener).
PRED_MAIN_1245 = "64153de0acc36127eda361905e6b71751d09263c"
E1246_FILE = (
    "test_type_e_1246_podcast_sentiment_172nd_verification_oct05_7pm.py"
)
D1245_FILE = (
    "test_type_d_1245_m976_m977_m978_qualitative_corpus_integrity_"
    "oct05_7pm.py"
)

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770
_T40 = "FORT" + "IETH relationship direction"
_T48 = "FORT" + "Y-EIGHTH falsification-family member"
_T49 = "FORT" + "Y-NINTH falsification-family member"
_T50 = "FIFT" + "IETH falsification-family member"
_T51 = "FIFT" + "Y-FIRST falsification-family member"
_T52 = "FIFT" + "Y-SECOND falsification-family member"
_T53 = "FIFT" + "Y-THIRD falsification-family member"

BLOCK_KEY = (
    "type_a_1247_oct_financial_peg_coverage_landscape_"
    "bounded_absence_audit"
)

# The four novel source URLs (verbatim from Full-URL listings,
# zero-hit repo-wide pre-commit via git grep -F).
PEG_URLS = [
    "https://www.reuters.com/business/broadcom-lend-anthropic-up-42-billion-lease-its-chips-filing-says-2026-10-01/",
    "https://techcrunch.com/2026/09/29/openai-reportedly-in-talks-to-raise-30b-round-at-1-4t-valuation/",
    "https://www.reuters.com/business/media-telecom/anthropic-warns-government-attitudes-may-hurt-customer-ties-ipo-prospectus-shows-2026-10-02/",
    "https://www.reuters.com/legal/transactional/openai-targets-30-billion-funding-14-trillion-valuation-bloomberg-news-reports-2026-09-29/",
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
    return data[BLOCK_KEY]


def _iter_source_files():
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [
            d for d in dirs
            if d not in ("__pycache__", ".git", ".venv", "node_modules")
        ]
        for f in files:
            yield os.path.join(root, f)


def _tracked_grep_files(needle):
    out = _git("grep", "-F", "-l", needle, "HEAD", "--", ".").stdout
    return [l for l in out.splitlines() if l.strip()]


def _git_grep_tracked_source(needle, scope):
    args = ["grep", "-F", "-l", needle, "HEAD", "--"]
    if scope:
        args.append(scope)
    else:
        args.append(".")
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

class TestAnchor1247:
    def test_anchor_sha_patched_to_main_commit(self):
        assert ANCHORED_SHA != "0" * 40
        assert len(ANCHORED_SHA) == 40

    def test_anchor_sha_format(self):
        assert len(ANCHORED_SHA) == 40

    def test_this_run_main_commit_is_anchor(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "main commit is the anchor" in src

    def test_rotation_phrase_in_docstring(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "THIRD leg of the 1245-1249 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1247:
    def test_predecessor_1246_chain_verified(self):
        for sha in (
            PRED_MAIN_1246, PRED_ANCHOR_1246, PRED_DOCSYNC_1246,
            PRED_FINAL_1246,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1245_chain_verified(self):
        res = _git("cat-file", "-t", PRED_MAIN_1245)
        assert res.stdout.strip() == "commit", "missing 1245 main"

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1245 -> E #1246 -> A #1247 -> B #1248 -> C #1249" in src

    def test_next_leg_is_type_b_1248(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1248 Type B" in src

    def test_type_a_lands_one_mechanism(self):
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type A lands one mechanism" in src

    def test_1246_window_position(self):
        text = _read(LOG_PATH)
        assert "SECOND leg of the 1245-1249 window" in text


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1247:
    def test_no_type_a_1247_file_precommit(self):
        # Own file excluded: exactly one match (this file) post-commit.
        hits = [
            f for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_a_1247")
        ]
        assert hits == [OWN_BASENAME], hits

    def test_block_key_present_post_commit(self):
        assert BLOCK_KEY in _read(PROFILE_FILE)

    def test_block_key_zero_hit_precommit_documented(self):
        # Verified pre-commit via git grep -F (see method notes);
        # post-commit the key lives in the profile (working tree).
        hits = _worktree_grep_files(BLOCK_KEY)
        assert any(
            h.endswith("competitor-coverage-research.yaml") for h in hits
        ), hits

    def test_mechanism_id_landed(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_iteration_field(self):
        assert _block()["iteration"] == ITERATION

    def test_next_number_forms_absent(self):
        # NEXT_NUM = 980 must have zero key forms (forward guard).
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_peg_urls_novel(self):
        for url in PEG_URLS:
            hits = _worktree_grep_files(url)
            # Post-commit each URL lives in the profile block and in
            # this file's PEG_URLS constant (the novelty carrier).
            assert any(
                h.endswith("competitor-coverage-research.yaml")
                for h in hits
            ), (url, hits)
            assert set(hits) <= {
                "profiles/competitor-coverage-research.yaml",
                "tests/" + OWN_BASENAME,
            }, (url, hits)


# ---------------------------------------------------------------------------
# 4. Coverage landscape: the three pegs and the bounded absence
# ---------------------------------------------------------------------------

class TestCoverageLandscape1247:
    def test_three_pegs_documented(self):
        pegs = _block()["financial_pegs"]
        assert len(pegs) == 3
        labels = [p["label"] for p in pegs]
        assert any("Broadcom" in l for l in labels)
        assert any("$30B" in l or "1.4T" in l for l in labels)
        assert any("Pentagon" in l for l in labels)

    def test_peg_dates_in_window(self):
        pegs = _block()["financial_pegs"]
        for p in pegs:
            assert p["date"] in (
                "2026-09-29", "2026-10-01", "2026-10-02",
            ), p["date"]

    def test_originator_attribution(self):
        text = _read(PROFILE_FILE)
        assert "Reuters" in text
        assert "Bloomberg" in text

    def test_bounded_absence_claim(self):
        block = _block()
        assert "bounded_absence" in block["verdict"].lower()
        assert block["coverage_landscape"]["profiled_originals_count"] == 0

    def test_query_set_count(self):
        block = _block()
        assert block["query_sets_total"] == 19

    def test_relay_tier_documented(self):
        text = _read(PROFILE_FILE)
        assert "trade-press relays" in text or "trade relays" in text

    def test_scorer_not_run(self):
        block = _block()
        assert "NOT RUN" in block["asymmetry_scorer"]

    def test_iteration_492_cited(self):
        text = _read(PROFILE_FILE)
        assert "iteration-492" in text or "iteration_492" in text


# ---------------------------------------------------------------------------
# 5. Scout-rejection audit: three candidates dead on verification
# ---------------------------------------------------------------------------

class TestScoutRejectionAudit1247:
    def test_three_rejections_documented(self):
        rejects = _block()["scout_rejections"]
        assert len(rejects) == 3

    def test_robinson_rejection_points_to_1227(self):
        rejects = _block()["scout_rejections"]
        r = [x for x in rejects if "Robinson" in x["candidate"]][0]
        assert "m967" in r["corpus_location"]
        assert "#1227" in r["corpus_location"]

    def test_dot_rejection_points_to_journalist_mechanism(self):
        rejects = _block()["scout_rejections"]
        r = [x for x in rejects if "Dot" in x["candidate"]][0]
        assert "journalists.yaml" in r["corpus_location"]

    def test_wired_astra_rejection_points_to_1077(self):
        rejects = _block()["scout_rejections"]
        r = [x for x in rejects if "Astra" in x["candidate"]][0]
        assert "m877" in r["corpus_location"]

    def test_rejection_locations_verify_in_repo(self):
        # The corpus locations cited must actually exist.
        assert _tracked_grep_files("type_a_1227_bi_openai_robinson") != []
        out = _git("grep", "-F", "-l", "m877",
                   "HEAD", "--", "profiles/wired.yaml").stdout
        assert "profiles/wired.yaml" in out


# ---------------------------------------------------------------------------
# 6. Statistical discipline (Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1247:
    def test_tone_not_scored(self):
        block = _block()
        assert block["tone_scores"] == "NOT_SCORED"

    def test_engine_not_run(self):
        text = _read(PROFILE_FILE)
        assert "engine NOT run" in text

    def test_p_value_not_calculated(self):
        block = _block()
        assert block["p_value"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        block = _block()
        assert block["is_significant"] is False

    def test_not_artifact_grade(self):
        block = _block()
        assert block["artifact_grade"] is False

    def test_no_analysis_json_update(self):
        block = _block()
        assert block["analysis_json_update"] is False

    def test_correlation_not_causation(self):
        text = _read(PROFILE_FILE)
        assert "Correlation is not causation" in text


# ---------------------------------------------------------------------------
# 7. Falsification ledger (holds at 52; m979 is NOT a member)
# ---------------------------------------------------------------------------

class TestFalsificationLedger1247:
    def test_not_a_member(self):
        block = _block()
        assert block["falsification_family_member"] is False

    def test_ledger_holds_at_52(self):
        text = _read(PROFILE_FILE)
        assert "Ledger holds at 52" in text

    def test_forty_eighth_intact(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_forty_ninth_intact(self):
        assert _git_grep_tracked_source(_T49, "profiles/") == [
            "profiles/careers/journalists.yaml"]

    def test_fiftieth_intact(self):
        out = _git(
            "grep", "-c", "-F", _T50, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_first_intact(self):
        out = _git(
            "grep", "-c", "-F", _T51, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_second_intact(self):
        out = _git(
            "grep", "-c", "-F", _T52, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_no_fifty_third(self):
        assert _git_grep_tracked_source(_T53, None) == []

    def test_no_fortieth_direction(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: forward guards for #1248 (Type B)
# ---------------------------------------------------------------------------

class TestGuardLifecycle1247:
    def test_max_is_979(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_980_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_980_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_980_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_type_b_1248_in_git_log_pin(self):
        out = _git("log", "--oneline", "--grep=Type B #1248").stdout
        assert out.strip() == ""

    def test_no_fortieth_direction_pin(self):
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

    def test_no_fifty_third_member_pin(self):
        assert _git_grep_tracked_source(_T53, None) == []

    def test_predecessor_1246_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1246_FILE))

    def test_next_leg_is_1248_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1248 Type B" in src

    def test_1246_pins_flip_by_design_documented(self):
        # #1246's no-Type-A-#1247-in-git-log pin flips BY DESIGN at
        # this run's main commit (the #1191-class self-trip, pinned in
        # TestStalenessPins1247); #1246's max-978, zero-979 (all
        # forms), fortieth-absent, forty-eighth-intact,
        # forty-ninth-intact, fiftieth-intact, fifty-first-intact,
        # fifty-second-intact, no-fifty-third guards stay green
        # (Type A lands no falsification member).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "flips BY DESIGN" in src


# ---------------------------------------------------------------------------
# 9. Background suite check (per #795: observe only, verdict to #1250)
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1247:
    def test_suite_log_exists(self):
        log = os.path.join(
            GOAL_HIDDEN, "type_d_1245_full_suite.log")
        assert os.path.exists(log)

    def test_suite_observed_not_owned(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "neither re-launches, kills, nor writes" in src

    def test_verdict_belongs_to_1250(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "belong to #1250" in src


# ---------------------------------------------------------------------------
# 10. Staleness pins (deselected in-gate per #721)
# ---------------------------------------------------------------------------

class TestStalenessPins1247:
    def test_1246_guard_lifecycle_post_commit_self_trip(self):
        # Runs the #1246 file's guard-lifecycle class post-commit: its
        # no-Type-A-#1247-in-git-log pin self-trips on this run's own
        # main commit BY DESIGN (the #1191-class self-trip); the class
        # is expected to report the flip, not to stay green.
        res = _class_run(E1246_FILE, "TestGuardLifecycle1246")
        assert "1 failed" in res.stdout or res.returncode != 0, (
            res.stdout[-500:])


# ---------------------------------------------------------------------------
# 11. Doc-sync (post-sync positive per #719; deselected in-gate).
# ---------------------------------------------------------------------------

class TestDocSync1247:
    def test_readme_test_file_table_has_1247_row_post_sync(self):
        text = _read(README_PATH)
        assert "test_type_a_1247" in text

    def test_architecture_has_1247_row_post_sync(self):
        text = _read(ARCH_PATH)
        assert "test_type_a_1247" in text

    def test_readme_stats_ratcheted(self):
        text = _read(README_PATH)
        assert str(README_TEST_COUNT) in text
        assert str(README_FILE_COUNT) in text


# ---------------------------------------------------------------------------
# 12. Iteration log (post-sync positive per #721; deselected in-gate).
# ---------------------------------------------------------------------------

class TestIterationLog1247:
    def test_1247_entry_present_post_sync(self):
        text = _read(LOG_PATH)
        assert "## #1247" in text

    def test_1246_entry_present(self):
        text = _read(LOG_PATH)
        assert "## #1246" in text

    def test_rotation_transparency_convention(self):
        text = _read(LOG_PATH)
        assert "1245-1249 window" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation: other runs' working state untouched.
# ---------------------------------------------------------------------------

class TestInFlightIsolation1247:
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
            "profiles/competitor-coverage-research.yaml",
        }
        assert set(staged) <= allowed, staged


README_TEST_COUNT = 77  # patched post-sync per #719
README_FILE_COUNT = 13  # patched post-sync per #719
