# Type C #704: ANI v. OpenAI India Litigation Leg (mechanism 657)
# FIRST dedicated litigation-type financial-incentive mechanism on the
# India-market contest leg: Asian News International's Delhi High Court
# copyright suit against OpenAI (Nov 2024 filing; Jul 24 2026 interim-relief
# denial; Sep 8 2026 appeal to the Division Bench; listed Sep 14 2026).
#
# The financial-incentive link is Medianama's BATNA-pricing insight (Sep 9
# 2026): the Jul 24 order is the only Indian ruling on whether AI companies
# may train on copyrighted news, and it is "the number every Indian publisher
# is quietly working from in licensing talks" - it sets the value of the
# alternative to a licence. The litigation leg thus prices OpenAI's licensing
# economics in India: the contest counterpart to the license-the-willing
# attribution deals with BCCL (Sep 7) and the Indian Express Group (Sep 8)
# (mechanism 609, iteration 624). Dual track: license the willing, contest
# the rest.
#
# QUALITATIVE structural mapping only. No scorer, no tone scores, no p-value,
# no effect size, no CI. NOT a falsification-family member (ledger stays at 21
# after #703's TWENTY-FIRST; per #609/#614 qualitative boundary). No
# analysis.json update.
#
# 704 = Type C (rotation window 703-707 opens B #703 -> C #704, then D #705,
# E #706, A #707). Anchor patched post-commit per #565 convention.
#
# Research method: 4 browser.search query sets this run (publisher AI
# licensing deal announced September 2026; Anthropic publisher licensing deal
# partnership; OpenAI BCCL Times of India Economic Times ChatGPT content
# partnership September 2026; ANI OpenAI Delhi High Court appeal copyright
# case, since 2026-09-06) + 1 browser.open first-hand read (FourWeekMBA India
# attribution-deal piece, 147 rendered lines). Litigation facts via verbatim
# search-result excerpts (excerpt-bounded, second-hand per #503); LiveLaw
# paywalled. Query set 1 surfaced the India-blitz already in corpus via
# mechanism 609, redirecting this run to the unmapped ANI litigation leg.
# URLs copied verbatim from Full-URL listings; no canonical URLs constructed.
# Novelty pre-commit greps: zero test_type_c_704 files, no Type C #704 in git
# log, zero mechanism_657 keys, max numeric mechanism id 656, no dedicated
# ANI litigation mechanism. No zero-coverage claims per iteration-492 rule;
# bounded absence only. No em dashes; ASCII-only.
"""Deselected pre-commit: rotation-guard anchor, novelty anchor, and doc-sync
tests per the #565 followup convention; anchors patched in the followup
commit once the main commit SHA is known."""

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
ITERATION = 704
MECH_KEY = "mechanism_657_ani_openai_india_litigation_leg_sep2026"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. Anchor tests are deselected pre-commit.
ANCHORED_SHA = "76ea86ed17ad5eaf79a347a566d9cdc18fc6e450"


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


class TestIterationMetadata704:
    def test_iteration_is_704(self):
        assert mech()["iteration"] == ITERATION

    def test_rotation_is_type_c(self):
        assert mech()["rotation"] == "Type C"

    def test_type_is_financial_incentive_mapping(self):
        assert mech()["type"] == "financial_incentive_mapping"

    def test_type_label(self):
        assert mech()["type_label"] == "Financial Incentive Mapping"

    def test_date_time_job_goal(self):
        m = mech()
        assert m["date_analyzed"] == "2026-09-12"
        assert m["time_pdt"] == "14:00"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_author_kit_with_ray(self):
        assert mech()["author"] == "Kit (with Ray)"

    def test_mechanism_id_657_int(self):
        assert isinstance(mech()["mechanism_id"], int)
        assert mech()["mechanism_id"] == 657

    def test_single_657_mechanism_key(self):
        hits = [k for k in load_competitor()["entities"]["openai"] if k.startswith("mechanism_657")]
        assert hits == [MECH_KEY]


