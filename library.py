from random import choice 
 from turtle import title

class Boo
    def init(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.borrowed = False

    def str(self):
        status = "Borrowed" if self.borrowed else "Available"
        return f"Title: {self.title}, Author: {self.author}, ID: {self.book_id}, Status: {status}"

class Member:
    def init(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.borrowed:
            book.borrowed = True
            self.borrowed_books.append(book)
            print(f"book '{book.title}' borrowed successfully.")
        else:
            print("book is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.borrowed = False
            self.borrowed_books.remove(book)
            print("book returned successfully.")
        else:
            print("you did not borrow this book.")

class Library:
    def init(self):
        self.books = []
        self.members = []

    def add_book(self, title, author, book_id):
        new_book = Book(title, author, book_id)
        self.books.append(new_book)
        print("book added successfully.")

    def add_member(self, name, member_id):
        new_member = Member(name, member_id)
        self.members.append(new_member)
        print("member added successfully.")

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
    def display_books(self):
        if not self.books:
            print("no books in the library.")
        else:
            for book in self.books:
                print(book)

my_library = Library()

while True:
    print("\n===== library menu =====")
    print("1. Add book")
    print("2. Add member")
    print("3. Display books")
    print("4. Borrow book")
    print("5. Return book")
    print("6. Exit")

    choice = input("enter an option: ")

    if choice == "1":
        title = input("enter book title: ")
        author = input("enter book author: ")
        book_id = input("enter book ID: ")
        my_library.add_book(title, author, book_id)

    elif choice == "2":
        name = input("enter member name: ")
        member_id = input("enter member id: ")
        my_library.add_member(name, member_id)

    elif choice == "3":
        my_library.display_books()

    elif choice == "4":
        book_id = input("enter book id: ")
        member_id = input("enter member ID: ")
        book = my_library.find_book(book_id)
        member = my_library.find_member(member_id)
        if book and member:
            member.borrow_book(book)
        else:
            print("book or member not found.")

    elif choice == "5":
        book_id = input("enter book ID: ")
        member_id = input("enter member ID: ")
        book = my_library.find_book(book_id)
        member = my_library.find_member(member_id)
        if book and member:
            member.return_book(book)
        else:
            print("book or member not found.")

    elif choice == "6":
        print("goodbye!")
        break
    else:
        print("invalid option. please try again.")