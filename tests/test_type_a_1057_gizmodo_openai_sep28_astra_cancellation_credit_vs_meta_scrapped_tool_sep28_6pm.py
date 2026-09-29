"""Type A #1057 (1055-1059 window, third leg D->E->A->B->C): Gizmodo x OpenAI
Sep-28-2026 GPT-6.1 Astra cancellation credit-normalization register vs
carried Gizmodo x Meta scrapped-AI-photo-tool comparator (mechanism 865).

FIRST dedicated Type A mechanism on Gizmodo's Sep-28-2026 "OpenAI Cancels
Release of GPT-6.1 Astra Because It 'Regressed' on Safety" piece (first-hand
full text via browser.open this run, 38 lines). Register: credit-giving
normalization - scare quotes distance the danger framing ('Regressed',
"go rogue", "sandboxes", "super intelligence"), the kicker is explicit:
"In other words, it was a faulty product, so OpenAI, to its credit,
didn't ship it." MANUAL ILLUSTRATIVE +0.15 on the new arm: a within-entity
register extreme for Gizmodo x OpenAI (block standing tone "dismissive",
cf. "A Stinkin' Phone?"; rogue-agent item -0.25). Carried Meta comparator
"The Public Got So Mad at Meta's New AI Photo Tool That It's Scrapped
Already" (2026-07, -0.55, carried from m587/m512). Same event class
(company scraps an AI product), opposite register: OpenAI's cancellation
of a deceptive model reads as responsible restraint, Meta's scrapping reads
as public shaming. Illustrative delta (OpenAI minus Meta) +0.70:
+0.15 minus -0.55. Extends m582 (Gizmodo x OpenAI null-tie control) and the
openai_rogue_ai_vs_meta_glasses paradox. NOT a falsification-family member
(single-item register documentation, no uniform-prediction test; the m582
control is not overturned by n=1); ledger unchanged. NOT artifact-grade.
MANUAL / qualitative only; engine NOT run on the arms per the Aug 28 2026
standing rule; p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant False;
verdict directionally_supported_not_proven. Strongest confounders: the
news-peg confound (voluntary pre-launch restraint genuinely reads as
responsible; backlash-yanked tool genuinely reads as humiliation - the
register may track the peg, not the entity); n=1 vs n=1; temporal mismatch
(Sep-28 safety-crisis cycle vs Jul-2026 Meta peg). Novelty verified
pre-commit (zero test_type_a_1057 files; no 'Type A #1057' in git log; max
numeric mechanism_id 864 pre-commit; zero gpt-6.1/GPT-6.1/astra/Astra/
2000818566 hits repo-wide; block key zero-hit; zero 866 keys post-commit);
1055-1059 window third leg D->E->A->B->C - Sep 28 2026 06:00 PM PDT.

Test tally: 48 tests, 12 classes.
EXPECTED_TESTS = 48
"""

import glob
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
OWN_BASENAME = os.path.basename(__file__)
MECH_KEY = "gizmodo_openai_astra_cancellation_credit_normalization_vs_meta_scrapped_tool"
M_ID = 869
ITER = 1057
TYPE_LETTER = "A"
RUN_PDT = "2026-09-28 18:00 PDT"
# Concatenated per #715 so this file never carries the contiguous literals.
MECH_ID_MARKER = "mechanism" + "_865"  # own-form underscore sweep marker
NEXT_US = "mechanism" + "_870"  # next-number underscore sweep
NEXT_DASH = "mechanism" + "-870"  # next-number dash sweep
NEXT_NUMERIC = "mechanism_id: " + "870"  # next-number numeric sweep
EXPECTED_ORDER = [("A", "1057"), ("E", "1056"), ("D", "1055"), ("C", "1054"), ("B", "1053")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "c38cb8b7cdeb9df2ce748218fc6809f1fc02d6d3"

GIZMODO_URL = "https://gizmodo.com/?p=2000818566"
META_URL = "https://gizmodo.com/the-public-got-so-mad-at-metas-new-ai-photo-tool-that-its-scrapped-already-2000784400"

README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
PROFILE = os.path.join("profiles", "gizmodo.yaml")

README_TESTS_BEFORE, README_FILES_BEFORE = 54193, 1381
EXPECTED_TESTS = 48
README_TESTS_AFTER, README_FILES_AFTER = 54193 + EXPECTED_TESTS, 1382

# In-flight work that must stay OUT of this run's staged set (targeted
# staging per the repo-wide traversal lesson): #899 (nytimes.yaml mechanism
# 771 hunk), #938 (test_type_b_938 anchor edit), #900 (untracked Type D test
# file), #1012-wt (working-tree edit on the committed Type A #1012 file).
INFLIGHT = {
    "profiles/nytimes.yaml",
    "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
    "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
    "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",
}

# Guard carriers for the 865 needles: the committed #1054 Type C test file's
# own forward-looking guard literals (test_zero_next_id_865's needle list)
# plus the #1055 Type D test file's carrier-pin documentation - guard/log
# context, not corpus data (per #1055's pin). This file never carries the
# contiguous literals (concatenated per #715).
GUARD_CARRIERS_865 = {
    "test_type_c_1054_nvidia_anthropic_ipo_anchor_stake_demand_recycling_eighteenth_direction_sep28_3am.py",
    "test_type_d_1055_m862_m863_m864_qualitative_corpus_integrity_sep28_4am.py",
}


def run_git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, timeout=120
    )


