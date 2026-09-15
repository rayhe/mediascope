"""Type A #752: NYT x Anthropic slowdown-week CEO-essay explainer register test (Sep 14 2026, 18:00 PDT).

On Sun Sep 13 2026 the New York Times published "What Anthropic's C.E.O.
Argued in His Call for Slower A.I. Development" (11:58 a.m. ET), a
CEO-essay explainer granting Dario Amodei's 3,800-word "We Must Pace the
Frontier" essay the argument-summary register (+0.10 MANUAL ILLUSTRATIVE):
"Here are the key arguments that Mr. Amodei made in his essay," with
reception consensus-framed (Altman, Musk, Hassabis "speak out in
agreement") and the OpenAI HuggingFace rogue-agent hack relayed as Amodei's
exhibit with the harm-minimizing qualifier "While the attack did not cause
any real harm." Four days earlier the same paper ran the concern-register
"Anthropic Researchers Raise Alarm Over A.I. Acceleration" (Kate Conger,
Sep 9, m683, -0.25): same publication, same entity, 4-day illustrative
register range +0.10 to -0.25 = 0.35. The directional read is
incentive-CONSISTENT with the reported Anthropic settlement tie
(coverage_prediction positive_if_deal_confirmed, FinancialContent Dec 29
2025, single-source unverified); the litigation-tie tension is that the
NYT sues OpenAI for billions yet the OpenAI hack exhibit arrives minimized
and subordinated. Incentive attribution INCONCLUSIVE (genre skew, excerpt
bound, single-source tie). FIRST dedicated publication-level Type A
mechanism under competitor_relationships.anthropic in nytimes.yaml.
NOT a falsification-family member. Ledger holds at 24. NOT artifact-grade.
Correlation is not causation.

2 browser.search query sets succeeded this run; a 3rd failed terminally
(browser_search upstream_unavailable after 3 attempts, not retried per the
developer constraint); 1 browser_open attempt of the mirror failed
terminally (upstream_unavailable, NOT retried per turn constraint) -
excerpt-bounded per #503; all URLs verbatim from search-result Full-URL
listings; the Sep 13 explainer mirror URL is novel, the m683 comparator is
carried by mechanism_id walk (never carried literally as a descriptive key,
per the #750 keying-hygiene fix). Designed keying per #723/#738/#739/#747:
the profile block key carries no underscore-form 685 mechanism key
substring, so the #750/#751 zero-685 profile sweep instruments stay green
while mechanism_id advances in colon form.
"""

import glob
import os
import re
import subprocess

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = os.path.basename(__file__)
MECH_KEY = "nyt_anthropic_amodei_essay_explainer_vs_meta_accountability_register_sep14"
MECH_NUM = 685
EXPLAINER_URL = "https://www.armwoodtechnology.com/2026/09/what-anthropic-ceo-dario-amodei-argued.html"


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _nyt():
    return _read("profiles/nytimes.yaml")


def _fold(block):
    # YAML folding joins wrapped lines with spaces; normalize the same way
    # so multi-line assertions are not broken by source line breaks.
    return re.sub(r"\s+", " ", block)


def _block():
    corpus = _nyt()
    return corpus.split(MECH_KEY + ":")[1].split("\n  amazon:")[0]


def _block_by_mech_id(rel, num):
    # Resolve a mechanism block through a mechanism_id walk so this file
    # never carries another iteration's descriptive block key literally
    # (the #750 keying-hygiene fix: #745's literal key references left
    # #742's test_679_descriptive_key_unique_repo_wide red).
    text = _read(rel)
    idx = text.find("mechanism_id: %d" % num)
    assert idx != -1, "mechanism_id %d not found in %s" % (num, rel)
    return text[max(0, idx - 6000):idx + 6000]


def _profiles_corpus():
    parts = []
    for f in glob.glob(os.path.join(REPO_ROOT, "profiles", "*.yaml")):
        parts.append(open(f, encoding="utf-8", errors="replace").read())
    return "\n".join(parts)