class TestLitigationLegFormalization704:
    def test_counterparty_ani(self):
        assert "Asian News International" in mech()["counterparty"]
        assert "ANI" in mech()["counterparty"]

    def test_case_title(self):
        assert mech()["case_title"] == "ANI MEDIA PVT. LTD. Vs. OPEN AI OPCO LLC"

    def test_forum_delhi_high_court(self):
        assert mech()["forum"] == "Delhi High Court"

    def test_relationship_type_litigation(self):
        assert mech()["relationship_type"] == "litigation"

    def test_timeline_six_entries(self):
        assert len(mech()["litigation_timeline"]) == 6

    def test_timeline_nov2024_filing_first_suit(self):
        joined = "\n".join(mech()["litigation_timeline"])
        assert "Nov 2024" in joined
        assert "first Indian media house" in joined

    def test_timeline_feb2025_interventions(self):
        joined = "\n".join(mech()["litigation_timeline"])
        assert "Feb 2025" in joined
        assert "Indian Express" in joined and "DNPA" in joined
        assert "31-page filing" in joined

    def test_timeline_mar27_2026_reserved(self):
        joined = "\n".join(mech()["litigation_timeline"])
        assert "Mar 27 2026" in joined and "reserves" in joined

    def test_timeline_jul24_2026_denial(self):
        joined = "\n".join(mech()["litigation_timeline"])
        assert "Jul 24 2026" in joined
        assert "Justice Amit Bansal" in joined
        assert "denies" in joined

    def test_timeline_sep8_2026_appeal_bench(self):
        joined = "\n".join(mech()["litigation_timeline"])
        assert "Sep 8 2026" in joined
        assert "Kameshwar Rao" in joined
        assert "Manmeet Pritam Singh Arora" in joined
        assert "did not assemble" in joined
        assert "Chief Justice of Patna High Court" in joined

    def test_timeline_sep14_2026_watch(self):
        joined = "\n".join(mech()["litigation_timeline"])
        assert "Sep 14 2026" in joined
        assert "watch item" in joined

    def test_jul24_holdings_eight(self):
        assert len(mech()["jul24_holdings"]) == 8

    def test_holdings_section52_research_storage_commercial(self):
        joined = "\n".join(mech()["jul24_holdings"])
        assert "52(1)(a)" in joined
        assert "research" in joined
        assert "storing a work electronically" in joined
        assert "commercial character" in joined

    def test_holdings_no_similarity_no_market_harm(self):
        joined = "\n".join(mech()["jul24_holdings"])
        assert "not substantially similar" in joined
        assert "market share" in joined or "subscription revenues" in joined

    def test_holdings_jurisdiction_amicus_dnpa(self):
        joined = "\n".join(mech()["jul24_holdings"])
        assert "territorial jurisdiction" in joined
        assert "Arul George Scaria" in joined
        assert "two-step framework" in joined
        assert "economic sustainability" in joined

    def test_ani_allegations_three(self):
        allegs = mech()["ani_allegations"]
        assert len(allegs) == 3
        joined = "\n".join(allegs)
        assert "verbatim reproduces" in joined
        assert "never occurred" in joined
        assert "commercial gain" in joined

    def test_openai_defenses_four(self):
        defenses = mech()["openai_defenses"]
        assert len(defenses) == 4
        joined = "\n".join(defenses)
        assert "transformative" in joined
        assert "blocklist" in joined

    def test_appeal_arguments_two(self):
        args = mech()["appeal_arguments"]
        assert len(args) == 2
        joined = "\n".join(args)
        assert "publicly available" in joined
        assert "fair-dealing interpretation" in joined

    def test_appeal_status_pending(self):
        assert mech()["appeal_status"].startswith("APPEAL PENDING")
        assert "Sep 14 2026" in mech()["appeal_status"]

    def test_batna_insight_medianama(self):
        insight = mech()["batna_insight"]
        assert "Medianama" in insight
        assert "only Indian ruling" in insight
        assert "alternative to a licence" in insight

    def test_dual_track_license_contest(self):
        dt = mech()["dual_track"]
        assert "License the willing, contest the rest" in dt
        assert "mechanism 609" in dt
        assert "Sep 7" in dt and "Sep 8" in dt


