from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

# One-To-One relation: a Book can have only one  
# piece of setails.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:asd123@localhost:5432/bookdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # to suppress a warning message
db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'book'
    
    id = db.Column(db.Integer, primary_key = True)	
    title = db.Column(db.String(80), nullable = False)
    # The difference between One-To-Many and One-To_One
    # is that we add the property 'uselist = False'
    # This property is by default True in case of One-To-Many.
    # This property says that instead of storing this as a list
    # of objects, this is going to maintain a One-To-One mapping. 
    details = db.relationship('BookDetails', backref = 'book', uselist = False)

class BookDetails(db.Model):
    __tablename__ = 'bookdetails'

    id = db.Column(db.Integer, primary_key = True) 
    detail = db.Column(db.String(255))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))     

db.drop_all()
db.create_all()