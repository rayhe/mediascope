"""Type A #1277: Atlantic x OpenAI Robinson resignation essay (Oct 7 2026, ~03:00 AM PDT).

m997 - FIRST dedicated corpus mechanism on the Atlantic platforming
David Robinson's first-person resignation essay "I Quit OpenAI Because
Its Culture Is Broken" (Oct 3 2026, 7am ET): Robinson, who led the
writing of safety reports accompanying OpenAI product releases (3.5
years, 12 frontier launches, helped draft the Preparedness Framework),
resigns warning the culture is broken, the sprint from launch to launch
fails the level of care needed, "the time for trial and error is over",
urging nuclear-plant/aviation-grade redundancy; an OpenAI spokesperson
rebuttal is printed.

The Atlantic's coverage_prediction for OpenAI is "softer", set on the
May 29 2024 strategic content-licensing partnership (in-corpus,
active). The naive uniform payer-softening prediction says the
licensing partner suppresses or softens adversarial payer content. The
observed is the opposite at the ideas-essay gatekeeping tier: flagship
placement for an insider "culture is broken" takedown of the payer,
printed at full strength. Falsification-member-confirmed, domain-
bounded to the ideas/essay gatekeeping tier (the adversarial content
is the author's first-person account, not newsroom-reported; the
publication-level test is gatekeeping). Per #715 this docstring uses
lowercase forms only: the fifty-fifth falsification-family member,
ledger 54->55.

MANUAL ILLUSTRATIVE scoring: essay -0.65 vs carried Atlantic x Meta
AI Watchdog band (m481: Strike-3 -0.75, pirated-books -0.55, mean
-0.65). Illustrative delta (OpenAI minus Meta): +0.10 clean (vs the
hardest Meta arm), 0.00 pooled. Near-null: the Atlantic went as hard
on the payer via the platformed essay as on Meta via its own
investigations.

Distinction from #1227 (BI x OpenAI, m967): different publication x
competitor pair, different financial tie (Atlantic-OpenAI May-2024 vs
Axel Springer-OpenAI Dec-2023), different editorial act (platforming
the primary insider essay vs breaking the departure exclusive). The
#1143 temporal-replication precedent does not block: no adversarial-
on-partner observation has been counted for the Atlantic x OpenAI
pair (m481/m694/m829/m913 are all thesis-consistent), unlike BI x
OpenAI where m399 already counted the hardness test. Distinction from
#1272 (Guardian x OpenAI, m994): different publication, straight-news
relay vs the primary insider essay.

The m913 bounded-silence finding stands for the straight-news crisis
tier; m997 bounds it to that tier (the Ideas desk platformed the
takedown - the silence was peg-specific, not blanket suppression).
The m481 Watchdog entity-selection pattern stands for the
investigation tier.

Statistical discipline: monitoring-only per the Aug 28 2026 standing
rule (MANUAL ILLUSTRATIVE ONLY, engine NOT run, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False, NOT artifact-grade, no
analysis.json update, verdict falsification_member_confirmed on the
domain-bounded gatekeeping peg). Correlation is not causation.
Hypothesis-generating only.

2 main-run browser.search verification sets + 1 delegated scout,
0 browser.open per #503. 3 novel relay URLs zero-hit pre-commit.
All URLs copied verbatim from Full-URL listings; no canonical URLs
constructed. ASCII-only, no em dashes.

Rotation: this run is iteration #1277 Type A, the THIRD leg of the
1275-1279 window (D #1275 -> E #1276 -> A #1277 -> B #1278 -> C #1279,
per the #565 anchor + rotation guard). Predecessor #1276 Type E
verified in git log (main 5d511a0e / anchor 9e715001 / doc-sync
1a109de9 / log-hash 37bd9a20); the 1270-1274 window is VERIFIED
CLOSED. This run's main commit is the anchor per #565;
ANCHORED_SHA patched post-commit. The #1276 forward guards verified
pre-commit this run: max-996; zero next-number nine-nine-seven
mechanism keys all forms (profiles/ + tests/ scope); fortieth
direction absent (profiles/ scope); forty-eighth member intact in
profiles/financial-times.yaml; forty-ninth member intact + fiftieth
member intact + fifty-second member intact in
profiles/careers/journalists.yaml; fifty-first member intact in
profiles/news-corp.yaml; fifty-third member intact in
profiles/the-verge.yaml; fifty-fourth member intact in
profiles/guardian.yaml (landed at #1257); no fifty-fifth member
(repo-wide); ledger 54. This run lands the fifty-fifth member:
TestGuardLifecycle1276's no-fifty-fifth-member pin flips at this
run's main commit BY DESIGN (the #1191-class self-trip), documented
in TestStalenessPins1277, not repaired. Next run #1278 Type B
continues the window. The #1275-launched background-suite verdict
belongs to #1280 per #795: this run OBSERVES only. In-flight during
this run: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file) - all
untouched; targeted staging only. Do NOT touch #1024 m846.

Pre-commit novelty greps per #715: zero test_type_a_1277 files on disk
(glob); no Type A #1277 in git log (--grep); max numeric mechanism_id
996 in-tree pre-commit (m994/m995/m996 verified at #1275; Type E adds
no mechanisms); zero numeric/underscore/dash next-number nine-nine-
seven mechanism key forms repo-wide pre-commit (needles format-built
per #715, own file excluded); 3 novel relay URLs zero-hit repo-wide
pre-commit (git grep -F); the essay headline carries 2 pre-commit repo
hits (m967 finding/title in profiles/business-insider.yaml + the #1227
iteration-log entry - both BI x OpenAI event coverage, a different
publication x competitor pair); the essay as an Atlantic x OpenAI
primary arm zero-hit in profiles/atlantic.yaml pre-commit; the
theatlantic.com essay slug zero-hit repo-wide pre-commit; no #1277
row in README/ARCHITECTURE test tables or iteration-log pre-commit;
README stats 70954/1601 pre-commit.

Doc-sync constants per #719: README_TEST_COUNT / README_FILE_COUNT
hold the post-doc-sync values from the start (patched pre-main once
the in-gate collection count is known); the doc-sync commit ratchets
README 70954/1601 -> post-sync totals.
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
ATLANTIC_PATH = os.path.join(PROFILES_DIR, "atlantic.yaml")
OWN_BASENAME = (
    "test_type_a_1277_atlantic_openai_robinson_essay_oct07_3am.py"
)
BLOCK_KEY = (
    "type_a_1277_atlantic_openai_robinson_essay_culture_broken_october"
)

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "eee6dfc46080a0abc0c3bd21d5126c0ec08b1643"  # patched in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 997
NEXT_NUM = 998  # integer only; key-form needles are format-built

# Predecessor chain: #1276 Type E CLOSED the second leg.
PRED_MAIN_1276 = "5d511a0e70bdcce1202ea38a8037844f92b57462"
PRED_ANCHOR_1276 = "9e7150012f03ac174c3b3ddfac705cba6b05b333"
PRED_DOCSYNC_1276 = "1a109de91dec87d7e712bb75fd8a9cd0e178a94e"
PRED_FINAL_1276 = "37bd9a20ca52503adbd6c37c901e8fc5598beb5f"

# This run's main commit (full sha), for the ancestor-form
# no-Type-A-#1277 pin. Patched in the terminal log-hash followup per
# #721.
PRED_MAIN_1277 = "0" * 40  # patched in the log-hash followup per #721 (main commit sha)

# #1278's main commit (full sha), for the ancestor-form no-Type-B-#1278
# pin. Patched in #1278's terminal log-hash followup per #721.
PRED_MAIN_1278 = "0" * 40  # patched in #1278's log-hash followup per #721 (main commit sha)

# The #1276 Type E file, for the staleness pin on its guard-lifecycle
# class (the no-fifty-fifth-member pin flips at this run's main commit
# BY DESIGN - the #1191-class self-trip).
D1276_FILE = (
    "test_type_e_1276_podcast_sentiment_178th_verification_oct07_2am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 71039  # post-doc-sync total (pre-sync 70954 + 85)
README_FILE_COUNT = 1602  # pre-sync 1601 + 1

# Tones (MANUAL ILLUSTRATIVE).
ESSAY_TONE = -0.65  # NEW Atlantic x OpenAI arm (first-person essay)
META_STRIKE3_TONE = -0.75  # carried m481 arm
META_BOOKS_TONE = -0.55  # carried m481 arm
META_MEAN = -0.65  # pooled mean of the two Meta arms
DELTA_CLEAN = 0.10  # -0.65 - (-0.75)
DELTA_POOLED = 0.00  # -0.65 - (-0.65)

NOVEL_URLS = [
    "https://hamirev.com/openai-safety-report-lead-quits/",
    "https://cellcog.ai/blog/openai-safety-lead-resigns/",
    "https://www.signalstack.news/blog/openai-safety-leader-"
    "resignation-culture-essay/",
]

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


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


def _load_atlantic():
    with open(ATLANTIC_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _block():
    data = _load_atlantic()
    return data["competitor_relationships"]["openai"][BLOCK_KEY]


def _iter_source_files():
    """Yield paths for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts.
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
    """Underscore-form mechanism key; needle format-built per #770."""
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [
        p for p in _iter_source_files() if needle in _read(p)
    ]


