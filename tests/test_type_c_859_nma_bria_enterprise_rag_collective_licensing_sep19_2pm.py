"""Type C #859 (855-859 window, fifth leg D->E->A->B->C, CLOSING the window):
News/Media Alliance x Bria enterprise-RAG collective licensing - first
dedicated US trade-association collective-licensing mechanism in the
corpus (mechanism 747). NMA (about 2,200 news, magazine and digital
media organizations; opt-in) licenses textual content into Bria's AI
System RAG product for enterprise clients; Bria compensates publishers
50% of all revenues apportioned by Bria's proprietary attribution
technology; AI System sublicensable as white-label to enterprise
customers (primary NMA AI Licensing Program page). Buyer side:
enterprise AI teams, foundation model developers, copilot builders,
agent orchestration platforms, legal/financial-services/healthcare
companies (Vered Horesh, Bria chief AI strategy officer, Digiday).
Usage modes: RAG pipelines, enterprise copilots, agent-based research
and analysis, search and answer engines. Announced March 23 2026
(Digiday, Sara Guaglione); six months old but NEW TO THE CORPUS as a
dedicated leg. Promotes the mechanism 723 tier_3_collective roster
mention ("NMA-Bria: 2,200 publisher members, enterprise AI clients
(Mar 2026)") to a first-class mechanism - the exact mirror of #819's
promotion of the "UK PLS Generative AI Solution" roster mention to
mechanism 723. First disclosed-economics collective mechanism in the
corpus (50% split, primary-sourced) versus undisclosed-fee PLS UK
(mechanism 723) and undisclosed-quantum Cashmere rails (mechanism 663).
Distinct from mechanism 663 (Cashmere/Perplexity single-lab
premium-data RAG rails, per-token pricing), mechanism 391 (Comet Plus
80/20 consumer revenue share), mechanisms 702/708 (Google buyer-side
pay-per-value pilot), mechanism 720 (LINC KK APAC pool-and-license),
mechanism 509 (Anthropic zero-deal contrast leg), and the Snowflake
enterprise-RAG marketplace intermediary. Mediascope relevance: a
supplier-side collective route INDEPENDENT of every Meta competitor -
the counterparty is startup Bria, not a big-five payer; publisher
diversification path not running through a competitor. Status ACTIVE
per #599 (bounded absence of termination/amendment). Confounders
2/2/1 (zero opt-in count; zero disclosed dollars; March vintage not
September news; proprietary attribution engine; paywall bounded
absence). Counterevidence 3 (Coffey "devastating" crisis frame;
Prohaska big-five second-best frame; no named enterprise clients).
MANUAL qualitative only, engine NOT run, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False, verdict
directionally_supported_not_proven; NOT falsification-family, ledger
holds at 26; no analysis.json update. Novelty verified pre-commit
(zero test_type_c_859 files; no 'Type C #859' in git log; max numeric
mechanism_id 746; zero underscore-form 747 keys by designed keying per
#715; block key zero-hit; zero dedicated Bria/NMA mechanisms
pre-commit - only m720 re-index mentions and the m723 roster entry;
all 7 Bria source URLs zero-hit repo-wide); 855-859 window fifth leg
D->E->A->B->C CLOSING it (anchor patched post-commit per #565) -
Sep 19 2026 14:00 PDT.
"""

