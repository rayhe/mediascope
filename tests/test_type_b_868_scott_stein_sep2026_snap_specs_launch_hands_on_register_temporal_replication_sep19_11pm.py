"""Type B #868 (865-869 window, fourth leg D->E->A->B): Scott Stein
Sep-17 Snap Specs launch hands-on register - temporal replication of
mechanism 588's register-constancy claim at a THIRD entity.

FIRST corpus evidence of Scott Stein's (CNET) Sep 17 2026 Snap Specs
launch hands-on "I Wore Snap Specs At Last: Here's What These Massive
Glasses Can Do" (excerpt-tier: mirror-attested title, Stein's own CNET
YouTube companion video title/chapters, ccstartup Mashable mirror's
Spiegel-interview attestation; full CNET text NOT first-hand reviewed).
The register runs "massive" (headline) / "chunky" (own video title) as
physical-descriptive adjectives inside the same enthusiastic hands-on
reviewer register documented for Meta (+0.65, Sep 2025) and
Samsung/Google (+0.70, Oct 2025) in mechanism 588: product-forward
feature relay moderated by honest-reviewer caveats (session-based use,
not all-day glasses), plus symmetric exec access (Spiegel 1-on-1 mirrors
the Zuckerberg demo / Himmel interview / White quotes stack). New
illustrative Snap tone +0.45; illustrative delta (Snap minus Meta) -0.20,
within hand-scoring noise. Three-entity band [0.65, 0.70, 0.45] holds
across a 12-month temporal span (Sep 2025 -> Sep 2026). EXTENDS mechanism
588 (2-entity constancy -> 3-entity constancy); EXTENDS mechanism 106's
domain bound (the enthusiasm gradient with privacy deferral is
news-register only; Stein's review register is entity-neutral across
Meta, Samsung/Google, AND Snap). Privacy-register symmetry: zero
surveillance vocabulary in BOTH the Meta arm (m588 documented) and the
Snap arm (4 cameras + contextual AI).

Meta/Samsung arms carried un-rescored per the #807 pattern. MANUAL
ILLUSTRATIVE only, engine NOT run, p_value/cohens_d/ci_95 NOT_CALCULATED,
is_significant False, verdict directionally_supported_not_proven; NOT
falsification-family, ledger holds at 27; no analysis.json update.
Novelty verified pre-commit (zero test_type_b_868 files; no 'Type B #868'
in git log; max 751; zero underscore-form 752 keys per #715; block key
zero-hit; "Snap Specs At Last" headline string zero-hit repo-wide; all 3
evidence URLs zero-hit; 4 browser.search query sets, 0 browser.open per
#503); count_stats gate (delta = this file exactly); 865-869 window
fourth leg D->E->A->B (anchor patched post-commit per #565) - Sep 19 2026
23:00 PDT.
"""

