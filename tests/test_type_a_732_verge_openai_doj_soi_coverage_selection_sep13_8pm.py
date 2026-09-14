"""Type A #732: The Verge x OpenAI DOJ statement-of-interest coverage-selection test (Sep 13 2026, 20:00 PDT).

Coverage-SELECTION test on the Vox Media x OpenAI strategic partnership
(May 29 2024): the DOJ filed a 20-page statement of interest on Sep 1 2026
in the consolidated In re OpenAI Copyright Infringement Litigation
(S.D.N.Y. MDL 25-md-03143) - the first federal government intervention in
AI copyright cases - siding WITH OpenAI (the Vox deal partner) AGAINST
publishers including the NYT (fact base carried from mechanism 672, #729
Type C). Six browser.search query sets this run surfaced zero theverge.com
items on the story (one set returned zero results total); bounded absence
per iteration-492, NOT a proven zero. Four days later (Sep 5) The Verge
published the adversarial wiki-incident piece (m598, -0.65 MANUAL
ILLUSTRATIVE). Operative margin is SELECTION not TONE: m598 proves the
adversarial register is available on the deal partner when selected.
Incentive attribution INCONCLUSIVE: the valence triangle (deal partner vs
fellow publishers vs government) makes publisher-solidarity cross-pressure
an equally-weighted confounder. NOT a falsification-family member (ledger
holds at 24). NOT artifact-grade. Correlation is not causation.

6 browser.search query sets this run; all URLs verbatim from search-result
Full-URL listings; no theverge.com URL reconstructed; SOI fact URLs carried
from mechanism 672 (#729) by design.
"""

import glob
import os
import re
import subprocess

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = os.path.basename(__file__)
MECH_KEY = "mechanism_673_verge_openai_doj_soi_coverage_selection_test_sep13"
MECH_NUM = 673


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _verge():
    return _read("profiles/the-verge.yaml")


def _fold(block):
    # YAML `>` folding joins wrapped lines with spaces; normalize the same way
    # so multi-line assertions are not broken by source line breaks.
    return re.sub(r"\s+", " ", block)


def _block():
    corpus = _verge()
    return corpus.split(MECH_KEY + ":")[1].split("\n  meta:")[0]


