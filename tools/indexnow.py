#!/usr/bin/env python3
"""Re-submit every sitemap URL to IndexNow (Bing/Yandex — ChatGPT search uses Bing).

Run after any deploy where page content changed:

    python3 tools/indexnow.py

Reads sitemap.xml (already built by tools/build_site.py) and POSTs the full URL list to
https://api.indexnow.org/indexnow in one call. The key must match INDEXNOW_KEY in
build_site.py and must already be live at https://www.saasquatchlab.com/<key>.txt — the
build writes that file itself, so just deploy before running this.

A 200 or 202 response means IndexNow accepted the submission.
"""
import json
import re
import sys
import urllib.request

sys.path.insert(0, __file__.rsplit("/tools/", 1)[0] + "/tools")
from build_site import INDEXNOW_KEY  # noqa: E402

HOST = "www.saasquatchlab.com"
ENDPOINT = "https://api.indexnow.org/indexnow"
SITEMAP = __file__.rsplit("/tools/", 1)[0] + "/sitemap.xml"


def main():
    with open(SITEMAP) as f:
        xml = f.read()
    urls = re.findall(r"<loc>(.*?)</loc>", xml)
    assert urls, "no <loc> entries found in %s — run tools/build_site.py first" % SITEMAP

    payload = json.dumps({
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": "https://%s/%s.txt" % (HOST, INDEXNOW_KEY),
        "urlList": urls,
    }).encode("utf-8")

    req = urllib.request.Request(
        ENDPOINT, data=payload, method="POST",
        headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            print("IndexNow: HTTP %d for %d URLs" % (r.status, len(urls)))
    except urllib.error.HTTPError as e:
        print("IndexNow: HTTP %d for %d URLs — %s" % (e.code, len(urls), e.read().decode(errors="replace")))
        raise


if __name__ == "__main__":
    main()
