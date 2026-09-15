"""Type C #754: Apple Siri nine-figure proposal + Amazon AI content marketplace
verification sweep (financial incentive mapping continuation).

On Mon Sep 14 2026 this run re-verifies the two open financial-incentive
threads carried from Type C #749 (Sep 14 2026, 15:00 PDT) as bounded-absence
sweeps with since=2026-09-01 filters:

Apple arm: the WSJ Aug 12 2026 exclusive (Apple in talks to pay publishers for
Siri AI content - variable per-use compensation, nine-figure budget, multiyear)
returns ONLY the Aug 12-13 2026 reports (WSJ exclusive + MacRumors, TheWrap,
TechCrunch, TechRepublic, AppleInsider, 9to5Mac) - zero closures in 33 days.
Status stays in_negotiation.

Amazon arm: the Feb 10 2026 AI content marketplace report (The Information,
AWS slides grouping the marketplace with Bedrock and Quick Suite) returns ONLY
the Feb 2026 reports (Reuters, PYMNTS, Hindu BusinessLine, Hypebeast,
PetaPixel, eWeek) - zero updates in 7+ months. Status stays building.

Corroborating context: the LLM Pulse master map (llmpulse.ai/blog/
ai-content-licensing-deals/, updated Sep 7 2026) is already in corpus; its
headline numbers (OpenAI-News Corp $250M/5yr, Reddit $203M disclosed,
Anthropic $1.5B settlement with final approval Jul 20 2026) reconfirm
in-corpus figures and add nothing new. Microsoft PCM: Yahoo remains the only
publicly named buyer (eWeek, crawled 2d) - no change since Feb 2026.

This run is VERIFICATION-ONLY: no new mechanism is mapped (max mechanism_id
stays 686), NOT a falsification-family member (ledger holds at 25), NOT
artifact-grade (no analysis.json update). The two entity blocks in
profiles/competitor-entities.yaml carry last_verified 2026-09-14 plus a
verification_sweep_sep14 note. Search-excerpt-bounded per #503 (2
browser.search query sets this run, no browser.open attempts). ASCII-only.
"""

import glob
import os
import re
import subprocess

import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = os.path.basename(__file__)
SIRI_PARENT = "sec_filing_q2_2026_cross_validation_aug29"
SIRI_KEY = "apple_siri_ai_deals_aug_2026"
MKT_KEY = "publisher_content_marketplace"
SWEEP_DATE = "2026-09-14"


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _entities_doc():
    with open(
        os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml"),
        encoding="utf-8",
    ) as fh:
        return yaml.safe_load(fh)


def _siri_block():
    doc = _entities_doc()
    return doc["entities"]["amazon"][SIRI_PARENT][SIRI_KEY]


def _mkt_block():
    doc = _entities_doc()
    return doc["entities"]["amazon"][MKT_KEY]


def _profiles_corpus():
    chunks = []
    for rel in (
        "profiles/competitor-entities.yaml",
        "profiles/competitor-coverage-research.yaml",
    ):
        chunks.append(_read(rel))
    return "\n".join(chunks)


def _mechanism_ids():
    return [
        int(x)
        for x in re.findall(r"mechanism_id:\s*(\d+)\b", _profiles_corpus())
    ]