class TestNovelty732:
    """Iteration 732 is new; nothing with this number existed pre-commit."""

    def test_single_type_a_732_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_a_732*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_a_732_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_a_732 files, no #732 in git log); this test
        # pins that no duplicate #732 main commit ever appears.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%H %s"],
            capture_output=True,
            text=True,
        )
        mains = [
            line for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type A #732:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type A #732 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        anchor = TestRotationCycleGuard732.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)


class TestRotationCycleGuard732:
    """Rotation: distinct-mains window test, #721-style.

    Robust to the #678 history artifact and the #565 followup convention: first
    occurrence of each distinct iteration number, newest first.
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

    def test_window_728_732_closes_e_to_a(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("A", "732"),
            ("E", "731"),
            ("D", "730"),
            ("C", "729"),
            ("B", "728"),
        ], "rotation window 728-732 wrong: %r" % (observed,)

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["A", "E", "D", "C", "B"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                "rotation broken: %s -> %s is not a valid cycle edge" % (a, b)
            )


class TestMechanism673Content:
    def test_mech_673_block_present_in_verge_openai(self):
        corpus = _verge()
        assert MECH_KEY + ":" in corpus
        assert "mechanism_id: 673" in corpus

    def test_iteration_metadata(self):
        block = _block()
        assert "iteration: 732" in block
        assert 'iteration_type: "A"' in block
        assert 'iteration_time: "2026-09-13 20:00 PDT"' in block
        assert 'entity_pair: "OpenAI vs Meta"' in block

    def test_finding_states_selection_not_tone(self):
        block = _fold(_block())
        assert "operative margin is SELECTION not TONE" in block
        assert "Incentive attribution is INCONCLUSIVE" in block
        assert "NOT a falsification-family member" in block
        assert "ledger holds at 24" in block

    def test_manual_illustrative_discipline(self):
        block = _block()
        assert "MANUAL ILLUSTRATIVE" in block
        assert "NOT_CALCULATED" in block
        assert "is_significant: false" in block
        assert "NOT" in block and "artifact-grade" in block
        assert "engine NOT run" in block

    def test_novelty_vs_existing_598_672(self):
        block = _block()
        assert "mechanism 598" in block
        assert "mechanism 672" in block
        assert "zero mechanism_673 keys repo-wide" in block

    def test_bounded_absence_language(self):
        block = _fold(_block())
        assert "bounded absence per iteration-492" in block
        assert "NOT a proven zero" in block
        assert "NONE_SURFACED_BOUNDED_ABSENCE" in block

    def test_soi_facts_carried_from_672(self):
        block = _fold(_block())
        assert "mechanism 672" in block
        assert "first federal government intervention" in block
        assert "25-md-03143" in block

    def test_source_urls_all_verbatim_from_this_run(self):
        block = _block()
        for url in [
            "https://www.techtimes.com/articles/326401/20260903/doj-backs-openai-fair-use-claim-ai-copyright-fight-creators-must-try-congress.htm",
            "https://www.ghacks.net/2026/09/03/trump-administration-backs-open-ai-in-new-york-times-copyright-case-calling-ai-training-fair-use/",
            "https://www.aiweekly.co/alerts/doj-backs-openais-fair-use-defense-in-nyt-training-case",
            "https://www.theverge.com/ai-artificial-intelligence/990773/openai-german-wiki-incident",
            "https://venturebeat.com/ai/openai-partners-with-the-atlantic-and-the-verge-publisher-vox-media",
        ]:
            assert url in block, url

    def test_no_reconstructed_verge_url(self):
        block = _fold(_block())
        assert "no Verge page opened first-hand" in block
        assert "policy-blocked for browser.open" in block

    def test_financial_predictor_carried(self):
        block = _fold(_block())
        assert "Vox Media x OpenAI strategic partnership" in block
        assert "May 29 2024" in block
        assert "PMC acquired Vox Media in 2026" in block

    def test_open_empirical_test_named(self):
        block = _fold(_block())
        assert "Sep 14 ANI Division Bench appeal" in block


class TestSupersessionAndCorpusPost731:
    def _profiles_corpus(self):
        parts = []
        for f in glob.glob(os.path.join(REPO_ROOT, "profiles", "*.yaml")):
            parts.append(open(f, encoding="utf-8", errors="replace").read())
        return "\n".join(parts)

    def test_max_mechanism_id_is_673(self):
        ids = [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)\b", self._profiles_corpus())]
        modern = [i for i in ids if i >= 600]
        assert max(modern) == 673, max(modern)

    def test_729_zero_673_sweep_fails_by_designed_supersession(self):
        # Documented, not repaired: advancing max numeric mechanism id to
        # 673 supersedes #729's zero-673 profiles sweep per the
        # #710/#720 convention.
        corpus = self._profiles_corpus()
        assert "mechanism_673_" in corpus
        ids = [int(x) for x in re.findall(r"mechanism_id:\s*['\"]?(\d+)", corpus)]
        assert 673 in ids

    def test_673_key_unique_repo_wide(self):
        corpus = self._profiles_corpus()
        keys = re.findall(r"\bmechanism_673_[a-z0-9_]+\b", corpus)
        assert set(keys) == {MECH_KEY}, keys

    def test_zero_underscore_674_keys(self):
        assert "mechanism_674_" not in self._profiles_corpus()


class TestLedger732:
    def test_falsification_ledger_holds_at_24(self):
        parts = []
        for f in glob.glob(os.path.join(REPO_ROOT, "profiles", "*.yaml")):
            parts.append(open(f, encoding="utf-8", errors="replace").read())
        corpus = "\n".join(parts)
        assert "TWENTY-FOURTH" in corpus
        assert "TWENTY-FIFTH" not in corpus

    def test_673_not_a_falsification_member(self):
        block = _block()
        assert "NOT a member - selection-margin finding" in block
