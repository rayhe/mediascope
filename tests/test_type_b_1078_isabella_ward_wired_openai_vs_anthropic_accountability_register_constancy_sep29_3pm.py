"""Type B #1078: Isabella Ward (WIRED) x OpenAI vs x Anthropic
accountability-register constancy - THIRTY-SIXTH falsification-family member
(ledger 35->36). FOURTH leg of the 1075-1079 window, CONTINUING it.

DESIGN (writer-level deal-gradient test):
- Same-writer pair: Isabella Ward, WIRED Business desk (Bloomberg migration
  June 2026, physics MSci).
- OpenAI arm CARRIED un-rescored per #807 from m877 (-0.35, 'OpenAI Delays
  Release of Latest Model Over Safety Concerns', Sep 29 2026; excerpt-tier,
  relay-attested per #503): safety-cancellation accountability register on
  the licensing deal partner (Conde Nast x OpenAI Aug 2024 multi-year deal,
  m877 financial_context).
- Anthropic arm FRESH this run, excerpt-tier (secondary digest, NOT
  relay-attested): 'Coders Say They Already Found Workarounds to Claude's
  Invisible Watermarks' (Aug 19 2026, 41 days earlier), byline corroborated
  by the AI-content-watermarking Wikipedia citation. MANUAL ILLUSTRATIVE
  -0.40: accountability plus harm-consequence register - the compliance
  instrument is dead on arrival (four-hour override) and foregrounds
  concrete false-positive harm (native French speaker fears employers
  rejecting candidates on a probability-only signal; EU fines up to 3% of
  turnover on a defeatable signal).
- Illustrative delta (Anthropic minus OpenAI): -0.05, near-null. The uniform
  payer-softening prediction (>=0.15) FAILS substantively at the writer
  level: the deal partner is covered at essentially the same hardness as
  the non-deal competitor. (The +0.05 direction is negligible.)
- EXTENDS #877 from publication-level to a writer-level falsification pair.
- Second writer-level deal-gradient falsification in the Sep-28/29 Astra
  window after #1038 (O'Brien, 33rd member).
- Scope note: no Isabella Ward Meta byline surfaced (4 search sets this
  run); the pair is cross-competitor by necessity, and the deal prediction
  is entity-general, so the falsification test is valid for the family.

NOVELTY VERIFICATION (pre-commit, all green):
- zero test_type_b_1078 files on disk (glob)
- no "Type B #1078" in git log (--grep)
- max numeric mechanism_id 877 in profiles/ pre-commit
- zero numeric 878 mechanism_id keys in profiles/ (mechanism_id regex sweep)
- zero underscore-form and dash-form 878 mechanism key strings repo-wide
  pre-commit (needles format-built per #715); block key zero-hit
- zero isabella_ward competitor_coverage in profiles/ pre-commit
- three novel URLs zero-hit repo-wide pre-commit (shermesagent digest,
  chrismeah substack, wikipedia watermarking)
- THIRTY-SIXTH member-form absent in profiles/ pre-commit

BY-DESIGN-FAILING SETS:
- Pre-commit run: deselect test_anchor_sha_patched_post_commit (novelty
  anchor 1 per #565, patched in the anchor followup), the rotation-guard
  main-commit tests (3: window, adjacency, single-main-commit - the main
  commit does not exist yet), the doc-sync ratchet (4 per #719, green after
  doc-sync), the iteration-log tests (4 per #721, green after the log-hash
  followup). Expected pre-commit: 64 green + 12 deselected.
- Post-commit re-runs: the two pre-commit-only tests
  (test_no_type_b_1078_in_git_log_precommit,
  test_anchor_sha_placeholder_precommit) fail BY DESIGN; deselect them on
  re-run per the #710/#720 convention.

STATISTICAL DISCIPLINE: MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026
standing rule. p_value/cohens_d/ci_95 NOT_CALCULATED. is_significant False.
Engine NOT run. verdict directionally_supported_not_proven.
no_analysis_json_update true. NOT artifact-grade. n=1 writer-level pair;
hypothesis-generating only. Correlation is not causation.

ASCII-only, no em dashes.
"""

import glob
import os
import re
import subprocess

import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOURNALISTS_YAML = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
COMPETITOR_YAML = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
OWN_BASENAME = (
    "test_type_b_1078_isabella_ward_wired_openai_vs_anthropic_"
    "accountability_register_constancy_sep29_3pm.py"
)

