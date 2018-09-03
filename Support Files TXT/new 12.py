import requests

 r=requests.get("https://ktu.edu.in"+lolall[0])
		  
>>> "https://ktu.edu.in"+lolall[0]
		  
'https://ktu.edu.in/eu/att/attachments.htm?download=file&id=CbL6Ed3Unr4xaYWZ9Jh6qMeEtgX7c6bWORqQOOcr1Ac%3D'
>>> r=requests.get("https://ktu.edu.in"+lolall[0],stream = True)
		  
>>> r
		  
<Response [200]>
>>> with open("Python.pdf","wb")as pdf:
		  for chunk in r.iter_content(chunk_size=1024):
		   if chunk:
		    pdf.write(chunk)

		  
1024
1024
1024
1024
1024
1024
1024
1024
885
>>> with open("C:\\pypro\\Python.pdf","wb")as pdf:
		  for chunk in r.iter_content(chunk_size=1024):
		   if chunk:
		    pdf.write(chunk)

		  
Traceback (most recent call last):
  File "<pyshell#99>", line 2, in <module>
    for chunk in r.iter_content(chunk_size=1024):
  File "C:\Users\Jeevan Jacob\AppData\Local\Programs\Python\Python37\lib\site-packages\requests\models.py", line 768, in iter_content
    raise StreamConsumedError()
requests.exceptions.StreamConsumedError
>>> os.chdir('c:\\pypro')
		  
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    os.chdir('c:\\pypro')
NameError: name 'os' is not defined
>>> import os
		  
>>> os.chdir('c:\\pypro')
		  
>>> r=requests.get("https://ktu.edu.in"+lolall[0],stream = True)
		  
>>> with open("C:\\pypro\\Python.pdf","wb")as pdf:
		  for chunk in r.iter_content(chunk_size=1024):
		   if chunk:
		    pdf.write(chunk)

		  
1024
1024
1024
1024
1024
1024
1024
1024
885
>>> 