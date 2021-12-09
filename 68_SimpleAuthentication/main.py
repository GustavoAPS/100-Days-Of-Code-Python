import werkzeug.security
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['SECRET_KEY'] = 'f2413f543f15b368b040661451f335983158b1e4567a0abe96b481b357a864e0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()

class loginUser():
    is_authenticated = False
    is_active = False
    is_anonymous = False

    def get_id:
        pass

def create_new_user(new_user_name, new_user_email, new_user_password):
    hash_password = werkzeug.security.generate_password_hash(new_user_password, method='pbkdf2:sha256', salt_length=8)
    print(hash_password)
    guest = User(name=new_user_name, email=new_user_email, password=hash_password)
    db.session.add(guest)
    db.session.commit()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():

    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        print(f"User received\n"
              f"Name: {name}\n"
              f"Email: {email}\n"
              f"Password: {password}\n")
        create_new_user(name, email, password)
        return render_template("secrets.html", name_of_user=name)

    if request.method == "GET":
        return render_template("register.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    print("download called")
    return send_from_directory('static/files/', "cheat_sheet.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
