"""
Exercise 09 — Nested Logic

Task:
    Ask the user for a grid size and print a grid of '*' characters.
"""

def print_grid(size):
    for _ in range(size):
        print("* " * size)

def main():
    size = int(input("Enter grid size: "))
    print_grid(size)

if __name__ == "__main__":
    main()
