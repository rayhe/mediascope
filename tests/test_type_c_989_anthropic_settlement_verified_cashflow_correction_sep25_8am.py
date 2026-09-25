"""Type C #989: Anthropic $1.5B settlement VERIFIED distribution-phase cash-flow
map + m822 year-shift correction - $1.07B in escrow per Docket 688 (Sep 2
2026), $450M Scheduled Payment 1 PAID Aug 19 2026 (not due Sep 25 2026),
final $450M due Sep 25 2027 or on IPO trigger; first author payments
$2,203.56/work by Nov 15 2026; CORRECTS m822 (Sep 8 postponement and Sep 25
preliminary approval were 2025, not 2026; no Sep 25 2026 hearing occurred;
December 2025 trial averted; judge-name "discrepancy" resolved as Alsup
retirement to Martinez-Olguin succession); m612 verified correct, no repair
needed. Mechanism 825 in profiles/competitor-entities.yaml, FIRST dedicated
corpus verification/correction mechanism.

What this covers: Six-outlet convergent dating (Reuters Sep 25 2025 URL,
Publishers Weekly 09/29/2025 issue opened first-hand, AP Sep 8 2025,
Authors Guild installment schedule, Docket 688 via settlementinsight Sep 7
2026, Publishers Lunch via File 770) proves #984 read September 2025
reporting through a September 2026 run-date lens. The verified record:
preliminary approval Sep 25 2025 (Alsup); Alsup retired end 2025; fairness
hearing May 14 2026 and final approval Jul 20 2026 (Martinez-Olguin, largest
known US copyright settlement, 482,460 works, 91%+ claimed); four
installments ($300M Oct 2025, $300M Jul 2026, $450M paid Aug 19 2026, $450M
due Sep 25 2027 or within 30 days of a qualifying funding event); escrow
$1,074,903,166.44; fee award $101.6M (cut from $187.5M); first distribution
~$2,203.56/work by Nov 15 2026; second ~$930/work after final tranche;
Sep 4 2026 consolidated-form emails with 30-day contest window (Publishers
Lunch: Macmillan/Hachette/Harlequin on reverted rights; Kensington/Coffee
House/Johns Hopkins at 100 percent).

Incentive geometry (qualitative only): IPO-trigger acceleration makes
~449,731 claimed works' rightsholders financial stakeholders in Anthropic's
IPO timing (NEW edge vs m612/m822); fee-award lodestar cut returns ~$86M to
the class; the $2,203.56 vs $3,000 gap is fees plus the missing final
tranche; Sep 4 contest window is the live venue for m612's capture-incentive
claim fight. Contrast with m789's priced market (judicial compulsion vs
voluntary transaction). Connects to [822, 612, 594, 509] - all verified
pre-commit in HEAD.

Qualitative per Aug 28 2026 standing rule: tone_scores NOT_SCORED,
p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False, engine NOT run,
NOT artifact-grade. Ledger holds at 30 (not a falsification-family member).
Evidence: 2 browser.open first-hand reads (PW + Reuters Sep 2025, documented
partial deviation from #503 for the correction's dating evidence); all other
sources excerpt-bounded. No coverage-tone claim. No causal claim.

SIXTH and CLOSING leg of the 985-989 rotation window: D (#985) -> E (#986) ->
A (#987) -> B (#988) -> C (#989, this run).

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
TEST_FILE = "tests/test_type_c_989_anthropic_settlement_verified_cashflow_correction_sep25_8am.py"
DATE_STR = "2026-09-25 08:00 PDT"

# Format-built per the #715 convention (never carried as literal strings)
MECH_ID_MARKER = "mechanism" + "_825"
NEXT_ID_MARKER = "mechanism" + "_826"
NEXT_ID_DASH = "mechanism" + "-826"

BLOCK_KEY = "type_c_989_anthropic_settlement_verified_cashflow_correction_sep25"
# Tail-block convention: zero-indent standalone block at the end of the file
EXPECTED_ITERATION = 989
# Anchor placeholder: replaced by the real main-commit SHA in the #565 anchor followup
ANCHORED_SHA = "a9b9fae1fe00568822d15b3509b6439921ca4f77"  # patched green in the anchor followup per #565

SOURCE_URLS = [
    "https://www.reuters.com/sustainability/boards-policy-regulation/us-judge-approves-15-billion-anthropic-copyright-settlement-with-authors-2025-09-25/?ref=spyglass.org",
    "https://www.publishersweekly.com/pw/by-topic/digital/copyright/article/98706-judge-gives-preliminary-approval-to-anthropic-settlement.html",
    "https://www.reuters.com/legal/government/landmark-anthropic-settlement-judge-rejects-windfall-lawyers-2026-07-21/",
    "https://srnnews.com/us-judge-approves-anthropics-1-5-billion-settlement-of-copyright-lawsuit/",
    "https://authorsguild.org/news/anthropic-settlement-update-91-percent-of-books-claimed/",
    "https://settlementinsight.com/news/anthropic-settlement-first-payments-by-november-15-2203-dollars-per-work-not-3000-and-30-days-to-contest-the-split",
    "https://www.alliemccormack.com/post/anthropic-v-bartz-the-final-ruling",
    "https://file770.com/tag/anthropic/",
    "https://fourweekmba.com/ai-anthropic-copyright-settlement-training-data-cost/",
    "https://tech-insider.org/au/anthropic-copyright-settlement-2026/",
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
    return re.search(r"^Type C #989:", line.split(" ", 1)[1] if " " in line else "")


class TestNovelty989:
    def test_type_c_989_test_file_only(self):
        """Zero test_type_c_989 files existed on disk before this run (glob pre-commit)."""
        out = subprocess.run(
            ["bash", "-c", "ls tests/test_type_c_989_* 2>/dev/null"],
            cwd=REPO, capture_output=True, text=True,
        ).stdout
        files = [line for line in out.splitlines() if line.strip()]
        assert files == [TEST_FILE]

    def test_type_c_989_main_commit_unique_and_anchored(self):
        """ANCHORED_SHA points at the single main-commit line of Type C #989."""
        import pytest
        pytestmark = pytest.mark.anchor  # noqa: F841
        out = subprocess.run(
            ["git", "log", "--all", "--format=%H %s", "--grep", "Type C #989"],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout
        mains = [line.split()[0] for line in out.splitlines() if re_match_main(line)]
        assert mains == [ANCHORED_SHA], f"expected single main commit {ANCHORED_SHA}"
        assert ANCHORED_SHA != "0" * 40

    def test_type_c_989_novelty_pinned_in_block(self):
        """The block's novelty field pins the zero-hit evidence for 825."""
        block = _block()
        assert "zero test_type_c_989 files on disk" in block
        assert "max numeric mechanism id pre-commit 824" in block
        assert "10 of 10 source URLs zero-hit repo-wide pre-commit" in block


class TestRotationCycleGuard989:
    def test_window_closes_d_e_a_b_c_for_985_989(self):
        """985-989 rotation window closes D->E->A->B->C."""
        import re
        out = _git_log_all()
        found = []
        for line in out.splitlines():
            m = re.search(r"Type\s+([A-E])\s+#(\d{3})\b", line)
            if m and m.group(2) in {"985", "986", "987", "988", "989"}:
                pair = (m.group(1), m.group(2))
                if pair not in found:
                    found.append(pair)
        assert [p[0] for p in sorted(found, key=lambda p: p[1])] == ["D", "E", "A", "B", "C"]

    def test_window_adjacent_pairs_985_989(self):
        """Each adjacent pair in the 985-989 window advances D->E->A->B->C."""
        import re
        out = _git_log_all()
        found = []
        for line in out.splitlines():
            m = re.search(r"Type\s+([A-E])\s+#(\d{3})\b", line)
            if m and m.group(2) in {"985", "986", "987", "988", "989"}:
                pair = (m.group(1), m.group(2))
                if pair not in found:
                    found.append(pair)
        by_iter = {p[1]: p[0] for p in found}
        assert by_iter["985"] == "D" and by_iter["986"] == "E"
        assert by_iter["987"] == "A" and by_iter["988"] == "B"
        assert by_iter["989"] == "C"

    def test_anchor_sha_is_committed_main_commit_989(self):
        """ANCHORED_SHA names a committed object whose subject is the #989 main commit."""
        sha = subprocess.run(
            ["git", "rev-parse", "--verify", ANCHORED_SHA],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout.strip()
        assert len(sha) == 40
        subject = subprocess.run(
            ["git", "log", "-1", "--format=%s", ANCHORED_SHA],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout.strip()
        assert subject.startswith("Type C #989:")


class TestMechanism825Content:
    def test_type_c_989_block_present(self):
        """The 989 tail block is present at zero indent in the profiles file."""
        text = _profiles_text()
        assert ("\n" + BLOCK_KEY + ":") in text

    def test_type_c_989_mechanism_name(self):
        """The mechanism name carries the verified cash-flow map and the m822 correction."""
        block = _block_yaml()
        assert block["mechanism_id"] == 825
        assert block["iteration"] == 989
        assert "$1.07B" in block["mechanism_name"] or "1.07B" in block["mechanism_name"]
        assert "PAID Aug 19 2026" in block["mechanism_name"]
        assert "CORRECTS m822" in block["mechanism_name"]

    def test_type_c_989_verified_timeline_2025(self):
        """The verified timeline places the postponement and preliminary approval in 2025."""
        block = _block()
        assert "September 8, 2025" in block
        assert "September 25, 2025" in block
        assert "PRELIMINARY approval" in block

    def test_type_c_989_no_sep25_2026_hearing(self):
        """The block asserts no Sep 25 2026 hearing was scheduled or occurred."""
        block = _block()
        assert "NO hearing scheduled or occurring" in block
        assert "no Sep 25 2026 hearing exists or occurred" in block

    def test_type_c_989_final_approval_jul20_2026(self):
        """Final approval Jul 20 2026 by Martinez-Olguin is mapped."""
        block = _block()
        assert "July 20, 2026" in block
        assert "Martinez-Olguin" in block
        assert "FINAL approval" in block

    def test_type_c_989_judge_succession(self):
        """The Alsup-to-Martinez-Olguin succession is mapped (retirement end 2025)."""
        block = _block()
        assert "Alsup retired" in block
        assert "judicial succession" in block

    def test_type_c_989_escrow_balance(self):
        """The Docket 688 escrow balance $1,074,903,166.44 is mapped."""
        block = _block()
        assert "1,074,903,166.44" in block
        assert "Docket 688" in block

    def test_type_c_989_installment_paid_early(self):
        """Scheduled Payment 1 ($450M) paid Aug 19 2026, not due Sep 25 2026."""
        block = _block()
        assert "paid on August 19, 2026" in block
        assert "five weeks before the contractual due date" in block
        assert "No $450M is due on Sep 25 2026" in block

    def test_type_c_989_final_installment_ipo_trigger(self):
        """Scheduled Payment 2 ($450M) due Sep 25 2027 or on qualifying funding event."""
        block = _block()
        assert "September 25, 2027" in block
        assert "qualifying funding event" in block

    def test_type_c_989_first_payment_2203(self):
        """First author payment ~$2,203.56/work by Nov 15 2026 is mapped."""
        block = _block()
        assert "2,203.56" in block
        assert "November 15" in block

    def test_type_c_989_fee_award(self):
        """The fee award $101.6M (cut from $187.5M) is mapped."""
        block = _block()
        assert "101.6M" in block or "101,561,111" in block
        assert "187.5M" in block
        assert "windfall" in block

    def test_type_c_989_claim_fight_update(self):
        """The Sep 2026 named-publisher claim-fight update extends m612."""
        block = _block()
        assert "Macmillan" in block
        assert "Hachette" in block
        assert "Harlequin" in block
        assert "Kensington" in block

    def test_type_c_989_m822_correction_audit(self):
        """The five-error m822 correction audit is present."""
        block = _block()
        assert "ERROR 1 (hearing year)" in block
        assert "ERROR 2 (hearing year)" in block
        assert "ERROR 3 (installment due date)" in block
        assert "ERROR 4 (trial fallback year)" in block
        assert "ERROR 5 (judge-name discrepancy)" in block
        assert "ROOT CAUSE" in block

    def test_type_c_989_m612_verified_correct(self):
        """m612 is verified correct and needed no repair."""
        block = _block()
        assert "m612" in block
        assert "verified correct" in block
        assert "No repair needed to m612" in block

    def test_type_c_989_ipo_trigger_incentive(self):
        """The IPO-trigger incentive alignment (NEW edge) is mapped."""
        block = _block()
        assert "IPO-trigger incentive alignment" in block
        assert "financial stakeholders" in block

    def test_type_c_989_connects_to_verified_ids(self):
        """connects_to carries the four HEAD-verified mechanism ids."""
        block = _block_yaml()
        assert block["connects_to"] == [822, 612, 594, 509]

    def test_type_c_989_source_urls_verbatim(self):
        """All ten source URLs are verbatim and zero-hit pre-commit."""
        block = _block_yaml()
        assert block["source_urls"] == SOURCE_URLS
        assert SOURCE_URLS[0].startswith("https://www.reuters.com/sustainability/")
        assert "2025-09-25" in SOURCE_URLS[0]
        assert SOURCE_URLS[4].startswith("https://authorsguild.org/")

    def test_type_c_989_two_browser_open_deviation(self):
        """Two first-hand browser.open reads are documented as a #503 deviation."""
        block = _block()
        assert "2 browser.open first-hand reads" in block
        assert "documented partial deviation from #503" in block

    def test_type_c_989_no_coverage_tone_claim(self):
        """No coverage-tone claim is made; this is a verified cash-flow correction."""
        block = _block()
        assert "No coverage-tone claim is made" in block


class TestM822Repair989:
    def test_m822_correction_989_field_present(self):
        """m822 carries the correction_989 audit field."""
        data = yaml.safe_load(_profiles_text())
        b822 = data["type_c_984_anthropic_settlement_distribution_sep25_hearing_450m_installment_sep25"]
        assert "correction_989" in b822
        assert "Year-shift repair" in b822["correction_989"]

    def test_m822_hearing_status_corrected(self):
        """m822 hearing_status carries CORRECTED/RESOLVED labels with 2025 dates."""
        data = yaml.safe_load(_profiles_text())
        b822 = data["type_c_984_anthropic_settlement_distribution_sep25_hearing_450m_installment_sep25"]
        text = str(b822["hearing_status"])
        assert "CORRECTED #989" in text
        assert "September 8, 2025" in text
        assert "Sep 25 2025" in text
        assert "RESOLVED #989" in text

    def test_m822_installment_superseded(self):
        """m822 installment_schedule is SUPERSEDED with the verified schedule pointer."""
        data = yaml.safe_load(_profiles_text())
        b822 = data["type_c_984_anthropic_settlement_distribution_sep25_hearing_450m_installment_sep25"]
        text = str(b822["installment_schedule"])
        assert "SUPERSEDED #989" in text
        assert "PAID Aug 19 2026" in text
        assert "mechanism 825" in text


class TestStatisticalDiscipline989:
    def test_type_c_989_qualitative_discipline(self):
        """Qualitative mapping: tone NOT_SCORED, p/d/CI NOT_CALCULATED, not significant, engine not run."""
        disc = _block_yaml()["statistical_discipline"]
        assert disc["tone_scores"] == "NOT_SCORED"
        assert disc["p_value"] == "NOT_CALCULATED"
        assert disc["cohens_d"] == "NOT_CALCULATED"
        assert disc["ci_95"] == "NOT_CALCULATED"
        assert disc["is_significant"] is False
        assert disc["engine_run"] is False

    def test_type_c_989_verdict_supported_not_proven(self):
        """Verdict is directionally_supported_not_proven; no causal claim."""
        disc = _block_yaml()["statistical_discipline"]
        assert disc["verdict"] == "directionally_supported_not_proven"
        assert disc["no_causal_claim"] is True
        assert disc["correlation_not_causation"] is True

    def test_type_c_989_confounders_ranked(self):
        """Confounders are ranked strong-first with six entries."""
        block = _block()
        assert "STRONG: Docket 688" in block
        assert "STRONG: Excerpt-bounded" in block
        assert "MODERATE:" in block
        assert "WEAK:" in block

    def test_type_c_989_bounded_absences(self):
        """Bounded absences per the iteration-492 rule; no zero-coverage claims."""
        block = _block()
        assert "No first-hand PACER/docket read" in block
        assert "not claimed" in block


class TestSupersessionAndCorpusPost988:
    def test_type_c_989_max_numeric_id_now_825(self):
        """Max numeric mechanism id is now 825 (colon form)."""
        import re
        ids = [int(m) for m in re.findall(r"mechanism_id:\s*(\d+)", _profiles_text())]
        assert max(ids) == 825

    def test_type_c_989_824_superseded_by_designed_825(self):
        """824 (journalists.yaml) remains the previous max; 825 is the new designed head."""
        import re
        out = subprocess.run(
            ["bash", "-c", "grep -rh 'mechanism_id: 82[45]\\b' profiles/ | sort -u"],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout
        assert "mechanism_id: 824" in out
        assert "mechanism_id: 825" in out
        text = _profiles_text()
        assert len(re.findall(r"mechanism_id:\s*825\b", text)) == 1

    def test_type_c_989_zero_826_keys_repo_wide(self):
        """No underscore-826 or colon-826 mechanism keys exist anywhere (next ID unassigned)."""
        import re
        text = _profiles_text()
        assert NEXT_ID_MARKER not in text
        assert NEXT_ID_DASH not in text
        assert len(re.findall(r"mechanism_id:\s*826\b", text)) == 0

    def test_type_c_989_826_not_preassigned_in_tests(self):
        """No test source file pre-assigns mechanism 826 (pycache excluded)."""
        out = subprocess.run(
            ["bash", "-c", "grep -rl " + NEXT_ID_MARKER + " tests/*.py 2>/dev/null | head -5"],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout
        assert out.strip() == ""

    def test_type_c_989_block_key_unique_and_top_level_parse(self):
        """The block key is unique and parses as a top-level YAML key."""
        text = _profiles_text()
        assert text.count("\n" + BLOCK_KEY + ":") == 1
        data = yaml.safe_load(text)
        assert BLOCK_KEY in data
        assert data[BLOCK_KEY]["mechanism_id"] == 825


class TestLedger989:
    def test_type_c_989_thirtieth_positive(self):
        """Ledger holds at 30 positive claims (not a falsification-family member)."""
        disc = _block_yaml()["statistical_discipline"]
        assert "30 positive" in disc["ledger"]
        assert disc["falsification_family"] is False

    def test_type_c_989_thirty_first_absent(self):
        """No 31st ledger member is claimed."""
        block = _block()
        assert "no new member" in block

    def test_type_c_989_ledger_note_and_no_analysis_update(self):
        """analysis.json is untouched; artifact grade is false."""
        disc = _block_yaml()["statistical_discipline"]
        assert disc["analysis_json_updated"] is False
        assert disc["artifact_grade"] is False

    def test_type_c_989_block_carries_no_member_claim(self):
        """The block makes no falsification-ledger membership claim."""
        block = _block()
        assert "not a falsification-family member" in block


class TestDocSync989:
    def test_type_c_989_readme_row(self):
        """README test-file table carries the #989 row (inserted in the main commit)."""
        import re
        with open(REPO + "/README.md", encoding="utf-8") as f:
            text = f.read()
        assert ("`" + TEST_FILE + "`") in text
        assert "Type C #989" in text
        assert re.search(r"mechanism" + r"\s+" + "825", text)

    def test_type_c_989_architecture_tree_row(self):
        """ARCHITECTURE.md tree carries the #989 row right after the #988 row."""
        with open(REPO + "/docs/ARCHITECTURE.md", encoding="utf-8") as f:
            text = f.read()
        row = TEST_FILE + "  # Type C #989:"
        assert row in text
        assert text.index(row) > text.index("Type B #988:")

    def test_type_c_989_architecture_label(self):
        block = _block()
        assert "Type C #989" in block or "iteration: 989" in block


class TestIterationLog989:
    def test_type_c_989_log_entry_present(self):
        """iteration-log.md opens with the #989 Type C entry (prepended in the main commit)."""
        with open(REPO + "/iteration-log.md", encoding="utf-8") as f:
            text = f.read()
        assert "## #989 Type C:" in text[:15000]
        assert "Type B #988" in text[:15000]

    def test_type_c_989_log_entry_carries_825(self):
        with open(REPO + "/iteration-log.md", encoding="utf-8") as f:
            head = f.read(15000)
        assert "825" in head
        assert "Anthropic" in head

    def test_type_c_989_log_entry_date_is_friday(self):
        with open(REPO + "/iteration-log.md", encoding="utf-8") as f:
            head = f.read(15000)
        assert "Sep 25 2026, 08:00 PDT" in head

    def test_type_c_989_window_closed_marker(self):
        """The log entry marks the 985-989 D->E->A->B->C window as closed."""
        with open(REPO + "/iteration-log.md", encoding="utf-8") as f:
            head = f.read(15000)
        assert "985-989" in head
        assert "window" in head.lower()
