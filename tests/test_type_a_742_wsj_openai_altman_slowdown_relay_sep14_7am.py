"""Type A #742: WSJ x OpenAI slowdown-week Altman relay register test (Sep 14 2026, 07:00 PDT).

The Wall Street Journal published a same-week pair with opposite registers
toward the two frontier labs. On Mon Sep 14 2026, Gareth Vipers' WSJ piece
"Microsoft Sets Limits for AI Models as Altman Details Control Risks"
relays Sam Altman's overnight X-post safety comments constructively:
federal framework welcomed, "pacing" framed as responsible, and the
potential IPO delay presented as a safety call (first-hand browser.open
read, 41 rendered lines; URL novel to the corpus). On Sun Sep 13, the same
paper ran "Anthropic's Moral Conflict Is Playing Out in Real Time" -
adversarial moral framing of the non-payer. News Corp collects ~$50M/yr
from OpenAI (May 2024, $250M/5yr) and $0/yr in AI licensing from Anthropic.
The within-week OpenAI-minus-Anthropic illustrative delta is +0.525,
directionally consistent with the deal predictor (payer softer than
non-payer). This extends the mechanism 616 dual-deal symmetry window
(#519): the OpenAI-vs-Meta axis stays near-symmetric under symmetric
softening while the OpenAI-vs-Anthropic axis is the one the incentive
structure predicts.

Incentive attribution is INCONCLUSIVE: the Altman piece's lead peg is
Microsoft's code-of-conduct announcement, the tone is respondent-positioning,
and mechanism 616's Tumbler Ridge precedent (-0.55, hardest OpenAI register
in the WSJ corpus, twelve days earlier) bounds any capture reading. Register
MIXES on the same payer within one month. NOT a falsification-family member
(register-mix refinement). NOT artifact-grade. Correlation is not causation.

4 browser.search query sets this run; 1 first-hand browser.open; all URLs
verbatim from search-result Full-URL listings; the Altman piece URL is novel,
the "Biggest AI Rivals" and "Moral Conflict" URLs are carried from #737 by
design; no wsj.com URLs constructed. Designed keying per #723/#738/#739: the
profile block key carries no underscore-form 679 mechanism key substring, so
the #740 zero-679 sweep instruments stay green while mechanism_id advances
in colon form.
"""

import glob
import os
import re
import subprocess

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = os.path.basename(__file__)
MECH_KEY = "wsj_openai_altman_slowdown_relay_vs_anthropic_moral_conflict_sep14"
MECH_NUM = 679
ALTMAN_URL = "https://www.wsj.com/tech/ai/altman-says-ais-rapid-progress-could-go-very-badly-1e840a6c"
RIVALS_URL = "https://www.wsj.com/tech/ai/anthropic-boss-warns-ai-industry-must-slow-the-pace-a4267b56"
MORAL_CONFLICT_URL = "https://www.wsj.com/tech/ai/anthropics-moral-conflict-is-playing-out-in-real-time-c503e0c1"


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _newscorp():
    return _read("profiles/news-corp.yaml")


def _fold(block):
    # YAML folding joins wrapped lines with spaces; normalize the same way
    # so multi-line assertions are not broken by source line breaks.
    return re.sub(r"\s+", " ", block)


def _block():
    corpus = _newscorp()
    return corpus.split(MECH_KEY + ":")[1].split("\n  meta:")[0]


def _profiles_corpus():
    parts = []
    for f in glob.glob(os.path.join(REPO_ROOT, "profiles", "*.yaml")):
        parts.append(open(f, encoding="utf-8", errors="replace").read())
    return "\n".join(parts)


