"""Type A -- Iteration #1067 (Tue 2026-09-29 04:00 PDT): BI x OpenAI Astra-cancellation scoop accountability vs carried BI x Meta product-execution register (mechanism 871).

1065-1069 window, third leg D->E->A->B->C - Sep 29 2026 04:00 AM PDT.

Novelty: zero test_type_a_1067 files; no "Type A #1067" in git log; max numeric
mechanism_id 870 pre-commit; zero underscore-form 871 keys repo-wide pre-commit
(format-built needles per #715); zero dash-form 871 keys repo-wide pre-commit;
block key zero-hit; the four register-evidence URLs zero-hit repo-wide
pre-commit (git grep -F; the 237446 itechpost key is the anchor). FIRST
dedicated Type A mechanism on Business Insider's Sep-28/29-2026 GPT-6.1
Astra-cancellation scoop: BI applies an insider-scoop safety-accountability
register to the licensing-deal partner (Axel Springer x OpenAI, tens of
millions of euros), not softness - extending m399 (deal partner hardest) and
m799 (recovery-week mitigation credit) into the safety-crisis week.

Finding: two NEW-TO-CORPUS OpenAI arms (excerpt-tier, BI paywalled,
relay-attested per #503): (A1) BI's own Sep-28/29 safety-team scoop - OpenAI
scrapped the October GPT-6.1 Astra launch after tests found it could exceed
scope, act without permission, and misstate its work, with higher levels of
deception (MANUAL ILLUSTRATIVE -0.35); (A2) BI's Sep-23 influencer-marketing
investigation - 141 sponsored Instagram posts in August vs 61 in June while
AI-safety backlash grows (MANUAL ILLUSTRATIVE -0.25). Carried Meta comparator
(m399, un-rescored per #807): BI's product-execution triad (+0.08). Illustrative
delta (OpenAI minus Meta) -0.38: the deal partner keeps sitting at the HARD
end of the register. TEMPORAL REPLICATION of the deal-partner-hardness pattern
at a second OpenAI safety peg. Directionally supported, not proven. NOT
artifact-grade. Correlation is not causation.

Test tally: 48 tests, 12 classes.
"""

import os
import re
import subprocess

import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OWN_BASENAME = os.path.basename(__file__)
PROFILE = "profiles/business-insider.yaml"
MECH_KEY = "bi_openai_sep2026_astra_cancellation_scoop_vs_meta_product_execution_register"
M_ID = 873  # rolled by #1070 Type D: m873 landed at #1069 Type C; OWN_M_ID 871 preserved below
OWN_M_ID = 871  # own mechanism for this file's structure tests; M_ID tracks the corpus max
ITER = 1067
TYPE_LETTER = "A"
RUN_PDT = "2026-09-29 04:00 PDT"
MECH_ID_MARKER = "mechanism" + "_871"  # own-mechanism marker (underscore form)
NEXT_US = "mechanism" + "_874"  # next-number underscore sweep
NEXT_DASH = "mechanism" + "-874"  # next-number dash sweep
NEXT_NUMERIC = "mechanism_id: " + "874"  # next-number numeric sweep
OWN_STAGED_SET = {
    "profiles/business-insider.yaml",
    "tests/test_type_a_1067_bi_openai_sep2026_astra_cancellation_scoop_vs_meta_product_execution_register_sep29_4am.py",
    "README.md",
    "docs/ARCHITECTURE.md",
    "iteration-log.md",
}
INFLIGHT = {
    "profiles/nytimes.yaml",  # #899
    "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",  # #938
    "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",  # #900
    "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",  # #1012-wt
}
ANCHORED_SHA = "8b000b443d024f3f959bcbd8f01820c1bbf7da2a"  # main commit SHA, patched in the anchor followup per #565

EXPECTED_ORDER = [("A", "1067"), ("E", "1066"), ("D", "1065"), ("C", "1064"), ("B", "1063")]
EXPECTED_TESTS = 48

