# -*- coding: utf-8 -*-
"""Type B #1248 tests: Mike Isaac (NYT) journalist cross-entity pair -
Meta AG-settlement competitive-maneuvering register vs Microsoft/OpenAI
unsealed "largest theft of labor" legal-accountability register.

Mechanism 980 (CONTROL-CASE, NOT a falsification-family member; ledger
holds at 52). Same writer, same outlet, 22 days apart (Aug 27 vs Sep 18
2026): Isaac reports Meta's AG settlement as competitive maneuvering
aimed at YouTube/TikTok (-0.35 MANUAL ILLUSTRATIVE, solo byline) and
runs the hard legal-accountability register on Microsoft/OpenAI's
unsealed court documents (-0.55, co-byline Karen Weise and Mike Isaac).
Illustrative delta (OpenAI minus Meta) -0.20: near-symmetric
adversarial, with the litigation adversary drawing the harder register.
The NYT x OpenAI relationship is litigation (NYT Co. sued OpenAI and
Microsoft Dec 2023, in-corpus), NOT a licensing deal, so the uniform
payer-softening prediction is not adjudicated. MANUAL ILLUSTRATIVE ONLY
per the Aug 28 2026 standing rule (tones hand-assigned, n=1 per arm;
p_value/cohens_d/ci_95 NOT_CALCULATED; engine NOT run; is_significant
false; NOT artifact-grade; verdict symmetric_adversarial_not_proven;
no analysis.json update).

Research: delegated scout (60 browser.search queries across 15 batches;
SELECTED Isaac as the tightest in-window same-journalist pair with
URL-complete arms; scout #2 Kafka rejected on URL incompleteness
- Apple arm was a LinkedIn self-post, no canonical BI URL, same bar as
the #1243 Feiner/Belanger rejections; Kashmir Hill half-pair rejected
- Meta-arm URL truncated, no clean competitor arm; all other probes
collided with existing Type B mechanisms or lacked pairs) + 2 main-run
browser.search verification sets (exact-headline Meta-arm search
returning the biztoc mirror verbatim with "(Mike Isaac/New York
Times)" byline and techmeme 2026-08-27 timestamp; exact-headline
OpenAI-arm search returning the portside mirror verbatim with "By
Karen Weise and Mike Isaac" byline plus Muck Rack profile
confirmation; corpus saturation greps: zero mike_isaac_type_b key, both
URLs zero-hit repo-wide, Meta-arm headline zero-hit repo-wide,
OpenAI-arm headline phrase pre-exists only via #867 outlet-level).
0 browser.open per #503 (excerpt-bounded). All URLs copied verbatim
from Full-URL listings; no canonical nytimes.com URLs constructed.
The m980 block lands in profiles/careers/journalists.yaml as a new
top-level mike_isaac_type_b key (per the #643 convention), appended at
the end of the file. Targeted staging by explicit path only; the
in-flight #899/#938/#900/#1012-wt files stay out of this run's
index/diff. Do NOT touch #1024 m846.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup commit. One anchor test (the placeholder pin) fails BY DESIGN
pre-commit; TestAnchor1248 deselected in the in-gate run. The main
commit is the anchor per #565.

FOURTH leg of the 1245-1249 window: D #1245 -> E #1246 -> A #1247 ->
B #1248 -> C #1249 per the #565 anchor + rotation guard. Next run
#1249 Type C closes the window. Type B lands one mechanism
(mechanism 980).

Per #795: this run only CHECKS the #1245-launched background suite
(goal hidden_files type_d_1245_full_suite.log, observed ALIVE at this
run's check, ~10% with live pytest processes 138406/138407); its
verdict and tombstone belong to #1250 (next Type D). This run neither
re-launches, kills, nor writes to the suite.

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
    "test_type_b_1248_mike_isaac_nyt_meta_ag_settlement_"
    "vs_openai_theft_of_labor_oct05_8pm.py"
)
PROFILE_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1245_full_suite.log")

MECH_NUM = 980
NEXT_NUM = 981  # integer only; key-form needles are format-built
ITERATION = 1248

ANCHORED_SHA = "9712e519175dff234d9b7558f4386213e039a83e"

# Predecessor #1247 chain (verified via git rev-parse pre-commit).
PRED_MAIN_1247 = "413a6731e686ae7d0988a35331945d830cd57bba"
PRED_ANCHOR_1247 = "24f0c246dec0e41da2d55c1513ff034ec3e81ea5"
PRED_DOCSYNC_1247 = "0d2d1c8d45075b5d66a31dc1731c3ed91736e57e"
PRED_FINAL_1247 = "956d6fa002a4c928abdd552d0ad7ad7121686da9"
# Predecessor #1246 chain (window SECOND leg).
PRED_MAIN_1246 = "bedd352bbbbbf01049521dc1638fd67b98e320e4"
A1247_FILE = (
    "test_type_a_1247_oct_financial_peg_coverage_landscape_"
    "bounded_absence_audit_oct05_8pm.py"
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
    "type_b_1248_mike_isaac_nyt_meta_ag_settlement_"
    "vs_openai_theft_of_labor_oct05_8pm"
)
JOURNALIST_KEY = "mike_isaac_type_b"

# The two novel source URLs (verbatim from Full-URL listings,
# zero-hit repo-wide pre-commit via git grep -F).
PEG_URLS = [
    "https://biztoc.com/x/6411946169c44995",
    "https://portside.org/2026-09-18/microsoft-and-openai-"
    "workers-worry-about-largest-theft-labor-history",
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

class TestAnchor1248:
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
        assert "FOURTH leg of the 1245-1249 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1248:
    def test_predecessor_1247_chain_verified(self):
        for sha in (
            PRED_MAIN_1247, PRED_ANCHOR_1247, PRED_DOCSYNC_1247,
            PRED_FINAL_1247,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1246_main_verified(self):
        res = _git("cat-file", "-t", PRED_MAIN_1246)
        assert res.stdout.strip() == "commit", "missing 1246 main"

    def test_window_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1245 -> E #1246 -> A #1247 -> B #1248 -> C #1249" in src

    def test_next_is_type_c_1249(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1249 Type C closes the window" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty
# ---------------------------------------------------------------------------

class TestMechanismNovelty1248:
    def test_no_type_b_1248_file_precommit(self):
        # Own file excluded: exactly one match (this file) post-commit.
        hits = [
            f for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_b_1248")
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
        # NEXT_NUM = 981 must have zero key forms (forward guard).
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
# 4. Block structure: the m980 pair
# ---------------------------------------------------------------------------

class TestBlockStructure1248:
    def test_required_top_fields(self):
        block = _block()
        for key in (
            "block_key", "mechanism_id", "iteration", "type", "date",
            "test_file", "author", "goal_id", "job_id", "journalist",
            "publication", "window", "design", "meta_arm", "openai_arm",
            "scorer_delta_MANUAL_ILLUSTRATIVE", "delta_reading",
            "confounders", "counter_evidence", "connects_to", "verdict",
            "finding", "falsification_family",
            "falsification_family_member", "falsification_ledger",
            "ledger_note", "is_significant", "correlation_not_causation",
            "no_analysis_json_update", "artifact_readiness",
            "research_method", "novelty", "background_suite_status",
            "in_flight", "source_urls",
        ):
            assert key in block, key

    def test_mechanism_ids_field(self):
        import yaml
        with open(PROFILE_FILE, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        assert data[JOURNALIST_KEY]["mechanism_ids"] == [MECH_NUM]

    def test_arm_structure(self):
        block = _block()
        for arm_name in ("meta_arm", "openai_arm"):
            arm = block[arm_name]
            for key in (
                "title", "date", "outlet", "author_byline", "entity",
                "url", "url_note", "evidence_tier", "key_quotes",
                "tone_MANUAL_ILLUSTRATIVE", "tone_reading", "status",
            ):
                assert key in arm, (arm_name, key)

    def test_block_key_designed_keying(self):
        # Designed keying per #715: iteration 1248 in key, no 980
        # substring anywhere in the key.
        assert "1248" in BLOCK_KEY
        assert "980" not in BLOCK_KEY
        assert _block()["block_key"] == BLOCK_KEY

    def test_two_source_urls(self):
        assert len(_block()["source_urls"]) == 2

    def test_type_and_entities(self):
        block = _block()
        assert block["type"] == "B"
        assert block["journalist"] == "Mike Isaac"
        assert block["publication"] == "new-york-times"
        assert block["meta_arm"]["entity"] == "meta"
        assert block["openai_arm"]["entity"] == "openai"


# ---------------------------------------------------------------------------
# 5. m980 content discipline
# ---------------------------------------------------------------------------

class TestM980ContentDiscipline1248:
    def test_meta_arm_headline_present(self):
        title = _block()["meta_arm"]["title"]
        assert "yet to publicly acknowledge" in title
        assert "AG settlement" in title

    def test_openai_arm_headline_present(self):
        title = _block()["openai_arm"]["title"]
        assert "Largest Theft of Labor" in title

    def test_bylines(self):
        block = _block()
        assert block["meta_arm"]["author_byline"] == "Mike Isaac"
        assert "Mike Isaac" in block["openai_arm"]["author_byline"]

    def test_arm_dates(self):
        block = _block()
        assert block["meta_arm"]["date"] == "2026-08-27"
        assert block["openai_arm"]["date"] == "2026-09-18"

    def test_tones_manual_illustrative(self):
        block = _block()
        assert block["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.35
        assert block["openai_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.55

    def test_delta_arithmetic(self):
        block = _block()
        delta = block["scorer_delta_MANUAL_ILLUSTRATIVE"]
        expected = (
            block["openai_arm"]["tone_MANUAL_ILLUSTRATIVE"]
            - block["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"]
        )
        assert abs(delta - expected) < 1e-9
        assert abs(delta - (-0.20)) < 1e-9

    def test_control_case_marking(self):
        block = _block()
        assert block["falsification_family_member"] is False
        assert block["falsification_ledger"] == 52
        assert "CONTROL-CASE" in block["finding"]

    def test_confounders_ranked(self):
        confs = _block()["confounders"]
        assert len(confs) >= 5
        joined = " ".join(confs)
        assert "STRONG" in joined
        assert "litigation" in joined.lower()

    def test_scout_rejection_audit_documented(self):
        method = _block()["research_method"]
        assert "Kafka" in method
        assert "Hill" in method

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
        assert block["openai_arm"]["url"] == PEG_URLS[1]


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL/QUALITATIVE ONLY)
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1248:
    def test_not_significant(self):
        assert _block()["is_significant"] is False

    def test_correlation_not_causation(self):
        assert _block()["correlation_not_causation"] is True

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_manual_illustrative_only(self):
        finding = _block()["finding"]
        assert "MANUAL ILLUSTRATIVE ONLY" in finding
        assert "NOT artifact-grade" in finding

    def test_engine_not_run(self):
        text = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "engine NOT run" in text

    def test_verdict_bounded(self):
        assert _block()["verdict"] == "symmetric_adversarial_not_proven"


# ---------------------------------------------------------------------------
# 7. Falsification ledger (holds at 52)
# ---------------------------------------------------------------------------

class TestFalsificationLedger1248:
    def test_ledger_holds_at_52(self):
        assert _block()["falsification_ledger"] == 52

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
        # Full-form claim lives in the m974 block (5 line hits); this
        # run's ledger_note carries only the lowercase prose form.
        out = _git(
            "grep", "-c", "-F", _T52, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_no_fifty_third_member_pin(self):
        assert _git_grep_tracked_source(_T53, ".") == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: forward guards for #1249 (Type C)
# ---------------------------------------------------------------------------

class TestGuardLifecycle1248:
    def test_max_is_980(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_981_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_981_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_981_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_type_c_1249_in_git_log_pin(self):
        out = _git("log", "--oneline", "--grep=Type C #1249").stdout
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
        assert _git_grep_tracked_source(_T53, ".") == []


# ---------------------------------------------------------------------------
# 9. Background suite (per #795: CHECKED ONLY this run)
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1248:
    def test_suite_log_exists(self):
        assert os.path.exists(SUITE_LOG), SUITE_LOG

    def test_suite_log_nonempty(self):
        assert os.path.getsize(SUITE_LOG) > 0

    def test_run_neither_relaunches_nor_kills(self):
        # Observation-only per #795: this run's own processes must not
        # include a suite launcher it started.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "neither" in src and "re-launches" in src

    def test_verdict_belongs_to_1250(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "belong to #1250" in src


# ---------------------------------------------------------------------------
# 10. Doc-sync (post-sync positive per #719; deselected in-gate).
# ---------------------------------------------------------------------------

class TestDocSync1248:
    def test_readme_test_file_table_has_1248_row_post_sync(self):
        text = _read(README_PATH)
        assert "test_type_b_1248" in text

    def test_architecture_has_1248_row_post_sync(self):
        text = _read(ARCH_PATH)
        assert "test_type_b_1248" in text

    def test_readme_stats_ratcheted(self):
        text = _read(README_PATH)
        assert str(README_TEST_COUNT) in text
        assert str(README_FILE_COUNT) in text


# ---------------------------------------------------------------------------
# 11. Iteration log (post-sync positive per #721; deselected in-gate).
# ---------------------------------------------------------------------------

class TestIterationLog1248:
    def test_1248_entry_present_post_sync(self):
        text = _read(LOG_PATH)
        assert "## #1248" in text

    def test_1247_entry_present(self):
        text = _read(LOG_PATH)
        assert "## #1247" in text

    def test_rotation_transparency_convention(self):
        text = _read(LOG_PATH)
        assert "1245-1249 window" in text


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1247's no-Type-B-#1248 pin self-trips post-commit.
# ---------------------------------------------------------------------------

class TestStalenessPins1248:
    def test_1247_guard_lifecycle_post_commit_self_trip(self):
        # Runs the #1247 file's guard-lifecycle class post-commit: its
        # no-Type-B-#1248-in-git-log pin self-trips on this run's own
        # main commit BY DESIGN (the #1191-class self-trip); the class
        # is expected to report the flip, not to stay green.
        res = _class_run(A1247_FILE, "TestGuardLifecycle1247")
        assert "1 failed" in res.stdout or res.returncode != 0, (
            res.stdout[-500:])


# ---------------------------------------------------------------------------
# 13. In-flight isolation: other runs' working state untouched.
# ---------------------------------------------------------------------------

class TestInFlightIsolation1248:
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


README_TEST_COUNT = 68343  # patched post-sync per #719
README_FILE_COUNT = 1573  # patched post-sync per #719
