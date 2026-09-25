"""
Exercise 13 — Looping Over Lists

Task:
    Loop through a list and print each item with its index.
"""

def main():
    shopping_list = ["milk", "eggs", "bread", "coffee"]
    for index, item in enumerate(shopping_list):
        print(f"{index}: {item}")

if __name__ == "__main__":
    main()
