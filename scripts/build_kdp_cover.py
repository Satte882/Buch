#!/usr/bin/env python3
import argparse
import random
from pathlib import Path

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from reportlab.lib.units import inch

TRIM_W = 5.06
TRIM_H = 7.81
BLEED = 0.125
SPINE_FACTORS = {"white": 0.002252, "cream": 0.0025}


def font_path(candidates):
    for candidate in candidates:
        if Path(candidate).exists():
            return candidate
    raise FileNotFoundError(candidates)


def tracked(c, text, font, size, tracking, cx, y):
    widths = [pdfmetrics.stringWidth(ch, font, size) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = cx - total / 2
    c.setFont(font, size)
    for ch, width in zip(text, widths):
        c.drawString(x, y, ch)
        x += width + tracking


def build(output: Path, pages: int, paper: str):
    spine_w = pages * SPINE_FACTORS[paper]
    cover_w = BLEED + TRIM_W + spine_w + TRIM_W + BLEED
    cover_h = BLEED + TRIM_H + BLEED
    spine_left = BLEED + TRIM_W
    spine_right = spine_left + spine_w
    front_left = spine_right
    front_right = cover_w

    bold = font_path([
        "/usr/share/fonts/truetype/roboto/unhinted/RobotoCondensed-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf",
    ])
    reg = font_path([
        "/usr/share/fonts/truetype/roboto/unhinted/RobotoCondensed-Regular.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed.ttf",
    ])
    pdfmetrics.registerFont(TTFont("NF-Bold", bold))
    pdfmetrics.registerFont(TTFont("NF-Reg", reg))

    W, H = cover_w * inch, cover_h * inch
    c = canvas.Canvas(
        str(output),
        pagesize=(W, H),
        pageCompression=1,
        initialFontName="NF-Bold",
        initialFontSize=10,
    )
    c.setTitle("NORMALFALL - KDP Paperback Cover")
    c.setSubject(
        f"KDP cover: trim {TRIM_W:.2f} x {TRIM_H:.2f} in; "
        f"{pages} pages; paper={paper}; spine={spine_w:.6f} in; "
        f"full cover={cover_w:.6f} x {cover_h:.3f} in"
    )

    black = Color(0.025, 0.025, 0.025)
    off = Color(0.88, 0.87, 0.84)
    grey = Color(0.67, 0.66, 0.63)
    red = Color(0.78, 0.055, 0.03)

    # Full-bleed dark background.
    c.setFillColor(black)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Subtle deterministic grain on the front panel.
    random.seed(882)
    c.saveState()
    try:
        c.setFillAlpha(0.09)
    except Exception:
        pass
    for _ in range(650):
        x = random.uniform(front_left, cover_w) * inch
        y = random.uniform(0, cover_h) * inch
        g = random.uniform(0.2, 0.55)
        c.setFillColor(Color(g, g, g))
        s = random.uniform(0.15, 0.6)
        c.rect(x, y, s, s, fill=1, stroke=0)
    c.restoreState()

    front_cx = (front_left + front_right) / 2 * inch

    # Large, cold, condensed title.
    title = "NORMALFALL"
    size = 60
    tracking = 0.8
    max_w = (TRIM_W - 0.28) * inch
    while (
        sum(pdfmetrics.stringWidth(ch, "NF-Bold", size) for ch in title)
        + tracking * (len(title) - 1)
        > max_w
    ):
        size -= 0.25
    c.setFillColor(off)
    tracked(c, title, "NF-Bold", size, tracking, front_cx, 6.47 * inch)

    # Ordered line field: all straight, one clearly deviating.
    x0 = (front_left + 0.42) * inch
    x1 = (front_right - 0.38) * inch
    bar_count = 18
    gap = (x1 - x0) / (bar_count - 1)
    bar_w = 0.071 * inch
    y_bottom = 0.98 * inch
    y_top = 5.95 * inch
    gap_y0 = 2.53 * inch
    gap_y1 = 2.76 * inch

    random.seed(20260902)
    for i in range(bar_count):
        x = x0 + i * gap
        if i != 9:
            c.setFillColor(grey)
            c.rect(x - bar_w / 2, y_bottom, bar_w, gap_y0 - y_bottom, fill=1, stroke=0)
            c.rect(x - bar_w / 2, gap_y1, bar_w, y_top - gap_y1, fill=1, stroke=0)
            c.setFillColor(black)
            for _ in range(7):
                yy = random.uniform(y_bottom, y_top)
                if gap_y0 < yy < gap_y1:
                    continue
                hh = random.uniform(0.015, 0.045) * inch
                ww = random.uniform(0.25, 0.75) * bar_w
                c.rect(x - ww / 2, yy, ww, hh, fill=1, stroke=0)
        else:
            # Red bar as a slightly tilted quadrilateral, broken at the impact point.
            c.setFillColor(red)
            tilt = 0.16 * inch
            p = c.beginPath()
            p.moveTo(x - bar_w / 2 + tilt * 0.15, gap_y1)
            p.lineTo(x + bar_w / 2 + tilt * 0.15, gap_y1)
            p.lineTo(x + bar_w / 2 + tilt, y_top)
            p.lineTo(x - bar_w / 2 + tilt, y_top)
            p.close()
            c.drawPath(p, fill=1, stroke=0)

            c.setFillColor(Color(0.45, 0.025, 0.015))
            p = c.beginPath()
            p.moveTo(x - bar_w / 2, gap_y0)
            p.lineTo(x + bar_w / 2, gap_y0)
            p.lineTo(x + bar_w / 2 - 0.03 * inch, y_bottom)
            p.lineTo(x - bar_w / 2 - 0.03 * inch, y_bottom)
            p.close()
            c.drawPath(p, fill=1, stroke=0)

            c.setFillColor(red)
            for _ in range(26):
                dx = random.uniform(-0.19, 0.18) * inch
                dy = random.uniform(-0.18, 0.18) * inch
                s = random.uniform(0.008, 0.028) * inch
                c.rect(x + dx, gap_y0 + dy, s, s, fill=1, stroke=0)
            c.setFillColor(off)
            for _ in range(12):
                dx = random.uniform(-0.16, 0.17) * inch
                dy = random.uniform(-0.12, 0.14) * inch
                s = random.uniform(0.008, 0.025) * inch
                c.rect(x + dx, gap_y0 + dy, s, s, fill=1, stroke=0)

    # Genre anchor.
    c.setFillColor(Color(0.74, 0.73, 0.70))
    tracked(c, "PSYCHOTHRILLER", "NF-Reg", 10.2, 5.2, front_cx, 0.46 * inch)

    # Spine: title, genre and one red break mark.
    spine_cx = (spine_left + spine_right) / 2 * inch
    c.saveState()
    c.translate(spine_cx, H / 2)
    c.rotate(90)
    c.setFillColor(off)
    c.setFont("NF-Bold", 21.5)
    c.drawCentredString(0, -7, "NORMALFALL")
    c.setFillColor(Color(0.55, 0.55, 0.53))
    c.setFont("NF-Reg", 6.1)
    c.drawCentredString(0, -20, "PSYCHOTHRILLER")
    c.restoreState()
    c.setStrokeColor(red)
    c.setLineWidth(2.0)
    c.line(spine_cx, 0.35 * inch, spine_cx + 0.022 * inch, 0.62 * inch)

    # Back: quiet and barcode-safe, with only a faint system motif in the upper half.
    bx = (BLEED + 0.55) * inch
    by1 = 5.98 * inch
    by2 = 7.12 * inch
    c.setStrokeColor(Color(0.24, 0.24, 0.23))
    c.setLineWidth(0.8)
    for i in range(9):
        xx = bx + i * 0.23 * inch
        c.line(xx, by1, xx, by2)
    c.setStrokeColor(Color(0.52, 0.04, 0.02))
    c.setLineWidth(1.35)
    xx = bx + 4 * 0.23 * inch
    c.line(xx, by1, xx + 0.035 * inch, by2)

    c.showPage()
    c.save()

    print(
        f"pages={pages} paper={paper} spine={spine_w:.6f}in "
        f"cover={cover_w:.6f}x{cover_h:.3f}in"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pages", type=int, default=591)
    parser.add_argument("--paper", choices=["white", "cream"], default="white")
    parser.add_argument("--output", default="NORMALFALL_COVER.pdf")
    args = parser.parse_args()
    build(Path(args.output), args.pages, args.paper)


if __name__ == "__main__":
    main()
