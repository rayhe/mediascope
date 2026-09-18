"""Type C #819 (2026-09-17 22:00 PDT): Publishers' Licensing Services (PLS) UK
collective AI licensing scheme - first dedicated UK collective-licensing
mechanism in the corpus (mechanism 723); launched at the London Book Fair
Mar 2026 with CLA/ALCS, 250+ publisher opt-ins.

Rotation window fifth leg: D (#815) -> E (#816) -> A (#817) -> B (#818) ->
C (#819), CLOSING the 815-819 window.

Evidence: 5 browser.search query sets this run, 0 browser.open first-hand
reads; all facts via search-result excerpts (second-hand per #503); all
URLs copied verbatim from search-result Full-URL listings; no canonical
URLs constructed. Statistical discipline per the qualitative Type C
convention: p_value/cohens_d/ci_95 NOT_CALCULATED, tone_scores
NOT_SCORED, is_significant False, engine NOT run; verdict
directionally_supported_not_proven; NOT a falsification-family member
(ledger holds at 26); no analysis.json update.

Deselected pre-commit per the #565 convention: anchor 1 + rotation
anchor 1 (patched green in the anchor followup); doc-sync 3 +
iteration-log 2 fail by design pre-commit, go green in the doc-sync
followup.

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
    "test_type_c_819_pls_collective_ai_licensing_uk_sep17_10pm.py"
)
MECH_NUM = 723
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention.
MECH_ID_MARKER = "mechanism" + "_723"
NEXT_ID_MARKER = "mechanism" + "_724"
NEXT_ID_NUMERIC = "mechanism_id: 724"
MECH_KEY = "pls_collective_ai_licensing_uk_sep2026"
URL_LEXIS = "https://www.lexisnexis.co.uk/legal/news/pls-launches-collective-ai-licensing-scheme-for-publishers-with-cla-alcs"
URL_EIN = "https://cop.einnews.com/pr_news/898966361/pls-offers-new-collective-ai-licensing-opportunity-to-publishers"
URL_PLS = "https://www.pls.org.uk/news-events-policy/news/over-250-publishers-opt-in-to-collective-ai-licensing-ahead-of-industry-conference-addressing-ai-copyright/"
URL_BOOKSELLER = "https://www.thebookseller.com/news/pls-launches-collective-ai-licensing-scheme-for-publishers"
URL_PPA = "https://ppa.co.uk/pls-launch-collective-ai-licensing-opportunity"
URL_ETIH = "https://www.edtechinnovationhub.com/news/pls-launches-collective-licensing-scheme-for-ai-use-of-published-content"
NEXT_SIBLING = "\n  linc_kk_japan_collective_licensing_sep2026:"
ANCHORED_SHA = "8e3a36a1eee42a1235f39a06162e10071a82893d"


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


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT] + list(args),
        capture_output=True,
        text=True,
    )


# --- Novelty ---------------------------------------------------------------


class TestNovelty819:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_c_819_file(self):
        files = sorted(
            str(p) for p in TESTS_DIR.glob("test_type_c_819*.py")
        )
        assert len(files) == 1, files
        assert files[0].endswith(TEST_BASENAME), files

    def test_type_c_819_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type C #819")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_novelty_verification_claim_present_in_block(self):
        # The block pins the pre-commit novelty greps (Zero Publishers
        # Licensing Services hits, all 6 PLS source URLs zero-hit, the m720
        # roster-mention-only status, max numeric mechanism_id 722); this test
        # pins the claim in the committed block, per the #752 convention.
        block = _block()
        assert "test_type_c_819" in block
        assert "Zero \"Publishers Licensing Services\" hits repo-wide pre-commit" in block
        assert "max numeric mechanism_id 722 pre-commit" in block


# --- Rotation cycle guard ---------------------------------------------------


class TestRotationCycleGuard819:
    """Rotation: 815-819 window fifth leg D->E->A->B->C, closing the window."""

    EXPECTED_ORDER = [
        ("C", "819"), ("B", "818"), ("A", "817"), ("E", "816"), ("D", "815"),
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
        # subject opens the #819 window-closing leg (HEAD drifts past it with
        # the anchor/doc-sync/push-status followups, per the #565 convention).
        res = _run_git("log", "--format=%H %s", "--all")
        hits = [l for l in res.stdout.splitlines()
                if l.startswith(ANCHORED_SHA + " ")]
        assert len(hits) == 1, hits
        assert "Type C #819: " in hits[0], hits


# --- Mechanism content -------------------------------------------------------


class TestMechanism723Content:
    def test_block_present_in_entities(self):
        block = _block()
        assert block.strip().startswith(MECH_KEY + ":")

    def test_iteration_metadata(self):
        data = _block_data()
        assert data["mechanism_id"] == MECH_NUM
        assert data["iteration"] == 819
        assert data["iteration_type"] == "C"
        assert data["date_analyzed"] == "2026-09-17"
        assert data["time_pdt"] == "22:00"
        assert data["job_id"] == "mediascope-daily-iteration"

    def test_scheme_launch_facts(self):
        data = _block_data()
        sf = data["scheme_facts"]
        assert "London Book Fair" in sf["launched"]
        assert "March 2026" in sf["launched"]
        assert "non-profit" in sf["operator"]
        assert "Copyright Licensing Agency" in " ".join(sf["developed_with"])
        assert "Authors Licensing and Collecting Society" in " ".join(sf["developed_with"])
        assert "Generative AI Training Licence" in sf["programme_name"]
        assert "training and fine-tuning" in sf["vehicle"]

    def test_owner_governance(self):
        data = _block_data()
        owners = " ".join(data["scheme_facts"]["owners"])
        assert "Publishers Association" in owners
        assert "Independent Publishers Guild" in owners
        assert "Professional Publishers Association" in owners
        assert "Association of Learned and Professional Society Publishers" in owners
        assert "Tom West" in data["scheme_facts"]["leadership"]

    def test_publisher_roster_and_opt_in_count(self):
        data = _block_data()
        roster = " ".join(data["publisher_roster"])
        assert "Practical Action Publishing" in roster
        assert "5m Books" in roster
        assert len(data["publisher_roster"]) == 2
        assert "250" in data["opt_in_count"]

    def test_named_opt_in_publisher_quotes(self):
        data = _block_data()
        quotes = " ".join(data["key_quotes"])
        assert "Rosanna Denning" in quotes
        assert "Jeremy Toynbee" in quotes
        assert "Tom West" in quotes
        assert "Saj Merali" in quotes
        assert len(data["key_quotes"]) == 4

    def test_tier_3_collective_reading(self):
        data = _block_data()
        t3 = _fold(data["tier_3_collective_reading"]["tier_3_extension"])
        assert "first dedicated uk collective-licensing mechanism" in t3
        assert "mechanism 663" in t3
        assert "prorata" in t3
        tax = _fold(data["tier_3_collective_reading"]["taxonomy_relationship"])
        assert "mechanism 720" in tax
        assert "small-publisher-access" in tax
        cross = _fold(data["tier_3_collective_reading"]["cross_references"])
        assert "702/708" in cross
        assert "statement of interest" in cross

    def test_source_urls_verbatim(self):
        data = _block_data()
        assert data["sources"][0] == (
            "https://www.lexisnexis.co.uk/legal/news/pls-launches-collective-ai-licensing-scheme-for-publishers-with-cla-alcs (PLS collective AI licensing scheme launch, CLA/ALCS collaboration, Mar 10 2026 issue)"
        )
        assert data["sources"][2] == (
            "https://www.pls.org.uk/news-events-policy/news/over-250-publishers-opt-in-to-collective-ai-licensing-ahead-of-industry-conference-addressing-ai-copyright/ (250+ opt-ins; Practical Action Publishing and 5m Books quotes; target publishers unable to secure direct deals)"
        )
        assert len(data["sources"]) == 6

    def test_meta_zero(self):
        data = _block_data()
        mz = _fold(data["overview"])
        assert "no coverage-tone claim" in mz
        assert "correlation is not causation" in mz


# --- Statistical discipline ---------------------------------------------------


class TestStatisticalDiscipline819:
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
        assert MECH_KEY.count("_" + "723") == 0

    def test_ranked_confounders_and_counterargument(self):
        data = _block_data()
        conf = data["confounders_ranked"]
        assert len(conf) == 5
        assert [c["strength"] for c in conf] == [
            "STRONG", "STRONG", "MODERATE", "MODERATE", "WEAK",
        ]
        assert "strongest_counterargument" in data
        assert "no named ai-buyer" in _fold(data["strongest_counterargument"])


# --- Supersession and corpus post-#818 --------------------------------------


class TestSupersessionAndCorpusPost818:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout))

    def test_corpus_max_is_723(self):
        assert max(self._numeric_ids()) == 723

    def test_iteration_818_max_722_sweep_superseded_by_design(self):
        # #818's max-722 sweeps fail by designed supersession now that 723 exists.
        assert max(self._numeric_ids()) != 722

    def test_zero_underscore_724_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_724_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_818_zero_underscore_723_sweep_stays_green(self):
        # The #818 zero-underscore-723 sweeps stay green post-#819 by designed keying:
        # neither the profile block nor this test file carries a literal underscore-723 key.
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", MECH_ID_MARKER, "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), \
                "literal underscore-723 key leaked into %s" % root

    def test_iteration_818_zero_numeric_723_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 723", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected #818's zero-numeric-723 sweep to fail by designed supersession"

    def test_numeric_723_keys_in_exactly_the_designed_location(self):
        res = _run_git("grep", "-r", "mechanism_id: 723", "--", "profiles/")
        hits = [l for l in res.stdout.strip().splitlines() if l.strip()]
        # Designed keying: one numeric 723 key in the marketplace
        # intermediary landscape block; no other profiles/ location.
        assert len(hits) == 1, "unexpected numeric 723 key spread in profiles/: %s" % hits
        assert "profiles/competitor-entities.yaml" in hits[0]

    def test_iteration_817_zero_underscore_722_sweep_stays_green(self):
        # The #817 zero-underscore-722 sweeps stay green post-#819 by designed keying.
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", "mechanism" + "_722", "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), \
                "literal underscore-722 key leaked into %s" % root


# --- Ledger -----------------------------------------------------------------


def _profiles_corpus():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith((".yaml", ".yml", ".md")):
                out.append(_read(os.path.join(root, fn)))
    return "\n".join(out)


class TestLedger819:
    def test_twenty_sixth_present_and_twenty_seventh_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference "TWENTY-SEVENTH" inside their own
        # negative guards, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus
        assert "ledger holds at 26" in _block()

    def test_m723_block_key_unique_and_entities_parse(self):
        import yaml

        doc = yaml.safe_load(_read(ENTITIES_PATH))
        assert doc["marketplace_intermediary_landscape"][MECH_KEY]["mechanism_id"] == 723
        keys = [
            k for k in doc["marketplace_intermediary_landscape"] if k == MECH_KEY
        ]
        assert len(keys) == 1

    def test_m723_not_a_falsification_family_member(self):
        data = _block_data()
        assert data["falsification_family"].startswith("NOT a member")

    def test_no_analysis_json_update_claimed(self):
        data = _block_data()
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False
        assert data["verdict"] == "directionally_supported_not_proven"


# --- Doc-sync ----------------------------------------------------------------


class TestDocSync819:
    def test_readme_row_819(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_819(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_819_file(self):
        text = _read(ARCH_PATH)
        assert "tests/" + TEST_BASENAME in text


# --- Iteration log ------------------------------------------------------------


class TestIterationLog819:
    def _log(self):
        return _read(LOG_PATH)

    def test_log_entry_present(self):
        assert "## #819 Type C:" in self._log()

    def test_log_mechanism_number_and_topic(self):
        log = self._log()
        idx = log.index("## #819 Type C:")
        entry = log[idx:idx + 8000]
        assert "mechanism 723" in entry
        assert "PLS" in entry
        assert "Publishers' Licensing Services" in entry

    def test_sep_17_2026_is_thursday(self):
        import datetime

        assert datetime.date(2026, 9, 17).strftime("%A") == "Thursday"
