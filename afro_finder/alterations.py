import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "scholarship"
)

cursor = db.cursor()

query = """
         DROP TABLE scholarships;
       """

resultset = cursor.execute(query)

print(resultset)