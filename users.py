class Users:
    def __init__(self):
        self.users = {}
 
    def add_user(self):
        name = input("What is user's name?: ")
        libID = input("What is your id number?: ")
        self.users[name]= {"name":name, "Library ID":libID}
        print(self.users[name])
        
    def search_users(self):
        user = input("What is the title of the book you're searching for?")
        if user in self.books:
            print(self.users[user])

    def display_users(self):
        for name in self.users:
            print(self.users[name])

