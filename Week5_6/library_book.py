'''
This program is a simple library book management where a book can be issued, returned and search 
the book. This uses OOP concepts along with file handling as well as try and except: error handling
'''
import csv
class Book:
    '''
    Class representing a book in the library.

    Attributes:
    book_id : Unique identifier for the book, datatype = int
    title: Title of the book, dataatype = str
    auth : Author of the book, datatype = str
    is_issued : Whether the book is currently issued or available, datatype = bool
    '''
    def __init__(self, book_id, title, auth, is_issued=False):
        self.book_id = book_id
        self.title = title
        self.auth = auth
        self.is_issued = is_issued

    def to_csv_row(self):
        return [self.book_id, self.title, self.auth, str(self.is_issued)]
    
    @classmethod
    def from_csv_row(cls, row):
        book_id, title, auth, issued_str = row
        is_issued = issued_str.strip().lower() == "true"
        return cls(book_id, title, auth, is_issued)
    
    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"BookID: {self.book_id}, Title: {self.title}, Author: {self.auth}, Status: {status}"

class Library:
    def __init__(self, filename):
        self.filename = filename

    def load_books(self):
        """
        Load books from the CSV file.
        Returns a list of Book objects. If the file doesn't exist, returns an empty list.
        """
        books = []
        try:
            with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                
                header = next(reader, None)
                for row in reader:
                    if row:  
                        book = Book.from_csv_row(row)
                        books.append(book)
        except FileNotFoundError:
            print("Books file not found. A new file will be created on saving.")
        except Exception as e:
            print("Error loading books:", e)
        return books

    def save_books(self, books):
        """
        Save the list of Book objects to the CSV file.
        """
        try:
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                
                writer.writerow(["Book ID", "Title", "Author", "Is Issued"])
                for book in books:
                    writer.writerow(book.to_csv_row())
        except Exception as e:
            print("Error saving books:", e)

    def issue_books(self, book_id):
        """
        Marks the specified book as issued if it is available.
        """
        books = self.load_books()
        found = False
        for book in books:
            if book.book_id.lower() == book_id.lower():
                found = True
                if not book.is_issued:
                    book.is_issued = True
                    print(f"Book '{book.title}' has been issued.")
                else:
                    print(f"Book '{book.title}' is already issued.")
                break
        if not found:
            print("Book not found.")
        self.save_books(books)

    def return_book(self, book_id):
        """
        Marks the specified book as returned (available) if it was issued.
        """
        books = self.load_books()
        found = False
        for book in books:
            if book.book_id.lower() == book_id.lower():
                found = True
                if book.is_issued:
                    book.is_issued = False
                    print(f"Book '{book.title}' has been returned.")
                else:
                    print(f"Book '{book.title}' was not issued.")
                break
        if not found:
            print("Book not found.")
        self.save_books(books)

    def search_book(self, keyword):
        """
        Searches for books with the keyword in Book ID, Title, or Author.
        """
        books = self.load_books()
        results = []
        keyword = keyword.lower()
        for book in books:
            if (keyword in book.book_id.lower() or 
                keyword in book.title.lower() or 
                keyword in book.auth.lower()):
                results.append(book)
        if results:
            print("\nSearch Results:")
            for book in results:
                print(book)
        else:
            print("No matching books found.")

filename = "books.csv"
library = Library(filename)
    
if not library.load_books():
    print("No books were found in the library. Adding sample books...")
    s_books = [Book("1", "The Pursuit of Happyness", "Chris Gardner"),
        Book("2", "Rita Hayworth and Shawshank Redemption", "Stephen King"),
        Book("3", "Forrest Gump", "Winston Groom")
    ]
    library.save_books(s_books)

    
while True:
    print("\n=== Library Book Management ===")
    print("1. Issue the books")
    print("2. Return books")
    print("3. Search books")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
        
    if choice == "1":
        book_id = input("Enter the Book ID to issue: ")
        library.issue_books(book_id)
    elif choice == "2":
        book_id = input("Enter the Book ID to return: ")
        library.return_book(book_id)
    elif choice == "3":
        keyword = input("Enter keyword to search (Book ID, Title, or Author): ")
        library.search_book(keyword)
    elif choice == "4":
        print("Exiting the System.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
