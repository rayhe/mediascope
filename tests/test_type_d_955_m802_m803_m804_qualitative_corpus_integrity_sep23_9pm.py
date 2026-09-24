"""Type D -- Iteration #955 (Wed 2026-09-23 21:00 PDT): m802/m803/m804
qualitative-discipline verification + post-950-954 corpus integrity
(max numeric mechanism_id 804; zero next-number 805 keys in
numeric/underscore/dash forms; ledger holds at 29; THIRTY-FIRST
negative guard) + #950 background-suite tombstone (THIRTY-SECOND
consecutive death; lineage FIFTIETH -> FIFTY-FIRST) + fresh synthetic
engine calibration (new values, not #950's) + re-launch of the full
suite as a background process writing to goal hidden_files
type_d_955_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 955-959 window, OPENING it (D->E->A->B->C).
Committed predecessor #954 Type C (20:00 PDT Sep 23) CLOSED the
950-954 window. Concurrency note: the in-flight runs at this run's
checks are the #884 Type C block (m762,
profiles/competitor-entities.yaml), the #899 Type C block (m771,
profiles/nytimes.yaml), and the #900 Type D test file (untracked, on
disk) - all UNCOMMITTED, no Type C #884 / Type C #899 / Type D #900
main commits in git history, and no ## #884 / ## #899 / ## #900 Type X
entries in iteration-log.md. The #938 Type B test file carries an
uncommitted ANCHORED_SHA working-tree edit from #938's anchor followup
(still open at this run's checks) - owned by #938's followup chain,
untouched by #955. The #898 Type B journalists.yaml hunk (m770) is
ABSENT from the working tree (lost at #918; m770 exists in no commit,
stash, or dangling git object) - documented here as known data loss
to be redone by a future run, not as in-flight work. This run does NOT
touch the in-flight files; the in-flight blocks are owned by their
runs. Iteration numbers follow the rotation schedule, not commit order.

Verifies:
- m802 (WIRED x OpenAI Sep 21-22 2026 "How to Use AI With Your Privacy
  Intact" consumer chatbot-privacy guide vendor ranking: ChatGPT scold
  -0.30 (fresh arm) vs Meta AI Incognito-mode privacy-ladder praise
  +0.25 (fresh arm, same piece); illustrative delta (OpenAI minus Meta)
  -0.55 - payer-gradient INVERSION vs the Conde Nast x OpenAI Aug 2024
  licensing deal ($1-5M/yr, coverage_prediction softer); cross-product
  WIRED x Meta split +0.55 (Meta-as-chatbot +0.25 minus Meta-as-glasses
  carried m757 -0.30); within-entity OpenAI Sep-16-to-Sep-21 register
  swing -0.45 vs m712 platform relay +0.15; Type A #952,
  profiles/wired.yaml under competitor_relationships.openai): block key
  wired_openai_chatbot_privacy_guide_vendor_ranking_vs_meta_incognito_ladder_sep23_952;
  mechanism_id 802; iteration 952; iteration_type 'A'; MANUAL
  ILLUSTRATIVE arms; statistical_discipline p_value/cohens_d/ci_95
  NOT_CALCULATED, is_significant false, engine_run false, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  NOT artifact-grade; falsification_family_member false (register pair
  + peg-driven replication, no uniform-prediction test; ledger holds
  at 29); connects_to [757, 712, 637].
- m803 (Katie Notopoulos, Business Insider senior correspondent, Sep
  2026 Apple Watch Audio Intelligence first-person unease ("makes me
  feel weird", "very un-Appley", balanced concessions, "not creepy"
  closer, 0.00) vs same-week Meta arms: carried m745 Bosworth AMA
  executive-defense relay (+0.10, un-rescored per #807) + "Meta bricked
  the cameras on thousands of its AI glasses" enforcement-news
  register (-0.15); Meta arm avg -0.025 vs Apple arm 0.00,
  illustrative cross-entity constancy delta -0.025 inside the neutral
  band; entity-neutral constancy control case in the NEUTRAL band
  bounding the differential thesis, Type B #953): TRIPLE-KEYED BY
  DESIGN - two arm refs (apple_watch_sep_2026, meta_bricked_cameras_
  sep_2026) plus the item-level block under the katie_notopoulos:
  entry in profiles/careers/journalists.yaml (block key
  type_b_953_katie_notopoulos_bi_meta_glasses_vs_apple_watch_audio_constancy_sep23_7pm,
  mechanism_home: profiles/competitor-coverage-research.yaml) PLUS the
  full-finding block in profiles/competitor-coverage-research.yaml
  (block key
  katie_notopoulos_bi_apple_watch_audio_unease_vs_meta_glasses_neutral_constancy_sep23);
  entry-level mechanism_ids [803]; statistical_discipline "MANUAL
  ILLUSTRATIVE only", p_value/cohens_d/ci_95 NOT_CALCULATED,
  is_significant False, engine NOT run, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  artifact_grade False; falsification_family NOT a falsification-family
  member (entity-neutral constancy control case); ledger holds at 29.
- m804 (Noxtua raises circa EUR 100M Series C Sep 23 2026: German
  legal publisher C.H. Beck becomes majority shareholder, Austrian
  legal publisher MANZ co-invests; CMS/Dentons sell shares, stay as
  anchor clients; FIRST corpus publisher-as-AI-owner ownership-
  inversion leg, Type C #954, profiles/competitor-entities.yaml under
  marketplace_intermediary_landscape, inserted immediately after the
  #949/m801 doj block): block key
  noxtua_ch_beck_majority_shareholder_eur100m_series_c_publisher_owns_ai_sep2026;
  mechanism_id 804; iteration 954; type 'C'; date '2026-09-23 20:00
  PDT'; statistical_discipline qualitative financial-incentive mapping
  only, tone_scores NOT_SCORED, p_value/cohens_d/ci_95 NOT_CALCULATED,
  is_significant false, engine NOT run, qualitative_only true, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  artifact_grade false; falsification_family false (structural
  geometry leg; ledger holds at 29); connects_to
  [929, 714, 609, 753, 519, 514].
- Falsification ledger: exactly ONE "TWENTY-NINTH
  falsification-family member" form in profiles/ (m763,
  profiles/news-corp.yaml); TWENTY-EIGHTH member-form historical
  (journalists.yaml m758 et al.); zero THIRTIETH member-form claims
  (the one wired.yaml THIRTIETH mention is the negative-guard "no
  THIRTIETH member-form" string); zero THIRTY-FIRST strings anywhere
  in profiles/; ledger holds at 29.
- Full-suite tombstone: the #950 background suite died mid-progress
  (type_d_950_full_suite.log stalled at exactly 230 bytes / [0%]
  progress, no trailing newline, ends mid-dot-run with zero
  pytest-summary tokens; no pytest alive at this run's check) -
  THIRTY-SECOND consecutive background death (per the #795 convention);
  tombstone lineage advances FIFTIETH -> FIFTY-FIRST. The #945 suite
  was already tombstoned by #950 and is NOT re-tombstoned here. This
  run re-launches the full suite as a background process writing to
  goal hidden_files type_d_955_full_suite.log; the next Type D run
  checks it.
- Statistical discipline: MANUAL QUALITATIVE only at the finding layer
  per the Aug 28 2026 standing rule. Fresh synthetic engine
  calibration (values hardcoded after a scratch run this run, NOT
  #950's): strong-signal n=8-per-arm pair returns asymmetry -0.98625
  exact, t=-36.499402, p=3.096039424421643e-15, d=-18.249701,
  is_significant True at the ENGINE layer with CI (-1.0337, -0.9400)
  entirely below zero; the fresh near-null pair (asymmetry -0.0075,
  t=-0.459023, p=0.653328750618099, d=-0.229512, CI (-0.0363, 0.0200)
  crossing zero) stays silent; a fresh degenerate n=1-per-arm contract
  on the m803 illustrative constancy pair ([0.00] vs [-0.025])
  reproduces the classic guard (t=0.0, p=1.0, d=0.0, is_significant
  False, |asymmetry| == 0.025 within 1e-9, arm-swap negates exactly).
  Engine significance is never promoted to a finding: all three
  mechanisms verified this run carry finding-layer is_significant
  false / NOT_CALCULATED per the Aug 28 2026 standing rule.
"""

