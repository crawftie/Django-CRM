import mysql.connector

# Database Config
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'James_Raynor2!'
)

# create cursor Object
cursorObject = dataBase.cursor()

# create Database
cursorObject.execute("CREATE DATABASE SDA")

print("Database Created Successfully")