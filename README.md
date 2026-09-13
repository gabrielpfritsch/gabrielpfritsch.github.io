# gabrielpfritsch.com

The source for my personal site: research, teaching, and a CV.

Plain HTML and CSS, no JavaScript beyond a light/dark toggle, served by
GitHub Pages.

## Building

Page content lives in `_body/`. After editing it, regenerate the pages:

```sh
python3 build.py
```

The CV is written in LaTeX in `cv/`. To rebuild it and update the copy the
site serves:

```sh
./cv/build.sh
```

To preview locally:

```sh
python3 -m http.server 4711
```

## Reuse

Feel free to borrow the layout or the stylesheet. Please don't reuse my
photo, CV, or papers.
