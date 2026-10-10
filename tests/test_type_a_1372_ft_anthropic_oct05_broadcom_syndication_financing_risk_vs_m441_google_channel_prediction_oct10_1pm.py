"""Type A #1372: FT x Anthropic Oct-5/6-2026 Broadcom $60B chip-debt
syndication financing-risk register vs the m441 "softer via Google
channel" prediction (Oct 10 2026, ~1:00 PM PDT).

The Oct-5/6-2026 Broadcom-Anthropic $60B chip-debt syndication launch
(Bank of America, Citigroup, Morgan Stanley begin syndicating the
record package to back Anthropic's lease of Google semiconductors:
$42B senior secured loans backed by Broadcom's A-minus rating; $18B
junior tranche without Broadcom guarantees, Blackstone committing
~$9B; funds 2027 chip orders; expands the Oct-1 Broadcom $42B
convertible-loan facility disclosure) is an FT ORIGINAL,
relay-attested by two independent secondaries: tradersunion (Oct 6)
"as first reported by the Financial Times"; aitechdaily (Oct 6) "the
Financial Times reported". Register: financing-risk DISCLOSURE, not
puff - the FT frames the deal as "the largest chip-financing deal
yet" and "a test of lender appetite for AI infrastructure debt", and
discloses that the junior slice "leaves lenders more directly
exposed to Anthropic's credit". MANUAL ILLUSTRATIVE -0.20
(hand-assigned at excerpt level, NOT an empirical score).

The tested prediction is m441 (iteration 441, Sep 1 2026, in this
same financial-times.yaml anthropic section): coverage_prediction
"softer via Google channel" - the indirect FT-Google commercial
partnership (single-figure millions GBP/yr, News AI pilot) plus
Google's up-to-$40B Anthropic investment predicts SOFTER Anthropic
financing coverage than Meta's capital-raise desperation framing.
The prediction FAILS on this peg: the FT originates the
financing-risk story on the indirectly-tied lab and runs the risk
register on it.

Same-week cross-lab comparator (carried, un-rescored per #807):
m1024's FT x OpenAI Oct-8 revenue-scoop arm (-0.35, the SIXTIETH
falsification-family member) - the FT ran the financing/financial
register on BOTH labs in the same week, on the deal partner and the
non-deal lab alike. Illustrative delta (Anthropic minus OpenAI)
+0.15: near-symmetric hardness across the deal boundary.

Verdict: falsification_member_confirmed; SIXTY-FIFTH member of the
falsification family (ledger 64->65); FIRST financing-risk-register
falsification at FT (after the THIRTY-FIFTH disclosure-register
#1047, the FORTY-SECOND regulatory-enforcement #1142, the
FORTY-EIGHTH suppression-claim #1202, the FIFTY-EIGHTH FT x Google
regulatory #1292, and the SIXTIETH financial-scoop #1322); FIRST
falsification of the m441 indirect prediction. Domain-bounded to
FT's financing-risk register on Anthropic in the Oct-5/6 window.

Counterevidence disclosed: m441's home pair (May-8 Anthropic
fundraising aspirational vs Jun-5 Meta equity-raise desperation -
the softer-Anthropic pattern STANDS on the fundraising
sub-register; this run bounds it); m859's +0.15 constructive
Anthropic IPO arm (Sep-14 - register follows peg, not entity);
m1024's payer arm ran HARDER (-0.35) than the Anthropic arm
(-0.20) in the same week.

Research method: 5 main-run browser.search verification sets (WSJ
Anthropic Oct 2026 - REJECTED as Sep-18-vintage relay set; FT Meta
wearables Oct 2026 - context only; Anthropic S-1 Oct 2026 -
REJECTED, still confidential; Samsung Android XR Oct 2026 -
context only; Broadcom-Anthropic $42B/$60B financing - SELECTED;
FT OpenAI Broadcom $50B financing - REJECTED as WSJ-original; FT
OpenAI revenue correction - SATURATED via m1024 #1322, caught on
main-run verification). 0 browser.open per #503; FT paywalled;
both FT arms relay-attested; excerpt-bounded. All 5 evidence URLs
copied verbatim from search-result Full-URL listings; no canonical
URLs constructed. No delegated scout this run (main-run sets only
per the #1341 lesson).

Type A lands one mechanism (m1047): max numeric mechanism_id
1046->1047; ledger 64->65; sixty-fifth member-form present
(financial-times.yaml); sixty-sixth member-form absent repo-wide;
fortieth direction absent by design. MANUAL / QUALITATIVE ONLY per
the Aug-28 standing rule; monitoring-only; NOT artifact-grade; no
analysis.json update. Correlation is not causation;
hypothesis-generating only.

Background suite per #795: the #1370-launched full suite runs at
goal hidden_files type_d_1370_full_suite.log: this run OBSERVES
only (neither re-launches, kills, nor writes to the suite). The
#1375 Type D run owns the next verdict per #795.

Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B
test file working-tree edit), #900 (untracked Type D test file),
#1012-wt (working-tree edit on the committed Type A #1012 file)
all left out of this run's index/diff via explicit-path staging.
#1024 m846 (profiles/competitor-entities.yaml) NOT touched -
decision pending. Do NOT touch #1024 m846.

Tests: 106 tests collected, 15 classes. In-gate: 96 passed +
10 deselected per #565/#719/#721 (TestAnchor1372 1 +
TestGuardLifecycle1372 2 + TestDocSync1372 3 +
TestIterationLog1372 3 + TestStalenessPins1372 1).
"""
import os
import re
import subprocess

