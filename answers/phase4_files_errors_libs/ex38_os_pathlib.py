"""
Exercise 38 — os & pathlib

Task:
    List all files in the current directory.
    Then list only .py files.
"""

from pathlib import Path

def list_all_files():
    print("All files:")
    for p in Path(".").iterdir():
        print(p.name)

def list_python_files():
    print("\nPython files:")
    for p in Path(".").iterdir():
        if p.suffix == ".py":
            print(p.name)

def main():
    list_all_files()
    list_python_files()

if __name__ == "__main__":
    main()
