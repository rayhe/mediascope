"""Type B #853 (850-854 window, fourth leg D->E->A->B): Boone Ashworth
Sep-16 Snap Specs launch register - temporal replication of mechanism 442
plus a bounded search-gap correction to mechanism 727.

FIRST corpus evidence of Ashworth's Sep 16 2026 7:40 pm WIRED launch-day
piece "Here's What Snap's Expensive Specs Can Actually Do" (excerpt-tier:
title/dek attested via the WIRED-sourced TechNewsTube feed item and two
NewsLocker WIRED-index reprints; WIRED paywalled, full text NOT first-hand
reviewed). The register hardens vs his Jun 16 2026 piece "You Can Finally
Buy Snap's New AR Specs for $2,195" (mechanism 442, +0.12 aspirational
availability): Expensive headline adjective, "chunky, pricey" dek, "Snap
thinks" attribution distancing, product-forward feature relay. New
illustrative Snap tone -0.15; within-journalist Jun-to-Sep delta -0.27.
The m442 pricing-inversion gap vs his Meta subscription arm (-0.48)
narrows 0.60 -> 0.33 but persists; the privacy-register asymmetry is
untouched (zero surveillance vocabulary on 4-camera glasses). Cross-
journalist replication of the Sep-16 hardening documented for Ropek
(TechCrunch, m269 refinement): two journalists, two outlets, same launch
window, same direction.

SCOPE CORRECTION: mechanism 727 (Type A #827) claimed no standalone WIRED
piece on the Sep 16 launch surfaced in bounded searches. This run attests
one, so the 727 finding was a search-coverage artifact; a
search_gap_correction_2026_09_19 caveat was appended to the 727 block this
run. Bounded absence of evidence is not evidence of non-publication.

Meta arms carried un-rescored from mechanisms 442/89/640-641 per the #807
pattern. MANUAL ILLUSTRATIVE only, engine NOT run, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False, verdict
directionally_supported_not_proven; NOT falsification-family, ledger holds
at 26; no analysis.json update. Novelty verified pre-commit (zero
test_type_b_853 files; no 'Type B #853' in git log; max 742; zero
underscore-form 743 keys per #715; block key zero-hit; headline string
zero-hit repo-wide; 3 browser.search query sets, 0 browser.open per #503);
count_stats gate (delta = this file exactly); 850-854 window fourth leg
D->E->A->B (anchor patched post-commit per #565) - Sep 19 2026 08:00 PDT.
"""