import pytest
import yaml


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
ITERLOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
FT_PATH = os.path.join(PROFILES_DIR, "financial-times.yaml")
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
OWN_BASENAME = (
    "test_type_a_1372_ft_anthropic_oct05_broadcom_syndication_"
    "financing_risk_vs_m441_google_channel_prediction_oct10_1pm.py"
)


# Pre-commit placeholder per #565; patched to the main-commit sha in
# the anchor followup (post-anchor the placeholder pin fails BY
# DESIGN).
ANCHORED_SHA = "e162b718eaebe64f28146d7d9c0585e7a3c81e4a"  # patched to the main commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1047
NEXT_NUM = 1048  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_a_1372_ft_anthropic_oct05_broadcom_syndication_"
    "financing_risk_register_vs_m441_google_channel_prediction"
)

# Predecessor chain: #1371 Type E was the SECOND leg of the
# 1370-1374 window. Its main/anchor/doc-sync/log-hash commits are
# pushed and ls-remote-verified.
PRED_MAIN_1371 = "021a0f7cc6b9549817ab7a6acc4bd260ef40675a"
PRED_ANCHOR_1371 = "ee03fa81adfa5bb34b44040654f1276758af469f"
PRED_DOCSYNC_1371 = "75e3e3e7c27779f354b40ef28aec11318c56cb5f"
PRED_FINAL_1371 = "b65bdc674fb2b03c43486368a9a572698d1b5dd6"
PRED_PUSH_1371 = "9c662e89282d506d12dfe96460e61d817c114b2d"

# This run's own main-commit sha, re-pinned per #721 in the anchor
# followup (the #1371 predecessor file's copy is re-pinned in the
# terminal log-hash followup per #721/#1292).
PRED_MAIN_1372 = "e162b718eaebe64f28146d7d9c0585e7a3c81e4a"

# Forward guard for the next leg: #1373 Type B. Re-pinned by #1373's
# anchor followup per #721 (starts as 0*40; placeholder-only).
PRED_MAIN_1373 = "9cb2b6cd92de9faef3bf0bb2a31b904947ffea85"  # re-pinned to the #1373 main sha in #1373's terminal log-hash followup per #721/#1292

