import lxml
import bs4 as bs
import urllib.request
import requests
import os
import webbrowser

def doit():
 source = urllib.request.urlopen('https://ktu.edu.in/eu/res/viewResults.htm').read()
 soup = bs.BeautifulSoup(source,'lxml')

 print(soup.title)
 print(soup.title.name)
 print(soup.title.string)


 lol=soup.find_all("a",string=" MCA Regular S3 Examination Dec 2017 (S3 Result) ")
 print('::::LIST::::')
 print(lol)

 print('::::STRING::::')

 lol2=str(lol)
 print(lol2)


 lol3 = lol2[lol2.find('"')+1:lol2.find('>')-1]
 print('::::Without KTU::::')
 print(lol3)
 lol3="https://ktu.edu.in"+lol3
 print('::::With KTU::::')
 print(lol3)
 lol3=lol3.replace('amp;','')
 print('::::With KTU & Removed "amp;"::::')
 print(lol3)

 source = urllib.request.urlopen(lol3).read()
 soup = bs.BeautifulSoup(source,'lxml')
 data = soup.findAll('div',attrs={'class':'c-details'})
 lolall=[]		 
 for div in data:
  links = div.findAll('a')
  for a in links:
   lolall.append(a['href'])

 for i in range(len(lolall)):
     print('::::Without KTU::::')
     print(lolall[i])
     temp=str(lolall[i])
     temp='https://ktu.edu.in'+temp
     lolall[i]=temp
     #lolall[i]=["https://ktu.edu.in"].append(lolall[i])
     print('::::With KTU::::')
     print(lolall[i])

 os.chdir('c:\\pypro')
 #from urllib.request import urlopen
 #from os.path import basename
 #from urllib.request import urlopen

 s3collegename=['dec2017mcas3result_AJC.pdf','dec2017mcas3result_AWH.pdf','dec2017mcas3result_TVE.pdf','dec2017mcas3result_VDA.pdf','dec2017mcas3result_FIT.pdf','dec2017mcas3result_TCR.pdf','dec2017mcas3result_LMC.pdf','dec2017mcas3result_MAC.pdf','dec2017mcas3result_MES.pdf','dec2017mcas3result_MCT.pdf','dec2017mcas3result_NCE.pdf','dec2017mcas3result_KTE.pdf','dec2017mcas3result_MGP.pdf','dec2017mcas3result_SCM.pdf','dec2017mcas3result_SNG.pdf','dec2017mcas3result_SJC.pdf','dec2017mcas3result_TKM.pdf','dec2017mcas3result_VAS.pdf']
 for i in range(len(lolall)):
  #webbrowser.open_new_tab(lolall[i])
  #response = urlopen(lolall[i])
  #print(basename(response.url))
   r=requests.get(lolall[i],stream = True)
   with open("C:\\pypro\\"+str(s3collegename[i]),"wb")as pdf:
    for chunk in r.iter_content(chunk_size=1024):
     if chunk:
      pdf.write(chunk)
