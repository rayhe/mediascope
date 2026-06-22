"""HTML dashboard generator for MediaScope analysis.

Generates a standalone, dark-themed, responsive HTML dashboard with
inline SVG charts. No external JavaScript dependencies.
"""

from __future__ import annotations

import html
import math
from datetime import datetime
from typing import Any, Optional


def generate_dashboard(data: dict, output_path: str) -> str:
    """Generate a standalone HTML dashboard from report data.

    Args:
        data: Report data dict with expected keys:
            - "publication_slug" (str)
            - "target_entity" (str)
            - "period_start" (str)
            - "period_end" (str)
            - "total_articles" (int)
            - "target_articles" (int)
            - "peer_articles" (int)
            - "overall_asymmetry" (float)
            - "asymmetry_by_entity" (dict[str, dict]) — per-entity scores
            - "journalist_rankings" (list[tuple[str, float]])
            - "framing_devices" (list[tuple[str, int]])
            - "top_articles" (list[dict])
        output_path: File path to write the HTML to.

    Returns:
        The output_path (for chaining).
    """
    pub = _esc(data.get("publication_slug", "Unknown"))
    target = _esc(data.get("target_entity", "Unknown"))
    period_start = _esc(data.get("period_start", ""))
    period_end = _esc(data.get("period_end", ""))
    total = data.get("total_articles", 0)
    target_count = data.get("target_articles", 0)
    peer_count = data.get("peer_articles", 0)
    overall_asym = data.get("overall_asymmetry", 0.0)
    asymmetry_by_entity = data.get("asymmetry_by_entity", {})
    journalist_rankings = data.get("journalist_rankings", [])
    framing_devices = data.get("framing_devices", [])
    top_articles = data.get("top_articles", [])
    generated_at = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    # Build SVG charts
    asymmetry_chart = _bar_chart(
        [(e, s.get("asymmetry_score", 0)) for e, s in asymmetry_by_entity.items()],
        title="Sentiment Asymmetry by Entity",
        color_fn=lambda v: "#ef4444" if v < 0 else "#22c55e",
    )

    journalist_chart = _bar_chart(
        journalist_rankings[:10],
        title="Top 10 Journalists by Asymmetry",
        color_fn=lambda v: "#ef4444" if v < 0 else "#22c55e",
    )

    framing_chart = _bar_chart(
        framing_devices[:10],
        title="Top Framing Devices",
        color_fn=lambda _: "#6366f1",
    )

    # Build article rows
    article_rows = ""
    for a in top_articles[:15]:
        tone = a.get("tone", 0)
        tone_color = "#ef4444" if tone < -0.1 else "#22c55e" if tone > 0.1 else "#94a3b8"
        title_text = _esc(a.get("title", "Untitled"))
        author_text = _esc(a.get("author", "Unknown"))
        date_text = _esc(str(a.get("date", ""))[:10])
        article_rows += f"""
            <tr>
                <td>{title_text}</td>
                <td>{author_text}</td>
                <td>{date_text}</td>
                <td style="color:{tone_color};font-weight:bold">{tone:.3f}</td>
            </tr>"""

    # Assemble HTML
    asym_color = "#ef4444" if overall_asym < 0 else "#22c55e"

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>MediaScope Dashboard — {pub}</title>
<style>
  :root {{
    --bg: #0f172a; --surface: #1e293b; --border: #334155;
    --text: #e2e8f0; --muted: #94a3b8; --accent: #6366f1;
    --red: #ef4444; --green: #22c55e;
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
         background: var(--bg); color: var(--text); padding: 2rem; line-height: 1.6; }}
  h1 {{ font-size: 1.8rem; margin-bottom: .25rem; }}
  h2 {{ font-size: 1.3rem; margin: 2rem 0 1rem; color: var(--accent); }}
  .subtitle {{ color: var(--muted); margin-bottom: 2rem; }}
  .cards {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; }}
  .card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 12px;
           padding: 1.25rem; }}
  .card .label {{ font-size: .85rem; color: var(--muted); text-transform: uppercase;
                  letter-spacing: .05em; }}
  .card .value {{ font-size: 2rem; font-weight: 700; margin-top: .25rem; }}
  .chart-container {{ background: var(--surface); border: 1px solid var(--border);
                      border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem;
                      overflow-x: auto; }}
  table {{ width: 100%; border-collapse: collapse; margin-top: .5rem; }}
  th, td {{ padding: .6rem 1rem; text-align: left; border-bottom: 1px solid var(--border); }}
  th {{ color: var(--muted); font-size: .85rem; text-transform: uppercase; }}
  tr:hover td {{ background: rgba(99,102,241,.08); }}
  .footer {{ margin-top: 3rem; color: var(--muted); font-size: .8rem; text-align: center; }}
  svg text {{ fill: var(--text); font-family: inherit; }}
  @media (max-width: 600px) {{ body {{ padding: 1rem; }} .cards {{ grid-template-columns: 1fr; }} }}