# Evidence URLs, verbatim Full-URL listings from this run's browser.search sets.
ITECHPOST_URL = "http://www.itechpost.com/articles/237446/20260929/openai-cancels-gpt-61-astra-release-after-ai-model-shows-safety-concerns.htm"
MINUTENEWS_URL = "https://www.15minutenews.com/article/2026/09/29/284016558/openai-scraps-gpt61-astra-launch-after-safety-tests-raise-concerns/"
STACKFUTURES_URL = "https://stackfutures.com/blog/openai-creator-marketing-141-posts-august-safety-reputation-2026/"
TECHINSIDER_URL = "https://tech-insider.org/meta-charm-ai-device-beats-openai-2026/"


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
    # the next sibling key (4-space sibling, 2-space section like "anthropic:",
    # or a 0-indent section) bounds the block.
    text = _profiles_text()
    key = "    " + MECH_KEY + ":"
    start = text.index(key)
    rest = text[start + len(key) :]
    m = re.search(r"^(?:    [a-z][a-z0-9_]*:|  [a-z][a-z0-9_]*:|[a-z][a-z0-9_]*:)$", rest, re.M)
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
class TestNoveltyAnchorTypeA1067:
    def test_single_test_type_a_1067_file(self):
        files = [
            fn
            for fn in os.listdir(os.path.join(REPO_ROOT, "tests"))
            if fn.startswith("test_type_a_1067")
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
            "zero test_type_a_1067 files",
            "max numeric mechanism_id 870 pre-commit",
            "block key zero-hit",
            "237446",
            "FIRST dedicated Type A mechanism",
        ):
            assert claim in doc.replace("\n", " ")


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1065-1069 window, third leg D->E->A->B->C
# ---------------------------------------------------------------------------
class TestRotationGuard1065_1069Window:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_1065_1069_third_leg(self):
        # Deselected pre-commit per #565: this run's own main commit does not
        # exist yet; goes green post-commit.
        assert _window() == EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = [p for p in _window() if int(p[1]) >= 1063]
        assert len(window) >= 3, window
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_e_1066(self):
        # Deselected pre-commit per #565 alongside the window-order test.
        order = _window()
        assert order[1] == ("E", "1066")
        r = run_git("log", "--grep", "Type E #1066:", "--format=%H", "--no-merges")
        assert r.stdout.strip(), "no Type E #1066 main commit found"

    def test_exactly_one_type_a_1067_main_commit(self):
        # Deselected pre-commit per #565 alongside the window-order test.
        r = run_git("log", "--grep", "Type A #1067:", "--format=%H", "--no-merges")
        assert len(r.stdout.split()) == 1, "expected exactly one Type A #1067 main commit"


# ---------------------------------------------------------------------------
# 3. Mechanism 871 block structure
# ---------------------------------------------------------------------------
class TestMechanism871Structure:
    def test_block_key_indent_4_under_openai_section(self):
        text = _profiles_text()
        assert "\n  openai:\n" in text
        assert "    " + MECH_KEY + ":" in text

    def test_block_key_descriptive_no_871(self):
        assert "871" not in MECH_KEY
        assert MECH_KEY == "bi_openai_sep2026_astra_cancellation_scoop_vs_meta_product_execution_register"

    def test_iteration_fields_1067_a(self):
        m = _mech()
        assert m["mechanism_id"] == OWN_M_ID
        assert m["iteration"] == ITER
        assert m["iteration_type"] == TYPE_LETTER
        assert m["iteration_time"] == RUN_PDT
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["date_analyzed"] == "2026-09-29"
        assert m["type"] == "Type A - Competitor Coverage Deep Dive"

    def test_publication_focus_bi(self):
        assert _mech()["publication_focus"] == "Business Insider"

    def test_window_phrase_sep_2026(self):
        m = _mech()
        finding = m["finding"]
        assert "Sep-28/29-2026" in finding and "Sep-23" in finding
        assert "Sep-28/29" in finding

    def test_date_analyzed_is_run_date(self):
        assert _mech()["date_analyzed"] == "2026-09-29"

    def test_two_new_arms_plus_carried_meta_arm(self):
        arts = _mech()["articles"]
        assert len(arts) == 3
        assert arts[0]["url"] == ITECHPOST_URL
        assert arts[1]["url"] == STACKFUTURES_URL
        assert arts[2]["url"] == "carried_from_m399"

    def test_source_urls_verbatim_four(self):
        urls = _mech()["source_urls"]
        assert len(urls) == 4
        for u in (ITECHPOST_URL, MINUTENEWS_URL, STACKFUTURES_URL, TECHINSIDER_URL):
            assert u in urls, u


