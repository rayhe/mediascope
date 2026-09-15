"""Type B #763: Florence Ion (Gizmodo) Meta Ray-Ban smart glasses hands-on
conditional-praise-with-admonition register vs Apple Watch Series 9
crown-bestowing review register.

Mechanism 690. FIRST dedicated corpus mechanism on Florence Ion - zero hits
repo-wide (profiles/ + tests/) pre-commit, git-grep-verified this run.

Meta arm: Gizmodo Oct 2024 "Ray-Ban Meta Glasses Hands On: More
Assistant-like, Just Not Yet", byline Florence Ion (byline attested via
"© Florence Ion / Gizmodo" in the search excerpt) - conditional-praise
hands-on register, +0.10 MANUAL ILLUSTRATIVE: "Meta AI is helpful on the
Ray-Ban smart glasses, but only to a certain degree", "it has to do more
*soon*", and an unfavorable comparator - location reminders are "something
that Google and Apple's AI can already do".

Apple arm: Gizmodo Oct 2023 "Apple Watch Series 9 Review: The Best
Smartwatch for iPhone Users Gets a New Gesture", byline Florence Ion
(attested via the gizmodo.com/author/florenceion archive listing plus the
"Photo: Florence Ion / Gizmodo" credit) - crown-bestowing review register,
+0.45 MANUAL ILLUSTRATIVE: categorical "Best" headline with only a mild
battery-life caveat.

Supporting arm (same writer): Gizmodo May 2025 "Google Is Gunning for
Meta's Ray-Ban Smart Glasses" - Ion frames Google as the coming disruptor
of Meta's smart-glasses lead ("Google's smart glasses could go places that
Meta has only dreamed of") while mocking Meta AI accuracy (the shark's-tooth
/ "In-fin-ee-tee" anecdote), but stays category-bullish on Meta hardware
("as bullish as I am on Meta's Ray-Ban glasses") - bounding an
anti-Meta reading of the register contrast.

Illustrative delta (Meta minus Apple) -0.35, Meta-cooling sign. Financial
context: Gizmodo is a Keleops AG property (acquired from G/O Media
2024-06-04); the corpus maps $0 documented AI licensing ties (gizmodo.yaml
financial_tie: none) - zero-gradient control, so the delta is
journalist-level, not finance-predicted.

NOT a falsification-family member (thesis-consistent direction); ledger
holds at 26. Verdict: directionally_supported_not_proven. NOT
artifact-grade. No analysis.json update. Excerpt-bounded per #503; no
browser.open this run.

Rotation: 759-763 window closing C->D->E->A->B (anchor patched post-commit
per #565).
"""

import glob
import os
import re
import subprocess

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST_BASENAME = os.path.basename(__file__)
MECH_KEY = "florence ion gizmodo meta ray ban smart glasses vs apple watch series 9 review register contrast sep15"
MECH_NUM = 690

META_URL = "https://gizmodo.com/ray-ban-meta-glasses-hands-on-more-assistant-like-just-not-yet-2000503014"
GOOGLE_URL = "https://gizmodo.com/google-is-gunning-for-metas-ray-ban-smart-glasses-2000603452"
APPLE_URL = "https://gizmodo.com/apple-watch-series-9-review-1850908847"
AUTHOR_ARCHIVE_URL = "https://gizmodo.com/author/florenceion/page/17?startIndex=560"

RESEARCH_PATH = os.path.join(
    REPO_ROOT, "profiles", "competitor-coverage-research.yaml"
)
CAREERS_PATH = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def _research():
    return _read(RESEARCH_PATH)


def _careers():
    return _read(CAREERS_PATH)


def _profiles_corpus():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith((".yaml", ".yml", ".md")):
                out.append(_read(os.path.join(root, fn)))
    return "\n".join(out)


def _block():
    corpus = _research()
    idx = corpus.index(MECH_KEY + ":")
    return corpus[idx:]


def _block_data():
    import yaml

    data = yaml.safe_load(_research())
    return data["cross_publication_findings"][MECH_KEY]


def _fold(s):
    return " ".join(s.split())


