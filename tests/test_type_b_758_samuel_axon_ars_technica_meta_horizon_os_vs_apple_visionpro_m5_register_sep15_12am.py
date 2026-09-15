"""Type B #758: Samuel Axon (Ars Technica) Meta Horizon OS platform-news register
vs Apple Vision Pro M5 affectionate-skeptic long-term-review register.

Mechanism 688. FIRST dedicated corpus mechanism on Samuel Axon - zero hits
repo-wide (profiles/ + tests/) pre-commit, git-grep-verified this run.

Meta arm: Ars Technica Apr 22 2024 "Meta debuts Horizon OS, with Asus,
Lenovo, and Microsoft on board", byline Samuel Axon (relay-attested) -
platform-opening business news register, +0.30 MANUAL ILLUSTRATIVE,
headline/dek/byline-bounded per #503.

Apple arm: Ars Technica circa Nov 2025 Apple Vision Pro M5 long-term review,
byline Samuel Axon (relay-attested, "Sameuel Axon for Ars Technica" sic) -
affectionate-skeptic long-term review register, +0.15 MANUAL ILLUSTRATIVE,
excerpt-bounded per #503 ("I still like the Vision Pro, but I can tell it's
hanging on by a thread", "practicality beat coolness", "I hope Apple keeps
working on it").

Illustrative delta (Meta minus Apple) +0.15, near-null with Meta-favoring
sign. Genre asymmetry (news vs review, 19 months apart) is the dominant
confound. Financial context: Ars Technica is a Conde Nast (Advance
Publications) property; no documented Advance/Conde Nast AI licensing deal
with Meta or Apple in the corpus; the in-corpus Advance chain points at
Reddit (governance/voting), not AI licensing - zero-gradient control.

TWENTY-SIXTH falsification-family member (ledger 25->26). Verdict:
directionally_supported_not_proven. NOT artifact-grade. No analysis.json
update. Excerpt-bounded per #503; no browser.open this run.

Rotation: 754-758 window closing C->D->E->A->B (anchor patched post-commit
per #565).
"""

import glob
import os
import re
import subprocess

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST_BASENAME = os.path.basename(__file__)
MECH_KEY = "samuel axon ars technica meta horizon os vs apple vision pro m5 register contrast sep15"
MECH_NUM = 688

HORIZON_URL = "https://technewstube.com/ars-technica/1633955/meta-horizon-os-asus-lenovo-microsoft-board/"
M5_REVIEW_URL = "https://macdailynews.com/2025/11/26/ars-technica-reviews-apples-m5-vision-pro-hope-apple-keeps-working-on-it/"
M5_REVIEW_TECHCRATIC_URL = "https://techcratic.com/index.php/2025/11/26/vision-pro-m5-review-its-time-for-apple-to-make-some-tough-choices/ars-technica/ars-technica/"
YOUTUBE_APP_URL = "https://techcratic.com/index.php/2026/02/12/it-took-two-years-but-google-released-a-youtube-app-on-vision-pro/ars-technica/ars-technica/"

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


class TestNovelty758:
    """Samuel Axon is new to the corpus: zero pre-commit hits."""

    def test_zero_axon_in_other_test_files(self):
        # Filesystem walk (not git grep): the new file is untracked
        # pre-commit, and git grep only sees tracked files.
        hits = [
            f
            for f in glob.glob(os.path.join(REPO_ROOT, "tests", "*.py"))
            if "Samuel Axon"
            in open(f, encoding="utf-8", errors="replace").read()
        ]
        assert hits == [os.path.join(REPO_ROOT, "tests", TEST_BASENAME)], hits

    def test_axon_in_profiles_only_new_block_and_careers(self):
        hits = _repo_grep("Samuel Axon", roots=("profiles",))
        assert sorted(hits) == [
            os.path.join("profiles", "careers", "journalists.yaml"),
            os.path.join("profiles", "competitor-coverage-research.yaml"),
        ], hits

    def test_zero_underscore_688_repo_wide_outside_this_file(self):
        hits = _repo_grep("mechanism" + "_688")
        hits = [h for h in hits if h != os.path.join("tests", TEST_BASENAME)]
        assert hits == [], hits

    def test_first_dedicated_mechanism_on_axon(self):
        corpus = _profiles_corpus()
        # Research block uses "mechanism_id: 688"; the careers backlink uses
        # the plural "mechanism_ids: [688]". Exactly one colon-form hit means
        # no other 688 block exists.
        assert corpus.count("mechanism_id: 688") == 1


