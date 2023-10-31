from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:asd123@localhost:5432/bookdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # to suppress a warning message
db = SQLAlchemy(app)

# Many-To-Many relation: Assume that an Author can have many Books 
# and a Book can also have many Authors.
#
# You cannot setup a Many-To-Many where you have a relationship
# on one object and an ID stored in the table becuase in this way 
# you will only be able to store a single ID in that table
# with the related object. So we need something to store
# an ID of one object and an idea of the related object and maintain
# multiple objects can relate to multiple other objects.
#
# link is a (joined or association) table with two columns.
# It maintains the relationship between Author and Book
# It has two forign keys (the primary keys of the tables)
# To automatically update link table, one need to create
# a connection within Author and Book via 'relationship()' 
# in each corresponding table.
link = db.Table('link',
   db.Column('author_id', db.Integer, db.ForeignKey('author.id')), 
   db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
   )
  
class Author(db.Model):
    __tablename__ = 'author'
	
    name = db.Column(db.String(80), nullable = False)
    id = db.Column(db.Integer, primary_key = True)
    # This attribute connects an Author object, a Book object, 
    # and the table link 
    books = db.relationship('Book', secondary = 'link', backref='wrote')
    
class Book(db.Model):
    __tablename__ = 'book'
	
    title = db.Column(db.String(80), nullable = False)
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(250))
    price = db.Column(db.String(8))
     
db.drop_all()
db.create_all()