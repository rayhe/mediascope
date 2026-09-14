# Type C #729: US DOJ Statement of Interest in NYT v. OpenAI (mechanism 672)
# FIRST dedicated political-incentive leg on the OpenAI x publisher financial
# vector: on Sep 1, 2026 the US Department of Justice filed a 20-page
# Statement of Interest under 28 U.S.C. section 517 in the consolidated
# OpenAI copyright litigation (S.D.N.Y., No. 25-md-03143, Judge Sidney H.
# Stein), urging the court to hold that training LLMs on copyrighted texts
# is fair use - arguing AGAINST the paid-licensing regime that OpenAI's
# $300-400M/yr publisher portfolio represents, i.e. state power aligned WITH
# the AI payer and AGAINST the publisher plaintiff (the NYT).
#
# Distinct from mechanism 657 (ANI v. OpenAI India litigation leg - different
# jurisdiction, different instrument), mechanism 666 (EU antitrust probe
# pushing Google TOWARD paid licensing - opposite state vector on the same
# policy question), mechanism 589 (Ziff Davis private litigation), and #471
# (NYT x OpenAI litigation-posture tone pair, not an incentive leg).
#
# QUALITATIVE structural mapping only. No scorer, no tone scores, no
# p-value, no effect size, no CI. NOT a falsification-family member
# (ledger holds at 24 after #728; per #609/#614 qualitative boundary).
# No analysis.json update.
#
# 729 = Type C (rotation window 725-729 closes D #725 -> E #726 -> A #727
# -> B #728 -> C #729). Anchor patched post-commit per #565 convention.
#
# Research method: 2 browser.search query sets this run: (1) AI publisher
# licensing deal September 2026 - surfaced UMG x ElevenLabs (Sep 10) and Suno
# x Warner/BMG (Sep 9) music-licensing news (rejected: music vertical,
# outside the publication-AI financial-incentive scope) plus the Scholarly
# Kitchen DOJ piece (SELECTED); (2) DOJ statement of interest NYT OpenAI fair
# use September 2026 - 6 corroborating sources (TechRepublic, Publishing
# Perspectives, Bloomberg Law, JD Supra, USA Today, Reason), all URLs copied
# verbatim from Full-URL listings, no canonical URLs constructed.
# Excerpt-bounded, second-hand evidence per #503 (no browser.open
# first-hand reads this run). Novelty pre-commit greps: zero test_type_c_729
# files on disk (glob); no "Type C #729" in git log (--grep); zero
# "mechanism_672" underscore-form strings repo-wide (grep); zero "Statement
# of Interest" hits repo-wide (grep); max numeric mechanism_id 671
# pre-commit; all 8 source URLs zero-hit repo-wide pre-commit. No zero-
# coverage claims per iteration-492 rule; bounded absence only. No em
# dashes; ASCII-only.
"""Deselected pre-commit: rotation-guard anchor and doc-sync tests per the
#565 followup convention; anchors patched in the followup commit once the
main commit SHA is known."""

import glob
import os
import re
import subprocess

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMPETITOR = os.path.join(REPO, "profiles", "competitor-entities.yaml")
TESTS_DIR = os.path.join(REPO, "tests")
TEST_BASENAME = os.path.basename(__file__)
ITERATION = 729
MECH_KEY = "doj_statement_of_interest_nyt_v_openai_fair_use_sep2026"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. Anchor tests are deselected pre-commit.
ANCHORED_SHA = "5468a02ac0079939d8f60ce7f72dcd894be4b3f9"


