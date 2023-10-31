from models import app, db, Author, Book

def create_books():
    # create three Author objects
    author1 = Author(name = 'author1', id = 1 )
    author2 = Author(name = 'author2', id = 2 )
    author3 = Author(name = 'author3', id = 3)

    db.session.add(author1)
    db.session.add(author2)
    db.session.add(author3)
    db.session.commit()

    # create two Book objects
    book1 = Book(title = 'book1', id = '11', description = 'desc1', price = '$5')
    book2 = Book(title = 'book2', id = '12', description = 'desc2', price = '$12')

    db.session.add(book1)
    db.session.add(book2)
    db.session.commit()
    
    book1.wrote.append(author1)
    db.session.commit() 
    
    book1.wrote.append(author2)
    db.session.commit()
    
    book1.wrote.append(author3)
    db.session.commit()

    book2.wrote.append(author2)
    db.session.commit()

    book2.wrote.append(author1)
    db.session.commit()
    
    
    # Querying
    #---------
    someAuthor = Author.query.filter_by(name='author1').first()
    print("Author data:")
    print(someAuthor)
    # someAuthor is an object. We can access its id, name and books attributes using 
    # the dot operator.
    print(someAuthor.id)
    print(someAuthor.name)
    '''
    print(someAuthor.books)
    print(someAuthor.books[0])
    print(someAuthor.books[0].id)
    '''
    
    someBook = Book.query.filter_by(title='book1').first()
    print("Book data:")
    print(someBook)
    # someBook is an object. We can obtain its id and title using the dot operator.
    print(someBook.id)
    print(someBook.title)
    print(someBook.wrote)
    print(someBook.wrote[0])
    print(someBook.wrote[0].id)
    
    for author in someBook.wrote:
       print(author.name)
    
'''   
    # add an Author object to the author attribute of Book object.
    book1.wrote.append(author2)
    book2.wrote.append(author3)
    db.session.add(book1)
    db.session.add(book2)
    db.session.commit()
    
    author4 = Author(name = 'author4', id = 4)
    author4.books.append(book1)
    db.session.add(author4)
    db.session.commit()
'''    
    
    
create_books()