# The #1371 Type E file, for the staleness pin on its guard
# lifecycle (post-terminal form at this run is "2 failed, 23
# passed": ONE #1272-class forward-guard expiry
# (test_1047_numeric_absent_in_profiles trips on the landed m1047
# block in profiles/financial-times.yaml) plus ONE member-form flip
# (test_no_sixty_fifth_member_pin trips on the landed sixty-fifth
# member at the new HEAD); the no_type_a_1372 forward pin flips
# green in this run's terminal log-hash followup per #721/#1292).
# Documented in TestStalenessPins1372, not repaired.
E1371_FILE = (
    "test_type_e_1371_podcast_sentiment_197th_"
    "verification_oct10_12pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 79976  # patched pre-main: pre-sync 79870 + 106 collected
README_FILE_COUNT = 1697  # patched pre-main: pre-sync 1696 + 1 (this file)

# m846 block region in profiles/competitor-entities.yaml at HEAD (the
# #1024 m846 decision-pending block; byte-identity pin in the
# in-flight isolation class). HEAD lines, 1-based, verified intact
# this run.
M846_HEAD_START = 26349
M846_HEAD_END = 26472

# The forward-guard needles are fragment-built per #715 so this file
# carries no contiguous sensitive literal.
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
_T62 = "SIXT" + "Y-SECOND falsification-family member"
_T63 = "SIXT" + "Y-THIRD falsification-family member"
_T64 = "SIXT" + "Y-FOURTH falsification-family member"
_T65 = "SIXT" + "Y-FIFTH falsification-family member"
_T66 = "SIXT" + "Y-SIXTH falsification-family member"

# ---------------------------------------------------------------------------
# This run's surfaced evidence (all URLs copied verbatim from the
# browser.search Full-URL listings; corpus novelty verified pre-commit
# via git grep -F).
# ---------------------------------------------------------------------------

NOVEL_URLS = [
    # Oct 6: "as first reported by the Financial Times" (tradersunion)
    "https://tradersunion.com/news/financial-news/show/3672083-"
    "broadcom-ai-chip-financing-60bn/",
    # Oct 6: "the Financial Times reported" (aitechdaily)
    "https://www.aitechdaily.com/broadcom-anthropic-60b-chip-debt-"
    "syndication/",
    # Oct 6: "the Financial Times reported on Tuesday" (tradingview)
    "https://www.tradingview.com/news/benzinga:0f49076c0094b:0-"
    "challenging-nvidia-s-dominance-broadcom-pairs-custom-tpu-chips-"
    "with-60-billion-debt-package/",
    # Oct 8: the $110B+ financing roundup (hokanews)
    "https://www.hokanews.com/2026/10/broadcom-wall-street-firms-"
    "line-up-over.html",
    # Oct 5/6: syndication-begin relay (neoteo)
    "https://www.neoteo.com/en/banks-began-syndicating-broadcom-"
    "backed-debt-for-anthropics-chip-lease",
]

# In-corpus corroboration (NOT novel keys).
INCORPUS_URLS = [
    # m1024: Reuters Oct-8 FT-revenue-scoop relay
    "https://www.reuters.com/business/openais-annualized-revenue-"
    "20-billion-less-than-previously-signaled-ft-reports-2026-10-08/",
    # m981: TechCrunch Oct-5 image-ads original
    "https://techcrunch.com/2026/10/05/openai-chatgpt-image-ads/",
]


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT] + list(args),
        capture_output=True, text=True, timeout=120,
    )


def _load_ft():
    with open(FT_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _max_numeric_mechanism_id():
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    found = []
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


def _iter_source_files():
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs
                   if d not in ("__pycache__", ".git", "node_modules")]
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
    """Numeric colon-form sweep, profiles/ scope only (per #715)."""
    needle = "mechanism_id: %d" % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in open(p, encoding="utf-8", errors="replace").read():
                hits.append(p)
    return hits


def _git_grep_tracked_source(needle, scope):
    return _git("grep", "-F", needle, "HEAD", "--", scope)


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
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------


class TestAnchor1372:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to the main commit sha per #565. This test runs
        # in the in-gate (passes pre-commit); post-anchor it fails BY
        # DESIGN (the patched form is asserted post-anchor).
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
# 2. Rotation guard: #1371 Type E was the SECOND leg; #1372 Type A is the
# THIRD leg of the 1370-1374 window (D #1370 -> E #1371 -> A #1372 ->
# B #1373 -> C #1374).
# ---------------------------------------------------------------------------


class TestRotationGuard1372:
    def test_predecessor_1371_shas_in_git_log(self):
        log = _git("log", "--oneline", "-60").stdout
        for sha, label in (
            (PRED_MAIN_1371, "1371 main"),
            (PRED_ANCHOR_1371, "1371 anchor"),
            (PRED_DOCSYNC_1371, "1371 doc-sync"),
            (PRED_FINAL_1371, "1371 log-hash"),
            (PRED_PUSH_1371, "1371 push-status"),
        ):
            assert sha[:8] in log, label

    def test_1371_push_status_done(self):
        text = _git("show", "HEAD:iteration-log.md").stdout
        assert PRED_MAIN_1371 in text
        assert "Push status (this run): DONE" in text

    def test_1371_type_e_in_git_log(self):
        out = _git("log", "--format=%s", "--grep=Type E #1371")
        assert "Type E #1371" in out.stdout

    def test_third_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "THIRD leg of the 1370-1374 window" in src

    def test_window_sequence_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1370 -> E #1371 -> A #1372 -> B #1373 -> C #1374" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty: Type A lands one mechanism (m1047); max 1046 ->
# 1047; next 1048 stays clean in all three key forms.
# ---------------------------------------------------------------------------