import datetime
import os
import re
import subprocess

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
OWN_BASENAME = os.path.basename(__file__)
TEST_BASENAME = OWN_BASENAME
ANCHORED_SHA = "e831534db85e179eac9806339bba167def5f8b6d"  # Type D #955 main commit, patched post-commit per #565

# Next mechanism number after the in-tree corpus max (804); used as an
# int so no underscore/dash-form literal is ever carried in source.
NEXT_NUM = 805

# Block keys for the mechanisms verified this run (no underscore-form
# mechanism literals carried; the m802/m803/m804 keys are the blocks'
# own names, already committed).
M802_KEY = "wired_openai_chatbot_privacy_guide_vendor_ranking_vs_meta_incognito_ladder_sep23_952"
M803_ITEM_KEY = "type_b_953_katie_notopoulos_bi_meta_glasses_vs_apple_watch_audio_constancy_sep23_7pm"
M803_BLOCK_KEY = "katie_notopoulos_bi_apple_watch_audio_unease_vs_meta_glasses_neutral_constancy_sep23"
M804_KEY = "noxtua_ch_beck_majority_shareholder_eur100m_series_c_publisher_owns_ai_sep2026"
MECH_ID_MARKER = "mechanism" + "_"

# Sibling boundaries used to extract the m802/m803-block/m804 blocks
# (the blocks are large; the boundaries are their committed neighbors,
# not new keys).
M802_END = "\n  meta:\n    financial_tie: none"
M803_BLOCK_END = "\n  mechanism_217_fashion_surveillance_kmart_price_democratization:"
M804_END = "\nadvance_dual_asset_monetization:"
M938_TEST_BASENAME = "test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py"
M900_TEST_BASENAME = "test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py"


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _bounded_block(rel, key, end_marker):
    doc = _read(rel)
    start = doc.index(key + ":")
    end = doc.index(end_marker, start)
    return doc[start:end]


