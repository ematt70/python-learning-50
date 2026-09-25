"""
Exercise 14 — List Comprehensions

Task:
    Create:
        - A list of squares from 1 to 10
        - A list of even squares only
"""

def main():
    squares = [n ** 2 for n in range(1, 11)]
    even_squares = [n for n in squares if n % 2 == 0]

    print("Squares:", squares)
    print("Even squares:", even_squares)

if __name__ == "__main__":
    main()
