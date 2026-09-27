"""
Exercise 02 — Variables & Types

Task:
    Create variables of type int, float, str, and bool.
    Print each variable and its type.

Instructions:
    - Use type() to inspect variable types.
    - Change values and re-run to see different results.

Expected Output (example):
    42 <class 'int'>
    3.14 <class 'float'>
    Hello <class 'str'>
    True <class 'bool'>
"""

def main():
    # Write your code below:
    var_int = 42
    var_float = 3.14
    var_str = "Hello"
    var_bool = True

    print(var_int, type(var_int))
    print(var_float, type(var_float))
    print(var_str, type(var_str))
    print(var_bool, type(var_bool))

if __name__ == "__main__":
    main()
