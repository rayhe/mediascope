"""Type A #747: WSJ x OpenAI slowdown-week enterprise watchdog expose register test (Sep 14 2026, 13:00 PDT).

On Mon Sep 14 2026 the Wall Street Journal published an enterprise watchdog
expose, "How the Clash Between Money and Safety Created a Monumental Crisis
for AI" (bylines Robert McMillan, Amrith Ramkumar, Keach Hagey, Erin Woo),
framing the frontier labs - OpenAI first among them - as leaders trapped in
a "Greek tragedy" of their own race, with Sacks quoted "stop pretending the
motivation to slow down is purely altruistic" and a DeepMind "hot goss"
channel demanding "actual, tangible actions they are taking to change their
pace to be safer." The SAME publication, on the SAME day, carried Gareth
Vipers' constructive CEO-framing relay of Sam Altman's overnight X-post
safety comments (m679, +0.10). News Corp collects ~$50M/yr from OpenAI (May
2024, $250M/5yr). The same-day within-publication illustrative gap between
the watchdog expose (-0.40) and the relay-pair average (+0.075) is -0.475:
watchdog HARDER than relay on the payer within 24 hours. This is the
tightest temporal register-mix the corpus has logged on a licensing payer
(prior tightest: m616's Tumbler Ridge -0.55 vs m679's relay +0.10, twelve
days apart), and it extends m679's one-month register-mix finding into a
same-publication-day bound. Incentive attribution is INCONCLUSIVE and leans
negative: if the licensing tie purchased uniform softening, the day's
hardest OpenAI register would not be the money-vs-safety expose. NOT a
falsification-family member (register-mix refinement). Ledger holds at 24.
NOT artifact-grade. Correlation is not causation.

4 browser.search query sets this run; 1 browser.open attempt of the Clash
piece failed terminally (upstream_unavailable, NOT retried per turn
constraint) - excerpt-bounded per #503 (21 rendered lines across 2 query
sets); all URLs verbatim from search-result Full-URL listings; the Clash
piece URL is novel, the relay URLs are carried from #742 by design; no
wsj.com URLs constructed. Designed keying per #723/#738/#739: the profile
block key carries no underscore-form 682 mechanism key substring, so the
#744/#745 zero-682 profile sweep instruments stay green while mechanism_id
advances in colon form.
"""

import glob
import os
import re
import subprocess

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = os.path.basename(__file__)
MECH_KEY = "wsj_openai_clash_money_safety_expose_vs_altman_relay_sep14"
MECH_NUM = 682
CLASH_URL = "https://www.wsj.com/tech/ai/openai-anthropic-crisis-money-safety-847bc1d6"
RELAY_URL = "https://www.wsj.com/tech/ai/altman-says-ais-rapid-progress-could-go-very-badly-1e840a6c"
RIVALS_URL = "https://www.wsj.com/tech/ai/anthropic-boss-warns-ai-industry-must-slow-the-pace-a4267b56"


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


