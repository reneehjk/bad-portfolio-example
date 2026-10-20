#!/usr/bin/env python3
"""Generate earnest-looking SVG mockups for the portfolio."""
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "assets"
OUT.mkdir(exist_ok=True)


def save(name, svg):
    (OUT / name).write_text(svg.strip() + "\n", encoding="utf-8")


def phone(x, y, w, h, bg, bars, accent, title=""):
    r = 18
    screen = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{bg}"/>'
    bezel = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="none" stroke="#1a1a1a" stroke-width="3"/>'
    notch = f'<rect x="{x + w * 0.32}" y="{y + 8}" width="{w * 0.36}" height="6" rx="3" fill="#111"/>'
    inner = []
    if title:
        inner.append(
            f'<text x="{x + 16}" y="{y + 42}" fill="{accent}" font-family="system-ui,sans-serif" font-size="11" font-weight="600">{title}</text>'
        )
    gy = y + 56
    for i, (bw, color) in enumerate(bars):
        inner.append(
            f'<rect x="{x + 16}" y="{gy}" width="{w * bw - 32}" height="10" rx="3" fill="{color}"/>'
        )
        gy += 18
        if i % 3 == 2:
            gy += 10
            inner.append(
                f'<rect x="{x + 16}" y="{gy}" width="{w - 32}" height="54" rx="8" fill="{accent}" opacity="0.18"/>'
            )
            gy += 68
    return screen + "".join(inner) + bezel + notch


def dashboard(w, h, bg, panel, accent, title):
    parts = [
        f'<rect width="{w}" height="{h}" fill="{bg}"/>',
        f'<rect width="160" height="{h}" fill="{panel}"/>',
        f'<rect x="24" y="28" width="90" height="12" rx="2" fill="{accent}"/>',
    ]
    for i, yy in enumerate(range(80, 320, 36)):
        fill = accent if i == 1 else "#ffffff33"
        parts.append(f'<rect x="24" y="{yy}" width="112" height="10" rx="2" fill="{fill}"/>')
    parts.append(f'<rect x="188" y="28" width="280" height="22" rx="4" fill="{panel}"/>')
    if title:
        parts.append(
            f'<text x="196" y="45" fill="#fff" font-family="system-ui,sans-serif" font-size="13">{title}</text>'
        )
    coords = [(188, 80, 280, 140), (484, 80, 280, 140), (188, 240, 576, 200)]
    for x, y, pw, ph in coords:
        parts.append(f'<rect x="{x}" y="{y}" width="{pw}" height="{ph}" rx="10" fill="#ffffff"/>')
        parts.append(f'<rect x="{x + 20}" y="{y + 24}" width="80" height="8" fill="#d0d5dd"/>')
        parts.append(f'<rect x="{x + 20}" y="{y + 48}" width="140" height="16" fill="{accent}"/>')
        parts.append(f'<rect x="{x + 20}" y="{y + 80}" width="{pw - 50}" height="8" fill="#eef1f4"/>')
        parts.append(f'<rect x="{x + 20}" y="{y + 100}" width="{pw - 90}" height="8" fill="#eef1f4"/>')
    return "\n".join(parts)


# ----- portraits / hero -----
save(
    "portrait.svg",
    """
<svg xmlns="http://www.w3.org/2000/svg" width="640" height="800" viewBox="0 0 640 800">
  <rect width="640" height="800" fill="#e8ddd0"/>
  <rect x="0" y="520" width="640" height="280" fill="#cfc3b4"/>
  <ellipse cx="320" cy="430" rx="150" ry="190" fill="#d8b49a"/>
  <ellipse cx="320" cy="250" rx="92" ry="108" fill="#e6c8b0"/>
  <ellipse cx="320" cy="188" rx="100" ry="70" fill="#3d2a22"/>
  <ellipse cx="278" cy="248" rx="8" ry="10" fill="#2c211c"/>
  <ellipse cx="362" cy="248" rx="8" ry="10" fill="#2c211c"/>
  <path d="M300 292 Q320 304 340 292" fill="none" stroke="#b07a62" stroke-width="4"/>
  <rect x="250" y="430" width="140" height="220" fill="#4a6fa5"/>
  <rect x="210" y="448" width="50" height="180" fill="#e6c8b0"/>
  <rect x="380" y="448" width="50" height="180" fill="#e6c8b0"/>
</svg>
""",
)

