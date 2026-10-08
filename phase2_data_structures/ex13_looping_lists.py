"""
Exercise 13 — Looping Over Lists

Task:
    Loop through a list and print each item with its index.

Instructions:
    - Use enumerate() to get index + value.
    - Print in the format: "0: milk".

Expected Output:
    0: milk
    1: eggs
    2: bread
    3: coffee
"""

def main():
    # Write your code below:
    groceryList = ['milk', 'eggs', 'bread', 'coffee']

    for index, groceryItem in enumerate(groceryList):
        print(f"{index}: {groceryItem}")

if __name__ == "__main__":
    main()
