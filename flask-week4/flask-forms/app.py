from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    date_of_birth = DateField('Date of Birth')
    fave_num = IntegerField('Favourite Number')
    fave_food = SelectField('Favourite Food', choices=[
        ("cake", "Cake"), ("fries", "Fries"), ("broccoli", "Broccoli")
    ])
    submit = SubmitField('Add Profile')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    message = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        date_of_birth = form.date_of_birth.data
        fave_num = form.fave_num.data
        fave_food = form.fave_food.data

        username = "MadDog99"

        if len(first_name) == 0 or len(last_name) == 0:
            message = "Please supply both first and last name"
        else:
            message = ( f'''Thank you, {username}, you have have given us the following information:\n'''
                        f'''Your name is: {first_name} {last_name}\n'''
                        f'''Your date of birth is: {date_of_birth}\n'''
                        f'''Your favourite number is: {fave_num}\n'''
                        f'''Your favourite food is: {fave_food} ''')

    return render_template('home.html', form=form, message=message)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')