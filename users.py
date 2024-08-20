from sql_connect import connect_database

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
        user = input("What is the name of the user you're searching for?")
        if user in self.books:
            print(self.users[user])

    def display_users(self):
        for name in self.users:
            print(self.users[name])

