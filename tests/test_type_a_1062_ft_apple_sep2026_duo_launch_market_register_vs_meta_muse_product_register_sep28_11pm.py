"""Type A -- Iteration #1062 (Mon 2026-09-28 23:00 PDT): FT x Apple Duo-launch market register vs carried FT x Meta Muse product register (mechanism 868).

1060-1064 window, third leg D->E->A->B->C - Sep 28 2026 11:00 PM PDT.

Novelty: zero test_type_a_1062 files; no "Type A #1062" in git log; max numeric
mechanism_id 867 pre-commit; zero underscore-form 868 keys repo-wide pre-commit
(format-built needles per #715); zero dash-form 868 keys repo-wide pre-commit;
block key zero-hit; the three register-evidence URLs zero-hit repo-wide
pre-commit (git grep -F; the 3344dc31 llmgram key is the anchor). FIRST
dedicated Type A mechanism under
competitor_relationships.apple in profiles/financial-times.yaml (the apple
section held only the financial stub: financial_tie none, $0, prediction
neutral).

Finding: on matched Sep launch pegs, FT applies a price-forward
market-analysis register to Apple's $1,999 foldable iPhone Duo launch
(MANUAL ILLUSTRATIVE +0.10, relay-attested: "an attempt to revive interest
in a stagnant smartphone market") inside the product-launch register band it
applies to Meta's Sep-8/9 Muse launch (carried m625, +0.05). Illustrative delta
(Apple minus Meta) +0.05 near-null: the $0-tie entity and the $0-tie
comparator sit in the same register band, consistent with the standing neutral
prediction. A second fresh Apple arm (FT on the Sep-28 $5.7B patent-verdict
against Apple, MANUAL ILLUSTRATIVE -0.20, financial-market liability framing)
is documented but unscored; its contrast with the m10 Alice conduct-testing
register aimed at Meta is register selection, not tone. Cross-entity
licensing-gradient observation (OpenAI +0.25 over Apple +0.10 over Meta
+0.05) is hypothesis-generating only: the peg confound is STRONG and n=1 per
arm. Directionally supported, not proven. NOT artifact-grade. Correlation is
not causation.

Test tally: 48 tests, 12 classes.
"""

import os
import re
import subprocess

