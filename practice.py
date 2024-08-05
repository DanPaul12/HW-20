class Genres:
    def __init__(self, name, info):
        self.__name__ = name
        self.__info__ = info

    def set_genre(self, genre):
        self.__name__ = genre

    def set_info(self, genre):
        self.__name__ = genre


class Books(Genres):
    def __init__(self, title, author, isbn, genre, info):
        self.title = title
        self.author = author
        self.isbn = isbn
        super().__init__(genre, info)
        self.books = {}
 
    def add_book(self):
        title = input("What is the title?: ")
        author = input("Who is the author?: ")
        isbn = input("What is the ISBN?: ")
        self.books[title]= {"title":title, "author":author, "ISBN":isbn, "availability": True}
        print(self.books[title])
    
    def borrow_book(self):
        title = input("What is the title of the book?: ")
        if title in self.books:
            self.books[title]["availability"] = False
            print("Book checked out")
        else:
            print("Book not found")

    def return_book(self):
        title = input("What is the title of the book?: ")
        if title in self.books:
            if self.books[title]["availability"] == False:
                print("Book returned")
            else:
                print("Book is already there you must be confused")
        else:
            print("Book not found")

    def display_books(self):
        for title in self.books:
            print(self.books[title])

books = Books("horror", "scary stuff")
    
books.add_book() 
books.borrow_book()
books.display_books()