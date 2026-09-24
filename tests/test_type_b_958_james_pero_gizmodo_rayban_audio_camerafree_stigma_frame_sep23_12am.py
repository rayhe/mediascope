"""Type B #958 (2026-09-24 00:00 PDT): James Pero (Gizmodo) journalist
cross-entity tracking - TEMPORAL NATURAL EXPERIMENT on the privacy objection
itself. Meta arm: Gizmodo Sep-23 2026 "Meta Introduces Audio-Only Smart
Glasses to Avoid the 'Perv' Problem" (byline James Pero via the
gizmodo.com/author/jpero listing and the gizmodo.com/latest "Gadgets James
Pero Sep 23" listing; dek-tier first-hand via the embed page opened this run;
body excerpt-tier via the coschedule full-text mirror per #503). Meta's FIRST
camera-free glasses (Ray-Ban Audio, 43g, 12-hr battery, 23 color/lens combos,
$349): the camera at the center of Pero's m791 adversarial register on the
Sep-16 Luna camera glasses ("Drastically Tone Down the Creep Factor",
"unsavory stuff", "major liability") is REMOVED, yet the privacy-accusation
frame PERSISTS in the headline/dek ("'Perv' Problem", "glasshole") - the
objection moves from hardware to brand. Body is product-forward first-person
hands-on, so the adversarial load sits entirely in the frame.
Editorial-not-company-driven: gearlive notes "Meta didn't say this pair
exists because of privacy. Gizmodo's headline said it for them." Comparator
arms carried un-rescored per #807: Snap "Do or Die" +0.35 (m746) and the m791
Sep-16 pair (Luna adversarial vs Snap Specs hands-on "Dorky, Fun",
Meta-minus-Snap delta -0.65). MANUAL ILLUSTRATIVE: Meta Audio arm -0.20 vs
Snap do-or-die +0.35 = illustrative delta -0.55, same direction as m791's
-0.65. EXTENDS m791 temporally (Sep 16 -> Sep 23); the register follows the
brand, not the hardware. NOT a falsification-family member (register
documentation + temporal extension, not a uniform-prediction test); ledger
holds at 29. connects_to: [211, 746, 791, 734, 749, 269, 743]. No
analysis.json update. Correlation is not causation. Hypothesis-generating
only. NOT artifact-grade.

Rotation window FOURTH leg: D (#955) -> E (#956) -> A (#957) -> B (#958 this
run) -> C (#959), continuing the 955-959 window.

Evidence: 4 browser.search query sets this run ((1) Meta Connect 2026 smart
glasses journalist hands-on Sep 23 - surfaced the Gizmodo live blog (Pero on
the ground in Menlo Park), Sun/Keach hands-on, mobilesyrup VR Glasses
hands-on; (2) James Pero Gizmodo Snap Spectacles Specs - surfaced the "Do or
Die" piece and "Do Snap's Beefy AR Glasses Actually Bend Your Ears?" (in
corpus via m746, carried); (3) Raymond Wong Gizmodo Snap Specs - REJECTED:
Wong already carries m95 (Samsung same-chip) + the Aug-6 Type B cross-entity
clean-control paradox; corpus-saturated; (4) Gizmodo "Perv" Problem Pero -
SELECTED: canonical byline via gizmodo.com/author/jpero ("James Pero, Author
at Gizmodo" listing the piece) + gizmodo.com/latest ("Gadgets James Pero Sep
23"); full text via the coschedule mirror (excerpt-tier); gearlive
corroboration ("Meta didn't say this pair exists because of privacy.
Gizmodo's headline said it for them."); WeSearch 5-outlet synthesis
(Mashable/TechCrunch/Engadget/Gizmodo + 1)). 1 browser.open success this run
(the Gizmodo embed page, dek-tier first-hand), 0 browser.open failures.
Sun/Keach and mobilesyrup arms REJECTED as primary (no within-journalist
competitor pair in corpus scope). Pre-commit novelty greps per #715: max
numeric mechanism_id 805 in-tree (profiles/) pre-commit; zero
test_type_b_958 files on disk (glob); no "Type B #958" in git log (--grep);
block key zero-hit repo-wide (git grep); both primary URLs zero-hit
repo-wide (git grep -F); zero underscore-form 806 mechanism key strings
repo-wide (format-built needles); zero numeric 806 mechanism_id keys in
profiles/.

Statistical discipline per the Aug 28 2026 standing rule: MANUAL
ILLUSTRATIVE scores only, p_value/cohens_d/ci_95 NOT_CALCULATED,
is_significant False, engine NOT run; verdict directionally_supported_not_proven;
no analysis.json update; NOT artifact-grade.

Deselected pre-commit per the #565 convention: anchor 1 + rotation guard 4
(patched green in the anchor followup); iteration-log entry tests 2 fail by
design pre-commit, go green with the entry per #719; doc-sync 3 green
post-doc-sync.

Anchor placeholder: patched to the main commit SHA in the #565 follow-up.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TESTS_DIR = Path(REPO_ROOT) / "tests"
PROFILE_PATH = "profiles/careers/journalists.yaml"
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
TEST_BASENAME = (
    "test_type_b_958_james_pero_gizmodo_rayban_audio_camerafree_"
    "stigma_frame_sep23_12am.py"
)
MECH_NUM = 806
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention.
MECH_ID_MARKER = "mechanism" + "_806"
NEXT_ID_MARKER = "mechanism" + "_807"
NEXT_ID_NUMERIC = "mechanism_id: 807"
MECH_KEY = (
    "type_b_958_james_pero_gizmodo_rayban_audio_camerafree_"
    "stigma_frame_persistence_sep23"
)
NEXT_SIBLING = "\ndaniel_cooper:"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"
ITERATION = 958
TYPE_LETTER = "B"

URL_EMBED = (
    "https://gizmodo.com/meta-introduces-audio-only-smart-glasses-"
    "to-avoid-the-perv-problem-2000815782/embed"
)
URL_MIRROR = (
    "https://api.coschedule.com/wordpress/preview/"
    "187fe651-d0f2-41f4-babe-507b256fdf61"
)
URL_AUTHOR = "https://gizmodo.com/author/jpero"
URL_GEARLIVE = (
    "https://www.gearlive.com/news/article/"
    "ray-ban-meta-audio-camera-free-glasses-349"
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
    doc = _read(PROFILE_PATH)
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


class TestNovelty958:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_b_958_file(self):
        files = sorted(str(p) for p in TESTS_DIR.glob("test_type_b_958*.py"))
        assert len(files) == 1, files
        assert files[0].endswith(TEST_BASENAME), files

    @pytest.mark.anchor
    def test_type_b_958_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type B #958")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_novelty_verification_claim_present_in_block(self):
        # The block pins the pre-commit novelty greps (zero test_type_b_958
        # files on disk, no "Type B #958" in git log, max numeric
        # mechanism_id 805 in-tree pre-commit, zero underscore-form 806
        # strings repo-wide, zero numeric 806-form mechanism keys in
        # profiles/, block key zero-hit repo-wide pre-commit, both primary
        # URLs zero-hit repo-wide pre-commit); this test pins the claim in
        # the committed block, per the #752 convention.
        data = _block_data()
        rm = _fold(data["novelty"])
        assert "zero test_type_b_958 files on disk" in rm
        assert "no 'type b #958' in git log" in rm
        assert "max numeric mechanism_id 805 in-tree pre-commit" in rm
        assert "zero underscore-form 806" in rm
        assert "zero numeric 806 mechanism_id keys in profiles/" in rm
        assert "block key zero-hit repo-wide" in rm
        assert "zero 'perv-problem' / '2000815782' / 'ray-ban audio' hits" in rm


# --- Rotation guard ---------------------------------------------------------


class TestRotationCycleGuard958:
    """Rotation: 955-959 window fourth leg D->E->A->B->C."""

    @pytest.mark.rotation
    def test_fourth_leg_of_955_959_window(self):
        assert TYPE_LETTER == "B"
        assert ITERATION == 958

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {955: "D", 956: "E", 957: "A", 958: "B", 959: "C"}
        assert expected[958] == "B"
        assert list(expected.values()) == ["D", "E", "A", "B", "C"]

    @pytest.mark.rotation
    def test_predecessor_957_committed(self):
        res = _run_git("log", "--format=%H %s", "--grep", "Type A #957")
        mains = [
            line
            for line in res.stdout.splitlines()
            if "Type A #957" in line and "followup" not in line.lower()
        ]
        assert mains, "predecessor #957 main commit not found"

    @pytest.mark.rotation
    def test_successor_959_not_yet_run(self):
        res = _run_git("log", "--oneline", "--grep", "Type C #959")
        assert not res.stdout.strip(), "successor #959 already present"


# --- Mechanism content ------------------------------------------------------


class TestMechanism806Content:
    def test_block_key_unique_and_parses(self):
        doc = _read(PROFILE_PATH)
        assert doc.count(MECH_KEY + ":") == 1
        data = _block_data()
        assert data["mechanism_id"] == 806

    def test_mechanism_identity_fields(self):
        data = _block_data()
        assert data["iteration"] == 958
        assert data["type"] == "B"
        assert data["goal_id"] == "goal_54093bda4145"
        assert data["author"] == "Kit (with Ray)"
        assert data["iteration_time"] == "2026-09-24 00:00 PDT"
        # #715 designed keying: the descriptive block key must not carry the
        # underscore-form mechanism key substring.
        assert MECH_ID_MARKER not in MECH_KEY

    def test_meta_arm_audio_camerafree_register(self):
        data = _block_data()
        arm = data["meta_arm"]
        f = _fold(arm["title"] + " " + " ".join(arm["key_quotes"]))
        assert "perv" in f and "problem" in f
        assert "glasshole" in f
        assert "without a camera" in f or "sans camera" in f
        assert "43g" in f and "12-hour" in f
        assert "gizmodo" in _fold(arm["publication"])
        assert "james pero" in _fold(arm["author_byline"])
        # The stigma frame persists WITH the camera removed.
        assert "moves from hardware to brand" in f
        # Editorial-not-company-driven: the frame is Gizmodo's, not Meta's.
        assert "gizmodo's headline said it for them" in f

    def test_comparator_arms_carried_unrescored_per_807(self):
        data = _block_data()
        carried = _fold(" ".join(data["comparator_arms_carried"]))
        assert "carried un-rescored per #807" in carried
        assert "m746" in carried and "m791" in carried
        assert "+0.35" in carried
        assert "-0.65" in carried
        assert "dorky, fun" in carried
        assert "do or die" in carried

    def test_arm_provenance_urls_verbatim(self):
        data = _block_data()
        assert data["meta_arm"]["url"] == URL_EMBED
        block = _fold(_block())
        assert _fold(URL_AUTHOR) in block
        assert _fold(URL_GEARLIVE) in block
        assert _fold(URL_MIRROR) in block

    def test_extension_claims_present(self):
        data = _block_data()
        ext = _fold(" ".join(data["extension_claims"]))
        assert "extends mechanism 791 temporally" in ext
        assert "replicates the m637 peg-follows-register pattern" in ext
        assert "register follows the brand" in ext
        assert 791 in data["connects_to"] and 746 in data["connects_to"]
        assert 211 in data["connects_to"]

    def test_type_b_journalist_tracking_discipline(self):
        data = _block_data()
        assert data["cautious_language_required"] is True
        cn = _fold(data["correlational_note"])
        assert "correlational observations" in cn
        assert "no causal claim" in cn


# --- Asymmetry scorer math --------------------------------------------------


class TestAsymmetryScorerMath:
    def test_outlet_divergence_delta(self):
        data = _block_data()
        d = _fold(data["illustrative_delta"])
        assert "-0.55" in d
        assert "-0.20" in d and "+0.35" in d

    def test_delta_direction_matches_m791_asymmetry(self):
        # Same direction as m791's -0.65: the register follows the brand,
        # not the hardware feature. Manual illustrative only.
        data = _block_data()
        d = _fold(data["illustrative_delta"])
        assert "same direction as m791" in d
        assert "manual_illustrative" in _fold(data["statistical_discipline"]["tone_scores"])

    def test_confounders_ranked_strong_first(self):
        data = _block_data()
        confs = data["ranked_confounders"]
        assert [c["rank"] for c in confs] == sorted(c["rank"] for c in confs)
        assert confs[0]["strength"] == "strong"
        first_three = {c["strength"] for c in confs[:3]}
        assert first_three == {"strong"}, [c["strength"] for c in confs[:3]]
        assert data["counterevidence"], "counterevidence must be non-empty"


# --- Statistical discipline -------------------------------------------------


class TestStatisticalDiscipline958:
    def test_manual_illustrative_only(self):
        data = _block_data()
        sd = data["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"

    def test_engine_not_run_no_significance(self):
        data = _block_data()
        sd = data["statistical_discipline"]
        assert sd["engine_run"] is False
        assert sd["is_significant"] is False
        assert data["no_analysis_json_update"] is True

    def test_not_artifact_grade_correlation_not_causation(self):
        data = _block_data()
        sd = data["statistical_discipline"]
        assert sd["artifact_grade"] is False
        assert sd["qualitative_only"] is True
        assert sd["correlation_not_causation"] is True

    def test_verdict_directionally_supported_not_proven(self):
        data = _block_data()
        assert data["statistical_discipline"]["verdict"] == "directionally_supported_not_proven"


# --- Supersession and corpus state post-957 ---------------------------------


class TestSupersessionAndCorpusPost957:
    def test_corpus_max_is_806(self):
        corpus = _profiles_corpus()
        ids = [int(m) for m in re.findall(r"mechanism_id:\s*(\d+)", corpus)]
        assert max(ids) == MECH_NUM, max(ids)

    def test_iteration_957_zero_underscore_806_sweep_stays_green(self):
        # #957's zero-806 profile sweep asserted the underscore form; the
        # #715 designed keying keeps it green after this run by construction.
        assert MECH_ID_MARKER not in _profiles_corpus()

    def test_iteration_957_zero_numeric_806_fails_by_designed_supersession(self):
        # #957's zero-numeric-806 sweep is superseded by this run's
        # mechanism_id 806 assignment, by design.
        assert "mechanism_id: 806" in _profiles_corpus()

    def test_zero_underscore_807_repo_wide(self):
        corpus = _profiles_corpus()
        assert NEXT_ID_MARKER not in corpus

    def test_zero_numeric_807_in_profiles(self):
        assert NEXT_ID_NUMERIC not in _profiles_corpus()

    def test_numeric_806_keys_in_exactly_the_designed_location(self):
        doc = _read(PROFILE_PATH)
        assert doc.count("mechanism_id: 806") == 1
        start = doc.index("james_pero:")
        end = doc.index("daniel_cooper:", start)
        assert "mechanism_id: 806" in doc[start:end]


# --- Falsification ledger ---------------------------------------------------


class TestLedger958:
    def test_thirtieth_present_and_thirty_first_absent(self):
        corpus = _profiles_corpus()
        assert "THIRTIETH" in corpus
        assert "THIRTY-FIRST" not in corpus

    def test_m806_block_key_unique_and_parses(self):
        doc = _read(PROFILE_PATH)
        assert doc.count(MECH_KEY + ":") == 1

    def test_m806_not_a_falsification_family_member(self):
        data = _block_data()
        ff = _fold(data["falsification_family"])
        assert "not a member" in ff
        assert "ledger holds at 29" in ff

    def test_ledger_count_unchanged_by_this_run(self):
        # This run documents register persistence; it does not test a
        # uniform prediction, so the ledger stays at 29.
        corpus = _profiles_corpus()
        assert "TWENTY-NINTH" in corpus


# --- Doc sync ----------------------------------------------------------------


class TestDocSync958:
    def test_readme_stats_table_updated(self):
        readme = _read(README_PATH)
        assert "49344" in readme and "1283" in readme

    def test_readme_test_file_table_row_present(self):
        assert TEST_BASENAME.replace(".py", "") in _read(README_PATH)

    def test_architecture_tests_tree_updated(self):
        assert TEST_BASENAME.replace(".py", "") in _read(ARCH_PATH)


# --- Iteration log ----------------------------------------------------------


class TestIterationLog958:
    def test_log_has_958_marker(self):
        assert "## #958 Type B" in _read(LOG_PATH)

    def test_log_entry_names_window_leg(self):
        assert "955-959 window" in _read(LOG_PATH)


# --- Push readiness ----------------------------------------------------------


class TestPushReadiness958:
    def test_ascii_only_no_em_dashes(self):
        text = _read(os.path.join("tests", TEST_BASENAME))
        assert "\u2014" not in text
        assert all(ord(c) < 128 for c in text)

    def test_profile_block_ascii_only_no_em_dashes(self):
        text = _block()
        assert "\u2014" not in text
        assert all(ord(c) < 128 for c in text)

    def test_no_literal_underscore_806_in_test_file(self):
        # The #715 sweep-instrument convention: the literal contiguous
        # underscore-form key must not appear in this file.
        text = _read(os.path.join("tests", TEST_BASENAME))
        assert MECH_ID_MARKER not in text

    def test_concurrent_files_untouched_by_this_run(self):
        # git diffs on the in-flight files must show only their own
        # blocks (m762 / m771); this run adds no 958 hunks to them.
        # #938's test file carries #938's own open anchor-followup working-tree
        # edit (owned by #938's chain, untouched by #958). The untracked
        # #900 Type D file is not in any diff; assert no 958 marker in it.
        for f, own in (
            ("profiles/competitor-entities.yaml", "762"),
            ("profiles/nytimes.yaml", "771"),
        ):
            diff = _run_git("diff", "--", f).stdout
            assert ("mechanism" + "_id" + ": " + own) in diff
            assert "958" not in diff
        rdiff = _run_git(
            "diff", "--",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_"
            "gemini_personalization_vs_meta_luna_stigma_sep16.py",
        ).stdout
        assert "958" not in rdiff
        d900 = _read(
            "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py"
        )
        assert "958" not in d900
        assert MECH_ID_MARKER not in d900
