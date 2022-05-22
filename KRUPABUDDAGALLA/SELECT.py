import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="thatsbydb"
)
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM beneficiaries")
myresult=mycursor.fetchall()
 
for x in myresult:
     print(x)