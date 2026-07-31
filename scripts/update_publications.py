#!/usr/bin/env python3
"""
Fetch new publications from Alice Rogers's ORCID record and append any
that aren't already in publications.bib.

How it works:
  1. Pull the list of DOIs from her public ORCID works.
  2. Look each DOI up on Crossref, which (unlike ORCID) reliably has the
     full author list, journal, volume, pages, etc.
  3. Skip anything before MIN_YEAR (she started directing the lab in
     2018, so earlier papers from prior positions aren't listed here)
     and anything whose DOI is already in publications.bib.
  4. Append new entries to publications.bib in the same format as the
     existing ones. Existing entries are never modified or reordered --
     this only ever adds.

Run manually with: python3 scripts/update_publications.py
The GitHub Actions workflow in .github/workflows/update-publications.yml
runs this on a schedule and opens a pull request if anything changed, so
a human reviews new entries before they go live.
"""

import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ORCID_ID = "0000-0002-7244-0860"  # Alice Rogers
MIN_YEAR = 2018  # excludes papers from before she directed the lab
BIB_PATH = Path(__file__).resolve().parent.parent / "publications.bib"
CONTACT_EMAIL = "alice.rogers@vuw.ac.nz"  # used in Crossref's "polite pool" header
USER_AGENT = f"meem-lab-website-bot/1.0 (mailto:{CONTACT_EMAIL})"


def fetch_json(url):
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def get_orcid_dois(orcid_id):
    data = fetch_json(f"https://pub.orcid.org/v3.0/{orcid_id}/works")
    dois = []
    for group in data.get("group", []):
        for summary in group.get("work-summary", []):
            for ext_id in (summary.get("external-ids", {}) or {}).get("external-id", []):
                if ext_id.get("external-id-type") == "doi":
                    dois.append(ext_id["external-id-value"].strip().lower())
    return sorted(set(dois))


def get_crossref_work(doi):
    try:
        data = fetch_json(f"https://api.crossref.org/works/{urllib.request.quote(doi)}")
    except urllib.error.HTTPError:
        return None
    return data.get("message")


def existing_dois():
    if not BIB_PATH.exists():
        return set()
    text = BIB_PATH.read_text()
    return {m.strip().lower() for m in re.findall(r"doi\s*=\s*\{([^}]*)\}", text)}


def existing_keys():
    if not BIB_PATH.exists():
        return set()
    text = BIB_PATH.read_text()
    return set(re.findall(r"@\w+\{([^,]+),", text))


def bibtex_escape(value):
    # Crossref titles sometimes carry JATS/XML markup (e.g. <scp><i>Genus
    # species</i></scp> for italicized species names) -- strip tags and
    # collapse the whitespace that's left behind, rather than leaking raw
    # markup into the rendered bibliography.
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value.replace("{", "").replace("}", "")


def make_key(work, used_keys):
    family = "Unknown"
    authors = work.get("author") or []
    if authors:
        family = re.sub(r"[^A-Za-z]", "", authors[0].get("family", "Unknown")) or "Unknown"
    year = str((work.get("issued", {}).get("date-parts") or [[None]])[0][0] or "n.d.")
    base = f"{family}{year}"
    key = base
    suffix = ord("a")
    while key in used_keys:
        key = f"{base}{chr(suffix)}"
        suffix += 1
    used_keys.add(key)
    return key


def format_authors(work):
    parts = []
    for a in work.get("author") or []:
        given = a.get("given", "").strip()
        family = a.get("family", "").strip()
        if family and given:
            parts.append(f"{family}, {given}")
        elif family:
            parts.append(family)
    return " and ".join(parts)


def to_bibtex(work, key):
    title = bibtex_escape((work.get("title") or [""])[0])
    journal = bibtex_escape((work.get("container-title") or [""])[0])
    year = (work.get("issued", {}).get("date-parts") or [[None]])[0][0]
    volume = work.get("volume", "")
    issue = work.get("issue", "")
    page = work.get("page", "")
    doi = work.get("DOI", "")
    author = format_authors(work)

    lines = [f"@article{{{key},"]
    if author:
        lines.append(f"  author = {{{author}}},")
    if title:
        lines.append(f"  title = {{{title}}},")
    if journal:
        lines.append(f"  journal = {{{journal}}},")
    if year:
        lines.append(f"  year = {{{year}}},")
    if volume:
        lines.append(f"  volume = {{{volume}}},")
    if issue:
        lines.append(f"  number = {{{issue}}},")
    if page:
        lines.append(f"  pages = {{{page}}},")
    if doi:
        lines.append(f"  doi = {{{doi}}}")
    lines.append("}")
    return "\n".join(lines)


def main():
    if ORCID_ID == "0000-0000-0000-0000":
        print("ORCID_ID is still a placeholder -- edit scripts/update_publications.py first.", file=sys.stderr)
        return 1

    known_dois = existing_dois()
    used_keys = existing_keys()

    try:
        candidate_dois = get_orcid_dois(ORCID_ID)
    except urllib.error.URLError as e:
        print(f"Could not reach ORCID: {e}", file=sys.stderr)
        return 1

    new_entries = []
    for doi in candidate_dois:
        if doi in known_dois:
            continue
        work = get_crossref_work(doi)
        if not work:
            continue
        year = (work.get("issued", {}).get("date-parts") or [[None]])[0][0]
        if not year or year < MIN_YEAR:
            continue
        key = make_key(work, used_keys)
        new_entries.append(to_bibtex(work, key))

    if not new_entries:
        print("No new publications found.")
        return 0

    with BIB_PATH.open("a") as f:
        f.write("\n\n" + "\n\n".join(new_entries) + "\n")

    print(f"Added {len(new_entries)} new publication(s) to {BIB_PATH.name}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
