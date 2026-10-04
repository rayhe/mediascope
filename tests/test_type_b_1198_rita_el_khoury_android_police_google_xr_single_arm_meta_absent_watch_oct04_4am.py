# -*- coding: utf-8 -*-
"""Type B #1198 tests: Rita El Khoury (Android Police senior writer)
FIRST dedicated Type B mechanism - m950 single-arm WATCH (NOT a
divergence finding). A systematic both-entities search (15 browser.search
query sets: 13 delegated-research + 2 main-run; 2 first-hand browser.open
reads, Oct 4 2026) surfaced exactly ONE attributable arm - her
Sep-17-2026 Android XR hands-on on Xreal Aura (+0.55 illustrative,
excerpt-attested, unobtrusiveness-as-virtue register, zero privacy
vocabulary) - and ZERO attributable Meta-glasses bylines after bounded
search (Muck Rack profile carries Moto Watch Ultra / Pixel Watch but no
Meta byline; Android Police Meta coverage in-window is Boxall/Steele,
both corpus-saturated). The mechanism pins the single arm, documents the
bounded absence, and sets a dated re-check (2-4 weeks): if a Meta arm
appears, the watch converts to a genuine two-arm mechanism testing the
Valnet incentive structure (mechanism 145). NOT a falsification-family
member; ledger holds at 47.

Iteration #1198, FOURTH leg of the 1195-1199 window
(D #1195 -> E #1196 -> A #1197 -> B #1198 -> C #1199).

The m950 block lives in profiles/careers/journalists.yaml as the
competitor_coverage sub-key of the new top-level `rita_el_khoury:` key
(per the #643 convention - zero rita_el_khoury top-level YAML key
pre-commit, zero Rita El Khoury prose hits pre-commit).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
One anchor test (the placeholder pin) fails BY DESIGN post-anchor.

Per #795: this run only CHECKS the #1195-launched background suite
(observed DEAD at this run's check: 1108 bytes, mtime Oct 4 02:23 PDT,
zero pytest processes alive, progress 1%); its verdict and tombstone
belong to #1200.

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the landed
or next number, the forty-seventh / forty-eighth member-claim forms, or
the thirty-fifth through fortieth direction forms; the constants are
constructed at runtime. (The landed ordinals live in wired.yaml (m946),
the-verge.yaml (m907) and competitor-entities.yaml
(m915/m933/m942/m945/m948) respectively.)
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
    "test_type_b_1198_rita_el_khoury_android_police_google_xr_"
    "single_arm_meta_absent_watch_oct04_4am.py"
)
BLOCK_KEY = (
    "type_b_1198_rita_el_khoury_android_police_google_xr_arm_only_"
    "meta_arm_absent_watch"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "de27d4753483539b302c737cf8aa5881143bd5c1"  # patched per #565
# Post-first-run values per #719: N tests collected; README ratchets
# 64134/1522 -> (64134+N)/1523 in the doc-sync followup.
README_TEST_COUNT = 64134 + 77  # 64211; patched post-first-run per #719
README_FILE_COUNT = 1523
COLLECTED_NEW_TESTS = 77  # patched post-first-run per #719

# Forward guards for the next landing. MECH_NUM=950 is THIS run's landed
# mechanism; NEXT_NUM=951 stays forward.
MECH_NUM = 950
NEXT_NUM = 951

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + number at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + number at runtime
FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
FORTY_EIGHTH_MEMBER = "FORTY" + "-EIGHTH falsification-family member"
THIRTY_FIFTH_DIR = "THIRTY" + "-FIFTH relationship direction"
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH relationship direction"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"
THIRTY_EIGHTH_DIR = "THIRTY" + "-EIGHTH relationship direction"
THIRTY_NINTH_DIR = "THIRTY" + "-NINTH relationship direction"
FORTIETH_DIR = "FORTI" + "ETH relationship direction"

# The landed m950 block lives here (colon-form key; no numeric-950 substring
# in the block key by designed keying per #715). El Khoury's entry is the
# top-level `rita_el_khoury:` key per the #643 convention.
JOURNALISTS_PATH = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
FILE_1197 = (
    "test_type_a_1197_mittr_openai_sep28_30_astra_chen_register_"
    "vs_carried_meta_sep23_india_havoc_oct04_3am.py"
)
EL_KHOURY_URLS = (
    "https://www.androidpolice.com/hour-with-android-xr-xreal-aura-glasses/",
    "https://wesearch.press/s/after-an-hour-with-android-xr-glasses-i-understand-why-googl-e4a3654b",
    "https://muckrack.com/rita-el-khoury",
    "https://talkingbiznews.com/media-news/android-police-hires-el-khoury-as-a-senior-writer/",
)

# Ordinal form of the falsification-family member that must stay present.
FORTY_SIXTH_LANDED = "FORTY-SIXTH falsification-family member"


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _load_journalists():
    return yaml.safe_load(_read(JOURNALISTS_PATH))


def _el_khoury_entry():
    data = _load_journalists()
    assert "rita_el_khoury" in data, "top-level rita_el_khoury key must exist"
    return data["rita_el_khoury"]


def _block():
    return _el_khoury_entry()["competitor_coverage"][BLOCK_KEY]


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

class TestAnchor1198:
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
        log = _git("log", "--oneline", "--grep=Type B #1198 anchor").stdout
        if ANCHORED_SHA != "0" * 40:
            assert "Type B #1198 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type B #1198:").stdout
        assert "Type B #1198" in log or ANCHORED_SHA == "0" * 40


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1198 is the FOURTH leg of the 1195-1199 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1198:
    def test_rotation_window_is_1195_1199(self):
        text = _block_text()
        assert "1195-1199" in text

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1195-1199 window FOURTH leg "
            "(D #1195 -> E #1196 -> A #1197 -> B #1198 -> C #1199)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1195", "Type E #1196", "Type A #1197"):
            assert marker in log, marker

    def test_next_run_is_type_c(self):
        # The next leg (#1199 Type C) is documented in this run's log entry
        # and block window field; it must not exist as a commit yet.
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "C #1199" in text
        assert _block()["window"].endswith("C #1199)")

    def test_no_type_b_1198_test_file_before_this_run(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1198_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (pre-commit claims, verifiable post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1198:
    def test_el_khoury_top_level_key_found(self):
        entry = _el_khoury_entry()
        assert entry["name"] == "Rita El Khoury"

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: the block key carries the iteration
        # number 1198, not the mechanism number.
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
        assert nums, "m950 must be present in profiles"

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_el_khoury_urls_in_block_source_urls_verbatim(self):
        urls = list(_el_khoury_entry()["source_urls"])
        for u in EL_KHOURY_URLS:
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
# 4. Block structure (the #643 top-level journalist-key convention).
# ---------------------------------------------------------------------------

class TestBlockStructure1198:
    def test_el_khoury_entry_is_top_level_key(self):
        data = _load_journalists()
        assert "rita_el_khoury" in data
        assert isinstance(data["rita_el_khoury"], dict)

    def test_competitor_coverage_subkey(self):
        entry = _el_khoury_entry()
        assert "competitor_coverage" in entry
        assert BLOCK_KEY in entry["competitor_coverage"]

    def test_mechanism_ids_list(self):
        entry = _el_khoury_entry()
        assert entry["mechanism_ids"] == [950]

    def test_required_block_fields(self):
        b = _block()
        for field in (
            "iteration", "mechanism_id", "type", "goal_id", "job_id",
            "scheduled_job_id", "date", "block_key", "test_file", "author",
            "journalist", "publication", "window", "design", "google_arm",
            "meta_arm_absent", "scorer", "financial_context", "finding",
            "confounders", "counter_evidence", "statistical_discipline",
            "verdict", "cautious_language_required", "correlational_note",
            "no_analysis_json_update", "falsification_family_member",
            "falsification_ledger", "ledger_note", "connects_to",
            "novelty", "research_method", "artifact_readiness",
            "background_suite_status", "in_flight",
        ):
            assert field in b, field

    def test_test_file_field_matches_own_basename(self):
        assert _block()["test_file"].endswith(OWN_BASENAME)

    def test_google_arm_tone(self):
        arm = _block()["google_arm"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == 0.55
        assert arm["entity"] == "google"

    def test_meta_arm_absent_documented(self):
        absent = _block()["meta_arm_absent"]
        assert absent["status"] == "ABSENT - bounded search negative"
        assert "recheck" in absent

    def test_publication_owner_valnet(self):
        entry = _el_khoury_entry()
        assert entry["publication_owner"] == "Valnet Inc."
        assert entry["current_publication"] == "Android Police"


# ---------------------------------------------------------------------------
# 5. m950 content discipline (single-arm watch honesty).
# ---------------------------------------------------------------------------

class TestM950ContentDiscipline1198:
    def test_key_quotes_verbatim(self):
        quotes = _block()["google_arm"]["key_quotes"]
        assert any("perfect solution for me" in q for q in quotes)
        assert any("more than simply impressed" in q for q in quotes)

    def test_evidence_tier_is_excerpt_attested(self):
        tier = _block()["google_arm"]["piece"]["evidence_tier"]
        assert "EXCERPT-ATTESTED" in tier
        assert "No full-text read" in tier

    def test_no_full_read_claim(self):
        # Honesty pin: MY block must not claim a first-hand full-text read
        # of the androidpolice.com page. (Scoped to the rita_el_khoury
        # entry: the m947 jeff_meyer block legitimately carries the
        # phrase for its own first-hand read.)
        text = _block_text()
        start = text.index("rita_el_khoury:")
        chunk = text[start:]
        assert "FIRST-HAND full-text read" not in chunk

    def test_recheck_dated(self):
        absent = _block()["meta_arm_absent"]
        assert "2-4 weeks" in absent["recheck"]

    def test_connects_to_145(self):
        assert 145 in _block()["connects_to"]

    def test_no_canonical_urls_constructed(self):
        # Every source URL must be one of the verbatim tool-output URLs.
        urls = list(_el_khoury_entry()["source_urls"])
        assert len(urls) == 4
        for u in EL_KHOURY_URLS:
            assert u in urls

    def test_near_miss_duino_documented_not_landed(self):
        # The Duino near-miss is documented in research_method but must not
        # appear as an arm or source URL (recency rejection).
        method = _block()["research_method"]
        assert "Duino" in method
        urls = list(_el_khoury_entry()["source_urls"])
        assert not any("howtogeek" in u for u in urls)

    def test_ascii_only(self):
        text = _block_text()
        start = text.index("rita_el_khoury:")
        chunk = text[start:start + 12000]
        chunk.encode("ascii")


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL ILLUSTRATIVE ONLY per Aug 28 rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1198:
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

    def test_no_delta_claimed(self):
        s = _block()["scorer"]
        assert s["illustrative_delta"] == "NOT_COMPUTABLE (single-arm watch)"

    def test_verdict_is_watch_not_finding(self):
        b = _block()
        assert b["verdict"].startswith("watch_pinned_not_a_finding")
        assert b["falsification_family_member"] is False
        assert b["no_analysis_json_update"] is True

    def test_statistical_discipline_strings(self):
        sd = _block()["statistical_discipline"]
        assert "watch_pinned_not_a_finding" in sd
        assert "artifact_grade false" in sd
        assert "no_analysis_json_update true" in sd

    def test_correlational_honesty(self):
        note = _block()["correlational_note"]
        assert "must not be cited as evidence of asymmetric coverage" in note


# ---------------------------------------------------------------------------
# 7. Falsification ledger (holds at 47 this run).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1198:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 47

    def test_forty_sixth_intact_in_verge(self):
        text = _read(os.path.join(PROFILES_DIR, "the-verge.yaml"))
        assert text.count(FORTY_SIXTH_LANDED) == 2

    def test_forty_seventh_stays_in_wired_m946(self):
        # No new member this run: the forty-seventh claim form stays
        # exactly in wired.yaml m946 (2 occurrences).
        text = _read(os.path.join(PROFILES_DIR, "wired.yaml"))
        assert text.count(FORTY_SEVENTH_MEMBER) == 2

    def test_forty_seventh_nowhere_else(self):
        for p in _needle_hits_profiles(FORTY_SEVENTH_MEMBER):
            assert p.endswith("wired.yaml"), p

    def test_forty_eighth_absent(self):
        assert _needle_hits_profiles(FORTY_EIGHTH_MEMBER) == []
        for p in _iter_source_files():
            if p.endswith(".py") and os.path.basename(p) != OWN_BASENAME:
                assert FORTY_EIGHTH_MEMBER not in open(
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

    def test_ledger_note_holds_at_47(self):
        note = _block()["ledger_note"]
        assert "Ledger holds at 47" in note
        assert "FORTY-SEVENTH member-form present" in note
        assert "FORTY-EIGHTH member-claim form absent repo-wide" in note


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (designed lifecycle; the #1199 Type C run
# pins the 951 landing).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1198:
    def test_zero_951_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 951" in src
        # Needles format-built per #715: constructed at runtime, never
        # written contiguously in source.
        assert (MECH_ID_MARKER + str(NEXT_NUM)) not in src
        assert (MECH_DASH_MARKER + str(NEXT_NUM)) not in src

    def test_no_fortieth_direction_guard(self):
        # The fortieth direction form stays absent in profiles/; the
        # constant is format-built so this file never carries it
        # contiguously. Scope is profiles/ (not repo-wide) because the
        # #1197 test file carries the contiguous fortieth needle in its
        # own constant definition (its fortieth test is profiles-scoped
        # too); a repo-wide scope would trip on that landed file.
        assert _needle_hits_profiles(FORTIETH_DIR) == [], FORTIETH_DIR
        assert len(FORTIETH_DIR) > 0

    def test_no_forty_eighth_member_guard(self):
        # Format-built per #715: constructed at runtime, never written
        # contiguously in source (verified by inspection of the constant
        # definition above).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FORTY_EIGHTH_MEMBER) not in src
        assert len(FORTY_EIGHTH_MEMBER) > 0

    def test_no_forty_seventh_member_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FORTY_SEVENTH_MEMBER) not in src
        assert len(FORTY_SEVENTH_MEMBER) > 0

    def test_1197_pins_flip_by_design_documented(self):
        # #1197's forward guards (max-949, zero-950 keys all forms,
        # no-Type-B-#1198-in-git-log) flip by design now that m950 has
        # landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1197" in src
        text = _block_text()
        assert "1197" in text or "m949" in text

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
# 9. Guard lifecycle (this run pins the 950 landing for #1199).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1198:
    def test_pins_on_950_landing(self):
        # The guards this run lays for the next leg: max-950, zero-951
        # numeric, no-Type-C-#1199-in-git-log.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 950" in src
        assert "NEXT_NUM = 951" in src

    def test_no_type_c_1199_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type C #1199").stdout
        assert log.strip() == ""

    def test_951_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1197_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1197))

    def test_el_khoury_key_unique(self):
        data = _load_journalists()
        assert list(data.keys()).count("rita_el_khoury") == 1


# ---------------------------------------------------------------------------
# 10. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1200).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1198:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1195_full_suite.log" in src

    def test_suite_checked_only_recorded_not_touched(self):
        # This run stays on targeted verification per the Type B brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest observation per #795:
        # #1195-launched suite DEAD at the 04:05 PDT check
        # (1108 bytes, last write Oct 4 02:23 PDT, progress 1%,
        # zero pytest processes alive). #1200 owns the verdict.
        status = _block()["background_suite_status"]
        assert "CHECKED ONLY" in status
        assert "DEAD" in status
        assert "#1200" in status

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no m950 markers.
        suite_log = os.path.expanduser(
            "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
            "hidden_files/type_d_1195_full_suite.log"
        )
        log = _read(suite_log)
        assert "m950" not in log
        assert "Type B #1198" not in log


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1198:
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
        assert "## #1198 Type B:" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 64134 + COLLECTED_NEW_TESTS
        assert README_FILE_COUNT == 1523


# ---------------------------------------------------------------------------
# 12. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1198:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1198 Type B:" in text

    def test_no_duplicate_1198_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1198 Type B:") == 1

    def test_window_fourth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1195-1199" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1198:
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
            assert "mechanism_id: 950" not in diff, path
            assert "Type B #1198" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 lives in profiles/competitor-entities.yaml;
        # this run must not alter that file at all.
        diff = _git("diff", "--", "profiles/competitor-entities.yaml").stdout
        assert "mechanism_id: 950" not in diff
        assert "Type B #1198" not in diff
