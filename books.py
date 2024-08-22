from sql_connect import connect_database
from sql_connect import Error

class Books:
    def __init__(self):
        self.books = {}
 
    def add_book(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                book_id = int(input("What is the book id?: "))
                title = input("What is the title?: ")
                author_id = int(input("What is author's id?: "))
                isbn = input("What is the ISBN?: ")
                availability = True
                query = "INSERT INTO books Values (%s, %s, %s, %s, %s)"
                values = book_id, title, author_id, isbn, availability
                cursor.execute(query, values)
                conn.commit()
                print("Book added succesfully")
            except Error:
                print({Error})
            finally:
                cursor.close()
                conn.close()
    
    def borrow_book(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                book_id = int(input("What is the book id?: "))
                query = "Set availability = %s WHERE book_id = %s"
                values = 0, book_id
                cursor.execute(query, values)
                conn.commit()
                print("Book borrowed succesfully")
            except Error as e:
                print({e})
            finally:
                cursor.close()
                conn.close()

    def search_books(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor(buffered = True)
                query = "SELECT title from books where id = %s"
                book = input("What is the book's id?: ")
                cursor.execute(query, (book,))
                conn.commit()
                for row in cursor.fetchall():
                    print(row)
            except Error as e:
                print({e})
            finally:
                cursor.close()
                conn.close()

    def display_books(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor(buffered = True)
                query = "SELECT * from books"
                cursor.execute(query)
                conn.commit()
                for row in cursor.fetchall():
                    print(row)
            except Error as e:
                print({e})
            finally:
                cursor.close()
                conn.close()