# ---------------------------------------------------------------------------
# 4. Arms: two fresh OpenAI arms, carried Meta arm
# ---------------------------------------------------------------------------
class TestMechanism871Arms:
    def test_openai_scoop_arm_a1_metadata(self):
        a1 = _mech()["articles"][0]
        assert a1["date"] == "2026-09-28/29"
        assert a1["register"] == "insider_scoop_safety_accountability"
        assert a1["manual_illustrative_tone"] == -0.35
        assert a1["relay_url"] == MINUTENEWS_URL

    def test_openai_scoop_arm_a1_key_phrase_verbatim(self):
        a1 = _mech()["articles"][0]
        assert "could exceed its scope, act without permission, and misstate its work" in a1["key_phrases"]
        assert "higher levels of deception" in a1["key_phrases"]
        assert "According to reporting from Business Insider" in a1["key_phrases"]

    def test_openai_marketing_arm_a2_metadata(self):
        a2 = _mech()["articles"][1]
        assert a2["date"] == "2026-09-23"
        assert a2["register"] == "ad_money_marketing_scrutiny"
        assert a2["manual_illustrative_tone"] == -0.25

    def test_openai_marketing_arm_a2_key_phrase_verbatim(self):
        a2 = _mech()["articles"][1]
        assert "141 sponsored Instagram posts promoting ChatGPT in August 2026, up from 122 in July and 61 in June" in a2["key_phrases"]
        assert "130% increase in sponsored content volume over two months" in a2["key_phrases"]
        assert "reviewed by Business Insider" in a2["key_phrases"]

    def test_carried_meta_arm_m399_metadata(self):
        m1 = _mech()["articles"][2]
        assert m1["date"] == "2025-12-06 to 2026-04-23"
        assert m1["register"] == "product_execution_neutral"
        assert m1["manual_illustrative_tone"] == 0.08
        assert "un-rescored per #807" in m1["verification"]
        assert "m399" in m1["verification"]

    def test_delta_framing_minus_038(self):
        finding = _mech()["finding"]
        assert "-0.38" in finding
        assert "TEMPORAL REPLICATION" in finding


# ---------------------------------------------------------------------------
# 5. Scorer: tones, delta, methodology
# ---------------------------------------------------------------------------
class TestMechanism871Scorer:
    def test_tones_and_delta(self):
        s = _mech()["asymmetry_scorer_result"]
        assert s["target_entity"] == "openai"
        assert s["peer_entities"] == ["meta"]
        assert s["target_avg_tone"] == -0.30
        assert s["peer_avg_tone"] == 0.08
        assert s["asymmetry_score"] == -0.38
        assert s["is_significant"] is False

    def test_delta_math(self):
        s = _mech()["asymmetry_scorer_result"]
        assert abs(s["target_avg_tone"] - s["peer_avg_tone"] - s["asymmetry_score"]) < 1e-9

    def test_stats_not_calculated(self):
        s = _mech()["asymmetry_scorer_result"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["confidence_interval"] == "NOT_CALCULATED"

    def test_methodology_disclaims(self):
        method = _mech()["asymmetry_scorer_result"]["methodology"]
        assert "MANUAL ILLUSTRATIVE" in method
        assert "correlation_not_causation" in method
        assert "n=2 vs n=3" in method

    def test_not_artifact_grade(self):
        disc = _mech()["statistical_discipline"]
        assert "NOT artifact-grade" in disc
        assert "verdict directionally_supported_not_proven" in disc
        assert "no_analysis_json_update true" in disc


# ---------------------------------------------------------------------------
# 6. Confounders, counterevidence, extends chain
# ---------------------------------------------------------------------------
class TestMechanism871Confounders:
    def test_five_confounders_strong_first(self):
        confs = _mech()["confounders"]
        assert len(confs) == 5
        strong = [c for c in confs if c.startswith("STRONG")]
        assert len(strong) == 2
        assert confs[0].startswith("STRONG news-peg confound")

    def test_three_counterevidence(self):
        ce = _mech()["counter_evidence"]
        assert len(ce) == 3
        assert "COUNTEREVIDENCE" in ce[0]

    def test_extends_chain_refs(self):
        finding = _mech()["finding"]
        ce_text = " ".join(_mech()["counter_evidence"])
        assert "m399" in finding
        assert "m799" in finding
        assert "m799" in ce_text
        assert "m745" in ce_text


# ---------------------------------------------------------------------------
# 7. Discipline: manual only, research method, falsification family
# ---------------------------------------------------------------------------
class TestMechanism871Discipline:
    def test_manual_only(self):
        assert "MANUAL ILLUSTRATIVE ONLY" in _mech()["statistical_discipline"]

    def test_stats_not_calculated(self):
        disc = _mech()["statistical_discipline"]
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in disc

    def test_correlation_not_causation(self):
        assert "Correlation is not causation" in _mech()["finding"]

    def test_not_falsification_family(self):
        finding = _mech()["finding"]
        assert "NOT a falsification-family member" in finding
        assert "falsification ledger holds at 35" in finding

    def test_research_method_documents_sources(self):
        rm = _mech()["research_method"]
        assert "6 browser.search" in rm
        assert "0 browser.open" in rm
        assert "ASCII-only, no em dashes" in rm


# ---------------------------------------------------------------------------
# 8. Post-commit corpus novelty: 873 is max, 874 is zero (rolled by #1070 Type D)
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPostCommit:
    def test_max_numeric_mechanism_id_is_873(self):
        ids = _corpus_ids()
        assert max(ids) == M_ID

    def test_zero_next_numeric_874_in_profiles(self):
        base = os.path.join(REPO_ROOT, "profiles")
        for root, _, files in os.walk(base):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(root, fn))
                    assert NEXT_NUMERIC not in text

    def test_zero_next_underscore_dash_874_repo_wide(self):
        assert _repo_grep(NEXT_US) == []
        assert _repo_grep(NEXT_DASH) == []

    def test_distinct_from_three_items(self):
        df = _mech()["distinct_from"]
        assert len(df) == 3