</style>
</head>
<body>
  <h1>📊 MediaScope Dashboard</h1>
  <p class="subtitle">{pub} — coverage of {target} — {period_start} to {period_end}</p>

  <div class="cards">
    <div class="card">
      <div class="label">Total Articles</div>
      <div class="value">{total}</div>
    </div>
    <div class="card">
      <div class="label">{target} Articles</div>
      <div class="value">{target_count}</div>
    </div>
    <div class="card">
      <div class="label">Peer Articles</div>
      <div class="value">{peer_count}</div>
    </div>
    <div class="card">
      <div class="label">Overall Asymmetry</div>
      <div class="value" style="color:{asym_color}">{overall_asym:+.3f}</div>
    </div>
  </div>

  <h2>Sentiment Asymmetry by Entity</h2>
  <div class="chart-container">{asymmetry_chart}</div>

  <h2>Journalist Asymmetry Rankings</h2>
  <div class="chart-container">{journalist_chart}</div>

  <h2>Top Articles by Bias Score</h2>
  <div class="chart-container">
    <table>
      <thead><tr><th>Title</th><th>Author</th><th>Date</th><th>Tone</th></tr></thead>
      <tbody>{article_rows}</tbody>
    </table>
  </div>

  <h2>Framing Devices</h2>
  <div class="chart-container">{framing_chart}</div>

  <div class="footer">
    Generated by MediaScope v0.1.0 · {generated_at}
  </div>
</body>
</html>"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(page)

    return output_path


# ── SVG chart helpers ────────────────────────────────────────────────

def _bar_chart(
    items: list[tuple[str, float]],
    title: str = "",
    width: int = 700,
    bar_height: int = 28,
    color_fn=None,
) -> str:
    """Generate a horizontal bar chart as inline SVG.

    Args:
        items: List of (label, value) pairs.
        title: Chart title.
        width: SVG width.
        bar_height: Height of each bar.
        color_fn: Optional callable(value) → color string.

    Returns:
        SVG string.
    """
    if not items:
        return '<p style="color:var(--muted)">No data available.</p>'

    if color_fn is None:
        color_fn = lambda _: "#6366f1"

    label_width = 180
    chart_width = width - label_width - 80
    padding_top = 30 if title else 10
    height = padding_top + len(items) * (bar_height + 6) + 10

    max_abs = max(abs(v) for _, v in items) if items else 1
    if max_abs == 0:
        max_abs = 1

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="100%" style="max-width:{width}px">',
    ]

    if title:
        svg_lines.append(
            f'<text x="{width // 2}" y="20" text-anchor="middle" '
            f'font-size="14" font-weight="600" fill="#94a3b8">{_esc(title)}</text>'
        )

    for i, (label, value) in enumerate(items):
        y = padding_top + i * (bar_height + 6)
        bar_w = abs(value) / max_abs * chart_width
        bar_w = max(bar_w, 2)  # minimum visible
        color = color_fn(value)

        # Label
        svg_lines.append(
            f'<text x="{label_width - 8}" y="{y + bar_height * 0.7}" '
            f'text-anchor="end" font-size="12" fill="#e2e8f0">'
            f'{_esc(str(label)[:25])}</text>'
        )

        # Bar
        svg_lines.append(
            f'<rect x="{label_width}" y="{y + 2}" '
            f'width="{bar_w:.1f}" height="{bar_height - 4}" '
            f'rx="4" fill="{color}" opacity="0.85"/>'
        )

        # Value label
        svg_lines.append(
            f'<text x="{label_width + bar_w + 6}" y="{y + bar_height * 0.7}" '
            f'font-size="11" fill="#94a3b8">{value:+.3f}</text>'
        )

    svg_lines.append("</svg>")
    return "\n".join(svg_lines)


def _esc(text: str) -> str:
    """HTML-escape a string."""
    return html.escape(str(text))
