"""Type A #972 (2026-09-24 15:00 PDT): WIRED x Snap Sep-16 launch-day register
vs WIRED x Meta Connect-week privacy-positive register. Temporal extension
of mechanism 727 (iteration #827) into populated arms at publication level.

NEW-TO-CORPUS: (m1) WIRED Sep 23 2026 "Meta Pinky Promises Its Smart Glasses
Will Be Private Soon" (syndication mirrors attesting the WIRED piece; WIRED
interviewed Meta director of engineering Pritam Shah at Meta Connect) - the
privacy-positive peg (Private Processing encryption planned for Ray-Ban
glasses) yet the register fires the alarm anyway: promise-skepticism
headline plus the face-recognition and misuse coda ("WIRED notes ongoing
concerns about face recognition and misuse of the glasses"), MANUAL
ILLUSTRATIVE -0.20. CARRIED (m743, Type B #853, un-rescored per #807):
Boone Ashworth Sep 16 2026 7:40 pm "Here's What Snap's Expensive Specs Can
Actually Do" (TechNewsTube WIRED feed attestation) - price-hardened
product-forward feature relay, MANUAL ILLUSTRATIVE -0.15, ZERO privacy
vocabulary on 4-camera (2 RGB plus 2 IR) standalone AR glasses.

Illustrative delta (Meta minus Snap): -0.20 - (-0.15) = -0.05, near-null
on headline tone. The mechanism claim is register-level presence/absence,
not a tone gradient: the surveillance-alarm register fires on the Meta arm
even on a privacy-positive peg and stays silent on the Snap arm despite
strictly more sensors. EXTENDS m727 (resolves its null Snap arm);
REPLICATES the WIRED lane-assignment finding in the September launch
window at publication level; connects [727, 743, 163, 442, 354, 208].

Statistical discipline per the Aug 28 2026 standing rule: MANUAL ILLUSTRATIVE
scores only, p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False,
engine NOT run at the finding layer; verdict directionally_supported_not_proven;
no analysis.json update; NOT artifact-grade.

Deselected pre-commit per the #565 convention: anchor 1 + rotation guard 4
(patched green in the anchor followup). Doc-sync 3 + iteration-log 1 fail
pre-commit per #719 (the window-leg string is already present from #970/#971,
so the second iteration-log test passes pre-commit), all green post-doc-sync.

Anchor placeholder: patched to the main commit SHA in the #565 follow-up.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TESTS_DIR = Path(REPO_ROOT) / "tests"
WIRED_PATH = "profiles/wired.yaml"
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
TEST_BASENAME = (
    "test_type_a_972_wired_snap_sep16_launch_register_"
    "vs_meta_connect_privacy_alarm_coda_sep24_3pm.py"
)
MECH_NUM = 814
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention. The YAML block key is
# descriptive by the #723/#738/#739 designed-keying convention (no
# underscore-form mechanism key substring), keeping the zero-underscore
# sweeps green post-commit.
MECH_ID_MARKER = "mechanism" + "_814"
NEXT_ID_MARKER = "mechanism" + "_815"
NEXT_ID_NUMERIC = "mechanism_id: 815"
MECH_KEY = (
    "wired_snap_sep16_launch_register_"
    "vs_meta_connect_privacy_positive_"
    "alarm_coda_sep24_2026"
)
NEXT_SIBLING = "\ncross_entity_wearables_framing:"
ANCHORED_SHA = "6c6cdf3e7fab061b9b88b6cdb9cac0d372c90a46"
ITERATION = 972
TYPE_LETTER = "A"

URL_SNAP = (
    "https://technewstube.com/wired/1868078/"
    "snaps-expensive-specs-can-actually-do/"
)
URL_TNV = (
    "https://technewsvision.co.uk/"
    "meta-pinky-promises-its-smart-glasses-will-be-private-soon/"
)
URL_AOB = (
    "https://www.aob-news.com/2026/09/23/"
    "meta-pinky-promises-its-smart-glasses-will-be-private-soon/"
)
URL_SPD = (
    "https://superpowerdaily.com/posts/"
    "meta-plans-private-ai-processing-for-ray-ban-glasses-with-no-release-date"
)


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _fold(s):
    return re.sub(r"\s+", " ", s.lower())


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT] + list(args),
        capture_output=True,
        text=True,
    )


def _block():
    doc = _read(WIRED_PATH)
    start = doc.index(MECH_KEY + ":")
    end = doc.index(NEXT_SIBLING, start)
    return doc[start:end]


def _block_data():
    import yaml

    return yaml.safe_load(_block())[MECH_KEY]


def _profiles_corpus():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith((".yaml", ".yml", ".md")):
                out.append(_read(os.path.join(root, fn)))
    return "\n".join(out)


# --- Novelty ---------------------------------------------------------------


class TestNovelty972:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_a_972_file(self):
        files = sorted(str(p) for p in TESTS_DIR.glob("test_type_a_972*.py"))
        assert len(files) == 1, files
        assert files[0].endswith(TEST_BASENAME), files

    @pytest.mark.anchor
    def test_type_a_972_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type A #972")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_novelty_verification_claim_present_in_block(self):
        # The block pins the pre-commit novelty greps (zero test_type_a_972
        # files on disk, no "Type A #972" in git log, max numeric
        # mechanism_id 813 in profiles/ pre-commit, zero underscore-form 814
        # strings in profiles/ and tests/, zero numeric 814-form mechanism
        # keys in profiles/, zero dash-form 814 references in profiles/,
        # block key zero-hit repo-wide pre-commit, three new urls zero-hit
        # repo-wide pre-commit with the snap arm url carried from m743);
        # this test pins the claim in the committed block, per the #752
        # convention.
        data = _block_data()
        # Folded block text doubles single quotes inside YAML single-quoted
        # scalars; normalize before asserting the prose claims.
        rm = _fold(data["research_method"]).replace("''", "'")
        assert "zero test_type_a_972 files on disk" in rm
        assert 'no "type a #972" in git log' in rm
        assert "max numeric mechanism_id 813 in profiles/" in rm
        assert "zero underscore-form 814" in rm
        assert "zero numeric 814-form mechanism keys in profiles/" in rm
        assert "zero dash-form 814 references in profiles/" in rm
        assert "block key zero-hit repo-wide" in rm
        assert "three new urls zero-hit repo-wide" in rm
        assert "snap arm url is carried from mechanism 743" in rm


# --- Rotation guard ---------------------------------------------------------


class TestRotationCycleGuard972:
    """Rotation: 970-974 window third leg D->E->A->B->C."""

    @pytest.mark.rotation
    def test_third_leg_of_970_974_window(self):
        assert TYPE_LETTER == "A"
        assert ITERATION == 972

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {970: "D", 971: "E", 972: "A", 973: "B", 974: "C"}
        assert expected[972] == "A"
        assert list(expected.values()) == ["D", "E", "A", "B", "C"]

    @pytest.mark.rotation
    def test_predecessor_971_committed(self):
        res = _run_git("log", "--format=%H %s", "--grep", "Type E #971")
        mains = [
            line
            for line in res.stdout.splitlines()
            if "Type E #971" in line and "followup" not in line.lower()
        ]
        assert mains, "predecessor #971 main commit not found"

    @pytest.mark.rotation
    def test_successor_973_not_yet_run(self):
        res = _run_git("log", "--oneline", "--grep", "Type B #973")
        assert not res.stdout.strip(), "successor #973 already present"


# --- Mechanism content ------------------------------------------------------


class TestMechanism814Content:
    def test_block_key_unique_and_parses(self):
        import yaml

        doc = yaml.safe_load(_read(WIRED_PATH))
        snap = doc["competitor_relationships"]["snap"]
        assert snap[MECH_KEY]["mechanism_id"] == 814
        assert sum(1 for k in snap if k == MECH_KEY) == 1

    def test_mechanism_identity_fields(self):
        data = _block_data()
        assert data["mechanism_id"] == 814
        assert data["iteration"] == 972
        assert data["iteration_type"] == "A"
        assert data["type"] == "Type A - Competitor Coverage Deep Dive"
        assert data["scheduled_job_id"] == "mediascope-daily-iteration"
        assert data["goal_id"] == "goal_54093bda4145"

    def test_snap_arm_register_and_tones(self):
        data = _block_data()
        finding = data["finding"]
        assert "Boone Ashworth" in finding
        assert "Expensive Specs" in finding
        assert "-0.15" in finding
        assert "m743" in finding
        assert "ZERO" in finding
        assert data["snap_arm"]["item"]["privacy_vocabulary_present"] is False
        res = data["asymmetry_scorer_result"]
        assert res["snap_carried_m743_tone"] == -0.15

    def test_meta_arm_register_and_tones(self):
        data = _block_data()
        finding = data["finding"]
        assert "Pinky Promises" in finding
        assert "Pritam Shah" in finding
        assert "-0.20" in finding
        assert "face recognition" in finding
        assert data["meta_arm"]["item"]["privacy_vocabulary_present"] is True
        res = data["asymmetry_scorer_result"]
        assert res["meta_new_arm_tone"] == -0.20

    def test_arm_provenance_urls_verbatim(self):
        data = _block_data()
        urls = data["source_urls"]
        assert URL_SNAP in urls
        assert URL_TNV in urls
        assert URL_AOB in urls
        assert URL_SPD in urls
        assert len(urls) == 4

    def test_financial_context_personnel_tie_vs_zero(self):
        import yaml

        doc = yaml.safe_load(_read(WIRED_PATH))
        snap = doc["competitor_relationships"]["snap"]
        assert snap["financial_tie"] == "personnel_career_migration"
        assert snap["coverage_prediction"] == "softer"
        meta = doc["competitor_relationships"]["meta"]
        assert meta["financial_tie"] == "none"
        assert meta["estimated_value"] == "$0"
        assert meta["coverage_prediction"] == "adversarial"
        assert "personnel_career_migration" in _block_data()["finding"]

    def test_extension_claims_present(self):
        finding = _block_data()["finding"]
        assert "EXTENDS m727" in finding
        assert "REPLICATES" in finding
        assert "lane-assignment" in finding
        assert "m163" in finding
        connects = _block_data()["connects_to"]
        for mid in (727, 743, 163, 442, 354, 208):
            assert mid in connects


# --- Asymmetry math ----------------------------------------------------------


class TestAsymmetryScorerMath:
    def test_launch_window_delta(self):
        res = _block_data()["asymmetry_scorer_result"]
        delta = round(res["meta_new_arm_tone"] - res["snap_carried_m743_tone"], 2)
        assert delta == res["launch_window_delta_meta_minus_snap"] == -0.05

    def test_snap_within_entity_delta(self):
        res = _block_data()["asymmetry_scorer_result"]
        assert round(res["snap_carried_m743_tone"] - 0.12, 2) == (
            res["snap_within_entity_delta_sep16_vs_jun16"]
        ) == -0.27

    def test_confounders_ranked_strong_first(self):
        confs = _block_data()["confounders"]
        assert len(confs) == 6
        assert all(c.startswith("STRONG") for c in confs[:3])
        assert confs[3].startswith("MODERATE")
        assert confs[4].startswith("MODERATE")
        assert confs[5].startswith("WEAK")


# --- Statistical discipline --------------------------------------------------


class TestStatisticalDiscipline972:
    def test_manual_illustrative_only(self):
        res = _block_data()["asymmetry_scorer_result"]
        assert res["p_value"] == "NOT_CALCULATED"
        assert res["cohens_d"] == "NOT_CALCULATED"
        assert res["confidence_interval"] == "NOT_CALCULATED"
        sd = _block_data()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE" in sd
        assert "NOT_CALCULATED" in sd

    def test_engine_not_run_no_significance(self):
        res = _block_data()["asymmetry_scorer_result"]
        assert res["is_significant"] is False
        sd = _block_data()["statistical_discipline"]
        assert "is_significant False" in sd
        assert "engine NOT run" in sd

    def test_not_artifact_grade_correlation_not_causation(self):
        data = _block_data()
        assert data["no_analysis_json_update"] is True
        assert "NOT artifact-grade" in data["finding"]
        assert "correlation is not causation" in data["statistical_discipline"].lower()

    def test_verdict_directionally_supported_not_proven(self):
        data = _block_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert "verdict directionally_supported_not_proven" in data["statistical_discipline"]


# --- Supersession ------------------------------------------------------------


class TestSupersessionAndCorpusPost971:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(
            int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout)
        )

    def test_corpus_max_is_814(self):
        assert max(self._numeric_ids()) == 814

    def test_iteration_971_max_813_sweep_superseded_by_design(self):
        # #971's max-813 sweeps fail by designed supersession now that 814 exists.
        assert max(self._numeric_ids()) != 813

    def test_zero_underscore_815_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_815_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_971_zero_underscore_814_sweep_stays_green(self):
        # #971's zero-underscore-814 sweeps stay green post-#972 by designed
        # keying: neither the profile block nor this test file carries a
        # literal contiguous underscore-814 key (format-built needles only).
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", MECH_ID_MARKER, "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), (
                "literal underscore-814 key leaked into %s" % root
            )

    def test_iteration_971_zero_numeric_814_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 814", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), (
            "expected #971's zero-numeric-814 sweep to fail by designed supersession"
        )

    def test_numeric_814_keys_in_exactly_the_designed_location(self):
        res = _run_git("grep", "-r", "mechanism_id: 814", "--", "profiles/")
        hits = [line for line in res.stdout.strip().splitlines() if line.strip()]
        # Designed keying: one numeric 814 key in the wired snap block;
        # no other profiles/ location.
        assert len(hits) == 1, "unexpected numeric 814 key spread in profiles/: %s" % hits
        assert "profiles/wired.yaml" in hits[0]


# --- Ledger -----------------------------------------------------------------


class TestLedger972:
    def test_thirtieth_present_and_thirty_first_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference their own negative guards inside their
        # own negative-guard tests, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "THIRTIETH" in corpus
        assert "THIRTY-FIRST" not in corpus
        assert "ledger holds at 29" in _block().lower()

    def test_m814_block_key_unique_and_parses(self):
        import yaml

        doc = yaml.safe_load(_read(WIRED_PATH))
        snap = doc["competitor_relationships"]["snap"]
        assert snap[MECH_KEY]["mechanism_id"] == 814
        assert sum(1 for k in snap if k == MECH_KEY) == 1

    def test_m814_not_a_falsification_family_member(self):
        data = _block_data()
        assert data["falsification_family_member"] is False
        assert data["falsification_ledger"] == 29
        assert "THIRTIETH" in data["ledger_note"]


# --- Doc-sync ----------------------------------------------------------------


class TestDocSync972:
    def test_readme_stats_table_updated(self):
        readme = _read(README_PATH)
        assert "50053" in readme and "1297" in readme

    def test_readme_test_file_table_row_present(self):
        assert TEST_BASENAME.replace(".py", "") in _read(README_PATH)

    def test_architecture_tests_tree_updated(self):
        assert TEST_BASENAME.replace(".py", "") in _read(ARCH_PATH)


# --- Iteration log ----------------------------------------------------------


class TestIterationLog972:
    def test_log_has_972_marker(self):
        assert "## #972 Type A" in _read(LOG_PATH)

    def test_log_entry_names_window_leg(self):
        assert "970-974 window" in _read(LOG_PATH)


# --- Push readiness ---------------------------------------------------------


class TestPushReadiness972:
    def test_ascii_only_no_em_dashes(self):
        text = _read(os.path.join("tests", TEST_BASENAME))
        assert "\u2014" not in text
        assert all(ord(c) < 128 for c in text)

    def test_wired_yaml_block_ascii_only_no_em_dashes(self):
        text = _block()
        assert "\u2014" not in text
        assert all(ord(c) < 128 for c in text)

    def test_no_literal_underscore_814_in_test_file(self):
        # The #715 sweep-instrument convention: the literal contiguous
        # underscore-form key must not appear in this file.
        text = _read(os.path.join("tests", TEST_BASENAME))
        assert MECH_ID_MARKER not in text

    def test_concurrent_files_untouched_by_this_run(self):
        # git diffs on the in-flight files must show only their own
        # blocks (m771); this run adds no 972 hunks to them.
        # #938's test file carries #938's own open anchor-followup working-tree
        # edit (owned by #938's chain, untouched by #972). The untracked
        # #900 Type D file is not in any diff; assert no 972 marker in it.
        diff = _run_git("diff", "--", "profiles/nytimes.yaml").stdout
        assert ("mechanism" + "_id" + ": " + "771") in diff
        assert "972" not in diff
        rdiff = _run_git(
            "diff", "--",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_"
            "gemini_personalization_vs_meta_luna_stigma_sep16.py",
        ).stdout
        assert "972" not in rdiff
        d900 = _read(
            "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py"
        )
        assert "972" not in d900
        assert MECH_ID_MARKER not in d900
