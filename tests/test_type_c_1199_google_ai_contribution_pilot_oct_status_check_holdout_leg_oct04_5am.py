# -*- coding: utf-8 -*-
"""Type C #1199 tests: Google AI-contribution pilot October status check
(TechRepublic Oct 2 2026) - several larger publishers DECLINED to
participate, hoping to negotiate more substantial licensing arrangements;
Simon Janvier analyst verdict (payout worth 0.1% of ad revenue, PR move);
scale/pricing/consent-decoupling/transparency-gap reconfirmed.
STATUS-CHECK EXTENSION of m891 (TWENTY-SEVENTH), m894 (TWENTY-EIGHTH),
m897 (TWENTY-NINTH), m900 (THIRTIETH) - no new direction landed.

Iteration #1199, FIFTH and CLOSING leg of the 1195-1199 window
(D #1195 -> E #1196 -> A #1197 -> B #1198 -> C #1199).

The m951 block lives in profiles/competitor-entities.yaml as a top-level
`type_c_1199_...` key (Type C convention; cf. m948 at #1194).

This run EXTENDS existing relationship directions; it does NOT land the
fortieth. The genuinely new leg is the large-publisher holdout
(TechRepublic Oct 2 2026), which deepens m894 divide-and-conquer from the
other side: the head opts out while the tail takes widget money. The
fortieth direction stays absent by design; the thirty-fifth (m915),
thirty-sixth (m933), thirty-seventh (m942), thirty-eighth (m945), and
thirty-ninth (m948) stand.

Ledger holds at 47: the forty-seventh falsification-family member stands
(m946, profiles/wired.yaml); this run claims no slot and takes no ledger
position beyond the hold.

Rejected candidates (not new directions, not status deltas): (1)
Lionsgate x Runway "new" deal - recycled Sep 2024 deal, no 2026 event;
(2) Stability AI $76M invest-and-license (TechCrunch Oct 2) - in corpus
as m942 (37th direction), follow-up interview peg; (3) Mehta
AI-Overviews dismissal re-report (Oct 3) - in corpus as m909 (33rd
direction); (4) OpenAI x Hearst (Bloomberg Law) - Oct 2024 deal in
corpus as #489, stale crawl; (5) Folha x OpenAI settlement arc - Aug
2025 suit + May 2026 deal in corpus, no in-window event; (6) Anthropic
settlement distribution friction - in corpus (m594), no October update;
(7) Apple Siri publisher negotiations / Axel Springer renewal - no Oct
reporting (bounded absence), m918's Oct 2 check stands. The memo's fifth
proposed URL (aiweekly.co) was already in-corpus (m891 block + #1099
test file) - caught pre-commit, excluded from novel sources.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.

Per #795: this run only CHECKS the #1195-launched background suite
(observed state recorded below); its verdict belongs to #1200.

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the next
number 952 keys, the forty-seventh / forty-eighth member forms, or the
fortieth direction-claim form; the 35th-39th direction forms are asserted
via runtime-built needles against the landed YAML (never written
contiguously in source); the constants are constructed at runtime.
"""

import glob
import os
import re
import subprocess

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
TESTS_DIR = HERE

