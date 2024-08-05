from books import Books
from users import Users
from genres import Genres
from genres import Authors

books = Books()
users = Users()
genres = Genres()
authors = Authors()

class UserInterface:
    def book_operations():
        while True:
            command = int(input(f"Book Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books\nPlease enter a number 1-5: "))
            if command == 1:
                Books.add_book(books)
                break
            elif command == 2:
                Books.borrow_book(books)
                break
            elif command == 3:
                Books.return_book(books)
                break
            elif command == 4:
                Books.search_books(books)
                break
            elif command == 5:
                Books.display_books(books)
                break
            else:
                print("Invalid command")

    def user_operations():
        while True:
            command = int(input(f"User Operations:\n1. Add a new user\n2. View user details\n3. Display all users\nPlease enter a number 1-3: "))
            if command == 1:
                Users.add_user(users)
                break
            elif command == 2:
                Users.search_users(users)
                break
            elif command == 3:
                Users.display_users(users)
                break
            else:
                print("Invalid command")

    def author_operations():
        while True:
            command = int(input(f"Author Operations:\n1. Add a new author\n2. View author details\n3. Display all authors\nPlease enter a number 1-3: "))
            if command == 1:
                Authors.add_author(authors)
                break
            elif command == 2:
                Authors.search_author(authors)
                break
            elif command == 3:
                Authors.display_authors(authors)
                break
            else:
                print("Invalid command")

    def genre_operations():
        while True:
            command = int(input(f"Genre Operations:\n1. Add a new genre\n2. View genre details\n3. Display all genres\nPlease enter a number 1-3: "))
            if command == 1:
                Genres.add_genre(genres)
                break
            elif command == 2:
                Genres.search_genres(genres)
                break
            elif command == 3:
                Genres.display_genres(genres)
                break
            else:
                print("Invalid command")

