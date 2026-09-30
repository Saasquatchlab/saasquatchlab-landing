#!/usr/bin/env python3
"""Refresh the Squatch Connect catalog snapshot used to build the eSIM SEO pages.

Run:  python3 tools/data/refresh_catalog.py

Fetches the public catalog endpoint and overwrites tools/data/connect_catalog.json.
Re-run tools/build_site.py afterwards to regenerate the destination pages with any
updated plans/pricing. Snapshotting (rather than fetching at request time) keeps
builds reproducible — this is a static site with no server-side rendering.
"""
import datetime
import json
import os
import urllib.request

SOURCE = "https://nbcwerrjqdouekpydfsy.supabase.co/functions/v1/catalog"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "connect_catalog.json")


def main():
    with urllib.request.urlopen(SOURCE, timeout=20) as r:
        data = json.loads(r.read().decode("utf-8"))

    assert "destinations" in data and "plans" in data, "unexpected catalog shape: %r" % list(data.keys())

    out = {
        "fetchedAt": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": SOURCE,
        "destinations": data["destinations"],
        "plans": data["plans"],
    }
    with open(OUT, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("Wrote %s (%d destinations, %d plans, fetched %s)" % (
        OUT, len(out["destinations"]), len(out["plans"]), out["fetchedAt"]))


if __name__ == "__main__":
    main()
