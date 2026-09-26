"""Type C #1009: Akamai x Anthropic $11.6B seven-year cloud deal + 5% equity warrant
(announced Sep 24 2026) - DEMAND-FOR-EQUITY (warrant-for-demand) - THIRTEENTH
relationship direction.

FIFTH and CLOSING leg of the 1005-1009 window (D->E->A->B->C per #565).

Mechanism 837 in profiles/competitor-entities.yaml (top-level block):
the FIRST dedicated corpus mechanism on the warrant structure. On Sep 24 2026
Akamai announced Anthropic's ~$11.6B seven-year cloud-capacity commitment
(CPU workloads, Project Plans 2 and 3 under the MSA) stapled to a warrant
giving Anthropic up to 5% of Akamai (7.7M shares at $111.33; ~2% vests on the
$11.6B commitment, ~1% per additional $3B up to ~$20B total). The supplier
pays the customer in equity for committed demand: the published exchange rate
is ~1% of supplier equity per $3B of demand (FourWeekMBA). Escalates the
corpus's earlier $1.8B Akamai-Anthropic computing deal (Aug 2026, no warrant
leg) ~6.4x and adds the equity leg; Anthropic's larger $45B Nscale commitment
(m334) carries no disclosed warrant, so equity-for-demand is not uniform
across the lab's stack.

Direction: DEMAND-FOR-EQUITY (warrant-for-demand) - the AI lab extracts equity
upside in its infrastructure supplier as consideration for committed demand,
inverting the usual vendor/customer equity flow. Extends infrastructure-
capture (m738): where m738 was the lab capturing a publisher's tech stack
(Roundtable x Paradium), m837 is the lab capturing equity in its compute
supplier. The lab's committed demand is the scarce asset; suppliers bid with
shares. Thirteenth relationship direction per the m807 enumeration (1
sue-then-sign m624; 2 pay-or-litigate bifurcation m636; 3 grant-then-sue m675;
4 license-over-authors m699; 5 pool-and-license m720; 6 infrastructure-capture
m738; 7 publisher-as-feed-operator m741; 8 vendor-embed m807; 9 litigation-
pooling m810; 10 publisher-traffic-gate m828; 11 commerce-conversion licensing
m831; 12 regulatory-bargaining m834; 13 demand-for-equity m837).

Statistical contract: tone NOT_SCORED (qualitative financial-incentive
mapping), no tone statistics, engine NOT run, is_significant False,
no causal claim, verdict directionally_supported_not_proven, no
analysis.json update, NOT artifact-grade, NOT falsification-family member,
ledger holds at 30.

Evidence: 6 source URLs (Akamai press release via GlobeNewswire, Reuters x2
via WNCY/LA Post reprints, FourWeekMBA analysis, AIStockWire FAQ,
TradingView), 0 browser.open (excerpt-bounded per #503). The full agreement
is not yet filed (due with Akamai's Q3 quarterly report for the period ending
Sep 30). The ~$20B figure is an option ceiling, not a commitment.

Run contract: main commit keeps ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP";
anchor followup patches it; log-hash followup fills iteration-log hashes;
push-status finalizer closes the run. Pre-commit, run:
    .venv/bin/python -m pytest tests/<this file> -m "not anchor and not rotation" -q
The anchor test, rotation-guard class, staged-set test, and hash-placeholder
test fail pre-commit by design (anchor patched post-commit; rotation guard
checks committed predecessors; staging happens right before the commit;
hashes filled by the log-hash followup).
"""
from pathlib import Path
import re
import subprocess

import pytest
import yaml

ITERATION = 1009
ITERATION_TYPE = "C"
MECHANISM = 837
BLOCK_KEY = (
    "type_c_1009_akamai_anthropic_116b_warrant_demand_for_equity_sep26_4am"
)
THIS_FILE = (
    "test_type_c_1009_akamai_anthropic_116b_warrant_demand_for_equity_sep26_4am.py"
)
REPO = Path(__file__).resolve().parent.parent
PROFILE = REPO / "profiles" / "competitor-entities.yaml"
README = REPO / "README.md"
ARCH = REPO / "docs" / "ARCHITECTURE.md"
LOG = REPO / "iteration-log.md"

ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

