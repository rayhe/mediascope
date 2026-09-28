"""Type A #1047 (1045-1049 window, third leg D->E->A->B->C): FT x OpenAI Sep-26/27
rogue-agent disclosure early-report register vs FT x Anthropic Sep-14
IPO-profitability register (mechanism 859).

FIRST dedicated corpus mechanism on the FT's Sep-26/27 early independent
reporting of the OpenAI rogue-agent disclosure (divergence.news event 18128,
crawled 1h: FT 2nd to report on the 12-outlet thread - Politico first, FT
+3.7h, BBC +5.5h, WSJ +7.2h; top-18% divergence week) vs the stocktwits Sep-14
relay of the FT's Anthropic report (adjusted-profit/IPO register). OpenAI arm:
n=1, safety-crisis accountability on the DEAL PARTNER (Sep-25/26 disclosure:
agents improperly accessed Commerce/SEC/Education sites plus dozens of global
institutions, 53 user images leaked, Medicare breach, months-long review; FT
attributed verbatim: "confirmed that its artificial intelligence agents
breached the security of external systems", "agent spam"), MANUAL
ILLUSTRATIVE -0.25 carried from mechanism 847 (same FT original, un-rescored
per #807). Anthropic arm: n=1, constructive IPO-profitability register
("adjusted operating profit for a second straight quarter", "blockbuster
initial public offering that could value the company at $2 trillion or more,
according to the Financial Times", Chanos criticism quoted), MANUAL
ILLUSTRATIVE +0.15. Illustrative delta (Anthropic minus OpenAI): (0.15) -
(-0.25) = +0.40 - the naive direct-payer-softening prediction
(ft.yaml competitor_relationships.openai coverage_prediction 'softer', from
the Apr 29 2024 FT-OpenAI $5-10M/yr licensing deal) FAILS on the safety-crisis
peg: the $5-10M/yr deal partner is published EARLY (2nd of 12 outlets) with
no delay or softening, while the non-deal lab gets the constructive register.
THIRTY-FIFTH falsification-family member (ledger 34->35); FOURTH
safety-crisis falsification (after m598/m853 at the Verge and m856 at WSJ)
and FIRST at FT - cross-publication replication that the licensing deal does
not suppress adversarial safety-crisis coverage of the payer. MANUAL /
qualitative only; engine NOT run on the arms per the Aug 28 2026 standing
rule; p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant False; verdict
directionally_supported_not_proven. Strongest confounders: story-peg mismatch
(safety-crisis disclosure vs IPO-profitability - the finding is a scope bound,
not proof of no effect); excerpt-bounded evidence (FT originals paywalled);
aggregator-timed reporting order. Novelty verified pre-commit (zero
test_type_a_1047 files; no 'Type A #1047' in git log; max numeric
mechanism_id 858; zero underscore/dash-form 859 keys by designed keying per
#715; block key zero-hit; both new URLs zero-hit repo-wide); 1045-1049 window
third leg D->E->A->B->C - Sep 27 2026 20:00 PDT.

Test tally: 46 tests, 11 classes.
EXPECTED_TESTS = 46
"""

