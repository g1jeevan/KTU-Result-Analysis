import PyPDF2
import os
import copy
import re
import psycopg2

os.chdir('c:\\pypro')
collegename='FIT'
pdffile=open('resulttkmbtech.pdf','rb')
reader = PyPDF2.PdfFileReader(pdffile)
nofpages = reader.numPages
a=''
for i in range(nofpages):
 page = reader.getPage(i)
 a = a + page.extractText()
a
#b=a.split("(Grade)")
#b[0]
#b[1]
#c=b[1]
#c
