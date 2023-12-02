import mysql.connector 
from mysql.connector import Error

connection = mysql.connector.connect(host="localhost,
                                     user="root",
                                     passwd="Basecode!257s",
                                     db="pysports")

try:
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("select database();")
        db = cursor.fetchone()
        print("You are connected to database: ", db)
except Error as e:
    print("Error while connecting to MYSQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MYSQL connection is closed")
                            