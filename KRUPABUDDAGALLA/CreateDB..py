import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="thatsmydb"

)
mycursor=mydb.cursor()
mycursor.execute("ALTER TABLE beneficiaries ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
