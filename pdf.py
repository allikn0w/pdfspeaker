#!/usr/bin/env python3

import PyPDF2

with open('redes_de_computadoras-freelibros-org(1).pdf','rb') as f:
  pdf = PyPDF2.PdfFileReader(f)

  page = pdf.getPage(34)
  print(page)
  print('Page type: {}'.format(str(type(page))))

  text = page.extractText()
  print(text)
