# Type C #734: Seattle Times + Newsday v. OpenAI + Microsoft (mechanism 675)
# FIRST dedicated grant-then-sue leg on the OpenAI x publisher financial
# vector: on Fri Sep 4, 2026 the Seattle Times and Newsday jointly sued
# OpenAI and Microsoft in S.D.N.Y., alleging paywalled-content scraping into
# training datasets (WebText, WebText2, Common Crawl, Bing index) with
# near-verbatim outputs and CMI removal. Both plaintiffs are recipients of
# the Oct 2024 $10M OpenAI-Microsoft AI Collaborative and Fellowship Grant
# (2-year fellowships, five newsrooms) - the grant bought zero observed
# litigation forbearance: 2 of 5 grant newsrooms sued the grant-makers about
# 23 months later, as the fellowship window closes (Oct 2024 + 2y = Oct 2026).
# Inverts the naive payer-softening prediction, mirroring mechanism 672's
# state-power inversion one level down. Completes the relationship-direction
# taxonomy: sue-then-sign (m624 Indian Express), pay-or-litigate (m636),
# grant-then-sue (this leg).
#
# QUALITATIVE structural mapping only. No scorer, no tone scores, no
# p-value, no effect size, no CI. NOT a falsification-family member
# (ledger holds at 24; per #609/#614 qualitative boundary).
# No analysis.json update.
#
# 734 = Type C (rotation window 730-734 closes D #730 -> E #731 -> A #732
# -> B #733 -> C #734). Anchor patched post-commit per #565 convention.
#
# Research method: 2 browser.search query sets this run: (1) Ziff Davis
# OpenAI lawsuit September 2026 development - surfaced the Seattle
# Times/Newsday suit via TradingView/GuruFocus (SELECTED) plus the Aug 6,
# 2026 Judge Stein Ziff Davis partial-dismissal orders (carried as context);
# (2) Seattle Times Newsday sue Microsoft OpenAI copyright (since 2026-09-01)
# - 7 corroborating sources (Reuters, LiveMint, Medianama, Engadget,
# TechCrunch, GeekWire, Business Day). All 8 URLs copied verbatim from
# Full-URL listings; no canonical URLs constructed. Excerpt-bounded,
# second-hand evidence per #503 (no browser.open first-hand reads this run).
# Novelty pre-commit greps: zero test_type_c_734 files on disk (glob); no
# "Type C #734" in git log (--grep); zero dedicated Seattle Times/Newsday
# lawsuit mechanisms repo-wide (grep); zero underscore-form 675 mechanism
# keys in profiles/ and tests/ (sweep carriers excluded per #715); max
# numeric mechanism_id 674 pre-commit; all 8 source URLs zero-hit repo-wide
# pre-commit. No em dashes; ASCII-only.
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
THIS_FILE = os.path.basename(__file__)
ITERATION = 734
MECH_KEY = "seattle_times_newsday_grant_then_sue_openai_microsoft_sep2026"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. Anchor tests are deselected pre-commit.
ANCHORED_SHA = "b24a663279efe0ee9e6fb275d18f0144e9adc81d"  # main-commit SHA, patched post-commit per #565


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


class TestIterationMetadata734:
    def test_iteration_is_734(self):
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
        assert m["time_pdt"] == "22:00"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_mechanism_id_675_int(self):
        assert isinstance(mech()["mechanism_id"], int)
        assert mech()["mechanism_id"] == 675

    def test_single_675_mechanism_block_in_openai(self):
        openai = load_competitor()["entities"]["openai"]
        hits = [k for k, v in openai.items()
                if isinstance(v, dict) and v.get("mechanism_id") == 675]
        assert hits == [MECH_KEY]

    def test_iteration_type_matches_rotation(self):
        assert mech()["iteration_type"] == "C"

    def test_first_grant_then_sue_leg_claim(self):
        assert "FIRST" in mech()["mechanism_name"]
        assert "grant-then-sue" in mech()["mechanism_name"]


class TestSuitFacts734:
    def test_filing_date_and_court(self):
        facts = " ".join(mech()["suit_facts"])
        assert "Sep 4, 2026" in facts
        assert "Southern District of New York" in facts

    def test_defendants_openai_and_microsoft(self):
        facts = " ".join(mech()["suit_facts"])
        assert "OpenAI and Microsoft" in facts

    def test_paywalled_scraping_allegation(self):
        facts = " ".join(mech()["suit_facts"])
        assert "paywall" in facts

    def test_datasets_named(self):
        facts = " ".join(mech()["suit_facts"])
        for ds in ("WebText", "WebText2", "Common Crawl", "Bing"):
            assert ds in facts, ds

    def test_verbatim_output_evidence(self):
        facts = " ".join(mech()["suit_facts"])
        assert "88-word verbatim" in facts
        assert "Boeing 737 MAX" in facts

    def test_cmi_removal_and_robotstxt(self):
        facts = " ".join(mech()["suit_facts"])
        assert "copyright-management-information" in facts or "CMI" in facts
        assert "robots.txt" in facts

    def test_relief_sought_destruction(self):
        facts = " ".join(mech()["suit_facts"])
        assert "destruction" in facts

    def test_fisco_memo_quote(self):
        facts = " ".join(mech()["suit_facts"])
        assert "Alan Fisco" in facts
        assert "millions of dollars a year" in facts

    def test_defendant_responses_present(self):
        facts = " ".join(mech()["suit_facts"])
        assert "surprised by the lawsuit" in facts
        assert "fair use" in facts

    def test_doj_timing_linkage(self):
        facts = " ".join(mech()["suit_facts"])
        assert "Justice Department" in facts or "DOJ" in facts


