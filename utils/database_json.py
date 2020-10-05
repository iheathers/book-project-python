"""
Database
"""
import json

book_file = 'books.json'


def create_table():
    with open(book_file, 'w') as file:
        json.dump([], file)


def add_book(name, author, read=False):
    books = get_all_books()
    books.append({
        "name": name,
        "author": author,
        "read": read
    })
    with open(book_file, 'w') as file:
        json.dump(books, file, indent=4)


def get_all_books():
    with open(book_file, 'r') as file:
        return json.load(file)


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True
    _save_all_books(books)


def _save_all_books(books):
    with open(book_file, 'w') as file:
        json.dump(books, file)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)