save(
    "hero.svg",
    """
<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="700" viewBox="0 0 1600 700">
  <rect width="1600" height="700" fill="#f6f1ea"/>
  <circle cx="1280" cy="120" r="220" fill="#ead9c8"/>
  <circle cx="200" cy="580" r="180" fill="#e2d3c4"/>
  <rect x="180" y="90" width="420" height="520" rx="8" fill="#d7c4b2"/>
  <rect x="640" y="140" width="360" height="440" rx="8" fill="#cbb7a6"/>
  <rect x="1040" y="70" width="380" height="560" rx="8" fill="#d3c0af"/>
</svg>
""",
)

# ----- SKB leasing phones -----
skb_bars = [
    (0.9, "#c9a227"),
    (0.7, "#d9d4c8"),
    (0.8, "#d9d4c8"),
    (0.55, "#1b365d"),
    (0.75, "#d9d4c8"),
    (0.6, "#d9d4c8"),
]
phones = [
    ("skb-1.svg", "Welcome"),
    ("skb-2.svg", "Inventory"),
    ("skb-3.svg", "Vehicle"),
    ("skb-4.svg", "Apply"),
    ("skb-5.svg", "Status"),
    ("skb-6.svg", "Profile"),
]
for name, title in phones:
    body = phone(70, 40, 220, 460, "#f7f4ee", skb_bars, "#1b365d", title)
    save(
        name,
        f'<svg xmlns="http://www.w3.org/2000/svg" width="360" height="540" viewBox="0 0 360 540"><rect width="360" height="540" fill="#ece7de"/>{body}</svg>',
    )

