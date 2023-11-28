class Book:
    def __init__(self, title, author, price, genre, quantity):
        self.title = title
        self.author = author
        self.price = price
        self.genre = genre
        self.quantity = quantity

class BookStore:
    books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():   
                self.books.remove(book)
                print(f"Book '{title}' removed successfully.")
                return
        print(f"Book '{title}' not found in the inventory.")

    def search_by_title(self, title):
        book_found = False
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"Name: {book.title}")
                book_found = True
        if not book_found:
            print("Book not found.")

    def search_by_author(self, author):
        book_found = False
        for book in self.books:
            if book.author.lower() == author.lower():
                print(f"Name: {book.author}")
                book_found = True
        if not book_found:
            print("Book not found.")

    def display_books(self):
        if self.books:
            for book in self.books:
                 print(f"Title: {book.title}, Author: {book.author} , genre{book.genre}, quantity{book.quantity}")
        else:
            print("No books in the inventory.")

class User:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.books_collection = []

    def buy_book(self, bookstore, title):
        for book in bookstore.books:
            if book.title.lower() == title.lower():
                self.books_collection.append(book)
                print(f"Book '{title}' added to the user's collection.")
                return
        print(f"Title: {book.title}, Author: {book.author}")

    def display_books_collection(self):
        if self.books_collection:
            for book in self.books_collection:
                print(f"Title: {book.title}, Author: {book.author} ")
        else:
            print("No books in the collection.")

def main():
    bookstore = BookStore()

    while True:
        print("Input a choice from the following options:")
        print("For adding a book, press 1")
        print("For removing a book, press 2")
        print("To search for a book by title, press 3")
        print("To search for a book by author name, press 4")
        print("To display books in the inventory, press 5")
        print("To enter user details, press 6")
        print("To quit the program, press 7")

        case = input("Select the case: ")

        if case == "1":
            title = input("The title of the book: ")
            Name = input("The author name of the book: ")
            genre= input("The genre of the book: ")
            price = int(input("The price of the book: "))
            quantity = int(input("The quantity of the book: "))

            book = Book(title, Name, price, genre, quantity)
            bookstore.add_book(book)

        elif case == "2":
            remove_book = input("Enter the title of the book: ")
            bookstore.remove_book(remove_book)

        elif case == "3":
            search_title = input("Enter the title for searching the book: ")
            bookstore.search_by_title(search_title)

        elif case == "4":
            search_author = input("Enter the author name for searching the book: ")
            bookstore.search_by_author(search_author)

        elif case == "5":
            bookstore.display_books()

        elif case == '6':
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            address = input("Enter your address: ")
            user = User(name, age, address)

            title_to_buy = input("Enter the title of the book you want to buy: ")
            user.buy_book(bookstore, title_to_buy)

            print("\nUser's Books Collection ")
            user.display_books_collection()

        elif case == "7":
            print("Quit the program.")
            break

        else:
            print("Invalid choice.")


main()



'''
class User:
    def __init__(self,name, age, adress):
        self.name = name
        self.age = age 
        self.adress = adress
        self.books_collection = []
    def buy_book(self , book):
        self.books_collection.append(book)
    def print_book_collection(self):
      for book in self.books_collection:
          print(book)       
class Book:
    def __init__(self , title , author , price):
        self.title = title
        self.author = author
        self.price = price 
Book_inventry = []


a = input("User NAme ")
b = input("Eter the Age of User ")
c = input("Adress of User ")
user =User(a,b,c)
print(f"Name: {user.name}")
print(f"Age: {user.age}")
print(f"Address: {user.adress}")
        
print(" Books in inventry :")
for book in Book_inventry :
    print(f"Title: {book.title}, Author: {book.author}, Price: {book.price}")


book_to_buy = Book_inventry[0]
user.buy_book(book_to_buy)
Book_inventry.remove(book_to_buy)

print("User's Book Collection:")
user.print_books_collection()


'''



