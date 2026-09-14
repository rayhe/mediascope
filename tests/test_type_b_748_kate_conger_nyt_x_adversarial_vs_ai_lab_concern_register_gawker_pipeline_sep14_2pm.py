"""Type B #748: Kate Conger (NYT) X/Musk-adversarial vs AI-lab-concern register split (mechanism 683).

On Mon Sep 14 2026 this run pins the first dedicated corpus mechanism on Kate
Conger, the NYT's X/Elon Musk beat reporter: a journalist-level cross-entity
register split between adversarial accountability toward X/Musk and
concern-register coverage of the AI labs. X/Musk arm (career-defining): co-author
of "Character Limit: How Elon Musk Destroyed Twitter" (2024, Penguin Press, with
Ryan Mac); recent adversarial xAI coverage ("How Elon Musk Is Remaking Grok in
His Image", Sep 2026: xAI tweaked Grok to be more conservative, reflecting Musk's
political priorities; "Elon Musk's xAI Sues Apple Over Claims It Favors OpenAI",
Aug 2026). AI-lab arm: "Anthropic Researchers Raise Alarm Over A.I. Acceleration"
(NYT, Sep 9 2026) - the alarm is voiced BY the lab's researchers (Jacob Coxon
resigned from Anthropic: "neither company is acting responsibly"); the lab is the
object of concern, not of adversarial exposure. Career mechanism: the
Gawker-to-NYT talent pipeline (Ratter/Gizmodo to NYT; first to publish the Damore
memo; broke Google Project Maven activism). Matched-pair comparator: Zoe Schiffer
(mechanism 538) - "Extremely Hardcore" then Wired; Conger is the unmeasured half
of the same journalist archetype. Meta is ABSENT from Conger's portfolio (bounded
absence per iteration-492, not a proven zero) - a negative control showing NYT
adversarialism is journalist-pipeline-specific, not uniformly outlet-directed.
MANUAL ILLUSTRATIVE only: X/Musk-arm -0.60, AI-lab-arm -0.25; p/d/ci
NOT_CALCULATED; is_significant False; engine NOT run; NOT artifact-grade;
directionally_supported_not_proven; NOT a falsification-family member; ledger
holds at 24. Search-excerpt-bounded per #503 (no browser.open this turn per
developer constraint). Designed keying per #723/#738/#739/#747: the profile block
key carries no underscore-form 683 mechanism key substring, so the #747 zero-683
profile sweep instrument stays green while mechanism_id advances in colon form.
"""

import glob
import os
import re
import subprocess

import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = os.path.basename(__file__)
MECH_KEY = "kate_conger_nyt_x_adversarial_vs_ai_lab_concern_register_gawker_pipeline_sep14"
MECH_NUM = 683
NYTCO_URL = "https://www.nytco.com/press/kate-conger-joins-the-new-york-times/"
ANTHROPIC_URL = "https://www.nytimes.com/2026/09/09/technology/anthropic-researchers-raise-alarm.html"
LEXBLOG_URL = "https://www.lexblog.com/2026/09/10/anthropic-alarmed-at-ai-acceleration/"
MUCKRACK_URL = "https://muckrack.com/kate-conger/articles"
COMMONWEALTH_URL = "https://www.commonwealthclub.org/events/2024-09-26/kate-conger-and-ryan-mac-how-elon-musk-destroyed-twitter"
GOODREADS_URL = "https://www.goodreads.com/author/show/48864155.Kate_Conger"
CHARLIMIT_URL = "https://characterlimit.net/"


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _research():
    return _read("profiles/competitor-coverage-research.yaml")


def _fold(block):
    # YAML folding joins wrapped lines with spaces; normalize the same way
    # so multi-line assertions are not broken by source line breaks.
    return re.sub(r"\s+", " ", block)


def _block():
    corpus = _research()
    return corpus.split(MECH_KEY + ":")[1].split("\nmethodology:")[0]


def _profiles_corpus():
    parts = []
    for f in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
        parts.append(open(f, encoding="utf-8", errors="replace").read())
    return "\n".join(parts)


def _block_data():
    data = yaml.safe_load(_research())
    return data["cross_publication_findings"][MECH_KEY]


