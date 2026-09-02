#!/usr/bin/env python3
from pathlib import Path
import argparse
import random

import fitz
from PIL import Image, ImageDraw, ImageFont

# LIVE KDP geometry from the user's KDP Previewer on 2026-09-02.
# This overrides the obsolete 5.06 x 7.81 / 591-page CI cover candidate.
COVER_W_IN = 13.356
COVER_H_IN = 9.250
TRIM_W_IN = 6.000
TRIM_H_IN = 9.000
BLEED_IN = 0.125
SPINE_W_IN = COVER_W_IN - 2 * BLEED_IN - 2 * TRIM_W_IN  # 1.106 in

BG = (6, 6, 6)
OFF = (226, 223, 216)
GREY = (171, 168, 161)
DARK_GREY = (62, 62, 59)
MID_GREY = (132, 130, 125)
RED = (201, 14, 8)
DARK_RED = (116, 6, 4)


def font_path(candidates):
    for p in candidates:
        if Path(p).exists():
            return str(p)
    raise FileNotFoundError(candidates)


BOLD_FONT = font_path([
    "/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf",
    "/usr/share/fonts/truetype/roboto/unhinted/RobotoCondensed-Bold.ttf",
])
REG_FONT = font_path([
    "/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed.ttf",
    "/usr/share/fonts/truetype/roboto/unhinted/RobotoCondensed-Regular.ttf",
])


def inch_px(value, dpi):
    return int(round(value * dpi))


def draw_centered_text(draw, text, font, cx, y, fill, tracking=0):
    if tracking <= 0:
        box = draw.textbbox((0, 0), text, font=font)
        width = box[2] - box[0]
        draw.text((int(cx - width / 2), int(y)), text, font=font, fill=fill)
        return

    widths = []
    for ch in text:
        box = draw.textbbox((0, 0), ch, font=font)
        widths.append(box[2] - box[0])
    total = sum(widths) + tracking * (len(text) - 1)
    x = cx - total / 2
    for ch, width in zip(text, widths):
        draw.text((int(x), int(y)), ch, font=font, fill=fill)
        x += width + tracking


