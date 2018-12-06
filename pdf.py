import PyPDF2

pdf_file = open('redes_de_computadoras-freelibros-org(1).pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(93)
page_content = page.extractText()
print(page_content.encode('utf-8'))
