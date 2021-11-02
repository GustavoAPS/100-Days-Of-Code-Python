import json

from flask import Flask
from flask import render_template
import requests


app = Flask(__name__)


# def get_posts():
#    with open("posts/posts_2021.json") as file:
#        contents = json.load(file)
#        return contents


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post')
def post():
    return render_template('post.html')


if __name__ == "__main__":
    app.run(debug=True)
