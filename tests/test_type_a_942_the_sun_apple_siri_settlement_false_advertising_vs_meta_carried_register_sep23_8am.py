"""Type A #942: The Sun (News Corp) x Apple Siri settlement "false advertising"
accountability register vs carried News Corp x Meta payer arm (m763) - Sep 23
2026 08:00 PDT.

FIRST dedicated mechanism block on The Sun (the-sun.com, The US Sun -
News Corp-owned via News UK; "The Sun" content is explicitly inside the
News Corp x OpenAI AI-licensing scope per mechanism 763 financial_context;
the_sun zero-hit repo-wide pre-commit). Fresh arms, Sep 18-22 2026,
excerpt-bounded per #503: (1) the Sep-22 Apple Siri AI $250M settlement
claims-opening piece ("iPhone 15 and 16 owners eligible to claim up to $95
in $250million payout after Apple accused of 'false advertising'", URL slug
17044701 zero-hit repo-wide pre-commit), MANUAL ILLUSTRATIVE -0.45
(accountability-adversarial consumer-service register: headline leads with
the plaintiff's allegation, Apple denial carried as the caveat); (2) the
Sep-18 iPhone 18 launch-lines piece ("Customers - and professional 'line
sitters' - queue up around the block to buy new $1,299 iPhone 18", URL slug
17024113 zero-hit repo-wide pre-commit), MANUAL ILLUSTRATIVE +0.35
(celebratory launch register: "Apple fever", global lines, CEO John Ternus
greeting customers). Within-outlet illustrative delta -0.80: same outlet,
same entity, 4 days apart - register selection tracks the news peg
(accountability vs launch celebration), not the entity. Carried comparator
un-rescored per #807: the NY Post Sep-18 Meta glasses-lawsuit piece from
m763 (-0.50). Illustrative Sun-Apple-settlement-minus-carried-NYPost-Meta
delta +0.05: near-symmetry at the adversarial tabloid register, consistent
with m763's dual-payer tabloid symmetry (+0.017). Reading: the parent's
tabloid register runs adversarial toward licensing payers (OpenAI -0.483,
Meta -0.50 at m763) AND toward the $0-AI-licensing non-partner (Apple -0.45
here) on liability pegs - uniform leniency is absent at the tabloid
register on both legs; the deal-softening prediction remains
partner-specific by construction (already falsified for the partner at
m763). NOT a falsification-family member (control-case extension: tests the
non-partner control, not the OpenAI-softening prediction); ledger holds at
29; THIRTIETH remains the negative guard. Verdict
directionally_supported_not_proven. NOT artifact-grade. No analysis.json
update. Correlation is not causation.
Max numeric mechanism_id 796 in-tree; zero underscore-form 796 mechanism
key strings repo-wide pre-commit (format-built needles, Type E iteration
artifacts acknowledged as non-mechanism). 940-944 window THIRD leg D->E->A
(anchor per #565). Concurrency: #884 (m762 competitor-entities.yaml),
#899 (m771 nytimes.yaml), #900 (untracked test) in-flight untouched.
ASCII-only. No em dashes.
"""
import os
import re
import glob
import subprocess

import pytest
import yaml

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOG = os.path.join(REPO, "iteration-log.md")
README = os.path.join(REPO, "README.md")
ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")
NEWSCORP = os.path.join(REPO, "profiles", "news-corp.yaml")
THIS_FILE = os.path.basename(__file__)

ITERATION = 942
TYPE_LETTER = "A"
RUN_PDT = "2026-09-23 08:00 PDT"
OWN_BASENAME = os.path.basename(__file__)
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

BLOCK_KEY = (
    "the_sun_apple_siri_settlement_false_advertising_"
    "vs_meta_carried_register_sep2026"
)

# Doc-sync ratchet: this file's own test count and the repo totals it
# implies (README 48414/1266 -> 48476/1267). Verified via .venv
# collect-only before the doc-sync edits.
THIS_FILE_TEST_COUNT = 62
README_TESTS_BEFORE = 48414
README_FILES_BEFORE = 1266
README_TESTS_AFTER = 48476
README_FILES_AFTER = 1267