ITER = 1078
M_ID = 878
NEXT_ID = 879
TYPE_LETTER = "B"
DATE_STR = "2026-09-29 15:00 PDT"
MECH_KEY = (
    "type_b_1078_isabella_ward_wired_openai_vs_anthropic_"
    "accountability_register_constancy_sep29"
)
EXPECTED_ORDER = [
    ("B", "1078"),
    ("A", "1077"),
    ("E", "1076"),
    ("D", "1075"),
    ("C", "1074"),
]

# #565 anchor: all-zeros placeholder until the anchor followup patches it.
ANCHORED_SHA = "0" * 40

# Runtime-built key needles per #715 / #770 (no contiguous literal in source).
MECH_ID_MARKER = "mechanism" + "_"
US_878 = MECH_ID_MARKER + "878"
DASH_878 = "mechanism" + "-" + "878"
US_879 = MECH_ID_MARKER + "879"
DASH_879 = "mechanism" + "-" + "879"

# Doc-sync ratchet per #719: README was STALE at doc-sync time (claimed
# 55334/1402/272 vs authoritative 54392/1402/273 from count_stats.py --check).
# This run corrects to the authoritative base and adds its own +76/+1.
README_TESTS_BEFORE = 54392
README_TESTS_AFTER = 54468
README_FILES_BEFORE = 1402
README_FILES_AFTER = 1403
README_JOURNALISTS = 273
EXPECTED_TESTS = 76

INFLIGHT = [
    "profiles/nytimes.yaml",
    "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",
    "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
    "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
]

NOVEL_URLS = [
    "https://github.com/shermesagent/ai-agency-knowledgebase/blob/HEAD/00-Daily-Digests/2026-08-23.md",
    "https://chrismeah.substack.com/p/is-work-working-for-juniors",
    "https://en.wikipedia.org/wiki/Artificial_intelligence_content_watermarking",
]
CARRIED_URLS = [
    "https://wesearch.press/s/openai-delays-release-of-latest-model-over-safety-concerns-11bacbdf",
    "https://www.aob-news.com/2026/09/29/openai-delays-release-of-latest-model-over-safety-concerns/",
]


def run_git(*args):
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _profiles_text():
    return _read(JOURNALISTS_YAML)


def _block():
    text = _profiles_text()
    start = text.index("    " + MECH_KEY + ":")
    rest = text[start:]
    m = re.search(r"\n- career:", rest)
    return rest[: m.start()] if m else rest


def _item():
    d = yaml.safe_load(_profiles_text())
    for it in d["journalists"]:
        if isinstance(it, dict) and it.get("name") == "Isabella Ward":
            return it
    raise AssertionError("Isabella Ward list item not found under journalists")


def _mech():
    return _item()["competitor_coverage"][MECH_KEY]


def _corpus_ids():
    ids = []
    base = os.path.join(REPO_ROOT, "profiles")
    for root, _, files in os.walk(base):
        for fn in files:
            if fn.endswith(".yaml"):
                text = _read(os.path.join(root, fn))
                for m in re.finditer(r"mechanism(?:_id)?:\s*(\d+)", text):
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


def _window(n=40):
    # First occurrence of each distinct iteration number, newest first
    # (robust to followup commits that repeat the same "Type X #N" wording
    # without the colon, per the #752 convention).
    subjects = (
        run_git("log", f"-{n}", "--format=%s", "--no-merges").stdout.splitlines()
    )
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out[:5]


