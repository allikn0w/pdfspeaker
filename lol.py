import textract


text = textract.process(
  'redes_de_computadoras-freelibros-org(1).pdf',
  method='pdfminer'
)

print(text)
