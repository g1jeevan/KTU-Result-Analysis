c.count('TKM16MCA')
44
>>> c.find('TKM16MCA')
1
>>> c.find('TKM16MCA',2)
103
>>> c1 = c.split('LTKM16MCA0')
for i in range(0,9):
	c1[i]
	print('\n')

	
''


'37RLMCA201(B), RLMCA203(B+), RLMCA205(B), RLMCA207(B), RLMCA209(B+), RLMCA231(O),RLMCA233(O)'


'38RLMCA201(C), RLMCA203(B+), RLMCA205(B+), RLMCA207(B), RLMCA209(B+),RLMCA231(A+), RLMCA233(A+)'


'39RLMCA201(A), RLMCA203(A+), RLMCA205(A+), RLMCA207(A+), RLMCA209(A),RLMCA231(O), RLMCA233(O)'


'40RLMCA201(B), RLMCA203(B+), RLMCA205(B+), RLMCA207(F), RLMCA209(B), RLMCA231(O),RLMCA233(O)'


'41RLMCA201(B), RLMCA203(B+), RLMCA205(B+), RLMCA207(B), RLMCA209(B+),RLMCA231(O), RLMCA233(A)'


'42RLMCA201(B+), RLMCA203(A), RLMCA205(B+), RLMCA207(B+), RLMCA209(B+),RLMCA231(O), RLMCA233(A+)'


'43RLMCA201(C), RLMCA203(B), RLMCA205(B), RLMCA207(B), RLMCA209(B+), RLMCA231(O),RLMCA233(O)'

 c.startswith('LTKM16')
True
>>> k='LTKM16MCA037'
>>> k
'LTKM16MCA037'
>>> k="LTKM16MCA037"
>>> k
'LTKM16MCA037'
>>> k=10
>>> k
10
>>> k='10'
>>> k
'10'
>>> int(k)+5
15
>>> k='LTKM16MCA037'
>>> k='10'
>>> int(k)
10
>>> k
'10'
>>> k='LTKM16MCA037'
>>> c.startswith(k)
True
>>> q=0
>>> w=4
>>> c.startswith(k[0:4])
True
>>> c.startswith(k[q:w])
True
>>> def fucntion1(name):
	print(name)

	
>>> fucntion1('BABU')
BABU
>>> fucntion1(12)
12

>>> def fucntion1(name):
	print('Name' + str(name))

	
>>> fucntion1(13)
Name13
>>> h=c.startswith('LTKM16')
>>> h
True
>>> int(h)
1
>>> s1='qwerty12345'
>>> 1
1
>>> s1
'qwerty12345'
>>> s1[5]
'y'
>>> s1[5]
'y'
=
>>> lines=c.splitlines()
>>> lines

s1
'qwerty12345'


>>> s1[5:]+'-'+s1[:5]
'y12345-qwert'
>>> s1[:4]+'-'+s1[:]
'qwer-qwerty12345'
>>> s1[:4]+'-'+s1[4-(len(s1)):]
'qwer-ty12345'
>>> s1[:6]+'-'+s1[6-(len(s1)):]
'qwerty-12345'