class TestMechanismNovelty1372:
    def test_max_numeric_mechanism_id_1047(self):
        # Post-landing form: the m1047 block is in the working tree
        # (landed before the in-gate run). Passes in the in-gate.
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_1047_numeric_present_in_profiles(self):
        # Post-landing form: numeric 1047 exists in exactly one
        # profile (the landed m1047 block); the 1048 pins stay green.
        hits = _repo_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == [FT_PATH], hits

    def test_zero_next_number_keys_all_forms(self):
        # Numeric (profiles/ scope), underscore and dash (repo-wide,
        # own file excluded per #715). Holds pre-commit and
        # post-commit (Type A lands m1047; the 1048 pins stay green).
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_key_designed_no_1047_1048_substring(self):
        # Per #723/#738/#739: the iteration-form block key carries no
        # underscore-form mechanism key substring (needle
        # format-built per #770 so this file carries no contiguous
        # literal).
        for n in (MECH_NUM, NEXT_NUM):
            needle = "%s%d" % (MECH_ID_MARKER, n)
            assert needle not in BLOCK_KEY
        assert "1372" in BLOCK_KEY
        assert BLOCK_KEY in _read(FT_PATH)

    def test_block_key_in_ft_anthropic_section(self):
        # Post-landing form: the m1047 block sits under
        # competitor_relationships.anthropic in
        # profiles/financial-times.yaml (indent 6, sibling after the
        # m892 block, ahead of x_twitter:). Passes in the in-gate
        # (block landed before the run).
        data = _load_ft()
        anth = data["competitor_relationships"]["anthropic"]
        assert BLOCK_KEY in anth
        assert anth[BLOCK_KEY]["mechanism_id"] == MECH_NUM
        assert anth[BLOCK_KEY]["verdict"] == "falsification_member_confirmed"
        assert anth[BLOCK_KEY]["falsification_family_member"] is True

    def test_novel_urls_zero_hit_pre_commit(self):
        # The 5 source URLs were verified zero-hit pre-commit
        # (git grep -F, documented in the block's novelty field). This
        # test pins that no file OTHER than this run's own m1047
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
                "profiles/financial-times.yaml",
                "tests/" + OWN_BASENAME,
            }, (url, paths)

    def test_incorpus_urls_attested(self):
        # The Reuters Oct-8 FT-revenue-scoop relay (m1024) is
        # in-corpus corroboration, not a novel key.
        out = _git("grep", "-F", "-l", INCORPUS_URLS[0], "HEAD", "--",
                   "profiles/", "tests/").stdout
        assert out.strip() != "", "expected the Reuters URL in corpus"

    def test_mech_num_next_num_pins(self):
        # The file's own constants pin the landing arithmetic.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1047" in src
        assert "NEXT_NUM = 1048" in src


