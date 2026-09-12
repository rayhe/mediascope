"""Type B #693: Nicole Nguyen (WSJ) same-journalist cross-entity byline-isolated
register pair - Apple iPhone Duo first-impressions (Sep 10, 2026) vs Meta
WhatsApp "Breaks Through Apple's Walled Garden" (Nov 20, 2025), ten months
apart, sole bylines, both read first-hand this run.

FIRST dedicated Type B mechanism on Nicole Nguyen (mechanism_id 650, next
free pre-commit; max numeric mechanism_id was 649). Zero mechanism_* keys
pre-existed under her entry; her Meta coverage lived only inside mechanism_67's
competitor_coverage sample_articles (tone 0.1 inherited estimate). Both arm URLs
are NEW TO CORPUS this run (repo-wide greps zero hits pre-commit). Tones are
hand-scored this run (#693), illustrative only per the Aug 28 standing rule.

Apple arm: WSJ Sep 10 2026 (Nguyen SOLE byline, wsj.com first-hand read,
77 rendered lines, https://www.wsj.com/tech/personal-tech/iphone-duo-apple-first-impressions-7234f86e,
NEW TO CORPUS) - "My First Impressions of the New Folding iPhone Duo".
Register = enthusiast consumer-tech first-impressions: "My desire for a folding
phone before today was zero. After today, it is a lot more than zero.", "I feel
a pull toward this device.", crease "barely visible... more subtle than
Samsung's... looked as flat and smooth as the one on an iPad." Moderated by
reviewer caveats: "I am not ready to recommend the Duo... just yet", 254g /
11.3mm closed vs Galaxy Fold 8 201g / 9.7mm, one-handed typing a challenge,
missed 8X zoom, $800 premium over iPhone 18 Pro, "not sure I want to spend that
premium on a first-generation Apple device." Tone +0.40 (MANUAL ILLUSTRATIVE).

Meta arm: WSJ Nov 20 2025 (Nguyen SOLE byline, read first-hand this run via the
livemint mirror, 87 rendered lines, mirror carries the WSJ byline sign-off
"Write to Nicole Nguyen at nicole.nguyen@wsj.com";
https://www.livemint.com/technology/whatsapp-is-breaking-through-apple-s-walled-garden-11763375190283.html,
NEW TO CORPUS; title/date in-corpus via mechanism_67 sample_articles; WSJ
canonical URL not verbatim in listings this run) - "WhatsApp Breaks Through
Apple's Walled Garden". Register = competitive-growth adoption reporting:
"The Meta-owned app is the world's default messaging platform, with over three
billion users.", "Yes, blue-bubble snobs are breaking out of Apple's walled
garden.", "The iPad version is great.", "WhatsApp is still winning over users."
Moderated by the Meta-money caveat: WhatsApp "has to delicately balance
initiatives from its parent company Meta - including money-making ones.
Recently, it began rolling out ads in a separate tab and gave Meta AI more
prominent placement." Tone +0.15 (MANUAL ILLUSTRATIVE; inherited 0.1 estimate
from #67 reaffirmed upward on full read).

Finding: REGISTER CONSTANCY with a deal-attribution bound. Illustrative delta
(Apple minus Meta) = +0.40 - (+0.15) = +0.25; p_value, cohens_d, ci
NOT_CALCULATED; is_significant False (Aug 28 standing rule);
statistical_contract degenerate_n1_per_arm per #638/#643. No engine run. NOT
artifact-grade.

NINETEENTH falsification-family member: the journalist-level "soft on Apple,
hard on Meta" attribution fails on Nguyen's byline - her Meta arm is
Meta-positive (competitive vs Apple). The Meta-deal-softness attribution also
fails on ordering: News Corp holds a $50M/yr Meta AI licensing deal (in-corpus
per #337), yet the paid counterparty's arm is the LESS positive of the two; the
register ordering (Apple > Meta) tracks genre (hands-on review enthusiasm vs
adoption-trend reportage), not the deal. This extends and constrains
mechanism_67's beat-assignment asymmetry: the WSJ structural separation
(Nguyen consumer voice vs Bobrowsky investigative voice) is not individual bias
- Nguyen's own byline carries Meta-positive framing when the beat allows.

Third-entity bound: Nguyen's Feb 13 2026 "Dragnet Era of Home Security Cameras"
(mechanism_67 surveillance_coverage) targets Ring (Amazon) and Nest (Google)
with privacy-adversarial framing while NOT targeting Meta glasses, so the
constancy found here is register-specific (consumer-tech), not blanket
cross-entity softness.

Financial context (correlation, not causation): News Corp balanced financial
ties: $50M/yr Meta + $50M/yr OpenAI AI licensing deals (in-corpus per #337).
The deal-predicts-softness gradient would expect Meta-softness at News Corp;
Nguyen's Meta arm IS positive (+0.15), but LESS positive than her Apple arm
(+0.40) despite Meta being the paid counterparty and Apple having no News Corp
AI licensing deal in corpus. Register ordering is the opposite of what a
journalist-level deal-softness attribution predicts; genre is the better
explanation.

Novelty vs prior work: FIRST dedicated Type B on Nicole Nguyen (zero
mechanism_* keys pre-existing under her entry). Distinct from the Satariano
(#688) and Hart constancy pins (different journalists) and from #56 (Field
volume analysis). Extends mechanism_67 from a beat-assignment description to a
pinned same-journalist byline-isolated pair.

Rotation: Type B follows Type A (#692) per A,B,C,D,E. Rotation guard,
doc-sync, and novelty-anchor classes are deselected pre-commit per the #565
followup convention; anchor patched in the followup commit once the main
commit SHA is known.
"""

