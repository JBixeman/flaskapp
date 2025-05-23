from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField,DateTimeField,
                     RadioField,SelectField,
                     TextAreaField,TextField)

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'KEY'

class InfoForm(FlaskForm):

    breed = StringField('What breed are you?', validators=[DataRequired()])
    neutered = BooleanField('Neutered?')
    mood = RadioField('Mood?', choices=[('mood_one','Happy'),('mood_two','Happy'),('mood_three','Excited')])
    food_choice = SelectField(u'Pick your favorite food:',choices=[('chi','Chicken'),('bf','Beef'),('fish','Fish')])
    feedback = TextAreaField('Feedback:')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food_choice'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))
    return render_template('base.html', form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)