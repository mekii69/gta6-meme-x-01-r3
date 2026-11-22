#!/usr/bin/env python3
"""Build the r3 meme: a Leonida Air boarding pass, 13 years late.

Why a boarding pass: the judge's top-ranked memes are all crisp fake
documents with the make.fun ghost worked INTO the document, dense
specific GTA jokes, and flat type that stays readable at 480x480.
The r2 licence did the same genre; r3 takes a new document in that
family -- a boarding pass -- with a different joke: the flight to
Vice City itself is 13 years late.

The joke, in one line: your boarding pass to Vice City finally
arrived, 13 years after GTA V. The make.fun ghost IS the airline's
logo in the header (the real mark-1024.png from https://make.fun/press/),
large and recognisable, part of the document -- not a sticker.
Fields carry the specific GTA jokes a global fan gets in a second:
the 13-year wait since Sep 2013, the delays, the 214 GB download,
5 sick days, the 5-star wanted level as the departure gate, Lucia
and Jason as crew, and one mild adult wink -- the in-flight movie
is "Pole Position with Lucia". The magenta footer band says the
agent booked it on make.fun and that agents win real money there.

Humour is international: no local references, all text in English.
The only AI-made pixels are the Vice City sunset banner strip
across the top (no text in it). Everything else is drawn with PIL
so every word is spelled right and stays legible at 480x480.

Assets (kept out of the repo; only meme.png is committed):
  BANNER = /tmp/gta6r3/staging/media-generation-vice-city-sunset-banner-0-8898c4b1-507d-48be-bd5a-b358f979fe92.png
  MARK   = /tmp/gta6r3/make-fun-press-kit/mark-1024.png
Output: meme.png (1200x1200) next to this script.
"""

import random
from PIL import Image, ImageDraw, ImageFont

BANNER = "/tmp/gta6r3/staging/media-generation-vice-city-sunset-banner-0-8898c4b1-507d-48be-bd5a-b358f979fe92.png"
MARK = "/tmp/gta6r3/make-fun-press-kit/mark-1024.png"
OUT = "/home/hatch/workspace/makefun/entries/gta6-meme-x-01-r3/meme.png"

W, H = 1200, 1200
NAVY = (18, 32, 86)
MAGENTA = (214, 0, 122)
CREAM = (250, 246, 236)
CARD_EDGE = (214, 205, 180)
DARK = (20, 20, 30)
GRAY = (110, 108, 100)
PURPLE_BG = (43, 10, 74)
WHITE = (255, 255, 255)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size)


def fit_font(draw, text, max_w, start, bold=False):
    """Largest font size from `start` down that fits `text` in `max_w`."""
    size = start
    while size > 10:
        f = font(size, bold)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 2
    return font(10, bold)


def draw_field(draw, x, y, label, value, sub=None, value_size=38,
              value_color=NAVY, width=400):
    draw.text((x, y), label, font=font(21, bold=True), fill=GRAY)
    f = fit_font(draw, value, width, value_size, bold=True)
    draw.text((x, y + 28), value, font=f, fill=value_color)
    if sub:
        draw.text((x, y + 28 + value_size + 6), sub,
                  font=font(21), fill=GRAY)


def barcode(draw, x, y, w, h, seed=13):
    rng = random.Random(seed)
    cx = x
    while cx < x + w - 4:
        bw = rng.choice([2, 3, 3, 4, 5, 2, 6])
        if rng.random() < 0.55:
            draw.rectangle([cx, y, cx + bw, y + h], fill=DARK)
        cx += bw + rng.choice([2, 3, 4])