import os
import re
import subprocess
import datetime

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = "test_type_b_868_scott_stein_sep2026_snap_specs_launch_hands_on_register_temporal_replication_sep19_11pm.py"
MECH_KEY = "type_b_868_scott_stein_sep2026_snap_specs_launch_hands_on_register_temporal_replication"
M_ID = 752
ITER = 868
TYPE_LETTER = "B"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_752"
NEXT_ID_MARKER = "mechanism" + "_753"
NEXT_ID_NUMERIC = "mechanism_id: " + "753"
EXPECTED_ORDER = [("B", "868"), ("A", "867"), ("E", "866"), ("D", "865"), ("C", "864")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP_PER_565"

SNAP_MIRROR_URL = "https://wesearch.press/s/i-wore-snap-specs-at-last-heres-what-these-massive-glasses-can-do-b02ecb8f"
SNAP_VIDEO_URL = "https://www.youtube.com/watch?v=lESTqJ1fACQ"
SNAP_TITLE = "I Wore Snap Specs At Last: Here's What These Massive Glasses Can Do"
SNAP_VIDEO_TITLE = "I Finally Tried Snap's Chunky AR Glasses In The Real World"
SPIEGEL_SOURCE_URL = "https://ccstartup.com/blog/2026/09/19/snap-launches-its-2195-specs-ar-glasses-at-an-awkward-time/"
META_ARM_URL = "https://newsatw.com/i-wore-metas-new-ray-ban-display-glasses-and-neural-band-i-feel-augmented/"
EXPECTED_URLS = [SNAP_MIRROR_URL, SNAP_VIDEO_URL, SPIEGEL_SOURCE_URL, META_ARM_URL]

README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _profiles_text():
    return _read(os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml"))


def _stein_item():
    d = yaml.safe_load(_profiles_text())
    return next(j for j in d["journalists"] if j.get("name") == "Scott Stein")


def _block():
    text = _profiles_text()
    start = text.index(MECH_KEY)
    end = text.index("\n- name: Wesley Hilliard", start)
    return text[start:end]


def _mech():
    return _stein_item()["competitor_coverage"][MECH_KEY]


def _corpus_ids():
    ids = []
    for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith(".yaml"):
                text = _read(os.path.join(root, fn))
                for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                    ids.append(int(m.group(1)))
    return ids


def _repo_grep(needle, roots=("profiles", "tests")):
    hits = []
    for r in roots:
        base = os.path.join(REPO_ROOT, r)
        for root, _, files in os.walk(base):
            for fn in files:
                if fn.rsplit(".", 1)[-1] in ("py", "yaml", "md", "json"):
                    p = os.path.join(root, fn)
                    if "__pycache__" in p:
                        continue
                    try:
                        if needle in _read(p):
                            hits.append(os.path.relpath(p, REPO_ROOT))
                    except OSError:
                        pass
    return hits


def _git(*args):
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def _git_log_mains(qualifier):
    out = _git("log", "--all", "--format=%H %s", "--grep", qualifier)
    mains = {}
    for line in out.splitlines():
        if not line.strip():
            continue
        sha, _, subject = line.partition(" ")
        if "Type B #868" in subject:
            mains[sha] = subject
    return mains


def _window(n=40):
    # First occurrence of each distinct iteration number, newest first
    # (robust to followup commits that repeat the same "Type X #N" wording
    # without the colon, per the #752 convention).
    subjects = _git("log", f"-{n}", "--format=%s", "--no-merges").splitlines()
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out[:5]


class TestNovelty868:
    def test_single_test_type_b_868_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_b_868") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_b_868_main_commit_unique_and_anchored(self):
        # No #868 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--", "tests/" + OWN_BASENAME],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type B #868" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "PATCH_ME_IN_FOLLOWUP_PER_565",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # This run ADDS mechanism 752: post-commit max is 752, zero 753
        # keys anywhere. Pre-commit sweeps verified max 751, zero
        # underscore-form 752 keys (designed keying per #715), block key
        # zero-hit, Snap headline string zero-hit repo-wide.
        assert max(_corpus_ids()) == 752
        assert _repo_grep(NEXT_ID_MARKER) == []
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == []

    def test_865_867_window_legs_present_prior_to_868(self):
        log = _read(LOG_PATH)
        for marker in (
            "## #865 Type D:",
            "## #866 Type E:",
            "## #867 Type A:",
        ):
            assert marker in log, marker


class TestRotationGuard868:
    """#868 is the Type B fourth leg of window 865-869: D->E->A->B."""

    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_865_869_fourth_leg(self):
        # Deselected pre-commit per #565 (the #868 main commit does not
        # exist yet); patched green in the anchor followup.
        window = _window()
        assert window[:4] == EXPECTED_ORDER[:4], (
            f"865-869 window fourth leg D->E->A->B: expected {EXPECTED_ORDER[:4]}, "
            f"got {window[:4]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        for (t1, n1), (t2, n2) in zip(window[:4], window[1:5]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_a_867(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        assert window[1] == ("A", "867"), (
            f"immediate predecessor must be Type A #867, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        # Patched to the real main-commit SHA in the anchor followup per
        # the #565 convention; deselected pre-commit at the pytest CLI.
        mains = _git_log_mains("Type B #868: Scott Stein")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "PATCH_ME_IN_FOLLOWUP_PER_565",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism752Structure:
    def test_block_key_exists_in_stein_item(self):
        assert MECH_KEY in _stein_item()["competitor_coverage"]

    def test_block_key_unique(self):
        keys = re.findall(r"^    " + MECH_KEY + r":$", _profiles_text(), re.M)
        assert len(keys) == 1, keys

    def test_iteration_and_type_and_time_pdt(self):
        block = _block()
        assert "iteration: 868" in block
        assert "iteration_type: 'B'" in block
        assert "2026-09-19 23:00 PDT" in block
        assert "mechanism_id: 752" in block

    def test_designed_keying_no_underscore_752_in_block(self):
        # Per #715: block keys and prose must not carry the underscore-form
        # mechanism id; the colon form mechanism_id: 752 is the only allowed
        # 752 reference.
        block = _block()
        assert MECH_ID_MARKER not in block
        assert "mechanism_id: 752" in block

    def test_yaml_parses_and_fields(self):
        mech = _mech()
        assert mech["mechanism_id"] == 752
        assert mech["iteration"] == 868
        assert mech["iteration_type"] == "B"
        assert mech["verdict"] == "directionally_supported_not_proven"
        assert mech["no_analysis_json_update"] is True
        assert mech["connects_to"] == [106, 588]
        assert mech["is_significant"] is False

    def test_stein_profile_context(self):
        item = _stein_item()
        assert MECH_KEY in item["competitor_coverage"]
        assert "type_b_588_scott_stein_handson_review_register_constancy" in item[
            "competitor_coverage"
        ]
        assert SNAP_MIRROR_URL in _block()

    def test_block_boundary_sentinel(self):
        # The block sits between the type_b_588 block and the Wesley
        # Hilliard item; the boundary line must be intact (regression guard
        # on the #868 boundary-drop incident, repaired pre-commit).
        text = _profiles_text()
        assert "\n- name: Wesley Hilliard" in text
        names = [
            j.get("name") for j in yaml.safe_load(text)["journalists"]
        ]
        assert names.count("Scott Stein") == 1
        assert names.count("Wesley Hilliard") == 1


class TestMechanism752NewSnapArm:
    def _snap(self):
        return _mech()["new_snap_arm"]

    def test_snap_arm_title_verbatim(self):
        assert self._snap()["title_verbatim"] == SNAP_TITLE

    def test_snap_arm_date_sep_17_2026(self):
        snap = self._snap()
        assert snap["date"] == "2026-09-17"
        assert snap["url"] == SNAP_MIRROR_URL
        assert snap["video_url"] == SNAP_VIDEO_URL
        assert snap["video_title"] == SNAP_VIDEO_TITLE

    def test_snap_arm_byline_attribution_and_role(self):
        snap = self._snap()
        assert "Scott Stein" in snap["byline"]
        assert "(sole)" in snap["byline"]
        assert "CNET" in snap["role"]
        assert snap["ceo_interview_source"] == SPIEGEL_SOURCE_URL

    def test_excerpt_tier_evidence_limitation(self):
        snap = self._snap()
        tier = snap["evidence_tier"]
        assert "EXCERPT-TIER" in tier
        assert "NOT first-hand reviewed" in tier
        assert "mirror-level register only" in tier
        assert "no URL construction" in tier

    def test_snap_arm_tone_plus_045_illustrative(self):
        snap = self._snap()
        assert snap["tone_illustrative"] == 0.45
        assert "MANUAL ILLUSTRATIVE" in snap["tone_basis"]
        assert "massive" in " ".join(snap["register_markers"])

    def test_spiegel_interview_symmetry(self):
        snap = self._snap()
        assert "Evan Spiegel" in snap["ceo_quote"]
        assert "session-based" in snap["ceo_quote"]
        assert "CNET's Scott Stein" in snap["ceo_interview_attestation"]


class TestMechanism752CarriedArms:
    def test_meta_arm_carried_unrescored_per_807(self):
        arm = _mech()["carried_meta_arm"]
        assert "un-rescored" in arm["note"]
        assert "#807" in arm["note"]
        assert arm["tone_illustrative"] == 0.65
        assert arm["date"] == "2025-09-18"
        assert META_ARM_URL in arm["source_urls"]

    def test_meta_arm_zero_privacy_documented(self):
        arm = _mech()["carried_meta_arm"]
        assert "zero privacy" in arm["privacy_treatment"]

    def test_samsung_arm_carried_unrescored(self):
        arm = _mech()["carried_samsung_google_arm"]
        assert "un-rescored" in arm["note"]
        assert arm["tone_illustrative"] == 0.7
        assert arm["date"] == "2025-10-22"

    def test_carried_arm_prices_verbatim(self):
        assert _mech()["carried_meta_arm"]["price"] == "$799"
        assert _mech()["carried_samsung_google_arm"]["price"] == "$1,799"

    def test_no_duplicate_mechanism_id_752(self):
        # Carried arms must not introduce any new numeric mechanism id;
        # the only colon-form 752 reference in the block is the mechanism's.
        block = _block()
        assert re.search(r"mechanism_id:\s*(\d+)", block).group(1) == "752"
        assert block.count("mechanism_id: 752") == 1

    def test_expected_urls_in_block(self):
        block = _block()
        for url in EXPECTED_URLS:
            assert url in block, url


class TestMechanism752Temporal:
    def test_snap_minus_meta_delta_math(self):
        s = _mech()["asymmetry_scorer_result"]
        assert s["illustrative_delta_snap_minus_meta"] == -0.2
        assert round(0.45 - 0.65, 2) == -0.2
        assert s["delta_calc"] == "0.45 - 0.65 = -0.20"

    def test_three_entity_band(self):
        s = _mech()["asymmetry_scorer_result"]
        assert s["three_entity_band"] == [0.65, 0.7, 0.45]
        assert s["target_entity"] == "Snap"
        assert s["reference_entity"] == "Meta"

    def test_extends_588_two_to_three_entities(self):
        refinement = " ".join(_mech()["temporal_refinement"])
        assert "mechanism 588" in refinement
        assert "THIRD entity" in refinement
        assert "12-month" in refinement

    def test_extends_106_domain_bound(self):
        refinement = " ".join(_mech()["temporal_refinement"])
        assert "mechanism 106" in refinement
        assert "launch-keynote register" in refinement

    def test_connects_to_106_and_588(self):
        mech = _mech()
        assert mech["connects_to"] == [106, 588]
        assert "TEMPORAL REFINEMENT" in mech["extends"]
        assert "mechanism 588" in mech["extends"]


class TestMechanism752Discipline:
    def test_p_value_not_calculated(self):
        assert _mech()["asymmetry_scorer_result"]["p_value"] == "NOT_CALCULATED"

    def test_cohens_d_not_calculated(self):
        assert _mech()["asymmetry_scorer_result"]["cohens_d"] == "NOT_CALCULATED"

    def test_ci_95_not_calculated(self):
        assert _mech()["asymmetry_scorer_result"]["ci_95"] == "NOT_CALCULATED"

    def test_is_significant_false_and_engine_not_run(self):
        mech = _mech()
        assert mech["is_significant"] is False
        assert "engine NOT run" in mech["asymmetry_scorer_result"]["engine"]

    def test_verdict_and_correlation_note(self):
        mech = _mech()
        assert mech["verdict"] == "directionally_supported_not_proven"
        assert "Correlation is not causation" in mech["correlation_note"]

    def test_no_analysis_json_update_and_not_artifact_grade(self):
        mech = _mech()
        assert mech["no_analysis_json_update"] is True
        assert mech["asymmetry_scorer_result"]["artifact_grade"] == "NOT artifact-grade"

    def test_falsification_ledger_holds_at_27_and_research_method(self):
        mech = _mech()
        assert "ledger holds at 27" in mech["falsification_family"]
        assert "NOT a falsification-family member" in mech["falsification_family"]
        assert "4 browser.search query sets" in mech["research_method"]
        assert "0 browser.open" in mech["research_method"]
        assert len(mech["confounders"]) == 8
        assert len(mech["counterevidence"]) == 3

    def test_confounder_severity_distribution(self):
        confs = " ".join(_mech()["confounders"])
        assert confs.count("[STRONG]") == 3
        assert confs.count("[MODERATE]") == 3
        assert confs.count("[WEAK]") == 2


class TestDocSync868:
    def test_readme_row_868(self):
        assert OWN_BASENAME in _read(README_PATH)

    def test_architecture_row_868(self):
        assert OWN_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_868_file(self):
        doc = _read(ARCH_PATH)
        assert OWN_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog868:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #868 Type B:")
        return log[idx : idx + 14000]

    def test_log_entry_present(self):
        assert "## #868 Type B:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism 752" in entry
        assert "Scott Stein" in entry
        assert "Snap Specs" in entry

    def test_log_rotation_window_865_869(self):
        entry = self._entry()
        assert "865-869" in entry


class TestDateGrounding868:
    def test_sep_19_2026_is_saturday(self):
        assert datetime.datetime(2026, 9, 19).strftime("%A") == "Saturday"

    def test_sep_17_2026_is_thursday(self):
        assert datetime.datetime(2026, 9, 17).strftime("%A") == "Thursday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 19, 23, 0).strftime("%H:%M") == "23:00"
