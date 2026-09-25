"""
Exercise 35 — Exception Handling

Task:
    Build a safe division function that:
        - Catches ValueError (bad input)
        - Catches ZeroDivisionError
        - Always prints a final message
"""

def safe_division():
    try:
        a = float(input("Enter a number: "))
        b = float(input("Enter another number: "))
        print("Result:", a / b)
    except ValueError:
        print("Error: Invalid number.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    finally:
        print("Done.")

def main():
    safe_division()

if __name__ == "__main__":
    main()
