from flask import Flask
from flask import render_template
from flask import request
import database_manager
import json


app = Flask(__name__)
database = database_manager.DatabaseManager()


def get_posts():
    with open("posts/posts_2021.json") as file:
        contents = json.load(file)
        return contents


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html', posts=database.get_all_posts())


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html', id=post_id)


@app.route('/create_post', methods=["POST"])
def create_post():
    title = request.form['title']
    sub_title = request.form['sub_title']
    text = request.form['text']
    database.create_new_post(post_title=title, post_sub_title=sub_title, post_text=text)
    return f"{title} {sub_title} {text}"


@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        # send email function
        print(f"{name} {email} {phone} {message}")
        return f"Message sent"

    return render_template('contact.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        name = request.form['username']
        password = request.form['password']
        return f"<h1>name: {name}password: {password}</h1>"
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
