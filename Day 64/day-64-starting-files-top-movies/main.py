from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv, find_dotenv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)

# load up the entries as environment variables
load_dotenv("D:/API/EnvironmentVariables/.env")

THE_MOVIE_DB_URL = "https://api.themoviedb.org/3/search/movie"
THE_MOVIE_DB_MOVIE_DETAIL_URL = "https://api.themoviedb.org/3/movie"
THE_MOVIE_DB_IMG_URL = "https://image.tmdb.org/t/p/w500"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.environ.get('THE_MOVIE_DB_HEADER')}"
}

# CREATE DB
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"

# initialize the app with the extension
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

    # After adding the new_movie the code needs to be commented out/deleted.
    # So you are not trying to add the same movie twice.
    if not Movie.query.filter_by(title="Phone Booth").first():
        new_movie = Movie(
            title="Phone Booth",
            year=2002,
            description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
            rating=7.5,
            ranking=10,
            review="My favourite character was the caller.",
            img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
        )
        db.session.add(new_movie)
        db.session.commit()
    if not Movie.query.filter_by(title="Avatar The Way of Water").first():
        second_movie = Movie(
            title="Avatar The Way of Water",
            year=2022,
            description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
            rating=7.3,
            ranking=9,
            review="I liked the water.",
            img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
        )
        db.session.add(second_movie)
        db.session.commit()

# Create edit movie form
class EditMovieForm(FlaskForm):
    rating = StringField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')
    cancel = SubmitField('Cancel', render_kw={'class':'btn btn-secondary'})

class AddMovieForm(FlaskForm):
    title = StringField('Movie title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')
    cancel = SubmitField('Cancel', render_kw={'class':'btn btn-secondary'})

@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    ranking = 1
    for movie in movies:
        movie.ranking = ranking
        ranking += 1
    db.session.commit()
    return render_template("index.html", movies=movies)

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = EditMovieForm()
    movie_id = request.args.get("id", type=int)
    movie = db.get_or_404(Movie, movie_id)

    if form.cancel.data: # if cancel button is clicked, the form.cancel.data will be True
        return redirect(url_for("home"))

    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("edit.html", form=form, movie_id=movie_id)

@app.route("/delete")
def delete():
    movie_id = request.args.get("id", type=int)
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=["POST", "GET"])
def add():
    form = AddMovieForm()

    if form.cancel.data: # if cancel button is clicked, the form.cancel.data will be True
        return redirect(url_for("home"))

    if form.validate_on_submit():
        search_movie = form.title.data.replace(' ', '%20')
        response = requests.get(f"{THE_MOVIE_DB_URL}?query={search_movie}", headers=headers)
        response.raise_for_status()
        movie_data = response.json()['results']
        movie_list = []
        for movie in movie_data:
            movie_list.append({
                'id': movie['id'],
                'title': movie['title'],
                'release_date': movie['release_date'],
            })
        return render_template("select.html", movie_list=movie_list)
        
    return render_template("add.html", form=form)

@app.route("/select")
def select():
    movie_id = request.args.get("id", type=int)
    response = requests.get(f"{THE_MOVIE_DB_MOVIE_DETAIL_URL}/{movie_id}", headers=headers)
    response.raise_for_status()
    movie_detail = response.json()
    new_movie = Movie(
        title= movie_detail['original_title'],
        year= movie_detail['release_date'],
        description= movie_detail['overview'],
        img_url= f"{THE_MOVIE_DB_IMG_URL}{movie_detail['poster_path']}",
    )
    db.session.add(new_movie)
    db.session.commit()
    # new_movie_id = db.session.scalar(db.select(Movie).where(Movie.title==movie_detail['original_title']))
    return redirect(url_for("edit", id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