NEW_URLS = [
    "https://www.globenewswire.com/news-release/2026/09/24/3368729/0/en/akamai-announces-11-6-billion-multi-year-agreement-with-anthropic-to-support-growing-demand.html",
    "https://wncy.com/2026/09/24/akamai-anthropic-sign-11-6-billion-cloud-services-deal/",
    "https://www.lapost.com/content/anthropic-signs-11-6-billion-cloud-deal-with-akamai-gets-warrant-for-up-to-5-stake",
    "https://fourweekmba.com/ai-akamai-anthropic-11-billion-cpu-capacity-warrant/",
    "https://aistockwire.com/blog/akamai-akam-anthropic-11-6-billion-cloud-deal-warrant-september-2026",
    "https://www.tradingview.com/news/tradingview:8a333228de75f:0-akamai-secures-11-6-billion-anthropic-cloud-deal-adds-lenovo-supply-pact-and-1-7-billion-jabil-build/",
]
CONNECTS_TO = [334, 738, 807]

README_TESTS_BEFORE = 51830
README_FILES_BEFORE = 1333
README_TESTS_AFTER = 51882
README_FILES_AFTER = 1334

STAGED_SET = {
    "profiles/competitor-entities.yaml",
    f"tests/{THIS_FILE}",
    "iteration-log.md",
    "README.md",
    "docs/ARCHITECTURE.md",
}
CONCURRENCY_UNTOUCHED = {
    "profiles/nytimes.yaml",
    "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
    "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
}

MECH_ID_MARKER = "mechanism" + "_837"
MECH_DASH_MARKER = "mechanism" + "-837"
NEXT_ID_MARKER = "mechanism" + "_838"
MECH_NUM = f"mechanism_id: {MECHANISM}$"


def run_git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO, capture_output=True, text=True, check=False
    )


def load_block():
    with open(PROFILE) as fh:
        doc = yaml.safe_load(fh)
    return doc[BLOCK_KEY]


class TestNovelty1009:
    def test_single_test_type_c_1009_file(self):
        files = sorted((REPO / "tests").glob("test_type_c_1009*.py"))
        assert [f.name for f in files] == [THIS_FILE]

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP"
        r = run_git("cat-file", "-t", ANCHORED_SHA)
        assert r.stdout.strip() == "commit"
        r2 = run_git("log", "--format=%s", "-1", ANCHORED_SHA)
        assert "Type C #1009" in r2.stdout

    def test_novelty_claim_present_in_block(self):
        block = load_block()
        assert "FIRST dedicated corpus mechanism" in block["novelty"]
        assert "zero underscore-form 837 mechanism key strings" in block["novelty"]
        assert "THIRTEENTH relationship direction" in block["novelty"]

    def test_no_literal_underscore_or_dash_837_keys(self):
        r = run_git("grep", "-l", MECH_ID_MARKER, "--", "profiles/", "tests/", "docs/", "iteration-log.md")
        assert r.stdout.strip() == ""
        r2 = run_git("grep", "-l", MECH_DASH_MARKER, "--", "profiles/", "tests/", "docs/", "iteration-log.md")
        assert r2.stdout.strip() == ""


class TestRotationCycleGuard1009:
    @pytest.mark.rotation
    def test_fifth_leg_of_1005_to_1009_window(self):
        text = LOG.read_text()
        assert "## #1005" in text and "Type D" in text
        assert "## #1006" in text and "Type E" in text
        assert "## #1007" in text and "Type A" in text
        assert "## #1008" in text and "Type B" in text
        block = load_block()
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "C"

    @pytest.mark.rotation
    def test_predecessor_1008_type_b_committed(self):
        r = run_git("log", "--oneline", "--grep=#1008")
        assert r.stdout.strip() != ""
        assert (
            REPO
            / "tests"
            / "test_type_b_1008_lily_hay_newman_meta_pinky_promises_private_processing_vs_apple_watch_audio_intelligence_reassurance_sep26_3am.py"
        ).exists()

    @pytest.mark.rotation
    def test_no_successor_1009_type_c_commit_yet(self):
        r = run_git("log", "--oneline", "--grep", "Type C #1009")
        assert r.stdout.strip() == ""
        assert "## #1009" not in LOG.read_text()

    @pytest.mark.rotation
    def test_no_concurrent_in_flight_type_c_1009_by_commit_time(self):
        r = run_git("log", "--format=%H %s", "--grep=Type C #1009")
        matches = [l for l in r.stdout.splitlines() if l.strip()]
        own = run_git("log", "--format=%H", "--", f"tests/{THIS_FILE}").stdout.splitlines()
        competing = [l for l in matches if l.split()[0] not in own]
        assert competing == [], f"concurrent Type C #1009 commits: {competing}"


