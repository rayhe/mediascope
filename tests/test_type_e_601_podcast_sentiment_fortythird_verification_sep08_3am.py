"""
Type E #601 - Podcast Sentiment Tracking: Forty-Third Verification Cycle Sep 8 03:00 PDT
Guilty Feminist 498 Hold No 499 (43rd cycle: Listen Notes 2d crawl latest 498
"Politics" recorded 20 Aug 2026 released 31 Aug, Chortle 2h crawl Sep 13 Kings
Place LPF no new episode announced, 499 penciled for Mon Sep 7 now 36h past the
usual drop slot with no 499 by 03:00 PDT / 10:00 UK Sep 8 in bounded
search-result snippets, secondary-only, episode 500 milestone approaching as a
watch item) +
EHE 30-Day Hold (no new primary campaign motif: re-surfaces only, all in
corpus: Times spoof-Epstein 43d, feminist.org FMF piece listed updated 7d /
crawled 2h, engadget bus stops 53d, latestly Jul 30 fact-check 40d, petapixel
Jul 23 lenticular, sifted.eu ban piece logged #480, afrotech ethics piece;
no competitor-equivalent guerrilla campaign in forty-three cycles) +
Attention Sphere 43rd No-Match AS PODCAST (quoted search top results are this
repository's own GitHub commits, rejected as circular; identity strand
unchanged from #596: breakingnewstoday.eu mirror + raleighnewstoday Privacy
Failures Analysis, both snippet-bounded) +
ONE NEW-TO-CORPUS press surface: biometricupdate.com/202609 (Sep 7, 2026)
"Meta sued over alleged facial recognition training for smart glasses":
Alvarez et al. v. Meta Platforms, N.D. Illinois, 66-page complaint alleging
Meta trained/tested NameTag facial recognition on Facebook/Instagram photos
for Ray-Ban/Oakley smart glasses and the Meta AI companion app (BIPA,
California publicity/misappropriation, CA Constitution privacy); cites
WIRED's June NameTag code discovery; zero pre-commit corpus hits for
"alvarez" or the new slug; snippet-bounded; allegations, not findings) +
recency frontier TIED at Sep 7 (bounded listings: Times "Fear and loathing"
~Sep 6-7 vs this surface Sep 7; no advance claimed) +
startupfortune/MediaNama-IFF/MediaNama-Jul23/webpronews/letsdatascience/
bloomberglaw-false-ad/Reuters-HateAid/cybernews/sifted/afrotech/petapixel/
engadget/latestly/feminist.org/thedrum explicitly distinguished as in-corpus
lineage +
MANUAL ILLUSTRATIVE no false significance, no em dashes, verbatim URLs as
surfaced, distinct from 596, forty-third verification cycle, extends #596 by
6 hours, not duplicate, iteration-log entry present and newest-first, #600
entry repositioned to newest-first order as miss repair.
"""

import re
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent
DOC_PATH = REPO_ROOT / "podcast-sentiment.md"
LOG_PATH = REPO_ROOT / "iteration-log.md"
README = REPO_ROOT / "README.md"
ARCH = REPO_ROOT / "docs" / "ARCHITECTURE.md"
TESTS_DIR = REPO_ROOT / "tests"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 601
DATE_STR = "2026-09-08 03:00 PDT"
TEST_FILE = Path(__file__).name
CYCLE = 43

FILE_597 = "test_type_a_597_wired_openai_apple_lawsuit_followup_coverage_selection_sep07_11pm.py"
FILE_598 = "test_type_b_598_alex_hern_migration_guardian_economist_register_constancy_sep08_12am.py"
FILE_599 = "test_type_c_599_vox_media_ai_revenue_architecture_sep08.py"
FILE_600 = "test_type_d_600_scorer_consistency_598_599_agreement_rotation_doc_sync_sep08_2am.py"

BIOMETRICUPDATE_URL = "https://www.biometricupdate.com/202609/meta-sued-over-alleged-facial-recognition-training-for-smart-glasses"


def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")


def read_log():
    return LOG_PATH.read_text(encoding="utf-8")


def read_readme():
    return README.read_text(encoding="utf-8")


def read_arch():
    return ARCH.read_text(encoding="utf-8")