class TestCrossReferences704:
    def _refs(self):
        return "\n".join(mech()["cross_references"])

    def test_mechanism_609_deal_blitz_counterpart(self):
        assert "mechanism 609" in self._refs()
        assert "contest counterpart" in self._refs()

    def test_mechanism_636_pay_or_litigate(self):
        assert "mechanism 636" in self._refs()

    def test_mechanism_519_woo_and_sue(self):
        assert "mechanism 519" in self._refs()

    def test_mechanism_614_bifurcation(self):
        assert "mechanism 614" in self._refs()

    def test_mechanism_509_anthropic_posture_contrast(self):
        refs = self._refs()
        assert "mechanism 509" in refs
        assert "Adweek Aug 26 2026" in refs

    def test_qualitative_boundary_609_614(self):
        assert "#609/#614 qualitative boundary" in self._refs()

    def test_503_second_hand_precedent(self):
        assert "#503" in self._refs()

    def test_iteration_492_bounded_absence(self):
        assert "iteration-492" in self._refs()

    def test_565_followup_convention(self):
        assert "#565" in self._refs()

    def test_aug28_standing_rule(self):
        assert "Aug 28 2026 standing rule" in self._refs()

    def test_cross_reference_count(self):
        assert len(mech()["cross_references"]) == 10


class TestNoveltyAndFirstDedicated704:
    def test_type_c_704_file_unique(self):
        matches = glob.glob(os.path.join(TESTS_DIR, "test_type_c_704*.py"))
        assert len(matches) == 1
        assert matches[0].endswith(TEST_BASENAME)

    def test_no_prior_ani_litigation_mechanism(self):
        keys = []
        for entity, block in load_competitor()["entities"].items():
            if isinstance(block, dict):
                keys += [k for k in block if k.startswith("mechanism_")]
        dups = [k for k in keys if re.search(r"ani.{0,3}openai|openai.{0,3}ani", k, re.I) and k != MECH_KEY]
        assert dups == []

    def test_max_mechanism_id_657(self):
        ids = []
        for entity, block in load_competitor()["entities"].items():
            if isinstance(block, dict):
                for k in block:
                    if k.startswith("mechanism_"):
                        m = re.match(r"mechanism_(\d+)_", k)
                        if m:
                            ids.append(int(m.group(1)))
        assert max(ids) == 657

    def test_novelty_claim_in_block(self):
        assert "FIRST dedicated ANI v. OpenAI litigation-leg mechanism" in mech()["novelty"]

    def test_distinct_from_609(self):
        assert "Distinct from mechanism 609" in mech()["novelty"]

    def test_seven_sources_all_http(self):
        urls = mech()["sources"]
        assert len(urls) == 7
        for u in urls:
            assert u.startswith("http")

    def test_sources_new_to_profiles_and_tests(self):
        # Source URLs are new-to-corpus with one documented exception: the
        # FourWeekMBA India synthesis piece is legitimately shared with
        # mechanism 609's block (the acknowledged parent deal-blitz
        # mechanism) and its #624 test file. Every other URL has exactly
        # one profiles/ hit (this block's sources list) and zero tests/
        # hits. (The iteration-log entry legitimately reprints the URLs
        # post-commit, so the log is out of scope here.)
        profiles_dir = os.path.join(REPO, "profiles")
        shared_624 = "test_type_c_624_openai_india_attribution_deal_blitz_sep09_3am.py"
        for u in mech()["sources"]:
            frag = u.split("//", 1)[1][:40]
            p_hits = []
            for root, _dirs, files in os.walk(profiles_dir):
                for f in files:
                    if f.endswith(".yaml"):
                        p = os.path.join(root, f)
                        text = open(p, encoding="utf-8").read()
                        for i, line in enumerate(text.splitlines()):
                            if frag in line:
                                p_hits.append((p, i + 1, line.strip()[:60]))
            t_hits = []
            for f in glob.glob(os.path.join(TESTS_DIR, "*.py")):
                if frag in open(f, encoding="utf-8").read():
                    t_hits.append(os.path.basename(f))
            if "fourweekmba.com" in frag:
                assert len(p_hits) == 2, f"expected 2 profiles/ hits for shared {frag}, got {p_hits}"
                assert t_hits == [shared_624], f"unexpected tests/ hits for {frag}: {t_hits}"
            else:
                assert len(p_hits) == 1, f"expected exactly one profiles/ hit for {frag}, got {p_hits}"
                assert t_hits == [], f"expected zero tests/ hits for {frag}, got {t_hits}"

    def test_type_c_704_main_commit_unique_and_anchored(self):
        # Runs green only post-main-commit per the #565 followup convention.
        # Deselect pre-commit; the followup patches ANCHORED_SHA to the real
        # main-commit SHA. Novelty was verified pre-commit by shell greps
        # (zero test_type_c_704 files, no #704 in git log, zero
        # mechanism_657 keys in profiles/, max mechanism id 656, no dedicated
        # ANI litigation mechanism, all seven URLs new-to-corpus).
        out = git("log", "--format=%H %s")
        mains = [
            line
            for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type C #704:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type C #704 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        assert sha == TestRotationCycleGuard704.ANCHORED_SHA, (
            "anchor patched in followup per #565 convention"
        )


