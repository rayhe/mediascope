"""Type A #737: FT x Anthropic slowdown-week profitability scoop register test (Sep 14 2026, 02:00 PDT).

The Financial Times ran a constructive company-briefed business scoop on
Anthropic on Sun Sep 13, 2026 (adjusted operating income positive for a
second straight quarter, 80%+ gross margins before partner revenue sharing
and training costs, IPO-framed; attested via Reuters re-report, FT original
paywalled). It published in the SAME 48-hour window as the slowdown-week
cluster: Amodei's 3800-word "We Must Pace the Frontier" essay (Sep 12),
the Coxon resignation (Sep 8, 79M+ X views, Hubinger agreement), Altman's
no-2026-IPO safety framing (Fortune, Sep 12), WSJ's adversarial "Anthropic's
Moral Conflict" piece (Sep 13), WSJ's "Biggest AI Rivals Agree They Need to
Slow It Down" (Sep 14), Reuters Breakingviews slowdown commentary (Sep 14),
and CNN's Anderson Cooper exclusive (Sep 12). FT's weekend selection was
the constructive investor-briefing scoop, not the Coxon/moral-conflict
accountability lane (bounded search-result absence across 3 query sets, not
a proven zero). Combined with mechanism 643 (adversarial AISI-refusal
watchdog scoop, Sep 9/10, -0.45 MANUAL ILLUSTRATIVE), FT's Anthropic register
MIXES within one week: watchdog on regulatory refusal, constructive on
company-briefed business numbers. Vs Meta comparator (carried): Meta's AI
work is never covered through the business-constructive lens - the
concentration paradox (Murgia 2025-26: Anthropic 9+, OpenAI 4, Google 4,
Meta 0 AI-lens articles); FT Meta Muse is neutral product-distribution
(+0.05, carried from mechanism 625). Incentive attribution INCONCLUSIVE:
no direct FT-Anthropic licensing deal exists (OpenAI holds the $5-10M/yr
FT deal; Anthropic is $0 direct), so a company-briefed investor scoop needs
no financial explanation - beat-access and news-value story. NOT a
falsification-family member (ledger holds at 24). NOT artifact-grade.
Correlation is not causation.

5 browser.search query sets this run; all URLs verbatim from search-result
Full-URL listings; 6 novel this-run URLs; 2 peer-context URLs carried from
mechanisms 717 and 643 by design; no ft.com URL reconstructed.
"""

import glob
import os
import re
import subprocess

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = os.path.basename(__file__)
MECH_KEY = "mechanism_676_ft_anthropic_slowdown_week_profitability_scoop_register_sep14"
MECH_NUM = 676


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _ft():
    return _read("profiles/financial-times.yaml")


def _fold(block):
    # YAML folding joins wrapped lines with spaces; normalize the same way
    # so multi-line assertions are not broken by source line breaks.
    return re.sub(r"\s+", " ", block)


def _block():
    corpus = _ft()
    return corpus.split(MECH_KEY + ":")[1].split("\n  x_twitter:")[0]