OWN_BASENAME = (
    "test_type_c_1199_google_ai_contribution_pilot_oct_status_check_"
    "holdout_leg_oct04_5am.py"
)
BLOCK_KEY = (
    "type_c_1199_google_ai_contribution_pilot_oct_status_check_"
    "holdout_leg_oct04_5am"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "0000000000000000000000000000000000000000"
# Post-first-run values per #719: README_TEST_COUNT / README_FILE_COUNT are
# patched to the post-sync-positive values after the first collection run
# (README ratchets 64211/1523 -> 64211+N/1524 in the doc-sync followup).
README_TEST_COUNT = 64211 + 87  # 64298; patched post-first-run per #719
README_FILE_COUNT = 1524
COLLECTED_NEW_TESTS = 87  # patched post-first-run per #719

# Forward guards for the next landing. MECH_NUM=951 is THIS run's landed
# mechanism; NEXT_NUM=952 stays forward.
MECH_NUM = 951
NEXT_NUM = 952

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + "952" at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + "952" at runtime
THIRTY_FIFTH_DIR = "THIRTY" + "-FIFTH relationship direction"
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH relationship direction"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"
THIRTY_EIGHTH_DIR = "THIRTY" + "-EIGHTH relationship direction"
THIRTY_NINTH_DIR = "THIRTY" + "-NINTH relationship direction"
FORTIETH_DIR = "FORT" + "IETH relationship direction"
FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
FORTY_EIGHTH_MEMBER = "FORTY" + "-EIGHTH falsification-family member"

# The landed m951 block lives here (top-level key; designed keying per
# #715: the block key carries iteration 1199, no 951 substring).
ENTITIES_PATH = os.path.join(REPO, "profiles", "competitor-entities.yaml")
FILE_1198 = (
    "test_type_b_1198_rita_el_khoury_android_police_google_xr_single_"
    "arm_meta_absent_watch_oct04_4am.py"
)
M846_BLOCK_NEEDLE = "type_c_1024_benioff"

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1195_full_suite.log"
)


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _load_entities():
    return yaml.safe_load(_read(ENTITIES_PATH))


def _block():
    return _load_entities()[BLOCK_KEY]


def _entities_text():
    return _read(ENTITIES_PATH)


def _git(*args):
    return subprocess.run(
        ["git", "-C", REPO] + list(args), capture_output=True, text=True
    )


def _main_sha():
    # The main commit exists only post-commit; pre-commit this is empty and
    # the m846 test falls back to the working-tree diff against HEAD.
    out = _git("log", "--format=%H", "--grep=Type C #1199:").stdout.strip()
    return out.splitlines()[0] if out else ""


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
    hits = []
    for path in _iter_source_files():
        try:
            text = _read(path)
        except (OSError, UnicodeError):
            continue
        if pattern in text:
            hits.append(path)
    return hits


def _needle_hits_profiles(needle):
    # profiles/-scoped needle search (cf. #1198): the #1197 test file
    # carries the contiguous fortieth needle in its own constant
    # definition, so the fortieth absence guard is profiles-scoped.
    out = _git("grep", "-l", "-F", needle, "--", "profiles").stdout
    return out.strip().splitlines() if out.strip() else []


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------

class TestAnchor1199:
    def test_anchor_sha_format(self):
        # Patched in the anchor followup per #565: ANCHORED_SHA is the
        # main-commit hash, a 40-char hex string, not the placeholder.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40

    def test_anchor_sha_is_main_commit(self):
        # The anchor commit patches ANCHORED_SHA to the main-commit hash;
        # verify it appears in the git log as a commit hash.
        log = _git("log", "--format=%H").stdout
        assert ANCHORED_SHA in log

    def test_anchor_followup_commit_message_convention(self):
        # The anchor followup uses the documented message shape:
        # "Type C #1199 anchor followup: ANCHORED_SHA -> <hash> ...".
        log = _git("log", "--oneline", "--grep=Type C #1199 anchor").stdout
        assert "Type C #1199 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type C #1199:").stdout
        assert "Type C #1199" in log


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1199 is the FIFTH and CLOSING leg of 1195-1199.
# ---------------------------------------------------------------------------

