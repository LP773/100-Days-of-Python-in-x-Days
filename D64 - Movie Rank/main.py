from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

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

# CREATE TABLE
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    movies = Movie.query.all()
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

if __name__ == '__main__':
    app.run(debug=True)
