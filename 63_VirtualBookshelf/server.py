from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
db = sqlite3.connect("books-collection.db")
cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

cursor.execute("INSERT OR REPLACE INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
cursor.execute("INSERT OR REPLACE INTO books VALUES(2, 'The Hobbit', 'J. R. R. Tolkien', '9.75')")
cursor.execute("INSERT OR REPLACE INTO books VALUES(3, 'Percy Jackson & the Olympians: The Lightning Thief', 'Rick Riordan', '8.5')")

db.commit()


all_books = [
    {
        "title": "Harry Potter.1",
        "author": "J. K. Rowling",
        "rating": 9,
    },
    {
        "title": "Harry Potter.3",
        "author": "J. K. Rowling",
        "rating": 10,
    },
    {
        "title": "A pequena sereia",
        "author": "Gaby",
        "rating": 10,
    }
]

@app.route('/')
def home():
    return render_template('index.html', books=all_books, booksNumber=len(all_books))


@app.route("/add")
def add():
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)
