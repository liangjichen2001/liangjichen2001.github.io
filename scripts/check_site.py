"""Check rendered Jekyll pages, internal links, anchors, and template leakage.

Usage: python scripts/check_site.py _site [--baseurl /preview]
Uses only the Python standard library; no browser or network is required.
"""

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.references = []
        self.ids = set()
        self.canonical = None
        self.redirect = False
        self.language = None
        self.headings = 0
        self.text = []
        self.feed(source)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "html":
            self.language = attrs.get("lang")
        if tag == "h1":
            self.headings += 1
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "refresh":
            self.redirect = True
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")
        for attribute in ("href", "src"):
            if attrs.get(attribute):
                self.references.append(attrs[attribute])

    def handle_data(self, data):
        self.text.append(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    parser.add_argument("--baseurl", default="")
    args = parser.parse_args()
    root = args.directory.resolve()
    baseurl = args.baseurl.rstrip("/")
    errors = []
    pages = {path.resolve(): Page(path.read_text(encoding="utf-8")) for path in root.rglob("*.html")}
    if not pages:
        parser.error(f"No generated HTML pages found in {root}")

    required = ("index.html", "research/index.html", "projects/index.html", "experience/index.html", "cv/index.html", "publication/2024-wt-cnn-lstm/index.html", "404.html", "sitemap/index.html")
    for relative in required:
        if not (root / relative).is_file():
            errors.append(f"Missing page: {relative}")

    references = 0
    for path, page in pages.items():
        relative = path.relative_to(root).as_posix()
        if not page.redirect:
            if not page.language:
                errors.append(f"{relative}: document language is missing")
            if page.headings != 1:
                errors.append(f"{relative}: expected one main heading, found {page.headings}")
        if re.search(r"Paper Title Number|GitHub University|Blog Post number|Lorem ipsum", " ".join(page.text), re.IGNORECASE):
            errors.append(f"{relative}: template example content was published")
        canonical = page.canonical or "https://liangjichen2001.github.io/"
        origin = urlsplit(canonical)
        page_url = urljoin(origin.scheme + "://" + origin.netloc, baseurl + "/" + relative)
        for reference in page.references:
            parsed = urlsplit(urljoin(page_url, reference))
            if parsed.scheme not in ("http", "https") or parsed.netloc != origin.netloc:
                continue
            references += 1
            target_path = unquote(parsed.path)
            if baseurl:
                if not target_path.startswith(baseurl + "/") and target_path != baseurl:
                    errors.append(f"{relative}: link escapes baseurl: {reference}")
                    continue
                target_path = target_path[len(baseurl):]
            target = (root / target_path.lstrip("/")).resolve()
            if not target.is_relative_to(root):
                errors.append(f"{relative}: link escapes output directory: {reference}")
                continue
            if target.is_dir():
                target = target / "index.html"
            if not target.is_file():
                errors.append(f"{relative}: missing target: {reference}")
            elif parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:
                errors.append(f"{relative}: missing anchor: {reference}")

    if errors:
        print("Site checks failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    print(f"Site checks passed: {len(pages)} HTML pages, {references} local links/assets; no template example content.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
