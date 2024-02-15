class Book:

    def __init__(self, title, author, isbn, availability=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = availability
    
    def __str__(self):
        return self.title

class Library:
    def __init__(self):
        self.books = []
            
    def add_book(self,book): 
        self.books.append(book)
        print(f"Added the book {book} to the library")
        
    def remove_book(self,isbn):
        for i in self.books:
           if i.isbn == isbn:
               self.books.remove(i)
               print(f"The book {i} is removed from the library")
        
    def search_book(self,title):
        for i in self.books:
            if i.title==title:
                return i
            else:
                print("The Book you are searching is not available")
    
    def checkout_book(self,isbn):
        for i in self.books:
            if i.isbn==isbn: 
                if i.availability==True:
                    i.availability=False
                    print("Book is available")
                else:
                    print("Book is not available")
        print("No Book found for this ISBN")
                      
    def return_book(self,isbn):
        for i in self.books:
          if i.isbn == isbn:
              if not i.availability:
                  i.availability==True
                  print(f"Return completed for the book {i}")
              else:
                  print(f"Book {i} was not checked out")
        print("Book with the given ISBN not found.")
            
            
                  
    def display_book(self):
        for i in self.books:
            if i.availability:
                print(i)
    

book1=Book('Python','David','123')
book2=Book('R','Thomas','456')
book3=Book('Statistics','John','789')


lib=Library()

lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)

lib.display_book()
lib.remove_book(book3)
lib.display_book()


#-------------------------------------------------------------------------------

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = True

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"
    
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book} to the library.")
    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Removed {book} from the library.")
                return
        print(f"No book found with ISBN: {isbn}")
    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
    def checkout_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.availability:
                    book.availability = False
                    print(f"You've successfully checked out {book}.")
                    return book
                else:
                    print(f"{book} is currently unavailable.")
                    return None
        print(f"No book found with ISBN: {isbn}")
        return None
    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.availability = True
                print(f"Thanks for returning {book}!")
                return
        print(f"No book found with ISBN: {isbn}")
    def display_available_books(self):
        print("Available Books:")
        for book in self.books:
            if book.availability:
                print(book)
    # Simulation
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
book2 = Book("Moby Dick", "Herman Melville", "0987654321")
book3 = Book("Pride and Prejudice", "Jane Austen", "1122334455")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


library.display_available_books()

library.display_available_books()
    
            
    

    
        