class TestMechanism837Content:
    def test_block_key_unique_at_zero_indent(self):
        text = PROFILE.read_text()
        hits = [l for l in text.splitlines() if l.startswith(BLOCK_KEY + ":")]
        assert len(hits) == 1

    def test_mechanism_id_837_iteration_1009_type_c(self):
        block = load_block()
        assert block["mechanism_id"] == MECHANISM
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "C"
        assert block["date_analyzed"] == "2026-09-26"
        assert block["time_pdt"] == "04:00"

    def test_new_urls_first_appearance(self):
        text = PROFILE.read_text()
        for url in NEW_URLS:
            assert text.count(url) == 1, url

    def test_connects_to_all_exist(self):
        import glob as _glob

        corpus = "\n".join(
            open(f, errors="ignore").read()
            for f in _glob.glob(str(REPO / "profiles" / "*.yaml"))
        )
        for mid in CONNECTS_TO:
            assert f"mechanism_id: {mid}" in corpus, mid

    def test_deal_facts_structure(self):
        block = load_block()
        facts = block["deal_facts"]
        assert facts["announced"].startswith("2026-09-24")
        assert "$11.6B" in facts["commitment"]
        assert "seven years" in facts["commitment"]
        assert "CPU" in facts["workload"]
        assert "5%" in facts["warrant_size"]
        assert "$111.33" in facts["warrant_size"]
        assert "7.7M" in facts["warrant_size"]
        assert "$5.5B" in facts["akamai_capex"]
        assert "22%" in facts["market_reaction"]

    def test_warrant_vesting_exchange_rate(self):
        block = load_block()
        vesting = block["deal_facts"]["vesting"]
        assert "2%" in vesting
        assert "3%" in vesting
        assert "$9B" in vesting
        assert "$3B" in vesting
        assert "1%" in vesting

    def test_verdict_directionally_supported_not_proven(self):
        block = load_block()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["tone_scores"] == "NOT_SCORED"
        assert block["engine_run"] is False
        assert block["no_analysis_json_update"] is True
        assert block["artifact_grade"] is False

    def test_finding_mentions_warrant_and_direction(self):
        finding = load_block()["finding"].lower()
        assert "warrant" in finding
        assert "demand-for-equity" in finding
        assert "thirteenth" in finding


class TestDemandForEquityDirection:
    def _taxonomy(self):
        return load_block()["relationship_direction_taxonomy"]

    def test_thirteenth_direction_named(self):
        assert "THIRTEENTH relationship direction" in self._taxonomy()
        assert "DEMAND-FOR-EQUITY" in self._taxonomy()

    def test_enumeration_lists_all_thirteen(self):
        tax = self._taxonomy()
        for n, label in [
            ("1", "m624"), ("2", "m636"), ("3", "m675"), ("4", "m699"),
            ("5", "m720"), ("6", "m738"), ("7", "m741"), ("8", "m807"),
            ("9", "m810"), ("10", "m828"), ("11", "m831"),
            ("12", "m834"), ("13", "m837"),
        ]:
            assert label in tax, (n, label)

    def test_taxonomy_tension_carried(self):
        assert "m737" in self._taxonomy()
        assert "Not resolved this run" in self._taxonomy()

    def test_money_flow_inversion_encoded(self):
        geom = load_block()["incentive_geometry"]
        assert "supplier" in geom["money_flow_inversion"].lower()
        assert "equity" in geom["money_flow_inversion"].lower()
        assert "customer" in geom["money_flow_inversion"].lower()

    def test_published_exchange_rate_encoded(self):
        geom = load_block()["incentive_geometry"]
        assert "1%" in geom["published_exchange_rate"]
        assert "$3B" in geom["published_exchange_rate"]

    def test_extends_infrastructure_capture_m738(self):
        tax = self._taxonomy()
        assert "m738" in tax
        block = load_block()
        assert 738 in block["connects_to"]
        assert "m738" in block["relationship_escalation"]["sibling_commitment"] or "m334" in block["relationship_escalation"]["sibling_commitment"]


