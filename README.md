# gabrielpfritsch.com

Personal academic site. Plain static HTML + CSS, served by GitHub Pages at
`gabrielpfritsch.com` (see `CNAME`). No build step is required to deploy.

## Layout

```
_head.part, _foot.part   shared page chrome
_body/*.html             the content of each page — edit these
build.py                 regenerates the four pages from the parts above
index.html               generated — do not edit directly
research/, teaching/, writing/, 404.html
favicon.svg, robots.txt, sitemap.xml
assets/css/style.css     the whole stylesheet
assets/img/              portrait
files/                   paper PDFs and CV
files/gs/                Goldman Sachs research reports
cv/cv.tex                CV source, moved off Overleaf
cv/build.sh              builds it and installs files/cv.pdf
```

## The CV

`cv/cv.tex` is the source of truth. `files/cv.pdf` is a build artefact, committed
so GitHub Pages can serve it. After editing the source:

```sh
./cv/build.sh
```

Commit the `.tex` and the regenerated `files/cv.pdf` together, or the published
PDF drifts from its source.

## Editing

Edit the relevant file in `_body/`, then:

```sh
python3 build.py
```

Commit both the `_body/` change and the regenerated HTML. Pushing to `main`
publishes within a minute or so.

To preview locally:

```sh
python3 -m http.server 4711
```

## Design notes

- Typeface is EB Garamond, loaded from Google Fonts. Worth self-hosting the
  woff2 subsets eventually to drop the third-party request.
- Colours are CSS custom properties at the top of `style.css`. Dark mode is a
  `prefers-color-scheme` media query — there is no toggle.
- Abstracts use `<details>`; no JavaScript anywhere on the site.
- `sitemap.xml` is hand-maintained. Add an entry when you add a page.
