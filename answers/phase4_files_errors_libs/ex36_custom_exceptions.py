"""
Exercise 36 — Custom Exceptions

Task:
    Create a custom exception called NegativeNumberError.
    Write a function that raises it if the user enters a negative number.
"""

class NegativeNumberError(Exception):
    pass

def check_number(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    print("Valid number:", n)

def main():
    try:
        num = int(input("Enter a number: "))
        check_number(num)
    except NegativeNumberError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
