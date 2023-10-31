from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

# One-To-Many relation: Assume that a Publisher can have many Books 
# but a Book can only have one Publisher.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:asd123@localhost:5432/bookdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # to suppress a warning message
db = SQLAlchemy(app)


class Publisher(db.Model):
    __tablename__ = 'publisher'
	
    name = db.Column(db.String(80), nullable = False)
    id = db.Column(db.Integer, primary_key = True)
    # This attribute connects Publisher with Book 
    # The name stored in backref is a sort of virtual column 
    # that will be inserted in the book table. This column will 
    # refer back to the Publisher.

    books = db.relationship('Book', backref = 'publisher')

class Book(db.Model):
    __tablename__ = 'book'
	
    title = db.Column(db.String(80), nullable = False)
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(250))
    price = db.Column(db.String(8))
    # This property refer to the "id" property in the "publisher" tabel
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'))
    
db.drop_all()
db.create_all()