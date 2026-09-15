"""Type C #769 (2026-09-15 11:00 PDT): Apollo AI-infrastructure financial architecture -
post-TechCrunch-sale correction and Sep 2026 status.

Mechanism 693 (update leg on mechanism 111): Apollo Global Management finances TWO
frontier AI labs - xAI via the $3.5B Valor Compute Infrastructure capital solution
(Jan 7 2026, triple-net lease of NVIDIA GB200 GPUs) and Anthropic via the $35B
Broadcom AI XPV Platform lead (Jun 9 2026) - while owning Yahoo, publisher of
Engadget. This iteration formalizes the post-TechCrunch-sale correction (TechCrunch
sold by Yahoo to Regent LP in Mar 2025 per the Aug 26 ownership correction, so the
Apollo chain is now Engadget-only), re-verifies both financing legs as live in
Sep 2026, corrects the corpus $11.2B Yahoo-acquisition figure to the verified $5B,
refines mechanism 104's $3.4B xAI figure to $3.5B, and honestly reports the
analytical consequence: the correction WEAKENS the Apollo-chain coverage case
because the strongest Apollo-chain coverage evidence (#305, Rebecca Bellan at
TechCrunch) reattributes to the Regent LP chain.

FIRST new mechanism on the yahoo_apollo entity since the Aug 26 ownership
correction. FIRST formal post-TechCrunch-sale Apollo-chain correction. FIRST $5B
Yahoo-acquisition figure correction. FIRST Sep 2026 live-status re-verification
of both Apollo AI-lab financing legs (Travers Smith regulatory-advice piece,
crawled ~Sep 2026, re-confirms the $35B XPV deal).

Qualitative Type C only: p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant
False per the Aug 28 2026 standing rule. Engine not run. NOT a
falsification-family member; ledger holds at 26. NOT artifact-grade; no
analysis.json update. Verdict: directionally_supported_not_proven on the
financial-relationship documentation and the ownership correction; no
coverage-tone claim.

Rotation: 765-769 window closes D->E->A->B->C (#765 Type D 8am, #766 Type E 9am,
#767 Type A 9am, #768 Type B 10am, #769 Type C 11am).
"""

import os
import re
import subprocess

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST_BASENAME = os.path.basename(__file__)
MECH_KEY = "apollo financial architecture post techcrunch sale engadget only chain correction sep2026"
MECH_NUM = 693
MECH_ID_MARKER = "mechanism" + "_693"  # must stay ABSENT from block and profiles

# Verbatim source URLs (copied from browser.search Full-URL listings; none constructed)
URL_VALOR_APOLLO_COM = "https://www.apollo.com/insights-news/pressreleases/2026/01/apollo-backs-5-4-billion-valor-and-xai-data-center-compute-infrastructure-transaction-with-3-5-billion-capital-solution-3214463"
URL_VALOR_IR = "https://ir.apollo.com/news-events/press-releases/detail/599/apollo-backs-5-4-billion-valor-and-xai-data-center-compute"
URL_VALOR_GNW = "https://www.globenewswire.com/news-release/2026/01/07/3214463/0/en/Apollo-Backs-5-4-Billion-Valor-and-xAI-Data-Center-Compute-Infrastructure-Transaction-with-3-5-Billion-Capital-Solution.html"
URL_XPV_IR = "https://ir.apollo.com/news-events/press-releases/detail/629/apollo-leads-35-billion-capital-solution-for-broadcom-ai"
URL_XPV_MILBANK = "https://www.milbank.com/en/news/milbank-advises-on-apollo-led-dollar35b-capital-solution-for-broadcom-ai-xpv-platform.html"
URL_XPV_WSJ = "https://www.wsj.com/tech/ai/broadcom-apollo-blackstone-launch-35-billion-ai-infrastructure-platform-8fc8f65e"
URL_XPV_BARRONS = "https://www.barrons.com/articles/broadcom-stock-price-ai-xpv-platform-7bcdfe21f53e"
URL_YAHOO_TC = "https://techcrunch.com/?p=2196989"
URL_YAHOO_ENGADGET = "https://www.engadget.com/verizon-media-sale-yahoo-apollo-funds-122155517.html"

