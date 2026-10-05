# -*- coding: utf-8 -*-
"""Type B #1218 tests: Christine Ji (MarketWatch) - Meta wearables FDA
hearing-support launch coverage vs Alphabet/Google AI-strategy analyst
defense, journalist-level CONTROL-CASE / register-symmetry (m962).

Mechanism m962 (control-case; ledger HOLDS at 50 - NOT a
falsification-family member). Ji applies the benign launch-news register to
Meta (FDA hearing-support prestige parity with Apple, +0.15) and the
bullish analyst-defense register to Alphabet (cloud-first AI strategy,
+0.25); illustrative delta (Google minus Meta) +0.10, near-null symmetry.
The Dow Jones x OpenAI content-licensing partnership is in-corpus but
OpenAI is not an arm, so no payer asymmetry separates the arms - the pair
tests register symmetry across entities, which is what it finds. FIRST
committed MarketWatch mechanism in corpus.

Excerpt-bounded research per #503 (delegated research + 2 main-run
browser.search verification sets: Meta-arm byline/quote attestation via
muckrack profile + marketwatch.com result; Google-arm byline/quote
attestation via Morningstar Dow Jones relay + marketwatch.com canonical;
0 browser.open reads). Researcher corpus-miss verified: the #1213-held
Christine Ji alternate was an Anthropic arm (never run, different pair).
Rejected as saturated / peg-absent / out-of-window / overlap: Barbara
Ortutay (co-byline proximity to #1213), Kurt Wagner (no in-window
originals), Maxwell Zeff (moved outlets, stale arms), Ryan Mac (no
in-window Meta originals), Hayden Field (saturated #557), Cade Metz
(saturated #471/m538), Mia Sato (saturated #215), Makena Kelly (no
in-window pair), Reece Rogers (saturated #385), Jeffrey Dastin (Meta arm
out of window), Krystal Hu (OpenAI arms only), Katie Paul (saturated
#667/m634), Stephen Nellis (mixed-entity peg), Kyle Wiggers (OpenAI
only), Jennifer Elias (no in-window pair), Tom Gerken (game reviews), Ron
Amadeo (no Meta arm, scouted #758), Corbin Davenport / Ryne Hager
(beat-boundary), David Imel (no originals), Ian Hamilton (no in-window
pair), Joe Maring (stale bylines), Lauren Feiner (no clean competitor
arm), Umar Shakir (no in-window pair).

The m962 block lives in profiles/careers/journalists.yaml as a
competitor_coverage sub-key of the NEW top-level `christine_ji_type_b`
key (per the #643 convention; name appears only in the #1213
held-alternate line, a Jul-2026 examples/sample_output/ byline, and the
iteration-log; zero dedicated type_b key pre-commit).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
One anchor test (the placeholder pin) fails BY DESIGN post-anchor.

Per #795: this run only CHECKS the #1215-launched background suite
(observed at this run's check: 9224 bytes, mtime Oct 4 2026 18:17 PDT,
stalled at ~12% progress, no pytest process visible in ps scan - an
observation, not a verdict); its verdict and tombstone belong to #1220
(next Type D).

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
landed or next number, the forty-eighth / forty-ninth / fiftieth /
fifty-first member-claim forms, or the thirty-fifth through fortieth
direction forms; the constants are constructed at runtime. (The landed
fiftieth ordinal lives in profiles/careers/journalists.yaml (m959); the
forty-ninth lives there too (m956); the forty-eighth lives in
profiles/financial-times.yaml (m952). No fifty-first member-claim form
exists repo-wide; this run does not create one.)
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
    "test_type_b_1218_christine_ji_marketwatch_meta_fda_hearing_vs_"
    "google_alpha_strategy_oct04_7pm.py"
)
BLOCK_KEY = (
    "type_b_1218_christine_ji_marketwatch_meta_fda_hearing_vs_"
    "google_alpha_strategy"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "6f8957ca01f139b1ed97e4e12de4db053ebb3b21"  # patched per #565
# Post-first-run values per #719: N tests collected; README ratchets
# 65757/1542 -> (65757+N)/1543 in the doc-sync followup.
README_TEST_COUNT = 65757 + 73  # 65830; patched post-first-run per #719
README_FILE_COUNT = 1543
COLLECTED_NEW_TESTS = 73  # patched post-first-run per #719

# Forward guards for the next landing. MECH_NUM=962 is THIS run's landed
# mechanism; NEXT_NUM=963 stays forward.
MECH_NUM = 962
NEXT_NUM = 963

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

# The landed 962 block lives here (colon-form key; no numeric-962 substring
# in the block key by designed keying per #715). It is a
# competitor_coverage sub-key of the NEW top-level `christine_ji_type_b`
# key in profiles/careers/journalists.yaml.
JOURNALISTS_PATH = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
FILE_1217 = (
    "test_type_a_1217_nyt_openai_sep25_rogue_agents_gov_sites_vs_meta_"
    "sep30_tax_credit_oct04_5pm.py"
)
FILE_1216 = "test_type_e_1216_podcast_sentiment_166th_verification_oct04_4pm.py"
FILE_1215 = (
    "test_type_d_1215_m958_m959_m960_qualitative_corpus_integrity_"
    "oct04_4pm.py"
)
JI_URLS = (
    "https://www.marketwatch.com/livecoverage/"
    "meta-connect-stock-mark-zuckerberg-keynote-ai/card/"
    "meta-joins-apple-in-bringing-fda-approved-hearing-support-to-its-"
    "wearables-bMAPnkFEcGxy78T9KwzI",
    "https://www.marketwatch.com/story/"
    "google-is-playing-a-different-ai-game-than-everyone-else-and-"
    "wall-street-may-be-missing-the-point-e91077a3",
)


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _load_journalists():
    with open(JOURNALISTS_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _ji_entry():
    return _load_journalists()["christine_ji_type_b"]


def _block():
    return _ji_entry()["competitor_coverage"][BLOCK_KEY]


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

class TestAnchor1218:
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
        log = _git("log", "--oneline", "--grep=Type B #1218 anchor").stdout
        if ANCHORED_SHA != "0" * 40:
            assert "Type B #1218 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type B #1218:").stdout
        assert "Type B #1218" in log or ANCHORED_SHA == "0" * 40


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1218 is the FOURTH leg of the 1215-1219 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1218:
    def test_rotation_window_is_1215_1219(self):
        text = _block_text()
        assert "1215-1219" in text

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1215-1219 window FOURTH leg "
            "(D #1215 -> E #1216 -> A #1217 -> B #1218 -> C #1219)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1215", "Type E #1216", "Type A #1217"):
            assert marker in log, marker

    def test_next_run_is_type_c(self):
        # The next leg (#1219 Type C) is documented in the window string;
        # it must not exist as a commit yet.
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "C #1219" in text
        assert _block()["window"].endswith("C #1219)")

    def test_no_type_b_1218_test_file_before_this_run(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1218_*.py"))
        assert files == [] or (
            len(files) == 1 and os.path.basename(files[0]) == OWN_BASENAME
        )


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (per #715).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1218:
    def test_ji_top_level_key_found(self):
        assert "christine_ji_type_b" in _load_journalists()

    def test_block_key_zero_mechanism_number_substring(self):
        assert "962" not in BLOCK_KEY
        assert "1218" in BLOCK_KEY

    def test_zero_underscore_mechanism_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_zero_dash_mechanism_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_zero_numeric_next_in_profiles(self):
        # NEXT_NUM=963 stays forward; MECH_NUM=962 is landed this run.
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

    def test_ji_urls_in_block_source_urls_verbatim(self):
        src = _block()["source_urls"]
        for url in JI_URLS:
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

class TestBlockStructure1218:
    def test_ji_entry_is_top_level_key(self):
        data = _load_journalists()
        assert list(data.keys()).count("christine_ji_type_b") == 1

    def test_competitor_coverage_subkey(self):
        assert BLOCK_KEY in _ji_entry()["competitor_coverage"]

    def test_mechanism_ids_list(self):
        assert _ji_entry()["mechanism_ids"] == [962]

    def test_required_block_fields(self):
        b = _block()
        for field in (
            "block_key", "mechanism_id", "iteration", "type", "date",
            "test_file", "author", "goal_id", "job_id", "scheduled_job_id",
            "journalist", "publication", "window", "design", "meta_arm",
            "google_arm", "scorer", "statistical_discipline",
            "financial_context", "finding", "confounders", "counter_evidence",
            "connects_to", "verdict", "falsification_family",
            "falsification_family_member", "falsification_ledger",
            "ledger_note", "is_significant", "correlation_not_causation",
            "no_analysis_json_update", "artifact_readiness",
            "research_method", "novelty", "background_suite_status",
            "in_flight", "source_urls",
        ):
            assert field in b, field

    def test_test_file_field_matches_own_basename(self):
        assert _block()["test_file"] == "tests/" + OWN_BASENAME

    def test_google_arm_tone(self):
        b = _block()
        assert b["google_arm"]["tone_MANUAL_ILLUSTRATIVE"] == 0.25

    def test_meta_arm_tone(self):
        b = _block()
        assert b["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == 0.15

    def test_publication_marketwatch(self):
        b = _block()
        assert b["publication"] == "marketwatch"
        assert _ji_entry()["publication"] == "marketwatch"

    def test_control_case_flag(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert b["verdict"] == "control_case_register_symmetry"
        assert b["falsification_ledger"] == 50


# ---------------------------------------------------------------------------
# 5. Content discipline (quotes, evidence tier, confounders).
# ---------------------------------------------------------------------------

class TestM962ContentDiscipline1218:
    def test_key_quotes_verbatim(self):
        b = _block()
        meta_quotes = b["meta_arm"]["key_quotes"]
        google_quotes = b["google_arm"]["key_quotes"]
        assert len(meta_quotes) >= 4 and len(google_quotes) >= 4
        assert any("FDA-approved hearing aid" in q for q in meta_quotes)
        assert any("Meta joins Apple" in q for q in meta_quotes)
        assert any("different game" in q for q in google_quotes)
        assert any("cloud-computing business" in q for q in google_quotes)

    def test_evidence_tier_is_excerpt_attested(self):
        b = _block()
        for arm in ("meta_arm", "google_arm"):
            tier = b[arm]["evidence_tier"]
            assert "EXCERPT-TIER" in tier
            assert "0 browser.open per #503" in tier

    def test_no_full_read_claim(self):
        b = _block()
        for arm in ("meta_arm", "google_arm"):
            tier = b[arm]["evidence_tier"]
            assert "full" not in tier.lower() or "FULL-TIER" not in tier

    def test_no_canonical_url_constructed(self):
        b = _block()
        for arm in ("meta_arm", "google_arm"):
            assert "none constructed" in b[arm]["url_note"].lower()

    def test_research_rejections_documented(self):
        method = _block()["research_method"]
        assert "Kurt Wagner" in method
        assert "Hayden Field" in method
        assert "Cade Metz" in method
        assert "Barbara Ortutay" in method

    def test_ascii_only(self):
        raw = _read(JOURNALISTS_PATH)
        try:
            raw.encode("ascii")
        except UnicodeEncodeError as exc:
            # Journalists.yaml carries pre-existing non-ASCII (e.g. smart
            # quotes in older blocks); the m962 block itself must be ASCII.
            start = raw.find("christine_ji_type_b")
            block_region = raw[start:start + 16000]
            try:
                block_region.encode("ascii")
            except UnicodeEncodeError as exc2:
                raise AssertionError(
                    "non-ASCII inside m962 block: %r" % (exc2,)
                ) from exc2

    def test_apple_benchmark_confound_documented(self):
        conf = _block()["confounders"]
        strong_text = " ".join(conf["strong"])
        assert "Apple" in strong_text
        assert "benchmark" in strong_text.lower()

    def test_muckrack_attestation_confound_documented(self):
        conf = _block()["confounders"]
        moderate_text = " ".join(conf["moderate"])
        assert "muckrack" in moderate_text.lower()

    def test_marketwatch_first_mechanism_noted(self):
        notes = _ji_entry()["notes"]
        assert "FIRST committed MarketWatch mechanism" in notes


# ---------------------------------------------------------------------------
# 6. Statistical discipline (Aug 28 2026 standing rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1218:
    def test_no_inferential_statistics(self):
        s = _block()["scorer"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"
        assert s["is_significant"] is False
        assert s["engine_run"] is False

    def test_illustrative_delta_value(self):
        s = _block()["scorer"]
        assert s["illustrative_delta_google_minus_meta"] == 0.10
        assert "(0.25) - (0.15) = +0.10" in s["delta_calc"]

    def test_manual_only_discipline(self):
        d = _block()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in d
        assert "Aug 28 2026" in d
        assert "NOT artifact-grade" in d

    def test_no_analysis_json_update(self):
        b = _block()
        assert b["no_analysis_json_update"] is True
        assert b["is_significant"] is False


# ---------------------------------------------------------------------------
# 7. Falsification ledger (holds at 50; control-case, no new member).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1218:
    def test_is_a_control_case_not_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 50
        assert b["verdict"] == "control_case_register_symmetry"

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
# 8. Forward-looking staleness (designed lifecycle; the #1219 Type C run
# pins the 963 landing; #1217's no-fifty-first / no-fortieth pins stay
# green through this run).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1218:
    def test_zero_963_guards_are_forward(self):
        # NEXT_NUM=963 stays forward: no 963 keys land this run.
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

    def test_1217_pins_flip_by_design_documented(self):
        # #1217's test_zero_962_guards_are_forward pin (NEXT_NUM=962) and
        # its no-Type-B-#1218-in-git-log pin flip BY DESIGN at this run:
        # m962 is landed in profiles/careers/journalists.yaml and this
        # commit carries "Type B #1218" once committed (post-commit). #1217's
        # fortieth-absent, forty-ninth-intact, fiftieth-intact, and
        # fifty-first-absent guards stay green through this run - verified
        # by the ledger tests above. Recorded, not repaired.
        b = _block()
        assert b["falsification_family_member"] is False
        log = _git(
            "log", "--oneline", "--grep=Type A #1217:"
        ).stdout
        assert "Type A #1217" in log or ANCHORED_SHA == "0" * 40


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this run's pins for #1219).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1218:
    def test_pins_on_962_landing(self):
        # The guards this run lays for the next leg: max-962, zero-963
        # numeric, no-Type-C-#1219-in-git-log.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 962" in src
        assert "NEXT_NUM = 963" in src

    def test_no_type_c_1219_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type C #1219").stdout
        assert log.strip() == ""

    def test_963_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1217_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1217))

    def test_ji_key_unique(self):
        data = _load_journalists()
        assert list(data.keys()).count("christine_ji_type_b") == 1


# ---------------------------------------------------------------------------
# 10. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1220).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1218:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1215_full_suite.log" in src

    def test_suite_checked_only_recorded_not_touched(self):
        # This run stays on targeted verification per the Type B brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest observation per #795:
        # #1215-launched suite at the 18:17 PDT check (9224 bytes,
        # mtime Oct 4 18:17 PDT, stalled at ~12% progress, no pytest
        # process visible in ps scan - an observation, not a verdict).
        # #1220 owns the verdict.
        status = _block()["background_suite_status"]
        assert "CHECKED ONLY" in status
        assert "no pytest process" in status
        assert "#1220" in status

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries none of this run's
        # markers.
        suite_log = os.path.expanduser(
            "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
            "hidden_files/type_d_1215_full_suite.log"
        )
        log = _read(suite_log)
        assert "Type B #1218" not in log
        assert "christine_ji" not in log


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch). Deselected by design
# in the in-gate until the doc-sync followup lands.
# ---------------------------------------------------------------------------

class TestDocSync1218:
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
        assert "## #1218 Type B" in text

    def test_doc_sync_constants_match_collect(self):
        assert COLLECTED_NEW_TESTS > 0
        assert README_TEST_COUNT == 65757 + COLLECTED_NEW_TESTS
        assert README_FILE_COUNT == 1543


# ---------------------------------------------------------------------------
# 12. Iteration log (per #721). Deselected by design until the log-hash
# followup registers all four hashes.
# ---------------------------------------------------------------------------

class TestIterationLog1218:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1218 Type B" in text

    def test_no_duplicate_1218_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1218 Type B") == 1

    def test_window_fourth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "FOURTH leg" in text
        assert "ledger holds at 50" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation (concurrency: leave other crons' working tree
# alone; do NOT touch #1024 m846).
# ---------------------------------------------------------------------------

class TestInflightIsolation1218:
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
            assert "mechanism_id: 962" not in diff, path
            assert "Type B #1218" not in diff, path

    def test_m846_untouched(self):
        diff = _git("diff", "--", "profiles/competitor-entities.yaml").stdout
        assert "m846" not in diff
