"""Type A #1042 (1040-1044 window, third leg D->E->A->B->C): WSJ x OpenAI Sep-27
U.N. rogue-agents adversarial safety-crisis register vs WSJ x Anthropic Sep-24
Akamai business-growth register (mechanism 856).

FIRST dedicated corpus mechanism on the WSJ's Sep 27 2026 OpenAI piece "OpenAI
Agents Used Aggressive Techniques to Access U.N. Website" (wsj.com paywalled;
register read from search-index excerpts per #503; 0 browser.open) vs the WSJ's
Sep 24 2026 Anthropic piece "Anthropic to Pay Akamai Technologies $11.6 Billion
Over Seven Years for Cloud Services". OpenAI arm: n=1, safety-crisis
adversarial incident reportage on the DEAL PARTNER ("rogue AI model",
"extremely worrying fundamental breakdown in AI containment", "borderline
hacking" per Stamos, U.N./Commerce/SEC/Australian-government probing, 53 user
images uploaded externally), MANUAL ILLUSTRATIVE -0.45. Anthropic arm: n=1,
business-growth register ($11.6B/7yr, ~5% Akamai warrant, shares surged 17%),
MANUAL ILLUSTRATIVE +0.10. Illustrative delta (Anthropic minus OpenAI): (0.10)
- (-0.45) = +0.55 - the naive direct-payer-softening prediction
(news-corp.yaml competitor_relationships.openai coverage_prediction 'softer',
from the News Corp-OpenAI May 2024 $50M/yr licensing deal) FAILS on this pair:
the $50M/yr deal partner gets the HARDER register than the settlement-revenue
lab. THIRTY-FOURTH falsification-family member (ledger 33->34); THIRD
safety-crisis falsification (after m598 and m853, both at the Verge) and FIRST
at WSJ/News Corp - cross-publication replication that the licensing deal does
not suppress adversarial safety-crisis coverage of the payer. MANUAL /
qualitative only; engine NOT run on the arms per the Aug 28 2026 standing rule;
p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant False; verdict
directionally_supported_not_proven. Strongest confounders: story-peg mismatch
(safety-crisis vs business deal - the finding is a scope bound, not proof of no
effect); excerpt-bounded evidence. Novelty verified pre-commit (zero
test_type_a_1042 files; no 'Type A #1042' in git log; max numeric mechanism_id
855; zero underscore/dash-form 856 keys by designed keying per #715; block key
zero-hit; both WSJ URLs zero-hit repo-wide); 1040-1044 window third leg
D->E->A->B->C - Sep 27 2026 15:00 PDT.

Test tally: 45 tests, 11 classes.
EXPECTED_TESTS = 45
"""

