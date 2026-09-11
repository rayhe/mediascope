"""Type A #672: MIT Technology Review x OpenAI agentic-safety accountability
register vs MIT Technology Review x Meta agentic-failure register
(mechanism 637, competitor_relationships.openai in profiles/mit-tech-review.yaml).

FIRST dedicated MIT TR x OpenAI Type A mechanism (prior openai block held only
financial metadata: indirect Prorata AI content-partner tie, prediction
neutral). All four OpenAI-arm-side Download/math URLs are NEW to the corpus
this run (repo-wide greps on URL fragments pre-commit):
(1) Sep 8 2026, "What OpenAI's latest controversy tells us about the future
of math" - MIT TR original, FIRST-HAND read this run (all 89 lines);
accountability-skeptical register: credit-scooping controversy over
Buckmaster/Alpoge work, agent opacity via Hugging Face hack callback, "lack of
collaborative spirit"; achievements credited ("indisputably impressive") -0.25
MANUAL ILLUSTRATIVE, first_hand (byline unattested in fetch);
(2) Sep 2 2026 Download: Astra "critical" cyber-risk rating with MIT TR
original cultural-problems linkage ("Its safety issues could indicate cultural
problems") -0.20, relay_bounded;
(3) Aug 19 2026 Download: Astra safety pause + Guardian hype-skepticism relay
-0.15, relay_bounded.

Meta arm: (1) Jun 5 2026 Download Meta hack "far simpler exploits" -0.40,
in-corpus via #619/#642; (2) Aug 6 2026 Download Meta rogue model
("Meta has become the latest firm to say its AI hacked another company",
"This is why AI agents can lie to reach their goals") -0.35, NEW TO CORPUS
this run, relay_bounded; (3) "Three reasons Meta will struggle with community
fact-checking" (Jan 2025) -0.55, in-corpus via #619/#642 (timing skew noted).

Scorer MANUAL ILLUSTRATIVE: illustrative delta (OpenAI minus Meta) +0.2333
(-0.20 - (-0.4333)). n=3 vs n=3 arms: engine RUN per the #642 n=3 precedent -
t=3.5000, p=0.042172, d=2.8577, is_significant True at the ENGINE layer;
EIGHTH DIVERGENCE PIN (ratchet 7 -> 8; #642 was seventh): p=0.042172 is the
LARGEST p-value in the divergence class (barely under 0.05). Finding layer
refuses empirical claims per the Aug 28 2026 standing rule.

Financial context: predictor indirect_prorata_tie; prediction ordering
neutral (OpenAI) vs adversarial (Meta); observed direction CONSISTENT, so NOT
a falsification-family member: no named gradient contradicted, the Prorata
tie is not an OpenAI payer leg. The Prorata content-partner tie buys OpenAI
no visible softness. Correlation only, not causation.

Rotation: Type A follows Type E (#671) per A,B,C,D,E. Rotation guard fails
by design pre-anchor; anchor patched in the followup per the #565 convention.
"""

import glob
import os
import re
import subprocess
import sys

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = os.path.basename(__file__)
PROFILE_PATH = os.path.join(REPO_ROOT, "profiles", "mit-tech-review.yaml")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = (
    "mechanism_637_mittr_openai_agentic_safety_accountability_register_"
    "vs_meta_agentic_failure_sep2026"
)

MATH_URL = (
    "https://www.technologyreview.com/2026/09/08/1143747/"
    "what-openais-latest-controversy-tells-us-about-the-future-of-math/"
)
SEP02_DOWNLOAD_URL = (
    "https://www.technologyreview.com/2026/09/02/1143283/"
    "the-download-ai-puzzles-alpha-centauri-mission/"
)
AUG19_DOWNLOAD_URL = (
    "https://www.technologyreview.com/2026/08/19/1140195/"
    "the-download-ai-recursive-self-improvement-problem-heatwave-causes/"
)
JUN05_META_DOWNLOAD_URL = (
    "https://www.technologyreview.com/2026/06/05/1138452/"
    "the-download-ai-hacking-mythos-chatbots-brain-impacts/"
)
AUG06_META_DOWNLOAD_URL = (
    "https://www.technologyreview.com/2026/08/06/1141278/"
    "the-download-google-ai-shake-up-meta-rogue-model/"
)
FACTCHECK_URL = (
    "https://www.technologyreview.com/2025/01/29/1110630/"
    "three-reasons-meta-will-struggle-with-community-fact-checking/"
)

