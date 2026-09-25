"""
Exercise 29 — Dunder Methods

Task:
    Create a Vector class that:
        - Stores x and y
        - Implements __str__
        - Implements __eq__
        - Implements __len__ (length rounded down)
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

def main():
    v1 = Vector(3, 4)
    v2 = Vector(3, 4)

    print(v1)
    print(v1 == v2)
    print(len(v1))

if __name__ == "__main__":
    main()
