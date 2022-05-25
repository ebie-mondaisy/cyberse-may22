from flask import Flask # Import Flask class
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy class
import os

app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI") # Set the connection string to connect to the database using an environment variable
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # Create SQLALchemy object

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

class Details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adress1 = db.Column(db.String(60), nullable=False)
    adress2 = db.Column(db.String(40), nullable=False)
    postcode = db.Column(db.String(10), nullable=False)

class Purchase_Date(db.Model):
    cal_id = db.Column(db.Integer, primary_key=True)
    date_purchase = db.Column(db.DateTime, nullable=False)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')