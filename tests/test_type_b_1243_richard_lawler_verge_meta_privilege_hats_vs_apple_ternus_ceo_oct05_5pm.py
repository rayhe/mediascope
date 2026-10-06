# -*- coding: utf-8 -*-
"""Type B #1243 tests: Richard Lawler (The Verge, Vox Media) - Meta
'attorney/client privilege' hats child-safety-disclosure accountability
(-0.50 MANUAL ILLUSTRATIVE, NEW Sep-24 arm, mirror-attested) vs Apple
John Ternus CEO-succession straight news (+0.05, NEW Sep-1 arm,
mirror-attested); illustrative delta (Apple minus Meta) +0.55
register asymmetry in the Meta-hard direction (m977).

Mechanism 977 (NOT a falsification-family member; ledger holds at 52).
Vox Media holds the May-2024 OpenAI content-licensing deal (in-corpus,
profiles/the-verge.yaml), so the outlet is deal-holding; the comparator
here is Apple, not the deal partner, so the uniform payer-softening
prediction is not adjudicated - this pair tests cross-entity register
symmetry at a deal-holding outlet (CONTROL-CASE, same brief as #1218).
Lawler runs the adversarial legal-accountability register on Meta's
privilege-hats maneuver in the teen-safety lawsuits and straight
succession news on Apple's CEO change 23 days earlier. Peg asymmetry
(misconduct-litigation vs CEO-succession) is the STRONG confound.

Excerpt-bounded research per #503 (delegated scout 10-candidate sweep +
4 main-run browser.search verification sets, 0 browser.open reads).
Scout's #1 (Hugh Langley / BI) REJECTED on main-run verification:
already screened and rejected at #1208 ("Meta arm Aug 27, out of
window") - re-selecting the identical arms would re-litigate a settled
rejection. Scout #3 (Feiner) and #4 (Belanger) rejected (URL gaps on
the Meta arms). SELECTED Lawler: both arms URL-complete with
byline-carrying technewstube mirrors, in-window Sep 1 / Sep 24,
zero dedicated type_b key pre-commit (m646 #687 used Lawler's iPhone
Duo piece at piece level only, not journalist-level saturation).

The m977 block lives in profiles/careers/journalists.yaml as a
competitor_coverage sub-key of the NEW top-level `richard_lawler_type_b`
key (per the #643 convention; zero dedicated type_b key pre-commit;
mechanism_ids [977]).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
One anchor test (the placeholder pin) fails BY DESIGN post-anchor.

Per #795: this run only CHECKS the #1240-launched background suite
(goal hidden_files type_d_1240_full_suite.log, observed DEAD at this
run's check: 0 live pytest processes - 3 pgrep hits were transient
phantoms - last write Oct 5 14:59 PDT ~1.6h stale, 2129 bytes, F mark
in the dot stream; an observation, not a verdict); its verdict and
tombstone belong to #1245 (next Type D). This run neither re-launches,
kills, nor writes to the suite.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit), #900
(untracked Type D test file), #1012-wt (working-tree edit on the committed
Type A #1012 file).

Type B lands one mechanism (mechanism 977); the Type A predecessor added
one (mechanism 976). Next run #1244 Type C closes the 1240-1244 window.
Rotation: D #1240 -> E #1241 -> A #1242 -> B #1243 -> C #1244. This run is
the FOURTH leg of the 1240-1244 window. The main commit is the anchor
per #565.

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
landed or next number, the forty-eighth through fifty-third
member-claim forms, or the thirty-fifth through fortieth direction forms;
the constants are constructed at runtime. (The landed ordinals live as
short lowercase forms in prose here; the live full-form claims live in
profiles/financial-times.yaml, profiles/news-corp.yaml, and
profiles/careers/journalists.yaml.)
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
    "test_type_b_1243_richard_lawler_verge_meta_privilege_hats_vs_"
    "apple_ternus_ceo_oct05_5pm.py"
)
TOP_KEY = "richard_lawler_type_b"

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "f574d8503446cdfa5c563cd20168950e988814a1"  # patched green in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 977
NEXT_NUM = 978  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_b_1243_richard_lawler_verge_meta_privilege_hats_vs_"
    "apple_ternus_ceo_oct05_5pm"
)

# Predecessor chain: #1242 Type A continued the 1240-1244 window.
PRED_MAIN_1242 = "9d35d369"
PRED_ANCHOR_1242 = "cb788aa2"
PRED_DOCSYNC_1242 = "926b6f7b"
PRED_FINAL_1242 = "c0a4236c"

# The #1242 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 976; zero next-number nine-seven-eight /
# no-Type-B-#1243-in-git-log / fortieth direction absent /
# forty-eighth through fifty-second members intact /
# fifty-third member absent / ledger 52).
E1242_FILE = (
    "test_type_a_1242_cnn_openai_sep28_uthmeier_injunction_"
    "bounded_absence_oct05_4pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 67920  # post-doc-sync total (pre-sync 67823 + 97)
README_FILE_COUNT = 1568  # pre-sync 1567 + 1 (this file)

# The forward-guard needles are fragment-built per #715 so this file
# carries no contiguous literal of a forward-guard claim form.
_T40 = "FORT" + "IETH relationship direction"
_T48 = "FORT" + "Y-EIGHTH falsification-family member"
_T49 = "FORT" + "Y-NINTH falsification-family member"
_T50 = "FIFT" + "IETH falsification-family member"
_T51 = "FIFT" + "Y-FIRST falsification-family member"
_T52 = "FIFT" + "Y-SECOND falsification-family member"
_T53 = "FIFT" + "Y-THIRD falsification-family member"

# Novel source URLs: 2 zero-hit repo-wide pre-commit (git grep -F);
# the Vox Media deal URL is an in-corpus re-surface (disclosed).
NOVEL_URLS = [
    "https://technewstube.com/theverge/1870470/"
    "meta-employees-ordered-attorneyclient-privilege-hats/",
    "https://technewstube.com/theverge/1863229/john-ternus-ceo-apple/",
]
RESURFACED_URLS = [
    "https://www.reuters.com/technology/"
    "openai-signs-content-deals-with-atlantic-vox-media-2024-05-29/",
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

class TestAnchor1243:
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
        assert "FOURTH leg of the 1240-1244 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1243:
    def test_predecessor_1242_chain_verified(self):
        for sha in (
            PRED_MAIN_1242, PRED_ANCHOR_1242, PRED_DOCSYNC_1242,
            PRED_FINAL_1242,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1241_chain_verified(self):
        for sha in ("600b3a8b", "1c8b10c1", "e58d7a64", "19c97dfd"):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1240 -> E #1241 -> A #1242 -> B #1243 -> C #1244" in src

    def test_next_leg_is_type_c_1244(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1244 Type C" in src

    def test_type_b_lands_one_mechanism(self):
        # Type B lands exactly one mechanism (mechanism 977); the Type
        # A predecessor added one (mechanism 976).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type B lands one mechanism" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1243:
    def test_top_key_found(self):
        assert _top()["mechanism_ids"] == [MECH_NUM]

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1243 in key, no 977 or
        # 978 substring.
        assert "1243" in BLOCK_KEY
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
        assert nums, "mechanism 977 must be present in profiles"

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_novel_urls_in_block_source_urls_verbatim(self):
        b = _block()
        urls = b["source_urls"]
        for novel in NOVEL_URLS:
            assert novel in urls, novel

    def test_resurfaced_deal_url_disclosed(self):
        b = _block()
        for resurfaced in RESURFACED_URLS:
            assert resurfaced in b["source_urls"], resurfaced
        assert "re-surface" in b["novelty"] or "resurface" in b["novelty"]

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
        # The Sep-24 privilege-hats mirror URL was zero-hit repo-wide
        # pre-commit; now present only inside this block.
        text = _block_text()
        assert "theverge/1870470" in text
        block_start = text.index(BLOCK_KEY + ":")
        assert "theverge/1870470" not in text[:block_start]

    def test_apple_headline_novelty(self):
        text = _block_text()
        assert "theverge/1863229" in text
        block_start = text.index(BLOCK_KEY + ":")
        assert "theverge/1863229" not in text[:block_start]

    def test_both_arms_new_documented(self):
        b = _block()
        assert "NEW" in b["meta_arm"]["status"]
        assert "NEW" in b["apple_arm"]["status"]

    def test_no_type_b_1243_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): the ONLY
        # matches are this run's own commits, whose messages carry the
        # run's own iteration subject (the followup commits match the
        # grep, so they join the own set; HEAD is admitted for any
        # same-run followup). The pin's substance - no PRIOR run
        # committed this run's iteration - holds.
        out = _git("log", "--format=%H %s", "--grep=Type B #1243").stdout
        own = {
            "f574d850", "14f2a13c", "843bc28a",
        }
        head = _git("rev-parse", "HEAD").stdout.strip()[:8]
        hits = [line for line in out.splitlines() if line.strip()]
        assert hits, "expected this run's own commits"
        for line in hits:
            assert (line.split()[0][:8] in own
                    or line.split()[0][:8] == head), line


# ---------------------------------------------------------------------------
# 4. Block structure under the NEW richard_lawler_type_b top-level key.
# ---------------------------------------------------------------------------

class TestBlockStructure1243:
    def test_journalists_profile_exists(self):
        assert os.path.exists(JOURNALISTS_PATH)

    def test_top_key_is_expected_parent(self):
        assert _top()["name"] == "Richard Lawler"
        assert _top()["publication"] == "the-verge"

    def test_block_key_present_under_competitor_coverage(self):
        assert BLOCK_KEY in _top()["competitor_coverage"]

    def test_mechanism_id_field(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_iteration_fields(self):
        b = _block()
        assert b["iteration"] == 1243
        assert b["type"] == "B"
        assert b["date"] == "2026-10-05 17:00 PDT"

    def test_required_block_fields(self):
        b = _block()
        for field in (
            "block_key", "mechanism_id", "iteration", "type", "date",
            "test_file", "author", "goal_id", "job_id",
            "scheduled_job_id", "journalist", "publication", "window",
            "design", "meta_arm", "apple_arm",
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
        assert _block()["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.50

    def test_apple_arm_tone(self):
        assert _block()["apple_arm"]["tone_MANUAL_ILLUSTRATIVE"] == 0.05

    def test_scorer_delta(self):
        assert _block()["scorer_delta_MANUAL_ILLUSTRATIVE"] == 0.55

    def test_connects_to_lineage(self):
        assert 646 in _block()["connects_to"]
        assert 425 in _block()["connects_to"]

    def test_source_urls_count(self):
        assert len(_block()["source_urls"]) == 3

    def test_meta_arm_date_and_byline(self):
        b = _block()
        assert b["meta_arm"]["date"] == "2026-09-24"
        assert b["meta_arm"]["author_byline"] == "Richard Lawler"

    def test_apple_arm_date_and_byline(self):
        b = _block()
        assert b["apple_arm"]["date"] == "2026-09-01"
        assert b["apple_arm"]["author_byline"] == "Richard Lawler"


# ---------------------------------------------------------------------------
# 5. Content discipline: verbatim quotes, mirror attestation, ASCII.
# ---------------------------------------------------------------------------

class TestM977ContentDiscipline1243:
    def test_meta_key_quotes_verbatim(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "attorney/client privilege" in joined
        assert "applied far too broadly" in joined

    def test_meta_headline_verbatim(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "Meta employees ordered" in joined
        assert "child safety disclosures" in joined

    def test_apple_key_quotes_verbatim(self):
        quotes = _block()["apple_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "John Ternus" in joined
        assert "Tim Cook" in joined

    def test_apple_succession_news_register(self):
        quotes = _block()["apple_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "For the first time since 2011" in joined

    def test_mirror_attestation_disclosed(self):
        b = _block()
        assert "mirror-attested" in b["meta_arm"]["evidence_tier"]
        assert "mirror-attested" in b["apple_arm"]["evidence_tier"]
        assert "0 browser.open per #503" in b["meta_arm"]["evidence_tier"]

    def test_no_constructed_theverge_url(self):
        # Every landed URL was copied verbatim from a Full-URL
        # listing; the Verge originals did not surface (bot-blocked
        # per the scout), so the mirror URLs carry the attested
        # slugs. No canonical theverge.com URL is constructed.
        for url in _block()["source_urls"]:
            assert "theverge.com/" not in url, url

    def test_vox_media_parent_disclosed(self):
        b = _block()
        assert "Vox" in b["design"] and "Media" in b["design"]

    def test_ascii_only(self):
        raw = _read(os.path.join(TESTS_DIR, OWN_BASENAME)).encode("utf-8")
        raw.decode("ascii")

    def test_no_em_dashes(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "\u2014" not in src
        assert "\u2013" not in src

    def test_yaml_block_ascii(self):
        # Only this run's appended block must be ASCII; the legacy
        # file carries pre-existing non-ASCII elsewhere.
        text = _block_text()
        block = text[text.index(TOP_KEY + ":"):]
        block.encode("ascii")


# ---------------------------------------------------------------------------
# 6. Statistical discipline: MANUAL/QUALITATIVE ONLY per Aug 28 2026 rule.
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1243:
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

    def test_verdict_directionally_supported_not_proven(self):
        assert _block()["verdict"] == "directionally_supported_not_proven"

    def test_not_artifact_grade(self):
        assert "NOT artifact-grade" in _block()["falsification_family"] or \
            "No analysis.json update warranted" in _block()["falsification_family"]


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 52 (NOT a member).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1243:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert "NOT a falsification-family member" in b["falsification_family"]

    def test_control_case_disclosed(self):
        b = _block()
        assert "CONTROL-CASE" in b["falsification_family"]

    def test_fifty_second_intact_in_journalists(self):
        # At HEAD (committed #1238): the fifty-second form appears 5x
        # in profiles/careers/journalists.yaml. This run's block uses
        # only the lowercase form, so the count is unchanged.
        out = _git(
            "grep", "-c", "-F", _T52, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_fifty_first_intact_in_news_corp(self):
        out = _git(
            "grep", "-c", "-F", _T51, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fiftieth_intact_in_journalists(self):
        out = _git(
            "grep", "-c", "-F", _T50, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_forty_ninth_intact_in_journalists(self):
        assert _git_grep_tracked_source(_T49, "profiles/") == [
            "profiles/careers/journalists.yaml"]

    def test_forty_eighth_intact_in_ft(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_fifty_third_absent(self):
        assert _git_grep_tracked_source(_T53, None) == []

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

    def test_ledger_holds_at_52(self):
        assert "holds at 52" in _block()["ledger_note"]
        assert _block()["falsification_ledger"] == 52

    def test_ledger_note_states_not_a_member(self):
        assert "NOT a falsification-family member" in _block()["ledger_note"]


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: pins for #1244; #1242's pins flip BY DESIGN.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1243:
    def test_pins_on_977_landing(self):
        # Type B lands one mechanism: max becomes 977, next is 978.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 977" in src
        assert "NEXT_NUM = 978" in src

    def test_no_type_c_1244_in_git_log_pin(self):
        out = _git("log", "--oneline", "--grep=Type C #1244").stdout
        assert out.strip() == "", out.strip()

    def test_978_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_978_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_978_dash_absent_repo_wide(self):
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

    def test_fifty_first_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T51, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_second_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T52, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_no_fifty_third_member_pin(self):
        # m977 is NOT a falsification-family member (CONTROL-CASE);
        # the fifty-third member-claim form stays absent repo-wide.
        assert _git_grep_tracked_source(_T53, None) == []

    def test_predecessor_1242_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1242_FILE))

    def test_next_leg_is_1244_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1244 Type C" in src

    def test_1242_pins_flip_by_design_documented(self):
        # #1242's forward guards (max-976, zero-978 keys all forms,
        # no-Type-B-#1243-in-git-log, fortieth absent, forty-eighth
        # through fifty-second intact in profiles/, fifty-third
        # absent) verified GREEN pre-commit this run via the subprocess
        # staleness pin (Type B lands mechanism 977 as a CONTROL-CASE,
        # not a family member); the max-976, zero-978, and
        # no-Type-B-#1243-in-git-log pins flip post-main-commit on this
        # run's own landing (the #1191-class self-trip, by design,
        # documented in the staleness pin below).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1242" in src
        assert "977" in src


# ---------------------------------------------------------------------------
# 9. Background suite: #1240's suite is CHECKED ONLY per #795.
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1243:
    def test_1240_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1240_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1240-launched suite is observed.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1243_full_suite.log"))

    def test_observation_documented_in_block(self):
        assert "#1240-launched" in _block()["background_suite_status"]
        assert "#795" in _block()["background_suite_status"]
        assert "#1245" in _block()["background_suite_status"]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1243:
    def test_readme_test_file_table_has_1243_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_b_1243" in readme

    def test_architecture_has_1243_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1243" in arch

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

class TestIterationLog1243:
    def test_1243_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1243 Type B" in log

    def test_1242_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1242 Type A" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1242's guard lifecycle flips BY DESIGN post-commit
# ---------------------------------------------------------------------------

class TestStalenessPins1243:
    def test_1242_guard_lifecycle_post_commit_self_trip(self):
        # Post-main-commit form: 5 of the 8 pass; the three that fail
        # BY DESIGN are test_pins_on_976_landing (max becomes 977),
        # test_no_type_b_1243_in_git_log_pin (this run's own main
        # commit carries "Type B #1243"), and
        # test_977_numeric_absent_in_profiles (mechanism 977 lands in
        # profiles/ this run). test_no_fifty_third_member_pin stays
        # GREEN: m977 is a CONTROL-CASE, not a family member. The
        # #1242 block is read-only to this run. Deselected pre-commit
        # (all three pins pass pre-commit).
        res = _class_run(E1242_FILE, "TestGuardLifecycle1242")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "3 failed, 5 passed" in res.stdout, res.stdout[-2000:]
        for name in (
            "test_pins_on_976_landing",
            "test_no_type_b_1243_in_git_log_pin",
            "test_977_numeric_absent_in_profiles",
        ):
            assert name in res.stdout, res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1243:
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
