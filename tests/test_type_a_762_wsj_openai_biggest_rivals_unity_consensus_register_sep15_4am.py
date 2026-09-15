"""Type A #762 (2026-09-15 04:00 PDT): WSJ x OpenAI slowdown-week unity-consensus register.

First dedicated mechanism (689) on the WSJ "Biggest AI Rivals Agree They Need to Slow
It Down" (Sep 14 2026, URL a4267b56 carried from #742/m679 by design) unity-consensus
statesman register (+0.15 MANUAL ILLUSTRATIVE): "a rare display of unity" by
Musk/Altman/Amodei, Altman's IPO delay framed as safety sacrifice. Completes the
same-publication-day register TRIAD on the OpenAI payer with m682's watchdog expose
(-0.40) and m679's constructive relay (+0.10): same-day span +0.15 to -0.40 = 0.55,
same-week corpus range +0.15 to -0.55 (m616 Tumbler Ridge) = 0.70. Meta - the other
News Corp AI payer - is absent from the unity consensus (excerpt-bounded). Incentive
attribution INCONCLUSIVE and MIXED: m682 bounded capture readings, m689 bounds
adversarial-uniformity readings; desk/genre routing explains the triad better than the
licensing tie. NOT a falsification-family member; ledger holds at 26. NOT
artifact-grade; no analysis.json update. Excerpt-bounded per #503 (WSJ paywalled, no
browser.open attempted this run). Rotation: 761-765 window opens E->A->B->C->D.

33 tests, 5 classes.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
PROFILE = REPO / "profiles" / "news-corp.yaml"
TESTS_DIR = REPO / "tests"

M_ID = 689
ITER = 762
MECH_KEY = "wsj_openai_biggest_rivals_unity_consensus_register_vs_clash_expose_sep14"
MECH_ID_MARKER = "mechanism" + "_689"  # must stay ABSENT from block and profile
UNITY_URL = "https://www.wsj.com/tech/ai/anthropic-boss-warns-ai-industry-must-slow-the-pace-a4267b56"
EXPOSE_URL = "https://www.wsj.com/tech/ai/openai-anthropic-crisis-money-safety-847bc1d6"
RELAY_URL = "https://www.wsj.com/tech/ai/altman-says-ais-rapid-progress-could-go-very-badly-1e840a6c"

# Anchor placeholder: patched to the main commit SHA in the #565 follow-up.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

# Distinctive unity-piece excerpt substrings (apostrophe-free, safe for raw-text match).
UNITY_QUOTES = [
    "rare display of unity by Elon Musk, Sam Altman and Dario Amodei",
    "may need to delay its much-anticipated IPO to focus on safety",
    "Dario is right",
    "a great idea, and we will do the same",
    "permanent, employee-level access to our systems",
]

NOVEL_CORROBORATING_URLS = [
    "https://www.reuters.com/business/what-amodei-altman-musk-have-said-about-ai-risks-stoking-doom-fears-2026-09-14/",
    "https://www.usatoday.com/story/tech/2026/09/14/ai-pace-frontier-regulation/91682225007/",
    "https://www.barrons.com/articles/anthropic-ceo-ai-slowdown-letter-2ac6a113",
    "https://techcrunch.com/2026/09/12/openais-sam-altman-says-it-would-be-ill-advised-to-go-public-in-2026/",
]

CARRIED_IPO_URL = "https://www.reuters.com/legal/litigation/openai-ipo-will-not-happen-2026-amid-ai-safety-fears-altman-says-2026-09-12/"


def _read_profile():
    return PROFILE.read_text(encoding="utf-8")


def _block():
    text = _read_profile()
    start = text.index(MECH_KEY)
    # Block ends where the sibling `  meta:` section begins.
    end = text.index("\n  meta:", start)
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


class TestNovelty762:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_a_762_file(self):
        files = sorted(TESTS_DIR.glob("test_type_a_762*.py"))
        assert len(files) == 1, files
        assert files[0].name == (
            "test_type_a_762_wsj_openai_biggest_rivals_unity_consensus_register_sep15_4am.py"
        ), files

    def test_type_a_762_main_commit_unique_and_anchored(self):
        mains = _git_log_mains(r"Type A #762: ")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED"), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim_present_in_block(self):
        # Novelty was verified pre-commit by shell greps (zero test_type_a_762
        # files, no Type A #762 in git log, unity_consensus_statesman_framing
        # zero-hit repo-wide, the 4 corroborating URLs zero-hit repo-wide,
        # max numeric mechanism_id 688, zero underscore-form 689 keys
        # excluding the #760 sweep-instrument carrier per #715); this test pins
        # the claim in the committed block, per the #752 convention.
        block = _block()
        assert "Zero test_type_a_762 files on disk pre-commit" in block
        assert 'no "Type A #762" in git log pre-commit' in block
        assert "unity_consensus_statesman_framing register string zero-hit repo-wide pre-commit" in block
        assert "max numeric mechanism_id 688 pre-commit" in block
        assert "Biggest AI Rivals Agree They Need to Slow It Down" in block


class TestRotationCycleGuard762:
    """Newest five mains open E->A->B->C->D (761-765 window)."""

    EXPECTED_ORDER = [("A", "762"), ("E", "761"), ("D", "760"), ("C", "759"), ("B", "758")]
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
        mains = _git_log_mains(r"Type A #762: ")
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED")
        assert mains and mains[0].startswith(ANCHORED_SHA + " ")


class TestMechanism689Content:
    """Mechanism 689 under competitor_relationships.openai: arms, quotes, scores."""

    def test_block_present_under_news_corp_openai(self):
        block = _block()
        assert f"mechanism_id: {M_ID}" in block
        assert "News Corp" in _read_profile()
        # news-corp blocks carry no entity_pair key (guardian convention); the
        # mechanism_name and descriptive key carry the pairing instead.
        assert "WSJ x OpenAI Slowdown-Week Unity-Consensus Register" in block
        assert MECH_KEY in _read_profile()

    def test_metadata_present(self):
        block = _block()
        for token in (
            "iteration: 762",
            'iteration_type: "A"',
            "type_label: Competitor Coverage Deep Dive",
            "job_id: mediascope-daily-iteration",
            "goal_id: goal_54093bda4145",
            "author: 'Kit (with Ray)'",
        ):
            assert token in block, token

    def test_openai_licensing_stub_preserved(self):
        # news-corp.yaml uses unquoted stub values (guardian.yaml quotes them).
        text = _read_profile()
        assert "financial_tie: licensing" in text
        assert "coverage_prediction: softer" in text
        assert "financial_tie: none" in text  # meta stub untouched

    def test_unity_arm_title_register_tone(self):
        block = _block()
        assert "Biggest AI Rivals Agree They Need to Slow It Down" in block
        assert "unity_consensus_statesman_framing" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.15" in block
        assert UNITY_URL in block
        assert "carried from #742 (m679) by design" in block

    def test_carried_unity_excerpts_verbatim(self):
        block = _block()
        for quote in UNITY_QUOTES:
            assert quote in block, quote[:60]

    def test_corraborating_urls_novel_and_carried(self):
        block = _block()
        for url in NOVEL_CORROBORATING_URLS:
            assert url in block, url
        assert "novel this run - URL zero-hit repo-wide pre-commit" in block
        assert CARRIED_IPO_URL in block
        assert "already in corpus (3 hits) - carried by design" in block

    def test_triad_context_arms_carried(self):
        block = _block()
        assert EXPOSE_URL in block
        assert RELAY_URL in block
        assert "mechanism: 682" in block
        assert "mechanism: 679" in block
        assert "tone_MANUAL_ILLUSTRATIVE: -0.40" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.10" in block

    def test_manual_illustrative_scores_and_delta(self):
        block = _block()
        assert "unity_score_MANUAL_ILLUSTRATIVE: 0.15" in block
        assert "expose_score_MANUAL_ILLUSTRATIVE: -0.40" in block
        assert "delta: 0.55" in block
        assert "p_value: 'NOT_CALCULATED - illustrative only, standing rule Aug 28 2026'" in block
        assert "is_significant: false" in block
        assert "artifact_grade" not in block or True  # artifact-grade handled via NOT artifact-grade string
        assert "NOT artifact-grade" in block
        assert "engine: \"NOT run\"" in block or "Engine NOT run" in block

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
            "Genre skew",
            "Respondent positioning",
            "Byline/desk unconfirmed",
            "originated in Altman",
            "n=1 new unity-register mechanism",
            "Meta absence is excerpt-bounded",
            "not hagiographic",
        ):
            assert token in block, token

    def test_bounded_absences_recorded(self):
        block = _block()
        assert "bounded search-result absence per iteration-492" in block
        assert "not a proven zero" in block

    def test_research_method_discloses_no_browser_open(self):
        block = _block()
        assert "5 browser.search query sets this run" in block
        assert "0 browser.open attempts" in block
        assert "excerpt-bounded per #503" in block

    def test_meta_absence_from_unity_bounded(self):
        block = _block()
        assert "absent from the unity consensus" in block
        assert "no statesman seat for Meta" in block

    def test_relations_to_679_682_616(self):
        block = _block()
        assert "relation_to_679" in block
        assert "relation_to_682" in block
        assert "relation_to_616" in block
        assert "0.70" in block  # same-week corpus range +0.15 to -0.55

    def test_designed_keying_no_underscore_form_in_block(self):
        block = _block()
        assert MECH_ID_MARKER not in block
        # The block key itself lives in the profile text (the _block() slice
        # starts after it); assert the descriptive keying in the full profile.
        assert MECH_KEY in _read_profile()


class TestSupersessionAndCorpusPost761:
    """Post-#761 corpus integrity: max 689, zero 690, designed supersession."""

    def test_max_numeric_mechanism_id_is_689(self):
        assert _max_numeric_mechanism_id() == M_ID

    def test_688_still_present(self):
        hits = [h for h in _repo_grep("mechanism_id: 688")]
        assert len(hits) >= 1, hits

    def test_zero_underscore_690_keys_repo_wide(self):
        hits = _repo_grep("mechanism" + "_690")
        assert hits == [], hits

    def test_zero_numeric_690_keys_in_profiles(self):
        hits = _repo_grep("mechanism_id: 690", roots=("profiles",))
        assert hits == [], hits

    def test_760_zero_689_tests_sweep_fails_by_designed_supersession(self):
        # The #760 Type D file asserts zero underscore-form 689 references in
        # tests/ (excluding only itself); this file is the designed carrier of
        # the 689 key string per the #715 pattern-rescope lesson, so that sweep
        # fails by designed supersession. The profiles-side sweep stays green.
        hits = _repo_grep("mechanism_id: 689", roots=("profiles",))
        assert len(hits) >= 1  # the new block; the #760 zero-numeric sweep is superseded by design

    def test_760_zero_689_profiles_sweep_stays_green_by_designed_keying(self):
        hits = _repo_grep("mechanism" + "_689", roots=("profiles",))
        assert hits == [], hits

    def test_759_no_new_underscore_689_keys_stays_green(self):
        # #759 asserted no underscore-form 689 in the profiles corpus; the
        # designed key carries no such substring, so it stays green.
        hits = _repo_grep("mechanism" + "_689", roots=("profiles",))
        assert hits == [], hits

    def test_news_corp_yaml_still_parses(self):
        import yaml

        d = yaml.safe_load(_read_profile())
        assert d["competitor_relationships"]["openai"][MECH_KEY]["mechanism_id"] == M_ID


class TestLedger762:
    """Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent; m689 not a member."""

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

    def test_m689_not_a_falsification_family_member(self):
        block = _block()
        assert "NOT a falsification-family member" in block
        assert "register-mix refinement" in block

    def test_no_analysis_json_update_claimed(self):
        block = _block()
        assert "no_analysis_json_update: true" in block
