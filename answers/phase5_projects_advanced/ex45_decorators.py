"""
Exercise 45 — Decorators

Task:
    Create a decorator that logs:
        - Function name
        - Execution time
"""

import time

def log_time(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Took {end - start:.2f} seconds")
        return result
    return wrapper

@log_time
def slow_function():
    time.sleep(1)

def main():
    slow_function()

if __name__ == "__main__":
    main()
