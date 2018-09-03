INSERT INTO s3 (rollno, rlmca201, rlmca203, rlmca205, rlmca207, rlmca209, rlmca231, rlmca233) VALUES (%s,%s, %s,%s,%s,%s,%s, %s)

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"

sql = "INSERT INTO s3 (rollno, rlmca201, rlmca203, rlmca205, rlmca207, rlmca209, rlmca231, rlmca233) VALUES (%s,%s, %s,%s,%s,%s,%s, %s)"

val = (roll, rlmca201[1], rlmca203[1], rlmca205[1], rlmca207[1], rlmca209[1], rlmca231[1], rlmca233[1])

for row in zip(roll, rlmca201, rlmca203, rlmca205, rlmca207, rlmca209, rlmca231, rlmca233):
val=row
mycursor.execute(sql, val)



++++ pip install mysql-python
