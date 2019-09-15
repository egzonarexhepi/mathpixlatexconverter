# Mathpix Latex Expansion

## Docs 

Created for Hophacks Fall 2019.

The purpose of this repo is to fulfill the Mathpix challenge to expand mathpix snip technology. Mathpix snip is a technology which processes handwritten or digitally printed advanced mathematical expressions and extracts Latex code from them. This process expands on mathpix snip technology to process larger data sets, like whole pages or several pages, rather than just a few lines which must be manually cropped (the current working stage of mathpix snip).

This project was created using publicly available APIs and Mathpix API found here: http://docs.mathpix.com

This application was built using Flask and Vue.js frameworks to showcase our Mathpix challenge. The Mathpix challenge was solved using a Google Cloud Vision Machine Learning API, OCR, which allowed us to detect text in any pdf and find the bounds of text for optimal cropping. So, larger data sets are deconstructed using OCR, processed by existing Mathpix technology, and then the extracted LaTeX code is reconstructed.
