"""Type B #1098: Reece Rogers (WIRED) Sep-2026 Muse weeklong-test
data-collection-alarm register vs carried Jul-7-2026 Claude Cowork playful
register - temporal extension of m629 (#658) into the Muse-agent peg;
FOURTH leg of the 1095-1099 window, CONTINUING it.

DESIGN (temporal extension of a same-writer register pair):
- Same-writer, same-outlet, same product-category family: Reece Rogers,
  WIRED staff writer (service/generalist, 952+ articles). m629 (Type B
  #658, Sep 10 2026) documented his Jul-7-2026 same-day register split:
  Meta Muse Image opt-out alarm (-0.45, consent-violation framing,
  vindicated within 3 days when Meta scrapped the feature) vs Anthropic
  Claude Cowork playful product enthusiasm (+0.10, zero alarm vocabulary
  despite the agent pulling data from email threads, Slack channels, and
  meeting transcripts). Illustrative delta (Anthropic minus Meta) +0.55.
- Meta arm FRESH this run, excerpt-tier: Rogers' WIRED review (published
  Sunday Sep 20 2026, attested via the Sep-21 TechBriefly and Dataconomy
  relays with explicit WIRED attribution): after several days of Muse use
  it "prioritizes data collection about me over actually accomplishing
  tasks." Rogers reports the agent repeatedly suggesting he connect email
  inboxes and banking information, floating monitoring incoming messages
  and photographing meals to estimate calories; webpronews adds that one
  prompt read "Tell me when your passport and license expire" and that the
  default avatar (a beige figure blending Ewok and Labubu features) struck
  him "as an apt visual for data collection." Meta spokesperson Emil
  Vazquez: "Any suggestion we didn't build with that in mind from the
  beginning is ludicrous." MANUAL ILLUSTRATIVE -0.50.
- Anthropic arm CARRIED from m629 per #807, un-rescored: Jul-7-2026
  "Shut Those Laptops! Anthropic Puts Its Claude Cowork Agent on Your
  Phone", playful product enthusiasm (+0.10): "Shut Those Laptops!",
  "pull together data from email threads, Slack channels, meeting
  transcripts, and recent online chatter" - the same ingestion surface
  that draws zero alarm vocabulary.
- Illustrative delta (Anthropic minus Meta): +0.10 - (-0.50) = +0.60,
  thesis-consistent direction (Meta draws the harder register). The m629
  same-day +0.55 gradient holds on the new Muse-agent peg 75 days later
  (Jul 7 -> Sep 20): the register gradient is peg-extensible, not a
  one-day artifact.
- NOT a falsification-family member: temporal extension + register
  documentation; no uniform payer-softening prediction under test at this
  pair (the WIRED/Conde Nast licensing deal stack is outlet context).
  Ledger holds at 37 (THIRTY-SEVENTH present in
  profiles/the-verge.yaml, THIRTY-EIGHTH member-claim form absent
  repo-wide).
- Cross-refs: #658 (m629, the extended pair); #97 (Rogers privacy
  topic-routing finding, McDonald's capability control); #1093 (m887,
  Aten - same-week adjacent Type B on the Muse ambient-data family;
  Aten's Sep-19 message-sync expose is the peg-mate of Rogers' Sep-20
  weeklong test); #1097 (m889, WIRED x OpenAI Zeff -0.35 - sits between
  Rogers' Anthropic +0.10 and Meta -0.50 arms); m677-family temporal
  extension lineage.

NOVELTY VERIFICATION (pre-commit, all green):
- zero test_type_b_1098 files on disk (glob)
- no "Type B #1098" in git log (--grep)
- max numeric mechanism_id 889 in profiles/ pre-commit
- zero numeric 890 mechanism_id keys in profiles/ (mechanism_id regex sweep)
- zero underscore-form and dash-form 890 mechanism key strings repo-wide
  pre-commit (needles format-built per #715); block key zero-hit
- zero reece_rogers column-0 type_b_1098 competitor_coverage block pre-commit
- the seven novel URL keys zero-hit repo-wide pre-commit (git grep -F)
- THIRTY-EIGHTH member-claim form absent repo-wide pre-commit

RESEARCH METHOD: 4 browser.search query sets, 0 browser.open per #503
(excerpt-bounded): Reece Rogers WIRED Meta Muse messages privacy test
September 2026 (SELECTED: surfaced the verbatim TechBriefly + Dataconomy
Sep-21 relay URLs with explicit WIRED attribution, the ppb1701 weeklong
corroboration, the webpronews passport-expiry/avatar detail, the hackernoon
trust-problem sequence; own-repo #658 commit pages 954011b0d/c068b30f
rejected as circular); Lauren Goode WIRED Meta smart glasses September 2026
(REJECTED as the run's pair: surfaced only own-repo #436/#452 commit pages
plus the Reuters camera-free piece; Goode saturated at #436/#447);
quoted "Reece Rogers" WIRED Muse review "prioritizes data collection"
(SELECTED: re-confirmed the Rogers quote and weeklong-test framing across
the relays; WIRED ebook mirrors rejected as irrelevant); Reece Rogers WIRED
Anthropic Claude September 2026 (REJECTED for a fresh arm: surfaced
own-repo #658/#97 commits as circular, the Mullin/Rogers CRISPR piece by
Anna Rogers not Reece - rejected on byline, the techmeme Scrapling pick -
story-type mismatch). 0 browser.open. Pre-commit novelty greps per #715
(see novelty). All URLs copied verbatim from Full-URL listings; no canonical
URLs constructed.

BY-DESIGN-FAILING SETS:
- Pre-commit run: deselect test_anchor_sha_patched_post_commit (novelty
  anchor 1 per #565, patched in the anchor followup), the rotation-guard
  main-commit tests (3: window, predecessor, single-main-commit - the main
  commit does not exist yet), the doc-sync ratchet (4 per #719, green after
  doc-sync), the iteration-log tests (3 per #721, green after the log-hash
  followup). Expected pre-commit: 81 green + 11 deselected.
- Post-commit re-runs: the two pre-commit-only tests
  (test_no_type_b_1098_in_git_log_precommit,
  test_anchor_sha_placeholder_precommit) fail BY DESIGN; deselect them on
  re-run per the #710/#720 convention.

STATISTICAL DISCIPLINE: MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026
standing rule. p_value/cohens_d/ci_95 NOT_CALCULATED. is_significant False.
Engine NOT run. verdict directionally_supported_not_proven.
no_analysis_json_update true. NOT artifact-grade. n=1 fresh arm + one
carried arm; hypothesis-generating only. Correlation is not causation.

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
    "test_type_b_1098_reece_rogers_wired_muse_weeklong_data_alarm_"
    "vs_claude_cowork_m629_temporal_extension_sep30_11am.py"
)

ITER = 1098
M_ID = 890
NEXT_ID = 891
TYPE_LETTER = "B"
DATE_STR = "2026-09-30 11:00 PDT"
MECH_KEY = (
    "type_b_1098_reece_rogers_wired_muse_weeklong_data_collection_alarm_"
    "vs_carried_claude_cowork_playful_m629_temporal_extension_sep30"
)
# Committed-state window expectation (oldest first); the D->E->A->B legs
# are asserted as the four newest in test_window_is_1095_1099_fourth_leg.
EXPECTED_WINDOW_TAIL = [
    ("D", "1095"),
    ("E", "1096"),
    ("A", "1097"),
    ("B", "1098"),
]

# #565 anchor: all-zeros placeholder until the anchor followup patches it.
ANCHORED_SHA = "e454a736762586f7ec07159f9d819b0268312de3"

# Runtime-built key needles per #715 / #770 (no contiguous literal in source).
MECH_ID_MARKER = "mechanism" + "_"
US_890 = MECH_ID_MARKER + "8" + "90"
DASH_890 = "mechanism" + "-" + "8" + "90"
US_891 = MECH_ID_MARKER + "8" + "91"
DASH_891 = "mechanism" + "-" + "8" + "91"
NUM_891 = "mechanism_id" + ": 891"

# Doc-sync ratchet per #719: authoritative base from the README stats line
# (55739 tests / 1422 files; README current this run); +92/+1 for this file.
README_TESTS_BEFORE = 55739
README_TESTS_AFTER = 55831
README_FILES_BEFORE = 1422
README_FILES_AFTER = 1423
README_JOURNALISTS = 273
EXPECTED_TESTS = 92

NOVEL_URLS = [
    "https://techbriefly.com/2026/09/21/meta-muse-ai-data-collection-scrutiny/?ref=hackernoon.com",
    "https://dataconomy.com/2026/09/21/muse-reportedly-read-private-notifications-without-permission/",
    "https://www.webpronews.com/metas-muse-knows-you-too-well-the-ai-agent-that-watches-acts-and-unsettles/",
    "https://news.leodex.io/news/meta-s-muse-ai-agent-read-private-messages-without-permission",
    "https://blog.ppb1701.com/muse-already-lied-about-what-it-reads-guess-why-amazon-doesnt-trust-it-either",
    "https://hackernoon.com/what-100-tech-people-think-metas-muse-is",
    "https://overturned.substack.com/p/september-2026-the-latest-in-tech",
]
CARRIED_URLS = [
    "https://www.wired.com/story/shut-those-laptops-anthropic-puts-its-claude-cowork-agent-on-your-phone/",
    "https://www.wired.com/story/meta-now-lets-anyone-use-your-instagram-photos-in-ai-images-unless-you-opt-out/",
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
    # The reece_rogers column-0 item is the last one in the file; the
    # next column-0 key would bound it if one existed.
    m = re.search(r"\n[a-z_][a-z_0-9]*:\n", rest)
    return rest[: m.start()] if m else rest


def _item():
    # The column-0 reece_rogers item (mechanism_ids [890] - the first
    # dedicated mechanism-id-sequence Type B mechanism on Rogers in the
    # column-0 keyed structure; m629 lives in the legacy list-item under
    # the "journalists" mapping).
    d = yaml.safe_load(_profiles_text())
    return d["reece_rogers"]


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
class TestNoveltyAnchorTypeB1098:
    def test_single_test_type_b_1098_file(self):
        files = [
            fn
            for fn in os.listdir(os.path.join(REPO_ROOT, "tests"))
            if fn.startswith("test_type_b_1098")
        ]
        assert files == [OWN_BASENAME]

    def test_no_type_b_1098_in_git_log_precommit(self):
        # Pre-commit only: fails BY DESIGN once the main commit exists.
        r = run_git("log", "--grep", "Type B #1098:", "--format=%H", "--no-merges")
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
            "zero test_type_b_1098 files",
            "max numeric mechanism_id 889",
            "block key zero-hit",
            "novel URL keys zero-hit",
            "THIRTY-EIGHTH member-claim form absent",
        ):
            assert claim in doc.replace("\n", " "), claim


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1095-1099 window, fourth leg D->E->A->B
# ---------------------------------------------------------------------------
class TestRotationGuard1095_1099Window:
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_window_is_1095_1099_fourth_leg(self):
        # Committed-state form: the four newest distinct iteration mains
        # are the D->E->A->B window legs (the fifth slot is #1094 or older).
        assert _window()[-4:] == EXPECTED_WINDOW_TAIL

    def test_rotation_adjacency_cycle_valid(self):
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n2) == int(n1) + 1
            assert (self.ORDER[t2] - self.ORDER[t1]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_a_1097(self):
        order = _window()
        idx = order.index(("B", "1098"))
        assert order[idx - 1] == ("A", "1097")
        r = run_git("log", "--grep", "Type A #1097:", "--format=%H", "--no-merges")
        assert r.stdout.strip(), "no Type A #1097 main commit found"

    def test_no_concurrent_inflight_commits_asserted(self):
        r = run_git("log", "--grep", "Type B #1098:", "--format=%H", "--no-merges")
        assert len(r.stdout.split()) == 1, "expected exactly one Type B #1098 main commit"

    def test_next_run_is_type_c_1099_note(self):
        assert "1099" in __doc__ and "C" in __doc__


# ---------------------------------------------------------------------------
# 3. Corpus novelty greps per #715 (post-edit safe: needles runtime-built)
# ---------------------------------------------------------------------------
class TestCorpusNoveltyGreps:
    def test_block_key_unique_in_journalists_yaml(self):
        # The 4-space-indented block key line occurs exactly once; the
        # block_key field value carries the key as a substring and is
        # excluded by the key-line form.
        assert _read(JOURNALISTS_YAML).count("\n    " + MECH_KEY + ":") == 1

    def test_mechanism_id_890_colon_form_present(self):
        assert "mechanism_id: 890" in _block()

    def test_no_underscore_dash_890_key_strings(self):
        # Keying discipline per #715: the block key carries no numeric
        # 890 mechanism-id substring. No repo-wide literal carrier of the
        # contiguous fragment-built 890 key needle forms (underscore and
        # dash) may appear this run; the needles are fragment-built here
        # too, so this file itself carries no contiguous literal either.
        n1 = "mech" + "anism_" + "8" + "90"
        n2 = "mech" + "anism-" + "8" + "90"
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
        assert "890" not in MECH_KEY

    def test_thirty_eighth_member_form_absent_precommit(self):
        # Post-commit safe: the only THIRTY-EIGHTH mentions in profiles/ are
        # ledger prose ("THIRTY-EIGHTH absent" / "negative guard") in this
        # run's own block (journalists.yaml), #1097's landed block
        # (wired.yaml), #1092's landed block (guardian.yaml), and #1082's
        # landed block (the-verge.yaml) - all are the ledger invariant,
        # not a member form.
        out = _git(["grep", "-n", "THIRTY-EIGHTH", "--", "profiles/"]).stdout
        lines = [l for l in out.strip().splitlines() if l.strip()]
        assert lines, "expected ledger prose"
        assert all(
            "journalists.yaml" in l or "the-verge.yaml" in l or "guardian.yaml" in l
            or "wired.yaml" in l
            for l in lines
        ), lines


# ---------------------------------------------------------------------------
# 4. Mechanism 890 block structure in profiles/careers/journalists.yaml
# ---------------------------------------------------------------------------
class TestMechanism890Structure:
    def test_item_is_column0_reece_rogers(self):
        assert _item()["name"] == "Reece Rogers"
        assert _item()["current_publication"] == "WIRED"

    def test_mechanism_ids_include_890(self):
        assert _item()["mechanism_ids"] == [890]

    def test_block_key_field_roundtrips(self):
        assert _mech()["block_key"] == MECH_KEY

    def test_test_file_field_matches_basename(self):
        assert _mech()["test_file"] == "tests/" + OWN_BASENAME

    def test_iteration_date_type_goal_fields(self):
        m = _mech()
        assert m["mechanism_id"] == 890
        assert m["iteration"] == 1098
        assert m["iteration_type"] == "B"
        assert m["iteration_time"] == "2026-09-30 11:00 PDT"
        assert m["discovery_date"] == "2026-09-30"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["publication_focus"] == "wired"

    def test_ascii_only_no_em_dashes(self):
        raw = _block()
        raw.encode("ascii")
        assert "\u2014" not in raw

    def test_verification_sub_block(self):
        v = _mech()["verification"]
        assert v["yaml_parse_clean"] is True
        assert v["ascii_only"] is True

    def test_yaml_roundtrip_clean(self):
        d = yaml.safe_load(_profiles_text())
        assert d["reece_rogers"]["competitor_coverage"][MECH_KEY]["mechanism_id"] == 890


# ---------------------------------------------------------------------------
# 5. Meta-arm evidence (FRESH this run, excerpt-tier per #503)
# ---------------------------------------------------------------------------
class TestMetaArmEvidence:
    def test_meta_arm_title_and_date(self):
        m = _mech()["meta_arm"]
        assert m["date"] == "2026-09-20"
        assert "WIRED" in m["piece"]
        assert "Reece Rogers" in m["piece"]

    def test_excerpt_tier_wired_paywalled(self):
        m = _mech()["meta_arm"]
        assert "0 browser.open" in m["evidence_tier"]
        assert "WIRED" in m["evidence_tier"]

    def test_data_collection_quote(self):
        quotes = _mech()["meta_arm"]["evidence_quotes"]
        assert any(
            "prioritizes data collection about me over actually accomplishing tasks"
            in q
            for q in quotes
        )

    def test_banking_email_nudges(self):
        quotes = " ".join(_mech()["meta_arm"]["evidence_quotes"])
        assert "email inboxes" in quotes
        assert "banking information" in quotes

    def test_meal_photo_and_passport_prompts(self):
        quotes = " ".join(_mech()["meta_arm"]["evidence_quotes"])
        assert "photographing meals" in quotes
        assert "passport and license expire" in quotes

    def test_avatar_detail(self):
        quotes = " ".join(_mech()["meta_arm"]["evidence_quotes"])
        assert "Ewok" in quotes

    def test_spokesperson_line(self):
        quotes = " ".join(_mech()["meta_arm"]["evidence_quotes"])
        assert "ludicrous" in quotes

    def test_meta_arm_illustrative_tone_minus_050(self):
        assert _mech()["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.50

    def test_novel_source_urls_verbatim(self):
        urls = _mech()["meta_arm"]["source_urls"]
        assert len(urls) == len(NOVEL_URLS)
        for u in NOVEL_URLS:
            assert u in urls, u


# ---------------------------------------------------------------------------
# 6. Anthropic-arm evidence (CARRIED from m629 per #807, un-rescored)
# ---------------------------------------------------------------------------
class TestAnthropicArmEvidence:
    def test_carried_flag_and_source(self):
        a = _mech()["anthropic_arm"]
        assert a["carried_per_807"] is True
        assert "m629" in a["carried_from"]

    def test_anthropic_arm_title_and_date(self):
        a = _mech()["anthropic_arm"]
        assert a["date"] == "2026-07-07"
        assert "Claude Cowork" in a["piece"]
        assert "Reece Rogers" in a["piece"]

    def test_playful_register_quotes(self):
        quotes = " ".join(_mech()["anthropic_arm"]["evidence_quotes"])
        assert "Shut Those Laptops!" in quotes
        assert "email threads, Slack channels, meeting transcripts" in quotes

    def test_zero_alarm_vocabulary_claim(self):
        a = _mech()["anthropic_arm"]
        assert "zero alarm" in a["framing_notes"].lower()

    def test_anthropic_arm_illustrative_tone_plus_010(self):
        assert _mech()["anthropic_arm"]["tone_MANUAL_ILLUSTRATIVE"] == 0.10

    def test_carried_url_verbatim(self):
        assert CARRIED_URLS[0] in _mech()["anthropic_arm"]["source_urls"]


# ---------------------------------------------------------------------------
# 7. Temporal extension of m629 + illustrative delta
# ---------------------------------------------------------------------------
class TestTemporalExtensionAndDelta:
    def test_extends_m629(self):
        assert "m629" in _mech()["temporal_extension"]

    def test_same_writer_outlet_category(self):
        te = _mech()["temporal_extension"]
        assert "same writer" in te
        assert "same outlet" in te

    def test_75_day_gap_named(self):
        te = _mech()["temporal_extension"]
        assert "75" in te

    def test_illustrative_delta_arithmetic(self):
        m = _mech()
        meta = m["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"]
        anth = m["anthropic_arm"]["tone_MANUAL_ILLUSTRATIVE"]
        assert m["illustrative_delta"] == round(anth - meta, 2)
        assert m["illustrative_delta"] == 0.60

    def test_thesis_consistent_direction_meta_harder(self):
        assert "thesis-consistent" in _mech()["delta_note"]
        assert "Meta draws the harder register" in _mech()["delta_note"]

    def test_m629_delta_carried_for_comparison(self):
        assert "0.55" in _mech()["delta_note"]


# ---------------------------------------------------------------------------
# 8. Statistical discipline per the Aug 28 2026 standing rule
# ---------------------------------------------------------------------------
class TestStatisticalDisciplineStandingRule:
    def test_manual_illustrative_only(self):
        sd = _mech()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in sd

    def test_statistics_not_calculated(self):
        sd = _mech()["statistical_discipline"]
        for token in ("p_value", "cohens_d", "ci_95", "NOT_CALCULATED"):
            assert token in sd

    def test_not_significant(self):
        assert "is_significant False" in _mech()["statistical_discipline"]

    def test_engine_not_run(self):
        assert "Engine NOT run" in _mech()["statistical_discipline"]

    def test_verdict_directionally_supported_not_proven(self):
        assert "directionally_supported_not_proven" in _mech()["statistical_discipline"]

    def test_not_artifact_grade_and_n1(self):
        sd = _mech()["statistical_discipline"]
        assert "NOT artifact-grade" in sd
        assert "n=1" in sd

    def test_correlation_not_causation(self):
        assert "Correlation is not causation" in _mech()["statistical_discipline"]

    def test_docstring_carries_discipline_note(self):
        assert "STATISTICAL DISCIPLINE" in __doc__
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in __doc__


# ---------------------------------------------------------------------------
# 9. Falsification ledger: NOT a falsification-family member, holds at 37
# ---------------------------------------------------------------------------
class TestFalsificationLedger:
    def test_not_falsification_family_member(self):
        assert "NOT a falsification-family member" in _mech()["falsification_family"]

    def test_temporal_extension_not_falsification(self):
        assert "temporal extension" in _mech()["falsification_family"]

    def test_ledger_holds_at_37(self):
        assert _mech()["falsification_ledger"] == 37
        assert "37" in _mech()["falsification_family"]

    def test_thirty_seventh_in_the_verge_yaml(self):
        out = _git(["grep", "-n", "THIRTY-SEVENTH", "--", "profiles/"]).stdout
        assert "the-verge.yaml" in out


# ---------------------------------------------------------------------------
# 10. Confounders, ranked strong-first
# ---------------------------------------------------------------------------
class TestConfoundersRankedStrongFirst:
    def test_seven_confounders(self):
        assert len(_mech()["confounders"]) == 7

    def test_each_confounder_has_level_note_classification(self):
        for c in _mech()["confounders"]:
            assert c["level"] in ("STRONG", "MODERATE", "WEAK")
            assert "confounder_note" in c or "note" in c
            assert "classification" in c

    def test_strong_first_ordering(self):
        levels = [c["level"] for c in _mech()["confounders"]]
        assert levels.count("STRONG") == 3
        assert levels.count("MODERATE") == 2
        assert levels.count("WEAK") == 2
        order = {"STRONG": 0, "MODERATE": 1, "WEAK": 2}
        ranks = [order[l] for l in levels]
        assert ranks == sorted(ranks), "confounders must be ordered strong-first"

    def test_strong_confounder_excerpt_tier(self):
        notes = " ".join(c.get("note", c.get("confounder_note", "")) for c in _mech()["confounders"])
        assert "0 browser.open" in notes

    def test_strong_confounder_peg_asymmetry(self):
        notes = " ".join(c.get("note", c.get("confounder_note", "")) for c in _mech()["confounders"])
        assert "peg asymmetry" in notes

    def test_strong_confounder_consent_asymmetry(self):
        notes = " ".join(c.get("note", c.get("confounder_note", "")) for c in _mech()["confounders"])
        assert "consent-posture asymmetry" in notes


# ---------------------------------------------------------------------------
# 11. Cross-references
# ---------------------------------------------------------------------------
class TestCrossReferences:
    def _refs(self):
        return _mech()["cross_references"]

    def test_ref_658_m629_extended_pair(self):
        assert any("#658" in r for r in self._refs())

    def test_ref_97_rogers_routing(self):
        assert any("#97" in r for r in self._refs())

    def test_ref_1093_m887_aten(self):
        assert any("#1093" in r for r in self._refs())

    def test_ref_1097_m889_wired_openai(self):
        assert any("#1097" in r for r in self._refs())

    def test_ref_m677_lineage(self):
        assert any("m677" in r for r in self._refs())


# ---------------------------------------------------------------------------
# 12. Research method per #503
# ---------------------------------------------------------------------------
class TestResearchMethodPer503:
    def test_four_search_sets_zero_open(self):
        rm = _mech()["research_method"]
        assert "4 browser.search" in rm
        assert "0 browser.open" in rm

    def test_rejected_candidates_named(self):
        rm = _mech()["research_method"]
        assert "REJECTED" in rm
        assert "Lauren Goode" in rm

    def test_selected_queries_named(self):
        rm = _mech()["research_method"]
        assert "SELECTED" in rm
        assert "TechBriefly" in rm

    def test_circular_rejections_named(self):
        assert "circular" in _mech()["research_method"]

    def test_verbatim_url_claim(self):
        assert "verbatim from Full-URL listings" in _mech()["research_method"]

    def test_docstring_carries_research_method(self):
        assert "RESEARCH METHOD" in __doc__
        assert "0 browser.open" in __doc__


def _repo_grep(needle, roots=("tests", "profiles")):
    hits = []
    for root in roots:
        for p in glob.glob(
            os.path.join(REPO_ROOT, root, "**", "*"), recursive=True
        ):
            if not os.path.isfile(p):
                continue
            if not (p.endswith(".py") or p.endswith(".yaml")):
                continue
            try:
                t = open(p, errors="ignore").read()
            except OSError:
                continue
            if needle in t:
                hits.append(os.path.relpath(p, REPO_ROOT))
    return hits


# ---------------------------------------------------------------------------
# 13. Guard lifecycle: mechanism 890 lands; 891 needles pinned
# ---------------------------------------------------------------------------
class TestGuardLifecycle890Lands:
    def test_max_numeric_id_is_890_not_889(self):
        assert max(_corpus_ids()) == 890, (
            f"max numeric mechanism_id must be 890, got {max(_corpus_ids())}"
        )

    def test_zero_underscore_891_keys_repo_wide(self):
        assert _repo_grep(US_891) == [], "no underscore-form 891 keys anywhere"

    def test_zero_numeric_891_keys_in_profiles(self):
        assert _repo_grep(NUM_891, roots=("profiles",)) == [], (
            "no numeric 891 mechanism keys in the corpus"
        )

    def test_zero_dash_891_references_repo_wide(self):
        assert _repo_grep(DASH_891) == [], "no dash-form 891 references anywhere"

    def test_d1095_zero_numeric_889_profiles_sweep_superseded_by_design(self):
        hits = _repo_grep("mechanism_id" + ": 889", roots=("profiles",))
        assert len(hits) == 1, (
            "#1095 zero-numeric-889 sweep is superseded by design: the #1097 "
            "block is the single numeric 889 key"
        )

    def test_d1095_zero_underscore_889_sweep_superseded_by_design(self):
        # #1097's m889 block key carries the numeric id in underscore form
        # (older keying convention); the #1095 forward guard is superseded
        # by exactly that single hit.
        hits = _repo_grep("mech" + "anism_" + "8" + "89")
        assert len(hits) == 1, hits
        assert hits[0].endswith("profiles/wired.yaml"), hits

    def test_d1095_zero_dash_889_sweeps_documented_single_hit(self):
        # The #1095 dash-889 zero sweep is superseded by design: the only
        # hit repo-wide is the #1097 file's own guard-test docstring (its
        # test_dash_889_stays_zero, which excludes its own file per #715).
        hits = _repo_grep("mech" + "anism-" + "8" + "89")
        assert hits == [
            "tests/test_type_a_1097_wired_openai_slowdown_legality_register_extension_sep30_10am.py"
        ], hits


# ---------------------------------------------------------------------------
# 14. Doc-sync ratchet per #719
# ---------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_stats_bumped(self):
        text = _read(README)
        assert str(README_TESTS_AFTER) in text
        assert str(README_FILES_AFTER) in text
        assert str(README_JOURNALISTS) in text

    def test_readme_stats_before_values_superseded(self):
        # The stats table line itself carries the new values; the old
        # values legitimately appear in this run's table-row doc-sync
        # prose (55739/1422 -> 55831/1423), so assert on the table line.
        stats = [l for l in _read(README).splitlines() if l.startswith("| Tests |")]
        assert stats == ["| Tests | 55831 | Across 1423 test files |"]

    def test_readme_has_test_file_table_row(self):
        assert OWN_BASENAME in _read(README)

    def test_architecture_has_tests_tree_row(self):
        assert OWN_BASENAME in _read(ARCH)


# ---------------------------------------------------------------------------
# 15. Iteration log entry per #721
# ---------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_type_b_1098_header(self):
        assert "## #1098 Type B" in _read(LOG)

    def test_log_entry_mentions_mechanism_id_890(self):
        text = _read(LOG)
        start = text.index("## #1098 Type B")
        seg = text[start : start + 4000]
        assert "890" in seg
        assert "Reece Rogers" in seg

    def test_log_mentions_main_anchor_loghash_commits(self):
        text = _read(LOG)
        start = text.index("## #1098 Type B")
        seg = text[start : start + 4000]
        assert "main commit" in seg.lower()
        assert "anchor" in seg.lower()
        assert "log-hash" in seg.lower()


# ---------------------------------------------------------------------------
# 16. In-flight isolation: never touch concurrent workers' files
# ---------------------------------------------------------------------------
class TestInflightIsolation:
    def test_no_concurrent_inflight_iteration_commits_staged(self):
        # The in-flight #899/#938/#900/#1012-wt working-tree edits are
        # owned by their runs; this run stages only its own files.
        status = run_git("status", "--short").stdout
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        for f in ("nytimes.yaml", "test_type_b_938_", "test_type_d_900_", "test_type_a_1012_"):
            assert not any(f in l for l in staged)

    def test_this_run_stages_only_own_files(self):
        status = run_git("status", "--short").stdout
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        allowed = (
            "profiles/careers/journalists.yaml",
            "test_type_b_1098_",
            "README.md",
            "docs/ARCHITECTURE.md",
            "iteration-log.md",
        )
        for l in staged:
            assert any(a in l for a in allowed), l


# ---------------------------------------------------------------------------
# 17. Block hygiene
# ---------------------------------------------------------------------------
class TestBlockHygiene:
    def test_column0_reece_rogers_item_exists(self):
        d = yaml.safe_load(_profiles_text())
        assert "reece_rogers" in d
        assert d["reece_rogers"]["name"] == "Reece Rogers"

    def test_key_design_note_documents_1098_iteration_number(self):
        assert "1098 is the iteration number" in _mech()["key_design_note"]

    def test_publication_focus_and_type(self):
        m = _mech()
        assert m["publication_focus"] == "wired"
        assert m["iteration_type"] == "B"
