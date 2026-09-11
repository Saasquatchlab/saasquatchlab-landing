#!/usr/bin/env python3
"""Generate the saasquatchlab.com static site.

Run:  python3 tools/build_site.py
Output: plain static .html written into the repo root. There is NO build step at
serve time — Vercel serves the committed HTML directly. This generator exists so
one art direction stays consistent across every page. Copy lives in content.py.

ART DIRECTION — "It's out there"
  The brand line is literal: a Pacific Northwest ridgeline at first light with
  the SaaSquatch mark standing in the treeline, half-occluded by the front rank
  of conifers. You have to look for it. That is the whole idea — privacy-first
  software that stays out of your way but is genuinely easy to use.

  Rules this file holds to, because the brief was explicitly to avoid generic
  SaaS/AI-template output:
    - Asymmetric editorial grid. Nothing is centred unless it earns it.
    - No pill badges, no gradient-text headlines, no boxed feature-card grids.
      Metadata is tracked micro-caps; features are hairline spec rows.
    - Extreme type-scale contrast: Fraunces display against small Inter.
    - Photographic surface: film grain, vignette, atmospheric haze — not flat CSS.
    - Motion is slow and atmospheric: masked word reveals, layered parallax.

NEVER emit into a `public/` directory — see CLAUDE.md (that takes the site down).
"""
import json
import re
from pathlib import Path
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import PRODUCTS, COMING, POLICIES, FOR_GOOD_SLUGS, FOR_GOOD_SHORT, FOR_GOOD_FULL  # noqa: E402
from legal import PRIVACY, SUPPORT, TERMS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ─────────────────────────────────────────────────────────────────────────────
# Ridgeline art — deterministic, so the skyline never shifts between builds
# ─────────────────────────────────────────────────────────────────────────────
W_START, W_END, FLOOR = -80, 1520, 660


def _cr(pts, floor=FLOOR):
    """Catmull-Rom through pts -> smooth cubic path, closed down to the floor."""
    n = len(pts)
    d = ["M %.1f %.1f" % pts[0]]
    for i in range(n - 1):
        p0, p1, p2 = pts[max(i - 1, 0)], pts[i], pts[i + 1]
        p3 = pts[min(i + 2, n - 1)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6.0, p1[1] + (p2[1] - p0[1]) / 6.0)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6.0, p2[1] - (p3[1] - p1[1]) / 6.0)
        d.append("C %.1f %.1f %.1f %.1f %.1f %.1f" % (c1 + c2 + p2))
    d.append("L %.1f %d L %.1f %d Z" % (pts[-1][0], floor, pts[0][0], floor))
    return " ".join(d)


def _ridge(seed, base, step, waves, jitter=0.0):
    rnd = random.Random(seed)
    pts, x = [], W_START
    while x <= W_END:
        y = base - sum(math.sin(x / wl + ph) * a for wl, a, ph in waves)
        pts.append((x, y - rnd.uniform(-jitter, jitter)))
        x += step
    return _cr(pts)


def _trees(seed, base, sway, hmin, hmax, wmin, wmax):
    rnd = random.Random(seed)
    d = ["M %d %d L %d %.1f" % (W_START, FLOOR, W_START, base)]
    x = W_START
    while x < W_END:
        w = rnd.uniform(wmin, wmax)
        h = rnd.uniform(hmin, hmax) * (1.45 if rnd.random() < 0.22 else 1.0)
        b = base + math.sin(x / 240.0) * sway
        d.append("L %.1f %.1f L %.1f %.1f L %.1f %.1f" % (x, b, x + w / 2, b - h, x + w, b))
        x += w
    d.append("L %d %d Z" % (W_END, FLOOR))
    return " ".join(d)


P = {
    "far": _ridge(11, 352, 90, [(520, 78, 0.4), (210, 26, 1.9), (95, 9, 3.1)], 5),
    "mid": _ridge(23, 432, 78, [(390, 52, 2.2), (165, 21, 0.6), (78, 7, 4.4)], 4),
    "near": _ridge(37, 494, 64, [(300, 30, 4.1), (128, 14, 2.7)], 3),
    "tb": _trees(53, 540, 8, 26, 58, 16, 30),
    "tf": _trees(71, 596, 11, 40, 104, 20, 40),
}

VB = 'viewBox="0 0 1440 660" preserveAspectRatio="xMidYMax slice" focusable="false"'


def scene(cryptid=True):
    """Layered ridgeline.

    Split into two SVGs so the sasquatch can sit *between* the back stand of
    conifers and the front rank — the front trees genuinely occlude it, which is
    the point of the brand line.
    """
    fig = ('\n      <img class="cryptid lyr" data-d="0.28" src="/mark-sasquatch.png" alt="" '
           'width="182" height="253" />') if cryptid else ""
    return """
    <div class="scene" aria-hidden="true">
      <div class="sun"></div>
      <div class="haze haze-a"></div>
      <svg class="scene-svg" __VB__>
        <path class="lyr" data-d="0.05" d="__FAR__" fill="var(--r4)" />
        <path class="lyr" data-d="0.10" d="__MID__" fill="var(--r3)" />
        <path class="lyr" data-d="0.16" d="__NEAR__" fill="var(--r2)" />
        <path class="lyr" data-d="0.23" d="__TB__" fill="var(--r1)" />
      </svg>__FIG__
      <svg class="scene-svg" __VB__>
        <path class="lyr" data-d="0.33" d="__TF__" fill="var(--r0)" />
      </svg>
      <div class="haze haze-b"></div>
      <div class="vignette"></div>
    </div>
""".replace("__VB__", VB).replace("__FAR__", P["far"]).replace("__MID__", P["mid"]).replace(
        "__NEAR__", P["near"]).replace("__TB__", P["tb"]).replace("__TF__", P["tf"]).replace(
        "__FIG__", fig)


GRAIN = ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='260' height='260'%3E"
         "%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' "
         "stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='260' height='260' filter='url(%23n)'/%3E%3C/svg%3E\")")