save(
    "skb-hero.svg",
    f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="720" viewBox="0 0 1400 720">
  <rect width="1400" height="720" fill="#1b365d"/>
  {phone(180, 80, 240, 520, "#f7f4ee", skb_bars, "#c9a227", "Home")}
  {phone(500, 80, 240, 520, "#f7f4ee", skb_bars, "#c9a227", "Browse")}
  {phone(820, 80, 240, 520, "#f7f4ee", skb_bars, "#c9a227", "Details")}
  {phone(1140, 80, 240, 520, "#f7f4ee", skb_bars, "#c9a227", "Apply")}
</svg>
""",
)

save(
    "skb-desktop.svg",
    f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="740" viewBox="0 0 1200 740">{dashboard(1200, 740, "#e9eef3", "#1b365d", "#c9a227", "SKB Leasing Admin")}</svg>',
)

save(
    "skb-grid.svg",
    """
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800" viewBox="0 0 1200 800">
  <rect width="1200" height="800" fill="#f4f0e8"/>
  <rect x="40" y="40" width="360" height="220" rx="12" fill="#1b365d"/>
  <rect x="420" y="40" width="360" height="220" rx="12" fill="#c9a227"/>
  <rect x="800" y="40" width="360" height="220" rx="12" fill="#4a5d4a"/>
  <rect x="40" y="290" width="360" height="220" rx="12" fill="#d9d4c8"/>
  <rect x="420" y="290" width="360" height="220" rx="12" fill="#1b365d"/>
  <rect x="800" y="290" width="360" height="220" rx="12" fill="#c9a227"/>
  <rect x="40" y="540" width="360" height="220" rx="12" fill="#4a5d4a"/>
  <rect x="420" y="540" width="360" height="220" rx="12" fill="#d9d4c8"/>
  <rect x="800" y="540" width="360" height="220" rx="12" fill="#1b365d"/>
</svg>
""",
)

# ----- stickies, journey, persona -----
save(
    "stickies.svg",
    """
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="700" viewBox="0 0 1200 700">
  <rect width="1200" height="700" fill="#f3f1ea"/>
  <rect x="40" y="40" width="160" height="140" fill="#fff3a1" transform="rotate(-4 120 110)"/>
  <rect x="230" y="70" width="160" height="140" fill="#ffd4e0" transform="rotate(3 310 140)"/>
  <rect x="430" y="40" width="160" height="140" fill="#c5e8c5" transform="rotate(-2 510 110)"/>
  <rect x="620" y="80" width="160" height="140" fill="#cde4ff" transform="rotate(5 700 150)"/>
  <rect x="820" y="50" width="160" height="140" fill="#fff3a1" transform="rotate(-6 900 120)"/>
  <rect x="1000" y="90" width="160" height="140" fill="#ffd4e0" transform="rotate(2 1080 160)"/>
  <rect x="80" y="280" width="160" height="140" fill="#cde4ff" transform="rotate(4 160 350)"/>
  <rect x="280" y="310" width="160" height="140" fill="#c5e8c5" transform="rotate(-3 360 380)"/>
  <rect x="480" y="270" width="160" height="140" fill="#fff3a1" transform="rotate(6 560 340)"/>
  <rect x="680" y="300" width="160" height="140" fill="#ffd4e0" transform="rotate(-2 760 370)"/>
  <rect x="880" y="280" width="160" height="140" fill="#cde4ff" transform="rotate(3 960 350)"/>
  <rect x="140" y="500" width="160" height="140" fill="#c5e8c5" transform="rotate(-5 220 570)"/>
  <rect x="360" y="520" width="160" height="140" fill="#fff3a1" transform="rotate(4 440 590)"/>
  <rect x="580" y="490" width="160" height="140" fill="#ffd4e0" transform="rotate(-3 660 560)"/>
  <rect x="800" y="510" width="160" height="140" fill="#cde4ff" transform="rotate(2 880 580)"/>
</svg>
""",
)

save(
    "journey.svg",
    """
<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="520" viewBox="0 0 1400 520">
  <rect width="1400" height="520" fill="#fafafa"/>
  <rect x="40" y="40" width="180" height="28" fill="#1c1c1c"/>
  <line x1="80" y1="240" x2="1320" y2="240" stroke="#ccc" stroke-width="4"/>
  <circle cx="160" cy="240" r="14" fill="#e07a5f"/>
  <circle cx="430" cy="240" r="14" fill="#e07a5f"/>
  <circle cx="700" cy="240" r="14" fill="#e07a5f"/>
  <circle cx="970" cy="240" r="14" fill="#e07a5f"/>
  <circle cx="1240" cy="240" r="14" fill="#e07a5f"/>
  <rect x="90" y="80" width="140" height="70" fill="#f3efe8"/>
  <rect x="360" y="80" width="140" height="70" fill="#f3efe8"/>
  <rect x="630" y="80" width="140" height="70" fill="#f3efe8"/>
  <rect x="900" y="80" width="140" height="70" fill="#f3efe8"/>
  <rect x="1170" y="80" width="140" height="70" fill="#f3efe8"/>
  <rect x="90" y="300" width="140" height="90" fill="#eee"/>
  <rect x="360" y="300" width="140" height="90" fill="#eee"/>
  <rect x="630" y="300" width="140" height="90" fill="#eee"/>
  <rect x="900" y="300" width="140" height="90" fill="#eee"/>
  <rect x="1170" y="300" width="140" height="90" fill="#eee"/>
  <rect x="90" y="410" width="140" height="50" fill="#f8d9d0"/>
  <rect x="360" y="410" width="140" height="50" fill="#f8d9d0"/>
  <rect x="630" y="410" width="140" height="50" fill="#e4f0d8"/>
  <rect x="900" y="410" width="140" height="50" fill="#e4f0d8"/>
  <rect x="1170" y="410" width="140" height="50" fill="#e4f0d8"/>
</svg>
""",
)

save(
    "persona.svg",
    """
<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="560" viewBox="0 0 1000 560">
  <rect width="1000" height="560" fill="#fff"/>
  <rect width="320" height="560" fill="#f3efe8"/>
  <circle cx="160" cy="160" r="78" fill="#e6c8b0"/>
  <ellipse cx="160" cy="148" rx="34" ry="40" fill="#d8b49a"/>
  <rect x="48" y="270" width="224" height="16" fill="#1c1c1c"/>
  <rect x="70" y="300" width="180" height="10" fill="#bbb"/>
  <rect x="380" y="48" width="200" height="14" fill="#1c1c1c"/>
  <rect x="380" y="80" width="540" height="10" fill="#ddd"/>
  <rect x="380" y="100" width="480" height="10" fill="#ddd"/>
  <rect x="380" y="120" width="500" height="10" fill="#ddd"/>
  <rect x="380" y="180" width="160" height="14" fill="#1c1c1c"/>
  <rect x="380" y="214" width="240" height="36" rx="18" fill="#e07a5f"/>
  <rect x="640" y="214" width="180" height="36" rx="18" fill="#ead9c8"/>
  <rect x="380" y="280" width="160" height="14" fill="#1c1c1c"/>
  <rect x="380" y="314" width="540" height="10" fill="#ddd"/>
  <rect x="380" y="334" width="500" height="10" fill="#ddd"/>
  <rect x="380" y="354" width="460" height="10" fill="#ddd"/>
  <rect x="380" y="400" width="160" height="14" fill="#1c1c1c"/>
  <rect x="380" y="434" width="540" height="10" fill="#ddd"/>
  <rect x="380" y="454" width="400" height="10" fill="#ddd"/>
</svg>
""",
)

save(
    "wireframes.svg",
    """
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="640" viewBox="0 0 1200 640">
  <rect width="1200" height="640" fill="#f5f5f5"/>
  <rect x="40" y="40" width="220" height="420" fill="#fff" stroke="#bbb"/>
  <rect x="60" y="70" width="180" height="16" fill="#ddd"/>
  <rect x="60" y="110" width="180" height="80" fill="#eee"/>
  <rect x="60" y="210" width="180" height="10" fill="#ddd"/>
  <rect x="60" y="230" width="140" height="10" fill="#ddd"/>
  <rect x="60" y="270" width="180" height="40" fill="#ccc"/>
  <rect x="300" y="40" width="220" height="420" fill="#fff" stroke="#bbb"/>
  <rect x="320" y="70" width="180" height="16" fill="#ddd"/>
  <rect x="320" y="110" width="80" height="80" fill="#eee"/>
  <rect x="420" y="110" width="80" height="80" fill="#eee"/>
  <rect x="320" y="210" width="180" height="10" fill="#ddd"/>
  <rect x="320" y="250" width="180" height="160" fill="#eee"/>
  <rect x="560" y="40" width="220" height="420" fill="#fff" stroke="#bbb"/>
  <rect x="580" y="70" width="180" height="24" fill="#ddd"/>
  <rect x="580" y="120" width="180" height="200" fill="#eee"/>
  <rect x="580" y="340" width="180" height="40" fill="#ccc"/>
  <rect x="820" y="40" width="340" height="420" fill="#fff" stroke="#bbb"/>
  <rect x="840" y="70" width="140" height="16" fill="#ddd"/>
  <rect x="840" y="110" width="300" height="80" fill="#eee"/>
  <rect x="840" y="210" width="140" height="100" fill="#eee"/>
  <rect x="1000" y="210" width="140" height="100" fill="#eee"/>
  <rect x="840" y="330" width="300" height="80" fill="#ddd"/>
</svg>
""",
)

# ----- Phoenix (sparse, dull) -----
save(
    "phoenix.svg",
    f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="740" viewBox="0 0 1200 740">{dashboard(1200, 740, "#eef1f4", "#4a5568", "#3182ce", "Phoenix Console")}</svg>',
)

save(
    "phoenix-thumb.svg",
    """
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="520" viewBox="0 0 800 520">
  <rect width="800" height="520" fill="#e8edf2"/>
  <rect x="40" y="40" width="720" height="40" fill="#4a5568"/>
  <rect x="40" y="100" width="200" height="380" fill="#fff"/>
  <rect x="60" y="130" width="160" height="10" fill="#cbd5e0"/>
  <rect x="60" y="160" width="140" height="10" fill="#3182ce"/>
  <rect x="60" y="190" width="150" height="10" fill="#cbd5e0"/>
  <rect x="260" y="100" width="500" height="180" fill="#fff"/>
  <rect x="280" y="130" width="200" height="14" fill="#4a5568"/>
  <rect x="280" y="170" width="440" height="8" fill="#e2e8f0"/>
  <rect x="280" y="190" width="380" height="8" fill="#e2e8f0"/>
  <rect x="260" y="300" width="240" height="180" fill="#fff"/>
  <rect x="520" y="300" width="240" height="180" fill="#fff"/>
</svg>
""",
)

# ----- Spotify-like app redesign -----
spot_bars = [
    (0.85, "#1db954"),
    (0.6, "#333"),
    (0.75, "#333"),
    (0.5, "#1db954"),
    (0.7, "#333"),
]
for i, title in enumerate(["Home", "Search", "Album", "Queue", "Profile", "Lyrics"], start=1):
    body = phone(70, 40, 220, 460, "#121212", spot_bars, "#1db954", title)
    save(
        f"app-{i}.svg",
        f'<svg xmlns="http://www.w3.org/2000/svg" width="360" height="540" viewBox="0 0 360 540"><rect width="360" height="540" fill="#0b0b0b"/>{body}</svg>',
    )

save(
    "app-hero.svg",
    f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="720" viewBox="0 0 1400 720">
  <rect width="1400" height="720" fill="#0b0b0b"/>
  {phone(220, 80, 240, 520, "#121212", spot_bars, "#1db954", "Home")}
  {phone(580, 80, 240, 520, "#121212", spot_bars, "#1db954", "Now Playing")}
  {phone(940, 80, 240, 520, "#121212", spot_bars, "#1db954", "Search")}
</svg>
""",
)

