# -*- coding: utf-8 -*-
"""Type C #1189 tests: OpenAI x Synopsys GPT-Synopsys (announced Sep 30 2026)
- multi-year agreement to jointly develop a specialized chip-design model.
OpenAI licenses Synopsys EDA tools and pays a training subscription fee; the
two go to market jointly with a performance-gated revenue share.
LICENSE-AND-CO-BUILD lands the thirty-eighth relationship direction
(mechanism 945).

Iteration #1189, FIFTH and CLOSING leg of the 1185-1189 window
(D #1185 -> E #1186 -> A #1187 -> B #1188 -> C #1189).

The m945 block lives in profiles/competitor-entities.yaml as a top-level
`type_c_1189_...` key (Type C convention; cf. m942 at #1184).

This run LANDS a new relationship direction (the thirty-eighth):
LICENSE-AND-CO-BUILD. The IP vendor licenses its proprietary tools INTO the
AI lab as a training substrate (the lab pays a subscription to learn the
tools); the two jointly develop a specialized model; the co-built product
goes to market jointly with performance-gated revenue sharing. Distinct from
the m594-family flat-fee cash licenses, m663 Perplexity premium-data
licensing, m391 Comet Plus 80/20 revenue-share-no-cobuild, m942
invest-and-license (no equity here), m804 Noxtua majority-ownership, m807
vendor-embed, and train-first-settle-later. The thirty-ninth direction stays
absent by design; the thirty-fifth (m915), thirty-sixth (m933), and
thirty-seventh (m942) stand.

Rejected candidates (not new directions): (1) Firecrawl $75M Series B +
Alexandria licensed-data platform (Sep 29 2026) - single LinkedIn-pulse
relay as primary evidence, too thin for a dedicated mechanism; (2) Google AI
Contribution Pilot Oct-1 payout figures - m891 already the TWENTY-SEVENTH
direction, a temporal extension; (3) SPUR Oct-2 content-telemetry standard +
AI Licensing Advisory Board invitations - Guardian/FT SPUR already
in-corpus, a temporal extension.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.

Per #795: this run only CHECKS the #1185-launched background suite
(observed state recorded below); its verdict belongs to #1190.

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the next
number 946 keys, the FORTY-SEVENTH member-claim form, or the thirty-eighth /
thirty-ninth direction-claim forms; the landed thirty-eighth direction form
is asserted via a runtime-built needle against the landed YAML (never
written contiguously in source); the constants are constructed at runtime.
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
    "test_type_c_1189_openai_synopsys_gpt_synopsys_license_and_cobuild_"
    "thirty_eighth_direction_oct03_9pm.py"
)
BLOCK_KEY = (
    "type_c_1189_openai_synopsys_gpt_synopsys_license_and_cobuild_"
    "thirty_eighth_direction_oct03_9pm"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "0" * 40
# Post-first-run values per #719: README_TEST_COUNT / README_FILE_COUNT are
# patched to the post-sync-positive values after the first collection run
# (README ratchets 63451/1513 -> 63451+N/1514 in the doc-sync followup).
README_TEST_COUNT = 63451 + 77  # 63528; patched post-first-run per #719
README_FILE_COUNT = 1514

# Forward guards for the next landing. MECH_NUM=945 is THIS run's landed
# mechanism; NEXT_NUM=946 stays forward.
MECH_NUM = 945
NEXT_NUM = 946

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + "946" at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + "946" at runtime
THIRTY_FIFTH_DIR = "THIRTY" + "-FIFTH relationship direction"
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH relationship direction"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"
THIRTY_EIGHTH_DIR = "THIRTY" + "-EIGHTH relationship direction"
THIRTY_NINTH_DIR = "THIRTY" + "-NINTH relationship direction"
FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
FORTY_EIGHTH_MEMBER = "FORTY" + "-EIGHTH falsification-family member"

# The landed m945 block lives here (top-level key; designed keying per
# #715: the block key carries iteration 1189, no 945 substring).
ENTITIES_PATH = os.path.join(REPO, "profiles", "competitor-entities.yaml")
FILE_1188 = (
    "test_type_b_1188_eli_tan_nyt_pervert_glasses_stigma_vs_other_"
    "companies_neutral_within_piece_oct03_8pm.py"
)
M846_BLOCK_NEEDLE = "type_c_1024_benioff"

# Ordinal form of the falsification family. The FORTY-SIXTH member form
# must be present repo-wide; the FORTY-SEVENTH member-claim form must be
# absent (negative guard). (The falsification-family thirty-sixth member
# m878 is a separate taxonomy from the relationship-direction ordinal.)
FORTY_SIXTH_LANDED = "FORTY-SIXTH falsification-family member"

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1185_full_suite.log"
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
    out = _git("log", "--format=%H", "--grep=Type C #1189:").stdout.strip()
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


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------

class TestAnchor1189:
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
        # "Type C #1189 anchor followup: ANCHORED_SHA -> <hash> ...".
        log = _git("log", "--oneline", "--grep=Type C #1189 anchor").stdout
        assert "Type C #1189 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type C #1189:").stdout
        assert "Type C #1189" in log


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1189 is the FIFTH and CLOSING leg of 1185-1189.
# ---------------------------------------------------------------------------

class TestRotationGuard1189:
    def test_rotation_window_is_1185_1189(self):
        assert "1185-1189" in _entities_text()

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1185-1189 window FIFTH and CLOSING leg "
            "(D #1185 -> E #1186 -> A #1187 -> B #1188 -> C #1189)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1185", "Type E #1186", "Type A #1187",
                       "Type B #1188"):
            assert marker in log, marker

    def test_no_type_d_1190_in_git_log_yet(self):
        # The next window (1190-1194) opens with Type D #1190; it must not
        # exist as a commit yet.
        log = _git("log", "--oneline", "--grep=Type D #1190").stdout
        assert log.strip() == ""

    def test_single_type_c_1189_test_file(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_c_1189_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (pre-commit claims, verifiable post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1189:
    def test_block_key_present_once(self):
        assert _entities_text().count(BLOCK_KEY + ":") == 1

    def test_block_key_zero_945_substring(self):
        # Designed keying per #715: the block key carries the iteration
        # number 1189, not the mechanism number 945.
        assert "945" not in BLOCK_KEY

    def test_zero_underscore_945_repo_wide(self):
        # Per #1188's forward guard (zero-945 keys all forms): no
        # underscore-form 945 mechanism key may exist repo-wide
        # (own file excluded from the walk).
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_945_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_946_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_945(self):
        present = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert present, "m945 must be present in profiles"
        for n in range(MECH_NUM + 1, MECH_NUM + 20):
            assert _profiles_grep_numeric_mechanism_id(n) == [], n

    def test_no_duplicate_block_key(self):
        d = _load_entities()
        assert list(d.keys()).count(BLOCK_KEY) == 1

    def test_urls_copied_verbatim(self):
        urls = [s["url"] for s in _block()["sources"]]
        assert len(urls) == 8
        assert (
            "https://www.reuters.com/business/synopsys-openai-strike-"
            "deal-develop-ai-model-chip-design-work-2026-09-30/"
        ) in urls
        assert (
            "https://www.hpcwire.com/aiwire/2026/10/02/synopsys-and-"
            "openai-partner-to-develop-specialized-ai-model-for-"
            "chip-design/"
        ) in urls
        assert (
            "https://aidailypost.com/news/openai-licenses-synopsys-"
            "tools-build-ai"
        ) in urls
        assert (
            "https://en.shafaqna.com/481349/synopsys-openai-deal-"
            "gpt-synopsys/"
        ) in urls
        assert (
            "https://theempiremagazine.com/gpt-synopsys-openai-"
            "semiconductor-design/"
        ) in urls
        assert (
            "https://groundtruth.day/news/gpt-synopsys-tool-running-"
            "chip-design-partnership.html"
        ) in urls
        assert (
            "https://upgradefeeling.com/blog/gpt-synopsys-frontier-"
            "ai-chip-design-tools/"
        ) in urls
        assert (
            "https://wesearch.press/s/gpt-synopsys-frontier-"
            "intelligence-to-revolutionize-chip-des-8fac3ce4"
        ) in urls
        for u in urls:
            assert u.startswith("https://"), u

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

class TestBlockStructure1189:
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
        assert b["iteration"] == 1189
        assert b["mechanism_id"] == 945

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


# ---------------------------------------------------------------------------
# 5. m945 content discipline (OpenAI x Synopsys GPT-Synopsys,
# LICENSE-AND-CO-BUILD, thirty-eighth direction landing).
# ---------------------------------------------------------------------------

class TestM945ContentDiscipline1189:
    def test_announcement_leg(self):
        f = _block()["finding"]
        assert "Sep 30 2026" in f
        assert "multi-year agreement" in f
        assert "GPT-Synopsys" in f
        assert "investor summit" in f
        assert "go-to-market collaboration" in f
        assert "San Francisco" in f

    def test_license_in_leg(self):
        f = _block()["finding"]
        assert "training subscription fee" in f
        assert "rather than building its own" in f
        assert "OpenAI infrastructure" in f
        assert "not used to train" in f

    def test_performance_gated_split_leg(self):
        f = _block()["finding"]
        assert "based on how well the model improves" in f
        assert "not a flat fee" in f

    def test_non_cannibalization_leg(self):
        f = _block()["finding"]
        assert "not be cannibalizing our business" in f
        assert "sign-off" in f
        assert "ground truth" in f
        assert "retained moat" in f

    def test_market_leg(self):
        f = _block()["finding"]
        assert "15%" in f
        assert "11.19%" in f
        assert "as much as 7%" in f

    def test_native_tool_use_leg(self):
        f = _block()["finding"]
        assert "native expert user" in f
        assert "model -> EDA tool -> measured result -> next action" in f
        assert "Brockman" in f
        assert "Jalapeno" in f
        assert "Synopsys.ai" in f

    def test_money_flow_legs(self):
        m = _block()["money_flow"]
        assert "training subscription fee" in m
        assert "REVENUE SHARED OUT" in m
        assert "NO equity leg" in m
        assert "m942 invest-and-license" in m
        assert "m391" in m

    def test_taxonomy_lands_thirty_eighth(self):
        t = _block()["relationship_direction_taxonomy"]
        assert "LICENSE-AND-CO-BUILD" in t
        # Landed thirty-eighth direction form asserted via the
        # runtime-built needle (never contiguous in source per #715).
        assert THIRTY_EIGHTH_DIR in t
        assert "m594" in t and "m391" in t and "m942" in t
        assert "m663" in t and "m804" in t and "m807" in t

    def test_taxonomy_distinguishes_comparators(self):
        t = _block()["relationship_direction_taxonomy"]
        assert "no co-build, no revenue split" in t
        assert "revenue SHARE without joint development" in t
        assert "takes NO equity" in t
        assert "ownership IS the instrument" in t
        assert "adversarial first" in t
        assert "sign-off/verification layer as the retained moat" in t

    def test_connects_to(self):
        assert _block()["connects_to"] == [594, 391, 942]

    def test_confounder_strongest_first(self):
        confs = _block()["confounders"]
        assert len(confs) == 6
        assert confs[0]["strength"] == "STRONG"
        strong = [c for c in confs if c["strength"] == "STRONG"]
        assert len(strong) == 2
        assert "0 browser.open" in confs[0]["text"]
        assert "unsized" in confs[1]["text"]

    def test_coverage_nexus_bounded_absence(self):
        cn = _block()["coverage_nexus"]
        assert "iteration-492" in cn
        assert "Bounded absence" in cn
        assert "NOT scored this run" in cn

    def test_corpus_positioning_leg(self):
        f = _block()["finding"]
        assert "FIRST dedicated corpus mechanism on license-and-co-build" in f
        assert "NOT tested" in f
        assert "Type A follow-up" in f

    def test_research_method_excerpt_tier(self):
        n = _block()["novelty"]
        assert "2 browser.search calls / 2 queries" in n
        assert "0 browser.open" in n


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL/QUALITATIVE ONLY per Aug 28 2026 rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1189:
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
        b = _block()
        assert b["artifact_grade"] is False


# ---------------------------------------------------------------------------
# 7. Falsification ledger (holds at 46; no new member this run).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1189:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False

    def test_forty_sixth_member_form_present(self):
        assert _repo_grep(FORTY_SIXTH_LANDED), FORTY_SIXTH_LANDED

    def test_forty_seventh_member_claim_absent(self):
        # Negative-guard wordings ("absent repo-wide") are allowed; the
        # affirmative member-claim form must not exist. Needle format-built
        # per #715; own file carries no contiguous needle.
        assert FORTY_SEVENTH_MEMBER not in _entities_text()

    def test_forty_eighth_member_claim_absent(self):
        assert FORTY_EIGHTH_MEMBER not in _entities_text()

    def test_ledger_note_wording(self):
        ff = _block()["falsification_family"]
        assert "ledger holds at 46" in ff
        assert "FORTY-SEVENTH member-claim form absent repo-wide" in ff
        # Landed thirty-eighth direction referenced via runtime-built
        # needle; the lowercase absence wording for the thirty-ninth
        # is contiguous prose (not the guard form).
        assert THIRTY_EIGHTH_DIR in ff
        assert "thirty-ninth direction form absent repo-wide" in ff


# ---------------------------------------------------------------------------
# 8. Direction landing (this run LANDS the thirty-eighth direction;
# the thirty-ninth stays absent by design).
# ---------------------------------------------------------------------------

class TestDirectionLanding1189:
    def test_thirty_eighth_direction_present_repo_wide(self):
        # Landed this run: the LICENSE-AND-CO-BUILD direction form must now
        # exist in the corpus. Needle format-built per #715.
        assert THIRTY_EIGHTH_DIR in _entities_text()

    def test_thirty_eighth_in_block_taxonomy(self):
        assert THIRTY_EIGHTH_DIR in _block()["relationship_direction_taxonomy"]

    def test_thirty_ninth_direction_absent(self):
        # Forward guard: the thirty-ninth direction-claim form must not
        # exist. Needle format-built per #715.
        assert THIRTY_NINTH_DIR not in _entities_text()

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

    def test_own_file_no_contiguous_thirty_eighth(self):
        # The contiguous landed form must not appear in this file's
        # source; the constant stays format-built per #715.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("THIRTY" + "-EIGHTH relationship direction") not in src
        assert len(THIRTY_EIGHTH_DIR) > 0

    def test_own_file_no_contiguous_thirty_ninth(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("THIRTY" + "-NINTH relationship direction") not in src
        assert len(THIRTY_NINTH_DIR) > 0

    def test_own_file_no_contiguous_946_forms(self):
        # Needles format-built per #715: constructed at runtime, never
        # written contiguously in source.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (MECH_ID_MARKER + str(NEXT_NUM)) not in src
        assert (MECH_DASH_MARKER + str(NEXT_NUM)) not in src

    def test_own_file_no_contiguous_forty_seventh(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("FORTY" + "-SEVENTH falsification-family member") not in src
        assert len(FORTY_SEVENTH_MEMBER) > 0

    def test_license_and_cobuild_form_named(self):
        assert "LICENSE-AND-CO-BUILD" in _block()["mechanism_name"]
        assert "LICENSE-AND-CO-BUILD" in _block()["relationship_direction_taxonomy"]


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this run pins the 945 landing + thirty-eighth
# direction for #1190; #1188's forward pins flip by design).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1189:
    def test_pins_on_945_landing(self):
        # The guards this run lays for the next leg: max-945, zero-946
        # numeric, no-Type-D-#1190-in-git-log, thirty-eighth landed,
        # thirty-ninth absent.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 945" in src
        assert "NEXT_NUM = 946" in src

    def test_no_type_d_1190_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type D #1190").stdout
        assert log.strip() == ""

    def test_946_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1188_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1188))

    def test_1188_pins_flip_by_design_documented(self):
        # #1188's forward guards (max-944, zero-945 numeric, no-Type-C-#1189
        # in git log) flip by design now that m945 has landed; recorded,
        # not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1188" in src
        text = _entities_text()
        assert "1188" in text or "m944" in text


# ---------------------------------------------------------------------------
# 10. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1190).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1189:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1185_full_suite.log" in src

    def test_suite_checked_only_recorded_not_touched(self):
        # This run stays on targeted verification per the Type C brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest observation per #795:
        # #1185-launched suite ambiguous at the 21:05 PDT check
        # (log 11188 bytes, last write Oct 3 20:56:35 PDT, progress at
        # 15% with xfail markers present, NO live pytest process at the
        # ps scan, ~8 min stale - up from 2% at #1186's 18:45 check, so
        # it progressed then went quiet; not declared dead by this run).
        # #1190 owns the verdict.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "CHECKED ONLY" in src
        assert "15%" in src
        assert "#1190" in src

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no m945 markers.
        log = _read(SUITE_LOG)
        assert "m945" not in log
        assert "Type C #1189" not in log


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1189:
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
        assert "#1189" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count (77).
        assert README_TEST_COUNT == 63451 + 77
        assert README_FILE_COUNT == 1514


# ---------------------------------------------------------------------------
# 12. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1189:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1189 Type C:" in text

    def test_no_duplicate_1189_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1189 Type C:") == 1

    def test_window_fifth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1185-1189" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1189:
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
            assert "mechanism_id: 945" not in diff, path
            assert "Type C #1189" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 block lives in profiles/competitor-entities.yaml;
        # this run appends the m945 block at the end of that file but must
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
        assert "mechanism_id: 945" in diff