import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OWN_BASENAME = os.path.basename(__file__)
PROFILE = "profiles/financial-times.yaml"
MECH_KEY = "ft_apple_sep2026_duo_launch_market_register_vs_meta_muse_product_register"
M_ID = 868
ITER = 1062
TYPE_LETTER = "A"
RUN_PDT = "2026-09-28 23:00 PDT"
MECH_ID_MARKER = "mechanism" + "_868"  # own-mechanism marker (underscore form)
NEXT_US = "mechanism" + "_869"  # next-number underscore sweep
NEXT_DASH = "mechanism" + "-869"  # next-number dash sweep
NEXT_NUMERIC = "mechanism_id: " + "869"  # next-number numeric sweep
OWN_STAGED_SET = {
    "profiles/financial-times.yaml",
    "tests/test_type_a_1062_ft_apple_sep2026_duo_launch_market_register_vs_meta_muse_product_register_sep28_11pm.py",
    "tests/test_type_a_1057_gizmodo_openai_sep28_astra_cancellation_credit_vs_meta_scrapped_tool_sep28_6pm.py",
    "tests/test_type_b_1058_lucas_ropek_techcrunch_sep28_openai_astra_inbrief_vs_sep16_meta_luna_inbrief_stigma_contrast_sep28_7pm.py",
    "tests/test_type_c_1059_sb_energy_openai_55b_warrant_tenant_nvidia_105b_backstop_recycling_nineteenth_direction_sep28_8pm.py",
    "tests/test_type_d_1060_m865_m866_m867_qualitative_corpus_integrity_sep28_9pm.py",
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
ANCHORED_SHA = "0" * 40  # patched by anchor followup per #565

EXPECTED_ORDER = [("A", "1062"), ("E", "1061"), ("D", "1060"), ("C", "1059"), ("A", "1057")]
EXPECTED_TESTS = 48

# Evidence URLs, verbatim Full-URL listings from this run's browser.search sets.
LLMGRAM_URL = "https://llmgram.app/news/2026/09/apple-unveils-first-foldable-iphone-duo-starting-at-1-999-3344dc31.html"
LIVEMINT_URL = "https://www.livemint.com/companies/from-smartphone-to-luxury-tech-iphone-duo-iphone-18-pro-why-apple-may-be-pushing-the-iphone-further-upmarket-11789221620065.html"
ARCHYNETYS_APPLE_URL = "https://www.archynetys.com/trend/2026-09-26/apple-faces-5-7-billion-patent-infringement-verdict-over-iphone-and-apple-watch"
ARCHYNETYS_META_URL = "https://www.archynetys.com/trend/2026-09-08/meta-unveils-ai-personal-assistant-linked-to-whatsapp-and-instagram"


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
    # Block key sits at 4-space indent under competitor_relationships -> apple;
    # the next sibling 4-space key (or the 0-indent cross_entity section that
    # follows this last-under-apple block) bounds the block.
    text = _profiles_text()
    key = "    " + MECH_KEY + ":"
    start = text.index(key)
    rest = text[start + len(key) :]
    m = re.search(r"^(?:    [a-z][a-z0-9_]*:|[a-z][a-z0-9_]*:)$", rest, re.M)
    end = start + len(key) + m.start()
    return text[start:end]


def _mech():
    d = yaml.safe_load(_profiles_text())
    return d["competitor_relationships"]["apple"][MECH_KEY]


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


def _mains_after(anchored):
    # Main commits for this run: "Type A #1062:" subjects after ANCHORED_SHA.
    subjects = run_git("log", f"{anchored}..HEAD", "--format=%H %s", "--no-merges").stdout
    mains = []
    for line in subjects.splitlines():
        if re.search(r"Type A #1062:", line):
            mains.append(line)
    return mains


def _subject_window():
    subjects = run_git("log", "-25", "--format=%s", "--no-merges").stdout.splitlines()
    out = []
    seen = set()
    for s in subjects:
        m = re.match(r"Type ([A-E]) #(\d+)", s)
        if m and m.group(2) not in seen:
            seen.add(m.group(2))
            out.append(m.groups())
    return out[:5]


# ---------------------------------------------------------------------------
# 1. Novelty anchor
# ---------------------------------------------------------------------------
class TestNoveltyAnchorTypeA1062:
    def test_single_test_type_a_1062_file(self):
        files = [
            fn
            for fn in os.listdir(os.path.join(REPO_ROOT, "tests"))
            if fn.startswith("test_type_a_1062")
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
            "zero test_type_a_1062 files",
            "max numeric mechanism_id 867 pre-commit",
            "block key zero-hit",
            "3344dc31",
            "FIRST dedicated Type A mechanism",
        ):
            assert claim in doc.replace("\n", " ")


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1060-1064 window, third leg D->E->A->B->C
# ---------------------------------------------------------------------------
class TestRotationGuard1060_1064Window:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_1060_1064_third_leg(self):
        # Deselected pre-commit per #565: this run's own main commit does not
        # exist yet; goes green post-commit. SUBJECT DEVIATION pinned (per
        # the #1060 rotation-guard chain test): the #1058 Type B main commit
        # (103c871d) uses the subject "MediaScope #1058 Type B: ..." instead
        # of the "^Type [A-E] #N:" convention, so it is NOT regex-visible to
        # the #752 helper; the regex-visible chain reads A #1062 -> E #1061
        # -> D #1060 -> C #1059 -> A #1057.
        assert _window() == EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        # The 1060-1064 window legs present so far are adjacent and
        # cycle-valid; the #1058 B leg is the pinned deviation (asserted
        # separately) and sits below the >=1059 filter.
        window = [p for p in _window() if int(p[1]) >= 1059]
        assert len(window) >= 3, window
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_subject_deviation_1058_pinned(self):
        # The #1058 Type B main commit exists under its deviated subject
        # and is regex-invisible to the #752 helper (pinned, not a new
        # deviation by this run).
        r = run_git("log", "--format=%H %s", "--grep=MediaScope #1058 Type B:", "--no-merges")
        assert r.returncode == 0
        mains = [
            line for line in r.stdout.splitlines()
            if line.split(" ", 1)[1].startswith("MediaScope #1058 Type B:")
        ]
        assert len(mains) == 1, r.stdout
        assert mains[0].startswith("103c871d"), mains[0]
        assert not re.match(r"Type [A-E] #\d+:", mains[0].split(" ", 1)[1])

    def test_predecessor_is_type_e_1061(self):
        # Deselected pre-commit per #565 alongside the window-order test.
        order = _window()
        assert order[1] == ("E", "1061")
        r = run_git("log", "--grep", "Type E #1061:", "--format=%H", "--no-merges")
        assert r.stdout.strip(), "no Type E #1061 main commit found"

    def test_exactly_one_type_a_1062_main_commit(self):
        # Deselected pre-commit per #565 alongside the window-order test.
        r = run_git("log", "--grep", "Type A #1062:", "--format=%H", "--no-merges")
        assert len(r.stdout.split()) == 1, "expected exactly one Type A #1062 main commit"


# ---------------------------------------------------------------------------
# 3. Mechanism 868 block structure
# ---------------------------------------------------------------------------
class TestMechanism868Structure:
    def test_block_key_indent_4_under_apple_section(self):
        text = _profiles_text()
        assert "\n  apple:\n" in text
        assert "    " + MECH_KEY + ":" in text

    def test_block_key_descriptive_no_868(self):
        assert "868" not in MECH_KEY
        assert MECH_KEY == "ft_apple_sep2026_duo_launch_market_register_vs_meta_muse_product_register"

    def test_iteration_fields_1062_a(self):
        m = _mech()
        assert m["mechanism_id"] == M_ID
        assert m["iteration"] == ITER
        assert m["iteration_type"] == TYPE_LETTER
        assert m["iteration_time"] == RUN_PDT
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["date_analyzed"] == "2026-09-28"
        assert m["type"] == "Type A - Competitor Coverage Deep Dive"

    def test_publication_focus_ft(self):
        assert _mech()["publication_focus"] == "Financial Times"

    def test_window_phrase_sep_2026(self):
        m = _mech()
        finding = m["finding"]
        assert "Sep-10-2026" in finding and "Sep-28-2026" in finding
        assert "Sep-8/9" in finding

    def test_date_analyzed_is_run_date(self):
        assert _mech()["date_analyzed"] == "2026-09-28"

    def test_two_new_arms_plus_carried_meta_arm(self):
        arts = _mech()["articles"]
        assert len(arts) == 3
        assert arts[0]["url"] == LLMGRAM_URL
        assert arts[1]["url"] == ARCHYNETYS_APPLE_URL
        assert arts[2]["url"] == ARCHYNETYS_META_URL


# ---------------------------------------------------------------------------
# 4. Arms: two fresh Apple arms, carried Meta arm
# ---------------------------------------------------------------------------
class TestMechanism868Arms:
    def test_apple_launch_arm_a1_metadata(self):
        a1 = _mech()["articles"][0]
        assert a1["date"] == "2026-09-10"
        assert a1["register"] == "price_forward_market_analysis"
        assert a1["manual_illustrative_tone"] == 0.10
        assert a1["relay_url"] == LIVEMINT_URL

    def test_apple_launch_arm_a1_key_phrase_verbatim(self):
        a1 = _mech()["articles"][0]
        assert "an attempt to revive interest in a stagnant smartphone market" in a1["key_phrases"]
        assert "will cost $1,999" in a1["key_phrases"]

    def test_apple_liability_arm_a2_metadata(self):
        a2 = _mech()["articles"][1]
        assert a2["date"] == "2026-09-28"
        assert a2["register"] == "financial_market_liability_framing"
        assert a2["manual_illustrative_tone"] == -0.20

    def test_apple_liability_arm_a2_key_phrase_verbatim(self):
        a2 = _mech()["articles"][1]
        assert "Burford Capital is positioned to receive up to $1.4 billion" in a2["key_phrases"]
        assert "$5.7 billion patent infringement verdict" in a2["key_phrases"]

    def test_carried_meta_arm_m625_metadata(self):
        m1 = _mech()["articles"][2]
        assert m1["date"] == "2026-09-08/09"
        assert m1["register"] == "product_distribution_factual"
        assert m1["manual_illustrative_tone"] == 0.05
        assert "un-rescored per #807" in m1["verification"]
        assert "m625" in m1["verification"]

    def test_source_urls_verbatim_four(self):
        urls = _mech()["source_urls"]
        assert len(urls) == 4
        for u in (LLMGRAM_URL, LIVEMINT_URL, ARCHYNETYS_APPLE_URL, ARCHYNETYS_META_URL):
            assert u in urls, u

    def test_near_null_delta_framing(self):
        finding = _mech()["finding"]
        assert "+0.05 near-null" in finding
        assert "the standing neutral prediction" in finding


# ---------------------------------------------------------------------------
# 5. Scorer: tones, delta, methodology
# ---------------------------------------------------------------------------
class TestMechanism868Scorer:
    def test_tones_and_delta(self):
        s = _mech()["asymmetry_scorer_result"]
        assert s["target_entity"] == "apple"
        assert s["peer_entities"] == ["meta"]
        assert s["target_avg_tone"] == 0.10
        assert s["peer_avg_tone"] == 0.05
        assert s["asymmetry_score"] == 0.05
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
        assert "n=1 vs n=1" in method

    def test_not_artifact_grade(self):
        disc = _mech()["statistical_discipline"]
        assert "NOT artifact-grade" in disc
        assert "verdict directionally_supported_not_proven" in disc


# ---------------------------------------------------------------------------
# 6. Confounders, counterevidence, extends chain
# ---------------------------------------------------------------------------
class TestMechanism868Confounders:
    def test_five_confounders_strong_first(self):
        confs = _mech()["confounders"]
        assert len(confs) == 5
        strong = [c for c in confs if c.startswith("STRONG")]
        assert len(strong) == 2
        assert confs[0].startswith("STRONG news-peg confound")

    def test_three_counterevidence(self):
        ce = _mech()["counter_evidence"]
        assert len(ce) == 3

    def test_extends_chain_refs(self):
        finding = _mech()["finding"]
        ce_text = " ".join(_mech()["counter_evidence"])
        assert "m625" in finding
        assert "m10" in finding
        assert "m10" in ce_text


# ---------------------------------------------------------------------------
# 7. Discipline: manual only, research method, falsification family
# ---------------------------------------------------------------------------
class TestMechanism868Discipline:
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
        assert "5 browser.search" in rm
        assert "0 browser.open" in rm
        assert "ASCII-only, no em dashes" in rm


# ---------------------------------------------------------------------------
# 8. Post-commit corpus novelty: 868 is max, 869 is zero
# ---------------------------------------------------------------------------
class TestCorpusNoveltyPostCommit:
    def test_max_numeric_mechanism_id_is_868(self):
        ids = _corpus_ids()
        assert max(ids) == M_ID

    def test_zero_next_numeric_869_in_profiles(self):
        base = os.path.join(REPO_ROOT, "profiles")
        for root, _, files in os.walk(base):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(root, fn))
                    assert NEXT_NUMERIC not in text

    def test_zero_next_underscore_dash_869_repo_wide(self):
        assert _repo_grep(NEXT_US) == []
        assert _repo_grep(NEXT_DASH) == []

    def test_distinct_from_three_items(self):
        df = _mech()["distinct_from"]
        assert len(df) == 3


