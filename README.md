
# MEEM Lab Website

This repository contains the Quarto-based website for the MEEM Lab at Victoria University of Wellington.

## Project Structure

- **index.qmd**: Homepage
- **people.qmd**: Lab members and bios
- **research.qmd**: Projects and publications
- **media.qmd**: News and media appearances
- **contact.qmd**: Contact and involvement information
- **people/**: Individual Markdown files for each lab member
- **images/**: Photos and other images used on the site
- **styles/**: Custom CSS and SCSS for site styling
- **_extensions/**: Custom Quarto Lua filters/extensions (e.g., for people profiles)
- **_site/**: Generated site output (do not edit directly)

## Editing Content

### Adding Yourself to the People Page

1. Copy the template below into a new file in the `people/` folder (e.g. `people/your-name.md`).
2. Fill in your details and save the file.
3. Add your photo to the `images/` folder. Your profile will appear automatically on the People page after the site is rebuilt.

Example front matter:

```yaml
---
name: Your Name
pronouns: your pronouns
photo: images/your-photo.jpg
profile-link: https://www.linkedin.com/in/your-linkedin
---

Your bio goes here. You can use markdown! Please bold your role (e.g. **PhD Student**) within the text of your bio.
```