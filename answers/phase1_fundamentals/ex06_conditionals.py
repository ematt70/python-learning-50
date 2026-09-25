"""
Exercise 06 — Conditionals

Task:
    Ask the user for an integer and:
        - Print whether it is positive, negative, or zero.
        - Print whether it is even or odd.
"""

def describe_number(n):
    if n > 0:
        sign = "Positive"
    elif n < 0:
        sign = "Negative"
    else:
        sign = "Zero"

    parity = "Even" if n % 2 == 0 else "Odd"
    return sign, parity

def main():
    n = int(input("Enter an integer: "))
    sign, parity = describe_number(n)
    print(sign)
    print(parity)

if __name__ == "__main__":
    main()
