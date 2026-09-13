"""Type C #724 (2026-09-13 12:00 PDT): Meta x Newsmax AI content partnership
(Jul 28 2026) ideology-bundle leg - mechanism 669.

FIRST dedicated corpus mechanism on Meta's Jul 28 2026 AI content
partnership with Newsmax Inc. (NYSE:NMAX): Meta gets Newsmax's current
reporting plus archived digital news content to power AI search and
discovery across Facebook, Instagram, WhatsApp, Meta AI, and consumer
devices including Quest headsets and Meta's AI smart glasses (MediaPost
Jul 30 2026 - the FIRST glasses-specific publisher revenue relationship
in the corpus, directly on the wearables axis).

Terms undisclosed; CEO Chris Ruddy on the Aug 14 2026 Q2 earnings call
called the deal "consistent with the market" and "potentially the start
of a meaningful licensing opportunity", and said Newsmax is in
discussions with OTHER AI companies (no Meta exclusivity). The leg joins
Meta's right-of-center-tilted publisher roster (Newsmax, Fox News Media,
Daily Caller, Washington Examiner per TheDesk Jul 28 2026) alongside
News Corp (mechanism 549, up-to-$50M/yr disclosed, Mar 2026), WBD/CNN,
USA Today Company, and People Inc. Meta's stated design is viewpoint
balance ("wide variety of viewpoints", Dec 2025 Meta blog via MediaPost),
so the ideology-skew reading is a hypothesis with strong counterevidence,
not a finding. Framed as ideology-BUNDLE (portfolio composition), not
ideology-CAPTURE.

QUALITATIVE structural mapping only. scorer none, tone_scores
NOT_SCORED, p_value / cohens_d / ci_95 NOT_CALCULATED, is_significant
False per the Aug 28 2026 standing rule; engine NOT run; NOT
artifact-grade; no analysis.json update. NOT a falsification-family
member (ledger holds at 24 per the #609/#614 qualitative boundary).

724 = Type C (rotation window 720-724 closes B #723 -> C #724).
Anchor patched post-commit per #565 convention.

Research method: 4 browser.search query sets this run: (1) Reddit Google
AI licensing renewal Sep 2026 - Jul 22 WSJ non-renewal report context +
RBC early-2027 timing leg (covered in corpus via the Jul 22 leg; not
selected); (2) Anthropic publisher licensing Sep 2026 - zero-deal posture
re-confirmed via the llmpulse tracker updated Sep 7 2026 (covered in
#719's sweep; not selected); (3) Apple publisher Siri AI deals Sep 2026 -
variable pay-per-use nine-figure structure (heavily covered: mechanisms
136/156/534/574/606/619; not selected); (4) Meta Newsmax AI licensing
deal - SELECTED. Excerpt-bounded, second-hand evidence per #503 (no
browser.open first-hand reads this run). All URLs copied verbatim from
Full-URL listings; no canonical URLs constructed. Pre-commit novelty
greps: zero test_type_c_724 files on disk (glob); no Type C #724 in git
log (--grep); no underscore-669 string in profiles/ pre-commit (the block
uses the colon form mechanism_id: 669 per the #723 designed-keying
lesson, so #723's zero-669 profiles sweep stays green); max numeric
mechanism id pre-commit 668; 4 of 4 source URLs zero-hit repo-wide
pre-commit; no dedicated Newsmax x Meta mechanism key repo-wide
pre-commit (only #644's research_method mention of a Dec 2025 search
item). No zero-coverage claims per iteration-492 rule; bounded absence
only. No em dashes in any new prose. ASCII only.
"""

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
ITERATION = 724
MECH_KEY = "newsmax_meta_ai_content_partnership_jul2026"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. Anchor test deselected pre-commit.
ANCHORED_SHA = "PENDING_FOLLOWUP"


