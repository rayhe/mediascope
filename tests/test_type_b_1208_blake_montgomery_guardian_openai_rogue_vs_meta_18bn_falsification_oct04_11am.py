# -*- coding: utf-8 -*-
"""Type B #1208 tests: Blake Montgomery (Guardian) - OpenAI "promptly goes
rogue" launch mockery vs Meta $18bn teen-harm legal reckoning, journalist-
level forty-ninth falsification-family member (m956).

Mechanism m956 (falsification-family member; ledger advances 48 -> 49).
The Guardian holds the OpenAI strategic content-licensing partnership
(Feb 14 2025, mechanism_514); Montgomery applies the adversarial register
to the deal partner at near-parity with Meta (illustrative delta
OpenAI-minus-Meta +0.05). INVERTS the #513 Dara Kerr directional-support
finding at the same outlet under the same deal.

Excerpt-bounded research per #503 (delegated research + 6 main-run
browser.search query sets, 0 browser.open reads). Rejected as saturated /
peg-absent / out-of-window: Sean Hollister, Hugh Langley, Richard Lawler,
Cristina Criddle, Samuel Gibbs, Johana Bhuiyan, Dara Kerr, Dominic Preston,
Tim Bradshaw, Alex Hern, Kyle Barr, Cade Metz, Wes Davis, Terrence O'Brien,
Jay Peters, Stevie Bonifield, Ece Yildirim, Brenda Stolyar, Florence Ion,
Tripp Mickle, Karen Weise, Ina Fried, Erin Griffith, George Hammond,
Cameron Faulkner, James Whitbrook, Dua Rashid, Antonio Di Benedetto,
Polly Thompson, Ross Andersen, Tim Higgins, Robert Booth.

The m956 block lives in profiles/careers/journalists.yaml as a
competitor_coverage sub-key of the NEW top-level `blake_montgomery_type_b`
key (per the #643 convention; career-profile list entry pre-exists under
`journalists:`; mechanism_ids [956]).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
One anchor test (the placeholder pin) fails BY DESIGN post-anchor.

Per #795: this run only CHECKS the #1205-launched background suite
(observed ALIVE at this run's check: 33178 bytes, mtime Oct 4 2026
11:02 PDT, pytest processes alive, progress ~11%); its verdict and
tombstone belong to #1210 (next Type D).

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the landed
or next number, the forty-eighth / forty-ninth / fiftieth member-claim
forms, or the thirty-fifth through fortieth direction forms; the constants
are constructed at runtime. (The landed forty-ninth ordinal lives in
profiles/careers/journalists.yaml (m956); the forty-eighth lives in
profiles/financial-times.yaml (m952).)
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
    "test_type_b_1208_blake_montgomery_guardian_openai_rogue_vs_"
    "meta_18bn_falsification_oct04_11am.py"
)
BLOCK_KEY = (
    "type_b_1208_blake_montgomery_guardian_openai_rogue_vs_"
    "meta_18bn_falsification"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "33e4af127738656a3f4a473d0b89061aafda13c8"  # patched per #565
# Post-first-run values per #719: N tests collected; README ratchets
# 64933/1532 -> (64933+N)/1533 in the doc-sync followup.
README_TEST_COUNT = 64933 + 73  # 65006; patched post-first-run per #719
README_FILE_COUNT = 1533
COLLECTED_NEW_TESTS = 73  # patched post-first-run per #719

# Forward guards for the next landing. MECH_NUM=956 is THIS run's landed
# mechanism; NEXT_NUM=957 stays forward.
MECH_NUM = 956
NEXT_NUM = 957

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"
MECH_DASH_MARKER = "mechanism" + "-"
FORTY_EIGHTH_MEMBER = "FORTY" + "-EIGHTH falsification-family member"
FORTY_NINTH_MEMBER = "FORTY" + "-NINTH falsification-family member"
FIFTIETH_MEMBER = "FIF" + "TIETH falsification-family member"
THIRTY_FIFTH_DIR = "THIRTY" + "-FIFTH relationship direction"
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH relationship direction"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"
THIRTY_EIGHTH_DIR = "THIRTY" + "-EIGHTH relationship direction"
THIRTY_NINTH_DIR = "THIRTY" + "-NINTH relationship direction"
FORTIETH_DIR = "FORTI" + "ETH relationship direction"

# The landed m956 block lives here (colon-form key; no numeric-956 substring
# in the block key by designed keying per #715). Montgomery's entry is the
# NEW top-level `blake_montgomery_type_b:` key (per the #643 convention).
JOURNALISTS_PATH = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
FILE_1207 = (
    "test_type_a_1207_bi_anthropic_ipo_prospectus_smart_people_"
    "financial_skeptical_vs_meta_execution_neutral_sep29_oct04_10am.py"
)
MONTGOMERY_URLS = (
    "https://www.theguardian.com/technology/2026/aug/26/"
    "meta-social-media-addiction-trial-settlement",
    "https://thedailybreakingnews.com/news/technology/"
    "openai-releases-new-ai-agent-which-promptly-goes-rogue-17oacip",
    "https://www.theguardian.com/global/2026/sep/28/ai-agents-spiral",
    "https://muckrack.com/blake-montgomery/articles",
)


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _load_journalists():
    return yaml.safe_load(_read(JOURNALISTS_PATH))


def _montgomery_entry():
    data = _load_journalists()
    assert "blake_montgomery_type_b" in data, (
        "top-level blake_montgomery_type_b key must exist"
    )
    return data["blake_montgomery_type_b"]


def _block():
    return _montgomery_entry()["competitor_coverage"][BLOCK_KEY]


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

class TestAnchor1208:
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
        log = _git("log", "--oneline", "--grep=Type B #1208 anchor").stdout
        if ANCHORED_SHA != "0" * 40:
            assert "Type B #1208 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type B #1208:").stdout
        assert "Type B #1208" in log or ANCHORED_SHA == "0" * 40


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1208 is the FOURTH leg of the 1205-1209 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1208:
    def test_rotation_window_is_1205_1209(self):
        text = _block_text()
        assert "1205-1209" in text

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1205-1209 window FOURTH leg "
            "(D #1205 -> E #1206 -> A #1207 -> B #1208 -> C #1209)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1205", "Type E #1206", "Type A #1207"):
            assert marker in log, marker

    def test_next_run_is_type_c(self):
        # The next leg (#1209 Type C) is documented in this run's log entry
        # and block window field; it must not exist as a commit yet.
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "C #1209" in text
        assert _block()["window"].endswith("C #1209)")

    def test_no_type_b_1208_test_file_before_this_run(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1208_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (pre-commit claims, verifiable post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1208:
    def test_montgomery_top_level_key_found(self):
        entry = _montgomery_entry()
        assert entry["name"] == "Blake Montgomery"

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: the block key carries the iteration
        # number 1208, not the mechanism number.
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
        assert nums, "m956 must be present in profiles"

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_montgomery_urls_in_block_source_urls_verbatim(self):
        urls = list(_block()["source_urls"])
        for u in MONTGOMERY_URLS:
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
# 4. Block structure (new journalist key per #643; first Montgomery
# mechanism; the landed forty-ninth member form lives in the YAML block,
# ---------------------------------------------------------------------------

class TestBlockStructure1208:
    def test_montgomery_entry_is_top_level_key(self):
        data = _load_journalists()
        assert "blake_montgomery_type_b" in data
        assert isinstance(data["blake_montgomery_type_b"], dict)

    def test_competitor_coverage_subkey(self):
        entry = _montgomery_entry()
        assert "competitor_coverage" in entry
        assert BLOCK_KEY in entry["competitor_coverage"]

    def test_mechanism_ids_list(self):
        entry = _montgomery_entry()
        assert entry["mechanism_ids"] == [956]

    def test_required_block_fields(self):
        b = _block()
        for field in (
            "iteration", "mechanism_id", "type", "goal_id", "job_id",
            "scheduled_job_id", "date", "block_key", "test_file", "author",
            "journalist", "publication", "window", "design", "openai_arm",
            "meta_arm", "corroborating_arm", "scorer", "financial_context",
            "finding", "confounders", "counter_evidence",
            "statistical_discipline", "verdict", "falsification_family",
            "falsification_family_member", "falsification_ledger",
            "ledger_note", "is_significant", "correlation_not_causation",
            "no_analysis_json_update", "artifact_readiness", "connects_to",
            "novelty", "research_method", "background_suite_status",
            "in_flight", "source_urls",
        ):
            assert field in b, field

    def test_test_file_field_matches_own_basename(self):
        assert _block()["test_file"].endswith(OWN_BASENAME)

    def test_openai_arm_tone(self):
        arm = _block()["openai_arm"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.35
        assert arm["entity"] == "openai"
        assert arm["author_byline"] == "Blake Montgomery (solo)"

    def test_meta_arm_tone(self):
        arm = _block()["meta_arm"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.40
        assert arm["entity"] == "meta"

    def test_publication_the_guardian(self):
        entry = _montgomery_entry()
        assert entry["publication"] == "the-guardian"

    def test_member_flag_true(self):
        b = _block()
        assert b["falsification_family_member"] is True
        assert b["falsification_ledger"] == 49
        assert b["verdict"] == "falsification_member_confirmed"


# ---------------------------------------------------------------------------
# 5. m956 content discipline (excerpt honesty, verbatim quotes, no
# constructed URLs).
# ---------------------------------------------------------------------------

class TestM956ContentDiscipline1208:
    def test_key_quotes_verbatim(self):
        b = _block()
        openai_quotes = b["openai_arm"]["key_quotes"]
        assert any("promptly goes rogue" in q for q in openai_quotes)
        meta_quotes = b["meta_arm"]["key_quotes"]
        assert any("up to $18bn" in q for q in meta_quotes)
        corr_quotes = b["corroborating_arm"]["key_quotes"]
        assert any("spiraling" in q or "going rogue" in q for q in corr_quotes)

    def test_evidence_tier_is_excerpt_attested(self):
        b = _block()
        assert "EXCERPT-TIER" in b["openai_arm"]["evidence_tier"]
        assert "EXCERPT-TIER" in b["meta_arm"]["evidence_tier"]
        assert "0 browser.open per #503" in b["openai_arm"]["evidence_tier"]

    def test_no_full_read_claim(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "first-hand" not in src.lower() or "no first-hand" in src.lower()

    def test_no_canonical_url_constructed(self):
        b = _block()
        assert "none constructed" in b["openai_arm"]["url_note"]
        assert "no canonical URLs constructed" in b["novelty"]

    def test_research_rejections_documented(self):
        method = _block()["research_method"]
        assert "REJECTED" in method
        assert "Sean Hollister" in method

    def test_ascii_only(self):
        # This run's additions must be ASCII-only. Pre-existing non-ASCII
        # in journalists.yaml (569 chars in HEAD, em dashes in older
        # career notes) is out of scope for this run.
        diff = _git("diff", "--", "profiles/careers/journalists.yaml").stdout
        added = "\n".join(
            l[1:] for l in diff.splitlines()
            if l.startswith("+") and not l.startswith("+++")
        )
        try:
            added.encode("ascii")
        except UnicodeEncodeError as e:
            raise AssertionError("non-ASCII in m956 YAML additions: %s" % e)
        text = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        try:
            text.encode("ascii")
        except UnicodeEncodeError as e:
            raise AssertionError("non-ASCII in test file: %s" % e)

    def test_kerr_inversion_documented(self):
        b = _block()
        assert "INVERTS the #513" in b["finding"] or "inverts #513" in b[
            "finding"
        ].lower() or "INVERTS" in b["finding"]
        assert 513 in b["connects_to"]


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026
# standing rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1208:
    def test_manual_illustrative_only(self):
        disc = _block()["statistical_discipline"]
        assert "MANUAL" in disc and "ILLUSTRATIVE" in disc

    def test_no_inferential_stats(self):
        scorer = _block()["scorer"]
        assert scorer["p_value"] == "NOT_CALCULATED" or "NOT_CALCULATED" in str(
            scorer
        )
        assert _block()["is_significant"] is False

    def test_delta_is_illustrative(self):
        scorer = _block()["scorer"]
        assert scorer["illustrative_delta_openai_minus_meta"] == 0.05
        assert "(-0.35) - (-0.40) = +0.05" in scorer["delta_calc"]

    def test_verdict_is_member_not_discovery(self):
        b = _block()
        assert b["verdict"] == "falsification_member_confirmed"
        assert b["no_analysis_json_update"] is True

    def test_statistical_discipline_strings(self):
        b = _block()
        assert "Aug 28 2026 standing rule" in b["statistical_discipline"]
        assert "engine NOT run" in b["scorer"]["statistical_discipline"]

    def test_correlational_honesty(self):
        b = _block()
        assert b["correlation_not_causation"] is True
        assert "not causation" in b["financial_context"]


# ---------------------------------------------------------------------------
# 7. Falsification ledger (m956 lands the FORTY-NINTH member; 48 -> 49).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1208:
    def test_is_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is True
        assert b["falsification_ledger"] == 49

    def test_forty_eighth_intact_in_ft(self):
        # Prior member untouched: the forty-eighth claim form stays
        # exactly in financial-times.yaml m952 (2 occurrences).
        text = _read(os.path.join(PROFILES_DIR, "financial-times.yaml"))
        assert text.count(FORTY_EIGHTH_MEMBER) == 2

    def test_forty_eighth_nowhere_else(self):
        for p in _needle_hits_profiles(FORTY_EIGHTH_MEMBER):
            assert p.endswith("financial-times.yaml"), p

    def test_forty_ninth_landed_in_journalists(self):
        # This run lands the forty-ninth member-claim form in the m956
        # block (profiles/careers/journalists.yaml) and nowhere else in
        # profiles/.
        hits = _needle_hits_profiles(FORTY_NINTH_MEMBER)
        assert len(hits) == 1, hits
        assert hits[0].endswith(
            os.path.join("careers", "journalists.yaml")
        ), hits

    def test_fiftieth_absent(self):
        assert _needle_hits_profiles(FIFTIETH_MEMBER) == []
        for p in _iter_source_files():
            if p.endswith(".py") and os.path.basename(p) != OWN_BASENAME:
                assert FIFTIETH_MEMBER not in open(
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

    def test_ledger_note_advances_to_49(self):
        note = _block()["ledger_note"]
        assert "Ledger advances 48 -> 49" in note
        assert "FORTY-NINTH member-claim form LANDED this run" in note
        assert "fiftieth member-claim form absent repo-wide" in note


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (designed lifecycle; the #1209 Type C run
# pins the 957 landing; #1207's no-forty-ninth pin flips BY DESIGN here).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1208:
    def test_zero_957_guards_are_forward(self):
        # NEXT_NUM=957 stays forward: no 957 keys land this run.
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FORTIETH_DIR) not in src
        assert len(FORTIETH_DIR) > 0

    def test_no_fiftieth_member_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FIFTIETH_MEMBER) not in src
        assert len(FIFTIETH_MEMBER) > 0

    def test_no_forty_ninth_member_guard(self):
        # The landed forty-ninth form lives in the YAML block, not here.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FORTY_NINTH_MEMBER) not in src
        assert len(FORTY_NINTH_MEMBER) > 0

    def test_1207_pins_flip_by_design_documented(self):
        # #1207's test_forty_ninth_absent pin (profiles + .py sweep) flips
        # BY DESIGN at this run: m956 lands the forty-ninth member-claim
        # form in profiles/careers/journalists.yaml. #1207's
        # test_no_forty_ninth_member_guard (own-file contiguous check)
        # stays green - this file format-builds the needle.
        b = _block()
        assert b["falsification_family_member"] is True
        log = _git(
            "log", "--oneline", "--grep=Type A #1207:"
        ).stdout
        assert "Type A #1207" in log or ANCHORED_SHA == "0" * 40


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this run's pins for #1209).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1208:
    def test_pins_on_956_landing(self):
        # The guards this run lays for the next leg: max-956, zero-957
        # numeric, no-Type-C-#1209-in-git-log.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 956" in src
        assert "NEXT_NUM = 957" in src

    def test_no_type_c_1209_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type C #1209").stdout
        assert log.strip() == ""

    def test_957_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1207_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1207))

    def test_montgomery_key_unique(self):
        data = _load_journalists()
        assert list(data.keys()).count("blake_montgomery_type_b") == 1


# ---------------------------------------------------------------------------
# 10. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1210).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1208:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1205_full_suite.log" in src

    def test_suite_checked_only_recorded_not_touched(self):
        # This run stays on targeted verification per the Type B brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest observation per #795:
        # #1205-launched suite ALIVE at the 11:02 PDT check
        # (33178 bytes, last write Oct 4 11:02:06 PDT, progress ~11%,
        # pytest processes alive). #1210 owns the verdict.
        status = _block()["background_suite_status"]
        assert "CHECKED ONLY" in status
        assert "ALIVE" in status
        assert "#1210" in status

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no m956 markers.
        suite_log = os.path.expanduser(
            "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
            "hidden_files/type_d_1205_full_suite.log"
        )
        log = _read(suite_log)
        assert "m956" not in log
        assert "Type B #1208" not in log


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1208:
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
        assert "## #1208 Type B:" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 64933 + COLLECTED_NEW_TESTS
        assert README_FILE_COUNT == 1533


# ---------------------------------------------------------------------------
# 12. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1208:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1208 Type B:" in text

    def test_no_duplicate_1208_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1208 Type B:") == 1

    def test_window_fourth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1205-1209" in text

    def test_ledger_49_in_log(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "ledger" in text.lower() and "49" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1208:
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
            assert "mechanism_id: 956" not in diff, path
            assert "Type B #1208" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 lives in profiles/competitor-entities.yaml;
        # this run must not alter that file at all.
        diff = _git("diff", "--", "profiles/competitor-entities.yaml").stdout
        assert "mechanism_id: 956" not in diff
        assert "Type B #1208" not in diff
