import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="mydatabase"
)
mycursor=mydb.cursor()

mycursor.execute("ALTER TABLE Customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