import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
OWN_BASENAME = os.path.basename(__file__)
MECH_KEY = "wsj_openai_sep27_un_rogue_agents_adversarial_vs_wsj_anthropic_sep24_akamai_growth_register_sep27_3pm"
M_ID = 856
ITER = 1042
TYPE_LETTER = "A"
RUN_PDT = "2026-09-27 15:00 PDT"
# Concatenated per #715 so this file never carries the contiguous literals.
MECH_ID_MARKER = "mechanism" + "_856"  # own-form underscore sweep marker
NEXT_US = "mechanism" + "_857"  # next-number underscore sweep
NEXT_DASH = "mechanism" + "-857"  # next-number dash sweep
NEXT_NUMERIC = "mechanism_id: " + "857"  # next-number numeric sweep
EXPECTED_ORDER = [("A", "1042"), ("E", "1041"), ("D", "1040"), ("C", "1039"), ("B", "1038")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "0" * 40

WSJ_UN_URL = "https://www.wsj.com/tech/ai/openai-agents-used-aggressive-techniques-to-access-u-n-website-522c70ff"
WSJ_AKAMAI_URL = "https://www.wsj.com/tech/anthropic-to-pay-akamai-technologies-11-6-billion-over-seven-years-for-cloud-services-7a55360b"
EXPECTED_URLS = [WSJ_UN_URL, WSJ_AKAMAI_URL]

README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
PROFILE = os.path.join("profiles", "news-corp.yaml")

README_TESTS_BEFORE, README_FILES_BEFORE = 53449, 1366
EXPECTED_TESTS = 45
README_TESTS_AFTER, README_FILES_AFTER = 53449 + EXPECTED_TESTS, 1367

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
    # the next 0-2-space key (meta:) bounds the block.
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
class TestNoveltyAnchorTypeA1042:
    def test_single_test_type_a_1042_file(self):
        files = [
            fn
            for fn in os.listdir(os.path.join(REPO_ROOT, "tests"))
            if fn.startswith("test_type_a_1042")
        ]
        assert files == [OWN_BASENAME]

    def test_anchor_sha_patched_post_commit(self):
        # Deselected pre-commit per #565: ANCHORED_SHA carries a placeholder
        # until the anchor followup patches it to the real main commit SHA.
        # main commit SHA once the followup patches ANCHORED_SHA.
        assert ANCHORED_SHA != "0" * 40
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)
        r = run_git("rev-parse", ANCHORED_SHA)
        assert r.returncode == 0 and r.stdout.strip() == ANCHORED_SHA

    def test_novelty_verification_claim(self):
        doc = __doc__
        for claim in (
            "zero\ntest_type_a_1042 files",
            "max numeric\nmechanism_id\n855",
            "block key\nzero-hit",
            "both WSJ URLs zero-hit",
        ):
            assert claim.replace("\n", " ") in doc.replace("\n", " ")


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1040-1044 window, third leg D->E->A->B->C
# ---------------------------------------------------------------------------
class TestRotationGuard1040_1044Window:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_1040_1044_third_leg(self):
        assert _window() == EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_e_1041(self):
        order = _window()
        assert order[1] == ("E", "1041")
        r = run_git("log", "--grep", "Type E #1041:", "--format=%H", "--no-merges")
        assert r.stdout.strip(), "no Type E #1041 main commit found"

    def test_no_concurrent_inflight_commits_asserted(self):
        r = run_git("log", "--grep", "Type A #1042:", "--format=%H", "--no-merges")
        assert len(r.stdout.split()) == 1, "expected exactly one Type A #1042 main commit"


# ---------------------------------------------------------------------------
# 3. Mechanism 856 block structure
# ---------------------------------------------------------------------------
class TestMechanism856Structure:
    def test_block_key_at_4space_indent_under_openai(self):
        text = _profiles_text()
        assert text.count("    " + MECH_KEY + ":") == 1

    def test_block_key_descriptive_no_856(self):
        # Designed keying per #715: the block key embeds NO 856 literal
        # (numeric, underscore-form, or dash-form).
        assert "856" not in MECH_KEY
        assert MECH_ID_MARKER.replace("+", "") not in MECH_KEY
        assert re.fullmatch(r"[a-z0-9_]+", MECH_KEY)

    def test_iteration_type_time(self):
        m = _mech()
        assert m["mechanism_id"] == M_ID
        assert m["iteration"] == ITER
        assert m["iteration_type"] == TYPE_LETTER
        assert m["type"] == "Type A: Competitor Coverage Deep Dive"
        assert m["time_pdt"] == "15:00"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_publication_pair_entities(self):
        m = _mech()
        assert m["publication"] == "Wall Street Journal (News Corp)"
        assert m["competitor_pair"] == "OpenAI vs Anthropic"

    def test_test_file_and_research_method(self):
        m = _mech()
        assert m["test_file"] == "tests/" + OWN_BASENAME
        assert "0 browser.open" in m["research_method"]
        assert "3 browser.search query sets" in m["research_method"]

    def test_rotation_window_noted(self):
        text = _block()
        assert "1040-1044" in text
        assert "third leg" in text


