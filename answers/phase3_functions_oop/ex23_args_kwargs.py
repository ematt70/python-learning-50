"""
Exercise 23 — *args and **kwargs

Task:
    Write a function debug_print(*args, **kwargs) that:
        - Prints all positional arguments
        - Prints all keyword arguments
"""

def debug_print(*args, **kwargs):
    for arg in args:
        print("Positional:", arg)
    for key, value in kwargs.items():
        print(f"Keyword: {key}={value}")

def main():
    debug_print(1, 2, 3, a=10, b=20)

if __name__ == "__main__":
    main()
