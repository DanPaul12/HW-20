from sql_connect import connect_database

class Books:
    def __init__(self):
        self.books = {}
 
    def add_book(self):
        conn = connect_database
        if conn is not None:
            try:
                cursor = conn.cursor()
                title = input("What is the title?: ")
                author_id = int(input("What is author's id?: "))
                isbn = input("What is the ISBN?: ")
                query = "INSERT INTO books Values (%s, %s, %s)"
                values = title, author_id, isbn
                cursor.execute(query, values)
            finally:
                cursor.close()
                conn.close()
    
    def borrow_book(self):
        title = input("What is the title of the book?: ")
        if title in self.books:
            self.books[title]["availability"] = False
            print("{title} checked out")
        else:
            print("Book not found")

    def return_book(self):
        title = input("What is the title of the book?: ")
        if title in self.books:
            if self.books[title]["availability"] == False:
                print("{title} returned")
            else:
                print("Book is already there you must be confused")
        else:
            print("Book not found")

    def search_books(self):
        title = input("What is the title of the book you're searching for?")
        if title in self.books:
            print(self.books.get(title))

    def display_books(self):
        for title in self.books:
            print(self.books[title])

