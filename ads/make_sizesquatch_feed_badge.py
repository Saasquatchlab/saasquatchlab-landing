#!/usr/bin/env python3
"""Rebuild ads/sizesquatch-ad-feed-v2.png: the original feed creative with its "Free on the App
Store" pill and Google's official Play badge side by side at equal height. The original is never
modified. Run from the repo root: python3 ads/make_sizesquatch_feed_badge.py"""
from PIL import Image, ImageDraw
src = Image.open('ads/sizesquatch-ad-feed.png').convert('RGBA'); W, H = src.size; px = src.load()
white = lambda p: p[0] > 245 and p[1] > 245 and p[2] > 245
ys = [y for y in range(800, 1000) if white(px[320, y])]; y0, y1 = min(ys), max(ys)     # x=320 is outside the phone
xs = [x for x in range(W) if white(px[x, (y0 + y1) // 2])]; x0, x1 = min(xs), max(xs)
pw, ph = x1 - x0 + 1, y1 - y0 + 1
pill = src.crop((x0, y0, x1 + 1, y1 + 1))
mask = Image.new('L', (pw, ph), 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, pw - 1, ph - 1), radius=ph // 2, fill=255)
pill.putalpha(mask)
out = src.copy(); o = out.load()
for y in range(y0, y1 + 1):                      # erase the pill with the vertical gradient sampled at x=40
    c = px[40, y]
    for x in range(x0, x1 + 1): o[x, y] = c
badge = Image.open('badge-google-play.png').convert('RGBA'); badge = badge.crop(badge.getbbox())
bw = round(badge.width * ph / badge.height); badge = badge.resize((bw, ph), Image.LANCZOS)
gap = 28; sx = (W - (pw + gap + bw)) // 2
out.alpha_composite(pill, (sx, y0)); out.alpha_composite(badge, (sx + pw + gap, y0))
out.convert('RGB').save('ads/sizesquatch-ad-feed-v2.png'); print('wrote ads/sizesquatch-ad-feed-v2.png')
