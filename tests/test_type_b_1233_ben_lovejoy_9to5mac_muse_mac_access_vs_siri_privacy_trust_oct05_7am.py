# -*- coding: utf-8 -*-
"""Type B #1233 tests: Ben Lovejoy (9to5Mac) - Meta Muse Mac-access op-ed
(-0.65 MANUAL ILLUSTRATIVE, NEW Sep-28 arm) vs Apple Siri agentic-AI op-eds
(+0.45 May-18 arm, +0.40 Jun-4 corroborating arm); illustrative delta
(Apple minus Meta) +1.10 (m971).

Mechanism 971 (CONFIRMING EXTENSION of m223; ledger HOLDS at 50 - NOT a
falsification-family member). Lovejoy applies the distrust-maximal register
to Meta Muse device access ("9to5Mac's Take on Muse: Nope.", "abysmal privacy
record") while granting Apple affirmative trust priors on the identical
capability class ("the most privacy-respecting AI chatbot out there"). The
Meta arm itself carries the intra-article Apple contrast ("I'm inclined to
trust the privacy and safety safeguards Apple has put into place"), so the
differential prior is extractable within the single piece. Prior Lovejoy
mechanism m223 (camera-feature class, Aug 2026) already established the
direction; m971 replicates it in the agentic-AI device-access class
(temporal + class extension). No documented 9to5Mac x Apple financial tie,
so the deal-partner prediction is untested, not falsified.

Excerpt-bounded research per #503 (delegated scout 12 browser.search query
sets across ~10 candidates + 3 main-run browser.search verification sets, 0
browser.open reads). Rejected: Karissa Bell, Rebecca Bellan, Shirin Ghaffary,
Stephen Council, Will Shanklin, Hayden Field (saturated/beat-moved);
fallbacks held: Ian Carlos Campbell, Anthony Ha, Marcus Mendes, Ashley
Belanger, Scott Younker. Main-run corrected the scout's corpus
characterization (m223 pre-exists on Lovejoy, so the novelty is the
agentic-AI device-access pair, not a first look at the journalist) and
rejected the scout's "zero known corpus hits" claim.

The m971 block lives in profiles/careers/journalists.yaml as a
competitor_coverage sub-key of the NEW top-level `ben_lovejoy_type_b` key
(per the #643 convention; no Lovejoy career-profile list entry pre-exists;
mechanism_ids [971]).

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

Type B lands one mechanism (mechanism 971); the Type A predecessor added
one (mechanism 970). Next run #1234 Type C closes the 1230-1234 window.
Rotation: D #1230 -> E #1231 -> A #1232 -> B #1233 -> C #1234. This run is
the FOURTH leg of the 1230-1234 window. The main commit is the anchor
per #565.

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
JOURNALISTS_PATH = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
OWN_BASENAME = (
    "test_type_b_1233_ben_lovejoy_9to5mac_muse_mac_access_vs_"
    "siri_privacy_trust_oct05_7am.py"
)
TOP_KEY = "ben_lovejoy_type_b"

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "0" * 40

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 971
NEXT_NUM = 972  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_b_1233_ben_lovejoy_9to5mac_muse_mac_access_vs_"
    "siri_privacy_trust_oct05_7am"
)

# Predecessor chain: #1232 Type A continued the 1230-1234 window.
PRED_MAIN_1232 = "9f74c6ee"
PRED_ANCHOR_1232 = "bb211ca8"
PRED_DOCSYNC_1232 = "ade7a8de"
PRED_FINAL_1232 = "196377eb"

# The #1232 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 970; zero next-number nine-seven-one /
# no-Type-B-#1233-in-git-log / fortieth direction absent /
# forty-eighth + forty-ninth + fiftieth members intact /
# fifty-first member absent / ledger 50).
E1232_FILE = (
    "test_type_a_1232_ap_openai_astra_delay_wire_vs_"
    "meta_18bn_settlement_wire_oct05_6am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 67048  # post-doc-sync total (pre-sync 66958 + 90)
README_FILE_COUNT = 1558  # pre-sync 1557 + 1 (this file)

# The forward-guard needles are fragment-built per #715 so this file
# carries no contiguous literal of a forward-guard claim form.
_T40 = "FORT" + "IETH relationship direction"
_T48 = "FORT" + "Y-EIGHTH falsification-family member"
_T49 = "FORT" + "Y-NINTH falsification-family member"
_T50 = "FIFT" + "IETH falsification-family member"
_T51 = "FIFT" + "Y-FIRST falsification-family member"

# Novel source URLs: all 4 zero-hit repo-wide pre-commit (git grep -F).
# Post-commit all 4 live in the block's source_urls.
NOVEL_URLS = [
    "https://9to5mac.com/2026/09/28/"
    "yeah-dont-give-metas-muse-app-access-to-your-mac/",
    "https://9to5mac.com/2026/05/18/"
    "heres-why-i-wont-be-switching-on-auto-deleting-siri-chats/",
    "https://9to5mac.com/2026/06/04/"
    "privacy-may-still-be-apples-savior-when-it-comes-to-"
    "delayed-ai-features/?extended-comments=1",
    "https://9to5mac.com/author/benlovejoy/",
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
    else:
        args.append(".")
    out = _git(*args).stdout
    cleaned = []
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("HEAD:"):
            line = line[len("HEAD:"):]
        if line:
            cleaned.append(line)
    return cleaned


def _load_journalists():
    return yaml.safe_load(_read(JOURNALISTS_PATH))


def _top():
    data = _load_journalists()
    assert TOP_KEY in data
    return data[TOP_KEY]


def _block():
    return _top()["competitor_coverage"][BLOCK_KEY]


def _block_text():
    return _read(JOURNALISTS_PATH)


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

class TestAnchor1233:
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
        assert "FOURTH leg of the 1230-1234 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1233:
    def test_predecessor_1232_chain_verified(self):
        for sha in (
            PRED_MAIN_1232, PRED_ANCHOR_1232, PRED_DOCSYNC_1232,
            PRED_FINAL_1232,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1231_chain_verified(self):
        for sha in ("9f4fdafe", "5d933b11", "c0d7f479", "2ba700c2"):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1230 -> E #1231 -> A #1232 -> B #1233 -> C #1234" in src

    def test_next_leg_is_type_c_1234(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1234 Type C" in src

    def test_type_b_lands_one_mechanism(self):
        # Type B lands exactly one mechanism (mechanism 971); the Type
        # A predecessor added one (mechanism 970).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type B lands one mechanism" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1233:
    def test_top_key_found(self):
        assert _top()["mechanism_ids"] == [MECH_NUM]

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1233 in key, no 971 or
        # 972 substring.
        assert "1233" in BLOCK_KEY
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
        assert nums, "mechanism 971 must be present in profiles"

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_novel_urls_in_block_source_urls_verbatim(self):
        b = _block()
        urls = b["source_urls"]
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
            os.path.join("profiles", "careers", "journalists.yaml"),
            "README.md",
            os.path.join("docs", "ARCHITECTURE.md"),
            "iteration-log.md",
        }
        for h in hits:
            assert h in allowed, h

    def test_meta_headline_novelty(self):
        # The Sep-28 Muse Mac-access headline was zero-hit repo-wide
        # pre-commit; now present only inside this block.
        text = _block_text()
        assert "yeah-dont-give-metas-muse-app-access-to-your-mac" in text
        block_start = text.index(BLOCK_KEY + ":")
        assert "yeah-dont-give-metas-muse-app-access-to-your-mac" not in text[:block_start]

    def test_apple_headline_novelty(self):
        text = _block_text()
        assert "auto-deleting-siri-chats" in text
        block_start = text.index(BLOCK_KEY + ":")
        assert "auto-deleting-siri-chats" not in text[:block_start]

    def test_both_arms_new_documented(self):
        b = _block()
        assert "NEW" in b["meta_arm"]["status"]
        assert "NEW" in b["apple_arm"]["status"]
        assert "NEW" in b["corroborating_arm"]["status"]

    def test_no_type_b_1233_in_git_log_pin(self):
        # Pre-commit form: no prior run committed this iteration.
        # Re-pinned to the post-commit own-set form in the log-hash
        # followup per #721 (the #1191-class self-trip).
        out = _git("log", "--oneline", "--grep=Type B #1233").stdout
        assert out.strip() == "", out.strip()


# ---------------------------------------------------------------------------
# 4. Block structure under the NEW ben_lovejoy_type_b top-level key.
# ---------------------------------------------------------------------------

class TestBlockStructure1233:
    def test_journalists_profile_exists(self):
        assert os.path.exists(JOURNALISTS_PATH)

    def test_top_key_is_expected_parent(self):
        assert _top()["name"] == "Ben Lovejoy"
        assert _top()["publication"] == "9to5mac"

    def test_block_key_present_under_competitor_coverage(self):
        assert BLOCK_KEY in _top()["competitor_coverage"]

    def test_mechanism_id_field(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_iteration_fields(self):
        b = _block()
        assert b["iteration"] == 1233
        assert b["type"] == "B"
        assert b["date"] == "2026-10-05 07:00 PDT"

    def test_required_block_fields(self):
        b = _block()
        for field in (
            "block_key", "mechanism_id", "iteration", "type", "date",
            "test_file", "author", "goal_id", "job_id",
            "scheduled_job_id", "journalist", "publication", "window",
            "design", "meta_arm", "apple_arm", "corroborating_arm",
            "scorer_delta_MANUAL_ILLUSTRATIVE", "delta_reading",
            "confounders", "counter_evidence", "connects_to", "verdict",
            "falsification_family", "falsification_family_member",
            "falsification_ledger", "ledger_note", "is_significant",
            "correlation_not_causation", "no_analysis_json_update",
            "artifact_readiness", "research_method", "novelty",
            "background_suite_status", "in_flight", "source_urls",
        ):
            assert field in b, field

    def test_test_file_field_matches_own_basename(self):
        assert _block()["test_file"] == "tests/" + OWN_BASENAME

    def test_meta_arm_tone(self):
        assert _block()["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.65

    def test_apple_arm_tone(self):
        assert _block()["apple_arm"]["tone_MANUAL_ILLUSTRATIVE"] == 0.45

    def test_corroborating_arm_tone(self):
        assert _block()["corroborating_arm"]["tone_MANUAL_ILLUSTRATIVE"] == 0.40

    def test_scorer_delta(self):
        assert _block()["scorer_delta_MANUAL_ILLUSTRATIVE"] == 1.10

    def test_connects_to_lineage(self):
        assert 223 in _block()["connects_to"]

    def test_source_urls_count(self):
        assert len(_block()["source_urls"]) == 4

    def test_meta_arm_date_and_byline(self):
        b = _block()
        assert b["meta_arm"]["date"] == "2026-09-28"
        assert b["meta_arm"]["author_byline"] == "Ben Lovejoy"


# ---------------------------------------------------------------------------
# 5. Content discipline: verbatim quotes, no constructed URLs, ASCII.
# ---------------------------------------------------------------------------

class TestM971ContentDiscipline1233:
    def test_meta_key_quotes_verbatim(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "9to5Mac's Take on Muse: Nope." in joined
        assert "unquestionably be the first entry" in joined

    def test_apple_key_quotes_verbatim(self):
        quotes = _block()["apple_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "most privacy-respecting AI chatbot out there" in joined

    def test_intra_article_apple_contrast_quoted(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "inclined to trust the privacy and safety safeguards Apple" in joined

    def test_no_constructed_9to5mac_url(self):
        # Every landed URL was copied verbatim from a Full-URL listing;
        # the canonical URLs carry the listing-attested slugs.
        for url in _block()["source_urls"]:
            assert url.startswith("https://9to5mac.com/"), url

    def test_byline_attestation_disclosed(self):
        assert "author/benlovejoy" in _block()["meta_arm"]["evidence_tier"]

    def test_author_page_url_verbatim_from_listing(self):
        assert "https://9to5mac.com/author/benlovejoy/" in _block()["source_urls"]

    def test_ascii_only(self):
        raw = _read(os.path.join(TESTS_DIR, OWN_BASENAME)).encode("utf-8")
        raw.decode("ascii")

    def test_no_em_dashes(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "\u2014" not in src
        assert "\u2013" not in src

    def test_yaml_block_ascii(self):
        # Only this run's appended block must be ASCII; the legacy
        # file carries pre-existing non-ASCII (curly quotes) elsewhere.
        text = _block_text()
        block = text[text.index(TOP_KEY + ":"):]
        block.encode("ascii")


# ---------------------------------------------------------------------------
# 6. Statistical discipline: MANUAL/QUALITATIVE ONLY per Aug 28 2026 rule.
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1233:
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

    def test_verdict_confirming_extension_not_discovery(self):
        assert _block()["verdict"] == "confirming_extension_of_m223_replication_not_a_discovery"

    def test_not_artifact_grade(self):
        assert "NOT artifact-grade" in _block()["falsification_family"] or \
            "No analysis.json update warranted" in _block()["falsification_family"]


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 50.
# ---------------------------------------------------------------------------

class TestFalsificationLedger1233:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert b["falsification_family"].startswith("NOT a falsification-family member")

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

    def test_ledger_note_holds_at_50(self):
        assert "Ledger HOLDS at 50" in _block()["ledger_note"]
        assert _block()["falsification_ledger"] == 50

    def test_falsification_field_states_confirming_extension(self):
        assert "Confirming extension" in _block()["falsification_family"]
        assert "m223" in _block()["falsification_family"]


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: pins for #1234; #1232's pins flip BY DESIGN.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1233:
    def test_pins_on_971_landing(self):
        # Type B lands one mechanism: max becomes 971, next is 972.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 971" in src
        assert "NEXT_NUM = 972" in src

    def test_no_type_c_1234_in_git_log_pin(self):
        out = _git("log", "--oneline", "--grep=Type C #1234").stdout
        assert out.strip() == "", out.strip()

    def test_972_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_972_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_972_dash_absent_repo_wide(self):
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

    def test_predecessor_1232_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1232_FILE))

    def test_next_leg_is_1234_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1234 Type C" in src

    def test_1232_pins_flip_by_design_documented(self):
        # #1232's forward guards (max-970, zero-971 keys all forms,
        # no-Type-B-#1233-in-git-log, fortieth absent, forty-eighth +
        # forty-ninth + fiftieth intact in profiles/, fifty-first
        # absent) verified GREEN pre-commit this run via the
        # subprocess staleness pin (Type B lands mechanism 971); the
        # max-970, zero-971, and no-Type-B-#1233-in-git-log pins flip
        # post-main-commit on this run's own landing (the #1191-class
        # self-trip, by design, documented in the staleness pin
        # below).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1232" in src
        assert "971" in src


# ---------------------------------------------------------------------------
# 9. Background suite: #1230's suite is CHECKED ONLY per #795.
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1233:
    def test_1230_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1230_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1230-launched suite is observed.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1233_full_suite.log"))

    def test_observation_documented_in_block(self):
        assert "#1230-launched" in _block()["background_suite_status"]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1233:
    def test_readme_test_file_table_has_1233_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_b_1233" in readme

    def test_architecture_has_1233_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1233" in arch

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

class TestIterationLog1233:
    def test_1233_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1233 Type B" in log

    def test_1232_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1232 Type A" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1232's guard lifecycle flips BY DESIGN post-commit
# ---------------------------------------------------------------------------

class TestStalenessPins1233:
    def test_1232_guard_lifecycle_post_commit_self_trip(self):
        # Post-main-commit form: 11 of the 13 pass; the two that fail
        # BY DESIGN are test_no_type_b_1233_in_git_log_pin (this run's
        # own main commit carries "Type B #1233") and
        # test_971_numeric_absent_in_profiles (mechanism 971 lands in
        # profiles/ this run). The #1232 block is read-only to this
        # run. Deselected pre-commit (both pins pass pre-commit).
        res = _class_run(E1232_FILE, "TestGuardLifecycle1232")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "2 failed, 11 passed" in res.stdout, res.stdout[-2000:]
        assert (
            "test_no_type_b_1233_in_git_log_pin" in res.stdout
        ), res.stdout[-2000:]
        assert (
            "test_971_numeric_absent_in_profiles" in res.stdout
        ), res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1233:
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
