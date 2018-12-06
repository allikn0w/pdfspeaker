#!/usr/bin/env python3

import pdftotext

with open("Tests/Informe.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# Iterate over all the pages
for page in pdf:
    print(page)

# Read the first page.
print(pdf[1])
