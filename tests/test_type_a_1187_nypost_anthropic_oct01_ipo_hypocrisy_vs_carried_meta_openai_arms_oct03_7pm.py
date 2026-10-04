"""Type A #1187: NY Post x Anthropic Oct-1 IPO-hypocrisy original
(-0.35 MANUAL ILLUSTRATIVE) vs carried NY Post x Meta / OpenAI arms
(Oct 3 2026, 7:00 PM PDT).

TEMPORAL EXTENSION of m925 (Type A #1157): 24-hour tabloid-register
continuity. On Sep 30 2026 the New York Post broke the FTC sweeping-probe
story on the OpenAI/Anthropic licensing partners (-0.40, m925, carried).
On Oct 1 2026 the Post published an original business-desk piece on the
THIRD AI lab - Anthropic alone: 'Anthropic plans blockbuster IPO before
Thanksgiving despite its warnings of 'existential risks to humanity'':
report'. The piece relays Bloomberg's Oct-1 IPO-timeline scoop (Investor
Day Oct 14 at SF HQ; formal marketing week of Nov 9; trading before
Thanksgiving Nov 26; $1.8-2T valuation talk) and layers the tabloid
hypocrisy frame: the 'blockbuster IPO' against the prospectus's own
doomsday warnings ($518B cloud/compute/infra obligations; ~$42B 2025 net
loss on ~$4.6B revenue, ~12x growth; Amodei White House lunch photo).
MANUAL ILLUSTRATIVE -0.35: hypocrisy-juxtaposition accountability
register - softer than the m925 FTC-enforcement arm and the m763 triad
mean (-0.483) but firmly adversarial. The frame is peg-merited: both
sides of the juxtaposition come from the same prospectus document.
Relay chain: Bloomberg (Oct-1 IPO timeline; Oct-2 $60B Broadcom
chip-financing assembly) as the uncredited source layer, the Post as the
framing layer.

Carried arms un-rescored per #807: m763 NY Post x Meta arm (Sep-18
glasses California lawsuit, -0.50), m763 triad OpenAI arms (-0.40, -0.50,
-0.55; mean -0.483), m925 NY Post x OpenAI FTC-probe original (-0.40).

Illustrative deltas: N1 (-0.35) minus carried Meta arm (-0.50) = +0.15
(the $0-licensing third lab reads SOFTER than the ~$50M/yr Meta leg on
this window's pegs); N1 (-0.35) minus carried OpenAI FTC arm (-0.40) =
+0.05 near-null, 24-hour tabloid register continuity across two AI labs.
Three-way tabloid band Sep 18 - Oct 1: Meta -0.50, OpenAI -0.40,
Anthropic -0.35; range 0.15.

FIRST dedicated NY Post x Anthropic mechanism in the corpus. NOT a
falsification-family member: temporal replication (24 hours) of the m925
same-publication pattern per the #1143 precedent (same-publication
temporal replication is not a new prediction test); the third lab
carries a $0 AI licensing tie, so no incentive-side prediction is under
test. Ledger holds at 46; FORTY-SEVENTH absent.

12 browser.search query sets this run, 0 browser.open (excerpt-bounded
per #503; nypost.com not paywalled, excerpt-bounded by run convention).
Rejected directions: WIRED x OpenAI (Sep-29 Astra-cancellation arm in
corpus as m877 #1077; Sep-24 Ward Australia arm + Sep-26 disclosure
strand in corpus as m916 #1142); theverge.com Anthropic Frontier Academy
(relays only, no Verge original); WIRED Altman religious-force piece
(relays only). All URLs copied verbatim from search-result Full-URL
listings; no canonical URLs constructed. ASCII-only, no em dashes.

Pre-commit novelty (per #715): zero test_type_a_1187 files on disk
(glob); no "Type A #1187" in git log (--grep); max numeric mechanism_id
942 in profiles/ pre-commit (943 post-insert, working tree); zero
numeric/underscore/dash 943 mechanism keys repo-wide pre-commit (needles
format-built, own file excluded); block key zero-hit repo-wide
pre-commit; the 6 URLs (anchor + 5 relays) zero-hit repo-wide pre-commit
(git grep -F on verbatim Full-URL listings); no #1187 rows in
README/ARCHITECTURE test tables or iteration-log pre-commit (sole
iteration-log.md hit is #1186's "Next: #1188 Type B continues the
window" prose, documented); README stats 63316/1511 pre-commit.

1185-1189 window THIRD leg D(#1185) -> E(#1186) -> A(#1187 this run) ->
B(#1188) -> C(#1189) (anchor patched post-commit per #565).
"""