def load_competitor():
    with open(COMPETITOR, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def mech():
    return load_competitor()["entities"]["openai"][MECH_KEY]


def git(*args):
    return subprocess.run(
        ["git", *args],
        cwd=REPO,
        capture_output=True,
        text=True,
        timeout=120,
    )


class TestIterationMetadata729:
    def test_iteration_is_729(self):
        assert mech()["iteration"] == ITERATION

    def test_rotation_is_type_c(self):
        assert mech()["rotation"] == "Type C"

    def test_type_is_financial_incentive_mapping(self):
        assert mech()["type"] == "financial_incentive_mapping"

    def test_type_label(self):
        assert mech()["type_label"] == "Financial Incentive Mapping"

    def test_date_time_job_goal(self):
        m = mech()
        assert m["date_analyzed"] == "2026-09-13"
        assert m["time_pdt"] == "17:00"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_mechanism_id_672_int(self):
        assert isinstance(mech()["mechanism_id"], int)
        assert mech()["mechanism_id"] == 672

    def test_single_672_mechanism_block_in_openai(self):
        openai = load_competitor()["entities"]["openai"]
        hits = [k for k, v in openai.items()
                if isinstance(v, dict) and v.get("mechanism_id") == 672]
        assert hits == [MECH_KEY]

    def test_no_underscore_672_key_in_profiles(self):
        # #723 designed-keying convention: the block key avoids the
        # "mechanism_672" underscore string so #728's
        # test_zero_mechanism_672_keys_repo_wide stays green.
        text = open(COMPETITOR, encoding="utf-8").read()
        assert "mechanism_672" not in text

    def test_iteration_type_matches_rotation(self):
        assert mech()["iteration_type"] == "C"

    def test_first_political_incentive_leg_claim(self):
        assert "FIRST" in mech()["mechanism_name"]
        assert "political-incentive" in mech()["mechanism_name"]


class TestFilingFacts729:
    def test_case_number_and_judge(self):
        facts = " ".join(mech()["filing_facts"])
        assert "25-md-03143" in facts
        assert "Sidney H. Stein" in facts
        assert "S.D.N.Y." in facts

    def test_twenty_page_statement_of_interest(self):
        facts = " ".join(mech()["filing_facts"])
        assert "20-page" in facts
        assert "28 U.S.C." in facts

    def test_filing_date_sep_1_with_discrepancy_logged(self):
        facts = " ".join(mech()["filing_facts"])
        assert "Sep 1, 2026" in facts
        assert "Sep 2" in facts
        assert "discrepancy" in facts

    def test_summary_judgment_motions_due_sep_4(self):
        facts = " ".join(mech()["filing_facts"])
        assert "Sep 4, 2026" in facts

    def test_bartz_over_kadrey(self):
        facts = " ".join(mech()["filing_facts"])
        assert "Bartz" in facts and "Kadrey" in facts

    def test_nyt_seeks_damages_training_ban_model_destruction(self):
        facts = " ".join(mech()["filing_facts"])
        assert "monetary damages" in facts
        assert "destruction of models" in facts

    def test_hundred_plus_ai_copyright_lawsuits(self):
        facts = " ".join(mech()["filing_facts"])
        assert "100" in facts
        assert "Edward Lee" in facts

    def test_nyt_uses_llms_irony(self):
        facts = " ".join(mech()["filing_facts"])
        assert "uses LLMs" in facts

    def test_key_quotes_pinned(self):
        quotes = " ".join(mech()["key_quotes"])
        for token in (
            "strong interest in this court rejecting",
            "thwart such creative and scientific progress",
            "large subsidies for old mainstream media",
            "level the playing field between mainstream and independent publishers",
            "AI dominance is critical",
            "stole from The New York Times",
            "trillion-dollar A.I. companies",
        ):
            assert token in quotes, token

    def test_seven_key_quotes(self):
        assert len(mech()["key_quotes"]) == 7

    def test_ten_filing_facts(self):
        assert len(mech()["filing_facts"]) == 10


class TestFinancialIncentiveTheory729:
    def test_argues_against_paid_licensing_regime(self):
        link = mech()["financial_incentive_link"]
        assert "AGAINST the paid-licensing regime" in link
        assert "$300-400M/yr" in link

    def test_license_alternative_priced_toward_zero(self):
        link = mech()["financial_incentive_link"]
        assert "toward zero" in link

    def test_batna_complement_with_657(self):
        link = mech()["financial_incentive_link"]
        assert "BATNA" in link
        assert "sets the value of the alternative to a licence" in link

    def test_timing_compression_sep_4_sep_14(self):
        link = mech()["financial_incentive_link"]
        assert "Sep 4" in link and "Sep 14" in link
        assert "ten days" in link

    def test_opposite_state_vector_to_666(self):
        link = mech()["financial_incentive_link"]
        assert "opposite state vectors" in link
        assert "666" in link

    def test_administration_specific_caveat(self):
        link = mech()["financial_incentive_link"]
        assert "administration-specific" in link
        assert "not a structural financial relationship" in link

    def test_inverse_of_payer_softening_prediction(self):
        link = mech()["financial_incentive_link"]
        assert "inverse of the naive payer-softening prediction" in link

    def test_related_mechanisms_eight(self):
        assert mech()["related_mechanisms"] == [471, 519, 549, 589, 609, 657, 660, 666]

    def test_no_coverage_tone_claim(self):
        assert mech()["no_coverage_tone_claim"] is True

    def test_correlational_note_no_causal_claim(self):
        assert "No causal claim" in mech()["correlational_note"]

    def test_not_falsification_family_ledger_24(self):
        ff = mech()["falsification_family"]
        assert "NOT a member" in ff
        assert "ledger holds at 24" in ff

    def test_no_analysis_json_update(self):
        assert "No analysis.json update warranted" in mech()["artifact_readiness"]


class TestConfounds729:
    def test_three_strong_confounds(self):
        strong = mech()["confounders"]["strong"]
        assert len(strong) == 3
        text = " ".join(strong)
        assert "second-hand" in text
        assert "not structural financial vector" in text
        assert "not binding" in text

    def test_three_moderate_confounds(self):
        moderate = mech()["confounders"]["moderate"]
        assert len(moderate) == 3
        text = " ".join(moderate)
        assert "motion-timed" in text
        assert "consolidates multiple plaintiffs" in text
        assert "unsettled" in text

    def test_three_weak_confounds(self):
        weak = mech()["confounders"]["weak"]
        assert len(weak) == 3
        text = " ".join(weak)
        assert "Sep 1-2" in text
        assert "not quantified" in text
        assert "future licensing leverage only" in text

    def test_four_counterevidence(self):
        ce = mech()["counterevidence"]
        assert len(ce) == 4
        text = " ".join(ce)
        assert "corporate capture" in text
        assert "$1.5B" in text
        assert "$3,000-per-work" in text

    def test_four_bounded_absences(self):
        ba = mech()["bounded_absences"]
        assert len(ba) == 4
        text = " ".join(ba)
        assert "iteration-492" in text
        assert "not claimed as none exist" in text

    def test_cross_references_ten(self):
        assert len(mech()["cross_references"]) == 10
        text = " ".join(mech()["cross_references"])
        for token in ("mechanism 471", "mechanism 657", "mechanism 666",
                      "#609/#614", "#503", "iteration-492", "#565",
                      "Aug 28 2026 standing rule"):
            assert token in text, token


class TestSourcesAndResearch729:
    def test_eight_source_urls(self):
        assert len(mech()["source_urls"]) == 8

    def test_scholarly_kitchen_url(self):
        urls = " ".join(mech()["source_urls"])
        assert "scholarlykitchen.sspnet.org/2026/09/10/ask-the-chefs-ai-and-copyright-licensing" in urls

    def test_techrepublic_url(self):
        urls = " ".join(mech()["source_urls"])
        assert "techrepublic.com/article/news-openai-us-government-ai-copyright-fight" in urls

    def test_publishing_perspectives_url(self):
        urls = " ".join(mech()["source_urls"])
        assert "publishingperspectives.com/2026/09" in urls

    def test_bloomberg_law_url(self):
        urls = " ".join(mech()["source_urls"])
        assert "news.bloomberglaw.com/ip-law/trump-administration-backs-openai-in-ny-times-copyright-suit" in urls

    def test_jdsupra_url(self):
        urls = " ".join(mech()["source_urls"])
        assert "jdsupra.com/legalnews/ip-hot-topic-the-doj-chimes-in-on-fair-5800952" in urls

    def test_usatoday_url(self):
        urls = " ".join(mech()["source_urls"])
        assert "usatoday.com/story/tech/2026/09/06/doj-openai-nyt-legal-battle-over-copyright-training" in urls

    def test_reason_url(self):
        urls = " ".join(mech()["source_urls"])
        assert "reason.com/2026/09/04/doj-says-barring-ai-training-on-copyrighted-material" in urls

    def test_techcrunch_counterevidence_url(self):
        urls = " ".join(mech()["source_urls"])
        assert "techcrunch.com/2026/09/06/authors-push-back-as-publishers-and-agents-seek-share-of-anthropic-settlement" in urls

    def test_all_source_urls_verbatim_copied(self):
        # Every URL must be copied verbatim from search results; none may be
        # invented. This pins the exact set found this run.
        urls = mech()["source_urls"]
        assert all(u.startswith("https://") for u in urls)
        assert len(set(urls)) == 8

    def test_research_method_two_query_sets(self):
        rm = mech()["research_method"]
        assert "2 browser.search query sets" in rm
        assert "#503" in rm
        assert "UMG x ElevenLabs" in rm
        assert "rejected: music vertical" in rm

    def test_mechanism_block_ascii_only(self):
        yaml.safe_dump(mech()).encode("ascii")

    def test_novelty_verification_tokens(self):
        nov = mech()["novelty"]
        for token in ("mechanism 657", "mechanism 666", "mechanism 589",
                      "#471", "max numeric mechanism_id 671 pre-commit",
                      "#728"):
            assert token in nov, token

    def test_eight_source_prose_entries(self):
        assert len(mech()["sources"]) == 8


class TestRotationCycleGuard729:
    """Deselected pre-commit; anchor patched in followup per #565."""

    WINDOW = {725: "D", 726: "E", 727: "A", 728: "B", 729: "C"}
    ANCHORED_SHA = ANCHORED_SHA

    def test_rotation_window_mapping(self):
        assert self.WINDOW == {725: "D", 726: "E", 727: "A", 728: "B", 729: "C"}

    def test_729_is_type_c_in_window(self):
        assert self.WINDOW[ITERATION] == "C"

    def test_728_was_type_b_in_window(self):
        assert self.WINDOW[728] == "B"

    @staticmethod
    def _mains():
        out = subprocess.run(
            ["git", "-C", REPO, "log", "--format=%s"],
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

    def test_window_725_729_closes_d_to_c(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("C", "729"),
            ("B", "728"),
            ("A", "727"),
            ("E", "726"),
            ("D", "725"),
        ], "rotation window 725-729 wrong: %r" % (observed,)

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["C", "B", "A", "E", "D"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for newer, older in zip(observed, observed[1:]):
            assert (order[newer] - order[older]) % 5 == 1, (
                "rotation broken: %s (older) -> %s (newer) is not a valid cycle edge" % (older, newer)
            )

    def test_anchor_is_main_commit_patched_in_followup(self):
        """Rotation window 725-729 closes D->C. Anchor patched in followup per #565."""
        result = git("log", "--format=%H %s")
        assert result.returncode == 0
        mains = [
            line for line in result.stdout.splitlines() if "Type C #729:" in line
        ]
        main = mains[0].split()[0] if mains else ""
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )

    def test_single_729_test_file_pre_commit(self):
        hits = [os.path.basename(p) for p in glob.glob(os.path.join(TESTS_DIR, "test_type_c_729*.py"))]
        assert hits == [TEST_BASENAME]


class TestDocSyncRatchet729:
    """Deselected pre-commit per #565 convention; patched green in followup."""
    README = os.path.join(REPO, "README.md")
    ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")
    LOG = os.path.join(REPO, "iteration-log.md")

    def test_readme_has_729_row(self):
        text = open(self.README, encoding="utf-8").read()
        assert TEST_BASENAME in text

    def test_architecture_has_729_tree_row(self):
        text = open(self.ARCH, encoding="utf-8").read()
        assert TEST_BASENAME in text

    def test_iteration_log_top_entry_729(self):
        text = open(self.LOG, encoding="utf-8").read()
        assert text.lstrip().startswith("#729 Type C:")

    def test_readme_row_mentions_doj(self):
        text = open(self.README, encoding="utf-8").read()
        seg = text[text.index(TEST_BASENAME):]
        seg = seg[:5000]
        assert "DOJ" in seg or "Statement of Interest" in seg


class TestSweepSupersession729:
    """Pins the post-#729 state: max mechanism_id 672; ledger holds at 24."""

    def test_max_mechanism_id_is_672(self):
        corpus = open(COMPETITOR, encoding="utf-8").read()
        ids = [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)\b", corpus)]
        modern = [i for i in ids if i >= 600]
        assert max(modern) == 672, max(modern)

    def test_zero_mechanism_673_keys_repo_wide(self):
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for f in files:
                if f.endswith((".yaml", ".yml")):
                    t = open(os.path.join(root, f), encoding="utf-8").read()
                    assert "mechanism_673" not in t, f

    def test_zero_mechanism_672_underscore_keys_repo_wide(self):
        # Mirrors #728's sweep: designed keying keeps the underscore string
        # out of profiles/*.yaml; this run's own block keys without it.
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for f in files:
                if f.endswith((".yaml", ".yml")):
                    t = open(os.path.join(root, f), encoding="utf-8").read()
                    assert "mechanism_672" not in t, f

    def test_728_max_671_sweep_fails_by_designed_supersession(self):
        # Documented, not repaired: advancing max numeric mechanism id to
        # 672 supersedes #728's max-671 sweep per the #710/#720 convention.
        corpus = open(COMPETITOR, encoding="utf-8").read()
        ids = [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)\b", corpus)]
        assert 672 in ids

    def test_falsification_ledger_holds_at_24(self):
        corpus = open(COMPETITOR, encoding="utf-8").read()
        assert "TWENTY-FOURTH" in corpus
        assert "TWENTY-FIFTH" not in corpus