class TestIterationNumberAndRotation:
    def test_iteration_number(self):
        assert ITERATION == 601

    def test_cycle_number_is_forty_third(self):
        assert CYCLE == 43

    def test_date_string(self):
        assert DATE_STR == "2026-09-08 03:00 PDT"

    def test_goal_and_job_ids(self):
        assert GOAL_ID == "goal_54093bda4145"
        assert JOB_ID == "mediascope-daily-iteration"

    def test_file_name_convention(self):
        assert TEST_FILE.startswith("test_type_e_601_")
        assert TEST_FILE.endswith("_sep08_3am.py")

    def test_previous_main_type_was_d(self):
        subjects = self._mains()
        assert re.search(r"Type D #600:", subjects[0]), (
            f"expected newest main commit to be Type D #600, got: {subjects[0]!r}"
        )

    def test_rotation_next_after_d_is_e(self):
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        assert (order["E"] - order["D"]) % 5 == 1

    def test_neighbor_test_files_exist(self):
        for f in (FILE_597, FILE_598, FILE_599, FILE_600):
            assert (TESTS_DIR / f).exists(), f"neighbor test file missing: {f}"

    def _mains(self):
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [
            s for s in out if re.match(r"^Type [A-E] #\d+:", s)
        ]
        assert len(mains) >= 5, "fewer than 5 main commits found"
        return mains


class TestGuiltyFeministHold:
    def test_498_hold_asserted(self):
        doc = read_doc()
        block = self._block(doc)
        assert "498" in block

    def test_no_499_by_run_time(self):
        doc = read_doc()
        block = self._block(doc)
        assert re.search(r"no 499 by 03:00 PDT.*10:00 UK", block), (
            "block must state the no-499 hold at 03:00 PDT Sep 8 / 10:00 UK Sep 8"
        )

    def test_listen_notes_still_498(self):
        doc = read_doc()
        block = self._block(doc)
        assert "498. Politics" in block or "498 \"Politics\"" in block

    def test_listen_notes_crawl_recency(self):
        doc = read_doc()
        block = self._block(doc)
        assert re.search(r"Listen Notes.{0,40}crawled? 2 days?", block), (
            "Listen Notes evidence must be a 2-day crawl this run"
        )

    def test_chortle_still_kings_place_only(self):
        doc = read_doc()
        block = self._block(doc)
        assert "Kings Place" in block
        assert re.search(r"Chortle.{0,40}crawled? 2 hours?", block), (
            "Chortle evidence must be a 2-hour crawl this run"
        )

    def test_cadence_note_499_penciled_sep_7(self):
        doc = read_doc()
        block = self._block(doc)
        assert re.search(r"499.{0,40}Mon(d)?(day)? Sep(t)?(ember)? 7", block), (
            "cadence note must record 499 penciled for Monday Sep 7"
        )

    def test_hold_is_bounded_absence_not_non_release(self):
        doc = read_doc()
        block = self._block(doc)
        assert re.search(r"bounded search-result absence", block), (
            "the hold must be stated as a bounded search-result absence, not a non-release claim"
        )

    def test_secondary_only_tier_disclosed(self):
        doc = read_doc()
        block = self._block(doc)
        assert re.search(r"secondary-only", block)

    def test_forty_third_cycle_labeled(self):
        doc = read_doc()
        block = self._block(doc)
        assert re.search(r"forty-third verification cycle", block, re.IGNORECASE), (
            "block must label this the forty-third verification cycle"
        )

    def _block(self, doc):
        m = re.search(
            r"## Iteration #601\b.*?(?=^## Iteration #|\Z)",
            doc,
            re.DOTALL | re.MULTILINE,
        )
        assert m, "Iteration #601 block not found in podcast-sentiment.md"
        return m.group(0)

class TestEHEHold:
    def test_thirty_day_hold(self):
        doc = read_doc()
        block = self._block(doc)
        assert re.search(r"30-day hold", block, re.IGNORECASE), (
            "EHE hold must read 30 days this cycle (Aug 10 Epstein spoof -> Sep 8)"
        )

    def test_last_primary_campaign_identified(self):
        doc = read_doc()
        block = self._block(doc)
        assert re.search(r"Aug(ust)? 10.*Epstein|Epstein.*Aug(ust)? 10", block)

    def test_no_new_primary_campaign_motif(self):
        doc = read_doc()
        block = self._block(doc)
        assert re.search(r"no new primary campaign motif", block, re.IGNORECASE)

    def test_resurfaces_all_in_corpus(self):
        doc = read_doc()
        block = self._block(doc)
        for outlet in ("thetimes", "feminist.org", "engadget", "latestly"):
            assert outlet in block.lower(), f"EHE re-surface section missing: {outlet}"

    def test_no_competitor_equivalent_forty_three_cycles(self):
        doc = read_doc()
        block = self._block(doc)
        assert re.search(r"no competitor-equivalent.*43|cycles", block, re.IGNORECASE)

    def test_no_double_counting(self):
        doc = read_doc()
        block = self._block(doc)
        assert re.search(r"no double-counting", block, re.IGNORECASE)

    def _block(self, doc):
        m = re.search(
            r"## Iteration #601\b.*?(?=^## Iteration #|\Z)",
            doc,
            re.DOTALL | re.MULTILINE,
        )
        assert m, "Iteration #601 block not found in podcast-sentiment.md"
        return m.group(0)