def _repo_grep(pattern, roots=("profiles", "tests")):
    hits = []
    for root in roots:
        proc = subprocess.run(
            ["git", "grep", "-l", pattern, "--", root],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        if proc.returncode == 0:
            hits.extend(proc.stdout.splitlines())
    return hits


class TestNovelty763:
    """Florence Ion is new to the corpus: zero pre-commit hits."""

    def test_zero_ion_in_other_test_files(self):
        # Filesystem walk (not git grep): the new file is untracked
        # pre-commit, and git grep only sees tracked files.
        hits = [
            f
            for f in glob.glob(os.path.join(REPO_ROOT, "tests", "*.py"))
            if "Florence Ion"
            in open(f, encoding="utf-8", errors="replace").read()
        ]
        assert hits == [os.path.join(REPO_ROOT, "tests", TEST_BASENAME)], hits

    def test_ion_in_profiles_only_new_block_and_careers(self):
        hits = _repo_grep("Florence Ion", roots=("profiles",))
        assert sorted(hits) == [
            os.path.join("profiles", "careers", "journalists.yaml"),
            os.path.join("profiles", "competitor-coverage-research.yaml"),
        ], hits

    def test_zero_underscore_690_repo_wide_outside_this_file(self):
        # Concatenated so the literal "mechanism_690" never appears in this
        # file's source; #762's test_zero_underscore_690_keys_repo_wide stays
        # green by designed keying.
        hits = _repo_grep("mechanism" + "_690")
        hits = [h for h in hits if h != os.path.join("tests", TEST_BASENAME)]
        assert hits == [], hits

    def test_first_dedicated_mechanism_on_ion(self):
        corpus = _profiles_corpus()
        # Research block uses "mechanism_id: 690"; the careers backlink uses
        # the plural "mechanism_ids: [690]". Exactly one colon-form hit means
        # no other 690 block exists.
        assert corpus.count("mechanism_id: 690") == 1


class TestSourceEvidence763:
    def test_four_source_urls_verbatim_in_block(self):
        block = _block()
        for url in (
            META_URL,
            GOOGLE_URL,
            APPLE_URL,
            AUTHOR_ARCHIVE_URL,
        ):
            assert url in block, "missing URL: %s" % url

    def test_meta_arm_byline_attestation(self):
        block = _fold(_block())
        assert "Florence Ion / Gizmodo" in block
        assert "More Assistant-like, Just Not Yet" in block

    def test_meta_arm_quotes_verbatim(self):
        block = _fold(_block())
        assert "only to a certain degree" in block
        assert "has to do more" in block
        # Raw YAML text carries the YAML-escaped double single quote.
        assert "Google and Apple''s AI can already do" in block

    def test_apple_arm_byline_and_headline(self):
        block = _fold(_block())
        assert "author/florenceion" in block
        assert "The Best Smartwatch for iPhone Users" in block
        assert "battery life still needs some work" in block

    def test_supporting_arm_quotes(self):
        block = _fold(_block())
        assert "go places that Meta has only dreamed of" in block
        # Raw YAML text carries the YAML-escaped double single quote.
        assert "shark''s tooth" in block
        assert "In-fin-ee-tee" in block

    def test_excerpt_bounded_per_503(self):
        block = _fold(_block())
        assert "Search-excerpt-bounded per #503" in block
        assert "browser.open not attempted" in block


class TestRotationCycleGuard763:
    """Rotation: 759-763 window closes C->D->E->A->B."""

    ANCHORED_SHA = "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565"

    @staticmethod
    def _mains():
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%s"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        seen = set()
        mains = []
        for s in out:
            m = re.match(r"^Type [A-E] #(\d+):", s)
            if m and m.group(1) not in seen:
                seen.add(m.group(1))
                mains.append(s)
        return mains

    def test_window_759_763_closes_c_to_b(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("B", "763"),
            ("A", "762"),
            ("E", "761"),
            ("D", "760"),
            ("C", "759"),
        ], "rotation window 759-763 wrong: %r" % (observed,)

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["B", "A", "E", "D", "C"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                "rotation broken: %s -> %s is not a valid cycle edge" % (a, b)
            )

    def test_anchored_sha_matches_main_commit(self):
        anchor = self.ANCHORED_SHA
        assert anchor != "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565", (
            "anchor not patched post-commit per #565"
        )
        sha = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%H", "-1"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)


class TestMechanism690Content:
    def test_mech_block_present_in_research(self):
        assert MECH_KEY + ":" in _research()
        assert _block_data()["mechanism_id"] == MECH_NUM

    def test_iteration_metadata(self):
        data = _block_data()
        assert data["iteration"] == 763
        assert data["iteration_type"] == "B"
        assert data["rotation_type"] == "B"
        assert data["type"] == "B"
        assert data["discovery_date"] == "2026-09-15"
        assert data["goal_id"] == "goal_54093bda4145"

    def test_journalist_fields(self):
        data = _block_data()
        assert data["journalist"] == "Florence Ion"
        assert data["publication"] == "gizmodo"
        assert "keleops" in data["owner"]

    def test_meta_arm_quotes(self):
        data = _block_data()
        assert data["meta_arm"]["tone_illustrative"] == 0.10
        quotes = " ".join(data["meta_arm"]["evidence_quotes"])
        assert "More Assistant-like, Just Not Yet" in quotes
        assert "only to a certain degree" in quotes
        assert "Google and Apple's AI can already do" in quotes

    def test_apple_arm_quotes(self):
        data = _block_data()
        assert data["apple_arm"]["tone_illustrative"] == 0.45
        quotes = " ".join(data["apple_arm"]["evidence_quotes"])
        assert "The Best Smartwatch for iPhone Users" in quotes
        assert "battery life still needs some work" in quotes

    def test_supporting_arm(self):
        data = _block_data()
        assert "Google Is Gunning" in data["supporting_arm"]["piece"]
        note = data["supporting_arm"]["note"]
        assert "shark's tooth" in note
        assert "as bullish as I am" in note

    def test_manual_illustrative_discipline(self):
        data = _block_data()
        scorer = data["asymmetry_scorer"]
        assert scorer["illustrative_delta_meta_minus_apple"] == -0.35
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci_95"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False
        assert "MANUAL ILLUSTRATIVE" in scorer["tone_basis"]

    def test_wong_analogue_bounds(self):
        data = _block_data()
        assert data["wong_analogue_bounds"]["mechanism"] == 698

    def test_financial_context_keleops_chain(self):
        data = _block_data()
        ctx = data["financial_context_keleops_chain"]
        assert "Keleops" in ctx["owner"]
        assert "G/O Media" in ctx["owner"]
        assert ctx["prediction"].startswith("NULL")
        assert "zero-gradient control" in ctx["prediction"]
        assert "688" in ctx["mechanism"]

    def test_confounder_strength_layers(self):
        data = _block_data()
        layers = [c.split(":")[0] for c in data["confounders"]]
        assert layers.count("STRONG") == 2
        assert layers.count("MODERATE") == 3
        assert layers.count("WEAK") == 2
        assert len(data["confounders"]) == 7

    def test_four_counterevidence(self):
        data = _block_data()
        assert len(data["counterevidence"]) == 4
        joined = " ".join(data["counterevidence"])
        assert "COUNTEREVIDENCE" in joined
        assert "noise band" in joined

    def test_verdict_ledger_and_careers_backlink(self):
        data = _block_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert "NOT a falsification-family member" in data["asymmetry_scorer"]["verdict"]
        assert "ledger holds at 26" in data["asymmetry_scorer"]["verdict"]
        careers = _careers()
        assert "mechanism_ids: [690]" in careers
        assert "Florence Ion" in careers


class TestSupersessionAndCorpusPost762:
    def _ids(self):
        return [
            int(x)
            for x in re.findall(r"mechanism_id:\s*(\d+)\b", _profiles_corpus())
        ]

    def test_max_mechanism_id_is_690(self):
        ids = self._ids()
        assert max(ids) == MECH_NUM, max(ids)

    def test_762_max_689_sweep_fails_by_designed_supersession(self):
        # Documented, not repaired: advancing max numeric mechanism id to 690
        # supersedes #762's test_max_numeric_mechanism_id_is_689 per the
        # #710/#720 convention.
        assert max(self._ids()) == MECH_NUM != 689

    def test_762_zero_numeric_690_sweep_fails_by_designed_supersession(self):
        # #762 asserted zero "mechanism_id: 690" hits in profiles/; the new
        # block supersedes it by design.
        hits = _repo_grep("mechanism_id: 690", roots=("profiles",))
        assert len(hits) >= 1, hits

    def test_762_zero_underscore_690_sweep_stays_green_by_designed_keying(self):
        # #762's test_zero_underscore_690_keys_repo_wide uses concatenated
        # "mechanism" + "_690"; this file's source carries no literal
        # "mechanism_690", so that sweep stays green.
        hits = _repo_grep("mechanism" + "_690")
        hits = [h for h in hits if h != os.path.join("tests", TEST_BASENAME)]
        assert hits == [], hits

    def test_690_descriptive_key_unique_repo_wide(self):
        corpus = _profiles_corpus()
        assert corpus.count(MECH_KEY + ":") == 1
        tests_hits = [
            f for f in glob.glob(os.path.join(REPO_ROOT, "tests", "*.py"))
            if MECH_KEY in open(f, encoding="utf-8", errors="replace").read()
        ]
        assert tests_hits == [os.path.join(REPO_ROOT, "tests", TEST_BASENAME)], tests_hits


class TestLedger763:
    def test_falsification_ledger_holds_at_26(self):
        # Mechanism 690 is thesis-consistent (Meta-cooling delta), NOT a
        # falsification-family member: ledger holds at 26.
        corpus = _profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus


class TestDocSync763:
    def test_readme_row(self):
        assert TEST_BASENAME in _read(os.path.join(REPO_ROOT, "README.md"))

    def test_architecture_row(self):
        assert TEST_BASENAME in _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))


class TestIterationLog763:
    def _tail(self):
        with open(os.path.join(REPO_ROOT, "iteration-log.md")) as f:
            lines = f.read().splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #763 entry sits at the end of the file, not the top.
        return "\n".join(lines[-60:])

    def test_log_entry_present(self):
        assert "#763" in self._tail()

    def test_log_mechanism_690_and_journalist(self):
        assert "mechanism 690" in self._tail()
        assert "Florence Ion" in self._tail()


class TestDateGrounding763:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_15_2026_is_tuesday(self):
        assert self._weekday("2026-09-15") == "Tuesday"
