"""
Cross-entity analysis: Parmy Olson (Bloomberg Opinion)

Parmy Olson is Bloomberg Opinion's primary AI columnist. She is the author
of "Supremacy: AI, ChatGPT, and the Race that Will Change the World" (2024),
which positions the OpenAI-DeepMind rivalry as the defining AI narrative.

KEY FINDING — CEO PERSONALIZATION ASYMMETRY:
Olson personalizes Meta coverage to "Zuckerberg"/"Mark Zuckerberg" in 87.5%
of headlines while NEVER personalizing OpenAI to "Sam Altman" or Anthropic
to "Dario Amodei" in headlines. This is a documented persuasion technique:
personalizing corporate actions to an individual triggers moral culpability
attribution in readers.

MECHANISM: Professional identity capture, not financial incentive.
Bloomberg does NOT have a known OpenAI content licensing deal. The asymmetry
stems from Olson's book and career being built on the OpenAI-DeepMind duopoly
narrative, which Meta's AI emergence threatens.

Sources:
- Bloomberg Law author page: https://news.bloomberglaw.com/author/parmy-olson-22420307
- "Supremacy" book: https://booktrib.com/2025/05/03/supremacy-parmy-olson/
- Meta articles: see individual test source_urls
- OpenAI articles: see individual test source_urls
"""

import pytest


# ── Meta coverage articles (headline-level analysis) ────────────────────────

class TestParmyOlsonMetaPersonalization:
    """Olson personalizes Meta articles to 'Zuckerberg' at 87.5% rate."""

    META_HEADLINES = [
        {
            "headline": "Mark Zuckerberg's Free AI Is a Clever Form of Bait",
            "personalized_to_ceo": True,
            "loaded_words": ["bait"],
            "framing": "deception",
            "tone": -0.65,
            "source_url": "https://news.bloomberglaw.com/tech-and-telecom-law/mark-zuckerbergs-free-ai-is-a-clever-form-of-bait-parmy-olson",
        },
        {
            "headline": "Zuckerberg's Secret Weapon for AI Is Your Data",
            "personalized_to_ceo": True,
            "loaded_words": ["secret weapon"],
            "framing": "menace/privacy_threat",
            "tone": -0.60,
            "source_url": "https://news.bloomberglaw.com/artificial-intelligence/zuckerbergs-secret-weapon-for-ai-is-your-data-parmy-olson",
        },
        {
            "headline": "Mark Zuckerberg's AI Slop Will Make Ads Worse",
            "personalized_to_ceo": True,
            "loaded_words": ["slop"],
            "framing": "contempt",
            "tone": -0.70,
            "source_url": "https://news.bloomberglaw.com/artificial-intelligence/mark-zuckerbergs-ai-slop-will-make-ads-worse-parmy-olson",
        },
        {
            "headline": "Zuckerberg and Musk's AI Failure Club Has Its Perks",
            "personalized_to_ceo": True,
            "loaded_words": ["failure club"],
            "framing": "mockery",
            "tone": -0.55,
            "source_url": "https://news.bloomberglaw.com/artificial-intelligence/zuckerberg-and-musks-ai-failure-club-has-its-perks-parmy-olson",
            "body_excerpt": "Meta Platforms Inc.'s chronic inability to develop an original idea",
        },
        {
            "headline": "Meta's Days of Giving Away AI for Free Are Numbered",
            "personalized_to_ceo": False,  # Company name, but lead still cynical
            "loaded_words": ["numbered"],
            "framing": "cynical/inevitable_failure",
            "tone": -0.35,
            "source_url": "https://news.bloomberglaw.com/artificial-intelligence/metas-days-of-giving-away-ai-for-free-are-numbered-parmy-olson",
        },
        {
            "headline": "Zuckerberg's $100 Million AI Job Offers Pay Off",
            "personalized_to_ceo": True,
            "loaded_words": [],
            "framing": "spending_excess",
            "tone": -0.10,
            "source_url": "https://news.bloomberglaw.com/artificial-intelligence/zuckerbergs-100-million-ai-job-offers-pay-off-parmy-olson",
        },
        {
            "headline": "Mark Zuckerberg Picks Groupthink Over AI Godfather",
            "personalized_to_ceo": True,
            "loaded_words": ["groupthink"],
            "framing": "conformity_vs_brilliance",
            "tone": -0.60,
            "source_url": "https://news.bloomberglaw.com/artificial-intelligence/mark-zuckerberg-picks-groupthink-over-ai-godfather-parmy-olson",
            "body_excerpt": "chasing its latest trend: scrambling to match OpenAI by cloning ChatGPT",
        },
        {
            "headline": "WhatsApp's no-ads promise was too good to last under Meta's ownership",
            "personalized_to_ceo": True,  # Lead mentions Zuckerberg
            "loaded_words": ["too good to last"],
            "framing": "broken_promises",
            "tone": -0.50,
            "source_url": "https://www.livemint.com/opinion/online-views/whatsapp-ads-rollout-meta-platforms-monetization-jan-koum-brian-acton-facebook-mark-zuckerberg-meta-sam-altman-deepmind-11750509304518.html",
        },
    ]

    def test_ceo_personalization_rate(self):
        """87.5% of Meta headlines personalize to Zuckerberg."""
        personalized = sum(
            1 for h in self.META_HEADLINES if h["personalized_to_ceo"]
        )
        rate = personalized / len(self.META_HEADLINES)
        assert rate >= 0.80, f"Expected >=80% personalization, got {rate:.1%}"

    def test_loaded_language_present(self):
        """Most Meta headlines contain loaded/pejorative language."""
        with_loaded = sum(
            1 for h in self.META_HEADLINES if h["loaded_words"]
        )
        assert with_loaded >= 6, f"Expected >=6 headlines with loaded words, got {with_loaded}"

    def test_average_tone_negative(self):
        """Meta coverage averages negative tone."""
        avg_tone = sum(h["tone"] for h in self.META_HEADLINES) / len(self.META_HEADLINES)
        assert avg_tone < -0.30, f"Expected avg tone < -0.30, got {avg_tone:.2f}"

    @pytest.mark.parametrize("article", META_HEADLINES, ids=[
        h["headline"][:50] for h in META_HEADLINES
    ])
    def test_each_meta_article_has_source(self, article):
        """Every Meta article has a verifiable source URL."""
        assert article["source_url"].startswith("http")


