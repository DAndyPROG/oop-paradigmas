import re

class Book:
    total_copies = 0  

    def __init__(self, title, author, isbn, copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__copies = copies
        Book.update_total_copies(copies)

    @property
    def copies(self):
        return self.__copies

    @copies.setter
    def copies(self, value):
        if value >= 0:
            self.__copies = value
        else:
            raise ValueError("Number of copies cannot be negative")

    @classmethod
    def update_total_copies(cls, amount):
        cls.total_copies += amount

    @staticmethod
    def validate_isbn(isbn):
        pattern = r"^(97(8|9))?\d{9}(\d|X)$"
        return bool(re.match(pattern, isbn.replace("-", "")))

    def check_availability(self):
        return self.__copies > 0

    def update_copies(self, amount):
        if self.__copies + amount >= 0:
            self.__copies += amount
        else:
            raise ValueError("Not enough copies to update")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

class Customer(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.check_availability():
            book.update_copies(-1)
            self.borrowed_books.append(book)
        else:
            raise Exception("Book not available")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.update_copies(1)
            self.borrowed_books.remove(book)
        else:
            raise Exception("This book was not borrowed by the user")

class Employee(User):
    def __init__(self, name, user_id, library, salary):
        super().__init__(name, user_id)
        self._salary = salary 
        self.library = library

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self._salary = value
        else:
            raise ValueError("Salary cannot be negative")

    def add_book(self, book):
        self.library.books.append(book)
        Book.update_total_copies(book.copies)

    def remove_book(self, book):
        if book in self.library.books:
            self.library.books.remove(book)
            Book.update_total_copies(-book.copies)
        else:
            raise Exception("Book not found in the library")

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def register_user(self, user):
        self.users.append(user)

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def list_available_books(self):
        available_books = [book for book in self.books if book.check_availability()]
        return available_books

library = Library()

book1 = Book("Harry Potter", "J.Rowling", "978-0-452-28423-4", 5)
book2 = Book("Grokking Algorythms", "Aditya Y. Bhargava", "978-0-06-085052-4", 3)

employee = Employee("Alice Smith", "EMP001", library, 50000)
employee.add_book(book1)
employee.add_book(book2)

customer = Customer("Michel Couldbe", "CUST123")
library.register_user(customer)

print("Available books:", [book.title for book in library.list_available_books()])

customer.borrow_book(book1)
print(f"Customer {customer.name} borrowed '{book1.title}'")

print("Available books after borrowing:", [book.title for book in library.list_available_books()])

customer.return_book(book1)
print(f"Customer {customer.name} returned '{book1.title}'")

print("Available books after returning:", [book.title for book in library.list_available_books()])

print("Is ISBN valid:", Book.validate_isbn("978-0-452-28423-4"))

print("Total copies of all books:", Book.total_copies)