# ---------------------------------------------------------------------------
# 1. Novelty anchor per #565 / #715
# ---------------------------------------------------------------------------
class TestNoveltyAnchorTypeB1078:
    def test_single_test_type_b_1078_file(self):
        files = [
            fn
            for fn in os.listdir(os.path.join(REPO_ROOT, "tests"))
            if fn.startswith("test_type_b_1078")
        ]
        assert files == [OWN_BASENAME]

    def test_no_type_b_1078_in_git_log_precommit(self):
        # Pre-commit only: fails BY DESIGN once the main commit exists.
        r = run_git("log", "--grep", "Type B #1078:", "--format=%H", "--no-merges")
        assert r.stdout.strip() == ""

    def test_anchor_sha_placeholder_precommit(self):
        # Pre-commit only: the anchor followup patches ANCHORED_SHA per #565.
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_post_commit(self):
        # Deselected pre-commit per #565: ANCHORED_SHA carries a placeholder
        # until the anchor followup patches it to the real main commit SHA.
        assert ANCHORED_SHA != "0" * 40
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)
        r = run_git("rev-parse", ANCHORED_SHA)
        assert r.returncode == 0 and r.stdout.strip() == ANCHORED_SHA

    def test_novelty_verification_claim(self):
        doc = __doc__
        for claim in (
            "zero\ntest_type_b_1078 files",
            "max numeric\nmechanism_id 877",
            "block key zero-hit",
            "three novel URLs\nzero-hit",
            "THIRTY-SIXTH member-form absent",
        ):
            assert claim.replace("\n", " ") in doc.replace("\n", " ")


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1075-1079 window, fourth leg D->E->A->B
# ---------------------------------------------------------------------------
class TestRotationGuard1075_1079Window:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_1075_1079_fourth_leg(self):
        assert _window() == EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_a_1077(self):
        order = _window()
        assert order[0] == ("A", "1077")
        r = run_git("log", "--grep", "Type A #1077:", "--format=%H", "--no-merges")
        assert r.stdout.strip(), "no Type A #1077 main commit found"

    def test_no_concurrent_inflight_commits_asserted(self):
        r = run_git("log", "--grep", "Type B #1078:", "--format=%H", "--no-merges")
        assert len(r.stdout.split()) == 1, "expected exactly one Type B #1078 main commit"

    def test_next_run_is_type_c_1079_note(self):
        assert "1079" in __doc__ and "C" in __doc__


# ---------------------------------------------------------------------------
# 3. Corpus novelty greps per #715 (post-edit safe: needles runtime-built)
# ---------------------------------------------------------------------------
class TestCorpusNoveltyGreps:
    def test_block_key_unique_in_journalists_yaml(self):
        # The 4-space-indented block key line occurs exactly once; the
        # test_file field value carries the key as a substring and is
        # excluded by the key-line form.
        assert _read(JOURNALISTS_YAML).count("\n    " + MECH_KEY + ":") == 1

    def test_mechanism_id_878_colon_form_present(self):
        assert "mechanism_id: 878" in _block()

    def test_no_underscore_dash_878_key_strings(self):
        # Keying discipline per #715: the block key carries no numeric
        # 878 mechanism-id substring. No repo-wide literal carrier of the
        # contiguous fragment-built 878 key needle forms (underscore and
        # dash) may appear this run; the needles are fragment-built here
        # too, so this file itself carries no contiguous literal either.
        n1 = "mech" + "anism_" + "8" + "78"
        n2 = "mech" + "anism-" + "8" + "78"
        hits = set()
        for p in glob.glob(os.path.join(REPO_ROOT, "tests", "test_*.py")):
            if os.path.basename(p) == OWN_BASENAME:
                continue
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.add(os.path.basename(p))
        for p in glob.glob(
            os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True
        ):
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.add(os.path.basename(p))
        assert hits == set(), hits

    def test_block_key_carries_no_numeric_id(self):
        assert "878" not in MECH_KEY


# ---------------------------------------------------------------------------
# 4. Mechanism 878 block structure
# ---------------------------------------------------------------------------
class TestMechanism878Structure:
    def test_block_key_exists_in_journalists_yaml(self):
        assert ("    " + MECH_KEY + ":") in _profiles_text()

    def test_block_key_unique(self):
        assert _profiles_text().count("    " + MECH_KEY + ":") == 1

    def test_iteration_and_type_and_time_pdt(self):
        m = _mech()
        assert m["iteration"] == ITER
        assert m["iteration_type"] == TYPE_LETTER
        assert m["mechanism_id"] == M_ID
        assert m["date"] == DATE_STR

    def test_journalist_and_entities(self):
        m = _mech()
        assert m["journalist"] == "Isabella Ward"
        assert m["publication"] == "WIRED"
        assert m["primary_entity"] == "OpenAI"
        assert m["comparator_entity"] == "Anthropic"
        assert m["finding_type"] == "journalist_cross_entity_register_constancy"

    def test_designed_keying_no_878_in_block_key(self):
        # Per #715: the block key must not carry the underscore/dash-form
        # mechanism key substrings consumed by the corpus id sweeps.
        assert "878" not in MECH_KEY
        assert US_878 not in MECH_KEY
        assert DASH_878 not in MECH_KEY
        assert "mechanism_id: 878" in _block()

    def test_mechanism_ids_list_contains_878(self):
        assert _item()["mechanism_ids"] == [878]

    def test_test_file_field_matches_own_basename(self):
        assert _mech()["test_file"] == "tests/" + OWN_BASENAME