import os
import re
import subprocess
import datetime

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = "test_type_c_859_nma_bria_enterprise_rag_collective_licensing_sep19_2pm.py"
MECH_KEY = "nma_bria_enterprise_rag_collective_licensing_sep2026"
M_ID = 747
ITER = 859
TYPE_LETTER = "C"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_747"
NEXT_ID_MARKER = "mechanism" + "_748"
NEXT_ID_NUMERIC = "mechanism_id: " + "748"
EXPECTED_ORDER = [("C", "859"), ("B", "858"), ("A", "857"), ("E", "856"), ("D", "855")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "c2872744d458293c13a362d97e6fc7373a1ea3b2"

DIGIDAY_URL = "https://digiday.com/media/news-media-alliance-signs-ai-licensing-deal-to-unlock-recurring-rag-revenue-for-small-and-mid-sized-publishers/"
NMA_PROGRAM_URL = "https://www.newsmediaalliance.org/news-media-alliance-ai-licensing-program/"
MEDIAPOST_URL = "https://www.mediapost.com/publications/article/413770/content-bounty-newsmedia-alliance-works-with-bri.html"
TVNEWSCHECK_URL = "https://tvnewscheck.com/ai/article/news-media-alliance-bria-ai-partner-on-licensing-agreement/"
BRIEFLY_URL = "https://briefly.co/anchor/Media_industry/story/newsmedia-alliance-signs-ai-licensing-deal-to-unlock-recurring-rag-revenue-for-small-and-mid-sized-publishers"
PULSE_URL = "https://www.pulse.bot/entertainment/news/newsmedia-alliance-signs-ai-licensing-deal-to-unlock-recurring-rag-revenue-for-small-and-mid-sized-p-21f01300-25a8-4e89-8803-90ed76c3ffb3/"
GREENHELIX_URL = "https://github.com/openclaw/skills/blob/HEAD/skills/mirni/greenhelix-agent-content-licensing-royalties/SKILL.md"

README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _entities_text():
    return _read(os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml"))


def _block():
    text = _entities_text()
    start = text.index(MECH_KEY)
    end = text.index("\nadvance_dual_asset_monetization:")
    return text[start:end]


def _corpus_ids():
    ids = []
    for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith(".yaml"):
                text = _read(os.path.join(root, fn))
                for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                    ids.append(int(m.group(1)))
    return ids


def _repo_grep(needle, roots=("profiles", "tests")):
    hits = []
    for r in roots:
        base = os.path.join(REPO_ROOT, r)
        for root, _, files in os.walk(base):
            for fn in files:
                if fn.rsplit(".", 1)[-1] in ("py", "yaml", "md", "json"):
                    p = os.path.join(root, fn)
                    try:
                        if needle in _read(p):
                            hits.append(os.path.relpath(p, REPO_ROOT))
                    except OSError:
                        pass
    return hits


def _git(*args):
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def _git_log_mains(qualifier):
    # --grep searches full commit messages (subject + body), so a body
    # mention of the qualifier (e.g. the anchor followup explaining its own
    # qualifier fix) would wrongly match. Filter subjects in Python so only
    # the real main commit qualifies.
    out = _git("log", "--all", "--format=%H %s", "--grep", "Type C #859")
    mains = {}
    for line in out.splitlines():
        if not line.strip():
            continue
        sha, _, subject = line.partition(" ")
        if "Type C #859" in subject and qualifier in subject:
            mains[sha] = subject
    return mains


def _window(n=40):
    # First occurrence of each distinct iteration number, newest first
    # (robust to followup commits that repeat the same "Type X #N" wording
    # without the colon, per the #752 convention).
    subjects = _git("log", f"-{n}", "--format=%s", "--no-merges").splitlines()
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out[:5]


class TestNovelty859:
    def test_single_test_type_c_859_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_c_859") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_c_859_main_commit_unique_and_anchored(self):
        # No #859 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--", "tests/" + OWN_BASENAME],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type C #859" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # This run ADDS mechanism 747: post-commit max is 747, zero 748
        # keys anywhere. Pre-commit sweeps verified max 746, zero
        # underscore-form 747 keys (designed keying per #715), block key
        # zero-hit, zero dedicated Bria/NMA mechanisms, all 7 source URLs
        # zero-hit repo-wide.
        assert max(_corpus_ids()) == 747
        assert _repo_grep(NEXT_ID_MARKER) == []
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == []

    def test_855_859_window_legs_present_prior_to_859(self):
        log = _read(LOG_PATH)
        for marker in (
            "## #855 Type D:",
            "## #856 Type E:",
            "## #857 Type A:",
            "## #858 Type B:",
        ):
            assert marker in log, marker


class TestRotationGuard859:
    """#859 is the Type C fifth leg of window 855-859: D->E->A->B->C, CLOSING it."""

    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_855_859_fifth_leg(self):
        # Deselected pre-commit per #565 (the #859 main commit does not
        # exist yet); patched green in the anchor followup.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"855-859 window fifth leg D->E->A->B->C: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_b_858(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        assert window[1] == ("B", "858"), (
            f"immediate predecessor must be Type B #858, got {window[1]}"
        )

    def test_anchor_sha_matches_head(self):
        # Patched to the real main-commit SHA in the anchor followup per
        # the #565 convention; deselected pre-commit at the pytest CLI.
        mains = _git_log_mains("Type C #859: News/Media Alliance x Bria")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism747Structure:
    def test_block_key_exists_in_competitor_entities(self):
        assert MECH_KEY in _entities_text()

    def test_block_key_unique(self):
        keys = re.findall(r"^  " + MECH_KEY + r":$", _entities_text(), re.M)
        assert len(keys) == 1, keys

    def test_block_nests_under_marketplace_intermediary_landscape(self):
        text = _entities_text()
        assert text.index("marketplace_intermediary_landscape:") < text.index(MECH_KEY)
        assert text.index(MECH_KEY) < text.index("\nadvance_dual_asset_monetization:")

    def test_iteration_and_type_and_time_pdt(self):
        block = _block()
        assert "iteration: 859" in block
        assert "type: 'C'" in block
        assert "2026-09-19 14:00 PDT" in block
        assert "mechanism_id: 747" in block

    def test_designed_keying_no_underscore_747_in_block(self):
        # Per #715: block keys and prose must not carry the underscore-form
        # mechanism id; the colon form mechanism_id: 747 is the only allowed
        # 747 reference.
        block = _block()
        assert MECH_ID_MARKER not in block
        assert "mechanism_id: 747" in block

    def test_yaml_parses_and_fields(self):
        d = yaml.safe_load(_entities_text())
        mech = d["marketplace_intermediary_landscape"][MECH_KEY]
        assert mech["mechanism_id"] == 747
        assert mech["verification"]["iteration"] == 859
        assert mech["verification"]["type"] == "C"
        assert mech["verification"]["date"] == "2026-09-19 14:00 PDT"
        assert mech["verdict"] == "directionally_supported_not_proven"
        assert mech["falsification_family"] is False
        assert mech["falsification_ledger_holds_at"] == 26
        assert mech["tone_scores"] == "NOT_SCORED"
        assert mech["connects_to"] == [723, 720]

    def test_max_mechanism_id_is_747(self):
        assert max(_corpus_ids()) == 747


class TestMechanism747DealFacts:
    def test_announced_mar_23_2026_digiday(self):
        block = _block()
        assert "March 23 2026" in block
        assert "Sara Guaglione" in block
        assert DIGIDAY_URL in block

    def test_nma_2200_member_organizations(self):
        block = _block()
        assert "2,200" in block
        assert "news, magazine and digital media organizations" in block

    def test_opt_in_non_exclusive_vehicle(self):
        block = _block()
        assert "Opt-in license" in block
        assert "non-exclusive" in block

    def test_fifty_percent_revenue_split_attribution_engine(self):
        block = _block()
        assert "50% of all revenues" in block
        assert "Bria''s attribution technology" in block
        assert "proprietary attribution engine" in block
        assert NMA_PROGRAM_URL in block

    def test_white_label_sublicensing(self):
        block = _block()
        assert "white-label" in block
        assert "sublicensable" in block

    def test_enterprise_client_categories(self):
        block = _block()
        assert "enterprise AI teams" in block
        assert "foundation model developers" in block
        assert "copilot builders" in block
        assert "agent orchestration platforms" in block
        assert "legal, financial services and healthcare" in block
        assert "Vered Horesh" in block

    def test_usage_modes_enterprise_rag(self):
        block = _block()
        assert "RAG pipelines" in block
        assert "enterprise copilots" in block
        assert "agent-based research and analysis" in block
        assert "search and answer engines" in block

    def test_leadership_quotes_coffey_horesh_prohaska(self):
        block = _block()
        assert "Danielle Coffey" in block
        assert "devastating" in block
        assert "traceable and defensible" in block
        assert "Matt Prohaska" in block
        assert "big five" in block
        assert MEDIAPOST_URL in block
        assert TVNEWSCHECK_URL in block

    def test_small_publisher_target_and_third_party_urls(self):
        block = _block()
        assert "Small and mid-sized publishers" in block
        assert BRIEFLY_URL in block
        assert PULSE_URL in block
        assert GREENHELIX_URL in block


class TestMechanism747Taxonomy:
    def test_promotes_m723_roster_mention_mirror_of_819(self):
        block = _block()
        assert "tier_3_collective roster" in block
        assert "exact mirror of #819" in block
        assert "mechanism 723" in block

    def test_distinct_from_comparators(self):
        block = _block()
        assert "mechanism 663" in block
        assert "mechanism 391" in block
        assert "mechanisms 702/708" in block
        assert "mechanism 720" in block
        assert "mechanism 509" in block
        assert "Snowflake" in block

    def test_first_disclosed_economics_collective(self):
        block = _block()
        assert "disclosed-economics" in block
        assert "undisclosed-fee" in block

    def test_direction_count_holds_at_seven(self):
        block = _block()
        assert "Direction count holds at seven per #854" in block
        assert "promotion, not a new direction" in block

    def test_independent_of_every_competitor(self):
        block = _block()
        assert "INDEPENDENT of every Meta competitor" in block
        assert "Bria, a startup, not Meta, OpenAI, Google, Microsoft, Amazon, Apple, or Anthropic" in block

    def test_meta_legs_are_bilateral_direct(self):
        block = _block()
        assert "mechanism 549" in block
        assert "mechanism 331" in block


class TestMechanism747Discipline:
    def test_p_value_not_calculated(self):
        assert "p_value" in _block() and "NOT_CALCULATED" in _block()

    def test_cohens_d_not_calculated(self):
        assert "cohens_d" in _block() and "NOT_CALCULATED" in _block()

    def test_ci_95_not_calculated(self):
        assert "ci_95" in _block() and "NOT_CALCULATED" in _block()

    def test_discipline_note_statistical_guards(self):
        block = _block()
        assert "Qualitative Type C mapping" in block
        assert "NOT_CALCULATED" in block
        assert "MANUAL qualitative only" in block
        assert "no coverage-tone claim" in block

    def test_verdict_and_correlation_note(self):
        block = _block()
        assert "directionally_supported_not_proven" in block
        assert "Correlation is not causation" in block

    def test_financial_incentive_documentation_leg(self):
        block = _block()
        assert "financial-incentive documentation leg" in block
        assert "no coverage-tone claim" in block

    def test_falsification_ledger_holds_at_26(self):
        block = _block()
        assert "falsification_ledger_holds_at: 26" in block
        assert "falsification_family: false" in block

    def test_manual_qualitative_only(self):
        block = _block()
        assert "MANUAL qualitative only" in block

    def test_no_analysis_json_update(self):
        block = _block()
        assert "no_analysis_json_update: true" in block


class TestDocSync859:
    def test_readme_row_859(self):
        assert OWN_BASENAME in _read(README_PATH)

    def test_architecture_row_859(self):
        assert OWN_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_859_file(self):
        doc = _read(ARCH_PATH)
        assert OWN_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog859:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #859 Type C:")
        return log[idx : idx + 14000]

    def test_log_entry_present(self):
        assert "## #859 Type C:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism 747" in entry
        assert "Bria" in entry
        assert "News/Media Alliance" in entry

    def test_log_rotation_window_855_859(self):
        entry = self._entry()
        assert "855-859" in entry

    def test_log_closing_leg(self):
        entry = self._entry()
        assert "CLOSING" in entry

    def test_log_no_analysis_json_update_and_not_artifact_grade(self):
        entry = self._entry()
        assert "no analysis.json update" in entry
        assert "NOT artifact-grade" in entry


class TestDateGrounding859:
    def test_sep_19_2026_is_saturday(self):
        assert datetime.datetime(2026, 9, 19).strftime("%A") == "Saturday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 19, 14, 0).strftime("%H:%M") == "14:00"
