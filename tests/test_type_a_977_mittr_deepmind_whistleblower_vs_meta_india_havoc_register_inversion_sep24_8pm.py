"""Type A #977 (2026-09-24 20:00 PDT): MIT TR September agent-misbehavior
register inversion - DeepMind cheating agents (Sep 14) get the fascination
register while Meta wearables (Sep 23 India investigation) get the havoc
accountability register. Same-month pair, both arms opened via browser.open
this run (full text); EXTENDS mechanism 476 with fresh evidence on both sides.

NEW-TO-CORPUS: (Google) MIT TR Sep 14 2026 "When AI agents cheated at math,
other AI agents blew the whistle on them" (prover-theta exploit, 14 cheated,
24 whistleblowers, Paglieri quoted at length, "reads like improv", zero
incompetence vocabulary) - MANUAL ILLUSTRATIVE +0.30. (Meta) MIT TR Sep 23
2026 "Smart glasses are already causing havoc in India" (Shubnam case, Delhi
police filming protesters, LED circumvention, FT passive-AI prototypes,
Hartzog kicker) - MANUAL ILLUSTRATIVE -0.60.

Illustrative delta (Meta minus Google): -0.60 - 0.30 = -0.90, n=1 per side,
NOT significant. The mechanism claim is register-level: the same underlying
theme (AI systems misbehaving) gets opposite registers by company, nine days
apart in the same publication. Within-article support: the Sep 14 piece frames
OpenAI's July Hugging Face breakout as "systemic" while DeepMind's own
cheating gets the whistleblower-hero arc. Cooperative-conflict counterevidence:
MIT TR runs its hardest-hitting Meta investigation despite MIT's Meta (FAIR)
funding - the two-sided nexus bounds the financial-incentive theory rather
than confirming it. Connects [476, 477, 15, 637, 742].

Statistical discipline per the Aug 28 2026 standing rule: MANUAL ILLUSTRATIVE
scores only, p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False,
engine NOT run at the finding layer; verdict directionally_supported_not_proven;
no analysis.json update; NOT artifact-grade.

Deselected pre-commit per the #565 convention: anchor 1 + rotation guard 4
(patched green in the anchor followup). Doc-sync 3 + iteration-log 2 fail
pre-commit per #719, all green post-doc-sync.

Anchor placeholder: patched to the main commit SHA in the #565 follow-up.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TESTS_DIR = Path(REPO_ROOT) / "tests"
MITTR_PATH = "profiles/mit-tech-review.yaml"
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
TEST_BASENAME = (
    "test_type_a_977_mittr_deepmind_whistleblower_vs_meta_india_havoc_"
    "register_inversion_sep24_8pm.py"
)
MECH_NUM = 817
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention. The YAML block key is
# descriptive by the #723/#738/#739 designed-keying convention (no
# underscore-form mechanism key substring), keeping the zero-underscore
# sweeps green post-commit.
MECH_ID_MARKER = "mechanism" + "_817"
NEXT_ID_MARKER = "mechanism" + "_818"
NEXT_ID_NUMERIC = "mechanism_id: 818"
MECH_KEY = (
    "mittr_sep14_deepmind_cheating_agents_whistleblowers_"
    "vs_sep23_meta_india_havoc_sep24_2026"
)
NEXT_SIBLING = "\n  x_twitter:"
ANCHORED_SHA = "b3b4de30a71fe7a19b58406903a29b5f9e2e3fdd"
ITERATION = 977
TYPE_LETTER = "A"

URL_GOOGLE = (
    "https://www.technologyreview.com/2026/09/14/1144037/"
    "ai-agents-blew-whistle-o-cheating-colleagues/"
)
URL_META = (
    "https://www.technologyreview.com/2026/09/23/1144953/"
    "smart-glasses-havoc-india/"
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
    doc = _read(MITTR_PATH)
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


class TestNovelty977:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_a_977_file(self):
        files = sorted(str(p) for p in TESTS_DIR.glob("test_type_a_977*.py"))
        assert len(files) == 1, files
        assert files[0].endswith(TEST_BASENAME), files

    @pytest.mark.anchor
    def test_type_a_977_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--format=%H %s", "--grep", "Type A #977")
        assert res.stdout.count(ANCHORED_SHA) == 1, (
            "main commit SHA not unique in Type A #977 log"
        )

    def test_novelty_verification_claim_present_in_block(self):
        # The block pins the pre-commit novelty greps (zero test_type_a_977
        # files on disk, no "Type A #977" in git log, max numeric
        # mechanism_id 816 in profiles/ pre-commit, zero underscore-form 817
        # strings in profiles/ and tests/, zero numeric 817-form mechanism
        # keys in profiles/, zero dash-form 817 references in profiles/,
        # block key zero-hit repo-wide pre-commit, two new urls zero-hit
        # repo-wide pre-commit); this test pins the claim in the committed
        # block, per the #752 convention.
        data = _block_data()
        # Folded block text doubles single quotes inside YAML single-quoted
        # scalars; normalize before asserting the prose claims.
        rm = _fold(data["research_method"]).replace("''", "'")
        assert "zero test_type_a_977 files on disk" in rm
        assert 'no "type a #977" in git log' in rm
        assert "max numeric mechanism_id 816 in profiles/" in rm
        assert "zero underscore-form 817" in rm
        assert "zero numeric 817-form mechanism keys in profiles/" in rm
        assert "zero dash-form 817 references in profiles/" in rm
        assert "block key zero-hit repo-wide" in rm
        assert "two new urls zero-hit repo-wide" in rm


# --- Rotation guard ---------------------------------------------------------


class TestRotationCycleGuard977:
    """Rotation: 975-979 window third leg D->E->A->B->C."""

    @pytest.mark.rotation
    def test_third_leg_of_975_979_window(self):
        assert TYPE_LETTER == "A"
        assert ITERATION == 977

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {975: "D", 976: "E", 977: "A", 978: "B", 979: "C"}
        assert expected[977] == "A"
        assert list(expected.values()) == ["D", "E", "A", "B", "C"]

    @pytest.mark.rotation
    def test_predecessor_976_committed(self):
        res = _run_git("log", "--format=%H %s", "--grep", "Type E #976")
        mains = [
            line
            for line in res.stdout.splitlines()
            if "Type E #976" in line and "followup" not in line.lower()
        ]
        assert mains, "predecessor #976 main commit not found"

    @pytest.mark.rotation
    def test_successor_978_not_yet_run(self):
        res = _run_git("log", "--oneline", "--grep", "Type B #978")
        assert not res.stdout.strip(), "successor #978 already present"


# --- Mechanism content ------------------------------------------------------


class TestMechanism817Content:
    def test_block_key_unique_and_parses(self):
        import yaml

        doc = yaml.safe_load(_read(MITTR_PATH))
        google = doc["competitor_relationships"]["google"]
        assert google[MECH_KEY]["mechanism_id"] == 817
        assert sum(1 for k in google if k == MECH_KEY) == 1

    def test_mechanism_identity_fields(self):
        data = _block_data()
        assert data["mechanism_id"] == 817
        assert data["iteration"] == 977
        assert data["iteration_type"] == "A"
        assert data["type"] == "Type A - Competitor Coverage Deep Dive"
        assert data["scheduled_job_id"] == "mediascope-daily-iteration"
        assert data["goal_id"] == "goal_54093bda4145"

    def test_google_arm_register_and_tone(self):
        data = _block_data()
        finding = data["finding"]
        assert "Paglieri" in finding
        assert "prover-theta" in finding
        assert "reads like improv" in finding
        assert "+0.30" in finding
        assert data["google_arm"]["tone"] == 0.30
        assert "blew the whistle" in data["google_arm"]["headline"]
        assert data["google_arm"]["register"] == "playful_scientific_fascination"
        res = data["asymmetry_scorer_result"]
        assert res["google_new_arm_tone"] == 0.30

    def test_meta_arm_register_and_tone(self):
        data = _block_data()
        finding = data["finding"]
        assert "Shubnam" in finding
        assert "havoc" in finding
        assert "Hartzog" in finding
        assert "-0.60" in finding
        assert data["meta_arm"]["tone"] == -0.60
        assert "havoc in India" in data["meta_arm"]["headline"]
        assert data["meta_arm"]["register"] == "investigative_accountability"
        res = data["asymmetry_scorer_result"]
        assert res["meta_new_arm_tone"] == -0.60

    def test_arm_provenance_urls_verbatim(self):
        data = _block_data()
        urls = data["source_urls"]
        assert URL_GOOGLE in urls
        assert URL_META in urls
        assert len(urls) == 2

    def test_financial_context_two_sided_nexus(self):
        import yaml

        doc = yaml.safe_load(_read(MITTR_PATH))
        google = doc["competitor_relationships"]["google"]
        assert google["financial_tie"] == "indirect"
        meta = doc["competitor_relationships"]["meta"]
        assert meta["financial_tie"] == "none"
        assert meta["coverage_prediction"] == "adversarial"
        fin = _block_data()["financial_two_sided_nexus"]
        assert "FAIR" in fin
        assert "MIT-Google Program" in fin
        assert "BOTH sides" in fin

    def test_extension_claims_present(self):
        finding = _block_data()["finding"]
        assert "EXTENDS m476" in finding
        assert "REPLICATES" in finding
        assert "cooperative-conflict counterevidence" in finding
        connects = _block_data()["connects_to"]
        for mid in (476, 477, 15, 637, 742):
            assert mid in connects

    def test_within_article_openai_contrast(self):
        data = _block_data()
        contrast = data["within_article_openai_contrast"]
        assert "systemic" in contrast
        assert "Hammond" in contrast
        assert "entity-directed" in contrast


# --- Asymmetry math ----------------------------------------------------------


class TestAsymmetryScorerMath:
    def test_nine_day_window_delta(self):
        res = _block_data()["asymmetry_scorer_result"]
        delta = round(res["meta_new_arm_tone"] - res["google_new_arm_tone"], 2)
        assert delta == res["delta_meta_minus_google"] == -0.90

    def test_tones_match_arm_registers(self):
        data = _block_data()
        res = data["asymmetry_scorer_result"]
        assert res["google_new_arm_tone"] == data["google_arm"]["tone"]
        assert res["meta_new_arm_tone"] == data["meta_arm"]["tone"]
        assert data["nine_day_window"].startswith("Sep 14 2026")

    def test_confounders_ranked_strong_first(self):
        confs = _block_data()["confounders"]
        assert len(confs) == 6
        assert all(c.startswith("STRONG") for c in confs[:3])
        assert confs[3].startswith("MODERATE")
        assert confs[4].startswith("MODERATE")
        assert confs[5].startswith("WEAK")


# --- Statistical discipline --------------------------------------------------


class TestStatisticalDiscipline977:
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
        assert (
            "verdict directionally_supported_not_proven"
            in data["statistical_discipline"].lower()
        )


# --- Supersession ------------------------------------------------------------


class TestSupersessionAndCorpusPost976:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(
            int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout)
        )

    def test_corpus_max_is_817(self):
        assert max(self._numeric_ids()) == 817

    def test_iteration_976_max_816_sweep_superseded_by_design(self):
        # #976's max-816 sweeps fail by designed supersession now that 817 exists.
        assert max(self._numeric_ids()) != 816

    def test_zero_underscore_818_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_818_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_976_zero_underscore_817_sweep_stays_green(self):
        # #976's zero-underscore-817 sweeps stay green post-#977 by designed
        # keying: neither the profile block nor this test file carries a
        # literal contiguous underscore-817 key (format-built needles only).
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", MECH_ID_MARKER, "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), (
                "literal underscore-817 key leaked into %s" % root
            )

    def test_iteration_976_zero_numeric_817_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 817", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), (
            "expected #976's zero-numeric-817 sweep to fail by designed supersession"
        )

    def test_numeric_817_keys_in_exactly_the_designed_location(self):
        res = _run_git("grep", "-r", "mechanism_id: 817", "--", "profiles/")
        hits = [line for line in res.stdout.strip().splitlines() if line.strip()]
        # Designed keying: one numeric 817 key in the mit-tech-review google
        # block; no other profiles/ location.
        assert len(hits) == 1, "unexpected numeric 817 key spread in profiles/: %s" % hits
        assert "profiles/mit-tech-review.yaml" in hits[0]


# --- Ledger -----------------------------------------------------------------


class TestLedger977:
    def test_thirtieth_present_and_thirty_first_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference their own negative guards inside their
        # own negative-guard tests, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "THIRTIETH" in corpus
        assert "THIRTY-FIRST" not in corpus
        assert "ledger holds at 29" in _block().lower()

    def test_m817_block_key_unique_and_parses(self):
        import yaml

        doc = yaml.safe_load(_read(MITTR_PATH))
        google = doc["competitor_relationships"]["google"]
        assert google[MECH_KEY]["mechanism_id"] == 817
        assert sum(1 for k in google if k == MECH_KEY) == 1

    def test_m817_not_a_falsification_family_member(self):
        data = _block_data()
        assert data["falsification_family_member"] is False
        assert data["falsification_ledger"] == 29
        assert "THIRTIETH" in data["ledger_note"]


# --- Doc-sync ----------------------------------------------------------------


class TestDocSync977:
    def test_readme_stats_table_updated(self):
        readme = _read(README_PATH)
        assert "50313" in readme and "1302" in readme

    def test_readme_test_file_table_row_present(self):
        assert TEST_BASENAME.replace(".py", "") in _read(README_PATH)

    def test_architecture_tests_tree_updated(self):
        assert TEST_BASENAME.replace(".py", "") in _read(ARCH_PATH)


# --- Iteration log ----------------------------------------------------------


class TestIterationLog977:
    def test_log_has_977_marker(self):
        assert "## #977 Type A" in _read(LOG_PATH)

    def test_log_entry_names_window_leg(self):
        assert "975-979 window" in _read(LOG_PATH)


# --- Push readiness ---------------------------------------------------------


class TestPushReadiness977:
    def test_ascii_only_no_em_dashes(self):
        text = _read(os.path.join("tests", TEST_BASENAME))
        assert "\u2014" not in text
        assert all(ord(c) < 128 for c in text)

    def test_mittr_yaml_block_ascii_only_no_em_dashes(self):
        text = _block()
        assert "\u2014" not in text
        assert all(ord(c) < 128 for c in text)

    def test_no_literal_underscore_817_in_test_file(self):
        # The #715 sweep-instrument convention: the literal contiguous
        # underscore-form key must not appear in this file.
        text = _read(os.path.join("tests", TEST_BASENAME))
        assert MECH_ID_MARKER not in text

    def test_concurrent_files_untouched_by_this_run(self):
        # git diffs on the in-flight files must show only their own
        # blocks (m771); this run adds no 977 hunks to them.
        # #938's test file carries #938's own open anchor-followup working-tree
        # edit (owned by #938's chain, untouched by #977). The untracked
        # #900 Type D file is not in any diff; assert no 977 marker in it.
        diff = _run_git("diff", "--", "profiles/nytimes.yaml").stdout
        assert "mechanism_id: 771" in diff
        assert "977" not in diff
        rdiff = _run_git(
            "diff", "--",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_"
            "gemini_personalization_vs_meta_luna_stigma_sep16.py",
        ).stdout
        assert "977" not in rdiff
        d900 = _read(
            "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py"
        )
        assert "977" not in d900
        assert MECH_ID_MARKER not in d900
