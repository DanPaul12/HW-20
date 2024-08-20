import mysql.connector
from mysql.connector import Error

def connect_database():
    db_name = "library_db"
    user = "root"
    password = "thegoblet2"
    host = "localhost"
    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )
        print("Connection to MySQL succesful")
        return conn
    except Error:
        print("{Error}")
