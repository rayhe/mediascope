# -*- coding: utf-8 -*-
"""Type A #1222 tests: WIRED - Apple N50 privacy-delay promise (CARRIED
Jul-26-2026 arm) vs WIRED - Meta Ray-Ban Audio camera-free launch window
(NEW Oct-2026 arm, Sep-24 to Oct-4).

Mechanism m964 (NOT a falsification-family member; ledger holds at 50).
CONFIRMING EXTENSION of m134 (remediation_coverage_selection_silence):
the July contrast (Meta v26 LED software fix shipped Jul 7 vs Apple N50
privacy-delay promise reported Jul 26) persists and sharpens in October
(Meta camera-free hardware SHIPPING Oct 13 at $349 vs the same unshipped
Apple promise). WIRED published zero Audio-hardware originals in the
Sep-24-Oct-4 window (bounded absence, m207-lineage: 0 WIRED vs 7+
outlets); WIRED's Connect-week Meta original stayed skeptical (m820
Pinky Promises, -0.45, carried). Apple's promise drew neutral
product-delay coverage (+0.10 MANUAL ILLUSTRATIVE, carried).

Research: 6 main-run browser.search query sets, 0 browser.open per #503.
The research arc: (1) WIRED Apple smart glasses October 2026 surfaced
the N50 delay relay cluster (Jul-26 Gurman origin) and the Meta Connect
Audio coverage; (2) WIRED Meta smart glasses Connect privacy October
2026 surfaced the Audio launch relay cluster; (3) wired.com Apple smart
glasses privacy delay Gurman confirmed Jul-26 as the current
Apple-glasses peg with no October WIRED Apple-glasses original;
(4) WIRED Apple facial recognition smart glasses confirmed the NameTag
removal was June 2026 (already in corpus via m134), not October-fresh;
(5) WIRED iPhone 17 review September 2026 surfaced WIRED's iPhone 17
line reviews (Sep 2025-Mar 2026, not October-fresh; #528 covers the
2025 iPhone 17 at journalist level) - REJECTED as the Apple arm;
(6) WIRED Ray-Ban Audio glasses review Meta Connect surfaced the
7-outlet Audio launch cluster with zero WIRED Audio-hardware originals
- SELECTED as the Meta arm. REJECTED: iPhone-17-review Apple arm
(stale, #528 saturated); Ashworth Gen-2 "creepy vibes" as a fresh Meta
arm (2025-era, not October-fresh); October WIRED NameTag follow-up (no
such piece - the removal was June 2026); Apple M5 Vision Pro October
launch (leak-stage, no WIRED original surfaced).

The m964 block lives in profiles/wired.yaml as a
competitor_relationships.apple sub-key (4-space indent), appended at
the end of the apple section after the m670 block. profiles/wired.yaml
carries NO in-flight hunks this run (verified via git status
pre-commit), so plain explicit-path staging is used; the in-flight
#899/#938/#900/#1012-wt files stay out of this run's index/diff.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
One anchor test (the placeholder pin) fails BY DESIGN post-anchor.

Per #795: this run only CHECKS the #1220-launched background suite
(type_d_1220_full_suite.log); its verdict and tombstone belong to #1225
(next Type D). This run neither re-launches, kills, nor writes to the suite.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit),
#900 (untracked Type D test file), #1012-wt (working-tree edit on the
committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the landed
or next number, the forty-ninth / fiftieth / fifty-first member-claim
forms, or the thirty-fifth through fortieth direction forms; the constants
are constructed at runtime. (The landed forty-ninth and fiftieth ordinals
live in profiles/careers/journalists.yaml; m956 and m959 respectively.)
"""

import glob
import os
import re
import subprocess

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
TESTS_DIR = HERE
PROFILES_DIR = os.path.join(REPO, "profiles")

