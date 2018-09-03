import PyPDF2
import os
import copy
import re
import psycopg2
import tabula as tbl
import tabulate as tblt

def doit():
 k=[]
 os.chdir('c:\\pypro')
 collegename='AJC'
 #pdffile=open('dec2017mcas3result_'+collegename+'.pdf','rb')
 #df=read_pdf('dec2017mcas3result_'+collegename+'.pdf')
 file ='resulttkmbtech.pdf'
 #tbl.convert_into(file,"test.json",pages="all",output_format="json")
 df = tbl.read_pdf(file, output_format='json',pages='all')
 #print(tblt.tabulate(df,headers='keys',tablefmt='psql'))
 print(df)
 k=df
 print(k)
doit()