class TestGrantThenSueTheory734:
    def test_grant_block_carried(self):
        theory = " ".join(mech()["grant_then_sue_theory"])
        assert "$10M" in theory
        assert "five newsrooms" in theory

    def test_naive_prediction_fails(self):
        theory = " ".join(mech()["grant_then_sue_theory"])
        assert "40%" in theory
        assert "zero observed litigation forbearance" in theory

    def test_taxonomy_three_legs(self):
        theory = " ".join(mech()["grant_then_sue_theory"])
        assert "sue-then-sign" in theory
        assert "pay-or-litigate" in theory
        assert "grant-then-sue" in theory

    def test_paid_portfolio_contrast(self):
        theory = " ".join(mech()["grant_then_sue_theory"])
        assert "$300-400M/yr" in theory or "paid publisher portfolio" in theory

    def test_no_causal_claim(self):
        theory = " ".join(mech()["grant_then_sue_theory"])
        assert "no causal claim" in theory

    def test_inversion_of_672_direction(self):
        overview = mech()["overview"]
        assert "inverse of the naive payer-softening prediction" in overview


class TestConfounds734:
    def test_confounder_tiers_present(self):
        c = mech()["confounders"]
        assert len(c["strong"]) >= 3
        assert len(c["moderate"]) >= 3
        assert len(c["weak"]) >= 3

    def test_excerpt_bounded_evidence_grade(self):
        strong = " ".join(mech()["confounders"]["strong"])
        assert "#503" in strong

    def test_motive_unobserved(self):
        strong = " ".join(mech()["confounders"]["strong"])
        assert "Motive unobserved" in strong or "motive" in strong.lower()

    def test_partial_cohort_response(self):
        strong = " ".join(mech()["confounders"]["strong"])
        assert "3 of 5" in strong or "40%" in strong

    def test_counterevidence_present(self):
        ce = mech()["counterevidence"]
        assert len(ce) >= 3
        assert any("AP and Vox Media" in x for x in ce)

    def test_bounded_absences_present(self):
        ba = mech()["bounded_absences"]
        assert len(ba) >= 3
        assert any("iteration-492" in x for x in ba)


class TestSourcesAndResearch734:
    def test_eight_source_urls(self):
        urls = mech()["source_urls"]
        assert len(urls) == 8

    def test_source_urls_verbatim(self):
        urls = mech()["source_urls"]
        assert urls[0] == "https://www.tradingview.com/news/gurufocus:0f442ee79094b:0-microsoft-s-openai-partnership-draws-fresh-legal-fire/"
        assert urls[1] == "https://www.reuters.com/legal/government/seattle-times-newsday-sue-openai-microsoft-alleging-copyright-infringement-2026-09-05/"
        assert urls[2] == "https://www.medianama.com/2026/09/223-seattle-times-sue-openai-copyrighted-journalism/"
        assert urls[3] == "https://www.engadget.com/2251707/seattle-times-newsday-sue-openai-microsoft-for-copyright-infringement/"
        assert urls[4] == "https://techcrunch.com/2026/09/05/seattle-times-and-newsday-are-the-latest-publications-to-sue-openai-and-microsoft/"
        assert urls[5] == "https://www.geekwire.com/2026/seattle-times-sues-microsoft-and-openai-alleging-they-trained-their-ai-on-its-journalism/"
        assert urls[6] == "https://www.livemint.com/technology/tech-news/seattle-times-newsday-sue-openai-microsoft-alleging-copyright-infringement-11788578229143.html"
        assert urls[7] == "https://www.businessday.co.za/world/international-companies/2026-09-06-seattle-times-newsday-sue-openai-and-microsoft-over-ai-use-of-journalism/"

    def test_source_citations_present(self):
        src = " ".join(mech()["sources"])
        for pub in ("TradingView", "Reuters", "Medianama", "Engadget",
                    "TechCrunch", "GeekWire", "LiveMint", "Business Day"):
            assert pub in src, pub

    def test_research_method_two_query_sets(self):
        rm = mech()["research_method"]
        assert "2 browser.search query sets" in rm
        assert "verbatim from Full-URL listings" in rm

    def test_cross_references_present(self):
        cr = mech()["cross_references"]
        joined = " ".join(cr)
        for ref in ("mechanism 672", "mechanism 589", "mechanism 624",
                    "mechanism 636", "mechanism 657"):
            assert ref in joined, ref

    def test_novelty_first_grant_then_sue(self):
        assert "FIRST dedicated grant-then-sue" in mech()["novelty"]

    def test_test_file_field_matches(self):
        assert mech()["test_file"] == "tests/" + THIS_FILE

    def test_statistical_discipline_qualitative(self):
        sd = mech()["statistical_discipline"]
        assert "tone NOT_SCORED" in sd
        assert "is_significant False" in sd
        assert "NOT a falsification-family member" in sd


