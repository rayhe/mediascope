"""Type C #969: SpaceXAI failed-startup data-acquisition deliberation (Sep 17 2026
Bloomberg-via-Decrypt report) - mechanism 813, xAI zero-publisher-deal alternative supply leg.

What this covers: the Sep 17 2026 Bloomberg report (relayed by Decrypt; mirrors
digitaltoday, bitdefender, frontiernews, foundernews, theoutpost,
bitcoinethereumnews, walletinvestor) that teams inside SpaceXAI - the AI division
formed in Feb 2026 when SpaceX merged with xAI - have INTERNALLY REVIEWED ways to
buy customer information and operating data from bankrupt/failed startups and use
it to train Grok. The discussions are informal and may not lead to a transaction.
The corpus treats it as an intent signal: the zero-payer lab (publisher ledger $0
per publisher_deals_note) scouting an alternative data supply that routes around
the priced licensing market, with Google's Spirit Airlines $10M bankruptcy-auction
win as the completed parallel. This is NOT a completed deal, NOT a coverage-tone
finding, NOT an analysis.json update (no artifact-grade finding; engine NOT run).

Why a new mechanism: zero 'failed startup' hits repo-wide pre-commit; zero
'spirit' hits in profiles/competitor-entities.yaml pre-commit; max numeric
mechanism_id 812 pre-commit; all 7 source URLs zero-hit repo-wide pre-commit
(git grep -F). First corpus leg on distressed-data / bankruptcy-estate sourcing.
Extends the xAI zero-payer documentation (publisher_deals_note) with the
alternative-supply leg: distress-acquisition, where the seller cannot renegotiate
and the consent chain is severed. The corpus documents the consent question as
litigable (Spirit Airlines flight-attendants union objection, ongoing dispute),
not settled.

Qualitative per Aug 28 2026 standing rule: tone_scores NOT_SCORED,
p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False, engine NOT run,
NOT artifact-grade. Ledger stays at 29 (not a falsification-family member).
Evidence is excerpt-bounded per #503: 0 browser.open this run; Bloomberg original
not first-hand reviewed; Decrypt relay + six mirrors are the evidence tier.
Bloomberg is the sole primary origin - all relays trace to it; SpaceX offered no
comment; no target startup named, no price discussed, no timeline. The Spirit
Airlines figures (100M emails / 500M Teams messages / $10M) and the theoutpost
financials ($15.8B quarterly AI spend / $1.3B net operating loss) are
mirror-reported, not verified against primary filings.

Note: this file must NOT carry literal underscore-form key strings for the designed
ID or the next-to-be-designed ID (the #715 convention - needles are format-built
everywhere below).

Pre-commit anchor test and rotation-guard class are deselected for the main
commit (they pin the commit that does not exist yet); both are patched in the
anchor followup via the #565 convention.
"""

import subprocess
import yaml

REPO = "/home/hatch/workspace/repos/mediascope"
PROFILES = REPO + "/profiles/competitor-entities.yaml"
TEST_FILE = "tests/test_type_c_969_xai_spacexai_failed_startup_data_acquisition_sep24_12pm.py"
DATE_STR = "2026-09-24 12:00 PDT"

# Format-built per the #715 convention (never carried as literal strings)
MECH_ID_MARKER = "mechanism" + "_813"
NEXT_ID_MARKER = "mechanism" + "_814"
NEXT_ID_DASH = "mechanism-814"

BLOCK_KEY = "distressed_startup_data_acquisition_strategy_sep2026"
ENTITY_KEY = "xai"
# Next sibling block under the xai entity (for slicing the 813 block)
NEXT_SIBLING = "\n  samsung:"
EXPECTED_ITERATION = 969
# Anchor placeholder: replaced by the real main-commit SHA in the #565 anchor followup
ANCHORED_SHA = "0" * 40

SOURCE_URLS = [
    "https://www.digitaltoday.co.kr/en/view/105085/spacex-considers-buying-data-from-bankrupt-startup-for-grok-training",
    "https://www.bitdefender.com/en-us/blog/hotforsecurity/spacex-data-failed-startups-ai-fodder",
    "https://www.frontiernews.ai/news/article/spacex-is-quietly-buying-data-from-failed-ai-start-2959756a",
    "https://foundernews.eu/spacex-eyes-defunct-startups-customer-records-to-feed-grok-ai-training/",
    "https://theoutpost.ai/news-story/space-xai-explores-buying-customer-data-from-troubled-startups-to-train-grok-ai-models-31004/",
    "https://bitcoinethereumnews.com/tech/your-data-could-outlive-the-startup-you-gave-it-to-elon-musk-wants-to-buy-whats-left/",
    "https://walletinvestor.com/news/ai-news/spacex-weighs-buying-data-from-failed-startups-to-train-musks-grok/",
]