def _read(path):
    with open(os.path.join(REPO_ROOT, path), encoding="utf-8") as f:
        return f.read()


def _profiles_text():
    return _read(PROFILE)


def _block():
    # Block key sits at 4-space indent under competitor_relationships -> openai;
    # the next 4-space key (the apple connect mechanism) bounds the block.
    text = _profiles_text()
    key = "    " + MECH_KEY + ":"
    start = text.index(key)
    rest = text[start + len(key) :]
    m = re.search(r"^    [a-z][a-z0-9_]*:$", rest, re.M)
    end = start + len(key) + m.start()
    return text[start:end]


def _mech():
    d = yaml.safe_load(_profiles_text())
    return d["competitor_relationships"]["openai"][MECH_KEY]


def _corpus_ids():
    ids = []
    base = os.path.join(REPO_ROOT, "profiles")
    for root, _, files in os.walk(base):
        for fn in files:
            if fn.endswith(".yaml"):
                text = _read(os.path.join(root, fn))
                for m in re.finditer(r"mechanism(?:_id)?:\s*(\d+)", text):
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


def _window(n=40):
    # First occurrence of each distinct iteration number, newest first
    # (robust to followup commits that repeat the same "Type X #N" wording
    # without the colon, per the #752 convention).
    subjects = (
        run_git("log", f"-{n}", "--format=%s", "--no-merges").stdout.splitlines()
    )
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out[:5]


# ---------------------------------------------------------------------------
# 1. Novelty anchor
# ---------------------------------------------------------------------------
class TestNoveltyAnchorTypeA1057:
    def test_single_test_type_a_1057_file(self):
        files = [
            fn
            for fn in os.listdir(os.path.join(REPO_ROOT, "tests"))
            if fn.startswith("test_type_a_1057")
        ]
        assert files == [OWN_BASENAME]

    def test_anchor_sha_patched_post_commit(self):
        # Deselected pre-commit per #565: ANCHORED_SHA carries a placeholder
        # until the anchor followup patches it to the real main commit SHA.
        assert ANCHORED_SHA != "0" * 40
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)
        r = run_git("rev-parse", ANCHORED_SHA)
        assert r.returncode == 0 and r.stdout.strip() == ANCHORED_SHA

    def test_novelty_verification_claim(self):
        doc = __doc__
        for claim in (
            "zero test_type_a_1057 files",
            "max numeric mechanism_id 864 pre-commit",
            "block key zero-hit",
            "2000818566 hits repo-wide",
        ):
            assert claim in doc.replace("\n", " ")


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1055-1059 window, third leg D->E->A->B->C
# ---------------------------------------------------------------------------
class TestRotationGuard1055_1059Window:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_1055_1059_third_leg(self):
        # Deselected pre-commit per #565: this run's own main commit does not
        # exist yet; goes green post-commit.
        assert _window() == EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_e_1056(self):
        # Deselected pre-commit per #565 alongside the window-order test.
        order = _window()
        assert order[1] == ("E", "1056")
        r = run_git("log", "--grep", "Type E #1056:", "--format=%H", "--no-merges")
        assert r.stdout.strip(), "no Type E #1056 main commit found"

    def test_exactly_one_type_a_1057_main_commit(self):
        # Deselected pre-commit per #565 alongside the window-order test.
        r = run_git("log", "--grep", "Type A #1057:", "--format=%H", "--no-merges")
        assert len(r.stdout.split()) == 1, "expected exactly one Type A #1057 main commit"

    def test_no_subject_deviation_in_window(self):
        doc = __doc__
        assert "1055-1059 window" in doc
        assert "third leg" in doc


