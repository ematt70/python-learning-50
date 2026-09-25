"""
Exercise 19 — Nested Collections

Task:
    Create a list of dictionaries representing users.
    Print all users.
    Then print only users age >= 30.
"""

def main():
    users = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 35},
        {"name": "Charlie", "age": 30},
    ]

    print("All users:")
    for user in users:
        print(user)

    print("\nUsers age >= 30:")
    for user in users:
        if user["age"] >= 30:
            print(user)

if __name__ == "__main__":
    main()
