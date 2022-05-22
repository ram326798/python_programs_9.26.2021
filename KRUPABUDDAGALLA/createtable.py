import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="mydatabase"
)
mycursor=mydb.cursor()
"""
mycursor.execute("CREATE TABLE Customers( name VARCHAR(255),Address VARCHAR(255))")
"""
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

