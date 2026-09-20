#!/usr/bin/env python3
"""Write the commitments from commitments.json into index.html and llms.txt.

Both files carry a marked block; this script replaces what is between the markers and
nothing else. The heading on the page ("Six commitments that stand in every contract.")
is written from the number of entries, so the count and the list cannot disagree again
— the fault found in the estate audit of 5 September 2026.

Run it after every edit to commitments.json:   python3 build/sync-commitments.py
It prints what it changed and exits non-zero if a marker is missing.
"""
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
NUMBER = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six",
          7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"}


def replace_block(text: str, name: str, body: str, path: pathlib.Path) -> str:
    start, end = f"commitments:{name}:start", f"commitments:{name}:end"
    pattern = re.compile(
        rf"(?P<open>[<#!-]*\s*{re.escape(start)}[^\n]*\n)(?P<body>.*?)(?P<close>[^\n]*{re.escape(end)}[^\n]*)",
        re.S)
    m = pattern.search(text)
    if not m:
        sys.exit(f"ERROR: marker '{start}' not found in {path.name} — restore it before running this.")
    return text[:m.start("body")] + body + text[m.end("body"):]


def main() -> None:
    items = json.loads((ROOT / "commitments.json").read_text(encoding="utf-8"))["commitments"]
    count = len(items)

    page = ROOT / "index.html"
    src = page.read_text(encoding="utf-8")
    lis = "\n".join(
        '    <li><span class="k">{k}</span><span class="v">{v}</span><span class="e">{e}</span></li>'.format(
            k=html.escape(i["key"]), v=html.escape(i["value"]), e=html.escape(i["page"]))
        for i in items)
    src = replace_block(src, "list", lis + "\n", page)
    heading = f'    <p class="lede">{NUMBER[count]} commitments that stand in every contract.</p>\n'
    src = replace_block(src, "heading", heading, page)
    page.write_text(src, encoding="utf-8")

    # llms.txt is read by people and by assistants, so it carries no marker comments:
    # the heading is the anchor, and the bullets under it are rewritten.
    ai = ROOT / "llms.txt"
    txt = ai.read_text(encoding="utf-8")
    heading_line = "## Commitments in every contract\n"
    m = re.search(re.escape(heading_line) + r"(?:- .*\n)+", txt)
    if not m:
        sys.exit("ERROR: the commitments heading and its bullets were not found in llms.txt.")
    bullets = "\n".join("- " + i["plain"] for i in items) + "\n"
    ai.write_text(txt[:m.start()] + heading_line + bullets + txt[m.end():], encoding="utf-8")

    print(f"{count} commitments written to index.html (list + heading) and llms.txt.")


if __name__ == "__main__":
    main()
