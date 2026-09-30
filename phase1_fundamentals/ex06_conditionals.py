"""
Exercise 06 — Conditionals

Task:
    Ask the user for an integer and:
        - Print whether it is positive, negative, or zero.
        - Print whether it is even or odd.

Instructions:
    - Use if/elif/else.
    - Use modulo (%) to check even/odd.

Expected Output:
    Positive
    Even
"""

def main():
    # Write your code below:
    number = int(input("Please enter a number: "))

    if number > 0:
        print("The number you entered is positive.")
    elif number < 0:
        print("The number you entered is negative.")
    else:
        print("The number you entered is zero.")

    if number % 2 == 0:
        print("The number you entered is even.")
    else:
        print("The number you entered is odd.")

if __name__ == "__main__":
    main()