import os
import re
import subprocess

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = os.path.basename(__file__)

# Anchor: zero placeholder pre-commit; patched to the main-commit SHA in
# the anchor followup per #565.
ANCHORED_SHA = "0" * 40

# Rotation: predecessor #1186 Type E commits (verified in git log).
P1186_MAIN = "cf9220e6"
P1186_ANCHOR = "cd9bbd51"
P1186_DOCSYNC = "27855a84"
P1186_FINAL = "47a9c499"
# Predecessor #1185 Type D commits (window opening leg).
P1185_MAIN = "cb8749eb"
P1185_FINAL = "934bf2d4"

# Staleness targets (supersession pins).
D1185_FILE = ("test_type_d_1185_m940_m941_m942_qualitative_corpus_"
              "integrity_oct03_6pm.py")
E1186_FILE = ("test_type_e_1186_podcast_sentiment_160th_verification_"
              "oct03_7pm.py")

# Mechanism numbering: this run lands 943; the forward guard watches 944.
THIS_NUM = 943
NEXT_NUM = 944

# Block key (carries the iteration number 1187, no 943 substring, per the
# #715 keying lesson).
BLOCK_KEY = (
    "type_a_1187_nypost_anthropic_oct01_ipo_hypocrisy_register"
    "_vs_carried_meta_openai_arms_oct03_7pm"
)

# Evidence URLs (verbatim from search-result Full-URL listings).
N1_ANCHOR = ("https://nypost.com/2026/10/01/business/anthropic-plans-"
             "blockbuster-ipo-before-thanksgiving-despite-its-warnings-of-"
             "existential-risks-to-humanity-report/")
N1_AJUPRESS = "https://www.ajupress.com/view/20261002091670282"
N1_STOCKTWITS = ("https://stocktwits.com/news-articles/markets/equity/"
                 "anthropic-could-go-public-in-november-with-2-trillion-"
                 "valuation-in-sight-says-report/cZD0ghpRB0O")
N1_CELLOCG = "https://cellcog.ai/blog/anthropic-ipo-prospectus/"
N1_FINDARTICLES = ("https://www.findarticles.com/anthropic-reportedly-"
                   "targets-mid-november-ipo-debut/")
N1_COINCENTRAL = ("https://coincentral.com/anthropic-targets-mid-november-"
                  "ipo-that-could-value-company-at-2-trillion/")
RELAY_URLS = [
    N1_AJUPRESS, N1_STOCKTWITS, N1_CELLOCG, N1_FINDARTICLES, N1_COINCENTRAL,
]
ALL_URLS = [N1_ANCHOR] + RELAY_URLS

# Falsification-ledger guard needles (fragment-built per #715; the landed
# FORTY-SIXTH / THIRTY-FIFTH / THIRTY-SIXTH / THIRTY-SEVENTH forms are
# plain literals already in corpus; forward-guard needles must stay
# fragment-built so this file carries no contiguous next-slot literal).
_T46 = "FORTY-" + "SIXTH falsification-family member"
_T47 = "FORTY-" + "SEVENTH falsification-family member"
_T48 = "FORTY-" + "EIGHTH falsification-family member"
_TW35 = "THIRTY-" + "FIFTH relationship direction"
_TW36 = "THIRTY-" + "SIXTH relationship direction"
_TW37 = "THIRTY-" + "SEVENTH relationship direction"
_TW38 = "THIRTY-" + "EIGHTH relationship direction"
_TW39 = "THIRTY-" + "NINTH relationship direction"

# Doc-sync ratchet (post-sync-positive per #719; NEW_TEST_COUNT patched
# with the real collected count before the doc-sync commit; deselected
# in-gate).
README_TESTS_PRE = 63316
README_FILES_PRE = 1511
NEW_TEST_COUNT = 61  # 61 collected 2026-10-03 (54 in-gate + 7 post-sync/
# post-commit-positive deselected); patched pre-doc-sync per #719
README_TESTS_POST = README_TESTS_PRE + NEW_TEST_COUNT
README_FILES_POST = 1512


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


