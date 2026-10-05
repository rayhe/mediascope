# -*- coding: utf-8 -*-
"""Type B #1223 tests: Allison Johnson (The Verge) - Meta Muse AI agent
hands-on vs OpenAI Dots agent hands-on, journalist-level CONFIRMING case
of the payer-softening direction (m965).

Mechanism m965 (confirming case; ledger HOLDS at 50 - NOT a
falsification-family member). Johnson applies the playful-diminutive
consumer-skepticism register to Meta's Muse ("cute little guy", "great at
spending my money", -0.20 MANUAL ILLUSTRATIVE) and the
enterprise-competent register to OpenAI's Dots ("enterprise software",
"work tools with a friendly skin", +0.25 MANUAL ILLUSTRATIVE);
illustrative delta (OpenAI minus Meta) +0.45, directionally favoring the
deal partner. The journalist herself performs the contrast in-text: "But
unlike the ultra-approachable Meta Muse, Dots feel very much like using
workplace software". Extends mechanism 494 (Vox Media x OpenAI strategic
content and product partnership, May 29 2024, owner-level tie to The
Verge) from the owner-level mapping into the journalist-level register;
Vox Media is OpenAI-only among AI-lab payers (corpus line at
competitor-entities.yaml:2798), Meta pays Vox $0. FIRST committed
Allison Johnson mechanism in corpus; zero dedicated type_b key
pre-commit (three provisional "no clean pair surfaced" rejection notes in
other journalists blocks, now resolved by the Oct 2 OpenAI Dots piece).

Excerpt-bounded research per #503 (delegated research + 2 main-run
browser.search verification sets: Meta-arm byline/quote attestation via
muckrack profile + wesearch.press listing + relay quote text; OpenAI-arm
byline/quote attestation via aifuture.org relay ("Photo: Allison Johnson
/ The Verge") + remotestake desk analysis; 0 browser.open reads).
Researcher screened 18 journalists; main-run verified all novelty claims
on the selected pair.

The m965 block lives in profiles/careers/journalists.yaml as a
competitor_coverage sub-key of the NEW top-level `allison_johnson_type_b`
key (per the #643 convention; name appears only in three provisional
rejection notes in other blocks and the iteration-log; zero dedicated
type_b key pre-commit).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
One anchor test (the placeholder pin) fails BY DESIGN post-anchor.

Per #795: this run only CHECKS the #1220-launched background suite
(observed at this run's check: 336 bytes, mtime Oct 4 2026 21:15 PDT,
~105 min stale at the ~23:00 check, no pytest process alive, zero
processes holding the log open per the /proc open-fd check - an
observation, not a verdict); its verdict and tombstone belong to #1225
(next Type D).

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
NEXT number, the forty-eighth / forty-ninth / fiftieth / fifty-first
member-claim forms, or the thirty-fifth through fortieth direction forms;
the constants are constructed at runtime. (The landed fiftieth ordinal
lives in profiles/careers/journalists.yaml (m959); the forty-ninth lives
there too (m956); the forty-eighth lives in profiles/financial-times.yaml
(m952). No fifty-first member-claim form exists repo-wide; this run does
not create one.)
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
    "test_type_b_1223_allison_johnson_verge_meta_muse_vs_openai_dots_"
    "oct04_11pm.py"
)
BLOCK_KEY = (
    "type_b_1223_allison_johnson_verge_meta_muse_vs_openai_dots_"
    "oct04_11pm"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "0" * 40  # patched per #565
# Post-first-run values per #719: N tests collected; README ratchets
# 66148/1547 -> (66148+N)/1548 in the doc-sync followup.
README_TEST_COUNT = 66148 + 65  # 66213; patched post-first-run per #719
README_FILE_COUNT = 1548
COLLECTED_NEW_TESTS = 65  # patched post-first-run per #719

# Forward guards for the next landing. MECH_NUM=965 is THIS run's landed
# mechanism; NEXT_NUM=966 stays forward.
MECH_NUM = 965
NEXT_NUM = 966

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + number at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + number at runtime
FORTY_EIGHTH_MEMBER = "FORTY" + "-EIGHTH falsification-family member"
FORTY_NINTH_MEMBER = "FORTY" + "-NINTH falsification-family member"
FIFTIETH_MEMBER = "FIFT" + "IETH falsification-family member"
FIFTY_FIRST_MEMBER = "FIFTY" + "-FIRST falsification-family member"
THIRTY_FIFTH_DIR = "THIRTY" + "-FIFTH relationship direction"
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH relationship direction"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"
THIRTY_EIGHTH_DIR = "THIRTY" + "-EIGHTH relationship direction"
THIRTY_NINTH_DIR = "THIRTY" + "-NINTH relationship direction"
FORTIETH_DIR = "FORTI" + "ETH relationship direction"

# The landed 965 block lives here (colon-form key; no numeric-965 substring
# in the block key by designed keying per #715). It is a
# competitor_coverage sub-key of the NEW top-level `allison_johnson_type_b`
# key in profiles/careers/journalists.yaml.
JOURNALISTS_PATH = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
FILE_1222 = (
    "test_type_a_1222_wired_apple_n50_promise_vs_meta_audio_remediation_"
    "silence_oct04_10pm.py"
)
FILE_1221 = "test_type_e_1221_podcast_sentiment_167th_verification_oct04_915pm.py"
FILE_1220 = (
    "test_type_d_1220_m961_m962_m963_qualitative_corpus_integrity_"
    "oct04_9pm.py"
)
JOHNSON_URLS = (
    "https://wesearch.press/s/metas-ai-agent-is-a-cute-little-guy-"
    "whos-great-at-spending-m-87fc3267",
    "https://www.todayintabs.com/p/meta-s-new-a-i-agent-for-losers",
    "https://remotestake.com/news/meta-s-ai-agent-is-a-cute-little-guy-"
    "who-s-great-at-spending-my-money-94f7e",
    "https://breakingnewstoday.eu/tech/metas-ai-agent-is-a-cute-little-"
    "guy-whos-great-at-spending-my-money/",
    "https://muckrack.com/allison-johnson-4",
    "https://aifuture.org/news/openai-s-dot-agent-is-enterprise-software-"
    "that-can-also-order-your-dinner-15015",
    "https://remotestake.com/news/openai-s-dot-agent-is-enterprise-"
    "software-that-can-also-order-your-dinner-84461",
)


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _load_journalists():
    with open(JOURNALISTS_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _johnson_entry():
    return _load_journalists()["allison_johnson_type_b"]


def _block():
    return _johnson_entry()["competitor_coverage"][BLOCK_KEY]


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
# 1. Anchor convention per #565.
# ---------------------------------------------------------------------------

class TestAnchor1223:
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
        log = _git("log", "--oneline", "--grep=Type B #1223 anchor").stdout
        if ANCHORED_SHA != "0" * 40:
            assert "Type B #1223 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type B #1223:").stdout
        assert "Type B #1223" in log or ANCHORED_SHA == "0" * 40


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1223 is the FOURTH leg of the 1220-1224 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1223:
    def test_rotation_window_is_1220_1224(self):
        text = _block_text()
        assert "1220-1224" in text

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1220-1224 window FOURTH leg "
            "(D #1220 -> E #1221 -> A #1222 -> B #1223 -> C #1224)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1220", "Type E #1221", "Type A #1222"):
            assert marker in log, marker

    def test_next_run_is_type_c(self):
        # The next leg (#1224 Type C) is documented in the window string;
        # it must not exist as a commit yet.
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "C #1224" in text
        assert _block()["window"].endswith("C #1224)")

    def test_no_type_b_1223_test_file_before_this_run(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1223_*.py"))
        assert files == [] or (
            len(files) == 1 and os.path.basename(files[0]) == OWN_BASENAME
        )


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (per #715).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1223:
    def test_johnson_top_level_key_found(self):
        assert "allison_johnson_type_b" in _load_journalists()

    def test_block_key_zero_mechanism_number_substring(self):
        assert "965" not in BLOCK_KEY
        assert "1223" in BLOCK_KEY

    def test_zero_underscore_mechanism_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_zero_dash_mechanism_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_zero_numeric_next_in_profiles(self):
        # NEXT_NUM=966 stays forward; MECH_NUM=965 is landed this run.
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_this_run(self):
        hits = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert len(hits) == 1, hits
        # git grep lines are "path:match"; the path is the prefix.
        assert hits[0].split(":")[0].endswith(
            os.path.join("careers", "journalists.yaml")
        ), hits[0]

    def test_no_duplicate_block_key(self):
        text = _block_text()
        # key line + block_key field + test_file field (which carries the
        # block key as its filename prefix).
        assert text.count(BLOCK_KEY) == 3

    def test_johnson_urls_in_block_source_urls_verbatim(self):
        src = _block()["source_urls"]
        for url in JOHNSON_URLS:
            assert url in src, url

    def test_block_key_zero_hit_except_landed(self):
        # The block key may appear only in the landed YAML block and in this
        # test file (BLOCK_KEY constant + references). Own-file uses are
        # excluded by design.
        hits = _source_grep(BLOCK_KEY)
        landed = [h for h in hits if "journalists.yaml" in h]
        assert len(landed) == 1, landed


# ---------------------------------------------------------------------------
# 4. Block structure.
# ---------------------------------------------------------------------------

class TestBlockStructure1223:
    def test_johnson_entry_is_top_level_key(self):
        data = _load_journalists()
        entry = data["allison_johnson_type_b"]
        assert entry["name"] == "Allison Johnson"
        assert entry["publication"] == "the-verge"

    def test_mechanism_ids_list(self):
        entry = _johnson_entry()
        assert entry["mechanism_ids"] == [965]

    def test_competitor_coverage_sub_key(self):
        entry = _johnson_entry()
        assert BLOCK_KEY in entry["competitor_coverage"]

    def test_required_fields_present(self):
        b = _block()
        for field in (
            "block_key",
            "mechanism_id",
            "iteration",
            "type",
            "date",
            "test_file",
            "author",
            "goal_id",
            "job_id",
            "journalist",
            "publication",
            "window",
            "meta_arm",
            "openai_arm",
            "scorer",
            "verdict",
            "source_urls",
        ):
            assert field in b, field

    def test_mechanism_id_field_value(self):
        assert _block()["mechanism_id"] == MECH_NUM
        assert _block()["iteration"] == 1223
        assert _block()["type"] == "B"

    def test_author_and_goal(self):
        b = _block()
        assert b["author"] == "Kit (with Ray)"
        assert b["goal_id"] == "goal_54093bda4145"

    def test_yaml_loads_cleanly(self):
        # The whole journalists.yaml must still parse after the append.
        data = _load_journalists()
        assert isinstance(data, dict)
        assert len(data) >= 49


# ---------------------------------------------------------------------------
# 5. m965 content discipline (arms, quotes, tones, financial context).
# ---------------------------------------------------------------------------

class TestM965ContentDiscipline1223:
    def test_meta_arm_identity(self):
        arm = _block()["meta_arm"]
        assert arm["entity"] == "meta"
        assert arm["author_byline"] == "Allison Johnson"
        assert arm["outlet"] == "the-verge"
        assert arm["date"] == "2026-09-23"
        assert "cute little guy" in arm["title"]
        assert "spending my money" in arm["title"]

    def test_meta_arm_tone(self):
        arm = _block()["meta_arm"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.20

    def test_meta_arm_key_quotes(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "spending my money" in joined
        assert "massive caveat" in joined
        assert "Marley" in joined

    def test_openai_arm_identity(self):
        arm = _block()["openai_arm"]
        assert arm["entity"] == "openai"
        assert arm["author_byline"] == "Allison Johnson"
        assert arm["outlet"] == "the-verge"
        assert arm["date"] == "2026-10-02"
        assert "Dot agent is enterprise software" in arm["title"]

    def test_openai_arm_tone(self):
        arm = _block()["openai_arm"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == 0.25

    def test_openai_arm_explicit_comparison_quote(self):
        # The journalist herself performs the cross-entity contrast in the
        # OpenAI piece; this is the load-bearing quote of the mechanism.
        quotes = _block()["openai_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "unlike the ultra-approachable Meta Muse" in joined
        assert "workplace software" in joined

    def test_openai_arm_byline_bound_stated(self):
        # Bounded byline-certainty: the OpenAI arm rests on the photo
        # credit + first-person voice, not a canonical byline; the block
        # must say so.
        tier = _block()["openai_arm"]["evidence_tier"]
        assert "bounded byline-certainty" in tier

    def test_scorer_delta(self):
        s = _block()["scorer"]
        assert s["meta_tone"] == -0.20
        assert s["openai_tone"] == 0.25
        assert s["illustrative_delta_openai_minus_meta"] == 0.45
        assert s["delta_calc"] == "(0.25) - (-0.20) = +0.45"

    def test_financial_context_m494(self):
        ctx = _block()["financial_context"]
        assert "mechanism 494" in ctx
        assert "May 29 2024" in ctx
        assert "OpenAI-only" in ctx
        assert "Meta pays Vox $0" in ctx

    def test_evidence_tier_excerpt(self):
        for arm_key in ("meta_arm", "openai_arm"):
            tier = _block()[arm_key]["evidence_tier"]
            assert "EXCERPT-TIER" in tier
            assert "0 browser.open per #503" in tier

    def test_both_arms_new_this_run(self):
        for arm_key in ("meta_arm", "openai_arm"):
            assert "NEW this run" in _block()[arm_key]["status"]


# ---------------------------------------------------------------------------
# 6. Statistical discipline (Aug 28 2026 standing rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1223:
    def test_no_p_values(self):
        s = _block()["scorer"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"
        assert s["is_significant"] is False

    def test_engine_not_run(self):
        s = _block()["scorer"]
        assert s["engine_run"] is False
        assert "engine NOT run" in s["statistical_discipline"]

    def test_manual_illustrative_only(self):
        disc = _block()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in disc
        assert "Aug 28 2026 standing rule" in disc
        assert "NOT artifact-grade" in disc

    def test_no_analysis_json_update(self):
        b = _block()
        assert b["no_analysis_json_update"] is True
        assert b["is_significant"] is False
        assert b["correlation_not_causation"] is True


# ---------------------------------------------------------------------------
# 7. Falsification ledger (holds at 50; this run is a confirming case,
# NOT a member).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1223:
    def test_is_a_confirming_case_not_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 50
        assert b["verdict"] == "confirming_extension_of_m494_not_a_discovery"

    def test_forty_eighth_intact_in_ft(self):
        # Prior member untouched: the forty-eighth claim form stays
        # exactly in financial-times.yaml m952 (2 occurrences).
        text = _read(os.path.join(PROFILES_DIR, "financial-times.yaml"))
        assert text.count(FORTY_EIGHTH_MEMBER) == 2

    def test_forty_eighth_nowhere_else(self):
        for p in _needle_hits_profiles(FORTY_EIGHTH_MEMBER):
            assert p.endswith("financial-times.yaml"), p

    def test_forty_ninth_intact_in_journalists(self):
        # Prior member untouched: the forty-ninth claim form stays
        # exactly in journalists.yaml m956 (3 occurrences).
        text = _read(JOURNALISTS_PATH)
        assert text.count(FORTY_NINTH_MEMBER) == 3

    def test_fiftieth_intact_in_journalists(self):
        # Prior member untouched: the fiftieth claim form stays
        # exactly in journalists.yaml m959 (3 occurrences). This run
        # does not add a member; it holds the ledger.
        text = _read(JOURNALISTS_PATH)
        assert text.count(FIFTIETH_MEMBER) == 3

    def test_fifty_first_absent(self):
        assert _needle_hits_profiles(FIFTY_FIRST_MEMBER) == []
        for p in _iter_source_files():
            if p.endswith(".py") and os.path.basename(p) != OWN_BASENAME:
                assert FIFTY_FIRST_MEMBER not in open(
                    p, encoding="utf-8", errors="replace"
                ).read(), p

    def test_directions_thirty_fifth_through_thirty_ninth_present(self):
        for needle in (
            THIRTY_FIFTH_DIR,
            THIRTY_SIXTH_DIR,
            THIRTY_SEVENTH_DIR,
            THIRTY_EIGHTH_DIR,
            THIRTY_NINTH_DIR,
        ):
            assert _needle_hits_profiles(needle) != [], needle

    def test_fortieth_direction_absent(self):
        assert _needle_hits_profiles(FORTIETH_DIR) == []

    def test_ledger_note_holds_at_50(self):
        note = _block()["ledger_note"]
        assert "Ledger HOLDS at 50" in note
        assert "fifty-first member-claim form absent repo-wide" in note


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (designed lifecycle; the #1224 Type C run
# pins the 966 landing; #1222's no-fifty-first / no-fortieth pins stay
# green through this run).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1223:
    def test_zero_966_guards_are_forward(self):
        # NEXT_NUM=966 stays forward: no 966 keys land this run.
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FORTIETH_DIR) not in src
        assert len(FORTIETH_DIR) > 0

    def test_no_fifty_first_member_guard(self):
        # The fifty-first form is not landed here; it must not appear
        # contiguously in this file either.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FIFTY_FIRST_MEMBER) not in src
        assert len(FIFTY_FIRST_MEMBER) > 0

    def test_no_fiftieth_member_guard(self):
        # The landed fiftieth form lives in the YAML block, not here.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FIFTIETH_MEMBER) not in src
        assert len(FIFTIETH_MEMBER) > 0

    def test_1222_pins_flip_by_design_documented(self):
        # #1222's test_zero_965_guards_are_forward pin (NEXT_NUM=965) and
        # its no-Type-B-#1223-in-git-log pin flip BY DESIGN at this run:
        # m965 is landed in profiles/careers/journalists.yaml and this
        # commit carries "Type B #1223" once committed (post-commit). #1222's
        # fortieth-absent, forty-ninth-intact, fiftieth-intact, and
        # fifty-first-absent guards stay green through this run - verified
        # by the ledger tests above. Recorded, not repaired.
        b = _block()
        assert b["falsification_family_member"] is False
        log = _git(
            "log", "--oneline", "--grep=Type A #1222:"
        ).stdout
        assert "Type A #1222" in log or ANCHORED_SHA == "0" * 40


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this run's pins for #1224).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1223:
    def test_pins_on_965_landing(self):
        # The guards this run lays for the next leg: max-965, zero-966
        # numeric, no-Type-C-#1224-in-git-log.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 965" in src
        assert "NEXT_NUM = 966" in src

    def test_no_type_c_1224_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type C #1224").stdout
        assert log.strip() == ""

    def test_966_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1222_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1222))

    def test_johnson_key_unique(self):
        data = _load_journalists()
        assert list(data.keys()).count("allison_johnson_type_b") == 1


# ---------------------------------------------------------------------------
# 10. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1225).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1223:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1220_full_suite.log" in src

    def test_suite_checked_only_recorded_not_touched(self):
        # This run stays on targeted verification per the Type B brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest observation per #795:
        # #1220-launched suite at the 23:00 PDT check (336 bytes,
        # mtime Oct 4 21:15 PDT, ~105 min stale, no pytest process alive,
        # zero processes holding the log open per the /proc open-fd check
        # - an observation, not a verdict). #1225 owns the verdict.
        status = _block()["background_suite_status"]
        assert "CHECKED ONLY" in status
        assert "no pytest process" in status
        assert "#1225" in status

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries none of this run's
        # markers.
        suite_log = os.path.expanduser(
            "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
            "hidden_files/type_d_1220_full_suite.log"
        )
        log = _read(suite_log)
        assert "Type B #1223" not in log
        assert "allison_johnson" not in log


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch). Deselected by design
# in the in-gate until the doc-sync followup lands.
# ---------------------------------------------------------------------------

class TestDocSync1223:
    def test_readme_stats_table_updated(self):
        # Current README stats-line convention (per #1217): "| Tests | N |
        # Across M test files |" - no slash form; assert the count and
        # file count both appear.
        text = _read(os.path.join(REPO, "README.md"))
        assert "| Tests |" in text
        assert str(README_TEST_COUNT) in text
        assert str(README_FILE_COUNT) in text

    def test_readme_test_table_row_present(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert OWN_BASENAME in text

    def test_architecture_tree_row_present(self):
        text = _read(os.path.join(REPO, "docs", "ARCHITECTURE.md"))
        assert OWN_BASENAME in text

    def test_iteration_log_entry_present(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1223 Type B" in text

    def test_doc_sync_constants_match_collect(self):
        assert COLLECTED_NEW_TESTS > 0
        assert README_TEST_COUNT == 66148 + COLLECTED_NEW_TESTS
        assert README_FILE_COUNT == 1548


# ---------------------------------------------------------------------------
# 12. Iteration log (per #721). Deselected by design until the log-hash
# followup registers all four hashes.
# ---------------------------------------------------------------------------

class TestIterationLog1223:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1223 Type B" in text

    def test_no_duplicate_1223_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1223 Type B") == 1

    def test_window_fourth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "FOURTH leg" in text
        assert "ledger holds at 50" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation (concurrency: leave other crons' working tree
# alone; do NOT touch #1024 m846).
# ---------------------------------------------------------------------------

class TestInflightIsolation1223:
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
            assert "mechanism_id: 965" not in diff, path
            assert "Type B #1223" not in diff, path

    def test_m846_untouched(self):
        diff = _git("diff", "--", "profiles/competitor-entities.yaml").stdout
        assert "m846" not in diff
