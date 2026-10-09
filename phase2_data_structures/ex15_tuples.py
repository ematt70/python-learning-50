"""
Exercise 15 — Tuples

Task:
    Create a tuple representing (x, y) coordinates.
    Unpack the tuple into x and y variables.

Instructions:
    - Use tuple unpacking: x, y = point.
    - Print both values.

Expected Output:
    Point: (3, 7)
    x: 3
    y: 7
"""

def main():
    # Write your code below:
    myTuple = (3, 7)
    x, y = myTuple

    print(f"Point: {myTuple}")
    print(f"x: {x}")
    print(f"y: {y}")

if __name__ == "__main__":
    main()
