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
import dotenv

app = Flask(__name__)
app.config['SECRET_KEY'] = f'{os.getenv("SECRET_KEY")}'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)
dotenv.load_dotenv()

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    year = db.Column(db.Integer)
    description = db.Column(db.String(500))
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(500))
    img_url = db.Column(db.String(500))

class RateMovieForm(FlaskForm):
    rating = StringField('Your Rating out of 10', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    done = SubmitField('Done')

class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    add_movie = SubmitField('Add Movie')

def tmdb_search_movie(movie_title):
    api_url = 'https://api.themoviedb.org/3/search/movie?query='
    url = api_url + movie_title
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('API_KEY')}"
    }
    response = requests.get(url, headers=headers)
    return(response.json())

def tmdb_get_movie(movie_id):
    api_url = 'https://api.themoviedb.org/3/movie/'
    url = api_url + str(movie_id)
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('API_KEY')}"
    }
    response = requests.get(url, headers=headers)
    return(response.json())

# CREATE TABLE
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars()
    return render_template("index.html", movie_list=movies)

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    form = RateMovieForm()
    edit_movie = Movie.query.get(id)
    title = edit_movie.title
    if request.method == "POST":
        if form.validate_on_submit():
            new_rating = form.rating.data
            new_review = form.review.data

            edit_movie.rating = new_rating
            edit_movie.review = new_review
            db.session.commit()
            return redirect(url_for("home"))
        else:
            return render_template("edit.html", form=form, movie_title=title)
    else:
        return render_template("edit.html", form=form, movie_title=title)

@app.route("/delete/<int:id>", methods=["GET"])
def delete(id):
    delete_movie = Movie.query.get(id)
    db.session.delete(delete_movie)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if request.method == "POST":
        movie_data = tmdb_search_movie(form.title.data)
        return render_template("select.html", data=movie_data['results'])
    else:
        tmdb_move_id = request.args.get('movie_id')
        if tmdb_move_id:
            movie_data = tmdb_get_movie(tmdb_move_id)
            title = movie_data['title']
            img = "https://image.tmdb.org/t/p/w500" + movie_data['poster_path']
            year = movie_data['release_date'].split('-')[0]
            description = movie_data['overview']
            rating = movie_data['vote_average']
            with app.app_context():
                new_movie = Movie(title=title, year=year, description=description, rating=rating, img_url=img)
                db.session.add(new_movie)
                db.session.commit()
                db_movie_id = new_movie.id
            return redirect(url_for("edit", id=db_movie_id))
        else:
            return render_template("add.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
