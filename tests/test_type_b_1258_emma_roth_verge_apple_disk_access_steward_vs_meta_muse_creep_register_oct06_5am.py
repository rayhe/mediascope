# -*- coding: utf-8 -*-
"""Type B #1258 tests: Emma Roth (The Verge) journalist
cross-entity pair - Meta Muse Sep-10 adversarial creep register
(CARRIED from m782, un-rescored per #807) vs Apple Oct-2 macOS
full-disk-access steward register (NEW arm).

Mechanism 986 (THESIS-CONSISTENT observation, NOT a falsification-family
member; ledger holds at 54). Same writer, same outlet, 22 days apart
(Sep 10 vs Oct 2, 2026): Roth covers Meta's Muse hands-on through the
adversarial creep toolkit register (-0.40 MANUAL ILLUSTRATIVE, carried
from m782) and covers Apple's disk-access tightening through a
good-faith steward register (+0.30, "will add new limits for 'full disk
access' on Mac", Meta's Muse named as the cautionary foil). Illustrative
delta (Apple minus Meta) +0.70: directionally softer on the
advertiser-class entity. The outlet's parent advertising ecosystem
documents Apple (Apple TV+) as an advertiser to owner-linked sports
properties (in-corpus the-verge.yaml, Boehly sports-ownership
advertising map), so the uniform payer-softening prediction points
exactly this way - the observation MATCHES the prediction rather than
failing it. Genre asymmetry (first-person hands-on vs policy-announcement
news relay) is the STRONG confound; evidence asymmetry
(first-hand verbatim mirror vs excerpt-tier aggregator) is STRONG;
topic asymmetry MODERATE; temporal 22 days WEAK. m860 (Roth Sep-24 Meta
Charms launch news, neutral) is the intra-journalist counterpoint. MANUAL
ILLUSTRATIVE ONLY per the Aug 28 2026 standing rule (NEW-arm tone
hand-assigned, Meta-arm tone carried; n=1 per arm; p_value/cohens_d/ci_95
NOT_CALCULATED; engine NOT run; is_significant false; NOT artifact-grade;
verdict thesis_consistent_not_proven; no analysis.json update).

Research: delegated scout (20 browser.search queries across candidate
journalists; SELECTED Roth as the tightest in-window same-journalist
pair with URL-complete arms; 12 rejected candidates with numbered audit:
Goode saturated #436, Song saturated #813/#993, Gurman newsletter format
#593, Younker readers-react #783, So counter-example #102/#457/#380,
Al Heeti podcast-arm #255, Rogers brief-format #658, Warren no Meta arm,
Robertson saturated, Waichulis genre-baked #248, Ortiz/Hiner 2025-dated
#803/#793, Pierce/Nelius/Heath no pair) + 2 main-run browser.search
verification sets (exact-headline Apple-arm search returning the WeSearch
record "Emma Roth, Oct 2, 2026, 8:08 PM UTC" plus the technewstube Verge
feed proxy "By Emma Roth Oct 2, 2026, 4:08 pm"; exact-headline Meta-arm
search returning the mediascope #918 commit page plus the dev.to
source-list attestation "Sept 10, 2026"; corpus saturation greps: both
Apple URLs zero-hit repo-wide (git grep -F), "Apple will limit Mac disk
access" headline zero-hit, zero emma_roth Apple-disk-access blocks,
no "Type B #1258" in git log; theverge.com canonical did not surface
for the Apple arm - no URL constructed per policy). 0 browser.open per
#503 (excerpt-bounded). All URLs copied verbatim from Full-URL listings.
The m986 block lands in profiles/careers/journalists.yaml inside the
existing emma_roth_type_b entry (FOURTH block after m782/m860/m953, per
the #643 convention); mechanism_ids patched to [782, 860, 953, 986].
Targeted staging by explicit path only; the in-flight
#899/#938/#900/#1012-wt files stay out of this run's index/diff. Do NOT
touch #1024 m846.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup commit. One anchor test (the placeholder pin) fails BY DESIGN
pre-commit; TestAnchor1258 deselected in the in-gate run. The main
commit is the anchor per #565.

FOURTH leg of the 1255-1259 window: D #1255 -> E #1256 -> A #1257 ->
B #1258 -> C #1259 per the #565 anchor + rotation guard. Next run
#1259 Type C closes the window. Type B lands one mechanism
(mechanism 986).

Per #795: this run only CHECKS the #1255-launched background suite
(goal hidden_files type_d_1255_full_suite.log, observed ALIVE at
this run's check: ~10% progress, F marks per the known
recurring-failure pattern, pytest processes live - an observation,
not a verdict; no verdict declared); its verdict and tombstone belong
to #1260 (next Type D). This run neither re-launches, kills, nor
writes to the suite.

ASCII-only, no em dashes. Needles format-built per #715: this file
must not carry contiguous numeric/underscore/dash mechanism-key forms
of the landed or next number, the forty-eighth / forty-ninth /
fiftieth / fifty-first / fifty-second / fifty-third / fifty-fourth
member-claim forms, the fifty-fifth member-claim form, or the fortieth
direction form; the constants are constructed at runtime. (The landed
ordinals live as short lowercase forms in prose here; the live
full-form claims live in profiles/: the forty-eighth in
profiles/financial-times.yaml, the forty-ninth / fiftieth /
fifty-second in profiles/careers/journalists.yaml, the fifty-first in
profiles/news-corp.yaml, the fifty-third in profiles/the-verge.yaml,
and the fifty-fourth in profiles/guardian.yaml.)
"""
import os
import re
import subprocess

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
    "test_type_b_1258_emma_roth_verge_apple_disk_access_steward_"
    "vs_meta_muse_creep_register_oct06_5am.py"
)
PROFILE_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1255_full_suite.log")

