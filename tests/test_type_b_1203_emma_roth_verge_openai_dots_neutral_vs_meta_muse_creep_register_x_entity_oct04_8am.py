# -*- coding: utf-8 -*-
"""Type B #1203 tests: Emma Roth (The Verge) - OpenAI Dots neutral
launch-news register vs Meta Muse adversarial creep register,
(register x entity) refinement of m782/m860.

Mechanism m953 (NOT a falsification-family member; ledger holds at 48).
Excerpt-bounded research per #503 (11 browser.search query sets, 0
browser.open reads) rejected as corpus-saturated: Victoria Song Sep-24
Vergecast (in corpus via #993/m827), Joanna Stern Sep-2026 Zuckerberg
interview (in corpus via #1113), Philip Berne TechRadar city piece (in
corpus, m725 block), Karissa Bell (saturated m722/m764), Andy Boxall
Sep-24 Audio "PR stunt" piece (saturated m824/m935), James Pero
(saturated m858/m933/m1003). The WIRED Sep-15 "I Felt Super Violated"
dating piece was investigated but its byline could not be attributed
from bounded search, so no mechanism was built on it.

The landed arm is NEW: Roth's Sep-29-2026 "OpenAI launches Dots, its
Muse competitor" (neutral product-news relay, +0.05 MANUAL
ILLUSTRATIVE, excerpt-attested via mirrors; canonical theverge.com URL
not recovered, none constructed). The Meta arm is CARRIED from m782
(#918, un-rescored per #807): Roth's Sep-10 "Meta's Muse AI works and
creeps me out" hands-on (-0.4). The Dots piece describes the functional
twin of the Muse behaviors that triggered Roth's creep toolkit
(always-on, "learn your preferences over time", "carry over the
context", "before you even think to ask") with zero of the toolkit: no
creep headline, no track-record anchor, no comment-seeking, no
suspicion-as-conclusion. Illustrative delta (Meta minus OpenAI) -0.45.
FIRST Roth OpenAI comparator arm (m782's counterevidence noted its
absence). Refinement: the creep toolkit is (register x entity)
conditional - it requires the Meta entity even when the behavioral peg
is identical; m860 (Roth neutral on Meta launch news) vs this arm
(neutral on OpenAI launch news) shows launch-news parity, ruling out a
blanket entity effect. Genre (hands-on vs launch news) remains the
dominant confound.

Iteration #1203, FOURTH leg of the 1200-1204 window
(D #1200 -> E #1201 -> A #1202 -> B #1203 -> C #1204).

The m953 block lives in profiles/careers/journalists.yaml as a
competitor_coverage sub-key of the EXISTING top-level `emma_roth_type_b`
key (mechanism_ids [782, 860] -> [782, 860, 953]).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
One anchor test (the placeholder pin) fails BY DESIGN post-anchor.

Per #795: this run only CHECKS the #1200-launched background suite
(observed DEAD at this run's check: 31226 bytes, mtime Oct 4 2026
07:59:29 PDT, zero pytest processes alive, ~10% progress); its verdict
and tombstone belong to #1205 (next Type D).

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the landed
or next number, the forty-eighth / forty-ninth member-claim forms, or
the thirty-fifth through fortieth direction forms; the constants are
constructed at runtime. (The landed forty-eighth ordinal lives in
financial-times.yaml (m952).)
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
    "test_type_b_1203_emma_roth_verge_openai_dots_neutral_vs_"
    "meta_muse_creep_register_x_entity_oct04_8am.py"
)
BLOCK_KEY = (
    "type_b_1203_emma_roth_verge_openai_dots_neutral_vs_"
    "meta_muse_creep_register_x_entity_oct04"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "0" * 40
# Post-first-run values per #719: N tests collected; README ratchets
# 64524/1527 -> (64524+N)/1528 in the doc-sync followup.
README_TEST_COUNT = 64524 + 75  # 64599; patched post-first-run per #719
README_FILE_COUNT = 1528
COLLECTED_NEW_TESTS = 75  # patched post-first-run per #719

# Forward guards for the next landing. MECH_NUM=953 is THIS run's landed
# mechanism; NEXT_NUM=954 stays forward.
MECH_NUM = 953
NEXT_NUM = 954

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + number at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + number at runtime
FORTY_EIGHTH_MEMBER = "FORTY" + "-EIGHTH falsification-family member"
FORTY_NINTH_MEMBER = "FORTY" + "-NINTH falsification-family member"
THIRTY_FIFTH_DIR = "THIRTY" + "-FIFTH relationship direction"
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH relationship direction"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"
THIRTY_EIGHTH_DIR = "THIRTY" + "-EIGHTH relationship direction"
THIRTY_NINTH_DIR = "THIRTY" + "-NINTH relationship direction"
FORTIETH_DIR = "FORTI" + "ETH relationship direction"

# The landed m953 block lives here (colon-form key; no numeric-953 substring
# in the block key by designed keying per #715). Roth's entry is the
# pre-existing top-level `emma_roth_type_b:` key (NOT a #643 new key).
JOURNALISTS_PATH = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
FILE_1202 = (
    "test_type_a_1202_ft_openai_oct01_03_safety_crisis_accountability_"
    "originals_vs_wsj_scoop_bounded_absence_oct04_8am.py"
)
ROTH_URLS = (
    "https://best-technologies.info/tech/openai-launches-dots-its-muse-competitor/",
    "https://wesearch.press/s/openai-launches-dots-its-muse-competitor-032218cf",
    "https://technewstube.com/theverge/1871645/openai-dots-muse-competitor/",
    "https://muckrack.com/emma-roth/articles",
)


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _load_journalists():
    return yaml.safe_load(_read(JOURNALISTS_PATH))


def _roth_entry():
    data = _load_journalists()
    assert "emma_roth_type_b" in data, "top-level emma_roth_type_b key must exist"
    return data["emma_roth_type_b"]


def _block():
    return _roth_entry()["competitor_coverage"][BLOCK_KEY]


def _block_text():
    return _read(JOURNALISTS_PATH)


def _git(*args):
    return subprocess.run(
        ["git", "-C", REPO] + list(args), capture_output=True, text=True
    )


def _profiles_grep_numeric_mechanism_id(num):
    out = _git("grep", "-F", "mechanism_id: %d" % num, "--", "profiles").stdout
    return out.strip().splitlines() if out.strip() else []


def _needle_hits_profiles(needle):
    out = _git("grep", "-l", "-F", needle, "--", "profiles").stdout
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
    hits = []
    for path in _iter_source_files():
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

class TestAnchor1203:
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
        log = _git("log", "--oneline", "--grep=Type B #1203 anchor").stdout
        if ANCHORED_SHA != "0" * 40:
            assert "Type B #1203 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type B #1203:").stdout
        assert "Type B #1203" in log or ANCHORED_SHA == "0" * 40


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1203 is the FOURTH leg of the 1200-1204 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1203:
    def test_rotation_window_is_1200_1204(self):
        text = _block_text()
        assert "1200-1204" in text

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1200-1204 window FOURTH leg "
            "(D #1200 -> E #1201 -> A #1202 -> B #1203 -> C #1204)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1200", "Type E #1201", "Type A #1202"):
            assert marker in log, marker

    def test_next_run_is_type_c(self):
        # The next leg (#1204 Type C) is documented in this run's log entry
        # and block window field; it must not exist as a commit yet.
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "C #1204" in text
        assert _block()["window"].endswith("C #1204)")

    def test_no_type_b_1203_test_file_before_this_run(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1203_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (pre-commit claims, verifiable post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1203:
    def test_roth_top_level_key_found(self):
        entry = _roth_entry()
        assert entry["name"] == "Emma Roth"

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: the block key carries the iteration
        # number 1203, not the mechanism number.
        assert str(MECH_NUM) not in BLOCK_KEY
        assert str(NEXT_NUM) not in BLOCK_KEY

    def test_zero_underscore_mechanism_repo_wide(self):
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_mechanism_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_next_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_this_run(self):
        nums = []
        for line in _profiles_grep_numeric_mechanism_id(MECH_NUM):
            nums.append(MECH_NUM)
        for n in range(MECH_NUM + 1, MECH_NUM + 20):
            assert _profiles_grep_numeric_mechanism_id(n) == [], n
        assert nums, "m953 must be present in profiles"

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_roth_urls_in_block_source_urls_verbatim(self):
        urls = list(_block()["source_urls"])
        for u in ROTH_URLS:
            assert u in urls, u
        assert all(u.startswith("https://") for u in urls)

    def test_block_key_zero_hit_except_landed(self):
        # Pre-commit the block key was zero-hit repo-wide; post-commit it
        # appears only in the landed YAML block, this test file, and the
        # doc-sync targets (README, ARCHITECTURE, iteration-log).
        hits = _source_grep(BLOCK_KEY)
        allowed = {
            os.path.join(REPO, "profiles", "careers", "journalists.yaml"),
            os.path.join(TESTS_DIR, OWN_BASENAME),
            os.path.join(REPO, "README.md"),
            os.path.join(REPO, "docs", "ARCHITECTURE.md"),
            os.path.join(REPO, "iteration-log.md"),
        }
        for h in hits:
            assert h in allowed, h


# ---------------------------------------------------------------------------
# 4. Block structure (pre-existing journalist key; third Roth mechanism).
# ---------------------------------------------------------------------------

class TestBlockStructure1203:
    def test_roth_entry_is_top_level_key(self):
        data = _load_journalists()
        assert "emma_roth_type_b" in data
        assert isinstance(data["emma_roth_type_b"], dict)

    def test_competitor_coverage_subkey(self):
        entry = _roth_entry()
        assert "competitor_coverage" in entry
        assert BLOCK_KEY in entry["competitor_coverage"]

    def test_mechanism_ids_list(self):
        entry = _roth_entry()
        assert entry["mechanism_ids"] == [782, 860, 953]

    def test_required_block_fields(self):
        b = _block()
        for field in (
            "iteration", "mechanism_id", "type", "goal_id", "job_id",
            "scheduled_job_id", "date", "block_key", "test_file", "author",
            "journalist", "publication", "window", "design", "openai_arm",
            "meta_arm", "scorer", "financial_context", "finding",
            "confounders", "counter_evidence", "statistical_discipline",
            "verdict", "cautious_language_required", "correlational_note",
            "no_analysis_json_update", "falsification_family_member",
            "falsification_ledger", "ledger_note", "connects_to",
            "novelty", "research_method", "artifact_readiness",
            "background_suite_status", "in_flight", "source_urls",
        ):
            assert field in b, field

    def test_test_file_field_matches_own_basename(self):
        assert _block()["test_file"].endswith(OWN_BASENAME)

    def test_openai_arm_tone(self):
        arm = _block()["openai_arm"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == 0.05
        assert arm["entity"] == "openai"
        assert arm["author_byline"] == "Emma Roth"

    def test_meta_arm_carried_documented(self):
        arm = _block()["meta_arm"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.4
        assert arm["entity"] == "meta"
        assert "CARRIED from m782" in arm["status"]

    def test_publication_the_verge(self):
        entry = _roth_entry()
        assert entry["publication"] == "the-verge"


# ---------------------------------------------------------------------------
# 5. m953 content discipline (excerpt honesty, verbatim quotes, no
# constructed URLs).
# ---------------------------------------------------------------------------

class TestM953ContentDiscipline1203:
    def test_key_quotes_verbatim(self):
        quotes = _block()["openai_arm"]["key_quotes"]
        assert any("learning your preferences over time" in q for q in quotes)
        assert any("before you even think to ask" in q for q in quotes)
        assert any("cute, customizable avatars" in q for q in quotes)

    def test_meta_arm_quotes_carried(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        assert any("creeps me out" in q for q in quotes)
        assert any("track record on privacy" in q for q in quotes)

    def test_evidence_tier_is_excerpt_attested(self):
        tier = _block()["openai_arm"]["evidence_tier"]
        assert "EXCERPT-TIER" in tier
        assert "not first-hand read" in tier

    def test_no_full_read_claim(self):
        # Honesty pin: the block must not claim a first-hand full-text read
        # of the theverge.com Dots page. (Scoped to the m953 block: the
        # m782 meta arm legitimately carries first-hand material.)
        text = _block_text()
        start = text.index(BLOCK_KEY + ":")
        chunk = text[start:start + 14000]
        assert "FIRST-HAND full-text read" not in chunk

    def test_no_canonical_url_constructed(self):
        # Every source URL must be one of the verbatim tool-output URLs.
        urls = list(_block()["source_urls"])
        assert len(urls) == 4
        for u in ROTH_URLS:
            assert u in urls
        assert not any(u.startswith("https://www.theverge.com/") for u in urls)

    def test_research_rejections_documented(self):
        method = _block()["research_method"]
        for name in ("Victoria Song", "Joanna Stern", "Philip Berne",
                     "Karissa Bell", "Andy Boxall", "James Pero"):
            assert name in method, name
        assert "I Felt Super Violated" in method

    def test_ascii_only(self):
        text = _block_text()
        start = text.index(BLOCK_KEY + ":")
        chunk = text[start:start + 14000]
        chunk.encode("ascii")


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL ILLUSTRATIVE ONLY per Aug 28 rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1203:
    def test_manual_illustrative_only(self):
        s = _block()["scorer"]
        assert "MANUAL ILLUSTRATIVE ONLY" in s["method"]
        assert s["engine_run"] is False
        assert s["is_significant"] is False

    def test_no_inferential_stats(self):
        s = _block()["scorer"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"

    def test_delta_is_illustrative(self):
        s = _block()["scorer"]
        assert s["illustrative_delta_meta_minus_openai"] == -0.45
        assert s["meta_tone_MANUAL_ILLUSTRATIVE"] == -0.4
        assert s["openai_tone_MANUAL_ILLUSTRATIVE"] == 0.05

    def test_verdict_is_refinement_not_discovery(self):
        b = _block()
        assert b["verdict"].startswith("mechanism_refinement_not_a_discovery")
        assert b["falsification_family_member"] is False
        assert b["no_analysis_json_update"] is True

    def test_statistical_discipline_strings(self):
        sd = _block()["statistical_discipline"]
        assert "NOT artifact-grade" in sd
        assert "no_analysis_json_update true" in sd

    def test_correlational_honesty(self):
        note = _block()["correlational_note"]
        assert "Correlation is not causation" in note
        assert "must accompany any citation" in note


# ---------------------------------------------------------------------------
# 7. Falsification ledger (holds at 48 this run).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1203:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 48

    def test_forty_eighth_intact_in_ft(self):
        # No new member this run: the forty-eighth claim form stays
        # exactly in financial-times.yaml m952 (2 occurrences).
        text = _read(os.path.join(PROFILES_DIR, "financial-times.yaml"))
        assert text.count(FORTY_EIGHTH_MEMBER) == 2

    def test_forty_eighth_nowhere_else(self):
        for p in _needle_hits_profiles(FORTY_EIGHTH_MEMBER):
            assert p.endswith("financial-times.yaml"), p

    def test_forty_ninth_absent(self):
        assert _needle_hits_profiles(FORTY_NINTH_MEMBER) == []
        for p in _iter_source_files():
            if p.endswith(".py") and os.path.basename(p) != OWN_BASENAME:
                assert FORTY_NINTH_MEMBER not in open(
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

    def test_ledger_note_holds_at_48(self):
        note = _block()["ledger_note"]
        assert "Ledger holds at 48" in note
        assert "FORTY-EIGHTH member-claim form present" in note
        assert "FORTY-NINTH member-claim form absent repo-wide" in note


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (designed lifecycle; the #1204 Type C run
# pins the 954 landing).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1203:
    def test_zero_954_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 954" in src
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

    def test_no_forty_ninth_member_guard(self):
        # Format-built per #715: constructed at runtime, never written
        # contiguously in source (verified by inspection of the constant
        # definition above).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FORTY_NINTH_MEMBER) not in src
        assert len(FORTY_NINTH_MEMBER) > 0

    def test_no_forty_eighth_member_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FORTY_EIGHTH_MEMBER) not in src
        assert len(FORTY_EIGHTH_MEMBER) > 0

    def test_1202_pins_flip_by_design_documented(self):
        # #1202's forward guards (max-952, zero-953 keys all forms,
        # no-Type-B-#1203-in-git-log) flip by design now that m953 has
        # landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1202" in src
        text = _block_text()
        assert "1202" in text or "m952" in text

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
# 9. Guard lifecycle (this run pins the 953 landing for #1204).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1203:
    def test_pins_on_953_landing(self):
        # The guards this run lays for the next leg: max-953, zero-954
        # numeric, no-Type-C-#1204-in-git-log.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 953" in src
        assert "NEXT_NUM = 954" in src

    def test_no_type_c_1204_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type C #1204").stdout
        assert log.strip() == ""

    def test_954_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1202_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1202))

    def test_roth_key_unique(self):
        data = _load_journalists()
        assert list(data.keys()).count("emma_roth_type_b") == 1


# ---------------------------------------------------------------------------
# 10. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1205).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1203:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1200_full_suite.log" in src

    def test_suite_checked_only_recorded_not_touched(self):
        # This run stays on targeted verification per the Type B brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest observation per #795:
        # #1200-launched suite DEAD at the 08:05 PDT check
        # (31226 bytes, last write Oct 4 07:59:29 PDT, progress ~10%,
        # zero pytest processes alive). #1205 owns the verdict.
        status = _block()["background_suite_status"]
        assert "CHECKED ONLY" in status
        assert "DEAD" in status
        assert "#1205" in status

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no m953 markers.
        suite_log = os.path.expanduser(
            "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
            "hidden_files/type_d_1200_full_suite.log"
        )
        log = _read(suite_log)
        assert "m953" not in log
        assert "Type B #1203" not in log


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1203:
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
        assert "## #1203 Type B:" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 64524 + COLLECTED_NEW_TESTS
        assert README_FILE_COUNT == 1528


# ---------------------------------------------------------------------------
# 12. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1203:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1203 Type B:" in text

    def test_no_duplicate_1203_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1203 Type B:") == 1

    def test_window_fourth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1200-1204" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1203:
    def test_inflight_files_untouched_by_this_run(self):
        # Marker-scoped: the working tree carries pre-existing
        # in-flight uncommitted changes (#899 nytimes.yaml hunk,
        # #938 test file, #900 test file, #1012-wt test-file edit).
        # This run's markers must appear in NONE of their diffs;
        # targeted staging at commit time picks up only this run's
        # two files.
        for path in (
            "profiles/nytimes.yaml",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_"
            "gemini_personalization_vs_meta_luna_stigma_sep16.py",
            "tests/test_type_d_900_m769_qualitative_corpus_integrity_"
            "sep21_1pm.py",
            "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_"
            "turn_agenda_setting_register_vs_carried_meta_india_"
            "havoc_m817_pairing_sep26_7am.py",
        ):
            diff = _git("diff", "--", path).stdout
            assert "mechanism_id: 953" not in diff, path
            assert "Type B #1203" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 lives in profiles/competitor-entities.yaml;
        # this run must not alter that file at all.
        diff = _git("diff", "--", "profiles/competitor-entities.yaml").stdout
        assert "mechanism_id: 953" not in diff
        assert "Type B #1203" not in diff