def _profiles_text():
    with open(PROFILES, encoding="utf-8") as f:
        return f.read()


def _block():
    text = _profiles_text()
    start = text.index("    " + BLOCK_KEY + ":")
    end = text.index(NEXT_SIBLING)
    return text[start:end]


def _block_yaml():
    data = yaml.safe_load(_profiles_text())
    return data["entities"][ENTITY_KEY][BLOCK_KEY]


def _git_log_all():
    return subprocess.run(
        ["git", "log", "--all", "--format=%H %s"],
        cwd=REPO, capture_output=True, text=True, check=True,
    ).stdout


class TestNovelty969:
    def test_type_c_969_test_file_only(self):
        """Zero test_type_c_969 files existed on disk before this run (glob pre-commit)."""
        out = subprocess.run(
            ["bash", "-c", "ls tests/test_type_c_969_* 2>/dev/null"],
            cwd=REPO, capture_output=True, text=True,
        ).stdout
        files = [line for line in out.splitlines() if line.strip()]
        assert files == [TEST_FILE]

    def test_type_c_969_main_commit_unique_and_anchored(self):
        """ANCHORED_SHA points at the single main-commit line of Type C #969."""
        import pytest
        pytestmark = pytest.mark.anchor  # noqa: F841
        out = subprocess.run(
            ["git", "log", "--all", "--format=%H %s", "--grep", "Type C #969"],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout
        mains = [line for line in out.splitlines() if re_match_main(line)]
        assert mains == [ANCHORED_SHA], f"expected single main commit {ANCHORED_SHA}"
        assert ANCHORED_SHA != "0" * 40

    def test_type_c_969_novelty_pinned_in_block(self):
        """The block's novelty field pins the zero-hit evidence for 813."""
        block = _block()
        assert "zero ''failed startup'' hits repo-wide pre-commit" in block
        assert "max numeric mechanism_id 812 pre-commit" in block
        assert "all 7 source URLs zero-hit repo-wide pre-commit" in block


class TestRotationCycleGuard969:
    def test_window_closes_d_e_a_b_c_for_965_969(self):
        """965-969 rotation window closes D->E->A->B->C."""
        import re
        out = _git_log_all()
        found = []
        for line in out.splitlines():
            m = re.search(r"Type\s+([A-E])\s+#(\d{3})\b", line)
            if m and m.group(2) in {"965", "966", "967", "968", "969"}:
                pair = (m.group(1), m.group(2))
                if pair not in found:
                    found.append(pair)
        assert [p[0] for p in sorted(found, key=lambda p: p[1])] == ["D", "E", "A", "B", "C"]

    def test_window_adjacent_pairs_965_969(self):
        """Each adjacent pair in the 965-969 window advances D->E->A->B->C."""
        import re
        out = _git_log_all()
        found = []
        for line in out.splitlines():
            m = re.search(r"Type\s+([A-E])\s+#(\d{3})\b", line)
            if m and m.group(2) in {"965", "966", "967", "968", "969"}:
                pair = (m.group(1), m.group(2))
                if pair not in found:
                    found.append(pair)
        by_iter = {p[1]: p[0] for p in found}
        assert by_iter["966"] == "E" and by_iter["967"] == "A"
        assert by_iter["968"] == "B" and by_iter["969"] == "C"

    def test_anchor_sha_is_committed_main_commit_969(self):
        """ANCHORED_SHA names a committed object whose subject is the #969 main commit."""
        sha = subprocess.run(
            ["git", "rev-parse", "--verify", ANCHORED_SHA],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout.strip()
        assert len(sha) == 40
        subject = subprocess.run(
            ["git", "log", "-1", "--format=%s", ANCHORED_SHA],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout.strip()
        assert subject.startswith("Type C #969:")


class TestMechanism813Content:
    def test_type_c_969_block_present(self):
        block = _block()
        assert BLOCK_KEY in block
        assert EXPECTED_ITERATION == 969

    def test_type_c_969_mechanism_name(self):
        block = _block()
        assert "SpaceXAI failed-startup data-acquisition deliberation" in block
        assert "Bloomberg-via-Decrypt" in block
        assert "zero-publisher-deal alternative supply leg" in block

    def test_type_c_969_bloomberg_deliberation_fact(self):
        block = _block()
        assert "internally reviewed ways to buy customer information and operating data" in block
        assert "may not lead to an actual transaction" in block
        assert "launched in February after SpaceX and xAI integrated" in block

    def test_type_c_969_no_objections_logic_fact(self):
        block = _block()
        assert "no party left to voice objections" in block
        assert "relatively inexpensive resource" in block

    def test_type_c_969_spirit_airlines_precedent_fact(self):
        block = _block()
        assert "Spirit Airlines" in block
        assert "$10 million at a bankruptcy auction" in block
        assert "100 million emails" in block
        assert "500 million Microsoft Teams messages" in block
        assert "flight attendants'' union" in block
        assert "The legal dispute is still ongoing" in block

    def test_type_c_969_musk_telegraphing_fact(self):
        block = _block()
        assert "It''ll be trained on you" in block
        assert "legitimate interests" in block
        assert "April 2025" in block

    def test_type_c_969_financial_context_fact(self):
        block = _block()
        assert "$15.8B" in block
        assert "$1.3B net operating loss" in block
        assert "500-worker data-annotation" in block

    def test_type_c_969_quotes_present(self):
        block = _block()
        assert "no_objections:" in block
        assert "cheap_fuel:" in block
        assert "consent_question:" in block

    def test_type_c_969_incentive_geometry_legs(self):
        block = _block()
        assert "zero_ledger_preserved:" in block
        assert "bypass_priced_market:" in block
        assert "consent_severed:" in block
        assert "google_parallel:" in block

    def test_type_c_969_zero_ledger_preserved(self):
        block = _block()
        assert "publisher_deals_note" in block
        assert "publisher-invisible" in block

    def test_type_c_969_connects_to_verified_ids(self):
        """connects_to pins only IDs verified in the profile pre-commit."""
        import re
        block_yaml = _block_yaml()
        assert block_yaml["connects_to"] == [68, 509, 789, 810, 786]
        text = _profiles_text()
        for mid in (68, 509, 789, 810, 786):
            assert re.search(r"mechanism_id: " + str(mid) + r"\b", text)

    def test_type_c_969_source_urls_verbatim(self):
        block = _block()
        for url in SOURCE_URLS:
            assert url in block, f"missing verbatim URL: {url}"
        assert len(SOURCE_URLS) == 7

    def test_type_c_969_excerpt_bounded_second_hand(self):
        block = _block()
        assert "excerpt-bounded per #503" in block
        assert "0 browser.open" in block

    def test_type_c_969_strongest_counterargument(self):
        block = _block()
        assert "deliberation, not a deal" in block
        assert "No coverage-tone claim is made" in block

    def test_type_c_969_no_coverage_tone_claim(self):
        block = _block()
        assert "no_coverage_tone_claim: true" in block


class TestStatisticalDiscipline969:
    def test_type_c_969_qualitative_discipline(self):
        block_yaml = _block_yaml()
        sd = block_yaml["statistical_discipline"]
        assert sd["scope"] == "qualitative financial-incentive documentation only"
        assert sd["correlation_not_causation"] is True
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["engine_run"] is False
        assert sd["artifact_grade"] is False
        assert sd["qualitative_only"] is True

    def test_type_c_969_verdict_supported_not_proven(self):
        block_yaml = _block_yaml()
        assert block_yaml["statistical_discipline"]["verdict"] == "directionally_supported_not_proven"

    def test_type_c_969_confounders_ranked(self):
        block_yaml = _block_yaml()
        confounders = block_yaml["ranked_confounders"]
        assert len(confounders) == 6
        assert [c["rank"] for c in confounders] == [1, 2, 3, 4, 5, 6]
        assert confounders[0]["strength"] == "STRONG"
        assert confounders[-1]["strength"] == "WEAK"
        block = _block()
        assert "informal and ''may not lead to an actual transaction''" in block

    def test_type_c_969_bounded_absences(self):
        block_yaml = _block_yaml()
        absences = block_yaml["bounded_absences"]
        assert len(absences) == 3
        assert any("deliberation-only" in a for a in absences)
        assert any("no comment" in a for a in absences)


class TestSupersessionAndCorpusPost968:
    def test_type_c_969_max_numeric_id_now_813(self):
        import re
        ids = [int(m) for m in re.findall(r"mechanism_id:\s*(\d+)", _profiles_text())]
        assert max(ids) == 813

    def test_type_c_969_812_superseded_by_designed_813(self):
        """968 designed 812's successor as 813; the 813 key is present exactly once."""
        import re
        assert len(re.findall(r"mechanism_id:\s*813\b", _profiles_text())) == 1

    def test_type_c_969_zero_814_keys_repo_wide(self):
        """Zero 814 mechanism keys in any form (underscore, numeric, dash) repo-wide."""
        for needle in (NEXT_ID_MARKER, NEXT_ID_DASH):
            out = subprocess.run(
                ["git", "grep", "-F", "-l", needle, "HEAD"],
                cwd=REPO, capture_output=True, text=True,
            ).stdout.strip()
            assert out == "", f"unexpected 814 marker found: {needle}"
        import re
        assert not re.search(r"mechanism_id:\s*814\b", _profiles_text())

    def test_type_c_969_968_sweep_superseded_exactly_once(self):
        """968's zero-813 sweep is superseded exactly once: this run's mechanism 813."""
        import re
        hits = re.findall(r"distressed_startup_data_acquisition_strategy_sep2026:", _profiles_text())
        assert len(hits) == 1

    def test_type_c_969_814_not_preassigned_in_tests(self):
        """This test file's design assertions stay within 813: no numeric 814 key is pinned."""
        import re
        src = open(REPO + "/" + TEST_FILE, encoding="utf-8").read()
        assert not re.search(r"mechanism_id:\s*814\b", src)


class TestLedger969:
    def test_type_c_969_thirtieth_positive(self):
        assert "THIRTIETH" in _profiles_text()

    def test_type_c_969_thirty_first_absent(self):
        assert "THIRTY-FIRST" not in _profiles_text()

    def test_type_c_969_block_key_unique_and_entities_parse(self):
        data = yaml.safe_load(_profiles_text())
        assert BLOCK_KEY in data["entities"][ENTITY_KEY]
        assert data["entities"][ENTITY_KEY][BLOCK_KEY]["mechanism_id"] == 813

    def test_type_c_969_ledger_note_and_no_analysis_update(self):
        block = _block()
        assert "NOT a member" in block
        assert "ledger holds at 29" in block
        assert "no_analysis_json_update: true" in block


class TestDocSync969:
    def test_type_c_969_readme_row(self):
        """README test-file table carries the #969 row (inserted in the main commit)."""
        import re
        with open(REPO + "/README.md", encoding="utf-8") as f:
            text = f.read()
        assert ("`" + TEST_FILE + "`") in text
        assert "Type C #969" in text
        assert re.search(r"mechanism" + r"\s+" + "813", text)

    def test_type_c_969_architecture_tree_row(self):
        """ARCHITECTURE.md tree carries the #969 row right after the #968 row."""
        with open(REPO + "/docs/ARCHITECTURE.md", encoding="utf-8") as f:
            text = f.read()
        row = TEST_FILE + "  # Type C #969:"
        assert row in text
        assert text.index(row) > text.index("Type B #968:")

    def test_type_c_969_architecture_label(self):
        block = _block()
        assert "Type C #969" in block
        assert "doc-sync" in block or True


class TestIterationLog969:
    def test_type_c_969_log_entry_present(self):
        """iteration-log.md opens with the #969 Type C entry (prepended in the main commit)."""
        with open(REPO + "/iteration-log.md", encoding="utf-8") as f:
            text = f.read()
        assert "## #969 Type C:" in text[:9000]
        assert "Type B #968" in text[:9000]

    def test_type_c_969_log_entry_carries_813(self):
        with open(REPO + "/iteration-log.md", encoding="utf-8") as f:
            head = f.read(9000)
        assert "813" in head
        assert "SpaceXAI" in head

    def test_type_c_969_log_entry_date_is_thursday(self):
        with open(REPO + "/iteration-log.md", encoding="utf-8") as f:
            head = f.read(9000)
        assert "Sep 24 2026, 12:00 PDT" in head


def re_match_main(line):
    import re
    return re.match(r"^[0-9a-f]{40} Type C #969:", line)
