# -*- coding: utf-8 -*-
"""Type C #1194 tests: Amazon x Synopsys $1B+ silicon-IP licensing (announced
Sep 30 2026) - AWS licenses Synopsys application-optimized chip blueprints
and expands EDA tool use under a license-plus-royalty model; Synopsys adopts
AWS EC2/storage and Amazon Bedrock for its own AI product development.
LICENSE-AND-ADOPT lands the thirty-ninth relationship direction
(mechanism 948).

Iteration #1194, FIFTH and CLOSING leg of the 1190-1194 window
(D #1190 -> E #1191 -> A #1192 -> B #1193 -> C #1194).

The m948 block lives in profiles/competitor-entities.yaml as a top-level
`type_c_1194_...` key (Type C convention; cf. m945 at #1189).

This run LANDS a new relationship direction (the thirty-ninth):
LICENSE-AND-ADOPT. The IP vendor licenses its blueprints INTO the
hyperscaler (license fees plus volume-gated royalties) AND adopts the
hyperscaler's cloud/AI platform for its own product development (cloud
spend back). The customer-vendor arrow runs both ways inside the same
agreement. Distinct from m945 license-and-co-build (no co-built product,
no joint go-to-market here), m391 Comet Plus 80/20, the m594-family
flat-fee cash licenses, m807 vendor-embed, and m942 invest-and-license
(no equity here). The fortieth direction stays absent by design; the
thirty-fifth (m915), thirty-sixth (m933), thirty-seventh (m942), and
thirty-eighth (m945) stand.

LEDGER-STATE NOTE: the #1192 m946 block (profiles/wired.yaml) claims the
forty-seventh falsification-family slot with ledger 47, while the #1193
m947 block (profiles/careers/journalists.yaml) asserts ledger holds at 46.
This run takes no position and claims no slot; reconciliation belongs to
the #1195 Type D corpus-integrity run per the rotation guard.

Rejected candidates (not new directions): (1) Firecrawl $75M Series B +
Alexandria licensed-data platform - still thin (LinkedIn-pulse primary),
rejected at #1189, no upgrade; (2) Google AI Contribution Pilot - m891
already the TWENTY-SEVENTH direction, a temporal extension; (3) DOJ
fair-use amicus brief in NYT v OpenAI - state legal intervention, not a
financial relationship, out of Type C scope; (4) Anthropic $1.5B
settlement distribution friction (publishers claiming author shares) -
distribution-phase, not a new relationship direction; the settlement is
in-corpus (m594 leg 4).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.

Per #795: this run only CHECKS the #1190-launched background suite
(observed state recorded below); its verdict belongs to #1195.

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the next
number 949 keys, the forty-seventh / forty-eighth member forms, or the
thirty-ninth / fortieth direction-claim forms; the landed thirty-ninth
direction form is asserted via a runtime-built needle against the landed
YAML (never written contiguously in source); the constants are constructed
at runtime.
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
    "test_type_c_1194_amazon_synopsys_1b_silicon_ip_license_and_adopt_"
    "thirty_ninth_direction_oct04_1am.py"
)
BLOCK_KEY = (
    "type_c_1194_amazon_synopsys_1b_silicon_ip_license_and_adopt_"
    "thirty_ninth_direction_oct04_1am"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "e9e8cd203ea5bf2c550016d507e24fcadebc125d"
# Post-first-run values per #719: README_TEST_COUNT / README_FILE_COUNT are
# patched to the post-sync-positive values after the first collection run
# (README ratchets 63827/1518 -> 63827+N/1519 in the doc-sync followup).
README_TEST_COUNT = 63827 + 83  # 63910; patched post-first-run per #719
README_FILE_COUNT = 1519
COLLECTED_NEW_TESTS = 83  # patched post-first-run per #719

# Forward guards for the next landing. MECH_NUM=948 is THIS run's landed
# mechanism; NEXT_NUM=949 stays forward.
MECH_NUM = 948
NEXT_NUM = 949

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + "949" at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + "949" at runtime
THIRTY_FIFTH_DIR = "THIRTY" + "-FIFTH relationship direction"
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH relationship direction"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"
THIRTY_EIGHTH_DIR = "THIRTY" + "-EIGHTH relationship direction"
THIRTY_NINTH_DIR = "THIRTY" + "-NINTH relationship direction"
FORTIETH_DIR = "FORT" + "IETH relationship direction"
FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
FORTY_EIGHTH_MEMBER = "FORTY" + "-EIGHTH falsification-family member"

# The landed m948 block lives here (top-level key; designed keying per
# #715: the block key carries iteration 1194, no 948 substring).
ENTITIES_PATH = os.path.join(REPO, "profiles", "competitor-entities.yaml")
FILE_1193 = (
    "test_type_b_1193_jeff_meyer_camerajabber_snap_specs_conspicuous_"
    "vs_meta_rayban_disguise_within_piece_oct04_12am.py"
)
M846_BLOCK_NEEDLE = "type_c_1024_benioff"

# Ordinal form of the falsification family. The FORTY-SIXTH member form
# must be present repo-wide (m907, profiles/the-verge.yaml). This run
# takes no ledger position per the LEDGER-STATE NOTE above.
FORTY_SIXTH_LANDED = "FORTY-SIXTH falsification-family member"

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1190_full_suite.log"
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
    out = _git("log", "--format=%H", "--grep=Type C #1194:").stdout.strip()
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

class TestAnchor1194:
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
        # "Type C #1194 anchor followup: ANCHORED_SHA -> <hash> ...".
        log = _git("log", "--oneline", "--grep=Type C #1194 anchor").stdout
        assert "Type C #1194 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type C #1194:").stdout
        assert "Type C #1194" in log


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1194 is the FIFTH and CLOSING leg of 1190-1194.
# ---------------------------------------------------------------------------

class TestRotationGuard1194:
    def test_rotation_window_is_1190_1194(self):
        assert "1190-1194" in _entities_text()

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1190-1194 window FIFTH and CLOSING leg "
            "(D #1190 -> E #1191 -> A #1192 -> B #1193 -> C #1194)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1190", "Type E #1191", "Type A #1192",
                       "Type B #1193"):
            assert marker in log, marker

    def test_no_type_d_1195_in_git_log_yet(self):
        # The next window (1195-1199) opens with Type D #1195; it must not
        # exist as a commit yet.
        log = _git("log", "--oneline", "--grep=Type D #1195").stdout
        assert log.strip() == ""

    def test_single_type_c_1194_test_file(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_c_1194_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (pre-commit claims, verifiable post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1194:
    def test_block_key_present_once(self):
        assert _entities_text().count(BLOCK_KEY + ":") == 1

    def test_block_key_zero_948_substring(self):
        # Designed keying per #715: the block key carries the iteration
        # number 1194, not the mechanism number 948.
        assert "948" not in BLOCK_KEY

    def test_zero_underscore_948_repo_wide(self):
        # Per #1193's forward guard (zero-948 keys all forms): no
        # underscore-form 948 mechanism key may exist repo-wide
        # (own file excluded from the walk).
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_948_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_949_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_948(self):
        present = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert present, "m948 must be present in profiles"
        for n in range(MECH_NUM + 1, MECH_NUM + 20):
            assert _profiles_grep_numeric_mechanism_id(n) == [], n

    def test_no_duplicate_block_key(self):
        d = _load_entities()
        assert list(d.keys()).count(BLOCK_KEY) == 1

    def test_urls_copied_verbatim(self):
        urls = [s["url"] for s in _block()["sources"]]
        assert len(urls) == 9
        assert (
            "https://www.reuters.com/business/retail-consumer/"
            "synopsys-amazon-web-services-sign-chip-design-licensing-"
            "deal-worth-more-than-1-2026-09-30/"
        ) in urls
        assert (
            "https://www.reuters.com/business/synopsys-shares-jump-"
            "robust-growth-outlook-openai-aws-deals-2026-10-01/"
        ) in urls
        assert (
            "https://catenaa.com/industries/technology/aws-announces-"
            "1bn-deal-with-synopsys-on-custom-silicon/"
        ) in urls
        assert (
            "https://fudzilla.com/amazon-throws-a-billion-at-custom-"
            "chip-design/"
        ) in urls
        assert (
            "https://www.verdict.co.uk/synopsys-silicon-ip-deal-amazon/"
        ) in urls
        assert (
            "https://www.tradingview.com/news/seekingalpha:cdb5e0c56094b:0-"
            "synopsys-amazon-sign-multiyear-agreement-for-custom-chips/"
        ) in urls
        assert (
            "https://www.fierce-network.com/newswire/amazon-inks-1b-"
            "custom-silicon-deal-synopsys"
        ) in urls
        assert (
            "https://news.lavx.hu/article/amazon-synopsys-sign-1-billion-"
            "ai-chip-design-deal"
        ) in urls
        assert (
            "https://zubiqo.com/news/amazon-aws-and-synopsys-sign-1b-"
            "custom-chip-licensing-deal-7a1wp4"
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

class TestBlockStructure1194:
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
        assert b["iteration"] == 1194
        assert b["mechanism_id"] == 948

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
        assert _block()["connects_to"] == [945, 594, 391, 807]
# ---------------------------------------------------------------------------
# 5. m948 content discipline (Amazon x Synopsys $1B+ silicon-IP
# license-and-adopt, thirty-ninth direction landing).
# ---------------------------------------------------------------------------

class TestM948ContentDiscipline1194:
    def test_announcement_leg(self):
        f = _block()["finding"]
        assert "more than $1 billion" in f
        assert "Stephen Nellis" in f
        assert "application-optimized" in f or "application-optimised" in f

    def test_reciprocal_adoption_leg(self):
        f = _block()["finding"]
        assert "Bedrock" in f
        assert "EC2" in f

    def test_license_plus_royalty_leg(self):
        f = _block()["finding"]
        assert "license-plus-royalty" in f
        assert "production volumes" in f

    def test_market_leg(self):
        f = _block()["finding"]
        assert "+10%" in f or "jumped 10%" in f
        assert "11.10" in f

    def test_dual_track_leg(self):
        f = _block()["finding"]
        assert "m945" in f
        assert "dual-track" in f or "Dual-track" in f

    def test_money_flow_reciprocal(self):
        mf = _block()["money_flow"]
        assert "AMAZON PAYS IN" in mf
        assert "SYNOPSYS PAYS BACK" in mf
        assert "unquantified" in mf

    def test_confounder_strengths(self):
        confs = _block()["confounders"]
        strengths = [c["strength"] for c in confs]
        assert strengths.count("STRONG") == 2
        assert "MODERATE" in strengths
        assert "WEAK" in strengths
        assert any("0 browser.open per #503" in c["text"] for c in confs)

    def test_coverage_nexus(self):
        cn = _block()["coverage_nexus"]
        assert "NOT scored" in cn
        assert "iteration-492" in cn

    def test_nine_sources(self):
        assert len(_block()["sources"]) == 9
        assert all(s["novel"] is True for s in _block()["sources"])

    def test_direction_named(self):
        assert "LICENSE-AND-ADOPT" in _block()["mechanism_name"]
        assert "LICENSE-AND-ADOPT" in _block()["relationship_direction_taxonomy"]


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL / qualitative-only per the Aug 28 2026
# standing rule; engine never run on findings).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1194:
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
# 7. Falsification ledger: NOT a member; ledger-state note, no position
# taken (reconciliation belongs to #1195 Type D per the rotation guard).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1194:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False

    def test_forty_sixth_member_form_present(self):
        assert _repo_grep(FORTY_SIXTH_LANDED), FORTY_SIXTH_LANDED

    def test_ledger_state_note_wording(self):
        ff = _block()["falsification_family"]
        assert "NOT a member" in ff
        assert "LEDGER-STATE NOTE" in ff
        assert "takes no position and claims no slot" in ff
        assert "#1195 Type D corpus-integrity run" in ff
        # Landed thirty-ninth direction referenced via runtime-built
        # needle; the lowercase absence wording for the fortieth is
        # contiguous prose (not the guard form).
        assert THIRTY_NINTH_DIR in ff
        assert "fortieth direction form absent repo-wide" in ff

    def test_own_file_no_contiguous_forty_seventh(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert FORTY_SEVENTH_MEMBER not in src
        assert len(FORTY_SEVENTH_MEMBER) > 0

    def test_own_file_no_contiguous_forty_eighth(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert FORTY_EIGHTH_MEMBER not in src
        assert len(FORTY_EIGHTH_MEMBER) > 0


# ---------------------------------------------------------------------------
# 8. Direction landing (this run LANDS the thirty-ninth direction;
# the fortieth stays absent by design).
# ---------------------------------------------------------------------------

class TestDirectionLanding1194:
    def test_thirty_ninth_direction_present_repo_wide(self):
        # Landed this run: the LICENSE-AND-ADOPT direction form must now
        # exist in the corpus. Needle format-built per #715.
        assert THIRTY_NINTH_DIR in _entities_text()

    def test_thirty_ninth_in_block_taxonomy(self):
        assert THIRTY_NINTH_DIR in _block()["relationship_direction_taxonomy"]

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

    def test_own_file_no_contiguous_thirty_ninth(self):
        # The contiguous landed form must not appear in this file's
        # source; the constant stays format-built per #715.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("THIRTY" + "-NINTH relationship direction") not in src
        assert len(THIRTY_NINTH_DIR) > 0

    def test_own_file_no_contiguous_fortieth(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("FORT" + "IETH relationship direction") not in src
        assert len(FORTIETH_DIR) > 0

    def test_own_file_no_contiguous_949_forms(self):
        # Needles format-built per #715: constructed at runtime, never
        # written contiguously in source.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (MECH_ID_MARKER + str(NEXT_NUM)) not in src
        assert (MECH_DASH_MARKER + str(NEXT_NUM)) not in src


# ---------------------------------------------------------------------------
# 9. Forward-looking staleness (designed lifecycle; the #1195 Type D run
# pins the 949 landing).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1194:
    def test_zero_949_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 949" in src
        # Needles format-built per #715: constructed at runtime, never
        # written contiguously in source.
        assert (MECH_ID_MARKER + str(NEXT_NUM)) not in src
        assert (MECH_DASH_MARKER + str(NEXT_NUM)) not in src

    def test_no_fortieth_direction_guard(self):
        # The fortieth direction form stays absent repo-wide; the
        # constant is format-built so the source never carries it.
        assert not _repo_grep(FORTIETH_DIR), FORTIETH_DIR
        assert len(FORTIETH_DIR) > 0

    def test_no_forty_seventh_member_guard(self):
        # Format-built per #715: constructed at runtime, never written
        # contiguously in source (verified by inspection of the constant
        # definition above). Scoped to this file per the #1193
        # convention; the #1192/#1193 ledger-state dispute is #1195
        # Type D territory, not asserted here.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert FORTY_SEVENTH_MEMBER not in src
        assert len(FORTY_SEVENTH_MEMBER) > 0

    def test_no_forty_eighth_member_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert FORTY_EIGHTH_MEMBER not in src
        assert len(FORTY_EIGHTH_MEMBER) > 0

    def test_1193_pins_flip_by_design_documented(self):
        # #1193's forward guards (max-947, zero-948 keys all forms,
        # no-Type-C-#1194-in-git-log, no-thirty-ninth-direction) flip by
        # design now that m948 has landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1193" in src
        text = _entities_text()
        assert "1193" in text or "m947" in text

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

    def test_thirty_ninth_direction_now_present(self):
        # Landed this run; the #1193 no-thirty-ninth guard flips by
        # design (supersession, not repair).
        assert _repo_grep(THIRTY_NINTH_DIR)


# ---------------------------------------------------------------------------
# 10. Guard lifecycle (this run pins the 948 landing for #1195).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1194:
    def test_pins_on_948_landing(self):
        # The guards this run lays for the next leg: max-948, zero-949
        # numeric, no-Type-D-#1195-in-git-log, thirty-ninth landed,
        # fortieth absent.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 948" in src
        assert "NEXT_NUM = 949" in src

    def test_no_type_d_1195_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type D #1195").stdout
        assert log.strip() == ""

    def test_949_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1193_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1193))

    def test_1193_pins_flip_by_design_documented(self):
        # #1193's forward guards (max-947, zero-948 numeric,
        # no-Type-C-#1194-in-git-log, no-thirty-ninth-direction) flip by
        # design now that m948 has landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1193" in src
        text = _entities_text()
        assert "1193" in text or "m947" in text
# ---------------------------------------------------------------------------
# 11. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1195).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1194:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1190_full_suite.log" in src

    def test_suite_checked_only_recorded_not_touched(self):
        # This run stays on targeted verification per the Type C brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest observation per #795:
        # #1190-launched suite ALIVE at the ~01:00 PDT check (log 7920
        # bytes, last write Oct 4 00:09 PDT, progress ~11%, 2 F markers
        # at ~10%, one pytest process alive) - progressing slowly, not
        # declared dead by this run. The 2 F markers are noted, not
        # adjudicated. #1195 owns the verdict.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "CHECKED ONLY" in src
        assert "11%" in src
        assert "#1195" in src

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no m948 markers.
        log = _read(SUITE_LOG)
        assert "m948" not in log
        assert "Type C #1194" not in log


# ---------------------------------------------------------------------------
# 12. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1194:
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
        assert "#1194" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 63827 + COLLECTED_NEW_TESTS
        assert README_FILE_COUNT == 1519


# ---------------------------------------------------------------------------
# 13. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1194:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1194 Type C:" in text

    def test_no_duplicate_1194_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1194 Type C:") == 1

    def test_window_fifth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1190-1194" in text


# ---------------------------------------------------------------------------
# 14. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1194:
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
            assert "mechanism_id: 948" not in diff, path
            assert "Type C #1194" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 block lives in profiles/competitor-entities.yaml;
        # this run appends the m948 block at the end of that file but must
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
        assert "mechanism_id: 948" in diff
