"""Type C #894 (890-894 window, fifth leg D->E->A->B->C, CLOSING the window):
OpenAI ChatGPT Ads Sep-16-2026 product step-up - Sponsored Agents US test,
Ads Manager AI tooling, HubSpot as first CRM partner, Shopify as first
ecommerce partner (mechanism 768).

EXTENDS mechanism 386 (Type C #386, Aug 30 2026), which documented the
ChatGPT Ads 31-European-market rollout (Aug 19 announcement / Aug 24
rollout; 1B weekly users, 20 percent commercial intent, ad run rate
approaching $1B annual per CFO Friar; static intent-based conversational
placements; agency-partner access at launch). Twenty-eight days later,
OpenAI stepped the product up: (1) Sponsored Agents - a clearly labeled
conversation with a business-sponsored agent users can enter after an ad
click, separate from ChatGPT's independent answers and the original chat,
in US test with select advertisers, no general-availability date;
(2) Ads Manager AI tooling - natural-language campaign
creation/update/analysis, AI-suggested copy and imagery from the landing
page and objective, optional AI text customization adapting copy to
conversation context with automatic translation; (3) HubSpot as first CRM
partner - connect a ChatGPT Ads account inside HubSpot, create ads, track
performance, follow up on leads without leaving HubSpot (HubSpot parallel
release naming Brian Landsman of OpenAI and Duncan Lennox of HubSpot;
$750 ad spend match for new accounts opened by Sep 30); (4) Shopify as
first ecommerce partner - free ChatGPT Ads app in the Shopify App Store
for US merchants from Sep 16 (listing dates release to Sep 3 2026),
products pre-integrated via Shopify Catalog, inventory sync, Shopify
pixel and conversion events, international rollout in ChatGPT Ads markets
beginning Sep 23. Corroborated by Reuters (Sep 16, Anzar Mehraj,
Bengaluru), unite.ai, ppc.land, and dev.to.

Incentive geometry: from static placements to agentic sponsored
conversations (the ad becomes a merchant representative inside ChatGPT)
and from media buy to advertiser-workflow capture (OpenAI touches the
merchant's catalog, pixel, conversion events, lead pipeline). The dual
dependency for shopping-content publishers extends: OpenAI is licensing
payer AND ad competitor AND now agentic-commerce competitor, against
Meta's $0 to Conde Nast (mechanism 386 finding, carried).

Verdict directionally_supported_not_proven. MANUAL / qualitative only;
engine NOT run per the Aug 28 2026 standing rule; no tone scores; no
significance claimed. NOT a falsification-family member: a
product/documentation leg with no coverage-tone pair; falsification
ledger holds at 29; no analysis.json update. Novelty verified pre-commit
(zero test_type_c_894 files; no 'Type C #894' in git log; max numeric
mechanism_id 767 in-tree; zero underscore-form 768 keys by designed
keying per #715; zero literal mechanism_768/mechanism-768 repo-wide;
zero 'sponsored agent' hits repo-wide; all 4 source URLs zero-hit);
count_stats gate (45831/1221; delta +45/+1 = the #894 file exactly, venv
python); 890-894 window fifth leg D->E->A->B->C, CLOSING the window
(anchor patched post-commit per #565); the concurrent Type C #884
(competitor-entities.yaml m762) remains uncommitted and untouched -
Sep 21 2026 07:00 PDT.
"""

import subprocess
import re
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_c_894_openai_sponsored_agents_agentic_ad_tool_rollout_sep21_7am.py"
MECH_KEY = "openai_sponsored_agents_agentic_ad_rollout_sep2026"
M_ID = 768
ITER = 894
TYPE_LETTER = "C"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_768"
NEXT_ID_MARKER = "mechanism" + "_769"
NEXT_ID_NUMERIC = "mechanism_id: 769"
EXPECTED_ORDER = [("C", "894"), ("B", "893"), ("A", "892"), ("E", "891"), ("D", "890")]
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "bab6b4b9be07b69ed58c75452b3266a97f06c01c"
EXPECTED_TEST_COUNT = 45
POST_COMMIT_TESTS = 45831
POST_COMMIT_FILES = 1221

