class Books:
    def __init__(self):
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

    def search_books(self):
        title = input("What is the title of the book you're searching for?")
        if title in self.books:
            print(self.books[title])

    def display_books(self):
        for title in self.books:
            print(self.books[title])