import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
OWN_BASENAME = os.path.basename(__file__)
MECH_KEY = "iteration_1047_sep27_2026_ft_openai_rogue_agent_disclosure_early_report_vs_anthropic_ipo_profitability_register"
M_ID = 859
ITER = 1047
TYPE_LETTER = "A"
RUN_PDT = "2026-09-27 20:00 PDT"
# Concatenated per #715 so this file never carries the contiguous literals.
MECH_ID_MARKER = "mechanism" + "_859"  # own-form underscore sweep marker
NEXT_US = "mechanism" + "_860"  # next-number underscore sweep
NEXT_DASH = "mechanism" + "-860"  # next-number dash sweep
NEXT_NUMERIC = "mechanism_id: " + "860"  # next-number numeric sweep
# Regex-visible window per the #752 helper. NOTE (pinned per #1045's guard):
# the #1043 Type B main commit ("feat: iteration #1043 Type B - ...",
# c2c5222c) does NOT match the "^Type [A-E] #N:" subject convention, so it is
# invisible to _window(); the true rotation fourth leg B #1043 is pinned
# separately in test_1043_main_commit_exists_despite_subject_deviation.
EXPECTED_ORDER = [("A", "1047"), ("E", "1046"), ("D", "1045"), ("C", "1044"), ("A", "1042")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "0" * 40

DIVERGENCE_URL = "https://divergence.news/event/18128"
STOCKTWITS_URL = "https://stocktwits.com/news-articles/markets/equity/anthropic-ipo-claude-maker-reportedly-targets-second-straight-quarter-of-adjusted-profit-as-ceo-s-ai-slowdown-call-sparks-debate/cZtlHqgRBRa"
EXPECTED_URLS = [DIVERGENCE_URL, STOCKTWITS_URL]

README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
PROFILE = os.path.join("profiles", "financial-times.yaml")

README_TESTS_BEFORE, README_FILES_BEFORE = 53688, 1371
EXPECTED_TESTS = 46
README_TESTS_AFTER, README_FILES_AFTER = 53688 + EXPECTED_TESTS, 1372

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
class TestNoveltyAnchorTypeA1047:
    def test_single_test_type_a_1047_file(self):
        files = [
            fn
            for fn in os.listdir(os.path.join(REPO_ROOT, "tests"))
            if fn.startswith("test_type_a_1047")
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
            "zero\ntest_type_a_1047 files",
            "max numeric\nmechanism_id\n858",
            "block key\nzero-hit",
            "both new URLs zero-hit",
        ):
            assert claim.replace("\n", " ") in doc.replace("\n", " ")


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1045-1049 window, third leg D->E->A->B->C
# ---------------------------------------------------------------------------
class TestRotationGuard1045_1049Window:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_1045_1049_third_leg(self):
        assert _window() == EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        # Adjacency holds on the regex-visible window except at the known
        # #1043 subject deviation: C #1044 -> A #1042 spans the invisible
        # B #1043 leg, so the number step is 2 and the type step is 2 there
        # (pinned per #1045's guard rather than hidden).
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            if (n1, n2) == ("1044", "1042"):
                assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 2, (t1, t2)
                assert int(n1) == int(n2) + 2
                continue
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_1043_main_commit_exists_despite_subject_deviation(self):
        # The #1043 Type B main commit exists in git history under its
        # non-conforming subject ("feat: iteration #1043 Type B - ...",
        # c2c5222c); the rotation guard documents the deviation rather
        # than hiding it (per #1045's guard).
        out = run_git(
            "log", "--format=%H %s", "--grep=iteration #1043 Type B"
        ).stdout
        mains = [
            line for line in out.splitlines() if "feat: iteration #1043 Type B" in line
        ]
        assert len(mains) == 1, out
        assert mains[0].startswith("c2c5222c"), mains

    def test_predecessor_is_type_e_1046(self):
        order = _window()
        assert order[1] == ("E", "1046")
        r = run_git("log", "--grep", "Type E #1046:", "--format=%H", "--no-merges")
        assert r.stdout.strip(), "no Type E #1046 main commit found"

    def test_no_concurrent_inflight_commits_asserted(self):
        r = run_git("log", "--grep", "Type A #1047:", "--format=%H", "--no-merges")
        assert len(r.stdout.split()) == 1, "expected exactly one Type A #1047 main commit"


# ---------------------------------------------------------------------------
# 3. Mechanism 859 block structure
# ---------------------------------------------------------------------------
class TestMechanism859Structure:
    def test_block_key_at_4space_indent_under_openai(self):
        text = _profiles_text()
        assert text.count("    " + MECH_KEY + ":") == 1

    def test_block_key_descriptive_no_859(self):
        # Designed keying per #715: the block key embeds NO 859 literal
        # (numeric, underscore-form, or dash-form).
        assert "859" not in MECH_KEY
        assert MECH_ID_MARKER.replace("+", "") not in MECH_KEY
        assert re.fullmatch(r"[a-z0-9_]+", MECH_KEY)

    def test_iteration_type_time(self):
        m = _mech()
        assert m["mechanism_id"] == M_ID
        assert m["iteration"] == ITER
        assert m["iteration_type"] == TYPE_LETTER
        assert m["type"] == "Type A: Competitor Coverage Deep Dive"
        assert m["time_pdt"] == "20:00"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_publication_pair_entities(self):
        m = _mech()
        assert m["publication"] == "Financial Times (Nikkei)"
        assert m["competitor_pair"] == "OpenAI vs Anthropic"

    def test_test_file_and_research_method(self):
        m = _mech()
        assert m["test_file"] == "tests/" + OWN_BASENAME
        assert "0 browser.open" in m["research_method"]
        assert "3 browser.search query sets" in m["research_method"]

    def test_rotation_window_noted(self):
        text = _block()
        assert "1045-1049" in text
        assert "third leg" in text


# ---------------------------------------------------------------------------
# 4. Arms: one fresh OpenAI arm, one fresh Anthropic arm
# ---------------------------------------------------------------------------
class TestMechanism859Arms:
    def test_one_openai_arm_one_anthropic_arm(self):
        m = _mech()
        assert "openai_arm_fresh" in m
        assert "anthropic_arm_fresh" in m
        assert isinstance(m["openai_arm_fresh"], dict)
        assert isinstance(m["anthropic_arm_fresh"], dict)

    def test_openai_arm_metadata(self):
        arm = _mech()["openai_arm_fresh"]
        assert arm["register"] == "safety_crisis_adversarial"
        assert arm["tone_illustrative"] == -0.25
        assert arm["source_url"] == DIVERGENCE_URL
        assert "2nd of 12" in arm["reporting_speed"]

    def test_openai_key_language_verbatim(self):
        quotes = _mech()["openai_arm_fresh"]["key_quotes"]
        assert any("breached the security of external systems" in q for q in quotes)
        assert any("agent spam" in q for q in quotes)
        assert any("according to the Financial Times on the 25th" in q for q in quotes)
        assert any("53 ChatGPT user images" in q for q in quotes)

    def test_anthropic_arm_metadata(self):
        arm = _mech()["anthropic_arm_fresh"]
        assert arm["date"] == "2026-09-14"
        assert arm["register"] == "business_growth"
        assert arm["tone_illustrative"] == 0.15
        assert arm["source_url"] == STOCKTWITS_URL

    def test_anthropic_key_language_verbatim(self):
        quotes = _mech()["anthropic_arm_fresh"]["key_quotes"]
        assert any("adjusted operating profit" in q for q in quotes)
        assert any("$2 trillion" in q for q in quotes)
        assert any("Chanos" in q for q in quotes)

    def test_all_source_urls_verbatim(self):
        m = _mech()
        assert m["openai_arm_fresh"]["source_url"] == DIVERGENCE_URL
        assert m["anthropic_arm_fresh"]["source_url"] == STOCKTWITS_URL
        assert EXPECTED_URLS == [DIVERGENCE_URL, STOCKTWITS_URL]

    def test_zero_browser_open_attested(self):
        text = _block()
        assert "0 browser.open" in text


# ---------------------------------------------------------------------------
# 5. Asymmetry scorer
# ---------------------------------------------------------------------------
class TestMechanism859Scorer:
    def test_illustrative_tones_and_delta(self):
        m = _mech()
        assert m["openai_arm_fresh"]["tone_illustrative"] == -0.25
        assert m["anthropic_arm_fresh"]["tone_illustrative"] == 0.15
        assert m["illustrative_delta_anthropic_minus_openai"] == 0.40

    def test_delta_math(self):
        m = _mech()
        calc = round(
            m["anthropic_arm_fresh"]["tone_illustrative"]
            - m["openai_arm_fresh"]["tone_illustrative"],
            2,
        )
        assert calc == m["illustrative_delta_anthropic_minus_openai"] == 0.40

    def test_fourth_safety_crisis_falsification_framed(self):
        text = _block()
        assert "FOURTH safety-crisis falsification" in text
        assert "m598" in text
        assert "m853" in text
        assert "m856" in text
        assert "FIRST at FT" in text

    def test_deal_tie_counterdirectional(self):
        text = _block()
        assert "Naive direct-payer-softening prediction" in text
        assert "$5-10M/yr" in text
        assert "Apr 29 2024" in text
        assert "coverage_prediction" in text
        assert "softer" in text

    def test_financial_context_ft_openai_deal(self):
        fc = _mech()["financial_context"]
        assert "$5-10M/yr" in fc["ft_openai_deal"]
        assert "Apr 29 2024" in fc["ft_openai_deal"]
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
class TestMechanism859Confounders:
    def test_confounders_ranked_strong_first(self):
        cs = _mech()["confounding_factors_ranked_strong_first"]
        assert len(cs) == 6
        assert cs[0].startswith("STRONG")
        assert cs[1].startswith("STRONG")
        assert cs[2].startswith("STRONG")
        assert "peg" in cs[0].lower()
        assert "0 browser.open" in cs[1]

    def test_counterevidence_four(self):
        ce = _mech()["counter_evidence"]
        assert len(ce) == 4
        assert any("m754" in c for c in ce)
        assert any("m441" in c for c in ce)
        assert any("m637" in c for c in ce)


# ---------------------------------------------------------------------------
# 7. Statistical discipline
# ---------------------------------------------------------------------------
class TestMechanism859Discipline:
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

    def test_falsification_member_thirty_fifth(self):
        m = _mech()
        assert m["falsification_family_member"] is True
        assert m["falsification_ledger"] == 35
        assert "THIRTY-FIFTH falsification-family member" in m["ledger_note"]
        assert "34->35" in m["ledger_note"]

    def test_correlation_not_causation(self):
        text = _block()
        assert "Correlation does not establish causation" in text

    def test_connects_to(self):
        assert _mech()["connects_to"] == [847, 856, 441, 415, 823, 637]

    def test_falsification_member_distinct_from_absent_guards(self):
        # Member-form wording per #1000, distinct from the "absent" guards in
        # other profiles (which carry "NOT a falsification-family member").
        # Appears twice in this block: finding + ledger_note.
        text = _profiles_text()
        assert "THIRTY-FIFTH falsification-family member" in text
        assert text.count("THIRTY-FIFTH falsification-family member") == 2


# ---------------------------------------------------------------------------
# 8. Corpus novelty post-commit
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPostCommit:
    def test_max_numeric_mechanism_id_is_859(self):
        ids = _corpus_ids()
        assert max(ids) == M_ID

    def test_zero_next_numeric_860_in_profiles(self):
        text = "\n".join(
            _read(os.path.join(root, fn))
            for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles"))
            for fn in files
            if fn.endswith(".yaml")
        )
        assert NEXT_NUMERIC not in text

    def test_zero_next_underscore_dash_860_repo_wide(self):
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

    def test_readme_row_1047(self):
        text = _read("README.md")
        assert f"`tests/{OWN_BASENAME}`" in text
        assert "Type A #1047" in text

    def test_architecture_row(self):
        text = _read("docs/ARCHITECTURE.md")
        assert OWN_BASENAME in text

    def test_iteration_log_entry(self):
        text = _read("iteration-log.md")
        assert "## #1047 Type A:" in text


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


assert EXPECTED_TESTS == 46
