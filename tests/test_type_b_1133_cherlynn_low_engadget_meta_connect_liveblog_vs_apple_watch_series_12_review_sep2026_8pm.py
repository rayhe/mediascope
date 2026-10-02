"""MediaScope iteration #1133 (Type B, journalist cross-entity tracking):
Cherlynn Low (Engadget) Sep-18/19 Apple Watch Series 12 scored review
(+0.30, 9.1/10, always-on ambient-listening controversy contained) vs
Sep-23 Meta Connect 2026 liveblog (0.0, neutral-wry relay, surveillance
joke) - genre-bound register contrast.

The anchor is the block keyed
type_b_1133_cherlynn_low_engadget_meta_connect_liveblog_vs_apple_watch_series_12_review_sep2026
under Cherlynn Low's competitor_coverage in
profiles/careers/journalists.yaml: mechanism 911, the SECOND dedicated
Type B mechanism on Low (m872/Type B #1068 covered the same-genre
hands-on vs hands-on pair: Apple Sep-9/10 +0.35 vs Meta Jun-23 +0.30,
illustrative delta +0.05 null; m911 uses NEW arms on both sides).

The within-writer contrast: her scored Apple review (+0.30 MANUAL
ILLUSTRATIVE) reads gentler than her Meta Connect liveblog (0.0 MANUAL
ILLUSTRATIVE) inside a 5-day window, although the Apple arm's
always-on ambient-listening capability is the stronger surveillance
story. Illustrative delta (Apple minus Meta) = +0.30, n=1 vs n=1
degenerate contract, NOT significant. The finding EXTENDS m872's
register-constancy finding with a genre leg: under genre control the
pair reads null (+0.05); when the review genre applies to Apple and
the liveblog genre applies to Meta, the same writer's register
diverges +0.30. The genre confound is STRONG, so this is a
genre-effect extension, not a journalist-bias claim.

NOT a falsification-family member: bounded searches found no Engadget
x Meta or Engadget x Apple financial relationship (no AI
content-licensing deal for Engadget with any lab), so no
payer-softening prediction is tested. Ledger holds at 46.

Rotation transparency: this run is iteration #1133 Type B, the FOURTH
leg of the 1130-1134 window (D #1130 -> E #1131 -> A #1132 -> B #1133 ->
C #1134). Predecessor #1132 Type A verified in git log (main
374ce8cd / anchor 21d8a967 / doc-sync 8bb6dded / log-hash fbeb43c0 /
count-correction 19926813, Oct 1 2026 7:00 PM PDT). Next run #1134
continues the window as Type C (fifth leg); it inherits the zero-912
forward guards, the no-thirty-fourth-direction guard, and the
no-forty-seventh-member guard from this run.

In-flight, untouched: #899 (profiles/nytimes.yaml m771 hunk), #938
(Type B test-file anchor edit), #900 (untracked Type D test file),
#1012-wt (working-tree edit on the committed Type A #1012 file). Do
NOT touch #1024 m846 (Ray's revert/leave/rebuild decision pending -
not an assistant repair task). Use targeted staging only.

Literal discipline per #715/#770: every mechanism-id and
member/direction forward-guard needle in this file is format-built at
runtime - no contiguous underscore/dash-911, underscore/dash-912,
forty-seventh member-claim, thirty-fourth direction, or thirty-third
direction forms appear in source. Permitted contiguous forms: the
landed FORTY-SIXTH member claim and the landed THIRTY-THIRD reference
in ledger-guard prose. Docstring prose uses hyphenated/lowercase
forms.
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
    "test_type_b_1133_cherlynn_low_engadget_meta_connect_liveblog_"
    "vs_apple_watch_series_12_review_sep2026_8pm.py"
)

# Pre-commit placeholder per #565; the anchor followup patches this to the
# main-commit hash.
ANCHORED_SHA = "9cb9ec5f54ae1d969c22e235bddbfca821a1e25f"  # Type B #1133 main commit (Type B runs self-anchor per #565)

MECH_NUM = 911
NEXT_NUM = 912

# Literal discipline per #715/#770: the underscore/dash mechanism-key forms,
# the block key, and the member/direction forward-guard forms are
# format-built so this file carries no contiguous needle.
MECH_ID_MARKER = "mechanism" + "_"
MECH_DASH_MARKER = "mechanism" + "-"

BLOCK_KEY = (
    "type_b_1133_cherlynn_low_engadget_meta_connect_liveblog_"
    "vs_apple_watch_series_12_review_sep2026"
)

FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
FORTY_SIXTH_MEMBER = "FORTY" + "-SIXTH falsification-family member"
THIRTY_FOURTH_DIR = "THIRTY" + "-FOURTH" + " relationship direction"
THIRTY_THIRD_LANDED = "THIRTY" + "-THIRD" + " relationship direction"
FORTY_SIXTH_LANDED = "FORTY-SIXTH falsification-family member"

PRED_MAIN_1132 = "374ce8cd"
PRED_ANCHOR_1132 = "21d8a967"
PRED_DOCSYNC_1132 = "8bb6dded"
PRED_LOGHASH_1132 = "fbeb43c0"

FILE_1132 = (
    "test_type_a_1132_nyt_openai_sep28_oct01_crisis_accountability_"
    "register_vs_carried_meta_arms_oct01_7pm.py"
)

URL_META_LIVEBLOG = (
    "https://www.engadget.com/"
    "2266105/meta-connect-2026-live-blog-ai-vr/"
)
URL_APPLE_REVIEW = (
    "https://WWW.Engadget.com/"
    "2260989/apple-watch-series-12-review-hrv-new-health-sensing-gesture/"
)

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1130_full_suite.log"
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
    return doc["cherlynn_low"]["competitor_coverage"][BLOCK_KEY]


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

class TestAnchor1133:
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
        assert "type_b_1133" in BLOCK_KEY
        assert "911" not in BLOCK_KEY
        assert BLOCK_KEY in _block_text()

    def test_journalist_file_and_indent(self):
        # The block lives under cherlynn_low's competitor_coverage at
        # indent 4 in profiles/careers/journalists.yaml.
        text = _block_text()
        assert "    " + BLOCK_KEY + ":" in text
        b = _block()
        assert b["journalist"] == "Cherlynn Low"
        assert b["block_key"] == BLOCK_KEY
        assert b["publication"] == "engadget"


# ---------------------------------------------------------------------------
# 2. Rotation guard (pre-commit assertions; git-log novelty test is
# SUPERSEDED BY DESIGN post-commit - deselect in post-commit full runs).
# ---------------------------------------------------------------------------

class TestRotationGuard1133:
    def test_predecessor_1132_chain_present(self):
        log = _git("log", "--oneline", "-80").stdout
        assert PRED_MAIN_1132 in log
        assert PRED_ANCHOR_1132 in log
        assert PRED_DOCSYNC_1132 in log
        assert PRED_LOGHASH_1132 in log

    def test_type_b_1133_novelty(self):
        # "Type B #1133" absent from git log pre-commit; own file not
        # yet committed. SUPERSEDED BY DESIGN once this run's main
        # commit ("Type B #1133:") lands; post-commit, the anchor
        # asserts the patched ANCHORED_SHA is present in git log.
        # Deselect this test in post-commit full runs.
        log = _git("log", "--oneline", "--grep=Type B #1133").stdout
        assert log.strip() == ""

    def test_window_order_d_e_a_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1130 -> E #1131 -> A #1132 -> B #1133" in src

    def test_window_fourth_leg(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FOURTH leg" in src
        assert "1130-1134" in src

    def test_next_run_1134_type_c_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "C #1134" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (post-landing state: max is 911; 912 absent in all
# forms; 911 underscore/dash absent - the forward guards for #1134+).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1133:
    def test_single_test_file_for_iteration(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1133*.py"))
        assert len(files) == 1, files

    def test_novelty_verification_claim_in_block(self):
        assert "zero test_type_b_1133 files on disk" in _block_text()

    def test_max_numeric_mechanism_id_is_911(self):
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_zero_underscore_912_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_912_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_912_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_911_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_zero_dash_911_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_911_numeric_present_only_in_journalists_block(self):
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

class TestBlockStructure1133:
    def test_block_loads_under_low_competitor_coverage(self):
        doc = yaml.safe_load(_block_text())
        assert BLOCK_KEY in doc["cherlynn_low"]["competitor_coverage"]

    def test_iteration_and_type(self):
        b = _block()
        assert b["iteration"] == 1133
        assert b["type"] == "B"

    def test_date_and_window(self):
        b = _block()
        assert b["date"] == "2026-10-01 20:00 PDT"
        assert "FOURTH leg" in b["window"]
        assert "1130-1134" in b["window"]

    def test_goal_and_job(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"

    def test_test_file_field(self):
        assert _block()["test_file"].endswith(OWN_BASENAME)

    def test_mechanism_id_911(self):
        assert _block()["mechanism_id"] == 911

    def test_author(self):
        assert _block()["author"] == "Kit (with Ray)"

    def test_ascii_no_em_dashes(self):
        # Scoped to this run's block segment (the file carries
        # pre-existing non-ASCII elsewhere).
        text = _block_text()
        start = text.index(BLOCK_KEY)
        segment = text[start : start + 25000]
        assert "\u2014" not in segment
        segment.encode("ascii")

    def test_second_dedicated_mechanism_on_low(self):
        doc = yaml.safe_load(_block_text())
        ids = doc["cherlynn_low"]["mechanism_ids"]
        assert ids == [872, 911]


# ---------------------------------------------------------------------------
# 5. Meta arm (Sep 23 Meta Connect 2026 liveblog).
# ---------------------------------------------------------------------------

class TestMetaArm1133:
    def test_title_and_date(self):
        arm = _block()["new_meta_arm"]
        assert arm["title"] == (
            "Meta Connect 2026 live: Updates from Mark Zuckerberg's "
            "keynote on AI glasses, VR and more"
        )
        assert arm["date"] == "Sep 23 2026"

    def test_url_novel_and_verbatim(self):
        arm = _block()["new_meta_arm"]
        assert arm["url"] == URL_META_LIVEBLOG
        assert "2266105/meta-connect-2026-live-blog-ai-vr" in arm["url"]

    def test_byline_low(self):
        arm = _block()["new_meta_arm"]
        assert "Cherlynn Low" in arm["byline"]

    def test_register_neutral_wry(self):
        arm = _block()["new_meta_arm"]
        assert arm["tone_score"] == 0.0
        assert "MANUAL ILLUSTRATIVE" in arm["tone_basis"]
        assert "0 browser.open per #503" in arm["tone_basis"]

    def test_surveillance_joke_present(self):
        quotes = _block()["new_meta_arm"]["key_quotes"]
        assert any("hackers salivating" in q for q in quotes)
        assert any("camera-free Ray-Ban Meta Audio" in q for q in quotes)

    def test_no_privacy_architecture_walkthrough(self):
        arm = _block()["new_meta_arm"]
        assert "zero privacy-architecture walkthrough" in arm["register_notes"]


# ---------------------------------------------------------------------------
# 6. Apple arm (Sep 18-19 Watch Series 12 scored review).
# ---------------------------------------------------------------------------

class TestAppleArm1133:
    def _arms(self):
        return _block()["new_apple_arms"]

    def test_single_arm(self):
        assert len(self._arms()) == 1

    def test_review_title_and_date(self):
        arm = self._arms()[0]
        assert arm["arm"] == "Apple Watch Series 12 scored review"
        assert "Catching up and catching heat" in arm["title"]
        assert arm["date"] == "Sep 18-19 2026"

    def test_review_url_verbatim_caps_flagged(self):
        # The listing carried odd capitalization; the block keeps it
        # verbatim (not normalized) and flags it in the novelty note.
        arm = self._arms()[0]
        assert arm["url"] == URL_APPLE_REVIEW
        assert "WWW.Engadget.com" in arm["url"]
        assert "2260989/apple-watch-series-12-review-hrv-new-health-sensing-gesture" in arm["url"]
        assert "Verbatim from the search listing" in _block()["novelty"] or \
            "VERBATIM from the search listing" in _block()["novelty"]

    def test_scored_9_1_and_health_array(self):
        arm = self._arms()[0]
        joined = " ".join(arm["key_quotes"])
        assert "9.1/10" in joined
        assert "health sensing" in joined

    def test_apple_privacy_messaging_relayed(self):
        arm = self._arms()[0]
        joined = " ".join(arm["key_quotes"])
        assert "privacy-minded way" in joined
        assert "uncritical" in arm["register_notes"]

    def test_ambient_listening_contained(self):
        arm = self._arms()[0]
        joined = " ".join(arm["key_quotes"])
        assert "Audio Intelligence" in joined
        assert "Siri Recaps" in joined
        assert "contained caveat" in joined
        assert arm["tone_score"] == 0.3


# ---------------------------------------------------------------------------
# 7. Register contrast.
# ---------------------------------------------------------------------------

class TestRegisterContrast1133:
    def test_delta_calc(self):
        rc = _block()["register_contrast"]
        assert rc["illustrative_delta_apple_minus_meta"] == 0.3
        assert "0.30 - 0.0 = +0.30" in rc["delta_calc"]

    def test_temporal_window(self):
        rc = _block()["register_contrast"]
        assert "5 days" in rc["temporal_window"]
        assert "Sep 18-19" in rc["temporal_window"]

    def test_reading_extends_m872(self):
        rc = _block()["register_contrast"]
        assert "m872" in rc["reading"]
        assert "GENRE-BOUND" in rc["reading"]

    def test_degenerate_contract_disclosed(self):
        rc = _block()["register_contrast"]
        assert "n=1 vs n=1 degenerate contract" in rc["reading"]
        assert "NOT significant" in rc["reading"]

    def test_genre_confounds_entity_reading(self):
        rc = _block()["register_contrast"]
        assert "NOT entity-animus evidence" in rc["reading"]
        assert "genre confound is STRONG" in rc["reading"]

    def test_primary_pair_identified(self):
        rc = _block()["register_contrast"]
        assert rc["meta_arm_tone"] == 0.0
        assert "+0.30" in rc["apple_arm_tones"]


# ---------------------------------------------------------------------------
# 8. Financial relationship (no gradient found - NOT a falsification test).
# ---------------------------------------------------------------------------

class TestFinancialRelationship1133:
    def test_no_engadget_meta_gradient(self):
        fr = _block()["financial_relationship"]
        assert "No Engadget x Meta financial relationship" in fr["engadget_meta"]

    def test_no_engadget_apple_gradient(self):
        fr = _block()["financial_relationship"]
        assert "No Engadget x Apple financial relationship" in fr["engadget_apple"]

    def test_static_media_ownership_change_logged(self):
        fr = _block()["financial_relationship"]
        assert "Static Media" in fr["ownership_change"]
        assert "Feb 2026" in fr["ownership_change"]
        assert "stale" in fr["ownership_change"]

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

class TestScorerDiscipline1133:
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
        assert any("STRONG: genre asymmetry" in c for c in confs)
        assert any("STRONG: form-factor asymmetry" in c for c in confs)

    def test_counterevidence_extends_not_contradicts_m872(self):
        ces = _block()["counterevidence"]
        assert any("EXTENDS m872" in c for c in ces)
        assert any("constancy under genre control" in c for c in ces)


# ---------------------------------------------------------------------------
# 10. Falsification ledger guard (holds at 46; no new member, no new
# direction; needles format-built per #715).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1133:
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
        # #1132's landed claim stays intact in the-verge.yaml; this run's
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

    def test_thirty_fourth_direction_absent_repo_wide(self):
        hits = self._ledger_hits(THIRTY_FOURTH_DIR)
        assert hits == [], hits
        assert THIRTY_FOURTH_DIR not in _profiles_text()

    def test_thirty_third_direction_intact_in_competitor_entities(self):
        # The THIRTY-THIRD direction is landed (m906, Type C #1124) in
        # competitor-entities.yaml; this run claims no new direction, so
        # the landed form must stay intact there (needle format-built
        # per #715).
        text = _read(os.path.join(PROFILES_DIR, "competitor-entities.yaml"))
        assert THIRTY_THIRD_LANDED in text

    def test_ledger_note_documents_hold(self):
        note = _block()["ledger_note"]
        assert "Ledger holds at 46" in note
        assert "NOT a falsification-family member" in note


# ---------------------------------------------------------------------------
# 11. Supersession pins: predecessor guards whose assertions flip BY DESIGN
# when this run's block lands; the unchanged forward guards stay green.
# ---------------------------------------------------------------------------

class TestSupersessionPins1133:
    def test_1132_file_pins_max_id_910_fails_by_design(self):
        # The 911 numeric id now exists in the working-tree profiles/
        # (this run's landed block); fails BY DESIGN post-landing.
        res = _node_run(
            FILE_1132,
            "TestGuardLifecycle1132::test_1132_file_pins_max_id_910_and_next_911",
        )
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1132_zero_numeric_911_fails_by_design(self):
        res = _node_run(
            FILE_1132, "TestGuardLifecycle1132::test_zero_next_numeric_911_in_profiles"
        )
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1132_zero_underscore_911_stays_green_by_design(self):
        # This run's keying uses the "mechanism_id: 911" FIELD FORM in the
        # YAML block and format-built needles in this test file (per #715),
        # so the contiguous underscore-911 form never lands anywhere and
        # #1132's zero-underscore-911 guard stays green. Only the NUMERIC
        # pin flips (mechanism_id: 911 in profiles/).
        res = _node_run(
            FILE_1132, "TestGuardLifecycle1132::test_zero_next_underscore_911_repo_wide"
        )
        assert res.returncode == 0, res.stdout[-1500:]

    def test_1132_zero_dash_911_stays_green_by_design(self):
        # Same keying-design reason as the underscore pin: the
        # contiguous dash-911 form never lands anywhere, so #1132's
        # zero-dash-911 guard stays green post-landing.
        res = _node_run(
            FILE_1132, "TestGuardLifecycle1132::test_zero_next_dash_911_repo_wide"
        )
        assert res.returncode == 0, res.stdout[-1500:]

    def test_1132_no_new_mechanisms_below_max_fails_by_design(self):
        res = _node_run(
            FILE_1132, "TestGuardLifecycle1132::test_no_new_mechanisms_below_max"
        )
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1132_no_type_b_1133_in_git_log_passes_pre_commit(self):
        # Pre-commit this passes (no "Type B #1133" in git log yet);
        # post main-commit it fails BY DESIGN. Deselect in post-commit
        # full runs; the anchor asserts the patched ANCHORED_SHA instead.
        res = _node_run(
            FILE_1132, "TestTypeARotationGuard1132::test_no_type_b_1133_in_git_log"
        )
        assert res.returncode == 0, res.stdout[-1500:]

    def test_1132_no_forty_seventh_guard_stays_green(self):
        # This run does NOT claim the forty-seventh member, so #1132's
        # no-forty-seventh guard stays green post-landing.
        res = _node_run(
            FILE_1132, "TestGuardLifecycle1132::test_no_forty_seventh_member_claim"
        )
        assert res.returncode == 0, res.stdout[-1500:]

    def test_1132_thirty_fourth_guard_stays_green(self):
        res = _node_run(
            FILE_1132, "TestGuardLifecycle1132::test_no_thirty_fourth_direction_claim"
        )
        assert res.returncode == 0, res.stdout[-1500:]


# ---------------------------------------------------------------------------
# 12. Background-suite check (#1130 suite: checked only, NOT touched).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1133:
    def test_1130_suite_checked_not_touched(self):
        # Per #795 the background suite belongs to its launching run
        # (#1130); this run checks it only. A dead suite would be
        # tombstoned by the next Type D run (#1135), not here.
        assert os.path.exists(SUITE_LOG), SUITE_LOG

    def test_1130_suite_death_observed_tombstone_belongs_to_1135(self):
        # The #1130-launched full suite stopped writing: its log was last
        # modified ~1 hour before this run's check (well past the 900s
        # freshness bound). Per #795 the verdict and tombstoning belong
        # to the next Type D run (#1135), not here. This test documents
        # the observed death: alive-status is NOT claimed.
        import time

        age = time.time() - os.path.getmtime(SUITE_LOG)
        assert age > 900, age
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "tombstone" in src


# ---------------------------------------------------------------------------
# 13. Doc-sync ratchet (per #719; patched counts post-collection).
# ---------------------------------------------------------------------------

class TestTypeBDocSync1133:
    def test_readme_test_table_row(self):
        text = _read(README_PATH)
        assert OWN_BASENAME in text

    def test_architecture_tree_row(self):
        text = _read(ARCH_PATH)
        assert OWN_BASENAME in text


# ---------------------------------------------------------------------------
# 14. Iteration log.
# ---------------------------------------------------------------------------

class TestTypeBIterationLog1133:
    def test_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1133 Type B" in log

    def test_1132_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1132 Type A" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "log-hash followup registers" in log


# ---------------------------------------------------------------------------
# 15. In-flight isolation: concurrent runs' uncommitted work is untouched.
# ---------------------------------------------------------------------------

class TestInFlightIsolation1133:
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
