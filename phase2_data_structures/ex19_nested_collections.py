"""
Exercise 19 — Nested Collections

Task:
    Create a list of dictionaries representing users.
    Print all users.
    Then print only users age >= 30.

Instructions:
    - Loop through the list.
    - Access fields with user["key"].

Expected Output:
    All users:
    {'name': 'Alice', 'age': 25}
    {'name': 'Bob', 'age': 35}
    {'name': 'Charlie', 'age': 30}

    Users age >= 30:
    {'name': 'Bob', 'age': 35}
    {'name': 'Charlie', 'age': 30}
"""

def main():
    # Write your code below:
    usersList = [
        {
            'name': 'Alice',
            'age': 25,
        },
        {
            'name': 'Bob',
            'age': 35,
        },
        {
            'name': 'Charlie',
            'age': 30,
        },
    ]
    oldUsers = []

    print("All users:")
    for user in usersList:
        print(user)
        if(user.get('age') >= 30):
            oldUsers.append(user)

    print(f"\nUsers age >= 30:")
    for user in oldUsers:
        print(user)
        
if __name__ == "__main__":
    main()