class TestNovelty737:
    """Iteration 737 is new; nothing with this number existed pre-commit."""

    def test_single_type_a_737_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_a_737*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_a_737_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_a_737 files, no #737 in git log); this test
        # pins that no duplicate #737 main commit ever appears.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%H %s"],
            capture_output=True,
            text=True,
        )
        mains = [
            line for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type A #737:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type A #737 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        anchor = TestRotationCycleGuard737.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)


class TestRotationCycleGuard737:
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

    def test_window_733_737_closes_e_to_a(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("A", "737"),
            ("E", "736"),
            ("D", "735"),
            ("C", "734"),
            ("B", "733"),
        ], "rotation window 733-737 wrong: %r" % (observed,)

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


class TestMechanism676Content:
    def test_mech_676_block_present_in_ft_anthropic(self):
        corpus = _ft()
        assert MECH_KEY + ":" in corpus
        assert "mechanism_id: 676" in corpus

    def test_iteration_metadata(self):
        block = _block()
        assert "iteration: 737" in block
        assert "iteration_type: A" in block
        assert "iteration_time: 2026-09-14 02:00 PDT" in block
        assert 'entity_pair: "Anthropic vs Meta"' in block

    def test_finding_states_register_mix_not_falsification(self):
        block = _fold(_block())
        assert "register MIXES within one week" in block
        assert "Incentive attribution is INCONCLUSIVE" in block
        assert "NOT a member - register-mix refinement" in block
        assert "Ledger holds at 24" in block

    def test_manual_illustrative_discipline(self):
        block = _block()
        assert "MANUAL ILLUSTRATIVE" in block
        assert "NOT_CALCULATED" in block
        assert "is_significant: false" in block
        assert "NOT" in block and "artifact-grade" in block
        assert "engine NOT run" in block

    def test_novelty_vs_existing_643_717(self):
        block = _block()
        assert "mechanism 643" in block
        assert "mechanism 717" in block
        assert "mechanism 441" in block
        assert "Zero mechanism_676 keys repo-wide pre-commit" in block

    def test_bounded_absence_language(self):
        block = _fold(_block())
        assert "bounded search-result absence" in block
        assert "not a proven zero" in block
        assert "NONE_SURFACED_BOUNDED_ABSENCE" in block

    def test_source_urls_novel_this_run(self):
        block = _block()
        for url in [
            "https://www.reuters.com/business/retail-consumer/anthropic-tells-investors-it-will-be-profitable-second-straight-quarter-ft-2026-09-13/",
            "https://www.cnn.com/2026/09/12/tech/anthropic-ceo-essay-ai?cid=external-feeds_iluminar_meta",
            "https://www.wsj.com/tech/ai/anthropics-moral-conflict-is-playing-out-in-real-time-c503e0c1",
            "https://www.wsj.com/tech/ai/anthropic-boss-warns-ai-industry-must-slow-the-pace-a4267b56",
            "https://www.reuters.com/commentary/breakingviews/ai-frontier-slowdown-could-give-second-tier-leg-up-2026-09-14/",
            "https://www.tradingview.com/news/stocktwits:31ab54064094b:0-anthropic-ipo-claude-maker-reportedly-targets-second-straight-quarter-of-adjusted-profit-as-ceo-s-ai-slowdown-call-sparks-debate/",
        ]:
            assert url in block, url

    def test_carried_urls_flagged(self):
        block = _fold(_block())
        assert "carried from mechanisms 717 and 643 by design" in block
        assert "mechanism 717 (#717 Type A)" in block
        assert "mechanism 643 (#682 Type A)" in block

    def test_no_reconstructed_ft_url(self):
        block = _fold(_block())
        assert "no ft.com URLs constructed" in block
        assert "FT original paywalled" in block

    def test_financial_predictor_stated(self):
        block = _fold(_block())
        assert "$5-10M per yr FT deal" in block
        assert "Anthropic is $0 direct" in block

    def test_concentration_paradox_carried(self):
        block = _fold(_block())
        assert "concentration paradox" in block
        assert "Meta 0 AI-lens articles" in block

    def test_open_empirical_test_named(self):
        block = _fold(_block())
        assert "Sep 23-24 Meta Connect" in block


class TestSupersessionAndCorpusPost736:
    def _profiles_corpus(self):
        parts = []
        for f in glob.glob(os.path.join(REPO_ROOT, "profiles", "*.yaml")):
            parts.append(open(f, encoding="utf-8", errors="replace").read())
        return "\n".join(parts)

    def test_max_mechanism_id_is_676(self):
        ids = [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)\b", self._profiles_corpus())]
        modern = [i for i in ids if i >= 600]
        assert max(modern) == 676, max(modern)

    def test_734_zero_676_sweep_fails_by_designed_supersession(self):
        # Documented, not repaired: advancing max numeric mechanism id to
        # 676 supersedes #734's zero-mechanism_676 repo-wide sweep per the
        # #710/#720 convention.
        corpus = self._profiles_corpus()
        assert "mechanism_676_" in corpus
        ids = [int(x) for x in re.findall(r"mechanism_id:\s*['\"]?(\d+)", corpus)]
        assert 676 in ids

    def test_735_zero_676_sweep_fails_by_designed_supersession(self):
        # Same convention for #735's test_max_mechanism_id_is_675 and
        # test_zero_mechanism_676_keys: advancing to 676 supersedes them.
        corpus = self._profiles_corpus()
        ids = [int(x) for x in re.findall(r"mechanism_id:\s*['\"]?(\d+)", corpus)]
        assert max(ids) >= 676

    def test_676_key_unique_repo_wide(self):
        corpus = self._profiles_corpus()
        keys = re.findall(r"\bmechanism_676_[a-z0-9_]+\b", corpus)
        assert set(keys) == {MECH_KEY}, keys

    def test_zero_underscore_677_keys(self):
        assert "mechanism_677_" not in self._profiles_corpus()


class TestLedger737:
    def test_falsification_ledger_holds_at_24(self):
        parts = []
        for f in glob.glob(os.path.join(REPO_ROOT, "profiles", "*.yaml")):
            parts.append(open(f, encoding="utf-8", errors="replace").read())
        corpus = "\n".join(parts)
        assert "TWENTY-FOURTH" in corpus
        assert "TWENTY-FIFTH" not in corpus

    def test_676_not_a_falsification_member(self):
        block = _block()
        assert "NOT a member - register-mix refinement" in block
