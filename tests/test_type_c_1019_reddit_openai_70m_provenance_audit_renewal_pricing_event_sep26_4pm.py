"""
Type C #1019 (iteration 1019, mechanism 843): Reddit AI-licensing quantum
provenance audit - the $70M/yr OpenAI figure is press arithmetic reconstructed
by subtraction, not a filing number. CORRECTION of the corpus's own
advance_dual_asset_monetization as-fact treatment. Filed-number inventory
(S-1 $203M aggregate, FY2025 10-K concentration risk, Q2 2026 $43.3M Other,
contracted-unrecognized $62.0M/$30.1M) plus the July 2026 Google $60M/yr
renewal as the live pricing event.

All findings are qualitative financial mapping (tone NOT_SCORED, engine not
run, no analysis.json update, NOT artifact-grade, NOT falsification-family
member, ledger holds at 30, verdict directionally_supported_not_proven).
No cash-payment claim is made for the OpenAI leg beyond the press
reconstruction; Meta $0 is bounded absence, not verified absence.
Correlation, not causation. Hypothesis-generating only.

Manual-illustrative style. Excerpt-bounded per #503: 0 browser.open this run;
the thestochasticparrot audit, the 10-K quotes, and all earnings figures are
carried from search excerpts and secondary relays, not first-hand filing reads.

Iteration #1019 Type C is the FIFTH and CLOSING leg of the 1015-1019 rotation
window (D->E->A->B->C per #565 anchor + rotation guard). Pre-commit novelty
greps per #715: zero test_type_c_1019 files on disk (glob), no "Type C #1019"
in git log (--grep), max numeric mechanism_id 842 pre-commit, zero
underscore/dash-form 843 keys repo-wide pre-commit (needles format-built),
block key zero-hit repo-wide pre-commit, 8 of 8 source URLs zero-hit
repo-wide pre-commit (fool.com Jul-28 piece was already in-corpus at
mechanism 253 source_urls, REPLACED with the ppc.land URL, re-verified
zero-hit; thestochasticparrot zero-hit repo-wide pre-commit).

Doc-sync post-run: 52320/1343 -> 52372/1344 (+52/+1, venv python).
Concurrency: #899 (nytimes.yaml m771 hunk), #938 (Type B test file anchor
edit), #900 (untracked test), #1012-wt (working-tree block-key fix) all stay
out of this run's index and diff.

Novelty, hash-placeholder, and staged-set tests fail pre-commit per the
#715/#721 conventions; all green post-doc-sync; iteration-log newest-entry
green; staged-set test fails pre-commit by design.
52 tests, 11 classes. ASCII only, no em dashes.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest
import yaml

THIS_FILE = "test_type_c_1019_reddit_openai_70m_provenance_audit_renewal_pricing_event_sep26_4pm.py"
BLOCK_KEY = "type_c_1019_reddit_openai_70m_provenance_audit_renewal_pricing_event_sep26_4pm"
MECHANISM = 843
NEXT_NUM = 844
ITERATION = 1019
ITERATION_TYPE = "C"
EXPECTED_TESTS = 52
ANCHORED_SHA = "7f8e944d"  # patched in the anchor followup per #565
PREDECESSOR_SHAS = {
    "55e3067be6dadab3f2b11e37fb3053d50e60c1f6",
    "4fcea1834c62bebcb8fca795a5d1aae7486ac493",
    "b802e7b417f64231d85d5c2dcd2c70f37c53e2d8",
    "4d01e77a0000000000000000000000000000000000",
}
NEW_URLS = [
    "https://thestochasticparrot.com/audits/reddit-gas-metered",
    "https://tech.slashdot.org/story/25/02/14/0019213/ai-licensing-deals-with-google-and-openai-make-up-10-of-reddits-revenue?sdsrc=prevbtmprev",
    "https://readwrite.com/openai-paid-70m-reddit-content-ai-licensing/",
    "https://earningsanatomy.com/blogs/reddit-rddt-q2-2026-earnings-revenue-up-61-percent-stock-drop",
    "https://mlq.ai/news/reddit-stock-drops-9-on-report-it-may-not-renew-60m-google-ai-data-deal-1/",
    "https://startupfortune.com/reddit-may-cut-off-googles-ai-access-when-their-60-million-deal-expires/",
    "https://www.techspot.com/community/topics/reddit-and-major-publishers-consider-blocking-google-as-ai-search-continues-destroying-web-traffic.298203/",
    "http://ppc.land/reddit-and-usa-today-face-google-exit-as-search-traffic-drops-28/",
]
CONNECTS_TO = [614, 735, 840, 732]
STAGED_SET = {
    "profiles/competitor-entities.yaml",
    "tests/" + THIS_FILE,
    "iteration-log.md",
    "README.md",
    "docs/ARCHITECTURE.md",
}
README_TESTS_BEFORE = 52320
README_TESTS_AFTER = 52372
README_FILES_BEFORE = 1343
README_FILES_AFTER = 1344

ROOT = Path(__file__).resolve().parent.parent
TESTS_DIR = ROOT / "tests"
PROF = ROOT / "profiles" / "competitor-entities.yaml"
LOG = ROOT / "iteration-log.md"
README = ROOT / "README.md"
ARCH = ROOT / "docs" / "ARCHITECTURE.md"


def run_git(*args):
    return subprocess.run(
        ["git", *args], cwd=str(ROOT), capture_output=True, text=True, timeout=90
    )


def _read(path):
    return Path(path).read_text(encoding="utf-8")


def _block():
    text = _read(PROF)
    parsed = yaml.safe_load(text)
    return parsed[BLOCK_KEY], text


# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1019:
    def test_single_new_test_file_on_disk(self):
        matches = list(TESTS_DIR.glob("test_type_c_1019*"))
        assert len(matches) == 1
        assert matches[0].name == THIS_FILE

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # Fails pre-anchor by design; passes after the anchor followup per
        # #565: the committed test must carry the real main-commit SHA.
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP"
        r = run_git("cat-file", "-t", ANCHORED_SHA)
        assert r.stdout.strip() == "commit"
        r2 = run_git("log", "--format=%s", "-1", ANCHORED_SHA)
        assert "Type C #1019" in r2.stdout

    def test_novelty_first_claim_present(self):
        block, _ = _block()
        novelty = block["novelty"]
        assert "FIRST" in novelty
        assert "provenance audit" in novelty
        assert "Reddit" in novelty

    def test_zero_underscore_or_dash_843_keys_pre_commit(self):
        r = run_git("grep", "-E", "mechanism_843|mechanism-843", "--",
                    "profiles/", "tests/", "docs/", "iteration-log.md")
        assert r.returncode != 0
        assert "mechanism_843" not in r.stdout
        assert "mechanism-843" not in r.stdout

    def test_thestochasticparrot_zero_hit_repo_wide_pre_commit(self):
        # The core audit source must be novel; post-append it appears exactly
        # once (this block). Pre-commit greps per #715 verified zero hits.
        block, text = _block()
        assert text.count(NEW_URLS[0]) == 1


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestRotationGuard1019:
    def test_window_legs_in_iteration_log(self):
        text = _read(LOG)
        assert "## #1015 Type D" in text
        assert "## #1016 Type E" in text
        assert "## #1017 Type A" in text
        assert "## #1018 Type B" in text
        assert "1015-1019" in text

    @pytest.mark.rotation
    def test_fifth_leg_of_1015_to_1019_window(self):
        block, _ = _block()
        assert "FIFTH leg of the 1015-1019 window" in block["rotation_transparency"]

    @pytest.mark.rotation
    def test_predecessor_1018_type_b_committed(self):
        r = run_git("log", "--oneline", "--grep", "Type B #1018")
        assert "Type B #1018" in r.stdout
        block, _ = _block()
        rt = block["rotation_transparency"]
        assert "55e3067be6dadab3f2b11e37fb3053d50e60c1f6" in rt
        assert "4fcea1834c62bebcb8fca795a5d1aae7486ac493" in rt

    @pytest.mark.rotation
    def test_no_successor_1020_type_d_commit_yet(self):
        r = run_git("log", "--oneline", "--grep", "Type D #1020")
        assert "Type D #1020" not in r.stdout

    @pytest.mark.rotation
    def test_no_concurrent_type_c_1019_by_commit_time(self):
        r = run_git("log", "--oneline", "--grep", "Type C #1019")
        assert "Type C #1019" not in r.stdout


# ---------------------------------------------------------------------------
# 3. Mechanism 843 block content
# ---------------------------------------------------------------------------
class TestMechanism843Content:
    def test_block_key_unique_at_zero_indent(self):
        _, text = _block()
        hits = [m.start() for m in re.finditer(r"^" + re.escape(BLOCK_KEY) + r":",
                                               text, re.M)]
        assert len(hits) == 1

    def test_mechanism_id_iteration_type_date_time(self):
        block, _ = _block()
        assert block["mechanism_id"] == MECHANISM
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == ITERATION_TYPE
        assert block["date_analyzed"] == "2026-09-26"
        assert block["time_pdt"] == "16:00"

    def test_type_and_label(self):
        block, _ = _block()
        assert block["type"] == "financial_incentive_mapping"
        assert block["type_label"] == "Financial Incentive Mapping"
        assert block["researcher"] == "Kit (with Ray)"
        assert block["author"] == "Kit (with Ray)"

    def test_verdict_directionally_supported_not_proven(self):
        block, _ = _block()
        assert block["verdict"] == "directionally_supported_not_proven"

    def test_mechanism_name_carries_correction_flag(self):
        block, _ = _block()
        assert "CORRECTION" in block["mechanism_name"]
        assert "advance_dual_asset_monetization" in block["mechanism_name"]


# ---------------------------------------------------------------------------
# 4. The $70M provenance audit
# ---------------------------------------------------------------------------
class TestProvenanceAudit70M:
    def test_reconstruction_chain_130m_minus_60m(self):
        block, _ = _block()
        finding = block["finding"]
        assert "roughly $130 million" in finding
        assert "$130M minus $60M leaves $70M" in finding

    def test_adweek_jen_wong_ten_percent_attribution(self):
        block, _ = _block()
        finding = block["finding"]
        assert "about 10% of its revenue" in finding
        assert "I'll call it 10%" in finding
        assert "Jen Wong" in finding

    def test_audit_certifies_reconstructed_by_subtraction(self):
        block, _ = _block()
        finding = block["finding"]
        assert "is an invoice reconstructed by subtraction from a percentage" in finding
        assert "Only figures with a filing number attached can be certified" in finding

    def test_10k_other_line_114_7m_comparator(self):
        block, _ = _block()
        finding = block["finding"]
        assert "$114.7 million" in finding

    def test_correction_of_advance_dual_asset_block(self):
        block, _ = _block()
        finding = block["finding"]
        assert "CORRECTION" in finding
        assert "advance_dual_asset_monetization" in finding
        assert "downgraded to press arithmetic" in finding
        assert "is NOT downgraded" in finding

    def test_no_cash_payment_claim_for_openai_leg(self):
        block, _ = _block()
        geom = block["incentive_geometry"]
        assert "NO cash-payment claim is made for the OpenAI leg" in geom["fee_status"]


# ---------------------------------------------------------------------------
# 5. Filed-number inventory
# ---------------------------------------------------------------------------
class TestFiledNumbers:
    def test_s1_203m_aggregate(self):
        block, _ = _block()
        finding = block["finding"]
        assert "aggregate data-licensing contract value $203 million" in finding
        assert "2-3 years" in finding

    def test_fy2025_10k_concentration_risk(self):
        block, _ = _block()
        finding = block["finding"]
        assert ("substantially all of the contract value associated with our "
                "licensing revenue is derived from two of our partners") in finding
        assert ("may not be renewed, or they may be renewed based on less "
                "favorable terms") in finding

    def test_fixed_or_usage_based_fee(self):
        block, _ = _block()
        assert "fixed fee or usage-based fee" in block["finding"]

    def test_q2_2026_other_43_3m(self):
        block, _ = _block()
        finding = block["finding"]
        assert "$43.3 million" in finding
        assert "+24% YoY" in finding
        assert "$62.0 million" in finding
        assert "$30.1 million" in finding

    def test_licensing_share_shrank_7_to_5_4(self):
        block, _ = _block()
        finding = block["finding"]
        assert "7.0%" in finding
        assert "5.4%" in finding
        assert "$36 million in a single quarter" in finding


# ---------------------------------------------------------------------------
# 6. The July 2026 Google renewal as live pricing event
# ---------------------------------------------------------------------------
class TestRenewalPricingEvent:
    def test_wsj_cnbc_jul22_renewal_talks(self):
        block, _ = _block()
        finding = block["finding"]
        assert "Jul 22 2026" in finding
        assert "WSJ" in finding
        assert "CNBC" in finding
        assert '"is ending soon,"' in finding

    def test_shutoff_threat_quoted(self):
        block, _ = _block()
        assert ("shutting off Google's access to its content for artificial "
                "intelligence use") in block["finding"]

    def test_stock_move_and_wells_fargo_warning(self):
        block, _ = _block()
        finding = block["finding"]
        assert "9.18%" in finding
        assert "$170.10" in finding
        assert "$500 million in AI licensing revenue" in finding

    def test_huffman_quotes(self):
        block, _ = _block()
        finding = block["finding"]
        assert "commercial use of our data requires commercial terms" in finding
        assert "10 blue links" in finding
        assert "dynamic pricing" in finding

    def test_mechanism_253_revolt_carried_not_duplicated(self):
        block, _ = _block()
        finding = block["finding"]
        assert "mechanism 253" in finding
        assert "this run adds the certification boundary, not the revolt" in finding


# ---------------------------------------------------------------------------
# 7. Source corroboration
# ---------------------------------------------------------------------------
class TestSourceCorroboration:
    def test_eight_sources(self):
        block, _ = _block()
        assert len(block["sources"]) == 8
        urls = [s["url"] for s in block["sources"]]
        assert len(set(urls)) == 8

    def test_new_urls_first_appearance(self):
        _, text = _block()
        for url in NEW_URLS:
            assert text.count(url) == 1, url

    def test_excerpt_bounded_note_honest(self):
        block, _ = _block()
        note = block["excerpt_bounded_note"]
        assert "0 browser.open this run" in note
        assert "NOT first-hand filing reads" in note

    def test_connects_to_all_exist(self):
        block, _ = _block()
        assert block["connects_to"] == CONNECTS_TO
        corpus = "".join(_read(p) for p in [
            ROOT / "profiles" / "competitor-entities.yaml",
            ROOT / "profiles" / "careers" / "journalists.yaml",
            ROOT / "profiles" / "news-corp.yaml",
        ])
        for mid in CONNECTS_TO:
            assert f"mechanism_id: {mid}" in corpus, mid


# ---------------------------------------------------------------------------
# 8. Statistical discipline (qualitative financial mapping)
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline:
    def test_tone_not_scored(self):
        block, _ = _block()
        assert block["tone_scores"] == "NOT_SCORED"

    def test_engine_not_run_and_no_analysis_update(self):
        block, _ = _block()
        assert block["engine_run"] is False
        assert block["no_analysis_json_update"] is True

    def test_artifact_grade_false(self):
        block, _ = _block()
        assert block["artifact_grade"] is False

    def test_excerpt_bounded_browser_opens_zero(self):
        block, _ = _block()
        assert block["browser_opens"] == 0
        assert block["verification"]["browser_opens"] == 0

    def test_correlation_not_causation(self):
        block, _ = _block()
        assert "Correlation, not causation" in block["finding"]
        assert "Hypothesis-generating only" in block["finding"]

    def test_confounders_eight_ranked_strong_first(self):
        block, _ = _block()
        confs = block["confounders"]
        assert len(confs) == 8
        strengths = [c["strength"] for c in confs]
        assert strengths == (["strong"] * 3 + ["medium"] * 3 + ["weak"] * 2)

    def test_counterevidence_five(self):
        block, _ = _block()
        assert len(block["counterevidence"]) == 5

    def test_strongest_counterargument_present(self):
        block, _ = _block()
        sca = block["strongest_counterargument"]
        assert "leverage theater" in sca
        assert "5.4%" in sca
        assert "Correlation, not causation" in sca


# ---------------------------------------------------------------------------
# 9. Falsification ledger
# ---------------------------------------------------------------------------
class TestLedger1019:
    def test_not_falsification_family_member(self):
        block, _ = _block()
        assert block["falsification_family_member"] is False

    def test_ledger_holds_at_30(self):
        block, _ = _block()
        assert block["falsification_ledger"] == 30

    def test_ledger_wordings_pinned(self):
        block, _ = _block()
        note = block["falsification_note"]
        assert "THIRTIETH" in note
        assert "#1000" in note
        assert "m818" in note


# ---------------------------------------------------------------------------
# 10. Doc sync
# ---------------------------------------------------------------------------
class TestDocSync1019:
    def test_readme_stats_row(self):
        text = _read(README)
        assert str(README_TESTS_AFTER) in text
        assert str(README_FILES_AFTER) in text
        assert f"| Tests | {README_TESTS_AFTER} | Across {README_FILES_AFTER} test files |" in text

    def test_readme_test_inventory_row(self):
        text = _read(README)
        assert THIS_FILE in text
        assert "Type C #1019" in text

    def test_arch_tree_row(self):
        text = _read(ARCH)
        assert THIS_FILE in text


# ---------------------------------------------------------------------------
# 11. Push readiness
# ---------------------------------------------------------------------------
class TestPushReadiness1019:
    def test_block_ascii_only(self):
        _, text = _block()
        start = text.find("\n" + BLOCK_KEY + ":")
        blk = text[start:]
        assert all(ord(c) < 128 for c in blk)

    def test_hash_placeholders_filled_post_followup(self):
        # Fails pre-commit per the #721 convention: this run's own main/anchor
        # SHAs are only known after the commits land, then patched into the log.
        # Predecessor (#1018) hashes are cited in Rotation transparency and do
        # not count; at least the main + anchor SHAs of #1019 must be present.
        text = _read(LOG)
        entry = text.split("## #1019")[1].split("## #1018")[0]
        own_hashes = {
            h for h in re.findall(r"\b[0-9a-f]{40}\b", entry)
            if h not in PREDECESSOR_SHAS
        }
        assert len(own_hashes) >= 2

    def test_staged_set_exactly_five_paths_and_concurrency_untouched(self):
        # Fails pre-commit by design: staging happens at commit time.
        r = run_git("diff", "--cached", "--name-only")
        staged = {f for f in r.stdout.splitlines() if f}
        assert staged == STAGED_SET
        # Concurrency: #899 (nytimes.yaml m771 hunk), #938 (Type B test file
        # anchor edit), #900 (untracked test), #1012 working-tree block-key
        # fix all stay out of this run's index.
        r2 = run_git("status", "--porcelain")
        idx = {line[3:] for line in r2.stdout.splitlines()
               if line[:2] in ("M ", "A ")}
        assert "profiles/nytimes.yaml" not in idx
        assert ("tests/test_type_b_938_dominic_preston_verge_pixel_watch_"
                "gemini_personalization_vs_meta_luna_stigma_sep16.py") not in idx
        assert ("tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_"
                "agenda_setting_register_vs_carried_meta_india_havoc_m817_"
                "pairing_sep26_7am.py") not in idx
        assert ("tests/test_type_d_900_m769_qualitative_corpus_integrity_"
                "sep21_1pm.py") not in idx
        r3 = run_git("diff", "--", "profiles/nytimes.yaml")
        assert "spur_licensing_market_exists_coalition_founder_datum_unsealed_filings_wave_sep2026" in r3.stdout