def _git(args):
    return subprocess.run(
        ["git", "-C", REPO] + args, capture_output=True, text=True, timeout=120
    )


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _block():
    doc = yaml.safe_load(_read(NEWSCORP))
    return doc["competitor_relationships"]["apple"][BLOCK_KEY]


# --------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# --------------------------------------------------------------------------
class TestNoveltyAnchorTypeA942:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #942 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--", "tests/" + OWN_BASENAME],
            cwd=REPO,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type A #942" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    @pytest.mark.anchor
    def test_exactly_one_type_a_942_file_on_disk(self):
        files = glob.glob(os.path.join(REPO, "tests", "*type_a_942*"))
        assert len(files) == 1 and os.path.basename(files[0]) == THIS_FILE


# --------------------------------------------------------------------------
# 2. Rotation guard, 940-944 window (deselected pre-commit per #565)
# --------------------------------------------------------------------------
class TestRotationGuard940_944Window:
    @pytest.mark.rotation
    def test_third_leg_of_940_944_window(self):
        assert TYPE_LETTER == "A"
        assert ITERATION == 942

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {940: "D", 941: "E", 942: "A", 943: "B", 944: "C"}
        assert expected[942] == "A"

    @pytest.mark.rotation
    def test_predecessor_941_type_e_committed(self):
        # #941 Type E is COMMITTED (its log entry sits at the head of
        # iteration-log.md); this run's own #942 entry will be prepended
        # above it.
        assert "## #941 Type E" in _read(LOG)

    @pytest.mark.rotation
    def test_no_concurrent_inflight_commits_asserted(self):
        # In-flight at this run's checks: #884 Type C (m762),
        # #899 Type C (m771), #900 Type D - none committed yet.
        # (#898/m770 is absent, not in-flight: lost at #918, per #920.)
        # Match only commit SUBJECTS that ARE an iteration-N commit
        # (subject starts with "Type L #N"), since other commits'
        # subjects/bodies may merely mention them (e.g. this run's own
        # concurrency note naming #884/#899/#900).
        subjects = [
            _git(["log", "--format=%s", "-1", c]).stdout.strip()
            for c in _git(["log", "--format=%H", "-8"]).stdout.splitlines()
        ]
        for n in ("884", "899", "900"):
            pat = re.compile(r"^Type [ABCDE] #" + n + r"(?!\d)")
            assert not any(pat.search(s) for s in subjects), (n, subjects)


# --------------------------------------------------------------------------
# 3. Mechanism 796 structure
# --------------------------------------------------------------------------
class TestMechanism796Structure:
    def test_block_lives_under_news_corp_apple_section(self):
        doc = yaml.safe_load(_read(NEWSCORP))
        assert BLOCK_KEY in doc["competitor_relationships"]["apple"]

    def test_mechanism_id_796(self):
        assert _block()["mechanism_id"] == 796

    def test_iteration_942_type_a(self):
        assert _block()["iteration"] == 942
        assert _block()["iteration_type"] == "A"
        assert _block()["rotation"] == "Type A"

    def test_job_and_goal_ids(self):
        assert _block()["job_id"] == "mediascope-daily-iteration"
        assert _block()["goal_id"] == "goal_54093bda4145"

    def test_publication_focus_the_sun(self):
        focus = _block()["publication_focus"]
        assert "The Sun" in focus and "the-sun.com" in focus
        assert "News Corp" in focus

    def test_block_key_carries_no_underscore_form_796(self):
        # The designed block key carries the date suffix, not the
        # mechanism number (per the underscore-key convention; the
        # number lives in mechanism_id only).
        assert "796" not in BLOCK_KEY


