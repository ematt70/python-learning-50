"""
Exercise 30 — Mini-Project: Library System

Task:
    Build a simple library catalog using classes:
        - Book class (title, author, year)
        - Library class with:
            - add_book()
            - list_books()
            - find_book(title)
"""

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def describe(self):
        print(f"'{self.title}' by {self.author} ({self.year})")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Title: ")
        author = input("Author: ")
        year = input("Year: ")
        self.books.append(Book(title, author, year))
        print("Book added.")

    def list_books(self):
        if not self.books:
            print("No books.")
            return
        for book in self.books:
            book.describe()

    def find_book(self):
        title = input("Search title: ")
        for book in self.books:
            if book.title.lower() == title.lower():
                book.describe()
                return
        print("Not found.")

def main():
    lib = Library()
    while True:
        print("\n1) Add  2) List  3) Find  4) Quit")
        choice = input("Choose: ")

        if choice == "1":
            lib.add_book()
        elif choice == "2":
            lib.list_books()
        elif choice == "3":
            lib.find_book()
        elif choice == "4":
            break
        else:
            print("Invalid.")

if __name__ == "__main__":
    main()
