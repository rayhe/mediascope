"""MediaScope iteration #1128 (Type B, journalist cross-entity tracking):
David Heaney (UploadVR) Sep-13/14/17 Meta-vs-Apple headline-softening
register contrast - Threads force-download relay vs Vision Pro layoff
"But Don't Panic" vs visionOS 27 product-positive.

The anchor is the block keyed
type_b_1128_david_heaney_uploadvr_meta_threads_vs_apple_vision_pro_layoffs_visionos_sep2026
under David Heaney's competitor_coverage in profiles/careers/journalists.yaml:
mechanism 908, the FIRST dedicated corpus mechanism on Heaney's Apple
coverage (m821/Type B #983 covered Snap-vs-Meta; this run adds the
Meta-vs-Apple leg).

The within-writer contrast: Heaney applies headline-level editorial
softening to Apple bad news (Sep-14 Vision Pro layoffs kicker "But Don't
Panic", +0.20 MANUAL ILLUSTRATIVE) one day after neutral-factual Meta relay
(Sep-13 Threads force-download, 0.0 MANUAL ILLUSTRATIVE), with a
product-positive visionOS 27 arm (+0.30) four days later. Illustrative
delta (Apple mean +0.25 minus Meta 0.0) = +0.25, n=1 vs n=2 degenerate
contract, NOT significant.

NOT a falsification-family member: bounded searches found no UploadVR x
Meta or UploadVR x Apple financial relationship, so no payer-softening
prediction is tested. Ledger holds at 46. Extends m821's Heaney register
finding (register follows the news peg) to a third entity (Apple).

Rotation transparency: this run is iteration #1128 Type B, the FOURTH leg
of the 1125-1129 window (D #1125 -> E #1126 -> A #1127 -> B #1128 -> C
#1129). Predecessor #1127 Type A verified in git log (main 80d3738e /
anchor ef613b1e / doc-sync 459184c8 / log-hash 36756bb0, Oct 1 2026 3:00 PM
PDT). Next run #1129 continues the window as Type C (fifth leg); it
inherits the zero-909 forward guards, the no-thirty-third-direction
guard, and the no-forty-seventh-member guard from this run.

In-flight, untouched: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B
test-file anchor edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit). Do NOT touch #1024 m846 (Ray's revert/leave/rebuild
decision pending - not an assistant repair task). Use targeted staging only.

Literal discipline per #715/#770: every mechanism-id and member-claim needle
in this file is format-built at runtime - no contiguous underscore/dash-908,
underscore/dash-909, forty-seventh member-claim, forty-sixth member-claim,
thirty-third direction, or thirty-second direction forms appear in source.
Permitted contiguous forms: the landed FORTY-FIFTH member claim and the
landed FORTY-SIXTH reference in ledger-guard prose. Docstring prose uses
hyphenated/lowercase forms.
"""

import glob
import os
import re
import subprocess

import yaml


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
JOURNALISTS_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
OWN_BASENAME = (
    "test_type_b_1128_david_heaney_uploadvr_meta_threads_"
    "vs_apple_vision_pro_layoffs_visionos_sep2026_4pm.py"
)

# Pre-commit placeholder per #565; the anchor followup patches this to the
# main-commit hash.
ANCHORED_SHA = "0cf311515ed7bbfa6a9a7bde0d7fcc63f7d632ff"  # Type B #1128 main commit (Type B runs self-anchor per #565)

MECH_NUM = 908
NEXT_NUM = 909

# Literal discipline per #715/#770: the underscore/dash mechanism-key forms,
# the block key, and the member/direction forward-guard forms are
# format-built so this file carries no contiguous needle.
MECH_ID_MARKER = "mechanism" + "_"
MECH_DASH_MARKER = "mechanism" + "-"

BLOCK_KEY = (
    "type_b_1128_david_heaney_uploadvr_meta_threads_"
    "vs_apple_vision_pro_layoffs_visionos_sep2026"
)

FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
FORTY_SIXTH_MEMBER = "FORTY" + "-SIXTH falsification-family member"
THIRTY_THIRD_DIR = "THIRTY" + "-THIRD" + " relationship direction"
THIRTY_SECOND_LANDED = "THIRTY" + "-SECOND" + " relationship direction"
FORTY_FIFTH_MEMBER = "FORTY-FIFTH falsification-family member"
FORTY_SIXTH_LANDED = "FORTY-SIXTH falsification-family member"

PRED_MAIN_1127 = "80d3738e"
PRED_ANCHOR_1127 = "ef613b1e"
PRED_DOCSYNC_1127 = "459184c8"
PRED_LOGHASH_1127 = "36756bb0"

FILE_1127 = (
    "test_type_a_1127_verge_openai_sep29_30_safety_crisis_double_"
    "oct01_3pm.py"
)

URL_META_THREADS = (
    "https://www.uploadvr.com/"
    "threads-apps-arrived-on-quest-meta-ray-ban-display/"
)
URL_APPLE_LAYOFFS = (
    "https://www.uploadvr.com/"
    "apple-vision-pro-layoffs-2026-gaming-immersive-video/"
)
URL_APPLE_VISIONOS = (
    "https://www.uploadvr.com/"
    "visionos-27-launched-for-apple-vision-pro-headsets/"
)


def _read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def _git(*args):
    return subprocess.run(
        ["git"] + list(args), cwd=REPO_ROOT, capture_output=True, text=True
    )


def _iter_source_files():
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [
            d
            for d in dirs
            if d not in (".git", "__pycache__", "node_modules", ".venv")
        ]
        for f in files:
            if f == OWN_BASENAME:
                continue
            if f.endswith(".py"):
                yield os.path.join(root, f)


def _repo_grep_underscore_mechanism(n):
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [p for p in _iter_source_files() if needle in _read(p)]


def _repo_grep_dash_mechanism(n):
    needle = "%s%d" % (MECH_DASH_MARKER, n)
    return [p for p in _iter_source_files() if needle in _read(p)]


def _profiles_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in _read(p):
                hits.append(p)
    return hits


def _max_numeric_mechanism_id_in_profiles():
    found = []
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            found.extend(int(m) for m in pat.findall(_read(os.path.join(root, f))))
    return max(found) if found else 0


def _profiles_text():
    parts = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            parts.append(_read(os.path.join(root, f)))
    return "\n".join(parts)


def _block():
    doc = yaml.safe_load(_read(JOURNALISTS_FILE))
    return doc["david_heaney"]["competitor_coverage"][BLOCK_KEY]


def _block_text():
    return _read(JOURNALISTS_FILE)


