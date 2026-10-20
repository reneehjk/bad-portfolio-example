#!/usr/bin/env python3
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "assets"


def save(name, svg):
    (OUT / name).write_text(svg.strip() + "\n", encoding="utf-8")


def phone(x, y, w, h, bg, bars, accent, title=""):
    r = 18
    parts = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{bg}"/>',
    ]
    if title:
        parts.append(
            f'<text x="{x + 16}" y="{y + 42}" fill="{accent}" font-family="system-ui,sans-serif" font-size="11" font-weight="600">{title}</text>'
        )
    gy = y + 56
    for i, (bw, color) in enumerate(bars):
        parts.append(
            f'<rect x="{x + 16}" y="{gy}" width="{w * bw - 32}" height="10" rx="3" fill="{color}"/>'
        )
        gy += 18
        if i % 3 == 2:
            gy += 10
            parts.append(
                f'<rect x="{x + 16}" y="{gy}" width="{w - 32}" height="54" rx="8" fill="{accent}" opacity="0.18"/>'
            )
            gy += 68
    parts.append(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="none" stroke="#1a1a1a" stroke-width="3"/>'
    )
    parts.append(
        f'<rect x="{x + w * 0.32}" y="{y + 8}" width="{w * 0.36}" height="6" rx="3" fill="#111"/>'
    )
    return "".join(parts)


def set_phones(prefix, bg_page, screen, accent, titles):
    bars = [(0.85, accent), (0.62, "#d8d8d8"), (0.74, "#d8d8d8"), (0.5, accent), (0.7, "#d8d8d8")]
    for i, title in enumerate(titles, 1):
        body = phone(70, 40, 220, 460, screen, bars, accent, title)
        save(
            f"{prefix}-{i}.svg",
            f'<svg xmlns="http://www.w3.org/2000/svg" width="360" height="540" viewBox="0 0 360 540"><rect width="360" height="540" fill="{bg_page}"/>{body}</svg>',
        )
    phones = "".join(
        phone(80 + i * 330, 80, 240, 520, screen, bars, accent, t)
        for i, t in enumerate(titles[:4])
    )
    save(
        f"{prefix}-hero.svg",
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="720" viewBox="0 0 1400 720"><rect width="1400" height="720" fill="{bg_page}"/>{phones}</svg>',
    )


set_phones("shop", "#f3f7f4", "#ffffff", "#2f6f4e", ["Home", "Browse", "Product", "Cart", "Checkout", "Account"])
set_phones("food", "#fff4ec", "#ffffff", "#e07a5f", ["Home", "Menu", "Item", "Cart", "Track", "Profile"])
set_phones("health", "#eef4f6", "#ffffff", "#2a6f86", ["Home", "Visit", "Records", "Messages"])

save(
    "shop-desktop.svg",
    """
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="740" viewBox="0 0 1200 740">
  <rect width="1200" height="740" fill="#eef3ef"/>
  <rect width="1200" height="64" fill="#2f6f4e"/>
  <rect x="40" y="96" width="360" height="280" rx="10" fill="#fff"/>
  <rect x="420" y="96" width="360" height="280" rx="10" fill="#fff"/>
  <rect x="800" y="96" width="360" height="280" rx="10" fill="#fff"/>
  <rect x="40" y="400" width="360" height="280" rx="10" fill="#fff"/>
  <rect x="420" y="400" width="360" height="280" rx="10" fill="#fff"/>
  <rect x="800" y="400" width="360" height="280" rx="10" fill="#fff"/>
</svg>
""",
)

print("ok")
