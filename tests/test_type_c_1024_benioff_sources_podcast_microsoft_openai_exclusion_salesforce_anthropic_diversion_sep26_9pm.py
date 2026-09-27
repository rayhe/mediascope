"""
Type C #1024 (iteration 1024, mechanism 846): FIRST exclusionary-diversion
geometry - Marc Benioff's own Sources Podcast disclosure (Alex Heath
interview, published the week of Sep 22 2026) that Microsoft's commercial
relationship with OpenAI blocked Salesforce from investing in OpenAI,
diverting ~$50M into Anthropic in 2023 (Series C, $4.1B pre-money), now
reported ~$5B, with $300M+ invested across later rounds, an expanded
Claudeforce partnership (Claude default in Slack/Slackbot), and a ~$300M/yr
Anthropic token-spend leg corroborated Sep 8 2026 by deputy CFO Mike
Spencer's margin-guidance remark. Extends mechanism 36
(salesforce_benioff_time): the Benioff-TIME owner-equity chain gains its
origin story - the equity position was CAUSED BY the Microsoft exclusion.
Also extends the corpus microsoft_openai_stake block with an exclusion
function beyond revenue share and Azure. NEW relationship direction:
FOURTEENTH per the m807 enumeration - EXCLUSIONARY-DIVERSION
(moat-diversion). Certification: Benioff-attributed, uncorroborated by
OpenAI/Microsoft; $5B reported-value not realized gain; "tens of billions"
is Benioff's own IPO projection; $1.3T private-market valuation single-
source and not adopted (corpus: $965B May raise, ~$2T IPO target).

All findings are qualitative financial mapping (tone NOT_SCORED, engine not
run, no analysis.json update, NOT artifact-grade, NOT falsification-family
member, ledger holds at 30, verdict directionally_supported_not_proven).
Correlation, not causation. Hypothesis-generating only.

Manual-illustrative style. Excerpt-bounded per #503: 0 browser.open this run;
the podcast quotes, investment figures, and token-spend corroboration are
carried from search excerpts and secondary relays, not first-hand audio
review or filing reads.

Iteration #1024 Type C is the FIFTH and CLOSING leg of the 1020-1024
rotation window (D->E->A->B->C per #565 anchor + rotation guard). Pre-commit
novelty greps per #715: zero test_type_c_1024 files on disk (glob), no
"Type C #1024" in git log (--grep), max numeric mechanism_id 845
pre-commit, zero underscore/dash-form 846 keys repo-wide pre-commit
(needles format-built), block key zero-hit repo-wide pre-commit, 8 of 8
source URLs zero-hit repo-wide pre-commit.

Doc-sync post-run: 52566/1348 -> 52619/1349 (+53/+1, venv python).
Concurrency: #899 (nytimes.yaml m771 hunk), #938 (Type B test file anchor
edit), #900 (untracked test), #1012 working-tree block-key fix all stay out
of this run's index and diff.

Novelty anchor, rotation-guard, hash-placeholder, staged-set, and doc-sync
tests fail pre-commit per the #565/#715/#719/#721 conventions; all green
post-doc-sync; iteration-log newest-entry green.

53 tests, 11 classes. ASCII only, no em dashes.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest
import yaml

THIS_FILE = "test_type_c_1024_benioff_sources_podcast_microsoft_openai_exclusion_salesforce_anthropic_diversion_sep26_9pm.py"
BLOCK_KEY = "type_c_1024_benioff_sources_podcast_microsoft_openai_exclusion_salesforce_anthropic_diversion_sep26_9pm"
MECHANISM = 846
ITERATION = 1024
ITERATION_TYPE = "C"
EXPECTED_TESTS = 53
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # patched in the anchor followup per #565
PREDECESSOR_SHAS = {
    "af7c36a36ee956a34efe6c9d7b50f3e5e4899461",
    "b4a2f7af90321287a51c8686f26bcad145f9cd5b",
    "58060cec7b3a5d4ba0516dba6c3d020662ebe893",
}
NEW_URLS = [
    "https://sources.news/p/marc-benioff-ai-boom-saaspocalypse",
    "https://www.livemint.com/companies/news/salesforce-missed-openai-its-50-million-anthropic-bet-is-now-worth-5-billion-11790164533797.html",
    "https://finance.biggo.com/news/4a8b410c-400f-4d05-bcbf-bc75422fc757",
    "https://particle.news/story/benioff-says-microsoft-ties-blocked-salesforce-from-openai-and-sent-it-to-anthropic",
    "https://www.tradingview.com/news/stocktwits:675c68c07094b:0-marc-benioff-says-microsoft-shut-salesforce-out-of-openai-so-he-bet-on-anthropic-instead-and-it-could-pay-tens-of-billions/",
    "https://www.techloy.com/marc-benioff-says-salesforce-will-spend-300-million-on-anthropic-tokens-this-year/",
    "https://finance.biggo.com/news/e474ac2f-4a1d-49c9-bda8-68b3d79f807d",
    "https://technologymagazine.com/news/salesforce-plans-to-spend-us-300m-on-anthropic-ai-tokens",
]
CONNECTS_TO = [36, 729, 735, 837]
STAGED_SET = {
    "profiles/competitor-entities.yaml",
    "tests/" + THIS_FILE,
    "iteration-log.md",
    "README.md",
    "docs/ARCHITECTURE.md",
}
README_TESTS_BEFORE = 52566
README_TESTS_AFTER = 52619
README_FILES_BEFORE = 1348
README_FILES_AFTER = 1349

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
class TestNovelty1024:
    def test_single_new_test_file_on_disk(self):
        matches = list(TESTS_DIR.glob("test_type_c_1024*"))
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
        assert "Type C #1024" in r2.stdout

    def test_novelty_first_claim_present(self):
        block, _ = _block()
        novelty = block["novelty"]
        assert "FIRST" in novelty
        assert "exclusionary-diversion" in novelty
        assert "Benioff" in novelty

    def test_zero_underscore_or_dash_846_keys_pre_commit(self):
        # Needle built by concatenation so this file's own source never
        # contains the literal (else git grep self-matches post-commit).
        # Underscore/dash 846 key forms must never exist; the numeric
        # mechanism_id: 846 is legitimately claimed by this run's block.
        needle = "mechanism" + "_846|mechanism" + "-846"
        r = run_git("grep", "-E", needle, "--",
                    "profiles/", "tests/", "docs/", "iteration-log.md")
        hits = [line for line in r.stdout.splitlines()
                if "test_zero_underscore_or_dash_846_keys_pre_commit" not in line]
        assert hits == []

    def test_sources_news_zero_hit_repo_wide_pre_commit(self):
        # The core primary-source writeup must be novel; post-append it
        # appears exactly once (this block). Pre-commit greps per #715
        # verified zero hits.
        block, text = _block()
        assert text.count(NEW_URLS[0]) == 1


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestRotationGuard1024:
    def test_window_legs_in_iteration_log(self):
        text = _read(LOG)
        assert "## #1020 Type D" in text
        assert "## #1021 Type E" in text
        assert "## #1022 Type A" in text
        assert "## #1023 Type B" in text
        assert "1020-1024" in text

    @pytest.mark.rotation
    def test_fifth_leg_of_1020_to_1024_window(self):
        block, _ = _block()
        assert "FIFTH leg of the 1020-1024 window" in block["rotation_transparency"]

    @pytest.mark.rotation
    def test_predecessor_1023_type_b_committed(self):
        r = run_git("log", "--oneline", "--grep", "Type B #1023")
        assert "Type B #1023" in r.stdout
        block, _ = _block()
        rt = block["rotation_transparency"]
        assert "Lucas Ropek" in rt
        assert "mechanism 845" in rt

    @pytest.mark.rotation
    def test_no_successor_1025_type_d_commit_yet(self):
        r = run_git("log", "--oneline", "--grep", "Type D #1025")
        assert "Type D #1025" not in r.stdout

    @pytest.mark.rotation
    def test_no_concurrent_type_c_1024_by_commit_time(self):
        # Own commits (touching this test file) are excluded per the #1018
        # convention: the guard is about a racing iteration, not this run.
        r = run_git("log", "--format=%H %s", "--grep", "Type C #1024")
        matches = [line for line in r.stdout.splitlines() if line.strip()]
        own = run_git(
            "log", "--format=%H", "--", "tests/" + THIS_FILE
        ).stdout.split()
        competing = [
            line for line in matches
            if line.split()[0] not in own
        ]
        assert competing == []


# ---------------------------------------------------------------------------
# 3. Mechanism 846 block content
# ---------------------------------------------------------------------------
class TestMechanism846Content:
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
        assert block["time_pdt"] == "21:00"

    def test_type_and_label(self):
        block, _ = _block()
        assert block["type"] == "financial_incentive_mapping"
        assert block["type_label"] == "Financial Incentive Mapping"
        assert block["researcher"] == "Kit (with Ray)"
        assert block["author"] == "Kit (with Ray)"

    def test_verdict_directionally_supported_not_proven(self):
        block, _ = _block()
        assert block["verdict"] == "directionally_supported_not_proven"

    def test_fourteenth_direction_exclusionary_diversion(self):
        block, _ = _block()
        tax = block["relationship_direction_taxonomy"]
        assert "FOURTEENTH" in tax["direction_number"]
        assert tax["direction_name"] == "EXCLUSIONARY-DIVERSION (moat-diversion)"
        assert "deal-blocking asset" in tax["definition"]

    def test_mechanism_name_carries_diversion_flag(self):
        block, _ = _block()
        assert "exclusionary-diversion" in block["mechanism_name"]
        assert "Sources Podcast" in block["mechanism_name"]


# ---------------------------------------------------------------------------
# 4. The exclusion event
# ---------------------------------------------------------------------------
class TestExclusionEvent:
    def test_venue_and_speaker(self):
        block, _ = _block()
        ev = block["exclusion_event"]
        assert "Sources podcast" in ev["venue"]
        assert "Alex Heath" in ev["venue"]
        assert "Marc Benioff" in ev["speaker"]
        assert "TIME owner" in ev["speaker"]

    def test_verbatim_quote_carried(self):
        block, _ = _block()
        ev = block["exclusion_event"]
        assert "because of the Microsoft relationship" in ev["verbatim"]
        assert "we were not allowed to invest in OpenAI" in ev["verbatim"]

    def test_blocking_asset_is_microsoft_stake(self):
        block, _ = _block()
        ev = block["exclusion_event"]
        assert "27%" in ev["blocking_asset"]
        assert "$250B" in ev["blocking_asset"]
        assert "microsoft_openai_stake" in ev["blocking_asset"]

    def test_certification_benioff_attributed(self):
        block, _ = _block()
        assert "Benioff-attributed" in block["exclusion_event"]["certification"]
        assert "no OpenAI or Microsoft corroboration" in block["exclusion_event"]["certification"]

    def test_m807_enumeration_reference(self):
        block, _ = _block()
        assert "m807 enumeration" in block["finding"]


# ---------------------------------------------------------------------------
# 5. The diversion investment
# ---------------------------------------------------------------------------
class TestDiversionInvestment:
    def test_initial_50m_at_4_1b(self):
        block, _ = _block()
        inv = block["diversion_investment"]
        assert "$50M" in inv["initial"]
        assert "$4.1B" in inv["initial"]
        assert "2023" in inv["initial"]

    def test_cumulative_300m_plus(self):
        block, _ = _block()
        assert "$300M+" in block["diversion_investment"]["cumulative"]

    def test_current_value_5b_reported_not_realized(self):
        block, _ = _block()
        cv = block["diversion_investment"]["reported_current_value"]
        assert "$5B" in cv
        assert "not realized gain" in cv

    def test_tens_of_billions_is_benioff_claim(self):
        block, _ = _block()
        ip = block["diversion_investment"]["ipo_projection"]
        assert "tens of billions" in ip
        assert "Benioff" in ip

    def test_claudeforce_operationalization(self):
        block, _ = _block()
        op = block["diversion_investment"]["operationalization"]
        assert "Claudeforce" in op
        assert "Slack" in op
        assert "Slackbot" in op

    def test_owner_equity_chain_extends_m36(self):
        block, _ = _block()
        chain = block["owner_equity_chain"]
        assert "mechanism 36" in chain["base"]
        assert "salesforce_benioff_time" in chain["base"]
        assert "TIME -> owner Marc Benioff -> Salesforce" in chain["chain"]
        assert "CAUSED BY the Microsoft exclusion" in chain["new_from_this_run"]


# ---------------------------------------------------------------------------
# 6. The demand-side leg
# ---------------------------------------------------------------------------
class TestDemandSideLeg:
    def test_300m_2026_projection(self):
        block, _ = _block()
        leg = block["demand_side_leg"]
        assert "$300M" in leg["projection_2026"]
        assert "2026" in leg["projection_2026"]
        assert "All-In podcast" in leg["projection_2026"]

    def test_spencer_cfo_corroboration(self):
        block, _ = _block()
        leg = block["demand_side_leg"]
        assert "Mike Spencer" in leg["cfo_corroboration"]
        assert "Deutsche Bank" in leg["cfo_corroboration"]
        assert "margin guidance" in leg["cfo_corroboration"]

    def test_three_part_stack_geometry(self):
        block, _ = _block()
        leg = block["demand_side_leg"]
        assert "equity leg" in leg["geometry"]
        assert "product leg" in leg["geometry"]
        assert "recurring-revenue leg" in leg["geometry"]


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
        assert "NOT first-hand audio review" in note

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

    def test_certification_boundaries_present(self):
        block, _ = _block()
        cb = block["certification_boundaries"]
        assert "Benioff's" in cb
        assert "$1.3 trillion" in cb
        assert "$965B" in cb
        assert "does not adopt it" in cb

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
        assert "retrospective framing" in sca
        assert "SaaSpocalypse" in sca
        assert "unfalsifiable from outside" in sca
        assert "Correlation, not causation" in sca


# ---------------------------------------------------------------------------
# 9. Falsification ledger
# ---------------------------------------------------------------------------
class TestLedger1024:
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
class TestDocSync1024:
    def test_readme_stats_row(self):
        text = _read(README)
        assert str(README_TESTS_AFTER) in text
        assert str(README_FILES_AFTER) in text
        assert f"| Tests | {README_TESTS_AFTER} | Across {README_FILES_AFTER} test files |" in text

    def test_readme_test_inventory_row(self):
        text = _read(README)
        assert THIS_FILE in text
        assert "Type C #1024" in text

    def test_arch_tree_row(self):
        text = _read(ARCH)
        assert THIS_FILE in text


# ---------------------------------------------------------------------------
# 11. Push readiness
# ---------------------------------------------------------------------------
class TestPushReadiness1024:
    def test_block_ascii_only(self):
        _, text = _block()
        start = text.find("\n" + BLOCK_KEY + ":")
        blk = text[start:]
        assert all(ord(c) < 128 for c in blk)

    def test_test_file_ascii_only(self):
        text = _read(TESTS_DIR / THIS_FILE)
        assert all(ord(c) < 128 for c in text)

    def test_hash_placeholders_filled_post_followup(self):
        # Fails pre-commit per the #721 convention: this run's own main/anchor
        # SHAs are only known after the commits land, then patched into the
        # log. Predecessor (#1023) hashes are cited in the entry and do not
        # count; at least the main + anchor SHAs of #1024 must be present.
        text = _read(LOG)
        entry = text.split("## #1024")[1].split("## #1023")[0]
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
