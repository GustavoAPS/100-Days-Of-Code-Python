import json
from flask import Flask
from flask import render_template


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


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html', id=post_id)


if __name__ == "__main__":
    app.run(debug=True)
