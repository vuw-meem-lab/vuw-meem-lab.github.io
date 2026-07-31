
# MEEM Lab Website

This repository contains the Quarto-based website for the MEEM Lab at Victoria University of Wellington: <https://vuw-meem-lab.github.io/>

You do **not** need to install anything or know how to code to add yourself to the People page or add a photo to the Gallery. Everything below can be done from a web browser.

Regularly maintaining the site (new publications, people leaving, job postings, etc.)? See [MAINTAINING.md](MAINTAINING.md) for a quick "what do I do when" checklist instead.

## Contents

- [Adding yourself to the People page](#adding-yourself-to-the-people-page)
- [Adding photos to the Gallery](#adding-photos-to-the-gallery)
- [Updating your bio, photo, or links later](#updating-your-bio-photo-or-links-later)
- [When someone leaves the lab](#when-someone-leaves-the-lab)
- [Posting or hiding job/PhD opportunities](#posting-or-hiding-jobphd-opportunities)
- [Common mistakes (read this if something looks wrong)](#common-mistakes-read-this-if-something-looks-wrong)
- [How changes go live](#how-changes-go-live)
- [For maintainers: project structure & local rendering](#for-maintainers-project-structure--local-rendering)

---

## Adding yourself to the People page

You'll be creating one small text file with your details. Here's how, with no software installation required:

1. Go to the [`people` folder](people/) in this repository on GitHub.
2. Click on **`template.md`** to open it, then click the **pencil/edit icon** (top right of the file view). This opens GitHub's built-in editor.
3. Click **"..."** (or use the "Copy raw file" button) and select **"Duplicate this file"** — or, if that's not available, select all the text, copy it, then go back to the `people` folder, click **Add file → Create new file**, and paste it in.
4. Name your new file `your-name.md` (lowercase, hyphens instead of spaces — e.g. `jane-smith.md`).
5. Edit the text between the two `---` lines (the "YAML header") to fill in your details — see the field guide below.
6. Below the second `---`, write a short bio (a paragraph or two is plenty). You can use `**bold**`, `*italic*`, and `[link text](https://example.com)`.
7. Scroll down, add a short message describing your change (e.g. "Add Jane Smith's profile"), and click **"Commit changes"** (choose **"Create a new branch and start a pull request"** if that option is offered — a lab admin will review and merge it; if you have direct write access you can commit straight to `main`).
8. Add your photo — see [Adding photos to the Gallery](#adding-photos-to-the-gallery) below for the drag-and-drop upload steps, but upload to the **`images/people/`** folder instead of `images/gallery/`, and use your own name for the filename (e.g. `jane-smith.jpg`).

Your profile will appear on the People page automatically once your change is merged into `main` — see [How changes go live](#how-changes-go-live).

### Field guide

Only **`name`** is strictly required — but please also fill in `role`, since that decides which section of the People page you appear in.

| Field | Required? | What to put |
|---|---|---|
| `name` | **Yes** | Your full name, e.g. `Jane Smith` |
| `role` | Strongly recommended | One of: `postdoc`, `ra`, `phd`, or `masters`. Anything else (or leaving it blank) puts you in a generic "Other" section. |
| `year_started` | Recommended | The year you started, e.g. `2024`. Used to order people within your section. |
| `vuwemail` | Optional | Your `@vuw.ac.nz` address — shows as a small mail icon next to your name. |
| `pronouns` | Optional | e.g. `she/her`, `he/him`, `they/them` |
| `photo` | Optional | Path to your photo — see below. Leave as-is to show a placeholder. |
| `links` | Optional | See below. |

**Photo path:** if you upload your photo to `images/people/jane-smith.jpg`, set `photo: images/people/jane-smith.jpg` — the path must match the uploaded file **exactly**, including the folder and the file extension (`.jpg` vs `.png` vs `.jpeg`).

**Links:** under `links:`, you can add any of `linkedin`, `orcid`, `scholar`, `researchgate`, `funding`, or a personal/project link as `link1`, `link2`, `link3`. Delete any line you don't want to use — don't leave a link with no URL after the colon.

```yaml
---
name: Jane Smith
vuwemail: jane.smith@vuw.ac.nz
pronouns: she/her
photo: images/people/jane-smith.jpg
role: phd
year_started: 2026

links:
  linkedin: https://linkedin.com/in/jane-smith
  orcid: https://orcid.org/0000-0000-0000-0000
  scholar: https://scholar.google.com/citations?user=xxxx
---

Jane is a PhD student studying marine ecology. Her research focuses on
[coral reef resilience](research.qmd). She loves diving and data.
```

A few things that will break your profile if you get them wrong — see the [common mistakes](#common-mistakes-read-this-if-something-looks-wrong) section:

- Don't remove either of the two `---` lines.
- Indent lines under `links:` with **spaces**, not the Tab key (GitHub's web editor uses spaces by default, so typing normally is fine — just don't paste in tab-indented text from Word or Excel).
- Every link needs something after the colon. If you're not using a link, delete the whole line rather than leaving it blank.

## Adding photos to the Gallery

1. Go to the [`images/gallery` folder](images/gallery/) in this repository.
2. Click **Add file → Upload files**.
3. Drag your photo in (jpg, jpeg, png, webp, or gif all work).
4. Scroll down, add a short commit message (e.g. "Add fieldwork photo"), and click **Commit changes**.

The Gallery page shows every image in that folder automatically — no other file needs editing to make it appear.

**Please also add a real caption/alt text for your photo** — this is what shows when someone hovers over (or tab-focuses) the photo, and it's also what screen readers read aloud for anyone who can't see the image, so it should actually describe what's in the photo rather than just restating the filename.

1. Open [`images/gallery/captions.yml`](images/gallery/captions.yml) and click the pencil/edit icon.
2. Add a new line in the form `your-filename.ext: "A description of the photo"`, using the *exact* filename you uploaded (including its extension).
3. Commit your change the same way as any other edit (see [How changes go live](#how-changes-go-live)).

For example:

```yaml
rov-deployment-fiordland.jpg: "Deploying the ROV from the deck of RV Coastal during a Fiordland survey"
```

Any photo not listed in `captions.yml` just falls back to a caption generated from its filename (dashes/underscores become spaces), which is a fine placeholder but not a substitute for a real description.

**If a photo needs a credit** (e.g. it was taken by a lab member who wants attribution), use the longer form instead of a plain string, with both a `caption` and a `credit`:

```yaml
rov-deployment-fiordland.jpg:
  caption: "Deploying the ROV from the deck of RV Coastal during a Fiordland survey"
  credit: "Photo: Jane Smith"
```

The credit shows as a small permanent label in the corner of the photo (not just on hover, since the point is that it's actually visible), separate from the caption.

## Updating your bio, photo, or links later

1. Go to your file in the [`people` folder](people/) and click the pencil/edit icon.
2. Make your changes and commit them (same as step 7 above).
3. To replace your photo, upload the new file to `images/people/` (step 8 above) — if you're keeping the same filename, GitHub will ask if you want to replace the existing file.

## When someone leaves the lab

1. Move their file from `people/` into `people/past/` (open the file, use the "..." menu → "Move file", or delete-and-recreate in the new location).
2. Add a `year_end` field to their YAML header with the year they finished.
3. If they completed a PhD while in the lab, add "Dr." to the start of their `name`.

They'll move automatically from "Current Lab Members" to "Past Members" on the People page.

## Posting or hiding job/PhD opportunities

The [Opportunities page](opportunities.qmd) works a little differently, since it's mostly empty most of the time.

**To post a listing:** edit `opportunities.qmd`, copy the example listing block under "Current Opportunities", and fill in your own title, closing date, description, and how to apply.

**To hide the page's listings** (e.g. there's nothing open right now): change `show: true` to `show: false` in the YAML header at the very top of `opportunities.qmd`, and save. The page stays up with a friendly "check back soon" message instead of a broken or empty-looking page — nobody hits a dead nav link. Set it back to `show: true` whenever you have something to advertise again.

## Common mistakes (read this if something looks wrong)

- **Photo shows as a broken image / placeholder:** the `photo:` path in your YAML almost always doesn't exactly match where the file actually is. Check the folder (`images/people/`), the filename spelling, and the extension (`.jpg` ≠ `.jpeg` ≠ `.png`) all match exactly — paths are case-sensitive.
- **Your profile doesn't show up at all:** make sure your file is directly inside `people/` (not a subfolder), ends in `.md`, and still has both `---` lines with `name:` filled in.
- **You're in the wrong section, or at the wrong place in the list:** check your `role` matches one of `postdoc`, `ra`, `phd`, `masters` exactly (lowercase), and that `year_started` is a plain number.
- **A link icon doesn't show up:** make sure there's a real URL after the colon (starting with `https://`) and that the line isn't commented out with a `#` at the start.
- **Change isn't showing on the live site yet:** see [How changes go live](#how-changes-go-live) below — it takes a minute or two after your commit is on `main`.

If something still looks wrong after checking the above, open an issue on this repository or ask a lab member with GitHub experience to take a look.

## How changes go live

Once your change is committed to the `main` branch (either directly, or via a pull request that's been merged), GitHub automatically rebuilds and republishes the whole site — nobody needs to run anything manually. This usually takes 1–2 minutes. You can check progress under the **Actions** tab of this repository; a green check means it's live, a red cross means something needs fixing (see below).

## For maintainers: project structure & local rendering

- **index.qmd**: Homepage
- **people.qmd**: Renders the People page from everything in `people/`
- **research.qmd**: Projects and publications (publications are pulled from `publications.bib`)
- **media.qmd**: News and media appearances
- **gallery.qmd**: Renders the Gallery page from everything in `images/gallery/`
- **opportunities.qmd**: Job/PhD listings; content is skipped in favor of a placeholder when its `show:` field is `false`
- **contact.qmd**: Contact and involvement information
- **people/**: One markdown file per current lab member (see `template.md`); `people/past/` holds alumni
- **images/**: Photos and other images used on the site
- **styles/**: Custom CSS and SCSS for site styling
- **_site/**: Generated site output (not tracked in git; rebuilt by `quarto render` and published by CI)
- **.github/workflows/quarto-publish.yml**: the GitHub Actions workflow that renders and publishes the site on every push to `main`

If a build fails (red cross in the **Actions** tab), click into the failed run and open the "Render site" step to see the error — R package installation issues are the most common cause, since the workflow installs R packages fresh on every run.

To preview changes locally before pushing, install [Quarto](https://quarto.org/docs/get-started/) and R with the `yaml`, `stringr`, `knitr`, and `rmarkdown` packages, then run:

```shell
quarto render
```

The rendered site will appear in the `_site/` folder — open `_site/index.html` in a browser to preview it.

## Image Copyright & License

All photos and images in this repository and on the MEEM Lab website are © 2026 MEEM Lab, Victoria University of Wellington. All rights reserved. Unauthorized use, reproduction, or distribution is strictly prohibited unless explicit written permission is granted by the lab.