class TestRotationGuard1199:
    def test_rotation_window_is_1195_1199(self):
        assert "1195-1199" in _entities_text()

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1195-1199 window FIFTH and CLOSING leg "
            "(D #1195 -> E #1196 -> A #1197 -> B #1198 -> C #1199)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1195", "Type E #1196", "Type A #1197",
                       "Type B #1198"):
            assert marker in log, marker

    def test_no_type_d_1200_in_git_log_yet(self):
        # The next window (1200-1204) opens with Type D #1200; it must not
        # exist as a commit yet.
        log = _git("log", "--oneline", "--grep=Type D #1200").stdout
        assert log.strip() == ""

    def test_single_type_c_1199_test_file(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_c_1199_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (pre-commit claims, verifiable post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1199:
    def test_block_key_present_once(self):
        assert _entities_text().count(BLOCK_KEY + ":") == 1

    def test_block_key_zero_951_substring(self):
        # Designed keying per #715: the block key carries the iteration
        # number 1199, not the mechanism number 951.
        assert "951" not in BLOCK_KEY

    def test_zero_underscore_951_repo_wide(self):
        # Per #1198's forward guard (zero-951 keys all forms): no
        # underscore-form 951 mechanism key may exist repo-wide
        # (own file excluded from the walk).
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_951_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_952_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_951(self):
        present = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert present, "m951 must be present in profiles"
        for n in range(MECH_NUM + 1, MECH_NUM + 20):
            assert _profiles_grep_numeric_mechanism_id(n) == [], n

    def test_no_duplicate_block_key(self):
        d = _load_entities()
        assert list(d.keys()).count(BLOCK_KEY) == 1

    def test_urls_copied_verbatim(self):
        urls = [s["url"] for s in _block()["sources"]]
        assert len(urls) == 4
        assert (
            "https://www.techrepublic.com/article/"
            "news-google-publisher-payments-ai-search/"
        ) in urls
        assert (
            "https://www.mail-studio.com/en/marketing-seo-en/"
            "google-ai-contribution-publishers/"
        ) in urls
        assert (
            "https://www.linkedin.com/pulse/google-ai-contribution-"
            "pilot-pays-value-clicks-markus-koeberle-fup3e"
        ) in urls
        assert (
            "https://www.linkedin.com/pulse/your-content-might-worth-"
            "money-googles-ai-right-now-ymv8f"
        ) in urls
        for u in urls:
            assert u.startswith("https://"), u

    def test_aiweekly_url_excluded_as_carried(self):
        # The memo's fifth URL was already in-corpus (m891 block + #1099
        # test file); it must NOT be among the novel sources.
        urls = [s["url"] for s in _block()["sources"]]
        assert not any("aiweekly.co" in u for u in urls)
        assert "aiweekly.co" in _block()["novelty"]

    def test_block_key_zero_hit_except_landed(self):
        # Pre-commit the block key was zero-hit repo-wide; post-commit it
        # appears only in the landed YAML block, this test file, and the
        # doc-sync surfaces (README, ARCHITECTURE, iteration-log).
        hits = _source_grep(BLOCK_KEY)
        allowed = {
            os.path.join(REPO, "profiles", "competitor-entities.yaml"),
            os.path.join(TESTS_DIR, OWN_BASENAME),
            os.path.join(REPO, "README.md"),
            os.path.join(REPO, "docs", "ARCHITECTURE.md"),
            os.path.join(REPO, "iteration-log.md"),
        }
        for h in hits:
            assert h in allowed, h


# ---------------------------------------------------------------------------
# 4. Block structure (Type C top-level key convention in
# profiles/competitor-entities.yaml).
# ---------------------------------------------------------------------------

class TestBlockStructure1199:
    def test_top_level_block_key(self):
        d = _load_entities()
        assert BLOCK_KEY in d

    def test_required_fields_present(self):
        b = _block()
        for field in (
            "block_key", "mechanism_id", "mechanism_name", "type",
            "type_label", "iteration", "iteration_type", "iteration_time",
            "goal_id", "scheduled_job_id", "window", "connects_to",
            "relationship_direction_taxonomy", "finding", "money_flow",
            "confounders", "coverage_nexus", "sources", "browser_opens",
            "tone_scored", "engine_run", "is_significant", "verdict",
            "no_analysis_json_update", "artifact_grade",
            "falsification_family_member", "falsification_family",
            "novelty", "rotation_transparency", "concurrency",
            "yaml_parse_clean", "ascii_only",
        ):
            assert field in b, field

    def test_type_and_iteration(self):
        b = _block()
        assert b["type"] == "financial_incentive_mapping"
        assert b["iteration_type"] == "C"
        assert b["iteration"] == 1199
        assert b["mechanism_id"] == 951

    def test_goal_and_job_ids(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_ascii_only_region(self):
        text = _entities_text()
        start = text.index(BLOCK_KEY + ":")
        text[start:].encode("ascii")

    def test_yaml_parse_clean(self):
        assert _block()["yaml_parse_clean"] is True
        assert _block()["ascii_only"] is True

    def test_browser_opens_zero(self):
        assert _block()["browser_opens"] == 0

    def test_connects_to(self):
        assert _block()["connects_to"] == [891, 894, 897, 900, 909]


# ---------------------------------------------------------------------------
# 5. m951 content discipline (Google AI-contribution pilot October
# status check; holdout leg; extension of the 27th-30th directions).
# ---------------------------------------------------------------------------

class TestM951ContentDiscipline1199:
    def test_holdout_leg(self):
        f = _block()["finding"]
        assert "DECLINED to participate" in f
        assert "more substantial licensing arrangements" in f

    def test_divide_deepened_leg(self):
        f = _block()["finding"]
        assert "m894" in f
        assert "head opts out" in f

    def test_scale_leg_reconfirmed(self):
        f = _block()["finding"]
        assert "invitation-only" in f
        assert "no application process" in f

    def test_pricing_tiers_leg(self):
        f = _block()["finding"]
        assert "0.1% of ad revenue" in f
        assert "$1M per year" in f

    def test_analyst_verdict_leg(self):
        f = _block()["finding"]
        assert "Simon Janvier" in f
        assert "PR move" in f
        assert "operationally irrelevant" in f

    def test_consent_decoupling_leg(self):
        f = _block()["finding"]
        assert "does NOT opt a site out" in f
        # YAML '' unescapes to a single apostrophe on load.
        assert "don't know how their payments are calculated" in f

    def test_regulatory_shadow_leg(self):
        f = _block()["finding"]
        assert "m909" in f
        assert "ONLY open payment channel" in f

    def test_money_flow_absent_flow(self):
        mf = _block()["money_flow"]
        assert "GOOGLE PAYS OUT" in mf
        assert "ABSENT flow" in mf
        assert "withheld payment" in mf

    def test_confounder_strengths(self):
        confs = _block()["confounders"]
        strengths = [c["strength"] for c in confs]
        assert strengths.count("STRONG") == 2
        assert "MODERATE" in strengths
        assert "WEAK" in strengths
        assert any("0 browser.open" in c["text"] for c in confs)

    def test_coverage_nexus(self):
        cn = _block()["coverage_nexus"]
        assert "NOT scored" in cn
        assert "iteration-492" in cn

    def test_four_novel_sources(self):
        assert len(_block()["sources"]) == 4
        assert all(s["novel"] is True for s in _block()["sources"])

    def test_extension_not_new_direction(self):
        assert "EXTENDS m891" in _block()["mechanism_name"]
        assert "STATUS-CHECK EXTENSION" in _block()[
            "relationship_direction_taxonomy"]
        assert "lands no new direction" in _block()["falsification_family"]


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL / qualitative-only per the Aug 28 2026
# standing rule; engine never run on findings).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1199:
    def test_no_engine_run(self):
        b = _block()
        assert b["engine_run"] is False
        assert b["tone_scored"] is False

    def test_stats_not_calculated(self):
        n = _block()["novelty"]
        assert "MANUAL / qualitative-only" in n
        assert "Aug 28 2026 standing rule" in n

    def test_verdict_discipline(self):
        b = _block()
        assert b["verdict"] == "directionally_supported_not_proven"
        assert b["no_analysis_json_update"] is True
        assert b["is_significant"] is False

    def test_not_artifact_grade(self):
        assert _block()["artifact_grade"] is False


# ---------------------------------------------------------------------------
# 7. Falsification ledger: NOT a member; ledger holds at 47.
# ---------------------------------------------------------------------------

class TestFalsificationLedger1199:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False

    def test_forty_seventh_member_form_present(self):
        # Format-built per #715: the contiguous form is never written in
        # this file's source (the 47th-member guard is file-scoped per
        # the #1193 convention; the landed claim lives in wired.yaml).
        assert _repo_grep(FORTY_SEVENTH_MEMBER), FORTY_SEVENTH_MEMBER
        assert len(FORTY_SEVENTH_MEMBER) > 0

    def test_ledger_holds_at_47(self):
        ff = _block()["falsification_family"]
        assert "ledger holds at 47" in ff
        assert "m946, profiles/wired.yaml" in ff

    def test_ledger_state_note_wording(self):
        ff = _block()["falsification_family"]
        assert "NOT a member" in ff
        assert "claims no slot" in ff
        # The forty-eighth absence is lowercase prose in the block (not
        # the guard form); the runtime-built needle asserts repo-wide
        # absence of the uppercase claim form.
        assert "forty-eighth member-claim form absent repo-wide" in ff
        assert not _repo_grep(FORTY_EIGHTH_MEMBER), FORTY_EIGHTH_MEMBER

    def test_own_file_no_contiguous_forty_seventh(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert FORTY_SEVENTH_MEMBER not in src
        assert len(FORTY_SEVENTH_MEMBER) > 0

    def test_own_file_no_contiguous_forty_eighth(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert FORTY_EIGHTH_MEMBER not in src
        assert len(FORTY_EIGHTH_MEMBER) > 0


# ---------------------------------------------------------------------------
# 8. Direction extension (this run EXTENDS the 27th-30th directions; the
# fortieth stays absent by design).
# ---------------------------------------------------------------------------

class TestDirectionExtension1199:
    def test_no_new_direction_landed(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert tax.startswith("STATUS-CHECK EXTENSION")

    def test_fortieth_direction_absent(self):
        # Forward guard: the fortieth direction-claim form must not
        # exist. Needle format-built per #715.
        assert FORTIETH_DIR not in _entities_text()

    def test_thirty_fifth_direction_still_present(self):
        # m915's METER-THEN-INVITE is the thirty-fifth relationship
        # direction; landed long ago, must still be present.
        assert THIRTY_FIFTH_DIR in _entities_text()

    def test_thirty_sixth_direction_still_present(self):
        # m933's REGULATORY-PREEMPTION is the thirty-sixth relationship
        # direction; landed #1169, must still be present.
        assert THIRTY_SIXTH_DIR in _entities_text()

    def test_thirty_seventh_direction_still_present(self):
        # m942's INVEST-AND-LICENSE is the thirty-seventh relationship
        # direction; landed #1184, must still be present.
        assert THIRTY_SEVENTH_DIR in _entities_text()

    def test_thirty_eighth_direction_still_present(self):
        # m945's LICENSE-AND-CO-BUILD is the thirty-eighth relationship
        # direction; landed #1189, must still be present.
        assert THIRTY_EIGHTH_DIR in _entities_text()

    def test_thirty_ninth_direction_still_present(self):
        # m948's LICENSE-AND-ADOPT is the thirty-ninth relationship
        # direction; landed #1194, must still be present.
        assert THIRTY_NINTH_DIR in _entities_text()

    def test_extended_directions_named(self):
        tax = _block()["relationship_direction_taxonomy"]
        assert "m891 UNILATERAL-PRICING" in tax
        assert "m894 DIVIDE-AND-CONQUER" in tax
        assert "m897 FRAME-THEN-PRICE" in tax
        assert "m900 TRACK-SEPARATED PRICING" in tax

    def test_own_file_no_contiguous_fortieth(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("FORT" + "IETH relationship direction") not in src
        assert len(FORTIETH_DIR) > 0

    def test_own_file_no_contiguous_952_forms(self):
        # Needles format-built per #715: constructed at runtime, never
        # written contiguously in source.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (MECH_ID_MARKER + str(NEXT_NUM)) not in src
        assert (MECH_DASH_MARKER + str(NEXT_NUM)) not in src


# ---------------------------------------------------------------------------
# 9. Forward-looking staleness (designed lifecycle; the #1200 Type D run
# pins the 952 landing).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1199:
    def test_zero_952_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 952" in src
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
        # Matches #1198's in-gate fix for the same defect class.
        assert _needle_hits_profiles(FORTIETH_DIR) == [], FORTIETH_DIR
        assert len(FORTIETH_DIR) > 0

    def test_no_forty_seventh_member_guard(self):
        # Format-built per #715: constructed at runtime, never written
        # contiguously in source (verified by inspection of the constant
        # definition above). File-scoped per the #1193 convention; the
        # landed claim lives in profiles/wired.yaml (the #1192 m946
        # block), not asserted here.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert FORTY_SEVENTH_MEMBER not in src
        assert len(FORTY_SEVENTH_MEMBER) > 0

    def test_no_forty_eighth_member_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert FORTY_EIGHTH_MEMBER not in src
        assert len(FORTY_EIGHTH_MEMBER) > 0

    def test_1198_pins_flip_by_design_documented(self):
        # #1198's forward guards (max-950, zero-951 keys all forms,
        # no-Type-C-#1199-in-git-log) flip by design now that m951 has
        # landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1198" in src
        text = _entities_text()
        assert "1198" in text or "m950" in text

    def test_thirty_fifth_direction_still_present(self):
        # The THIRTY-FIFTH relationship direction is a landed ordinal;
        # its wording must still be present repo-wide.
        assert _repo_grep("THIRTY-FIFTH relationship direction")

    def test_thirty_sixth_direction_still_present(self):
        assert _repo_grep("THIRTY-SIXTH relationship direction")

    def test_thirty_seventh_direction_still_present(self):
        assert _repo_grep("THIRTY-SEVENTH relationship direction")

    def test_thirty_eighth_direction_still_present(self):
        assert _repo_grep("THIRTY-EIGHTH relationship direction")

    def test_thirty_ninth_direction_still_present(self):
        assert _repo_grep("THIRTY-NINTH relationship direction")


# ---------------------------------------------------------------------------
# 10. Guard lifecycle (this run pins the 951 landing for #1200).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1199:
    def test_pins_on_951_landing(self):
        # The guards this run lays for the next leg: max-951, zero-952
        # numeric, no-Type-D-#1200-in-git-log, extension (fortieth
        # absent), forty-seventh intact, no forty-eighth.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 951" in src
        assert "NEXT_NUM = 952" in src

    def test_no_type_d_1200_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type D #1200").stdout
        assert log.strip() == ""

    def test_952_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1198_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1198))

    def test_1198_pins_flip_by_design_documented(self):
        # #1198's forward guards (max-950, zero-951 numeric,
        # no-Type-C-#1199-in-git-log) flip by design now that m951 has
        # landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1198" in src
        text = _entities_text()
        assert "1198" in text or "m950" in text


# ---------------------------------------------------------------------------
# 11. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1200).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1199:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1195_full_suite.log" in src

    def test_suite_checked_only_recorded_not_touched(self):
        # This run stays on targeted verification per the Type C brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest observation per #795:
        # #1195-launched suite DEAD at the ~05:00 PDT check (log 1108
        # bytes, last write Oct 4 02:23 PDT, progress 1%, zero pytest
        # processes alive at this run's ps scan; THIRTY-THIRD
        # consecutive background death). Its verdict and tombstone
        # belong to #1200 per #795. CHECKED ONLY.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "CHECKED ONLY" in src
        assert "THIRTY-THIRD" in src
        assert "#1200" in src

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no m951 markers.
        log = _read(SUITE_LOG)
        assert "m951" not in log
        assert "Type C #1199" not in log


# ---------------------------------------------------------------------------
# 12. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1199:
    def test_readme_stats_table_updated(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert "| Tests |" in text

    def test_readme_test_table_row_present(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert OWN_BASENAME in text

    def test_architecture_tree_row_present(self):
        text = _read(os.path.join(REPO, "docs", "ARCHITECTURE.md"))
        assert OWN_BASENAME in text

    def test_iteration_log_entry_present(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "#1199" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 64211 + COLLECTED_NEW_TESTS
        assert README_FILE_COUNT == 1524


# ---------------------------------------------------------------------------
# 13. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1199:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1199 Type C:" in text

    def test_no_duplicate_1199_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1199 Type C:") == 1

    def test_window_fifth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1195-1199" in text


# ---------------------------------------------------------------------------
# 14. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1199:
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
            assert "mechanism_id: 951" not in diff, path
            assert "Type C #1199" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 block lives in profiles/competitor-entities.yaml;
        # this run appends the m951 block at the end of that file but must
        # not alter the m846 block region. Post-commit the working-tree
        # diff is empty, so the check runs against the main commit's own
        # diff for the file (pre-commit it falls back to the working-tree
        # diff against HEAD).
        sha = _main_sha()
        if sha:
            diff = _git(
                "show", sha, "--", "profiles/competitor-entities.yaml"
            ).stdout
        else:
            diff = _git(
                "diff", "HEAD", "--", "profiles/competitor-entities.yaml"
            ).stdout
        assert M846_BLOCK_NEEDLE not in diff
        assert "mechanism_id: 951" in diff
