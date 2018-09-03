import PyPDF2
import os
import copy
import re
os.chdir('c:\\pypro')
pdffile=open('result.pdf','rb')
reader = PyPDF2.PdfFileReader(pdffile)
reader.numPages
nofpages = reader.numPages
a=''
for i in range(nofpages):
	page = reader.getPage(i)
	a = a + page.extractText()
a
b=a.split("(Grade)")
b
b[0]
b[1]
c=b[1]
c
c1 = c.split('TKM16MCA')
c2=c1
c3=c1
for i in range(len(c2)):
	print('\n old Len : '+str(len(c2[i])))
	k=c2[i].find('RLMCA201')
	print("\n K = : ",k)
	print("\n"+c2[i])
	c2[i]=c2[i][:k]+' , '+c2[i][k-(len(c2[i])):]
	print("\n"+c2[i])
	print('\n new Len : '+str(len(c2[i])))
m=0
roll = {}
#demoroll=[]
rlmca201 = []
#rlmca201.append([])
rlmca203 = []
#rlmca203.append([])
rlmca205 = []
#rlmca205.append([])
rlmca207 = []
#rlmca207.append([])
rlmca209 = []
#rlmca209.append([])
rlmca231 = []
#rlmca231.append([])
rlmca233 = []
#rlmca233.append([])
fg=0

print('FFFFFFFFFFFFFFFFFFFOOOOOOOOOOORRRRRRRRRR')
for i in range(1,len(c2)):
 print('LENNNNNN : ',(len(c2)))
 roll[m]=copy.copy(int(re.search(r'\d+', c2[i]).group()))

 #demoroll.append(([int(s) for s in c2[i].split() if s.isdigit()]))
 #print(demoroll)
 #roll=demoroll[m]
 #roll=roll[[roll.find('[')+1,roll.find(']')]]
 #print(demoroll[m])
 
 print('*********')
 print(roll[m])
 splitsub = c2[i].split(',')

 for j in range(len(splitsub)):
  print(splitsub[j])
  fg=splitsub[j][splitsub[j].find('(')+1:splitsub[j].find(')')]
  print(fg)

  if j==1:

   if i==1:
     rlmca201.append(fg)
   elif i!=1:
     rlmca201.append(fg)

  elif j==2:
   rlmca203.append(fg)
  elif j==3:
   rlmca205.append(fg)
  elif j==4:
   rlmca207.append(fg)
  elif j==5:
   rlmca209.append(fg)
  elif j==6:
   rlmca231.append(fg)
  elif j==7:
   rlmca233.append(fg)
  else:
   print('finish')
 m=m+1
i=0
for i in range(len(roll)):

 print('ROll Number : ',roll[i])
 print('  ',rlmca201[i],'  ',rlmca203[i],'  ',rlmca205[i],'  ',rlmca207[i],'  ',rlmca209[i],'  ',rlmca231[i],'  ',rlmca233[i])


def bubblesortgrade(roll,rlmca201,rlmca203,rlmca205,rlmca207,rlmca209,rlmca231,rlmca233):

 n = len(roll)
 
 # Traverse through all array elements
 for i in range(n):
 
  # Last i elements are already in place
  for j in range(0, n-i-1):
 
   if roll[j] > roll[j+1] :
    roll[j], roll[j+1] = roll[j+1], roll[j]
    rlmca201[j],rlmca201[j+1] = rlmca201[j+1], rlmca201[j]
    rlmca203[j],rlmca203[j+1] = rlmca203[j+1], rlmca203[j]   
    rlmca205[j],rlmca205[j+1] = rlmca205[j+1], rlmca205[j]
    rlmca207[j],rlmca207[j+1] = rlmca207[j+1], rlmca207[j]
    rlmca209[j],rlmca209[j+1] = rlmca209[j+1], rlmca209[j]
    rlmca231[j],rlmca231[j+1] = rlmca231[j+1], rlmca231[j]
    rlmca233[j],rlmca233[j+1] = rlmca233[j+1], rlmca233[j]

bubblesortgrade(roll,rlmca201,rlmca203,rlmca205,rlmca207,rlmca209,rlmca231,rlmca233)
print('')
print('')
print('*********************************************')
print('************After Bubble sort :**************')
print('*********************************************')
for i in range(len(roll)):

 print('ROll Number : ',roll[i])
 print('  ',rlmca201[i],'  ',rlmca203[i],'  ',rlmca205[i],'  ',rlmca207[i],'  ',rlmca209[i],'  ',rlmca231[i],'  ',rlmca233[i])
 
