"""
Exercise 46 — Generators

Task:
    Create a generator that yields Fibonacci numbers.
"""

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def main():
    gen = fibonacci()
    for _ in range(10):
        print(next(gen), end=" ")
    print()

if __name__ == "__main__":
    main()