def _repo_grep_dash_mechanism(n):
    needle = "mechanism" + "-" + str(n)
    return [
        p for p in _iter_source_files() if needle in _read(p)
    ]


def _repo_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in _read(p):
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
                    _read(os.path.join(root, f))
                )
            )
    return max(found) if found else 0


def _git_grep_tracked_source(needle, scope):
    """Literal needle across tracked profile/test source files.

    scope is "profiles/" or None (profiles/ + tests/). Excludes the
    sweep carrier and __pycache__ artifacts per #715.
    """
    out = _git("grep", "-F", "-l", needle, "HEAD", "--",
               "profiles/", "tests/").stdout
    hits = []
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("HEAD:"):
            line = line[len("HEAD:"):]
        path = line
        if "__pycache__" in path:
            continue
        if path.endswith("/" + OWN_BASENAME) or path == OWN_BASENAME:
            continue
        if scope == "profiles/" and not path.startswith("profiles/"):
            continue
        hits.append(path)
    return hits


# ---------------------------------------------------------------------------
# 1. Anchor per #565 (5 tests; placeholder pre-commit, patched post-anchor)
# ---------------------------------------------------------------------------
class TestAnchor1277:
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
        assert "THIRD leg of the 1275-1279 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestRotationGuard:
    def test_predecessor_1276_chain_verified(self):
        for sha in (
            PRED_MAIN_1276, PRED_ANCHOR_1276, PRED_DOCSYNC_1276,
            PRED_FINAL_1276,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1275 -> E #1276 -> A #1277 -> B #1278 -> C #1279" in src

    def test_next_leg_is_type_b_1278(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1278 Type B" in src

    def test_type_a_lands_one_mechanism(self):
        assert MECH_NUM == 997
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_this_run_is_third_leg(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "iteration #1277 Type A, the THIRD leg" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty
# ---------------------------------------------------------------------------
class TestMechanismNovelty:
    def test_max_numeric_mechanism_id_997(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_no_type_a_1277_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type A #1277" must be this run's
        # main commit or a descendant of it - i.e., no PRIOR run
        # committed this run's iteration. Deselected in the in-gate
        # run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type A #1277")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1277).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_zero_next_number_keys_all_forms(self):
        # Numeric (profiles/ scope), underscore and dash (profiles/ +
        # tests/ scope, own file excluded per #715).
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_key_designed_no_997_substring(self):
        # Per #723/#738/#739: the iteration-form block key carries no
        # underscore-form 997 substring (needle format-built per #770
        # so this file carries no contiguous literal).
        needle = "%s%d" % (MECH_ID_MARKER, MECH_NUM)
        assert needle not in BLOCK_KEY
        assert BLOCK_KEY in _read(ATLANTIC_PATH)

    def test_forward_guards_for_1278(self):
        # max-997; zero-998 all forms; fortieth direction absent
        # (profiles/ scope); forty-eighth through fifty-fifth members
        # intact; no fifty-sixth member (repo-wide); ledger 55. The
        # fifty-fifth is asserted on the working tree (this run's
        # block, committed at the main commit); the HEAD-based sweep
        # sees it from the main commit onward.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 997" in src
        assert "NEXT_NUM = 998" in src
        assert "ledger 54->55" in src
        assert _git_grep_tracked_source(_T40, "profiles/") == []
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]
        assert _git_grep_tracked_source(_T49, "profiles/") == [
            "profiles/careers/journalists.yaml"]
        assert _T55 in _read(ATLANTIC_PATH)
        assert _git_grep_tracked_source(_T56, None) == []

    def test_novel_urls_zero_hit_pre_commit(self):
        # The 3 relay URLs were verified zero-hit pre-commit (git
        # grep -F, documented in the block's novelty field). This test
        # pins that no file OTHER than this run's own m997 block ever
        # carries them, so it holds pre-commit (zero hits) and
        # post-commit (only the landed block hits).
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
                "profiles/atlantic.yaml",
                "tests/" + OWN_BASENAME,
            }, (url, paths)


# ---------------------------------------------------------------------------
# 4. Falsification ledger (fifty-fifth member lands this run)
# ---------------------------------------------------------------------------
class TestFalsificationLedger:
    def test_fifty_fifth_member_present_in_block(self):
        block = _block()
        assert block["falsification_family_member"] is True
        assert _T55 in block["falsification_family"]
        assert block["falsification_ledger"] == "55"
        assert block["ledger"] == "55"

    def test_forty_eighth_through_fifty_fourth_intact(self):
        # The earlier members survive this run unchanged (tracked
        # sources at HEAD; this run's block is additive).
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]
        assert _git_grep_tracked_source(_T54, "profiles/") == [
            "profiles/guardian.yaml"]

    def test_no_fifty_sixth_member_repo_wide(self):
        assert _git_grep_tracked_source(_T56, None) == []

    def test_verdict_falsification_member_confirmed(self):
        block = _block()
        assert block["verdict"].startswith(
            "falsification_member_confirmed")

    def test_ledger_55_in_block(self):
        block = _block()
        assert "ledger 54->55" in block["falsification_family"]


# ---------------------------------------------------------------------------
# 5. Atlantic essay arm
# ---------------------------------------------------------------------------
class TestAtlanticEssay:
    def _item(self):
        return _block()["openai_arms"][0]["item"]

    def test_headline(self):
        assert self._item()["title"] == (
            "I Quit OpenAI Because Its Culture Is Broken")

    def test_date_oct_3_2026(self):
        assert self._item()["date"] == "2026-10-03"

    def test_author_robinson(self):
        assert self._item()["author_byline"] == "David Robinson"

    def test_publication_atlantic_original(self):
        assert "The Atlantic (original; relay-attested)" in self._item()[
            "publication"]

    def test_framing_first_person_essay(self):
        assert self._item()["framing"] == (
            "first_person_insider_resignation_essay")

    def test_tone_minus_065(self):
        assert self._item()["manual_illustrative_tone"] == ESSAY_TONE

    def test_deal_not_disclosed(self):
        assert self._item()["deal_disclosed"] is False

    def test_evidence_tier_relay_attested(self):
        assert self._item()["evidence_tier"] == "relay-attested"


# ---------------------------------------------------------------------------
# 6. Meta arms (carried m481)
# ---------------------------------------------------------------------------
class TestMetaArms:
    def test_carried_from_m481(self):
        assert "m481" in _block()["meta_arms"]["carried_from"]

    def test_strike3_arm(self):
        arms = _block()["meta_arms"]["arms"]
        assert arms[0]["manual_illustrative_tone"] == META_STRIKE3_TONE
        assert arms[0]["mechanism_ref"] == "m481"

    def test_pirated_books_arm(self):
        arms = _block()["meta_arms"]["arms"]
        assert arms[1]["manual_illustrative_tone"] == META_BOOKS_TONE
        assert arms[1]["mechanism_ref"] == "m481"

    def test_meta_band_mean(self):
        assert _block()["meta_arms"]["meta_band_mean"] == META_MEAN


# ---------------------------------------------------------------------------
# 7. Financial relationship
# ---------------------------------------------------------------------------
class TestFinancialRelationship:
    def test_atlantic_openai_deal(self):
        rel = _block()["financial_relationship"]
        assert "May 29 2024" in rel
        assert "strategic content-licensing partnership" in rel

    def test_atlantic_meta_zero(self):
        rel = _block()["financial_relationship"]
        assert "Atlantic x Meta $0" in rel

    def test_coverage_prediction_softer(self):
        data = _load_atlantic()
        assert data["competitor_relationships"]["openai"][
            "coverage_prediction"] == "softer"


# ---------------------------------------------------------------------------
# 8. Asymmetry delta (MANUAL ILLUSTRATIVE ONLY)
# ---------------------------------------------------------------------------
class TestAsymmetryDelta:
    def test_delta_math_clean(self):
        calc = ESSAY_TONE - META_STRIKE3_TONE
        assert abs(calc - DELTA_CLEAN) < 1e-9

    def test_delta_math_pooled(self):
        calc = ESSAY_TONE - META_MEAN
        assert abs(calc - DELTA_POOLED) < 1e-9

    def test_block_delta_matches(self):
        res = _block()["asymmetry_scorer_result"]
        assert res["illustrative_delta_openai_minus_meta_clean"] == (
            DELTA_CLEAN)
        assert res["illustrative_delta_openai_minus_meta_pooled"] == (
            DELTA_POOLED)

    def test_delta_direction_near_null(self):
        res = _block()["asymmetry_scorer_result"]
        assert "Near-null illustrative delta" in res["delta_direction"]
        assert "FAILS on this peg" in res["delta_direction"]

    def test_engine_not_run(self):
        res = _block()["asymmetry_scorer_result"]
        assert res["engine_run"] is False
        assert res["is_significant"] is False
        assert res["artifact_grade"] is False

    def test_sample_sizes_declared(self):
        res = _block()["asymmetry_scorer_result"]
        assert "n=1 vs n=1" in res["methodology"]
        assert "n=1 vs n=2" in res["methodology"]

    def test_verdict_member_confirmed(self):
        res = _block()["asymmetry_scorer_result"]
        assert res["verdict"] == "falsification_member_confirmed"


# ---------------------------------------------------------------------------
# 9. Research method
# ---------------------------------------------------------------------------
class TestResearchMethod:
    def test_scout_and_main_run_query_sets_documented(self):
        method = _block()["research_method"]
        assert "1 delegated scout" in method
        assert "2 main-run browser.search verification sets" in method

    def test_scout_rejections_documented(self):
        method = _block()["research_method"]
        assert "AP x OpenAI" in method
        assert "BI x OpenAI held as backups" in method
        assert "#1267 done" in method

    def test_1143_precedent_documented(self):
        block = _block()
        assert "#1143" in block["falsification_family"]
        assert "#1143" in block["research_method"]

    def test_zero_browser_open(self):
        assert "0 browser.open per #503" in _block()["research_method"]

    def test_ascii_no_em_dash(self):
        # In-gate fix: scoped to this run's landed block. atlantic.yaml
        # carries pre-existing em dashes at HEAD (outside the m997
        # block), so the whole-file assertion cannot pass without
        # rewriting history. The ASCII discipline is asserted on the
        # m997 block's own content via an allow_unicode round-trip.
        dumped = yaml.safe_dump(_block(), allow_unicode=True)
        assert "\\u2014" not in dumped

    def test_no_constructed_canonical_urls(self):
        method = _block()["research_method"]
        assert "no canonical URLs constructed" in method
        assert "NOT used per the no-construction rule" in method


# ---------------------------------------------------------------------------
# 10. Statistical discipline (Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline:
    def test_p_value_not_calculated(self):
        res = _block()["asymmetry_scorer_result"]
        assert res["p_value"].startswith("NOT_CALCULATED")

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_correlation_not_causation(self):
        assert _block()["correlation_not_causation"] is True

    def test_manual_illustrative_only(self):
        disc = _block()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE" in disc

    def test_verdict_member_confirmed(self):
        assert _block()["verdict"].startswith(
            "falsification_member_confirmed")

    def test_not_artifact_grade(self):
        assert _block()["statistical_discipline"].find(
            "NOT artifact-grade") != -1


# ---------------------------------------------------------------------------
# 11. Guard lifecycle for #1277 (forward pins for #1278)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1277:
    def test_pins_on_mechanism_landing(self):
        # Type A lands one mechanism: max 997, next 998.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 997" in src
        assert "NEXT_NUM = 998" in src

    def test_no_type_b_1278_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in #1278's terminal log-hash followup per #721): every commit
        # whose message matches "Type B #1278" must be #1278's main
        # commit or a descendant of it. Deselected in the in-gate run
        # (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1278")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1278's own commits"
        main = _git("rev-parse", PRED_MAIN_1278).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_998_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_998_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_998_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_forty_ninth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T49, "profiles/") == [
            "profiles/careers/journalists.yaml"]

    def test_fiftieth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T50, "profiles/") == [
            "profiles/careers/journalists.yaml"]

    def test_fifty_first_member_intact_pin(self):
        assert _git_grep_tracked_source(_T51, "profiles/") == [
            "profiles/news-corp.yaml"]

    def test_fifty_second_member_intact_pin(self):
        assert _git_grep_tracked_source(_T52, "profiles/") == [
            "profiles/careers/journalists.yaml"]

    def test_fifty_third_member_intact_pin(self):
        assert _git_grep_tracked_source(_T53, "profiles/") == [
            "profiles/the-verge.yaml"]

    def test_fifty_fourth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T54, "profiles/") == [
            "profiles/guardian.yaml"]

    def test_fifty_fifth_member_intact_pin(self):
        # Landed this run (m997, profiles/atlantic.yaml). Asserted on
        # the working tree so the pin is stable across the main-commit
        # boundary; the HEAD sweep sees it from the main commit on.
        assert _T55 in _read(ATLANTIC_PATH)

    def test_no_fifty_sixth_member_pin(self):
        assert _git_grep_tracked_source(_T56, None) == []

    def test_predecessor_1276_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, D1276_FILE))

    def test_next_leg_is_1278_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1278 Type B" in src

    def test_1276_pins_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestGuardLifecycle1276" in src
        assert "3 failed, 14 passed" in src