TARGET_SCORES = [-0.25, -0.20, -0.15]
PEER_SCORES = [-0.40, -0.35, -0.55]
TARGET_AVG = -0.20
PEER_AVG = -0.4333
EXPECTED_DELTA = 0.2333

ENGINE_T = 3.5
ENGINE_P = 0.042172
ENGINE_D = 2.8577


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT, *args],
        capture_output=True,
        text=True,
    )


def _profile():
    with open(PROFILE_PATH) as f:
        return yaml.safe_load(f)


def _entity():
    return _profile()["competitor_relationships"]["openai"]


def _mechanism():
    return _entity()[MECH_KEY]


def _read(path):
    with open(os.path.join(REPO_ROOT, path)) as fh:
        return fh.read()


class TestIterationMetadata672:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 672

    def test_type_a(self):
        m = _mechanism()
        assert m["iteration_type"] == "A"
        assert "Type A" in m["type"]

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 637

    def test_mechanism_id_unique_repo_wide(self):
        out = subprocess.run(
            ["grep", "-rn", "mechanism_id: 637", os.path.join(REPO_ROOT, "profiles")],
            capture_output=True,
            text=True,
        )
        hits = [l for l in out.stdout.splitlines() if l.strip()]
        assert len(hits) == 1, "mechanism_id 637 must appear exactly once: %r" % (hits,)

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_pair_names_mittr_openai_meta(self):
        m = _mechanism()
        assert m["pair"] == "MIT Technology Review x OpenAI (vs Meta)"
        assert "MIT TR x OpenAI" in m["finding"]

    def test_iteration_time_sep11_5am(self):
        assert _mechanism()["iteration_time"] == "2026-09-11 05:00 PDT"

    def test_author_kit_with_ray(self):
        assert _mechanism()["author"] == "Kit (with Ray)"


class TestOpenAIEntityStructure672:
    def test_mechanism_nested_under_openai(self):
        ent = _entity()
        assert MECH_KEY in ent
        assert ent[MECH_KEY]["mechanism_id"] == 637

    def test_sibling_financial_metadata_intact(self):
        ent = _entity()
        assert ent["financial_tie"] == "indirect"
        assert ent["coverage_prediction"] == "neutral"
        assert "Prorata" in ent["description"]

    def test_meta_block_untouched(self):
        meta = _profile()["competitor_relationships"]["meta"]
        assert meta["financial_tie"] == "none"
        assert meta["estimated_value"] == "$0"
        assert meta["coverage_prediction"] == "adversarial"

    def test_first_dedicated_type_a_under_openai(self):
        ent = _entity()
        mech_keys = [k for k in ent if k.startswith("mechanism_")]
        assert mech_keys == [MECH_KEY], (
            "openai block held only financial metadata before this run: %r" % (mech_keys,)
        )