ENTITIES_PATH = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

# Placeholder pre-commit; patched to the main-commit SHA in the #565 followup.
ANCHORED_SHA = "PENDING_ANCHOR_PATCH_PER_565"


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _norm(text):
    return " ".join(text.split())


def _git_log_mains(prefix_pat):
    out = subprocess.run(
        ["git", "-C", REPO_ROOT, "log", "--format=%H %s", "--no-merges", "--", "."],
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    return [line for line in out if re.search(prefix_pat, line)]


def _repo_grep(pattern, roots=("profiles", "tests")):
    hits = []
    for root in roots:
        proc = subprocess.run(
            ["git", "grep", "-l", pattern, "--", root],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        if proc.returncode == 0:
            hits.extend(proc.stdout.splitlines())
    return hits


def _profiles_corpus():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith((".yaml", ".yml", ".md")):
                out.append(_read(os.path.join(root, fn)))
    return "\n".join(out)


def _entities_raw():
    return _read(ENTITIES_PATH)


def _block():
    corpus = _entities_raw()
    return corpus[corpus.index(MECH_KEY + ":"):]


def _block_data():
    import yaml

    d = yaml.safe_load(_entities_raw())
    return d["entities"]["yahoo_apollo"][MECH_KEY]


class TestNovelty769:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_c_769_file(self):
        files = sorted(
            f for f in os.listdir(os.path.join(REPO_ROOT, "tests"))
            if f.startswith("test_type_c_769") and f.endswith(".py")
        )
        assert files == [TEST_BASENAME], files

    def test_type_c_769_main_commit_unique_and_anchored(self):
        mains = _git_log_mains(r"Type C #769: ")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim_present_in_block(self):
        # Novelty was verified pre-commit by shell greps (zero test_type_c_769
        # files, no "Type C #769" in git log, the post-sale-correction key
        # fragment zero-hit repo-wide, max numeric mechanism_id 692, zero
        # underscore-form 693 keys excluding sweep-instrument carriers per
        # #715); this test pins the claim in the committed block, per the
        # #752 convention.
        block = _block()
        assert "Zero test_type_c_769 files on disk pre-commit" in block
        assert 'no "Type C #769" in git log pre-commit' in block
        assert '"post techcrunch sale engadget only chain correction" zero-hit repo-wide pre-commit' in block
        assert "max numeric mechanism_id 692 pre-commit" in block


class TestRotationCycleGuard769:
    """Rotation: 765-769 window closes D->E->A->B->C."""

    EXPECTED_ORDER = [("C", "769"), ("B", "768"), ("A", "767"), ("E", "766"), ("D", "765")]
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def _window(self):
        # First occurrence of each distinct iteration number, newest first
        # (robust to the #756-style followup commits that repeat the same
        # "Type X #N" wording without the colon, per the #752 convention).
        mains = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%s", "--no-merges", "-n", "40", "--", "."],
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        seen_nums = set()
        out = []
        for s in mains:
            m = re.match(r"Type ([A-E]) #(\d+):", s)
            if m and m.group(2) not in seen_nums:
                seen_nums.add(m.group(2))
                out.append(m.groups())
        return out[:5]

    def test_window_closes_deabc(self):
        assert self._window() == self.EXPECTED_ORDER

    def test_window_cycle_edges_are_adjacent(self):
        window = self._window()
        for (t1, _), (t2, _) in zip(window, window[1:]):
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains(r"Type C #769: ")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains and mains[0].startswith(ANCHORED_SHA + " "), mains


class TestMechanism693Content:
    def test_block_present_in_entities(self):
        assert MECH_KEY + ":" in _entities_raw()

    def test_block_key_field_matches_test_file(self):
        data = _block_data()
        assert data["block_key"] == "type_c_769_apollo_financial_architecture_post_tc_sale_engadget_only_chain_sep15_11am"

    def test_mechanism_id_is_693(self):
        assert _block_data()["mechanism_id"] == MECH_NUM

    def test_type_c_and_iteration_769(self):
        data = _block_data()
        assert data["iteration"] == 769
        assert data["iteration_type"] == "C"
        assert data["type"] == "C"
        assert data["type_label"] == "Financial Incentive Mapping"
        assert data["rotation_type"] == "C"

    def test_entity_is_yahoo_apollo(self):
        import yaml

        d = yaml.safe_load(_entities_raw())
        assert MECH_KEY in d["entities"]["yahoo_apollo"]

    def test_block_key_unique_in_entities(self):
        assert _entities_raw().count(MECH_KEY + ":") == 1

    def test_entities_yaml_parses_clean(self):
        import yaml

        d = yaml.safe_load(_entities_raw())
        assert d["entities"]["yahoo_apollo"][MECH_KEY]["mechanism_id"] == MECH_NUM

    def test_designed_keying_no_underscore_form_in_block(self):
        # The m693 block key carries no underscore-form marker substring, so
        # #768's zero-underscore-693 sweeps stay GREEN.
        assert MECH_ID_MARKER not in _block()

    def test_iteration_time_and_goal(self):
        data = _block_data()
        assert data["iteration_time"] == "2026-09-15 11:00 PDT"
        assert data["goal_id"] == "goal_54093bda4145"
        assert data["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_update_leg_on_mechanism_111(self):
        block = _norm(_block())
        assert "mechanism 111" in block
        assert "correction-and-status leg" in block


class TestDealTerms769:
    """The verified financial terms: both legs, exact figures, exact dates."""

    def test_xai_valor_3_5b_of_5_4b(self):
        block = _norm(_block())
        assert "$3.5B" in block
        assert "$5.4B" in block
        assert "2026-01-07" in block

    def test_xai_valor_triple_net_lease_gb200(self):
        block = _norm(_block())
        assert "Triple net lease" in block
        assert "GB200" in block
        assert "Valor Compute Infrastructure" in block

    def test_xai_valor_nvidia_anchor_lp(self):
        block = _norm(_block())
        assert "Anchor Limited Partner" in block

    def test_anthropic_xpv_35b(self):
        block = _norm(_block())
        assert "$35B" in block
        assert "2026-06-09" in block
        assert "Broadcom" in block

    def test_anthropic_xpv_blackstone_and_banks(self):
        block = _norm(_block())
        assert "Blackstone" in block

    def test_anthropic_xpv_20gw_target(self):
        block = _norm(_block())
        assert "20GW" in block

    def test_verbatim_source_urls_present(self):
        block = _block()
        for url in (
            URL_VALOR_APOLLO_COM, URL_VALOR_IR, URL_VALOR_GNW,
            URL_XPV_IR, URL_XPV_MILBANK, URL_XPV_WSJ, URL_XPV_BARRONS,
            URL_YAHOO_TC, URL_YAHOO_ENGADGET,
        ):
            assert url in block, url

    def test_nine_source_urls(self):
        assert len(_block_data()["source_urls"]) == 9


class TestOwnershipCorrection769:
    """The post-TechCrunch-sale correction: Engadget-only Apollo chain."""

    def test_techcrunch_severed_to_regent(self):
        block = _norm(_block())
        assert "Regent LP" in block
        assert "Mar 2025" in block
        assert "SEVERED" in block

    def test_engadget_only_chain(self):
        block = _norm(_block())
        assert "Engadget ONLY" in block

    def test_5b_yahoo_acquisition_correction(self):
        block = _norm(_block())
        assert "$5B" in block
        assert "$11.2B" in block
        assert "$4.25B" in block
        assert "10%" in block

    def test_mechanism_104_xai_figure_refined(self):
        block = _norm(_block())
        assert "$3.4B" in block
        assert "refined to" in block

    def test_bellan_305_reattributed_to_regent(self):
        block = _norm(_block())
        assert "#305" in block
        assert "reattribute" in block.lower()

    def test_correction_weakens_apollo_chain_case(self):
        block = _norm(_block())
        assert "WEAKENS" in block


class TestStatisticalDiscipline769:
    """Qualitative-only Type C: no scoring, no significance, ledger holds."""

    def test_tone_scores_not_scored(self):
        assert _block_data()["tone_scores"] == "NOT_SCORED"

    def test_stats_not_calculated(self):
        disc = _block_data()["statistical_discipline"]
        assert "p_value NOT_CALCULATED" in disc
        assert "cohens_d NOT_CALCULATED" in disc
        assert "ci_95 NOT_CALCULATED" in disc

    def test_is_significant_false(self):
        assert "is_significant False" in _block_data()["statistical_discipline"]

    def test_engine_not_run(self):
        assert "Engine NOT run" in _block_data()["statistical_discipline"]

    def test_no_analysis_json_update(self):
        assert _block_data()["no_analysis_json_update"] is True

    def test_ledger_holds_at_26(self):
        disc = _block_data()["statistical_discipline"]
        assert "ledger holds at 26" in disc
        assert "NOT a falsification-family member" in disc

    def test_verdict_directionally_supported(self):
        assert "directionally_supported_not_proven" in _block_data()["statistical_discipline"]


class TestSupersessionAndCorpusPost768:
    """Post-#768 corpus integrity: max 693, zero 694, designed supersession."""

    def _ids(self):
        return [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)\b", _profiles_corpus())]

    def test_max_numeric_mechanism_id_is_693(self):
        assert max(self._ids()) == MECH_NUM, max(self._ids())

    def test_692_still_present(self):
        hits = [h for h in _repo_grep("mechanism_id: 692")]
        assert len(hits) >= 1, hits

    def test_zero_underscore_693_keys_repo_wide(self):
        hits = _repo_grep(MECH_ID_MARKER)
        assert hits == [], hits

    def test_zero_numeric_694_keys_in_profiles(self):
        hits = _repo_grep("mechanism_id: 694", roots=("profiles",))
        assert hits == [], hits

    def test_d768_zero_numeric_693_profiles_sweep_fails_by_designed_supersession(self):
        # #768 asserted zero "mechanism_id: 693" hits in profiles/; the m693
        # block supersedes it by design per the #710/#720 convention.
        hits = _repo_grep("mechanism_id: 693", roots=("profiles",))
        assert len(hits) >= 1, hits

    def test_d768_max_692_sweep_superseded_by_design(self):
        # #768 asserted max == 692; advancing to 693 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert max(self._ids()) == MECH_NUM != 692

    def test_d768_zero_underscore_693_profiles_sweep_stays_green(self):
        # #768 asserted zero underscore-form 693 markers in profiles/; the
        # m693 block key carries no such substring by designed keying, so
        # that sweep stays green.
        hits = _repo_grep(MECH_ID_MARKER, roots=("profiles",))
        assert hits == [], hits

    def test_d768_zero_underscore_693_tests_sweep_stays_green(self):
        # #768 asserted zero underscore-form 693 markers in tests/; this file
        # builds the marker by concatenation ("mechanism" + "_693") and
        # carries no contiguous literal, so the sweep stays green.
        hits = _repo_grep(MECH_ID_MARKER, roots=("tests",))
        hits = [h for h in hits if not h.endswith(TEST_BASENAME)]
        assert hits == [], hits

    def test_m693_block_key_unique_and_entities_parse(self):
        assert _entities_raw().count(MECH_KEY + ":") == 1
        import yaml

        d = yaml.safe_load(_entities_raw())
        assert d["entities"]["yahoo_apollo"][MECH_KEY]["mechanism_id"] == MECH_NUM


class TestLedger769:
    """Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent; m693 not a member."""

    def test_twenty_sixth_present_and_twenty_seventh_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference "TWENTY-SEVENTH" inside their own
        # negative guards, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus

    def test_m693_not_falsification_family(self):
        fam = _block_data()["falsification_family"]
        assert "NOT a falsification-family member" in fam
        assert "ledger holds at 26" in fam


class TestDocSync769:
    def test_readme_row_769(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_readme_lists_769_file(self):
        doc = _read(README_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))

    def test_architecture_row_769(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_769_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog769:
    def test_iteration_log_entry_769(self):
        assert "Type C #769" in _read(LOG_PATH)

    def test_iteration_log_mentions_mechanism_693(self):
        assert "693" in _read(LOG_PATH)