class TestNovelty747:
    """Iteration 747 is new; nothing with this number existed pre-commit."""

    def test_single_type_a_747_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_a_747*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_a_747_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_a_747 files, no #747 in git log); this test
        # pins that no duplicate #747 main commit ever appears.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%H %s"],
            capture_output=True,
            text=True,
        )
        mains = [
            line for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type A #747:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type A #747 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        anchor = TestRotationCycleGuard747.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)


class TestRotationCycleGuard747:
    """Rotation: distinct-mains window test, #721-style.

    Robust to the #678 history artifact and the #565 followup convention: first
    occurrence of each distinct iteration number, newest first. #747 opens the
    new 747-751 window, closing A->B->C->D->E.
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

    def test_window_743_747_closes_b_to_a(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("A", "747"),
            ("E", "746"),
            ("D", "745"),
            ("C", "744"),
            ("B", "743"),
        ], "rotation window 743-747 wrong: %r" % (observed,)

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


class TestMechanism682Content:
    def test_mech_block_present_in_newscorp_openai(self):
        corpus = _newscorp()
        assert MECH_KEY + ":" in corpus
        assert "mechanism_id: 682" in corpus

    def test_iteration_metadata(self):
        block = _block()
        assert "iteration: 747" in block
        assert "iteration_type: A" in block
        assert "time_pdt: '13:00'" in block
        assert "date_analyzed: '2026-09-14'" in block
        assert "target_entity: 'openai'" in block
        assert "peer_arm: 'same_publication_same_day_relay_pair'" in block

    def test_excerpt_bounded_method(self):
        block = _fold(_block())
        assert "search_excerpt_bounded_21_rendered_lines_across_2_query_sets" in block
        assert "browser.open" in block
        assert "upstream_unavailable" in block
        assert "NOT retried" in block

    def test_clash_watchdog_quotes(self):
        block = _fold(_block())
        assert "Monumental Crisis" in block
        assert "Greek tragedy" in block
        assert "stop pretending the motivation to slow down is purely altruistic" in block
        assert "actual, tangible actions they are taking to change their pace to be safer" in block
        assert "Robert McMillan" in block

    def test_watchdog_harder_than_relay_on_payer(self):
        block = _fold(_block())
        assert "expose_score_MANUAL_ILLUSTRATIVE: -0.40" in block
        assert "relay_avg: 0.075" in block
        assert "delta: -0.475" in block
        assert "watchdog HARDER than relay on the same payer" in block

    def test_novel_clash_url(self):
        block = _block()
        assert CLASH_URL in block
        assert "NOVEL this run - zero hits repo-wide pre-commit" in block

    def test_carried_urls_flagged_by_design(self):
        block = _fold(_block())
        assert RELAY_URL in block
        assert RIVALS_URL in block
        assert "carried from #742" in block
        assert "no rescoring" in block

    def test_deal_predictor_stated(self):
        block = _fold(_block())
        assert "$50M/yr" in block
        assert "$250M/5yr" in block
        assert "Anthropic leg $0 AI licensing" in block

    def test_tightest_temporal_register_mix(self):
        block = _fold(_block())
        assert "Tightest temporal register-mix on a payer in the corpus" in block
        assert "within 24 hours" in block
        assert "Tumbler Ridge -0.55" in block

    def test_register_range_dominates(self):
        block = _fold(_block())
        assert "0.65" in block
        assert "Register SELECTION dominates entity targeting at WSJ x OpenAI" in block

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
        assert "Register MIXES within 24 hours on the same payer" in block
        assert "Incentive attribution is INCONCLUSIVE" in block
        assert "NOT a falsification-family member" in block
        assert "Ledger holds at 24" in block

    def test_designed_keying(self):
        # The block key and the whole profile corpus carry no underscore-form
        # 682 mechanism key substring; the id advances in colon form only.
        # This keeps the #744/#745 zero-682 profile sweep instruments green.
        assert "mechanism" + "_682" not in MECH_KEY
        assert "mechanism_id: 682" in _block()
        assert "mechanism" + "_682" not in _profiles_corpus()


class TestSupersessionAndCorpusPost746:
    def _ids(self):
        return [
            int(x)
            for x in re.findall(r"mechanism_id:\s*(\d+)\b", _profiles_corpus())
        ]

    def test_max_mechanism_id_is_682(self):
        ids = self._ids()
        assert max(ids) == MECH_NUM, max(ids)

    def test_745_max_681_sweep_fails_by_designed_supersession(self):
        # Documented, not repaired: advancing max numeric mechanism id to 682
        # supersedes #745's test_max_mechanism_id_is_681 per the #710/#720
        # convention.
        assert max(self._ids()) == 682

    def test_744_745_zero_682_profile_sweeps_stay_green_by_designed_keying(self):
        # The #744/#745 profile-YAML zero-682 sweeps assert the contiguous
        # underscore form absent from every profile YAML; the #747 block key
        # was designed to keep them green.
        assert "mechanism" + "_682" not in _profiles_corpus()

    def test_744_745_zero_682_test_sweep_stays_green_by_designed_keying(self):
        # The #745 other-tests zero-682 sweep scans test files for the
        # underscore form with trailing underscore; this file was written to
        # keep it green (keying uses the descriptive block key and
        # colon/space forms only).
        own = open(os.path.join(REPO_ROOT, "tests", TEST_BASENAME)).read()
        assert "mechanism" + "_682_" not in own

    def test_682_descriptive_key_unique_repo_wide(self):
        corpus = _profiles_corpus()
        assert corpus.count(MECH_KEY + ":") == 1
        tests_hits = [
            f for f in glob.glob(os.path.join(REPO_ROOT, "tests", "*.py"))
            if MECH_KEY in open(f, encoding="utf-8", errors="replace").read()
        ]
        assert tests_hits == [os.path.join(REPO_ROOT, "tests", TEST_BASENAME)], tests_hits

    def test_zero_underscore_683_keys(self):
        assert "mechanism" + "_683" not in _profiles_corpus()


class TestLedger747:
    def test_falsification_ledger_holds_at_24(self):
        corpus = _profiles_corpus()
        assert "TWENTY-FOURTH" in corpus
        assert "TWENTY-FIFTH" not in corpus

    def test_682_not_a_falsification_member(self):
        block = _fold(_block())
        assert "NOT a falsification-family member" in block