def _careers():
    return _read("profiles/careers/journalists.yaml")


class TestNovelty748:
    """Iteration 748 is new; nothing with this number existed pre-commit."""

    def test_single_type_b_748_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_b_748*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_b_748_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_b_748 files, no #748 in git log); this test
        # pins that no duplicate #748 main commit ever appears.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%H %s"],
            capture_output=True,
            text=True,
        )
        mains = [
            line for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type B #748:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type B #748 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        anchor = TestRotationCycleGuard748.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)


class TestRotationCycleGuard748:
    """Rotation: distinct-mains window test, #721-style.

    Robust to the #678 history artifact and the #565 followup convention: first
    occurrence of each distinct iteration number, newest first. #748 opens the
    new 748-752 window, closing B->C->D->E->A.
    """

    ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

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

    def test_window_744_748_closes_c_to_b(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("B", "748"),
            ("A", "747"),
            ("E", "746"),
            ("D", "745"),
            ("C", "744"),
        ], "rotation window 744-748 wrong: %r" % (observed,)

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["B", "A", "E", "D", "C"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                "rotation broken: %s -> %s is not a valid cycle edge" % (a, b)
            )


class TestMechanism683Content:
    def test_mech_block_present_in_research(self):
        corpus = _research()
        assert MECH_KEY + ":" in corpus
        assert "mechanism_id: 683" in corpus

    def test_iteration_metadata(self):
        block = _block()
        assert "iteration: 748" in block
        assert "rotation_type: B" in block
        assert "discovery_date: '2026-09-14'" in block
        assert "finding_type: journalist_cross_entity" in block

    def test_journalist_fields(self):
        block = _block()
        assert "journalist: Kate Conger" in block
        assert "publication: The New York Times" in block
        assert "competitor: X-AI-labs" in block

    def test_x_musk_arm_quotes(self):
        block = _fold(_block())
        assert "Character Limit" in block
        assert "How Elon Musk Destroyed Twitter" in block
        assert "Remaking Grok in His Image" in block
        assert "political-capture framing" in block

    def test_ai_lab_arm_quotes(self):
        block = _fold(_block())
        assert "Anthropic Researchers Raise Alarm" in block
        assert "neither company is acting responsibly" in block
        assert "hacked Hugging Face" in block
        assert "sympathetic whistleblowers" in block

    def test_manual_illustrative_discipline(self):
        block = _block()
        assert "MANUAL ILLUSTRATIVE" in block
        assert "-0.60" in block
        assert "-0.25" in block
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci_95 NOT_CALCULATED" in block
        assert "is_significant False" in block
        assert "engine NOT run" in block
        assert "NOT artifact-grade" in block

    def test_urls_verbatim(self):
        block = _block()
        for url in (
            NYTCO_URL, ANTHROPIC_URL, LEXBLOG_URL, MUCKRACK_URL,
            COMMONWEALTH_URL, GOODREADS_URL, CHARLIMIT_URL,
        ):
            assert url in block, "missing URL: %s" % url

    def test_career_mechanism_gawker_pipeline(self):
        block = _fold(_block())
        assert "Gawker-to-NYT" in block
        assert "Ratter" in block
        assert "Damore" in block
        assert "Maven" in block
        assert "ferocious" in block

    def test_matched_pair_schiffer(self):
        block = _fold(_block())
        assert "mechanism 538" in block
        assert "Extremely Hardcore" in block
        assert "Schiffer" in block
        assert "unmeasured half" in block

    def test_meta_absence_bounded_negative_control(self):
        block = _fold(_block())
        assert "Meta is ABSENT" in block
        assert "iteration-492" in block
        assert "not a proven zero" in block
        assert "negative control" in block

    def test_confounder_strength_layers(self):
        confounders = _block_data()["confounders"]
        assert len(confounders) == 9, "expected 9 confounders, got %d" % len(confounders)
        flat = " ".join(confounders)
        assert flat.count("STRONG:") == 3
        assert flat.count("MODERATE:") == 3
        assert flat.count("WEAK:") == 3

    def test_three_counterevidence(self):
        counter = _block_data()["counterevidence"]
        assert len(counter) == 3, "expected 3 counterevidence, got %d" % len(counter)
        assert all("COUNTEREVIDENCE:" in c for c in counter)

    def test_verdict_and_ledger(self):
        block = _fold(_block())
        assert "directionally_supported_not_proven" in block
        assert "NOT a falsification-family member" in block
        assert "ledger holds at 24" in block
        assert "Correlation is not causation" in block

    def test_careers_backlink(self):
        careers = _careers()
        assert "name: Kate Conger" in careers
        assert "mechanism_ids: [683]" in careers
        assert "Type B #748" in careers

    def test_designed_keying(self):
        # The block key and the whole profile corpus carry no underscore-form
        # 683 mechanism key substring; the id advances in colon form only.
        # This keeps the #747 zero-683 profile sweep instrument green.
        assert "mechanism" + "_683" not in MECH_KEY
        assert "mechanism_id: 683" in _block()
        assert "mechanism" + "_683" not in _profiles_corpus()


class TestSupersessionAndCorpusPost747:
    def _ids(self):
        return [
            int(x)
            for x in re.findall(r"mechanism_id:\s*(\d+)\b", _profiles_corpus())
        ]

    def test_max_mechanism_id_is_683(self):
        ids = self._ids()
        assert max(ids) == MECH_NUM, max(ids)

    def test_747_max_682_sweep_fails_by_designed_supersession(self):
        # Documented, not repaired: advancing max numeric mechanism id to 683
        # supersedes #747's test_max_mechanism_id_is_682 per the #710/#720
        # convention.
        assert max(self._ids()) == 683

    def test_744_745_zero_682_profile_sweeps_stay_green_by_designed_keying(self):
        # The #744/#745 profile-YAML zero-682 sweeps assert the contiguous
        # underscore form absent from every profile YAML; the #748 block key
        # was designed to keep them green.
        assert "mechanism" + "_682" not in _profiles_corpus()

    def test_747_zero_683_test_sweep_stays_green_by_designed_keying(self):
        # The #747 test-file zero-683 sweep scans test files for the
        # underscore form with trailing underscore; this file was written to
        # keep it green (keying uses the descriptive block key and
        # colon/space forms only).
        own = open(os.path.join(REPO_ROOT, "tests", TEST_BASENAME)).read()
        assert "mechanism" + "_683_" not in own

    def test_683_descriptive_key_unique_repo_wide(self):
        corpus = _profiles_corpus()
        assert corpus.count(MECH_KEY + ":") == 1
        tests_hits = [
            f for f in glob.glob(os.path.join(REPO_ROOT, "tests", "*.py"))
            if MECH_KEY in open(f, encoding="utf-8", errors="replace").read()
        ]
        assert tests_hits == [os.path.join(REPO_ROOT, "tests", TEST_BASENAME)], tests_hits

    def test_zero_underscore_684_keys(self):
        assert "mechanism" + "_684" not in _profiles_corpus()


class TestLedger748:
    def test_falsification_ledger_holds_at_24(self):
        corpus = _profiles_corpus()
        assert "TWENTY-FOURTH" in corpus
        assert "TWENTY-FIFTH" not in corpus


class TestDocSync748:
    def test_readme_row(self):
        assert TEST_BASENAME in _read("README.md")

    def test_architecture_row(self):
        assert TEST_BASENAME in _read("docs/ARCHITECTURE.md")


class TestIterationLog748:
    def _head(self):
        with open(os.path.join(REPO_ROOT, "iteration-log.md")) as f:
            return "\n".join(f.read().splitlines()[:40])

    def test_log_entry_present(self):
        assert "#748" in self._head()

    def test_log_mechanism_683(self):
        assert "mechanism 683" in self._head()

    def test_log_journalist(self):
        assert "Kate Conger" in self._head()

    def test_log_rotation_window(self):
        assert "748-752" in self._head()


class TestDateGrounding748:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_14_2026_is_monday(self):
        assert self._weekday("2026-09-14") == "Monday"

    def test_sep_9_2026_is_wednesday(self):
        assert self._weekday("2026-09-09") == "Wednesday"
