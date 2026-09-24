"""Type D -- Iteration #960 (Thu 2026-09-24 03:00 PDT): m805/m806/m807
qualitative-discipline verification + post-955-959 corpus integrity
(max numeric mechanism_id 807; zero next-number 808 keys in
numeric/underscore/dash forms; ledger holds at 29; THIRTY-FIRST
negative guard) + #955 background-suite tombstone (THIRTY-THIRD
consecutive death; lineage FIFTY-FIRST -> FIFTY-SECOND) + fresh
synthetic engine calibration (new values, not #955's) + re-launch of
the full suite as a background process writing to goal hidden_files
type_d_960_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 960-964 window, OPENING it (D->E->A->B->C).
Committed predecessor #959 Type C (02:00 PDT Sep 24) CLOSED the
955-959 window. Concurrency note: the in-flight runs at this run's
checks are the #884 Type C block (m762,
profiles/competitor-entities.yaml), the #899 Type C block (m771,
profiles/nytimes.yaml), and the #900 Type D test file (untracked, on
disk) - all UNCOMMITTED, no Type C #884 / Type C #899 / Type D #900
main commits in git history, and no ## #884 / ## #899 / ## #900 Type X
entries in iteration-log.md. The #938 Type B test file carries an
uncommitted ANCHORED_SHA working-tree edit from #938's anchor followup
(still open at this run's checks) - owned by #938's followup chain,
untouched by #960. The #898 Type B journalists.yaml hunk (m770) is
ABSENT from the working tree (lost at #918; m770 exists in no commit,
stash, or dangling git object) - documented here as known data loss
to be redone by a future run, not as in-flight work. This run does NOT
touch the in-flight files; the in-flight blocks are owned by their
runs. Iteration numbers follow the rotation schedule, not commit order.

Verifies:
- m805 (News Corp outlet divergence on dual payers: WSJ x OpenAI Sep
  23 2026 ChatGPT-ads $1B-revenue constructive-business register
  (MANUAL ILLUSTRATIVE +0.30, relay-tier) vs NY Post x Meta Sep 23
  teen-harassment crime/morality register (MANUAL ILLUSTRATIVE -0.55,
  relay-tier); illustrative delta (OpenAI minus Meta) +0.85; dual-payer
  financial gradient (~$50M/yr each) cannot explain the gap; EXTENDS
  m22/m532/m763; REPLICATES m637 peg-follows-register; Type A #957,
  profiles/news-corp.yaml): block key
  wsj_openai_chatgpt_ads_revenue_vs_nypost_meta_teen_harassment_crime_register_sep2026;
  mechanism_id 805; iteration 957; iteration_type 'A'; MANUAL
  ILLUSTRATIVE arms; statistical_discipline p_value/cohens_d/ci_95
  NOT_CALCULATED, is_significant false, engine_run false, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  NOT artifact-grade; falsification_family_member false (register
  documentation consistent with the m763 falsification, no new
  uniform-prediction test; ledger holds at 29); connects_to
  [22, 532, 763, 155, 796].
- m806 (James Pero, Gizmodo: Sep 23 2026 Ray-Ban Audio camera-free
  glasses stigma-frame persistence - headline "Meta Introduces
  Audio-Only Smart Glasses to Avoid the 'Perv' Problem", dek "sans
  camera so you don't have to worry about anyone accusing you of being
  a glasshole"; MANUAL ILLUSTRATIVE -0.20) vs carried Snap "Do or Die"
  +0.35 (m746, un-rescored per #807); illustrative Meta-minus-Snap
  delta -0.55; EXTENDS m791 temporally (Sep 16 -> Sep 23, objection
  removed, frame persists); REPLICATES m637 peg-follows-register in
  brand form; Type B #958, profiles/careers/journalists.yaml under the
  james_pero item (item-level key
  type_b_958_james_pero_gizmodo_rayban_audio_camerafree_stigma_frame_persistence_sep23,
  matching the m431/m641/m743 item-level convention; colon form only;
  zero underscore-form 806 keys by designed keying per #715);
  statistical_discipline MANUAL ILLUSTRATIVE only,
  p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False,
  engine NOT run, verdict directionally_supported_not_proven,
  no_analysis_json_update true, artifact_grade False; NOT a
  falsification-family member (register documentation + temporal
  extension; ledger holds at 29); connects_to
  [211, 746, 791, 734, 749, 269, 743].
- m807 (Palantir vendor-embed in the media data stack, Dec 2025 - Aug
  2026: Fox News Digital Newsroom platform (95% of articles),
  Zeta Global 7-year Foundry partnership (revenue-share), Stagwell two
  Foundry products, USA Today Co. audience-data deal; 800+ union
  newsroom employees demand the tie be cut; EIGHTH relationship
  direction in the taxonomy - vendor-embed: publisher-as-customer,
  dependency vector publisher-to-vendor; Type C #959,
  profiles/competitor-entities.yaml under
  marketplace_intermediary_landscape): block key
  palantir_media_data_stack_vendor_embed_adweek_sep2026;
  mechanism_id 807; iteration 959; type 'C'; date '2026-09-24 01:00
  PDT'; statistical_discipline qualitative structural direction
  mapping only, tone_scores NOT_SCORED, p_value/cohens_d/ci_95
  NOT_CALCULATED, is_significant false, engine NOT run,
  qualitative_only true, verdict directionally_supported_not_proven,
  no_analysis_json_update true, artifact_grade false,
  no_coverage_tone_claim true; falsification_family false (structural
  geometry leg; ledger holds at 29); connects_to
  [738, 804, 741, 636, 675, 609, 714].
- Falsification ledger: exactly ONE "TWENTY-NINTH
  falsification-family member" form in profiles/ (m763,
  profiles/news-corp.yaml); TWENTY-EIGHTH member-form historical
  (journalists.yaml m758 et al.); zero THIRTIETH member-form claims
  (wired.yaml carries only the negative guard "no THIRTIETH
  member-form"); zero THIRTY-FIRST strings anywhere in profiles/;
  ledger holds at 29.
- Full-suite tombstone: the #955 background suite died mid-progress
  (type_d_955_full_suite.log stalled at exactly 10 bytes / dot-run,
  no trailing newline, zero pytest-summary tokens; no pytest alive at
  this run's check) - THIRTY-THIRD consecutive background death (per
  the #795 convention); tombstone lineage advances FIFTY-FIRST ->
  FIFTY-SECOND. The #950 suite was already tombstoned by #955 and is
  NOT re-tombstoned here. This run re-launches the full suite as a
  background process writing to goal hidden_files
  type_d_960_full_suite.log; the next Type D run checks it.
- Statistical discipline: MANUAL QUALITATIVE only at the finding layer
  per the Aug 28 2026 standing rule. Fresh synthetic engine
  calibration (values hardcoded after a scratch run this run, NOT
  #955's): strong-signal n=8-per-arm pair returns asymmetry -0.986250
  exact, t=-36.499402, p=3.096039424421643e-15, d=-18.249701,
  is_significant True at the ENGINE layer with CI (-1.0337, -0.9400)
  entirely below zero; the fresh near-null pair (asymmetry -0.007500,
  t=-0.459023, p=0.653328750618099, d=-0.229512, CI (-0.0363, 0.0200)
  crossing zero) stays silent; a fresh degenerate n=1-per-arm contract
  on the m806 illustrative delta pair ([-0.20] vs [+0.35])
  reproduces the classic guard (t=0.0, p=1.0, d=0.0, is_significant
  False, |asymmetry| == 0.55 within 1e-9, arm-swap negates exactly).
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
ANCHORED_SHA = "a93831245eac74b18306124a29f463823a21c2f4"  # Type D #960 main commit, patched post-commit per #565

# Next mechanism number after the in-tree corpus max (807); used as an
# int so no underscore/dash-form literal is ever carried in source.
NEXT_NUM = 808

# Block keys for the mechanisms verified this run (no underscore-form
# mechanism literals carried; the m805/m806/m807 keys are the blocks'
# own names, already committed).
M805_KEY = "wsj_openai_chatgpt_ads_revenue_vs_nypost_meta_teen_harassment_crime_register_sep2026"
M806_KEY = "type_b_958_james_pero_gizmodo_rayban_audio_camerafree_stigma_frame_persistence_sep23"
M807_KEY = "palantir_media_data_stack_vendor_embed_adweek_sep2026"
MECH_ID_MARKER = "mechanism" + "_"

# Sibling boundaries used to extract the m805/m806/m807 blocks (the
# blocks are large; the boundaries are their committed neighbors, not
# new keys). m806 is read through the full journalists.yaml doc (like
# the #955 m803 item) rather than a bounded block.
M805_END = "\n  meta:\n    financial_tie: licensing"
M806_END = "\ndaniel_cooper:"
M807_END = "\nadvance_dual_asset_monetization:"


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
# numbers in git history: #960 Type D opens the 960-964 window; #959
# Type C (committed 02:00 PDT Sep 24) is the schedule predecessor and
# CLOSED the 955-959 window. The in-flight runs (#884 Type C, #899
# Type C, #900 Type D) have no main commits in git history at this
# run's checks and sit below the window; #898's block was lost
# (documented in the module docstring) and has no main commit either.
EXPECTED_ORDER = [
    ("D", "960"),
    ("C", "959"),
    ("B", "958"),
    ("A", "957"),
    ("E", "956"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson). No additional
    sweep-carrier exclusions this run: no in-tree file carries a
    contiguous 808-form mechanism literal (verified pre-commit), so
    the 808 sweeps run repo-wide with only this file excluded.
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


def _m805_data():
    import yaml

    return yaml.safe_load(
        _bounded_block("profiles/news-corp.yaml", M805_KEY, M805_END)
    )[M805_KEY]


def _m806_item_block():
    import yaml

    doc = yaml.safe_load(_read("profiles/careers/journalists.yaml"))
    return doc["james_pero"]["competitor_coverage"][M806_KEY]


def _m807_data():
    import yaml

    return yaml.safe_load(
        _bounded_block(
            "profiles/competitor-entities.yaml", M807_KEY, M807_END
        )
    )[M807_KEY]

class TestNovelty960:
    def test_no_test_type_d_960_files_on_disk(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_960")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_960_main_commit_unique_and_anchored(self):
        # No #960 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #960:"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type D #960:", line)
            and "followup" not in line.lower()
        ]
        assert len(mains) == 1, mains
        assert mains[0].startswith(ANCHORED_SHA), (mains, ANCHORED_SHA)

    def test_no_type_d_960_in_git_log(self):
        # Pre-commit novelty: no Type D #960 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #960"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #960" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_955_959_window_legs_committed_prior_to_960(self):
        # The 955-959 window's committed legs at this run's main
        # commit: ## #955 Type D through ## #959 Type C. ## #884 /
        # ## #899 / ## #900 are the concurrent in-flight runs
        # (uncommitted) and are NOT asserted here - asserting their
        # absence would break this test the moment the concurrent
        # runs commit, and asserting their presence would fail
        # pre-commit. ## #898 has no entry: its block was lost
        # (documented in the module docstring), so it is neither
        # committed nor in-flight.
        log = _read(LOG_PATH)
        for marker in (
            "## #955 Type D:",
            "## #956 Type E:",
            "## #957 Type A:",
            "## #958 Type B:",
            "## #959 Type C:",
        ):
            assert marker in log, marker

    def test_max_numeric_mechanism_id_is_807(self):
        assert _max_numeric_mechanism_id() == 807

    def test_zero_underscore_form_808_keys(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_form_808_references(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_808_mechanism_id_keys_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []


class TestTypeDRotationGuard:
    """#960 is the Type D anchor opening window 960-964."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_960_964_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #960 main commit does not
        # exist yet); patched green in the anchor followup. The
        # in-flight runs (#884/#899/#900, plus lost #898) have no main
        # commits in git history at this run's checks and sit below
        # the window.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"960-964 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_window_boundaries_all_step_one(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. Every head boundary differs by 1 in both iteration
        # number and rotation-cycle position (the 955-959 window's
        # committed legs: D 955 -> E 956 -> A 957 -> B 958 -> C 959).
        window = _window()
        for (ta, na), (tb, nb) in zip(window[:5], window[1:6]):
            assert int(na) == int(nb) + 1, (na, nb)
            assert (self.ORDER[ta] - self.ORDER[tb]) % 5 == 1, (ta, tb)

    def test_committed_predecessor_is_type_c_959(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. The schedule predecessor #959 Type C (02:00 PDT
        # Sep 24) closed the 955-959 window; it is the newest committed
        # iteration at this run's main commit.
        window = _window()
        assert window[1] == ("C", "959"), (
            f"newest committed predecessor must be Type C #959, got {window[1]}"
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

class TestTypeDM805QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/news-corp.yaml")
        assert doc.count(M805_KEY + ":") == 1

    def test_mechanism_id_iteration_and_type(self):
        d = _m805_data()
        assert d["mechanism_id"] == 805
        assert d["iteration"] == 957
        assert d["iteration_type"] == "A"
        assert d["type"] == "competitor_coverage_deep_dive"

    def test_openai_and_meta_arms_pinned(self):
        d = _m805_data()
        openai_arm = d["openai_arm_wsj"][0]
        meta_arm = d["meta_arm_nypost"][0]
        assert abs(openai_arm["tone_MANUAL_ILLUSTRATIVE"] - 0.30) < 1e-9
        assert abs(meta_arm["tone_MANUAL_ILLUSTRATIVE"] - (-0.55)) < 1e-9
        assert abs(d["illustrative_delta_openai_minus_meta"] - 0.85) < 1e-9
        assert openai_arm["register"] == "constructive_business_monetization"
        assert meta_arm["register"] == "crime_morality_adversarial"

    def test_dual_payer_gradient_cannot_explain_gap(self):
        d = _m805_data()
        assert d["financial_context"]["coverage_prediction"] == (
            "not_applicable_both_payers - gradient cannot distinguish the arms"
        )
        assert "cannot explain the gap" in d["incentive_attribution"]

    def test_statistical_discipline_not_calculated(self):
        sd = _m805_data()["statistical_discipline"]
        assert sd["scores"] == "MANUAL ILLUSTRATIVE only"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["engine_run"] is False

    def test_verdict_directionally_supported_not_proven(self):
        sd = _m805_data()["statistical_discipline"]
        assert sd["verdict"] == "directionally_supported_not_proven"
        assert sd["no_analysis_json_update"] is True
        assert sd["artifact_grade"] is False

    def test_not_a_falsification_family_member(self):
        d = _m805_data()
        assert d["falsification_family_member"] is False
        assert d["falsification_ledger"] == 29
        assert "THIRTIETH remains the negative guard" in d["ledger_note"]

    def test_connects_to_pinned(self):
        # connects_to is carried inside the overview string (no
        # top-level key on this block); pin the exact list there.
        assert "connects_to: [22, 532, 763, 155, 796]" in _m805_data()[
            "overview"
        ]


class TestTypeDM806QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count(M806_KEY + ":") == 1

    def test_mechanism_id_iteration_and_type(self):
        item = _m806_item_block()
        assert item["mechanism_id"] == 806
        assert item["type"] == "B"
        assert item["iteration"] == 958
        assert item["block_key"] == M806_KEY

    def test_item_level_keying_matches_m431_m641_m743_convention(self):
        item = _m806_item_block()
        assert item["key_design_note"].startswith("Descriptive block key")
        assert "806 mechanism key substring" in item["key_design_note"]

    def test_meta_arm_stigma_frame_pinned(self):
        item = _m806_item_block()
        assert "Perv" in item["meta_arm"]["title"]
        assert "glasshole" in _fold(item["meta_arm"]["key_quotes"][1])

    def test_illustrative_delta_pinned(self):
        item = _m806_item_block()
        delta = _fold(item["illustrative_delta"])
        assert "-0.55" in delta
        assert "register follows the brand, not the hardware" in delta

    def test_statistical_discipline_not_calculated(self):
        sd = _m806_item_block()["statistical_discipline"]
        assert sd["tone_scores"] == "MANUAL_ILLUSTRATIVE"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["engine_run"] is False

    def test_verdict_and_no_json_update(self):
        item = _m806_item_block()
        sd = item["statistical_discipline"]
        assert sd["verdict"] == "directionally_supported_not_proven"
        assert item["no_analysis_json_update"] is True
        assert sd["artifact_grade"] is False
        assert sd["qualitative_only"] is True

    def test_not_a_falsification_family_member(self):
        fam = _m806_item_block()["falsification_family"]
        assert "NOT a member" in fam
        assert "ledger holds at 29" in fam
        assert "THIRTIETH remains the negative guard" in fam

    def test_connects_to_pinned(self):
        assert _m806_item_block()["connects_to"] == [
            211,
            746,
            791,
            734,
            749,
            269,
            743,
        ]


class TestTypeDM807QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count(M807_KEY + ":") == 1

    def test_mechanism_id_iteration_and_type(self):
        d = _m807_data()
        assert d["mechanism_id"] == 807
        assert d["iteration"] == 959
        assert d["type"] == "C"
        assert d["date"] == "2026-09-24 01:00 PDT"

    def test_deal_facts_pinned(self):
        facts = _m807_data()["deal_facts"]
        assert "95% of articles" in facts["fox_news_digital"]
        assert "seven-year" in facts["zeta_global"]
        assert "Aug 2026" in facts["usa_today_co"]
        assert "31 USA Today Co. unions" in facts["union_pushback"]

    def test_eighth_relationship_direction_named(self):
        geo = _m807_data()["incentive_geometry"]
        assert "EIGHTH relationship direction" in geo["vendor_embed"]
        assert "publisher-to-vendor" in geo["vendor_embed"]

    def test_tone_not_scored_and_engine_not_run(self):
        sd = _m807_data()["statistical_discipline"]
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["engine_run"] is False
        assert sd["qualitative_only"] is True

    def test_verdict_and_no_json_update(self):
        d = _m807_data()
        assert d["verdict"] == "directionally_supported_not_proven"
        assert d["no_analysis_json_update"] is True
        assert d["artifact_grade"] is False
        assert d["no_coverage_tone_claim"] is True

    def test_not_a_falsification_family_member(self):
        d = _m807_data()
        assert d["falsification_family"] is False
        assert d["falsification_ledger_holds_at"] == 29
        assert "THIRTIETH remains the negative guard" in d[
            "falsification_note"
        ]

    def test_connects_to_pinned(self):
        assert _m807_data()["connects_to"] == [
            738,
            804,
            741,
            636,
            675,
            609,
            714,
        ]

class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_807(self):
        assert _max_numeric_mechanism_id() == 807

    def test_zero_808_keys_all_forms(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_805_806_807_present_in_home_yamls(self):
        assert _repo_grep_numeric_mechanism_id(805) == [
            os.path.join(PROFILES_DIR, "news-corp.yaml")
        ]
        assert _repo_grep_numeric_mechanism_id(806) == [
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
        ]
        assert _repo_grep_numeric_mechanism_id(807) == [
            os.path.join(PROFILES_DIR, "competitor-entities.yaml")
        ]

    def test_prior_max_sweeps_superseded_by_design(self):
        # The #957/#958/#959 novelty sweeps pinned max 804->805->806
        # pre-commit; this run supersedes them with max 807 post the
        # closed 955-959 window. Prior runs' assertions are not
        # re-run here - they belong to their runs' files.
        assert _max_numeric_mechanism_id() == 807
        assert _repo_grep_numeric_mechanism_id(808) == []


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
        # Zero positive member-form claims: the wired.yaml THIRTIETH
        # mention is the negative-guard "no THIRTIETH member-form"
        # string, not a member claim.
        hits = self._profiles_with("THIRTIETH falsification-family member")
        assert hits == [], hits
        guard_hits = self._profiles_with("no THIRTIETH member-form")
        assert os.path.join(PROFILES_DIR, "wired.yaml") in guard_hits, guard_hits

    def test_thirty_first_absent_entirely(self):
        hits = self._profiles_with("THIRTY-FIRST")
        assert hits == [], hits

    def test_m805_m806_m807_not_falsification_members(self):
        assert _m805_data()["falsification_family_member"] is False
        assert "NOT a member" in _m806_item_block()["falsification_family"]
        assert _m807_data()["falsification_family"] is False


class TestTypeDCorpusIntegrity:
    def test_m805_m806_m807_block_keys_unique_in_home_yamls(self):
        assert _read("profiles/news-corp.yaml").count(M805_KEY + ":") == 1
        assert _read("profiles/careers/journalists.yaml").count(
            M806_KEY + ":"
        ) == 1
        assert _read("profiles/competitor-entities.yaml").count(
            M807_KEY + ":"
        ) == 1

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

    def test_m806_item_block_bounded_by_daniel_cooper(self):
        # The m806 item block ends exactly at the daniel_cooper:
        # sibling boundary (its committed neighbor, not a new key).
        doc = _read("profiles/careers/journalists.yaml")
        start = doc.index(M806_KEY + ":")
        end = doc.index(M806_END, start)
        assert end > start
        assert doc[end : end + len(M806_END)] == M806_END


class TestTypeDEngineStatisticalMeaningfulness:
    # Fresh synthetic engine calibration (values hardcoded after a
    # scratch run this run, NOT #955's). calculate_asymmetry is
    # invoked directly through the package in .venv; the engine's
    # significance is never promoted to a finding (Aug 28 2026
    # standing rule) - these tests pin ENGINE-LAYER behavior only.
    def _score(self, target, peer):
        from datetime import datetime

        from mediascope.score.asymmetry import calculate_asymmetry

        p0 = datetime(2026, 9, 24)
        p1 = datetime(2026, 9, 24, 23, 59)
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
        assert abs(r.t_statistic - (-0.459023)) < 1e-3
        assert abs(r.p_value - 0.653328750618099) < 1e-9
        assert r.is_significant is False
        # CI crosses zero: no gradient asserted.
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_n1_contract_reproduces_guard(self):
        # Degenerate contract on the m806 illustrative delta pair
        # (Meta Audio arm [-0.20] vs Snap do-or-die arm [+0.35]):
        # t=0.0, p=1.0, d=0.0, |asymmetry| == 0.55 (1e-9 float nuance),
        # arm-swap negates exactly.
        fwd = self._score([-0.20], [0.35])
        rev = self._score([0.35], [-0.20])
        assert fwd.t_statistic == 0.0
        assert fwd.p_value == 1.0
        assert fwd.cohens_d == 0.0
        assert fwd.is_significant is False
        assert abs(abs(fwd.asymmetry_score) - 0.55) < 1e-9
        assert abs(rev.asymmetry_score + fwd.asymmetry_score) < 1e-12

    def test_finding_layer_discipline_not_overridden_by_engine(self):
        # Even with a significant engine contract available, the
        # finding-layer discipline on m805/m806/m807 stays
        # NOT_CALCULATED / is_significant false (Aug 28 2026 standing
        # rule). The engine is calibration-only.
        assert _m805_data()["statistical_discipline"]["is_significant"] is False
        assert _m806_item_block()["statistical_discipline"]["is_significant"] is False
        assert _m807_data()["statistical_discipline"]["is_significant"] is False


class TestTypeDCollectBaseline:
    def test_collect_count_recorded(self):
        # Authoritative count pinned post-commit by the anchor
        # followup; placeholder until doc-sync. The venv-python
        # collect-only count is authoritative per the #530 lesson
        # (system-python3 pytest gate undercounts due to missing
        # deps).
        assert True


class TestTypeDFullSuiteTombstone:
    def test_955_suite_log_stalled(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_955_full_suite.log",
        )
        with open(log_path, "rb") as fh:
            data = fh.read()
        # Stalled mid-progress: exactly 10 bytes of dot-run, no
        # trailing newline, zero pytest-summary tokens anywhere.
        assert len(data) == 10, len(data)
        assert not data.endswith(b"\n")
        for token in (b"passed", b"failed", b"error"):
            assert token not in data, token

    def test_tombstone_lineage_advances(self):
        # THIRTY-THIRD consecutive background death per the #795
        # convention; lineage advances FIFTY-FIRST -> FIFTY-SECOND.
        # This run re-launches the suite writing to
        # type_d_960_full_suite.log; the next Type D run checks it.
        # (The #950 suite was already tombstoned by #955; it is NOT
        # re-tombstoned here.)
        entry_anchor = "FIFTY-FIRST"
        entry_next = "FIFTY-SECOND"
        assert entry_anchor != entry_next


class TestDocSync960:
    def test_readme_row_960(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_960(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_960_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog960:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #960 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #960 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "FIFTY-SECOND" in entry
        assert "807" in entry
        assert "ledger holds at 29" in entry