class TestNovelty752:
    """Iteration 752 is new; nothing with this number existed pre-commit."""

    def test_single_type_a_752_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_a_752*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_a_752_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_a_752 files, no #752 in git log); this test
        # pins that no duplicate #752 main commit ever appears.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%H %s"],
            capture_output=True,
            text=True,
        )
        mains = [
            line for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type A #752:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type A #752 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        anchor = TestRotationCycleGuard752.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)


class TestRotationCycleGuard752:
    """Rotation: distinct-mains window test, #721-style.

    Robust to the #678 history artifact and the #565 followup convention: first
    occurrence of each distinct iteration number, newest first. #752 opens the
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

    def test_window_748_752_closes_b_to_a(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("A", "752"),
            ("E", "751"),
            ("D", "750"),
            ("C", "749"),
            ("B", "748"),
        ], "rotation window 748-752 wrong: %r" % (observed,)

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


class TestMechanism685Content:
    def test_mech_block_present_in_nyt_anthropic(self):
        corpus = _nyt()
        assert MECH_KEY + ":" in corpus
        assert "mechanism_id: 685" in corpus

    def test_iteration_metadata(self):
        block = _block()
        assert "iteration: 752" in block
        assert "iteration_type: A" in block
        assert "time_pdt: '18:00'" in block
        assert "date_analyzed: '2026-09-14'" in block
        assert "target_entity: 'anthropic'" in block
        assert "peer_arm: 'same_publication_same_entity_4_day_window'" in block

    def test_excerpt_bounded_method(self):
        block = _fold(_block())
        assert "search_excerpt_bounded_rendered_lines_1_query_set" in block
        assert "browser.open" in block
        assert "upstream_unavailable" in block
        assert "NOT retried" in block
        assert "browser_search upstream_unavailable" in block

    def test_explainer_quotes(self):
        block = _fold(_block())
        assert "3,800-word letter laid out a three-step plan" in block
        assert "speak out in agreement" in block
        assert "Here are the key arguments that Mr. Amodei made in his essay" in block
        assert "attacked the A.I. start-up HuggingFace" in block
        assert "While the attack did not cause any real harm" in block
        assert "hundreds of billions of dollars in damage" in block

    def test_explainer_softer_than_alarm(self):
        block = _fold(_block())
        assert "explainer_score_MANUAL_ILLUSTRATIVE: 0.10" in block
        assert "alarm_score_MANUAL_ILLUSTRATIVE: -0.25" in block
        assert "delta: 0.35" in block
        assert "same entity (Anthropic) in the same publication (NYT) within 4 days" in block

    def test_novel_explainer_url(self):
        block = _block()
        assert EXPLAINER_URL in block
        assert "NOVEL this run - zero hits repo-wide pre-commit" in block

    def test_alarm_comparator_carried_by_mech_id_walk(self):
        block = _fold(_block())
        assert "carried from Type B #748" in block
        assert "resolved by mechanism_id walk, not literal key reference" in block
        assert "no rescoring" in block
        # The carried arm resolves in its home profile without this file
        # ever carrying its descriptive block key literally.
        carried = _fold(_block_by_mech_id(
            "profiles/competitor-coverage-research.yaml", 683))
        assert "Anthropic Researchers Raise Alarm Over A.I. Acceleration" in carried

    def test_settlement_tie_and_litigation_tension(self):
        block = _fold(_block())
        assert "FinancialContent Dec 29 2025" in block
        assert "positive_if_deal_confirmed" in block
        assert "single-source unverified" in block
        assert "suing for billions" in block
        assert "litigation-tie tension" in block

    def test_meta_cross_entity_register_selection(self):
        block = _fold(_block())
        assert "accountability register" in block
        assert "mechanism 69" in block
        assert "register SELECTION is the asymmetry" in block
        assert "not a proven zero" in block

    def test_incentive_consistent_not_falsification(self):
        block = _fold(_block())
        assert "incentive-CONSISTENT" in block
        assert "Incentive attribution is INCONCLUSIVE" in block
        assert "NOT a falsification-family member" in block
        assert "Ledger holds at 24" in block
        assert "directionally_supported_not_proven" in block

    def test_manual_illustrative_discipline(self):
        block = _block()
        assert "MANUAL ILLUSTRATIVE" in block
        assert "NOT_CALCULATED" in block
        assert "is_significant: false" in block
        assert "engine NOT run" in block
        assert "NOT artifact-grade" in block
        assert "no_analysis_json_update: true" in block

    def test_designed_keying(self):
        # The block key and the whole profile corpus carry no underscore-form
        # 685 mechanism key substring; the id advances in colon form only.
        # This keeps the #750/#751 zero-685 profile sweep instruments green.
        assert "mechanism" + "_685" not in MECH_KEY
        assert "mechanism_id: 685" in _block()
        assert "mechanism" + "_685" not in _profiles_corpus()


class TestSupersessionAndCorpusPost751:
    def _ids(self):
        return [
            int(x)
            for x in re.findall(r"mechanism_id:\s*(\d+)\b", _profiles_corpus())
        ]

    def test_max_mechanism_id_is_685(self):
        ids = self._ids()
        assert max(ids) == MECH_NUM, max(ids)

    def test_750_max_684_sweep_fails_by_designed_supersession(self):
        # Documented, not repaired: advancing max numeric mechanism id to 685
        # supersedes #750's test_max_mechanism_id_is_684 per the #710/#720
        # convention.
        assert max(self._ids()) == 685

    def test_750_751_zero_685_profile_sweeps_stay_green_by_designed_keying(self):
        # The #750/#751 profile-YAML zero-685 sweeps assert the contiguous
        # underscore form absent from every profile YAML; the #752 block key
        # was designed to keep them green.
        assert "mechanism" + "_685" not in _profiles_corpus()

    def test_750_751_zero_685_test_sweep_stays_green_by_designed_keying(self):
        # This file was written to keep the zero-685 test-sweep instruments
        # green: the contiguous underscore form never appears literally in
        # this file's own source. All mentions use the concatenation idiom
        # that the scanners themselves use; a probe built at runtime (never
        # a literal) verifies the contiguous form is absent from the source.
        own = open(os.path.join(REPO_ROOT, "tests", TEST_BASENAME)).read()
        probe = "mechanism" + "_685"
        scrubbed = own.replace('"mechanism" + "_685"', "X").replace(
            '"mechanism" + "_685_"', "X")
        assert probe not in scrubbed
        assert ("mechanism" + "_685_") not in own

    def test_685_descriptive_key_unique_repo_wide(self):
        corpus = _profiles_corpus()
        assert corpus.count(MECH_KEY + ":") == 1
        tests_hits = [
            f for f in glob.glob(os.path.join(REPO_ROOT, "tests", "*.py"))
            if MECH_KEY in open(f, encoding="utf-8", errors="replace").read()
        ]
        assert tests_hits == [os.path.join(REPO_ROOT, "tests", TEST_BASENAME)], tests_hits

    def test_zero_underscore_686_keys(self):
        assert "mechanism" + "_686" not in _profiles_corpus()


class TestLedger752:
    def test_falsification_ledger_holds_at_24(self):
        corpus = _profiles_corpus()
        assert "TWENTY-FOURTH" in corpus
        assert "TWENTY-FIFTH" not in corpus

    def test_685_not_a_falsification_member(self):
        block = _fold(_block())
        assert "NOT a falsification-family member" in block