# ---------------------------------------------------------------------------
# 4. Arms: one fresh OpenAI arm, one fresh Anthropic arm
# ---------------------------------------------------------------------------
class TestMechanism856Arms:
    def test_one_openai_arm_one_anthropic_arm(self):
        m = _mech()
        assert "openai_arm_fresh" in m
        assert "anthropic_arm_fresh" in m
        assert isinstance(m["openai_arm_fresh"], dict)
        assert isinstance(m["anthropic_arm_fresh"], dict)

    def test_openai_arm_metadata(self):
        arm = _mech()["openai_arm_fresh"]
        assert arm["title"] == "OpenAI Agents Used Aggressive Techniques to Access U.N. Website"
        assert arm["date"] == "2026-09-27"
        assert arm["register"] == "safety_crisis_adversarial"
        assert arm["tone_illustrative"] == -0.45
        assert arm["source_url"] == WSJ_UN_URL

    def test_openai_key_language_verbatim(self):
        quotes = _mech()["openai_arm_fresh"]["key_quotes"]
        assert any("rogue AI model" in q for q in quotes)
        assert any("fundamental breakdown in AI containment" in q for q in quotes)
        assert any("borderline" in q and "hacking" in q for q in quotes)
        assert any("Securities and Exchange Commission" in q for q in quotes)

    def test_anthropic_arm_metadata(self):
        arm = _mech()["anthropic_arm_fresh"]
        assert arm["title"] == "Anthropic to Pay Akamai Technologies $11.6 Billion Over Seven Years for Cloud Services"
        assert arm["date"] == "2026-09-24"
        assert arm["register"] == "business_growth"
        assert arm["tone_illustrative"] == 0.10
        assert arm["source_url"] == WSJ_AKAMAI_URL

    def test_anthropic_key_language_verbatim(self):
        quotes = _mech()["anthropic_arm_fresh"]["key_quotes"]
        assert any("11.6 billion" in q for q in quotes)
        assert any("warrant" in q for q in quotes)
        assert any("surged 17%" in q for q in quotes)

    def test_all_source_urls_verbatim(self):
        m = _mech()
        assert m["openai_arm_fresh"]["source_url"] == WSJ_UN_URL
        assert m["anthropic_arm_fresh"]["source_url"] == WSJ_AKAMAI_URL
        assert EXPECTED_URLS == [WSJ_UN_URL, WSJ_AKAMAI_URL]

    def test_zero_browser_open_attested(self):
        text = _block()
        assert "0 browser.open" in text


