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
"""

def compute_values(a, b):
    return {
        "sum": a + b,
        "difference": a - b,
        "product": a * b,
        "quotient": a / b,
        "floor_division": a // b,
        "exponent": a ** b,
    }

def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    results = compute_values(a, b)

    print("Sum:", results["sum"])
    print("Difference:", results["difference"])
    print("Product:", results["product"])
    print("Quotient:", results["quotient"])
    print("Floor division:", results["floor_division"])
    print("Exponent:", results["exponent"])

if __name__ == "__main__":
    main()