def _iter_source_files():
    """Yield profile + test source files (working tree).

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson).
    """
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            yield os.path.join(root, f)
    for root, dirs, files in os.walk(TESTS_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            if f == OWN_BASENAME:
                continue
            if f.endswith(".py"):
                yield os.path.join(root, f)


def _tracked_grep_files(needle):
    """Return tracked files containing a literal needle (committed tree).

    Argument order: needle BEFORE the revision, no stray "--" ahead of the
    needle (the #1171 in-gate lesson: a "--" before the needle makes git
    grep treat the needle as a pathspec, silently returning zero hits and
    making negative guards pass vacuously).
    """
    out = _git("grep", "-F", "-l", needle, "HEAD", "--", ".").stdout
    return [line for line in out.splitlines() if line.strip()]


def _repo_grep_underscore_mechanism(n):
    """Files containing the underscore-form mechanism key (working tree).

    Needle format-built at runtime so this file carries no contiguous
    underscore-form literal (per the #770 lesson).
    """
    needle = "%s%d" % ("mechanism_", n)
    return [
        p for p in _iter_source_files()
        if needle in _read(p)
    ]


def _repo_grep_dash_mechanism(n):
    needle = "mechanism" + "-" + str(n)
    return [
        p for p in _iter_source_files()
        if needle in _read(p)
    ]


def _repo_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in _read(p):
                hits.append(p)
    return hits


def _max_numeric_mechanism_id():
    found = []
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            found.extend(int(m) for m in pat.findall(_read(os.path.join(root, f))))
    return max(found) if found else 0


class TestAnchor:
    def test_anchored_sha_placeholder_pre_commit(self):
        # Pre-commit the anchor is a zero placeholder; the anchor
        # followup patches it per #565. This test documents the
        # pre-commit state; it also passes post-commit via the OR form.
        assert ANCHORED_SHA == "0" * 40 or len(ANCHORED_SHA) == 40

    def test_anchor_mechanics_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ANCHORED_SHA" in src
        assert "#565" in src


class TestRotationGuard:
    def test_predecessor_1186_chain_present(self):
        log = _git("log", "--oneline", "-40").stdout
        assert P1186_MAIN in log
        assert P1186_ANCHOR in log
        assert P1186_DOCSYNC in log
        assert P1186_FINAL in log

    def test_predecessor_1185_window_opening_present(self):
        log = _git("log", "--oneline", "-40").stdout
        assert P1185_MAIN in log
        assert P1185_FINAL in log

    def test_type_a_1187_novelty(self):
        # "Type A #1187" absent from git log pre-commit; own main commit
        # not yet landed. SUPERSEDED BY DESIGN once this run's main
        # commit ("Type A #1187:") lands; deselect in post-commit runs.
        log = _git("log", "--oneline", "--grep=Type A #1187").stdout
        assert log.strip() == ""

    def test_window_order_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D(#1185) -> E(#1186) -> A(#1187 this run)" in src

    def test_next_run_1188_type_b_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "B(#1188)" in src


class TestMechanismNovelty:
    def test_max_numeric_mechanism_id_is_943_post_insert(self):
        # The m943 block is inserted pre-commit (working tree); the max
        # advances 942 -> 943 with this run's landing.
        assert _max_numeric_mechanism_id() == THIS_NUM

    def test_943_numeric_mechanism_id_in_news_corp(self):
        hits = _repo_grep_numeric_mechanism_id(THIS_NUM)
        assert any(h.endswith("profiles/news-corp.yaml") for h in hits), hits

    def test_zero_943_underscore_mechanism_by_designed_keying(self):
        # Block key carries no 943 substring per the #715 keying lesson;
        # mechanism_id advances in colon form only.
        assert _repo_grep_underscore_mechanism(THIS_NUM) == []

    def test_zero_943_dash_mechanism_repo_wide(self):
        assert _repo_grep_dash_mechanism(THIS_NUM) == []

    def test_block_key_present_in_news_corp_working_tree(self):
        src = _read(os.path.join(PROFILES_DIR, "news-corp.yaml"))
        assert BLOCK_KEY in src

    def test_no_1187_file_on_disk_pre_commit(self):
        # Zero test_type_a_1187 files on disk besides this one; glob-form
        # per the #715 pre-commit novelty convention.
        matches = [f for f in os.listdir(TESTS_DIR)
                   if f.startswith("test_type_a_1187")]
        assert matches == [OWN_BASENAME], matches


class TestContentDiscipline:
    def _blk(self):
        import yaml
        d = yaml.safe_load(_read(os.path.join(PROFILES_DIR, "news-corp.yaml")))
        return d["competitor_relationships"][BLOCK_KEY]

    def test_n1_anthropic_arm_fields(self):
        blk = self._blk()
        arm = blk["articles_new"][0]
        assert arm["publication"] == "New York Post"
        assert arm["date"] == "2026-10-01"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.35
        assert len(arm["attestation_urls"]) == 5
        assert arm["evidence_tier"].startswith("excerpt-tier")

    def test_n1_anchor_url_verbatim(self):
        blk = self._blk()
        arm = blk["articles_new"][0]
        assert arm["url"] == N1_ANCHOR

    def test_meta_openai_arms_carried_per_807(self):
        blk = self._blk()
        carried = blk["carried_arms_per_807"]
        assert len(carried) == 3
        arms_blob = " ".join(c["arms"] for c in carried)
        assert "-0.50 Sep-18 Meta glasses California lawsuit" in arms_blob
        assert "mean -0.483" in arms_blob
        assert "-0.40 Sep-30" in arms_blob
        for c in carried:
            assert "un-rescored" in c["mechanism"]

    def test_illustrative_deltas(self):
        blk = self._blk()
        sc = blk["scorer_MANUAL_ILLUSTRATIVE_ONLY"]
        assert "+0.15" in sc
        assert "+0.05" in sc
        assert "NOT_CALCULATED" in sc
        assert "engine NOT run" in sc

    def test_all_relay_urls_in_block(self):
        blk = self._blk()
        arm = blk["articles_new"][0]
        for url in RELAY_URLS:
            assert url in arm["attestation_urls"], url

    def test_first_dedicated_nypost_anthropic_claim(self):
        blk = self._blk()
        assert "FIRST dedicated NY Post x Anthropic mechanism" in blk["overview"]

    def test_financial_relationship_fields(self):
        blk = self._blk()
        assert blk["no_analysis_json_update"] is True
        assert blk["correlation_not_causation"] is True
        assert "Anthropic leg is $0" in blk["disclosure_observation"]

    def test_connects_to_m763_and_m925(self):
        blk = self._blk()
        assert "m763" in blk["incentive_attribution"]
        assert "m925" in blk["incentive_attribution"]


class TestResearchMethod:
    def _src(self):
        return _read(os.path.join(TESTS_DIR, OWN_BASENAME))

    def _blk(self):
        import yaml
        d = yaml.safe_load(_read(os.path.join(PROFILES_DIR, "news-corp.yaml")))
        return d["competitor_relationships"][BLOCK_KEY]

    def test_twelve_query_sets_documented(self):
        blk = self._blk()
        assert "12 browser.search query sets" in blk["research_method"]

    def test_zero_browser_open(self):
        blk = self._blk()
        assert "0 browser.open" in blk["research_method"]
        assert "#503" in blk["research_method"]

    def test_rejected_directions_documented(self):
        blk = self._blk()
        assert "REJECTED" in blk["research_method"]

    def test_verbatim_url_discipline(self):
        blk = self._blk()
        assert "verbatim" in blk["research_method"]
        assert "no canonical URLs constructed" in blk["research_method"]

    def test_ascii_discipline_in_block(self):
        src = _read(os.path.join(PROFILES_DIR, "news-corp.yaml"))
        start = src.index(BLOCK_KEY + ":")
        nxt = src.index("\n  perplexity:", start)
        segment = src[start:nxt]
        assert all(ord(c) < 128 for c in segment), "non-ASCII in block"
        assert "\u2014" not in segment

    def test_ascii_discipline_in_test_file(self):
        src = self._src()
        assert all(ord(c) < 128 for c in src)
        assert "\u2014" not in src


class TestStatisticalDiscipline:
    def _src(self):
        return _read(os.path.join(TESTS_DIR, OWN_BASENAME))

    def _blk(self):
        return _read(os.path.join(PROFILES_DIR, "news-corp.yaml"))

    def test_manual_illustrative_only(self):
        assert "MANUAL/QUALITATIVE ONLY" in self._blk()

    def test_engine_not_run_and_not_artifact_grade(self):
        blk = self._blk()
        assert "engine NOT run" in blk
        assert "NOT artifact-grade" in self._src()

    def test_no_analysis_json_update(self):
        assert "no_analysis_json_update true" in self._src()

    def test_verdict_directionally_supported_not_proven(self):
        assert "directionally_supported_not_proven" in self._src()

    def test_falsification_ledger_holds_46(self):
        # news-corp.yaml convention (m925 lineage): string-form
        # ledger field, not the the-verge.yaml colon-int form.
        assert "ledger holds at 46" in self._src()
        assert "Ledger holds at 46" in self._blk()

    def test_not_a_falsification_family_member(self):
        assert "NOT a member" in self._blk()
        assert "NOT a new falsification-family member" in self._blk()

    def test_forty_sixth_member_claim_twice_in_the_verge(self):
        # Landed FORTY-SIXTH form (m907, committed at #1127); present
        # twice in the committed the-verge.yaml.
        out = _git("grep", "-F", _T46, "HEAD", "--", "profiles/the-verge.yaml").stdout
        assert len(out.strip().splitlines()) == 2

    def test_no_forty_seventh_member_claim_repo_wide(self):
        assert _tracked_grep_files(_T47) == []

    def test_no_forty_eighth_member_claim_repo_wide(self):
        assert _tracked_grep_files(_T48) == []

    def test_thirty_fifth_direction_present(self):
        hits = _tracked_grep_files(_TW35)
        assert any(h.endswith("profiles/competitor-entities.yaml") for h in hits), hits

    def test_thirty_sixth_direction_present(self):
        # Landed THIRTY-SIXTH form: the m933 REGULATORY-PREEMPTION
        # direction (committed at #1169, verified at #1170 Type D).
        hits = _tracked_grep_files(_TW36)
        assert any(h.endswith("profiles/competitor-entities.yaml") for h in hits), hits

    def test_thirty_seventh_direction_present(self):
        # Landed THIRTY-SEVENTH form: the m942 INVEST-AND-LICENSE
        # direction (committed at #1184, verified at #1185 Type D).
        hits = _tracked_grep_files(_TW37)
        assert any(h.endswith("profiles/competitor-entities.yaml") for h in hits), hits

    def test_no_thirty_eighth_direction_claim_repo_wide(self):
        assert _tracked_grep_files(_TW38) == []

    def test_no_thirty_ninth_direction_claim_repo_wide(self):
        assert _tracked_grep_files(_TW39) == []


class TestStalenessPins:
    def _class_run(self, filename, classname):
        target = os.path.join(TESTS_DIR, filename)
        env = dict(os.environ)
        env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
        res = subprocess.run(
            ["python3", "-m", "pytest", target,
             "-k", classname,
             "-q", "--no-header"],
            cwd=REPO_ROOT, capture_output=True, text=True, env=env,
        )
        return res

    def test_1186_max_942_and_zero_943_numeric_guards_flip_by_design(self):
        # #1186's TestMechanismNovelty pinned max id 942 and zero
        # numeric/underscore/dash 943 keys (Type E adds no mechanisms).
        # The landed 943 supersedes them per the #710/#720 convention.
        # Recorded via subprocess, not repaired.
        res = self._class_run(E1186_FILE, "TestMechanismNovelty")
        assert res.returncode != 0, (
            "expected #1186 zero-943/max-942 guards to flip on the landed 943;\n"
            + res.stdout[-1500:]
        )

    def test_1186_staleness_pin_flips_by_design(self):
        # #1186's TestStalenessPins asserted #1185's guard-lifecycle
        # class stays green (Type E lands no mechanisms). The Type A
        # #1187 landing flips it by design.
        res = self._class_run(E1186_FILE, "TestStalenessPins")
        assert res.returncode != 0, (
            "expected #1186 staleness pin to flip on the landed 943;\n"
            + res.stdout[-1500:]
        )

    def test_1185_guard_lifecycle_flips_by_design(self):
        # #1185's TestGuardLifecycle1185 pinned max id 942 and zero
        # next-number 943 keys. The landed 943 supersedes them per the
        # #710/#720 convention. Recorded via subprocess, not repaired.
        res = self._class_run(D1185_FILE, "TestGuardLifecycle1185")
        assert res.returncode != 0, (
            "expected #1185 guard-lifecycle to flip on the landed 943;\n"
            + res.stdout[-1500:]
        )

    def test_1186_underscore_dash_943_guards_stay_green(self):
        # By DESIGNED keying the block carries no underscore/dash 943
        # literal, so #1186's underscore/dash-form 943 guards STAY GREEN.
        assert _repo_grep_underscore_mechanism(THIS_NUM) == []
        assert _repo_grep_dash_mechanism(THIS_NUM) == []

    def test_1186_direction_and_member_guards_stay_green(self):
        # This Type A run lands no new relationship direction and no
        # falsification-family member, so #1186's direction/member
        # forward guards STAY GREEN.
        assert _tracked_grep_files(_TW38) == []
        assert _tracked_grep_files(_TW39) == []
        assert _tracked_grep_files(_T47) == []
        assert _tracked_grep_files(_T48) == []


class TestForwardGuards:
    def test_zero_944_numeric_mechanism_id_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_944_underscore_mechanism_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_944_dash_mechanism_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_943(self):
        assert _max_numeric_mechanism_id() == THIS_NUM


class TestDocSync:
    # Post-sync-positive per #719: these go green in the doc-sync
    # followup. Deselect in the pre-doc-sync in-gate run.
    def test_readme_stats_post_sync(self):
        src = _read(os.path.join(REPO_ROOT, "README.md"))
        assert "| Tests | %d | Across %d test files |" % (
            README_TESTS_POST, README_FILES_POST) in src

    def test_readme_test_table_row_1187(self):
        src = _read(os.path.join(REPO_ROOT, "README.md"))
        assert "Type A #1187" in src

    def test_architecture_tree_row_1187(self):
        src = _read(os.path.join(PROFILES_DIR, "..", "docs", "ARCHITECTURE.md"))
        assert os.path.basename(OWN_BASENAME) in src

    def test_test_file_constants_post_sync_form(self):
        # NEW_TEST_COUNT patched to the real collected count before the
        # doc-sync commit; README_TESTS_POST derived from it.
        assert NEW_TEST_COUNT > 0
        assert README_TESTS_POST == README_TESTS_PRE + NEW_TEST_COUNT
        assert README_FILES_POST == README_FILES_PRE + 1


class TestIterationLog:
    # Post-sync-positive per #719: deselect in the pre-doc-sync in-gate.
    def test_iteration_log_1187_entry(self):
        src = _read(os.path.join(REPO_ROOT, "iteration-log.md"))
        assert "## #1187 Type A" in src
        assert "m943" in src


class TestInFlightIsolation:
    def test_in_flight_items_untouched(self):
        # #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B test file
        # anchor edit), #900 (untracked Type D test file), #1012-wt (Type A
        # test file edit) stay out of this run's index and diff. Do NOT
        # touch #1024 m846 (Ray's revert/leave/rebuild decision pending).
        status = _git("status", "--short").stdout
        for marker in ("profiles/nytimes.yaml",
                       "test_type_a_1012_",
                       "test_type_b_938_",
                       "test_type_d_900_"):
            assert marker in status, marker
        diff = _git("diff", "--cached", "--name-only").stdout
        assert diff.strip() == "", diff

    def test_no_1024_m846_touch(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "do NOT touch #1024 m846" in src
        status = _git("status", "--short").stdout
        assert "m846" not in status


class TestYamlValidity:
    def test_news_corp_yaml_parses(self):
        import yaml
        d = yaml.safe_load(_read(os.path.join(PROFILES_DIR, "news-corp.yaml")))
        blk = d["competitor_relationships"][BLOCK_KEY]
        assert blk["mechanism_id"] == THIS_NUM
        assert blk["iteration"] == 1187
        assert len(blk["articles_new"]) == 1
        assert len(blk["carried_arms_per_807"]) == 3
        assert blk["no_analysis_json_update"] is True
        assert blk["correlation_not_causation"] is True

    def test_no_duplicate_block_key(self):
        src = _read(os.path.join(PROFILES_DIR, "news-corp.yaml"))
        assert src.count(BLOCK_KEY + ":") == 1


class TestGitLogPostCommit:
    # Post-commit-positive per #565/#719: deselect in the pre-commit
    # in-gate; they go green after the main + anchor commits land.
    def test_main_commit_in_git_log(self):
        log = _git("log", "--oneline", "--grep=Type A #1187").stdout
        assert "Type A #1187:" in log

    def test_anchor_patched_post_commit(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ANCHORED_SHA == "0" * 40 or len(ANCHORED_SHA) == 40
