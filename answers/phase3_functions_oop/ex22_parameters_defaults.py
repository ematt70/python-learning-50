"""
Exercise 22 — Parameters & Default Arguments

Task:
    Write a function greet(name, greeting="Hello") that prints a greeting.
    Demonstrate calling it with:
        - Only a name
        - A name and a custom greeting
"""

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

def main():
    greet("Erich")
    greet("Erich", "Welcome")

if __name__ == "__main__":
    main()