class TestNovelty754:
    def test_single_type_c_754_file(self):
        hits = glob.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_c_754*.py")
        )
        assert hits == [os.path.join(REPO_ROOT, "tests", TEST_BASENAME)], hits

    def test_type_c_754_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_c_754 files, no #754 in git log, zero
        # verification_sweep_sep14 keys repo-wide, max mechanism_id 686
        # pre-commit); this test pins that no duplicate #754 main commit
        # ever appears.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%H %s"],
            capture_output=True,
            text=True,
        )
        mains = [
            line for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type C #754:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type C #754 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        anchor = TestRotationCycleGuard754.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)


class TestRotationCycleGuard754:
    """Rotation: distinct-mains window test, #721-style.

    Robust to the #678 history artifact and the #565 followup convention:
    first occurrence of each distinct iteration number, newest first. #754
    closes the 750-754 window, closing D->E->A->B->C.
    """

    ANCHORED_SHA = "68cc3454e4e785b91a759f2645c92cde0b06756d"  # main commit this run, per #565

    @staticmethod
    def _mains():
        # First occurrence of each distinct iteration number, newest first.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%s"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        seen = set()
        mains = []
        for s in out:
            m = re.match(r"^Type [A-E] #(\d+):", s)
            if m and m.group(1) not in seen:
                seen.add(m.group(1))
                mains.append(s)
        return mains

    def test_window_750_754_closes_d_to_c(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("C", "754"),
            ("B", "753"),
            ("A", "752"),
            ("E", "751"),
            ("D", "750"),
        ], "rotation window 750-754 wrong: %r" % (observed,)

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["C", "B", "A", "E", "D"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                "rotation broken: %s -> %s is not a valid cycle edge" % (a, b)
            )


class TestSiriVerificationSweep754:
    def test_siri_block_present(self):
        block = _siri_block()
        assert block["report_date"] == "2026-08-12"
        assert block["source"] == "Wall Street Journal"

    def test_siri_last_verified_sep14(self):
        assert _siri_block()["last_verified"] == SWEEP_DATE

    def test_siri_sweep_note_zero_closures(self):
        note = _siri_block()["verification_sweep_sep14"]
        assert "Type C #754" in note
        assert "zero closures" in note
        assert "Status stays in_negotiation" in note
        assert "in_negotiation" in note

    def test_siri_financial_terms_intact(self):
        block = _siri_block()
        assert block["budget_magnitude"] == "nine_figure"
        assert block["compensation_model"] == "variable_pay_per_use"
        assert block["deal_type"] == "content_licensing"

    def test_siri_source_urls_all_august_2026(self):
        urls = _siri_block()["source_urls"]
        assert len(urls) >= 6
        joined = " ".join(urls)
        # Zero September 2026 closure URLs: bounded absence is the finding.
        assert "2026/09" not in joined
        assert "2026-09" not in joined
        assert "2026/08/12" in joined or "2026/08/13" in joined

    def test_siri_sweep_excerpt_bounded_discipline(self):
        note = _siri_block()["verification_sweep_sep14"]
        assert "per #503" in note
        assert "since-filtered search" in note


class TestAmazonMarketplaceVerificationSweep754:
    def test_marketplace_block_present(self):
        block = _mkt_block()
        assert block["announced"] == "2026-02"

    def test_marketplace_status_still_building(self):
        assert _mkt_block()["status"] == "building"

    def test_marketplace_last_verified_sep14(self):
        assert _mkt_block()["last_verified"] == SWEEP_DATE

    def test_marketplace_sweep_note_zero_updates(self):
        note = _mkt_block()["verification_sweep_sep14"]
        assert "Type C #754" in note
        assert "zero updates" in note
        assert "Status stays building" in note

    def test_marketplace_source_urls_all_february_2026(self):
        urls = _mkt_block()["source_urls"]
        joined = " ".join(urls)
        # Zero September 2026 update URLs: bounded absence is the finding.
        assert "2026/09" not in joined
        assert "2026-09" not in joined
        assert "2026-02-10" in joined


class TestStatisticalDiscipline754:
    def test_verification_only_no_new_mechanism(self):
        ids = _mechanism_ids()
        assert max(ids) == 686, max(ids)

    def test_no_new_underscore_687_keys(self):
        assert "mechanism" + "_687" not in _profiles_corpus()

    def test_753_zero_686_sweep_stays_green(self):
        assert "mechanism" + "_686" not in _profiles_corpus()

    def test_750_751_zero_685_sweeps_stay_green(self):
        assert "mechanism" + "_685" not in _profiles_corpus()

    def test_ledger_holds_at_25(self):
        corpus = _profiles_corpus()
        assert "TWENTY-FIFTH" in corpus
        assert "TWENTY-SIXTH" not in corpus

    def test_no_analysis_json_update_warranted(self):
        # Verification-only run: the iteration log must record that no
        # analysis.json update was warranted.
        log = _read("iteration-log.md")
        idx = log.find("#754 Type C:")
        assert idx != -1
        entry = log[idx:idx + 4000]
        assert "no analysis.json update" in entry


class TestDocSync754:
    def test_readme_row(self):
        assert TEST_BASENAME in _read("README.md")

    def test_architecture_row(self):
        assert TEST_BASENAME in _read("docs/ARCHITECTURE.md")


class TestIterationLog754:
    def test_log_entry_present(self):
        assert "#754 Type C:" in _read("iteration-log.md")

    def test_log_bounded_absences(self):
        log = _read("iteration-log.md")
        idx = log.find("#754 Type C:")
        entry = log[idx:idx + 4000]
        assert "zero closures" in entry
        assert "zero updates" in entry
        assert "Apple Siri" in entry
        assert "Amazon" in entry

    def test_log_rotation_window(self):
        log = _read("iteration-log.md")
        idx = log.find("#754 Type C:")
        entry = log[idx:idx + 4000]
        assert "750-754" in entry
        assert "D->E->A->B->C" in entry


class TestDateGrounding754:
    def test_sep_14_2026_is_monday(self):
        import datetime

        assert datetime.date(2026, 9, 14).strftime("%A") == "Monday"
