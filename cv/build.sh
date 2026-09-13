#!/bin/sh
# Builds cv.pdf from cv.tex and installs it as the copy the site serves.
set -e
cd "$(dirname "$0")"
latexmk -pdf -quiet cv.tex
cp cv.pdf ../files/cv.pdf
latexmk -c >/dev/null
echo "built cv/cv.pdf -> files/cv.pdf"
