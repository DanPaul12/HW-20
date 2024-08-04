class Users:
    def __init__(self):
        self.users = {}
 
    def add_user(self):
        name = input("What is user's name?: ")
        libID = input("What is your id number?: ")
        self.users[name]= {"name":name, "Library ID":libID}
        print(self.users[name])

    def display_users(self):
        for name in self.users:
            print(self.users[name])

books = Books()
    
books.add_book() 
books.borrow_book()
books.display_books()