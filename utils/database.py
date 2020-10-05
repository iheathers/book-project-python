"""
Database
"""
import json

book_file = 'books.txt'


# def create_table():
#     with open(book_file, 'w') as file:
#         file.write("")


def add_book(name, author, read='0'):
    with open(book_file, 'a') as file:
        file.write(f'{name},{author},{read}\n')


def get_all_books():
    with open(book_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]
        return [
            {"name": line[0], "author": line[1], "read": line[2]}
            for line in lines
        ]


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
        _save_all_books(books)


def _save_all_books(books):
    with open(book_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)
