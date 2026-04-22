from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    with app.app_context():
        books = Book.query.all()

    if len(books) == 0:
        empty = True
    else:
        empty = False

    return render_template('index.html', books=books, empty=empty)

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        with app.app_context():
            book = Book(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
            db.session.add(book)
            db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('add.html')

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        book = Book.query.get(id)
        new_rating = request.form['new_rating']
        book.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('edit.html', book=book)

@app.route("/delete/<int:id>", methods=['GET'])
def delete(id):
    if request.method == 'GET':
        with app.app_context():
            book = Book.query.get(id)
            db.session.delete(book)
            db.session.commit()
            return redirect(url_for('home'))
    else:
        return None


if __name__ == "__main__":
    app.run(debug=True)

