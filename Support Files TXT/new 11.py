
import lxml
>>> import bs4 as bs
>>> import urllib.request
>>> source = urllib.request.urlopen('https://ktu.edu.in/eu/res/viewResults.htm').read()

>>> soup = bs.BeautifulSoup(source,'lxml')
>>> 
>>> 
>>> print(soup.title)
<title>APJ Abdul Kalam Technological University :: Home</title>
>>> print(soup.title.name)
title
>>> print(soup.title.string)
APJ Abdul Kalam Technological University :: Home
>>> print(soup.title.parent.name)

head
>>> for url in soup.find_all('a'):
    print(url.get('href'))

import urllib.request
source = urllib.request.urlopen('https://ktu.edu.in/eu/res/viewResults.htm').read()

>>> 
>>> soup = bs.BeautifulSoup(source,'lxml')


for div in soup.find_all('div', class_='c-details'):
    print(div.text)
	
data = soup.findAll('div',attrs={'class':'c-details'})

for div in data:
     links = div.findAll('a')
     for a in links:
	     print(" "+a['href'])
		 
		 
***************** give space between " MCA...result) "

		 
soup.find_all("a",string=" MCA Regular S3 Examination Dec 2017 (S3 Result) ")
			 
[<a href="/eu/res/viewExamResults.htm?examDefIdEnr=FXvhPiJH3xujG7QivHyFvPWkAo9IM3Kl9SUIS7s8qsE%3D&amp;type=YOFNXr1Z4hniPYIVtLovxu6JkNRJs%2FE8s75OgLYnfqs%3D&amp;publishId=PWaBXEGVp8SYLK1ThBXdReMtPiG8k0a%2BEaYi%2BEInc9U%3D"> MCA Regular S3 Examination Dec 2017 (S3 Result) </a>]
>>> lol=soup.find_all("a",string=" MCA Regular S3 Examination Dec 2017 (S3 Result) ")
			 
>>> lol['href']
			 
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    lol['href']
TypeError: list indices must be integers or slices, not str
>>> lol
			 
[<a href="/eu/res/viewExamResults.htm?examDefIdEnr=FXvhPiJH3xujG7QivHyFvPWkAo9IM3Kl9SUIS7s8qsE%3D&amp;type=YOFNXr1Z4hniPYIVtLovxu6JkNRJs%2FE8s75OgLYnfqs%3D&amp;publishId=PWaBXEGVp8SYLK1ThBXdReMtPiG8k0a%2BEaYi%2BEInc9U%3D"> MCA Regular S3 Examination Dec 2017 (S3 Result) </a>]
>>> 

lol2=str(lol)
lol3 = lol2[lol2.find('"')+1:lol2.find('>')-1]
lol3="https://ktu.edu.in"+lol3
lol3=lol3.replace
>>> lol3=lol3.replace('amp;','')
			 
>>> source = urllib.request.urlopen(lol3).read()
			 
>>> soup = bs.BeautifulSoup(source,'lxml')
			 
>>> data = soup.findAll('div',attrs={'class':'c-details'})
			 
>>> for div in data:
     links = div.findAll('a')
     for a in links:
	     print(" "+a['href'])

lolall=[]		 
for div in data:
     links = div.findAll('a')
     for a in links:
      lolall.append(a['href'])
	  
	  
	  
	  

# imported the requests library
import requests
image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
 
# URL of the image to be downloaded is defined as image_url
r = requests.get(image_url) # create HTTP response object
 
# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("python_logo.png",'wb') as f:
 
    # Saving received content as a png file in
    # binary format
 
    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(r.content)

	
	
	
	
	
	
if i==0:
  with open("C:\\pypro\\Python.pdf","wb")as pdf:
   for chunk in r.iter_content(chunk_size=1024):
     if chunk:
      pdf.write(chunk)
 elif i==1:
  with open("C:\\pypro\\Python.pdf","wb")as pdf:
   for chunk in r.iter_content(chunk_size=1024):
     if chunk:
      pdf.write(chunk)
 elif i==2:
  with open("C:\\pypro\\Python.pdf","wb")as pdf:
   for chunk in r.iter_content(chunk_size=1024):
     if chunk:
      pdf.write(chunk)
 elif i==3:
  with open("C:\\pypro\\Python.pdf","wb")as pdf:
   for chunk in r.iter_content(chunk_size=1024):
     if chunk:
      pdf.write(chunk)
 elif i==4:
  with open("C:\\pypro\\Python.pdf","wb")as pdf:
   for chunk in r.iter_content(chunk_size=1024):
     if chunk:
      pdf.write(chunk)
 elif i==5:
  with open("C:\\pypro\\Python.pdf","wb")as pdf:
   for chunk in r.iter_content(chunk_size=1024):
     if chunk:
      pdf.write(chunk)
 elif i==6:
  with open("C:\\pypro\\Python.pdf","wb")as pdf:
   for chunk in r.iter_content(chunk_size=1024):
     if chunk:
      pdf.write(chunk)
 elif i==7:
  with open("C:\\pypro\\Python.pdf","wb")as pdf:
   for chunk in r.iter_content(chunk_size=1024):
     if chunk:
      pdf.write(chunk)
 elif i==8:
  with open("C:\\pypro\\Python.pdf","wb")as pdf:
   for chunk in r.iter_content(chunk_size=1024):
     if chunk:
      pdf.write(chunk)
 elif i==9:
  with open("C:\\pypro\\Python.pdf","wb")as pdf:
   for chunk in r.iter_content(chunk_size=1024):
     if chunk:
      pdf.write(chunk)
 elif i==10:
  with open("C:\\pypro\\Python.pdf","wb")as pdf:
   for chunk in r.iter_content(chunk_size=1024):
     if chunk:
      pdf.write(chunk)
 elif i==11:
  with open("C:\\pypro\\Python.pdf","wb")as pdf:
   for chunk in r.iter_content(chunk_size=1024):
     if chunk:
      pdf.write(chunk)
 elif i==12:
  with open("C:\\pypro\\Python.pdf","wb")as pdf:
   for chunk in r.iter_content(chunk_size=1024):
     if chunk:
      pdf.write(chunk)
 elif i==13:
  with open("C:\\pypro\\Python.pdf","wb")as pdf:
   for chunk in r.iter_content(chunk_size=1024):
     if chunk:
      pdf.write(chunk)
 elif i==14:
  with open("C:\\pypro\\Python.pdf","wb")as pdf:
   for chunk in r.iter_content(chunk_size=1024):
     if chunk:
      pdf.write(chunk)
 elif i==15:
  with open("C:\\pypro\\Python.pdf","wb")as pdf:
   for chunk in r.iter_content(chunk_size=1024):
     if chunk:
      pdf.write(chunk)
 elif i==16:
  with open("C:\\pypro\\Python.pdf","wb")as pdf:
   for chunk in r.iter_content(chunk_size=1024):
     if chunk:
      pdf.write(chunk)
 elif i==17:
  with open("C:\\pypro\\Python.pdf","wb")as pdf:
   for chunk in r.iter_content(chunk_size=1024):
     if chunk:
      pdf.write(chunk)
 else:
  print('Please Check the length of the list')
	
	