class TestAttentionSphereIdentity:
    def test_forty_third_no_match(self):
        doc = read_doc()
        block = self._block(doc)
        assert re.search(r"43rd no-match", block, re.IGNORECASE), (
            "Attention Sphere podcast no-match must read 43rd this cycle"
        )

    def test_circular_github_rejection(self):
        doc = read_doc()
        block = self._block(doc)
        assert re.search(r"own GitHub commits.*circular|circular.*GitHub", block), (
            "quoted-search results that are this repository's own GitHub commits "
            "must be rejected as circular"
        )

    def test_identity_strand_unchanged(self):
        doc = read_doc()
        block = self._block(doc)
        assert "breakingnewstoday" in block
        assert "Privacy Failures Analysis" in block

    def test_task_spec_still_misidentified(self):
        doc = read_doc()
        block = self._block(doc)
        assert re.search(r"misidentified", block, re.IGNORECASE)

    def _block(self, doc):
        m = re.search(
            r"## Iteration #601\b.*?(?=^## Iteration #|\Z)",
            doc,
            re.DOTALL | re.MULTILINE,
        )
        assert m, "Iteration #601 block not found in podcast-sentiment.md"
        return m.group(0)

class TestNewSurfaces:
    def test_biometricupdate_new_to_corpus(self):
        doc = read_doc()
        block = self._block(doc)
        assert BIOMETRICUPDATE_URL in block

    def test_alvarez_lawsuit_identified(self):
        doc = read_doc()
        block = self._block(doc)
        assert re.search(r"Alvarez et al\. v\. Meta Platforms", block)

    def test_illinois_forum_and_nametag(self):
        doc = read_doc()
        block = self._block(doc)
        assert "N.D. Illinois" in block
        assert "NameTag" in block

    def test_66_page_complaint_and_statutes(self):
        doc = read_doc()
        block = self._block(doc)
        assert "66-page" in block
        assert "BIPA" in block

    def test_allegations_not_findings(self):
        doc = read_doc()
        block = self._block(doc)
        assert re.search(r"allegations, not (court )?findings", block, re.IGNORECASE)

    def test_recency_frontier_tied_not_advanced(self):
        doc = read_doc()
        block = self._block(doc)
        assert re.search(r"recency frontier.*TIED|TIED.*recency frontier", block, re.IGNORECASE), (
            "frontier must be stated as TIED at Sep 7, not claimed advanced"
        )

    def test_in_corpus_lineage_distinguished(self):
        doc = read_doc()
        block = self._block(doc)
        for marker in ("#561", "#576", "#581", "#591", "#480"):
            assert marker in block, f"in-corpus lineage missing mechanism ref: {marker}"

    def test_zero_precommit_hits_claimed(self):
        doc = read_doc()
        block = self._block(doc)
        assert re.search(r"zero pre-commit.*hits", block, re.IGNORECASE)

    def _block(self, doc):
        m = re.search(
            r"## Iteration #601\b.*?(?=^## Iteration #|\Z)",
            doc,
            re.DOTALL | re.MULTILINE,
        )
        assert m, "Iteration #601 block not found in podcast-sentiment.md"
        return m.group(0)


class TestScoresAndDiscipline:
    def test_manual_illustrative_only(self):
        doc = read_doc()
        block = self._block(doc)
        assert "MANUAL ILLUSTRATIVE" in block

    def test_no_significance_claimed(self):
        doc = read_doc()
        block = self._block(doc)
        assert "p_value NOT_CALCULATED" in block
        assert "is_significant False" in block

    def test_no_em_dashes_in_block(self):
        doc = read_doc()
        block = self._block(doc)
        assert "\u2014" not in block, "em dash found in Iteration #601 block"
        assert "\u2013" not in block, "en dash found in Iteration #601 block"

    def test_no_em_dashes_in_this_test_file(self):
        text = (TESTS_DIR / TEST_FILE).read_text(encoding="utf-8")
        assert "\u2014" not in text, "em dash found in test file"
        assert "\u2013" not in text, "en dash found in test file"

    def _block(self, doc):
        m = re.search(
            r"## Iteration #601\b.*?(?=^## Iteration #|\Z)",
            doc,
            re.DOTALL | re.MULTILINE,
        )
        assert m, "Iteration #601 block not found in podcast-sentiment.md"
        return m.group(0)