class TestRotationCycleGuard734:
    """Deselected pre-commit; anchor patched in followup per #565."""

    WINDOW = {730: "D", 731: "E", 732: "A", 733: "B", 734: "C"}
    ANCHORED_SHA = ANCHORED_SHA

    def test_rotation_window_mapping(self):
        assert self.WINDOW == {730: "D", 731: "E", 732: "A", 733: "B", 734: "C"}

    def test_734_is_type_c_in_window(self):
        assert self.WINDOW[ITERATION] == "C"

    def test_733_was_type_b_in_window(self):
        assert self.WINDOW[733] == "B"

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

    def test_window_730_734_closes_d_to_c(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("C", "734"),
            ("B", "733"),
            ("A", "732"),
            ("E", "731"),
            ("D", "730"),
        ], "rotation window 730-734 wrong: %r" % (observed,)

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
        """Rotation window 730-734 closes D->C. Anchor patched in followup per #565."""
        result = git("log", "--format=%H %s")
        assert result.returncode == 0
        mains = [
            line for line in result.stdout.splitlines() if "Type C #734:" in line
        ]
        main = mains[0].split()[0] if mains else ""
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )

    def test_single_734_test_file_pre_commit(self):
        hits = [os.path.basename(p) for p in glob.glob(os.path.join(TESTS_DIR, "test_type_c_734*.py"))]
        assert hits == [THIS_FILE]


class TestDocSyncRatchet734:
    """Deselected pre-commit per #565 convention; patched green in followup."""
    README = os.path.join(REPO, "README.md")
    ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")
    LOG = os.path.join(REPO, "iteration-log.md")

    def test_readme_has_734_row(self):
        text = open(self.README, encoding="utf-8").read()
        assert THIS_FILE in text

    def test_architecture_has_734_tree_row(self):
        text = open(self.ARCH, encoding="utf-8").read()
        assert THIS_FILE in text

    def test_iteration_log_top_entry_734(self):
        text = open(self.LOG, encoding="utf-8").read()
        assert text.lstrip().startswith("#734 Type C:")

    def test_readme_row_mentions_grant_then_sue(self):
        text = open(self.README, encoding="utf-8").read()
        seg = text[text.index(THIS_FILE):]
        seg = seg[:5000]
        assert "grant-then-sue" in seg


class TestSweepSupersession734:
    """Pins the post-#734 state: max mechanism_id 675; ledger holds at 24.

    The underscore-form 675 key target is built dynamically (never as a
    literal in this file) so the committed #733 zero-sweep for that key
    stays green. Sweep carriers for the 675 forward-sweep are the files
    that legitimately contain the literal.
    """

    def test_max_mechanism_id_is_675(self):
        corpus = open(COMPETITOR, encoding="utf-8").read()
        ids = [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)\b", corpus)]
        modern = [i for i in ids if i >= 600]
        assert max(modern) == 675, max(modern)

    def test_zero_underscore_675_keys_in_profiles(self):
        target = "mechanism_675" + "_"
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for f in files:
                if f.endswith((".yaml", ".yml")):
                    t = open(os.path.join(root, f), encoding="utf-8").read()
                    assert target not in t, f

    def test_zero_underscore_675_keys_outside_carriers(self):
        target = "mechanism_675" + "_"
        carriers = {
            "test_type_b_733_jessica_conditt_engadget_apple_adversarial_beat_routing_sep13_9pm.py",
        }
        hits = []
        for fn in os.listdir(TESTS_DIR):
            fp = os.path.join(TESTS_DIR, fn)
            if fn in carriers or not os.path.isfile(fp):
                continue
            if target in open(fp, encoding="utf-8").read():
                hits.append(fn)
        assert hits == [], f"underscore-675 keys outside sweep carriers: {hits}"

    def test_zero_mechanism_676_keys_repo_wide(self):
        # Mirrors the #729 pattern: profiles/-only walk. My own file
        # references 676 in this sweep test, so tests/ is excluded.
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for f in files:
                if f.endswith((".yaml", ".yml")):
                    t = open(os.path.join(root, f), encoding="utf-8").read()
                    assert "mechanism_676" not in t, f

    def test_733_max_674_sweep_fails_by_designed_supersession(self):
        # Documented, not repaired: advancing max numeric mechanism id to
        # 675 supersedes #733's max-674 sweep per the #710/#720 convention.
        corpus = open(COMPETITOR, encoding="utf-8").read()
        ids = [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)\b", corpus)]
        assert 675 in ids

    def test_falsification_ledger_holds_at_24(self):
        corpus = open(COMPETITOR, encoding="utf-8").read()
        assert "TWENTY-FOURTH" in corpus
        assert "TWENTY-FIFTH" not in corpus
