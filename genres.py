from sql_connect import connect_database
from sql_connect import Error

class Genres:
    def __init__(self):
        self.genres = {}

class Authors:
    def __init__(self):
        self.authors = {}
 
    def add_author(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                name = input("What is the author's name?: ")
                info = input("What is the autor's info?: ")
                id = int(input("What is author's id?"))
                query = "INSERT INTO authors (id, name, biography) Values (%s, %s, %s)"
                values = id, name, info
                cursor.execute(query, values)
                conn.commit()
                print("Author added")
            finally:
                cursor.close()
                conn.close()
                

    def search_author(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor(buffered = True)
                query = "SELECT %s from authors"
                author = input("Which author are you searching for?: ")
                cursor.execute(query, author)
                conn.commit()
                for row in cursor.fetchall():
                    print(row)
            except Error as e:
                print({e})
            finally:
                cursor.close()
                conn.close()

    def display_authors(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor(buffered = True)
                query = "SELECT * from authors"
                cursor.execute(query)
                conn.commit()
                for row in cursor.fetchall():
                    print(row)
            except Error as e:
                print({e})
            finally:
                cursor.close()
                conn.close()