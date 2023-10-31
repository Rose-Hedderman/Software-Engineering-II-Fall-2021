from models import app, db, Book, BookDetails

def create_books():
    #Populating
    #----------
    # creating book1, book2, and book3 first, then add and committ.
    # Creating book1
    # In DBs, you need to figure out the id of the parent (i.e., publisher_id) that you want to add
    # In SQLAlchmey, you need only to supply the parent object and SQLAlchmey will extract the id.
    # I need to pass the publisher of the book. 
    newBook1 = Book(title = 'book1', id = 1)
    newBook2 = Book(title = 'book2', id = 2)
    newBook3 = Book(title = 'book3', id = 3) 

    db.session.add(newBook1)
    db.session.add(newBook2)
    db.session.add(newBook3)
    db.session.commit()

    # creating bookDetails3, bookDetails3, bookDetails3
    bookDetails1 = BookDetails(id = 11, detail = 'details of book 1')
    bookDetails2 = BookDetails(id = 12, detail = 'details of book 2')
    bookDetails3 = BookDetails(id = 13, detail = 'details of book 3')

    db.session.add(bookDetails1)
    db.session.add(bookDetails2)
    db.session.add(bookDetails2)
    db.session.commit()
    
    # You cannot use 'newBook1.details.append(bookDetails1)" since 
    # the property 'uselist' is set to False, i.e., One-To-One mapping
    # You can simply assign bookDetails1 object to 
    # the property newBook1.details and SQLAlchmey will 
    # automatically take care of the foreign key relationship.    
    newBook1.details = bookDetails1
    newBook2.details = bookDetails2
    newBook3.details = bookDetails3
    db.session.commit()
    
    # What happens If I add another book details, BookDetails4, to a previously assigned book, newBook1?
    # since I have one-to-one relationship, What I am trying to add is to add two children to the same parent.
    # If you run the following, you will notice that 'BookDetails1' will no longer has "book_id", and it's 
    # book_id is assigned to 'BookDetails4'.
    #bookDetails4 = BookDetails(id = 14, detail = 'details of book 4')
    #bookDetails4.book = newBook1
    #db.session.add(bookDetails4)
    #db.session.commit()
    
    
    

create_books()
