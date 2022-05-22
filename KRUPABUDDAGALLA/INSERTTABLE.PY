import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="mydatabase"
)

mycursor=mydb.cursor()
sql="INSERT INTO Customers(name,address) VALUES(%s,%s)"

val=("david","kadapa")
val=("k")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted.")




