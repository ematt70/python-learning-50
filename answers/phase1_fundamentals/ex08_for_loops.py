"""
Exercise 08 — For Loops & Ranges

Task:
    Print all even numbers from 1 to 100.
"""

def print_even_numbers(limit):
    for n in range(1, limit + 1):
        if n % 2 == 0:
            print(n)

def main():
    print_even_numbers(100)

if __name__ == "__main__":
    main()