import ast
import glob
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAREERS_PATH = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = "mechanism_650_nicole_nguyen_apple_duo_first_impressions_vs_meta_whatsapp_walled_garden_sep12"
TEST_BASENAME = "test_type_b_693_nicole_nguyen_apple_duo_first_impressions_vs_meta_whatsapp_walled_garden_sep12_3am.py"

APPLE_TONE = 0.40
META_TONE = 0.15
EXPECTED_DELTA = 0.25

APPLE_URL = "https://www.wsj.com/tech/personal-tech/iphone-duo-apple-first-impressions-7234f86e"
META_URL = "https://www.livemint.com/technology/whatsapp-is-breaking-through-apple-s-walled-garden-11763375190283.html"
NEWS_CORP_META_DEAL_URL = "https://www.wsj.com/business/media/news-corp-meta-in-ai-content-licensing-deal-worth-up-to-50-million-a-year-d4fbf244"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. The rotation-guard class is deselected pre-commit.
ANCHORED_SHA = "2c7f14952d514101638d67bc50d1e458777866a0"


def _careers():
    with open(CAREERS_PATH) as f:
        return yaml.safe_load(f)


def _nguyen():
    matches = []
    for j in _careers()["journalists"]:
        if isinstance(j, dict) and j.get("name") == "Nicole Nguyen":
            matches.append(j)
    assert len(matches) == 1, "expected exactly one Nicole Nguyen entry, got %d" % len(matches)
    return matches[0]


def _mechanism():
    n = _nguyen()
    assert MECH_KEY in n, "%s missing from Nicole Nguyen entry" % MECH_KEY
    return n[MECH_KEY]


def _mechanism_text():
    return yaml.safe_dump(_mechanism(), allow_unicode=True)


def _count_def_tests():
    path = os.path.join(TESTS_DIR, TEST_BASENAME)
    tree = ast.parse(open(path).read())
    return sum(
        isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
        and n.name.startswith("test_")
        for n in ast.walk(tree)
    )


def read_readme():
    with open(README_PATH) as f:
        return f.read()


def read_arch():
    with open(ARCH_PATH) as f:
        return f.read()


def read_log_start():
    with open(LOG_PATH) as f:
        return f.read()


