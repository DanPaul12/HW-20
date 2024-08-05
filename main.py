from user_interface import UserInterface

def main():
    while True:
        command = input(f"Welcome to the Library Management System!\nMain Menu:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Genre Operations\n5. Quit")
        if command == 1:
            UserInterface.book_operations()
        elif command == 2:
            UserInterface.user_operations()
        elif command == 3:
            UserInterface.author_operations()
        elif command == 4:
            UserInterface.genre_operations()
        elif command == 5:
            break
        else:
            print("Invalid command")


main()