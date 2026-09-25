"""
Exercise 24 — Scope & LEGB Rule

Task:
    Demonstrate Python's scope rules by:
        - Creating a global variable
        - Creating a function that defines a local variable
        - Printing both inside and outside the function
"""

x = 10  # global variable

def show_scope():
    local = 5
    print(f"Inside function: local={local}, global={x}")

def main():
    show_scope()
    print(f"Outside function: global={x}")

if __name__ == "__main__":
    main()
