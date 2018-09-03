demo
'037 # RLMCA201(B), RLMCA203(B+), RLMCA205(B), RLMCA207(B), RLMCA209(B+), RLMCA231(O),RLMCA233(O)L'
>>> demo2=demo[(demo.find('RLMCA201'):demo.find(')')]
	       
SyntaxError: invalid syntax
>>> demo2=demo[(demo.find('RLMCA201')):(demo.find(')'))]
	       
>>> demo2
	       
'RLMCA201(B'
>>> demo2=demo[(demo.find('RLMCA201(')+9):(demo.find(')'))]
	       
>>> demo2
	       
'B'
>>> demo3=demo[(demo.find('RLMCA203(')+9):(demo.find(')'))]
	       
>>> demo4=demo[(demo.find('RLMCA205(')+9):(demo.find(')'))]
	       
>>> demo5=demo[(demo.find('RLMCA207(')+9):(demo.find(')'))]
	       
>>> demo6=demo[(demo.find('RLMCA209(')+9):(demo.find(')'))]
demo7=demo[(demo.find('RLMCA231(')+9):(demo.find(')'))]
demo8=demo[(demo.find('RLMCA233(')+9):(demo.find(')'))]
	       
SyntaxError: multiple statements found while compiling a single statement
>>> demo6=demo[(demo.find('RLMCA209(')+9):(demo.find(')'))]
	       demo7=demo[(demo.find('RLMCA231(')+9):(demo.find(')'))]demo8=demo[(demo.find('RLMCA233(')+9):(demo.find(')'))]
	       
SyntaxError: multiple statements found while compiling a single statement
>>> demo6=demo[(demo.find('RLMCA209(')+9):(demo.find(')'))]
	       
>>> demo7=demo[(demo.find('RLMCA231(')+9):(demo.find(')'))]
	       
>>> demo8=demo[(demo.find('RLMCA233(')+9):(demo.find(')'))]
	       
>>> print(demo1+' -> '+demo2+' -> '+demo3+' -> '+demo4+' -> '+demo5+' -> '+demo6+' -> '+demo7+' -> '+demo8)
	       
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(demo1+' -> '+demo2+' -> '+demo3+' -> '+demo4+' -> '+demo5+' -> '+demo6+' -> '+demo7+' -> '+demo8)
TypeError: can only concatenate list (not "str") to list
>>> print(str(demo1)+' -> '+demo2+' -> '+demo3+' -> '+demo4+' -> '+demo5+' -> '+demo6+' -> '+demo7+' -> '+demo8)
	       
[37] -> B ->  ->  ->  ->  ->  -> 
>>> demo3
	       
''
>>> demo3=demo[(demo.find('RLMCA203(')+9):((demo.find('RLMCA201(')+9)+(demo.find(')')))]
	       
>>> demo3
	       
'B+)'
>>> demo3=demo[(demo.find('RLMCA203(')+9):(9+(demo.find(')')))]
	       
>>> demo3
	       
''
>>> demo3=demo[(demo.find('RLMCA203(')+9):((demo.find('RLMCA201(')+8)+(demo.find(')')))]
	       
>>> demo3
	       
'B+'
>>> demo4=demo[(demo.find('RLMCA205(')+9):((demo.find('RLMCA203(')+8)+(demo.find(')')))]
	       
>>> demo4
	       
'B'
>>> demo5=demo[(demo.find('RLMCA206(')+9):((demo.find('RLMCA205(')+8)+(demo.find(')')))]
	       
>>> demo5
	       
'MCA201(B), RLMCA203(B+), RLMCA205(B), RLMCA207(B)'
>>> demo5=demo[(demo.find('RLMCA207(')+9):((demo.find('RLMCA205(')+8)+(demo.find(')')))]
	       
>>> demo5
	       
'B)'



for i in range(len(demosplit)):
	print(demosplit[i])
	fg=demosplit[i][demosplit[i].find('(')+1:demosplit[i].find(')')]
	if i==0:
	       demo2=fg
	elif i==1:
	       demo3=fg
	elif i==2:
	       demo4=fg
	elif i==3:
	       demo5=fg
	elif i==4:
	       demo6=fg
	elif i==5:
	       demo7=fg
	elif i==6:
	       demo8=fg
	else:
	       print('finish')

	       
037 # RLMCA201(B)
 RLMCA203(B+)
 RLMCA205(B)
 RLMCA207(B)
 RLMCA209(B+)
 RLMCA231(O)
RLMCA233(O)L
>>> print(str(demo1)+' -> '+demo2+' -> '+demo3+' -> '+demo4+' -> '+demo5+' -> '+demo6+' -> '+demo7+' -> '+demo8)
	       
[37] -> B -> B+ -> B -> B -> B+ -> O -> O