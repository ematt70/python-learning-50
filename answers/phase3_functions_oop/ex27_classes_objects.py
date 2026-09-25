"""
Exercise 27 — Classes & Objects

Task:
    Create a Book class with:
        - title
        - author
        - year
    Add a method describe() that prints the book info.
"""

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def describe(self):
        print(f"'{self.title}' by {self.author} ({self.year})")

def main():
    book = Book("Dune", "Frank Herbert", 1965)
    book.describe()

if __name__ == "__main__":
    main()