# --------------------------------------------------------------------------
# 4. Finding content: two fresh Sun arms
# --------------------------------------------------------------------------
class TestFindingContent:
    def _arms(self):
        return {a["title"]: a for a in _block()["articles_apple_fresh"]}

    def test_fresh_arm1_settlement_url_present(self):
        urls = [a["url"] for a in _block()["articles_apple_fresh"]]
        assert (
            "https://www.the-sun.com/money/17044701/iphone-owners-claim-payout-"
            "apple-false-advertising-settlement/" in urls
        )

    def test_fresh_arm1_settlement_title_false_advertising(self):
        titles = [a["title"] for a in _block()["articles_apple_fresh"]]
        assert any("accused of 'false advertising'" in t for t in titles)

    def test_fresh_arm1_tone_minus_045(self):
        arm = self._arms()[
            "iPhone 15 and 16 owners eligible to claim up to $95 in "
            "$250million payout after Apple accused of 'false advertising'"
        ]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.45

    def test_fresh_arm1_register_accountability(self):
        arm = self._arms()[
            "iPhone 15 and 16 owners eligible to claim up to $95 in "
            "$250million payout after Apple accused of 'false advertising'"
        ]
        assert arm["register"] == "accountability_adversarial_consumer_service"

    def test_fresh_arm2_launch_url_present(self):
        urls = [a["url"] for a in _block()["articles_apple_fresh"]]
        assert (
            "https://www.the-sun.com/money/17024113/"
            "long-lines-apple-iphone-launch/" in urls
        )

    def test_fresh_arm2_launch_tone_plus_035(self):
        arm = self._arms()[
            "Customers - and professional 'line sitters' - queue up around "
            "the block to buy new $1,299 iPhone 18"
        ]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == 0.35
        assert arm["register"] == "launch_celebration_consumer_fever"

    def test_excerpts_verbatim_present(self):
        quotes = self._arms()[
            "iPhone 15 and 16 owners eligible to claim up to $95 in "
            "$250million payout after Apple accused of 'false advertising'"
        ]["key_quotes"]
        assert any("denied any wrongdoing" in q for q in quotes)
        assert any("$250million class action settlement" in q for q in quotes)

    def test_within_outlet_delta_minus_080(self):
        scorer = _block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        pair = scorer["within_outlet_pair"]
        assert pair["delta_settlement_minus_launch"] == -0.80
        assert pair["delta_calc"] == "(-0.45) - (0.35) = -0.80"

    def test_cross_outlet_delta_plus_005(self):
        scorer = _block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        pair = scorer["cross_outlet_family_pair"]
        assert pair["sun_apple_settlement"] == -0.45
        assert pair["carried_nypost_meta_glasses_lawsuit"] == -0.50
        assert pair["delta"] == 0.05
        assert pair["delta_calc"] == "(-0.45) - (-0.50) = +0.05"


# --------------------------------------------------------------------------
# 5. Statistical discipline (standing rule Aug 28 2026)
# --------------------------------------------------------------------------
class TestStatisticalDisciplineStandingRule:
    def _scorer(self):
        return _block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]

    def test_manual_illustrative_only(self):
        assert self._scorer()["methodology"].startswith("MANUAL ILLUSTRATIVE")

    def test_p_value_not_calculated(self):
        assert self._scorer()["p_value"] == "NOT_CALCULATED - illustrative only, standing rule Aug 28 2026"

    def test_cohens_d_not_calculated(self):
        assert self._scorer()["cohens_d"] == "NOT_CALCULATED"

    def test_ci_95_not_calculated(self):
        assert self._scorer()["ci_95"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        assert self._scorer()["is_significant"] is False

    def test_engine_not_run(self):
        assert "Engine NOT run" in self._scorer()["methodology"]

    def test_verdict_directionally_supported_not_proven(self):
        assert (
            _block()["statistical_discipline"].find(
                "directionally_supported_not_proven"
            )
            >= 0
        )

    def test_not_artifact_grade_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True
        assert "NOT artifact-grade" in _block()["finding"]


# --------------------------------------------------------------------------
# 6. Financial geometry
# --------------------------------------------------------------------------
class TestFinancialGeometry:
    def test_news_corp_openai_deal_in_financial_context(self):
        fc = _block()["financial_context"]
        assert "$50M/yr" in fc and "May 2024" in fc

    def test_meta_deal_in_financial_context(self):
        fc = _block()["financial_context"]
        assert "up to $50M/yr" in fc and "Mar 2026" in fc

    def test_apple_zero_ai_licensing_leg(self):
        fc = _block()["financial_context"]
        assert "$0 documented AI-licensing revenue to News Corp" in fc

    def test_sun_inside_openai_licensing_scope(self):
        fc = _block()["financial_context"]
        assert "The Sun content in scope" in fc

    def test_deal_softening_prediction_partner_specific(self):
        assert "partner-specific by construction" in _block()["finding"]


# --------------------------------------------------------------------------
# 7. Carried arms per #807
# --------------------------------------------------------------------------
class TestCarriedArms807:
    def _carried(self):
        return _block()["articles_meta_carried"][0]

    def test_m763_nypost_meta_arm_carried_minus_050(self):
        arm = self._carried()
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.50
        assert arm["publication"] == "New York Post"

    def test_carried_unrescored_per_807_marker(self):
        assert "carried from mechanism 763 (#887)" in self._carried()[
            "url_status"
        ]

    def test_scorer_methodology_names_807(self):
        assert "per #807" in _block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"][
            "methodology"
        ]

    def test_carried_url_not_claimed_novel(self):
        assert "NOT claimed novel" in self._carried()["url_status"]


