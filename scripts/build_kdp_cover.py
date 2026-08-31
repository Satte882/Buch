#!/usr/bin/env python3
import argparse
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import black, white
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth

TRIM_W = 5.06
TRIM_H = 7.81
BLEED = 0.125
SPINE_FACTORS = {"white": 0.002252, "cream": 0.0025}


def font_path(candidates):
    for p in candidates:
        if Path(p).exists():
            return p
    raise FileNotFoundError(candidates)


def build(output: Path, pages: int, paper: str):
    spine_w = pages * SPINE_FACTORS[paper]
    cover_w = BLEED + TRIM_W + spine_w + TRIM_W + BLEED
    cover_h = BLEED + TRIM_H + BLEED
    W, H = cover_w * inch, cover_h * inch

    spine_left = (BLEED + TRIM_W) * inch
    spine_right = (BLEED + TRIM_W + spine_w) * inch
    front_left = spine_right
    front_right = W

    pdfmetrics.registerFont(TTFont("Title", font_path([
        "/usr/share/fonts/truetype/roboto/unhinted/RobotoCondensed-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf",
    ])))
    pdfmetrics.registerFont(TTFont("Sub", font_path([
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ])))

    c = canvas.Canvas(str(output), pagesize=(W, H), pageCompression=1,
                      initialFontName="Title", initialFontSize=10)
    c.setTitle("NORMALFALL - KDP Paperback Cover")
    c.setSubject(f"5.06 x 7.81 in; {pages} pages; B/W {paper} paper; {cover_w:.6f} x {cover_h:.3f} in")
    c.setFillColor(white)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(black)
    c.setStrokeColor(black)
    c.setLineWidth(1.25)

    base_y = H * 0.515

    def heart(cx, cy):
        pts = [(-0.18,0),(-0.12,0),(-0.085,0.035),(-0.055,-0.060),(0,0.300),
               (0.055,-0.185),(0.095,0.055),(0.135,0),(0.18,0)]
        return [(cx+x*inch, cy+y*inch) for x,y in pts]

    def poly(pts):
        p = c.beginPath()
        p.moveTo(*pts[0])
        for pt in pts[1:]:
            p.lineTo(*pt)
        c.drawPath(p, stroke=1, fill=0)

    # Back cover: full-width flatline, otherwise completely blank.
    c.line(0, base_y, spine_left, base_y)

    # Front cover: line spans the complete front panel width.
    front_cx = (front_left + front_right) / 2
    hp = heart(front_cx, base_y)
    c.line(front_left, base_y, hp[0][0], base_y)
    poly(hp)
    c.line(hp[-1][0], base_y, front_right, base_y)

    # Spine: exact heartbeat motif rotated 90 degrees; line spans full height.
    spine_cx = (spine_left + spine_right) / 2
    raw = heart(0,0)
    rot = [(spine_cx-y, base_y+x) for x,y in raw]
    c.line(spine_cx, 0, spine_cx, rot[0][1])
    poly(rot)
    c.line(spine_cx, rot[-1][1], spine_cx, H)

    def tracked(text, font, size, tracking, cx, y):
        c.setFont(font, size)
        widths = [stringWidth(ch, font, size) for ch in text]
        x = cx - (sum(widths) + tracking*(len(text)-1))/2
        for ch,w in zip(text,widths):
            c.drawString(x,y,ch)
            x += w + tracking

    title = "NORMALFALL"
    size, tracking = 50, 3.2
    max_w = (TRIM_W - 0.35) * inch
    while sum(stringWidth(ch,"Title",size) for ch in title) + tracking*(len(title)-1) > max_w:
        size -= 0.5
    tracked(title,"Title",size,tracking,front_cx,H*0.665)

    lines = [
        "EINE REGEL WIDERSTEHT ALLEM,",
        "AUSSER DEM BEWEIS,",
        "DASS ES OHNE SIE BESSER GEHT.",
    ]
    for i,line in enumerate(lines):
        tracked(line,"Sub",10.8,1.8,front_cx,H*0.382-i*18)

    c.showPage()
    c.save()
    print(f"pages={pages} paper={paper} spine={spine_w:.6f}in cover={cover_w:.6f}x{cover_h:.3f}in")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", type=int, required=True)
    ap.add_argument("--paper", choices=["white","cream"], default="white")
    ap.add_argument("--output", default="NORMALFALL_COVER.pdf")
    a = ap.parse_args()
    build(Path(a.output), a.pages, a.paper)


if __name__ == "__main__":
    main()