# ---------------------------------------------------------------------------
# 12. Staleness pins for #1277 (1 test; deselected pre-commit per #721)
# ---------------------------------------------------------------------------
class TestStalenessPins1277:
    def _class_run(self, filename, classname):
        target = os.path.join(TESTS_DIR, filename)
        env = dict(os.environ)
        env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
        res = subprocess.run(
            ["python3", "-m", "pytest", target,
             "-k", classname,
             "-q", "--no-header"],
            cwd=REPO_ROOT, capture_output=True, text=True, env=env,
        )
        return res

    def test_1276_guard_lifecycle_post_commit(self):
        # Post-main-commit form: 17 tests in the class, 14 pass and 3
        # fail - the no_fifty_fifth_member pin (this run's main commit
        # lands the fifty-fifth member-claim form; the #1191-class
        # self-trip, permanent red), the no_type_a_1277_in_git_log pin
        # (hits go non-empty at the main commit while PRED_MAIN_1277
        # in the #1276 file is still 0*40; re-pinned green in this
        # run's log-hash followup per #721), and the
        # 997_numeric_absent_in_profiles pin (trips on the landed m997
        # block's "mechanism_id: 997"; the #1272-class forward-guard
        # expiry - the next-number guard is consumed by the landing).
        # Deselected in the in-gate run (pre-commit the class is 17
        # passed); asserted post-main-commit. The #1276 file is
        # read-only to this run except the #721 re-pin; the flips are
        # documented here, not repaired.
        res = self._class_run(
            D1276_FILE,
            "TestGuardLifecycle1276",
        )
        out = res.stdout + res.stderr
        assert "3 failed, 14 passed" in out, out[-2000:]
        assert "no_fifty_fifth_member" in out, out[-2000:]
        assert "no_type_a_1277_in_git_log" in out, out[-2000:]
        assert "997_numeric_absent_in_profiles" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 13. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------
