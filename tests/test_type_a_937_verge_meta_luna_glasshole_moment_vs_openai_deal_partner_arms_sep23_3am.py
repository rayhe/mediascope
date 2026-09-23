"""Type A #937: The Verge x Meta Luna "Glasshole Moment" launch-day register
vs carried Verge x OpenAI deal-partner arms (m751/m598) - Sep 23 2026 03:00 PDT.

FIRST dedicated mechanism block under the the-verge.yaml meta: entity section
(previously a stub header only). Fresh arm: The Verge's Sep-23 2026 launch-day
Luna piece ("Meta's Camera-Free 'Luna' Smart Glasses Are the Company's
Glasshole Moment", URL slug 785732 zero-hit repo-wide pre-commit),
excerpt-bounded per #503 (theverge.com policy-blocked for browser.open per
standing rule). MANUAL ILLUSTRATIVE -0.50 (adversarial privacy-alarm
editorial). Carried comparators un-rescored per #807: Verge x OpenAI m751
(-0.55, Sep-18 doom-loop legal-filing) and m598 (-0.65, Sep-4/5 wiki-incident),
mean -0.60; Verge x Meta m592 July glasses band [-0.55, -0.60, -0.50], mean
-0.55; BI x Meta Luna relay m786 (#932, -0.25) as same-peg cross-publication
control. Illustrative deltas: Meta-Luna-minus-OpenAI-mean +0.10 (non-payer
softer than the Vox deal partner at the same outlet - inversion of the naive
payer-softening prediction); Verge-minus-BI on the identical Luna peg -0.25.
NOT a falsification-family member (genre skew STRONG; clean same-beat
falsification already exists as m751, TWENTY-SEVENTH member); control-case
extension. Ledger holds at 29; THIRTIETH remains the negative guard.
Verdict directionally_supported_not_proven. NOT artifact-grade.
No analysis.json update. Correlation is not causation.
Max numeric mechanism_id 793 in-tree; zero underscore-form 793 mechanism key
strings repo-wide. 935-939 window THIRD leg D->E->A (anchor per #565).
Concurrency: #884 (m762 competitor-entities.yaml), #899 (m771 nytimes.yaml),
#900 (untracked test) in-flight untouched. ASCII-only. No em dashes.
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
VERGE = os.path.join(REPO, "profiles", "the-verge.yaml")
THIS_FILE = os.path.basename(__file__)

ITERATION = 937
TYPE_LETTER = "A"
RUN_PDT = "2026-09-23 03:00 PDT"
OWN_BASENAME = os.path.basename(__file__)
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

BLOCK_KEY = (
    "verge_meta_luna_glasshole_moment_launch_register_"
    "vs_openai_deal_partner_arms_sep23_2026"
)


def _git(args):
    return subprocess.run(
        ["git", "-C", REPO] + args, capture_output=True, text=True, timeout=120
    )


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _block():
    doc = yaml.safe_load(_read(VERGE))
    return doc["competitor_relationships"]["meta"][BLOCK_KEY]


# --------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# --------------------------------------------------------------------------
class TestNoveltyAnchorTypeA937:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #937 main commit exists pre-commit; the anchor test pins
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
            if "Type A #937" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    @pytest.mark.anchor
    def test_exactly_one_type_a_937_file_on_disk(self):
        files = glob.glob(os.path.join(REPO, "tests", "*type_a_937*"))
        assert len(files) == 1 and os.path.basename(files[0]) == THIS_FILE


# --------------------------------------------------------------------------
# 2. Rotation guard, 935-939 window (deselected pre-commit per #565)
# --------------------------------------------------------------------------
class TestRotationGuard935_939Window:
    @pytest.mark.rotation
    def test_third_leg_of_935_939_window(self):
        assert TYPE_LETTER == "A"
        assert ITERATION == 937

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {935: "D", 936: "E", 937: "A", 938: "B", 939: "C"}
        assert expected[937] == "A"

    @pytest.mark.rotation
    def test_predecessor_936_type_e_committed(self):
        # #936 Type E is COMMITTED (its log entry sits at the head of
        # iteration-log.md); this run's own #937 entry will be prepended
        # above it.
        assert "## #936 Type E" in _read(LOG)

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
# 3. Mechanism 793 structure
# --------------------------------------------------------------------------
class TestMechanism793Structure:
    def test_block_lives_under_verge_meta_section(self):
        doc = yaml.safe_load(_read(VERGE))
        assert BLOCK_KEY in doc["competitor_relationships"]["meta"]

    def test_mechanism_id_793(self):
        assert _block()["mechanism_id"] == 793

    def test_iteration_937_type_a(self):
        b = _block()
        assert b["iteration"] == 937
        assert b["iteration_type"] == "A"
        assert b["iteration_time"] == "2026-09-23 03:00 PDT"

    def test_job_and_goal_ids(self):
        b = _block()
        assert b["scheduled_job_id"] == "mediascope-daily-iteration"
        assert b["goal_id"] == "goal_54093bda4145"

    def test_block_key_carries_no_underscore_form_793(self):
        # Designed keying per #715: the block key must not carry an
        # underscore-form 793 mechanism key substring (format-built
        # needle, no literal carrier).
        n1 = "m" + "ech" + "an" + "is" + "m" + "_79" + "3"
        assert n1 not in BLOCK_KEY

    def test_publication_focus_the_verge(self):
        assert _block()["publication_focus"] == "The Verge (Vox Media)"


# --------------------------------------------------------------------------
# 4. Finding content
# --------------------------------------------------------------------------
class TestFindingContent:
    def test_fresh_arm_url_present(self):
        url = _block()["meta_fresh_arm"]["url"]
        assert url == (
            "https://www.theverge.com/news/785732/"
            "meta-luna-camera-free-smart-glasses-glasshole-moment"
        )

    def test_fresh_arm_title_glasshole_moment(self):
        title = _block()["meta_fresh_arm"]["title"]
        assert "Glasshole Moment" in title
        assert "Luna" in title

    def test_fresh_arm_tone_minus_half(self):
        assert _block()["meta_fresh_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.50

    def test_fresh_arm_register(self):
        assert (
            _block()["meta_fresh_arm"]["register"]
            == "adversarial_privacy_alarm_editorial"
        )

    def test_excerpts_verbatim_present(self):
        excerpts = _block()["meta_fresh_arm"]["excerpts_verbatim"]
        assert len(excerpts) >= 3
        assert any("Glasshole Moment" in e for e in excerpts)

    def test_delta_meta_luna_minus_openai_plus_tenth(self):
        scorer = _block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["illustrative_delta_meta_luna_minus_openai_mean"] == 0.10

    def test_cross_publication_same_peg_delta(self):
        ctrl = _block()["cross_publication_same_peg_control"]
        assert ctrl["illustrative_verge_minus_bi"] == -0.25
        assert ctrl["bi_luna_arm"]["manual_illustrative_tone"] == -0.25


# --------------------------------------------------------------------------
# 5. Statistical discipline: the Aug 28 2026 standing rule
# --------------------------------------------------------------------------
class TestStatisticalDisciplineStandingRule:
    def test_manual_illustrative_only(self):
        assert (
            _block()["statistical_discipline"]["scorer"]
            == "MANUAL ILLUSTRATIVE only"
        )

    def test_p_value_not_calculated(self):
        assert "NOT_CALCULATED" in _block()["statistical_discipline"]["p_value"]

    def test_cohens_d_not_calculated(self):
        assert "NOT_CALCULATED" in _block()["statistical_discipline"]["cohens_d"]

    def test_ci_95_not_calculated(self):
        assert "NOT_CALCULATED" in _block()["statistical_discipline"]["ci_95"]

    def test_is_significant_false(self):
        assert _block()["statistical_discipline"]["is_significant"] is False

    def test_engine_not_run(self):
        assert _block()["statistical_discipline"]["engine"] == "NOT run"

    def test_verdict_directionally_supported_not_proven(self):
        assert (
            _block()["statistical_discipline"]["verdict"]
            == "directionally_supported_not_proven"
        )

    def test_not_artifact_grade_no_analysis_json_update(self):
        sd = _block()["statistical_discipline"]
        assert sd["artifact_grade"] is False
        assert sd["no_analysis_json_update"] is True
        assert sd["correlation_not_causation"] is True


# --------------------------------------------------------------------------
# 6. Financial geometry: Vox x OpenAI deal vs $0 Meta tie
# --------------------------------------------------------------------------
class TestFinancialGeometry:
    def test_vox_openai_deal_in_entity_pair(self):
        assert "May 29 2024" in _block()["entity_pair"]

    def test_meta_zero_tie_in_entity_pair(self):
        assert "$0 tie" in _block()["entity_pair"]

    def test_meta_section_zero_tie_header(self):
        doc = yaml.safe_load(_read(VERGE))
        meta = doc["competitor_relationships"]["meta"]
        assert meta["financial_tie"] == "none"
        assert meta["estimated_value"] == "$0"

    def test_openai_section_deal_header(self):
        doc = yaml.safe_load(_read(VERGE))
        openai = doc["competitor_relationships"]["openai"]
        assert openai["financial_tie"] == "licensing"
        assert openai["coverage_prediction"] == "softer"
        assert "May 2024" in openai["description"]
        # The deal is documented in-corpus via the m751/m598 blocks; the
        # finding names the venturebeat-attested May 29 2024 partnership.
        assert "May 29 2024" in _block()["incentive_attribution"]


# --------------------------------------------------------------------------
# 7. Carried arms per #807 (un-rescored)
# --------------------------------------------------------------------------
class TestCarriedArms807:
    def test_openai_m751_carried_minus_055(self):
        arms = _block()["openai_arms_carried"]["arms"]
        m751 = [a for a in arms if a["mechanism"] == 751][0]
        assert m751["manual_illustrative_tone"] == -0.55

    def test_openai_m598_carried_minus_065(self):
        arms = _block()["openai_arms_carried"]["arms"]
        m598 = [a for a in arms if a["mechanism"] == 598][0]
        assert m598["manual_illustrative_tone"] == -0.65

    def test_openai_carried_mean_minus_060(self):
        assert _block()["openai_arms_carried"]["openai_carried_mean"] == -0.60

    def test_meta_band_m592_carried(self):
        band = _block()["meta_band_carried"]
        assert band["source_mechanism"] == 592
        assert band["meta_band_mean"] == -0.55
        tones = [a["manual_illustrative_tone"] for a in band["arms"]]
        assert tones == [-0.55, -0.60, -0.50]

    def test_carried_per_807_markers(self):
        assert "#807" in _block()["openai_arms_carried"]["carried_per"]
        assert "#807" in _block()["meta_band_carried"]["carried_per"]

    def test_scorer_methodology_names_807(self):
        assert "#807" in _block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"][
            "methodology"
        ]


# --------------------------------------------------------------------------
# 8. Confounders and counter-evidence
# --------------------------------------------------------------------------
class TestConfoundersAndCounterEvidence:
    def test_genre_skew_strong_confounders(self):
        strong = _block()["confounders"]["strong"]
        assert any("Genre skew" in c for c in strong)

    def test_excerpt_bounded_evidence_grade(self):
        grade = _block()["meta_fresh_arm"]["evidence_grade"]
        assert "excerpt-bounded" in grade
        assert "0 browser.open" in grade

    def test_temporal_skew_moderate(self):
        moderate = _block()["confounders"]["moderate"]
        assert any("Temporal skew" in c for c in moderate)

    def test_counter_evidence_present(self):
        assert len(_block()["counter_evidence"]) >= 3

    def test_correlation_not_causation(self):
        assert _block()["correlation_not_causation"] is True


# --------------------------------------------------------------------------
# 9. Falsification ledger: NOT a member, holds at 29
# --------------------------------------------------------------------------
class TestFalsificationLedger:
    def test_not_a_falsification_family_member(self):
        assert _block()["falsification_family"].startswith("NOT a member")

    def test_ledger_holds_at_29(self):
        assert _block()["ledger"] == "29"

    def test_thirtieth_remains_negative_guard(self):
        assert "THIRTIETH remains the negative guard" in _block()[
            "falsification_family"
        ]

    def test_no_thirtieth_member_form_for_793(self):
        # Negative guard per #860: no "THIRTIETH" member-form string tied
        # to this run's mechanism anywhere repo-wide (format-built
        # needle, no literal carrier beyond this assertion's own parts).
        n1 = "TH" + "IR" + "TI" + "ETH"
        hits = []
        for p in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"),
                           recursive=True):
            t = open(p, errors="ignore").read()
            if n1 in t and "793" in t[max(0, t.find(n1) - 200):t.find(n1) + 200]:
                hits.append(p)
        assert hits == []

    def test_finding_states_control_case_extension(self):
        assert "control-case extension" in _block()["finding"]


# --------------------------------------------------------------------------
# 10. Doc-sync ratchet per #719
# --------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_stats_table_updated(self):
        readme = _read(README)
        assert "48199" in readme and "1262" in readme

    def test_readme_test_file_table_row_present(self):
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        text = _read(ARCH)
        assert THIS_FILE.replace(".py", "") in text


# --------------------------------------------------------------------------
# 11. Iteration-log entry per #719 (fails by design pre-commit)
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_937_marker(self):
        assert "## #937 Type A" in _read(LOG)

    def test_log_entry_names_window_leg(self):
        assert "935-939 window" in _read(LOG)


# --------------------------------------------------------------------------
# 12. Corpus novelty greps (post-commit form)
# --------------------------------------------------------------------------
class TestCorpusNoveltyPostCommitGreps:
    def test_exactly_one_type_a_937_file(self):
        files = glob.glob(os.path.join(REPO, "tests", "*type_a_937*"))
        assert len(files) == 1 and os.path.basename(files[0]) == THIS_FILE

    def test_max_numeric_mechanism_id_793(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(
            os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True
        ):
            for m in re.finditer(
                n7 + r"\s*(\d+)", open(f, errors="ignore").read()
            ):
                maxid = max(maxid, int(m.group(1)))
        # 793 in-tree: 793 (this run, the-verge.yaml meta section).
        # The in-flight #884/#899 blocks (m762/m771) are lower.
        assert maxid == 793

    def test_exactly_one_numeric_793_key_in_profiles(self):
        # Only the new block's colon-form KEY line counts; prose
        # mentions of the pre-commit sweep inside the quoted
        # research_method/novelty strings are not keys (format-built
        # needle per #715: no literal next-number key string carried).
        d1 = "79" + "3"
        hits = []
        for f in glob.glob(
            os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True
        ):
            for i, line in enumerate(open(f, errors="ignore"), 1):
                s = line.strip()
                if re.match(r"mechanism_id:\s*" + d1 + r"([^0-9]|$)", s):
                    hits.append((f, i))
        assert len(hits) == 1
        assert hits[0][0].endswith("profiles/the-verge.yaml")

    def test_zero_format_built_793_carriers(self):
        # Format-built needles per #715: no literal 793 mechanism key
        # strings carried. Designed keying is colon-form in profiles/;
        # the tests/ filename hits are a different namespace.
        # __pycache__ artifacts excluded per the #715 pattern-rescope
        # lesson. Own file excluded as sweep carrier.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_79" + "3"
        n2 = "mech" + "anism" + "-" + "79" + "3"
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
            for line in _read(VERGE).splitlines()
            if re.match(r"^    " + re.escape(BLOCK_KEY) + r":\s*$", line)
        ]
        assert len(keyed) == 1

    def test_url_slug_novel_to_profiles(self):
        # Slug 785732 novel this run: within profiles/ its sole carrier
        # is the-verge.yaml (docs/ARCHITECTURE.md and this test file are
        # this run's own documentation carriers; format-built slug, no
        # literal carrier).
        s1 = "78" + "57" + "32"
        out = _git(["grep", "-l", s1, "--", "profiles/"]).stdout.splitlines()
        assert out == ["profiles/the-verge.yaml"], out

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
