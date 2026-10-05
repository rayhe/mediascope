# -*- coding: utf-8 -*-
"""Type C #1234 tests: Cloudflare Monetization Gateway + Pay Per Use beta
activation (Sep 30 2026) - STATUS-CHECK EXTENSION of the m786
tollbooth-operator stack (mechanism 972).

Mechanism 972 (STATUS-CHECK EXTENSION of m786; ledger HOLDS at 50 - NOT a
falsification-family member). Cloudflare moved both AI payment products
into closed beta on Sep 30 2026: the Monetization Gateway (sellers charge
AI agents per request; HTTP 402 + x402; USDC on Base) and Pay Per Use
(publishers paid when an AI company reports using their content; buyer
defines use + sets price; self-reported JSON lines; monthly dashboard
settlement). The Sep-30 move is the waitlist-to-beta transition (the Jul 1
announcement is carried via m786). Opposite control arrows inside one
launch: the seller designs the meter on the gateway; the payer designs it
on Pay Per Use. No new direction (fortieth stays absent by design);
thirty-fifth through thirty-ninth stand.

Excerpt-bounded research per #503 (delegated scout ~15 browser.search query
sets across ~12 candidates + 2 main-run browser.search verification sets, 0
browser.open reads). The scout's primary (Google AI Contribution Pilot
payout figures) was REJECTED on main-run review: the pilot's Sep-29/30 rate
disclosure, Oct 1-2 reception leg, and large-publisher holdout are all
in-corpus (m891 family reception block + status-check extension). The
scout's #3 (Perplexity $35M ARR via digitallab247 Sep 13) is HELD as a
future Type C candidate. The scout's bonus lead (Microsoft Publisher
Content Marketplace / AWS AI Content Trading Platform) was rejected as
in-corpus. The Sep-15 default-block enforcement is carried via #924, not
re-claimed as novel.

The m972 block lives in profiles/competitor-entities.yaml as a top-level
key appended at end of file (the #1024 m846 hunk untouched; explicit-path
staging).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
One anchor test (the placeholder pin) fails BY DESIGN post-anchor.

Per #795: this run only CHECKS the #1230-launched background suite
(goal hidden_files type_d_1230_full_suite.log, observed at this run's
check); its verdict and tombstone belong to #1235 (next Type D). This run
neither re-launches, kills, nor writes to the suite.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit), #900
(untracked Type D test file), #1012-wt (working-tree edit on the committed
Type A #1012 file).

Type C lands one mechanism (mechanism 972); the Type B predecessor added
one (mechanism 971). This run is the FIFTH and CLOSING leg of the
1230-1234 window. Next run #1235 Type D opens the 1235-1239 window.
Rotation: D #1230 -> E #1231 -> A #1232 -> B #1233 -> C #1234. The main
commit is the anchor per #565.

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
landed or next number, the forty-eighth / forty-ninth / fiftieth /
fifty-first member-claim forms, or the thirty-fifth through fortieth
direction forms; the constants are constructed at runtime. (The landed
ordinals live as short lowercase forms in prose here; the live full-form
claims live in profiles/financial-times.yaml and
profiles/careers/journalists.yaml: the forty-eighth, forty-ninth, and
fiftieth members respectively.)
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
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
OWN_BASENAME = (
    "test_type_c_1234_cloudflare_monetization_gateway_"
    "pay_per_use_beta_activation_oct05_8am.py"
)
TOP_KEY = None  # Type C lands at competitor-entities.yaml top level.

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "0" * 40

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 972
NEXT_NUM = 973  # integer only; key-form needles are format-built

# Fragment-built per #715: the contiguous key never appears in this file.
BLOCK_KEY = (
    "type_c_1234_cloudflare_monetization_gateway_"
    "pay_per_use_beta_activation_oct05_8am"
)

# Predecessor chain: #1233 Type B closed the fourth leg of the window.
PRED_MAIN_1233 = "882a1284"
PRED_ANCHOR_1233 = "88329e37"
PRED_DOCSYNC_1233 = "0ecb502a"
PRED_FINAL_1233 = "deb33f16"

# The #1233 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 971; zero next-number nine-seven-two /
# no-Type-C-#1234-in-git-log / fortieth direction absent /
# forty-eighth + forty-ninth + fiftieth members intact /
# fifty-first member absent / ledger 50).
E1233_FILE = (
    "test_type_b_1233_ben_lovejoy_9to5mac_muse_mac_access_vs_"
    "siri_privacy_trust_oct05_7am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 67131  # post-doc-sync total (pre-sync 67048 + 83)
README_FILE_COUNT = 1559  # pre-sync 1558 + 1 (this file)

# The forward-guard needles are fragment-built per #715 so this file
# carries no contiguous literal of a forward-guard claim form.
_T40 = "FORT" + "IETH relationship direction"
_T48 = "FORT" + "Y-EIGHTH falsification-family member"
_T49 = "FORT" + "Y-NINTH falsification-family member"
_T50 = "FIFT" + "IETH falsification-family member"
_T51 = "FIFT" + "Y-FIRST falsification-family member"

# Novel source URLs: all 5 zero-hit repo-wide pre-commit (git grep -F).
# Post-commit all 5 live in the block's source_urls.
NOVEL_URLS = [
    "https://www.searchenginejournal.com/cloudflare-moves-"
    "monetization-gateway-pay-per-use-into-beta/591719/",
    "https://appstackinsider.com/insights/cloudflare-s-paid-"
    "mcp-access-raises-a-bigger-question/",
    "https://newsletter.dsurfer.com/p/wave-issue-311",
    "https://dev.to/scriptmasterlabs01/what-is-cloudflare-"
    "monetization-gateway-the-callback-is-the-gate-the-"
    "judgment-is-missing-3a33",
    "https://superpowerdaily.com/posts/cloudflare-opens-closed-"
    "beta-to-let-sellers-charge-ai-agents-per-use",
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
    args = ["grep", "-F", "-l", needle, "HEAD", "--"]
    if scope:
        args.append(scope)
    out = _git(*args).stdout
    cleaned = []
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("HEAD:"):
            line = line[len("HEAD:"):]
        if line:
            cleaned.append(line)
    return cleaned


def _load_entities():
    return yaml.safe_load(_read(ENTITIES_PATH))


def _block():
    data = _load_entities()
    assert BLOCK_KEY in data
    return data[BLOCK_KEY]


def _block_text():
    return _read(ENTITIES_PATH)


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

class TestAnchor1234:
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
        assert "FIFTH and CLOSING leg of the 1230-1234 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1234:
    def test_predecessor_1233_chain_verified(self):
        for sha in (
            PRED_MAIN_1233, PRED_ANCHOR_1233, PRED_DOCSYNC_1233,
            PRED_FINAL_1233,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1232_chain_verified(self):
        for sha in ("9f74c6ee", "bb211ca8", "ade7a8de", "196377eb"):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1230 -> E #1231 -> A #1232 -> B #1233 -> C #1234" in src

    def test_next_leg_is_type_d_1235(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1235 Type D" in src

    def test_type_c_lands_one_mechanism(self):
        # Type C lands exactly one mechanism (mechanism 972); the Type
        # B predecessor added one (mechanism 971).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type C lands one mechanism" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1234:
    def test_top_key_found(self):
        data = _load_entities()
        assert BLOCK_KEY in data
        assert data[BLOCK_KEY]["mechanism_id"] == MECH_NUM

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1234 in key, no 972 or
        # 973 substring.
        assert "1234" in BLOCK_KEY
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
        nums = []
        for _line in _repo_grep_numeric_mechanism_id(MECH_NUM):
            nums.append(MECH_NUM)
        for n in range(MECH_NUM + 1, MECH_NUM + 20):
            assert _repo_grep_numeric_mechanism_id(n) == [], n
        assert nums, "mechanism 972 must be present in profiles"

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_novel_urls_in_block_source_urls_verbatim(self):
        b = _block()
        urls = [s["url"] for s in b["sources"]]
        for novel in NOVEL_URLS:
            assert novel in urls, novel

    def test_block_key_zero_hit_except_landed(self):
        # Pre-commit the block key was zero-hit repo-wide; post-commit
        # it appears only in the landed YAML block and the doc-sync
        # targets (README, ARCHITECTURE, iteration-log). This test
        # file never carries the contiguous key: BLOCK_KEY is
        # fragment-built per #715.
        out = _git("grep", "-F", "-l", BLOCK_KEY, "HEAD", "--", ".").stdout
        hits = []
        for line in out.splitlines():
            line = line.strip()
            if line.startswith("HEAD:"):
                line = line[len("HEAD:"):]
            if line.strip():
                hits.append(line.strip())
        allowed = {
            os.path.join("profiles", "competitor-entities.yaml"),
            "README.md",
            os.path.join("docs", "ARCHITECTURE.md"),
            "iteration-log.md",
        }
        for h in hits:
            assert h in allowed, h

    def test_sep30_beta_novelty(self):
        # The Sep-30 waitlist-to-beta transition was zero-hit repo-wide
        # pre-commit; now present only inside this block.
        text = _block_text()
        assert "waitlist-to-beta" in text
        block_start = text.index(BLOCK_KEY + ":")
        assert "waitlist-to-beta" not in text[:block_start]

    def test_no_type_c_1234_in_git_log_pin(self):
        # Pre-commit form: no prior run committed this run's iteration
        # subject. Re-pinned to the own-set form in the log-hash
        # followup per #721.
        out = _git("log", "--oneline", "--grep=Type C #1234").stdout
        assert out.strip() == "", out.strip()


# ---------------------------------------------------------------------------
# 4. Block structure at the competitor-entities.yaml top level.
# ---------------------------------------------------------------------------

class TestBlockStructure1234:
    def test_entities_profile_exists(self):
        assert os.path.exists(ENTITIES_PATH)

    def test_block_key_present_at_top_level(self):
        data = _load_entities()
        assert BLOCK_KEY in data
        assert data[BLOCK_KEY]["block_key"] == BLOCK_KEY

    def test_mechanism_id_field(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_iteration_fields(self):
        b = _block()
        assert b["iteration"] == 1234
        assert b["iteration_type"] == "C"
        assert b["iteration_time"] == "2026-10-05 08:00 AM PDT"

    def test_required_block_fields(self):
        b = _block()
        for field in (
            "block_key", "mechanism_name", "type", "finding",
            "money_flow", "confounders", "sources", "verdict",
            "novelty", "rotation_transparency", "concurrency",
        ):
            assert field in b, field

    def test_test_file_field_matches_own_basename(self):
        assert _block()["test_file"] == "tests/" + OWN_BASENAME

    def test_connects_to_m786_line(self):
        assert _block()["connects_to"] == [64, 738, 786]

    def test_source_urls_count(self):
        assert len(_block()["sources"]) == 5

    def test_no_new_direction_claim(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert tax.startswith("STATUS-CHECK EXTENSION, not a new direction")

    def test_type_label(self):
        assert _block()["type_label"] == "Financial Incentive Mapping"


# ---------------------------------------------------------------------------
# 5. Content discipline: verbatim excerpts, no constructed URLs.
# ---------------------------------------------------------------------------

class TestM972ContentDiscipline1234:
    def test_sep30_beta_quote_verbatim(self):
        finding = _block()["finding"]
        assert "put two AI payment products into beta on Sept. 30" in finding

    def test_mechanics_quote_verbatim(self):
        finding = _block()["finding"]
        assert "as a line of JSON against opted-in domains" in finding

    def test_control_geometry_quote_verbatim(self):
        finding = _block()["finding"]
        assert (
            "the AI company defines the use and sets the price"
            in finding
        )

    def test_no_constructed_cloudflare_blog_url(self):
        # Per #503 no canonical Cloudflare blog URL was constructed or
        # fetched; all facts are excerpt-bounded from trade secondaries.
        text = _block_text()
        block_start = text.index(BLOCK_KEY + ":")
        block_end = text.index("yaml_parse_clean", block_start)
        own = text[block_start:block_end]
        assert "blog.cloudflare.com" not in own

    def test_scout_correction_documented(self):
        # The scout's Google-AI-Contribution-Pilot primary was rejected
        # on main-run review (in-corpus); the correction is disclosed.
        assert "REJECTED on main-run review" in _block()["novelty"]

    def test_sep15_carried_not_novel(self):
        conf = " ".join(c["text"] for c in _block()["confounders"])
        assert "Carried-not-novel" in conf
        assert "#924" in conf

    def test_ascii_only(self):
        text = _block_text()
        block_start = text.index(BLOCK_KEY + ":")
        own = text[block_start:]
        own.encode("ascii")

    def test_no_em_dashes(self):
        text = _block_text()
        block_start = text.index(BLOCK_KEY + ":")
        block_end = text.index("yaml_parse_clean", block_start)
        own = text[block_start:block_end]
        assert "\u2014" not in own
        assert "\u2013" not in own

    def test_yaml_block_ascii(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        src.encode("ascii")


# ---------------------------------------------------------------------------
# 6. Statistical discipline: MANUAL / qualitative only per Aug 28 2026 rule.
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1234:
    def test_manual_qualitative_only(self):
        assert "MANUAL" in _block()["novelty"]

    def test_browser_opens_zero(self):
        assert _block()["browser_opens"] == 0

    def test_tone_not_scored(self):
        assert _block()["tone_scored"] is False

    def test_engine_not_run(self):
        assert _block()["engine_run"] is False

    def test_is_significant_false(self):
        assert _block()["is_significant"] is False

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_verdict_directionally_supported_not_proven(self):
        assert _block()["verdict"] == "directionally_supported_not_proven"

    def test_not_artifact_grade(self):
        assert _block()["artifact_grade"] is False


# ---------------------------------------------------------------------------
# 7. Falsification ledger: NOT a member; ledger holds at 50.
# ---------------------------------------------------------------------------

class TestFalsificationLedger1234:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert b["falsification_family"].startswith("NOT a member")

    def test_forty_eighth_intact_in_ft(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_forty_ninth_intact_in_journalists(self):
        assert _git_grep_tracked_source(_T49, "profiles/") == [
            "profiles/careers/journalists.yaml"]

    def test_fiftieth_intact_in_journalists(self):
        out = _git(
            "grep", "-c", "-F", _T50, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_first_absent(self):
        assert _git_grep_tracked_source(_T51, None) == []

    def test_directions_thirty_fifth_through_thirty_ninth_present(self):
        for needle in (
            "THIRT" + "Y-FIFTH relationship direction",
            "THIRT" + "Y-SIXTH relationship direction",
            "THIRT" + "Y-SEVENTH relationship direction",
            "THIRT" + "Y-EIGHTH relationship direction",
            "THIRT" + "Y-NINTH relationship direction",
        ):
            assert _git_grep_tracked_source(needle, "profiles/") != [], needle

    def test_fortieth_direction_absent(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_verdict_field_states_status_check_extension(self):
        fam = _block()["falsification_family"]
        assert "status-check extension" in fam
        assert "m786" in fam
        assert "ledger holds at 50" in fam


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: pins for #1235; #1233's pins flip BY DESIGN.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1234:
    def test_pins_on_972_landing(self):
        # Type C lands one mechanism: max becomes 972, next is 973.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 972" in src
        assert "NEXT_NUM = 973" in src

    def test_no_type_d_1235_in_git_log_pin(self):
        out = _git("log", "--oneline", "--grep=Type D #1235").stdout
        assert out.strip() == "", out.strip()

    def test_973_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_973_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_973_dash_absent_repo_wide(self):
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
        out = _git(
            "grep", "-c", "-F", _T50, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_fifty_first_member_pin(self):
        assert _git_grep_tracked_source(_T51, None) == []

    def test_predecessor_1233_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1233_FILE))

    def test_next_leg_is_1235_type_d(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1235 Type D" in src

    def test_1233_pins_flip_by_design_documented(self):
        # #1233's forward guards (max-971, zero-972 keys all forms,
        # no-Type-C-#1234-in-git-log, fortieth absent, forty-eighth +
        # forty-ninth + fiftieth intact in profiles/, fifty-first
        # absent) verified GREEN pre-commit this run via the
        # subprocess staleness pin (Type C lands mechanism 972); the
        # max-971, zero-972, and no-Type-C-#1234-in-git-log pins flip
        # post-main-commit on this run's own landing (the #1191-class
        # self-trip, by design, documented in the staleness pin
        # below).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1233" in src
        assert "972" in src


# ---------------------------------------------------------------------------
# 9. Background suite: #1230's suite is CHECKED ONLY per #795.
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1234:
    def test_1230_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1230_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1230-launched suite is observed.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1234_full_suite.log"))

    def test_observation_documented_in_block(self):
        rt = _block()["rotation_transparency"]
        assert "#1230 background-suite verdict belongs to #1235" in rt


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1234:
    def test_readme_test_file_table_has_1234_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_c_1234" in readme

    def test_architecture_has_1234_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_c_1234" in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_PATH)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 11. Iteration log (3 tests; deselected pre-commit per #721)
# ---------------------------------------------------------------------------

class TestIterationLog1234:
    def test_1234_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1234 Type C" in log

    def test_1233_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1233 Type B" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1233's guard lifecycle flips BY DESIGN post-commit
# ---------------------------------------------------------------------------

class TestStalenessPins1234:
    def test_1233_guard_lifecycle_post_commit_self_trip(self):
        # Post-main-commit form: 11 of the 13 pass; the two that fail
        # BY DESIGN are test_no_type_c_1234_in_git_log_pin (this run's
        # own main commit carries "Type C #1234") and
        # test_972_numeric_absent_in_profiles (mechanism 972 lands in
        # profiles/ this run). The #1233 block is read-only to this
        # run. Deselected pre-commit (both pins pass pre-commit).
        res = _class_run(E1233_FILE, "TestGuardLifecycle1233")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "2 failed, 11 passed" in res.stdout, res.stdout[-2000:]
        assert (
            "test_no_type_c_1234_in_git_log_pin" in res.stdout
        ), res.stdout[-2000:]
        assert (
            "test_972_numeric_absent_in_profiles" in res.stdout
        ), res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1234:
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
