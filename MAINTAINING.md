# Maintaining the site — quick reference for Alice

This is a short "what do I do when" checklist for the recurring things you'll
need to update. Everything here happens in a web browser on github.com — you
never need to install anything or touch a terminal. For the full step-by-step
of any task (exact buttons to click, field-by-field guidance), follow the
link — this doc won't repeat those details, just tell you where to go and
what to expect.

If anything here doesn't match what you're seeing, or a step feels wrong,
stop and ask Chelsey rather than guessing — it's easy to fix a mistake in
this repo, but easier still to just ask first.

## A new publication comes out

Every Monday, a bot checks my ORCID record and — if it finds a paper that
isn't already on the Research page — opens a **pull request** titled "New
publications found on ORCID." You'll see it under the **Pull requests** tab
of the repository (there'll be a notification badge).

1. Open the pull request and look at the diff — it'll show one or more new
   `@article{...}` blocks being added to `publications.bib`.
2. Skim the title, authors, and journal for anything obviously wrong
   (auto-fetched data occasionally has a formatting quirk).
3. If it looks right, click **Merge pull request**. It'll be live on the
   Research page within a couple of minutes.
4. If something looks off, either edit it directly in the PR (there's an
   edit/pencil icon on the changed file) or ask Chelsey to take a look.

**If a paper isn't showing up** (e.g. it's brand new and not yet on my ORCID
record, or was never linked to my ORCID), you can add it by hand instead:
open [`publications.bib`](publications.bib), click edit, and add a new entry
in the same format as the others near the top of the file, then commit. The
Research page sorts by year automatically, so it doesn't matter where in the
file you add it.

## Someone joins the lab

This is normally self-service — send new lab members the link to the
[README's "Adding yourself to the People page"
section](README.md#adding-yourself-to-the-people-page) and they can add their
own profile without your help. If you'd rather add someone yourself, the same
instructions work for you too.

## Someone leaves the lab

Follow [the README's "When someone leaves the lab"
section](README.md#when-someone-leaves-the-lab) — in short: move their file
from `people/` to `people/past/`, add a `year_end`, and add "Dr." to their
name if they finished a PhD with us. They'll move from "Current Lab Members"
to "Past Members" on the People page automatically.

## Posting or removing a job/PhD listing

Follow [the README's "Posting or hiding job/PhD opportunities"
section](README.md#posting-or-hiding-jobphd-opportunities). Short version:
edit `opportunities.qmd` directly — either add a listing under "Current
Opportunities," or flip `show: true` to `show: false` at the top of the file
when there's nothing to advertise (the page stays up with a "check back
soon" message rather than disappearing or looking broken).

## Adding a news/media mention

There's no special system for this one — it's just a plain list.

1. Open [`media.qmd`](media.qmd) and click the pencil/edit icon.
2. Add a new line under "In the News" or "Media Appearances," matching the
   format of the existing entries (a markdown link, then a dash and the
   source/date).
3. Commit your change.

## Updating a research project description or funding info

Open [`research.qmd`](research.qmd) directly and edit the relevant section —
project descriptions, funders, and the team list under each project are all
plain text/markdown you can edit like a Word document.

## To do: missing past-member links

A few alumni on the People page don't have a link on their name yet. If you
come across a LinkedIn, Google Scholar, or similar profile link for any of
them, add it as `link1` in their file's `links:` section (same pattern as
the other past members) and commit:

- [ ] Andy Chang — `people/past/andy-chang.md`
- [ ] Baylee Wade — `people/past/baylee-wade.md`
- [ ] Victoria Carrington — `people/past/victoria-carrington.md`

Example — if `links:` currently just says `links:` with nothing under it,
change it to:

```yaml
links:
  link1: https://www.linkedin.com/in/their-profile/
```

## If something looks broken after a change

1. Check the **Actions** tab of the repository — a yellow dot means it's
   still building (wait a minute or two), a green check means it's live, a
   red cross means the build failed.
2. If it's a red cross, click into the failed run to see what went wrong, or
   just ask Chelsey — build failures are almost always a technical issue with
   the site's dependencies, not something wrong with the content you added.

## The two things worth remembering

- **You can't easily break the live site.** Every change is a commit, and
  every commit can be undone. If something looks wrong after a change, the
  safest fix is usually just to undo that specific edit.
- **Nothing you do here updates the live site immediately** — it takes
  1–2 minutes for GitHub to rebuild and republish after a change lands on
  `main`. If you don't see your change yet, give it a minute before assuming
  something's wrong.