EXPECTED_URLS = [
    "https://www.reuters.com/business/media-telecom/openai-tests-advertiser-sponsored-agents-expands-ai-tools-chatgpt-ads-2026-09-16/",
    "https://www.unite.ai/openai-tests-sponsored-agents-and-rolls-out-ai-tools-for-chatgpt-ads/",
    "https://ppc.land/openai-lets-advertisers-run-chatgpt-ads-from-hubspot-and-shopify/",
    "https://dev.to/alifar/openai-tests-sponsored-agents-for-chatgpt-ads-with-hubspot-and-shopify-integrations-34gm",
]


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _profiles_text() -> str:
    return (_repo_root() / "profiles" / "wired.yaml").read_text()


def _block() -> str:
    text = _profiles_text()
    start = text.index(MECH_KEY)
    end = text.index("\nvittoria_elliott_cross_entity_aug30:")
    return text[start:end]


def _mech() -> dict:
    d = yaml.safe_load(_profiles_text())
    return d[MECH_KEY]


def _corpus_ids() -> list:
    ids = []
    for p in (_repo_root() / "profiles").rglob("*.yaml"):
        for m in re.finditer(r"mechanism_id:\s*(\d+)", p.read_text(errors="ignore")):
            ids.append(int(m.group(1)))
    return ids


def _repo_grep(needle: str, roots=("profiles", "tests")) -> list:
    hits = []
    root = _repo_root()
    for r in roots:
        for p in (root / r).rglob("*"):
            if p.is_file() and p.suffix in (".py", ".yaml", ".md", ".json"):
                try:
                    if needle in p.read_text(errors="ignore"):
                        hits.append(str(p.relative_to(root)))
                except OSError:
                    pass
    return hits