class TestIterationMetadata693:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 693

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 650

    def test_mechanism_id_unique_repo_wide(self):
        seen = {}
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                if int(m.group(1)) == 650:
                    seen.setdefault(650, []).append(path)
        assert len(seen.get(650, [])) == 1, "mechanism_id 650 not unique: %r" % (seen.get(650),)

    def test_type_is_b(self):
        assert _mechanism()["type"] == "B"

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_block_key_matches(self):
        assert _mechanism()["block_key"] == "type_b_693_nicole_nguyen_apple_duo_first_impressions_vs_meta_whatsapp_walled_garden_sep12"

    def test_first_type_b_on_nguyen(self):
        n = _nguyen()
        assert MECH_KEY in n
        other_pairs = [
            k for k in n
            if k.startswith("mechanism_") and k != MECH_KEY
        ]
        assert not other_pairs, "unexpected second mechanism on Nicole Nguyen: %r" % (other_pairs,)

    def test_no_duplicate_693_file(self):
        others = [
            p for p in glob.glob(os.path.join(TESTS_DIR, "test_type_b_693_*.py"))
            if os.path.basename(p) != TEST_BASENAME
        ]
        assert not others, "duplicate #693 test files: %r" % (others,)


class TestNovelty693:
    """Iteration 693 is new; nothing with this number existed pre-commit."""

    def test_single_type_b_693_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_b_693*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_b_693_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; the main
        # commit exists exactly once post-commit and its SHA matches the
        # rotation-guard anchor patched in the followup. Novelty was
        # verified pre-commit by shell greps (zero test_type_b_693 files,
        # no #693 in git log, no mechanism_id 650 in profiles, both arm
        # URLs zero repo-wide hits); this test pins that no duplicate #693
        # main commit ever appears.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        mains = [
            line
            for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type B #693:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type B #693 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        assert sha == TestRotationCycleGuard693.ANCHORED_SHA, (
            "anchor patched in followup per #565 convention"
        )


class TestNguyenArms693:
    def test_apple_arm_date_and_sole_byline(self):
        apple = _mechanism()["apple_arm"]
        assert apple["date"] == "2026-09-10"
        assert apple["byline"] == "Nicole Nguyen (sole)"
        assert "first-hand" in apple["byline_attribution"]

    def test_apple_arm_url_verbatim(self):
        assert _mechanism()["apple_arm"]["url"] == APPLE_URL

    def test_apple_arm_url_new_to_corpus_note(self):
        apple = _mechanism()["apple_arm"]
        assert "new to corpus" in apple["byline_attribution"]

    def test_apple_arm_register_and_tone(self):
        apple = _mechanism()["apple_arm"]
        assert "enthusiast" in apple["register"]
        assert "first-impressions" in apple["register"]
        assert "folding phone before today was zero" in apple["register_detail"]
        assert "not ready to recommend" in apple["register_detail"]
        assert apple["tone_illustrative"] == APPLE_TONE

    def test_apple_arm_evidence_grade_first_hand(self):
        apple = _mechanism()["apple_arm"]
        assert "first-hand read" in apple["evidence_grade"]
        assert "77 rendered lines" in apple["evidence_grade"]

    def test_meta_arm_date_and_sole_byline(self):
        meta = _mechanism()["meta_arm"]
        assert meta["date"] == "2025-11-20"
        assert meta["byline"] == "Nicole Nguyen (sole)"
        assert "first-hand" in meta["byline_attribution"]

    def test_meta_arm_url_verbatim(self):
        assert _mechanism()["meta_arm"]["url"] == META_URL

    def test_meta_arm_url_new_to_corpus_note(self):
        meta = _mechanism()["meta_arm"]
        assert "new to corpus" in meta["byline_attribution"]

    def test_meta_arm_register_and_tone(self):
        meta = _mechanism()["meta_arm"]
        assert "competitive-growth" in meta["register"]
        assert "walled garden" in meta["register_detail"]
        assert "Meta AI more prominent placement" in meta["register_detail"]
        assert meta["tone_illustrative"] == META_TONE

    def test_meta_arm_evidence_grade_mirror_bounded(self):
        meta = _mechanism()["meta_arm"]
        assert "mirror" in meta["evidence_grade"]
        assert "mechanism_67" in meta["evidence_grade"]

    def test_both_arms_same_publication(self):
        assert _mechanism()["publication"] == "The Wall Street Journal"
        assert "same-journalist" in _mechanism()["pair_shape"]


