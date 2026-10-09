"""
Exercise 17 — Dictionary Methods

Task:
    Practice:
        - keys()
        - values()
        - items()
        - get()

Instructions:
    - Print each method result.
    - Use get() with a default value.

Expected Output:
    Keys: ['name', 'age', 'city']
    Values: ['Erich', 42, 'Davenport']
    Items: [('name', 'Erich'), ('age', 42), ('city', 'Davenport')]
    Get name: Erich
    Get country: Unknown
"""

def main():
    # Write your code below:
    personDict = {
        "name": "Erich",
        "age": "42",
        "city": "Davenport"
    }

    print(f"Keys: {personDict.keys()}")
    print(f"Values: {personDict.values()}")
    print(f"Items: {personDict.items()}")
    print(f"Get name: {personDict.get("name")}")
    print(f"Get country: {personDict.get("country", "Unknown")}")


if __name__ == "__main__":
    main()
