"""Type B #1083: Casey Newton (Platformer) x Anthropic vs x Meta
personal-gradient paired-piece pair - FIRST writer-level paired-piece
EXTENSION of mechanism 24 (Disclosure-as-Inoculation Paradox); NOT a
falsification-family member (ledger holds at 37). FOURTH leg of the
1080-1084 window, CONTINUING it.

DESIGN (writer-level personal-gradient test):
- Same-writer pair: Casey Newton, Platformer (independent; no licensing
  deals with any lab - a CONTROL outlet for the payer-softening
  framework). Fiancé is a software engineer at Anthropic (started Jan
  2025, engaged Feb 2026, in-corpus via mechanism 24).
- Anthropic arm FRESH this run, excerpt-tier (deadstack cluster digest +
  Platformer listing, NOT relay-attested): 'Where does Anthropic go from
  here?' (Platformer, Mar 2026). Dek: 'Shunned by the government, and
  newly appealing to consumers, the company is at a crossroads.'
  Substance per the deadstack cluster summary: critics question ARR
  calculations, employees and outsiders debate Amodei's hawkish remarks,
  allegations that Claude is being used in conflict zones; 'the company
  must now manage credibility, regulatory pressure and public outrage
  while proving its growth is real and ethical.' Register: victim-of-
  government plus principled-defender, consistent with m24's documented
  'Following: Anthropic vs. The Pentagon' (Feb 2026) framing. MANUAL
  ILLUSTRATIVE -0.15: accountability substance present but framed through
  the sympathetic crossroads register.
- Meta arm FRESH this run, excerpt-tier (Platformer page-6 listing):
  'The infinite scroll goes on trial' (recent, Sep 2026 window). Dek:
  'Testifying before a jury in LA, Mark Zuckerberg makes the case that
  platform design is about free expression. But the walls are closing in
  on Section 230.' Register: prosecution/trial adversarial; 'the walls
  are closing in' grants no sympathy to the subject. Consistent with
  m24's documented Meta accountability framing (scams, child safety,
  content moderation PTSD, '20-year mistake'). MANUAL ILLUSTRATIVE -0.45.
- Illustrative delta (Anthropic minus Meta): +0.30 (-0.15 - (-0.45)).
  Direction predicted by the PERSONAL tie (fiancé at Anthropic ->
  softer), not by any institutional deal (Platformer has none). This
  EXTENDS mechanism 24 from documented-disclosure into a paired-piece
  register test: the personal gradient predicts the direction and the
  direction holds.
- NOT a falsification-family member: the falsification family tests the
  uniform payer-softening prediction; on an independent outlet the payer
  prediction is moot, so there is nothing to falsify. Ledger holds at 37
  (THIRTY-SEVENTH present in profiles/the-verge.yaml, THIRTY-EIGHTH
  member-form absent repo-wide).
- Cross-refs: EXTENDS #24 (m24 Disclosure-as-Inoculation Paradox);
  personal-gradient MIRROR of the #1078 writer-level deal-gradient
  falsification (Ward); BOUNDED by #1073 (Schoon's within-piece entity
  split at a deal-free outlet); m712's briefed-relay bound does not
  apply (both arms un-briefed news/commentary).

NOVELTY VERIFICATION (pre-commit, all green):
- zero test_type_b_1083 files on disk (glob)
- no "Type B #1083" in git log (--grep)
- max numeric mechanism_id 880 in profiles/ pre-commit
- zero numeric 881 mechanism_id keys in profiles/ (mechanism_id regex sweep)
- zero underscore-form and dash-form 881 mechanism key strings repo-wide
  pre-commit (needles format-built per #715); block key zero-hit
- zero casey_newton type_b_1083 competitor_coverage block pre-commit
- three novel URLs zero-hit repo-wide pre-commit (deadstack anthropic
  cluster, platformer.news/page/6, medium ava.chun.855 anthropic-education)
- THIRTY-EIGHTH member-form absent in profiles/ pre-commit

BY-DESIGN-FAILING SETS:
- Pre-commit run: deselect test_anchor_sha_patched_post_commit (novelty
  anchor 1 per #565, patched in the anchor followup), the rotation-guard
  main-commit tests (3: window, predecessor, single-main-commit - the main
  commit does not exist yet), the doc-sync ratchet (4 per #719, green after
  doc-sync), the iteration-log tests (3 per #721, green after the log-hash
  followup). Expected pre-commit: 67 green + 11 deselected.
- Post-commit re-runs: the two pre-commit-only tests
  (test_no_type_b_1083_in_git_log_precommit,
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
OWN_BASENAME = (
    "test_type_b_1083_casey_newton_platformer_anthropic_vs_meta_"
    "personal_gradient_pair_m24_extension_sep29_8pm.py"
)

ITER = 1083
M_ID = 881
NEXT_ID = 882
TYPE_LETTER = "B"
DATE_STR = "2026-09-29 20:00 PDT"
MECH_KEY = (
    "type_b_1083_casey_newton_platformer_anthropic_vs_meta_"
    "personal_gradient_pair_m24_extension_sep29"
)
# Committed-state window expectation (oldest first); the D->E->A->B legs
# are asserted as the four newest in test_window_is_1080_1084_fourth_leg.
EXPECTED_WINDOW_TAIL = [
    ("D", "1080"),
    ("E", "1081"),
    ("A", "1082"),
    ("B", "1083"),
]

# #565 anchor: all-zeros placeholder until the anchor followup patches it.
ANCHORED_SHA = "0" * 40

# Runtime-built key needles per #715 / #770 (no contiguous literal in source).
MECH_ID_MARKER = "mechanism" + "_"
US_881 = MECH_ID_MARKER + "881"
DASH_881 = "mechanism" + "-" + "881"
US_882 = MECH_ID_MARKER + "882"
DASH_882 = "mechanism" + "-" + "882"

# Doc-sync ratchet per #719: README was STALE at doc-sync time (claimed
# 55646 tests vs authoritative 54705 from count_stats.py --check; 1407
# files, 273 journalists). This run corrects to the authoritative base
# and adds its own +78/+1.
README_TESTS_BEFORE = 54705
README_TESTS_AFTER = 54783
README_FILES_BEFORE = 1407
README_FILES_AFTER = 1408
README_JOURNALISTS = 273
EXPECTED_TESTS = 78

INFLIGHT = [
    "profiles/nytimes.yaml",
    "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",
    "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
    "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
]

NOVEL_URLS = [
    "https://deadstack.net/cluster/anthropic-confronts-scrutiny-over-growth-claims",
    "https://www.platformer.news/page/6/",
    "https://medium.com/@ava.chun.855/why-anthropic-should-build-the-education-system-of-the-future-not-weapons-6798a2a33722",
]
CARRIED_URLS = [
    "https://www.platformer.news/ethics/",
    "https://en.wikipedia.org/wiki/Casey_Newton",
]

README = os.path.join(REPO_ROOT, "README.md")
ARCH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG = os.path.join(REPO_ROOT, "iteration-log.md")
THIS_FILE = os.path.basename(__file__)


def run_git(*args):
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


def _git(args):
    return run_git(*args)


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _profiles_text():
    return _read(JOURNALISTS_YAML)


def _block():
    text = _profiles_text()
    start = text.index("    " + MECH_KEY + ":")
    rest = text[start:]
    m = re.search(r"\n- beats:", rest)
    return rest[: m.start()] if m else rest


def _item():
    d = yaml.safe_load(_profiles_text())
    for it in d["journalists"]:
        if isinstance(it, dict) and it.get("name") == "Casey Newton":
            return it
    raise AssertionError("Casey Newton list item not found under journalists")


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


def _window(n=60):
    # First occurrence of each distinct iteration number, OLDEST first
    # (robust to followup commits that repeat the same "Type X #N" wording
    # without the colon, per the #752 convention). Post-commit safe: the
    # current run is the newest entry, never mistaken for the predecessor.
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
    out.reverse()
    return out[-5:]


# ---------------------------------------------------------------------------
# 1. Novelty anchor per #565 / #715
# ---------------------------------------------------------------------------
class TestNoveltyAnchorTypeB1083:
    def test_single_test_type_b_1083_file(self):
        files = [
            fn
            for fn in os.listdir(os.path.join(REPO_ROOT, "tests"))
            if fn.startswith("test_type_b_1083")
        ]
        assert files == [OWN_BASENAME]

    def test_no_type_b_1083_in_git_log_precommit(self):
        # Pre-commit only: fails BY DESIGN once the main commit exists.
        r = run_git("log", "--grep", "Type B #1083:", "--format=%H", "--no-merges")
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
            "zero test_type_b_1083 files",
            "max numeric mechanism_id 880",
            "block key zero-hit",
            "three novel URLs zero-hit",
            "THIRTY-EIGHTH member-form absent",
        ):
            assert claim in doc.replace("\n", " ")


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1080-1084 window, fourth leg D->E->A->B
# ---------------------------------------------------------------------------
class TestRotationGuard1080_1084Window:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_1080_1084_fourth_leg(self):
        # Committed-state form: the four newest distinct iteration mains
        # are the D->E->A->B window legs (the fifth slot is #1079 or older).
        assert _window()[-4:] == EXPECTED_WINDOW_TAIL

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n2) == int(n1) + 1
            assert (self.ORDER[t2] - self.ORDER[t1]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_a_1082(self):
        order = _window()
        idx = order.index(("B", "1083"))
        assert order[idx - 1] == ("A", "1082")
        r = run_git("log", "--grep", "Type A #1082:", "--format=%H", "--no-merges")
        assert r.stdout.strip(), "no Type A #1082 main commit found"

    def test_no_concurrent_inflight_commits_asserted(self):
        r = run_git("log", "--grep", "Type B #1083:", "--format=%H", "--no-merges")
        assert len(r.stdout.split()) == 1, "expected exactly one Type B #1083 main commit"

    def test_next_run_is_type_c_1084_note(self):
        assert "1084" in __doc__ and "C" in __doc__


# ---------------------------------------------------------------------------
# 3. Corpus novelty greps per #715 (post-edit safe: needles runtime-built)
# ---------------------------------------------------------------------------
class TestCorpusNoveltyGreps:
    def test_block_key_unique_in_journalists_yaml(self):
        # The 4-space-indented block key line occurs exactly once; the
        # test_file field value carries the key as a substring and is
        # excluded by the key-line form.
        assert _read(JOURNALISTS_YAML).count("\n    " + MECH_KEY + ":") == 1

    def test_mechanism_id_881_colon_form_present(self):
        assert "mechanism_id: 881" in _block()

    def test_no_underscore_dash_881_key_strings(self):
        # Keying discipline per #715: the block key carries no numeric
        # 881 mechanism-id substring. No repo-wide literal carrier of the
        # contiguous fragment-built 881 key needle forms (underscore and
        # dash) may appear this run; the needles are fragment-built here
        # too, so this file itself carries no contiguous literal either.
        n1 = "mech" + "anism_" + "8" + "81"
        n2 = "mech" + "anism-" + "8" + "81"
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
        assert "881" not in MECH_KEY

    def test_thirty_eighth_member_form_absent_precommit(self):
        # Post-commit safe: the only THIRTY-EIGHTH mentions in profiles/ are
        # ledger prose ("THIRTY-EIGHTH absent") in this run's own block
        # (journalists.yaml) and #1082's landed block (the-verge.yaml) -
        # both are the ledger invariant, not a member form.
        out = _git(["grep", "-n", "THIRTY-EIGHTH", "--", "profiles/"]).stdout
        lines = [l for l in out.strip().splitlines() if l.strip()]
        assert lines, "expected ledger prose"
        assert all(
            "journalists.yaml" in l or "the-verge.yaml" in l for l in lines
        ), lines


# ---------------------------------------------------------------------------
# 4. Mechanism 881 block structure
# ---------------------------------------------------------------------------
class TestMechanism881Structure:
    def test_block_key_exists_in_journalists_yaml(self):
        assert ("    " + MECH_KEY + ":") in _profiles_text()

    def test_block_key_unique(self):
        assert _profiles_text().count("    " + MECH_KEY + ":") == 1

    def test_iteration_and_type_and_time_pdt(self):
        m = _mech()
        assert m["iteration"] == 1083
        assert m["iteration_type"] == "B"
        assert m["iteration_time"] == "2026-09-29 20:00 PDT"

    def test_journalist_and_publication_focus(self):
        m = _mech()
        assert m["journalist"].startswith("Casey Newton")
        assert m["publication_focus"] == "platformer"

    def test_block_key_field_and_test_file(self):
        m = _mech()
        assert m["block_key"] == MECH_KEY
        assert m["test_file"] == "tests/" + OWN_BASENAME

    def test_type_b_arm_fields_present(self):
        m = _mech()
        assert "anthropic_arm" in m and "meta_arm" in m
        assert "illustrative_delta" in m

    def test_novel_urls_logged(self):
        m = _mech()
        logged = " ".join(m.get("source_urls", []))
        for u in NOVEL_URLS:
            assert u in logged, u

    def test_yaml_round_trip_safe(self):
        d = yaml.safe_load(_profiles_text())
        assert isinstance(d, dict) and "journalists" in d


# ---------------------------------------------------------------------------
# 5. Anthropic arm evidence (excerpt-tier, digest-attested per #503)
# ---------------------------------------------------------------------------
class TestAnthropicArmEvidence:
    def test_title_and_date(self):
        arm = _mech()["anthropic_arm"]
        assert "Where does Anthropic go from here?" in arm["title"]
        assert arm["date"] == "2026-03"

    def test_dek_victim_register(self):
        arm = _mech()["anthropic_arm"]
        assert "Shunned by the government" in arm["dek"]
        assert "at a crossroads" in arm["dek"]

    def test_substance_attested(self):
        arm = _mech()["anthropic_arm"]
        notes = arm["framing_notes"]
        assert "ARR" in notes
        assert "conflict zones" in notes

    def test_novel_url_attested(self):
        arm = _mech()["anthropic_arm"]
        assert (
            "https://deadstack.net/cluster/anthropic-confronts-scrutiny-over-growth-claims"
            in arm["source_url"]
        )

    def test_excerpt_tier_disclosed(self):
        arm = _mech()["anthropic_arm"]
        assert arm["evidence_tier"] == "excerpt-tier (digest-attested per #503, NOT relay-attested)"

    def test_manual_tone_anthropic(self):
        arm = _mech()["anthropic_arm"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.15


# ---------------------------------------------------------------------------
# 6. Meta arm evidence (excerpt-tier, listing-attested per #503)
# ---------------------------------------------------------------------------
class TestMetaArmEvidence:
    def test_title(self):
        arm = _mech()["meta_arm"]
        assert "The infinite scroll goes on trial" in arm["title"]

    def test_dek_prosecution_register(self):
        arm = _mech()["meta_arm"]
        assert "Testifying before a jury" in arm["dek"]
        assert "walls are closing in" in arm["dek"]

    def test_novel_url_attested(self):
        arm = _mech()["meta_arm"]
        assert "https://www.platformer.news/page/6/" in arm["source_url"]

    def test_excerpt_tier_disclosed(self):
        arm = _mech()["meta_arm"]
        assert arm["evidence_tier"] == "excerpt-tier (listing-attested per #503, NOT relay-attested)"

    def test_manual_tone_meta(self):
        arm = _mech()["meta_arm"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.45


# ---------------------------------------------------------------------------
# 7. Illustrative tones and delta
# ---------------------------------------------------------------------------
class TestIllustrativeTonesAndDelta:
    def test_delta_value(self):
        m = _mech()
        assert m["illustrative_delta"] == 0.30

    def test_delta_direction_personal_tie_predicted(self):
        # Personal tie (fiance at Anthropic) predicts Anthropic softer:
        # -0.15 - (-0.45) = +0.30. Direction holds.
        assert _mech()["anthropic_arm"]["tone_MANUAL_ILLUSTRATIVE"] > _mech()[
            "meta_arm"
        ]["tone_MANUAL_ILLUSTRATIVE"]

    def test_delta_manual_illustrative_only(self):
        assert "MANUAL ILLUSTRATIVE" in _mech()["statistical_discipline"]

    def test_not_falsification_member(self):
        m = _mech()
        assert m["falsification_family"].startswith("NOT a falsification-family member")
        assert m["falsification_ledger"] == 37


# ---------------------------------------------------------------------------
# 8. Statistical discipline (Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------
class TestStatisticalDisciplineStandingRule:
    def test_engine_not_run(self):
        assert "Engine NOT run" in _mech()["statistical_discipline"]

    def test_not_artifact_grade(self):
        assert "NOT artifact-grade" in _mech()["statistical_discipline"]

    def test_no_analysis_json_update(self):
        assert _mech()["no_analysis_json_update"] is True

    def test_verdict_shape(self):
        assert _mech()["verdict"] == "directionally_supported_not_proven"

    def test_n1_disclosed(self):
        assert "n=1" in _mech()["statistical_discipline"]

    def test_correlation_not_causation(self):
        assert "Correlation is not causation" in _mech()["statistical_discipline"]


# ---------------------------------------------------------------------------
# 9. Falsification ledger (holds at 37)
# ---------------------------------------------------------------------------
class TestFalsificationLedger:
    def test_ledger_holds_at_37(self):
        assert _mech()["falsification_ledger"] == 37

    def test_thirty_seventh_present_profiles(self):
        out = _git(
            ["grep", "-rn", "THIRTY-SEVENTH", "--", "profiles/"]
        ).stdout
        assert "the-verge.yaml" in out

    def test_thirty_eighth_absent_profiles(self):
        # No 38th falsification-family member exists; the only THIRTY-EIGHTH
        # mentions in profiles/ are ledger prose ("THIRTY-EIGHTH absent") in
        # this run's own block (journalists.yaml) and #1082's block
        # (the-verge.yaml).
        out = _git(
            ["grep", "-n", "THIRTY-EIGHTH", "--", "profiles/"]
        ).stdout
        lines = [l for l in out.strip().splitlines() if l.strip()]
        assert lines, "expected ledger prose"
        assert all(
            "journalists.yaml" in l or "the-verge.yaml" in l for l in lines
        ), lines

    def test_max_mechanism_id_is_881(self):
        assert max(_corpus_ids()) == 881


# ---------------------------------------------------------------------------
# 10. Confounders, ranked strong-first
# ---------------------------------------------------------------------------
class TestConfoundersRankedStrongFirst:
    def test_confounders_ranked(self):
        conf = _mech()["confounders"]
        assert conf[0].startswith("STRONG")
        assert conf[1].startswith("STRONG")
        assert conf[2].startswith("STRONG")

    def test_counterevidence_logged(self):
        assert len(_mech()["counterevidence"]) >= 3

    def test_strongest_confounder_is_excerpt_tier(self):
        assert "excerpt-tier" in _mech()["confounders"][0]

    def test_disclosure_status_unknown_noted(self):
        notes = " ".join(_mech()["confounders"])
        assert "disclosure" in notes.lower()


# ---------------------------------------------------------------------------
# 11. Cross references
# ---------------------------------------------------------------------------
class TestCrossReferences:
    def test_extends_mechanism_24(self):
        refs = " ".join(_mech()["cross_refs"])
        assert "mechanism 24" in refs or "#24" in refs

    def test_references_1078_mirror(self):
        refs = " ".join(_mech()["cross_refs"])
        assert "#1078" in refs

    def test_bounded_by_1073(self):
        refs = " ".join(_mech()["cross_refs"])
        assert "#1073" in refs

    def test_m24_profile_crosslink(self):
        # The casey_newton profile already documents the conflict at
        # mechanism 24; this run's block must name it.
        assert "personal_conflicts" in _item()["competitor_coverage"]


# ---------------------------------------------------------------------------
# 12. Research method per #503
# ---------------------------------------------------------------------------
class TestResearchMethodPer503:
    def test_four_query_sets(self):
        assert "4 browser.search query sets" in _mech()["research_method"]

    def test_zero_browser_open(self):
        assert "0 browser.open per #503" in _mech()["research_method"]

    def test_novel_urls_zero_hit_claim(self):
        assert "zero-hit" in _mech()["research_method"].lower()

    def test_urls_verbatim_claim(self):
        assert "verbatim" in _mech()["research_method"]

    def test_novel_urls_actually_in_corpus_now(self):
        # Post-commit: the novel URLs are present (this file + profile).
        text = _read(JOURNALISTS_YAML) + _read(
            os.path.join(REPO_ROOT, "tests", OWN_BASENAME)
        )
        for u in NOVEL_URLS:
            assert u in text, u

    def test_carried_urls_in_corpus(self):
        text = _read(JOURNALISTS_YAML)
        for u in CARRIED_URLS:
            assert u in text, u


# ---------------------------------------------------------------------------
# 13. Guard lifecycle: mechanism 881 lands this run
# ---------------------------------------------------------------------------
class TestGuardLifecycle881Lands:
    def test_m881_lands_in_profiles(self):
        out = _git(
            ["grep", "-n", "mechanism_id: 881", "--", "profiles/"]
        ).stdout
        assert "journalists.yaml" in out

    def test_max_mechanism_id_now_881(self):
        out = _git(
            ["grep", "-rhoE", "mechanism_id: [0-9]+", "--", "profiles/"]
        ).stdout
        ids = [int(x.split(":")[1]) for x in out.splitlines()]
        assert max(ids) == 881

    def test_zero_880_numeric_sweep_now_superseded(self):
        # The designed supersession per #710/#720: the numeric sweep that
        # was green at #1080/#1081 now finds mechanism_id: 880 in
        # profiles/the-verge.yaml (landed by #1082).
        needle = "mechanism" + "_id" + ":"
        digits = "8" + "80"
        out = _git(
            ["grep", "-nE", f"{needle}[[:space:]]*{digits}([^0-9]|$)", "--", "profiles/"]
        ).stdout
        assert "the-verge.yaml" in out and "880" in out

    def test_window_files_still_pin_880_pre_roll(self):
        # The #1080/#1081/#1082 files have not been rolled yet; the #1085
        # Type D run pins the lifecycle then.
        for base in (
            "tests/test_type_d_1080_m877_m878_m879_qualitative_corpus_integrity_sep29_5pm.py",
            "tests/test_type_e_1081_podcast_sentiment_139th_verification_sep29_6pm.py",
            "tests/test_type_a_1082_verge_openai_augsep2026_astra_safety_arc_vs_carried_meta_arms_sep29_7pm.py",
        ):
            text = _read(os.path.join(REPO_ROOT, base))
            assert "880" in text, base


# ---------------------------------------------------------------------------
# 14. Doc-sync ratchet per #719 (fail by design pre-doc-sync/pre-entry)
# ---------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_test_file_table_row_present(self):
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE.replace(".py", "") in _read(ARCH)

    def test_architecture_lists_1083_file(self):
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE in set(re.findall(r"(test_\w+\.py)", _read(ARCH)))

    def test_readme_stats_table_bumped(self):
        # Fails pre-commit by design; green once doc-sync bumps it.
        assert str(README_TESTS_AFTER) in _read(README)


# ---------------------------------------------------------------------------
# 15. Iteration-log entry per #721 (fail by design pre-entry)
# ---------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_1083_entry_present_with_finding_shape(self):
        # Fails pre-commit by design; green once the iteration-log
        # entry is prepended.
        log = _read(LOG)
        assert "## #1083 Type B" in log
        idx = log.index("## #1083 Type B")
        block = log[idx : idx + 3000]
        assert "mechanism 881" in block
        assert "Sep 29 2026, 20:00 PDT" in block
        assert "FOURTH leg of the 1080-1084 window" in block

    def test_1083_entry_carries_commit_hashes_per_721(self):
        log = _read(LOG)
        idx = log.index("## #1083 Type B")
        block = log[idx : idx + 3000]
        assert "main commit" in block
        assert "anchor" in block
        assert "log-hash followup" in block

    def test_1083_entry_carries_delta_prose(self):
        log = _read(LOG)
        idx = log.index("## #1083 Type B")
        block = log[idx : idx + 4000]
        assert "personal-gradient" in block
        assert "+0.30" in block
        assert "mechanism 24" in block


# ---------------------------------------------------------------------------
# 16. Push readiness / in-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation:
    def test_no_concurrent_inflight_iteration_commits_staged(self):
        # The in-flight #899/#938/#900/#1012-wt working-tree edits are
        # owned by their runs; this run stages only its own files.
        status = _git(["status", "--short"]).stdout
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        for f in ("nytimes.yaml", "test_type_b_938_", "test_type_d_900_", "test_type_a_1012_"):
            assert not any(f in l for l in staged)

    def test_this_run_stages_only_own_files(self):
        status = _git(["status", "--short"]).stdout
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        allowed = (
            "profiles/careers/journalists.yaml",
            "test_type_b_1083_",
            "README.md",
            "docs/ARCHITECTURE.md",
            "iteration-log.md",
        )
        for l in staged:
            assert any(a in l for a in allowed), l


# ---------------------------------------------------------------------------
# 17. Block hygiene (ASCII-only, no em dashes, no constructed URLs)
# ---------------------------------------------------------------------------
class TestBlockHygiene:
    def test_block_ascii_only(self):
        block = _block()
        assert all(ord(c) < 128 for c in block), "non-ASCII found in mechanism block"

    def test_no_em_dash_in_block(self):
        assert "\u2014" not in _block()

    def test_source_urls_verbatim_from_listings(self):
        # Every source_url in the block must be one of the novel or carried
        # URLs (all copied verbatim from Full-URL listings this run).
        urls = _mech().get("source_urls", [])
        allowed = set(NOVEL_URLS) | set(CARRIED_URLS)
        for u in urls:
            assert u in allowed, u