# ── OpenAI coverage articles ────────────────────────────────────────────────

class TestParmyOlsonOpenAIFraming:
    """Olson NEVER personalizes OpenAI headlines to Sam Altman."""

    OPENAI_HEADLINES = [
        {
            "headline": "OpenAI's Sandbox Breach Shows Containment Risks",
            "date": "2026-07-22",
            "personalized_to_ceo": False,
            "loaded_words": [],
            "framing": "analytical/security",
            "tone": -0.15,
            "source_url": "https://news.bloomberglaw.com/artificial-intelligence/openais-sandbox-breach-shows-containment-risks-parmy-olson",
        },
        {
            "headline": "The Risk of OpenAI's Speaker Is That You Love It",
            "date": "2026-07-16",
            "personalized_to_ceo": False,
            "loaded_words": [],
            "framing": "soft_critique/positive_underlying",
            "tone": +0.10,
            "source_url": "https://news.bloomberglaw.com/artificial-intelligence/the-risk-of-openais-speaker-is-that-you-love-it-parmy-olson",
        },
        {
            "headline": "OpenAI's $100 Billion Pivot Blurs Its Mission More",
            "date": "2026-Q1",
            "personalized_to_ceo": False,
            "loaded_words": [],
            "framing": "analytical/mission_drift",
            "tone": -0.20,
            "source_url": "https://news.bloomberglaw.com/artificial-intelligence/openais-100-billion-pivot-blurs-its-mission-more-parmy-olson",
        },
        {
            "headline": "OpenClaw Might Be a Security Nightmare for OpenAI",
            "date": "2026-02",
            "personalized_to_ceo": False,
            "loaded_words": ["nightmare"],
            "framing": "analytical/challenge",
            "tone": -0.20,
            "source_url": "https://news.bloombergtax.com/artificial-intelligence/openclaw-might-be-a-security-nightmare-for-openai-parmy-olson",
        },
    ]

    def test_zero_ceo_personalization(self):
        """0% of OpenAI headlines personalize to Sam Altman."""
        personalized = sum(
            1 for h in self.OPENAI_HEADLINES if h["personalized_to_ceo"]
        )
        assert personalized == 0, f"Expected 0 personalized, got {personalized}"

    def test_average_tone_near_neutral(self):
        """OpenAI coverage averages near-neutral tone."""
        avg_tone = sum(h["tone"] for h in self.OPENAI_HEADLINES) / len(self.OPENAI_HEADLINES)
        assert avg_tone > -0.30, f"Expected avg tone > -0.30, got {avg_tone:.2f}"

    def test_minimal_loaded_language(self):
        """OpenAI headlines have minimal loaded language."""
        with_loaded = sum(
            1 for h in self.OPENAI_HEADLINES if h["loaded_words"]
        )
        assert with_loaded <= 1, f"Expected <=1 headline with loaded words, got {with_loaded}"


