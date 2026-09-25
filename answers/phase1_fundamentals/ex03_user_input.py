"""
Exercise 03 — User Input

Task:
    Ask the user for their name and age.
    Print a greeting that includes both.
"""

def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(f"Hello {name}, you are {age} years old!")

if __name__ == "__main__":
    main()