# ─────────────────────────────────────────────────────────────────────────────
# Design system
# ─────────────────────────────────────────────────────────────────────────────
CSS = """
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg: #050907;
      --bg-2: #070d09;
      --ink: #eaf1e7;
      --ink-2: #93ab98;
      --ink-3: #5d7565;
      --rule: #182619;
      --rule-lit: #24382b;

      --moss: #2d6a4f;
      --fern: #74c69d;
      --frond: #b7e4c7;

      /* atmospheric perspective: distant ridges keep light, near ones lose it */
      --r4: #18271f; --r3: #131f19; --r2: #0e1813; --r1: #0a120e; --r0: #050907;

      --key: __ACCENT__;
      --gut: clamp(1.25rem, 4vw, 4rem);
      --ease: cubic-bezier(0.16, 1, 0.3, 1);
    }

    html { -webkit-text-size-adjust: 100%; }
    @media (prefers-reduced-motion: no-preference) { html { scroll-behavior: smooth; } }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      background: var(--bg); color: var(--ink);
      line-height: 1.6; -webkit-font-smoothing: antialiased;
      overflow-x: hidden; position: relative;
    }

    /* Film grain — keeps the surface photographic rather than flat CSS.
       Deliberately NO mix-blend-mode: a blended fixed layer makes WebKit drop
       the whole page to black on scroll. Plain low opacity reads the same on a
       ground this dark. */
    body::after {
      content: ''; position: fixed; inset: 0; z-index: 200; pointer-events: none;
      background-image: __GRAIN__; background-repeat: repeat; opacity: 0.022;
    }

    a { color: inherit; text-decoration: none; }
    img { max-width: 100%; display: block; }
    :focus-visible { outline: 2px solid var(--fern); outline-offset: 4px; border-radius: 3px; }
    .skip { position: absolute; left: -9999px; top: 0; z-index: 300; background: var(--moss); color: #fff; padding: 0.7rem 1.1rem; }
    .skip:focus { left: 0; }

    .g { display: grid; grid-template-columns: repeat(12, 1fr); column-gap: clamp(0.75rem, 1.6vw, 1.6rem); max-width: 1360px; margin: 0 auto; padding: 0 var(--gut); }

    /* ── micro type ────────────────────────────────────────────────────── */
    .marque { display: flex; align-items: center; gap: 0.85rem; font-size: 0.66rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.24em; color: var(--ink-3); }
    .marque::before { content: ''; width: clamp(20px, 4vw, 56px); height: 1px; background: var(--rule-lit); flex-shrink: 0; }
    .marque.key { color: var(--key); }
    .marque.key::before { background: color-mix(in srgb, var(--key) 55%, transparent); }
    .fig { font-size: 0.63rem; text-transform: uppercase; letter-spacing: 0.2em; color: var(--ink-3); font-weight: 500; }
    .hero-icon { width: 62px; height: 62px; border-radius: 15px; object-fit: cover; margin-bottom: 1.5rem; }
    .hero-icon.em { display: grid; place-items: center; font-size: 1.7rem; background: color-mix(in srgb, var(--key) 16%, transparent); }

    /* ── display type ──────────────────────────────────────────────────── */
    h1, h2, h3, .disp { font-family: 'Fraunces', 'Iowan Old Style', Georgia, serif; font-weight: 600; letter-spacing: -0.028em; font-variation-settings: 'SOFT' 0, 'WONK' 1; }
    .mega { font-size: clamp(3.4rem, 13vw, 10.5rem); line-height: 0.9; }
    .mega em { font-style: italic; color: var(--frond); letter-spacing: -0.036em; }
    .mega .ind { display: block; padding-left: clamp(0px, 7vw, 5.5rem); }

    /* word-level masked reveal */
    .w { display: inline-block; overflow: hidden; vertical-align: bottom; padding-bottom: 0.08em; }
    .w > span { display: inline-block; transform: translateY(110%); transition: transform 1.1s var(--ease); }
    .lit .w > span { transform: none; }

    .lede { font-size: clamp(1rem, 1.35vw, 1.18rem); color: var(--ink-2); line-height: 1.74; max-width: 44ch; }
    .lede strong { color: var(--ink); font-weight: 600; }

    /* ── links ─────────────────────────────────────────────────────────── */
    .lnk { display: inline-flex; align-items: center; gap: 0.7rem; font-size: 0.72rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.18em; color: var(--ink); padding-bottom: 0.55rem; position: relative; }
    .lnk::after { content: ''; position: absolute; left: 0; bottom: 0; height: 1px; width: 100%; background: var(--rule-lit); }
    .lnk::before { content: ''; position: absolute; left: 0; bottom: 0; height: 1px; width: 100%; background: var(--key); transform: scaleX(0); transform-origin: left; transition: transform 0.6s var(--ease); z-index: 1; }
    .lnk:hover::before { transform: scaleX(1); }
    .lnk svg { transition: transform 0.5s var(--ease); }
    .lnk:hover svg { transform: translateX(6px); }
    .lnk.key { color: var(--key); }
    .lnk.off { color: var(--ink-3); pointer-events: none; }
    .lnk.off::before { display: none; }
    .acts { display: flex; flex-wrap: wrap; gap: clamp(1.4rem, 4vw, 3rem); align-items: center; }
    .badge-app-store { display: inline-block; line-height: 0; transition: opacity 0.4s var(--ease), transform 0.5s var(--ease); }
    .badge-app-store img { display: block; height: 50px; width: auto; }
    .badge-app-store:hover { opacity: 0.85; transform: translateY(-1px); }

    /* ── scene ─────────────────────────────────────────────────────────── */
    .scene { position: absolute; inset: 0; overflow: hidden; pointer-events: none; z-index: 0; }
    .scene-svg { position: absolute; inset: 0; width: 100%; height: 100%; }
    .lyr { will-change: transform; }
    .sun { position: absolute; left: 64%; top: -14%; width: 80vw; height: 80vw; max-height: 940px; transform: translateX(-50%); background: radial-gradient(circle at 50% 50%, color-mix(in srgb, var(--key) 21%, transparent) 0%, transparent 57%), radial-gradient(circle at 50% 50%, rgba(192, 123, 58, 0.14) 0%, transparent 45%); }
    .haze { position: absolute; left: -30%; width: 160%; height: 300px; background: radial-gradient(ellipse 48% 50% at 50% 50%, rgba(150, 176, 170, 0.17) 0%, transparent 70%); }
    .haze-a { bottom: 27%; animation: drift 78s ease-in-out infinite; }
    .haze-b { bottom: 5%; height: 220px; opacity: 0.6; animation: drift 112s ease-in-out infinite reverse; }
    @keyframes drift { 0%, 100% { transform: translateX(-8%) } 50% { transform: translateX(8%) } }
    .vignette { position: absolute; inset: 0; background: radial-gradient(ellipse 82% 72% at 50% 44%, transparent 38%, rgba(5, 9, 7, 0.58) 100%), linear-gradient(to bottom, rgba(5, 9, 7, 0.42) 0%, transparent 24%, transparent 60%, var(--bg) 99%); }

    /* the sasquatch, standing in the trees — faint on purpose */
    .cryptid {
      position: absolute; left: 71%; bottom: 4%; width: auto;
      height: clamp(92px, 15vw, 210px);
      opacity: 0.085; filter: blur(0.4px);
      transition: opacity 1.6s var(--ease);
    }
    .hero:hover .cryptid { opacity: 0.16; }

    /* ── hero ──────────────────────────────────────────────────────────── */
    .hero { position: relative; isolation: isolate; padding: clamp(4.5rem, 12vh, 8rem) 0 clamp(3.5rem, 8vh, 6rem); }
    .hero > .g { position: relative; z-index: 2; }
    .hero-mark { grid-column: 1 / -1; margin-bottom: clamp(2.25rem, 7vh, 4.5rem); }
    .hero-type { grid-column: 1 / -1; }
    .hero-foot { grid-column: 1 / -1; margin-top: clamp(2.25rem, 5vh, 3.5rem); display: grid; grid-template-columns: repeat(12, 1fr); column-gap: clamp(0.75rem, 1.6vw, 1.6rem); row-gap: 2rem; align-items: end; border-top: 1px solid var(--rule); padding-top: clamp(1.75rem, 3.5vh, 2.5rem); }
    .hero-acts { grid-column: 1 / span 5; }
    .hero-lede { grid-column: 7 / span 6; }
    .hero-cap { grid-column: 1 / -1; margin-top: 1.25rem; }

    /* ── sections ──────────────────────────────────────────────────────── */
    section { position: relative; padding: clamp(4.5rem, 11vh, 8.5rem) 0; }
    .ruled { border-top: 1px solid var(--rule); }
    .head { grid-column: 1 / span 8; margin-bottom: clamp(2.75rem, 6vh, 4.5rem); }
    .head .t { font-size: clamp(1.9rem, 5vw, 3.7rem); line-height: 1.04; margin: 1.15rem 0 1.15rem; }
    .head .t em { font-style: italic; color: var(--frond); }
    .head .lede { max-width: 52ch; }

    /* ── product index ─────────────────────────────────────────────────── */
    .idx { grid-column: 1 / -1; }
    .item { display: grid; grid-template-columns: 4.5rem minmax(0, 1fr) minmax(0, 1.05fr) auto; column-gap: clamp(1rem, 2.5vw, 2.5rem); align-items: start; padding: clamp(1.75rem, 3.5vh, 2.6rem) 0; border-top: 1px solid var(--rule); position: relative; }
    .item:last-child { border-bottom: 1px solid var(--rule); }
    .item::before { content: ''; position: absolute; left: calc(var(--gut) * -0.5); right: calc(var(--gut) * -0.5); top: 0; bottom: 0; z-index: -1; opacity: 0; background: linear-gradient(96deg, color-mix(in srgb, var(--rc) 10%, transparent), transparent 55%); transition: opacity 0.5s var(--ease); }
    a.item:hover::before { opacity: 1; }
    .item-n { font-family: 'Fraunces', Georgia, serif; font-size: 0.78rem; color: var(--ink-3); letter-spacing: 0.14em; padding-top: 0.6rem; }
    .item-id { display: flex; align-items: center; gap: 0.9rem; margin-bottom: 0.75rem; flex-wrap: wrap; }
    .item-logo { width: 40px; height: 40px; border-radius: 10px; object-fit: cover; flex-shrink: 0; }
    .item-logo.em { display: grid; place-items: center; font-size: 1.15rem; background: color-mix(in srgb, var(--rc) 16%, transparent); }
    .item-name { font-family: 'Fraunces', Georgia, serif; font-size: clamp(1.35rem, 2.4vw, 2rem); font-weight: 600; letter-spacing: -0.024em; line-height: 1.08; }
    .item-cat { font-size: 0.63rem; text-transform: uppercase; letter-spacing: 0.2em; color: var(--ink-3); margin-top: 0.15rem; }
    .item-desc { color: var(--ink-2); font-size: 0.92rem; line-height: 1.74; }
    .item-meta { list-style: none; margin-top: 0.95rem; display: flex; flex-wrap: wrap; gap: 0.3rem 1.15rem; }
    .item-meta li { font-size: 0.75rem; color: var(--ink-3); display: flex; align-items: center; gap: 0.45rem; }
    .item-meta li::before { content: ''; width: 3px; height: 3px; border-radius: 50%; background: var(--rc); flex-shrink: 0; }
    .item-go { padding-top: 0.6rem; color: var(--rc); display: flex; align-items: center; gap: 0.55rem; font-size: 0.68rem; text-transform: uppercase; letter-spacing: 0.18em; font-weight: 600; white-space: nowrap; }
    .item-go svg { transition: transform 0.5s var(--ease); }
    a.item:hover .item-go svg { transform: translateX(6px); }
    .item-go.off { color: var(--ink-3); }

    .st { font-size: 0.6rem; text-transform: uppercase; letter-spacing: 0.16em; font-weight: 600; padding: 0.24rem 0.55rem; border: 1px solid; border-radius: 2px; white-space: nowrap; }
    .st.live { color: var(--frond); border-color: rgba(183, 228, 199, 0.34); }
    .st.review { color: #e6a87c; border-color: rgba(230, 168, 124, 0.34); }
    .st.soon { color: #9dbccb; border-color: rgba(157, 188, 203, 0.32); }

    /* ── spec rows (deliberately not feature cards) ────────────────────── */
    .specs { grid-column: 1 / -1; border-top: 1px solid var(--rule); }
    .spec { display: grid; grid-template-columns: 4.5rem minmax(0, 4fr) minmax(0, 6fr); column-gap: clamp(1rem, 2.5vw, 2.5rem); padding: clamp(1.4rem, 2.8vh, 2rem) 0; border-bottom: 1px solid var(--rule); }
    .spec-n { font-family: 'Fraunces', Georgia, serif; font-size: 0.76rem; color: var(--ink-3); letter-spacing: 0.14em; padding-top: 0.35rem; }
    .spec-t { font-family: 'Fraunces', Georgia, serif; font-size: 1.15rem; font-weight: 600; letter-spacing: -0.02em; line-height: 1.3; }
    .spec-d { color: var(--ink-2); font-size: 0.91rem; line-height: 1.76; }

    /* ── promise band ──────────────────────────────────────────────────── */
    .band { grid-column: 1 / -1; display: grid; grid-template-columns: minmax(0, 7fr) minmax(0, 4fr); gap: clamp(1.5rem, 4vw, 3.5rem); align-items: center; padding: clamp(1.75rem, 4vh, 2.75rem) 0; border-top: 1px solid var(--key); border-bottom: 1px solid var(--rule); background: linear-gradient(100deg, color-mix(in srgb, var(--key) 8%, transparent), transparent 70%); }
    .band p { color: var(--ink-2); font-size: 1.01rem; line-height: 1.74; padding-left: clamp(0px, 2vw, 1.5rem); }
    .band strong { color: var(--ink); font-weight: 600; }
    .band .side { justify-self: end; padding-right: clamp(0px, 2vw, 1.5rem); }

    /* ── ledger ────────────────────────────────────────────────────────── */
    .ledger { grid-column: 1 / -1; display: grid; grid-template-columns: repeat(4, 1fr); border-top: 1px solid var(--rule); }
    .led { padding: clamp(1.5rem, 3.5vh, 2.4rem) clamp(0.75rem, 2vw, 1.75rem) clamp(1.5rem, 3.5vh, 2.4rem) 0; border-right: 1px solid var(--rule); }
    .led:last-child { border-right: 0; }
    .led-n { font-family: 'Fraunces', Georgia, serif; font-size: clamp(2.2rem, 4.5vw, 3.4rem); font-weight: 600; line-height: 1; color: var(--frond); letter-spacing: -0.03em; }
    .led-l { font-size: 0.71rem; color: var(--ink-3); margin-top: 0.7rem; line-height: 1.55; text-transform: uppercase; letter-spacing: 0.11em; }

    /* ── prose ─────────────────────────────────────────────────────────── */
    .prose { grid-column: 2 / span 8; }
    .prose.wide { grid-column: 1 / span 9; }
    .prose h2 { font-size: 1.42rem; margin: 2.9rem 0 0.8rem; scroll-margin-top: 5rem; }
    .prose h2:first-child { margin-top: 0; }
    .prose h3 { font-family: 'Inter', sans-serif; font-size: 0.97rem; font-weight: 700; color: var(--fern); margin: 1.9rem 0 0.45rem; letter-spacing: 0; scroll-margin-top: 5rem; }
    .prose p, .prose li { color: var(--ink-2); font-size: 0.96rem; line-height: 1.8; }
    .prose p { margin-bottom: 0.95rem; }
    .prose ul { margin: 0 0 1.15rem 1.15rem; }
    .prose li { margin-bottom: 0.42rem; }
    .prose strong { color: var(--ink); font-weight: 600; }
    .prose a { color: var(--fern); text-decoration: underline; text-underline-offset: 3px; text-decoration-color: rgba(116, 198, 157, 0.35); }
    .prose a:hover { text-decoration-color: var(--fern); }
    .prose .lead { font-size: 1.05rem; color: var(--ink); border-left: 2px solid var(--key); padding-left: 1.3rem; margin-bottom: 2.1rem; }

    .tbl-wrap { overflow-x: auto; margin: 1.4rem 0 1.7rem; }
    table { width: 100%; border-collapse: collapse; font-size: 0.88rem; min-width: 460px; }
    th, td { text-align: left; padding: 0.68rem 0.8rem 0.68rem 0; border-bottom: 1px solid var(--rule); vertical-align: top; }
    th { color: var(--ink); font-weight: 600; font-size: 0.64rem; text-transform: uppercase; letter-spacing: 0.15em; }
    td { color: var(--ink-2); }
    .pill { display: inline-block; font-size: 0.64rem; font-weight: 600; padding: 0.1rem 0.5rem; border: 1px solid; border-radius: 2px; text-transform: uppercase; letter-spacing: 0.1em; white-space: nowrap; }
    .pill.none { color: var(--frond); border-color: rgba(183, 228, 199, 0.34); }
    .pill.some { color: #e6a87c; border-color: rgba(230, 168, 124, 0.34); }

    /* ── closer ────────────────────────────────────────────────────────── */
    .closer { position: relative; isolation: isolate; overflow: hidden; padding: clamp(5rem, 13vh, 9rem) 0 clamp(4rem, 10vh, 7rem); }
    .closer-in { grid-column: 1 / span 9; position: relative; z-index: 2; }
    .closer h2 { font-size: clamp(2.1rem, 6.4vw, 4.6rem); line-height: 1.0; margin-bottom: 1.3rem; }
    .closer h2 em { font-style: italic; color: var(--frond); }
    .closer .lede { margin-bottom: 2.4rem; }

    /* ── nav ───────────────────────────────────────────────────────────── */
    .nav { position: sticky; top: 0; z-index: 90; display: flex; align-items: center; justify-content: space-between; padding: 0.95rem var(--gut); border-bottom: 1px solid transparent; transition: background 0.4s var(--ease), border-color 0.4s var(--ease); }
    .nav.stuck { background: rgba(5, 9, 7, 0.86); backdrop-filter: blur(16px) saturate(1.3); border-bottom-color: var(--rule); }
    .nav-left { display: flex; align-items: center; gap: clamp(1rem, 2.6vw, 2rem); min-width: 0; }
    .nav-right { display: flex; align-items: center; gap: 1.4rem; }
    .brand { display: flex; align-items: center; gap: 0.7rem; font-size: 0.76rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.17em; }
    .brand-mark { width: 30px; height: 30px; border-radius: 8px; flex-shrink: 0; background: linear-gradient(145deg, #1e4d38, var(--moss) 55%, #40916c); display: grid; place-items: center; overflow: hidden; }
    .brand-mark img { width: 74%; height: auto; }
    .nav-list { display: flex; align-items: center; gap: clamp(1rem, 2.4vw, 2.1rem); list-style: none; }
    .nav-list > li { position: relative; }
    .nav-list > li > a, .nav-back { font-size: 0.66rem; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 500; color: var(--ink-3); transition: color 0.25s; }
    .nav-list > li > a:hover, .nav-back:hover { color: var(--ink); }
    .nav-back { display: inline-flex; align-items: center; gap: 0.55rem; }

    /* ── nav dropdowns ─────────────────────────────────────────────────── */
    .nav-trigger { display: inline-flex; align-items: center; gap: 0.4rem; }
    .nav-trigger::after { content: ''; width: 5px; height: 5px; border-right: 1px solid currentColor; border-bottom: 1px solid currentColor; transform: rotate(45deg) translateY(-1px); opacity: 0.7; transition: transform 0.25s var(--ease); }
    .nav-drop:hover .nav-trigger::after, .nav-drop.open .nav-trigger::after { transform: rotate(225deg) translateY(1px); }
    .nav-menu { position: absolute; top: 100%; left: 0; margin-top: 0.9rem; min-width: 232px; list-style: none; padding: 0.5rem 0; background: rgba(5, 9, 7, 0.96); backdrop-filter: blur(16px) saturate(1.3); border: 1px solid var(--rule); border-radius: 3px; opacity: 0; visibility: hidden; transform: translateY(-6px); transition: opacity 0.22s var(--ease), transform 0.22s var(--ease), visibility 0.22s; z-index: 95; }
    .nav-drop:hover .nav-menu, .nav-drop:focus-within .nav-menu, .nav-drop.open .nav-menu { opacity: 1; visibility: visible; transform: none; }
    .nav-menu a { display: block; padding: 0.55rem 1.1rem; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.13em; font-weight: 500; color: var(--ink-2); white-space: nowrap; transition: color 0.2s, background 0.2s; }
    .nav-menu a:hover, .nav-menu a:focus-visible { color: var(--ink); background: rgba(255, 255, 255, 0.04); }

    /* ── mobile nav toggle + panel ────────────────────────────────────── */
    .nav-toggle { display: none; font: inherit; font-size: 0.66rem; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 500; color: var(--ink); background: transparent; border: 1px solid var(--rule-lit); border-radius: 3px; padding: 0.5rem 0.9rem; cursor: pointer; }
    .nav-toggle:hover { border-color: var(--ink-3); }
    .nav-mobile { display: none; background: var(--bg-2); border-bottom: 1px solid var(--rule); padding: 0.5rem var(--gut) 1.5rem; }
    .nav-mobile:not([hidden]) { display: block; }
    .nav-mobile > ul { list-style: none; }
    .nav-mobile > ul > li { border-top: 1px solid var(--rule); }
    .nav-mobile > ul > li:first-child { border-top: 0; }
    .nav-mobile > ul > li > a, .nav-mobile-head { display: block; padding: 0.9rem 0; font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.14em; font-weight: 600; color: var(--ink); }
    .nav-mobile-group ul { list-style: none; padding-bottom: 0.6rem; }
    .nav-mobile-group ul a { display: block; padding: 0.55rem 0 0.55rem 1rem; font-size: 0.68rem; text-transform: uppercase; letter-spacing: 0.12em; color: var(--ink-2); }
    .nav-mobile a:hover { color: var(--frond); }

    /* ── footer ────────────────────────────────────────────────────────── */
    .foot { border-top: 1px solid var(--rule); padding: clamp(3rem, 7vh, 4.5rem) 0 2rem; background: var(--bg-2); }
    .foot-g { grid-column: 1 / -1; display: grid; grid-template-columns: 1.6fr repeat(3, 1fr); gap: clamp(1.75rem, 4vw, 3rem); }
    .foot h4 { font-family: 'Inter', sans-serif; font-size: 0.61rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.19em; color: var(--ink-3); margin-bottom: 1.15rem; }
    .foot ul { list-style: none; display: flex; flex-direction: column; gap: 0.6rem; }
    .foot a { font-size: 0.83rem; color: var(--ink-2); transition: color 0.25s; }
    .foot a:hover { color: var(--ink); }
    .foot-blurb { font-size: 0.83rem; color: var(--ink-2); margin-top: 1rem; max-width: 28ch; line-height: 1.7; }
    .foot-base { grid-column: 1 / -1; margin-top: clamp(2.25rem, 5vh, 3rem); padding-top: 1.5rem; border-top: 1px solid var(--rule); display: flex; justify-content: space-between; flex-wrap: wrap; gap: 0.75rem; }

    /* ── reveal ────────────────────────────────────────────────────────── */
    .r { opacity: 0; transform: translateY(26px); transition: opacity 0.9s var(--ease), transform 0.9s var(--ease); }
    .r.lit { opacity: 1; transform: none; }

    /* ── responsive ────────────────────────────────────────────────────── */
    @media (max-width: 1000px) {
      .hero-lede { grid-column: 6 / -1; }
      .hero-acts { grid-column: 1 / span 5; }
      .head { grid-column: 1 / span 10; }
      .prose, .prose.wide { grid-column: 1 / -1; }
      .closer-in { grid-column: 1 / -1; }
      .band { grid-template-columns: 1fr; }
      .band .side { justify-self: start; padding-left: clamp(0px, 2vw, 1.5rem); }
      .foot-g { grid-template-columns: 1fr 1fr; }
      .item { grid-template-columns: 3.5rem minmax(0, 1fr) auto; }
      .item-desc { grid-column: 2 / -1; margin-top: 0.5rem; }
    }
    @media (max-width: 760px) {
      .nav-list { display: none; }
      .nav-toggle { display: inline-flex; }
      .item { grid-template-columns: 2.5rem 1fr; row-gap: 0.6rem; }
      .item-n { padding-top: 0.2rem; }
      .item-desc, .item-go { grid-column: 2; }
      .item-go { padding-top: 0.4rem; }
      .spec { grid-template-columns: 2.5rem 1fr; row-gap: 0.5rem; }
      .spec-d { grid-column: 2; }
      .hero-foot { row-gap: 1.75rem; }
      .hero-lede, .hero-acts { grid-column: 1 / -1; }
      .ledger { grid-template-columns: 1fr 1fr; }
      .led { border-bottom: 1px solid var(--rule); }
      .led:nth-child(2) { border-right: 0; }
      .foot-g { grid-template-columns: 1fr; }
      .cryptid { left: 66%; height: clamp(80px, 20vw, 130px); opacity: 0.11; }
    }

    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after { animation-duration: 0.001ms !important; animation-iteration-count: 1 !important; transition-duration: 0.001ms !important; }
      .r { opacity: 1; transform: none; }
      .w > span { transform: none; }
    }
"""