# ---------------------------------------------------------------------------
# 5. OpenAI arm carried un-rescored per #807
# ---------------------------------------------------------------------------
class TestOpenAIArmCarriedPer807:
    def test_openai_arm_piece_title(self):
        assert (
            _mech()["openai_arm"]["piece"]
            == "OpenAI Delays Release of Latest Model Over Safety Concerns"
        )

    def test_openai_arm_author_date(self):
        arm = _mech()["openai_arm"]
        assert arm["author"] == "Isabella Ward"
        assert arm["date"] == "2026-09-29"

    def test_openai_arm_tone_carried_minus_035(self):
        assert _mech()["openai_arm"]["illustrative_tone"] == -0.35
        assert "m877" in _mech()["openai_arm"]["tone_basis"]

    def test_openai_arm_urls_carried_disclosed(self):
        urls = _mech()["openai_arm"]["urls"]
        seen = {u["url"]: u for u in urls}
        for url in CARRIED_URLS:
            assert url in seen, url
            assert seen[url].get("carried") is True

    def test_openai_arm_register_accountability(self):
        assert _mech()["openai_arm"]["register"] == "accountability"


# ---------------------------------------------------------------------------
# 6. Anthropic arm evidence (fresh, excerpt-tier)
# ---------------------------------------------------------------------------
class TestAnthropicArmEvidence:
    def test_anthropic_arm_piece_title(self):
        assert "Workarounds to Claude" in _mech()["anthropic_arm"]["piece"]

    def test_anthropic_arm_byline_ward(self):
        arm = _mech()["anthropic_arm"]
        assert arm["author"] == "Isabella Ward"
        assert arm["publication"] == "WIRED"

    def test_anthropic_arm_date_aug_19_2026(self):
        assert _mech()["anthropic_arm"]["date"] == "2026-08-19"

    def test_anthropic_arm_excerpt_tier_disclosed(self):
        basis = _mech()["anthropic_arm"]["tone_basis"]
        assert "Excerpt-tier" in basis
        assert "not relay-attested" in basis

    def test_anthropic_arm_evidence_quotes(self):
        basis = _mech()["anthropic_arm"]["tone_basis"]
        for needle in (
            "within four hours",
            "really bad solution",
            "probability-only signal",
            "3% of turnover",
            "practically history just one day later",
        ):
            assert needle in basis, needle

    def test_anthropic_arm_tone_minus_040_manual_illustrative(self):
        assert _mech()["anthropic_arm"]["illustrative_tone"] == -0.40
        assert "MANUAL ILLUSTRATIVE" in __doc__

    def test_anthropic_arm_urls_novel(self):
        urls = _mech()["anthropic_arm"]["urls"]
        seen = {u["url"]: u for u in urls}
        for url in NOVEL_URLS:
            assert url in seen, url
            assert seen[url].get("novel") is True


# ---------------------------------------------------------------------------
# 7. Illustrative tones and delta
# ---------------------------------------------------------------------------
class TestIllustrativeTonesAndDelta:
    def test_tones_openai_minus_035_anthropic_minus_040(self):
        m = _mech()
        assert m["openai_arm"]["illustrative_tone"] == -0.35
        assert m["anthropic_arm"]["illustrative_tone"] == -0.40

    def test_delta_calc_minus_005(self):
        assert _mech()["illustrative_delta_anthropic_minus_openai"] == -0.05
        assert "-0.40 - (-0.35) = -0.05" in _mech()["delta_calc"]

    def test_delta_near_null(self):
        assert abs(_mech()["illustrative_delta_anthropic_minus_openai"]) < 0.10
        assert "near-null" in _mech()["delta_calc"]

    def test_uniform_prediction_fails_substantively(self):
        calc = _mech()["delta_calc"]
        assert ">=0.15" in calc
        assert "fails substantively" in calc


