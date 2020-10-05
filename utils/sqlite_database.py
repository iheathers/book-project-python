"""
Database
"""
from typing import List, Dict, Union
from .database_connection import DatabaseConnection

Book = Dict[str, Union[str, int]]


def create_table() -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)")


def add_book(name, author, read=False) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO books VALUES (?, ?, ?)", (name, author, read))


def get_all_books() -> List[Book]:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books")
        books = [{"name": row[0], "author": row[1], "read": row[2]} for row in cursor.fetchall()]
        return books


def mark_book_as_read(name: str):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE books SET read=1 WHERE name=?", (name,))


def delete_book(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM books WHERE name=?", (name,))
