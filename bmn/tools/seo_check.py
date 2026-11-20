#!/usr/bin/env python3
"""BMN repository SEO checks. Standard library only; no network requests."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import json
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://bdgaskins27889.github.io/bmn/"
errors = []

class HeadParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_head = False
        self.in_json = False
        self.scripts = []
        self.meta = {}
        self.canonicals = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "head":
            self.in_head = True
        if not self.in_head:
            return
        if tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta.setdefault(key.lower(), []).append(a.get("content", ""))
        if tag == "link" and a.get("rel") == "canonical":
            self.canonicals.append(a.get("href"))
        if tag == "script" and a.get("type") == "application/ld+json":
            self.in_json = True
    def handle_data(self, data):
        if self.in_json:
            self.scripts.append(data)
    def handle_endtag(self, tag):
        if tag == "script":
            self.in_json = False
        if tag == "head":
            self.in_head = False

def fail(page, reason):
    errors.append(f"{page}: {reason}")

sitemap = ROOT / "sitemap.xml"
try:
    tree = ET.parse(sitemap)
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [x.text for x in tree.findall(".//s:loc", ns)]
except (ET.ParseError, OSError) as exc:
    print(f"Invalid sitemap: {exc}")
    sys.exit(1)

if len(urls) != len(set(urls)):
    fail("sitemap.xml", "duplicate URL entries")
expected = []
for page in sorted(ROOT.rglob("*.html")):
    rel = page.relative_to(ROOT).as_posix()
    if rel == "index.html":
        url = BASE
    elif rel.endswith("/index.html"):
        url = BASE + rel[:-10]
    else:
        url = BASE + rel
    expected.append(url)
    parser = HeadParser()
    parser.feed(page.read_text(encoding="utf-8"))
    if parser.canonicals != [url]:
        fail(rel, f"canonical mismatch: {parser.canonicals!r}, expected {url}")
    for field in ("description", "twitter:card", "twitter:image", "og:image", "og:title", "og:description", "og:url"):
        values = parser.meta.get(field, [])
        if len(values) != 1 or not values[0]:
            fail(rel, f"missing/duplicate {field}")
    if parser.meta.get("og:url") != [url]:
        fail(rel, "og:url does not match canonical")
    if not parser.scripts:
        fail(rel, "missing JSON-LD")
    for raw in parser.scripts:
        try:
            data = json.loads(raw)
            if not isinstance(data, dict) or data.get("@context") != "https://schema.org":
                fail(rel, "invalid Schema.org context")
        except json.JSONDecodeError as exc:
            fail(rel, f"invalid JSON-LD: {exc}")
    for field in ("og:image", "twitter:image"):
        for image_url in parser.meta.get(field, []):
            if not image_url.startswith(BASE):
                fail(rel, f"{field} must use an absolute BMN URL")
                continue
            local = ROOT / unquote(urlparse(image_url).path.removeprefix("/bmn/"))
            if not local.is_file():
                fail(rel, f"{field} references missing file: {local.name}")

for url in expected:
    if url not in urls:
        fail("sitemap.xml", f"missing HTML page: {url}")
for url in urls:
    if url not in expected:
        fail("sitemap.xml", f"URL has no matching HTML file: {url}")
if errors:
    print("\n".join("ERROR: " + e for e in errors))
    sys.exit(1)
print(f"BMN SEO checks passed: {len(expected)} HTML pages and {len(urls)} sitemap entries.")
