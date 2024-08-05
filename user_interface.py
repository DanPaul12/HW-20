from books import Books
from users import Users
from genres import Genres
from genres import Authors

class UserInterface:
    def book_operations():
        while True:
            command = int(input(f"Book Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books"))
            if command == 1:
                Books.add_book()
            elif command == 2:
                Books.borrow_book()
            elif command == 3:
                Books.return_book()
            elif command == 4:
                Books.search_books()
            elif command == 5:
                Books.display_books()
            else:
                print("Invalid command")

    def user_operations():
        while True:
            command = int(input(f"User Operations:\n1. Add a new user\n2. View user details\n3. Display all users"))
            if command == 1:
                Users.add_user()
            elif command == 2:
                Users.search_users()
            elif command == 3:
                Users.display_users()
            else:
                print("Invalid command")

    def author_operations():
        while True:
            command = int(input(f"Author Operations:\n1. Add a new author\n2. View author details\n3. Display all authors"))
            if command == 1:
                Authors.add_author()
            elif command == 2:
                Authors.search_author()
            elif command == 3:
                Authors.display_authors()
            else:
                print("Invalid command")

    def genre_operations():
        while True:
            command = int(input(f"Genre Operations:\n1. Add a new genre\n2. View genre details\n3. Display all genres"))
            if command == 1:
                Genres.add_genre()
            elif command == 2:
                Genres.search_genres()
            elif command == 3:
                Genres.display_genres()
            else:
                print("Invalid command")

user_interface = UserInterface()
user_interface.book_operations