class TestResearchMethod704:
    def test_four_query_sets_documented(self):
        rm = mech()["research_method"]
        assert rm.count("query set") >= 4 or ("(1)" in rm and "(4)" in rm)

    def test_fourweekmba_first_hand_147_lines(self):
        rm = mech()["research_method"]
        assert "FourWeekMBA" in rm
        assert "147 rendered lines" in rm

    def test_livelaw_paywall_disclosed(self):
        assert "paywalled" in mech()["research_method"]

    def test_second_hand_bounded_per_503(self):
        rm = mech()["research_method"]
        assert "second-hand" in rm
        assert "#503" in rm

    def test_verbatim_urls_no_invented(self):
        rm = mech()["research_method"]
        assert "verbatim" in rm
        assert "no canonical URLs invented" in rm

    def test_ani_query_set_since_filter(self):
        assert "since 2026-09-06" in mech()["research_method"]

    def test_ascii_only(self):
        raw = open(COMPETITOR, "rb").read()
        i = raw.find(b"mechanism_657_ani_openai")
        j = raw.find(b"  anthropic:", i)
        raw[i:j].decode("ascii")

    def test_no_em_dashes_in_block(self):
        raw = open(COMPETITOR, "rb").read()
        i = raw.find(b"mechanism_657_ani_openai")
        j = raw.find(b"  anthropic:", i)
        block = raw[i:j].decode("ascii")
        assert "\u2014" not in block and "\u2013" not in block


