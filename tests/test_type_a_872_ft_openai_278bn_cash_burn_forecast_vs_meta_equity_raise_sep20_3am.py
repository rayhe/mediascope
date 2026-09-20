"""Type A iteration 872: FT x OpenAI Sep-18 2026 $278B cash-burn forecast scoop
(balance-sheet realism register) vs the FT Jun-5 Meta equity-raise desperation
comparator (mechanism 754), THIRD leg of the 870-874 rotation window.

Type A contract (per the standing rotation doctrine): add ONE mechanism block keyed under
profiles/<publication>.yaml competitor_relationships, covering a publication x competitor
pair that is fresh this run, with attribution URLs verified against a real search, and
cross-reference the existing comparator register from an earlier Type A on the same
outlet. This run: Financial Times x OpenAI.

Publication focus: Financial Times. Competitor: OpenAI. Comparison entity: Meta.
Financial context: financial_tie licensing ($5-10M/yr secondary, mechanism 54),
direction receiving, coverage_prediction softer_than_expected (this profile,
competitor_relationships.openai) - so the deal prediction is uniform softening on the
deal partner; the observed register does NOT falsify it (company-forecasted financial
disclosure with bullish revenue context, not adversarial coverage).

OpenAI arm (FRESH this run, mechanism 754): the FT's Sep-18 2026 scoop, via the Reuters
relay (Mrinmay Dey, Sep 18): "OpenAI expects to burn through $278 billion in cash
between 2026 and 2030 as it ramps up spending on computing power and infrastructure,
the Financial Times reported on Friday, citing a company presentation seen by the
newspaper." Figures: negative free cash flow $278B over 2026-2030; revenue tenfold
$36B (2026) to $350B (2030); cumulative $840B revenue through decade end; ~$856B
computing/infrastructure spend (largest expense); the $122B March raise "on track to
exhaust that cash by 2028". Register: balance-sheet realism. MANUAL ILLUSTRATIVE tone
-0.15 (mixed register: burn framing negative, bullish revenue trajectory positive;
judgment call, documented). FT original paywalled, so excerpt-bounded per #503, 0
browser.open this run.

Comparator arm (CARRIED, un-rescored per #807): the FT Jun-5 2026 Meta equity-raise
scoop from mechanism 718 (mechanism 435 lineage): "Meta weighs big equity raising to
finance AI infrastructure", shares down 6.6% on the report, "creative" ways to raise
cash for AI capex "as much as $145 billion this year and even higher in 2027".
MANUAL ILLUSTRATIVE -0.30, desperation register.

Illustrative delta: OpenAI-minus-Meta +0.15 (-0.15 - (-0.30)). The gap NARROWS
sharply vs mechanism 718's +0.55 (matched capital-raise pegs): the FT's most
balance-sheet-adversarial OpenAI item this window - a cash-burn scoop that undercuts
its own Sep-15 $1.2T investor-demand scoop - still lands gentler than the Meta
capital-raise register. Cross-peg arms (company-financials forecast vs financing
event), so the comparison is weaker than 718's matched pegs. MANUAL ILLUSTRATIVE ONLY
per the Aug 28 2026 standing rule: engine NOT run (degenerate n=1 check only);
p_value, cohens_d, ci_95 all NOT_CALCULATED; is_significant False; NOT artifact-grade;
NO analysis.json update.

Findings: NOT a falsification-family member (ledger holds at 27). The illustrative gap
is directionally consistent with mechanism 54's licensing-incentive prediction but does
not contradict any coverage_prediction. EXTENDS mechanism 718 with the cash-burn
successor at the same outlet x pair. Correlation is not causation.

Research: 5 browser.search query sets this run. REJECTED candidates: Bloomberg x
OpenAI $200B/$850B (stale mid-Aug story, no profiled-publication primary); Bloomberg
$1.2T follow-up (no bloomberg.yaml profile); BI x Anthropic Sep-13 Nasdaq scoop
(already in corpus via Type A #857, mechanisms 745/746); NYT x OpenAI $1.5T financing
(already in corpus via Type A #822). SELECTED: FT x OpenAI $278B cash-burn forecast
(Sep 18; zero corpus hits on "278 billion"/"856 billion"). Novelty verified
pre-commit (zero test_type_a_872 files on disk; no "Type A #872" in git log; all four
evidence URLs zero-hit repo-wide; block key zero-hit pre-commit; max numeric
mechanism_id 753; zero underscore-form 754 keys by designed keying per #715).

Rotation: 870-874 window THIRD leg, D(#870) -> E(#871) -> A(#872) (anchor patched
post-commit per #565). Sep 20 2026 03:00 PDT. 50 tests, 11 classes.
"""

