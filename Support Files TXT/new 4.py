k=0

for i in range(len(c)):
	k=c.find(')L',k) or c.find(')T',k)
	c=c[:k+11]+' # '+c[(len(c)-(k+1)):]
	print(k)
	i=k+1+
	
	
	# Splitted Results
	for i in range(50):
	print(c1[i])
	print('\n')
	
	
	k=0
	c2=c1
	for i in range(len(c2)):
		print('\n old Len : '+len(c2[i]))
		k=c2[i].find('RLMCA201')
		c2[i]=c2[:k+1]+' # '+c2[(len(c2[i])-(k+1)):]
		print('\n new Len : '+len(c2[i]))
		
		
		****** Edited *****
		
	for i in range(len(c2)):
	print('\n old Len : '+str(len(c2[i])))
	k=c2[i].find('RLMCA201')
	c2[i]=c2[i][:k]+'_#_'+c2[i][(len(c2[i])-(k)):]
	print('\n new Len : '+str(len(c2[i])))
	
	********** COrrect Split *********
	
	for i in range(len(c2)):
	print('\n old Len : '+str(len(c2[i])))
	k=c2[i].find('RLMCA201')
	print("\n K = : ",k)
	print("\n"+c2[i])
	c2[i]=c2[i][:k]+' # '+c2[i][k-(len(c2[i])):]
	print("\n"+c2[i])
	print('\n new Len : '+str(len(c2[i])))
	
	