class TestStatisticalDiscipline704:
    def _sd(self):
        return mech()["statistical_discipline"]

    def test_scope_qualitative_only(self):
        assert self._sd()["scope"] == "qualitative structural mapping only"
        assert self._sd()["qualitative_only"] is True

    def test_correlation_not_causation(self):
        assert self._sd()["correlation_not_causation"] is True

    def test_p_cohens_ci_not_calculated(self):
        assert self._sd()["p_value"] == "NOT_CALCULATED"
        assert self._sd()["cohens_d"] == "NOT_CALCULATED"
        assert self._sd()["ci_95"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        assert self._sd()["is_significant"] is False

    def test_tone_not_scored(self):
        assert self._sd()["tone_scores"] == "NOT_SCORED"

    def test_artifact_grade_false(self):
        assert self._sd()["artifact_grade"] is False

    def test_no_analysis_json_update(self):
        assert "No analysis.json update" in mech()["artifact_readiness"]

    def test_no_coverage_tone_claim(self):
        assert mech()["no_coverage_tone_claim"] is True


class TestConfounderRanking704:
    def _confs(self):
        return mech()["ranked_confounders"]

    def test_five_ranked_confounders(self):
        assert len(self._confs()) == 5
        assert [c["rank"] for c in self._confs()] == [1, 2, 3, 4, 5]

    def test_strong_first_two(self):
        assert self._confs()[0]["strength"] == "strong"
        assert self._confs()[1]["strength"] == "strong"

    def test_second_hand_strong_confounder(self):
        assert "second-hand" in self._confs()[0]["confounder"]
        assert "2026: DHC: 5900" in self._confs()[0]["confounder"]

    def test_interim_ruling_strong_confounder(self):
        assert "interim prima facie" in self._confs()[1]["confounder"]
        assert "directional" in self._confs()[1]["confounder"]

    def test_moderate_next_two(self):
        assert self._confs()[2]["strength"] == "moderate"
        assert self._confs()[3]["strength"] == "moderate"
        assert "not a MediaScope tracked publication" in self._confs()[2]["confounder"]
        assert "coincidence" in self._confs()[3]["confounder"]

    def test_weak_last_distinct_from_609(self):
        assert self._confs()[4]["strength"] == "weak"
        assert "mechanism 609" in self._confs()[4]["confounder"]
        assert "not a duplicate" in self._confs()[4]["confounder"]


class TestCautionAndBoundaries704:
    def test_correlational_note_no_causal_claim(self):
        note = mech()["correlational_note"]
        assert "correlational structural incentives" in note
        assert "No causal claim" in note

    def test_cautious_language_required(self):
        assert mech()["cautious_language_required"] is True

    def test_not_falsification_family_member(self):
        assert "NOT a member" in mech()["falsification_family"]

    def test_ledger_stays_21(self):
        assert "ledger stays at 21" in mech()["falsification_family"]
        assert "TWENTY-FIRST" in mech()["falsification_family"]

    def test_qualitative_boundary_cited(self):
        assert "#609/#614 qualitative boundary" in mech()["falsification_family"]

    def test_timing_coincidence_flagged(self):
        conf = mech()["ranked_confounders"][3]["confounder"]
        assert "coincidence" in conf
        assert "not coordination" in conf

    def test_appeal_outcome_not_prejudged(self):
        assert "APPEAL PENDING" in mech()["appeal_status"]
        assert "outcome unresolved this run" in "\n".join(mech()["litigation_timeline"])


class TestRotationCycleGuard704:
    """Deselected pre-commit for the anchor test; anchor patched in followup."""

    WINDOW = {703: "B", 704: "C", 705: "D", 706: "E", 707: "A"}
    ANCHORED_SHA = ANCHORED_SHA

    def test_window_703_707_opens_b(self):
        assert self.WINDOW[703] == "B"
        assert self.WINDOW[704] == "C"

    def test_rotation_order_cyclic(self):
        order = ["A", "B", "C", "D", "E"]
        for it, typ in self.WINDOW.items():
            assert typ in order
        assert order[(order.index(self.WINDOW[703]) + 1) % 5] == self.WINDOW[704]
        assert self.WINDOW[705] == "D" and self.WINDOW[706] == "E" and self.WINDOW[707] == "A"

    def test_703_committed_in_git_log(self):
        out = git("log", "--oneline", "--grep", "Type B #703").stdout.strip()
        assert out != "", "missing committed iteration #703"

    def test_anchor_is_main_commit_704(self):
        # Per #565 convention the anchor is patched to the #704 main commit
        # in the followup; verify the patch landed.
        assert git("cat-file", "-e", f"{self.ANCHORED_SHA}^{{commit}}").returncode == 0
        msg = git("log", "-1", "--format=%s", self.ANCHORED_SHA).stdout.strip()
        assert "Type C #704" in msg

    def test_iteration_log_entry_regex_self_check(self):
        sample = "#704 Type C: ANI v. OpenAI India litigation leg"
        assert re.match(r"^#704 Type C:", sample)


class TestDocSyncRatchet704:
    README = os.path.join(REPO, "README.md")
    ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")
    LOG = os.path.join(REPO, "iteration-log.md")

    def test_readme_has_704_row(self):
        text = open(self.README, encoding="utf-8").read()
        assert TEST_BASENAME in text

    def test_architecture_has_704_tree_row(self):
        text = open(self.ARCH, encoding="utf-8").read()
        assert TEST_BASENAME in text

    def test_iteration_log_top_entry_704(self):
        text = open(self.LOG, encoding="utf-8").read()
        assert text.lstrip().startswith("#704 Type C:")

    def test_readme_row_mentions_ani_litigation(self):
        text = open(self.README, encoding="utf-8").read()
        seg = text[text.index(TEST_BASENAME):]
        seg = seg[:4000]
        assert "ANI" in seg and "litigation" in seg

    def test_doc_count_stats_sync(self):
        text = open(self.README, encoding="utf-8").read()
        assert "| Tests | 37142 |" in text and "Across 1032 test files" in text
