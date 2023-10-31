from models import app, db, Publisher, Book

def create_books():
    #Populating
    #----------
    # creating publisher1
    newPublisher1 = Publisher(name = 'publisher1', id = 11 )
        
    # After I create newPublisher1, I can then add it to my session. 
    db.session.add(newPublisher1)
    # commit the session to my DB.
    db.session.commit()
    
    # creating publisher2 
    newPublisher2 = Publisher(name = 'publisher2', id = 12 )
    db.session.add(newPublisher2)
    db.session.commit()
    
    # creating book1, book2, and book3 first, then add and committ.
    # In DBs, you need to figure out the id of the parent (i.e., publisher_id) that you want to add
    # In SQLAlchmey, you need only to supply the parent object and SQLAlchmey will extract the id.
    # I need to pass the publisher of the book. 
    newBook1 = Book(title = 'book1', id = 1,          \
        description = 'description1', price = '$45',  \
        publisher = newPublisher1)
           
    # creating book2    
    newBook2 = Book(title = 'book2', id = 2,         \
        description = 'description2', price = '$50', \
        publisher = newPublisher2)

    # creating book3    
    newBook3 = Book(title = 'book3', id = 3,         \
        description = 'description3', price = '$55') 

    db.session.add(newBook1)
    db.session.add(newBook2)
    db.session.add(newBook3)
    db.session.commit()
    
    # Book class has the property books, which is set up
    # as a flask relationship. So, I can use books as
    # a list. I can append a Book object to a Publisher object 
    newPublisher1.books.append(newBook3) 
    #newBook3.publisher = newPublisher1 # another way to achieve the same
    db.session.commit() 

    # Querying
    #---------
    somePublisher = Publisher.query.filter_by(name='publisher1').first()
    print("Publisher data:")
    print(somePublisher)
    # somePublisher is an object. We can access its id, name and books attributes using 
    # the dot operator.
    print(somePublisher.id)
    print(somePublisher.name)
    print(somePublisher.books)
    print(somePublisher.books[0])
    print(somePublisher.books[0].id)
    
    someBook = Book.query.filter_by(title='book1').first()
    print("Book data:")
    print(someBook)
    # someBook is an object. We can obtain its id and title using the dot operator.
    print(someBook.id)
    print(someBook.title)
    print(someBook.publisher)
    print(someBook.publisher.id)
    print(someBook.publisher.name)
    

create_books()