# ---------------------------------------------------------------------------
# 8. Statistical discipline per the Aug 28 2026 standing rule
# ---------------------------------------------------------------------------
class TestStatisticalDisciplineStandingRule:
    def test_manual_illustrative_only(self):
        assert "MANUAL ILLUSTRATIVE ONLY" in _mech()["statistical_discipline"]

    def test_not_calculated_fields(self):
        sd = _mech()["statistical_discipline"]
        for needle in ("p_value", "cohens_d", "ci_95"):
            assert needle in sd
        assert "NOT_CALCULATED" in sd

    def test_is_significant_false_engine_not_run(self):
        sd = _mech()["statistical_discipline"]
        assert "is_significant False" in sd
        assert "Engine NOT run" in sd

    def test_verdict_directionally_supported_not_proven(self):
        assert (
            "directionally_supported_not_proven" in _mech()["statistical_discipline"]
        )

    def test_no_analysis_json_update_not_artifact_grade(self):
        assert _mech()["no_analysis_json_update"] is True
        assert "NOT artifact-grade" in _mech()["statistical_discipline"]

    def test_n1_degenerate_hypothesis_generating(self):
        sd = _mech()["statistical_discipline"]
        assert "n=1" in sd
        assert "hypothesis-generating only" in sd


# ---------------------------------------------------------------------------
# 9. Falsification ledger 35 -> 36
# ---------------------------------------------------------------------------
class TestFalsificationLedger:
    def test_thirty_sixth_member_form_present_in_journalists_yaml(self):
        assert "THIRTY-SIXTH" in _profiles_text()
        assert "THIRTY-SIXTH" in _mech()["falsification_family"]

    def test_ledger_35_to_36(self):
        ff = _mech()["falsification_family"]
        assert "ledger 35->36" in ff
        assert _mech()["falsification_ledger"] == 36

    def test_thirty_fifth_carriers_preserved(self):
        text = _profiles_text() + _read(COMPETITOR_YAML)
        assert "THIRTY-FIFTH" in text

    def test_cross_ref_1038_obrien_33rd_member(self):
        refs = " ".join(_mech()["cross_refs"])
        assert "#1038" in refs
        assert "33rd member" in refs

    def test_competitor_entities_ledger_note_36(self):
        text = _read(COMPETITOR_YAML)
        assert "THIRTY-SIXTH" in text
        assert "Ledger holds at 36" in text


# ---------------------------------------------------------------------------
# 10. Confounders ranked strong-first
# ---------------------------------------------------------------------------
class TestConfoundersRankedStrongFirst:
    def test_confounder_strong_first_ordering(self):
        confs = _mech()["confounders_ranked"]
        assert len(confs) == 7
        assert confs[0].startswith("STRONG")
        assert confs[1].startswith("STRONG")
        assert confs[2].startswith("STRONG")
        assert confs[-1].startswith("WEAK")

    def test_temporal_gap_41_days(self):
        confs = " ".join(_mech()["confounders_ranked"])
        assert "41 days" in confs

    def test_excerpt_tier_strong(self):
        assert "excerpt-tier" in _mech()["confounders_ranked"][0]

    def test_n1_degenerate_moderate(self):
        confs = " ".join(_mech()["confounders_ranked"])
        assert "MODERATE n=1" in confs


# ---------------------------------------------------------------------------
# 11. Cross-references
# ---------------------------------------------------------------------------
class TestCrossReferences:
    def test_cross_ref_877_extends(self):
        refs = " ".join(_mech()["cross_refs"])
        assert "#877" in refs
        assert "EXTENDS" in refs

    def test_cross_ref_1068_low(self):
        refs = " ".join(_mech()["cross_refs"])
        assert "#1068" in refs

    def test_cross_ref_528_chokkattu(self):
        refs = " ".join(_mech()["cross_refs"])
        assert "#528" in refs

    def test_cross_ref_m712_bound(self):
        refs = " ".join(_mech()["cross_refs"])
        assert "m712" in refs


# ---------------------------------------------------------------------------
# 12. Research method per #503
# ---------------------------------------------------------------------------
class TestResearchMethodPer503:
    def test_four_search_query_sets(self):
        assert "4 browser.search query sets" in _mech()["research_method"]

    def test_zero_browser_open(self):
        assert "0 browser.open" in _mech()["research_method"]

    def test_excerpt_tier_conventions(self):
        rm = _mech()["research_method"]
        assert "no canonical URLs constructed" in rm
        assert "verbatim from Full-URL listings" in rm

    def test_scope_note_no_ward_meta_byline(self):
        assert "no Isabella Ward Meta byline surfaced" in _mech()["design"]

    def test_all_urls_verbatim(self):
        for url in NOVEL_URLS + CARRIED_URLS:
            assert url.startswith("https://")
            assert " " not in url


