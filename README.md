
# MEEM Lab Website

This repository contains the Quarto-based website for the MEEM Lab at Victoria University of Wellington.

## Project Structure

- **index.qmd**: Homepage
- **people.qmd**: Lab members and bios
- **research.qmd**: Projects and publications
- **media.qmd**: News and media appearances
- **gallery.qmd**: Lab photo gallery
- **contact.qmd**: Contact and involvement information
- **people/**: Individual Markdown files for each lab member
- **images/**: Photos and other images used on the site
- **styles/**: Custom CSS and SCSS for site styling
- **_site/**: Generated site output (not tracked in git; rebuilt by `quarto render` and published by CI)

## Image Copyright & License

All photos and images in this repository and on the MEEM Lab website are © 2026 MEEM Lab, Victoria University of Wellington. All rights reserved. Unauthorized use, reproduction, or distribution is strictly prohibited unless explicit written permission is granted by the lab.

## Editing Content

### Adding Images to the Gallery

1. Place your image files in the `images/gallery/` folder. Supported formats: jpg, jpeg, png, webp, gif.
2. The gallery page (`gallery.qmd`) will automatically display all images in this folder, using the filename (without extension) as the caption.
3. To update or remove an image, simply add, replace, or delete the file in `images/gallery/`.

### Adding Yourself to the People Page

1. Copy the template from `people/template.md` into a new file in the `people/` folder (e.g. `people/your-name.md`).
2. Fill in your details in the YAML header and write your bio below. All fields are optional except `name`.
3. Add your photo to the `images/people/` folder and reference it in your YAML (e.g. `photo: images/people/your-photo.jpg`).
4. Add any relevant links (LinkedIn, ORCID, Google Scholar, etc.) in the `links` section.
5. Your profile will appear automatically on the People page after the site is rebuilt.

#### Example YAML front matter:
```yaml
---
name: Your Name
vuwemail: firstname.lastname@vuw.ac.nz
pronouns: your pronouns
photo: images/people/your-photo.jpg
role: phd
year_started: 2026
links:
	linkedin: https://linkedin.com/in/your-linkedin
	orcid: https://orcid.org/0000-0000-0000-0000
	scholar: https://scholar.google.com/citations?user=xxxx
---
Your bio goes here. You can use markdown! Please bold your role (e.g. **PhD Student**) within the text of your bio.
```

### Updating or Removing Lab Members

1. When someone leaves the lab, move their markdown file to the `people/past/` folder.
2. Add a `year_end` field to the YAML header with the year they finished.
3. If they completed a PhD, add 'Dr.' to the start of their name.
4. Past members will be listed automatically in the "Past Members" section.

### Editing Bios or Photos

1. To update your bio or photo, edit your markdown file in the `people/` folder and update the YAML or bio text.
2. Replace your photo in the `images/people/` folder if needed.

### Rebuilding the Site

After making changes, rebuild the site using Quarto:

```shell
quarto render
```

The updated site will appear in the `_site/` folder.