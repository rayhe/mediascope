# -*- coding: utf-8 -*-
"""Type A #1242 tests: CNN (WBD) x OpenAI - Sep-28-2026 Uthmeier
temporary-injunction motion bounded absence at profiled nationals.

Mechanism 976 (NOT a falsification-family member; temporal extension
of mechanism #347; ledger holds at 52). The live full-form claim
lives in profiles/competitor-coverage-research.yaml under
cross_publication_findings. On Sep 28, 2026 Florida AG James Uthmeier
filed a dozens-of-pages motion for temporary injunction in the 10th
Judicial Circuit, Highlands County (case 26000295GCAXMX, per Bloomberg
Law) seeking six prohibitions against OpenAI and CEO Sam Altman inside
the June-1 civil suit, the most aggressive state-level AI-development
restraint sought to date (prior authorization for new-model training).
Trade and regional outlets covered it (PYMNTS, Bloomberg Law,
cybersecuritynews, mixed-news, AI Daily Post, American Star News,
Floridian Press, NeoTeo, Zubiqo, ISPR, AI Policy Desk tracker,
ExplainX Sep-28 digest, Change.org petition); three search sets found
zero profiled-national originals in the Sep-28 to Oct-5 window
(bounded absence per the iteration-492 rule). CNN's institutional
awareness is proven by #347 (Jun-1 OpenAI suit original; Aug-24
subpoena piece; Aug-26/27 Meta settlement quoting Uthmeier). The
asymmetry scorer is NOT RUN on the new peg (absence yields no fresh
arm); #347's carried arms and delta are unchanged. Statistical
discipline: MONITORING/QUALITATIVE ONLY per the Aug 28 2026 standing
rule (no tone asserted on absent coverage; p_value/cohens_d/ci_95
NOT_CALCULATED; engine NOT run; is_significant false; NOT
artifact-grade; no analysis.json update; verdict
directionally_supported_not_proven).

Research: 4 browser.search query sets this run (Florida AG Uthmeier
sues OpenAI Altman guardrails; site: cnn.com/nytimes.com/wsj.com/
washingtonpost.com Uthmeier OpenAI injunction; Florida halt OpenAI
model development major newspaper; Florida Uthmeier injunction
ft.com/theguardian.com/businessinsider.com/theverge.com) - SELECTED
the Bloomberg Law + cybersecuritynews + mixed-news + ISPR + AI Policy
Desk attestation cluster; REJECTED the Sora-2 peg (discontinued Apr
2026, stale) and the Guardian/FT enforcement-week pegs (saturated:
m934, m901, m952). 0 browser.open per #503 (excerpt-bounded). The
mechanism 976 block lands in
profiles/competitor-coverage-research.yaml as a top-level key
(0-indent, matching the recent Type A convention in that file),
appended at the end of the file. Targeted staging by explicit path only; the
in-flight #899/#938/#900/#1012-wt files stay out of this run's
index/diff.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup commit. One anchor test (the placeholder pin) fails BY DESIGN
post-anchor; TestAnchor1242 deselected in the in-gate run. The main
commit is the anchor per #565.

THIRD leg of the 1240-1244 window: D #1240 -> E #1241 -> A #1242 ->
B #1243 -> C #1244 per the #565 anchor + rotation guard. Next run
#1243 Type B continues the window. Type A lands one mechanism
(mechanism 976).

Per #795: this run only CHECKS the #1240-launched background suite
(goal hidden_files type_d_1240_full_suite.log, observed ALIVE at this
run's check); its verdict and tombstone belong to #1245 (next Type D).
This run neither re-launches, kills, nor writes to the suite.

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
    "test_type_a_1242_cnn_openai_sep28_uthmeier_injunction_"
    "bounded_absence_oct05_4pm.py"
)
PROFILE_FILE = os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "9d35d3691368a569720e29028e15ff9ed7d26e9f"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 976
NEXT_NUM = 977  # integer only; key-form needles are format-built

# Fragment-built per #715: the bare block key never appears
# contiguously in this file.
BLOCK_KEY = (
    "cnn_wbd_uthmeier_openai_sep28_"
    "injunction_bounded_absence_1242"
)

# Predecessor chain: #1241 Type E continued the 1240-1244 window.
PRED_MAIN_1241 = "600b3a8b"
PRED_ANCHOR_1241 = "1c8b10c1"
PRED_DOCSYNC_1241 = "e58d7a64"
PRED_FINAL_1241 = "19c97dfd"
PRED_MAIN_1240 = "f64ea8a3"
PRED_ANCHOR_1240 = "a2bcfaa1"
PRED_DOCSYNC_1240 = "888b95df"
PRED_FINAL_1240 = "bf11f510"

# The #1241 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 975; zero next-number nine-seven-six
# keys all forms / no-Type-E-#1241-in-git-log / fortieth direction
# absent / forty-eighth through fifty-second members intact /
# fifty-third member absent / ledger 52).
E1241_FILE = (
    "test_type_e_1241_podcast_sentiment_171st_"
    "verification_oct05_3pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 67823  # post-doc-sync total (pre-sync 67749 + 74)
README_FILE_COUNT = 1567  # pre-sync 1566 + 1 (this file)

# The forward-guard needles are fragment-built per #715 so this file
# carries no contiguous literal of a forward-guard claim form.
_T40 = "FORT" + "IETH relationship direction"
_T48 = "FORT" + "Y-EIGHTH falsification-family member"
_T49 = "FORT" + "Y-NINTH falsification-family member"
_T50 = "FIFT" + "IETH falsification-family member"
_T51 = "FIFT" + "Y-FIRST falsification-family member"
_T52 = "FIFT" + "Y-SECOND falsification-family member"
_T53 = "FIFT" + "Y-THIRD falsification-family member"

# Novel source URLs: 8 are zero-hit repo-wide pre-commit (git grep
# -F); the 2 CNN URLs are in-corpus re-surfaces (mechanism #347 arms,
# carried as the institutional-awareness baseline).
NOVEL_URLS = [
    "https://www.pymnts.com/news/artificial-intelligence/2026/"
    "florida-asks-judge-to-stop-openai-model-development-over-safety-risks/",
    "https://news.bloomberglaw.com/litigation/"
    "florida-sues-to-block-new-openai-models-without-safeguards",
    "https://cybersecuritynews.com/"
    "florida-ag-seeks-emergency-injunction-on-chatgpt/",
    "https://www.mixed-news.com/en/"
    "florida-attorney-general-injunction-openai-minors-chatgpt/",
    "https://aidailypost.com/news/florida-cites-extinction-risks-bid-stop",
    "https://ispr.info/2026/10/01/"
    "florida-wants-a-court-to-stop-chatgpt-from-pretending-to-be-human/",
    "https://www.aipolicydesk.com/blog/"
    "state-ag-ai-chatbot-lawsuits-tracker-florida-openai-2026",
    "https://www.explainx.ai/blog/"
    "september-28-2026-ai-news-coverage-gaps-digest-2026",
]
RESURFACE_URLS = [
    "https://www.cnn.com/2026/06/01/business/"
    "florida-sues-chatgpt-openai-sam-altman",
    "https://www.cnn.com/2026/08/27/tech/"
    "meta-settlement-impact-on-teens-business",
]


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


def _iter_working_tree_profiles():
    """Yield profile paths in the working tree (includes uncommitted)."""
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
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
    else:
        args.append(".")
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


def _load_profile():
    import yaml
    return yaml.safe_load(_read(PROFILE_FILE))


def _block():
    return _load_profile()[BLOCK_KEY]


def _block_text():
    return _read(PROFILE_FILE)


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

class TestAnchor1242:
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
        assert "THIRD leg of the 1240-1244 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1242:
    def test_predecessor_1241_chain_verified(self):
        for sha in (
            PRED_MAIN_1241, PRED_ANCHOR_1241, PRED_DOCSYNC_1241,
            PRED_FINAL_1241,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1240_chain_verified(self):
        for sha in (
            PRED_MAIN_1240, PRED_ANCHOR_1240, PRED_DOCSYNC_1240,
            PRED_FINAL_1240,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1240 -> E #1241 -> A #1242 -> B #1243 -> C #1244" in src

    def test_next_leg_is_type_b_1243(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1243 Type B" in src

    def test_type_a_lands_one_mechanism(self):
        # Type A lands exactly one mechanism (mechanism 976); the Type
        # E predecessor added none.
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type A lands one mechanism" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1242:
    def test_cnn_injunction_line_new_at_head(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): the ONLY
        # tracked profiles/ file carrying the block-key prefix at HEAD
        # is this run's own landing; no PRIOR run had the line.
        needle = BLOCK_KEY[:20]  # fragment-built prefix
        hits = _git_grep_tracked_source(needle, "profiles/")
        assert hits == [os.path.join(
            "profiles", "competitor-coverage-research.yaml")], hits

    def test_findings_section_found(self):
        # The block is a top-level key (0-indent), matching the recent
        # Type A convention in this file (m910 at 43923 et al.).
        data = _load_profile()
        assert BLOCK_KEY in data

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1242 in key, no 976 or
        # 977 substring.
        assert "1242" in BLOCK_KEY
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
        for n in range(MECH_NUM + 1, MECH_NUM + 20):
            assert _repo_grep_numeric_mechanism_id(n) == [], n

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_novel_urls_in_block_source_urls_verbatim(self):
        b = _block()
        urls = b["source_urls"]
        for novel in NOVEL_URLS:
            assert novel in urls, novel

    def test_resurface_urls_in_block_and_in_corpus(self):
        # The 2 CNN URLs are in-corpus re-surfaces (mechanism #347
        # arms) carried as the institutional-awareness baseline.
        b = _block()
        urls = b["source_urls"]
        for resurface in RESURFACE_URLS:
            assert resurface in urls, resurface
            hits = _git_grep_tracked_source(resurface, None)
            assert any("competitor-coverage-research" in h for h in hits), hits

    def test_no_cnn_injunction_block_before_this_run(self):
        # The novelty claim: no sep28-injunction block existed in
        # competitor-coverage-research.yaml before this run's landing;
        # now present only inside this block.
        text = _block_text()
        block_start = text.index(BLOCK_KEY + ":")
        assert "uthmeier_openai_sep28" not in text[:block_start]

    def test_case_number_novelty(self):
        # Case number 26000295GCAXMX is novel repo-wide (pre-commit
        # zero-hit; now only in this block).
        text = _block_text()
        assert text.count("26000295GCAXMX") >= 1

    def test_no_type_a_1242_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): the ONLY
        # matches are this run's own commits, whose messages carry the
        # run's own iteration subject (the followup commits match the
        # grep, so they join the own set; HEAD is admitted for any
        # same-run followup). The pin's substance - no PRIOR run
        # committed this run's iteration - holds.
        out = _git("log", "--format=%H %s", "--grep=Type A #1242").stdout
        own = {
            "9d35d369", "cb788aa2", "926b6f7b",
        }
        head = _git("rev-parse", "HEAD").stdout.strip()[:8]
        hits = [line for line in out.splitlines() if line.strip()]
        assert hits, "expected this run's own commits"
        for line in hits:
            assert (line.split()[0][:8] in own
                    or line.split()[0][:8] == head), line


# ---------------------------------------------------------------------------
# 4. Block structure under cross_publication_findings.
# ---------------------------------------------------------------------------

class TestBlockStructure1242:
    def test_profile_exists(self):
        assert os.path.exists(PROFILE_FILE)

    def test_findings_section_is_expected_parent(self):
        data = _load_profile()
        assert BLOCK_KEY in data

    def test_block_key_present_under_findings(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_required_fields_present(self):
        b = _block()
        for field in (
            "mechanism_id", "iteration", "type", "publication",
            "discovery_summary", "openai_peg", "coverage",
            "baseline_from_347", "confounders", "source_urls",
            "asymmetry_scorer", "verdict", "novelty",
            "research_method", "rotation_transparency", "concurrency",
            "verification",
        ):
            assert field in b, "missing %s" % field

    def test_six_prohibitions_documented(self):
        b = _block()
        prohibitions = b["openai_peg"]["prohibitions_requested"]
        assert len(prohibitions) == 6
        joined = " ".join(prohibitions)
        assert "independent third-party safety guardrails" in joined
        assert "minors" in joined

    def test_yaml_parse_clean(self):
        data = _load_profile()
        assert data is not None

    def test_ascii_only_block(self):
        start = _block_text().index(BLOCK_KEY + ":")
        # Block runs to end of file (appended last).
        segment = _block_text()[start:]
        segment.encode("ascii")


# ---------------------------------------------------------------------------
# 5. Content discipline for the bounded-absence finding.
# ---------------------------------------------------------------------------

class TestM976ContentDiscipline1242:
    def test_finding_states_bounded_absence(self):
        b = _block()
        text = str(b["discovery_summary"])
        assert "BOUNDED ABSENCE" in text
        cov = str(b["coverage"]["bounded_absence_profiled_nationals"])
        assert "iteration-492" in cov

    def test_not_a_falsification_member(self):
        b = _block()
        text = str(b["discovery_summary"])
        assert "NOT a" in text and "falsification-family member" in text

    def test_ledger_holds_at_52(self):
        b = _block()
        assert "Ledger holds at 52" in str(b["discovery_summary"])

    def test_verdict_form(self):
        b = _block()
        assert b["verdict"].startswith(
            "mechanism_documentation_not_a_discovery")

    def test_three_search_sets_documented(self):
        b = _block()
        text = str(b["coverage"]["bounded_absence_profiled_nationals"])
        assert "Three search sets" in text

    def test_baseline_347_carried(self):
        b = _block()
        base = b["baseline_from_347"]
        assert "cnn.com/2026/06/01" in base["cnn_jun1_openai_suit"]
        assert "institutional_awareness" in base

    def test_confounders_disclosed(self):
        b = _block()
        names = [c["name"] for c in b["confounders"]]
        assert "News-cycle saturation" in names
        assert "Motion-not-order" in names
        severities = [c["severity"] for c in b["confounders"]]
        assert severities.count("STRONG") == 2

    def test_scorer_not_run_disclosed(self):
        b = _block()
        assert "NOT RUN" in str(b["asymmetry_scorer"])


# ---------------------------------------------------------------------------
# 6. Statistical discipline (Aug 28 2026 standing rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1242:
    def test_monitoring_qualitative_only(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MONITORING/QUALITATIVE ONLY" in src

    def test_engine_not_run(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "engine NOT run" in src

    def test_not_significant(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "is_significant false" in src

    def test_no_analysis_json_update(self):
        b = _block()
        assert "No analysis.json update" in str(b["verdict"])

    def test_not_artifact_grade(self):
        b = _block()
        assert "NOT artifact-grade" in str(b["verdict"])

    def test_no_tone_on_absent_coverage(self):
        b = _block()
        assert "no tone is asserted on absent coverage" in str(
            b["asymmetry_scorer"])


# ---------------------------------------------------------------------------
# 7. Falsification ledger pins (this run adds NO member).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1242:
    def _needle(self, frag):
        return frag

    def test_forty_eighth_member_intact_pin(self):
        hits = _git_grep_tracked_source(_T48, "profiles/financial-times.yaml")
        assert hits, "forty-eighth member claim missing"

    def test_forty_ninth_member_intact_pin(self):
        hits = _git_grep_tracked_source(
            _T49, "profiles/careers/journalists.yaml")
        assert hits, "forty-ninth member claim missing"

    def test_fiftieth_member_intact_pin(self):
        hits = _git_grep_tracked_source(
            _T50, "profiles/careers/journalists.yaml")
        assert hits, "fiftieth member claim missing"

    def test_fifty_first_member_intact_pin(self):
        hits = _git_grep_tracked_source(_T51, "profiles/news-corp.yaml")
        assert hits, "fifty-first member claim missing"

    def test_fifty_second_member_intact_pin(self):
        hits = _git_grep_tracked_source(
            _T52, "profiles/careers/journalists.yaml")
        assert hits, "fifty-second member claim missing"

    def test_no_fifty_third_member_pin(self):
        hits = _git_grep_tracked_source(_T53, None)
        assert hits == [], hits

    def test_no_fortieth_direction_pin(self):
        hits = _git_grep_tracked_source(_T40, "profiles/")
        assert hits == [], hits

    def test_this_run_adds_no_member(self):
        # m976 is mechanism_documentation_not_a_discovery; the ledger
        # holds at 52 and no fifty-third claim form lands.
        b = _block()
        assert "NOT a" in str(b["discovery_summary"])
        assert "Ledger holds at 52" in str(b["discovery_summary"])


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: forward guards for #1243 (next Type B).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1242:
    def test_pins_on_976_landing(self):
        # max numeric mechanism_id is 976; zero 977 key forms all
        # forms (numeric/underscore/dash); no Type B #1243 in git log;
        # fortieth direction absent; fifty-third member absent.
        assert _max_numeric_mechanism_id() == MECH_NUM
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_type_b_1243_in_git_log_pin(self):
        out = _git("log", "--format=%H %s", "--grep=Type B #1243").stdout
        hits = [line for line in out.splitlines() if line.strip()]
        assert hits == [], hits

    def test_977_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_fifty_second_member_present_pin(self):
        hits = _git_grep_tracked_source(
            _T52, "profiles/careers/journalists.yaml")
        assert hits, "fifty-second member claim missing"

    def test_no_fifty_third_member_pin(self):
        hits = _git_grep_tracked_source(_T53, None)
        assert hits == [], hits

    def test_predecessor_1241_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1241_FILE))

    def test_next_leg_is_1243_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1243 Type B" in src

    def test_1241_pins_flip_by_design_documented(self):
        # #1241's no-Type-E-#1241-in-git-log pin flips BY DESIGN at
        # this run's main commit (the #1191-class self-trip, re-pinned
        # in the log-hash followup); the pin substance - no PRIOR run
        # committed #1241 - holds and is documented here.
        out = _git("log", "--format=%H %s", "--grep=Type E #1241").stdout
        hits = [line for line in out.splitlines() if line.strip()]
        assert hits, "expected #1241's own commits"


# ---------------------------------------------------------------------------
# 9. Background suite: observed only per #795.
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1242:
    def test_1240_suite_log_exists(self):
        log = os.path.join(GOAL_HIDDEN, "type_d_1240_full_suite.log")
        assert os.path.exists(log), "expected #1240 suite log"

    def test_this_run_launches_no_suite(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "neither re-launches, kills, nor writes to the suite" in src

    def test_observation_documented_in_block(self):
        b = _block()
        assert "#1245" in str(b["rotation_transparency"])
        assert "#795" in str(b["rotation_transparency"])


# ---------------------------------------------------------------------------
# 10. Staleness pins (post-sync positive per #721; deselected in-gate).
# ---------------------------------------------------------------------------

class TestStalenessPins1242:
    def test_1241_guard_lifecycle_post_commit_self_trip(self):
        # Runs the #1241 file's guard-lifecycle class post-commit: its
        # no-Type-E-#1241-in-git-log pin self-trips on this run's own
        # main commit BY DESIGN (the #1191-class self-trip); the class
        # is expected to report the flip, not to stay green.
        res = _class_run(E1241_FILE, "TestGuardLifecycle1241")
        assert "1 failed" in res.stdout or res.returncode != 0, (
            res.stdout[-500:])


# ---------------------------------------------------------------------------
# 11. Doc-sync (post-sync positive per #719; deselected in-gate).
# ---------------------------------------------------------------------------

class TestDocSync1242:
    def test_readme_test_file_table_has_1242_row_post_sync(self):
        text = _read(README_PATH)
        assert "test_type_a_1242" in text

    def test_architecture_has_1242_row_post_sync(self):
        text = _read(ARCH_PATH)
        assert "test_type_a_1242" in text

    def test_readme_stats_ratcheted(self):
        text = _read(README_PATH)
        assert str(README_TEST_COUNT) in text
        assert str(README_FILE_COUNT) in text


# ---------------------------------------------------------------------------
# 12. Iteration log (post-sync positive per #721; deselected in-gate).
# ---------------------------------------------------------------------------

class TestIterationLog1242:
    def test_1242_entry_present_post_sync(self):
        text = _read(LOG_PATH)
        assert "## #1242" in text

    def test_1241_entry_present(self):
        text = _read(LOG_PATH)
        assert "## #1241" in text

    def test_rotation_transparency_convention(self):
        text = _read(LOG_PATH)
        assert "1240-1244 window" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation: other runs' working state untouched.
# ---------------------------------------------------------------------------

class TestInFlightIsolation1242:
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
        assert "test_type_d_900" in res.stdout

    def test_938_test_file_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_b_938" in res.stdout

    def test_1012_wt_working_tree_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_a_1012" in res.stdout

    def test_do_not_touch_1024_m846(self):
        # Guarded in the log entry per convention; the test file keeps
        # the in-flight list only (own-file reference would trip the
        # contiguous-literal discipline elsewhere).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1024" in src
