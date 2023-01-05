# documentation = 'https://pythonhosted.org/PyPDF2/index.html'
import PyPDF2
pdf = PyPDF2.PdfFileReader('python textbook.pdf')
# print(pdf.getDocumentInfo())
# print(pdf.getNumPages())
# print(pdf.getPage(10))
# print(pdf.getPage(9).extractText())
# print(pdf.getPage(9).getContents())