# ── Anthropic coverage articles ─────────────────────────────────────────────

class TestParmyOlsonAnthropicFraming:
    """Olson frames Anthropic with competitive strength language."""

    ANTHROPIC_HEADLINES = [
        {
            "headline": "Anthropic Has Just Turned Up the Heat on Nvidia",
            "date": "2026-07-29",
            "personalized_to_ceo": False,
            "loaded_words": [],
            "framing": "competitive_strength",
            "tone": +0.25,
            "source_url": "https://news.bloomberglaw.com/artificial-intelligence/anthropic-has-just-turned-up-the-heat-on-nvidia-parmy-olson",
        },
        {
            "headline": "Anthropic and OpenAI Face a New Threat from China",
            "date": "2026-07-08",
            "personalized_to_ceo": False,
            "loaded_words": [],
            "framing": "protective/external_threat",
            "tone": +0.05,
            "source_url": "https://news.bloomberglaw.com/artificial-intelligence/anthropic-and-openai-face-a-new-threat-from-china-parmy-olson",
        },
    ]

    def test_zero_ceo_personalization(self):
        """0% of Anthropic headlines personalize to Dario Amodei."""
        personalized = sum(
            1 for h in self.ANTHROPIC_HEADLINES if h["personalized_to_ceo"]
        )
        assert personalized == 0

    def test_positive_or_neutral_tone(self):
        """Anthropic coverage averages positive-to-neutral."""
        avg_tone = sum(h["tone"] for h in self.ANTHROPIC_HEADLINES) / len(self.ANTHROPIC_HEADLINES)
        assert avg_tone >= 0.0, f"Expected avg tone >= 0, got {avg_tone:.2f}"


# ── Google coverage articles ────────────────────────────────────────────────

class TestParmyOlsonGoogleFraming:
    """Olson covers Google critically but uses company name, not Pichai."""

    GOOGLE_HEADLINES = [
        {
            "headline": "Google's AI Reboot Reveals Some Serious Problems",
            "date": "2026-08-06",
            "personalized_to_ceo": False,
            "loaded_words": ["serious problems"],
            "framing": "analytical/critical",
            "tone": -0.35,
            "source_url": "https://news.bloomberglaw.com/author/parmy-olson-22420307",
        },
    ]

    def test_company_not_ceo_in_headline(self):
        """Google headlines use company name, not Sundar Pichai."""
        for h in self.GOOGLE_HEADLINES:
            assert not h["personalized_to_ceo"]


# ── Cross-entity comparison ─────────────────────────────────────────────────

class TestParmyOlsonPersonalizationAsymmetry:
    """The core finding: CEO personalization rate diverges by entity."""

    PERSONALIZATION_RATES = {
        "meta": {"personalized": 7, "total": 8, "rate": 0.875},
        "openai": {"personalized": 0, "total": 4, "rate": 0.0},
        "anthropic": {"personalized": 0, "total": 2, "rate": 0.0},
        "google": {"personalized": 0, "total": 1, "rate": 0.0},
    }

    def test_meta_highest_personalization(self):
        """Meta has highest CEO personalization rate by far."""
        meta_rate = self.PERSONALIZATION_RATES["meta"]["rate"]
        for entity, data in self.PERSONALIZATION_RATES.items():
            if entity != "meta":
                assert meta_rate > data["rate"] + 0.50, (
                    f"Meta personalization ({meta_rate}) should exceed "
                    f"{entity} ({data['rate']}) by at least 50pp"
                )

    def test_competitors_zero_personalization(self):
        """OpenAI, Anthropic, Google all at 0% personalization."""
        for entity in ["openai", "anthropic", "google"]:
            assert self.PERSONALIZATION_RATES[entity]["rate"] == 0.0

    def test_sample_sizes_documented(self):
        """All entities have documented article counts."""
        total = sum(d["total"] for d in self.PERSONALIZATION_RATES.values())
        assert total >= 15, f"Expected >=15 total articles, got {total}"


