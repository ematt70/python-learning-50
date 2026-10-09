"""
Exercise 16 — Dictionaries Intro

Task:
    Create a dictionary representing a person with:
        - name
        - age
        - city

Instructions:
    - Access values using person["key"].
    - Print each field.

Expected Output:
    Name: Erich
    Age: 42
    City: Davenport
"""

def main():
    # Write your code below:
    personDict = {
        "name": "Erich",
        "age": "42",
        "city": "Davenport"
    }

    print(f"Name: {personDict["name"]}")
    print(f"Age: {personDict["age"]}")
    print(f"City: {personDict["city"]}")
          

if __name__ == "__main__":
    main()