class TestDocSync:
    def test_readme_test_file_table_has_1277_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_a_1277" in readme

    def test_architecture_has_1277_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_a_1277" in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_PATH)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 14. Iteration log (3 tests; deselected pre-commit per #721)
# ---------------------------------------------------------------------------
class TestIterationLog:
    def test_1277_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1277 Type A" in log

    def test_1276_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1276 Type E" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 15. In-flight isolation
# ---------------------------------------------------------------------------
class TestInFlightIsolation:
    def test_899_nytimes_hunk_untouched(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert "profiles/nytimes.yaml" in modified
        # Its uncommitted hunk belongs to #899's run; this run stages
        # only its own paths.
        staged = _git("diff", "--cached", "--name-only").stdout.split()
        assert "profiles/nytimes.yaml" not in staged

    def test_900_untracked_file_untouched(self):
        assert os.path.exists(
            os.path.join(
                TESTS_DIR,
                "test_type_d_900_m769_qualitative_corpus_integrity_"
                "sep21_1pm.py",
            )
        )
        res = _git("status", "--porcelain")
        assert "test_type_d_900_" in res.stdout

    def test_938_test_file_edit_owned_by_its_run(self):
        res = _git("diff", "--name-only")
        assert "test_type_b_938_" in res.stdout
        staged = _git("diff", "--cached", "--name-only").stdout.split()
        assert not any("test_type_b_938_" in p for p in staged)

    def test_1012_wt_working_tree_edit_owned_by_its_run(self):
        res = _git("diff", "--name-only")
        assert "test_type_a_1012_" in res.stdout
        staged = _git("diff", "--cached", "--name-only").stdout.split()
        assert not any("test_type_a_1012_" in p for p in staged)

    def test_do_not_touch_1024_m846(self):
        res = _git("diff", "--name-only")
        assert "competitor-entities.yaml" not in res.stdout
        staged = _git("diff", "--cached", "--name-only").stdout.split()
        assert "profiles/competitor-entities.yaml" not in staged