class TestSourceEvidence758:
    def test_four_source_urls_verbatim_in_block(self):
        block = _block()
        for url in (
            HORIZON_URL,
            M5_REVIEW_URL,
            M5_REVIEW_TECHCRATIC_URL,
            YOUTUBE_APP_URL,
        ):
            assert url in block, "missing URL: %s" % url

    def test_meta_arm_byline_attestation(self):
        block = _fold(_block())
        assert "By Samuel Axon Apr 22, 2024" in block
        assert "Meta debuts Horizon OS" in block

    def test_apple_arm_byline_attestation(self):
        block = _fold(_block())
        assert "Sameuel Axon for Ars Technica" in block
        assert "hanging on by a thread" in block
        assert "practicality beat coolness" in block
        assert "Hope Apple keeps working on it" in block

    def test_excerpt_bounded_per_503(self):
        block = _fold(_block())
        assert "Search-excerpt-bounded per #503" in block
        assert "no browser.open this run" in block or "browser.open not attempted" in block


class TestRotationCycleGuard758:
    """Rotation: 754-758 window closes C->D->E->A->B, #753-style."""

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

    def test_window_754_758_closes_c_to_b(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("B", "758"),
            ("A", "757"),
            ("E", "756"),
            ("D", "755"),
            ("C", "754"),
        ], "rotation window 754-758 wrong: %r" % (observed,)

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


class TestMechanism688Content:
    def test_mech_block_present_in_research(self):
        corpus = _research()
        assert MECH_KEY + ":" in corpus
        assert "mechanism_id: 688" in corpus

    def test_iteration_metadata(self):
        block = _block()
        assert "iteration: 758" in block
        assert "rotation_type: B" in block
        assert "discovery_date: '2026-09-15'" in block
        assert "type: B" in block

    def test_journalist_fields(self):
        block = _block()
        assert "journalist: 'Samuel Axon'" in block
        assert "publication: ars technica" in block
        assert "owner: conde nast (advance publications)" in block

    def test_meta_arm_quotes(self):
        block = _fold(_block())
        assert "Meta debuts Horizon OS" in block
        assert "Asus, Lenovo, and Microsoft on board" in block
        assert "open up the operating system" in block

    def test_apple_arm_quotes(self):
        block = _fold(_block())
        assert "hanging on by a thread" in block
        assert "Content is light, developer support is tepid" in block
        assert "it''s amazing" in block
        assert "not going to be as big as the iPhone" in block

    def test_supporting_arm(self):
        block = _fold(_block())
        assert "Feb 12 2026 Vision Pro YouTube-app news" in block
        assert "review-specific, not a standing anti-Apple posture" in block

    def test_manual_illustrative_discipline(self):
        block = _fold(_block())
        assert "MANUAL ILLUSTRATIVE" in block
        assert "+0.30" in block
        assert "+0.15" in block
        assert "p_value: NOT_CALCULATED" in block
        assert "cohens_d: NOT_CALCULATED" in block
        assert "ci_95: NOT_CALCULATED" in block
        assert "is_significant: false" in block
        assert "statistical_contract: degenerate_n1_per_arm" in block
        assert "NOT artifact-grade" in block

    def test_wong_analogue_bounds(self):
        block = _fold(_block())
        assert "mechanism: 698" in block
        assert "Raymond Wong" in block
        assert "mechanism 686" in block
        assert "journalist-specific, not genre-general" in block

    def test_financial_context_advance_chain(self):
        block = _fold(_block())
        assert "Advance" in block
        assert "Conde Nast" in block
        assert "mechanism 305" in block
        assert "NULL" in block
        assert "zero-gradient control" in block
        assert "Reddit" in block

    def test_confounder_strength_layers(self):
        confounders = _block_data()["confounders"]
        assert len(confounders) == 8, "expected 8 confounders, got %d" % len(confounders)
        flat = " ".join(confounders)
        assert flat.count("STRONG:") == 3
        assert flat.count("MODERATE:") == 3
        assert flat.count("WEAK:") == 2

    def test_three_counterevidence(self):
        counter = _block_data()["counterevidence"]
        assert len(counter) == 3, "expected 3 counterevidence, got %d" % len(counter)
        assert all("COUNTEREVIDENCE:" in c for c in counter)

    def test_verdict_ledger_and_careers_backlink(self):
        block = _fold(_block())
        assert "directionally_supported_not_proven" in block
        assert "TWENTY-SIXTH falsification-family member" in block
        assert "ledger 25->26" in block
        assert "Correlation only" in block
        careers = _careers()
        assert "name: Samuel Axon" in careers
        assert "mechanism_ids: [688]" in careers
        assert "Type B #758" in careers


