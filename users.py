from sql_connect import connect_database
from sql_connect import Error

class Users:
    def __init__(self):
        self.users = {}
 
    def add_user(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                user_id = int(input("What is the user id?: "))
                name = input("What is user's name?: ")
                libID = input("What is user's id number?: ")
                query = "INSERT INTO users Values (%s, %s, %s)"
                values = user_id, name, libID
                cursor.execute(query, values)
                conn.commit()
                print("User added succesfully")
            finally:
                cursor.close()
                conn.close()
                
        
    def search_users(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                user = input("What is the name of the user you're searching for?")
                query = "SELECT %s from users"
                cursor.execute(query, user)
                conn.commit()
                for row in cursor.fetchall():
                    print(row)
            except Error:
                print({Error})
            finally:
                cursor.close()
                conn.close()

    def display_users(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor(buffered = True)
                query = "SELECT * from users"
                cursor.execute(query)
                conn.commit()
                for row in cursor.fetchall():
                    print(row)
            except Error as e:
                print({e})
            finally:
                cursor.close()
                conn.close()