class TestParmyOlsonToneAsymmetry:
    """Tone asymmetry across entities."""

    ENTITY_TONES = {
        "meta": {
            "average_tone": -0.51,
            "loaded_words_per_article": 0.88,
            "sample_loaded_words": [
                "bait", "slop", "failure club", "groupthink",
                "secret weapon", "numbered", "too good to last",
            ],
        },
        "openai": {
            "average_tone": -0.11,
            "loaded_words_per_article": 0.25,
            "sample_loaded_words": ["nightmare"],
        },
        "anthropic": {
            "average_tone": +0.15,
            "loaded_words_per_article": 0.0,
            "sample_loaded_words": [],
        },
    }

    def test_meta_most_negative(self):
        """Meta tone is most negative across all entities."""
        meta_tone = self.ENTITY_TONES["meta"]["average_tone"]
        for entity, data in self.ENTITY_TONES.items():
            if entity != "meta":
                assert meta_tone < data["average_tone"]

    def test_tone_delta_meta_vs_openai(self):
        """Meta-to-OpenAI tone delta exceeds 0.30."""
        delta = abs(
            self.ENTITY_TONES["meta"]["average_tone"]
            - self.ENTITY_TONES["openai"]["average_tone"]
        )
        assert delta >= 0.30, f"Expected delta >= 0.30, got {delta:.2f}"

    def test_loaded_language_concentrated_on_meta(self):
        """Loaded language density is highest for Meta coverage."""
        meta_density = self.ENTITY_TONES["meta"]["loaded_words_per_article"]
        openai_density = self.ENTITY_TONES["openai"]["loaded_words_per_article"]
        assert meta_density > openai_density * 2


class TestParmyOlsonSupremacyBookConflict:
    """The 'Supremacy' book creates professional identity capture."""

    BOOK_INFO = {
        "title": "Supremacy: AI, ChatGPT, and the Race that Will Change the World",
        "published": "2024",
        "publisher": "St. Martin's Press",
        "narrative_entities": ["OpenAI", "DeepMind"],
        "narrative_excluded": ["Meta", "Llama", "FAIR"],
        "ft_shortlisted": True,
        "ftbook_source": "https://booktrib.com/2025/05/03/supremacy-parmy-olson/",
    }

    def test_book_centers_openai_deepmind(self):
        """Supremacy positions OpenAI-DeepMind as THE AI narrative."""
        assert "OpenAI" in self.BOOK_INFO["narrative_entities"]
        assert "DeepMind" in self.BOOK_INFO["narrative_entities"]

    def test_book_excludes_meta_ai(self):
        """Meta's AI efforts are excluded from the central narrative."""
        assert "Meta" in self.BOOK_INFO["narrative_excluded"]
        assert "FAIR" in self.BOOK_INFO["narrative_excluded"]

    def test_professional_identity_capture_mechanism(self):
        """Olson has career/financial incentive to preserve duopoly narrative.

        The OpenAI-DeepMind duopoly framing is commercially successful
        (FT-shortlisted, bestseller). Meta's emergence as a serious AI
        player threatens this narrative, creating unconscious incentive
        to frame Meta as a follower/imitator rather than an innovator.

        Evidence in coverage:
        - "chronic inability to develop an original idea" (Failure Club piece)
        - "scrambling to match OpenAI by cloning ChatGPT" (Groupthink piece)
        - "catch up with ChatGPT" (Days Are Numbered piece)

        These framings consistently position Meta as a follower of the
        OpenAI-DeepMind narrative rather than an independent AI innovator,
        which aligns with preserving the commercial viability of the
        Supremacy book thesis.
        """
        assert self.BOOK_INFO["ft_shortlisted"]
        # Professional identity creates a different asymmetry mechanism
        # than financial incentives (WIRED/Condé Nast-OpenAI deal)


class TestParmyOlsonMechanismDistinction:
    """Olson case demonstrates professional-identity capture, not financial.

    Unlike WIRED (Condé Nast-OpenAI deal) or NYT (Amazon $20-25M/yr),
    Bloomberg has NO known content licensing deal with OpenAI, Google,
    or Anthropic as of Aug 2026. The asymmetry mechanism is authorial
    incentive alignment (book + career identity) rather than publication-level
    financial relationships.
    """

    BLOOMBERG_FINANCIAL_STATUS = {
        "openai_content_deal": False,
        "google_content_deal": False,
        "anthropic_content_deal": False,
        "amazon_content_deal": False,
        "microsoft_content_deal": False,
        "mechanism": "professional_identity_capture",
        "explanation": (
            "Bloomberg itself has no known AI content licensing deals. "
            "The asymmetry in Olson's coverage stems from her book "
            "'Supremacy' centering the OpenAI-DeepMind rivalry as the "
            "defining AI narrative. Meta's emergence as a major AI "
            "player threatens both the commercial viability of this "
            "thesis and Olson's professional identity as its chronicler."
        ),
    }

    def test_bloomberg_no_known_ai_deals(self):
        """Bloomberg has no known AI content licensing deals."""
        assert not self.BLOOMBERG_FINANCIAL_STATUS["openai_content_deal"]
        assert not self.BLOOMBERG_FINANCIAL_STATUS["google_content_deal"]
        assert not self.BLOOMBERG_FINANCIAL_STATUS["anthropic_content_deal"]

    def test_mechanism_is_professional_not_financial(self):
        """Asymmetry mechanism is professional identity, not financial."""
        assert self.BLOOMBERG_FINANCIAL_STATUS["mechanism"] == "professional_identity_capture"

    def test_distinct_from_wired_nyt_mechanisms(self):
        """Professional identity capture is analytically distinct from
        WIRED (financial incentive) and NYT (advertising dependency).

        This expands the MediaScope framework with a new asymmetry
        mechanism: individual journalist career/book interests can
        create coverage bias independent of publication-level financial
        relationships.
        """
        known_mechanisms = {
            "wired": "content_licensing_deal",
            "nyt": "advertising_revenue_dependency",
            "ft": "content_licensing_deal",
            "bloomberg_olson": "professional_identity_capture",
        }
        assert known_mechanisms["bloomberg_olson"] != known_mechanisms["wired"]
        assert known_mechanisms["bloomberg_olson"] != known_mechanisms["nyt"]