# ---------------------------------------------------------------------------
# 5. Asymmetry scorer
# ---------------------------------------------------------------------------
class TestMechanism856Scorer:
    def test_illustrative_tones_and_delta(self):
        m = _mech()
        assert m["openai_arm_fresh"]["tone_illustrative"] == -0.45
        assert m["anthropic_arm_fresh"]["tone_illustrative"] == 0.10
        assert m["illustrative_delta_anthropic_minus_openai"] == 0.55

    def test_delta_math(self):
        m = _mech()
        calc = round(
            m["anthropic_arm_fresh"]["tone_illustrative"]
            - m["openai_arm_fresh"]["tone_illustrative"],
            2,
        )
        assert calc == m["illustrative_delta_anthropic_minus_openai"] == 0.55

    def test_third_safety_crisis_falsification_framed(self):
        text = _block()
        assert "THIRD safety-crisis falsification" in text
        assert "m598" in text
        assert "m853" in text
        assert "FIRST at WSJ" in text

    def test_deal_tie_counterdirectional(self):
        text = _block()
        assert "Naive direct-payer-softening prediction" in text
        assert "$50M/yr" in text
        assert "May 2024" in text
        assert "coverage_prediction" in text
        assert "softer" in text

    def test_financial_context_settlement_revenue(self):
        fc = _mech()["financial_context"]
        assert "$50M/yr" in fc["newscorp_openai_deal"]
        assert "Bartz" in fc["newscorp_anthropic_tie"]
        assert "non_causal_language" in fc

    def test_stats_not_calculated(self):
        s = _mech()["statistical_discipline"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"
        assert s["is_significant"] is False


# ---------------------------------------------------------------------------
# 6. Confounders and counterevidence
# ---------------------------------------------------------------------------
class TestMechanism856Confounders:
    def test_confounders_ranked_strong_first(self):
        cs = _mech()["confounding_factors_ranked_strong_first"]
        assert len(cs) == 6
        assert cs[0].startswith("STRONG")
        assert cs[1].startswith("STRONG")
        assert cs[2].startswith("STRONG")
        assert "peg" in cs[0].lower()
        assert "0 browser.open" in cs[2]

    def test_counterevidence_four(self):
        ce = _mech()["counter_evidence"]
        assert len(ce) == 4
        assert any("m532" in c for c in ce)
        assert any("Jul 31" in c for c in ce)
        assert any("m682" in c for c in ce)


# ---------------------------------------------------------------------------
# 7. Statistical discipline
# ---------------------------------------------------------------------------
class TestMechanism856Discipline:
    def test_statistical_discipline_qualitative_only(self):
        d = _mech()["statistical_discipline"]
        assert d["scores"] == "MANUAL ILLUSTRATIVE only"
        assert d["engine_run"] is False
        assert d["is_significant"] is False
        assert d["verdict"] == "directionally_supported_not_proven"

    def test_no_analysis_json_update(self):
        assert _mech()["statistical_discipline"]["no_analysis_json_update"] is True

    def test_not_artifact_grade(self):
        assert _mech()["statistical_discipline"]["artifact_grade"] is False

    def test_falsification_member_thirty_fourth(self):
        m = _mech()
        assert m["falsification_family_member"] is True
        assert m["falsification_ledger"] == 34
        assert "THIRTY-FOURTH falsification-family member" in m["ledger_note"]
        assert "33 -> 34" in m["ledger_note"]

    def test_correlation_not_causation(self):
        text = _block()
        assert "Correlation does not establish causation" in text

    def test_connects_to(self):
        assert _mech()["connects_to"] == [532, 598, 616, 682, 733, 846, 853]

    def test_falsification_member_distinct_from_absent_guards(self):
        # Member-form wording per #1000, distinct from the "absent" guards in
        # other profiles (which carry "NOT a falsification-family member").
        # Appears twice in this block: summary + ledger_note.
        text = _profiles_text()
        assert "THIRTY-FOURTH falsification-family member" in text
        assert text.count("THIRTY-FOURTH falsification-family member") == 2


# ---------------------------------------------------------------------------
# 8. Corpus novelty post-commit
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPostCommit:
    def test_max_numeric_mechanism_id_is_856(self):
        ids = _corpus_ids()
        assert max(ids) == M_ID

    def test_zero_next_numeric_857_in_profiles(self):
        text = "\n".join(
            _read(os.path.join(root, fn))
            for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles"))
            for fn in files
            if fn.endswith(".yaml")
        )
        assert NEXT_NUMERIC not in text

    def test_zero_next_underscore_dash_857_repo_wide(self):
        assert _repo_grep(NEXT_US) == []
        assert _repo_grep(NEXT_DASH) == []


# ---------------------------------------------------------------------------
# 9. Doc-sync ratchet per #719 (green post-doc-sync)
# ---------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_header_stats_bumped(self):
        text = _read("README.md")
        assert str(README_TESTS_AFTER) in text
        assert str(README_FILES_AFTER) in text

    def test_readme_row_1042(self):
        text = _read("README.md")
        assert f"`tests/{OWN_BASENAME}`" in text
        assert "Type A #1042" in text

    def test_architecture_row(self):
        text = _read("docs/ARCHITECTURE.md")
        assert OWN_BASENAME in text

    def test_iteration_log_entry(self):
        text = _read("iteration-log.md")
        assert "## #1042 Type A:" in text


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


assert EXPECTED_TESTS == 45
