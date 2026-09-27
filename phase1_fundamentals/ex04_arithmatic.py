"""
Exercise 04 — Basic Arithmetic

Task:
    Ask the user for two numbers and print:
        - Sum
        - Difference
        - Product
        - Quotient
        - Floor division
        - Exponent

Instructions:
    - Convert input to float.
    - Use arithmetic operators: +, -, *, /, //, **.

Expected Output:
    Sum: 7
    Difference: 3
    Product: 10
    Quotient: 2.5
    Floor division: 2
    Exponent: 32
"""

def main():
    # Write your code below:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    print(f"Sum: {number1 + number2:.0f}")
    print(f"Difference: {number1 - number2:.0f}")
    print(f"Product: {number1 * number2:.0f}")
    print(f"Quotient: {number1 / number2:.1f}")
    print(f"Floor division: {number1 // number2:.0f}")
    print(f"Exponent: {number1 ** number2:.0f}")

if __name__ == "__main__":
    main()