import os
import re
import subprocess
import datetime

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = "test_type_b_853_boone_ashworth_sep2026_snap_specs_launch_register_temporal_replication.py"
MECH_KEY = "type_b_853_boone_ashworth_sep2026_snap_specs_launch_register_temporal_replication"
M_ID = 743
ITER = 853
TYPE_LETTER = "B"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_743"
NEXT_ID_MARKER = "mechanism" + "_744"
NEXT_ID_NUMERIC = "mechanism_id: " + "744"
EXPECTED_ORDER = [("B", "853"), ("A", "852"), ("E", "851"), ("D", "850"), ("C", "849")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP_PER_565"

SNAP_MIRROR_URL = "https://technewstube.com/wired/1868078/snaps-expensive-specs-can-actually-do/"
SNAP_TITLE = "Here's What Snap's Expensive Specs Can Actually Do"
SNAP_DEK = "Snap thinks its chunky, pricey smart glasses are the future of human computing, powered by a new AI app and features that do everything from translating languages to improving your golf swing."
JUN16_URL = "https://www.wired.com/story/you-can-finally-buy-snaps-new-ar-specs-for-2195/"
META_SUB_URL = "https://www.wired.com/story/why-meta-is-charging-a-subscription-for-on-device-smart-glasses-features/"
EXPECTED_URLS = [SNAP_MIRROR_URL, JUN16_URL, META_SUB_URL]

README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _profiles_text():
    return _read(os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml"))


def _wired_text():
    return _read(os.path.join(REPO_ROOT, "profiles", "wired.yaml"))


def _block():
    text = _profiles_text()
    start = text.index(MECH_KEY)
    end = text.index("\n- auto_detected_migrations: 5", start)
    return text[start:end]


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
        if "Type B #853" in subject:
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


class TestNovelty853:
    def test_single_test_type_b_853_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_b_853") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_b_853_main_commit_unique_and_anchored(self):
        # No #853 main commit exists pre-commit; the anchor test pins
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
            if "Type B #853" in line and "followup" not in line.lower()
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
        # This run ADDS mechanism 743: post-commit max is 743, zero 744
        # keys anywhere. Pre-commit sweeps verified max 742, zero
        # underscore-form 743 keys (designed keying per #715), block key
        # zero-hit, Snap Specs headline string zero-hit repo-wide.
        assert max(_corpus_ids()) == 743
        assert _repo_grep(NEXT_ID_MARKER) == []
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == []

    def test_850_852_window_legs_present_prior_to_853(self):
        log = _read(LOG_PATH)
        for marker in (
            "## #850 Type D:",
            "## #851 Type E:",
            "## #852 Type A:",
        ):
            assert marker in log, marker


class TestRotationGuard853:
    """#853 is the Type B fourth leg of window 850-854: D->E->A->B."""

    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_850_854_fourth_leg(self):
        # Deselected pre-commit per #565 (the #853 main commit does not
        # exist yet); patched green in the anchor followup.
        window = _window()
        assert window[:4] == EXPECTED_ORDER[:4], (
            f"850-854 window fourth leg D->E->A->B: expected {EXPECTED_ORDER[:4]}, "
            f"got {window[:4]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        for (t1, n1), (t2, n2) in zip(window[:4], window[1:5]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_a_852(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        assert window[1] == ("A", "852"), (
            f"immediate predecessor must be Type A #852, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        # Patched to the real main-commit SHA in the anchor followup per
        # the #565 convention; deselected pre-commit at the pytest CLI.
        mains = _git_log_mains("Type B #853: Boone Ashworth")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "PATCH_ME_IN_FOLLOWUP_PER_565",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism743Structure:
    def test_block_key_exists_in_journalists_profile(self):
        assert MECH_KEY in _profiles_text()

    def test_block_key_unique(self):
        keys = re.findall(r"^  " + MECH_KEY + r":$", _profiles_text(), re.M)
        assert len(keys) == 1, keys

    def test_iteration_and_type_and_time_pdt(self):
        block = _block()
        assert "iteration: 853" in block
        assert "iteration_type: 'B'" in block
        assert "2026-09-19 08:00 PDT" in block
        assert "mechanism_id: 743" in block

    def test_designed_keying_no_underscore_743_in_block(self):
        # Per #715: block keys and prose must not carry the underscore-form
        # mechanism id; the colon form mechanism_id: 743 is the only allowed
        # 743 reference.
        block = _block()
        assert MECH_ID_MARKER not in block
        assert "mechanism_id: 743" in block

    def test_yaml_parses_and_fields(self):
        d = yaml.safe_load(_profiles_text())
        item = next(
            j for j in d["journalists"] if j.get("name") == "Boone Ashworth"
        )
        mech = item[MECH_KEY]
        assert mech["mechanism_id"] == 743
        assert mech["iteration"] == 853
        assert mech["iteration_type"] == "B"
        assert mech["verdict"] == "directionally_supported_not_proven"
        assert mech["no_analysis_json_update"] is True
        assert mech["connects_to"] == [442, 727]
        assert mech["is_significant"] is False

    def test_boone_ashworth_profile_context(self):
        d = yaml.safe_load(_profiles_text())
        item = next(
            j for j in d["journalists"] if j.get("name") == "Boone Ashworth"
        )
        assert MECH_KEY in item
        assert SNAP_MIRROR_URL in _block()


class TestMechanism743NewSnapArm:
    def _snap(self):
        d = yaml.safe_load(_profiles_text())
        item = next(
            j for j in d["journalists"] if j.get("name") == "Boone Ashworth"
        )
        return item[MECH_KEY]["new_snap_arm"]

    def test_snap_arm_title_verbatim(self):
        assert self._snap()["title_verbatim"] == SNAP_TITLE

    def test_snap_arm_dek_verbatim(self):
        assert self._snap()["dek_verbatim"] == SNAP_DEK

    def test_snap_arm_date_sep_16_2026(self):
        snap = self._snap()
        assert snap["date"] == "2026-09-16"
        assert snap["time"] == "7:40 pm"

    def test_snap_arm_byline_attribution_and_role(self):
        snap = self._snap()
        assert "Boone Ashworth" in snap["byline"]
        assert "(sole)" in snap["byline"]
        assert "WIRED" in snap["role"]
        assert snap["url"] == SNAP_MIRROR_URL

    def test_excerpt_tier_evidence_limitation(self):
        snap = self._snap()
        tier = snap["evidence_tier"]
        assert "EXCERPT-TIER" in tier
        assert "paywalled" in tier
        assert "NOT first-hand reviewed" in tier
        assert "Title/dek-level register only" in tier

    def test_snap_arm_tone_minus_015_illustrative(self):
        snap = self._snap()
        assert snap["tone_illustrative"] == -0.15
        assert "MANUAL ILLUSTRATIVE" in snap["tone_basis"]
        assert "Expensive" in " ".join(snap["register_markers"])


class TestMechanism743CarriedArms:
    def _mech(self):
        d = yaml.safe_load(_profiles_text())
        item = next(
            j for j in d["journalists"] if j.get("name") == "Boone Ashworth"
        )
        return item[MECH_KEY]

    def test_carried_snap_jun16_unrescored(self):
        arm = self._mech()["carried_snap_jun16_arm"]
        assert "un-rescored" in arm["note"]
        assert "442" in arm["note"]
        assert arm["tone_illustrative"] == 0.12
        assert arm["url"] == JUN16_URL
        assert "aspirational" in arm["framing"]

    def test_meta_arms_carried_unrescored_per_807(self):
        note = self._mech()["carried_meta_arms"]["note"]
        assert "un-rescored" in note
        assert "#807" in note

    def test_meta_subscription_arm_tone_minus_048(self):
        arms = self._mech()["carried_meta_arms"]["arms"]
        sub = [a for a in arms if "Subscription" in a["title"]]
        assert len(sub) == 1
        assert sub[0]["tone_illustrative"] == -0.48
        assert sub[0]["url"] == META_SUB_URL
        assert "co-byline" in sub[0]["byline"]

    def test_meta_led_fix_arm_tone_minus_015(self):
        arms = self._mech()["carried_meta_arms"]["arms"]
        led = [a for a in arms if "LED Fix" in a["title"]]
        assert len(led) == 1
        assert led[0]["tone_illustrative"] == -0.15
        assert "Boone Ashworth (sole)" in led[0]["byline"]

    def test_category_headline_arm_date_aug_02(self):
        arms = self._mech()["carried_meta_arms"]["arms"]
        creepy = [a for a in arms if "Creepy" in a["title"]]
        assert len(creepy) == 1
        assert creepy[0]["date"] == "2026-08-02"
        assert "mechanism 89" in creepy[0]["framing"]

    def test_no_duplicate_mechanism_id_743(self):
        # Carried arms must not introduce any new numeric mechanism id;
        # the only colon-form 743 reference in the block is the mechanism's.
        block = _block()
        assert re.search(r"mechanism_id:\s*(\d+)", block).group(1) == "743"
        assert block.count("mechanism_id: 743") == 1


class TestMechanism743Temporal:
    def _mech(self):
        d = yaml.safe_load(_profiles_text())
        item = next(
            j for j in d["journalists"] if j.get("name") == "Boone Ashworth"
        )
        return item[MECH_KEY]

    def test_within_journalist_hardening_delta_math(self):
        s = self._mech()["asymmetry_scorer_result"]
        assert s["within_journalist_temporal_delta_snap_jun_to_sep"] == -0.27
        assert round(-0.15 - 0.12, 2) == -0.27
        assert s["temporal_delta_calc"] == "-0.15 - 0.12 = -0.27"

    def test_pricing_inversion_gap_narrows_but_persists(self):
        s = self._mech()["asymmetry_scorer_result"]
        assert s["illustrative_delta_snap_minus_meta"] == 0.33
        assert round(s["target_avg"] - s["reference_avg"], 2) == 0.33
        refinement = " ".join(self._mech()["temporal_refinement"])
        assert "0.33" in refinement
        assert "0.60" in refinement

    def test_cross_journalist_replication_ropek(self):
        refinement = " ".join(self._mech()["temporal_refinement"])
        assert "Ropek" in refinement
        assert "m269" in refinement

    def test_connects_to_442_and_727(self):
        mech = self._mech()
        assert mech["connects_to"] == [442, 727]
        assert "TEMPORAL REFINEMENT" in mech["extends"]
        assert "mechanism 442" in mech["extends"]

    def test_m727_scope_correction_present(self):
        correction = " ".join(self._mech()["m727_scope_correction"])
        assert "search-coverage artifact" in correction
        assert "not a publication absence" in correction
        assert "search_gap_correction_2026_09_19" in correction
        # The caveat is also physically appended to the 727 block in wired.yaml.
        wired = _wired_text()
        assert "search_gap_correction_2026_09_19" in wired
        assert "Type B #853" in wired


class TestMechanism743Discipline:
    def _mech(self):
        d = yaml.safe_load(_profiles_text())
        item = next(
            j for j in d["journalists"] if j.get("name") == "Boone Ashworth"
        )
        return item[MECH_KEY]

    def test_p_value_not_calculated(self):
        assert self._mech()["asymmetry_scorer_result"]["p_value"] == "NOT_CALCULATED"

    def test_cohens_d_not_calculated(self):
        assert self._mech()["asymmetry_scorer_result"]["cohens_d"] == "NOT_CALCULATED"

    def test_ci_95_not_calculated(self):
        assert self._mech()["asymmetry_scorer_result"]["ci_95"] == "NOT_CALCULATED"

    def test_is_significant_false_and_engine_not_run(self):
        mech = self._mech()
        assert mech["is_significant"] is False
        assert "engine NOT run" in mech["asymmetry_scorer_result"]["engine"]

    def test_verdict_and_correlation_note(self):
        mech = self._mech()
        assert mech["verdict"] == "directionally_supported_not_proven"
        assert "Correlation is not causation" in mech["correlation_note"]

    def test_no_analysis_json_update_and_not_artifact_grade(self):
        mech = self._mech()
        assert mech["no_analysis_json_update"] is True
        assert mech["asymmetry_scorer_result"]["artifact_grade"] == "NOT artifact-grade"

    def test_falsification_ledger_holds_at_26_and_research_method(self):
        mech = self._mech()
        assert "ledger holds at 26" in mech["falsification_family"]
        assert "TWENTY-SIXTH" in mech["falsification_family"]
        assert "3 browser.search query sets" in mech["research_method"]
        assert "0 browser.open" in mech["research_method"]
        assert len(mech["confounders"]) == 7
        assert len(mech["counterevidence"]) == 4

    def test_confounder_severity_distribution(self):
        confs = " ".join(self._mech()["confounders"])
        assert confs.count("[STRONG]") == 3
        assert confs.count("[MODERATE]") == 2
        assert confs.count("[WEAK]") == 2


class TestDocSync853:
    def test_readme_row_853(self):
        assert OWN_BASENAME in _read(README_PATH)

    def test_architecture_row_853(self):
        assert OWN_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_853_file(self):
        doc = _read(ARCH_PATH)
        assert OWN_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog853:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #853 Type B:")
        return log[idx : idx + 14000]

    def test_log_entry_present(self):
        assert "## #853 Type B:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism 743" in entry
        assert "Boone Ashworth" in entry
        assert "Snap Specs" in entry

    def test_log_rotation_window_850_854(self):
        entry = self._entry()
        assert "850-854" in entry

    def test_log_records_m727_correction(self):
        entry = self._entry()
        assert "search_gap_correction_2026_09_19" in entry


class TestDateGrounding853:
    def test_sep_19_2026_is_saturday(self):
        assert datetime.datetime(2026, 9, 19).strftime("%A") == "Saturday"

    def test_sep_16_2026_is_wednesday(self):
        assert datetime.datetime(2026, 9, 16).strftime("%A") == "Wednesday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 19, 8, 0).strftime("%H:%M") == "08:00"