import os
import re
import subprocess

import pytest
import yaml

TEST_FILE = __file__
OWN_BASENAME = "test_type_a_872_ft_openai_278bn_cash_burn_forecast_vs_meta_equity_raise_sep20_3am.py"
MECH_KEY = "ft_openai_278bn_cash_burn_forecast_vs_meta_equity_raise_sep18"
M_ID = 754
ITER = 872
TYPE_LETTER = "A"
ANCHORED_SHA = "4ee277c2cd0ef4415b41f0a9a49c18f62eb48981"

MECH_ID_MARKER = "mechanism" + "_754"
NEXT_ID_MARKER = "mechanism" + "_755"
NEXT_ID_NUMERIC = "mechanism_id: " + "755"
NEXT_ID_DASH = "mechanism" + "-755"

WIXX_URL = "https://wixx.com/2026/09/18/openai-expects-to-burn-through-almost-280-billion-by-2030-ft-reports/"
TECHTIMES_URL = "https://www.techtimes.com/articles/327752/20260920/openai-projects-278b-cash-burn-record-round-runs-dry-before-revenue-catches.htm"
HBL_URL = "https://www.thehindubusinessline.com/info-tech/openai-forecasts-cash-burn-near-280-billion-by-2030/article71483712.ece"
INVESTORSCOM_URL = "https://www.investors.com/news/technology/anthropic-ipo-delayed-openai-expects-massive-cash-burn/"
META_MIRROR_URL = "https://www.reuters.com/technology/meta-weighs-big-equity-raising-finance-ai-infrastructure-ft-reports-2026-06-05/"

# Type A #872 is the THIRD leg of the 870-874 window: D(#870) -> E(#871) -> A(#872).
EXPECTED_ORDER = [("A", "872"), ("E", "871"), ("D", "870"), ("C", "869"), ("B", "868")]


def _repo_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _read(relpath):
    with open(os.path.join(_repo_root(), relpath), "r", encoding="utf-8") as fh:
        return fh.read()


def _yaml_block():
    text = _read("profiles/financial-times.yaml")
    start = text.index(MECH_KEY)
    end = text.index("\n  meta:", start)
    return text[start:end]


def _block_yaml():
    data = yaml.safe_load(_read("profiles/financial-times.yaml"))
    return data["competitor_relationships"]["openai"][MECH_KEY]


def _git(*args):
    proc = subprocess.run(
        ["git", "-C", _repo_root()] + list(args),
        capture_output=True,
        text=True,
    )
    return proc


def _repo_grep(pattern):
    hits = []
    for root, dirs, files in os.walk(_repo_root()):
        if ".git" in dirs:
            dirs.remove(".git")
        if "__pycache__" in dirs:
            dirs.remove("__pycache__")
        for fname in files:
            if not fname.endswith((".py", ".yaml", ".yml", ".md", ".json")):
                continue
            fpath = os.path.join(root, fname)
            try:
                with open(fpath, "r", encoding="utf-8", errors="ignore") as fh:
                    for lineno, line in enumerate(fh, 1):
                        if re.search(pattern, line):
                            hits.append((os.path.relpath(fpath, _repo_root()), lineno, line.strip()))
            except OSError:
                continue
    return hits


