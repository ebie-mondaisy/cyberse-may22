from flask import Flask, request, redirect, url_for, render_template
import os
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
app = Flask(__name__)

'''Start of Database Code'''
#no need for extra bits as the database will be built in
#app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SECRET_KEY"] = "CHOCOLATE_RAIN"

db = SQLAlchemy(app)


#syntax for if a message does not exist - if __init__ doesn't see a message, it will create one
#raise a validation error if user submits a form with errors in it
class ValidateUsername():
    def __init__(self, message=None):
        if not message:
            message = "Invalide username. Create Another"
        self.message = message

    def __call__(self, form, field):
        if field.data.lower() == 'admin':
            raise ValidationError(self.message)

#creating a form
class CustomerForm(FlaskForm):
    username = StringField("Username:", validators=[DataRequired(), ValidateUsername()])
    f_name = StringField("First Name:")
    l_name = StringField("Last Name:")
    submit = SubmitField("Submit")

    # def validate_username(self, username):
    #     if username.data.lower() == 'admin':
    #         raise ValidationError("Invalid username. Create Another.")
    #     return True



class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Colum(db.String(30), nullable=False)
    f_name = db.Column(db.String(30), nullable=False)
    l_name = db.Column(db.String(30), nullable=False)

db.create_all()
#db.drop_all()

'''Star of Website Code'''
@app.route('/home')
def hello_internet():
    return "Hello Internet!"

#creating an object to put variables into
#if statment to differentiate between GET and POST
@app.route('/form', methods=["GET", "POST"])
def add_cust():
    form = CustomerForm()

    if request.method == "POST":
        if form.validate_on_submit() and form.validate_username(form.username):
            cust1 = Customer(username=form.username.data, f_name=form.f_name.data, l_name=form.l_name.data)
            db.session.add(cust1)
            db.session.commit()
            
            return f"{cust1.f_name} has been added to the database!"
        else:
            return f"{form.username.errors}"

    return render_template("form.html", form = form)

#use this to test the get and post requests in postman
@app.route('/diff', methods=["GET", "POST"])
def hello_diff():
    if request.method == "POST":
        return "<h2>post request</h2>"
    else:
        return "<h2>get request</h2>"

#if you put a given word after the forwards slash, the function sill print it 5 times
# <int: ""> will turn the variable into an integer
@app.route('/edit/<int:word>')
def edit(word):
    return f"{word * 5}"

#take you to given web address
@app.route('/redirects')
def redirects():
    return redirect("https://www.google.co.uk")

#redirecting to whatever the url is for the given web address
@app.route('/urlfor')
def urlfor():
    return redirect(url_for("hello_internet"))

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)