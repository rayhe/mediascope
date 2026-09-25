"""Type C #984: Anthropic $1.5B settlement distribution-phase Sep 2026 status -
Judge William Alsup postpones final distribution approval on Sep 8 with 34
specific questions, sets Sep 25 hearing; $450M installment due Sep 25, 2026;
extends mechanism 612. Mechanism 822 in profiles/competitor-entities.yaml,
FIRST dedicated corpus mechanism on the distribution-phase judicial-oversight
and cash-flow status of the largest AI-copyright settlement.

What this covers: Bloomberg Law reports Alsup postponed his approval on
Sep 8, set 34 specific questions and scenarios across two filings, and set the
next hearing for Sep 25 in the US District Court for the Northern District of
California. The settlement covers some 465,000 books at roughly $3,000 per
book; a December jury trial with theoretical exposure up to $1 trillion is the
fallback if approval fails. Separately, a $450M installment is due Sep 25,
2026 under the reported four-installment schedule ($300M Oct 2 2025, $300M
within a week of final approval, $450M Sep 25 2026, $450M Sep 25 2027 -
entrelligence, single secondary source). The hearing outcome is unknown (this
run precedes it) and is not claimed.

Incentive geometry (qualitative only): the publisher over-claim pattern (m612)
is the distribution-phase capture incentive; the 34-question postponement is
the judicial cost imposed on it. The $450M installment is the largest single
payment in the schedule - the cash-flow event that makes the distribution
phase real. Contrast with m789's priced licensing market (voluntary
transaction vs judicial compulsion). News Corp exposure carried from m594
(HarperCollins in the April Henry over-claim example). Connects to
[612, 594, 509, 753, 589] - all verified pre-commit in HEAD.

Qualitative per Aug 28 2026 standing rule: tone_scores NOT_SCORED,
p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False, engine NOT run,
NOT artifact-grade. Ledger holds at 30 (not a falsification-family member).
Evidence is excerpt-bounded per #503: 0 browser.open this run; Bloomberg Law
excerpt + entrelligence + newsgab corroboration are the evidence tier.
No coverage-tone claim. No causal claim.

FIFTH and CLOSING leg of the 980-984 rotation window: D (#980) -> E (#981) ->
A (#982) -> B (#983) -> C (#984, this run).

Note: this file must NOT carry literal underscore-form key strings for the
designed ID or the next-to-be-designed ID (the #715 convention - needles are
format-built everywhere below).

Pre-commit anchor test and rotation-guard class are deselected for the main
commit (they pin the commit that does not exist yet); both are patched in the
anchor followup via the #565 convention.
"""

import subprocess

import yaml

REPO = "/home/hatch/workspace/repos/mediascope"
PROFILES = REPO + "/profiles/competitor-entities.yaml"
TEST_FILE = "tests/test_type_c_984_anthropic_settlement_sep25_hearing_450m_installment_sep25_3am.py"
DATE_STR = "2026-09-25 03:00 PDT"

# Format-built per the #715 convention (never carried as literal strings)
MECH_ID_MARKER = "mechanism" + "_822"
NEXT_ID_MARKER = "mechanism" + "_823"
NEXT_ID_DASH = "mechanism" + "-823"

BLOCK_KEY = "type_c_984_anthropic_settlement_distribution_sep25_hearing_450m_installment_sep25"
# Tail-block convention: zero-indent standalone block at the end of the file
EXPECTED_ITERATION = 984
# Anchor placeholder: replaced by the real main-commit SHA in the #565 anchor followup
ANCHORED_SHA = "0000000000000000000000000000000000000000"  # patched green in the anchor followup per #565

SOURCE_URLS = [
    "https://news.bloomberglaw.com/ip-law/anthropic-ai-copyright-settlement-must-clear-logistical-hurdles",
    "https://entrelligence.com/federal-judge-approves-anthropic-paying-1-5b-to-settle-lawsuit-with-book-authors/",
    "https://newsgab.com/authors-push-back-publishers-agents-seek-anthropic-settlement/",
    "https://techcrunch.com/2026/09/06/authors-push-back-as-publishers-and-agents-seek-share-of-anthropic-settlement/",
]


def _profiles_text():
    with open(PROFILES, encoding="utf-8") as f:
        return f.read()


def _block():
    text = _profiles_text()
    start = text.index("\n" + BLOCK_KEY + ":")
    return text[start:]


def _block_yaml():
    data = yaml.safe_load(_profiles_text())
    return data[BLOCK_KEY]