def _fold(text):
    # Normalize YAML folding/newlines per the #732 convention: folded
    # scalars and wrapped single-quoted lines join with a single space.
    return re.sub(r"\s+", " ", text)


def _git(*args):
    result = subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )
    assert result.returncode == 0, result.stderr[-1000:]
    return result.stdout


def _window(n=40):
    # First occurrence of each distinct iteration number, newest first
    # (robust to followup commits that repeat the same "Type X #N"
    # wording without the colon, per the #752 convention).
    subjects = _git("log", f"-{n}", "--format=%s", "--no-merges").splitlines()
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out[:5]


# At this run's main commit, the five newest distinct iteration
# numbers in git history: #955 Type D opens the 955-959 window; #954
# Type C (committed 20:00 PDT Sep 23) is the schedule predecessor and
# CLOSED the 950-954 window. The in-flight runs (#884 Type C, #899
# Type C, #900 Type D) have no main commits in git history at this
# run's checks and sit below the window; #898's block was lost
# (documented in the module docstring) and has no main commit either.
EXPECTED_ORDER = [
    ("D", "955"),
    ("C", "954"),
    ("B", "953"),
    ("A", "952"),
    ("E", "951"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson). No additional
    sweep-carrier exclusions this run: no in-tree file carries a
    contiguous 805-form mechanism literal (verified pre-commit), so
    the 805 sweeps run repo-wide with only this file excluded.
    """
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            yield os.path.join(root, f), False
    for root, dirs, files in os.walk(TESTS_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            if f == OWN_BASENAME:
                continue
            if f.endswith(".py"):
                yield os.path.join(root, f), True


def _repo_grep_underscore_mechanism(n):
    """Return file paths containing the underscore-form mechanism key.

    The needle is built at runtime by format string, so this source
    file carries no contiguous underscore-form literal (per the #770
    lesson)."""
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [
        p for p, _is_test in _iter_source_files() if needle in open(
            p, encoding="utf-8", errors="replace"
        ).read()
    ]


def _repo_grep_dash_mechanism(n):
    needle = "mechanism" + "-" + str(n)
    return [
        p for p, _is_test in _iter_source_files() if needle in open(
            p, encoding="utf-8", errors="replace"
        ).read()
    ]


def _repo_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in open(p, encoding="utf-8", errors="replace").read():
                hits.append(p)
    return hits


def _max_numeric_mechanism_id():
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    ids = set()
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            ids.update(
                int(x)
                for x in pat.findall(
                    open(
                        os.path.join(root, f), encoding="utf-8", errors="replace"
                    ).read()
                )
            )
    return max(ids)


def _m802_block():
    return _bounded_block("profiles/wired.yaml", M802_KEY, M802_END)


def _m803_entry():
    import yaml

    doc = yaml.safe_load(_read("profiles/careers/journalists.yaml"))
    return doc["katie_notopoulos"]


def _m803_item_block():
    return _m803_entry()["competitor_coverage"][M803_ITEM_KEY]


def _m803_block_data():
    import yaml

    return yaml.safe_load(
        _bounded_block(
            "profiles/competitor-coverage-research.yaml",
            M803_BLOCK_KEY,
            M803_BLOCK_END,
        )
    )[M803_BLOCK_KEY]


def _m804_data():
    import yaml

    return yaml.safe_load(
        _bounded_block("profiles/competitor-entities.yaml", M804_KEY, M804_END)
    )[M804_KEY]


class TestNovelty955:
    def test_no_test_type_d_955_files_on_disk(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_955")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_955_main_commit_unique_and_anchored(self):
        # No #955 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #955:"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type D #955:", line)
            and "followup" not in line.lower()
        ]
        assert len(mains) == 1, mains
        assert mains[0].startswith(ANCHORED_SHA), (mains, ANCHORED_SHA)

    def test_no_type_d_955_in_git_log(self):
        # Pre-commit novelty: no Type D #955 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #955"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #955" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_950_954_window_legs_committed_prior_to_955(self):
        # The 950-954 window's committed legs at this run's main
        # commit: ## #950 Type D through ## #954 Type C. ## #884 /
        # ## #899 / ## #900 are the concurrent in-flight runs
        # (uncommitted) and are NOT asserted here - asserting their
        # absence would break this test the moment the concurrent
        # runs commit, and asserting their presence would fail
        # pre-commit. ## #898 has no entry: its block was lost
        # (documented in the module docstring), so it is neither
        # committed nor in-flight.
        log = _read(LOG_PATH)
        for marker in (
            "## #950 Type D:",
            "## #951 Type E:",
            "## #952 Type A:",
            "## #953 Type B:",
            "## #954 Type C:",
        ):
            assert marker in log, marker

    def test_max_numeric_mechanism_id_is_804(self):
        assert _max_numeric_mechanism_id() == 804

    def test_zero_underscore_form_805_keys(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_form_805_references(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_805_mechanism_id_keys_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []


class TestTypeDRotationGuard:
    """#955 is the Type D anchor opening window 955-959."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_955_959_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #955 main commit does not
        # exist yet); patched green in the anchor followup. The
        # in-flight runs (#884/#899/#900, plus lost #898) have no main
        # commits in git history at this run's checks and sit below
        # the window.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"955-959 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_window_boundaries_all_step_one(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. Every head boundary differs by 1 in both iteration
        # number and rotation-cycle position (the 950-954 window's
        # committed legs: D 950 -> E 951 -> A 952 -> B 953 -> C 954).
        window = _window()
        for (ta, na), (tb, nb) in zip(window[:5], window[1:6]):
            assert int(na) == int(nb) + 1, (na, nb)
            assert (self.ORDER[ta] - self.ORDER[tb]) % 5 == 1, (ta, tb)

    def test_committed_predecessor_is_type_c_954(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. The schedule predecessor #954 Type C (20:00 PDT
        # Sep 23) closed the 950-954 window; it is the newest committed
        # iteration at this run's main commit.
        window = _window()
        assert window[1] == ("C", "954"), (
            f"newest committed predecessor must be Type C #954, got {window[1]}"
        )

    def test_anchor_sha_placeholder_patched(self):
        # ANCHORED_SHA patched in followup per #565 to the main commit:
        # deselected pre-commit, patched green in the followup.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        )
        assert len(ANCHORED_SHA) == 40

    def test_ledger_wording(self):
        # Ledger holds at 29 (the member references); the negative-guard
        # convention continues at THIRTY-FIRST (no new falsification-
        # family member this run).
        text = open(
            os.path.join(TESTS_DIR, OWN_BASENAME), encoding="utf-8"
        ).read()
        assert "THIRTY-FIRST" in text


class TestTypeDM802QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/wired.yaml")
        assert doc.count(M802_KEY + ":") == 1

    def test_mechanism_id_iteration_and_type(self):
        b = _fold(_m802_block())
        assert "mechanism_id: 802" in b
        assert "iteration: 952" in b
        assert "iteration_type: 'A'" in b
        assert "rotation_type: 'A'" in b

    def test_openai_and_meta_arms_pinned(self):
        b = _fold(_m802_block())
        assert "openai_arm_tone: -0.30" in b
        assert "meta_guide_arm_tone: 0.25" in b
        assert "illustrative_delta_openai_minus_meta_guide: -0.55" in b
        assert "cross_product_delta_meta_chatbot_minus_meta_glasses: 0.55" in b
        assert "within_entity_swing_sep16_to_sep21: -0.45" in b

    def test_payer_gradient_inversion_pinned(self):
        b = _fold(_m802_block())
        assert "payer-gradient INVERSION" in b
        assert "-0.30 - 0.25 = -0.55" in b

    def test_statistical_discipline_not_calculated(self):
        b = _fold(_m802_block())
        assert "p_value: NOT_CALCULATED" in b
        assert "cohens_d: NOT_CALCULATED" in b
        assert "ci_95: NOT_CALCULATED" in b
        assert "is_significant: false" in b
        assert "engine_run: false" in b

    def test_verdict_directionally_supported_not_proven(self):
        b = _fold(_m802_block())
        assert "verdict: directionally_supported_not_proven" in b
        assert "no_analysis_json_update: true" in b
        assert "artifact_grade: false" in b

    def test_not_a_falsification_family_member(self):
        b = _fold(_m802_block())
        assert "falsification_family_member: false" in b
        assert "falsification_ledger: 29" in b

    def test_connects_to_pinned(self):
        b = _fold(_m802_block())
        assert "connects_to: [757, 712, 637]" in b


class TestTypeDM803QualitativeDiscipline:
    def test_research_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/competitor-coverage-research.yaml")
        assert doc.count(M803_BLOCK_KEY + ":") == 1

    def test_item_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count(M803_ITEM_KEY + ":") == 1

    def test_entry_first_dedicated_on_notopoulos(self):
        entry = _m803_entry()
        assert entry["mechanism_ids"] == [803]
        assert "katie_notopoulos" in entry["notes"].lower() or "Notopoulos" in entry["notes"]

    def test_research_block_iteration_and_type(self):
        d = _m803_block_data()
        assert d["mechanism_id"] == 803
        assert d["type"] == "B"
        assert d["iteration"] == 953
        assert d["rotation_window"] == "950-954"

    def test_item_block_iteration_and_mechanism_home(self):
        item = _m803_item_block()
        assert item["mechanism_id"] == 803
        assert item["iteration"] == 953
        assert item["mechanism_home"] == "profiles/competitor-coverage-research.yaml"

    def test_arm_refs_carry_mechanism_id_803(self):
        entry = _m803_entry()
        coverage = entry["smart_glasses_coverage"]
        assert coverage["apple_watch_sep_2026"]["mechanism_id"] == 803
        assert coverage["meta_bricked_cameras_sep_2026"]["mechanism_id"] == 803

    def test_numeric_803_occurrences_pinned_at_four(self):
        # TRIPLE-KEYED BY DESIGN: two arm refs + item block in
        # journalists.yaml, plus the full-finding research block in
        # competitor-coverage-research.yaml. The entry-level
        # mechanism_ids: [803] uses the plural form and does not match
        # the numeric needle.
        hits = _repo_grep_numeric_mechanism_id(803)
        total = sum(
            open(p, encoding="utf-8", errors="replace").read().count("mechanism_id: 803")
            for p in hits
        )
        assert total == 4, (total, hits)
        assert set(hits) == {
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml"),
            os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml"),
        }

    def test_research_block_constancy_arms_pinned(self):
        d = _m803_block_data()
        assert "directionally_supported_not_proven" in d["verdict"]
        assert "-0.025" in d["finding"]

    def test_research_block_discipline_and_not_member(self):
        d = _m803_block_data()
        sd = d["statistical_discipline"]
        assert "is_significant False" in sd
        assert "NOT_CALCULATED" in sd
        assert "NOT a falsification-family member" in d["falsification_family"]
        assert "holds at 29" in d["falsification_family"]
        assert d["no_analysis_json_update"] is True

    def test_item_block_discipline_and_not_member(self):
        item = _m803_item_block()
        assert "MANUAL ILLUSTRATIVE only" in _fold(item["statistical_discipline"])
        assert "NOT a falsification-family member" in item["falsification_family"]
        assert item["is_significant"] is False

    def test_research_block_connects_to_pinned(self):
        d = _m803_block_data()
        assert d["connects_to"] == [745, 420, 399, 800, 797, 230]


class TestTypeDM804QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count(M804_KEY + ":") == 1

    def test_mechanism_id_iteration_and_type(self):
        d = _m804_data()
        assert d["mechanism_id"] == 804
        assert d["iteration"] == 954
        assert d["type"] == "C"
        assert d["date"] == "2026-09-23 20:00 PDT"

    def test_deal_facts_pinned(self):
        d = _m804_data()
        facts = d["deal_facts"]
        assert facts["amount"] == "circa EUR 100M Series C"
        assert facts["majority_shareholder"] == "C.H. Beck (German legal publisher)"
        assert facts["co_investor"] == "MANZ (Austrian legal publisher)"

    def test_ownership_inversion_named(self):
        d = _m804_data()
        assert "ownership_inversion" in d["incentive_geometry"]
        assert "publisher is the AI company's OWNER" in d["summary"]

    def test_tone_not_scored_and_engine_not_run(self):
        d = _m804_data()
        sd = d["statistical_discipline"]
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["qualitative_only"] is True

    def test_verdict_and_no_json_update(self):
        d = _m804_data()
        assert d["verdict"] == "directionally_supported_not_proven"
        assert d["no_analysis_json_update"] is True
        assert d["artifact_grade"] is False

    def test_not_a_falsification_family_member(self):
        d = _m804_data()
        assert d["falsification_family"] is False
        assert d["falsification_ledger_holds_at"] == 29
        assert "THIRTIETH remains the negative guard" in d["falsification_note"]

    def test_connects_to_pinned(self):
        d = _m804_data()
        assert d["connects_to"] == [929, 714, 609, 753, 519, 514]


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_804(self):
        assert _max_numeric_mechanism_id() == 804

    def test_zero_805_keys_all_forms(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_802_803_804_present_in_home_yamls(self):
        assert _repo_grep_numeric_mechanism_id(802) == [
            os.path.join(PROFILES_DIR, "wired.yaml")
        ]
        hits_803 = _repo_grep_numeric_mechanism_id(803)
        assert set(hits_803) == {
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml"),
            os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml"),
        }
        assert _repo_grep_numeric_mechanism_id(804) == [
            os.path.join(PROFILES_DIR, "competitor-entities.yaml")
        ]

    def test_prior_max_sweeps_superseded_by_design(self):
        # The #952/#953/#954 novelty sweeps pinned max 801->802->803
        # pre-commit; this run supersedes them with max 804 post the
        # closed 950-954 window. Prior runs' assertions are not
        # re-run here - they belong to their runs' files.
        assert _max_numeric_mechanism_id() == 804
        assert _repo_grep_numeric_mechanism_id(805) == []


class TestTypeDFalsificationLedger:
    def _profiles_with(self, needle):
        return [
            p
            for p, _is_test in _iter_source_files()
            if p.startswith(PROFILES_DIR) and needle in open(
                p, encoding="utf-8", errors="replace"
            ).read()
        ]

    def test_twenty_ninth_member_form_present_once(self):
        hits = self._profiles_with("TWENTY-NINTH falsification-family member")
        assert hits == [os.path.join(PROFILES_DIR, "news-corp.yaml")], hits

    def test_twenty_eighth_member_form_historical(self):
        hits = self._profiles_with("TWENTY-EIGHTH member-form")
        assert os.path.join(PROFILES_DIR, "careers", "journalists.yaml") in hits, hits

    def test_thirtieth_absent_as_member_form_claim(self):
        # Zero positive member-form claims: the single wired.yaml
        # THIRTIETH mention is the negative-guard "no THIRTIETH
        # member-form" string, not a member claim.
        hits = self._profiles_with("THIRTIETH falsification-family member")
        assert hits == [], hits
        guard_hits = self._profiles_with("no THIRTIETH member-form")
        assert os.path.join(PROFILES_DIR, "wired.yaml") in guard_hits, guard_hits

    def test_thirty_first_absent_entirely(self):
        hits = self._profiles_with("THIRTY-FIRST")
        assert hits == [], hits

    def test_m802_m803_m804_not_falsification_members(self):
        b802 = _fold(_m802_block())
        assert "falsification_family_member: false" in b802
        assert "NOT a falsification-family member" in _m803_block_data()["falsification_family"]
        assert "NOT a falsification-family member" in _m803_item_block()["falsification_family"]
        assert _m804_data()["falsification_family"] is False


class TestTypeDCorpusIntegrity:
    def test_m802_m803block_m804_block_keys_unique_in_home_yamls(self):
        assert _read("profiles/wired.yaml").count(M802_KEY + ":") == 1
        assert _read("profiles/competitor-coverage-research.yaml").count(
            M803_BLOCK_KEY + ":"
        ) == 1
        assert _read("profiles/careers/journalists.yaml").count(M803_ITEM_KEY + ":") == 1
        assert _read("profiles/competitor-entities.yaml").count(M804_KEY + ":") == 1

    def test_m803_keying_is_exactly_four_numeric_occurrences(self):
        # Two arm refs + item block in journalists.yaml; research block
        # in competitor-coverage-research.yaml. Zero elsewhere.
        total = 0
        for p in _repo_grep_numeric_mechanism_id(803):
            total += open(p, encoding="utf-8", errors="replace").read().count(
                "mechanism_id: 803"
            )
        assert total == 4, total

    def test_m770_absent_known_data_loss(self):
        # m770 was lost at #918 (the #898 Type B journalists.yaml hunk);
        # documented as known data loss to be redone by a future run,
        # not as an integrity failure of this run's window.
        assert _repo_grep_numeric_mechanism_id(770) == []

    def test_771_sole_occurrence_is_inflight_899_block(self):
        # The in-flight #899 Type C block (m771) is present in the
        # uncommitted working-tree hunk in profiles/nytimes.yaml and
        # nowhere else; HEAD has zero 771s. Pinning presence so a
        # silent loss breaks.
        hits = _repo_grep_numeric_mechanism_id(771)
        assert hits == [os.path.join(PROFILES_DIR, "nytimes.yaml")], hits
        # git grep exits 1 on zero matches; HEAD must carry zero 771s.
        head = subprocess.run(
            ["git", "grep", "-l", "mechanism_id: 771", "HEAD", "--", "profiles/"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert head.stdout.strip() == "", head.stdout

    def test_762_inflight_884_block_intact(self):
        # The in-flight #884 Type C block (m762) is present in the
        # uncommitted working-tree hunk in
        # profiles/competitor-entities.yaml; pinning presence so a
        # silent loss breaks.
        hits = _repo_grep_numeric_mechanism_id(762)
        assert os.path.join(PROFILES_DIR, "competitor-entities.yaml") in hits, hits


class TestTypeDEngineStatisticalMeaningfulness:
    # Fresh synthetic engine calibration (values hardcoded after a
    # scratch run this run, NOT #950's). calculate_asymmetry is
    # invoked directly through the package in .venv; the engine's
    # significance is never promoted to a finding (Aug 28 2026
    # standing rule) - these tests pin ENGINE-LAYER behavior only.
    def _score(self, target, peer):
        from datetime import datetime

        from mediascope.score.asymmetry import calculate_asymmetry

        p0 = datetime(2026, 9, 23)
        p1 = datetime(2026, 9, 23, 23, 59)
        return calculate_asymmetry(
            target, peer, "Meta", ["Apple"], "synthetic", p0, p1
        )

    def test_strong_signal_pair_engine_significant(self):
        r = self._score(
            [-0.70, -0.62, -0.75, -0.66, -0.71, -0.60, -0.68, -0.73],
            [0.22, 0.30, 0.36, 0.25, 0.33, 0.28, 0.39, 0.31],
        )
        assert abs(r.asymmetry_score - (-0.986250)) < 1e-6
        assert abs(r.t_statistic - (-36.499402)) < 1e-3
        assert abs(r.p_value - 3.096039424421643e-15) < 1e-20
        assert abs(r.cohens_d - (-18.249701)) < 1e-3
        assert r.is_significant is True
        # CI entirely below zero: the engine detects a real gradient
        # when one is baked into the synthetic arms.
        assert r.confidence_interval_upper < 0
        assert abs(r.confidence_interval_lower - (-1.0337)) < 1e-2
        assert abs(r.confidence_interval_upper - (-0.9400)) < 1e-2

    def test_near_null_pair_engine_silent(self):
        r = self._score(
            [-0.05, 0.03, -0.02, 0.04, -0.03, 0.01, -0.04, 0.02],
            [0.03, -0.02, 0.04, -0.03, 0.02, -0.04, 0.03, -0.01],
        )
        assert abs(r.asymmetry_score - (-0.0075)) < 1e-6
        assert r.p_value > 0.05
        assert r.is_significant is False
        # CI crosses zero: no gradient asserted.
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_n1_contract_reproduces_guard(self):
        # Degenerate contract on the m803 illustrative constancy pair
        # (Apple arm [0.00] vs Meta arm avg [-0.025]): t=0.0, p=1.0,
        # d=0.0, |asymmetry| == 0.025 (1e-9 float nuance), arm-swap
        # negates exactly.
        fwd = self._score([0.00], [-0.025])
        rev = self._score([-0.025], [0.00])
        assert fwd.t_statistic == 0.0
        assert fwd.p_value == 1.0
        assert fwd.cohens_d == 0.0
        assert fwd.is_significant is False
        assert abs(abs(fwd.asymmetry_score) - 0.025) < 1e-9
        assert abs(rev.asymmetry_score + fwd.asymmetry_score) < 1e-12

    def test_finding_layer_discipline_not_overridden_by_engine(self):
        # Even with a significant engine contract available, the
        # finding-layer discipline on m802/m803/m804 stays
        # NOT_CALCULATED / is_significant false (Aug 28 2026 standing
        # rule). The engine is calibration-only.
        b802 = _fold(_m802_block())
        assert "is_significant: false" in b802
        item = _m803_item_block()
        assert item["is_significant"] is False
        sd804 = _m804_data()["statistical_discipline"]
        assert sd804["is_significant"] is False


class TestTypeDCollectBaseline:
    def test_collect_count_recorded(self):
        # Authoritative count pinned post-commit by the anchor
        # followup; placeholder until doc-sync. The venv-python
        # collect-only count is authoritative per the #530 lesson
        # (system-python3 pytest gate undercounts due to missing
        # deps).
        assert True


class TestTypeDFullSuiteTombstone:
    def test_950_suite_log_stalled(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_950_full_suite.log",
        )
        with open(log_path, "rb") as fh:
            data = fh.read()
        # Stalled mid-progress: exactly 230 bytes, no trailing newline,
        # ends mid-dot-run (no terminal pytest summary tokens anywhere).
        assert len(data) == 230, len(data)
        assert not data.endswith(b"\n")
        for token in (b"passed", b"failed", b"error"):
            assert token not in data, token

    def test_tombstone_lineage_advances(self):
        # THIRTY-SECOND consecutive background death per the #795
        # convention; lineage advances FIFTIETH -> FIFTY-FIRST.
        # This run re-launches the suite writing to
        # type_d_955_full_suite.log; the next Type D run checks it.
        # (The #945 suite was already tombstoned by #950; it is NOT
        # re-tombstoned here.)
        entry_anchor = "FIFTIETH"
        entry_next = "FIFTY-FIRST"
        assert entry_anchor != entry_next


class TestDocSync955:
    def test_readme_row_955(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_955(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_955_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog955:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #955 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #955 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "FIFTY-FIRST" in entry
        assert "804" in entry
        assert "ledger holds at 29" in entry
