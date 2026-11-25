"""Generate the profile stat cards (assets/stats.svg, assets/languages.svg).

Runs in GitHub Actions on a schedule with the workflow's GITHUB_TOKEN, using only
public data and the standard library, so the profile has no third-party stats service.
"""
import json
import os
import pathlib
import urllib.request
from xml.sax.saxutils import escape

USER = os.environ.get("PROFILE_USER", "coopersimpson101-debug")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT = pathlib.Path(__file__).resolve().parent.parent / "assets"

BG, BORDER, FG, MUTED = "#0d1117", "#30363d", "#e6edf3", "#8b949e"
FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
LANG_COLORS = {
    "C": "#555555", "Python": "#3572A5", "TypeScript": "#3178c6", "WGSL": "#1a5e9a",
    "JavaScript": "#f1e05a", "Assembly": "#6E4C13", "Objective-C": "#438eff", "Metal": "#8f14e9",
    "Shell": "#89e051", "HTML": "#e34c26", "CSS": "#663399", "Makefile": "#427819",
    "C++": "#f34b7d", "Jupyter Notebook": "#DA5B0B",
}
FALLBACK = ["#F97316", "#22D3EE", "#A78BFA", "#34D399", "#FBBF24", "#F472B6", "#60A5FA", "#2DD4BF"]


def api(url, data=None):
    req = urllib.request.Request(url, data=data, headers={
        "Accept": "application/vnd.github+json", "User-Agent": "profile-stats",
        **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def gql(query):
    return api("https://api.github.com/graphql", json.dumps({"query": query}).encode())["data"]


def collect():
    repos, page = [], 1
    while True:
        batch = api(f"https://api.github.com/users/{USER}/repos?type=owner&per_page=100&page={page}")
        repos += batch
        if len(batch) < 100:
            break
        page += 1
    repos = [r for r in repos if not r["fork"] and not r["archived"] and r["name"] != USER]
    langs = {}
    for r in repos:
        for lang, n in api(r["languages_url"]).items():
            langs[lang] = langs.get(lang, 0) + n
    c = gql(f'{{ user(login: "{USER}") {{ contributionsCollection {{ contributionCalendar {{ totalContributions }} '
            f'totalCommitContributions totalIssueContributions totalPullRequestContributions }} }} }}')
    cc = c["user"]["contributionsCollection"]
    return {
        "repos": len(repos),
        "stars": sum(r["stargazers_count"] for r in repos),
        "contributions": cc["contributionCalendar"]["totalContributions"],
        "commits": cc["totalCommitContributions"],
        "issues": cc["totalIssueContributions"],
        "prs": cc["totalPullRequestContributions"],
        "langs": langs,
    }


def card(w, h, title, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{escape(title)}">'
            f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="10" fill="{BG}" stroke="{BORDER}"/>'
            f'<text x="24" y="38" fill="{FG}" font-family="{FONT}" font-size="17" font-weight="700">{escape(title)}</text>'
            f'{body}</svg>')


def stats_svg(s):
    rows = [("Public projects", s["repos"]),
            ("Public contributions, last year", s["contributions"]),
            ("Public commits, last year", s["commits"]),
            ("Issues opened, last year", s["issues"])]
    if s["stars"] >= 10:
        rows.insert(1, ("Stars", s["stars"]))
    body = ""
    for i, (k, v) in enumerate(rows):
        y = 80 + i * 32
        body += (f'<text x="24" y="{y}" fill="{MUTED}" font-family="{FONT}" font-size="14">{escape(k)}</text>'
                 f'<text x="470" y="{y}" fill="{FG}" font-family="{FONT}" font-size="14" font-weight="700" '
                 f'text-anchor="end">{v:,}</text>')
    return card(495, 200, "GitHub activity", body)


def languages_svg(langs):
    total = sum(langs.values()) or 1
    top = sorted(langs.items(), key=lambda kv: -kv[1])[:8]
    colors = [LANG_COLORS.get(k, FALLBACK[i % len(FALLBACK)]) for i, (k, _) in enumerate(top)]
    x, bar = 24.0, ""
    for (k, n), c in zip(top, colors):
        w = 447 * n / total
        bar += f'<rect x="{x:.2f}" y="56" width="{max(w, 1):.2f}" height="10" fill="{c}"/>'
        x += w
    body = f'<clipPath id="r"><rect x="24" y="56" width="447" height="10" rx="5"/></clipPath><g clip-path="url(#r)">{bar}</g>'
    for i, ((k, n), c) in enumerate(zip(top, colors)):
        cx, cy = 24 + (i % 2) * 230, 98 + (i // 2) * 28
        body += (f'<circle cx="{cx + 6}" cy="{cy - 5}" r="6" fill="{c}"/>'
                 f'<text x="{cx + 20}" y="{cy}" fill="{FG}" font-family="{FONT}" font-size="14">{escape(k)}</text>'
                 f'<text x="{cx + 205}" y="{cy}" fill="{MUTED}" font-family="{FONT}" font-size="14" '
                 f'text-anchor="end">{100 * n / total:.1f}%</text>')
    return card(495, 200, "Languages (by code size)", body)


def main():
    s = collect()
    OUT.mkdir(exist_ok=True)
    (OUT / "stats.svg").write_text(stats_svg(s), encoding="utf-8")
    (OUT / "languages.svg").write_text(languages_svg(s["langs"]), encoding="utf-8")
    print(json.dumps({k: v for k, v in s.items() if k != "langs"}))


if __name__ == "__main__":
    main()