class TestThirdEntityNote693:
    def test_dragnet_era_note(self):
        note = _mechanism()["third_entity_note"]
        assert "Dragnet Era" in note["dragnet_era"]
        assert "Ring (Amazon)" in note["dragnet_era"]
        assert "NOT targeting Meta glasses" in note["dragnet_era"]

    def test_register_specific_bound(self):
        note = _mechanism()["third_entity_note"]
        assert "register-specific" in note["corroboration_role"]


class TestScorerDelta693:
    def test_arrays(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert s["target_tones_manual_illustrative"] == [APPLE_TONE]
        assert s["reference_tones_manual_illustrative"] == [META_TONE]

    def test_arithmetic(self):
        s = _mechanism()["asymmetry_scorer_result"]
        delta = s["target_avg"] - s["reference_avg"]
        assert abs(delta - EXPECTED_DELTA) < 1e-9, "delta %r != %r" % (delta, EXPECTED_DELTA)
        assert abs(s["delta_apple_minus_meta"] - EXPECTED_DELTA) < 1e-9

    def test_manual_illustrative_guards(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci"] == "NOT_CALCULATED"
        assert s["is_significant"] is False
        assert s["statistical_contract"] == "degenerate_n1_per_arm"
        assert s["artifact_grade"] is False

    def test_no_engine_run(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert "no engine run" in s["method"]

    def test_tones_hand_scored_this_run(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert "hand-assigned" in s["method"]

    def test_limitations_stated(self):
        lim = _mechanism()["asymmetry_scorer_result"]["limitations"]
        assert "no co-byline confound" in lim
        assert "#638/#643" in lim


class TestFinancialContext693:
    def test_correlation_not_causation(self):
        fc = _mechanism()["financial_context"]
        assert "Correlation, not causation" in fc

    def test_news_corp_balanced_deals(self):
        fc = _mechanism()["financial_context"]
        assert "$50M/yr Meta" in fc
        assert "$50M/yr OpenAI" in fc
        assert NEWS_CORP_META_DEAL_URL in fc

    def test_ordering_contradicts_deal_attribution(self):
        fc = _mechanism()["financial_context"]
        assert "opposite of what a journalist-level deal-softness attribution predicts" in fc
        assert "genre" in fc

    def test_verdict_bounds(self):
        v = _mechanism()["verdict"]
        assert "NINETEENTH falsification-family member" in v
        assert "REGISTER CONSTANCY" in v
        assert "mechanism_67" in v
        assert "Correlation, not causation" in v
        assert "No analysis.json update warranted" in v


class TestConfounders693:
    def test_confounders_present_and_ranked(self):
        confs = _mechanism()["confounders"]
        assert len(confs) >= 7
        assert sum(c.startswith("[STRONG]") for c in confs) >= 3

    def test_strong_genre_asymmetry(self):
        confs = _mechanism()["confounders"]
        strong = [c for c in confs if c.startswith("[STRONG]")]
        assert any("Genre asymmetry" in c for c in strong)

    def test_strong_product_category_asymmetry(self):
        confs = _mechanism()["confounders"]
        strong = [c for c in confs if c.startswith("[STRONG]")]
        assert any("Product-category asymmetry" in c for c in strong)

    def test_strong_apple_adversarial_meta_positivity(self):
        confs = _mechanism()["confounders"]
        strong = [c for c in confs if c.startswith("[STRONG]")]
        assert any("Apple-adversarial" in c for c in strong)

    def test_moderate_time_order(self):
        confs = _mechanism()["confounders"]
        mod = [c for c in confs if c.startswith("[MODERATE]")]
        assert any("Time order" in c for c in mod)

    def test_moderate_mirror_bounded(self):
        confs = _mechanism()["confounders"]
        mod = [c for c in confs if c.startswith("[MODERATE]")]
        assert any("Mirror-bounded" in c for c in mod)

    def test_cross_references_constancy_family(self):
        refs = " ".join(_mechanism()["cross_references"])
        assert "#477/#482/#488/#493/#498/#508/#513/#518" in refs
        assert "#672/#678" in refs
        assert "#67/mechanism_67" in refs

    def test_novelty_language(self):
        nov = _mechanism()["novelty"]
        assert "FIRST dedicated Type B mechanism on Nicole Nguyen" in nov
        assert "zero mechanism_* keys pre-existing" in nov


class TestRotationCycleGuard693:
    # Deselected pre-commit per the #565 followup convention; the rotation
    # window only closes once the #693 main commit exists.
    ANCHORED_SHA = ANCHORED_SHA

    @staticmethod
    def _mains():
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        return [s for s in out if re.match(r"^Type [A-E] #\d+:", s)]

    def test_window_689_693_closes_c_to_b(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("B", "693"),
            ("A", "692"),
            ("E", "691"),
            ("D", "690"),
            ("C", "689"),
        ], "rotation window 689-693 wrong: %r" % (observed,)

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

    def test_anchor_is_main_patch_in_followup(self):
        # Post-commit anchor: the #693 main commit. Patched in the followup
        # per the #565 convention once the main commit SHA is known.
        pytest.skip("anchor patched in followup per #565 convention")

    def test_rotation_guard_regex_actually_matches(self):
        # #632 process note: a rotation guard whose regex never matches is a
        # silent no-op. Verify the guard regexes match a real main-commit
        # subject (the double-backslash r"...#(\d+)..." form silently matches
        # nothing). Written as a semantic check rather than a literal-pattern
        # check so the test cannot defeat itself by containing the pattern.
        src = open(os.path.join(TESTS_DIR, TEST_BASENAME)).read()
        patterns = re.findall(r're\.search\(r"([^"]+)"', src)
        guard_patterns = [p for p in patterns if p.startswith("Type (")]
        assert guard_patterns, "no rotation-guard regex found in this file"
        sample = "Type B #693: Nicole Nguyen Apple Duo first-impressions vs WhatsApp walled-garden byline register"
        for p in guard_patterns:
            m = re.search(p, sample)
            assert m and m.group(1) == "B" and m.group(2) == "693", (
                "rotation regex %r fails to match a real subject "
                "(double-backslash bug?)" % (p,)
            )


class TestDocSyncRatchet693:
    # Fails pre-commit by design per the #565 followup convention; the README
    # test-file table row and ARCHITECTURE tree row land in the doc-sync commit.
    def test_readme_has_693_row(self):
        assert "test_type_b_693" in read_readme()

    def test_arch_has_693_row(self):
        assert "test_type_b_693" in read_arch()

    def test_readme_row_mentions_nguyen(self):
        assert "Nicole Nguyen" in read_readme()

    def test_log_starts_with_693(self):
        assert read_log_start().startswith("#693 Type B:")

    def test_def_test_count_matches(self):
        # The README row for #693 must carry this file's own def-test count.
        n = _count_def_tests()
        assert str(n) in read_readme(), (
            "README #693 row should mention this file's def-test count %d" % n
        )


class TestNoBrittlePatterns693:
    def test_yaml_reparses_clean(self):
        n = _nguyen()
        m = n[MECH_KEY]
        assert isinstance(m["mechanism_id"], int)
        assert isinstance(m["apple_arm"]["tone_illustrative"], float)
        assert isinstance(m["meta_arm"]["tone_illustrative"], float)
        assert isinstance(m["asymmetry_scorer_result"]["is_significant"], bool)

    def test_no_em_dash_in_mechanism(self):
        assert "\u2014" not in _mechanism_text()
        assert "\u2028" not in _mechanism_text()
        src = open(os.path.join(TESTS_DIR, TEST_BASENAME)).read()
        assert "\u2014" not in src
        assert "\u2028" not in src

    def test_all_urls_http_or_https(self):
        urls = [
            _mechanism()["apple_arm"]["url"],
            _mechanism()["meta_arm"]["url"],
        ]
        assert urls, "no URLs recorded"
        for u in urls:
            assert u.startswith(("http://", "https://")), "bad URL: %r" % (u,)