def _git(*args: str) -> str:
    return subprocess.run(
        ["git", *args],
        cwd=_repo_root(),
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def _git_log_mains(qualifier: str) -> dict:
    out = _git("log", "--all", "--format=%H %s", "--grep", qualifier)
    mains = {}
    for line in out.splitlines():
        if not line.strip():
            continue
        sha, _, subject = line.partition(" ")
        if "Type C #894" in subject:
            mains[sha] = subject
    return mains


def _window(n: int = 40) -> list:
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


def _iteration_log_head() -> str:
    return (_repo_root() / "iteration-log.md").read_text()[:12000]


class TestNovelty894:
    @pytest.mark.anchor
    def test_single_test_type_c_894_file(self):
        files = list((_repo_root() / "tests").glob("test_type_c_894*"))
        assert files == [Path(__file__)], (
            "exactly one test_type_c_894 file (this one) must exist"
        )

    @pytest.mark.anchor
    def test_type_c_894_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-commit. Novelty was verified pre-commit by shell
        # greps (zero test_type_c_894 files, no #894 in git log, max numeric
        # mechanism_id 767 in-tree, zero underscore-form 768 keys, zero
        # literal mechanism_768/mechanism-768, zero 'sponsored agent' hits,
        # all 4 source URLs zero-hit); this test pins that no duplicate
        # #894 main commit ever appears.
        mains = _git_log_mains("Type C #894: OpenAI Sep-16-2026")
        assert len(mains) == 1, f"exactly one Type C #894 main commit, got {mains}"
        assert ANCHORED_SHA in mains, (
            "patched SHA must match a real Type C #894 main commit"
        )

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "ANCHORED_SHA must be patched to the real main-commit SHA"
        assert len(ANCHORED_SHA) == 40


class TestRotationCycleGuard894:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    @pytest.mark.rotation
    def test_window_is_890_894_fifth_leg(self):
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"890-894 window fifth leg D->E->A->B->C: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    @pytest.mark.rotation
    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    @pytest.mark.rotation
    def test_predecessor_is_type_b_893_committed(self):
        # The #893 run committed as ee0f04e (+ followups); it is the real
        # fourth leg of the window.
        window = _window()
        assert window[1] == ("B", "893"), (
            f"immediate predecessor must be Type B #893, got {window[1]}"
        )

    @pytest.mark.rotation
    def test_concurrent_884_still_in_flight_not_in_subjects(self):
        # The concurrent Type C #884 run (competitor-entities.yaml m762)
        # remains uncommitted. Iteration numbers follow the rotation
        # schedule, not commit order, so the subject sequence must read
        # 894 -> 893 -> 892 -> 891 -> 890 with the in-flight 884 skipped.
        subjects = _git("log", "-25", "--format=%s", "--no-merges").splitlines()
        nums = []
        for line in subjects:
            m = re.match(r"Type [A-E] #(\d+)", line)
            if m and (not nums or nums[-1] != m.group(1)):
                nums.append(m.group(1))
        assert nums[:5] == ["894", "893", "892", "891", "890"], nums[:5]
        assert "884" not in nums

    @pytest.mark.rotation
    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type C #894: OpenAI Sep-16-2026")
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        newest_sha = next(iter(mains))
        assert newest_sha == ANCHORED_SHA, mains


class TestMechanism768Content:
    def test_block_key_exists_in_wired_profile(self):
        assert MECH_KEY in _profiles_text()

    def test_mechanism_id_768(self):
        assert _mech()["mechanism_id"] == M_ID

    def test_iteration_type_and_time_pdt(self):
        m = _mech()
        assert m["iteration"] == ITER
        assert m["iteration_type"] == TYPE_LETTER
        assert m["iteration_time"] == "2026-09-21 07:00 PT"
        assert m["date_analyzed"] == "2026-09-21"

    def test_publication_parent_competitor_fields(self):
        m = _mech()
        assert m["publication"] == "WIRED"
        assert "Conde Nast" in m["parent_company"]
        assert m["competitor"] == "OpenAI"

    def test_extends_386_connects_to(self):
        m = _mech()
        assert m["connects_to"] == [386]
        assert "386" in m["type_c_focus"]
        assert "EXTENDS mechanism 386" in m["focus"]

    def test_sponsored_agents_facts(self):
        block = _block()
        assert "Sponsored Agents" in block
        assert "clearly labeled" in block
        assert "separate from ChatGPT" in block
        assert "select advertisers" in block
        assert "no general-availability date announced" in block

    def test_hubspot_first_crm_facts(self):
        block = _block()
        assert "HubSpot" in block
        assert "first CRM partner" in block
        assert "Brian Landsman" in block
        assert "750-dollar ad spend match" in block

    def test_shopify_first_ecommerce_facts(self):
        block = _block()
        assert "Shopify" in block
        assert "first ecommerce partner" in block
        assert "Shopify Catalog" in block
        assert "Shopify pixel" in block

    def test_sep_23_international_rollout(self):
        block = _block()
        assert "Sep 23" in block
        assert "Sep 3 2026" in block

    def test_source_urls_present(self):
        block = _block()
        for url in EXPECTED_URLS:
            assert url in block, f"expected source URL missing: {url}"

    def test_confounders_ranked_strong_first(self):
        block = _block()
        strong_pos = block.index("[STRONG]")
        moderate_pos = block.index("[MODERATE]")
        assert strong_pos < moderate_pos, "confounders must be ranked strong-first"

    def test_counterevidence_present(self):
        block = _block()
        assert "counter_evidence" in block
        assert "labeling discipline" in block

    def test_statistical_discipline_qualitative_only(self):
        sd = _mech()["statistical_discipline"]
        assert sd["qualitative_only"] is True
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["engine_run"] is False
        assert sd["verdict"] == "directionally_supported_not_proven"

    def test_no_coverage_tone_claim(self):
        assert _mech()["no_coverage_tone_claim"] is True

    def test_designed_keying_no_underscore_768_in_block(self):
        # The block must not carry the literal underscore-form 768 key;
        # mechanism numbering travels in the mechanism_id field only
        # (designed keying per #715).
        assert MECH_ID_MARKER not in _block(), (
            "block must not contain the literal underscore-form 768 key"
        )

    def test_research_method_rejections(self):
        block = _block()
        assert "research_method" in block
        assert "zero test_type_c_894 files" in block
        assert "no Type C #894 in git log" in block
        assert "max numeric mechanism_id 767 pre-commit" in block


class TestSupersession894:
    def test_max_numeric_id_is_768(self):
        assert max(_corpus_ids()) == 768, (
            "corpus now maxes at 768: supersedes #893 max-767, #892 max-766, "
            "and #891 max-765 sweeps by design"
        )

    def test_zero_underscore_769_keys_repo_wide(self):
        assert _repo_grep(NEXT_ID_MARKER) == [], (
            "no underscore-form 769 keys anywhere by designed keying per #715"
        )

    def test_zero_numeric_769_keys_in_profiles(self):
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == [], (
            "no numeric 769 mechanism keys in the corpus"
        )

    def test_no_second_894_block_key_variant(self):
        # The block key must appear exactly once as a top-level YAML key;
        # any second occurrence is a real duplication.
        keys = re.findall(r"^" + MECH_KEY + r":$", _profiles_text(), re.M)
        assert len(keys) == 1, keys

    def test_893_max_767_sweep_superseded_by_design(self):
        assert max(_corpus_ids()) == 768, (
            "#893 max-767 sweep is superseded by design"
        )

    def test_892_max_766_sweep_superseded_by_design(self):
        assert max(_corpus_ids()) == 768, (
            "#892 max-766 sweep is superseded by design"
        )

    def test_891_max_765_sweep_superseded_by_design(self):
        assert max(_corpus_ids()) == 768, (
            "#891 max-765 sweep is superseded by design"
        )

    def test_concurrent_884_change_not_in_this_commit_scope(self):
        # The concurrent Type C #884 block in competitor-entities.yaml stays
        # uncommitted and is NOT part of this run's scope.
        status = _git("status", "--short")
        assert "profiles/competitor-entities.yaml" in status, (
            "concurrent #884 change must remain uncommitted in the working tree"
        )

    def test_no_analysis_json_update(self):
        assert _mech()["no_analysis_json_update"] is True


class TestLedger894:
    def test_twenty_ninth_member_form_present_once(self):
        hits = _repo_grep("TWENTY-NINTH falsification-family member", roots=("profiles",))
        assert len(hits) == 1, (
            f"exactly one TWENTY-NINTH member-form in profiles/, got {hits}"
        )

    def test_no_thirtieth_member_form(self):
        hits = _repo_grep("THIRTIETH falsification-family member", roots=("profiles",))
        assert hits == [], (
            f"zero THIRTIETH member-forms in profiles/ (negative-guard strings only), got {hits}"
        )

    def test_block_states_ledger_holds_at_29(self):
        assert "holds at 29" in _block()

    def test_not_a_falsification_member(self):
        block = _block()
        assert "NOT a falsification-family member" in block


class TestDocSync894:
    def test_readme_test_count_gate(self):
        readme = (_repo_root() / "README.md").read_text()
        assert f"| Tests | {POST_COMMIT_TESTS} |" in readme
        assert f"Across {POST_COMMIT_FILES} test files" in readme

    def test_readme_type_c_table_row(self):
        assert TEST_BASENAME in (_repo_root() / "README.md").read_text()

    def test_architecture_test_count_gate(self):
        arch = (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()
        assert str(POST_COMMIT_TESTS) in arch and str(POST_COMMIT_FILES) in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in (_repo_root() / "docs" / "ARCHITECTURE.md").read_text()


class TestIterationLog894:
    def test_log_captures_iteration_894(self):
        head = _iteration_log_head()
        assert "#894 Type C:" in head
        assert "07:00 PDT" in head
        assert "m768" in head

    def test_log_states_890_894_window(self):
        assert "890-894" in _iteration_log_head()

    def test_log_closes_window(self):
        head = _iteration_log_head()
        assert "CLOSING" in head

    def test_log_notes_893_committed_predecessor(self):
        head = _iteration_log_head()
        assert "#893" in head
        assert "ee0f04e" in head
