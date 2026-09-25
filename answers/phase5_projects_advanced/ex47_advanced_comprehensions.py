"""
Exercise 47 — Advanced Comprehensions

Task:
    Create:
        - A dict comprehension mapping numbers to squares
        - A set comprehension of even squares
        - A nested list comprehension (3x3 grid)
"""

def main():
    squares = {n: n*n for n in range(1, 4)}
    even_squares = {n*n for n in range(1, 11) if (n*n) % 2 == 0}
    grid = [[col for col in range(1, 4)] for _ in range(3)]

    print(squares)
    print(even_squares)
    print(grid)

if __name__ == "__main__":
    main()
