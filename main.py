from flask import Flask, render_template, request, url_for, redirect, json, jsonify, Response, make_response
from flask_sqlalchemy import SQLAlchemy
import requests
from random import randint

# initializing Flask app 
app = Flask(__name__) 

# Google Cloud SQL (change this accordingly) 
PASSWORD ="password"
PUBLIC_IP_ADDRESS ="35.188.116.177"
DBNAME ="db1"
PROJECT_ID ="cs331e-test"
INSTANCE_NAME ="api-test-mysql"

# make these command line arguments that provide when you deploy the app OR
# or use other options like connecting directly from App Engine


# configuration 
app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql+mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket=/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True

db = SQLAlchemy(app) 

# User ORM for SQLAlchemy 
class Users(db.Model):
    eid = db.Column(db.String(50), primary_key = True, nullable = False) 
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = False, unique = True) 

@app.route('/users/add', methods =['GET', 'POST']) 
def add(): 

    # eid = "rz5292"
    # name = "Roger Zhong"
    # email = "roger.z@utexas.edu"

    if request.method == 'POST':
        data = request.json
        eid = data['eid']
        name = data['name']
        email = data['email']

        # checking if user already exists 
        user = Users.query.filter_by(email = email).first() 

        if not user: 
            try: 
                # creating Users object 
                user = Users( 
                    eid = eid,
                    name = name, 
                    email = email 
                ) 
                # adding the fields to users table 
                db.session.add(user) 
                db.session.commit() 
                # response 
                responseObject = { 
                    'status' : 'success'
                } 

                return make_response(responseObject, 200) 
            except: 
                responseObject = { 
                    'status' : 'fail'
                } 

                return make_response(responseObject, 400) 
            
        else: 
            # if user already exists then send status as fail 
            responseObject = { 
                'status' : 'fail', 
                'message': 'User already exists'
            } 

            return make_response(responseObject, 403) 



@app.route('/users/delete', methods =['GET', 'POST']) 
def delete(): 
	# getting id, name and email 
    eid = "rz5292"

	# checking if user already exists 
    user = Users.query.filter_by(eid = eid).first() 

    if user: 
        try: 
            db.session.delete(user) 
            db.session.commit() 
            # response 
            responseObject = { 
                'status' : 'success'
            } 

            return make_response(responseObject, 200) 
        except: 
            responseObject = { 
                'status' : 'fail'
            } 

            return make_response(responseObject, 400) 
        
    else: 
        # if user already exists then send status as fail 
        responseObject = { 
            'status' : 'fail', 
            'message': 'User does not exist'
        } 

        return make_response(responseObject, 403) 



@app.route('/users/') 
def view(): 
    # fetches all the users 
    users = Users.query.all() 

    response = list()
    for user in users: 
        response.append({ 
            "eid" : user.eid,
            "name" : user.name, 
            "email": user.email 
        }) 

    return make_response({ 
        'users': response
    }, 200) 








class Books(db.Model):
    bookid = db.Column(db.String(50), primary_key = True, nullable = False) 
    title = db.Column(db.String(50), nullable = False)

@app.route('/')
def index():
    books = Books.query.all() 
    response = list()

    # books = [{'title': 'Software Engineering', 'id': '1'}, \
    #          {'title':'Algorithm Design', 'id':'2'},       \
    #          {'title':'Python', 'id':'3'}]

    for book in books: 
        response.append({ 
            "id" : book.bookid,
            "title" : book.title
        }) 
        
    return render_template('showBook.html', books = response)

@app.route('/book/new')
def newBook():
    return render_template('newBook.html')

@app.route('/book/<int:book_id>/delete')
def deleteBook(book_id):
    book = Books.query.filter_by(bookid = book_id).first()
    return render_template('deleteBook.html', id = book.bookid, title = book.title)


@app.route('/delete/<int:book_id>', methods=['GET','POST'])
def bookDelete(book_id):
    book = Books.query.filter_by(bookid = book_id).first()

    if book: 
        db.session.delete(book) 
        db.session.commit() 

    return redirect(url_for('index'))

@app.route('/add/', methods=['GET','POST'])
def bookAdd():
    title = request.form['name']
    bookid = randint(0, 9999999)
    
    book = Books.query.filter_by(bookid = bookid).first()

    if not book:
        book = Books( 
            bookid = bookid,
            title = title
        ) 
        db.session.add(book) 
        db.session.commit()
            
    return redirect(url_for('index'))

@app.route('/book/')
def bookjson():
    books = Books.query.all() 

    response = list()

    for book in books: 
        response.append({ 
            "id" : book.bookid,
            "title" : book.title
        }) 

    return make_response({  
        'books': response 
    }, 200) 

@app.route('/book/<int:book_id>', methods=['GET','POST'])
def book(book_id):
    book = Books.query.filter_by(bookid = book_id).first()

    response = {
        "id" : book.bookid,
        "title" : book.title
    }

    return make_response(response, 200)



if __name__ == "__main__":
    db.drop_all()
    db.create_all()

    base_url = "https://openlibrary.org/works/OL20439524W.json"
    response = requests.get(url=base_url)
    json_data = json.loads(response.text)

    title = json_data["title"]
    bookid = json_data["covers"][0]

    book = Books.query.filter_by(bookid = bookid).first() 

    if not book: 
        book = Books( 
            bookid = bookid,
            title = title 
        ) 
        db.session.add(book) 
        db.session.commit() 


    base_url = "https://openlibrary.org/works/OL20864122W.json"
    response = requests.get(url=base_url)
    json_data = json.loads(response.text)

    title = json_data["title"]
    bookid = json_data["covers"][0]

    book = Books.query.filter_by(bookid = bookid).first() 

    if not book: 
        book = Books( 
            bookid = bookid,
            title = title 
        ) 
        db.session.add(book) 
        db.session.commit() 

    app.run()