JS = """
  (function () {
    var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
    var nav = document.querySelector('.nav');
    function stick() { nav.classList.toggle('stuck', scrollY > 20); }
    stick(); addEventListener('scroll', stick, { passive: true });

    var hero = document.querySelector('.hero-type');
    if (hero) requestAnimationFrame(function () { setTimeout(function () { hero.classList.add('lit'); }, 80); });

    var items = document.querySelectorAll('.r');
    if (reduce || !('IntersectionObserver' in window)) {
      items.forEach(function (el) { el.classList.add('lit'); });
    } else {
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('lit'); io.unobserve(e.target); } });
      }, { rootMargin: '0px 0px -10% 0px', threshold: 0.06 });
      items.forEach(function (el, i) { el.style.transitionDelay = Math.min(i % 5, 4) * 70 + 'ms'; io.observe(el); });
    }

    // Atmospheric parallax — near ranks travel further than distant ones
    var lyrs = document.querySelectorAll('.lyr');
    if (!reduce && lyrs.length) {
      var tick = false;
      function paint() {
        var y = scrollY;
        for (var i = 0; i < lyrs.length; i++) {
          lyrs[i].style.transform = 'translate3d(0,' + (y * (+lyrs[i].dataset.d || 0)).toFixed(2) + 'px,0)';
        }
        tick = false;
      }
      addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(paint); } }, { passive: true });
      paint();
    }

    // Nav dropdowns — CSS hover/:focus-within already reveals the menu;
    // this layers in click-to-toggle (so the trigger stays a real link),
    // Escape, and outside-click for keyboard and touch users.
    var drops = document.querySelectorAll('.nav-drop');
    function closeDrop(li) {
      li.classList.remove('open');
      var t = li.querySelector('.nav-trigger');
      if (t) t.setAttribute('aria-expanded', 'false');
    }
    function closeAllDrops() { drops.forEach(closeDrop); }
    drops.forEach(function (li) {
      var trigger = li.querySelector('.nav-trigger');
      if (!trigger) return;
      li.addEventListener('mouseenter', function () { trigger.setAttribute('aria-expanded', 'true'); });
      li.addEventListener('mouseleave', function () { if (!li.classList.contains('open')) trigger.setAttribute('aria-expanded', 'false'); });
      li.addEventListener('focusin', function () { trigger.setAttribute('aria-expanded', 'true'); });
      li.addEventListener('focusout', function (e) {
        if (!li.contains(e.relatedTarget)) closeDrop(li);
      });
      trigger.addEventListener('click', function (e) {
        if (!li.classList.contains('open')) {
          e.preventDefault();
          closeAllDrops();
          li.classList.add('open');
          trigger.setAttribute('aria-expanded', 'true');
        }
      });
    });
    document.addEventListener('click', function (e) {
      drops.forEach(function (li) { if (!li.contains(e.target)) closeDrop(li); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key !== 'Escape') return;
      var open = document.querySelector('.nav-drop.open');
      closeAllDrops();
      if (open) { var t = open.querySelector('.nav-trigger'); if (t) t.focus(); }
      if (navMobile && !navMobile.hidden) { navMobile.hidden = true; if (navToggle) { navToggle.setAttribute('aria-expanded', 'false'); navToggle.focus(); } }
    });

    // Mobile "Menu" toggle — stacked list below the 760px breakpoint,
    // where the dropdown nav has nowhere to go.
    var navToggle = document.querySelector('.nav-toggle');
    var navMobile = document.getElementById('nav-mobile');
    if (navToggle && navMobile) {
      navToggle.addEventListener('click', function () {
        var opening = navMobile.hidden;
        navMobile.hidden = !opening;
        navToggle.setAttribute('aria-expanded', String(opening));
      });
    }
  })();
"""

