from flask import Flask, render_template, request, redirect, url_for
import sqlite3


class DatabaseManager:
    def __init__(self):
        self.db = sqlite3.connect("books-collection.db")
        self.cursor = self.db.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT OR REPLACE INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# cursor.execute("INSERT OR REPLACE INTO books VALUES(2, 'The Hobbit', 'J. R. R. Tolkien', '9.75')")
# cursor.execute("INSERT OR REPLACE INTO books VALUES(3, 'Percy Jackson & the Olympians: The Lightning Thief', 'Rick Riordan', '8.5')")


# cursor.execute("SELECT title, author, rating FROM books;")
# dataTuples = cursor.fetchall()

# all_books = []

# for bookTuple in dataTuples:
#    entry = {
#        "title": bookTuple[0],
#        "author": bookTuple[1],
#        "rating": bookTuple[2],
#    }
#    all_books.append(entry)

# db.commit()

# print(all_books)
