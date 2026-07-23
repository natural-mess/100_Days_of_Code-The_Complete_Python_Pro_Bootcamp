from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # This queries your database to find the user by their ID
    return db.get_or_404(User, user_id)

# CREATE TABLE IN DB


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_active)


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        login_info = db.session.execute(db.select(User).filter_by(email=request.form.get('email'))).scalar()
        if login_info:
            flash('You have already signed up with that email, login instead!')
            return redirect(url_for('login'))
        new_user = User(
            email = request.form.get('email'),
            password = generate_password_hash(request.form.get('password'), method="pbkdf2:sha256", salt_length=8),
            name = request.form.get('name'),
        )
        # print(new_user.password)
        db.session.add(new_user)
        db.session.commit()
        # Log in and authenticate user after adding details to database.
        login_user(new_user)
        return redirect(url_for('secrets'), logged_in=current_user.is_active)
    return render_template("register.html")


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        login_info = db.session.execute(db.select(User).filter_by(email=request.form.get('email'))).scalar()
        print(login_info)
        if login_info:
            if check_password_hash(login_info.password, request.form.get('password')):
                login_user(login_info)
                # Imagine a user tries to visit /admin_dashboard, but they aren't logged in. 
                # Flask-Login intercepts them and kicks them to the /login page. 
                # But Flask is polite! It remembers where they wanted to go by putting it in the URL like this:
                # yourwebsite.com/login?next=/admin_dashboard
                # next = request.args.get('next')
                return redirect(url_for('secrets'), logged_in=current_user.is_active)
            else:
                flash('Password incorrect, please try again.')
                return render_template("login.html")
        else:
            flash('That email does not exist, please try again.')
            return render_template("login.html")
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
def download():
    return send_from_directory(directory='static/files', path='cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