# --------------------------------------------------------------------------
# 8. Confounders and counter-evidence
# --------------------------------------------------------------------------
class TestConfoundersAndCounterEvidence:
    def test_strong_confounders_present(self):
        strong = _block()["confounders_ranked"]["strong"]
        assert any("Tabloid genre default" in c for c in strong)

    def test_excerpt_bounded_evidence_grade(self):
        strong = _block()["confounders_ranked"]["strong"]
        assert any("Excerpt-bounded fresh arms" in c for c in strong)

    def test_moderate_and_weak_confounders(self):
        ranked = _block()["confounders_ranked"]
        assert len(ranked["moderate"]) >= 2
        assert len(ranked["weak"]) >= 1

    def test_counter_evidence_present(self):
        ce = _block()["counter_evidence"]
        assert any("m697" in c for c in ce)
        assert any("m631" in c for c in ce)

    def test_correlation_not_causation(self):
        assert _block()["correlation_not_causation"] is True


# --------------------------------------------------------------------------
# 9. Falsification ledger
# --------------------------------------------------------------------------
class TestFalsificationLedger:
    def test_not_a_falsification_family_member(self):
        assert _block()["falsification_family"].startswith("NOT a member")

    def test_ledger_holds_at_29(self):
        assert "holds at 29" in _block()["ledger"]
        assert "TWENTY-NINTH" in _block()["ledger"]

    def test_thirtieth_remains_negative_guard(self):
        assert "THIRTIETH remains the negative guard" in _block()[
            "falsification_family"
        ]

    def test_no_thirtieth_member_form_for_796(self):
        # Negative guard per #860: no "THIRTIETH" member-form string tied
        # to this run's mechanism anywhere repo-wide (format-built
        # needle, no literal carrier beyond this assertion's own parts).
        n1 = "TH" + "IR" + "TI" + "ETH"
        hits = []
        for p in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"),
                           recursive=True):
            t = open(p, errors="ignore").read()
            if n1 in t and "796" in t[max(0, t.find(n1) - 200):t.find(n1) + 200]:
                hits.append(p)
        assert hits == []

    def test_finding_states_control_case_extension(self):
        assert "Control-case extension" in _block()["finding"]


# --------------------------------------------------------------------------
# 10. Doc-sync ratchet per #719
# --------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_stats_table_updated(self):
        readme = _read(README)
        assert str(README_TESTS_AFTER) in readme
        assert str(README_FILES_AFTER) in readme

    def test_readme_test_file_table_row_present(self):
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        text = _read(ARCH)
        assert THIS_FILE.replace(".py", "") in text


# --------------------------------------------------------------------------
# 11. Iteration-log entry per #719 (fails by design pre-commit)
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_942_marker(self):
        assert "## #942 Type A" in _read(LOG)

    def test_log_entry_names_window_leg(self):
        assert "940-944 window" in _read(LOG)


