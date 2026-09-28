"""Type A #1052 (1050-1054 window, third leg D->E->A->B->C): Guardian x OpenAI
Sep-26-2026 AP-wire training-halt register vs carried Meta arms (mechanism 862).

FIRST dedicated Type A mechanism on the Guardian's Sep-26-2026 AP-wire
training-halt piece (Guardian-published, Associated Press, Sat 26 Sep 2026
21.10 EDT; excerpt-bounded via Guardian-attributed mirror, 0 browser.open this
turn per #503). Register: incident-accountability safety-crisis via wire relay -
the Guardian runs the verbatim "going rogue" headline on its Feb-2025
licensing partner during the safety-crisis escalation. MANUAL ILLUSTRATIVE
-0.35 on the new arm: the HARDEST Guardian OpenAI arm yet (vs -0.15 Aug-18
m537, -0.10 Milmo m517, -0.25 Sep-17 m760); still softer than the carried Meta
mean (-0.50, m687 arms). With the new arm the OpenAI mean moves -0.1667 ->
-0.2125 against the carried Meta mean -0.50, so the illustrative gap narrows
(delta magnitude 0.333 -> 0.2875) without closing. Within-entity temporal
hardening: -0.15 (Aug-18) -> -0.25 (Sep-17) -> -0.35 (Sep-26). The register
follows the PEG (safety-crisis escalation), not the entity - the m842/m736
cross-publication pattern holds at the Guardian. Directionally CONSISTENT with
the standing softer coverage_prediction, so NOT a falsification-family member
(ledger holds at 35). NOT artifact-grade. MANUAL / qualitative only; engine NOT
run on the arms per the Aug 28 2026 standing rule; p_value/cohens_d/ci_95
NOT_CALCULATED; is_significant False; verdict directionally_supported_not_proven.
Strongest confounders: excerpt-bounded wire mirror (0 browser.open per #503);
wire-relay register (AP desk, not a Guardian original); temporal skew
(Sep-26 safety-crisis peak vs Aug/Sep Meta pegs). Novelty verified pre-commit
(zero test_type_a_1052 files; no 'Type A #1052' in git log; max numeric
mechanism_id 861; zero underscore-form 862 keys in profiles/ - test-file guard
literals in #1049/#1050 files excluded as carriers per #715; zero dash-form
862 references outside guard carriers; zero numeric 862 keys in profiles/;
block key zero-hit; wesearch.press mirror URL zero-hit repo-wide; headline
string zero-hit repo-wide); 1050-1054 window third leg D->E->A->B->C - Sep 28
2026 01:00 PDT.

Test tally: 53 tests, 12 classes.
EXPECTED_TESTS = 53
"""

