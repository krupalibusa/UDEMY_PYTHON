# Base class for a Book
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        return "'{}' by {} (ISBN: {})".format(self.title, self.author, self.isbn)

# Base class for a Member
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_borrowed:
            print("Sorry, '{}' is already borrowed.".format(book.title))
        else:
            self.borrowed_books.append(book)
            book.is_borrowed = True
            print("{} borrowed '{}'.".format(self.name, book.title))

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False
            print("{} returned '{}'.".format(self.name, book.title))
        else:
            print("{} doesn't have '{}' borrowed.".format(self.name, book.title))

# Derived class for a Student Member
class Student(Member):
    def __init__(self, name):
        super().__init__(name)
        self.borrow_limit = 3

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.borrow_limit:
            print("Sorry, {} has reached the borrow limit.".format(self.name))
        else:
            super().borrow_book(book)

# Derived class for a Faculty Member
class Faculty(Member):
    def __init__(self, name):
        super().__init__(name)
        self.borrow_limit = 5

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.borrow_limit:
            print("Sorry, {} has reached the borrow limit.".format(self.name))
        else:
            super().borrow_book(book)

# Class for Library
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print("Added book: '{}'".format(book.title))

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Removed book: '{}'".format(book.title))
        else:
            print("Book '{}' not found.".format(book.title))

    def add_member(self, member):
        self.members.append(member)
        print("Added member: {}".format(member.name))

    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)
            print("Removed member: {}".format(member.name))
        else:
            print("Member {} not found.".format(member.name))

    def list_books(self):
        print("Books in the library:")
        for index, book in enumerate(self.books):
            print("{}. {}".format(index + 1, book))

    def list_members(self):
        print("Members of the library:")
        for index, member in enumerate(self.members):
            print("{}. {}".format(index + 1, member.name))

# Example usage
library = Library()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
book2 = Book("1984", "George Orwell", "9876543210")
book3 = Book("To Kill a Mockingbird", "Harper Lee", "1122334455")
book4 = Book("Pride and Prejudice", "Jane Austen", "2233445566")
book5 = Book("The Catcher in the Rye", "J.D. Salinger", "3344556677")
book6 = Book("Moby-Dick", "Herman Melville", "4455667788")
book7 = Book("War and Peace", "Leo Tolstoy", "5566778899")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
library.add_book(book6)
library.add_book(book7)

student = Student("Alice")
faculty = Faculty("Dr. Smith")

library.add_member(student)
library.add_member(faculty)

def interactive_session(library):
    while True:
        print("\n1. Borrow a book")
        print("2. Return a book")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            borrow_book_interactive(library)
        elif choice == '2':
            return_book_interactive(library)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid number.")

def borrow_book_interactive(library):
    while True:
        library.list_members()
        member_choice = input("Enter the number of the member who wants to borrow a book (or 'exit' to go back): ")
        if member_choice.lower() == 'exit':
            break

        if not member_choice.isdigit() or int(member_choice) < 1 or int(member_choice) > len(library.members):
            print("Invalid choice. Please enter a valid number.")
            continue

        member = library.members[int(member_choice) - 1]

        library.list_books()
        book_choice = input("Enter the number of the book to borrow: ")
        if not book_choice.isdigit() or int(book_choice) < 1 or int(book_choice) > len(library.books):
            print("Invalid choice. Please enter a valid number.")
            continue

        book = library.books[int(book_choice) - 1]

        member.borrow_book(book)

def return_book_interactive(library):
    while True:
        library.list_members()
        member_choice = input("Enter the number of the member who wants to return a book (or 'exit' to go back): ")
        if member_choice.lower() == 'exit':
            break

        if not member_choice.isdigit() or int(member_choice) < 1 or int(member_choice) > len(library.members):
            print("Invalid choice. Please enter a valid number.")
            continue

        member = library.members[int(member_choice) - 1]

        print("Borrowed books:")
        for index, book in enumerate(member.borrowed_books):
            print("{}. {}".format(index + 1, book))

        book_choice = input("Enter the number of the book to return: ")
        if not book_choice.isdigit() or int(book_choice) < 1 or int(book_choice) > len(member.borrowed_books):
            print("Invalid choice. Please enter a valid number.")
            continue

        book = member.borrowed_books[int(book_choice) - 1]

        member.return_book(book)

# Start the interactive session
interactive_session(library)