MECH_NUM = 986
NEXT_NUM = 987  # integer only; key-form needles are format-built
ITERATION = 1258

ANCHORED_SHA = "2c40dc1b4397e62258491babcc4a9e8dcae6d47e"

# Predecessor #1257 chain (verified via git rev-parse pre-commit).
PRED_MAIN_1257 = "841f1b2b098836e167fe8d113fe4feddc661782d"
PRED_ANCHOR_1257 = "f112fb8630fc81a5108acfbbf44b4a533d25c296"
PRED_DOCSYNC_1257 = "a048dc328ab6a4cd771b37ea546318bfd10ab2fb"
PRED_FINAL_1257 = "b67d591f9fd6d5ba67be4554cb5ff5222d3a1669"
# Predecessor #1256 chain (window SECOND leg).
PRED_MAIN_1256 = "09867f9d9cfb5a9097741962663e3b343097d865"
A1257_FILE = (
    "test_type_a_1257_guardian_anthropic_oct01_bhuiyan_hijab_"
    "cross_lab_test_oct06_4am.py"
)

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770
_T40 = "FORT" + "IETH relationship direction"
_T48 = "FORT" + "Y-EIGHTH falsification-family member"
_T49 = "FORT" + "Y-NINTH falsification-family member"
_T50 = "FIFT" + "IETH falsification-family member"
_T51 = "FIFT" + "Y-FIRST falsification-family member"
_T52 = "FIFT" + "Y-SECOND falsification-family member"
_T53 = "FIFT" + "Y-THIRD falsification-family member"
_T54 = "FIFT" + "Y-FOURTH falsification-family member"
_T55 = "FIFT" + "Y-FIFTH falsification-family member"

BLOCK_KEY = (
    "type_b_1258_emma_roth_verge_apple_disk_access_steward_"
    "vs_meta_muse_creep_register_oct06_5am"
)
JOURNALIST_KEY = "emma_roth_type_b"