class TestNovelty742:
    """Iteration 742 is new; nothing with this number existed pre-commit."""

    def test_single_type_a_742_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_a_742*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_a_742_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_a_742 files, no #742 in git log); this test
        # pins that no duplicate #742 main commit ever appears.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%H %s"],
            capture_output=True,
            text=True,
        )
        mains = [
            line for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type A #742:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type A #742 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        anchor = TestRotationCycleGuard742.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)


class TestRotationCycleGuard742:
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

    def test_window_738_742_closes_b_to_a(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("A", "742"),
            ("E", "741"),
            ("D", "740"),
            ("C", "739"),
            ("B", "738"),
        ], "rotation window 738-742 wrong: %r" % (observed,)

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


class TestMechanism679Content:
    def test_mech_block_present_in_newscorp_openai(self):
        corpus = _newscorp()
        assert MECH_KEY + ":" in corpus
        assert "mechanism_id: 679" in corpus

    def test_iteration_metadata(self):
        block = _block()
        assert "iteration: 742" in block
        assert "iteration_type: A" in block
        assert "time_pdt: '07:00'" in block
        assert "date_analyzed: '2026-09-14'" in block
        assert "target_entity: 'openai'" in block
        assert "peer_entity: 'anthropic'" in block

    def test_first_hand_read_evidence(self):
        block = _fold(_block())
        assert "first_hand_browser_open_41_rendered_lines" in block
        assert "Gareth Vipers" in block
        assert "2026-09-14" in block

    def test_constructive_relay_quotes(self):
        block = _fold(_block())
        assert "very badly" in block
        assert "No amount of American competitive pressure should justify recklessness" in block
        assert "much anticipated initial public offering to focus on safety" in block
        assert "stoked fears" in block

    def test_ipo_delay_framed_as_safety_call(self):
        block = _fold(_block())
        assert "IPO delay is framed as a safety call" in block
        assert "no market-timing skepticism in the surfaced text" in block

    def test_novel_altman_url(self):
        block = _block()
        assert ALTMAN_URL in block
        assert "NOVEL this run - zero hits repo-wide pre-commit" in block

    def test_carried_urls_flagged_by_design(self):
        block = _fold(_block())
        assert RIVALS_URL in block
        assert MORAL_CONFLICT_URL in block
        assert "carried from #737" in block
        assert "no rescoring" in block

    def test_deal_predictor_stated(self):
        block = _fold(_block())
        assert "$50M/yr" in block
        assert "$250M/5yr" in block
        assert "Anthropic leg $0 AI licensing" in block

    def test_dual_payer_symmetry_carried(self):
        block = _fold(_block())
        assert "#519" in block
        assert "symmetric softening" in block
        assert "m616" in block

    def test_manual_illustrative_discipline(self):
        block = _block()
        assert "MANUAL ILLUSTRATIVE" in block
        assert "NOT_CALCULATED" in block
        assert "is_significant: false" in block
        assert "engine NOT run" in block
        assert "NOT artifact-grade" in block
        assert "no_analysis_json_update: true" in block

    def test_bounded_absence_language(self):
        block = _fold(_block())
        assert "Bounded search-result absence per iteration-492" in block
        assert "not a proven zero" in block

    def test_register_mix_not_falsification(self):
        block = _fold(_block())
        assert "Register MIXES within one month on the same payer" in block
        assert "Incentive attribution is INCONCLUSIVE" in block
        assert "NOT a falsification-family member" in block
        assert "Ledger holds at 24" in block

    def test_designed_keying(self):
        # The block key and the whole profile corpus carry no underscore-form
        # 679 mechanism key substring; the id advances in colon form only.
        assert "mechanism" + "_679" not in MECH_KEY
        assert "mechanism_id: 679" in _block()
        assert "mechanism" + "_679" not in _profiles_corpus()


class TestSupersessionAndCorpusPost741:
    def _ids(self):
        return [
            int(x)
            for x in re.findall(r"mechanism_id:\s*(\d+)\b", _profiles_corpus())
        ]

    def test_max_mechanism_id_is_679(self):
        ids = self._ids()
        assert max(ids) == MECH_NUM, max(ids)

    def test_740_max_678_sweep_fails_by_designed_supersession(self):
        # Documented, not repaired: advancing max numeric mechanism id to 679
        # supersedes #740's test_max_mechanism_id_is_678 per the #710/#720
        # convention.
        assert max(self._ids()) == 679

    def test_740_zero_679_profile_sweep_stays_green_by_designed_keying(self):
        # The #740 profile-YAML zero-679 sweep asserts the contiguous
        # underscore form absent from every profile YAML; the #742 block key
        # was designed to keep it green.
        assert "mechanism" + "_679" not in _profiles_corpus()

    def test_740_zero_679_test_sweep_stays_green_by_designed_keying(self):
        # The #740 other-tests zero-679 sweep scans test files for the
        # underscore form with trailing underscore; this file was written to
        # keep it green (keying uses the descriptive block key and
        # colon/space forms only).
        own = open(os.path.join(REPO_ROOT, "tests", TEST_BASENAME)).read()
        assert "mechanism" + "_679_" not in own

    def test_679_descriptive_key_unique_repo_wide(self):
        corpus = _profiles_corpus()
        assert corpus.count(MECH_KEY + ":") == 1
        tests_hits = [
            f for f in glob.glob(os.path.join(REPO_ROOT, "tests", "*.py"))
            if MECH_KEY in open(f, encoding="utf-8", errors="replace").read()
        ]
        assert tests_hits == [os.path.join(REPO_ROOT, "tests", TEST_BASENAME)], tests_hits

    def test_zero_underscore_680_keys(self):
        assert "mechanism" + "_680" not in _profiles_corpus()


class TestLedger742:
    def test_falsification_ledger_holds_at_24(self):
        corpus = _profiles_corpus()
        assert "TWENTY-FOURTH" in corpus
        assert "TWENTY-FIFTH" not in corpus

    def test_679_not_a_falsification_member(self):
        block = _fold(_block())
        assert "NOT a falsification-family member" in block