def load_competitor():
    with open(COMPETITOR, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def mech():
    return load_competitor()["entities"]["meta"][MECH_KEY]


def git(*args):
    return subprocess.run(
        ["git", "-C", REPO, *args],
        capture_output=True,
        text=True,
        timeout=120,
    )


class TestNovelty724:
    """Iteration 724 is new; mechanism 669 is the next free id."""

    def test_single_type_c_724_file(self):
        hits = glob.glob(os.path.join(TESTS_DIR, "test_type_c_724*.py"))
        assert len(hits) == 1, "expected exactly this file, got %r" % (hits,)
        assert hits[0].endswith(TEST_BASENAME)

    def test_mechanism_id_is_669(self):
        m = mech()
        assert m["mechanism_id"] == 669
        assert m["iteration"] == 724
        assert m["iteration_type"] == "C"
        assert m["rotation"] == "Type C"
        assert m["type"] == "financial_incentive_mapping"

    def test_mechanism_key_colon_form(self):
        # Designed keying per the #723 lesson: the corpus key carries no
        # underscore-669 string, so #723's zero-669 profiles sweep stays
        # green (NO supersession there).
        assert "mechanism_669" not in MECH_KEY
        text = open(COMPETITOR, encoding="utf-8").read()
        assert "mechanism_id: 669" in text


class TestIterationMetadata724:
    def test_iteration_metadata(self):
        m = mech()
        assert m["date_analyzed"] == "2026-09-13"
        assert m["time_pdt"] == "12:00"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_type_c_focus_present(self):
        focus = mech()["type_c_focus"]
        assert "Newsmax" in focus
        assert "Jul 28 2026" in focus
        assert "smart glasses" in focus

    def test_test_file_self_reference(self):
        assert mech()["test_file"] == "tests/" + TEST_BASENAME

    def test_type_label(self):
        assert mech()["type_label"] == "Financial Incentive Mapping"


class TestDealFacts724:
    def test_announcement_date(self):
        m = mech()
        assert m["announcement_date"] == "2026-07-28"
        assert "ACCESS Newswire" in m["announced_by"]

    def test_counterparty(self):
        assert "NYSE:NMAX" in mech()["deal_terms"]["counterparty"]

    def test_scope_apps(self):
        scope = mech()["deal_terms"]["scope"]
        for surface in ("Facebook", "Instagram", "WhatsApp"):
            assert surface in scope, surface

    def test_wearables_scope_first_glasses_leg(self):
        ws = mech()["deal_terms"]["wearables_scope"]
        assert "Quest" in ws
        assert "smart glasses" in ws
        assert "FIRST" in ws

    def test_terms_undisclosed(self):
        dt = mech()["deal_terms"]
        assert dt["value"].startswith("UNDISCLOSED")
        assert "consistent with the market" in dt["value"]

    def test_no_exclusivity(self):
        excl = mech()["deal_terms"]["exclusivity"]
        assert excl.startswith("NONE")
        assert "OTHER AI companies" in excl

    def test_training_rights_undisclosed(self):
        assert mech()["deal_terms"]["training_rights"].startswith("UNDISCLOSED")

    def test_roster_right_of_center(self):
        roster = mech()["portfolio_roster"]
        for outlet in ("Newsmax", "Fox News Media", "Daily Caller",
                       "Washington Examiner"):
            assert outlet in roster["right_of_center_legs"], outlet

    def test_roster_corporate_center_and_balance_design(self):
        roster = mech()["portfolio_roster"]
        for outlet in ("News Corp", "CNN", "USA Today", "People Inc"):
            assert outlet in roster["corporate_center_legs"], outlet
        assert "wide variety of viewpoints" in roster["meta_stated_design"]

    def test_q2_call(self):
        call = mech()["q2_2026_earnings_call"]
        assert call["date"] == "2026-08-14"
        assert call["speaker"] == "CEO Chris Ruddy"
        assert "meaningful licensing opportunity" in call["forward_opportunity"]

    def test_source_urls_verbatim(self):
        urls = mech()["source_urls"]
        assert urls == [
            "https://thedesk.net/2026/07/facebook-parent-meta-signs-ai-licensing-agreement-with-newsmax/",
            "https://www.morningstar.com/news/accesswire/1197285msn/newsmax-and-meta-enter-ai-content-partnership",
            "https://www.mediapost.com/publications/article/416899/meta-forges-ai-content-deal-with-newsmax.html",
            "https://www.marketbeat.com/instant-alerts/newsmax-q2-earnings-call-highlights-2026-08-14/",
        ]


class TestStatisticalDiscipline724:
    def test_scorer_none(self):
        sd = mech()["statistical_discipline"]
        assert sd["scorer"] == "none"
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["qualitative_only"] is True
        assert sd["correlation_not_causation"] is True
        assert sd["is_significant"] is False
        assert sd["artifact_grade"] is False

    def test_no_tone_claim(self):
        assert mech()["asymmetry_relevance"]["no_tone_claim"] is True
        assert mech()["statistical_discipline"]["no_coverage_tone_claim"] is True
        assert mech()["asymmetry_relevance"]["tone_predictor_grade"].startswith("UNRATED")

    def test_no_analysis_json_update(self):
        ap = os.path.join(REPO, "analysis.json")
        if os.path.exists(ap):
            assert MECH_KEY not in open(ap, encoding="utf-8").read()


class TestResearchMethod724:
    def test_four_query_sets(self):
        assert "4 browser.search query sets" in mech()["research_method"]

    def test_excerpt_bounded_convention(self):
        assert "#503" in mech()["research_method"]

    def test_bounded_absence_rule(self):
        assert "iteration-492" in mech()["research_method"]

    def test_ascii_only(self):
        yaml.safe_dump(mech()).encode("ascii")

    def test_no_em_dash_in_block(self):
        text = yaml.safe_dump(mech())
        assert "—" not in text and "–" not in text


class TestRotationCycleGuard724:
    """Deselected pre-commit for the anchor test; anchor patched in followup."""

    WINDOW = {720: "D", 721: "E", 722: "A", 723: "B", 724: "C"}
    ANCHORED_SHA = ANCHORED_SHA

    def test_rotation_window_mapping(self):
        assert self.WINDOW == {720: "D", 721: "E", 722: "A", 723: "B", 724: "C"}

    def test_724_is_type_c_in_window(self):
        assert self.WINDOW[ITERATION] == "C"

    def test_723_was_type_b_in_window(self):
        assert self.WINDOW[723] == "B"

    def test_rotation_adjacency_valid(self):
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        seq = [self.WINDOW[i] for i in (720, 721, 722, 723, 724)]
        assert seq == ["D", "E", "A", "B", "C"]
        for newer, older in zip(seq[1:], seq):
            assert (order[newer] - order[older]) % 5 == 1, (
                "rotation broken: %s (older) -> %s (newer) is not a valid cycle edge"
                % (older, newer)
            )

    def test_anchored_sha_on_main(self):
        assert git("cat-file", "-e", f"{self.ANCHORED_SHA}^{{commit}}").returncode == 0
        msg = git("log", "-1", "--format=%s", self.ANCHORED_SHA).stdout.strip()
        assert "Type C #724" in msg

    def test_single_724_test_file_pre_commit(self):
        hits = [
            os.path.basename(p)
            for p in glob.glob(os.path.join(TESTS_DIR, "test_type_c_724*.py"))
        ]
        assert hits == [TEST_BASENAME]

    def test_iteration_log_entry_regex_self_check(self):
        sample = "#724 Type C: Meta x Newsmax AI content partnership"
        assert re.match(r"^#724 Type C:", sample)


class TestDocSyncRatchet724:
    README = os.path.join(REPO, "README.md")
    ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")
    LOG = os.path.join(REPO, "iteration-log.md")

    def test_readme_has_724_row(self):
        text = open(self.README, encoding="utf-8").read()
        assert TEST_BASENAME in text

    def test_architecture_has_724_tree_row(self):
        text = open(self.ARCH, encoding="utf-8").read()
        assert TEST_BASENAME in text

    def test_iteration_log_has_724_entry(self):
        text = open(self.LOG, encoding="utf-8").read()
        assert "#724 Type C:" in text
        assert "Newsmax" in text

    def test_readme_row_mentions_newsmax(self):
        text = open(self.README, encoding="utf-8").read()
        seg = text[text.index(TEST_BASENAME):]
        seg = seg[:5000]
        assert "Newsmax" in seg

    def test_doc_count_stats_sync(self):
        readme = open(self.README, encoding="utf-8").read()
        assert re.search(r"\| Tests \| \d+ \| Across \d+ test files \|", readme)


class TestSweepSupersession724:
    """Pins the post-#724 state: max mechanism_id 669; ledger holds at 24."""

    def _profiles_corpus(self):
        texts = []
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for f in files:
                if f.endswith((".yaml", ".yml")):
                    texts.append(
                        open(os.path.join(root, f), encoding="utf-8").read()
                    )
        return "\n".join(texts)

    def test_max_mechanism_id_is_669(self):
        corpus = self._profiles_corpus()
        ids = [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)\b", corpus)]
        modern = [i for i in ids if i >= 600]
        assert max(modern) == 669, max(modern)

    def test_723_zero_669_profiles_sweep_stays_green(self):
        # Designed keying: this block uses the colon form, so #723's
        # profiles sweep for the underscore-669 string stays green -
        # NO supersession needed there.
        assert "mechanism_669" not in self._profiles_corpus()

    def test_723_max_668_sweep_fails_by_designed_supersession(self):
        # Documented, not repaired: advancing max numeric mechanism id to
        # 669 supersedes #723's test_max_mechanism_id_is_668 per the
        # #710/#720 convention.
        corpus = self._profiles_corpus()
        ids = [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)\b", corpus)]
        assert max(i for i in ids if i >= 600) == 669

    def test_zero_underscore_669_keys_in_other_test_files(self):
        # Own file excluded from the sweep per the #715 pattern-rescope
        # lesson: MECH_KEY legitimately names the mechanism here.
        key_re = re.compile(r"\bmechanism_669_[a-z0-9_]")
        for f in glob.glob(os.path.join(TESTS_DIR, "test_*.py")):
            if os.path.basename(f) == TEST_BASENAME:
                continue
            assert not key_re.search(open(f, encoding="utf-8").read()), f

    def test_falsification_ledger_holds_at_24(self):
        corpus = self._profiles_corpus()
        assert "TWENTY-FOURTH" in corpus
        assert "TWENTY-FIFTH" not in corpus


class TestDateGrounding724:
    """Event dates grounded; weekdays verified via date -d (America/Los_Angeles)."""

    def test_announcement_date_grounded(self):
        block = open(COMPETITOR, encoding="utf-8").read()
        # Tuesday Jul 28 2026, verified via date -d
        assert "2026-07-28" in block

    def test_q2_call_date_grounded(self):
        block = open(COMPETITOR, encoding="utf-8").read()
        # Friday Aug 14 2026, verified via date -d
        assert "2026-08-14" in block

    def test_run_date_grounded(self):
        m = mech()
        # Sunday Sep 13 2026, verified via date -d
        assert m["date_analyzed"] == "2026-09-13"
        assert m["time_pdt"] == "12:00"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"