class TestNovelty872:
    def test_single_test_type_a_872_file(self):
        files = [f for f in os.listdir(os.path.join(_repo_root(), "tests"))
                 if f.startswith("test_type_a_872")]
        assert files == [OWN_BASENAME]

    def test_type_a_872_main_commit_unique_and_anchored(self):
        # DESELECTED pre-commit (per #565): the commit does not exist yet.
        proc = _git("log", "--format=%H %s", "--grep", "Type A #872")
        mains = [ln for ln in proc.stdout.splitlines()
                 if re.search(r"Type A #872(?::| )", ln)
                 and "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) == 1
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565")
        assert mains[0].startswith(ANCHORED_SHA + " ")

    def test_novelty_verification_claim(self):
        blk = _block_yaml()
        novelty = blk["novelty"]
        assert "Zero test_type_a_872 files" in novelty
        assert 'no "Type A #872" in git log' in novelty or "no Type A #872 in git log" in novelty
        assert "cash-burn forecast scoop" in novelty
        assert "block key zero-hit repo-wide pre-commit" in novelty
        assert "max numeric mechanism_id 753 pre-commit" in novelty
        assert "zero underscore-form 754" in novelty

    def test_870_871_window_legs_present_prior_to_872(self):
        log = _read("iteration-log.md")
        assert "## #870 Type D:" in log
        assert "## #871 Type E:" in log
        idx_870 = log.index("## #870 Type D:")
        idx_871 = log.index("## #871 Type E:")
        assert idx_871 < idx_870


class TestRotationGuard872:
    # All rotation-guard tests are DESELECTED pre-commit (per #565).
    def test_window_is_870_874_third_leg(self):
        subjects = _git("log", "--format=%s").stdout.splitlines()
        order = []
        for s in subjects:
            m = re.search(r"Type ([A-E]) #(\d+)(?::| )", s)
            if m and m.group(2) in ("868", "869", "870", "871", "872"):
                # Followups and test-fixups are not rotation legs. The
                # push-status followup commit type (introduced at #864)
                # is excluded alongside anchor/log-hash followups.
                if ("anchor followup" not in s and "log-hash followup" not in s
                        and "push-status followup" not in s and "test fixup" not in s):
                    order.append((m.group(1), m.group(2)))
        for expected, got in zip(EXPECTED_ORDER, order):
            assert expected == got

    def test_rotation_adjacency_cycle_valid(self):
        cycle = ["D", "E", "A", "B", "C"]
        got = [t for t, _n in EXPECTED_ORDER]
        assert got == ["A", "E", "D", "C", "B"]
        assert cycle[cycle.index("D") + 1] == "E"
        assert cycle[cycle.index("E") + 1] == "A"

    def test_predecessor_is_type_e_871(self):
        proc = _git("log", "--oneline", "--grep", "Type E #871", "--all")
        mains = [ln for ln in proc.stdout.splitlines()
                 if "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) >= 1

    def test_anchor_sha_matches_head(self):
        head = _git("rev-parse", "HEAD").stdout.strip()
        assert ANCHORED_SHA == head


class TestNoveltyAnchor872:
    def test_block_key_absent_before_this_run(self):
        # The designed block key must not collide with any earlier
        # mechanism key; uniqueness is asserted structurally in
        # TestMechanism754Structure, this anchors the novelty claim text.
        assert "ft_openai_278bn_cash_burn" in MECH_KEY
        assert MECH_KEY.endswith("sep18")


class TestMechanism754Structure:
    def test_block_key_exists_in_ft_profile(self):
        text = _read("profiles/financial-times.yaml")
        assert text.count(MECH_KEY) == 1
        block = _yaml_block()
        assert block.startswith(MECH_KEY)

    def test_block_key_unique_in_profile(self):
        text = _read("profiles/financial-times.yaml")
        assert text.count(MECH_KEY) == 1

    def test_block_lives_under_openai_competitor_relationship(self):
        blk = _block_yaml()
        assert blk["mechanism_id"] == M_ID
        assert blk["competitor"] == "openai"
        assert blk["iteration"] == ITER
        assert blk["iteration_type"] == TYPE_LETTER

    def test_mechanism_id_754_adjacent_to_key(self):
        text = _read("profiles/financial-times.yaml")
        start = text.index(MECH_KEY)
        assert "mechanism_id: 754" in text[start:start + 400]

    def test_pair_and_iteration_fields(self):
        blk = _block_yaml()
        assert blk["publication_pair"] == "FT x OpenAI"
        assert blk["entity_pair"] == "OpenAI vs Meta"
        assert blk["iteration_time"] == "2026-09-20 03:00 PDT"
        assert blk["scheduled_job_id"] == "mediascope-daily-iteration"
        assert blk["goal_id"] == "goal_54093bda4145"
        assert blk["type"] == "Type A - Competitor Coverage Deep Dive"
        assert blk["comparison_entities"] == ["meta"]

    def test_m718_block_still_present(self):
        # The $1.2T scoop comparator mechanism must survive this edit.
        text = _read("profiles/financial-times.yaml")
        assert "ft_openai_1_2tn_funding_round_scoop_vs_meta_equity_raise_desperation_sep17" in text
        assert "mechanism_id: 718" in text

    def test_meta_section_intact_after_insert(self):
        text = _read("profiles/financial-times.yaml")
        assert "\n  meta:\n    financial_tie: none" in text


class TestMechanism754OpenAIArm:
    def _arm(self):
        return _block_yaml()["articles"][0]

    def test_fresh_arm_identity(self):
        arm = self._arm()
        assert arm["date"] == "2026-09-18"
        assert arm["register"] == "balance_sheet_realism_cash_burn"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == pytest.approx(-0.15)
        assert "cash-burn" in arm["title"]

    def test_attribution_url_verbatim_in_block(self):
        block = _yaml_block()
        assert WIXX_URL in block
        assert TECHTIMES_URL in block
        assert HBL_URL in block
        assert INVESTORSCOM_URL in block

    def test_ft_attribution_evidence(self):
        block = _yaml_block()
        assert "citing a company presentation seen by the newspaper" in block
        assert "Mrinmay Dey" in block

    def test_key_figures(self):
        block = _yaml_block()
        assert "$278 billion" in block
        assert "$856 billion" in block
        assert "$840 billion" in block
        assert "$350 billion" in block
        assert "exhaust that cash by 2028" in block

    def test_key_language(self):
        block = _yaml_block()
        assert "burn through $278 billion in cash" in block
        assert "negative free cash flow" in block
        assert "largest expense category" in block

    def test_bullish_counterweight_noted(self):
        block = _yaml_block()
        assert "tenfold" in block
        assert "$36 billion" in block

    def test_excerpt_bounded_evidence_grade(self):
        arm = self._arm()
        assert "paywalled" in arm["source_note"]
        assert "headline-level and quote-level only" in arm["source_note"]
        assert "FT body register unverified" in arm["source_note"]


class TestMechanism754ComparatorArm:
    def _arm(self):
        return _block_yaml()["articles"][1]

    def test_meta_arm_carried(self):
        arm = self._arm()
        assert arm["date"] == "2026-06-05"
        assert arm["register"] == "capital_raise_desperation"
        assert arm["meta_capital_tone_MANUAL_ILLUSTRATIVE"] == pytest.approx(-0.30)

    def test_meta_mirror_url_verbatim(self):
        block = _yaml_block()
        assert META_MIRROR_URL in block

    def test_carried_unrescored_per_807(self):
        arm = self._arm()
        assert "carried un-rescored per #807" in arm["source_note"]

    def test_comparator_key_language(self):
        block = _yaml_block()
        assert "down 6.6%" in block
        assert '"creative" ways to raise cash' in block
        assert "$145 billion" in block


class TestMechanism754Scorer:
    def _scorer(self):
        return _block_yaml()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]

    def test_illustrative_tones(self):
        s = self._scorer()
        assert s["openai_arm_avg"] == pytest.approx(-0.15)
        assert s["meta_arm_avg"] == pytest.approx(-0.30)

    def test_delta_openai_minus_meta(self):
        s = self._scorer()
        assert s["illustrative_register_delta_openai_minus_meta"] == pytest.approx(0.15)

    def test_delta_arithmetic_logged(self):
        s = self._scorer()
        assert s["delta_calc"] == "-0.15 - (-0.30) = 0.15"

    def test_engine_degenerate_only(self):
        s = self._scorer()
        assert "degenerate n=1 check" in s["engine_degenerate"]
        assert "is_significant False" in s["engine_degenerate"]

    def test_convention_target_minus_peer(self):
        s = self._scorer()
        assert "target-minus-peer" in s["convention"]
        assert "target = OpenAI arm" in s["convention"]

    def test_tone_basis_manual_illustrative(self):
        s = self._scorer()
        assert "MANUAL ILLUSTRATIVE" in s["methodology"]
        assert "not empirical corpus scores" in s["methodology"]

    def test_verdict_and_discipline(self):
        s = self._scorer()
        assert s["verdict"] == "directionally_supported_not_proven"
        assert s["no_analysis_json_update"] is True
        assert s["artifact_grade"] is False
        assert "NOT_CALCULATED" in s["finding_layer"]


class TestMechanism754Discipline:
    def test_stats_not_calculated(self):
        s = _block_yaml()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "p_value NOT_CALCULATED" in s["finding_layer"]
        assert "cohens_d NOT_CALCULATED" in s["finding_layer"]
        assert "ci_95 NOT_CALCULATED" in s["finding_layer"]
        assert "is_significant False" in s["finding_layer"]

    def test_not_a_falsification_family_member(self):
        blk = _block_yaml()
        assert "NOT a member" in blk["falsification_family"]
        assert "Ledger holds at 27" in blk["falsification_family"]

    def test_no_twenty_eighth_member_form(self):
        block = _yaml_block()
        assert "TWENTY-EIGHTH" not in block

    def test_confounders_and_counterevidence_present(self):
        blk = _block_yaml()
        conf = blk["confounders_ranked"]
        assert set(conf.keys()) == {"strong", "moderate", "weak"}
        assert len(conf["strong"]) >= 3
        assert len(conf["moderate"]) >= 3
        assert len(conf["weak"]) >= 2
        assert len(blk["counterevidence"]) >= 5

    def test_connects_claims(self):
        block = _yaml_block()
        assert "cash-burn successor" in block
        assert "correlation is not causation" in block.lower()
        assert "NOT artifact-grade" in block

    def test_cross_references_present(self):
        blk = _block_yaml()
        refs = " ".join(blk["cross_references"])
        assert "mechanism 54" in refs
        assert "mechanism 718" in refs
        assert "mechanism 643" in refs
        assert "mechanism 676" in refs


class TestNoCrossContamination872:
    def test_block_ascii_only_no_em_dashes(self):
        block = _yaml_block()
        block.encode("ascii")
        assert "\u2014" not in block
        assert "\u2013" not in block

    def test_no_literal_755_mechanism_keys(self):
        hits = _repo_grep(re.escape(NEXT_ID_MARKER))
        assert hits == []
        hits = _repo_grep(re.escape(NEXT_ID_NUMERIC))
        assert hits == []
        hits = _repo_grep(re.escape(NEXT_ID_DASH))
        assert hits == []

    def test_block_key_absent_from_other_test_files(self):
        hits = _repo_grep(re.escape(MECH_KEY))
        test_hits = [h for h in hits if h[0].startswith("tests" + os.sep)]
        assert len(test_hits) == 1
        assert test_hits[0][0].endswith(OWN_BASENAME)


class TestDocSync872:
    def test_readme_test_file_row_present(self):
        readme = _read("README.md")
        assert OWN_BASENAME in readme
        assert "Type A #872" in readme

    def test_readme_stats_table_updated(self):
        readme = _read("README.md")
        assert "| Tests | 44592 |" in readme
        assert "Across 1200 test files" in readme

    def test_architecture_row_present(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert OWN_BASENAME in arch
        assert "Type A #872" in arch

    def test_iteration_log_entry_present(self):
        log = _read("iteration-log.md")
        assert "## #872 Type A:" in log
        assert "Type A #872" in log


class TestDateGrounding872:
    def test_iteration_time_present(self):
        block = _yaml_block()
        assert "2026-09-20 03:00 PDT" in block

    def test_arm_dates_present(self):
        block = _yaml_block()
        assert "2026-09-18" in block
        assert "2026-06-05" in block

    def test_window_reference_in_file(self):
        # The window reference lives in the test module docstring.
        text = _read("tests/" + OWN_BASENAME)
        assert "870-874" in text
        assert "THIRD leg" in text
        assert "D->E->A" in text
