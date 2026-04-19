from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

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
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    cafe_location = StringField('Cafe Location', validators=[DataRequired(), URL()])
    open = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close = StringField('Closing Time e.g. 6PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', validators=[DataRequired()],choices=[
        ('☕','☕'),
        ('☕☕','☕☕'),
        ('☕☕☕','☕☕☕'),
        ('☕☕☕☕','☕☕☕☕'),
        ('☕☕☕☕☕','☕☕☕☕☕')
    ])
    wifi_strength = SelectField('Wifi Strength Rating', validators=[DataRequired()], choices=[
        ('✘', '✘'),
        ('💪', '💪'),
        ('💪💪', '💪💪'),
        ('💪💪💪', '💪💪💪'),
        ('💪💪💪💪💪', '💪💪💪💪💪'),
        ('💪💪💪💪💪💪', '💪💪💪💪💪💪')
    ])
    power_availability = SelectField('Power Availability Rating', validators=[DataRequired()], choices=[
        ('✘', '✘'),
        ('🔌', '🔌'),
        ('🔌🔌', '🔌🔌'),
        ('🔌🔌🔌', '🔌🔌🔌'),
        ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),
        ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')
    ])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    print(form.data)
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', newline='', encoding='utf-8') as csv_file:
            row = [
                form.cafe.data,
                form.cafe_location.data,
                form.open.data,
                form.close.data,
                form.coffee_rating.data,
                form.wifi_strength.data,
                form.power_availability.data
            ]
            writer = csv.writer(csv_file)
            writer.writerow(row)
            return "<h1>Successfully added Cafe!</h1>"
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