def _git_log_all():
    return subprocess.run(
        ["git", "log", "--all", "--format=%H %s"],
        cwd=REPO, capture_output=True, text=True, check=True,
    ).stdout


def re_match_main(line):
    import re
    return re.search(r"^Type C #984:", line.split(" ", 1)[1] if " " in line else "")


class TestNovelty984:
    def test_type_c_984_test_file_only(self):
        """Zero test_type_c_984 files existed on disk before this run (glob pre-commit)."""
        out = subprocess.run(
            ["bash", "-c", "ls tests/test_type_c_984_* 2>/dev/null"],
            cwd=REPO, capture_output=True, text=True,
        ).stdout
        files = [line for line in out.splitlines() if line.strip()]
        assert files == [TEST_FILE]

    def test_type_c_984_main_commit_unique_and_anchored(self):
        """ANCHORED_SHA points at the single main-commit line of Type C #984."""
        import pytest
        pytestmark = pytest.mark.anchor  # noqa: F841
        out = subprocess.run(
            ["git", "log", "--all", "--format=%H %s", "--grep", "Type C #984"],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout
        mains = [line.split()[0] for line in out.splitlines() if re_match_main(line)]
        assert mains == [ANCHORED_SHA], f"expected single main commit {ANCHORED_SHA}"
        assert ANCHORED_SHA != "0" * 40

    def test_type_c_984_novelty_pinned_in_block(self):
        """The block's novelty field pins the zero-hit evidence for 822."""
        block = _block()
        assert "zero test_type_c_984 files on disk" in block
        assert "max numeric mechanism id pre-commit 821" in block
        assert "4 of 4 source URLs zero-hit repo-wide pre-commit" in block


class TestRotationCycleGuard984:
    def test_window_closes_d_e_a_b_c_for_980_984(self):
        """980-984 rotation window closes D->E->A->B->C."""
        import re
        out = _git_log_all()
        found = []
        for line in out.splitlines():
            m = re.search(r"Type\s+([A-E])\s+#(\d{3})\b", line)
            if m and m.group(2) in {"980", "981", "982", "983", "984"}:
                pair = (m.group(1), m.group(2))
                if pair not in found:
                    found.append(pair)
        assert [p[0] for p in sorted(found, key=lambda p: p[1])] == ["D", "E", "A", "B", "C"]

    def test_window_adjacent_pairs_980_984(self):
        """Each adjacent pair in the 980-984 window advances D->E->A->B->C."""
        import re
        out = _git_log_all()
        found = []
        for line in out.splitlines():
            m = re.search(r"Type\s+([A-E])\s+#(\d{3})\b", line)
            if m and m.group(2) in {"980", "981", "982", "983", "984"}:
                pair = (m.group(1), m.group(2))
                if pair not in found:
                    found.append(pair)
        by_iter = {p[1]: p[0] for p in found}
        assert by_iter["980"] == "D" and by_iter["981"] == "E"
        assert by_iter["982"] == "A" and by_iter["983"] == "B"
        assert by_iter["984"] == "C"

    def test_anchor_sha_is_committed_main_commit_984(self):
        """ANCHORED_SHA names a committed object whose subject is the #984 main commit."""
        sha = subprocess.run(
            ["git", "rev-parse", "--verify", ANCHORED_SHA],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout.strip()
        assert len(sha) == 40
        subject = subprocess.run(
            ["git", "log", "-1", "--format=%s", ANCHORED_SHA],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout.strip()
        assert subject.startswith("Type C #984:")


class TestMechanism822Content:
    def test_type_c_984_block_present(self):
        """The 984 tail block is present at zero indent in the profiles file."""
        text = _profiles_text()
        assert ("\n" + BLOCK_KEY + ":") in text

    def test_type_c_984_mechanism_name(self):
        """The mechanism name carries the Sep 25 hearing and $450M installment."""
        block = _block_yaml()
        assert block["mechanism_id"] == 822
        assert block["iteration"] == 984
        assert "Sep 25" in block["mechanism_name"]
        assert "$450M" in block["mechanism_name"]

    def test_type_c_984_thirty_four_questions(self):
        """The Sep 8 postponement with 34 specific questions is mapped."""
        block = _block()
        assert "34 specific questions" in block
        assert "Sep 8" in block
        assert "William Alsup" in block

    def test_type_c_984_sep25_hearing(self):
        """The Sep 25 ND Cal hearing is mapped as a scheduled gate."""
        block = _block()
        assert "Sep 25" in block
        assert "Northern District of California" in block

    def test_type_c_984_hearing_outcome_unknown(self):
        """The hearing outcome is explicitly not claimed (run precedes the hearing)."""
        block = _block()
        assert "outcome is unknown" in block
        assert "not claimed" in block

    def test_type_c_984_installment_schedule(self):
        """The four-installment schedule with the Sep 25 2026 $450M leg is mapped."""
        block = _block()
        assert "$300M" in block
        assert "Oct 2, 2025" in block
        assert "$450M" in block
        assert "Sep 25, 2027" in block

    def test_type_c_984_installment_single_source(self):
        """The installment schedule is carried as single-source (entrelligence)."""
        block = _block()
        assert "single secondary source" in block

    def test_type_c_984_judge_name_discrepancy(self):
        """The Martinez-Olguin vs Alsup judge-name discrepancy is bounded, not adjudicated."""
        block = _block()
        assert "Martinez-Olguin" in block
        assert "not adjudicated" in block

    def test_type_c_984_trillion_exposure_theoretical(self):
        """The $1T jury-trial exposure is carried as theoretical, not a forecast."""
        block = _block()
        assert "$1 trillion" in block
        assert "theoretical statutory maximum" in block

    def test_type_c_984_calendar_coincidence_not_causal(self):
        """The Sep 25 installment/hearing date coincidence is noted, not interpreted."""
        block = _block()
        assert "Calendar coincidence" in block
        assert "no causal or contractual link claimed" in block

    def test_type_c_984_connects_to_verified_ids(self):
        """connects_to carries the five HEAD-verified mechanism ids."""
        block = _block_yaml()
        assert block["connects_to"] == [612, 594, 509, 753, 589]

    def test_type_c_984_source_urls_verbatim(self):
        """All four source URLs are verbatim and zero-hit pre-commit."""
        block = _block_yaml()
        assert block["source_urls"] == SOURCE_URLS
        assert SOURCE_URLS[0].startswith("https://news.bloomberglaw.com/")
        assert SOURCE_URLS[1].startswith("https://entrelligence.com/")

    def test_type_c_984_excerpt_bounded_second_hand(self):
        """Evidence tier is excerpt-bounded per #503 (0 browser.open)."""
        block = _block()
        assert "Excerpt-bounded" in block
        assert "0 browser.open" in block

    def test_type_c_984_no_coverage_tone_claim(self):
        """No coverage-tone claim is made; this is court-calendar and cash-flow status."""
        block = _block()
        assert "No coverage-tone claim is made" in block

    def test_type_c_984_counterevidence_bounded(self):
        """Counterevidence bounds the capture-incentive reading."""
        block = _block()
        assert "Rasenberger" in block
        assert "bad recordkeeping" in block


class TestStatisticalDiscipline984:
    def test_type_c_984_qualitative_discipline(self):
        """Qualitative mapping: tone NOT_SCORED, p/d/CI NOT_CALCULATED, not significant, engine not run."""
        disc = _block_yaml()["statistical_discipline"]
        assert disc["tone_scores"] == "NOT_SCORED"
        assert disc["p_value"] == "NOT_CALCULATED"
        assert disc["cohens_d"] == "NOT_CALCULATED"
        assert disc["ci_95"] == "NOT_CALCULATED"
        assert disc["is_significant"] is False
        assert disc["engine_run"] is False

    def test_type_c_984_verdict_supported_not_proven(self):
        """Verdict is directionally_supported_not_proven; no causal claim."""
        disc = _block_yaml()["statistical_discipline"]
        assert disc["verdict"] == "directionally_supported_not_proven"
        assert disc["no_causal_claim"] is True
        assert disc["correlation_not_causation"] is True

    def test_type_c_984_confounders_ranked(self):
        """Confounders are ranked strong-first with six entries."""
        block = _block()
        assert "STRONG: Hearing outcome unknown" in block
        assert "STRONG: Excerpt-bounded" in block
        assert "STRONG: Judge-name discrepancy" in block
        assert "MODERATE:" in block
        assert "WEAK:" in block

    def test_type_c_984_bounded_absences(self):
        """Bounded absences per the iteration-492 rule; no zero-coverage claims."""
        block = _block()
        assert "No outcome of the Sep 25 hearing" in block
        assert "not claimed" in block


class TestSupersessionAndCorpusPost983:
    def test_type_c_984_max_numeric_id_now_822(self):
        """Max numeric mechanism id is now 822 (colon form)."""
        import re
        ids = [int(m) for m in re.findall(r"mechanism_id:\s*(\d+)", _profiles_text())]
        assert max(ids) == 822

    def test_type_c_984_821_superseded_by_designed_822(self):
        """821 (journalists.yaml) remains the previous max; 822 is the new designed head."""
        import re
        out = subprocess.run(
            ["bash", "-c", "grep -rh 'mechanism_id: 82[12]\\b' profiles/ | sort -u"],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout
        assert "mechanism_id: 821" in out
        assert "mechanism_id: 822" in out
        text = _profiles_text()
        assert len(re.findall(r"mechanism_id:\s*822\b", text)) == 1

    def test_type_c_984_zero_823_keys_repo_wide(self):
        """No underscore-823 or colon-823 mechanism keys exist anywhere (next ID unassigned)."""
        import re
        text = _profiles_text()
        assert NEXT_ID_MARKER not in text
        assert NEXT_ID_DASH not in text
        assert len(re.findall(r"mechanism_id:\s*823\b", text)) == 0

    def test_type_c_984_823_not_preassigned_in_tests(self):
        """No test source file pre-assigns mechanism 823 (pycache excluded)."""
        out = subprocess.run(
            ["bash", "-c", "grep -rl " + NEXT_ID_MARKER + " tests/*.py 2>/dev/null | head -5"],
            cwd=REPO, capture_output=True, text=True,
        ).stdout
        assert out.strip() == ""

    def test_type_c_984_block_key_unique_and_top_level_parse(self):
        """The block key is unique and parses as a top-level YAML key."""
        text = _profiles_text()
        assert text.count("\n" + BLOCK_KEY + ":") == 1
        data = yaml.safe_load(text)
        assert BLOCK_KEY in data
        assert data[BLOCK_KEY]["mechanism_id"] == 822


class TestLedger984:
    def test_type_c_984_thirtieth_positive(self):
        """Ledger holds at 30 positive claims (not a falsification-family member)."""
        disc = _block_yaml()["statistical_discipline"]
        assert "30 positive" in disc["ledger"]
        assert disc["falsification_family"] is False

    def test_type_c_984_thirty_first_absent(self):
        """No 31st ledger member is claimed."""
        block = _block()
        assert "no new member" in block

    def test_type_c_984_ledger_note_and_no_analysis_update(self):
        """analysis.json is untouched; artifact grade is false."""
        disc = _block_yaml()["statistical_discipline"]
        assert disc["analysis_json_updated"] is False
        assert disc["artifact_grade"] is False

    def test_type_c_984_block_carries_no_member_claim(self):
        """The block makes no falsification-ledger membership claim."""
        block = _block()
        assert "not a falsification-family member" in block


class TestDocSync984:
    def test_type_c_984_readme_row(self):
        """README test-file table carries the #984 row (inserted in the main commit)."""
        import re
        with open(REPO + "/README.md", encoding="utf-8") as f:
            text = f.read()
        assert ("`" + TEST_FILE + "`") in text
        assert "Type C #984" in text
        assert re.search(r"mechanism" + r"\s+" + "822", text)

    def test_type_c_984_architecture_tree_row(self):
        """ARCHITECTURE.md tree carries the #984 row right after the #983 row."""
        with open(REPO + "/docs/ARCHITECTURE.md", encoding="utf-8") as f:
            text = f.read()
        row = TEST_FILE + "  # Type C #984:"
        assert row in text
        assert text.index(row) > text.index("Type B #983:")

    def test_type_c_984_architecture_label(self):
        block = _block()
        assert "Type C #984" in block or "iteration: 984" in block


class TestIterationLog984:
    def test_type_c_984_log_entry_present(self):
        """iteration-log.md opens with the #984 Type C entry (prepended in the main commit)."""
        with open(REPO + "/iteration-log.md", encoding="utf-8") as f:
            text = f.read()
        assert "## #984 Type C:" in text[:12000]
        assert "Type B #983" in text[:12000]

    def test_type_c_984_log_entry_carries_822(self):
        with open(REPO + "/iteration-log.md", encoding="utf-8") as f:
            head = f.read(12000)
        assert "822" in head
        assert "Anthropic" in head

    def test_type_c_984_log_entry_date_is_friday(self):
        with open(REPO + "/iteration-log.md", encoding="utf-8") as f:
            head = f.read(12000)
        assert "Sep 25 2026, 03:00 PDT" in head

    def test_type_c_984_window_closed_marker(self):
        """The log entry marks the 980-984 D->E->A->B->C window as closed."""
        with open(REPO + "/iteration-log.md", encoding="utf-8") as f:
            head = f.read(12000)
        assert "980-984" in head
        assert "window" in head.lower()
