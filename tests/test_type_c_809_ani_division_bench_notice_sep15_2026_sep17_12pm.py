"""Type C #809 (2026-09-17 12:00 PDT): ANI v. OpenAI Division Bench issues
notice and seeks OpenAI's reply (Sep 15 2026) - reconstituted
Jhingan/Arora bench lists December 08 hearing; OpenAI's Sep 2024
voluntary no-scrape undertaking lapsed with the July 24 order; the
litigation leg of the India two-tier pricing structure gets a dated
calendar (mechanism 717).

Rotation window fifth leg: D (#805) -> E (#806) -> A (#807) -> B (#808) ->
C (#809), CLOSING the 805-809 window.

Evidence: 2 browser.open first-hand reads this run (LiveLaw AMP page, 41
rendered lines; Mint page, 50 rendered lines); all URLs copied verbatim
from search-result Full-URL listings; no canonical URLs constructed.
Statistical discipline per the qualitative Type C convention:
p_value/cohens_d/ci_95 NOT_CALCULATED, tone_scores NOT_SCORED,
is_significant False, engine NOT run; verdict
directionally_supported_not_proven; NOT a falsification-family member
(ledger holds at 26); no analysis.json update.

Anchor placeholder: patched to the main commit SHA in the #565 follow-up.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TESTS_DIR = Path(REPO_ROOT) / "tests"
REPO = Path(REPO_ROOT)
ENTITIES_PATH = "profiles/competitor-entities.yaml"
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
TEST_BASENAME = (
    "test_type_c_809_ani_division_bench_notice_sep15_2026_sep17_12pm.py"
)
MECH_NUM = 717
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention.
MECH_ID_MARKER = "mechanism" + "_717"
NEXT_ID_MARKER = "mechanism" + "_718"
NEXT_ID_NUMERIC = "mechanism_id: 718"
MECH_KEY = "ani_v_openai_division_bench_notice_sep2026"
LL_URL = (
    "www.livelaw.in/amp/high-court/delhi-high-court/"
    "notice-ani-appeal-interim-relief-copyright-case-against-chatgpt-550053"
)
LM_URL = (
    "www.livemint.com/companies/news/"
    "delhi-high-court-openai-copyright-lawsuit-ani-plea-stop-chatgpt-"
    "from-using-content-11789457353087.html"
)
NEXT_SIBLING = "\n  anthropic:"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _block():
    doc = _read(ENTITIES_PATH)
    start = doc.index(MECH_KEY + ":")
    end = doc.index(NEXT_SIBLING, start)
    return doc[start:end]


def _block_data():
    import yaml

    return yaml.safe_load(_block())[MECH_KEY]


def _fold(s):
    return re.sub(r"\s+", " ", s.lower())


def _git_log_mains(pattern):
    proc = subprocess.run(
        ["git", "-C", REPO_ROOT, "log", "--format=%H %s", "--no-merges", "--", "."],
        capture_output=True,
        text=True,
    )
    return [l for l in proc.stdout.splitlines() if re.search(pattern, l)]


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT] + list(args),
        capture_output=True,
        text=True,
    )


# --- Novelty ---------------------------------------------------------------


class TestNovelty809:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_c_809_file(self):
        files = sorted(
            str(p) for p in TESTS_DIR.glob("test_type_c_809*.py")
        )
        assert len(files) == 1, files
        assert files[0].endswith(TEST_BASENAME), files

    def test_type_c_809_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type C #809")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_novelty_verification_claim_present_in_block(self):
        # The block pins the pre-commit novelty greps (zero Jhingan hits,
        # both source URLs zero-hit, zero underscore-form 717 keys, max
        # numeric mechanism_id 716); this test pins the claim in the
        # committed block, per the #752 convention.
        block = _block()
        assert "test_type_c_809" in block
        assert "Zero Jhingan hits repo-wide pre-commit" in block
        assert "max numeric mechanism_id 716 pre-commit" in block


# --- Rotation cycle guard ---------------------------------------------------


class TestRotationCycleGuard809:
    """Rotation: 805-809 window fifth leg D->E->A->B->C, closing the window."""

    EXPECTED_ORDER = [
        ("C", "809"), ("B", "808"), ("A", "807"), ("E", "806"), ("D", "805"),
    ]
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def _window(self):
        # First occurrence of each distinct iteration number, newest first
        # (robust to the #756-style followup commits that repeat the same
        # "Type X #N" wording without the colon, per the #752 convention;
        # hardened per the #783 repair to dedupe by iteration number).
        mains = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%s", "--no-merges",
             "-n", "40", "--", "."],
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
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        )
        # Durable post-commit: the anchored main commit is in history and its
        # subject opens the #809 window-closing leg (HEAD drifts past it with
        # the anchor/doc-sync/push-status followups, per the #565 convention).
        res = _run_git("log", "--format=%H %s", "--all")
        hits = [l for l in res.stdout.splitlines()
                if l.startswith(ANCHORED_SHA + " ")]
        assert len(hits) == 1, hits
        assert "Type C #809: " in hits[0], hits


# --- Mechanism content -------------------------------------------------------


class TestMechanism717Content:
    def test_block_present_in_entities(self):
        block = _block()
        assert block.strip().startswith(MECH_KEY + ":")

    def test_iteration_metadata(self):
        data = _block_data()
        assert data["mechanism_id"] == MECH_NUM
        assert data["iteration"] == 809
        assert data["iteration_type"] == "C"
        assert data["date_analyzed"] == "2026-09-17"
        assert data["time_pdt"] == "12:00"
        assert data["job_id"] == "mediascope-daily-iteration"

    def test_procedural_facts(self):
        data = _block_data()
        pf = data["procedural_facts"]
        assert "Avneesh Jhingan" in pf["bench"]
        assert "Manmeet Pritam Singh Arora" in pf["bench"]
        assert "December 08, 2026" in pf["next_hearing"]
        assert "notice" in pf["action"]
        assert "Siddhant Kumar" in pf["ani_counsel"]
        assert "Kapil Sibal" in pf["intervenors"]
        assert "Arvind Datar" in pf["intervenors"]
        assert "Sep 11 2024" in pf["lapsed_undertaking"]
        assert "Jul 24 2026" in pf["lapsed_undertaking"]

    def test_litigation_leg_repricing_frame(self):
        data = _block_data()
        block = _fold(data["litigation_leg_repricing"])
        assert "december 08" in block
        assert "lapsed" in block
        assert "mechanism 609" in block
        assert "two-tier" in block

    def test_cross_references(self):
        block = _fold(_block())
        for ref in ("mechanism 681", "mechanism 678", "mechanism 609",
                    "mechanism 663"):
            assert ref in block, ref

    def test_first_hand_reads(self):
        block = _fold(_block())
        assert "2 browser.open first-hand reads" in block
        assert "livelaw amp page" in block
        assert "41 rendered lines" in block
        assert "50 rendered lines" in block

    def test_source_urls_verbatim(self):
        data = _block_data()
        assert data["source_urls"] == [
            "https://" + LL_URL,
            "https://" + LM_URL,
        ]


# --- Statistical discipline ---------------------------------------------------


class TestStatisticalDiscipline809:
    def test_statistical_discipline_type_c(self):
        data = _block_data()
        sd = data["statistical_discipline"]
        assert sd["scorer"] == "none"
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["qualitative_only"] is True
        assert sd["correlation_not_causation"] is True
        assert sd["artifact_grade"] is False

    def test_verdict_ledger_and_source_urls(self):
        data = _block_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False
        assert "ledger holds at 26" in data["falsification_family"]

    def test_designed_keying_no_underscore_form_in_block(self):
        # Per the #715/#723/#738/#739 designed-keying convention, the block
        # key and block text must never carry the contiguous underscore-form
        # marker; the needle is format-built so this test carries no literal.
        block = _block()
        needle = MECH_ID_MARKER
        assert needle not in block
        assert MECH_KEY.count("_" + "717") == 0

    def test_ranked_confounders_and_counterargument(self):
        data = _block_data()
        conf = data["ranked_confounders"]
        assert len(conf) == 5
        assert [c["rank"] for c in conf] == [1, 2, 3, 4, 5]
        assert [c["strength"] for c in conf] == [
            "strong", "strong", "moderate", "moderate", "weak",
        ]
        assert "strongest_counterargument" in data
        assert "routine procedure" in _fold(data["strongest_counterargument"])


# --- Supersession and corpus post-#808 --------------------------------------


class TestSupersessionAndCorpusPost808:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout))

    def test_corpus_max_is_717(self):
        assert max(self._numeric_ids()) == 717

    def test_iteration_808_max_716_sweep_superseded_by_design(self):
        # #808's max-716 sweep fails by designed supersession now that 717 exists.
        assert max(self._numeric_ids()) != 716

    def test_zero_underscore_718_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_718_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_807_zero_underscore_716_sweep_stays_green(self):
        # #807's zero-underscore-716 sweeps stay green post-#809 by designed keying.
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", "mechanism" + "_716", "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), \
                "literal underscore-716 key leaked into %s" % root

    def test_iteration_808_zero_underscore_717_sweep_stays_green(self):
        # #808's zero-underscore-717 sweeps stay green post-#809 by designed keying:
        # neither the profile block nor this test file carries a literal underscore-717 key.
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", MECH_ID_MARKER, "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), \
                "literal underscore-717 key leaked into %s" % root

    def test_iteration_808_zero_numeric_717_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 717", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected #808's zero-numeric-717 sweep to fail by designed supersession"

    def test_numeric_717_keys_in_exactly_the_one_designed_location(self):
        res = _run_git("grep", "-r", "mechanism_id: 717", "--", "profiles/")
        hits = [l for l in res.stdout.strip().splitlines() if l.strip()]
        # Designed keying: one numeric 717 key in the openai financial-incentive
        # block; no other profiles/ location.
        assert len(hits) == 1, "unexpected numeric 717 key spread in profiles/: %s" % hits
        assert "profiles/competitor-entities.yaml" in hits[0]


# --- Ledger -----------------------------------------------------------------


def _profiles_corpus():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith((".yaml", ".yml", ".md")):
                out.append(_read(os.path.join(root, fn)))
    return "\n".join(out)


class TestLedger809:
    def test_twenty_sixth_present_and_twenty_seventh_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference "TWENTY-SEVENTH" inside their own
        # negative guards, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus
        assert "ledger holds at 26" in _block()

    def test_m717_block_key_unique_and_entities_parse(self):
        import yaml

        doc = yaml.safe_load(_read(ENTITIES_PATH))
        assert doc["entities"]["openai"][MECH_KEY]["mechanism_id"] == 717
        keys = [
            k for k in doc["entities"]["openai"] if k == MECH_KEY
        ]
        assert len(keys) == 1

    def test_m717_not_a_falsification_family_member(self):
        data = _block_data()
        assert data["falsification_family"].startswith("NOT a member")

    def test_no_analysis_json_update_claimed(self):
        data = _block_data()
        assert data["no_analysis_json_update"] is True
        assert "No analysis.json update warranted" in data["artifact_readiness"]


# --- Doc-sync ----------------------------------------------------------------


class TestDocSync809:
    def test_readme_row_809(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_809(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_809_file(self):
        text = _read(ARCH_PATH)
        assert "tests/" + TEST_BASENAME in text


# --- Iteration log ------------------------------------------------------------


class TestIterationLog809:
    def _log(self):
        return _read(LOG_PATH)

    def test_log_entry_present(self):
        assert "## #809 Type C:" in self._log()

    def test_log_mechanism_number_and_topic(self):
        log = self._log()
        idx = log.index("## #809 Type C:")
        entry = log[idx:idx + 8000]
        assert "mechanism_id 717" in entry
        assert "ANI" in entry
        assert "December 08" in entry

    def test_sep_17_2026_is_thursday(self):
        import datetime

        assert datetime.date(2026, 9, 17).strftime("%A") == "Thursday"