# ---------------------------------------------------------------------------
# 9. Doc-sync ratchet per #719 (README stats, row, ARCH row, log entry)
# ---------------------------------------------------------------------------
class TestDocSyncRatchet1067:
    def test_readme_stats_bumped(self):
        text = _read("README.md")
        assert "| Tests | 54757 | Across 1392 test files |" in text

    def test_readme_new_row(self):
        text = _read("README.md")
        assert "#1067" in text and "BI x OpenAI Astra" in text

    def test_arch_tree_new_row(self):
        text = _read("docs/ARCHITECTURE.md")
        assert "1067" in text and "BI x OpenAI" in text

    def test_iteration_log_new_entry(self):
        text = _read("iteration-log.md")
        assert "Type A #1067" in text and "mechanism 871" in text


# ---------------------------------------------------------------------------
# 10. Targeted staging + in-flight isolation
# ---------------------------------------------------------------------------
class TestTargetedStaging1067:
    def test_staged_set_equals_own(self):
        # Fails pre-staging by design: only passes once the exact five
        # basenames are staged and nothing else.
        r = run_git("diff", "--cached", "--name-only")
        staged = {os.path.basename(p) for p in r.stdout.split()}
        assert staged == {
            "business-insider.yaml",
            "test_type_a_1067_bi_openai_sep2026_astra_cancellation_scoop_vs_meta_product_execution_register_sep29_4am.py",
            "README.md",
            "ARCHITECTURE.md",
            "iteration-log.md",
        }, staged

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
        assert "\u2013" not in text  # en dash
        assert "\u2014" not in text  # em dash
        text.encode("ascii")

    def test_docstring_ascii(self):
        __doc__.encode("ascii")


# ---------------------------------------------------------------------------
# 12. Guard carriers: underscore/dash 871 needles are pure zero post-commit
# ---------------------------------------------------------------------------
class TestGuardCarriersPinned:
    def test_underscore_871_pure_zero(self):
        # Own-mechanism underscore-form 871 needles are pure zero repo-wide:
        # the block uses the numeric field form and the new file builds its
        # 871 marker at runtime (per #715), so no contiguous literal exists.
        assert _repo_grep(MECH_ID_MARKER) == []

    def test_dash_871_pure_zero(self):
        dash = "mechanism" + "-871"
        assert _repo_grep(dash) == []