class TestToneScorer672:
    def test_scorer_block_methodology_manual(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "MANUAL ILLUSTRATIVE" in s["methodology"]
        assert "DO NOT claim empirical significance" in s["methodology"]

    def test_target_scores_match_openai_tones(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["target_scores_MANUAL_ILLUSTRATIVE"] == TARGET_SCORES
        assert s["target_avg"] == TARGET_AVG

    def test_peer_scores_match_meta_tones(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["peer_scores_MANUAL_ILLUSTRATIVE"] == PEER_SCORES
        assert s["peer_avg"] == PEER_AVG

    def test_delta_arithmetic_exact_4dp(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["delta_manual_illustrative"] == EXPECTED_DELTA
        assert s["delta_manual_illustrative"] == round(TARGET_AVG - PEER_AVG, 4)
        assert abs(s["delta_manual_illustrative"] - (TARGET_AVG - PEER_AVG)) < 1e-4

    def test_yaml_engine_block_matches_pinned_values(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        eng = s["engine_welch_t_3_5000"]
        assert "t=3.5000" in eng
        assert "p=0.042172" in eng
        assert "d=2.8577" in eng
        assert "is_significant True" in eng

    def test_engine_pinned_constants(self):
        assert ENGINE_T == 3.5
        assert ENGINE_P == 0.042172
        assert ENGINE_D == 2.8577
        assert ENGINE_T > 0

    def test_finding_layer_refuses(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        finding = s["finding_layer"]
        assert "NOT_CALCULATED" in finding
        assert "is_significant False" in finding
        assert "EIGHTH DIVERGENCE PIN" in finding
        assert "ratchet 7 -> 8" in finding

    def test_divergence_class_records(self):
        finding = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]["finding_layer"]
        assert "LARGEST" in finding
        assert "0.042172" in finding
        assert "barely under 0.05" in finding
        assert "#642 holds the smallest (0.001213)" in finding
        assert "#602 holds the largest |d| (9.2557)" in finding

    def test_positive_t_sign_means_openai_softer(self):
        # Positive t: target (OpenAI) mean > peer (Meta) mean.
        assert ENGINE_T > 0
        assert TARGET_AVG > PEER_AVG

    def test_convention_stated(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "target-minus-peer" in s["convention"]
        assert "target = OpenAI arm" in s["convention"]

    def test_article_tones_match_scorer_arms(self):
        m = _mechanism()
        openai_tones = [a["manual_illustrative_tone"] for a in m["openai_articles"]]
        meta_tones = [a["manual_illustrative_tone"] for a in m["meta_articles"]]
        assert openai_tones == TARGET_SCORES
        assert meta_tones == PEER_SCORES


class TestRegisterAnalysis672:
    def _openai(self):
        return {a["title"]: a for a in _mechanism()["openai_articles"]}

    def _meta(self):
        return {a["title"]: a for a in _mechanism()["meta_articles"]}

    def test_math_url_verbatim(self):
        a = self._openai()["What OpenAI's latest controversy tells us about the future of math"]
        assert a["url"] == MATH_URL

    def test_math_first_hand_read(self):
        a = self._openai()["What OpenAI's latest controversy tells us about the future of math"]
        assert "first-hand read this run" in a["source_note"]
        assert "all 89 lines" in a["source_note"]
        assert a["date"] == "2026-09-08"

    def test_math_register_accountability_skeptical(self):
        a = self._openai()["What OpenAI's latest controversy tells us about the future of math"]
        assert a["register"] == "accountability_skeptical"
        assert "credit-scooping" in a["key_framing"]
        assert "Hugging Face hack" in a["key_framing"]
        assert a["manual_illustrative_tone"] == -0.25

    def test_math_byline_unattested(self):
        a = self._openai()["What OpenAI's latest controversy tells us about the future of math"]
        assert "byline unattested in fetch" in a["source_note"]

    def test_sep02_download_url_verbatim(self):
        a = self._openai()["The Download: AI puzzles and a path to our nearest star system"]
        assert a["url"] == SEP02_DOWNLOAD_URL
        assert a["date"] == "2026-09-02"

    def test_sep02_register_safety_skeptic_cultural(self):
        a = self._openai()["The Download: AI puzzles and a path to our nearest star system"]
        assert a["register"] == "safety_skeptic_cultural"
        assert "cultural problems" in a["key_framing"]
        assert a["manual_illustrative_tone"] == -0.20

    def test_aug19_download_url_verbatim(self):
        a = self._openai()["The Download: AI's self-improvement problem, and what's driving the heat"]
        assert a["url"] == AUG19_DOWNLOAD_URL
        assert a["date"] == "2026-08-19"
        assert a["register"] == "safety_watch_hype_skeptic"
        assert "spark hype" in a["key_framing"]
        assert a["manual_illustrative_tone"] == -0.15

    def test_download_relay_bounded(self):
        arts = self._openai()
        relay = [arts["The Download: AI puzzles and a path to our nearest star system"],
                 arts["The Download: AI's self-improvement problem, and what's driving the heat"]]
        for a in relay:
            assert "relay bounded" in a["source_note"]
            assert "search-result excerpt" in a["source_note"]

    def test_meta_jun05_carried_from_619(self):
        a = self._meta()["The Download: AI hacking beyond Mythos, and chatbots' impact on our brains"]
        assert a["url"] == JUN05_META_DOWNLOAD_URL
        assert "in-corpus via #619/#642" in a["source_note"]
        assert a["manual_illustrative_tone"] == -0.40

    def test_meta_aug06_download_url_verbatim(self):
        a = self._meta()["The Download: Google's AI shake-up and Meta's rogue model"]
        assert a["url"] == AUG06_META_DOWNLOAD_URL
        assert a["date"] == "2026-08-06"
        assert a["register"] == "agentic_failure_deception"
        assert "Muse Spark 1.1" in a["key_framing"]
        assert "lie to reach their goals" in a["key_framing"]
        assert a["manual_illustrative_tone"] == -0.35

    def test_meta_aug06_new_to_corpus(self):
        a = self._meta()["The Download: Google's AI shake-up and Meta's rogue model"]
        assert "NEW TO CORPUS this run" in a["source_note"]

    def test_meta_factchecking_carried_with_timing_skew(self):
        a = self._meta()["Three reasons Meta will struggle with community fact-checking"]
        assert a["url"] == FACTCHECK_URL
        assert a["date"] == "2025-01-29"
        assert "timing-skew confounder" in a["source_note"]
        assert a["manual_illustrative_tone"] == -0.55

    def test_all_register_urls_https(self):
        m = _mechanism()
        for a in m["openai_articles"] + m["meta_articles"]:
            assert a["url"].startswith("https://"), a["url"]


class TestFinancialContext672:
    def test_predictor_prorata_indirect(self):
        fc = _mechanism()["financial_context"]
        assert "Prorata AI content partner" in fc["mittr_openai"]
        assert "no direct OpenAI licensing deal" in fc["mittr_openai"]

    def test_prediction_neutral_vs_adversarial(self):
        fc = _mechanism()["financial_context"]
        assert "prediction neutral" in fc["mittr_openai"]
        assert "$0" in fc["mittr_meta"]
        assert "prediction adversarial" in fc["mittr_meta"]

    def test_direction_consistent_not_contradicted(self):
        fc = _mechanism()["financial_context"]
        assert fc["direction"].startswith("consistent:")
        assert "-0.20 avg" in fc["direction"]
        assert "-0.4333 avg" in fc["direction"]

    def test_not_falsification_family_member(self):
        fc = _mechanism()["financial_context"]
        assert "NOT a falsification-family member" in fc["status"]
        assert "no named gradient contradicted" in fc["status"]

    def test_no_openai_payer_leg(self):
        fc = _mechanism()["financial_context"]
        assert "not an OpenAI payer leg" in fc["status"]

    def test_correlation_only(self):
        fc = _mechanism()["financial_context"]
        assert "correlation only" in fc["correlation_note"]

    def test_finding_states_not_falsification(self):
        assert "NOT a falsification-family member" in _mechanism()["finding"]


class TestConfounders672:
    def _ranked(self):
        return _mechanism()["confounders_ranked"]

    def test_three_strong_confounders(self):
        assert len(self._ranked()["strong"]) == 3

    def test_event_valence_skew_strong(self):
        strong = self._ranked()["strong"]
        assert any("Event valence skew" in c for c in strong)
        assert any("tracks event badness" in c for c in strong)

    def test_download_relay_genre_strong(self):
        strong = self._ranked()["strong"]
        assert any("Download relay genre" in c for c in strong)

    def test_timing_skew_strong(self):
        strong = self._ranked()["strong"]
        assert any("Timing skew" in c for c in strong)

    def test_three_moderate_confounders(self):
        assert len(self._ranked()["moderate"]) == 3

    def test_byline_unattested_moderate(self):
        moderate = self._ranked()["moderate"]
        assert any("byline unattested" in c for c in moderate)

    def test_prediction_granularity_moderate(self):
        moderate = self._ranked()["moderate"]
        assert any("Prediction granularity coarse" in c for c in moderate)

    def test_news_peg_moderate(self):
        moderate = self._ranked()["moderate"]
        assert any("News-peg" in c for c in moderate)

    def test_two_weak_confounders(self):
        assert len(self._ranked()["weak"]) == 2

    def test_counterevidence_three_items(self):
        ce = _mechanism()["counterevidence"]
        assert len(ce) == 3

    def test_counterevidence_achievement_credit(self):
        ce = _mechanism()["counterevidence"]
        assert any("indisputably impressive" in c for c in ce)

    def test_counterevidence_voluntary_pause(self):
        ce = _mechanism()["counterevidence"]
        assert any("voluntary pauses" in c for c in ce)


class TestNovelty672:
    def test_zero_test_files_pre_commit(self):
        files = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_a_672*.py"))
        assert files == [os.path.join(REPO_ROOT, "tests", TEST_BASENAME)], files

    def test_single_type_a_672_file(self):
        files = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_a_672*.py"))
        assert len(files) == 1

    def test_type_a_672_main_commit_unique_and_anchored(self):
        # Fails pre-commit by design per the #565 followup convention; anchor
        # patched in the followup once the #672 main-commit SHA is known.
        result = _run_git("log", "--format=%H %s")
        assert result.returncode == 0
        mains = [
            line for line in result.stdout.splitlines() if "Type A #672:" in line
        ]
        assert len(mains) == 1, "exactly one Type A #672 main commit: %r" % (mains,)
        anchored = TestRotationCycleGuard672.ANCHORED_SHA
        assert anchored == mains[0].split()[0], (
            "anchor patched in followup per #565 convention"
        )

    def test_no_672_iteration_collision(self):
        text = _read("profiles/mit-tech-review.yaml")
        assert text.count("iteration: 672") == 1

    def test_no_mechanism_638_anywhere(self):
        out = subprocess.run(
            ["grep", "-rn", "mechanism_id: 638", os.path.join(REPO_ROOT, "profiles")],
            capture_output=True,
            text=True,
        )
        assert out.stdout.strip() == "", out.stdout

    def test_distinct_from_619_642(self):
        novelty = _mechanism()["novelty"]
        assert "Distinct from #619" in novelty
        assert "#642" in novelty
        finding = _mechanism()["finding"]
        assert "FIRST dedicated MIT TR x OpenAI Type A mechanism" in finding

    def test_no_zero_coverage_claims(self):
        # iteration-492 rule: absences stated as bounded search-result absences.
        research = _mechanism()["research_method"]
        assert "zero 1143747 / 1143283 / 1140195 / 1141278 hits repo-wide" in research


class TestRotationCycleGuard672:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #672 main-commit SHA is known.
    ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

    @staticmethod
    def _mains():
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        return [s for s in out if re.match(r"^Type [A-E] #\d+:", s)]

    def test_window_668_672_closes_e_to_a(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("A", "672"),
            ("E", "671"),
            ("D", "670"),
            ("C", "669"),
            ("B", "668"),
        ], "rotation window 668-672 wrong: %r" % (observed,)

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["A", "E", "D", "C", "B"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                "rotation broken: %s -> %s is not a valid cycle edge" % (a, b)
            )

    def test_anchor_is_main_commit_patched_in_followup(self):
        result = _run_git("log", "--format=%H %s")
        assert result.returncode == 0
        mains = [
            line for line in result.stdout.splitlines() if "Type A #672:" in line
        ]
        main = mains[0].split()[0] if mains else ""
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )


class TestDocSync672:
    # Fails pre-commit by design per the #565 followup convention; the README
    # stats table refresh, narrative line, and ARCHITECTURE row land in the
    # doc-sync commit.
    def _readme_stats(self):
        path = os.path.join(REPO_ROOT, "README.md")
        with open(path) as fh:
            text = fh.read()
        m = re.search(r"\| Tests \| (\d+) \| Across (\d+) test files \|", text)
        assert m, "README stats table row not found"
        return int(m.group(1)), int(m.group(2))

    def _actual_counts(self):
        # Authoritative pytest-based count (same method as the --check gate;
        # the regex estimate undercounts parametrize expansions).
        out = subprocess.run(
            [sys.executable, "scripts/count_stats.py", "--pytest"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=400,
        )
        m = re.search(r"Total tests\s+(\d+)", out.stdout)
        assert m
        total = int(m.group(1))
        files = len(glob.glob(os.path.join(REPO_ROOT, "tests", "test_*.py")))
        return total, files

    def test_readme_stats_table_fresh(self):
        assert self._readme_stats() == self._actual_counts()

    def test_readme_narrative_line_fresh(self):
        path = os.path.join(REPO_ROOT, "README.md")
        with open(path) as fh:
            text = fh.read()
        m = re.search(r"has \*\*(\d+) tests\*\* across (\d+) test files", text)
        assert m, "README narrative test-count line not found"
        total, files = self._actual_counts()
        assert (int(m.group(1)), int(m.group(2))) == (total, files)

    def test_architecture_row_present(self):
        text = _read("docs/ARCHITECTURE.md")
        assert "test_type_a_672" in text

    def test_iteration_log_entry_672(self):
        text = _read("iteration-log.md")
        assert "#672" in text


class TestNoBrittlePatterns672:
    def test_yaml_reparses_clean(self):
        _profile()

    def test_no_em_dashes_in_mechanism_block(self):
        text = _read("profiles/mit-tech-review.yaml")
        start = text.index(MECH_KEY)
        block = text[start : text.index("  meta:", start)]
        assert "\u2014" not in block, "em dash found in mechanism 637 block"
        assert "\u2013" not in block, "en dash found in mechanism 637 block"

    def test_no_invented_canonical_urls(self):
        m = _mechanism()
        for a in m["openai_articles"] + m["meta_articles"]:
            assert "1143747" in a["url"] or "1143283" in a["url"] or \
                "1140195" in a["url"] or "1141278" in a["url"] or \
                "1138452" in a["url"] or "1110630" in a["url"], (
                "URL must be one of the verbatim attested URLs: %r" % (a["url"],)
            )

    def test_mechanism_key_matches_iteration_numbering(self):
        assert "637" in MECH_KEY
        assert _mechanism()["iteration"] == 672
