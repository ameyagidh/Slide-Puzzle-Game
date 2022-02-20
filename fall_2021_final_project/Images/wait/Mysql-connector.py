import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd="asggb222"
    )
print(mydb)

mycursor = mydb.cursor()
# Just runn this once
#mycursor.execute("CREATE database testdb")

mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)