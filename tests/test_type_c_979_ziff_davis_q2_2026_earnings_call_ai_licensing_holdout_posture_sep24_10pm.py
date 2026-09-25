"""Type C #979: Ziff Davis Q2 2026 earnings call (Aug 6 2026) - CEO Vivek Shah states
the AI-licensing holdout posture on the record - mechanism 819, FIRST dedicated
corpus mechanism on a publisher CEO's on-the-record refusal to sign AI licensing
deals that compromise foundational-training compensation rights.

What this covers: the Aug 6 2026 Ziff Davis Q2 earnings call where Shah, asked
about AI content licensing, says the company is "not inclined to sign a
RAG-focused agreement that compromises our right to fair compensation for
foundational training", wants to "establish the right financial precedent more
than anything else than booking kind of a quick dollar", confirms "the
litigation that we have with OpenAI is proceeding", and closes with "I'd rather
be patient than early and lock in a little bit of cash". Twenty-nine days later
the awaited legal-clarity vehicle arrives: the Sep 4 2026 MDL 1:25-md-03143
cross-motions for summary judgment, with Ziff Davis among the five publisher
movants seeking liability judgment (ppc.land; mixed-news.com corroboration).

Incentive geometry (qualitative only): the corpus's adversarial-incentive
publisher (m589) now has management-stated holdout strategy - forgo near-term
licensing cash to maximize legal-precedent value; the two-tier licensing theory
(RAG signable in principle, training-data rights non-negotiable); contrast with
m789's priced market (the holdout refuses to transact at current prices) and
m816's 50/50 public anchor; second pay-or-sue confirmation after m603
(Reddit v. Anthropic); plaintiff-side undercut of m672's DOJ zero-price vector.
Connects to [589, 672, 603, 789, 816, 636] - all verified pre-commit in HEAD.

Qualitative per Aug 28 2026 standing rule: tone_scores NOT_SCORED,
p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False, engine NOT run,
NOT artifact-grade. Ledger holds at 30 (not a falsification-family member).
Evidence is excerpt-bounded per #503: 0 browser.open this run; MarketBeat
transcript excerpt + dailypolitical Aug-9 summary are the evidence tier;
ppc.land and mixed-news.com carry the Sep-4 motions. No coverage-tone claim.
No causal claim.

FIFTH and CLOSING leg of the 975-979 rotation window: D (#975) -> E (#976) ->
A (#977) -> B (#978) -> C (#979, this run).

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
TEST_FILE = "tests/test_type_c_979_ziff_davis_q2_2026_earnings_call_ai_licensing_holdout_posture_sep24_10pm.py"
DATE_STR = "2026-09-24 22:00 PDT"

# Format-built per the #715 convention (never carried as literal strings)
MECH_ID_MARKER = "mechanism" + "_819"
NEXT_ID_MARKER = "mechanism" + "_820"
NEXT_ID_DASH = "mechanism" + "-820"

BLOCK_KEY = "type_c_979_ziff_davis_q2_2026_earnings_call_ai_licensing_holdout_posture_sep24"
# Tail-block convention: zero-indent standalone block at the end of the file
EXPECTED_ITERATION = 979
# Anchor placeholder: replaced by the real main-commit SHA in the #565 anchor followup
ANCHORED_SHA = "0000000000000000000000000000000000000000"  # patched green in the anchor followup per #565

SOURCE_URLS = [
    "https://www.MarketBeat.com/earnings/reports/2026-8-6-j2-global-inc-stock/",
    "https://www.dailypolitical.com/2026/08/09/ziff-davis-q2-earnings-call-highlights.html",
    "https://ppc.land/openai-and-microsoft-ask-judge-to-end-10-8-million-article-copyright-case/",
    "https://mixed-news.com/en/news-publishers-summary-judgment-openai-microsoft-fair-use/",
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
    return re.search(r"^Type C #979:", line.split(" ", 1)[1] if " " in line else "")


class TestNovelty979:
    def test_type_c_979_test_file_only(self):
        """Zero test_type_c_979 files existed on disk before this run (glob pre-commit)."""
        out = subprocess.run(
            ["bash", "-c", "ls tests/test_type_c_979_* 2>/dev/null"],
            cwd=REPO, capture_output=True, text=True,
        ).stdout
        files = [line for line in out.splitlines() if line.strip()]
        assert files == [TEST_FILE]

    def test_type_c_979_main_commit_unique_and_anchored(self):
        """ANCHORED_SHA points at the single main-commit line of Type C #979."""
        import pytest
        pytestmark = pytest.mark.anchor  # noqa: F841
        out = subprocess.run(
            ["git", "log", "--all", "--format=%H %s", "--grep", "Type C #979"],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout
        mains = [line.split()[0] for line in out.splitlines() if re_match_main(line)]
        assert mains == [ANCHORED_SHA], f"expected single main commit {ANCHORED_SHA}"
        assert ANCHORED_SHA != "0" * 40

    def test_type_c_979_novelty_pinned_in_block(self):
        """The block's novelty field pins the zero-hit evidence for 819."""
        block = _block()
        assert "Zero ''rather be patient than early'' / ''right financial precedent'' hits repo-wide pre-commit" in block
        assert "max numeric mechanism_id 818 in profiles/ pre-commit" in block
        assert "four source URLs" in block and "zero-hit repo-wide pre-commit" in block


class TestRotationCycleGuard979:
    def test_window_closes_d_e_a_b_c_for_975_979(self):
        """975-979 rotation window closes D->E->A->B->C."""
        import re
        out = _git_log_all()
        found = []
        for line in out.splitlines():
            m = re.search(r"Type\s+([A-E])\s+#(\d{3})\b", line)
            if m and m.group(2) in {"975", "976", "977", "978", "979"}:
                pair = (m.group(1), m.group(2))
                if pair not in found:
                    found.append(pair)
        assert [p[0] for p in sorted(found, key=lambda p: p[1])] == ["D", "E", "A", "B", "C"]

    def test_window_adjacent_pairs_975_979(self):
        """Each adjacent pair in the 975-979 window advances D->E->A->B->C."""
        import re
        out = _git_log_all()
        found = []
        for line in out.splitlines():
            m = re.search(r"Type\s+([A-E])\s+#(\d{3})\b", line)
            if m and m.group(2) in {"975", "976", "977", "978", "979"}:
                pair = (m.group(1), m.group(2))
                if pair not in found:
                    found.append(pair)
        by_iter = {p[1]: p[0] for p in found}
        assert by_iter["975"] == "D" and by_iter["976"] == "E"
        assert by_iter["977"] == "A" and by_iter["978"] == "B"
        assert by_iter["979"] == "C"

    def test_anchor_sha_is_committed_main_commit_979(self):
        """ANCHORED_SHA names a committed object whose subject is the #979 main commit."""
        sha = subprocess.run(
            ["git", "rev-parse", "--verify", ANCHORED_SHA],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout.strip()
        assert len(sha) == 40
        subject = subprocess.run(
            ["git", "log", "-1", "--format=%s", ANCHORED_SHA],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout.strip()
        assert subject.startswith("Type C #979:")


class TestMechanism819Content:
    def test_type_c_979_block_present(self):
        """The 819 block parses as a top-level key in competitor-entities.yaml."""
        data = _block_yaml()
        assert data["mechanism_id"] == 819
        assert data["iteration"] == EXPECTED_ITERATION
        assert data["rotation"] == "Type C"

    def test_type_c_979_mechanism_name(self):
        block = _block()
        assert "Ziff Davis Q2 2026 earnings call (Aug 6 2026)" in block
        assert "AI-licensing holdout posture" in block

    def test_type_c_979_two_tier_quote(self):
        """Shah's two-tier licensing theory is quoted verbatim."""
        block = _block()
        assert "not inclined to sign a RAG-focused agreement" in block
        assert "compromises our right to fair compensation for foundational training" in block

    def test_type_c_979_precedent_over_cash_quote(self):
        block = _block()
        assert "establish the right financial precedent" in block
        assert "booking kind of a quick dollar" in block

    def test_type_c_979_patient_not_early_quote(self):
        block = _block()
        assert "rather be patient than early and lock in a little bit of cash" in block

    def test_type_c_979_litigation_proceeding(self):
        block = _block()
        assert "The litigation that we have with OpenAI is proceeding" in block
        assert "rational licensing market for us and frankly, for everyone" in block

    def test_type_c_979_reiteration_bounded(self):
        """The 'last quarter' reiteration is marked bounded, not evidenced."""
        block = _block()
        assert "reiterate what I said last quarter" in block
        assert "NOT separately verified this run" in block

    def test_type_c_979_september_clarity_vehicle(self):
        """The Sep 4 2026 MDL cross-motions arc is documented."""
        block = _block()
        assert "Sep 4 2026" in block
        assert "cross-motions for summary judgment" in block
        assert "1:25-md-03143" in block
        assert "twenty-nine days after the earnings call" in block

    def test_type_c_979_five_publisher_movants(self):
        """Ziff Davis is named among the five publisher movants."""
        block = _block()
        assert "The New York Times Company" in block
        assert "the Center for Investigative Reporting" in block
        assert "statutory damages run per article rather than per issue" in block

    def test_type_c_979_competing_accounts_bounded(self):
        """ppc.land's competing-accounts framing is carried as characterization, not fact."""
        block = _block()
        assert "0.00012 percent" in block
        assert "10.8 million articles copied" in block
        assert "not asserted as fact" in block

    def test_type_c_979_connects_to_verified_ids(self):
        data = _block_yaml()
        assert data["connects_to"] == [589, 672, 603, 789, 816, 636]

    def test_type_c_979_source_urls_verbatim(self):
        block = _block()
        for url in SOURCE_URLS:
            assert url in block, f"missing verbatim URL: {url}"

    def test_type_c_979_excerpt_bounded_second_hand(self):
        block = _block()
        assert "0 browser.open" in block
        assert "excerpt-bounded per #503" in block

    def test_type_c_979_no_coverage_tone_claim(self):
        block = _block()
        assert "makes no claim about Ziff Davis-owned outlets" in block
        assert "Type A follow-ups flagged" in block


class TestStatisticalDiscipline979:
    def test_type_c_979_qualitative_discipline(self):
        data = _block_yaml()
        sd = data["statistical_discipline"]
        assert sd["scope"] == "qualitative financial-incentive documentation only"
        assert sd["correlation_not_causation"] is True
        assert sd["scorer"] == "none"
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["engine_not_run"] is True
        assert sd["no_analysis_json_update"] is True
        assert sd["artifact_grade"] is False
        assert sd["falsification_family_member"] is False

    def test_type_c_979_verdict_supported_not_proven(self):
        data = _block_yaml()
        assert data["statistical_discipline"]["verdict"] == "directionally_supported_not_proven"

    def test_type_c_979_confounders_ranked(self):
        data = _block_yaml()
        confs = data["ranked_confounders"]
        assert [c["rank"] for c in confs] == [1, 2, 3, 4, 5, 6]
        assert confs[0]["strength"] == "STRONG"
        assert confs[1]["strength"] == "STRONG"
        assert "Earnings-call rhetoric" in confs[0]["text"]

    def test_type_c_979_bounded_absences(self):
        data = _block_yaml()
        assert len(data["bounded_absences"]) == 4
        assert any("No court ruling yet" in b for b in data["bounded_absences"])


class TestSupersessionAndCorpusPost978:
    def test_type_c_979_max_numeric_id_now_819(self):
        """Max numeric mechanism_id across profiles/ YAMLs is now 819."""
        import re
        text = _profiles_text()
        ids = [int(m) for m in re.findall(r"mechanism_id:\s*(\d+)", text)]
        assert max(ids) == 819

    def test_type_c_979_818_superseded_by_designed_819(self):
        """978's zero-819 sweep is superseded exactly once: this run's mechanism 819."""
        import re
        hits = re.findall(
            r"type_c_979_ziff_davis_q2_2026_earnings_call_ai_licensing_holdout_posture_sep24:",
            _profiles_text(),
        )
        assert len(hits) == 1

    def test_type_c_979_zero_820_keys_repo_wide(self):
        """Zero 820 mechanism keys in any form (underscore, numeric, dash) repo-wide."""
        for needle in (NEXT_ID_MARKER, NEXT_ID_DASH):
            out = subprocess.run(
                ["git", "grep", "-F", "-l", needle],
                cwd=REPO, capture_output=True, text=True,
            ).stdout.strip()
            assert out == "", f"unexpected 820 marker found: {needle}"
        import re
        assert not re.search(r"mechanism_id:\s*820\b", _profiles_text())

    def test_type_c_979_820_not_preassigned_in_tests(self):
        """This test file's design assertions stay within 819: no numeric 820 key is pinned."""
        import re
        src = open(REPO + "/" + TEST_FILE, encoding="utf-8").read()
        assert not re.search(r"mechanism_id:\s*820\b", src)

    def test_type_c_979_block_key_unique_and_top_level_parse(self):
        text = _profiles_text()
        assert text.count("\n" + BLOCK_KEY + ":") == 1
        data = yaml.safe_load(text)
        assert BLOCK_KEY in data


class TestLedger979:
    def test_type_c_979_thirtieth_positive(self):
        """THIRTIETH falsification-family member-form present once (journalists.yaml, #978)."""
        out = subprocess.run(
            ["bash", "-c",
             "grep -rn --exclude-dir=.git 'THIRTIETH falsification-family member' profiles/ 2>/dev/null"],
            cwd=REPO, capture_output=True, text=True,
        ).stdout.strip().splitlines()
        assert len(out) == 1
        assert "journalists.yaml" in out[0]

    def test_type_c_979_thirty_first_absent(self):
        """Zero THIRTY-FIRST strings anywhere in profiles/ - ledger holds at 30."""
        out = subprocess.run(
            ["bash", "-c",
             "grep -rn --exclude-dir=.git 'THIRTY-FIRST' profiles/ 2>/dev/null | wc -l"],
            cwd=REPO, capture_output=True, text=True,
        ).stdout.strip()
        assert out == "0"

    def test_type_c_979_ledger_note_and_no_analysis_update(self):
        data = _block_yaml()
        assert "Ledger holds at 30" in data["statistical_discipline"]["ledger_note"]
        assert data["statistical_discipline"]["no_analysis_json_update"] is True
        assert data["statistical_discipline"]["falsification_family_member"] is False

    def test_type_c_979_block_carries_no_member_claim(self):
        block = _block()
        assert "falsification-family member" not in block.replace(
            "not a uniform-prediction test", "")


class TestDocSync979:
    def test_type_c_979_readme_row(self):
        """README test-file table carries the #979 row (inserted in the main commit)."""
        import re
        with open(REPO + "/README.md", encoding="utf-8") as f:
            text = f.read()
        assert ("`" + TEST_FILE + "`") in text
        assert "Type C #979" in text
        assert re.search(r"mechanism" + r"\s+" + "819", text)

    def test_type_c_979_architecture_tree_row(self):
        """ARCHITECTURE.md tree carries the #979 row right after the #978 row."""
        with open(REPO + "/docs/ARCHITECTURE.md", encoding="utf-8") as f:
            text = f.read()
        row = TEST_FILE + "  # Type C #979:"
        assert row in text
        assert text.index(row) > text.index("Type B #978:")

    def test_type_c_979_architecture_label(self):
        block = _block()
        assert "Type C #979" in block or "iteration: 979" in block


class TestIterationLog979:
    def test_type_c_979_log_entry_present(self):
        """iteration-log.md opens with the #979 Type C entry (prepended in the main commit)."""
        with open(REPO + "/iteration-log.md", encoding="utf-8") as f:
            text = f.read()
        assert "## #979 Type C:" in text[:12000]
        assert "Type B #978" in text[:12000]

    def test_type_c_979_log_entry_carries_819(self):
        with open(REPO + "/iteration-log.md", encoding="utf-8") as f:
            head = f.read(12000)
        assert "819" in head
        assert "Ziff Davis" in head

    def test_type_c_979_log_entry_date_is_thursday(self):
        with open(REPO + "/iteration-log.md", encoding="utf-8") as f:
            head = f.read(12000)
        assert "Sep 24 2026, 22:00 PDT" in head