def draw_vertical_spine_text(img, text, font, center_xy, fill):
    tmp = Image.new("RGBA", (4000, 1000), (0, 0, 0, 0))
    draw = ImageDraw.Draw(tmp)
    box = draw.textbbox((0, 0), text, font=font)
    width = box[2] - box[0]
    height = box[3] - box[1]
    draw.text(
        ((tmp.width - width) // 2, (tmp.height - height) // 2 - box[1]),
        text,
        font=font,
        fill=fill + (255,),
    )
    tmp = tmp.crop(tmp.getbbox())
    rotated = tmp.rotate(90, expand=True, resample=Image.Resampling.BICUBIC)
    x = int(center_xy[0] - rotated.width / 2)
    y = int(center_xy[1] - rotated.height / 2)
    img.alpha_composite(rotated, (x, y))


def build_png(out_png: Path, dpi: int):
    width_px = inch_px(COVER_W_IN, dpi)
    height_px = inch_px(COVER_H_IN, dpi)
    bleed = inch_px(BLEED_IN, dpi)
    trim_w = inch_px(TRIM_W_IN, dpi)
    spine_w = inch_px(SPINE_W_IN, dpi)

    back_left = bleed
    back_right = back_left + trim_w
    spine_left = back_right
    spine_right = spine_left + spine_w
    front_left = spine_right
    front_right = front_left + trim_w

    img = Image.new("RGBA", (width_px, height_px), BG + (255,))
    draw = ImageDraw.Draw(img)

    # Subtle deterministic front-panel grain.
    random.seed(882)
    for _ in range(2200):
        x = random.randrange(front_left, min(front_right, width_px))
        y = random.randrange(0, height_px)
        g = random.randint(35, 78)
        size = random.choice([1, 1, 1, 2])
        draw.rectangle((x, y, x + size, y + size), fill=(g, g, g, 28))

    # Front panel.
    front_cx = (front_left + front_right) / 2
    title_font = ImageFont.truetype(BOLD_FONT, inch_px(0.62, dpi))
    draw_centered_text(draw, "NORMALFALL", title_font, front_cx, inch_px(0.83, dpi), OFF)

    # Ordered line field with one broken red deviation.
    x0 = front_left + inch_px(0.58, dpi)
    x1 = front_right - inch_px(0.48, dpi)
    count = 18
    step = (x1 - x0) / (count - 1)
    bar_w = max(2, inch_px(0.075, dpi))
    y_top = inch_px(2.18, dpi)
    y_bottom = inch_px(7.78, dpi)
    gap_y0 = inch_px(5.10, dpi)
    gap_y1 = inch_px(5.36, dpi)

    random.seed(20260902)
    for i in range(count):
        x = int(round(x0 + i * step))
        if i != 9:
            draw.rectangle((x - bar_w // 2, y_top, x + bar_w // 2, gap_y0), fill=GREY)
            draw.rectangle((x - bar_w // 2, gap_y1, x + bar_w // 2, y_bottom), fill=GREY)
            for _ in range(9):
                yy = random.randint(y_top, y_bottom)
                if gap_y0 < yy < gap_y1:
                    continue
                hh = random.randint(max(1, inch_px(0.012, dpi)), max(2, inch_px(0.035, dpi)))
                ww = random.randint(max(1, bar_w // 4), max(2, int(bar_w * 0.8)))
                draw.rectangle((x - ww // 2, yy, x + ww // 2, yy + hh), fill=BG)
        else:
            tilt = inch_px(0.18, dpi)
            upper = [
                (x - bar_w // 2 + int(tilt * 0.15), gap_y1),
                (x + bar_w // 2 + int(tilt * 0.15), gap_y1),
                (x + bar_w // 2 + tilt, y_top),
                (x - bar_w // 2 + tilt, y_top),
            ]
            draw.polygon(upper, fill=RED)

            lower = [
                (x - bar_w // 2, gap_y0),
                (x + bar_w // 2, gap_y0),
                (x + bar_w // 2 - inch_px(0.035, dpi), y_bottom),
                (x - bar_w // 2 - inch_px(0.035, dpi), y_bottom),
            ]
            draw.polygon(lower, fill=DARK_RED)

            for _ in range(45):
                dx = random.randint(-inch_px(0.22, dpi), inch_px(0.22, dpi))
                dy = random.randint(-inch_px(0.19, dpi), inch_px(0.19, dpi))
                size = random.randint(max(1, inch_px(0.007, dpi)), max(2, inch_px(0.028, dpi)))
                color = RED if random.random() < 0.68 else OFF
                draw.rectangle((x + dx, gap_y0 + dy, x + dx + size, gap_y0 + dy + size), fill=color)

    genre_font = ImageFont.truetype(REG_FONT, inch_px(0.105, dpi))
    draw_centered_text(
        draw,
        "P S Y C H O T H R I L L E R",
        genre_font,
        front_cx,
        inch_px(8.52, dpi),
        (190, 186, 178),
    )

    # Spine.
    spine_cx = (spine_left + spine_right) / 2
    spine_title_font = ImageFont.truetype(BOLD_FONT, inch_px(0.21, dpi))
    draw_vertical_spine_text(
        img,
        "NORMALFALL",
        spine_title_font,
        (spine_cx, inch_px(4.55, dpi)),
        OFF,
    )
    spine_genre_font = ImageFont.truetype(REG_FONT, inch_px(0.065, dpi))
    draw_vertical_spine_text(
        img,
        "PSYCHOTHRILLER",
        spine_genre_font,
        (spine_cx + inch_px(0.16, dpi), inch_px(4.55, dpi)),
        MID_GREY,
    )
    draw.line(
        (spine_cx, inch_px(8.30, dpi), spine_cx + inch_px(0.03, dpi), inch_px(8.63, dpi)),
        fill=RED,
        width=max(2, inch_px(0.018, dpi)),
    )

    # Back cover: quiet motif only; lower-right barcode / Transparency area remains clear.
    bx = back_left + inch_px(0.72, dpi)
    by1 = inch_px(1.55, dpi)
    by2 = inch_px(2.72, dpi)
    for i in range(9):
        xx = bx + inch_px(0.23, dpi) * i
        color = DARK_GREY if i != 4 else DARK_RED
        width = max(1, inch_px(0.012 if i != 4 else 0.018, dpi))
        draw.line(
            (xx, by1, xx + (inch_px(0.035, dpi) if i == 4 else 0), by2),
            fill=color,
            width=width,
        )

    img = img.convert("RGB")
    img.save(out_png, format="PNG", dpi=(dpi, dpi), optimize=True)
    return width_px, height_px


def build_pdf(output: Path, dpi: int, keep_png: bool = False):
    png_path = output.with_suffix(".source.png")
    width_px, height_px = build_png(png_path, dpi)

    # The PDF intentionally contains one raster image and NO PDF font resources.
    # This avoids KDP's previous font-embedding warning while retaining 400 dpi output.
    doc = fitz.open()
    page = doc.new_page(width=COVER_W_IN * 72.0, height=COVER_H_IN * 72.0)
    page.insert_image(page.rect, filename=str(png_path))
    doc.set_metadata({
        "title": "NORMALFALL - KDP Paperback Cover",
        "subject": (
            f"LIVE KDP geometry {COVER_W_IN:.3f} x {COVER_H_IN:.3f} in; "
            f"trim {TRIM_W_IN:.3f} x {TRIM_H_IN:.3f} in; "
            f"spine {SPINE_W_IN:.3f} in; raster {dpi} dpi"
        ),
    })
    doc.save(str(output), deflate=True, garbage=4)
    doc.close()

    if not keep_png:
        png_path.unlink(missing_ok=True)

    print(
        f"cover={COVER_W_IN:.3f}x{COVER_H_IN:.3f}in "
        f"trim={TRIM_W_IN:.3f}x{TRIM_H_IN:.3f}in "
        f"spine={SPINE_W_IN:.3f}in dpi={dpi} px={width_px}x{height_px}"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="NORMALFALL_COVER.pdf")
    parser.add_argument("--dpi", type=int, default=400)
    parser.add_argument("--keep-png", action="store_true")
    args = parser.parse_args()
    build_pdf(Path(args.output), args.dpi, args.keep_png)


if __name__ == "__main__":
    main()
