"""
Exercise 03 — User Input

Task:
    Ask the user for their name and age.
    Print a greeting that includes both.

Instructions:
    - Use input() to read from the user.
    - Convert age to int using int().
    - Build a formatted string using f-strings.

Expected Interaction:
    Enter your name: Erich
    Enter your age: 42
    Hello Erich, you are 42 years old!
"""

from unicodedata import name


def main():
    # Write your code below:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    print(f"Hello {name}, you are {age} years old!")

if __name__ == "__main__":
    main()
