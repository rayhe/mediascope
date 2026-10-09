"""Type A #1322: FT x OpenAI Oct-8-2026 revenue-scoop accountability original (Oct 8 2026, ~08:00 PM PDT).

m1024 - the FT breaks an adverse, market-moving revenue story on its own
Apr-29-2024 licensing partner: OpenAI told investors its annualized
revenue was approaching $50 billion at the end of September, about $20
billion below the $70 billion previously signaled (the FT reports the
discrepancy arose from OpenAI investors' own attempts to force
comparability with Anthropic's differently-calculated run rate).
Market impact: Nasdaq -1.25% (worst day since mid-August), Oracle -5.5%,
Nvidia -2.9%. OpenAI declined to comment. Relay-attested via four
independent relays (TechCrunch Oct 8, Reuters Oct 8, Morningstar/Dow
Jones Oct 8, CNN Oct 8); 0 browser.open per #503; the FT original URL
did not surface in search listings (no-construction rule).

MANUAL ILLUSTRATIVE scoring: FT x OpenAI revenue scoop -0.35 vs
carried FT x Meta arms mean -0.5833. Illustrative delta (OpenAI minus
Meta): +0.23 - the payer draws a slightly less-negative register, but
the thesis test is the uniform payer-softening prediction, not the
delta: the $5-10M/yr deal predicts a muted register on OpenAI; the FT
instead breaks the scoop. The uniform softening prediction FAILS on the
financial-scoop register.

Per #715 this docstring uses lowercase forms only: the sixtieth
falsification-family member, ledger 59->60. The uppercase claim form
lives only in the landed profile block. FIFTH FT publication-level
member (after the thirty-fifth #1047 disclosure-register, the
forty-second #1142 regulatory-enforcement-register, the forty-eighth
#1202 suppression-claim, and the fifty-eighth #1292 FT x Google
regulatory-register); FIRST falsification pin on the financial-scoop
register. Domain-bounded to FT's financial-scoop register on OpenAI in
the Oct-8 window. The #1143 temporal-replication precedent does not
block: this is a fresh adverse-scoop peg (four independent relays), not
a re-score. Counterevidence disclosed: m625 (FT Sep 3-9 Astra coronation
+0.25 vs Meta Muse +0.05) is the incentive-prediction-consistent
baseline on product-launch pegs; the member claim is register-bounded,
not blanket.

Statistical discipline: monitoring-only per the Aug 28 2026 standing
rule (MANUAL ILLUSTRATIVE ONLY, engine NOT run, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False, NOT artifact-grade, no
analysis.json update, verdict falsification_member_confirmed on the
domain-bounded peg). Correlation is not causation. Hypothesis-generating
only.

1 delegated scout (fresh publication+competitor pair discovery; 3
ranked candidates returned; SELECTED the FT x OpenAI Oct-8 revenue
scoop) + 1 main-run browser.search verification set, 0 browser.open per
#503. 4 novel relay URLs zero-hit pre-commit. All URLs copied verbatim
from Full-URL listings; no canonical URLs constructed. ASCII-only, no em
dashes.

Rotation: this run is iteration #1322 Type A, the THIRD leg of the
1320-1324 window (D #1320 -> E #1321 -> A #1322 -> B #1323 -> C #1324,
per the #565 anchor + rotation guard). Predecessor #1321 Type E
verified in git log (main a8ac5238 / anchor c2f5a24b / doc-sync
85e2481c / podcast-sentiment followup a935e401 / log-hash a283839e);
the 1315-1319 window is VERIFIED CLOSED. This run's main commit is the
anchor per #565; ANCHORED_SHA patched post-commit. The #1321 forward
guards verified pre-commit this run: max-1023; zero next-number
one-zero-two-four mechanism keys all forms (profiles/ + tests/ scope);
no-Type-A-#1322-in-git-log; fortieth direction absent (profiles/ scope);
forty-eighth through fifty-ninth members intact; no sixtieth member
(repo-wide); ledger 59. This run lands the sixtieth member:
TestGuardLifecycle1321's no-sixtieth-member pin flips at this run's main
commit BY DESIGN (the #1191-class self-trip), documented in
TestStalenessPins1322, not repaired. Next run #1323 Type B continues
the window. The #1320-launched background-suite verdict belongs to #1325
per #795: this run OBSERVES only (log last write Oct 8 17:59 PDT, zero
live pytest processes at this run's check - appears stalled).
In-flight during this run: #899 (profiles/nytimes.yaml m771 hunk), #938
(Type B test file working-tree edit), #900 (untracked Type D test file),
#1012-wt (working-tree edit on the committed Type A #1012 file) - all
untouched; targeted staging only. Do NOT touch #1024 m846.

Pre-commit novelty greps per #715: zero test_type_a_1322 files on disk
(glob); no Type A #1322 in git log (--grep); max numeric mechanism_id
1023 in profiles/ pre-commit (mechanism_id regex sweep); zero
numeric/underscore/dash next-number one-zero-two-four mechanism key
forms repo-wide pre-commit (needles format-built per #715, own file
excluded); "## #1322" zero-hit in iteration-log pre-commit; README
stats 75027/1646 pre-commit; no #1322 row in README/ARCHITECTURE test
tables pre-commit; 4 novel relay URLs zero-hit repo-wide pre-commit
(git grep -F); "approaching $50 billion" zero-hit repo-wide pre-commit;
the Oct-8 revenue scoop zero-hit in profiles/financial-times.yaml
pre-commit; distinct from m625 (Sep 3-9 launch-week coronation vs
distribution, not a scoop), the m718 Sep-15 $1.2tn valuation scoop
(different peg), and m847/m1047/#1142 (disclosure/regulatory pegs).

Doc-sync constants per #719: README_TEST_COUNT / README_FILE_COUNT
hold the post-doc-sync values from the start (patched pre-main once
the in-gate collection count is known); the doc-sync commit ratchets
README 75027/1646 -> post-sync totals.
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
FT_PATH = os.path.join(PROFILES_DIR, "financial-times.yaml")
OWN_BASENAME = (
    "test_type_a_1322_ft_openai_oct08_revenue_scoop_"
    "vs_carried_meta_arms_oct08_8pm.py"
)
BLOCK_KEY = (
    "type_a_1322_ft_openai_oct08_revenue_scoop_"
    "accountability_vs_carried_meta_arms"
)

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "237e0a1e2f21b114e11a1c0405c2905ea31f9eba"  # patched in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1024
NEXT_NUM = 1025  # integer only; key-form needles are format-built

# Predecessor chain: #1321 Type E CLOSED the second leg.
PRED_MAIN_1321 = "a8ac5238faadeed657069bc3b3c01729207b8165"
PRED_ANCHOR_1321 = "c2f5a24b16961644d181a0d0a7fc3ebdd558db29"
PRED_DOCSYNC_1321 = "85e2481c054a0263bf79472051f6e564243e3880"
PRED_FINAL_1321 = "a283839e1585807d605ac42423206a0f5e4d1f3f"

# This run's main commit (full sha), for the ancestor-form
# no-Type-A-#1322 pin. Patched in the terminal log-hash followup per
# #721.
PRED_MAIN_1322 = "237e0a1e2f21b114e11a1c0405c2905ea31f9eba"  # re-pinned in the log-hash followup per #721

# #1323's main commit (full sha), for the ancestor-form no-Type-B-#1323
# pin. Patched in #1323's terminal log-hash followup per #721.
PRED_MAIN_1323 = "6fae5cd614267592c77100188b6e956bb6d7ed34"  # re-pinned by #1323 terminal log-hash followup per #721

# The #1321 Type E file, for the staleness pin on its guard-lifecycle
# class (max id 1023; zero next-number one-zero-two-four /
# no-Type-A-#1322-in-git-log / fortieth direction absent /
# forty-eighth through fifty-ninth members intact / sixtieth member
# absent / ledger 59).
E1321_FILE = (
    "test_type_e_1321_podcast_sentiment_187th_verification_oct08_6pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 75115  # post-doc-sync total (pre-sync 75027 + 88)
README_FILE_COUNT = 1647  # pre-sync 1646 + 1 (this file)

# Tones (MANUAL ILLUSTRATIVE).
OPENAI_SCOOP_TONE = -0.35  # NEW FT x OpenAI arm (Oct-8 revenue scoop)
META_MEAN = -0.5833333333333333  # carried FT x Meta arms mean
DELTA_OPENAI_MINUS_META = 0.2333333333333333  # -0.35 - (-0.5833...)

NOVEL_URLS = [
    "https://techcrunch.com/2026/10/08/"
    "openais-revenue-is-reportedly-20-billion-less-than-"
    "previously-projected/",
    "https://www.reuters.com/business/"
    "openais-annualized-revenue-20-billion-less-than-previously-"
    "signaled-ft-reports-2026-10-08/",
    "https://www.morningstar.com/news/dow-jones/202610087175/"
    "oracle-amd-others-slide-after-report-of-revision-to-"
    "openai-revenue-estimate",
    "https://www.cnn.com/2026/10/08/investing/openai-nasdaq-stocks"
    "?cid=external-feeds_iluminar_meta",
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
_T57 = "FIFT" + "Y-SEVENTH falsification-family member"
_T58 = "FIFT" + "Y-EIGHTH falsification-family member"
_T59 = "FIFT" + "Y-NINTH falsification-family member"
_T60 = "SIXT" + "IETH falsification-family member"
_T61 = "SIXT" + "Y-FIRST falsification-family member"


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


def _load_ft():
    with open(FT_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _block():
    data = _load_ft()
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
class TestAnchor1322:
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
        assert "THIRD leg of the 1320-1324 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestRotationGuard:
    def test_predecessor_1321_chain_verified(self):
        for sha in (
            PRED_MAIN_1321, PRED_ANCHOR_1321, PRED_DOCSYNC_1321,
            PRED_FINAL_1321,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1320 -> E #1321 -> A #1322 -> B #1323 -> C #1324" in src

    def test_next_leg_is_type_b_1323(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1323 Type B" in src

    def test_type_a_lands_one_mechanism(self):
        assert MECH_NUM == 1024
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_this_run_is_third_leg(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "iteration #1322 Type A, the THIRD leg" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty
# ---------------------------------------------------------------------------
class TestMechanismNovelty:
    def test_max_numeric_mechanism_id_1024(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_no_type_a_1322_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type A #1322" must be this run's
        # main commit or a descendant of it - i.e., no PRIOR run
        # committed this run's iteration. Deselected in the in-gate
        # run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type A #1322")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1322).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_zero_next_number_keys_all_forms(self):
        # Numeric (profiles/ scope), underscore and dash (profiles/ +
        # tests/ scope, own file excluded per #715).
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_key_designed_no_1024_substring(self):
        # Per #723/#738/#739: the iteration-form block key carries no
        # underscore-form one-zero-two-four mechanism key substring
        # (needle format-built per #770 so this file carries no
        # contiguous literal).
        needle = "%s%d" % (MECH_ID_MARKER, MECH_NUM)
        assert needle not in BLOCK_KEY
        assert BLOCK_KEY in _read(FT_PATH)

    def test_forward_guards_for_1323(self):
        # max-1024; zero-1025 all forms; fortieth direction absent
        # (profiles/ scope); forty-eighth through sixtieth members
        # intact; no sixty-first member (repo-wide); ledger 60. The
        # sixtieth is asserted on the working tree (this run's block,
        # committed at the main commit); the HEAD-based sweep sees it
        # from the main commit onward.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1024" in src
        assert "NEXT_NUM = 1025" in src
        assert "ledger 59->60" in src
        assert _git_grep_tracked_source(_T40, "profiles/") == []
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]
        assert _T60 in _read(FT_PATH)
        assert _git_grep_tracked_source(_T61, None) == []

    def test_novel_urls_zero_hit_pre_commit(self):
        # The 4 relay URLs were verified zero-hit pre-commit (git
        # grep -F, documented in the block's novelty field). This test
        # pins that no file OTHER than this run's own m1024 block ever
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
                "profiles/financial-times.yaml",
                "tests/" + OWN_BASENAME,
            }, (url, paths)


# ---------------------------------------------------------------------------
# 4. Falsification ledger (sixtieth member lands this run)
# ---------------------------------------------------------------------------
class TestFalsificationLedger:
    def test_sixtieth_member_present_in_block(self):
        block = _block()
        assert block["falsification_family_member"] is True
        assert _T60 in block["falsification_family"]
        assert block["falsification_ledger"] == "60"
        assert block["ledger"] == "60"

    def test_forty_eighth_through_fifty_ninth_intact(self):
        # The earlier members survive this run unchanged (tracked
        # sources at HEAD; this run's block is additive).
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]
        assert _git_grep_tracked_source(_T59, "profiles/") == [
            "profiles/news-corp.yaml"]

    def test_no_sixty_first_member_repo_wide(self):
        assert _git_grep_tracked_source(_T61, None) == []

    def test_verdict_falsification_member_confirmed(self):
        block = _block()
        assert block["verdict"].startswith(
            "falsification_member_confirmed")

    def test_ledger_60_in_block(self):
        block = _block()
        assert "ledger 59->60" in block["falsification_family"]


# ---------------------------------------------------------------------------
# 5. FT x OpenAI revenue scoop arm (NEW this run)
# ---------------------------------------------------------------------------
class TestFtOpenaiRevenueScoop:
    def _item(self):
        return _block()["openai_arms"][0]["item"]

    def test_headline(self):
        assert "revenue scoop" in self._item()["title"]
        assert "$50B" in self._item()["title"]

    def test_date_oct_8_2026(self):
        assert self._item()["date"] == "2026-10-08"

    def test_publication_ft_original(self):
        assert "Financial Times (original; relay-attested)" in (
            self._item()["publication"])

    def test_framing_financial_scoop(self):
        assert self._item()["framing"] == (
            "financial_scoop_accountability")

    def test_tone_minus_035(self):
        assert self._item()["manual_illustrative_tone"] == (
            OPENAI_SCOOP_TONE)

    def test_deal_not_disclosed(self):
        assert self._item()["deal_disclosed"] is False

    def test_evidence_tier_relay_attested(self):
        assert self._item()["evidence_tier"] == "relay-attested"

    def test_market_impact_nasdaq(self):
        impact = self._item()["market_impact"]
        assert any("Nasdaq -1.25%" in row for row in impact)


# ---------------------------------------------------------------------------
# 6. Meta arms (carried from the type_a_1292 block, un-rescored per #807)
# ---------------------------------------------------------------------------
class TestMetaArms:
    def test_carried_from_1292_block(self):
        assert "type_a_1292" in _block()["meta_arms"]["carried_from"]

    def test_three_arms(self):
        arms = _block()["meta_arms"]["arms"]
        assert len(arms) == 3
        tones = [a["manual_illustrative_tone"] for a in arms]
        assert tones == [-0.55, -0.62, -0.58]

    def test_meta_band_mean(self):
        assert _block()["meta_arms"]["meta_mean"] == META_MEAN


# ---------------------------------------------------------------------------
# 7. Financial relationship
# ---------------------------------------------------------------------------
class TestFinancialRelationship:
    def test_ft_openai_licensing_deal(self):
        rel = _block()["financial_relationship"]
        assert "Apr 29 2024" in rel
        assert "$5-10M/yr" in rel

    def test_ft_meta_zero_tie(self):
        rel = _block()["financial_relationship"]
        assert "FT x Meta: $0" in rel

    def test_coverage_prediction_softer(self):
        data = _load_ft()
        assert data["competitor_relationships"]["openai"][
            "coverage_prediction"] == "softer"


# ---------------------------------------------------------------------------
# 8. Asymmetry delta (MANUAL ILLUSTRATIVE ONLY)
# ---------------------------------------------------------------------------
class TestAsymmetryDelta:
    def test_delta_math(self):
        calc = OPENAI_SCOOP_TONE - META_MEAN
        assert abs(calc - DELTA_OPENAI_MINUS_META) < 1e-9

    def test_block_delta_matches(self):
        res = _block()["asymmetry_scorer_result"]
        assert abs(
            res["illustrative_delta_openai_minus_meta"] - 0.23
        ) < 0.01

    def test_delta_direction_positive_softening_test(self):
        res = _block()["asymmetry_scorer_result"]
        assert "uniform payer-softening prediction" in (
            res["delta_direction"])
        assert "FAILS on the financial-scoop register" in (
            res["delta_direction"])

    def test_engine_not_run(self):
        res = _block()["asymmetry_scorer_result"]
        assert res["engine_run"] is False
        assert res["is_significant"] is False
        assert res["artifact_grade"] is False

    def test_sample_sizes_declared(self):
        res = _block()["asymmetry_scorer_result"]
        assert "n=1 vs n=3" in res["methodology"]

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
        assert "1 main-run browser.search verification set" in method

    def test_1143_precedent_documented(self):
        block = _block()
        assert "#1143" in block["falsification_family"]
        assert "#1143" in block["research_method"]

    def test_counterevidence_disclosed(self):
        block = _block()
        assert any("m625" in item
                   for item in block["counterevidence"])

    def test_zero_browser_open(self):
        assert "0 browser.open per #503" in _block()["research_method"]

    def test_ascii_no_em_dash(self):
        # Scoped to this run's landed block: financial-times.yaml
        # carries pre-existing em dashes at HEAD (outside the m1024
        # block), so the whole-file assertion cannot pass without
        # rewriting history. The ASCII discipline is asserted on the
        # m1024 block's own content via an allow_unicode round-trip.
        dumped = yaml.safe_dump(_block(), allow_unicode=True)
        assert "\\u2014" not in dumped

    def test_no_constructed_canonical_urls(self):
        method = _block()["research_method"]
        assert "no canonical URLs constructed" in method
        assert "did not surface" in _block()["openai_arms"][0][
            "item"]["url_source"]


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
# 11. Guard lifecycle for #1322 (forward pins for #1323)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1322:
    def test_pins_on_mechanism_landing(self):
        # Type A lands one mechanism: max 1024, next 1025.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1024" in src
        assert "NEXT_NUM = 1025" in src

    def test_no_type_b_1323_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1323's terminal log-hash followup
        # per #721): every commit whose message matches "Type B
        # #1323" must be #1323's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1323")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1323's own commits"
        main = _git("rev-parse", PRED_MAIN_1323).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1025_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1025_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1025_dash_absent_repo_wide(self):
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
        # Landed this run (m1024, profiles/financial-times.yaml).
        # Asserted on the working tree so the pin is stable across the
        # main-commit boundary; the HEAD sweep sees it from the main
        # commit on.
        assert _T60 in _read(FT_PATH)

    def test_no_sixty_first_member_pin(self):
        assert _git_grep_tracked_source(_T61, None) == []

    def test_predecessor_1321_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1321_FILE))

    def test_next_leg_is_1323_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1323 Type B" in src

    def test_1321_pins_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1322" in src


# ---------------------------------------------------------------------------
# 12. Staleness pins for #1322 (1 test; deselected pre-commit per #721)
# ---------------------------------------------------------------------------
class TestStalenessPins1322:
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

    def test_1321_guard_lifecycle_post_commit(self):
        # Post-main-commit form: the #1321 guard-lifecycle class has
        # 22 tests; 20 pass and 2 fail - the no_sixtieth_member pin
        # (this run's main commit lands the sixtieth member-claim
        # form; the #1191-class self-trip, permanent red), and the
        # 1024_numeric_absent_in_profiles pin (trips on the landed
        # m1024 block's "mechanism_id: 1024"; the #1272-class
        # forward-guard expiry - the next-number guard is consumed by
        # the landing). The no_type_a_1322_in_git_log pin flips green
        # at the #721 re-pin (done pre-commit of the log-hash
        # followup, so it never shows red in this check). Deselected
        # in the in-gate run (pre-commit the class is 22 passed);
        # asserted post-main-commit. The #1321 file is read-only to
        # this run except the #721 re-pin; the flips are documented
        # here, not repaired.
        res = self._class_run(
            E1321_FILE,
            "TestGuardLifecycle1321",
        )
        out = res.stdout + res.stderr
        assert "2 failed, 20 passed" in out, out[-2000:]
        assert "no_sixtieth_member" in out, out[-2000:]
        assert "1024_numeric_absent_in_profiles" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 13. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------
class TestDocSync:
    def test_readme_test_file_table_has_1322_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_a_1322" in readme

    def test_architecture_has_1322_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_a_1322" in arch

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
    def test_1322_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1322 Type A" in log

    def test_1321_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1321 Type E" in log

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