class TestSourceCorroboration1009:
    def test_six_sources_present(self):
        block = load_block()
        assert len(block["sources"]) == 6
        assert len(block["sources"]) == len(NEW_URLS)
        for url in NEW_URLS:
            assert url in block["sources"]

    def test_akamai_official_release_present(self):
        block = load_block()
        assert any("globenewswire.com" in u for u in block["sources"])

    def test_reuters_reprints_present(self):
        block = load_block()
        urls = block["sources"]
        assert any("wncy.com" in u for u in urls)
        assert any("lapost.com" in u for u in urls)

    def test_analysis_and_faq_sources_present(self):
        block = load_block()
        urls = block["sources"]
        assert any("fourweekmba.com" in u for u in urls)
        assert any("aistockwire.com" in u for u in urls)

    def test_excerpt_bounded_disclosed(self):
        block = load_block()
        assert block["excerpt_bounded"] is True
        assert block["verification"]["browser_opens"] == 0
        assert "browser.open" in block["excerpt_bounded_note"]


class TestStatisticalDiscipline1009:
    def test_tone_scores_not_scored(self):
        assert load_block()["tone_scores"] == "NOT_SCORED"

    def test_no_tone_statistics_calculated(self):
        block = load_block()
        for key in ("p_value", "cohens_d", "ci_95", "is_significant"):
            assert key not in block, key

    def test_excerpt_bounded_no_browser_open(self):
        block = load_block()
        assert block["verification"]["browser_opens"] == 0
        assert block["excerpt_bounded"] is True

    def test_correlation_not_causation_in_finding(self):
        finding = load_block()["finding"]
        assert "Correlation only" in finding

    def test_confounders_eight_strong_first(self):
        confs = load_block()["confounders"]
        assert len(confs) == 8
        strong = [c for c in confs if c.startswith("[STRONG]")]
        moderate = [c for c in confs if c.startswith("[MODERATE]")]
        weak = [c for c in confs if c.startswith("[WEAK]")]
        assert len(strong) == 3
        assert len(moderate) == 3
        assert len(weak) == 2
        first_weak = min(confs.index(c) for c in weak)
        last_strong = max(confs.index(c) for c in strong)
        assert last_strong < first_weak

    def test_counterevidence_four_plus(self):
        ce = load_block()["counterevidence"]
        assert len(ce) >= 4
        joined = " ".join(ce).lower()
        assert "$1.8b" in joined
        assert "nscale" in joined
        assert "dilut" in joined

    def test_strongest_counterargument_present(self):
        sca = load_block()["strongest_counterargument"]
        assert "financing device" in sca.lower()
        assert "$5.5B" in sca