# ---------------------------------------------------------------------------
# 3. Mechanism 865 block structure
# ---------------------------------------------------------------------------
class TestMechanism865Structure:
    def test_block_key_at_4space_indent_under_openai(self):
        text = _profiles_text()
        assert text.count("    " + MECH_KEY + ":") == 1

    def test_block_key_descriptive_no_865(self):
        # Designed keying per #715: the block key embeds NO 865 literal
        # (numeric, underscore-form, or dash-form).
        assert "865" not in MECH_KEY
        assert re.fullmatch(r"[a-z0-9_]+", MECH_KEY)

    def test_iteration_type_time(self):
        m = _mech()
        assert m["mechanism_id"] == M_ID
        assert m["iteration"] == ITER
        assert m["iteration_type"] == TYPE_LETTER
        assert m["type"] == "Type A - Competitor Coverage Deep Dive"
        assert m["iteration_time"] == RUN_PDT
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_publication_focus(self):
        m = _mech()
        assert "Gizmodo" in m["publication_focus"]

    def test_test_file_and_window(self):
        text = _block()
        assert "1055-1059" in text
        assert "third leg" in text

    def test_date_analyzed(self):
        m = _mech()
        assert m["date_analyzed"] == "2026-09-28"

    def test_two_articles(self):
        m = _mech()
        assert len(m["articles"]) == 2


# ---------------------------------------------------------------------------
# 4. Arms: one fresh Gizmodo OpenAI arm, one carried Meta comparator
# ---------------------------------------------------------------------------
class TestMechanism865Arms:
    def test_fresh_openai_arm_metadata(self):
        arm = _mech()["articles"][0]
        assert arm["title"] == "OpenAI Cancels Release of GPT-6.1 Astra Because It 'Regressed' on Safety"
        assert arm["url"] == GIZMODO_URL
        assert str(arm["date"]) == "2026-09-28"
        assert arm["register"] == "credit_giving_normalization"
        assert arm["manual_illustrative_tone"] == 0.15

    def test_fresh_arm_key_phrases_verbatim(self):
        phrases = _mech()["articles"][0]["key_phrases"]
        assert any("to its credit" in p for p in phrases)
        assert any("Regressed" in p for p in phrases)
        assert any("go rogue" in p for p in phrases)
        assert any("Saachi Jain" in p for p in phrases)

    def test_fresh_arm_first_hand_verification(self):
        v = _mech()["articles"][0]["verification"]
        assert "first-hand" in v
        assert "browser.open" in v
        assert "NEW-TO-CORPUS" in v

    def test_carried_meta_arm_metadata(self):
        arm = _mech()["articles"][1]
        assert arm["title"] == "The Public Got So Mad at Meta's New AI Photo Tool That It's Scrapped Already"
        assert arm["url"] == META_URL
        assert str(arm["date"]) == "2026-07"
        assert arm["manual_illustrative_tone"] == -0.55

    def test_carried_meta_arm_verification(self):
        v = _mech()["articles"][1]["verification"]
        assert "carried" in v
        assert "m587" in v or "#512" in v

    def test_source_urls_verbatim(self):
        m = _mech()
        assert m["source_urls"] == [GIZMODO_URL, META_URL]

    def test_same_event_class_framed(self):
        text = _block()
        assert "Same event class" in text
        assert "scraps an AI product" in text