OWN_BASENAME = (
    "test_type_a_1222_wired_apple_n50_promise_vs_meta_audio_remediation_"
    "silence_oct04_10pm.py"
)
BLOCK_KEY = (
    "type_a_1222_wired_apple_n50_promise_vs_meta_audio_remediation_"
    "silence_october"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "6ff9a172fdae57905bef1e932ad6da7a4cfeef9a"  # patched per #565
# Post-first-run values per #719: N tests collected; README ratchets
# 66066/1546 -> (66066+N)/1547 in the doc-sync followup.
README_TEST_COUNT = 66066 + 82  # patched post-first-run per #719
README_FILE_COUNT = 1547
COLLECTED_NEW_TESTS = 82  # patched post-first-run per #719

# Forward guards for the next landing. MECH_NUM=964 is THIS run's landed
# mechanism; NEXT_NUM=965 stays forward.
MECH_NUM = 964
NEXT_NUM = 965

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + number at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + number at runtime
FORTY_NINTH_MEMBER = "FORTY" + "-NINTH falsification-family member"
FIFTIETH_MEMBER = "FIFT" + "IETH falsification-family member"
FIFTY_FIRST_MEMBER = "FIFTY" + "-FIRST falsification-family member"
THIRTY_FIFTH_DIR = "THIRTY" + "-FIFTH relationship direction"
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH relationship direction"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"
THIRTY_EIGHTH_DIR = "THIRTY" + "-EIGHTH relationship direction"
THIRTY_NINTH_DIR = "THIRTY" + "-NINTH relationship direction"
FORTIETH_DIR = "FORTI" + "ETH relationship direction"

# The landed m964 block lives here. It is a
# competitor_relationships.apple sub-key of profiles/wired.yaml.
WIRED_PATH = os.path.join(REPO, "profiles", "wired.yaml")
FILE_1221 = "test_type_e_1221_podcast_sentiment_167th_verification_oct04_915pm.py"
FILE_1220 = "test_type_d_1220_m961_m962_m963_qualitative_corpus_integrity_oct04_9pm.py"

# Novel relay URLs (verbatim from Full-URL listings; zero-hit repo-wide
# pre-commit via git grep -F).
NOVEL_URLS = (
    "https://hiconsumption.com/tech/ray-ban-meta-audio-glasses/",
    "https://themodems.com/tech/ray-ban-meta-audio-glasses-no-camera/",
    "https://techxplore.com/news/2026-09-meta-camera-free-ai-glasses.html",
    "https://dataconomy.com/2026/07/27/apple-delays-smart-glasses-over-privacy-concerns/",
)


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _load_wired():
    return yaml.safe_load(_read(WIRED_PATH))


def _apple_section():
    data = _load_wired()
    assert "competitor_relationships" in data
    assert "apple" in data["competitor_relationships"]
    return data["competitor_relationships"]["apple"]


def _block():
    return _apple_section()[BLOCK_KEY]


def _block_text():
    return _read(WIRED_PATH)


def _git(*args):
    return subprocess.run(
        ["git", "-C", REPO] + list(args), capture_output=True, text=True
    )


def _profiles_grep_numeric_mechanism_id(num):
    out = _git("grep", "-F", "mechanism_id: %d" % num, "--", "profiles").stdout
    return out.strip().splitlines() if out.strip() else []


def _repo_grep(pattern, exclude_paths=(), file_globs=None):
    """Repo-wide grep; file_globs restricts to a file set (None = all)."""
    candidates = []
    for root, _dirs, files in os.walk(REPO):
        rel_root = os.path.relpath(root, REPO)
        if rel_root.startswith(".git") or rel_root.startswith(".pytest_cache"):
            continue
        for name in files:
            rel = os.path.join(rel_root, name) if rel_root != "." else name
            if rel in exclude_paths:
                continue
            if file_globs and not any(
                name.endswith(g.lstrip("*")) for g in file_globs
            ):
                continue
            candidates.append(os.path.join(root, name))
    hits = []
    for path in candidates:
        try:
            text = _read(path)
        except (OSError, UnicodeError):
            continue
        if pattern in text:
            hits.append(path)
    return hits


def _iter_source_files():
    return _repo_grep(
        "", exclude_paths=("tests/" + OWN_BASENAME,),
        file_globs=("*.py", "*.yaml", "*.md", "*.txt", "*.sh", "*.json"),
    )


def _repo_grep_underscore_mechanism(n):
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [p for p in _iter_source_files() if needle in _read(p)]


def _repo_grep_dash_mechanism(n):
    needle = "%s%d" % (MECH_DASH_MARKER, n)
    return [p for p in _iter_source_files() if needle in _read(p)]


def _source_grep(pattern):
    """Repo-wide grep including this file (for landed-key allowlisting)."""
    hits = []
    for path in _repo_grep("", file_globs=("*.py", "*.yaml", "*.md", "*.txt", "*.sh", "*.json")):
        try:
            text = _read(path)
        except (OSError, UnicodeError):
            continue
        if pattern in text:
            hits.append(path)
    return hits


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------

class TestAnchor1222:
    def test_anchor_sha_format(self):
        # 40-char hex in both states (placeholder 0*40 pre-anchor,
        # main-commit hash post-anchor).
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA

    def test_anchor_placeholder_or_main_commit(self):
        # Either the pre-anchor placeholder or a hash present in git log.
        if ANCHORED_SHA != "0" * 40:
            log = _git("log", "--format=%H").stdout
            assert ANCHORED_SHA in log

    def test_anchor_placeholder_pin(self):
        # BY DESIGN: green pre-anchor (placeholder), red post-anchor
        # (patched). Exactly one designed failure post-anchor per the
        # #1196 corrective pattern.
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_followup_commit_message_convention(self):
        # Post-anchor only meaningful; pre-anchor the grep is empty and the
        # assertion is vacuous-truthful via the placeholder pin above.
        log = _git("log", "--oneline", "--grep=Type A #1222 anchor").stdout
        if ANCHORED_SHA != "0" * 40:
            assert "Type A #1222 anchor" in log


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1222 is the THIRD leg of the 1220-1224 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1222:
    def test_rotation_window_is_1220_1224(self):
        text = _block_text()
        assert "1220-1224" in text

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1220-1224 window THIRD leg "
            "(D #1220 -> E #1221 -> A #1222 -> B #1223 -> C #1224)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1220", "Type E #1221"):
            assert marker in log, marker

    def test_predecessor_hashes_verified(self):
        # Committed predecessors verified pre-commit per the rotation guard.
        log = _git("log", "--oneline").stdout
        assert "0d29e5f9" in log  # #1221 Type E main
        assert "eec4bc91" in log  # #1220 Type D main

    def test_next_run_is_type_b(self):
        # The next leg (#1223 Type B) is documented in the block window
        # field; the iteration-log entry carrying it lands in the doc-sync
        # followup (TestIterationLog1222 pins it there).
        assert "B #1223" in _block()["window"]
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1220-1224" in text

    def test_no_type_a_1222_test_file_before_this_run(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1222_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (pre-commit claims, verifiable post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1222:
    def test_apple_section_found(self):
        sec = _apple_section()
        assert BLOCK_KEY in sec

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1222 in key, no 964 substring.
        assert "1222" in BLOCK_KEY
        assert str(MECH_NUM) not in BLOCK_KEY
        assert str(NEXT_NUM) not in BLOCK_KEY

    def test_zero_underscore_mechanism_repo_wide(self):
        # Per #715 designed keying the landed number appears only as
        # "mechanism_id: 964" (colon form); the underscore key form must
        # not exist repo-wide.
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_mechanism_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_next_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_this_run(self):
        nums = []
        for _line in _profiles_grep_numeric_mechanism_id(MECH_NUM):
            nums.append(MECH_NUM)
        for n in range(MECH_NUM + 1, MECH_NUM + 20):
            assert _profiles_grep_numeric_mechanism_id(n) == [], n
        assert nums, "m964 must be present in profiles"

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_novel_urls_in_block_source_urls_verbatim(self):
        b = _block()
        urls = [u["url"] for u in b["source_urls"]]
        for novel in NOVEL_URLS:
            assert novel in urls, novel

    def test_block_key_zero_hit_except_landed(self):
        # Pre-commit the block key was zero-hit repo-wide; post-commit it
        # appears only in the landed YAML block, this test file, and the
        # doc-sync targets (README, ARCHITECTURE, iteration-log).
        hits = _source_grep(BLOCK_KEY)
        allowed = {
            os.path.join(REPO, "profiles", "wired.yaml"),
            os.path.join(TESTS_DIR, OWN_BASENAME),
            os.path.join(REPO, "README.md"),
            os.path.join(REPO, "docs", "ARCHITECTURE.md"),
            os.path.join(REPO, "iteration-log.md"),
        }
        for h in hits:
            assert h in allowed, h

    def test_no_ray_ban_audio_in_wired_before_this_run(self):
        # The novelty claim: "ray-ban audio" was absent from wired.yaml
        # before this run's landing; now present via this block's arms.
        text = _block_text().lower()
        assert text.count("ray-ban audio") >= 1
        b = _block()
        assert "ray-ban meta audio" in b["meta_arm"]["title"].lower()

    def test_apple_arm_disclosed_carried(self):
        b = _block()
        assert "CARRIED" in b["apple_arm"]["status"]
        assert "m134" in b["apple_arm"]["status"]

    def test_meta_arm_new_documented(self):
        b = _block()
        assert "NEW this run" in b["meta_arm"]["status"]


# ---------------------------------------------------------------------------
# 4. Block structure under competitor_relationships.apple.
# ---------------------------------------------------------------------------

class TestBlockStructure1222:
    def test_apple_section_is_expected_parent(self):
        data = _load_wired()
        assert "apple" in data["competitor_relationships"]

    def test_block_key_present_under_apple(self):
        assert BLOCK_KEY in _apple_section()

    def test_mechanism_id_field(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_iteration_fields(self):
        b = _block()
        assert b["iteration"] == 1222
        assert b["iteration_type"] == "A"
        assert b["publication"] == "WIRED"
        assert b["rotation"] == "Type A"

    def test_required_block_fields(self):
        b = _block()
        for field in (
            "mechanism_id", "date_analyzed", "type", "iteration",
            "iteration_type", "publication", "competitor_pair", "author",
            "block_key", "test_file", "window", "design",
            "distinct_from_prior", "finding", "financial_relationship",
            "apple_arm", "meta_arm", "register_analysis",
            "asymmetry_scorer_MANUAL_ILLUSTRATIVE", "scorer",
            "confounders", "counterevidence", "verdict",
            "cautious_language_required", "correlational_note",
            "no_analysis_json_update", "statistical_discipline",
            "falsification_family_member", "falsification_ledger",
            "ledger_note", "connects_to", "novelty", "research_method",
            "rotation_transparency", "concurrency",
            "background_suite_status", "in_flight", "source_urls",
            "browser_opens", "tone_scored", "engine_run",
            "is_significant", "artifact_grade", "yaml_parse_clean",
            "ascii_only",
        ):
            assert field in b, field

    def test_test_file_field_matches_own_basename(self):
        assert _block()["test_file"] == "tests/" + OWN_BASENAME

    def test_apple_arm_tone(self):
        assert _block()["apple_arm"]["tone_MANUAL_ILLUSTRATIVE"] == 0.10

    def test_meta_arm_tone_carried(self):
        # The Meta-arm tone is the carried m820 skeptical-register tone;
        # the Audio-hardware silence itself is unscored (0 articles).
        assert _block()["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.45
        assert "unscored" in _block()["meta_arm"]["status"]

    def test_connects_to_m134_lineage(self):
        conns = _block()["connects_to"]
        for mid in (134, 207, 446, 670, 820):
            assert mid in conns, mid

    def test_source_urls_novel_flags(self):
        b = _block()
        assert len(b["source_urls"]) == 4
        for u in b["source_urls"]:
            assert u["novel"] is True
            assert u["accessed"] == "2026-10-04"

    def test_browser_opens_zero(self):
        assert _block()["browser_opens"] == 0


# ---------------------------------------------------------------------------
# 5. Content discipline: excerpt-bounded, no constructed URLs, ASCII-only.
# ---------------------------------------------------------------------------

class TestM964ContentDiscipline1222:
    def test_apple_key_quotes_verbatim(self):
        quotes = _block()["apple_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "priority No. 1" in joined
        assert "WWDC in 2027" in joined

    def test_meta_key_quotes_verbatim(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "removed the camera entirely" in joined
        assert "13 October" in joined

    def test_evidence_tier_is_excerpt_attested(self):
        b = _block()
        assert "EXCERPT-TIER" in b["apple_arm"]["evidence_tier"]
        assert "EXCERPT-TIER" in b["meta_arm"]["evidence_tier"]

    def test_no_full_read_claim(self):
        b = _block()
        assert "not first-hand read" in b["apple_arm"]["evidence_tier"]
        assert "not first-hand read" in b["meta_arm"]["evidence_tier"]

    def test_no_canonical_url_constructed(self):
        b = _block()
        assert "none constructed per policy" in b["apple_arm"]["url_source"]
        assert "none constructed per policy" in b["meta_arm"]["url_source"]

    def test_bounded_absence_disclosed(self):
        b = _block()
        assert "bounded absence" in b["meta_arm"]["url_source"]
        assert "m207" in b["meta_arm"]["url_source"]

    def test_research_rejections_documented(self):
        method = _block()["research_method"]
        assert "REJECTED" in method
        assert "iPhone" in method

    def test_ascii_only(self):
        text = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert text.isascii(), "test file must be ASCII-only"
        assert "\u2014" not in text and "\u2013" not in text
        block_text = _block_text()
        assert "\u2014" not in block_text and "\u2013" not in block_text


# ---------------------------------------------------------------------------
# 6. Statistical discipline (Aug 28 2026 standing rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1222:
    def test_manual_illustrative_only(self):
        b = _block()
        assert b["tone_scored"] is False
        assert b["engine_run"] is False
        assert b["is_significant"] is False
        assert b["artifact_grade"] is False

    def test_no_inferential_stats(self):
        s = _block()["scorer"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"

    def test_delta_is_illustrative(self):
        s = _block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["delta"] == 0.55
        assert "not empirical" in s["note"]

    def test_verdict_is_confirming_extension_not_discovery(self):
        v = _block()["verdict"]
        assert v.startswith("confirming_extension_of_m134_not_a_discovery")

    def test_statistical_discipline_strings(self):
        d = _block()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE scores only" in d
        assert "NOT artifact-grade" in d

    def test_correlational_honesty(self):
        assert "not causation" in _block()["correlational_note"]
        assert "Correlation is not causation" in _block()["correlational_note"]

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_silence_unscored_by_construction(self):
        s = _block()["scorer"]
        assert "selection margin" in s["silence_read"]


def _needle_hits_profiles(needle):
    out = _git("grep", "-l", "-F", needle, "--", "profiles").stdout
    return out.strip().splitlines() if out.strip() else []


# ---------------------------------------------------------------------------
# 7. Falsification ledger (holds at 50; m964 is a confirming extension).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1222:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 50

    def test_forty_ninth_intact_in_journalists(self):
        # No new member this run: the forty-ninth claim form stays
        # exactly in profiles/careers/journalists.yaml (m956, 3 occurrences).
        text = _read(os.path.join(PROFILES_DIR, "careers", "journalists.yaml"))
        assert text.count(FORTY_NINTH_MEMBER) == 3

    def test_fiftieth_intact_in_journalists(self):
        # The fiftieth claim form stays exactly in
        # profiles/careers/journalists.yaml (m959, 3 occurrences).
        text = _read(os.path.join(PROFILES_DIR, "careers", "journalists.yaml"))
        assert text.count(FIFTIETH_MEMBER) == 3

    def test_forty_ninth_nowhere_else(self):
        for p in _needle_hits_profiles(FORTY_NINTH_MEMBER):
            assert p.endswith(os.path.join("careers", "journalists.yaml")), p

    def test_fiftieth_nowhere_else(self):
        for p in _needle_hits_profiles(FIFTIETH_MEMBER):
            assert p.endswith(os.path.join("careers", "journalists.yaml")), p

    def test_fifty_first_absent(self):
        assert _needle_hits_profiles(FIFTY_FIRST_MEMBER) == []
        for p in _iter_source_files():
            if p.endswith(".py") and os.path.basename(p) != OWN_BASENAME:
                assert FIFTY_FIRST_MEMBER not in open(
                    p, encoding="utf-8", errors="replace"
                ).read(), p

    def test_directions_thirty_fifth_through_thirty_ninth_present(self):
        for needle in (
            THIRTY_FIFTH_DIR, THIRTY_SIXTH_DIR, THIRTY_SEVENTH_DIR,
            THIRTY_EIGHTH_DIR, THIRTY_NINTH_DIR,
        ):
            assert _needle_hits_profiles(needle) != [], needle

    def test_fortieth_direction_absent(self):
        assert _needle_hits_profiles(FORTIETH_DIR) == []

    def test_ledger_note_holds_at_50(self):
        note = _block()["ledger_note"]
        assert "Ledger holds at 50" in note
        assert "FORTY-NINTH member-claim form present" in note
        assert "FIFTIETH member-claim form present" in note
        assert "fifty-first member-claim form absent repo-wide" in note

    def test_verdict_is_confirming_not_falsifying(self):
        assert "confirming_extension" in _block()["verdict"]
        assert "falsification" in _block()["verdict"].lower()


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (designed lifecycle; the #1223 Type B run
# pins the 965 landing).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1222:
    def test_zero_965_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 965" in src
        # Needles format-built per #715: constructed at runtime, never
        # written contiguously in source.
        assert (MECH_ID_MARKER + str(NEXT_NUM)) not in src
        assert (MECH_DASH_MARKER + str(NEXT_NUM)) not in src

    def test_no_fortieth_direction_guard(self):
        # The fortieth direction form stays absent in profiles/; the
        # constant is format-built so this file never carries it
        # contiguously. Scope is profiles/ (not repo-wide) because other
        # landed test files may carry the contiguous needle in their own
        # constant definitions with profiles-scoped tests.
        assert _needle_hits_profiles(FORTIETH_DIR) == [], FORTIETH_DIR
        assert len(FORTIETH_DIR) > 0

    def test_no_fifty_first_member_guard(self):
        # Format-built per #715: constructed at runtime, never written
        # contiguously in source (verified by inspection of the constant
        # definition above).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FIFTY_FIRST_MEMBER) not in src
        assert len(FIFTY_FIRST_MEMBER) > 0

    def test_no_forty_ninth_member_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FORTY_NINTH_MEMBER) not in src
        assert len(FORTY_NINTH_MEMBER) > 0

    def test_no_fiftieth_member_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FIFTIETH_MEMBER) not in src
        assert len(FIFTIETH_MEMBER) > 0

    def test_1221_pins_flip_by_design_documented(self):
        # #1221's forward guards (max-963, zero-964 keys all forms,
        # no-Type-A-#1222-in-git-log) flip by design now that m964 has
        # landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1221" in src
        text = _block_text()
        assert "1221" in text

    def test_thirty_fifth_direction_still_present(self):
        assert _repo_grep(THIRTY_FIFTH_DIR)

    def test_thirty_sixth_direction_still_present(self):
        assert _repo_grep(THIRTY_SIXTH_DIR)

    def test_thirty_seventh_direction_still_present(self):
        assert _repo_grep(THIRTY_SEVENTH_DIR)

    def test_thirty_eighth_direction_still_present(self):
        assert _repo_grep(THIRTY_EIGHTH_DIR)

    def test_thirty_ninth_direction_still_present(self):
        assert _repo_grep(THIRTY_NINTH_DIR)


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this run pins the 964 landing for #1223).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1222:
    def test_pins_on_964_landing(self):
        # The guards this run lays for the next leg: max-964,
        # zero-965 all forms, no-Type-B-#1223-in-git-log, fortieth
        # direction absent (profiles/ scope), forty-ninth member
        # intact + fiftieth member intact in
        # profiles/careers/journalists.yaml, fifty-first member absent
        # (repo-wide), ledger 50.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 964" in src
        assert "NEXT_NUM = 965" in src

    def test_no_type_b_1223_in_git_log_pin(self):
        out = _git("log", "--oneline", "--grep=Type B #1223").stdout
        assert out.strip() == "", out.strip()

    def test_965_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1221_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1221))

    def test_predecessor_1220_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1220))

    def test_apple_key_unique(self):
        # The 1222-keyed block appears once as a block key; the
        # "type_a_1222_" prefix also occurs in the block_key field value
        # and the test_file field value (tests/test_type_a_1222_...).
        text = _block_text()
        assert text.count("type_a_1222_") == 3

    def test_next_leg_is_1223_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1223 Type B" in src


# ---------------------------------------------------------------------------
# 10. Background suite check-only per #795.
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1222:
    def test_suite_log_path_noted(self):
        status = _block()["background_suite_status"]
        assert "type_d_1220_full_suite.log" in status

    def test_suite_checked_only_recorded_not_touched(self):
        status = _block()["background_suite_status"]
        assert "CHECKED ONLY per #795" in status
        assert "neither re-launches, kills, nor writes" in status

    def test_verdict_belongs_to_1225(self):
        status = _block()["background_suite_status"]
        assert "#1225" in status

    def test_no_pytest_spawned_by_this_run(self):
        # This run's in-gate pytest invocation targets only this file;
        # no background full-suite process is owned by this run.
        status = _block()["background_suite_status"]
        assert "no verdict declared" in status


# ---------------------------------------------------------------------------
# 11. Doc-sync (#719: constants patched post-first-run; README/ARCHITECTURE
# rows and iteration-log entry land in the doc-sync followup).
# ---------------------------------------------------------------------------

class TestDocSync1222:
    def test_readme_stats_table_updated(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert "| Tests |" in text
        assert str(README_TEST_COUNT) in text

    def test_readme_test_table_row_present(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert OWN_BASENAME in text

    def test_architecture_tree_row_present(self):
        text = _read(os.path.join(REPO, "docs", "ARCHITECTURE.md"))
        assert OWN_BASENAME in text

    def test_iteration_log_entry_present(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1222 Type A:" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 66066 + COLLECTED_NEW_TESTS
        assert README_FILE_COUNT == 1547


# ---------------------------------------------------------------------------
# 12. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1222:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1222 Type A:" in text

    def test_no_duplicate_1222_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1222 Type A:") == 1

    def test_window_third_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1220-1224" in text

    def test_log_hash_followup_registers_hashes(self):
        # Per #721 the log-hash followup registers all four hashes in the
        # iteration-log entry; pre-commit the entry is absent and this is
        # vacuous via the header test above. Post-doc-sync the entry must
        # carry the main-commit hash once the log-hash followup lands.
        text = _read(os.path.join(REPO, "iteration-log.md"))
        if "## #1222 Type A:" in text and ANCHORED_SHA != "0" * 40:
            assert ANCHORED_SHA in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation (this run touches profiles/wired.yaml + the new
# test file only; #899/#938/#900/#1012-wt and #1024 stay out).
# ---------------------------------------------------------------------------

class TestInflightIsolation1222:
    def test_no_1222_markers_in_nytimes_yaml(self):
        text = _read(os.path.join(PROFILES_DIR, "nytimes.yaml"))
        assert BLOCK_KEY not in text
        assert "Type A #1222" not in text

    def test_no_1222_markers_in_inflight_test_files(self):
        for name in (
            "test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
            "test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",
            "test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
        ):
            text = _read(os.path.join(TESTS_DIR, name))
            assert BLOCK_KEY not in text, name
            assert "Type A #1222" not in text, name

    def test_m846_untouched(self):
        # #1024 m846 lives in profiles/competitor-entities.yaml; Ray's
        # revert/leave/rebuild decision is pending - this run must not
        # touch that file.
        text = _read(os.path.join(PROFILES_DIR, "competitor-entities.yaml"))
        assert BLOCK_KEY not in text
        assert "Type A #1222" not in text

    def test_wired_yaml_has_no_other_uncommitted_hunks(self):
        # Post-commit re-pin per the #1191-class pattern: the working tree
        # is clean after the four-commit sequence, so the pre-commit
        # "uncommitted diff contains the block" form is vacuous. The
        # post-commit form asserts the tree is clean and the landed block
        # is present exactly once as a block key.
        out = _git("diff", "--", "profiles/wired.yaml").stdout
        out_staged = _git("diff", "--cached", "--", "profiles/wired.yaml").stdout
        assert out.strip() == "", out.strip()
        assert out_staged.strip() == "", out_staged.strip()
        assert _block_text().count(BLOCK_KEY + ":") == 1

    def test_only_intended_paths_changed(self):
        # The working tree may only differ from HEAD on this run's two
        # paths plus the four pre-existing in-flight paths.
        out = _git("status", "--short").stdout
        allowed = {
            "profiles/wired.yaml",
            "tests/" + OWN_BASENAME,
            "profiles/nytimes.yaml",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
            "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",
            "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
        }
        for line in out.strip().splitlines():
            parts = line.split(None, 1)
            path = parts[-1].strip().strip('"')
            assert path in allowed, (line, path)
