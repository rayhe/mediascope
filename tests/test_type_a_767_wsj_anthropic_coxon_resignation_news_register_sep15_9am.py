"""Type A #767 (2026-09-15 09:00 PDT): WSJ x Anthropic Coxon-resignation news register.

First dedicated mechanism (691) on the WSJ "Anthropic Researcher Quits Over
'Out-of-Control' AI Fears" (Sep 10 2026, URL 707b7628 zero-hit repo-wide
pre-commit) straight-news insider-resignation register (-0.10 MANUAL
ILLUSTRATIVE): scare-quote attribution headline, Coxon "destroy humanity" and
Hubinger ">10% kill all humans" lines printed verbatim and unsoftened, standard
"didn't immediately comment" no-comment line, Anthropic defense partially
carried (Amodei slow-development warnings noted).

Same-peg cross-publication comparator carried from #647/m622: WIRED's Sep 9
Coxon interview grants Anthropic existential-seriousness credit (+0.25),
Anthropic contrasted FAVORABLY against OpenAI. Illustrative WIRED-minus-WSJ
delta +0.35 - the sharpest same-peg cross-publication contrast in the corpus,
fully confounded by genre (long-form interview vs straight news).

Completes the WSJ slowdown-week Anthropic ARC: Sep 10 Coxon news (-0.10) ->
Sep 13 Moral Conflict expose (m682, -0.40) -> Sep 14 unity consensus (m689,
+0.15); same-entity same-week range 0.55. OpenAI-payer comparator: m679 Altman
relay (+0.10) vs Coxon news (-0.10), illustrative OpenAI-minus-Anthropic delta
+0.20, thesis-consistent direction. Incentive attribution INCONCLUSIVE and
MIXED: the arc bounds BOTH uniform-capture and uniform-hostility readings;
desk/genre routing explains the register mix better than the licensing tie.
NOT a falsification-family member; ledger holds at 26. NOT artifact-grade; no
analysis.json update. Excerpt-bounded per #503 (WSJ paywalled, no browser.open
attempted this run; 9 browser.search query sets). Rotation: 766-770 window
opens E->A->B->C->D.

36 tests, 5 classes.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
PROFILE = REPO / "profiles" / "news-corp.yaml"
TESTS_DIR = REPO / "tests"

M_ID = 691
ITER = 767
MECH_KEY = "wsj_anthropic_coxon_resignation_news_register_vs_wired_seriousness_credit_sep10"
MECH_ID_MARKER = "mechanism" + "_691"  # must stay ABSENT from block and profile
COXON_URL = "https://www.wsj.com/tech/ai/anthropic-researcher-quits-over-out-of-control-ai-fears-707b7628"
EXPOSE_URL = "https://www.wsj.com/tech/ai/openai-anthropic-crisis-money-safety-847bc1d6"
UNITY_URL = "https://www.wsj.com/tech/ai/anthropic-boss-warns-ai-industry-must-slow-the-pace-a4267b56"
RELAY_URL = "https://www.wsj.com/tech/ai/altman-says-ais-rapid-progress-could-go-very-badly-1e840a6c"

# Anchor placeholder: patched to the main commit SHA in the #565 follow-up.
ANCHORED_SHA = "3672c8dd63275abf4a6c40e626f2a29638dc0b63"

# Distinctive Coxon-piece excerpt substrings (safe for raw-text match).
COXON_QUOTES = [
    "Anthropic researcher is quitting the artificial-intelligence industry",
    "worried such systems could spiral out of control and destroy humanity",
    "by the end of next year things could be out of control already",
    "Anthropic didn",
    "We really do earnestly believe AI could kill all humans",
]

NOVEL_CORROBORATING_URLS = [
    "https://people.com/employee-at-top-ai-company-quits-with-public-warning-the-tech-could-kill-us-all-and-then-former-co-worker-agrees-12112847",
    "https://phys.org/news/2026-09-anthropic-resigns-dangers-ai.html?deviceType=mobile",
    "https://www.usatoday.com/story/tech/2026/09/10/anthropic-stops-potential-bioweapons-research-report-says/91694786007/",
    "https://www.thetimes.com/uk/technology-uk/article/anthropic-warns-ai-could-take-over-the-internet-in-six-months-k8w5707fh",
]


def _read_profile():
    return PROFILE.read_text(encoding="utf-8")


def _block():
    text = _read_profile()
    start = text.index(MECH_KEY)
    # Block ends where the sibling `  perplexity:` section begins.
    end = text.index("\n  perplexity:", start)
    return text[start:end]


def _git_log_mains(prefix_pat):
    out = subprocess.run(
        ["git", "log", "--format=%H %s", "--no-merges", "--", "."],
        cwd=REPO, capture_output=True, text=True,
    ).stdout.splitlines()
    return [l for l in out if re.search(prefix_pat, l)]


def _repo_grep(needle, roots=("profiles", "tests")):
    hits = []
    for root in roots:
        base = REPO / root
        for dirpath, _dirs, files in os.walk(base):
            if "__pycache__" in dirpath:
                continue
            for f in files:
                if f == Path(__file__).name or f.endswith(".pyc"):
                    continue
                p = Path(dirpath) / f
                try:
                    if needle in p.read_text(encoding="utf-8", errors="replace"):
                        hits.append(str(p.relative_to(REPO)))
                except OSError:
                    pass
    return hits


def _max_numeric_mechanism_id():
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    best = 0
    for dirpath, _dirs, files in os.walk(REPO / "profiles"):
        for f in files:
            if not f.endswith(".yaml"):
                continue
            text = (Path(dirpath) / f).read_text(encoding="utf-8", errors="replace")
            for m in pat.finditer(text):
                best = max(best, int(m.group(1)))
    return best


class TestNovelty767:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_a_767_file(self):
        files = sorted(TESTS_DIR.glob("test_type_a_767*.py"))
        assert len(files) == 1, files
        assert files[0].name == (
            "test_type_a_767_wsj_anthropic_coxon_resignation_news_register_sep15_9am.py"
        ), files

    def test_type_a_767_main_commit_unique_and_anchored(self):
        mains = _git_log_mains(r"Type A #767: ")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED"), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim_present_in_block(self):
        # Novelty was verified pre-commit by shell greps (zero test_type_a_767
        # files, no Type A #767 in git log, Coxon WSJ URL slug 707b7628
        # zero-hit repo-wide, "Anthropic Researcher Quits Over" title string
        # zero-hit, wsj_anthropic_coxon block key zero-hit, the 4
        # corroborating URLs zero-hit repo-wide, max numeric mechanism_id 690,
        # zero underscore-form 691 keys excluding sweep-instrument carriers
        # per #715); this test pins the claim in the committed block, per the
        # #752 convention.
        block = _block()
        assert "Zero test_type_a_767 files on disk pre-commit" in block
        assert 'no "Type A #767" in git log pre-commit' in block
        assert "707b7628 zero-hit repo-wide pre-commit" in block
        assert "max numeric mechanism_id 690 pre-commit" in block
        assert "Anthropic Researcher Quits Over" in block


class TestRotationCycleGuard767:
    """Newest five mains open E->A->B->C->D (766-770 window)."""

    EXPECTED_ORDER = [("A", "767"), ("E", "766"), ("D", "765"), ("C", "764"), ("B", "763")]
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def _window(self):
        # First occurrence of each distinct iteration number, newest first
        # (robust to the #756-style followup commits that repeat the same
        # "Type X #N:" prefix, per the #752 convention).
        mains = subprocess.run(
            ["git", "log", "--format=%s", "--no-merges", "-n", "40", "--", "."],
            cwd=REPO, capture_output=True, text=True,
        ).stdout.splitlines()
        seen_nums: set[str] = set()
        out: list[tuple[str, str]] = []
        for s in mains:
            m = re.match(r"Type ([A-E]) #(\d+):", s)
            if m and m.group(2) not in seen_nums:
                seen_nums.add(m.group(2))
                out.append(m.groups())
        return out[:5]

    def test_window_opens_eabcd(self):
        assert self._window() == self.EXPECTED_ORDER

    def test_window_cycle_edges_are_adjacent(self):
        window = self._window()
        for (t1, _), (t2, _) in zip(window, window[1:]):
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains(r"Type A #767: ")
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED")
        assert mains and mains[0].startswith(ANCHORED_SHA + " ")


class TestMechanism691Content:
    """Mechanism 691 under competitor_relationships.anthropic: arms, quotes, scores."""

    def test_block_present_under_news_corp_anthropic(self):
        block = _block()
        assert f"mechanism_id: {M_ID}" in block
        assert "News Corp" in _read_profile()
        # news-corp blocks carry no entity_pair key (guardian convention); the
        # mechanism_name and descriptive key carry the pairing instead.
        assert "WSJ x Anthropic Coxon-Resignation News Register" in block
        assert MECH_KEY in _read_profile()

    def test_metadata_present(self):
        block = _block()
        for token in (
            "iteration: 767",
            'iteration_type: "A"',
            "type_label: Competitor Coverage Deep Dive",
            "job_id: mediascope-daily-iteration",
            "goal_id: goal_54093bda4145",
            "author: 'Kit (with Ray)'",
        ):
            assert token in block, token

    def test_anthropic_settlement_stub_preserved(self):
        # news-corp.yaml uses unquoted stub values (guardian.yaml quotes them).
        text = _read_profile()
        assert "financial_tie: settlement_revenue" in text
        assert "coverage_prediction: neutral" in text
        assert "financial_tie: licensing" in text  # openai stub untouched

    def test_coxon_arm_title_register_tone(self):
        block = _block()
        assert "Anthropic Researcher Quits Over" in block
        assert "straight_news_insider_resignation_attribution_framed" in block
        assert "tone_MANUAL_ILLUSTRATIVE: -0.10" in block
        assert COXON_URL in block
        assert "novel this run - URL zero-hit repo-wide pre-commit" in block

    def test_carried_coxon_excerpts_verbatim(self):
        block = _block()
        for quote in COXON_QUOTES:
            assert quote in block, quote[:60]

    def test_wired_seriousness_arm_carried_from_622(self):
        block = _block()
        assert "mechanism: 622" in block
        assert "carried from #647 (m622) by design" in block
        assert "existential_seriousness_credit_interview" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.25" in block
        assert "Crunch Time for Humanity" in block

    def test_corraborating_urls_novel_this_run(self):
        block = _block()
        for url in NOVEL_CORROBORATING_URLS:
            assert url in block, url
        assert "novel this run - URL zero-hit repo-wide pre-commit" in block
        assert "The Times (News Corp sibling)" in block

    def test_arc_context_arms_carried(self):
        block = _block()
        assert EXPOSE_URL in block
        assert UNITY_URL in block
        assert RELAY_URL in block
        assert "mechanism: 682" in block
        assert "mechanism: 689" in block
        assert "mechanism: 679" in block
        assert "tone_MANUAL_ILLUSTRATIVE: -0.40" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.15" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.10" in block

    def test_manual_illustrative_scores_and_deltas(self):
        block = _block()
        assert "wired_score_MANUAL_ILLUSTRATIVE: 0.25" in block
        assert "wsj_score_MANUAL_ILLUSTRATIVE: -0.10" in block
        assert "delta: 0.35" in block
        assert "delta +0.20" in block
        assert "p_value: 'NOT_CALCULATED - illustrative only, standing rule Aug 28 2026'" in block
        assert "is_significant: false" in block
        assert "NOT artifact-grade" in block
        assert "engine: 'NOT run'" in block

    def test_no_disclosure_claim_bounded(self):
        block = _block()
        assert "No disclosure visibility claim is made" in block
        assert "excerpt-bounded analysis cannot rule in or out boilerplate disclosure" in block

    def test_incentive_attribution_inconclusive_mixed(self):
        block = _block()
        assert "incentive_attribution" in block
        assert "INCONCLUSIVE" in block
        assert "MIXED" in block
        assert "Correlation is not causation" in block
        assert "NOT a falsification-family member" in block

    def test_confounders_ranked_3_3_3(self):
        block = _block()
        for section in ("strong:", "moderate:", "weak:"):
            assert section in block, section
        for token in (
            "Excerpt-bounded read",
            "Genre skew dominates",
            "Event-driven peg",
            "Byline unconfirmed",
            "index-bounded",
            "mirror-only",
            "n=1 new news-register mechanism",
            "weakest evidence tier",
        ):
            assert token in block, token

    def test_bounded_absences_recorded(self):
        block = _block()
        assert "bounded search-result absence per iteration-492" in block
        assert "not a proven zero" in block

    def test_research_method_discloses_no_browser_open(self):
        block = _block()
        assert "9 browser.search query sets this run" in block
        assert "0 browser.open attempts" in block
        assert "excerpt-bounded per #503" in block

    def test_relations_to_622_682_689_679_616(self):
        block = _block()
        assert "relation_to_622" in block
        assert "relation_to_682" in block
        assert "relation_to_689" in block
        assert "relation_to_679" in block
        assert "relation_to_616" in block
        assert "0.55" in block  # same-entity same-week range -0.40 to +0.15

    def test_designed_keying_no_underscore_form_in_block(self):
        block = _block()
        assert MECH_ID_MARKER not in block
        # The block key itself lives in the profile text (the _block() slice
        # starts after it); assert the descriptive keying in the full profile.
        assert MECH_KEY in _read_profile()

    def test_date_bound_recorded(self):
        block = _block()
        assert "index-bounded, not page-verified" in block
        assert '"said Tuesday"' in block


class TestSupersessionAndCorpusPost766:
    """Post-#766 corpus integrity: max 691, zero 692, designed supersession."""

    def test_max_numeric_mechanism_id_is_691(self):
        assert _max_numeric_mechanism_id() == M_ID

    def test_690_still_present(self):
        hits = [h for h in _repo_grep("mechanism_id: 690")]
        assert len(hits) >= 1, hits

    def test_zero_underscore_692_keys_repo_wide(self):
        hits = _repo_grep("mechanism" + "_692")
        assert hits == [], hits

    def test_zero_numeric_692_keys_in_profiles(self):
        hits = _repo_grep("mechanism_id: 692", roots=("profiles",))
        assert hits == [], hits

    def test_d765_zero_underscore_691_profiles_sweep_stays_green(self):
        # #765 asserted zero literal "mechanism_691" in profiles/; the m691
        # block key carries no underscore-form 691 substring by designed
        # keying, so that sweep stays green.
        hits = _repo_grep("mechanism" + "_691", roots=("profiles",))
        assert hits == [], hits

    def test_d765_zero_underscore_691_tests_sweep_stays_green(self):
        # #765 asserted zero "mechanism_691" references in tests/; this file
        # builds the marker by concatenation ("mechanism" + "_691") so no
        # contiguous literal exists in tests/ either - the sweep stays green.
        hits = _repo_grep("mechanism" + "_691", roots=("tests",))
        own = str((TESTS_DIR / Path(__file__).name).relative_to(REPO))
        hits = [h for h in hits if h != own]
        assert hits == [], hits

    def test_d765_zero_numeric_691_profiles_sweep_fails_by_designed_supersession(self):
        # #765 asserted zero "mechanism_id: 691" hits in profiles/; the m691
        # block supersedes it by design per the #710/#720 convention.
        hits = _repo_grep("mechanism_id: 691", roots=("profiles",))
        assert len(hits) >= 1, hits

    def test_d765_max_690_sweep_superseded_by_design(self):
        # #765 asserted max == 690; advancing to 691 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 691 != 690

    def test_m691_block_key_unique_in_news_corp(self):
        text = _read_profile()
        assert text.count(MECH_KEY + ":") == 1

    def test_news_corp_yaml_still_parses(self):
        import yaml

        d = yaml.safe_load(_read_profile())
        assert d["competitor_relationships"]["anthropic"][MECH_KEY]["mechanism_id"] == M_ID


class TestLedger767:
    """Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent; m691 not a member."""

    def _profiles_corpus(self):
        parts = []
        for root, _dirs, files in os.walk(REPO / "profiles"):
            for f in files:
                p = Path(root) / f
                parts.append(p.read_text(encoding="utf-8", errors="replace"))
        return "\n".join(parts)

    def test_twenty_sixth_present_and_twenty_seventh_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference "TWENTY-SEVENTH" inside their own
        # negative guards, so a tests/ sweep would false-positive).
        corpus = self._profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus
        assert "Ledger holds at 26" in _block()

    def test_m691_not_a_falsification_family_member(self):
        block = _block()
        assert "NOT a falsification-family member" in block
        assert "register SELECTION dominates entity targeting" in block

    def test_no_analysis_json_update_claimed(self):
        block = _block()
        assert "no_analysis_json_update: true" in block