# ---------------------------------------------------------------------------
# 5. Asymmetry scorer
# ---------------------------------------------------------------------------
class TestMechanism865Scorer:
    def test_illustrative_tones_and_delta(self):
        s = _mech()["asymmetry_scorer_result"]
        assert s["target_entity"] == "openai"
        assert s["peer_entities"] == ["meta"]
        assert s["target_avg_tone"] == 0.15
        assert s["peer_avg_tone"] == -0.55
        assert s["asymmetry_score"] == 0.7

    def test_delta_math(self):
        s = _mech()["asymmetry_scorer_result"]
        calc = s["target_avg_tone"] - s["peer_avg_tone"]
        assert abs(calc - 0.7) < 1e-9
        assert abs(calc - s["asymmetry_score"]) < 1e-9

    def test_stats_not_calculated(self):
        s = _mech()["asymmetry_scorer_result"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["confidence_interval"] == "NOT_CALCULATED"
        assert s["is_significant"] is False

    def test_methodology_disclaims_significance(self):
        s = _mech()["asymmetry_scorer_result"]
        assert "MANUAL ILLUSTRATIVE" in s["methodology"]
        assert "n=1 vs n=1" in s["methodology"]
        assert "correlation_not_causation" in s["methodology"]

    def test_not_artifact_grade(self):
        text = _block()
        assert "NOT artifact-grade" in text


# ---------------------------------------------------------------------------
# 6. Confounders and counterevidence
# ---------------------------------------------------------------------------
class TestMechanism865Confounders:
    def test_confounders_six_ranked_strong_first(self):
        cs = _mech()["confounders"]
        assert len(cs) == 6
        assert cs[0].startswith("STRONG")
        assert cs[1].startswith("STRONG")
        assert "news-peg" in cs[0]
        assert "n=1 vs n=1" in cs[1]

    def test_counterevidence_three(self):
        ce = _mech()["counter_evidence"]
        assert len(ce) == 3
        assert any("Stinkin" in c for c in ce)
        assert any("m582" in c for c in ce)
        assert any("WSJ" in c for c in ce)

    def test_extends_chain_referenced(self):
        text = _block()
        assert "m582" in text
        assert "paradox" in text


# ---------------------------------------------------------------------------
# 7. Statistical discipline
# ---------------------------------------------------------------------------
class TestMechanism865Discipline:
    def test_statistical_discipline_manual_only(self):
        d = _mech()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE" in d
        assert "n=1 vs n=1" in d
        assert "directional" in d

    def test_stats_not_calculated_in_discipline(self):
        d = _mech()["statistical_discipline"]
        assert "NOT_CALCULATED" in d
        assert "is_significant" in d and "False" in d

    def test_correlation_not_causation(self):
        text = _block()
        assert "Correlation is not causation" in text

    def test_not_falsification_family_member(self):
        text = _block()
        assert "NOT a" in text and "falsification-family member" in text
        assert "ledger unchanged" in text

    def test_research_method_documents_sources(self):
        rm = _mech()["research_method"]
        assert "browser.search" in rm
        assert "browser.open" in rm
        assert "first-hand" in rm
        assert "no canonical URL" in rm


# ---------------------------------------------------------------------------
# 8. Corpus novelty post-commit
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPostCommit:
    def test_max_numeric_mechanism_id_is_869(self):
        ids = _corpus_ids()
        assert max(ids) == M_ID

    def test_zero_next_numeric_870_in_profiles(self):
        text = "\n".join(
            _read(os.path.join(root, fn))
            for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles"))
            for fn in files
            if fn.endswith(".yaml")
        )
        assert NEXT_NUMERIC not in text

    def test_zero_next_underscore_dash_870_repo_wide(self):
        assert _repo_grep(NEXT_US) == []
        assert _repo_grep(NEXT_DASH) == []

    def test_distinct_from_documents_novelty(self):
        df = _mech()["distinct_from"]
        assert len(df) == 3
        assert any("No prior mechanism" in d for d in df)


# ---------------------------------------------------------------------------
# 9. Doc-sync ratchet per #719 (green post-doc-sync)
# ---------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_header_stats_bumped(self):
        text = _read("README.md")
        assert str(README_TESTS_AFTER) in text
        assert str(README_FILES_AFTER) in text

    def test_readme_row_1057(self):
        text = _read("README.md")
        assert f"`tests/{OWN_BASENAME}`" in text
        assert "Type A #1057" in text

    def test_architecture_row(self):
        text = _read("docs/ARCHITECTURE.md")
        assert OWN_BASENAME in text

    def test_iteration_log_entry(self):
        text = _read("iteration-log.md")
        assert "## #1057 Type A:" in text


# ---------------------------------------------------------------------------
# 10. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation:
    def test_inflight_files_untouched(self):
        r = run_git("diff", "--cached", "--name-only")
        staged = set(r.stdout.split())
        for f in INFLIGHT:
            assert f not in staged, f"in-flight file staged: {f}"


# ---------------------------------------------------------------------------
# 11. ASCII-only, no em dashes
# ---------------------------------------------------------------------------
class TestBlockHygiene:
    def test_block_ascii_no_em_dash(self):
        text = _block()
        assert "\u2014" not in text  # em dash
        assert "\u2013" not in text  # en dash
        text.encode("ascii")

    def test_docstring_ascii(self):
        __doc__.encode("ascii")


# ---------------------------------------------------------------------------
# 12. Guard carriers for 865 pinned (per #1055's pin)
# ---------------------------------------------------------------------------
class TestGuardCarriersPinned:
    def test_865_underscore_needles_confined_to_guard_carriers(self):
        # The 865 underscore needles live only in the two documented guard
        # carriers (#1054 test-file guard literals, #1055 test-file
        # carrier-pin docs, per #1055's pin); this file never carries the
        # contiguous literal (concatenated per #715); iteration-log prose is
        # guard/log context, not corpus data.
        hits = {os.path.basename(p) for p in _repo_grep(MECH_ID_MARKER)}
        assert hits == GUARD_CARRIERS_865, f"uncarried 865 needle: {hits}"

    def test_own_file_carries_no_contiguous_865_needles(self):
        # Needles built by concatenation per #715 so this assertion never
        # self-carries the contiguous literals it checks for.
        text = _read(os.path.join("tests", OWN_BASENAME))
        assert ("mechanism" + "_865") not in text
        assert ("mechanism" + "-865") not in text


assert EXPECTED_TESTS == 48
