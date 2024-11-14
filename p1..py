import mysql.connector


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="rkce"
)
c=mydb.cursor()
c.execute("create table students(sid int,sname varchar(30),smarks int)")
c.execute("insert into students values (101,'mahi',50)")
c.execute("insert into students values (102,'sonu',55)")
c.execute("insert into students values (103,'jeevi',60)")
mydb.commit()