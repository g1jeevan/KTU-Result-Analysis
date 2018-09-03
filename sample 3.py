import PyPDF2
import os
os.chdir('c:\\pypro')
pdffile=open('result.pdf','rb')
reader = PyPDF2.PdfFileReader(pdffile)
reader.numPages
page = reader.getPage(0)
page.extractText()


for in range(0,)

nofpages=reader.numPages

for in range(0,nofpages)

for i in range(0,nofpages):
page = reader.getPage(i)
a = a+page1.extractText()

b=sring.split("(Grade)")

