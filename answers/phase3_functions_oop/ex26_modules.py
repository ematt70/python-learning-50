"""
Exercise 26 — Importing Modules

Task:
    Create two modules:
        - helpers.py containing a function add(a, b)
        - This file (ex26_modules.py) should import helpers and call add()
"""

import helpers

def main():
    result = helpers.add(2, 3)
    print(result)

if __name__ == "__main__":
    main()
