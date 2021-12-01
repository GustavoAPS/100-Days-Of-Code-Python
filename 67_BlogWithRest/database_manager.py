from flask import Flask, render_template, request, redirect, url_for
import sqlite3


# crud - CREATE READ UPDATE DELETE


class DatabaseManager:

    def __init__(self):
        print("database initialized")

        self.db = sqlite3.connect("posts.db", check_same_thread=False)
        self.cursor = self.db.cursor()
        self.create_database()

    def create_database(self):

        self.cursor.execute("CREATE TABLE IF NOT EXISTS posts "
                            "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
                            "title varchar(250) NOT NULL UNIQUE, "
                            "sub_title varchar(250) NOT NULL,  "
                            "post_text text NOT NULL)")

        self.db.commit()

    def create_new_post(self, post_title, post_sub_title, post_text):
        self.cursor.execute(f"INSERT OR REPLACE INTO posts VALUES('None','{post_title}','{post_sub_title}','{post_text}')")
        self.db.commit()

    def get_post(self):
        pass

    def update_post(self):
        pass

    def delete_post(self):
        pass

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