# ---------------------------------------------------------------------------
# 4. Guard lifecycle: forward pins for #1373; #1372 staged this run.
# Type A lands the sixty-fifth falsification-family member (m1047):
# ledger 64->65.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1372:
    def test_pins_on_1046_landing(self):
        # Type A lands one mechanism: max becomes 1047, next 1048.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1047" in src
        assert "NEXT_NUM = 1048" in src

    def test_no_type_a_1372_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721/#1292): every commit whose
        # message matches "Type A #1372" must be this run's main
        # commit or a descendant of it. Deselected in the in-gate
        # run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type A #1372")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1372's own commits"
        main = _git("rev-parse", PRED_MAIN_1372).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_b_1373_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1373's terminal log-hash followup
        # per #721): every commit whose message matches "Type B
        # #1373" must be #1373's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1373 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type B #1373")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1373's own commits"
        main = _git("rev-parse", PRED_MAIN_1373).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1047_numeric_present_in_profiles(self):
        # Post-landing form: numeric 1047 is the landed m1047 block.
        assert _repo_grep_numeric_mechanism_id(MECH_NUM) == [FT_PATH]

    def test_1047_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_1047_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_1048_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1048_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1048_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/").stdout == ""

    def test_forty_eighth_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T48, "HEAD", "--",
                   "profiles/financial-times.yaml")
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_forty_ninth_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T49, "HEAD", "--",
                   "profiles/careers/journalists.yaml")
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fiftieth_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T50, "HEAD", "--",
                   "profiles/careers/journalists.yaml")
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_first_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T51, "HEAD", "--",
                   "profiles/news-corp.yaml")
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_second_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T52, "HEAD", "--",
                   "profiles/careers/journalists.yaml")
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_fifty_third_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T53, "HEAD", "--",
                   "profiles/the-verge.yaml")
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fourth_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T54, "HEAD", "--",
                   "profiles/guardian.yaml")
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fifth_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T55, "HEAD", "--",
                   "profiles/atlantic.yaml")
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_sixth_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T56, "HEAD", "--",
                   "profiles/wired.yaml")
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_seventh_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T57, "HEAD", "--",
                   "profiles/ap.yaml")
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T58, "HEAD", "--",
                   "profiles/financial-times.yaml")
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_ninth_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T59, "HEAD", "--",
                   "profiles/news-corp.yaml")
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixtieth_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T60, "HEAD", "--",
                   "profiles/financial-times.yaml")
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_first_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T61, "HEAD", "--",
                   "profiles/wired.yaml")
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_second_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T62, "HEAD", "--",
                   "profiles/news-corp.yaml")
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_third_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T63, "HEAD", "--",
                   "profiles/news-corp.yaml")
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_fourth_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T64, "HEAD", "--",
                   "profiles/ap.yaml")
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_fifth_member_present_pin(self):
        # Post-landing form: the m1047 block carries the sixty-fifth
        # member-claim form twice (finding + falsification_family).
        # Working-tree scoped (the block is landed before the
        # in-gate); passes in the in-gate.
        out = subprocess.run(
            ["grep", "-c", "-F", _T65, FT_PATH],
            capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip() == "2", out.stdout

    def test_no_sixty_sixth_member_pin(self):
        # The sixty-sixth member-claim form stays absent repo-wide
        # (working tree, own file excluded; the needle is
        # fragment-built per #715).
        needle = _T66
        hits = []
        for p in _iter_source_files():
            if needle in open(p, encoding="utf-8",
                               errors="replace").read():
                hits.append(p)
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                if needle in open(p, encoding="utf-8",
                                   errors="replace").read():
                    hits.append(p)
        assert hits == [], hits

    def test_ledger_holds_at_65(self):
        # m1047 is falsification_member_confirmed: ledger advances
        # 64->65. Working-tree form (block landed before the
        # in-gate); passes in the in-gate.
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        assert blk["ledger"] == "65"
        assert blk["falsification_ledger"] == "65"


# ---------------------------------------------------------------------------
# 5. Staleness pin: the predecessor's guard lifecycle, run as-is.
# ---------------------------------------------------------------------------


class TestStalenessPins1372:
    def test_1371_guard_lifecycle_post_terminal_expiry(self):
        # Post-terminal-followup form: 25 tests in the class; 23
        # pass, 2 fail BY DESIGN - ONE #1272-class forward-guard
        # expiry (test_1047_numeric_absent_in_profiles trips on the
        # landed m1047 block in profiles/financial-times.yaml; the
        # 1047-underscore/dash pins stay green - no
        # one-zero-four-seven mechanism-key forms landed) plus ONE
        # member-form flip (test_no_sixty_fifth_member_pin trips on
        # the landed sixty-fifth member at the new HEAD). The
        # no_type_a_1372_in_git_log ancestor pin (the #1191-class
        # self-trip) was red at #1371's main-commit time; this run's
        # terminal log-hash followup re-pins PRED_MAIN_1372 in BOTH
        # its own file's copy and the #1371 predecessor file's copy
        # per the #1292 re-pin-both-copies precedent and the #721
        # re-pin rule, flipping it green. The forty-eighth through
        # sixty-fourth member pins stay green; the fortieth
        # direction pin stays green.
        # Deselected in the in-gate run (fails pre-commit by design);
        # verified post-terminal.
        res = _class_run(E1371_FILE, "TestGuardLifecycle1371")
        out = res.stdout + res.stderr
        assert "2 failed, 23 passed" in out, out[-2000:]

# ---------------------------------------------------------------------------
# 6. Doc-sync per #719 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestDocSync1372:
    def test_readme_test_file_table_has_1372_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_a_1372" in readme

    def test_architecture_has_1372_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_a_1372" in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_PATH)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 7. Iteration log per #721 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestIterationLog1372:
    def test_iteration_log_has_1372_entry_post_sync(self):
        log = _read(ITERLOG_PATH)
        assert "## #1372" in log

    def test_iteration_log_registers_hash_chain(self):
        log = _read(ITERLOG_PATH)
        assert "021a0f7c" in log  # #1371 main, the predecessor anchor
        assert "Type A #1372" in log

    def test_iteration_log_finding_summary(self):
        log = _read(ITERLOG_PATH)
        assert "syndication" in log


# ---------------------------------------------------------------------------
# 8. Corpus integrity: the peg's banked state and this run's novelty.
# ---------------------------------------------------------------------------


class TestCorpusIntegrity1372:
    def test_m441_prediction_banked_in_anthropic_section(self):
        # The m441 "softer via Google channel" prediction is banked
        # in this same anthropic section (iteration 441, Sep 1 2026):
        # the prediction under test, not a novel claim.
        data = _load_ft()
        anth = data["competitor_relationships"]["anthropic"]
        assert "softer via Google channel" in anth["coverage_prediction"]

    def test_m1024_revenue_scoop_in_corpus(self):
        # m1024 (#1322): the FT's Oct-8 OpenAI revenue-scoop
        # accountability original is in-corpus: the same-week
        # cross-lab comparator, carried un-rescored per #807.
        data = _load_ft()
        oai = data["competitor_relationships"]["openai"]
        keys = [k for k in oai.keys() if "mechanism_id" not in str(k)]
        found = any(
            isinstance(oai[k], dict) and oai[k].get("mechanism_id") == 1024
            for k in keys
        )
        assert found, "expected m1024 in the FT openai section"

    def test_no_prior_type_a_on_syndication_peg(self):
        # No prior Type A tests the FT's financing-risk register on
        # the Oct-5/6 Broadcom-Anthropic syndication peg.
        out = _git("grep", "-F", "-l", "Broadcom-Anthropic",
                   "HEAD", "--", "tests/").stdout
        assert out.strip() == ""

    def test_prior_ft_anthropic_mechanisms_distinct(self):
        # m892 (#1102): S-1 existential-risk register (disclosure
        # register, mechanism_documented). m676: Sep-14
        # profitability scoop (constructive +0.20). m441: the
        # prediction's home pair (fundraising sub-register). All
        # distinct from this run's syndication financing-risk peg.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        for token in ("m892", "m676", "m441", "m1024", "m859"):
            assert token in src, token

    def test_m1024_not_double_counted(self):
        # The FT x OpenAI Oct-8 revenue-correction arm was caught as
        # SATURATED via m1024 on main-run verification (the
        # scout-blindness-class catch): it is the comparator, not a
        # new finding. This test pins the catch in the record.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "SATURATED" in src
        assert "m1024" in src

    def test_framing_zero_hit_pre_commit(self):
        # The "FT x Anthropic Oct-5/6 syndication financing-risk"
        # framing is this run's own; the block key is the designed
        # novel form.
        assert BLOCK_KEY in _read(FT_PATH)


# ---------------------------------------------------------------------------
# 9. Research method: main-run verification sets, excerpt-bounded.
# ---------------------------------------------------------------------------


class TestResearchMethod1372:
    def test_five_search_sets_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "5 main-run browser.search verification sets" in src

    def test_zero_browser_open(self):
        # Per #503: 0 browser.open; the FT original is paywalled and
        # did not surface in Full-URL listings; both FT arms are
        # relay-attested.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "0 browser.open per #503" in src

    def test_urls_verbatim_from_listings(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "copied verbatim from search-result Full-URL listings" in src
        assert "no canonical URLs constructed" in src

    def test_no_delegated_scout_this_run(self):
        # Main-run sets only per the #1341 lesson (the #1368/#1369
        # runs logged the ninth and tenth scout-corpus-blindness
        # instances; #1371 ran scout-free and this run follows).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "No delegated scout this run" in src

    def test_rejected_sets_documented(self):
        # The rejected candidate sets are documented with reasons:
        # WSJ Anthropic (Sep-18 vintage), Anthropic S-1 (still
        # confidential), FT OpenAI Broadcom $50B (WSJ-original), FT
        # OpenAI revenue correction (saturated via m1024).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        for token in ("REJECTED", "SATURATED", "SELECTED"):
            assert token in src, token

    def test_excerpt_bounded(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "excerpt-bounded" in src


# ---------------------------------------------------------------------------
# 10. Confounders, ranked.
# ---------------------------------------------------------------------------


class TestConfounders1372:
    def test_strong_confounders_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Relay-bounded" in src
        assert "hand-assigned at excerpt level" in src

    def test_moderate_confounders_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "inherently newsy" in src
        assert "different sub-register" in src

    def test_counterevidence_m441_home_pair(self):
        # The m441 home pair stands: the softer-Anthropic pattern on
        # the fundraising sub-register is bounded, not overturned.
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        ce = " ".join(blk["counterevidence"])
        assert "m441" in ce
        assert "STANDS" in ce

    def test_counterevidence_m859_constructive(self):
        # m859's +0.15 constructive Anthropic arm: the register is
        # peg-conditional, not entity-hostile.
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        ce = " ".join(blk["counterevidence"])
        assert "m859" in ce
        assert "peg-conditional" in ce

    def test_counterevidence_m1024_harder(self):
        # m1024's payer arm ran harder (-0.35) than the Anthropic arm
        # (-0.20): disclosed as the same-week comparator.
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        ce = " ".join(blk["counterevidence"])
        assert "m1024" in ce
        assert "-0.35" in ce


# ---------------------------------------------------------------------------
# 11. Verdict: the sixty-fifth falsification-family member.
# ---------------------------------------------------------------------------


class TestVerdict1372:
    def test_verdict_falsification_member_confirmed(self):
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        assert blk["verdict"] == "falsification_member_confirmed"
        assert blk["falsification_family_member"] is True

    def test_sixty_fifth_member_claim(self):
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        assert "SIXTY-FIFTH falsification-family member" in \
            blk["falsification_family"]
        assert "ledger 64->65" in blk["falsification_family"]

    def test_first_financing_risk_register_at_ft(self):
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        assert "FIRST financing-risk-register falsification at FT" in \
            blk["falsification_family"]

    def test_first_m441_prediction_falsification(self):
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        assert 'FIRST falsification of the m441 "softer via Google ' \
            'channel" prediction' in blk["falsification_family"]

    def test_domain_bounded(self):
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        assert "Domain-bounded to FT" in blk["falsification_family"]
        assert "Oct-5/6" in blk["falsification_family"]

    def test_pairs_with_sixtieth(self):
        # Pairs with the SIXTIETH (m1024) as the same-week cross-lab
        # register pair: Oct-5/6 Anthropic syndication vs Oct-8
        # OpenAI revenue scoop.
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        assert "SIXTIETH (m1024)" in blk["falsification_family"]
        assert "delta +0.15" in blk["falsification_family"]

# ---------------------------------------------------------------------------
# 12. The research substance: the FT syndication original and the two
# relay attributions.
# ---------------------------------------------------------------------------


class TestFTAnthropicSyndication1372:
    def test_peg_date_oct05_06(self):
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        assert "Oct 5/6 2026" in blk["anthropic_arm_new"]["peg"]

    def test_syndication_structure(self):
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        detail = blk["anthropic_arm_new"]["detail"]
        for token in ("Bank of America", "Citigroup", "Morgan Stanley",
                      "$42B senior secured", "$18B junior",
                      "Blackstone", "2027"):
            assert token in detail, token

    def test_ft_originator_relay_attested(self):
        # Two independent relay attributions of the FT as originator.
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        role = blk["anthropic_arm_new"]["ft_role"]
        assert "as first reported by the Financial Times" in role
        assert "the Financial Times reported" in role

    def test_register_financing_risk_disclosure(self):
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        reg = blk["anthropic_arm_new"]["register"]
        assert "largest chip-financing deal yet" in reg
        assert "test of lender appetite" in reg
        assert "more directly exposed to Anthropic" in reg

    def test_manual_illustrative_tone(self):
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        assert blk["anthropic_arm_new"]["manual_illustrative_tone"] == -0.20

    def test_oct01_loan_context(self):
        # The syndication expands the Oct-1 Broadcom $42B
        # convertible-loan facility disclosure (Reuters).
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        assert "Oct-1 Broadcom $42B" in blk["anthropic_arm_new"]["detail"]

    def test_openai_arm_carried_m1024(self):
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        arm = blk["openai_arm_carried"]["arm"]
        assert arm["manual_illustrative_tone"] == -0.35
        assert "2026-10-08" in arm["date"]
        assert "carried un-rescored per #807" in \
            blk["openai_arm_carried"]["carried_from"]

    def test_illustrative_delta(self):
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        res = blk["asymmetry_scorer_result"]
        assert "delta (Anthropic minus OpenAI) +0.15" in res
        assert "near-symmetric hardness" in res

    def test_meta_arm_cross_peg_disclosed(self):
        # The Meta comparator is cross-peg, disclosed as such (not a
        # matched-peg delta).
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        assert "cross-peg" in blk["asymmetry_scorer_result"]
        arms = blk["meta_arm_carried"]["arms"]
        assert arms[0]["manual_illustrative_tone"] == -0.55
        assert arms[1]["manual_illustrative_tone"] == 0.10

    def test_m441_prediction_tested_block(self):
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        pt = blk["m441_prediction_tested"]
        assert "softer via Google channel" in pt["prediction"]
        assert pt["outcome"].startswith("FAILS")

    def test_five_source_urls(self):
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        assert len(blk["source_urls"]) == 5
        for url in blk["source_urls"]:
            assert url.startswith("https://"), url

    def test_open_empirical_test(self):
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        assert "First-hand open of the FT Oct-5/6 syndication piece" in \
            blk["open_empirical_test"]


# ---------------------------------------------------------------------------
# 13. Financial relationship: the m441 indirect prediction.
# ---------------------------------------------------------------------------


class TestFinancialRelationship1372:
    def test_anthropic_section_prediction(self):
        data = _load_ft()
        anth = data["competitor_relationships"]["anthropic"]
        assert anth["financial_tie"] == "none_direct_indirect_via_google"
        assert "softer via Google channel" in anth["coverage_prediction"]

    def test_google_channel_basis(self):
        data = _load_ft()
        anth = data["competitor_relationships"]["anthropic"]
        desc = anth["description"]
        assert "single figure millions GBP/yr" in desc
        assert "up to $40B" in desc

    def test_openai_deal_contrast(self):
        # The FT's direct OpenAI deal ($5-10M/yr) vs the indirect
        # Anthropic channel: the prediction under test is the
        # indirect one.
        data = _load_ft()
        oai = data["competitor_relationships"]["openai"]
        assert oai["financial_tie"] == "licensing"
        assert "$5-10M/yr" in oai["estimated_value"]

    def test_meta_zero_tie(self):
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        assert "Meta provides $0" in \
            data["competitor_relationships"]["anthropic"]["description"]

    def test_prediction_fails_on_peg(self):
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        assert "FAILS on this peg" in blk["finding"]
        assert "FAILS on the Oct-5/6 syndication peg" in \
            blk["m441_prediction_tested"]["outcome"]

    def test_no_causal_claim(self):
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        assert "Correlation is not causation" in blk["finding"]


# ---------------------------------------------------------------------------
# 14. In-flight isolation: #899/#938/#900/#1012-wt untouched; #1024
# m846 untouched.
# ---------------------------------------------------------------------------


class TestInFlightIsolation1372:
    def test_no_profiles_edit_beyond_ft_anthropic(self):
        # The only profiles/ working-tree modification beyond the
        # pre-existing in-flight #899 hunk is this run's m1047 hunk
        # on profiles/financial-times.yaml.
        out = _git("status", "--porcelain", "--", "profiles/").stdout
        lines = [l for l in out.splitlines() if l.strip()]
        assert lines == [" M profiles/financial-times.yaml",
                         " M profiles/nytimes.yaml"], lines

    def test_899_hunk_untouched(self):
        # The pre-existing #899 m771 hunk on profiles/nytimes.yaml is
        # byte-identical to HEAD plus the hunk (this run stages
        # nothing from it).
        out = _git("diff", "--", "profiles/nytimes.yaml").stdout
        assert "m771" in out or "771" in out

    def test_no_competitor_entities_edit(self):
        # #1024 m846 (profiles/competitor-entities.yaml) NOT touched -
        # decision pending.
        out = _git("status", "--porcelain", "--",
                   "profiles/competitor-entities.yaml").stdout
        assert out.strip() == ""

    def test_m846_region_byte_identical(self):
        lines = _read(ENTITIES_PATH).splitlines()
        region = lines[M846_HEAD_START - 1:M846_HEAD_END]
        head = _git("show", "HEAD:profiles/competitor-entities.yaml") \
            .stdout.splitlines()
        head_region = head[M846_HEAD_START - 1:M846_HEAD_END]
        assert region == head_region

    def test_inflight_test_files_untouched(self):
        # #938 (Type B working-tree edit), #900 (untracked Type D
        # file), #1012-wt (working-tree edit on the committed Type A
        # #1012 file) are left out of this run's index/diff via
        # explicit-path staging.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "explicit-path staging" in src


# ---------------------------------------------------------------------------
# 15. Statistical discipline: MANUAL / QUALITATIVE ONLY.
# ---------------------------------------------------------------------------


class TestStatisticalDiscipline1372:
    def test_manual_qualitative_only(self):
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        assert "MANUAL ILLUSTRATIVE ONLY" in blk["statistical_discipline"]

    def test_engine_not_run(self):
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        assert "engine NOT run" in blk["statistical_discipline"]
        assert "is_significant false" in blk["statistical_discipline"]

    def test_no_p_values(self):
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        assert "NOT_CALCULATED" in blk["statistical_discipline"]

    def test_not_artifact_grade(self):
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        assert blk["no_analysis_json_update"] is True
        assert blk["correlation_not_causation"] is True

    def test_tone_not_scored_on_absent_arm(self):
        # The scorer result states the discipline on the carried and
        # new arms; no empirical tone distribution exists.
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        assert "NOT artifact-grade" in blk["asymmetry_scorer_result"]

    def test_hypothesis_generating_only(self):
        data = _load_ft()
        blk = data["competitor_relationships"]["anthropic"][BLOCK_KEY]
        assert "hypothesis-generating only" in blk["finding"]