import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
OWN_BASENAME = os.path.basename(__file__)
MECH_KEY = "guardian_openai_sep26_ap_wire_training_halt_rogue_register_vs_carried_meta_arms"
M_ID = 862
ITER = 1052
TYPE_LETTER = "A"
RUN_PDT = "2026-09-28 01:00 PDT"
# Concatenated per #715 so this file never carries the contiguous literals.
MECH_ID_MARKER = "mechanism" + "_862"  # own-form underscore sweep marker
NEXT_US = "mechanism" + "_863"  # next-number underscore sweep
NEXT_DASH = "mechanism" + "-863"  # next-number dash sweep
NEXT_NUMERIC = "mechanism_id: " + "863"  # next-number numeric sweep
EXPECTED_ORDER = [("A", "1052"), ("E", "1051"), ("D", "1050"), ("C", "1049"), ("B", "1048")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "9862438823bd9d714584f7413b82f75d4c5a79c0"

WESEARCH_URL = "https://wesearch.press/s/openai-halts-training-of-latest-models-as-reports-mount-of-a-a9516e1c"
EXPECTED_URLS = [WESEARCH_URL]

README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
PROFILE = os.path.join("profiles", "guardian.yaml")

README_TESTS_BEFORE, README_FILES_BEFORE = 53931, 1376
EXPECTED_TESTS = 53
README_TESTS_AFTER, README_FILES_AFTER = 53931 + EXPECTED_TESTS, 1377

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

# Guard carriers for the 862 needles: the #1049 Type C test file's own guard
# literals, the #1050 Type D test file's carrier-pin docs, this file's own
# __pycache__ artifact (compiled after the run), plus iteration-log prose -
# guard/log context, not corpus data (per #1050's pin).
GUARD_CARRIERS_862 = {
    "tests/test_type_c_1049_google_ft_feb2026_second_payer_leg_bundled_leverage_seventeenth_direction_sep27_10pm.py",
    "tests/test_type_d_1050_m859_m860_m861_qualitative_corpus_integrity_sep27_11pm.py",
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
    # the next 2-space key (meta:) bounds the block.
    text = _profiles_text()
    key = "    " + MECH_KEY + ":"
    start = text.index(key)
    rest = text[start + len(key) :]
    m = re.search(r"^ {0,2}[a-z][a-z0-9_]*:$", rest, re.M)
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
class TestNoveltyAnchorTypeA1052:
    def test_single_test_type_a_1052_file(self):
        files = [
            fn
            for fn in os.listdir(os.path.join(REPO_ROOT, "tests"))
            if fn.startswith("test_type_a_1052")
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
            "zero\ntest_type_a_1052 files",
            "max numeric\nmechanism_id\n861",
            "block key\nzero-hit",
            "wesearch.press mirror URL zero-hit",
        ):
            assert claim.replace("\n", " ") in doc.replace("\n", " ")


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1050-1054 window, third leg D->E->A->B->C
# ---------------------------------------------------------------------------
class TestRotationGuard1050_1054Window:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_1050_1054_third_leg(self):
        # Deselected pre-commit per #565: this run's own main commit does not
        # exist yet; goes green post-commit.
        assert _window() == EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_e_1051(self):
        # Deselected pre-commit per #565 alongside the window-order test.
        order = _window()
        assert order[1] == ("E", "1051")
        r = run_git("log", "--grep", "Type E #1051:", "--format=%H", "--no-merges")
        assert r.stdout.strip(), "no Type E #1051 main commit found"

    def test_exactly_one_type_a_1052_main_commit(self):
        # Deselected pre-commit per #565 alongside the window-order test.
        r = run_git("log", "--grep", "Type A #1052:", "--format=%H", "--no-merges")
        assert len(r.stdout.split()) == 1, "expected exactly one Type A #1052 main commit"

    def test_no_subject_deviation_in_window(self):
        # The 1050-1054 window has a clean subject convention (per #1051's
        # note: "no subject deviation touches this window").
        doc = __doc__
        assert "1050-1054 window" in doc
        assert "third leg" in doc


# ---------------------------------------------------------------------------
# 3. Mechanism 862 block structure
# ---------------------------------------------------------------------------
class TestMechanism862Structure:
    def test_block_key_at_4space_indent_under_openai(self):
        text = _profiles_text()
        assert text.count("    " + MECH_KEY + ":") == 1

    def test_block_key_descriptive_no_862(self):
        # Designed keying per #715: the block key embeds NO 862 literal
        # (numeric, underscore-form, or dash-form).
        assert "862" not in MECH_KEY
        assert MECH_ID_MARKER.replace("+", "") not in MECH_KEY
        assert re.fullmatch(r"[a-z0-9_]+", MECH_KEY)

    def test_iteration_type_time(self):
        m = _mech()
        assert m["mechanism_id"] == M_ID
        assert m["iteration"] == ITER
        assert m["iteration_type"] == TYPE_LETTER
        assert m["type"] == "Type A - Competitor Coverage Deep Dive"
        assert m["time_pdt"] == "01:00"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_publication_pair_entities(self):
        m = _mech()
        assert m["publication"] == "The Guardian"
        assert m["publication_slug"] == "guardian"
        assert m["competitor_pair"] == "OpenAI (Feb 2025 licensing partner) vs Meta ($0 deal)"

    def test_test_file_and_research_method(self):
        m = _mech()
        assert m["test_file"] == "tests/" + OWN_BASENAME
        assert "0 browser.open" in m["research_method"]
        assert "2 browser.search query sets" in m["research_method"]

    def test_rotation_window_noted(self):
        text = _block()
        assert "1050-1054" in text
        assert "third leg" in text

    def test_author_and_date(self):
        m = _mech()
        assert m["author"] == "Kit (with Ray)"
        assert m["date"] == "2026-09-28"

    def test_publication_focus(self):
        m = _mech()
        assert m["publication_focus"] == "The Guardian"


# ---------------------------------------------------------------------------
# 4. Arms: one fresh Guardian OpenAI arm, carried comparators
# ---------------------------------------------------------------------------
class TestMechanism862Arms:
    def test_fresh_openai_arm_structure(self):
        m = _mech()
        assert "openai_arm_fresh" in m
        assert isinstance(m["openai_arm_fresh"], dict)

    def test_fresh_arm_metadata(self):
        arm = _mech()["openai_arm_fresh"]
        assert arm["date"] == "2026-09-26"
        assert arm["register"] == "safety_crisis_accountability_wire_relay"
        assert arm["tone_illustrative"] == -0.35
        assert arm["source_url"] == WESEARCH_URL
        assert "0 browser.open" in arm["evidence_bound"]

    def test_fresh_arm_key_language_verbatim(self):
        quotes = _mech()["openai_arm_fresh"]["key_quotes"]
        assert any("going rogue" in q for q in quotes)
        assert any("halts training of latest models" in q for q in quotes)
        assert any("acted in unexpected ways" in q for q in quotes)

    def test_fresh_arm_ap_attribution(self):
        arm = _mech()["openai_arm_fresh"]
        assert "Associated Press" in arm["byline_attribution"]
        assert "26 Sep 2026" in arm["byline_attribution"]

    def test_carried_openai_arms_three(self):
        carried = _mech()["openai_arm_carried"]
        assert len(carried) == 3
        assert any("537" in c and "-0.15" in c for c in carried)
        assert any("517" in c and "-0.10" in c for c in carried)
        assert any("760" in c and "-0.25" in c for c in carried)

    def test_carried_meta_arms_two(self):
        carried = _mech()["meta_arm_carried"]
        assert len(carried) == 2
        assert any("687" in c and "-0.45" in c for c in carried)
        assert any("687" in c and "-0.55" in c for c in carried)
        assert _mech()["meta_mean"] == -0.50

    def test_openai_mean_with_fresh(self):
        assert _mech()["openai_mean_with_fresh"] == -0.2125

    def test_all_source_urls_verbatim(self):
        m = _mech()
        assert m["openai_arm_fresh"]["source_url"] == WESEARCH_URL
        assert EXPECTED_URLS == [WESEARCH_URL]


# ---------------------------------------------------------------------------
# 5. Asymmetry scorer
# ---------------------------------------------------------------------------
class TestMechanism862Scorer:
    def test_illustrative_tones_and_delta(self):
        m = _mech()
        assert m["openai_arm_fresh"]["tone_illustrative"] == -0.35
        assert m["illustrative_delta_openai_minus_meta"] == 0.29

    def test_delta_math(self):
        m = _mech()
        calc = round(m["openai_mean_with_fresh"] - m["meta_mean"], 2)
        assert calc == m["illustrative_delta_openai_minus_meta"] == 0.29

    def test_gap_narrows_without_closing(self):
        text = _block()
        assert "0.375" in text
        assert "0.333" in text
        assert "0.2875" in text
        assert "narrows" in text
        assert "without closing" in text

    def test_within_entity_hardening(self):
        text = _block()
        assert "-0.15" in text and "-0.25" in text and "-0.35" in text
        assert "register follows the PEG" in text

    def test_deal_tie_directional_not_falsification(self):
        text = _block()
        assert "coverage_prediction" in text
        assert "softer" in text
        assert "Directionally" in text and "CONSISTENT" in text
        assert "NOT a falsification-family member" in text

    def test_methodology_disclaims_significance(self):
        m = _mech()
        assert "DO NOT claim empirical significance" in m["methodology"]
        assert m["methodology"].count("carried") >= 1
        assert "scored_arm false" in m["methodology"]


# ---------------------------------------------------------------------------
# 6. Confounders and counterevidence
# ---------------------------------------------------------------------------
class TestMechanism862Confounders:
    def test_confounders_ranked_strong_first(self):
        cs = _mech()["confounding_factors_ranked_strong_first"]
        assert len(cs) == 6
        assert cs[0].startswith("STRONG")
        assert cs[1].startswith("STRONG")
        assert cs[2].startswith("STRONG")
        assert "0 browser.open" in cs[0]
        assert "wire" in cs[1].lower()

    def test_counterevidence_four(self):
        ce = _mech()["counter_evidence"]
        assert len(ce) == 4
        assert any("HARDEST" in c for c in ce)
        assert any("Register" in c for c in ce)
        assert any("Medicare" in c for c in ce)
        assert any("687" in c for c in ce)

    def test_peer_pole_context(self):
        text = _block()
        assert "The Register" in text
        assert "OpenAI-speak" in text

    def test_incentive_attribution_inconclusive(self):
        assert _mech()["incentive_attribution"].startswith("INCONCLUSIVE")


# ---------------------------------------------------------------------------
# 7. Statistical discipline
# ---------------------------------------------------------------------------
class TestMechanism862Discipline:
    def test_statistical_discipline_qualitative_only(self):
        d = _mech()["statistical_discipline"]
        assert d["scores"] == "MANUAL ILLUSTRATIVE only"
        assert d["engine_run"] is False
        assert d["is_significant"] is False
        assert d["verdict"] == "directionally_supported_not_proven"

    def test_stats_not_calculated(self):
        d = _mech()["statistical_discipline"]
        assert d["p_value"] == "NOT_CALCULATED"
        assert d["cohens_d"] == "NOT_CALCULATED"
        assert d["ci_95"] == "NOT_CALCULATED"

    def test_no_analysis_json_update(self):
        assert _mech()["statistical_discipline"]["no_analysis_json_update"] is True

    def test_not_artifact_grade(self):
        assert _mech()["statistical_discipline"]["artifact_grade"] is False

    def test_falsification_not_a_member_ledger_35(self):
        m = _mech()
        assert m["falsification_family_member"] is False
        assert m["falsification_ledger"] == 35
        assert "ledger holds at 35" in m["ledger_note"]

    def test_correlation_not_causation(self):
        text = _block()
        assert "Correlation does not establish causation" in text

    def test_connects_to(self):
        assert _mech()["connects_to"] == [687, 760, 537, 517]


# ---------------------------------------------------------------------------
# 8. Corpus novelty post-commit
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPostCommit:
    def test_max_numeric_mechanism_id_is_862(self):
        ids = _corpus_ids()
        assert max(ids) == M_ID

    def test_zero_next_numeric_863_in_profiles(self):
        text = "\n".join(
            _read(os.path.join(root, fn))
            for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles"))
            for fn in files
            if fn.endswith(".yaml")
        )
        assert NEXT_NUMERIC not in text

    def test_zero_next_underscore_dash_863_repo_wide(self):
        assert _repo_grep(NEXT_US) == []
        assert _repo_grep(NEXT_DASH) == []

    def test_extends_chain_referenced(self):
        text = _block()
        assert "mechanism 760" in text
        assert "m687" in text


# ---------------------------------------------------------------------------
# 9. Doc-sync ratchet per #719 (green post-doc-sync)
# ---------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_header_stats_bumped(self):
        text = _read("README.md")
        assert str(README_TESTS_AFTER) in text
        assert str(README_FILES_AFTER) in text

    def test_readme_row_1052(self):
        text = _read("README.md")
        assert f"`tests/{OWN_BASENAME}`" in text
        assert "Type A #1052" in text

    def test_architecture_row(self):
        text = _read("docs/ARCHITECTURE.md")
        assert OWN_BASENAME in text

    def test_iteration_log_entry(self):
        text = _read("iteration-log.md")
        assert "## #1052 Type A:" in text


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
        assert "—" not in text  # em dash
        assert "–" not in text  # en dash
        text.encode("ascii")

    def test_docstring_ascii(self):
        __doc__.encode("ascii")


# ---------------------------------------------------------------------------
# 12. Guard carriers for 862 pinned (per #1050's pin)
# ---------------------------------------------------------------------------
class TestGuardCarriersPinned:
    def test_862_needles_confined_to_guard_carriers(self):
        # The 862 underscore needles live only in the two documented guard
        # carriers (#1049 test-file guard literals, #1050 test-file
        # carrier-pin docs, per #1050's pin); this file never carries the
        # contiguous literal (concatenated per #715); iteration-log prose is
        # guard/log context, not corpus data.
        hits = set(_repo_grep(MECH_ID_MARKER))
        assert hits == GUARD_CARRIERS_862, f"uncarried 862 needle: {hits}"


assert EXPECTED_TESTS == 53