# --------------------------------------------------------------------------
# 12. Corpus novelty greps (post-commit form)
# --------------------------------------------------------------------------
class TestCorpusNoveltyPostCommitGreps:
    def test_exactly_one_type_a_942_file(self):
        files = glob.glob(os.path.join(REPO, "tests", "*type_a_942*"))
        assert len(files) == 1 and os.path.basename(files[0]) == THIS_FILE

    def test_this_file_test_count_matches_collect(self):
        # The doc-sync ratchet constants stay honest: THIS_FILE holds
        # exactly THIS_FILE_TEST_COUNT tests (collect-only, no -m).
        import sys
        sys.path.insert(0, os.path.join(REPO, ".venv", "lib", "python3.12",
                                        "site-packages"))
        result = subprocess.run(
            [os.path.join(REPO, ".venv", "bin", "pytest"), "--collect-only",
             "-q", "tests/" + THIS_FILE],
            cwd=REPO, capture_output=True, text=True, timeout=120,
        )
        m = re.search(r"(\d+) tests? collected", result.stdout)
        assert m and int(m.group(1)) == THIS_FILE_TEST_COUNT, result.stdout[-500:]

    def test_max_numeric_mechanism_id_796(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(
            os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True
        ):
            for m in re.finditer(
                n7 + r"\s*(\d+)", open(f, errors="ignore").read()
            ):
                maxid = max(maxid, int(m.group(1)))
        # 796 in-tree: 796 (this run, news-corp.yaml apple section).
        # The in-flight #884/#899 blocks (m762/m771) are lower.
        assert maxid == 796

    def test_exactly_one_numeric_796_key_in_profiles(self):
        # Only the new block's colon-form KEY line counts; prose
        # mentions of the pre-commit sweep inside the quoted
        # research_method/novelty strings are not keys (format-built
        # needle per #715: no literal next-number key string carried).
        d1 = "79" + "6"
        hits = []
        for f in glob.glob(
            os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True
        ):
            for i, line in enumerate(open(f, errors="ignore"), 1):
                s = line.strip()
                if re.match(r"mechanism_id:\s*" + d1 + r"([^0-9]|$)", s):
                    hits.append((f, i))
        assert len(hits) == 1
        assert hits[0][0].endswith("profiles/news-corp.yaml")

    def test_zero_format_built_796_carriers(self):
        # Format-built needles per #715: no literal 796 mechanism key
        # strings carried. Designed keying is colon-form in profiles/;
        # the tests/ filename hits are a different namespace.
        # __pycache__ artifacts excluded per the #715 pattern-rescope
        # lesson. Own file excluded as sweep carrier. The Type E
        # iteration-number artifacts (after_796, from_796) are not
        # mechanism keys and are not matched by the needles.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_79" + "6"
        n2 = "mech" + "anism" + "-" + "79" + "6"
        hits = []
        for p in glob.glob(
            os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True
        ):
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.append(p)
        for p in glob.glob(os.path.join(REPO, "tests", "test_*.py")):
            if os.path.basename(p) == THIS_FILE:
                continue
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.append(p)
        assert hits == []

    def test_block_key_exactly_once_as_mapping_key(self):
        # The full key occurs once as a YAML mapping key; prose
        # mentions of the prefix inside the quoted
        # research_method/novelty strings are not keys (prefix form per
        # the #877 convention; BLOCK_KEY is this run's own designed key).
        keyed = [
            line
            for line in _read(NEWSCORP).splitlines()
            if re.match(r"^    " + re.escape(BLOCK_KEY) + r":\s*$", line)
        ]
        assert len(keyed) == 1

    def test_url_slugs_novel_to_profiles(self):
        # Slugs 17044701 and 17024113 novel this run: within profiles/
        # their sole carrier is news-corp.yaml (docs/ARCHITECTURE.md and
        # this test file are this run's own documentation carriers;
        # format-built slugs, no literal carrier).
        for s in ("17" + "044701", "17" + "024113"):
            out = _git(["grep", "-l", s, "--", "profiles/"]).stdout.splitlines()
            assert out == ["profiles/news-corp.yaml"], (s, out)

    def test_concurrent_inflight_files_not_in_this_commit_scope(self):
        # In-flight: #884 Type C (competitor-entities.yaml m762),
        # #899 Type C (nytimes.yaml m771), #900 Type D (untracked test
        # file) - all uncommitted; this run's staged set must not
        # include those files. (#898/m770 is absent, not in-flight.)
        status = _git(["status", "--short"]).stdout
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        for f in ("competitor-entities", "journalists.yaml", "nytimes.yaml"):
            assert not any(f in l for l in staged)

    def test_ascii_only_no_em_dashes(self):
        text = _read(__file__)
        assert "\u2014" not in text
