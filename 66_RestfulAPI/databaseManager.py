import sqlite3

db = sqlite3.connect("cafes.db")
cursor = db.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT OR REPLACE INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# cursor.execute("INSERT OR REPLACE INTO books VALUES(2, 'The Hobbit', 'J. R. R. Tolkien', '9.75')")
# cursor.execute("INSERT OR REPLACE INTO books VALUES(3, 'Percy Jackson & the Olympians: The Lightning Thief', 'Rick Riordan', '8.5')")


# cursor.execute("SELECT title, author, rating FROM books;")
# dataTuples = cursor.fetchall()


all_books = []

for bookTuple in dataTuples:
    entry = {
        "title": bookTuple[0],
        "author": bookTuple[1],
        "rating": bookTuple[2],
    }
    all_books.append(entry)

# db.commit()

print(all_books)