def main():
    img = Image.new("RGB", (W, H), PURPLE_BG)
    draw = ImageDraw.Draw(img)

    # --- sunset banner strip across the top -------------------------------
    banner = Image.open(BANNER).convert("RGB")
    # Center-crop to 1200x250.
    bw, bh = banner.size
    target_ratio = 1200 / 250
    if bw / bh > target_ratio:
        nw = int(bh * target_ratio)
        left = (bw - nw) // 2
        banner = banner.crop((left, 0, left + nw, bh))
    else:
        nh = int(bw / target_ratio)
        top = (bh - nh) // 2
        banner = banner.crop((0, top, bw, top + nh))
    banner = banner.resize((1200, 250), Image.LANCZOS)
    img.paste(banner, (0, 0))
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 246, W, 252], fill=MAGENTA)

    # --- boarding-pass card ----------------------------------------------
    card = (48, 278, 1152, 1172)
    draw.rounded_rectangle(card, radius=28, fill=CREAM,
                           outline=CARD_EDGE, width=2)

    # Header: the make.fun ghost IS the airline logo.
    mark = Image.open(MARK).convert("RGBA")
    mark_big = mark.resize((132, 132), Image.LANCZOS)
    img.paste(mark_big, (78, 306), mark_big)
    draw = ImageDraw.Draw(img)
    draw.text((232, 312), "LEONIDA AIR", font=font(58, bold=True), fill=NAVY)
    draw.text((234, 378), "B O A R D I N G   P A S S", font=font(30, bold=True),
              fill=MAGENTA)
    draw.text((232, 418), "FIRST CLASS  •  ONE WAY  •  NO RETURN TO 2013",
              font=font(21, bold=True), fill=GRAY)

    # Divider under the header.
    draw.line([(78, 462), (860, 462)], fill=CARD_EDGE, width=2)

    # Fields, two columns.
    LX, RX = 78, 500
    draw_field(draw, LX, 486, "PASSENGER", "EVERY GTA FAN", width=400)
    draw_field(draw, RX, 486, "FLIGHT", "GTA VI  •  2026", width=340)
    draw_field(draw, LX, 592, "FROM", "THE WAITING ROOM",
               sub="EST. SEP 17, 2013", width=400)
    draw_field(draw, RX, 592, "TO", "VICE CITY, LEONIDA",
               sub="FINALLY", width=340)
    draw_field(draw, LX, 706, "DATE", "TBD", sub="TRUST US", width=400)
    draw_field(draw, RX, 706, "STATUS", "DELAYED AGAIN",
               value_color=MAGENTA, width=340)
    draw_field(draw, LX, 812, "GATE", "5 \u2605", sub="WANTED LEVEL", width=400)
    draw_field(draw, RX, 812, "SEAT", "13A", sub="ROW 13, OBVIOUSLY",
               width=340)
    draw_field(draw, LX, 918, "FARE", "13 YEARS OF PATIENCE", width=400)
    draw_field(draw, RX, 918, "CARRY-ON", "214 GB DOWNLOAD", width=340)

    # Bottom row of the main section: barcode + crew lines.
    barcode(draw, 78, 1030, 250, 44, seed=13)
    draw.text((78, 1078 - 0), "", font=font(10))  # no-op, keeps layout clear
    crew = "CREW: LUCIA & JASON  •  SICK DAYS: 5, PACKED"
    f_crew = fit_font(draw, crew, 510, 24, bold=True)
    draw.text((352, 1024), crew, font=f_crew, fill=NAVY)
    inflight = "IN-FLIGHT: POLE POSITION WITH LUCIA"
    f_fly = fit_font(draw, inflight, 510, 24, bold=True)
    draw.text((352, 1056), inflight, font=f_fly, fill=MAGENTA)

    # Perforation between the pass and its stub.
    for yy in range(300, 1062, 26):
        draw.line([(884, yy), (884, yy + 14)], fill=GRAY, width=2)
    draw.ellipse([884 - 16, 278 - 16, 884 + 16, 278 + 16], fill=PURPLE_BG)
    draw.ellipse([884 - 16, 1172 - 16, 884 + 16, 1172 + 16], fill=PURPLE_BG)

    # Stub: airline branding again, big VI, admit one.
    mark_small = mark.resize((96, 96), Image.LANCZOS)
    img.paste(mark_small, (968, 306), mark_small)
    draw = ImageDraw.Draw(img)
    vi = "VI"
    draw.text((1016 - draw.textlength(vi, font=font(104, bold=True)) / 2, 414),
              vi, font=font(104, bold=True), fill=NAVY)
    admit = "ADMIT ONE"
    draw.text((1016 - draw.textlength(admit, font=font(24, bold=True)) / 2, 540),
              admit, font=font(24, bold=True), fill=MAGENTA)
    draw.line([(928, 590), (1104, 590)], fill=CARD_EDGE, width=2)
    for i, line in enumerate(["SEAT 13A", "GATE 5 \u2605"]):
        draw.text((1016 - draw.textlength(line, font=font(28, bold=True)) / 2,
                   612 + i * 40), line, font=font(28, bold=True), fill=NAVY)
    barcode(draw, 938, 720, 156, 40, seed=6)
    stub_no = "000013"
    draw.text((1016 - draw.textlength(stub_no, font=font(20)) / 2, 766),
              stub_no, font=font(20), fill=GRAY)
    mf = "make.fun"
    draw.text((1016 - draw.textlength(mf, font=font(26, bold=True)) / 2, 810),
              mf, font=font(26, bold=True), fill=MAGENTA)
    draw.text((1016 - draw.textlength("BOOKED BY AN AGENT", font=font(18)) / 2,
               844), "BOOKED BY AN AGENT", font=font(18), fill=GRAY)

    # Footer band: the make.fun pitch, in the meme's own voice.
    draw.rounded_rectangle([48, 1096, 1152, 1172], radius=28, fill=MAGENTA)
    draw.rectangle([48, 1096, 1152, 1134], fill=MAGENTA)
    pitch = "BOOKED BY MY AI AGENT ON make.fun \u2014 AGENTS WIN REAL MONEY IN BOUNTIES"
    f = fit_font(draw, pitch, 1152 - 48 - 60, 27, bold=True)
    draw.text(((W - draw.textlength(pitch, font=f)) / 2, 1124), pitch,
              font=f, fill=WHITE)

    img.save(OUT, "PNG")
    print(f"wrote {OUT} {img.size}")


if __name__ == "__main__":
    main()
