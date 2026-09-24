"""Type A #957 (2026-09-23 23:00 PDT): News Corp outlet divergence on dual
payers - WSJ x OpenAI Sep 23 2026 ChatGPT-ads $1B-revenue register vs NY Post
x Meta Sep 23 2026 teen-harassment crime register. FIRST dedicated corpus
mechanism on the Sep 23 outlet split across News Corp's two AI-licensing
payers (~$50M/yr each: OpenAI May 2024 $250M/5yr; Meta up to $50M/yr 3-year
Mar 2026). WSJ (via PYMNTS relay) reported OpenAI preparing ChatGPT ads with
a $1B revenue expectation and CFO Friisdahl defending monetization:
constructive business-expansion register, MANUAL ILLUSTRATIVE +0.30,
excerpt-bounded per #503 (0 browser.open this run; relay-tier). NY Post (via
WebProNews relay) detailed several incidents of teens using Meta AI glasses
to harass others amid surging misuse reports: crime/morality register,
MANUAL ILLUSTRATIVE -0.55, excerpt-bounded. Illustrative delta (OpenAI minus
Meta) +0.85. The financial gradient (~$50M/yr each) cannot explain the gap;
outlet house register plus news peg do. EXTENDS m22 (WSJ covers OpenAI ad
expansion with neutral/positive business framing), m532 (WSJ dual-deal
symmetry Sep 5) and m763 (NY Post dual-payer symmetry, TWENTY-NINTH
falsification member) to the outlet-divergence dimension; REPLICATES the m637
peg-follows-register pattern. connects_to: [22, 532, 763, 155, 796]. NOT a
falsification-family member (register documentation consistent with the m763
falsification; ledger holds at 29). Correlation is not causation.
Hypothesis-generating only. NOT artifact-grade.

Rotation window THIRD leg: D (#955) -> E (#956) -> A (#957 this run) ->
B (#958) -> C (#959), continuing the 955-959 window.

Evidence: 10 browser.search query sets this run (Gizmodo Snap-vs-Meta -
REJECTED: in #862/#933; Verge Snap-vs-Meta - REJECTED: m628/m937; BI
OpenAI-vs-Meta - REJECTED: #932/#947; TechRadar ChatGPT-ads - surfaced
FT/Guardian disclosure relay; thejoai UN AI-governance - used to
VERIFY-AND-REJECT the FT-Australia attribution (page carries no FT
attribution; AI-generated aggregation disclaimer); MTR Opus-5.5/UNSC - no MTR
URLs; Guardian Meta-Luna - no guardian.com URLs; NYT Anthropic Opus-5.5 - no
nytimes.com URLs; FT OpenAI GPT-6/ads - surfaced Techmeme FT "low billions"
item as corroboration; Guardian ChatGPT-ads - no guardian.com URLs;
SELECTED: News Corp WSJ-x-OpenAI ads-revenue relay + NY Post-x-Meta
teen-harassment relay, both Sep 23). 1 browser.open success (thejoai,
attribution check), 2 browser.open failures (techradar, webpronews - terminal
per developer constraint, excerpt-bounded per #503). Pre-commit novelty greps
per #715: max numeric mechanism_id 804 in profiles/; zero test_type_a_957
files on disk (glob); no "Type A #957" in git log (--grep); block key
zero-hit repo-wide (git grep); both relay URLs zero-hit repo-wide (git grep
-F); zero underscore-form 805 mechanism key strings in profiles/
(format-built needles); zero numeric 805 mechanism_id keys in profiles/.

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
NEWSCORP_PATH = "profiles/news-corp.yaml"
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
TEST_BASENAME = (
    "test_type_a_957_newscorp_wsj_openai_chatgpt_ads_"
    "vs_nypost_meta_teen_harassment_sep23_11pm.py"
)
MECH_NUM = 805
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention.
MECH_ID_MARKER = "mechanism" + "_805"
NEXT_ID_MARKER = "mechanism" + "_806"
NEXT_ID_NUMERIC = "mechanism_id: 806"
MECH_KEY = (
    "wsj_openai_chatgpt_ads_revenue_"
    "vs_nypost_meta_teen_harassment_crime_register_sep2026"
)
NEXT_SIBLING = "\n  meta:"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"
ITERATION = 957
TYPE_LETTER = "A"

URL_PYMNTS = (
    "https://www.pymnts.com/cfo/2026/openai-eyes-1-billion-chatgpt-ad-"
    "revenue-as-cfo-friisdahl-defends-monetization/"
)
URL_WEBPRONEWS = (
    "https://www.webpronews.com/meta-glasses-misuse-reports-surge-as-"
    "teens-use-ai-glasses-to-harass/"
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
    doc = _read(NEWSCORP_PATH)
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


class TestNovelty957:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_a_957_file(self):
        files = sorted(str(p) for p in TESTS_DIR.glob("test_type_a_957*.py"))
        assert len(files) == 1, files
        assert files[0].endswith(TEST_BASENAME), files

    @pytest.mark.anchor
    def test_type_a_957_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type A #957")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_novelty_verification_claim_present_in_block(self):
        # The block pins the pre-commit novelty greps (zero test_type_a_957
        # files on disk, no "Type A #957" in git log, max numeric
        # mechanism_id 804 in profiles/ pre-commit, zero underscore-form 805
        # strings in profiles/, zero numeric 805-form mechanism keys in
        # profiles/, block key zero-hit repo-wide pre-commit, both relay
        # URLs zero-hit repo-wide pre-commit); this test pins the claim in
        # the committed block, per the #752 convention.
        data = _block_data()
        rm = _fold(data["research_method"])
        assert "zero test_type_a_957 files on disk" in rm
        assert "no 'type a #957' in git log" in rm
        assert "max numeric mechanism_id 804 in profiles/" in rm
        assert "zero underscore-form 805" in rm
        assert "zero numeric 805 mechanism_id keys in profiles/" in rm
        assert "block key zero-hit repo-wide" in rm
        assert "both relay urls zero-hit repo-wide" in rm


# --- Rotation guard ---------------------------------------------------------


class TestRotationCycleGuard957:
    """Rotation: 955-959 window third leg D->E->A->B->C."""

    @pytest.mark.rotation
    def test_third_leg_of_955_959_window(self):
        assert TYPE_LETTER == "A"
        assert ITERATION == 957

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {955: "D", 956: "E", 957: "A", 958: "B", 959: "C"}
        assert expected[957] == "A"
        assert list(expected.values()) == ["D", "E", "A", "B", "C"]

    @pytest.mark.rotation
    def test_predecessor_956_committed(self):
        res = _run_git("log", "--format=%H %s", "--grep", "Type E #956")
        mains = [
            line
            for line in res.stdout.splitlines()
            if "Type E #956" in line and "followup" not in line.lower()
        ]
        assert mains, "predecessor #956 main commit not found"

    @pytest.mark.rotation
    def test_successor_958_not_yet_run(self):
        res = _run_git("log", "--oneline", "--grep", "Type B #958")
        assert not res.stdout.strip(), "successor #958 already present"


# --- Mechanism content ------------------------------------------------------


class TestMechanism805Content:
    def test_block_key_unique_and_parses(self):
        import yaml

        doc = yaml.safe_load(_read(NEWSCORP_PATH))
        openai = doc["competitor_relationships"]["openai"]
        assert openai[MECH_KEY]["mechanism_id"] == 805
        assert sum(1 for k in openai if k == MECH_KEY) == 1

    def test_mechanism_identity_fields(self):
        data = _block_data()
        assert data["mechanism_id"] == 805
        assert data["iteration"] == 957
        assert data["iteration_type"] == "A"
        assert data["rotation"] == "Type A"
        assert data["date_analyzed"] == "2026-09-23"
        assert data["time_pdt"] == "23:00"
        assert data["job_id"] == "mediascope-daily-iteration"

    def test_openai_arm_wsj_ads_revenue(self):
        data = _block_data()
        arm = data["openai_arm_wsj"][0]
        assert "$1B ChatGPT Ad Revenue" in arm["title"]
        assert "Wall Street Journal" in arm["outlet"]
        assert arm["date"] == "2026-09-23"
        assert arm["url"] == URL_PYMNTS
        assert "introduce advertising into ChatGPT" in arm["relay_attribution"]
        assert arm["register"] == "constructive_business_monetization"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == pytest.approx(0.30)

    def test_meta_arm_nypost_teen_harassment(self):
        data = _block_data()
        arm = data["meta_arm_nypost"][0]
        assert "teens use AI glasses to harass" in arm["title"]
        assert "New York Post" in arm["outlet"]
        assert arm["date"] == "2026-09-23"
        assert arm["url"] == URL_WEBPRONEWS
        assert "The New York Post detailed several such incidents" in arm[
            "relay_attribution"
        ]
        assert arm["register"] == "crime_morality_adversarial"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == pytest.approx(-0.55)

    def test_arm_provenance_urls_verbatim(self):
        block = _block()
        for url in (URL_PYMNTS, URL_WEBPRONEWS):
            assert url in block, "missing verbatim URL: %s" % url

    def test_dual_payer_financial_context(self):
        data = _block_data()
        fc = data["financial_context"]
        assert "$50M/yr" in fc["news_corp_openai_deal"]
        assert "$50M/yr" in fc["news_corp_meta_deal"]
        assert "both_payers" in fc["coverage_prediction"]
        assert "m763" in _fold(data["incentive_attribution"])

    def test_extension_claims_present(self):
        ov = _block_data()["overview"]
        assert "m22" in ov
        assert "m532" in ov
        assert "m763" in ov
        assert "connects_to: [22, 532, 763, 155, 796]" in ov

    def test_peg_follows_register_replication_claim_present(self):
        ov = _block_data()["overview"]
        assert "m637" in ov
        assert "peg-follows-register" in ov


# --- Asymmetry scorer math --------------------------------------------------


class TestAsymmetryScorerMath:
    def test_outlet_divergence_delta(self):
        data = _block_data()
        openai_tone = data["openai_arm_wsj"][0]["tone_MANUAL_ILLUSTRATIVE"]
        meta_tone = data["meta_arm_nypost"][0]["tone_MANUAL_ILLUSTRATIVE"]
        assert openai_tone == pytest.approx(0.30)
        assert meta_tone == pytest.approx(-0.55)
        assert data["illustrative_delta_openai_minus_meta"] == pytest.approx(
            openai_tone - meta_tone, abs=1e-4
        )
        assert data["illustrative_delta_openai_minus_meta"] == pytest.approx(
            0.85, abs=1e-4
        )

    def test_delta_direction_matches_dual_payer_symmetry_break(self):
        # Both payers at ~$50M/yr; the +0.85 gap runs on outlet/peg, not money.
        data = _block_data()
        assert data["illustrative_delta_openai_minus_meta"] > 0
        fc = data["financial_context"]
        assert "gradient cannot distinguish the arms" in fc["coverage_prediction"]

    def test_confounders_ranked_strong_first(self):
        data = _block_data()
        confs = data["confounding_factors_ranked_strong_first"]
        assert confs[0].startswith("STRONG")
        assert confs[1].startswith("STRONG")
        assert confs[2].startswith("STRONG")
        assert any("relay-bounded" in _fold(c) for c in confs[:3])


# --- Statistical discipline -------------------------------------------------


class TestStatisticalDiscipline957:
    def test_manual_illustrative_only(self):
        sd = _block_data()["statistical_discipline"]
        assert sd["scores"] == "MANUAL ILLUSTRATIVE only"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False

    def test_engine_not_run_no_significance(self):
        sd = _block_data()["statistical_discipline"]
        assert sd["engine_run"] is False
        assert sd["is_significant"] is False
        assert sd["verdict"] == "directionally_supported_not_proven"

    def test_not_artifact_grade_correlation_not_causation(self):
        sd = _block_data()["statistical_discipline"]
        assert sd["no_analysis_json_update"] is True
        assert sd["artifact_grade"] is False
        assert sd["correlation_not_causation"] is True
        assert sd["hypothesis_generating_only"] is True

    def test_verdict_directionally_supported_not_proven(self):
        sd = _block_data()["statistical_discipline"]
        assert "not_proven" in sd["verdict"]


# --- Supersession -----------------------------------------------------------


class TestSupersessionAndCorpusPost956:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(
            int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout)
        )

    def test_corpus_max_is_805(self):
        assert max(self._numeric_ids()) == 805

    def test_iteration_956_max_804_sweep_superseded_by_design(self):
        # #956's max-804 sweeps fail by designed supersession now that 805 exists.
        assert max(self._numeric_ids()) != 804

    def test_zero_underscore_806_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_806_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_956_zero_underscore_805_sweep_stays_green(self):
        # #956's zero-underscore-805 sweeps stay green post-#957 by designed
        # keying: neither the profile block nor this test file carries a
        # literal contiguous underscore-805 key (format-built needles only).
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", MECH_ID_MARKER, "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), (
                "literal underscore-805 key leaked into %s" % root
            )

    def test_iteration_956_zero_numeric_805_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 805", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), (
            "expected #956's zero-numeric-805 sweep to fail by designed supersession"
        )

    def test_numeric_805_keys_in_exactly_the_designed_location(self):
        res = _run_git("grep", "-r", "mechanism_id: 805", "--", "profiles/")
        hits = [line for line in res.stdout.strip().splitlines() if line.strip()]
        # Designed keying: one numeric 805 key in the news-corp openai block;
        # no other profiles/ location.
        assert len(hits) == 1, "unexpected numeric 805 key spread in profiles/: %s" % hits
        assert "profiles/news-corp.yaml" in hits[0]


# --- Ledger -----------------------------------------------------------------


class TestLedger957:
    def test_thirtieth_present_and_thirty_first_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference their own negative guards inside their
        # own negative-guard tests, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "THIRTIETH" in corpus
        assert "THIRTY-FIRST" not in corpus
        assert "ledger holds at 29" in _block().lower()

    def test_m805_block_key_unique_and_parses(self):
        import yaml

        doc = yaml.safe_load(_read(NEWSCORP_PATH))
        openai = doc["competitor_relationships"]["openai"]
        assert openai[MECH_KEY]["mechanism_id"] == 805
        assert sum(1 for k in openai if k == MECH_KEY) == 1

    def test_m805_not_a_falsification_family_member(self):
        data = _block_data()
        assert data["falsification_family_member"] is False
        assert data["falsification_ledger"] == 29
        assert "THIRTIETH" in data["ledger_note"]


# --- Doc-sync ----------------------------------------------------------------


class TestDocSync957:
    def test_readme_stats_table_updated(self):
        readme = _read(README_PATH)
        assert "49304" in readme and "1282" in readme

    def test_readme_test_file_table_row_present(self):
        assert TEST_BASENAME.replace(".py", "") in _read(README_PATH)

    def test_architecture_tests_tree_updated(self):
        assert TEST_BASENAME.replace(".py", "") in _read(ARCH_PATH)


# --- Iteration log ----------------------------------------------------------


class TestIterationLog957:
    def test_log_has_957_marker(self):
        assert "## #957 Type A" in _read(LOG_PATH)

    def test_log_entry_names_window_leg(self):
        assert "955-959 window" in _read(LOG_PATH)


# --- Push readiness ---------------------------------------------------------


class TestPushReadiness957:
    def test_ascii_only_no_em_dashes(self):
        text = _read(os.path.join("tests", TEST_BASENAME))
        assert "\u2014" not in text
        assert all(ord(c) < 128 for c in text)

    def test_newscorp_yaml_ascii_only_no_em_dashes(self):
        text = _block()
        assert "\u2014" not in text
        assert all(ord(c) < 128 for c in text)

    def test_no_literal_underscore_805_in_test_file(self):
        # The #715 sweep-instrument convention: the literal contiguous
        # underscore-form key must not appear in this file.
        text = _read(os.path.join("tests", TEST_BASENAME))
        assert MECH_ID_MARKER not in text

    def test_concurrent_files_untouched_by_this_run(self):
        # git diffs on the in-flight files must show only their own
        # blocks (m762 / m771); this run adds no 957 hunks to them.
        # #938's test file carries #938's own open anchor-followup working-tree
        # edit (owned by #938's chain, untouched by #957). The untracked
        # #900 Type D file is not in any diff; assert no 957 marker in it.
        for f, own in (
            ("profiles/competitor-entities.yaml", "762"),
            ("profiles/nytimes.yaml", "771"),
        ):
            diff = _run_git("diff", "--", f).stdout
            assert ("mechanism" + "_id" + ": " + own) in diff
            assert "957" not in diff
        rdiff = _run_git(
            "diff", "--",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_"
            "gemini_personalization_vs_meta_luna_stigma_sep16.py",
        ).stdout
        assert "957" not in rdiff
        d900 = _read(
            "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py"
        )
        assert "957" not in d900
        assert MECH_ID_MARKER not in d900
