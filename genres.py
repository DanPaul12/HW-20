from sql_connect import connect_database

class Genres:
    def __init__(self):
        self.genres = {}
 
    def add_genre(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                name = input("What is the genre's name?: ")
                info = input("What is the genre's description?: ")
                query = "INSERT INTO Authors Values (%s, %s)"
                values = name, info
                cursor.execute(query, values)
                conn.commit()
            finally:
                cursor.close()
                conn.close()

    def search_genres(self):
        genre = input("What is the name of the genre you're searching for?")
        if genre in self.genres:
            print(self.genres[genre])

    def display_genres(self):
        for name in self.genres:
            print(self.genres[name])


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
        author = input("What is the name of the author you're searching for?")
        if author in self.authors:
            print(self.authors[author])

    def display_authors(self):
        for name in self.authors:
            print(self.authors[name])