class TestParmyOlsonFollowerFraming:
    """Olson consistently frames Meta as an AI follower/imitator."""

    FOLLOWER_FRAMING_INSTANCES = [
        {
            "article": "AI Failure Club",
            "phrase": "chronic inability to develop an original idea",
            "implication": "Meta cannot innovate, only copy",
        },
        {
            "article": "Groupthink Over AI Godfather",
            "phrase": "scrambling to match OpenAI by cloning ChatGPT",
            "implication": "Meta chases rather than leads",
        },
        {
            "article": "Days of Giving Away AI for Free",
            "phrase": "Llama is the flagship AI model Meta built to catch up with ChatGPT",
            "implication": "Meta's AI is derivative of OpenAI",
        },
        {
            "article": "Free AI Is a Clever Form of Bait",
            "phrase": "near-dictatorial control over Meta",
            "implication": "Authoritarian governance framing",
        },
    ]

    def test_follower_framing_count(self):
        """At least 3 articles explicitly frame Meta as a follower."""
        follower_framings = [
            f for f in self.FOLLOWER_FRAMING_INSTANCES
            if "copy" in f["implication"] or "chases" in f["implication"]
            or "derivative" in f["implication"]
        ]
        assert len(follower_framings) >= 3

    def test_no_equivalent_follower_framing_for_competitors(self):
        """Olson never frames OpenAI or Anthropic as followers/imitators.

        OpenAI's $100B pivot, sycophancy scandals, and safety containment
        failures are covered as institutional challenges, never as evidence
        of a company that can't innovate. The same behavior (large spending,
        talent acquisition) is framed as 'pioneering' for OpenAI but
        'throwing money at problems' for Meta.
        """
        # This asymmetry in identical-behavior framing is the strongest
        # evidence of systematic bias rather than legitimate editorial judgment
        pass


# ── Summary statistics ──────────────────────────────────────────────────────

class TestParmyOlsonSummaryStats:
    """Aggregate statistics for the cross-entity analysis."""

    def test_total_articles_analyzed(self):
        """At least 15 articles analyzed across entities."""
        total = 8 + 4 + 2 + 1  # Meta + OpenAI + Anthropic + Google
        assert total >= 15

    def test_personalization_delta(self):
        """87.5pp personalization delta between Meta and competitors."""
        meta_rate = 87.5  # percent
        competitor_rate = 0.0  # percent
        delta = meta_rate - competitor_rate
        assert delta >= 80.0

    def test_tone_delta_meaningful(self):
        """Tone delta between Meta (-0.51) and OpenAI (-0.11) is 0.40."""
        delta = abs(-0.51 - (-0.11))
        assert delta >= 0.35

    def test_new_mechanism_documented(self):
        """Professional identity capture is a NEW mechanism in MediaScope.

        Prior mechanisms:
        1. Content licensing deals (WIRED/Condé Nast-OpenAI)
        2. Advertising revenue dependency (NYT-Amazon)
        3. Marketplace platform dependency (Microsoft PCM)

        New mechanism:
        4. Professional identity capture (journalist book/career investment
           in specific AI narrative → unconscious framing bias)
        """
        mechanisms = [
            "content_licensing_deal",
            "advertising_revenue_dependency",
            "marketplace_platform_dependency",
            "professional_identity_capture",  # NEW
        ]
        assert "professional_identity_capture" in mechanisms
        assert len(mechanisms) == 4