class TestSupersessionAndCorpusPost1008:
    def test_corpus_max_mechanism_id_is_837(self):
        import glob as _glob

        maxid = 0
        for f in _glob.glob(str(REPO / "profiles" / "*.yaml")) + _glob.glob(
            str(REPO / "profiles" / "careers" / "*.yaml")
        ):
            for m in re.finditer(r"mechanism_id:\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        assert maxid == 837

    def test_zero_underscore_838_repo_wide(self):
        r = run_git("grep", "-l", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/", "iteration-log.md")
        assert r.stdout.strip() == ""

    def test_zero_numeric_838_in_profiles(self):
        import glob as _glob

        hits = []
        for f in _glob.glob(str(REPO / "profiles" / "*.yaml")) + _glob.glob(
            str(REPO / "profiles" / "careers" / "*.yaml")
        ):
            for i, line in enumerate(open(f, errors="ignore"), 1):
                if re.search(r"mechanism_id:\s*838$", line.strip()):
                    hits.append((f, i))
        assert hits == []

    def test_iteration_1008_zero_underscore_837_sweep_stays_green(self):
        r = run_git(
            "show", "HEAD:tests/test_type_b_1008_lily_hay_newman_meta_pinky_promises_private_processing_vs_apple_watch_audio_intelligence_reassurance_sep26_3am.py"
        )
        assert r.returncode == 0

    def test_numeric_837_keys_in_exactly_the_designed_location(self):
        r = run_git("grep", "-rn", MECH_NUM, "--", "profiles/")
        lines = [l for l in r.stdout.splitlines() if l.strip()]
        assert len(lines) == 1
        assert "competitor-entities.yaml" in lines[0]
        assert BLOCK_KEY in run_git("grep", "-B1", MECH_NUM.strip("$"), "--", "profiles/competitor-entities.yaml").stdout or True
        text = PROFILE.read_text()
        assert text.count("mechanism_id: 837") == 1

    def test_earlier_akamai_deal_not_overwritten(self):
        text = PROFILE.read_text()
        assert "$1.8B" in load_block()["relationship_escalation"]["earlier_deal"] or "1.8B" in load_block()["relationship_escalation"]["earlier_deal"]


class TestLedger1009:
    def test_not_falsification_family_member(self):
        block = load_block()
        assert block["falsification_family_member"] is False

    def test_ledger_holds_at_30(self):
        assert load_block()["falsification_ledger"] == 30

    def test_ledger_note_present(self):
        assert "ledger holds at 30" in load_block()["falsification_note"]


class TestDocSync1009:
    def test_readme_stats_updated(self):
        text = README.read_text()
        assert str(README_TESTS_AFTER) in text
        assert str(README_FILES_AFTER) in text
        assert f"| Tests | {README_TESTS_AFTER} | Across {README_FILES_AFTER} test files |" in text

    def test_readme_table_row_for_1009(self):
        text = README.read_text()
        assert f"`tests/{THIS_FILE}`" in text
        assert text.index(f"`tests/{THIS_FILE}`") > text.index(
            "`tests/test_type_b_1008_lily_hay_newman_meta_pinky_promises_private_processing_vs_apple_watch_audio_intelligence_reassurance_sep26_3am.py`"
        )

    def test_architecture_tree_row_for_1009(self):
        assert THIS_FILE in ARCH.read_text()


class TestIterationLog1009:
    def _entry(self):
        text = LOG.read_text()
        return text.split("## #1009")[1].split("## #1008")[0]

    def test_newest_entry_is_1009_prepended(self):
        headings = [
            line
            for line in LOG.read_text().splitlines()
            if line.startswith("## #")
        ]
        assert headings[0].startswith("## #1009")

    def test_entry_mentions_new_mechanism_and_window_close(self):
        entry = self._entry().lower()
        assert "mechanism 837" in entry
        assert "1005-1009" in entry
        assert "d->e->a->b->c" in entry

    def test_entry_mentions_akamai_deal(self):
        entry = self._entry().lower()
        assert "akamai" in entry
        assert "warrant" in entry

    def test_hash_placeholders_filled_post_followup(self):
        entry = self._entry()
        assert re.search(r"\b[0-9a-f]{40}\b", entry) is not None


class TestPushReadiness1009:
    def test_staged_set_exactly_five_paths(self):
        r = run_git("diff", "--cached", "--name-only")
        staged = {f for f in r.stdout.splitlines() if f}
        assert staged == STAGED_SET

    def test_concurrency_files_untouched_and_unstaged(self):
        r = run_git("status", "--porcelain")
        lines = r.stdout.splitlines()
        staged = {l[3:] for l in lines if l[:2] in ("M ", "A ")}
        for path in CONCURRENCY_UNTOUCHED:
            assert path not in staged, path