class TestSupersessionAndCorpusPost757:
    def _ids(self):
        return [
            int(x)
            for x in re.findall(r"mechanism_id:\s*(\d+)\b", _profiles_corpus())
        ]

    def test_max_mechanism_id_is_688(self):
        ids = self._ids()
        assert max(ids) == MECH_NUM, max(ids)

    def test_757_max_687_sweep_fails_by_designed_supersession(self):
        # Documented, not repaired: advancing max numeric mechanism id to 688
        # supersedes #757's test_max_numeric_mechanism_id_is_687 per the
        # #710/#720 convention.
        assert max(self._ids()) == MECH_NUM != 687

    def test_757_zero_numeric_688_sweep_fails_by_designed_supersession(self):
        # #757 asserted zero "mechanism_id: 688" hits in profiles/; the new
        # block supersedes it by design.
        hits = _repo_grep("mechanism_id: 688", roots=("profiles",))
        assert len(hits) >= 1, hits

    def test_757_zero_underscore_688_sweep_stays_green_by_designed_keying(self):
        hits = _repo_grep("mechanism" + "_688")
        hits = [h for h in hits if h != os.path.join("tests", TEST_BASENAME)]
        assert hits == [], hits

    def test_688_descriptive_key_unique_repo_wide(self):
        corpus = _profiles_corpus()
        assert corpus.count(MECH_KEY + ":") == 1
        tests_hits = [
            f for f in glob.glob(os.path.join(REPO_ROOT, "tests", "*.py"))
            if MECH_KEY in open(f, encoding="utf-8", errors="replace").read()
        ]
        assert tests_hits == [os.path.join(REPO_ROOT, "tests", TEST_BASENAME)], tests_hits


class TestLedger758:
    def test_falsification_ledger_advances_to_26(self):
        corpus = _profiles_corpus()
        assert "TWENTY-SIXTH" in corpus
        assert "TWENTY-SEVENTH" not in corpus


class TestDocSync758:
    def test_readme_row(self):
        assert TEST_BASENAME in _read(os.path.join(REPO_ROOT, "README.md"))

    def test_architecture_row(self):
        assert TEST_BASENAME in _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))


class TestIterationLog758:
    def _tail(self):
        with open(os.path.join(REPO_ROOT, "iteration-log.md")) as f:
            lines = f.read().splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #758 entry sits at the end of the file, not the top.
        return "\n".join(lines[-60:])

    def test_log_entry_present(self):
        assert "#758" in self._tail()

    def test_log_mechanism_688_and_journalist(self):
        assert "mechanism 688" in self._tail()
        assert "Samuel Axon" in self._tail()


class TestDateGrounding758:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_15_2026_is_tuesday(self):
        assert self._weekday("2026-09-15") == "Tuesday"