# ---------------------------------------------------------------------------
# 9. Doc-sync ratchet per #719 (README stats, row, ARCH row, log entry)
# ---------------------------------------------------------------------------
class TestDocSyncRatchet1062:
    def test_readme_stats_bumped(self):
        text = _read("README.md")
        assert "| Tests | 54505 | Across 1387 test files |" in text

    def test_readme_new_row(self):
        text = _read("README.md")
        assert "#1062" in text and "FT x Apple Duo-launch market register" in text

    def test_arch_tree_new_row(self):
        text = _read("docs/ARCHITECTURE.md")
        assert "1062" in text and "FT x Apple Duo-launch" in text

    def test_iteration_log_new_entry(self):
        text = _read("iteration-log.md")
        assert "Type A #1062" in text and "mechanism 868" in text


# ---------------------------------------------------------------------------
# 10. In-flight isolation: targeted staging only
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
        assert "–" not in text  # en dash
        assert "—" not in text  # em dash
        text.encode("ascii")

    def test_docstring_ascii(self):
        __doc__.encode("ascii")


# ---------------------------------------------------------------------------
# 12. Guard carriers: underscore/dash 868 needles are pure zero post-commit
# ---------------------------------------------------------------------------
class TestGuardCarriersPinned:
    def test_underscore_868_pure_zero(self):
        # Own-mechanism underscore-form 868 needles are pure zero repo-wide:
        # the block uses the numeric field form and the new file builds its
        # 868 marker at runtime (per #715), so no contiguous literal exists.
        assert _repo_grep(MECH_ID_MARKER) == []

    def test_dash_868_pure_zero(self):
        dash = "mechanism" + "-868"
        assert _repo_grep(dash) == []