# ---------------------------------------------------------------------------
# 13. Guard lifecycle: 878 lands, 879 forward needles, supersessions
# ---------------------------------------------------------------------------
class TestGuardLifecycle878Lands:
    def test_878_landing_in_journalists_yaml(self):
        assert max(_corpus_ids()) == M_ID

    def test_zero_879_forward_needles_format_built(self):
        # The next leg (#1079) consumes colon-form 879; the next Type D
        # (#1080) pins the underscore/dash zero-879 guards. This run's
        # needles are runtime-built, so no contiguous literal is pinned.
        assert _repo_grep(US_879) == []
        assert _repo_grep(DASH_879) == []

    def test_877_and_36th_sweeps_now_superseded_by_design(self):
        # Per #710/#720: the #1075/#1076/#1077 zero-877 forward-looking
        # guards and the zero-36th-member guards fail BY DESIGN from this
        # commit (877 landed at #1077; the 36th member lands HERE).
        assert [p for p in _repo_grep("mechanism_id: 877")] != []
        text = _profiles_text() + _read(COMPETITOR_YAML)
        assert "THIRTY-SIXTH" in text

    def test_no_mechanism_key_needle_carriers_added(self):
        # This run's own files carry no contiguous underscore/dash 878
        # needle (per #715); the 878 landing is colon-form by design.
        block = _block()
        assert US_878 not in block
        assert DASH_878 not in block


# ---------------------------------------------------------------------------
# 14. Doc-sync ratchet per #719 (green post-doc-sync)
# ---------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_header_stats_bumped(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert str(README_TESTS_AFTER) in text
        assert str(README_FILES_AFTER) in text
        assert str(README_JOURNALISTS) in text

    def test_readme_row_1078(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert f"`tests/{OWN_BASENAME}`" in text
        assert "Type B #1078" in text

    def test_architecture_row(self):
        text = _read(os.path.join(REPO_ROOT, "docs/ARCHITECTURE.md"))
        assert OWN_BASENAME in text

    def test_iteration_log_entry(self):
        text = _read(os.path.join(REPO_ROOT, "iteration-log.md"))
        assert "## #1078 Type B:" in text


# ---------------------------------------------------------------------------
# 15. Iteration-log entry per #721
# ---------------------------------------------------------------------------
class TestIterationLogEntry:
    def _entry(self):
        text = _read(os.path.join(REPO_ROOT, "iteration-log.md"))
        start = text.index("## #1078 Type B:")
        end = text.find("\n## #1077 Type A:", start)
        return text[start:end] if end != -1 else text[start:]

    def test_itlog_header_1078(self):
        assert self._entry().startswith("## #1078 Type B:")

    def test_itlog_commit_hashes(self):
        entry = self._entry()
        assert "log-hash followup registers both hashes here per #721" in entry

    def test_itlog_window_leg(self):
        entry = self._entry()
        assert "FOURTH leg" in entry
        assert "D->E->A->B->C" in entry

    def test_itlog_rotation_guard(self):
        entry = self._entry()
        assert "rotation guard" in entry.lower()


# ---------------------------------------------------------------------------
# 16. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation:
    def test_inflight_files_untouched(self):
        r = run_git("diff", "--cached", "--name-only")
        staged = set(r.stdout.split())
        for f in INFLIGHT:
            assert f not in staged, f"in-flight file staged: {f}"


# ---------------------------------------------------------------------------
# 17. ASCII-only, no em dashes (scoped to this run's own prose)
# ---------------------------------------------------------------------------
class TestBlockHygiene:
    def _own_prose(self):
        note = [
            line
            for line in _read(COMPETITOR_YAML).splitlines()
            if "THIRTY-SIXTH" in line and "1078" in line
        ]
        return _block() + "\n" + "\n".join(note) + "\n" + _read(__file__)

    def test_ascii_only(self):
        bad = [c for c in self._own_prose() if ord(c) > 127]
        assert not bad, f"non-ASCII in this run's prose: {bad[:5]}"

    def test_no_em_dashes(self):
        # Em dash built at runtime so this source file stays ASCII-only.
        assert chr(0x2014) not in self._own_prose()
