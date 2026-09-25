"""
Exercise 10 — Mini-Project: Simple Calculator

Task:
    Build a command-line calculator that:
        - Asks the user to choose an operation (+, -, *, /)
        - Asks for two numbers
        - Prints the result
        - Repeats until the user quits
"""

def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError("Unknown operation.")

def main():
    while True:
        print("\nSimple Calculator")
        print("Operations: +, -, *, / or q to quit")
        op = input("Choose operation: ").strip()

        if op.lower() == "q":
            print("Goodbye!")
            break

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = calculate(a, b, op)
            print("Result:", result)
        except ValueError as e:
            print("Error:", e)
        except ZeroDivisionError as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