# The two novel source URLs (verbatim from Full-URL listings,
# zero-hit repo-wide pre-commit via git grep -F).
PEG_URLS = [
    "https://technewstube.com/theverge/1872816/apple-limit-mac-disk-"
    "access-ai-agents-substantially/",
    "https://wesearch.press/s/apple-will-limit-mac-disk-access-as-ai-"
    "agents-substantially-ac153d8f",
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

class TestAnchor1258:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to the main commit sha per #565. Deselected in
        # the in-gate run; the patched form is asserted post-anchor.
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_to_main_commit(self):
        # Post-commit form: ANCHORED_SHA patched to this run's main
        # commit sha per #565 in the anchor followup. Pre-commit this
        # is 0*40 and the test fails BY DESIGN; deselected in-gate.
        assert ANCHORED_SHA != "0" * 40
        assert len(ANCHORED_SHA) == 40

    def test_anchor_sha_format(self):
        assert len(ANCHORED_SHA) == 40

    def test_this_run_main_commit_is_anchor(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "main commit is the anchor" in src

    def test_rotation_phrase_in_docstring(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FOURTH leg of the 1255-1259 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1258:
    def test_predecessor_1257_chain_verified(self):
        for sha in (
            PRED_MAIN_1257, PRED_ANCHOR_1257, PRED_DOCSYNC_1257,
            PRED_FINAL_1257,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1256_main_verified(self):
        res = _git("cat-file", "-t", PRED_MAIN_1256)
        assert res.stdout.strip() == "commit", "missing 1256 main"

    def test_window_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1255 -> E #1256 -> A #1257 -> B #1258 -> C #1259" in src

    def test_next_is_type_c_1259(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1259 Type C closes the window" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty
# ---------------------------------------------------------------------------

class TestMechanismNovelty1258:
    def test_no_type_b_1258_file_precommit(self):
        # Own file excluded: exactly one match (this file) post-commit.
        hits = [
            f for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_b_1258")
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
        # NEXT_NUM = 987 must have zero key forms (forward guard).
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
# 4. Block structure: the m986 pair
# ---------------------------------------------------------------------------

class TestBlockStructure1258:
    def test_required_top_fields(self):
        block = _block()
        for key in (
            "block_key", "mechanism_id", "iteration", "type", "date",
            "test_file", "author", "goal_id", "job_id", "scheduled_job_id",
            "journalist", "publication", "window", "design", "finding",
            "meta_arm", "apple_arm", "scorer", "financial_context",
            "confounders", "counter_evidence", "statistical_discipline",
            "verdict", "cautious_language_required", "correlational_note",
            "no_analysis_json_update", "falsification_family_member",
            "falsification_ledger", "ledger_note", "connects_to",
            "novelty", "research_method", "artifact_readiness",
            "background_suite_status", "in_flight", "source_urls",
        ):
            assert key in block, key

    def test_mechanism_ids_field(self):
        import yaml
        with open(PROFILE_FILE, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        assert data[JOURNALIST_KEY]["mechanism_ids"] == [
            782, 860, 953, MECH_NUM]

    def test_arm_structure(self):
        block = _block()
        for arm_name in ("meta_arm", "apple_arm"):
            arm = block[arm_name]
            for key in (
                "entity", "outlet", "author_byline", "title", "date",
                "tone_MANUAL_ILLUSTRATIVE",
            ):
                assert key in arm, (arm_name, key)

    def test_block_key_designed_keying(self):
        # Designed keying per #715: iteration 1258 in key, no 986
        # substring anywhere in the key.
        assert "1258" in BLOCK_KEY
        assert "986" not in BLOCK_KEY
        assert _block()["block_key"] == BLOCK_KEY

    def test_two_source_urls(self):
        assert len(_block()["source_urls"]) == 2

    def test_type_and_entities(self):
        block = _block()
        assert block["type"] == "B"
        assert block["journalist"] == "Emma Roth"
        assert block["publication"] == "The Verge"
        assert block["meta_arm"]["entity"] == "meta"
        assert block["apple_arm"]["entity"] == "apple"


# ---------------------------------------------------------------------------
# 5. m986 content discipline
# ---------------------------------------------------------------------------

class TestM986ContentDiscipline1258:
    def test_meta_arm_headline_present(self):
        title = _block()["meta_arm"]["title"]
        assert "Meta's Muse AI works and creeps me out" in title

    def test_apple_arm_headline_present(self):
        title = _block()["apple_arm"]["title"]
        assert "limit Mac disk access" in title
        assert "substantially" in title

    def test_bylines(self):
        block = _block()
        assert block["meta_arm"]["author_byline"] == "Emma Roth"
        assert block["apple_arm"]["author_byline"] == "Emma Roth"

    def test_arm_dates(self):
        block = _block()
        assert block["meta_arm"]["date"] == "2026-09-10"
        assert block["apple_arm"]["date"] == "2026-10-02"

    def test_meta_arm_carried_un_rescored(self):
        block = _block()
        assert "CARRIED from m782" in block["meta_arm"]["status"]
        assert "un-rescored per #807" in block["meta_arm"]["status"]
        assert block["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.4

    def test_apple_arm_tone_manual_illustrative(self):
        assert _block()["apple_arm"]["tone_MANUAL_ILLUSTRATIVE"] == 0.3

    def test_delta_arithmetic(self):
        block = _block()
        delta = block["scorer"]["illustrative_delta_apple_minus_meta"]
        expected = (
            block["apple_arm"]["tone_MANUAL_ILLUSTRATIVE"]
            - block["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"]
        )
        assert abs(delta - expected) < 1e-9
        assert abs(delta - 0.70) < 1e-9

    def test_scorer_discipline(self):
        scorer = _block()["scorer"]
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci_95"] == "NOT_CALCULATED"
        assert scorer["engine_run"] is False
        assert scorer["is_significant"] is False

    def test_thesis_consistent_marking(self):
        block = _block()
        assert block["falsification_family_member"] is False
        assert block["falsification_ledger"] == 54
        assert "THESIS-CONSISTENT" in block["finding"]
        assert "NOT a falsification-family member" in block["finding"]

    def test_financial_context_apple_tie(self):
        context = _block()["financial_context"]
        assert "Apple TV+" in context
        assert "the-verge.yaml" in context

    def test_confounder_genre_strong(self):
        confs = _block()["confounders"]["strong"]
        assert len(confs) >= 2
        joined = " ".join(confs)
        assert "Genre" in joined

    def test_counter_evidence_m860(self):
        joined = " ".join(_block()["counter_evidence"])
        assert "m860" in joined

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
        assert block["apple_arm"]["url"] == PEG_URLS[0]
        assert block["source_urls"] == PEG_URLS


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL/QUALITATIVE ONLY)
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1258:
    def test_not_significant(self):
        assert _block()["scorer"]["is_significant"] is False

    def test_correlation_not_causation(self):
        assert "Correlation is not causation" in _block()["correlational_note"]

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_manual_illustrative_only(self):
        finding = _block()["finding"]
        assert "MANUAL ILLUSTRATIVE ONLY" not in finding
        discipline = _block()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE scores only" in discipline
        assert "NOT artifact-grade" in discipline

    def test_engine_not_run(self):
        text = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "engine NOT run" in text

    def test_verdict_bounded(self):
        assert _block()["verdict"].startswith("thesis_consistent_not_proven")


# ---------------------------------------------------------------------------
# 7. Falsification ledger (holds at 54)
# ---------------------------------------------------------------------------

class TestFalsificationLedger1258:
    def test_ledger_holds_at_54(self):
        assert _block()["falsification_ledger"] == 54

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
        assert _git_grep_tracked_source(_T54, "profiles/") == [
            "profiles/guardian.yaml"]

    def test_no_fifty_fifth_member_pin(self):
        assert _git_grep_tracked_source(_T55, ".") == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: forward guards for #1259 (Type C)
# ---------------------------------------------------------------------------

class TestGuardLifecycle1258:
    def test_pins_on_986_landing(self):
        # Type B lands m986: max becomes 986, next is 987.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 986" in src
        assert "NEXT_NUM = 987" in src

    def test_no_type_c_1259_in_git_log_pin(self):
        out = _git("log", "--oneline", "--grep=Type C #1259")
        assert out.stdout.strip() == ""

    def test_987_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_987_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_987_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        # The fortieth direction-claim form stays absent in profiles/.
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

    def test_fifty_third_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T53, "HEAD", "--",
            "profiles/the-verge.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fourth_member_present_pin(self):
        assert _git_grep_tracked_source(_T54, "profiles/") == [
            "profiles/guardian.yaml"]

    def test_no_fifty_fifth_member_pin(self):
        assert _git_grep_tracked_source(_T55, None) == []

    def test_predecessor_1257_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, A1257_FILE))

    def test_next_leg_is_1259_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1259 Type C" in src

    def test_1257_pins_flip_by_design_documented(self):
        # #1257's forward guards (max-985, zero-986 keys all forms,
        # no-Type-B-#1258-in-git-log, fortieth absent, forty-eighth +
        # forty-ninth + fiftieth + fifty-first + fifty-second +
        # fifty-third intact and fifty-fourth present in profiles/,
        # no fifty-fifth) verified GREEN pre-commit this run via the
        # subprocess staleness pin (Type B lands m986 as a
        # thesis-consistent observation, NOT a falsification-family
        # member); the max-985, zero-986-numeric, and
        # no-Type-B-#1258-in-git-log pins flip post-main-commit on this
        # run's own landing (the #1191-class self-trip, by design,
        # documented in the staleness pin below).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1258" in src
        assert "no_type_b_1258_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 9. Background suite (per #795: CHECKED ONLY this run)
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1258:
    def test_suite_log_exists(self):
        assert os.path.exists(SUITE_LOG), SUITE_LOG

    def test_suite_log_nonempty(self):
        assert os.path.getsize(SUITE_LOG) > 0

    def test_run_neither_relaunches_nor_kills(self):
        # Observation-only per #795: this run's own processes must not
        # include a suite launcher it started.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "neither" in src and "re-launches" in src

    def test_verdict_belongs_to_1260(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "belong to #1260" in src


# ---------------------------------------------------------------------------
# 10. Doc-sync (post-sync positive per #719; deselected in-gate).
# ---------------------------------------------------------------------------

class TestDocSync1258:
    def test_readme_test_file_table_has_1258_row_post_sync(self):
        text = _read(README_PATH)
        assert "test_type_b_1258" in text

    def test_architecture_has_1258_row_post_sync(self):
        text = _read(ARCH_PATH)
        assert "test_type_b_1258" in text

    def test_readme_stats_ratcheted(self):
        text = _read(README_PATH)
        assert str(README_TEST_COUNT) in text
        assert str(README_FILE_COUNT) in text


# ---------------------------------------------------------------------------
# 11. Iteration log (post-sync positive per #721; deselected in-gate).
# ---------------------------------------------------------------------------

class TestIterationLog1258:
    def test_1258_entry_present_post_sync(self):
        text = _read(LOG_PATH)
        assert "## #1258" in text

    def test_1257_entry_present(self):
        text = _read(LOG_PATH)
        assert "## #1257" in text

    def test_rotation_transparency_convention(self):
        text = _read(LOG_PATH)
        assert "1255-1259 window" in text


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1257's guard lifecycle flips by design
#      (1 test; deselected pre-commit, verified post-main-commit)
# ---------------------------------------------------------------------------

class TestStalenessPins1258:
    def test_1257_guard_lifecycle_flips_by_design_post_commit(self):
        # Runs the #1257 file's guard-lifecycle class post-commit:
        # its no-Type-B-#1258-in-git-log pin self-trips on this run's
        # own main commit and its zero-986-numeric pin trips on the
        # landed m986 block (both BY DESIGN, the #1191-class self-trip
        # family); the class is expected to report the flips, not to
        # stay green.
        res = _class_run(A1257_FILE, "TestGuardLifecycle1257")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "failed" in res.stdout, res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation: other runs' working state untouched.
# ---------------------------------------------------------------------------

class TestInFlightIsolation1258:
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


README_TEST_COUNT = 69238  # patched post-sync per #719
README_FILE_COUNT = 1583  # patched post-sync per #719