ARR = ('<svg width="20" height="9" viewBox="0 0 20 9" fill="none" stroke="currentColor" stroke-width="1.4" '
       'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M0 4.5h18M14.5 1 18 4.5 14.5 8"/></svg>')
ARR_B = ('<svg width="20" height="9" viewBox="0 0 20 9" fill="none" stroke="currentColor" stroke-width="1.4" '
         'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 4.5H2M5.5 1 2 4.5 5.5 8"/></svg>')
MARK = '<span class="brand-mark" aria-hidden="true"><img src="/mark-sasquatch.png" alt="" width="182" height="253" /></span>'
NUM_WORDS = {5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"}


def words(text, d0=0.0, step=0.08):
    """Wrap each word in a mask so it can rise into place on reveal."""
    return " ".join(
        '<span class="w"><span style="transition-delay:%.3fs">%s</span></span>' % (d0 + i * step, w)
        for i, w in enumerate(text.split(" ")))


APP_STORE_BADGE = ('<a class="badge-app-store" href="%s" target="_blank" rel="noopener" '
                   'aria-label="Download on the App Store">'
                   '<img src="/badge-app-store.svg" alt="Download on the App Store" '
                   'width="150" height="50" loading="lazy" /></a>')


def link(label, href, key=False, off=False, ext=False):
    if off:
        return '<span class="lnk off">%s %s</span>' % (label, ARR)
    if href.startswith("https://apps.apple.com/"):
        # Apple's official badge, unmodified, per App Store marketing guidelines
        return APP_STORE_BADGE % href
    rel = ' target="_blank" rel="noopener"' if ext else ""
    return '<a class="lnk%s" href="%s"%s>%s %s</a>' % (" key" if key else "", href, rel, label, ARR)


def shell(title, desc, body, accent="#52b788", canonical="", schema=None):
    ld = '\n  <script type="application/ld+json">%s</script>' % json.dumps(schema) if schema else ""
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>__T__</title>
  <meta name="description" content="__D__" />
  <link rel="canonical" href="__C__" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="__T__" />
  <meta property="og:description" content="__D__" />
  <meta property="og:url" content="__C__" />
  <meta property="og:site_name" content="SaaSquatch Lab" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="theme-color" content="#050907" />
  <link rel="icon" href="/mark-sasquatch.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;1,9..144,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <style>__CSS__</style>__LD__
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
__B__
  <script>__JS__</script>
</body>
</html>
""".replace("__T__", title).replace("__D__", desc).replace(
        "__C__", canonical or "https://www.saasquatchlab.com/").replace(
        "__CSS__", CSS.replace("__ACCENT__", accent).replace("__GRAIN__", GRAIN)).replace(
        "__JS__", JS).replace("__B__", body).replace("__LD__", ld)


def nav_groups(home):
    """Ordered nav descriptor: plain (label, href) pairs and dropdown groups.

    `home` controls whether in-page anchors resolve relative to `/` (product,
    privacy, and legal pages) or bare (the home page itself).
    """
    prefix = "" if home else "/"
    products = [(p["name"], "/%s" % p["slug"]) for p in PRODUCTS]
    for_good = [("About Sasquatch for Good", "/for-good")] + \
        [(find_product(s)["name"], "/%s" % s) for s in FOR_GOOD_SLUGS]
    support = [("Support", "/support"), ("Privacy Policy", "/privacy"),
               ("Terms of Use", "/terms"), ("Contact", "mailto:hello@saasquatchlab.com")]
    return [
        dict(kind="drop", id="products", label="Products", href="%s#products" % prefix, items=products),
        dict(kind="link", label="Principles", href="%s#principles" % prefix),
        dict(kind="link", label="About", href="%s#about" % prefix),
        dict(kind="drop", id="forgood", label="Sasquatch for Good", href="/for-good", items=for_good),
        dict(kind="drop", id="support", label="Support", href="/support", items=support),
        dict(kind="link", label="Contact", href="mailto:hello@saasquatchlab.com"),
    ]


def nav(home=False, back=False):
    groups = nav_groups(home)

    def desktop_item(g):
        if g["kind"] == "link":
            return '<li><a href="%s">%s</a></li>' % (g["href"], g["label"])
        sub = "".join('<li role="none"><a role="menuitem" href="%s">%s</a></li>' % (h, t)
                      for t, h in g["items"])
        menu_id = "nav-menu-%s" % g["id"]
        return ('<li class="nav-drop">'
                '<a href="%s" class="nav-trigger" aria-haspopup="true" aria-expanded="false" aria-controls="%s">'
                '%s</a>'
                '<ul class="nav-menu" id="%s" role="menu">%s</ul>'
                '</li>') % (g["href"], menu_id, g["label"], menu_id, sub)

    def mobile_item(g):
        if g["kind"] == "link":
            return '<li><a href="%s">%s</a></li>' % (g["href"], g["label"])
        sub = "".join('<li><a href="%s">%s</a></li>' % (h, t) for t, h in g["items"])
        return ('<li class="nav-mobile-group">'
                '<a class="nav-mobile-head" href="%s">%s</a>'
                '<ul>%s</ul></li>') % (g["href"], g["label"], sub)

    # The brand already sits on the left; repeating it on the right reads as a bug.
    back_link = ('<a class="nav-back" href="/#products">%s All products</a>' % ARR_B) if back else ""

    return """
  <nav class="nav">
    <div class="nav-left">
      <a href="/" class="brand">__MARK__ SaaSquatch Lab</a>
      __BACK__
    </div>
    <div class="nav-right">
      <ul class="nav-list">__ITEMS__</ul>
      <button type="button" class="nav-toggle" aria-expanded="false" aria-controls="nav-mobile">Menu</button>
    </div>
  </nav>
  <div class="nav-mobile" id="nav-mobile" hidden>
    __MBACK__
    <ul>__MITEMS__</ul>
  </div>
""".replace("__MARK__", MARK).replace("__BACK__", back_link).replace(
        "__ITEMS__", "".join(desktop_item(g) for g in groups)).replace(
        "__MBACK__", ('<a class="nav-back" href="/#products">%s All products</a>' % ARR_B) if back else "").replace(
        "__MITEMS__", "".join(mobile_item(g) for g in groups))


def footer():
    prods = "".join('<li><a href="/%s">%s</a></li>' % (p["slug"], p["name"]) for p in PRODUCTS)
    privs = "".join('<li><a href="/%s/privacy">%s</a></li>' % (p["slug"], p["name"]) for p in PRODUCTS)
    return """
  <footer class="foot">
    <div class="g">
      <div class="foot-g">
        <div>
          <a href="/" class="brand">__MARK__ SaaSquatch Lab</a>
          <p class="foot-blurb">Privacy-first software from the Pacific Northwest. Easy to use, and it stays out of your way.</p>
        </div>
        <div><h4>Products</h4><ul><li><a href="/for-good">Sasquatch for Good</a></li>__PRODS__</ul></div>
        <div><h4>Privacy</h4><ul><li><a href="/privacy">All policies</a></li>__PRIVS__</ul></div>
        <div><h4>Company</h4><ul>
          <li><a href="/support">Support</a></li>
          <li><a href="/terms">Terms of Use</a></li>
          <li><a href="/privacy">Privacy Policy</a></li>
          <li><a href="mailto:hello@saasquatchlab.com">hello@saasquatchlab.com</a></li>
        </ul></div>
      </div>
      <div class="foot-base">
        <span class="fig">&copy; 2026 SaaSquatch Lab LLC</span>
        <span class="fig">It&rsquo;s out there</span>
      </div>
    </div>
  </footer>
""".replace("__MARK__", MARK).replace("__PRODS__", prods).replace("__PRIVS__", privs)


# ─────────────────────────────────────────────────────────────────────────────
# Pages
# ─────────────────────────────────────────────────────────────────────────────
PRINCIPLES = [
    ("Private by default",
     "No ad SDKs, no cross-app tracking, no data brokers. Four of our seven products collect nothing "
     "at all, because they have no servers to collect it to. That is a structural promise, not a policy one."),
    ("Easy on purpose",
     "Privacy software has a reputation for being a chore. Ours is not. If a privacy guarantee costs you "
     "three extra taps, we treat that as a design bug and fix it."),
    ("Transparent by default",
     "Pricing, data practices, and limitations written in plain language — including the parts that are "
     "inconvenient for us. If we cannot defend a decision to your face, we do not ship it."),
    ("No dark patterns",
     "No manufactured urgency, no buried cancellation, no design that works against you. Cancelling is as "
     "easy as subscribing, because it happens in your own app store settings."),
    ("Built to last",
     "Self-funded and answerable to the people using the software rather than to investors, which is the "
     "only reason we can afford to plan in years instead of quarters."),
]


def spec_rows(pairs):
    return "".join(
        '<div class="spec r"><div class="spec-n">%02d</div><div class="spec-t">%s</div>'
        '<div class="spec-d">%s</div></div>' % (i, t, d)
        for i, (t, d) in enumerate(pairs, 1))


def find_product(slug):
    return next(p for p in PRODUCTS if p["slug"] == slug)


def product_row(p, n):
    """One hairline catalogue row for a product — shared by the home index and /for-good."""
    mark = ('<img class="item-logo" src="/%s" alt="" width="40" height="40" />' % p["logo"]
            if p.get("logo") else '<div class="item-logo em" aria-hidden="true">%s</div>' % p["emoji"])
    return ("""
          <a class="item r" href="/__SLUG__" style="--rc: __RC__">
            <div class="item-n">__N__</div>
            <div>
              <div class="item-id">__MARK__
                <div>
                  <div class="item-name">__NAME__</div>
                  <div class="item-cat">__CAT__</div>
                </div>
                <span class="st __TC__">__TAG__</span>
              </div>
              <ul class="item-meta">__META__</ul>
            </div>
            <p class="item-desc">__DESC__</p>
            <span class="item-go">Explore __ARR__</span>
          </a>
""".replace("__SLUG__", p["slug"]).replace("__RC__", p["accent"]).replace("__N__", "%02d" % n)
            .replace("__MARK__", mark).replace("__NAME__", p["name"])
            .replace("__CAT__", p["category"]).replace("__TC__", p["tagclass"])
            .replace("__TAG__", p["tag"]).replace("__DESC__", p["blurb"])
            .replace("__META__", "".join("<li>%s</li>" % m for m in p["meta"]))
            .replace("__ARR__", ARR))


def home():
    n_products = len(PRODUCTS)
    n_word = NUM_WORDS.get(n_products, str(n_products))
    items = [product_row(p, i) for i, p in enumerate(PRODUCTS, 1)]
    for_good_items = [product_row(find_product(s), i) for i, s in enumerate(FOR_GOOD_SLUGS, 1)]

    items.append("""
          <div class="item r" style="--rc: __RC__">
            <div class="item-n">__N__</div>
            <div>
              <div class="item-id"><div class="item-logo em" aria-hidden="true">__EM__</div>
                <div>
                  <div class="item-name">__NAME__</div>
                  <div class="item-cat">__CAT__</div>
                </div>
                <span class="st __TC__">__TAG__</span>
              </div>
              <ul class="item-meta">__META__</ul>
            </div>
            <p class="item-desc">__DESC__</p>
            <span class="item-go off">Not yet open</span>
          </div>
""".replace("__RC__", COMING["accent"]).replace("__N__", "%02d" % (len(PRODUCTS) + 1))
        .replace("__EM__", COMING["emoji"]).replace("__NAME__", COMING["name"])
        .replace("__CAT__", COMING["category"]).replace("__TC__", COMING["tagclass"])
        .replace("__TAG__", COMING["tag"]).replace("__DESC__", COMING["blurb"])
        .replace("__META__", "".join("<li>%s</li>" % m for m in COMING["meta"])))

    body = (nav(home=True) + """
  <header class="hero">
__SCENE__
    <div class="g">
      <p class="marque hero-mark">Est. 2026 &middot; Pacific Northwest</p>
      <div class="hero-type">
        <h1 class="mega">__H1A__<em class="ind">__H1B__</em></h1>
      </div>
      <div class="hero-foot">
        <div class="hero-acts">
          <div class="acts">
            __A1__
            __A2__
          </div>
        </div>
        <div class="hero-lede">
          <p class="lede"><strong>Privacy-first software that is actually easy to use.</strong>
          __NWORD__ products built on one rule &mdash; your data is not the product. No ad trackers,
          no data brokers, no dark patterns.</p>
        </div>
        <p class="fig hero-cap">Fig. 01 &mdash; Cascade ridgeline, first light. Subject unconfirmed.</p>
      </div>
    </div>
  </header>

  <main id="main">
  <section id="products" class="ruled">
    <div class="g">
      <div class="head r">
        <p class="marque key">The catalogue</p>
        <h2 class="t">__NWORD__ products,<br /><em>one refusal</em></h2>
        <p class="lede">Every one is built on the same refusal to monetise you. What differs is only how
        much data the product genuinely needs to function &mdash; and for most of them, the honest
        answer is none at all.</p>
      </div>
      <div class="idx">__ITEMS__</div>
    </div>
  </section>

  <section id="for-good" class="ruled">
    <div class="g">
      <div class="head r">
        <p class="marque key">A separate promise</p>
        <h2 class="t">Sasquatch<br /><em>for Good</em></h2>
        <p class="lede">__FORGOOD_SHORT__</p>
        <div class="acts r" style="margin-top: 1.5rem">__FORGOOD_LINK__</div>
      </div>
      <div class="idx">__FORGOOD_ITEMS__</div>
    </div>
  </section>

  <section id="principles" class="ruled">
    <div class="g">
      <div class="head r">
        <p class="marque key">How we build</p>
        <h2 class="t">Principles,<br /><em>not platitudes</em></h2>
        <p class="lede">Constraints we hold ourselves to when it costs us something, which is the only
        time a principle counts.</p>
      </div>
      <div class="specs">__PRINCIPLES__</div>
    </div>
  </section>

  <section id="about" class="ruled">
    <div class="g">
      <div class="head r">
        <p class="marque key">About</p>
        <h2 class="t">Independent software,<br /><em>long-term thinking</em></h2>
        <p class="lede">SaaSquatch Lab is an independent software company in the Pacific Northwest,
        building tools for communities, travellers, job seekers, and people who lift heavy things &mdash;
        without a surveillance business model underneath. Every product is self-funded, which is the
        whole reason we can build this way.</p>
      </div>
      <div class="ledger r">
        <div class="led"><div class="led-n">__NCOUNT__</div><div class="led-l">Products shipping or in review</div></div>
        <div class="led"><div class="led-n">4</div><div class="led-l">Apps that collect zero data</div></div>
        <div class="led"><div class="led-n">0</div><div class="led-l">Ad trackers, ever</div></div>
        <div class="led"><div class="led-n">PNW</div><div class="led-l">Pacific Northwest built</div></div>
      </div>
    </div>
  </section>

  <section class="closer ruled">
    <div class="g">
      <div class="closer-in">
        <h2 class="r">Software that <em>leaves you alone</em></h2>
        <p class="lede r">Start with whichever one solves a problem you actually have.</p>
        <div class="acts r">__A3__ __A4__</div>
      </div>
    </div>
  </section>
  </main>
""".replace("__SCENE__", scene(cryptid=True))
        .replace("__H1A__", words("It&rsquo;s"))
        .replace("__H1B__", words("out there", d0=0.09))
        .replace("__A1__", link("See what we build", "#products", key=True))
        .replace("__A2__", link("How we build", "#principles"))
        .replace("__A3__", link("Browse the catalogue", "#products", key=True))
        .replace("__A4__", link("Read our privacy policies", "/privacy"))
        .replace("__ITEMS__", "".join(items))
        .replace("__FORGOOD_SHORT__", FOR_GOOD_SHORT)
        .replace("__FORGOOD_LINK__", link("More about Sasquatch for Good", "/for-good", key=True))
        .replace("__FORGOOD_ITEMS__", "".join(for_good_items))
        .replace("__NWORD__", n_word).replace("__NCOUNT__", str(n_products))
        .replace("__PRINCIPLES__", spec_rows(PRINCIPLES)) + footer())

    return shell(
        "SaaSquatch Lab — It's out there",
        "Privacy-first software that is actually easy to use. Sasquatch Social, Squatch Lift, SizeSquatch, "
        "Squatch Connect, Squatch Travel, and App Tracker — from an independent studio in the Pacific "
        "Northwest. No ad trackers, no data brokers, no dark patterns.",
        body, accent="#52b788", canonical="https://www.saasquatchlab.com/",
        schema={"@context": "https://schema.org", "@type": "Organization",
                "name": "SaaSquatch Lab", "legalName": "SaaSquatch Lab LLC",
                "slogan": "It's out there",
                "url": "https://www.saasquatchlab.com/",
                "logo": "https://www.saasquatchlab.com/mark-sasquatch.png",
                "email": "hello@saasquatchlab.com",
                "description": "Independent privacy-first software studio in the Pacific Northwest.",
                "sameAs": ["https://www.sasquatchsocial.com", "https://saasquatchapptracker.com"]})


def product_schema(p):
    store = next((h for l, h, k, on in p["ctas"] if on and h.startswith("https://apps.apple.com/")), None)
    d = {"@context": "https://schema.org", "@type": "SoftwareApplication",
         "name": p["name"], "applicationCategory": "TravelApplication" if "eSIM" in p["category"] else "UtilitiesApplication",
         "operatingSystem": "iOS" + (", Android" if "Android" in p["category"] else ""),
         "description": re.sub(r"<[^>]+>", "", p["blurb"]).replace("&rsquo;", "'").replace("&middot;", "·"),
         "url": "https://www.saasquatchlab.com/%s" % p["slug"],
         "image": "https://www.saasquatchlab.com/%s" % p["logo"] if p.get("logo") else None,
         "author": {"@type": "Organization", "name": "SaaSquatch Lab", "url": "https://www.saasquatchlab.com"},
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}}
    if store: d["installUrl"] = store
    return {k: v for k, v in d.items() if v is not None}


def product_page(p):
    acts = " ".join(link(l, h, key=(k == "primary"), off=not on, ext=on and h.startswith("http"))
                    for l, h, k, on in p["ctas"])
    detail = "".join(
        '<div class="r"><h2>%s</h2>%s</div>' % (h, "".join("<p>%s</p>" % x for x in ps))
        for h, ps in p.get("detail", []))

    body = (nav(back=True) + """
  <header class="hero">
__SCENE__
    <div class="g">
      <div class="hero-mark">
        __ICON__
        <p class="marque key">__CAT__ &mdash; __TAG__</p>
        __FORGOOD__
      </div>
      <div class="hero-type">
        <h1 class="mega" style="font-size: clamp(2.3rem, 6.6vw, 5.2rem)">__TAGLINE__</h1>
      </div>
      <div class="hero-foot">
        <div class="hero-acts"><div class="acts">__ACTS__</div></div>
        <div class="hero-lede"><p class="lede">__BLURB__</p></div>
        <p class="fig hero-cap">__NOTE__</p>
      </div>
    </div>
  </header>

  <main id="main">
  <section style="padding-top: 0">
    <div class="g">
      <div class="band r">
        <p>__PROMISE__</p>
        <div class="side">__PLINK__</div>
      </div>
    </div>
  </section>

  <section class="ruled" style="padding-top: clamp(3rem, 7vh, 5rem)">
    <div class="g">
      <div class="head r">
        <p class="marque key">What it does</p>
        <h2 class="t">__NAME__, <em>in full</em></h2>
      </div>
      <div class="specs">__SPECS__</div>
    </div>
  </section>

  __DETAIL__

  <section class="closer ruled">
    <div class="g">
      <div class="closer-in">
        <h2 class="r">__NAME__</h2>
        <p class="lede r">__TAGLINE_P__</p>
        <div class="acts r">__ACTS__</div>
      </div>
    </div>
  </section>
  </main>
""".replace("__SCENE__", scene(cryptid=False)).replace("__CAT__", p["category"])
        .replace("__ICON__",
                 '<img class="hero-icon" src="/%s" alt="%s app icon" width="62" height="62" />'
                 % (p["logo"], p["name"]) if p.get("logo")
                 else '<div class="hero-icon em" aria-hidden="true">%s</div>' % p["emoji"])
        .replace("__TAG__", p["tag"])
        .replace("__FORGOOD__",
                 '<p class="marque" style="margin-top:0.6rem"><a href="/for-good">Part of Sasquatch for Good</a></p>'
                 if p.get("for_good") else "")
        .replace("__TAGLINE__", words(p["tagline"]))
        .replace("__TAGLINE_P__", p["tagline"])
        .replace("__ACTS__", acts).replace("__BLURB__", p["blurb"])
        .replace("__NOTE__", p["hero_note"]).replace("__PROMISE__", p["promise"])
        .replace("__PLINK__", link("Privacy policy", "/%s/privacy" % p["slug"]))
        .replace("__NAME__", p["name"]).replace("__SPECS__", spec_rows(p["features"]))
        .replace("__DETAIL__",
                 ('<section class="ruled"><div class="g"><div class="prose">%s</div></div></section>' % detail)
                 if detail else "") + footer())

    return shell(
        "%s — %s | SaaSquatch Lab" % (p["name"], p["tagline"].rstrip(".")),
        p["blurb"].replace("&mdash;", "—").replace("&rsquo;", "'"),
        body, accent=p["accent"],
        canonical="https://www.saasquatchlab.com/%s" % p["slug"], schema=product_schema(p))


def privacy_page(slug, d):
    secs = "".join(
        '<h2 id="%s">%s</h2>%s' % (
            h.lower().replace(" ", "-").replace("&rsquo;", ""), h,
            "".join("<p>%s</p>" % x for x in ps))
        for h, ps in d["sections"])
    body = (nav(back=True) + """
  <main id="main">
    <section style="padding-top: clamp(3rem, 8vh, 5rem)">
      <div class="g">
        <div class="prose">
          <p class="marque key" style="margin-bottom: 1.5rem">Privacy policy</p>
          <h1 style="font-size: clamp(2.1rem, 5.5vw, 3.3rem); line-height: 1.05; margin-bottom: 0.7rem;">__NAME__</h1>
          <p class="fig" style="margin-bottom: 2rem;">SaaSquatch Lab LLC &middot; Effective __DATE__</p>
          <p class="lead">__SHORT__</p>
          __SECS__
          <h2 id="changes">Changes</h2>
          <p>If we change this policy we will update the effective date above and, for material changes, give
          notice in the app. This sits alongside our <a href="/privacy">company-wide privacy policy</a> and
          <a href="/terms">Terms of Use</a>.</p>
          <h2 id="contact">Contact</h2>
          <p>SaaSquatch Lab LLC, Pacific Northwest, United States<br />
          <a href="mailto:hello@saasquatchlab.com">hello@saasquatchlab.com</a></p>
        </div>
      </div>
    </section>
  </main>
""".replace("__NAME__", d["name"] + " Privacy Policy").replace("__SHORT__", d["short"])
        .replace("__SECS__", secs).replace("__DATE__", d.get("effective", "7 September 2026")) + footer())

    return shell(
        "%s Privacy Policy — SaaSquatch Lab" % d["name"],
        d["short"].replace("&rsquo;", "'"),
        body, accent=d["accent"],
        canonical="https://www.saasquatchlab.com/%s/privacy" % slug)


def for_good_page():
    """The /for-good landing page: fuller statement, the two apps, how to reach us."""
    items = [product_row(find_product(s), i) for i, s in enumerate(FOR_GOOD_SLUGS, 1)]
    statement = "".join("<p>%s</p>" % para for para in FOR_GOOD_FULL)
    body = (nav(back=True) + """
  <header class="hero" style="padding-bottom: clamp(2rem, 5vh, 3.5rem)">
__SCENE__
    <div class="g">
      <p class="marque hero-mark key">A separate promise</p>
      <div class="hero-type">
        <h1 class="mega" style="font-size: clamp(2.6rem, 7.2vw, 5.6rem)">Sasquatch<em> for Good</em></h1>
      </div>
    </div>
  </header>

  <main id="main">
  <section style="padding-top: 0">
    <div class="g">
      <div class="prose r">__STATEMENT__</div>
    </div>
  </section>

  <section class="ruled">
    <div class="g">
      <div class="head r">
        <p class="marque key">The apps</p>
        <h2 class="t">Free, on purpose,<br /><em>no exceptions</em></h2>
        <p class="lede">No account, no ads, no subscriptions &mdash; and none planned.</p>
      </div>
      <div class="idx">__ITEMS__</div>
    </div>
  </section>

  <section class="closer ruled">
    <div class="g">
      <div class="closer-in">
        <h2 class="r">Get in <em>touch</em></h2>
        <p class="lede r">Have an idea that belongs in this family, or a question about one of these apps?
        Email us &mdash; we read everything.</p>
        <div class="acts r">__CONTACT__ __PRIVACY__</div>
      </div>
    </div>
  </section>
  </main>
""".replace("__SCENE__", scene(cryptid=True))
        .replace("__STATEMENT__", statement)
        .replace("__ITEMS__", "".join(items))
        .replace("__CONTACT__", link("hello@saasquatchlab.com", "mailto:hello@saasquatchlab.com", key=True))
        .replace("__PRIVACY__", link("Read our privacy policies", "/privacy")) + footer())

    return shell(
        "Sasquatch for Good — SaaSquatch Lab",
        "A family of free apps built to help, not to make money: no accounts, no ads, no subscriptions. "
        "Squatch Vitals and Squatch Aphantasia.",
        body, accent="#4f86c6", canonical="https://www.saasquatchlab.com/for-good")


def legal_page(body, title, desc, canonical, accent="#52b788"):
    """Wrap hand-authored legal/support copy in the shared shell."""
    inner = (nav(back=True) + """
  <main id="main">
    <section style="padding-top: clamp(3rem, 8vh, 5rem)">
      <div class="g">
        <div class="prose">__BODY__</div>
      </div>
    </section>
  </main>
""".replace("__BODY__", body) + footer())
    return shell(title, desc, inner, accent=accent, canonical=canonical)


def write(rel, html):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(html)
    print("  %-40s %6.1f KB" % (rel, len(html) / 1024.0))


def main():
    assert not os.path.isdir(os.path.join(ROOT, "public")), \
        "A public/ directory exists — that 404s the whole site. See CLAUDE.md."
    print("Building saasquatchlab.com")
    write("index.html", home())
    write("for-good/index.html", for_good_page())
    for p in PRODUCTS:
        write("%s/index.html" % p["slug"], product_page(p))
    for slug, d in POLICIES.items():
        write("%s/privacy/index.html" % slug, privacy_page(slug, d))

    # Registered with App Store Connect — these paths must not change.
    write("privacy/index.html", legal_page(
        PRIVACY, "Privacy Policy — SaaSquatch Lab",
        "SaaSquatch Lab privacy policy covering Sasquatch Social, Squatch Lift, SizeSquatch, "
        "Squatch Connect, Squatch Travel, and App Tracker.",
        "https://www.saasquatchlab.com/privacy"))
    write("terms/index.html", legal_page(
        TERMS, "Terms of Use — SaaSquatch Lab",
        "Terms of Use and End User License Agreement for SaaSquatch Lab apps, including "
        "subscription terms for Squatch Lift Pro.",
        "https://www.saasquatchlab.com/terms"))
    write("support/index.html", legal_page(
        SUPPORT, "Support — SaaSquatch Lab",
        "Support for SaaSquatch Lab products: SizeSquatch, Sasquatch Social, and App Tracker.",
        "https://www.saasquatchlab.com/support"))

    pages = ["/", "/for-good"] + ["/%s" % p["slug"] for p in PRODUCTS] \
        + ["/%s/privacy" % slug for slug in POLICIES] \
        + ["/sizesquatch/privacy", "/squatch-connect/privacy", "/squatchtravel/privacy"] \
        + ["/privacy", "/terms", "/support"]
    write_crawl_files(sorted(set(pages), key=pages.index))

    print("Still hand-maintained: /sizesquatch/privacy, /squatch-connect/privacy,")
    print("  /squatchtravel/privacy (each App Store registered, content unchanged)")


def write_crawl_files(pages):
    base = "https://www.saasquatchlab.com"
    Path("robots.txt").write_text("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % base)
    urls = "".join("  <url><loc>%s%s</loc></url>\n" % (base, u) for u in pages)
    Path("sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % urls)
    lines = ["# SaaSquatch Lab", "", "> Privacy-first software that is actually easy to use. Independent studio in the Pacific Northwest.", "", "## Products"]
    for p in PRODUCTS:
        store = next((h for l, h, k, on in p["ctas"] if on and h.startswith("https://apps.apple.com/")), None)
        desc = re.sub(r"<[^>]+>", "", p["blurb"]).replace("&rsquo;", "'").replace("&middot;", "·")
        lines.append("- [%s](%s/%s): %s%s" % (p["name"], base, p["slug"], desc, (" App Store: " + store) if store else ""))
    lines += ["", "## Policies", "- [Privacy](%s/privacy)" % base, "- [Terms of Use](%s/terms)" % base, "- [Support](%s/support)" % base]
    Path("llms.txt").write_text("\n".join(lines) + "\n")
    print("  robots.txt, sitemap.xml (%d urls), llms.txt" % len(pages))


if __name__ == "__main__":
    main()
