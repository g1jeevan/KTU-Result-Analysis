
>>> import mysql.connector
>>> mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mcatest"
)
>>> print(mydb)
<mysql.connector.connection.MySQLConnection object at 0x000002E49C52E630>

>>> mycursor = mydb.cursor()
>>> sql = "INSERT INTO s3 (rollno, rlmca201, rlmca203, rlmca205, rlmca207, rlmca209, rlmca231, rlmca233) VALUES (%s,%s, %s,%s,%s,%s,%s, %s)"


1=roll[0]
>>> w2=rlmca201[0]
>>> w2
'B'
>>> w3=rlmca203[0]
>>> w4=rlmca205[0]
>>> w5=rlmca207[0]
>>> w6=rlmca209[0]
>>> w7=rlmca231[0]
>>> w8=rlmca233[0]
>>> w1
[37]
>>> w2
'B'
>>> w3
'B+'
>>> w4
'B'
>>> w5
'B'
>>> w6
'B+'
>>> w7
'O'
>>> w8
'O'
>>> val = (roll,w1,w2,w3,w4,w5,w6,w7,w8)
>>> mycursor.execute(sql, val)
Traceback (most recent call last):
  File "C:\Users\Jeevan Jacob\AppData\Local\Programs\Python\Python37\lib\site-packages\mysql\connector\conversion.py", line 179, in to_mysql
    return getattr(self, "_{0}_to_mysql".format(type_name))(value)
AttributeError: 'MySQLConverter' object has no attribute '_list_to_mysql'


>>> val=(12,'JJ','JJ','JJ','JJ','JJ','JJ','JJ')
>>> mycursor.execute(sql, val)
>>> mydb.commit()

>>> r1=''.join(str(roll[0]))
>>> val=(r1,'JJ','JJ','JJ','JJ','JJ','JJ','JJ')
>>> mycursor.execute(sql, val)
>>> mydb.commit()
>>> r1
'[37]'
>>> val=(int(r1),'JJ','JJ','JJ','JJ','JJ','JJ','JJ')
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    val=(int(r1),'JJ','JJ','JJ','JJ','JJ','JJ','JJ')
ValueError: invalid literal for int() with base 10: '[37]'
>>> val=(1,r1,'JJ','JJ','JJ','JJ','JJ','JJ')
>>> mycursor.execute(sql, val)
>>> mydb.commit()
>>> r1
'[37]'
>>> int(r1)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    int(r1)
ValueError: invalid literal for int() with base 10: '[37]'
>>> r1=str(roll[0])
>>> r1
'[37]'
>>> roll(0)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    roll(0)
TypeError: 'list' object is not callable
>>> roll[0]
[37]


