from utils import sqlite_database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice: """


def menu():
    sqlite_database.create_table()
    user_input = input(USER_CHOICE)

    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()

        elif user_input == 'l':
            list_books()

        elif user_input == 'r':
            prompt_read_book()

        elif user_input == 'd':
            prompt_delete_book()

        else:
            print("Unknown command. Please try again.")

        user_input = input(USER_CHOICE)

    if user_input == 'q':
        print("Stopping the program!!!")


def prompt_add_book():
    name = input("Enter book name: ")
    author = input("Enter book author: ")
    print("Adding a new book...")
    sqlite_database.add_book(name, author)


def list_books():
    books = sqlite_database.get_all_books()
    print("Listing all books...")
    for book in books:
        name = book['name']
        author = book['author']
        read = book['read']
        print(f'Name: {name}\nAuthor: {author}\nRead: {read}\n')


def prompt_read_book():
    name = input("Enter name of book you have read already: ")
    print("Marking book as read...")
    sqlite_database.mark_book_as_read(name)


def prompt_delete_book():
    name = input("Enter book name you want to delete: ")
    print("Deleting the book")
    sqlite_database.delete_book(name)


menu()
