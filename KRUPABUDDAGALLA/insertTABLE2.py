import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="thatsmydb"
)
mycursor=mydb.cursor()
sql="INSERT INTO beneficiaries(name,address) values(%s,%s)"
val=[
    ("akshay","kadapa"),
    ("krupa","kadapa"),
    ("shiny","nandyal"),
    ("richie","vijayawada"),
    ("honey","kadapa")
    ]
mycursor.executemany(sql,val)

mydb.commit()
print(mycursor.rowcount,"record inserted")