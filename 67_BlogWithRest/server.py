from flask import Flask
from flask import render_template
from flask import request
import json


app = Flask(__name__)


def get_posts():
    with open("posts/posts_2021.json") as file:
        contents = json.load(file)
        return contents


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html', posts=get_posts())


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html', id=post_id)


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