# ----- filler project thumbs -----
save(
    "bakery.svg",
    """
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="520" viewBox="0 0 800 520">
  <rect width="800" height="520" fill="#f4e4c1"/>
  <circle cx="400" cy="230" r="120" fill="#fff8ea" stroke="#c45c26" stroke-width="8"/>
  <text x="400" y="225" text-anchor="middle" font-family="Georgia,serif" font-size="28" fill="#c45c26">Rise &amp; Thyme</text>
  <text x="400" y="258" text-anchor="middle" font-family="Georgia,serif" font-size="12" fill="#8a5a3b">BAKERY · EST. 2024</text>
</svg>
""",
)

save(
    "poster.svg",
    """
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="1040" viewBox="0 0 800 1040">
  <rect width="800" height="1040" fill="#111"/>
  <rect x="40" y="40" width="720" height="960" fill="#f2ff3a"/>
  <text x="80" y="220" font-family="Impact,Arial Black,sans-serif" font-size="92" fill="#111">TYPE</text>
  <text x="80" y="330" font-family="Impact,Arial Black,sans-serif" font-size="92" fill="#ff2d95">NIGHT</text>
  <text x="80" y="420" font-family="Arial,sans-serif" font-size="22" fill="#111">THU 08.14 · ROOM 204 · 7PM</text>
  <rect x="80" y="520" width="280" height="280" fill="#111"/>
  <rect x="400" y="640" width="280" height="160" fill="#ff2d95"/>
</svg>
""",
)

