"""
Exercise 25 — Lambda Functions

Task:
    Use a lambda function to sort a list of dictionaries by "age".
"""

def main():
    people = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
    ]
    sorted_people = sorted(people, key=lambda p: p["age"])
    print(sorted_people)

if __name__ == "__main__":
    main()