class TestSources:
    def test_biometricupdate_url_verbatim(self):
        doc = read_doc()
        block = self._block(doc)
        assert BIOMETRICUPDATE_URL in block

    def test_listen_notes_url_present(self):
        doc = read_doc()
        block = self._block(doc)
        assert "listennotes.com/podcasts/the-guilty-feminist" in block

    def test_chortle_url_present(self):
        doc = read_doc()
        block = self._block(doc)
        assert "chortle.co.uk" in block

    def test_ehe_source_urls_verbatim(self):
        doc = read_doc()
        block = self._block(doc)
        for url in (
            "https://www.thetimes.com/uk/london/article/meta-ai-glasses-spoof-advert-jeffrey-epstein-slx3wttm5",
            "https://feminist.org/news/helpful-or-hurtful-the-growing-privacy-debate-over-meta-glasses/",
            "https://www.latestly.com/social-viral/fact-check/did-jeffrey-epstein-feature-on-meta-smart-glasses-billboard-ad-in-london-fact-check-finds-viral-claim-fake-7538349.html",
        ):
            assert url in block, f"EHE source URL missing: {url}"

    def _block(self, doc):
        m = re.search(
            r"## Iteration #601\b.*?(?=^## Iteration #|\Z)",
            doc,
            re.DOTALL | re.MULTILINE,
        )
        assert m, "Iteration #601 block not found in podcast-sentiment.md"
        return m.group(0)

class TestConfoundersAndLog:
    def test_strong_confounders_present(self):
        doc = read_doc()
        block = self._block(doc)
        assert re.search(r"STRONG:", block)

    def test_bounded_absence_confounders_ranked(self):
        doc = read_doc()
        block = self._block(doc)
        assert "all holds are bounded search-result absences" in block

    def test_hours_cadence_bounded(self):
        doc = read_doc()
        block = self._block(doc)
        assert re.search(r"time-bounded to 03:00 PDT", block)

    def test_log_entry_present_newest_first(self):
        log = read_log()
        assert log.startswith("#601 Type E:"), (
            "iteration-log.md must start with the #601 entry (newest-first)"
        )

    def test_log_entry_covers_rotation_edge(self):
        log = read_log()
        head = log[:3000]
        assert re.search(r"rotation 600 D -> 601 E", head)

    def test_600_entry_repositioned(self):
        log = read_log()
        pos600 = log.find("#600 Type D:")
        pos601 = log.find("#601 Type E:")
        assert pos600 != -1 and pos601 != -1
        assert pos601 < pos600, "#601 entry must precede #600 entry"
        assert pos600 < 12000, (
            f"#600 entry should sit near the top after the miss repair, "
            f"found at char {pos600}"
        )

    def _block(self, doc):
        m = re.search(
            r"## Iteration #601\b.*?(?=^## Iteration #|\Z)",
            doc,
            re.DOTALL | re.MULTILINE,
        )
        assert m, "Iteration #601 block not found in podcast-sentiment.md"
        return m.group(0)


class TestNoBrittleSweep601:
    def test_no_old_cycle_labels_claimed_current(self):
        doc = read_doc()
        block = self._block(doc)
        assert "forty-second" not in block.lower(), (
            "block must not reuse the #596 forty-second cycle label"
        )
        assert "29-day hold" not in block.lower(), (
            "block must not reuse the stale 29-day hold label"
        )

    def test_distinct_from_596(self):
        doc = read_doc()
        block = self._block(doc)
        assert "distinct from 596" in block or "extends #596" in block

    def test_no_zero_coverage_claims(self):
        doc = read_doc()
        block = self._block(doc)
        assert not re.search(r"\bzero coverage\b", block, re.IGNORECASE)

    def _block(self, doc):
        m = re.search(
            r"## Iteration #601\b.*?(?=^## Iteration #|\Z)",
            doc,
            re.DOTALL | re.MULTILINE,
        )
        assert m, "Iteration #601 block not found in podcast-sentiment.md"
        return m.group(0)


class TestRotationCycleGuard601:
    """Rotation guard, deselected pre-commit per the #565 followup convention.

    Asserts the post-commit anchor, so it runs green only in the followup
    commit after the main commit SHA is known. Pre-commit it is deselected.
    """

    def _mains(self):
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [s for s in out if re.match(r"^Type [A-E] #\d+:", s)]
        assert len(mains) >= 5
        return mains

    def test_window_597_601_closes_d_to_e(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("E", "601"),
            ("D", "600"),
            ("C", "599"),
            ("B", "598"),
            ("A", "597"),
        ], f"rotation window 597-601 wrong: {observed}"

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["E", "D", "C", "B", "A"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                f"rotation broken: {a} -> {b} is not a valid cycle edge"
            )


class TestDocSyncRatchet601:
    def test_readme_row_for_601(self):
        readme = read_readme()
        assert re.search(r"#601", readme), "README.md missing the #601 test-table row"

    def test_arch_row_for_601(self):
        arch = read_arch()
        assert re.search(r"#601", arch), "docs/ARCHITECTURE.md missing the #601 tree row"

    def test_596_row_survives_in_readme(self):
        readme = read_readme()
        assert re.search(r"#596", readme), "README.md lost the #596 row"

    def test_596_row_survives_in_arch(self):
        arch = read_arch()
        assert re.search(r"#596", arch), "docs/ARCHITECTURE.md lost the #596 row"
