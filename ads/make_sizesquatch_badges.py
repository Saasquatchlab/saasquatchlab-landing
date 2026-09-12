#!/usr/bin/env python3
"""Composite the official Google Play badge onto the SizeSquatch Meta ad creatives.

Run:  python3 ads/make_sizesquatch_badges.py

Reads the live creatives (ads/sizesquatch-ad-feed.png, ads/sizesquatch-ad-story.png —
untouched, still referenced by the Meta ad library) and writes new files
(ads/sizesquatch-ad-feed-v2.png, ads/sizesquatch-ad-story-v2.png) with the official,
unmodified Google Play badge (badge-google-play.png, repo root — same asset the site
uses) added at bottom-centre.

Neither original creative contains the official Apple badge artwork (both use a custom
white "Free on the App Store" pill, not Apple's badge), so there is no existing Apple
badge to match height against. Per the brief's fallback for that case, the Play badge is
placed bottom-centre inside the safe area instead — sized to fill whatever clean
background band exists below the last real content, with a small margin on each side, so
it reads as a deliberate second call-to-action rather than a squeezed-in afterthought.

Not a single pixel of the original artwork is touched: the script only pastes (alpha
composited) the untouched badge PNG into blank background it detects programmatically,
and Google's built-in transparent clear space around the badge is never cropped.
"""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BADGE_PATH = os.path.join(ROOT, "badge-google-play.png")

JOBS = [
    dict(src="ads/sizesquatch-ad-feed.png", dst="ads/sizesquatch-ad-feed-v2.png",
         top_gap=8, bottom_margin=6, max_h=60),
    dict(src="ads/sizesquatch-ad-story.png", dst="ads/sizesquatch-ad-story-v2.png",
         top_gap=16, bottom_margin=16, max_h=140),
]


def last_content_row(im):
    """Highest y (from the top) below which the image is just smooth background —
    found by comparing each row's pixels against that row's own left-edge background
    colour (the creatives are a vertical gradient, so this tolerates the gradient
    itself while still catching real content)."""
    w, h = im.size
    px = im.load()
    for y in range(h - 1, 0, -1):
        bg = px[2, y]
        for x in range(0, w, 2):
            p = px[x, y]
            if abs(p[0] - bg[0]) + abs(p[1] - bg[1]) + abs(p[2] - bg[2]) > 8:
                return y
    return 0


def composite(job):
    src_path = os.path.join(ROOT, job["src"])
    dst_path = os.path.join(ROOT, job["dst"])
    im = Image.open(src_path).convert("RGBA")
    w, h = im.size

    content_bottom = last_content_row(im.convert("RGB"))
    available = h - content_bottom
    badge_h = max(1, min(job["max_h"], available - job["top_gap"] - job["bottom_margin"]))

    badge = Image.open(BADGE_PATH).convert("RGBA")
    bw, bh = badge.size
    scale = badge_h / bh
    badge_w = round(bw * scale)
    badge_resized = badge.resize((badge_w, badge_h), Image.LANCZOS)

    x = (w - badge_w) // 2
    y = h - job["bottom_margin"] - badge_h

    out = im.copy()
    out.alpha_composite(badge_resized, (x, y))
    out.save(dst_path)
    print("  %-38s badge %dx%d at (%d, %d) — safe band was %dpx (content ends y=%d, canvas h=%d)"
          % (job["dst"], badge_w, badge_h, x, y, available, content_bottom, h))


def main():
    assert os.path.isfile(BADGE_PATH), "badge-google-play.png not found at repo root"
    print("Compositing Google Play badge onto SizeSquatch ad creatives (v2)")
    for job in JOBS:
        composite(job)


if __name__ == "__main__":
    main()
