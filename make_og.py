"""
Generate Open Graph (OG) image for ronnelestrada.com
Spec: 1200x630, text-overlay style using the Cebu rooftop photo
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

# --- CONFIG ---
SRC = "/home/claude/site/assets/ronnel-cebu.png"
OUT = "/home/claude/site/assets/og-image.png"
W, H = 1200, 630

# Brand colors
NAVY_DEEP = (15, 38, 64)      # #0F2640
GOLD = (196, 162, 101)         # #C4A265
CREAM = (245, 240, 235)        # #F5F0EB
GOLD_SOFT = (212, 185, 122)    # #D4B97A

# --- LOAD AND CROP BASE IMAGE ---
img = Image.open(SRC).convert("RGB")
src_w, src_h = img.size

# Target ratio 1200:630 = 1.905
target_ratio = W / H
src_ratio = src_w / src_h

# Crop to match target ratio — keep the subject & skyline, shift crop right
if src_ratio > target_ratio:
    # Source is wider than target — crop sides
    new_w = int(src_h * target_ratio)
    left = (src_w - new_w) // 2
    img = img.crop((left, 0, left + new_w, src_h))
else:
    # Source is taller than target — crop top/bottom
    new_h = int(src_w / target_ratio)
    # For a portrait photo, bias crop toward upper-middle (keep face & skyline)
    top = int((src_h - new_h) * 0.15)
    img = img.crop((0, top, src_w, top + new_h))

img = img.resize((W, H), Image.LANCZOS)

# --- DARKEN LEFT SIDE FOR TEXT LEGIBILITY ---
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw_overlay = ImageDraw.Draw(overlay)

# Gradient: dark on left fading to transparent on right
for x in range(W):
    # Dark from 0 to ~55%, fading out by 75%
    if x < int(W * 0.55):
        alpha = 200 - int((x / (W * 0.55)) * 60)  # 200 -> 140
    elif x < int(W * 0.75):
        alpha = 140 - int(((x - W * 0.55) / (W * 0.20)) * 140)
    else:
        alpha = 0
    draw_overlay.line([(x, 0), (x, H)], fill=(15, 38, 64, max(0, alpha)))

img_rgba = img.convert("RGBA")
img_rgba = Image.alpha_composite(img_rgba, overlay)

# --- ADD TEXT ---
draw = ImageDraw.Draw(img_rgba)

# Try to load Playfair Display or fallback to DejaVu
def load_font(size, bold=False, italic=False):
    candidates = []
    if bold:
        candidates += [
            "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf",
        ]
    elif italic:
        candidates += [
            "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf",
        ]
    else:
        candidates += [
            "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf",
        ]
    for c in candidates:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                continue
    return ImageFont.load_default()

def load_sans(size, bold=False):
    candidates = []
    if bold:
        candidates += [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        ]
    else:
        candidates += [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        ]
    for c in candidates:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                continue
    return ImageFont.load_default()

# Fonts
font_label = load_sans(22, bold=False)
font_name = load_font(96, bold=True)
font_tagline = load_font(32, italic=True)
font_url = load_sans(22, bold=False)

# Text layout
LEFT = 70
y = 170

# Small label above name
label = "ADVISOR · STORYTELLER · BUILDER"
draw.text((LEFT, y), label, font=font_label, fill=GOLD, spacing=4)
y += 45

# Name — two lines for better visual weight
draw.text((LEFT, y), "Ronnel", font=font_name, fill=CREAM)
y += 100
# "Estrada" in italic gold
draw.text((LEFT, y), "Estrada", font=font_name, fill=GOLD_SOFT)
y += 120

# Tagline
tagline = "Island-born. World-shaped. Purpose-driven."
draw.text((LEFT, y), tagline, font=font_tagline, fill=(245, 240, 235, 230))
y += 55

# URL pinned to bottom-left
url_y = H - 60
draw.text((LEFT, url_y), "ronnelestrada.com", font=font_url, fill=GOLD)

# Thin gold accent line under URL
draw.rectangle([(LEFT, url_y - 20), (LEFT + 60, url_y - 18)], fill=GOLD)

# --- SAVE ---
img_rgba.convert("RGB").save(OUT, "PNG", optimize=True)
print(f"Saved: {OUT}")
print(f"Size: {os.path.getsize(OUT) / 1024:.1f} KB")
print(f"Dimensions: {W}x{H}")
