#!/usr/bin/env python3
"""Small stdlib-only check for local HTML references and fragment targets.

Not a full HTML validator. Intended as a fast pull-request smoke test.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

PUBLIC = Path(__file__).resolve().parent.parent / "public"
INDEX = PUBLIC / "index.html"


class LocalReferences(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.errors = []
        self.experiments = 0
        self.map_names = set()
        self.usemaps = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if "lab-card" in values.get("class", "").split():
            self.experiments += 1
        if tag == "map" and values.get("name"):
            self.map_names.add(values["name"])
        if values.get("usemap"):
            self.usemaps.append(values["usemap"])
        if values.get("srcset"):
            for descriptor in values["srcset"].split(","):
                source = descriptor.strip().split(" ")[0]
                if source:
                    self.links.append(source)
        if values.get("poster"):
            self.links.append(values["poster"])
        element_id = values.get("id")
        if element_id:
            if element_id in self.ids:
                self.errors.append("duplicate id: " + element_id)
            self.ids.add(element_id)
        for attribute in ("href", "src"):
            if values.get(attribute):
                self.links.append(values[attribute])


def main():
    if not INDEX.is_file():
        print("missing public/index.html")
        return 1

    parser = LocalReferences()
    parser.feed(INDEX.read_text(encoding="utf-8"))
    errors = list(parser.errors)
    if parser.experiments < 23:
        errors.append(f"expected at least 23 experiments, got {parser.experiments}")
    for name in parser.usemaps:
        if not name.startswith("#") or name[1:] not in parser.map_names:
            errors.append("missing image map: " + name)

    for item in parser.links:
        url = urlsplit(item)
        if url.scheme or url.netloc or item.startswith("//"):
            continue
        path = unquote(url.path)
        target = (PUBLIC / path).resolve() if path else INDEX
        try:
            target.relative_to(PUBLIC.resolve())
        except ValueError:
            errors.append("path escapes public/: " + item)
            continue
        if path and not target.is_file():
            errors.append("missing local file: " + item)
        if url.fragment and (not path or target == INDEX) and unquote(url.fragment) not in parser.ids:
            errors.append("missing fragment target: " + item)

    for required in ("styles.css", "app.js", "favicon.svg", "robots.txt", "sitemap.xml", "assets/picture-wide.svg", "assets/picture-narrow.svg", "assets/image-map.svg", "assets/media-poster.svg"):
        if not (PUBLIC / required).is_file():
            errors.append("missing required file: " + required)

    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print("OK: local references, fragments, and required files")
    return 0


if __name__ == "__main__":
    sys.exit(main())