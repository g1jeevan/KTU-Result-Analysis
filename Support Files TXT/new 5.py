

037RLMCA201(B), RLMCA203(B+), RLMCA205(B), RLMCA207(B), RLMCA209(B+), RLMCA231(O),RLMCA233(O)L


demo5=demo[(demo.find('RLMCA207(')+9):(demo.find(')'))]
demo6=demo[(demo.find('RLMCA209(')+9):(demo.find(')'))]
demo7=demo[(demo.find('RLMCA231(')+9):(demo.find(')'))]
demo8=demo[(demo.find('RLMCA233(')+9):(demo.find(')'))]

m=0
roll = []
rlmca201 = []
rlmca203 = []
rlmca205 = []
rlmca207 = []
rlmca209 = []
rlmca231 = []
rlmca233 = []



m=0
roll = []
rlmca201 = []
rlmca201.append([])
rlmca203 = []
rlmca203.append([])
rlmca205 = []
rlmca205.append([])
rlmca207 = []
rlmca207.append([])
rlmca209 = []
rlmca209.append([])
rlmca231 = []
rlmca231.append([])
rlmca233 = []
rlmca233.append([])



for i in range(len(c2)):
	roll[m] = [int(s) for s in c2[i].split() if s.isdigit()]
	splitsub = c2[i].split(',')
	for j in range(len(splitsub)):
		print(splitsub[j])
		fg=splitsub[j][splitsub[j].find('(')+1:splitsub[j].find(')')]
		if j==0:
			rlmca201[m]=fg
		elif j==1:
			rlmca203[m]=fg
		elif j==2:
			rlmca205[m]=fg
		elif j==3:
			rlmca207[m]=fg
		elif j==4:
			rlmca209[m]=fg
		elif j==5:
			rlmca231[m]=fg
		elif j==6:
			rlmca233[m]=fg
		else:
	       print('finish')
	m=m+1
	********** [m:]**************
	 for i in range(len(c2)):
	roll[m:]=[int(s) for s in c2[i].split() if s.isdigit()]
	splitsub = c2[i].split(',')
	for j in range(len(splitsub)):
		print(splitsub[j])
		fg=splitsub[j][splitsub[j].find('(')+1:splitsub[j].find(')')]
		if j==0:
			rlmca201.append(fg)
		elif j==1:
			rlmca203[m:]=fg
		elif j==2:
			rlmca205[m:]=fg
		elif j==3:
			rlmca207[m:]=fg
		elif j==4:
			rlmca209[m:]=fg
		elif j==5:
			rlmca231[m:]=fg
		elif j==6:
			rlmca233.append(fg)
		else:
			print('finish')
	m=m+1

	************ Append ***********
	 for i in range(len(c2)):
	roll[m:]=[int(s) for s in c2[i].split() if s.isdigit()]
	splitsub = c2[i].split(',')
	for j in range(len(splitsub)):
		print(splitsub[j])
		fg=splitsub[j][splitsub[j].find('(')+1:splitsub[j].find(')')]
		if j==0:
			rlmca201.append(fg)
		elif j==1:
			rlmca203.append(fg)
		elif j==2:
			rlmca205.append(fg)
		elif j==3:
			rlmca207.append(fg)
		elif j==4:
			rlmca209.append(fg)
		elif j==5:
			rlmca231.append(fg)
		elif j==6:
			rlmca233.append(fg)
		else:
			print('finish')
	m=m+1

	
	
	
	
	
	for i in range(len(c2)):
	print('ROll Number : '+str(roll[i])+'  '+rlmca201[i]+'  '+rlmca203[i]+'  '+rlmca205[i]+'  '+rlmca207[i]+'  '+rlmca209[i]+'  '+rlmca231[i]+'  '+rlmca233[i])
	
	
	
	
	xxxxxx
	for i in range(len(c2)):
	print('ROll Number : '+str(roll[i]))
	print('  '+rlmca201[i]+'  '+rlmca203[i]+'  '+rlmca205[i]+'  '+rlmca207[i]+'  '+rlmca209[i]+'  '+rlmca231[i]+'  '+rlmca233[i])