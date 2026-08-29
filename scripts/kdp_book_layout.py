from __future__ import annotations

import argparse
from dataclasses import replace
from pathlib import Path

from docx import Document
from docx.shared import Cm

from polish_docx import PROFILES, polish_docx


# KDP paperback trim: 5.06 x 7.81 in = 12.85 x 19.84 cm, without bleed.
#
# The former custom trim was 12.0 x 18.7 cm with a live text area of
# 9.50 x 17.40 cm. The KDP adaptation deliberately preserves that live area
# instead of simply enlarging the text block. This keeps line length, density
# and the approved thriller typesetting visually stable while moving the trim
# to a KDP-supported size.
KDP_PROFILE = replace(
    PROFILES["buchvorschau"],
    subject="NORMALFALL – KDP Paperback 5.06 x 7.81 in",
    page_width_cm=12.85,
    page_height_cm=19.84,
    top_cm=1.22,
    bottom_cm=1.22,
    left_cm=1.78,   # inside margin with mirrorMargins enabled
    right_cm=1.57,  # outside margin
)

# Page numbers are printable content as well. Keep them safely farther from
# the trim edge than the previous 0.35 cm benchmark setting.
KDP_HEADER_FOOTER_DISTANCE_CM = 0.75


def apply_kdp_layout(path: Path) -> None:
    polish_docx(path, KDP_PROFILE)

    # polish_docx keeps the existing book conventions but its benchmark profile
    # sets header/footer distance to 0.35 cm. Override that final geometry here
    # for the KDP production file.
    doc = Document(path)
    for section in doc.sections:
        section.header_distance = Cm(KDP_HEADER_FOOTER_DISTANCE_CM)
        section.footer_distance = Cm(KDP_HEADER_FOOTER_DISTANCE_CM)
    doc.save(path)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Apply the canonical NORMALFALL KDP paperback layout."
    )
    parser.add_argument("document", type=Path)
    args = parser.parse_args()

    if not args.document.exists():
        raise SystemExit(f"File not found: {args.document}")

    apply_kdp_layout(args.document)
    print(
        "Applied KDP layout: 12.85 x 19.84 cm, "
        "margins 1.78/1.57/1.22/1.22 cm, footer 0.75 cm"
    )


if __name__ == "__main__":
    main()