save(
    "dribbble.svg",
    f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="740" viewBox="0 0 1200 740">{dashboard(1200, 740, "#1b1030", "#3d2463", "#b388ff", "Finly Overview")}</svg>',
)

save(
    "dayloop.svg",
    """
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="520" viewBox="0 0 800 520">
  <rect width="800" height="520" fill="#e7f6f2"/>
  <rect x="80" y="60" width="640" height="400" rx="16" fill="#fff"/>
  <rect x="110" y="90" width="180" height="22" fill="#1a9b7a"/>
  <rect x="110" y="140" width="580" height="50" rx="8" fill="#f0faf7"/>
  <rect x="110" y="206" width="580" height="50" rx="8" fill="#f0faf7"/>
  <rect x="110" y="272" width="580" height="50" rx="8" fill="#c8efe3"/>
  <rect x="110" y="338" width="580" height="50" rx="8" fill="#f0faf7"/>
</svg>
""",
)

save(
    "brand.svg",
    """
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="520" viewBox="0 0 800 520">
  <rect width="800" height="520" fill="#111"/>
  <text x="400" y="250" text-anchor="middle" font-family="Georgia,serif" font-size="64" fill="#e8d5a3">AL</text>
  <text x="400" y="300" text-anchor="middle" font-family="Georgia,serif" font-size="16" letter-spacing="8" fill="#e8d5a3">AVERY LANE</text>
</svg>
""",
)

save(
    "packaging.svg",
    """
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="520" viewBox="0 0 800 520">
  <rect width="800" height="520" fill="#dce6d8"/>
  <rect x="250" y="80" width="300" height="360" rx="8" fill="#f7f3ea"/>
  <rect x="250" y="80" width="300" height="70" fill="#6b8f71"/>
  <text x="400" y="270" text-anchor="middle" font-family="Georgia,serif" font-size="28" fill="#3d5a40">bloom box</text>
  <text x="400" y="304" text-anchor="middle" font-family="Georgia,serif" font-size="12" fill="#6b8f71">HAND &amp; BODY</text>
</svg>
""",
)

save(
    "uikit.svg",
    """
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="520" viewBox="0 0 800 520">
  <rect width="800" height="520" fill="#f6f4ff"/>
  <rect x="60" y="70" width="200" height="48" rx="24" fill="#7c5cbf"/>
  <rect x="280" y="70" width="200" height="48" rx="8" fill="#fff" stroke="#7c5cbf" stroke-width="2"/>
  <rect x="500" y="70" width="220" height="48" rx="8" fill="#1c1c1c"/>
  <circle cx="120" cy="200" r="36" fill="#7c5cbf"/>
  <circle cx="220" cy="200" r="36" fill="#cbb6f0"/>
  <rect x="300" y="170" width="420" height="16" rx="8" fill="#eee"/>
  <rect x="300" y="200" width="300" height="16" rx="8" fill="#7c5cbf"/>
  <rect x="60" y="280" width="680" height="160" rx="16" fill="#fff"/>
  <rect x="90" y="310" width="200" height="100" rx="8" fill="#efeafb"/>
  <rect x="310" y="310" width="200" height="100" rx="8" fill="#efeafb"/>
  <rect x="530" y="310" width="180" height="100" rx="8" fill="#efeafb"/>
</svg>
""",
)

print("wrote", len(list(OUT.glob("*.svg"))), "svgs to", OUT)