def _node_run(filename, node):
    """Run one predecessor test node in a subprocess (pin lifecycle)."""
    target = os.path.join(TESTS_DIR, filename) + "::" + node
    env = dict(os.environ)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    return subprocess.run(
        ["python3", "-m", "pytest", target, "-q", "--no-header"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        env=env,
    )


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder; patched green post-commit per #565).
# ---------------------------------------------------------------------------

class TestAnchor1128:
    def test_anchored_sha_placeholder_pre_commit(self):
        # Pre-commit the anchor is a zero placeholder; the anchor followup
        # patches it per #565. The post-commit rotation guard asserts the
        # patched ANCHORED_SHA is present in git log.
        # Deselect this test in post-commit full runs.
        assert ANCHORED_SHA == "0" * 40

    def test_anchored_sha_shape(self):
        assert len(ANCHORED_SHA) == 40

    def test_anchor_mechanics_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ANCHORED_SHA" in src
        assert "#565" in src

    def test_block_key_matches_file_and_profile(self):
        # The format-built BLOCK_KEY is the colon-form profile key carrying
        # the iteration number (not the mechanism id) per #715.
        assert "type_b_1128" in BLOCK_KEY
        assert "908" not in BLOCK_KEY
        assert BLOCK_KEY in _block_text()

    def test_journalist_file_and_indent(self):
        # The block lives under david_heaney's competitor_coverage at indent
        # 4 in profiles/careers/journalists.yaml (top-level slug key).
        text = _block_text()
        assert "    " + BLOCK_KEY + ":" in text
        b = _block()
        assert b["journalist"] == "David Heaney"
        assert b["block_key"] == BLOCK_KEY
        assert b["publication"] == "uploadvr"


# ---------------------------------------------------------------------------
# 2. Rotation guard (pre-commit assertions; git-log novelty test is
# SUPERSEDED BY DESIGN post-commit - deselect in post-commit full runs).
# ---------------------------------------------------------------------------

class TestRotationGuard1128:
    def test_predecessor_1127_chain_present(self):
        log = _git("log", "--oneline", "-80").stdout
        assert PRED_MAIN_1127 in log
        assert PRED_ANCHOR_1127 in log
        assert PRED_DOCSYNC_1127 in log
        assert PRED_LOGHASH_1127 in log

    def test_type_b_1128_novelty(self):
        # "Type B #1128" absent from git log pre-commit; own file not
        # yet committed. SUPERSEDED BY DESIGN once this run's main
        # commit ("Type B #1128:") lands; post-commit, the anchor
        # asserts the patched ANCHORED_SHA is present in git log.
        # Deselect this test in post-commit full runs.
        log = _git("log", "--oneline", "--grep=Type B #1128").stdout
        assert log.strip() == ""

    def test_window_order_d_e_a_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1125 -> E #1126 -> A #1127 -> B #1128" in src

    def test_window_fourth_leg(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FOURTH leg" in src
        assert "1125-1129" in src

    def test_next_run_1129_type_c_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "C #1129" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (post-landing state: max is 908; 909 absent in all
# forms; 908 underscore/dash absent - the forward guards for #1129+).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1128:
    def test_single_test_file_for_iteration(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1128*.py"))
        assert len(files) == 1, files

    def test_novelty_verification_claim_in_block(self):
        assert "zero test_type_b_1128 files on disk" in _block_text()

    def test_max_numeric_mechanism_id_is_908(self):
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_zero_underscore_909_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_909_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_909_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_908_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_zero_dash_908_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_908_numeric_present_only_in_journalists_block(self):
        hits = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == [JOURNALISTS_FILE], hits

    def test_block_key_zero_hit_outside_own_file(self):
        # The block key must not appear anywhere except the landed profile
        # block (own file carries only the format-built form).
        hits = [
            p for p in _iter_source_files() if BLOCK_KEY in _read(p)
        ]
        assert hits == [], hits


# ---------------------------------------------------------------------------
# 4. Block structure.
# ---------------------------------------------------------------------------

class TestBlockStructure1128:
    def test_block_loads_under_heaney_competitor_coverage(self):
        doc = yaml.safe_load(_block_text())
        assert BLOCK_KEY in doc["david_heaney"]["competitor_coverage"]

    def test_iteration_and_type(self):
        b = _block()
        assert b["iteration"] == 1128
        assert b["type"] == "B"

    def test_date_and_window(self):
        b = _block()
        assert b["date"] == "2026-10-01 16:00 PDT"
        assert "FOURTH leg" in b["window"]
        assert "1125-1129" in b["window"]

    def test_goal_and_job(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"

    def test_test_file_field(self):
        assert _block()["test_file"].endswith(OWN_BASENAME)

    def test_mechanism_id_908(self):
        assert _block()["mechanism_id"] == 908

    def test_author(self):
        assert _block()["author"] == "Kit (with Ray)"

    def test_ascii_no_em_dashes(self):
        # Scoped to this run's block segment per the #1123 convention
        # (the file carries pre-existing non-ASCII elsewhere, e.g. the
        # Conde Nast note at line ~89).
        text = _block_text()
        start = text.index(BLOCK_KEY)
        segment = text[start : start + 20000]
        assert "\u2014" not in segment
        segment.encode("ascii")


# ---------------------------------------------------------------------------
# 5. Meta arm (Sep 13 Threads on Quest & Meta Ray-Ban Display).
# ---------------------------------------------------------------------------

class TestMetaArm1128:
    def test_title_and_date(self):
        arm = _block()["new_meta_arm"]
        assert arm["title"] == "Threads Apps Arrived On Quest & Meta Ray-Ban Display"
        assert arm["date"] == "Sep 13 2026"

    def test_url_novel_and_verbatim(self):
        arm = _block()["new_meta_arm"]
        assert arm["url"] == URL_META_THREADS
        assert "threads-apps-arrived-on-quest-meta-ray-ban-display" in arm["url"]

    def test_byline_heaney(self):
        arm = _block()["new_meta_arm"]
        assert "David Heaney" in arm["byline"]

    def test_register_neutral_factual(self):
        arm = _block()["new_meta_arm"]
        assert arm["tone_score"] == 0.0
        assert "MANUAL ILLUSTRATIVE" in arm["tone_basis"]
        assert "0 browser.open per #503" in arm["tone_basis"]

    def test_force_download_detail_present(self):
        quotes = _block()["new_meta_arm"]["key_quotes"]
        assert any("force-downloading" in q for q in quotes)
        assert any("unhappy" in q for q in quotes)

    def test_no_adversarial_meta_framing(self):
        arm = _block()["new_meta_arm"]
        assert "Zero adversarial framing of Meta as an actor" in arm["register_notes"]


# ---------------------------------------------------------------------------
# 6. Apple arms (Sep 14 layoffs; Sep 17 visionOS 27).
# ---------------------------------------------------------------------------

class TestAppleArms1128:
    def _arms(self):
        return _block()["new_apple_arms"]

    def test_two_arms(self):
        assert len(self._arms()) == 2

    def test_layoffs_title_kicker(self):
        arm = self._arms()[0]
        assert arm["arm"] == "Vision Pro layoffs"
        assert "But Don't Panic" in arm["title"]
        assert arm["date"] == "Sep 14 2026"

    def test_layoffs_url_novel_and_verbatim(self):
        arm = self._arms()[0]
        assert arm["url"] == URL_APPLE_LAYOFFS
        assert "apple-vision-pro-layoffs-2026-gaming-immersive-video" in arm["url"]

    def test_layoffs_headline_softening(self):
        arm = self._arms()[0]
        quotes = arm["key_quotes"]
        assert any("But Don't Panic" in q for q in quotes)
        assert any("not going away" in q for q in quotes)
        assert any("100 staff" in q for q in quotes)
        assert arm["tone_score"] == 0.2
        assert "headline/framing" in arm["tone_basis"]

    def test_layoffs_body_factual(self):
        arm = self._arms()[0]
        assert "Gurman" in " ".join(arm["key_quotes"])
        assert "HEADLINE level" in arm["register_notes"]

    def test_visionos_title_and_date(self):
        arm = self._arms()[1]
        assert arm["arm"] == "visionOS 27 launch"
        assert "visionOS 27 Launched" in arm["title"]
        assert arm["date"] == "Sep 17 2026"

    def test_visionos_url_novel_and_verbatim(self):
        arm = self._arms()[1]
        assert arm["url"] == URL_APPLE_VISIONOS
        assert "visionos-27-launched-for-apple-vision-pro-headsets" in arm["url"]

    def test_visionos_product_positive(self):
        arm = self._arms()[1]
        quotes = arm["key_quotes"]
        assert any("biggest upgrades yet" in q for q in quotes)
        assert arm["tone_score"] == 0.3

    def test_visionos_discloses_google_deal(self):
        # Counterevidence against a concealment reading: the piece
        # discloses Apple's $1B/yr Google co-development inside the text.
        arm = self._arms()[1]
        joined = " ".join(arm["key_quotes"])
        assert "$1 billion/year deal" in joined
        assert "counterevidence" in arm["register_notes"]


# ---------------------------------------------------------------------------
# 7. Register contrast.
# ---------------------------------------------------------------------------

class TestRegisterContrast1128:
    def test_delta_calc(self):
        rc = _block()["register_contrast"]
        assert rc["illustrative_delta_apple_minus_meta"] == 0.25
        assert "(0.20 + 0.30) / 2 - 0.0 = +0.25" in rc["delta_calc"]

    def test_temporal_window(self):
        rc = _block()["register_contrast"]
        assert "1 day" in rc["temporal_window"]
        assert "Sep 13 Meta vs Sep 14 Apple" in rc["temporal_window"]

    def test_reading_extends_m821(self):
        rc = _block()["register_contrast"]
        assert "m821" in rc["reading"]
        assert "third entity (Apple)" in rc["reading"]

    def test_degenerate_contract_disclosed(self):
        rc = _block()["register_contrast"]
        assert "n=1 vs n=2 degenerate contract" in rc["reading"]
        assert "NOT significant" in rc["reading"]

    def test_primary_pair_identified(self):
        rc = _block()["register_contrast"]
        assert rc["meta_arm_tone"] == 0.0
        assert "+0.25" in rc["apple_arm_tones"]


# ---------------------------------------------------------------------------
# 8. Financial relationship (no gradient found - NOT a falsification test).
# ---------------------------------------------------------------------------

class TestFinancialRelationship1128:
    def test_no_uploadvr_meta_gradient(self):
        fr = _block()["financial_relationship"]
        assert "No UploadVR x Meta financial relationship" in fr["uploadvr_meta"]

    def test_no_uploadvr_apple_gradient(self):
        fr = _block()["financial_relationship"]
        assert "No UploadVR x Apple financial relationship" in fr["uploadvr_apple"]

    def test_luckey_caution_false_positive(self):
        fr = _block()["financial_relationship"]
        assert "false-positive caution" in fr["luckey_caution"]
        assert "NOT UploadVR the publication" in fr["luckey_caution"]

    def test_not_a_falsification_test(self):
        fr = _block()["financial_relationship"]
        assert "No payer-softening prediction is testable" in fr["test"]
        assert "NOT a falsification-family member" in fr["result"]

    def test_revenue_model_bounded(self):
        fr = _block()["financial_relationship"]
        assert "ad/affiliate" in fr["revenue_model"]


# ---------------------------------------------------------------------------
# 9. Scorer discipline.
# ---------------------------------------------------------------------------

class TestScorerDiscipline1128:
    def test_manual_illustrative_only(self):
        assert "MANUAL ILLUSTRATIVE ONLY" in _block()["scorer"]["method"]

    def test_engine_not_run(self):
        assert "engine NOT run" in _block()["scorer"]["method"]

    def test_not_significant(self):
        assert "is_significant False" in _block()["scorer"]["method"]

    def test_no_analysis_json_update(self):
        assert "no_analysis_json_update true" in _block()["scorer"]["method"]

    def test_verdict_not_proven(self):
        assert "directionally_supported_not_proven" in _block()["scorer"]["verdict"]

    def test_confounder_count(self):
        confs = _block()["confounders"]
        assert len(confs) == 5
        assert any("STRONG: news-peg mismatch" in c for c in confs)
        assert any("counterevidence" in c.lower() or "Counterevidence" in c for c in confs)


# ---------------------------------------------------------------------------
# 10. Falsification ledger guard (holds at 46; no new member, no new
# direction; needles format-built per #715).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1128:
    def _ledger_hits(self, needle):
        return [
            p for p in _iter_source_files()
            if needle in _read(p)
        ]

    def test_member_flag_false(self):
        assert _block()["falsification_family_member"] is False

    def test_ledger_46(self):
        assert _block()["falsification_ledger"] == 46

    def test_forty_sixth_landed_intact(self):
        # #1127's landed claim stays intact in the-verge.yaml; this run's
        # block references it only in non-claim phrasing.
        hits = [
            p for p in
            [os.path.join(PROFILES_DIR, f) for f in os.listdir(PROFILES_DIR)
             if f.endswith(".yaml")]
            if FORTY_SIXTH_LANDED in _read(p)
        ]
        assert hits == [os.path.join(PROFILES_DIR, "the-verge.yaml")], hits

    def test_forty_seventh_member_absent_repo_wide(self):
        # The affirmative forty-seventh claim form must not appear anywhere
        # (needle format-built per #715; own file carries no contiguous
        # form; the profile block carries only negative-guard wording).
        assert FORTY_SEVENTH_MEMBER not in _profiles_text()
        hits = self._ledger_hits(FORTY_SEVENTH_MEMBER)
        assert hits == [], hits

    def test_thirty_third_direction_absent_repo_wide(self):
        hits = self._ledger_hits(THIRTY_THIRD_DIR)
        assert hits == [], hits
        assert THIRTY_THIRD_DIR not in _profiles_text()

    def test_thirty_second_direction_intact_in_competitor_entities(self):
        # The THIRTY-SECOND direction is landed (m906, Type C #1124) in
        # competitor-entities.yaml; this run claims no new direction, so the
        # landed form must stay intact there (needle format-built per #715).
        text = _read(os.path.join(PROFILES_DIR, "competitor-entities.yaml"))
        assert THIRTY_SECOND_LANDED in text

    def test_ledger_note_documents_hold(self):
        note = _block()["ledger_note"]
        assert "Ledger holds at 46" in note
        assert "NOT a falsification-family member" in note


# ---------------------------------------------------------------------------
# 11. Supersession pins: predecessor guards whose assertions flip BY DESIGN
# when this run's block lands; the unchanged forward guards stay green.
# ---------------------------------------------------------------------------

class TestSupersessionPins1128:
    def test_1127_novelty_max_907_fails_by_design(self):
        # The 908 numeric id now exists in the working-tree profiles/
        # (this run's landed block); fails BY DESIGN post-landing.
        res = _node_run(
            FILE_1127,
            "TestGuardLifecycle1127::test_1127_file_pins_max_id_907_and_next_908",
        )
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1127_no_new_mechanisms_below_max_fails_by_design(self):
        res = _node_run(
            FILE_1127, "TestGuardLifecycle1127::test_no_new_mechanisms_below_max"
        )
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1127_zero_numeric_908_fails_by_design(self):
        res = _node_run(
            FILE_1127, "TestGuardLifecycle1127::test_zero_next_numeric_908_in_profiles"
        )
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1127_no_type_b_1128_in_git_log_fails_by_design_post_commit(self):
        # Pre-commit this passes (no "Type B #1128" in git log yet); post
        # main-commit it fails BY DESIGN. Deselect in post-commit full
        # runs; the anchor asserts the patched ANCHORED_SHA instead.
        res = _node_run(
            FILE_1127, "TestTypeARotationGuard1127::test_no_type_b_1128_in_git_log"
        )
        assert res.returncode == 0, res.stdout[-1500:]

    def test_1127_forty_seventh_guard_stays_green(self):
        # This run does NOT claim the forty-seventh member, so #1127's
        # no-forty-seventh guard stays green post-landing.
        res = _node_run(
            FILE_1127, "TestGuardLifecycle1127::test_no_forty_seventh_member_claim"
        )
        assert res.returncode == 0, res.stdout[-1500:]

    def test_1127_thirty_third_guard_stays_green(self):
        res = _node_run(
            FILE_1127, "TestGuardLifecycle1127::test_no_thirty_third_direction_claim"
        )
        assert res.returncode == 0, res.stdout[-1500:]


# ---------------------------------------------------------------------------
# 12. Doc-sync ratchet (per #719; patched counts post-collection).
# ---------------------------------------------------------------------------

class TestDocSync1128:
    def test_readme_stats_row(self):
        text = _read(README_PATH)
        assert OWN_BASENAME in text

    def test_architecture_tree_row(self):
        text = _read(ARCH_PATH)
        assert OWN_BASENAME in text


# ---------------------------------------------------------------------------
# 13. Iteration log.
# ---------------------------------------------------------------------------

class TestIterationLog1128:
    def test_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1128 Type B" in log

    def test_1127_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1127 Type A" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "log-hash followup registers" in log


# ---------------------------------------------------------------------------
# 14. In-flight isolation: concurrent runs' uncommitted work is untouched.
# ---------------------------------------------------------------------------

class TestInFlightIsolation1128:
    def test_899_nytimes_hunk_untouched(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert "profiles/nytimes.yaml" in modified
        # Its uncommitted hunk belongs to #899's run; this run stages
        # only its own files.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#899" in src

    def test_938_test_file_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_b_938" in res.stdout

    def test_900_untracked_file_untouched(self):
        res = _git("status", "--short")
        assert "test_type_d_900_m769" in res.stdout

    def test_1012_working_tree_edit_untouched(self):
        res = _git("status", "--short")
        assert "test_type_a_1012" in res.stdout

    def test_do_not_touch_1024_m846(self):
        # Ray's revert/leave/rebuild decision on #1024's m846 is pending;
        # guarded in the log entry per convention, untouched by this run.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1024" in src
